Result: DONE — Cursor’s official plugin docs provide a byte-exact, eligible `.cursor-plugin/plugin.json` citation and document both plugin formats and their components.

## Findings and behavior

- The official page distinguishes Agent Plugins (root `plugin.json`) from Cursor Plugins (`.cursor-plugin/plugin.json`); both may be installed from marketplaces. Cursor Plugins add Cursor-specific components; Agent Plugins are the portable format for skills and MCP servers. The source page is on the frozen counter’s pinned `cursor.com` host (`verifiers/check_plugin_manifests.py:240`).
- Eligible manifest token for the Cursor row: `.cursor-plugin/plugin.json`. It is the client-specific Cursor Plugin path, has two path segments, and its final `.json` segment contains `plugin`; it has no `marketplace` segment. The v2 token conditions are in `verifiers/check_plugin_manifests.py:535-558`.
- The page’s component evidence:
  - Line 3: plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundles.
  - Lines 9, 13-18: a plugin can combine components; rules, agents, commands, and hooks are marked Cursor Plugins, while skills and MCP servers are available in both formats.
  - Lines 22-28: Agent Plugins package portable skills and MCP servers; the page names their root `plugin.json` and Cursor Plugins’ `.cursor-plugin/plugin.json`, followed by the Cursor-specific rules, agents, commands, and hooks.
  - Lines 27-30 and 255-258: Cursor Plugins can also use variables; the page recommends Agent Plugins for portable skills/MCP servers and Cursor Plugins when Cursor-specific components are needed.
  - Lines 283-298: Cursor Plugin directory example and default/custom component-directory discovery.
  - Lines 315-320: `~/.cursor/plugins/local` is a local development/test location for either plugin format, not another manifest path.
- No bytes were removed or reshaped from the cited quote. It is fetched-byte line 28 (16 whitespace-delimited words):

  > - **Cursor Plugins**: plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and [variables](https://cursor.com/docs/reference/plugins.md#variables)

## Draft rows for L1 integration

SOURCES column order follows `corpus/SOURCES.md:12-13`; adjacent S072-S078 rows are at `corpus/SOURCES.md:85-91`.

```markdown
| S084 | Cursor Docs — Plugins — https://cursor.com/docs/plugins.md | docs | A | Cursor's documented manifest paths and components for Agent Plugins and Cursor Plugins | § What plugins contain (`plugins.md:9-18`); § The Agent Plugins standard (`:22-30`); § Creating plugins and format layouts (`:253-298`); fetched as https://cursor.com/docs/plugins.md (200, 20,323 B, sha256 `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62`) at 2026-10-23T04:46:52Z (seat SrcCursor) | Agent Plugins use a root `plugin.json` and package skills/MCP servers; Cursor Plugins use `.cursor-plugin/plugin.json` and can add rules, skills, agents, commands, MCP servers, hooks, and variables | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |
```

```markdown
| Cursor | `.cursor-plugin/plugin.json` (+ root `plugin.json` for Agent Plugins; local development folder `~/.cursor/plugins/local`) | Cursor Plugins: rules, skills, agents, commands, MCP servers, hooks, variables; Agent Plugins: skills and MCP servers | Choose the plugin format before packaging |
```

```markdown
| Cursor | `.cursor-plugin/plugin.json` | S084 | "- **Cursor Plugins**: plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and [variables](https://cursor.com/docs/reference/plugins.md#variables)" |
```

The one quote above is also the exact quote to record in `corpus/lessons/round-57.md` under `## Gate` for counter quote-in-gate coverage.

## Fetch provenance and checks

- Exact fetch command (exit 0):
  `mkdir -p /fast/scratch/hyaku/kotoba-r57/SrcCursor && date -u && timeout 90s curl -L -sS --max-time 80 -D /fast/scratch/hyaku/kotoba-r57/SrcCursor/plugins.headers -o /fast/scratch/hyaku/kotoba-r57/SrcCursor/plugins.md -w 'requested_url=https://cursor.com/docs/plugins.md\nfinal_url=%{url_effective}\nhttp_status=%{http_code}\nbytes=%{size_download}\n' https://cursor.com/docs/plugins.md && sha256sum /fast/scratch/hyaku/kotoba-r57/SrcCursor/plugins.md && wc -c /fast/scratch/hyaku/kotoba-r57/SrcCursor/plugins.md`
- Observed `date -u` line: `Fri 23 Oct 2026 04:46:52 AM UTC`.
- Requested URL: `https://cursor.com/docs/plugins.md`; final URL after redirects: `https://cursor.com/docs/plugins.md`; HTTP 200; 20,323 bytes; sha256 `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62`. `wc -c` returned `20323`.
- Base-SOURCES URL check command: `grep -n 'cursor.com/docs/plugins' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md; printf 'grep exit=%s\n' "$?"`. Observed no matches and `grep exit=1`; thus this URL is not already present in the lane SOURCES file.
- This is a positive documentation finding, not a Q30 “nothing documented” claim; the Q30 sweep was not applicable.
- No sandbox commit or frozen `--fetch` counter run was made, so there is no C1 predicate/F/K/G result from this seat. No product files, counters, or lesson were edited; rows above are drafts for integration. No tools were installed or updated.

## Gates, touched surfaces, limits

- Passed for this scoped source assignment: fetched the official pinned-host documentation; captured date, requested/final URL, status, byte count, and digest; confirmed the source URL is not in base SOURCES; found a byte-exact 6–25-word quote containing the eligible token and `plugins` outside it; drafted the S084, SKILL.md, and entry rows.
- Touched artifacts: `/fast/scratch/hyaku/kotoba-r57/SrcCursor/plugins.md`, `/fast/scratch/hyaku/kotoba-r57/SrcCursor/plugins.headers`, and this report `.ufo/waves/round-57/build/SrcCursor.md`. Product surfaces intentionally unchanged by this leaf: `corpus/SOURCES.md`, `SKILL.md`, `corpus/knowledge/plugin-manifests-round57.md`, and `corpus/lessons/round-57.md`.
- Limits: these drafts establish only Cursor’s documented formats and the cited contents; they do not establish runtime loading behavior, completeness of all plugin capabilities, or the round-wide C1 predicate. The counter itself describes runtime/completeness as out of its scope (plan `plans/round-57.md:42-43`).