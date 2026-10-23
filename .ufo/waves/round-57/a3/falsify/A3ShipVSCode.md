Result: MIXED — The VS Code capability inventory and existing citation locations hold, but both tip and candidate need an Agent Plugins 1.0 qualifier on the namespace claim.

## Scope and input identity

Reviewed only the VS Code ship cells at lane revision `07c33d73ddce769d9cea2846a6313164401b5478` and their treatment in `.ufo/waves/round-57/a3/a2-candidate.patch`.

- `SKILL.md:119`: the short ship cell.
- `corpus/knowledge/plugin-manifests-round57.md:44`: the detailed ship cell and its source ranges.
- Candidate patch `:17` and `:99`: both VS Code rows are unchanged context lines, not replacements. Thus the candidate retains the same issue. Candidate `:84-85` changes the S081 quote-location explanation; that explanation is independently confirmed below.
- Read-only input identification, run inside my sandbox:

```text
timeout 5 git --no-optional-locks rev-parse HEAD
exit 0
07c33d73ddce769d9cea2846a6313164401b5478

timeout 5 git --no-optional-locks rev-parse HEAD:SKILL.md HEAD:corpus/knowledge/plugin-manifests-round57.md
exit 0
dc7987bdcdd674a834a0393952fa22eaa73afcef
9e0a0271b447db618f1941d50680caab621797b5

timeout 5 sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/a3/a2-candidate.patch
exit 0
2e681cf5b416a7053e3e51340743269141f935f7af4b223287b4aa2184798f2a  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/a3/a2-candidate.patch
```

The candidate was treated only as a claim/input. No evidence was taken from prior-attempt scratch or residual reports.

## Independent live-source receipt

Source: S081, [VS Code — Agent plugin authoring reference](https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md).

Fetched bytes: `/fast/scratch/hyaku/kotoba-r57a3/A3ShipVSCode/S081-agent-plugin-reference.md`. All source line numbers below refer to this unmodified file, not rendered HTML. No Markdown bytes were stripped or rewritten.

Command (exit 0):

```sh
timeout 5 date -u && timeout 70 curl --location --silent --show-error --max-time 65 --output /fast/scratch/hyaku/kotoba-r57a3/A3ShipVSCode/S081-agent-plugin-reference.md --write-out 'URL %{url_effective}\nHTTP %{http_code}\nBYTES %{size_download}\n' https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md && timeout 5 wc -c /fast/scratch/hyaku/kotoba-r57a3/A3ShipVSCode/S081-agent-plugin-reference.md && timeout 5 sha256sum /fast/scratch/hyaku/kotoba-r57a3/A3ShipVSCode/S081-agent-plugin-reference.md
```

Observed output:

```text
Fri 23 Oct 2026 06:45:52 AM UTC
URL https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md
HTTP 200
BYTES 21972
21972 /fast/scratch/hyaku/kotoba-r57a3/A3ShipVSCode/S081-agent-plugin-reference.md
d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e  /fast/scratch/hyaku/kotoba-r57a3/A3ShipVSCode/S081-agent-plugin-reference.md
```

This byte count and full hash match the committed S081 record at `corpus/SOURCES.md:94`.

## Findings

### 1. Fixable format-scope defect: namespace discovery is not universal

Both manifest cells explicitly list Agent Plugins 1.0, Copilot, Claude, and Legacy OpenPlugin. Their adjacent ship cells say that agents, commands, rules and hooks are under/read from `com.github.copilot`, without limiting that statement to Agent Plugins 1.0.

Strongest documentary counterexample: the same reference gives different hook locations for two other formats already listed in the row. These are byte-exact source lines:

S081 `:310-312`:

```text
| Agent Plugins 1.0 | `com.github.copilot/hooks/hooks.json` |
| Claude | `hooks/hooks.json` |
| Copilot | `hooks.json` (at the plugin root) |
```

S081 `:314` says: “VS Code auto-detects the plugin format and discovers the hook file automatically.” S081 `:392` preserves existing format-specific discovery rules. The namespace assertion is valid for Agent Plugins packages (`:73-85,296,379`), not a rule for every format supported by VS Code.

[INFERENCE] An audit that applies the unqualified namespace instruction to a Copilot or Claude package can miss its documented hook file. This is a qualification defect, not an unsupported capability type and not evidence from a runtime execution.

Smallest safe correction: put `in Agent Plugins 1.0` beside the namespace claim in both cells. No new component class, manifest-path change, counter change, or measurement claim is needed.

### 2. Every listed component type is supported; no missing component class found in this reference

| Listed part | Independent S081 line evidence | Assessment |
|---|---|---|
| Portable skills and MCP servers | `:11,15-16`; their discovery locations at `:71,78-79`; portable package summary at `:377` | Holds. Portability is an Agent Plugins 1.0 statement, not identical discovery across formats. |
| Agents | `:17,81,379` | Holds; client-specific. |
| Commands / slash commands | `:20,82,379` | Holds. The short cell's “commands” and detailed cell's “slash commands” refer to the documented command surface; they need not be duplicated. |
| Rules | `:83` places `rules/` under the namespace; `:379` explicitly says VS Code reads rules there | Holds. The existing cited directory example supports the row; `:379` is stronger direct evidence for “read from.” |
| Hooks | `:18,84-85,293,296,306-314,379` | Holds, with the format qualifier in finding 1. |
| Automation templates | `:19` names reusable prompts and schedules; `:121,124,128,138,157,161` supply capability, discovery and prompt semantics | Holds; explicitly VS Code-specific, not portable. |
| Auto-detected formats and manifest paths in the detailed cell | `:97-104` | Holds for all four listed formats. |

No additional top-level instruction-bearing component class was found in this S081 reference. Skills already include instructions, scripts and resources (`:16`); automation templates already include their Markdown prompt bodies (`:161`). These are not missing classes to add to the list.

Useful boundaries, not separate missing ship types:

- S081 `:128` locates default automation templates at root `automations/`; `:138` permits configured extra paths relative to `com.github.copilot/`; `:157` permits exclusive configured paths. Do not relocate all automation templates into the namespace by implication.
- S081 `:121` says installing a template does not create or enable an automation. The existing “can ship” language does not claim otherwise.
- S081 `:367` says an agent's frontmatter `hooks` field is currently omitted when passing the agent to the Copilot harness. A shipped hook definition is not proof it executes. This does not falsify a ship inventory and does not require a new component class.

### 3. Existing citation ranges hold; the candidate's S081 quote note is accurate

The detailed row cites `agent-plugin-reference.md:11-22,73-85,97-104`:

- `:11-22` contains portable skills/MCP, agents, hooks, automation templates and slash commands.
- `:73-85` contains the namespace directory example, including agents, commands, rules and hooks.
- `:97-104` contains auto-detection, the schema condition/default, and all four manifest paths.

There is no wrong or shifted existing range. The problem is the missing format qualification, not a fabricated source location. Add direct namespace/discovery evidence when making that qualification explicit.

The quote at `corpus/knowledge/plugin-manifests-round57.md:26` is exactly the middle sentence of the three-sentence fetched line `:97`:

> A root `plugin.json` that declares the canonical Agent Plugins `$schema` uses Agent Plugins semantics.

That independently confirms candidate patch `:84-85`; no whitespace folding or Markdown stripping is needed for S081.

## Exact text to land

My own cells, not the unchanged candidate rows. These are cell literals, not verbatim quotations from the vendor page. Only the ship cells and the detailed row's evidence cell need to change.

### `SKILL.md:119` — ship cell

Old:

```text
portable skills and MCP servers; agents, commands, rules and hooks under `com.github.copilot`; automation templates
```

New:

```text
portable skills and MCP servers; agents, commands, rules and hooks under `com.github.copilot` in Agent Plugins 1.0; VS Code-specific automation templates
```

Evidence for every part: portable skills/MCP `:11,15-16,71`; agents/commands/rules/hooks and qualified namespace `:73-85,296,379`; VS Code-specific automation templates `:19,121-124`.

### `corpus/knowledge/plugin-manifests-round57.md:44` — ship cell

Old:

```text
portable skills and MCP servers; client-specific agents, hooks, automation templates and slash commands; agents, commands, rules and hooks read from `com.github.copilot`; formats auto-detected (Agent Plugins 1.0 and Copilot root `plugin.json`, Claude `.claude-plugin/plugin.json`, Legacy OpenPlugin `.plugin/plugin.json`)
```

New:

```text
portable skills and MCP servers; client-specific agents, hooks, automation templates and slash commands; in Agent Plugins 1.0, agents, commands, rules and hooks read from `com.github.copilot`; formats auto-detected (Agent Plugins 1.0 and Copilot root `plugin.json`, Claude `.claude-plugin/plugin.json`, Legacy OpenPlugin `.plugin/plugin.json`)
```

Evidence for every part: portable skills/MCP `:11,15-16`; client-specific agents/hooks/templates/slash commands `:17-20`; qualified namespace plus rules `:73-85,296,379`; format auto-detection and each manifest `:97-104`; retained other-format discovery `:306-314,392`.

Source-lines cell, old:

```text
S081 `agent-plugin-reference.md:11-22,73-85,97-104`
```

Source-lines cell, new:

```text
S081 `agent-plugin-reference.md:11-22,73-85,97-104,306-314,379,392`
```

## Impact and limits

- Impacted assigned axis: depth — retain the complete supported inventory while making the format/discovery boundary source-accurate.
- This is a fixable wording defect, not grounds to invent a fifth own-format manifest or change the frozen C1 predicate/accounting. The existing capability inventory and source quote survive the attack.
- No canonical judgment, admission, integration, client execution, lane-code execution, or C1 rerun was performed by this seat. Scope did not include reviewing other clients or S086–S088.
- The sandbox was cloned and checked out with bounded `timeout` commands. No sandbox commits were made. No lane file was changed except this authorized report.
- Tools installed or updated: none.
