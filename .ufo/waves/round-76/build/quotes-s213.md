# S213 located quotes — description-craft rules (round 76, seat B04QuotesScribe)

Status: DRAFT (pre-freeze). Counters freeze before data; this file is build input for
`corpus/knowledge/description-craft-round76.md` (B12), `SKILL.md` § Body craft (B13) and
`verifiers/check_desc_craft.py` conjunct (b) (B06). It is not itself a claim artifact.

## Provenance

- URL: https://agentskills.io/skill-creation/optimizing-descriptions.md
- S213 row: `corpus/SOURCES.md` (kotoba lane), same page opened in round 75, re-opened this round.
- Fetch: `curl -sS -L` at 2026-10-27T16:5xZ (UTC), HTTP 200, `content-type: text/markdown; charset=utf-8`.
- Bytes: 13403, lines 196, sha256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`.
- Snapshot named by this seat: `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` — byte-identical
  to the fetch above (`cmp` clean, same sha256), landed by B03SnapshotFetch at 13:57 local.
  Line numbers below are line numbers of **those bytes**; any snapshot with the same digest has the
  same line numbers.
- Page-uniqueness baselines (same fetch, same method):
  - `.ufo/waves/round-76/snapshots/evaluating-skills.md` — 16973 bytes, 300 lines,
    sha256 `a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684`.
  - `.ufo/waves/round-76/snapshots/best-practices.md` — 15060 bytes, 277 lines,
    sha256 `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41`.

## Method (so a counter can recompute it)

1. Load the three snapshot files as UTF-8 text; keep `\n` line numbering.
2. First heading of the page = line 5 (`# Optimizing skill descriptions`); lines 1–3 are the
   agentskills.io "Documentation Index" site-chrome block (`> ## Documentation Index`, llms.txt
   pointer, "Use this file to discover…"). A quote qualifies only if its line > 5 and it does not
   occur in lines 1–3 (`chrome_hit` column).
3. Word count = `len(quote.split())` (whitespace split; em dashes count as tokens), must be ≤ 25.
4. Page-unique = exact-substring `in` test against both baseline files (whole body, chrome included),
   plus exactly one occurrence in the optimizing-descriptions body.
5. All 13 quotes below were asserted in the snapshot bytes before this file was written; each row
   records the nearest preceding `#` heading.

## Quotes

| # | Rule | Line | Heading it sits under | Words | Quote | In evaluating-skills | In best-practices |
|---|---|---|---|---|---|---|---|
| 1 | imperative phrasing | 25 | L21 `## Writing effective descriptions` | 3 | `Use imperative phrasing.` | no | no |
| 2 | imperative phrasing | 25 | L21 `## Writing effective descriptions` | 18 | `Frame the description as an instruction to the agent: "Use this skill when..." rather than "This skill does..."` | no | no |
| 3 | user intent, not implementation | 26 | L21 `## Writing effective descriptions` | 13 | `Describe what the user is trying to achieve, not the skill's internal mechanics.` | no | no |
| 4 | pushy / breadth | 27 | L21 `## Writing effective descriptions` | 7 | `Err on the side of being pushy` | no | no |
| 5 | pushy / breadth | 27 | L21 `## Writing effective descriptions` | 17 | `Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly` | no | no |
| 6 | trigger-surface burden | 17 | L13 `## How skill triggering works` | 10 | `This means the description carries the entire burden of triggering.` | no | no |
| 7 | trigger-surface coverage | 45 | L43 `### Should-trigger queries` | 9 | `These test whether the description captures the skill's scope.` | no | no |
| 8 | trigger-surface coverage | 155 | L149 `## The optimization loop` | 23 | `If should-trigger queries are failing, the description may be too narrow. Broaden the scope or add context about when the skill is useful.` | no | no |
| 9 | length | 28 | L21 `## Writing effective descriptions` | 10 | `A few sentences to a short paragraph is usually right` | no | no |
| 10 | length | 28 | L21 `## Writing effective descriptions` | 19 | `long enough to cover the skill's scope, short enough that it doesn't bloat the agent's context across many skills` | no | no |
| 11 | length (hard ceiling) | 28 | L21 `## Writing effective descriptions` | 7 | `enforces a hard limit of 1024 characters.` | no | no |
| 12 | length (growth warning) | 159 | L149 `## The optimization loop` | 16 | `Check that the description stays under the 1024-character limit — descriptions tend to grow during optimization.` | no | no |
| 13 | anti-overfit | 157 | L149 `## The optimization loop` | 7 | `Avoid adding specific keywords from failed queries` | no | no |

Every row: `occurrences` in the optimizing-descriptions body = 1, `after_first_heading` = true,
`chrome_hit` = false (verified; JSON below).

## Requested rules the page does NOT state (calibration finding)

The seat brief asked for quotes on five rule families. Three are sourced above; two are **absent**
from this page and must not be attributed to S213:

- **front-loading the use case — ABSENT.** `grep -in` over the snapshot for `front-load`, `front load`,
  `use case`, `lead with`, `starts with`, `opening`, `single sentence`, `one-sentence` → 0 hits.
  The only `front` hits are `frontmatter` (lines 9, 173).
- **self-contained first sentence — ABSENT.** `grep -in` for `first sentence`, `self-contained`,
  `self contained` → 0 hits.

What the page shows *by example* instead, and what a counter can check: the worked "After"
frontmatter (lines 179–190) opens with capability clauses (`Analyze CSV and tabular data files — …`)
and puts the imperative trigger clause **second** (`Use this skill when the user has a CSV, TSV, or
Excel file …`). Line 192 then explains the change as *more specific about what the skill does* and
*broader about when it applies*. So S213's enforceable content is: imperative trigger phrasing
somewhere in the description, breadth of trigger contexts, short length, ≤1024 characters — not a
"front-loaded use case" or a "self-contained first sentence" rule. Entry/draft wording that claims
those two rules would be an unsourced upgrade and should be struck or marked `[INFERENCE]`.

## Consumable JSON (machine-checkable copy of the table)

```json
[
 {"rule":"imperative-phrasing","quote":"Use imperative phrasing.","words":3,"line":25,"heading":"L21 ## Writing effective descriptions","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"imperative-phrasing","quote":"Frame the description as an instruction to the agent: \"Use this skill when...\" rather than \"This skill does...\"","words":18,"line":25,"heading":"L21 ## Writing effective descriptions","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"user-intent","quote":"Describe what the user is trying to achieve, not the skill's internal mechanics.","words":13,"line":26,"heading":"L21 ## Writing effective descriptions","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"pushy","quote":"Err on the side of being pushy","words":7,"line":27,"heading":"L21 ## Writing effective descriptions","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"pushy","quote":"Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly","words":17,"line":27,"heading":"L21 ## Writing effective descriptions","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"trigger-surface","quote":"This means the description carries the entire burden of triggering.","words":10,"line":17,"heading":"L13 ## How skill triggering works","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"trigger-surface","quote":"These test whether the description captures the skill's scope.","words":9,"line":45,"heading":"L43 ### Should-trigger queries","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"trigger-surface","quote":"If should-trigger queries are failing, the description may be too narrow. Broaden the scope or add context about when the skill is useful.","words":23,"line":155,"heading":"L149 ## The optimization loop","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"length","quote":"A few sentences to a short paragraph is usually right","words":10,"line":28,"heading":"L21 ## Writing effective descriptions","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"length","quote":"long enough to cover the skill's scope, short enough that it doesn't bloat the agent's context across many skills","words":19,"line":28,"heading":"L21 ## Writing effective descriptions","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"length","quote":"enforces a hard limit of 1024 characters.","words":7,"line":28,"heading":"L21 ## Writing effective descriptions","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"length","quote":"Check that the description stays under the 1024-character limit — descriptions tend to grow during optimization.","words":16,"line":159,"heading":"L149 ## The optimization loop","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false},
 {"rule":"anti-overfit","quote":"Avoid adding specific keywords from failed queries","words":7,"line":157,"heading":"L149 ## The optimization loop","occurrences":1,"in_evaluating":false,"in_best_practices":false,"after_first_heading":true,"chrome_hit":false}
]
```

## Suggested minimum for conjunct (b) (≥4 quotes, ≤25 words, page-unique, after first heading)

Any four from the table satisfy (b). The four with the most claim coverage: #2 (imperative),
#8 (trigger-surface breadth), #10 (length), #13 (anti-overfit). For the SKILL.md row (c), fragments
`Use imperative phrasing`, `captures the skill's scope` and `A few sentences to a short paragraph`
are all substrings of the snapshot (the last with its exact capitalisation, line 28), so (c)'s
"at least two quote fragments" is satisfiable without touching the entry's quote set.

## Limits

- These are **documentary** quotes from a markdown snapshot; no agent client was run, so no
  claim about measured trigger rates follows from them (eval-fidelity stays held per plan C1, and
  the round-75 Gate hold is untouched by this file).
- The chrome check is against (i) the two other page snapshots' full bodies and (ii) this page's
  3-line docs-index block. The rendered-site navigation chrome was not fetched (no HTML fetch this
  round), so a quote appearing only in a rendered nav sidebar cannot be excluded this way; none of
  the 13 quotes is boilerplate in the two sibling .md bodies, which is the check the contract names.
- At the time this seat started, `.ufo/waves/round-76/snapshots/` did not exist; this seat fetched
  the three pages itself (`curl`, HTTP 200 each) and re-ran the whole check against B03's snapshot
  bytes once they landed. `snapshots/MANIFEST.sha256` and `snapshots/fetch-record.json` were absent
  at 13:59 when this file was first written; both landed by 14:00 and re-verify here:
  `sha256sum -c MANIFEST.sha256` → all three `OK`, exit 0, digests equal to the three recorded above;
  `fetch-record.json` → three `http_status: 200` records with the same digests and byte counts. The
  in-counter digest table of conjunct (a) is B06's to add.
