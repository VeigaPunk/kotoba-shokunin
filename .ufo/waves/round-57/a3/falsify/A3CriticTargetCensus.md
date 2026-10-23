Result: BREAKS — four is the selected-row score, not a demonstrated ceiling under the frozen grammar; independently fetched docs expose additional supported paths, and an executable Q45 record check rejects round 57's uncensused plan.

## Scope and axes

Reviewed `07c33d73ddce769d9cea2846a6313164401b5478`, specifically M62, Q45, the C1 plan and frozen token rule. Primary axis: calibration; secondary: consistency and depth (distinguishing a client's default, compatibility format, and recognized third-party format). This is criticism, not admission or a claim verdict. The declared `4 of 4; new ground 4`, exit 1 remains a MISS. No counter, lane content, index or jj state was changed; no judge or model runtime was invoked. No attempt-2 candidate or prohibited attempt scratch was used as evidence.

All `census-fetch/` and `census-upstream-*/` paths below are inside my sandbox `/fast/scratch/hyaku/kotoba-r57a3/A3CriticTargetCensus/`, cloned and checked out at the reviewed lane revision. The counter there hashes to `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`. No sandbox commit was made.

## 1. The population changes when the actual frozen rule replaces the later row-selection rule

**Counterexample:** VS Code's own, newly cited S081 page documents `.plugin/plugin.json` for Legacy OpenPlugin. It passes the frozen token rule, carries no foreign-client marker, and is on a non-base documentation URL. This path was consciously omitted by the later own-format-first row rule; it was not absent from the honest documented population.

Evidence:

- `verifiers/check_plugin_manifests.py:535-558`: two or more path segments are an alternative to containing the row's own client marker. The rule does **not** require a client-named path, the default format, or a non-legacy format.
- `verifiers/check_plugin_manifests.py:561-567`: the separate foreign-marker guard also permits `.plugin/plugin.json` for VS Code and `.github/plugin/plugin.json` for Copilot CLI.
- `census-fetch/vscode.md:103-104`, byte-exact, including the LF, no bytes removed (11 whitespace-delimited words):

  ```text
  | Claude | `.claude-plugin/plugin.json` |
  | Legacy OpenPlugin | `.plugin/plugin.json` |
  ```

- `census-fetch/vscode.md:97-104` identifies auto-detection and the four formats. The excerpt's plugin word outside the chosen token comes from the adjacent Claude-path token; this is mechanically accepted, not evidence that OpenPlugin is VS Code's proprietary format.
- `corpus/knowledge/plugin-manifests-round57.md:14-20` explicitly says its own-format-first row rule was fixed **after** counter freeze and that `.plugin/plugin.json` would pass but was not selected. Thus the round itself records the distinction M62 later collapses.
- `corpus/knowledge/plugin-manifests-round57.md:43` counts Codex's supported compatibility manifest. Legacy/compatibility status alone is not a uniform reason that a supported manifest cannot be documented honestly.

### Independent seven-client census

This table counts **documented supported manifest paths satisfying the frozen grammar and foreign-name guard**, not rows already scored, not proprietary formats, and not a full C1 pass.

| Client | Independently found path | Documentation evidence in fetched bytes | Frozen grammar / foreign guard | Important qualification |
|---|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` | `census-fetch/claude.md:34` | pass / none | Existing counted client; optional manifest. |
| Codex | `.codex-plugin/plugin.json` | `census-fetch/codex.md:24-26,135-137` | pass / none | Supported compatibility fallback, not portable root default. |
| VS Code | `.plugin/plugin.json` | `census-fetch/vscode.md:97-104` | pass / none | Additional supported Legacy OpenPlugin format; not a VS Code-named proprietary format. S081 URL is new relative to base. |
| Copilot CLI | `.github/plugin/plugin.json` | `census-fetch/copilot-reference.md:402` | pass / none | Additional legacy Copilot path; the fetched reference URL is base S028, so **this citation cannot add a FOUND row**. |
| Gemini CLI | `gemini-extension.json` | `census-fetch/gemini.md:106-107` | pass / none | Existing counted client; required root extension file. |
| Cursor | `.cursor-plugin/plugin.json` | `census-fetch/cursor.md:27-30,207-209` | pass / none | Existing counted client; distinct from portable root format. |
| opencode | No eligible path found in completed sweep | `census-fetch/opencode-current-build.mdx:1770-1785`; current docs tree, changelog and corpus searches below | `package.json` fails; plugin directories fail | Package metadata is documented; no plugin/extension-named JSON path was found. |

Therefore: **six clients have a documented supported path meeting token shape/identity in this census; five of those have a non-base source URL here. Four remains the chosen-row result, not the frozen grammar's maximum.** Do not report six FOUND clients: Copilot's source-URL eligibility is a separate failing guard. Do not report a measured five-client pass either: I did not change the table, entry, Gate or row-selection policy and did not run such a world.

[INFERENCE] Keeping the four already-counted rows and honestly labeling VS Code's supported legacy path supplies a plausible fifth under the frozen predicate, without lowering F or G. Whether leading a reader-facing row with that compatibility path harms the intended decision table is a content/judgment tradeoff, not proof that only four clients document counter-shaped manifests. The canonical judge must decide that tradeoff; this seat does not.

Further exact evidence, each a contiguous byte span with no markup stripped:

- Claude, `census-fetch/claude.md:34`: "Save the manifest at `.claude-plugin/plugin.json` under the plugin root."
- Copilot, substring of `census-fetch/copilot-reference.md:402`: "Legacy plugins: `.plugin/plugin.json`, `plugin.json`, `.github/plugin/plugin.json`, or `.claude-plugin/plugin.json` (checked in this order)."
- VS Code conventional extension manifest, `census-fetch/vscode-extension-manifest.md:6`: "Every Visual Studio Code extension needs a manifest file `package.json` at the root of the extension directory structure."

### Strong false positive rejected, not counted

`.vscode/extensions.json` **does** satisfy `token_well_formed(..., "VS Code")`. But `census-fetch/vscode-market.md:253-268` describes workspace extension recommendations, including a `recommendations` array, not a plugin manifest. I did not promote a grammar-shaped configuration file into a manifest. The conventional VS Code extension's actual manifest is `package.json` (`census-fetch/vscode-extension-manifest.md:6`), which fails the frozen filename rule. No new `.vscode`-named plugin manifest was established.

### Observed grammar probe

Executed only in my pinned sandbox:

`timeout 30s python3 -B -c '<probe importing verifiers/check_plugin_manifests.py; apply token_well_formed, foreign_marker, base_url_keys and found_on_page to the fetched bytes>'`

Observed output, exit 0:

```text
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
Claude Code '.claude-plugin/plugin.json' well_formed=True foreign=None literal_on_page=True base_url=False
Codex '.codex-plugin/plugin.json' well_formed=True foreign=None literal_on_page=True base_url=False
VS Code '.plugin/plugin.json' well_formed=True foreign=None literal_on_page=True base_url=False
Copilot CLI '.github/plugin/plugin.json' well_formed=True foreign=None literal_on_page=True base_url=True
Gemini CLI 'gemini-extension.json' well_formed=True foreign=None literal_on_page=True base_url=False
Cursor '.cursor-plugin/plugin.json' well_formed=True foreign=None literal_on_page=True base_url=False
opencode 'package.json' well_formed=False foreign=None literal_on_page=True base_url=False
VS Code contiguous quote words 11 extra_plugin_word True found_on_fetched_page True
VS Code quote byte-exact True
boundary case VS Code '.vscode/extensions.json' well_formed=True
boundary case VS Code 'plugin.json' well_formed=False
boundary case opencode '.opencode/plugins/' well_formed=False
boundary case opencode '.opencode/package.json' well_formed=False
```

The essential probe is reproducible without writing a file:

```sh
timeout 30s python3 -B - <<'PY'
import importlib.util, pathlib, subprocess
p=pathlib.Path('verifiers/check_plugin_manifests.py')
s=importlib.util.spec_from_file_location('frozen_manifest',p)
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
b=subprocess.run(['timeout','15s','git','--no-optional-locks','show',m.BASE+':corpus/SOURCES.md'],capture_output=True,text=True,check=True).stdout
keys=m.base_url_keys(b)
for client,token,url in [
 ('VS Code','.plugin/plugin.json','https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md'),
 ('Copilot CLI','.github/plugin/plugin.json','https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md')]:
 print(client,m.token_well_formed(token,client),m.foreign_marker(client,token),m.url_key(url) in keys)
q='| Claude | `.claude-plugin/plugin.json` |\n| Legacy OpenPlugin | `.plugin/plugin.json` |'
page=pathlib.Path('census-fetch/vscode.md').read_text()
print('quote words',len(q.replace('`','').split()),'found',m.found_on_page(page,q,'.plugin/plugin.json'))
PY
```

## 2. Q45 can fail on the old plan, but not honestly as `5 > 4` under the token-only census

`plans/round-57.md:31-33,119-122` freezes F>=5/G>=3. The plan has no pre-freeze census, census command, census receipt, independent census-seat record or margin. Q45 was added afterward (`corpus/QUALITY.md:56`). A prospective check can reject that actual omission. It cannot honestly prove a token-only population of four: the independently found supported-path population is six, and `5 <= 6` is true.

**Exact proposed round-58 record check:** after the independent seat has reviewed the full source/guard census, put these literal field labels before `## Claims` in the plan: `C1 reachable population`, `C1 target margin`, `C1 census command`, `C1 census receipt`, `C1 census seat`. Population must be the jointly eligible count for the declared row-selection policy, not merely the number of strings matching the regex. The receipt must document source eligibility, exclusions, row rule, distinct-token/new-ground feasibility, and pre-freeze provenance. The executable check below checks recorded presence, arithmetic and receipt existence; it deliberately does not pretend that record presence verifies those semantic facts.

Run this same command on `plans/round-58.md` before freeze. For the observed replay, the last argument was `plans/round-57.md`:

```sh
timeout 10s python3 -B - plans/round-58.md <<'PY'
import pathlib,re,sys
p=pathlib.Path(sys.argv[1]); text=p.read_text()
claim=re.search(r'with F\s*≥\s*(\d+)\s+and G\s*≥\s*(\d+)',text)
if not claim:
    print('Q45 FAIL: missing C1 target sentence'); sys.exit(1)
target=int(claim[1]); prefix=text.split('## Claims',1)[0]
patterns={
 'population':r'^C1 reachable population: (\d+) of 7$',
 'margin':r'^C1 target margin: (\d+) - (\d+) = (\d+)$',
 'command':r'^C1 census command: `([^`]+)`$',
 'receipt':r'^C1 census receipt: `([^`]+)`$',
 'seat':r'^C1 census seat: (.+); writes no content$'}
record={k:re.search(v,prefix,re.M) for k,v in patterns.items()}
missing=[k for k,v in record.items() if not v]
if missing:
    print('Q45 FAIL: no complete pre-Claims C1 census record; missing '+', '.join(missing)+'; frozen target F>='+str(target)); sys.exit(1)
pop=int(record['population'][1]); a,b,margin=map(int,record['margin'].groups())
if not 0<=target<=pop<=7 or (a,b,margin)!=(pop,target,pop-target):
    print('Q45 FAIL: target/margin inconsistent with reachable census'); sys.exit(1)
receipt=p.parent.parent/record['receipt'][1]
if not receipt.is_file():
    print('Q45 FAIL: missing census receipt '+str(receipt)); sys.exit(1)
print('Q45 record OK: target '+str(target)+' <= reachable '+str(pop)+'; margin '+str(margin)+'; review receipt for pre-freeze provenance and full frozen guards')
PY
```

Executed the identical Python body via `timeout 10s python3 -B -c <body> plans/round-57.md`, in the pinned sandbox. Observed:

```text
Q45 FAIL: no complete pre-Claims C1 census record; missing population, margin, command, receipt, seat; frozen target F>=5
Q45 check exit 1
```

This demonstrates the **missing-census failure arm on round 57**, not a retrospectively fabricated numeric failure, and does not assert that a round-58 plan exists or passed. The frozen counter is not changed. A record-only check can be gamed with false attestations; independent receipt review remains necessary. In particular, counting Copilot's base S028 as eligible or assigning `.plugin/plugin.json` to two clients would overstate joint reachability (base-URL guard and E5 duplicate-token disqualification).

## 3. Smallest safe corrections, exact old → new text

These are proposed text replacements for the L1, not edits performed by this seat. They preserve the measured MISS and M62's stable identifier while correcting the causal claim.

### M62 (`corpus/lessons/round-57.md:92-100`)

Old:

```text
- **M62 `target-above-reachable-population`** (the mined mistake) · C1's frozen target was F ≥ 5 of seven clients
  (`plans/round-57.md` § Claims), set before any census of how many clients document an own-format plugin manifest; the
  honest count is 4 (Claude Code, Codex, Gemini CLI, Cursor), so the landed table scores `plugin manifests found on the
  live page 4 of 4; new ground 4`, exit 1 (`.ufo/waves/round-57/C1-measure.txt`). The zero margin was reported
  during the build wave (`CriticAxisFit`, `ScoutPluginMcp`, `CriticC1Rows`, ~04:50–04:54Z), after the target was frozen · captured-by: none (the
  pre-freeze control wave asks whether a do-nothing control reaches the target, not whether honest content can) ·
  fix: Q45 — before freezing a per-client target, a seat that writes no content counts the clients whose own
  documentation states the claimed form under the counter's token rule, and the plan records that census with the target
  set at or below it; not yet shown able to fail (no round-58 plan exists).
```

New:

```text
- **M62 `target-above-reachable-population`** (historical label; corrected diagnosis: missing pre-freeze census and
  late row-rule narrowing) · C1 froze F ≥ 5 of seven clients before a census and before the own-format-first row rule
  recorded in `corpus/knowledge/plugin-manifests-round57.md:14-20`. That later rule selected four counted clients;
  the landed table scores `plugin manifests found on the live page 4 of 4; new ground 4`, exit 1
  (`.ufo/waves/round-57/C1-measure.txt`), a MISS. Four is not a demonstrated ceiling under the frozen grammar:
  VS Code documents the supported Legacy OpenPlugin `.plugin/plugin.json` on new source S081, and Copilot CLI
  documents `.github/plugin/plugin.json` on base source S028 (the latter citation remains ineligible).
  Captured-by: none before freeze. Fix: Q45 — census the declared reader-facing form and row-selection rule under
  all frozen eligibility guards before freezing either rule or target. Shown able to fail: the record check in
  `.ufo/waves/round-57/a3/falsify/A3CriticTargetCensus.md` exits 1 on round 57's missing census; it does not prove
  that F ≥ 5 was unreachable. No round-58 plan is claimed to exist or to have passed.
```

### Q45 (`corpus/QUALITY.md:56`)

Old:

```text
| Q45 | Before a per-client (or per-item) target is frozen, a seat that writes no content counts the population whose own sources state the claimed form under the counter's token rule; the plan records that census and its command, and sets the target at or below it with the margin stated. | claim plans with per-client targets | M62 `target-above-reachable-population` (`corpus/lessons/round-57.md` § Mistakes) | — |
```

New:

```text
| Q45 | Before a per-client (or per-item) target is frozen, a seat that writes no content records a source-backed census for the declared reader-facing form and row-selection rule under all frozen counter eligibility guards, not token shape alone; freeze the row rule with the target. The plan records the census, reproducible command and receipt, exclusions and jointly reachable margin, and refuses freeze if the census is missing or the target exceeds it. | claim plans with per-client targets | M62 `target-above-reachable-population` (historical label; corrected diagnosis in `corpus/lessons/round-57.md` § Mistakes) | — |
```

**Disposition boundary:** fixing the inaccurate reachability explanation and making Q45 executable are fixable calibration defects. Choosing to lead with a legacy supported path rather than a client's default/own-format path is a reader-facing tradeoff, not an automatic improvement. Do not silently change that policy to turn this MISS into a HIT, lower the frozen target, or certify six full-guard clients from this report.

## 4. Current-source sweep and provenance

### Fetch method and successful capture receipts

All requests used ordinary curl, no browser or challenge bypass. For the initial captures the command form was `timeout 180s bash -c '<loop>'`, with each URL run as `curl -L --fail --max-time 35 --connect-timeout 10 --silent --show-error -o census-fetch/<file> -w 'HTTP %{http_code}; bytes %{size_download}; effective %{url_effective}\n' <URL>`, followed by `wc -c` and `sha256sum`. Later requests used the same ordinary GET with `--fail-with-body` and a 40 s curl / 50 s outer timeout. Every success below had HTTP 200, curl exit 0, requested URL equal to effective URL, and the recorded stored byte count equal to curl's byte count. UTC timestamps are verbatim `date -u` output.

| File under `census-fetch/` | URL | `date -u` | Bytes | SHA-256 |
|---|---|---|---:|---|
| claude.md | https://code.claude.com/docs/en/plugins-reference.md | Fri Oct 23 06:46:25 AM UTC 2026 | 42124 | f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e |
| codex.md | https://developers.openai.com/plugins/build/plugins.md | Fri Oct 23 06:46:25 AM UTC 2026 | 38036 | c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1 |
| gemini.md | https://geminicli.com/docs/extensions/reference.md | Fri Oct 23 06:46:25 AM UTC 2026 | 12022 | 8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72 |
| cursor.md | https://cursor.com/docs/plugins.md | Fri Oct 23 06:46:25 AM UTC 2026 | 20323 | 74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62 |
| vscode.md | https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference.md | Fri Oct 23 06:46:25 AM UTC 2026 | 21972 | d6e10328d582db6210fcccc453947d8140ff08a41c31170c4c90816578a44f9e |
| copilot-create.md | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md | Fri Oct 23 06:46:25 AM UTC 2026 | 7711 | c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64 |
| copilot-reference.md | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | Fri Oct 23 06:46:25 AM UTC 2026 | 47200 | d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0 |
| opencode.md (HTML bytes) | https://opencode.ai/docs/plugins/ | Fri Oct 23 06:46:25 AM UTC 2026 | 109777 | c7b687a4547ba6832eb69ac73acaf9de285267c633068f404a1e8dc41e1fdfe6 |
| vscode-use.md | https://code.visualstudio.com/docs/agent-customization/agent-plugins.md | Fri Oct 23 06:47:27 AM UTC 2026 | 16711 | b717e6f2bf05db2e161ffef8fe82d1002ccea452c7a45d91dc95d7505153757e |
| copilot-market.md | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace.md | Fri Oct 23 06:47:27 AM UTC 2026 | 4148 | af3bd6efe1aadaef2b6634f76d6dd6ec02892765cdc26369c5cb6903a8b4da91 |
| opencode-plain.md | https://opencode.ai/docs/plugins.md | Fri Oct 23 06:47:27 AM UTC 2026 | 9357 | c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e |
| opencode-tree.md (JSON bytes) | https://api.github.com/repos/anomalyco/opencode/git/trees/dev?recursive=1 | Fri Oct 23 06:47:28 AM UTC 2026 | 2971864 | 6aebf56e0a0d215939773d622b29a86a80dc06c8726d3d8da3bd188ed4ff51d9 |
| opencode-changelog.md | https://raw.githubusercontent.com/anomalyco/opencode/dev/CHANGELOG.md | Fri Oct 23 06:47:28 AM UTC 2026 | 50001 | 7c4cb74025c345d5a5df08195da5005674478055c6c804f25221f3bb931c519b |
| opencode-current-build.mdx | https://raw.githubusercontent.com/anomalyco/opencode/4d30794bcf4dccdcadbcb1f62bb35b4943a96426/services/www/src/docs/content/build/plugins/index.mdx | Fri Oct 23 06:50:37 AM UTC 2026 | 60780 | e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5 |
| opencode-current-top.mdx | https://raw.githubusercontent.com/anomalyco/opencode/4d30794bcf4dccdcadbcb1f62bb35b4943a96426/services/www/src/docs/content/plugins.mdx | Fri Oct 23 06:50:37 AM UTC 2026 | 4371 | 39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3 |
| vscode-market.md | https://code.visualstudio.com/docs/configure/extensions/extension-marketplace.md | Fri Oct 23 06:50:37 AM UTC 2026 | 28063 | 68f4a7daca3c9817002b714307ee199cdc92394ce9a049b703e09db449172fcd |
| vscode-extension-manifest.md | https://code.visualstudio.com/api/references/extension-manifest.md | Fri Oct 23 06:50:38 AM UTC 2026 | 23938 | 320c731e44339e974f90fc91441ef0c746f984d57dc8711c69982c3d36852d39 |

One rejected search URL: `https://docs.github.com/en/copilot/concepts/agents/about-plugins.md`, `date -u` `Fri Oct 23 06:46:25 AM UTC 2026`, HTTP 404, curl exit 22, download count 0; `--fail` saved no body/file, so no fetched-body digest exists and it supports no content claim.

### opencode negative sweep (Q30)

- **Current docs source tree:** `timeout 180s git clone --quiet --depth 1 --filter=blob:none --sparse --single-branch --branch dev https://github.com/anomalyco/opencode.git census-upstream-opencode && timeout 120s git -C census-upstream-opencode sparse-checkout set services/www/src/docs/content && timeout 10s git -C census-upstream-opencode rev-parse HEAD` exited 0 and printed upstream source revision `4d30794bcf4dccdcadbcb1f62bb35b4943a96426`. The independently fetched tree JSON identifies the same upstream revision at `census-fetch/opencode-tree.md:2`. This is an upstream source revision, not a sandbox-created commit.
- **Release notes/changelog:** opened the 50,001-byte current root `CHANGELOG.md` above. Specialized case-insensitive search for `plugin.json|extension.json|manifest|package.json` returned `No matches found`.
- **Entire current docs source tree plus changelog:** specialized case-insensitive search with `([A-Za-z0-9_.*-]+/)*[A-Za-z0-9_.*-]*(plugin|extension)[A-Za-z0-9_.*-]*\.json` returned `No matches found`. A separate `manifest` search found the generic `package.json` label at `build/plugins/index.mdx:1770-1773` and an unrelated troubleshooting `manifest.json`, not a qualifying plugin filename.
- **Lane corpus at the pinned revision:** specialized case-insensitive searches for opencode plugin/extension JSON paths and `.opencode/...json` returned `No matches found`. Generic plugin-manifest discussion was opened in `corpus/knowledge/plugin-manifests-round57.md` and the corpus was also searched for `.plugin/plugin.json`/`.github/plugin/plugin.json`.
- These three legs support **no eligible path found in this bounded current-source sweep**, not a universal statement about all possible future or undocumented opencode formats. The upstream current-source build/top guides were separately curl-fetched with full receipts above; served V1 and current V2 bytes and line numbers are not mixed.

### Other search/operation limits

- Web searches covered Copilot `.github/plugin/plugin.json`, VS Code `plugin.json`/`.vscode`/`extension.json`/`vscode-plugin`, and opencode `plugin.json`/named manifest variants. Search summaries were discovery only, never evidence; the conclusions above use fetched vendor bytes.
- Copilot creation and marketplace guides contained no additional qualifying named path in the inspected captures. This is not a claim that all Copilot documentation is silent. The known legacy reference is positive evidence, but base-URL barred.
- An attempted async source clone was refused by the tool's background-job cap before execution. Retrying synchronously obtained the opencode source above. No process outside this seat was killed.
- VS Code source clone command (same bounded clone/sparse-checkout shape, `docs release-notes`) ended exit 124 after its 120 s sparse-checkout cap. A read-only `timeout 10s git --no-optional-locks -C census-upstream-vscode rev-parse HEAD` subsequently exited 0, identifying upstream source revision `a03090533810eb02e5b9a2a650e2a3df32192b42`. Available docs confirmed the Legacy OpenPlugin row (`docs/agents/reference/agent-plugin-reference.md:116`); the available release notes mentioned `.vscode/extensions.json` as recommendations. This partial source checkout is **not** used to certify absence of every possible VS Code-named manifest. The decisive positive evidence is the complete HTTP-200 vendor documentation fetch.
- No full C1 rerun, runtime plugin load, builds, tests or lint checks were performed by this scoped critic. The exercised checks are only the frozen grammar/page-presence probe and the exact Q45 record-check failure above. No tool was installed or upgraded.
