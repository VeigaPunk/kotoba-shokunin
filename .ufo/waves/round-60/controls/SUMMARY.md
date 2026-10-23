# Round 60 — pre-data control receipts, counter v1 (summary; the seat reports beside this file are the receipts)

Counter v1 `verifiers/check_scoped_rules.py` sha256 `6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440`
(`TARGET = 3`), frozen at `49c3e87d`; worlds built on `49c3e87d`. Predicate `C1 predicate: --fetch exit 0 (F>=TARGET)`.

| control | role | S (snapshots) | F (live) | exit | predicate |
|---|---|---|---|---|---|
| CtlDoNothing (freeze rev, base, header-only world) | executor | 0 of 0 | 0 of 0 | 1 | NOT MET |
| CtlJunk | mutation-tester | 0 of 7 | 0 of 7 | 1 | NOT MET |
| CtlAllFalse (invented rows, URLs, snapshots on pinned hosts) | mutation-tester | 7 of 7 | 0 of 7 | 1 | NOT MET |
| CtlNoReader (real census rows, no snapshots) | executor | 0 of 4 | 0 of 4 | 1 | NOT MET (also 0 of 4 under v2, same report) |
| CtlFabSnapshot (real tokens/URLs/keys, invented quotes and action lines) | mutation-tester | 1 of 4 | 0 of 4 | 1 | NOT MET |
| CtlLabelShortcut (rows from labels, hook rows, counter fixtures) | mutation-tester | 0 of 2 | 0 of 2 | 1 | NOT MET |
| CtlWrongKey | executor | — | — | — | **cancelled** at the settle deadline (dispatched about 10:47Z, cancelled 12:04Z), no receipt, no world committed in its sandbox |
| CtlInventedAction | executor | — | — | — | **cancelled** at the settle deadline (same times), no receipt, no world committed |

No v1 control meets the predicate. The offline snapshot line alone is met by a fabricated world (CtlAllFalse 7 of 7), so
it is committed-bytes evidence only; the live conjunct rejects it. `CtlFabSnapshot` found the base-URL conjunct the W0
census never scored (three census pages are base rows S043/S048/S049), which led to erratum E1 and counter v2
(`plans/round-60.md` § Erratum E1). The two cancelled seats leave the wrong-key and invented-action conjuncts without a
pre-data control receipt; the counter's own self-test arms (wrong `description` key at Cursor `:65`/`:99`, one-word
action overlap) and build-wave item `ExecKeyForms` stand in, and that gap is disclosed in the report.
v2 control receipts: `.ufo/waves/round-60/controls-v2/`.
