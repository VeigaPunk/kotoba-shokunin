# ConnW2Report

role: UFO-FSD connector
item: ConnW2Report — cross-check the round-63 landed state at `cbbee56e9a3589b0b46736ad36f1b77701def80e` against PROTOCOL.md's round-robin report minimum (there is no numbered §4) and `.ufo/prompts/kotoba-round-63.md` §4 plus §6.6 extras. Produce the fleet-report skeleton. No production edit.

Axes named: **calibration** (judged; self-assessment vs committed bytes) and **depth** (must not be harmed). One move kept: stop the report from inheriting two false success signatures (census `17 W04`, and a receipt/LOG tie the tip does not contain). The G9 predicate is untouched.

Tools installed: none.

## Attack

Read-only. `git rev-parse HEAD` was `cbbee56e9a3589b0b46736ad36f1b77701def80e`. No verifier was re-run. The orchestrator's stated remeasure at this rev is ground truth and is not re-confirmed here.

```text
$ git log --oneline 35d44b4b4dcdda234b5dbff7af37e432fec55f05..cbbee56e9a3589b0b46736ad36f1b77701def80e
cbbee56 round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32), r62 routed-repairs counter, S119 + entry, LOG corrections (defects 1-4), w1 evidence
8c4cefa round-63: plan freeze and C1 do-nothing control (v31 5 of 6), census-before

$ git diff --name-status 35d44b4b4dcdda234b5dbff7af37e432fec55f05 8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
A	.ufo/waves/round-63/census-before.txt
A	.ufo/waves/round-63/controls/C1-do-nothing-v31.txt
A	plans/round-63.md

$ git diff --stat 35d44b4b4dcdda234b5dbff7af37e432fec55f05 cbbee56e9a3589b0b46736ad36f1b77701def80e -- LOG.md SCORECARD.md
 LOG.md | 9 +++++++++
 1 file changed, 9 insertions(+)
```

`SCORECARD.md` has no diff. `git show cbbee56e:LOG.md | grep -n 'Round 63\|round-63\|Round-63'` hits only the defect-3 correction bullet (line 2575). There is no Round 63 entry.

`git diff 35d44b4b..cbbee56e -- corpus/SOURCES.md` is `+17`: the S119 row and the search-log note at `corpus/SOURCES.md:221-235`. Registry rows (`awk` on `^\| S[0-9]+`): **116 at `35d44b4b` → 117 at `cbbee56e`** (only S119 added; S092 and S116 absent at both). `cmp` of SOURCES line 62 (the S049 row): **`S049_LINE_IDENTICAL`**. `grep -c icmje .ufo/waves/round-63/census-before.txt` → **0**.

Census contract, `scripts/sources-census.sh:32-33` and `:644-656`:

```text
#             E05 kind enum violation
#             E11 used-by path missing on disk
#             W04 same URL across scopes (warnings do not affect clean lanes)
```

Committed census bodies:

- `.ufo/waves/round-63/census-before.txt` (in `8c4cefa`): 16 `W04` lines, one `ok` line, `exit=0`. Every W04 line is `duplicate url … across scopes`.
- `.ufo/waves/round-63/census-interim.txt` (in `cbbee56e`): the same 16 `W04` lines, plus `E05 S119 kind=guidance`, two `E11` (missing used-by the knowledge entry and `corpus/lessons/round-63.md`), `exit=1`.
- `git ls-tree -r cbbee56e .ufo/waves/round-63/` has no `census-after.txt` and no C2-after receipt. The C1 receipt is `.ufo/waves/round-63/receipts/C1-g9-measure.txt`.

C1 receipt header (file text, not a re-run):

```text
C1 predicate: python3 -B verifiers/check_scoped_rules_v32.py --self-test
base 35d44b4b4dcdda234b5dbff7af37e432fec55f05 (working tree)
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
exit=0
```

C2 before, `.ufo/waves/round-63/controls/C2-before-r62tip.txt` (five `FAIL`, including `append-only prefix=True grew_by=0`):

```text
r62 routed defects closed 0 of 5
EXIT=1
```

Orchestrator ground truth, not re-run here: `--rev cbbee56e` prints `r62 routed defects closed 5 of 5`, exit 0.

S119 row (`corpus/SOURCES.md:131`): kind `docs`, tier `A`, status `mined`, recheck `365d`, used-by `corpus/knowledge/compound-clause-citation-round63.md, corpus/lessons/round-63.md`. Lesson quote counts: 16 words at snapshot `:170`, 7 words at `:172` (`corpus/lessons/round-63.md:22-23`).

`SHONEN.md` four boxes, all `[~]`, lines 5, 7, 9, 11 (evidence 6, 8, 10, 12). No diff this round.

Production diffs at the tip, `git diff -U0` hunk headers: `SKILL.md` adds the v32 and `check_r63_routed_repairs.py` registry rows; `PROVINCE.md` adds one frontier bullet at line 27; `corpus/QUALITY.md` replaces the Q57 row (`@@ -68 +68`) and appends Q58; `corpus/README.md` appends two index rows; `compound-clause-citation-round63.md` is new (109 lines).

## Verdict on the committed bytes

Wave 1 is two commits, both `kotoba-shokunin <kotoba@shokunin.local>`. The predicate numbers are nameable. Four report-contract ties are not. Contradictions, not averaged:

1. **Plan §C2 vs E1 vs the control.** `plans/round-63.md:111-117` still says check 4 passes at the r62 tip, so that paragraph alone is 1 of 5 (`CriticCalib` finding 1; `ScribeReportSkeleton` finding 3). Erratum E1 (`plans/round-63.md:150-158`) adds the growth conjunct. The committed control fails all five, `0 of 5`, `EXIT=1`. E1 and the control agree. Lines 111-117 are stale text in the same file. Cite the control. Do not cite 111-117 as the measurement.

2. **Plan "17 W04" vs what W04 counts.** `plans/round-63.md:137-138` expects after = exit 0, 17 W04 *because S119's URL is new*. W04 counts the same URL across scopes. A new URL adds zero W04 lines. Round 62's LOG says 15 → 16 W04 because S118 duplicates S103. S119's URL is absent from `census-before.txt`. Success for a new URL is **16 W04, exit 0, no line naming S119**. **17 W04 is the duplicate-URL / re-open signature**, which the same plan sentence says to record as a re-open. The lesson (`corpus/lessons/round-63.md:24`) says E05 was "fixed immediately" and E11 fixed "by this commit". The only committed census after the row is `census-interim.txt`, which still has both errors and records kind `guidance`. The committed row's kind is `docs`. Those files disagree. Neither is a tip census.

3. **C1 receipt rev vs the rev the report must name.** The three predicate lines match the orchestrator's remeasure at `cbbee56e`. The receipt's line 3 names the working tree at `35d44b4b`, not `cbbee56e`. `PROVINCE.md:27`, the new README index row, and the SKILL registry row state `6 of 6` and `5 of 5` without naming `cbbee56e`. Citing them as the tip measurement repeats r62 defect 2a, the class C2 claims to close.

4. **LOG tie and the 8.5/10 collision.** §4 requires every landed change tied to a LOG.md entry and a commit. The only LOG delta is the nine-line `### Round-62 corrections` block. It covers spot-check defects 1–4. It does not name v32, the C2 counter, S119, the lesson, the knowledge entry, or the SKILL/PROVINCE/QUALITY/README edits. `SCORECARD.md` has no round-63 row: depth stays 9 (`:28`); owned consistency/calibration stays 10 (`:29`). The plan's "lowest owned axis (calibration/consistency 8.5)" is the round-47 advisory disposition (`SCORECARD.md:365`), not the owned row. `CriticCalib` finding 6 already separates them.

5. **Bounds the headline must not swallow.** `CriticC1Bound` attacks reading `6 of 6` as semantic closure or a depth increase, and does not attack the six-instance numerator. `CriticCalib` attacks reading `5 of 5` as five routed defects closed or as a numeric calibration move. `ConnSibling` routes both moves `kotoba`. Q57 was edited in place; the LOG prefix check does not see that.

## Sections the L1 cannot fill honestly

| Section | Fillable now | Not honest if written as |
|---|---|---|
| Work performed | C1 depth, C2 calibration, both commits | "lowest owned axis 8.5" without owned-row 10 at `SCORECARD.md:29` |
| Landed changes | The commit table below | "each tied to a round-63 LOG entry" — none exists |
| Before → after | Both commands, both before receipts, orchestrator tip numbers | `C1-g9-measure.txt` as measured at `cbbee56e`; any C2-after path |
| Sources & frontier | Before 16 W04 exit 0; rows 116→117; S119 tier A kind docs; S049 bytes unchanged | After = 17 W04, or exit 0 copied from the plan or lesson line 24 |
| Trend verdicts | The evidence each word must not contradict | Any of the four words locked before wave 2 |
| SHONEN | Four `[~]` lines with committed pointers | Any `[x]` |
| Stale-lane | No other kotoba prompt; this round still open | Calling round 63 closed or silent |
| Cross-domain | Both moves `kotoba` (`ConnSibling.md`) | A sibling handoff |
| Tool installs | None in the wave-1 reports grepped | A package version |

## Proposed move

Write the fleet report from the skeleton below. Before that report is committed, append — do not rewrite — the Round 63 LOG entry in the exact text here, and commit a `census-after.txt` plus C1/C2 receipts whose headers name the rev being measured. Do not change either frozen predicate or any score.

Affected axis: **calibration**. Depth is not moved: the G9 predicate, the six-instance numerator, and score 9 stay. Owned consistency stays 10. Advisory 8.5 stays 8.5.

### Smallest safe correction — exact text to append to `LOG.md`

```markdown
## 2026-10-23 — Round 63 (hyaku run 5, attempt 3): C1 depth G9 clause guard; C2 calibration routed-repair checks

- Commits: plan/control/census-before `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8`; wave-1 build `cbbee56e9a3589b0b46736ad36f1b77701def80e`. This entry is the LOG tie for both. The `### Round-62 corrections` block above covers spot-check defects 1–4 only.
- C1 (depth; score held 9): `verifiers/check_scoped_rules_v32.py`. Frozen predicate `python3 -B verifiers/check_scoped_rules_v32.py --self-test`. Do-nothing control `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` at `35d44b4b` prints `survivors closed 5 of 6`. The committed receipt `.ufo/waves/round-63/receipts/C1-g9-measure.txt` is a working-tree run at `35d44b4b`, not a measurement at `cbbee56e`.
- C2 (calibration; owned score held 10; round-47 advisory disposition 8.5 unchanged): `verifiers/check_r63_routed_repairs.py`. Before `.ufo/waves/round-63/controls/C2-before-r62tip.txt` prints `r62 routed defects closed 0 of 5`, exit 1, under erratum E1 (check 4 fails on `grew_by=0`). `plans/round-63.md:111-117` (check 4 passes) is the pre-E1 paragraph and is not this measurement. No after receipt file is in `cbbee56e`.
- Landed in `cbbee56e` besides the two verifiers: `corpus/SOURCES.md` (S119 added, 116→117 registry rows; S049 row bytes unchanged; search-log note appended), `corpus/lessons/round-63.md`, `corpus/knowledge/compound-clause-citation-round63.md`, `corpus/QUALITY.md` (Q57 row edited in place; Q58 appended), `corpus/README.md`, `SKILL.md` (two registry rows), `PROVINCE.md` (one frontier bullet), `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md`, `.ufo/waves/round-63/` wave-1 evidence. `SCORECARD.md` not edited.
- Census: before 16 W04, exit 0 (`.ufo/waves/round-63/census-before.txt`). W04 counts duplicate URLs, so a new S119 URL does not target 17 W04. Interim `.ufo/waves/round-63/census-interim.txt` is 16 W04 + E05 + two E11, exit 1, and does not describe the committed `kind=docs` row. No census-after is in this commit.
```

That text does not assert the tip remeasure. If wave 2 adds a receipt, append a second bullet. Do not edit this one. An append keeps `35d44b4b:LOG.md` a prefix; a rewrite of the round-62 block fails C2 check 4.

## Report skeleton

Fleet path, written by the L1, not by this seat: `.ufo/reports/round-63/kotoba.md`. `PENDING-wave-2` means not fillable from `cbbee56e` bytes.

```markdown
## Work performed

C1 — depth: close the sixth frozen erratum survivor, G9 `e2f-compound-purpose-outside-citation`, by `verifiers/check_scoped_rules_v32.py`. Frozen predicate and the three required lines: `plans/round-63.md:35-49`. Depth score stays 9 (`SCORECARD.md:28`). `CriticC1Bound` finding 5: `6 of 6` is not a band move.

C2 — calibration: five repair checks over the r62 spot-check, computed from committed bytes by `verifiers/check_r63_routed_repairs.py --rev <rev>`. Frozen checks: `plans/round-63.md:88-109`, as refined by erratum E1 (`plans/round-63.md:150-158`). The owned scorecard row stays 10 (`SCORECARD.md:29`). The plan's "8.5" is the round-47 advisory disposition (`SCORECARD.md:365`), not that row. Numeric delta 0. `5 of 5` is five repair checks, not a claim that every §6 sub-item is new discrimination (`CriticCalib` findings 2 and 6).

- Plan, v31 do-nothing control, census-before: `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8`.
- Wave-1 build (v32, C2 counter, S119, lesson, entry, LOG corrections, w1 reports): `cbbee56e9a3589b0b46736ad36f1b77701def80e`.
- Mined mistake M94 (plan headline contradicted check 4; captured-by none; fix E1): `corpus/lessons/round-63.md:45`.
- Cross-domain: none to route. Both moves `kotoba` (`.ufo/waves/round-63/w1/ConnSibling.md`). Chousa's claim-support vocabulary was proposed as a citation, not absorbed.

## Landed changes

LOG tie for the rows below: **PENDING-wave-2** until the Round 63 entry above is committed. The only LOG text this round added at `cbbee56e` is `LOG.md` `### Round-62 corrections` (defects 1–4).

| Change | Commit |
|---|---|
| `plans/round-63.md`, `census-before.txt`, `controls/C1-do-nothing-v31.txt` | `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` |
| `verifiers/check_scoped_rules_v32.py` | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `verifiers/check_r63_routed_repairs.py` | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `LOG.md` round-62 correction block only | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `corpus/SOURCES.md` S119 row + search-log note (S049 row not rewritten) | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `corpus/lessons/round-63.md`, `corpus/knowledge/compound-clause-citation-round63.md` | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `corpus/QUALITY.md` Q57 edited in place, Q58 appended; `corpus/README.md` two index rows | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `SKILL.md` two registry rows; `PROVINCE.md` one frontier bullet | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md` (defect 1, was untracked) | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `.ufo/waves/round-63/` controls, interim census, C1 working-tree receipt, S119 snapshot, w1 reports | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |

`SCORECARD.md`: no change. Do not add a round-63 score row that raises depth or calibration.

## Before → after measurements

- C1 command: `python3 -B verifiers/check_scoped_rules_v32.py --self-test`.
  - Before / do-nothing, at `35d44b4b4dcdda234b5dbff7af37e432fec55f05`, receipt `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt`: `survivors closed 5 of 6`, and `e2f-compound-purpose-outside-citation: before accepted; after accepted`.
  - After, orchestrator remeasure at `cbbee56e9a3589b0b46736ad36f1b77701def80e` (this seat did not re-run it): `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, exit 0.
  - Do not cite `.ufo/waves/round-63/receipts/C1-g9-measure.txt` as that after-measurement. Its line 3 is `base 35d44b4b… (working tree)`. **PENDING-wave-2:** a receipt whose header names `cbbee56e`.
  - Bound (`CriticC1Bound`): `6 of 6` closes the frozen instance. It does not close semantic compound-purpose, and it does not move depth off 9.

- C2 command: `python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>`.
  - Before, `<rev>` = `35d44b4b4dcdda234b5dbff7af37e432fec55f05`, receipt `.ufo/waves/round-63/controls/C2-before-r62tip.txt`: five `FAIL` lines (check 4 `prefix=True grew_by=0`), `r62 routed defects closed 0 of 5`, `EXIT=1`. This is E1. It is not `plans/round-63.md:111-117`.
  - After, orchestrator remeasure at `cbbee56e`: `r62 routed defects closed 5 of 5`, exit 0. No receipt file is in the tree. **PENDING-wave-2:** the path of a receipt taken at the rev the report names. If wave 2 changes bytes, remeasure; do not keep this sentence under a newer rev.
  - Bound: five repair checks. Not "5 of 5 routed defects" in the spot-check's sense, and not history-level append-only (`CriticCalib` findings 2 and 5).

## Sources & frontier

Command, both sides:

```text
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
```

- Rows: 116 → 117. Added S119, tier **A**, kind **docs** (not `guidance`), status `mined`, opened 2026-10-23, recheck `365d`, used-by the round-63 knowledge entry and `corpus/lessons/round-63.md`. Quotes ≤25 words: lesson `:22-23`. Snapshot `.ufo/waves/round-63/snapshots/S119.page`, sha256 `d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2` as recorded on the row. The row says a same-size re-fetch hashed differently, so byte-identity across fetches is not claimed.
- Census before, at `8c4cefa`, file `.ufo/waves/round-63/census-before.txt`: **16 W04, exit 0**. S119's URL is not in that file.
- Census after: **PENDING-wave-2.** Do not write `17 W04`. A new URL stays at 16 W04 and adds no S119 line. 17 W04 means a new duplicate, which the plan says to record as a re-open. The only later committed census is `.ufo/waves/round-63/census-interim.txt`: 16 W04 + `E05 S119 kind=guidance` + two `E11`, `exit=1`. That E05 does not match the committed `kind=docs` row. Lesson line 24 is not a census result.
- Rows touched old → new: **S049 row bytes unchanged** (`cmp` of line 62). Status stays `mined`. Held receipt stays 17,403 B, sha256 `884c67ca…`, fetched 2026-10-22T20:09:33Z. The touch is the search-log append `corpus/SOURCES.md:221-235`: default `Accept` on 2026-10-23 is HTTP 200, 17,252 B, sha256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0`; `Accept: text/markdown` is HTTP 404, 389 B. Not a field rewrite.
- Frontier rows advanced: S119 new → `mined` (`corpus/lessons/round-63.md:49`). No other row's status field changed.
- Mistake mined: M94. Not a fourth claim.

## Trend verdicts

**PENDING-wave-2** for the word on each line. Evidence the chosen word must not contradict:

- expansion — a registry row was added (116→117) and two verifiers landed. `improved` is not available until `census-after.txt` is 16 W04, exit 0, with no S119 error line. If that re-run exits 1, the word is not `improved`.
- quality — the frozen G9 instance flips under the stated self-test lines. `CriticC1Bound` forbids reading that as semantic closure. Do not raise depth above 9.
- discernment — E1 made the before-count match the five arms (`0 of 5` with check 4 failing). That corrects M94. `CriticCalib` forbids reading `5 of 5` as general calibration or as a score move. No scalar.

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — `SHONEN.md:6` (round-46 inventory; round-57 recount; round-60 pointer). Untouched this round.
- [~] At least one end-to-end domain task executed and logged in LOG.md — `SHONEN.md:8` (`corpus/knowledge/cold-run-round11.md`). Untouched this round.
- [~] Instructions executable by an agent without oral context — `SHONEN.md:10` (round-8 aggregator cold run; no fresh non-author re-run). Untouched this round.
- [~] No cross-domain bleed (PROVINCE.md still accurate) — `SHONEN.md:12`, plus `.ufo/waves/round-63/w1/ConnSibling.md` (both moves `kotoba`). Still `[~]`: that scanner is lane-dispatched, not a non-author verifier.

No box is `[x]`. Defect 5 stays operator-owned (`plans/round-63.md:84`).

## Stale-lane

Respawn-per-round driver. No other kotoba mission is open: the dispatched kotoba prompt on disk is `.ufo/prompts/kotoba-round-63.md`, and a content grep of `.ufo/state` for `kotoba` matched nothing. This round's own mission is still open (wave 2 falsify) and is not silent: `cbbee56e` is a lane-authored commit after launch. Grade for any other mission: none found.

## Tool installs

None. Pacman pause held. Wave-1 reports grepped for `installed` / `uv tool` / `pacman` record only "none".
```

## Risks

- A census re-run that prints 17 W04 falsifies "S119's URL is new". The skeleton says to record a re-open. Writing 17 W04 as success would hide it.
- A wave-2 edit to v32 or the C2 counter makes the `cbbee56e` remeasure stale. After-paths stay PENDING so the report cannot keep pre-falsify numbers under a newer rev.
- Appending the LOG entry before wave-2 receipts is safe only because the text does not claim a tip receipt. Adding the receipt later by editing this entry is a LOG rewrite and can fail C2 check 4. Append a second bullet.
- Stating both "owned calibration 10" and "advisory 8.5" looks like two scores. It is two committed rows. Collapsing them is the harm this move refuses.

## Verification

For the L1, after the append and the wave-2 receipts. Not run by this seat.

1. `35d44b4b:LOG.md` is still a byte-prefix of the new LOG, and the new bytes contain the heading `Round 63`.
2. The census command pasted in full as `census-after.txt`. Pass for a new URL: 16 W04, exit 0, no `S119` error line. 17 W04 is not pass.
3. Both counting commands re-run at the rev the report names. Receipt headers name that same rev. `C1-g9-measure.txt:3` stays labeled working-tree-at-`35d44b4b`.
4. Report sections in §4 order, four `[~]` SHONEN lines, no `[x]`, trend words only after (1)–(3), no depth or calibration numeral changed in `SCORECARD.md`.
