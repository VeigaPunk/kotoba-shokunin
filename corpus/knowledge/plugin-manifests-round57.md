---
source: S079 https://code.claude.com/docs/en/plugins-reference.md; S080 https://developers.openai.com/plugins/build/plugins.md; S081 https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md; S082 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md; S083 https://geminicli.com/docs/extensions/reference.md; S084 https://cursor.com/docs/plugins.md; S085 https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch
---

# Plugin manifests by client (round 57)

A skill, agent, command or rule file can reach a client inside a plugin (Gemini CLI: an extension) instead of from the
project tree. Before auditing such a file, find the plugin it came from and its manifest. This entry records, from each
client's own documentation opened on 2026-10-23, where that manifest lives and what a plugin can ship. It is vendor
documentation, not a runtime measurement: no client was run.

**Row rule (applied to every row the same way).** The manifest cell leads with the client's own-format manifest path —
a path whose folder or file name names the client — and, where the client documents none, with the default manifest
its page names. Seven clients, one rule: Claude Code, Codex, Gemini CLI and Cursor document an own-format path; VS Code
and Copilot CLI default to the shared Agent Plugins root `plugin.json`; opencode plugins are code modules with no JSON
manifest. The rule was fixed when the source seats returned (after the counter was frozen) and it does not choose
between paths to raise a count: VS Code's Legacy OpenPlugin `.plugin/plugin.json` would pass the counter and is not used
(`.ufo/waves/round-57/build/CriticC1Rows.md`, `SrcVSCode.md`).

| Client | Manifest | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` | S079 | "Save the manifest at `.claude-plugin/plugin.json` under the plugin root." |
| Codex | `.codex-plugin/plugin.json` | S080 | "The plugin-creator skill will create the plugin folder, create a supported `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring for the plugin." |
| VS Code | `plugin.json` | S081 | "A root `plugin.json` that declares the canonical Agent Plugins `$schema` uses Agent Plugins semantics." |
| Copilot CLI | `plugin.json` | S082 | "Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory." |
| Gemini CLI | `gemini-extension.json` | S083 | "Each extension must have a `gemini-extension.json` file in its root directory." |
| Cursor | `.cursor-plugin/plugin.json` | S084 | "plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and" |
| opencode | `.opencode/plugins/` | S085 | "Plugins under `.opencode/plugins/` are loaded automatically, like the local example above." |

Quote locations (fetched bytes, seat reports under `.ufo/waves/round-57/build/`): S079 `plugins-reference.md:34`; S080
`build-plugins.md:135-137` (line breaks folded to spaces); S081 `agent-plugin-reference.md:97`; S082
`plugins-creating.md` step 2 (the list number `2. ` is not quoted); S083 `extensions-reference.md:106-107` (one line
break folded); S084 `plugins.md:28`, a contiguous substring (the list marker and bold label before it and the link
after it are not quoted); S085 `index.mdx:21`.

## What a plugin can ship

| Client | Instruction-bearing parts a plugin can ship | Source lines |
|---|---|---|
| Claude Code | skills, Markdown commands and agents, hooks, MCP and LSP server configurations, output styles; the manifest is optional and every other file sits at the plugin root, not inside `.claude-plugin/` | S079 `plugins-reference.md:34-36,611-629` |
| Codex | skills under `skills/`, MCP servers through `mcp.json` (the scaffold writes `.mcp.json`), lifecycle hooks for manually installed desktop plugins, assets; portable packages put `plugin.json` at the root and `.codex-plugin/plugin.json` stays supported as a compatibility fallback | S080 `build-plugins.md:14-30,52-89` |
| VS Code | portable skills and MCP servers; client-specific agents, hooks, automation templates and slash commands; agents, commands, rules and hooks read from `com.github.copilot`; formats auto-detected (Agent Plugins 1.0 and Copilot root `plugin.json`, Claude `.claude-plugin/plugin.json`, Legacy OpenPlugin `.plugin/plugin.json`) | S081 `agent-plugin-reference.md:11-22,73-85,97-104` |
| Copilot CLI | agents, skills, hooks, MCP server configurations; Agent Plugins 1.0 adds Copilot-specific commands, rules and LSP servers | S082 `plugins-creating.md:14-21,48-71` |
| Gemini CLI | MCP servers, a context file (`contextFileName`), TOML commands, hooks (in `hooks/hooks.json`, not in the manifest), skills, sub-agents, policy rules | S083 `extensions-reference.md:104-112,146-161,229-269` |
| Cursor | Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks; Agent Plugins (root `plugin.json`): skills and MCP servers | S084 `plugins.md:9-30` |
| opencode | a JavaScript/TypeScript module that registers agents, commands, MCP configuration, skills, tools and runtime hooks in code; a published package carries a `package.json` | S085 `index.mdx:10-22,214-235,414-445,610-627,865-892,1768-1786` |

## Findings

- Four of seven clients document an own-format manifest path (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`,
  `gemini-extension.json`, `.cursor-plugin/plugin.json`). VS Code, Copilot CLI, Codex and Cursor also read the shared
  Agent Plugins root `plugin.json`, so a root `plugin.json` alone does not tell which client a plugin targets.
- One package can serve several clients at once: VS Code reads Claude's format (S081 `:103`), and the host inventory
  found plugins shipping `.claude-plugin`, `.codex-plugin` and `.cursor-plugin` side by side
  (`.ufo/waves/round-57/build/ScoutPluginSweep.md`, host observation, not a documented rule).
- A plugin-shipped MCP server is still a server configuration, so the round-52 `instructions` records apply to it
  unchanged (`corpus/knowledge/mcp-server-instructions-round52.md`); a plugin-shipped agent uses the client's agent
  format from `corpus/knowledge/agent-definition-files-round56.md`, but the client may ignore some keys inside a
  plugin (`.ufo/waves/round-57/build/ScoutPluginMcp.md`, reviewer reading).
- Gemini CLI's context file makes an extension an always-on instruction surface, which the always-on checklist covers
  once the file is found (`corpus/knowledge/alwayson-rule-files-round53.md`).

## Limits

- What `verifiers/check_plugin_manifests.py` checks (Q31): per client, the SKILL.md row token's shape (a `.json` final
  segment carrying `plugin`/`extension`, at least two segments or the client's own name, no dotted folder, no
  `marketplace`, no other client's name), the entry row's manifest cell equal to that token, a 6–25-word quote that
  holds the token and a plugin/extension word outside it, a new tier-A `mined` SOURCES row opened 2026-10-23 on the
  client's pinned host that is not a base URL or a change note, the quote in `corpus/lessons/round-57.md` § Gate, and
  with `--fetch` the quote and the token on the live page; new ground counts tokens held nowhere in the base tree
  outside `.ufo/`. It does not check the `What a plugin can ship` cells, the row rule above, or whether a client loads
  a plugin as documented; those are reviewer judgment.
- Copilot CLI's legacy manifest locations are listed on the CLI plugin reference page, which is base row S028; this
  entry does not re-cite it.
- opencode: "no JSON manifest" is read from the pinned V2 build guide and its sweep in `Srcopencode.md` (docs tree,
  changelog, lane corpus); a `package.json` describes a published package, not a plugin-specific manifest.
- omp, this host's harness, also reads plugin manifests (`.omp-plugin/plugin.json`, then `.claude-plugin/plugin.json`);
  that is binary evidence (`ScoutPluginSweep.md`), not a documented source, and omp is not one of the seven rows.
