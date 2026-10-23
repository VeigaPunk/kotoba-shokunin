Result: BREAKS — The no-reader line-count control reached K=8/11 (E=4/5), a high-count finding; none of the four controls met the exact C2 predicate.

## Findings and verdict

Axes: discrimination (K and E), skipped behavioral work, exact byte restoration, and frozen-counter custody.

| World | K | E | Counter exit | Meets K=11 and E=5? | Verdict |
|---|---:|---:|---:|---|---|
| Pristine | 4/11 | 5/5 | 1 | No | Valid baseline; inner pristine self-test passed |
| (a) always exits 1 | Not scored | Not scored | 2 | No | Inconclusive mutation score: its own pristine self-test fails |
| (b) always exits 0 | 0/11 | 5/5 | 1 | No | Rejected/killed control |
| (c) line count only | 8/11 | 4/5 | 1 | No | Rejected/killed control; high-K coverage finding |
| (d) case-call count only | 4/11 | 5/5 | 1 | No | Rejected/killed control; reproduces baseline totals without behavior |
| Restored after each of (a)–(d) | 4/11 | 5/5 | 1 | No | Same output as pristine |

The strict Boolean C2 acceptance predicate rejected every evaluable control. BREAKS is the requested high-count classification, not a claim that any control passed the predicate. Control (c) doubles the pristine kill total while skipping every behavioral case, reader call, and CLI probe; equivalent E5 catches its comment/line-count sensitivity. Control (d) matches the pristine aggregate score but kills M08–M11 instead of pristine M01–M03/M07. Do not treat a failing pristine self-test in (a) as killed mutants.

## Frozen detector and scope

Checkout before any world: `3de87aad29e960c95ed35840442f424c48c29729`. All sandbox Git writes and control execution used `/fast/scratch/hyaku/kotoba-r58/CtlC2AllFail`. Only this report was written in the lane. No counter was edited, no external source was fetched, no paid model call was made, no other runtime was invoked, and no tool was installed or updated.

Time window for the identical `--file` detector series: 2026-10-23T07:56:02.014080+00:00 through 2026-10-23T07:57:29.880732+00:00.

Expected detector: the committed `verifiers/check_sweep_mutants.py`, whose `evaluate` routine first requires pristine self-test exit 0, then applies the 11 mutants and 5 equivalents exactly once. Exit 0 iff K=11 and E=5; exit 1 otherwise; pristine failure gives exit 2 before K/E are printed. Counter evidence: `verifiers/check_sweep_mutants.py:258-273,277-283,379-399` at the pinned checkout.

Every controlled `--file` run below uses the identical command, working directory, and environment. `TMPDIR` was set to the sandbox’s `.control-tmp`, and GIT_DIR, GIT_WORK_TREE, and GIT_INDEX_FILE were absent. The earlier revision preflight used the counter’s default temporary-directory setting; it is also pasted below. Each started external command was capped with `timeout` (at most 900 seconds). No concurrent load runs were used.

## Worlds: smallest behavior-bearing mutation

Each world changes only `verifiers/check_correction_sweep.py:169`, preserving the 307-line layout and all frozen old-text anchors. Original line: `    fails, n = [], 0`. Keeping this initialization preserves the enclosing binding required by the nested `nonlocal n`; the added return skips the existing self-test. Original call count is 15 four-space-prefixed `case(` occurrences, excluding `def case(`. The string construction in (d) avoids adding a self-counting occurrence. No corpus or actual correction-sweep behavior is read by these controls.

### (a) always exits 1

Commit: sandbox 6e20441e8f740c8438bf7b11956a1bcb115fef5b (/fast/scratch/hyaku/kotoba-r58/CtlC2AllFail)

Replacement at `verifiers/check_correction_sweep.py:169`:
```python
    fails, n = [], 0; return 1
```

### (b) always exits 0

Commit: sandbox 7b7d0791551ffd4b5b6d3799af6fab8cc31b24fc (/fast/scratch/hyaku/kotoba-r58/CtlC2AllFail)

Replacement at `verifiers/check_correction_sweep.py:169`:
```python
    fails, n = [], 0; return 0
```

### (c) original line count only

Commit: sandbox 3af281205022745f69136b7b9f012f4e22f3566a (/fast/scratch/hyaku/kotoba-r58/CtlC2AllFail)

Replacement at `verifiers/check_correction_sweep.py:169`:
```python
    fails, n = [], 0; return int(len(Path(__file__).read_text().splitlines()) != 307)
```

### (d) original case-call count only

Commit: sandbox 81467c9c29bcd86a09de6e09fb6ac1763feab5d6 (/fast/scratch/hyaku/kotoba-r58/CtlC2AllFail)

Replacement at `verifiers/check_correction_sweep.py:169`:
```python
    fails, n = [], 0; return int(Path(__file__).read_text().count("    " + "case" + "(") != 15)
```

## Hash and restoration evidence

At the initial committed checkout, `timeout 30 sha256sum verifiers/check_command_files.py verifiers/check_sweep_mutants.py verifiers/check_correction_sweep.py` exited 0 with:
```text
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
```

| Control | Before source sha256 | Mutated source sha256 | Restored source sha256 |
|---|---|---|---|

| (a) | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` | `b445475eb000ff531dce3bea5a32929bfe92e311e31a108c9352789156eb4ace` | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` |

| (b) | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` | `000cd0e6a25fc7dd1aa8b84c3ea88cefe3006e3966c56a1ab9252134d3ee805b` | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` |

| (c) | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` | `63fe255631eb15035d449ce69e43daa25881f67387197150f88de5e7b00aff6a` | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` |

| (d) | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` | `b2faa749db839aaa049e88f38fd9cfa901bd0cbe1de0f44d8f06151de29bdd2b` | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` |


The original one-line initialization was restored after each detector, including the exit-2 control. Each restored hash equals the initial sha256 and the same detector was then rerun; full outputs follow. Final working bytes are pristine; sandbox world commits are intentionally retained for reproduction (the checkout/index are not claimed to be clean). Final counter hashes also match the initial committed bytes.

## Preparation commands

Both commands exited 0, with no output:
```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/CtlC2AllFail
timeout 60 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r58/CtlC2AllFail checkout -q 3de87aad29e960c95ed35840442f424c48c29729
```

`timeout 30 wc -l verifiers/check_correction_sweep.py` exited 0 and printed `307 verifiers/check_correction_sweep.py`. `timeout 30 mkdir -p /fast/scratch/hyaku/kotoba-r58/CtlC2AllFail/.control-tmp` exited 0 with no output. The source search `^    case\(` returned the 15 calls at lines 195,196,197,198,199,201,203,211,213,219,221,225,227,229,232.

For each (a)–(d), `timeout 60 git add verifiers/check_correction_sweep.py` and the following corresponding commit command exited 0, with empty stdout/stderr. `timeout 60 git rev-parse HEAD` exited 0 for each; its observed identity is labelled under the world above.

```sh
timeout 60 git -c 'user.name=Kotoba mutation control' -c user.email=kotoba-control@localhost -c core.hooksPath=/dev/null commit -q -m 'sandbox C2 control a: self-test always exits one'
```

```sh
timeout 60 git -c 'user.name=Kotoba mutation control' -c user.email=kotoba-control@localhost -c core.hooksPath=/dev/null commit -q -m 'sandbox C2 control b: self-test always exits zero'
```

```sh
timeout 60 git -c 'user.name=Kotoba mutation control' -c user.email=kotoba-control@localhost -c core.hooksPath=/dev/null commit -q -m 'sandbox C2 control c: self-test only checks original line count'
```

```sh
timeout 60 git -c 'user.name=Kotoba mutation control' -c user.email=kotoba-control@localhost -c core.hooksPath=/dev/null commit -q -m 'sandbox C2 control d: self-test only counts original case calls'
```

## Full detector output and exit codes

### Initial revision preflight

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --rev 3de87aad29e960c95ed35840442f424c48c29729
stdout:
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
stderr:
(empty)
exit=1
```

### pristine --file baseline

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
stderr:
(empty)
exit=1
```

### a always-fail frozen score

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
(empty)
stderr:
could-not-evaluate: pristine self-test exit 1
exit=2
```

### a restored frozen score

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
stderr:
(empty)
exit=1
```

### b always-pass frozen score

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
M01 mutant survived exit=0
M02 mutant survived exit=0
M03 mutant survived exit=0
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant survived exit=0
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 0 of 11; equivalents survived 5 of 5
stderr:
(empty)
exit=1
```

### b restored frozen score

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
stderr:
(empty)
exit=1
```

### c line-count frozen score

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant killed exit=1
M09 mutant killed exit=1
M10 mutant killed exit=1
M11 mutant killed exit=1
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent killed exit=1
sweep mutants killed 8 of 11; equivalents survived 4 of 5
stderr:
(empty)
exit=1
```

### c restored frozen score

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
stderr:
(empty)
exit=1
```

### d case-count frozen score

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
M01 mutant survived exit=0
M02 mutant survived exit=0
M03 mutant survived exit=0
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant survived exit=0
M08 mutant killed exit=1
M09 mutant killed exit=1
M10 mutant killed exit=1
M11 mutant killed exit=1
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
stderr:
(empty)
exit=1
```

### d restored frozen score

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
stdout:
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant survived exit=0
M05 mutant survived exit=0
M06 mutant survived exit=0
M07 mutant killed exit=1
M08 mutant survived exit=0
M09 mutant survived exit=0
M10 mutant survived exit=0
M11 mutant survived exit=0
E1 equivalent survived exit=0
E2 equivalent survived exit=0
E3 equivalent survived exit=0
E4 equivalent survived exit=0
E5 equivalent survived exit=0
sweep mutants killed 4 of 11; equivalents survived 5 of 5
stderr:
(empty)
exit=1
```

## Full hash-run outputs

### a mutated source hash

```text
$ timeout 30 sha256sum verifiers/check_correction_sweep.py
stdout:
b445475eb000ff531dce3bea5a32929bfe92e311e31a108c9352789156eb4ace  verifiers/check_correction_sweep.py
stderr:
(empty)
exit=0
```

### a restored source hash

```text
$ timeout 30 sha256sum verifiers/check_correction_sweep.py
stdout:
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
stderr:
(empty)
exit=0
```

### b mutated source hash

```text
$ timeout 30 sha256sum verifiers/check_correction_sweep.py
stdout:
000cd0e6a25fc7dd1aa8b84c3ea88cefe3006e3966c56a1ab9252134d3ee805b  verifiers/check_correction_sweep.py
stderr:
(empty)
exit=0
```

### b restored source hash

```text
$ timeout 30 sha256sum verifiers/check_correction_sweep.py
stdout:
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
stderr:
(empty)
exit=0
```

### c mutated source hash

```text
$ timeout 30 sha256sum verifiers/check_correction_sweep.py
stdout:
63fe255631eb15035d449ce69e43daa25881f67387197150f88de5e7b00aff6a  verifiers/check_correction_sweep.py
stderr:
(empty)
exit=0
```

### c restored source hash

```text
$ timeout 30 sha256sum verifiers/check_correction_sweep.py
stdout:
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
stderr:
(empty)
exit=0
```

### d mutated source hash

```text
$ timeout 30 sha256sum verifiers/check_correction_sweep.py
stdout:
b2faa749db839aaa049e88f38fd9cfa901bd0cbe1de0f44d8f06151de29bdd2b  verifiers/check_correction_sweep.py
stderr:
(empty)
exit=0
```

### d restored source hash

```text
$ timeout 30 sha256sum verifiers/check_correction_sweep.py
stdout:
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
stderr:
(empty)
exit=0
```

### final frozen counter hashes

```text
$ timeout 30 sha256sum verifiers/check_command_files.py verifiers/check_sweep_mutants.py
stdout:
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
stderr:
(empty)
exit=0
```

Report: .ufo/waves/round-58/controls/CtlC2AllFail.md
