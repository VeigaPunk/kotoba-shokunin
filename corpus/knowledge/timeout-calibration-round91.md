source: S263 (Python documentation — subprocess — https://docs.python.org/3/library/subprocess.html — § Using the subprocess Module, definition-list entry `subprocess.run` (HTML line 270), timeout paragraph at HTML lines 288-292; contrast entry `subprocess.Popen.communicate` at HTML line 1042; page footer "Last updated on Nov 05, 2026 (12:47 UTC)" at HTML line 2037; fetched 2026-11-05) and the own-work receipt `.ufo/waves/round-91/receipts/harness-selftest-duration.txt` (the round-91 standalone measurement of `verify_harness_independent.py --self-test`: wall-seconds 160.2, exit 0, `0 failure(s) over 123 assertions`, 1-minute loadavg 2.73 at start and 3.16 at end, measured against revision 9264baaa823cdae3d009a4004e014639551e016f)
verified-at: 2026-11-05 @ base 9af1a7af2adf0ab07cfd53f92affc1ed8d992262 (the round-91 freeze commit, which carries the measurement receipt; the receipt names its own measured revision, 9264baaa823cdae3d009a4004e014639551e016f, which is the round base)
recheck: grep -n '^SELF_TEST_TIMEOUT_S = ' verifiers/check_assertion_floors.py (expect `SELF_TEST_TIMEOUT_S = 360`) and python3 -B verifiers/check_assertion_floors.py --self-test (expect `0 failure(s) over N assertions`, exit 0) and python3 -B verifiers/check_tip_battery.py --rev <landing-rev> (expect `guards 5 of 5; tip battery exit 0: 3 of 6`) — the frozen predicate of plans/round-91.md § C2 leg A

# Timeout calibration (round 91 C2 leg A): a measured child duration and a cap derived from it

## What the guard is and what the cap is

`verifiers/check_assertion_floors.py` reruns every registered instrument's `--self-test` and FAILs
when the observed assertion count is below the recorded floor. Each child self-test runs under a
per-child cap: the base `--self-test-timeout` seconds scaled by the host's 1-minute runnable count
(`child_timeout_s`), clamped at `SELF_TEST_TIMEOUT_MAX_SCALE` times the base. The base at the
round-91 freeze commit was `SELF_TEST_TIMEOUT_S = 120`.

Two things about that cap matter for the round:

1. **A too-tight cap is a false red, a too-generous cap is only a delayed report.** A child that is
   merely slow under fleet load is read by a tight cap as a hang (`exit 2`, "could-not-evaluate"),
   which is indistinguishable from a genuinely hung child. A generous cap only postpones the report
   of a real hang.
2. **The scale factor cannot rescue the idle case.** At load factor 1 (an idle host, or the
   `--load 1` probe affordance) the cap equals the base exactly.

## The Q39 calibration arithmetic

Q39 requires a nested self-test timeout to be calibrated against a *measured* duration with
declared headroom, and to record the host load and the elapsed wall time, so that an unannotated
timeout cannot be read as either a hang or a slow-but-healthy child. The round-91 calibration is
three steps, all from the committed receipt:

1. **Measured:** `verify_harness_independent.py --self-test` run standalone measured
   **160.2 s** wall, exit 0, `0 failure(s) over 123 assertions` (`.ufo/waves/round-91/receipts/
   harness-selftest-duration.txt`; the receipt names its measured revision
   `9264baaa823cdae3d009a4004e014639551e016f`).
2. **Doubled:** `160.2 x 2 = 320.4 s` of headroom over the measured child.
3. **Rounded up to the 60 s grid:** `320.4 -> 360`, so the shipped base is
   **`SELF_TEST_TIMEOUT_S = 360`**.

At the old base of 120 s the idle-host cap was below the measured standalone duration of that
child: a healthy tree could be read as a hang. At 360 the same child has more than twice its
measured standalone runtime of headroom at load factor 1, and still more under load.

**The MEASURED constant.** The measurement is also pinned in the file, so the cap and its
justification cannot drift apart: a new constant `MEASURED_SELFTEST_S = 161` (the ceiling of the
measured 160.2 s) cites the receipt, and a new floors-guard self-test arm asserts
`SELF_TEST_TIMEOUT_S >= 2 * MEASURED_SELFTEST_S`. Lowering the cap reds the arm; lowering the
measured side reds a second arm that pins the measured constant to its receipt value, so the two
sides must be edited together and a re-measurement cannot silently become the new premise.

**The timeout contract (S263).** The cap is only meaningful against the API it wraps, and the two
`subprocess` timeout APIs differ. `subprocess.run(..., timeout=cap)` is a kill-and-wait contract:
on expiry the child is killed and waited for, and `TimeoutExpired` is raised after the child has
terminated. The lane's floors guard calls `subprocess.run` with `timeout=cap` for every child
self-test, so a child that overruns its cap is killed and reaped before the guard reads
`TimeoutExpired` — a timeout report does not leak an orphan child. `Popen.communicate(timeout=…)`
is the opposite contract (the child is not killed on expiry), so it is not interchangeable for a
timeout gate; this is why the row's scope names the `run()` contract as the one that binds.

## Bounds (what this calibration does not establish)

1. **One host, one measurement.** The 160.2 s figure is a single sample taken on this Linux host on
   2026-11-05 under fleet load (1-minute loadavg 2.73 at the start, 3.16 at the end), not an
   idle-host sample and not a distribution. It bounds the child as observed, not the child's worst
   case on a busier or slower machine.
2. **One instrument.** The measurement covers `verify_harness_independent.py --self-test` alone.
   The other registered instruments' self-tests were not re-measured this round, so the calibration
   is grounded on the slowest measured child, not on a measured maximum over the whole set.
3. **The base is a floor on the cap, not the cap itself.** `child_timeout_s` scales the base by
   the host's 1-minute runnable count, so 360 s is the cap at load factor 1; under load the
   effective cap is larger, and at the measurement's own load of 2.73 the *old* 120 s base would
   have scaled to about 328 s — which is why the measured run did not itself hit the old cap, and
   why the idle-host case is the one the arithmetic must cover.
4. **The doubling and the 60 s grid are calibration policy, not measurement.** 160.2 s is
   measured; the factor 2 and the grid are chosen margins. Only the measured side is evidence.
5. **The cap also bounds the guard's own inner fixture subprocesses.** The same constant is the
   timeout for the guard's self-test worlds, so the shipped base widens those fixture backstops
   too. That is a longer hang backstop, not a false-green path.
6. **The able-to-fail arms exercise the cap through the guard's own seam** (the
   `--self-test-timeout` / `--load` affordance in hermetic stub worlds), not against a real hung
   child on this host.

## Reviewer-judged parts

Whether the headroom factor and the grid are the right margins, and whether one measured child is
the right calibration target, are named non-author seats' calls in the round-91 wave; they are not
measured here.
