Result: DONE — CtlReopenForged: a S/F=0/0 offline/live exit=1/1; b S/F=0/0 offline/live exit=1/1; c S/F=0/0 offline/live exit=1/1; d S/F=3/3 offline/live exit=1/0; predicate MET

## Finding and bounds

Control: `CtlReopenForged`, counter v2. Variants a–c were KILLED. Variant d SURVIVED: historical page bytes copied from the held S043/S048/S049 reads, with new S103–S105 ids and correctly bound `re-opens` prefixes, back all three clients and reach F=3. This is a coverage finding about fresh-reading provenance, not permission to change the frozen contract. Erratum E1 promises a new key fact relative to the held SOURCES line; it does not authenticate when snapshot bytes were acquired. No counter code, lane source, sibling clone, or contract was changed. The sole lane write is this report.

Axes: prefix binding, source/snapshot provenance, exact-byte restoration. All executable work ran in the designated isolated clone. No tools were installed or updated. No model calls, browser, alternate runtime, subagents, or pushes were used.

## Frozen detector and expected discrimination

Freeze revision: `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`. Read `TARGET = 3` from the committed cloned counter at `verifiers/check_scoped_rules.py:249`; `BASE` is its own pinned round-59 base (`:243`). Read plan C1/A1/E1 at `plans/round-60.md:21–153`. Relevant counter points: snapshot pin `:1068–1096`, reopen binding `:972–994`, live quote/key check `:2535–2547`, and predicate `:1245–1249`.

Observed frozen-byte checks (both exit 0):

```text
$ timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show b1cd64bb45eee744c4ec93be8631f1eddb28fddd:verifiers/check_scoped_rules.py | timeout 30 sha256sum
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  -
$ timeout 30 sha256sum verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

Expected detector: the identical bounded frozen CLI, with and without `--fetch`, on pristine, each mutant, and exact restored bytes. A missing prefix, a wrong held id, or a non-base id must reject the three reopened base URLs. Variant d separately challenges whether a fresh-day row/prefix is evidence of a fresh source read; the frozen implementation has no acquisition-time authentication. A live exit 0 means F>=TARGET. Offline always exits 1 by contract, even when every snapshot is backed; “passes offline” below means S=3. Baseline live exit 0 and restored live exit 0 make a–c kills conclusive, not baseline failures.

## World construction and mutations

World shape reuses the frozen `--self-test` world helper layout (`verifiers/check_scoped_rules.py:1704–1753`): SKILL section/header, entry table, Gate quotes, 11-column SOURCES rows, per-id SHA pins, and committed snapshots. Existing helpers `curl_argv`, `snapshot_path`, and `self_sha` were reused without modifying their module. No `--self-test` was run.

All worlds have exactly three eligible client rows: Claude Code `.claude/rules/` / `paths`, Copilot CLI `.github/instructions` / `applyTo`, Cursor `.cursor/rules` / `globs`. The Copilot folder is the census report’s explicit alternate eligible token (`w0/CensusCopilotCLI.md:122–130`), avoiding an embedded table pipe without shaping any quote. Cursor uses the census’s working `/docs/rules` route; its URL key equals S049’s `/docs/rules.md` key under the frozen normalization. Four absent clients produce expected reject lines but do not enter K=3.

In every world: `SKILL.md:135–141`, `corpus/knowledge/scoped-rules-round60.md:3–7`, `corpus/lessons/round-60.md:3–7`, `corpus/SOURCES.md:115–117`, and `.ufo/waves/round-60/snapshots/S103.page` through `S105.page`. Commits are sequential descendants of the freeze; only this seat’s clone was written.

| World | Small mutation versus pristine | S | F | Offline exit | Live exit | Verdict |
|---|---|---:|---:|---:|---:|---|
| pristine | Correct S043/S048/S049 prefixes; construction fetch bytes | 3 | 3 | 1 | 0 | Satisfying baseline |
| a | Remove `re-opens S### —` from each new row’s teaches cell | 0 | 0 | 1 | 1 | KILLED |
| b | All three teaches prefixes name held id S047, whose URL differs | 0 | 0 | 1 | 1 | KILLED |
| c | Prefixes name S103/S104/S105 respectively: current new ids, not base ids | 0 | 0 | 1 | 1 | KILLED |
| d | Correct prefixes; copy the actual old S043/S048/S049 fetched bytes into new snapshots and pin those SHA values | 3 | 3 | 1 | 0 | SURVIVED |
| restored | Restore exact pristine bytes of every world file | 3 | 3 | 1 | 0 | Restoration passes |

For d, no construction refetch was made: all three snapshot contents came directly from round-53 saved files. The new rows deliberately retain the pristine `Fetched 2026-10-23T12:06:23Z` assertion, so it is a forged provenance claim in this mutant, not a report assertion. Only S103’s SHA/byte count and body differ from pristine: S048 and S049 already had byte-identical bodies. S103’s old page still has the chosen quote :168, action :194, and key :198–199, so unrelated semantic/pin failures do not mask the freshness probe. Counter `--fetch` still performs its required live check; “no fresh fetch” here refers to the provenance of committed d snapshot bytes, not suppressing the live detector.

## Construction fetch receipts and verbatim evidence

One explicit construction fetch per page, ordinary curl with the frozen UA/Accept. The frozen live detector retains its own maximum of three attempts per page per command. No other source was fetched by this seat. Construction headers, exact bodies, and JSON receipts are under `/fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts/fetch`. Live CLI timestamps/commands/stdout/stderr/exit are separately saved in `/fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts`; the frozen counter does not output live body hashes, so none is asserted.

### S103 — Claude Code

URL: https://code.claude.com/docs/en/memory.md

```text
$ date -u
Fri Oct 23 12:06:23 PM UTC 2026
$ timeout 45 curl -D /fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts/fetch/S103.headers -o /fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts/fetch/S103.page -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '
%{http_code} %{url_effective}' https://code.claude.com/docs/en/memory.md

200 https://code.claude.com/docs/en/memory.md
exit 0
stderr: (empty)
bytes 54043
sha256 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7
```

Quote at fetched line 168 (14 words), byte-exact contiguous text; no bytes stripped, Markdown backticks retained:

```text
For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory.
```

Scope key citation: `paths` at line 198; Action cell at line 194: Scope rules to specific files using YAML frontmatter and matching patterns. These same citations are used in all variants.

### S104 — Copilot CLI

URL: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md

```text
$ date -u
Fri Oct 23 12:06:23 PM UTC 2026
$ timeout 45 curl -D /fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts/fetch/S104.headers -o /fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts/fetch/S104.page -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '
%{http_code} %{url_effective}' https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md

200 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
exit 0
stderr: (empty)
bytes 8730
sha256 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
```

Quote at fetched line 56 (11 words), byte-exact contiguous text; no bytes stripped, Markdown backticks retained:

```text
2. Optionally, create subdirectories of `.github/instructions` to organize your instruction files.
```

Scope key citation: `applyTo` at line 66; Action cell at line 60: Create a frontmatter block containing `applyTo` and use glob syntax to specify files or directories. These same citations are used in all variants.

### S105 — Cursor

URL: https://cursor.com/docs/rules

```text
$ date -u
Fri Oct 23 12:06:23 PM UTC 2026
$ timeout 45 curl -D /fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts/fetch/S105.headers -o /fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts/fetch/S105.page -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '
%{http_code} %{url_effective}' https://cursor.com/docs/rules

200 https://cursor.com/docs/rules
exit 0
stderr: (empty)
bytes 17403
sha256 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
```

Quote at fetched line 32 (11 words), byte-exact contiguous text; no bytes stripped, Markdown backticks retained:

```text
Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled.
```

Scope key citation: `globs` at line 85; Action cell at line 131: Use `globs` to scope a rule to specific files or directories; separate multiple patterns with commas. These same citations are used in all variants.

## Historical bytes used only by d

These files were read, never written. Observed command, exit 0:

```text
$ timeout 30 sha256sum /fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md /fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/copilot-cli-custom-instructions.md /fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.4524a03e99d4

971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff  /fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md

00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  /fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/copilot-cli-custom-instructions.md

884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  /fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.4524a03e99d4

```

S043’s full SHA is recorded in the frozen SOURCES row `corpus/SOURCES.md:56`. S048’s row `:61` records prefix `00e45ea5…` and 8730 bytes; the old saved file above resolves that prefix to the full matching digest. S049’s row `:62` records prefix `884c67ca…` and 17403 bytes; its full hash and the same gate time are also in `round-53/build/ScribeCursor.md:78` and the saved `ScribeCursor/fetch/gate.tsv:1`. Original fetch times/statuses are inherited historical evidence, not new fetches by this seat: S043 2026-10-22T20:04:43Z HTTP 200 (51971 bytes), S048 2026-10-22T20:05:13Z HTTP 200 (8730 bytes), S049 2026-10-22T20:09:33Z HTTP 200 (17403 bytes).

## Full frozen-counter receipts

Every command below ran with cwd `/fast/scratch/hyaku/kotoba-r60/CtlReopenForged`; stderr was empty in all twelve runs. Counter SHA printed by every command is `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.

### pristine

sandbox 18afb8135ad4f95450f584b07b90b373190417c6 (/fast/scratch/hyaku/kotoba-r60/CtlReopenForged)


offline; `date -u`: `Fri Oct 23 12:07:17 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 18afb8135ad4f95450f584b07b90b373190417c6
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 18afb8135ad4f95450f584b07b90b373190417c6
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```


live; `date -u`: `Fri Oct 23 12:07:17 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 18afb8135ad4f95450f584b07b90b373190417c6 --fetch
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 18afb8135ad4f95450f584b07b90b373190417c6
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: (empty)
```

C1 predicate: --fetch exit 0 (F>=TARGET) — MET

### a-missing-prefix

sandbox d680535976ff0c1700d3ff1f5cf7f175e2b78441 (/fast/scratch/hyaku/kotoba-r60/CtlReopenForged)


offline; `date -u`: `Fri Oct 23 12:07:36 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev d680535976ff0c1700d3ff1f5cf7f175e2b78441
scoped rule files backed on committed snapshots 0 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev d680535976ff0c1700d3ff1f5cf7f175e2b78441
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S104: S104 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S105: S105 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```


live; `date -u`: `Fri Oct 23 12:07:36 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev d680535976ff0c1700d3ff1f5cf7f175e2b78441 --fetch
scoped rule files backed on committed snapshots 0 of 3; found on the live page 0 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev d680535976ff0c1700d3ff1f5cf7f175e2b78441
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S104: S104 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S105: S105 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

### b-wrong-base-id

sandbox 76e16614e9c68589b4577d051ef90492e86568a8 (/fast/scratch/hyaku/kotoba-r60/CtlReopenForged)


offline; `date -u`: `Fri Oct 23 12:07:50 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 76e16614e9c68589b4577d051ef90492e86568a8
scoped rule files backed on committed snapshots 0 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 76e16614e9c68589b4577d051ef90492e86568a8
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S104: S104 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S105: S105 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```


live; `date -u`: `Fri Oct 23 12:07:50 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 76e16614e9c68589b4577d051ef90492e86568a8 --fetch
scoped rule files backed on committed snapshots 0 of 3; found on the live page 0 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 76e16614e9c68589b4577d051ef90492e86568a8
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S104: S104 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S105: S105 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

### c-nonbase-id

sandbox 358e43d1d3839158865eb9a8d25bf75852cb7489 (/fast/scratch/hyaku/kotoba-r60/CtlReopenForged)


offline; `date -u`: `Fri Oct 23 12:08:02 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 358e43d1d3839158865eb9a8d25bf75852cb7489
scoped rule files backed on committed snapshots 0 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 358e43d1d3839158865eb9a8d25bf75852cb7489
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S104: S104 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S105: S105 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```


live; `date -u`: `Fri Oct 23 12:08:02 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 358e43d1d3839158865eb9a8d25bf75852cb7489 --fetch
scoped rule files backed on committed snapshots 0 of 3; found on the live page 0 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 358e43d1d3839158865eb9a8d25bf75852cb7489
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S104: S104 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S105: S105 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; re-open names no base row with this URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

### d-copied-base-snapshots

sandbox 7f05968a085ddf9fb9155b0a1047808d616b7b1b (/fast/scratch/hyaku/kotoba-r60/CtlReopenForged)


offline; `date -u`: `Fri Oct 23 12:08:42 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 7f05968a085ddf9fb9155b0a1047808d616b7b1b
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7f05968a085ddf9fb9155b0a1047808d616b7b1b
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```


live; `date -u`: `Fri Oct 23 12:08:42 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 7f05968a085ddf9fb9155b0a1047808d616b7b1b --fetch
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7f05968a085ddf9fb9155b0a1047808d616b7b1b
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: (empty)
```

C1 predicate: --fetch exit 0 (F>=TARGET) — MET

### restored

sandbox 3c8dabfb85017d5a6d4c89fb3e4574fbecf1c227 (/fast/scratch/hyaku/kotoba-r60/CtlReopenForged)


offline; `date -u`: `Fri Oct 23 12:09:02 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 3c8dabfb85017d5a6d4c89fb3e4574fbecf1c227
scoped rule files backed on committed snapshots 3 of 3; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 3c8dabfb85017d5a6d4c89fb3e4574fbecf1c227
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
stderr: (empty)
```


live; `date -u`: `Fri Oct 23 12:09:02 PM UTC 2026`

```text
$ timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 3c8dabfb85017d5a6d4c89fb3e4574fbecf1c227 --fetch
scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 3c8dabfb85017d5a6d4c89fb3e4574fbecf1c227
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 0
stderr: (empty)
```

C1 predicate: --fetch exit 0 (F>=TARGET) — MET

## Before, mutant, and restored hashes

Only `corpus/SOURCES.md` changes in a–c. In d, only it and `S103.page` differ from pristine; the S104/S105 historical copies are byte-identical. Other world files and the counter remain unchanged in every variant. Hashes below were recorded as part of each detector receipt.

| World | corpus/SOURCES.md SHA256 | S103.page SHA256 |
|---|---|---|

| pristine | `355349418cf599cbc448eed0855e66fcff8278885d9490c1c77350e614936bca` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |

| a-missing-prefix | `0b536ba5eececad1a6faeb8095edd1f6191cce3bb796fbb57b0c3314dbec9c4d` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |

| b-wrong-base-id | `93dabe063f4b029e904a6bf2d0998ad4e38f31f33886d91cc5c0ce82be1e33d0` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |

| c-nonbase-id | `6326a2a77600f0d468d013878b4df36d9754126beea1546391696548df1b40a3` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |

| d-copied-base-snapshots | `ef6b7322c5608a35b2b2639402b52fa16e4f7a69f4e85f50d92db3fb2f186302` | `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff` |

| restored | `355349418cf599cbc448eed0855e66fcff8278885d9490c1c77350e614936bca` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |


Exact restoration evidence: every saved pristine world file compared byte-for-byte equal after restoration; all seven comparisons were `true`. The same bounded detector then returned S=3/F=3 and live exit 0 on sandbox 3c8dabfb85017d5a6d4c89fb3e4574fbecf1c227 (/fast/scratch/hyaku/kotoba-r60/CtlReopenForged). Full before/after manifest:

| File | Before SHA256 | Restored SHA256 | Exact bytes equal |
|---|---|---|---|

| `SKILL.md` | `0168a9ee5f4c6c49bfa3d89971e968239b1282c282fa7faa887dc2cae25a9c25` | `0168a9ee5f4c6c49bfa3d89971e968239b1282c282fa7faa887dc2cae25a9c25` | true |

| `corpus/SOURCES.md` | `355349418cf599cbc448eed0855e66fcff8278885d9490c1c77350e614936bca` | `355349418cf599cbc448eed0855e66fcff8278885d9490c1c77350e614936bca` | true |

| `corpus/knowledge/scoped-rules-round60.md` | `0a269522f0e614d06fb259bb3c9a3faaf53ba31f64b09cfa3be62a2fef4ca4c6` | `0a269522f0e614d06fb259bb3c9a3faaf53ba31f64b09cfa3be62a2fef4ca4c6` | true |

| `corpus/lessons/round-60.md` | `74a77415770512ae8325c8eec42307fec510d2347ee8da317bc859ca685ff7d0` | `74a77415770512ae8325c8eec42307fec510d2347ee8da317bc859ca685ff7d0` | true |

| `.ufo/waves/round-60/snapshots/S103.page` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | true |

| `.ufo/waves/round-60/snapshots/S104.page` | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | true |

| `.ufo/waves/round-60/snapshots/S105.page` | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | true |

| `verifiers/check_scoped_rules.py` | `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a` | `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a` | SHA unchanged |


Machine-readable exact-restoration receipt: `/fast/scratch/hyaku/kotoba-r60/CtlReopenForged/control-receipts/restoration.json`. Working world files are restored to pristine, not left on a mutant. The mutant commits and bounded detector receipts remain available in the designated sandbox for the L1 to inspect. No change is proposed or integrated.


Control-d predicate success was messaged immediately to `agent://KotobaR60` after its live result. This report records observations only; judging or redesigning the contract belongs to the L1.
