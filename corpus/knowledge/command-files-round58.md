---
source: S089 https://code.claude.com/docs/en/slash-commands.md; S090 https://learn.chatgpt.com/docs/custom-prompts.md; S091 https://code.visualstudio.com/docs/agent-customization/prompt-files.md; S093 https://geminicli.com/docs/cli/custom-commands.md; S094 https://cursor.com/docs/reference/deeplinks.md; S095 https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx; S028 (re-opened) https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_command_files.py --rev <rev> --fetch
---

# Custom command files by client (round 58)

A custom command (VS Code: a prompt file; Codex: a custom prompt) is a file the user writes once and invokes by typing
`/name`. It is a different instruction surface from a skill: the model does not choose it from a description, the user
types it. Before auditing one, find the folder the client reads and what a file in it may set. This entry records, from
each client's own documentation opened on 2026-10-23, where that folder is and what a file sets. It is vendor
documentation, not a runtime measurement: no client was run.

Three clients point authors from command files to skills: Claude Code calls `.claude/commands/` files "the older format"
that "still works" (S089 `slash-commands.md:172`); Codex marks custom prompts deprecated in favour of skills (S090
`custom-prompts.md:5-8`); VS Code prompt files run only in Local harness sessions, and its page sends reusable workflows
for other harnesses to an agent skill (S091 `prompt-files.md:17`). Copilot CLI documents no command folder of its own:
its plugin reference loads Claude Code's folder and lets skills override it — "then commands (.claude/commands/), skills
override commands" (S028 `cli-plugin-reference.md:456`, re-opened this round); a CLI plugin's `com.github.copilot/commands/`
namespace is a plugin path, not a user folder (W0 `CensusCopilotCLI`).

**Row rule (applied to every row the same way).** The Command files cell leads with the folder (or file pattern) the
client's own page names for user-written command or prompt files — the project folder where both a project and a user
folder exist, else the only one documented — and the quote is the page's own sentence naming it. The rule and the
targets were frozen before any row was written (`plans/round-58.md` § C1, census before targets). Codex's and VS Code's
folders were already named in this corpus (`instruction-surface-census-round13.md`), so they are not new ground.
Quote notes: every quote is copied from the fetched bytes; the VS Code quote spans a Markdown table
(`prompt-files.md:21-25`), so its table pipes are written as `&#124;` to keep them inside one cell — no other byte is
changed; the Gemini CLI quote keeps the page's list marker `1.` and bold markers; the opencode quote is from the pinned
docs source because the served page is HTML without `Accept: text/markdown`.

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
  variables (`:69-70`); user-level files live in the profile folder.
- **Gemini CLI** (S093): TOML files with the `.toml` extension (`:41-42`); required `prompt`, optional `description`;
  the path under `commands/` names the command and subfolders make `:` namespaces (`:25-27`); `{{args}}` substitutes
  what follows the command (`:58-67`); a project `.gemini/commands/` sits beside the user folder (`:8-17`).
- **Cursor** (S094): Markdown files in the project folder (`customize-cursor.md:31`, supporting page in the S094 row);
  no frontmatter or argument schema is documented on these pages.
- **opencode** (S095): only `.md` files are discovered and nested paths become `/`-separated names (`:28`); optional YAML
  frontmatter, and the trimmed body is the prompt template (`:37`); `$ARGUMENTS` is the whole argument string (`:99`);
  the user folder is `~/.config/opencode/commands/` (`:21`).

## Limits

- Vendor documentation only; no client was run, so precedence between a command and a same-named skill is recorded only
  where a page states it (Copilot CLI, S028 `:456`).
- What the counter reads (Q31): `verifiers/check_command_files.py` reads the SKILL.md table's Client, Command files (first
  backticked span) and Action (word count only) cells, this table, the SOURCES rows and the lesson `## Gate`, and with
  `--fetch` the live page. It does not read the `What a file sets` cells or the list above; those are reviewer judgment,
  re-opened by the round's falsify seats.
