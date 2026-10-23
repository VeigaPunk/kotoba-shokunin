Result: DONE — Gemini CLI's S076 evidence and sandbox dry-run are ready; the row is live-backed, while the one-client world does not meet the global C1 threshold.

## Behavior and evidence

- The candidate official documentation page is `https://geminicli.com/docs/core/subagents.md` (host `geminicli.com`, pinned for Gemini CLI). Fetch command, run from `/home/vgpnk/Projects/shokunin`:
  `timeout 900s date -u '+%Y-%m-%dT%H:%M:%SZ' && timeout 120s curl --max-time 90s -fL -sS -o /fast/scratch/hyaku/kotoba-r56/SrcGeminiCLI/gemini-subagents.md -w 'HTTP %{http_code}\n' https://geminicli.com/docs/core/subagents.md && timeout 120s wc -c /fast/scratch/hyaku/kotoba-r56/SrcGeminiCLI/gemini-subagents.md && timeout 120s sha256sum /fast/scratch/hyaku/kotoba-r56/SrcGeminiCLI/gemini-subagents.md`
  Observed output / exit: `2026-10-23T02:47:06Z`; `HTTP 200`; `23614` bytes; SHA-256 `4b9baa88628b0a2bdaea87dc6b9a5c5dd2d998274ba9a93cc6ed23c53b8ee2db`; command exit 0. Fetched-byte line references below are from that saved `.md` file.
- One selected quote (6 words; copied byte-for-byte from `subagents.md:324`, Markdown retained): `2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)`. It carries the `.gemini/agents/*.md` location form verbatim and `agents` outside the path; the C1 counter accepted it.
- Docs facts: custom files are Markdown with YAML frontmatter (`subagents.md:320`); frontmatter must begin with `---` and body is the System Prompt (`:328-329`). The schema marks `name` and `description` required (`:364-365`); `tools` is an optional list of tool names and omitted `tools` inherits parent-session tools (`:367`); `model` is optional and defaults to `inherit` (`:369`). Project and user locations are explicitly labeled (`:323-324`). The page says subagents are enabled by default and shows `experimental.enableAgents: false` as the disable setting (`:591-597`): it documents an opt-out, not an opt-in gate, and does not explicitly call the feature experimental.
- The documentation page lists project-level and user-level paths but does not state same-name precedence. For a supplemental implementation cross-check only, fetched official Gemini CLI repository source `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/agents/registry.ts` at `2026-10-23T02:52:43Z`: HTTP 200, 24090 B, SHA-256 `7bc0634e1dcc6bc99907a2b7eca05c9d8aa37444006961411abd32f94eb702e8` (moving `main` snapshot; not a commit pin). Its fetched bytes identify project agents first (`registry.ts:173`, registration awaited at `:218-229`), then user agents (`:238-253`); duplicate handling says “The later definition will be ignored.” (`:350-352`). [INFERENCE] When a project agent is eligible and registers, its same-name definition therefore wins over the user-level one. This implementation detail is not documented by the S076 page. Current code also skips project agents for a home-directory workspace or an untrusted folder (`:174-179`, `:230-234`), so the precedence conclusion is conditional on project registration.

## Ready-to-paste blocks

### 1. SOURCES row (11 cells)
```markdown
| S076 | Gemini CLI docs — Subagents — https://geminicli.com/docs/core/subagents.md | docs | A | Gemini CLI custom subagent files: locations, format, schema, and enablement | § Agent definition files `subagents.md:320-324`; § File format `:328-329`; § Configuration schema `:364-369`; § Disabling subagents `:589-597`; fetched 2026-10-23T02:47:06Z, HTTP 200, 23614 B, sha256 `4b9baa88628b0a2bdaea87dc6b9a5c5dd2d998274ba9a93cc6ed23c53b8ee2db` (seat SrcGeminiCLI) | Custom agents are Markdown with YAML frontmatter; project/user paths; required `name` and `description`; optional `tools` and `model` | mined | 2026-10-23 | 90d | corpus/knowledge/agent-definition-files-round56.md, corpus/lessons/round-56.md |
```

### 2. Entry row
```markdown
| Gemini CLI | `.gemini/agents/*.md` | S076 | "2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)" |
```

### 3. Detail paragraph
```text
Gemini CLI defines custom agents as Markdown `.md` files with YAML frontmatter (“Custom agents are defined as Markdown files (`.md`) with YAML frontmatter.”, `subagents.md:320`); the file must start with YAML frontmatter and its body becomes the System Prompt (“The file **MUST** start with YAML frontmatter enclosed in triple-dashes `---`.” and “The body of the markdown file becomes the agent's **System Prompt**.”, `:328-329`). The schema marks `name` and `description` required (“| `name`         | string | Yes      | Unique identifier (slug) used as the tool name for the agent.”, `:364`; “| `description`  | string | Yes      | Short description of what the agent does.”, `:365`). `tools` is an optional array of allowed tool names (“| `tools`        | array  | No       | List of tool names this agent can use.”, `:367`); if omitted it inherits parent-session tools (“**If omitted, it inherits all tools from the parent session.**”, `:367`), while the isolation section says “The subagent only has access to the tools you explicitly grant it.” (`:390-391`). `model` is an optional string and defaults to `inherit` (“| `model`        | string | No       | Specific model to use”, and “Defaults to `inherit` (uses the main session model).”, `:369`). The page labels `.gemini/agents/*.md` “Project-level” and shared with the team (`:323`), and `~/.gemini/agents/*.md` “User-level” and personal (`:324`); it does not state duplicate-name precedence. Supplemental current-main implementation loads project agents before user agents (`registry.ts:173`, `:218-229`, `:238-253`) and says “The later definition will be ignored.” (`:350-352`). [INFERENCE] A project agent that is eligible and registers wins a same-name collision; this is code-derived behavior, not a rule stated on the documentation page. Subagents are enabled by default (“Subagents are enabled by default.”, `subagents.md:591`) and can be disabled using `"experimental": { "enableAgents": false }` (`:596`); the page documents an opt-out setting but does not explicitly label the feature experimental.
```

### 4. SKILL.md decision-table row
```markdown
| Gemini CLI | `.gemini/agents/*.md` (user-level: `~/.gemini/agents/*.md`) | Markdown with YAML frontmatter; requires `name` and `description`; optional `tools` names usable tools and `model` selects a model | Create a team-shared or personal agent definition |
```

### 5. Gate row
```markdown
| S076 | https://geminicli.com/docs/core/subagents.md | 2026-10-23T02:47:06Z | 23614 B, sha256 `4b9baa88…` | "2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)" | `subagents.md:324` | SrcGeminiCLI |
```

## Gates and dry-run

- Before drafting, `functions.grep` searched the lane `corpus/SOURCES.md` for the literal `https://geminicli.com/docs/core/subagents.md`: `No matches found`. The same fixed-string search in the e02 sandbox SOURCES also found no URL or S076 row. `timeout 120s git --no-optional-locks -C /fast/scratch/hyaku/kotoba-r56/SrcGeminiCLI diff --quiet b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 HEAD -- corpus/SOURCES.md` returned 0, confirming the sandbox source registry was byte-identical to base before adding S076.
- Sandbox clone command completed with no output; `git rev-parse HEAD` confirmed `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8` before the world was edited. The world commit command added only `SKILL.md`, `corpus/SOURCES.md`, `corpus/knowledge/agent-definition-files-round56.md`, and `corpus/lessons/round-56.md`; commit `efa45d45dd0b6e13ea38364b0ef238db12ff1ea8` (`4 files changed, 19 insertions`). The two fetched source files remain sandbox-only and were not staged.
- Required dry-run command: `timeout 900s python3 -B verifiers/check_agent_definitions.py --rev efa45d45dd0b6e13ea38364b0ef238db12ff1ea8 --fetch` (cwd `/fast/scratch/hyaku/kotoba-r56/SrcGeminiCLI`) exited 1. Exact Gemini line: `Gemini CLI   BACKED token=.gemini/agents/*.md norm=.gemini/agents found=yes base_count=0`. `BACKED` / `found=yes` means this row, entry quote, Gate quote, source and live path passed; the one-client world printed `agent-definition locations found on the live page 1 of 1; new ground 1`, below the global requirement F≥5 and G≥2. This is not a global C1 pass.

## Rejections, touched surfaces, scope, artifacts

- Rejected pages opened: none. The S076 documentation page was used for the row and file facts; the GitHub registry source was used only for supplemental implementation precedence. Web-search result pages were not opened or used.
- Lane touched surface: this report only, `.ufo/waves/round-56/build/SrcGeminiCLI.md`. No lane product files, counters, lesson, or index were edited.
- Sandbox touched surfaces in commit `efa45d45dd0b6e13ea38364b0ef238db12ff1ea8`: `SKILL.md`, `corpus/SOURCES.md`, `corpus/knowledge/agent-definition-files-round56.md`, `corpus/lessons/round-56.md`. Sandbox captures: `/fast/scratch/hyaku/kotoba-r56/SrcGeminiCLI/gemini-subagents.md` and `/fast/scratch/hyaku/kotoba-r56/SrcGeminiCLI/registry.ts`.
- Out of scope: C2 remains withdrawn; no C2 delegate/map changes, no other clients' rows, no counter edits, no full seven-client C1 pass, and no install/update. No build, tests, lint, or formatter ran; the only executed gate was the explicitly requested sandbox C1 `--fetch` counter.
