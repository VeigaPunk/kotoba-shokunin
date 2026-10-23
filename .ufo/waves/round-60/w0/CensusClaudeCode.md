Result: DONE — Claude Code: ELIGIBLE `.claude/rules/` key `paths` line 198

Census seat CensusClaudeCode. One client. No lane files edited. No tools installed (pacman paused; nothing missing). Fetched bytes: `/fast/scratch/hyaku/kotoba-r60/CensusClaudeCode/memory.md` (headers beside it at `memory.md.headers`).

## Fetch

- URL: `https://code.claude.com/docs/en/memory.md` (pinned host `code.claude.com`; `.md` variant, no redirect).
- `date -u` at fetch: `Fri 23 Oct 2026 10:29:06 AM UTC`. Response `date`: `Fri, 23 Oct 2026 10:29:06 GMT`.
- Command (exit 0): `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' -D memory.md.headers -o memory.md -w '...' 'https://code.claude.com/docs/en/memory.md'`
- Observed: `url=https://code.claude.com/docs/en/memory.md http=200 bytes=54043 redir=0`. Content-Type `text/markdown; charset=utf-8`.
- sha256: `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` (`sha256sum memory.md`, 54043 bytes, 664 lines).

## Candidate

Token as printed (backticked on the page): `.claude/rules/`

The page names that directory for project rules, and says rules in it can be scoped so they load only for matching files. Heading and lead (fetched bytes):

```
sed -n '166p' memory.md
### Organize rules with `.claude/rules/`

sed -n '168p' memory.md
For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory. This keeps instructions modular and easier for teams to maintain. Rules can also be [scoped to specific file paths](#path-specific-rules), so they only load into context when Claude works with matching files, reducing noise and saving context space.
```

Not marked experimental, preview, deprecated, or beta. A case-insensitive scan of the 664 lines found none of those words. Version notes on the same page (`Before v2.1.211`, `Before v2.1.217`, `Before v2.1.239`) are past behavior, not a preview flag.

Same normalised token, not a second row: `~/.claude/rules/` (line 273) is user-level rules. After stripping one leading `~/` it is `.claude/rules`. Line 640 also names path-scoped rules in both `.claude/rules/` and `~/.claude/rules/`.

Not the candidate: `.claude/CLAUDE.md` matches the path regex but loads at launch for every session (line 188), not only for matching files.

## Quote (6–25 words, no bytes stripped)

Contiguous prefix of line 168 through the first `directory.` Backticks kept. Nothing removed.

`For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory.`

Whitespace-separated word count: 14 (`python3` `len(q.split())` → 14). Token `.claude/rules/` is word 13. Outside that span the word `instructions` matches `(?i)\b(rules?|instructions?)\b`. Preceding character is a backtick (segment boundary; not `.`, `/`, or `-`).

## Scope key

K = `paths`. L = 198. Key form is `paths:` at an identifier boundary (start of line, then `:`). After `:` the line is empty, so the value is a block. Line 199 (within the next 3) holds the glob `src/api/**/*.ts` (a run containing `*`).

```
sed -n '198,201p' memory.md
paths:
  - "src/api/**/*.ts"
---

```

(Line 201 is empty. These four lines sit in the fenced example opened at line 196.)

The same key also passes elsewhere on this snapshot, so a later counter that accepts any one site still hits it:

- Line 231, same block form; line 232 is `  - "src/**/*.{ts,tsx}"`.
- Line 250, backticked table cell `` | `paths` | ``, and the word `patterns` on that line outside K:

```
sed -n '250p' memory.md
| `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |
```

Line 218 has `glob` and `patterns` but `` `paths` `` is not followed by `:` or `=` and is not a table cell, so it is not a key site.

## Action line

What a rule author does (line 194). A cell can cite this line; it shares content words with the scoping action (`scoped`, `files`, `frontmatter`, `paths`, `matching`, `patterns` — more than two `[a-z]{4,}` words outside backticks):

```
sed -n '194p' memory.md
Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.
```

Also citable, not the chosen line: line 176 `Place markdown files in your project's `.claude/rules/` directory.`

## Wrong key (fails the Scope-key rule)

`description`, `alwaysApply`, `globs`, and `applyTo` do not occur on this page (case-insensitive scan). The trap on the page is the frontmatter table's column header `Description` (line 248), which a careless author could cite instead of `paths`. It is not backticked, not followed by `:` or `=`, and not a `` | `K` | `` cell:

```
sed -n '248p' memory.md
| Field | Required | Description |
```

The only field the page says Claude Code reads from a rule is `paths` (line 246: `` `paths` is the only field Claude Code reads from a rule; any other field is ignored without an error. ``). A second printed frontmatter name, auto-memory `modified` (line 561), is backticked prose, not `modified:` / `modified=` and not a table cell, and the line has no `*` glob and no `glob`/`pattern(s)` word. It fails the same rule.

## Conjuncts (C1 row rule, on these bytes)

| Conjunct | Verdict |
|---|---|
| Own docs on a pinned host name the rule-file path | YES — `code.claude.com` memory page |
| File or folder for a rule/instruction file | YES — directory of markdown rule files (lines 166, 176) |
| Applies only when the agent works on matching files | YES — line 168 "only load into context when Claude works with matching files"; line 194 "only apply when Claude is working with files matching the specified patterns". Same directory also holds rules with no `paths`, which load at launch (line 188); the path-scoped ones are the eligible use |
| `TOKEN_RE` of `check_hook_files.py` (`^(~/\|\\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`) | YES |
| After one leading `~/` or `./`, ≥ 2 segments | YES — `.claude`, `rules` |
| First segment starts with `.` | YES |
| No segment word skill(s)/agent(s)/command(s)/prompt(s)/plugin(s)/extension(s)/hook(s); `rules` allowed | YES — words `claude`, `rules` |
| E7: no non-final segment has a dot except as its first character | YES — `.claude` dot is the first character; `rules` is final |
| No other client's marker (`codex`/`vscode`/`copilot`/`gemini`/`cursor`/`opencode`) | YES — `claude` is this client's own marker |
| E5 (shared token with another client) | not applied — dropped for this round |
| Key K names the matching paths as a key that takes a path pattern at one line L | YES — `paths` at line 198 (also 231 and 250) |
| Scope-key semantic on the fetched bytes | YES — see Scope key above |
| Quote 6–25 words, token at segment boundaries, rule/instruction word outside the token | YES — 14 words, line 168 |
| Action-citable line (semantic) on the fetched bytes | YES — line 194 |
| Not changelog/release/news/blog/tracker | YES — docs page |

## Base greps (read-only, rev `31092dc6f875370bddd6eb1e4da4ca0d210c56af`)

Token with one leading `~/` or `./` and one trailing `/` removed: `.claude/rules`.

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.claude/rules' 31092dc6f875370bddd6eb1e4da4ca0d210c56af -- . ':!.ufo' | wc -l
```

exit 0, output `2`. The two blobs (not `SKILL.md`): `verifiers/check_agent_definitions.py`, `verifiers/verify_alwayson.py`.

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 31092dc6f875370bddd6eb1e4da4ca0d210c56af:SKILL.md | grep -cF 'paths'
```

exit 0, output `5`. Those lines are other uses of the substring (`SKILL.md` lines 102, 113, 288, 488, 495 at this rev: command-file prose, a checklist, harness paths). They are not a scoped-rule row. `SKILL.md` is not one of the two `.claude/rules` blobs.

## Not used

Q30 sweep not run: a candidate exists, so the client is not `silent` and not `not checked`.
