# D3 — forward pointer from the round-49 census to its round-74 re-pin (DRAFT, not applied)

Seat `B10RepairD2D3`, round 76. Routed defect: `corpus/lessons/round-74-verifier-spotcheck.md` § Routed defects item 3
— "The round-49 census entry `corpus/knowledge/sibling-overlap-census-round49.md` carries no forward pointer to its
round-74 re-pin (the README index row and `PROVINCE.md` do); append one so a reader of the old entry meets the
corrected tsukuroi class."

Verified before drafting: `grep -c 'round-74\|round74\|Round 74' corpus/knowledge/sibling-overlap-census-round49.md`
→ **0** (exit 1) at `4de12b6`; the re-pin exists and is tracked
(`git ls-files corpus/knowledge/sibling-overlap-census-round74.md` → the path, 23,405 B), `verified-at: 2026-10-25`,
and its § "One class changes: tsukuroi `none` → `adjacent` (basis kotoba)" plus its counts line "10 adjacent, 10 none,
0 contested … round 49 had 9 adjacent and 11 none" are the facts the pointer restates.

## Placement rule (hard)

The round-74 entry cites this file **by line range**: "the classification rule (`:43-64`), its round-50 precedence
section (`:246-295`) and the round-51 status of that rule (`:416-458`)". At `4de12b6` those lines are exactly
`## Classification rule` (:43), `## Round 50: precedence between contested and a stated split (routed defect D3)`
(:246) and `## Round 51 status of the precedence rule (routed D6)` (:416); the file ends at :466. The pointer is
therefore a **tail append after line 466** — never an insertion, never a frontmatter edit, so no line above moves and
no line range in either entry changes meaning.

## Text to append (verbatim; patch `B10RepairD2D3.formA.patch` / `.formB.patch`, same hunk)

```markdown

## Round 74 forward pointer (append-only, routed D3)

The rows above are the round-49 pin and are not edited. The census was re-pinned, method unchanged, at the same 20
sibling lanes read at heads frozen before any wave-1 seat ran, in
`corpus/knowledge/sibling-overlap-census-round74.md` (round 74, `verified-at: 2026-10-25`). That entry applies this
entry's classification rule (`:43-64`), its round-50 precedence section (`:246-295`) and the round-51 status of that
rule (`:416-458`) unchanged, recomputes all nine cells per lane, and records one class change: tsukuroi `none` →
`adjacent`, basis kotoba. Counts at round 74: 10 adjacent, 10 none, 0 contested (round 49: 9 adjacent, 11 none).
Read the round-74 entry for current classes; nothing above this section moves, so the line ranges cited here and in
the round-74 entry stay valid. Status at `4de12b6` (2026-10-27): this entry's own `recheck` command prints `rows 20
verified 20` but exits 1 on the `## Adjacent` cross-check — 15 lane commits have moved since 2026-10-22 and tsukuroi
reads `adjacent` in `PROVINCE.md`, not `none`, for 16 `FAIL` lines — while the round-74 entry's same command prints
`rows 20 verified 20` and `province rows 20 matched 20`, exit 0. The rows here stay the round-49 pin; the round-74
entry is the live reading.
```

The last sentence group is the freshness half: the entry's frontmatter `recheck:` is left **byte-identical** (the file
is append-only), so the pointer — not an edited claim — carries the news that the round-49 recheck is now red on the
`## Adjacent` cross-check. Measured on 2026-10-27 (below); remove those three lines if the integrator prefers the
pointer to state only the re-pin.

## Measured effect (scratch clone, `4de12b6` base vs the appended file)

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md
  base   : 16 FAIL lines, "rows 20 verified 20", "province rows 20 matched 4", exit 1
  appended: 16 FAIL lines, "rows 20 verified 20", "province rows 20 matched 4", exit 1
  diff of the FAIL sets: empty (identical line-for-line)
```

The 16 lines are 15 `commit … does not match the census` plus 1 `tsukuroi classification 'adjacent' does not match the
census 'none'` — all pre-existing at the base (the round-49 pins predate the lanes' current heads and the tsukuroi
reclassification the round-74 entry records). The append adds **no** row, **no** table line and **no** class word in
table form, so the row parser's counts are unchanged: `rows 20 verified 20` before and after.

```
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md
  rows 20 verified 20 / province rows 20 matched 20 / exit 0   (base, Form A, Form B — unchanged)
```

Other gates on the same three states (`4de12b6`, `fe3ef00` Form A, `47a2f92` Form B): `verify_skill_checklist.py
--json` exit 0 / 11 pass in all three (`trigger.citation_resolves` 205, `governance.citation_resolves` 1302 with the
fragment vs 1301 at base, all resolving); `verify_corpus_integrity.py --json` and `verify_corpus_independent.py
--json` exit 1 in all three with the same four pre-existing DRIFTs (`tracked_files 145 vs 144`, `unindexed 1 vs 0`,
`report_total 101 vs 99`, `commit_total 44 vs 43`); `check_r67_routed_repairs.py` 3 of 4, `check_r69_routed_repairs.py`
9 of 10, `check_r69_routed_repairs_v2.py` 8 of 10 in all three.

## Landing instructions

1. `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin apply --check .ufo/waves/round-76/build/B10RepairD2D3.formA.patch`
   (or `.formB.patch`); the census hunk is identical in both and applies cleanly to `4de12b6`.
2. Append only — apply the patch, do not hand-splice a section into the middle of the file; the round-74 entry's
   `:43-64`, `:246-295`, `:416-458` citations must keep pointing at the classification rule, the round-50 precedence
   section and the round-51 status section.
3. Re-run the two census commands above and `verify_skill_checklist.py --json`; expect the numbers in the tables.
4. The frontmatter (`source:`, `verified-at: 2026-10-22`, `recheck:`) is deliberately untouched; if the lane wants a
   fresh `verified-at`, that is a separate decision (an in-place edit to an append-only entry) and not part of D3.
