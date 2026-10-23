source: S072 (https://code.claude.com/docs/en/agent-sdk/subagents.md, `sdk-subagents.md:17`), S073 (https://developers.openai.com/codex/subagents.md, `subagents.md:341-343`), S074 (https://code.visualstudio.com/docs/agent-customization/custom-agents.md, `custom-agents.md:63`), S075 (https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md, `create-custom-agents-for-cli.md:23-25`), S076 (https://geminicli.com/docs/core/subagents.md, `subagents.md:324`), S077 (https://cursor.com/docs/subagents.md, `subagents.md:427`), S078 (anomalyco/opencode `agents.mdx` at `4e0bc522`, `:41-44`); schema detail for Claude Code from S026 (base row)
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch

# Agent-definition files by client (round 56)

Where seven clients' own documentation says their agent-definition files (subagents, custom agents) live, and
what such a file sets. Every row quotes a page opened on 2026-10-23 in round 56 (`../SOURCES.md` S072–S078; fetch
records in `../lessons/round-56.md` § Gate and the seat reports `../../.ufo/waves/round-56/build/Src*.md`). These
are documentation statements, not measured client behaviour: no client was run to see which file it loads.

Why the lane needs it: `../../SKILL.md` § Agent-definition fidelity checklist was written for opencode files
(`opencode/agents/*.md`, opencode's `agent` map and `subagents:` rosters). Applying its boxes to another client's
file applies the wrong schema — Cursor makes `name` optional and derives it from the file name, Codex files are not
Markdown at all.

## Per-client record

| Client | Location | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude/agents/` | S072 | "**Filesystem-based**: define agents as markdown files in `.claude/agents/` directories." |
| Codex | `.codex/agents/` | S073 | "To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents." |
| VS Code | `.github/agents` | S074 | "For example, save this planning agent as `.github/agents/planner.agent.md`. It uses read-only tools to research a task and return a plan:" |
| Copilot CLI | `.github/agents/` | S075 | "Choose between the options to create the custom agent in the repository or in your home directory: Project (`.github/agents/`)" |
| Gemini CLI | `.gemini/agents/*.md` | S076 | "2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)" |
| Cursor | `.cursor/agents/` | S077 | "You can also create subagents manually by adding markdown files to `.cursor/agents/` (project) or `~/.cursor/agents/` (user)." |
| opencode | `.opencode/agents` | S078 | "A nested path becomes part of the agent ID: text .opencode/agents/team/reviewer.md → team/reviewer" |

Quote notes: S072 is the Agent SDK page, which points back to Claude Code's filesystem definitions; the schema
detail (`name`, `description`, `tools`, `model`) is from the base row S026 (`SrcClaudeCode`, `CriticC1Rows`). S073's
URL redirects to `learn.chatgpt.com/docs/agent-configuration/subagents.md` (a pinned Codex host). S076's quote is
the user-level line; the project-level line `.gemini/agents/*.md` is the line before it (`subagents.md:323`) and
holds no agent word. S078's quote is the body of a fenced example whose info string `text` stays in the quote; the
fence markers were removed (`Srcopencode`).

## Findings

1. **Two shared folders, one format split.** VS Code and Copilot CLI both use `.github/agents/` in the repository and
   `~/.copilot/agents/` for the user (S074, S075); Copilot CLI uses the personal profile when both define the same ID
   (S075). Codex alone uses standalone TOML with required `name`, `description` and `developer_instructions` (S073);
   the other six use Markdown, with YAML frontmatter where the page names one.
2. **Compatibility reads are not ownership.** Cursor also reads `.claude/agents/` and `.codex/agents/` (S077
   `subagents.md:84-92`, its own files win name conflicts), and VS Code lists `.claude/agents` as a workspace
   location in Claude format (S074 `custom-agents.md:123-126`). A row names each client's own folder; a
   compatibility folder belongs to the client that defines it.
3. **Required keys differ.** Claude Code requires `name` and `description` (S026); Gemini CLI requires both (S076);
   Copilot CLI requires `description` and makes `name` optional (S075); Cursor lists every field as optional and
   derives `name` from the file name (S077); opencode states no required key (S078).
4. **Tool limits use different keys.** `tools` (Claude Code, VS Code, Copilot CLI, Gemini CLI), `readonly`
   (Cursor), `permissions` (opencode V2, which drops the legacy `tools` key), `features.*` switches (Codex).
5. **Location history (seat `ScoutChangelogSweep`, not SOURCES rows).** opencode moved its folders from `agent/` to
   `agents/` on 2026-01-17 and still loads the singular form; VS Code renamed chat modes (`.github/chatmodes`,
   `.chatmode.md`) to custom agents in release 1.106; Copilot CLI moved its user folder from
   `~/.config/copilot/agents/` to `~/.copilot/agents/` on 2026-03-02.

## Limits

- `verifiers/check_agent_definitions.py --rev <rev> --fetch` (v1.3, errata 1–3 in `../../plans/round-56.md`) checks
  only: the first table under `### Agent-definition files by client` (header, one row per client, the first
  backticked location token, its `agent`/`agents` segment, that it sits under the client's own configuration
  directory, and an Action of at least three words); this entry's table (one `S###`, a 3–25-word quote holding the
  token and an agent word outside it); the cited SOURCES row (new id, `docs` kind, tier A, `mined`, opened
  2026-10-22 or 2026-10-23, pinned host, not a base or tracker URL); the quote in the lesson Gate; and, with
  `--fetch`, the quote and the token on the live page, after redirects, on a pinned host. New ground counts distinct
  normalised locations with no case-insensitive occurrence in the base tree outside `.ufo/`.
- It does not check the `What the file sets` cells, the Findings above, whether a client loads any of these files,
  or clients outside the seven. Those are reviewer readings of the cited pages.
- The base-text count is case-insensitive, so `.claude/agents` and `.codex/agents` count as held partly because the
  base text holds `.claude/AGENTS.md` and `.codex/AGENTS.md` (`ScoutHeldAgentDefs`); this only makes new ground
  harder to reach.
- On this host `~/.config/opencode/agents/` does not exist (`C2RedesignTruth`, `ScoutHostClients`), although
  `../../SKILL.md` § Sources still describes 18 files there; that statement is stale and is routed, not changed here.
