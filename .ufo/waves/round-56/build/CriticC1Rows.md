Result: DONE — independently opened all seven clients' documentation and compared all seven Src reports; found an incompatible checklist Action plus bounded extension and quotation-provenance gaps.

## Scope and evidence boundary

Axes: depth and calibration. Read-only content criticism, not a C1 predicate result, admission, runtime test, or integration. Frozen repository reference: `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`. Only this report is written in the lane. No counter, product file, agentdef box, map disposition, or Git/jj lane state was changed.

Own sandbox/capture directory, abbreviated **D** below: `/fast/scratch/hyaku/kotoba-r56/CriticC1Rows/`. The required clone/checkout command exited 0 and printed:

```text
Fri Oct 23 02:46:38 AM UTC 2026
e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8
```

The initial seven-client captures were opened at 02:47:40–02:48:07Z, before reading any Src report. The V2 opencode comparison was also opened before Src reports. Later supplementary captures are labeled below. No sandbox commits were made.

## Independent per-client record

All file references in this table are fetched bytes under D, not a citation to another seat's investigation.

| Client | Documented project location | Documented user location | Definition format and what it sets | Tool configuration and important boundary | Evidence |
|---|---|---|---|---|---|
| Claude Code | `.claude/agents/`; nested project definitions are discovered up to the repository root | `~/.claude/agents/` | Markdown `.md`, YAML frontmatter, Markdown system prompt; `name` and `description` required; model and other configuration optional | `tools`: comma-separated string or YAML list allowlist; `disallowedTools`: denylist; omitted `tools` inherits the tools available to subagents. The filename need not match `name`. | `claude-subagents.md:162-174,242-266,289-307,444-446` |
| Codex | `.codex/agents/` | `~/.codex/agents/` | Standalone TOML; required `name`, `description`, `developer_instructions`; model/reasoning settings and supported capability reductions | The documented reduction knobs are supported `features.* = false` keys and skill controls. Parent permissions, provider and MCP servers are inherited; putting `sandbox_mode`, `approval_policy`, `model_provider`, or `mcp_servers` in the custom file does not override them. A generic `tools` allowlist is not established by the reviewed schema. | `codex-subagents.md:341-365,387-415` |
| VS Code | `.github/agents`, `.agent.md` or `.md`; `.claude/agents` is explicitly the Claude-format compatibility route | Copilot harness: `~/.copilot/agents`; Local: VS Code profile storage; Claude harness: `~/.claude/agents` in Claude format | VS Code format: optional YAML header plus Markdown instructions. All header fields optional. Selected harness determines field behavior. | `tools`: string or string array. Local omission uses tools enabled in the picker; unavailable tools ignored. Local tool names, subagent controls and handoffs are not automatically portable to Copilot. `mcp-servers` is not used by VS Code custom agents. | `vscode-agents.md:59-69,104-130`; `vscode-reference.md:10,24-64,140-159` |
| Copilot CLI | `.github/agents/` | `~/.copilot/agents/` | Markdown profile with YAML frontmatter and Markdown instructions; guide creates `.agent.md`, and its ID rule also recognizes `.md`; `description` required, `name` optional/display-oriented | `tools`: list or comma-separated string; omission or `["*"]` enables all available tools, explicit list selects tools, `[]` disables all. File ID, not optional display `name`, governs deduplication; personal wins over repository for the same ID. | `copilot-create.md:17,23-30,78-80`; `copilot-reference.md:10-31,40-53` |
| Gemini CLI | `.gemini/agents/*.md` | `~/.gemini/agents/*.md` | Markdown `.md`; must start with YAML frontmatter; body is system prompt; `name` and `description` required; optional model, temperature and run limits | `tools`: optional array; omission inherits all parent-session tools; `*` and MCP wildcard forms documented. Inline `mcpServers` is supported. Even `*` does not permit invoking other subagents. | `gemini-subagents.md:320-394,406-411` |
| Cursor | `.cursor/agents/` | `~/.cursor/agents/` | Markdown with YAML frontmatter; listed fields `name`, `description`, `model`, `readonly`, `is_background` are all optional; body is the prompt | The opened configuration table lists those five fields, not a `tools` allowlist; FAQ positively says tools, including configured MCP tools, are inherited. `readonly` restricts writes. Cloud MCP configuration is a separate exception. `.claude/agents` and `.codex/agents` are labeled compatibility paths, not Cursor's own form. | `cursor-subagents.md:73,81-128,427,470` |
| opencode | `.opencode/agents/` | `~/.config/opencode/agents/` | Both V1 and V2 document Markdown agents with frontmatter and a prompt body, but their configuration schemas differ. V1 also uses `agent` in JSON; V2 uses `agents` in JSONC. | V1: `permission` map; legacy `tools` boolean map deprecated. V2: ordered `permissions` rules with `action`, `resource`, `effect`; explicitly says not to use legacy `tools`, `permission`, `prompt`, etc. in new V2 agent configuration. Same path does not make these schemas interchangeable. | `opencode-agents.md:165-233,390-394,439-516`; `opencode-v2-agents.md:5-17,30-77,236-259,340` |

The Cursor/Codex observations about unlisted fields are bounded to the opened schema and positive inheritance statements. They are not a vendor-wide silence finding or proof of how a binary handles an unknown key. No client is labeled "silent"; a Q30-wide negative sweep was not completed.

## Strongest counterexample: the Action cell ports the wrong authority

**Observed proposal:** `.ufo/waves/round-56/build/SrcCursor.md:36` ends with `Apply checklist to Cursor subagents`. Its own preceding cell correctly says all five listed Cursor fields are optional.

**Counterexample from local evidence:** a Cursor definition without a `name` is documented as valid/defaulting from its filename (`D/cursor-subagents.md:124`), while the unchanged opencode checklist treats absent `name` as a defect (`SKILL.md:316-317`). The next box requires enrollment in an `opencode.json` agent map or reachable `subagents:` roster (`SKILL.md:318-320`), whereas Cursor says it includes all custom subagents in its available tools (`D/cursor-subagents.md:431`). Claude Code also explicitly says, at `D/claude-subagents.md:298`, "The filename doesn't have to match." Codex identifies agents by `name`, with stem matching only a convention (`D/codex-subagents.md:413-415`). Location discovery cannot transfer those checklist requirements.

**Impacted axes:** depth, calibration; consistency/operability if the Action is followed.

**Smallest safe correction:** replace the Cursor Action with `Review Cursor schema and prompt`. The shared intro should say `Use this table for client-specific schema review; the checklist below remains opencode-only.` In particular, remove the contradictory "before applying it" implication in `ScribeC1Frame.md:31`. Preserve all nine box texts. This is a fixable scope defect, not a necessary tradeoff.

**Guard boundary:** the frozen counter reads location `sr[1]` and Action word count `sr[3]`, not settings `sr[2]` or Action meaning (`verifiers/check_agent_definitions.py:625-644`). I inspected that code; I did not execute a mutant or counter. A location receipt cannot establish that this Action is appropriate. Do not trade calibration for a counted location or present source-reading as execution of the checklist; such a trade belongs with the canonical judge, not an author-side pass.

## Additional static integration counterexample

`ScribeC1Frame.md:33` places the new `### Agent-definition files by client` heading between the existing checklist heading and its boxes. Independently inspected parser code updates a box's section on **every** heading (`verifiers/verify_skill_checklist.py:673-675,701-707`), and map parity compares `(section, sha256)` pairs (`:1274-1289`). The current map pins agentdef boxes to `Agent-definition fidelity checklist` (`verifiers/checklist-baseline.json`, agentdef.01 and .02 entries).

**[INFERENCE], not an executed gate result:** that placement relabels the boxes and creates map-parity mismatches even when all nine box texts remain byte-identical. This independently corroborates the same placement concern in `CriticAxisFit.md:54-60`.

**Impacted axes:** consistency, operability and calibration. **Smallest safe correction:** put the new table before the existing `## Agent-definition fidelity checklist` heading, leaving that heading and its nine boxes together. This prevents a fixable regression; it is not a tradeoff required by C1.

## Final Src-report comparison and every disagreement found

| Report and proposal pointer | Independent comparison | Smallest safe correction / calibration |
|---|---|---|
| `SrcClaudeCode.md:34,42,47,56,59` | No sustained disagreement on native paths, format, tools, or model. I attacked the SDK-vs-CLI provenance: newly opened `D/claude-sdk-subagents.md:17,174,736-744` explicitly points back to Claude Code's filesystem definitions and names the same CLI directories. Its bytes match the report's recorded SDK hash. S072 supports the filesystem path; S026 supports the richer file schema, as the report explicitly discloses. | Retain that attribution split. Do not turn an SDK programmatic `AgentDefinition` schema into a filesystem-file schema or call this held path new ground. No such substitution is present in the proposed row. |
| `SrcCodex.md:24,30,40,49` | No material disagreement. Standalone TOML, all three required keys, supported feature reductions, native project/user paths, and model settings match the independent capture. The report bounds its generic-tools observation to the reviewed section and discloses line-wrap folding. | Keep parent permission/provider/MCP inheritance in the knowledge detail if discussing tool restrictions; do not add a `tools` allowlist or per-agent sandbox override by analogy. These are guards against widening, not a correction to the present row. |
| `SrcVSCode.md:20,25,30` | Native workspace path, harness-dependent user storage, optional header, and tools match. Small quotation-provenance disagreement: the detail quotes `The Local harness ...` and a plain-text Claude-format table row; raw `D/vscode-agents.md:126` contains `**Local**`, and `:113` contains a Markdown link around `Claude agent format`. Those detail excerpts are not raw byte-exact as displayed. The selected C1 path quote at `:63` is exact. | Add a disclosure that these supporting schema excerpts strip Markdown markup, or copy the raw substrings. This is quote hygiene, not false location/schema evidence or a predicate miss. |
| `SrcCopilotCLI.md:27,32` | Paths, YAML/frontmatter, tools defaults and precedence agree. The detail's universal `Each ... is a Markdown .agent.md file` is over-narrow if read as an extension requirement: the same CLI guide's ID rule explicitly handles `.md` too (`D/copilot-create.md:30`). | Say `Markdown profiles (.agent.md; .md also recognized)`, or `.agent.md/.md profiles`. The guide's creation convention is not proof that every recognized agent must use the longer suffix. Entry/Gate quote normalization is explicitly disclosed in `SrcCopilotCLI.md:9`; I do not call that fabrication. |
| `SrcGeminiCLI.md:8,21,31,36` | Schema and both locations agree. A scope-specific quote gap remains: the selected quote says only `User-level` and `~/.gemini/agents/*.md`, while the Location cell first presents the unprefixed project path. The project fact itself is supported by the immediately preceding raw line 323. | Prefer a project-labeled quote for the project-first cell, or label the witnessed location user-level. This is not a counter break: the frozen normalization expressly allows removing `~/`. Do not say the current quote alone establishes project scope. |
| `SrcCursor.md:28,31,36` | Native paths and selected quote are exact; no compatibility path is passed off as Cursor's own. Optional fields and `readonly` are correctly bounded. The Action disagreement is the concrete defect detailed above. | Replace the Action; do not "fix" it by imposing opencode name/roster rules on Cursor. |
| `Srcopencode.md:8,16,19,23,28,34` | Native project/user paths, V2 frontmatter/body, `permissions`, model inheritance and explicit exclusion of legacy `tools` match the independent V2 capture and newly opened pinned source. No V1/V2 key substitution is present. The selected quote has a presentation/provenance gap: its bare `text` is a code-fence information string, not prose or part of an agent ID (`D/opencode-v2-agents.mdx:41-45`). The report discloses removing fence markers, so I do not call the path fabricated or the normalization undisclosed. | Preserve fence syntax in the source excerpt, or explicitly label the result a normalized Markdown-source excerpt, not verbatim prose. Lead the settings cell with `V2`; qualify `no required key stated` as a finding about the opened page, not a schema guarantee. Do not infer optionality merely from an unmarked documentation table. |

Comparison closed at `Fri 23 Oct 2026 03:02:53 AM UTC`, after all seven reports were read. I found no wrong native directory or compatibility-directory substitution in these proposed rows; that is a bounded finding about the reviewed proposals, not a vendor-wide absence claim.

For the Gemini project-first cell, this exact raw excerpt supplies the project label and an agent word within 25 words (`D/gemini-subagents.md:320-323`; keep the raw line breaks, or disclose folding for a one-line table):

```text
Custom agents are defined as Markdown files (`.md`) with YAML frontmatter. You
can place them in:

1.  **Project-level:** `.gemini/agents/*.md` (Shared with your team)
```

The quoted path alone does not establish every settings cell. I checked the separate schema sections above rather than treating a path quote as evidence for tools/model/permission behavior.

The opencode quote's raw source span is below (`D/opencode-v2-agents.mdx:41-45`). Keeping this syntax makes the origin of `text` visible rather than presenting it as a word in the author's sentence:

````text
A nested path becomes part of the agent ID:

```text
.opencode/agents/team/reviewer.md  →  team/reviewer
```
````

Calibration guard: do not sum the Src seats' one-client new-ground receipts. VS Code and Copilot CLI both present `.github/agents`; the frozen rule counts distinct normalized forms, not client labels (`verifiers/check_agent_definitions.py:78-84`). No aggregate C1 result was measured by this review.

## Capture receipts: observed commands, outputs and source locations

For the ordinary captures I ran the command family below with the literal URL and D capture paths for each row. Every listed capture call exited 0 and returned HTTP 200; the recorded effective URL equals the requested URL. This is a description of the individual observed tool calls, not a script subsequently run:

```sh
timeout 50s curl -sSL --max-time 40 -D HEADER -o BODY -w 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' URL && timeout 5s date -u && timeout 5s sha256sum BODY
```

The V2 agents call additionally used `-H 'Accept: text/markdown'`. The Codex tree-discovery call used `timeout 60s` and `--max-time 50`. Raw bytes were not stripped or reformatted in the saved bodies.

| Body under D | URL opened | UTC access | HTTP / bytes | Observed SHA-256 |
|---|---|---|---|---|
| `claude-subagents.md` | https://code.claude.com/docs/en/sub-agents.md | 2026-10-23T02:47:40Z | 200 / 111624 | `84b2646c513754ef5f33c6f5a0d7f59960021a65b5a09c35b9158fa116a73d5a` |
| `codex-subagents.md` | https://learn.chatgpt.com/docs/agent-configuration/subagents.md | 2026-10-23T02:48:07Z | 200 / 22907 | `e7469d41c5a18a4ee66ee40ca4a9a2617a697e42554a0198ac4481e1e597357f` |
| `vscode-agents.md` | https://code.visualstudio.com/docs/agent-customization/custom-agents.md | 2026-10-23T02:47:40Z | 200 / 15714 | `8643b0986edea38447e9c759052284439a39e332d9f3dea2c4a6934c3361b07f` |
| `vscode-reference.md` | https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference.md | 2026-10-23T02:48:28Z | 200 / 11205 | `71e4dbc2daea59ea575fbc1eb307f8b1f1324c1b586aa942abf957ac8b8f0288` |
| `copilot-create.md` | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md | 2026-10-23T02:47:40Z | 200 / 8379 | `506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2` |
| `copilot-reference.md` | https://docs.github.com/en/copilot/reference/custom-agents-configuration.md | 2026-10-23T02:48:07Z | 200 / 18901 | `9ea3e683cfcb7950af70e577ef5453cfe95690c2ff34185acb5896b60bfb0a12` |
| `gemini-subagents.md` | https://geminicli.com/docs/core/subagents.md | 2026-10-23T02:47:40Z | 200 / 23614 | `4b9baa88628b0a2bdaea87dc6b9a5c5dd2d998274ba9a93cc6ed23c53b8ee2db` |
| `cursor-subagents.md` | https://cursor.com/docs/subagents.md | 2026-10-23T02:47:40Z | 200 / 27660 | `264b4b00e713ec0dd73939306690ea4013168bead35411da3cc56fc1a71b2668` |
| `opencode-agents.md` | https://opencode.ai/docs/agents.md | 2026-10-23T02:47:40Z | 200 / 20997 | `5d070a8ba9c2db70db759aa019e2e48e5c3cd834d4892f17ffb99ba3fc852b1b` |
| `opencode-v2-agents.md` | https://opencode.ai/v2/docs/agents/ | 2026-10-23T02:50:15Z | 200 / 8637 | `1f87da9eeb0e996aa42b0d8e6c7b32e1ff0cb22be1e1817a61040a35cb30fa4b` |
| `vscode-migration.md` | https://code.visualstudio.com/docs/agent-customization/migrate-customizations.md | 2026-10-23T02:54:47Z | 200 / 59037 | `a671708e4247448a8128000d5ef3b7c4ebbef15a81d7feccd74d486c1b64941a` |
| `claude-sdk-subagents.md` | https://code.claude.com/docs/en/agent-sdk/subagents.md | 2026-10-23T02:58:22Z | 200 / 41461 | `5b7aa6c66705f223744ac58acd69b7629d4ccd23c56655678c975b22f9711315` |
| `opencode-agents.html` (V2 discovery) | https://opencode.ai/docs/agents/ | 2026-10-23T02:49:30Z | 200 / 183509 | `1bddca5ba3df59505ae4ec4bb082887764ad5fe255b78100408158e5d1e70b27` |
| `opencode-v2-index.html` (agents-link discovery at line 60) | https://opencode.ai/v2/docs | 2026-10-23T02:49:59Z | 200 / 21049 | `1b65665753f849f0cac0a115fe32a7607cc08d194959c8af21863d0454a6cda3` |
| `codex-tree.json` (discovery only, not schema evidence) | https://api.github.com/repos/openai/codex/git/trees/main?recursive=1 | 2026-10-23T02:54:47Z | 200 / 3352083 | `7adcfe6675a872ef69562e1b9b81d624cfdeca00255a1a30343bdd2634a6093d` |
| `opencode-v2-agents.mdx` (supplement after reading Srcopencode) | https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/agents.mdx | 2026-10-23T03:02:01Z | 200 / 8779 | `6cca5b0a5a88387e94177d9c13d2e539fb710d69b2298ca6d44b9bc465c8b57a` |

Observed `date -u` lines, pasted rather than inferred from HTTP `Date` headers:

```text
Fri 23 Oct 2026 02:47:40 AM UTC
Fri 23 Oct 2026 02:48:07 AM UTC
Fri 23 Oct 2026 02:48:28 AM UTC
Fri 23 Oct 2026 02:49:30 AM UTC
Fri 23 Oct 2026 02:49:59 AM UTC
Fri 23 Oct 2026 02:50:15 AM UTC
Fri 23 Oct 2026 02:54:47 AM UTC
Fri 23 Oct 2026 02:58:22 AM UTC
Fri 23 Oct 2026 03:02:01 AM UTC
```

Additional byte-comparison evidence: `timeout 10s diff -u /fast/scratch/hyaku/kotoba-r56/SrcCopilotCLI/config.md /fast/scratch/hyaku/kotoba-r56/CriticC1Rows/copilot-reference.md` exited 1. Output showed only three changes from escaped `> \[!NOTE]` to `> [!NOTE]` at lines 7, 33 and 110. Thus the reference captures' differing hashes/byte counts are not a demonstrated schema disagreement; I do not treat them as false provenance.

## Limits and handoff

No client CLI, paid model call, headless browser, self-test, verifier, C1/C2 counter, judge, test suite, lint, or formatter was run. No tools were installed or updated. The optional availability probe `timeout 5s command -v inotifywait` exited 1 with no output; no watcher or other background process was started. All commands were timeout-capped; no process tree remains running from this review.

This review establishes documented paths/schema and content counterexamples, not actual discovery/loading behavior. It does not claim freshness or validate the final integrated line budget. The integration owner should use the source-specific actions, keep native versus compatibility identities and V1/V2 permissions distinct, preserve the nine opencode box bytes and their heading association, and run its assigned final checks itself. No check is claimed passed here.
