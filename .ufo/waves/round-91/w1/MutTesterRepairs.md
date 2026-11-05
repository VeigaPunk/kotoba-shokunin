# MutTesterRepairs — round 91 attack on C2 (floors cap + pin, freeze-gate ladder)

Seat: MutTesterRepairs (attack, mutation-tester). Read-only w.r.t. the lane and every builder patch.

## Candidate

- Base: `9af1a7af2adf0ab07cfd53f92affc1ed8d992262` (freeze commit).
- Applied in scratch clone, in order: `ExecFloorsCap/ExecFloorsCap.patch`, then `ExecLadder/ExecLadder.patch`
  (both `git apply --check` clean before apply).
- Candidate commit (scratch identity, scratch clone only): `49e6817014da3b48cb2fca36343236081f8449bc`.
- Gates: ExecFloorsCap_READY (blob `0b29bcd0…`, selftest_N=176, rc 0); ExecLadder_READY
  `verdict=REPAIRABLE rc=0` — so m7 applies.
- Candidate pristine probes (rev `49e6817`): floors `--self-test` rc 0, `0 failure(s) over 176 assertions` (5.8 s);
  instrument-pin guard rc 0, `guard-failures 0`; freeze-gate `--self-test` rc 0, `0 failure(s) over 31 assertions`.

## Detectors (same bounded probes on pristine and every mutant, 120 s cap each)

- `floors`: `python3 -B verifiers/check_assertion_floors.py --self-test`
- `tip`: `check_tip_battery.run_guards(repo, base, rev)` called in-process (instrument-pin and the other battery guards).
  The full `check_tip_battery.py --rev` did not finish within 120 s even on pristine (rc 124 at 120 s); that is recorded
  as finding F4 and is why the guard function is probed directly.
- `gate`: `python3 -B verifiers/check_freeze_gate.py --self-test`
- Where a mutant reds only through the guard's `main` pre-check, the bare walk `check_assertion_floors.py --repo <mut>`
  was run (it exits before the child self-tests; rc 2 within about 1 s).

## Mutants (fresh clone per mutant, one exact-match edit asserted to occur once, scratch commit)

| id | mutant | floors self-test | instrument-pin (tip) | freeze-gate self-test | verdict |
|---|---|---|---|---|---|
| m1 | cap `SELF_TEST_TIMEOUT_S 360 -> 120` | rc 1, `FAIL: C2 leg A(b) cap >= 2 x measured: SELF_TEST_TIMEOUT_S=120 MEASURED_SELFTEST_S=161: got 120` | rc 1 (blob not pinned) | rc 0 | KILLED (floors, tip) |
| m2 | `MEASURED_SELFTEST_S = 161 -> 1` | rc 1, `FAIL: C2 leg A(b) measured side pinned to the receipt: MEASURED_SELFTEST_S == 161: got 1` | rc 1 | rc 0 | KILLED (floors, tip) |
| m3 | `floors_guard` floor 176 -> 175, `floors-registry.json` row only | rc 0 (176 assertions) | rc 0 | rc 0 | **SURVIVED** all bounded probes; bare walk rc 2 `FAIL registry floor drift: floors_guard registry=175 expected=176 row=176` |
| m3b | `floors_guard` 176 -> 175 in both in-file tables, JSON unchanged | rc 0 | rc 1 (blob not pinned) | rc 0 | KILLED (tip); bare walk rc 2 `registry=176 expected=175 row=175` |
| m4 | `INSTRUMENT_PINS` entry `6f2c52fb…` deleted | rc 0 | rc 1 `instrument-pin … blob 6f2c52fb… … is not a pinned blob` | rc 0 | KILLED (tip) |
| m5 | one behavioural byte: `SELF_TEST_TIMEOUT_MAX_SCALE = 15.0 -> 15.1` | rc 0 (176) | rc 1 (blob `3610bd7a…` unpinned) | rc 0 | KILLED only by the pin |
| m5b | one comment byte: `Round 91 (claim C2 leg A(a)-(b)` -> `Round 92 …` | rc 0 | rc 1 (blob `d8f634c5…` unpinned) | rc 0 | KILLED only by the pin |
| m6 | self-test timeout enforcement `subprocess.run(..., timeout=cap)` -> `timeout=None` | rc 1, 7 failures, first `FAIL: T2 idle host: the cap is the base and the child times out: exit 2: got 0` | rc 1 | rc 0 | KILLED (floors, tip) |
| m7 | ladder repair reverted: `except (OSError, UnicodeError)` -> `except OSError` | rc 0 | rc 0 | rc 1, `FAIL arm plan-not-utf8 could-not-evaluate: unexpected UnicodeDecodeError(...)`, 1 failure over 31 | KILLED (gate) |
| m7b | full ladder-repair revert: except line + `arm_plan_not_utf8` + its registration removed | rc 0 | rc 0 | rc 1, `FAIL arm floors-row freeze_gate (path + floor == assertion count): freeze_gate floor 31 != self-test assertion count 30`, 1 failure over 30 | KILLED (gate) |

Totals: 10 mutants, 9 killed by the bounded probes, 1 survived the bounded probes (m3) and was killed by the bare-walk
pre-check. No mutant is killed by a probe that was not run. Machine-readable: `mutants.tsv`, `summary.json`, `results.json`.

## Findings

- **F1 (coverage gap, m3 and m3b).** The floors `--self-test` does not run `registry_anchor_drift()`. Lowering the
  `floors_guard` row in `verifiers/floors-registry.json` (m3) leaves all 176 arms green. The guard's `main` catches it
  before any child self-test, at rc 2 (`registry_anchor_drift`, called at `check_assertion_floors.py` `main` line ~610), so
  the frozen behaviour is correct, but no self-test arm pins the JSON row. m3b (in-file tables lowered, JSON unchanged)
  is caught by the same pre-check and by the pin.
- **F2 (coverage gap, m5).** A one-byte behavioural change to the child-cap constant survives every self-test arm. The
  runaway-load clamp arm asserts `child_timeout_s(SELF_TEST_TIMEOUT_S, 1e9) == SELF_TEST_TIMEOUT_MAX_SCALE * SELF_TEST_TIMEOUT_S`,
  computing the expectation from the same constant, so it cannot detect a change to that constant. The only channel that
  reds m5 is the instrument-pin blob check. That is a byte-identity guard, not a behavioural assertion.
- **F3 (scope, not a mutant).** The ExecFloorsCap patch also bumps the `freeze_gate` floor 30 -> 31 in
  `check_assertion_floors.py` (`EXPECTED_INSTRUMENTS`, `INSTRUMENTS`) and in `verifiers/floors-registry.json`
  (`freeze_gate` row). The plan gives that seat the `floors_guard` registry row only and does not name this row in the
  touch list. The bump is not optional once the ladder arm lands: m7b shows the freeze gate's own arm
  `floors-row freeze_gate (path + floor == assertion count)` reds at 31 vs 30. The coupling should be named in the plan.
- **F4 (constraint, not a mutant).** On the candidate, `check_tip_battery.py --rev <rev> --repo <repo>` exceeded the 120 s
  probe cap (rc 124 at 120 s on pristine). The full battery runtime is therefore not measured here. The instrument-pin
  guard, probed through `run_guards` in-process, is 0.09 s with 0 failures on pristine. The L1 gate that prints
  `guards 5 of 5; tip battery exit 0: 3 of 6` needs a budget longer than 120 s.
- **F5 (design cost, m5b).** The pin is byte-exact. A comment-only edit to `check_assertion_floors.py` reds the tip battery
  (m5b). Every future edit to that file needs a pin admission, which is the stated design but should be expected by the
  next author.
- **F6 (ladder repair, m7/m7b).** The single-line ladder repair is killed by the new `plan-not-utf8` arm, and the full
  revert is killed by the freeze gate's floor-coupling arm (F3). The ExecLadder repair is covered by its arm.

## Restoration / hygiene

- Candidate and mutants were built only in `/fast/scratch/hyaku/kotoba-r91/MutTesterRepairs/`. No lane, fleet root,
  or builder patch was written. `git apply` ran in the scratch clone only.
- Scratch directory deleted on exit (trap). Receipts kept in this wave dir: `harness.py`, `tipguard.py`, `results.json`,
  `mutants.tsv`, `summary.json`, `m3-bare.out`, `m3b-bare.out`.
- No installs, no kernel or host setting changes.
