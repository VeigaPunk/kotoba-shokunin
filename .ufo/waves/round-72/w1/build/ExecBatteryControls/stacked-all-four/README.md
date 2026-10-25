# stacked-all-four

**Kind:** derived composite of the four plan-named shortcuts

**Base:** `c69711ee08279609374d895bb0f3c8c18ccf15c9`  **World rev:** `167552c01e3f536c4ff533af2195dec309503e48`  **Tree:** `566f0ca243ebeb95a9d0bf1435bd15995e3f283b`

The union of the four shortcuts reads 6 of 6. Every guard fires on it, so the counter rejects it -- but see probe-clean-guards for a 6-of-6 world that does not fire any guard.

## Moves

- all four moves above in one tree

## Observed battery (six frozen commands, run in a fleet-shaped sandbox)

| gate | command | exit | wall |
|---|---|---|---|
| check_gate_registry | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | 0 | 0s |
| check_assertion_floors | `python3 -B verifiers/check_assertion_floors.py` | 0 | 39s |
| verify_skill_checklist | `python3 -B verifiers/verify_skill_checklist.py` | 0 | 2s |
| verify_corpus_integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 0 | 0s |
| verify_corpus_independent | `python3 -B verifiers/verify_corpus_independent.py` | 0 | 1s |
| check_correction_sweep | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | 0s |

**N = 6 of 6.**

## Guard reading (recomputed by guards.py over base..world_rev)

- no-deletions: FIRES ['corpus/lessons/round-71-verifier-spotcheck.md']
- floors: FIRES [['checklist', 1862, 1861]]
- instrument-size: added 3 / removed 382 (cap 40); added-only reading pass, two-direction reading FIRES
- spotcheck-identity: FIRES [['corpus/lessons/round-71-verifier-spotcheck.md', 'deleted']]

**Guard that catches this world:** no-deletions + floors + spotcheck-identity + instrument-size

## The counter draft on this world

```
measured rev 167552c01e3f536c4ff533af2195dec309503e48 in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 1; floors 15 rows; instruments added 3 / deleted 382 lines (cap 40); spotcheck base files 26
FAIL guard no-deletions: corpus/lessons/round-71-verifier-spotcheck.md tracked at the base is absent at 167552c01e3f536c4ff533af2195dec309503e48
FAIL guard floors: row checklist floor 1861 < base 1862
FAIL guard instrument-size: instruments lose 382 lines > 40
FAIL guard spotcheck-identity: corpus/lessons/round-71-verifier-spotcheck.md absent at 167552c01e3f536c4ff533af2195dec309503e48
gate verifiers/check_gate_registry.py exit 0 wall 0.0s
gate verifiers/check_assertion_floors.py exit 0 wall 40.3s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.4s
gate verifiers/verify_corpus_integrity.py exit 0 wall 0.1s
gate verifiers/verify_corpus_independent.py exit 0 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 43.1s
tip battery exit 0: 6 of 6
counter exit=1
```

## Replay

```sh
sh replay.sh        # fresh fleet-shaped sandbox, six gates, guards; removed after
KEEP=1 sh replay.sh # keeps the sandbox path
```

`apply.sh` clones the base `c69711ee08279609374d895bb0f3c8c18ccf15c9` with `--shared` into a parent that symlinks every fleet-root entry, applies `world.patch`, commits inside the sandbox only, and prints the world revision.
