# r88-controls.md — the round-88 freeze's C2 control declarations, as frozen (fixture)

Reconstructs plans/round-88.md § C2's four discrimination controls exactly as the
round-88 freeze declared them, BEFORE any control was executed. The declared
expectation for `w_added_red` ("v2 D5 FAIL (ii)") is the unsatisfiable one: the
committed round-88 record shows the v2 gate reads D5 PASS on that world
(ExecMonotoneD5 F1: "the monotone test cannot see a new instance"; CriticFalsify
C2-S1: "the frozen control, as written, cannot FAIL under (ii)"). Round 88 shipped
this freeze with the control never executed — spotcheck routed defect 3. Running
this plan through `verifiers/check_freeze_gate.py` must therefore REFUSE the freeze:
exit 1, naming `w_added_red`, with the declared-vs-observed text.

Grounded declarations (plans/round-88.md § C2, carried verbatim):

- `w_added_red` — the tip plus a pointer to an unresolvable commit in a new lesson
  line → v2 D5 FAIL (ii).
- `w_silenced` — the tip with one integrity check removed from the script → v2 D5
  FAIL (i) (a monotone-only variant passes this world; that is why (i) exists).
- `w_healed` — the base `223ae62` with `report_dead` absent (a fixture that resolves
  its one red) → v2 D5 PASS.
- `w_tip` — the landing tip → v2 D5 PASS.

Each control's command is a committed simulator
(`verifiers/fixtures/freeze-gate/sim-*.sh`) that greps the named round-88 receipt
and prints the OBSERVED world verdict it records; a missing receipt exits 2
(fail-closed). Grounding per control: `w_added_red` →
`.ufo/waves/round-88/w1/ExecMonotoneD5.md` (F1) + `w1/ExecMonotoneD5/receipts.txt`
(`--- w_added` block); `w_silenced` → `receipts.txt` (`--- w_silenced` block) +
`w1/CriticFalsify/attacks.md` (C2-S2); `w_healed` → `receipts.txt` (`--- w_healed`
block); `w_tip` → `receipts/before-C2-tip.txt` (the r87 do-nothing reading) +
`receipts/l1-c2-tip.txt` + `w1/ReviewerC2/review.md` (item 4, the reviewer's
independent re-derivation).

## Controls

- control w_added_red: bash verifiers/fixtures/freeze-gate/sim-w-added-red.sh
  expect: exit 0; stdout contains D5=FAIL
- control w_silenced: bash verifiers/fixtures/freeze-gate/sim-w-silenced.sh
  expect: exit 0; stdout contains D5=FAIL
- control w_healed: bash verifiers/fixtures/freeze-gate/sim-w-healed.sh
  expect: exit 0; stdout contains D5=PASS
- control w_tip: bash verifiers/fixtures/freeze-gate/sim-w-tip.sh
  expect: exit 0; stdout contains D5=PASS
