# w4-bless-drift

**Kind:** plan § C3 shortcut control 4 — bless the corpus DRIFT values in
`verifiers/corpus-baseline.json` without indexing the spot-check file.

**Base:** `072048fa8e8a52c707d25f7079772fa317244eb7`  **World rev (measured):**
`a99306051d4bd9294f9018f1831591835553c9a2`  **Tree:** `5983cb12d26ca2e908c3710b794373ee9cca347b`

## Moves (2)

- `corpus.index.tracked_files` expectation 135 → **136**
- `corpus.pointers.report_total` expectation 93 → **95**

Both are the base's own observed values; the unindexed spot-check file is deliberately left
unindexed (`corpus.index.unindexed` stays `zero`-mode, expect 0).

## Counter reading

| gate | exit | wall |
|---|---|---|
| check_gate_registry `--rev <rev>` | 0 | 0.7s |
| check_assertion_floors | 0 | 78.1s |
| verify_skill_checklist | 0 | 2.3s |
| verify_corpus_integrity | **1** | 0.4s |
| verify_corpus_independent | **1** | 0.8s |
| check_correction_sweep `--root .` | 0 | 0.1s |

**`tip battery exit 0: 4 of 6`, counter exit 1** (`counter.out`, run 21:13).

## Why the blessing does not work — measured

Running the gate in the world tree:

```
corpus.index    tracked=136 unindexed=1 stale=0 missing=0
corpus.pointers report_dead=0/95 commit_total=41 unresolvable=0 nonhash=0
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
8/9 checks pass; DRIFT: corpus.index.unindexed
exit 1
```

`zero`-mode checks are **baseline-independent** by construction
(`verifiers/verify_corpus_integrity.py:94-96`: "`--no-baseline` suppresses the comparison …
but a `zero` violation is baseline-independent and still exits 1"), so blessing the two
`equal` values leaves the unindexed file red. `verify_corpus_independent` re-derives the
same `unindexed` observation without a baseline and also exits 1. Plan expectation holds:
integrity stays red.

## Guard reading

| guard | verdict |
|---|---|
| no-deletions | PASS |
| floors | PASS |
| instrument-size | FAIL — `instruments gain 76 lines > 40` (inherited from the base) |
| instrument-pin | PASS |
| spotcheck-identity | PASS |

`verifiers/corpus-baseline.json` is not covered by any guard: no path guard, no pin, no
floor. The only thing that stops this world is that the `zero`-mode checks ignore the file
entirely. (This is the same conclusion the round-72 sibling reached for base `c69711e`; the world is
re-derived here because the round-73 base's observed values are 136 tracked / 1 unindexed /
95 report pointers, not the values the r72 patch was written against, so that patch does not
apply.)

N is stable across the fleet-object drift described in `w1-delete-and-rerecord/README.md`:
the world keeps the unindexed spot-check, so both corpus gates are red at either fleet
state.

## Replay

```sh
sh replay.sh            # fresh fleet-shaped sandbox; prints rev, battery, counter exit
KEEP=1 sh replay.sh     # keeps the sandbox
```

Round-72 sibling: `.ufo/waves/round-72/w1/build/ExecBatteryControls/w4-bless-drift/`.
