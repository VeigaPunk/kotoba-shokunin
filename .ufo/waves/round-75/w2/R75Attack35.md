# R75Attack35 — attack on R75Facet35

## Verdict
**Finding survives, narrowly.** The suggested arithmetic is a valid sufficient safeguard for the cited reference runner when query strings are unique; the report identifies a real caveat in that its applicability is implementation-specific, not a rule of the guides. I found no source contradiction or evidence that the SKILL instruction itself is false. The material actionable point is to make the rule's scope explicit, not to replace it with a stronger universal claim.

## Axes
Calibration; consistency; operability.

## Independent evidence / counterexample
At measured revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `SKILL.md:193` says to keep runs × threshold non-integral and query strings unique, then directs to the round-70 knowledge entry. That entry at `corpus/knowledge/skill-eval-artefacts-round70.md:13-16` explicitly limits the sources to guide advice and one implementation, and `:58-72` states the equality-only disagreement and the action.

I reopened the pinned source bytes ` .ufo/waves/round-70/snapshots/S211-run_eval.py.txt` (sha prefix recorded in the knowledge source table): `run_eval` schedules `runs_per_query` executions for every eval-set item (`:198-211`), aggregates outcomes by exact query string (`:213-229`), and compares should-trigger rates with `>=` (`:230-234`). Thus duplicate strings can change the actual denominator; for example, with two identical entries, 3 runs each, and threshold 0.5, the denominator is 6, and 3 triggers produce equality. With a unique string, 3 runs and threshold 0.5 cannot produce equality. More generally the actual denominator for this implementation is `runs_per_query × duplicate-entry count`, so uniqueness plus non-integral `runs_per_query × threshold` prevents equality for a unique query. This confirms the report's aggregation caveat, but also shows its stated control—record actual denominator and threshold—is sufficient and non-vacuous.

No safe local runtime check can execute this external evaluator's `claude -p` model runs without live external execution. Static inspection of the pinned implementation is direct evidence for the claimed aggregation/comparator behavior; no live fetch or experiment was performed.

## Attack assessment / smallest correction
The report's caveat is a defensible precision correction, not a demonstrated defect in the guard: it already says query strings must be unique, which directly excludes the duplicate-string counterexample, and the knowledge entry already scopes the claim to the reference implementation. Its proposed per-query denominator check catches non-default settings and aggregation exactly. No broader defect or out-of-scope issue established.

Smallest safe correction if further wording is desired: say explicitly that `runs × threshold` means the **actual per-query-string denominator** used by the cited runner, and label the recommendation as runner-specific guidance. Avoid implying this rule reconciles all guide/implementation semantics; it only avoids equality-boundary cases.

## Evidence boundary
Read-only inspection of `SKILL.md:193`, the target report `w1/R75Facet35.md`, `corpus/knowledge/skill-eval-artefacts-round70.md:13-16,58-72`, and the pinned S211 source lines above. No lane-source edits, runtime experiment, or live fetch.

Report: `.ufo/waves/round-75/w2/R75Attack35.md`