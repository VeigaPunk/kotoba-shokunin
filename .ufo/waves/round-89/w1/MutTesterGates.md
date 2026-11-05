# MutTesterGates — round 89 (r89-w1) mutation of the two new instruments

Seat: MutTesterGates (attack, mutation-tester). Lane tip measured: `0f2b866` (wave dispatch commit; the
lane's committed base for this round, with the wave's uncommitted instrument files present in the
scratch copy). Scratch only: `/fast/scratch/hyaku/kotoba-r89/MutTesterGates/`. The lane was read, never
written. No lane file was edited; no git write was run.

## Measure (Q47, two-sided)

- Killed = the mutant changes a committed fixture's observed exit away from the frozen predicate
  (freeze gate: `fixed` → 0, `r88-controls.md` → 1, `--self-test` → 0 with `0 failure(s)`; D5 v3:
  the six worlds against the frozen exit ladder). A self-test-only kill is recorded as such.
- Equivalent = a semantics-preserving rewrite; must survive (every honest exit unchanged).
- Tables: `.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv` and `equivalents.tsv`.
- Transcripts: `.ufo/waves/round-89/w1/MutTesterGates/transcripts/` (every run: fixture or world, exit, stdout).
- Mutant sources: `.ufo/waves/round-89/w1/MutTesterGates/mutants/{fg,d5}/`. Harness:
  `.ufo/waves/round-89/w1/MutTesterGates/harness.py` (re-runnable in any scratch copy).
- Base receipt measured at the pristine copy: `.ufo/waves/round-89/w1/MutTesterGates/receipts/d5v3-base-receipt.json`.

## Pristine baselines (both instruments, unmutated)

| Instrument | Probe | Observed |
|---|---|---|
| `check_freeze_gate.py` | `--self-test` | `0 failure(s) over 30 assertions`, exit 0 |
| `check_freeze_gate.py` | `--plan r88-controls-fixed.md` | exit 0 |
| `check_freeze_gate.py` | `--plan r88-controls.md` | exit 1 (refuses `w_added_red`) |
| `check_r86_routed_repairs_v3.py` | `--self-test` | `0 failure(s) over 33 assertions`, exit 0 |
| `check_r86_routed_repairs_v3.py` | world `w_tip` / `w_healed` | exit 0, `closed 5 of 5`, `instance drift 0` |
| same | `w_added_instance` / `w_silenced` / `w_rerecorded` / `w_newname` | exit 1 each (`closed 4 of 5`, `drift 2/0/0/1`) |
| same | Q79 equivalence: lane working tree vs base clone, integrity observation dict | identical (`True`) |
| same | lane tip, working tree (`--root` = lane copy) | exit 0, `closed 5 of 5`, `instance drift 0` |

Worlds were built as shallow clones of the lane copy with one committed edit each:
`w_added_instance` appends `commit \`0123…4567\`` (unresolvable) to a lesson; `w_healed` replaces the
dead commit in `corpus/lessons/round-81.md:8` with HEAD; `w_silenced` deletes the `commit_nonhash`
line from the integrity `CHECKS` table; `w_rerecorded` re-records the three equal-mode expects to the
base observed values; `w_newname` appends `commit \`not-a-hash-token\`` (a new DRIFT name).
Each world's DRIFT set was checked against the expected verdict before the matrix ran.

## Declared mutants — results

### Freeze gate (`verifiers/check_freeze_gate.py`)

| Mutant | Killed by | Observed exit before → after (fixed / unsat / self-test) |
|---|---|---|
| expectation sign flip, exit clause (`!=` → `==`) | fixture `fixed` 0→1, self-test 0→1 | 0/1/0 → 1/1/1 |
| expectation sign flip, stdout clause (`not in` → `in`) | fixture `fixed` 0→1, self-test 0→1 | 0/1/0 → 1/1/1 |
| control-skip, `w_added_red` not run | fixture `unsat` 1→0, self-test 0→1 | 0/1/0 → 0/0/1 |
| control-skip, last control not run (`controls[:-1]`) | **self-test only** (0→1); both committed fixtures unchanged | 0/1/0 → 0/1/1 |
| exit ladder: refusal returns 2 | fixture `unsat` 1→2, self-test 0→1 | 0/1/0 → 0/2/1 |
| exit ladder: could-not-evaluate returns 1 | **self-test only** (0→1); no committed fixture reaches the eval rung | 0/1/0 → 0/1/1 |
| parse drops `stdout contains` clause | fixture `unsat` 1→0, self-test 0→1 | 0/1/0 → 0/0/1 |
| parse drops `exit` clause (extra, not declared) | **self-test only** | 0/1/0 → 0/1/1 |
| duplicate-name acceptance (must stay exit 3) | **not killed — see Finding F1** | duplicate-name plan: exit 0 (`2 control(s) held`), expected exit 3 |

### D5 v3 (`verifiers/check_r86_routed_repairs_v3.py`)

Worlds listed in the order w_tip, w_healed, w_added_instance, w_silenced, w_rerecorded, w_newname.
Expected exits 0, 0, 1, 1, 1, 1.

| Mutant | Killed by | Observed exit before → after |
|---|---|---|
| d5iii removed (leg PASS and K = 0) | `w_added_instance` 1→0 | 0,0,1,1,1,1 → 0,0,0,1,1,1 |
| d5iii leg forced PASS, K kept (extra) | **SURVIVED at exit** (K independently refuses); N line prints `5 of 5` on `w_added_instance` while exit is 1 | 0,0,1,1,1,1 → 0,0,1,1,1,1 |
| digest check removed (`snap_ok = True`) | `w_rerecorded` 1→0 | 0,0,1,1,1,1 → 0,0,1,1,0,1 |
| subset flipped to superset | `w_healed` 0→1 (false red on a healed red) | 0,0,1,1,1,1 → 0,1,1,1,1,1 |
| instance comparison, non-growth made strict (`>` → `>=`) | `w_tip` 0→1, `w_healed` 0→1 | 0,0,1,1,1,1 → 1,1,1,1,1,1 (K = 8 or 9 on every world) |
| D1–D4 dropped from the counter | `w_tip` 0→1, `w_healed` 0→1 | 0,0,1,1,1,1 → 1,1,1,1,1,1 (`closed 1 of 5` at the honest tip, was 5) |

Interpretation notes: "instance comparison `<` instead of `<=`" was read as the non-growth test
`observed <= receipt`; the mutant makes it strict (`observed < receipt`, so an equal value counts as
growth). The mutant that the frozen text would reject as a `<`-for-`<=` slip is the one that reds the
honest tip; this is what the seat asked to see. The leg-only variant of d5iii (second row) is a
measured redundancy: the K term (`instance drift`) refuses independently, so the exit is unchanged,
but the printed `r86 routed defects closed` line disagrees with the exit (`5 of 5` with exit 1).

## Equivalents — all survive (exit codes unchanged on every honest fixture)

| Equivalent | Fixture set | Result |
|---|---|---|
| FG rename local `problems` → `issues` | fixed/unsat/self-test | survives (0/1/0) |
| FG reformat expect-line parser (same grammar, multi-line form) | fixed/unsat/self-test | survives (0/1/0) |
| FG move helper `_one_line` after the parser class | fixed/unsat/self-test | survives (0/1/0) |
| FG plan: reorder controls (fixed; `w_added_red` moved last in unsat) | committed plans | survives (0 / 1) |
| FG plan: reformat expect line (extra spaces, `exit    0 ;  stdout   contains   …`) | committed plans | survives (0 / 1) |
| D5 reorder D1–D4 loop | six worlds | survives (exits as pristine) |
| D5 rename locals (`grew`, `mdrift`) | six worlds | survives |
| D5 move helper `growth_names` before `main` | six worlds | survives |

The seat's "reorder the controls dict" has no dict in either instrument; the nearest analogue was
reordering the controls of the committed fixture plans, and that was done. "Reformat the expect-line
parser" applies to the freeze gate only; D5 has no expect-line grammar (N/A on D5).

## Findings

**F1 — duplicate control names are accepted (exit 0), not refused (exit 3). Freeze gate, C1 arm gap.**
`--plan` on a block with `- control w_tip:` declared twice runs both, reports `freeze gate: 2 control(s)
held — freeze may proceed`, exit 0. The plan's frozen spec lists the invalid-spec cases (no command, no
expectation, empty block) and does not list duplicates, and no self-test arm exercises them. So the
seat's "must stay exit 3" is not what the pristine instrument does. The duplicate-name mutant is
therefore not a kill but a live spec gap. Not rescued here (ExecFreezeGate owns the file; the predicate
is frozen). Route to the L1: either add a duplicate-name arm and an exit-3 refusal in a pre-score
addendum, or record the gap as a known limit of C1.

**F2 — three freeze-gate mutants are killed by self-test arms only, not by committed fixtures.**
`control-skip (last control)` and `exit ladder: eval rung → 1` (and the extra `exit`-clause drop) leave
both committed plans at their frozen exits; only the self-test arms catch them. The frozen battery's
"each killed = a committed fixture changes verdict" is therefore not met for these three. The C1
headline still rests on the self-test for the eval rung. Route: a fixture that reaches the eval rung
and one whose refusal is on the last control would make the committed plans discriminate those arms.

**F3 — leg-only d5iii removal is invisible at the exit code (redundancy with K).**
With the d5iii leg forced PASS but K kept, `w_added_instance` still exits 1 and the printed count reads
`closed 5 of 5`. A reader of the printed line alone would see a green count on a red exit. The exit
ladder itself is correct; the report line is the surface that disagrees. Not a predicate defect, but
worth noting to the reviewer as a reading hazard.

**F4 — the d5iii removal and digest removal are each caught by exactly the world the seat named.**
`w_added_instance` (d5iii) and `w_rerecorded` (digest) flip to exit 0 under their mutants. `w_healed`
catches the superset flip (a healed red reads as a new name). `w_tip` and `w_healed` catch the
strict-comparison and D1–D4-dropped mutants. Under the D1–D4-dropped mutant the honest tip reads
`closed 1 of 5`, so the count's meaning changes (it is not an accidental 4-of-5).

**F5 — Q79 location equivalence holds for the honest base.** The lane working tree and a clone of the
same committed HEAD give identical integrity observation dicts (`True`). Measured in this scratch copy
only; the L1 must re-measure at the freeze commit.

## Risks

- The base receipt was written at the dispatch commit `0f2b866`, not at the freeze commit. The
  mutation verdicts depend on the receipt's pinned digests and observations; the L1's freeze receipt
  must be re-measured and the matrix re-run at that revision before the claim is scored.
- The honest-world matrix ran against a scratch copy that includes the wave's uncommitted instrument
  files (the lane's committed state for those files is absent). The D5 gate and integrity run were
  unaffected, but a future run must start from the freeze commit.
- All three self-test-only kills (F2) mean the committed-fixture discrimination is thinner than
  the self-test tally (`0 failure(s) over 30 assertions`) suggests.

## Host / tooling

No install or upgrade. No kernel setting changed. No pacman transaction. Python 3.14.8, git 2.56.0
were used as found.

## Files written (all under the wave dir or scratch)

- `.ufo/waves/round-89/w1/MutTesterGates.md` (this report)
- `.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`
- `.ufo/waves/round-89/w1/MutTesterGates/equivalents.tsv`
- `.ufo/waves/round-89/w1/MutTesterGates/summary.json`
- `.ufo/waves/round-89/w1/MutTesterGates/harness.py`
- `.ufo/waves/round-89/w1/MutTesterGates/transcripts/` (FG and D5 run output)
- `.ufo/waves/round-89/w1/MutTesterGates/mutants/{fg,d5}/` (mutated instrument sources and plans)
- `.ufo/waves/round-89/w1/MutTesterGates/receipts/d5v3-base-receipt.json`
