# Round 93 — addendum 1 (KotobaR93, L1; integration record — no predicate, counter, control, target or kill rule changes)

Frozen at `6d7eee0570912d9f3b9d3e3d0137f3c755451233`: `plans/round-93.md`,
`verifiers/fixtures/round-93/c1-killpin-rev.sh`, `verifiers/fixtures/round-93/c2-pinkey.sh`, both
forgery patches and the pre-data receipts. None of those bytes changes in this addendum.

## A1 — integration repair to the C1 builder patch (ReviewerKillPin, blocking)

ExecKillPinRev's patch rebinds the module global `KILL_SET_PINNED` to fixture values (9, 10) inside
`self_test()` and never restores it; the round-92 live arms then compared against the leaked fixture
value. The dropped-row live arm passed for the wrong reason (`kill_set_check(dropped_text)` read
`observed 16 kill rows, pinned 9`), and the live-manifest arm had been switched to a literal 17
(`.ufo/waves/round-93/w1/ReviewerKillPin.md` line 7). The L1 repair, before any landing reading:
`self_test()` captures `module_pin = KILL_SET_PINNED` on entry, both live arms pass `module_pin`
explicitly, and the `finally` block restores the module value. Self-test after the repair:
`0 failure(s) over 31 assertions`. The `--rev` path, the three `mb-*` manifest anchors (each matches
once) and `KILL_SET_PINNED = 17` are unchanged by the repair.

## A2 — pre-landing reading on the integrated scratch candidate (not a landing measurement)

On the scratch commit `cc5b537eba845a24252cac2c1646528e05c3769b` (freeze + the four builder patches +
A1; a scratch revision that does not resolve in the lane, declared as such): the C1 counter read
`C1-PREDICATE-MET` rc 0 and the C2 counter read `C2-PREDICATE-MET` rc 0. These readings are
diagnostic only. The claim readings are taken at the committed lane landing revision and recorded in
`.ufo/waves/round-93/receipts/landing/` (round-92 closure defect 1).
