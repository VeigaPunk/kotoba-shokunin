source: S213 — Agent Skills — Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions.md — § How skill triggering works (`optimizing-descriptions.md:13`, the caution at `:19`), § Writing effective descriptions (`:21`–`:28`); the loop's counsels at `:157`/`:159` are recorded, not admitted — located quote "An under-specified description means the skill won't trigger when it should; an over-broad description means it triggers when it shouldn't." (`:9`, 20 words)
verified-at: 2026-10-27
recheck: 90d — from the lane root, `for t in 'under-specified description' 'Frame the description as an instruction' "not the skill's internal mechanics" 'Err on the side of being pushy' "doesn't name the domain directly" "even if they don't explicitly mention" 'A few sentences to a short paragraph' 'hard limit of 1024 characters' 'typically only consult skills'; do printf '%s\t%s\n' "$t" "$(grep -c -F -- "$t" .ufo/waves/round-76/snapshots/optimizing-descriptions.md)"; done` prints nine counts, `1` for each, on 2026-10-27; any 0 means the page moved or the fetch failed, which is a re-open of the page and never a silent pass
ground: the lane held S213 for the page's eval protocol only — its anchor is the "Running multiple times" subsection, its `used-by` is `corpus/knowledge/skill-eval-artefacts-round70.md`, and no entry carried the page's writing principles; at base `b7f13f4` a phrase sweep of `SKILL.md corpus/knowledge/*.md corpus/QUALITY.md` for five rule phrasings (`imperative phrasing`, `err on the side of being pushy`, `few sentences to a short paragraph`, `hard limit of 1024`, `burden of triggering`) matched 0 files.

# Writing a skill's `description`: the specification's own rules, and this lane's description measured against them

§ Writing effective descriptions is four principles for the field that decides whether a skill is read at
all (`:17`). What the lane did not hold is the writing itself: the rules at `:25`–`:28`, admitted here at the
guide-advice level round 74 used for the same guides' body advice and turned on this lane's own `description`.

Each quote below is a literal substring of one line of `.ufo/waves/round-76/snapshots/optimizing-descriptions.md`
(13,403 bytes, 196 lines, sha256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, HTTP 200 per
`snapshots/fetch-record.json`): no join across lines, no dropped bytes, whitespace-collapsed comparison only, and
each also occurs in neither `evaluating-skills.md` (`a799805f…fb684`) nor `best-practices.md` (`ab9f3b60…fb41`),
so each is page-unique, not site chrome.

| page | S id | rule | quote | location | tokens | action |
|---|---|---|---|---|---|---|
| optimizing-descriptions | S213 | phrase the description as an instruction to act | "Frame the description as an instruction to the agent" | `optimizing-descriptions.md:25` | `Use imperative phrasing` | carry a clause that tells the agent when to reach for the skill, so the reader decides whether to act |
| optimizing-descriptions | S213 | describe the user's goal, not the skill's internals | "Describe what the user is trying to achieve, not the skill's internal mechanics." | `optimizing-descriptions.md:26` | `Focus on user intent, not implementation` | word it in the task vocabulary a user brings and keep file names, sections and tooling out of the matching surface |
| optimizing-descriptions | S213 | err toward over-inclusion of contexts | "Err on the side of being pushy" | `optimizing-descriptions.md:27` | `Err on the side of being pushy` | list the situations the skill covers even when the list looks redundant: a missed context costs the whole skill |
| optimizing-descriptions | S213 | name the contexts where the user never says the domain word | "Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly" | `optimizing-descriptions.md:27` | `Explicitly list contexts where the skill applies` | add the phrasings a user types without the artifact nouns — paraphrases, task words, symptoms — beside the exact terms |
| optimizing-descriptions | S213 | keep it short: a few sentences, not a page | "A few sentences to a short paragraph is usually right" | `optimizing-descriptions.md:28` | `Keep it concise` | budget by sentences; a description that needs the full character allowance is a finding, not a fit |

## This lane's own `description`, measured

The measured field is the YAML folded-scalar render of the `description:` block of `SKILL.md` — frontmatter
lines 4–18 (15 lines) rendering as one string — not a physical-line count. Measured at base `b7f13f4`, the description
block being outside this round's touch list, so the counter's recomputation at the measured tip governs.

| measured field | value | how measured (and recomputed by `verifiers/check_desc_craft.py` conjunct (d)) |
|---|---|---|
| rendered `description` length (characters) | 1022 | the block's clip-preserving YAML render — `len()` of the parsed value, the folded block's terminal newline kept (the stripped variant is 1021) |
| first sentence length (characters) | 151 | the same render to the first `. ` boundary, period included (150 without it) |

| rule | verdict | what the description shows |
|---|---|---|
| imperative phrasing (`:25`) | **not met** | sentence 1 (151 characters) is declarative — "Prompt & skill craft — audits, writes, and rewrites `SKILL.md` / `AGENTS.md` / dispatch prompts / system prompts …" — and no clause anywhere is an instruction to act; `Triggers:` lists conditions as noun phrases, not as the page's imperative form |
| user intent, not mechanics (`:26`) | **partial** | "for trigger fidelity and decision density" names the outcome, but the object list (`SKILL.md` / `AGENTS.md` / dispatch prompts / system prompts) is the internal mechanics the page keeps out of the surface |
| pushy (`:27`) | **met** | 8 quoted trigger phrases, 108 characters of quoted span, plus 3 anti-trigger categories: characters spent on breadth, not on trusting the domain word |
| unnamed-domain contexts (`:27`) | **partial** | 2 of the 8 phrases (`trigger words`, `prompt craft`) avoid the artifact nouns; there is no clause of the page's "even if they don't explicitly mention" kind |
| short (`:28`) | **not met** | 1022 characters in 7 sentences, against *A few sentences to a short paragraph*: at the ceiling, not under it |
| the 1,024 ceiling (`:28`) | **met, at the edge** | "enforces a hard limit of 1024 characters." — 2 characters of headroom: any added phrase, or any edit that lengthens a line, breaks the limit |

Findings a reader can act on:

- **The imperative gap is the page's first rule and the description's clearest miss.** The repair converts
  sentence 1's opening into a trigger clause, and the render only stays legal if something else is cut first.
- **The cheapest cut is sentence 7** — `Note: shokunin files sit outside the omp discovery roots, so omp never
  reads this text.` (87 characters): a deployment fact, not a trigger statement, and already a body rule in
  `corpus/knowledge/frontmatter-trigger-surface.md:153`–`:154` ("`description` craft is audit-hygiene, not
  routing surface").
- **This round does not rewrite the description**, because C2's R1 pins the render at 1022 at the measured tip
  and an edit here would move the number that receipt is checked against; the repair routes forward with the
  two findings above as its brief.

## What this entry does not claim (Q62)

- **No front-loading rule, no self-contained-first-sentence rule.** The page states neither — a sweep for
  `front-load`, `front load`, `use case`, `lead with`, `starts with`, `first sentence`, `self-contained`
  returns 0 hits — and its worked example (`:184`–`:188`) puts the imperative trigger clause second, reading
  the improvement at `:192` as more specific about what the skill does and broader about when it applies.
- **The 1,024 number is the specification's authoring limit, not a client render cut.** Which client cuts or
  budgets a listing, and at what number, is `skill-listing-thresholds-round54.md`'s subject (`:15`–`:16`), and
  is counted there by `verifiers/check_description_thresholds.py`.
- **The page's eval protocol is recorded, not admitted.** It is already cited by S213's row and counted in
  `corpus/knowledge/skill-eval-artefacts-round70.md`; holding it is scope by assignment, not absence, because
  whether a measured trigger rate predicts triggering is an eval-fidelity claim.

## Limits

- **Documentary evidence, no client run, eval-fidelity held.** Every rule is a sentence of a pinned markdown
  snapshot; no agent client was installed, prompted or observed, and no trigger rate, pass rate or overfit
  measurement is reported. The page's own caution bounds it — agents "typically only consult skills for tasks
  that require knowledge or capabilities beyond what they can handle alone" (`:19`) — so a matching description
  can still go unused.
- **The audit rows are reads of a string, not of a router.** `verdict` compares rendered text to quoted rules
  at a named revision; whether the description would trigger, and whether these are the right rules, is
  judgement assigned to non-author seats — `A01RevQuoteLocate` (location, word count, page-uniqueness),
  `A17CritAudit` (verdict support in the page's own text), `A13CritHollowC1` (whether a restatement world can
  satisfy the counter without the page) — and to the round closure, never to this entry's author.
- **The convention is contested inside the lane, and the round names it.** `check_sibling_census.py`
  `description_of` and `verify_harness_claims.py`'s `len(re.sub(r"\s+", " ", desc).strip())` report 1021 for these
  bytes; the claim's counters take the clip-preserving parse (1022, terminal newline kept), so the two are not
  interchangeable and the headroom under the other convention is 3 characters.
- **Line numbers are the snapshot's, not the live page's.** The URL can change under a fixed digest; the
  recheck line counts tokens, and a 0 there is a re-open of the page.

## Related

- `corpus/knowledge/spec-skill-creation-craft-round74.md` — the body half of the same guides; this is the field's half.
- `corpus/knowledge/frontmatter-trigger-surface.md` — the router's matching surface; its §11 pairing of a noun with imperative-context triggers came from measurement, a different evidence class from this page's advice, and its §12 is why a file outside a discovery root makes this audit hygiene rather than routing.
- `corpus/knowledge/render-mechanism-round7.md` — omp's first-sentence render and compression path, which does not reach a file outside a discovery root.
- `corpus/knowledge/frontmatter-rule-authorities-round48.md` — the 1,024 authority and the validator constant behind it.

<!-- build note — seat B12EntryDraft, round 76, pre-freeze draft. Landed copy is
corpus/knowledge/description-craft-round76.md. Strip this comment on landing. -->
