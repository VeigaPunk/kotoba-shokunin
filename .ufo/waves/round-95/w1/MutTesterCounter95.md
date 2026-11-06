# MutTesterCounter95 — mutate the v3 counter itself (scratch copy only)

Seat: MutTesterCounter95 (mutation-tester, r95-w1, leaf — no subagents). Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin (read-only for this seat except this report and .ufo/waves/round-95/w1/MutTesterCounter95/). Scratch: /fast/scratch/hyaku/kotoba-r95/MutTesterCounter95 (TMPDIR+HYAKU_SCRATCH; removed before yield).

## Assignment

Design >=6 mutants of the v3 counter `verifiers/fixtures/round-95/selftest-kills.py` (scratch copy only; lane file byte-frozen), run each against the base 673d1e2e6f850bb54dda9698cf825cf6788c7d0d, the r94c1 positive control and the six forgery worlds (built with the frozen `build-forgeries.py` into scratch), and say which committed control receipt or world exposes each. A counter mutant no control world exposes is a gap in the control battery — report it with the minimal new control world that would.

## Setup evidence (so far)

- `sha256 counter-pristine.py == lane selftest-kills.py == d6ae74af40135f9b30b0101d5a195a3d950b6a72073020ac59ba58da1d269001` (the plan's frozen sha).
- Scratch clone `$S/repo` at 673d1e2e6f850bb54dda9698cf825cf6788c7d0d; `git rev-parse --show-toplevel` == `$S/repo`.
- Committed receipts to compare against: `.ufo/waves/round-95/receipts/{redbefore-c1-base,poscontrol-r94c1-base,forgery-f1..f6-*.txt}`.
- Comparability note: pre-data receipts were taken at round base 2d886a91e57efd3555ec9076a63209e2d8bfbb8d; my contexts run at the freeze commit. Driver asserts `git diff 2d886a91 673d1e2e -- verifiers/check_mutation_battery.py` is empty so the instrument bytes (and therefore every run line) are comparable; receipt header lines (rev/repo) differ by construction.

## Counter mutants under test (all 1:1 line-count replacements in the scratch copy)

| id | mutation (anchor -> replacement) | predicted exposure from committed controls |
|---|---|---|
| M1-classify-rc-only | `if rc == 1 and n >= 1 and fails >= 1:` -> `if rc != 0:` (REPORTED-FAILURE on any rc != 0) | f6: n11 crash run (rc 1, no summary) reclassified RUN-ERROR -> KILLED; reading `run errors 1, killed 0 of 3` becomes `run errors 0, killed 1 of 3`. Verdict stays UNMET; receipt-line deviation. |
| M2-classify-drop-fail-line | same anchor -> `if rc == 1 and n >= 1:` (FAIL-line conjunct dropped) | none committed: f6 has no summary (still RUN-ERROR); every other failing run has `FAIL ` lines. GAP — demo world f7-summary-no-fail-line. |
| M3-code-decoys-skipped | `held_code += cls == "CLEAN"` -> `held_code += 1` | f1/f2/f3: code decoys held 0/3 -> faked 3/3. Verdict UNMET both ways (killed 0 of 3 blocks met); tally deviation only. |
| M4-comment-decoys-skipped | `held_comment += cls == "CLEAN"` -> `held_comment += 1` | f1: comment decoys held 0/3 -> faked 3/3. Tally deviation only. |
| M5-runner-writes-mutant-to-disk | `path.write_text(on_disk, ...)` -> `path.write_text(text, ...)` in `run_text` (source-blind rule 3 broken) | f5 should flip to FALSE MET: sniffer sees mutant tokens in mutant runs -> killed 3 of 3, decoys held 3 of 3, honest CLEAN -> `C1-PREDICATE-MET` on a forgery world. f1/f2/f3/f4: heavy tally deviations. |
| M6-honest-clean-conjunct-dropped | predicate drops `cls_h == "CLEAN" and` | none committed: every committed world has honest CLEAN. GAP — demo world f9-honest-trip should flip to FALSE MET. |
| M7-decoy-held-rc0-no-summary | both decoy tallies -> `cls == "CLEAN" or rc == 0` | none committed: all committed decoy runs are CLEAN-with-summary or REPORTED-FAILURE. GAP — demo world f10-decoy-silent-zero (decoy runs exit 0 with no summary) should expose at tally level. |
| M8-positive-forced-killed | `pos = 1 if cls == "REPORTED-FAILURE" else 0` -> `pos = 1` | none committed (positive killed 1 of 1 in every committed receipt). GAP — minimal world is the future C1 candidate minus its positive arm; also exposes naturally at candidate measurement. |

## Demo worlds (built in scratch, identity MutTesterCounter95, never the lane)

- f7-summary-no-fail-line: f6-shaped two-row pin probe, but signals by printing `1 failure(s) over 1 assertions` + exit 1 with NO `FAIL ` line. Pristine counter: RUN-ERROR (run errors 1), UNMET. M2: KILLED (killed 1 of 3, run errors 0) — exposes M2 at tally level; verdict flip needs a world that kills all three targets that way (design in findings).
- f9-honest-trip: instrument reports a failure whenever its own source lacks decoy markers (`# r95-decoy` comment or `__decoy__` guard, literals split to stay marker-free). Honest run REPORTED-FAILURE -> pristine counter UNMET; M6 (honest conjunct dropped) reads MET — FALSE MET verdict flip.
- f10-decoy-silent-zero: instrument `os._exit(0)`s when decoy markers are present; decoy runs exit 0 without the summary -> pristine counter: decoys held 0 of 3; M7 fakes 3 of 3. Verdict UNMET both ways (killed 0 of 3); tally-level exposure.

## Status

Matrix launched: 9 counter variants (pristine + M1..M8) x 8 committed contexts (base-c1, pos-r94c1, f1..f6) + demo contexts f7/f9/f10 under pristine and their targeted mutant. Results and verdicts appended below when the job lands. Receipts will be copied to `.ufo/waves/round-95/w1/MutTesterCounter95/receipts/`.
