source: S030 (https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills, `skills.md:18, 179, 685, 805-810`), S031 (https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference, `cli-command-reference.md:1278, 1300, 1304-1325`), S025 (https://code.visualstudio.com/docs/agent-customization/agent-skills, `agent-skills.md:150-151, 289-296`), S022 (https://code.claude.com/docs/en/skills, `skills.md:347, 393, 549, 577, 886, 894-907, 1194-1195`), S024 (https://opencode.ai/docs/skills, `skills.md:45, 128-129, 133-188, 230`), S029 (https://geminicli.com/docs/cli/skills/, `skills.md:20-22, 75, 94, 118-120`), S021 (https://learn.chatgpt.com/docs/build-skills, `build-skills.md:183-189, 218`)
verified-at: 2026-10-22
recheck: rc=0; for p in "https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md 64856ff4" "https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md c61997ef" "https://code.visualstudio.com/docs/agent-customization/agent-skills.md de5ba34f" "https://code.claude.com/docs/en/skills.md cdfcb0df" "https://opencode.ai/docs/skills.md f10ced73" "https://geminicli.com/docs/cli/skills.md 8e1b4cbe" "https://learn.chatgpt.com/docs/build-skills.md ed6e324f"; do set -- $p; curl -fsSL "$1" | sha256sum | grep -q "^$2" || { echo "DRIFT $1"; rc=1; }; done; python3 -B verifiers/check_overlap_levers.py --fetch && test "$rc" -eq 0

# Levers that take one of two overlapping skills out of the choice (round 51)

Frontier area: sibling arbitration (`PROVINCE.md` § Core). The round-50 entry
`skill-selection-rules-round50.md` found that no client documents a rule between two differently
named, author-written skills whose descriptions both match, and its finding 4 said "the documented remedy for
overlap is specificity in the description". This entry supersedes finding 4. On the same seven
clients, every page also documents a lever that does not touch the description wording: it removes
one named skill from the candidates. Each page was opened on 2026-10-22 by a round-51 build seat
(reports under `../../.ufo/waves/round-51/build/Src*.md`), and the L1 re-fetched the quoted lines at
15:08Z; the hashes in the recheck above are the bytes quoted.

## Levers by client

| client | row | lever | quote |
|---|---|---|---|
| GitHub Copilot SDK | S030 | the application lists skill names to disable in that session's config ("Disable specific skills while keeping others active", `:179`; the page does not say whether a disabled skill leaves the catalog) | "Use `disabledSkills` to exclude conflicting skills" (skills.md:809) |
| GitHub Copilot CLI | S031 | a frontmatter field stops the agent invoking the skill on its own | "`disable-model-invocation` \| boolean \| No \| Prevent the agent from automatically invoking this skill." (cli-command-reference.md:1278) |
| VS Code | S025 | a frontmatter flag stops the agent loading the skill on its own; the `/` command still works | "`disable-model-invocation` \| No \| Controls whether the agent can automatically load the skill based on relevance." (agent-skills.md:151) |
| Claude Code | S022 | a frontmatter flag stops Claude loading the skill on its own and takes its description out of Claude's context; the user can still run `/name` | "`disable-model-invocation` \| No \| Set to `true` to prevent Claude from automatically loading this skill." (skills.md:393) |
| opencode | S024 | a skill metadata key keeps the skill out of the model-facing skill list; it can still be loaded by exact name | "Skills with `metadata["opencode/autoinvoke"]` set to `"false"` are not included in `<available_skills>`." (skills.md:128) |
| Gemini CLI | S029 | a command disables one named skill, in the user scope by default or one workspace with `--scope workspace` | "`/skills disable <name>`: Prevents a specific skill from being used." (skills.md:94) |
| Codex | S021 | a per-skill policy turns off implicit invocation; explicit `$skill` use still works | "`allow_implicit_invocation` (default: `true`): When `false`, Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works." (build-skills.md:218) |

Other levers on the same pages, not counted (seat reports): Copilot SDK `skillDirectories` (`:262`),
`enableSkills` (`:683`) and the frontmatter mapping of `disable-model-invocation` (`:648`); Copilot
CLI `ignoredSkillsLocations` (directories excluded from discovery, `:1300`), `copilot skill disable <name>`
(`:1304-1325`); VS Code `user-invocable`,
which hides the skill from the `/` menu while the agent can still load it (`:150`), the opposite
effect; Claude Code `skillOverrides` with `"off"` or `"user-invocable-only"` (`:894-907`) and
`paths` globs; opencode permission `deny` on the skill name (`:133-156, 230`; a per-agent `allow` can
override a global `deny`, `:160-188`) and `tools: skill: false` (all skills off); Gemini CLI `gemini skills disable` (CLI reference `cli-reference.md:130`) and the
`skills.disabled` settings list (configuration `configuration.md:2295-2296`; neither page has a row); Codex
`[[skills.config]]` with `enabled = false` (`:183-189`).

## Findings

1. **Every one of the seven clients documents at least one lever, other than the description,
   that removes a named skill from the model's candidates.** The counted levers fall into two
   effects: automatic choice off with manual use kept (Copilot CLI, VS Code, Claude Code, opencode,
   Codex) and removed in a scope (Copilot SDK per session, Gemini CLI per user or workspace). A
   third kind, outside a scope (directory or path settings), is not counted here.
2. **None of the levers decides between two differently named skills that both remain
   candidates.** (Claude Code does document one rule between two same-named nested skills that both
   stay available: Claude invokes the one whose directory holds the working files, `skills.md:183-186`;
   falsify `ReopenS022.md`.) Each removes
   one skill. Bounded to these seven pages; the sweeps are pasted in the seven source seat reports
   (`../../.ufo/waves/round-51/build/Src*.md`), and the falsify seats re-ran them (`Reopen*.md`). Round-50 finding 1 stands: between two differently named skills that both match, the
   description is still the only lever the pages document. The one page that ties a lever to
   conflicts is the Copilot SDK's § Skill conflicts (`:805-810`), and its remedies are removal
   ("exclude") and reorganising directories; that section is about conflicting instructions after
   both skills load, not two descriptions matching one prompt (`CriticLearning.md`).
3. **Who holds the lever differs.** The skill author holds the counted frontmatter or metadata
   levers (Copilot CLI, VS Code, Claude Code, opencode, Codex); the user holds the Gemini CLI
   command; the application developer holds the SDK session config (Copilot SDK).
   An author who does not own the neighbouring skill can only use the author-held levers on their
   own skill.
4. **The Claude Code row is carried, not new.** `disable-model-invocation` and `paths` were already
   named in `skill-selection-rules-round50.md` § What this changes for craft. Round-50 finding 4 cut
   its own source short: `skills.md:1194` ("Make the description more specific") is item 1 of a
   two-item list whose item 2 is "Add `disable-model-invocation: true` if you only want manual
   invocation" (`:1195`). Four of the seven counted levers are new to the corpus (see the corrections below).

## What this changes for craft

When two skills overlap, rewriting the description is the only lever these pages document that
keeps both skills automatic everywhere (Claude Code `paths` keeps both automatic for a split by
location). Reach for a removal lever instead when the skill should never fire unasked anyway (side
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
- Secondary pages checked by seat `LeverOtherPages.md` (about one per client) add only all-or-nothing
  switches (for example VS Code `ChatStrictPluginOnlyCustomization`, Gemini CLI `skills.enabled`).
  That check was not exhaustive: Gemini CLI's CLI reference (`gemini skills disable <name>`,
  `cli-reference.md:130`) and configuration page (`skills.disabled`, `configuration.md:2295-2296`)
  also carry per-skill levers (falsify `ReopenS029.md` F1); both are named under "Other levers" and
  neither is counted.

## Falsify-wave corrections (round 51, before the report)

Seat reports under `../../.ufo/waves/round-51/falsify/`. The table above was corrected in place before
the report; the rows it replaced (landed at lane `34cfffbb`) are recorded here.

- **Effects** (`CriticLeverSemantics.md`): the Copilot SDK's `disabledSkills` is set per session ("Enable/disable
  capabilities per session", `skills.md:18`), so its effect is "removed in a scope", not "removed
  everywhere"; Gemini CLI's `/skills disable` is user-scoped by default and workspace-scoped with
  `--scope workspace` (`skills.md:75, 118-120`), also "removed in a scope". opencode's permission `deny`
  can be overridden per agent (`skills.md:160-188`), so the row now counts the author-held metadata
  key `opencode/autoinvoke` (`skills.md:45, 128-129`) instead.
- **Copilot CLI** (`ReviewReviewedList.md`, `CriticC2Landed.md`): the row counted `ignoredSkillsLocations`,
  a per-directory lever labelled "removed everywhere", and the lesson gave a false reason for
  skipping the frontmatter field (escaped `\|` pipes do sit inside a table cell; the counter reads
  them). The row now counts `disable-model-invocation` (`cli-command-reference.md:1278`), held by the
  skill author.
- **VS Code and Claude Code quotes** (`CriticC2Landed.md` F4): the VS Code quote at `:289` did not state
  the effect and named `user-invocable`, whose effect is the opposite; the row now quotes the field's
  own table row (`:151`). Claude Code now quotes `:393` with the plain field name, so the reviewed
  list needs no `disable-model-invocation: true` variant.
- **Novelty** (`CriticLearningLanded.md`): four rows are new to the corpus (Copilot CLI, VS Code,
  Gemini CLI, Codex), not six. Claude Code's lever was in the round-50 entry; the Copilot SDK quote
  was in the round-50 spot-check (`corpus/lessons/round-50-verifier-spotcheck.md:189`); opencode's
  per-skill permission `deny` was in round-9 knowledge (`harness-router-models-round9.md:126`),
  though `opencode/autoinvoke` as a lever is new here.
- **Who holds a lever** (finding 3 above, corrected): after the corrections the skill author holds a
  counted lever on five of seven clients (Copilot CLI, VS Code, Claude Code, opencode, Codex); the
  application developer holds the Copilot SDK one; the user holds the Gemini CLI one.
- **Splitting by location**: the location branch of the craft advice rests on Claude Code's `paths`
  globs (`skills.md:403`) and Copilot CLI's `ignoredSkillsLocations` (`:1300`); neither is a counted
  row. "The skill should never fire unasked" follows Claude Code `skills.md:347, 549`.
- **Copilot SDK scope** (`ReopenS030.md`): the page also has a same-name rule (a provider skill
  replaces a file-based skill with the same name, `skills.md:685`) and a built-in exclusion under
  `mode: "empty"` (`:711-724`); neither decides between two differently named skills.
- **What the counter does not measure** (`CriticC2Landed.md`): it checks that each key term is an exact
  span in a quote on the reviewed page and that the row's labels come from the allowed words; whether
  the quote's sense and the `lever`, `held by` and `effect` cells match the page is reviewer judgment,
  checked by the falsify seats `Reopen*.md` and `CriticLeverSemantics.md`, not by the script.
