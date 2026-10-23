Result: HOLDS — The snapshot-only self-test scored K = 11, E = 0, exit 1; the frozen C2 predicate rejected this shortcut.

## Control and expected detector

Axes: minimal control cost, predicate discrimination, exact-byte restoration.

- Counter revision: `3de87aad29e960c95ed35840442f424c48c29729`, checked out before constructing the world. The counter was never edited.
- World: sandbox 6ecf4d3cfc36b664888170077856a6f1f7155684 (/fast/scratch/hyaku/kotoba-r58/CtlC2Snapshot).
- One behavior-bearing insertion at that world's `verifiers/check_correction_sweep.py:169–176` makes `self_test()` return after checking its own source snapshot. All original behavioral fixtures remain below an unconditional return, preserving the frozen replacement texts but never executing those fixtures.
- The expected digest covers the entire source after replacing its embedded digest's first occurrence with 64 ASCII zeroes. This avoids a self-referential hash; the stored digest is `3efe944a8eea214c3915eac6c8a14bfc75c7cd27da9b2e12cd150a1327eb44cd`.
- No fixture IDs, mutant labels, mutant texts, or equivalent labels occur in the inserted decision logic.
- Expected: every frozen source change fails the snapshot, yielding K = 11 but E < 5. Observed: K = 11, E = 0, exit 1. All five equivalent rewrites were falsely rejected by the shortcut, including the comment-only E5.
- Verdict: the shortcut was rejected/killed by the combined C2 predicate, not a C2 finding. K = 11 alone would accept this bad self-test; requiring E = 5 prevents that acceptance (`verifiers/check_sweep_mutants.py:258–273,394–399`).

Inserted control:

```python
    # Snapshot-only control: skip every behavioral fixture below.
    from hashlib import sha256
    expected = "3efe944a8eea214c3915eac6c8a14bfc75c7cd27da9b2e12cd150a1327eb44cd"
    source = Path(__file__).read_bytes()
    actual = sha256(source.replace(expected.encode("ascii"), b"0" * 64, 1)).hexdigest()
    print("source snapshot: " + ("matches" if actual == expected else "changed"))
    return 0 if actual == expected else 1
```

## All detector runs

All commands ran in `/fast/scratch/hyaku/kotoba-r58/CtlC2Snapshot`, with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` removed from the environment and `TMPDIR=/fast/scratch/hyaku/kotoba-r58/CtlC2Snapshot/.probe-tmp`. The same frozen counter evaluated pristine, mutated, and restored bytes. No stderr was emitted by these runs.

Each evaluated source passed the counter's pristine self-test guard, which requires exit 0 before evaluating the table (`verifiers/check_sweep_mutants.py:258–262`). The pristine/restored counter exit 1 below is the expected K = 4 predicate miss, not a failed pristine self-test and not evidence of killing the control.

### 1. Pristine bytes at the committed counter revision

```text
TMPDIR=/fast/scratch/hyaku/kotoba-r58/CtlC2Snapshot/.probe-tmp timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
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
exit=1
```

### 2. Snapshot-only sandbox world

The revision argument below identifies sandbox 6ecf4d3cfc36b664888170077856a6f1f7155684 (/fast/scratch/hyaku/kotoba-r58/CtlC2Snapshot).

```text
TMPDIR=/fast/scratch/hyaku/kotoba-r58/CtlC2Snapshot/.probe-tmp timeout 900 python3 -B verifiers/check_sweep_mutants.py --rev 6ecf4d3cfc36b664888170077856a6f1f7155684
M01 mutant killed exit=1
M02 mutant killed exit=1
M03 mutant killed exit=1
M04 mutant killed exit=1
M05 mutant killed exit=1
M06 mutant killed exit=1
M07 mutant killed exit=1
M08 mutant killed exit=1
M09 mutant killed exit=1
M10 mutant killed exit=1
M11 mutant killed exit=1
E1 equivalent killed exit=1
E2 equivalent killed exit=1
E3 equivalent killed exit=1
E4 equivalent killed exit=1
E5 equivalent killed exit=1
sweep mutants killed 11 of 11; equivalents survived 0 of 5
exit=1
```

### 3. Restored pristine bytes

```text
TMPDIR=/fast/scratch/hyaku/kotoba-r58/CtlC2Snapshot/.probe-tmp timeout 900 python3 -B verifiers/check_sweep_mutants.py --file verifiers/check_correction_sweep.py
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
exit=1
```

## Hashes and restoration evidence

`timeout 30 sha256sum verifiers/check_correction_sweep.py` completed with exit 0 before mutation and after committing the control, producing these actual source hashes:

| State | SHA256 |
|---|---|
| Pristine | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` |
| Snapshot world | `9e12f24ebe994d36053a19c354d8fe5aadb0cd9ce78a812e4c49ef324c04e235` |
| Restored | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` |

Restoration ran in a `finally` block after scoring the sandbox world:

```text
timeout 30 git checkout -q 3de87aad29e960c95ed35840442f424c48c29729
exit=0
```

At that restored revision, the following command records both the exact restored target and the committed counter hashes:

```text
timeout 30 sha256sum verifiers/check_correction_sweep.py verifiers/check_command_files.py verifiers/check_sweep_mutants.py
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
exit=0
```

The two counter hashes also matched the initial `timeout 30 sha256sum verifiers/check_command_files.py verifiers/check_sweep_mutants.py` output at `3de87aad29e960c95ed35840442f424c48c29729` (exit 0). The source bytes and detector outputs were restored exactly. The empty scratch TMPDIR was removed successfully. The sandbox commit remains in the clone; nothing was pushed. Lane code and counters were not changed; only this assigned report was written in the lane. No tools were installed or updated.
