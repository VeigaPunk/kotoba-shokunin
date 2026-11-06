author: hyaku closure (non-author integrator, @m_zfl)

# Round 97 verifier spot-check (non-author closure of kotoba round 97)

This closes lane-round kotoba r97. The round base is `fa1bebae33e6b0ab4e36b9ba73ff7d4c5d610520`
(the round-96 spot-check commit). The closure prompt's "before" is the freeze
`148395bf42af97436b1b832a97a175515f981939`, and the lane tip is
`1d44bd820cf4ec53a37baba2b45f6da7776a84bd`. The report is `.ufo/reports/round-97/kotoba.md` in the
fleet repo. The reviewer did not author the round, and none of these checks changes a lane-authored
file. The reviewer ran no lane gate (PROTOCOL § Gate standard, Closure consequence). Gate verdicts
below are therefore verified from committed evidence, and each one says so.

Driver digest (copied from `.ufo/watchdog.log`, which can change):

```
2026-11-06T00:44:27-03:00 launch kotoba round=97 pgid=3652779 driver=hyaku-inline attempt=1
2026-11-06T01:43:16-03:00 lane-dead-no-report kotoba round=97; retry same round (hyaku-inline attempt=1: L1 ended without a landed report: FAIL report_of (missing, unchanged, no SHONEN heading, or < 400B): .ufo/reports/round-97/kotoba.md)
2026-11-06T01:43:18-03:00 launch kotoba round=97 pgid=736139 driver=hyaku-inline attempt=2
2026-11-06T01:43:48-03:00 lane-dead-no-report kotoba round=97; retry same round (hyaku-inline attempt=2: L1 ended without a landed report: FAIL report_of (missing, unchanged, no SHONEN heading, or < 400B): .ufo/reports/round-97/kotoba.md)
2026-11-06T01:43:50-03:00 launch kotoba round=97 pgid=739000 driver=hyaku-inline attempt=3
2026-11-06T01:44:20-03:00 lane-dead-no-report kotoba round=97; retry same round (hyaku-inline attempt=3: L1 ended without a landed report: FAIL report_of (missing, unchanged, no SHONEN heading, or < 400B): .ufo/reports/round-97/kotoba.md)
2026-11-06T07:56:50-03:00 launch kotoba round=97 pgid=1022870 driver=hyaku-inline attempt=1
2026-11-06T08:19:24-03:00 complete kotoba round=97; hyaku-inline attempt=1
```

## Step-1 conformance

- **Report.** Fleet commit `a03888b0f96a70ed9f5b44e83390948c005dab50`, authored by
  `kotoba-shokunin <kotoba@shokunin.local>` at 08:18:20-03:00. That is after the last lane commit
  (`1d44bd82`, 08:17:14) and before the `complete` line (08:19:24). The `## SHONEN` heading has
  four lines, one per box, all `[~]`, matching `SHONEN.md` lines 5/7/9/11 at the tip.
- **Cited commits.** Each hash below exists and
  `git merge-base --is-ancestor <hash> refs/heads/master` holds:
  - `7c01b10d54fbdcd97dd9ba06fe0954828e8a880f`
  - `94a1021762a888d8a360ba6efa759372cef392fb`
  - `148395bf42af97436b1b832a97a175515f981939`
  - `693be9c321c26078a2adbf32c220dfcd371cbe35`
  - `38361a2513dabe6e01a1d63a5abde89e7b521271`
  - `1d44bd820cf4ec53a37baba2b45f6da7776a84bd`
  - `fa1bebae33e6b0ab4e36b9ba73ff7d4c5d610520`

  All the round commits are authored `kotoba-shokunin`.
- **Lane state.** `jj-lane.sh state` printed
  `state branch=master local=1d44bd82… remote=1d44bd82… ahead=0 behind=0 head=detached tracked=0 untracked=0`.
  `git status --porcelain` printed nothing. `git ls-remote origin refs/heads/master` printed
  `1d44bd820cf4ec53a37baba2b45f6da7776a84bd`.
- **Prompt.** `.ufo/prompts/kotoba-round-97.md` (103929 B; last commit `5225db97`, 07:56:48, just
  before the relaunch):
  - its `##` headings 1–5 equal those of `templates/round-prompt.md`;
  - `templates/round-prompt.md` is byte-identical to the canonical
    `kimi-shokunin/templates/round-prompt.md` (`cmp` rc 0);
  - `diff` of template lines 1–140 against prompt lines 1–140 shows only placeholder substitutions
    (`{{LANE}}`, `{{ROUND}}`, `{{FLEET_ROOT}}`, `{{AXES}}`);
  - the hyaku addendum is §6.

  The template contract is carried.
- **Evidence timing.** Landing receipts are dated 07:59–08:15 and ship in `38361a2` (08:17:12), so
  no evidence is future-dated.
- **Conformance notes (status-neutral):**
  - the report names `fa1bebae` as base, and the closure prompt names the freeze `148395bf` as
    "before". Both are consistent: the instruments and the freeze were landed by the first attempt;
  - attempts 2 and 3 each died within 30 s of launch, which is a driver-side issue;
  - the first attempt left the integration staged and uncommitted from 01:07 to 07:56. The relaunch
    re-verified and landed it at 07:58:32 (`693be9c3`).

## Claim re-checks

### C1 — depth: the self-test kills thirteen more frozen survivors t01..t13

Re-measured structurally by the reviewer; the kill tally is evidence-verified (lane gate, not run).

- **Plan unchanged after the freeze.** `git diff --stat 148395bf 1d44bd82 -- plans/round-97.md` is
  empty. The predicate, target, kill rule and frozen mutant list are at `plans/round-97.md` lines
  72–97 of the freeze.
- **Production identity.**
  - `diff <(git show fa1bebae:verifiers/verify_dispatch_prompts.py) <(git show 693be9c3:…) | grep -E '^[0-9]'`
    gives `1102a1103,1333`, a single pure insertion.
  - `grep -nE '^def '` puts `def self_test()` at line 679 and the next top-level def
    (`box_proof`) at 1344, so the insertion lies inside `self_test()`.
  - `693be9c3` → `1d44bd82` leaves the file unchanged (`diff` rc 0).
- **Arm targets.** The added lines name every target, from `t01` to `t13`
  (`grep -oE 't(0[1-9]|1[0-3])\b' | sort -u`): 13 of 13.
- **Assertions.** Static `rec(` call sites go from 62 (`fa1bebae`) to 90 (`693be9c3`), +28. The
  committed runtime tally is `0 failure(s) over 78 assertions` (base runs in
  `receipts/redbefore-c1-base.txt`) → `0 failure(s) over 105 assertions` (`receipts/landing/dp-selftest.txt`,
  rc 0), +27. The two deltas agree up to one conditional site.
- **Kill tally (evidence-verified).**
  - Before, `receipts/redbefore-c1-base.txt`: `C1 targets killed 0 of 13 (run errors 0) … C1-PREDICATE-UNMET`, rc 1.
  - After, `receipts/landing/c1-v5.txt` at `693be9c3`:
    `C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13`,
    `rules v5: honest runs CLEAN 3 of 3; mirror runs reported 14 of 14`, `C1-PREDICATE-MET`, rc 0.
  - `receipts/landing/c1-rulesv4.txt`: the same tally under `--rules v4`, MET, rc 0.
- **Kill-rule conjuncts (evidence-verified).** Each is rc 0 at landing:
  - `r96c1-v5.txt` `R96C1-PREDICATE-MET`;
  - `r95c1-v5.txt` `R95C1-PREDICATE-MET`;
  - `dp-boxproof.txt` `boxes proven 2`.
- **Counter identity.** `sha256sum` of `verifiers/fixtures/round-97/selftest-kills.py` is
  `b4200c5209b1c8a7…` at `94a10217`, `148395bf`, `693be9c3` and `1d44bd82`.
- **Bound (from the lane's own critic).** `.ufo/waves/round-97/w1/CriticClaimR97.md` line 102 says
  that of the 13 targets, 12 are real verdict errors and one, t09 (`note` dropped), is cosmetic: no
  verifier reads the note. The frozen predicate counts it, so the claim is met as frozen, and the
  report discloses it (addendum A5). The substantive move is 12 verdict-bearing mutants plus one
  observable-only mutant.
- **Result.** Reported 0 → 13 of 13; the committed evidence agrees. **Verified.**

### C2 — consistency (calibration sub-axis): v5 refuses g3/g7/g8 while h1/h2 hold

Counter-bytes identity was re-measured by the reviewer; the forgery tally is evidence-verified.

- **Frozen predicate.** `plans/round-97.md` lines 104–120 at the freeze: forgeries refused 3 of 3
  and honest held 2 of 2. g2b is a disclosed bound and is not scored. The claim dies if the counter
  bytes differ from the instrument commit.
- **Counter and runner bytes.** `selftest-kills.py` (`b4200c52…`) and `forgery-controls.py`
  (`28fbdb9ff9469763…`) are identical from the instrument commit `94a10217` through the tip
  (re-measured above).
- **Do-nothing control.** `receipts/c2-before-v4.txt`:
  `C2 v4: forgeries refused 0 of 3; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-UNMET`, rc 1.
- **Cause control.** `receipts/c2-v5-as-v4.txt`: `C2 v5-as-v4: forgeries refused 0 of 3 …`, UNMET,
  rc 1.
- **After.** `receipts/landing/c2-v5.txt` at `693be9c3` reads:
  - g3-recompile-compare, g7-stateful-fake and g8-clone-marker each give `R96C1-PREDICATE-UNMET` rc 1;
  - h1 (`801dd9bc`) and h2 (`693be9c3`) give MET;
  - final lines: `C2 v5: forgeries refused 3 of 3; honest held 2 of 2; bound g2b MET`,
    `C2-PREDICATE-MET`, rc 0.
- **Bounds, disclosed by the lane and not rescued.** These are addendum-1 A1–A3 and `corpus/QUALITY.md` Q87:
  - g10 (committed-reference sniffer) reads MET under v5;
  - g11 reads MET under a replayed `KOTOBA_R97_SEED`;
  - counter-rule mutants V4–V9 survive C2's worlds.

  The claim is met as frozen. It is not a general no-arm refusal.
- **Result.** Reported 0 → 3 of 3; the committed evidence agrees. **Verified.**

### No-harm (evidence-verified; SCORECARD re-read)

- **SCORECARD.** `git diff 148395bf 1d44bd82 -- SCORECARD.md` appends only the round-97
  annotations and the round-98 intentions. Every axis score is held (depth 9, consistency 10), and
  no row is rewritten.
- **Unchanged files.** `SKILL.md`, `PROVINCE.md` and `corpus/knowledge/` show an empty diff over the
  round.
- **Landing receipts.** All of these are rc 0:
  - `r96-c1`, `r96-r95c1`, `r95-c1`, `r95-r94c1` and `r93-c1-killpin` each give MET;
  - `r92-controls`: `shortcuts refused 2 of 2; honest held 2 of 2`;
  - `dp-live-equal` (live verdict lines identical between base and landing);
  - `gate-registry`: `74 of 74 … phantom 0`;
  - `floors-selftest`: `0 failure(s) over 176 assertions`;
  - `skill-identity`.
- **Tip battery.** `tip-battery.txt` reads `guards 5 of 5; tip battery exit 0: 3 of 6`, rc 1. The
  red gates are `verify_skill_checklist`, `verify_corpus_integrity` and `verify_corpus_independent`,
  exactly the three red in round 96's `.ufo/waves/round-96/receipts/landing/tip-battery.txt`. This is
  a carried red: not new harm, and a conformance defect routed below.

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | C1 verified: the self-test kills 0 → 13 of 13 frozen survivors (one of them observable-only, t09). Production code is byte-identical outside `self_test()` |
| consistency | improved | C2 verified: the v5 counter refuses 0 → 3 of 3 committed no-arm forgery worlds, and the honest worlds hold 2 of 2. Bounded by g10/g11 (Q87) |
| coverage | unchanged | no knowledge entry and no owned surface changed |
| operability | unchanged | tip battery 3 of 6, the same reds as round 96 |
| freshness | unchanged | no change |
| calibration | unchanged | C2 is graded on the lane's consistency row (its calibration sub-axis). The calibration row itself did not move |
| adjacency | unchanged | PROVINCE.md unchanged. The ConnectorOverlapR97 sibling finding was reported, not absorbed |

No axis was harmed.

## Discernment spot-check (lesson `round-97.md` § Gate)

Sources were re-opened by the reviewer on 2026-11-06 with
`curl -sS -L -w '%{http_code} %{size_download}'` and then `sha256sum`.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S273 Bazel Test encyclopedia | admit (A, mined) | https://bazel.build/reference/test-encyclopedia → 200, 223640 B | agree | Line 656 is `<h2 … id="test-interaction-filesystem">`. Lines 659–661 hold the quote: "Tests should create files only within the directories specified by `$TEST_TMPDIR` and `$TEST_UNDECLARED_OUTPUTS_DIR` (if set). These directories will be initially empty." `wc -w` gives 21, within the ≤25 limit. The quote grounds per-run fresh TMPDIR/HOME (v5 rule 4). The size and line numbers match exactly. The sha256 differs (`7bab4660…` vs the recorded `6b07e08f…`): the page is regenerated with build-specific ids, so its whole-page digest is not reproducible (routed below) |
| S274 GoogleTest Advanced (registry row quote) | admit (A, mined) | https://google.github.io/googletest/advanced.html → 200, 214623 B, sha256 `7317f5e7…` (equal to the recorded value) | agree | Line 2110 is `<h3 id="shuffling-the-tests">`. Lines 2112–2113 carry the quote, which is 25 words, at the limit. `--gtest_shuffle` occurs exactly once. The source grounds shuffled honest bracketing (rule 6) |
| S275 pytest `tmp_path` | reject (redundant corroboration) | https://docs.pytest.org/en/stable/how-to/tmp_path.html → 200, 40121 B, sha256 `dbc7d4b7…` (equal to the recorded value) | agree | Lines 314–315 carry "…a temporary directory unique to each test function." (8 words). S273 already grounds run isolation. The per-test-function fixture adds no distinct rule to the counter, and the flip condition is stated. The rejection is a curation choice on a sound source, which is correct |

The new SOURCES rows S273 and S274 were re-opened, and their quotes are located at the stated lines
within ≤25 words.

**Census.** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exits
rc 0 with last line `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md` and 34 `W04` lines, the same as
round start. Rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`) go from 198 at `fa1bebae`
to 202 at `1d44bd82`, matching the report.

**Mistake mining.** `## Mistakes` mines `shared-state-between-scored-runs`. `corpus/QUALITY.md`
row Q87 cites `corpus/lessons/round-97.md`. The fix can fail: v5-as-v4 refuses 0 of 3.

**Correction.** C97-1 (the round-96 S272 word count, 19 recorded vs 22 measured) is appended to
§ Corrections. This closes round-96 routed defect 1.

## Trend verdicts

- **expansion: unchanged.** `git diff --stat fa1bebae 1d44bd82 -- corpus/knowledge` is empty. The
  four new rows are registry rows; no admitted knowledge entry was added.
- **quality: improved.** The province instrument's self-test now catches 13 frozen behaviours it
  missed, 12 of them verdict-bearing. The kill counter refuses three forgery classes it accepted. The
  round-96 receipt error is corrected append-only. No admitted entry failed a re-check.
- **discernment: improved.** The non-author spot-check agrees with the gate on both admits and the
  reject sampled. The mined mistake became Q87, citing its lesson. New forgery classes g10/g11 were
  named as bounds rather than claimed away.

## Routed defects (lane fixes next round)

1. Tip battery `3 of 6`: `verify_skill_checklist`, `verify_corpus_integrity` and
   `verify_corpus_independent` are still red. This is carried from round 96, and the lane owes a
   disposition or fix.
2. g10 (committed-reference) and g11 (seeded replay) read MET under v5 (A1/A2, Q87 bound). The
   round-98 v6 counter is the declared vehicle.
3. Counter-rule mutants V4–V9 survive C2's control worlds (A3). The rules are not yet pinned by
   committed controls.
4. MutTesterDispatchR97 left 11 new dispatch-checker survivors (A4).
5. A5 items:
   - the counter exits with an uncaught-exception traceback instead of the exit ladder;
   - the `dispatch_prompts` assertion floor is 56 against 105 observed, and should be raised;
   - t10's behaviour depends on running as root.
6. Kill-set hygiene: t09 was a cosmetic, observable-only mutant counted as a kill target. Future
   frozen kill sets should exclude no-verdict mutants or label them separately.
7. S273 access record: the whole-page sha256 of bazel.build does not reproduce on re-fetch (same size
   and lines, different bytes). Record an excerpt digest, or mark the page dynamic, so a re-open can
   verify the access record.
8. Orchestrator/operator, not lane:
   - the wave validator rejects a `planner` seat, so the L1 held it;
   - retry attempts 2 and 3 died within 30 s;
   - the first attempt left post-freeze integration uncommitted for about 6 h.
