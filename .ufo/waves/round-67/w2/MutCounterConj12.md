# MutCounterConj12 — mutation probe of C2 conjuncts 1 and 2

## Attack and measured object

- **Attacks:** the landed C2 counter's conjunct 1 entry-existence guard and conjunct 2 `source:`/`S###` guard. Each was challenged independently by the smallest behavior-bearing inversion: deleting only the token `not ` from that guard.
- **Measured committed tree:** `da86c03e482a6aef433c34d733726b37c7cf6607` (landed tip), read through the counter's `--rev` machinery. This is not the pinned base.
- **Counter under mutation:** a scratch copy of `verifiers/check_instruction_authority.py`; no lane source was mutated.
- **Sandbox:** `/tmp/k67-mut-counter-conj12-40ge_2q9`.
- **Bounded detector (same for pristine, each mutant, and each restoration):**
  `python3 -B /tmp/k67-mut-counter-conj12-40ge_2q9/counter.py --rev da86c03e482a6aef433c34d733726b37c7cf6607 --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin`
  Each child had a 20 s timeout; runs were sequential so only one mutant existed at a time.
- The lane counter and the counter bytes at the landed commit matched before the probe: SHA-256 `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`.

## Pristine control

Expected: exit 0 and `authority ladder grounded 1 of 1`. Actual: exit **0**, stderr empty.

```text
authority ladder grounded 1 of 1
```

The baseline passed, so the mutant results below are conclusive rather than baseline-failure inconclusive.

## M1 — conjunct 1: entry must exist

**Mutant (one site, one token deleted):**

```diff
-    if not entry_path.is_file():
+    if entry_path.is_file():
```

- Before SHA-256: `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`
- Mutated SHA-256: `002b767b67cdb3fc51a5fa97ce80afc442102a3b232b3c6609d88dba950b05e4`
- Single-site check: reversing only this replacement reproduces the pristine bytes (`changed_bytes_only_at_site=true`).
- **Expected detector:** the committed entry exists, so the inverted guard must return not-grounded: nonzero exit, no `authority ladder grounded 1 of 1`, and the entry-missing diagnostic.
- **Actual exit:** **1**; stderr empty; success line present: **false**.
- **First failing line (first output line):** `authority ladder grounded 0 of 1`
- **First finding line:** `  - entry missing: corpus/knowledge/instruction-authority-ladder-round67.md`

```text
authority ladder grounded 0 of 1
  - entry missing: corpus/knowledge/instruction-authority-ladder-round67.md
```

**Verdict: KILLED.** The valid committed-tip detector rejected the mutant with the required conjunct-1 refusal and diagnostic.

### Restoration after M1

- Before/expected SHA-256: `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`
- After/actual SHA-256: `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`
- Exact original bytes restored: **true**; independent pristine-copy comparison: **true**.
- Restored-byte detector rerun: exit **0**, success line present: **true**.

```text
authority ladder grounded 1 of 1
```

## M2 — conjunct 2: entry must carry a `source:` line naming an `S###` id

M1 was restored before this mutant was introduced.

**Mutant (one site, one token deleted):**

```diff
-    if not src_lines:
+    if src_lines:
```

- Before SHA-256: `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`
- Mutated SHA-256: `94c10f1cd33e792361d71b944500da91e6929f20e7f47fe7754b756e7cc2e869`
- Single-site check: reversing only this replacement reproduces the pristine bytes (`changed_bytes_only_at_site=true`).
- **Expected detector:** the committed entry has parsed source lines, so the inverted guard must return not-grounded: nonzero exit, no `authority ladder grounded 1 of 1`, and the no-source-line diagnostic.
- **Actual exit:** **1**; stderr empty; success line present: **false**.
- **First failing line (first output line):** `authority ladder grounded 0 of 1`
- **First finding line:** `  - no `source:` line naming an S### id`

```text
authority ladder grounded 0 of 1
  - no `source:` line naming an S### id
```

**Verdict: KILLED.** The valid committed-tip detector rejected the mutant with the required conjunct-2 refusal and diagnostic.

### Restoration after M2

- Before/expected SHA-256: `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`
- After/actual SHA-256: `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212`
- Exact original bytes restored: **true**; independent pristine-copy comparison: **true**.
- Restored-byte detector rerun: exit **0**, success line present: **true**.

```text
authority ladder grounded 1 of 1
```

## Final integrity and verdict

| Evidence | SHA-256 / result |
|---|---|
| Lane counter before | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` |
| Committed counter at measured tip | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` |
| Scratch counter after final restoration | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` |
| Lane counter after | `e4f50ca466d19f6297d8f7a66ac90268ee7da7324ff2483fda8f30ebc43a3212` |
| Final scratch bytes exactly pristine | **true** |
| Lane bytes unchanged | **true** |

**Local mutation verdict: 2 killed, 0 survived, 0 inconclusive.** Both required mutants refused to print the success line and exited 1; pristine and restored honest bytes stayed green. This is only the assigned detector-sensitivity probe, not a judgement of C2 or a contract change.

Raw per-run stdout, stderr, exit codes, and hashes are retained under `/tmp/k67-mut-counter-conj12-40ge_2q9` (`results.json` plus per-case files). No tools were installed or upgraded.
