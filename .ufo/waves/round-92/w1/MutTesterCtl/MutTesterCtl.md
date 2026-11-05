# MutTesterCtl — round-92 w1: mutation probe of the C1 control worlds and the kill-set pin

Seat: MutTesterCtl (leaf, no subagent dispatch). Scope: attack ExecCtlWorlds (C1 control worlds) and
ExecKillPin (C2(a) kill-set-size arm) on the candidate. Nothing in the lane was written; nothing was
committed to the lane; no installs were made.

## Candidate

- Base: `e073723ae667b64e534f8621bddb83ad12ad0e71` (freeze commit).
- Candidate: freeze + `ExecCtlWorlds.patch` + `ExecKillPin.patch`, committed in my scratch clone
  (scratch identity, `$S/repo`) as **`52dc61ea4e33047ce1a9776c3a5fa92ff9fcc6fa`**. Diff from base: 6 files,
  271 insertions (`check_mutation_battery.py` +36; `verifiers/fixtures/round-92/*` five scripts +235).
- `git rev-parse --show-toplevel` before every commit: the scratch clone path.
- Note: ExecCtlWorlds' READY names `81f7c8b` as its own scratch commit; my rebuild from the same patch
  is `52dc61e` (different commit, same applied content). Its probe receipt and mine reproduce the same
  counting line (see baseline).

## Baseline (unmutated candidate) — equivalents green

| check | command | observed | rc |
|---|---|---|---|
| frozen counting | `bash verifiers/fixtures/round-92/controls-run.sh` | `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2` | 0 (438 s) |
| per-script | stderr of controls-run | C2-shortcut rc=1 met=yes; C2-honest rc=0 met=yes; C1-shortcut rc=1 met=yes; C1-honest rc=0 met=yes | — |
| battery self-test | `python3 -B verifiers/check_mutation_battery.py --self-test` | `0 failure(s) over 28 assertions` | 0 (3 s) |
| candidate on dropped-row world | same self-test, one kill row removed (16 kill rows) | `FAIL arm kill-set-size: the live manifest's kill-row count equals the pin :: observed 16 kill rows, pinned 17` / `1 failure(s) over 28 assertions` | 1 |

Receipts: `receipts/base-controls.{out,err,rc}`, `receipts/base-bat-selftest.{out,rc}`,
`receipts/cand-dropped-selftest.out`.

## Mutants

Each mutant is a fresh scratch clone of the candidate with one single-occurrence exact-match edit
(the edit script asserts the anchor count is 1). Diffs: `receipts/mutants.diff`.

### m1 — counting prints `2 of 2` when a refused world exits 0 — **SURVIVED**

- Diff (controls-run.sh, `step`): `if [ "$rc" = "$want" ] && …` → `if { [ "$rc" = "$want" ] || [ "$rc" = 0 ]; } && …`
  (a refused row now counts met when it exits 0 and prints its named line).
- Live candidate (frozen counting command, unchanged worlds): `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, **rc 0** (`receipts/m1-controls.{out,rc}`). Identical to baseline, because the real refused worlds exit 1. So the frozen counting command does not distinguish m1 on the live tree.
- Discriminating world (stub harness, `receipts/stub-*.{out,err}`): four one-line stand-in worlds where the refused C2 world prints its named line and exits 0.
  - candidate counting: `observed: shortcuts refused 1 of 2; honest held 2 of 2`, **rc 1** (C2-shortcut rc=0 met=no).
  - m1 counting: `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, **rc 0** (C2-shortcut rc=0 met=yes).
- Verdict: the frozen predicate (exact line + exit 0 + each refused world's stdout names its conjunct) is MET under m1 on that world. No candidate consumer checks the refused world's exit code (per-script rc goes only to stderr; ExecCtlWorlds ships no self-test of controls-run.sh; ReviewerCtl's probes have not landed). **SURVIVED.** Finding F1.

### m2 — ctl-c2-capline-only-v2 drops the tip-battery invocation (cap-only decision) — **KILLED**

- Diff: `out="$(… check_tip_battery.py …)"; trc=$?` → `trc=0; cap=$(grep SELF_TEST_TIMEOUT_S … "$S/verifiers/check_assertion_floors.py"); out=""; if cap >= 320 then out="guard instrument-pin PASS"`.
- Discriminating world: the committed cap-only shortcut (cap 330, NO `INSTRUMENT_PINS` admission). The first mutant run used a relative path (cwd bug in my edit); that was re-applied with `$S`-anchored path and re-run. Corrected result: `C2-SHORTCUT-ACCEPTED: instrument-pin guard PASS on the shortcut world`, **rc 0** (`receipts/m2-mut.{out,err}`). Candidate on the same world: `C2-SHORTCUT-REFUSED … blob a189e61 … is not a pinned blob`, **rc 1** (`receipts/m2-cand.out`).
- Frozen counting on m2: `observed: shortcuts refused 1 of 2; honest held 2 of 2`, **rc 1** (`receipts/m2-controls.{out,rc}`; C2-shortcut rc=0 met=no). **KILLED** by the frozen counting command.
- Pinned-but-wrong-cap variant (considered): under m2 the cap gate still runs first (`cap < 320` → `out=""` → NOT-EVALUATED exit 2), so it does not read MET; the discriminator is the unpinned cap-only world above.

### m3 — ctl-c1-manifest-only-v2 passes the base rev, not the committed world rev — **KILLED**

- Diff: `--rev "$WREV"` → `--rev "$FREEZE"` in the battery call.
- Discriminating world: the committed manifest-only world (appended `mb-c1-shortcut-kill` row, committed in scratch). Under m3 the battery reads the base manifest (no row): `killed 17 of 17 … disclosed survivors 0 of 0`, `C1-SHORTCUT-ACCEPTED: battery exit 0 on the manifest-only world`, **rc 0**. The `rows committed and read` conjunct does not print (stdout has no `C1-SHORTCUT-REFUSED` line). `receipts/m3-mut.out`.
- Frozen counting on m3: `observed: shortcuts refused 1 of 2; honest held 2 of 2`, **rc 1** (`receipts/m3-controls.{out,rc}`; C1-shortcut rc=0 met=no). **KILLED** by the frozen counting command. This is the round-91 defect class re-instantiated; the rev-scoped read is what catches it.

### m4 — kill-set-size arm removed from `check_mutation_battery.py --self-test` — **SURVIVED (frozen counting) / KILLED (plan's C2(a) after-reading only)**

- Diff: the 13 lines of the arm (`live = Path(__file__)…` through the `"malformed" in broken_detail` check) deleted. Arm count drops 28 → 25.
- Dropped-row world: one kill row removed from the working-tree manifest (`fg-m1-expect-exit-sign-flip`; 17 → 16).
  - m4 self-test: `0 failure(s) over 25 assertions`, **rc 0** (`receipts/m4-dropped-selftest.out`). The dropped-row world is green again — the m6 class recurs.
  - candidate self-test on the same world: `FAIL arm kill-set-size … observed 16 kill rows, pinned 17` / `1 failure(s) over 28 assertions`, **rc 1** (`receipts/cand-dropped-selftest.out`).
- m4 honest self-test: `0 failure(s) over 25 assertions`, rc 0 — below the plan's landing floor N ≥ 26 (`receipts/m4-honest-selftest.out`).
- Frozen counting on m4: `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, **rc 0** (`receipts/m4-controls.{out,rc}`). The battery's measured-revision path does not run the self-test arm, so the frozen counting command cannot see m4.
- Verdict: the plan's C2(a) after-readings (same world must exit 1 naming `kill-set-size`; honest N ≥ 26) catch m4 directly; the frozen controls do not. Nothing else has been built to catch it. Finding F2.

### m5 — ctl-c1-honest drops its exit-0 requirement — **SURVIVED (bare-HEAD counting) / KILLED (rev-argument probe)**

- Diff: `if [ "$rc" = 0 ] && printf … grep -qF 'mutation battery killed 17 of 17 …'` → `if printf … grep -qF …` (committed in the probe world `5e142df`, together with the G3 world below).
- Discriminating world: candidate + SKILL.md with every line naming `check_mutation_battery.py` removed (committed, `ee6f5a3`). The battery at that rev: `G3 registry presence FAIL: 0 SKILL.md line(s)`, prints the full `killed 17 of 17 …` line, **rc 1**.
  - candidate `ctl-c1-honest.sh ee6f5a3`: `C1-PREDICATE-UNMET: battery rc 1 without the frozen predicate line`, **rc 1** (`receipts/m5-world-cand.out`).
  - m5 `ctl-c1-honest.sh 5e142df`: `C1-PREDICATE-MET`, **rc 0** (`receipts/m5-world-mut.out`).
- Frozen counting on the m5 probe world (m5 HEAD): `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, **rc 0** (`receipts/m5-controls.{out,rc}`). On the bare candidate HEAD the frozen counting runs ctl-c1-honest with no rev argument, so the rc-0 conjunct is never exercised: [INFERENCE] the bare-HEAD counting reads the same MET under m5 as under the candidate.
- Verdict: KILLED by a rev-argument probe; SURVIVED under the frozen counting command, which never passes a rev. Finding F3.

## Findings

- **F1 (m1): the refused-world exit code is not pinned by any consumer.** `controls-run.sh` counts a refused row met on the named line alone when a refused world exits 0 (m1 counts `2 of 2` rc 0 on the stub world). The frozen predicate requires only the exact line and exit 0. A fix needs an addendum that pins refused rc = 1 (or a controls-run self-test); not applied here, per the freeze.
- **F2 (m4): C2(a) has no executable frozen control.** `plans/round-92-controls.md` declares only the C1 controls and the six pre-data controls. The kill-set-size arm is checked by the battery's `--self-test` alone; the frozen counting command does not run it (m4 reads `2 of 2` rc 0). The pin also reads the instrument's own working-tree manifest, not the measured revision's committed manifest; a committed dropped-row revision is caught only by the literal `17 of 17` in `ctl-c1-honest.sh` (candidate: `killed 16 of 16` → UNMET, [INFERENCE] from the literal, not run). The self-test pin and the measured-revision count can disagree.
- **F3 (m5): the honest control's rc-0 conjunct is untested by the frozen counting.** The counting command never passes a revision, so a version of the honest script that accepts a G3-failing battery (rc 1 with the full line) reads MET there (`C1-PREDICATE-MET`, rc 0) while the candidate reads UNMET.
- **F4 (message, minor):** `ctl-c1-honest.sh` on rc 1 with the full line prints `battery rc 1 without the frozen predicate line`, though the full line is printed; the text is misleading about which conjunct failed.
- **F5 (runtime):** the frozen counting command takes 411–453 s wall time in every run (C2-shortcut alone ~189 s, its tip battery). The brief's 120 s per-probe guidance is exceeded; the freeze gate's 1200 s timeout is not.
- **Reviewer consumers:** ReviewerCtl had not published probes when I checked (`agent://ReviewerCtl`: "No final output yet"). My verdicts use only the candidate's own counting command, the battery self-test, and my own probes; if ReviewerCtl's probes cover m1, m4 or m5, that changes the SURVIVED lines above.

## Restoration / evidence

- Lane: nothing written. Scratch: `/fast/scratch/hyaku/kotoba-r92/MutTesterCtl/` (clone, mutant clones, stubs, receipts), removed before yield. `HYAKU_SCRATCH` pointed inside that dir for every control run.
- Mutant files were applied only to scratch clones; no restore needed. The candidate clone and each mutant clone were discarded with the scratch directory.
- Installs: none.
- Receipts copied here: `receipts/` (base, m1–m5 rc and outputs, stub harness, `mutants.diff`, `worlds.txt`).
