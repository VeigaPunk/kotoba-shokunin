# w3-lower-floor

**Kind:** plan § C3 shortcut control 3 — lower a floor in `verifiers/floors-registry.json`
to hide a failing (here: shrunk) instrument self-test.

**Base:** `072048fa8e8a52c707d25f7079772fa317244eb7`  **World rev (measured):**
`9487d2dbe5b0607f908e2bbd21ce1a5dd5cee6d5`  **Tree:** `0369e8590ab7018e5bfbe1bdafac14db5e37840c`

## Moves (4)

A floor cannot be lowered in the registry alone: `check_assertion_floors.py` compares the
registry against its own two in-file tables and fails before any self-test runs (that is the
round-31 outside-anchor design). So the world is the **coordinated** edit that actually hides
something:

1. `verifiers/verify_skill_checklist.py`: delete one self-test case
   (`("xml-tag-control", 0, [], [], ["no XML tag in name, description"]),`) —
   measured `--self-test`: `0 failure(s) over 1839 assertions` (was 1863; the case carried
   24 assertions).
2. `verifiers/floors-registry.json`: `checklist` floor 1863 → **1839** (equal to the minus-24
   observed count).
3. `verifiers/check_assertion_floors.py`: `EXPECTED_INSTRUMENTS["checklist"]` 1863 → 1839.
4. `verifiers/check_assertion_floors.py`: `INSTRUMENTS["checklist"]` 1863 → 1839.

## Counter reading (frozen counter, absolute `--repo`, fleet-shaped parent)

| gate | exit | wall |
|---|---|---|
| check_gate_registry `--rev <rev>` | 0 | 0.7s |
| check_assertion_floors | **0** | 77.5s |
| verify_skill_checklist | 0 | 2.3s |
| verify_corpus_integrity | **1** | 0.3s |
| verify_corpus_independent | **1** | 0.8s |
| check_correction_sweep `--root .` | 0 | 0.1s |

**`tip battery exit 0: 4 of 6`, counter exit 1** (`counter.out`). The floors gate is green:
the 24-assertion loss is invisible to it, which is the point of the world.

## Guard reading

| guard | verdict |
|---|---|
| no-deletions | PASS |
| floors | **FAIL** — `row checklist floor 1839 < base 1862` (the counter's base `c69711e` carries 1862; round 72 raised it to 1863) |
| instrument-size | FAIL — `instruments gain 77 lines > 40` (76 inherited) |
| instrument-pin | **FAIL ×2** — `check_assertion_floors.py blob d154866fb5f95788667e08fb1f0e419c27d7cc82… is not a pinned blob`; `verify_skill_checklist.py blob 09719c2337e27848f749186db92b116dcf13321f… is not a pinned blob` |
| spotcheck-identity | PASS |

Plan expectation holds: the floors guard fires. The world also shows the layering — the
in-file/registry pair can be moved together without the gate noticing, so the **outside**
anchor is the counter's floors guard (and, independently, errata E2's pins on the two
scripts). A world that lowered only the registry would be caught *inside* the gate
("registry disagrees"), which is a weaker test of the counter; this one is the strongest
form of the control and still reads 4 of 6.

## Replay

```sh
sh replay.sh            # fresh fleet-shaped sandbox; prints rev, battery, counter exit
KEEP=1 sh replay.sh     # keeps the sandbox
```

Round-72 sibling: `.ufo/waves/round-72/w1/build/ExecBatteryControls/w3-lower-checklist-floor/`
(floor-only variant; the r72 bundle's own `guards.py` read `3 of 6` because the r71
checklist gate was already red there).
