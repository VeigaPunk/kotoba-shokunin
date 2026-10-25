# w4-bless-drift

**Kind:** plan-named shortcut control (plan § C3 item 4)

**Base:** `c69711ee08279609374d895bb0f3c8c18ccf15c9`  **World rev:** `74ec027d731b82935442352b58b718460a4b2f44`  **Tree:** `fac9527a9eb1a450d38d9e0cd9a06eec60ca9485`

verify_corpus_integrity.py:688-695 keeps unindexed and commit_nonhash in baseline-free 'zero' mode (evaluate():717-720), so the two blessed values are ignored and the gate stays exit 1. The three 'equal' values are blessable and do go green. The world reads N == 2 -- byte-for-byte the base's battery -- so this shortcut moves nothing at all.

## Moves

- bless the five DRIFT observations in verifiers/corpus-baseline.json (tracked_files 133, unindexed 1, report_total 93, commit_total 41, commit_nonhash 2); no corpus file is touched or indexed

## Observed battery (six frozen commands, run in a fleet-shaped sandbox)

| gate | command | exit | wall |
|---|---|---|---|
| check_gate_registry | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | 1 | 1s |
| check_assertion_floors | `python3 -B verifiers/check_assertion_floors.py` | 1 | 43s |
| verify_skill_checklist | `python3 -B verifiers/verify_skill_checklist.py` | 0 | 2s |
| verify_corpus_integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 1 | 0s |
| verify_corpus_independent | `python3 -B verifiers/verify_corpus_independent.py` | 1 | 1s |
| check_correction_sweep | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | 0s |

**N = 2 of 6.**

## Guard reading (recomputed by guards.py over base..world_rev)

- no-deletions: pass 
- floors: pass 
- instrument-size: added 0 / removed 0 (cap 40); added-only reading pass, two-direction reading pass
- spotcheck-identity: pass 

**Guard that catches this world:** none needed: verify_corpus_integrity.py stays red by construction

## The counter draft on this world

```
measured rev 74ec027d731b82935442352b58b718460a4b2f44 in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 0; floors 15 rows; instruments added 0 / deleted 0 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 1 wall 0.3s
gate verifiers/check_assertion_floors.py exit 1 wall 41.6s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.4s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.1s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 44.4s
tip battery exit 0: 2 of 6
counter exit=1
```

## Replay

```sh
sh replay.sh        # fresh fleet-shaped sandbox, six gates, guards; removed after
KEEP=1 sh replay.sh # keeps the sandbox path
```

`apply.sh` clones the base `c69711ee08279609374d895bb0f3c8c18ccf15c9` with `--shared` into a parent that symlinks every fleet-root entry, applies `world.patch`, commits inside the sandbox only, and prints the world revision.
