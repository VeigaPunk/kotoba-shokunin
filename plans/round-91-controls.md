# Round 91 — pre-data controls (frozen declarations)

Executed through the round-89 capability before any candidate exists:

    python3 -B verifiers/check_freeze_gate.py --plan plans/round-91-controls.md --timeout 1200

Each control script exits 0 iff its world MEETS the claim predicate of `plans/round-91.md`; the
frozen declaration expects every do-nothing or shortcut world to be UNMET (exit 1). Base
revision: `9264baaa823cdae3d009a4004e014639551e016f`.

Controls: `ctl-c1-base` runs the battery instrument as it stands at the base (no-work reading);
`ctl-c1-manifest-only` is the shortcut of adding the three guard rows without the instrument
(the uncommitted manifest is not read by G1, so the reading stays unmet — the expectation is
exit 1 either way); `ctl-c2-base` runs the tip battery at the base; `ctl-c2-capline-only` is the
shortcut of raising the child cap alone.

## Controls

- control ctl-c1-base: bash verifiers/fixtures/round-91/ctl-c1-base.sh
  expect: exit 1; stdout contains C1-PREDICATE-UNMET
- control ctl-c1-manifest-only: bash verifiers/fixtures/round-91/ctl-c1-manifest-only.sh
  expect: exit 1; stdout contains C1-PREDICATE-UNMET
- control ctl-c2-base: bash verifiers/fixtures/round-91/ctl-c2-base.sh
  expect: exit 1; stdout contains C2-PREDICATE-UNMET
- control ctl-c2-capline-only: bash verifiers/fixtures/round-91/ctl-c2-capline-only.sh
  expect: exit 1; stdout contains C2-PREDICATE-UNMET
