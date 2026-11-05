# Headwater

Headwater is a venture sourcing agent. It collects public artifacts (papers, repositories,
models, launch posts, filings and job postings), resolves them to the people and
organisations behind them, ranks candidates with a deterministic and explainable score, and
uses language models only to classify, resolve ambiguity, summarise, assess fit against a
firm's thesis and verify. Every sentence in every output cites an Evidence record with its
source URL. It exists because early-stage sourcing is a data and attention race, and the
public record of who is building what is larger than any team reads.

This repository is the showcase: documents, numbers and a few code excerpts. The full
source lives in a private repository and is available for review on request.

## Architecture

See `ARCHITECTURE.md` for the diagrams. In one line: Scout collects, Triage classifies,
Resolve builds the entity graph, Score ranks deterministically, Analyst writes a cited brief,
Verifier checks every sentence and scores it against a rubric, Firm fit maps the ranked list
to a firm's stated thesis and researched portfolio, and the outputs are a thesis report, a
watermarked firm report, a CSV with stable ids and an internal dashboard.

The stages follow an observe, decide, act, improve loop: Scout and Triage observe, Resolve
and Score decide, Analyst and Firm fit act, Verifier and the evaluation suite improve the
next run.

## Scoring, in plain terms

A candidate's score is a weighted sum of six components, each between 0 and 1 and each
carrying its own explanation and evidence: momentum (growth of stars, downloads, launch
attention and hiring against a robust baseline), founder quality (anchor affiliations,
citation growth, shipped open source), formation (a first filing, a first job posting,
organisation age), thesis fit, a consensus penalty for what is already obvious, and
integrity of the record. The weights are a versioned configuration; the defaults in this
showcase are illustrative and a firm's tuned weights stay private. No model ranks.

## Reliability and backtest numbers

From `EVALUATION.md` (2026-11-05):

| Test | Result |
|---|---|
| Verifier, 40 seeded false statements in 20 accepted briefs | 40 of 40 detected, 7 false alarms in 124 untouched sentences |
| Firm fit, planted competitor of a portfolio company | flagged as a conflict at 0.85, citing the planted record |
| Triage, 66 hand-labelled artifacts | relevant precision 0.96, recall 0.66, kappa 0.55 |
| Resolver, 26 hand-labelled ambiguous pairs | accuracy 0.69, no wrong automatic merge |
| Robotics backtest, 18 companies that announced rounds | recall@50 of 0 at 4, 8 and 12 weeks on a thirteen-week store |
| Pack sanity, 7 packs | all run clean; 69 percent of top-25 candidates carry the pack's vocabulary |

## Known limitations

- The backtest is on a store too young to hold the momentum history the scorer relies on;
  it tests publication and filing timing only, and finds nothing. Weekly runs over a quarter
  are needed before the ranking's predictive value can be measured.
- Coverage of the funding universe is partial: eight of ten press-announced robotics rounds
  in the window were never collected by any source.
- GitHub withholds stargazer timestamps from personal access tokens, so star velocity is
  computed from the star counts the weekly runs record themselves; it needs at least a week
  of observations per repository, and the first runs score on star levels.
- Large sites that refuse non-browser clients stay unverified by design.
- Pack vocabularies drift from what the triage model admits; the sanity check measures the
  gap per pack.

## Code excerpts

Five excerpts under `excerpts/`, extracted from marked regions of the real source so they
stay in sync: the budget-capped model client, the budget itself, the verifier loop, the HTTP
client with rate limits, caching, record and replay, and the Evidence data model.

## Contact

Leon D. Bahner. headwaterventure@proton.me

All rights reserved; see `LICENSE` and `NOTICE`. Full source available for review on request.
