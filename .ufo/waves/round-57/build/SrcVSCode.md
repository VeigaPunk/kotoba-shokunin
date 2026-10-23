Result: DONE — sourced a documented VS Code plugin manifest path and drafted the S081/SKILL.md/entry rows with the format limitation explicit.

## Findings

The official VS Code authoring reference identifies these formats and manifest locations: Agent Plugins 1.0 and Copilot use root `plugin.json`; Claude uses `.claude-plugin/plugin.json`; Legacy OpenPlugin uses `.plugin/plugin.json` (`agent-plugin-reference.md:97-104`). VS Code says it auto-detects formats from the root manifest and format-specific paths (`:97`), so `.plugin/plugin.json` is a documented VS Code-recognized manifest path, specifically for the Legacy OpenPlugin format—not the universal/default VS Code path. The generic root token `plugin.json` is not a viable C1 token: the frozen v2 grammar rejects its single path segment without the `vscode` marker (`verifiers/check_plugin_manifests.py:71-95`).

The proposed token `.plugin/plugin.json` has two path segments, its final segment is `plugin.json`, it names no other frozen client, and the read-only base-revision search found no held occurrence. Its quote is the adjacent two-row excerpt below, byte-for-byte from the fetched Markdown at lines 103–104 (11 whitespace-separated words); `plugin` appears outside the target token in the Claude-format path. No source bytes are removed. The draft entry cell HTML-entity-encodes the quote's pipe characters (`&#124;`) only to keep the quote inside one Markdown table cell; entity decoding reproduces the source bytes.

Across supported formats, the reference documents portable skills (instructions, scripts, resources) and MCP servers, plus client-specific agents, hooks, automation templates, and slash commands (`:11-22`). VS Code reads custom agents, commands, rules, hooks, and automation path configuration from `com.github.copilot` (`:73-85, 379`). Agent Plugins automation templates are VS Code-specific and carry reusable prompts/schedules (`:121-128`); MCP servers provide additional tools and data sources and use root `mcp.json` for Agent Plugins 1.0 (`:203-212`); hooks run shell commands at agent lifecycle points and are client-specific (`:293-314`). The reference cautions that supported components vary by format/client (`:11, 97-104, 377-392`). No LSP or context-file component is claimed from these pages.

### Exact source quote

Source lines 103–104:

```text
| Claude | `.claude-plugin/plugin.json` |
| Legacy OpenPlugin | `.plugin/plugin.json` |
```

### Draft SOURCES row

```text
| S081 | VS Code — Agent plugin authoring reference — https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | docs | A | VS Code's documented agent-plugin manifest formats and the capabilities available across them (vendor documentation; not a runtime test) | § Package structure (`agent-plugin-reference.md:11-22`); § Plugin manifest (`:45-47,71-85`); § Plugin formats (`:97-104`); § Automations (`:121-128`); § MCP servers (`:203-212`); § Hooks (`:291-314`); § Cross-tool compatibility (`:375-392`) | VS Code documents root `plugin.json` for Agent Plugins 1.0 and Copilot, `.claude-plugin/plugin.json` for Claude, and `.plugin/plugin.json` for Legacy OpenPlugin; packages can ship portable skills and MCP servers plus client-specific agents, commands, rules, hooks, automation templates, and slash commands | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |
```

### Draft SKILL.md row

```text
| VS Code | `.plugin/plugin.json` (Legacy OpenPlugin; Agent Plugins 1.0/Copilot use root `plugin.json`; Claude uses `.claude-plugin/plugin.json`) | Across formats: portable skills and MCP servers; client-specific custom agents, hooks, automation templates, and slash commands; VS Code reads agents, commands, rules, and hooks from `com.github.copilot/` | Check plugin format before moving components |
```

### Draft entry row

```text
| VS Code | `.plugin/plugin.json` | S081 | "&#124; Claude &#124; `.claude-plugin/plugin.json` &#124; &#124; Legacy OpenPlugin &#124; `.plugin/plugin.json` &#124;" |
```

## Fetch and gates

Both fetches were ordinary `curl -sSL --fail-with-body` requests, saved under the seat scratch directory; no browser was used.

1. Executed:

```sh
timeout 90s bash -c 'set -o pipefail; mkdir -p /fast/scratch/hyaku/kotoba-r57/SrcVSCode/sources; date -u; url="https://code.visualstudio.com/docs/agent-customization/agent-plugins.md"; printf "URL: %s\n" "$url"; curl -sSL --fail-with-body -w "FINAL_URL: %{url_effective}\nHTTP_STATUS: %{http_code}\nBYTES: %{size_download}\n" "$url" -o /fast/scratch/hyaku/kotoba-r57/SrcVSCode/sources/agent-plugins.md; rc=$?; printf "CURL_EXIT: %s\n" "$rc"; if [ "$rc" -eq 0 ]; then sha256sum /fast/scratch/hyaku/kotoba-r57/SrcVSCode/sources/agent-plugins.md; fi; exit "$rc"'
```

Output: `Fri Oct 23 04:47:03 AM UTC 2026`; URL and final URL `https://code.visualstudio.com/docs/agent-customization/agent-plugins.md`; HTTP 200; 16,711 bytes; curl exit 0; SHA-256 `b717e6f2bf05db2e161ffef8fe82d1002ccea452c7a45d91dc95d7505153757e`.

2. Executed:

```sh
timeout 90s bash -c 'set -o pipefail; date -u; url="https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md"; printf "URL: %s\n" "$url"; curl -sSL --fail-with-body -w "FINAL_URL: %{url_effective}\nHTTP_STATUS: %{http_code}\nBYTES: %{size_download}\n" "$url" -o /fast/scratch/hyaku/kotoba-r57/SrcVSCode/sources/agent-plugin-reference.md; rc=$?; printf "CURL_EXIT: %s\n" "$rc"; if [ "$rc" -eq 0 ]; then sha256sum /fast/scratch/hyaku/kotoba-r57/SrcVSCode/sources/agent-plugin-reference.md; fi; exit "$rc"'
```

Output: `Fri Oct 23 04:47:13 AM UTC 2026`; URL and final URL `https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md`; HTTP 200; 21,972 bytes; curl exit 0; SHA-256 `d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e`.

The pinned-host SOURCES reuse search (`functions.grep`, pattern `code\.visualstudio\.com/docs/agents/reference/agent-plugin-reference`, `corpus/SOURCES.md`) returned “No matches found”; this URL is not a base SOURCES URL. The read-only base query `timeout 30s bash -c 'git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n -F ".plugin/plugin.json" 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- . ":!.ufo"; rc=$?; printf "GIT_GREP_EXIT: %s\n" "$rc"; exit 0'` printed `GIT_GREP_EXIT: 1` with no matches. The frozen counter was not run; no C1 predicate result is claimed.

Q30 is not applicable: the opened documentation explicitly lists JSON manifests, including the VS Code-recognized `.plugin/plugin.json`. No changelog/release-note + docs-source-tree + corpus sweep was performed, and no “no manifest” claim is made.

## Touched surfaces and limits

- Wrote only this scoped report in the lane. No product files, SOURCES, lesson, entry, SKILL.md, frozen counter, or verifier were edited; no lane Git/jj writes, sandbox clone/commit, tests, or counter execution.
- Fetched artifacts: `/fast/scratch/hyaku/kotoba-r57/SrcVSCode/sources/agent-plugins.md` and `/fast/scratch/hyaku/kotoba-r57/SrcVSCode/sources/agent-plugin-reference.md`.
- Report: `.ufo/waves/round-57/build/SrcVSCode.md`.
- No tools installed or updated.