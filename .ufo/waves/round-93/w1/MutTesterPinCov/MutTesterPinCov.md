# MutTesterPinCov — mutation probe of the C2 build (check_tip_battery.py, instrument-pin coverage)

Seat: MutTesterPinCov. Candidate: `6d7eee0` (freeze) + `ExecPinCoverage.patch` → commit `322fbe0a2212344702481f04672bfc2d114e1153`
(scratch clone; checker sha256 `7c8e741c…`). Counter REPO = scratch clone. Mutants are single-commit edits of that
candidate's checker; each mutant's counter run names its own revision.

## Baseline (pristine candidate bytes)
- `c2-pinkey.sh 322fbe0a… <clone>`: honest `guard instrument-pin PASS` + `guards 5 of 5`; keydrop `FAIL guard instrument-pin: verifiers/check_correction_sweep.py has no INSTRUMENT_PINS key` + `guards 4 of 5`; keyswap same; `C2-PREDICATE-MET`, rc 0.
- `check_tip_battery.py --self-test`: `self-test: 0 failure(s) over 80 assertions`, rc 0.

## Mutant verdicts
Counter = frozen `c2-pinkey.sh`. Self-test = `check_tip_battery.py --self-test`.

| # | Mutant (rev) | Counter | Self-test | Verdict |
|---|---|---|---|---|
| m1 | coverage check deleted (`17808f3d`) | `C2-PREDICATE-UNMET` rc 1: keydrop `guard instrument-pin PASS`, `guards 5 of 5` (silent) | rc 1, 4 FAIL: keydrop exits 0 not 1; keydrop names no key; keydrop tally not 4 of 5; keyswap names no key | **KILLED** (both) |
| m2 | key COUNT not key SET (`cf7cb08e`) | `C2-PREDICATE-UNMET` rc 1: keydrop silent (6 keys ≥ 6 scripts) | rc 1, 2 FAIL: keydrop and keyswap FAIL lines do not name `check_correction_sweep.py` | **KILLED** (both) |
| m3 | coverage only when `len(INSTRUMENT_PINS) >= 7` (`481c3373`) | `C2-PREDICATE-UNMET` rc 1: keydrop (6 keys) silent; keyswap (7 keys) still names the key | rc 1, 4 FAIL (keydrop exit/line/tally; keyswap names) | **KILLED** (both) |
| m4 | failure filed under `instrument-pin-coverage` (`b2e6957a`) | `C2-PREDICATE-UNMET` rc 1: keydrop `guard instrument-pin PASS`, `guards 5 of 5`; the new id is not in the tally | rc 1, 3 FAIL (keydrop names-key, keydrop tally 4 of 5, keyswap names-key) | **KILLED** (both) |
| m5 | coverage hardcoded to `("verifiers/check_correction_sweep.py",)` (`68658a83`) | `C2-PREDICATE-MET` rc 0 (keydrop and keyswap both name the key, tally 4 of 5) | rc 0, `0 failure(s) over 80 assertions` | **SURVIVED** (both) — see hand world |
| m6 | empty-dict exemption removed (`8a1b4834`) | `C2-PREDICATE-MET` rc 0 (counter never runs with empty pins) | rc 1, 5 FAIL (`satisfying world exits 0: exit 1`; frozen line; relative/absolute `--repo`; spot-check-added world) | **KILLED** by self-test; **SURVIVED** the counter |

m5 hand world (`68658a83` with ONLY the `verifiers/check_gate_registry.py` key removed; 6 keys; `--rev 68658a83 --repo <clone> --fleet /home/vgpnk/Projects/shokunin`, rc 1 = carried tip-battery reds):
- `guard instrument-pin PASS`; `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 3 of 6`.
- `grep -c check_gate_registry` on the output: `1` (only the gate-list line; no FAIL naming it). Dropping `check_gate_registry.py`'s key slips through; the mutated checker's coverage check is only for `check_correction_sweep.py`.

## Findings (for L1)
1. **Coverage is pinned to one key, in both the counter and the self-test (m5).** `c2-pinkey.sh` only tests the `check_correction_sweep.py` key; `check_tip_battery.py --self-test` only drops `BATTERY[5]` (`missing = BATTERY[5][0]`). A checker that covers only that one path passes all 80 self-test assertions and the frozen counter. Dropping any of the other five BATTERY keys is unobserved. This is a coverage gap of the C2 predicate itself, not in the disclosed scope (which names only `check_freeze_gate.py`). Recommendation (L1 act, addendum before scoring): parameterize the self-test loop over every BATTERY key (or add a `BATTERY[0]` arm to the counter), then re-run the m5 probe.
2. **The frozen tally hides out-of-tally guard ids (m4).** `guard_ids` is a fixed 5-tuple in `measure()`; a failure filed under any other id prints no `FAIL guard` line and does not move `guards N of 5`. The counter catches this only through its keydrop arm; no separate check asserts the id set.
3. **Counter and self-test are complementary.** m6 passes the counter (the counter's worlds never use empty pins) and is caught only by the self-test. Neither alone kills m1–m6 except m5.
4. No defect found in the frozen counter predicate. The frozen counter is not rescued or edited.

## Evidence files (lane seat dir, this directory)
- `selftest-baseline.out` (`0 failure(s) over 80 assertions`), `selftest-m1..m6.out`
- `counter-m1..m6.out` (per-mutant `c2-pinkey.sh` output, rc)
- `mutant-diffs/m1..m6.diff` (exact mutation vs candidate `322fbe0a`)

## Carried-red note
The tip battery's own exit is 1 in every world (`tip battery exit 0: 3 of 6`); the counter reads only guard lines and the tally, as its header says. Not a finding of this probe.

## Scratch
Clones and scratch dir `/fast/scratch/hyaku/kotoba-r93/MutTesterPinCov/` removed before yield. No lane, fleet, or sibling write; no git write in the lane; no host setting touched. No tools installed.
