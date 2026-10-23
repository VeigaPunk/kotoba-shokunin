Result: MIXED — S076 (Gemini CLI) and S077 (Cursor) re-open live with byte-identical SHA-256 hashes and pass the frozen C1 `--fetch` counter at `c22fdd390e10623209024c9bbc2fa86b0cdfc333`, but the landed prose has five fixable calibration/consistency defects across `SKILL.md:107-108`, `corpus/knowledge/agent-definition-files-round56.md`, and `corpus/SOURCES.md:89-90` (unqualified `enableAgents` in `SKILL.md:107` and missing from the entry/SOURCES `teaches`; unqualified `description` requirement for `kind: remote` Gemini subagents; user-level quote witnessing Gemini's project path; incomplete Cursor field/precedence sync between `SKILL.md:108` and the entry; and unnoted `.codex/agents/` Markdown-vs-TOML conflict).

## 1. Live re-open & C1 counter verification

All fetches and counter runs executed in the isolated sandbox `/fast/scratch/hyaku/kotoba-r56/ReopenS076S077` (checked out at `c22fdd390e10623209024c9bbc2fa86b0cdfc333`, no sandbox commits created). No tools were installed or updated.

### Fetch commands and observed outputs

Command 1 (primary S076 and S077 live re-open, exit code `0`):
```sh
timeout 120 bash -c '
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
mkdir -p /fast/scratch/hyaku/kotoba-r56/ReopenS076S077
cd /fast/scratch/hyaku/kotoba-r56/ReopenS076S077
echo "=== S076 ==="
date -u +"%Y-%m-%dT%H:%M:%SZ"
curl -sS -L -D s076.headers -o s076.md -w "HTTP_STATUS:%{http_code} EFFECTIVE_URL:%{url_effective} BYTES:%{size_download}\n" "https://geminicli.com/docs/core/subagents.md"
wc -c s076.md
sha256sum s076.md
echo "=== S077 ==="
date -u +"%Y-%m-%dT%H:%M:%SZ"
curl -sS -L -D s077.headers -o s077.md -w "HTTP_STATUS:%{http_code} EFFECTIVE_URL:%{url_effective} BYTES:%{size_download}\n" "https://cursor.com/docs/subagents.md"
wc -c s077.md
sha256sum s077.md
'
```
Observed output:
```text
=== S076 ===
2026-10-23T03:07:42Z
HTTP_STATUS:200 EFFECTIVE_URL:https://geminicli.com/docs/core/subagents.md BYTES:23614
23614 s076.md
4b9baa88628b0a2bdaea87dc6b9a5c5dd2d998274ba9a93cc6ed23c53b8ee2db  s076.md
=== S077 ===
2026-10-23T03:07:42Z
HTTP_STATUS:200 EFFECTIVE_URL:https://cursor.com/docs/subagents.md BYTES:27660
27660 s077.md
264b4b00e713ec0dd73939306690ea4013168bead35411da3cc56fc1a71b2668  s077.md
```

Command 2 (linked Gemini CLI documentation cross-checks, exit code `0`):
```sh
timeout 120 bash -c '
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
cd /fast/scratch/hyaku/kotoba-r56/ReopenS076S077/fetched
echo "=== remote-agents.md ==="
date -u +"%Y-%m-%dT%H:%M:%SZ"
curl -sS -L -D s076_remote.headers -o s076_remote.md -w "HTTP_STATUS:%{http_code} EFFECTIVE_URL:%{url_effective} BYTES:%{size_download}\n" "https://geminicli.com/docs/core/remote-agents.md"
wc -c s076_remote.md
sha256sum s076_remote.md
echo "=== configuration.md ==="
date -u +"%Y-%m-%dT%H:%M:%SZ"
curl -sS -L -D s076_config.headers -o s076_config.md -w "HTTP_STATUS:%{http_code} EFFECTIVE_URL:%{url_effective} BYTES:%{size_download}\n" "https://geminicli.com/docs/reference/configuration.md"
wc -c s076_config.md
sha256sum s076_config.md
'
```
Observed output:
```text
=== remote-agents.md ===
2026-10-23T03:09:59Z
HTTP_STATUS:200 EFFECTIVE_URL:https://geminicli.com/docs/core/remote-agents.md BYTES:17048
17048 s076_remote.md
8bdfde65084df86a28fa0367e820bea431e93e8f2346d2e2c3b15071f3989906  s076_remote.md
=== configuration.md ===
2026-10-23T03:10:00Z
HTTP_STATUS:200 EFFECTIVE_URL:https://geminicli.com/docs/reference/configuration.md BYTES:102704
102704 s076_config.md
4fb90004ef3e4aeb3705ceeea4ab8a0d8e0e3aa4553293a1df035990740cc9ca  s076_config.md
```

Command 3 (linked Cursor documentation cross-check, exit code `0`):
```sh
timeout 60 bash -c '
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
cd /fast/scratch/hyaku/kotoba-r56/ReopenS076S077/fetched
date -u +"%Y-%m-%dT%H:%M:%SZ"
curl -sS -L -D s077_customize.headers -o s077_customize.md -w "HTTP_STATUS:%{http_code} EFFECTIVE_URL:%{url_effective} BYTES:%{size_download}\n" "https://cursor.com/docs/customize-cursor.md"
wc -c s077_customize.md
sha256sum s077_customize.md
'
```
Observed output:
```text
2026-10-23T03:10:37Z
HTTP_STATUS:200 EFFECTIVE_URL:https://cursor.com/docs/customize-cursor.md BYTES:5200
5200 s077_customize.md
9ae0878d97465512ad29459f5406538ec7b427dfbaa39e1cc95d3deb447f363e  s077_customize.md
```

Command 4 (sandbox C1 counter run at `c22fdd390e10623209024c9bbc2fa86b0cdfc333`, exit code `0`):
```sh
timeout 120 bash -c '
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
cd /fast/scratch/hyaku/kotoba-r56/ReopenS076S077
python3 -B verifiers/check_agent_definitions.py --rev c22fdd390e10623209024c9bbc2fa86b0cdfc333 --fetch --json
echo "EXIT_CODE:$?"
'
```
Observed output (S076 and S077 excerpts from JSON; full exit `EXIT_CODE:0`, `"backed": 7, "of": 7, "found": 7, "new_ground": 3`):
```json
  {
   "client": "Gemini CLI",
   "row": "S076",
   "url": "https://geminicli.com/docs/core/subagents.md",
   "quote": "2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)",
   "token": ".gemini/agents/*.md",
   "norm": ".gemini/agents",
   "in_k": true,
   "backed": true,
   "why": [],
   "found": true,
   "base_count": 0
  },
  {
   "client": "Cursor",
   "row": "S077",
   "url": "https://cursor.com/docs/subagents.md",
   "quote": "You can also create subagents manually by adding markdown files to `.cursor/agents/` (project) or `~/.cursor/agents/` (user).",
   "token": ".cursor/agents/",
   "norm": ".cursor/agents",
   "in_k": true,
   "backed": true,
   "why": [],
   "found": true,
   "base_count": 0
  }
```

---

## 2. Check-by-check verification and findings

All quotes below are byte-exact (Markdown retained, not stripped) and ≤25 words, with line numbers in `/fast/scratch/hyaku/kotoba-r56/ReopenS076S077/fetched/`.

### Finding 1 — Gemini CLI `enableAgents` default: conflated with agent-file schema in `SKILL.md:107` and omitted from `agent-definition-files-round56.md` and `SOURCES.md:89` `teaches` (fixable defect)

- **Attacked surfaces:**
  - `SKILL.md:99`: `Basis: corpus/knowledge/agent-definition-files-round56.md (S072–S078, S026)`
  - `SKILL.md:107` (`What the file sets` cell): ``Markdown with YAML frontmatter; `name` and `description` required; optional `tools` and `model`; subagents are on by default (`enableAgents`)``
  - `corpus/knowledge/agent-definition-files-round56.md:1-71` (0 occurrences of `enableAgents` or `settings.json`)
  - `corpus/SOURCES.md:89` (`scope` vs `teaches` cells): `scope` says `Gemini CLI custom subagent files: locations, format, schema, and enablement` and `anchor` cites `§ Disabling subagents :589-597`, but `teaches` says only `Custom agents are Markdown with YAML frontmatter; project/user paths; required name and description; optional tools and model`.
- **Counterexample & local evidence:**
  - In `s076.md:591-592` (15 words, byte-exact):
    `Subagents are enabled by default. To disable them, set `enableAgents` to `false` in your `settings.json`:`
  - In `s076.md:596` (5 words, byte-exact):
    `  "experimental": { "enableAgents": false }`
  - Confirmed in `s076_config.md:2133-2136` (13 words, byte-exact):
    `- **`experimental.enableAgents`** (boolean):` / `- **Description:** Enable local and remote subagents.` / `- **Default:** `true``
  - Putting `subagents are on by default (\`enableAgents\`)` in the `What the file sets` column of `SKILL.md:107` without naming `settings.json` or the parent key `experimental.enableAgents` misattributes a `settings.json` toggle to the `.gemini/agents/*.md` file schema, and leaves `SKILL.md:107` ungrounded by `corpus/knowledge/agent-definition-files-round56.md`.
- **Impacted axes:** consistency, calibration, depth.
- **Smallest safe correction:**
  1. In `SKILL.md:107` (`What the file sets`), clarify `(on by default; disabled via \`experimental.enableAgents: false\` in \`settings.json\`)` (or move the `settings.json` toggle note to `corpus/knowledge/agent-definition-files-round56.md`).
  2. Add `experimental.enableAgents` (default `true` in `settings.json`, `subagents.md:591-597`) to `corpus/knowledge/agent-definition-files-round56.md` and `corpus/SOURCES.md:89` `teaches`.

### Finding 2 — Gemini CLI required keys: `name` and `description` hold for default (`kind: local`) agents in `s076.md:364-366`, but `kind: remote` agents in `.gemini/agents/*.md` do not use `description` (fixable scope qualification)

- **Attacked surfaces:**
  - `SKILL.md:107`: ``Markdown with YAML frontmatter; `name` and `description` required; optional `tools` and `model`; subagents are on by default (`enableAgents`)``
  - `corpus/knowledge/agent-definition-files-round56.md:46`: `3. **Required keys differ.** Claude Code requires \`name\` and \`description\` (S026); Gemini CLI requires both (S076);`
  - `corpus/SOURCES.md:89`: `required \`name\` and \`description\`; optional \`tools\` and \`model\``
- **Counterexample & local evidence:**
  - In `s076.md:364` (18 words, byte-exact):
    `| `name`         | string | Yes      | Unique identifier (slug) used as the tool name for the agent.`
  - In `s076.md:365` (14 words, byte-exact):
    `| `description`  | string | Yes      | Short description of what the agent does.`
  - In `s076.md:366` (12 words, byte-exact):
    `| `kind`         | string | No       | `local` (default) or `remote`.                                                                                                                                                                                |`
  - In `s076.md:367` (15 words, byte-exact) and `:369` (22 words, byte-exact):
    `| `tools`        | array  | No       | List of tool names this agent can use.`
    `| `model`        | string | No       | Specific model to use (for example, `gemini-3-preview`). Defaults to `inherit` (uses the main session model).`
  - However, `s076.md:580` links to `/docs/core/remote-agents` (`s076_remote.md`). `s076_remote.md:32-33` places remote subagents in the same `.gemini/agents/*.md` and `~/.gemini/agents/*.md` paths, and `s076_remote.md:39-42` defines their schema:
    - `s076_remote.md:39` (10 words, byte-exact): `| `kind`            | string | Yes      | Must be `remote`.`
    - `s076_remote.md:41` (21 words, byte-exact): `| `agent_card_url`  | string | Yes\*    | The URL to the agent's A2A card endpoint. Required if `agent_card_json` is not provided.`
    - Remote `.gemini/agents/*.md` files (`s076_remote.md:48-52`) have no `description` frontmatter key and no Markdown body.
- **Impacted axes:** calibration, depth.
- **Smallest safe correction:** Qualify Gemini CLI's required keys in `corpus/knowledge/agent-definition-files-round56.md:46` (and optionally `SKILL.md:107`) as applying to local subagents (`kind: local`, the default in `subagents.md:364-366`).

### Finding 3 — Gemini CLI location witness: project token `.gemini/agents/*.md` is backed by a user-level quote (`~/.gemini/agents/*.md`) via substring matching (fixable provenance sharpness defect)

- **Attacked surfaces:**
  - `SKILL.md:107`: ``.gemini/agents/*.md` (user `~/.gemini/agents/*.md`)``
  - `corpus/knowledge/agent-definition-files-round56.md:25,31-33`: Location `.gemini/agents/*.md` paired with Quote `"2.  **User-level:** \`~/.gemini/agents/*.md\` (Personal agents)"`
  - `corpus/lessons/round-56.md:18,22-23`
- **Counterexample & local evidence:**
  - `s076.md:323` (7 words, byte-exact): `1.  **Project-level:** `.gemini/agents/*.md` (Shared with your team)`
  - `s076.md:324` (5 words, byte-exact): `2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)`
  - `verifiers/check_agent_definitions.py:573` passes `s076.md:324` for the project token `.gemini/agents/*.md` only because `.gemini/agents/*.md` is a substring of `~/.gemini/agents/*.md`. Although disclosed at `agent-definition-files-round56.md:31-33`, `s076.md:320-323` provides a direct project-level quote within the 25-word limit (24 words across lines 320–323: `Custom agents are defined as Markdown files (\`.md\`) with YAML frontmatter. You can place them in:` + `1.  **Project-level:** \`.gemini/agents/*.md\` (Shared with your team)`).
- **Impacted axes:** calibration, consistency.
- **Smallest safe correction:** Keep the disclosure at `agent-definition-files-round56.md:31-33` (not a C1 counter break), or replace the quote with the 24-word whitespace-folded span `s076.md:320-323` so the quoted line directly witnesses the project-level location cell.

### Finding 4 — Cursor optional fields and `readonly`: `SKILL.md:108` lists five optional fields not all grounded in `agent-definition-files-round56.md`, while omitting what `readonly` does (fixable defect)

- **Attacked surfaces:**
  - `SKILL.md:108`: ``Markdown with YAML frontmatter; `name` (defaults to the file name), `description`, `model`, `readonly`, `is_background`, all optional``
  - `corpus/knowledge/agent-definition-files-round56.md:14,47-50`
  - `corpus/SOURCES.md:90`: `optional fields including \`model\` and \`readonly\``
- **Counterexample & local evidence:**
  - `s077.md:96` (9 words, byte-exact): `Each subagent is a markdown file with YAML frontmatter:`
  - `s077.md:124-128` marks all five documented configuration fields `Required: No`:
    - `s077.md:124` (21 words, byte-exact): `| `name`          | string  | No       | Derived from filename | Display name and identifier. Use lowercase letters and hyphens.                                                                      |`
    - `s077.md:125` (23 words, byte-exact): `| `description`   | string  | No       | —                     | Short description shown in Task tool hints. Agent reads this to decide delegation.                                                   |`
    - `s077.md:126` (18 words, byte-exact): `| `model`         | string  | No       | `inherit`             | Model to use: `inherit` or a specific model ID.`
    - `s077.md:127` (25 words, byte-exact): `| `readonly`      | boolean | No       | `false`               | If `true`, the subagent runs with restricted write permissions (no file edits, no state-changing shell commands).`
    - `s077.md:128` (22 words, byte-exact): `| `is_background` | boolean | No       | `false`               | If `true`, the subagent runs in the background without blocking the parent.                                                          |`
  - `s077.md:470` (14 words, byte-exact): `Yes. Subagents inherit all tools from the parent, including MCP tools from configured servers.`
  - `SKILL.md:99` cites `corpus/knowledge/agent-definition-files-round56.md` as its basis, yet `agent-definition-files-round56.md:47-50` never names `description`, `model`, or `is_background` for Cursor (and `SOURCES.md:90` omits `is_background`), while `SKILL.md:108` lists `readonly` only as a bare field name without stating that it restricts write permissions (`s077.md:127`) and that Cursor has no `tools` allowlist key (inheriting parent tools per `s077.md:470`).
- **Impacted axes:** consistency, depth, calibration.
- **Smallest safe correction:** Name all five optional Cursor fields (`name`, `description`, `model`, `readonly`, `is_background`) and parent tool inheritance in `corpus/knowledge/agent-definition-files-round56.md:47-50`, and note `readonly` (restricts writes) in `SKILL.md:108`.

### Finding 5 — Cursor compatibility reads (`.claude/agents/`, `.codex/agents/`) and precedence: split across `SKILL.md:108` and `agent-definition-files-round56.md:42-43`, plus unnoted `.codex/agents/` Markdown-vs-TOML conflict (fixable defect)

- **Attacked surfaces:**
  - `SKILL.md:108`: Location ``.cursor/agents/` (user `~/.cursor/agents/`; also reads `.claude/agents/` and `.codex/agents/`)``; Action `Review Cursor's own schema; project files win name conflicts`
  - `corpus/knowledge/agent-definition-files-round56.md:42-43`: `2. **Compatibility reads are not ownership.** Cursor also reads \`.claude/agents/\` and \`.codex/agents/\` (S077 \`subagents.md:84-92\`, its own files win name conflicts)`
  - `corpus/SOURCES.md:90`: `and project precedence for name conflicts`
- **Counterexample & local evidence:**
  - `s077.md:85-90` lists both project-level and user-level compatibility directories:
    - `s077.md:85` (10 words, byte-exact): `| **Project subagents** | `.cursor/agents/`   | Current project only                                 |`
    - `s077.md:86` (10 words, byte-exact): `|                       | `.claude/agents/`   | Current project only (Claude compatibility)          |`
    - `s077.md:87` (10 words, byte-exact): `|                       | `.codex/agents/`    | Current project only (Codex compatibility)           |`
    - `s077.md:89` (12 words, byte-exact): `|                       | `~/.claude/agents/` | All projects for current user (Claude compatibility) |`
    - `s077.md:90` (12 words, byte-exact): `|                       | `~/.codex/agents/`  | All projects for current user (Codex compatibility)  |`
  - `s077.md:92` states two distinct precedence rules (23 words, byte-exact):
    `Project subagents take precedence when names conflict. When multiple locations contain subagents with the same name, `.cursor/` takes precedence over `.claude/` or `.codex/`.`
  - First, `SKILL.md:108` and `SOURCES.md:90` record only the first sentence of `s077.md:92` (project over user), whereas `agent-definition-files-round56.md:42-43` records only the second sentence (`.cursor/` over `.claude/` or `.codex/`) and omits project-over-user precedence (despite Finding 1 at `:39-40` contrasting Copilot CLI's personal-over-project rule) as well as user compatibility paths `~/.claude/agents/` and `~/.codex/agents/`.
  - Second, `s077.md:87,90` labels `.codex/agents/` and `~/.codex/agents/` `(Codex compatibility)` while `s077.md:96` states `Each subagent is a markdown file with YAML frontmatter:`. Meanwhile, Finding 1 (`agent-definition-files-round56.md:40-41`, from S073) establishes that Codex custom agents in `.codex/agents/` are standalone TOML files, not Markdown. Neither `SKILL.md:99,104,108` nor `agent-definition-files-round56.md:40-45` warns the reader of this documented format discrepancy on `.codex/agents/`.
- **Impacted axes:** consistency, depth, operability.
- **Smallest safe correction:** In `corpus/knowledge/agent-definition-files-round56.md:42-43`, record both rules from `s077.md:92` (project subagents beat user subagents; `.cursor/` beats `.claude/` and `.codex/`), include `~/.claude/agents/` and `~/.codex/agents/` from `s077.md:89-90`, and note that S077 documents Markdown frontmatter while S073 documents TOML in `.codex/agents/`. In `SKILL.md:108` Action, say `project and .cursor/ files win name conflicts`.
