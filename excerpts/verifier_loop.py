"""The verifier loop over cited sentences.

Excerpt `verifier_loop` from Headwater (`src/headwater/agents/verifier.py`), extracted from a marked
region of the real source so it stays in sync. Shared for evaluation only; all rights
reserved; the full source is available for review on request."""

def verify_brief(
    ctx: RunContext, brief: Brief, *, system: str
) -> tuple[Brief, Verification] | None:
    """Label every checkable sentence, drop what is not supported, return the cleaned brief."""
    text, rows = render_brief_for_verification(ctx, brief)
    labels: list[VerificationLabel] = []
    model = "rule:missing-evidence"
    judge_score: float | None = None
    judge_notes = ""
    cost = 0.0
    cached = False
    needs_model = [r for r in rows if r[3]]
    if needs_model:
        try:
            result = ctx.llm.complete(
                "verifier",
                system=system,
                user=text,
                output_model=VerifierOut,
                tag=brief.candidate_id,
            )
        except (BudgetExhausted, LLMUnavailable, LLMProviderError):
            raise
        if result.stubbed:
            return None
        model, cost, cached = result.model, result.cost_usd, result.cached
        judge_score, judge_notes = result.output.judge_score, result.output.judge_notes
        decided = {(lo.section, lo.index): lo for lo in result.output.labels}
        for section, i, sent, _has_ev in needs_model:
            lo = decided.get((section, i))
            label = lo.label if lo is not None else "unsupported"
            note = lo.note if lo is not None else "no verdict returned for this sentence"
            labels.append(
                VerificationLabel(
                    section=section,
                    index=i,
                    sentence=sent.text,
                    label=label,
                    evidence_ids=sent.evidence_ids,
                    note=note,
                )
            )
    for section, i, sent, has_ev in rows:
        if not has_ev:
            labels.append(
                VerificationLabel(
                    section=section,
                    index=i,
                    sentence=sent.text,
                    label="unsupported",
                    evidence_ids=sent.evidence_ids,
                    note="cited evidence not in store",
                )
            )
    verdict = {(lab.section, lab.index): lab.label for lab in labels}
    removed: list[str] = []
    cleaned: dict[str, list[CitedSentence]] = {}
    for section, sentences in brief.sections().items():
        kept: list[CitedSentence] = []
        for i, sent in enumerate(sentences):
            if verdict.get((section, i), "supported") == "supported":
                kept.append(sent)
            else:
                removed.append(sent.text)
        cleaned[section] = kept
    factual = [lab for lab in labels]
    support_rate = (
        (sum(1 for lab in factual if lab.label == "supported") / len(factual)) if factual else 1.0
    )
    new_brief = brief.model_copy(update={**cleaned, "run_id": ctx.run_id})
    verification = Verification(
        candidate_id=brief.candidate_id,
        run_id=ctx.run_id,
        model=model,
        labels=labels,
        support_rate=round(support_rate, 4),
        judge_score=judge_score,
        judge_notes=judge_notes,
        removed=removed,
        created_at=utcnow(),
        cost_usd=cost,
        cached=cached,
    )
    return new_brief, verification
