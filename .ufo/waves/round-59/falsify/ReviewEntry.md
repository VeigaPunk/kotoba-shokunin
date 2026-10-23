Result: MIXED — every per-client factual claim, the frontmatter, and the Not-held list check out against the cited snapshot lines, but two quote-shaping sentences (S097 and S098) misdescribe the actual bytes and need correction.

Review scope: `corpus/knowledge/hook-files-round59.md` at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` (working tree tip 3f15f84; content read via `git --no-optional-locks show c63ccc68:<path>`, dumped to scratch /fast/scratch/hyaku/kotoba-r59/ReviewEntry/rev/). No lane files modified; no tools installed (none needed).

## Findings (by severity)

### F1 — S098 quote-shaping note misdescribes the bytes (the only material defect)
Entry line 63: "S098: lines 59-60 (a table row and the next heading) folded to single spaces; the three literal `|` bytes are written `&#124;` so the quote stays in one Markdown cell."

(a) "the next heading" is false. S098 has no adjacent heading: the heading list of the snapshot is (line: heading) 4 "# Configure agent hooks... (Preview)", 16 "## Choose the hook implementation", 32 "### Migrate", 38 "## Create and manage hooks", 52 "## Choose a hook source", 73 "## Create your first Copilot hook", 114 "## Configure commands and event data", 122 "### Events and payloads", 141 "### Decisions and failures", 156 "## Agent-scoped hooks", 167 "## Existing Local hooks", 187 "## Troubleshoot hooks", 199 "## Security considerations", 210 "## Related resources". There is no "## Hooks" heading; line 60 is the second row of the Need/Source table.

(b) The cell is NOT a fold of lines 59-60. Raw snapshot lines (byte-exact):
```
S098.page:59 | `| Automation shared with a repository | `.github/hooks/*.json` at the repository root |`
S098.page:60 | `| Hooks alongside other personal or repository settings | An inline `hooks` map in a supported Copilot settings file |`
```
Decoded cell (&#124; → |): `Automation shared with a repository | `.github/hooks/*.json` at the repository root | | Hooks` (3 pipes). Python byte-compare: `cell == l59[2:] + " | Hooks"` is MATCH; `cell == " ".join([l59,l60])` is MISMATCH (full fold would continue "...| Hooks alongside other personal or repository settings | An inline `hooks` map in a supported Copilot settings file |"). So the applied shape = line 59 with its leading `| ` dropped, plus the head of line 60 through its first word "Hooks"; the rest of line 60 is discarded. That truncation is not stated.

Correction for line 63: "S098: line 59 (the table row `Automation shared with a repository …`), its leading `| ` dropped, joined with the head of line 60 (the next table row) through the word `Hooks`; whitespace collapsed to single spaces; the three kept literal `|` bytes are written `&#124;` so the quote stays in one Markdown cell."

### F2 — S097 quote-shaping note omits a front-trim
Entry line 62: "S097: lines 38-44 folded to single spaces; the Markdown link and the list marker `-` are kept as printed."

The cell is `a default `hooks/hooks.json` file. See [Build plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the plugin packaging rules. In practice, the four most useful locations are: - `~/.codex/hooks.json``. Byte-compare against `" ".join(S097.page[38:44])`:
- full fold = `manifest or a default ... file. See [Build plugins](…) for the plugin packaging rules.  In practice, the four most useful locations are:  - `~/.codex/hooks.json`` (starts "manifest or ...", and the blank line 43 yields double spaces).
- The cell instead starts at "a default ..." (the leading "manifest or " of line 38 is cut) and has single spaces ("rules. In practice", "are: -").
So the sentence is accurate about the link and the `-` marker and about whitespace collapsing, but does not state that the head of line 38 ("manifest or ") is trimmed; and the fold of the full lines would contain double spaces from the blank line, so "folded to single spaces" is only true of the collapsed rendering.

Correction for line 62: add the trim: "S097: lines 38-44 folded to single spaces, opening 'manifest or ' trimmed (quote begins at 'a default …'); the Markdown link and the list marker `-` are kept as printed."

## Verified as HOLDS (no correction needed)

1. Claude Code note (lines 32-35) vs S096.page: `~/.claude/settings.json` + `.claude/settings.local.json` rows at :243-245; events SessionStart :33, PreToolUse :37, PostToolUse :40, SessionEnd :65; "Command hooks execute shell commands with your full user permissions ... Review and test all hook commands before adding them" at :4146. Quote cell == S096.page:910 byte-exact (MATCH).
2. Codex note (lines 36-39) vs S097.page: config forms at :32-35 ("Codex discovers hooks next to active config layers ... - `hooks.json`; - inline `[hooks]` tables inside `config.toml`"), four-most-useful locations at :42-47 with `~/.codex/hooks.json` first (:44); events PreToolUse :25, SessionStart :27; "Non-managed hooks must be reviewed and trusted before they run." :19.
3. VS Code note (lines 40-43) vs S098.page: repository-shared `.github/hooks/*.json` :59; personal :58, settings :60, plugin :61, agent-scoped :62; Preview at :4 (title) and :11; events sessionStart :128, preToolUse :130; "Hook configuration and scripts are executable code. Review them before use ..." :202.
4. Copilot CLI note (lines 44-46) vs S099.page: repository `.github/hooks/*.json` + personal `~/.copilot/hooks/*.json` :28 (sentence bytes present, MATCH); events sessionStart :34, preToolUse :37; "Do not assume that the same events, input, or output work unchanged across surfaces." :26 (also the SKILL row's E5 rationale is internal editorial, not a page claim).
5. Gemini CLI note (lines 47-49) vs S100.page: project `.gemini/settings.json` at "When you open a project with hooks defined in `.gemini/settings.json`:" :413 (full-line MATCH); `BeforeTool`/`AfterModel` :31; "Verify the source of any project hooks or extensions before enabling them." :442. "Session events are on the separate hooks page, which is not a row": live probe `https://geminicli.com/docs/hooks.md` returns 200, 8341 B, sha a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9, containing `SessionStart`/`SessionEnd` (lines 40-41); no SOURCES row at this rev cites that URL (grep of `corpus/SOURCES.md` at c63ccc68 shows only S100 best-practices). HOLDS.
6. Cursor note (lines 50-53) vs S101.page: project `.cursor/hooks.json` runs for cloud agents :50; user `~/.cursor/hooks.json` unavailable to cloud agents :102; events preToolUse :27 and :67, postToolUse :67; sessionStart definition :1340; cloud-agent "not run"/deferred row :88; trusted-workspace statements :649/:781. The hooks.md 404 / same-bytes claim reproduced exactly with the counter's header set (`curl -sSL --max-time 30 -A <browser UA> -H "Accept: text/markdown, text/plain;q=0.9, */*;q=0.8"`):
   - `https://cursor.com/docs/hooks.md` → HTTP 404, effective URL https://cursor.com/docs/hooks.md, body 389 B ("# Page not found\nThis page doesn't exist. ...");
   - `https://cursor.com/docs/hooks` → HTTP 200, 69,145 B, sha256 8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d — byte-identical to the committed S101.page.
   (Note: without the `Accept: text/markdown` header the site content-negotiates to a 1.3 MB HTML page; the counter's fixed header set is what the note describes, and it reproduces exactly.)
7. opencode note (lines 54-57): live probe `https://opencode.ai/docs/hooks.md` → HTTP 404 (94 B JSON `{"status":404,"message":"Cannot find any route matching [GET] https://opencode.ai/docs/hooks.md"}`); `https://opencode.ai/docs/hooks` also 404. Consistent with the cited w0/Censusopencode.md and build/SrcOpencodeNegative.md.
8. Frontmatter: URLs on line 2 equal the SOURCES rows' URLs (S096 code.claude.com/docs/en/hooks.md; S097 learn.chatgpt.com/docs/hooks.md; S098 code.visualstudio.com/docs/agent-customization/hooks.md; S099 docs.github.com/en/copilot/concepts/customizations/hooks.md; S100 geminicli.com/docs/hooks/best-practices.md; S101 cursor.com/docs/hooks). `verified-at: 2026-10-23` matches every row's opened date. "each sha256 equals its SOURCES row" verified for all six snapshots: `sha256sum` output equals the row shas exactly (S096 c6ef9d21…; S097 57166ef0…; S098 98c5be6b…; S099 23370e09…; S100 fb44fbcf…; S101 8436af76…) and byte counts equal the rows' counts (274,129 / 47,133 / 15,152 / 8,428 / 17,650 / 69,145). The recheck command names the actual verifier.
9. Scope boundary (lines 16-19): round-13 census quote "executable surfaces, out of prompt-craft province" found verbatim at `corpus/knowledge/instruction-surface-census-round13.md:265` at this rev; `.ufo/waves/round-59/w0/ConnSiblingHooks.md` exists in the wave tree.
10. Not-held list (lines 66-71): all three bullets are hedged accurately; the cross-surface warning cites S099:26 which is verified.

## Commands and evidence
- `git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:corpus/knowledge/hook-files-round59.md` etc. (exit 0) — source of all quoted entry lines.
- `sha256sum .ufo_waves_round-59_snapshots_S{096..101}.page` (exit 0) — shas above; all six equal the SOURCES rows.
- Python byte-compare (exit 0): S096 MATCH; S097 cell vs full fold MISMATCH (prefix "manifest or " trimmed, blank-line double spaces collapsed); S098 cell == l59[2:]+" | Hooks" MATCH, full fold MISMATCH; S099/S100/S101 MATCH.
- `curl -sSL --max-time 30 -A "$UA" -H "Accept: $ACC" -w '\n%{http_code} %{url_effective}\n'` (exit 0) for cursor hooks.md (404), cursor /docs/hooks (200, sha matches), opencode hooks.md (404), gemini hooks.md (200). Capture time 2026-10-23 09:53 UTC; all probes above recorded with status, byte count and sha256.

## Residual risk / verification gaps
- The note-level 404/same-bytes claim is tied to the counter's fixed curl header set; the site serves different bytes to other Accept values (observed 1.3 MB HTML for default Accept). The counter's run is the canonical measure, and its header set reproduces the claim exactly; no residual risk for the note text.
- I did not re-run the full verifier (`--fetch`) in a sandbox; live fetch probes were limited to the URLs the notes assert about (cursor hooks.md, cursor /docs/hooks, opencode hooks.md, gemini hooks.md). The per-client content claims are verified against the committed snapshots, which is what the assignment asked.
- No tools installed; no lane state mutated; only this report written at .ufo/waves/round-59/falsify/ReviewEntry.md.
