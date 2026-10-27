# M76-1 — mistake-row draft (round-76 lesson `## Mistakes`)

Seat `B08LessonDrafts` (scribe). **Draft only: not applied to any lane file**; the L1 integrates.
Source of truth for the id: `plans/round-76.md` § Frontier step — "Mistakes: M76-1 (folded-scalar block measured as
frontmatter lines) → Q74".

## Row, 5-column shape (header as `corpus/lessons/round-73.md:74` and `corpus/lessons/round-74.md:85`)

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M76-1 | block scalar measured by a line window | `corpus/lessons/round-75.md:11` (M75-1) calls the frontmatter "substantially shorter" from `awk 'NR>=3&&NR<=8{print NR ":" length($0) ":" $0}'` → `14,76,78,73,79,72` (sum 392), while the same row cites lines 3–18 and the block renders 1,022 characters (1,021 stripped) at `65a5c7a`, `ac9f295` and `b7f13f4b`; `plans/round-75.md:15` repeats the premise ("the stale 1,021-char assertion in `considerthese/2026-10-26.md` is not the current base") | Q67/Q54/Q60 require a reproducible count at a revision but none requires the measurement unit to match the artefact's parse unit — the r75 closure caught it (`corpus/lessons/round-75-verifier-spotcheck.md` § 4 `:63`, § 6 R1 `:77`), the round did not | Q74 (whole-block rendered measure naming parser, slice and clip newline); the r76 R1 correction in `corpus/lessons/round-75.md` restates 1,022 (clip) and withdraws the stale-premise row and the Gate reject; the clip/stripped convention is frozen in `plans/round-76-addendum-1.md` (`7eed80e9`) and every receipt prints both variants |

## Row, 4-column shape (header as `corpus/lessons/round-75.md:9`, if the round-76 lesson keeps that shape)

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| block scalar measured by a line window | `corpus/lessons/round-75.md:11` (M75-1) calls the frontmatter "substantially shorter" from `awk 'NR>=3&&NR<=8{print NR ":" length($0) ":" $0}'` → `14,76,78,73,79,72` (sum 392), while the same row cites lines 3–18 and the block renders 1,022 characters (1,021 stripped) at `65a5c7a`, `ac9f295` and `b7f13f4b`; `plans/round-75.md:15` repeats the premise ("the stale 1,021-char assertion in `considerthese/2026-10-26.md` is not the current base") | Q67/Q54/Q60 require a reproducible count at a revision but none requires the measurement unit to match the artefact's parse unit — the r75 closure caught it (`corpus/lessons/round-75-verifier-spotcheck.md` § 4 `:63`, § 6 R1 `:77`), the round did not | Q74 (whole-block rendered measure naming parser, slice and clip newline); the r76 R1 correction in `corpus/lessons/round-75.md` restates 1,022 (clip) and withdraws the stale-premise row and the Gate reject; the clip/stripped convention is frozen in `plans/round-76-addendum-1.md` (`7eed80e9`) and every receipt prints both variants |

## Anchor

- 5-column table: insert as the **first data row**, immediately after the `|---|---|---|---|---|` separator line.
- 4-column table: insert as the **first data row**, immediately after the `|---|---|---|---|` separator line.
- One shape only; never both rows.

## Numbers in the row, reproduced at `b7f13f4b39cbd43076a85568adca763a6f674e7a`

```
git show b7f13f4:SKILL.md | awk 'NR>=3&&NR<=8{printf "%d:%d ",NR,length($0)}'
→ 3:14 4:76 5:78 6:73 7:79 8:72      (sum 392 — the row's "14,76,78,73,79,72")
git show b7f13f4:SKILL.md | awk 'NR>=4&&NR<=18{s+=length($0)} END{print s}'
→ 1037                               (raw content block: 15 lines, indent included)
git show b7f13f4:SKILL.md | python3 -c "import sys,yaml;d=yaml.safe_load(sys.stdin.read().split('---')[1])['description'];print(len(d),len(d.strip()))"
→ 1022 1021                          (folded render incl. clip newline; stripped)
```

The slice keeps the block's trailing newline (`split('---')[1]`); slicing at the closing newline before `---` reads
1,021. The convention (clip 1,022 / stripped 1,021, both printed by every receipt) is frozen in
`plans/round-76-addendum-1.md` § "Render-length convention", committed `7eed80e9`. First sentence: 151 characters. The description is identical at
`65a5c7a663249e0522cc49e4a148424200d9ddfe`, `ac9f29510d3914a6edb97c8dbdb3445cab9141de` and
`4de12b61f75c73e3675ef0e422cc2be0f7da8960`.

## Disposition

Q74 (`corpus/QUALITY.md`) is the guard this row is graded by; it is drafted in `B08-q74-quality-row.diff` beside this
file. The row's `fix` cell names that criterion, not a prose promise.
