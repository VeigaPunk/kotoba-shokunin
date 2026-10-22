# ProbeReportBaseline: report-baseline vs prompt rounds (round 49 falsify)

Verdict: HOLDS-BOUNDED. It applies to the 17 fleet lanes that have `.ufo/state/<id>.report-baseline`. For each, the first field equals the highest top-level `.ufo/prompts/<id>-round-<N>.md`, and no prompt round exceeds its baseline. Live `dispatch.08` exits 0 with status PASS. The claim does not cover the 6 lanes with prompts but no baseline (29 files, all N/A), nor `.ufo/prompts/closure/`.

## Scope and bounds
- Read-only probe of fleet `/home/vgpnk/Projects/shokunin/.ufo/state` and `.ufo/prompts`. Not attacked here: C1, C2, R1, records (other seats).
- Report location: the fleet root has no `.ufo/waves/round-49` (`ls -d` exit=2). The report sits in the lane at `.ufo/waves/round-49/falsify/ProbeReportBaseline.md` per the Report-trailer rule. This is the only file written in the lane.
- Scratch: `/fast/scratch/hyaku/kotoba-r49/falsify/ProbeReportBaseline/` (clone at c48793dbe5eb30cd661f42ecad7399ae94e3d7ad; `control/` holds the positive control).
- Tools: none installed or updated. Used python3 stdlib, git and coreutils, all already present.

## Per-lane table (17 baseline lanes)
first = first field of `<id>.report-baseline`. highest = max N of top-level `<id>-round-<N>.md`. files = round-named top-level prompts. dispatch.08 = verifier per-lane PASS/FAIL/N/A. above = prompt rounds greater than first.

| lane | first | highest | equal | files | dispatch.08 P/F/N | above |
|---|---|---|---|---|---|---|
| chousa | 28 | 28 | yes | 6 | 6/0/0 | none |
| kagi | 28 | 28 | yes | 23 | 23/0/0 | none |
| kaidoku | 25 | 25 | yes | 14 | 14/0/0 | none |
| kake | 29 | 29 | yes | 25 | 25/0/0 | none |
| kama | 25 | 25 | yes | 18 | 18/0/0 | none |
| kasegi | 23 | 23 | yes | 17 | 17/0/0 | none |
| kengaku | 29 | 29 | yes | 18 | 18/0/0 | none |
| kotoba | 49 | 49 | yes | 18 | 18/0/0 | none |
| kotodama | 52 | 52 | yes | 4 | 4/0/0 | none |
| kumitate | 39 | 39 | yes | 21 | 21/0/0 | none |
| mado | 23 | 23 | yes | 13 | 13/0/0 | none |
| mori | 25 | 25 | yes | 16 | 16/0/0 | none |
| revenger | 62 | 62 | yes | 3 | 3/0/0 | none |
| souji | 22 | 22 | yes | 11 | 11/0/0 | none |
| tabi | 22 | 22 | yes | 12 | 12/0/0 | none |
| tameshi | 26 | 26 | yes | 16 | 16/0/0 | none |
| tsukuroi | 25 | 25 | yes | 15 | 15/0/0 | none |

Totals: equal yes 17, equal no 0. Lanes with a prompt above baseline: 0. dispatch.08 file verdicts: 250 PASS, 0 FAIL.

Lanes with prompts but no baseline (outside the claim):

| lane | max N | files | legacy `.round` | dispatch.08 P/F/N |
|---|---|---|---|---|
| aggregator | 12 | 9 | 10 | 0/0/9 |
| audio | 101 | 2 | 1 | 0/0/2 |
| game-dev-2d | 105 | 2 | 1 | 0/0/2 |
| game-dev-3d | 108 | 2 | 1 | 0/0/2 |
| lore | 103 | 2 | 1 | 0/0/2 |
| protocol | 15 | 12 | 14 | 0/0/12 |

## Findings (by severity)

F1 Medium. The dispatch.08 check status reads PASS while 29 of 279 evaluated files are N/A. The verifier marks the six baseline-less lanes N/A ("state-stale: only X.round present ... not compared"). The check status is PASS because the verifier docstring (lines 41-44) gives PASS whenever some file passes. Aggregator (12 vs legacy 10) and protocol (15 vs 14) already exceed their frozen `.round` values. Audio, game-dev-2d, game-dev-3d and lore exceed `.round`=1 by 102 to 107. The baseline rule cannot FAIL them, so the gate cannot catch them. Owner decision: give these lanes a baseline or retire their prompts, and consider surfacing N/A in the check status.

F2 Low. The verifier docstring (lines 13-14) says `closure/` "is out of scope and is reported". The output does not report it. `out_of_scope` has 13 entries (`.gitkeep`, eight `<lane>-L1.md`, four `*-round-1-continuation-kaika.md`) and none names closure.

F3 Low-medium. Name collision in `closure/`. It holds 89 files named `<lane>-round-<N>.md` for the 16 baseline lanes. Each shares its name with a top-level file. None is byte-identical: all 89 top-level copies are larger, the diffs run 281 to 482 changed lines, and the first lines differ. The closure copy is the integrator-of-record prompt ("You are the hyaku non-author integrator ... chousa round 27"). The top-level file is the L1 dispatch prompt. Name-keyed tooling that recurses gets the wrong role. The claim holds: every closure round is at or below its lane's top-level maximum and baseline (16 of 16 checked).

F4 Low. Legacy `.round` disagrees with the baseline for all 15 baseline lanes that have one (for example kagi 16 vs 28, kotoba 16 vs 49, revenger 1 vs 62). dispatch.08 correctly ignores it (verifier lines 181-202). Any consumer that reads `.round` gets values frozen since 2026-10-15.

F5 Bound. Equality is true by construction on the normal path. `scripts/hyaku/inline.sh` lines 99-100 write the prompt and the baseline with the same N. The watchdog records the baseline at launch (`scripts/shokunin-watchdog.sh` line 203). So the equality probe is not an independent check. The real gate is dispatch.08's per-file N <= baseline, which would not catch a baseline running ahead of its prompts. None exists today.

F6 Info. Every baseline's second field is e3b0c442...b855, the SHA-256 of empty input (all 17). This matches design: `report_digest` hashes a missing report as the empty stream (`scripts/shokunin-watchdog.sh` lines 108-116), and baselines are recorded before launch, when no report exists. The field records "no report at capture", not the current report.

F7 Info. Counting. `ls` shows 292 prompt entries; `ls -A` shows 293 (hidden `.gitkeep`). A naive `<lane>-round-*.md` glob also matches the four `*-round-1-continuation-kaika.md` files. A digits-only guard excludes them, and none changes a maximum.

Positive control. dispatch.08 does FAIL when a round exceeds baseline. A scratch copy of the fixture (`kote-round-9.md`, baseline 6) gives `round 9 > latest dispatched 6 (kote.report-baseline = 6)` with exit 1. The gate works for exceedance and is blind to F1.

## Evidence (commands and exit codes)
1. Python probe (eval cell, stdlib glob/os/re). 17 baseline files, each 68 bytes, one line, two tokens, no CRLF or BOM. Equal yes 17, no 0. Regex max vs glob max mismatches 0. Top-level 293 entries = 279 round-named + 13 other + 1 directory. Cell completed without error.
2. `bash -c 'set -o pipefail; ls .ufo/prompts | wc -l'` gives 292, exit=0. `ls -A .ufo/prompts | wc -l` gives 293, exit=0. `ls .ufo/state/*.report-baseline | wc -l` gives 17, exit=0. `ls .ufo/state | wc -l` gives 80, exit=0. `find .ufo/prompts/closure -type f | wc -l` gives 89, exit=0.
3. `find .ufo/prompts -mindepth 1 -maxdepth 1 -name '.*'` gives `.gitkeep`, exit=0.
4. `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>`, then `git -C <scratch> checkout -q c48793db...`. `rev-parse HEAD` gives c48793dbe5eb30cd661f42ecad7399ae94e3d7ad, exit=0.
5. `python3 -B verifiers/verify_dispatch_prompts.py --check dispatch.08 --json`, run in the scratch clone with default fleet paths. Exit code 0. Check status PASS. Detail: "279 file(s) evaluated: 250 PASS, 0 FAIL, 29 N/A; 13 out of scope". Conjuncts: filename_role_round_equal 279 PASS; filename_report_dir_round_equal 279 PASS; round_le_latest_dispatched 250 PASS, 29 N/A, 0 FAIL.
6. Cross-check: the verifier's per-lane maximum equals the probe's highest N for all 17 lanes. Its detail strings name the same baseline values. 0 mismatches.
7. Positive control: `python3 -B verifiers/verify_dispatch_prompts.py --check dispatch.08 --prompts <control>/prompts --state-dir <control>/state --fleet <control>/fleet --json`. Exit code 1. FAIL on `kote-round-9.md`.
8. Closure comparison (eval cell): 89 closure names also exist top-level. Byte-identical 0. Closure rounds above baseline: none. Closure lanes without baseline: none.
9. `ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/round-49` gives "No such file or directory", exit=2.
10. Reads: verifier lines 1-70, `state_source` (178-202), `evaluate_dispatch_08` (379-442); `scripts/shokunin-watchdog.sh` lines 108-138 and 203; `scripts/hyaku/inline.sh` lines 99-100.

Not run: the C1 guard, the C2 `--box-proof` run and R1 tests. Their results are not claimed here.
