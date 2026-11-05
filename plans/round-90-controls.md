# Round 90 — pre-data controls (frozen declarations)

Executed through the round-89 capability before any candidate score:

    python3 -B verifiers/check_freeze_gate.py --plan plans/round-90-controls.md

Each control script exits 0 iff its world MEETS the claim predicate of `plans/round-90.md`;
the frozen declaration expects the do-nothing / shortcut worlds to be UNMET (exit 1). Base
revision: `0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5`.

## Controls

- control ctl-c1-absence: bash verifiers/fixtures/round-90/ctl-c1-absence.sh
  expect: exit 1; stdout contains C1-PREDICATE-UNMET
- control ctl-c1-r89harness: bash verifiers/fixtures/round-90/ctl-c1-r89harness.sh
  expect: exit 1; stdout contains C1-PREDICATE-UNMET
- control ctl-c1-stub: bash verifiers/fixtures/round-90/ctl-c1-stub.sh
  expect: exit 1; stdout contains C1-PREDICATE-UNMET
- control ctl-c2-windows: bash verifiers/fixtures/round-90/ctl-c2-windows.sh
  expect: exit 1; stdout contains C2-PREDICATE-UNMET
- control ctl-c2-empty: bash verifiers/fixtures/round-90/ctl-c2-empty.sh
  expect: exit 1; stdout contains C2-PREDICATE-UNMET
- control ctl-c2-fake: bash verifiers/fixtures/round-90/ctl-c2-fake.sh
  expect: exit 1; stdout contains C2-PREDICATE-UNMET
