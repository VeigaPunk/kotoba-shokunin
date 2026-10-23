Result: DONE — CtlAllFalse: S 7 of 7; F 0 of 7; G 0; exit 1; predicate NOT MET

## Control and expected detector

- Control: `CtlAllFalse`, one all-false/fabricated-source world. Axes: isolated bytes, offline saturation, live-source discrimination, exact restoration.
- Measured world: sandbox bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc (/fast/scratch/hyaku/kotoba-r59/CtlAllFalse). The restoration commit remains HEAD; the measured world remains in its history.
- Frozen input: `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`; no lane source or counter bytes were edited.
- Read frozen constants directly at `verifiers/check_hook_files.py:253-254`: `TARGET = 4`, `NEW_TARGET = 5`.
- Expected detector: offline backing accepts the seven internally consistent fabricated records, while `--fetch` rejects invented source URLs; the predicate requires both F >= 4 and G >= 5 (`verifiers/check_hook_files.py:208-220,1245-1251`).
- Observed: S = 7 of K = 7, F = 0 of K = 7, G = 0, fetch exit 1. The offline run also exits 1 by definition. G is computed only over FOUND clients, so G = 0 does not establish anything about the invented tokens' base-tree novelty (`verifiers/check_hook_files.py:182-194`).

C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET

**Mutation verdict: INCONCLUSIVE, not a killed mutant.** The pristine frozen tree already returns predicate exit 1 (S/F/G all zero). This probe therefore does not supply a passing-pristine/failing-mutated kill. Its concrete control result is rejection of this fabricated world by the full live predicate, with acceptance of every offline conjunct (S = 7). No global C1 verdict or contract change is asserted.

The freeze addendum at `plans/round-59.md:93-98` was read: the Events conjunct proves printed identifiers, not hook-event semantics. Invented identifiers on fabricated snapshots satisfy that offline conjunct here; no live documentation supports them.

## Frozen counter identity

Lane read-only identity command (exit 0):
```text
$ timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 67b68e0f9a0c48e5aa5ced63e6117cfca69da491:verifiers/check_hook_files.py | sha256sum
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -
```

From the sandbox clone, the counter actually executed (exit 0):
```text
$ timeout 10 sha256sum verifiers/check_hook_files.py
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
```

## Mutation bytes and committed evidence

The defect is fabricated provenance, not altered verifier logic. Seven new IDs S096–S102 use invented URLs on each client's pinned host, invented valid hook tokens, 11–12-word invented quotes containing the token and `hooks`, and two invented CamelCase events per client. The snapshot digest is self-consistently written into its fabricated SOURCES row, including the deliberately untrue `fetched` label. These records are sandbox negative-control data, never admitted client facts.

Construction reuses the frozen self-test's exact `page_for` helper and `src_row` template (`verifiers/check_hook_files.py:1857-1882`), extracted without running the self-test or changing its file. Each snapshot consists only of the quote paragraph and the two event identifiers in code tags.

Evidence below refers to the measured world sandbox bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc (/fast/scratch/hyaku/kotoba-r59/CtlAllFalse):

- `SKILL.md:121-131`: exact Hook files heading, first-table header, seven rows, and six-word action cells.
- `corpus/knowledge/hook-files-round59.md:5-13`: entry header, same tokens, one new source ID per client, and the invented quotes.
- `corpus/SOURCES.md:108-114`: seven docs/A/mined/2026-10-23 rows with full snapshot sha256 pins.
- `corpus/lessons/round-59.md:3-16`: Gate section and identical invented quotes.
- `.ufo/waves/round-59/snapshots/S096.page:1` through `S102.page:1`: exact fabricated page bytes.

| Source | Client | Invented token | Invented events | Quote words | Snapshot bytes |
|---|---|---|---|---:|---:|
| S096 | Claude Code | `.claude/hookfile.json` | `ClaudeFabricatedBegin`, `ClaudeFabricatedEnd` | 12 | 170 |
| S097 | Codex | `~/.codex/hookset.json` | `CodexFabricatedBegin`, `CodexFabricatedEnd` | 11 | 162 |
| S098 | VS Code | `.vscode/hookset.json` | `VscodeFabricatedBegin`, `VscodeFabricatedEnd` | 12 | 165 |
| S099 | Copilot CLI | `.copilot/hookset.json` | `CopilotFabricatedBegin`, `CopilotFabricatedEnd` | 12 | 172 |
| S100 | Gemini CLI | `.gemini/hookset.json` | `GeminiFabricatedBegin`, `GeminiFabricatedEnd` | 12 | 168 |
| S101 | Cursor | `.cursor/hookset.json` | `CursorFabricatedBegin`, `CursorFabricatedEnd` | 11 | 164 |
| S102 | opencode | `.opencode/hookset.json` | `OpencodeFabricatedBegin`, `OpencodeFabricatedEnd` | 11 | 172 |

Invented quote substrings, byte-exact on line 1 of the corresponding fabricated snapshot; no Markdown bytes stripped:

- `S096.page:1`: Claude Code runs automatic hooks from the .claude/hookfile.json file during every session
- `S097.page:1`: Codex runs automatic hooks from the ~/.codex/hookset.json file during every session
- `S098.page:1`: VS Code runs automatic hooks from the .vscode/hookset.json file during every session
- `S099.page:1`: Copilot CLI runs automatic hooks from the .copilot/hookset.json file during every session
- `S100.page:1`: Gemini CLI runs automatic hooks from the .gemini/hookset.json file during every session
- `S101.page:1`: Cursor runs automatic hooks from the .cursor/hookset.json file during every session
- `S102.page:1`: opencode runs automatic hooks from the .opencode/hookset.json file during every session

## Exact detector receipts

All commands ran from `/fast/scratch/hyaku/kotoba-r59/CtlAllFalse`, with GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE absent from the subprocess environment. Each detector is capped at 900 seconds. Only ordinary curl traffic from the unchanged counter was used; no challenge was bypassed.

The passive strace wrapper records subprocess stdout, not substituted network content. The enclosed scoring command is exactly the prescribed `timeout 900 python3 -B verifiers/check_hook_files.py --rev <sandbox-commit> --fetch`.

The first traced fetch used `-s 0`, which elided payloads. Its actual full counter stdout and exit are retained below, but its response-body hashes were not captured and are not claimed. A separate bounded receipt-capture run used `-s 10485760`; its full response fingerprints appear below. Each of the two fetch runs made at most three attempts per invented URL (six attempts per URL across both invocations); pristine/restored runs had no backed rows and made no page fetches.

### pristine-offline

frozen pristine revision 67b68e0f9a0c48e5aa5ced63e6117cfca69da491

```text
Fri Oct 23 09:22:59 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit 1
```

### pristine-fetch

frozen pristine revision 67b68e0f9a0c48e5aa5ced63e6117cfca69da491

```text
Fri Oct 23 09:22:59 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491 --fetch
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit 1
```

### mutant-offline

sandbox bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc (/fast/scratch/hyaku/kotoba-r59/CtlAllFalse)

```text
Fri Oct 23 09:24:24 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc
hook files backed on committed snapshots 7 of 7; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc
stderr: (empty)
exit 1
```

### mutant-fetch

sandbox bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc (/fast/scratch/hyaku/kotoba-r59/CtlAllFalse)

```text
Fri Oct 23 09:24:24 AM UTC 2026
$ timeout 900 strace -ff -ttt -s 0 -xx -e trace=execve,write -o /fast/scratch/hyaku/kotoba-r59/CtlAllFalse/CtlAllFalse-mutant-fetch.trace timeout 900 python3 -B verifiers/check_hook_files.py --rev bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc --fetch
hook files backed on committed snapshots 7 of 7; found on the live page 0 of 7; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc
reject Claude Code: live fetch failed: HTTP 404 at https://code.claude.com/docs/en/hook-files-invented.md
reject Codex: live fetch failed: HTTP 404 at https://learn.chatgpt.com/docs/hook-files-invented.md
reject VS Code: live fetch failed: HTTP 404 at https://code.visualstudio.com/docs/agent-customization/hook-files-invented.md
reject Copilot CLI: live fetch failed: HTTP 404 at https://docs.github.com/en/copilot/hook-files-invented.md
reject Gemini CLI: live fetch failed: HTTP 404 at https://geminicli.com/docs/hook-files-invented.md
reject Cursor: live fetch failed: HTTP 404 at https://cursor.com/docs/hook-files-invented.md
reject opencode: live fetch failed: HTTP 404 at https://opencode.ai/docs/hook-files-invented.md
stderr: (empty)
exit 1
```

### restored-offline

sandbox f65870c55026656983e8aa4888de6fbd3e3badf8 (/fast/scratch/hyaku/kotoba-r59/CtlAllFalse)

```text
Fri Oct 23 09:25:45 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev f65870c55026656983e8aa4888de6fbd3e3badf8
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev f65870c55026656983e8aa4888de6fbd3e3badf8
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit 1
```

### restored-fetch

sandbox f65870c55026656983e8aa4888de6fbd3e3badf8 (/fast/scratch/hyaku/kotoba-r59/CtlAllFalse)

```text
Fri Oct 23 09:25:45 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev f65870c55026656983e8aa4888de6fbd3e3badf8 --fetch
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev f65870c55026656983e8aa4888de6fbd3e3badf8
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
stderr: (empty)
exit 1
```

### mutant-fetch-recorded

sandbox bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc (/fast/scratch/hyaku/kotoba-r59/CtlAllFalse)

```text
Fri Oct 23 09:26:33 AM UTC 2026
$ timeout 900 strace -ff -ttt -s 10485760 -xx -e trace=execve,write -o /fast/scratch/hyaku/kotoba-r59/CtlAllFalse/CtlAllFalse-mutant-fetch-recorded.trace timeout 900 python3 -B verifiers/check_hook_files.py --rev bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc --fetch
hook files backed on committed snapshots 7 of 7; found on the live page 0 of 7; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev bb43204d10abaec4e1b1a0ff358ba4de7f94b1cc
reject Claude Code: live fetch failed: HTTP 404 at https://code.claude.com/docs/en/hook-files-invented.md
reject Codex: live fetch failed: HTTP 404 at https://learn.chatgpt.com/docs/hook-files-invented.md
reject VS Code: live fetch failed: HTTP 404 at https://code.visualstudio.com/docs/agent-customization/hook-files-invented.md
reject Copilot CLI: live fetch failed: HTTP 404 at https://docs.github.com/en/copilot/hook-files-invented.md
reject Gemini CLI: live fetch failed: HTTP 404 at https://geminicli.com/docs/hook-files-invented.md
reject Cursor: live fetch failed: HTTP 404 at https://cursor.com/docs/hook-files-invented.md
reject opencode: live fetch failed: HTTP 404 at https://opencode.ai/docs/hook-files-invented.md
stderr: (empty)
exit 1
```

## Actual live-response evidence (receipt-capture run)

Access-start line from `date -u`:
```text
Fri Oct 23 09:26:33 AM UTC 2026
```

Per-attempt UTC times below are decoded from strace's epoch timestamp on the successful `/usr/bin/curl` exec. Status/effective URL come from curl's original write-out trailer. Body lengths and sha256 are over the exact concatenated successful stdout writes before that trailer. All writes were checked for non-truncation and equal requested/returned lengths. The 21 curl logs give exactly three attempts for each of the seven URLs.

| Source | Invented requested URL | Actual effective URL | HTTP | Body bytes | Actual body sha256 |
|---|---|---|---:|---:|---|
| S096 | https://code.claude.com/docs/en/hook-files-invented.md | https://code.claude.com/docs/en/hook-files-invented.md | 404 | 653 | `ef957ff8cd7b3e0cf2802a24e6379dbb5f7a9d30d4e98900f42f8d3977b8c3d4` |
| S097 | https://developers.openai.com/codex/hook-files-invented.md | https://learn.chatgpt.com/docs/hook-files-invented.md | 404 | 9 | `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31` |
| S098 | https://code.visualstudio.com/docs/agent-customization/hook-files-invented.md | https://code.visualstudio.com/docs/agent-customization/hook-files-invented.md | 404 | 9 | `0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5` |
| S099 | https://docs.github.com/en/copilot/hook-files-invented.md | https://docs.github.com/en/copilot/hook-files-invented.md | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |
| S100 | https://geminicli.com/docs/hook-files-invented.md | https://geminicli.com/docs/hook-files-invented.md | 404 | 31633 | `d716f45c4728be293f5af8e1011d0835170e12bbedd440dc362fd752c5a588ee` |
| S101 | https://cursor.com/docs/hook-files-invented.md | https://cursor.com/docs/hook-files-invented.md | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` |
| S102 | https://opencode.ai/docs/hook-files-invented.md | https://opencode.ai/docs/hook-files-invented.md | 404 | 111 | `4a6523706291aefaa5999f883a89e0997e2077b220be9900f16cb10c190b5d52` |

All three attempts for each row had the same observed status, effective URL, body length, and body hash. Per-attempt evidence:

| Source / attempt | UTC access start | Trace (scratch-relative) | exec line | stdout write lines |
|---|---|---|---:|---|
| S096 / 1 | 2026-10-23T09:26:33.925027Z | `CtlAllFalse-mutant-fetch-recorded.trace.19051` | 15 | 16, 17 |
| S096 / 2 | 2026-10-23T09:26:34.174393Z | `CtlAllFalse-mutant-fetch-recorded.trace.20806` | 15 | 16, 17 |
| S096 / 3 | 2026-10-23T09:26:34.585903Z | `CtlAllFalse-mutant-fetch-recorded.trace.23669` | 15 | 16, 17 |
| S097 / 1 | 2026-10-23T09:26:34.824240Z | `CtlAllFalse-mutant-fetch-recorded.trace.26869` | 15 | 16, 17 |
| S097 / 2 | 2026-10-23T09:26:35.066108Z | `CtlAllFalse-mutant-fetch-recorded.trace.30996` | 15 | 16, 17 |
| S097 / 3 | 2026-10-23T09:26:35.301966Z | `CtlAllFalse-mutant-fetch-recorded.trace.35397` | 15 | 16, 17 |
| S098 / 1 | 2026-10-23T09:26:35.548716Z | `CtlAllFalse-mutant-fetch-recorded.trace.40289` | 15 | 16, 17 |
| S098 / 2 | 2026-10-23T09:26:35.717711Z | `CtlAllFalse-mutant-fetch-recorded.trace.43320` | 15 | 16, 17 |
| S098 / 3 | 2026-10-23T09:26:35.880915Z | `CtlAllFalse-mutant-fetch-recorded.trace.46328` | 15 | 16, 17 |
| S099 / 1 | 2026-10-23T09:26:36.041998Z | `CtlAllFalse-mutant-fetch-recorded.trace.49426` | 15 | 16, 17 |
| S099 / 2 | 2026-10-23T09:26:36.083718Z | `CtlAllFalse-mutant-fetch-recorded.trace.49873` | 15 | 16, 17 |
| S099 / 3 | 2026-10-23T09:26:36.109114Z | `CtlAllFalse-mutant-fetch-recorded.trace.50120` | 15 | 16, 17 |
| S100 / 1 | 2026-10-23T09:26:36.129355Z | `CtlAllFalse-mutant-fetch-recorded.trace.50221` | 15 | 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| S100 / 2 | 2026-10-23T09:26:36.152045Z | `CtlAllFalse-mutant-fetch-recorded.trace.50346` | 15 | 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| S100 / 3 | 2026-10-23T09:26:36.177585Z | `CtlAllFalse-mutant-fetch-recorded.trace.50481` | 15 | 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| S101 / 1 | 2026-10-23T09:26:36.200762Z | `CtlAllFalse-mutant-fetch-recorded.trace.50600` | 15 | 16, 17 |
| S101 / 2 | 2026-10-23T09:26:36.418170Z | `CtlAllFalse-mutant-fetch-recorded.trace.51555` | 15 | 16, 17 |
| S101 / 3 | 2026-10-23T09:26:36.644221Z | `CtlAllFalse-mutant-fetch-recorded.trace.52164` | 15 | 16, 17 |
| S102 / 1 | 2026-10-23T09:26:36.860565Z | `CtlAllFalse-mutant-fetch-recorded.trace.52803` | 15 | 16, 17 |
| S102 / 2 | 2026-10-23T09:26:37.406019Z | `CtlAllFalse-mutant-fetch-recorded.trace.58949` | 15 | 16, 17 |
| S102 / 3 | 2026-10-23T09:26:37.939972Z | `CtlAllFalse-mutant-fetch-recorded.trace.67173` | 15 | 16, 17 |

Actual rejection-page quotes, each at most 25 words, with original body line numbers. No tags, Markdown, or other bytes were stripped. The actual body files are under this sandbox's `fetch-evidence/`, named by their full body hash. These are rejection-page observations, not assertions that any client lacks hooks.

`/fast/scratch/hyaku/kotoba-r59/CtlAllFalse/fetch-evidence/ef957ff8cd7b3e0cf2802a24e6379dbb5f7a9d30d4e98900f42f8d3977b8c3d4.body:6`
```text
# Page Not Found
```

`/fast/scratch/hyaku/kotoba-r59/CtlAllFalse/fetch-evidence/e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31.body:1`
```text
Not found
```

`/fast/scratch/hyaku/kotoba-r59/CtlAllFalse/fetch-evidence/0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5.body:1`
```text
Not Found
```

`/fast/scratch/hyaku/kotoba-r59/CtlAllFalse/fetch-evidence/979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522.body:1`
```text
<title>404 - GitHub Docs</title>
```

`/fast/scratch/hyaku/kotoba-r59/CtlAllFalse/fetch-evidence/d716f45c4728be293f5af8e1011d0835170e12bbedd440dc362fd752c5a588ee.body:1`
```text
<title>Page Not Found | Gemini CLI</title>
```

`/fast/scratch/hyaku/kotoba-r59/CtlAllFalse/fetch-evidence/4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1.body:1`
```text
# Page not found
```

`/fast/scratch/hyaku/kotoba-r59/CtlAllFalse/fetch-evidence/4a6523706291aefaa5999f883a89e0997e2077b220be9900f16cb10c190b5d52.body:1`
```text
{"status":404,"message":"Cannot find any route matching [GET] https://opencode.ai/docs/hook-files-invented.md"}
```

## Exact restoration evidence

Restoration: sandbox f65870c55026656983e8aa4888de6fbd3e3badf8 (/fast/scratch/hyaku/kotoba-r59/CtlAllFalse). All edited original files were written back from saved pristine bytes; the nine newly added control files were removed. The control remains inspectable via its measured commit. A rejected deletion edit with a mis-copied S098 anchor applied no changes; current anchors were reread and the subsequent removal succeeded.

Observed `git rev-parse` tree IDs (exit 0 for both commit sequences):
```text
pristine frozen tree: 304854156e782f0e4e8d9d08db88537567f94139
mutated control tree: eb2a3094290b2dcdab3c527a3f9d4ea5cd7077ab
restored tree:        304854156e782f0e4e8d9d08db88537567f94139
```

Before/after SHA-256 values (`ABSENT` denotes no file). Restored working bytes were directly hashed and matched every pristine value; pristine/restored bounded detector outputs are above.

| Path | Pristine sha256 | Mutated sha256 | Restored sha256 |
|---|---|---|---|
| `SKILL.md` | `2af0a1a9c09fd241ce0c146976f4996f08714f2413b55f283ef8fdf5a1111e07` | `e48128431cf0ee2dbbad25e8c1d2e72ca657af66c04d962a8f918d20d8e55d90` | `2af0a1a9c09fd241ce0c146976f4996f08714f2413b55f283ef8fdf5a1111e07` |
| `corpus/SOURCES.md` | `9656d5d9d882d24b3b71f5ce63f96a4fd2a1732d90576b56fd5763350374d150` | `85389ce01fdf6628efdd5909d814812ac0f19b884963036fdc83bd4e86a66fa7` | `9656d5d9d882d24b3b71f5ce63f96a4fd2a1732d90576b56fd5763350374d150` |
| `corpus/knowledge/hook-files-round59.md` | `ABSENT` | `e04ac4ec5ca53590d0917843b5850b701d800735fbd2ea0955a7e8239743e88b` | `ABSENT` |
| `corpus/lessons/round-59.md` | `ABSENT` | `a5923efcac988a771eea9d2f0fb6e2472c13930f9a2ef0d98371154c785813f2` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S096.page` | `ABSENT` | `b79c1e24aa52b53f33134ae8b73d226d202fcec137267f78a4a9a5b26d9ac015` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S097.page` | `ABSENT` | `3b5b839f4d12ed391b2eb1aedadd03849795dcca2dd632ce1b0a4134caebf0ed` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S098.page` | `ABSENT` | `86c6b1a28a01d28280edd2baddfb5acfdba7833e74ba2d600fc57b88241fddda` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S099.page` | `ABSENT` | `803de91bba7df75721c675fc4d9e6841e5bb99a5c8235ec71d363bff05b095d2` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S100.page` | `ABSENT` | `15cad6924bba65838d16e3b611836583f1f2aba674ab3896ffdafacdf6105ced` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S101.page` | `ABSENT` | `f4322417b71e01af4a4f0d3f26cc6158dccad0884158f42c69b4cfde357411c2` | `ABSENT` |
| `.ufo/waves/round-59/snapshots/S102.page` | `ABSENT` | `93d5a88d01f5bf28513bc8cab7b22cd56998d157d1d87396d6899316f7ec89b7` | `ABSENT` |
| `verifiers/check_hook_files.py` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` |

Counter remained unmodified throughout. The receipt-capture rerun read the already committed mutated world after restoration; it changed no tracked bytes. Only scratch receipt artifacts remain outside the restored tracked tree. No lane Git/jj writes, pushes, sibling edits, model calls, self-tests, or unrelated checks were performed. Tools installed or upgraded: none.

Report: .ufo/waves/round-59/controls/CtlAllFalse.md
