# R75Facet18 — guide recommendation versus implementation boundary

## Observed evidence

- `corpus/knowledge/skill-eval-artefacts-round70.md:13-16` explicitly says S209/S210 are guides rather than the specification, and labels their numerical advice non-normative. Lines 33-34 separate S213's “above” threshold wording from S211's `>=` implementation; lines 58-72 explain the equality boundary.
- The entry's factual premise is testable on its pinned source snapshots: the entry names S213/S211 and their committed snapshot hashes at lines 1-5. It says at lines 62-70 that a unique query under three runs and threshold 0.5 cannot tie, but duplicated identical query strings can aggregate to six observations and yield 3/6. This is a claim about one reference implementation, not clients; the scope refusal at lines 74-82 expressly disclaims native client execution.
- The r74 spotcheck documents source and judgement checks separately: `corpus/lessons/round-74-verifier-spotcheck.md:55-60` reports committed snapshot hashes and a page-fidelity judgement as distinct rows, while lines 63-64 limits evidence-verified status to the counter output/self-test. This is a useful precedent for not describing source-byte verification as independent semantic validation.

## Assessment (inference)

This is a narrow, falsifiable audit candidate, and its calibration is comparatively strong: authority, comparator, exact-equality case, aggregation caveat, and refusal to generalize to clients are explicit. The risk is temporal and evidentiary, not an observed factual error: round-70 snapshots substantiate the historical claim, but do not establish that upstream sources or any current evaluator still have those semantics. The r74 report's re-opened sources cannot upgrade this separate S211/S213 evidence.

## Concrete check/control

Use only committed bytes: hash the S211/S213 snapshot files and compare to the pins recorded in the knowledge entry; inspect the relevant source lines and independently calculate the listed rates. Control cases: unique query with 3 trials at 0.5 (no equality possible); duplicate same query with 6 aggregated trials, 3 successes (equality); and a should-not-trigger equality case. Record the implementation's grouped denominator and comparator separately from the guide's wording. Label the result “historical guide/reference-implementation comparison”; make no current-client or current-upstream claim absent a separately authorized re-open.

**Confidence:** High that the entry is bounded and its claims are falsifiable from pinned snapshots; moderate that it is a useful r75 audit candidate, since current behavior is not evidenced.

**Remaining unknowns:** Whether S211/S213 changed after the committed snapshots; whether any present client uses this evaluator or matching comparator semantics.

## Evidence paths / commands

Paths relative to `kotoba-shokunin`:
- `corpus/knowledge/skill-eval-artefacts-round70.md:1-8,13-16,33-34,56-82`
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt` and `S213-optimizing-descriptions.md` (pins are recorded in the entry's source rows)
- `corpus/lessons/round-74-verifier-spotcheck.md:55-64`

Commands for committed-byte reproduction: `git show <rev>:.ufo/waves/round-70/snapshots/S211-run_eval.py.txt`; `git show <rev>:.ufo/waves/round-70/snapshots/S213-optimizing-descriptions.md`; `sha256sum` on extracted committed bytes. No live fetch or model experiment performed.
