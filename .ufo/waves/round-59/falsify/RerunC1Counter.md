Result: HOLDS — the frozen C1 measurement reproduces exactly, and the self-test kills one event-cardinality mutant before exact restoration.

# Scope and isolation

Attacked: the declared C1 measurement, not round admission or the semantic correctness of every Events cell. Axis: depth; supporting evidence: reproducibility and exact restoration. The Events-presence/semantics distinction remains the frozen addendum in `plans/round-59.md:93-98`; this probe does not replace the cell reviewers.

All lane-code execution and mutation occurred only in `/fast/scratch/hyaku/kotoba-r59/RerunC1Counter`. The lane was read-only except for this report. No sibling, fleet-root, lane-index, jj-state, or target changes were made. No pushes were run.

Sandbox creation command (exit 0; stdout and stderr empty):

```sh
timeout 900 bash -c 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/RerunC1Counter && git -C /fast/scratch/hyaku/kotoba-r59/RerunC1Counter checkout -q c63ccc6823e1f6a8577acbb43d19551eadbbee9a'
```

Every detector below used that sandbox as cwd, removed `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` from its environment, and set `TMPDIR=/fast/scratch/hyaku/kotoba-r59/RerunC1Counter/.git` so the self-test's temporary repositories stayed inside this sandbox. Each detector had a 900-second timeout. The three pristine runs were concurrent; mutation and restoration runs were sequential afterward.

# Frozen counter identity and targets

At the measured revision, `verifiers/check_hook_files.py:253-254` contains `TARGET = 4` and `NEW_TARGET = 5`, matching `plans/round-59.md:78-81`. Neither target was mutated.

Executed in the sandbox:

```sh
timeout 900 bash -o pipefail -c 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:verifiers/check_hook_files.py | sha256sum'
```

Stdout:

```text
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -
```

Exit 0. This equals the frozen SHA in `plans/round-59.md:80` and `.ufo/waves/round-59/C1-measure.txt:4`. The pristine working counter had that same SHA before execution; all pristine detector stdout identity lines also printed it.

# Pristine detector outputs

Before each of the following three runs, `timeout 30 date -u` exited 0 and printed:

```text
Fri Oct 23 09:53:04 AM UTC 2026
```

## With live fetch

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a --fetch
```

Stdout:

```text
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
```

Exit 0; stderr empty. All three stdout lines exactly match `.ufo/waves/round-59/C1-measure.txt:7-9`; the exit matches line 11. F=6 meets TARGET=4 and G=6 meets NEW_TARGET=5.

## Without live fetch

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a
```

Stdout:

```text
hook files backed on committed snapshots 6 of 6; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev c63ccc6823e1f6a8577acbb43d19551eadbbee9a
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
```

Exit 1; stderr empty. All three stdout lines exactly match `.ufo/waves/round-59/C1-measure.txt:15-17`; the exit matches line 18. This is the specified non-fetch outcome, not a baseline failure: `plans/round-59.md:55` and counter lines 208-210 explicitly distinguish it from the live predicate.

## Self-test, pristine bytes

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --self-test
```

Stdout:

```text
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71
self-test: 0 failure(s) over 323 assertions
```

Exit 0; stderr empty. This also reproduces the self-test result recorded in `plans/round-59.md:80-81`.

# One mutation probe

Mutant: a one-character off-by-one defect in `events_cell_why`, sandbox `verifiers/check_hook_files.py:718`:

```diff
-    if len(events) < 2:
+    if len(events) < 1:
```

This wrongly admits a single Events identifier. The expected detector was the same bounded `timeout 900 python3 -B verifiers/check_hook_files.py --self-test` on pristine, mutated, and restored bytes. Existing assertions at counter lines 1585-1587 and 2133-2138 check that one Events span fails and is not backed. No test assertions, targets, or lane files were changed.

Before the mutated run, `timeout 30 date -u` exited 0 and printed:

```text
Fri Oct 23 09:54:06 AM UTC 2026
```

Mutated command:

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --self-test
```

Stdout:

```text
counter sha256 84a6e28a763f92545b1c4a87a74390167c10fe6f3517fca00cb117e64226b7f7
FAIL one span does not pass the events cell: got [], expected ['SKILL.md Events cell holds 1 distinct backticked name(s) (need >= 2)']
FAIL an Events cell with one span is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL an Events cell with one span is reported as such: got False, expected True
self-test: 3 failure(s) over 323 assertions
```

Exit 1; stderr empty. Verdict: **KILLED**. The pristine detector passed, so this is not an inconclusive baseline failure. Exact correction: restore the frozen `< 2` comparison; that restoration was applied only in the sandbox. This does not propose a contract change.

## Restored detector and byte evidence

Before the restored run, `timeout 30 date -u` exited 0 and printed:

```text
Fri Oct 23 09:54:30 AM UTC 2026
```

Restored command:

```sh
timeout 900 python3 -B verifiers/check_hook_files.py --self-test
```

Stdout:

```text
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71
self-test: 0 failure(s) over 323 assertions
```

Exit 0; stderr empty.

| Counter state | SHA256 | Self-test exit |
|---|---|---|
| Before mutation / pristine | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` | 0 |
| Mutated | `84a6e28a763f92545b1c4a87a74390167c10fe6f3517fca00cb117e64226b7f7` | 1 |
| After restoration | `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` | 0 |

Restoration used the inverse surgical edit. A subsequent `timeout 900 git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:verifiers/check_hook_files.py` exited 0 with empty stderr. Comparing its captured bytes directly to the restored sandbox file returned `True`; SHA comparisons to both the pre-mutation and frozen digests also returned `True`.

# Supplemental ordinary-curl source-access record

The pristine counter stdout does not expose per-request body sizes or hashes. These are separately observed ordinary-curl GETs at the times below, **not retroactive telemetry from the earlier counter run**. No browser, challenge solver, client CLI, or paid model call was used. At most three GETs were concurrent.

Each URL below was passed as the final argument to this command, using the frozen counter's User-Agent and Accept values (`verifiers/check_hook_files.py:316-319,1065-1068`):

```sh
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
timeout 60 curl -sSL --max-time 30 -A "$UA" -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '\n%{http_code} %{url_effective}' "$URL"
```

Every curl exited 0, had empty stderr, and returned HTTP 200 with effective URL identical to its requested URL. Body byte counts and SHA256 values exclude only curl's appended write-out trailer (the separating newline plus status/effective-URL text), not any fetched body bytes. Each quotation below is a byte-exact substring at the stated fetched-body line; no Markdown bytes were stripped.

For S096, S097, S098, and S099, `timeout 30 date -u` immediately before each GET exited 0 and printed:

```text
Fri Oct 23 09:55:01 AM UTC 2026
```

For S100 and S101, it exited 0 and printed:

```text
Fri Oct 23 09:55:02 AM UTC 2026
```

| Row | Requested / effective URL | HTTP | Body bytes | Body SHA256 | Verbatim substring and fetched line |
|---|---|---|---|---|---|
| S096 | https://code.claude.com/docs/en/hooks.md | 200 | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` | `.claude/settings.json`, line 243 |
| S097 | https://learn.chatgpt.com/docs/hooks.md | 200 | 47133 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` | `~/.codex/hooks.json`, line 44 |
| S098 | https://code.visualstudio.com/docs/agent-customization/hooks.md | 200 | 15152 | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` | `.github/hooks/`, line 59 |
| S099 | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 200 | 8428 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` | `~/.copilot/hooks/`, line 28 |
| S100 | https://geminicli.com/docs/hooks/best-practices.md | 200 | 17650 | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` | `.gemini/settings.json`, line 379 |
| S101 | https://cursor.com/docs/hooks | 200 | 69145 | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` | `.cursor/hooks.json`, line 50 |

These supplemental body sizes and digests match the measured revision's `corpus/SOURCES.md:108-113`. This observation makes no independent ruling on every event's semantics.

# Comparison and no-harm after-column

The captured-run/receipt comparison returned:

```text
fetch stdout exactly matches receipt lines 7-9: True
fetch exit matches receipt line 11: True
committed-only stdout exactly matches receipt lines 15-17: True
committed-only exit matches receipt line 18: True
self-test pristine/mutated/restored exits: [0, 1, 0]
all detector stderr streams empty: True
all supplementary fetches HTTP 200 and curl exit 0: True
```

| Surface | Before | After |
|---|---|---|
| Declared live measurement | Receipt: backed 6/6, found 6/6, new ground 6; exit 0 | Independent pristine run identical; no measurement correction needed |
| Committed-only measurement | Receipt: backed 6/6, live not run, new ground 0; exit 1 | Independent pristine run identical |
| Counter identity | Frozen SHA `f695d59e…` | Full SHA and direct byte equality restored |
| One-span defect detection | Pristine self-test exit 0 | Mutant exit 1 with three named failures; restored exit 0 |
| Lane contract and content | Read-only assignment | No code/content/target changes; only this report written |

No broader no-harm or round-admission judgment is claimed. No tools were installed or updated; operator rules were read before execution.

Report: .ufo/waves/round-59/falsify/RerunC1Counter.md
