# B08LessonDrafts — R1 correction, Q74 criterion, M76-1 row (drafts)

VERDICT: three drafts delivered under `.ufo/waves/round-76/build/`, applied to zero lane files; every number in
them re-derived from committed bytes at `b7f13f4b` and at three further revisions, and at the tip `eab64394`
(`SKILL.md` unchanged between the last measured rev and the tip; render `1022 1021` at the tip); both patch
fragments dry-run exit 0 against base bytes and against tip bytes; the frozen counter
`verifiers/check_r75_routed_repairs.py` does not exist at either revision (`git cat-file -e` exit 128 on both), so no
counter verdict is claimed.

Report: `.ufo/waves/round-76/w1/B08LessonDrafts.md`

## Axes

| axis | what this seat moves |
|---|---|
| consistency | the r75 lesson's false row and Gate reject get an appended correction that names exactly what it supersedes; the r75 plan's repeat of the same premise is named too, so R1's re-derivation is discharged with a pointer instead of a promise |
| calibration | the number is stated with its convention (clip 1,022 / stripped 1,021) and with the slice that produces each, so the off-by-one cannot re-enter as ambiguity |
| depth | Q74 is a criterion, not a prose caution: surface (rendered value), unit (characters, clip named), boundary rule, and the arithmetic that makes 392 ≠ 1,022 |
| operability | the correction carries the three commands that reproduce its numbers; the M76-1 fragment carries the anchor lines for both table shapes the lane uses |
| coverage | measured at four revisions (65a5c7a, ac9f295, b7f13f4b, 4de12b61) and checked at the current tip for file drift |
| freshness | base→tip diff on both target files is empty at run time, so the fragments apply to the bytes the L1 will land on |
| adjacency | cross-checked against `.ufo/waves/round-76/w1/B21RevMethod.md` (independent measurement) — numbers agree; only the class label differs, disclosed below |

## 1. Artefacts (none applied; the L1 integrates)

| file | size | sha256 |
|---|---|---|
| `.ufo/waves/round-76/build/B08-r1-round-75-correction.diff` | 6,519 B | `94ae0d6832e19aed374e0c3015390e0508dca72062cd879cdaf770a8b10f4279` |
| `.ufo/waves/round-76/build/B08-q74-quality-row.diff` | 2,821 B | `6cbe0e14dacef4589be5ee97d6c20ac108b8b633da6748b023e4abda834c3044` |
| `.ufo/waves/round-76/build/B08-m76-1-round-76-row.md` | 4,453 B | `6e55b5d2a55a9b644bd1267d7c071ac5cfbc85f2a901231e7c141da936908bf8` |
| `.ufo/waves/round-76/build/B08-notes.md` | 6,111 B | `9e75f8f2131c9e6daacb03ce1becf22f583a6fea6acfc3ff6f02990325694d73` |
| `.ufo/waves/round-76/build/B08-verify.txt` | 205 lines | `0d87f87ed3fa2a0b4792c5fa96626a076507a39cb0083792a18f1bf12473454a` |

Each diff is one hunk with the file's last three lines as context (`@@ -10,3 +10,25 @@`; `@@ -87,3 +87,4 @@`);
`grep '^-[^-]'` over either diff returns nothing (exit 1), so both are append-only. The transcript
`.ufo/waves/round-76/build/B08-verify.txt` holds every command with its exit code, including the dry-runs against base and tip bytes.

## 2. R1 — appended correction for `corpus/lessons/round-75.md`

Appended section `## Correction (appended, round 76 — R1 of the round-75 verifier spot-check)`, 12 → 34 lines.
It names, verbatim, both superseded texts:

- the M75-1 row (`corpus/lessons/round-75.md:11`), quoted in full in a 4-space indented block so it cannot
  re-enter the `## Mistakes` table, and
- the Gate reject sentence (`:5`): "any claim that the 1021-character description size reported in
  `considerthese/2026-10-26.md` remains current; current frontmatter is materially shorter".

and asserts the measurement:

- rendered `description` = **1,022 characters** (clip) / **1,021** stripped, **first sentence 151**;
- block geometry `description: >` line 3, content lines **4–18** (15), closing `---` line 19;
- arithmetic: 1,037 raw over lines 4–18 − 30 indent + 14 join spaces = 1,021 folded, + clip newline = 1,022;
- the r75 window `NR>=3&&NR<=8` sums to 392 over 6 of the block's 16 source lines;
- the slice rule (`split('---')[1]` keeps the newline → 1,022; slicing at the closing `\n---` → 1,021);
- the convention frozen by `plans/round-76-addendum-1.md` (committed `7eed80e9`): clip 1,022 / stripped 1,021,
  both printed by every receipt;
- authority `corpus/lessons/round-75-verifier-spotcheck.md` § 6 R1, with § 4 `:63` and § 5 `:72`.

It also withdraws the `stale-premise` classification, and states what R1's "re-derive" owes: the same premise is
written into `plans/round-75.md:15` ("the stale 1,021-char assertion in `considerthese/2026-10-26.md` is not the
current base"), while **no r75 claim consumed it** — r75's C1 is the equality-threshold claim on `SKILL.md:193`.

Measured (transcript §2, §3, §7, §8):

```
$ git show b7f13f4:SKILL.md | python3 -c "import sys,yaml;d=yaml.safe_load(sys.stdin.read().split('---')[1])['description'];print(len(d),len(d.strip()))"
1022 1021                                                                    # exit 0
$ git show b7f13f4:SKILL.md | awk 'NR>=4&&NR<=18{s+=length($0)} END{print s}'   # 1037, exit 0
$ git show b7f13f4:SKILL.md | awk 'NR>=3&&NR<=8{printf "%d:%d ",NR,length($0)}'  # 3:14 4:76 5:78 6:73 7:79 8:72, exit 0
```

Same `1022 1021` at `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `ac9f29510d3914a6edb97c8dbdb3445cab9141de`,
`4de12b61f75c73e3675ef0e422cc2be0f7da8960`.

Red before → green after (transcript §4–§5), on a copy of the committed bytes:

| string | base copy | after patch |
|---|---|---|
| `1,022 characters` | 0 (exit 1) | 1 (exit 0) |
| `lines 4–18` | 0 (exit 1) | 2 (exit 0) |
| `M75-1` | 0 (exit 1) | 1 (exit 0) |
| `Q74` | 0 (exit 1) | 1 (exit 0) |
| `r1-folded-render.txt` | 0 (exit 1) | 1 (exit 0) |
| `7eed80e9` | 0 (exit 1) | 1 (exit 0) |
| `clip 1,022 / stripped 1,021` | 0 (exit 1) | 1 (exit 0) |

The two superseded strings read `1` in the base copy because that is where they must be named from.

## 3. Q74 — criterion row for `corpus/QUALITY.md`

Appended after Q73, 89 → 90 lines, `supersedes` `—` (supersedes none, as the seat brief requires). Criterion:
a YAML block scalar is measured by its render over the whole block at a named revision, never on a line window;
the number names the parser (`yaml.safe_load`), the slice (block's trailing newline kept) and the convention
(clip 1,022 / stripped 1,021); a raw-line sum is not the scalar's value because `length($0)` counts the two-space
indent and the `description: >` marker (the r75 window sums to 392 for a block that renders 1,022). Grounded in
M76-1, carrying `corpus/lessons/round-75.md:11` and `corpus/lessons/round-75-verifier-spotcheck.md` § 4 `:63`, § 6 R1 `:77`.

## 4. M76-1 — mistakes-table row for the round-76 lesson

`class` = `block scalar measured by a line window`; `evidence` = the M75-1 row's own bytes, the window/block sums,
`plans/round-75.md:15`, and the spot-check § 4 `:63` / § 6 R1 `:77`; `captured-by` = Q67/Q54/Q60 required a
reproducible count at a revision but none required the measurement's unit to match the artefact's parse unit — the
r75 closure caught it, the round did not; `fix` = Q74, the R1 correction, and the frozen clip/stripped convention.
Both table shapes are drafted (5-column `id` table as `corpus/lessons/round-73.md:74` and `round-74.md:85`, or the
4-column table `round-75.md:9` used) with an explicit anchor for each; exactly one is to be inserted.

## 5. Findings (evidence attached, dispositions named)

- **F1 — the premise is in the plan, not only the lesson.** `plans/round-75.md:15` reads "current description
  frontmatter lines 4–8 lengths are 76,78,73,79,72 (the stale 1,021-char assertion in `considerthese/2026-10-26.md`
  is not the current base)". R1's "re-derive any plan/claim that consumed" therefore has a target; the correction
  names it and records that no r75 *claim* consumed it. Disposition: named in the R1 correction; the plan is filed
  and is not rewritten (append-only discipline).
- **F2 — the class label is the error, not the premise.** `stale-premise` described a conclusion drawn from a
  window measurement; the premise was current. Disposition: the correction withdraws the classification; M76-1's
  class is the measurement defect.
- **F3 — the row is self-contradictory in one cell.** `corpus/lessons/round-75.md:11` cites "lines 3–18" and then
  measures `NR>=3&&NR<=8`. That is the cheapest tell and is quoted in both the correction and the M76-1 evidence.
- **F4 — the off-by-one is now frozen, not tolerated.** `plans/round-76-addendum-1.md` (committed `7eed80e9`)
  fixes clip = 1,022 and requires both variants in every receipt. The correction and Q74 name the convention; the
  receipt `.ufo/waves/round-76/receipts/r1-folded-render.txt` is another seat's; it is absent at the tip this seat
  measured and its contents are not asserted.
- **F5 — class-label divergence with a sibling, disclosed.** `.ufo/waves/round-76/w1/B21RevMethod.md` §7 proposes
  `layout-window-counted-as-value`; this seat's row says "block scalar measured by a line window". The evidence,
  captured-by and fix cells agree; the label choice belongs to the lesson owner (`B17LessonScribe`) and the L1.
  Sent to B17 with both options.
- **F6 — no counter, no verdict.** `verifiers/check_r75_routed_repairs.py` is absent at `b7f13f4` and at
  `eab6439` (absent from the tree at both; no tree entry, so no manifest row can hide it); the name occurs only in
  the plan, the addendum, the round-76 wave spec and dispatch, and seat reports. Nothing here is scored against it;
  the fragments are written to the plan's R1 sentence plus the addendum's convention.

## 6. Pointer hygiene (Q68/Q60, measured)

```
$ python3 -B verifiers/check_report_pointers.py --report .ufo/waves/round-76/w1/B08LessonDrafts.md \
    --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev eab64394dba08a47f6797a2e23719be14675b44b --round 76
report pointers resolved 22 of 40; unresolved 18 (11 distinct tokens)
```

Every remaining unresolved pointer is a planned output that does not exist at the measured rev: this report, the five
`B08-*` drafts under `.ufo/waves/round-76/build/`, the sibling report `.ufo/waves/round-76/w1/B21RevMethod.md` and
the counter `verifiers/check_r75_routed_repairs.py` (all absent or untracked at `eab6439` — F6), and the receipt
`.ufo/waves/round-76/receipts/r1-folded-render.txt` (another seat's, absent). The count moves with the report's own
text, since the command block above is itself parsed; the last run is the one quoted. No committed lane file is cited
without resolving: `corpus/lessons/round-75.md`, `corpus/QUALITY.md`, `plans/round-75.md`,
`corpus/lessons/round-75-verifier-spotcheck.md` and `SKILL.md` all resolve at `b7f13f4`, and the conventions
document resolves at its committing rev `7eed80e9` (`git cat-file -e 7eed80e9:plans/round-76-addendum-1.md`,
exit 0).

## 7. Limits

- Nothing applied, committed, staged or pushed; no `git`/`jj` write. The lane `git status --porcelain` at run time
  showed five untracked `.ufo/waves/round-76/**` entries only (siblings' work), no modified tracked file.
- The round-76 lesson body is `B17LessonScribe`'s; this seat supplies the M76-1 and Q74 text and the R1 diff only.
- Scratch (`/fast/scratch/hyaku/kotoba-r76/B08LessonDrafts/`) removed before yielding; nothing under `/tmp` is
  cited. No tool was installed.
