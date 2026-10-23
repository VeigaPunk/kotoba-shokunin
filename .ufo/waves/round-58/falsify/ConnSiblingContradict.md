Result: HOLDS — no sibling lane states a command-file folder, precedence, or format that contradicts the landed SKILL.md "Custom command files by client" table at 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe; the only C1-relevant hits (six in game-dev-3d-shokunin) are descriptive and agree.

# Adjacency attack — sibling command-file claims vs landed SKILL table

Lane: kotoba-shokunin (read-only). Base/landed rev under attack: `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`. Sibling scan read-only across `/home/vgpnk/Projects/shokunin/*-shokunin` excluding kotoba-shokunin. Reference build report: `.ufo/waves/round-58/build/ConnSiblingCommands.md`.

## Landed table attacked (SKILL.md § Custom command files by client)

| Client | Folder (landed) | Format/pre (landed) |
|---|---|---|
| Claude Code | `.claude/commands/` (project) | Markdown; skill frontmatter except `name`/`paths`; `argument-hint`, named `$name` |
| Codex | `~/.codex/prompts/` (user only) | Markdown; `description`, `argument-hint`; `$1`–`$9`, `$ARGUMENTS` |
| VS Code | `.github/prompts` (workspace; user in profile) | `.prompt.md`; `description`, `name`, `argument-hint`, `agent`, `model`, `tools`; `${input:…}` |
| Copilot CLI | none own; loads Claude Code's `.claude/commands/`; skills override commands | as Claude Code |
| Gemini CLI | `~/.gemini/commands/` (user; project `.gemini/commands/`) | TOML `.toml`; required `prompt`, optional `description`; path→name, subfolders→`:`; `{{args}}` |
| Cursor | `.cursor/commands` (project) | Markdown workflow prompt; no frontmatter/argument schema documented |
| opencode | `.opencode/commands/` (project; user `~/.config/opencode/commands/`) | `.md` only; nested path→`/`-separated name; optional YAML frontmatter; trimmed body template; `$ARGUMENTS` |

## Method

1. `git --no-optional-locks grep -n -I -F` for each of the six path patterns (`.claude/commands`, `.gemini/commands`, `.cursor/commands`, `.opencode/command` singular as task spelling, `.codex/prompts`, `.github/prompts`) across all 20 sibling lanes (tracked files).
2. Province ownership: `grep -qiE 'command file|slash command|custom command|prompt file|\.claude/commands|\.codex/prompts|\.github/prompts'` in each sibling `PROVINCE.md`.
3. Broader adjacency checks: regex co-occurrence of client names with command/prompt across siblings; `override` + command; `skills override`/`commands override`; command/prompt directory/folder terms; `Custom command files`/`command files` phrases; opencode binary string inspection for `command` vs `commands`.

Commands (representative, exit 0 unless noted):
- `for d in *-shokunin; do git -C "$d" grep -I -n -F '.claude/commands' ...; done` → only `game-dev-3d-shokunin`: 6 hits.
- `for d in *-shokunin; do git -C "$d" grep -I -l -F 'Custom command files' ...; done` → no output (exit 1, expected no matches).
- `for d in *-shokunin; do grep -qiE ... "$d/PROVINCE.md"; done` → no province matches.
- `strings .../opencode-linux-x64/bin/opencode | grep -iE '\.opencode/command'` → no singular directory; binary contains `.opencode/commands` (plural), agreeing with S095/landed table.

## Hits (per hit: agree / contradict)

All six C1-relevant hits are in `game-dev-3d-shokunin` (HEAD `89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080`), all descriptive (Kimi reverse-engineering of Claude Code import sources / out-of-scope markers), none redefine a folder, precedence, or format.

| # | file:line | excerpt (as fetched) | Verdict |
|---|---|---|---|
| 1 | `corpus/knowledge/unreal-mcp/adaptation-kimi.md:230` | `` `~/.claude/AGENTS.md`, `~/.claude/CLAUDE.md`, `~/.claude/skills/`, `~/.claude/commands/` and `~/.claude.json` — listed as import sources for Kimi `/import-from-cc-codex`, not live config. `` | **agree** — treats `.claude/commands/` as an existing Claude Code surface (user-level import source), consistent with census ELIGIBLE `.claude/commands/`; does not deny or redefine the project-level folder in the landed table. |
| 2 | `reports/round-101/probes/kimi-surfaces.md:559` | `` `.claude/commands/**` as out of scope. `` (importer skill explicitly lists it out of scope) | **agree** — acknowledges the path as a Claude Code surface; no contradiction. |
| 3 | `reports/round-101/r101-distiller.md:560` | `` ~/.agents/skills/  ~/.claude/AGENTS.md  ~/.claude/CLAUDE.md  ~/.claude/commands/ `` (extracted path list) | **agree** — same descriptive import-source set; no folder/preceence/format claim. |
| 4 | `reports/round-102/kimi-surfaces.md:114` | `` `.claude/AGENTS.md`, `.claude/CLAUDE.md`, `.claude/skills`, `.claude/commands` and `.claude.json` (3 hits) — import sources, not live config. `` | **agree** — explicitly labels them import sources, not live config; no contradiction with Claude Code row. |
| 5 | `reports/round-104/gate/scratch/c85a816/corpus/knowledge/unreal-mcp/adaptation-kimi.md:230` | duplicate of hit 1 inside a scratch copy | **agree** — duplicate of a descriptive hit; no new claim. |
| 6 | `reports/round-107/r107-kimi-adapt.md:207` | `` `.claude/skills` ×6, `.claude/commands` ×4, `.agents/skills` ×3 — the `.claude/*` paths are import sources. `` | **agree** — counts them as import sources; consistent with census. |

## Non-C1 "command"/"prompt" hits

The generic phrase hits enumerated in `ConnSiblingCommands.md` (prompt file, custom command, slash command) were re-checked at the file level. They refer to unrelated topics (fleet dispatch prompts, Docker/kitty custom commands, Kimi in-TUI slash commands, opencode config keys). None states a client command-file folder, precedence, or format. In particular:
- `kagi-shokunin`'s `~/.config/opencode/command/` (singular) appears only as a census child / config-layering probe target, not as a claim that opencode's command-file folder is singular; the opencode 1.19.4 binary exposes `.opencode/commands` (plural), matching S095 and the landed table. No contradiction.
- `kumitate-shokunin` S007 references Codex CLI developer commands at `~/.codex/config.toml` (MCP registration), consistent with Codex being a `~/.codex/` surface; it does not redefine `~/.codex/prompts/`.
- No sibling `PROVINCE.md` claims command-file / slash-command / custom-command ground.

## Affected axes

- Depth/adjacency (C1): no contradiction found; the landed table's seven rows are not challenged by sibling lanes.
- No effect on frozen counter `python3 -B verifiers/check_command_files.py --rev <rev> --fetch` (F ≥ 4, G ≥ 3); no counter, rule, or target was changed or proposed to change.

## Proposed move

No integration change required from adjacency. L1 may note in the round-58 integration record that the six game-dev-3d hits were re-verified as descriptive (import-source/out-of-scope) and agree with the census; no SKILL.md table edit, no SOURCES row change, and no routed repair is warranted from this seat. If L1 wants a defensive citation, add a one-line note in `corpus/knowledge/command-files-round58.md` (reviewer-owned) that sibling lanes reference `.claude/commands/` only as Kimi import sources, not as a normative client folder — but this is optional and does not affect C1.

## Risks

- Scan covered tracked files only (matching the build report's method). Untracked/scratch copies (e.g. `reports/round-104/gate/scratch/...`) were included only where tracked; they duplicated existing hits and introduced no new claims.
- Future sibling edits could introduce a command-file claim; re-run this scan before final C1 integration if any sibling lane changes command-related content.
- Generic-phrase hits were classified by context; a lane could hide a command-folder claim under an unrelated heading. The broader client+command co-occurrence and override checks above found none beyond the six listed.

## Verification

- `git --no-optional-locks grep` (six path patterns, 20 sibling lanes) → only the six hits listed; exit 0 for the grep invocations that found matches, exit 1 (no matches) for the other five patterns.
- Province grep across 20 sibling `PROVINCE.md` → no matches.
- `strings .../opencode-linux-x64/bin/opencode | grep '\.opencode/command'` → no singular directory; plural `.opencode/commands` present.
- No lane files were modified; no git writes performed in any lane. Report written only at the assigned path.