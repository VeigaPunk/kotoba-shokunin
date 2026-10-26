# R75Attack19 — independent falsification of R75Facet19

**Verdict: survived attack; central comparator distinction is substantiated and materially actionable within its stated documentation/reference-runner scope.** I found no evidence that the report overstates this as native client behavior. The round-70 entry itself now explicitly qualifies the distinction: lines 86–88 say the guide's wording does not resolve equality and `>=` is an implementation fact, not the guide's definition.

## Re-opened evidence and cheap check

At the measured lane revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `corpus/knowledge/skill-eval-artefacts-round70.md:33-34` quotes guide “above” and implementation `>=`; lines 58–72 state the discrepancy and bound it. The frozen source bytes support that account:

- `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:83-92`: passes are defined by whether the skill was invoked; § multiple runs sets the should-trigger wording to rate “above a threshold” and suggests 0.5.
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234`: aggregation is by query string, rate is `sum(triggers)/len(triggers)`, and the should-trigger predicate is `trigger_rate >= trigger_threshold` (line 232).
- Same snapshot lines 266–267: defaults are three runs and threshold 0.5.

The stated boundary arithmetic checks out: with 3 runs and threshold .5, possible rates are 0, 1/3, 2/3, 1, so equality is impossible for one query string listed once. Two runs can yield 1/2; duplicate occurrences pooled by the implementation can yield 3/6; with three runs, thresholds 1/3 or 2/3 can be reached. Thus the strict-versus-inclusive distinction is a real, one-directional pass/fail divergence at equality, while the report properly avoids asserting that the default unique-query setup necessarily hits it.

## Attack result / residual caveat

The proposed arm that produces an equality-rate should-trigger case and compares the two predicates is non-vacuous: strict `>` fails and inclusive `>=` passes. Naming the comparator is a useful control if a report presents a pass rate. The duplicate-query arm is relevant only when exercising this implementation's aggregation: lines 213–229 pool all occurrences under the same query string. In that case, entries with the same string but inconsistent `should_trigger` labels would also collapse to one `query_items[query]` record (overwritten as futures complete), making that malformed/ambiguous fixture unsuitable as an independent labeled-case test; use repeated occurrences with consistent labels or avoid duplicates. This caveat does not invalidate the ordinary unique-query/even-runs example.

## Verification gaps

No live fetch or execution of the reference runner was needed; this was a static source comparison plus arithmetic check. The `lsp` device was not available in the mounted tool set, so semantic LSP checks were unavailable; these are documentation/snapshot facts and were checked directly in the cited bytes. No lane source or other lane files were modified.