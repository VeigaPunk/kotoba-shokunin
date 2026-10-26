# R75Facet59 — `SKILL.md:166` description-threshold headline vs its cited counter

Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe` (worktree clean except untracked
`.ufo/waves/round-75/`). Read-only: no fetch, no client run, no edit outside this report.

## Observation (committed bytes)

`SKILL.md:166` is a standalone rule sentence above the table at `SKILL.md:164-177`:

> A documented maximum is not a render cut: four clients state 1,024 and none documents a cut there,
> Claude Code and Codex cut or budget the listing, omp cuts at 99 (§ Router model). Basis:
> `corpus/knowledge/skill-listing-thresholds-round54.md` (S053–S059, S062–S064), checked by
> `verifiers/check_description_thresholds.py`.

Its four clauses are sourced in the entry: "four clients document 1,024" and "None of their pages documents a
cut at that number" at `corpus/knowledge/skill-listing-thresholds-round54.md:15-19`; the cut/budget pair at
`:20-27`; omp at `:32-34`. At HEAD the count is true by direct measurement of the table: exactly four rows
carry a `1024` token in the documented-threshold cell — VS Code `SKILL.md:172`, Copilot CLI `:173`, Cursor
`:175`, opencode `:176` (Claude Code `:170` = 1,536/budget; Codex `:171` = 2%/8,000; Gemini `:174` = ~100 words).
An in-memory parse of the table returned `count rows with 1024 token: 4`.

The cited counter (`verifiers/check_description_thresholds.py`) at this revision:

- prints `description thresholds backed 7 of 7 clients`, exit 0, with `--rev 65a5c7a…`;
- `--self-test` prints `self-test: 0 failure(s) over 26 assertions`, exit 0;
- has `TARGET = 4` (`:83`) and seven pinned `CLIENTS` (`:86-87`); `TARGET` is a floor over backed rows,
  declared `4 of 7` in the historical plan (`plans/round-54.md:26`), not a count of clients stating 1,024;
- in `judge()` reads only the threshold cell's number tokens (`:281`) and the action cell's non-emptiness
  (`:284`); the "past the threshold" cell (column 3, where "none documents a cut" lives) is never read, and
  the sentence is never parsed;
- disclaims the reading itself: "The counter does not judge whether the number is a render cut, a budget or
  an authoring maximum" (`:46-48`).

Falsifiability probe (in-memory mutants of the committed text, no repo write; scratch
`/fast/scratch/hyaku/kotoba-r75/R75Facet59/probe.py`):

| mutant | counter verdict |
|---|---|
| `four clients` → `five clients` | `7` backed (unchanged) |
| VS Code past-cell → `Truncated past 1024 characters` | `7` backed (unchanged) |
| `omp cuts at 99` → `omp cuts at 100` | `7` backed (unchanged) |
| Cursor threshold `1,024` → `2,048` | `6` backed (only because the entry quote no longer holds the number token) |

So the counter has no clause-level falsifier for "four", "none documents a cut", or "omp … 99"; only row
presence and quote/number-token equality are measured.

Two further committed facts bear on the same sentence:

- **Pointer staleness.** `(§ Router model)` lands on `SKILL.md:153-156`, which now only says the body moved
  to `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Router model (round 72). The moved
  table at `corpus/knowledge/anatomy-and-compression.md:211` states the "hard 99-char cliff"; the in-file
  mechanism paragraph is `SKILL.md:26-30` (`slice(0, _8n-1)`, `_8n=100`). The cited parenthetical is a
  redirect, not the evidence.
- **Boundary ambiguity 99 vs 100.** The omp guard models `CLIFF = 100` and returns inputs `<= CLIFF`
  unchanged (`verifiers/verify_harness_claims.py:73,240,242`); its vectors are 99→99 and exactly-100→100
  (`:591-592`). So a description of exactly 100 characters is *not* cut; the 99-character figure is the
  retained length after a cut, and the trigger is ">100". "omp cuts at 99" is true of the retained length,
  not of the boundary input.
- **Scope of "four".** `SKILL.md:176` itself scopes opencode to "v1 docs page; the v2 page says it enforces
  no maximum" (entry `:17-19`, S064), so the present-tense headline rests one of its four on a superseded
  page. Also `Codex CLI`'s shipped parser cuts at 1,024 from source (entry `:26-27`) — a fifth 1,024 in the
  corpus, documented as source-read, not as a documented maximum.

## Assessment

Depth is real: each clause has an entry row, a located quote, a tier-A `mined` row and a Gate record, and
the four-client count checks out at HEAD. The weakness is calibration, not support (Q26/Q31): the sentence
says "checked by" the counter, but the counter measures none of its distinguishing clauses, and its printed
`backed 7 of 7` (floor 4) reads as a stronger statement about 1,024 than it is. The numeric collision
`TARGET = 4` vs "four clients" makes the conflation easy for a round-75 description audit that reuses this
gate. The 99/100 boundary and the opencode v1/v2 scope are the two places where an audit keyed on this
sentence would mispredict a render.

Inference (not measured): a reader who treats "backed 7 of 7" as "seven clients document 1,024" would be
wrong on three of the seven rows; the sentence gives no counter output that separates the two numbers.

## Concrete check/control

Two operable options; neither edits the frozen round-54 counter (Q28, Q73 — a successor is a second
measurement).

**(a) Clause counter, frozen before data** — `verifiers/check_description_thresholds_clauses.py --rev <rev>`:
- print `threshold rows stating 1024: N of 7`; require `N == 4` (measured 4 at HEAD);
- print the four "past the threshold" cells verbatim and `rows whose past-cell states a cut: N`; the
  judgment is assigned to named non-author seats, because a lexical sweep over the four committed cells
  matches the *denial* sentences 4/4 (probe: VS Code `drop, refusal, truncation, warning`; Cursor
  `cut, warned, warning`), i.e. a substring/`cut|truncat|refus` check over-flags every honest row (Q20/Q23:
  "stricter/looser is a measured direction");
- print `omp: trigger >100, retained <=99` read from the committed guard's vectors, not from prose;
- print `source page current: opencode v1` (or the v2 substitution) so "four clients state 1,024" carries
  its scope in the output.

Must-fail arms (expected verdicts): add a fifth 1024 row → `5 of 7`, exit 1; change one past-cell to an
affirmative cut ("Truncated past 1024 characters") → reviewer red with the cell printed, and the mechanical
arm only if its false-positive rate on the four honest cells is recorded as 4/4 and handled by negation;
change the omp constant 100→101 → the harness vectors red; run at the round-54 base (before the table) →
`0 of 4`, exit 1 (do-nothing control).

**(b) Bound the sentence instead** (no new code): replace "checked by `verifiers/check_description_thresholds.py`"
with "row presence and quote/number-token equality checked by `verifiers/check_description_thresholds.py`;
the 1,024/no-cut and omp readings are the entry's and a reviewer's". This satisfies Q26 by dropping the
clauses the counter does not turn on, and Q31 by naming the cells the code reads.

Either option should also (i) point the omp clause at the moved section line or `SKILL.md:26-30` rather than
the redirect, and (ii) state "trigger >100, retained ≤99" so a description audit's boundary case is fixed.

## Risks and limits

- No frozen round-75 claim exists here: `plans/round-74.md` is historical (its C1/C2 are not this facet),
  and `TARGET = 4` is round 54's plan value. This report is a candidate, not a verdict on the lane.
- The counter's `--fetch` path was not exercised (no live fetch allowed); all statements are about
  committed bytes at `65a5c7a`.
- The omp boundary rests on the lane's source-read model in `verify_harness_claims.py`, not a client run;
  the entry itself records "no client was run".
- No sibling round-75 facet reported on `SKILL.md:164-177` at the time of writing (`grep -l` over
  `.ufo/waves/round-75/w1/*.md` for this section/counter returned nothing), so the facet is distinct.

## Report trailer

- `SKILL.md:153-156,164-177,170-176` (sentence, table, 1024 rows; pointer target)
- `corpus/knowledge/skill-listing-thresholds-round54.md:15-34,60-67` (findings 1-4, Limits)
- `corpus/knowledge/anatomy-and-compression.md:201-213` (moved Router model, 99-char cliff at `:211`)
- `verifiers/check_description_thresholds.py:46-48,83,86-87,281,284,368-397` (docstring, target, clients, judge, self-test arms)
- `verifiers/verify_harness_claims.py:73,240,242,591-592` (CLIFF=100; 100→100 vector)
- `plans/round-54.md:26` (historical `4 of 7` target)
- Commands: `python3 -B verifiers/check_description_thresholds.py --rev 65a5c7a…` → `description thresholds backed 7 of 7 clients`, exit 0; `--self-test` → `0 failure(s) over 26 assertions`, exit 0; in-memory probe (four clauses, mutants above) under `/fast/scratch/hyaku/kotoba-r75/R75Facet59/probe.py`.
