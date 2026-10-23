Result: HOLDS — both real-source off-topic worlds scored F=0, K=0, G=0 with the unchanged committed counter and failed the frozen predicate.

## Counterexample and scope

The cheap world skips learning custom command-file locations: it relabels real skill folders, a plugin manifest, an agent folder, always-on instructions, a settings file and rules as command files. A second world substitutes a real documentation link whose last component is `commands.md`. Every quote comes from an ordinary HTTP fetch of an actual pinned-host page; none is fabricated.

Axes: C1 depth, source fidelity, and discriminative validity of F/K/G. No admission or canonical judgment is made here.

Clone: `/fast/scratch/hyaku/kotoba-r58/CtlC1OffTopic`.

- W1: sandbox 39903415a7ec14fc090bc59fe949b49db76a5557 (/fast/scratch/hyaku/kotoba-r58/CtlC1OffTopic).
- W2: sandbox b5799ce55965d7879c41af980885f6420b81a790 (/fast/scratch/hyaku/kotoba-r58/CtlC1OffTopic).

Both descend from the required checkout `3de87aad29e960c95ed35840442f424c48c29729`. Only sandbox content/evidence files changed; neither counter was edited. The clone is left checked out at that frozen revision, with both world commits retained.

The initial assignment's `None` sentinel description was stale. The named commit actually has `TARGET = 4` and `NEW_TARGET = 3` at `verifiers/check_command_files.py:246-247`; L1 confirmed the correction. Predicate used: `--fetch` exit 0 iff F >= 4 and G >= 3. Neither world meets it or reaches a high count.

## Exact source evidence

All paths in this section are files committed in W1. Quotes are contiguous, byte-exact, one-line substrings of the fetched Markdown. No internal Markdown bytes were stripped, no words inserted, and no line breaks folded. Surrounding quotation marks below are delimiters, not source bytes. List markers or surrounding prose outside each quoted span are not quoted.

| Client | fetched file and line | words | verbatim quote |
|---|---|---|---|
| Claude Code, W1 | `control-evidence/claude-skills.md:190` | 15 | "Claude Code loads the skills in that directory's `.claude/skills/`, along with its `.claude/commands/` and `.claude/agents/`." |
| Codex | `control-evidence/codex-plugins.md:26` | 8 | "`.codex-plugin/plugin.json` files remain supported as a compatibility fallback." |
| VS Code | `control-evidence/vscode-agents.md:128` | 13 | "Prefer native harness folders, such as `.github/agents` and `~/.copilot/agents`, over custom search locations." |
| Copilot CLI | `control-evidence/copilot-instructions.md:36` | 11 | "In the root of your repository, create a file named `.github/copilot-instructions.md`." |
| Gemini CLI | `control-evidence/gemini-mcp.md:1149` | 7 | "`~/.gemini/settings.json` or the project config `.gemini/settings.json` file." |
| Cursor | `control-evidence/cursor-rules.md:32` | 11 | "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled." |
| opencode | `control-evidence/opencode-skills.md:25` | 10 | "Global definitions are also loaded from `~/.config/opencode/skills/*/SKILL.md`, `~/.claude/skills/*/SKILL.md`, and `~/.agents/skills/*/SKILL.md`." |
| Claude Code, W2 | `control-evidence/claude-skills.md:15` | 18 | "For built-in commands like `/help` and `/compact`, and bundled skills like `/debug` and `/code-review`, see the [commands reference](/docs/en/commands.md)." |

W1 table: `SKILL.md:602-614`; entry: `corpus/knowledge/command-files-round58.md:5-13`; new control source ids S901-S907: `corpus/SOURCES.md:102-108`; recorded quotes: `corpus/lessons/round-58.md:5-15`. W2 changes only Claude's token, quote and source anchor in those files. Other six rows stay the same.

### Fetch commands and observed metadata

The seven source fetches ran with four HTTP processes at most. Each used the following exact argument pattern (substitute the URL and output file from the records below):

```sh
timeout 900 date -u
timeout 900 curl -L --max-time 90 --connect-timeout 20 --silent --show-error --output control-evidence/FILE.md --write-out 'HTTP %{http_code}\nbytes %{size_download}\nURL %{url_effective}\n' URL
timeout 900 sha256sum control-evidence/FILE.md
```

All curl commands exited 0; the date and sha256sum outputs were captured as shown (their individual statuses were not retained by the fetch helper). All seven final URLs equal their requested URLs. For each of those seven requests the pasted `date -u` line was:

```text
Fri Oct 23 07:55:45 AM UTC 2026
```

```text
https://code.claude.com/docs/en/skills.md
HTTP 200
bytes 114542
URL https://code.claude.com/docs/en/skills.md
6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd  control-evidence/claude-skills.md
exit code: 0

https://developers.openai.com/plugins/build/plugins.md
HTTP 200
bytes 38036
URL https://developers.openai.com/plugins/build/plugins.md
c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1  control-evidence/codex-plugins.md
exit code: 0

https://code.visualstudio.com/docs/agent-customization/custom-agents.md
HTTP 200
bytes 15714
URL https://code.visualstudio.com/docs/agent-customization/custom-agents.md
8643b0986edea38447e9c759052284439a39e332d9f3dea2c4a6934c3361b07f  control-evidence/vscode-agents.md
exit code: 0

https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
HTTP 200
bytes 8730
URL https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  control-evidence/copilot-instructions.md
exit code: 0

https://geminicli.com/docs/tools/mcp-server.md
HTTP 200
bytes 43656
URL https://geminicli.com/docs/tools/mcp-server.md
4aefc4dc30c329cbbd16ca24fe294fb0d91ec87e8f61baca7116c19b6a1a14fd  control-evidence/gemini-mcp.md
exit code: 0

https://cursor.com/docs/rules.md
HTTP 200
bytes 17403
URL https://cursor.com/docs/rules.md
884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  control-evidence/cursor-rules.md
exit code: 0

https://opencode.ai/docs/skills.md
HTTP 200
bytes 5365
URL https://opencode.ai/docs/skills.md
f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561  control-evidence/opencode-skills.md
exit code: 0
```

Two additional ordinary fetches explored the opencode documentation-link variant; neither supplied a scored row. They are retained in W1 rather than presented as source evidence for a scored quote:

```text
https://opencode.ai/v2/docs/commands/
Fri Oct 23 07:56:35 AM UTC 2026
HTTP 200
bytes 32304
URL https://opencode.ai/v2/docs/commands/
32591ac3db0056fdbf3b5e20b78e70514da0d7306707cbf7c412ca19276640e0  control-evidence/opencode-commands.md
exit code: 0

https://opencode.ai/v2/docs/commands/
Fri Oct 23 07:56:54 AM UTC 2026
HTTP 200
bytes 7220
URL https://opencode.ai/v2/docs/commands/
c3dc75fc48071613c359126e7d84e2298afd10c4b83aac83383e94a1489a23dc  control-evidence/opencode-commands-markdown.md
exit code: 0
```

The first used the same curl arguments as above. The second additionally used `-H 'Accept: text/markdown'`, matching that page's own ordinary Markdown-copy content negotiation (`control-evidence/opencode-commands.md:268`). No headless browser, challenge bypass, client/model call or alternate judging runtime was used.

## Which conjunct rejects each row

Frozen implementation references: token grammar `verifiers/check_command_files.py:568-589`; quote external-word requirement `:700-706`; base-URL exclusion `:729-730`; K assigned only after the grammar succeeds `:768-772`; only backed rows are fetched `:1920-1932`.

| World/client | token | grammar failure(s) | additional observed backing failure(s) |
|---|---|---|---|
| W1 Claude Code | `.claude/skills/` | final component has no command/prompt word; forbidden `skills` segment | source URL already held at base |
| Both Codex | `.codex-plugin/plugin.json` | final component has no command/prompt word; forbidden `plugin` segments | quote has no command/prompt word outside token; source URL already held |
| Both VS Code | `.github/agents` | final component has no command/prompt word; forbidden `agents` segment | external-word requirement; source URL already held |
| Both Copilot CLI | `.github/copilot-instructions.md` | final component has no command/prompt word | external-word requirement; source URL already held |
| Both Gemini CLI | `.gemini/settings.json` | final component has no command/prompt word | external-word requirement; source URL already held |
| Both Cursor | `.cursor/rules` | final component has no command/prompt word; forbidden `rules` segment | external-word requirement; source URL already held |
| Both opencode | `~/.config/opencode/skills/*/SKILL.md` | final component has no command/prompt word; forbidden `skills` and `SKILL` segments | external-word requirement; source URL already held |
| W2 Claude Code | `/docs/en/commands.md` | leading `/` violates path regex; also not a dot-led first segment | source URL already held |

All rows have unique client names and tokens, a four-word action, matching entry tokens, 6–25-word quotes, new source ids, correctly shaped docs/A/mined/opened-date rows, pinned hosts, and Gate-recorded quotes. No action/table/quote-length/citation-shape failure appears in the counter output.

The Claude W1 quote does satisfy the lexical external-command-word conjunct: `.claude/commands/` elsewhere in the quote supplies it. W2 also satisfies it with ordinary prose. Neither is counted because its proposed token fails the path grammar. This is the strongest observed version of this control, not an all-false/empty-table test.

Important limitation: all seven cited URLs were already in the base SOURCES ledger. The freshness guard independently rejects them. K=0 nevertheless directly shows the separate grammar rejection before URL freshness is considered. With `--fetch`, these worlds make no counter HTTP requests because no row is backed; the actual source opens are the independently recorded HTTP requests above. The result is not proof of semantic discrimination for every possible off-topic token or for newly eligible paths.

## Frozen counter runs — full output

All four commands ran in the clone. Shell wrappers captured the counter's status with `status=$?` and printed it, so the following exit codes are the counter exits, not the wrapper exits.

### W1 — seven off-topic surfaces

World: sandbox 39903415a7ec14fc090bc59fe949b49db76a5557 (/fast/scratch/hyaku/kotoba-r58/CtlC1OffTopic).

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev 39903415a7ec14fc090bc59fe949b49db76a5557 --fetch
```

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 39903415a7ec14fc090bc59fe949b49db76a5557
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md command token '.claude/skills/' is not well-formed; entry row S901: S901 URL 'https://code.claude.com/docs/en/skills.md' is already a base SOURCES URL
reject Codex: SKILL.md command token '.codex-plugin/plugin.json' is not well-formed; entry row S902: quote holds no command/prompt word outside the token; S902 URL 'https://developers.openai.com/plugins/build/plugins.md' is already a base SOURCES URL
reject VS Code: SKILL.md command token '.github/agents' is not well-formed; entry row S903: quote holds no command/prompt word outside the token; S903 URL 'https://code.visualstudio.com/docs/agent-customization/custom-agents.md' is already a base SOURCES URL
reject Copilot CLI: SKILL.md command token '.github/copilot-instructions.md' is not well-formed; entry row S904: quote holds no command/prompt word outside the token; S904 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md command token '.gemini/settings.json' is not well-formed; entry row S905: quote holds no command/prompt word outside the token; S905 URL 'https://geminicli.com/docs/tools/mcp-server.md' is already a base SOURCES URL
reject Cursor: SKILL.md command token '.cursor/rules' is not well-formed; entry row S906: quote holds no command/prompt word outside the token; S906 URL 'https://cursor.com/docs/rules.md' is already a base SOURCES URL
reject opencode: SKILL.md command token '~/.config/opencode/skills/*/SKILL.md' is not well-formed; entry row S907: quote holds no command/prompt word outside the token; S907 URL 'https://opencode.ai/docs/skills.md' is already a base SOURCES URL
exit code: 1
```

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev 39903415a7ec14fc090bc59fe949b49db76a5557
```

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 39903415a7ec14fc090bc59fe949b49db76a5557
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md command token '.claude/skills/' is not well-formed; entry row S901: S901 URL 'https://code.claude.com/docs/en/skills.md' is already a base SOURCES URL
reject Codex: SKILL.md command token '.codex-plugin/plugin.json' is not well-formed; entry row S902: quote holds no command/prompt word outside the token; S902 URL 'https://developers.openai.com/plugins/build/plugins.md' is already a base SOURCES URL
reject VS Code: SKILL.md command token '.github/agents' is not well-formed; entry row S903: quote holds no command/prompt word outside the token; S903 URL 'https://code.visualstudio.com/docs/agent-customization/custom-agents.md' is already a base SOURCES URL
reject Copilot CLI: SKILL.md command token '.github/copilot-instructions.md' is not well-formed; entry row S904: quote holds no command/prompt word outside the token; S904 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md command token '.gemini/settings.json' is not well-formed; entry row S905: quote holds no command/prompt word outside the token; S905 URL 'https://geminicli.com/docs/tools/mcp-server.md' is already a base SOURCES URL
reject Cursor: SKILL.md command token '.cursor/rules' is not well-formed; entry row S906: quote holds no command/prompt word outside the token; S906 URL 'https://cursor.com/docs/rules.md' is already a base SOURCES URL
reject opencode: SKILL.md command token '~/.config/opencode/skills/*/SKILL.md' is not well-formed; entry row S907: quote holds no command/prompt word outside the token; S907 URL 'https://opencode.ai/docs/skills.md' is already a base SOURCES URL
exit code: 1
```

### W2 — actual documentation URL path substituted for Claude

World: sandbox b5799ce55965d7879c41af980885f6420b81a790 (/fast/scratch/hyaku/kotoba-r58/CtlC1OffTopic).

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev b5799ce55965d7879c41af980885f6420b81a790 --fetch
```

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev b5799ce55965d7879c41af980885f6420b81a790
custom command files found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md command token '/docs/en/commands.md' is not well-formed; entry row S901: S901 URL 'https://code.claude.com/docs/en/skills.md' is already a base SOURCES URL
reject Codex: SKILL.md command token '.codex-plugin/plugin.json' is not well-formed; entry row S902: quote holds no command/prompt word outside the token; S902 URL 'https://developers.openai.com/plugins/build/plugins.md' is already a base SOURCES URL
reject VS Code: SKILL.md command token '.github/agents' is not well-formed; entry row S903: quote holds no command/prompt word outside the token; S903 URL 'https://code.visualstudio.com/docs/agent-customization/custom-agents.md' is already a base SOURCES URL
reject Copilot CLI: SKILL.md command token '.github/copilot-instructions.md' is not well-formed; entry row S904: quote holds no command/prompt word outside the token; S904 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md command token '.gemini/settings.json' is not well-formed; entry row S905: quote holds no command/prompt word outside the token; S905 URL 'https://geminicli.com/docs/tools/mcp-server.md' is already a base SOURCES URL
reject Cursor: SKILL.md command token '.cursor/rules' is not well-formed; entry row S906: quote holds no command/prompt word outside the token; S906 URL 'https://cursor.com/docs/rules.md' is already a base SOURCES URL
reject opencode: SKILL.md command token '~/.config/opencode/skills/*/SKILL.md' is not well-formed; entry row S907: quote holds no command/prompt word outside the token; S907 URL 'https://opencode.ai/docs/skills.md' is already a base SOURCES URL
exit code: 1
```

```sh
timeout 900 python3 -B verifiers/check_command_files.py --rev b5799ce55965d7879c41af980885f6420b81a790
```

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev b5799ce55965d7879c41af980885f6420b81a790
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md command token '/docs/en/commands.md' is not well-formed; entry row S901: S901 URL 'https://code.claude.com/docs/en/skills.md' is already a base SOURCES URL
reject Codex: SKILL.md command token '.codex-plugin/plugin.json' is not well-formed; entry row S902: quote holds no command/prompt word outside the token; S902 URL 'https://developers.openai.com/plugins/build/plugins.md' is already a base SOURCES URL
reject VS Code: SKILL.md command token '.github/agents' is not well-formed; entry row S903: quote holds no command/prompt word outside the token; S903 URL 'https://code.visualstudio.com/docs/agent-customization/custom-agents.md' is already a base SOURCES URL
reject Copilot CLI: SKILL.md command token '.github/copilot-instructions.md' is not well-formed; entry row S904: quote holds no command/prompt word outside the token; S904 URL 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md' is already a base SOURCES URL
reject Gemini CLI: SKILL.md command token '.gemini/settings.json' is not well-formed; entry row S905: quote holds no command/prompt word outside the token; S905 URL 'https://geminicli.com/docs/tools/mcp-server.md' is already a base SOURCES URL
reject Cursor: SKILL.md command token '.cursor/rules' is not well-formed; entry row S906: quote holds no command/prompt word outside the token; S906 URL 'https://cursor.com/docs/rules.md' is already a base SOURCES URL
reject opencode: SKILL.md command token '~/.config/opencode/skills/*/SKILL.md' is not well-formed; entry row S907: quote holds no command/prompt word outside the token; S907 URL 'https://opencode.ai/docs/skills.md' is already a base SOURCES URL
exit code: 1
```

## Frozen counter SHA256 custody

At the initial frozen checkout, this command exited 0:

```sh
timeout 900 sha256sum verifiers/check_command_files.py verifiers/check_sweep_mutants.py
```

```text
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
f7664401095948fd84889de1767e4fa6a32b7dc25cb50f49de2c981543d3241f  verifiers/check_sweep_mutants.py
exit code: 0
```

After the scoring runs, the following commands checked out the same frozen commit and hashed the requested glob; both exited 0:

```sh
timeout 900 git checkout -q 3de87aad29e960c95ed35840442f424c48c29729
timeout 900 sha256sum verifiers/check_*.py
```

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
exit code: 0
```

## Smallest safe correction

No counter correction is required by these two observed controls. Keep the token-grammar, external-word and source-freshness conjuncts intact. This result does not justify widening the grammar to skills, agents, rules, manifests, settings or documentation paths.

No tools were installed or updated. No builds, linters, formatters, self-tests or C2 runs were performed; only the assigned C1 scoring and source/custody commands above.
