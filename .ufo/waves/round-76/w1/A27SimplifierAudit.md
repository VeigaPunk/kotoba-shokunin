# A27SimplifierAudit — economy attack on `corpus/knowledge/description-craft-round76.md` (round 76, w1)

VERDICT: report-only — audited draft `build/entry-draft.md` sha256 `6ff08be67d8e20312e541b7467c83f927c6c7f9e20882e015ffe188e77d1e4f9` (110 lines, 12,235 B); 11 cuts proposed, 0 applied, 0 lane files edited, 0 claim data written.

## Axes named

| axis | what it asks | why it is the seat's |
|---|---|---|
| E1 single-home fact | each admitted fact has exactly one corpus entry that states it; elsewhere it is a pointer | duplicate authority is the weight this seat removes |
| E2 conjunct coverage | every frozen conjunct (a)–(f) is readable from the draft's bytes | a cut that breaks a conjunct is harm, not economy |
| E3 sentence load | no sentence that carries neither a fact, a boundary, nor a pointer | restatement without restating an owner |
| E4 pointer over restatement | a cross-reference replaces a repeated fact, not decorates it | the lane's index convention (`## Related`) already exists |
| E5 convention singularity | one number, one measurement convention, named once | two render conventions in one wave is a second convention by another name |

## Version audited

Copy taken for a stable read (`/fast/scratch/hyaku/kotoba-r76/A27SimplifierAudit/entry-draft.snap.md`, sha256
`6ff08be6…1e4f9`); the live draft was being revised while this seat read it, so all line numbers below are of
that snapshot. Snapshot content's own header and § numbering: header lines 1–4, intro 8–12, quote method 14–20,
rule table 22–29, measured table 36–39, verdict table 48–54, findings 58–67, Q62 71–80, Limits 84–98,
Related 102–107.

## Ownership map — what already has a home

| rule family in the draft | existing owner (committed bytes at base `b7f13f4`) | draft treatment that is correct | draft treatment that repeats |
|---|---|---|---|
| eval half: query set, repeated runs, 0.5 rate, train/validation split, loop counsels | `corpus/knowledge/skill-eval-artefacts-round70.md` F7 (`:33`), "Trigger sets are labelled, repeated and split" (`:48-51`), same page S210/S213 | L77–80 names it out of scope by assignment, pointer present | the four named facts in L77–78 ("query set, repeated runs, rate threshold, train/validation split and loop counsels (`:157`, `:159`)") restate round70's own table |
| 1,024 authoring maximum and its validator constant | `corpus/knowledge/frontmatter-rule-authorities-round48.md:44`; `corpus/knowledge/skill-listing-thresholds-round54.md:15-16` | row 29 delegates in its action cell; Q62 bullet 74–76 delegates again | the delegation appears three times (row 29, Q62 bullet, Related L103–104) |
| description render / H7s / 94-char reach / cache-or-truncate | `corpus/knowledge/render-mechanism-round7.md`; `corpus/knowledge/sibling-description-rewrites-round8.md` §1 (`:51` measured 94) | Related pointer only (L106) | none — kept out, correct |
| literal trigger strings, anti-trigger clause, sibling arbitration | `corpus/knowledge/sibling-description-rewrites-round8.md` §3.0 + `SKILL.md` trigger-fidelity checklist | audit is S213-scoped; no checklist restatement | none |
| "description carries the whole trigger surface" | `corpus/knowledge/spec-skill-creation-craft-round74.md` ("The description is the whole trigger surface"); `corpus/knowledge/frontmatter-trigger-surface.md:29,96,111` | one pointer clause, L8–9, no quote | none |
| discovery-root fact (a file outside a root never routes) | `corpus/knowledge/frontmatter-trigger-surface.md:153-154` (§12) | finding cites it, does not restate it | none |

Residual (correctly unowned, the entry's only new facts): imperative phrasing, user intent-not-mechanics,
pushy breadth including unnamed contexts, a few-sentences length budget, and the absence finding
(no front-loading / no self-contained-first-sentence rule on this page).

## Cut list (each item names the anchor text in the audited snapshot)

Ranked by weight removed per word lost. "Saved" is lines of the 110.

| # | anchor (snapshot) | what it repeats / why it is dead weight | action | saved |
|---|---|---|---|---|
| C1 | L18–20 "The page teaches the first two rules by example as well: its worked \"After\" block (`:184`–`:188`) puts the capability clause first and the imperative trigger clause second, and `:192` reads the improvement as…" | the identical fact is stated again at L71–73, where Q62 needs it for the absence finding and where the sweep that grounds it lives. Two citations of one example paragraph = one owner too many | cut L18–20, keep L71–73; the method paragraph ends at "page-unique, not site chrome." | 3 |
| C2 | L96–98 "**1022 vs 1021 is one named measurement choice.** The folded block ends with a newline: the YAML parse includes it, a hand fold does not…" | the same explanation is inside the L38 cell ("the folded block's terminal newline included (1021 without it)"). Two homes for one convention choice, and the bullet is the one that reads as an apology | cut the bullet; keep the cell, worded as the plan words it ("whole block, terminal newline included"), and let the counter's docstring own the convention | 3 |
| C3 | L64–67 "**This round does not rewrite the description.** C2's R1 pins the render at 1022, recomputed from… `.ufo/waves/round-76/receipts/r1-folded-render.txt`…" | round mechanics in a durable entry: R1's own receipt and LOG line carry it, and the bullet restates 1022 a third time in the same file | cut to one clause in the findings head: "no description edit lands this round (R1 pins the render)" | 3 |
| C4 | L91–93 "…judgement assigned to non-author attack seats — `A01RevQuoteLocate` (location, word count, page-uniqueness), `A17CritAudit` (verdict support in the page's own text), `A13CritHollowC1` (…)" | three round-scoped seat ids in an entry that outlives the round; the plan already names them | cut the parenthetical trio, keep "this wave's non-author attack seats and the round closure" | 2 |
| C5 | L54 "\| re-check after an edit (`:159`, line only, no quote here) \| **standing constraint** \| …" | a verdict row for a rule the rule table no longer carries (the loop rows were cut), evidenced by a bare line number — the one row in the file with no located quote | cut the row | 1 |
| C6 | L77–78 "The query set, repeated runs, rate threshold, train/validation split and loop counsels (`:157`, `:159`)…" | four fact names restating round70 to say "not ours"; the pointer does that work alone, and the `:157`/`:159` citation cites text the entry does not admit | cut the enumeration and the section citation | 1 |
| C7 | L52–53 (rows `short` + `hard limit 1024`) | the page states both in one bullet (`:28`); split, the file prints "1022 characters" twice and "2 characters of headroom" twice | merge into one row: `short — 1022 chars in 7 sentences, 2 chars of headroom under 1024` | 1 |
| C8 | L50 "8 quoted trigger phrases in 149 characters plus 3 anti-trigger categories in 153" | 149 and 153 are *sentence* lengths (measured: sentence 2 = 149 chars, sentence 3 = 153), not phrase spans — the 8 quoted spans total 108 chars. The numbers name the wrong quantity, so they are dead weight and a calibration defect | cut both numbers, keep the counts (8 phrases, 3 categories) | 0 |
| C9 | L41–42 "148 words … 9 sibling lanes named" | neither number is used by any verdict row; both are `verifiers/check_sibling_census.py`'s measured fields (G1 lane naming, G4 length) — a second authority for numbers this entry does not need, and the lane count is the claim most likely to rot | cut both | 0 |
| C10 | row 22 header `\| page \| S id \| rule \| quote \| location \| tokens \| action \|` — `page` cell is `optimizing-descriptions` in all six rows | a constant column; the page is already named in L14. (Round 74's table keeps it because it spans three pages — copying the shape here carries a column that is load-bearing there only) | drop the `page` column, keep `S id` per row | 0 |
| C11 | L1 "…§ The optimization loop (`:149`–`:159`)…" | an anchor section the entry admits nothing from (all loop rules were cut). An over-broad anchor is exactly what conjunct (e)'s anchor log will record | trim to `§ How skill triggering works (:13)`, `§ Writing effective descriptions (:21`–`:28)`, and the worked example (`:184`–`:192`) | 0 |

Total lines saved by C1–C7: **13** (110 → 97). C8–C11 are width/claim-shape cuts with no line change.

## Budget finding (this seat's own earlier number, withdrawn)

I sent the entry seat a ≤70-line / ≤6-quote budget before the draft existed; that number was mis-priced, and
the draft's reply is right to refuse it. Counted on the snapshot (script, not by eye): 110 lines = 4 header +
5 headings (title + 4 `##`) + **21 table lines** (rule 8, measured 4, verdict 9) + 6 Related bullets +
18 blank separators + **56 prose lines**. Frozen core is therefore 36 content lines and 54 with its blanks;
prose is 56, not 63. C1–C7 take prose to 43, so the floor under the current table design is **97 lines
/ ~10.5 KB** — larger than round 70's entry (88 lines, 9,926 B), which has one table where this one has three.
The honest budget for this entry is "≤100 lines, every prose sentence carrying a fact, a boundary or a
pointer", not 70.

## Preserved contract (must not be cut by any of the above)

| conjunct | carried by (snapshot lines) | survives |
|---|---|---|
| (a) snapshot chain | header trio L1–4 (URL, sha256, fetch record) + L14–16 | yes |
| (b) ≥4 located quotes, ≤25 words, page-unique | rule table 24–29 → 6 quotes after cuts, measured 9/13/7/17/10/7 words; plus header quote `:9` (20) and Limits quote `:19` (17) | yes, 6 ≥ 4 |
| (c) act-on row | `SKILL.md` patch, not this entry | n/a |
| (d) audit values = counter recompute | measured table 36–39 (1022, 151) | yes — C2 keeps one convention statement, not zero |
| (e) registry used-by | `corpus/SOURCES.md` row S213, another seat | n/a |
| (f) provenance trio | L1–3 | yes |

## Evidence (commands run in this seat, at base `b7f13f4` + untracked wave dirs)

1. **Quote verification** — Python over the three snapshots, for all 11 quotes the draft uses or cites
   (`:9`, `:25`, `:26`, `:27`×2, `:28`×2, `:157`, `:159`, `:17`, `:19`): each occurs **once** in
   `optimizing-descriptions.md`, **0** times in `evaluating-skills.md` and **0** times in
   `best-practices.md`, at the line the draft cites, with **≤25 words** (20/9/13/7/17/10/7/6/7/8/17). Exit 0.
2. **Recheck line executes** — the first audited version's L3 loop verbatim prints `1` for each of its seven tokens, exit 0 (the final version runs eight; see the final scan).
3. **Absence sweep (Q14)** — `grep -icF` for `front-load`, `front load`, `use case`, `lead with`,
   `starts with`, `first sentence`, `self-contained` on the snapshot: `0 0 0 0 0 0 0`. Exit 1 per term
   (no match), which is the claim's point.
4. **Description measurement** — `SKILL.md` frontmatter parsed two ways:
   `---\n(.*?)\n---` capture + `yaml.safe_load` → **1021** chars, no terminal newline;
   `---\n(.*?\n)---` capture → **1022** chars, terminal newline. First sentence **151**; 148 words;
   7 sentences; 8 double-quoted spans totalling 108 chars; sentence 2 = 149, sentence 3 = 153.
   The lane's existing readers agree with 1021: `verifiers/check_sibling_census.py:380` `description_of`
   (ws-collapsed, block indicator stripped) returns 1021, and `verifiers/verify_harness_claims.py:324`
   (`len(re.sub(r"\s+"," ",desc).strip())`) reads the same field the same way.
5. **Facts the draft cites elsewhere** — `skill-listing-thresholds-round54.md:15-16` does say four clients
   document 1,024 and none documents a cut there; `frontmatter-trigger-surface.md:153-154` does say
   "`description` craft is audit-hygiene, not routing surface". Both verbatim, so C6's and C2's cuts remove
   repetition, not support.
6. **Counter state** — `verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` did not
   exist at audit time, so conjunct (d)'s recompute convention is still open. That is why E5 is on the list:
   whichever convention the counter implements becomes the number the entry must print, and the entry should
   print it once.

## Adjacency / calibration notes that change weight

- **1022 vs 1021 is not a stylistic pair: it moves a second number.** The repair brief's "2 characters of
  headroom" is 2 under the 1022 convention and 3 under the 1021 one used by two existing counters. One
  convention, named once, in one place (the counter docstring + the L38 cell), keeps the headroom claim
  single-valued. If the counter lands on 1021, C2's frozen `r1-folded-render.txt` (plan: "prints 1022")
  breaks — so the convention is a C1/C2 coupling, not a wording choice.
- **L8 says "four principles", the rule table has six rows.** Correct (bullets `:27` and `:28` each state two
  rules) but unstated, so a reader can count a contradiction. Cheapest fix is four words in the table caption
  or the row-26/27 pairing order, not a new sentence.
- **The recheck line and the `tokens` column pin different strings.** The loop pins quote fragments
  (`Frame the description as an instruction`, `doesn't name the domain directly`); the column pins the page's
  bold lead-ins (`Use imperative phrasing`, `Explicitly list contexts where the skill applies`). Both are
  legitimate pins; the cost is two vocabularies a reader must reconcile, and only two of six column tokens are
  exercised by the loop. One clause in the caption ("`tokens` is the page's lead-in, not a recheck token")
  buys the reconciliation for less than rewriting either list.
- **Rule 1 (imperative phrasing) is adjacent to, not the same as, `frontmatter-trigger-surface.md` §11.**
  §11 is an observation — all 5 literal `ufo` misses in opencode.db were domain mentions, so "pair the noun
  with slash-form or imperative-context triggers" (`:148`–`:149`, measured 2026-09-28) — while rule 1 is the
  page's advice. Different evidence classes, so neither entry should absorb the other; a half-clause on the
  rule-1 row ("the same shape §11 measured") buys the distinction and stops a closure reader scoring a second
  authority. A corpus-wide sweep for the four rule phrasings confirms no entry states them today
  (`grep -rniE "imperative (phras|descript|verb|trigger)|user intent|err on the side|be pushy|a few
  sentences|short paragraph" corpus/knowledge/*.md SKILL.md corpus/QUALITY.md` → 1 unrelated hit,
  `trigger-miss-proxy-round6.md:13`, a session-text field), so the entry's "no entry carried the writing
  principles" ground line holds and its four rules have no rival home.
- **Header quote `:9` is never used in the body.** It is the page's failure-mode claim and it is page-unique,
  but nothing in the entry exercises it. Either the intro names the two failure modes (it is the page's own
  framing of why the four rules matter) or the header quote is decorative. Not a cut — a tie-in, because
  Q12/round-74 convention puts a located quote in `source:`.

## Tradeoffs and what this seat did not do

- **Cut C10 (the `page` column) trades lane convention for width.** Round 74's rule table has the same seven
  columns; there the column varies. Keeping it here costs six repeated cells and buys shape-identity with the
  precedent. I rank it below C1–C7 for that reason: it is a shape call, not a weight call.
- **Cut C4 (seat names) trades in-round verifiability for durability.** The plan names the three seats, so no
  evidence is lost by dropping them from the entry; a closure reader who wants the assignment reads the plan.
- **Cut C5 removes a verdict a reader might want** (the growth warning at `:159` *is* relevant with 2 chars of
  headroom). But the rule is not admitted, so the row cannot cite it as evidence, and the headroom fact is
  already in the merged row C7. If the entry writer prefers keeping a `:159` line, it belongs in Limits as a
  one-clause standing risk, not as a verdict row.
- **No edits made.** This seat attacked economy only: no file under `corpus/`, `verifiers/`, `SKILL.md` or the
  wave `build/` tree was written; the lane tree's shared bytes are unchanged by this seat, and the only file
  written is this report. Scratch (`/fast/scratch/hyaku/kotoba-r76/A27SimplifierAudit/`) is removed before
  yield.
- **Not judged here**: whether the page's rules are the right ones (assigned to `A17CritAudit` and closure),
  whether a restatement world can satisfy the counter (`A13CritHollowC1`), quote location/word-count
  re-derivation (`A01RevQuoteLocate`). This seat's numbers are economy counts, not verdicts on the claim.

No tools were installed; no package manager was run.

## Re-scan after the entry seat's revision (B12EntryDraft)

Re-audited `build/entry-draft.md` sha256 `80276920b37c3ba157877514c146b0eb6a04d65c17d0bc5a631499a2dc6738d7`
(101 lines, 11,153 B; composition 4 header + 5 headings + 19 table lines + 4 Related + 17 blanks + 52 prose).
Cuts taken: C1, C3, C5, C6, C7, C8, C9, C11, and the cell half of C2. C4 is declined with a reason I accept
(the plan asks judgement assigned to *named* seats, and the ids are the checkable form). Net: 110 → 101 lines,
12,235 → 11,153 B.

Survives the re-scan: (a) header trio; (b) five rule quotes (9/13/7/17/10 words) + header `:9` (20) + Limits
`:19` (17), all verified once-in-page and absent from both baselines; (d) the measured table still carries
1022/151; (f) provenance. The recheck loop runs at six tokens, `1` each, exit 0.

Remaining, in weight order:

- **R1 — the convention has two homes again.** The measured cell now says "the folded block's terminal newline
  included" (right home, 8 words) and Limits still spends six lines on the same choice. Keep the cell phrase;
  cut the Limits bullet to the contested half only — the two readers' names and the headroom consequence —
  ≤2 lines. Saved: 3–4.
- **R2 — a Q23 risk the revision introduced.** Row `the 1,024 ceiling (:28, authority frontmatter-rule-authorities-round48.md:44)`
  attributes a rule to the page with **no located quote** in the cell, while the Q62 bullet attributes the same
  number to round54 and Related lists round48 — three delegations and one unattributed rule. Cheaper than
  adding an attribution: restore the 7-word page quote (`enforces a hard limit of 1024 characters.`, verified
  page-unique) and drop the `authority …` clause, leaving authority in Q62 + Related. No line cost, one more
  quote than the ≥4 floor needs.
- **R3 — one quote is unpinned.** The recheck's six tokens cover the header quote and the five rows; the Limits
  `:19` quote ("typically only consult skills…", `grep -c -F` = 1) is not among them. Add a seventh token or
  drop the quote — an unpinned quote is the one kind of drift the recheck line exists to catch.
- **R4 — `page` column still constant** across the five rows (`optimizing-descriptions` each time). Lowest
  weight: shape call against round 74's seven-column precedent, kept or dropped on that ground alone.

Floor after R1–R3: ~97–98 lines, unchanged from the first audit — the 13-line cut I proposed and the ~3 that
remain are what the current table design allows. Nothing in the re-scan moves a conjunct.

## Final scan (R1–R3 applied, R4 declined)

`build/entry-draft.md` sha256 `72d4f40d2e0e86abc9b9d328fd6814d58fa95e353a8bb972d4fcde581a5e33d6` —
**98 lines, 10,947 B** (4 header + 5 headings + 19 table lines + 4 Related + 17 blanks + 49 prose). From the
first audited version: 110 → 98 lines (−12), 12,235 → 10,947 B (−1,288). Prose: 56 → 49.

Verified on these bytes, not on the writer's description of them:

- **R1 (convention one home)** — the measured cell names the terminal-newline convention; Limits carries only
  the contested half: both readers (`check_sibling_census.py` `description_of`, `verify_harness_claims.py`'s
  collapse+strip) report 1021, headroom becomes 3, and either counter breaks C2's R1 receipt. Four lines, no
  restatement of the cell.
- **R2 (Q23 attribution)** — the ceiling row now quotes `enforces a hard limit of 1024 characters.` in the cell
  and drops the `authority …` clause; authority survives in Q62 (`skill-listing-thresholds-round54.md:15`–`:16`
  + `check_description_thresholds.py`) and Related (`frontmatter-rule-authorities-round48.md:44`). A rule
  attributed to the page now carries its located quote.
- **R3 (every quote pinned)** — the recheck loop runs eight tokens, `1` for each, exit 0
  (`under-specified description`, `Frame the description as an instruction`, `not the skill's internal
  mechanics`, `Err on the side of being pushy`, `doesn't name the domain directly`, `A few sentences to a short
  paragraph`, `hard limit of 1024 characters`, `typically only consult skills`). Independently checked each
  token against `evaluating-skills.md` and `best-practices.md`: `0` and `0` for all eight, so the eight pins are
  page-unique as well as page-present. Every quoted span the recheck covers is one of those eight — but the
  file carries a **ninth** page-verbatim span the loop does not pin: the unnamed-domain verdict cell's
  "even if they don't explicitly mention" (6 words, `grep -c -F` = `1` in the page, `0` in both baselines at
  `entry-draft.md:43`). It is a fragment of the *same* page sentence row 4 quotes, so it is either an
  extension the 25-word ceiling will not take or a ninth token; a de-quoted paraphrase avoids both. Recorded
  here because my own first pass counted tokens instead of spans and would have certified "all pinned".
- **R4 (constant `page` column) — declined, correctly.** The reason is better than my cut: `page` is the
  round-74 `check_spec_craft.py` table shape, and B06's counter may reuse that parse; the column buys a shared
  parse for 5 characters a row. Withdrawn.

Conjuncts on the final bytes: (a) header trio; (b) eight page-unique quotes ≤25 words, five in the rule table
(floor is four; the ninth, unpinned 6-word fragment in the unnamed-domain verdict cell is not one of them); (d) 1022 / 151 in the measured table, convention named once; (f) provenance trio. Nothing
moved. Economy is at its floor for this table design: the remaining bulk is three tables (19 lines) and a
49-line prose body in which every sentence is now a fact, a boundary, or a pointer.
