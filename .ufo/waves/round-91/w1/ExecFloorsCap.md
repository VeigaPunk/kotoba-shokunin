# ExecFloorsCap — C2 leg A build (floors child cap + instrument-pin admission + freeze_gate floor bump)

Seat: ExecFloorsCap (executor). Base: freeze commit 9af1a7af2adf0ab07cfd53f92affc1ed8d992262.
Patch: `.ufo/waves/round-91/w1/ExecFloorsCap/ExecFloorsCap.patch` (3 files, `--binary`, against the freeze base; 166 lines).
READY: `.ufo/waves/round-91/w1/ExecFloorsCap_READY` → `blob=6f2c52fb2e09e817dff3360b97400a5d6e53626c selftest_N=176 rc=0`.

## Files changed (scratch clone only; lane untouched)

- `verifiers/check_assertion_floors.py`
  - (a) `SELF_TEST_TIMEOUT_S = 120` → `360`; comment names `.ufo/waves/round-91/receipts/harness-selftest-duration.txt`.
  - (b) `MEASURED_SELFTEST_S = 161` (ceil 160.2) with its receipt named; arms: `SELF_TEST_TIMEOUT_S >= 2 * MEASURED_SELFTEST_S` and `MEASURED_SELFTEST_S == 161` (pins the measured side so lowering it reds too).
  - (c) over-cap arm (`--self-test-timeout 0.3 --load 1`, child sleeps 3.0 s → `FAIL stub self-test timed out after 0.3s`, exit 2, no PASS line) and sub-cap arm (`--self-test-timeout 2.0 --load 1`, child 0.2 s → `PASS stub observed=3 floor=3`, exit 0), through the existing `run_flags`/`slow_world` seam; plus two shipped-constant arms on `child_timeout_s` (idle keeps base; runaway clamps at 15 x base).
  - `floors_guard` 150 → 176 in both in-file tables and the docstring.
  - `freeze_gate` 30 → 31 in `EXPECTED_INSTRUMENTS`, the `INSTRUMENTS` row and the docstring (L1 directive; see Coupling).
  - Docstring CHILD CAP: base 120 → 360, round-91 paragraph; stale `15 x 120 s` comment → `15 x 360 s`.
- `verifiers/floors-registry.json`: `floors_guard.floor` 150 → 176 and `freeze_gate.floor` 30 → 31. `instrument_total` stays 19. No other row touched.
- `verifiers/check_tip_battery.py`: `INSTRUMENT_PINS["verifiers/check_assertion_floors.py"]` appended with `6f2c52fb…` and a pointer comment to `plans/round-91.md § C2 leg A(d)`; the three existing entries kept.

Not touched: `check_freeze_gate.py` (ExecLadder's file), SKILL.md, spotcheck lessons, corpus, `.ufo/state`, MANIFEST, scripts, the lane index.

## Evidence (observed lines)

- Base count from freeze commit (`git archive 9af1a7a verifiers`, self-test): `0 failure(s) over 165 assertions` (`floors-selftest` base, scratch).
- Clone, final bytes: `python3 -B verifiers/check_assertion_floors.py --self-test` → `0 failure(s) over 176 assertions`, rc 0 (`floors-selftest.txt`).
- Arm reconciliation: 9 new `rec` calls + 2 `swap` anchor assertions from the two new `slow_world` worlds = +11 → 176. Per-label log diff vs base: only the 11 new labels differ.
- `python3 -B verifiers/check_tip_battery.py --self-test` → `self-test: 0 failure(s) over 74 assertions`, rc 0 (`tip-selftest.txt`).
- Pure drift check (imports module; calls read-only `registry_drift` / `registry_anchor_drift`; no instrument walk): `[]` / `[]`; floors_guard row 176 = expected 176 (`drift-check.txt` at the pre-bump state; re-checked at the coupled state: `registry_drift [] anchor []`, `freeze row 31 31`).
- Blob: `git hash-object verifiers/check_assertion_floors.py` → `6f2c52fb2e09e817dff3360b97400a5d6e53626c` (computed after the final floors edit; equals pin on line 141 of check_tip_battery.py).
- Standalone apply proof: fresh clone at 9af1a7a, `git apply --check` OK, applied, `hash-object` = `6f2c52fb…` (`APPLY_CHECK_OK_ALONE`).
- Coupled apply proof (base + ExecLadder.patch + ExecFloorsCap.patch, fresh clone): `COUPLED_APPLY_OK`; `check_freeze_gate.py --self-test` → `0 failure(s) over 31 assertions` rc 0 (`freeze-selftest-coupled.txt`); floors → 176 rc 0; tip → 74 rc 0.
- Able-to-fail (`mutants-driver.py`, copies in scratch, full verifiers tree copied; final bytes):
  - `SELF_TEST_TIMEOUT_S = 120`: rc 1, `FAIL: C2 leg A(b) cap >= 2 x measured … got 120`.
  - `MEASURED_SELFTEST_S = 100`: rc 1, `FAIL: C2 leg A(b) measured side pinned … got 100`.
  - clamp removed: rc 1, `FAIL: C2 leg A(a) shipped cap: a runaway load clamps … got 360.0` (plus T1/T3).
  - child timeout disabled (`timeout=cap*1000`): rc 1, 16 failures incl. `C2 leg A(c) over-cap child: exit 2 … got 0`.
- Not run, per instruction: live floors walk, live tip battery.

## Coupling (L1 directive, verified)

- ExecLadder's patch adds a freeze-gate arm (30 → 31). Its `arm_floor_row` pins the registry `freeze_gate.floor == len(ARMS)`, so the patched freeze gate reads `FAIL arm floors-row freeze_gate … floor 30 != 31` alone (ExecLadder receipt).
- My bump makes the live floors walk expect `freeze_gate` ≥ 31. [INFERENCE from the `observed >= floor` rule, not run] Without the ladder patch, the live floors walk would read `freeze_gate observed=30 floor=31` FAIL.
- Therefore the two patches must land together. Coupled proof above: all three self-tests green.
- Note on the directive's wording: the floors guard treats a floor as a minimum, so the red for a bare 30 comes from the freeze gate's own self-test, not from the floors guard. The bump is still required.

## Findings / deviations from the item text

1. The measured child is `verify_harness_independent.py`, not this guard's own self-test. Docstring and constant comment say so.
2. The receipt's measured revision is `9264baaa…` (round base), not `9af1a7a…` as the item text states. Cited as the receipt says.
3. Base floors self-test count was 165, not the 150 floor; new count 176 → floor 176 (not 174 from my first pass; corrected before commit).
4. [INFERENCE] Old-base rationale: at load factor 1 the 120 s cap is below the measured 160.2 s child runtime; at the measured load 2.73 the scaled cap is 120 × 2.73 ≈ 328 s, which exceeds 160.2 s, so that measurement did not hit the cap. The docstring states the arithmetic only.
5. Pin-admission gap is healed in the patch; live `instrument-pin` guard not verified here (L1 measures).

## Risks

- `SELF_TEST_TIMEOUT_S` also governs the guard's own inner subprocess timeouts in `self_test()`; they widen from 120 to 360 s (longer hang backstop for fixture runs, no false-green path).
- The `== 161` pin arm reds on any future re-measurement, intentionally (re-measure must edit constant and pin together).
- Blob pin is exact-bytes: any later edit to `check_assertion_floors.py` requires re-pinning.
- Patch is coupled to ExecLadder's patch on the freeze_gate floor (see Coupling). Applying mine alone reds the live floors walk on freeze_gate (inference above).
- L1 must run: `python3 -B verifiers/check_tip_battery.py --rev <landing>` (expect `guards 5 of 5; tip battery exit 0: 3 of 6`) and a bare `python3 -B verifiers/check_assertion_floors.py` at the landing (exit 0, 360 s cap).

## Host / tooling

- No package or tool installs. No sysctl, kernel, or PATH changes. No pacman.
- Scratch dir `/fast/scratch/hyaku/kotoba-r91/ExecFloorsCap/` removed at yield; receipts retained under `.ufo/waves/round-91/w1/ExecFloorsCap/`.
