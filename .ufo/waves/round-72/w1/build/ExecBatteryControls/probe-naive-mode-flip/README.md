# probe-naive-mode-flip

**Kind:** derived probe: the flip alone, nothing else

**Base:** `c69711ee08279609374d895bb0f3c8c18ccf15c9`  **World rev:** `167b098976e68c2e9d2c02ed36ac66b0472a51f0`  **Tree:** `b63c4ba6bb392ab83b3d321defe312f91358b5da`

Isolates the flip and measures its two remaining costs. verify_corpus_integrity stays exit 1 because 'equal' mode now compares the observed 1 and 2 against a baseline that still says 0 (the bless is a separate step), and check_assertion_floors stays exit 1 because the instrument's own self-test still pins the zero-mode verdict (one assertion). N == 3. probe-clean-guards takes both steps.

## Moves

- flip corpus.index.unindexed and corpus.pointers.commit_nonhash from 'zero' to 'equal' in verifiers/verify_corpus_integrity.py (2 lines)
- drop unindexed and commit_nonhash from violations() in verifiers/verify_corpus_independent.py (2 lines)

## Observed battery (six frozen commands, run in a fleet-shaped sandbox)

| gate | command | exit | wall |
|---|---|---|---|
| check_gate_registry | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | 1 | 0s |
| check_assertion_floors | `python3 -B verifiers/check_assertion_floors.py` | 1 | 38s |
| verify_skill_checklist | `python3 -B verifiers/verify_skill_checklist.py` | 0 | 2s |
| verify_corpus_integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 1 | 0s |
| verify_corpus_independent | `python3 -B verifiers/verify_corpus_independent.py` | 0 | 0s |
| check_correction_sweep | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | 0s |

**N = 3 of 6.**

## Guard reading (recomputed by guards.py over base..world_rev)

- no-deletions: pass 
- floors: pass 
- instrument-size: added 4 / removed 4 (cap 40); added-only reading pass, two-direction reading pass
- spotcheck-identity: pass 

**Guard that catches this world:** floors (corpus_integrity self-test); the integrity gate itself stays red

## The counter draft on this world

```
measured rev 167b098976e68c2e9d2c02ed36ac66b0472a51f0 in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 0; floors 15 rows; instruments added 4 / deleted 4 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 1 wall 0.3s
gate verifiers/check_assertion_floors.py exit 1 wall 43.5s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.5s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.2s
gate verifiers/verify_corpus_independent.py exit 0 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 46.8s
tip battery exit 0: 3 of 6
counter exit=1
```

## Replay

```sh
sh replay.sh        # fresh fleet-shaped sandbox, six gates, guards; removed after
KEEP=1 sh replay.sh # keeps the sandbox path
```

`apply.sh` clones the base `c69711ee08279609374d895bb0f3c8c18ccf15c9` with `--shared` into a parent that symlinks every fleet-root entry, applies `world.patch`, commits inside the sandbox only, and prints the world revision.
