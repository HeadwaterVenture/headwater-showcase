"""The budget with per-stage shares and reservations.

Excerpt `budget` from Headwater (`src/headwater/llm/budget.py`), extracted from a marked
region of the real source so it stays in sync. Shared for evaluation only; all rights
reserved; the full source is available for review on request."""

@dataclass
class Budget:
    cap_usd: float
    label: str = "run"
    spent_usd: float = 0.0
    reserved_usd: float = 0.0
    skipped: list[str] = field(default_factory=list)
    by_stage: dict[str, float] = field(default_factory=dict)
    reserved_by_stage: dict[str, float] = field(default_factory=dict)
    calls: int = 0

    @property
    def remaining_usd(self) -> float:
        return max(0.0, self.cap_usd - self.spent_usd - self.reserved_usd)

    def can_afford(self, amount_usd: float) -> bool:
        return amount_usd <= self.remaining_usd + 1e-9

    def reserve(self, stage: str, amount_usd: float, share: float = 1.0) -> Reservation:
        if not self.can_afford(amount_usd):
            raise BudgetExhausted(stage, amount_usd, self.remaining_usd, self.cap_usd)
        # the stage share counts calls in flight too, so parallel callers cannot all
        # squeeze through the gap between one reservation and its commit
        stage_cap = self.cap_usd * share
        used_here = self.by_stage.get(stage, 0.0) + self.reserved_by_stage.get(stage, 0.0)
        if used_here + amount_usd > stage_cap + 1e-9:
            raise BudgetExhausted(stage, amount_usd, max(0.0, stage_cap - used_here), stage_cap)
        self.reserved_usd += amount_usd
        self.reserved_by_stage[stage] = self.reserved_by_stage.get(stage, 0.0) + amount_usd
        return Reservation(stage=stage, amount_usd=amount_usd)

    def commit(self, reservation: Reservation, actual_usd: float) -> None:
        if reservation.settled:
            return
        self._unreserve(reservation)
        self.spent_usd += actual_usd
        self.by_stage[reservation.stage] = self.by_stage.get(reservation.stage, 0.0) + actual_usd
        self.calls += 1
        reservation.settled = True

    def release(self, reservation: Reservation) -> None:
        if reservation.settled:
            return
        self._unreserve(reservation)
        reservation.settled = True

    def _unreserve(self, reservation: Reservation) -> None:
        self.reserved_usd -= reservation.amount_usd
        left = self.reserved_by_stage.get(reservation.stage, 0.0) - reservation.amount_usd
        self.reserved_by_stage[reservation.stage] = max(0.0, left)

    def record_skip(self, stage: str, what: str) -> None:
        self.skipped.append(f"{stage}: {what}")

    def summary(self) -> dict[str, object]:
        return {
            "label": self.label,
            "cap_usd": round(self.cap_usd, 4),
            "spent_usd": round(self.spent_usd, 4),
            "remaining_usd": round(self.remaining_usd, 4),
            "calls": self.calls,
            "by_stage": {k: round(v, 4) for k, v in self.by_stage.items()},
            "skipped": list(self.skipped),
        }
