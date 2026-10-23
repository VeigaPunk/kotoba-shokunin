Result: MIXED — Both identifiers are genuine S085 V2 tool hooks and the bounded Q30 sweep finds no separate hook-config file, but the reusable SKILL row omits the V2 scope despite materially different V1 hook keys.

## Scope and authority

Attacked revision: `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`; specifically `SKILL.md:133` and `corpus/knowledge/hook-files-round59.md:54-57`. Primary axis: depth. Secondary risk: calibration/operability from applying a version-specific identifier to the wrong API. This is source review, not runtime verification or claim admission.

All investigation writes and source extraction were confined to `/fast/scratch/hyaku/kotoba-r59/CriticOpencodeRow/`. The only lane write is this report. No tools were installed, no subagents were dispatched, no client/model CLI or other judgment runtime was invoked, and no hook implementation was run. The frozen counter, rule, population and targets were not changed. This seat did not run or mutate C1; it makes no independent claim about the six counted rows or their receipt.

Sandbox creation, exit 0:

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/CriticOpencodeRow && timeout 30 git -C /fast/scratch/hyaku/kotoba-r59/CriticOpencodeRow checkout -q c63ccc6823e1f6a8577acbb43d19551eadbbee9a && timeout 10 git -C /fast/scratch/hyaku/kotoba-r59/CriticOpencodeRow rev-parse HEAD
```

Observed output: `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`.

## 1. HOLDS — S085 prints both names at the exact cited lines, as hook events

Reopened the full raw URL registered in `corpus/SOURCES.md:98`, not an inferred relative page and not the different currently served V1 plugin page. Saved bytes: `r59-S085.page`, HTTP 200, 60,780 bytes, SHA256 `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5`, equal to S085's registry fingerprint.

Byte-exact quotes, no Markdown bytes stripped, each below 25 words:

| Fetched location | Quote | Reading |
|---|---|---|
| `r59-S085.page:1735` | `Inspect or replace tool input before execution.` | Documents the before operation. |
| `r59-S085.page:1738` | `await ctx.tool.hook("execute.before", (event) => {` | Actual tool-domain hook registration, not an incidental identifier. |
| `r59-S085.page:1743` | `Inspect successful results or failures after execution.` | Documents the after operation. |
| `r59-S085.page:1746` | `await ctx.tool.hook("execute.after", (event) => {` | Actual tool-domain hook registration. |

The enclosing section is `## Hooks` at line 1335, and `### Tools` at line 1733. `ToolHooks` at lines 1754-1758 maps the two names to `ToolExecuteBefore` and `ToolExecuteCompleted | ToolExecuteFailed`. The registration signature at lines 1760-1764 gives its callback an event of that indexed type. Both spans therefore rule **event**, independently of the frozen counter's string-presence test. Neither is covered by the separate experimental WebSocket warning at line 1536.

Current default-branch source was independently pinned via GitHub's commits API to `74f8d4860f49c563909e6b039b0cc8b454ebce72` (committer timestamp `2026-10-23T08:30:21Z`). The same file extracted from that current revision has the identical SHA256. This is not stale line-number evidence.

## 2. BREAKS — the row's unstated cross-version applicability

Concrete counterexample: a reader auditing an OpenCode V1 plugin through the current served `https://opencode.ai/docs/plugins.md` receives `tool.execute.before` and `tool.execute.after`, not the bare V2 tool-domain names. This is not evidence that the S085 names are fabricated; it is evidence that their API scope matters.

Evidence:

- `SKILL.md:133` labels its client only `opencode` and prints the two bare names without saying V2. Neither the Hook section introduction at line 123 nor the entry's opencode note at lines 54-57 supplies a version boundary.
- `r59-live-plugins.md:190-193` explicitly lists the two **Tool Events** as `tool.execute.after` and `tool.execute.before`; the example at line 241 uses the before key in a returned hooks object.
- The current V1 docs source at `packages/web/src/content/docs/plugins.mdx:201-202` lists the same prefixed keys. The served page and source have different fingerprints, so I did not treat one as the other's exact-byte snapshot.
- Most decisively, **S085 itself** distinguishes the APIs: `r59-S085.page:1808` uses the V2 registration, while line 1815 uses the V1 returned-object key. Its line 1825 says, byte-exact: `- Keep each implementation on its own API; sharing an export does not translate V1 hooks into V2 hooks.`
- Current `services/www/src/docs/content/build/plugins/migrate-v1.mdx:159-160` explicitly maps the prefixed V1 keys to the V2 `ctx.tool.hook` calls. At lines 334-335 it says the APIs remain separate and are not automatically translated.
- This is relevant to the lane's own audience, not a hypothetical ancient release: `SKILL.md:531-534` identifies its measured local opencode substrate as npm `opencode-ai` 1.19.3, and the neighboring agent-definition row at line 91 already distinguishes V1 from V2.

[INFERENCE] Treating the row's bare identifiers as V1 return-object keys would not name the documented V1 extension points. No V1/V2 runtime failure was executed here.

Impacted axes: **depth**, because the table is not self-contained about which API its names describe; **calibration**, because S085's V2-specific authority is silently broadened; potentially **operability** if a downstream hook author copies the names across APIs. This is a fixable scoping defect, not a fabricated-event counterexample, not discovery of a seventh hook-config client, and not a tradeoff requiring a target change.

Smallest safe correction: label the existing Events cell `V2 tool hooks: ...` while retaining both identifiers and the S085 line citations. In the entry note, add the same V2 scope if it discusses those names; do not imply they are V1 returned-object keys. Existing S085 already contains the version distinction, so this correction does not require inventing a new source or altering a frozen rule.

## 3. HOLDS — no separate declarative hook-config file is documented in the checked current surfaces

The intended Hook config distinction survives: hooks are plugin-module code, not a separate settings-like hook-definition file. It would be overbroad to mean “no file ever contains hook code”: the docs plainly show JavaScript/TypeScript plugin files. The row's explanatory clause supplies that distinction; the safest wording is **“no separate hook-config file documented: hook code is a plugin module.”**

Positive evidence, rather than only a guessed URL's 404:

- Served V1 page `r59-live-plugins.md:64-65` calls a plugin a JavaScript/TypeScript module returning a hooks object. Its line 65, byte-exact: `functions. Each function receives a context object and returns a hooks object.`
- V1 default discovery roots are at lines 17-20. Npm loading is at lines 24-45; the general `opencode.json` file's `plugin` list selects modules/packages at lines 28-32. It does not define event handlers there.
- S085 `r59-S085.page:10-22` shows a plugin code module and automatic `.opencode/plugins/` discovery; lines 1335 onward document hook registration in that module.
- S087 `r59-S087.page:5-34` allows configured plugin directories; lines 46-60 document project and global automatic discovery. Its line 31, byte-exact: `Relative paths resolve from the config file containing the entry.` The entry note correctly says **by default** and explicitly includes configured paths/npm packages. I did not revive the already-attacked “only these two directories” rationale.
- A genuine general config path in a plugin load-order list is not a counterexample: V1 `r59-live-plugins.md:51-56` lists `~/.config/opencode/opencode.json`, but lines 26-32 establish its role as package selection, not hook-definition configuration.

### Q30: all three sweep legs opened

Let `ROOT=/fast/scratch/hyaku/kotoba-r59/CriticOpencodeRow` and `UP=$ROOT/opencode-74f8d4860f49c563909e6b039b0cc8b454ebce72` below. Searches used `functions.grep`, case-insensitive, `gitignore=false`; these tools do not expose a shell exit code, so none is invented.

1. **Changelog:** opened the full current `CHANGELOG.md`, `r59-current-CHANGELOG.md` (HTTP 200, 50,001 bytes). Tree API independently records its blob size as 50,001. It identifies itself as V2 release notes at lines 3-5, latest heading `v2.1.3 — 2026-10-22`. Search `hooks?|plugin|\.opencode/` finds actual API hook changes, including lines 143, 184, 195, 197, 351 and 421. Search `hooks\.(json|jsonc|ya?ml|toml)|\.opencode/hooks` finds no hook-config path in the changelog.
2. **Current docs source tree:** opened the recursive tree API at the independently resolved current SHA: `truncated=false`, 9,534 tree entries, 652 blobs under `services/www/src/docs/` plus `packages/web/src/content/docs/`. The JSON count query was `[.tree[]|select(.type=="blob")|select(.path|startswith("services/www/src/docs/") or startswith("packages/web/src/content/docs/"))]|length`, result `652`. The docs-path query for case-insensitive `hook` returns `[]`. Downloaded the current official source archive and extracted **both complete docs trees**, not only the plugin page. Search `hooks\.(json|jsonc|ya?ml|toml)|\.opencode/hooks` over both trees returns **`No matches found`**. A broader search `hook.{0,80}(config|\.json|\.ya?ml|\.toml)|(?:config|\.json|\.ya?ml|\.toml).{0,80}hook|"hooks"|hook configuration|hook config|hook file` finds only V2 API context at `build/plugins/index.mdx:1420,1687` and `build/plugins/migrate-v1.mdx:274`, not declarative hook-file configuration. The V2 `config.mdx` itself returns **`No matches found`** for `hook`; its plugin section at lines 511-530 configures package/directory loading.
3. **Lane corpus:** searched the entire committed sandbox `corpus/` with `hook`, then `\.opencode/hooks|hooks\.(json|jsonc|ya?ml|toml)|hook[- ]?(config|file)|^.*opencode.*hook`. Reopened the relevant hits: `corpus/knowledge/plugin-manifests-round57.md:14-22,38,60,95-97` already describes plugin modules, and `instruction-surface-census-round13.md:265-266,283` distinguishes executable plugin roots and non-file hook APIs. Other `hooks.json` hits concern Codex/Gemini/Cursor, not an opencode hook-config file. Historical internal read-hook references are not a standalone user hook configuration mechanism. The new entry at lines 54-57 agrees with this evidence.

This is a bounded negative about dedicated declarative hook configuration, **not** a claim that opencode is silent about hooks or that its runtime can never load another file. The reported hooks URL 404 was not re-run merely to reconfirm it, and a 404 was not treated as the sweep.

## 4. Field ruling and counter boundary

| Attacked field | Ruling | Reason |
|---|---|---|
| Client | HOLDS | Identifies the product; add API scope in the Events field. |
| Hook config | HOLDS in its dedicated-config meaning | Both current docs generations implement hooks in plugin modules; no separate hook-config file found in the Q30 sweep. Tighten “no hook file” to avoid implying no code files. |
| Events | HOLDS as S085 V2 hook events; BREAKS if left version-unqualified for both supported APIs | Exact lines and hook types verify; the same source distinguishes incompatible V1 keys. |
| Action | HOLDS | Reading the plugin module is the correct route, rather than hunting for a separate declarative hook file. Check its V1/V2 API before interpreting its event names. |
| Entry note | HOLDS | Defaults, configured paths and npm alternatives are correctly distinguished; Q30 evidence is reproducible and not 404-only. |

Static counter reading, not an executed result: `verifiers/check_hook_files.py:891-900` only sets `in_k=True` for a well-formed backticked Hook config token. This row has none. Lines 926-927 also record the absent entry-table row. The two real Events spans therefore do not make opencode counted/backed. The frozen plan's addendum at `plans/round-59.md:93-98` correctly leaves event semantics to source review. Keep opencode's exclusion and all frozen counter/target bytes unchanged.

## Fetch receipts and commands

All bodies are under `ROOT`. Each shell sequence printed `timeout 10 date -u`, performed the listed bounded curl, then ran `wc -c` and `sha256sum` on the saved body. Every listed sequence exited 0, with HTTP status 200. No challenge, browser or access-control bypass was used.

First batch's exact UTC line: `Fri 23 Oct 2026 09:53:16 AM UTC`.
Second batch's exact UTC line: `Fri 23 Oct 2026 09:53:51 AM UTC`.

| Batch | Body | URL | HTTP | Bytes | SHA256 |
|---|---|---|---|---|---|
| 1 | `r59-S085.page` | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx | 200 | 60780 | `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` |
| 1 | `r59-S087.page` | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx | 200 | 4371 | `39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3` |
| 1 | `r59-live-plugins.md` | https://opencode.ai/docs/plugins.md | 200 | 9357 | `c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e` |
| 1 | `r59-live-config.md` | https://opencode.ai/docs/config.md | 200 | 26060 | `fe28a438a1464cb5a43231a7af56f2ed16b019016731052ddfc2ae86fd54cda8` |
| 1 | `r59-dev-commit.json` | https://api.github.com/repos/anomalyco/opencode/commits/dev | 200 | 6439 | `e17bd596d83bf1403d8e6c173c4bfc616a5c7b7ca64f15c0bd30f7666b8de991` |
| 2 | `r59-current-tree.json` | https://api.github.com/repos/anomalyco/opencode/git/trees/74f8d4860f49c563909e6b039b0cc8b454ebce72?recursive=1 | 200 | 2971864 | `b4ba920f70b9ceb37780e8b799e423a71460a43d94d55059dc47f338ac71e87d` |
| 2 | `r59-current-CHANGELOG.md` | https://raw.githubusercontent.com/anomalyco/opencode/74f8d4860f49c563909e6b039b0cc8b454ebce72/CHANGELOG.md | 200 | 50001 | `7c4cb74025c345d5a5df08195da5005674478055c6c804f25221f3bb931c519b` |
| 2 | `r59-current-source.tar.gz` | https://codeload.github.com/anomalyco/opencode/tar.gz/74f8d4860f49c563909e6b039b0cc8b454ebce72 | 200 | 79828134 | `154e3e9bd1b2a99da011efd758adbb6ae62aa5e7597492e035aeb9441fa358b2` |

Concrete fetch subcommands executed, all exit 0 (the `-w` format was `HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n`):

```sh
timeout 90 curl -sSL --max-time 60 -H 'Accept: text/plain' -o r59-S085.page -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx
timeout 90 curl -sSL --max-time 60 -H 'Accept: text/plain' -o r59-S087.page -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx
timeout 90 curl -sSL --max-time 60 -H 'Accept: text/markdown' -o r59-live-plugins.md -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' https://opencode.ai/docs/plugins.md
timeout 90 curl -sSL --max-time 60 -H 'Accept: text/markdown' -o r59-live-config.md -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' https://opencode.ai/docs/config.md
timeout 90 curl -sSL --max-time 60 -H 'Accept: application/vnd.github+json' -o r59-dev-commit.json -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' https://api.github.com/repos/anomalyco/opencode/commits/dev
timeout 120 curl -sSL --max-time 100 -H 'Accept: application/vnd.github+json' -o r59-current-tree.json -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' 'https://api.github.com/repos/anomalyco/opencode/git/trees/74f8d4860f49c563909e6b039b0cc8b454ebce72?recursive=1'
timeout 90 curl -sSL --max-time 60 -H 'Accept: text/plain' -o r59-current-CHANGELOG.md -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' https://raw.githubusercontent.com/anomalyco/opencode/74f8d4860f49c563909e6b039b0cc8b454ebce72/CHANGELOG.md
timeout 180 curl -sSL --max-time 160 -H 'Accept: application/gzip' -o r59-current-source.tar.gz -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' https://codeload.github.com/anomalyco/opencode/tar.gz/74f8d4860f49c563909e6b039b0cc8b454ebce72
```

Archive extraction, exit 0:

```sh
timeout 120 tar -xzf r59-current-source.tar.gz -- opencode-74f8d4860f49c563909e6b039b0cc8b454ebce72/services/www/src/docs opencode-74f8d4860f49c563909e6b039b0cc8b454ebce72/packages/web/src/content/docs
```

`timeout 10 sha256sum` on current extracted `build/plugins/index.mdx` and `plugins.mdx` exited 0 and reproduced the S085/S087 hashes above. Extracted migration/source fingerprints (from `timeout 10 wc -c ... && timeout 10 sha256sum ...`, exit 0):

| Relative to the current archive root | Bytes | SHA256 |
|---|---|---|
| `services/www/src/docs/content/build/plugins/migrate-v1.mdx` | 15100 | `9ac058db236908db691e9b5337d27b3178c5b44eca478ab84c59c8cafc65d510` |
| `services/www/src/docs/content/config.mdx` | 16687 | `15e0fc4dc6ff1d5b305b6bebfd34d8a00e175ce60911f80277dea7e50f311d98` |
| `packages/web/src/content/docs/plugins.mdx` | 9473 | `4cc0d8db8645a036d1398a9e3be65c386ab75d003a2699c14bc06c267ea1354f` |

## Smallest safe correction, consolidated

Keep both genuine names, the plugin-module route and opencode's uncounted status. Add **V2** to the Events cell and use **no separate hook-config file documented** in the Hook config cell/entry note. Do not substitute V1 keys into a V2 citation, add a fake declarative hook file, or change the counter/rule/targets. The canonical judge retains the admission decision.
