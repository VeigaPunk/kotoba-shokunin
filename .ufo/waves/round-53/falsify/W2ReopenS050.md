Result: MIXED — the S050 fetch still returns the same bytes and sha256 prefix the anchor cell records, all four cited section ranges and both knowledge-entry line ranges say exactly what the row and entry claim, but the anchor's parenthetical "frontmatter only differs" breaks: the served markdown also carries a site-wide `llms.txt` navigation line that is absent from `docs/src/ai/instructions.md` at `cfb894a5`.

# S050 re-open (Zed — Agent Instructions)

## Target and revision actually read

- Row: `corpus/SOURCES.md:63`, judged revision `c775d6823bfca8f0de8c0874032a954438b38edc` (`git show <rev>:corpus/SOURCES.md | sed -n '63p'`).
- Citations checked: `corpus/SOURCES.md:63`; `corpus/knowledge/alwayson-rule-files-round53.md:1, 32, 40, 53`; lesson gate row `corpus/lessons/round-53.md:30`; builder report `.ufo/waves/round-53/build/ScribeZed.md:7, 23, 28, 44-46, 52, 68`.
- Lane state note (not a defect of S050): at 20:40Z `git status --porcelain=v1` in the lane shows ` M corpus/SOURCES.md`, ` M corpus/knowledge/alwayson-rule-files-round53.md`, `?? corpus/lessons/round-53.md`. The working-tree S050 row differs from the judged blob only by writing the upstream repo prefix (`at zed-industries/zed@cfb894a5` instead of `at commit cfb894a5`); the knowledge Zed row (`:32`) is identical. This report evaluates the judged blob and says where the working copy differs.
- No lane file was written except this report; no git or jj write ran anywhere. No tool installed.

## Re-open receipt (ordinary curl, no browser, no challenge bypass)

| # | URL | UTC access | HTTP | bytes | sha256 | content-type |
|---|---|---|---|---|---|---|
| 1 | https://zed.dev/docs/ai/instructions.md | 2026-10-22T20:36:44Z | 200 | 3,169 | `7c63efe035bf063809fb9815d4ed4ce6bdde6adb718e56ecd245e025f8244ab9` | text/markdown; charset=utf-8 |
| 2 | https://zed.dev/docs/ai/instructions.md (re-fetch) | 2026-10-22T20:37:15Z | 200 | 3,169 | `7c63efe035bf063809fb9815d4ed4ce6bdde6adb718e56ecd245e025f8244ab9` | text/markdown; charset=utf-8 |
| 3 | https://raw.githubusercontent.com/zed-industries/zed/cfb894a5dde8ccf3fba1659164f47fdd1c024e2e/docs/src/ai/instructions.md | 2026-10-22T20:39:47Z | 200 | 3,256 | `1bc6e31274cb4f7ff637f74c2fab1d0051ff258b5f310db485580336f91d7f4a` | text/plain; charset=utf-8 |
| 4 | https://zed.dev/docs/ai/skills.md (control, for the nav line) | 2026-10-22T20:39:25Z | 200 | 12,053 | `764f294ea53ecfe9220c5033ac805a53dc02607b25a85b63001c57343e2b9038` | text/markdown; charset=utf-8 |

Fetch 2 was `cmp`-identical to fetch 1 (`cmp` → no output, exit 0). Fetch 3 at the full 40-hex commit is `cmp`-identical to the short-sha fetch (`SAME`). Scratch dir: `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReopenS050/`.

## Anchor-cell comparison

Judged anchor cell: `fetched 2026-10-22T20:05:08Z (200, 3,169 B, sha256 `7c63efe0…`), byte-identical on re-fetch 20:12:06Z; body identical to `docs/src/ai/instructions.md` at commit `cfb894a5` (frontmatter only differs)`.

- **Status 200 — HOLDS.** Fetch 1 reports `http_code=200`.
- **3,169 B — HOLDS.** `size_download=3169`; `wc -c` 3169.
- **sha256 `7c63efe0…` — HOLDS.** Measured full digest begins `7c63efe035bf0638`; the abbreviated cell is the house convention (compare S015 `fdbc8136…`, S018 `9a67de89…`).
- **byte-identical on re-fetch — HOLDS now.** My two fetches 43 s apart are identical; the recorded 20:12:06Z re-fetch is corroborated by `ScribeZed.md:52` and by the same full digest at `ScribeZed.md:44`. The earlier timestamps themselves are the builder's record, not re-observable.
- **"body identical to `docs/src/ai/instructions.md` at commit `cfb894a5`" — HOLDS exactly.** Removing served line 1 and source frontmatter lines 1-4 makes the two files equal: 63 lines, 3,078 bytes each, both hashing to `2ec79b6c0dce27397b32672bbe92f3a808e3f62b69ad651be809e03329b48db9`.
- **"(frontmatter only differs)" — BREAKS.** The byte arithmetic shows two differences, not one: served 3,169 = 91-byte site-wide nav line + 3,078-byte body; source 3,256 = 178-byte frontmatter (4 lines, including newlines) + 3,078-byte body. The served file's extra line 1 is, verbatim: `> For the complete documentation index and Markdown links, see [llms.txt](/docs/llms.txt).` The source bytes contain no `llms.txt` string at all, and the identical line opens another Zed docs markdown page (fetch 4, `skills.md` line 1), so it is site-serving chrome — but "frontmatter only differs" is false as written: the served page drops the frontmatter and adds a 91-byte navigation line.
- **Impact of that break:** none on the row's `teaches`, on any cited line number, on the knowledge entry, or on any verifier. The load-bearing claim (the documentation body matches the pinned source tree) is exact. Severity low. The same sentence appears in the build report (`ScribeZed.md:45`, `:68`). Note the SOURCES contract makes rows append-only — only `status`, `recheck`, `used-by` change in place, and a correction is a new row — so fixing the wording means a correcting row, not an edit (fleet `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:49-51`).

## Cited section ranges — HOLDS/BREAKS per line

All line numbers are against the served `instructions.md` (fetch 1), which is the file the URL and the anchor name. Headings confirmed by `grep -n '^## '`: `11`, `23`, `39`, `50`, `57`.

| Cited range | What the row/knowledge says the range shows | Observed (quote ≤25 words, line) | Verdict |
|---|---|---|---|
| `instructions.md:11-21` (§ Personal Instructions) | personal always-on file | `:13` "Personal instructions apply to every project you open with the Zed Agent."; `:18` `~/.config/zed/AGENTS.md`; `:21` "On Windows, the equivalent file is under `%APPDATA%\Zed\AGENTS.md`." Range starts at the `:11` heading and ends at `:21`; next heading `:23`. | **HOLDS** |
| `:23-37` (§ Project Instructions) | first-match nine-name list and personal/project combination | `:25` "Project instruction files apply to the current project. Zed uses the first matching file in this list:"; `:37` "Project instructions override personal `AGENTS.md` when they conflict." | **HOLDS** |
| `:27-35` (list, cited by row prose and knowledge `:32` as `:25-35`) | fixed nine-name ordered list, starts four names, ends two names | `sed -n '27,35p' \| grep -c '^- '` → `9`; order is `.rules`, `.cursorrules`, `.windsurfrules`, `.clinerules`, `.github/copilot-instructions.md`, `AGENT.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`. | **HOLDS** |
| `:39-48` (§ Instruction File Support) | which files the Zed Agent loads, and the loader's boundary | `:45` "`CLAUDE.md` | Loaded as compatible project instructions by Zed Agent"; `:48` "External Agents and Terminal Threads may read their own native instruction files directly. Do not assume Zed's instruction loader controls those agents." | **HOLDS** |
| `:57-63` (§ Migrating from Rules) | rules replaced, `.rules` stays as a compatibility name | `:59` "Rules have been replaced by Skills and Instructions:"; `:63` "project `.rules` files remain supported as compatible project instruction files" | **HOLDS** |

Row `teaches` decomposed:

- "Zed uses the first matching project instruction file" — `:25`, verbatim. **HOLDS.**
- "a fixed nine-name ordered list that starts `.rules`, `.cursorrules`, `.windsurfrules`, `.clinerules` and ends `CLAUDE.md`, `GEMINI.md`" — `:27-35`, nine items, same order. **HOLDS.**
- "never merges two of them" — the page never uses "merge"; it says only the first matching file (`:25`), which entails one project file. Code corroboration is claimed at `ScribeZed.md:23` ("One project file per worktree root, never merged"), which this seat did not re-run. **HOLDS** as a paraphrase of `:25`; the merge clause is [INFERENCE] from "first matching file" plus the builder's code reading, not a page sentence.

## Knowledge-entry citations

| Location | Claim | Observed | Verdict |
|---|---|---|---|
| `alwayson-rule-files-round53.md:1` | S050 source range `instructions.md:23-37` | `:23` § Project Instructions heading through `:37` override sentence; the range contains the first-match rule and the whole name list. | **HOLDS** |
| `:32` col 3 | "the first match of a nine-name list … (`instructions.md:25-35`)" | `:25` first-match sentence, `:27-35` the nine names. | **HOLDS** |
| `:32` col 4 | "reads `AGENTS.md`; `CLAUDE.md` is ignored silently" | `AGENTS.md` at `:33` precedes `CLAUDE.md` at `:34` in a first-match list, so with both present only `AGENTS.md` is selected. `CLAUDE.md` is read when no earlier name matches (`:45` "Loaded as compatible project instructions by Zed Agent"), which the column header's both-present scope does not claim otherwise. | **HOLDS**; see D2 for "silently" and the scope reading |
| `:32` col 5 | "none documented; `@AGENTS.md` is literal text (code reading at `cfb894a5`, `ScribeZed.md`)" | No `@` character occurs anywhere in the served bytes (`grep -n '@' zed-instructions.md` → no output), so "none documented" holds. The code half points at `ScribeZed.md:28`, which states the loader has no import expansion and marks it "[INFERENCE from code; not executed]" and "the model may or may not act on" it. | **HOLDS** for the doc half; see D3 for the lost inference marker |
| `:40` | "Codex, opencode and Zed read only `AGENTS.md`" (both-files scenario) | For Zed, `AGENTS.md` (`:33`) outranks `CLAUDE.md` (`:34`) by first match (`:25`). | **HOLDS** in the stated both-files scope |
| `:53` | `GEMINI.md` and `.github/copilot-instructions.md` are further names (S050) | Both names are in the list, `:31` and `:35`. | **HOLDS** |
| `corpus/lessons/round-53.md:30` | S050 gate row: 3,169 B, `7c63efe0…`, quote at `instructions.md:25` | Bytes and digest prefix match fetch 1; `:25` contains the quoted sentence verbatim. | **HOLDS** |

## Registry and census check

`./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin --today 2026-10-22 kotoba` → exit 0:

```
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/build-skills across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
```

S050 does not appear in any E or W finding; the three W04 rows are the same pre-existing warnings the plan records at base. Row fields pass the schema: 13 pipe fields, status `mined` with an existing `used-by` path (`corpus/knowledge/alwayson-rule-files-round53.md`), `opened 2026-10-22` not in the future, `recheck 90d`. The run read the working tree (which differs from the judged blob only in S050's commit-reference formatting) and the result is the same for the judged row.

## Defects

- **D1 — Low (anchor cell accuracy).** `corpus/SOURCES.md:63` says the served page differs from `docs/src/ai/instructions.md` at `cfb894a5` by "frontmatter only". Observed: frontmatter (178 bytes) is absent from the served file and a 91-byte site-wide nav line is added; byte totals 3169 = 91 + 3078 and 3256 = 178 + 3078. The documentation body itself is byte-identical (3,078 bytes, `2ec79b6c…`). No fact, line citation or verifier depends on the parenthetical. Same sentence at `.ufo/waves/round-53/build/ScribeZed.md:45` and `:68`; a fix is a correcting row under the append-only contract.
- **D2 — Informational.** `corpus/knowledge/alwayson-rule-files-round53.md:32` says "`CLAUDE.md` is ignored silently". The selection half is sourced (`:25` first match, `:33` before `:34`); "silently" (no warning) is an absence claim: `grep -n -iE 'warn|silent'` over the served page returns no hit, and the builder's recorded sweeps (`ScribeZed.md:58-62`) cover import, symlink, size and dated text, not notification. Not contradicted; label it an inference or add the sweep. The column header scopes the sentence to the both-present case; read alone it could be taken as "Zed never reads CLAUDE.md", which `:45` denies.
- **D3 — Informational.** The same cell states "`@AGENTS.md` is literal text" flatly, while its cited report marks that exact conclusion `[INFERENCE from code; not executed]` and says the model may or may not act on the text (`ScribeZed.md:28`). The "code reading" pointer keeps it honest; no contradiction, and the doc half (no import documented) is fully sourced (zero `@` in the page).

## Not checked / residual unknowns

- The zed loader code at `cfb894a5` (first-match `.next()`, no import expansion, symlink handling) was not re-executed or re-cloned here; the row's code-adjacent clauses rest on `ScribeZed.md` and are marked as corroboration, not independent proof.
- The historic fetch times `20:05:08Z` and `20:12:06Z` are the builder's record; I confirmed the bytes and digest now and across two of my own fetches, which is consistent but does not re-observably prove those timestamps.
- The HTML route (`ScribeZed.md:45`, G2) and the release-notes route (G5) are outside this ticket and untouched.
- zed.dev could in principle serve different bytes to a browser session; no headless browser was used, per the bounds, so this is a plain-HTTP observation only.
