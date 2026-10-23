# Round 59 — pre-data control receipts (summary; the seat reports beside this file are the receipts)

Counter `verifiers/check_hook_files.py` sha256 `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`
(`TARGET = 4`, `NEW_TARGET = 5`), frozen at `4b2125c9`; worlds built on `67b68e0f`. Predicate
`C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET)`.

| control | role | S (snapshots) | F (live) | G | exit | predicate |
|---|---|---|---|---|---|---|
| CtlDoNothing (freeze rev, base, header-only worlds) | executor | 0 of 0 | 0 of 0 | 0 | 1 | NOT MET |
| CtlJunk | mutation-tester | 0 of 7 | 0 of 7 | 0 | 1 | NOT MET |
| CtlAllFalse (invented rows, URLs, snapshots on pinned hosts) | mutation-tester | 7 of 7 | 0 of 7 | 0 | 1 | NOT MET |
| CtlNoReader (real rows, no snapshots) | executor | 0 of 6 | 0 of 6 | 0 | 1 | NOT MET |
| CtlFabSnapshot (real tokens/URLs, invented quotes in fabricated snapshots) | mutation-tester | 6 of 6 | 0 of 6 | 0 | 1 | NOT MET |
| CtlFabEvents (real everything, invented events) | executor | 0 of 6 | 0 of 6 | 0 | 1 | NOT MET |
| CtlOffTopic (round-58 command rows relabelled) | executor | 0 of 0 | 0 of 0 | 0 | 1 | NOT MET |
| CtlLabelShortcut (tokens/events/quotes/snapshots from labels and the counter's fixtures) | mutation-tester | 0 of 0 | 0 of 0 | 0 | 1 | NOT MET |

No control meets the predicate. Limit recorded before data: the offline snapshot line alone is met by fabricated
worlds (CtlAllFalse 7 of 7, CtlFabSnapshot 6 of 6), so it is committed-bytes evidence only, never the claim's
measure; the live `--fetch` conjunct is what rejects them.
