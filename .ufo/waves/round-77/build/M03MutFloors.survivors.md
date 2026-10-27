# M03MutFloors — instrumentation mutation findings

Scratch clone base: `6523aced1ee0ebe07dca996213bdc645a6acbd1e`. Detector was each target verifier's bounded `python3 -B verifiers/<file> --self-test`. Pristine baselines all passed: floors guard `0 failure(s) over 165 assertions` (exit 0); tip battery `self-test: 0 failure(s) over 69 assertions` (exit 0); skill-evals `self-test: 0 failure(s)` (exit 0; included the positive exact multi-member arm and negative substring/negation arms).

| # | Mutant | Detector result | Verdict |
|---:|---|---|---|
| 1 | EXPECTED_INSTRUMENTS spec_craft floor 250→249 | 0 failures / 165, exit 0 | SURVIVED |
| 2 | EXPECTED_INSTRUMENTS sibling_reread floor 47→46 | 0 failures / 165, exit 0 | SURVIVED |
| 3 | registry spec_craft floor 250→249 | 0 failures / 165, exit 0 | SURVIVED |
| 4 | registry sibling_reread floor 47→46 | 0 failures / 165, exit 0 | SURVIVED |
| 5 | INSTRUMENTS spec_craft floor 250→249 | 0 failures / 165, exit 0 | SURVIVED |
| 6 | INSTRUMENTS sibling_reread floor 47→46 | 0 failures / 165, exit 0 | SURVIVED |
| 7–10 | assertion-floors pin digest byte changed at offsets 0, 1, 2, 3 | each 0 failures / 69, exit 0 | SURVIVED (all four) |
| 11 | remove assertion-floors pin declaration | SyntaxError line 127, exit 1 | KILLED, but malformed mutant (not informative) |
| 12 | used-by test accepts raw substring | 2 failures, exit 1 | KILLED |
| 13 | remove negation exclusion from accepted SKILL lines | 2 failures, exit 1 | KILLED |
| 14 | used-by accepts substring via `any(ENTRY in p ...)` | 2 failures, exit 1 | KILLED |
| 15 | case-folded raw substring used-by check | 2 failures, exit 1 | KILLED |
| 16 | bypass negation filter | 2 failures, exit 1 | KILLED |
| 17 | relax exactly-one-good-line check to at-least-one | 1 failure, exit 1 | KILLED |
| 18 | delete EXPECTED spec_craft row | 0 failures / 165, exit 0 | SURVIVED |
| 19 | delete EXPECTED sibling_reread row | 0 failures / 165, exit 0 | SURVIVED |
| 20–21 | delete registry spec_craft/sibling_reread row opener | JSON parse error, exit 1 | KILLED, malformed mutant (not informative) |

**Coverage findings.** The floors guard self-test does not assert that the D4 floors themselves remain 250 and 47, nor that those rows are present in each source table: lowering/removing them from `EXPECTED_INSTRUMENTS` survives the self-test. Its `--self-test` executes fixture-world checks, not the live `main()` instrument walk; running it against a mutant's self-test code therefore does not test the live floor policy. Likewise, tip-battery `--self-test` starts by setting global `INSTRUMENT_PINS = {}` and exercises a synthetic pin map; it never asserts the production assertion-floors blob digest. Thus any changed pin byte survives the self-test. This is the exact self-test gap for these instrumentation edits. The existing skill-evals self-test does cover both intended distinctions: a valid comma-separated exact multi-entry member is accepted, while substring and negated forms fail.

Mutant count: 21. Informative surviving mutants: 12 (six floor changes/deletions in guard tables and six pin-byte changes); killed: 7 informative predicate cases (used-by/negation); malformed mutants: 3 (pin removal and two malformed registry row deletions). No counter source was changed in the lane.

Restoration: each mutation was independently reverted to captured original bytes immediately after its detector. Scratch pre-mutation and final SHA-256 values were identical:
- `verifiers/check_assertion_floors.py`: `84458c057eef2bff8d7c76e4fdc029428688e3920deb0b69f948387433061f21`
- `verifiers/floors-registry.json`: `708308b01723a8ddd92298a58a1acabf0f186888220b9f1b12150cc7b32567a7`
- `verifiers/check_tip_battery.py`: `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`
- `verifiers/check_skill_evals_v2.py`: `d4df34cf48ba11cc6631cd1e7ef24334b634f92d1e8b54fcd6368b39e4224bfb`

Commands exercised in the scratch clone: `python3 -B verifiers/check_assertion_floors.py --self-test`; `python3 -B verifiers/check_tip_battery.py --self-test`; `python3 -B verifiers/check_skill_evals_v2.py --self-test`. Each actual exit code is recorded above. No tools installed.