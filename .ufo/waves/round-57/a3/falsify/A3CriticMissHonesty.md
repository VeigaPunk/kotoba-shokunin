Result: MIXED — the declared 4-of-4 miss and the candidate's manifest-token preservation hold, but the lesson overstates an own-format census as an honesty ceiling and the opencode explanation overstates the source.

## Scope and axes

Reviewed `07c33d73ddce769d9cea2846a6313164401b5478`, the C1 receipt at `ac22ca8791980314a37eb1daa69b846f80a1b9e2`, and the candidate diff as untrusted proposed text only. Axes: calibration and depth. This is an advisory criticism, not an admission or canonical judgment. No lane code, counter, test, client CLI, or other judging runtime was executed. No lane files were edited; this report is the only lane write. No tools were installed or updated.

`FETCH` below means `/fast/scratch/hyaku/kotoba-r57a3/A3CriticMissHonesty`. All fetched-byte evidence is in that sandbox, not any prohibited earlier-attempt directory.

## 1. The seven rows apply the stated rule consistently, but the rule is not the frozen predicate

The rule is own-format first, otherwise the documented default (`corpus/knowledge/plugin-manifests-round57.md:14-20`; `SKILL.md:113`). It explicitly dates its selection after the counter freeze. The frozen predicate instead accepts certain non-foreign, sufficiently scoped manifest filenames; it does not require a client-named format (`verifiers/check_plugin_manifests.py:71-100,108-132`). The entry itself acknowledges that the counter does not check the row rule (`corpus/knowledge/plugin-manifests-round57.md:67-74`).

| Row | Landed first token / rule application | Independent source-byte evidence | Counting effect |
|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json`: own-format path; optional is disclosed | `FETCH/S079.md:30-34` | Counted, as receipt line 6 records |
| Codex | `.codex-plugin/plugin.json`: client-named compatibility format, not the portable default; that limitation is disclosed | `FETCH/S080.md:14-26,54-62,76-88`; `SKILL.md:118` | Own-first selects a passing token where portable-default-first would select rejected root `plugin.json`; this is a policy effect, not a per-row exception |
| VS Code | `plugin.json`: neither client-named format is documented; choose root default, while listing supported foreign/legacy forms | `FETCH/S081.md:97-104`; `SKILL.md:119` | Fails; the documented `.plugin/plugin.json` is omitted as the leading token under this policy, not because it is undocumented |
| Copilot CLI | `plugin.json`: its creation guide names the root manifest; the legacy paths are only referred to here | `FETCH/S082.md:14-27`; `SKILL.md:120`; lesson `:36` identifies the base-S028 exclusion | Fails; using the base reference for a new backed source is independently barred, so its legacy path is not a fifth from these seven sources |
| Gemini CLI | `gemini-extension.json`: client-named required root file | `FETCH/S083.md:104-111` | Counted, as receipt line 10 records |
| Cursor | `.cursor-plugin/plugin.json`: own named format; Agent Plugins root form also disclosed | `FETCH/S084.md:25-30,255-258`; `SKILL.md:122` | Counted; own-format preference rather than the first/portable format in the docs |
| opencode | `.opencode/plugins/`: explicitly a discovery directory, not a purported JSON manifest | `FETCH/S085.mdx:10-22`; package manifest at `:1768-1786`; `SKILL.md:123` | Fails regardless of choosing this directory or `package.json`; the latter lacks the required plugin/extension word in its final filename (`verifiers/check_plugin_manifests.py:535-558`) |

**Answer to tuning:** no row-specific exception is evident. A single own-first/default policy explains all the selections, including the unfavorable VS Code result. Its effects are not uniformly conservative: it helps Codex, keeps Cursor's client-specific form, and excludes VS Code's qualifying legacy form. That does not establish the author's motive, nor does uniform application establish that this is the only honest policy. The opencode row also needs an explicit no-qualifying-manifest branch in the prose rule: a directory is not a documented default manifest.

## 2. Strongest counterexample: another client-neutral rule can supply a fifth

Counterexample rule, applied to every client: **prefer the client's named format; otherwise prefer a documented, non-foreign format-specific manifest path over a generic root manifest; otherwise use the documented root default. Always identify compatibility/legacy status and disclose the root default.** This is a different policy, not a proposed correction to the measured rows.

It preserves the four counted tokens and selects VS Code's `.plugin/plugin.json`, explicitly labelled Legacy OpenPlugin, while Copilot CLI still uses the root token on S082. No token collision is introduced. The VS Code source already supports both the legacy path and the default, so naming the former as a supported legacy format need not falsely call it the default.

Live, byte-exact two-row quote from `FETCH/S081.md:103-104` (11 whitespace-delimited words, no markdown removed):

```text
| Claude | `.claude-plugin/plugin.json` |
| Legacy OpenPlugin | `.plugin/plugin.json` |
```

The token has two segments and a `plugin.json` final segment, contains no foreign marker, and is distinct from the other six first tokens. The quote holds a plugin word outside the target token, in the adjacent Claude path. Those are the actual frozen conditions, not an assertion that OpenPlugin is VS Code's native/default format (`verifiers/check_plugin_manifests.py:535-567,634-643,663-674`). S081's source URL and eligibility are already used by the landed entry. The same quote and path were independently proposed before landing in `.ufo/waves/round-57/build/SrcVSCode.md:5-18,29-35` and discussed in `build/ScoutPluginMcp.md:106-110`.

**[INFERENCE, not a run or a new receipt]:** a coherent separate world replacing VS Code's SKILL token, entry token/quote and Gate quote with these supported legacy-format values could reach F=5, K=5. The existing four distinct new-ground tokens already supply G=4, so an added fifth cannot make G<3. I did not construct or execute that world. This refutes the stronger claim that *no client-neutral honest selection could reach five*; it does not refute the observed F=4 for the actual landed policy.

Depth tradeoff: legacy-first would make a secondary format more prominent than the default. The actual row policy is defensible on that usability basis. Changing it after measurement would change the measured content, not repair the historical receipt. Preserve the declared miss and all measured tokens; the canonical judge owns any disposition.

## 3. Receipt versus the records

The actual after receipt is `.ufo/waves/round-57/C1-measure.txt:1-13`: F=4, K=4, G=4, exit 1. It counts Claude Code, Codex, Gemini CLI and Cursor and rejects VS Code, Copilot CLI and opencode. K is grammar-eligible rows, **not all seven clients** (`verifiers/check_plugin_manifests.py:100,727-740`). Thus this is not a seven-client completeness result.

The before value is real but is in a different receipt: `.ufo/waves/round-57/controls/C1-base-v2.txt:14-25` records `0 of 0; new ground 0`, exit 1. `C1-measure.txt` itself contains only the after measurement and a non-fetch after run.

| Record | Comparison with evidence |
|---|---|
| `SCORECARD.md:28`, depth-row lead | Honest about MISS, exit 1, F=4 and G=4, measured content commit, and score held 9. Its four-own-format explanation is independently supported by source reading, not measured by the counter. The attached C1-measure pointer alone does not supply the before value; the base-v2 receipt does. No inflated passing result or score increase found. |
| `SCORECARD.md:148`, `**Round 57` line | Same honest miss and threshold. No claim of passing C1 or measured loading. It is a shorter result summary, not a stronger receipt. |
| `LOG.md:2488-2493`, Round 57 | Numeric result and rejected VS Code alternative match the receipt and sources. The extra claim `opencode has no JSON manifest` is too broad: its own pinned build guide expressly calls the package-plugin `package.json` a minimal manifest. See finding 4. |
| `corpus/README.md:147-153`, round-57 note | Conservatively says recorded, not held as a verified claim; gives F=4/G=4 and the unmet threshold; explicitly leaves runtime loading and plugin-shipped MCP instructions unheld. No numerical inflation found. Its seven-client description is documentation coverage, not seven successful counter rows. |
| `corpus/lessons/round-57.md:92-100`, M62 | Goes further than the receipt with `target-above-reachable-population`, `the honest count is 4`, and a census framed only around own-format manifests. Four is correct **under the landed own-first/default policy**, not the maximum reachable under the frozen grammar and these sources. The counterexample in section 2 matters. |

The lesson's zero-margin attribution also needs separation from the landed policy. The cited build reports discuss broader legacy-path configurations: `build/CriticC1Rows.md:35-42,98-108` offers legacy paths; `build/ScoutPluginMcp.md:71-88` includes the VS Code legacy path but excludes Copilot's base source; `build/CriticAxisFit.md:42-49` discusses another five-client configuration. They do not prove that an own-format population of four leaves zero slack against a target of five. Under the landed rule that difference is minus one, not zero.

**Impacted axes:** calibration primarily (do not turn an observed miss into a universal impossibility claim); depth secondarily (preserve default-versus-supported-legacy distinctions). This is a fixable explanation defect, not grounds to relabel the historical exit 1 as a pass.

## 4. Positive source contradiction: opencode does call a JSON file a manifest

`FETCH/S085.mdx:1770-1773` says, byte-exact, with no shaping:

```text
A package plugin uses the same default export as a local plugin. A minimal
manifest is:

```json title="package.json"
```

The prose quote is 16 words; the last displayed line is the source fence opener identifying the file, not prose. This is positive evidence, not a silence claim. I did not perform an independent Q30 changelog + current-docs-tree + corpus silence sweep and make no client-wide negative assertion.

Consequences:

- `LOG.md:2493`, entry `:17-18,77-78`, and lesson Gate `:34` say more than this source supports with unqualified `no JSON manifest` / `not a plugin manifest` wording.
- `SKILL.md:123` also says `there is no manifest to read`; that overstates a discovery-directory row for a package plugin.
- The candidate partially repairs entry `:17-18` in its diff lines 62-64 by distinguishing a plugin-specific manifest, but candidate line 25 retains the SKILL parenthetical `no JSON manifest` and the action `there is no manifest to read`, next to its new `package.json` qualification.
- None of this supplies an additional counted row: `package.json` fails the frozen filename grammar. Correct the explanation without replacing `.opencode/plugins/`.

## 5. Candidate patch does not change a counted manifest token

Read the full 119-line candidate diff; I did not apply it. Evidence below concerns what its proposed bytes change, not the truth of its source/receipt claims.

The first-backtick token vector before and after is identical:

```text
Claude Code  .claude-plugin/plugin.json
Codex        .codex-plugin/plugin.json
VS Code      plugin.json
Copilot CLI  plugin.json
Gemini CLI   gemini-extension.json
Cursor       .cursor-plugin/plugin.json
opencode     .opencode/plugins/
```

- Candidate `.ufo/waves/round-57/a3/a2-candidate.patch:14-25`: changes ship cells, not any manifest cell or action cell; its unchanged context includes the other token rows. In particular the newly added `package.json`, local-plugin paths and `CLAUDE.md` are in ship cells, not the first-backtick manifest cell.
- Candidate `:47-75`: changes entry prose before the first table, not the first table's tokens, source IDs or quotes. The later hunk starts at original entry line 29 with unchanged Cursor/opencode context, then edits quote notes and later sections.
- Candidate `:33-39`: appends S086–S088; it neither modifies S079–S085 nor points the measured first table at the new IDs. `sources_table` resolves by the entry's S-id and does not interpret `supersedes` prose (`verifiers/check_plugin_manifests.py:436-444,659-707`).
- No frozen-counter or lesson-Gate file appears in the candidate diff.

Therefore **no counted manifest token changes**, and no token-based promotion of this miss is hidden in the candidate. This is static diff evidence, not an executed post-patch counter result.

One separate provenance risk: candidate `:111-116` appends the counter command directly to the *own-format census*. The counter expressly does not check that row rule (entry `:73-74`). Numerical agreement between the own-format census and F=4 is not proof that the counter measures the census. Keep those two observations separately labelled.

## 6. Smallest safe corrections — exact old → new, without token changes

These are suggestions to L1 only. Do not edit counters, reselect historical row tokens, replace the receipt, or rewrite append-only LOG history.

### A. Qualify the lesson's ceiling, and distinguish margins

At `corpus/lessons/round-57.md:92`, old:

`(the mined mistake)`

New:

`(the mined mistake; population under the landed row policy)`

At `:93-94`, old:

`set before any census of how many clients document an own-format plugin manifest; the\n  honest count is 4 (Claude Code, Codex, Gemini CLI, Cursor)`

New:

`set before a census and before the row-selection policy was fixed; the count under the landed own-format-first/default rule\n  is 4 (Claude Code, Codex, Gemini CLI, Cursor)`

At `:95-96`, old:

`The zero margin was reported\n  during the build wave (`CriticAxisFit`, `ScoutPluginMcp`, `CriticC1Rows`, ~04:50–04:54Z), after the target was frozen`

New:

`Build critics reported zero-margin configurations using legacy paths\n  (`CriticAxisFit`, `ScoutPluginMcp`, `CriticC1Rows`, ~04:50–04:54Z), after the target was frozen. Those were not a census under the landed rule: four eligible rows against a target of five leaves a deficit of one. A different uniform rule allowing a documented non-foreign format-specific fallback could add VS Code's Legacy OpenPlugin `.plugin/plugin.json` (S081 `:103-104`); that is a counterfactual, not a replacement measurement`

Q45's census remains useful; its application should bind both the source/token rules and the proposed row-selection policy. Do not present it as already preventing a later round's failure.

### B. Replace the overbroad opencode explanation with the documented, non-countable package case

For the explanatory text in entry `:17-18`, old:

`opencode plugins are code modules with no JSON\nmanifest.`

New:

`opencode plugins are code modules; the package-plugin `package.json` is called a minimal manifest,\nbut its filename does not meet the frozen counter grammar (S085 `index.mdx:1770-1773`).`

For `SKILL.md:123` (also retained in candidate line 25), old:

`(no JSON manifest: a plugin is a JavaScript/TypeScript module)`

New:

`(code-module discovery folder; package plugins use `package.json`)`

Same row's action, old:

`Review the module code; there is no manifest to read`

New:

`Review the module code and any package metadata`

For lesson Gate `:34`, old reason:

`a published package's metadata file, not a plugin manifest; the row names the plugin folder and says there is no JSON manifest`

New reason:

`the package-plugin `package.json` is called a minimal manifest by S085 `index.mdx:1770-1773`, but its filename fails the frozen token grammar; retain the discovery-folder token`

For entry Limits `:77-78`, old:

`opencode: "no JSON manifest" is read from the pinned V2 build guide and its sweep in `Srcopencode.md` (docs tree,\n  changelog, lane corpus); a `package.json` describes a published package, not a plugin-specific manifest.`

New:

`opencode: the pinned V2 build guide calls the package-plugin `package.json` a minimal manifest (`index.mdx:1770-1773`),\n  but that filename fails the frozen token grammar; `.opencode/plugins/` is a discovery folder, not a manifest file.`

For append-only `LOG.md:2493`, do not rewrite the old clause. Append a named correction stating the intended old → new:

`opencode has no JSON manifest` → `opencode's package-plugin `package.json` is called a minimal manifest, but its filename does not meet the frozen counter grammar; C1 remains 4 of 4, new ground 4, exit 1 at ac22ca87`.

### C. Keep the candidate's census and frozen measurement distinct

Candidate lines 111-116, old proposed paragraph:

```text
- Four of seven clients document an own-format manifest path (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`,
  `gemini-extension.json`, `.cursor-plugin/plugin.json`) — 4 — `python3 -B verifiers/check_plugin_manifests.py --rev
  ac22ca87 --fetch` 2026-10-23 (`.ufo/waves/round-57/C1-measure.txt`). VS Code, Copilot CLI, Codex and Cursor also read
  the shared Agent Plugins root `plugin.json`, so a root `plugin.json` alone does not tell which client a plugin targets.
```

New:

```text
- Four of seven clients document an own-format manifest path (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`,
  `gemini-extension.json`, `.cursor-plugin/plugin.json`): a source-reading census under the row rule above (S079–S085),
  not a rule the counter measures. Separately, `python3 -B verifiers/check_plugin_manifests.py --rev ac22ca87 --fetch`
  on 2026-10-23 produced `plugin manifests found on the live page 4 of 4; new ground 4`, exit 1
  (`.ufo/waves/round-57/C1-measure.txt`). VS Code, Copilot CLI, Codex and Cursor also read the shared Agent Plugins
  root `plugin.json`, so a root `plugin.json` alone does not tell which client a plugin targets.
```

### D. Tighten the before/after receipt pointers

At the C1 pointer in the depth-row lead, old:

`(.ufo/waves/round-57/C1-measure.txt)` (the path is backticked in the file).

New:

`(before: `.ufo/waves/round-57/controls/C1-base-v2.txt:14-25`; after: `.ufo/waves/round-57/C1-measure.txt:1-13`)`.

The same distinction can be stated in the appended LOG correction. The numerical records and declared miss otherwise need no correction.

## Commands and live fetch receipts

Observed read-only lane command, exit 0:

```sh
timeout 30s git --no-optional-locks rev-parse HEAD
```

Output: `07c33d73ddce769d9cea2846a6313164401b5478`.

Observed content-continuity command, exit 0, no output:

```sh
timeout 30s git --no-optional-locks diff ac22ca8791980314a37eb1daa69b846f80a1b9e2 07c33d73ddce769d9cea2846a6313164401b5478 -- SKILL.md corpus/knowledge/plugin-manifests-round57.md corpus/SOURCES.md verifiers/check_plugin_manifests.py
```

This establishes no changes in those measured surfaces between the content commit and the attacked tip; it is not a counter execution.

Sandbox preparation, exit 0, no output:

```sh
timeout 120s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3CriticMissHonesty && timeout 30s git -C /fast/scratch/hyaku/kotoba-r57a3/A3CriticMissHonesty checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

Each source fetch used the following exact command form in `FETCH`, with FILE and URL instantiated by the table; each command completed exit 0. No browser, access-control bypass, paid calls, or retries were used.

```sh
timeout 5s date -u && timeout 65s curl -L -sS --fail-with-body --max-time 60 -o FILE -w 'HTTP %{http_code}; bytes %{size_download}; URL %{url_effective}\n' URL && timeout 5s sha256sum FILE
```

First four commands printed this date line: `Fri 23 Oct 2026 06:46:52 AM UTC`.
Last three commands printed this date line: `Fri 23 Oct 2026 06:47:18 AM UTC`.

| FILE | URL / effective URL (identical) | HTTP | bytes | sha256 |
|---|---|---|---:|---|
| S079.md | https://code.claude.com/docs/en/plugins-reference.md | 200 | 42124 | `f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e` |
| S080.md | https://developers.openai.com/plugins/build/plugins.md | 200 | 38036 | `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1` |
| S081.md | https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | 200 | 21972 | `d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e` |
| S082.md | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md | 200 | 7711 | `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64` |
| S083.md | https://geminicli.com/docs/extensions/reference.md | 200 | 12022 | `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72` |
| S084.md | https://cursor.com/docs/plugins.md | 200 | 20323 | `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62` |
| S085.mdx | https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx | 200 | 60780 | `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` |

All seven byte hashes match the committed S079–S085 access records. This report independently re-opened only those sources; it does not certify S086–S088 or any attempt-2 fetch receipt.

Report: .ufo/waves/round-57/a3/falsify/A3CriticMissHonesty.md
