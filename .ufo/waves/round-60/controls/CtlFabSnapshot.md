Result: DONE — CtlFabSnapshot: S 1 of 4; F 0 of 4; exit 1; predicate NOT MET

## Mutant and verdict

Control: `CtlFabSnapshot`, fabricated snapshots. The four real census clients, tokens, URLs and keys are retained. All four quotes and Action lines are invented; each six-line fabricated snapshot contains its invented quote at line 2, its real key with `src/fabricated-lattice/**/*.ts` at line 4, and its invented action at line 6. Each SOURCES row pins that fabricated page's actual sha256. The counter is unchanged.

**Full-predicate mutation verdict: INCONCLUSIVE, not killed.** The genuine pristine world already exits 1: Claude Code, Copilot CLI and Cursor have census URLs that the frozen counter rejects as already present in BASE_REV SOURCES. Pristine and restored results are S 1 of 4, F 1 of 4, exit 1; the fabricated world is S 1 of 4, F 0 of 4, exit 1. Consequently this probe cannot establish an exit-code kill. At the admitted VS Code row, the invented snapshot passes offline backing but the live reread explicitly rejects the invented quote. This is a row-level detection observation, not a full-predicate kill or an adequacy judgment.

Expected detector: the frozen `--fetch` live quote check should reject invented quotes even when their fabricated snapshots and supplied hashes agree. The declared predicate is exit 0 iff F >= TARGET; TARGET was read from the committed counter, `verifiers/check_scoped_rules.py:232`, and is 3. Offline exit 1 is required by this counter even for backed rows and is not itself evidence of rejection.

## Isolation and identities

All code execution, world edits and Git writes occurred only in `/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot`. This report is the only lane file written. No tools were installed or updated; no client/model runtime was invoked.

- Freeze: `49c3e87d4fb5677783c55f8225c9e4f892273879`.
- Genuine pristine world: sandbox a2893fa26d08cda5a866875af121046573b699fa (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot).
- **Scored fabricated world:** sandbox 8933ce9e95372cb8daedd6145e4b930fe472d239 (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot).
- Exact-byte restoration: sandbox b713e5b1017d784f558e5b8c674bceaca8f1cd1b (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot).

The fabricated commit remains available for replay; the scratch working files were restored and committed, not left fabricated. World layout and self-pinning SOURCES rows reuse the frozen counter's self-test pattern at `verifiers/check_scoped_rules.py:1603-1684`; no self-test was executed by this seat.

Freeze identity command, exit 0:

```text
timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 49c3e87d4fb5677783c55f8225c9e4f892273879:verifiers/check_scoped_rules.py | sha256sum
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  -
```

From the sandbox clone, `sha256sum verifiers/check_scoped_rules.py` (run with `timeout 30`), exit 0:

```text
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  verifiers/check_scoped_rules.py
```

The same counter hash was printed by all six detector runs and was unchanged in the restoration comparison.

## Fabricated bytes and citations

Evidence pointers below refer to the scored fabricated sandbox commit, not the subsequently restored worktree.

- `SKILL.md:135-142`: exact heading, required table header, four tokens, key citations `S103 :4` through `S106 :4`, and Action citations at line 6.
- `corpus/knowledge/scoped-rules-round60.md:3-8`: matching entry table and invented quotes.
- `corpus/lessons/round-60.md:3-10`: Gate records the same invented quotes.
- `corpus/SOURCES.md:115-118`: S103–S106, real census URLs, required row fields and fabricated-page sha256 pins.
- `.ufo/waves/round-60/snapshots/S103.page:2,4,6`, likewise S104–S106: quote, real key/glob, invented action.

Each invented quote is 11 whitespace-separated words after removing backticks. No text below is represented as a quotation from a vendor:

```text
Luminous rules in `.claude/rules/` synchronize amber lattice files through matching patterns.
Luminous rules in `.github/instructions/**/*.instructions.md` synchronize amber lattice files through matching patterns.
Luminous rules in `.github/instructions` synchronize amber lattice files through matching patterns.
Luminous rules in `.cursor/rules` synchronize amber lattice files through matching patterns.
```

The invented Action line, identical in each snapshot and its cited cell:

```text
Calibrate saffron guidance for lattice files using amber matching patterns.
```

| id | real client | real token | real key | fabricated page bytes | fabricated sha256 |
|---|---|---|---|---:|---|
| S103 | Claude Code | `.claude/rules/` | `paths` | 260 | f954da8bdd4b97d109334075277372dcf67bd6dd736eac78b975325b662d780b |
| S104 | VS Code | `.github/instructions/**/*.instructions.md` | `applyTo` | 285 | 8e234e9f21b8120d3aca274ea95bc762157dd157b9043b8676e1731f3084261c |
| S105 | Copilot CLI | `.github/instructions` | `applyTo` | 268 | 427a6ed29e968997ec214fe97675f5fa8a4aac8e5746a4b58cbabe25e21eb24a |
| S106 | Cursor | `.cursor/rules` | `globs` | 254 | 76c20d25fae398a158dc2394c8573a7c65032ce9c78b2fc7f469b68e862c8c7f |

Census pointers: `w0/CensusClaudeCode.md:15,43,73`, `w0/CensusVSCode.md:19,50,75`, `w0/CensusCopilotCLI.md:61,76,122-127`, `w0/CensusCursor.md:18,55,73`, all under `.ufo/waves/round-60/`. Copilot uses the census's explicitly eligible folder token and its pipe-free quote at fetched line 56, rather than the primary file-pattern quote containing a Markdown table pipe. The counter splits cells on literal pipes (`verifiers/check_scoped_rules.py:404-408`). This is the same token in pristine, mutated and restored worlds, not a post-result substitution.

## Source acquisition for the genuine pristine world

One ordinary curl acquisition per page, all exit 0 and HTTP 200. All used the counter's browser UA and Accept header. Snapshot bodies were stored directly under this sandbox's `.ufo/waves/round-60/snapshots/`; response headers are under its `control-receipts/S103.headers` through `S106.headers`.

For every row below `date -u` printed exactly:

```text
Fri 23 Oct 2026 10:48:12 AM UTC
```

| id | requested and effective URL | HTTP | bytes (`curl` and `wc -c`) | fetched sha256 |
|---|---|---:|---:|---|
| S103 | https://code.claude.com/docs/en/memory.md | 200 | 54043 | 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7 |
| S104 | https://code.visualstudio.com/docs/agent-customization/custom-instructions.md | 200 | 23715 | a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f |
| S105 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | 200 | 8730 | 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980 |
| S106 | https://cursor.com/docs/rules | 200 | 17403 | 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8 |

Acquisition command shape (substitute the row's id and URL; each invocation was a separate bounded command):

```sh
timeout 5 date -u && timeout 45 curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -D control-receipts/S103.headers -o .ufo/waves/round-60/snapshots/S103.page -w 'HTTP %{http_code}; URL %{url_effective}; bytes %{size_download}\n' https://code.claude.com/docs/en/memory.md && timeout 5 wc -c .ufo/waves/round-60/snapshots/S103.page && timeout 5 sha256sum .ufo/waves/round-60/snapshots/S103.page
```

The three subsequent live detector runs retain the frozen maximum of three attempts per page per run (`verifiers/check_scoped_rules.py:1137-1161`); no extra source-retry loop or bot-challenge mechanism was used. Their stdout does not expose response byte counts or hashes; the acquisition metadata above is for the explicitly captured pristine bodies, not an assertion about unrecorded live response bytes.

Genuine pristine quotes, all byte-exact contiguous substrings of the fetched line, with no Markdown stripping (each <=25 words):

- S103 line 168: “For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory.”
- S104 line 32: “Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`.”
- S105 line 56: “2. Optionally, create subdirectories of `.github/instructions` to organize your instruction files.”
- S106 line 32: “Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled.”

Pristine key/Action citations were respectively S103 :198/:194, S104 :164/:329, S105 :66/:60, S106 :85/:131. The URLs were not changed to evade the observed base-URL rejection.

## Detector receipts — exact commands and full stdout

All commands ran with cwd `/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot`. All six exit codes are 1; no stderr was emitted by the counter.

### Pristine, without fetch

sandbox a2893fa26d08cda5a866875af121046573b699fa (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot)

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev a2893fa26d08cda5a866875af121046573b699fa
```

Exit 1. Full stdout:

```text
scoped rule files backed on committed snapshots 1 of 4; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev a2893fa26d08cda5a866875af121046573b699fa
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### Pristine, with fetch

sandbox a2893fa26d08cda5a866875af121046573b699fa (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot)

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev a2893fa26d08cda5a866875af121046573b699fa --fetch
```

Exit 1. Full stdout:

```text
scoped rule files backed on committed snapshots 1 of 4; found on the live page 1 of 4
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev a2893fa26d08cda5a866875af121046573b699fa
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### Fabricated control, without fetch

sandbox 8933ce9e95372cb8daedd6145e4b930fe472d239 (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot)

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 8933ce9e95372cb8daedd6145e4b930fe472d239
```

Exit 1. Full stdout:

```text
scoped rule files backed on committed snapshots 1 of 4; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 8933ce9e95372cb8daedd6145e4b930fe472d239
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### Fabricated control, with fetch — assigned predicate receipt

sandbox 8933ce9e95372cb8daedd6145e4b930fe472d239 (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot)

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 8933ce9e95372cb8daedd6145e4b930fe472d239 --fetch
```

Exit 1. Full stdout:

```text
scoped rule files backed on committed snapshots 1 of 4; found on the live page 0 of 4
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev 8933ce9e95372cb8daedd6145e4b930fe472d239
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: live page: the quote is not on the page
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

C1 predicate: --fetch exit 0 (F>=TARGET) — NOT MET

### Restored, without fetch

sandbox b713e5b1017d784f558e5b8c674bceaca8f1cd1b (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot)

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev b713e5b1017d784f558e5b8c674bceaca8f1cd1b
```

Exit 1. Full stdout:

```text
scoped rule files backed on committed snapshots 1 of 4; live not run
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev b713e5b1017d784f558e5b8c674bceaca8f1cd1b
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

### Restored, with fetch

sandbox b713e5b1017d784f558e5b8c674bceaca8f1cd1b (/fast/scratch/hyaku/kotoba-r60/CtlFabSnapshot)

```sh
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev b713e5b1017d784f558e5b8c674bceaca8f1cd1b --fetch
```

Exit 1. Full stdout:

```text
scoped rule files backed on committed snapshots 1 of 4; found on the live page 1 of 4
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440; rev b713e5b1017d784f558e5b8c674bceaca8f1cd1b
reject Claude Code: entry row S103: S103 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: entry row S105: S105 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: entry row S106: S106 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

## Before, mutant and restoration hashes

The following command was run at each committed stage, exit 0 each time:

```sh
timeout 5 sha256sum verifiers/check_scoped_rules.py SKILL.md corpus/SOURCES.md corpus/knowledge/scoped-rules-round60.md corpus/lessons/round-60.md .ufo/waves/round-60/snapshots/S103.page .ufo/waves/round-60/snapshots/S104.page .ufo/waves/round-60/snapshots/S105.page .ufo/waves/round-60/snapshots/S106.page
```

The pristine and restored columns are identical for every file. A separate byte-for-byte in-memory comparison of all nine files printed `Exact restoration: 9 of 9 files` and one `MATCH` per file.

| file | pristine sha256 = restored sha256 | mutant sha256 |
|---|---|---|
| verifiers/check_scoped_rules.py | 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440 | 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440 |
| SKILL.md | 3ea38efe40150d352e90a891a56e24cdb2c29a981134ce183babdeec6e274329 | 7dacec1df929fa6c2b068c03d11d2cc31b5bc2f6e8c603a0a6b8c5e69cedfc76 |
| corpus/SOURCES.md | fa61ded44478fdc8d06ec390dd1de4c07d5d09f9b26483f1d4189bc3cae6dc20 | 4d4c7c3f82f7f914ed93c480b756f7d398a49e79c1f50b32193cc67e90484bae |
| corpus/knowledge/scoped-rules-round60.md | 55c502365fdbb27ff5fd65b18b52bf2687f8e174df1f8a006188c2d22a29fd0c | e51850430feb6ef7a5238813d31df7e844c9322d3ac337266bf58561d59bea47 |
| corpus/lessons/round-60.md | 27fcf8a31a84a3ecb579c4b27e72bd41646adfc90503804f0b10fec3edc13a89 | 1fc5e32246fe0da4c808e3d1e1dc8ce037078e6ddd0513e6f2f7668a97cae429 |
| .ufo/waves/round-60/snapshots/S103.page | 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7 | f954da8bdd4b97d109334075277372dcf67bd6dd736eac78b975325b662d780b |
| .ufo/waves/round-60/snapshots/S104.page | a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f | 8e234e9f21b8120d3aca274ea95bc762157dd157b9043b8676e1731f3084261c |
| .ufo/waves/round-60/snapshots/S105.page | 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980 | 427a6ed29e968997ec214fe97675f5fa8a4aac8e5746a4b58cbabe25e21eb24a |
| .ufo/waves/round-60/snapshots/S106.page | 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8 | 76c20d25fae398a158dc2394c8573a7c65032ce9c78b2fc7f469b68e862c8c7f |

Restoration used a bounded `git restore --source=a2893fa26d08cda5a866875af121046573b699fa --worktree --` with exactly the eight changed world paths above, followed by an explicit-path add and a sandbox-only restore commit. The counter was never edited. The restored offline and live detector outputs reproduce the pristine S/F counts and exits.

Report: .ufo/waves/round-60/controls/CtlFabSnapshot.md
