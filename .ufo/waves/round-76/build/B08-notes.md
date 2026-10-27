# B08LessonDrafts — integration sheet (drafts only, nothing applied)

Seat: `B08LessonDrafts` (scribe, leaf). Wave `round-76/w1`. Base `b7f13f4b39cbd43076a85568adca763a6f674e7a`;
tip while drafting `eab64394dba08a47f6797a2e23719be14675b44b`. Both target files are **identical base→tip**
(`git diff --stat b7f13f4 eab6439 -- corpus/lessons/round-75.md corpus/QUALITY.md` empty, exit 0).

Nothing is applied to a lane file by this seat. Verification transcript beside this file:
`B08-verify.txt` — every command below ran there with its exit code.

## Artefacts

| file | what | sha256 |
|---|---|---|
| `B08-r1-round-75-correction.diff` | appends `## Correction (appended, round 76 — R1 …)` to `corpus/lessons/round-75.md` (12 → 34 lines) | `94ae0d6832e19aed374e0c3015390e0508dca72062cd879cdaf770a8b10f4279` |
| `B08-q74-quality-row.diff` | appends the `Q74` row to `corpus/QUALITY.md` (89 → 90 lines) | `6cbe0e14dacef4589be5ee97d6c20ac108b8b633da6748b023e4abda834c3044` |
| `B08-m76-1-round-76-row.md` | the `M76-1` row in both table shapes, anchors, and every command behind its numbers | `6e55b5d2a55a9b644bd1267d7c071ac5cfbc85f2a901231e7c141da936908bf8` |

Each diff is a single hunk (`@@ -10,3 +10,25 @@` for r1, `@@ -87,3 +87,4 @@` for Q74) whose three context lines
are the file's last three lines; `grep '^-[^-]'` over either diff returns nothing (exit 1), so both are
append-only. Both dry-run clean against the base bytes and against the tip's bytes (transcript §3, §3b).

## What the correction asserts (pinned to bytes)

- Rendered `description` at `b7f13f4` = **1,022 characters** clip / **1,021** stripped; first sentence **151**.
  `git show b7f13f4:SKILL.md | python3 -c "import sys,yaml;d=yaml.safe_load(sys.stdin.read().split('---')[1])['description'];print(len(d),len(d.strip()))"` → `1022 1021`.
- Block geometry: `description: >` on line 3, content lines **4–18** (15), closing `---` on line 19.
- Whole content block raw = 1,037 (indent counted); the r75 window `NR>=3&&NR<=8` = `14,76,78,73,79,72` (sum 392);
  folding arithmetic 1,037 − 30 indent + 14 join spaces = 1,021, + clip newline = 1,022.
- Convention named in the text and frozen: `plans/round-76-addendum-1.md` § "Render-length convention"
  (committed `7eed80e9`, `git cat-file -e 7eed80e9:plans/round-76-addendum-1.md` exit 0) — clip 1,022 /
  stripped 1,021, both printed by every receipt.
- Superseded text named and quoted verbatim (Gate `:5` and the M75-1 row `:11`, the row in a 4-space indented
  block so it does not re-enter the `## Mistakes` table). The row's `stale-premise` classification is withdrawn.
- Re-derivation owed by R1 is discharged with a pointer: `plans/round-75.md:15` repeats the premise ("the stale
  1,021-char assertion … is not the current base"); **no r75 claim consumed it** (r75 C1 is the equality-threshold
  claim on `SKILL.md:193`).
- Authority cited: `corpus/lessons/round-75-verifier-spotcheck.md` § 6 R1, plus § 4 `:63` and § 5 `:72`.
- Same description `1022 1021` at `65a5c7a`, `ac9f295`, `b7f13f4b`, `4de12b61`.

Red-before → green-after (transcript §4–§5): `1,022 characters`, `lines 4–18`, `M75-1`, `Q74`,
`r1-folded-render.txt`, `7eed80e9`, `clip 1,022 / stripped 1,021` each read `0` (exit 1) in the base copies and
`1` (exit 0) after the patch; the two superseded strings read `1` in base because they exist to be named there.

## Q74 row

Appended after Q73, `supersedes` = `—`. A YAML block scalar is measured by its render over the whole block at a
named revision; the number names the parser (`yaml.safe_load`), the slice (block's trailing newline kept) and the
convention (clip 1,022 / stripped 1,021); a raw-line sum is not the scalar's value because `length($0)` counts the
two-space indent and the `description: >` marker. Grounded in M76-1, carrying the r75 window sum 392 against the
render 1,022.

## M76-1 row

`class` = "block scalar measured by a line window". Evidence: the M75-1 row's own bytes (`:11`), the window/block
sums, `plans/round-75.md:15`, spot-check § 4 `:63` / § 6 R1 `:77`. `captured-by` records that Q67/Q54/Q60 required a
reproducible count at a revision but none required the measurement's unit to match the artefact's parse unit, and
that the r75 closure caught it, the round did not. `fix` names Q74, the R1 correction and the frozen convention.
Two shapes are drafted; **the L1 inserts exactly one** (5-column `id` table as rounds 73/74, or the 4-column table
round 75 used).

## Cross-checks against sibling work (read-only)

- `B21RevMethod.md` §1–§4: same numbers independently (1,022 clip / 1,021 stripped / 392 window / 151 first
  sentence, four revisions, three renderers, reflow falsification). Its §7 proposes the class label
  `layout-window-counted-as-value` where this draft says "block scalar measured by a line window"; the label is a
  judgement call for the lesson owner (B17) and the L1 — the cell contents agree, only the wording differs.
- `B21RevMethod.md` §5 D-a…D-e match this draft's claims; D-e is the off-by-one this draft now names via
  `7eed80e9`.

## Dependencies and limits (not evidence this seat holds)

- `.ufo/waves/round-76/receipts/r1-folded-render.txt` is another seat's; the correction states what the
  addendum *requires* of it (recompute from the measured revision, print both variants, name the convention)
  and does not claim the receipt's current contents — it does not exist at the tip this seat measured.
  If that receipt prints only one variant, the correction and the addendum disagree — flagged, not resolved here.
- `verifiers/check_r75_routed_repairs.py` does not exist at base (`ls` 2×, exit 2); the correction is written to the
  plan's R1 sentence and the addendum's convention. **No counter run is claimed.**
- The round-76 lesson body belongs to `B17LessonScribe`; this seat supplies the M76-1 and Q74 text only.
- Nothing applied, committed, staged or pushed; no `git`/`jj` write of any kind. Scratch under
  `/fast/scratch/hyaku/kotoba-r76/B08LessonDrafts/` was removed before yielding.
- No tool was installed for this seat.
