## Controls

- control w_tip: bash verifiers/fixtures/freeze-gate/sim-w-tip.sh
  expect: exit 0; stdout contains D5=PASS
- control w_healed: bash verifiers/fixtures/freeze-gate/sim-w-healed.sh
  expect: exit 0; stdout contains D5=PASS
- control w_silenced: bash verifiers/fixtures/freeze-gate/sim-w-silenced.sh
  expect: exit 0; stdout contains D5=FAIL-world-unreachable
- control w_added_red: bash verifiers/fixtures/freeze-gate/sim-w-added-red.sh
  expect: exit 0; stdout contains D5=PASS
