# X01Simplifier — seat report (kotoba round 77, w1)

Scoped: cut the round-76 C1 draft row and entry without losing a quote, a pointer or a conjunct the
frozen C1 counter reads; prove it in a scratch clone; list duplicate homes. Nothing in the lane was
edited; the deliverable is a draft for the L1 in `.ufo/waves/round-77/build/`.

## Cuts (before → after)

| artifact | draft | cut | delta |
|---|---|---|---|
| entry `corpus/knowledge/description-craft-round76.md` | 10,975 chars / 99 lines | 9,407 chars / 95 lines | −1,568 (−14.3 %), −4 lines |
| § Body craft rule row | 447 chars / 65 words | 395 chars / 56 words | −52 (−11.6 %) |
| `check_desc_craft.py` registry row | 1,156 chars | 822 chars | −334 |
| `check_r75_routed_repairs.py` registry row | 922 chars | 760 chars | −162 |
| SKILL.md patch total | 2,525 chars | 1,977 chars | −548 (−21.7 %), 3 lines → 3 |

Entry sections: frontmatter −71, title+intro+rule table −462, measured −400, Q62 −117, Limits −203,
Related −315. Full per-section table and the exact cut strings are in
`build/X01Simplifier.md`; the landable entry is `build/X01Simplifier.entry.md`.

Cut, in one line each: the rule table's five-times-repeated `page` column and full-path location cells
(one page, named once, `:25` shorthand); the measure table's duplicate "how measured" column (convention
stated once, both numbers kept); the restated `frontmatter-trigger-surface` rule text (pointer
`:153`–`:154` kept); the `skill-listing-thresholds-round54` explanation (pointer kept, range corrected);
the eval-protocol restatement (one sentence + pointers); the Related-bullet document summaries;
`ground:` to its two checkable facts. In the rule row: `, and err pushy` and `, including ones the user
never names`, both stated verbatim by fragments already in that row. In the registry rows: the
exhaustive conjunct restatement that is the counter docstrings' subject.

## Proof (scratch clone, `6523aced` base, frozen counter sha256 `cf3c45d9…`)

Own exit status captured per run (no pipeline):

| world | C1 | own exit |
|---|---|---|
| D-A `66e7499` drafts, lesson as filed | `description craft backed 5 of 6` | 1 |
| X-A `ff185a2` cuts, lesson as filed | `description craft backed 5 of 6` | 1 |
| D-B `7727393` drafts, lesson Gate quote fixed | `description craft backed 6 of 6` | 0 |
| X-B `7202829` cuts + cut registry rows, same fix | `description craft backed 6 of 6` | 0 |

Same conjuncts, arm by arm: (b) 11 located quotes in both **and the same set**; (c) 1 row + 3 fragments
in both; (d) 1022/1021/151 in both; (e)/(f) pass in both; (a) is lesson-dependent (below). The draft↔cut
diff is `SKILL.md` and the entry only. `check_gate_registry.py --rev X-B` → `62 of 62`, phantom 0, own
exit 0 (base: `60 of 62`, own exit 1). `SKILL.md` 593 lines with the three rows; anchors re-measured on
the r77 base (`## Gate registry` 445→446, `## Sources` 514→517, budget box 285→286).

Quote check independent of the counter: each of the five entry quotes and three row fragments occurs
exactly once in `snapshots/optimizing-descriptions.md`, zero times in `evaluating-skills.md` and
`best-practices.md`. Audit numbers re-derived at base: render 1022 clip / 1021 stripped, first sentence
151, 8 quoted trigger phrases / 108 chars / 7 sentences.

## Duplicate homes (one authoritative home per fact)

1. Files outside the omp discovery root never route; `description` craft there is audit-hygiene —
   `corpus/knowledge/frontmatter-trigger-surface.md:150`–`:155` (§12, sentence at `:153`–`:154`).
   The draft restated the rule in Findings bullet 2 and explained §11/§12 in Related; the cut keeps the
   example quote and the pointer, drops the restatement.
2. Authoring maximum ≠ render cut; 1,024 is the spec's ceiling, not a client cut; which client cuts or
   budgets at what number — `corpus/knowledge/skill-listing-thresholds-round54.md:15`–`:21`.
   The draft restated the distinction and cited `:15`–`:16` (Finding 1 only); the cut keeps one clause
   plus the pointer, corrected to `:15`–`:21`.
3. The omp first-sentence render path outside a discovery root — `render-mechanism-round7.md` and
   `frontmatter-trigger-surface.md` §9/§12; the draft's Related trailing clause restated it; pointer kept.
4. The trigger-rate protocol recorded, not admitted — the round-76 lesson's `Reject (held)`; Q62 now
   points instead of restating.
5. The 1021/1022 render convention — frozen in `plans/round-76-addendum-1.md` and printed beside the
   number; stated once in the cut, no duplicate column.

## Input defects found (must be handled by the L1; I did not edit the lane)

1. **The round-76 lesson draft fails C1 (a) as filed.** Its Gate quote is
   `"`A few sentences to a short paragraph is usually right`"`: the backticks sit inside the double
   quotes, `quote_spans()` yields a backtick-bearing span that is not a substring of the page, and the
   counter prints `(a) the lesson Gate carries no <=25-word quote located in the
   optimizing-descriptions snapshot` → `5 of 6`, exit 1. Minimal repair: move the backticks outside the
   quotes. With that one edit the same drafts score `6 of 6`, exit 0 — so the block is the lesson's, not
   this cut's. (The draft is not confidence-worthy here: it asserts a "located quote" that the frozen
   counter cannot locate.)
2. **The patch draft's anchor list is stale in one place:** "`## Gate registry` stays line 448" —
   measured 445 base / 446 patched on `6523aced`. Its other anchors hold.
3. **The entry draft's `skill-listing-thresholds-round54.md:15`–`:16`** covers only Finding 1 while the
   sentence also carries Finding 2's content; corrected in the cut to `:15`–`:21`.

## Deliberate non-cuts / tradeoff

Rule rows, their quotes and `action` cells stay (each is a distinct page rule and an instruction); the
`recheck:` command stays verbatim (freshness probe); the registry rows stay one line each (the SKILL.md
budget is a line budget; 593 unchanged); Limits and Q62 non-claims stay. Tradeoff: re-adding the `page`
column to the rule table costs ≈130 chars and changes no counter arm, if the L1 prefers row-local page
naming.

## Scope

Wrote only `.ufo/waves/round-77/build/X01Simplifier.*` and this report. No lane/fleet git or jj write, no
counter edit, no install, no `pacman`; scratch clone removed.

VERDICT: cut accepted: entry −1,568 chars (−14.3 %) and SKILL.md patch −548 chars (−21.7 %) with the C1 counter scoring the identical six-conjunct set (same 11 quotes, 3 fragments, 1022/151) at 6 of 6; two input defects found, one (lesson Gate quote wrapped in backticks) blocks (a) as filed and is a one-line repair.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/X01Simplifier.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/X01Simplifier.entry.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/X01Simplifier.skill-patch.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/X01Simplifier.receipt.txt
