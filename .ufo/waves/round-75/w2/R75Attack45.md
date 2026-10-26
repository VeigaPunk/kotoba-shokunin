# R75Attack45 — independent attack on R75Facet45

## Verdict
**Finding survives as a bounded implementation/documentation mismatch; its proposed authoring controls are partly overstated and not equally actionable.** The source wording and runner comparison are independently present in committed bytes at lane revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`. The report correctly labels the instability concern as an inference rather than a quantified result. However, “keep threshold × runs non-integral” is not a complete general control when identical query strings aggregate multiple runs, and deduplication is a behavior-changing data constraint rather than universally safe advice. The strongest control is to specify which comparator governs the actual implementation and include a comparator-boundary fixture.

## Axes
Depth, freshness, consistency, calibration, operability, adjacency.

## Independent evidence and cheap check
Re-opened `corpus/knowledge/skill-eval-artefacts-round70.md:48-72` and committed snapshots at `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:136-167` and `S211-run_eval.py.txt:213-242,266-267`.

- S210 says validation is only for checking generalization during revisions, yet step 5 explicitly says select the best iteration by validation pass rate (`:151-161`). Thus “never guides edits” does not mean the validation set is never used in selection; R75Facet45 correctly identifies the set as serving a selection criterion and appropriately stops short of claiming a confidence guarantee.
- S210 separately recommends fresh, never-optimized queries as an honest final generalization check (`:171-175`). This makes the facet's recommendation to use a separate untouched test set a reasonable distinction, but it is a proposed control, not what the cited guide itself requires.
- S211 groups runs by query string (`:213-229`), computes the rate, then uses `>=` for should-trigger and `<` for should-not-trigger (`:227-242`). Its default is three runs and threshold 0.5 (`:266-267`). Therefore the equality boundary exists in the runner, while a unique query with the defaults cannot realize equality. A duplicated string can: two entries × three runs = six observations, and 3/6 = 0.5. This independently confirms the report's cited edge-case structure.
- S210 uses “above” for should-trigger and “below” for should-not-trigger; equality is not assigned by that wording. The documentation-versus-implementation discrepancy is real for this pinned evidence, not evidence of a universal client behavior.

Cheap arithmetic check: for a single unique query and defaults, `k/3 = 0.5` has no integer solution; for duplicate aggregation, `k/6 = 0.5` at `k=3`. For threshold `1/3` and three runs, equality is realizable. These match the entry's explanation.

## Attack / scope assessment
The factual claim is true and scoped. No actionable counterexample defeats it. Potential weakness: the proposed “keep threshold × runs non-integral” suppresses equality only if the relevant denominator is the actual collected observations per query string. The implementation aggregates duplicate entries, so nominal runs-per-query alone may understate that denominator; additionally each query may have failures recorded as `False` (`:221-225`). Deduplicating may alter intended weighting/label semantics and is not always a valid correction. Stating the comparator and testing an equality case are safer than trying to avoid every equality-producing configuration.

The statistical warning is appropriately calibrated: the snapshots establish repeated optimization/validation-based selection, but do not quantify selection bias or guarantee a particular magnitude. Per-query counts/rates and a separate fresh test set are reasonable controls, not sourced prescriptions. There is no demonstrated duplicate report: `R75Facet44` is a separate wave-one report on the threshold comparator, not evidence that this finding is false; avoid treating mere overlap as independent support.

## Smallest safe correction
Retain the bounded mismatch and caveat. Phrase control as: freeze queries/splits/labels and the comparator; test a threshold-equality fixture using the actual per-query aggregation; use a separate fresh query set for a final generalization claim. Present deduplication and non-integral threshold×effective-run counts only as optional ways to avoid the specific equality case, not universal requirements.

No lane files changed; only this report was written. No upstream live fetch or execution was needed: the committed snapshot bytes directly expose the comparison and arithmetic cases.

Report path: `.ufo/waves/round-75/w2/R75Attack45.md`
