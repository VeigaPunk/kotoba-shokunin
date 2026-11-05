# ReviewerBattery — r90-w1 (attack seat): mutation-battery instrument

Full verdicts, commands, and observed lines: `.ufo/waves/round-90/w1/ReviewerBattery/review.md`
(evidence transcripts under `ReviewerBattery/predicate-runs/`, guard probe scripts under
`ReviewerBattery/guards/`, recipe mutants under `ReviewerBattery/recipes/`).

## Attack summary (findings by severity)

- **F1 HIGH — predicate unmeetable at every rev of the lane (landing-scope defect, not a battery defect).**
  The executed battery (`check_mutation_battery.py` sha256 `0828fd9b…3b`, == BATTERY_READY) and its
  `verifiers/fixtures/mutation-battery/manifest.tsv` exist ONLY as untracked working-tree files at
  tip `6fa5bb6d`. `git show <rev>:verifiers/fixtures/mutation-battery/manifest.tsv` fails at every
  first-parent ancestor of the tip (7/7 tested) and `git fsck --dangling` holds no manifest-like blob.
  Every frozen-predicate run ends:
  `could-not-evaluate: G1: git show 6fa5bb6d…:verifiers/fixtures/mutation-battery/manifest.tsv failed` (exit 2).
  Preserved refs: `predicate-runs/predicate-run.tip.out`, `predicate-run.R2B.out`, `predicate-run.R3.out`.
  In-world (scratch clone, rev R4–R9) the same instrument behaves per predicate; the fix is the L1
  commit of the untracked pair, not a code change.
- **F2 MEDIUM — G3 is a raw line-substring check, weaker than plan § C1's "registry row conformant".**
  A mangled row (broken backtick pair, stray "X" in the path token) still yields
  `G3 registry presence PASS: 1 SKILL.md line(s) name check_mutation_battery.py` (world RA,
  `predicate-run.RA.out`). G3 absence fires correctly (world RB: `G3 … FAIL: 0 SKILL.md line(s)`).
- **F3/F4/F5 INFO — no defects.** Docstring predicate sentence byte-equals plan line 26
  (`mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors S of S`).
  d5 probes pin only FG baselines (`0/0/1`) and leave d5 baselines observed-only (exit AND kept-output
  diffing both flip kills); manifest guards refuse all malformed rows/recipes/dispositions; the
  self-test's broken-conjunct arm genuinely breaks `K == M` (`killed 3 of 4`, exit 1).

## Guard reality (verified ferrous)

- G1: full-40-hex rev asserted; poisoned uncommitted working tree never read (world R13:
  `G1 revision identity PASS` with full sentence intact).
- G2: recorded-sha256 read-back refuses tamper and truncation
  (`G2 copy integrity: tampered on disk sha256 …, recorded …`); full run logs
  `G2 copy integrity PASS: 20 mutant copies and 2 revision copies read back at their recorded sha256`.
- G3: fires on no-row world (RB, exit 1), passes on registered world (R4/R6E).
- Exit ladder: 0 satisfying (world R8 reclassification), 1 content fail (13of14/K<M), 2 could-not-evaluate
  (anchor miss, guard trips), never a crash on a mutant.

## Recipe reality (verified on real code)

Hand-applied via `re.compile` on final bytes, count=1 verified, diffs of 1–2 real code lines, all
mutants compile: `fg-m3-ladder-refusal-to-2` (line 288 `EXIT_REFUSED`→`EXIT_EVAL`; killed
`[fg-self-test 0->1; fg-unsat-plan 1->2]`), `d5-m2-digest-check-removed` (`snap_ok = True`; killed
`[d5-self-test 0->1]`), plus the in-battery matrix: `fg-m4 stdout-parse drop → exit 3` flips,
equivalents survive, survivor `d5-m1a` flips only the `d5-self-test` (0→1) at worlds R6E/R9/R10 —
no crash-on-mutant anywhere; anchor-mismatch worlds exit cleanly `could-not-evaluate: anchor miss`.

## Baseline honesty (verified, two-sided)

`base-d5v3.txt` re-run byte-identical (only d1's tip pin moves 0c20d8ab→6fa5bb6d; `closed 4 of 5 /
instance drift 4` unchanged). FG probe baselines re-observed 0/1/0 == declared. A r89-receipt probe
flip is reported as a KILL, not swallowed: `d5-m2` shows the digest-check removal flips
`d5-self-test` 0→1 → killed; `diff_against()` marks output-only flips (`"output changed"`) as kills too;
the self-test's `fx-k4` kill row that flips NOTHING is what breaks `K == M` (exit 1, `killed 3 of 4`).

## Self-test honesty

`--self-test` → `0 failure(s) over 19 assertions`, exit 0 (whole run and the 19 `t.check` sites verified ==
source count). Broken-conjunct arm confirmed: mutating its fixture world re-derives
`killed 3 of 4` + exit 1 in the battery's own satisfiable-vs-broken fixture pair.

## Bounds statement

Scratch `/fast/scratch/hyaku/kotoba-r90/ReviewerBattery` created, TMPDIR-bound, and DELETED before
yield (verified: `ls` → No such file or directory; 24 `--work` worlds self-cleaned; receipts captured
into `w1/ReviewerBattery/` first). No git/jj writes in the lane, the fleet, or any shared path; the
only repo writes were scratch-clone commits inside `/fast/scratch/hyaku/kotoba-r90/ReviewerBattery/repo2`
with `rev-parse --show-toplevel` == clone dir asserted before each. No tool installs.

## Residual risk

- The L1 must commit `verifiers/check_mutation_battery.py` + `verifiers/fixtures/mutation-battery/`
  (and the SKILL.md registry row for G3 to pass at the scored rev). Until then C1 cannot verify.
- G3's substring-level conformance leaves a registry-row-grammar gap; a future counter should parse
  the row's columns, not just its id substring (F2).
