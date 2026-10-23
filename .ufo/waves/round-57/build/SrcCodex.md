Result: DONE — OpenAI’s Codex plugin build guide documents a JSON manifest, supported plugin contents, and a source-backed S080 draft.

## Finding

**Manifest token:** `.codex-plugin/plugin.json` (the page calls this a supported Codex compatibility manifest). The same page says portable Agent Plugins packages use root `plugin.json` (`build-plugins.md:14-26, 76-89`). The token is taken verbatim from the documentation; this report does not claim that the frozen counter was run.

**Exact quote (22 words), from the fetched bytes, with source line breaks retained and no bytes removed** (`build-plugins.md:135-137`):

```text
The plugin-creator skill will create the plugin folder, create a supported
`.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring
for the plugin.
```

The token is verbatim and “plugin” also occurs outside it (“plugin folder” and “for the plugin”). For the one-line entry-row draft below, the two source line breaks (after “supported” and “wiring”) are folded to spaces to fit the SOURCES table; the quote block above preserves the original breaks.

**What the build guide documents:**
- Portable packages have root `plugin.json`; the plugin folder may include `skills/`, `mcp.json`, optional assets, and lifecycle hooks for manually installed Codex desktop plugins (`build-plugins.md:14-22`).
- OpenAI-specific presentation, MCP server mappings, and hook settings go under `extensions.com.openai` in root `plugin.json`; `.codex-plugin/plugin.json` remains a supported compatibility fallback (`:24-30`).
- The Codex compatibility scaffold lists `.mcp.json`, `.app.json`, `skills/`, `hooks/`, `scripts/`, and `assets/`; only `.codex-plugin/plugin.json` is always created. The MCP and app files carry `mcpServers` and `apps` objects; skills are under `skills/` (`:61-80`). A requested `hooks/` directory is empty until `hooks/hooks.json` and scripts are added (`:82-89`).
- Portable examples put the plugin manifest at the plugin root (`:220-245`). For authoring locations, repo examples use `$REPO_ROOT/plugins/`, personal examples use `~/.codex/plugins/`, and the marketplace `source.path` selects the actual plugin folder (`:278-334, 343-346, 459-466`). Those are plugin-folder examples, not alternate manifest paths.
- This page does not document agents/subagents, packaged command files, rule/context files, or LSP as plugin parts; no claim is made for them. The separate overview page fetched as a companion lists skills, MCP servers, browser extensions, and hooks (`codex-plugins.md:80-99`), but it does not replace the build guide’s manifest evidence.

## Draft rows

SOURCES header read at `corpus/SOURCES.md:12`; S072–S078 were read at `:85-91` to match the 11-column format. The requested URL did not appear in the base SOURCES search, and S080 was not already present.

```text
| S080 | OpenAI Developers — Package your plugin — https://developers.openai.com/plugins/build/plugins.md | docs | A | Codex Agent Plugins manifest locations and documented package contents (vendor documentation; not runtime behavior) | § Portable Agent Plugins package (`plugins.md:14-30`); § Plugin creator output (`:61-89`); § Create a plugin manually (`:220-267`); fetched 2026-10-23T04:47:08Z, HTTP 200, 38,036 B, sha256 `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1` (seat SrcCodex) | Portable packages use root `plugin.json`; Codex supports `.codex-plugin/plugin.json` as a compatibility manifest. Docs list skills, MCP configuration, optional assets, and lifecycle hooks (manual Codex desktop only); the compatibility scaffold also has optional app mappings, scripts, and hook files | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |
```

```text
| Codex | `.codex-plugin/plugin.json` (portable root `plugin.json`; repo plugin folders under `$REPO_ROOT/plugins/`, personal example `~/.codex/plugins/`; marketplace `source.path` is configurable) | Skills under `skills/`; MCP servers via `mcp.json` (Codex scaffold: `.mcp.json`); lifecycle hooks via `hooks/`, `hooks/hooks.json`, and scripts (manually installed desktop plugins); optional assets; scaffold also supports `.app.json` app mappings and scripts | Inspect the manifest before trusting bundled instructions |
```

```text
| Codex | `.codex-plugin/plugin.json` | S080 | "The plugin-creator skill will create the plugin folder, create a supported `.codex-plugin/plugin.json` compatibility manifest, and add MCP server wiring for the plugin." |
```

The entry quote cell is whitespace-folded as noted above; the exact fetched quote is the line-preserving block in Findings. No `## Gate` update is included in this leaf report.

## Provenance and commands

Fetched with `curl` and retained under `/fast/scratch/hyaku/kotoba-r57/SrcCodex/`.

1. Overview fetch command: `mkdir -p /fast/scratch/hyaku/kotoba-r57/SrcCodex && timeout 45s bash -c 'set -e; date -u; curl -L --max-time 30 --max-filesize 5242880 -sS -o /fast/scratch/hyaku/kotoba-r57/SrcCodex/codex-plugins.md -w "http_status=%{http_code}\nfinal_url=%{url_effective}\nbytes=%{size_download}\n" https://developers.openai.com/codex/plugins.md; sha256sum /fast/scratch/hyaku/kotoba-r57/SrcCodex/codex-plugins.md; wc -c /fast/scratch/hyaku/kotoba-r57/SrcCodex/codex-plugins.md'`
   - `date -u`: `Fri Oct 23 04:46:52 AM UTC 2026`
   - Input URL: `https://developers.openai.com/codex/plugins.md`; final URL: `https://learn.chatgpt.com/docs/plugins.md`; HTTP 200; 14,241 bytes; sha256 `612ebfed2779c4aa5c412d8b069ed723e8c2ea264a140ebed5ad52a0853d4db0`; `wc -c` = `14241`.
2. Build-guide fetch command: `timeout 45s bash -c 'set -e; date -u; curl -L --max-time 30 --max-filesize 5242880 -sS -o /fast/scratch/hyaku/kotoba-r57/SrcCodex/build-plugins.md -w "http_status=%{http_code}\nfinal_url=%{url_effective}\nbytes=%{size_download}\n" https://developers.openai.com/plugins/build/plugins.md; sha256sum /fast/scratch/hyaku/kotoba-r57/SrcCodex/build-plugins.md; wc -c /fast/scratch/hyaku/kotoba-r57/SrcCodex/build-plugins.md'`
   - `date -u`: `Fri Oct 23 04:47:08 AM UTC 2026`
   - Input and final URL: `https://developers.openai.com/plugins/build/plugins.md`; HTTP 200; 38,036 bytes; sha256 `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1`; `wc -c` = `38036`.
3. `functions.grep` on `corpus/SOURCES.md`, pattern `developers\.openai\.com/plugins/build/plugins|learn\.chatgpt\.com/docs/build-plugins` → `No matches found`. `functions.grep` for `| S080 |` → `No matches found`.

## Gates, touched surfaces, limits

- Both fetches were below the 5 MiB cap; observed HTTP status was 200. URLs are on the counter’s pinned Codex hosts. The S080 URL is not a base SOURCES URL.
- No Q30 “no manifest” sweep was run because the live official page explicitly documents JSON manifests. No `--fetch` counter run, sandbox commit, build, test, or plugin execution was performed; therefore this is source evidence and row drafting only, not a C1 predicate receipt or runtime-behavior claim.
- Only the two fetched Markdown files in the named scratch directory and this report were written. No lane product files, judge/counters, lesson, commit, or C2 surface was changed. No tools were installed or updated.

Artifacts: `/fast/scratch/hyaku/kotoba-r57/SrcCodex/codex-plugins.md`; `/fast/scratch/hyaku/kotoba-r57/SrcCodex/build-plugins.md`; `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/build/SrcCodex.md`.
