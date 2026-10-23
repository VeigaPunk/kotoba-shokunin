Result: DONE — Cursor: ELIGIBLE `.cursor/rules` key `globs` line 85

Census seat CensusCursor. One client. No lane files edited. No tools installed (pacman paused; nothing missing). Scored snapshot: `/fast/scratch/hyaku/kotoba-r60/CensusCursor/rules.md` (headers `rules.md.hdr`). A second page was fetched and is not the scored snapshot (see Help page).

## Fetch

- URL that returns the page: `https://cursor.com/docs/rules` with `Accept: text/markdown` (pinned host `cursor.com`). Final URL `https://cursor.com/docs/rules`. Content-Type `text/markdown; charset=utf-8`. `x-matched-path: /api/raw`.
- The `.md` variant `https://cursor.com/docs/rules.md` is **404** (same Accept, 389 bytes, final URL unchanged, `date` `Fri, 23 Oct 2026 10:32:02 GMT`). `llms.txt` and the help page link that 404. Do not cite it.
- `date -u` at the scored fetch: `Fri 23 Oct 2026 10:29:16 AM UTC`. Response `date`: `Fri, 23 Oct 2026 10:29:16 GMT`.
- Command (exit 0): `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' -H 'Accept: text/markdown' -D rules.md.hdr -o rules.md --max-time 40 'https://cursor.com/docs/rules'`
- Observed write-out: `md_status=200 final=https://cursor.com/docs/rules size=17403 ctype=text/markdown; charset=utf-8`.
- sha256: `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` (`sha256sum rules.md`, 17403 bytes, 399 lines).

`docs.cursor.com/context/rules` (probed the same minute) redirects to `https://cursor.com/docs` (the index, 42554 bytes), not this page.

## Candidate

Token as printed, backticked in prose: `.cursor/rules`

Project rules live in that folder as `.mdc` files and can be scoped with the `globs` frontmatter key so they attach only when a matching file is in context. The folder also holds always-apply, description-selected, and manual rules (lines 65–70). The path-scoped ones are the eligible use.

```
sed -n '32p' rules.md
Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. They are scoped using path patterns, invoked manually, or included based on relevance.

sed -n '68p' rules.md
| `false`       | —             | provided | Auto-attached when a matching file is in context.                |
```

Not marked experimental, preview, or deprecated on this page. A scan of the 399 lines for those words plus `legacy` hit only line 250, inside an example of adding a Cursor setting (`For beta features, add toggle in `@settingsBetaTab.tsx``). That sentence is not a status of rules.

Same normalised token, not a second row: line 45 prints `.cursor/rules/` (trailing slash) inside a bash tree, not as a backticked span. `normalise()` of that form is `.cursor/rules`.

Not the candidate:

- `AGENTS.md` (lines 315–357), including nested files that apply when working in that directory. One segment, does not start with `.`, no frontmatter path key. Directory nesting, not a scope key.
- `.cursorrules` is absent from this page. The help page calls it legacy (below). It is one segment, so it fails the token rule anyway.

## Quote (6–25 words, no bytes stripped)

Contiguous prefix of line 32 through `version-controlled.` Backticks kept. Nothing removed. `line.startswith(quote)` is true on the fetched bytes (`q_len` 81, `line_len` 168).

`Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled.`

Whitespace-separated word count: 11 (`len(q.split())` → 11; `len(q.replace("`","").split())` → 11). Token `.cursor/rules` is word 5. Outside that span, `(?i)\b(rules?|instructions?)\b` matches the earlier word `rules` in `Project rules` (span 8–13). The match inside `/rules` (span 30–35) is inside the token and does not count. Left character of the token is a backtick.

The whole of line 32 is also 24 words and would pass. Not used: line 9 (`Stored in `.cursor/rules`, version-controlled and scoped to your codebase.`) has `rules` only inside the token.

## Scope key

K = `globs`. L = 85. Key form is `globs:` at an identifier boundary (start of line, then `:`). The same line holds the glob `src/components/**/*.tsx`, one run of `[A-Za-z0-9_./*{},!-]` containing `*`. The next-3-lines clause is not needed.

```
sed -n '85,88p' rules.md
globs: src/components/**/*.tsx
alwaysApply: false
---

```

(Line 88 is empty. These lines sit in the fenced example opened at line 83, title `Auto-attached by file pattern`.)

Line 65 is a backticked table cell `` | `globs` | `` but it is **not** a key site: the only `globs` is K's own span, and the line has no `*` run and no other `glob`/`pattern(s)` word. Cite 85, not 65.

Line 131 has `` `globs` `` and the word `patterns`, but `globs` is not followed by `:` or `=` and is not a table cell, so it is not a key site. It is the action line.

## Action line

What a rule author does (line 131). A cell can cite this line. Content words of four or more letters outside backticks include `scope`, `rule`, `specific`, `files`, `directories`, `multiple`, `patterns` (more than two):

```
sed -n '131p' rules.md
Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas.
```

Also citable, not the chosen line: line 148, `Agent generates the rule file with proper frontmatter and saves it to `.cursor/rules`.`

## Wrong key (fails the Scope-key rule)

`description` at line 179 is `description:` (key form holds) but the line has no `*` run and no `glob`/`globs`/`pattern`/`patterns` word, and the value is not a block (`"` follows the colon, not only spaces, `[`, or `|`):

```
sed -n '179p' rules.md
description: "This rule provides standards for frontend components and API validation"
```

`alwaysApply` at line 74 fails the same way (`true` follows the colon; lines 86 and 100 are the same shape):

```
sed -n '74p' rules.md
alwaysApply: true
```

Traps that **pass the mechanical test** and must not be cited as the scope key:

- Line 65. `` | `description` | `` and `` | `alwaysApply` | `` are backticked table cells, and the word `globs` sits on that line outside either span. A cell that names `description` or `alwaysApply` at line 65 would clear the Scope-key rule even though neither key names paths.

```
sed -n '65p' rules.md
| `alwaysApply` | `description` | `globs`  | Behavior                                                         |
```

- Line 99. `description:` plus the word `patterns` outside K. No `*` glob. Still a mechanical pass for the wrong key.

```
sed -n '99p' rules.md
description: RPC service conventions and patterns for the backend
```

`applyTo` and `paths` do not occur on this page.

## Conjuncts (C1 row rule, on these bytes)

| Conjunct | Verdict |
|---|---|
| Own docs on a pinned host name the rule-file path | YES — `cursor.com` `/docs/rules` |
| File or folder for a rule/instruction file | YES — project-rule folder (lines 9, 32, 42) |
| Applies only when the agent works on matching files | YES — line 32 "scoped using path patterns"; line 68 "Auto-attached when a matching file is in context" when `globs` is provided. The same folder also holds rules that are not path-scoped (lines 67, 69, 70) |
| `TOKEN_RE` of `check_hook_files.py` (`^(~/\|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`) | YES |
| After one leading `~/` or `./`, ≥ 2 segments | YES — `.cursor`, `rules` |
| First segment starts with `.` | YES |
| No segment word skill(s)/agent(s)/command(s)/prompt(s)/plugin(s)/extension(s)/hook(s); `rules` allowed | YES — words `cursor`, `rules` |
| E7: no non-final segment has a dot except as its first character | YES — the dot in `.cursor` is the first character; `rules` is final |
| No other client's marker (`claude`/`codex`/`vscode`/`copilot`/`gemini`/`opencode`) | YES — `cursor` is this client's own marker |
| E5 (shared token with another client) | not applied — dropped for this round |
| Key K names the matching paths as a key that takes a path pattern at one line L | YES — `globs` at line 85 only (line 65 fails for this K) |
| Scope-key semantic on the fetched bytes | YES — see Scope key above |
| Quote 6–25 words, token at segment boundaries, rule/instruction word outside the token | YES — 11 words, prefix of line 32 |
| Action-citable line (semantic) on the fetched bytes | YES — line 131 |
| Not changelog/release/news/blog/tracker | YES — docs page |

## Base greps (read-only, rev `31092dc6f875370bddd6eb1e4da4ca0d210c56af`)

Token with one leading `~/` or `./` and one trailing `/` removed: `.cursor/rules`.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.cursor/rules' 31092dc6f875370bddd6eb1e4da4ca0d210c56af -- . ':!.ufo' | wc -l
```

exit 0, output `5`. The five blobs (not `SKILL.md`): `corpus/knowledge/instruction-surface-census-round13.md`, `corpus/knowledge/instruction-surface-remeasure-round13.md`, `verifiers/check_agent_definitions.py`, `verifiers/check_command_files.py`, `verifiers/check_hook_files.py`.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 31092dc6f875370bddd6eb1e4da4ca0d210c56af:SKILL.md | grep -cF 'globs'
```

exit 1, output `0` (grep's no-match status; the count printed is 0). A separate `grep -cF '.cursor/rules'` on that same `SKILL.md` blob is also `0`, exit 1.

## Help page (not the scored snapshot)

`https://cursor.com/help/customization/rules` with the same Accept, fetched `Fri 23 Oct 2026 10:31:37 AM UTC` (response `date` `Fri, 23 Oct 2026 10:31:37 GMT`), HTTP 200, final URL unchanged, 6285 bytes, sha256 `c6d2b0697e0b8f51d0d9ad7701a850cd81c389ec075e24b15e24bbd4e5afcdfc`, saved at `/fast/scratch/hyaku/kotoba-r60/CensusCursor/help-rules.md`. It repeats `.cursor/rules/` (with a trailing slash) and "Apply to Specific Files" (line 27, example `` `*.tsx` ``) but never prints `globs:` as a key, so it cannot carry K. It does say the other file is legacy:

```
sed -n '88p' help-rules.md
The `.cursorrules` file in your project root is legacy and will be deprecated. To migrate:
```

That status is about `.cursorrules`, not `.cursor/rules`.

## Not used

Q30 sweep not run: a candidate exists, so the client is not `silent` and not `not checked`.
