Result: DONE — Cursor: ELIGIBLE `.cursor/commands`

Census seat CensusCursor. Read-only. No tools installed. No lane code executed. Fetched bytes kept under `/tmp/census-cursor/` (not lane content). No sandbox clone: nothing executed lane code.

## Page

Primary (quote source): `https://cursor.com/docs/reference/deeplinks.md`

- Access: `Fri 23 Oct 2026 07:38:07 AM UTC` (`date -u` immediately before the curl that saved the body). Header: `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`, `date: Fri, 23 Oct 2026 07:38:07 GMT`, `x-matched-path: /api/raw`. No `Location`.
- Fetch: `curl -sSL -D <headers> -o <body> -w "%{http_code} %{size_download} %{url_effective}"`, exit 0. Final status 200, effective URL unchanged, 5972 bytes.
- sha256: `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4`. 169 lines. Title line 1: `# Deeplinks`.
- Pinned host `cursor.com`. Not a changelog, release, news, or blog URL.
- `https://docs.cursor.com/reference/deeplinks.md` and `https://docs.cursor.com/docs/reference/deeplinks.md`: with `-L`, HTTP/2 308 then 200 at `https://cursor.com/docs` (docs index, 603611 bytes, sha256 `e03630749f530a5f8b2ef7a07347c5789cc0f8901ac395672455edf22cf2b907`). That alias does not serve this article. The article URL above is the one that was read.

Supporting definition, no path token: `https://cursor.com/docs/customize-cursor.md`. Same curl batch, `Fri 23 Oct 2026 07:38:07 AM UTC`, HTTP/2 200, `text/markdown`, 5200 bytes, sha256 `9ae0878d97465512ad29459f5406538ec7b427dfbaa39e1cc95d3deb447f363e`. Line 31: `**Commands**` are "Reusable prompts you invoke with `/` in Agent chat. Commands are markdown files that define a focused workflow or action." Count of `.cursor/commands` in that body: 0.

## Token

Printed folder: `.cursor/commands`

One occurrence in the deeplinks body, line 54: custom commands are "defined in" that directory, and a command deeplink "creates a new command with the specified name and content" after the user reviews it. The filename template `.cursor/commands/[command].md` is not on this page.

`~/.cursor/commands` does not occur in the deeplinks body, the customize page, the skills page, the help skills page, the plugins reference, the CLI slash-command page, or `llms.txt` (count 0 in each).

## Quote

File `cursor.com_docs_reference_deeplinks.md` line 54. No bytes stripped. Contiguous substring (confirmed `token in quote` True). 13 whitespace-separated words (backticks left in: still 13; stripping the backtick characters does not change the word count).

```
Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory.
```

The token `.cursor/commands` is inside that span. Outside it, `Command` and `commands` match `(?i)\bcommands?\b`.

## C1 conjuncts

Scored against `plans/round-58.md` § C1 and the v2 path regex `TOKEN_RE` in `verifiers/check_plugin_manifests.py:258` (`^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`). Own-marker behaviour taken from that file's foreign-name guard (`:91-95`, `:561-567`): another client's marker rejects; the row's own marker does not. `TOKEN_RE.fullmatch(".cursor/commands")` is True (checked in a one-off Python copy of that regex, not by running the verifier).

| Conjunct | Verdict |
|---|---|
| Own documentation on a pinned host | YES. `cursor.com` |
| Folder or file pattern for a user-written reusable prompt / custom slash-command file | YES. Folder where custom commands are defined (line 54). Customize page line 31, a different page, calls Commands reusable `/` prompts stored as markdown files. This page does not print a filename |
| v2 path regex | YES. `.cursor/commands` full-matches `TOKEN_RE` |
| After one leading `~/` or `./`, ≥ 2 path segments | YES. Nothing to strip. Non-empty segments `.cursor` and `commands` |
| First segment starts with `.` | YES. `.cursor` |
| Final non-empty segment, split on `-` `.` `_`, holds `command` / `commands` / `prompt` / `prompts` | YES. `commands` |
| No segment word is skill, skills, agent, agents, rule, rules, plugin, plugins, extension, extensions | YES. Split words are `cursor` and `commands` (leading dot yields an empty piece, not a banned word) |
| No dot inside a non-final segment except as its first character | YES. The only dot in `.cursor` is the first character |
| No other client's marker (`claude`, `codex`, `vscode`, `copilot`, `gemini`, `opencode`) | YES. `cursor` is this client's own marker (`MARKERS["Cursor"]`), not another client's |
| Not the same path as another client's row | Not shown as shared. A site-constrained search for `.cursor/commands` on opencode.ai, geminicli.com, developers.openai.com, code.visualstudio.com, docs.github.com, and code.claude.com returned no matches (the engine then relaxed the constraint; the hits were the Cursor changelog and third-party pages). `CensusClaudeCode.md` records `.claude/commands/`, a different path. This seat did not fetch the other six clients' docs. E5 is cross-row and is not closed here |
| Quote 6–25 words, token case-sensitive, command(s)/prompt(s) outside the token | YES. 13 words, line 54, as quoted above |
| Source is not changelog / release / news / blog | YES |

## Not marked deprecated or legacy

On the deeplinks page, `deprecat`, `legacy`, `older`, and `migrate` occur 0 times.

`https://cursor.com/docs/skills.md` (curl `Fri 23 Oct 2026 07:38:34 AM UTC`, HTTP/2 200, `text/markdown`, 18477 bytes, sha256 `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d`) lines 316–329 describe a built-in `/migrate-to-skills` that converts existing user-level and workspace-level slash commands into skills. It does not say `.cursor/commands` is deprecated or legacy, and it does not print that path. The one `legacy` on that page is the skill frontmatter field `globs` (line 210), not this directory. `deprecat` occurs 0 times.

That migration note does not fail any C1 conjunct. The successor paths `.cursor/skills/` and `~/.cursor/skills/` are not eligible: the segment `skills` is banned, and the final segment does not hold command/prompt.

## Excluded: changelog file pattern

`https://cursor.com/changelog/1-6.md` is HTTP 404 (54681 bytes of HTML, not this article). `https://cursor.com/changelog/1-6` (curl `Fri 23 Oct 2026 07:39:48 AM UTC`, exit 0): HTTP/2 200, `content-type: text/html; charset=utf-8`, `date: Thu, 22 Oct 2026 22:32:35 GMT`, 145839 bytes, sha256 `8d2a8bcfbbd6f0d6a7e76cc4535106d5384a471564ba98e6cbe166be6a8f5152`.

Line 2 of that HTML (repeated at line 43) contains, with tags left in place:

```
<p>You can now create reusable prompts and quickly share them with your team. <a href="https://cursor.com/help/customization/skills#how-do-i-migrate-commands-to-skills" rel="noopener noreferrer" target="_blank">Commands</a> are stored in <code>.cursor/commands/[command].md</code>. Run them by typing <code>/</code> in the Agent input and selecting the command from the dropdown menu.</p>
```

Changelog URLs never count. The printed pattern `.cursor/commands/[command].md` also fails `TOKEN_RE` (`[` and `]` are outside the character class). `fullmatch` is False. The words `legacy` and `deprecat` do not occur in that HTML. The anchor on "Commands" points at the skills migration help section; the storage sentence is still present tense.

## Near-misses (not the row)

| Printed text | Page | Line | Why it is not the token |
|---|---|---|---|
| `commands/` | `https://cursor.com/docs/reference/plugins.md` (HTTP/2 200, `text/markdown`, 30324 bytes, sha256 `3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204`, fetched `Fri 23 Oct 2026 07:38:07 AM UTC`) | 51, 161, 268 | One segment. Does not start with `.`. Line 268: "Place them in the `commands/` directory." `TOKEN_RE` matches, the C1 segment rules do not |
| `commands/deploy-staging.md` | same plugins page | 272 | First segment `commands` does not start with `.`. Final segment splits to `deploy`, `staging`, `md` |
| `.cursor/skills/` | `https://cursor.com/docs/skills.md` | 66, 110–111, 127 | Final segment `skills` is banned and is not a command/prompt word |
| `~/.cursor/skills/` | same skills page | 68, 70 | Same `skills` ban |
| CLI `/model`, `/plan`, … | `https://cursor.com/docs/cli/reference/slash-commands.md` (HTTP/2 200, 6309 bytes, sha256 `a39f8c0086b6ca6e2bfde6c3595142987cdef4489ad0c0e213510bb746947111`) | 3–40 | Built-in CLI commands. No user file path. Count of `.cursor/commands`: 0 |
| `origin` subcommands | `https://cursor.com/docs/origin/cli/reference/commands.md` (HTTP/2 200, 13437 bytes, sha256 `da21ac820101e8ac2f54855236c80b4e7e75231314b6035f7b32f3cb26aa9034`, fetched `Fri 23 Oct 2026 07:39:48 AM UTC`) | 1–7 | Origin git CLI. The page says it is separate from the Agent CLI. No `.cursor/commands` |

Probed and 404 (389-byte body, effective URL unchanged): `https://cursor.com/docs/commands.md`, `https://cursor.com/docs/agent/commands.md`, `https://cursor.com/help/customization/commands.md`, `https://cursor.com/docs/context/commands.md`, `https://cursor.com/docs/cli/reference/commands.md`. `https://cursor.com/llms.txt` (HTTP/2 200, `content-type: text/plain; charset=utf-8`, `date: Fri, 23 Oct 2026 07:38:10 GMT`, 24815 bytes, sha256 `38cc4995af1037fea4daa16f4b2ed1062a4c21df63440e5703608eec1017085d`) lists no custom-command article other than the CLI slash-command page, the Origin command reference, and the deeplinks page already scored.

## Q30

Not run. A candidate exists on the current docs page, so the silent-client sweep does not apply.
