Result: DONE — opencode: NOT ELIGIBLE (hook code is documented only in `.opencode/plugins/` and `~/.config/opencode/plugins/`, both banned by the segment `plugins`; v2 also names `.opencode/plugin/`, banned by `plugin`)

No tool was installed.

## What the client's pages name

opencode does not publish a hooks file (no `hooks.json`, no `.opencode/hooks`). `https://opencode.ai/docs/hooks.md` and `https://opencode.ai/docs/hooks` are HTTP 404. The published mechanism is plugins: JavaScript/TypeScript modules loaded from a plugins directory return or register hooks that run on lifecycle events. Both the still-served v1 pages and the v2 docs source name that directory. They do not name any other file as the place hook commands or hook code live.

Pinned docs commit for raw sources: `74f8d4860f49c563909e6b039b0cc8b454ebce72` on `anomalyco/opencode` (default branch `dev`, committer `2026-10-23T08:30:21Z`, `gh api` at `Fri 23 Oct 2026 09:03:44 AM UTC`). `sst/opencode` raw of the same path and SHA returned HTTP 200 and the same 4,371 bytes.

## Fetches

`Fri 23 Oct 2026 09:02:52 AM UTC` through `Fri 23 Oct 2026 09:02:56 AM UTC`. User-Agent `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`. Bytes under `/fast/scratch/hyaku/kotoba-r59/Censusopencode/`.

| URL | status | bytes | sha256 | saved as |
|---|---|---|---|---|
| https://opencode.ai/docs/plugins.md | 200 | 9357 | `c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e` | `opencode.ai_docs_plugins.md` |
| https://opencode.ai/docs/config.md | 200 | 26060 | `fe28a438a1464cb5a43231a7af56f2ed16b019016731052ddfc2ae86fd54cda8` | `opencode.ai_docs_config.md` |
| https://opencode.ai/docs/hooks.md | 404 | 97 | (body is a JSON 404) | `opencode.ai_docs_hooks.md` |
| https://opencode.ai/config.json | 200 | 65410 | `a582efab285edebb320d2fa6d2e4750ec4fe0e588e8af0e413d630e5bce1c5b9` | `more_opencode.ai_config.json` |
| https://opencode.ai/llms.txt | 200, final URL `https://opencode.ai/v2/llms.txt` | 4061 | (index only) | `opencode.ai_llms.txt` |
| https://opencode.ai/v2/docs/plugins.md | 404 | 9 | | `opencode.ai_v2_docs_plugins.md.body` |
| https://opencode.ai/v2/docs/config.md | 404 | 9 | | `opencode.ai_v2_docs_config.md.body` |

`Fri 23 Oct 2026 09:04:23 AM UTC` through `Fri 23 Oct 2026 09:04:25 AM UTC`, raw sources at the pin above:

| path | status | bytes | sha256 |
|---|---|---|---|
| `services/www/src/docs/content/plugins.mdx` | 200 | 4371 | `39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3` |
| `services/www/src/docs/content/build/plugins/index.mdx` | 200 | 60780 | `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` |
| `services/www/src/docs/content/config.mdx` | 200 | 16687 | `15e0fc4dc6ff1d5b305b6bebfd34d8a00e175ce60911f80277dea7e50f311d98` |
| `services/www/src/docs/content/migrate-v1.mdx` | 200 | 20805 | `f3d42b36cec1b498d19543b32e72a069e006ee2a4a6884e548ce3a9408fd78a0` |
| `packages/web/src/content/docs/plugins.mdx` | 200 | 9473 | `4cc0d8db8645a036d1398a9e3be65c386ab75d003a2699c14bc06c267ea1354f` |
| `CHANGELOG.md` | 200 | 50001 | `7c4cb74025c345d5a5df08195da5005674478055c6c804f25221f3bb931c519b` |

GitHub blob size of `CHANGELOG.md` at that pin is 50001 (`gh api` `Fri 23 Oct 2026 09:08:23 AM UTC`), so the raw body is the whole file. `config.mdx` (v2) and `https://opencode.ai/config.json` contain no case-insensitive `hook`. v2 HTML for `/v2/docs/config/`, `/v2/docs/permissions/`, and `/v2/docs/tools/` likewise has no `hook`.

## Candidates

### 1. `.opencode/plugins/` — the project folder the docs name for hook code

Printed at `opencode.ai_docs_config.md:774` and `opencode.ai_docs_plugins.md:17`, `:56`. v2 source `raw_services_www_src_docs_content_plugins.mdx:47` and build index `:21`.

Quote (v1 config page, contiguous, backticks kept as printed; word count 8 after stripping backticks, the counter's count). Lines 772–774:

> hooks, and integrations.
>
> Place plugin files in `.opencode/plugins/`

`hooks` is outside the token. A same-page window also exists on `opencode.ai_docs_plugins.md:329-333` (12 words; the normalised form `.opencode/plugins` sits inside the fence title `.opencode/plugins/compaction.ts`, right boundary `/`):

> hooks
>
> Customize the context included when a session is compacted:
>
> ```ts title=".opencode/plugins/compaction.ts"

v2 mdx pages name the folder but no 6–25-word window on those files joins it to `hook`/`hooks`.

Events, byte-exact, on `opencode.ai_docs_plugins.md` (the hooks page; `/docs/hooks` is 404). Each matches `^[A-Za-z][A-Za-z0-9_.:-]*$`:

- `tool.execute.before` line 193
- `tool.execute.after` line 192
- `session.created` line 177
- `session.idle` line 182
- `experimental.session.compacting` line 338 (code) and line 353 (prose)

Not a changelog URL. The folder itself is not marked experimental, preview, or deprecated. The compaction key is named `experimental.session.compacting`. v2 `build/plugins/index.mdx:1536` says "These hooks are experimental" about the websocket hooks only (`experimental.ws.handshake`, `experimental.ws.send`, `experimental.ws.receive`).

### 2. `~/.config/opencode/plugins/` — global folder, same role

Printed at `opencode.ai_docs_plugins.md:18` and `:55`, and `opencode.ai_docs_config.md:774`. v2 `plugins.mdx:60`.

Same-page quote on `opencode.ai_docs_plugins.md:51-55` (21 words after backtick strip):

> hooks run in sequence. The load order is:
>
> 1. Global config (`~/.config/opencode/opencode.json`)
> 2. Project config (`opencode.json`)
> 3. Global plugin directory (`~/.config/opencode/plugins/`)

Events are the same list on that page. Not experimental as a folder.

### 3. `.opencode/plugin/` — v2 migration only

`raw2_services_www_src_docs_content_migrate-v1.mdx:591` and `raw_services_www_src_docs_content_build_plugins_migrate-v1.mdx:38`: "V2 discovers local plugins from both `.opencode/plugin/` and `.opencode/plugins/`; use `.opencode/plugins/` for V2 files." No 6–25-word window on those files joins this token to `hook`/`hooks`. Migration guide, not a changelog path (`migrate` is not a change-note word).

### Not a hook-config file: `~/.config/opencode/opencode.json`

Grammar would pass (segments `.config`, `opencode`, `opencode.json`; no banned word; E7 holds; own marker only). `opencode.ai_docs_plugins.md:51-53` has a 12-word quote ("hooks run in sequence. The load order is: 1. Global config (`~/.config/opencode/opencode.json`)"). The page does not call that file hook configuration. It is global config; the `plugin` array names npm packages (`opencode.ai_docs_plugins.md:28-32`). The hook code is in the plugin modules. `./.opencode/opencode.jsonc` (`plugins.mdx:41`) is the same kind of config path. `./opencode.jsonc` is one segment after stripping `./` and does not start with `.`.

## Conjunct table

| conjunct | `.opencode/plugins/` | `~/.config/opencode/plugins/` | `.opencode/plugin/` |
|---|---|---|---|
| own pinned-host docs name it as the hook-code folder | yes | yes | yes (v2 migrate only) |
| TOKEN_RE | yes | yes | yes |
| after one `~/` or `./`, at least 2 segments | yes | yes | yes |
| first segment starts with `.` | yes | yes | yes |
| no banned segment word (skill/skills/agent/agents/command/commands/prompt/prompts/rule/rules/plugin/plugins/extension/extensions) | **no** (`plugins`) | **no** (`plugins`) | **no** (`plugin`) |
| E7: no dot inside a non-final segment except as its first character | yes | yes | yes |
| no other client's marker (claude, codex, vscode, copilot, gemini, cursor) | yes (`opencode` is this client) | yes | yes |
| E5: not the token another client's row would lead with | not found on the other six hosts (below) | same | same |
| 6-25-word quote, token at a segment boundary, hook/hooks outside the token | yes on v1 config.md (8) and v1 plugins.md (12); no on v2 mdx | yes on v1 plugins.md (21) and v1 config.md (10); no on v2 mdx | no |
| at least 2 event identifiers on that page or the hooks page | yes (`opencode.ai_docs_plugins.md`) | yes, same page as the 21-word quote | events exist on the plugin pages; quote already fails |
| page is not changelog/release/news/blog/issue | yes | yes | yes |
| marked experimental/preview/deprecated | folder: no | folder: no | no |

E5 search, `Fri 23 Oct 2026 09:07:12 AM UTC`: `gh search code` for `.opencode/plugins/` returned third-party repos only (opencode primers and adapters), not `anthropics/claude-code`, `openai/codex`, `microsoft/vscode`, `microsoft/vscode-docs`, `github/copilot-cli`, or `google-gemini/gemini-cli`. A web search restricted to the other six pinned hosts returned no matches (the engine then dropped the site filter and returned only opencode.ai). [INFERENCE] no other client row would lead with these tokens.

## New-ground pre-count (base `a975cbbf00534443c49bf02e29c813a3db0bf0f8`)

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.opencode/plugins' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo' | wc -l
```

exit 0, output `8`.

```
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.config/opencode/plugins' a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo' | wc -l
```

exit 0, output `5`.

Neither token is new ground. `git grep -ilF '.opencode/plugin'` is also 8 because `-F` matches the plural `.opencode/plugins` as a prefix; that count is not a separate hit. `.config/opencode/opencode.json` is 1 file (`SKILL.md`). `.opencode/opencode.jsonc` is 0.

## Q30 legs (not a silence claim)

The client is not silent. Changelog `CHANGELOG.md` at the pin mentions compaction hooks, permission hooks, and request hooks as API behavior, not a hook-config path. Docs tree search (`gh` code search plus the mdx files above) found no `hooks.json`, no `experimental.hook`, and no `.opencode/hooks`. `git grep -il hook <base> -- corpus | wc -l` is 8. Corpus already records `.opencode/plugins/` as plugin discovery (S085/S087), which is the same banned token.
