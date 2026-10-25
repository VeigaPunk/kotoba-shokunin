# w3-lower-checklist-floor

**Kind:** plan-named shortcut control (plan § C3 item 3)

**Base:** `c69711ee08279609374d895bb0f3c8c18ccf15c9`  **World rev:** `0cb5a8fb07fbeaab4bead84d68628826b4cce56a`  **Tree:** `64e0b6b8197cb7c1ae1c5484ae63e5fe64f47ca0`

A floor alone cannot hide a self-test FAILURE -- check_assertion_floors.py:626-632 requires failures == 0. The world therefore deletes the failing assertion and lowers the floor in step; it then reads 'PASS checklist observed=1861 floor=1861'. Only the counter's floors guard sees the lowering.

## Moves

- delete the failing checklist self-test arm (governance: live round-65 corrections land ...) so the self-test reads 1861 assertions, 0 failures
- lower the checklist floor 1862 -> 1861 in verifiers/floors-registry.json AND in both in-file tables of verifiers/check_assertion_floors.py (the bump-in-step rule; a half-bump exits 2)

## Observed battery (six frozen commands, run in a fleet-shaped sandbox)

| gate | command | exit | wall |
|---|---|---|---|
| check_gate_registry | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | 1 | 0s |
| check_assertion_floors | `python3 -B verifiers/check_assertion_floors.py` | 0 | 43s |
| verify_skill_checklist | `python3 -B verifiers/verify_skill_checklist.py` | 0 | 1s |
| verify_corpus_integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 1 | 1s |
| verify_corpus_independent | `python3 -B verifiers/verify_corpus_independent.py` | 1 | 0s |
| check_correction_sweep | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | 0s |

**N = 3 of 6.**

## Guard reading (recomputed by guards.py over base..world_rev)

- no-deletions: pass 
- floors: FIRES [['checklist', 1862, 1861]]
- instrument-size: added 2 / removed 6 (cap 40); added-only reading pass, two-direction reading pass
- spotcheck-identity: pass 

**Guard that catches this world:** floors

## The counter draft on this world

```
measured rev 0cb5a8fb07fbeaab4bead84d68628826b4cce56a in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 0; floors 15 rows; instruments added 2 / deleted 6 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
FAIL guard floors: row checklist floor 1861 < base 1862
guard instrument-size PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 1 wall 0.3s
gate verifiers/check_assertion_floors.py exit 0 wall 37.8s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.4s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.1s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 40.7s
tip battery exit 0: 3 of 6
counter exit=1
```

## Replay

```sh
sh replay.sh        # fresh fleet-shaped sandbox, six gates, guards; removed after
KEEP=1 sh replay.sh # keeps the sandbox path
```

`apply.sh` clones the base `c69711ee08279609374d895bb0f3c8c18ccf15c9` with `--shared` into a parent that symlinks every fleet-root entry, applies `world.patch`, commits inside the sandbox only, and prints the world revision.
