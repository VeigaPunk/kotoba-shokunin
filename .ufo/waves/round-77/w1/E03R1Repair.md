# E03R1Repair — final R1 repair for C2 (kotoba round 77, wave w1)

Seat: `E03R1Repair` (executor, leaf). Lane base `6523aced1ee0ebe07dca996213bdc645a6acbd1e`
(r77 freeze; plan base `2f675548eaad2a037a899d39247c1fd7a88aaf48`).
Axes named: **consistency** (C2) and its **calibration** sub-axis — nothing else. This seat earns no
depth and no freshness credit; it touches no file another claim measures, and its no-harm duty is the
parent's battery, not a claim here.

## What was produced

1. **The final appended correction block** for `corpus/lessons/round-75.md` — 24 lines appended after
   the existing 12, byte-compatible with the frozen counter's append-only arm
   (`now.startswith(base_at_b7f13f4)`).
2. **The R1 receipt text** for `.ufo/waves/round-76/receipts/r1-folded-render.txt` (45 lines) — the
   path the frozen counter reads; delivered as a build file for the L1 to land.
3. **One unified patch** carrying both, `git diff` format, new-file entry included, apply-able from the
   lane root.

Deliverables (this wave's build dir):

- `.ufo/waves/round-77/build/E03R1Repair.r1-round-75-correction.patch`
  sha256 `125b0e691f5b6ce9f1de425ec0d5fcfed9a63db7241f3d0d4e6fb9d0ee3b1547`, 83 lines,
  0 removed lines / 50 added.
- `.ufo/waves/round-77/build/E03R1Repair.r1-folded-render.txt`
  sha256 `d9bcb5e1be4b2481131f566d9c4768e5f55a78fee8fbb0070e0bfdfb4c1489db`, 45 lines.
- `.ufo/waves/round-77/build/E03R1Repair.verify.txt` — the transcript behind every line below.

## What the correction asserts (all re-measured, none inherited)

- Superseded text named: M75-1 (`corpus/lessons/round-75.md:11`) and the Gate reject candidate (`:5`),
  both quoted verbatim; the superseded row is reproduced in a 4-space indented block (it cannot
  re-enter the `## Mistakes` table) and compared byte-equal to the base row (793 == 793).
- The description of `SKILL.md` renders **1,022 characters** clip-preserving and **1,021** stripped —
  YAML folded scalar at `description: >` line 3, block content lines **4–18**, closing `---` line 19;
  first sentence 151. Identical clip render (sha256 `3756d530…8861cc`) at `65a5c7a`, `4de12b61`,
  `ac9f295`, `b7f13f4`.
- Folding arithmetic stated so the number reproduces: raw sum over lines 4–18 = 1,037 (indent counted),
  − 30 indent + 14 join spaces = 1,021, + clip newline = 1,022; the r75 window `NR>=3&&NR<=8`
  (`14,76,78,73,79,72`, sum 392) is shown to be a line window, not the scalar's value.
- Convention named and pinned: `plans/round-76-addendum-1.md` (committed `7eed80e9`) — clip 1,022 /
  stripped 1,021, both printed by every receipt.
- Re-derivation discharged: `plans/round-75.md:15` carries the same premise; no r75 claim consumed it
  (r75 C1 is the equality-threshold claim on `SKILL.md:193`, verified) — the plan note and the Gate
  reject are withdrawn, nothing else in round 75 rests on the number.
- Authority: `corpus/lessons/round-75-verifier-spotcheck.md` § 6 R1, with § 4 (`:63`, the DISAGREE row)
  and § 5 (`:72`, quality harmed) cited.

## Verification (scratch clone of lane HEAD; frozen counter, not edited)

Counter bytes match the plan's pin: `sha256 verifiers/check_r75_routed_repairs.py` =
`989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`.

| world | result | exit |
|---|---|---|
| r77 base `2f675548` | `r75 routed repairs closed 0 of 4` (R1–R4 open) | 1 |
| patch applied to a **fresh clone** of lane HEAD, committed `8db8a5c8` | `closed 1 of 4` — **R1 closed, R2/R3/R4 open** | 1 |
| mutant A: receipt without a named revision | R1 open (`names no measured revision`) | 1 |
| mutant B: receipt numbers shifted 1022→1023 / 1021→1020 | R1 open (`does not print 1022`, `… stripped variant 1021`) | 1 |
| C1 counter at the same commit | `description craft backed 0 of 6` (unchanged) | 1 |

Byte-compare of the patched tree against the candidate tree: both files identical. Lane-side
`git apply --check` on the deliverable patch: exit 0.

## Deviations from the B08 draft (one defect fixed, two clarifications)

- **Defect:** B08's last paragraph read "**Rule landed.** `corpus/QUALITY.md` Q74: …". At lane HEAD
  `grep -n Q74 corpus/QUALITY.md` returns nothing (the table ends at Q73). A correction whose purpose
  is to remove a false claim cannot carry a second false claim. Replaced by a "**Rule.**" paragraph
  that states the rule and names Q74 as this round's quality-table repair with its tracked draft
  (`.ufo/waves/round-76/build/B08-q74-quality-row.diff`) — true whether or not the row has landed.
- **Landing provenance:** the heading names round 77 (the round that lands the data); the round-76
  paths exist only because the frozen counter pins them, and the correction says so where it names the
  receipt path.
- **Append-only clarity:** one paragraph states that the superseded row at `:11` and Gate sentence at
  `:5` stay in place and are read together with the correction.

## Landing notes for the L1

1. From the lane root: `git apply .ufo/waves/round-77/build/E03R1Repair.r1-round-75-correction.patch`
   (or the equivalent `jj-lane` commit with the same bytes). The patch adds the 24-line append and the
   new receipt file; it rewrites nothing.
2. The append and the receipt must land in the same commit as far as the counter is concerned — R1's
   two arms read the lesson and the receipt at the measured revision. They are in one patch for that
   reason.
3. If any sibling appends to `corpus/lessons/round-75.md` first, the hunk's trailing context no longer
   matches: re-apply as a plain append of the same 24 lines at end of file (the counter requires
   base-plus-append with `M75-1`/quotes/1022/lines 4–18/spot-check citation inside the appended
   region, not a fixed offset).
4. Expected state after this patch alone: `r75 routed repairs closed 1 of 4`, exit 1.

## Risks

- **R2/R3/R4 are other seats' files.** This repair is independent of them: the receipt measures the
  historical r75 tip `ac9f295`, an ancestor of every later lane commit, so R1 stays closed once the
  lane advances past it.
- **History reachability.** The receipt's closure depends on `ac9f295` remaining reachable in the lane
  history (it is a committed lane tip; `jj-lane` never rewrites landed history).
- **Q74 text.** No dependency: the correction no longer asserts the row exists.
- **Round-76 path naming** is disclosed here and in the correction text (R76-D2 discipline) so a
  reader is not asked to infer that round 76 landed data — it did not.

## Blockers

None. Nothing was blocked, nothing unrun was reported as passing. No tool was installed (no pacman,
no network); scratch under `/fast/scratch/hyaku/kotoba-r77/E03R1Repair/` was removed before yielding.

VERDICT: Final R1 repair verified — patch alone on a fresh lane clone flips `check_r75_routed_repairs.py` R1 to closed (1 of 4, exit 1, R2–R4 untouched) with both render variants, the convention and the block 4–18 named; B08's unlanded-Q74 claim removed.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E03R1Repair.r1-round-75-correction.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E03R1Repair.r1-folded-render.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E03R1Repair.verify.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E03R1Repair.md
