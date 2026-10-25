# Round 72 — plan addendum 1 (errata E1–E4, committed before any claim data)

Written after wave 1 returned (53 of 53 seats settled, `.ufo/waves/round-72/w1-results.json`) and
before any claim data landed: no SKILL.md edit, no SOURCES row, no entry, no instrument edit is
committed when this file is. The frozen plan `plans/round-72.md` (commit `7b229a1`) is not edited;
each erratum below names the plan sentence it supersedes and the wave-1 seat finding that forced it.
No predicate sentence changes. Q28: nothing below widens a judgment table after a seat scored data —
no seat scored claim data in wave 1; wave 1 measured populations, controls and bases.

## E1 — C2: the removal set is frozen, not derived from literal absence (plan § C2, ledger conjunct)

The plan said the ledger "must equal exactly the set of base classes whose literal the counter finds
absent from the live opencode dump". The Q45 census (`w1/ScoutOpencodeV2.md`) found one absent
literal (`CONTEXT.md`) but the re-derivation seats (`ExecOC1.md`, `ExecOC2.md`) found two more
declared classes with **no loader** on v2.1.4 although their literal survives as prompt prose
(`opencode:instructions/CLAUDE.md`, `opencode:claude-home/CLAUDE.md`); the other six classes have
honest v2.1.4 rules (`ExecOC3a/3b/4/5/6`). The target stays `p == 7`, `k == 3` (the census reached
7: the rules are derivable, so the plan's lowering clause does not fire). The ledger conjunct is
replaced by: the ledger must equal exactly the three classes in `FROZEN_REMOVALS` of
`verifiers/check_substrate_repin_v2.py`, each with frozen anchor regexes that the counter itself
finds matching **nothing** in the live opencode dump. A ledgered class outside the set, a missing
one, or one with a live anchor fails. A census row removed by the ledger is excused by
`verify_surfaces.py` only while the same anchors stay absent (the instrument re-checks them), and
the 1.19.x rules stay as the committed fixture generation. Counter sha256 and base reading:
`receipts/freeze2-counters.txt`, `receipts/c2-base.txt` (exit 2: `cannot evaluate`, the default
opencode path is gone — the do-nothing control is not a pass).

## E2 — C3: instrument blob pins (plan § C3, guard list)

`w1/ExecBatteryControls.md` F1: world `probe-clean-guards` read `6 of 6` and passed all four
structural guards (a 16-line semantic weakening of the two corpus gates inside the 40-line cap,
baseline blessed, the other two gates fixed honestly). F2: the plan's size cap as worded does not
catch a stub. The counter adds the guard `instrument-pin`: each of the six battery scripts must be
byte-identical to the base blob or to one named draft blob (the wave-1 drafts `ExecArmFix` and
`ExecIndexBaseline`, applied to the base blobs, plus the L1's floors raise) — `INSTRUMENT_PINS` in
`verifiers/check_tip_battery.py`. The size cap and floors guard stay. F3/F4 (a floor edit alone cannot
hide a self-test failure; the "bless drift" world moves nothing) are recorded as properties of
those controls, not as counter changes.

## E3 — C1: a box states its rule (plan § C1, clause (a))

`w1/ExecAuthorControls.md`: world `w9-token-list` (the four boxes replaced by their token sets
under honest tails) read `4 of 4` under the frozen clause (a). The counter adds a minimum body of 25
words before the tail (`MIN_BODY_WORDS`), self-test arm `token-only box under an honest tail`. The
headline is bounded to what the counter reads (Q26): **the counter counts boxes of the stated form
with the stated sources; whether a box carries its rule is a reviewer judgement**, assigned to the
wave-2 reviewers and the non-author closure and reported as such. World `w10-quote-echo-snapshot`
is closed by construction: the snapshot shas are frozen in the counter source (`SNAPSHOT_PINS`),
not read from the measured revision.
The A4 pins name the three rows the assimilated entry cites (new ids by document: S214 Factory,
S215 pi, S216 Hermes Agent); the entry cites the committed wave-1 snapshots
(`.ufo/waves/round-72/snapshots/S262-…md`, `S263-pi-skills.md`, `S264-hermes-skills.md`).

## E4 — C1: what the control receipts are

The wave-1 control bundles (`w1/build/ExecAuthorControls`, `ExecBatteryControls`,
`ExecRepinControls`) were scored by the seats' own oracles/instruments, built before the final ids
existed. Each counter's `--self-test` drives `main()` on a satisfying fixture world and one broken
world per conjunct in isolated local git worlds (50, 16 and 42 assertions;
`receipts/c-selftest-*.txt`); the bases read `0 of 4` exit 1 (C1), `cannot evaluate` exit 2 (C2) and
`2 of 6` exit 1 (C3) (`receipts/c1-base.txt`, `c2-base.txt`, `c3-base.txt`). Replay of the seats'
shortcut bundles against the landed counters on the landed tree is a wave-2 item
(mutation-testers), reported as a second measurement, never in place of the declared one.
