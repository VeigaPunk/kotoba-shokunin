# MutCounterPrint — round 67 wave 2

## Attack and verdict

**Attacked invariant:** the landed C2 counter's `--self-test` catches mutations to the public
output contract: the exact `authority ladder grounded N of 1` line, a truthful `N`, and exit 1
on a not-grounded world.

**Verdict: 0 killed / 3 survived / 0 inconclusive.** The pristine self-test passed, and every
mutant also passed it with `0 failure(s)` and exit 0. The expected output-contract detection did
not occur. This is a self-test coverage finding; it does not change the frozen counter contract.

The concrete defect is visible in `verifiers/check_instruction_authority.py`: `selftest()` calls
`check(base)` at line 234 and `check(world)` at line 263. It never calls `main()`, captures its
stdout, or checks its exit status. Thus the mutated line 292 and return line 295 are outside the
self-test's execution path, despite the line-221 docstring saying that it drives public `main()`.

## Measurement identity and isolation

- Landed tip / counter-byte identity: `da86c03e482a6aef433c34d733726b37c7cf6607`.
- Pinned base: `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. It was not supplied to this
  self-test probe: `--self-test` defines its honest world as the working tree passed by `--repo`.
- Original counter: `verifiers/check_instruction_authority.py`, SHA-256
  `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`.
- Isolated scratch copy:
  `/tmp/k67-mut-counter-print.ZMsaFq/verifiers/check_instruction_authority.py`.
- Pristine scratch snapshot: `/tmp/k67-mut-counter-print.ZMsaFq/pristine.py`.
- No lane tracked file, Git index, or jj state was mutated. No tools were installed.

The bounded detector, unchanged for pristine, mutated, and restored bytes, was:

```sh
python3 -B /tmp/k67-mut-counter-print.ZMsaFq/verifiers/check_instruction_authority.py \
  --self-test --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin
```

Supplementary direct-`main()` probes used scratch worlds under
`/tmp/k67-mut-counter-print.ZMsaFq/`: `honest-world` contains the three working-tree input files;
`broken-world` is the same copy with the entry deleted. These probes demonstrate that each mutant
actually changed its targeted public behavior; the kill verdicts below come only from the common
`--self-test` detector.

## Pristine baseline

Self-test output (exit 0):

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
SELF_TEST_EXIT=0
```

Direct pristine control:

```text
PRISTINE_MAIN honest-world
authority ladder grounded 1 of 1
MAIN_EXIT=0
PRISTINE_MAIN broken-world
authority ladder grounded 0 of 1
  - entry missing: corpus/knowledge/instruction-authority-ladder-round67.md
MAIN_EXIT=1
```

Baseline SHA-256:
`e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`.

## M1 — rename the public output line

**Mutant (only line 292):**

```diff
-print(f"authority ladder grounded {n} of {TOTAL}")
+print(f"authority ladder verdict {n} of {TOTAL}")
```

- Mutated SHA-256: `4036d18d6dcb075d70bc6551f39c5d09e003ea86e0d0b00136a474157e2bd52f`.
- Expected detector: exact-line assertion fails; self-test exits 1.
- Actual self-test output (exit 0):

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
SELF_TEST_EXIT=0
```

- **Verdict: SURVIVED.** Direct public-output evidence:

```text
M1_MAIN honest-world
authority ladder verdict 1 of 1
MAIN_EXIT=0
M1_MAIN broken-world
authority ladder verdict 0 of 1
  - entry missing: corpus/knowledge/instruction-authority-ladder-round67.md
MAIN_EXIT=1
```

- Restoration after M1: SHA-256 returned to
  `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`;
  bytewise `cmp` against pristine returned `RESTORE_CMP_EXIT=0`.

## M2 — always print `1 of 1`, independent of findings

**Mutant (only line 292; return logic left intact):**

```diff
-print(f"authority ladder grounded {n} of {TOTAL}")
+print(f"authority ladder grounded 1 of {TOTAL}")
```

- Mutated SHA-256: `4b5871aadb161cd4f9c0ebdf3465ba24278e9ba3985d5f335041a494822c4d7b`.
- Expected detector: the broken-world exact-line assertion fails (it must print `0 of 1`);
  self-test exits 1.
- Actual self-test output (exit 0):

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
SELF_TEST_EXIT=0
```

- **Verdict: SURVIVED.** Direct public-output evidence (the honest and broken worlds both print
  `1 of 1`, while the broken world still exits 1):

```text
M2_MAIN honest-world
authority ladder grounded 1 of 1
MAIN_EXIT=0
M2_MAIN broken-world
authority ladder grounded 1 of 1
  - entry missing: corpus/knowledge/instruction-authority-ladder-round67.md
MAIN_EXIT=1
```

- Restoration after M2: SHA-256 returned to
  `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`;
  bytewise `cmp` against pristine returned `RESTORE_CMP_EXIT=0`.

## M3 — exit 0 on a not-grounded world

**Mutant (only line 295):**

```diff
-return 0 if n == TOTAL else 1
+return 0
```

- Mutated SHA-256: `c3bc75436cff68b634fb3caf5417b518a305aa587ff580696c331d46b2ab0e4a`.
- Expected detector: broken-world exit-status assertion fails; self-test exits 1.
- Actual self-test output (exit 0):

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
SELF_TEST_EXIT=0
```

- **Verdict: SURVIVED.** Direct public-exit evidence:

```text
M3_MAIN honest-world
authority ladder grounded 1 of 1
MAIN_EXIT=0
M3_MAIN broken-world
authority ladder grounded 0 of 1
  - entry missing: corpus/knowledge/instruction-authority-ladder-round67.md
MAIN_EXIT=0
```

- Restoration after M3: restored to the pristine bytes before the final detector run; evidence
  below.

## Final restoration and restored-byte detector

After M3, the working scratch counter was copied from the pristine snapshot and the same bounded
self-test was rerun. Output (exit 0):

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
SELF_TEST_EXIT=0
```

Final hashes:

```text
e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212  /tmp/k67-mut-counter-print.ZMsaFq/pristine.py
e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212  /tmp/k67-mut-counter-print.ZMsaFq/verifiers/check_instruction_authority.py
e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_instruction_authority.py
SCRATCH_RESTORE_CMP_EXIT=0
LANE_UNCHANGED_CMP_EXIT=0
```

`git status --short -- verifiers/check_instruction_authority.py` printed nothing. All three
mutants were confined to scratch and exact pristine bytes were restored after every probe.
