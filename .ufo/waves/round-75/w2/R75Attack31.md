# R75Attack31 — independent falsification of R75Facet31

## Verdict

**Survives the narrow factual attack; actionable calibration flaw in the candidate is not established.** At measured lane revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`, the exact local S211 snapshot supports the equality comparator and per-query aggregation described in the report. The proposed arithmetic check is meaningful for the named reference implementation, but the report overstates the “duplicate query entries” control as if duplication necessarily creates additional trials: the counter groups by query string, so duplicate entries do so only if they are each scheduled as separate work items (which the enclosing loop does at lines 190–211); duplicate entries with differing `should_trigger` values are additionally collapsed into one result and `query_items[query]` retains whichever item is encountered last. This is a real limitation on interpreting that advice, not a contradiction of the central scoped finding.

## Independent evidence

- `corpus/knowledge/skill-eval-artefacts-round70.md:58–72` states the claim and bounds it to the guide wording and `run_eval.py`.
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213–241` groups runs by exact query string, appends one result for each submitted future, divides `sum(triggers)` by collected run count, uses `>=` for should-trigger and `<` for should-not-trigger, and emits one result per distinct query key.
- Same snapshot `:190–211` schedules every item in `eval_set` for each run index, so repeated identical query entries are indeed scheduled as repeated trials; `:266–267` sets default three runs and threshold 0.5.
- Therefore one unique query with 3 runs cannot attain 0.5; with 4 runs and 2 positives it can, and the two should-trigger predicates disagree exactly at equality. At threshold 1/3 with 3 runs, equality is attainable (one positive); at 2/3 it is attainable (two positives). In each case `>=` passes where strict “above” fails. Duplicate identical entries under default settings yield six trials and equality is possible at 3/6.

## Attack on proposed control / scope

“De-duplicate query strings” is not an unambiguously safe remediation: duplicate entries are precisely what the implementation counts as extra executions in the denominator, while the output exposes only one result per string. If duplicates differ in `should_trigger`, the result's label depends on completion-order assignment to `query_items`, not an explicit conflict rule (`:215–230`). A report author should identify the exact eval-set semantics and comparator rather than blindly deduplicate. The source itself is enough to identify that caveat; no execution against model-dependent CLI was needed or performed.

No evidence here supports generalization beyond these two pinned texts, and the entry explicitly refuses that generalization. The report's recommended cheap mutant test is not evidence of current defect; it is a proposed future control. No source or report changes were made. `lsp` is not mounted in this session (the available-tool response lists only `ast_edit, debug`); this is a text/snapshot review, not semantic LSP proof. No live fetch or tool install.
