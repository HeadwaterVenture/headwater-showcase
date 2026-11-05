# Data policy

Headwater stores only the public professional information the ranking needs, and every
stored field carries the URL it came from. This document is the policy the code
implements; the data model (`src/headwater/models/`) and the source modules
(`src/headwater/sources/`) are the enforcement.

## Sources

Only public, documented APIs and public pages are used. Each source has a per-source
rate limit in code, an on-disk cache so nothing is fetched twice, and a descriptive
`User-Agent`.

| Source | What is fetched | Limits applied | Notes |
|---|---|---|---|
| arXiv API | paper metadata: title, abstract, authors, categories, dates, affiliations when present | 1 request / 3 s | Atom XML. Public preprints. |
| OpenAlex | work ids, citation counts, authorships, author profiles (institutions, counts by year) | ≤ 8 requests / s, polite pool with `mailto` | Public scholarly graph. |
| GitHub REST + GraphQL | public repos, topics, stars with timestamps, commits, contributor logins, organisation and user public profile fields (login, name, company, website, created date) | GitHub's published limits, conditional requests, backoff | Email addresses are never requested or stored. |
| Hugging Face Hub | public models, datasets, spaces, downloads, likes, organisation overview counts | ≤ 5 requests / s | |
| Hacker News (Algolia) | stories: title, URL, points, comments, author handle, date | ≤ 5 requests / s | |
| SEC EDGAR | Form D filings: issuer name, state, industry group, amounts, related persons and roles, filing date | ≤ 8 requests / s, `User-Agent` with contact email as the SEC requires | The issuer phone number in Form D is **not** stored. |
| Greenhouse, Lever, Ashby posting APIs | open job postings: title, department, location, dates | queried only for companies already resolved from other sources; board tokens are discovered from the company's own careers page, never guessed or brute-forced | |
| Firm websites | homepage, portfolio, thesis and team pages of a firm being profiled | robots.txt respected; only the pages needed | Used for firm profiles only (private). |
| Optional, behind flags | Semantic Scholar (needs key), SBIR.gov awards, Tranco rank, Product Hunt, Apple App Store RSS | skipped cleanly when disabled or unreachable | |

**Never used:** LinkedIn, X/Twitter, or any site whose terms forbid automated access.
No page is fetched in violation of its robots.txt.

## What is stored

- **Persons:** names and public handles (OpenAlex id, ORCID, GitHub login, Hugging Face
  handle), public professional affiliations with the page they were seen on, and an
  "anchor alumni" flag derived from those affiliations. Nothing else.
- **Organisations:** name, domain, GitHub and Hugging Face organisation handles,
  earliest public appearance, Form D filing facts, job board token, stage hints.
- **Artifacts, Signals, Evidence:** public items (papers, repos, models, posts, filings),
  dated measurements about them, and the exact fetched content behind each claim.

**Not collected, ever:** personal email addresses, phone numbers, home addresses, dates
of birth, photos, or private account data. Source modules strip these fields when an
API returns them (for example GitHub's `email`, Form D's `issuerPhoneNumber`).

## Traceability

Every Signal, Artifact, brief sentence and firm-fit paragraph cites an Evidence record
(URL, fetch time, content hash, excerpt). The store enforces this with foreign keys and
the Reporter refuses to render an uncited factual sentence.

## Retention and deletion

Everything lives in one SQLite file (`data/headwater.sqlite`) and the HTTP cache inside
it. Deleting a person or organisation is `DELETE` by id; the Evidence records remain
because they are copies of public pages, not personal records. The demo snapshot bundled
with the repository contains only the top-N candidates of one run.

## Confidentiality

Firm profiles (`private/firms/`) are derived from the firm's own public website, kept
out of version control, and used only to produce that firm's report. No firm name
appears in any shared artifact other than that firm's own report.
