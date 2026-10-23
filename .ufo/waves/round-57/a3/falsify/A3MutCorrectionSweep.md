Result: DONE — Eleven isolated mutants covered all three round-57 registry rows, their declared-pattern weakening, the seed addition and all four new self-test arms; four were killed and seven survived, with exact restoration after every mutant.

# Scope and detector

Axis under test: consistency. This is a mutation-probe result, not a round-admission judgment. Lane code was read only; only this seat's isolated verifier copy was mutated. No frozen counter or sibling scratch copy was edited. No untrusted earlier-attempt evidence was used. No fix is proposed or integrated.

Assigned content revision: `07c33d73ddce769d9cea2846a6313164401b5478`. The read-only lane diff against `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a` added registry rows at `verifiers/check_correction_sweep.py:74–79`, one SEEDED entry at line 89 and four case calls at lines 225–233. Each registry row was probed twice, independently: deletion and a weakened declared pattern. The seed entry and each new case call were deleted once. No two defects were active together.

All executions used `/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep`, cloned from the lane and checked out at the assigned revision. Sandbox creation used the following commands; both exited 0 with no output:

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

The same two commands were run on pristine, mutated and restored bytes for EVERY mutant, sequentially (66 bounded detector invocations total):

```sh
# S
timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test
# R
timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478
```

Environment: GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE unset; `TMPDIR=/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/mutation-tmp`; `PYTHONDONTWRITEBYTECODE=1`. A subprocess-level 125-second ceiling also guarded each `timeout 120` command. No command timed out. The temporary directory was removed after the final restored runs (`timeout 30 rmdir mutation-tmp`, exit 0). No sandbox commit was created.

Expected detector: S is the behavioral canary for row removal and seeded red/green cases; R executes the working-tree (possibly mutated) verifier against pinned committed CONTENT and serves as the existing-content control. R alone is not a negative fixture. Survival below means both supplied commands exited 0. It does not mean byte-identical stdout: dropped-case mutants visibly lower the assertion count to 17, but the command does not reject that reduction. No extra frozen-count detector was added.

Every pristine/restored S run exited 0 with exactly `0 failure(s) over 18 assertions\n`; every pristine/restored R run exited 0 with exactly `correction sweep: 0 stale block(s)\n`. All those stderr streams were empty. Consequently no baseline failure was counted as a kill; there were zero inconclusive mutants. All eleven mutated R runs also exited 0 with the same R output.

UTC wall-clock command after the probes (`timeout 30 date -u`, exit 0):

```text
Fri 23 Oct 2026 06:50:18 AM UTC
```

No live source fetch was needed for this source-code mutation assignment. No tool was installed or updated.

# Mutant | killed by | survived

| Mutant (original verifier line) | Killed by | Survived |
|---|---|---|
| M01-delete-s076-row: Delete S076 registry row (74–75) | S: exit 1; `r57 quote notes red` loses the S076 id | No |
| M02-delete-s078-row: Delete S078 registry row (76–77) | S: exit 1; `r57 quote notes red` loses the S078 id | No |
| M03-delete-singular-row: Delete singular-agent registry row (78–79) | S: exit 1; `r57 singular agent clause red` gets no id | No |
| M04-weaken-s076-declared: S076 declaration: `Round-57 correction` → `Round-57` (75) | None: S/R both exit 0; S still reports 18 assertions | Yes |
| M05-weaken-s078-declared: S078 declaration: `Round-57 correction` → `Round-57` (77) | None: S/R both exit 0; S still reports 18 assertions | Yes |
| M06-weaken-singular-declared: Singular declaration: remove `:486` from the pattern (79) | None: S/R both exit 0; S still reports 18 assertions | Yes |
| M07-drop-seeded-entry: Drop the round-57 SEEDED entry (89) | S: exit 1; missing-file RuntimeError in the first fixture | No |
| M08-drop-quote-notes-red-arm: Drop `r57 quote notes red` case (225–226) | None: S/R both exit 0; S drops from 18 to 17 assertions | Yes |
| M09-drop-quote-notes-green-arm: Drop `r57 quote notes green` case (227–228) | None: S/R both exit 0; S drops from 18 to 17 assertions | Yes |
| M10-drop-singular-red-arm: Drop `r57 singular agent clause red` case (229–231) | None: S/R both exit 0; S drops from 18 to 17 assertions | Yes |
| M11-drop-singular-green-arm: Drop `r57 singular agent clause green` case (232–233) | None: S/R both exit 0; S drops from 18 to 17 assertions | Yes |

Four kills: M01–M03 by failed expected-id assertions; M07 by an uncaught missing-file error. Seven survivors: three weakened-declaration mutants and four dropped-case mutants. R killed none.

# What each survivor lets through

The following input examples are **[INFERENCE] from the changed regex and the existing sweep at lines 116–130**, not additional executed fixtures. The actual executed evidence is the two supplied commands in the receipt section.

- **M04:** lets the S076 stale assertion coexist with a bare round label, without the required correction marker. Example block: `S076's project line holds no agent word. Round-57.` The red fixture has no round label and the green fixture has the complete marker, so neither distinguishes the weakened requirement.
- **M05:** the corresponding S078 hole. Example block: `S078's quote is the body of a fenced example. Round-57.` A bare label would satisfy the mutant without `Round-57 correction`.
- **M06:** lets the singular-agent claim carry any `migrate-v1.mdx` reference without the pinned `:486`. A block containing the exact stale phrase and `migrate-v1.mdx:999` would satisfy the mutant. Existing red has no reference and existing green has the full reference, so the weakened citation requirement is not distinguished.
- **M08:** lets a self-test with the entire quote-notes negative case removed exit 0. It removes the dedicated rejection test for BOTH S076 and S078 stale notes without corrections. The mutation itself does not change production sweep behavior; [INFERENCE] a later loss of either row's rejection behavior could escape the remaining round-57 fixtures.
- **M09:** lets a self-test with the quote-notes positive case removed exit 0. It loses the dedicated evidence that same-block `Round-57 correction` is accepted. Production sweep behavior is unchanged by this mutant; [INFERENCE] false-positive regressions lose that fixture's protection.
- **M10:** lets a self-test with the singular-agent negative case removed exit 0. It loses the dedicated test that the stale singular-agent clause without the declaration is rejected. Production sweep behavior is unchanged; [INFERENCE] later loss of that rejection could escape the remaining round-57 fixtures.
- **M11:** lets a self-test with the singular-agent positive case removed exit 0. It loses the dedicated acceptance test for the exact `migrate-v1.mdx:486` citation. Production sweep behavior is unchanged; [INFERENCE] false-positive regressions lose that fixture's protection.

These are coverage findings, not permission to weaken the original requirements. The four dropped-case mutants have an observable 18→17 count delta; all three weakened-pattern survivors retain the identical 18-assertion output.

# Exact mutations (old → new)

Locations refer to the committed original `verifiers/check_correction_sweep.py`. Only the displayed block changed in each independent mutant. Each code block includes its trailing newline. “Empty” means deletion, not a replacement comment or placeholder. These are defect descriptions, not proposed fixes.

## M01-delete-s076-row — original line(s) 74–75

Old:

```python
    {"id": "r57-r2-s076-note", "file": "corpus/knowledge/agent-definition-files-round56.md",
     "stale": r"holds no agent word", "declared": r"Round-57 correction", "lead": False},
```

New:

Empty (block deleted).

## M02-delete-s078-row — original line(s) 76–77

Old:

```python
    {"id": "r57-r2-s078-note", "file": "corpus/knowledge/agent-definition-files-round56.md",
     "stale": r"body of a fenced example", "declared": r"Round-57 correction", "lead": False},
```

New:

Empty (block deleted).

## M03-delete-singular-row — original line(s) 78–79

Old:

```python
    {"id": "r57-r2-skill-singular-agent", "file": "SKILL.md",
     "stale": r"singular `agent/` still loads", "declared": r"migrate-v1\.mdx:486", "lead": False},
```

New:

Empty (block deleted).

## M04-weaken-s076-declared — original line(s) 75

Old:

```python
     "stale": r"holds no agent word", "declared": r"Round-57 correction", "lead": False},
```

New:

```python
     "stale": r"holds no agent word", "declared": r"Round-57", "lead": False},
```

## M05-weaken-s078-declared — original line(s) 77

Old:

```python
     "stale": r"body of a fenced example", "declared": r"Round-57 correction", "lead": False},
```

New:

```python
     "stale": r"body of a fenced example", "declared": r"Round-57", "lead": False},
```

## M06-weaken-singular-declared — original line(s) 79

Old:

```python
     "stale": r"singular `agent/` still loads", "declared": r"migrate-v1\.mdx:486", "lead": False},
```

New:

```python
     "stale": r"singular `agent/` still loads", "declared": r"migrate-v1\.mdx", "lead": False},
```

## M07-drop-seeded-entry — original line(s) 89

Old:

```python
    "corpus/knowledge/agent-definition-files-round56.md",
```

New:

Empty (block deleted).

## M08-drop-quote-notes-red-arm — original line(s) 225–226

Old:

```python
    case("r57 quote notes red", "- x\n", "| d | 9 | x |\n",
         ["r57-r2-s076-note", "r57-r2-s078-note"], seed={ent: stale_e})
```

New:

Empty (block deleted).

## M09-drop-quote-notes-green-arm — original line(s) 227–228

Old:

```python
    case("r57 quote notes green", "- x\n", "| d | 9 | x |\n", [],
         seed={ent: stale_e.rstrip("\n") + " Round-57 correction (R2): see the lesson.\n"})
```

New:

Empty (block deleted).

## M10-drop-singular-red-arm — original line(s) 229–231

Old:

```python
    case("r57 singular agent clause red", "- x\n", "| d | 9 | x |\n",
         ["r57-r2-skill-singular-agent"],
         skill="| opencode | `.opencode/agents` (singular `agent/` still loads per a docs commit) |\n")
```

New:

Empty (block deleted).

## M11-drop-singular-green-arm — original line(s) 232–233

Old:

```python
    case("r57 singular agent clause green", "- x\n", "| d | 9 | x |\n", [],
         skill="| opencode | singular `agent/` still loads (`migrate-v1.mdx:486`) |\n")
```

New:

Empty (block deleted).

# Mutated command outputs

For each entry, R exited 0, stdout was `correction sweep: 0 stale block(s)\n`, stderr empty. S outputs follow verbatim; all S stderr streams were empty except M07, whose full traceback is preserved.

## M01-delete-s076-row — S exit 1

stdout:

```text
1 failure(s) over 18 assertions
FAIL r57 quote notes red: got ['r57-r2-s078-note corpus/knowledge/agent-definition-files-round56.md:1 stale claim without the declared result']
```

## M02-delete-s078-row — S exit 1

stdout:

```text
1 failure(s) over 18 assertions
FAIL r57 quote notes red: got ['r57-r2-s076-note corpus/knowledge/agent-definition-files-round56.md:1 stale claim without the declared result']
```

## M03-delete-singular-row — S exit 1

stdout:

```text
1 failure(s) over 18 assertions
FAIL r57 singular agent clause red: got []
```

## M04-weaken-s076-declared — S exit 0

stdout:

```text
0 failure(s) over 18 assertions
```

## M05-weaken-s078-declared — S exit 0

stdout:

```text
0 failure(s) over 18 assertions
```

## M06-weaken-singular-declared — S exit 0

stdout:

```text
0 failure(s) over 18 assertions
```

## M07-drop-seeded-entry — S exit 1

stdout:

Empty.

stderr:

```text
Traceback (most recent call last):
  File "/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py", line 306, in <module>
    sys.exit(main())
             ~~~~^^
  File "/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py", line 291, in main
    return self_test()
  File "/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py", line 194, in self_test
    case("red both", stale_r, stale_s, ["r51-c2-readme", "r51-c2-scorecard-lead"])
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py", line 184, in case
    got = sweep(reader(None, t))
  File "/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py", line 120, in sweep
    raise RuntimeError("missing %s" % e["file"])
RuntimeError: missing corpus/knowledge/agent-definition-files-round56.md
```

## M08-drop-quote-notes-red-arm — S exit 0

stdout:

```text
0 failure(s) over 17 assertions
```

## M09-drop-quote-notes-green-arm — S exit 0

stdout:

```text
0 failure(s) over 17 assertions
```

## M10-drop-singular-red-arm — S exit 0

stdout:

```text
0 failure(s) over 17 assertions
```

## M11-drop-singular-green-arm — S exit 0

stdout:

```text
0 failure(s) over 17 assertions
```

# Exact-byte restoration evidence

Original SHA-256 (also printed by `timeout 30 sha256sum verifiers/check_correction_sweep.py`, exit 0):

```text
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
```

Let **P** = `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18`. The table records the hash before AND after BOTH S and R in each phase. Every mutated phase had one distinct non-P hash; all runs in that phase retained it. Every pristine and restored phase had P before and after both commands. Restoration was performed before the next mutant; even M07's failing self-test was followed by exact restoration and both restored detectors.

| Mutant | Pristine before/after S,R | Mutated before/after S,R (SHA-256) | Restored before/after S,R |
|---|---|---|---|
| M01-delete-s076-row | P → P | `153d14a5e9c6403c908f24b3dd6aeabb72aa64c1f90b82965d067e903ca91b0d` → same | P → P |
| M02-delete-s078-row | P → P | `a852c6fe57d9c55aa304bb847f7286ed6061b19daf0f8c66818aa4b55a999d18` → same | P → P |
| M03-delete-singular-row | P → P | `4369d598c4e006aa0a2e558d608db6994bcdf9ae2bf312ec7a74a393f0ad9f89` → same | P → P |
| M04-weaken-s076-declared | P → P | `1e508d098cf930e2373e3949145405bd62a51d7d325418e5353e2b2ea021ddf6` → same | P → P |
| M05-weaken-s078-declared | P → P | `f24014d48b236fb6653293224ee914de274450b0e1d4d7174c97a4ec4bc1d7d6` → same | P → P |
| M06-weaken-singular-declared | P → P | `5fb6ff20cb630d330c5b5fc40891080c56a0a3ead160bf08f26839fb334edea7` → same | P → P |
| M07-drop-seeded-entry | P → P | `4f455dd8404aa0d96580f4e93cb8873c51dda33eb51a965ceb4fd66dfbf7972d` → same | P → P |
| M08-drop-quote-notes-red-arm | P → P | `ca454494649d5ba9b4d03eec08278ac95931c3fc4442183840a4f947a048959c` → same | P → P |
| M09-drop-quote-notes-green-arm | P → P | `c88e95d4a17f1998cefe4951347ef4eaf53747cb4363ce6cc64a35e06e76eb24` → same | P → P |
| M10-drop-singular-red-arm | P → P | `d7bbc8a280e1dde8187da9c427a88cc13a72f6f90aed9563b7ea09997ee96048` → same | P → P |
| M11-drop-singular-green-arm | P → P | `7a06fd21777538338b21c2dc3426b01e551a88709dc4ba7e2f1735aebea7c729` → same | P → P |

The final two restored runs (M11) exited 0 with 18 assertions / zero stale blocks and hash P before and after both commands. No mutation remains in the scratch verifier. The lane verifier was never written.

# Full execution receipt

One JSON object per invocation, in actual execution order. Includes the exact command, UTC start, exit code, stdout, stderr and before/after source hashes. These are captured outputs, not predicted outputs. All paths are inside this seat's sandbox; there is no evidence from an earlier attempt.

```jsonl
{"mutant":"M01-delete-s076-row","phase":"pristine","utc":"2026-10-23T06:47:24.243294+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1288}
{"mutant":"M01-delete-s076-row","phase":"pristine","utc":"2026-10-23T06:47:24.372163+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0496}
{"mutant":"M01-delete-s076-row","phase":"mutated","utc":"2026-10-23T06:47:32.313721+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":1,"stdout":"1 failure(s) over 18 assertions\nFAIL r57 quote notes red: got ['r57-r2-s078-note corpus/knowledge/agent-definition-files-round56.md:1 stale claim without the declared result']\n","stderr":"","sha256_before":"153d14a5e9c6403c908f24b3dd6aeabb72aa64c1f90b82965d067e903ca91b0d","sha256_after":"153d14a5e9c6403c908f24b3dd6aeabb72aa64c1f90b82965d067e903ca91b0d","elapsed_seconds":0.117}
{"mutant":"M01-delete-s076-row","phase":"mutated","utc":"2026-10-23T06:47:32.430723+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"153d14a5e9c6403c908f24b3dd6aeabb72aa64c1f90b82965d067e903ca91b0d","sha256_after":"153d14a5e9c6403c908f24b3dd6aeabb72aa64c1f90b82965d067e903ca91b0d","elapsed_seconds":0.0455}
{"mutant":"M01-delete-s076-row","phase":"restored","utc":"2026-10-23T06:47:37.633684+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1266}
{"mutant":"M01-delete-s076-row","phase":"restored","utc":"2026-10-23T06:47:37.760330+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0447}
{"mutant":"M02-delete-s078-row","phase":"pristine","utc":"2026-10-23T06:47:37.805064+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1251}
{"mutant":"M02-delete-s078-row","phase":"pristine","utc":"2026-10-23T06:47:37.930218+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0434}
{"mutant":"M02-delete-s078-row","phase":"mutated","utc":"2026-10-23T06:47:43.643018+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":1,"stdout":"1 failure(s) over 18 assertions\nFAIL r57 quote notes red: got ['r57-r2-s076-note corpus/knowledge/agent-definition-files-round56.md:1 stale claim without the declared result']\n","stderr":"","sha256_before":"a852c6fe57d9c55aa304bb847f7286ed6061b19daf0f8c66818aa4b55a999d18","sha256_after":"a852c6fe57d9c55aa304bb847f7286ed6061b19daf0f8c66818aa4b55a999d18","elapsed_seconds":0.1165}
{"mutant":"M02-delete-s078-row","phase":"mutated","utc":"2026-10-23T06:47:43.759536+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"a852c6fe57d9c55aa304bb847f7286ed6061b19daf0f8c66818aa4b55a999d18","sha256_after":"a852c6fe57d9c55aa304bb847f7286ed6061b19daf0f8c66818aa4b55a999d18","elapsed_seconds":0.0471}
{"mutant":"M02-delete-s078-row","phase":"restored","utc":"2026-10-23T06:47:48.876583+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1342}
{"mutant":"M02-delete-s078-row","phase":"restored","utc":"2026-10-23T06:47:49.010805+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0508}
{"mutant":"M03-delete-singular-row","phase":"pristine","utc":"2026-10-23T06:47:49.061729+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1378}
{"mutant":"M03-delete-singular-row","phase":"pristine","utc":"2026-10-23T06:47:49.199593+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0592}
{"mutant":"M03-delete-singular-row","phase":"mutated","utc":"2026-10-23T06:47:59.082050+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":1,"stdout":"1 failure(s) over 18 assertions\nFAIL r57 singular agent clause red: got []\n","stderr":"","sha256_before":"4369d598c4e006aa0a2e558d608db6994bcdf9ae2bf312ec7a74a393f0ad9f89","sha256_after":"4369d598c4e006aa0a2e558d608db6994bcdf9ae2bf312ec7a74a393f0ad9f89","elapsed_seconds":0.1257}
{"mutant":"M03-delete-singular-row","phase":"mutated","utc":"2026-10-23T06:47:59.207791+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"4369d598c4e006aa0a2e558d608db6994bcdf9ae2bf312ec7a74a393f0ad9f89","sha256_after":"4369d598c4e006aa0a2e558d608db6994bcdf9ae2bf312ec7a74a393f0ad9f89","elapsed_seconds":0.0452}
{"mutant":"M03-delete-singular-row","phase":"restored","utc":"2026-10-23T06:48:04.296512+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1448}
{"mutant":"M03-delete-singular-row","phase":"restored","utc":"2026-10-23T06:48:04.441340+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0577}
{"mutant":"M04-weaken-s076-declared","phase":"pristine","utc":"2026-10-23T06:48:04.499132+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1603}
{"mutant":"M04-weaken-s076-declared","phase":"pristine","utc":"2026-10-23T06:48:04.659441+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0538}
{"mutant":"M04-weaken-s076-declared","phase":"mutated","utc":"2026-10-23T06:48:16.498891+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"1e508d098cf930e2373e3949145405bd62a51d7d325418e5353e2b2ea021ddf6","sha256_after":"1e508d098cf930e2373e3949145405bd62a51d7d325418e5353e2b2ea021ddf6","elapsed_seconds":0.1462}
{"mutant":"M04-weaken-s076-declared","phase":"mutated","utc":"2026-10-23T06:48:16.645116+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"1e508d098cf930e2373e3949145405bd62a51d7d325418e5353e2b2ea021ddf6","sha256_after":"1e508d098cf930e2373e3949145405bd62a51d7d325418e5353e2b2ea021ddf6","elapsed_seconds":0.0581}
{"mutant":"M04-weaken-s076-declared","phase":"restored","utc":"2026-10-23T06:48:21.771796+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1454}
{"mutant":"M04-weaken-s076-declared","phase":"restored","utc":"2026-10-23T06:48:21.917195+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0522}
{"mutant":"M05-weaken-s078-declared","phase":"pristine","utc":"2026-10-23T06:48:21.969528+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1366}
{"mutant":"M05-weaken-s078-declared","phase":"pristine","utc":"2026-10-23T06:48:22.106130+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.051}
{"mutant":"M05-weaken-s078-declared","phase":"mutated","utc":"2026-10-23T06:48:27.525723+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"f24014d48b236fb6653293224ee914de274450b0e1d4d7174c97a4ec4bc1d7d6","sha256_after":"f24014d48b236fb6653293224ee914de274450b0e1d4d7174c97a4ec4bc1d7d6","elapsed_seconds":0.1545}
{"mutant":"M05-weaken-s078-declared","phase":"mutated","utc":"2026-10-23T06:48:27.680256+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"f24014d48b236fb6653293224ee914de274450b0e1d4d7174c97a4ec4bc1d7d6","sha256_after":"f24014d48b236fb6653293224ee914de274450b0e1d4d7174c97a4ec4bc1d7d6","elapsed_seconds":0.0558}
{"mutant":"M05-weaken-s078-declared","phase":"restored","utc":"2026-10-23T06:48:32.441520+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.2901}
{"mutant":"M05-weaken-s078-declared","phase":"restored","utc":"2026-10-23T06:48:32.731613+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1093}
{"mutant":"M06-weaken-singular-declared","phase":"pristine","utc":"2026-10-23T06:48:32.841128+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.2532}
{"mutant":"M06-weaken-singular-declared","phase":"pristine","utc":"2026-10-23T06:48:33.094348+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.093}
{"mutant":"M06-weaken-singular-declared","phase":"mutated","utc":"2026-10-23T06:48:41.541908+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"5fb6ff20cb630d330c5b5fc40891080c56a0a3ead160bf08f26839fb334edea7","sha256_after":"5fb6ff20cb630d330c5b5fc40891080c56a0a3ead160bf08f26839fb334edea7","elapsed_seconds":0.1304}
{"mutant":"M06-weaken-singular-declared","phase":"mutated","utc":"2026-10-23T06:48:41.672318+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"5fb6ff20cb630d330c5b5fc40891080c56a0a3ead160bf08f26839fb334edea7","sha256_after":"5fb6ff20cb630d330c5b5fc40891080c56a0a3ead160bf08f26839fb334edea7","elapsed_seconds":0.051}
{"mutant":"M06-weaken-singular-declared","phase":"restored","utc":"2026-10-23T06:48:47.273320+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1329}
{"mutant":"M06-weaken-singular-declared","phase":"restored","utc":"2026-10-23T06:48:47.406243+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0507}
{"mutant":"M07-drop-seeded-entry","phase":"pristine","utc":"2026-10-23T06:48:47.457056+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1428}
{"mutant":"M07-drop-seeded-entry","phase":"pristine","utc":"2026-10-23T06:48:47.599886+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0537}
{"mutant":"M07-drop-seeded-entry","phase":"mutated","utc":"2026-10-23T06:48:54.170801+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":1,"stdout":"","stderr":"Traceback (most recent call last):\n  File \"/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py\", line 306, in <module>\n    sys.exit(main())\n             ~~~~^^\n  File \"/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py\", line 291, in main\n    return self_test()\n  File \"/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py\", line 194, in self_test\n    case(\"red both\", stale_r, stale_s, [\"r51-c2-readme\", \"r51-c2-scorecard-lead\"])\n    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py\", line 184, in case\n    got = sweep(reader(None, t))\n  File \"/fast/scratch/hyaku/kotoba-r57a3/A3MutCorrectionSweep/verifiers/check_correction_sweep.py\", line 120, in sweep\n    raise RuntimeError(\"missing %s\" % e[\"file\"])\nRuntimeError: missing corpus/knowledge/agent-definition-files-round56.md\n","sha256_before":"4f455dd8404aa0d96580f4e93cb8873c51dda33eb51a965ceb4fd66dfbf7972d","sha256_after":"4f455dd8404aa0d96580f4e93cb8873c51dda33eb51a965ceb4fd66dfbf7972d","elapsed_seconds":0.0332}
{"mutant":"M07-drop-seeded-entry","phase":"mutated","utc":"2026-10-23T06:48:54.203968+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"4f455dd8404aa0d96580f4e93cb8873c51dda33eb51a965ceb4fd66dfbf7972d","sha256_after":"4f455dd8404aa0d96580f4e93cb8873c51dda33eb51a965ceb4fd66dfbf7972d","elapsed_seconds":0.0469}
{"mutant":"M07-drop-seeded-entry","phase":"restored","utc":"2026-10-23T06:48:59.936843+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1332}
{"mutant":"M07-drop-seeded-entry","phase":"restored","utc":"2026-10-23T06:49:00.070069+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0508}
{"mutant":"M08-drop-quote-notes-red-arm","phase":"pristine","utc":"2026-10-23T06:49:00.120971+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1474}
{"mutant":"M08-drop-quote-notes-red-arm","phase":"pristine","utc":"2026-10-23T06:49:00.268356+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0602}
{"mutant":"M08-drop-quote-notes-red-arm","phase":"mutated","utc":"2026-10-23T06:49:13.429302+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 17 assertions\n","stderr":"","sha256_before":"ca454494649d5ba9b4d03eec08278ac95931c3fc4442183840a4f947a048959c","sha256_after":"ca454494649d5ba9b4d03eec08278ac95931c3fc4442183840a4f947a048959c","elapsed_seconds":0.1248}
{"mutant":"M08-drop-quote-notes-red-arm","phase":"mutated","utc":"2026-10-23T06:49:13.554093+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"ca454494649d5ba9b4d03eec08278ac95931c3fc4442183840a4f947a048959c","sha256_after":"ca454494649d5ba9b4d03eec08278ac95931c3fc4442183840a4f947a048959c","elapsed_seconds":0.0545}
{"mutant":"M08-drop-quote-notes-red-arm","phase":"restored","utc":"2026-10-23T06:49:18.189031+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1405}
{"mutant":"M08-drop-quote-notes-red-arm","phase":"restored","utc":"2026-10-23T06:49:18.329599+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0526}
{"mutant":"M09-drop-quote-notes-green-arm","phase":"pristine","utc":"2026-10-23T06:49:18.382319+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1337}
{"mutant":"M09-drop-quote-notes-green-arm","phase":"pristine","utc":"2026-10-23T06:49:18.516081+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0528}
{"mutant":"M09-drop-quote-notes-green-arm","phase":"mutated","utc":"2026-10-23T06:49:22.953143+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 17 assertions\n","stderr":"","sha256_before":"c88e95d4a17f1998cefe4951347ef4eaf53747cb4363ce6cc64a35e06e76eb24","sha256_after":"c88e95d4a17f1998cefe4951347ef4eaf53747cb4363ce6cc64a35e06e76eb24","elapsed_seconds":0.1302}
{"mutant":"M09-drop-quote-notes-green-arm","phase":"mutated","utc":"2026-10-23T06:49:23.083411+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"c88e95d4a17f1998cefe4951347ef4eaf53747cb4363ce6cc64a35e06e76eb24","sha256_after":"c88e95d4a17f1998cefe4951347ef4eaf53747cb4363ce6cc64a35e06e76eb24","elapsed_seconds":0.0545}
{"mutant":"M09-drop-quote-notes-green-arm","phase":"restored","utc":"2026-10-23T06:49:28.251903+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1376}
{"mutant":"M09-drop-quote-notes-green-arm","phase":"restored","utc":"2026-10-23T06:49:28.389509+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0616}
{"mutant":"M10-drop-singular-red-arm","phase":"pristine","utc":"2026-10-23T06:49:28.451292+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1444}
{"mutant":"M10-drop-singular-red-arm","phase":"pristine","utc":"2026-10-23T06:49:28.595684+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0525}
{"mutant":"M10-drop-singular-red-arm","phase":"mutated","utc":"2026-10-23T06:49:32.995091+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 17 assertions\n","stderr":"","sha256_before":"d7bbc8a280e1dde8187da9c427a88cc13a72f6f90aed9563b7ea09997ee96048","sha256_after":"d7bbc8a280e1dde8187da9c427a88cc13a72f6f90aed9563b7ea09997ee96048","elapsed_seconds":0.1379}
{"mutant":"M10-drop-singular-red-arm","phase":"mutated","utc":"2026-10-23T06:49:33.133047+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"d7bbc8a280e1dde8187da9c427a88cc13a72f6f90aed9563b7ea09997ee96048","sha256_after":"d7bbc8a280e1dde8187da9c427a88cc13a72f6f90aed9563b7ea09997ee96048","elapsed_seconds":0.0527}
{"mutant":"M10-drop-singular-red-arm","phase":"restored","utc":"2026-10-23T06:49:37.920372+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.131}
{"mutant":"M10-drop-singular-red-arm","phase":"restored","utc":"2026-10-23T06:49:38.051421+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0522}
{"mutant":"M11-drop-singular-green-arm","phase":"pristine","utc":"2026-10-23T06:49:38.103750+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.1306}
{"mutant":"M11-drop-singular-green-arm","phase":"pristine","utc":"2026-10-23T06:49:38.234357+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0533}
{"mutant":"M11-drop-singular-green-arm","phase":"mutated","utc":"2026-10-23T06:49:42.799591+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 17 assertions\n","stderr":"","sha256_before":"7a06fd21777538338b21c2dc3426b01e551a88709dc4ba7e2f1735aebea7c729","sha256_after":"7a06fd21777538338b21c2dc3426b01e551a88709dc4ba7e2f1735aebea7c729","elapsed_seconds":0.28}
{"mutant":"M11-drop-singular-green-arm","phase":"mutated","utc":"2026-10-23T06:49:43.079645+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"7a06fd21777538338b21c2dc3426b01e551a88709dc4ba7e2f1735aebea7c729","sha256_after":"7a06fd21777538338b21c2dc3426b01e551a88709dc4ba7e2f1735aebea7c729","elapsed_seconds":0.0959}
{"mutant":"M11-drop-singular-green-arm","phase":"restored","utc":"2026-10-23T06:49:47.516815+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --self-test","exit_code":0,"stdout":"0 failure(s) over 18 assertions\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.2309}
{"mutant":"M11-drop-singular-green-arm","phase":"restored","utc":"2026-10-23T06:49:47.747764+00:00","command":"timeout 120 python3 -B verifiers/check_correction_sweep.py --rev 07c33d73ddce769d9cea2846a6313164401b5478","exit_code":0,"stdout":"correction sweep: 0 stale block(s)\n","stderr":"","sha256_before":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","sha256_after":"799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18","elapsed_seconds":0.0906}
```
