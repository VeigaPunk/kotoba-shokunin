Result: MIXED — Claude Code's "(project)", Cursor's "(project)", and opencode's two plural folders each omit a command location the client's docs still state; Codex, VS Code, Gemini CLI, and Copilot CLI scope cells match the pages opened.

Attacked the Command files scope cells of `SKILL.md` at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` (lines 113–119, confirmed with `git --no-optional-locks show`). No lane code was run. No tool was installed or updated. Fetched bytes are under `/fast/scratch/hyaku/kotoba-r58/ScoutUserFolders/fetch/`. Quotes below are contiguous source bytes, 25 words or fewer, no bytes stripped unless a line says so.

Cells under attack:

| Client | `SKILL.md` scope cell |
|---|---|
| Claude Code | `:113` `.claude/commands/` (project) |
| Codex | `:114` `~/.codex/prompts/` (user only; not shared through the repo) |
| VS Code | `:115` `.github/prompts` (workspace; user files in the profile) |
| Copilot CLI | `:116` no own folder: it loads Claude Code's `.claude/commands/` |
| Gemini CLI | `:117` `~/.gemini/commands/` (user; project `.gemini/commands/`) |
| Cursor | `:118` `.cursor/commands` (project) |
| opencode | `:119` `.opencode/commands/` (project; user `~/.config/opencode/commands/`) |

## Breaks

### Claude Code — "(project)" drops personal command files and added-directory loads

Pinned page S089 does not print the string `~/.claude/commands` (count 0 in the 114,542-byte fetch). It does print two other scopes the cell's "(project)" leaves out.

URL: `https://code.claude.com/docs/en/slash-commands.md`
`date -u`: `Fri 23 Oct 2026 08:26:07 AM UTC`
HTTP 200, 114,542 bytes, sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd`.

Line 190 (15 words):

```
Claude Code loads the skills in that directory's `.claude/skills/`, along with its `.claude/commands/` and `.claude/agents/`.
```

An added directory (`--add-dir` / `/add-dir`) loads that directory's `.claude/commands/`. The cell says project only. The same page's line 192 says that folder is not watched, so a session restart is required after an edit there. That is the same folder name in a third root, not a user home folder.

Line 276 (7 words):

```
personal skills or command files in `~/.claude/`
```

The pinned page places personal command files in `~/.claude/`. It does not spell the `commands/` segment on that line.

Line 745 (7 words, stops before the markdown link):

```
custom commands from user, project, plugin, or
```

The next bytes on that line are `[additional-directory](#skills-from-additional-directories) sources`. User is a named source, not only project.

Same host, current directory page, linked from the docs index (`https://code.claude.com/docs/llms.txt` line 19). Not the S089 URL.

URL: `https://code.claude.com/docs/en/claude-directory.md`
`date -u`: `Fri 23 Oct 2026 08:27:22 AM UTC`
HTTP 200, 28,637 bytes, sha256 `dcdaaf756a9596854e03cd5c9a4d0952e9806215eabfe92cd6328b0a1265ffc8`.
`~/.claude/commands` count on this page: 0.

Line 51 (10 words):

```
Global-scope files live in `~/.claude/` and apply across all projects.
```

Line 74, the file/scope cells (the row also says "Single-file prompts; same mechanism as skills"):

```
[`commands/*.md`](#ce-commands) | Project and global
```

[INFERENCE] Joining line 51 with line 74 gives global command files at `~/.claude/commands/*.md` and project files at `.claude/commands/*.md`. The page states both facts and never prints the joined token. The built-in commands page `https://code.claude.com/docs/en/commands.md` (same 08:27:22Z batch, HTTP 200, 54,225 bytes, sha256 `80164a5bc0d09cd44fef9d2d99d152a4fefae04adace1cdfba55d7448db7ed52`) has no `.claude/commands` path; it is the built-in command list.

L1 text, not a counter change: the "(project)" parenthetical should also say personal command files live under `~/.claude/` (S089 `:276`) and that `commands/*.md` is project and global (`claude-directory.md:51,74`), and that an added directory loads `.claude/commands/` (S089 `:190`). Do not cite `~/.claude/commands/` as a string the pinned page prints.

### Cursor — "(project)" omits user-level commands; no user directory path is printed

Pinned S094 and its supporting customize page name only `.cursor/commands`. They do not say "project". Current docs on the same host say slash commands exist at user level and workspace level, and they do not print a user command directory.

URL: `https://cursor.com/docs/skills.md`
`date -u`: `Fri 23 Oct 2026 08:27:22 AM UTC`
HTTP 200, 18,477 bytes, sha256 `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d`.

Line 323 (the whole line, 19 words):

```
- **Slash commands**: Both user-level and workspace-level commands are converted to skills with `disable-model-invocation: true`, preserving their explicit invocation behavior.
```

`~/.cursor/commands` count on this page: 0. Line 329 tells the reader to review generated skills in `.cursor/skills/`, which is the migration output, not the command folder.

Help page, same fact, HTML. URL: `https://cursor.com/help/customization/skills`
`date -u`: `Fri 23 Oct 2026 08:29:20 AM UTC`
HTTP 200, 181,908 bytes, sha256 `1fa1a626e791bb05f6b2a98e1d655d852913a8bb5b59de1f1dd170ade3001082`.
HTML line 39, text node after `</strong>`, no bytes stripped (10 words):

```
Both user-level and workspace-level commands, preserving their explicit invocation behavior.
```

`~/.cursor/commands` count in that help body: 0.

Pinned page, for contrast. URL: `https://cursor.com/docs/reference/deeplinks.md`
Same 08:26:07Z batch. HTTP 200, 5,972 bytes, sha256 `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4`.
Line 54 (13 words):

```
Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory.
```

Supporting `https://cursor.com/docs/customize-cursor.md` (same batch, HTTP 200, 5,200 bytes, sha256 `9ae0878d97465512ad29459f5406538ec7b427dfbaa39e1cc95d3deb447f363e`) line 31 calls commands markdown files and does not give a path. `.cursor/commands` count: 0.

Q30 for a printed user command directory, not for the user-level scope above:

- Changelog index `https://cursor.com/changelog` (08:29:01Z, HTTP 200, 204,106 bytes, sha256 `f1bb810497168fff3aa28afab07c4a0b3b1eeb9c069ca23ddaf782b18486d15a`): count of `.cursor/commands/` and `~/.cursor/commands` is 0.
- Changelog `https://cursor.com/changelog/1-6` (same batch, HTTP 200, 145,839 bytes, sha256 `8d2a8bcfbbd6f0d6a7e76cc4535106d5384a471564ba98e6cbe166be6a8f5152`). HTML line 2, tags not stripped; the path sits in a `<code>` element: `Commands are stored in .cursor/commands/[command].md`. No `~/.cursor/commands`. This URL is a changelog, so it is not a C1 source.
- Docs index `https://cursor.com/llms.txt` (08:27:22Z, HTTP 200, 24,815 bytes, sha256 `38cc4995af1037fea4daa16f4b2ed1062a4c21df63440e5703608eec1017085d`): customizing section lists customize, plugins, rules, skills, subagents, hooks, mcp. No custom-commands page. `https://cursor.com/docs/plugins.md` (08:29:01Z, HTTP 200, 20,323 bytes, sha256 `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62`): no `.cursor/commands`.
- Lane corpus grep for `~/.cursor/commands`: no hit.

The cell's "(project)" is a scope word the pinned page does not use, and it omits the user-level commands `skills.md:323` names. It does not omit a printed user folder path, because none of these pages print one. Do not write `~/.cursor/commands/` into the cell from this report.

### opencode — plural folders are right; legacy `command/` is still discovered and unnamed

Pinned S095 names both scopes the cell names, and one more directory name.

URL: `https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx`
`date -u`: `Fri 23 Oct 2026 08:26:07 AM UTC`
HTTP 200, 7,242 bytes, sha256 `dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11`.

Line 21 (10 words), matches the cell:

```
Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`.
```

Line 34 (8 words):

```
The legacy singular directories `command/` are also discovered,
```

Line 35 continues `but use `commands/` for new files.` Counts in this file: `command/` = 1, `.opencode/command/` = 0, `~/.config/opencode/command/` = 0, `.opencode/commands/` = 18, `~/.config/opencode/commands/` = 3. The page does not print the dotted singular paths. It does say the singular directories are still discovered. The cell names only the plural folders.

Line 252 is the same two scopes plus walk-up, not a third folder name (16 words):

```
Project sources take precedence over global sources, and nearer project sources take precedence over ancestor sources.
```

L1 text: keep both plural folders, and say legacy singular `command/` directories are still discovered (`commands.mdx:34-35`). Do not invent `.opencode/command/` as a printed token.

## Holds

### Codex — "user only; not shared through the repo" matches the page

URL: `https://learn.chatgpt.com/docs/custom-prompts.md`
Same 08:26:07Z batch. HTTP 200, 3,357 bytes, sha256 `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9`.

Line 10 (17 words):

```
live in your local Codex home directory (for example, `~/.codex`), so they're not shared through your repository.
```

Line 62 is the cell's folder: `~/.codex/prompts/`. No project `.codex/prompts` token on the page (the four `.codex/prompts` hits are all under `~/`).

Q30 before recording that no project prompt folder is documented:

- Docs index `https://learn.chatgpt.com/llms.txt` (saved as the redirect target of `https://developers.openai.com/codex/llms.txt`, 08:29:20Z, HTTP 200, 33,447 bytes, sha256 `fc7b20eaea56f8fe5dcc0280262009f9546172c521f69cb08b8befc89f03b943`). The only custom-prompt entry is `custom-prompts.md`, marked deprecated.
- Config reference, requested `https://developers.openai.com/codex/config-file/config-reference.md`, final `https://learn.chatgpt.com/docs/config-file/config-reference.md`. `date -u`: `Fri 23 Oct 2026 08:29:51 AM UTC`. HTTP 200, 136,297 bytes, sha256 `fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21`. Count of `.codex/prompts` and of `prompts/`: 0.
- `https://raw.githubusercontent.com/openai/codex/main/README.md` (08:29:01Z, HTTP 200, 3,334 bytes, sha256 `ba4e1f69ff48386e72a9c5e1edaf76aad64a475c2d51af79ccba6d1128261ba7`): no `prompts`.
- `https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md` (same batch, HTTP 200, 330 bytes, sha256 `c8458f99de91a4b4b9682ecb72c396f0d08c03c51a657759e1239c3a14c697d5`) points at GitHub releases and has no prompt directory. The releases HTML was not opened.
- Lane corpus `instruction-surface-census-round13.md:103` says omp loads `~/.codex/prompts` and `.codex/prompts/`. That is an omp loader line, not Codex documentation. It does not contradict the Codex page's "not shared through your repository."

### VS Code — workspace path plus profile user data, and no filesystem path to omit

URL: `https://code.visualstudio.com/docs/agent-customization/prompt-files.md`
Same 08:26:07Z batch. HTTP 200, 13,729 bytes, sha256 `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685`.

Line 25: `` `.github/prompts` folder ``
Line 26 (9 words):

```
Your user data (specific to your VS Code profile)
```

Line 28 says a user-level file is created with the Agent Customizations editor or **Chat: New Prompt File**. The page never prints `~/.config/Code/User/prompts` or any other user filesystem path. The cell's "user files in the profile" matches line 26. It does not omit a path the page names.

Overview `https://code.visualstudio.com/docs/agent-customization/overview.md` (08:29:20Z, HTTP 200, 18,157 bytes, sha256 `885f054a49d12863f0579de39e54ba0b0953de18e46a5a2e566d6cd46c0a4315`) line 98 sends user-level prompt locations back to this page, and lines 184–185 show `prompts/` only under the repo's `.github/` tree. Parent-repo discovery (`prompt-files.md:31`, overview `:170-174`) is still that `.github/prompts` folder, not a second path.

Release notes: requested `https://code.visualstudio.com/updates`, final `https://code.visualstudio.com/updates/v1_143` (08:29:01Z, HTTP 200, 109,694 bytes, sha256 `82cc7101cf08eaac134c642f4ebcb676c94a1ed470ca6f8b686cc2966c0145b9`). No match for `.github/prompts`, `prompt file`, or `User/prompts`. Older release notes were not opened. Lane corpus has `.github/prompts` only as the VS Code workspace path already in the cell.

### Gemini CLI — both folders in the cell are the two the page names

URL: `https://geminicli.com/docs/cli/custom-commands.md`
Same 08:26:07Z batch. HTTP 200, 12,129 bytes, sha256 `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872`.

Line 10: `Gemini CLI discovers commands from two locations, loaded in a specific order:`
Line 12 names `~/.gemini/commands/`.
Line 15, after four leading spaces (7 words):

```
`<your-project-root>/.gemini/commands/`. These commands are specific to the
```

The cell's parenthetical `.gemini/commands/` drops the page's `<your-project-root>/` prefix. That is the same project-root relative folder the other rows use, not a different directory. `https://geminicli.com/docs/llms.txt` returned HTTP 404 at 08:29:01Z. An extensions `commands/` directory is not on this page; this page says two locations, and the cell names both.

### Copilot CLI — no user or project command folder of its own

Pinned S028. URL: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md`
Same 08:26:07Z batch. HTTP 200, 47,200 bytes, sha256 `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0`.

Line 456 (6 words inside the diagram):

```
then commands (.claude/commands/), skills override commands
```

`~/.copilot/commands` and `~/.claude/commands` counts on this page: 0. Line 159's `com.github.copilot/commands/` is the plugin component directory, not a user or project command folder. The cell's "no own folder" holds for those two scopes.

Command reference, not S028. URL: `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md`
08:29:01Z, HTTP 200, 461,944 bytes, sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9`.
Line 1334 (13 words):

```
Commands are an alternative to skills stored as individual `.md` files in `.claude/commands/`.
```

Same Claude Code path. No second folder on that line. The CLI docs tree walk already recorded in `.ufo/waves/round-58/build/ScoutCopilotPrompts.md` was not repeated here.

## Fetch times

```
Fri 23 Oct 2026 08:26:07 AM UTC
Fri 23 Oct 2026 08:27:22 AM UTC
Fri 23 Oct 2026 08:29:01 AM UTC
Fri 23 Oct 2026 08:29:20 AM UTC
Fri 23 Oct 2026 08:29:51 AM UTC
```
