# Round 91 — addendum 1 (L1 amendments and dispositions)

Author: KotobaR91a2 (L1, attempt 2). Attempt 1 (KotobaR91) froze the plan and dispatched wave
`r91-w1` (`.ufo/waves/round-91/r91-w1.ready.dispatched`, 2026-11-05T12:06:18-03:00), then ended
without a landed report (watchdog `lane-dead-no-report kotoba round=91`, 2026-11-05T13:34:09-03:00).
Base: freeze commit `9af1a7af2adf0ab07cfd53f92affc1ed8d992262`.

**Timing disclosure.** A1, A3 and A5 were written after the wave-1 seats had returned candidate
readings (their receipts under `.ufo/waves/round-91/w1/`). None of them changes a predicate sentence,
counter, manifest row, PROBES entry, control script or fixture. Every landing measurement is taken
at the landing revision, after the landing commit, and is named as such in
`.ufo/waves/round-91/receipts/landing/`.

## A1 — freeze_gate floor coupling (touch-list amendment)

ExecLadder's new freeze-gate self-test arm `arm floors-row freeze_gate` pins
`verifiers/floors-registry.json` `freeze_gate.floor == len(ARMS)` (now 31). The ladder repair
therefore cannot land without the `freeze_gate` floor moving 30 → 31 in `floors-registry.json` and in
the two in-file tables of `verifiers/check_assertion_floors.py` (`EXPECTED_INSTRUMENTS`,
`INSTRUMENTS`). Observed red without it: MutTesterRepairs m7b (`FAIL arm floors-row freeze_gate …
freeze_gate floor 31 != self-test assertion count 30`); coupled proof in
`ExecFloorsCap/freeze-selftest-coupled.txt` (0 failure(s) over 31 assertions). The plan's touch-list
line for `verifiers/floors-registry.json` ("`floors_guard` floor value only") is amended to
"`floors_guard` and `freeze_gate` floor values", and the `freeze_gate` cells of the two in-file tables
are added to the touch list. ExecFloorsCap made this bump under attempt 1's directive; this addendum
records it. No predicate changes: leg A(d)'s tip-battery line, leg B(b)'s `N' > 30` and the floors
guard's `instrument_total` (stays 19) are untouched.

## A2 — census expectation (187 → 190, not 189)

Plan § Frontier step says "Census before→after: 187 → 189 expected". The plan's own counting command
(`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`) counts `rejected` rows, and
the round's frontier step places the rejection candidate (S264) in the registry as a `rejected` row.
Measured after-count with S262, S263 and S264 appended: **190** (`.ufo/waves/round-91/w1/ScribeCorpus/census-after.txt`;
census validate exit 0; tiers A 149 / B 23 / C 18; statuses mined 165 / queued 7 / rejected 18). No row
is dropped to meet the old expectation.

## A3 — leg B identity (disposition, recorded after the seats' re-derivations)

The routed pointer (`.ufo/reports/round-90/kotoba.md` § Routed defects, item 5: "Freeze-gate
probe-world exit-ladder inconsistency") names no rung or input class. Disposition: the claim is
bound to the **non-UTF-8-plan rung mismatch**, which is re-derived from committed base bytes
(`ExecLadder/rung-probe-base.txt`: a non-UTF-8 plan exits 1 with an uncaught `UnicodeDecodeError`
where the docstring ladder assigns rung 2; RevengerLadder's 17-row probe reads the same first
mismatch; CriticClaims reproduces it in `receipts/ladder-rung-base.txt`). The re-derivation record is
`receipts/ladder-defect.md`. The identity of this instance with the routed pointer is a judgement and
is **not established** by the seats: CriticClaims F4 names a second documented-but-odd path (a
fail-closed simulator exiting 2 that the gate reports as rc 1), which the gate docstring states is
intended. Leg B is claimed on the re-derived instance; the pointer's identity is reported open, not
closed. Same-class ladder findings left unrepaired and routed to round 92 (not claimed closed):
`--work` under a regular file → uncaught `NotADirectoryError` (ExecLadder F4; CriticClaims F5),
duplicate control names both run and read `held` (ExecLadder F1), declared `exit 127` never compared
(ExecLadder F2).

## A4 — plan citation corrected (C1 no-work evidence pointer)

Plan § C1 says the controls `ctl-c1-m2/mb-m15/mb-m16` "print `SURVIVED` (plans/round-91-controls.md)".
That file declares four controls and names no mutant replay, so the pointer is wrong. The base
SURVIVED evidence is the round-90 battery transcript
(`.ufo/waves/round-90/w1/MutTesterBattery/transcripts/harness-run.log`, lines 9, 22, 23), re-observed
at base bytes this round (`ExecBatteryArms/mutant-mb-m2.txt`, `mutant-mb-m15.txt`, `mutant-mb-m16.txt`;
replayed again by CriticClaims). The claim's substance is unchanged; the pointer is corrected.

## A5 — frozen-control defects (recorded, routed, not repaired)

(i) `ctl-c2-capline-only` reads the working-tree cap and tests only `cap >= 320`; on the cap-only
shortcut world it prints `C2-PREDICATE-MET`, exit 0, so it does not refuse the shortcut it names
(CriticClaims § Controls). The shortcut is refused by the real instrument instead: the tip battery's
`instrument-pin` guard FAILs on the cap-only world (`CriticClaims/receipts/tip-battery-capline-only-shortcut.txt`,
`guards 4 of 5; tip battery exit 0: 2 of 6`). (ii) `ctl-c1-manifest-only` appends its three kill rows
to a clone's working tree while passing the committed base rev to `--rev`; G1 reads committed bytes,
so the appended rows are never read. Its expected exit 1 holds for the plain no-work reason
(`killed 14 of 14`, `C1-PREDICATE-UNMET`), not the shortcut it names. Both controls were executed and
held at the freeze base (`receipts/freeze-gate-r91.txt`, 4 control(s) held, exit 0), which is the only
state they were declared for. They are not re-run at the landing: a post-landing run refuses
`ctl-c2-capline-only` by construction (its cap reads 360). Redesign (committed shortcut worlds that G1
can read; a pin-asserting cap control) is routed to round 92. Kill rule: no control, counter,
manifest or PROBES byte is amended after any scored reading.

## A6 — index and PROVINCE touch-list notes

`corpus/README.md` gains the coverage-map index rows for the three round-91 corpus files and for
`corpus/lessons/round-90-verifier-spotcheck.md` (unindexed at base; carried red `corpus.index.unindexed 1`).
`PROVINCE.md` § Core (round-90 routed defect 3) gains the mutation battery in the executable-instruments
bullet. The frozen touch list's "append-only Frontier notes" is not executed: `verifiers/check_province_core.py`
pins `## Frontier` and `## Adjacent` byte-identical to their base (errata ledger on `## Adjacent` only),
so a Frontier edit would red a historical counter outside any claim. The frontier advance rests on the
SOURCES rows and the round lesson, as the frozen § Frontier step states.
