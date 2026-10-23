---
source: S089 https://code.claude.com/docs/en/slash-commands.md; S090 https://learn.chatgpt.com/docs/custom-prompts.md; S091 https://code.visualstudio.com/docs/agent-customization/prompt-files.md; S093 https://geminicli.com/docs/cli/custom-commands.md; S094 https://cursor.com/docs/reference/deeplinks.md; S095 https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx; S028 (re-opened) https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_command_files.py --rev <rev> --fetch
---

# Custom command files by client (round 58)

A custom command (VS Code: a prompt file; Codex: a custom prompt) is a file the user writes once and invokes as a slash
command — `/name`, or a prefixed or namespaced form (Codex `/prompts:name`, Gemini CLI `/dir:name`). The pages below
describe it as user-invoked; that the model does not pick it from a description, as it may pick a skill, is this lane's
reading of those pages, not a sentence any of them states. Before auditing one, find the folder the client reads and what a file in it may set. This entry records, from
each client's own documentation opened on 2026-10-23, where that folder is and what a file sets. It is vendor
documentation, not a runtime measurement: no client was run.

Three clients point authors from command files to skills: Claude Code calls `.claude/commands/` files "the older format"
that "still works" (S089 `slash-commands.md:172`); Codex marks custom prompts deprecated in favour of skills (S090
`custom-prompts.md:5-8`); VS Code prompt files run only in Local harness sessions, and its page sends reusable workflows
for other harnesses to an agent skill (S091 `prompt-files.md:17`). Copilot CLI documents no command folder of its own:
its plugin reference loads Claude Code's folder and lets skills override it — "then commands (.claude/commands/), skills
override commands" (S028 `cli-plugin-reference.md:456`, re-opened this round); a CLI plugin's `com.github.copilot/commands/`
namespace is a plugin path, not a user folder (W0 `CensusCopilotCLI`).

**Row rule (applied to every row the same way).** The Command files cell leads with the folder (or file pattern) named
in the census token the plan froze for that client (`plans/round-58.md` § C1, census before targets): the project folder
for Claude Code, Cursor and opencode; the only documented folder for Codex (user) and VS Code (workspace; its user prompt
files live in profile data, not a named folder); for Gemini CLI the user folder `~/.gemini/commands/`, because its project
form is printed as `<your-project-root>/.gemini/commands/`, which the counter's token grammar rejects. Codex's and VS
Code's folders were already named in this corpus (`instruction-surface-census-round13.md`), so they are not new ground.

Quote notes (corrected in the falsify wave, seats `ReviewEntry`, `CriticVSCodeQuote`, `ReopenS091`): Codex, Cursor and
opencode quote one source line verbatim. Claude Code drops the line's leading `* ` list marker. Gemini CLI keeps the
page's `1.` list marker and bold markers and folds one line break (`custom-commands.md:12-13`) to a space. VS Code spans
five source lines of a Markdown table (`prompt-files.md:21-25`): the line breaks and the blank line are folded to single
spaces and each table pipe is written `&#124;` so the quote stays inside one table cell; no word is changed; the page has
no prose sentence naming the folder in 6–25 words. opencode quotes the pinned docs source because the served page is HTML
without `Accept: text/markdown`, on which the counter's tag stripping separates the folder from its closing period.
S089's URL (`slash-commands.md`) serves the same bytes as `skills.md`, the URL of base row S065: S089 is a second row
on the same document, mined for the command-file content, not an independent authority (`CriticS089Alias`).

| Client | Command files | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude/commands/` | S089 | "**Command files**: a Markdown file in `.claude/commands/` is the older format and still works." |
| Codex | `~/.codex/prompts/` | S090 | "Manage prompts by editing or deleting files under `~/.codex/prompts/`." |
| VS Code | `.github/prompts` | S091 | "that the Local harness uses for prompt files. &#124; Scope &#124; Default file location &#124; &#124;-------&#124;-----------------------&#124; &#124; Workspace &#124; `.github/prompts` folder &#124;" |
| Gemini CLI | `~/.gemini/commands/` | S093 | "1.  **User commands (global):** Located in `~/.gemini/commands/`. These commands are available in any project you are working on." |
| Cursor | `.cursor/commands` | S094 | "Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory." |
| opencode | `.opencode/commands/` | S095 | "Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`." |

## What a file sets (per client; quotes in the seat reports `.ufo/waves/round-58/build/Src*.md`)

- **Claude Code** (S089): a Markdown file; `deploy.md` becomes `/deploy` (`:450`); the same frontmatter as a skill except
  `name` and `paths` (`:378`); `argument-hint` and named positional `arguments` for `$name` substitution (`:402-403`).
- **Codex** (S090): a Markdown file in the user folder only, not shared through the repository (`:10`); `draftpr.md` is
  invoked as `/prompts:draftpr` (`:18,34`); frontmatter `description` and `argument-hint` (`:40-41`); `$1`–`$9` and
  `$ARGUMENTS` placeholders (`:42`).
- **VS Code** (S091): `.prompt.md` Markdown files (`:35`); optional frontmatter `description`, `name`, `argument-hint`,
  `agent`, `model`, `tools` (`:39-44`); `name` follows `/` and defaults to the file name (`:40`); `${input:…}`
  variables (`:69`); user-level files live in VS Code profile user data (`:26`).
- **Gemini CLI** (S093): TOML files with the `.toml` extension (`:41-42`); required `prompt`, optional `description`;
  the path under `commands/` names the command and subfolders make `:` namespaces (`:25-27`); `{{args}}` substitutes
  what follows the command (`:58-67`); a project `.gemini/commands/` sits beside the user folder (`:8-17`).
- **Cursor** (S094): Markdown files (`customize-cursor.md:31`, supporting page in the S094 row) in `.cursor/commands`
  (`deeplinks.md:54`); these pages document no frontmatter or argument schema, and no user-level path is printed.
- **opencode** (S095): only `.md` files are discovered and nested paths become `/`-separated names (`:28`); optional YAML
  frontmatter, and the trimmed body is the prompt template (`:37`); `$ARGUMENTS` is the whole argument string (`:99`) and
  `$1`–`$n` positional placeholders exist (`:109`); the user folder is `~/.config/opencode/commands/` (`:21`); legacy
  singular `command/` folders are still discovered (`:34`).

## Limits

- Vendor documentation only; no client was run, so precedence between a command and a same-named skill is recorded only
  where a page states it (Copilot CLI, S028 `:456`).
- What the counter reads (Q31): `verifiers/check_command_files.py` reads the SKILL.md table's Client, Command files (first
  backticked span) and Action (word count only) cells, this table, the SOURCES rows and the lesson `## Gate`, and with
  `--fetch` the live page, and scans the base revision's blobs outside `.ufo/` for held tokens (new ground). It does not
  read the `What a file sets` cells or the list above; those are reviewer judgment, re-opened by the round's falsify seats
  (a mutant making Gemini's `prompt` optional still scores 6 of 6, `RerunC1Counter`).
