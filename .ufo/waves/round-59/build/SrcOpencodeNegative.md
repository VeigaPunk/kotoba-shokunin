Result: DONE — opencode stays a negative row: no hook-config file on the pinned docs tree, so the SKILL Hook config cell is plain words (no backtick); S085's page already prints the event names and S102 is not needed.

No tool was installed. Lane files were not edited. Fetches and the sparse checkout live under `/fast/scratch/hyaku/kotoba-r59/SrcOpencodeNegative/`. The counter module was imported read-only from the lane; it was not run against a revision.

# Draft SKILL row

One line. Hook config cell has no backticks (the example sentence, unchanged). Events cell backticks are only the four hook names; line refs are not backticked, because a backticked `index.mdx:1738` matches `EVENT_RE` and is not on the page. Action cell is 12 words.

| opencode | no hook file: hook code is a plugin module, see § Plugin manifests by client (S085, S087) | `http.request` (S085 index.mdx:1478), `http.response` (S085 index.mdx:1483), `execute.before` (S085 index.mdx:1738), `execute.after` (S085 index.mdx:1746) | Read the plugin module; do not look for a hook config file |

Checked against `verifiers/check_hook_files.py` as imported (not a `--rev` run): Hook config backticks `[]`; `event_spans` = `http.request`, `http.response`, `execute.before`, `execute.after`; `events_cell_why` = `[]`; action words = 12. `event_on_page` is true for all four on the S085 bytes and false for all four on the S087 bytes.

Counter consequence, from `judge` (`check_hook_files.py:891-914,926-927`): a Hook config cell with no backtick is `SKILL.md hook config cell holds no backticked token` and `in_k` stays false, so opencode is not in K. A missing knowledge-entry row adds `no entry row names the client` and still does not enter K. Do not add an entry row to silence that: S085 is already a base SOURCES row, and a row cannot be backed without a well-formed token. Do not put `.opencode/plugins/` in backticks; CtlFabEvents already showed that token rejected as not well-formed (`controls/CtlFabEvents.md:39`).

# Do S085 / S087 carry the lines?

S085's URL bytes do. S087's do not. No new row. S102 stays unused.

S085 and the current pin are the same file. `date -u` `Fri 23 Oct 2026 09:35:08 AM UTC`: `gh api repos/anomalyco/opencode/commits/dev` and `repos/sst/opencode/commits/dev` both returned `74f8d4860f49c563909e6b039b0cc8b454ebce72`, committer `2026-10-23T08:30:21Z` (same pin as `w0/Censusopencode.md`). Fetches `Fri 23 Oct 2026 09:35:25 AM UTC` through `Fri 23 Oct 2026 09:35:29 AM UTC`, User-Agent and Accept copied from `check_hook_files.py:316-318`:

| page | status | bytes | sha256 |
|---|---|---|---|
| S085 URL at `bdf757209ff742b8551a4874347edb845241e5bb` (`…/build/plugins/index.mdx`) | 200 | 60780 | `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` |
| same path at `74f8d486…` | 200 | 60780 | same `e505931a…` |
| S087 URL (`…/content/plugins.mdx`) at `bdf7572…` | 200 | 4371 | `39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3` |
| same path at `74f8d486…` | 200 | 4371 | same `39afa299…` |

Those sha256 values are the ones printed in `corpus/SOURCES.md` S085 and S087. S085's anchor cites Hooks at `index.mdx:1335-1418`. That range prints `prompt`, `context`, and `compaction` as `ctx.session.hook` names (`:1357`, `:1408`, `:1415`). It does not include the four names in the draft. The same page does, outside that range, as the string argument of a `.hook(` call and again as an interface key:

- `index.mdx:1478` `await ctx.session.hook("http.request", (event) => {` and `:1581` `"http.request": SessionHttpRequestHook`
- `index.mdx:1483` `await ctx.session.hook("http.response", (event) => {` and `:1582` `"http.response": SessionHttpResponseHook`
- `index.mdx:1738` `await ctx.tool.hook("execute.before", (event) => {` and `:1756` `"execute.before": ToolExecuteBefore`
- `index.mdx:1746` `await ctx.tool.hook("execute.after", (event) => {` and `:1757` `"execute.after": ToolExecuteCompleted | ToolExecuteFailed`

`index.mdx:1491` heads `#### Native WebSocket (experimental)` and `:1536` says `These hooks are experimental and their names or shapes may change.` That sentence covers `experimental.ws.handshake`, `experimental.ws.send`, and `experimental.ws.receive` (`:1503`, `:1522`, `:1531`). Those three are on the page and match `EVENT_RE`; they are not in the draft. `http.request` and `http.response` are under `#### Native HTTP` (`:1468`), before that heading.

`index.mdx:1815` also prints the V1 key `"tool.execute.before"` inside the `server()` example, next to the V2 call `ctx.tool.hook("execute.before"` at `:1808`. The draft uses the V2 name. `tool.execute.before` is on this page once; `tool.execute.after`, `session.created`, and `session.idle` are not (counts 0 on the S085 bytes).

S087 `plugins.mdx` (160 lines) has one `hook` hit, line 142: `Create plugins that add tools, hooks, integrations, commands, agents, and other behavior.` It prints no event identifier from the draft. Its job in the Hook config cell is the discovery fact already mined: `.opencode/plugins/` at `:47` and `~/.config/opencode/plugins/` at `:60`.

A second pinned page, not a SOURCES row, repeats the same V2 names: `services/www/src/docs/content/build/plugins/migrate-v1.mdx` maps V1 `tool.execute.before` to `ctx.tool.hook("execute.before"` (`:159`) and `tool.execute.after` to `execute.after` (`:160`). `effect.mdx` prints the same `.hook(` strings. Neither is needed for the row.

The live V1 page is a different document. `https://opencode.ai/docs/plugins.md` at `Fri 23 Oct 2026 09:35:25 AM UTC`, HTTP 200, 9357 B, sha256 `c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e`, final URL unchanged. It prints `tool.execute.before` at lines 88, 193, and 241, `tool.execute.after` at 192, `session.created` at 177, `session.idle` at 182 and 218, `experimental.session.compacting` at 338, 353, and 362. Those lines are not the S085 or S087 bytes. The English source of that page, `packages/web/src/content/docs/plugins.mdx` at the pin, is HTTP 200, 9473 B, sha256 `4cc0d8db8645a036d1398a9e3be65c386ab75d003a2699c14bc06c267ea1354f`, and lists the same names at `:182-202`. Not a SOURCES row, and not required.

# Q30 sweep (not a silence claim)

The client is not silent and not eligible. All three legs were opened.

1. Changelog and release notes. `CHANGELOG.md` at `74f8d486…`, raw HTTP 200, 50001 B, sha256 `7c4cb74025c345d5a5df08195da5005674478055c6c804f25221f3bb931c519b`. GitHub contents API at `Fri 23 Oct 2026 09:37:44 AM UTC` reports `size: 50001`, so the body is the whole file. Hook lines are API behavior, not a config path: `:143` compaction hook result field, `:184` and `:197` compaction hooks, `:195` request hooks, `:351` permission hooks, `:421` Promise hook. No `hooks.json`, no `.opencode/hooks`. `gh api repos/anomalyco/opencode/releases?per_page=20` at `Fri 23 Oct 2026 09:37:10 AM UTC`, filtered to bodies containing `hook`: empty. Latest release named there is `v1.19.4`, published `2026-10-22T13:03:41Z`.

2. Current docs source tree, pin `74f8d4860f49c563909e6b039b0cc8b454ebce72`. Tree API `Fri 23 Oct 2026 09:37:44 AM UTC`: `truncated: false`, 9534 paths. Zero paths contain `hooks.json` or `hooks.mdx`. No `.opencode/hooks` path; `.opencode/` in that tree holds `agent/`, `command/`, `plugins/`, `skills/`, `themes/`, `tool/`, not a hooks file. Sparse checkout of `services/www/src/docs` and `packages/web/src/content/docs` at that HEAD (`Fri 23 Oct 2026 09:38:11 AM UTC`, 652 files): `grep -RIl -e 'hooks.json' -e '.opencode/hooks'` prints nothing. `https://opencode.ai/docs/hooks.md` HTTP 404, 97 B; `https://opencode.ai/docs/hooks` HTTP 404, 94 B (same fetch window). v2 `config.mdx` (16687 B, sha256 `15e0fc4dc6ff1d5b305b6bebfd34d8a00e175ce60911f80277dea7e50f311d98`) has no line matching `hook`. Live `https://opencode.ai/docs/config.md` HTTP 200, 26060 B, sha256 `fe28a438a1464cb5a43231a7af56f2ed16b019016731052ddfc2ae86fd54cda8`; its only hook line is `:772`, which points at the plugins page (`custom tools, hooks, and integrations`), not a file. GitHub code search at `Fri 23 Oct 2026 09:37:10 AM UTC` returned `total: 0` for `hooks.json`, `.opencode/hooks`, `.opencode/hook`, and `~/.config/opencode/hooks`, while the same API returned `total: 65` for `.opencode/plugins/`, so the index was answering.

3. Corpus. `grep -ril hook /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus` exit 0, eight files: `corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-8.md`, `corpus/lessons/round-57.md`, `corpus/knowledge/instruction-surface-census-round13.md`, `corpus/knowledge/instruction-surface-remeasure-round13.md`, `corpus/knowledge/opencode-extraction-round14.md`, `corpus/knowledge/plugin-manifests-round57.md`. The `hooks.json` hits are other clients (S086 Codex scaffold, S083 Gemini `hooks/hooks.json`, S088 Cursor `hooks/hooks.json`). No corpus file contains `.opencode/hooks` or an opencode `hooks.json`. `plugin-manifests-round57.md` already records opencode hooks as code inside the plugin module (S085, S087), which is the banned `plugins` segment.

# What the integrator should not do

- Do not open S102 for this client.
- Do not backtick a path in the opencode Hook config cell, and do not backtick the line refs in the Events cell.
- Do not cite `experimental.ws.handshake` as one of the two required names without saying the page marks that set experimental (`index.mdx:1536`).
- This row is one line. It does not by itself cross the 600-line SKILL budget.
