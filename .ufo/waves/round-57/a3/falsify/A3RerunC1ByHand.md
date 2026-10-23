Result: MIXED — Reading the seven source pages yields six documented manifest-location rows, not four; the frozen counter's four-of-four MISS remains a different, narrower measurement.

# Scope and method

Axes: depth and calibration. Reviewed `SKILL.md:111–123` and `corpus/SOURCES.md:92–98` at lane revision `07c33d73ddce769d9cea2846a6313164401b5478`. Base: `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`.

I extracted each manifest cell's first backticked token, fetched its S079–S085 page with curl, and read the documentation. I neither read nor executed `verifiers/check_plugin_manifests.py`. The reported counter classifications below come from the existing `.ufo/waves/round-57/C1-measure.txt:5–13`, not a fresh counter run. This is an independent source-reading method, not a claim of a blind review: the assignment and receipt already disclosed the four-of-four result.

All fetched bytes and headers are under `/fast/scratch/hyaku/kotoba-r57a3/A3RerunC1ByHand/` (abbreviated `scratch/` below), in my isolated checkout. No sandbox commits were created. No evidence was taken from the forbidden prior-attempt locations or from the untrusted candidate patch.

# Hand count

| Client / SKILL line | First token | Page states this is a manifest location? | Base occurrences | Existing counter receipt |
|---|---|---|---:|---|
| Claude Code / 117 | `.claude-plugin/plugin.json` | Yes; S079:34,617 | 0 | BACKED |
| Codex / 118 | `.codex-plugin/plugin.json` | Yes; compatibility manifest, S080:24–26,76 | 0 | BACKED |
| VS Code / 119 | `plugin.json` | Yes; root manifest, S081:45–47,97–104 | 0 | Rejected: token shape and sharing |
| Copilot CLI / 120 | `plugin.json` | Yes; root manifest, S082:14,27 | 0 | Rejected: token shape and sharing |
| Gemini CLI / 121 | `gemini-extension.json` | Yes; required root file, S083:106–111 | 0 | BACKED |
| Cursor / 122 | `.cursor-plugin/plugin.json` | Yes; Cursor Plugin format, S084:27–28,207–208 | 0 | BACKED |
| opencode / 123 | `.opencode/plugins/` | No; automatically loaded module directory, S085:10–22 | 0 | Rejected: token shape |

**Manual F = 6 of 7 rows.** That does not agree with `4 of 4` as a census of documented manifest locations. It does agree that all four rows the receipt calls BACKED really are backed. The two disagreements are VS Code and Copilot CLI: a reader accepts both documented root manifests, while the frozen instrument rejects both. The opencode rejection is not a reader/instrument disagreement about the first token: its directory is not a manifest.

**New ground:** six source-backed client rows have zero base occurrences. They represent **five distinct case-folded supported token values**, because VS Code and Copilot CLI share `plugin.json`. Thus the hand-derived source-backed distinct-token count is **5**, not 6. The directory token is also absent at base, but its absence cannot earn manifest new ground. The existing instrument's G=4 is consistent with excluding both root-manifest rows. These alternative counts do not replace the frozen predicate or turn its recorded exit 1 into a pass.

## Reading evidence

Each quotation below is a byte-exact contiguous substring of the fetched bytes, preserves Markdown, and is at most 25 words. No Markdown bytes or internal line breaks were stripped.

1. **Claude Code**, `scratch/S079.md:34`:
   ```text
   Save the manifest at `.claude-plugin/plugin.json` under the plugin root.
   ```
2. **Codex**, `scratch/S080.md:76`:
   ```text
   Only `.codex-plugin/plugin.json` is always created.
   ```
   The compatibility-fallback explanation is at :24–26; this is not confusing the compatibility layout with the portable root manifest.
3. **VS Code**, `scratch/S081.md:47`:
   ```text
   An Agent Plugins 1.0 package has a `plugin.json` file at its root that declares the standard's schema:
   ```
4. **Copilot CLI**, `scratch/S082.md:27`:
   ```text
   2. Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory.
   ```
5. **Gemini CLI**, `scratch/S083.md:106–107`:
   ```text
   Gemini CLI loads extensions from `<home>/.gemini/extensions`. Each extension
   must have a `gemini-extension.json` file in its root directory.
   ```
6. **Cursor**, the contiguous suffix/prefix across `scratch/S084.md:207–208`:
   ```text
   A Cursor Plugin has a
   `.cursor-plugin/plugin.json` manifest.
   ```
7. **opencode**, `scratch/S085.mdx:21`:
   ```text
   Plugins under `.opencode/plugins/` are loaded automatically, like the local example above.
   ```
   This describes loading modules, not a manifest filename. The same document explicitly introduces a package manifest at :1770–1771:
   ```text
   A package plugin uses the same default export as a local plugin. A minimal
   manifest is:
   ```
   Its immediately following JSON fence is titled `package.json` (:1773), with package fields and exports at :1774–1785.

# Findings and smallest safe corrections

## F1 — Two source-backed rows are excluded by the instrument's representation rules

Evidence: the VS Code and Copilot CLI excerpts above versus `.ufo/waves/round-57/C1-measure.txt:8–9`. Root `plugin.json` is expressly documented as the manifest, not merely mentioned in navigation, a changelog, or unrelated prose. Both live page hashes equal their recorded SOURCES hashes, so source drift does not explain the discrepancy.

Impact: **depth** if four is presented as the number of documented manifest locations; **calibration** if eligibility rejection is presented as source rejection or if the verifier is credited with checking the entire table.

The frozen counter legitimately applies its declared restrictions; the defect is conflating that subset with the source census. Do not change its grammar, threshold, or duplicate policy in this round, and do not substitute a legacy path merely to manufacture a fifth counted row.

Smallest attribution correction, `SKILL.md:113`, exact old → new:

- Old: `locations and quotes checked by `verifiers/check_plugin_manifests.py`, the other cells are reviewer readings.`
- New: `` `verifiers/check_plugin_manifests.py` checks eligible manifest rows only; root `plugin.json` rows, the opencode directory and other cells require reviewer readings.``

Keep the measured `4 of 4; new ground 4`, exit 1, intact, and identify the independent source-reading result separately as F=6/7, five distinct new supported token values.

## F2 — opencode's directory is correctly uncounted, but “no JSON manifest” overstates the documentation

Evidence: `SKILL.md:123`, `corpus/knowledge/plugin-manifests-round57.md:17–18,77–78`, and the rejected `package.json` rationale at `corpus/lessons/round-57.md:34` versus `scratch/S085.mdx:1768–1786`. S085 calls the package file a minimal manifest. Local-module discovery and package-manifest metadata are distinct cases; a generic package manifest is not a standalone plugin-specific filename, but that does not mean there is no JSON manifest to read.

Impact: **depth** and **calibration**. This is a fixable content distinction, not a reason to alter the frozen counter or count the directory as a manifest. `corpus/SOURCES.md:98` already makes the package/local distinction and needs no correction for this finding.

Smallest coordinated wording corrections, exact old → new:

- `SKILL.md:123`, manifest cell:
  - Old: `` `.opencode/plugins/` (no JSON manifest: a plugin is a JavaScript/TypeScript module)``
  - New: `` `.opencode/plugins/` (local modules, not a manifest; packaged plugins use `package.json`)``
- `SKILL.md:123`, action cell:
  - Old: `Review the module code; there is no manifest to read`
  - New: ``Review the module code and, for packaged plugins, `package.json` ``
- `corpus/knowledge/plugin-manifests-round57.md:17–18`:
  - Old:
    ```text
    opencode plugins are code modules with no JSON
    manifest.
    ```
  - New:
    ```text
    opencode local plugins are code modules, while packaged plugins use
    `package.json`.
    ```
- The same entry :77, replace only the quoted assertion:
  - Old: `"no JSON manifest"`
  - New: `"local modules and package manifests are distinct"`
- `corpus/lessons/round-57.md:34`, rejected-item reason:
  - Old: `a published package's metadata file, not a plugin manifest; the row names the plugin folder and says there is no JSON manifest`
  - New: `` `package.json` is documented as a package-plugin manifest (S085:1768–1786), but it does not meet C1's frozen token grammar``

The first token can remain the explicitly labelled directory. These wording corrections do not change this review's F=6/7 or the counter receipt.

## F3 — The miss is observed; a global honest-population ceiling is not established by it

Evidence: `corpus/lessons/round-57.md:92–100` names M62 `target-above-reachable-population`, calls four the honest own-format count, and says “zero margin.” The source reading above finds six truthful manifest-location rows. `scratch/S081.md:99–104` also documents VS Code's Legacy OpenPlugin `.plugin/plugin.json`; the entry itself acknowledges that alternate at :19. The landed row rule, fixed after counter freeze (:14–20), deliberately chooses the root default instead.

The receipt establishes the selected table's **one-row shortfall** from F>=5, not that all truthful content is bounded at four. [INFERENCE] A complete global reachability claim would need to account for documented alternate formats and every frozen guard; I did not execute a counter experiment to establish such a bound. Choosing those alternates can sacrifice the table's native/default-format selection policy, so it is not automatically a safe improvement.

Impact: **calibration**. Preserve the MISS. Scope the lesson to the selected row rule rather than treating a token-filter result as a census of reality.

Smallest wording corrections in `corpus/lessons/round-57.md:92–96`, exact old → new:

- `target-above-reachable-population` → `selected-token-population-below-target`
- `honest count is 4` → `own-format count is 4`
- `The zero margin was reported` → `The one-row shortfall under the chosen row rule was reported`

# Reproduction evidence

## Curl fetches

For each row I ran the following command from the isolated checkout, substituting the exact URL and output filename in the table. All seven command chains exited **0**; every final HTTP status was **200**. The status and byte counts below are curl's observed write-out, not inferred from the SOURCES entries.

```sh
timeout 5s date -u && timeout 70s curl --location --silent --show-error --max-time 60 --dump-header S079.headers --output S079.md --write-out 'http=%{http_code} bytes=%{size_download} final=%{url_effective}\n' https://code.claude.com/docs/en/plugins-reference.md && timeout 5s sha256sum S079.md && printf 'exit 0\n'
```

| ID / output | URL (also final URL) | Verbatim `date -u` output | HTTP | Bytes | SHA256 |
|---|---|---|---:|---:|---|
| S079.md | https://code.claude.com/docs/en/plugins-reference.md | Fri 23 Oct 2026 06:46:18 AM UTC | 200 | 42124 | f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e |
| S080.md | https://developers.openai.com/plugins/build/plugins.md | Fri 23 Oct 2026 06:46:18 AM UTC | 200 | 38036 | c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1 |
| S081.md | https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | Fri 23 Oct 2026 06:46:18 AM UTC | 200 | 21972 | d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e |
| S082.md | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md | Fri 23 Oct 2026 06:46:18 AM UTC | 200 | 7711 | c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64 |
| S083.md | https://geminicli.com/docs/extensions/reference.md | Fri 23 Oct 2026 06:46:31 AM UTC | 200 | 12022 | 8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72 |
| S084.md | https://cursor.com/docs/plugins.md | Fri 23 Oct 2026 06:46:31 AM UTC | 200 | 20323 | 74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62 |
| S085.mdx | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx | Fri 23 Oct 2026 06:46:31 AM UTC | 200 | 60780 | e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5 |

All seven hashes equal the corresponding committed S079–S085 hashes at the reviewed revision. Headers are `scratch/S079.headers` through `scratch/S085.headers`.

## Base-token counts

Working directory: `/fast/scratch/hyaku/kotoba-r57a3/A3RerunC1ByHand`. Each following pipeline was run separately, once per client row, including the duplicate root token. Each printed **0** and the pipeline exited **0** (the `wc` result; no claim that a no-match `git grep` exits zero). The last three additionally printed `pipeline exit 0`.

```sh
# Claude Code
timeout 30s git --no-optional-locks grep -i -F -o '.claude-plugin/plugin.json' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- . ':!.ufo' | timeout 5s wc -l
# Codex
timeout 30s git --no-optional-locks grep -i -F -o '.codex-plugin/plugin.json' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- . ':!.ufo' | timeout 5s wc -l
# VS Code
timeout 30s git --no-optional-locks grep -i -F -o 'plugin.json' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- . ':!.ufo' | timeout 5s wc -l
# Copilot CLI
timeout 30s git --no-optional-locks grep -i -F -o 'plugin.json' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- . ':!.ufo' | timeout 5s wc -l
# Gemini CLI
timeout 30s git --no-optional-locks grep -i -F -o 'gemini-extension.json' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- . ':!.ufo' | timeout 5s wc -l && printf 'pipeline exit 0\n'
# Cursor
timeout 30s git --no-optional-locks grep -i -F -o '.cursor-plugin/plugin.json' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- . ':!.ufo' | timeout 5s wc -l && printf 'pipeline exit 0\n'
# opencode
timeout 30s git --no-optional-locks grep -i -F -o '.opencode/plugins/' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- . ':!.ufo' | timeout 5s wc -l && printf 'pipeline exit 0\n'
```

No counters, tests, client runtimes, model calls, or judgment runtimes were executed. No tools were installed or updated. Only this report was written in the lane. The broader candidate-patch, ship-cell, quote-note and no-harm reviews are not claimed by this scoped report.
