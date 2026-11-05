# r88-controls-fixed.md — the round-88 C2 controls with the OBSERVED verdicts (fixture)

The same four round-88 controls as `r88-controls.md` (plans/round-88.md § C2), with
each expectation re-declared to the verdict the committed round-88 receipts record:

- `w_added_red` observed **PASS** (ExecMonotoneD5 F1; CriticFalsify C2-S1) — the
  r88 declaration `stdout contains D5=FAIL` was unsatisfiable;
- `w_silenced` observed **FAIL via (i)** — the identity leg reads "rev has 8 names,
  base has 9", so the silenced check's world is unreachable
  (`D5=FAIL-world-unreachable`);
- `w_healed` observed **PASS** (a healed red passes);
- `w_tip` observed **PASS** (the honest landing tip; before-C2-tip.txt records the
  do-nothing r87 reading `4 of 5` at the same tip, l1-c2-tip.txt and
  ReviewerC2/review.md item 4 record the v2 reading `5 of 5`).

The same gate must HOLD this plan: exit 0. Holding the fixed plan while refusing
`r88-controls.md` is the mechanical reproduction of F1 — the gate discriminates the
unsatisfiable declaration from the observable reality, which is what round 88's
unexecuted freeze did not do.

## Controls

- control w_added_red: bash verifiers/fixtures/freeze-gate/sim-w-added-red.sh
  expect: exit 0; stdout contains D5=PASS
- control w_silenced: bash verifiers/fixtures/freeze-gate/sim-w-silenced.sh
  expect: exit 0; stdout contains D5=FAIL-world-unreachable
- control w_healed: bash verifiers/fixtures/freeze-gate/sim-w-healed.sh
  expect: exit 0; stdout contains D5=PASS
- control w_tip: bash verifiers/fixtures/freeze-gate/sim-w-tip.sh
  expect: exit 0; stdout contains D5=PASS
