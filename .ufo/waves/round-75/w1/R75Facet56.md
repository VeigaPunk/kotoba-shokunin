# R75Facet56 — description-threshold summary sentence (`SKILL.md:166`) and its table

Seat: R75Facet56 (executor, axes calibration + operability). Read-only; no edits, no delegation,
no gate runs, no live fetch. All bytes below are committed bytes at lane HEAD
`65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git -C kotoba-shokunin rev-parse HEAD`);
`git diff --stat -- SKILL.md verifiers/check_description_thresholds.py
corpus/knowledge/skill-listing-thresholds-round54.md corpus/QUALITY.md` is empty (worktree = HEAD
for every file cited here). Only untracked path: `?? .ufo/waves/round-75/` (the wave's own output dir).

## Facet under test (distinct from facets on 3–56, 188–196, 218–229, 237–247)

`SKILL.md:166` — the single summary sentence over `### Description thresholds by client`
(`SKILL.md:164`, table `SKILL.md:168-176`, seven rows), its grounding entry
`corpus/knowledge/skill-listing-thresholds-round54.md`, and the counter it names,
`verifiers/check_description_thresholds.py` (registry row `SKILL.md:464`).

Sentence, verbatim (`git show HEAD:SKILL.md | sed -n '166p'`):

> A documented maximum is not a render cut: four clients state 1,024 and none documents a cut there,
> Claude Code and Codex cut or budget the listing, omp cuts at 99 (§ Router model). Basis:
> `corpus/knowledge/skill-listing-thresholds-round54.md` (S053–S059, S062–S064), checked by
> `verifiers/check_description_thresholds.py`.

Clause decomposition used below: **C-a** "four clients state 1,024"; **C-b** "none documents a cut
there" (a four-client negative); **C-c** "Claude Code and Codex cut or budget the listing";
**C-d** "omp cuts at 99 (§ Router model)"; **C-e** "checked by check_description_thresholds.py".

## Observations (commands and printed values)

| id | command | observed |
|---|---|---|
| O1 | `git show HEAD:SKILL.md \| sed -n '170,176p' \| awk -F'\|' '$3 ~ /1,?024/ {gsub(/^ +| +$/,"",$2); print NR": "$2}'` | `3: VS Code`, `4: Copilot CLI`, `6: Cursor`, `7: opencode` → **4 rows**, so C-a holds on the table as written |
| O2 | `git show HEAD:SKILL.md \| sed -n '170,176p' \| awk -F'\|' '$3 ~ /1,?024/ {print $2" => "$4}'` | VS Code `Not documented: the page states no truncation, drop, warning or refusal past 1024, and no listing budget`; Copilot CLI `Not documented; the page states the cap and no truncation, shortening or refusal`; Cursor `No cut documented; the release notes document a warning: …`; opencode `nothing: no cut, truncation, warning or refusal — …` |
| O3 | `git show HEAD:verifiers/check_description_thresholds.py \| nl -ba \| sed -n '19,48p'` | a client is BACKED iff: one table row names it; header first four cells match; **action cell** (r[3]) non-empty; **threshold cell** (r[1]) holds ≥1 number token; one entry row; `S###` row is 11-cell, tier A, `mined`, opened `2026-10-22`, `used-by` names the entry, pinned host; quote 3–25 words containing one cell number token and recorded in the round-54 Gate. Then, verbatim: "The counter does not judge whether the number is a render cut, a budget or an authoring maximum" (`:46-48`) |
| O4 | `git show HEAD:verifiers/check_description_thresholds.py \| nl -ba \| sed -n '280,285p'` | `sr = smine[0] + [""] * 4`; only `sr[1]` (threshold tokens) and `sr[3]` (action) are read — **`sr[2]`, the "Past the threshold" cell, is never read** |
| O5 | `git show HEAD:verifiers/check_description_thresholds.py` → `:83`, `:86`, `:514`; `grep -c 'documented maximum is not a render cut'` → `0` | `TARGET = 4`; `CLIENTS` has 7 names; `return 0 if value >= TARGET else 1`; the counter never reads `SKILL.md:166`'s sentence — its acceptance rule is the table, not the summary |
| O6 | `git show HEAD:verifiers/check_description_thresholds.py \| nl -ba \| sed -n '189p'` | `if tuple(clean(x) for x in c[:len(header)]) == header:` — header match is a **prefix** match; a fifth column added to either table is silently tolerated |
| O7 | `grep -n 'changelog\|release notes\|source tree\|grep' corpus/knowledge/skill-listing-thresholds-round54.md` | only `:40` (Claude Code: "the changelog records a startup warning") and `:45` (Cursor: quote from `release-notes.md:122`). **No** changelog/release-notes leg, no docs-source-tree leg and no corpus grep for VS Code (S055) or Copilot CLI (S056) |
| O8 | `git show HEAD:SKILL.md \| sed -n '29,30p;153,156p;556,557p'`; `git show HEAD:corpus/knowledge/anatomy-and-compression.md \| grep -n 'Router model\|99'` | omp render = `cache.get(key) ?? previewSkillDescription`, `_8n=100`, `slice(0, _8n-1)`, first-sentence-if-≥40-chars fallback; `## Router model — which harness, which gate` (`SKILL.md:153`) now holds only the pointer to `corpus/knowledge/anatomy-and-compression.md § Moved from SKILL.md § Router model (round 72)` (`:201`), whose omp row (`:211`) reads "cached LLM line, else deterministic truncator … hard 99-char cliff" |
| O9 | `grep -n -A6 'skill-listing-thresholds-round54' corpus/lessons/round-68.md` | `:126-128`: "the 1024-character cap documented in `corpus/knowledge/skill-listing-thresholds-round54.md`: the value is 1,019 characters stripped and 1,020 parsed … against the cap the table documents **for VS Code, Copilot CLI and opencode**" |
| O10 | `git show HEAD:corpus/knowledge/skill-listing-thresholds-round54.md \| nl -ba \| sed -n '15,19p;32,34p;60,67p'` | Finding 1 (`:15-19`) counts the 1,024 set as "VS Code S055, Copilot CLI S056, Cursor S058, opencode S059 as `1-1024`" and asserts "None of their pages documents a cut at that number"; Finding 4 (`:32-34`) says "omp … cuts at offset 99 **unless a cached one-liner exists**"; Limits (`:60-67`) name only the counter's own blind spots |

## Findings

**F1 — C-e overstates the counter (control weakness, Q31 class; `corpus/QUALITY.md:42`).**
The sentence's four payload clauses are exactly what the named counter does not compute.
`check_description_thresholds.py` reads r[0] (client), r[1] (a *number token*), r[3] (action
non-empty) and the entry/`SOURCES`/Gate cells (O3, O4); it never reads the "Past the threshold"
cell where C-b lives, never classifies maximum / cut / budget, and never reads `SKILL.md:166`
(O5). Prose therefore credits a counter with C-a, C-b, C-c and C-d while the counter's own
docstring (`:46-48`) explicitly assigns the classification to "the entry's and the reviewer's".
The entry already carries the honest version (`:60-67`); `SKILL.md:166` does not.
Concrete control (frozen-counter blindness, runnable as a future sandbox arm, not run here):
1. copy the lane to scratch, rewrite `SKILL.md:166` to the opposite reading ("every client
   documents a cut at its number; omp never cuts"), leave table 168–176 untouched, commit, and
   run `python3 -B verifiers/check_description_thresholds.py --rev <scratch rev>`.
   Predicted `description thresholds backed 7 of 7` exit 0 — **[INFERENCE]**, grounded in O3–O5:
   no code path reads that line or the `sr[2]` cell. A green here *proves* the attribution is
   unwarranted; it is the falsifier the sentence needs and does not have.
2. Replacement conjunct for a successor counter: C-a is checkable on committed bytes —
   `count(rows under `### Description thresholds by client` whose 2nd cell matches `1,?024`) == 4`
   (observed 4, O1) — and C-b is checkable on r[2] text: every row counted in (1) must have a
   `Past the threshold` cell containing none of `truncat|shorten|drop|refus` outside a `not`/`no`
   scope, or the claim drops to the three clients that carry a release-note/source leg.
3. Do **not** conflate C-a's 4 with the counter's `TARGET = 4` (`:83`): the target is a floor over
   seven clients and stays green on `4 of 7`, so deleting Cursor's row (→ C-a false) still exits 0.

**F2 — C-b is a four-client negative with no Q30 sweep (calibration; `corpus/QUALITY.md:41`).**
Q30 requires a "documents nothing about Y" negative to name, per client, the vendor changelog or
release notes, the current docs source tree, and a grep of the lane's own corpus. The entry names
the changelog/release-note leg only for Claude Code and Cursor (O7); for **VS Code (S055) and
Copilot CLI (S056)** it names none of the three, yet both rows end in "Not documented … no
truncation, shortening or refusal" (O2). Under Q30 those are "not checked", not "silent", and the
compressed sentence at `SKILL.md:166` converts four page-level absences into one documented
negative. Concrete control: add three sweep columns to the entry's `## Per-client record` (the
frozen counter tolerates extra columns — O6, prefix compare at `:189` — so this is an entry edit,
not a counter edit) with commands per cell, e.g. changelog + docs-tree retrieval recorded in
`FETCH-LOG.tsv`, and `grep -rn 'truncat\|shorten\|1024' SKILL.md corpus/ PROVINCE.md` for the
corpus leg; a successor conjunct requires the three cells non-empty for every client named in the
negative and goes red when one is blank (falsifier: blank S055's three cells → must FAIL).

**F3 — C-d drops its own condition and its in-file anchor is now a stub (scope, operability).**
"omp cuts at 99" is the cache-miss path only: `SKILL.md:29-30` states
`cache.get(key) ?? previewSkillDescription` with the cache-hit branch being an LLM one-liner
(validator ≤160 chars), and the entry's Finding 4 keeps the qualifier
"unless a cached one-liner exists" (`:32-34`) while the moved table row calls it a "hard 99-char
cliff" only after "cached LLM line, else deterministic truncator"
(`corpus/knowledge/anatomy-and-compression.md:211`). Second, `(§ Router model)` (`SKILL.md:166`)
now resolves to a pointer-only section (`SKILL.md:153-156`); the mechanism sits two hops away
(`anatomy-and-compression.md:201,211`; `SKILL.md:29-30,556-557`). For a description audit that
budgets chars, the difference matters: a cache hit renders up to ~160 chars of rewritten text,
not a 99-char prefix. Control: the sentence must carry the condition ("when the description cache
misses") and the moved anchor; mechanical check —
`git show HEAD:SKILL.md | sed -n '166p' | grep -c 'cache'` → 0 today, and the same command against
the entry's Finding 4 → 1.

**F4 — C-a's population disagrees with the lane's own r68 record (calibration, cross-file).**
`SKILL.md:166` says four clients state 1,024 (VS Code, Copilot CLI, Cursor, opencode); the lane's
round-68 lesson says the same table documents the cap "for VS Code, Copilot CLI and opencode"
(`corpus/lessons/round-68.md:126-128`) and the round-67 spot-check repeats the three-client form
(`corpus/lessons/round-67-verifier-spotcheck.md:71`). Both cite
`skill-listing-thresholds-round54.md`; they differ on whether Cursor's release-note warning is a
"statement of the 1,024". A description audit that measures headroom against "the cap" inherits
this 3-vs-4 ambiguity. Control: one count command used by both surfaces —
`git show HEAD:SKILL.md | sed -n '170,176p' | awk -F'|' '$3 ~ /1,?024/ {c++} END{print c}'` → `4`,
plus a one-line note that Cursor's instance is a release-note warning, not an authoring maximum
(the entry's Cursor reading cell already says so, `:45`).

**F5 — minor: the parenthetical `(S053–S059, S062–S064)` is wider than what anything pins.**
The counter validates only the per-client `S###` rows (S053–S059) through the entry's record table;
S062 (Claude CHANGELOG), S063 (Codex config), S064 (opencode V2) are cited in the entry's Findings
(`:20-34`) but no conjunct reads them. `SOURCES.md:75-77` shows all three as 11-cell, tier A,
`docs`, `mined` — so the rows exist; the *use* of them in the sentence is unverified. Control:
either drop them from the `SKILL.md:166` basis pointer or extend the successor counter to require
each of S062–S064 to appear in the entry body verbatim as `S###` (cheap: `grep -c` on the entry).

## Adjacent-facet cross-check (not my facet; recorded so the parent does not re-derive it)

Facet 14 cites `SKILL.md:218-229` and reads the 19-vs-45 denominator as a conflict. Verified here,
independently, that there is no conflict: the trigger-fidelity checklist has 19 boxes
(`git show HEAD:SKILL.md | awk '/^## Trigger-fidelity checklist/,/^## Agent-definition fidelity
checklist/' | grep -c '^- \[ \]'` → 19, of which 8 carry an `(executed:` marker), and the whole
file has 45 boxes across four checklists (19+9+9+8), matching
`verifiers/checklist-baseline.json`'s `box_total: 45` and its section counter
(`Trigger-fidelity 19, Agent-definition 9, Dispatch-prompt 9, Always-on 8`; dispositions
8 executed / 4 delegated / 33 unexecuted). The sentence's "every box in this file" is therefore
true of the 45-box map, and "eight of the nineteen" is true of the trigger section. Reported as
observation only; the paragraph's own assessment belongs to that facet.

## Risks and limits

- No gate, counter, self-test or live fetch was run (wave-in-flight rule; parent owns gates).
  O3–O6 are code reads, not executions; the F1 prediction is labelled `[INFERENCE]`.
- Line numbers are the HEAD revision `65a5c7a6`; they will drift on any later `SKILL.md` edit.
- F2's changelog/docs-tree legs cannot be closed read-only this round (no live fetch); the finding
  is that the sweep is *absent*, which is a committed-bytes fact (O7).
- No tool was installed; nothing was written outside this report; no scratch dir was created.
- Blocker: none.

Report: `.ufo/waves/round-75/w1/R75Facet56.md`
Files changed: none in the lane; this report only.
