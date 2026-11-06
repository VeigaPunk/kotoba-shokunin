# Round 99 — kotoba (Linux host, omp) — plan

Author: KotobaR99 (L1, attempt 1). Round: 99. Base: lane tip at round start
`52e8e95ac4faf4ded84d7b82cbc204792590d0f7` (branch `master`, `jj-lane.sh state`: local == remote,
`ahead=0 behind=0 tracked=0 untracked=0`).
Instrument commit: `c0489d14156a7687d10ae5389d72eaa923b2bc29` — `verifiers/fixtures/round-99/selftest-kills.py`
(v6.1: the round-98 v6 counter with only its mutant tables changed) and
`verifiers/fixtures/round-99/carried-reds.py` (v1). Freeze commit: **this commit** — the plan and the
pre-data receipts in `.ufo/waves/round-99/receipts/`, all taken with the committed instrument bytes.

Both claims are frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-99-addendum-*.md` BEFORE any
scored reading.

## Inherited state resolved at freeze

- Lane clean at base; one launch of round 99 in `.ufo/watchdog.log`, no `lane-dead-no-report kotoba
  round=99`: nothing inherited. No `corpus/lessons/operator-*.md`.
- `corpus/lessons/round-98-verifier-spotcheck.md` read in full (round 98: rejected-honest-stop, C2
  missed). Routed defects:
  1. C2 non-reproducible refusal (v6 g11 rests on a `/dev/shm` marker) → **not claimed this round**;
     carried to round 100 with the g16 pristine-export hole. Reason: a v7 counter is a rules change
     whose own controls need a full round; this round spends its claim slots on the two carried
     surfaces that have measured, falsifiable before-states (C1, C2 below).
  2. Report line count (+183 vs 182) → correction in this round's report and LOG.md § Round 99.
  3. SCORECARD r98 C1 annotation names `63cd48d9` where the receipt measured `a060b450` → appended
     correction in SCORECARD.md (append-only).
  4. `/dev/shm/.r97-g11-run.*` leftovers → no v6/v7 g11 world runs this round; the L1 lists any
     remaining markers in the report (not attributable, not deleted).
  5. S279 conditional denial (step (4) also requires the caller to lack `CAP_SYS_PTRACE`) → the
     round-99 lesson records the conjunct as a correction note (ScoutSourcesR99 re-opens ptrace(2)).
  6. Carried tip-battery reds → **this round's C2**.
- SCORECARD "Round 99 planned": the tip-battery reds → C2; the v7 counter → carried (defect 1);
  the `dispatch_prompts` floor raise → carried.

## Counting commands (frozen at the instrument commit)

- **C1:** `python3 -B verifiers/fixtures/round-99/selftest-kills.py c1 <rev>` (v6.1; rules 1–10 are the
  v6 rules unchanged; `--rules v5` reproduces the round-97 rules for separability).
- **C2:** `python3 -B verifiers/fixtures/round-99/carried-reds.py <rev> [REPO]` (header is the
  specification).

## Claim C1 — depth (lowest owned non-retired axis, score 9) — the dispatch-prompt checker's self-test kills twelve more frozen survivors

Surface moved: `verifiers/verify_dispatch_prompts.py --self-test`, the executable proof of SKILL.md
§ Dispatch-prompt fidelity boxes `dispatch.04` / `dispatch.08`, its `--box-proof`, and (new this round)
its live CLI (`run_checks`, `main`'s exit code and `--check` selection, `read_text`'s substrate error),
which the self-test has never called (MutTesterDispatchR98 F4).

- **Frozen mutants** (`CLAIMS["c1"]` of v6.1; MutTesterDispatchR98 n01–n05, n07–n11, n13, n14 — the
  twelve verdict-bearing survivors at the round-98 landing, each with a differential witness in
  `.ufo/waves/round-98/w1/MutTesterDispatchR98.md`): t01-l1-suffix-unanchored, t02-role-round-above,
  t03-proof-map-hash-unenf, t04-proof-missing-skill, t05-proof-verdict-mismatch,
  t06-runchecks-first-only, t07-main-fail-exit-zero, t08-main-check-ignored,
  t09-readtext-oserror-empty, t10-verdict-of-prefix, t11-map-duplicate-first, t12-finish-fails-nas;
  positive p00-md-not-stripped. Excluded by rule: n12, n18, n19, n20 (equivalent / reporting-only /
  verdict-equivalent); n06, n15, n16, n17 (killed at the round-98 landing).
- **Predicate (frozen; the same sentence as the counter header):** `<C>-PREDICATE-MET` iff (honest)
  every honest run is CLEAN; (targets) every target mutant applies and is KILLED; (positive) the
  positive mutant applies and is KILLED; (guard) every target's comment decoy and code decoy HOLDS.
- **Target:** `C1-PREDICATE-MET`, exit 0, at the landing revision — tally
  `C1 targets killed 12 of 12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 12 of 12; code decoys held 12 of 12`.
- **Do-nothing control (pre-data):** `receipts/redbefore-c1-base.txt` — the counter at the round base
  (production and self-test bytes of the round-98 landing) → `C1 targets killed 0 of 12`,
  `C1-PREDICATE-UNMET`, rc 1; `receipts/redbefore-c1-base-rulesv5.txt` the same under `--rules v5`.
- **Positive controls (pre-data):** `r98c1`, `r97c1` at the base → MET
  (`receipts/poscontrol-r98c1-base.txt`, `receipts/poscontrol-r97c1-base.txt`).
- **Kill rule:** unmet if the landing reading is not `C1-PREDICATE-MET`; if a frozen anchor no longer
  matches; if `selftest-kills.py r98c1|r97c1|r96c1|r95c1 <rev>` stops reading MET; if
  `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` stops reading `boxes proven 2` rc 0;
  if production code of `verify_dispatch_prompts.py` outside `self_test()` and its self-test helpers
  changes; or if the counter bytes at the landing revision differ from `c0489d14`. A miss is an honest
  stop, never a narrowed target.
- **Sourced:** S281 (Python argparse, `action='append'`, opened 2026-11-06,
  `receipts/sources-opened.txt`) grounds the t08 arm: `verify_dispatch_prompts.py:527` declares
  `--check` with `action="append"`, so `--check dispatch.04` selects exactly that check.

## Claim C2 — consistency (calibration sub-axis, score 10) — the three carried tip-battery reds read green without weakening a gate

Surface moved: the lane's self-assessment gates against the repo state. `verify_skill_checklist.py`
has been red since round 81's record commit `23e838c`; `verify_corpus_integrity.py` and
`verify_corpus_independent.py` red at every revision since round 88 (ScoutTipReds,
`.ufo/waves/round-98/w1/ScoutTipReds.md` § 2 and timeline). Since round 92 the landing no-harm rule
accepted "the base red set" as a conjunct, so the red never healed (ScoutTipReds F6).

- **Predicate (frozen; the same sentence as the counter header):** `C2-PREDICATE-MET` iff (reds)
  carried reds green 3 of 3; (selftests) 3 of 3 self-tests exit 0 at or above their base assertion
  floor; (frozen) all four frozen-byte conjuncts hold; (guards) the tip battery at REV reports guards
  5 of 5.
- **Target:** `carried-reds.py <landing rev>` →
  `C2 carried reds green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok`, `C2-PREDICATE-MET`, rc 0.
- **Do-nothing control (pre-data, `receipts/c2-base.txt`):** the round base →
  `carried reds green 0 of 3` → `C2-PREDICATE-UNMET`, rc 1.
- **Forgery controls (pre-data; committed patches `receipts/ctl-worlds/*.patch` on the base, receipts
  `receipts/c2-ctl-*.txt`), each must read UNMET:** w1 the two corpus gates stubbed to `sys.exit(0)`;
  w2 the corpus baseline re-recorded to the observed drift only; w3 the checklist's governance check
  switched to N/A with its blob admitted in `INSTRUMENT_PINS`; w4 the checklist's governance check
  forced to PASS with its blob admitted; w5 `check_tip_battery.py` edited outside `INSTRUMENT_PINS`.
- **Honest route the counter admits:** content fixes (coverage-map rows for unindexed lessons; the
  `corpus/lessons/round-81.md:8` absent test-world hash written in the gates' quoted form, meaning
  unchanged), an equal-mode baseline re-record taken AFTER every corpus change of the landing tree,
  appended `GOVERNANCE_CORRECTIONS` rows with one appended LOG.md correction notice (data, not code —
  the `:30,37` line-anchor gate defect, ScoutTipReds F5, is fixed as a correction row, and the regex
  fix is routed), and one `INSTRUMENT_PINS` admission of the new checklist blob.
- **Kill rule:** unmet if the landing reading is not `C2-PREDICATE-MET` rc 0; if any forgery control
  reads MET at freeze (then the counter is wrong and the claim is withdrawn, never rescued); or if the
  counter bytes at the landing revision differ from `c0489d14`.
- **Governance hygiene at integration:** LOG.md / SCORECARD.md text written this round cites fleet
  paths in the `../` form and never cites a file that does not exist yet (the fleet report) — the
  class that produced most of the checklist reds (mined mistake below).

## Separability

C1 changes only `self_test()` of `verify_dispatch_prompts.py` (no C2 gate reads it except the
checklist's delegated `--box-proof`, which C1's kill rule keeps at `boxes proven 2`); C2 changes only
corpus index/baseline data, one historical quoting, the checklist's corrections data, a LOG.md notice and
one battery pin. Each is measured at its own candidate (base + its patch) as well as at the landing.

## Frontier step

- **Census** before: `receipts/census-before.txt` rc 0, 34 `W04`, 206 rows.
- **Sourced claim:** C1 cites S281 (argparse), opened this round.
- **Mined mistake (draft):** class `governance-cell-cites-fleet-path-repo-rooted` (round 82+ wrote
  `.ufo/reports/...`, `.ufo/watchdog.log`, `.ufo/l0-questions.md` repo-rooted in LOG/SCORECARD) ·
  evidence ScoutTipReds § 2.1 row 4 · captured-by `governance.citation_resolves` (it did fire) but the
  landing no-harm rule accepted an unchanged red set (F6) · fix: C2 plus a QUALITY criterion that a
  landing's no-harm reading requires the carried-reds counter MET, not "red set unchanged" — shown
  able to fail by `receipts/c2-base.txt` (0 of 3).
- **Assimilation:** none planned (`merge/kotoba/` not taken). `considerthese/` re-read by the scribe.

## Wave

One v1 wave `r99-w1` (11 seats; ≥25 % attack): see `.ufo/waves/round-99/gen-w1.py`. The L1 holds the
planner seat (the validator rejects `planner`); ConnectorOverlapR99 carries the planning data-walk.

## Pre-data readings (taken at the instrument commit, before any seat)

- C1: `redbefore-c1-base.txt` and `redbefore-c1-base-rulesv5.txt` → `C1 targets killed 0 of 12 … comment decoys held 12 of 12; code decoys held 12 of 12`, UNMET rc 1; `poscontrol-r98c1-base.txt` 9 of 9 MET, `poscontrol-r97c1-base.txt` 13 of 13 MET.
- C2: `c2-base.txt` → `C2 carried reds green 0 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok`, UNMET rc 1.
- C2 forgery controls, all UNMET rc 1: w1 `green 2 of 3; self-tests held 1 of 3; frozen 2 of 4; guards FAIL`; w2 `green 0 of 3`; w3 `green 0 of 3; frozen 3 of 4` (checklist prints an N/A line); w4 `green 1 of 3; frozen 3 of 4` — disclosed: the forced-PASS checklist reads GREEN and its self-test holds (1864), so w4 is refused by frozen conjunct (4) alone (`bytes differ outside the corrections data`); w5 `frozen 3 of 4`.
