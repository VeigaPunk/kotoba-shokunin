Result: DONE — Gemini CLI: ELIGIBLE `~/.gemini/commands/`

Client: Gemini CLI. Eligible token, as printed: `~/.gemini/commands/`.
Backing page: `https://geminicli.com/docs/cli/custom-commands.md` (pinned host `geminicli.com`; docs URL, not changelog/release/news/blog).
The page is not marked deprecated or legacy (search of the fetched bytes for `deprecat`, `legacy`, `obsolete`: no matches).

## Fetch (primary)

Command batch started with `date -u` then `curl -sSL` of the `.md` variant (shell exit 0; status taken from curl's `%{http_code}` and the response status line).

- `date -u`: `Fri 23 Oct 2026 07:37:49 AM UTC`
- Response `date`: `Fri, 23 Oct 2026 07:37:49 GMT`
- `last-modified`: `Fri, 16 Oct 2026 02:36:07 GMT`
- HTTP status: 200
- `content-type`: `text/markdown; charset=utf-8`
- bytes: 12129 (`content-length` 12129; `wc -c` 12129)
- sha256: `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872`

The HTML URL `https://geminicli.com/docs/cli/custom-commands/` also returned 200 (138240 bytes, sha256 `d0ef568eff8705afa4b5a375a8ef297b5575ed54c701dd499da8648e3f4a883c`) in the same batch. The quote below is from the `.md` bytes, not the HTML.

## What the page states

Users write reusable prompts as custom slash commands: TOML files in a commands directory. The required field is `prompt`. Line 12 (1-indexed `splitlines` of the fetched body):

```
1.  **User commands (global):** Located in `~/.gemini/commands/`. These commands
```

No markdown bytes were stripped. Verbatim quote (8 whitespace-separated words, line 12, byte offset of the token inside the quote = 40):

```
**User commands (global):** Located in `~/.gemini/commands/`. These commands
```

Words: `**User` / `commands` / `(global):**` / `Located` / `in` / `` `~/.gemini/commands/`. `` / `These` / `commands`.

The token `~/.gemini/commands/` sits inside word 6. `(?i)\b(commands?|prompts?)\b` also matches word 2 (`commands`, quote offsets 7–15) and word 8 (`commands`, offsets 68–76), both outside the token span 40–59. The match at offset 50 is the `commands` inside the token and does not count.

## Conjuncts for `~/.gemini/commands/`

Scored against the C1 row rule. Path segments after stripping one leading `~/` and dropping the empty trailing slash: `.gemini`, `commands`. v2 path regex from `verifiers/check_plugin_manifests.py` (`^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$`) is included because the plan's well-formed rule starts with it.

| conjunct | result |
|---|---|
| Own current docs on a pinned host, not a changelog/release/news/blog URL | yes |
| Folder or file pattern where the user writes a reusable prompt / custom slash-command file | yes — global user commands; `.toml` files; required `prompt` |
| After one leading `~/` or `./`: >= 2 path segments | yes — 2 |
| First segment starts with `.` | yes — `.gemini` |
| Final non-empty segment, split on `-` `.` `_`, holds `command`/`commands`/`prompt`/`prompts` | yes — `commands` |
| No segment split on `-._` equals skill/skills/agent/agents/rule/rules/plugin/plugins/extension/extensions | yes — pieces are ``, `gemini`, `commands` |
| No dot inside a non-final segment except as its first character | yes — only non-final segment is `.gemini` |
| No other client's marker (`claude`, `codex`, `vscode`, `copilot`, `cursor`, `opencode`; `gemini` is this client's own) | yes — substring `gemini` is own; none of the other six |
| v2 path regex | yes |
| Not the same path as another client's row | not observed here — see below |
| Verbatim 6–25-word quote, token case-sensitive, `command(s)`/`prompt(s)` outside the token | yes — 8 words, line 12 |
| Page marks the form deprecated/legacy | no |

Same-path note: this seat did not open the other six clients' docs (sibling census seats). `grep` of `/home/vgpnk/Projects/shokunin/kotoba-shokunin` for `.gemini/commands` hits only `plans/round-58.md` line 30, where the plan lists it beside `.claude/commands`, `.cursor/commands`, and `.opencode/commands` and says the base tree holds each 0 times. The token contains Gemini CLI's own marker `gemini`, so under the v2 foreign-name guard it is foreign for the other six clients.

## Other printed candidates (not eligible)

Same primary fetch unless noted.

| printed token | where | why it fails |
|---|---|---|
| `` `<your-project-root>/.gemini/commands/` `` | custom-commands.md line 15 | first segment `<your-project-root>` does not start with `.`; fails v2 path regex (`<`, `>`) |
| `` `<project>/.gemini/commands/` `` | reference commands.md lines 118–119 and 123–124 | first segment `<project>` does not start with `.`; fails v2 path regex |
| `` `~/.gemini/commands/test.toml` `` | custom-commands.md line 29 | final segment `test.toml` splits to `test`, `toml` — not command/prompt |
| `` `<project>/.gemini/commands/git/commit.toml` `` | custom-commands.md line 30 | first segment not `.`; final `commit.toml` is not command/prompt; fails v2 regex |
| `` `~/.gemini/commands/refactor` `` | custom-commands.md line 288 | final segment `refactor` is not command/prompt |
| `` `commands/` `` | extensions reference.md lines 231–232 | one segment; does not start with `.` |

`.gemini/commands/` (no `~/`) would pass the shape rules, but it is not its own printed token. It only appears as the suffix of the project spans above. Normalising the eligible token (strip one `~/`, strip one trailing `/`) yields `.gemini/commands`.

The extensions page says to put TOML files in a `commands/` subdirectory of an extension. That is a second place a user can write command files, and the printed token `commands/` fails the shape rules. Extensions themselves load from `<home>/.gemini/extensions` (line 106), whose final segment is the forbidden word `extensions` and is not a command/prompt word. Not a second eligible row.

## Corroboration (not the quote source)

`https://geminicli.com/docs/reference/commands.md` — same batch, `date` header `Fri, 23 Oct 2026 07:37:50 GMT`, HTTP 200, `text/markdown`, 24304 bytes, sha256 `d31e28d5fd5c2cd98cf96344908ea996e5937207737f617c71a9a318e43a98d7`. Lines 117–119 repeat the same user token:

```
    - **Description:** List available custom command `.toml` files from all
      sources (user-level `~/.gemini/commands/`, project-level
```

`https://geminicli.com/docs/extensions/reference.md` — `date` header `Fri, 23 Oct 2026 07:37:51 GMT`, HTTP 200, `text/markdown`, 12022 bytes, sha256 `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72`.

Pinned GitHub raw mirror `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/custom-commands.md` — `date -u` `Fri 23 Oct 2026 07:40:02 AM UTC`, response `date` `Fri, 23 Oct 2026 07:40:02 GMT`, HTTP 200, 12130 bytes, sha256 `d0a7dacc329cfb6055195b066e70e6c75cfce280e626101bad14f4d1907a7e83`. The body is the site `.md` bytes plus one trailing `0x0a`. Line 12 is the same text, including `` `~/.gemini/commands/` ``.

## Tools

No packages installed.
