# Scoring, illustrated

The ranking is deterministic: a weighted sum of six component scores, each between 0
and 1, each with its own explanation and the ids of the evidence behind it. No model
ranks. The weights below are the **illustrative defaults** shipped with the engine
(version `illustrative-1`); a firm's tuned weights are private
and are never part of this showcase.

| Component | Illustrative weight |
|---|---|
| momentum | +0.30 |
| founder quality | +0.25 |
| formation | +0.20 |
| thesis fit | +0.10 |
| consensus penalty | -0.10 |
| integrity | -0.05 |

- **momentum**: growth of stars, downloads, launch attention and hiring, z-scored
  against a robust baseline of the run's own candidates; acceleration counts for more
  than level, and without a time series the component is level-only and says so.
- **founder quality**: anchor affiliations, citation trajectory, shipped open source,
  prior exits.
- **formation**: a new organisation, a first Form D filing, a first job posting, a
  departure from an anchor.
- **thesis fit**: share of relevant artifacts and keyword coverage for the pack.
- **consensus penalty**: large rounds, press attention and incumbency make a candidate
  obvious; the penalty subtracts.
- **integrity**: young accounts, mirrors and inconsistent records subtract.

Every candidate's report entry shows the breakdown, the top three signals with links,
a confidence label and "what would change my mind".
