Result: MIXED — All six mutants survived the frozen exit predicate; (a)–(e) changed its row-level result, while (f) erased all seven schema cells without changing the measurement.

# Q25: C1 content dependence

Axis under attack: depth. This is a mutation-detector finding, not a round judgment or a proposal to change the frozen counter, targets, or row rule.

Sandbox: `/fast/scratch/hyaku/kotoba-r58/MutC1Content`.
Pristine checkout: sandbox 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe (/fast/scratch/hyaku/kotoba-r58/MutC1Content).
Every mutant was committed independently from that pristine checkout, scored, and restored to it before the next mutation. The only lane write by this seat is this report.

Evidence root, abbreviated `E` below: `/fast/scratch/hyaku/kotoba-r58/MutC1Content/.mutation-evidence/`.

## Detector and expected behavior

For pristine, each mutant, and each restoration, the exact bounded behavioral command was:

```sh
timeout 600s python3 -B verifiers/check_command_files.py --rev "$REV" --fetch
```

`$REV` was the full checkout/commit hash labeled for that world below. Commands ran with the sandbox as cwd, `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` removed from the environment, and `TMPDIR` inside `E`. There were 13 detector invocations: one pristine, six mutated, six restored. No self-test, client CLI, paid call, or other agent runtime was invoked.

Frozen predicate: exit 0 iff F >= 4 and G >= 3. K counts well-formed SKILL table tokens, not successful backing. Expected row-level detections were a missing SOURCES row (a), a changed quote (b), a foreign/shared token (c), a missing Gate quote (d), and a forbidden skill token (e). The counter explicitly does not read the schema cells (f): `corpus/knowledge/command-files-round58.md:65-68`.

The executed counter bytes matched the file at the supplied freeze revision exactly (read-only `git show`, exit 0). SHA256, also printed by every detector run:

`aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c`

Evidence: `E/comparison.json`; `E/pristine-sha256.json`; every run receipt's `counter sha256` line. The counter was never edited or stubbed.

## Scores

| World | F | K | G | Exit | Frozen-predicate verdict | Visible in scores/diagnostics? |
|---|---:|---:|---:|---:|---|---|
| Pristine | 6 | 6 | 4 | 0 | Baseline passes | — |
| (a) Delete S093 registry row | 5 | 6 | 3 | 0 | SURVIVED | Yes: Gemini CLI rejected |
| (b) Cursor quote: allow → permit | 5 | 6 | 3 | 0 | SURVIVED | Yes: Cursor rejected |
| (c) Backtick Copilot CLI's Claude folder | 5 | 7 | 3 | 0 | SURVIVED | Yes: Claude Code lost; Copilot still rejected |
| (d) Drop S095's Gate admission line | 5 | 6 | 3 | 0 | SURVIVED | Yes: opencode rejected |
| (e) Claude token → `.claude/skills/` | 5 | 5 | 3 | 0 | SURVIVED | Yes: Claude Code rejected |
| (f) All seven schema cells → `x` | 6 | 6 | 4 | 0 | SURVIVED | No: stdout identical except measured revision |
| Restored after (a) | 6 | 6 | 4 | 0 | Baseline restored | — |
| Restored after (b) | 6 | 6 | 4 | 0 | Baseline restored | — |
| Restored after (c) | 6 | 6 | 4 | 0 | Baseline restored | — |
| Restored after (d) | 6 | 6 | 4 | 0 | Baseline restored | — |
| Restored after (e) | 6 | 6 | 4 | 0 | Baseline restored | — |
| Restored after (f) | 6 | 6 | 4 | 0 | Baseline restored | — |

No mutant was killed by the declared exit predicate. None was inconclusive: pristine and all six restored measurements passed. Do not describe the five diagnostic losses as exit failures: the aggregate target deliberately leaves margin.

### Pristine output

`date -u`: `Fri Oct 23 08:26:58 AM UTC 2026`.

```text
custom command files found on the live page 6 of 6; new ground 4
reject Copilot CLI: SKILL.md command token ':456' is not well-formed; no entry row names the client
exit 0
```

The baseline Copilot token is the first backticked span, its citation `:456`; its Claude command path is plain text. Evidence: `SKILL.md:116`; `E/00-pristine.txt:1-14` (complete command and output).

## Mutants and actual detector output

### (a) Remove the S093 SOURCES row

Commit: sandbox 02b72b951a9d59594274ec0e0635afc2e10610d1 (/fast/scratch/hyaku/kotoba-r58/MutC1Content).

Mutation: delete only pristine `corpus/SOURCES.md:105`; leave the Gemini table row, entry quote, and Gate quote untouched. Expected detector: SOURCES backing rejects Gemini CLI; K is unchanged.

`date -u`: `Fri Oct 23 08:27:41 AM UTC 2026`.

```text
custom command files found on the live page 5 of 6; new ground 3
reject Gemini CLI: entry row S093: S093 absent or malformed in SOURCES.md
exit 0
```

Verdict: SURVIVED the frozen predicate; row-level defect observed. Complete output: `E/a-delete-S093-mutated.txt:1-14`.

### (b) Change the Cursor quote by one word

Commit: sandbox 88f8fc156e959bd1e3378243f745464e3aa56ab7 (/fast/scratch/hyaku/kotoba-r58/MutC1Content).

Mutation: in `corpus/knowledge/command-files-round58.md:39`, replace only `allow` with `permit`; the lesson's original quote is unchanged. Expected detector: changed entry quote no longer appears in Gate. This smallest single-copy mutation tests the backing comparison, not an isolated live-page quote comparison: Cursor is rejected before its page is fetched.

`date -u`: `Fri Oct 23 08:28:02 AM UTC 2026`.

```text
custom command files found on the live page 5 of 6; new ground 3
reject Cursor: entry row S094: round-58 Gate does not record this quote
exit 0
```

Verdict: SURVIVED the frozen predicate; row-level defect observed. Complete output: `E/b-Cursor-one-word-mutated.txt:1-14`.

### (c) Backtick `.claude/commands/` in the Copilot CLI cell

Commit: sandbox 7dcc6dccf90a08dd3fb8f216a906e134b9e30780 (/fast/scratch/hyaku/kotoba-r58/MutC1Content).

Mutation: add only the two backticks around the existing plain-text path in `SKILL.md:116`. Preserve the wording, citation, schema cell and action. Expected detector: the new first backticked span is well-formed (raising K), foreign to Copilot CLI, and shared with Claude Code (disqualifying Claude Code too).

`date -u`: `Fri Oct 23 08:28:17 AM UTC 2026`.

```text
custom command files found on the live page 5 of 7; new ground 3
reject Claude Code: SKILL.md command token '.claude/commands/' is shared by rows Claude Code, Copilot CLI
reject Copilot CLI: SKILL.md command token '.claude/commands/' carries Claude Code's marker 'claude'; SKILL.md command token '.claude/commands/' is shared by rows Claude Code, Copilot CLI; no entry row names the client
exit 0
```

Verdict: SURVIVED the frozen predicate; foreign-name and shared-token guards are observable. Complete output: `E/c-Copilot-backticks-mutated.txt:1-14`.

### (d) Drop S095's line under `## Gate`

Commit: sandbox afb242a44355467a4168279651cf9a5fb8044391 (/fast/scratch/hyaku/kotoba-r58/MutC1Content).

Mutation: delete only pristine `corpus/lessons/round-58.md:15`, the S095 admission/quote line. Keep the `## Gate` heading, other admissions, S095 registry row, and entry quote. Expected detector: the opencode quote lacks its Gate record.

`date -u`: `Fri Oct 23 08:28:28 AM UTC 2026`.

```text
custom command files found on the live page 5 of 6; new ground 3
reject opencode: entry row S095: round-58 Gate does not record this quote
exit 0
```

Verdict: SURVIVED the frozen predicate; row-level defect observed. Complete output: `E/d-drop-S095-Gate-mutated.txt:1-14`.

### (e) Replace Claude Code's token with `.claude/skills/`

Commit: sandbox ac04f177957edc2be57421f454b982981b3e025d (/fast/scratch/hyaku/kotoba-r58/MutC1Content).

Mutation: change only the first backticked token in `SKILL.md:113`; preserve entry, source, Gate and other cells. Expected detector: command grammar rejects the skill token, lowering K; entry-token and quote-token checks also reject it.

`date -u`: `Fri Oct 23 08:28:41 AM UTC 2026`.

```text
custom command files found on the live page 5 of 5; new ground 3
reject Claude Code: SKILL.md command token '.claude/skills/' is not well-formed; entry row S089: entry Command files cell '`.claude/commands/`' is not the SKILL.md token '.claude/skills/'; quote does not hold the command token '.claude/skills/' (case-sensitive)
exit 0
```

Verdict: SURVIVED the frozen predicate; row-level defect observed. Complete output: `E/e-Claude-skills-mutated.txt:1-14`.

### (f) Replace every `What a file sets` cell with `x`

Commit: sandbox b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b (/fast/scratch/hyaku/kotoba-r58/MutC1Content).

Mutation: replace all seven data cells in the `What a file sets` column, `SKILL.md:113-119`, with `x`. Preserve header, client names, command cells, action cells, entry, SOURCES, lesson, and counter. Expected detector: no observation of these cells; unchanged score.

`date -u`: `Fri Oct 23 08:28:58 AM UTC 2026`.

```text
custom command files found on the live page 6 of 6; new ground 4
exit 0
```

Verdict: SURVIVED and invisible to this detector. Complete stdout equals pristine stdout after removing only the `counter rev` line (`E/comparison.json`, `f_stdout_equals_pristine_except_rev: true`). Complete output: `E/f-format-cells-x-mutated.txt:1-14`.

This is the requested coverage finding: the counter does not establish that SKILL.md teaches what a command file sets. All seven such explanations can be erased while keeping F/K/G/exit and every row diagnostic unchanged. The entry itself already discloses this review-only boundary at `corpus/knowledge/command-files-round58.md:65-68`; no frozen-contract change is proposed.

## Before/after hashes and exact restoration

SHA256 of pristine bytes, also the restored SHA256 after every mutant:

| File | Pristine = restored SHA256 |
|---|---|
| `SKILL.md` | `18e0fde1abdb2a7a56e1fdcce18cd04bae4f35d78668ae2485dc36b653f9ada6` |
| `corpus/knowledge/command-files-round58.md` | `f0b554dacc629b5a6e24ff9eac21e69e73eb4dd3e19a83dfa7c6a4c729a9cf7f` |
| `corpus/SOURCES.md` | `41320ab6caba893d8b9655dfa0af11b56c5602964c145a80aabc42d7c72f640f` |
| `corpus/lessons/round-58.md` | `a51f2672cf3a6254b6c91127633afa553d90cf0427c4df7cece810d9ab654824` |
| `verifiers/check_command_files.py` | `aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c` |

| World | Mutated file | Mutated SHA256 |
|---|---|---|
| (a) | `corpus/SOURCES.md` | `4ab0176ddf1becfa654a89bc9e7d3832d1c0a28caa59a022d18b95e167fdb4be` |
| (b) | `corpus/knowledge/command-files-round58.md` | `c8909a8999ef6c5018120fd264d3f03d7bf6594be974afb8dad317d8b4dc4335` |
| (c) | `SKILL.md` | `58934f65b6420b84fba5a979516f8ead6dfaddd9562f0aaa72e7244f60e097af` |
| (d) | `corpus/lessons/round-58.md` | `032619bbb6da1994ba020739dff29b1ddf5a858a7abbcecdb4f6eb0da2d7ca65` |
| (e) | `SKILL.md` | `e5f04c3f00c51912d2f3979f5b485cfce6781dd4e42da2722681a056dbebc26a` |
| (f) | `SKILL.md` | `5b5146b3c9ae6c4145fcbe11a597bed13f601d0994f4ad35b949b29d7dc2464f` |

Each scoring operation used a `finally` restoration (`timeout 30s git -c core.hooksPath=/dev/null checkout -q "$PRISTINE"`, exit 0) followed by comparison of the five files' exact bytes with their saved pristine bytes, not hashes alone. All comparisons were true. The same bounded detector then ran on the restored revision with exit 0 and the original 6/6/4 scores. Final checkout remains pristine; mutant commits and receipts remain only in this sandbox.

| Restoration | Pasted `date -u` line | Complete detector output | Byte comparison evidence |
|---|---|---|---|
| (a) | `Fri Oct 23 08:27:41 AM UTC 2026` | `E/a-delete-S093-restored.txt:1-14` | `E/a-delete-S093-restoration.json` |
| (b) | `Fri Oct 23 08:28:03 AM UTC 2026` | `E/b-Cursor-one-word-restored.txt:1-14` | `E/b-Cursor-one-word-restoration.json` |
| (c) | `Fri Oct 23 08:28:17 AM UTC 2026` | `E/c-Copilot-backticks-restored.txt:1-14` | `E/c-Copilot-backticks-restoration.json` |
| (d) | `Fri Oct 23 08:28:29 AM UTC 2026` | `E/d-drop-S095-Gate-restored.txt:1-14` | `E/d-drop-S095-Gate-restoration.json` |
| (e) | `Fri Oct 23 08:28:41 AM UTC 2026` | `E/e-Claude-skills-restored.txt:1-14` | `E/e-Claude-skills-restoration.json` |
| (f) | `Fri Oct 23 08:28:59 AM UTC 2026` | `E/f-format-cells-x-restored.txt:1-14` | `E/f-format-cells-x-restoration.json` |

Aggregate machine-readable receipts: `E/worlds.json`, `E/restorations.json`, `E/comparison.json`.

## Independent source snapshots

These are ordinary curl fetches recorded separately from the detector runs, not intercepted counter responses. The frozen `--fetch` command performed its own real network requests. No claim is made that curl's separate responses were those exact request instances. All snapshot bodies were retained byte-for-byte, with no stripping, under `E/sources/`.

For each SID/URL below, command (exit 0 in all six cases):

```sh
timeout 45s curl --location --max-time 35 --max-filesize 5242880 --silent --show-error --user-agent kotoba-shokunin-counter/58 --dump-header "$E/sources/$SID.headers" --output "$E/sources/$SID.body" --write-out '%{json}' "$URL"
```

| SID | URL | Pasted `date -u` line | HTTP | Bytes | SHA256 |
|---|---|---|---:|---:|---|
| S089 | https://code.claude.com/docs/en/slash-commands.md | `Fri Oct 23 08:29:26 AM UTC 2026` | 200 | 114542 | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |
| S090 | https://learn.chatgpt.com/docs/custom-prompts.md | `Fri Oct 23 08:29:27 AM UTC 2026` | 200 | 3357 | `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` |
| S091 | https://code.visualstudio.com/docs/agent-customization/prompt-files.md | `Fri Oct 23 08:29:27 AM UTC 2026` | 200 | 13729 | `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685` |
| S093 | https://geminicli.com/docs/cli/custom-commands.md | `Fri Oct 23 08:29:27 AM UTC 2026` | 200 | 12129 | `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872` |
| S094 | https://cursor.com/docs/reference/deeplinks.md | `Fri Oct 23 08:29:27 AM UTC 2026` | 200 | 5972 | `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` |
| S095 | https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx | `Fri Oct 23 08:29:27 AM UTC 2026` | 200 | 7242 | `dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11` |

Evidence: `E/source-receipts.json` and `E/sources/S###.json` contain actual argv, exit code, effective URL, curl metadata, date, size and hash. This seat makes no Q30 silence finding and did not independently reopen S028; its scoped assignment is the six content-dependence mutations, not the other falsify seats' source and no-harm reviews.

Tool installs/updates: none. No pushes, lane code edits, fleet state writes, or sibling sandbox writes.
