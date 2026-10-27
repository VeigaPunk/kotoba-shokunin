# F23 mutation probe — assertion-floor guard

Axes: depth, consistency, calibration, freshness, operability. Probe scope is mutation coverage of assertion-floor guards; this does not verify either claim's data or the full w2 battery.

## Frozen tip and counters

Lane HEAD is `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (`round-77: freeze plan, base receipts (counters unchanged from r76 freeze)`). `git show --name-only HEAD` contains only the plan and base receipts; no claim-data commit is present. Consequently the exact attacked claim data is not landed at this tip.

At the tip, direct counter commands returned:

- `python3 -B verifiers/check_desc_craft.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` → six conjunct failures (`(a)` through `(f)`), `description craft backed 0 of 6`, exit 1.
- `python3 -B verifiers/check_r75_routed_repairs.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e --work /tmp/F23-c2-work` → R1–R4 open, `r75 routed repairs closed 0 of 4`, exit 1.

Counter bytes match the plan pins: C1 `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`; C2 `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`. Both gates are red because data is absent at the frozen tip, so their claim verdict is **inconclusive / not verified**.

## Assertion-floor mutation

Attacked item: `verifiers/check_assertion_floors.py` self-test coverage for floor guards, specifically weakening a required floor from 250 to 249 (and analogous 47→46); this is the smallest relevant behavior-bearing mutation. The committed lane source was not touched by this seat.

The landed-round build evidence `.ufo/waves/round-77/build/M03MutFloors.survivors.md` records the scratch detector `python3 -B verifiers/check_assertion_floors.py --self-test`: pristine `self-test: 0 failure(s) over 165 assertions`, exit 0; after `EXPECTED_INSTRUMENTS` floor `spec_craft 250→249`, output remains `0 failures / 165`, exit 0 (SURVIVED). The same report records analogous survival for `sibling_reread 47→46`, both floor-table copies and deletion of the expected rows. This is an observed coverage gap, not a failure of the frozen C1/C2 counters. Mutation report restoration evidence: final scratch hashes equal the captured pristine hashes for `check_assertion_floors.py` (`84458c057eef2bff8d7c76e4fdc029428688e3920deb0b69f948387433061f21`), `floors-registry.json` (`708308b01723a8ddd92298a58a1acabf0f186888220b9f1b12150cc7b32567a7`), `check_tip_battery.py` (`e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`), and `check_skill_evals_v2.py` (`d4df34cf48ba11cc6631cd1e7ef24334b634f92d1e8b54fcd6368b39e4224bfb`). The M03 evidence reports all these mutations independently reverted. I did not mutate or restore lane files.

Minimal repair: extend the guard self-test to assert that the production floor rows and constants are present and unchanged, rather than only testing synthetic fixture behavior; also assert the expected pinned digest in a test that exercises the production pin configuration. This improves operability/coverage and does not weaken depth, consistency, calibration, or freshness. No repair was made here; counters and claims remain frozen.

No-harm battery, quote reopening, and entry/row/lesson/receipt review were outside this seat's mutation probe and are not claimed as passed. No tools installed.

VERDICT: assertion-floor mutants survived their self-test; coverage finding. C1/C2 claim gates red at frozen HEAD because claim data is absent; inconclusive, not verified.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F23Mutation-TestAssertion.md