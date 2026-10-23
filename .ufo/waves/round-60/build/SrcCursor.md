Result: PARTIAL — Cursor evidence and all requested row text are prepared, but the lane snapshot and product rows were not installed under the report-only scribe boundary.

## Fetch and byte identity

No tools were installed or updated. I read `verifiers/check_scoped_rules.py` before selecting the citation and used its `curl_argv` and response-trailer handling (`:321-324, 1169-1197`). The requested `.md` route is not used; S108's source URL is the working Markdown route.

- `date -u` output: `Fri Oct 23 12:09:11 PM UTC 2026` (exit 0).
- Exact curl invocation (exit 0):
  ```
  curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' https://cursor.com/docs/rules
  ```
- Observed trailer: `200 https://cursor.com/docs/rules`; HTTP 200, final URL unchanged. Body size: 17,403 bytes. SHA-256: `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`.
- The exact counter-parsed body bytes are saved at `/fast/scratch/hyaku/kotoba-r60/SrcCursor/S108.page` (not the lane snapshot path). `sha256sum /fast/scratch/hyaku/kotoba-r60/SrcCursor/S108.page` → exit 0, `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  /fast/scratch/hyaku/kotoba-r60/SrcCursor/S108.page`; `wc -c -l /fast/scratch/hyaku/kotoba-r60/SrcCursor/S108.page` → exit 0, `399 17403 /fast/scratch/hyaku/kotoba-r60/SrcCursor/S108.page`.
- I did not write `.ufo/waves/round-60/snapshots/S108.page`: the seat boundary permits writing only this report, not lane evidence/product files. `timeout 60s test -e /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S108.page; printf 'test exit=%s\n' "$?"` → `test exit=1` (destination absent). The lane's `corpus/lessons/round-60.md` and `corpus/knowledge/scoped-rules-round60.md` also returned not found on read, so the Gate, entry and SKILL rows below are exact proposed text, not landed changes.

## Quote

Chosen quote, verbatim and unshaped: the first sentence of snapshot line 32. No bytes inside the quote were stripped; its Markdown backticks are preserved. The remainder of the fetched line, not included in this sentence, is ` They are scoped using path patterns, invoked manually, or included based on relevance.`

Command and output (line is from the scratch snapshot):
```
$ timeout 60s sed -n '32p' /fast/scratch/hyaku/kotoba-r60/SrcCursor/S108.page
Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled.
$ timeout 60s bash -c "printf '%s\\n' 'Project rules live in .cursor/rules as .mdc files and are version-controlled.' | wc -w"
11
```

The count uses the counter's `q_plain = quote.replace("`", "")` representation (`check_scoped_rules.py:1018-1022`): 11 whitespace-separated words, within 6–25. `.cursor/rules` is present at path-segment boundaries; `rules` in `Project rules` is outside the token span (`:679-723`). The counter's quote normalization drops Markdown punctuation and lowercases (`:935-961`), so this contiguous sentence is present in the fetched bytes. The same exact quote is proposed in the Gate line below; the counter's Gate test accepts whitespace-normalized quote text (`:739-754`).

## Scope key

`K = globs`; cite line 85. Required `sed -n '<L>,<L+3>p'` output (exit 0):
```
$ timeout 60s sed -n '85,88p' /fast/scratch/hyaku/kotoba-r60/S108.page
globs: src/components/**/*.tsx
alwaysApply: false
---

```

`globs` is the first backticked key in the proposed Scope key cell. On line 85 it is at an identifier boundary, followed by `:`, and its first value token is `src/components/**/*.tsx`; that token contains `*` and uses only characters accepted by `pattern_value`. This satisfies the A1 `key_site` / `scope_conjunct` rule (`check_scoped_rules.py:759-771, 793-870, 915-924`).

## Action

Proposed Action text is the page's direct instruction. It cites line 131:
```
$ timeout 60s sed -n '131p' /fast/scratch/hyaku/kotoba-r60/SrcCursor/S108.page
Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.
```

Full proposed cell, including citation, is 18 whitespace-separated words:
```
$ timeout 60s bash -c "printf '%s\\n' 'Use globs to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131)' | wc -w"
18
```

Applying `content_words` exactly as specified (`check_scoped_rules.py:881-912`) leaves `W = {scope, rule, specific, files, directories, separate, multiple, patterns, commas}` after excluding backticks, the citation and pinned STOPWORDS (`:330-342`). Every member appears on line 131; the shared-word list is that same set. Its count command/output is:
```
$ timeout 60s bash -c "printf '%s\\n' 'scope rule specific files directories separate multiple patterns commas' | wc -w"
9
```
For `|W| = 9`, the required shared count is `max(2, ceil(9/2)) = 5` (`action_need`, `:889-912`); all 9 are shared. The cell is below the 25-word maximum.

## Proposed exact text for integration

**SOURCES row S108** (full SHA-256 printed as required; follows the existing column order):
```
| S108 | Cursor Docs — Rules — https://cursor.com/docs/rules | docs | A | Cursor project rule files under `.cursor/rules` and path-glob scoping of `.mdc` files | § Project rules (`rules.md:30-32`); example frontmatter (`rules.md:83-85`); § Glob pattern examples (`rules.md:130-131`); fetched 2026-10-23T12:09:11Z, HTTP 200, 17,403 B, sha256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | re-opens S049 — Cursor documents project rules in `.cursor/rules` as `.mdc` files; `globs` scopes a rule to specific files or directories, and multiple patterns are comma-separated | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md, corpus/lessons/round-60.md |
```

**Entry row** for `corpus/knowledge/scoped-rules-round60.md`:
```
| Cursor | `.cursor/rules` | S108 | Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. |
```

**Gate line** for `corpus/lessons/round-60.md`:
```
- **S108 Cursor (re-open of S049)** — https://cursor.com/docs/rules — accessed 2026-10-23T12:09:11Z (HTTP 200, 17,403 B, sha256 `884c67ca…`; seat `SrcCursor`) — `rules.md:32`: "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled."
```

**SKILL row** for `### Scoped rule files by client`:
```
| Cursor | `.cursor/rules` (project rule folder for `.mdc` files, S108 :32) | `globs` (example `src/components/**/*.tsx`, S108 :85) | Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131) |
```

## Hand checks against the frozen counter

This is a manual review, not a C1 run or a receipt.

- **Source admission / re-open.** The proposed row uses `docs`, tier `A`, status `mined`, opened date `2026-10-23`, a full SHA-256, and pinned host `cursor.com` (`check_scoped_rules.py:262-279, 1029-1081`). The URL path `/docs/rules` is neither a tracker nor a change-note path (`:592-609`). The base S049 source cell at `corpus/SOURCES.md:62` uses `https://cursor.com/docs/rules.md`; `url_key` strips trailing `.md` (`:560-578`), so it equals the proposed URL key. The proposed teaches cell starts exactly `re-opens S049 —`. `reopen_why` accepts that only if S049 is in base, its own URL matches and the key is absent from S049's base row (`:972-994`); the read S049 row has no `globs` occurrence. No S049 in-place edit is proposed.
- **Token / entry.** `.cursor/rules` has two path segments, a dot-led first segment, the allowed `rules` segment, no banned word, and Cursor's own marker; the token checks are in `:634-662`. The proposed quote carries the exact token and the separate word `rules`; `strip_quotes`, `token_span`, and `rule_word_outside` are at `:679-732`. The quote is in the fetched page after the counter's normalization (`:935-961`) and is recorded in the proposed Gate text. The proposed source citation is S108, and its entry quote count is above.
- **Snapshot / citations / semantics.** The row's full hash equals the scratch body's hash above. The proposed Scope cell's first key is `globs`, with its own `S108 :85` citation; the proposed Action cell cites its own `S108 :131` line. Those lines satisfy the A1 scope and action predicates by the checks above (`:779-924`). The counter's exact acceptance still remains unmeasured because the source, snapshot and table rows have not been installed in the lane.
- **No counter execution.** As directed, `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` was not run; I did not run C1 self-tests, builds, or other verification.

## Conflicting prior records (verbatim)

The round-60 reports disagree; these are copied verbatim for the canonical judge, not resolved by this seat:

- `.ufo/waves/round-60/w0/CensusCursor.md:1`: `Result: DONE — Cursor: ELIGIBLE `.cursor/rules` key `globs` line 85`
- `.ufo/waves/round-60/w0b/RecensusCursor.md:1`: `Result: DONE — Cursor: NOT ELIGIBLE (no non-base page on a pinned host has `.cursor/rules` and `globs` in A1 key form; the only `globs:` site's final URL is the base rules page)`

The current assignment specifies the v2 re-open of S049; this report supplies the corresponding evidence and text, but makes no counter verdict. The C1 measurement remains for the L1 after control receipts.

## Touched surfaces, limits, out of scope

- Lane write: this report only, at `.ufo/waves/round-60/build/SrcCursor.md`. No product source, judge, `SOURCES.md`, `SKILL.md`, entry file, lesson, snapshot destination, Git/JJ state, or index was edited.
- External evidence artifact: exact body bytes at `/fast/scratch/hyaku/kotoba-r60/SrcCursor/S108.page`.
- Not done here: copying the snapshot to the lane, adding the proposed rows, the C1 counter/target measurement, SKILL line-budget move, or other clients. The round-60 entry and lesson files were absent in this worktree; those rows are handoff text only.
