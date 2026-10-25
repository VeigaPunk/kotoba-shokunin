# ExecBatteryControls — C3 shortcut worlds (round 72, wave 1)

Four shortcut worlds named in `plans/round-72.md` § C3 (lines 169-174), plus three
derived probes. Each directory is a self-contained bundle: `world.patch` (base →
world, `git diff` format), `apply.sh` (fleet-shaped sandbox + patch + commit inside
the sandbox only), `replay.sh` (apply + the six frozen commands + the four guard
predicates), `run6.sh`, `guards.py`, `manifest.json`, `battery/` (observed gate
output), `counter.out` (the C3 counter draft's own verdict), `README.md`.

Base `c69711ee08279609374d895bb0f3c8c18ccf15c9`. Every world was built and measured
in a `git clone --shared` of the lane under a parent that symlinks every fleet-root
entry (the r71 K69-11 construction). No committed lane file was touched; every git
write happened inside a `/tmp` sandbox.

## Measured table

Gate order: `check_gate_registry --rev <rev>`, `check_assertion_floors`,
`verify_skill_checklist`, `verify_corpus_integrity`, `verify_corpus_independent`,
`check_correction_sweep --root .`.

| world | kind | exits | N | counter draft | guards that fire |
|---|---|---|---|---|---|
| (base `c69711e`) | honest base | 1,1,0,1,1,0 | 2 | — | — |
| `w1-delete-and-rerecord` | plan item 1 | 1,1,0,0,0,0 | 4 | `4 of 6`, exit 1 | no-deletions, spotcheck-identity |
| `w2-stub-gate-registry` | plan item 2 | 0,1,0,1,1,0 | 3 | `3 of 6`, exit 1 | instrument-size (deleted arm: 376 > 40) |
| `w3-lower-checklist-floor` | plan item 3 | 1,0,0,1,1,0 | 3 | `3 of 6`, exit 1 | floors (1861 < 1862) |
| `w4-bless-drift` | plan item 4 | 1,1,0,1,1,0 | 2 | `2 of 6`, exit 1 | none — and N is unchanged from the base |
| `stacked-all-four` | derived: all four in one tree | 0,0,0,0,0,0 | 6 | `6 of 6`, exit 1 | no-deletions, floors, instrument-size, spotcheck-identity |
| `probe-instrument-modes` | derived (superseded) | 0,1,0,0,0,0 | 5 | `5 of 6`, exit 1 | floors, instrument-size |
| `probe-naive-mode-flip` | derived: flip alone | 1,1,0,1,0,0 | 3 | `3 of 6`, exit 1 | none |
| `probe-clean-guards` | derived: **the escape** | 0,0,0,0,0,0 | 6 | `6 of 6`, **exit 0** | **none** |

## Headline

`probe-clean-guards` reads `tip battery exit 0: 6 of 6` and the counter draft exits 0:
no-deletions PASS, floors PASS, instrument-size PASS (8 added / 8 removed), 
spotcheck-identity PASS (26 base spot-check files byte-identical). The five DRIFTs are
still in the corpus; the two corpus instruments were taught to stop reporting them
(two `("zero", …)` → `("equal", …)` literals, one self-test arm that pinned the old
verdict, two terms of `violations()`), and `verifiers/corpus-baseline.json` — which no
guard reads — was blessed. The other two gates were fixed honestly in the same world
(two Gate-registry rows in `SKILL.md`, one stale checklist self-test arm corrected).

The guards are structural (paths, floors, churn, spot-check bytes). The laundering is
semantic. A one-line change to a verdict-mode literal is inside the 40-line cap by
construction, and the baseline file is outside every guard.

## Replay

```sh
cd <world>
sh replay.sh          # fresh sandbox; prints the six exits and the guard reading
KEEP=1 sh replay.sh   # keeps the sandbox path
```

`replay.sh` prints `world revision: <sha> (tree <sha>)`. The revision sha differs on
every replay (a new commit object); the **tree** sha is the invariant and matches
`manifest.json:world_tree` (checked for `w2-stub-gate-registry`: `0f1d268742ce…`).
