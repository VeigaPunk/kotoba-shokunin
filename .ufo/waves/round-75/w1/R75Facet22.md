# R75Facet22 — trigger-eval threshold calibration

## Finding

**Candidate: `corpus/knowledge/skill-eval-artefacts-round70.md:33-35,58-72` — supported, narrowly bounded calibration discrepancy; freshness remains unverified.** The entry distinguishes the guide's strict “above” threshold from the reference runner's `>=`, and quantifies equality cases (notably default 3 runs vs even run counts). This is a concrete, falsifiable description-audit candidate, not evidence about current client behavior or a normative requirement.

## Evidence (committed bytes)

- Lane `HEAD` observed as `65a5c7a663249e0522cc49e4a148424200d9ddfe`; `git status --short` showed only the already-present untracked `.ufo/waves/round-75/` directory. The sources and snapshot were read from this commit's tree via `git show HEAD:...` (knowledge file is 85 lines). No edits outside this report.
- `corpus/knowledge/skill-eval-artefacts-round70.md:33-35` records guide S213 as “above”, runner S211 as `>=`; lines 58-72 explain the equality boundary and mitigation. The underlying committed S210 snapshot says “above a threshold” at `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:88-93`. The S211 snapshot computes the rate and uses `>=` for should-trigger and `<` for should-not-trigger at `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:227-234`.
- `corpus/SOURCES.md` rows S213 and S211 were located in committed HEAD at lines 153 and 157 respectively. S213 identifies the guide and its upstream revision; S211 explicitly scopes its authority to one reference implementation, and records upstream tree `dbd4588` equal to main **on 2026-10-25**. This is support for the historical comparison, not a claim of current upstream equality.
- `corpus/knowledge/skill-eval-artefacts-round70.md:8` gives a 90-day recheck that fetches eight quotes. That control is an announced future recheck, not proof it has run since the recorded 2026-10-25 verification. No live fetch was made for this read-only assignment.
- Relevant calibration bar: `corpus/QUALITY.md:37` (Q26) requires each headline clause to be measured by its counter or a cited guard; `:36` (Q25) requires a counter to fail on falsified content. These support bounding any R75 wording to the verified threshold difference rather than generalizing to clients.

## Concrete check/control

At the committed snapshots, assert the guide contains the strict `trigger rate is above a threshold` statement and runner branch is `trigger_rate >= trigger_threshold`; calculate representative cases: default 3 runs gives rates 0, 1/3, 2/3, 1 (no equality at 0.5), while 2 runs can yield 1/2 and separates the rules. Counter-control: mutate the runner comparison from `>=` to `>` and require the equality fixture's outcome to change; separately preserve a should-not-trigger equality case to verify its `<` rule. For a present-tense upstream claim, re-open the cited upstream revision and current source before asserting they remain aligned; the dated equality-to-main note alone cannot establish that.

## Limits / confidence

High confidence in what the committed guide snapshot and committed runner snapshot say, and in the bounded mathematical comparison. No claim that any client runs this workflow natively (the entry explicitly refuses that scope at lines 74-82), that this discrepancy changes an actual evaluation outcome in deployed clients, or that upstream sources remain unchanged today. This facet identifies existing evidence and a precise control; it does not make a new round-level depth score.