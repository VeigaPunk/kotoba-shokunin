# probe-instrument-modes

**Kind:** derived probe (superseded by probe-naive-mode-flip; kept for its receipt)

**Base:** `c69711ee08279609374d895bb0f3c8c18ccf15c9`  **World rev:** `014b190e565d31af58ca02202059f79fc79b00ae`  **Tree:** `8331cef6d3c7f5cb9dfc6ff067c7f4a027802ae5`

The first, confounded probe. It shows the flip's first-order cost: the corpus_integrity self-test still pins the flipped arm, so check_assertion_floors reads 'FAIL corpus_integrity observed=161 floor=161 self_test_failures=1' and the world reads N == 5.

## Moves

- stub check_gate_registry.py
- delete the failing checklist arm and lower its floor
- flip the two zero-mode corpus verdicts in verify_corpus_integrity.py
- drop the two counts from verify_corpus_independent.py violations()
- bless the five DRIFT values

## Observed battery (six frozen commands, run in a fleet-shaped sandbox)

| gate | command | exit | wall |
|---|---|---|---|
| check_gate_registry | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | 0 | 0s |
| check_assertion_floors | `python3 -B verifiers/check_assertion_floors.py` | 1 | 48s |
| verify_skill_checklist | `python3 -B verifiers/verify_skill_checklist.py` | 0 | 1s |
| verify_corpus_integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 0 | 1s |
| verify_corpus_independent | `python3 -B verifiers/verify_corpus_independent.py` | 0 | 0s |
| check_correction_sweep | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | 0s |

**N = 5 of 6.**

## Guard reading (recomputed by guards.py over base..world_rev)

- no-deletions: pass 
- floors: FIRES [['checklist', 1862, 1861]]
- instrument-size: added 7 / removed 386 (cap 40); added-only reading pass, two-direction reading FIRES
- spotcheck-identity: pass 

**Guard that catches this world:** floors (via the corpus_integrity self-test) + instrument-size + floors guard

## The counter draft on this world

```
measured rev 014b190e565d31af58ca02202059f79fc79b00ae in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 0; floors 15 rows; instruments added 7 / deleted 386 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
FAIL guard floors: row checklist floor 1861 < base 1862
FAIL guard instrument-size: instruments lose 386 lines > 40
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.0s
gate verifiers/check_assertion_floors.py exit 1 wall 38.3s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.4s
gate verifiers/verify_corpus_integrity.py exit 0 wall 0.2s
gate verifiers/verify_corpus_independent.py exit 0 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 41.0s
tip battery exit 0: 5 of 6
counter exit=1
```

## Replay

```sh
sh replay.sh        # fresh fleet-shaped sandbox, six gates, guards; removed after
KEEP=1 sh replay.sh # keeps the sandbox path
```

`apply.sh` clones the base `c69711ee08279609374d895bb0f3c8c18ccf15c9` with `--shared` into a parent that symlinks every fleet-root entry, applies `world.patch`, commits inside the sandbox only, and prints the world revision.
