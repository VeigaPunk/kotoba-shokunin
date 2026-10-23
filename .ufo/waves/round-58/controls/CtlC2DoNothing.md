Result: HOLDS — the base and junk-only controls both scored K=4/11, E=5/5, exit 1; neither reached the C2 predicate, and exact target bytes were restored.

## Scope and worlds

Axes: frozen-counter immutability, rejection of no-work changes, and byte-exact restoration.

All execution and Git writes occurred with cwd `/fast/scratch/hyaku/kotoba-r58/CtlC2DoNothing`. The clone was created from the lane and initially checked out at `3de87aad29e960c95ed35840442f424c48c29729` (setup exit 0). The only lane write is this report. No source pages were fetched and no tools were installed or updated.

- Supplied base / do-nothing target: `f56f6e191762c27c1aa2af11a204db9e2ca4edec`, explicitly scored with `--rev`.
- Junk world: sandbox 60daae0321a7061f4b5529332e98237e21f8ec7c (/fast/scratch/hyaku/kotoba-r58/CtlC2DoNothing).
- Restored, unchanged-target world: sandbox baccaa79bb6a9ff62f22a00aa230dbf521571ff5 (/fast/scratch/hyaku/kotoba-r58/CtlC2DoNothing).

The junk world adds only one docstring sentence, one comment, blank lines, and two duplicate clean-fixture self-test arms to `verifiers/check_correction_sweep.py`. The arms repeat the existing clean case at base `verifiers/check_correction_sweep.py:199`; they assert nothing new. At the junk revision, the additions are at lines 19–20 and 236–239:

```python
Sandbox junk control: extra prose and duplicate clean cases add no coverage.

    # Junk control: these repeat the existing clean-fixture assertion unchanged.
    case("junk clean duplicate one", "- nothing here\n", "| depth | 9 | x |\n", [])
    case("junk clean duplicate two", "- nothing here\n", "| depth | 9 | x |\n", [])
```

No registry entries, readers, frozen mutant texts, existing assertions, or counter bytes were changed. Both sandbox commit commands exited 0. The added target lines were then removed, and the restoration was committed before its detector run.

## Expected detector and verdict

Frozen detector: `verifiers/check_sweep_mutants.py` from `3de87aad29e960c95ed35840442f424c48c29729`. It first requires the target's pristine self-test to exit 0 (`:258–273`), then returns 0 iff K=11 and E=5 (`:394–399`). Expected negative-control result: K=4, E=5, exit 1, unchanged by comments or redundant cases.

Observed: all four detector runs produced K=4, E=5, exit 1. M01, M02, M03 and M07 were killed; M04–M06 and M08–M11 survived; E1–E5 survived. No row was not-applicable, no timeout occurred, and no run reported `could-not-evaluate`. Thus this is an evaluable negative control, not an inconclusive pristine-self-test failure. The junk control was rejected and gained zero kills. No counter-bypass finding in these controls; this does not establish adequacy against other controls.

| Run | K | E | Exit |
|---|---:|---:|---:|
| Base, direct requested command | 4/11 | 5/5 | 1 |
| Base, clone-local TMPDIR | 4/11 | 5/5 | 1 |
| Junk, clone-local TMPDIR | 4/11 | 5/5 | 1 |
| Restored, clone-local TMPDIR | 4/11 | 5/5 | 1 |

The first baseline used the counter's inherited/default temporary-directory location. It was repeated with TMPDIR under the clone; that repeat, the junk run, and the restored run use the same bounded detector and clone-local temporary directory.

## Complete detector runs

### 1. Base: direct requested command

```text
$ timeout 900 python3 -B verifiers/check_sweep_mutants.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
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
Exit: 1
```

### 2. Base: clone-local temporary directories

```text
$ timeout 900 env TMPDIR=/fast/scratch/hyaku/kotoba-r58/CtlC2DoNothing/.control-tmp python3 -B verifiers/check_sweep_mutants.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
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
Exit: 1
```

### 3. Junk world

Revision below: sandbox 60daae0321a7061f4b5529332e98237e21f8ec7c (/fast/scratch/hyaku/kotoba-r58/CtlC2DoNothing).

```text
$ timeout 900 env TMPDIR=/fast/scratch/hyaku/kotoba-r58/CtlC2DoNothing/.control-tmp python3 -B verifiers/check_sweep_mutants.py --rev 60daae0321a7061f4b5529332e98237e21f8ec7c
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
Exit: 1
```

### 4. Restored target

Revision below: sandbox baccaa79bb6a9ff62f22a00aa230dbf521571ff5 (/fast/scratch/hyaku/kotoba-r58/CtlC2DoNothing).

```text
$ timeout 900 env TMPDIR=/fast/scratch/hyaku/kotoba-r58/CtlC2DoNothing/.control-tmp python3 -B verifiers/check_sweep_mutants.py --rev baccaa79bb6a9ff62f22a00aa230dbf521571ff5
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
Exit: 1
```

## Hashes and restoration evidence

At initial checkout `3de87aad29e960c95ed35840442f424c48c29729`:

```text
$ timeout 15 sha256sum verifiers/check_command_files.py verifiers/check_sweep_mutants.py verifiers/check_correction_sweep.py
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
Exit: 0
```

After committing the junk world:

```text
$ timeout 15 sha256sum verifiers/check_correction_sweep.py
7507c6743ac08cf159229c275c56d0c64de2f8f05214f55fee73581cc0281cb4  verifiers/check_correction_sweep.py
Exit: 0
```

After committing the restoration:

```text
$ timeout 15 sha256sum verifiers/check_command_files.py verifiers/check_sweep_mutants.py verifiers/check_correction_sweep.py
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
Exit: 0
```

Direct supplied-base blob hash:

```text
$ timeout 15 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git show f56f6e191762c27c1aa2af11a204db9e2ca4edec:verifiers/check_correction_sweep.py | timeout 15 sha256sum
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  -
Exit: 0
```

The restored target SHA-256 equals both the initial frozen-checkout target and the supplied base blob. Both counter hashes also remain identical. The restored detector run reproduces the base's complete row-by-row output and exit code.
