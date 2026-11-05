# MutTesterBattery — round 90 C1 (mutation-battery runner, attacked)

Target: `verifiers/check_mutation_battery.py`, sha256 `0828fd9b6277c98826521109b7abac5930dea9c9e5bb26314d84b54218477e3b`
(BATTERY_READY, 10:38). Every mutant was applied to a scratch copy of the lane (`/fast/scratch/hyaku/kotoba-r90/MutTesterBattery/repo`);
the lane was only read. Lane battery sha unchanged after the run.

Scratch setup (scratch only, not in the lane): `repo` = `git clone --shared` of the lane at 6fa5bb6; commit `bf614ecb` adds the
battery bytes and manifest (the lane does not commit them yet); `a93b51b3` adds one SKILL.md row (G3 arm); `9792df49`/`0fbc18de`
(X2) breaks the freeze gate at its baseline; `9e697467`/`e5870c94` (X5) makes a manifest anchor over-match. Working-tree overlays
(X3 dirty manifest, X4 dirty SKILL.md) were restored with `git checkout` in scratch after each run.

## Baselines (pristine)

| run | command | observed | exit |
|---|---|---|---|
| B1 self-test | `python3 -B verifiers/check_mutation_battery.py --self-test` | `0 failure(s) over 19 assertions` | 0 |
| B2 frozen, no SKILL row (`bf614ecb`) | `--rev bf614ecb… --work …` | G1 PASS; G2 PASS (20 mutant + 2 revision copies); G3 FAIL `0 SKILL.md line(s)`; `mutation battery killed 13 of 13 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 1` | 1 |
| B3 frozen, SKILL row (`a93b51b3`) | same | G3 PASS `1 SKILL.md line(s)`; same predicate line | 1 |
| B4 frozen at lane tip 6fa5bb6 | `--rev 6fa5bb6…` | `could-not-evaluate: G1: git show 6fa5bb6…:verifiers/fixtures/mutation-battery/manifest.tsv failed` | 2 |
| B5 frozen, lane-parent shape (`a93b51b3`, clone under a parent that holds the real `.ufo/reports/round-76/kotoba.md` symlink) | same | same as B3; d5-base-receipt baseline `closed 4 of 5`, `instance drift 4` (matches plan) | 1 |

Transcripts: `transcripts/p1-selftest.txt`, `p2-frozen-noskill.txt`, `p3-frozen-skillrow.txt`, `p4-frozen-lane-tip.txt`, `p5-frozen-lane-shape.txt`.

## Finding F1 (content fail on the pristine bytes) — the survivor row is killed

The frozen predicate cannot exit 0 at the final bytes: `disclosed survivors 0 of 1`. The one survivor-class row
`d5-m1a-d5iii-leg-only` is KILLED, not survived. Its recipe (`if not grew and not added:` → `if True:` at
`verifiers/check_r86_routed_repairs_v3.py:786`) flips the d5 self-test exit 0→1 through the fixture arm
`FAIL arm w_added_instance (frozen control): an added finding under already-red names fails via d5iii with drift 2`.
The manifest disposition ("the lane's frozen probes never reach a grown instance") is therefore false at the final bytes.
Result: the predicate exits 1 on the pristine bytes even with G3 PASS (B3). Route to the owner of the manifest (ExecBattery) and
the L1: the disposition/class must be amended by addendum before any scored reading, or the row must be re-classed `kill`.
I did not edit the manifest.

## Mutation table (`mutants.tsv`, 19 declared mutants)

Killed 16 of 19. Each probe was the battery self-test and the frozen run at `a93b51b3`; mutants that changed no
observation were then probed with an X control (X1 non-hex-commit rev, X2 broken-baseline rev, X3 dirty manifest, X4 dirty
SKILL.md, X5 over-matching anchor rev). Killed by arm:

- Self-test arm kills: m1 sign flip (`satisfying world (clean)`), m3 G2 read-back (`G2 copy integrity: … exits 2`), m4 G3 skip
  (`G3 registry presence: no SKILL.md row … exits 1`), m5 survivor class dropped (predicate line), m7 equivalent skipped
  (`satisfying world` + frozen 1→2), m8 G1 rev-bytes from working tree (`G1 dirty working tree`, poison arm), m9 trailing-ws
  into multi-line strings (`equivalence arm trailing-whitespace`), m10 comment-insert emits non-comment (syntax-breaking),
  m12 probe exit constant (`baseline fg-unsat-plan exit 0, declared 1`), m14 could-not-evaluate→1 (`G1 … exit 2`), m19 G3 match
  broken (`satisfying world`).
- Frozen-run kills: m6 printed predicate line drift (`equivalents survived` → `survive`, output changed, exit 1 unchanged).
- Probe-only kills (no self-test arm): m11 baseline guard removed → X2 exit 2→1; m13 anchor over-match guard weakened → X5
  exit 2→1; m17 manifest read from working tree → X3 exit 1→0; m18 SKILL.md read from working tree → X4 `G3 … PASS` → `FAIL`.

SURVIVED (recorded honestly, kill-class rows not killed):

- m2 `G1` non-hex-commit check removed: exit ladder unchanged (2 via the `git show` fallback); only the diagnostic text changes
  (X1). No self-test arm passes a well-formed non-commit rev. Coverage gap, not a predicate defect.
- m15 `G1` scratch clean-tree guard off: unreachable. The clone is `--no-checkout` plus a detached checkout, so it is always clean.
  A dead guard; route to L1 (remove, or document as unreachable).
- m16 revision-copy restore not re-read: verdict-invariant (each row writes its own mutant; baselines are precomputed). A stale
  mutated copy would stay on disk after the loop, unobserved. Low risk, noted.

Coverage gaps the table exposes: the self-test has no arm for the broken-baseline exit 2 (m11), the anchor over-match exit 2
(m13), or manifest/SKILL.md read from the working tree (m17, m18). The G1 poison arm poisons the target file only. Each gap is
killed only by my external X probes, so the battery's own self-test under-guards G1 and G2-adjacent arms.

## Equivalents (`equivalents.tsv`)

- Five own semantics-preserving rewrites of the battery (trailing comment, docstring comma, local rename `kept`→`keep_lines`,
  trailing spaces on a return line, CLASSES reflow): all 5 survived. Self-test identical, frozen run identical.
- The battery's six generated equivalence rows (comment-insert, docstring-reword, trailing-whitespace × fg/d5): all 6 survived on
  B2 and on every mutant run that did not break them. The generator-breaking mutants m9 and m10 were killed.

## Predicate-level result of the attack

`mutation battery killed 13 of 13 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 1` with exit 1 at every
pristine run (F1). The counter is sound on K, E and G1/G2 arms; the disclosed-survivor count is the defect.

## Risks

- F1 blocks the frozen predicate at the final bytes; the L1 must amend or re-class the row before a scored reading.
- The battery is not committed in the lane (B4 exit 2 at the tip); the frozen run needs the L1 commit first.
- Scratch clone layout: my first runs used a clone named `repo` with no fleet report symlink; the d5-base probe then reported
  `instance drift 5` and `SKIP location_flipped`. B5 (lane-parent shape with the real report symlink) matches the plan. The
  predicate verdict is the same in both shapes; the d5-base observation is location-dependent (Q79) and the battery does not guard it.
- Tools: none installed or upgraded; pacman not used.
- Scratch dir deleted before yield; `harness.py` in this directory is a copy of the scratch harness (paths point at scratch).

Files written: `mutants.tsv`, `equivalents.tsv`, `summary.json`, `harness.py`, `MutTesterBattery.md`, `transcripts/*`
(all under `.ufo/waves/round-90/w1/MutTesterBattery/`). The spec's `w1/MutTesterBattery.md` path sits outside this seat's
ownership, so the report lives here.
