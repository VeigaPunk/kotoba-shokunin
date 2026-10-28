# Kb81E11Receipts — independent receipt re-derivation (round 81, w1)

Seat: executor, leaf. Axis worked: calibration/consistency evidence — an INDEPENDENT second
derivation of the base gate truths, for comparison against the BatteryRunner (Kb81E10Battery),
seat Kb81S06Shonen's base receipts and the plan.

## What I did

Own driver, no E10 receipts copied and no E10 runner read or called (I read the *r80* runner
that the L1 brief names as the port source, to recover the battery's gate list and argv shape).
Scratch clone of the lane at `b284223105f4d106f7e8f56ed4fd296c643cda0e`, made fleet-shaped the
same way the round-79 F1 finding requires: the clone is named `kotoba-shokunin` and every other
fleet entry is a symlink beside it (`/fast/scratch/hyaku/kotoba-r81/Kb81E11Receipts/world/kotoba-shokunin`).

Every command was run as `bash -c '<cmd>' >> <receipt> 2>&1; rc=$?` from the world lane root and
the receipt's last line is that command's own exit status (M80-1). The `| tail -40` on the driver
invocation trimmed only the printed summary; no verdict was read from a pipeline.

Environment: Python 3.14.8, git 2.56.0 (receipt block 19). Lane HEAD == base
`b284223105f4d106f7e8f56ed4fd296c643cda0e`; fleet HEAD `8566072e04f235b23b48786cbb61589837017c97`
(working tree dirty — block 21). No tool installed or upgraded (nothing was missing); pacman not run.

## The six battery gates at the base — my reading

| # | command (from the world lane root) | exit | headline |
|---|---|---|---|
| 01 | `python3 -B verifiers/check_gate_registry.py --rev b2842231…` | **0** | `gate registry rows conformant 63 of 63 lane verifiers; phantom 0` |
| 02 | `python3 -B verifiers/check_assertion_floors.py` | **0** | 17 `PASS` rows (`floors_guard observed=165 floor=150`, etc.) |
| 03 | `python3 -B verifiers/verify_skill_checklist.py --json` | **0** | `pass 11, fail 0, na 0`; 596 lines within budget 600 |
| 04 | `python3 -B verifiers/verify_corpus_integrity.py --json` | **1** | `4/9 checks pass`; DRIFTs `tracked_files 155≠154`, `unindexed 1`, `report_total 111≠109`, `report_dead 1`, `commit_unresolvable 2` |
| 05 | `python3 -B verifiers/verify_corpus_independent.py --json` | **1** | DRIFTs `corpus.index.unindexed 1`, `corpus.pointers.commit_unresolvable 2`; **`report_dead 0`** |
| 06 | `python3 -B verifiers/check_correction_sweep.py --root .` | **0** | `correction sweep: 0 stale block(s)` |

4 of 6 gates exit 0 — consistent with the committed base line `guards 5 of 5; tip battery exit 0: 4 of 6`
(`.ufo/waves/round-81/receipts/tipbattery-base-dot.txt`). Blocks 07–10 repeat the cheap gates with
explicit `--repo <world>` / `--json` / `--root <world>` and read identically, so the default repo
resolution (`Path(__file__).parent.parent`) is the world clone, not the lane.

I did **not** run `check_tip_battery.py` (not my item, ~105 s): my 4-of-6 gate-exit sum is
*consistent with* the plan's base `exit 1`, and does not by itself measure the counter's status.

### cat-file existence probes (the r77/r76 report split)

| # | command | exit | meaning |
|---|---|---|---|
| 11 | `git -C <lane> cat-file -e HEAD:.ufo/reports/round-77/kotoba.md` | **128** (fatal: path does not exist in 'HEAD') | the r77 report is **not** in the lane |
| 12 | `git -C <lane> cat-file -e HEAD:.ufo/reports/round-76/kotoba.md` | **0** | r76 is in the lane |
| 13 | `git -C <fleet> cat-file -e HEAD:.ufo/reports/round-77/kotoba.md` | **0** | the r77 report object resolves in the fleet |
| 14 | `git -C <fleet> cat-file -e HEAD:.ufo/reports/round-76/kotoba.md` | **0** | fleet has r76 too |

All four match the expected `128 / 0 / 0 / 0`. Block 13 is the positive evidence for R1: the
object expression `HEAD:.ufo/reports/round-77/kotoba.md` is resolvable today, in the fleet root,
which is exactly the hop the integrity gate's pointer model lacks.

## Where the readings disagree

**D1 — plan § Trigger vs measured bytes (independent gate's report arm).** The plan says
`verify_corpus_independent.py` exits 1 "on the same `commit_unresolvable` 2 plus `report_dead` 1".
Measured at `b2842231`: exit 1, `pointers.report_dead = 0`, `report_dead_detail = []`,
`report_total = 111` (INFO); the red arms are `corpus.index.unindexed 1` and
`corpus.pointers.commit_unresolvable 2`. Mechanism, proved in block 20b:

- `verify_corpus_integrity.py` keeps the raw token `HEAD:.ufo/reports/round-77/kotoba.md`;
  `report_pointer_exists()` returns **False** because the token does not start with `.ufo/reports/`
  and its path resolution lands on `corpus/lessons/HEAD:.ufo/reports/…` → `report_dead 1`.
- `verify_corpus_independent.py` tokenizes the same line as `.ufo/reports/round-77/kotoba.md`
  (rev prefix stripped), which is then found at the fleet root: the fleet working-tree file is
  8547 bytes and contains `## SHONEN` → **green**.

Consequence for the repair set as written: R1 (report-pointer object resolution + content
identity) is scoped to `verify_corpus_integrity.py` only. The independent gate is not merely
unaffected — its pointer predicate never inspects the `<rev>:<path>` object expression at all,
and resolves existence against the **fleet working tree**; so the r80 W10 class (marker at the
report path) is invisible to that gate, and a plan line that credits the independent gate with
`report_dead 1` at base is not supported by these bytes. I did not repair it (patch seat, not
mine); it is a design finding for the R1 owner and the C1 critics.

Cross-checks: no seat disagrees with my six-gate figures. `w1/Kb81S06Shonen.md:47,50` reads the
same registry 63/63 and the same integrity `4/9` + five DRIFTs; `w1/Kb81S08ReadmeRows.md:39`
reads independent `rc=1; unindexed 1, commit_unresolvable 2, report_dead 0`; E10's in-flight
`build/base-battery/03-gate-registry.txt` ends `exit=0`, `63 of 63` (block 04 was still writing at
my read). `w1/Kb81K02Patterns.md:7` independently found the same plan-vs-measurement divergence
(M103); my artifacts are the second, receipted derivation of it, not a copy of that report.

**D2 — the base receipt set named by the plan is incomplete.** Plan § Trigger cites
`.ufo/waves/round-81/receipts/` as the base gate-truth evidence. At my write time that directory
holds `tipbattery-base-dot.txt` and `census-before.txt` only; there is no gate-level receipt and no
`exit=` line for the counter there (S02's M81-2 reads the same gap). My published file supplies
the six gate-level exits with own-exit capture, which is what the comparison against E10 needs.

## Risks / operability notes

- **The corpus gates' fleet hop is mutable external state.** `FLEET_ROOT` is hardcoded to
  `/home/vgpnk/Projects/shokunin` in both gates, and the hop is `is_file()`/`os.path.isfile()` on
  that **working tree** — not a git object, not the measured rev. At my run the fleet tree was
  dirty (`M .ufo/reports/round-58/chousa.md`, untracked `.scratch/closure-mado-r50.json`,
  `.scratch/source-routing-queue.md`, `o.bin`) and its HEAD is not the base. A lane verdict
  therefore depends on bytes outside the measured commit; R1's content-identity arm strengthens
  that dependence (it will read the fleet file's `## SHONEN`/size), and the attacker-controlled
  fleet copy is the residual hole (K02's W12 prediction). Recorded, not repaired.
- Both fleet report files already satisfy R1's proposed identity at base (r76: 8128 B, r77:
  8547 B, both contain `## SHONEN`, block 20b) — so the identity arm is satisfiable without any
  lane commit; the discriminating power comes from the marker case only.
- Fleet working tree modified by others, untouched by me: every git call in this seat was
  read-only, and my only writes are under `.ufo/waves/round-81/`.

## Evidence

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E11Receipts.txt`
= 1288 lines, 43937 bytes, sha256 `9c0031f75411121eee901963ab1450b96d79d27e47838b6848ae7b4ecaf6280a`.
One block per command (command, cwd, UTC, verbatim stdout+stderr, own `exit=`), 22 blocks:
01–06 the six gates, 07–10 explicit-argv identity arms, 11–14 the cat-file probes, 15–18 HEAD /
version context, 19 toolchain, 20a a probe attempt that failed on my own wrong helper name (kept
for honesty), 20b the corrected pointer-model probe, 21 the fleet working-tree listing.
Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E11Receipts` was removed after publication.

VERDICT: base gate truths independently confirmed (registry 0, floors 0, checklist 0, integrity 1, independent 1, correction 0 = 4 of 6; lane/fleet cat-file 128/0/0/0), with one plan disagreement: the independent gate reads `report_dead 0` at base, not 1 — the only red report arm is the integrity gate's unparsed `HEAD:`-prefixed token.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E11Receipts.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E11Receipts.md
