# probe-clean-guards

**Kind:** derived probe: the counter-design finding

**Base:** `c69711ee08279609374d895bb0f3c8c18ccf15c9`  **World rev:** `25b059d2fa62bec7fddb02dd176db53952982f33`  **Tree:** `8c6b217dd03a055466b42d9d0f6dbeb77872355e`

This world reads 6 of 6 and passes every guard (no deletion, no floor lowered, 8 added / 8 removed instrument lines, all 26 spot-check files byte-identical). The five DRIFTs are still present in the corpus; the instruments were taught to stop reporting them, and the baseline file that says so is not guarded.

## Moves

- flip the two zero-mode corpus verdicts in verify_corpus_integrity.py
- flip its self-test arm that pinned the zero-mode verdict (1 line)
- drop the two counts from violations() in verify_corpus_independent.py
- bless the five DRIFT values in verifiers/corpus-baseline.json (unguarded file)
- honest fixes for the other two gates: two Gate-registry rows for check_r69_routed_repairs_v2.py and check_skill_evals_v2.py in SKILL.md (two prose line joins keep the 600-line budget), and the stale checklist self-test arm corrected to the live PASS

## Observed battery (six frozen commands, run in a fleet-shaped sandbox)

| gate | command | exit | wall |
|---|---|---|---|
| check_gate_registry | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | 0 | 0s |
| check_assertion_floors | `python3 -B verifiers/check_assertion_floors.py` | 0 | 43s |
| verify_skill_checklist | `python3 -B verifiers/verify_skill_checklist.py` | 0 | 1s |
| verify_corpus_integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 0 | 1s |
| verify_corpus_independent | `python3 -B verifiers/verify_corpus_independent.py` | 0 | 0s |
| check_correction_sweep | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | 0s |

**N = 6 of 6.**

## Guard reading (recomputed by guards.py over base..world_rev)

- no-deletions: pass 
- floors: pass 
- instrument-size: added 8 / removed 8 (cap 40); added-only reading pass, two-direction reading pass
- spotcheck-identity: pass 

**Guard that catches this world:** NOTHING: reads 6 of 6 and passes all four guards

## The counter draft on this world

```
measured rev 25b059d2fa62bec7fddb02dd176db53952982f33 in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 0; floors 15 rows; instruments added 8 / deleted 8 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.3s
gate verifiers/check_assertion_floors.py exit 0 wall 39.1s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.4s
gate verifiers/verify_corpus_integrity.py exit 0 wall 0.2s
gate verifiers/verify_corpus_independent.py exit 0 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 42.1s
tip battery exit 0: 6 of 6
counter exit=0
```

## Replay

```sh
sh replay.sh        # fresh fleet-shaped sandbox, six gates, guards; removed after
KEEP=1 sh replay.sh # keeps the sandbox path
```

`apply.sh` clones the base `c69711ee08279609374d895bb0f3c8c18ccf15c9` with `--shared` into a parent that symlinks every fleet-root entry, applies `world.patch`, commits inside the sandbox only, and prints the world revision.
