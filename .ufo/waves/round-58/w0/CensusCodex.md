Result: DONE — Codex: ELIGIBLE `~/.codex/prompts/`

Census seat CensusCodex. Read-only. No tools installed. No lane code executed. Fetched bytes kept under `/fast/scratch/hyaku/kotoba-r58/CensusCodex/` (not lane content).

## Page

Primary (quote source): `https://learn.chatgpt.com/docs/custom-prompts.md`

- Access: `Fri 23 Oct 2026 07:38:12 AM UTC` (`date -u` on the curl that saved the body). Response header `date: Fri, 23 Oct 2026 07:38:12 GMT`, `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`, `x-vercel-cache: MISS`. No further redirect (`url_effective` is that URL).
- Fetch: `curl -sSL -D headers -o custom-prompts.md`, exit 0.
- Bytes: 3357. sha256: `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9`. 62 lines. Title line 1: `# Custom Prompts`.
- Pinned host `learn.chatgpt.com`. Not a changelog, release, news, or blog URL.
- Same path on `developers.openai.com` (also pinned): `Fri 23 Oct 2026 07:39:20 AM UTC`, `HTTP/2 308`, `location: https://learn.chatgpt.com/docs/custom-prompts.md`. An earlier `-L` fetch of `https://developers.openai.com/codex/custom-prompts.md` (`Fri 23 Oct 2026 07:37:50 AM UTC`) landed on the same markdown bytes (same sha256, 3357 bytes, HTTP 200).

HTML rendering of the same page, not the quote source: `https://learn.chatgpt.com/docs/custom-prompts`, `Fri 23 Oct 2026 07:40:02 AM UTC`, HTTP 200, 358363 bytes, sha256 `ee5d7460a6a177a0cf04adf2aea060b04af4d224eea4d9c9dd6b3bff170d33f5`. The token and the sentence are present. Where the markdown has backticks, the HTML has `<code>` … `</code>` (those ten bytes around the token). A fetch of the HTML URL will not contain the backtick characters.

`github.com/openai/codex` README (`https://raw.githubusercontent.com/openai/codex/main/README.md`, `Fri 23 Oct 2026 07:39:29 AM UTC`, HTTP 200, 3334 bytes, sha256 `ba4e1f69ff48386e72a9c5e1edaf76aad64a475c2d51af79ccba6d1128261ba7`) does not mention `prompts/` or a custom-command directory. The docs-tree API call returned HTTP 403 rate limit; the HTML tree page did not contain `.codex/prompts`. The documented pattern is the learn.chatgpt.com page above.

## Token

Printed folder: `~/.codex/prompts/`

It is the directory where a user writes a Markdown file that Codex loads as a custom slash command. Line 8: custom prompts turn Markdown files into reusable prompts invoked as slash commands. Line 15: `mkdir -p ~/.codex/prompts`. Line 62: edit or delete files under `~/.codex/prompts/`; only top-level Markdown files in that folder are scanned.

`normalise` (strip one leading `~/` and one trailing `/`) of `~/.codex/prompts/` and of the line-15 spelling `~/.codex/prompts` is the same path `.codex/prompts`. The row token is the backticked directory form on line 62.

## Quote

File `custom-prompts.md` line 62. No bytes stripped. Contiguous substring (confirmed `quote in file` True). 9 whitespace-separated words (backticks left in: still 9).

`Manage prompts by editing or deleting files under `~/.codex/prompts/`.`

The token `~/.codex/prompts/` is inside that span. Outside it, `prompts` matches `(?i)\bprompts?\b`.

## C1 conjuncts

Scored against `plans/round-58.md` § C1 and the v2 path regex `TOKEN_RE` in `verifiers/check_plugin_manifests.py` (`^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`). Own-marker behaviour taken from that file's foreign-name guard: another client's marker inside the token is rejected; the row's own marker is not. Codex's own marker is `codex`.

| Conjunct | Verdict |
|---|---|
| Own documentation on a pinned host | YES. `learn.chatgpt.com`. Also reached by 308 from `developers.openai.com` |
| Folder or file pattern for a user-written reusable prompt / custom slash-command file | YES. Markdown files under `~/.codex/prompts/`, invoked as `/prompts:…` (lines 8, 15, 18, 34, 62) |
| v2 path regex | YES. `~/.codex/prompts/` full-matches `TOKEN_RE` |
| After one leading `~/` or `./`, ≥ 2 path segments | YES. Strip `~/`. Non-empty segments `.codex` and `prompts` |
| First segment starts with `.` | YES. `.codex` |
| Final non-empty segment, split on `-` `.` `_`, holds `command` / `commands` / `prompt` / `prompts` | YES. `prompts` |
| No segment word is skill, skills, agent, agents, rule, rules, plugin, plugins, extension, extensions | YES. Words are `codex`, `prompts` |
| No dot inside a non-final segment except as its first character | YES. The only dot in `.codex` is the first character |
| No other client's marker (`claude`, `vscode`, `copilot`, `gemini`, `cursor`, `opencode`) | YES. `codex` is this client's own marker, not another client's |
| Not the same path as another client's row | Not shown as shared. A search for `~/.codex/prompts` constrained to the other six clients' pinned hosts returned no matches (the engine then relaxed the constraint; the hits were Codex pages and GitHub issues). This seat did not fetch those clients' docs. E5 is cross-row and is not closed here |
| Quote 6–25 words, token case-sensitive, command(s)/prompt(s) outside the token | YES. 9 words, line 62, as quoted above |
| Source is not changelog / release / news / blog | YES |

## Deprecated, not withdrawn

The page marks the form deprecated and still states the write location.

- Line 5: `Custom prompts are deprecated.`
- Line 8: `Custom prompts (deprecated) let you turn Markdown files into reusable prompts that you can invoke as slash commands in both the Codex CLI and the Codex IDE extension.`
- Lines 12–18 and 62 still tell the user to create `~/.codex/prompts` and to put Markdown files directly under `~/.codex/prompts/`.

That does not fail any C1 conjunct. The index line on `https://learn.chatgpt.com/llms.txt` (same curl batch, HTTP 200, 33447 bytes, sha256 `fc7b20eaea56f8fe5dcc0280262009f9546172c521f69cb08b8befc89f03b943`, line 98) says `Deprecated. Use skills for reusable prompts`.

The recommended successor is skills, not a command-file path. `https://learn.chatgpt.com/docs/build-skills.md` (`Fri 23 Oct 2026 07:40:15 AM UTC`, HTTP 200, 11035 bytes, sha256 `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`), line 138, prints `.agents/skills`. That token is not eligible: segment words `agents` and `skills` are banned, and the final segment does not hold command/commands/prompt/prompts. `$CWD/.agents/skills` and `$HOME/.agents/skills` (lines 142 and 145) also fail `TOKEN_RE` (the `$`).

## Near-misses on the custom-prompts page (not the row)

| Printed text | Line | Why it is not the token |
|---|---|---|
| `~/.codex` | 10 | One segment after stripping `~/`. Final word `codex`, not command/prompt |
| `~/.codex/prompts` | 15 | Same directory, no trailing slash. `normalise` equals the row token. Not a second path |
| `~/.codex/prompts/draftpr.md` | 18 | Final segment `draftpr.md` splits to `draftpr`, `md`. No command/prompt word |

## Q30

Not run. A candidate exists on the current docs page, so the silent-client sweep does not apply.
