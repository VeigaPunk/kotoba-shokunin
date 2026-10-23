Result: MIXED — Every listed Copilot CLI component is documented, but the tip's “adds” wording obscures legacy commands/LSP support; the candidate's format distinction is source-backed.

## Scope and axes

Reviewed only the Copilot CLI ship cells in `SKILL.md:120` and `corpus/knowledge/plugin-manifests-round57.md:45` at `07c33d73ddce769d9cea2846a6313164401b5478`, plus their proposed replacements in `.ufo/waves/round-57/a3/a2-candidate.patch:22,104`. The patch was a claim to check, not evidence. Revision files were read from my isolated clone at `/fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI`. No attempt-1/attempt-2 scratch was used.

Impacted axis: depth (accurate component/format distinctions and actionable source locations). This is a fixable wording defect, not an established runtime regression or an axis tradeoff. No admission, score, or canonical-judge decision is made here.

## Independently opened sources and receipts

Commands below ran from `/fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI`. Each command chain exited 0. Dates are the verbatim `date -u` output immediately before each curl. Saved files are the original response bodies; no Markdown stripping, line folding, or other byte transformation was performed.

### S082 — creation guide

URL: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md

```sh
timeout 5s date -u && timeout 60s curl --location --silent --show-error --max-time 50 --output /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/plugins-creating.md --write-out 'HTTP %{http_code}\nbytes %{size_download}\nurl %{url_effective}\n' https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md && timeout 5s sha256sum /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/plugins-creating.md && timeout 5s wc -c /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/plugins-creating.md
```

Observed output, exit 0:

```text
Fri 23 Oct 2026 06:46:18 AM UTC
HTTP 200
bytes 7711
url https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md
c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64  /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/plugins-creating.md
7711 /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/plugins-creating.md
```

This independently fetched digest matches S082's recorded digest; the relevant line positions have not drifted.

### S028 — CLI plugin reference

S028's canonical URL is https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference; its recorded fetched representation and my requested URL are https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md.

```sh
timeout 5s date -u && timeout 60s curl --location --silent --show-error --max-time 50 --output /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/cli-plugin-reference.md --write-out 'HTTP %{http_code}\nbytes %{size_download}\nurl %{url_effective}\n' https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md && timeout 5s sha256sum /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/cli-plugin-reference.md && timeout 5s wc -c /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/cli-plugin-reference.md
```

Observed output, exit 0:

```text
Fri 23 Oct 2026 06:46:18 AM UTC
HTTP 200
bytes 47200
url https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md
d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0  /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/cli-plugin-reference.md
47200 /fast/scratch/hyaku/kotoba-r57a3/A3ShipCopilotCLI/cli-plugin-reference.md
```

The size and digest prefix agree with the recorded S028 fetch. All source line references below are to these freshly fetched bytes.

## Findings

### F1 — strongest counterexample: commands and LSP are not Agent Plugins-only capabilities

At the tip the skill says `Agent Plugins adds commands, rules, LSP servers`, and the knowledge entry says `Agent Plugins 1.0 adds Copilot-specific commands, rules and LSP servers`.

The reference places `commands` and `lspServers` under **Legacy manifest fields** (`cli-plugin-reference.md:183,205-217`):

- Line 213, the `commands` field description: “Path(s) to command directories.”
- Line 217, the `lspServers` field description: “Path to an LSP configuration file, or inline server definitions.”
- Line 109 documents that a manifest without a recognized Agent Plugins schema uses the legacy format.

Thus a documented legacy plugin can declare command directories and LSP configuration without opting into Agent Plugins. This is a documentation counterexample, not an executed client probe. [INFERENCE] A reader interpreting “adds” as a format capability boundary would incorrectly rule those components out of a legacy-plugin audit. The word can also mean merely “adds to this row's preceding list”; that weaker reading is not falsified. Do not promote this ambiguity into a claim that the listed components do not exist.

The candidate fixes the important distinction: `com.github.copilot` is the client-specific directory in Agent Plugins 1.0, not evidence that legacy plugins lack commands/LSP. Its component list is supported directly by `plugins-creating.md:21`, and the reference supplies exact paths at `cli-plugin-reference.md:154-164`.

Smallest safe correction: replace the tip cells with the candidate cells, with only `can name` / `can declare` added in the legacy parentheticals. That small modal clarification avoids implying that legacy path fields are mandatory: `plugins-creating.md:71` allows default locations, and `cli-plugin-reference.md:207` says “All are optional. The CLI uses default conventions if omitted.” This is a precision improvement, not a separately proven false assertion in the candidate.

### F2 — component-by-component check; no fabricated listed part

Quotes below are contiguous, byte-exact substrings of their named fetched lines, each at most 25 words. No Markdown bytes inside a quotation were stripped.

| Part or qualifier in the recommended cells | Live line evidence | Assessment |
|---|---|---|
| agents, skills, hooks, MCP server configurations | `plugins-creating.md:14`: “A plugin can also contain any combination of agents, skills, hooks, and MCP server configurations.” The legacy manifest example repeats all four fields at `:58-61`. | Supported in tip and candidate. |
| Agent Plugins 1.0 Copilot-specific agents, commands, rules, hooks and LSP servers | `plugins-creating.md:21`: “Copilot-specific components such as agents, commands, rules, hooks, and LSP servers come from the `com.github.copilot` directory in the plugin.” | All five types are explicitly named. No listed type is invented. |
| These are client-specific rather than portable Agent Plugins components | `cli-plugin-reference.md:152`: “Agent Plugins 1.0 does not define portable agents, hooks, commands, rules, or LSP servers.” Skills and MCP are the two portable types at `:143-148`; also `plugins-creating.md:18,21`. | Candidate's qualifier holds; it is not a claim that the CLI cannot load these parts. |
| `com.github.copilot` is a directory, not a manifest path or JSON namespace key | `plugins-creating.md:21,69`; exact component locations at `cli-plugin-reference.md:158-162`: agents directory, commands directory, rules directory, hooks JSON, LSP JSON. | Candidate's directory statement holds. The manifest's `extensions` data map is distinct (`plugins-creating.md:48`; `cli-plugin-reference.md:128,152`). |
| Legacy plugins can name component paths in `plugin.json` | `plugins-creating.md:50-63,71`; `cli-plugin-reference.md:205-217`, particularly optionality/defaults at `:207`. | Supported, with optionality made explicit in the proposed wording. |
| Legacy `commands` and `lspServers` fields | `cli-plugin-reference.md:213,217`, under the legacy heading at `:183`. | Candidate examples and their cited line numbers hold exactly. |

Missing instruction-bearing types: S082's explicit list at `plugins-creating.md:14,21` is fully represented in both the tip and candidate: agents, skills, hooks, MCP servers, commands, rules, LSP servers. The tip omits the namespaced location/format distinction, not an eighth listed type. The guide's fixed portable locations (`:69`, `skills/` and root `mcp.json`) are further routing detail, not additional component kinds.

The additionally cited S028 page documents agent-scoped `mcp-servers` (`cli-plugin-reference.md:219-237`), already within the cells' agents/MCP categories. It also documents legacy extension directories (`:215`), but that line does not establish their instruction-bearing contents. I do not infer an additional instruction surface from the word “extensions” alone, and make no client-wide silence/absence claim. The Agent Plugins `extensions` map and the legacy extension-directory field must not be conflated.

### F3 — citation audit

- Tip `S082 plugins-creating.md:14-21,48-71`: all cited ranges exist. `:14` holds the four initial components; `:21` holds all five Copilot-specific names and the directory; `:48-71` holds format/schema and path details. No displaced or nonexistent cited line was found for this row. The weakness is the summary's “adds” wording, not fabricated quotation provenance.
- Candidate keeps those S082 ranges and adds `S028 cli-plugin-reference.md:152,213,217`: `:152` is exactly the nonportable-components statement; `:213` is the legacy `commands` field; `:217` is legacy `lspServers`. Every cited candidate line holds its claimed text. The directory is supported by S082 `:21` even though S028 `:152` alone does not name Copilot's directory.
- For the recommended optionality wording, add S028 `:207`; the retained S082 `:71` independently supports defaults.

## Exact old → new text to land

Choice: my own cells, differing from the untrusted candidate only by making the legacy path declarations explicitly optional. Manifest and action cells remain unchanged.

### `SKILL.md:120`, ship cell

Old at the assigned tip:

```text
agents, skills, hooks, MCP server configs; Agent Plugins adds commands, rules, LSP servers
```

New:

```text
agents, skills, hooks, MCP server configs; in Agent Plugins 1.0 the Copilot-specific agents, commands, rules, hooks and LSP servers come from `com.github.copilot` (legacy plugins can name component paths in `plugin.json`)
```

Candidate → new: replace exactly `legacy plugins name component paths` with `legacy plugins can name component paths`; leave its other cell bytes unchanged.

### `corpus/knowledge/plugin-manifests-round57.md:45`, ship cell

Old at the assigned tip:

```text
agents, skills, hooks, MCP server configurations; Agent Plugins 1.0 adds Copilot-specific commands, rules and LSP servers
```

New:

```text
agents, skills, hooks, MCP server configurations; in Agent Plugins 1.0, Copilot-specific agents, commands, rules, hooks and LSP servers come from `com.github.copilot` (legacy plugins can declare component paths such as `commands` and `lspServers` in `plugin.json`)
```

Candidate → new: replace exactly `legacy plugins declare component paths` with `legacy plugins can declare component paths`; leave its other ship-cell bytes unchanged.

Matching source cell, old at tip:

```text
S082 `plugins-creating.md:14-21,48-71`
```

Matching source cell, old in candidate:

```text
S082 `plugins-creating.md:14-21,48-71`; S028 `cli-plugin-reference.md:152,213,217`
```

Matching source cell, new:

```text
S082 `plugins-creating.md:14-21,48-71`; S028 `cli-plugin-reference.md:152,207,213,217`
```

## Boundaries and checks

No lane content or counter was edited; only this report was written in the lane. The clone/checkout command succeeded with exit 0, with writes confined to my sandbox. The two curl/hash/count chains above were exercised. No client runtime, counter, test suite, judge, model call, browser, or alternate orchestration runtime was invoked. No tools were installed or upgraded.

The cells are explicitly outside C1's measured predicate (`plans/round-57.md:42-43`; knowledge entry `:73-74`). These findings therefore do not turn the declared measured C1 miss into a pass, nor establish any new manifest/token count. Integration and any requested final verification belong to the L1.
