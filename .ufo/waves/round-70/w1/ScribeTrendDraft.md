# ScribeTrendDraft — kotoba round 70, wave 1: draft Trend verdicts

Seat: `L1Kotoba70.ScribeTrendDraft` (scribe, read-only). Grounded only in committed bytes at
`16b212a390c7ce68b6bce49b2c3766b154fbcbae` (base `7d51253f99906b8551b6a0a108761eedac00de74`), against the
table in `/home/vgpnk/Projects/shokunin/LEARNING.md:31-38`. This is a draft written in prose for the
L1's report; it is not a verdict of record.

## Verdict (draft)

| Trend | Draft verdict | One-line basis |
|---|---|---|
| expansion | **improved** | one admitted entry on ground the lane did not hold, three new `mined` rows, indexed, and it passes its own bar at the tip |
| quality | **unchanged** | no existing entry was re-verified, deepened in place or superseded; the stale records (r69 errata, S201 log) were marked, not left; F2 was corrected before the report |
| discernment | **unchanged (provisional) — pending the outside spot-check** | `QUALITY.md` is byte-identical and no round-70 spot-check is recorded yet |

Trade check: `expansion: improved` alongside `quality: unchanged` is not a trade under
`LEARNING.md:37-38`, because quality is not harmed.

## Expansion — improved

- **Ground was not held at the base.** I ran `git show 7d51253:<f> | grep -c 'evaluating-skills\|evals.json'`
  over `corpus/SOURCES.md` and every `corpus/knowledge/*` file at the base, and every file printed
  0. The entry's `ground:` line says the same (`corpus/knowledge/skill-eval-artefacts-round70.md:6`).
- **New entry:** `corpus/knowledge/skill-eval-artefacts-round70.md` has eight fact rows, F1–F8
  (lines 17-26). Its three `source:` lines (lines 1-3) name S209, S210 and S211.
- **Each source is a `mined` row with 11 cells.** At `corpus/SOURCES.md:150-152`, an awk cell count
  printed `S209 11`, `S210 11` and `S211 11`. Each row's `used-by` names the entry.
- **Coverage-map row:** `corpus/README.md:133` ("Skill evaluation artefacts (round 70)").
- **The entry clears the bar it was admitted under.** I ran
  `TMPDIR=<scratch> python3 -B verifiers/check_skill_evals.py --rev 16b212a… --fetch`, which printed
  `measured-rev: 16b212a390c7ce68b6bce49b2c3766b154fbcbae`, `skill eval facts backed 8 of 8`,
  `live quotes found 8 of 8`, `exit=0`. The base control records `0 of 8`
  (`.ufo/waves/round-70/controls/C2-base.txt`), and the junk and forged controls both record `0 of 8`.
- **Spot re-reads of the snapshots:**
  - F7: `S210-optimizing-descriptions.md:92` carries "A should-trigger query passes if its trigger
    rate is above a threshold … A should-not-trigger query passes if its trigger rate is below that
    threshold."
  - F8: `S211-run_eval.py.txt:232` is `did_pass = trigger_rate >= trigger_threshold`, and line 234 is
    `did_pass = trigger_rate < trigger_threshold`.
  - Defaults: lines 266-267 set `--runs-per-query` to 3 and `--trigger-threshold` to 0.5.
  - The entry's odd-run-count argument (lines 46-56) therefore follows from the committed bytes.
- **Not on uncovered ground: F7.** F7 and the train/validation advice overlap the S124
  skill-creator loop the lane already held. The entry says so itself at line 44 ("matches the
  skill-creator loop the lane already held (S124)"). The net-new ground is F1–F6 and F8.
- **Other expansion observables did not move:**
  - No frontier area was entered: `git diff --stat 7d51253 16b212a -- PROVINCE.md` is empty.
  - There is no new kind of source. S211 is `code`, and the base already held 5 `code` rows
    (awk over `7d51253:corpus/SOURCES.md` printed `5`).
  - No capability was admitted to `SCORECARD.md`. The one SCORECARD addition is the r69 annotation
    block at `SCORECARD.md:431-436`.

## Quality — unchanged

- **No existing entry changed.** `git diff --stat 7d51253 16b212a` shows the only `corpus/knowledge/`
  change is the new file. `corpus/SOURCES.md` gained exactly three rows (+3, −0), so nothing was
  re-verified, deepened in place or superseded. The table's `improved` condition
  (`LEARNING.md:34`) is not met.
- **The r69 errata mark stale records; they do not leave them.**
  - `corpus/lessons/round-69.md:172` is the K69-10 erratum (18 → 22 assertions).
  - `corpus/lessons/round-69.md:173` is the K69-9 erratum (the omitted in-place edit to S201).
  - `corpus/lessons/round-70.md:155-158` logs S201's anchor change old→new: `(13 words)` →
    `(14 words)`.
  - `LOG.md:2698-2724` carries the r69 entry with the 10-receipt and 23 + 1 corrections, plus two
    governance notices.

  These keep the `harmed` condition ("found false or stale and left unmarked") clear. They are
  corrections to lesson and log records, though, not knowledge entries re-verifying, so they do not
  meet `improved`.
- **The F2 wording correction** (commit `ac3c0f1`, a one-line diff to the entry's line 20):
  - At `8edeb49` the entry said the three JSON files are "produced by the run, not written by the
    author".
  - The committed page says "produced during the eval process — by the agent, by scripts, or by
    you" (`S209-evaluating-skills.md:86`). The old wording contradicted the page; the new wording
    ("produced by the agent, by scripts, or by the author during the run") matches it.
  - The entry is page-true at the tip, so this is not harm. But: (a) the C2 counter printed 8 of 8
    on the false wording, because it checks the quote cell and key terms, not the fact cell — the
    Q51 class (`corpus/QUALITY.md` Q51); (b) the correction is recorded only in the commit message.
    `git grep -n 'F2' 16b212a -- corpus/lessons/round-70.md` finds nothing, so the lesson's
    `## Mistakes` (M113–M116) does not log it (see `LEARNING.md:19-21`).
- **Not upgraded to `unprovable-but-better`.** The entry's tier-A corroboration of the held S124
  loop and its documented `>=`/"above" disagreement are arguably a deepening. Under
  `LEARNING.md:46-48` that verdict needs a named non-author reviewer with reasons on record, and
  none exists at `16b212a`.

## Discernment — unchanged (provisional), pending the outside spot-check

- **No outside spot-check exists yet.** `corpus/lessons/round-70.md` carries only the suggested
  sample (lines 108-109: "admit S209 … and reject S301"). There is no agree/disagree record, and no
  kotoba round-70 report exists under `/home/vgpnk/Projects/shokunin/.ufo/reports/round-70/` (it holds
  `audio.md`, `game-dev-2d.md`, `game-dev-3d.md` and `kotodama.md`). Under `LEARNING.md:40-45` the
  verdict cannot be `improved` until a non-author records it. A subagent the lane dispatched does not
  count (`LEARNING.md:45`).
- **No criterion was added without a lesson.** `git diff --stat 7d51253 16b212a -- corpus/QUALITY.md`
  is empty, so the second `harmed` clause is not triggered.
- **No inherited disagreement is left unlearned.** The r69 closure recorded all agree, including the
  corrected S201 reject (`corpus/lessons/round-69-verifier-spotcheck.md:124-140`). It also recorded
  discernment `improved` via Q62 (same file, line 148).
- **The refusals rest on observations that are not in committed bytes.**
  `corpus/lessons/round-70.md:72-90` refuses four items:
  - S285/S286: "observed by fetching both forms".
  - S301: "opened this round".
  - S303: cites lines 64 and 68 of `improve_description.py`.
  - The staged `english-leads-relocated-round9.md`: refused because no bounded sweep was run. This
    is Q62-compliant, since it rests on a fact about this round's evidence.

  Only S209–S211 have committed snapshots (`git ls-tree -r --name-only 16b212a --
  .ufo/waves/round-70/snapshots` lists three files). The S301 line gives a title and a date but no
  URL, and `git grep 'S301' 16b212a` hits only staged-id lists and the two prose mentions. The
  outside checker therefore has to re-open the S301 reject live and cannot verify it from the tree.
- **What is pending, and what flips the verdict:**
  - A non-author (a fresh reviewer or the operator) has to re-open S209 and S301 and record
    agree/disagree with reasons in the round lesson. That needs at least one admit and one reject
    (`LEARNING.md:42-45`).
  - It flips to `improved` if the spot-check agrees on both, or if a disagreement becomes a lesson
    that adds a grounded `QUALITY.md` criterion.
  - It flips to `harmed` if a disagreement is left unlearned.
- **Open obligation (not a discernment trigger).** M116 says "Captured by: `none`"
  (`corpus/lessons/round-70.md:144`), but `QUALITY.md` carries no criterion citing M116 at
  `16b212a`. That is required by `LEARNING.md:19-21` ("when no criterion caught it, a `QUALITY.md`
  criterion citing that lesson"). M116 is a counter-design mistake, not a gate disagreement, so it
  does not move discernment under the table. The report should still either land the criterion or
  say why not.

## Findings to route (outside the verdicts)

1. **There is no committed C2 receipt at the tip.**
   `git ls-tree -r --name-only 16b212a -- .ufo/waves/round-70/receipts` lists `C1-measure.txt`,
   `K69-11-inplace.txt`, `census-before.txt` and `r69-tip-defense.txt`, and no C2 measurement. Under
   Q50, a report stating "8 of 8 at the tip" needs a receipt that names the final tip. My run above is
   a seat observation, not that receipt.
2. **The index row is stale.** `corpus/README.md:135` ("Round-70 lessons") lists "`## Mistakes`
   M113-M115", but the lesson at the tip carries M116 (`corpus/lessons/round-70.md:136`).
3. **The F2 correction is not logged in the lesson** (see Quality above).
4. **C1 stands a miss as declared at the tip, reproduced:**
   `TMPDIR=<scratch> python3 -B verifiers/check_r69_routed_repairs.py --rev 16b212a…` printed
   `r69 routed defects closed 9 of 10`, `K69-11: governance.citation_resolves FAIL`, `exit=1`. That
   matches `receipts/C1-measure.txt` at `8edeb49` and lesson M116. The in-place repair is shown only
   at `ac3c0f1`, outside the claim (`receipts/K69-11-inplace.txt`: `pass: 11`, `5 recorded
   correction(s) excused`). I did not re-run that in-place receipt.
5. **`SKILL.md` is at the budget:** 600 lines at `16b212a` (`git show 16b212a:SKILL.md | wc -l`
   printed `600`) against the ≤600 line limit in the plan's no-harm battery. One more line breaks it.

## Commands run (all read-only; scratch `/tmp/k70w1-ScribeTrendDraft.1dzv`, removed)

- `git log --oneline 7d51253..16b212a` and `git diff --stat 7d51253 16b212a` (42 files, +3447 −87).
- `git diff 7d51253 16b212a -- SKILL.md corpus/README.md corpus/SOURCES.md corpus/lessons/round-69.md
  SCORECARD.md verifiers/verify_skill_checklist.py verifiers/corpus-baseline.json LOG.md`.
- `git show ac3c0f1 -- corpus/knowledge/skill-eval-artefacts-round70.md` (the F2 diff).
- `git show 16b212a:<snapshot> | grep -n …` for S209:86, S210:92 and S211:232,234,266-267.
- The two counter runs above (C2: exit 0; C1: exit 1). The working tree was not modified.
  `git status --porcelain` showed only the wave's untracked `.ufo/waves/round-70/w1*` paths.

## Out of scope / unobserved

I did not run the plan's no-harm battery. I did not fetch S285, S286, S301 or S303, so the refusal
reasons are unverified by this seat. I did not perform the outside spot-check, and could not, since
this seat is lane-dispatched. Tools installed or updated: none.
