# Round 60 — pre-data control receipts, counter v2 (summary; the seat reports beside this file are the receipts)

Counter v2 `verifiers/check_scoped_rules.py` sha256 `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`
(`TARGET = 3`), frozen at `b1cd64bb`. Predicate `C1 predicate: --fetch exit 0 (F>=TARGET)`. The three seats were
first refused twice by the session job cap ("Background job limit reached (100)") and spawned on the third send at about
12:05Z; the harness renamed them `CtlRescoreV2-3`, `CtlReopenForged-3`, `CtlReopenHeldKey-3` (same tasks, unchanged).

| control | role | worlds | result under v2 | predicate |
|---|---|---|---|---|
| CtlRescoreV2 | executor | the six v1 worlds (`controls/SUMMARY.md`) | max F = 1; all exit 1 (CtlAllFalse still S 7 of 7 offline) | NOT MET |
| CtlReopenForged a–c | mutation-tester | base URL with no `re-opens`, wrong base id, non-base id | S 0 / F 0, exit 1 | NOT MET |
| CtlReopenForged d | mutation-tester | real rows/keys/quotes/actions; the three re-open snapshots are round-53 scratch bytes (2026-10-22) under rows that claim a fetch today | S 3 / F 3, `--fetch` exit 0 | **MET** |
| CtlReopenHeldKey a | mutation-tester | re-open whose base row already holds K | S 2 / F 2, exit 1 | NOT MET |
| CtlReopenHeldKey b | mutation-tester | locale / enterprise alias URLs with real content | S 3 / F 3, `--fetch` exit 0 | **MET** |
| CtlReopenHeldKey c | mutation-tester | live redirect to a different base key | S 3 / F 2, exit 1 | NOT MET |

Two worlds meet the predicate. Each carries the real table content and forges only source provenance (fetch time, or an
alias of a held page), which the counter cannot authenticate. Per the phase-4 rule the claim was declared exploratory
before any C1 data entered the lane (`plans/round-60.md` § Erratum E2, commit `49f7ff22`); the counter, target and
predicate were not changed.
