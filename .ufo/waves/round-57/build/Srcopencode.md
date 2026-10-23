Result: DONE — OpenCode's V2 docs label `package.json` a package-plugin manifest, but no plugin-specific JSON token satisfies frozen counter v2, so S085 cannot count toward C1.

## Findings

- **Exact documented manifest label:** `package.json` (`plugins-build-index.mdx:1770-1785`), in the “A package plugin … A minimal manifest is” section. The sample is a generic npm package manifest with `name`, `version`, `type`, `exports`, and `dependencies`; the page does not give it a plugin-specific filename. Do not turn this into `plugin.json`, `.opencode/plugin.json`, or `opencode-plugin.json`.
- **Documented local plugin location:** `.opencode/plugins/` (`plugins-build-index.mdx:10-22`). The sibling discovery page gives the global location `~/.config/opencode/plugins/` (`plugins.mdx:46-61`). These are directories, not JSON manifest files.
- **C1 v2 consequence:** `package.json` fails the frozen token rule because its final segment has no `plugin`/`extension` word and it does not contain the opencode marker; `.opencode/plugins/` and `~/.config/opencode/plugins/` are directories and cannot qualify. This is a static reading of the frozen rule (`verifiers/check_plugin_manifests.py:15-17, 76-80, 535-558`), not a counter run. No eligible opencode manifest token was found; no token was invented.
- **What plugins can ship/register, as documented in the V2 build guide:** skills (including `path` and `content`, and add/update/remove: `plugins-build-index.mdx:865-892`); agents (inspect/update/remove/select default: `:214-235`); commands (`:414-445`); MCP server configuration (`:610-627`); tools (`:961-985`); runtime hooks (`:1335-1350`) that can modify model instructions/messages/tools/options (`:1396-1418`). The main plugin page additionally says plugins add tools, hooks, integrations, commands, agents, and other behavior (`plugins.mdx:141-142`). These are documented plugin API capabilities, not evidence that those components are packaged as separate files. No claim is made here for rule files or LSP definitions.

### Exact quote

Fetched bytes: `plugins-build-index.mdx:1770-1773`. 18 whitespace-delimited words; no bytes removed; the line breaks and blank line below are part of the quote. It contains `package.json` and `plugin` outside that token, but the token is not C1-v2-valid.

````text
A package plugin uses the same default export as a local plugin. A minimal
manifest is:

```json title="package.json"
````

### Draft SOURCES row (documentation evidence; not a C1-eligible client row)

Columns match `corpus/SOURCES.md:12-13`. Both URLs are pinned to the same upstream commit; the first contains the quote and V2 API details, the second supplies the global discovery path.

```text
| S085 | anomalyco/opencode — V2 plugin documentation, pinned at `bdf757209ff742b8551a4874347edb845241e5bb` — https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx; https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx | docs | A | OpenCode V2 package-plugin manifest label, plugin discovery locations, and programmatically registerable plugin surfaces | Local plugin (`index.mdx:10-22`); Agent (`:214-235`); Commands (`:414-445`); MCP (`:610-627`); Skills (`:865-892`); Tools (`:961-985`); Hooks (`:1335-1418`); Publish (`:1768-1786`); sibling discovery page `plugins.mdx:46-61,141-142`; fetched 2026-10-23T04:51:25Z (HTTP 200, 60,780 B, sha256 `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5`); sibling page fetched 2026-10-23T04:47:59Z (HTTP 200, 4,371 B, sha256 `39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3`) | OpenCode calls `package.json` the minimal manifest for a package plugin and loads local plugin modules from `.opencode/plugins/`; global discovery uses `~/.config/opencode/plugins/`. The build guide documents plugin APIs for skills, agents, commands, MCP configuration, tools, and runtime hooks, but no plugin-specific JSON filename meeting the frozen token grammar. | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |
```

### Draft SKILL.md row (evidence-only; do not present as a C1-valid row)

```text
| opencode | `package.json` (project plugin directory: `.opencode/plugins/`; global: `~/.config/opencode/plugins/`) | Plugin modules can register/transform skills, agents, commands, tools, and MCP server configuration; runtime hooks can modify prompt/model context. | Treat package.json as package metadata; do not infer a plugin-specific manifest filename. |
```

### Draft entry row (evidence-only; the frozen counter rejects its manifest token)

The exact quote above is multiline. For this one-line row rendering, `\n` stands for the original LF bytes; it is not a different quote.

```text
| opencode | `package.json` | S085 | "A package plugin uses the same default export as a local plugin. A minimal\nmanifest is:\n\n```json title=\"package.json\"" |
```

## Gates and source checks

- Read binding `.ufo/waves/round-57/bounds.md`, `plans/round-57.md`, the `SOURCES.md` header and S072–S078, and the frozen counter v2 rules before drafting. Bounds were followed: no subagents, no lane git/jj writes, and only this report was written in the lane.
- Checked the proposed `services/www/src/docs/content/build/plugins/index.mdx`, `services/www/src/docs/content/plugins.mdx`, and `opencode.ai/docs/plugins.md` paths against `corpus/SOURCES.md`; the exact-path searches returned **No matches found**. The S085 URLs are not base SOURCES URLs.
- Q30 sweep completed for the question “is there a plugin-specific JSON manifest?”:
  - Release notes: fetched root `CHANGELOG.md` at the pinned commit; case-insensitive search for `plugin.json`, `extension.json`, plugin/manifest combinations, and `package.json` returned **No matches found**. The wider plugin/extension search found release entries about plugin hooks/tools and a bundled Figma plugin/skills, but no manifest filename (e.g. `CHANGELOG.md:490-495`).
  - Current docs source tree: sparse-cloned `services/www/src/docs/content` at the `dev` tip below, then searched it for `manifest`, `plugin.json`, and `extension.json`. The only plugin manifest mention was `build/plugins/index.mdx:1770-1773`, which labels `package.json`; `troubleshooting.mdx:157` is an unrelated `manifest.json`. No plugin-specific JSON path was found.
  - Corpus: case-insensitive `plugin` search across `corpus/` returned 25 matching files (paged 20 + 5); a targeted case-insensitive search for `plugin.json`, `opencode-plugin.json`, and `.opencode/...plugin.json` returned **No matches found**. This was done with the specialized search tool rather than shell `grep`, per tool policy.
- **C1 gate:** no opencode row was run through `check_plugin_manifests.py --fetch`; that check was optional, and the documented `package.json`/directory tokens cannot satisfy its frozen v2 token grammar. No C1 predicate result is claimed. C2 remains withdrawn and untouched.
- Line-budget note: `SKILL.md` currently has 598/600 lines; any later integration of the seven-client table still needs the planned verbatim budget move. This report does not change `SKILL.md`.

## Fetch provenance and artifacts

`curl` outputs below include requested URL, final URL, HTTP status, byte count, and sha256. Every requested URL equaled its final URL.

1. Served official page, command: `curl --location --silent --show-error --dump-header /fast/scratch/hyaku/kotoba-r57/Srcopencode/plugins.headers --output /fast/scratch/hyaku/kotoba-r57/Srcopencode/plugins.md https://opencode.ai/docs/plugins.md --write-out ...`
   - `date -u`: `Fri 23 Oct 2026 04:46:54 AM UTC`
   - Requested/final: `https://opencode.ai/docs/plugins.md`; HTTP 200; 9,357 B; SHA-256 `c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e`.
   - Scratch file: `/fast/scratch/hyaku/kotoba-r57/Srcopencode/plugins.md`.
2. Source revision discovery: `git ls-remote https://github.com/anomalyco/opencode.git refs/heads/dev refs/heads/main` printed `bdf757209ff742b8551a4874347edb845241e5bb refs/heads/dev` (no `main` line).
3. Pinned top-level docs, changelog, and tree were fetched at `date -u` `Fri 23 Oct 2026 04:47:59 AM UTC`:
   - `https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx` → same final URL, HTTP 200, 4,371 B, SHA-256 `39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3`; file `/fast/scratch/hyaku/kotoba-r57/Srcopencode/plugins.mdx`.
   - `https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/CHANGELOG.md` → same final URL, HTTP 200, 50,001 B, SHA-256 `7c4cb74025c345d5a5df08195da5005674478055c6c804f25221f3bb931c519b`; file `/fast/scratch/hyaku/kotoba-r57/Srcopencode/root-CHANGELOG.md`.
   - `https://api.github.com/repos/anomalyco/opencode/git/trees/bdf757209ff742b8551a4874347edb845241e5bb?recursive=1` → same final URL, HTTP 200, 2,971,864 B, SHA-256 `c3b333bf9500b2c17753a7dd064f051014542a54c2f1076f2bdb71a1c4661317`; file `/fast/scratch/hyaku/kotoba-r57/Srcopencode/docs-tree.json`.
4. Pinned V2 build guide, command: `curl --location --silent --show-error --dump-header /fast/scratch/hyaku/kotoba-r57/Srcopencode/plugins-build-source.headers --output /fast/scratch/hyaku/kotoba-r57/Srcopencode/plugins-build-index.mdx https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx --write-out ...`
   - `date -u`: `Fri 23 Oct 2026 04:51:25 AM UTC`
   - Requested/final: `https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx`; HTTP 200; 60,780 B; SHA-256 `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5`.
   - Scratch file: `/fast/scratch/hyaku/kotoba-r57/Srcopencode/plugins-build-index.mdx`.
5. Docs-source clone command (all writes confined to seat scratch): `timeout 180s git clone --quiet --depth 1 --filter=blob:none --sparse https://github.com/anomalyco/opencode.git /fast/scratch/hyaku/kotoba-r57/Srcopencode/opencode-tree && timeout 60s git -C /fast/scratch/hyaku/kotoba-r57/Srcopencode/opencode-tree checkout -q bdf757209ff742b8551a4874347edb845241e5bb && timeout 60s git -C /fast/scratch/hyaku/kotoba-r57/Srcopencode/opencode-tree sparse-checkout set services/www/src/docs/content && git -C /fast/scratch/hyaku/kotoba-r57/Srcopencode/opencode-tree rev-parse HEAD` printed `bdf757209ff742b8551a4874347edb845241e5bb`.
6. An initial fetch attempt was rejected before execution because its requested working directory did not yet exist (`/fast/scratch/hyaku/kotoba-r57/Srcopencode`); the directory was then created, and the fetches above succeeded. No source bytes were written by the failed attempt.

## Touched surfaces, out of scope, and limits

- **Touched:** only `.ufo/waves/round-57/build/Srcopencode.md` in the lane; the served-page captures, pinned docs, release notes, tree listing, and sparse clone are under `/fast/scratch/hyaku/kotoba-r57/Srcopencode/`.
- **Not changed:** product `SKILL.md`, `corpus/SOURCES.md`, `corpus/knowledge/`, `corpus/lessons/round-57.md`, verifiers/counters, and C2 fence handling. No tool installed or updated; no sandbox commit; no runtime plugin load test.
- **Known limit:** the served `/docs/plugins.md` capture (9,357 B) differs materially from the pinned `dev` source `plugins.mdx` (4,371 B). The report uses the pinned V2 source for S085 and does not combine their line numbers. Claims are documentation readings, not execution evidence.
- **Next integration decision:** S085 can document the generic `package.json` manifest and plugin APIs, but the opencode SKILL/entry row must be excluded from the frozen C1 count unless the vendor docs provide an actually spelled, plugin/extension-named JSON manifest path. No such path was found in the completed Q30 sweep.