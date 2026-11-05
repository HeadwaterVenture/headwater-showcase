"""The Evidence data model.

Excerpt `evidence_model` from Headwater (`src/headwater/models/entities.py`), extracted from a marked
region of the real source so it stays in sync. Shared for evaluation only; all rights
reserved; the full source is available for review on request."""

class Evidence(BaseModel):
    """An immutable record of exactly what was fetched.

    Every Signal, Artifact and cited sentence points at one of these. The id is derived
    from the URL, the content hash and the excerpt, so the same item fetched twice is one
    record, changed content is a new record, and two items from one API page are two
    records that share a `raw_ref`.
    """

    id: str
    run_id: str
    source: str
    url: str
    fetched_at: datetime
    content_hash: str
    excerpt: str = Field(max_length=EXCERPT_MAX_CHARS)
    title: str | None = None
    display_url: str | None = None  # human-readable page for the same item, if different
    raw_ref: str | None = None  # key into the HTTP cache / fixture holding the full payload

    model_config = {"frozen": True}

    @classmethod
    def create(
        cls,
        *,
        run_id: str,
        source: str,
        url: str,
        content: str,
        excerpt: str | None = None,
        title: str | None = None,
        display_url: str | None = None,
        raw_ref: str | None = None,
        fetched_at: datetime | None = None,
    ) -> Evidence:
        digest = content_hash(content)
        snippet = (excerpt if excerpt is not None else content)[:EXCERPT_MAX_CHARS]
        return cls(
            id=stable_id("ev", url, digest, snippet),
            run_id=run_id,
            source=source,
            url=url,
            fetched_at=fetched_at or utcnow(),
            content_hash=digest,
            excerpt=snippet,
            title=title,
            display_url=display_url,
            raw_ref=raw_ref,
        )


class Signal(BaseModel):
    """A dated, sourced measurement about an entity (stars, downloads, points, filings...)."""

    id: str
    entity_type: EntityType
    entity_id: str
    type: str
    value: float
    observed_at: datetime
    source_url: str
    evidence_id: str
    run_id: str
    raw_ref: str | None = None
    note: str | None = None

    @classmethod
    def create(
        cls,
        *,
        entity_type: EntityType,
        entity_id: str,
        type: str,
        value: float,
        observed_at: datetime,
        source_url: str,
        evidence_id: str,
        run_id: str,
        raw_ref: str | None = None,
        note: str | None = None,
    ) -> Signal:
        return cls(
            id=stable_id("sig", entity_type, entity_id, type, observed_at.isoformat(), source_url),
            entity_type=entity_type,
            entity_id=entity_id,
            type=type,
            value=value,
            observed_at=observed_at,
            source_url=source_url,
            evidence_id=evidence_id,
            run_id=run_id,
            raw_ref=raw_ref,
            note=note,
        )
