Result: HOLDS — none of 13 sandbox worlds reached F >= 4 and G >= 3; an IDE-only page nevertheless produced one false Copilot CLI count (F=1, K=1, G=0).

## Scope, axes, and custody

Assigned review only: C1 labels, shared tokens, foreign markers, exact entry cells, and reused base URLs. Axes: depth, client identity, source/provenance fidelity, and counter discrimination/new ground. No admission, integration, canonical judgment, C2 scoring, or other runtime was invoked. No tools installed or updated.

All executable work ran in `/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel`. Only this report was written in the lane. The counter was never edited. Worlds are immutable Git commits built from `3de87aad29e960c95ed35840442f424c48c29729` with Git object/index plumbing; tracked working-tree files remain at that revision. Each world's four replacement documents are sandbox fixture data, not proposed lane content. Objects are retained at `refs/sandbox/round58/<world-name>` in this clone.

Setup (exit 0, no stdout):

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; timeout 900 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel && timeout 900 git -C /fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel checkout -q 3de87aad29e960c95ed35840442f424c48c29729
```

The assignment context's `None` targets were stale. `git show` at the named commit and the frozen file's lines 246–247 establish `TARGET=4`, `NEW_TARGET=3`; L1 explicitly confirmed this during the review. Every observed score below used those committed bytes, unchanged. All 26 counter invocations exited 1, not the unfrozen-target exit 2.

## Counterexample and smallest safe correction

### 1. Numerical shortcut guards held; this is not an unconditional provenance endorsement

Shared VS Code/Copilot tokens rejected both rows, including case/prefix aliases and an unrecognized misspelled sharing partner. The foreign Cursor token was rejected without needing another Claude row. All seven misspellings and all six duplicated SKILL labels were rejected. All six case-only entry mismatches and all six added-slash mismatches were rejected. Both literal and normalized-alias re-citations of a base URL were rejected. Their maximum F and G were zero.

Evidence: full outputs below; frozen counter `shared_tokens` at `verifiers/check_command_files.py:666-675`, exact-name/duplicate handling at `:759-784`, foreign-marker handling at `:592-598`, E4 at `:660-663`, base-URL rejection at `:729-730`. K is a grammar/unique-label denominator, not a count of backed rows: shared, foreign, and E4-invalid rows can remain in K. Missing clients in the narrow worlds are deliberately absent and their exact rejection messages are preserved below.

No correction to those tested guards is supported by these runs.

### 2. Fixable low-count provenance defect: removing the VS Code label makes IDE documentation count as Copilot CLI

Counterexample: sandbox 9093047e690c030d1d85228799afae0fbe8fbe6e (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel), `a_copilot_only_offtopic`. It writes one Copilot CLI row using `.github/prompts/` and cites a genuine GitHub prompt-file tutorial. With VS Code also present, E5 rejects both; removing VS Code changes the same Copilot row to BACKED and FOUND, F=1/K=1/G=0. The full fetch and non-fetch outputs are pasted below, both exit 1. This is a row-level false attribution, not a predicate/high-count break.

Evidence: the world's `SKILL.md:7`, entry `corpus/knowledge/command-files-round58.md:5`, and `corpus/SOURCES.md:5`; fetched `fetch-github.md:47` is the genuine path sentence. The same fetched page at `:7` and `:15` explicitly says:

> Prompt files are only available in VS Code, Visual Studio, and JetBrains IDEs.

That is a 14-word, byte-exact substring; no Markdown bytes stripped. The counter's pinned-host check (`:731-732`) proves vendor-host membership, not product identity. Its own `What a file sets`/`Action` cells in this sandbox expressly call the file an incorrectly relabelled IDE prompt; they are not hidden by the control.

Impacted axes: client identity, source fidelity/provenance, and depth. Smallest safe correction for current content: do not admit this as a Copilot CLI row; require source evidence specifically establishing a CLI reusable-command-file location. A future counter revision could bind this client to CLI-specific documentation routes plus positive and negative product-identity fixtures. That would be a new measurement, not a permitted edit to this frozen counter. The Rust judge remains the sole authority on admission; these runs do not certify the seven-row table.

### 3. Explicit tradeoffs, not demonstrated predicate bypasses

- Removing `./` and a trailing slash in an entry is expressly allowed by `normalise()`. Sandbox d567a698a60630c36f970f1bceeb48ab395acc69 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel) scores F=1/K=1/G=1 for the genuine Cursor row. Adding a slash when the SKILL token has none is not that operation and was rejected across six clients.
- Duplicate entry labels are not duplicate SKILL labels. Sandbox 0ccd7e5848e6daedb859f1e803914cb6d9bcafb8 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel) has an invalid Cursor entry first and a valid Cursor entry second; the latter is selected, F=1/K=1/G=1. `judge` tries entries until one passes at `:785-795`. The frozen contract requires exactly one SKILL row, not exactly one entry row. Reviewers must not infer that every entry is consistent merely because one backs a client. An entry-uniqueness rule, if desired, is a contract change and a second measurement.

## Score summary

All rows below have fetch exit 1 and non-fetch exit 1. `B` is the non-fetch backed count. G is not computed by the non-fetch mode.

| World | F | K | G | B | What rejected the targeted rows / why a row counted |
|---|---:|---:|---:|---:|---|
| a_shared_exact | 0 | 2 | 0 | 0 | E5: both VS Code and Copilot CLI share `.github/prompts/` |
| a_shared_alias_misspelled | 0 | 1 | 0 | 0 | VS Code poisoned by casefold(normalise) sharing with `Copilot CLl`; canonical Copilot CLI absent |
| a_copilot_only_offtopic | 1 | 1 | 0 | 1 | Copilot CLI falsely counted from IDE-only GitHub page; token held at base |
| b_foreign_marker | 0 | 1 | 0 | 0 | Cursor carries Claude Code marker `claude`; no sharing row needed |
| c_misspelled_names | 0 | 0 | 0 | 0 | Each canonical client has zero SKILL rows despite its canonical entry |
| c_duplicated_skill_names | 0 | 0 | 0 | 0 | Each of six clients has two SKILL rows; Copilot CLI absent |
| d_entry_case_mismatch | 0 | 6 | 0 | 0 | E4 for every one of six case-only mismatches |
| d_entry_added_slash | 0 | 6 | 0 | 0 | E4 for every one of six added-slash mismatches |
| d_entry_allowed_normalisation | 1 | 1 | 1 | 1 | Genuine Cursor row; entry equals normalise(raw token), as allowed |
| e_reused_base_url (initial fixture) | 0 | 1 | 0 | 0 | Both entries accidentally share S907 alias data; alias base URL rejected twice |
| c_duplicate_entry_names (initial fixture) | 0 | 1 | 0 | 0 | Both entries accidentally share the bad cell; E4 rejected twice |
| e_reused_base_url_corrected | 0 | 1 | 0 | 0 | Both S900 literal and S907 normalized-alias base URL independently rejected |
| c_duplicate_entry_names_corrected | 1 | 1 | 1 | 1 | Valid second entry selected; invalid first entry does not disqualify client |

Fixture honesty: `deepcopy([same_dict, same_dict])` preserves the shared reference. That made the two initial E/duplicate-entry fixtures narrower than their descriptions. Their actual outputs are retained, not relabelled as the intended controls. I corrected only the sandbox builder to allocate independent dictionaries and ran only the two corrected worlds. The counter was not changed. No numerical conclusion relies on the erroneous fixture descriptions.

Builder commands (both exit 0; their complete counter outputs are pasted below):

```sh
timeout 900 python3 -B build_label_worlds.py
timeout 900 python3 -B build_label_worlds.py e_reused_base_url_corrected c_duplicate_entry_names_corrected
```

Reproduction artifacts in the clone: `build_label_worlds.py`, `control-worlds.json`, `control-worlds-corrections.json`, `control-runs.txt`, `control-runs-corrections.txt`, and one `<world>-fetch.log` / `<world>-no-fetch.log` per world. The builder never imports, patches, or stubs the counter; it invokes the exact requested command surface for each commit.

## Frozen hashes

At checkout `3de87aad29e960c95ed35840442f424c48c29729`, command `timeout 30 sha256sum verifiers/check_*.py`, exit 0, full output:

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

Read-only `git ls-tree` at that commit (exit 0) also gave:

```text
100755 blob 2efd8b5e92ba62c176d10922d84fb4fdb6a5ee4e	verifiers/check_command_files.py
100755 blob be7c508b4448b61539c6bb787ae6369dbe61f124	verifiers/check_sweep_mutants.py
```

Each scoring invocation below independently printed the same C1 counter sha256. No counter self-test, build, lint, unrelated check, or paid model/client call was run.

## Source access and exact quotations

Only ordinary curl/HTTP and web search were used. No headless browser, challenge bypass, or access-control workaround. All fetched bodies and headers remain in the clone. No client is claimed silent, so no Q30 absence conclusion is made. Metadata includes unused supporting fetches as well as the pages used in fixtures.

Each fetch command below exited 0. Its `date -u` output is recorded verbatim in the table. The command template was:

```sh
timeout 5 date -u && timeout 120 curl --max-time 90 -sSL -D <headers> -o <body> -w 'HTTP %{http_code}\nbytes %{size_download}\neffective %{url_effective}\n' <URL> && timeout 10 sha256sum <body>
```

The opencode fetch additionally supplied `-H 'Accept: text/markdown'` before `-D`. All effective URLs equalled the listed URL. The hashes below are the complete observed sha256, not shortened identifiers.

| Body / headers | URL | date -u | HTTP | Bytes | sha256 |
|---|---|---|---:|---:|---|
| `fetch-vscode.md` / `fetch-vscode.headers` | [https://code.visualstudio.com/docs/agent-customization/prompt-files.md](https://code.visualstudio.com/docs/agent-customization/prompt-files.md) | `Fri 23 Oct 2026 07:56:07 AM UTC` | 200 | 13729 | `4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685` |
| `fetch-github.md` / `fetch-github.headers` | [https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file.md](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/your-first-prompt-file.md) | `Fri 23 Oct 2026 07:56:07 AM UTC` | 200 | 3039 | `117468ccb3abe5d07ae8f76a309f291b0fb93dae6d06de789feb9b90aa87b0ed` |
| `fetch-cursor.md` / `fetch-cursor.headers` | [https://cursor.com/docs/reference/deeplinks.md](https://cursor.com/docs/reference/deeplinks.md) | `Fri 23 Oct 2026 07:56:07 AM UTC` | 200 | 5972 | `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` |
| `fetch-claude-base.md` / `fetch-claude-base.headers` | [https://code.claude.com/docs/en/skills.md](https://code.claude.com/docs/en/skills.md) | `Fri 23 Oct 2026 07:56:07 AM UTC` | 200 | 114542 | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |
| `fetch-vscode-migrate.md` / `fetch-vscode-migrate.headers` | [https://code.visualstudio.com/docs/agent-customization/migrate-customizations.md](https://code.visualstudio.com/docs/agent-customization/migrate-customizations.md) | `Fri 23 Oct 2026 07:56:42 AM UTC` | 200 | 59037 | `a671708e4247448a8128000d5ef3b7c4ebbef15a81d7feccd74d486c1b64941a` |
| `fetch-claude-commands.md` / `fetch-claude.commands.headers` | [https://code.claude.com/docs/en/slash-commands.md](https://code.claude.com/docs/en/slash-commands.md) | `Fri 23 Oct 2026 07:56:42 AM UTC` | 200 | 114542 | `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` |
| `fetch-vscode-overview.md` / `fetch-vscode-overview.headers` | [https://code.visualstudio.com/docs/agent-customization/overview.md](https://code.visualstudio.com/docs/agent-customization/overview.md) | `Fri 23 Oct 2026 07:57:24 AM UTC` | 200 | 18157 | `885f054a49d12863f0579de39e54ba0b0953de18e46a5a2e566d6cd46c0a4315` |
| `fetch-vscode-learn.md` / `fetch-vscode-learn.headers` | [https://code.visualstudio.com/learn/customizations/6-prompt-files.md](https://code.visualstudio.com/learn/customizations/6-prompt-files.md) | `Fri 23 Oct 2026 07:57:24 AM UTC` | 200 | 5531 | `780968575728a76a0c623ec6bb501997ab8f8470b4587519c3114c2a99cfc589` |
| `fetch-vscode-guide.md` / `fetch-vscode-guide.headers` | [https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/guides/context-engineering-guide.md](https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agents/guides/context-engineering-guide.md) | `Fri 23 Oct 2026 07:58:43 AM UTC` | 200 | 21465 | `fa7bf4bc323730590750800e12bd4cc33c6dde4b55d477d0040425edc39c5d4b` |
| `fetch-gemini.md` / `fetch-gemini.headers` | [https://geminicli.com/docs/cli/custom-commands.md](https://geminicli.com/docs/cli/custom-commands.md) | `Fri 23 Oct 2026 07:58:43 AM UTC` | 200 | 12129 | `8f3295e8ca502b0c70bb3bf672f0dc0130ecb868fad4a88d5cac0f36ac6f3872` |
| `fetch-opencode.md` / `fetch-opencode.headers` | [https://opencode.ai/v2/docs/commands/](https://opencode.ai/v2/docs/commands/) | `Fri 23 Oct 2026 07:58:43 AM UTC` | 200 | 7220 | `c3dc75fc48071613c359126e7d84e2298afd10c4b83aac83383e94a1489a23dc` |
| `fetch-codex.md` / `fetch-codex.headers` | [https://learn.chatgpt.com/docs/custom-prompts.md](https://learn.chatgpt.com/docs/custom-prompts.md) | `Fri 23 Oct 2026 07:59:05 AM UTC` | 200 | 3357 | `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` |


All fixture quotations below are contiguous byte-exact substrings in the fetched bytes; no Markdown characters were stripped when storing the quotes. Each quotation is at most 25 whitespace-separated words. The counter's own matching normalization is not a claim that the source bytes were altered.

- `fetch-claude-base.md:172` and `fetch-claude-commands.md:172`:

  ```text
  **Command files**: a Markdown file in `.claude/commands/` is the older format and still works.
  ```

- `fetch-codex.md:62`:

  ```text
  Manage prompts by editing or deleting files under `~/.codex/prompts/`.
  ```

- `fetch-vscode-guide.md:170`:

  ```text
  Optionally, create a [prompt file](/docs/agent-customization/prompt-files.md) `.github/prompts/plan-qna.prompt.md` that invokes the **Plan** agent
  ```

  The SKILL token `.github/prompts/` is the directory prefix of the documented file example. The frozen boundary rule allows the normalized token followed by `/`. This avoids the pipe-containing location-table quotation in the census; no pipe or Markdown bytes were fabricated or escaped to get through the entry-table parser.

- `fetch-github.md:47`:

  ```text
  Save the prompt file above as `explain-code.prompt.md` in your `.github/prompts` folder.
  ```

- `fetch-gemini.md:12`:

  ```text
  **User commands (global):** Located in `~/.gemini/commands/`. These commands
  ```

- `fetch-cursor.md:54`:

  ```text
  Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory.
  ```

- `fetch-opencode.md:19`:

  ```text
  Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`.
  ```

The foreign-marker world deliberately copies the genuine Claude quote into the Cursor entry and attributes it to the Cursor URL. This is labelled fabricated attribution in the builder and world description. The observed sole rejection is the foreign marker; the counter does not fetch that already-rejected row. More generally, `--fetch` in zero-backed worlds is not evidence that their source URLs were fetched by the counter. The independent curl captures above establish source access separately.

## Complete scoring output: initial worlds

Each header identifies the sandbox commit and clone path. Everything from each `$ timeout ...` line through its `exit 1` line is the complete recorded counter stdout/stderr and observed exit code, without omitted rejection lines.

```text

## a_shared_exact
sandbox baa3870f7efb68d71d5c22d77387cfe724dc53f7 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
VS Code and Copilot CLI use the same real .github/prompts/ token; both quotes are real and their hosts are pinned.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev baa3870f7efb68d71d5c22d77387cfe724dc53f7 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev baa3870f7efb68d71d5c22d77387cfe724dc53f7
custom command files found on the live page 0 of 2; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md command token '.github/prompts/' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md command token '.github/prompts/' is shared by rows Copilot CLI, VS Code
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev baa3870f7efb68d71d5c22d77387cfe724dc53f7
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev baa3870f7efb68d71d5c22d77387cfe724dc53f7
custom command files backed 0 of 2; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md command token '.github/prompts/' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md command token '.github/prompts/' is shared by rows Copilot CLI, VS Code
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1


## a_shared_alias_misspelled
sandbox 766911e38dc70e0ba40896db7085de93576dc92f (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
The shared partner is misspelled and changes case and leading/trailing slash form; E5 should still disqualify VS Code.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 766911e38dc70e0ba40896db7085de93576dc92f --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 766911e38dc70e0ba40896db7085de93576dc92f
custom command files found on the live page 0 of 1; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md command token '.github/prompts/' is shared by rows Copilot CLl, VS Code
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 766911e38dc70e0ba40896db7085de93576dc92f
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 766911e38dc70e0ba40896db7085de93576dc92f
custom command files backed 0 of 1; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md command token '.github/prompts/' is shared by rows Copilot CLl, VS Code
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1


## a_copilot_only_offtopic
sandbox 9093047e690c030d1d85228799afae0fbe8fbe6e (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
Remove VS Code. Relabel IDE-only prompt documentation on docs.github.com as Copilot CLI. The fetched page explicitly excludes CLI availability.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 9093047e690c030d1d85228799afae0fbe8fbe6e --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 9093047e690c030d1d85228799afae0fbe8fbe6e
custom command files found on the live page 1 of 1; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Copilot CLI  BACKED token=.github/prompts/ norm=.github/prompts found=yes held-at-base=yes
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 9093047e690c030d1d85228799afae0fbe8fbe6e
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 9093047e690c030d1d85228799afae0fbe8fbe6e
custom command files backed 1 of 1; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Copilot CLI  BACKED token=.github/prompts/ norm=.github/prompts
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1


## b_foreign_marker
sandbox 0775e66751c6bc854d6e7fa954d968f5a2e7a2a0 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
Cursor is given .claude/commands/ with a real Claude quote falsely attributed to the pinned Cursor deeplinks page. There is no Claude row, so the foreign-marker guard is isolated from E5.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 0775e66751c6bc854d6e7fa954d968f5a2e7a2a0 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 0775e66751c6bc854d6e7fa954d968f5a2e7a2a0
custom command files found on the live page 0 of 1; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md command token '.claude/commands/' carries Claude Code's marker 'claude'
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 0775e66751c6bc854d6e7fa954d968f5a2e7a2a0
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 0775e66751c6bc854d6e7fa954d968f5a2e7a2a0
custom command files backed 0 of 1; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md command token '.claude/commands/' carries Claude Code's marker 'claude'
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1


## c_misspelled_names
sandbox 14de5f157be2817b09d24d35160fde6e4a564123 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
All seven labels are near-spellings but not canonical identities; entry labels remain canonical.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 14de5f157be2817b09d24d35160fde6e4a564123 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 14de5f157be2817b09d24d35160fde6e4a564123
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1)
reject Codex: SKILL.md rows naming client: 0 (need exactly 1)
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1)
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1)
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1)
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1)
reject opencode: SKILL.md rows naming client: 0 (need exactly 1)
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 14de5f157be2817b09d24d35160fde6e4a564123
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 14de5f157be2817b09d24d35160fde6e4a564123
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1)
reject Codex: SKILL.md rows naming client: 0 (need exactly 1)
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1)
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1)
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1)
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1)
reject opencode: SKILL.md rows naming client: 0 (need exactly 1)
exit 1


## c_duplicated_skill_names
sandbox 77487eb659f5b8487ddaec9e6a6ec5648cfe5923 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
All six otherwise eligible SKILL clients have two identical rows. Exact duplicates must not be silently deduplicated.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 77487eb659f5b8487ddaec9e6a6ec5648cfe5923 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 77487eb659f5b8487ddaec9e6a6ec5648cfe5923
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md rows naming client: 2 (need exactly 1)
reject Codex: SKILL.md rows naming client: 2 (need exactly 1)
reject VS Code: SKILL.md rows naming client: 2 (need exactly 1)
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 2 (need exactly 1)
reject Cursor: SKILL.md rows naming client: 2 (need exactly 1)
reject opencode: SKILL.md rows naming client: 2 (need exactly 1)
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 77487eb659f5b8487ddaec9e6a6ec5648cfe5923
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 77487eb659f5b8487ddaec9e6a6ec5648cfe5923
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 2 (need exactly 1)
reject Codex: SKILL.md rows naming client: 2 (need exactly 1)
reject VS Code: SKILL.md rows naming client: 2 (need exactly 1)
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 2 (need exactly 1)
reject Cursor: SKILL.md rows naming client: 2 (need exactly 1)
reject opencode: SKILL.md rows naming client: 2 (need exactly 1)
exit 1


## d_entry_case_mismatch
sandbox e17d7c1bb0b116e7c7a9a6e30c67a179c130a25d (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
Six otherwise eligible rows retain real case-correct quotes, but each entry Command files cell uppercases its path.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev e17d7c1bb0b116e7c7a9a6e30c67a179c130a25d --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev e17d7c1bb0b116e7c7a9a6e30c67a179c130a25d
custom command files found on the live page 0 of 6; new ground 0
reject Claude Code: entry row S900: entry Command files cell '`.CLAUDE/COMMANDS/`' is not the SKILL.md token '.claude/commands/'
reject Codex: entry row S901: entry Command files cell '`~/.CODEX/PROMPTS/`' is not the SKILL.md token '~/.codex/prompts/'
reject VS Code: entry row S902: entry Command files cell '`.GITHUB/PROMPTS/`' is not the SKILL.md token '.github/prompts/'
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: entry row S904: entry Command files cell '`~/.GEMINI/COMMANDS/`' is not the SKILL.md token '~/.gemini/commands/'
reject Cursor: entry row S905: entry Command files cell '`.CURSOR/COMMANDS`' is not the SKILL.md token '.cursor/commands'
reject opencode: entry row S906: entry Command files cell '`.OPENCODE/COMMANDS/`' is not the SKILL.md token '.opencode/commands/'
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev e17d7c1bb0b116e7c7a9a6e30c67a179c130a25d
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev e17d7c1bb0b116e7c7a9a6e30c67a179c130a25d
custom command files backed 0 of 6; new ground not computed (needs --fetch)
reject Claude Code: entry row S900: entry Command files cell '`.CLAUDE/COMMANDS/`' is not the SKILL.md token '.claude/commands/'
reject Codex: entry row S901: entry Command files cell '`~/.CODEX/PROMPTS/`' is not the SKILL.md token '~/.codex/prompts/'
reject VS Code: entry row S902: entry Command files cell '`.GITHUB/PROMPTS/`' is not the SKILL.md token '.github/prompts/'
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: entry row S904: entry Command files cell '`~/.GEMINI/COMMANDS/`' is not the SKILL.md token '~/.gemini/commands/'
reject Cursor: entry row S905: entry Command files cell '`.CURSOR/COMMANDS`' is not the SKILL.md token '.cursor/commands'
reject opencode: entry row S906: entry Command files cell '`.OPENCODE/COMMANDS/`' is not the SKILL.md token '.opencode/commands/'
exit 1


## d_entry_added_slash
sandbox 318a4b941160bd6ef7985a21b2db56a292d264c4 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
All six SKILL paths have no trailing slash; each entry adds one. This is not raw token or normalise(token).

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 318a4b941160bd6ef7985a21b2db56a292d264c4 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 318a4b941160bd6ef7985a21b2db56a292d264c4
custom command files found on the live page 0 of 6; new ground 0
reject Claude Code: entry row S900: entry Command files cell '`.claude/commands/`' is not the SKILL.md token '.claude/commands'
reject Codex: entry row S901: entry Command files cell '`~/.codex/prompts/`' is not the SKILL.md token '~/.codex/prompts'
reject VS Code: entry row S902: entry Command files cell '`.github/prompts/`' is not the SKILL.md token '.github/prompts'
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: entry row S904: entry Command files cell '`~/.gemini/commands/`' is not the SKILL.md token '~/.gemini/commands'
reject Cursor: entry row S905: entry Command files cell '`.cursor/commands/`' is not the SKILL.md token '.cursor/commands'
reject opencode: entry row S906: entry Command files cell '`.opencode/commands/`' is not the SKILL.md token '.opencode/commands'
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 318a4b941160bd6ef7985a21b2db56a292d264c4
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 318a4b941160bd6ef7985a21b2db56a292d264c4
custom command files backed 0 of 6; new ground not computed (needs --fetch)
reject Claude Code: entry row S900: entry Command files cell '`.claude/commands/`' is not the SKILL.md token '.claude/commands'
reject Codex: entry row S901: entry Command files cell '`~/.codex/prompts/`' is not the SKILL.md token '~/.codex/prompts'
reject VS Code: entry row S902: entry Command files cell '`.github/prompts/`' is not the SKILL.md token '.github/prompts'
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: entry row S904: entry Command files cell '`~/.gemini/commands/`' is not the SKILL.md token '~/.gemini/commands'
reject Cursor: entry row S905: entry Command files cell '`.cursor/commands/`' is not the SKILL.md token '.cursor/commands'
reject opencode: entry row S906: entry Command files cell '`.opencode/commands/`' is not the SKILL.md token '.opencode/commands'
exit 1


## d_entry_allowed_normalisation
sandbox d567a698a60630c36f970f1bceeb48ab395acc69 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
Calibration: ./ and the trailing slash are removed in the entry; the explicit frozen normalise rule permits this.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev d567a698a60630c36f970f1bceeb48ab395acc69 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev d567a698a60630c36f970f1bceeb48ab395acc69
custom command files found on the live page 1 of 1; new ground 1
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       BACKED token=./.cursor/commands/ norm=.cursor/commands found=yes held-at-base=no
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev d567a698a60630c36f970f1bceeb48ab395acc69
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev d567a698a60630c36f970f1bceeb48ab395acc69
custom command files backed 1 of 1; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       BACKED token=./.cursor/commands/ norm=.cursor/commands
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1


## e_reused_base_url
sandbox 87745a7fa9aef36db8626ffefceec2e46d6e5c95 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
Two fresh SOURCES ids recite the base skills URL, once literally and once through host/path case, repeated slash, percent encoding, trailing slash, query and fragment aliases. Both use a genuine quote from the base URL.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 87745a7fa9aef36db8626ffefceec2e46d6e5c95 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 87745a7fa9aef36db8626ffefceec2e46d6e5c95
custom command files found on the live page 0 of 1; new ground 0
reject Claude Code: entry row S907: S907 URL 'https://CODE.CLAUDE.COM/docs//EN/%73kills.md/?probe=1#repeat' is already a base SOURCES URL; entry row S907: S907 URL 'https://CODE.CLAUDE.COM/docs//EN/%73kills.md/?probe=1#repeat' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 87745a7fa9aef36db8626ffefceec2e46d6e5c95
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 87745a7fa9aef36db8626ffefceec2e46d6e5c95

[Showing lines 1-300 of 340. Use :301 to continue]
```

## Complete scoring output: corrected independent-record worlds

```text

## e_reused_base_url_corrected
sandbox d215313554339b3710e92aa93064991fffe619a6 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
Two fresh SOURCES ids recite the base skills URL, once literally and once through host/path case, repeated slash, percent encoding, trailing slash, query and fragment aliases. Both use a genuine quote from the base URL.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev d215313554339b3710e92aa93064991fffe619a6 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev d215313554339b3710e92aa93064991fffe619a6
custom command files found on the live page 0 of 1; new ground 0
reject Claude Code: entry row S900: S900 URL 'https://code.claude.com/docs/en/skills.md' is already a base SOURCES URL; entry row S907: S907 URL 'https://CODE.CLAUDE.COM/docs//EN/%73kills.md/?probe=1#repeat' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev d215313554339b3710e92aa93064991fffe619a6
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev d215313554339b3710e92aa93064991fffe619a6
custom command files backed 0 of 1; new ground not computed (needs --fetch)
reject Claude Code: entry row S900: S900 URL 'https://code.claude.com/docs/en/skills.md' is already a base SOURCES URL; entry row S907: S907 URL 'https://CODE.CLAUDE.COM/docs//EN/%73kills.md/?probe=1#repeat' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1


## c_duplicate_entry_names_corrected
sandbox 0ccd7e5848e6daedb859f1e803914cb6d9bcafb8 (/fast/scratch/hyaku/kotoba-r58/CtlC1SharedLabel)
Scope calibration: the frozen contract forbids duplicate SKILL client rows, not entry rows. An invalid first entry and valid second entry share the Cursor label.

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 0ccd7e5848e6daedb859f1e803914cb6d9bcafb8 --fetch
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 0ccd7e5848e6daedb859f1e803914cb6d9bcafb8
custom command files found on the live page 1 of 1; new ground 1
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       BACKED token=.cursor/commands norm=.cursor/commands found=yes held-at-base=no
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

$ timeout 900 python3 -B verifiers/check_command_files.py --rev 0ccd7e5848e6daedb859f1e803914cb6d9bcafb8
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 0ccd7e5848e6daedb859f1e803914cb6d9bcafb8
custom command files backed 1 of 1; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       BACKED token=.cursor/commands norm=.cursor/commands
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1

```

Report: .ufo/waves/round-58/controls/CtlC1SharedLabel.md
