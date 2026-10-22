source: S030 (https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills, `skills.md:177-179, 697, 805-810`), S031 (https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference, `cli-command-reference.md:1278, 1300, 1304-1325`), S025 (https://code.visualstudio.com/docs/agent-customization/agent-skills, `agent-skills.md:150-151, 289-296`), S022 (https://code.claude.com/docs/en/skills, `skills.md:549, 577, 886, 894-907, 1194-1195`), S024 (https://opencode.ai/docs/skills, `skills.md:128-129, 133-156, 230`), S029 (https://geminicli.com/docs/cli/skills/, `skills.md:20-22, 94`), S021 (https://learn.chatgpt.com/docs/build-skills, `build-skills.md:183-189, 218`)
verified-at: 2026-10-22
recheck: for p in "https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md 64856ff4" "https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md c61997ef" "https://code.visualstudio.com/docs/agent-customization/agent-skills.md de5ba34f" "https://code.claude.com/docs/en/skills.md cdfcb0df" "https://opencode.ai/docs/skills.md f10ced73" "https://geminicli.com/docs/cli/skills.md 8e1b4cbe" "https://learn.chatgpt.com/docs/build-skills.md ed6e324f"; do set -- $p; curl -fsSL "$1" | sha256sum | grep -q "^$2" || echo "DRIFT $1"; done; python3 -B verifiers/check_overlap_levers.py --fetch

# Levers that take one of two overlapping skills out of the choice (round 51)

Frontier area: sibling arbitration (`PROVINCE.md` § Core). The round-50 entry
`skill-selection-rules-round50.md` found that no client documents a rule between two differently
named skills whose descriptions both match, and its finding 4 said "the documented remedy for
overlap is specificity in the description". This entry supersedes finding 4. On the same seven
clients, every page also documents a lever that does not touch the description wording: it removes
one named skill from the candidates. Each page was opened on 2026-10-22 by a round-51 build seat
(reports under `../../.ufo/waves/round-51/build/Src*.md`), and the L1 re-fetched the quoted lines at
15:08Z; the hashes in the recheck above are the bytes quoted.

## Levers by client

| client | row | lever | quote |
|---|---|---|---|
| GitHub Copilot SDK | S030 | the application lists skill names to disable in the session config, so those skills are never offered | "Use `disabledSkills` to exclude conflicting skills" (skills.md:809) |
| GitHub Copilot CLI | S031 | the user's settings exclude whole skill directories from discovery | "Use the `ignoredSkillsLocations` setting to exclude specific directories (and their descendants) from discovery, regardless of which location above would otherwise surface them." (cli-command-reference.md:1300) |
| VS Code | S025 | a frontmatter flag stops the agent loading the skill on its own; the `/` command still works | "Use the `user-invocable` and `disable-model-invocation` frontmatter properties to control how each skill is accessed:" (agent-skills.md:289) |
| Claude Code | S022 | a frontmatter flag takes the skill out of Claude's context; the user can still run `/name` | "**Hide individual skills** by adding `disable-model-invocation: true` to their frontmatter. This removes the skill from Claude's context entirely." (skills.md:886) |
| opencode | S024 | a permission `deny` pattern on the skill name hides the skill from the agent and rejects loading it | "Check permissions—skills with `deny` are hidden from agents" (skills.md:230) |
| Gemini CLI | S029 | a session command disables one named skill | "`/skills disable <name>`: Prevents a specific skill from being used." (skills.md:94) |
| Codex | S021 | a per-skill policy turns off implicit invocation; explicit `$skill` use still works | "`allow_implicit_invocation` (default: `true`): When `false`, Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works." (build-skills.md:218) |

Other levers on the same pages, not counted (seat reports): Copilot SDK `skillDirectories` (`:262`),
`enableSkills` (`:683`) and the frontmatter mapping of `disable-model-invocation` (`:648`); Copilot
CLI `disable-model-invocation` (a table row at `:1278`), `copilot skill disable <name>`
(`:1304-1325`) and `disabledSkills` in the config directory reference; VS Code `user-invocable`,
which hides the skill from the `/` menu while the agent can still load it (`:150`), the opposite
effect; Claude Code `skillOverrides` with `"off"` or `"user-invocable-only"` (`:894-907`) and
`paths` globs; opencode `opencode/autoinvoke` set to `"false"` (`:128-129`) and `tools: skill: false`
(all skills off); Gemini CLI `gemini skills disable` and the `skills.disabled` settings list; Codex
`[[skills.config]]` with `enabled = false` (`:183-189`).

## Findings

1. **Every one of the seven clients documents at least one lever, other than the description,
   that removes a named skill from the model's candidates.** The levers fall into three effects:
   removed everywhere (Copilot SDK, Copilot CLI, opencode, Gemini CLI), automatic choice off with
   manual use kept (VS Code, Claude Code, Codex), and outside a scope (directory or path
   settings, not counted here).
2. **None of the levers decides between two skills that both remain candidates.** Each removes
   one skill. Round-50 finding 1 stands: between two differently named skills that both match, the
   description is still the only lever the pages document. The one page that ties a lever to
   conflicts is the Copilot SDK's § Skill conflicts (`:805-810`), and its remedies are removal
   ("exclude") and reorganising directories; that section is about conflicting instructions after
   both skills load, not two descriptions matching one prompt (`CriticLearning.md`).
3. **Who holds the lever differs.** The skill author holds the frontmatter flags (VS Code, Claude
   Code, Codex); the user or operator holds settings, permissions and commands (Copilot CLI,
   opencode, Gemini CLI); the application developer holds the SDK session config (Copilot SDK).
   An author who does not own the neighbouring skill can only use the author-held levers on their
   own skill.
4. **The Claude Code row is carried, not new.** `disable-model-invocation` and `paths` were already
   named in `skill-selection-rules-round50.md` § What this changes for craft. Round-50 finding 4 cut
   its own source short: `skills.md:1194` ("Make the description more specific") is item 1 of a
   two-item list whose item 2 is "Add `disable-model-invocation: true` if you only want manual
   invocation" (`:1195`). Six of the seven rows are new to the corpus.

## What this changes for craft

When two skills overlap, rewriting the description is the only lever that keeps both skills
automatic. Reach for a removal lever instead when the skill should never fire unasked anyway (side
effects or timing, such as deploy or commit), when the split is by file location rather than by
intent, or when you do not own the other skill's file. The cost is real: a manual-only or disabled
skill also stops firing on prompts that only it matches. kotoba's `SKILL.md` § Anti-patterns carries
the table (checked by `python3 -B verifiers/check_overlap_levers.py`).

## omp, the lane's own harness (outside the seven-client count)

Seat `../../.ufo/waves/round-51/build/LeverOmp.md` read omp 18.12.6's shipped documentation
(`omp://skills.md`) and its binary: omp documents no tie-break either, and offers removal levers of
the same kinds: `hide: true` or `disable-model-invocation` (out of the prompt listing, still reachable
by `skill://` and `/skill:`), `enabled: false` (skipped in discovery), `skills.ignoredSkills` and
`skills.includeSkills`, and CLI `--skills <globs>` / `--no-skills`. omp's `globs` and `alwaysApply`
are metadata, not activation controls (`omp://skills.md:63`). No SOURCES row is written for omp's
shipped docs, so this paragraph is not counted and carries no row.

## Limits

- These are documentation statements, not measured client behaviour; no harness here runs these
  clients.
- The counted key terms come from a reviewed list frozen in `verifiers/check_overlap_levers.py`
  (`REVIEWED_LEVERS`). That list is a reviewer's judgment, not a measurement. The L1 added three
  terms before landing so that a quote could carry the exact backtick span:
  `ignoredSkillsLocations` (Copilot CLI; the per-skill lever sits in a table row whose pipes cannot
  be quoted inside a table cell), `disable-model-invocation: true` (Claude Code) and
  `/skills disable <name>` (Gemini CLI).
- The Copilot CLI row's lever works per directory, not per skill name.
- Pages move: the recheck compares content hashes; S030's page was byte-identical to the round-50
  spot-check fetch (`64856ff4…`).
- Secondary pages checked by seat `LeverOtherPages.md` add only all-or-nothing switches (for example
  VS Code `ChatStrictPluginOnlyCustomization`, Gemini CLI `skills.enabled`); none adds a per-skill
  lever missing from the skills pages.
