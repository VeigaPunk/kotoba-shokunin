Result: DONE — Claude Code’s official docs identify `.claude-plugin/plugin.json` and enumerate the plugin’s standard component inventory for S079.

## Findings

- **Manifest token:** `.claude-plugin/plugin.json`. The reference says “Save the manifest at `.claude-plugin/plugin.json` under the plugin root.” This is a byte-exact quote from fetched `plugins-reference.md:34`, 9 whitespace-delimited words; no bytes were removed or shaped. It includes the token and “plugin” outside it. The reference also identifies the manifest as optional (`plugins-reference.md:617`). The token has two path segments, ends in `plugin.json`, carries this client’s `claude` marker in `.claude-plugin`, and names no other client.
- **What the docs say a plugin can ship** (all line numbers refer to the fetched bytes):
  - Skills: `skills/`, one `<name>/SKILL.md` per skill; a root `SKILL.md` can load as a single skill (`plugins-reference.md:618`).
  - Flat Markdown commands (`:619`); agent Markdown files (`:620`); hook configuration (`:621`).
  - MCP server definitions (`.mcp.json`, `:622`) and LSP server configurations (`.lsp.json`, `:623`).
  - Output-style Markdown (`:624`), workflow `.js` files (`:625`), theme JSON (`:626`), and a monitors array (`:627`).
  - Executables in `bin/` are put on the Bash tool’s PATH while enabled; the page notes claude.ai and Cowork do not install plugins containing this directory (`:628`). `settings.json` can provide `agent` and `subagentStatusLine` defaults (`:629`).
  - The manifest’s component-key table independently describes skills, commands, agents, hooks, MCP, LSP, output styles, and workflows (`plugins-reference.md:148-155`). The standard-layout table does not designate a standalone rules/context-file component (`:617-629`); this report does not claim one is loaded. The page does say other plugin files belong at the plugin root (`:34`), which alone does not establish loader behavior for arbitrary files.
- **User/other locations:** the manifest path is relative to the plugin root (`plugins-reference.md:34`). The official overview says fetched/installed plugin data is held under `~/.claude/plugins/` (`plugins.md:82`); scopes are user, project (committed `.claude/settings.json`), and local (`:99-107`). For development, a plugin can be loaded straight from its folder with `--plugin-dir` (`:75`). These are storage/scope facts, not alternate manifest-relative paths.

## Draft rows

SOURCES row in the existing 11-column shape (`SOURCES.md:12-13`); tier A, status mined, opened 2026-10-23:

```markdown
| S079 | Claude Code Docs — Plugin manifest and component reference — https://code.claude.com/docs/en/plugins-reference.md; plugin overview — https://code.claude.com/docs/en/plugins.md | docs | A | Claude Code plugin manifest path and standard component inventory; installed plugin location, scopes, and folder-based development loading (vendor documentation, not a runtime measurement) | § Standard layout (`plugins-reference.md:617-629`); manifest path (`:34`); plugin overview on disk and install scopes (`plugins.md:82, 99-109`); fetched 2026-10-23T04:46:45Z and 2026-10-23T04:47:05Z, HTTP 200 for both; byte counts and sha256 below | When present, Claude Code’s manifest is `.claude-plugin/plugin.json` under the plugin root. The documented standard layout includes skills, Markdown commands and agents, hooks, MCP/LSP configs, output styles, workflows, themes, monitors, executables, and settings; the overview documents `~/.claude/plugins/` and user/project/local scopes | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |
```

Draft SKILL.md table row (first backticked span in the manifest cell is the token):

```markdown
| Claude Code | `.claude-plugin/plugin.json` (under plugin root; installed copy at `~/.claude/plugins/`; user/project/local enablement; project settings `.claude/settings.json`; local development with `--plugin-dir`) | Skills; Markdown commands and agents; hooks; MCP/LSP server configurations; output styles; JS workflows; themes; monitors; executables; settings | Audit the plugin root and manifest |
```

Draft entry row (`Manifest` cell is the token; quote is verbatim):

```markdown
| Claude Code | .claude-plugin/plugin.json | S079 | "Save the manifest at `.claude-plugin/plugin.json` under the plugin root." |
```

## Fetch and provenance

Saved response bodies and headers are under `/fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/`.

1. Command (exit 0):
   `mkdir -p /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode && date -u && timeout 60 curl -sSL --max-time 45 -D /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins-reference.headers -o /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins-reference.md -w 'effective_url=%{url_effective}\nhttp_code=%{http_code}\nsize_download=%{size_download}\n' https://code.claude.com/docs/en/plugins-reference.md && wc -c /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins-reference.md && sha256sum /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins-reference.md`
   Output: `Fri 23 Oct 2026 04:46:45 AM UTC`; `effective_url=https://code.claude.com/docs/en/plugins-reference.md`; `http_code=200`; `size_download=42124`; `42124 /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins-reference.md`; sha256 `f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e`.
2. Command (exit 0):
   `date -u && timeout 60 curl -sSL --max-time 45 -D /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins.headers -o /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins.md -w 'effective_url=%{url_effective}\nhttp_code=%{http_code}\nsize_download=%{size_download}\n' https://code.claude.com/docs/en/plugins.md && wc -c /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins.md && sha256sum /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins.md`
   Output: `Fri 23 Oct 2026 04:47:05 AM UTC`; `effective_url=https://code.claude.com/docs/en/plugins.md`; `http_code=200`; `size_download=13454`; `13454 /fast/scratch/hyaku/kotoba-r57/SrcClaudeCode/plugins.md`; sha256 `9f50044fa9a2c7c939f6e82cb2edb2a4c854f9fe814a528ae84098125436ee32`.
3. Search of `corpus/SOURCES.md` for `code\.claude\.com/docs/en/plugins-reference|plugins-reference\.md|plugins\.md` returned **No matches found**. The proposed source URLs are not existing base SOURCES URLs.

## Gates, touched surfaces, and limits

- Positive manifest evidence was found, so the Q30 negative-evidence sweep (release notes, docs source tree, corpus grep) was not applicable; no `none found` claim is made.
- The frozen C1 `--fetch` counter was not run. This source seat’s research is not evidence of a counter pass, F/K/G totals, or integrated C1 acceptance. No C2 work was done; C2 was withdrawn before data. No counter, verifier, product file, or Git state was changed.
- Only this report was written in the lane. Fetch artifacts are the two Markdown bodies and their `.headers` files in the scratch directory above. No tools were installed or updated.
- Integration remains subject to the frozen C1 rules and the line-budget move: the plan records SKILL.md at 598/600 lines, so perform the required verbatim budget move before adding the new table; do not edit checklist box text. The docs establish what Anthropic documents, not whether a particular installed Claude Code build loads every component as stated.

## Artifact path

`.ufo/waves/round-57/build/SrcClaudeCode.md`
