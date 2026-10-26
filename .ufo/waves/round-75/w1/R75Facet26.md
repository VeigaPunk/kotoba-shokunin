# R75Facet26 — description trigger-test calibration

## Axis
Calibration / falsifiability of the description-trigger evaluation advice in `SKILL.md` lines 193–194, grounded in `corpus/knowledge/skill-eval-artefacts-round70.md` lines 48–72.

## Observed committed evidence
- `SKILL.md:193` describes a trigger set of ~20 queries at ~3 runs and says threshold/run count should be non-integral; it cites the evaluation artefact entry.
- The entry distinguishes guide advice from normative specification at `corpus/knowledge/skill-eval-artefacts-round70.md:13-16`.
- The source-derived facts at `:33-34` distinguish guide wording (“above” threshold) from implementation `>=`; `:58-72` explains equality cases, duplicate query strings, and non-default thresholds. Its action is to keep threshold × runs non-integral, deduplicate strings, or state the applied rule.
- The entry says the guides recommend about 20 queries, ~3 runs, ~40% held-out validation at `:48-54`; these are recommendations, not guarantees of statistical power or client behavior.
- Historical plan `plans/round-74.md:47-61` declares depth and freshness claims, not a frozen r75 claim; its provenance must not be treated as an r75 declaration.

## Assessment (inference)
This is a well-calibrated, falsifiable candidate: the precise boundary discrepancy is anchored to a guide and a pinned implementation, and the concrete controls directly avoid the equality boundary. But “non-integral” is underspecified operationally: a runner may aggregate duplicate prompts or use a threshold different from 0.5, and a count-level statement alone does not establish actual repeated-run semantics. The entry does address duplicate strings and alternative thresholds, so the remaining risk is whether a future audit tests the exact runner/configuration rather than merely checking prose or nominal settings.

## Concrete check/control
For an r75 audit, freeze the actual threshold, per-query run count, query identity normalization, and aggregation rule before scoring. On the exact committed runner, include a should-trigger query at equality (choose an even run count with threshold 0.5, e.g. 2/4 successes) and assert the expected guide-vs-runner verdicts separately; include a duplicate-string case and a non-default threshold whose product with run count is integral. Preserve command, runner revision, and outputs. Report this as a control of the equality claim, not evidence that the overall skill description is effective.

## Evidence basis / limits
Committed bytes read: `kotoba-shokunin/SKILL.md:193-194`; `kotoba-shokunin/corpus/knowledge/skill-eval-artefacts-round70.md:13-16,33-34,48-72`; `kotoba-shokunin/plans/round-74.md:47-61`. No live fetch, runtime execution, or r75 claim declaration was examined. Confidence: high for the textual distinction and proposed boundary control; no conclusion about actual r75 runner behavior.