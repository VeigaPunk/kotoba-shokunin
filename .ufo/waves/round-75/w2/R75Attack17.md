# R75Attack17 — falsification attack on R75Facet17 (trigger-query design / construct-validity audit candidate)

**Verdict: SURVIVED.** The facet's central factual claim is true at the exact cited bytes; every line citation, hash pin, and content characterization I re-opened checks out. The proposed controls are non-vacuous in design but conditional on a frozen query corpus that the r75 plan does not declare — a materiality bound the facet itself discloses. No counterevidence, no scope error, no incorrect inference found. Partial control-level overlap with sibling facets is flagged, not a duplicate.

## What the facet claims (central factual claim)

The r70 knowledge entry identifies S210/S213 as the Agent Skills description-optimization *guide*, pins snapshot and upstream revision, and dates its historical `ground:` sweep to `7d51253f`; the pinned S210 snapshot contains concrete test-design rules (varied positive axes; near-miss negatives with keyword overlap; fixed mixed ~40% validation split; train-only edit guidance; selection by validation pass rate; fresh queries after selection); and the lane's compact `SKILL.md:193` guidance does not itself carry those construct-validity safeguards — making a sourced query-design audit a suitable candidate rule.

## Independent re-verification (all at tip `65a5c7a663249e0522cc49e4a148424200d9ddfe`, read-only)

| facet claim | re-opened evidence | result |
|---|---|---|
| entry identifies S210/S213 as the description-optimization guide, pins snapshot/revision | `corpus/knowledge/skill-eval-artefacts-round70.md:2` (S210, snapshot `S210-optimizing-descriptions.md`, sha256 `7cc54fbb…`), `:6` (S213, upstream `agentskills/agentskills@69ef37e9…`, supersedes S210) | CONFIRMED, exact lines |
| snapshot pin is real | recomputed `sha256sum` of the committed snapshot → `7cc54fbb6abbcf08…` = SOURCES row pin | CONFIRMED by independent recomputation |
| `ground:` sweep dated `7d51253f` | `:9` "printed nothing at `7d51253f`"; `git log -1 7d51253f` → "round-69 verifier spot-check" (commit exists) | CONFIRMED |
| authority note says advice is non-normative | `:13-16`, "Nothing below is a normative spec rule." at `:16` | CONFIRMED |
| entry describes trigger query construction, repetition, held-out split; warns guide/runner differ at threshold; disclaims native-client execution | `:48` (labelled ~20 queries, ~3 runs, ~40% validation), `:56-72` (the disagreement; content at 58-72), `:74-82` (Scope and refusals; content at 76-82) | CONFIRMED (facet's ranges are the content lines; headers sit at 56/74) |
| positive queries vary phrasing / explicitness / detail / complexity | snapshot `:43-49`, four axes verbatim | CONFIRMED |
| negatives are near-misses with keyword overlap, not obviously irrelevant | snapshot `:54-65` (weak: fibonacci/weather; strong: Excel-budget, csv→postgres ETL) | CONFIRMED; facet range `:41-66` exact (`:41` "Aim for about 20 queries") |
| fixed, mixed ~40% validation split; train failures only; select by validation pass rate; fresh queries | snapshot `:136,143,145` (60/40, proportional mix, split fixed), `:153` (only train failures), `:161` (select by validation pass rate), `:175` (5-10 fresh queries, "honest check") | CONFIRMED; facet ranges `:136-163,171-175` exact |
| `SKILL.md:193` compact guidance is not itself evidence any query set follows the safeguards | read `SKILL.md:193` whole: evals.json, PASS/FAIL, ~20 queries, ~3 runs, threshold equality, non-integral runs × threshold, unique strings — **no** variation axes, **no** near-miss negatives, **no** split discipline; `grep -c near-miss SKILL.md` → 0 | CONFIRMED — the facet's sharpest inference holds |
| entry's protocol bullet also lacks the construct-validity guard (facet: audits that merely count queries "can miss" it) | `grep -n near-miss` in the entry → only `:4` and `:78`, both the *opt-in plugin* sense, not the negative-query sense | CONFIRMED |
| source-row scope `corpus/SOURCES.md:151,153` | row 151 = S210, row 153 = S213 | CONFIRMED, exact |
| `corpus/QUALITY.md:36-37` = Q25/Q26 | row 36 = Q25 (counter must fail on mutant), row 37 = Q26 (headline bounded to what the counter measures) | CONFIRMED, exact |
| `plans/round-74.md:47-58,98-99` claim identity/bound distinction | `:47-58` = C1 declaration (depth, SOURCED + assimilation); `:98-99` = "**Bound (Q26, Q51):** … whether a rule sentence is true of the page is a reviewer judgement no counter makes" | CONFIRMED; correctly labelled "not a frozen r75 plan" |
| r74 spotcheck: separate C1 verdict `improved`, page fidelity + counter outputs | `corpus/lessons/round-74-verifier-spotcheck.md:46-64` (C1 coverage table, "**Verdict: coverage `improved`.**"), `:100-105` (per-axis: depth/calibration unchanged) | CONFIRMED; facet correctly calls it a *separate* claim |
| Evidence limits: six blob hashes | `git rev-parse HEAD:<path>` → `d612f22d`, `c103d829`, `9f3e7b33`, `6ed3a9ae`, `d3fa9ba2`, `8bc4cc41` — all six match the facet's abbreviated hashes | CONFIRMED, all six |

## Attack results

**1. Truth — holds.** Every cited byte says what the facet says it says. The one place I expected a possible misquote — whether the lane's compact guidance really lacks the construct-validity guard — resolved in the facet's favor: `SKILL.md:193` carries no variation axes or near-miss rule, and the entry's only "near-miss" occurrences are the plugin near-miss of its native-client refusal, a different concept.

**2. Scope — no error, with one materiality bound.** The facet is explicit that it is a *candidate rule* for a future audit, "not a finding that the current description has failed." `plans/round-75.md` freezes exactly one claim (C1: threshold-equality conditionality, surface `SKILL.md:193` + entry `:56-72`, evidence `R75Facet02/03`) and states "Expansion is not claimed on this already-covered ground"; no committed trigger-query corpus, split assignment, or description-edit audit exists at base. Consequently Facet17's failure modes (duplicated/missing label, one-class split, absent near-miss negatives, validation item in an edit rationale, irreproducible rate) have **no committed object to fire on in round 75** — the control is prospective, and only becomes non-vacuous when a future round freezes the query fixture the facet describes. The facet's own Evidence limits disclose this posture, so it is a bound, not a defect. Integrator should file it as future-round audit design, not an r75-firable control.

**3. Inference — no error found.** Spot-checked the three load-bearing inferences: (a) "an audit that merely counts labelled queries … can miss the construct-validity guard" — true, since the only lane surfaces (`SKILL.md:193`, entry `:48-54`) omit it (grep-verified); (b) "a query set of easy unrelated negatives could yield a reassuring false-trigger rate" — matches the snapshot's own weak/strong negative taxonomy at `:57-65`; (c) "if held-out examples influenced edits, the claimed validation score is no longer held out" — matches snapshot `:145,153`. The facet's reading of "fixed, mixed 40%" is faithful to "~40%", "proportional mix", "keep the split fixed".

**4. Non-vacuity of proposed controls — conditional but well-formed.** Each listed failure mode is byte-observable *given* a frozen query set plus edit history; the facet prescribes recomputation of counts/rates from committed outcome rows, satisfying Q25/Q26 as cited. One binding cost the facet does not name: "validation queries/results absent from the evidence used to choose or revise descriptions" requires commit-level edit attribution that the current corpus does not structurally record; an audit would need to define where edit rationale lives before the leakage check can fail observably.

**5. Duplicate check — partial overlap, not a duplicate.** The r70 entry is wave 1's most-mined artifact (≥19 facets touch it: 02, 05, 07, 10, 17, 18, 19, 21, 22, 23, 28, 30, 31, 32, 40, 41, 42, 45, 51); the dominant cluster attacks threshold-equality wording. Facet17's central claim — the snapshot's query-design rules at `:41-66,136-163,171-175` as a construct-validity guard — is distinct. Material control-level overlap exists with **R75Facet28** (its control: "Keep near-miss negatives sharing vocabulary with the skill … and retain a held-out validation split untouched by wording edits") and with Facet21/Facet42, which cite the same split lines. None of those centers Facet17's failure taxonomy (one-class split, label duplication, validation leakage, easy-negative false reassurance). Flag for the integrator: if a future query-design audit is adopted, 17+28+21+42 controls should merge into one fixture spec rather than four.

**6. Run control test — safe check executed.** The facet's cheap recompute control was exercised on its snapshot-pin claim: `sha256sum` of the committed S210 snapshot reproduces `7cc54fbb…` exactly as pinned in the entry (`:2`) and SOURCES row 151. The pin is reproducible from committed bytes, as the facet's control demands.

## Residual risk / verification gaps

- Upstream revision `69ef37e9…` (S213, entry `:6`) and the S211 tree `dbd4588…` were not verified against the live upstream (no live fetch; the facet likewise claims only that the entry *records* the pins, which is true). The 90-day recheck (`:8`) has not been observed running since 2026-10-25.
- Whether any future r75+ round actually freezes a trigger-query corpus determines whether this facet ever becomes firable; today it cannot fail.
- The facet's truncated prose (`:41-66` end boundary) was verified inclusive of content through `:65` with `:66` blank — boundary-accurate, no content missed.

## Report trailer

Attack target: `.ufo/waves/round-75/w1/R75Facet17.md`. Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe` (kotoba-shokunin `master`). All checks read-only git/file inspection; one sha256 recomputation; no live fetch, no edits outside this report, no scratch artifacts written.

Evidence paths (relative to `kotoba-shokunin`):
- `corpus/knowledge/skill-eval-artefacts-round70.md:2,6-9,13-16,48,56-72,74,78`
- `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:41,43-49,54-65,136,143,145,153,161,175`
- `SKILL.md:193`
- `corpus/SOURCES.md:151,153`
- `corpus/QUALITY.md:36-37`
- `corpus/lessons/round-74-verifier-spotcheck.md:46-64,100-105`
- `plans/round-74.md:47-58,98-99`
- `plans/round-75.md:5-11` (frozen r75 C1 — scope bound for the candidate rule)
- Sibling-overlap comparison: `.ufo/waves/round-75/w1/R75Facet28.md`, `R75Facet21.md`, `R75Facet42.md`
