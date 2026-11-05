# ReviewerRepairs — attack C2 leg A (cap arithmetic, arm, pin, tip battery)

Seat: ReviewerRepairs (reviewer, attack). Base: freeze commit `9af1a7af2adf0ab07cfd53f92affc1ed8d992262`.
Scratch clone: `/fast/scratch/hyaku/kotoba-r91/ReviewerRepairs/repo` (deleted at yield; second probe clone `repo2` also deleted).
Waited for `ExecFloorsCap_READY`: absent at first 6 polls (120 s cadence from 12:0x), present from 12:15.

Candidate: `git clone -q --shared <lane> $S/repo && git checkout -q 9af1a7af2adf0ab07cfd53f92affc1ed8d992262`
then `git apply ExecFloorsCap.patch`, committed scratch-only as
`cd21b3c0ebaa67600c5b2b732a565c6be0032268`
(`git -C $D rev-parse --show-toplevel` == `$D` before the commit). Files touched by the patch:
`verifiers/check_assertion_floors.py`, `verifiers/check_tip_battery.py`, `verifiers/floors-registry.json`.

**Receipt-status note (no defect, corrected mid-run by the builder):** the `blob.txt` I first
observed read `0b29bcd0…` (12:0x); by 12:14–12:15 the seat dir was refreshed and
`ExecFloorsCap_READY` read `blob=6f2c52fb2e09e817dff3360b97400a5d6e53626c selftest_N=176 rc=0`,
matching the patch pin and my `git hash-object` on the applied bytes. Apply-proof:
fresh clone at 9af1a7a + `git apply --check` → clean (replicated twice).

## (a) Self-test on the candidate — PASS

Command: `cd $S/repo && TMPDIR=$S/tmpe python3 -B verifiers/check_assertion_floors.py --self-test`
- Observed: `0 failure(s) over 176 assertions`, `rc=0` (twice; wall ~5.8 s each).
- New arms present by name (from candidate bytes, `rec(` call sites total 120):
  - `C2 leg A(b) cap >= 2 x measured: SELF_TEST_TIMEOUT_S=%s MEASURED_SELFTEST_S=%s`
  - `C2 leg A(b) measured side pinned to the receipt: MEASURED_SELFTEST_S == 161`
  - `C2 leg A(a) shipped cap: an idle host keeps the base exactly`
  - `C2 leg A(a) shipped cap: a runaway load clamps at 15 x the shipped base`
  - `C2 leg A(c) over-cap child: exit 2` / `the line reads self-test timed out` / `no PASS line is printed`
  - `C2 leg A(c) sub-cap child: exit 0` / `the PASS line is printed`

## (b) Q39 arithmetic — PASS

- `SELF_TEST_TIMEOUT_S = 360` (line 208), `MEASURED_SELFTEST_S = 161` (line 214, `# ceil(160.2)`).
- `360 >= 2 * 161 = 322` holds; 161 = ceil(160.2 s) of the committed receipt
  `.ufo/waves/round-91/receipts/harness-selftest-duration.txt` (`wall-seconds: 160.2`,
  `0 failure(s) over 123 assertions`, loadavg 2.73 → 3.16, rev `9264baaa…`).
- 360 = 2 × 160.2 = 320.4 rounded up to the 60 s grid; comment names the receipt. Docstring
  arithmetic updated (stale round-56 `15 x 120 s` → `15 x 360 s`).

## (c) Able-to-fail (scratch copy `repo2`, never the candidate) — PASS

- Cap lowered to 120: `1 failure(s) over 176 assertions`, rc 1,
  `FAIL: C2 leg A(b) cap >= 2 x measured: SELF_TEST_TIMEOUT_S=120 MEASURED_SELFTEST_S=161: got 120`.
- `MEASURED_SELFTEST_S = 1`: rc 1, `FAIL: C2 leg A(b) measured side pinned to the receipt: MEASURED_SELFTEST_S == 161: got 1`.
- `MEASURED_SELFTEST_S = 180`: rc 1, same measured-side pin line (`got 180`) — any change on the
  measured side reds, not just lowering. (The cap-side arm also reds if 2×measured rises above 360,
  but the pin arm reds first at 180.)

## (d) Pin cross-check and pin-guard FAIL probe — PASS (attack intent), one attribution caveat

- `git -C "$D" hash-object verifiers/check_assertion_floors.py` on the candidate = `6f2c52fb2e09e817dff3360b97400a5d6e53626c`;
  the ExecFloorsCap patch appends exactly that blob to
  `INSTRUMENT_PINS["verifiers/check_assertion_floors.py"]` in `verifiers/check_tip_battery.py`
  (comment names `plans/round-91.md § C2 leg A(d)`; prior three blobs kept).
- One-byte flip in `repo2` (offset 14217, `R`→`O`, mutated blob `0f877ae28587b5ffbfefac81b9778a178220c542`), then
  `TMPDIR=$S/tmpe python3 -B verifiers/check_tip_battery.py --rev 9af1a7af2adf0ab07cfd53f92affc1ed8d992262`:
  observed `FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob c10c0f108f484221d0a7600ac227f10f019f5d4d at 9af1a7af2adf0ab07cfd53f92affc1ed8d992262 is not a pinned blob`,
  `guards 4 of 5; tip battery exit 0: 3 of 6`, wall ≈ 202–224 s.
- Caveat (verification gap, recorded honestly): the pin guard reads the blob **at the named rev**,
  and I named the freeze base, whose floors blob is `c10c0f10…` (already unpinned — this is
  exactly the r90 gap the patch heals). The run before any mutation (`bg_6504`, clean clone) printed
  the identical FAIL line, so the FAIL at that rev is **not attributable to my one-byte flip**.
  The fail-closed direction is confirmed (guard names the class and refuses), but the
  mutated-blob→FAIL edge itself was not isolated; the green edge (`guards 5 of 5` at the landing
  rev with the admitted blob) must be read at the landing, not at 9af1a7a. No other guard regressed
  at this rev (no-deletions/floors/instrument-size/spotcheck-identity all PASS on both runs —
  base no-harm holds).

## (e) Live floors walk on the candidate (patch A only) — OBSERVED rc 1 (coupling, see finding)

Command: `cd $S/repo && TMPDIR=$S/tmpe python3 -B verifiers/check_assertion_floors.py` (bare), wall 223.55 s ≤ GATE_TIMEOUT_S 280.

```
... 18 PASS rows ...
PASS floors_guard observed=176 floor=176
FAIL freeze_gate observed=30 floor=31 self_test_failures=1
```
rc 1, wall 3:43.54 (`/usr/bin/time -v`; that run also included `PASS harness observed=34 …` through
`PASS pins observed=62 floor=62` — full line list in the transcript). With ExecLadder's patch
absent, the freeze-gate self-test stays at 30 formulas, so the in-file floor bump to 31 reds it.
This is the documented two-patch coupling (ExecFloorsCap.md § Coupling); my item defined the
candidate as patch A only, so this rc 1 is the *expected* reading for that intermediate candidate,
not a counter defect. The landed candidate (A + B) is the one the plan predicates; its bare walk
must be green and is ExecLadder/L1's commitment (their coupled self-tests already read green:
`freeze-selftest-coupled.txt` `0 failure(s) over 31 assertions`).

## Attack items name what they attack

- (a)/(b) attack the cap-constant reading (`SELF_TEST_TIMEOUT_S`, `MEASURED_SELFTEST_S`) and the
  Q39 calibration tie to the committed measurement receipt.
- (c) attacks arm liveness: the new arms must fail when the calibrated constants move.
- (d) attacks the instrument-pin admission (E2-style laundering channel): a one-byte floors edit
  must leave the tip battery red unless the blob is admitted.
- (e) attacks the floors_guard floor bump and the freeze_rate pre-coupling: the live walk with the
  bump but without the ladder patch should be red on freeze_gate (it is).

## Verdict

Per-item: (a) PASS, (b) PASS, (c) PASS, (d) PASS with attribution caveat, (e) rc 1 as predicted by
the coupling. No counter defect found against leg A's frozen predicate. Scoped findings in
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-91/w1/ReviewerRepairs.md`.
Scratch deleted before this receipt was written; tool installs: none.
