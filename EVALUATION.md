# Evaluation

Every number here comes from a command, a fixture under `eval/` and a result file under
`eval/results/` (`<name>_latest.json` is the most recent run of each). Re-run everything with
`make eval` (`headwater eval all`); the live tests run under the evaluation budget cap and
save a run with status `eval`, never `completed`. Numbers as of 2026-11-05, on the store
built by milestones 2 to 6 (seven packs, 90-day windows collected from 2026-08-04).

The labelled sets were written by the builder, not by a domain expert; where a label needed
knowledge the evidence does not show, the label is `unsure` and the case is reported but not
scored. Weak numbers are reported as they are.

## 1. Robotics backtest (`headwater eval backtest`, `eval/backtest_robotics.yaml`)

**Question.** Would the pipeline have surfaced companies that went on to announce a priced
round, before the announcement, from the data that existed at the time?

**Fixture.** 18 robotics and physical-AI companies that announced a round inside the window
the store covers: 10 from press announcements found by web search (the article is the
citation; pre-seed to venture rounds, 2026-08-09 to 2026-10-30) and 8 first-sale Form D
filings linked to the robotics pack (the EDGAR document is the citation; USD 1.8M to 57M,
2026-08-07 to 2026-10-21). Companies are matched to the store by normalised name, domain
and founders' names, so a founder who published before incorporating counts.

**Method.** The ordinary deterministic scorer runs in `backtest` mode as of each date:
artifacts published, signals observed and Form D filings filed on or before that date. Every
signal that is a level read at collection time has no history in this store and is therefore
absent from every as-of score: GitHub stars, forks, commits in window, contributors,
followers, public repos; Hugging Face downloads, likes, organisation counts; Hacker News
points and comments; job postings; OpenAlex citation and works counts. What remains is
publication dates, filing dates, affiliations, organisation age and thesis fit. Coverage
starts at the first collection window (2026-08-04); horizons before that are "no data".

**Result.**

| Horizon before the announcement | Companies with data | In the top 50 | Recall@50 |
|---|---|---|---|
| 4 weeks | 7 | 0 | 0.00 |
| 8 weeks | 4 | 0 | 0.00 |
| 12 weeks | 2 | 0 | 0.00 |

- 10 of 18 labelled companies exist in the store at all. The 8 press-sourced companies that
  do not (Tangent, Danu, Feather, Maven, Ultra, Reframe, Avatar, Corvus) were never collected
  by any source: no paper, repository, model, launch post or filing of theirs fell into the
  window's queries. Coverage of the funding universe, not ranking, is the first limit.
- The 8 Form D companies are in the store only because of their filing, and had nothing else:
  none was a candidate at any as-of date before its filing. A filing is a lagging signal and
  the pipeline has nothing earlier on these issuers.
- One company ranked before its round: Machenta (seed, 2026-10-27) through its founders'
  papers, at rank 242 of the robotics list four weeks before, and nothing earlier. Bleu
  Robotics' founders are in the store but tied to an academic organisation and so never
  seeded as candidates.
- Median lead time: none. No labelled company entered the top 50 before its announcement.

**Leakage risks, stated.** Triage labels were produced by the model after the as-of dates (a
classification of content, but with hindsight possible); entity merges and founder links
happened at collection time; `earliest_seen` of a Form D issuer was learned from the filing;
Form D companies are present only because of the filing. None of these risks flatters the
result above, which is zero.

**Reading.** Over a 13-week store with no signal history the backtest can only test
publication-and-filing timing, and on that alone the pipeline does not anticipate rounds.
The momentum components the scorer is built around (star velocity, download growth, launch
velocity) need a store that has run weekly for months; this backtest should be re-run once
`github_stars_cum` and the other series have history, and after the weekly runs have recorded
star counts for a few weeks, since GitHub withholds stargazer timestamps from personal access
tokens and velocity is computed from Headwater's own observations.

## 2. Sanity evaluation, every pack (`headwater eval sanity`, `eval/sanity/<pack>.yaml`)

All seven packs have a completed run with no failures and no budget skips.

| Pack | Candidates | Top 25 carrying the pack's own vocabulary | Labelled companies in the store | Cost of the run |
|---|---|---|---|---|
| AI infrastructure | 808 | 23 | 1 of 9 | $2.87 |
| Robotics and physical AI | 1,216 | 19 | 1 of 10 | $1.72 |
| Energy | 151 | 22 | 0 of 9 | $2.82 |
| Defense and dual-use | 51 | 17 | 0 of 9 | $2.39 |
| Vertical AI | 226 | 16 | 0 of 9 | $2.86 |
| Fintech and market structure | 103 | 14 | 0 of 8 | $2.60 |
| Sports, gaming and consumer | 174 | 9 | 0 of 8 | $1.16 |

"Carrying the pack's vocabulary" means at least one of the pack's include phrases and none
of its exclude phrases in the candidate's name, summary and artifact titles; it is a
deterministic plausibility check, not a judgement of quality. Overall 120 of 175 (0.69).

- The labelled companies (Figure, Anduril, Commonwealth Fusion, Modal, Polymarket, Harvey
  and their peers) are established companies: 2 of 62 are in the store and none is a
  candidate. This is by design (candidates are pre-formation teams and organisations with
  artifacts in a 90-day window, anchors excluded), and it says the packs run; it does not say
  they would have found those companies early. The backtest above is the test of that.
- The weak pack is sports, gaming and consumer: 16 of its top 25 carry none of the pack's
  vocabulary. They are game engines, Minecraft reimplementations and modding frameworks the
  triage model labelled relevant to "gaming" while the pack's phrases describe sports media,
  betting, fantasy, fitness and creator tools. Either the pack's keywords should name game
  development and engines, or its triage prompt should exclude them; a reviewer decision.
- Fintech (11 of 25 without vocabulary) and vertical AI (9 of 25) show the same gap in
  milder form: their candidates are plausible but their packs' phrase lists are narrow.

## 3. Precision flow (`headwater eval label`, `headwater eval precision`)

`headwater eval label --thesis <pack>` writes `exports/labels_<pack>_<date>.csv` with the
top 50 of the latest completed run (rank, name, kind, url, score, confidence, summary, the
brief's first sentence) and an empty `label` column; `headwater eval precision <csv>` computes
precision@10 and precision@25 from `1`/`0` (or yes/no) labels and says when the top k is not
fully labelled. The sheets exist for every pack; the labels are the reviewer's to fill, so no
precision number is claimed here.

## 4. Agent reliability

### 4.1 Triage agreement (`headwater eval triage`, `eval/triage_labels_robotics.yaml`)

66 robotics artifacts the model labelled (22 per label), re-labelled by the builder from the
title and type alone.

| | Model: relevant | Model: adjacent | Model: irrelevant |
|---|---|---|---|
| Human: relevant | 21 | 11 | 0 |
| Human: adjacent | 1 | 9 | 6 |
| Human: irrelevant | 0 | 2 | 16 |

Exact agreement 0.70, Cohen's kappa 0.55. For the binary question "relevant or not": precision
0.955, recall 0.656. The model is conservative: it never called an irrelevant artifact
relevant, and most disagreements are its `adjacent` where the human said `relevant` (VLA
policy repositories, world-action models, tactile sensing). Since adjacent artifacts still
reach the resolver and the scorer, the cost of that conservatism is a lower thesis-fit
component, not a missed candidate.

### 4.2 Resolver accuracy (`headwater eval resolver`, `eval/resolver_pairs.yaml`)

56 cases from the live review queue, labelled by the builder from the evidence each case
shows: 8 organisation name collisions (GitHub, Hugging Face and domain records of the same
name) and 48 paper-author versus GitHub-user pairs where the login spells the author's name.
Labels: 25 `same`, 1 `different`, 22 `unsure` (name-only evidence), 8 stale (a record was
merged by a later run, so the case no longer exists; set aside). Each case is re-judged by
the live resolver fallback and the merge policy of decision #27 is applied: `merge` needs
`same` at confidence 0.8 or more, `same` below that goes to review, `different` is rejected.

| Judged | Scored (same or different) | Correct | Accuracy | Auto-merges | Wrong auto-merges | To review | Rejected |
|---|---|---|---|---|---|---|---|
| 48 | 26 | 18 | 0.69 | 9 | 0 | 16 | 23 |

- Of the 25 pairs labelled `same`, the model said `same` for 17 and `different` for 8. The 8
  misses are name-plus-topic matches with no shared affiliation or repository in the
  records shown (three Bingxin Xu papers against a GitHub user who curates coding agents for
  robot learning, two Christian Rauch papers against the apriltag contributor); the model's
  reasoning names the match and declines it for lack of a hard link. Those pairs are
  rejected outright rather than queued, which is the cost of the policy: a `different`
  verdict never reaches a reviewer.
- Of the 17 it called `same`, 7 cleared the 0.8 bar and merged, 10 went to review at 0.5
  (the client caps confidence at 0.5 when the model cites no evidence id).
- Of the 22 `unsure` pairs the model said `same` for 8 (2 merged, 6 to review) and
  `different` for 14; no label exists to score them.
- No wrong auto-merge: the policy's precision held on this set. Its recall is the weak
  number: 7 of 25 true matches merged automatically, 10 more would need a reviewer's click.
- Cost: $0.14 the first time; the re-run after setting stale cases aside cost $0 from the
  response cache.

### 4.3 Verifier detection of seeded false statements (`headwater eval verifier`)

20 briefs whose sentences the verifier had accepted; in each, two supported fact sentences
were altered so their own evidence no longer supports them (13 numbers tripled, 9 years moved
back three years, 18 terms swapped for an opposite such as GitHub to GitLab or open-source to
closed-source), then the brief was verified again against the same evidence.

| Seeded false sentences | Detected | Labelled contradicted | Untouched supported sentences | False alarms | Judge score drop |
|---|---|---|---|---|---|
| 40 | 40 (1.00) | 40 | 124 | 7 (0.056) | 1.6 points |

Every seeded falsehood was caught and labelled `contradicted` rather than merely unsupported.
The price is 7 false alarms in 124 untouched sentences (in 6 of 20 briefs): sentences the
verifier had accepted once and rejected on a second reading. That is the verifier's own
run-to-run variance and the reason support rates in the reports sit at 85 to 92 percent
rather than 100. Cost $0.29.

### 4.4 Firm-fit conflict detection (`headwater eval firmfit`)

The seeded scenario of the tests, run against the live model: a launch post calls the
candidate "a direct competitor to Acme Robotics", a company on the firm's portfolio list.
Result: one flag, `conflict: Acme Robotics` at confidence 0.85, citing the planted record;
the fit paragraph has 3 sentences; no flag for a company outside the portfolio. Cost $0.02.
The same scenario passes offline with the model stubbed (deterministic mentions) and with a
scripted model (`tests/test_firmfit.py`, `tests/test_evaluation.py`).

## 5. Regression tests

131 tests run offline on recorded fixtures (`make test`): source parsers, HTTP replay,
store, resolver rules, scorer, every agent with scripted models, firm profiles and reports,
portfolio research, the dead-network behaviour, the evaluation suite and the dashboard
queries, the leak check with seeded leaks, the showcase generator, the demo site and the
architecture PDF. `ruff` and `mypy --strict` are clean.

## 6. What the numbers say, together

- The agents are reliable at what they are asked to do: the verifier catches every seeded
  falsehood, the firm-fit stage flags a planted competitor, triage never promotes the
  irrelevant, and the resolver never auto-merges a pair the builder labelled different.
- The ranking's predictive value is unproven. The backtest is zero on a store too young to
  hold the momentum history the scorer depends on, and the labelled companies of the sanity
  sets are the kind of company the pipeline is not built to find. The honest next step is
  weekly runs for a quarter, which also build the star-count series velocity needs, and the precision labels from the
  reviewer; then this file gets a second column.
- Pack vocabulary drifts from what the triage model admits, most visibly for sports and
  gaming. The sanity check now measures that gap per pack on every run.
