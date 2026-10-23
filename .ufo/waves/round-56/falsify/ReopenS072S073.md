Result: MIXED — S072 and S073 resolve live with byte-identical hashes (`5b7aa6c6…`, `e7469d41…`) and verbatim Gate quotes (`S072.md:17`, `S073.md:341-343`), but the Claude Code schema citation to base row `S026` exceeds `S026`'s recorded `SOURCES.md` scope/anchors/used-by (while live `sub-agents.md` has drifted to `111,624 B` / `84b2646c…`) and Codex's `features.*` cells (`SKILL.md:104`, `agent-definition-files-round56.md:49-50`) are wider than `S073.md:346-348,400-409`.

## 1. Live Fetch Receipts (`S072`, `S073`, and base schema page `S026`)

Command executed (exit code `0`):

```text
$ mkdir -p /fast/scratch/hyaku/kotoba-r56/ReopenS072S073 && date -u +"%Y-%m-%dT%H:%M:%SZ" && curl -sSL -D /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S072.headers -o /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S072.md -w "HTTP %{http_code} | effective_url: %{url_effective} | bytes: %{size_download}\n" "https://code.claude.com/docs/en/agent-sdk/subagents.md" && sha256sum /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S072.md && wc -c /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S072.md && date -u +"%Y-%m-%dT%H:%M:%SZ" && curl -sSL -D /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S073.headers -o /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S073.md -w "HTTP %{http_code} | effective_url: %{url_effective} | bytes: %{size_download}\n" "https://developers.openai.com/codex/subagents.md" && sha256sum /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S073.md && wc -c /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S073.md && date -u +"%Y-%m-%dT%H:%M:%SZ" && curl -sSL -D /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S026.headers -o /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S026.md -w "HTTP %{http_code} | effective_url: %{url_effective} | bytes: %{size_download}\n" "https://code.claude.com/docs/en/sub-agents.md" && sha256sum /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S026.md && wc -c /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S026.md
2026-10-23T03:07:28Z
HTTP 200 | effective_url: https://code.claude.com/docs/en/agent-sdk/subagents.md | bytes: 41461
5b7aa6c66705f223744ac58acd69b7629d4ccd23c56655678c975b22f9711315  /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S072.md
41461 /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S072.md
2026-10-23T03:07:29Z
HTTP 200 | effective_url: https://learn.chatgpt.com/docs/agent-configuration/subagents.md | bytes: 22907
e7469d41c5a18a4ee66ee40ca4a9a2617a697e42554a0198ac4481e1e597357f  /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S073.md
22907 /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S073.md
2026-10-23T03:07:29Z
HTTP 200 | effective_url: https://code.claude.com/docs/en/sub-agents.md | bytes: 111624
84b2646c513754ef5f33c6f5a0d7f59960021a65b5a09c35b9158fa116a73d5a  /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S026.md
111624 /fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S026.md
```

| Row | Requested URL | Effective URL (HTTP status chain) | UTC access (`date -u`) | Bytes | SHA-256 | Matches `SOURCES.md` & `round-56.md` § Gate? |
|---|---|---|---|---|---|---|
| S072 | `https://code.claude.com/docs/en/agent-sdk/subagents.md` | `https://code.claude.com/docs/en/agent-sdk/subagents.md` (`HTTP/2 200`) | `2026-10-23T03:07:28Z` | `41,461` | `5b7aa6c66705f223744ac58acd69b7629d4ccd23c56655678c975b22f9711315` | Yes — identical to `corpus/SOURCES.md:85` and `corpus/lessons/round-56.md:14` |
| S073 | `https://developers.openai.com/codex/subagents.md` | `https://learn.chatgpt.com/docs/agent-configuration/subagents.md` (`HTTP/2 308` → `HTTP/2 200`) | `2026-10-23T03:07:29Z` | `22,907` | `e7469d41c5a18a4ee66ee40ca4a9a2617a697e42554a0198ac4481e1e597357f` | Yes — identical to `corpus/SOURCES.md:86` and `corpus/lessons/round-56.md:15` |
| S026 (base schema source) | `https://code.claude.com/docs/en/sub-agents.md` | `https://code.claude.com/docs/en/sub-agents.md` (`HTTP/2 200`) | `2026-10-23T03:07:29Z` | `111,624` | `84b2646c513754ef5f33c6f5a0d7f59960021a65b5a09c35b9158fa116a73d5a` | Drifted from `corpus/SOURCES.md:39` (`110,784 B`, sha256 `89aa73eb…`, fetched `2026-10-22T12:28:30Z`) |

## 2. Verbatim Gate Quote Verification

1. **S072 (`corpus/lessons/round-56.md:14`, `corpus/knowledge/agent-definition-files-round56.md:21`)**:
   - Recorded quote (8 words): `"**Filesystem-based**: define agents as markdown files in `.claude/agents/` directories."`
   - Observed in `/fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S072.md:17`:
     `* **Filesystem-based**: define agents as markdown files in `.claude/agents/` directories. See [defining subagents as files](/docs/en/sub-agents.md)`
   - Verdict: **HOLDS.** Byte-exact contiguous substring at `S072.md:17` (no Markdown stripped).

2. **S073 (`corpus/lessons/round-56.md:15`, `corpus/knowledge/agent-definition-files-round56.md:22`)**:
   - Recorded quote (20 words): `"To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents."`
   - Observed in `/fast/scratch/hyaku/kotoba-r56/ReopenS072S073/S073.md:341-343`:
     - Line 341: `To define your own custom agents, add standalone TOML files under`
     - Line 342: `` `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped ``
     - Line 343: `agents.`
   - Verdict: **HOLDS with line-wrap folding.** Exact words and backticks at `S073.md:341-343` with the two hard line breaks (`\n`) joined by single spaces (see Finding F3 below on disclosure in `Quote notes:`).

## 3. Attacks and Findings (Cells Wider Than Their Cited Row or Page)

### Finding F1 — Claude Code schema claims cite base row `S026`, but `corpus/SOURCES.md:39` (`S026`) is narrower than the cited schema and was not updated (`SKILL.md:103`, `corpus/knowledge/agent-definition-files-round56.md:1,29-30,46`, `corpus/SOURCES.md:39,85`)

- **Target lines**:
  - `SKILL.md:103`: `| Claude Code | .claude/agents/ (user ~/.claude/agents/) | Markdown with YAML frontmatter, body is the system prompt; name and description required; tools allowlist; optional model (schema: S026) | Write project subagents here and check keys against Claude Code's schema, not the opencode checklist |`
  - `corpus/knowledge/agent-definition-files-round56.md:1,29-30,46`: `schema detail for Claude Code from S026 (base row)`; `the schema detail (name, description, tools, model) is from the base row S026`; `3. **Required keys differ.** Claude Code requires name and description (S026)`
  - `corpus/SOURCES.md:39` (row `S026`) and `corpus/SOURCES.md:85` (row `S072`)
- **Counterexample & evidence**:
  1. **S072 (`S072.md`) does not document the filesystem Markdown schema**: `S072.md:141-160` (`### AgentDefinition configuration`) documents the **programmatic SDK** `AgentDefinition` object, where `description` (`:145`) and `prompt` (`:146`) are the required fields and `name` is not a field at all (the dictionary key names the agent at `:52-53,101-102`). For filesystem definitions (`S072.md:172-174,734-744`), `S072.md:744` defers the file schema to `/docs/en/sub-agents.md#write-subagent-files`. In addition, while `S072.md:736` does document the user path `~/.claude/agents/` (`"Claude Code watches ~/.claude/agents/ and .claude/agents/ and picks up a new or edited agent file within a few seconds"`), `corpus/SOURCES.md:85` (row S072) anchors only `§ Overview, sdk-subagents.md:14-18`, which mentions only `.claude/agents/`.
  2. **The live `sub-agents.md` page (`S026.md`) supports the schema cells, but the `SOURCES.md:39` row `S026` does not**:
     - On live `S026.md` (`111,624 B`, sha256 `84b2646c…`), the schema claims hold:
       - `S026.md:94`: `"Subagents are Markdown files with YAML frontmatter."`
       - `S026.md:162-163`: `| .claude/agents/ | Current project | 3 |` and `| ~/.claude/agents/ | All your projects | 4 |`
       - `S026.md:242`: `"Subagent files use YAML frontmatter for configuration, followed by the system prompt in Markdown:"`
       - `S026.md:289`: `"Only name and description are required."` (also table rows `:298` `name | Yes`, `:299` `description | Yes`, `:300` `tools | No`, `:302` `model | No`; note `:341` carves out plugin subagents: `"A plugin subagent whose frontmatter has no name or doesn't parse still loads, under its filename."`)
       - `S026.md:349`: `"The model field controls which model the subagent uses:"`
       - `S026.md:446`: `"To restrict tools, use the tools field as an allowlist or the disallowedTools field as a denylist."`
     - However, in `corpus/SOURCES.md:39`, row `S026`'s `scope` (`Claude Code's documented delegation rule for subagents ... and what the page says when two subagents collide`), `anchor` (`:299`, `:839`, `:156`, `:176`, `:1293`), and `teaches` cover only automatic delegation and same-`name` collision precedence — not YAML frontmatter, system prompt body, required `name`, `tools`, or `model`. Moreover, `S026`'s `used-by` cell (`SOURCES.md:39`) omits `SKILL.md` and `corpus/knowledge/agent-definition-files-round56.md`, and live `sub-agents.md` has drifted from `S026`'s recorded `110,784 B` / `89aa73eb…` to `111,624 B` / `84b2646c…` (shifting `S026`'s anchored lines `:839` → `:838` and `:1293` → `:1292`).
- **Impacted axes**: consistency, calibration.
- **Smallest safe correction**: In `corpus/SOURCES.md:85` (S072), add `:736` (`§ Troubleshooting → § Filesystem-based agents not loading`) to S072's anchor and teaches so `~/.claude/agents/` is anchored in S072 itself; in `corpus/knowledge/agent-definition-files-round56.md:29-30`, cite the exact `sub-agents.md` schema lines (`:94,162-163,242,289,298-302,349,446`) and note that `S026` in `SOURCES.md` was scoped to delegation/collision at `110,784 B` (`89aa73eb…`) while live `sub-agents.md` on 2026-10-23 (`111,624 B`, `84b2646c…`) carries those schema lines.

### Finding F2 — Codex `features.*` cells are wider than `S073.md` on capability/tool restrictions (`SKILL.md:104`, `corpus/knowledge/agent-definition-files-round56.md:49-50`)

- **Target lines**:
  - `SKILL.md:104` (`What the file sets`): `Standalone TOML, not Markdown; name, description and developer_instructions required; model keys; features.* switches turn capabilities off`
  - `corpus/knowledge/agent-definition-files-round56.md:49-50` (Finding 4): `4. **Tool limits use different keys.** tools (Claude Code, VS Code, Copilot CLI, Gemini CLI), readonly (Cursor), permissions (opencode V2, which drops the legacy tools key), features.* switches (Codex).`
- **Counterexample & evidence**:
  - `S073.md:400-405` does not document arbitrary `features.*` switches or a general tool-restriction list; it lists five specific supported feature keys that can be set to `false` (plus separate `skills.*` keys):
    - `S073.md:400-402`: `"To reduce a custom agent's capabilities, set supported feature keys to false: features.shell_tool, features.apps, features.plugins, features.memories, or features.request_permissions_tool."`
    - `S073.md:402-404`: `"Disable individual skills with skills.config or bundled skills with skills.bundled.enabled = false."`
  - `S073.md:329-331,346-348,407-411` explicitly states that a custom agent TOML file **cannot** create a read-only sandbox or override parent permissions, sandbox mode, approval policy, or MCP servers:
    - `S073.md:329-331`: `"Custom agent instructions can ask an agent to avoid edits, but they don't create a separate read-only sandbox."`
    - `S073.md:346-348`: `"They inherit the parent's permissions, provider, and MCP servers; a custom agent file can't override those settings."`
    - `S073.md:407-409`: `"Other session settings, including sandbox_mode, approval_policy, model_provider, and mcp_servers, don't override the parent configuration when placed in a custom agent file."`
  - `SrcCodex.md:40` originally qualified `supported features.* switches can disable capabilities`, but `SKILL.md:104` dropped `supported`, and `agent-definition-files-round56.md:49-50` places `features.* switches (Codex)` unconditionally under `Tool limits use different keys` without noting that only the five supported `features.*` keys can be set to `false` and that permissions/sandbox/MCP settings are inherited from the parent session. (Also in Finding 4 at `:49`, Claude Code's `disallowedTools` denylist at `S026.md:301,446` is omitted beside `tools`.)
- **Impacted axes**: depth, calibration.
- **Smallest safe correction**:
  - In `SKILL.md:104`: restore `supported` before `features.*` (`supported features.* switches turn capabilities off`).
  - In `corpus/knowledge/agent-definition-files-round56.md:49-50`: write `tools (and disallowedTools in Claude Code; tools in VS Code, Copilot CLI, Gemini CLI), readonly (Cursor), permissions (opencode V2, which drops the legacy tools key), and supported features.* = false switches (Codex, while permissions, sandbox_mode, and mcp_servers inherit from the parent)`.

### Finding F3 — Undisclosed line-wrap folding for `S073` in `Quote notes:` (`corpus/lessons/round-56.md:22-24`, `corpus/knowledge/agent-definition-files-round56.md:29-34`)

- **Target lines**:
  - `corpus/lessons/round-56.md:15,22-24`
  - `corpus/knowledge/agent-definition-files-round56.md:22,29-34`
- **Counterexample & evidence**:
  - In `S073.md:341-343`, the quoted sentence occupies three lines separated by `\n` after `under` and after `project-scoped`.
  - Both `corpus/lessons/round-56.md:22-24` and `corpus/knowledge/agent-definition-files-round56.md:29-34` include a `Quote notes:` paragraph detailing quote normalizations (S073 URL redirect, S076 line choice, S078 code-fence removal), and `SrcCodex.md:49` disclosed joining the three lines with spaces, but the integrated `Quote notes:` omit that `S073`'s quote folded two hard line breaks into spaces.
- **Impacted axes**: calibration.
- **Smallest safe correction**: Add `(with line breaks in :341-343 folded to spaces)` to the S073 sentence in `corpus/lessons/round-56.md:22` and `corpus/knowledge/agent-definition-files-round56.md:31`.

### Finding F4 — `SKILL.md:99` implies `verifiers/check_agent_definitions.py` checks `S026` and the full basis (`SKILL.md:99`)

- **Target line**:
  - `SKILL.md:99`: `Basis: corpus/knowledge/agent-definition-files-round56.md (S072–S078, S026), checked by verifiers/check_agent_definitions.py.`
- **Counterexample & evidence**:
  - `verifiers/check_agent_definitions.py:578-579,599-600,625-666` checks only the first backticked location token in `SKILL.md`, the action cell's word count (`>= 3`), and the new round-56 `S072–S078` rows; it explicitly disqualifies base rows such as `S026` and never inspects `What the file sets` (`sr[2]`), as `corpus/knowledge/agent-definition-files-round56.md:58-67` states.
- **Impacted axes**: calibration.
- **Smallest safe correction**: Change the end of `SKILL.md:99` to `Basis: corpus/knowledge/agent-definition-files-round56.md (S072–S078; Claude schema S026), locations checked by verifiers/check_agent_definitions.py.`

## 4. Summary Verification Matrix (`S072`, `S073`, `S026`)

| Surface / Cell | Cited source | Supported by live page? | Supported by `SOURCES.md` row as written? | Verdict |
|---|---|---|---|---|
| `round-56.md:14` & `entry:21` Gate quote (`S072`) | `S072` (`sdk-subagents.md:17`) | Yes (`41,461 B`, `5b7aa6c6…`, line 17 byte-exact) | Yes (`SOURCES.md:85`) | **HOLDS** |
| `round-56.md:15` & `entry:22` Gate quote (`S073`) | `S073` (`subagents.md:341-343`) | Yes (`22,907 B`, `e7469d41…`, lines 341–343 with `\n` folded) | Yes (`SOURCES.md:86`) | **HOLDS** (disclose line-wrap fold, F3) |
| `SKILL.md:103` Location (`.claude/agents/` + user `~/.claude/agents/`) | `S072`, `S026` | Yes (`S072.md:17,174,736`; `S026.md:162-163`) | Partial (`S072` row anchors only `:14-18`, omitting `:736`) | **MIXED** (F1) |
| `SKILL.md:103` What the file sets & `entry:1,29-30,46` (`schema: S026`) | `S026` | Yes on live `sub-agents.md:94,242,289,298-302,349,446` (`111,624 B`, `84b2646c…`) | No — outside `S026`'s `scope`/`anchor`/`teaches`/`used-by` in `SOURCES.md:39` | **WIDER THAN ROW** (F1) |
| `SKILL.md:104` Location (`.codex/agents/` + user `~/.codex/agents/`) | `S073` | Yes (`S073.md:341-343`) | Yes (`SOURCES.md:86`) | **HOLDS** |
| `SKILL.md:104` What the file sets & `entry:40` (TOML, required `name`, `description`, `developer_instructions`, `model` keys) | `S073` | Yes (`S073.md:341,350-354,389-396`) | Yes (`SOURCES.md:86`) | **HOLDS** |
| `SKILL.md:104` (`features.* switches turn capabilities off`) & `entry:49-50` Finding 4 (`features.* switches (Codex)`) | `S073` | Wider than `S073.md:329-331,346-348,400-409` (only 5 supported `features.*` keys; permissions/sandbox/MCP inherited) | Wider than `S073` page | **WIDER THAN PAGE** (F2) |

## Tooling and Process Hygiene

- No tools were installed or updated during this review.
- No lane files were modified; only `.ufo/waves/round-56/falsify/ReopenS072S073.md` was written in the lane, and scratch fetch files were saved under `/fast/scratch/hyaku/kotoba-r56/ReopenS072S073/`.
- No background processes were left running.
