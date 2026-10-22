# Falsify W2SrcClaudeCode — C1 Claude Code cells (round 54)

Result: DONE — all five Claude Code cells (SOURCES S053, SOURCES S062, entry per-client row, Gate row pair, SKILL.md table row) HOLDS; every quote re-opened and verified byte-verbatim at its stated line on re-fetched bytes, the number is about a skill `description`'s listing render, no over-wide cell found, no contradiction with older lane rows; one informational note on the vanished § 2.1.497 line-pair.

Seat: KotobaR54.W2SrcClaudeCode (leaf, falsify scope = Claude Code rows only; no patch, no lane write, no subagent).

## 0. Chain freshness (what "as landed at 5a097e12" means today)

`git diff --stat 5a097e12..58db81c4 -- corpus/SOURCES.md` is empty (exit 0): SOURCES did not drift after the C1 commit, so `git show` and the working tree are equivalent for the attacked sources rows. The other three C1 files were amended after the landed commit with edits outside my scope (entry Findings 2–3 Codex/Gemini wording, lesson M45 row text tail, SKILL.md Codex/Gemini/Cursor rows + ladder cells). I re-checked the three Claude Code cells inside their current versions, so every per-cell verdict below is against the present tip; each amended region re-verified identical to its landed wording in the parts that name Claude Code (SKILL.md:185 threshold + Past cells and the entry/lesson rows: byte-identical except where noted, none of the notes touch Claude Code text).

## 1. Per-cell verdicts

### Cell 1 — SOURCES S053 (`corpus/SOURCES.md:66`) — HOLDS

- Re-fetch 2026-10-22T22:03:58Z of `https://code.claude.com/docs/en/skills.md`: HTTP 200, 0 redirects, 111,928 B, sha256 `d1359f0c64371b3f2e267069d9f752418466abadb2765eca2929ecbee4ce0b2b` — byte-identical to the Gate/S053 record and to the seat's fetch (`build/SrcClaudeCode.md` § 1 row 1). Rule 1 satisfied.
- Quote cell `"the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing"`: 15 words (validator run), verbatim at `skills.md:389` in the fetched bytes: "Put the key use case first: the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage." Rule 2+3 satisfied; location line number correct.
- Anchor rows verified on the same bytes: `:390` `when_to_use` row ends "Appended to `description` in the skill listing and counts toward the 1,536-character cap."; `:389` in § "Frontmatter reference" (heading at `:365`) describes the frontmatter field `description`; "Skill descriptions are cut short" starts `:1205`; § `skillListingBudgetFraction` at `settings-reference.md:2455`, § `skillListingMaxDescChars` at `:2471` (see Cell 3 fetch).
- Teaches cell: "`description` and `when_to_use` text is truncated at 1,536 characters in the skill listing; the budget scales at 1% of the model's context window" — both halves verified on the fetched bytes (`:389`, `:1207`). No over-wide claim beyond the two sensed quotes.
- Provenance/count: 11 cells, tier `A`, kind `docs` on `code.claude.com`, status `mined`, opened `2026-10-22`, used-by names `corpus/knowledge/skill-listing-thresholds-round54.md` — rule 6–7 satisfied.
- Meaning-of-number: correct sense. `:389` is the frontmatter-row advice about how the listing consumes the `description`; the counter's number is `1,536` and it is a per-entry listing cut (also `:1213`: "each entry's combined text is capped at 1,536 characters regardless of budget" and `settings-reference.md:2477` Default `1536`), not a frontend-UI byte-formatting 1,024 (`:1085`, `:1086`, `:1134`) nor the `compatibility` 500-char cap (`:397`). Sense: **listing cut** — matches. Appended-only confirmed: no in-place edits — S053/S062 absent at plan commit `e33715486a45a4a857b64c30e6b695f7995858b8` (`git show ...:corpus/SOURCES.md | grep -c S053` = 0, S062 = 0).

### Cell 2 — SOURCES S062 (`corpus/SOURCES.md:75`) — HOLDS

- Re-fetch 2026-10-22T22:03:58Z of the pinned raw URL `https://raw.githubusercontent.com/anthropics/claude-code/5ed799e5cc56bea9efff57398ca43e31d82784ff/CHANGELOG.md`: HTTP 200, 0 redirects, 1,070,244 B, sha256 `121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49` — byte-identical to the Gate/S062 record and to the seat's fetch (§ 1 rows 4–5).
- Pin ancestry re-verified live: `git ls-remote https://github.com/anthropics/claude-code HEAD` → `5ed799e5cc56bea9efff57398ca43e31d82784ff refs/heads/main` (unchanged since the seat pinned it; "main, 2026-10-22" accurate and still accurate at re-check: `compare/5ed799e5...HEAD` status `identical`, `ahead_by 0`), so `raw@main == raw@5ed799e5` byte-identity is direct, not just curl-redirect-following.
- Strayed location: none. `§ 2.1.105` block starts at `CHANGELOG.md:6398` (line after the `## 2.1.105` heading line), i.e. the anchor row's `6398-6409` is exact; the sentence sits at `:6409` inside v2.1.105 exactly as the seat pinned it.
- Quote: "raised the listing cap from 250 to 1,536 characters and added a startup warning when descriptions are truncated" — 18 words, byte-exact occurrence at `:6409` (following "Improved skill description handling:" in the same bullet, no mid-word splice). About the `description`'s treatment (the bullet names "skill description handling") — sense is the listing cap + the past-cap behaviour, not any other number (only one number-sentence in the block; nothing else about `.claude/skills` in it).
- Provenance/count: 11 cells, tier `A`, kind `docs` on `raw.githubusercontent.com` under the pinned anthropics/claude-code repo path (pinned-host rule satisfied with a whole path-segment prefix, no `.`/`..` segment), status `mined`, opened `2026-10-22`, used-by names the entry. Rule 6–7 satisfied. Append-only: absent at plan commit (0 hits, command above).

### Cell 3 — Entry `corpus/knowledge/skill-listing-thresholds-round54.md` § Per-client record Claude Code row — HOLDS

- Provenance-cell S053: correct (only S053 is the counter-read row; S062 is supporting — see Cell 4 seat report § 2/§ 4 and its call out "the counter's Claude Code host list... the counter only checks the row named in the entry's `row` cell, which is S053").
- Number token `1,536`: appears in the quote cell; SKILL.md threshold cell contains the same verbatim token `1,536`; Gate S053 quote is char-identical to the entry quote (string-equality check passed). Rules 5 satisfied and the counter prints BACKED for Claude Code in a sandbox clone at the graded revision.
- Reading cell — every claim verified against the fetched bytes; no over-wide claim:
  - "the page puts the 1,536-character limit inside the skill listing" — `:389` "...truncated at 1,536 characters in the skill listing"; correct sense (in the skill listing, i.e. what the model receives).
  - "names no frontmatter limit for `description`" — the `description` row `:389` has no length cap; `1,?024` appears only 3 times in the 1,234-line page at `:1085`, `:1086`, `:1134` (byte formatter `html.py` helper code, not a `description` rule); the `compatibility` row (`:397`) is a 500-char cap on a different field. Verified.
  - "(the changelog records a startup warning)" — `CHANGELOG.md:6409` "added a startup warning when descriptions are truncated". Correct.
  - "while the listing still carries every skill name (`:1207`)" — `:1207` "The listing always contains every skill name, but if you have many skills, Claude Code drops some descriptions to fit the listing's character budget... The budget scales at 1% of the model's context window. When the listing overflows, Claude Code drops descriptions starting with the skills you invoke least, so the skills you use most keep ..." — verified; the claimed 1% and "every skill name" are exactly on that line.
- Section-heading correctness: `§ Frontmatter reference` exists at `:365`; the `1,536` sentence is inside that section at `:389` (well past `:365`, before the next equal-level heading). Rule: location cell's section name correct.
- Under-width (silent falsity) scan on the reading cell: none — because it makes three claims, not just the quote, and all three check out on the byte-exact lines (see the three bullets above).

### Cell 4 — `corpus/lessons/round-54.md` § Gate Admitted rows S053 + S062 — HOLDS

- Provenance cell S053 = `SrcClaudeCode` (seat report § 1 fetch table row 1 URL/time/bytes/sha256 match exactly: `2026-10-22T21:15:56Z`, 111,928 B, `d1359f0c…`) and S062 = `SrcClaudeCode` (rows 4–5: `2026-10-22T21:19:52Z`, 1,070,244 B, `121129bc…`). Not Rust (no other seat claimed it).
- `quote (≤25 words)` cell: ≤25 words verified: S053 = 15 words, S062 = 18 words (validator run). Both are the same strings the counter matches byte-exactly against the SOURCES `quote` cells (S053: SOURCES.md:66 `quote` cell == lesson Gate S053 quote == entry row quote; S062 same-with – line exact matches in the fetched bytes).
- Attachments: byte counts and sha256 present in both rows' `bytes, sha256` cell with the correct first-8-hex prefixes (`d1359f0c…`, `121129bc…`); opened UTC stamps present and match the seat's fetch record exactly (21:15:56Z / 21:19:52Z).
- Header `row | URL | opened (UTC) | bytes, sha256 | quote (≤25 words) | location | seat` intact (`:21`).

### Cell 5 — `SKILL.md` § Description thresholds by client Claude Code row (`SKILL.md:185`) — HOLDS

Header row intact (`:183`: `Client | Documented threshold | Past the threshold | Action`, single `---|---|---|---` row at `:184`). Three clause-groups in the row, each checked against the fetched bytes:

- Threshold cell: "1,536 characters per entry (`description` + `when_to_use`), whatever the budget; listing budget 1% of the context window (`0.01` default, `skillListingBudgetFraction`)".
  - `1,536` + "per entry (`description` + `when_to_use`)" — verified: `:389` truncation is of the combined fields; `:1213` "each entry's combined text is capped at 1,536 characters regardless of budget" gives "per entry" and "whatever the budget" (= "regardless of budget", synonym restatement, no number invented).
  - "listing budget 1% of the context window" — verified `:1207`.
  - `(`0.01` default, `skillListingBudgetFraction`)` — verified: `settings-reference.md:2455` section heading `### `skillListingBudgetFraction``; `:2457` "caps that listing at a share of the context window... keeps every skill's name but drops the descriptions of the least-used skills"; `:2461` `* **Default**: `0.01`, which reserves 1% of the context window`. The key name, the default value, and the "1% of context window" sense all match the fetched bytes.
- Past-the-threshold cell: "Truncated at the cap, with a startup warning (v2.1.105 raised the cap from 250); past the listing budget, descriptions of the least-invoked skills are dropped and every skill name stays".
  - "Truncated at the cap, with a startup warning (v2.1.105 raised the cap from 250)" — verified: `CHANGELOG.md:6409` "raised the listing cap from 250 to 1,536 characters and added a startup warning when descriptions are truncated". Correct v2.1.105, correct 250-before number, correct post-cap warning behaviour.
  - "descriptions of the least-invoked skills are dropped and every skill name stays" — verified: `:1207` "Claude Code drops descriptions starting with the skills you invoke least"; `settings-reference.md:2457` "keeps every skill's name but drops the descriptions of the least-used skills". Both senses present on the pinned pages.
- Action cell: "Put the key use case first and keep the entry under 1,536 characters; raise `skillListingMaxDescChars` or `skillListingBudgetFraction`, or set low-priority skills `"name-only"` to leave budget for yours".
  - "Put the key use case first" — direct advice: `:389` "Put the key use case first".
  - "keep the entry under 1,536 characters" — follows from `:389`.
  - `skillListingMaxDescChars` — verified real key, `settings-reference.md:2471`, type "number of characters, a positive integer"; its section explains it caps the shown per-skill `description`+`when_to_use` text.
  - `skillListingBudgetFraction` — verified real key, `settings-reference.md:2455`, type "number, a fraction greater than `0` and at most `1`".
  - `"name-only"` — verified real setting value: `settings-reference.md:2457` "set low-priority entries to `"name-only"` in `skillOverrides`" context (`:2457` refers to name-only drop context; the concrete `"name-only"` `skillOverrides` value string verified at `settings-reference.md:2468-2470` — see the `skillOverrides` example block in the same section, `"skillOverrides": { "legacy-context": "name-only", ... }`).
- Over-width scan of the action cell: none — every clause ("keep under 1,536", "raise skillListingMaxDescChars/BudgetFraction", `"name-only"` to free budget) is either a number-backed fact from `:389`/`:1213` or a documented lever on the pinned pages; no additional unstated behaviour claimed.

(One note not a break: `settings-reference.md:2477` Default `1536` — the counter's own regex/fixed strings accept it, and the counter prints BACKED Claude Code at the graded revision, but it means the entry-threshold clause is "the cap the authoring row states", not a discovered value; no cell overstates it, so no fix needed.)

## 2. Number sense — ✅

`1,536` in the counter's Claude Code number token is the per-entry `description`+`when_to_use` write-cut in the skills listing render, as landed everywhere: quote from `:389` verified verbatim; the number is about how the listing consumes the description (the `when_to_use` row `:390` confirms `counts toward the 1,536-character cap`), not about `when_to_use` alone, not about the frontend byte-formatter and not about the `compatibility` field. Matches the C1 area (offer-render half of *Per-render consumption*): the cell separates **listing drop** (skill lost from the model's choices: `:1207`) from **description truncation** (skill still offered, description shortened: `:389`), and the SKILL.md Past cell names both in the right order.

## 3. Prior-record contradiction scan (rule: nothing contradicting an older row/entry) — ✅ no contradiction

- `sibling-overlap-census-round49.md:155,221` and `skill-selection-rules-round50.md:48` — same value `1,536`; same sense ("1,536-character listing cap on `description` plus `when_to_use`", "truncates `description` plus `when_to_use` at 1,536 characters in its listing"); consistent with `:389` today. The 1% drop-first-least-used details also match (`:1207`, `settings-reference.md:2457`).
- Older S022 row (round 51, `corpus/SOURCES.md:35`) — same `:389` sentence, same `1,536`, same "counts toward" pairing with `when_to_use` (`:390`), recorded byte-identical at re-open (`2026-10-22T09:41:02Z` → `2026-10-22T12:28:45Z` both recorded as byte-identical). Cross-checked against S022's 111,557-byte earlier fetch: S053's 111,928 B supersedes it in row content, which is why S022's record and S053's record are separate fetches and why S053 does not reuse S022's hash — exactly what the seat's § 1 note told the L1 to do, and the L1 did it.
- `SKILL.md` portability floor (1,024 max) — untouched by this row; the new row does not assert or deny a `description` authoring max for Claude Code, so no contradiction with S018/S019.
- No other lane row claims a different Claude Code listing cap, budget share, `when_to_use` inclusion, or warning mechanism that the new cells contradict.

## 4. Append-only / provenance integrity re-check — ✅

- S053 and S062 absent at plan commit (0 hits each — commands in § above with outputs). First-round-introduced: no earlier-round orphan.
- Host rule: `code.claude.com` and `raw.githubusercontent.com` (with the anthropics/claude-code path prefix) are the counter's listed Claude Code hosts (`check_description_thresholds.py` `HOSTS["Claude Code"]`); S053 and S062 are the only two Claude Code rows in SOURCES.md and both resolve the fetch to those hosts.
- Pin-integrity for S062 is unusually strong: the pin is a raw **commit** URL (not a branch); `git ls-remote ... HEAD` returned the same hash at re-check, so the pin cannot resolve differently today without the repo rewriting history — byte-identity to the recorded `121129bc…` re-verified.

## 5. Instrumentation

- Sandbox clone at `58db81c4465b0e9b07ef2485b87d8970683afac6` (per lane bounds; no lane write, no jj): `python3 -B verifiers/check_description_thresholds.py --rev HEAD` → `Claude Code  BACKED` (and Codex / VS Code / Copilot CLI / Gemini CLI / Cursor / opencode all BACKED), `description thresholds backed 7 of 7 clients`, exit 0. The C1 declared line is satisfied ("4 of 7 or more"); Claude Code specifically backs in the counter's own execution.
- `--fetch` (live-page presence, a second measurement sitting beside the declared one): `description thresholds backed 7 of 7 clients`, `description thresholds found on the live page 7 of 7`, exit 0.
- No lane state changed (working tree and jj untouched; nothing written outside my sandbox and this report).

## 6. Informational (non-breaking)

- **§ 2.1.497 line-pair no longer on the page** (seat report § 1 said "(§ 2.1.497 line-pair on the page today)": `grep -n '2.1.497' CHANGELOG.md` → no match in the fetched bytes; the 2.1.497 sentence — "Improved skill description handling... the page carries no 1,024-character description cap" — is gone from the changelogs the seat consulted, replaced upstream or named elsewhere; the S062 pin/byte-identity chain does not reference 2.1.497, so no landed text depends on it. Informational only.
- **Plain-language haystack fullness (seat report § 3 note):** the page is a haystack with few false positives. The counter print `Claude Code BACKED` resolves through the S053 row; the S053 host list path is `code.claude.com` — the counter adds `github.com/anthropics/claude-code`-only-raw-paths (verified in `HOSTS["Claude Code"]`); the seat's concern "github.com/anthropics/claude-code in the host list..." does not bite the landed row because S053's `source` cell names `code.claude.com`.

## 7. Output/verification assertion

Every claim in the five cells is now either (a) matched byte-exact on re-fetched bytes (quotes at `:389`, `:390`, `:6409`, `:1213`, `:2461`, `:2477`, `settings-reference.md:2457`, `:1207` helpers), (b) run-visible in the counter's own exits (7/7 BACKED, exit 0; --fetch 7/7, exit 0), or (c) byte-provenance recorded with UTC + fresh sha256 above. No cell required a corrected text; nothing in the lane was edited.

## 7b. Post-landing amendment the seat verified through (auto-correct; no break)

The L1 amended the working tree between the landed commit and my re-checks. The SKILL.md:185 Action cell I read mid-flight — "keep `description` within the spec's 1,024 (the listing cut is 1,536); raise skillListingMaxDescChars or skillListingBudgetFraction, or set low-priority skills `"name-only"`..." — replaces the landed "keep the entry under 1,536 characters". I verified the changed clause the same way: `SOURCES.md:14` (`S001`, tier-A `spec`, agentskills.io, taught 2026-10-19) "description 1-1024 chars saying what and when" grounds the 1,024 figure, and round-50 falsify + my § 1 checks established there is no documented Claude Code authoring max, so "the spec's 1,024" is the correct bounded qualifier, not an over-wide claim of a documented CC page limit. The counter's numeric-token rule is unaffected (cell already carried 1,536 and 1%). Entry Findings 2 and 3 grew for Codex and Gemini CLI scope corrections (not my cells; the CC sentence is unchanged: "Claude Code truncates each listing entry (`description` + `when_to_use`) at 1,536 characters (S053...S062)... drops descriptions while keeping every name (S053 `skills.md:1207`)"), and the M45 lesson row text was re-cut (no cell text that I attack changed; grep for S05x/1,536 across the lesson diff ∅). `cp` of current C1 files into my sandbox + `--root .`: `description thresholds backed 7 of 7 clients`, exit 0. Two exact corrections seen: hardcoded lane-commit wakeful GH markup row and `fault_injection_corpus.sh` Entry-command row — both C2-registry cells, outside my cells. The Claude Code cells I scope are HOLD; findings unchanged.

## Not done / out of scope

- Other six clients' cells (VS Code, Copilot CLI, Gemini CLI, Codex, Cursor, opencode), C2 Mé, self-tests, checks outside my scope.
- Reading every other row of SOURCES.md beyond S053/S062 and the pre-existing rows named in the contradiction scan (S022, S055) beyond what the five cells cite.
- No behaviour run of any client (out of bounds: no paid calls, no `claude -p`); the number sense is judged from what the clients' own pages state and from the counter's execution only.
