# SC03QualityRows — seat report (kotoba round 77, w1)

Seat: `SC03QualityRows` (scribe, leaf). Item: draft new `corpus/QUALITY.md` criteria from the r76 closure
and the r76 wave, rejecting any candidate an existing Q already covers, and deliver appendable table rows.

Axes I was working (named for the record): **depth** (a criterion whose mechanism is a class, not a
file), **consistency** (row shape, `supersedes` discipline, duplicate check), **calibration** (every row's
falsifier is a real world, and the rows that are *not* bar-level are refused), **operability** (each row
carries the command that shows it red or green), **freshness** (all evidence from the r76 closure/wave of
2026-10-27, re-measured at the current base).

Nothing was applied to a lane file: no claim data, no QUALITY append, no lesson edit. Two files written,
both in the wave dir.

## Behaviour

Read first: `corpus/QUALITY.md` (89 lines; last 15 rows and the append-only/supersedes rule at `:4-6,71-73`),
`plans/round-77.md`, `plans/round-76.md`, the r76 build drafts (`B08-q74-quality-row.diff`, `B08-notes.md`,
`lesson-draft.md`), `corpus/lessons/round-76-verifier-spotcheck.md` (§1 CD1–CD4, §5 R76-D1…D5), and the two
frozen counter docstrings (`verifiers/check_desc_craft.py:1-30`, `verifiers/check_r75_routed_repairs.py:1-26`).
The r76 addenda were read where a row depends on them: `plans/round-76-addendum-2.md` §1 (the base-gate exit
withdrawal, which Q75 cites); the other addenda were grepped for `QUALITY`/`Q7x`/`row` (no row guidance
beyond the Q73-pin note at addendum 2 §3) and not read in full.

Four candidates were scored; all four were admitted (none was already covered), and three further
candidates were refused: one as a duplicate of a row I drafted, two as not bar-level. The dispositions are
in the deliverable's first table.

## Evidence — every command run and what it printed

Measurements ran in `/fast/scratch/hyaku/kotoba-r77/SC03QualityRows/clone`
(`git clone --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin clone`; `git -C clone rev-parse
--show-toplevel` → that path; HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`) or read-only in the lane.

| # | command | observed | exit |
|---|---|---|---|
| 1 | `wc -l corpus/QUALITY.md`; `grep -n '^\| Q' corpus/QUALITY.md \| tail -1` | `89`; last row `Q73` at `:89` | 0 |
| 2 | `git show 6523ace:corpus/QUALITY.md \| sha256sum`; `git diff --stat -- corpus/QUALITY.md` | `08dbfae23b7cea190971cb1e931fedbe5a980cb577609d0bfe4336d83e8b1261`; empty diff | 0 |
| 3 | `git show 2f675548:SKILL.md \| python3 -c "import sys,yaml;t=sys.stdin.read();d=yaml.safe_load(t.split('---')[1])['description'];print(len(d),len(d.strip()),len(d.strip().split('. ')[0]+'.'))"` | `1022 1021 151` | 0 |
| 4 | same at `6523ace` | `1022 1021 151` | 0 |
| 5 | `git show 2f675548:SKILL.md \| awk 'NR>=3&&NR<=8{print NR ":" length($0)}'` + sum | `3:14 4:76 5:78 6:73 7:79 8:72`, `sum=392` | 0 |
| 6 | `git show 2f675548:SKILL.md \| sed -n '3,19p'` | `description: >` at `:3`, content `:4-18`, closing `---` at `:19` (16 source lines in the block incl. marker) | 0 |
| 7 | `python3 -B verifiers/verify_corpus_integrity.py --json` direct, in the clone | exit 1 | 1 |
| 8 | `python3 -B verifiers/verify_corpus_integrity.py --json 2>&1 \| tail -3` | exit 0 (pipe's status) | 0 |
| 9 | `python3 -B verifiers/verify_corpus_independent.py --json` direct / piped | exit 1 / exit 0 | 1 / 0 |
| 10 | `false \| cat >/dev/null; echo $?` / `false; echo $?` | `0` / `1` | 0 / 1 |
| 11 | `sed -n '1,12p' .ufo/waves/round-76/base-battery/base-battery.txt \| cat -n` | `:2` integrity header, `:3-5` JSON tail, `:6 exit=0`; `:7` independent header, `:8-10` JSON tail, `:11 exit=0` | 0 |
| 12 | `sha256sum .ufo/waves/round-76/base-battery/base-battery.txt`; `git cat-file -e 6523ace:<same>` | `27412fd742ab6f1186ecf9515a0bcbc07983729e7a4f64ba0a23869ba80f48fb`; present | 0 |
| 13 | `git cat-file -e <rev>:corpus/lessons/round-76.md` for `b7f13f4`, `6ce2724`, `2f675548`, `6523ace` | `128 128 128 128` | 128 ×4 |
| 14 | `grep -n 'round-76 lesson' plans/round-76.md` | `11:`, `74:` | 0 |
| 15 | `git show --name-status --pretty= 6ce2724` | `A kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md` (one path) | 0 |
| 16 | `git cat-file -e ec7f853:kotoba-shokukin/…/A18ScoutSnapshot.md` / `ec7f853:.ufo/…/A18ScoutSnapshot.md` | 128 / 0 | 128 / 0 |
| 17 | `git show ec7f853:.ufo/… \| sha256sum` / `git show 6ce2724:kotoba-shokukin/… \| sha256sum` | both `ae39b182e2bf4b95b7337f65fb6ceb4cb423e5b37fd4c0ffb9e49de9238118fb` | 0 |
| 18 | `git ls-tree -r --name-only 6523ace \| grep -c '^kotoba-shokukin/'`; `git log --oneline --all -- <each typo path>` | `2`; added by `ac9f295` (r75) and `6ce2724` (r76) | 0 |
| 19 | `grep -n '^| M76-1\|^| M76-7\|^| M76-8' .ufo/waves/round-77/build/SC01Lesson76.round-76.md` | rows at `:104`, `:108`, `:109` | 0 |
| 20 | `grep -rn 'Q74\|Q75\|Q76\|Q77' verifiers/ SKILL.md plans/round-77.md` | no matches | 1 |
| 21 | row-shape check over the deliverable (unescaped-pipe split) | 4 rows, 5 fields each | 0 |
| 22 | `sed -n '7p' plans/round-76-addendum-2.md`; `grep -n 'exit=' .ufo/waves/round-76/base-battery/base-gate-correction.txt`; `git cat-file -e 6523ace:<same>` | "the command pipeline recorded `tail`'s exit status, not the gate process status"; the corrected receipt reads `139:exit=1`, `270:exit=1` and is committed | 0 |

Rows 7–10 are a *falsifier observation*, not a gate verdict: both corpus gates are red at `6523ace`
(pre-existing base condition, routed as R76-D4) and I am only showing that the receipt's recorded `exit=0`
is the pipe's. I did **not** run `check_desc_craft.py` or `check_r75_routed_repairs.py`; nothing in the
rows relies on their output.

## Findings

1. **`M76-7` in the lesson draft cites the receipt's lines off by one.** It reads
   `base-battery.txt:3-7` and `:9-11`; `cat -n` on the 36-line receipt puts the blocks at `:2-6` and
   `:7-11` (`:7` is the second `==` header, `:8` its first JSON line). My Q75 row uses the verified
   numbers; messaged to `SC01Lesson76` for the fix.
2. **`Q74` is not in the tree at the r77 base.** `corpus/QUALITY.md` ends at Q73 at `2f675548`; the r76
   `B08-q74-quality-row.diff` is unlanded. Any record that cites Q74 (the B08 notes, the r76 lesson draft's
   fix cell) is citing a promise. My deliverable says so explicitly and does not claim Q74 landed.
3. **The pipeline-exit class is a repeat, not an instance — and the repair already exists without the
   rule.** r54 recorded the same shape (`check_description_thresholds.py … | tail -3; echo exit=$?` → 0,
   `W2CriticLesson.md:87`), r76 repeated it in a battery receipt; the L1 then withdrew that capture in
   `plans/round-76-addendum-2.md:7` and a corrected receipt (`.ufo/waves/round-76/base-battery/base-gate-correction.txt:139,270`,
   `exit=1` each) is committed. No lesson and no QUALITY row carried the class until the r76 lesson draft
   added M76-7 — which is why Q75 is a class row rather than a receipt cleanup.
4. **CD1 is also a repeat.** Both commits that added `kotoba-shokukin/` paths are named "recover/preserve
   … report" (`ac9f295`, `6ce2724`), which is what makes "check the path a recovery commit adds" a rule
   rather than a one-off cleanup.
5. **Q76 binds this round's own plan.** `plans/round-77.md:44` promises `corpus/lessons/round-76.md` and
   `:52` promises the wave; the plan's own landing order (lesson before QUALITY) is what keeps my rows'
   citations live.

## Touched surfaces

- Written: `.ufo/waves/round-77/build/SC03QualityRows.quality-rows.md` (rows + candidate table + checks +
  preconditions + limits), `.ufo/waves/round-77/w1/SC03QualityRows.md` (this report).
- Not touched: `corpus/QUALITY.md`, any lesson, `SKILL.md`, `MANIFEST.json`, `scripts/`, `.ufo/state/`,
  `considerthese/`, the lane git index/JJ state. No git or jj write anywhere; the scratch clone was
  read-only.
- Tooling: none installed or upgraded (no pacman, no uv/npm). Python `yaml` 6.0.3 was already present.
- Scratch: `/fast/scratch/hyaku/kotoba-r77/SC03QualityRows/` removed before yielding (verified empty).

## Out of scope / not done

- Counter runs, C1/C2 measurement, lesson/LOG/SCORECARD text, `SKILL.md` edits, SOURCES rows — other
  seats and the L1.
- I did not adjudicate `M76-1`'s class label; the row cites the lesson draft's `number-drift` (the
  reviewer `R05RevLessonDrafts.findings.md:9` calls the other label non-vocabulary) and the committed bytes.
- CD3/CD4 were not drafted as rows (see deliverable § Limits) — outside this seat's candidate list, and I
  do not claim existing rows cover them.

VERDICT: Four QUALITY rows drafted (Q74 measured-field convention, Q75 gate's own exit status, Q76 promised-lesson landing, Q77 recovery-commit path), each with a real falsifier and a lesson anchor verified at line; one candidate rejected as duplicate of Q74; the r76 lesson's M76-7 line refs are off by one and were routed; nothing applied to the lane.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/SC03QualityRows.quality-rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/SC03QualityRows.md
