# MutCounterConj34 — round 67 wave 2

## Attack and axes

This attacks **C2's landed counter**, not the entry's prose: whether conjunct 3 (a cited row must be `mined`) and conjunct 4 (the row's complete `source` cell must occur in that id's entry `source:` line) are independently load-bearing.

Axes: targeted mutant detection (depth), honest-world calibration, and exact byte restoration. Two one-line mutants were tested sequentially, with exact restoration between them.

## Measurement identity and bounded detector

- Landed revision measured: `da86c03e482a6aef433c34d733726b37c7cf6607`.
- Pinned base `2a8eba56b3f9321b70c569fa2816d42237ca49a2` was **not** used as the honest world.
- Scratch: `/tmp/kotoba-r67-MutCounterConj34-uuyca45t`.
- The pristine counter and the three-file honest world (`ENTRY`, `SOURCES`, and `README`) were materialized with `git show <landed-rev>:<path>`. The committed counter was byte-equal to the lane worktree counter.
- The same detector ran on pristine, each mutated, and each restored counter, with a 20-second subprocess bound:

```sh
python3 -B /tmp/kotoba-r67-MutCounterConj34-uuyca45t/work.py   --repo /tmp/kotoba-r67-MutCounterConj34-uuyca45t/honest --self-test
```

Pristine SHA-256: `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`.

### Pristine baseline

Exit **0**; stderr empty; first failing line: **none**. Actual stdout:

```text
PASS honest world: grounded 1 of 1
PASS broken world rejected: entry missing
PASS broken world rejected: no source line
PASS broken world rejected: id does not resolve
PASS broken world rejected: row not mined
PASS broken world rejected: source cell absent from the entry
PASS broken world rejected: no verified-at
PASS broken world rejected: no recheck
PASS broken world rejected: no coverage-map row
PASS broken world rejected: quote not in the anchor cell
self-test: 0 failure(s) over 10 assertions
```

The baseline is conclusive: the detector itself is green before mutation.

## Mutant 1 — conjunct 3 mined-status guard

At pristine line 169, only the status guard was disabled; row lookup, row shape, and every other conjunct remained unchanged:

```diff
-        if status != "mined":
+        if False:
```

**Expected detector:** the honest world stays green, but the `row not mined` world is wrongly grounded; self-test exit 1 with first failure `FAIL broken world survived: row not mined -> grounded 1`.

**Actual output:** exit **1**. Actual stdout:

```text
PASS honest world: grounded 1 of 1
PASS broken world rejected: entry missing
PASS broken world rejected: no source line
PASS broken world rejected: id does not resolve
PASS broken world rejected: source cell absent from the entry
PASS broken world rejected: no verified-at
PASS broken world rejected: no recheck
PASS broken world rejected: no coverage-map row
PASS broken world rejected: quote not in the anchor cell
self-test: 1 failure(s) over 10 assertions
```

Actual stderr, whose first line is the requested first failing line:

```text
FAIL broken world survived: row not mined -> grounded 1
```

**Verdict: KILLED.** The detector observed the targeted non-`mined` row being accepted while the honest world and all other broken worlds retained their expected verdicts. This is not a baseline failure and not inconclusive.

## Mutant 2 — conjunct 4 source-membership guard

After restoring mutant 1 to the exact pristine bytes, only pristine line 174 was changed:

```diff
-        if row_source not in src_lines[sid]:
+        if False:
```

**Expected detector:** the honest world stays green, but the `source cell absent from the entry` world is wrongly grounded; self-test exit 1 with first failure `FAIL broken world survived: source cell absent from the entry -> grounded 1`.

**Actual output:** exit **1**. Actual stdout:

```text
PASS honest world: grounded 1 of 1
PASS broken world rejected: entry missing
PASS broken world rejected: no source line
PASS broken world rejected: id does not resolve
PASS broken world rejected: row not mined
PASS broken world rejected: no verified-at
PASS broken world rejected: no recheck
PASS broken world rejected: no coverage-map row
PASS broken world rejected: quote not in the anchor cell
self-test: 1 failure(s) over 10 assertions
```

Actual stderr, whose first line is the requested first failing line:

```text
FAIL broken world survived: source cell absent from the entry -> grounded 1
```

**Verdict: KILLED.** Only the targeted source-cell world survived in this battery; the honest world stayed green and every other broken world was still rejected.

## Restoration and honest-byte evidence

Each restoration ran the same self-test after copying the pristine bytes back over `work.py`:

| detector run | exit | first failing line | honest-world output | summary | counter SHA-256 |
|---|---:|---|---|---|---|
| pristine | 0 | none | `PASS honest world: grounded 1 of 1` | `self-test: 0 failure(s) over 10 assertions` | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` |
| conjunct-3 mutant | 1 | `FAIL broken world survived: row not mined -> grounded 1` | `PASS honest world: grounded 1 of 1` | `self-test: 1 failure(s) over 10 assertions` | `c1738b7f37fbf169446acaed0251a27e80770b76c962a7a1d1d4b8e7276099ff` |
| restored after conjunct 3 | 0 | none | `PASS honest world: grounded 1 of 1` | `self-test: 0 failure(s) over 10 assertions` | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` |
| conjunct-4 mutant | 1 | `FAIL broken world survived: source cell absent from the entry -> grounded 1` | `PASS honest world: grounded 1 of 1` | `self-test: 1 failure(s) over 10 assertions` | `6584c869744e638f7f32273e1850e8761ef17e59d6bef4c4f94c191fe53a7127` |
| restored after conjunct 4 | 0 | none | `PASS honest world: grounded 1 of 1` | `self-test: 0 failure(s) over 10 assertions` | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` |

Both restored runs had empty stderr. Before/after byte checks:

| mutation probe | before SHA-256 | mutated SHA-256 | after SHA-256 | exact restoration |
|---|---|---|---|---|
| conjunct 3 | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` | `c1738b7f37fbf169446acaed0251a27e80770b76c962a7a1d1d4b8e7276099ff` | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` | yes, byte comparison |
| conjunct 4 | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` | `6584c869744e638f7f32273e1850e8761ef17e59d6bef4c4f94c191fe53a7127` | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` | yes, byte comparison |

A final independent `cmp -s work.py pristine.py` succeeded (exit 0); both files and the lane counter hashed to the same pristine digest above. `git diff --exit-code da86c03e482a6aef433c34d733726b37c7cf6607 -- verifiers/check_instruction_authority.py` also exited 0 with no output.

Finally, the restored counter ran against the landed revision:

```sh
python3 -B /tmp/kotoba-r67-MutCounterConj34-uuyca45t/work.py   --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin   --rev da86c03e482a6aef433c34d733726b37c7cf6607
```

Exit **0**, stderr empty, actual stdout:

```text
authority ladder grounded 1 of 1
```

## Probe verdict

**Both assigned mutants are KILLED; no surviving mutant or inconclusive baseline resulted.** The honest bytes remained green during both mutation runs and after both restorations. This is evidence only for the two attacked counter conjuncts, not a judgment of the entry's prose or a license to change the contract.
