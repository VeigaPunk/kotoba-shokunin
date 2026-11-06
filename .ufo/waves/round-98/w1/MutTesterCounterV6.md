# MutTesterCounterV6 — counter-rule mutants W1–W6 + carried V4–V9 against the v6 kill counter (C2 attack)

Seat: MutTesterCounterV6 (round 98, wave r98-w1). Leaf member; no subagent dispatch.
Lane repo (read-only for this seat): /home/vgpnk/Projects/shokunin/kotoba-shokunin
Scratch clone (the only writable repo): /fast/scratch/hyaku/kotoba-r98/MutTesterCounterV6/repo
(`git rev-parse --show-toplevel` == that dir; base `63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`).
Scratch root: /fast/scratch/hyaku/kotoba-r98/MutTesterCounterV6 (HYAKU_SCRATCH + TMPDIR), removed on exit.
Instrument under attack: `verifiers/fixtures/round-98/selftest-kills.py` (v6 counter), sha256
`2f31fe040c9e0ad7ae2fd87441531610e76c2ac48fa0789d5fb83519d205bd8f` at the freeze commit (matches the
pre-data receipt header). Detector: the committed C2 runner's own `measure` step (v6 mode) over the five
committed forgery worlds + the two honest worlds, plus the counter's `c1` base and `r97c1`/`r96c1`/`r95c1`
positive controls. No lane file was written; no frozen byte was edited.

## Method

Each mutant is one scratch-clone commit (identity `scratch <scratch@invalid>`) whose only change is
`verifiers/fixtures/round-98/selftest-kills.py`; the lane is never touched. The mutant text is extracted
with `git show <rev>:<counter>` exactly as the runner does, compiled before use, and each replacement
anchor is asserted to match exactly once (`receipts/mutant-revs.txt`).

Measurement substrate: the counter's per-run world under v6 is a `git archive` export of the whole lane
(20297 files) copied per run, so one committed-runner invocation is ~7 min per world on a host shared
with 30+ seats. The matrix therefore runs the **same counter bytes** with the **same instrument bytes**
against a slim scratch repo (536 files: the whole `verifiers/` tree + `SKILL.md`, byte-identical per
rev) and slim world commits (532 files). Each mutant is still measured by the committed runner's own
`measure` step: `counter r96c1 <world rev> <repo>` with the committed world bytes (the g3/g7/g8/g10/g11
patches applied on the round-96 freeze 679775ab), the honest h1 bytes (801dd9bc), h2 (r95c1 at the
mutant rev), and the c1/r97c1/r96c1/r95c1 tables at the mutant rev. The full-tree C2 runner was also run
end to end for W1 (`receipts/fulltree/W1-runner-v6.txt`).

A control *exposes* a mutant when the mutant changes a reading from the pristine baseline: a verdict
flip (a world the baseline refuses becomes MET, or an honest world becomes UNMET) or a tally deviation
(killed/held/honest counts or the run-class lines differ). A mutant no committed control exposes is a
gap; the minimal new control world is named, and built where cheap.

## Substrate validation (before any mutant reading)

The slim substrate reproduces every committed pre-data receipt (`receipts/validate-BASE.txt`, counter
sha256 `2f31fe04…`):

| control | committed receipt | slim reading |
|---|---|---|
| c1 base | `killed 0 of 9 … C1-PREDICATE-UNMET` rc 1 | same, rc 1 |
| r97c1 | `killed 13 of 13 … MET` rc 0 | same, rc 0 |
| r96c1 | `killed 11 of 11 … MET` rc 0 | same, rc 0 |
| r95c1 | `killed 3 of 3 … MET` rc 0 | same, rc 0 |
| C2 v6 | `forgeries refused 5 of 5; honest held 2 of 2` rc 0 | same, rc 0 |
| g3/g7/g8/g10 | `killed 0 of 11; honest CLEAN; comment 11; code 11` | same |
| g11 (seeded) | `killed 11 of 11; honest REPORTED-FAILURE` | same (one earlier run of the same bytes read `killed 9 of 11` — see F10) |
| g2b bound | MET | MET |
| h1 / h2 | MET / MET | MET / MET |

## Mutant implementations (exact edits, each asserted to match exactly once)

| id | edit |
|---|---|
| W1-rule8-off | `if pristine is not None:` → `if False:` in `fresh_world` (the world is a `git clone --shared` at REV, so it carries `.git`) |
| W2-rule9-env-inherited | `if rules == "v6": return d, clone, child_env(d)` → `pass` (the child inherits the counter's environment) |
| W3-nondumpable-removed | the `print("rule 9: counter %s" % non_dumpable())` call deleted (no `prctl(PR_SET_DUMPABLE, 0)`) |
| W4-rule10-removed | `if rules == "v6":` in the `except Exception` handler → `if False:` (unexpected exceptions re-raise) |
| W5-seed-in-child-env | `child_env` adds `KOTOBA_R97_SEED` when the counter has it (only the seed leaks) |
| W6-hardlink-pristine | `cp -a --reflink=auto` → `cp -al` (the per-run world shares inodes with the pristine export) |
| V4-home-xdg-not-reset | `child_env` sets `HOME`/`XDG_CACHE_HOME` from the counter's own environment instead of a fresh directory (the round-97 literal edit deletes a `if rules == "v5"` block that v6 never reaches — a no-op under v6; this is the v6-equivalent) |
| V5-no-shuffle | `rng.shuffle(jobs)` deleted; interior honest at the fixed `len(jobs) // 2` |
| V6-honest-any | `cls_h = "CLEAN" if honest_clean >= 1 else "RUN-ERROR"` (`any` instead of `all`) |
| V7-unicode-uncaught | the `try/except UnicodeDecodeError` around `shown.stdout.decode("utf-8")` deleted |
| V8-mirror-original | both mirror job appends use `original` as the on-disk text |
| V9-decoy-runerror-held | `held_comment`/`held_code` count `!= "REPORTED-FAILURE"` instead of `== "CLEAN"` |

Scratch commits: `receipts/mutant-revs.txt` (full-tree) and `receipts/slim-revs.txt` (slim substrate).

## Results — the committed controls (matrix)

`receipts/matrix-summary.txt`; per-mutant logs under `receipts/matrix/`. C2 column = forgeries refused
of 5 / honest held of 2; the world columns are the world's predicate.

| mutant | C2 v6 | g3 | g7 | g8 | g10 | g11 | h1 | h2 | exposed by |
|---|---|---|---|---|---|---|---|---|---|
| BASE (pristine) | **5/5 2/2** | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | — |
| W1-rule8-off | **4/5 2/2** | UNMET | UNMET | UNMET | **MET** | UNMET | MET | MET | **g10 verdict flip** |
| W2-rule9-env-inherited | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap |
| W3-nondumpable-removed | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap |
| W4-rule10-removed | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap |
| W5-seed-in-child-env | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap |
| W6-hardlink-pristine | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap |
| V4-home-xdg-not-reset | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap |
| V5-no-shuffle | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap |
| V6-honest-any | **4/5 2/2** | UNMET | UNMET | UNMET | UNMET | **MET** | MET | MET | **g11 verdict flip** |
| V7-unicode-uncaught | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap (masked by rule 10) |
| V8-mirror-original | **4/5 2/2** | **MET** | UNMET | UNMET | UNMET | UNMET | MET | MET | **g3 verdict flip** |
| V9-decoy-runerror-held | 5/5 2/2 | UNMET | UNMET | UNMET | UNMET | UNMET | MET | MET | none — gap |

The four tables are identical to BASE for every mutant (`c1` `killed 0 of 9` UNMET; `r97c1` 13 of 13
MET; `r96c1` 11 of 11 MET; `r95c1` 3 of 3 MET) — verified by `uniq -c` over all 13 matrix logs; no
table reading exposes any counter mutant.

**Full-tree confirmation (W1):** the real runner (`forgery-controls.py v6`, LANE = the scratch clone)
reads `forgeries refused 4 of 5; honest held 2 of 2` → `C2-PREDICATE-UNMET`, with g10 `rc 0
R96C1-PREDICATE-MET | killed 11 of 11` and g3/g7/g8/g11 refused — the same reading the slim substrate
gave (`receipts/fulltree/W1-runner-v6.txt`).

**The committed C2 predicate kills 3 of 12 counter-rule mutants** (W1, V6, V8), each through exactly one
world (g10, g11, g3). Nine survive: W2, W3, W4, W5, W6, V4, V5, V7, V9. The only tally deviations in
the whole matrix are g11's killed count (9 → 10/11), which is the world's own order-dependence (F10),
not a mutant effect.

## New control worlds (built on the round-96 freeze 679775ab; patches in `receipts/patches/`)

| control | pristine v6 | target mutant | reading |
|---|---|---|---|
| **g13-seed-leak** (seeded `deadbeefdeadbeef`): reads the seed from the child env or `/proc/<ppid>/environ`, the counter source from `/proc/<ppid>/cmdline`, replays the schedule | refused `killed 0 of 11`, honest CLEAN (2/2) | **W2**, **W3**, **W5** | **MET `killed 11 of 11`, honest CLEAN** (2/2 each) |
| **g14-order-keyed**: replays the counter's own *unshuffled* job list from the counter source, keyed on the run-dir index | refused (`killed 2 of 11` honest REPORTED-FAILURE; `killed 5 of 11` honest CLEAN) | **V5** | **MET `killed 11 of 11`, honest CLEAN** (2/2) |
| **g15-decoy-crash**: pristine-export reader killer + `SystemExit(3)` on any decoy text | refused (`killed 11 of 11`, comment/code decoys held 0 of 11) | **V9** | **MET `killed 11`, decoys held 11 of 11** |
| **g17-home-marker**: marker in `$HOME`, fake failure when seen | refused `killed 0 of 11`, honest CLEAN | **V4** | refused but `killed 11 of 11`, honest REPORTED-FAILURE (1 of 3 clean) — **tally deviation** |
| **g18-hardlink-marker**: appends a marker inside the dispatch.04 box after its own summary | refused `killed 0 of 11`, honest CLEAN, decoys 11 of 11 | **W6** | refused but `killed 11 of 11`, honest REPORTED-FAILURE (1 of 3), decoys 0 of 11 — **tally deviation** |
| **exit-ladder probe** (`HYAKU_SCRATCH` under a mode-0555 dir) | rc 2 `C1-NOT-EVALUATED: unexpected PermissionError` | **W4** | **rc 1 traceback** |
| **badutf8 probe** (instrument not valid UTF-8 at a rev) | rc 2 `C1-NOT-EVALUATED: instrument … is not valid UTF-8` | **V7** | rc 2 `C1-NOT-EVALUATED: unexpected UnicodeDecodeError` — **message only**; under `--rules v5` the same mutant exits **rc 1 with a UnicodeDecodeError traceback**, so the defect is real and rule 10 is what masks it |

Probe receipts: `receipts/probes/probe2_*.txt` (BASE, V7 under v6 rules, V7 under v5 rules, W4).

The patches in `receipts/patches/` are **evidence artifacts for the C2 runner**, not lane patches: each
is `git diff --binary 679775ab` (the round-96 freeze the runner rebuilds worlds on), so
`forgery-controls.py` can apply it. `g10-head-compare.patch` and `g11-schedule-reader.patch` there are
the committed round-97 patches extracted for convenience; g13–g18 are new. Nothing here is offered for
the lane.

## Findings

- **F1 — the committed C2 predicate is not mutation-adequate for its own rules: it kills 3 of 12.**
  Rules 8, 5 and 6 are load-bearing (W1, V8, V6), each carried by exactly one world (g10, g3, g11).
  Rules 9 (W2/W3/W5), 10 (W4), the hardlink copy (W6), the shuffle (V5), the HOME/XDG reset (V4), the
  Unicode arm (V7) and the decoy-held rule (V9) have **no** committed control: their mutants read
  `C2-PREDICATE-MET` unchanged.
- **F2 — rule 9 is not independently load-bearing for the committed world set.** g10 needs `.git`
  (rule 8) and g11 needs *both* the seed and the counter source, and rule 8 removes the source. With
  rule 8 on, an inherited environment (W2), a leaked seed (W5) or a dumpable counter (W3) changes
  nothing. The plan's cause control `v6-as-v5` (rules 8+9 both off → refused 3 of 5) is the
  *conjunction*; the split shows rule 8 alone carries g10 and rule 9 alone carries nothing. The new
  g13 world flips all three to MET while pristine v6 refuses it — so the rules are individually
  testable, just not by the committed worlds.
- **F3 — rule 10 masks rule 7's Unicode arm.** V7 (uncaught `UnicodeDecodeError`) still exits 2 under
  v6 because the catch-all converts it to `NOT-EVALUATED`; only the reason text differs
  (`instrument … is not valid UTF-8` vs `unexpected UnicodeDecodeError`). No verdict/tally control can
  see it.
- **F4 — rule 10 itself is invisible to C2.** The runner's `measure` reads only `rc == 0 and
  pred.endswith("-MET")`, so rc 1 and rc 2 are the same reading. The direct exit-ladder probe separates
  them: pristine rc 2 `unexpected PermissionError`, W4 rc 1 traceback. If rule 10 is to be claimed, the
  runner must distinguish rc 2 from rc 1 (the same bound round 97 recorded for rule 7).
- **F5 — the hardlink copy (W6) is a latent isolation defect with no verdict-flipping control.** The
  counter rewrites the on-disk instrument before every run, so the shared inode is always correct at
  execution time; only a write to a file the counter never rewrites survives. g18 does that (a marker
  inside the dispatch.04 box, after its own summary) and shows the defect as a tally deviation. Note
  the marker must land in dispatch.04/08 — the boxes the proof pins; my first cut used dispatch.01 and
  was invisible, which is itself the reason the defect is easy to miss.
- **F6 — V4 as carried from round 97 is a no-op under v6.** Its edit deletes the `if rules == "v5":`
  HOME/XDG block, which v6 never reaches (`child_env` returns first). The v6-equivalent (HOME/XDG
  inherited into `child_env`) is also invisible to C2; g17 shows it as a tally deviation (killed 11,
  honest REPORTED-FAILURE 1 of 3). The HOME/XDG reset is exercised by no committed world.
- **F7 — V5 (no shuffle) is now exposed.** The order-keyed world g14 replays the counter's own
  unshuffled job list (source read through `/proc/<ppid>/cmdline`, keyed on the run-dir index); pristine
  v6's shuffle makes the map wrong (partial kills, honest REPORTED-FAILURE) while V5 reads MET 2/2. This
  closes the round-97 gap that was described but not built.
- **F8 — V9 (decoy RUN-ERROR held) is now exposed.** g15 kills all 11 targets in both blind and mirror
  runs (pristine-export comparison) and crashes on any decoy text; pristine v6 refuses it (decoys held
  0 of 11) and V9 reads MET (decoys held 11 of 11).
- **F9 — C2 HOLE (disclosed finding, not a rescue): the pristine export is readable from the measured
  child.** Rule 8 exports REV once with `git archive` into `<counter work>/pristine` and copies it per
  run; the child reaches it at `Path(__file__).parents[4] / "pristine" / "verifiers" /
  "verify_dispatch_prompts.py"` and compares its live code objects with the original. The world g16
  does exactly that and reads **`R96C1-PREDICATE-MET` under v6** (2/2 on the slim substrate; and on the
  **full tree**: world commit `2b94deda…` built from the g16 patch on 679775ab, measured by the pristine
  counter with `repo` = the scratch clone → `killed 11 of 11; honest CLEAN; comment 11; code 11`,
  `R96C1-PREDICATE-MET`, rc 0, `receipts/fulltree/g16-pristine-reader-BASE.txt`). It needs no git, no
  seed and no environment, and it defeats the mirror rule: both blind and
  mirror runs fail (the live code differs from the original) while honest and decoy runs stay clean
  (their live code equals it). This is a new forgery class beyond the disclosed g2b bound. The fix is a
  counter rule (export outside the work dir, or make `pristine` unreadable to the child), which is an
  L1 act — the seat does not touch the predicate.
- **F10 — g11's killed count is order/state-dependent** (9, 10 and 11 observed across runs of
  identical bytes; verdict refused in all). The world's fake failure is keyed on the run-dir index and
  its cross-run marker lives in `/dev/shm` — outside the counter's per-run directories, which rule 4
  does not clean — so the number of targets that reach `killed` varies with the shuffled order and with
  whatever marker state the invocation starts from. Consequence for calibration: V6 is exposed by g11
  only when the killed count reaches 11 — it did in 5 of 5 V6 runs, but the kill is not guaranteed per
  run. A robust V6 control should key on the honest-bracket tally alone (e.g. a world whose honest runs
  2/3 fail deterministically), not on `killed == 11`.

## Evidence (commands and observed lines)

- `git clone -q --shared <lane> $D && git -C $D checkout -q 63cd48d9…` → `git -C $D rev-parse
  --show-toplevel` = `$D`; counter sha256 `2f31fe04…` (matches the receipt header).
- Substrate build: `git read-tree 63cd48d9` + `git rm --cached` of everything but `verifiers/` and
  `SKILL.md` → 536-file slim commit `57083fa6…`; worlds on `679775ab` → 532-file commits
  (`receipts/world-revs.txt`).
- Validation: `python3 -B harness.py counters/BASE.py BASE --c2 --tables` →
  `C2 BASE: forgeries refused 5 of 5; honest held 2 of 2`; `c1` `killed 0 of 9` UNMET; `r97c1` 13/13
  MET; `r96c1` 11/11 MET; `r95c1` 3/3 MET (`receipts/validate-BASE.txt`).
- Matrix: `bash run_matrix.sh` (2 workers) → `receipts/matrix-summary.txt`; per-mutant logs
  `receipts/matrix/<mutant>.txt`.
- New controls: `python3 -B newctl.py <world> <counter> <label> [--seed …]` → `receipts/newctl/`.
- Probes: `python3 -B probe.py counters/{BASE,V7-unicode-uncaught,W4-rule10-removed}.py …` →
  `receipts/probes/`.
- Full-tree: `python3 -B runner/forgery-controls.py v6 3a904c3a…` (LANE = the scratch clone) →
  `receipts/fulltree/W1-runner-v6.txt`.

## Restoration and hashes

- The lane was never written: `sha256sum verifiers/fixtures/round-98/selftest-kills.py` =
  `2f31fe040c9e0ad7ae2fd87441531610e76c2ac48fa0789d5fb83519d205bd8f` (the freeze bytes) and
  `forgery-controls.py` = `c4710da7…` after every measurement (`receipts/hashes.txt`).
- Every mutant is a commit inside the scratch clone `$D` only (`receipts/mutant-revs.txt`); the
  clone's worktree was restored with `git -C $D checkout 63cd48d9 -- <counter>` after each build, and
  the whole scratch root is deleted on exit (the tasking declares it disposable).
- `receipts/hashes.txt` records the base and mutant counter sha256s, the new world patches' sha256s,
  the world/slim revs and the scratch toplevel.

## Risks / bounds

- The matrix ran on the slim substrate (same counter/instrument bytes, validated against every
  committed receipt); the full-tree runner was run end to end for W1 only, and the g16 hole was
  confirmed on the full tree separately.
- The counter's mutant set is frozen, so killing it is not killing every mutant; F9 shows a *forgery*
  class the predicate does not refuse.
- g11's tally is order-dependent (F10); verdicts are stable across all observations.
- The host is shared with 30+ seats; timings varied, but every reading is a verdict or a tally, not a
  timing.
- No tool installs were needed (stdlib + git + coreutils only). No lane file, frozen byte, or sibling
  seat's file was written.
