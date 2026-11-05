"""HTTP client with rate limits.

Excerpt `http_client` from Headwater (`src/headwater/http/client.py`), extracted from a marked
region of the real source so it stays in sync. Shared for evaluation only; all rights
reserved; the full source is available for review on request."""

def _request_with_retries(
    self, source: str, url: str, headers: Mapping[str, str]
) -> tuple[httpx.Response, int]:
    stats = self._stats(source)
    last_exc: Exception | None = None
    if (
        self._offline_since is not None
        and self._clock() - self._offline_since < self.offline_probe_s - 1e-3  # fp drift
    ):
        stats.errors += 1
        raise NetworkUnavailable(url, self._offline_reason)
    for attempt in range(1, self.max_attempts + 1):
        self._throttle(source)
        started = self._clock()
        try:
            response = self._client.get(url, headers=dict(headers))
        except httpx.HTTPError as exc:  # network / timeout
            if self._network_works():
                # the network is fine, this host is the problem: no breaker count, and a
                # host that does not exist gets no retry, a slow one gets a single retry
                stats.errors += 1
                if _looks_like_no_such_host(exc):
                    raise HttpError(0, url, f"no such host ({str(exc)[:80]})") from exc
                if attempt >= 2:
                    raise HttpError(0, url, f"host not answering ({str(exc)[:80]})") from exc
                last_exc = exc
                stats.retries += 1
                self._sleep(self._backoff(attempt))
                continue
            last_exc = exc
            stats.retries += 1
            self._net_failures += 1
            if self._net_failures >= self.offline_after:
                self._offline_since = self._clock()
                self._offline_reason = str(exc)[:120]
                stats.errors += 1
                log.error(
                    "network unavailable, requests stopped",
                    extra={
                        "source": source,
                        "failures": self._net_failures,
                        "probe_s": self.offline_probe_s,
                        "error": self._offline_reason,
                    },
                )
                raise NetworkUnavailable(url, self._offline_reason) from exc
            wait = self._backoff(attempt)
            log.warning(
                "network error, retrying",
                extra={
                    "source": source,
                    "attempt": attempt,
                    "wait_s": round(wait, 1),
                    "error": str(exc)[:120],
                },
            )
            self._sleep(wait)
            continue
        self._net_failures, self._offline_since = 0, None
        self._last_good_host = httpx.URL(url).host or self._last_good_host
        elapsed_ms = int((self._clock() - started) * 1000)
        status = response.status_code
        if status == 429 or (
            status == 403 and response.headers.get("x-ratelimit-remaining") == "0"
        ):
            rl_wait = self._rate_limit_wait(response)
            if (
                rl_wait is None
                or rl_wait > self.max_rate_limit_wait_s
                or attempt == self.max_attempts
            ):
                stats.errors += 1
                raise HttpError(status, url, f"rate limited; wait {rl_wait}s exceeds cap")
            stats.retries += 1
            log.warning(
                "rate limited, waiting",
                extra={"source": source, "wait_s": round(rl_wait, 1), "attempt": attempt},
            )
            self._sleep(rl_wait)
            continue
        if status >= 500 and attempt < self.max_attempts:
            stats.retries += 1
            wait = self._backoff(attempt)
            log.warning(
                "server error, retrying",
                extra={"source": source, "status": status, "wait_s": round(wait, 1)},
            )
            self._sleep(wait)
            continue
        return response, elapsed_ms
    stats.errors += 1
    raise HttpError(0, url, f"gave up after {self.max_attempts} attempts: {last_exc}")

def _network_works(self) -> bool:
    """Can a host known to answer still be reached? Cached for ten seconds."""
    now = self._clock()
    if now - self._canary_checked_at < 10.0:
        return self._canary_ok
    self._canary_ok = self._canary(self._last_good_host or "example.com")
    self._canary_checked_at = now
    return self._canary_ok

def _throttle(self, source: str) -> None:
    limiter = self._limiters.get(source)
    if limiter is None:
        return
    now = self._clock()
    wait = 0.0
    if limiter.limit.min_interval_s and limiter.last_call:
        wait = max(wait, limiter.limit.min_interval_s - (now - limiter.last_call))
    if limiter.limit.max_per_window:
        while limiter.window and now - limiter.window[0] > limiter.limit.window_s:
            limiter.window.popleft()
        if len(limiter.window) >= limiter.limit.max_per_window:
            wait = max(wait, limiter.limit.window_s - (now - limiter.window[0]) + 0.05)
    if wait > 0:
        self._sleep(wait)
        now = self._clock()
    limiter.last_call = now
    limiter.window.append(now)

@staticmethod
def _backoff(attempt: int) -> float:
    return float(min(30.0, (2 ** (attempt - 1)) + random.uniform(0, 0.5)))
