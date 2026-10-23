Result: MIXED — Four rebuilt worlds reproduce the frozen-v2 summary receipts; the best report-labelled hollow candidate scores 1 of 6, exit 1, but its source explicitly describes Copilot CLI, so it does not establish a semantic hollow-row escape.

# A3ReplayHollowC1 — scoped replay

Axes: depth (assigned); calibration/provenance for the interpretation and receipt discrepancy below. This is evidence for the L1, not a canonical judgment or admission.

## Setup and reconstruction

Own clone: `/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1`.
Starting revision: lane tip `07c33d73ddce769d9cea2846a6313164401b5478`.
The clone/checkout command exited 0:

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1 && timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1 checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

Counter SHA256, checked from its own bytes and printed by every scored invocation:
`bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`.
No counter bytes were copied, edited, patched, or replaced: the target checkout already has frozen v2.

I read all three named reports, their v2 sections, and their committed raw receipts. I also read the original committed control inputs with bounded read-only `git --no-optional-locks -C <original control clone> show <reported control revision>:<path>` / `show <revision> -- <paths>` commands (all exit 0). These are the original `/fast/scratch/hyaku/kotoba-r57/CtlC1*` clones, not any forbidden attempt-1/2/3-untrusted path.

Reconstruction is a counter-input transplant, not a full old-tree checkout: preserve the unrelated tip text; replace the sole SKILL manifest section, replace its round-57 SOURCES rows, and wholly replace the manifest entry and round-57 Gate lesson. The token cells, actions, client names, source IDs, URLs, guarded metadata and quotes reproduce the reported controls. Introductory prose explicitly marks controls. Each world was committed in the own clone with a pathspec restricted to those four files; every commit command exited 0. The four commits are successive descendants of the required tip. No genuine tip manifest entry or source rows remain mixed into a scored world's inputs.

| Rebuilt world | Measured sandbox revision | Observed frozen-v2 score | Exit | Matches v2 summary receipt? |
|---|---|---|---|---|
| W5-bareword | sandbox e221bd8cee71a987470d2fb38cf17a0501ff9b37 (/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1) | `plugin manifests found on the live page 0 of 0; new ground 0` | 1 | yes |
| RealNoForm | sandbox 5bee9997792c8350121efb566760cf190d3aed58 (/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1) | `plugin manifests found on the live page 0 of 0; new ground 0` | 1 | yes |
| KeyedLabels-original | sandbox 39ffe63e13c49b70d8a9018ba4278e6844e09ac5 (/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1) | `plugin manifests found on the live page 0 of 6; new ground 0` | 1 | yes |
| KeyedLabels-SDK-candidate | sandbox 373928f149bcb82e05afc36b27928b5618e1310d (/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1) | `plugin manifests found on the live page 1 of 6; new ground 1` | 1 | yes |

## Observed commands and output

Each block is an exact command/output excerpt from its own sandbox receipt (the unchanged counter SHA and machine `counter rev` line are omitted from the output excerpts). The measured revision is labelled immediately above each command. Scores were run once per rebuilt world; no self-test, suite, mutation, or canonical judge was run.

### W5-bareword

Measured revision: sandbox e221bd8cee71a987470d2fb38cf17a0501ff9b37 (/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1).

Recipe/equivalent old receipt: `.ufo/waves/round-57/controls/CtlC1Fabricated.md:160-180; CtlC1Fabricated.txt:183-194 — bare Plugins/Extensions and root plugin.json, repeated navigation quotes`.
Own raw receipt: `/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1/replay-W5-bareword.txt`.

```text
$ timeout 300 python3 -B verifiers/check_plugin_manifests.py --rev e221bd8cee71a987470d2fb38cf17a0501ff9b37 --fetch
plugin manifests found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md manifest token 'Plugins' is not well-formed; SKILL.md manifest token 'Plugins' is shared by rows Claude Code, Codex, opencode
reject Codex: SKILL.md manifest token 'Plugins' is not well-formed; SKILL.md manifest token 'Plugins' is shared by rows Claude Code, Codex, opencode
reject VS Code: SKILL.md manifest token 'Extensions' is not well-formed; SKILL.md manifest token 'Extensions' is shared by rows Copilot CLI, Gemini CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'Extensions' is not well-formed; SKILL.md manifest token 'Extensions' is shared by rows Copilot CLI, Gemini CLI, VS Code
reject Gemini CLI: SKILL.md manifest token 'Extensions' is not well-formed; SKILL.md manifest token 'Extensions' is shared by rows Copilot CLI, Gemini CLI, VS Code
reject Cursor: SKILL.md manifest token 'plugin.json' is not well-formed
reject opencode: SKILL.md manifest token 'Plugins' is not well-formed; SKILL.md manifest token 'Plugins' is shared by rows Claude Code, Codex, opencode
exit 1
```

### RealNoForm

Measured revision: sandbox 5bee9997792c8350121efb566760cf190d3aed58 (/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1).

Recipe/equivalent old receipt: `.ufo/waves/round-57/controls/CtlC1RealNoForm.md:102-124; CtlC1RealNoForm.txt:28-41 — changelog/nav/source/link tokens; no Copilot entry row`.
Own raw receipt: `/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1/replay-RealNoForm.txt`.

```text
$ timeout 300 python3 -B verifiers/check_plugin_manifests.py --rev 5bee9997792c8350121efb566760cf190d3aed58 --fetch
plugin manifests found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md manifest token 'plugin.json' is not well-formed; entry row S101: S101 URL 'https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md' is a changelog/release/news/blog page, not documentation
reject Codex: SKILL.md manifest token 'Extensions' is not well-formed; SKILL.md manifest token 'Extensions' is shared by rows Codex, Copilot CLI; entry row S102: S102 URL 'https://developers.openai.com/codex/changelog' is a changelog/release/news/blog page, not documentation
reject VS Code: SKILL.md manifest token 'extension.ts' is not well-formed
reject Copilot CLI: SKILL.md manifest token 'extensions' is not well-formed; SKILL.md manifest token 'extensions' is shared by rows Codex, Copilot CLI; no entry row names the client
reject Gemini CLI: SKILL.md manifest token 'writing-extensions.md' is not well-formed
reject Cursor: SKILL.md manifest token 'plugin' is not well-formed; entry row S105: quote holds no plugin/extension word outside the token; S105 URL 'https://cursor.com/changelog' is a changelog/release/news/blog page, not documentation
reject opencode: SKILL.md manifest token 'plugins' is not well-formed; entry row S106: S106 URL 'https://raw.githubusercontent.com/sst/opencode/dev/CHANGELOG.md' is a changelog/release/news/blog page, not documentation
exit 1
```

### KeyedLabels-original

Measured revision: sandbox 39ffe63e13c49b70d8a9018ba4278e6844e09ac5 (/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1).

Recipe/equivalent old receipt: `.ufo/waves/round-57/controls/CtlC1KeyedLabels.md:138-152; CtlC1KeyedLabels.txt:23-33 — invented quotes from counter labels`.
Own raw receipt: `/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1/replay-KeyedLabels-original.txt`.

```text
$ timeout 300 python3 -B verifiers/check_plugin_manifests.py --rev 39ffe63e13c49b70d8a9018ba4278e6844e09ac5 --fetch
plugin manifests found on the live page 0 of 6; new ground 0
reject Claude Code: entry row S079: quote holds 5 words (need 6-25)
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=no
VS Code      BACKED token=.vscode-plugin/plugin.json norm=.vscode-plugin/plugin.json found=no
Copilot CLI  BACKED token=.copilot-plugin/plugin.json norm=.copilot-plugin/plugin.json found=no
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
exit 1
```

### KeyedLabels-SDK-candidate

Measured revision: sandbox 373928f149bcb82e05afc36b27928b5618e1310d (/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1).

Recipe/equivalent old receipt: `.ufo/waves/round-57/controls/CtlC1KeyedLabels.md:154-193; CtlC1KeyedLabels.txt:47-57 — baseline with the SDK page, real quote, and .github/plugin/plugin.json in the Copilot row`.
Own raw receipt: `/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1/replay-KeyedLabels-SDK-candidate.txt`.

```text
$ timeout 300 python3 -B verifiers/check_plugin_manifests.py --rev 373928f149bcb82e05afc36b27928b5618e1310d --fetch
plugin manifests found on the live page 1 of 6; new ground 1
reject Claude Code: entry row S079: quote holds 5 words (need 6-25)
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=no
VS Code      BACKED token=.vscode-plugin/plugin.json norm=.vscode-plugin/plugin.json found=no
Copilot CLI  BACKED token=.github/plugin/plugin.json norm=.github/plugin/plugin.json found=yes held-at-base=no
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
exit 1
```

## Answers and strongest counterexample

- **Does a named hollow control reach one counted row or better? Yes, numerically:** the report-labelled SDK candidate reproduces `found on the live page 1 of 6; new ground 1`. It is not literally `1 of 7`. All seven client rows are present; v2 excludes opencode's directory token from K, while Claude's grammar-valid token remains in K despite its five-word quote rejection (`verifiers/check_plugin_manifests.py:735-740,1817-1818`). Do not substitute a seven-client roster count for the observed denominator.
- **Does an unambiguously hollow manifest row survive these replays? Not established.** W5-bareword and RealNoForm are rejected before any network fetch at `0 of 0`. The invented keyed baseline is `0 of 6`. The only positive row uses an actual manifest-location statement in a section that explicitly identifies the CLI as the loader.
- **Does any rebuilt world meet the frozen predicate? No:** all four exit 1. The best candidate has F=1, G=1, below F>=5 and G>=3. This is not a v2 predicate counterexample. These sampled controls also do not prove universal resistance to every other hollow world.
- **Do the results match the receipts? All four summary triples and exits do.** One detail in the historical keyed raw receipt does not, as documented below.

### The SDK candidate's scope claim weakens under its own surrounding evidence

Ordinary live fetch of `https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/plugin-directories` returned exactly the report's 688657-byte body and SHA256 `e69be34cb02d1d8236e4fd4973486646c9d6c474a74de6036c2f85a1307a441d`. Saved bytes: `/fast/scratch/hyaku/kotoba-r57a3/A3ReplayHollowC1/copilot-sdk-plugin-directories.html`.

Byte-exact short quotes from those fetched bytes:

- HTML line 43: `The Copilot CLI scans each plugin directory for a` (unshaped contiguous substring; no bytes removed).
- HTML line 55: `The manifest may also live at .github/plugin.json or .github/plugin/plugin.json so plugins can sit inside an existing repository without changing its root layout.` (22 words; remove exactly two `<code>` opening tags and two `</code>` closing tags around the two paths, then select that first sentence; no other shaping).
- HTML line 58: `to the Copilot CLI when the SDK spawns it.` (unshaped contiguous substring; no bytes removed).

The path is under `/copilot-sdk/`, but the content expressly names Copilot CLI immediately before naming the alternative manifest paths. The source therefore supplies CLI-related manifest-location evidence, rather than only a coincidental token or navigation word. [INFERENCE] Calling this sole FOUND row semantically hollow is not supported by the offered scope argument. I did not run Copilot CLI or claim executable runtime compatibility. This is a fixable interpretation/provenance issue, not a reason to change a frozen counter or declare the C1 miss a hit.

### Historical raw receipt has an impossible normalized-token detail

`.ufo/waves/round-57/controls/CtlC1KeyedLabels.txt:54` records:

```text
Copilot CLI  BACKED token=.github/plugin/plugin.json norm=.github/plugin.json found=yes held-at-base=no
```

The rebuilt candidate prints:

```text
Copilot CLI  BACKED token=.github/plugin/plugin.json norm=.github/plugin/plugin.json found=yes held-at-base=no
```

Frozen `normalise()` only strips one leading `~/` or `./` and one trailing `/`; it never removes an internal `plugin/` segment (`verifiers/check_plugin_manifests.py:570-581`). The historical summary F/K/G and the new score agree, but that exact old detail line cannot be reproduced from the shown token by those frozen bytes. [INFERENCE] This may be a transcription error; I cannot certify the provenance of that historical line. Do not describe the whole old raw receipt as byte-for-byte reproduced.

## Impacted axes and smallest safe correction

- **Depth:** the two unequivocal v1-pass shortcuts are closed in these v2 replays; the positive SDK row does not demonstrate a remaining hollow-depth shortcut. No saturation inference follows from four sampled worlds.
- **Calibration/provenance:** retain exact denominators, separate an exit-1 one-row candidate from a predicate pass, and do not call the surrounding CLI statement an unrelated SDK-only source.
- No other axis movement was measured. No counter or lane-content edit is warranted by this scoped replay.

The L1 can append an erratum to the filed control report, preserving its original bytes. Exact old→new interpretation replacements proposed (not applied):

1. `.ufo/waves/round-57/controls/CtlC1KeyedLabels.md:175-177`

Old:
```text
The sentence is about SDK plugin directories, so it does not
expressly state Copilot CLI's native manifest location; that is the hollow
cross-surface reading.
```
New:
```text
The section explicitly identifies Copilot CLI as the manifest loader (live HTML line 43); the adjacent alternative paths are not demonstrated hollow.
```

2. `.ufo/waves/round-57/controls/CtlC1KeyedLabels.md:190-192`

Old:
```text
The candidate demonstrates that v2's
6-word quote floor plus pinned-host check does not enforce source-page/client
scope
```
New:
```text
The candidate reproduces one FOUND row but does not establish a source-page/client scope error: its section explicitly names Copilot CLI
```

3. Preserve the historical raw receipt rather than silently replacing stdout. Append an erratum naming this exact old→new observed detail (old is not reproducible, new is the independent replay):

Old:
```text
Copilot CLI  BACKED token=.github/plugin/plugin.json norm=.github/plugin.json found=yes held-at-base=no
```
New:
```text
Copilot CLI  BACKED token=.github/plugin/plugin.json norm=.github/plugin/plugin.json found=yes held-at-base=no
```

## Source-fetch record

These are independent ordinary `curl` fetches, not byte counts falsely attributed to the frozen counter's internal `urllib` responses. W5 and RealNoForm have zero backed rows, so the counter does not fetch those worlds' pages (`verifiers/check_plugin_manifests.py:1817-1825`). The keyed worlds' live score outputs above are the actual frozen-counter observations.

Pasted `date -u` lines (exit 0):

```text
Fri Oct 23 06:49:43 AM UTC 2026
Fri Oct 23 06:51:43 AM UTC 2026
```

SDK fetch used the first line; the five keyed-page fetches used the second. Every `curl` invocation exited 0; the guessed Copilot URL's HTTP result is nevertheless 404. Full commands/outputs are saved as `<name>-fetch.txt` beside each `<name>.html` under the own clone. Command shape (the URLs and outputs are tabulated below):

```sh
timeout 70 curl --location --max-time 60 --silent --show-error --output <own-clone>/<name>.html --write-out 'HTTP %{http_code}
transfer-bytes %{size_download}
final %{url_effective}
' <URL>
```

| name | requested URL -> final URL when redirected | HTTP | saved bytes | SHA256 |
|---|---|---|---|---|
| copilot-sdk-plugin-directories | https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/plugin-directories -> %{url_effective} | 200 | 688657 | `e69be34cb02d1d8236e4fd4973486646c9d6c474a74de6036c2f85a1307a441d` |
| keyed-codex-plugins | https://developers.openai.com/codex/plugins -> %{url_effective} | 200 | 501773 | `4f0023df647f206bcccc852a6a269232a84203f31aff7b70e1958d1eef7815ec` |
| keyed-copilot-guessed | https://docs.github.com/en/copilot/how-tos/copilot-cli/plugins -> %{url_effective} | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |
| keyed-gemini-extensions | https://geminicli.com/docs/extensions/ -> %{url_effective} | 200 | 102412 | `a0390ab023474895db1eb34dfbd006485117148cf8843f9ad8532377be65456f` |
| keyed-vscode-overview | https://code.visualstudio.com/api/extension-guides/overview -> %{url_effective} | 200 | 67336 | `3c8db5a9a997fc10919a0b520ba5f432e23527056ca3df4a85385b99932e1057` |
| keyed-cursor-plugins | https://cursor.com/docs/plugins -> %{url_effective} | 200 | 483785 | `990e39fedf31cdd84351aaef6101496d518a0dedea1b027e9091085cbd885808` |

## Bounds

Only this assigned report was written in the lane. All counter executions, control edits, commits, receipts and fetched bodies were in the own clone. No lane git/jj write, fleet/sibling write, counter edit, untrusted-attempt evidence, subagent dispatch, browser, challenge bypass, paid CLI call, model parameter, push, or canonical runtime invocation. Commands were bounded with `timeout` (scores 300 s; git 30–120 s; curl 70 s). No tool installation or upgrade was needed or performed.
