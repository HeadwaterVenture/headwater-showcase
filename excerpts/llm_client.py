"""Budget-capped.

Excerpt `llm_client` from Headwater (`src/headwater/llm/client.py`), extracted from a marked
region of the real source so it stays in sync. Shared for evaluation only; all rights
reserved; the full source is available for review on request."""

def complete(
    self,
    stage: str,
    *,
    system: str,
    user: str,
    output_model: type[T],
    max_tokens: int | None = None,
    tag: str = "",
) -> LLMResult[T]:
    route = self.route(stage)
    max_tokens = max_tokens or route.max_tokens
    prompt_hash = self._prompt_hash(route, system, user, output_model, max_tokens)
    started = time.monotonic()
    content_hash = self._content_hash(stage, user, output_model)
    with self._lock:
        ready = self._before_call(
            stage,
            route,
            prompt_hash,
            content_hash,
            system,
            user,
            output_model,
            max_tokens,
            tag,
            started,
        )
    if isinstance(ready, LLMResult):
        return ready
    provider, price, reservation = ready
    return self._call(
        stage,
        route,
        prompt_hash,
        content_hash,
        system,
        user,
        output_model,
        max_tokens,
        tag,
        started,
        provider,
        price,
        reservation,
    )

def _before_call(
    self,
    stage: str,
    route: StageRoute,
    prompt_hash: str,
    content_hash: str,
    system: str,
    user: str,
    output_model: type[T],
    max_tokens: int,
    tag: str,
    started: float,
) -> LLMResult[T] | tuple[Provider, ModelPrice, Reservation]:
    """Cache hit, stub, or a budget reservation for a real call (under the lock)."""
    if self.use_cache:
        hit = self.store.llm_cache_get(prompt_hash)
        if hit is None and self.content_keyed:
            hit = self.store.llm_cache_get_by_content(content_hash)
        if hit is not None:
            try:
                output = output_model.model_validate_json(hit["text"])
            except ValidationError:
                output = None  # schema changed since caching; fall through to a fresh call
            if output is not None:
                rec = self._record(
                    stage, route, prompt_hash, outcome="cached", tag=tag, started=started
                )
                return LLMResult(
                    output=output,
                    stage=stage,
                    provider=str(hit.get("provider", route.provider)),
                    model=str(hit.get("model", route.model)),
                    cost_usd=0.0,
                    latency_ms=rec.latency_ms,
                    prompt_hash=prompt_hash,
                    call_id=rec.id,
                    cached=True,
                )

    provider = self.providers.get(route.provider)
    if provider is None:
        stub = self.stub_factory(stage, output_model) if self.stub_factory else None
        if stub is None:
            raise LLMUnavailable(
                f"stage '{stage}' needs provider '{route.provider}' (no key) and no cache entry"
            )
        rec = self._record(stage, route, prompt_hash, outcome="stub", tag=tag, started=started)
        return LLMResult(
            output=output_model.model_validate(stub.model_dump()),
            stage=stage,
            provider="stub",
            model=route.model,
            cost_usd=0.0,
            latency_ms=rec.latency_ms,
            prompt_hash=prompt_hash,
            call_id=rec.id,
            stubbed=True,
        )

    if self._unreachable is not None:
        raise LLMUnavailable(
            f"provider '{route.provider}' unreachable ({self._unreachable}); "
            "LLM calls stopped for this run"
        )

    price = self.models.price(route.model)
    estimate = estimate_call_cost_usd(
        price,
        prompt_chars=len(system) + len(user),
        max_tokens=max_tokens,
        chars_per_token=self.models.estimation.chars_per_token,
    )
    try:
        reservation = self.budget.reserve(stage, estimate, share=self.models.share(stage))
    except BudgetExhausted:
        self.budget.record_skip(stage, tag or prompt_hash[:12])
        self._record(
            stage, route, prompt_hash, outcome="budget_skipped", tag=tag, started=started
        )
        raise
    return provider, price, reservation
