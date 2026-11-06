author: hyaku closure (non-author integrator, @m_zfl)

# Round 99 verifier spot-check (non-author closure of kotoba round 99)

This closes lane-round kotoba r99. Round base `52e8e95ac4faf4ded84d7b82cbc204792590d0f7` (the
round-98 spot-check commit); lane tip `0a65cceb5b8fa5bb25a095828a1e6cd0e3681ee3`. Report:
`.ufo/reports/round-99/kotoba.md` in the fleet repo. The reviewer did not author the round and
changes no lane-authored file. No lane gate or lane counter was executed (PROTOCOL § Gate standard,
Closure consequence): gate and counter verdicts below are verified from committed receipts, and
each one says so. The reviewer ran the plain measurements (git/grep/wc/sha256/curl/census) itself
on 2026-11-06.

Driver digest (copied from `.ufo/watchdog.log`, which can change):

```
2026-11-06T10:38:00-03:00 launch kotoba round=99 pgid=2963268 driver=hyaku-inline attempt=1
2026-11-06T12:03:23-03:00 complete kotoba round=99; hyaku-inline attempt=1
```

## Step-1 conformance

- **Report.**
  - Fleet commit `caed7fd4bdf65dda7d2788cae3f7cd73dfb718ec`, author
    `kotoba-shokunin <kotoba@shokunin.local>`, committed 12:00:06-03:00.
  - That is after the last lane commit `0a65cceb` (11:59:03) and before the `complete` line
    (12:03:23).
  - The `## SHONEN` heading is present, with 4 lines, one per box, all `[~]`.
- **Hashes.** For each of `c0489d14…`, `b53e2096…`, `e215f0f9…`, `bacb1541…`, `e6c59844…`,
  `0a65cceb…` and the base `52e8e95a…`:
  - `git cat-file -t` gives `commit`;
  - `git merge-base --is-ancestor <h> master` is true.

  `git log 52e8e95a..master` lists exactly those six round commits, all authored by the lane
  identity.
- **Pushed and clean.**
  - `jj-lane.sh state` gives `branch=master local=remote=0a65cceb… ahead=0 behind=0 head=detached
    tracked=0 untracked=0`.
  - `git status --porcelain` is empty.
  - `git ls-remote origin refs/heads/master` gives `0a65cceb…`.
- **Prompt.**
  - `.ufo/prompts/kotoba-round-99.md` is committed by the lane identity (`ec275b8a`).
  - A `diff` of its lines 1–140 against `templates/round-prompt.md` shows only placeholder
    substitutions (`{{LANE}}`, `{{ROUND}}`, `{{FLEET_ROOT}}`, `{{AXES}}`).
  - §§ 1, 2, 2b, 3, 4 and 5 are present verbatim, and the hyaku addendum § 6 follows.

  The prompt carries the template contract.
- **Conformance notes** (status-neutral):
  - **N1.** The planner seat was held by the L1 because the wave validator rejects the `planner`
    role. ConnectorOverlapR99 Part 3 carried the planning data-walk. This is disclosed. It is a
    validator/driver gap for the operator, not lane debt.
  - **N2.** A wave seat left a 366 MB untracked clone (`repo/`) at the lane root. The L1 removed it
    before landing and mined it as a mistake. Nothing is left over (`git status --porcelain` is
    empty).

## Claims

### C1 — depth: the dispatch-prompt checker's self-test kills the twelve frozen survivors t01..t12

Re-measured by the reviewer (plain git/grep over committed bytes):

- `git diff -U0 52e8e95a bacb1541 -- verifiers/verify_dispatch_prompts.py | grep '^@@'` gives
  `@@ -1514,0 +1515,270 @@ def self_test() -> int:`. That is one insert-only hunk of 270 lines
  inside `self_test()`, and the production code is unchanged. It agrees with `prod-identity.txt`.
- `git diff 52e8e95a 0a65cceb -- verifiers/verify_dispatch_prompts.py | grep -c '^-[^-]'` gives
  `0`.
- `grep -oE 'r99-t[0-9]{2}'` over that diff gives the 12 distinct ids `r99-t01`..`r99-t12`.
- The new arms call the live CLI. In the diff, `main(` appears 7 times and `run_checks(` once.
  This agrees with the report's statement that the arms reach `run_checks`, `main`'s exit code and
  `--check`.
- The instrument is frozen. The blob IDs of `verifiers/fixtures/round-99/selftest-kills.py` and
  `carried-reds.py` at `0a65cceb` equal those at the instrument commit `c0489d14`. This agrees
  with `instr-identity.txt`.

Evidence-verified (committed receipts; the counter was not run):

- **Before.** `receipts/redbefore-c1-base.txt` was first committed in the freeze `b53e2096`, before
  the landing. It reads `C1 targets killed 0 of 12 (run errors 0); positive killed 1 of 1; honest
  CLEAN; …` → `C1-PREDICATE-UNMET`, `rc=1`.
- **After.** `receipts/landing/c1-v61.txt` (committed `e6c59844`) reads `C1 targets killed 12 of
  12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 12 of 12; code
  decoys held 12 of 12` → `C1-PREDICATE-MET`, `rc=0`. `c1-rulesv5.txt` gives the same tally.
- **Self-test.** `receipts/landing/dp-selftest.txt`, run over `git archive bacb1541`, reads
  `0 failure(s) over 154 assertions`, `rc=0`.

**Verdict: depth `improved`.** The values match the report: 0 → 12 of 12, and 128 → 154 assertions.
The 8 of 22 new MutTesterDispatchR99 survivors (the exit-2 ladder) are disclosed and routed. They
do not falsify the frozen predicate.

### C2 — consistency (calibration sub-axis): the three carried tip-battery reds read green, with no gate weakened

Re-measured by the reviewer:

- **Corpus gates byte-identical.** `git diff --quiet 52e8e95a 0a65cceb --
  verifiers/verify_corpus_integrity.py` and the same for `verify_corpus_independent.py` are both
  silent: both files are byte-identical at the tip.
- **Checklist change is data-only.** `git diff -U1 52e8e95a bacb1541 --
  verifiers/verify_skill_checklist.py` has hunks only at `GOVERNANCE_CORRECTIONS_HORIZON`
  (2723 → 3601) and inside the `GOVERNANCE_CORRECTIONS = (…)` block. The block has 16 appended
  rows (3586–3601) and one in-place change: row 2621's subject line goes from 158 to 161.
- **The re-pin is honest.** `git show 52e8e95a:SCORECARD.md | sed -n 161p` contains
  `round-60/kotoba.md` and line 158 does not. Line 161 is the true subject, and the frozen
  conjunct in `carried-reds.py` (header lines 26–30) permits "only its subject line may move". This
  agrees with ReviewerRedsR99's "same artefact" ruling.
- **Battery change is one pin.** `git diff 52e8e95a bacb1541 -- verifiers/check_tip_battery.py`
  shows only one appended blob `b6280c68…` inside `INSTRUMENT_PINS`, and the earlier pins are
  kept.
- **Append-only files.** The deleted/added line counts (non-blank lines, `grep -c '^-[^-]'` /
  `grep -c '^+[^+]'`) from `git diff 52e8e95a 0a65cceb` are below. LOG.md grows 3580 → 3612 lines,
  so the new correction rows 3586–3601 sit after the base's end:

  | file | deleted | added |
  |---|---|---|
  | `LOG.md` | 0 | 27 |
  | `SCORECARD.md` | 0 | 3 |
  | `corpus/README.md` | 0 | 9 |
  | `corpus/QUALITY.md` | 0 | 1 |
  | `corpus/SOURCES.md` | 0 | 1 |

  No added `corpus/README.md` row contains `*`. `SKILL.md` and `PROVINCE.md` have 0/0.
- **None of the four disclosed post-freeze shapes is used** (addendum 2 B1). There is no in-place
  governance rewrite, the new correction rows pin lines after the base's end, the index rows have
  no wildcard, and the only bound row (2621) resolves to the same artefact. This agrees with
  `post-hoc-holes.txt`.

Evidence-verified (receipts; the gates and counter were not run):

- **Before.** `receipts/c2-base.txt` (committed in the freeze `b53e2096`) reads `C2 carried reds
  green 0 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` → UNMET, `rc=1`.
- **Controls.** The five control receipts `c2-ctl-w1..w5` (committed in the freeze) all read
  `C2-PREDICATE-UNMET`, `rc=1`.
- **After.** `receipts/landing/c2.txt` reads `guards 5 of 5; tip battery exit 0: 6 of 6` and
  `C2 carried reds green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` → MET, `rc=0`.
  `c2-record-tip.txt` reads the same MET at `e6c59844`.

**Verdict: consistency `improved`.**

- C2 counter bound: four forged worlds built after the freeze read MET under the v1 counter. This
  is a counter weakness. The frozen kill rule names only the frozen controls, and the landing
  demonstrably avoids all four shapes, so the claim stands.
- The holes are routed (defect 3 below).

### No harm

- `git diff 52e8e95a 0a65cceb -- SCORECARD.md` adds three paragraphs only:
  - the r98 C99-2 correction;
  - the Round 100 plan;
  - the Round 99 axis annotations.

  It changes no score cell and deletes no line.
- `SKILL.md` and `PROVINCE.md` are untouched.
- The census holds at `rc 0` with `W04` 34, the same as the round start.
- No owned axis is harmed.

| axis | verdict |
|---|---|
| depth | improved |
| consistency | improved |
| coverage | unchanged |
| operability | unchanged |
| freshness | unchanged |
| calibration | unchanged |
| adjacency | unchanged |

`calibration` is the parent of the consistency sub-axis. It is graded `unchanged` separately,
because no calibration-row claim was declared, matching the round-98 closure key set.

## Discernment spot-check (`corpus/lessons/round-99.md` § Gate)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S281 Python argparse (`release/3.15.2`) | admit (tier A, mined) | `curl -sS https://docs.python.org/release/3.15.2/library/argparse.html` → `200 327874`; sha256 `36e8d5361b591376bbf9255c08147ece82f5f1fe52a5abd3d149656e902bb8ae`; `sed -n 989,990p` | agree | The bytes and digest equal the row's access record exactly. Lines 989–990 read "`'append'` - This appends each argument value to a list. / It is useful for allowing an option to be specified multiple times." The 22-word quote is present after the code span is folded. Choosing the pinned release over the rolling `/3/` alias is the correct ruling. The row grounds only the stdlib meaning of `action="append"`, which is what the t08 arm needs. |
| git-hash-object(1) lead | reject (not rowed) | `curl -sSL https://git-scm.com/docs/git-hash-object` → `200 29933`; sha256 `b7e8f953…eb798` (equal to the lesson's record); `grep -c 'Computes the object ID'` → 1 | agree | The pin mechanism reads `git rev-parse <rev>:<path>` (`verifiers/check_tip_battery.py`: line 344 at base, **line 349 at tip**, `got = git(clone, "rev-parse", "%s:%s" % (rev, path))`). It does not hash a file, so S267 (gitrevisions) and S268 (cat-file `-e`) are the right authorities. `grep -c git-scm.com/docs/git-hash-object corpus/SOURCES.md` → 0, so the reject is real, not a silent row. The line pointer drifted (defect 1). |

- **Newly written SOURCES row re-opened.** S281 (above).
  - Quote: 22 words, ≤ 25.
  - Location: HTML lines 989–990, verified.
  - The row count `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` goes from
    206 at the base to 207 at the tip.
- **Census.** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kotoba` → 34 `W04` duplicate-URL warnings (pre-existing, none on
  S281), last line `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md`, `rc=0`.

## Trend verdicts

- **expansion: unchanged.** `git diff --stat 52e8e95a 0a65cceb -- knowledge/` is empty. The one new
  registry row grounds an instrument arm and is not new domain knowledge.
- **quality: improved.** Two changes, both verified above:
  - C1: the province instrument's self-test kills 12 more frozen behaviours, with production bytes
    unchanged.
  - C2: the lane's own tip battery is green 6 of 6 for the first time since round 81, with both
    corpus gates byte-identical and the checklist changed in data only.
- **discernment: improved.**
  - The rolling-alias digest defect was caught before landing (addendum 1, `e215f0f9`, committed
    before the landing `bacb1541`).
  - Five forgery controls were committed before the data.
  - The post-freeze counter holes were disclosed, not claimed away.
  - Both sampled gate decisions agree on re-open.

## Routed defects (the lane fixes these next round)

1. **Lesson pointer drift.** `corpus/lessons/round-99.md` § Gate cites
   `verifiers/check_tip_battery.py:344` for the `rev-parse <rev>:<path>` read. At the round tip
   that line is **349**, because the C2 pin admission inserted 5 lines above it; 344 is the base
   line. The lane should append a named correction that cites `<rev>:<path>:<line>`.
2. **S279 superseding row** (C99-3). The `CAP_SYS_PTRACE` conjunct is recorded only in the lesson.
   The registry-form correction is a new row whose `teaches` cell opens with `supersedes S279 —`,
   and it is still open.
3. **C2 counter holes** (addendum 2 B1). Four MutTesterRedsR99 worlds read MET under
   `carried-reds.py` v1:
   - in-place governance rewrite;
   - an unbound correction target;
   - a correction row pinned to a pre-existing line;
   - a wildcard index row.

   Any future reuse of the counter needs conjuncts that refuse these shapes.
4. **Carried from round 98.**
   - Defect 1: the v7 counter for g11/g16, without a forger-reachable tmpfs marker.
   - Rolling-alias digests on S253, S270 and S276 (C99-4).
   - The `strip_token_dressing` comma-anchor fix.
5. **C1 survivors.** 8 of 22 MutTesterDispatchR99 mutants survive (the exit-2 ladder, F2).
6. **Seat hygiene.** A wave seat cloned a repo into the lane root (N2). The seat prompt or scratch
   discipline should pin clones under `/fast/scratch/hyaku/<lane>-r<N>`.

## Operator note (promotion is operator-owned)

All four SHONEN boxes stay `[~]`. To this non-author:

- Box 1 (SKILL.md tables, checklists and sources) now appears checkable from outside: the committed
  checklist gate reads all 11 checks PASS at the landing (`receipts/landing/c2.txt`, evidence-verified).
- Box 4 (PROVINCE accurate, no bleed) appears checkable from `PROVINCE.md` being unchanged plus
  ConnectorOverlapR99 Part 2.

The reviewer neither writes nor recommends a promotion here.
