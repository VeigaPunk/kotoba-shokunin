# ExecIndexRow — r90-w1 seat report (carry-in index-row repair)

Seat: ExecIndexRow (executor, leaf). Scope held: `corpus/README.md` (one index row), `receipts/index-*.txt`, `.ufo/waves/round-90/w1/` bundle. No tool installs; no pacman; no git write anywhere (scratch clone verified via `git rev-parse --show-toplevel` before use; no commit made in it); scratch dir removed before this report.

## Change

`corpus/README.md` line 186 (only line added to the file):

```
| Round-89 verifier spot-check (indexed round 90) | `lessons/round-89-verifier-spotcheck.md` | the non-author closure of round 89 (kotoba round 89 admitted; C1 and C2 evidence-verified, the S258/S259 admits and the assimilation reject agreed; routed notes 1–3 for round 90); landed at `0c20d8a` after the r89 landing measurement, indexed round 90; written by the hyaku closure, never edited here |
```

- Format mirrors the r87/r88 sibling rows (README lines 181–182), placed to close the round-89 cluster before `## Frontier`.
- Lateness note is inline, per the house convention of the earlier late-indexed spot-check rows ("landed at `<rev>` without an index row … indexed round N"): the file was committed at the round base `0c20d8a` ("round-89 verifier spot-check (integrator, hyaku)"), i.e. after the r89 landing measurement pinned at `99ddd746`, so no r89 receipt could have indexed it. Nothing else in the file changed.

## Gate readings

Lane run (`receipts/index-integrity.txt`; `git rev-parse master` → `6fa5bb6d4ceeb51f0455e512a52d8b75628f404c`):

- `corpus.index.unindexed` **0**, verdict **PASS** (base: 1, DRIFT; `unindexed_detail` empty). `index_patterns` 198 → 199 (the new column-2 token); `stale_patterns` 0, `missing_paths` 0 (the token matches the tracked file); `report_total` 146 and `commit_total` 62 unchanged (the row adds no report pointer and no commit citation); `report_dead` 0, `commit_nonhash` 0.
- **Exit 1, not the 0 the seat spec named.** All four DRIFT rows were already DRIFT at base (`base-integrity.json`, rc=1) and are outside this seat's write scope:
  - `corpus.index.tracked_files` 181 vs baseline `expect 172`, `corpus.pointers.report_total` 146 vs 127, `corpus.pointers.commit_total` 62 vs 59 — the frozen baseline (`verifiers/corpus-baseline.json`, frozen bytes, last re-recorded against the round-87 tree at `e03f9e22`) is stale; its own notes establish the landing re-record class ("Index rows … committed first; the gate's own counts were observed afterwards", `round85_rerecord`/`round86_rerecord`). Refreshing those three `equal` expectations is the L1's integration act, not a seat edit of frozen bytes.
  - `corpus.pointers.commit_unresolvable` 1 (`corpus/lessons/round-81.md:8`, the correctly-described absent test-world commit) — declared carried red ("expectation stays 0, gate remains red"); the site lives in a file this seat does not own.

Q05 regression arm (`receipts/index-regression.txt`, scratch clone `/fast/scratch/hyaku/kotoba-r90/ExecIndexRow/repo`, toplevel asserted, no git mutation, deleted after):

- with-row world (lane README copied in): `"unindexed": 0` (line 21).
- row removed (pristine committed README restored; guard line `README == committed bytes (row removed)`): `"unindexed": 1` (line 170).
- The new row is the sole cause of the 0↔1 flip; rc=1 in both scratch worlds is dominated by the same carried baseline DRIFTs named above.

## Handoff

`.ufo/waves/round-90/w1/INDEX_READY` written: `corpus.index.unindexed 0`.

## Findings for the L1

1. **Predicate-vs-frozen-state deviation (disclosed, not rescued):** the seat spec's "exit 0" is unreachable at this tree without editing frozen bytes (`corpus-baseline.json`) or a non-owned file (`lessons/round-81.md`). The named red (`unindexed 1`) is green; the residual exit 1 is the declared stale-equal re-record class plus the declared carried `commit_unresolvable`. Suggest the landing re-record updates the three `equal` expectations (tracked 181, report_total 146, commit_total 62 — plus whatever the round's own files add) exactly as in `round86_rerecord`, and states the `commit_unresolvable` residual as carried.
2. No counter defect found in the frozen gate; no amendment needed. No other corpus file touched.
