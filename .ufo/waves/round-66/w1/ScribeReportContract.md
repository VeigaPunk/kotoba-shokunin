# ScribeReportContract — round-66 W1 report-contract comparison (read-only seat)

Scope: compare the round-66 kotoba fleet report against the canonical report contract, its
declared claims, its committed receipts, the census outputs, trend verdicts, SHONEN boxes and
the Stale-lane line. Missing or unresolved evidence only; no fleet file, claim, counter,
threshold, plan or receipt was edited.

## Revisions read (not re-measured)

| Role | Revision |
|---|---|
| Pinned claim base (plan) | `11385e04e368c1e94ab1a5a89d7439033eb1f855` |
| Lane revisions cited by the report | `e7d1d8c`, `806b53b`, `daedcdf`, `4119647`, `fc1b71e`, `9e75e734` |
| Lane tip when the fleet report was committed | `9e75e7345574af59d0585429a0f25b6179aa375d` (2026-10-24 04:20:01 -0300) |
| Fleet report commit | `1154d57a9ebb17faa4c9f8f456a6e53c51c230ae` (author `kotoba-shokunin <kotoba@shokunin.local>`, 04:23:35 -0300), only file `.ufo/reports/round-66/kotoba.md`, byte-identical to the worktree draft, ancestor of fleet HEAD, present on `origin/main` and `origin/master` |
| Current lane HEAD (post-report, non-author) | `2a8eba56b3f9321b70c569fa2816d42237ca49a2` — `round-66 verifier spot-check (integrator, hyaku): non-author admit/reject`, 04:26:20 -0300 |
| Current lane worktree | `M .ufo/waves/round-66/w1/swarm-registry.json`, untracked `w1/ScoutS122Reopen.md` (live W1 seats) |
| Fleet worktree | detached at `a54d40c8`; 12 `.ufo/state/*.report-baseline` files plus `.ufo/watchdog.log` and fleet `SCORECARD.md` modified, several untracked files present (none authored by this seat) |

Method: committed objects only — `git cat-file -t`, `git merge-base --is-ancestor`,
`git show <rev>:<path> | sha256sum`, `git log/diff --name-status/--numstat`, `grep`, `sed`,
`python3` (JSON parse, block diff). I executed no verifier, gate, self-test or mutation run,
so no line below is a re-measurement of any claim; values quoted from receipts are the
receipts' own bytes.

## Contract comparison

Source of the contract: `templates/round-prompt.md` §4 (required sections, in order, and the
marker rule) plus `scripts/hyaku/lane-addendum.md` items 6–7 (Trend verdicts, Stale-lane,
tool installs).

| Required item | Report state |
|---|---|
| **Work performed** opens with the declared claims and axes | Present, line 5: C1 depth, C2 consistency/calibration sub-axis |
| **Landed changes** tied to LOG.md and commit hashes | Present, lines 16–23; traceability gaps F5/F6 |
| **Before → after measurements** (counting command + measured commit, one per claim) | Present, lines 27, 28; C2 before-pointer gap F1; revision gap F2 |
| **Sources & frontier** (row count command, added-by-tier, touched old→new, frontier advanced) | Present, lines 30–34; all four elements present and verified |
| **Trend verdicts** expansion / quality / discernment with evidence, no scalar | Present, lines 82–84; discernment conflict F3 |
| **SHONEN** heading, one line per box | Present, lines 86–91: 4 lines, all `[~]`; box-3 pointer drift F4 |
| Stale-lane line (respawn-per-round; no other mission open) | Present, line 93; status snapshot superseded F8 |
| Tool installs | Present, line 94: `Tool installs: none.` |

No required section is missing, extra top-level sections do not exist, and the report carries
real committed evidence — it is not a marker under the contract's marker rule.

## Verified concordances (evidence read, not executed)

- All six cited lane commits resolve as commits and are ancestors of current HEAD `2a8eba5`;
  `078eec4` (SHONEN box-2 pointer) also resolves and is an ancestor.
- Instrument shas at `9e75e734` equal the shas printed inside the receipts:
  `check_scoped_rules_v32.py` `97d89716…`, `verify_corpus_integrity.py` `febfa57e…`,
  `verify_corpus_independent.py` `de51f457…`, `check_r66_routed_repairs.py` `3129c0d7…`.
  The counter sha at its freeze commit `e7d1d8c` is also `3129c0d7…`, so the frozen counter
  bytes are unchanged at the tip.
- C1 receipts match the report: `234` → `240` assertions, `worlds reject 7 of 7`,
  `eligible rows pass 4 of 4`, `survivors closed 6 of 6`, the G9 disabled-admit must-fail
  line, five mutants exit 1 with the named witness/control attribution
  (`C1-measure.txt`, `C1-landed-measure.txt`, `C1-kill.txt`, `controls/C1-one-word-control.txt`).
- C2 receipts match the report: base `0 of 2` exit 1 → `2 of 2` exit 0
  (`C2-before.txt`, `C2-routed-after.txt`); primary gate `9/9`, `tracked=118 unindexed=0`,
  `report_dead=0/79`, `commit_total=37 unresolvable=0 nonhash=0` (`C2-integrity-after.txt`);
  independent `commit_total=37 unresolvable=0` after a `38 / 3` red at `4119647`, self-test
  103 assertions (`C2-independent-*.txt`); floors 15 PASS at 240/161/103 (`FLOORS-after.txt`);
  registry `43 of 43` (`REGISTRY-after.txt`); checklist `pass=11` (`CHECKLIST-after.txt`).
- Counter pins in `verifiers/check_r66_routed_repairs.py:41-49` are exactly the plan's frozen
  values 118 / 0 / 79 / 0 / 37 / 0 / 0.
- SOURCES: `grep -c '^| S'` reads 119 at `11385e04` and 120 at current HEAD; row 133 is S122
  (tier A, `mined`, opened 2026-10-24, recheck 180d, `used-by` =
  `corpus/knowledge/fleet-commit-resolution-round66.md, corpus/lessons/round-66.md`). The
  base→tip SOURCES diff is +3 lines only (the S122 row plus two append-only search notes); no
  existing row cell changed.
- Census receipts: both carry 16 `W04` notices + `kotoba ok …` + `exit=0`, identical content.
- SHONEN.md has 4 boxes; the report mirrors all 4 as `[~]`. Boxes 1, 2 and 4 pointers resolve
  exactly (`.ufo/round-46/scouts/B2.md:44`; `LOG.md:287,294,342` at `078eec4`;
  `PROVINCE.md:35` §Adjacent and the SHONEN.md evidence text).
- Wave evidence: `w1-spec.json` has 35 items with role counts exactly as reported
  (reviewer 11, scout 6, scribe 5, mutation-tester 5, critic 4, executor 3, connector 1; no
  planner item); the committed `w1/swarm-registry.json` at `9e75e734` has 35 members with
  `agentId: null`; `wave-prepared.txt` matches.
- No `kotoba | round-66` line exists in `.ufo/l0-questions.md`, consistent with
  "no L0 question … needed". I installed no tool.

## Findings — missing or unresolved evidence

**F1 (medium) — C2 before-values have no committed receipt pointer.**
Line 28 reports `Pinned base 11385e04…: r66 routed defects closed 0 of 2, exit 1` without
naming the file that holds it. The frozen controls exist and are committed at `e7d1d8c`:
`controls/C2-before.txt` (prints `0 of 2`, `D1…FAIL`, `D2…FAIL`, exit 1, plus the sandbox
gate's `4/9 checks pass` DRIFT block) and `controls/C2-counter-selftest.txt`
(`0 failure(s) over 14 assertions`, sha `3129c0d7…`). The report text contains zero
occurrences of `C2-before` or `C2-counter-selftest`, while the parallel C1 bullet (line 27)
does cite its control (`controls/C1-one-word-control.txt`). The contract item requires
command + measured commit (both present), so this is an evidence-pointer gap, not a missing
section.

**F2 (medium) — after-values were measured at `fc1b71e`, not at the plan's round-66 tip.**
`plans/round-66.md` freezes `check_r66_routed_repairs.py --rev <round-66-tip>` = `2 of 2`
and `verify_corpus_integrity.py` exit 0 "at the final lane tree". The report (line 28) and
`receipts/C2-routed-after.txt` / `C2-integrity-after.txt` name `fc1b71e`; the lane tip at
report filing was `9e75e734`, one commit later, and no receipt runs either command at
`9e75e734`. Mitigation measured here: the four instruments' sha256 at `9e75e734` equal the
receipts' pinned shas, and `9e75e734`'s file set contains no verifier source change — so a
tip-equal result is plausible, but it is not recorded.

**F3 (medium) — `discernment: unchanged` conflicts with a later non-author record.**
Report line 84 states the verdict above. Lane commit `2a8eba5` (lands 2 m 45 s after the
fleet report commit) adds `corpus/lessons/round-66-verifier-spotcheck.md`, which records an
outside agree on the S122 admit and closes with "trend verdicts: expansion unchanged, quality
improved, discernment improved. Round 66 is **admitted**." Both statements are in the
record; reported verbatim below for the canonical judge, not resolved here.

**F4 (low) — SHONEN box-3 pointer drift.**
Line 90 cites `corpus/lessons/round-8-aggregator-box3-coldrun.md:36-37,78,100`. `:36-37`
(B1/B2 rows) and `:78` (grade-impact line) resolve; `:100` is the heading
`## kotoba reconciliation (round 13, 2026-09-28)`, and the quoted sentence "Presentational
only — no verdict, count, or quotation above was changed." sits at `:102`. The report
inherits this pointer from `SHONEN.md`, so it is repeated drift, not newly introduced; the
pointer still resolves to the right section.

**F5 (low) — Landed changes omit `SKILL.md`, `corpus/QUALITY.md` and most README index rows.**
`git diff --name-status 11385e04 9e75e734` lists 40 paths. No Landed-changes bullet names
`SKILL.md` (modified at `806b53b` — v32 gate-row text plus the new
`check_r66_routed_repairs.py` row — and at `fc1b71e` — the two corpus-verifier rows) or
`corpus/QUALITY.md` (exactly +1 line at `806b53b`, the Q61 row now at
`corpus/QUALITY.md:76`). The `corpus/README.md` index rows are only partly covered: bullet 3
describes the `daedcdf` +2 row without naming the file, while the +6 rows at `806b53b` (four
r62–r65 spot-checks, r66 lesson, C2 knowledge entry) and the +1/−1 at `fc1b71e` are
unenumerated. Work performed line 8 names the index work, and every change is still under a
named commit, so this is completeness, not a marker.
Relatedly, line 10 says Q61 is "recorded in `corpus/lessons/round-66.md`"; there the lesson
only cites Q61 as captured-by — the criterion's definition is `corpus/QUALITY.md:76`.

**F6 (low) — LOG.md names 4 of the 6 cited lane commits.**
`LOG.md` §Round 66 (`LOG.md:2624`) contains `e7d1d8c` (1), `daedcdf` (1), `4119647` (1),
`fc1b71e` (3), and **zero** occurrences of `806b53b` and `9e75e73`. The report's blanket
sentence at line 16 ("Each item is recorded in … `LOG.md` §Round 66") is true at section level
and false at hash level for those two commits.

**F7 (informational) — census quote blocks are whitespace-normalized.**
Both quoted blocks (lines 37–56 and 59–78) reproduce the receipts' 16 `W04` rows + `kotoba ok`
line + `exit=0` in the same order, but the column separator is spaces; the receipt files use
tabs, and the report contains no tab character (`grep -cP '\t'` = 0). Content matches
semantically; a byte diff of "as recorded" block versus `census-before.txt` /
`census-after.txt` fails on separators only.

**F8 (informational) — two status statements are write-time snapshots, now superseded.**
Line 93 says "The current attempt is progressing from watchdog launch
`2026-10-24T03:25:51-03:00 …`"; `.ufo/watchdog.log:1169` records
`2026-10-24T04:24:00-03:00 complete kotoba round=66; hyaku-inline attempt=1`, 25 s after the
fleet report commit. Line 11 says `actual dispatched 0, returned 0, dead 0`; the orchestrator
has since dispatched the 35-seat W1 (this seat is one), so the cited
`w1/swarm-registry.json` no longer matches the worktree copy, though the committed copy at
`9e75e734` still has 35 `agentId: null` members. Neither statement was false when filed.

**F9 (informational, judge-owned) — calibration shape.**
C2 is filed on the calibration sub-axis but its counter counts routed-defect closure (0→2),
not mismatches between SCORECARD/SHONEN self-assessment and observed repo state; the report
contains no such mismatch count. The addendum's claim-sizing rule 9 requires one for a
calibration claim. Contract-wise the report is conformant; recorded for the canonical judge
only.

## Conflicts for the canonical judge (verbatim)

1. Discernment verdict:
   - Report, `.ufo/reports/round-66/kotoba.md:84`: "**discernment: unchanged** — this L1
     seat had no independent non-author round-66 admit/reject sample; `corpus/lessons/round-66.md`
     §Gate records that limit rather than claiming outside agreement."
   - `corpus/lessons/round-66-verifier-spotcheck.md` (lane commit `2a8eba5`, non-author
     integrator): "**discernment: improved** — my outside check agrees with the gate's only
     round-66 admit (S122); no reject was produced to disagree with …" and "Round 66 is
     **admitted**."
2. Measured revision: plan names `<round-66-tip>`; receipts and report name `fc1b71e`
   (F2). The integrator spot-check accepted the receipts without executing gates.

## Out of scope / untouched

- I did not execute any gate, verifier, self-test, mutation or census; I did not edit the
  report, plan, controls, receipts, LOG, SCORECARD, SOURCES, corpus, verifier or lane jj/Git
  state, and I did not touch the fleet root.
- This file is my only write. No subagent was dispatched (leaf member). No tool was installed
  (no pacman/uv/binary channel used).

## Artifact paths

- Compared report: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-66/kotoba.md`
  (= fleet commit `1154d57`)
- Contract: `/home/vgpnk/Projects/shokunin/templates/round-prompt.md` §4;
  `/home/vgpnk/Projects/shokunin/scripts/hyaku/lane-addendum.md` items 6–7
- Lane evidence base: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/`
  — `plans/round-66.md`, `.ufo/waves/round-66/{controls,receipts,census-before.txt,census-after.txt,w1-spec.json,w1/swarm-registry.json}`,
  `LOG.md:2624+`, `SCORECARD.md:383`, `SHONEN.md`, `corpus/SOURCES.md:133`,
  `corpus/QUALITY.md:76`, `corpus/lessons/round-66.md`,
  `corpus/lessons/round-66-verifier-spotcheck.md` (at `2a8eba5`),
  `verifiers/check_r66_routed_repairs.py`, `verifiers/corpus-baseline.json`
- This seat's report: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-66/w1/ScribeReportContract.md`
