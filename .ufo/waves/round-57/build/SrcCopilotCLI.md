Result: PARTIAL — the official creation guide documents a root `plugin.json` and component types, but its only evidenced token is rejected by frozen C1 v2.

## Findings

The fetched official GitHub Docs creation guide says an Agent Plugins 1.0 manifest is at the plugin root and that legacy plugins have additional locations, but this page does not enumerate those legacy paths. Its exact manifest token is `plugin.json`; that is a real JSON manifest, not evidence that Copilot CLI has no JSON manifest. The frozen counter explicitly rejects bare `plugin.json` because it has one path segment and contains no Copilot marker (`verifiers/check_plugin_manifests.py:71-89`). Therefore the draft rows below are factually sourced but **not eligible for C1 v2 counting**. No alternative path was invented. `[INFERENCE]` This Copilot row will not be backed by the frozen counter if submitted with this source/token.

### Fetch provenance

- UTC line: `Fri 23 Oct 2026 04:47:14 AM UTC`.
- Actual curl URL argument: `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md`.
- Final URL: `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md`.
- HTTP status: 200; downloaded bytes: 7,711 (`wc -c` also returned 7,711); sha256: `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64`.
- Saved bytes: `/fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/plugins-creating.md`.
- The first curl `--write-out` label printed `requested_url=https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating` (missing `.md`); the URL argument and final URL above include `.md`.
- Duplicate-URL search: `functions.grep` for `docs\.github\.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating` in `corpus/SOURCES.md` returned `No matches found`.

The fetched bytes contain this single-page quote at line 27 (17 words, including the list marker; no bytes removed):

> 2. Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory.

The token is `plugin.json`. The quote includes “plugin” outside the token. It meets the quote length/content shape but the token fails C1 v2.

### What a plugin can ship (documented facts)

- Any combination of agents, skills, hooks, and MCP server configurations (line 14).
- Agent Plugins 1.0 is described as portable for skills and MCP servers; the legacy Copilot format supports Copilot-specific components and configurable component paths (lines 18-21).
- The guide specifically names Copilot-specific agents, commands, rules, hooks, and LSP servers as coming from `com.github.copilot` (line 21).
- For Agent Plugins 1.0, skills are immediate subdirectories of `skills/`, each with `SKILL.md`; MCP configuration is root `mcp.json`; Copilot-specific components include `com.github.copilot/agents/` and `com.github.copilot/hooks/hooks.json` (lines 69-70).
- Legacy plugins may use default component locations or paths configured in `plugin.json` (line 71); examples show `agents`, `skills`, `hooks`, and `mcpServers` fields (lines 50-62).

### Draft rows (not counter-eligible)

SOURCES column shape, proposed S082:

    | S082 | GitHub Docs — Creating a plugin for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md | docs | A | Copilot CLI plugin manifest location, supported formats, and documented component types (vendor documentation; not runtime behavior) | § Plugin structure (`plugins-creating.md:14-21`); § Creating a plugin (`:27`, `:48-71`); fetched 2026-10-23T04:47:14Z, HTTP 200, 7,711 B, sha256 `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64` (seat SrcCopilotCLI) | Copilot CLI's creation guide places `plugin.json` at the plugin directory root and documents agents, skills, hooks, MCP server configurations, and Agent Plugins 1.0 Copilot-specific commands, rules, and LSP servers | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |

Draft SKILL.md row (the first backticked span is the exact page token; it fails the frozen token rule):

    | Copilot CLI | `plugin.json` (Agent Plugins 1.0 at plugin root; this page does not enumerate legacy locations) | agents, skills, hooks, MCP server configurations; Agent Plugins 1.0 also has Copilot-specific agents, commands, rules, hooks, and LSP servers | Check the plugin manifest before reading bundled skills |

Draft knowledge-entry row:

    | Copilot CLI | `plugin.json` | S082 | "2. Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory." |

### Gates, scope, and limits

- Source fetch: HTTP 200, recorded above. This was a documentation read, not a test of plugin loading/runtime behavior.
- New source URL: no match in `corpus/SOURCES.md` for the creation-guide host/path; it differs from existing S028's CLI plugin-reference path.
- Frozen C1 v2 token gate: fails by inspection; no counter was run and no sandbox commit was made.
- Q30 sweep: not run because this page confirms a JSON manifest exists.
- An alternate discovery attempt at `https://docs.github.com/en/copilot/reference/cli-plugin-reference.md` returned HTTP 404 (502 B, sha256 `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522`; UTC line `Fri 23 Oct 2026 04:50:00 AM UTC`). It is not used as a source. The path containing the detailed legacy discovery list is the existing CLI plugin-reference base URL, which is not a permitted new SOURCES URL for C1.
- No files outside this scoped report and the scratch fetch artifacts were written; no tool was installed. C2 and all verifier/code changes are out of scope.

## Exact fetch commands

Primary page:

```sh
mkdir -p /fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI && date -u && timeout 30s curl -L --silent --show-error --output /fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/plugins-creating.md --write-out 'requested_url=https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating\nfinal_url=%{url_effective}\nhttp_status=%{http_code}\nbytes_downloaded=%{size_download}\n' https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md && wc -c < /fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/plugins-creating.md && sha256sum /fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/plugins-creating.md
```

Alternate route check:

```sh
date -u && timeout 30s curl -L --silent --show-error --output /fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/cli-plugin-reference-alternate.md --write-out 'requested_url=https://docs.github.com/en/copilot/reference/cli-plugin-reference.md\nfinal_url=%{url_effective}\nhttp_status=%{http_code}\nbytes_downloaded=%{size_download}\n' https://docs.github.com/en/copilot/reference/cli-plugin-reference.md && wc -c < /fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/cli-plugin-reference-alternate.md && sha256sum /fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/cli-plugin-reference-alternate.md
```

## Touched surfaces and artifact paths

- Written: `.ufo/waves/round-57/build/SrcCopilotCLI.md` (this report) only.
- Fetched source: `/fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/plugins-creating.md`.
- Failed alternate fetch: `/fast/scratch/hyaku/kotoba-r57/SrcCopilotCLI/cli-plugin-reference-alternate.md`.
- Product files, counters, source registry, knowledge entry, lesson, and SKILL.md were not edited.