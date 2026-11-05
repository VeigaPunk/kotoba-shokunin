# MutTesterBattery — round-92 C2 candidate: mutation attack

Seat: MutTesterBattery (leaf; no dispatch). Receipts: `.ufo/waves/round-92/w1/MutTesterBattery/`.

## Candidate

- Freeze base `e073723ae667b64e534f8621bddb83ad12ad0e71` + `ExecKillPin.patch` + `ExecLadderR92.patch`
  (both applied cleanly with `git apply`; file sets disjoint: check_mutation_battery.py vs
  check_freeze_gate.py, check_assertion_floors.py, check_tip_battery.py, floors-registry.json).
- Scratch candidate commit `178a4675556f500ef6488d27a575ef647896ac6f` (scratch identity, scratch clone only).
- READY files: `KILLPIN-READY N=28`, `LADDER-READY N'=34`.

## Honest baseline on the candidate (equivalence arms)

| check | observed | verdict |
|---|---|---|
| battery `--self-test` | `0 failure(s) over 28 assertions`, rc 0 | held (N ≥ 26) |
| freeze-gate `--self-test` | `0 failure(s) over 34 assertions`, rc 0 | held (N' ≥ 34) |
| floors `--self-test` | `0 failure(s) over 176 assertions`, rc 0 | held; registry drift `[]`, anchor drift `[]` |
| freeze-gate `fp-minimal.md` | `freeze gate: 1 control(s) held — freeze may proceed`, rc 0 | held |
| freeze-gate `r88-controls.md` | `REFUSED control w_added_red ...`, rc 1 | **identical to base** (see F-3) |
| freeze-gate `r88-controls-fixed.md` | `freeze gate: 4 control(s) held`, rc 0 (base and candidate) | held |
| tip battery `--rev 178a467` | `guard instrument-pin PASS`; `guards 5 of 5`; rc 1 from the three carried corpus gates (verify_skill_checklist, verify_corpus_integrity, verify_corpus_independent) | as the plan predicts |
| battery `--rev` base `e073723` | `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, rc 0 | base green |
| battery `--rev` candidate `178a467` | `could-not-evaluate: anchor miss: fg-x1-parse-drop-exit-clause edit 1 matches 0 time(s) in the revision bytes`, rc 2 | **BLOCKER** (F-1) |

## Mutants (each on a fresh clone of the candidate; diffs in `mutant-*.diff`)

| id | mutation | expected | observed (rc, line) | verdict |
|---|---|---|---|---|
| m1 | delete manifest row `fg-m1-expect-exit-sign-flip` (kill row, line 2) | battery self-test FAIL naming kill-set-size | rc 1: `FAIL arm kill-set-size: the live manifest's kill-row count equals the pin :: observed 16 kill rows, pinned 17`; `1 failure(s) over 28 assertions` | **killed** |
| m1-c | same, committed (`d8320137`), then `battery --rev` | — | rc 2: `could-not-evaluate: baseline bat-self-test exit 1, declared 0` | refused (not silent) |
| m2a | `KILL_SET_PINNED = 18` (+1) | FAIL on honest bytes (false red) | rc 1: `FAIL arm kill-set-size ... observed 17 kill rows, pinned 18`; `1 failure(s) over 28` | **killed** |
| m2b | `KILL_SET_PINNED = 16` (−1) | FAIL | rc 1: `FAIL arm kill-set-size ... observed 17 kill rows, pinned 16`; `FAIL arm ... dropped is refused by the pin :: observed 16 kill rows, pinned 16`; `2 failure(s) over 28` | **killed** |
| m3 | remove duplicate-name rejection (3 lines, `if name in seen:`) | freeze-gate self-test FAIL; rp-duplicate-names world reads held | self-test rc 1: `FAIL arm parse-duplicate control name ... `, `1 failure(s) over 34`; `fp-duplicate-names.md` rc 0: `freeze gate: 2 control(s) held — freeze may proceed` | **killed** (both channels; defect reappears in the world) |
| m4 | `if rc in (126, 127):` → `if False:` | self-test FAIL; rp-exit127 world reads could-not-evaluate rc 2 | self-test rc 1: `FAIL arm unobservable-rung declared exit 126/127 ...`, `1 failure(s) over 34`; `fp-exit127.md` rc 2: `COULD-NOT-EVALUATE control one27 (line 6): command not found (rc=127)` | **killed** (defect reappears in the world) |
| m5 | remove the 4-line `_work_root_problem` translation in `run_gate` | self-test FAIL; rp-work world crashes | self-test rc 1: `FAIL arm work-root ... unexpected NotADirectoryError(20, 'Not a directory')`, `1 failure(s) over 34`; `--work <file>/sub` rc 1 traceback `NotADirectoryError`; `--work <file>` rc 1 traceback (`NotADirectoryError` from mkdtemp, not the base `FileExistsError`) | **killed** |
| m6 | `floors-registry.json` freeze_gate floor `34` → `31` (in-file tables and self-test still 34) | plan: floors `--self-test` FAIL (drift arm) | `--self-test`: rc 0, `0 failure(s) over 176 assertions` — **SURVIVED the self-test**. Guard run (no `--self-test`): rc 2, `FAIL registry floor drift: freeze_gate registry=31 expected=34 row=34`, returns before any child self-test | **killed by the guard run; survived the self-test** (F-2) |
| m7a | delete the whole `check_freeze_gate.py` key (7 lines, comment included) from `INSTRUMENT_PINS` | tip `guard instrument-pin` FAIL | `guard instrument-pin PASS`; `guards 5 of 5` | **SURVIVED** (F-4) |
| m7b | drop the floors postimage blob `4ed35c4…` from the `check_assertion_floors.py` tuple | instrument-pin FAIL | `FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob 4ed35c4… at 178a467 is not a pinned blob`; `guards 4 of 5` | **killed** |
| m7c | drop the `check_freeze_gate.py` postimage blob `856f543…` (key kept, base blob only) | instrument-pin FAIL | `FAIL guard instrument-pin: verifiers/check_freeze_gate.py blob 856f543… at 178a467 is not a pinned blob`; `guards 4 of 5` | **killed** |

Equivalents (must survive): honest self-tests, fp-minimal, r88-controls fixture — all unchanged from base or green on the candidate. **Survived as required.**

Score: 9 of 10 mutants killed by a named channel; 1 survived (m7a). Equivalents: 3 of 3 held.

## Findings

**F-1 (BLOCKER for C1 honest control and the rev-scoped battery). Stale fg-x1 anchor.**
ExecLadderR92 rewrote the `parse_expect` line `control.expect_rc = int(m.group(1))` into `rc = int(m.group(1)) ... control.expect_rc = rc`. The frozen kill row `fg-x1-parse-drop-exit-clause` (manifest line 9) still anchors on the old text, so the candidate's `battery --rev` aborts at rc 2 (`anchor miss ... matches 0 time(s)`). The plan's `ctl-c1-honest.sh` expects `killed 17 of 17 kill-set`, exit 0 — it cannot hold on the candidate as built.
Diagnostic only (scratch clone `m8`, commit `d82fe5a6`): re-pointing the fg-x1 anchor to `control.expect_rc = rc\n            continue` makes `battery --rev` read `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, rc 0. So the anchor is the only blocker on the rev path. The manifest is not owned by either builder; any repair is an L1 act through an addendum before scored reading. Not applied in the lane.

**F-2 (plan expectation misplaced). The floors registry drift arm is not in `--self-test`.**
`check_assertion_floors.py` routes `--self-test` straight to `self_test()` (line 582) before `registry_drift()`/`registry_anchor_drift()` run in `main()` (lines 604–610). So a registry floor left at 31 is invisible to `--self-test` (m6: rc 0, 176 assertions) and visible only to the guard run (rc 2, `FAIL registry floor drift`). The plan's "floors self-test FAIL (drift arm fires)" is wrong about where the arm fires; the registry arm is correct in `main()`. Recommend the plan/controls text name the guard run, or L1 decides an addendum; no predicate was changed here.

**F-3 (plan wording). `r88-controls.md` is a refusal fixture.**
The plan says the fixture "still exits 0". The fixture's own header says it must REFUSE (exit 1, naming `w_added_red`). Base and candidate give the identical refusal line (rc 1). The honest counterpart `r88-controls-fixed.md` exits 0 on both trees. The equivalence holds; the plan sentence is inaccurate.

**F-4 (coverage gap). Deleting the pin key is silent.**
The tip-battery pin guard iterates `INSTRUMENT_PINS.items()` only (check_tip_battery.py:328); `check_freeze_gate.py` is not in `BATTERY`, so `instrument-size` does not cover it either. Removing the whole key (m7a) leaves `guard instrument-pin PASS`, `guards 5 of 5`. The plan's m7 expectation ("append omitted → FAIL") holds for a tuple omission (m7c) but not for key removal. A coverage finding for the lesson; not a candidate regression.

**F-5 (minor). The kill-set-size arm reads the working-tree manifest.**
`self_test()` reads `Path(__file__).parent.parent / MANIFEST` (the live working tree), not the measured revision's committed manifest that the plan describes. The rev path is refused rather than silent (m1-c: rc 2, baseline self-test exit 1), but a rev-only kill-row drop is caught by refusal, not by the named arm.

**F-6 (minor). rp probes pin the old base.**
`verifiers/fixtures/round-92-predata/rp-m6-dropped-row.sh` sets `BASE=5031a78…` and checks that out in its clone, not the freeze commit `e073723…`. It therefore tests 5031a78 bytes, not the candidate; the m1 mutant above was run on the candidate directly.

## Restoration and hygiene

- No lane file written. Every mutation ran in a scratch clone under `/fast/scratch/hyaku/kotoba-r92/MutTesterBattery/` (deleted at yield).
- No install, no host or kernel change, no sysctl, no pacman.
- Processes: sequential runs only; no processes left running.
