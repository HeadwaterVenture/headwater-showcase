<!-- Sample thesis report from a live run, included in the showcase for illustration.
Candidate names and links are public; paths and private references are removed. Only the ranks listed in showcase/allowlist.yaml are shown in full; the others are
withheld by policy. -->

# Headwater thesis report: Robotics and physical AI

*Run `run_20261103T180024_2e73` · as of 2026-11-03 · lookback 90 days · mode live*

## Run summary

| | |
|---|---|
| Sources queried | arxiv: 170 new, 2 requests, 0 cached; openalex: 91 new, 56 requests, 0 cached; github: 222 new, 279 requests, 186 cached; huggingface: 480 new, 108 requests, 8 cached; hn: 42 new, 6 requests, 0 cached; edgar: 0 new, 0 requests, 1 cached; sbir: 0 new, 0 requests, 0 cached; jobs: 0 new, 0 requests, 2 cached; github_search: 0 new, 24 requests, 0 cached; web: 0 new, 6 requests, 4 cached |
| Triage funnel | collected = 11262 → triaged = 10969 → triage_relevant = 2652 → triage_adjacent = 4203 → triage_irrelevant = 4114 → triage_llm_labelled = 409 → triage_llm_pending = 0 → organisations = 1947 → persons = 103606 → seeds = 1216 → excluded_anchor_academic = 42 → candidates = 1216 |
| LLM cost | $1.7177 of a $5.0000 cap |
| Verification rate | 85.5% · judge score 6.5/10 |
| Failures | none |

**Notices**

- incremental collection from 2026-10-30 (previous run run_20261102T221156_0e08); scoring still covers the full 90-day window
- github: star history skipped: fine-grained tokens cannot read stargazer timestamps; momentum uses star levels, commits and contributors (a classic token with no scopes enables star velocity)
- scorer excluded Google DeepMind: anchor organisation
- scorer excluded NVIDIA: anchor organisation
- scorer excluded NVlabs: anchor organisation
- scorer excluded thu-ml: academic
- scorer excluded LeCAR-Lab: academic
- scorer excluded cocel-postech: academic
- scorer excluded showlab: academic
- scorer excluded XPolicyLab: academic
- scorer excluded 34 more anchor/academic organisations

| Stage | OK | Processed | Skipped | Cost | Seconds | Notes |
|---|---|---|---|---|---|---|
| scout | yes | 1005 | 0 | $0.0000 | 267.61 |  |
| triage | yes | 835 | 10543 | $0.0239 | 40.82 | labels by model: claude-haiku-5-5=9710, keyword-gate=1259 |
| resolve | yes | 6855 | 7 | $0.0291 | 97.58 | 70 links, 5 merges, 210 ambiguous cases (20 decided by LLM, 7 queued for review); repo CuboiLeo/SuperMimic-Reproduced cites paper 2610.28480; repo swirl-uk/BiGym2 cites paper 2610.07594; repo OpenDriveLab/P2P-T cites paper 2609.35375; repo mk322/DeliveryGym cites paper 2609.19801; repo Ly041021/TIO-Former cites paper 2609.17198; merged person GALABA VAMSI (GitHub profile name matches login galabavamsi); merged person Jianglong Ye (GitHub profile name matches login jianglongye); 11 GitHub profiles checked for login-name matches; 2000 author profiles fetched from OpenAlex |
| enrich | yes | 0 | 0 | $0.0000 | 5.41 |  |
| score | yes | 1216 | 0 | $0.0000 | 1.85 |  |
| analyst | yes | 32 | 18 | $1.0804 | 565.17 | 72 absence sentences cited to the whole packet |
| verifier | yes | 32 | 18 | $0.5842 | 231.58 |  |

## Ranked candidates (top 25)

_25 candidates in the full report; 7 shown here in full, the rest withheld with their rank, kind, score and confidence._

### 1. Withheld
*person · score 0.423 · confidence medium · name and evidence withheld*

### 2. Withheld
*organisation · score 0.390 · confidence medium · name and evidence withheld*

### 3. Withheld
*person · score 0.375 · confidence medium · name and evidence withheld*

### 4. Withheld
*organisation · score 0.373 · confidence medium · name and evidence withheld*

### 5. Withheld
*organisation · score 0.349 · confidence low · name and evidence withheld*

### 6. OpenBMB ([site](https://github.com/OpenBMB/DeepThinkVLA))
*organisation · score 0.330 · confidence medium · falling (was #4)*

SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action Models
| Component | Raw | Weight | Weighted | Why |
|---|---|---|---|---|
| momentum | 0.51 | 0.32 | +0.164 | stars level 535 (z +0.8; no history yet) [stars level only] |
| founder_quality | 0.45 | 0.27 | +0.123 | citation growth +37% y/y (z +3.0); shipped open source (535 stars); prior exits: no source yet |
| formation | 0.00 | 0.22 | +0.000 | no formation events observed |
| thesis_fit | 0.54 | 0.08 | +0.043 | 62% of 4 artifacts relevant/adjacent across 3 sources |
| consensus_penalty | 0.00 | -0.13 | -0.000 | no consensus signals |
| integrity | 0.00 | -0.06 | -0.000 | no integrity flags |

**Top signals**

- openalex_citations = 0.0 on 2026-11-02 ([source](https://api.openalex.org/works?filter=doi%3A10.48550%2Farxiv.2609.02319%7C10.48550%2Farxiv.2609.02306%7C10.48550%2Farxiv.2609.02293%7C10.48550%2Farxiv.2609.02270%7C10.48550%2Farxiv.2609.02252%7C10.48550%2Farxiv.2609.02237%7C10.48550%2Farxiv.2609.02222%7C10.48550%2Farxiv.2609.02219%7C10.48550%2Farxiv.2609.02217%7C10.48550%2Farxiv.2609.02964%7C10.48550%2Farxiv.2609.02159%7C10.48550%2Farxiv.2609.02157%7C10.48550%2Farxiv.2609.02134%7C10.48550%2Farxiv.2609.02097%7C10.48550%2Farxiv.2609.02079%7C10.48550%2Farxiv.2609.02046%7C10.48550%2Farxiv.2609.02020%7C10.48550%2Farxiv.2609.02003%7C10.48550%2Farxiv.2609.05533%7C10.48550%2Farxiv.2609.01961%7C10.1007%2F978-3-032-33701-6_7%7C10.48550%2Farxiv.2609.01938%7C10.48550%2Farxiv.2609.01899%7C10.48550%2Farxiv.2609.01873%7C10.48550%2Farxiv.2609.01799%7C10.48550%2Farxiv.2609.01775%7C10.48550%2Farxiv.2609.01731%7C10.48550%2Farxiv.2609.01596%7C10.48550%2Farxiv.2609.01579%7C10.48550%2Farxiv.2609.01567%7C10.48550%2Farxiv.2609.01556%7C10.48550%2Farxiv.2609.01699%7C10.48550%2Farxiv.2609.01518%7C10.1145%2F3767308.3835398%7C10.48550%2Farxiv.2609.01453%7C10.48550%2Farxiv.2609.01420%7C10.48550%2Farxiv.2609.01418%7C10.48550%2Farxiv.2609.01408%7C10.48550%2Farxiv.2609.01404%7C10.48550%2Farxiv.2609.01394%7C10.48550%2Farxiv.2609.01384%7C10.48550%2Farxiv.2609.01351%7C10.48550%2Farxiv.2609.01339%7C10.48550%2Farxiv.2609.01281%7C10.48550%2Farxiv.2609.01260%7C10.48550%2Farxiv.2609.01252%7C10.48550%2Farxiv.2609.01215%7C10.48550%2Farxiv.2609.01207%7C10.48550%2Farxiv.2609.01172%7C10.48550%2Farxiv.2609.01148&amp;per-page=50&amp;select=id%2Cdoi%2Ctitle%2Cpublication_date%2Ccited_by_count%2Cauthorships%2Creferenced_works_count%2Ctype&amp;mailto=headwaterventure%40proton.me)) `[ev_54f5254b2a99bb3c]`
- github_stars = 535.0 on 2026-11-02 ([source](https://api.github.com/search/repositories?q=topic%3Arobotics+pushed%3A%3E%3D2026-08-04+stars%3A%3E%3D100&amp;sort=stars&amp;order=desc&amp;per_page=100&amp;page=2)) `[ev_4b515f2fbabeba1d]`
- github_commits_window = 68.0 on 2026-11-02 ([source](https://api.github.com/repos/OpenBMB/SimpleNav/commits?since=2026-08-04T22%3A11%3A56.797200%2B00%3A00&amp;until=2026-11-02T22%3A11%3A56.797200%2B00%3A00&amp;per_page=100)) `[ev_162d7ad577c20c3a]`

**Brief** _(model claude-opus-5-5, cached)_

*What building.* OpenBMB is a GitHub organisation publishing open-source vision-language-action (VLA) model research code for robotics, including DeepThinkVLA, described as &#34;Enhancing Reasoning Capability of Vision-Language-Action Models&#34;. [[ev_4b515f2fbabeba1d]](https://github.com/OpenBMB/DeepThinkVLA) OpenBMB also hosts SimpleMemVLA, a native-video memory for VLA models aimed at long-horizon robot manipulation, and SimpleNav, a framework for navigation VLA research. [[ev_f0b1317dcc5dbcfe]](https://github.com/OpenBMB/SimpleMemVLA) [[ev_7591ff7d28296c59]](https://github.com/OpenBMB/SimpleNav) 
*Why now.* OpenBMB created two new VLA repositories in late August 2026 (SimpleNav on 2026-08-27 and SimpleMemVLA on 2026-08-29), with pushes as recent as 2026-10-31. [[ev_7591ff7d28296c59]](https://github.com/OpenBMB/SimpleNav) [[ev_f0b1317dcc5dbcfe]](https://github.com/OpenBMB/SimpleMemVLA) The cadence of new robotics repositories suggests OpenBMB is expanding from a single VLA project into a broader embodied-AI research line, though this is an academic open-source pattern rather than a company formation signal. [[ev_4b515f2fbabeba1d]](https://github.com/OpenBMB/DeepThinkVLA) [[ev_f0b1317dcc5dbcfe]](https://github.com/OpenBMB/SimpleMemVLA) [[ev_7591ff7d28296c59]](https://github.com/OpenBMB/SimpleNav) 
*Key signals.* OpenBMB/DeepThinkVLA had 535 stars and 51 forks, MIT-licensed, with topics including robotics, rl and vla. [[ev_4b515f2fbabeba1d]](https://github.com/OpenBMB/DeepThinkVLA) The SimpleMemVLA paper, published 2026-09-02 in cs.CV, cs.LG and cs.RO, lists 11 authors including Junbo Cui and Yankai Lin, with the first author Cheng Yin affiliated with Huazhong University of Science and Technology. [[ev_879a91d874aa244f]](https://arxiv.org/abs/2609.05533) [[ev_54f5254b2a99bb3c]](https://openalex.org/W7212076977) Co-author Junbo Cui, affiliated with Beijing University of Posts and Telecommunications, has 18 works and 128 citations, with yearly citations of 52 in 2025 and 71 in 2026. [[ev_35903cded498bcf0]](https://openalex.org/A5100862506) 
*Risks.* The evidence shows no formation events, funding, team or commercial activity; OpenBMB appears to be an academic open-source organisation rather than an investable startup. [[ev_4b515f2fbabeba1d]](https://github.com/OpenBMB/DeepThinkVLA) [[ev_54f5254b2a99bb3c]](https://openalex.org/W7212076977) [[ev_35903cded498bcf0]](https://openalex.org/A5100862506) All three projects are MIT-licensed research code, which makes defensibility and a path to a proprietary product unclear. [[ev_4b515f2fbabeba1d]](https://github.com/OpenBMB/DeepThinkVLA) [[ev_7591ff7d28296c59]](https://github.com/OpenBMB/SimpleNav) 
*Questions a partner would ask.* Is OpenBMB a research collective tied to universities or a lab, and is there any intent to form a company around the VLA work? Who are the core contributors behind DeepThinkVLA, SimpleMemVLA and SimpleNav, and who would be a founder? Have the VLA models been run on physical robots, and with what results versus existing VLA baselines? Is anyone outside academia using these repositories, for example robotics companies building on the code? What is the funding and institutional relationship behind OpenBMB? 
*Verification:* 75.0% of checked sentences supported; 2 removed; judge 6.5/10.

**What would change my mind**

- Star history is missing (needs a classic GitHub token): acceleration could be flat or fake.
- No Form D on file: a first filing would confirm a priced round and formation date.
- No job board found: open engineering roles would confirm the team is growing.
- No anchor-lab alumni identified among linked people; an affiliation check could change founder quality.

### 7. JBR-001 ([site](https://projecthub.arduino.cc))
*organisation · score 0.324 · confidence low · rising (was #16)*

Show HN: JBR-001 – An open-source 3D printable desktop robot
| Component | Raw | Weight | Weighted | Why |
|---|---|---|---|---|
| momentum | 0.96 | 0.32 | +0.308 | HN 133 pts (z +3.0), 0.2 pts/h (z +3.0) |
| founder_quality | 0.00 | 0.27 | +0.000 | prior exits: no source yet |
| formation | 0.00 | 0.22 | +0.000 | no formation events observed |
| thesis_fit | 0.20 | 0.08 | +0.016 | 50% of 1 artifacts relevant/adjacent across 1 sources |
| consensus_penalty | 0.00 | -0.13 | -0.000 | no consensus signals |
| integrity | 0.00 | -0.06 | -0.000 | no integrity flags |

**Top signals**

- hn_points = 133.0 on 2026-11-02 ([source](https://hn.algolia.com/api/v1/search_by_date?query=robot&amp;tags=story&amp;numericFilters=created_at_i%3E%3D1785871811%2Ccreated_at_i%3C%3D1793647811&amp;hitsPerPage=100&amp;page=3)) `[ev_4860f1faaa9b9913]`

**Brief** _(model claude-opus-5-5)_

*What building.* JBR-001 is an open-source, 3D printable desktop companion robot powered by Arduino UNO Q, with source code, 3D printable files and assembly instructions published on Arduino Project Hub. [[ev_4860f1faaa9b9913]](https://news.ycombinator.com/item?id=49890707) The JBR-001 robot has a camera, distance sensor, buzzer, an animated display and 3 servo motors that move its head and arms, and it can recognise objects and respond to them. [[ev_4860f1faaa9b9913]](https://news.ycombinator.com/item?id=49890707) 
*Why now.* JBR-001 was posted as a Show HN on 2026-09-29 and drew 133 points and 32 comments. [[ev_4860f1faaa9b9913]](https://news.ycombinator.com/item?id=49890707) [[ev_81421b07765ce957]](https://news.ycombinator.com/item?id=49890707) In our reading, the interest is driven by a hobbyist build on new Arduino UNO Q hardware rather than by a company event, so the timing case is weak. 
*Key signals.* The Show HN post for JBR-001 received 133 points and 32 comments as of its 2026-09-29 listing. [[ev_4860f1faaa9b9913]](https://news.ycombinator.com/item?id=49890707) The JBR-001 project is fully open source, with code, printable parts and assembly instructions hosted on Arduino Project Hub under the account syntheticaidata. [[ev_4860f1faaa9b9913]](https://news.ycombinator.com/item?id=49890707) The Show HN post was submitted by the HN user gvuksic. [[ev_81421b07765ce957]](https://news.ycombinator.com/item?id=49890707) 
*Risks.* The packet contains no record of a company, named founders, funding or customers behind JBR-001. [[ev_4860f1faaa9b9913]](https://news.ycombinator.com/item?id=49890707) [[ev_81421b07765ce957]](https://news.ycombinator.com/item?id=49890707) Both records in the packet are the same Hacker News post, so the evidence is thin and rests on a single dated event. [[ev_4860f1faaa9b9913]](https://news.ycombinator.com/item?id=49890707) [[ev_81421b07765ce957]](https://news.ycombinator.com/item?id=49890707) In our judgement, an open-source hobby robot built on a commodity Arduino board may be hard to defend commercially, and its fit with the physical AI thesis is marginal. 
*Questions a partner would ask.* Who is behind the syntheticaidata account and gvuksic, and is there an intent to form a company around JBR-001? Is JBR-001 a side project, a showcase for synthetic AI data work, or the start of a product? Does the team plan to sell kits or assembled units, and at what price? How is object recognition done on the Arduino UNO Q: on-device models or a cloud service? What has happened since the Show HN in terms of builds, inbound demand or contributors? 
*Verification:* 100.0% of checked sentences supported; judge 6.5/10.

**What would change my mind**

- No Form D on file: a first filing would confirm a priced round and formation date.
- No job board found: open engineering roles would confirm the team is growing.
- No anchor-lab alumni identified among linked people; an affiliation check could change founder quality.
- Single-source evidence: a second independent source (paper, repo, launch, filing) would raise confidence.

### 8. Open-X-Humanoid ([site](https://github.com/Open-X-Humanoid/TienKung-Lab))
*organisation · score 0.323 · confidence medium · rising (was #22)*

Open-X-Humanoid/HEX
| Component | Raw | Weight | Weighted | Why |
|---|---|---|---|---|
| momentum | 0.55 | 0.32 | +0.176 | stars level 914 (z +1.1; no history yet) [stars level only] |
| founder_quality | 0.41 | 0.27 | +0.110 | citation growth -5% y/y (z +1.5); shipped open source (914 stars); prior exits: no source yet |
| formation | 0.00 | 0.22 | +0.000 | no formation events observed |
| thesis_fit | 0.47 | 0.08 | +0.038 | 75% of 2 artifacts relevant/adjacent across 2 sources |
| consensus_penalty | 0.00 | -0.13 | -0.000 | no consensus signals |
| integrity | 0.00 | -0.06 | -0.000 | no integrity flags |

**Top signals**

- github_stars = 914.0 on 2026-11-02 ([source](https://api.github.com/search/repositories?q=topic%3Aembodied-ai+pushed%3A%3E%3D2026-08-04+stars%3A%3E%3D100&amp;sort=stars&amp;order=desc&amp;per_page=100&amp;page=1)) `[ev_3c1457f7ee639cf9]`
- github_commits_window = 3.0 on 2026-11-02 ([source](https://api.github.com/repos/Open-X-Humanoid/HEX/commits?since=2026-08-04T22%3A11%3A56.797200%2B00%3A00&amp;until=2026-11-02T22%3A11%3A56.797200%2B00%3A00&amp;per_page=100)) `[ev_4fb2a1d06b1ded44]`

**Brief** _(model claude-opus-5-5)_

*What building.* Open-X-Humanoid is a GitHub organisation publishing TienKung-Lab, described as a &#34;Direct IsaacLab Workflow for Legged Robots&#34; and tagged for humanoid robots, reinforcement learning and sim2sim. [[ev_3c1457f7ee639cf9]](https://github.com/Open-X-Humanoid/TienKung-Lab) Open-X-Humanoid also publishes HEX, described as &#34;a whole-body vision-language-action framework for full-sized humanoid robots&#34; and tagged for imitation learning, cross-embodiment and whole-body manipulation. [[ev_1d4fbe02ba514999]](https://github.com/Open-X-Humanoid/HEX) 
*Why now.* TienKung-Lab, a legged-robot training workflow, was created on 2025-07-03, and HEX, a whole-body vision-language-action framework, followed on 2026-05-19. [[ev_3c1457f7ee639cf9]](https://github.com/Open-X-Humanoid/TienKung-Lab) [[ev_1d4fbe02ba514999]](https://github.com/Open-X-Humanoid/HEX) In our reading, this sequence shows Open-X-Humanoid moving from locomotion training tooling toward whole-body manipulation policies within about ten months. Both repositories remained active in October 2026: TienKung-Lab was last pushed on 2026-10-23, and HEX had three commits on 2026-10-04. [[ev_3c1457f7ee639cf9]](https://github.com/Open-X-Humanoid/TienKung-Lab) [[ev_4fb2a1d06b1ded44]](https://github.com/Open-X-Humanoid/HEX/commits) 
*Key signals.* HEX has accumulated 187 stars and 6 forks since its creation on 2026-05-19. [[ev_1d4fbe02ba514999]](https://github.com/Open-X-Humanoid/HEX) Both repositories are original projects written in Python, are not forks and are owned by the same organisation account (owner_id 217879969). [[ev_3c1457f7ee639cf9]](https://github.com/Open-X-Humanoid/TienKung-Lab) [[ev_1d4fbe02ba514999]](https://github.com/Open-X-Humanoid/HEX) The packet includes an OpenAlex profile for Shuanghao Bai, listing 20 works and 121 citations, with 11 of those works dated 2026. [[ev_44e5cc868a2aa31a]](https://openalex.org/A5111095090) 
*Risks.* The packet contains no record of a company, funding, named founders or a formation event for Open-X-Humanoid. [[ev_1d4fbe02ba514999]](https://github.com/Open-X-Humanoid/HEX) [[ev_3c1457f7ee639cf9]](https://github.com/Open-X-Humanoid/TienKung-Lab) [[ev_44e5cc868a2aa31a]](https://openalex.org/A5111095090) [[ev_4fb2a1d06b1ded44]](https://github.com/Open-X-Humanoid/HEX/commits) TienKung-Lab&#39;s licence is listed as &#34;NOASSERTION&#34; and HEX&#39;s licence is null, so the terms for reuse and commercialisation are unclear. [[ev_3c1457f7ee639cf9]](https://github.com/Open-X-Humanoid/TienKung-Lab) [[ev_1d4fbe02ba514999]](https://github.com/Open-X-Humanoid/HEX) 
*Questions a partner would ask.* Who are the people behind Open-X-Humanoid, and is there a legal entity or a plan to form one? How is Open-X-Humanoid connected to the TienKung humanoid hardware, and who owns that platform? What is Shuanghao Bai&#39;s role, if any, in TienKung-Lab or HEX? Which licence will TienKung-Lab and HEX carry, and is a commercial product planned on top of them? Has HEX been run on physical full-sized humanoids, and with what sim-to-real results? 
*Verification:* 81.8% of checked sentences supported; 2 removed; judge 6.5/10.

**What would change my mind**

- Star history is missing (needs a classic GitHub token): acceleration could be flat or fake.
- No Form D on file: a first filing would confirm a priced round and formation date.
- No job board found: open engineering roles would confirm the team is growing.
- No anchor-lab alumni identified among linked people; an affiliation check could change founder quality.

### 9. Nicklas Hansen ([site](https://arxiv.org/abs/2610.39044))
*person · score 0.306 · confidence medium · new*

Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand
| Component | Raw | Weight | Weighted | Why |
|---|---|---|---|---|
| momentum | 0.55 | 0.32 | +0.177 | stars level 995 (z +1.2; no history yet) [stars level only] |
| founder_quality | 0.32 | 0.27 | +0.087 | citation growth -45% y/y (z -0.5); shipped open source (995 stars); prior exits: no source yet |
| formation | 0.00 | 0.22 | +0.000 | no formation events observed |
| thesis_fit | 0.52 | 0.08 | +0.041 | 67% of 3 artifacts relevant/adjacent across 3 sources |
| consensus_penalty | 0.00 | -0.13 | -0.000 | no consensus signals |
| integrity | 0.00 | -0.06 | -0.000 | no integrity flags |

**Top signals**

- openalex_citations = 0.0 on 2026-11-02 ([source](https://api.openalex.org/works?filter=doi%3A10.48550%2Farxiv.2610.39543%7C10.48550%2Farxiv.2610.39528%7C10.48550%2Farxiv.2610.39454%7C10.48550%2Farxiv.2610.39451%7C10.48550%2Farxiv.2610.39446%7C10.48550%2Farxiv.2610.39429%7C10.48550%2Farxiv.2610.39416%7C10.48550%2Farxiv.2610.39385%7C10.48550%2Farxiv.2610.39379%7C10.48550%2Farxiv.2610.39378%7C10.48550%2Farxiv.2610.39367%7C10.48550%2Farxiv.2610.39327%7C10.48550%2Farxiv.2610.39320%7C10.48550%2Farxiv.2610.39319%7C10.48550%2Farxiv.2610.39314%7C10.48550%2Farxiv.2610.39287%7C10.1007%2F978-3-032-37242-0_22%7C10.48550%2Farxiv.2610.39282%7C10.48550%2Farxiv.2610.39280%7C10.48550%2Farxiv.2610.39279%7C10.48550%2Farxiv.2610.39278%7C10.48550%2Farxiv.2610.39267%7C10.48550%2Farxiv.2610.39232%7C10.48550%2Farxiv.2610.39212%7C10.48550%2Farxiv.2610.39180%7C10.48550%2Farxiv.2610.39167%7C10.48550%2Farxiv.2610.39147%7C10.48550%2Farxiv.2610.39126%7C10.48550%2Farxiv.2610.39125%7C10.48550%2Farxiv.2610.39119%7C10.48550%2Farxiv.2610.39100%7C10.48550%2Farxiv.2610.39076%7C10.48550%2Farxiv.2610.39055%7C10.48550%2Farxiv.2610.39054%7C10.48550%2Farxiv.2610.39044%7C10.48550%2Farxiv.2610.39005%7C10.48550%2Farxiv.2610.38993%7C10.48550%2Farxiv.2610.38967%7C10.48550%2Farxiv.2610.38930%7C10.48550%2Farxiv.2610.38901%7C10.48550%2Farxiv.2610.38888%7C10.48550%2Farxiv.2610.38867%7C10.1109%2Fjiot.2026.3742225.%7C10.48550%2Farxiv.2610.38744%7C10.48550%2Farxiv.2610.38731%7C10.48550%2Farxiv.2610.38661%7C10.48550%2Farxiv.2610.38657%7C10.48550%2Farxiv.2610.38628%7C10.48550%2Farxiv.2610.38613%7C10.48550%2Farxiv.2610.38611&amp;per-page=50&amp;select=id%2Cdoi%2Ctitle%2Cpublication_date%2Ccited_by_count%2Cauthorships%2Creferenced_works_count%2Ctype&amp;mailto=headwaterventure%40proton.me)) `[ev_82aa4042254c0ea9]`
- github_stars = 995.0 on 2026-11-02 ([source](https://api.github.com/search/repositories?q=topic%3Arobotics+pushed%3A%3E%3D2026-08-04+stars%3A%3E%3D100&amp;sort=stars&amp;order=desc&amp;per_page=100&amp;page=2)) `[ev_8ba52b17a9f2281c]`
- github_commits_window = 1.0 on 2026-11-02 ([source](https://api.github.com/repos/nicklashansen/tdmpc2/commits?since=2026-08-04T22%3A11%3A56.797200%2B00%3A00&amp;until=2026-11-02T22%3A11%3A56.797200%2B00%3A00&amp;per_page=100)) `[ev_57e7776060cb24f3]`

**Brief** _(model claude-opus-5-5)_

*What building.* Nicklas Hansen is the last-listed author on &#34;Catch It All!&#34;, a sim-to-real catching framework for humanoid robots that uses only one egocentric camera, and a co-author on FACT, a training method for world-action models. [[ev_da5d5b3efa75e17a]](https://arxiv.org/abs/2610.39044) [[ev_c0062560be8bd514]](https://arxiv.org/abs/2608.10232) The packet contains no record of a company, product or commercial entity associated with Nicklas Hansen. [[ev_57e7776060cb24f3]](https://github.com/nicklashansen/tdmpc2/commits) [[ev_82aa4042254c0ea9]](https://openalex.org/W7224820942) [[ev_8ba52b17a9f2281c]](https://github.com/nicklashansen/tdmpc2) [[ev_c0062560be8bd514]](https://arxiv.org/abs/2608.10232) [[ev_d347dc6b0a6d4473]](https://openalex.org/A5086722753) [[ev_da5d5b3efa75e17a]](https://arxiv.org/abs/2610.39044) 
*Why now.* Two robotics papers listing Nicklas Hansen as an author appeared on arXiv in quick succession: FACT on 2026-08-10 and Catch It All! on 2026-10-28. [[ev_c0062560be8bd514]](https://arxiv.org/abs/2608.10232) [[ev_da5d5b3efa75e17a]](https://arxiv.org/abs/2610.39044) The tdmpc2 repository, created 2023-10-26, is still maintained, with a commit on 2026-10-02 and a last push on 2026-10-20. [[ev_8ba52b17a9f2281c]](https://github.com/nicklashansen/tdmpc2) [[ev_57e7776060cb24f3]](https://github.com/nicklashansen/tdmpc2/commits) In our reading, the recent papers apply Nicklas Hansen&#39;s world-model work to humanoid and dexterous manipulation tasks, but nothing in the packet shows a move toward company formation. 
*Key signals.* The tdmpc2 repository has 995 stars and 216 forks. [[ev_8ba52b17a9f2281c]](https://github.com/nicklashansen/tdmpc2) The OpenAlex profile for Nicklas Hansen lists 31 works and 818 citations, with yearly citations rising from 113 in 2023 to 239 in 2024. [[ev_d347dc6b0a6d4473]](https://openalex.org/A5086722753) Catch It All! reports policies that generalize to unseen objects with varying geometry, deformability and elasticity for underhand and overhand catches. [[ev_da5d5b3efa75e17a]](https://arxiv.org/abs/2610.39044) FACT targets a stated weakness of world-action models: they are trained mostly on successful demonstrations and have little reason to predict the consequences of bad actions. [[ev_c0062560be8bd514]](https://arxiv.org/abs/2608.10232) 
*Risks.* The packet contains no record of a company, funding, co-founders or formation activity for Nicklas Hansen. [[ev_57e7776060cb24f3]](https://github.com/nicklashansen/tdmpc2/commits) [[ev_82aa4042254c0ea9]](https://openalex.org/W7224820942) [[ev_8ba52b17a9f2281c]](https://github.com/nicklashansen/tdmpc2) [[ev_c0062560be8bd514]](https://arxiv.org/abs/2608.10232) [[ev_d347dc6b0a6d4473]](https://openalex.org/A5086722753) [[ev_da5d5b3efa75e17a]](https://arxiv.org/abs/2610.39044) In our view, the evidence is thin: six records showing academic output and one open-source repository, which is not enough to judge Nicklas Hansen&#39;s commercial intent or ability to lead a team. 
*Questions a partner would ask.* What is Nicklas Hansen&#39;s current position, and when does it end? Is TD-MPC2 being used outside academia, and by whom? Did Nicklas Hansen lead the Catch It All! work, or advise on it as last author, and on what hardware was it run? Is Nicklas Hansen considering starting a company, and with which co-authors? Which world-model capability would Nicklas Hansen commercialize first: control, manipulation or failure-aware training? 
*Verification:* 81.8% of checked sentences supported; 2 removed; judge 6.5/10.

**What would change my mind**

- Star history is missing (needs a classic GitHub token): acceleration could be flat or fake.
- No anchor-lab alumni identified among linked people; an affiliation check could change founder quality.

### 10. Withheld
*person · score 0.304 · confidence low · name and evidence withheld*

### 11. Withheld
*organisation · score 0.301 · confidence low · name and evidence withheld*

### 12. Withheld
*organisation · score 0.298 · confidence low · name and evidence withheld*

### 13. Withheld
*organisation · score 0.297 · confidence low · name and evidence withheld*

### 14. Bingao Chen ([site](https://arxiv.org/abs/2610.20064))
*person · score 0.294 · confidence medium · rising (was #428)*

Towards Agentic Robots: Model, Data, Environment, and Harness
| Component | Raw | Weight | Weighted | Why |
|---|---|---|---|---|
| momentum | 0.31 | 0.32 | +0.099 | stars level 30 (z -0.7; no history yet) [stars level only] |
| founder_quality | 0.53 | 0.27 | +0.143 | anchor alumni (100% of linked people); citations 0 (z -0.7; no trajectory yet); shipped open source (30 stars); prior exits: no source yet |
| formation | 0.00 | 0.22 | +0.000 | no formation events observed |
| thesis_fit | 0.65 | 0.08 | +0.052 | 75% of 4 artifacts relevant/adjacent across 3 sources |
| consensus_penalty | 0.00 | -0.13 | -0.000 | no consensus signals |
| integrity | 0.00 | -0.06 | -0.000 | no integrity flags |

**Top signals**

- openalex_citations = 0.0 on 2026-11-02 ([source](https://api.openalex.org/works?filter=doi%3A10.48550%2Farxiv.2610.20607%7C10.48550%2Farxiv.2610.20606%7C10.48550%2Farxiv.2610.20596%7C10.48550%2Farxiv.2610.20579%7C10.48550%2Farxiv.2610.20560%7C10.48550%2Farxiv.2610.20552%7C10.48550%2Farxiv.2610.20531%7C10.48550%2Farxiv.2610.20524%7C10.48550%2Farxiv.2610.20504%7C10.48550%2Farxiv.2610.20490%7C10.48550%2Farxiv.2610.20476%7C10.48550%2Farxiv.2610.20474%7C10.48550%2Farxiv.2610.20460%7C10.48550%2Farxiv.2610.20442%7C10.48550%2Farxiv.2610.20429%7C10.48550%2Farxiv.2610.20409%7C10.48550%2Farxiv.2610.20351%7C10.48550%2Farxiv.2610.20336%7C10.48550%2Farxiv.2610.20333%7C10.48550%2Farxiv.2610.20320%7C10.48550%2Farxiv.2610.20318%7C10.48550%2Farxiv.2610.20312%7C10.48550%2Farxiv.2610.20280%7C10.48550%2Farxiv.2610.20278%7C10.48550%2Farxiv.2610.20255%7C10.48550%2Farxiv.2610.20244%7C10.48550%2Farxiv.2610.20241%7C10.48550%2Farxiv.2610.20226%7C10.48550%2Farxiv.2610.20223%7C10.1007%2F978-3-031-79032-4_11%7C10.48550%2Farxiv.2610.20160%7C10.48550%2Farxiv.2610.20157%7C10.48550%2Farxiv.2610.20150%7C10.48550%2Farxiv.2610.20134%7C10.48550%2Farxiv.2610.23986%7C10.48550%2Farxiv.2610.20121%7C10.48550%2Farxiv.2610.20064%7C10.48550%2Farxiv.2610.20055%7C10.48550%2Farxiv.2610.20019%7C10.48550%2Farxiv.2610.20009%7C10.48550%2Farxiv.2610.19993%7C10.48550%2Farxiv.2610.19957%7C10.48550%2Farxiv.2610.19913%7C10.48550%2Farxiv.2610.19896%7C10.48550%2Farxiv.2610.19839%7C10.48550%2Farxiv.2610.19825%7C10.48550%2Farxiv.2610.19815%7C10.48550%2Farxiv.2610.19798%7C10.48550%2Farxiv.2610.19785%7C10.48550%2Farxiv.2610.19765&amp;per-page=50&amp;select=id%2Cdoi%2Ctitle%2Cpublication_date%2Ccited_by_count%2Cauthorships%2Creferenced_works_count%2Ctype&amp;mailto=headwaterventure%40proton.me)) `[ev_4711baf1b373f798]`
- github_stars = 30.0 on 2026-11-02 ([source](https://api.github.com/search/repositories?q=%22manipulation%22+in%3Aname%2Cdescription%2Ctopics+created%3A%3E%3D2026-08-04+stars%3A%3E%3D5&amp;sort=stars&amp;order=desc&amp;per_page=100&amp;page=1)) `[ev_a4923aa5f6e84a5d]`
- github_commits_window = 2.0 on 2026-11-02 ([source](https://api.github.com/repos/bingaochen/Astra-on-RoboMME/commits?since=2026-08-04T22%3A11%3A56.797200%2B00%3A00&amp;until=2026-11-02T22%3A11%3A56.797200%2B00%3A00&amp;per_page=100)) `[ev_6279fb78776ac5a3]`

**Brief** _(model claude-opus-5-5)_

*What building.* Bingao Chen is first author of FoveaVLA, a Vision-Language-Action model that replaces the wrist camera with learned foveation actions, predicting alongside each action chunk the interaction region to observe at the next policy query. [[ev_27ec35135e74640d]](https://arxiv.org/abs/2610.20064) Bingao Chen also owns the GitHub repository Astra-on-RoboMME, described as a three-tier system for memory-augmented robotic manipulation in which Astra plans, a small VLM monitors, and a VLA acts, reporting 79.13% success on RoboMME. [[ev_a4923aa5f6e84a5d]](https://github.com/bingaochen/Astra-on-RoboMME) The packet contains no record of a company, product or commercial entity associated with Bingao Chen. [[ev_27ec35135e74640d]](https://arxiv.org/abs/2610.20064) [[ev_4711baf1b373f798]](https://openalex.org/W7222349417) [[ev_4d851dfcd64a1299]](https://arxiv.org/abs/2608.16885) [[ev_6279fb78776ac5a3]](https://github.com/bingaochen/Astra-on-RoboMME/commits) [[ev_93c0f916483eceed]](https://openalex.org/A5147434949) [[ev_a4923aa5f6e84a5d]](https://github.com/bingaochen/Astra-on-RoboMME) [[ev_aebe8c8d6cbbee96]](https://arxiv.org/abs/2610.20442) 
*Why now.* Bingao Chen&#39;s output is concentrated in a short window: a co-authored hierarchical robot foundation model paper ($τ_0$-VLA) published 2026-08-17, the Astra-on-RoboMME repository created 2026-09-21, and two papers (FoveaVLA and Towards Agentic Robots) published 2026-10-14. [[ev_4d851dfcd64a1299]](https://arxiv.org/abs/2608.16885) [[ev_a4923aa5f6e84a5d]](https://github.com/bingaochen/Astra-on-RoboMME) [[ev_27ec35135e74640d]](https://arxiv.org/abs/2610.20064) [[ev_aebe8c8d6cbbee96]](https://arxiv.org/abs/2610.20442) 
*Key signals.* FoveaVLA lists Bingao Chen as first author alongside Lihan Zha, C. Karen Liu and Guy Tevet, published 2026-10-14 in cs.RO and cs.AI. [[ev_27ec35135e74640d]](https://arxiv.org/abs/2610.20064) The Astra-on-RoboMME repository has 30 stars and 3 forks, is Apache-2.0 licensed, and its commit history shows activity only on 2026-09-21 with a last push on 2026-09-23. [[ev_a4923aa5f6e84a5d]](https://github.com/bingaochen/Astra-on-RoboMME) [[ev_6279fb78776ac5a3]](https://github.com/bingaochen/Astra-on-RoboMME/commits) OpenAlex records affiliations for Bingao Chen with Sun Yat-sen University and the Chinese University of Hong Kong in 2026. [[ev_93c0f916483eceed]](https://openalex.org/A5147434949) Bingao Chen is one of many co-authors on the large-team $τ_0$-VLA paper (2026-08-17) and the Towards Agentic Robots survey-style paper (2026-10-14), so those mainly indicate group membership rather than individual leadership. [[ev_4d851dfcd64a1299]](https://arxiv.org/abs/2608.16885) [[ev_aebe8c8d6cbbee96]](https://arxiv.org/abs/2610.20442) 
*Risks.* The packet contains no record of a company, funding, co-founders or stated intent to commercialize. [[ev_27ec35135e74640d]](https://arxiv.org/abs/2610.20064) [[ev_4711baf1b373f798]](https://openalex.org/W7222349417) [[ev_4d851dfcd64a1299]](https://arxiv.org/abs/2608.16885) [[ev_6279fb78776ac5a3]](https://github.com/bingaochen/Astra-on-RoboMME/commits) [[ev_93c0f916483eceed]](https://openalex.org/A5147434949) [[ev_a4923aa5f6e84a5d]](https://github.com/bingaochen/Astra-on-RoboMME) [[ev_aebe8c8d6cbbee96]](https://arxiv.org/abs/2610.20442) The work so far reads as academic research contributions rather than a product, and the system&#39;s medium-confidence, rank-14 score reflects limited signal beyond affiliation and a small repository. 
*Questions a partner would ask.* What is Bingao Chen&#39;s current role and stage (PhD student, research assistant, visiting researcher), and under which lab was FoveaVLA done? Has FoveaVLA been tested on real hardware, and how does it compare to wrist-camera baselines on the same tasks? Is Astra-on-RoboMME a one-off benchmark entry or the start of a system Bingao Chen intends to keep developing? What was Bingao Chen&#39;s individual contribution to $τ_0$-VLA, and which organization led that project? Does Bingao Chen have any intent to start a company, and with whom? 
*Verification:* 80.0% of checked sentences supported; 2 removed; judge 6.5/10.

**What would change my mind**

- Star history is missing (needs a classic GitHub token): acceleration could be flat or fake.

### 15. OpenMind ([site](https://github.com/OpenMind/OM1))
*organisation · score 0.293 · confidence low · steady (was #15)*

OpenMind/OM1
| Component | Raw | Weight | Weighted | Why |
|---|---|---|---|---|
| momentum | 0.63 | 0.32 | +0.202 | stars level 2959 (z +1.7; no history yet) [stars level only] |
| founder_quality | 0.22 | 0.27 | +0.059 | shipped open source (2959 stars); prior exits: no source yet |
| formation | 0.00 | 0.22 | +0.000 | no formation events observed |
| thesis_fit | 0.39 | 0.08 | +0.032 | 100% of 1 artifacts relevant/adjacent across 1 sources |
| consensus_penalty | 0.00 | -0.13 | -0.000 | no consensus signals |
| integrity | 0.00 | -0.06 | -0.000 | no integrity flags |

**Top signals**

- github_stars = 2959.0 on 2026-11-02 ([source](https://api.github.com/search/repositories?q=topic%3Arobotics+pushed%3A%3E%3D2026-08-04+stars%3A%3E%3D100&amp;sort=stars&amp;order=desc&amp;per_page=100&amp;page=1)) `[ev_ea54f92ce7000910]`
- github_commits_window = 22.0 on 2026-11-02 ([source](https://api.github.com/repos/OpenMind/OM1/commits?since=2026-08-04T22%3A11%3A56.797200%2B00%3A00&amp;until=2026-11-02T22%3A11%3A56.797200%2B00%3A00&amp;per_page=100)) `[ev_2870233ca777a05e]`

**Brief** _(model claude-opus-5-5, cached)_

*What building.* OpenMind publishes OM1, an MIT-licensed open-source repository described as a &#34;Modular AI HAL (Hardware Abstraction Layer) for Robots&#34;, written primarily in Go. [[ev_ea54f92ce7000910]](https://github.com/OpenMind/OM1) The OM1 repository is tagged with the topics llm, multiagent, robotics, ros2 and zenoh, and lists https://openmind.com as its homepage. [[ev_ea54f92ce7000910]](https://github.com/OpenMind/OM1) 
*Why now.* OM1 was created on 2025-01-08 and had 2959 stars and 995 forks at the time of fetch, with a last push dated 2026-10-13. [[ev_ea54f92ce7000910]](https://github.com/OpenMind/OM1) A hardware abstraction layer that connects LLM-based agents to robots through ROS2 and Zenoh could become shared infrastructure for robot developers, which is why OpenMind fits the physical AI thesis; this is an interpretation based on the repository description and topics only. [[ev_ea54f92ce7000910]](https://github.com/OpenMind/OM1) 
*Key signals.* OM1 has 2959 stars and 995 forks, a high fork-to-star ratio that suggests developers are building on the code rather than only bookmarking it. [[ev_ea54f92ce7000910]](https://github.com/OpenMind/OM1) The OM1 commit log shows regular activity through September 2026, including commits dated 2026-09-30, 2026-09-28, 2026-09-24 and three on 2026-09-15. [[ev_2870233ca777a05e]](https://github.com/OpenMind/OM1/commits) OM1 is owned by a GitHub organization account (OpenMind), is not a fork, is not archived, and had 41 open issues at the time of fetch. [[ev_ea54f92ce7000910]](https://github.com/OpenMind/OM1) 
*Risks.* Momentum is based on a single star count with no history, so growth trajectory cannot be assessed from the packet. [[ev_ea54f92ce7000910]](https://github.com/OpenMind/OM1) OM1 is released under the MIT license, so any business would need to capture value beyond the open-source code itself; this is an interpretation, not an observed fact. [[ev_ea54f92ce7000910]](https://github.com/OpenMind/OM1) 
*Questions a partner would ask.* Who are the founders and core team behind OpenMind, and what is their robotics background? Has OpenMind raised money or formed a company entity, and what is the commercial model around an MIT-licensed HAL? Which robot platforms does OM1 run on today, and who is deploying it in practice? How much of the 995-fork and 2959-star base comes from active contributors versus one-off interest? How does OM1 differ from building directly on ROS2 or other robot agent frameworks? 
*Verification:* 83.3% of checked sentences supported; 1 removed; judge 6.5/10.

**What would change my mind**

- Star history is missing (needs a classic GitHub token): acceleration could be flat or fake.
- No Form D on file: a first filing would confirm a priced round and formation date.
- No job board found: open engineering roles would confirm the team is growing.
- No anchor-lab alumni identified among linked people; an affiliation check could change founder quality.

### 16. shengshu-ai ([site](https://github.com/shengshu-ai/Motus2))
*organisation · score 0.290 · confidence medium · rising (was #116)*

shengshu-ai/Motus2
| Component | Raw | Weight | Weighted | Why |
|---|---|---|---|---|
| momentum | 0.46 | 0.32 | +0.148 | stars level 264 (z +0.5; no history yet) [stars level only] |
| founder_quality | 0.41 | 0.27 | +0.111 | citation growth +60% y/y (z +3.0); shipped open source (264 stars); prior exits: no source yet |
| formation | 0.00 | 0.22 | +0.000 | no formation events observed |
| thesis_fit | 0.39 | 0.08 | +0.032 | 100% of 1 artifacts relevant/adjacent across 2 sources |
| consensus_penalty | 0.00 | -0.13 | -0.000 | no consensus signals |
| integrity | 0.00 | -0.06 | -0.000 | no integrity flags |

**Top signals**

- github_stars = 264.0 on 2026-11-02 ([source](https://api.github.com/search/repositories?q=%22manipulation%22+in%3Aname%2Cdescription%2Ctopics+created%3A%3E%3D2026-08-04+stars%3A%3E%3D5&amp;sort=stars&amp;order=desc&amp;per_page=100&amp;page=1)) `[ev_53bf7f44d6b893b1]`
- github_commits_window = 5.0 on 2026-11-02 ([source](https://api.github.com/repos/shengshu-ai/Motus2/commits?since=2026-08-04T22%3A11%3A56.797200%2B00%3A00&amp;until=2026-11-02T22%3A11%3A56.797200%2B00%3A00&amp;per_page=100)) `[ev_f68e181bb6705efc]`

**Brief** _(model claude-opus-5-5)_

*What building.* shengshu-ai publishes Motus2 on GitHub, described as &#34;A Self-Evolving General World Model for Dexterous Manipulation&#34;. [[ev_53bf7f44d6b893b1]](https://github.com/shengshu-ai/Motus2) The Motus2 repository is owned by a GitHub account of type &#34;Organization&#34; and lists no license, no primary language and no homepage. [[ev_53bf7f44d6b893b1]](https://github.com/shengshu-ai/Motus2) 
*Why now.* The Motus2 repository was created on 2026-09-11, and the fetched snapshot shows 264 stars and 8 forks. [[ev_53bf7f44d6b893b1]](https://github.com/shengshu-ai/Motus2) A world model for dexterous manipulation is directly relevant to the robotics and physical AI thesis, and early star accumulation suggests the release drew attention, though without star history the trajectory cannot be judged. 
*Key signals.* Motus2 had 264 stargazers and 8 forks in the fetched record, with a creation date of 2026-09-11T15:12:14Z. [[ev_53bf7f44d6b893b1]](https://github.com/shengshu-ai/Motus2) The packet includes an OpenAlex author record for Hongzhe Bi, listing 9 works, 17 citations and an affiliation with Beijing University of Posts and Telecommunications. [[ev_8d51b39c9540c2cc]](https://openalex.org/A5125964905) The Hongzhe Bi record shows 5 works in 2026 against 2 in 2025, with citations of 8 in 2026 and 5 in 2025. [[ev_8d51b39c9540c2cc]](https://openalex.org/A5125964905) The packet contains no record linking Hongzhe Bi to shengshu-ai or to the Motus2 repository. [[ev_53bf7f44d6b893b1]](https://github.com/shengshu-ai/Motus2) [[ev_8d51b39c9540c2cc]](https://openalex.org/A5125964905) [[ev_f68e181bb6705efc]](https://github.com/shengshu-ai/Motus2/commits) 
*Risks.* The packet contains no record of a company formation, funding, named founders or customers for shengshu-ai. [[ev_53bf7f44d6b893b1]](https://github.com/shengshu-ai/Motus2) [[ev_8d51b39c9540c2cc]](https://openalex.org/A5125964905) [[ev_f68e181bb6705efc]](https://github.com/shengshu-ai/Motus2/commits) 
*Questions a partner would ask.* Who are the people behind the shengshu-ai GitHub organisation, and is Hongzhe Bi among them? Is shengshu-ai a formed company, a lab group, or part of an existing company? Which robot hands and datasets is Motus2 trained and evaluated on, and what does &#34;self-evolving&#34; mean in practice? Will Motus2 weights and code be released under a license that permits commercial use? Is there a paper or benchmark result accompanying Motus2, and how does it compare to the predecessor implied by the name? 
*Verification:* 72.7% of checked sentences supported; 3 removed; judge 6.0/10.

**What would change my mind**

- Star history is missing (needs a classic GitHub token): acceleration could be flat or fake.
- No Form D on file: a first filing would confirm a priced round and formation date.
- No job board found: open engineering roles would confirm the team is growing.
- No anchor-lab alumni identified among linked people; an affiliation check could change founder quality.

### 17. Withheld
*organisation · score 0.287 · confidence low · name and evidence withheld*

### 18. Withheld
*organisation · score 0.287 · confidence medium · name and evidence withheld*

### 19. Withheld
*person · score 0.275 · confidence medium · name and evidence withheld*

### 20. Withheld
*organisation · score 0.275 · confidence low · name and evidence withheld*

### 21. Withheld
*organisation · score 0.267 · confidence low · name and evidence withheld*

### 22. Withheld
*organisation · score 0.267 · confidence low · name and evidence withheld*

### 23. Withheld
*organisation · score 0.265 · confidence low · name and evidence withheld*

### 24. Withheld
*organisation · score 0.265 · confidence low · name and evidence withheld*

### 25. Withheld
*organisation · score 0.264 · confidence low · name and evidence withheld*

## Evidence index

- `ev_023b6202b9bf815e` [hn](https://news.ycombinator.com/item?id=49525153) fetched 2026-11-02 · sha256:4052f10e6b2d
- `ev_08c74bc58c8e168c` [github](https://github.com/enactic/openarm/commits) fetched 2026-11-02 · sha256:c9afd12280e7
- `ev_096e3b700bf1b786` [github_search](https://github.com/RLinf/RLark) fetched 2026-11-02 · sha256:3164abc60324
- `ev_11e7a829700bcb21` [github](https://github.com/RoboVerseOrg/RoboVerse/commits) fetched 2026-11-02 · sha256:1d65ce6c0d91
- `ev_162d7ad577c20c3a` [github](https://github.com/OpenBMB/SimpleNav/commits) fetched 2026-11-02 · sha256:1ef66a993e81
- `ev_19519d65c0640a92` [github](https://github.com/starVLA/starVLA/commits) fetched 2026-11-02 · sha256:167528edbb9e
- `ev_1b6d7cad4d589e7d` [openalex](https://openalex.org/W7223142413) fetched 2026-11-02 · sha256:a39ad4a62e93
- `ev_1d1f0fe2ffbd6fc0` [github](https://github.com/newton-physics/newton/commits) fetched 2026-11-02 · sha256:e64fcbb0e64e
- `ev_1d4fbe02ba514999` [github_search](https://github.com/Open-X-Humanoid/HEX) fetched 2026-11-02 · sha256:fe365b941672
- `ev_21adc6d198b2a666` [github_search](https://github.com/enactic/openarm) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_27ec35135e74640d` [arxiv](https://arxiv.org/abs/2610.20064) fetched 2026-11-02 · sha256:71ba74de47fa
- `ev_286b1f5d14a4b289` [github_search](https://github.com/newton-physics/newton) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_2870233ca777a05e` [github](https://github.com/OpenMind/OM1/commits) fetched 2026-11-02 · sha256:69ad1629a8da
- `ev_2bf300fd78d9dedd` [hn](https://news.ycombinator.com/item?id=49525153) fetched 2026-11-02 · sha256:d29a3278ef40
- `ev_35903cded498bcf0` [openalex](https://openalex.org/A5100862506) fetched 2026-11-02 · sha256:304b89700092
- `ev_3c1457f7ee639cf9` [github_search](https://github.com/Open-X-Humanoid/TienKung-Lab) fetched 2026-11-02 · sha256:fe365b941672
- `ev_3d035b21cc12440a` [github](https://github.com/nasa-jpl/rosa/commits) fetched 2026-11-03 · sha256:bc6d86155f63
- `ev_3dcb53b7e4098981` [github](https://github.com/RLinf/RLinf/commits) fetched 2026-11-02 · sha256:716cf099c359
- `ev_4107907ec13734e1` [github_search](https://github.com/LuwuDynamics/xgoduck_hardware) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_44e5cc868a2aa31a` [openalex](https://openalex.org/A5111095090) fetched 2026-11-02 · sha256:0d5c19e8b585
- `ev_4711baf1b373f798` [openalex](https://openalex.org/W7222349417) fetched 2026-11-02 · sha256:ec0362e9e49c
- `ev_48599459443d5f8f` [github](https://github.com/robocasa/robocasa/commits) fetched 2026-11-02 · sha256:c9e2bf305e6d
- `ev_4860f1faaa9b9913` [hn](https://news.ycombinator.com/item?id=49890707) fetched 2026-11-02 · sha256:bf169f256816
- `ev_4b515f2fbabeba1d` [github_search](https://github.com/OpenBMB/DeepThinkVLA) fetched 2026-11-02 · sha256:cea85d59df74
- `ev_4d851dfcd64a1299` [arxiv](https://arxiv.org/abs/2608.16885) fetched 2026-11-02 · sha256:78d45402a81c
- `ev_4fb2a1d06b1ded44` [github](https://github.com/Open-X-Humanoid/HEX/commits) fetched 2026-11-02 · sha256:d67e8079e1ed
- `ev_53bf7f44d6b893b1` [github_search](https://github.com/shengshu-ai/Motus2) fetched 2026-11-02 · sha256:c2a96e394386
- `ev_54f5254b2a99bb3c` [openalex](https://openalex.org/W7212076977) fetched 2026-11-02 · sha256:c6e842808fbe
- `ev_57546c26befd5af8` [openalex](https://openalex.org/A5023707892) fetched 2026-11-02 · sha256:afc552f90f03
- `ev_57769acafd0b4357` [openalex](https://openalex.org/A5042268986) fetched 2026-11-02 · sha256:b849ed8c1da3
- `ev_57e7776060cb24f3` [github](https://github.com/nicklashansen/tdmpc2/commits) fetched 2026-11-02 · sha256:57202fe3b923
- `ev_602da3a6f50a1bd9` [github_search](https://github.com/RLinf/RLinf) fetched 2026-11-02 · sha256:fe365b941672
- `ev_6279fb78776ac5a3` [github](https://github.com/bingaochen/Astra-on-RoboMME/commits) fetched 2026-11-02 · sha256:bbd0156cddc3
- `ev_6b7c1cee3933dde2` [openalex](https://openalex.org/W7207528192) fetched 2026-11-02 · sha256:816a0314ea24
- `ev_6c07f4b0a767db9b` [github](https://github.com/air-embodied-brain/Zetta-Embodiment/commits) fetched 2026-11-02 · sha256:7b08b2f5f98e
- `ev_6c8c13b476875a16` [github_search](https://github.com/RoboTwin-Platform/RMBench) fetched 2026-11-02 · sha256:ccd55cc7da89
- `ev_6f796ef21d93e34f` [github_search](https://github.com/robocasa/robocasa) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_71fdb5ed1690b703` [hn](https://news.ycombinator.com/item?id=49525153) fetched 2026-11-02 · sha256:fc9f7d4acb39
- `ev_749f4b9261b04e41` [arxiv](https://arxiv.org/abs/2610.28480) fetched 2026-11-02 · sha256:cf128bab2d28
- `ev_7591ff7d28296c59` [github_search](https://github.com/OpenBMB/SimpleNav) fetched 2026-11-02 · sha256:851016f1b009
- `ev_78eab9102dbed3d8` [github](https://github.com/dexmal/opendm/commits) fetched 2026-11-02 · sha256:eadfa26dca6d
- `ev_7cbd3f60521ceb0e` [github_search](https://github.com/CuboiLeo/SuperMimic-Reproduced) fetched 2026-11-02 · sha256:41188e5bcf68
- `ev_7ced2dbc3eff958a` [github](https://github.com/CuboiLeo/SuperMimic-Reproduced/commits) fetched 2026-11-02 · sha256:940af3acd010
- `ev_81421b07765ce957` [hn](https://news.ycombinator.com/item?id=49890707) fetched 2026-11-02 · sha256:0e9c1bee472f
- `ev_82aa4042254c0ea9` [openalex](https://openalex.org/W7224820942) fetched 2026-11-02 · sha256:3fc9e051c395
- `ev_85e01bb09b126ac9` [github](https://github.com/fspinola/dexoak/commits) fetched 2026-11-02 · sha256:17662a6bed7c
- `ev_879a91d874aa244f` [arxiv](https://arxiv.org/abs/2609.05533) fetched 2026-11-02 · sha256:680880eb66d9
- `ev_89ef68fa6f12b81e` [openalex](https://openalex.org/W7223004984) fetched 2026-11-02 · sha256:66465ba8a300
- `ev_8ba52b17a9f2281c` [github_search](https://github.com/nicklashansen/tdmpc2) fetched 2026-11-02 · sha256:cea85d59df74
- `ev_8d51b39c9540c2cc` [openalex](https://openalex.org/A5125964905) fetched 2026-11-03 · sha256:4d3c1a734ea1
- `ev_8e5b73854c544de8` [github_search](https://github.com/RoboVerseOrg/RoboVerse) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_93c0f916483eceed` [openalex](https://openalex.org/A5147434949) fetched 2026-11-02 · sha256:84e1fd078092
- `ev_94157073e75a10e1` [github](https://github.com/LuwuDynamics/xgoduck_hardware/commits) fetched 2026-11-02 · sha256:7167a1b7188c
- `ev_9533bf21fb6cc870` [github_search](https://github.com/starVLA/starVLA) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_9faa4cec62ba1d99` [github_search](https://github.com/RoboVerseOrg/RoboVerse) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_a3e8c6f0a50d3b65` [openalex](https://openalex.org/A5066489766) fetched 2026-11-02 · sha256:08cad9f78d18
- `ev_a4923aa5f6e84a5d` [github_search](https://github.com/bingaochen/Astra-on-RoboMME) fetched 2026-11-02 · sha256:c2a96e394386
- `ev_a5924052a6b3ec18` [github_search](https://github.com/kevinzakka/mjbatch) fetched 2026-11-02 · sha256:0f1b1cdf5d01
- `ev_a6d797acce5486a1` [github](https://github.com/RoboTwin-Platform/RoboTwin/commits) fetched 2026-11-02 · sha256:7284984b23bf
- `ev_a7a4d95242f0435d` [github_search](https://github.com/dexmal/dexbotic) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_a90cb344f9e03b8a` [github](https://github.com/kevinzakka/mjbatch/commits) fetched 2026-11-02 · sha256:a52ee698145a
- `ev_add4beb3ececfa91` [github_search](https://github.com/RLinf/RLinf) fetched 2026-11-03 · sha256:e88a14bce610
- `ev_aebe8c8d6cbbee96` [arxiv](https://arxiv.org/abs/2610.20442) fetched 2026-11-02 · sha256:71ba74de47fa
- `ev_b25a2bf31b72de15` [github_search](https://github.com/air-embodied-brain/Zetta-Embodiment) fetched 2026-11-02 · sha256:851016f1b009
- `ev_b53d02f79e91d39d` [github_search](https://github.com/nasa-jpl/rosa) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_b8a93417aafdf0e0` [github](https://github.com/dorianborian/sesame-robot/commits) fetched 2026-11-02 · sha256:f9dfcd374717
- `ev_bbed8b38fbb051a2` [openalex](https://openalex.org/A5038304040) fetched 2026-11-02 · sha256:b849ed8c1da3
- `ev_bdc41a0a8940fe11` [github_search](https://github.com/fspinola/dexoak) fetched 2026-11-02 · sha256:a7da8ff18169
- `ev_c0062560be8bd514` [arxiv](https://arxiv.org/abs/2608.10232) fetched 2026-11-02 · sha256:d0f92e583eac
- `ev_c0ba416b29454d19` [github_search](https://github.com/starVLA/VLAct) fetched 2026-11-02 · sha256:abc0d4a3debc
- `ev_c12b31db8337f32f` [arxiv](https://arxiv.org/abs/2609.02358) fetched 2026-11-02 · sha256:680880eb66d9
- `ev_c23afd4173617f43` [github_search](https://github.com/nasa-jpl/rosa) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_c280eda4bbaf0852` [github_search](https://github.com/robocasa/robocasa) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_c4b1483c64007789` [openalex](https://openalex.org/A5073253090) fetched 2026-11-02 · sha256:a24265369b7c
- `ev_ca3fda066691164e` [github](https://github.com/RoboDojo-Benchmark/RoboDojo/commits) fetched 2026-11-02 · sha256:640a1b3b5787
- `ev_cda84db166c4f05a` [github_search](https://github.com/newton-physics/newton) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_d13c7e5b42f9874e` [github_search](https://github.com/RoboDojo-Benchmark/RoboDojo) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_d347dc6b0a6d4473` [openalex](https://openalex.org/A5086722753) fetched 2026-11-02 · sha256:a928ce26dbc4
- `ev_d5d04932685edf86` [github](https://github.com/nasa-jpl/rosa/commits) fetched 2026-11-02 · sha256:483c441b6a8b
- `ev_da5d5b3efa75e17a` [arxiv](https://arxiv.org/abs/2610.39044) fetched 2026-11-02 · sha256:4ce25ab07c24
- `ev_dad59c2b7814d840` [github_search](https://github.com/dorianborian/sesame-robot) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_ddccf7b618d65a72` [github_search](https://github.com/enactic/openarm) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_e0a7a513ab9c889e` [github_search](https://github.com/OpenBMB/SimpleMemVLA) fetched 2026-11-03 · sha256:68ddf88d12b5
- `ev_e196b5cb041b6916` [github_search](https://github.com/LuwuDynamics/xgoduck_hardware) fetched 2026-11-02 · sha256:abc0d4a3debc
- `ev_e2c74fd3065a61a1` [github](https://github.com/OpenWAM-Official/OpenWAM/commits) fetched 2026-11-02 · sha256:5bb0e78575c2
- `ev_e3b0b6c65a2c8ccf` [github_search](https://github.com/OpenWAM-Official/OpenWAM) fetched 2026-11-03 · sha256:f4231def54a4
- `ev_e59eaa47d9b49a20` [arxiv](https://arxiv.org/abs/2610.26762) fetched 2026-11-02 · sha256:cf128bab2d28
- `ev_e671ff7ef7f21fdf` [github](https://github.com/TianxingChen) fetched 2026-11-02 · sha256:d09977ba4ec4
- `ev_e7760b5f7e2115de` [github_search](https://github.com/dexmal/opendm) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_ea54f92ce7000910` [github_search](https://github.com/OpenMind/OM1) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_eedc57496151a23a` [github_search](https://github.com/RoboTwin-Platform/RoboTwin) fetched 2026-11-02 · sha256:689dd74324b6
- `ev_f0b1317dcc5dbcfe` [github_search](https://github.com/OpenBMB/SimpleMemVLA) fetched 2026-11-02 · sha256:13788f3bccd4
- `ev_f0db067811a4fc05` [openalex](https://openalex.org/A5052150026) fetched 2026-11-02 · sha256:fa05dfa5eb15
- `ev_f5c458cb07176aa2` [github_search](https://github.com/OpenWAM-Official/OpenWAM-Official.github.io) fetched 2026-11-02 · sha256:a7da8ff18169
- `ev_f68e181bb6705efc` [github](https://github.com/shengshu-ai/Motus2/commits) fetched 2026-11-02 · sha256:b89e1e069113
- `ev_f9fde8640e6b0f21` [github_search](https://github.com/OpenWAM-Official/OpenWAM) fetched 2026-11-02 · sha256:abc0d4a3debc
- `ev_fb0d1ac0155400ab` [arxiv](https://arxiv.org/abs/2610.09117) fetched 2026-11-02 · sha256:0280fb3dfc71
