# LeverOtherPages — secondary doc pages vs the main skills pages (7 pinned clients)

Result: **no per-skill overlap lever exists only on a secondary page** for any of the 7 clients.
Four clients' secondary pages duplicate a per-skill lever already on their skills page; one
(GitHub Copilot SDK) has no selection lever on the secondary pages checked; the two
secondary-only levers found (Gemini CLI `skills.enabled`, VS Code `ChatStrictPluginOnlyCustomization`)
are whole-surface toggles that disable *all* skills, so they cannot stop one of two overlapping
skills from being chosen. C2 rows must cite skills pages; secondary pages are corroboration at most.

## Per client: what the secondary page adds

| Client | Secondary page opened | Lever there | On the client's skills page? |
|---|---|---|---|
| GitHub Copilot SDK | `docs/features/changing-tools.md`, `customization-locations.md` | none (only `skillDirectories` discovery) | per-skill lever is `disabledSkills`, on its own skills doc `:174-184` |
| GitHub Copilot CLI | `cli-command-reference.md`, `add-skills.md` | `copilot skill disable NAME`; `/skills` Enable/Disable | yes — `add-skills.md:149`; reference `:1304-1313` |
| VS Code | `enterprise/manage-ai-settings.md` | `ChatStrictPluginOnlyCustomization` (global) | **no** — global only; per-skill lever is on the skills page (`:151`, `:289-296`) |
| Claude Code | `permissions.md`, `managed-settings.md` | `Skill(skill:<name>)` deny; `strictPluginOnlyCustomization` | yes — `skills.md:846-866` (deny incl. "Disable all skills"), `:894-924` (`skillOverrides`) |
| opencode | `permissions.md`, `config.md` | `skill` permission key, pattern `deny` | yes — `skills.md:133-156` (same JSON example) |
| Gemini CLI | `settings` reference | `skills.enabled` (global, default true) | **no** — global only; per-skill `/skills disable <name>` is on the skills page `:94` |
| Codex | `config-reference` | `[[skills.config]] enabled=false`; `approval_policy.granular.skill_approval` | yes — `build-skills.md:181-189`; approval knob is scripts-only, not selection |

Count: 4 of 7 secondary pages merely duplicate a per-skill lever already on the skills page
(Copilot CLI, Claude Code, opencode, Codex); 1 of 7 adds no selection lever at all (Copilot SDK);
2 of 7 (Gemini CLI, VS Code) add a global toggle only. 0 of 7 add a new per-skill lever.

## Quotes (verbatim, line = line in fetched bytes; all ≤25 words)

- Gemini CLI settings reference, `:189`: ``| Enable Agent Skills | `skills.enabled` | Enable Agent Skills. | `true`  |``
  — Gemini skills page has zero occurrences of `skills.enabled` (`grep -c` = 0).
- Gemini CLI skills page, `:94`: ``- `/skills disable <name>`: Prevents a specific skill from being used.``
- VS Code enterprise settings, `:294`: "Set `ChatStrictPluginOnlyCustomization` when you also need to block standalone user and workspace skills, agents, instructions, and MCP servers."
- VS Code skills page, `:289`: "By default, all skills appear in the `/` menu. Use the `user-invocable` and `disable-model-invocation` frontmatter properties to control how each skill is accessed:"
- VS Code skills page, `:151`: "Controls whether the agent can automatically load the skill based on relevance."
- Claude Code permissions, `:138`: "A `Skill(skill:<name>)` deny rule instead"
- Claude Code skills page, `:848`: "**Disable all skills** by denying the Skill tool in `/permissions`:"
- Claude Code skills page, `:902-903`: `` `"user-invocable-only"` | Hidden | Yes `` / `` `"off"` | Hidden | Hidden ``
- opencode permissions, `:157`: "`skill` — loading a skill (matches the skill name)"
- opencode skills page, `:153`: "Skill hidden from agent, access rejected"
- Codex config reference, `:383`: "Per-skill enablement overrides stored in config.toml."
- Codex config reference, `:393`: "Enable or disable the referenced skill."
- Codex config reference, `:188`: "When `true`, skill-script approval prompts are allowed to surface."
- Codex build-skills, `:183`: "Use `[[skills.config]]` entries in `~/.codex/config.toml` to disable a skill without deleting it:"
- Copilot CLI command reference, `:1313`: "`enable <name>` / `disable <name>` | Enable or disable a skill by name."
- Copilot CLI add-skills, `:149`: "`copilot skill disable SKILL-NAME` and `copilot skill enable SKILL-NAME` to turn a skill off and back on"
- Copilot CLI command reference, `:688` + `:835`: "`--excluded-tools=TOOL ...` | These tools will not be available to the model." / "`skill` | Invoke custom skills"
- Copilot SDK skills doc, `:176`: "Disable specific skills while keeping others active:"
- Copilot SDK skills doc, `:184`: `disabledSkills: ["experimental-feature", "deprecated-tool"],`

## Notes that change how a C2 row may be worded

1. **Global toggles are not overlap levers.** `skills.enabled=false` (Gemini CLI) and
   `ChatStrictPluginOnlyCustomization` (VS Code) remove every skill, so they cannot stop one of two
   overlapping skills from being chosen. A C2 key term must not accept them. Same for Copilot CLI
   `--excluded-tools skill` and opencode `tools: {skill: false}` (`skills.md:192-203`): the tool is
   hidden for all skills.
2. **Deny kinds differ.** Copilot CLI `--deny-tool` accepts kinds `memory/read/shell/url/write` and
   MCP servers (command reference `:842-849`); `skill` is a *tool name* (`:830-836`), so the
   documented lever is `--excluded-tools skill`, not `--deny-tool=skill(name)`. Do not cite the
   latter as documented.
3. **Codex also has a per-skill enable/disable duplicate**, so a Codex row can cite either
   `build-skills.md:183-188` or `config-reference:381-393`; the approval knob
   (`approval_policy.granular.skill_approval`) gates skill *scripts* after selection and is not a
   selection lever.
4. **Claude Code's deny rules are already on its skills page** (`skills.md:846-866`), including the
   blanket `Skill` deny and `Skill(deploy *)`; the permissions page only repeats the parameter form.
   `syncClaudeAiSkills` (`settings.md:314`) is a sync switch, not a selection lever.
5. **VS Code documents per-skill hiding in frontmatter** on the skills page (both properties set =
   "Disabled skills", `:296`), plus `github.copilot.chat.skillTool.enabled` (`:196`), a tool toggle.
6. Route probes that did not resolve (recorded, not used): `learn.chatgpt.com/docs/config-reference`
   (404), `code.visualstudio.com/docs/copilot/reference/copilot-settings.md` (404, 9 B),
   `/docs/agents/reference/copilot-settings.md` (404, 9 B),
   `/docs/copilot/reference/copilot-settings-and-preferences.md` (404, 9 B);
   `code.visualstudio.com/docs/reference/default-settings.md` is a 766 B stub that defers to the
   Settings editor, so no enumerable VS Code setting list was obtainable this way.

## Evidence — every page opened with curl, no browser

Fetch root: `/fast/scratch/hyaku/kotoba-r51/build/LeverOtherPages/sources/` (scratch only).
Times UTC, 2026-10-22. Bytes and sha256 are of the saved body.

| URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://code.claude.com/docs/en/permissions.md | 14:19:46Z | 200 | 86703 | `b9e93331a3fb9f14cb834300106cc8fc9bb4cd799b0426d20cf0d3707488f724` |
| https://code.claude.com/docs/en/skills.md | 14:20:17Z | 200 | 111557 | `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456` |
| https://code.claude.com/docs/en/managed-settings.md | 14:21:47Z | 200 | 59226 | `7481ad8deb6f00aacd38e489e7ebf040fee96c451647718c9c023aa72d2b3bd5` |
| https://code.claude.com/docs/en/settings.md | 14:19:45Z | 200 | 41791 | `513768ecae767349…` (prefix only) |
| https://opencode.ai/docs/permissions.md | 14:19:47Z | 200 | 7436 | `de5ba0670ecc566f1c825162c67dbed554a35d249d4d0e38d2253fabe02beb56` |
| https://opencode.ai/docs/skills.md | 14:20:17Z | 200 | 5365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` |
| https://opencode.ai/docs/config.md | 14:19:47Z | 200 | 26060 | `fe28a438a1464cb5…` (prefix only) |
| https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 14:19:48Z | 200 | 22871 | `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` |
| https://code.visualstudio.com/docs/enterprise/manage-ai-settings.md | 14:20:18Z | 200 | 33047 | `49894046232ff57b4b964550f962cbc4a9a975930e910398b9dcb540960f073f` |
| https://geminicli.com/docs/cli/settings.md | 14:19:47Z | 200 | 37344 | `be5edf443e30b8a23cb7817983b88c5268e47d8b6afd7a88c71fe65fcdcd8a89` |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/settings.md | 14:19:47Z | 200 | 37345 | `f20e3dfa2c27974be9d2200a5d0f6804e45b09b90810b432ca9bebec9fc355e2` |
| https://geminicli.com/docs/cli/skills.md | 14:20:18Z | 200 | 5763 | `8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590` |
| https://developers.openai.com/codex/config-reference.md | 14:20:18Z | 200 | 136297 | `fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21` |
| https://learn.chatgpt.com/docs/build-skills.md | 14:20:42Z | 200 | 11035 | `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` |
| https://learn.chatgpt.com/docs/enterprise/skills.md | 14:20:18Z | 200 | 3551 | `cea03f3708d47495…` (prefix only) |
| https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 14:21:47Z | 200 | 461944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |
| https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md | 14:22:05Z | 200 | 10057 | `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0` |
| https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/allowing-tools.md | 14:21:47Z | 200 | 11021 | `dc342f3e7c9ba8a62cf1fc4106e52192c592f35fd813f272040b1c4200a44515` |
| https://raw.githubusercontent.com/github/copilot-sdk/main/docs/features/skills.md | 14:21:04Z | 200 | 33484 | `6a4838e226a1c9d7cbc6a5ec4f11fc1cd4fc482cf1f1f4a46df5c056d5995830` |
| https://raw.githubusercontent.com/github/copilot-sdk/main/docs/features/customization-locations.md | 14:23:00Z | 200 | 5312 | `943487ebb298cb5a…` (prefix only) |

`allowing-tools.md` contains no occurrence of "skill" (`grep -i skill` empty), so the CLI's
tool-permission page documents no skill-specific deny; the tool names and `--excluded-tools` live in
the command reference.

## Commands run (exit codes verbatim)

- fetch loop batch 1 (five URLs): exit 0; each line printed `UTC HTTP bytes sha256-prefix URL`.
- fetch loop batch 2 (five URLs): exit 0; includes the single 404 `learn.chatgpt.com/docs/config-reference`.
- fetch loop batches 3–9: exit 0 each.
- `grep -n -i …` / `sed -n … | nl -ba` over saved bodies for each quote above: exit 0 (no-match greps
  exit 1, noted where they prove absence: `grep -c 'skills.enabled'` on Gemini skills page → `0`,
  exit 1; `grep -i skill` on `allowing-tools.md` → empty, exit 1).
- `python3 -c` on `api.github.com/repos/github/copilot-sdk/contents/docs` and `…/docs/features`: exit 0.

No writes outside `/fast/scratch/hyaku/kotoba-r51/build/LeverOtherPages/` and this report.
No installs or upgrades were needed.
