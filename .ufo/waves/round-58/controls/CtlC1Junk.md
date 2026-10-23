Result: HOLDS — both junk worlds score F=0 and G=0 with the unchanged committed C1 counter, including the variant with K=7.

## Counterexample and scope

Attempted shortcut: add seven invented or misassigned command locations, meaningless file-setting cells (`banana`), three-word junk action cells (`Banana banana banana`), matching knowledge-entry location cells, seven new SOURCES rows on the respective clients' pinned documentation hosts, and real page quotations repeated in the lesson Gate. None of the seven cited pages contains its assigned junk token or normalized form. No reusable command-location knowledge was supplied.

- W1: sandbox a6dae8c45a4d7c5f3f50c2822db4b633003f37e2 (/fast/scratch/hyaku/kotoba-r58/CtlC1Junk).
- W2: sandbox 22669956159b03b81dac2dee2da924e08ee9e21a (/fast/scratch/hyaku/kotoba-r58/CtlC1Junk). This stronger variant changes only Copilot CLI's location in the SKILL and entry tables, making all seven tokens grammar-eligible while leaving all prose and source quotes junk/unrelated.

All command/output revision hashes in each run below refer to the labelled sandbox commit in that run's heading. Neither commit is a lane commit; neither was pushed.

| Client | W1 token | W2 token |
|---|---|---|
| Claude Code | `.x/commands` | unchanged |
| Codex | `.github/prompts/` | unchanged |
| VS Code | `.config/commands/` | unchanged |
| Copilot CLI | `./.commands/` | `.commands/commands/` |
| Gemini CLI | `.docs/prompt.md` | unchanged |
| Cursor | `.cmd/prompts` | unchanged |
| opencode | `.junk/commands/` | unchanged |

`.github/prompts/` is deliberately assigned to Codex, not VS Code: it is not claimed to be nonexistent for every client. The Codex page contains neither spelling. W1's `./.commands/` fails the two-segment grammar after stripping `./`; W2 removes that easy failure.

Evidence in either sandbox commit: `SKILL.md:125-135`, `corpus/knowledge/command-files-round58.md:5-13`, `corpus/SOURCES.md:102-108`, and `corpus/lessons/round-58.md:3-11`. The raw fetched source bodies are committed under `control-evidence/fetches/` in both sandbox worlds.

## Frozen counter custody

Clone/setup command, exit 0, no output:

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
timeout 120 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/CtlC1Junk
timeout 120 git -C /fast/scratch/hyaku/kotoba-r58/CtlC1Junk checkout -q 3de87aad29e960c95ed35840442f424c48c29729
```

The assignment's initial `TARGET/NEW_TARGET=None` sentence was stale; L1 confirmed the correction by message. The actual file at `3de87aad29e960c95ed35840442f424c48c29729` has `TARGET = 4` and `NEW_TARGET = 3` at `verifiers/check_command_files.py:246-247`. Its predicate is exit 0 iff F>=4 and G>=3 with `--fetch`. The exact committed counter was used unchanged. Every scored run prints the same counter sha256 as the pre-world checkout.

Command at that checkout, exit 0:

```sh
timeout 30 sha256sum verifiers/check_*.py
```

Full output:

```text
2f672bd155a4c125caa7e1758e06137b72ede4caec75d4e67baeee227bbe6c47  verifiers/check_agent_definitions.py
8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe  verifiers/check_agentdef_boxes.py
7d989ed4ae85375ffd3c5786543b810b93820e823132ec1da104f18e8eb19f47  verifiers/check_alwayson_boxes.py
a17c310319c1ed13a44b2878c111de09bfa9f21e0f02cb1fe14f37e81ddd3663  verifiers/check_assertion_floors.py
30a17b8f83fa2fb716655e6b32aabe8d94b44ef4c2ca700ce7340ccae955f962  verifiers/check_callee_rename.py
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18  verifiers/check_correction_sweep.py
a6844d7261b391af3f1659ee70913e3146a65cb420419aa7b4a936801546d72b  verifiers/check_could_not_evaluate.py
15fdf83b30ddb0c68bf694a7d607a59dd80f685ba1d7750487f48d4b602fe186  verifiers/check_description_thresholds.py
e13eb88d8cfc32fc8975968280aa5a0055416fb07e43facbf1f585d951787e5a  verifiers/check_explicit_invocation.py
71bd4e90b3c50d368efff108c78dd5b9c04641002f7f2109eafe73d59df6c9e0  verifiers/check_gate_finding_delta.py
01b8ad1b1a2d9f7568dc6b970cd5c9ec621bf58af411973f001fa3ad0c35ddce  verifiers/check_gate_registry.py
b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac  verifiers/check_infoless_fences.py
8e04e8fc3eae12789ee1db42b0ef593f583f107e61dc54fe465ea52238838cae  verifiers/check_mcp_instructions.py
5cff0fedd41f05698edbb38866fd556718bd6ad1f67c08b5f313d38d0d1bec1b  verifiers/check_opencode_repin.py
f1b3890c3e1750b2719afd24586d38dd81b3e1e1c70ada6ae585211b0f0a2656  verifiers/check_overlap_levers.py
bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e  verifiers/check_plugin_manifests.py
2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7  verifiers/check_sibling_census.py
9f18f00ce488d687362cfa3e16df8f4fec56da9e580423a83d2bad6283998bd3  verifiers/check_sources_append_only.py
9615d5476ca1d8031880aca92c137526e989ce13d69298379b9dc95a2067e4ee  verifiers/check_substrate_pins.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
```

## Scores: every counter run

All runs used cwd `/fast/scratch/hyaku/kotoba-r58/CtlC1Junk`. No self-tests, extra judge, or alternative runtime was invoked.

| World | Mode | F | K | G | Backed | Exit |
|---|---|---|---|---|---|---|
| W1 | `--fetch` | 0 | 6 | 0 | 0 | 1 |
| W1 | no `--fetch` | not measured | 6 | not computed | 0 | 1 |
| W2 | `--fetch` | 0 | 7 | 0 | 0 | 1 |
| W2 | no `--fetch` | not measured | 7 | not computed | 0 | 1 |

### W1 — sandbox a6dae8c45a4d7c5f3f50c2822db4b633003f37e2 (/fast/scratch/hyaku/kotoba-r58/CtlC1Junk), with fetch

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev a6dae8c45a4d7c5f3f50c2822db4b633003f37e2 --fetch
```

Full output; exit 1:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev a6dae8c45a4d7c5f3f50c2822db4b633003f37e2
custom command files found on the live page 0 of 6; new ground 0
reject Claude Code: entry row S089: quote does not hold the command token '.x/commands' (case-sensitive)
reject Codex: entry row S090: quote does not hold the command token '.github/prompts/' (case-sensitive)
reject VS Code: entry row S091: quote does not hold the command token '.config/commands/' (case-sensitive)
reject Copilot CLI: SKILL.md command token './.commands/' is not well-formed; entry row S092: quote does not hold the command token './.commands/' (case-sensitive)
reject Gemini CLI: entry row S093: quote does not hold the command token '.docs/prompt.md' (case-sensitive)
reject Cursor: entry row S094: quote does not hold the command token '.cmd/prompts' (case-sensitive)
reject opencode: entry row S095: quote does not hold the command token '.junk/commands/' (case-sensitive)
exit code 1
```

### W1 — sandbox a6dae8c45a4d7c5f3f50c2822db4b633003f37e2 (/fast/scratch/hyaku/kotoba-r58/CtlC1Junk), without fetch

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev a6dae8c45a4d7c5f3f50c2822db4b633003f37e2
```

Full output; exit 1:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev a6dae8c45a4d7c5f3f50c2822db4b633003f37e2
custom command files backed 0 of 6; new ground not computed (needs --fetch)
reject Claude Code: entry row S089: quote does not hold the command token '.x/commands' (case-sensitive)
reject Codex: entry row S090: quote does not hold the command token '.github/prompts/' (case-sensitive)
reject VS Code: entry row S091: quote does not hold the command token '.config/commands/' (case-sensitive)
reject Copilot CLI: SKILL.md command token './.commands/' is not well-formed; entry row S092: quote does not hold the command token './.commands/' (case-sensitive)
reject Gemini CLI: entry row S093: quote does not hold the command token '.docs/prompt.md' (case-sensitive)
reject Cursor: entry row S094: quote does not hold the command token '.cmd/prompts' (case-sensitive)
reject opencode: entry row S095: quote does not hold the command token '.junk/commands/' (case-sensitive)
exit code 1
```

### W2 — sandbox 22669956159b03b81dac2dee2da924e08ee9e21a (/fast/scratch/hyaku/kotoba-r58/CtlC1Junk), with fetch

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev 22669956159b03b81dac2dee2da924e08ee9e21a --fetch
```

Full output; exit 1:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 22669956159b03b81dac2dee2da924e08ee9e21a
custom command files found on the live page 0 of 7; new ground 0
reject Claude Code: entry row S089: quote does not hold the command token '.x/commands' (case-sensitive)
reject Codex: entry row S090: quote does not hold the command token '.github/prompts/' (case-sensitive)
reject VS Code: entry row S091: quote does not hold the command token '.config/commands/' (case-sensitive)
reject Copilot CLI: entry row S092: quote does not hold the command token '.commands/commands/' (case-sensitive)
reject Gemini CLI: entry row S093: quote does not hold the command token '.docs/prompt.md' (case-sensitive)
reject Cursor: entry row S094: quote does not hold the command token '.cmd/prompts' (case-sensitive)
reject opencode: entry row S095: quote does not hold the command token '.junk/commands/' (case-sensitive)
exit code 1
```

### W2 — sandbox 22669956159b03b81dac2dee2da924e08ee9e21a (/fast/scratch/hyaku/kotoba-r58/CtlC1Junk), without fetch

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev 22669956159b03b81dac2dee2da924e08ee9e21a
```

Full output; exit 1:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 22669956159b03b81dac2dee2da924e08ee9e21a
custom command files backed 0 of 7; new ground not computed (needs --fetch)
reject Claude Code: entry row S089: quote does not hold the command token '.x/commands' (case-sensitive)
reject Codex: entry row S090: quote does not hold the command token '.github/prompts/' (case-sensitive)
reject VS Code: entry row S091: quote does not hold the command token '.config/commands/' (case-sensitive)
reject Copilot CLI: entry row S092: quote does not hold the command token '.commands/commands/' (case-sensitive)
reject Gemini CLI: entry row S093: quote does not hold the command token '.docs/prompt.md' (case-sensitive)
reject Cursor: entry row S094: quote does not hold the command token '.cmd/prompts' (case-sensitive)
reject opencode: entry row S095: quote does not hold the command token '.junk/commands/' (case-sensitive)
exit code 1
```

## Source evidence: real quotations, wrong locations

All seven independent ordinary curl fetches exited 0, returned HTTP 200, and had effective URL equal to the requested URL. No browser, access-control workaround, client CLI, or paid model call was used. These fetches establish quote provenance; the counter itself fetches only backed rows (`verifiers/check_command_files.py:1920-1932`), so these zero-backed control runs do not exercise its HTTP fetch loop.

The `date -u` lines immediately before the fetch commands were:

```text
T1: Fri 23 Oct 2026 07:55:35 AM UTC
T2: Fri 23 Oct 2026 07:55:51 AM UTC
```

For each row, the command was the following, with its literal URL and raw path substituted; each exit was recorded as 0:

```sh
date -u
timeout 90 curl --max-time 80 -sS -L <URL> -o <raw-path> -w "url_effective %{url_effective}\nhttp_code %{http_code}\nsize_download %{size_download}\n"
timeout 30 wc -c <raw-path>
timeout 30 sha256sum <raw-path>
```

Raw paths below are relative to `/fast/scratch/hyaku/kotoba-r58/CtlC1Junk/control-evidence/fetches/`.

| Row / time | URL (HTTP 200; curl exit 0) | Raw file:line | Bytes | sha256 |
|---|---|---|---|---|
| S089 / T1 | https://code.claude.com/docs/en/slash-commands.md | `claude.md:7` | 114542 | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |
| S090 / T1 | https://learn.chatgpt.com/docs/custom-prompts.md | `codex.md:38` | 3357 | `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` |
| S091 / T1 | https://code.visualstudio.com/docs/agent-customization/prompt-files.md | `vscode.md:5` | 13729 | `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685` |
| S092 / T2 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview.md | `copilot.md:15` | 4304 | `38f2e097044641c32451491df4bbe4b7e232969fe50558aa3bb4fda2ac79189b` |
| S093 / T2 | https://geminicli.com/docs/cli/custom-commands.md | `gemini.md:10` | 12129 | `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872` |
| S094 / T2 | https://cursor.com/docs/reference/deeplinks.md | `cursor.md:3` | 5972 | `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` |
| S095 / T2 | https://opencode.ai/v2/docs/commands/ | `opencode.html:73` | 32304 | `32591ac3db0056fdbf3b5e20b78e70514da0d7306707cbf7c412ca19276640e0` |

Each quote is a contiguous, byte-exact substring of the specified fetched line, with no internal byte deletion or whitespace shaping. The Claude quote excludes the leading two bytes `> `; the opencode quote excludes the enclosing `<p>` and `</p>` tags (three and four bytes). No other Markdown stripping was performed.

- S089, 18 words: "Create, manage, and share skills to extend Claude's capabilities in Claude Code. Includes custom commands and bundled skills."
- S090, 13 words: "Codex reads prompt metadata and resolves placeholders the next time the session starts."
- S091, 22 words: "Prompt files simplify prompting for common tasks by encoding them as standalone Markdown files that you invoke as slash commands in chat."
- S092, 16 words: "Hooks let you run your own shell commands at key points during a Copilot CLI session."
- S093, 12 words: "Gemini CLI discovers commands from two locations, loaded in a specific order:"
- S094, 20 words: "Deeplinks allow you to share prompts, commands, and rules with others, enabling collaboration and knowledge sharing across teams and communities."
- S095, 17 words: "Add YAML frontmatter when the command needs metadata. The trimmed Markdown body is always the prompt template."

A case-sensitive tool grep over all seven fetched bodies for the junk spellings and normalized forms returned only `vscode.md:25: | Workspace | `.github/prompts` folder |`. That is a different row's page, not Codex's cited page. A separate grep for `\.github/prompts` in `codex.md` returned `No matches found`; a separate grep for `\.x/commands` in `claude.md` also returned `No matches found`. The combined search included `\.commands`, which covers both Copilot variants, and all other assigned tokens. This is a bounded observation about these fetched bodies, not a claim that any client is silent about the command-file topic.

## Interpretation, axes, smallest safe correction

- **No FINDING:** neither control reaches F>=4 and G>=3, nor a high F/G. K=6 or K=7 is only grammar eligibility, not claimed learning.
- **Evidence of discrimination:** all seven W2 rejections are solely `quote does not hold the command token`; the token-to-quote conjunct at `verifiers/check_command_files.py:700-706` rejects real-but-unrelated provenance before live-page credit. W1 additionally rejects the malformed one-segment token.
- **Impacted axes if the shortcut had worked:** C1 depth and provenance fidelity; operability of the counter as an instrument. No impact demonstrated by these worlds. No axis score or canonical admission judgment was made.
- **Smallest safe correction:** none indicated by this control. Preserve the token-in-quote requirement and do not turn grammar count K into evidence credit. These results do not establish semantic quality of action cells or correctness of all possible live-page contexts.

Only the assigned report was written in the lane. All world edits, Git writes, source downloads, and counter executions occurred in the isolated sandbox clone. No lane Git index or jj state was mutated. No tools were installed or updated.
