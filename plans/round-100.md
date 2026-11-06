# Round 100 — kotoba (Linux host, omp) — plan

Author: KotobaR100 (L1, attempt 1). Round: 100. Base: lane tip at round start
`7b449a637c03d9b4c43a81b4df37cb38c2ea89ee` (branch `master`, the round-99 spot-check commit;
`jj-lane.sh state`: local == remote, `ahead=0 behind=0 tracked=0 untracked=0`).
Instrument commit: `d1e1170d950fc378bb6a28bbfc5a62802669be86` — `verifiers/fixtures/round-100/selftest-kills.py`
(v6.2: the round-99 v6.1 counter with only its mutant tables changed) and
`verifiers/fixtures/round-100/anchor-lists.py` (v1). Freeze commit: **this commit** — the plan, the
pre-data receipts in `.ufo/waves/round-100/receipts/` (all taken with the committed instrument bytes),
the control-world builder and its committed patches, and the source-opening receipt.

Both claims are frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-100-addendum-*.md` BEFORE any
scored reading.

## Inherited state resolved at freeze

- Lane clean at base; one launch of round 100 in `../.ufo/watchdog.log`, no `lane-dead-no-report kotoba
  round=100`: nothing inherited. No `corpus/lessons/operator-*.md`.
- `corpus/lessons/round-99-verifier-spotcheck.md` read in full (round 99: both claims verified
  improved). Routed defects:
  1. Lesson pointer drift (`check_tip_battery.py:344` is the base line; 349 at the round-99 tip) →
     named correction C100-1 in `corpus/lessons/round-100.md` citing `<rev>:<path>:<line>`, and the
     round's mined mistake.
  2. S279 superseding row → new row (frontier step below).
  3. carried-reds v1 counter holes → `carried-reds.py` is not reused this round; the C2 counter here is
     a different instrument whose checklist conjunct refuses an in-place rewrite of any base
     correction row and any added row (`checklist_confined`); the four shapes stay recorded against
     v1 for any future reuse.
  4. Carried from round 98: (a) the v7 kill counter for g11/g16 → **carried again, not claimed**: it is
     a rules change whose own forgery controls need a full round, and this round's two slots go to the
     two surfaces with measured, falsifiable before-states; (b) rolling-alias digests of S253, S270,
     S276 → superseding rows pinned to `release/3.15.2` (frontier step); (c) the
     `strip_token_dressing` comma-anchor fix → **this round's C2**.
  5. C1 survivors (MutTesterDispatchR99 F2, the exit-2 ladder) → **this round's C1**.
  6. Seat hygiene (a clone at the lane root) → every seat prompt pins scratch under
     `/fast/scratch/hyaku/kotoba-r100/<seat>/` and the L1 sweeps the lane root before landing.
- Base tip battery: `receipts/c2-base.txt` shows `tip battery exit 0: 4 of 6` — both corpus gates red
  at the base because the closure-landed `corpus/lessons/round-99-verifier-spotcheck.md` is unindexed
  (`corpus.index unindexed=1`). Per Q89 the landing heals it (a coverage-map row for that file — the
  file itself is closure-authored and never edited — and an equal-mode baseline re-record after every
  corpus file of the landing is in place). This is landing no-harm work, not a claim.

## Counting commands (frozen at the instrument commit)

- **C1:** `python3 -B verifiers/fixtures/round-100/selftest-kills.py c1 <rev>` (v6.2; `--rules v5`
  reproduces the round-97 rules).
- **C2:** `python3 -B verifiers/fixtures/round-100/anchor-lists.py <rev> [REPO]` (header is the
  specification).

## Claim C1 — depth (lowest owned non-retired axis, score 9) — the dispatch-prompt checker's self-test kills its exit-2 ladder

Surface moved: `verifiers/verify_dispatch_prompts.py --self-test`, the executable proof of SKILL.md
§ Dispatch-prompt fidelity boxes `dispatch.04` / `dispatch.08`; this round its substrate-error exit
ladder (`main`'s not-a-directory and `EnvError` returns, the `--json` substrate payload), the
directory substrate check, the UTF-8 decode of `read_text` and `run_checks`' request order — none of
which any self-test arm observes at the base (MutTesterDispatchR99 F2, F3, F5).

- **Frozen mutants** (`CLAIMS["c1"]` of v6.2): t01-notdir-exit-zero (m01), t02-enverror-exit-one (m02),
  t03-json-exitcode-zero (m03), t04-dircheck-exists (m22), t05-readtext-latin1 (m08),
  t06-runchecks-sorted (the F3 order permutation); positive p00-md-not-stripped. Excluded by rule: m19
  (provably equivalent), m09 (reporting-only), m21 (equivalent on the committed SKILL.md, the round-99
  n20 rule), m04 (RUN-ERROR class). m03 is admitted: the payload's `exit_code` is the verdict a
  `--json` consumer reads.
- **Predicate (frozen; the same sentence as the counter header):** `<C>-PREDICATE-MET` iff (honest)
  every honest run is CLEAN; (targets) every target mutant applies and is KILLED; (positive) the
  positive mutant applies and is KILLED; (guard) every target's comment decoy and code decoy HOLDS.
- **Target:** `C1-PREDICATE-MET`, exit 0, at the landing revision — tally
  `C1 targets killed 6 of 6 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 6 of 6; code decoys held 6 of 6`.
- **Do-nothing control (pre-data):** `receipts/redbefore-c1-base.txt` (the counter at the round base)
  must read `C1 targets killed 0 of 6` → `C1-PREDICATE-UNMET` rc 1; `redbefore-c1-base-rulesv5.txt` the
  same under `--rules v5`.
- **Positive controls (pre-data):** `r99c1`, `r98c1` at the base → MET
  (`receipts/poscontrol-r99c1-base.txt`, `receipts/poscontrol-r98c1-base.txt`).
- **Kill rule:** unmet if the landing reading is not `C1-PREDICATE-MET`; if a frozen anchor no longer
  matches; if `selftest-kills.py r99c1|r98c1|r97c1|r96c1|r95c1 <rev>` stops reading MET; if
  `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` stops reading `boxes proven 2` rc 0;
  if production code of `verify_dispatch_prompts.py` outside `self_test()` changes (one insert-only
  region inside it is the admitted shape); or if the counter bytes at the landing revision differ from
  `d1e1170d`. A miss is an honest stop, never a narrowed target.
- **Arm constraint (stated to the builder):** an arm whose mutant raises (t04: a plain file reaching
  `iterdir`) must catch the exception and record a failure, because a traceback exit is RUN-ERROR
  under rule 1, never a kill.
- **Sourced:** S282 (Python 3.15.2 pathlib, `Path.is_dir`, opened 2026-11-06,
  `receipts/sources-opened.txt`; supersedes the rolling-alias S276) grounds the t04 arm: "False will be
  returned if the path is invalid, inaccessible or missing, or if it points to something other than a
  directory" — a plain file must fail the directory check, which `exists()` does not.

## Claim C2 — consistency (calibration sub-axis, score 10) — the checklist gate's citation reading matches the repo for comma-list line anchors

Surface moved: the lane's self-assessment gate `verifiers/verify_skill_checklist.py` (both public
citation checks, `check_governance_citations` and `check_citation_resolves`, through
`strip_token_dressing`). At the base a cited file that exists reads red when its line anchor is a
comma list (`file.md:30,37`), the form SKILL.md itself uses; the round-99 stopgap excused the one live
instance by a correction row (LOG.md:3598 → SCORECARD.md:529).

- **Predicate (frozen; the same sentence as the counter header):** `C2-PREDICATE-MET` iff
  (mismatches) the truth table reads 0 mismatches over both public check paths; (gate) the real-tree
  checklist is green; (selftest) its self-test holds at or above the base floor; (kill) the revert
  mutant is killed by the self-test; (frozen) all three frozen-byte conjuncts hold; (battery) the tip
  battery reads guards 5 of 5 and its checklist gate exits 0.
- **Target:** `anchor-lists.py <landing rev>` →
  `C2 mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant KILLED; frozen 3 of 3; battery ok`,
  `C2-PREDICATE-MET`, rc 0.
- **The admitted change (frozen bytes, so the revert mutant and the confinement conjunct are exact):**
  in `strip_token_dressing`, the line
  `    m = re.match(r"^(.+\.\w+):\d+(-\d+)?$", tok)` becomes
  `    m = re.match(r"^(.+\.\w+):\d+(-\d+)?(,\d+(-\d+)?)*$", tok)`; an arm inside `self_test()` that
  fails when the old line is restored; the one `GOVERNANCE_CORRECTIONS` row whose stale token is
  `corpus/lessons/round-80-verifier-spotcheck.md:30,37` removed (with the fix its subject resolves, so
  the fail-closed correction check would report it as naming no live red subject); one
  `INSTRUMENT_PINS` admission of the new checklist blob in `check_tip_battery.py`. Nothing else in the
  checklist changes (the counter's `checklist_confined`).
- **Do-nothing control (pre-data, `receipts/c2-base.txt`):** the round base →
  `C2 mismatches 8 of 28; … revert mutant ABSENT; frozen 2 of 3; …` → `C2-PREDICATE-UNMET`, rc 1.
- **Controls (pre-data; committed patches `receipts/ctl-worlds/*.patch` on the base, built by
  `.ufo/waves/round-100/build-ctl-worlds.py` in a scratch repo; receipts `receipts/c2-ctl-*.txt`),
  each must read UNMET:**
  - p1 fix line only (truth-table positive: must read `mismatches 0 of 28`; red elsewhere — gate RED
    from the now-dead correction row, revert mutant SURVIVED, battery FAIL on the unpinned blob);
  - f1 a sloppy anchor regex `:.*$` with the row removed and pinned (mismatches > 0; frozen refuses);
  - f2 the honest fix line and row removal, pinned, no self-test arm (refused by the kill conjunct
    alone);
  - f3 fix line and arm, pinned, correction row kept (refused by the real-tree gate: the fail-closed
    correction check);
  - f4 row removed only, no code fix (mismatches 8; gate RED);
  - f5 the honest change plus `check_governance_citations` forced to PASS (mismatches on the
    governance path's red rows; frozen refuses).
- **Kill rule:** unmet if the landing reading is not `C2-PREDICATE-MET` rc 0; if any control except
  p1's mismatch tally reads MET at freeze (then the counter is wrong and the claim is withdrawn, never
  rescued); or if the counter bytes at the landing revision differ from `d1e1170d`.

## Separability

C1 changes only `self_test()` of `verify_dispatch_prompts.py`; C2 changes only
`verify_skill_checklist.py` (fix line, `self_test()` arm, one corrections row) and one battery pin. No C1
target reads the checklist, and C2's counter reads nothing of the dispatch-prompt checker except as a
battery gate it does not score. Each is measured at its own candidate (base + its patch) as well as at
the landing.

## Frontier step

- **Census** before: `receipts/census-before.txt` rc 0, 34 `W04`, 207 rows.
- **Rows planned (opened this round, `receipts/sources-opened.txt`):** S282 pathlib (supersedes S276),
  S283 tempfile (supersedes S253), S284 unittest (supersedes S270) — all pinned to
  `docs.python.org/release/3.15.2/`, digest re-fetch-stable; S285 ptrace(2) (supersedes S279 — adds
  step (4)'s `CAP_SYS_PTRACE` conjunct, round-99 C99-3).
- **Sourced claim:** C1 cites S282.
- **Mined mistake (draft):** class `line-pointer-cited-at-base-revision` (the round-99 lesson cited
  `check_tip_battery.py:344`, true at the base, 349 at the tip after an insertion above it) ·
  evidence `corpus/lessons/round-99-verifier-spotcheck.md` routed defect 1 · captured-by none · fix:
  a correction row citing `<rev>:<path>:<line>` plus a QUALITY criterion; shown able to fail by
  `git show 0a65cceb:verifiers/check_tip_battery.py | sed -n 344p` (no `rev-parse`).
- **Assimilation:** none planned (`merge/kotoba/` not taken). `considerthese/` re-read by the scribe.

## Wave

One v1 wave `r100-w1` (11 seats; ≥25 % attack): see `.ufo/waves/round-100/gen-w1.py`. The L1 holds the
planner seat (the validator rejects `planner`); ConnectorOverlapR100 carries the planning data-walk.

## Pre-data readings (taken at the instrument commit, before any seat)

See the receipts; the summary lines are appended below by the L1 before this commit.

- C1: `redbefore-c1-base.txt` and `redbefore-c1-base-rulesv5.txt` → `C1 targets killed 0 of 6 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 6 of 6; code decoys held 6 of 6`, UNMET rc 1; `poscontrol-r99c1-base.txt` 12 of 12 MET, `poscontrol-r98c1-base.txt` 9 of 9 MET.
- C2: `c2-base.txt` → `C2 mismatches 8 of 28; gate GREEN; self-test HELD; revert mutant ABSENT; frozen 2 of 3; battery ok`, UNMET rc 1 (the 8 mismatches are rows r01–r04 on both paths; self-test 1864 assertions).
- C2 controls, all UNMET rc 1:
  - p1 fix line only: `mismatches 0 of 28; gate RED; self-test HELD; revert mutant SURVIVED; frozen 2 of 3; battery FAIL` — the truth-table positive reads 0 mismatches.
  - f1 sloppy regex: `mismatches 10 of 28; gate GREEN; …; revert mutant ABSENT; frozen 2 of 3; battery ok`.
  - f2 no arm: `mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant SURVIVED; frozen 3 of 3; battery ok` — refused by the kill conjunct alone.
  - f3 row kept: `mismatches 0 of 28; gate RED; …; revert mutant KILLED; frozen 2 of 3; battery FAIL`.
  - f4 data-only removal: `mismatches 8 of 28; gate RED; …; revert mutant ABSENT; frozen 2 of 3; battery FAIL`.
  - f5 governance forced PASS: `mismatches 7 of 28; gate GREEN; self-test BROKEN; revert mutant KILLED; frozen 2 of 3; battery ok`.
