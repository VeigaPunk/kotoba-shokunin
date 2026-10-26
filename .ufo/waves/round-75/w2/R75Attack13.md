# R75Attack13 — falsification of R75Facet13

Measured revision: kotoba-shokunin `65a5c7a663249e0522cc49e4a148424200d9ddfe` (working tree = measured rev; fleet root `661e538`). Attack axes: citation fidelity, evidence-chain truth, context/cherry-pick, scope, duplication, control non-vacuousness.

## Verdict: SURVIVES (true, in-scope, well-calibrated), with two materiality caveats

No factual claim of the facet broke under attack. Every cited file:line was re-opened at the measured revision and matches, including exact line numbers — unusual precision for a wave-1 report. Two caveats reduce its marginal value rather than its truth.

## Attack log

### 1. Citation fidelity — all four pins EXACT
- `corpus/lessons/round-74-verifier-spotcheck.md:127-130` is exactly the `**quality: improved**` bullet; its sub-claims match the facet's rendering: "stale at 15 of 20 pins at base (re-measured)" (=a), "20/20 pinned" (=b), "8/8 sampled quotes re-located" (=c), "its one stale classification is corrected" (=d), and the parenthetical "(The lane self-graded `unchanged`; the outside re-check supplies the verification it lacked.)" at :129-130. Confirmed by line-numbered grep.
- `round-74-verifier-spotcheck.md:74` is exactly the "8 sampled rows … 8/8 located" re-check row — the "explicitly a sample" reading is correct ("sampled", 8 of 20 lanes; 12 rows unsampled).
- `corpus/knowledge/skill-eval-artefacts-round70.md:18-21` is the output-vs-trigger two-questions passage with "Human review is reserved for what neither can capture." at :21; `:31-32` are the F5 (scripts vs LLM judgment) and F6 ("Style, visual design and whether an output feels right are left to human review") fact rows. The facet's machine-checkable-vs-judgment reading is accurate.
- `plans/round-74.md:98-100` is exactly "**Bound (Q26, Q51):** form, sources and tokens are counted; whether a rule sentence is true of the page is a reviewer judgement no counter makes — assigned to named non-author wave-2 seats" (at :98-99; :100 blank/section break). The facet's paraphrase is faithful.

### 2. Evidence-chain truth — independently re-derived, not just quoted
- The facet's "15/20 stale pins at base" inherits the spotcheck's number. I re-derived it from the tracked receipt `.ufo/waves/round-74/receipts/sibling-staleness-base.tsv` (the spotcheck's bare `receipts/…` paths resolve under `.ufo/waves/round-74/`; 7 c2 receipts incl. `c2-base-freeze.txt`, `c2-carry-forward.txt`, `c2-selftest-freeze.txt` are present): 23 lines = 3 header comments + 20 data rows; counting rows carrying a diff/staleness marker independently of the header's self-report gives **15**. The chain holds at bytes, not narrative.
- Cherry-pick check: "quality" occurs exactly once in the spotcheck (lines 127-129). No competing `quality:` verdict was omitted; the facet's single-verdict framing is complete.

### 3. Proposed control — safe, coherent, partially non-vacuous
The three stated evidence commands are pure reads; reproduced above. The proposed clause-level matrix with negative controls (wrong-page true quote; over-broad paraphrase of the correct source) is executable against existing counter machinery (token/quote-in-pinned-snapshot checks) and its mechanical arm would be non-vacuous: a wrong-page citation fails hash/token membership. The judgment arm (named non-author entailment/scope review) matches the r74 precedent it cites. Not executed here — it is a design, and scoring it would require a chosen paragraph; the facet honestly flags this as unresolved.

### 4. Scope and duplication — in-scope, but partially redundant (caveat A)
- In-scope: wave-1 was 64-seat recon producing candidate attacks; this facet is a calibration/sourced-depth candidate, and `plans/round-75.md` confirms r75 is a description-audit round (S213 curation; description frontmatter lines 4-8 measured at base).
- Caveat A (redundancy): the facet's core distinction is already embodied in the frozen r75 design. `plans/round-75.md` C1 states "This counter is intentionally a narrow content invariant, not a semantic source adjudicator; non-author attack/review remains required" — i.e. the plan itself performs the mechanical/judgment separation the facet asks for. Sibling facets make near-identical points: R75Facet01 (row-by-row non-author adjudication of facts vs SKILL sentences), R75Facet08 (one source locator per clause, supported/overreach/unsupported reviewer marks), R75Facet25 (page-fidelity judgment vs evidence-verified counter). Facet13's distinct residual contribution is the two specific negative-control worlds (wrong-page quote, over-broad paraphrase); the rest of its proposal overlaps prior art.

### 5. Facet's "remaining unknown" was partially resolvable (caveat B)
The facet says no r75 target paragraph/claim is frozen "in the examined files" — true for its examined set, but `plans/round-75.md` (same rev) already freezes C1 on a different claim (`SKILL.md:193` threshold-equality sentence, grep -Fxc predicate) and pins the current description (frontmatter lines 4-8 lengths 76,78,73,79,72; the 1,021-char figure from `ec2c1d3` is explicitly stale — description changed since the r74 verdict). A scoped check of the plan would have sharpened the proposal to the current base and avoided re-proposing an audit whose separation principle the plan already states. Not a falsehood; a depth gap.

## Findings summary
- F1 (survives): central factual claim and all four citations exact at `65a5c7a`; evidence chain independently re-derived (15/20, 20 rows, receipts present).
- F2 (caveat, materiality): proposal largely redundant with frozen r75 C1 scope disclaimer and facets 01/08/25; unique value = the two negative-control worlds.
- F3 (caveat, depth): "which paragraph r75 targets" was answerable from `plans/round-75.md` (frontmatter lines 4-8; C1 elsewhere); facet's unknown was self-imposed by its file set.
- No counterevidence found; no scope error; no misinference; no falsified control.

## Report trailer
- Target: `.ufo/waves/round-75/w1/R75Facet13.md`
- Evidence (all read at kotoba `65a5c7a663249e0522cc49e4a148424200d9ddfe`): `corpus/lessons/round-74-verifier-spotcheck.md:74,127-130` (grep -n verified); `corpus/knowledge/skill-eval-artefacts-round70.md:18-21,31-32`; `plans/round-74.md:98-100`; `plans/round-75.md:1-40` (C1 counter scope; description lengths); `.ufo/waves/round-74/receipts/sibling-staleness-base.tsv` (23 lines, 20 data rows, 15 stale re-counted); `.ufo/waves/round-74/receipts/` c2 receipt set (7 files).
- Commands run: revision pin (`git rev-parse`), line-numbered greps, receipt row counts, receipt dir listing — all read-only; no lane edits, no commits, no live fetch.
- Revision integrity: the lane working tree turned concurrently dirty during the attack (round activity: LOG.md, SCORECARD.md, SKILL.md, corpus files; not written by this seat). All cited ranges were re-verified against committed bytes via `git show HEAD:…` — line content identical at `65a5c7a` for every citation; the working-tree drift in `skill-eval-artefacts-round70.md` does not touch lines 18-21/31-32. Findings rest on the measured rev, not drifted bytes.
- Scratch `/fast/scratch/hyaku/kotoba-r75/R75Attack13/` created and removed; empty.
- LSP: no server available for these prose/markdown artifacts; literal file/line evidence used.
- Report: `.ufo/waves/round-75/w2/R75Attack13.md`
