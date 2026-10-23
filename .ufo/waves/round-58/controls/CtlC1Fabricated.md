Result: BREAKS — the no-reader surface gives fabricated attributions a high backing count (6/6), but the frozen --fetch predicate rejects the world (F=0, K=6, G=0; exit 1).

## Counterexample and scope

**FINDING: high no-reader backing count, not a pass of C1.** Six real command/prompt-folder tokens, six existing pinned-host documentation URLs, and six invented 13-word quotations produce `backed 6 of 6` without reading a page. With `--fetch`, none counts. Neither run exits 0; this world does **not** meet the committed predicate F>=4 and G>=3 on `--fetch`.

Axes: claimed C1 depth/new ground, source fidelity, and provenance honesty. The vulnerability is only in treating structural backing as source verification; the declared live-fetch gate holds against this control. K is a token-shape count, not a count of verified facts.

World: **sandbox 6a3f2d35ee73014dcafb445a21c73b74a26e99c5 (/fast/scratch/hyaku/kotoba-r58/CtlC1Fabricated)**. Parent is the requested counter commit `3de87aad29e960c95ed35840442f424c48c29729`; no counter was edited. Only four world files were committed:

- `SKILL.md:125-137`: six-row command-file table, with identical generic file-setting/action cells.
- `corpus/SOURCES.md:102-107`: S089–S094, typed `docs`, tier A, `mined`, opened 2026-10-23; real URLs with fabricated teaching text.
- `corpus/knowledge/command-files-round58.md:7-12`: fabricated quotes attributed to those rows.
- `corpus/lessons/round-58.md:5-10`: the same invented quotes repeated in `## Gate`.

No client runtime, paid model, canonical judge, admission, integration, or push was invoked. No lane content was changed except this report. Source captures remain untracked in the sandbox.

### Scores

| Run | F | K | G | Other observed count | Exit | Meets frozen C1 predicate? |
|---|---:|---:|---:|---|---:|---|
| `--fetch` | 0 | 6 | 0 | six structurally BACKED rows; all `found=no` | 1 | No |
| without `--fetch` | not measured | 6 | not computed | B=6 backed of 6 | 1 | No; this is not the predicate run |

The actual no-fetch output does not report F or G. Its six is **B, not F**; assigning F=6 or G=4 to that run would fabricate a measurement. The six covers the eligible population but does not establish six sourced facts.

## Construction and counter custody

Clone/checkout command (exit 0):

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; timeout 900 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/CtlC1Fabricated && timeout 900 git -C /fast/scratch/hyaku/kotoba-r58/CtlC1Fabricated checkout -q 3de87aad29e960c95ed35840442f424c48c29729
```

Before world edits, in that clone at the requested revision, command (exit 0):

```sh
timeout 900 sha256sum verifiers/check_command_files.py verifiers/check_sweep_mutants.py
```

Full output:

```text
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
```

Read-only committed-blob custody command (exit 0):

```sh
timeout 900 git --no-optional-locks log -1 --format='%H%n%s%n%aI' 3de87aad29e960c95ed35840442f424c48c29729 && timeout 900 git --no-optional-locks show 3de87aad29e960c95ed35840442f424c48c29729:verifiers/check_command_files.py | timeout 900 sha256sum
```

Full output:

```text
3de87aad29e960c95ed35840442f424c48c29729
round-58: pre-freeze — C1/C2 counters (targets F>=4, G>=3 after the Q45 census 6/4), gate-registry rows, census record, W0 evidence
2026-10-23T04:51:33-03:00
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  -
```

The initial context's `None` target statement was stale, as L1 subsequently confirmed. The requested committed bytes actually have `TARGET = 4`, `NEW_TARGET = 3` at `verifiers/check_command_files.py:246-247`. Both scoring runs identify the same sha256 above. No sentinel or target modification was used.

Commit creation used `timeout 900 git add SKILL.md corpus/SOURCES.md corpus/knowledge/command-files-round58.md corpus/lessons/round-58.md` followed by `timeout 900 git -c core.hooksPath=/dev/null -c commit.gpgSign=false commit -m 'sandbox control: fabricated command-file source quotations'` (exit 0). The commit changed four files, 42 insertions; no counter file was staged.

## Full scoring receipts

Both commands ran in `/fast/scratch/hyaku/kotoba-r58/CtlC1Fabricated` against **sandbox 6a3f2d35ee73014dcafb445a21c73b74a26e99c5 (/fast/scratch/hyaku/kotoba-r58/CtlC1Fabricated)**. Hashes inside the verbatim commands/output below identify this sandbox world, not a lane commit.

### Live-source run — exit 1

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev 6a3f2d35ee73014dcafb445a21c73b74a26e99c5 --fetch
```

Full output:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 6a3f2d35ee73014dcafb445a21c73b74a26e99c5
custom command files found on the live page 0 of 6; new ground 0
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands found=no
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts found=no
VS Code      BACKED token=.github/prompts/ norm=.github/prompts found=no
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Gemini CLI   BACKED token=.gemini/commands/ norm=.gemini/commands found=no
Cursor       BACKED token=.cursor/commands/ norm=.cursor/commands found=no
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands found=no
```

### No-reader run — exit 1

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev 6a3f2d35ee73014dcafb445a21c73b74a26e99c5
```

Full output:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 6a3f2d35ee73014dcafb445a21c73b74a26e99c5
custom command files backed 6 of 6; new ground not computed (needs --fetch)
Claude Code  BACKED token=.claude/commands/ norm=.claude/commands
Codex        BACKED token=~/.codex/prompts/ norm=.codex/prompts
VS Code      BACKED token=.github/prompts/ norm=.github/prompts
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Gemini CLI   BACKED token=.gemini/commands/ norm=.gemini/commands
Cursor       BACKED token=.cursor/commands/ norm=.cursor/commands
opencode     BACKED token=.opencode/commands/ norm=.opencode/commands
```

## Sources: real pages, invented quotes

Every control quotation is the following **fabricated** sentence with its own row's token substituted, not a quotation found on the linked page:

> Save reusable commands in `.claude/commands/` and give every prompt a short purpose statement.

The other tokens are `~/.codex/prompts/`, `.github/prompts/`, `.gemini/commands/`, `.cursor/commands/`, and `.opencode/commands/`. Each resulting quote has 13 whitespace-delimited words, a case-exact token, and command/prompt words outside that token. There is no quote shaping in the fabricated strings. Real-source byte locations below establish that the tokens/URLs are plausible; they are not represented as support for the fabricated sentence.

Captures are under `/fast/scratch/hyaku/kotoba-r58/CtlC1Fabricated/control-evidence/fabricated/`. All six ordinary HTTP opens returned 200 without changing the URL. The opencode response is HTML despite the local `.md` filename. No bot challenge or access control was bypassed.

| Client | Requested and effective URL | Captured file; real token location | HTTP | Bytes | sha256 |
|---|---|---|---:|---:|---|
| Claude Code | https://code.claude.com/docs/en/slash-commands.md | `claude.md:172` | 200 | 114542 | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |
| Codex | https://learn.chatgpt.com/docs/custom-prompts.md | `codex.md:62` | 200 | 3357 | `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` |
| VS Code | https://code.visualstudio.com/docs/agent-customization/prompt-files.md | `vscode.md:25` | 200 | 13729 | `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685` |
| Gemini CLI | https://geminicli.com/docs/cli/custom-commands.md | `gemini.md:12-17` | 200 | 12129 | `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872` |
| Cursor | https://cursor.com/docs/reference/deeplinks.md | `cursor.md:54` | 200 | 5972 | `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` |
| opencode | https://opencode.ai/v2/docs/commands/ | `opencode.md:66` | 200 | 32304 | `32591ac3db0056fdbf3b5e20b78e70514da0d7306707cbf7c412ca19276640e0` |

For each row, the actual source-open command had this form, with its listed file stem and URL (all six command sequences exited 0):

```sh
timeout 900 date -u && timeout 120 curl --location --max-time 100 --connect-timeout 15 --silent --show-error --user-agent kotoba-shokunin-counter/58 --dump-header control-evidence/fabricated/STEM.headers --output control-evidence/fabricated/STEM.md --write-out 'http_status %{http_code}\nurl_effective %{url_effective}\nsize_download %{size_download}\n' URL && timeout 900 sha256sum control-evidence/fabricated/STEM.md
```

Verbatim `date -u` output for each of Claude Code, Codex, VS Code, and Gemini CLI:

```text
Fri 23 Oct 2026 07:55:35 AM UTC
```

Verbatim `date -u` output for each of Cursor and opencode:

```text
Fri 23 Oct 2026 07:55:46 AM UTC
```

A case-insensitive `functions.grep` over the six captured `.md` files, pattern `Save reusable commands in|give every prompt a short purpose statement`, `gitignore=false`, returned exactly `No matches found` (tool search, no shell exit code). This establishes absence of the fabricated prefix/suffix in the captured bytes. The frozen live run separately reports all six `found=no`; its plain-text output does not expose fetch-error details, so no stronger transport-cause claim is made about that run.

## Smallest safe correction

Keep `--fetch` mandatory for C1 claim receipts, and never substitute B or K for F. The frozen implementation already returns 1 without `--fetch` (`verifiers/check_command_files.py:1073-1076`) and computes new ground only from live-found rows (`:1933-1944`). No counter edit is needed to reject this world. If a consumer promotes the no-fetch `BACKED` label into verified provenance, correct that consumer/receipt interpretation; changing frozen semantics would be a separately declared measurement.

No tools were installed or updated. Only the assigned control runs were performed; no self-tests, builds, linters, unrelated probes, or C2 scoring were run.
