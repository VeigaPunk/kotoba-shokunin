# X01Simplifier — the C1 draft row and entry, cut (kotoba round 77, w1)

Status: **build draft for the L1**, not applied. No lane file outside `.ufo/waves/round-77/` was
written; no counter byte was edited (the clone's `verifiers/check_desc_craft.py` hashes
`cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`, the frozen pin).

Inputs: `.ufo/waves/round-76/build/skill-patch.md` and `.ufo/waves/round-76/build/entry-draft.md`,
both treated as untrusted drafts and re-measured. Base for every clone commit:
`6523aced1ee0ebe07dca996213bdc645a6acbd1e`.

Deliverables:
- `X01Simplifier.entry.md` — the cut entry, landable as `corpus/knowledge/description-craft-round76.md`
  (no build comment to strip).
- `X01Simplifier.skill-patch.md` — the three cut rows with measured anchors for the r77 base.
- `X01Simplifier.receipt.txt` — every command, its **own** exit status, and the size tables.

## 1. Before / after

| artifact | draft | cut | delta |
|---|---|---|---|
| entry `description-craft-round76.md` | 10,975 chars (11,054 B), 99 lines | 9,407 chars (9,467 B), 95 lines | **−1,568 (−14.3 %)**, −4 lines |
| entry rendered body (no frontmatter) | 10,750 chars | 9,182 chars | −1,568 |
| § Body craft rule row | 447 chars, 65 words | 395 chars, 56 words | −52 (−11.6 %), −9 words |
| `check_desc_craft.py` registry row | 1,156 chars, 148 words | 822 chars, 108 words | −334 |
| `check_r75_routed_repairs.py` registry row | 922 chars, 122 words | 760 chars, 95 words | −162 |
| SKILL.md patch total | 2,525 chars | 1,977 chars | **−548 (−21.7 %)** |
| inserted lines | 3 (593 total) | 3 (593 total) | 0 |

Entry by section (rendered chars):

| section | draft | cut | delta |
|---|---|---|---|
| frontmatter (`source:`/`verified-at:`/`recheck:`/`ground:`) | 1,667 | 1,596 | −71 |
| title + intro + rule table | 2,603 | 2,141 | −462 |
| `## This lane's own description, measured` | 3,023 | 2,623 | −400 |
| `## What this entry does not claim (Q62)` | 1,012 | 895 | −117 |
| `## Limits` | 1,569 | 1,366 | −203 |
| `## Related` | 876 | 561 | −315 |

## 2. What was cut, and why a reader cannot act on it

**Entry.**
1. **Rule table `page` column dropped** (five repetitions of `optimizing-descriptions`; the paragraph
   above the table already names the one page and its digest). Location cells switched from
   `optimizing-descriptions.md:25` to the cartesian shorthand `:25`, which the counter's own docstring
   names "the round-74/round-76 entry house style" (`cited_lines()` accepts both forms).
2. **Measure table third column dropped.** It restated the render convention already stated in the
   paragraph above it; the convention now appears once, with both numbers (`clip 1022`, stripped 1021,
   first sentence 151) and the `verifiers/check_desc_craft.py` conjunct (d) pointer kept.
3. **Findings bullet 2:** the deployment fact was stated twice — once as the example (the quote) and
   once as a restatement of `frontmatter-trigger-surface.md`'s rule text. The rule text is the home of
   that document; the pointer `:153`–`:154` stays.
4. **Q62 bullet 2:** the "authoring maximum ≠ render cut" explanation is `skill-listing-thresholds-round54.md`'s
   Findings 1–2; cut to one clause + the pointer (and the pointer's range corrected, § 6.3).
   **Q62 bullet 3:** the eval-protocol scope statement exists in the lesson's `Reject (held)`; cut to
   one sentence with both pointers.
5. **Related:** each bullet now carries the pointer plus only the caveat that changes how it is used
   (evidence class, §12 routing status); the explanations of those documents' contents were removed
   because they are the documents' own business.
6. **`ground:`** compressed from a narrative of what the anchor/`used-by` held to the two checkable
   facts (old `used-by`, and the base-`b7f13f4` phrase sweep that matched 0 files).
7. **`## Limits`** keeps all four bullets and every non-claim; only wording was tightened (−203).

**SKILL.md patch.**
8. **Rule row:** `, and err pushy` removed — the rule is already the verbatim fragment
   `"Err on the side of being pushy"` in the same row. `, including ones the user never names` removed —
   fragment four (`"Explicitly list contexts where the skill applies, including cases where the user
   doesn't name the domain directly"`) states it verbatim in the same row. Three cells, `S213`, the
   entry path and all three fragments remain.
9. **Registry rows:** the exhaustive conjunct lists were the counter docstrings' subject; cut from the
   rows. Kept: kind, entry command, `0=clean, 1=failed, 2=could-not-evaluate`, the round label and the
   frozen verdict line, `--self-test`, the pinned-values location, write scope, owner. The rows stay one
   line each, so the 600-line budget is untouched (593).

Nothing was cut that the C1 counter reads: no quote, no fragment, no citation line, no provenance field,
no audit number.

## 3. Proof — the counter scores the same conjuncts

Scratch clone `/fast/scratch/hyaku/kotoba-r77/X01Simplifier/clone` (shared clone of the lane,
`git rev-parse --show-toplevel` = the clone, author `scratch-r77 <scratch@example.invalid>` before the
first commit). Two worlds per lesson variant; every run captured the **gate's own** exit status
(`cmd > out 2>&1; echo "exit=$?"`), never a pipeline's:

| world | what it holds | C1 output | own exit |
|---|---|---|---|
| D-A `66e7499` | r76 drafts, lesson as filed | `description craft backed 5 of 6` | 1 |
| X-A `ff185a2` | X01 cuts, lesson as filed | `description craft backed 5 of 6` | 1 |
| D-B `7727393` | r76 drafts, lesson Gate quote de-backticked (§ 6.1) | `description craft backed 6 of 6` | 0 |
| X-B `7202829` | X01 cuts + cut registry rows, same lesson fix | `description craft backed 6 of 6` | 0 |

Per-conjunct notes are identical between the paired worlds (full text in `X01Simplifier.receipt.txt`):

- (b): **11** located page-unique quotes in both, and **the same set** (compared as sets, not counts).
- (c): 1 Body craft row citing entry + S213, carrying **3** located fragments in both.
- (d): clip **1022** / stripped **1021** / first sentence **151**, equal in both.
- (e), (f): pass in both; the entry text changes do not touch them.
- (a): fails in both A-worlds and passes in both B-worlds — the failure is the draft lesson's, not the
  cut's (§ 6.1).

Operability of the cut registry rows: `check_gate_registry.py --rev X-B` → `62 of 62`, phantom 0,
**own exit 0**; at the base the same gate prints `60 of 62` for the two unregistered counters, own
exit 1. `SKILL.md` is 593 lines with the three rows applied; `## Gate registry` 446, `## Sources` 517.

The only files that differ between the paired worlds are `SKILL.md` (the row swap; plus the two registry
rows in the B pair) and the entry (`git diff --stat`, receipt).

The **delivered** files themselves were re-applied verbatim — `X01Simplifier.entry.md` plus the three
rows parsed out of `X01Simplifier.skill-patch.md` — to a fresh commit `d68feab`; the counter reads
`6 of 6`, own exit 0 (receipt, last block).

Independent quote check (not trusting the draft): each of the five rule-table quotes and each of the
three row fragments occurs **exactly once** in `snapshots/optimizing-descriptions.md` and **zero** times
in `evaluating-skills.md` and `best-practices.md`. The draft's audit figures were re-derived from
`SKILL.md` at base: render 1022 clip / 1021 stripped, first sentence 151, 8 quoted trigger phrases,
108 characters of quoted span, 7 sentences — all hold.

## 4. Duplicated facts (one authoritative home per fact)

| fact the draft repeats | authoritative home | draft repetition | what the cut does |
|---|---|---|---|
| a file outside the omp discovery roots never routes, so `description` craft there is audit-hygiene | `corpus/knowledge/frontmatter-trigger-surface.md:150`–`:155` (§12), sentence at `:153`–`:154` | Findings bullet 2 restates the rule text; Related bullet 2 explains §11/§12 in its own words | keeps the example quote and the `:153`–`:154` pointer; the rule text is no longer restated; Related keeps the pointer + the evidence-class caveat only |
| an authoring maximum is not a render cut; 1,024 is the spec's ceiling, not a client cut; which client cuts/budgets at what number | `corpus/knowledge/skill-listing-thresholds-round54.md:15`–`:21` (Findings 1–2; omp's 99-char cut at `:33`) | Q62 bullet 2 restated the distinction and the pointer | one clause + the pointer; the pointer range corrected to `:15`–`:21` (the draft's `:15`–`:16` covered Finding 1 only, while the sentence also claims Finding 2's content) |
| the omp first-sentence render path does not reach a file outside a discovery root | `corpus/knowledge/render-mechanism-round7.md` + `frontmatter-trigger-surface.md` §9/§12 | Related bullet 2's trailing clause | pointer kept, clause cut |
| the trigger-rate protocol is recorded, not admitted | `corpus/lessons/round-76.md` § Gate `Reject (held)`; S213's row | Q62 bullet 3 and § Limits both restate scope | Q62 keeps one sentence + pointers; Limits keeps the evidence class |
| the 1021/1022 render convention | `plans/round-76-addendum-1.md` § Render-length convention (frozen), printed beside the number | the measure table's third column restated it beside the prose | stated once in the paragraph, both numbers kept |

No duplicate was resolved by deleting the pointer; only the restatements went.

## 5. What I deliberately did not cut

- The five rule rows, their quotes, `rule`, `tokens` and `action` cells: each is a distinct page rule and
  an instruction a skill author acts on.
- The `recheck:` command: it is the freshness probe, not prose.
- The three registry rows as lines: the SKILL.md budget is a **line** budget and the rows are one line
  each; the cut is character weight, not lines.
- The entry's `## Limits` bullets and the Q62 non-claims: they are the honesty surface a reviewer acts on.
- The other r76 drafts (lesson, sources, LOG, SCORECARD): not this seat's artifacts.

Tradeoff if the L1 wants the page column back in the rule table: 5 × 26 ≈ 130 chars, no counter arm
changes; I cut it because one page named once is the house rule for a single-page entry.

## 6. Defects found in the inputs (reported, not silently fixed in the lane)

1. **The round-76 lesson draft, as filed, fails C1 (a).** Its Gate quote is
   `"`A few sentences to a short paragraph is usually right`"` — the backticks sit *inside* the double
   quotes, so `quote_spans()` yields a span containing backticks, which is not a substring of the page.
   The counter prints `(a) the lesson Gate carries no <=25-word quote located in the
   optimizing-descriptions snapshot`, `5 of 6`, exit 1. Minimal repair: move the backticks outside the
   quotes (`` `"A few sentences to a short paragraph is usually right"` ``). Proven: with that one edit the
   same drafts score `6 of 6`, exit 0 (D-B). This is the difference between the A and B worlds above; it
   must be fixed in the landed lesson or C1 cannot close, independently of any cut.
2. **The patch draft's anchor list is stale in one place:** it says `## Gate registry` "stays line 448".
   Measured at the r77 base: 445, patched 446. The other anchors hold (rule row 217, registry rows
   514–515, `## Sources` 514→517, budget box 285→286, 590→593 lines).
3. **The entry draft's `skill-listing-thresholds-round54.md` cite** (`:15`–`:16`) under-covers the
   sentence it supports (Findings 1 **and** 2); corrected to `:15`–`:21` in the cut.

## 7. Axes

- **Depth**: unchanged claim, but the entry now carries the same sourced content in 14.3 % fewer
  characters and the SKILL.md patch in 21.7 % fewer, so a reader reaches the rules sooner.
- **Consistency**: the cut follows the lane's own house forms (r74 rule table, `:N` shorthand, registry
  eight-column shape) and removes the r76 draft's two copies of facts owned elsewhere.
- **Calibration**: no number was added; every number kept was re-derived (1022/1021/151, 8 phrases/
  108 chars/7 sentences) or verified (quote occurrence counts).
- **Operability**: the cut rows are proven conformant by `check_gate_registry.py` (62 of 62) and the
  counter still exits 0 on the cut world; the anchors are measured on the r77 base, not copied.
- **Freshness**: no new source, no re-fetch; S213's digest and the page snapshot are untouched.

## 8. Scope / hygiene

- Wrote only `.ufo/waves/round-77/build/X01Simplifier.*` and `.ufo/waves/round-77/w1/X01Simplifier.md`.
- No lane/fleet git or jj write; scratch clone only, removed before yield.
- No tool installed or upgraded.
- `pacman` not run.

VERDICT: cut accepted: entry −1,568 chars (−14.3 %) and SKILL.md patch −548 chars (−21.7 %) with the C1 counter scoring the identical six-conjunct set (11/11 same quotes, 3/3 fragments, 1022/151) at 6 of 6, plus two input defects found (lesson Gate quote blocks (a) as filed; stale registry anchor).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/X01Simplifier.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/X01Simplifier.entry.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/X01Simplifier.skill-patch.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/X01Simplifier.receipt.txt
