# Round 51 falsify: NoHarmGates

**Verdict: HOLDS-BOUNDED.** Gates green at base and red at HEAD (HARM): **none**. All 11 base-green gates are green at HEAD `59903b2637689739a5b9901956301da72d0effe1`. The result covers the 19 gate commands in rows 1-19 (row 20 is one extra run), run on this host at 2026-10-22T15:19Z, one run per side. Bounds: rows 13 and 15 are green only for the installed omp 18.12.6 binary; rows 3, 4, 14 and 16 stay red at HEAD (they were red at base too); the overlap-levers base value is a HEAD-counter reading of the base revision, not a base counter.

Confidence: high on the exit codes and summary lines (every base row re-measured identically; the HEAD rows were measured once). Medium on "no harm" beyond these 19 commands: no gate outside the list was run.

What this item attacks: regressions of the base-green gates; floors lowered to pass; greens that come from an empty or vacuous check.

## Setup

- HEAD clone `fleet/kotoba-shokunin` at 59903b26 (`rev-parse HEAD` confirmed). BASE clone at 43ca0bfb (confirmed). Scratch root: `/fast/scratch/hyaku/kotoba-r51/falsify/NoHarmGates/`.
- Fleet shape as in BaseReplay.md: `.ufo` (68M) and `PROTOCOL.md` copied; the other 49 root entries are symlinks to `/home/vgpnk/Projects/shokunin/`, sibling lanes included.
- Runner `run_side.sh`: the 17 BaseReplay commands plus `check_overlap_levers.py` and its `--self-test`, and one HEAD-only run with `--rev 43ca0bf`. Both sides ran at the same time (both finished at 15:19:30Z and 15:19:31Z, 98 s wall each). Logs: `{base,head}/logs/gNN.log`.
- The BASE column was re-run on the same host in the same minute. It matches BaseReplay.md on all 17 rows (exit code and summary), so no host drift since 14:25Z moved any base row.

## Table

rc = exit code. "Re-run" = my base run at 15:19Z.

| # | Gate (run from clone root) | BASE rc / summary (BaseReplay.md; re-run identical) | HEAD rc / summary | No-harm verdict |
|---|---|---|---|---|
| 1 | `verify_skill_checklist.py --json` | 0 · pass 11 fail 0 na 0 | 0 · pass 11 fail 0 na 0 | green to green |
| 2 | `verify_skill_checklist.py --self-test` | 0 · 0 failures over 1851 assertions | 0 · 0 failures over 1851 assertions | green to green |
| 3 | `verify_corpus_integrity.py --json` | 1 · 4 DRIFT: tracked 70 vs 69, unindexed 1, report_total 45 vs 44, report_dead 2 | 1 · 1 DRIFT: report_dead 2. Tracked 72 and report_total 46 now PASS | red to red, narrowed; not harm |
| 4 | `verify_corpus_independent.py` | 1 · DRIFT unindexed=1, DRIFT report_dead=2 | 1 · DRIFT report_dead=2; unindexed 0 PASS | red to red, narrowed; not harm |
| 5 | `check_assertion_floors.py` | 0 · 11 PASS, each observed = floor | 0 · 12 PASS, each observed = floor (surfaces 115, overlap_levers 22) | green to green |
| 6 | `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | 0 · rows 20 verified 20; province rows 20 matched 20 | 0 · same | green to green |
| 7 | same, plus `--skill SKILL.md` | 0 · names 9 of 9; length 1019 of 1024 | 0 · same | green to green |
| 8 | `check_sibling_census.py --self-test` | 0 · 0 failures over 68 assertions | 0 · same | green to green |
| 9 | `verify_dispatch_prompts.py --self-test` | 0 · 0 failures over 56 assertions | 0 · same | green to green |
| 10 | `verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 · boxes proven 2 | 0 · same | green to green |
| 11 | `verify_harness_independent.py --self-test` | 0 · 0 failures over 123 assertions | 0 · same | green to green |
| 12 | `compare_harness_independent.py --self-test` | 0 · 0 failures over 330 assertions | 0 · same | green to green |
| 13 | `verify_surfaces.py --json` (C1 freshness) | 1 · pass 5 fail 2 | 0 · pass 7 fail 0 | red to green (improved) |
| 14 | `verify_harness_claims.py` | 1 · 21/28 pass; 7 DRIFT lines | 1 · 21/28 pass; the same 7 DRIFT lines | red to red, unchanged; not harm |
| 15 | `check_substrate_pins.py` | 1 · DRIFT 2/3 pins failed | 0 · OK 3/3 pins hold | red to green (improved; bound to this binary) |
| 16 | `fault_injection_corpus.sh` | 1 · 4 red rows: fault-0-control, fault-f, fault-g, fault-h; 6 must-fire rows PASS | 1 · same 4 red rows, same 6 PASS rows; causes narrowed to report_dead | red to red; not harm |
| 17 | `box_proof_case_deletion.py --rev <rev>` | 0 · killed 6 of 6; controls 2 of 2; na 1 of 1 | 0 · same | green to green |
| 18 | `check_overlap_levers.py` (new, C2) | absent at 43ca0bf: rc 2, "can't open file" | 0 · overlap levers backed 7 of 7 clients | new gate; not harm |
| 19 | `check_overlap_levers.py --self-test` | absent at 43ca0bf: rc 2 | 0 · 0 failures over 22 assertions | new gate; not harm |
| 20 | extra: `check_overlap_levers.py --rev 43ca0bf` (HEAD counter, base bytes) | not a base gate | 1 · overlap levers backed 0 of 7 clients; all seven "SKILL.md table absent" | base value for C2 |

Tally: 11 gates green at base, all 11 green at HEAD. 6 gates red at base: 2 turned green (13, 15), 4 stayed red (3, 4, 14, 16). 2 gates are new (18, 19) and absent at base.

Claims checked against the run: row 13 pass 5 to 7 of 7 (matches the C1 claim); row 15 DRIFT 2/3 to OK 3/3 (matches); integrity 5/9 to 8/9 (matches: 4 DRIFT at base, 1 at HEAD); overlap levers 0 of 7 to 7 of 7 (matches, with the bound in finding 8).

## Findings

1. **HARM: none.** No base-green gate is red at HEAD. Rows 13 and 15 went red to green; rows 3, 4, 14, 16 are red on both sides.
2. **Rows 14 and 16 are not named in the round's own record.** A strict grep of `corpus/lessons/round-51.md` and `plans/round-51.md` for `fault[-_ ]`, `fault inj`, `21/28` and `verify_harness_claims` returns no matches. Both rows are red at base too, so this is a bookkeeping gap, not harm. Route to the L1 as carried items: row 14 is host-state drift in the omp key set (reads `~/.omp`); row 16 has four red rows, and fault-h keeps the absolute expectation noted in BaseReplay F3, which HEAD does not change (`verifiers/fault_injection_corpus.sh` is absent from the base-to-HEAD diffstat).
3. **Rows 3 and 4 keep one red check: report_dead = 2.** The commit message of 59903b26 names it ("closure-owned round-48 spot-check"). This matches BaseReplay F1. The "5/9 to 8/9" count in that message is right.
4. **Row 13 is not vacuous.** The HEAD log shows `surfaces.no_uncovered_class` PASS ("all 8 extracted loader class(es) declared") and `surfaces.literal_present` PASS ("42 loader-kind entries verified against the dumps"). Base failed with "0 loader class(es) extracted". The green is earned, not an empty pass.
5. **Row 15 is green only for the installed binary.** `verifiers/baseline.json` now pins omp sha256 `85d9daf3…` and mtime `2026-10-21T20:37:24.615549837-03:00`; the HEAD log shows `delta 0 ns`. A later omp update turns this red again, by design. The re-pin is backed by a new fixture, `verifiers/fixtures/surfaces/strings-omp-18.12.6.txt` (36 lines added in the diffstat).
6. **No floor was lowered.** `git diff 43ca0bf 59903b26 -- verifiers/check_assertion_floors.py verifiers/floors-registry.json` shows surfaces 99 to 115 (raised), overlap_levers 22 added, instrument total 11 to 12. Every floor at HEAD has observed = floor (row 5).
7. **Corpus baseline re-record is neutral.** `verifiers/corpus-baseline.json` expect values moved 69 to 72 (tracked files) and 44 to 46 (report pointers). The HEAD counts equal those values. The commit message names the three files behind the +3 tracked files: the round-50 closure file, the round-51 entry and the round-51 lesson. Noted only because a re-record moves the anchor.
8. **C2 base value is structural (calibration).** `check_overlap_levers.py` does not exist at 43ca0bf. The plan's "0 of 7 at base" comes only from the HEAD counter run with `--rev 43ca0bf` (row 20). Every client reads "SKILL.md table absent", so the 0-to-7 step shows that the table and its rows exist. It does not show that depth was measured. The seven BACKED results rest on the frozen `REVIEWED_LEVERS` list (`verifiers/check_overlap_levers.py` lines 137-141, which say the judgment "is not a measurement"). This is for the C2 attack seat.
9. **Several gates read live host paths.** Rows 6-8 read sibling git history; rows 13-15 read the omp binary and `~/.omp`; `verify_dispatch_prompts.py` defaults to `/home/vgpnk/Projects/shokunin/.ufo/prompts` (lines 98-99); `fault_injection_corpus.sh` plant_f reads `/home/vgpnk/Projects/shokunin/.ufo/reports/round-4/kotoba.md` (lines 227-228). Both sides ran in the same window, so the comparison is fair. A later run can move these rows.
10. **Fleet shape is clean.** Sibling symlinks are present, and row 1 is green on both sides. The scratch-shape artifact in BaseReplay F5 did not recur.

## Residual risk and verification gaps

- One host, one run per side. Flakiness is not measured.
- Not run: `check_overlap_levers.py --fetch`. It needs the network, and the assignment did not ask for it. The L1's "--fetch 7 of 7 at 15:10:48Z" is not re-measured here.
- Not run: anything in the lane checkout (bounds). The lane's untracked `.ufo/waves/round-51/` is not in the clone. No verifier reads `.ufo/waves` at runtime; the only mentions are comments and docstrings in `verifiers/check_sibling_census.py` (lines 410, 509-510).
- Not covered here: mutation checks of C1 and C2, the routed-defect repairs and the resume items. Other falsify seats own those.

## Evidence (commands and exit codes)

- `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>/head/fleet/kotoba-shokunin` rc 0; `git -C <clone> checkout -q 59903b26…` rc 0; `rev-parse HEAD` = `59903b2637689739a5b9901956301da72d0effe1`. Base: same steps with `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`, rc 0, rev-parse matched.
- `bash run_side.sh base 43ca0bfb…` → g01 0, g02 0, g03 1, g04 1, g05 0, g06 0, g07 0, g08 0, g09 0, g10 0, g11 0, g12 0, g13 1, g14 1, g15 1, g16 1, g17 0, g18 2, g19 2. Last line: `base DONE 2026-10-22T15:19:30Z`.
- `bash run_side.sh head 59903b26…` → g01 0, g02 0, g03 1, g04 1, g05 0, g06 0, g07 0, g08 0, g09 0, g10 0, g11 0, g12 0, g13 0, g14 1, g15 0, g16 1, g17 0, g18 0, g19 0, g20 1. Last line: `head DONE 2026-10-22T15:19:31Z`.
- Per-check detail: JSON parse of the g01, g03 and g13 logs; text reads of the g04, g05, g14, g15 and g16 logs (eval kernel).
- `git diff 43ca0bf 59903b26 -- verifiers/check_assertion_floors.py verifiers/floors-registry.json verifiers/corpus-baseline.json verifiers/baseline.json` (in the head clone) rc 0.
- `sha256sum /home/vgpnk/.local/bin/omp` rc 0 → `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`, at 15:17Z.
- Tools: none installed or upgraded. Present: Python 3.14.8, git 2.56.0. `git cat-file -t` in the head clone reports `commit` for 7c81a7878992..., e03203021d0d... and 34cfffbb242f.... `git rev-parse origin/master` in the head clone (the lane master at clone time) = 59903b26.
