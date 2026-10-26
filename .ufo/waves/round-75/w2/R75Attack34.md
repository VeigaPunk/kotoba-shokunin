# R75Attack34 — independent falsification of R75Facet34

## Axes
Consistency; operability.

## Verdict
The central factual distinction survives; the proposed actionable scope is modest and well bounded. However, the specific claimed duplicate-query equality case is not a safe/valid control against the reference runner: duplicate query strings are collapsed into one dictionary key and `query_items[query]` is overwritten by whichever duplicate item was processed last. If duplicate entries disagree on `should_trigger`, the runner silently attributes all aggregated runs to the last item’s label. Same-label duplicates do aggregate and do produce equality as described, but they also change the effective number of runs and weight that query relative to others. Thus the report’s counterexample is real for same-label duplicates but its proposed test does not establish general duplicate-handling correctness.

## Evidence

At measured master `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `corpus/knowledge/skill-eval-artefacts-round70.md:33-34,62-72` contains the `above` vs `>=` distinction, default 3 runs/0.5 threshold, per-query-string aggregation, and recommendation. The independent exact cited implementation is `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt`: lines 200-211 submit a future for every eval item/run; lines 213-225 aggregate results by `item["query"]` and overwrite `query_items[query]` on each future; lines 227-234 compute the rate and use the surviving item’s `should_trigger`. Lines 266-267 set defaults 3 and 0.5. Therefore same-label duplicate entries yield 6 trials in one denominator and can reach 3/6 equality; conflicting-label duplicate entries yield a last-writer label assignment, not two independently assessed queries.

Cheap arithmetic check (no live runner invocation): for three successes of six trials, `3/6 == 0.5`, so `>=` passes and strict `>` does not. For a single three-run query, possible rates are 0, 1/3, 2/3, 1, so equality at 0.5 is impossible. At threshold 1/3 and three trials, one success reaches equality. These cases match the entry’s narrow arithmetic statement.

The entry’s scope refusal at lines 76-82 and its round-75 correction at lines 86-88 explicitly distinguish a reference implementation from client/native behavior and say the guide leaves equality unresolved. This correction mitigates the potential misreading that `>=` defines the guide. No evidence supports actual client routing claims, and the report expressly refuses them.

## Attack / smallest safe correction

Retain the bounded candidate, but make its control table include duplicate query strings with both consistent and conflicting `should_trigger` labels, and report the runner’s last-writer behavior as an implementation quirk rather than implying deduplication alone guarantees a sound independent-query score. If the intended control only tests equality semantics, use same-label duplicates and state that restriction. The source entry itself does recommend deduplicating query strings or declaring the comparator, so this is a refinement, not a reason to reject its central finding.

## Report

Report: `.ufo/waves/round-75/w2/R75Attack34.md`
