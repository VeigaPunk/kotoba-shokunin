Result: DONE — All five requested counter mutations were killed by one-clause laundering revisions; the synthetic base and its deliberate OC-4/OC-6 weakening are recorded.

# C1 counter mutation probe

All revisions and mutation copies were made in `/fast/scratch/hyaku/kotoba-r53/MutCounterC1`, cloned and checked out at the frozen plan commit. No lane source files were changed.

## Synthetic green base and scope

The all-green synthetic base is `de143bd97d754b75bfa8a7343e8b7afad6447b24`. To isolate the frozen counter's clauses before the C1 re-derivation candidate existed, it re-pins `verifiers/baseline.json` to the observed 1.19.4 SHA-256 and weakens OC-4/OC-6 in `verifiers/verify_surfaces.py` to test only `<system-reminder>` and `targets:["AGENTS.md"]` presence (scratch `verifiers/verify_surfaces.py:693-694,707-708`; `verifiers/baseline.json:10`). This is intentionally crude and is not evidence that either rule matches loader behavior. That limitation is expressly outside C1's claim (`plans/round-53.md:35-36`).

Command: `python3 -B verifiers/check_opencode_repin.py --repo /fast/scratch/hyaku/kotoba-r53/MutCounterC1 --rev de143bd97d754b75bfa8a7343e8b7afad6447b24` → exit 0.

Observed: `opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions`.

## Kill table

“Killed” means the real frozen counter rejects the single-clause laundering revision (exit 1), while that clause's mutated copy accepts it (exit 0). Each revision was run with the real counter and its corresponding one-change mutant.

| Mutation | Laundering revision | Real counter | Mutant | Killed? |
|---|---|---|---|---|
| Drop kept-class clause | `5ab52a840e841c3b993f76d61dcdb46e2bcbf495` | `kept 7/9`, exit 1 | `kept 7/9`, exit 0 | Yes |
| Drop self-test clause | `2b442d773e9c0aa361f38888271d7f52d7da0487` | `self-test 1 failure(s) over 129 assertions`, exit 1 | same output, exit 0 | Yes |
| Accept `opencode_extract` ABSENT | `3fec38d176138d8290f273ce6acf7ad04d7f5ac5` | `opencode_extract ABSENT`, exit 1 | same output, exit 0 | Yes |
| Count pin `FAIL` as `PASS` | `2822cdc68830a598692aba9655354766e7c02835` | `pins OK 2/3`, exit 1 | `pins OK 3/3`, exit 0 | Yes |
| Compare only `class_id` | `5ab52a840e841c3b993f76d61dcdb46e2bcbf495` | `classes kept 7 of 9`, exit 1 | `classes kept 9 of 9`, exit 0 | Yes |

In each row all unlisted counter fields were green: surfaces 7/7, pins 3/3, classes 9/9, and self-test 0/129, except for the single target value named in that row. For the class rows, the revision changes the `read-hook/instructions` literal to `AGENTS.md` and re-kinds `instruction-context/AGENTS.md` to `loader-config`, with matching census cells; the IDs remain present and all seven surface checks pass. This changes only the tuple checked by the kept-class condition. For self-test, the revision flips one fixture assertion's expected code at scratch `verifiers/verify_surfaces.py:1475`. For ABSENT, it aliases only the JSON output ID at scratch `verifiers/verify_surfaces.py:1666`, leaving seven PASS records. For pins, it retains the old 1.19.3 hash and maps the resulting `DRIFT` verdict to `FAIL` in that candidate's JSON serializer (`verifiers/check_substrate_pins.py:265-266`) so the exact requested FAIL-as-PASS mutant is exercised.

### Actual counter output lines

The following are the observed first output lines; all had the same second line: `substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032`.

```text
kept-class real (1): opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 7 of 9; self-test 0 failure(s) over 129 assertions
kept-class mutant (0): opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 7 of 9; self-test 0 failure(s) over 129 assertions
self-test real (1): opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 1 failure(s) over 129 assertions
self-test mutant (0): opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 1 failure(s) over 129 assertions
ABSENT real (1): opencode re-pin: surfaces pass 7 of 7 (opencode_extract ABSENT); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions
ABSENT mutant (0): opencode re-pin: surfaces pass 7 of 7 (opencode_extract ABSENT); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions
pin FAIL real (1): opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions
pin FAIL mutant (0): opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions
class_id-only real (1): opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 7 of 9; self-test 0 failure(s) over 129 assertions
class_id-only mutant (0): opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions
```

### Mutation and restoration hashes

Each probe copied the pristine counter (`verifiers/check_opencode_repin.py`) before mutation, ran the pristine copy, ran the one-change mutant, restored the copy from the pristine bytes, then reran it. The pristine hash before each probe and the restored hash afterward were both `9abcaa12fb41563a44517fdbcac773fb54aebb79f4334d317277b6e783ca4fbd`.

| Mutant copy | Mutated SHA-256 | Restored SHA-256 |
|---|---|---|
| `mutants/drop_kept.py` | `44c1a6ad4de66a5a0d73944b9315dbc7bdbf2e7f7b19de910388782aaf8c9373` | `9abcaa12fb41563a44517fdbcac773fb54aebb79f4334d317277b6e783ca4fbd` |
| `mutants/drop_selftest.py` | `5ac67a0acb7747f7045f1841e9e8986cd13798abb5989b2f3ff27819b7969aec` | `9abcaa12fb41563a44517fdbcac773fb54aebb79f4334d317277b6e783ca4fbd` |
| `mutants/accept_absent.py` | `eff36dcdc2e6748e293a6f83e550f14b99f24799ce7b153f6486a000cc9590db` | `9abcaa12fb41563a44517fdbcac773fb54aebb79f4334d317277b6e783ca4fbd` |
| `mutants/fail_as_pass.py` | `457bd49e8453c94b2afd948271ef077d3bf704100f7716bf6e9fe840bc174cdd` | `9abcaa12fb41563a44517fdbcac773fb54aebb79f4334d317277b6e783ca4fbd` |
| `mutants/class_id_only.py` | `b88a6c321684537acc014c4e3799501d8d24e5ca466c739205b99487f2cc0782` | `9abcaa12fb41563a44517fdbcac773fb54aebb79f4334d317277b6e783ca4fbd` |

Final `sha256sum` observed the pristine counter and all five restored copies at the same `9abcaa12fb41563a44517fdbcac773fb54aebb79f4334d317277b6e783ca4fbd` hash.

### Pin verdict note

A preliminary stale-hash candidate, `5ca7d6e091c841741a736fa545f973bba8939033`, emitted `DRIFT`, not `FAIL`; `check_substrate_pins.py:116-124` defines `DRIFT` as its mismatch verdict. On that candidate the requested `("PASS", "FAIL")` mutant still reported 2/3 and exited 1, so it did not exercise the specified mutation. The probe was restored, then the final pin candidate normalized only the JSON verdict to `FAIL`; raw JSON confirmed one FAIL and two PASS, and the requested mutant changed the count to 3/3. No tool was installed or updated.