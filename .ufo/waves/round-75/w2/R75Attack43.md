# R75Attack43 — independent attack on R75Facet43

## Axes
Calibration, depth, freshness, and evidence/provenance scope.

## Verdict
The central factual claim survives: the equality mismatch is supported by the pinned guide and runner bytes. The facet correctly distinguishes prose/counter coverage from behavioral execution and does not claim that its proposed control has already run. Its proposed boundary table is directionally useful, but is incomplete unless it models aggregation by query string and label collisions; a plain `(threshold, runs, multiplicity)` table can miss an implementation-specific overwrite behavior.

## Independent evidence at HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`

- `corpus/knowledge/skill-eval-artefacts-round70.md:58-72` states guide `above`, runner `>=`, threshold default 0.5, 3 runs default, and the caveats for duplicate strings and non-default thresholds. The statement is properly bounded to the guide and reference runner; `:76-82` explicitly refuses a universal client-runtime claim.
- Reopened `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:88-93`: the guide says should-trigger passes if rate is “above a threshold” and should-not-trigger if “below.” It does not state equality behavior.
- Reopened `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234,264-267`: results are appended into `query_triggers[query]` (including failed runs as `False`), rate is `sum(triggers) / len(triggers)`, positives use `>=` at line 232 and negatives `<` at 234; defaults are 3 runs and threshold 0.5. Thus at equality the positive-query predicates differ. A single query with three outcomes cannot have rate 0.5; two occurrences of a query contribute six outcomes under the grouping shown, so 3/6 reaches equality.
- Cheap arithmetic check: with threshold 0.5, 3 runs gives rates {0, 1/3, 2/3, 1}; with six outcomes it includes 3/6. At threshold 1/3 and 3 runs, equality is reachable. In both examples the strict positive predicate is false and inclusive predicate true. No runner execution or live fetch was needed.
- `verifiers/check_skill_evals.py:125-175` (as cited by facet) checks quote/snapshot and row structure, not those arithmetic predicates. So the facet's distinction between provenance coverage and behavior proof is accurate.

## Attack on the proposed control

A duplicate-only multiplicity input is not enough to model this exact code: `query_items[query] = item` at line 218 retains the last item for that query, while all occurrences' outcomes are aggregated at lines 213-229. If repeated identical query text carries inconsistent `should_trigger` labels, whichever item was last completed determines which comparator is applied to the aggregate. The facet's control mentions duplicate multiplicity but does not mention label consistency or this last-item selection. This is a real implementation-specific boundary for a control intended to mirror `run_eval.py`; it does not falsify the stated equality discrepancy.

## Smallest safe correction

Keep the finding and its explicit scope. For the proposed fixture/table, either require every repeated query string to have the same `should_trigger` label, or include a mixed-label duplicate case and assert the actual aggregation/last-item behavior. Do not present the existing snapshot counter as enforcing this behavior. No lane edits, live fetches, or source execution performed.

Report: `.ufo/waves/round-75/w2/R75Attack43.md`
