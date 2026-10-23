Result: DONE — CtlLabelShortcut: S 0 of 0; F 0 of 0; G 0; exit 1; predicate NOT MET

## Control and detector

Control: `CtlLabelShortcut`, one label-keyed shortcut world, retained as sandbox 063faa4b822a25b89637c0390a3683c0bbdbf86b (/fast/scratch/hyaku/kotoba-r59/CtlLabelShortcut), branch `sandbox/CtlLabelShortcut`. Its parent is frozen revision `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`. The sandbox working tree was restored to that frozen revision after the probe; the control commit remains available on its branch.

Mutant: add the required hook section, knowledge-entry table, seven synthetic SOURCES rows S096–S102, lesson Gate and seven fixture snapshots. Select unrelated tokens solely by client label from the existing agent-definition/plugin-manifest tables; copy events, action and quote strings from the counter's self-test. Copy URLs and full digest pins from the census reports without opening any hook page. The counter itself is unmodified. The control files explicitly identify their synthetic provenance and are not admitted knowledge.

Expected detector: the frozen `--fetch` predicate must not accept these unrelated paths and copied fixtures. Token grammar, quote/token alignment and census-pin-versus-fixture-byte checks should reject them before live fetching.

Observed: all seven labels are rejected; S=0, F=0, G=0, exit 1. K=0 counts well-formed tokens, not the seven presented client rows. This control does not meet the predicate. Mutation-testing verdict: **INCONCLUSIVE**, not a killed mutant, because the pristine baseline also exits 1; this is a negative control result, not evidence from a passing baseline.

C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET

Read from the committed frozen counter copied into the clone: `verifiers/check_hook_files.py:253-254` has `TARGET = 4`, `NEW_TARGET = 5`. `plans/round-59.md:35-62` defines the row rule/predicate; its freeze addendum at lines 93–98 states that Events checks printed identifiers, not their semantic status as hook events. This control makes no semantic-events claim and does not change that contract.

Axes used for this probe: isolation, evidence fidelity, behavioral discrimination. No tools installed or updated. No paid client CLI, browser, challenge bypass, additional agent or runtime invoked. All code execution and Git writes occurred only in the assigned sandbox clone; the only lane write is this report.

## Input provenance

All paths below are in the frozen clone unless marked as control-commit paths. No hook page was manually fetched. The counter only calls `fetch` for backed rows (`verifiers/check_hook_files.py:2383-2390`); every probe had zero backed rows, so none of these runs entered that loop. Accordingly there are no new HTTP status/body/hash receipts from this seat. Census fetch metadata below is copied evidence, not a claimed independent access.

| Client / new row | Hook config copied unchanged | Frozen SKILL.md location | URL/digest receipt copied |
|---|---|---|---|
| Claude Code / S096 | `.claude-plugin/plugin.json` | `SKILL.md:99`, Plugin manifests | `.ufo/waves/round-59/w0/CensusClaudeCode.md:13-17` |
| Codex / S097 | `.codex/agents/` | `SKILL.md:86`, Agent-definition files | `.ufo/waves/round-59/w0/CensusCodex.md:9-13` |
| VS Code / S098 | `.github/agents` | `SKILL.md:87`, Agent-definition files | `.ufo/waves/round-59/w0/CensusVSCode.md:8-14` |
| Copilot CLI / S099 | `plugin.json` | `SKILL.md:102`, Plugin manifests | `.ufo/waves/round-59/w0/CensusCopilotCLI.md:11-13` |
| Gemini CLI / S100 | `gemini-extension.json` | `SKILL.md:103`, Plugin manifests | `.ufo/waves/round-59/w0/CensusGeminiCLI.md:10-14` |
| Cursor / S101 | `.cursor/agents/` | `SKILL.md:90`, Agent-definition files | `.ufo/waves/round-59/w0/CensusCursor.md:7-10` |
| opencode / S102 | `.opencode/plugins/` | `SKILL.md:105`, Plugin manifests | `.ufo/waves/round-59/w0/Censusopencode.md:13-17` |

Census URL/digest pairs copied into SOURCES rows:

| Row | URL | Census sha256 |
|---|---|---|
| S096 | https://code.claude.com/docs/en/hooks.md | c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8 |
| S097 | https://learn.chatgpt.com/docs/hooks.md | 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92 |
| S098 | https://code.visualstudio.com/docs/agent-customization/hooks.md | 98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08 |
| S099 | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4 |
| S100 | https://geminicli.com/docs/hooks/best-practices.md | fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc |
| S101 | https://cursor.com/docs/hooks.md | 8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d |
| S102 | https://opencode.ai/docs/plugins.md | c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e |

Fixture reuse: `verifiers/check_hook_files.py:1845-1864` supplies the SKILL/entry/source/Gate table shapes, action text, quote1/quote2 and `page_for` helper. The quote strings were copied without substitutions or byte stripping:

- line 1852: `Claude Code runs a PreToolUse hook from a .claude/settings.json file`
- line 1853: `Gemini CLI runs a BeforeTool hook from a .gemini/hooks/ folder`

`PreToolUse`, `PostToolUse` came from fixture lines 1848 and 1872; `BeforeTool`, `AfterTool` from lines 1850 and 1873. All rows except Gemini use quote1 and the first event pair; Gemini uses quote2 and the second pair. Snapshots are literal expansions of `page_for` at lines 1857–1860, with no trailing newline, not fetched bodies. S096/97/98/99/101/102 use the same 130-byte Claude fixture; S100 uses the 122-byte Gemini fixture. Their actual hashes differ from the census pins, as intended by this assigned shortcut.

In the control commit, the new SKILL section starts at `SKILL.md:121`, SOURCES rows at `corpus/SOURCES.md:108-114`, entry table at `corpus/knowledge/hook-files-round59.md:9-17`, and Gate at `corpus/lessons/round-59.md:3-15`; each snapshot consists of fixture HTML on line 1.

## Frozen-counter identity

Read-only lane command, exit 0:

```sh
timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 67b68e0f9a0c48e5aa5ced63e6117cfca69da491:verifiers/check_hook_files.py | timeout 30 sha256sum
```

```text
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -
```

Clone identity command before mutation, exit 0, cwd `/fast/scratch/hyaku/kotoba-r59/CtlLabelShortcut`:

```sh
timeout 30 sha256sum verifiers/check_hook_files.py SKILL.md corpus/SOURCES.md && timeout 10 date -u
```

Full stdout:

```text
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
2af0a1a9c09fd241ce0c146976f4996f08714f2413b55f283ef8fdf5a1111e07  SKILL.md
9656d5d9d882d24b3b71f5ce63f96a4fd2a1732d90576b56fd5763350374d150  corpus/SOURCES.md
Fri 23 Oct 2026 09:21:52 AM UTC
```

## Pristine detector

Cwd for every detector below: `/fast/scratch/hyaku/kotoba-r59/CtlLabelShortcut`.

Exact command, exit 1, stderr empty:

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491 --fetch
```

Full stdout:

```text
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

## Control detector with --fetch

Measured sandbox 063faa4b822a25b89637c0390a3683c0bbdbf86b (/fast/scratch/hyaku/kotoba-r59/CtlLabelShortcut).

Exact command, exit 1, stderr empty:

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --rev 063faa4b822a25b89637c0390a3683c0bbdbf86b --fetch
```

Full stdout:

```text
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 063faa4b822a25b89637c0390a3683c0bbdbf86b
reject Claude Code: SKILL.md hook token '.claude-plugin/plugin.json' is not well-formed; entry row S096: quote does not hold the hook token '.claude-plugin/plugin.json' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S096.page sha256 44b97afee77d... does not equal the SOURCES row sha256 c6ef9d211e8c...
reject Codex: SKILL.md hook token '.codex/agents/' is not well-formed; entry row S097: quote does not hold the hook token '.codex/agents/' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S097.page sha256 44b97afee77d... does not equal the SOURCES row sha256 57166ef03e70...
reject VS Code: SKILL.md hook token '.github/agents' is not well-formed; entry row S098: quote does not hold the hook token '.github/agents' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S098.page sha256 44b97afee77d... does not equal the SOURCES row sha256 98c5be6b693a...
reject Copilot CLI: SKILL.md hook token 'plugin.json' is not well-formed; entry row S099: quote does not hold the hook token 'plugin.json' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S099.page sha256 44b97afee77d... does not equal the SOURCES row sha256 23370e092d2e...
reject Gemini CLI: SKILL.md hook token 'gemini-extension.json' is not well-formed; entry row S100: quote does not hold the hook token 'gemini-extension.json' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S100.page sha256 e8bbbf6997de... does not equal the SOURCES row sha256 fb44fbcfaccc...
reject Cursor: SKILL.md hook token '.cursor/agents/' is not well-formed; entry row S101: quote does not hold the hook token '.cursor/agents/' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S101.page sha256 44b97afee77d... does not equal the SOURCES row sha256 8436af768468...
reject opencode: SKILL.md hook token '.opencode/plugins/' is not well-formed; entry row S102: quote does not hold the hook token '.opencode/plugins/' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S102.page sha256 44b97afee77d... does not equal the SOURCES row sha256 c76613823185...
```

C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET

## Control detector without --fetch

Measured sandbox 063faa4b822a25b89637c0390a3683c0bbdbf86b (/fast/scratch/hyaku/kotoba-r59/CtlLabelShortcut).

Exact command, exit 1, stderr empty:

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --rev 063faa4b822a25b89637c0390a3683c0bbdbf86b
```

Full stdout:

```text
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 063faa4b822a25b89637c0390a3683c0bbdbf86b
reject Claude Code: SKILL.md hook token '.claude-plugin/plugin.json' is not well-formed; entry row S096: quote does not hold the hook token '.claude-plugin/plugin.json' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S096.page sha256 44b97afee77d... does not equal the SOURCES row sha256 c6ef9d211e8c...
reject Codex: SKILL.md hook token '.codex/agents/' is not well-formed; entry row S097: quote does not hold the hook token '.codex/agents/' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S097.page sha256 44b97afee77d... does not equal the SOURCES row sha256 57166ef03e70...
reject VS Code: SKILL.md hook token '.github/agents' is not well-formed; entry row S098: quote does not hold the hook token '.github/agents' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S098.page sha256 44b97afee77d... does not equal the SOURCES row sha256 98c5be6b693a...
reject Copilot CLI: SKILL.md hook token 'plugin.json' is not well-formed; entry row S099: quote does not hold the hook token 'plugin.json' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S099.page sha256 44b97afee77d... does not equal the SOURCES row sha256 23370e092d2e...
reject Gemini CLI: SKILL.md hook token 'gemini-extension.json' is not well-formed; entry row S100: quote does not hold the hook token 'gemini-extension.json' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S100.page sha256 e8bbbf6997de... does not equal the SOURCES row sha256 fb44fbcfaccc...
reject Cursor: SKILL.md hook token '.cursor/agents/' is not well-formed; entry row S101: quote does not hold the hook token '.cursor/agents/' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S101.page sha256 44b97afee77d... does not equal the SOURCES row sha256 8436af768468...
reject opencode: SKILL.md hook token '.opencode/plugins/' is not well-formed; entry row S102: quote does not hold the hook token '.opencode/plugins/' (case-sensitive); snapshot .ufo/waves/round-59/snapshots/S102.page sha256 44b97afee77d... does not equal the SOURCES row sha256 c76613823185...
```

## Mutated byte hashes

Command, exit 0:

```sh
timeout 30 sha256sum verifiers/check_hook_files.py SKILL.md corpus/SOURCES.md corpus/knowledge/hook-files-round59.md corpus/lessons/round-59.md .ufo/waves/round-59/snapshots/S096.page .ufo/waves/round-59/snapshots/S097.page .ufo/waves/round-59/snapshots/S098.page .ufo/waves/round-59/snapshots/S099.page .ufo/waves/round-59/snapshots/S100.page .ufo/waves/round-59/snapshots/S101.page .ufo/waves/round-59/snapshots/S102.page && timeout 30 wc -c .ufo/waves/round-59/snapshots/S096.page .ufo/waves/round-59/snapshots/S100.page
```

Full stdout:

```text
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
374f77d3b05a98588c3fa3cee8ab1d088c1e93ae6df1dd05a2676b608ea38ea1  SKILL.md
7585865572aac3bc7870fa29a73c205ac9abf081f181329d27b2e46d21f64724  corpus/SOURCES.md
544f4cc84379fd48101c340d6b3717d4b56cfea766e71cd6a6ae1caa7a61b4e2  corpus/knowledge/hook-files-round59.md
d2850970fc99807bc6504ec66c64d7ff7d389ab1b570b5c9a65f3b454cccb2e6  corpus/lessons/round-59.md
44b97afee77d654aebe5d7a8cbdf2c6231c34bd2bedd633ee9e146cf3ff46513  .ufo/waves/round-59/snapshots/S096.page
44b97afee77d654aebe5d7a8cbdf2c6231c34bd2bedd633ee9e146cf3ff46513  .ufo/waves/round-59/snapshots/S097.page
44b97afee77d654aebe5d7a8cbdf2c6231c34bd2bedd633ee9e146cf3ff46513  .ufo/waves/round-59/snapshots/S098.page
44b97afee77d654aebe5d7a8cbdf2c6231c34bd2bedd633ee9e146cf3ff46513  .ufo/waves/round-59/snapshots/S099.page
e8bbbf6997de1026169552a396c5c6e7e3efb6c501f56fb91db5f1721ad50d24  .ufo/waves/round-59/snapshots/S100.page
44b97afee77d654aebe5d7a8cbdf2c6231c34bd2bedd633ee9e146cf3ff46513  .ufo/waves/round-59/snapshots/S101.page
44b97afee77d654aebe5d7a8cbdf2c6231c34bd2bedd633ee9e146cf3ff46513  .ufo/waves/round-59/snapshots/S102.page
130 .ufo/waves/round-59/snapshots/S096.page
122 .ufo/waves/round-59/snapshots/S100.page
252 total
```

## Restoration evidence and restored detector

Restoration command, exit 0, cwd assigned clone:

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; timeout 10 git branch sandbox/CtlLabelShortcut 063faa4b822a25b89637c0390a3683c0bbdbf86b && timeout 30 git -c core.hooksPath=/dev/null checkout -q 67b68e0f9a0c48e5aa5ced63e6117cfca69da491 && timeout 30 sha256sum verifiers/check_hook_files.py SKILL.md corpus/SOURCES.md && timeout 10 git rev-parse HEAD 67b68e0f9a0c48e5aa5ced63e6117cfca69da491^{tree} HEAD^{tree}
```

Full stdout:

```text
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
2af0a1a9c09fd241ce0c146976f4996f08714f2413b55f283ef8fdf5a1111e07  SKILL.md
9656d5d9d882d24b3b71f5ce63f96a4fd2a1732d90576b56fd5763350374d150  corpus/SOURCES.md
67b68e0f9a0c48e5aa5ced63e6117cfca69da491
304854156e782f0e4e8d9d08db88537567f94139
304854156e782f0e4e8d9d08db88537567f94139
```

Thus the two edited existing files and the unchanged counter match their pristine hashes exactly. The nine added paths were absent before construction and absent again after restoration. The specialized glob query over the new entry, lesson and snapshot paths returned this same output before construction and after restoration:

```text
Path not found: /fast/scratch/hyaku/kotoba-r59/CtlLabelShortcut/corpus/knowledge/hook-files-round59.md, /fast/scratch/hyaku/kotoba-r59/CtlLabelShortcut/corpus/lessons/round-59.md, /fast/scratch/hyaku/kotoba-r59/CtlLabelShortcut/.ufo/waves/round-59/snapshots/*
```

Exact restored detector command, exit 1, stderr empty:

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491 --fetch
```

Full stdout:

```text
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

Final clock command `timeout 10 date -u`, exit 0:

```text
Fri 23 Oct 2026 09:24:37 AM UTC
```

No additional mutations or tests were run. The label/fixture shortcut did not meet the frozen C1 predicate; the baseline failure prevents calling it a killed mutant. Exact frozen bytes were restored, while the one control world remains retained in its labelled sandbox commit.

Report: .ufo/waves/round-59/controls/CtlLabelShortcut.md
