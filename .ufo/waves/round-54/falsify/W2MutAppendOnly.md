Result: DONE — ten single-point mutants were tested; each was killed by its targeted detector, while merge exclusion needed a synthetic merge fixture because the real ranges contain no SOURCES merge commit.

## Setup and pristine checks

The verifier was tested only in the isolated clone `/fast/scratch/hyaku/kotoba-r54/W2MutAppendOnly`, checked out at `58db81c4465b0e9b07ef2485b87d8970683afac6`. The source was pristine before the probes, SHA-256 `d4d1d62b16ededc8f31e5df71738285bd88768a2b3e3b9824b2782143fef3805`.

Commands and observed outputs:

- `python3 -B verifiers/check_sources_append_only.py --self-test` → `self-test: 0 failure(s) over 14 assertions`; exit 0.
- `python3 -B verifiers/check_sources_append_only.py --base 55973a20 --rev e792607e` → `breach e792607e8 S050 anchor: …`; `sources append-only breach 1 change(s) in 1 of 1 commits`; exit 1.
- `python3 -B verifiers/check_sources_append_only.py --base 55973a20 --rev 'e792607e^'` → `sources append-only rows clean: 0 commits scanned, 0 protected-cell changes`; exit 0.
- `python3 -B verifiers/check_sources_append_only.py --base 422ffd10 --rev 58db81c4465b0e9b07ef2485b87d8970683afac6` → `log 5a097e12b S046 used-by: …`; `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes`; exit 0. Thus S046's `used-by` edit was logged, and appended rows did not cause a breach.

## Mutants

All edits were one behavior-bearing point at a time in `verifiers/check_sources_append_only.py`. “Killed” means the listed detector produced an outcome different from its expected result.

| # | Single-point mutant | Expected detector | Actual output / exit | Verdict |
|---|---|---|---|---|
| 1 | Line 30: remove `status` from `PERMITTED`. | `--self-test`: permitted status change stays a note. | `FAIL status in place: 1 breach(es), wanted 0`; `FAIL status in place: 0 log note(s), wanted 1`; 2 failures, exit 1. | KILLED |
| 2 | Line 30: add `anchor` to `PERMITTED`. | `--self-test`: anchor edit is a breach. | `FAIL anchor in place: 0 breach(es), wanted 1`; `FAIL anchor in place: 1 log note(s), wanted 0`; 2 failures, exit 1. | KILLED |
| 3 | Line 71: replace removed-row breach append with `continue`. | `--self-test`: removed row is a breach. | `FAIL row removed: 0 breach(es), wanted 1`; 1 failure, exit 1. | KILLED |
| 4 | Line 32: change header regex from `id` to `idx`. | `--self-test`: header must be parsed. | 5 failure messages (missing status/used-by notes and anchor/teaches/removed-row breaches); exit 1. | KILLED |
| 5 | Line 31: change row ID minimum from `S` + 3 digits to 4 digits. | Red range must report the S050 anchor breach. | `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes`; exit 0 instead of 1. | KILLED |
| 6 | Line 100: ignore `base` and set range to `rev`. | Green range ending at `e792607e^` must be clean. | 12 breaches in 3 of 15 commits (including `S022 teaches`, `S019 scope/anchor/teaches`); exit 1 instead of 0. | KILLED |
| 7 | Line 101: remove `--no-merges`. | Merge-resolution-only protected edit should be excluded; tested on actual round history and a constructed two-parent fixture. | Actual round-54 range stayed clean, 1 commit scanned, exit 0 (survived that range). `git rev-list --merges --all -- corpus/SOURCES.md | wc -l` returned `0`. On the synthetic fixture, pristine gate: 2 commits scanned, clean, exit 0; mutant: `breach 0a1421969 S001 anchor: original anchor -> merge-resolved anchor`; 1 breach in 1 of 3 commits, exit 1. | KILLED by synthetic merge detector; real-range survival is a coverage limitation, not a contract change. |
| 8 | Line 183: return 0 instead of 1 when breaches exist. | Red range must exit 1. | Breach still printed for `S050 anchor`, but process exited 0. | KILLED |
| 9 | Line 77: permit only `status` and `recheck`, not `used-by`. | Round-54 range must log S046's permitted `used-by` update and remain clean. | `breach 5a097e12b S046 used-by: …`; 1 breach in 1 of 1 commits; exit 1. | KILLED |
| 10 | Line 74: invert equality to inequality in the unchanged-cell skip. | `--self-test` unchanged and changed-cell arms must match their expected counts. | 14 failures over 14 assertions, including 14 breaches on the unchanged arm; exit 1. | KILLED |

The synthetic merge fixture was created only inside the scratch clone. Its base was `bb652e9731a275f2b81f97cdad73c2daa7934cbf`; its merge was `0a14219696b07ad05e196cc6528b873708a9e899`. Both parent commits changed only permitted cells; the merge resolution introduced the protected `anchor` edit.

## Restoration

After all probes, the verifier's SHA-256 was again `d4d1d62b16ededc8f31e5df71738285bd88768a2b3e3b9824b2782143fef3805`, matching the pristine hash; `test "$(sha256sum … | cut -d ' ' -f 1)" = d4d1d62b16ededc8f31e5df71738285bd88768a2b3e3b9824b2782143fef3805` exited 0. On restored bytes, the self-test again passed 14/14 (exit 0), red range again reported one S050 breach (exit 1), green range was clean (exit 0), round-54 range logged only the S046 `used-by` note and was clean (exit 0), and the pristine synthetic merge fixture was clean (2 commits scanned, exit 0).
