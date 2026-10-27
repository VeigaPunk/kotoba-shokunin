# C04CritRowFaithful — does the r76 § Body craft row (and the entry's rule table) restate S213 faithfully?

Seat: critic, round 77 w1. Inputs read in full: `.ufo/waves/round-76/build/skill-patch.md`, `entry-draft.md`,
`.ufo/waves/round-76/snapshots/optimizing-descriptions.md` (sha256 recomputed `7cc54fbb…bd837`, 196 lines),
`SKILL.md` §§ Compression rules / Body craft (lines 195–216), § Frontmatter craft (158–177, line 193),
`verifiers/check_desc_craft.py` conjunct (c) (lines 821–857), `plans/round-77.md`.
No client run; documentary check against the page's bytes only.

## Verdict in one line

The draft row is **not faithful**: it fuses three of the page's rules into one row, splices in two eval-loop
counsels (`:157`, `:159`) that the draft's own entry says are "recorded, not admitted", and its "re-check length
after each edit" restates a fact SKILL.md already homes (1024 limit). Replace it with the three-row set below
(passes C1 conjunct (c); +5 lines → 595 ≤ 600).

## Counterexamples (evidence)

1. **Row contradicts the entry it cites.** Entry line 1: "the loop's counsels at `:157`/`:159` are recorded, not
   admitted". The row's action cell quotes both: `"descriptions tend to grow during optimization"` is `:159`
   (loop step 3, "Revise the description"), `"Avoid adding specific keywords from failed queries"` is `:157`
   (same step). Both sit under `## The optimization loop` (`:149`–`:163`), whose premise is a run eval set with
   failed queries; neither is under `## Writing effective descriptions` (`:21`–`:28`). A reader following the
   row gets eval-loop advice labelled as description-writing guidance, and the entry's Limits ("eval-fidelity
   held") say the opposite. Two of the row's three fragments therefore rest on admitted-by-the-row,
   not-admitted-by-the-entry content.
2. **Duplicate home (Compression rule: one authoritative home per fact).** "Re-check length" restates the 1024
   limit that SKILL.md already homes at line 162 (Portability floor) and in § Description thresholds by client
   (lines 172–176). The page's own wording is "Check that the description stays under the 1024-character limit"
   — the number is the spec's, not a S213-new rule. The overfitting counsel is the page's train/validation
   protocol, which line 193 and `skill-eval-artefacts-round70.md` already carry (S210/S213 § Avoiding
   overfitting, § The optimization loop).
3. **Rule fusion.** Row rule cell "an imperative about the goal, not the mechanics, and err pushy" merges `:25`
   (imperative phrasing: "Use this skill when..." — about *when to act*), `:26` (user intent, not
   implementation) and `:27` (pushy). "Imperative about the goal" is a hybrid the page never states: the page's
   imperative is a trigger condition, the page's goal/mechanics split is a different bullet. The six existing
   rows are one rule each, and S223/S224/S225 each get two rows — the row breaks the house one-rule-per-row
   shape (447 chars/65 words vs the neighbours' 150–260 chars).
4. **Front-loading trap avoided in the draft but a risk in the fix.** The page has 0 hits for `front-load`,
   `front load`, `use case`, `lead with`, `starts with`, `first sentence`, `self-contained` (grep -c -i -F, all 0
   on the verified bytes) and its worked example (`:184`–`:189`) puts `Use this skill when` in the second
   sentence. SKILL.md already carries front-loading advice, but sourced to other clients (lines 172–173), not
   S213. Any rewrite must not say "open with"/"lead with"; that is the overreach to watch for.

## Verdict per rule

### The draft § Body craft row (3 rules in one)

| rule in the draft row | page location | verdict | reason |
|---|---|---|---|
| imperative / goal-not-mechanics (rule cell only; no quote) | `:25`, `:26` | **fused / garbled** | two bullets read as one; "imperative about the goal" is not on the page; the imperative's content (when to act) is dropped from the action cell entirely |
| `"Err on the side of being pushy"`: list the contexts the skill serves, including ones the user never names | `:27` | **faithful** | page: "Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly"; fragment verbatim (bold-wrapped on the page, so substring match only) |
| `"descriptions tend to grow during optimization"` → "re-check length after each edit" | `:159` | **overreach (scope) + duplicate** | eval-loop counsel, not a writing principle; "after each edit" is the row's gloss — the page says check the 1024 limit in the revise step; the 1024 fact has a home at SKILL.md:162 |
| `"Avoid adding specific keywords from failed queries"` → "name the category instead" | `:157` | **overreach (scope)** | verbatim and paraphrase accurate ("find the general category or concept those queries represent"), but it is overfitting counsel conditional on failed eval queries, which the entry records, not admits; line 193 homes the overfitting protocol |
| row length (447 chars) | — | **house-style break** | six sibling rows are single-rule, ~150–260 chars |

### The entry's rule table (five rows)

| entry row | page location | verdict | reason |
|---|---|---|---|
| 1 instruction to act; quote "Frame the description as an instruction to the agent"; token `Use imperative phrasing` | `:25` | **faithful** | quote and token are substrings; action "tells the agent when to reach for the skill, so the reader decides whether to act" restates "The agent is deciding whether to act, so tell it when to act" |
| 2 user's goal, not internals; quote "Describe what the user is trying to achieve, not the skill's internal mechanics." | `:26` | **faithful with one gloss** | quote verbatim; action's "keep file names, sections and tooling out of the matching surface" is the entry's extrapolation of "internal mechanics" — the page names no files/sections/tooling. Soften or mark as the lane's reading |
| 3 over-inclusion; quote "Err on the side of being pushy" | `:27` | **overreach in the action cell** | "even when the list looks redundant: a missed context costs the whole skill" is not on the page (page: pushy = "Explicitly list contexts where the skill applies") |
| 4 contexts where the user never says the domain word; quote "Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly" | `:27` | **faithful quote, double-counted rule** | same bullet as row 3; rows 3 and 4 are one page rule split in two, which inflates the "four principles" count to five rows. Action's "paraphrases, task words, symptoms" is the lane's gloss, not the page's |
| 5 short; quote "A few sentences to a short paragraph is usually right" | `:28` | **quote faithful, action overreach** | "a description that needs the full character allowance is a finding, not a fit" is not on the page: the page gives the sentence guidance with "usually" and separately a 1024 hard limit; it never ties the two |
| audit verdict "short (`:28`) **not met** — 1022 characters in 7 sentences" | `:28` | **overstated** | 7 sentences is arguably a "short paragraph"; the page's soft "usually right" does not support a hard "not met". Use "stretched / at the ceiling" or drop the verdict; the 1022-vs-1024 row already carries the number |
| "What this entry does not claim" (no front-loading, example puts imperative clause second) | `:184`–`:188` | **faithful, range off by one** | grep confirms 0 hits; the worked example is `:184`–`:189` (line 189 carries `explicitly mention "CSV" or "analysis."`); `:192` reading is correct |

## Corrected wording

Three rows, one rule each, page-faithful; no eval-loop content, no 1024 restatement, no front-loading. The
entry path appears once (row 1, which alone carries ≥2 located fragments, so conjunct (c) is met); rows 2–3 use the
house source cell `S213 optimizing-descriptions`. Drop the `:157`/`:159` rules altogether (they are already
"recorded, not admitted" in the entry; they stay there).

```text
| frame the description as an instruction that says when to act | S213 optimizing-descriptions; `corpus/knowledge/description-craft-round76.md` | "Frame the description as an instruction to the agent": write `Use this skill when...`, not `This skill does...`, because the agent is deciding whether to act. |
| describe what the user wants to achieve, not the skill's internals | S213 optimizing-descriptions | Word the description in the task the user states, not in the skill's file names, sections or tooling, because the agent matches against what the user asked for. |
| err on the side of being pushy | S213 optimizing-descriptions | List the contexts the skill applies to, including phrasings where the user never names the domain, as in `even if they don't explicitly mention "CSV" or "analysis."` |
```

Checked with the counter's own helpers (`quote_spans`, `backtick_spans`, `words`, whitespace-collapsed substring
against the verified page bytes), scratch script only, no repo write: row 1 yields three located fragments
(`Frame the description as an instruction to the agent` 9 words, `Use this skill when...` 4, `This skill does...` 3) ≥
MIN_FRAGMENTS 2 / MIN_FRAGMENT_WORDS 3; the draft row yields three (7/6/7 words) too, so the counter cannot tell the
two apart — the difference is faithfulness, not the count. Row 3's inline example is a located 9-word span (page `:27`).
Row 2 holds no quote on purpose: the page sentence is `:26`, already the entry's quote, and rows 2–3 need none for
the counter. Row 2's "file names, sections or tooling" is the lane's reading: if the L1 wants strict
restating, use "Word the description in the task the user states, not in how the skill works inside" ("internal
mechanics", `:26`).

Row 4 (short, `:28`) is deliberately not added: the 1024 number is homed at SKILL.md:162, and "a few sentences to a
short paragraph" is a soft "usually right" that the lane's own description does not clearly violate. If the L1 wants
it, `| keep it concise | S213 optimizing-descriptions | A few sentences to a short paragraph is usually right; the hard limit is 1024 characters (§ Frontmatter craft). |` points to the existing home rather than
restating it (+1 line → 596).

## Knock-on edits for the patch

- Line budget: 590 + 3 rows + 2 registry rows = **595** (margin 5; with the optional 4th row 596). Anchors move
  accordingly (rule rows 217–219, registry rows ≈516–517; re-measure after applying).
- Registry row text for `check_desc_craft.py` ("SKILL.md § Body craft carries a row citing the entry and S213 with
  ≥2 quote fragments") stays true unchanged.
- Entry: delete the unsupported clauses in rows 3, 5 (and soften 2 and 4's glosses), merge rows 3 and 4 or state
  that both are `:27`, change `:184`–`:188` to `:184`–`:189`, relabel the 5th audit verdict. These are entry text
  edits; they do not touch the frozen counters (the counter reads the quote/location cells, not the action cells —
  checked in the docstring's conjunct (b); this seat did not run the counter on a modified entry, so re-run it in the
  scratch clone after the edit).

## Not checked

The measured audit numbers (1022 / 151 / 7 sentences) and the description-as-declarative verdicts were taken from
the draft, not recomputed here; the full counter was not run (this seat reads and writes no lane tree).

Tooling: none installed. Scratch dir `/fast/scratch/hyaku/kotoba-r77/C04CritRowFaithful/` held one helper script and was removed before yield.

VERDICT: draft row unfaithful — fuses rules :25/:26/:27, admits eval-loop counsels :157/:159 the entry itself says are not admitted, duplicates the 1024 home; replace with the three single-rule rows above (counter conjunct (c) still met)
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/C04CritRowFaithful.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/C04CritRowFaithful.md
