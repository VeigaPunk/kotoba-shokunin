# ReviewerKillPin — review of ExecKillPinRev C1 patch (round 93)

Full findings are at `.ufo/waves/round-93/w1/ReviewerKillPin/ReviewerKillPin.md` (same content).

Verdict: C1 met on the candidate `9bf0090ee80c001bcd69d895ee304c1051f68086`; frozen counter reads `C1-PREDICATE-MET` (drop rc 2 names kill-set-size; other rc 2 does not; honest rc 0 does not).

BLOCKING (arm only): `verifiers/check_mutation_battery.py:800` calls `kill_set_check(dropped_text)` without the pin, so it compares against the leaked module value 9, not 17. Sim C: forcing 16 there makes the arm FAIL ("observed 16 kill rows, pinned 16"); with explicit 17 the arm passes. Fix: `kill_set_check(dropped_text, 17)`.

Non-blocking: patch uses `c/`/`w/` prefixes (applies, same bytes); round-92 shortcut control was not run on the candidate; builder controls-run.sh timed out in its seat.
