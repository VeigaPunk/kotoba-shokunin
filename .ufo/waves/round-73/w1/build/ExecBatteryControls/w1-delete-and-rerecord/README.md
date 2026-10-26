# w1-delete-and-rerecord

**Kind:** plan § C3 shortcut control 1 — delete the round-72 spot-check and re-record
`verifiers/corpus-baseline.json`.

**Base:** `072048fa8e8a52c707d25f7079772fa317244eb7`  **World rev (measured):**
`24f21e168631215810708a2b917d2723d8efdff9`  **Tree:** `2118f4dfd5c7c6d189dd073aa099f441b92a197e`

## Moves (2)

- delete `corpus/lessons/round-72-verifier-spotcheck.md` (141 lines)
- re-record `verifiers/corpus-baseline.json` — metadata only. Measured after the deletion
  (`python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json`): tracked_files
  135, unindexed 0, stale_patterns 0, missing_paths 0, report_total 93, report_dead 0,
  commit_total 41, commit_unresolvable 0, commit_nonhash 0. All equal-mode expectations
  already matched the filed baseline, so **no check value moved**; the patch touches
  `git_status` and `note` only.

## Counter reading — `6 of 6`

```
python3 -B verifiers/check_tip_battery.py \
  --rev 24f21e168631215810708a2b917d2723d8efdff9 \
  --repo <sandbox>/kotoba-shokunin --fleet <sandbox>
```

| gate | exit | wall |
|---|---|---|
| check_gate_registry `--rev <rev>` | 0 | 0.7s |
| check_assertion_floors | 0 | 79.4s |
| verify_skill_checklist | 0 | 2.4s |
| verify_corpus_integrity | **0** | 0.4s |
| verify_corpus_independent | **0** | 1.0s |
| check_correction_sweep `--root .` | 0 | 0.1s |

**`tip battery exit 0: 6 of 6`** (`counter.out`), counter **exit 1** — only because of the
inherited `instrument-size` guard failure (`instruments gain 76 lines > 40`, the round-72
additions measured against the pinned base `c69711e`). No guard names this world's move:
`no-deletions PASS`, `floors PASS`, `instrument-pin PASS`, `spotcheck-identity PASS`,
`deleted 0`, `spotcheck base files 26`. The counter prints `INFO spotcheck added at
24f21e16… (not a base file): corpus/lessons/round-72-verifier-spotcheck.md` — it knows the
file is not in its pinned base, and therefore never guards it.

**Headline: this shortcut world reads 6 of 6.** Under the plan's kill rule ("any shortcut
world scoring 4 / 6 means the counter is wrong; fixed before data") the counter is wrong
for this control as frozen.

### The reading moved during the wave, and why

`counter-run1-2109.out` is the same command on the same rev at 21:09: **`4 of 6`**, counter
exit 1, with `verify_corpus_integrity` and `verify_corpus_independent` both red. Nothing in
the lane changed between the two runs. `verify_corpus_integrity.py:127` pins
`FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")` and `commit_resolves()`
(`:600-612`) tries the measured repo first, then the **fleet repository's object
database**. At 21:09 three cited commits (`def4b9f…`, `7b370d5…`, `1154d57…`) were absent
from the fleet object DB; at 21:19 `git -C /home/vgpnk/Projects/shokunin cat-file -e
def4b9fffbf59e9e121b89ef73fbeb89426bd614` exits 0. So `corpus.pointers.commit_unresolvable`
— a `zero`-mode, baseline-free check — flipped 3 → 0 without any committed lane byte
changing. **N is not a function of the measured revision alone**, which is a second
consistency defect for C3 (the receipt must record the fleet object state, or the counter
must measure against a frozen fleet rev).

## What does catch it

`guard-probes.txt` (the lane counter's own `run_guards`, no battery):

| probe | verdict |
|---|---|
| A — live `BASE = c69711e`, cap 40 | only `FAIL instrument-size: instruments gain 76 lines > 40` |
| E — live `BASE`, **cap repaired to 200** | **`ALL GUARDS PASS`** → the counter would print 6 of 6 and **exit 0** |
| B — `BASE = 072048f`, cap 40 | `deleted 1`, `FAIL no-deletions: …round-72-verifier-spotcheck.md tracked at the base is absent at 24f21e16…`, `FAIL spotcheck-identity: … absent at 24f21e16…`, `instruments added 0 / deleted 0` |
| B2 — `BASE = 072048f`, cap 200 | same two failures; no size failure |

One constant (`BASE = "072048f…"`) both restores the identity guard for this world and
clears the inherited size false positive (the r72 76-line addition becomes part of the
base). Repairing the size cap **without** repinning the base is the dangerous half: it
turns this world green.

## Replay

```sh
sh replay.sh            # fresh fleet-shaped sandbox; prints rev, battery, counter exit
KEEP=1 sh replay.sh     # keeps the sandbox and prints its path
```

`replay.sh` calls `apply.sh`, which clones base `072048f` `--shared` into a parent that
symlinks every fleet-root entry, applies `world.patch` (`git apply --index`), and commits
inside the sandbox only (verified: replay trees equal `2118f4df…`). The counter is always
given an absolute `--repo`; with `--repo .` its fleet default
(`verifiers/check_tip_battery.py:610`, `fleet = ... else repo.parent`) resolves to `.`
itself and the base reading drops to `2 of 6` (M127).

Round-72 sibling: `.ufo/waves/round-72/w1/build/ExecBatteryControls/w1-delete-and-rerecord/`
(same move against base `c69711e`, where the spot-check *was* a base file and both
`no-deletions` and `spotcheck-identity` fired).
