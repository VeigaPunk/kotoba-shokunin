# ReviewerBattery — r90-w1 attack on `verifiers/check_mutation_battery.py` and `verifiers/fixtures/mutation-battery/`

seat: ReviewerBattery (attack seat r90-w1). Attack target as landed by ExecBattery-4 (byte-identical copy preserved at
`.ufo/waves/round-90/w1/ReviewerBattery/battery-script.defended.bin`; observed sha256 was tracked across the attack minutes and matched
BATTERY_READY (content `0828fd9b6277c98826521109b7abac5930dea9c9e5bb26314d84b54218477e3b`). All paths are lane-local unless
explicitly stated as scratch. Probe logs live in `predicate-runs/`, guard scripts in `guards/`, recipe mutants in `recipes/`.

Attack started before BATTERY_READY was emitted (the handoff file landed at 10:38, middle of the attack). Two lanes tested
against: the live lane at commit 6fa5bb6d (freezer: "round-90: freeze entry in LOG") and the scratch
clone-with-as-written-world at R4 = 5f5064eb (R4 world: battery script landed (uncommitted), manifest landed
(uncommitted), SKILL.md battery row bait present — G3 will be exercised at R4, R5, R6, R7, R8, R9, RA, RB worlds).

## Attack axes

1. **1a — predicate identity (kill rule)**

   The docstring's predicate sentence reads, at `verifiers/check_mutation_battery.py:6` (line for the frozen predicate):

   > `mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors S of S`

   The plan's own frozen predicate text, at `plans/round-90.md:26`, is the byte-identical string:

   > `mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors S of S`

   No drift. The docstring body is the frozen predicate; the `%d`-interpolating runtime counterpart `LINE_FMT` lives at line 62;
   the fallback that makes the docstring the *only* source of truth is that a run may pass line-format-args with `K==M` grunting (see 4).

2. **1b — manifest-guard tamper (missing class column + malformed class)**

   In-vitro (scratch `guards/iv-manifest-guards.py`, driven through importlib against the frozen bytes):

   - `id\ttarget\tclass\trecipe\tdisposition` (5-col) row sanity: `PARSED-OK`
   - row with 4 columns (missing class col): `COULD-NOT-EVALUATE: manifest line 2: 4 columns, expected 5` (exit 2)
   - row with 6 columns (extra col): `COULD-NOT-EVALUATE: manifest line 2: 6 columns, expected 5`
   - bad class name (`killk`): `COULD-NOT-EVALUATE: manifest fg-m2: class 'killk' not in ('kill', 'equivalent', 'survivor')`
   - recipe not-JSON: `COULD-NOT-EVALUATE: manifest fg-t1: recipe is not JSON (Expecting value: line 1 column 1 (char 0))`
   - recipe op not `replace`: `COULD-NOT-EVALUATE: manifest fg-t2: kill recipe must be replace with edits`
   - equivalent recipe kind not in the 3 allowed: `COULD-NOT-EVALUATE: manifest fg-u1: equivalent recipe must be a rewrite in ('comment-insert', 'docstring-reword', 'trailing-whitespace')`
   - edit dict missing `anchor`: `COULD-NOT-EVALUATE: manifest fg-v1: edit needs anchor and with`
   - survivor with whitespace-only disposition: `COULD-NOT-EVALUATE: manifest fg-s5: survivor row needs a disposition`

   **No defect found** — every malformed manifest variant refused at could-not-evaluate and none reached probe execution.

3. **1c — G2 copy integrity / sha256 re-read (the tamper guard)**

   In-vitro (scratch `guards/iv-g2copy.py`, driving the frozen module's own `place()` over a temp write-back):

   - honest write-back, digest read back equal: PASS
   - honest write-back followed by byte-tamper on disk (sha256 vs recorded mismatch): caught with
     `G2 copy integrity: tampered on disk sha256 9dfce5e15efc, recorded 1d035ac51680`
   - truncated write-back (digest read back shorter): caught with the same refusal text
   - full-battery run at R4 (whole `--rev … --work …` path): `G2 copy integrity PASS: 20 mutant copies and 2 revision copies read back at their recorded sha256` (9+ repeats)

   **No defect found** — writing a mutated file whose sha256 was edited after recording cannot pass; the guard refused every forged world.

4. **2 — guard realities at whole-battery level (G1, G3, and the frozen exit ladder)**

   Worlds committed in the scratch clone (never in the lane):

   | world | what was forged | observed |
   |---|---|---|
   | R2/R2B/tip 6fa5bb6d | manifest only on disk (uncommitted) | `could-not-evaluate: G1: git show 6fa5bb6d…:….manifest.tsv failed`, exit 2 — correct: the manifest must be IN the rev |
   | R3 = 168fd095 | battery script + manifest landed, no SKILL.md row | `G3 registry presence FAIL: 0 SKILL.md line(s) name check_mutation_battery.py`, predicate line `… disclosed survivors 0 of 1`, exit 1 |
   | R4 = 5f5064eb | battery script + manifest landed, SKILL.md battery row added | `G3 registry presence PASS: 1 SKILL.md line(s) name check_mutation_battery.py`, all 13 kill rows killed, 6 equivalents survived, `disclosed survivors 0 of 1`, exit 1 (survivor d5-m1a flips, see 4) |
   | RB = fd23ae80 | SKILL.md battery rows stripped after having been R4-present | `G3 registry presence FAIL: 0 SKILL.md line(s) name check_mutation_battery.py`, exit 1 — **G3 fires on a SKILL.md without the row** |
   | RA = 4a3b7f12 | SKILL.md row mangled (extra "X" inside the backtick path → backticks unbalanced) | `G3 registry presence PASS: 1 SKILL.md line(s) name check_mutation_battery.py` — G3 is a byte-containment check on the id substring, not a row-conformance check; a visually broken row still passes. See Finding F2. |
   | R13 | uncommitted poison to the d5 gate's working tree | `G1 revision identity PASS` and standard 13/13, 6/6, 0/1 output, exit 1 — the poison was never read; commit bytes only. |

   One world tripped G1 on identity (R3): the battery's own `git show <rev>:SKILL.md` refusal names *is not a commit of <lane>* —
   correct refusal when the rev is not a tip-commit of the *cwd* lane: scratch-clone commits are visible to the battery only when
   run from inside the scratch clone, which is fine because the fix only invokes `--rev <lane-tip-hash>` in the live lane.

5. **3 — recipe reality (kill-set is real; probes flip for the named reason)**

   The manifest at `verifiers/fixtures/mutation-battery/manifest.tsv` is landed (uncommitted at base): 21 rows (13 kill, 6 equivalent, 1 survivor),
   recipes ported from r89 MutTesterGates with re-anchored texts for the final bytes.

   - **fg-m3-ladder-refusal-to-2** — applied by hand via `re.compile` on pristine final bytes
     (`"; "\.join\(problems\)\), file=out\)\n            return EXIT_REFUSED`, count=1, unique at line 288 of the final bytes; `with`:
     replace the lone `return EXIT_REFUSED` with `return EXIT_EVAL`). Diff: 1 line, real code, not a comment; mutant compiles cleanly.
     R4 in-world battery run: `fg-m3-ladder-refusal-to-2 kill killed [fg-self-test exit 0->1; fg-unsat-plan exit 1->2]` —
     the killed probe flips for the named reason (the refusal ladder turns REFUSED(1)→EVAL(2)).
   - **fg-m4-parse-drop-stdout-clause** — `fg-fixed-plan exit 0->3; fg-unsat-plan exit 1->3` (dropping the stdout clause makes spec
     completion reach `INVALID SPEC` trip-wire exit 3). Real-code mutation; no crash; verdict changed.
   - **d5-m2-digest-check-removed** — applied by hand on pristine d5 (`snap_ok = (m_integrity == receipt["integrity_sha256"]\n\s+and m_baseline == receipt["baseline_sha256"])\n`, count=1, replaced with `    snap_ok = True`).
     Diff: real code, only the digest-pair conditional. In-world battery run: `d5-m2 killed [d5-self-test exit 0->1]` — the killed
     probe flips because the self-test's re-record/tamper arm now returns `instance drift 0`-equivalent green where the pristine bytes refuse. No crash.
     **Cross-check 4b**: the hand-applied d5-m1a mutation of the pristine d5 bytes in `/fast/scratch/hyaku/kotoba-r90/ReviewerBattery/m2world/fleet/repo2`
     showed `instance drift 0` reached — but under the FROZEN battery the r89-receipt is in the world only as the `.ufo/waves` directory checkout,
     so the d5-base-receipt probe read `instance drift 5` in that world (`corpus.pointers.report_dead 1>0` appears as drift simply from the emitted
     world's fresh CO state, not from a wrong probe). The battery refuses to mis-attribute: the d5-m1a survivor KILLS the d5-self-test
     only in the pristine+R4 world (`predicate-run.R6E.out`) and correctly reads `killed` there.
   - **a crash-on-mutant**: none. All 13 kill-row mutations in the R4 run produce verdict flips, never a segfault or a Python traceback; the
     only malformed-recipe case (`fx-x-missing-anchor` in the battery's own self-test, and my d5-m1a-removed world R6F) exits
     `could-not-evaluate: anchor miss … matches 0 time(s) in the revision bytes, expected 1` — a clean refusal, not a crash.

   **No defect found** on axis 3 — the kill-set is honest; equivalent rows survive; the killed probes flip for the named reasons.

6. **4 — baseline honesty**

   The frozen d5 baseline (committed anchor `.ufo/waves/round-90/receipts/base-d5v3.txt`; preserved at `anchor.base-d5v3.as-committed.txt`):

   ```
   PASS d1 two receipts carry exit=0; instruments equal 04647b0f..0c20d8ab
   FAIL d5ii new DRIFT names absent from the receipt: ['corpus.index.unindexed']
   FAIL d5iii instance growth under: ['corpus.index.tracked_files 181>180', 'corpus.index.unindexed 1>0', 'corpus.pointers.commit_total 62>61', 'corpus.pointers.report_total 146>144']
   r86 routed defects closed 4 of 5
   instance drift 4
   ```

   Re-ran the d5 probe myself in the live lane tree (`observed-d5-baseline-lane.txt`): identical lines except d1's second rev pin
   `0c20d8ab -> 6fa5bb6d` (tip moved between the committed base receipt and my run; the class count does not change `closed 4 of 5 / instance drift 4`).

   The frozen probe set in the battery (`PROBES` at declared baselines): FG `self-test=0, fixed-plan=0, unsat-plan=1`; D5 `self-test=None, base-receipt=None`
   (`None` = observed-only). Re-ran FG probes myself at the base-commit extract: fixed=0, unsat=1, selftest=0 — the declared FG baselines match my observation.

   On the kill-rule question ("a flip on the r89-receipt probe would be reported as a kill, not swallowed"): demonstrated twice.
   (i) remove the digest check (d5-m2) and the d5-self-test probe exits 0->1 → `killed`. (ii) forge an added DRIFT name and the
   d5-base-receipt probe exit stays at declared-None but its *output changes* → `diff_against()` reports `output changed` → `killed`
   (predicate `K == M` requires every kill row to diff). A kill row that flips NOTHING is explicitly handled — the `broken conjunct K == M`
   self-test arm exits 1 with `killed 3 of 4` (battery self-test, observed 19-failure-free).

   **No defect found** on axis 4.

7. **5 — self-test honesty (broken-conjunct arm really breaks a conjunct)**

   `--self-test` → `0 failure(s) over 19 assertions` (both at the pristine scratch copy and re-confirmed on the battery script copy
   in the lane at 10:49-10:57, exit 0). The 19 `t.check` call sites count to exactly 19 in the source (`guards/…`-style source walk:
   19 `t.check` calls). The broken-conjunct arm is `fx-k4-d5-dead-return` (`FX_KILL_DEAD`, recipe `    return 0\n` → `    return 1\n`,
   disposition "fixture: a kill-class row no probe observes (broken conjunct)"): with that row added to the satisfying world the
   battery exits 1 and prints `mutation battery killed 3 of 4 kill-set; …` (the `line_broken` arm). That is a genuine conjunct break —
   the added kill row cannot be observed by any probe, so K < M and the exact predicate line flips to `killed 3 of 4`, proving the
   arm *does* break `K == M` rather than passing vacuously.

   **No defect found.**

## Findings (by severity)

**F1 (HIGH, invalid-landing, not a battery defect): the battery + manifest fixtures are NOT COMMITTED — they are untracked files
at the live lane tip 6fa5bb6d, so the frozen predicate can never pass at any rev in this lane.** Every predicate run against any
existing commit fails with `could-not-evaluate: G1: git show <REV>:verifiers/fixtures/mutation-battery/manifest.tsv failed` (exit 2).
`git cat-file` over all 7 first-parent ancestors of the tip: none contains the manifest; `git fsck --dangling` has 16 dangling
blobs, 0 manifest-like; reflog shows only `export from jj` entries (the R90 tip's last op is `qtqqopuvq 2026-11-05 10:40:34`).
The lane is a jj-colocated repo; the ExecBattery landing never reached git (or jj's export ran before the files were staged jj-side).
This is an ExecBattery-4 handoff scope defect, not a counter defect: BATTERY_READY declares the script self-test green while the
predicate's G1 precondition is structurally unmeetable at every rev of the lane. Logging as a reviewer finding; no lane byte touched.

**F2 (MEDIUM, G3 conformance is weaker than the plan claims): G3 is a raw substring check** —
`g3_rows = sum(1 for ln in git_show(lane, rev, SKILL).splitlines() if BATTERY.encode() in ln)` (line ~340). It counts *lines* that
contain `check_mutation_battery.py` anywhere (my RA world showed a row with a broken/unbalanced backtick and an inserted stray "X"
still counts as G3 PASS; a bare `markdown-code-fence` mention would also pass). The plan's G3 wording is "the gate registry row
must name the battery"; the weaker substring reading satisfies the letter, but the *registry-conformance* semantics claimed in
plan § C1's Target ("registry row … conformant") is NOT implemented by the battery's G3. Not a wrong-verdict on the landed
manifest (the R4 world's G3 PASS line corresponds to a real, well-formed row) — a scope gap to name for a future counter iteration.

**F3 (LOW, observed twice and benign): the docstring's frozen predicate sentence and the plan's byte-match exactly; the runtime
`LINE_FMT` interpolates only the printed line.** The exact-match printer `LINE_FMT % (K, M, E_s, E, S_disc, S_decl)` uses the same
sentence shape. No drift. No action.

**F4 (INFO): the d5 probes' declared baselines are `None` (observed-only), unlike the FG probes' `0/0/1`.** Two sides to note:
(i) proactive honesty — the d5 baseline can be non-deterministic under lane state (the d5-base-receipt probe output pins
corpus.index DRIFT contents that move as the lane feeds its own receipts in); pinning it would risk false could-not-evaluate on
any corpus movement. (ii) the flip detection still works because `diff_against()` compares both exit AND kept output lines
(`RUN_SPECIFIC` regex strips run-specific scratch paths and 12+ hex tokens first). Attack could not break it; satisfied.

**F5 (INFO): the survivor row's disposition text says "r89 recorded SURVIVED (mutants.tsv)"** and the r89 matrix
(`transcripts/d5-matrix.txt`) shows the survivor surviving on all six worlds *except* w_newname flips (0->1). The manifest's
disposition text is a committed claim that binds the survivor to "never flips under the frozen probes": the frozen probes are
the d5-self-test and d5-base-receipt probes, and the survivor's actual r89 lab target (w_newname) is NOT one of the frozen
probes — so the disposition's parenthetical ("the lane's frozen probes (the self-test and the base-receipt run at the lane)
never reach a grown instance") is what makes the row honest. Confirmed in-world at R6E and R9 that the survivor flips the
d5-self-test only when the d5iii leg's own guard-feeds (`grew`/`added`) are removed — which is the expected under-flow that
d5-m1b (the *removed* leg kill row) kills via `grew = []`. Internally consistent.

## Test-of-record exhaustion checks

- No git/jj writes ran in the lane, the fleet, or the shared clone dir contents (the only write surface in the scratch clone at
  `/fast/scratch/hyaku/kotoba-r90/ReviewerBattery/repo2` was `git add`/`git commit` over the clone's own working tree, which the
  clone recipe's own commit authorization covers: `git -C "$D" rev-parse --show-toplevel` was asserted equal to $D before every commit there).
- No git/jj writes in the lane, against frozen instruments, against SKILL.md, or against any sibling seat's file. My recorded
  writes: only under `.ufo/waves/round-90/w1/ReviewerBattery/` + the one BATTERY_READY watch (read-only).
- Scratch `--work` dirs (`wA…wRB`) were created and cleaned by the battery itself; the base-tree and m2probe/copy dirs sit inside
  the one scratch root that I will delete before yield.
- The lane's own `git status --porcelain` at attack end showed exactly the 6 known ExecBattery/ExecFloors Bump/IndexRow files
  (`corpus/README.md`, `check_assertion_floors.py`, `floors-registry.json`, plus untracked battery script/fixtures dir) and my
  hand-off receipt files — mine are only `w1/ReviewerBattery.md` + `w1/ReviewerBattery/**`. No shared file was touched.
- Scratch cleanup pending at yield: `/fast/scratch/hyaku/kotoba-r90/ReviewerBattery` (removed after this review is written).

## Tool installs

None (no `pacman`, no `uv tool`, no binary drops; `python3 -B`, `git`, `sha256sum` only).
