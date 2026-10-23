Result: DONE — opencode: ELIGIBLE `.opencode/commands/`

Census seat Censusopencode. Read-only. No tools installed. No lane code executed. Fetched bytes kept under `/tmp/census-opencode/` (not lane content).

## Page

Primary (quote source): `https://opencode.ai/v2/docs/commands/`

- Access: `Fri 23 Oct 2026 07:39:49 AM UTC` (`date -u` immediately before the curl). Response header: `date: Fri, 23 Oct 2026 07:39:50 GMT`, `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`, `content-length: 7220`, `vary: Accept`. No `Location`.
- Fetch: `curl -sSL -H 'Accept: text/markdown'`. Exit 0. Final URL unchanged. The suffix URL `https://opencode.ai/v2/docs/commands.md` is HTTP/2 404, 9 bytes, body `Not found`, sha256 `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31`. The HTML page (HTTP/2 200, 32304 bytes, sha256 `32591ac3db0056fdbf3b5e20b78e70514da0d7306707cbf7c412ca19276640e0`, fetched `Fri 23 Oct 2026 07:37:53 AM UTC`) has a copy-as-markdown control that fetches the same URL with `Accept: text/markdown` (script near the end of that HTML).
- Bytes: 7220. sha256: `c3dc75fc48071613c359126e7d84e2298afd10c4b83aac83383e94a1489a23dc`. 258 lines. Line 1: `# Commands`.
- Why this page is current: `https://opencode.ai/llms.txt` is HTTP/2 301 to `/v2/llms.txt` (`Fri 23 Oct 2026 07:39:43 AM UTC`; body 4061 bytes, sha256 `79fe81b6d690646e875dbbbc696738286f677a47bd2ea39c4318437ed0dfacd0`). Line 1 of that body is `# OpenCode V2 Documentation`. Line 18 lists `[Commands](https://opencode.ai/v2/docs/commands/)`.
- Host `opencode.ai` is pinned. Path is `/v2/docs/commands/`, not changelog, release, news, or blog.

Corroboration, same directories, older Starlight tree still served:

- `https://opencode.ai/docs/commands.md` — `Fri 23 Oct 2026 07:37:53 AM UTC`, header `date: Fri, 23 Oct 2026 07:37:53 GMT`, HTTP/2 200, `content-type: text/plain; charset=utf-8`, 6664 bytes, sha256 `30b0b5b4bdeb407855fb6b7f9b6beac6399f42f0209c1854cf5bdb3a0ceb1745`. Lines 77–78: `` - Global: `~/.config/opencode/commands/` `` and `` - Per-project: `.opencode/commands/` ``.
- Source of that page, pinned raw mirror: `https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/web/src/content/docs/commands.mdx` — `Fri 23 Oct 2026 07:39:17 AM UTC`, HTTP/2 200, `text/plain`, 6712 bytes, sha256 `853516ad84f3cf9c2c09b9ddb72a1b44c98eac072db4c2712434259bbd8bd93c`. The Starlight HTML footer links `https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/commands.mdx`. Same two directories at mdx lines 82–83. `https://github.com/sst/opencode` is HTTP/2 301 to `https://github.com/anomalyco/opencode` (same minute).

## Token

Printed folder: `.opencode/commands/`

Line 19 of the v2 markdown: a user puts project command files there. Line 3: `Create `.opencode/commands/review.md` to turn a prompt into `/review``. Line 26: only `.md` files are discovered. Lines 32–33: use `commands/` for new files.

A second printed folder on the same line also passes every conjunct below: `~/.config/opencode/commands/` (global). One client, one row. The counted token is the project folder. The global folder is recorded so the row is not forced onto it.

## Quote

File body line 19. No bytes stripped. The line is a contiguous substring of the fetched markdown. 10 whitespace-separated words with the backticks left in, and still 10 after removing the four backtick bytes (U+0060).

`Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`.`

After backtick removal the token `.opencode/commands/` starts at a space and the next byte is `.` (the sentence period, U+002E), which is not a letter, digit, `_`, or `-`. `commands` in `global commands` and in `project commands` matches `(?i)\bcommands?\b` outside that span. The `commands` inside the token does not.

## C1 conjuncts

Scored against `plans/round-58.md` § C1 and the v2 path regex `TOKEN_RE` in `verifiers/check_plugin_manifests.py:258` (`^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`). Own-marker behaviour from that file's foreign-name guard (`:245-252`, `:561-567`): a token may contain this client's marker `opencode`; it may not contain another client's.

| Conjunct | Verdict |
|---|---|
| Own documentation on a pinned host | YES. `opencode.ai` |
| Folder or file pattern for a user-written reusable prompt / custom slash-command file | YES. Markdown files in `.opencode/commands/`; a file there becomes a `/` command (lines 3, 19, 26) |
| v2 path regex | YES. `.opencode/commands/` full-matches `TOKEN_RE` (local `re.fullmatch`, exit 0) |
| After one leading `~/` or `./`, ≥ 2 path segments | YES. Nothing to strip. Non-empty segments `.opencode` and `commands` |
| First segment starts with `.` | YES. `.opencode` |
| Final non-empty segment, split on `-` `.` `_`, holds `command` / `commands` / `prompt` / `prompts` | YES. `commands` |
| No segment word is skill, skills, agent, agents, rule, rules, plugin, plugins, extension, extensions | YES. Words are `opencode`, `commands` |
| No dot inside a non-final segment except as its first character | YES. The only dot in `.opencode` is the first character (`seg[1:]` has no dot) |
| No other client's marker (`claude`, `codex`, `vscode`, `copilot`, `gemini`, `cursor`) | YES. `opencode` is this client's own marker |
| Not the same path as another client's row | Not shown as shared. A site-constrained search of cursor.com, docs.cursor.com, code.claude.com, geminicli.com, developers.openai.com, code.visualstudio.com, and docs.github.com for `.opencode/commands` returned no matches (the engine then relaxed the constraint; the hits were OpenCode pages). This seat did not fetch those clients' docs. E5 is cross-row and is not closed here |
| Quote 6–25 words, token case-sensitive, command(s)/prompt(s) outside the token | YES. 10 words, line 19, as quoted above |
| Source is not changelog / release / news / blog | YES |

The global token `~/.config/opencode/commands/` also full-matches `TOKEN_RE`. After stripping one `~/`: segments `.config`, `opencode`, `commands` (3). First segment starts with `.`. Final word `commands`. No banned segment word. No dot in a non-final segment except as the first character of `.config`. No other client's marker. The same line-19 quote holds it case-sensitively, bounded by spaces after backtick removal, with `commands` outside that span (`global commands`, `project commands`, and the project path).

## Legacy label

`deprecated` does not occur in the v2 commands markdown. `legacy` occurs once, and not on the counted token.

Lines 32–33, verbatim, the line break kept:

`The legacy singular directories `command/` are also discovered,`
`but use `commands/` for new files.`

`command/` alone fails the row rule: one non-empty segment, and it does not start with `.`. The page does not print `.opencode/command/`. [INFERENCE] that full path would match `TOKEN_RE` and the word rule, but it is not a printed token, and the sentence above calls the singular directory legacy. The counted plural folder is the form the page tells the user to use for new files.

## Near-misses on the same page (not the row)

| Printed text | Line | Why it is not the token |
|---|---|---|
| `.opencode/commands/review.md` (and the other `title=".opencode/commands/….md"` examples) | 3, 5, 23, 28, 37, 99, 109, 117, 127, 143, 152, 169, 181, 199, 212, 247, 254 | Final segment splits to a filename stem plus `md`. No command/prompt word in that segment |
| `command/` | 32 | One segment; does not start with `.`; the sentence calls it legacy |
| `commands/` | 33 | One segment; does not start with `.` |
| JSON key `"commands"` | 77 | Not a path |

## Q30

Not run. A candidate exists on the current docs page, so the silent-client sweep does not apply.
