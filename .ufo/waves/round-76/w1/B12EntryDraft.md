# B12EntryDraft — draft `corpus/knowledge/description-craft-round76.md`

Seat: leaf, report-only. No subagents, no background jobs, no installs (nothing installed; only `python3` +
PyYAML, `grep`, `sha256sum`, `git show` were used). No scratch directory created. No git/jj write of any kind;
no file touched outside the two named artifacts.

Artifacts:

- draft — `.ufo/waves/round-76/build/entry-draft.md` (98 lines by `wc -l`, 11,054 bytes, final)
- landed copy (L1 integrates) — `corpus/knowledge/description-craft-round76.md`

VERDICT: DRAFT-COMPLETE — provenance trio + ground first; 5 located page-unique quotes (b needs ≥4); measured
audit rows 1022 / 151 verbatim; Q62 refusals with sweep evidence; Limits naming documentary evidence, no
client run, held eval-fidelity and the non-author judgement seats. Every local self-check exit 0. Not landed,
so (b)/(d)/(f) are not yet readable by the frozen counter from its frozen path.

## Behaviour

Order in the file is exactly the plan's: `source:` (S213 + URL + section anchors) → `verified-at: 2026-10-27`
→ `recheck:` → `ground:`, then title and body.

1. **Admitted rules** — one markdown rule table, columns `page | S id | rule | quote | location | tokens |
   action` (the r74 `check_spec_craft.py` house shape plus `location`). Five rows, five quotes, each a
   contiguous substring of a single snapshot line: `:25` imperative phrasing, `:26` user intent, `:27` pushy,
   `:27` unnamed-domain contexts, `:28` a few sentences.
2. **Self-audit** — measured rows (`rendered description length (characters) | 1022`,
   `first sentence length (characters) | 151`) plus six verdict rows on this lane's own `description`:
   imperative **not met**, intent **partial**, pushy **met** (8 quoted trigger phrases, 108 characters of
   quoted span, 3 anti-trigger categories), unnamed-domain contexts **partial** (2 of 8 phrases avoid the
   artifact nouns), short **not met** (1022 characters, 7 sentences), the 1,024 ceiling **met at the edge**
   (2 characters of headroom; the ceiling is an audit row citing `:28` + `frontmatter-rule-authorities-round48.md:44`,
   not a re-derived rule).
3. **Q62 refusals** — front-loading and self-contained-first-sentence refused on a 0-hit sweep (with the page's
   worked example `:184`–`:188` showing the trigger clause second); the 1,024 number refused as a "client
   render cut" (authoring limit; `skill-listing-thresholds-round54.md:15`–`:16`); the eval protocol refused **by
   assignment, not by absence** (page-supported, held).
4. **Findings** — the imperative gap; the cheapest cut (the 87-character deployment note, whose fact is already
   `frontmatter-trigger-surface.md:153`–`:154`); and why this round must not rewrite the field.
5. **Limits** — documentary evidence with the page's `:19` caution; audit rows are reads of a string, not of a
   router, with judgement assigned to `A01RevQuoteLocate`, `A17CritAudit`, `A13CritHollowC1` and the closure;
   the 1022 convention, contested inside the lane (below); snapshot-relative line numbers.

## Gates (commands as run, with exit codes)

All from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

- **Measured field** (`python3` + `yaml.safe_load` on the frontmatter, `len()` of the parsed `description`):
  `1022`; first sentence (`split('. ')[0]` + period) `151`; 148 words; 7 sentences; 8 quoted spans totalling
  108 characters; `1024 − 1022 = 2` headroom. exit 0.
- **Same measure at base**: `git show b7f13f4b39cbd43076a85568adca763a6f674e7a:SKILL.md` → `1022` / `151`.
  exit 0.
- **Recheck command printed in the entry**, run as written: nine tokens, `1` each, exit 0
  (`under-specified description`, `Frame the description as an instruction`, `not the skill's internal
  mechanics`, `Err on the side of being pushy`, `doesn't name the domain directly`, `even if they don't
  explicitly mention`, `A few sentences to a short paragraph`, `hard limit of 1024 characters`, `typically only
  consult skills`). The ninth was added after `A27SimplifierAudit-3` found it in the unnamed-domain verdict
  cell — a fragment of the same page sentence row 4 quotes, quoted separately because row 4 is at the 25-word
  ceiling.
- **Quote location + uniqueness** (script over the three round-76 snapshots): 5/5 rule rows `page=True`,
  `uniq=True` against `evaluating-skills.md` and `best-practices.md`, `after=True`, words `9, 13, 7, 17, 10`;
  the two quotes outside the rule table also check clean — the ceiling quote (7 words) and the Limits quote
  `typically only consult skills…` (17 words) — and the header `source:` quote (`:9`, 20 words) is page-unique
  too. Eight claim quotes in total, five in the rule table, against (b)'s floor of four, plus the verdict-cell
  fragment above; every page-verbatim span in the file is page-unique and pinned by one of the nine tokens
  (the section name `Running multiple times` in `ground:` is the one page-verbatim string outside both — it is
  a heading reference, not a claim quote). exit 0.
- **Snapshot digests**: `sha256sum` → `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837` for
  optimizing-descriptions, equal to `snapshots/MANIFEST.sha256` and to `fetch-record.json` (HTTP 200, 13,403 B);
  the other two records `a799805f…` / `ab9f3b60…` also match the manifest.
- **Consolidated self-check** (trio order, 5 rule rows valid, audit rows `1022` and `151`, Limits section):
  ALL True, exit 0.
- **Ground sweep**: `grep -icE 'imperative phrasing|err on the side of being pushy|few sentences to a short
  paragraph|hard limit of 1024|burden of triggering'` over `SKILL.md corpus/knowledge/*.md corpus/QUALITY.md`
  → 0 files. `grep -rn 'check_desc_craft' verifiers/` → 0 hits. `wc -l SKILL.md` → 590.

## Touched surfaces

- Written: `.ufo/waves/round-76/build/entry-draft.md`, this report. Messages sent (not files): `KotobaR76`,
  `B06DescCounter`, `B07RepairCounter`, `A27SimplifierAudit-3`, `B15Simplifier`.
- Read only: `plans/round-76.md`, `SKILL.md`, `corpus/SOURCES.md` (S213), six `corpus/knowledge/` entries,
  `corpus/QUALITY.md`, `verifiers/{check_spec_craft,check_description_thresholds,check_sibling_census,verify_harness_claims}.py`,
  `.ufo/waves/round-76/{snapshots/**,build/quotes-s213.md,build/skill-patch.md,w1-spec.json,base-battery/**}`.
- Not written: the landed entry, `verifiers/**`, `SKILL.md`, `corpus/SOURCES.md`, lessons, LOG, SCORECARD,
  receipts.

## Out of scope (other seats)

- Land the draft; conjunct (e) fails until B14 appends the S213 `used-by`.
- `SKILL.md` § Body craft row + § Gate registry rows (B13, `build/skill-patch.md`). Its three fragments are all
  in the page, but the third — `Avoid adding specific keywords from failed queries` — is deliberately **not** a
  rule in this entry (eval-scope refusal), so the row should not lean on this entry for it.
- `check_desc_craft.py` + `--self-test` (B06), `check_r75_routed_repairs.py` (B07), all receipts.
- The `description` rewrite itself: no seat this round.

## Findings

1. **The lane's own description fails the page's first rule.** Sentence 1 is declarative ("audits, writes, and
   rewrites `SKILL.md` / `AGENTS.md` / …"); no clause is an instruction to act. Verdicts: imperative not met,
   intent partial, pushy met, unnamed-domain contexts partial, short not met, ceiling met at 2 characters.
2. **C1 and C2 collide on the same number, and the collision is deliberate.** R1's receipt pins the render at
   1022 at the measured tip; rewriting the description this round would move it and break R1. The entry states
   this and routes the repair forward instead of acting on it.
3. **The measurement convention is contested inside the lane — escalated.** 1022 is the YAML-parsed value
   *including* the folded block's terminal newline. The lane's two existing description readers report 1021 for
   the same bytes: `check_sibling_census.py` `description_of` (collapse + strip) and `verify_harness_claims.py`
   (`len(re.sub(r"\s+"," ",desc).strip())`). If either counter recomputes with those shapes it prints 1021,
   which breaks R1's frozen 1022 and C1's audit conjunct together; under that convention the headroom is 3, not
   2. Raised to `KotobaR76`, `B06DescCounter`, `B07RepairCounter`; recorded in the entry's Limits. The round
   then named the convention for the frozen targets (clip-preserving, receipts printing both variants) and B05's
   receipt records the same fork, so 1022 is single-valued at measurement time; the escalation stands only as the
   rule that a counter recomputing this cell must name it.
4. **Measuring the block, not the lines.** The block spans `SKILL.md` lines 4–18 but renders as one string — the
   r75 M75-1 failure mode. The entry names the method, and states the value once.
5. **Two rule families in the seat brief are not on the page.** "Front-load the use case" and "self-contained
   first sentence" return 0 hits (B04's sweep and mine agree); the page's worked example puts the trigger
   clause second. Both are refused with the sweep as the reason.
6. **Two economy attacks received across three revisions; all load-bearing cuts applied.**
   `A27SimplifierAudit-3` withdrew its ≤70-line budget on reading the tables (C1–C3, C5–C7 applied; C4 declined
   at first, then accepted by that seat). On re-scan it raised three, all applied: **R1** the 1022 convention had
   two homes, so the Limits bullet is now the contested half only (two readers + the 3-character consequence);
   **R2** the ceiling row attributed a rule to the page with no located quote — the 7-word quote
   `enforces a hard limit of 1024 characters.` is back in the cell and the authority clause is gone (authority
   stays in Q62 and Related); **R3** the Limits `:19` quote was unpinned, so the recheck loop now carries eight
   tokens covering every quoted span. **R4** (drop the `page` column) declined: the column is the r74
   `check_spec_craft.py` table shape, and B06's counter may reuse that header parse.
   `B15Simplifier` asked for the 1024 rule to be demoted (done — an audit row now), Related de-duplicated
   (6 → 4 bullets), Limits bullet 2 merged into bullet 1, and the unused counts dropped; its last item (O1)
   removed an intro parenthetical that claimed the principles were already held in the lane — `ground:` denies
   it and a check confirmed `spec-skill-creation-craft-round74.md` mentions S213 only as an exclusion and
   `frontmatter-trigger-surface.md` holds no principle, so the parenthetical went and `ground:` stayed. A27's
   final scan then found a ninth page-verbatim span (the verdict-cell fragment) unpinned by the recheck loop;
   the loop now carries nine tokens. Both simplifiers independently produced the 1021/1022 conflict, which is
   why it is escalated rather than noted. Final revision history: 110 → 98 lines (A27 verified the 98-line
   bytes) → 97 → 98 after the Limits convention clause landed on B05's receipt, 12,235 → 11,054 bytes; no quote,
   cell, token or conjunct moved after the 98-line scan except the additions named here.
7. **B05's audit receipt landed after this seat's first measure, and it agrees.** `.ufo/waves/round-76/receipts/description-audit-4de12b61f75c73e3675ef0e422cc2be0f7da8960.txt` reports 1022 (clip-preserving) /
   1021 (stripped), first sentence 151, 7 sentences, 8 literal quoted strings, headroom 2 — every value my
   table states. One label in it is off by one: it prints `description_body_lines = 4-17` while the block is
   lines 4–18 (line 17 ends "…never reads this", line 18 is "  text.", line 19 is the closing `---`) and its own
   `frontmatter_close_line = 19` agrees with mine; its measures are over the same bytes, so only the label was
   wrong. B05 regenerated the receipt twice from its scripts (verbatim capture preserved; the B12-caught label
   fix gave `66734c99…0863`, the sentence-7 count fix gave the current `332530f7…7ddd`, 439 lines / 29,552 B),
   and it now prints `description_body_lines = 4-18 (15 lines)`, the host note at 87 characters proper / 88 as
   rendered, and mechanics at 410 of the 1021-char text / 411 of the 1022-char render — one convention named per
   span. The entry states the same extent, now with the line count, and its measured cell names the convention
   (`clip-preserving … the stripped variant is 1021`, `151 … 150 without it`) so anything printing the number
   prints both, per the round's rule. The 4–18 extent is also the r75 closure's wording, so it is the lane's
   convention, not just R1's. The 1021/1022 fork itself is resolved in the round: the frozen targets take the
   clip-preserving parse and every receipt prints both variants, which is what the entry's Limits states.

## Known limits of this seat's output

- Every conjunct that reads a path (`corpus/knowledge/description-craft-round76.md`, S213 `used-by`, the
  `SKILL.md` row) is unproven until land.
- `check_desc_craft.py` does not exist yet, so it was not run; the self-checks above approximate (b), (d) and
  (f) only, and (d) is approximated by "the table carries the recomputed integers", not by executing the counter.
- Whether the page teaches these rules, and whether each audit verdict is supportable from the page's own text,
  is left to `A01RevQuoteLocate`, `A17CritAudit` and `A13CritHollowC1`.
