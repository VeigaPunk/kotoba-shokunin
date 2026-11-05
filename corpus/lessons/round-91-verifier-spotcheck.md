author: hyaku closure (non-author integrator, @m_zfl)

# Round 91 verifier spot-check (non-author closure of kotoba round 91)

Checked 2026-11-05 against lane tip `43d373b6739179d11594e4ae80e668e696f1716f` (branch `master`,
local == remote, `ahead=0` via `scripts/hyaku/jj-lane.sh state`); report
`.ufo/reports/round-91/kotoba.md` committed in the fleet repo by the lane identity `kotoba-shokunin`
(`2a6f80652e60c1068fce4ee336f4626e71b922a6`). I did not author the round; nothing lane-authored was
edited. Gate evidence was verified as committed bytes, never re-executed (PROTOCOL §Gate standard,
Closure consequence); counts over committed bytes were re-run by me.

## Step-1 conformance

- Report contract: `SHONEN` heading present with exactly 4 lines for the lane's 4 boxes, all `[~]`
  with resolvable pointers — one-to-one against `SHONEN.md`. Minimum substance present (work
  performed, evidence pointers, landed changes tied to LOG.md § Round 91 at line 3484, checkable
  hashes). Not a marker: real committed work. Status `ok`.
- Commits: `9af1a7af` (freeze), `c6631ca4` (A), `43d373b6` (B) all exist and
  `git merge-base --is-ancestor <hash> master` holds for each, plus round base `9264baaa`.
- Pushed: `jj-lane.sh state` → `branch=master local=43d373b6 remote=43d373b6 ahead=0 behind=0`;
  `git status --porcelain` shows one untracked file only (see defects).
- Prompt fidelity: `.ufo/prompts/kotoba-round-91.md` renders the full `templates/round-prompt.md`
  contract verbatim (§§1, 2, 2b, 3, 4, 5 — report path, commit-before-report, SHONEN heading rule,
  hash citation, write scope, L0 channel) plus hyaku addendum §6 and the §7 scratch directive; L2
  floor text matches `MISSION.md` §L2 concurrency (≥ 8 in one batched call).

## Claim re-checks (re-measured = my own command over committed bytes; evidence-verified = committed receipt)

- **C1 (depth) — VERIFIED (re-measured + evidence-verified).**
  - Mine: `git show <rev>:verifiers/fixtures/mutation-battery/manifest.tsv | grep -cP '\tkill\t'`
    → 14 at `9264baaa`, 14 at `9af1a7af`, 17 at `c6631ca4`, 17 at `43d373b6`.
  - Receipt `.ufo/waves/round-91/receipts/landing/c1-predicate-landing.txt` (committed): rev
    `c6631ca4`; `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed
    survivors 0 of 0`; `rc=0`; G1/G2/G3 PASS; `mb-m2`, `mb-m15`, `mb-m16` killed; ladder rows
    `fg-m3-ladder-refusal-to-2`, `fg-m3b-ladder-eval-to-1` killed. Base clone receipt:
    `killed 14 of 14`, rc 0 at `9af1a7af`.
  - Self-test: `c1-selftest-base.txt` 19 assertions rc 0 → `c1-selftest-landing.txt`
    `0 failure(s) over 25 assertions` rc 0 (≥ 22 met).
  - Base survivors: `.ufo/waves/round-90/w1/MutTesterBattery/transcripts/harness-run.log` lines 9,
    22, 23 show `mb-m2`, `mb-m15`, `mb-m16` SURVIVED at the round-90 base — the before-state is real.
- **C2 leg A (freshness) — VERIFIED (re-measured + evidence-verified).**
  - Mine: `grep -n '^SELF_TEST_TIMEOUT_S = \|MEASURED_SELFTEST_S = '` → 120 (line 202) at
    `9264baaa`; 360 (line 208) and `MEASURED_SELFTEST_S = 161` (line 214) at `43d373b6`.
  - `git rev-parse c6631ca4:verifiers/check_assertion_floors.py` =
    `6f2c52fb2e09e817dff3360b97400a5d6e53626c`; `INSTRUMENT_PINS` at landing lists exactly that blob
    as the round-91 admission.
  - Receipts: `harness-selftest-duration.txt` (wall 160.2 s at `9264baaa`, exit 0);
    `base-floors-selftest.txt` 165 assertions rc 0 → `floors-selftest-landing.txt` 176 rc 0;
    `tipbattery-before.txt` at `9264baaa`: `FAIL guard instrument-pin` (blob `c10c0f10` unpinned),
    `guards 4 of 5` → `tipbattery-landing.txt` at `c6631ca4`: pin guard PASS, `guards 5 of 5`,
    rc 1 from the three carried red corpus gates — exactly as reported;
    `floors-live-landing.txt`: 19/19 PASS incl. `floors_guard observed=176 floor=176` and
    `freeze_gate observed=31 floor=31`, rc 0, load 1.90 → 2.12.
- **C2 leg B (freshness) — VERIFIED (evidence-verified + committed able-to-fail).**
  - Self-test: `c2-freezegate-selftest-base.txt` 30 assertions rc 0 →
    `c2-freezegate-selftest-landing.txt` 31 rc 0.
  - Able-to-fail: `w1/ExecLadder/able-to-fail.txt` — repaired line reverted in a scratch world →
    `FAIL arm plan-not-utf8 could-not-evaluate` rc 1; the fix's red-before state is committed.
    `receipts/ladder-defect.md` re-derives the base defect. Coupling: `verifiers/floors-registry.json`
    carries `floors_guard=176`, `freeze_gate=31` (addendum A1).
- **Census — VERIFIED (re-measured).** `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 187 at
  `9264baaa`, 190 at `43d373b6`; `git diff 9af1a7af c6631ca4 -- corpus/SOURCES.md` removed lines = 0
  (append-only holds); `scripts/sources-census.sh validate --root … kotoba` → rc 0 (33 pre-existing
  W04 duplicate-URL warnings, final verdict `ok`).
- **Corpus/no-harm — VERIFIED.** `corpus-integrity-landing.json`:
  `corpus.index.unindexed` observed 0 PASS (base receipt: 1); `d5v3-landing` instance drift 3
  (`d5ii` PASS) vs `base-d5v3` drift 4 (`d5ii` FAIL); `gate-registry-landing` 74/74 rc 0;
  `sibling-census-landing` `province rows 20 matched 4` rc 1 — same as base;
  `province-core-landing` rows 0 of 2 rc 1 — unchanged (stale base pin, pre-existing);
  `base-skill-size.txt` SKILL.md 600 lines / 92,672 B; SCORECARD diff `9264baaa→43d373b6` is
  append-only annotations (depth held 9, no score lowered).

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | C1 verified: kill surface 14→17 with three base survivors now killed, self-test 19→25 |
| freshness | improved | C2 verified: cap 120→360 calibrated to a measured 160.2 s, instrument-pin admission repairs the r90 landing miss, freeze-gate ladder defect repaired with committed able-to-fail |
| calibration | improved | spot-check below agrees 3/3 on this round's gate decisions; misses mined as `## Mistakes` rows with routed fixes, not hidden |
| coverage | unchanged | no claim; PROVINCE § Core line records an own instrument; sibling census red carried unchanged |
| operability | unchanged | no claim; instruments still run (bare floors walk 19/19 rc 0; registry 74/74) |
| adjacency | unchanged | connector found no sibling copies; no cross-domain absorption; census unchanged |

## Spot-check table (discernment, LEARNING.md)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S262 PIT "Basic concepts" | admit (tier A) | `https://pitest.org/quickstart/basic_concepts` (HTTP 200, 12,155 B — byte size matches the row) | agree | all three located quotes found in the live page (stripped text) and at the cited raw-HTML lines: "…referred to as equivalent mutations." (line 123), "Killed means a test caught the mutation successfully." (line 175), "Survived means the mutation was not detected…" ; `No coverage` outcome present, so the added-value rationale vs S260 holds; scope honestly excludes the lane's battery mechanics and any score formula; word counts 18/8/11 ≤ 25 |
| S263 Python `subprocess` | admit (tier A) | `https://docs.python.org/3/library/subprocess.html` (HTTP 200, 208,648 B — byte size matches the row) | agree (one anchor slip) | both quotes verified in the live page; run() dt at line 270 and timeout paragraph at 288-292 match the row exactly, footer "Last updated on Nov 05, 2026 (12:47 UTC)" at line 2037 matches; the `Popen.communicate` contrast quote is present but sits at line 1071 (entry dt 1051), where the row and lesson cite line 1042 — quote text, section and meaning correct, one anchor line off; run()-vs-communicate contrast is the right contract for a `subprocess.run(..., timeout=cap)` guard |
| S264 Wikipedia "Mutation testing" | reject (tier C) | `https://en.wikipedia.org/wiki/Mutation_testing` (HTTP 200) | agree | score-formula sentence found verbatim ("the mutation score is the number of mutants killed / total number of mutants.") and the equivalent-mutant sentence is present; community-editable tertiary text is a lead, never sole support for a tier-A-scoped claim (CORPUS.md: `community` never A; C never sole support); the denominator-convention conflict with the round's two-sided rule is a real reason; flip condition recorded |

Note (S262 upstream corroboration): the row additionally cites the page's upstream source
`quickstart/basic_concepts.markdown` in `hcoles/pitest-site` (gh-pages) at `e8995cd59e3c`. My
Gitiles attempts (`pitest.googlesource.com` with `pitest-site`/`hcoles/pitest-site`, branch and
`refs/heads/gh-pages`, with and without the revision) returned NOT_FOUND, so that corroboration
pointer was not re-opened by me; the admitted row's grounding stands on the primary URL, which
resolves with matching size and located quotes. Sub-pointer graded `unprovable`, not `harmed`.

## Trend verdicts (closure, non-author)

- **expansion: improved.** Two admitted knowledge entries on ground the coverage map did not hold
  (`knowledge/mutation-battery-arms-round91.md` citing mined S262;
  `knowledge/timeout-calibration-round91.md` citing mined S263), each opening with the provenance
  trio and a committed `recheck:`; SOURCES 187→190 append-only; tier split A:2, C:1 (rejected).
- **quality: improved.** `corpus.index.unindexed` 1→0; tip battery instrument-pin guard FAIL→PASS
  (4/5→5/5) closing the round-90 landing miss; freeze-gate exit-ladder defect repaired with a
  committed red-before; D5 instance drift 4→3 with `d5ii` FAIL→PASS; both new entries' recheck
  constants re-derived green; no admitted entry failing its recheck.
- **discernment: improved.** Outside spot-check (this file) agrees with the gate on both admits and
  the reject (3/3), with reasons recorded above; the round's own misses (vacuous control, number
  drift, unpinned-blob landing, unsettled wave registry) are mined into `## Mistakes` with routed
  fixes rather than suppressed.

## Routed defects for the lane's next round (round 92)

1. `ctl-c2-capline-only` reads MET on its own shortcut world (declared exit 1, observed exit 0) and
   `ctl-c1-manifest-only` never reads its appended rows — frozen-declaration defects, disclosed and
   routed by the lane (addendum A5); redesign as committed shortcut worlds through the public path.
2. Battery bound: a dropped kill row keeps the self-test green and prints `killed 16 of 16`; only
   the exact predicate line catches it — add a self-test arm pinning the kill-set size (lane already
   plans this).
3. Ladder findings unrepaired: `--work` under a regular file raises uncaught `NotADirectoryError`;
   duplicate control names read as held; declared `exit 127` never compared.
4. S263 anchor slip: row and lesson cite the `Popen.communicate` contrast quote at HTML line 1042;
   the byte-identical page (208,648 B) has the entry at 1051 and the quote at 1071. Correct the
   anchor at next touch (append-only correction per SOURCES contract rule 2/3) — the quote itself
   is verified.
5. Untracked `.ufo/waves/round-91/r91-w1-results.json` appeared in the lane repo at 14:05 (one
   minute after the round's completion line) — the wave settlement the report requested, written by
   the orchestrator side, uncommitted. Resolve next round (commit or remove); not lane debt for
   round 91. The report's own open item (WAVE-DONE never received; `ReviewerRepairs` dead seat;
   attempt-1 registry unsettled) stands as disclosed.
6. Pre-existing census warnings: 33 W04 duplicate-URL-across-scopes rows (non-blocking, `ok`);
   `check_province_core` stale base pin `a5f7459` and red Frontier check carried unchanged.

Operator note (promotion-owned): the four SHONEN boxes carry resolvable pointers; this closure
re-verified the landing-run, executability and cross-domain boxes from committed receipts and gates.
The assessment remains asserted-by-author (`[~]`), so promotion review still owes its own non-author
pass.
