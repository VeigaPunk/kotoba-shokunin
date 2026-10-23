Result: HOLDS — Base, counters-only, and heading-plus-empty-table controls all printed F=0, K=0, G=0 with --fetch and exited 1; none met F>=4 and G>=3.

## Scope, axes, and counterexample

Assigned C1 only. Impacted axis: depth, specifically resistance to granting sourced-learning credit to no work or empty presentation. The strongest assigned counterexample adds the exact section heading and table header but no client rows, facts, actions, sources, quotes, or lesson content. This shortcut did not gain credit. These results do not establish resistance to other controls.

All execution and git writes occurred in `/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing`. Only this report was written in the lane. No counter was edited. No tools were installed or updated.

World identities (all hashes below are sandbox identities, not lane deliverables):

- Base: sandbox f56f6e191762c27c1aa2af11a204db9e2ca4edec (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing).
- Counters-only: sandbox 3de87aad29e960c95ed35840442f424c48c29729 (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing).
- Empty table: sandbox ebc9e9947085d5b77f895e168efb31994d8d7ccc (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing), a child of the counters-only world. The commit reported one file changed and five insertions, all in `SKILL.md`.

The empty-table world's only addition is `SKILL.md:125-129`:

```markdown
### Custom command files by client

| Client | Command files | What a file sets | Action |
|---|---|---|---|

```

## Frozen-counter identity and context discrepancy

The initial assignment described unfrozen `None` targets. The assigned committed bytes actually have `TARGET = 4` and `NEW_TARGET = 3` at `verifiers/check_command_files.py:246-247`. L1 subsequently confirmed the context sentence was stale and instructed scoring those bytes unchanged. All six runs below used those same bytes and exited 1, not 2. None printed `targets not frozen`.

At the counters-only checkout, command:

```sh
timeout 900 sha256sum verifiers/check_command_files.py verifiers/check_sweep_mutants.py
```

Full output, exit 0:

```text
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
```

Independent committed-blob identity command, cwd the sandbox clone:

```sh
timeout 900 git show 3de87aad29e960c95ed35840442f424c48c29729:verifiers/check_command_files.py | timeout 900 sha256sum
```

Full output, exit 0:

```text
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  -
```

Evidence pointers are to these committed counter bytes in the sandbox: `SKILL_HEADING` and `SKILL_HEADER` at `verifiers/check_command_files.py:284-285`; measured content is read from the requested revision at `:1908-1914`; backed rows and K are collected at `:1919-1921`; fetching only iterates backed rows at `:1923-1932`; the sentinel handling and predicate return are at `:1961-1964`. All seven clients were rejected in every run, so the fetch loop had no backed source to fetch. No external page receipts were needed for these no-content worlds.

## Six scoring runs

Every command below ran with cwd `/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing`. Code blocks contain the complete counter output; temporary-shell notices from the tool wrapper are not counter output. Exit codes are observed tool exit codes.

### 1. Base, with --fetch

World: sandbox f56f6e191762c27c1aa2af11a204db9e2ca4edec (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing).

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec --fetch
```

Exit 1. Full output:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### 2. Base, without --fetch

World: sandbox f56f6e191762c27c1aa2af11a204db9e2ca4edec (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing).

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
```

Exit 1. Full output:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### 3. Counters-only, with --fetch

World: sandbox 3de87aad29e960c95ed35840442f424c48c29729 (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing).

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev 3de87aad29e960c95ed35840442f424c48c29729 --fetch
```

Exit 1. Full output:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 3de87aad29e960c95ed35840442f424c48c29729
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### 4. Counters-only, without --fetch

World: sandbox 3de87aad29e960c95ed35840442f424c48c29729 (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing).

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev 3de87aad29e960c95ed35840442f424c48c29729
```

Exit 1. Full output:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 3de87aad29e960c95ed35840442f424c48c29729
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### 5. Empty table, with --fetch

World: sandbox ebc9e9947085d5b77f895e168efb31994d8d7ccc (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing).

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev ebc9e9947085d5b77f895e168efb31994d8d7ccc --fetch
```

Exit 1. Full output:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev ebc9e9947085d5b77f895e168efb31994d8d7ccc
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### 6. Empty table, without --fetch

World: sandbox ebc9e9947085d5b77f895e168efb31994d8d7ccc (/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing).

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev ebc9e9947085d5b77f895e168efb31994d8d7ccc
```

Exit 1. Full output:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev ebc9e9947085d5b77f895e168efb31994d8d7ccc
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

## Construction receipts

Sandbox setup command, cwd `/fast/scratch/hyaku`, exit 0, no output:

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE && timeout 900 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing && timeout 900 git -C /fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing checkout -q 3de87aad29e960c95ed35840442f424c48c29729
```

Before adding the empty table, `timeout 900 git rev-parse HEAD`, cwd the sandbox, exited 0 and printed the counters-only sandbox identity:

```text
3de87aad29e960c95ed35840442f424c48c29729
```

After the five-line sandbox-only edit, construction command, cwd the sandbox:

```sh
timeout 900 git add -- SKILL.md && timeout 900 git -c user.name='KotobaR58 CtlC1DoNothing' -c user.email='ctl-c1-do-nothing@invalid' -c commit.gpgsign=false commit -m 'control: add only empty custom command files table'
```

Exit 0. Full output (short identity refers to the labelled empty-table sandbox world above):

```text
[detached HEAD ebc9e99] control: add only empty custom command files table
 1 file changed, 5 insertions(+)
```

`timeout 900 git rev-parse HEAD`, cwd the sandbox, then exited 0 and printed the empty-table sandbox identity:

```text
ebc9e9947085d5b77f895e168efb31994d8d7ccc
```

## Smallest safe correction

No counter change is indicated by these assigned controls: absence of content and an empty exact-shape table both receive zero credit. Correct the stale assignment description from unfrozen `None` targets to committed TARGET=4 / NEW_TARGET=3; L1 has acknowledged that description error. Do not change the frozen counter or infer broader shortcut resistance from these three worlds.

## Requested wildcard checksum receipt

After scoring, returned to the counters-only sandbox checkout and ran, cwd `/fast/scratch/hyaku/kotoba-r58/CtlC1DoNothing`:

```sh
timeout 900 git checkout -q 3de87aad29e960c95ed35840442f424c48c29729 && timeout 900 sha256sum verifiers/check_*.py
```

The tool backgrounded this command as `bg_2012`, then delivered its completed receipt. Numeric exit status was not exposed by that background receipt; no numeric status is invented here. The six scoring runs above each explicitly exposed exit 1. Complete checksum output:

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
