Result: DONE — CtlFabSnapshot: S 6 of 6; F 0 of 6; G 0; exit 1; predicate NOT MET

## Finding and expected detector

Control: **CtlFabSnapshot**, fabricated-snapshot negative control. Verdict: **KILLED by the declared live detector**. A real-source pristine world passed before mutation; the fabricated world failed specifically because every invented quote was absent from its live page; exact restoration passed again. The offline snapshot check accepted all six fabricated pages. That offline result is a coverage finding, not a change to the live contract.

C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET

Expected detector: `timeout 900 python3 -B verifiers/check_hook_files.py --rev <sandbox-commit> --fetch`; expected mutation outcome: S=6, F=0, G=0, exit 1. Without `--fetch`, expected S=6 and exit 1 because offline mode never satisfies C1.

Axes held: frozen-counter integrity, one-defect isolation, reproducible receipts and exact restoration. No counter edits, lane code execution, lane Git/jj writes, pushes, tool installs, paid model calls, browser use, or challenge bypasses. The only lane write is this report. All code execution and sandbox commits occurred in the assigned clone.

## Freeze and worlds

Freeze: `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`. Read `TARGET = 4` and `NEW_TARGET = 5` from committed `verifiers/check_hook_files.py:253-254`, not the task prose. Read `plans/round-59.md` C1 and its freeze addendum: the Events conjunct proves printed identifier presence, not event semantics. This control uses actual event names; it does not probe the addendum limitation.

- Pristine positive baseline: sandbox 2854318355cf29f87dbca3bbf39f61c8ea894fae (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot).
- Fabricated-snapshot control: sandbox cff124a8b6593179c29099a74ae8466662d0710c (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot).
- Exact restored positive world: sandbox 76310513bda537e3b58c249de44cccb072e79e08 (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot).

All three descend from the freeze in this isolated clone. K=6 uses the six eligible census clients. opencode is deliberately absent because the frozen census marks it ineligible; its rejection is included in every stdout below.

Frozen lane-byte check, exit 0:
```text
$ timeout 60 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 67b68e0f9a0c48e5aa5ced63e6117cfca69da491:verifiers/check_hook_files.py | sha256sum
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -
```

From the clone, before the baseline and after restoration, exit 0 both times:
```text
$ timeout 60 sha256sum verifiers/check_hook_files.py
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
```

## One coordinated mutation

Kept the exact same six census tokens, source URLs, real Events cells, client names, action cells, source ids, date, kind, tier and status. Replaced only quote provenance: all six entry/Gate quotes became invented eleven-word sentences; six snapshot pages were fabricated to contain those sentences plus the unchanged real events; six SOURCES pins were changed to the fabricated bytes. The Gate location/provenance note changed accordingly. The misleading `fetched` text retained in SOURCES is part of this intentional negative control, not a claim about the fabricated pages.

World evidence at the control commit: `SKILL.md:121-132`; `corpus/knowledge/hook-files-round59.md:9-14`; `corpus/SOURCES.md:108-113`; `corpus/lessons/round-59.md:5-16`; each `.ufo/waves/round-59/snapshots/S096.page` through `S101.page`, line 1. Reused the frozen self-test's `page_for` helper and `src_row` formatter verbatim via AST extraction (`verifiers/check_hook_files.py:1857-1882`); no self-test or helper monkeypatching was run.

Invented quote template (11 words, token at word 8): `The glass otter stores ceremonial hooks in <token> for violet Tuesdays.` These are fabricated control strings, not quotations from vendors:

| Row | Client | Token | Real events | Fabricated page bytes | Fabricated page sha256 (also in SOURCES) |
|---|---|---|---|---:|---|
| S096 | Claude Code | `.claude/settings.json` | `PreToolUse`, `PostToolUse` | 147 | `8983bb109bc7add7ca96d49c2b2ff14233dacf014a5208ca942fca67cc71c978` |
| S097 | Codex | `~/.codex/hooks.json` | `PreToolUse`, `SessionStart` | 146 | `a453e48161db51363f9a3bec9fd5bb0c27825fd73c7b5f300a0c356a7cd9bbb1` |
| S098 | VS Code | `.github/hooks/*.json` | `sessionStart`, `preToolUse` | 147 | `943555c0c19d2ad24a1ae7704ca75aa668dcab21b23ac3620eaeef3c3f19a2bd` |
| S099 | Copilot CLI | `~/.copilot/hooks/*.json` | `sessionStart`, `preToolUse` | 150 | `66e494bb7ab0336b35e44f1344855d63ef5f934aea02104fa5180887f39f1503` |
| S100 | Gemini CLI | `.gemini/settings.json` | `BeforeTool`, `AfterModel` | 146 | `8b6b22381059aef77cfec048dc3e321665377f941443047d5c35ec25194e6bbc` |
| S101 | Cursor | `.cursor/hooks.json` | `preToolUse`, `postToolUse` | 144 | `7b3ee5600979ec3fa2dd3c6b0099ef2d956e495230cea2fd5dff36e9d6684868` |

The invented quotes contain the literal word `hooks` outside the token and satisfy the 6–25-word rule. Every fabricated page is the helper's `<p>quote</p><p><code>event</code> ...</p>` layout. The offline detector accepting 6/6 below demonstrates the pages, pins, quotes, Gate and event-presence constraints were wired correctly.

## Full bounded behavioral receipts

All commands below ran from `/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot`. Stdout is reproduced in full; stderr was empty for every detector run. No baseline failure was treated as a killed mutant.

### Pristine — offline

sandbox 2854318355cf29f87dbca3bbf39f61c8ea894fae (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot)

```text
Fri Oct 23 09:25:51 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 2854318355cf29f87dbca3bbf39f61c8ea894fae
hook files backed on committed snapshots 6 of 6; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 2854318355cf29f87dbca3bbf39f61c8ea894fae
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: empty
```

### Pristine — live

sandbox 2854318355cf29f87dbca3bbf39f61c8ea894fae (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot)

```text
Fri Oct 23 09:25:51 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 2854318355cf29f87dbca3bbf39f61c8ea894fae --fetch
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 2854318355cf29f87dbca3bbf39f61c8ea894fae
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: empty
```

### Mutant — offline

sandbox cff124a8b6593179c29099a74ae8466662d0710c (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot)

```text
Fri Oct 23 09:26:56 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev cff124a8b6593179c29099a74ae8466662d0710c
hook files backed on committed snapshots 6 of 6; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev cff124a8b6593179c29099a74ae8466662d0710c
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: empty
```

### Mutant — live

sandbox cff124a8b6593179c29099a74ae8466662d0710c (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot)

```text
Fri Oct 23 09:26:56 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev cff124a8b6593179c29099a74ae8466662d0710c --fetch
hook files backed on committed snapshots 6 of 6; found on the live page 0 of 6; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev cff124a8b6593179c29099a74ae8466662d0710c
reject Claude Code: live page: the quote is not on the page
reject Codex: live page: the quote is not on the page
reject VS Code: live page: the quote is not on the page
reject Copilot CLI: live page: the quote is not on the page
reject Gemini CLI: live page: the quote is not on the page
reject Cursor: live page: the quote is not on the page
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: empty
```

### Restored — offline

sandbox 76310513bda537e3b58c249de44cccb072e79e08 (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot)

```text
Fri Oct 23 09:27:17 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 76310513bda537e3b58c249de44cccb072e79e08
hook files backed on committed snapshots 6 of 6; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 76310513bda537e3b58c249de44cccb072e79e08
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: empty
```

### Restored — live

sandbox 76310513bda537e3b58c249de44cccb072e79e08 (/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot)

```text
Fri Oct 23 09:27:17 AM UTC 2026
$ timeout 900 python3 -B verifiers/check_hook_files.py --rev 76310513bda537e3b58c249de44cccb072e79e08 --fetch
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 76310513bda537e3b58c249de44cccb072e79e08
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: empty
```

## Opened source receipts and real-event provenance

Ordinary curl only, using the frozen counter's browser UA and Accept header. Initial source collection command: `timeout 240 python3 -B ctl_fab_snapshot_fetch.py` (exit 0, one GET for each of the six census URLs). Cursor's `.md` URL returned HTTP 404, so it was not used as the row URL; the separately opened known non-`.md` URL returned HTTP 200 and the census bytes. No challenge was passed. Each source-collection run fetched a URL once; each frozen live-detector invocation has the frozen maximum of three attempts per URL. There were no fetch retries added by this probe.

Source collection metadata (date lines copied from actual `date -u` output; effective URL equals requested URL for every row):

| Row/use | Requested URL | date -u | HTTP | Bytes | sha256 |
|---|---|---|---:|---:|---|
| S096 (used) | https://code.claude.com/docs/en/hooks.md | `Fri Oct 23 09:22:45 AM UTC 2026` | 200 | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` |
| S097 (used) | https://learn.chatgpt.com/docs/hooks.md | `Fri Oct 23 09:22:45 AM UTC 2026` | 200 | 47133 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` |
| S098 (used) | https://code.visualstudio.com/docs/agent-customization/hooks.md | `Fri Oct 23 09:22:45 AM UTC 2026` | 200 | 15152 | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` |
| S099 (used) | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | `Fri Oct 23 09:22:45 AM UTC 2026` | 200 | 8428 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` |
| S100 (used) | https://geminicli.com/docs/hooks/best-practices.md | `Fri Oct 23 09:22:45 AM UTC 2026` | 200 | 17650 | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` |
| S101 (not used, initial 404) | https://cursor.com/docs/hooks.md | `Fri Oct 23 09:22:45 AM UTC 2026` | 404 | 389 | `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` |
| S101 (used alternate URL) | https://cursor.com/docs/hooks | `Fri Oct 23 09:23:23 AM UTC 2026` | 200 | 69145 | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` |

Source bytes and raw metadata: `/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot/.ctl/CtlFabSnapshot/fetched/metadata.json` and the saved paths named there. Cursor alternate fetch used:
```text
timeout 45 curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' https://cursor.com/docs/hooks
exit 0; HTTP 200; 69145 body bytes
```

The following positive-baseline quotes are byte-exact contiguous slices of those fetched bytes, each at most 25 words. No bytes are stripped in these report quotations. For Markdown-table storage only, the baseline applies whitespace splitting/joining (all whitespace runs become one ASCII space), and replaces the two VS Code U+007C pipe bytes with the six ASCII bytes `&#124;` each. Backticks and all other non-whitespace bytes are retained. Counter quote normalization accepts that table encoding.

### S096 — Claude Code

https://code.claude.com/docs/en/hooks.md; fetched bytes lines 910-910; 21 words.

```text
This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails:
```

Real event identifiers on the same fetched page: `PreToolUse` line 37, `PostToolUse` line 40.

### S097 — Codex

https://learn.chatgpt.com/docs/hooks.md; fetched bytes lines 38-44; 22 words.

```text
a default `hooks/hooks.json` file. See [Build
plugins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) for the
plugin packaging rules.

In practice, the four most useful locations are:

- `~/.codex/hooks.json`
```

Real event identifiers on the same fetched page: `PreToolUse` line 25, `SessionStart` line 27.

### S098 — VS Code

https://code.visualstudio.com/docs/agent-customization/hooks.md; fetched bytes lines 59-60; 8 words.

```text
`.github/hooks/*.json` at the repository root |
| Hooks
```

Real event identifiers on the same fetched page: `sessionStart` line 128, `preToolUse` line 130.

### S099 — Copilot CLI

https://docs.github.com/en/copilot/concepts/customizations/hooks.md; fetched bytes lines 28-28; 8 words.

```text
Copilot CLI also supports personal hooks in `~/.copilot/hooks/*.json`.
```

Real event identifiers on the same fetched page: `sessionStart` line 34, `preToolUse` line 37.

### S100 — Gemini CLI

https://geminicli.com/docs/hooks/best-practices.md; fetched bytes lines 413-413; 10 words.

```text
When you open a project with hooks defined in `.gemini/settings.json`:
```

Real event identifiers on the same fetched page: `BeforeTool` line 31, `AfterModel` line 31.

### S101 — Cursor

https://cursor.com/docs/hooks; fetched bytes lines 50-50; 24 words.

```text
If you have hooks defined in `.cursor/hooks.json` at the root of your project, cloud agents pick them up and run them during their work.
```

Real event identifiers on the same fetched page: `preToolUse` line 860, `postToolUse` line 897.

## Exact-byte restoration evidence

All ten world files were backed up before mutation. Restoration ran in an unconditional `finally` block after the mutant detector, then was committed; exact byte comparisons were true for 10/10 files, and the full restored SHA256 mapping equaled the pristine mapping. The unchanged counter was also hashed in all phases. The restored detector again returned S=6, F=6, G=6, exit 0. No scratch world remains mutated.

Actual per-file SHA256 values (`before` is pristine; `after` is the fabricated world; `restored` is after exact-byte restoration):

| Path | Before | After | Restored |
|---|---|---|---|
| `SKILL.md` | `2e6d7b3c22803165225f152cf3b5f4a7d4f7263226ce24f7a416435647b44630` | `2e6d7b3c22803165225f152cf3b5f4a7d4f7263226ce24f7a416435647b44630` | `2e6d7b3c22803165225f152cf3b5f4a7d4f7263226ce24f7a416435647b44630` |
| `corpus/knowledge/hook-files-round59.md` | `b0e9fbe9d715050ec0bbd3ca4a7453280391b2abc2161cace0b7a54eb1858cf2` | `4b3722cb35c61403948e04270537efd3cd4698a2386ddafa1d9beb5d006b1fb6` | `b0e9fbe9d715050ec0bbd3ca4a7453280391b2abc2161cace0b7a54eb1858cf2` |
| `corpus/SOURCES.md` | `2955a050bb731609ea2db705f07a49eb0f959402ca3a04445b9dd20b49e1a68f` | `2ce63218534f68a08a0212a2f46a4250fde9273f1784262d90037e17cfda3e87` | `2955a050bb731609ea2db705f07a49eb0f959402ca3a04445b9dd20b49e1a68f` |
| `corpus/lessons/round-59.md` | `3a79fcc8c4fd346743b3a3fe6288a022d6f6fa4f3c7cba7663c50c200ef5214b` | `b2e280b3b94807a14b46e592c5f5022df3d952240ec1eb6e5e406b93f4569321` | `3a79fcc8c4fd346743b3a3fe6288a022d6f6fa4f3c7cba7663c50c200ef5214b` |
| `.ufo/waves/round-59/snapshots/S096.page` | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` | `8983bb109bc7add7ca96d49c2b2ff14233dacf014a5208ca942fca67cc71c978` | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` |
| `.ufo/waves/round-59/snapshots/S097.page` | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` | `a453e48161db51363f9a3bec9fd5bb0c27825fd73c7b5f300a0c356a7cd9bbb1` | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` |
| `.ufo/waves/round-59/snapshots/S098.page` | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` | `943555c0c19d2ad24a1ae7704ca75aa668dcab21b23ac3620eaeef3c3f19a2bd` | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` |
| `.ufo/waves/round-59/snapshots/S099.page` | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` | `66e494bb7ab0336b35e44f1344855d63ef5f934aea02104fa5180887f39f1503` | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` |
| `.ufo/waves/round-59/snapshots/S100.page` | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` | `8b6b22381059aef77cfec048dc3e321665377f941443047d5c35ec25194e6bbc` | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` |
| `.ufo/waves/round-59/snapshots/S101.page` | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` | `7b3ee5600979ec3fa2dd3c6b0099ef2d956e495230cea2fd5dff36e9d6684868` | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` |
| `verifiers/check_hook_files.py` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` |

Machine-readable receipts and restoration evidence, retained only in the assigned sandbox:
- `/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot/.ctl/CtlFabSnapshot/receipts.json` (all six exact commands, dates, stdout, stderr and exit codes).
- `/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot/.ctl/CtlFabSnapshot/pristine_hashes.json` and `mutant_hashes.json`.
- `/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot/.ctl/CtlFabSnapshot/restoration.json` (all ten byte-equality results and restored hashes).

Final scope: only this assigned mutation probe was performed. No admission, integration, shipping decision or contract change is asserted. No tools were installed or updated.

Report: .ufo/waves/round-59/controls/CtlFabSnapshot.md
