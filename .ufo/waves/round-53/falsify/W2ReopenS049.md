Result: MIXED — the S049 anchor reproduces byte-for-byte (HTTP 200, 17,403 B, sha256 `884c67ca…`) and all fourteen lines the row and knowledge entry cite say what they claim, but the entry's Cursor `CLAUDE.md` fact rests on `help/customization/rules.md`, which has no SOURCES row and is missing from the entry's own `source:` header.

Seat: `KotobaR53.W2ReopenS049` (scout, leaf). Judged revision `c775d6823bfca8f0de8c0874032a954438b38edc`. Read-only web fetch and read-only lane inspection; I wrote only this report and scratch files under `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReopenS049/`. No lane file edited, no git write in the lane, no tool installed or upgraded (so the tooling directive has no entry to record), no model call, no browser.

## 1. Re-open receipt for the row's URL

Command, run in `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReopenS049`:

```
curl -sS -L --max-time 60 -o s049-rules.md -w 'url_effective=%{url_effective}\nhttp_code=%{http_code}\nsize_download=%{size_download}\ncontent_type=%{content_type}\n' 'https://cursor.com/docs/rules.md'
```
exit=0, and

```
sha256sum s049-rules.md ; wc -l -c s049-rules.md
```

| field | observed | row anchor cell (`corpus/SOURCES.md:62`) | verdict |
|---|---|---|---|
| UTC access | 2026-10-22T20:36:40Z | recorded 2026-10-22T20:09:33Z (seat gate fetch) | new observation, same bytes |
| HTTP | 200 | — | HOLDS |
| url_effective | `https://cursor.com/docs/rules.md` (no redirect) | that URL | HOLDS |
| content-type | `text/markdown; charset=utf-8` | "markdown route" | HOLDS |
| bytes | 17,403 | 17,403 B | HOLDS |
| sha256 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | `884c67ca…` | HOLDS |
| lines | 399 | (cites up to `:375`) | consistent |

Stability: the seat's two fetches (2026-10-22T20:05:37Z sweep, 20:09:33Z gate) and this one (20:36:40Z) are three observations over 31 minutes, byte-identical. The page has not moved since the row was written.

Two adjacent checks, same batch:
- `https://cursor.com/docs/context/rules.md` → 404, 389 B, `text/markdown; charset=utf-8`, sha256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1`. The row cites the live route, not the dead old path. (Matches the seat's rejection record.)
- `https://cursor.com/llms.txt` → 200, 24,815 B, sha256 `38cc4995af1037fea4daa16f4b2ed1062a4c21df63440e5703608eec1017085d`; it lists `docs/rules.md` at `:67` and `help/customization/rules.md` at `:397`, so both pages are first-class published docs pages (relevant to D1 below).

## 2. Line-by-line check of what the row cites

Each quote is ≤25 words from the fetched bytes; line numbers are the fetched file's.

| cited as | line text (quote) | what the row/entry claims from it | verdict |
|---|---|---|---|
| `§ Project rules (rules.md:32)` | "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled." | project rules are `.mdc` under `.cursor/rules` | HOLDS |
| `:42` | "Project rules must use the `.mdc` extension. A plain `.md` file in `.cursor/rules` is ignored" | teaches: project rules must be `.mdc` | HOLDS |
| `§ Importing rules from a repository (:311-313)` | ":313 Rules aren't imported on their own." | repository import is not a redirect form | HOLDS |
| `§ Referencing files from a rule (:127)` | "A file mention like `@migration-template.sql` tells Agent where to look, and Agent reads the file with its tools" + "The file's contents are not inlined into the prompt" | teaches: `@file` is a lazy tool read, contents not inlined | HOLDS |
| `§ Best practices (:155)` | "Keep rules under 500 lines" | entry §6: Cursor's length guidance | HOLDS |
| `:160` | "Reference files instead of copying their contents." | bodies cannot carry the referenced file's text | HOLDS |
| `§ Team Rules precedence (:307)` | "Rules are applied in this order: **Team Rules → Project Rules → User Rules**." | precedence axis recorded | HOLDS |
| `§ AGENTS.md (:317)` | "Place it in your project root as an alternative to `.cursor/rules`" | AGENTS.md is read at the root | HOLDS |
| `:321` | "Cursor supports AGENTS.md in the project root and subdirectories." | lesson Gate quote; entry table: root and subdirectories | HOLDS (verbatim) |
| `:342` | "they will be automatically applied when working with files in that directory or its children" | nested files apply automatically | HOLDS |
| `:357` | "Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence." | teaches: "the more specific file winning" | HOLDS for "more specific wins"; D3 notes the dropped "combined" half |
| `§ FAQ (:375)` | "The file is not inlined into the prompt, so if something must always be in context, paste it into the rule body." | reinforces `:127`; grounds "a rule body cannot inline another file's text" ([INFERENCE], but the page states it outright at `:127`) | HOLDS |
| row `teaches` compression | ":127 … Put anything that must always be in context directly in the rule body." | "so a rule body cannot inline another file's text" | HOLDS |

## 3. Line-by-line check of what the knowledge entry cites for S049

Entry: `corpus/knowledge/alwayson-rule-files-round53.md`.

| entry location | citation | check | verdict |
|---|---|---|---|
| `:1` (source header) | `S049 (https://cursor.com/docs/rules.md, `rules.md:127, 317-357`)` | both regions exist and support the AGENTS.md and non-inline facts | HOLDS (see D1: the header omits a page the entry later relies on) |
| `:31` names-read cell | `AGENTS.md` at the root and in subdirectories (`rules.md:317-357`) | `:321`, `:342`, `:357` as above | HOLDS |
| `:31` names-read cell | `CLAUDE.md` "the same way", always applied (`help/customization/rules.md:97-99`, `ScribeCursor.md`) | help page `:97` "Cursor reads `CLAUDE.md` files the same way it reads `AGENTS.md`." and `:99` "`CLAUDE.md` files are always applied to every conversation, regardless of any `alwaysApply` frontmatter setting." — quote exact; help page refetched 2026-10-22T20:36:40Z, 200, 6,285 B, sha256 `c6d2b0697e0b8f51d0d9ad7701a850cd81c389ec075e24b15e24bbd4e5afcdfc` | HOLDS as a quote; D1: that page has no SOURCES row |
| `:31` both-files cell | "reads both; no page orders them" | `grep -c -i 'claude'` on the row's page → 0; the help page's only order statement is `:82` "Team Rules > Project Rules > User Rules", and the docs page's is `:307` plus `:357` nesting — none orders AGENTS.md against CLAUDE.md | HOLDS; D4: the negative names no sweep |
| `:31` redirect cell | "none: … (`rules.md:127`)" | page documents no import/symlink redirect for rule files; `:313` "Rules aren't imported on their own."; `:127`/`:375` the opposite of inlining | HOLDS; D4 applies |
| `:40` | "VS Code, Copilot CLI and Cursor read both (S047–S049)" | the Cursor third rests only on the help page; S049's page cannot support it | D1 (citation cannot carry the clause) |
| `:49` | "not a universal import (S045 `:135-137`, S049 `:127`)" | `:127` states mentions are read lazily, not inlined | HOLDS |
| `:66` | "Cursor: "Keep rules under 500 lines" (S049 `:155`)" | verbatim at `:155` | HOLDS |
| `ScribeCursor.md` (gate table) | `:321`, `:357`, `:313`, `:127`, `:155`, `:160`, help `:97`, `:99` | every quote in the seat's gate table matches the bytes I fetched; its sha256 and byte count for both pages match mine | HOLDS |

## 4. Defects

**D1 — the Cursor "read both" fact has no SOURCES row behind it (severity: MEDIUM).**
`corpus/SOURCES.md` holds exactly one Cursor row (S049, `:62`), and its URL's page contains zero occurrences of "claude" in any case (`grep -c -i 'claude' s049-rules.md` → 0). The entry's Cursor `CLAUDE.md` statement (`corpus/knowledge/alwayson-rule-files-round53.md:31`) and its consequence (`:40`, "S047–S049") therefore stand on `https://cursor.com/help/customization/rules.md`, which is not in the registry, is not in the entry's `source:` header (`:1`), and is not in the lesson Gate's admitted table (`corpus/lessons/round-53.md:29` lists only the docs route). The fact is true and the quote exact; the ledger path is broken. The lesson records the disposition as taste — "one row per client is enough for the entry's claims; their quotes stay in the seat reports" (`corpus/lessons/round-53.md:56`) — while the plan's Frontier step says "SOURCES: rows for every always-on source opened this round" (`plans/round-53.md:84`). The L1 should either land the help-page row (the seat drafted it verbatim, `ScribeCursor.md` § SOURCES rows to append, second row) or record the deviation; S049's `scope` cell cannot absorb it, per D2.

**D2 — S049's `scope` cell promises the whole file set, the page answers one file name (severity: LOW).**
`corpus/SOURCES.md:62` scope: "Which always-on rule files Cursor Agent reads…" The page lists "four types of rules" (`:5`) without `CLAUDE.md`, and `CLAUDE.md` appears nowhere (`grep -c -i 'claude'` → 0), a documentation inconsistency the seat itself recorded (`ScribeCursor.md` § 1, last paragraph). The `teaches` cell is accurate; the scope cell is broader than its page, and a reader auditing Cursor's file set from the registry finds no row that answers it.

**D3 — the `teaches` cell drops the additive half of `:357` (severity: LOW).**
Row: "AGENTS.md is read from the project root and any subdirectory with the more specific file winning". Page `:357`: "Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence." "Winning" alone can be read as replacement; the page's semantics are combine-then-override. The same row's `scope` cell says "how nested files combine" and cites `:342`, so nothing is misstated downstream, but the `teaches` cell is the sentence a reader quotes.

**D4 — the two Cursor negatives name no sweep (severity: LOW, Q30 record shape).**
`corpus/knowledge/alwayson-rule-files-round53.md:31` records "reads both; no page orders them" and a redirect cell of "none". Both are per-client negatives; neither names the three legs Q30 requires (`corpus/QUALITY.md:41`). The sweep exists and is complete in the seat report (`ScribeCursor.md` § Q30 sweep record: release notes `200 301193`, 281-page docs tree, lane-corpus grep), so the fix is a citation (`ScribeCursor.md` § Q30) in those cells or in § Limits, not new measurement.

**D5 — one Cursor sentence in § "What follows" carries an unmarked inference (severity: LOW, informational).**
`corpus/knowledge/alwayson-rule-files-round53.md:47-48`: "VS Code, Cursor: both load, and the `CLAUDE.md` then adds only its client-specific lines". "Both load" is documented for Cursor (help `:97` "reads `CLAUDE.md` files the same way", `:99` "always applied"); "adds only its client-specific lines" is the lane's deduction from that, not a vendor sentence, and the paragraph's closing citation (S045 `:135-137`, S049 `:127`) grounds only the "not a universal import" conclusion. An [INFERENCE] marker on the Cursor parenthetical would keep the entry's own convention (the omp row already marks exactly such a step).

## 5. Non-defects checked and cleared

- Row landed in the correct commit: `git blame -L 62,62 corpus/SOURCES.md` → `55973a2` (the C2 commit), not the frozen plan commit; a content row landing after `3bb0a7a3` is not a counter widening.
- Registry accepts the row: `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, `kotoba ok /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`; the only W04 lines are the pre-existing duplicate-URL warnings for S018, S019, S021 recorded in the plan, none for S049. Eleven cells, `kind docs`, `tier A`, `status mined` with `used-by` pointing at a file that exists and cites S049 (`corpus/knowledge/alwayson-rule-files-round53.md`).
- No overclaim about dated text: neither the row nor the entry attributes a dated-text rule to Cursor (entry §5 lists only S043, S019, Gemini CLI), consistent with the page, which has no such rule.
- No overclaim about redirects: the entry's "none" is about rule-file redirects; the only `@` mention is used for templates, and `:313` says rules are not imported on their own. Both statements agree.
- No Cursor `GEMINI.md` claim anywhere; the entry's §4 lists only S046, S047, S048, S050.
- `verify_alwayson.py` reads no knowledge-entry citation and no SOURCES row (grep: no `S049`, no `SOURCES`), so D1/D4 are unguarded by any verifier — recorded as a coverage observation, not a claim about the counter's own statement.

## 6. Limits

- Documentation only. I did not run a Cursor build; the row's claims are about what Cursor publishes, and nothing here measures the product.
- I checked the row's URL, the entry's direct citations of it, and the help page the entry cites in the same cell. I did not re-open the other Cursor pages (CLI, CLI changelog, Bugbot, release notes) beyond what the seat's gate table quotes; those carry no row and no entry claim except through `ScribeCursor.md`.
- "No page orders them" (D4) is a universal negative I could only re-confirm on the two pages I fetched plus the seat's sweep; I did not re-run the 281-page tree sweep.
- Not in scope by bounds: the C1 counter and its three guards, the C2 counter and its guards, the other seven SOURCES rows, any fix.

## 7. Commands and exit codes

| command | exit | output |
|---|---|---|
| `curl -sS -L --max-time 60 -o s049-rules.md -w … https://cursor.com/docs/rules.md` | 0 | `200`, `17403`, `text/markdown; charset=utf-8`, no redirect |
| `sha256sum s049-rules.md` | 0 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |
| `grep -c -i 'claude' s049-rules.md` | 1 | `0` |
| `curl … https://cursor.com/help/customization/rules.md` | 0 | `200`, `6285`, sha256 `c6d2b069…` |
| `curl … https://cursor.com/docs/context/rules.md` | 0 | `404`, `389`, sha256 `4f98eb06…` |
| `curl … https://cursor.com/llms.txt` | 0 | `200`, `24815`, sha256 `38cc4995…`; `:67` docs route, `:397` help route |
| `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | 0 | `kotoba ok …/corpus/SOURCES.md`; W04 S018/S019/S021 only |
| `git blame -L 62,62 corpus/SOURCES.md` | 0 | row from `55973a2` |
