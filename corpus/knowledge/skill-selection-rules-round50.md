source: S024 (https://opencode.ai/docs/skills, `skills.md:72-73, 110`), S025 (https://code.visualstudio.com/docs/agent-customization/agent-skills, `agent-skills.md:64, 148, 302`), S026 (https://code.claude.com/docs/en/sub-agents, `sub-agents.md:77, 176, 839, 860, 1293`), S027 (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills, `add-skills.md:33, 233`), S028 (https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference, `cli-plugin-reference.md:415`), S029 (https://geminicli.com/docs/cli/skills/, `skills.md:51-52`), S022 (https://code.claude.com/docs/en/skills, `skills.md:198, 389, 1194, 1207`), S019 (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices, `best-practices.md:161, 206, 215`)
verified-at: 2026-10-22
recheck: for p in "https://opencode.ai/docs/skills.md f10ced73" "https://code.visualstudio.com/docs/agent-customization/agent-skills.md de5ba34f" "https://code.claude.com/docs/en/sub-agents.md 89aa73eb" "https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills.md 18c361b5" "https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md d0d362cc" "https://geminicli.com/docs/cli/skills.md 8e1b4cbe" "https://code.claude.com/docs/en/skills.md cdfcb0df" "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md f0a5d61b"; do set -- $p; curl -fsSL "$1" | sha256sum | grep -q "^$2" || echo "DRIFT $1"; done  # prints nothing on 2026-10-22T13:36Z (8 of 8 pages byte-identical to the recorded fetch); each DRIFT line names a page whose bytes moved, so its quotes must be re-located before this entry is cited again

# How clients choose between skills (round 50)

Frontier area: sibling arbitration (`PROVINCE.md` § Core). The round-49 census
(`sibling-overlap-census-round49.md`) found no documented tie-break between two skills whose
descriptions both match, on three pages (S022, S023, S018). This entry widens that to eight more
pages from five clients and says what the documented rules are keyed on. Every page was opened on
2026-10-22 by a round-50 build seat (reports under `../../.ufo/waves/round-50/build/Src*.md`) and its
bytes re-checked by the L1 at 13:36Z with the recheck above.

## What each client documents

| client | row | the description's role (quote, location) | "which one wins" rule documented | keyed on |
|---|---|---|---|---|
| opencode | S024 | "OpenCode lists available skills in the `skill` tool description." (`skills.md:110`); "Keep it specific enough for the agent to choose correctly." (`skills.md:73`) | "Ensure skill names are unique across all locations" (`skills.md:229`) | name |
| VS Code (GitHub Copilot in the editor) | S025 | "Copilot reads the skill's `name` and `description` from the YAML frontmatter." (`agent-skills.md:302`) | duplicate names across workspace roots: "the primary root takes precedence" (`agent-skills.md:64`, inside the page's experimental Codex-integration note) | name, location |
| Claude Code subagents | S026 | delegation uses "the `description` field in subagent configurations" (`sub-agents.md:839`) | same-name files: one loads, "chosen by filesystem read order rather than a documented precedence" (`sub-agents.md:176`); the built-in `claude` agent is used "When a task doesn't fit a more specialized agent." (`sub-agents.md:77`) | name; one fit-based default (built-in catch-all) |
| GitHub Copilot (cloud agent) | S027 | "Copilot will decide when to use your skills based on your prompt and the skill's description" (`add-skills.md:233`) | none on this page | — |
| GitHub Copilot CLI | S028 | — | "**Agents and skills** use first-found-wins precedence." (`cli-plugin-reference.md:415`) | name, load order |
| Gemini CLI | S029 | — | "If multiple skills share the same name, the version from the higher-precedence location is used." (`skills.md:51-52`) | name, location |
| Claude Code skills | S022 | "What the skill does and when to use it. Claude uses this to decide when to apply the skill." (`skills.md:389`, round 49) | name clash settled by origin (`skills.md:198`) | name, origin |
| Anthropic best practices | S019 | "Your description must provide enough detail for Claude to determine when to select this Skill" (`best-practices.md:215`) | none | — |

## Findings

1. **No client documents a rule between two differently named, author-written skills whose
   descriptions both match.** Sweep (Q14): each page's fetched markdown was searched with
   `grep -ciE` for `overlap`, `ambigu`, `precedence`, `tie[- ]?break`, `conflict`,
   `multiple skills`, `same name`, `prioriti`, `1024`, `truncat`; every non-zero hit is located in
   the seat reports and concerns a same-name collision, a length cap, site chrome or an unrelated
   sense. A wider sweep by falsify seat `../../.ufo/waves/round-50/falsify/CriticFrontierSweep.md`
   (choice words such as `choose`, `select`, `which skill`, `more speciali`) found one fit-based rule,
   finding 2, and no rule between two authored skills.
2. **One fit-based rule exists, for a built-in default only.** Claude Code uses its catch-all `claude`
   agent "When a task doesn't fit a more specialized agent." (S026 `sub-agents.md:77`). It prefers any
   specialized agent over the catch-all; it does not choose between two specialized ones.
3. **Every other documented rule is keyed on the name** (and the location, origin or load order that
   decides between two copies of one name). None compares two descriptions.
4. **The documented remedy for overlap is specificity in the description.** opencode: "specific
   enough for the agent to choose correctly" (S024 `skills.md:73`); Claude Code subagents: "Make each
   description specific enough to route to the right subagent" (S026 `sub-agents.md:1293`); Claude
   Code skills: "Make the description more specific" (S022 `skills.md:1194`).
5. **Length caps differ by client:** 1,024 characters for `description` (S024 `skills.md:72`, S025
   `agent-skills.md:148`, S019 `best-practices.md:161`); Claude Code truncates `description` plus
   `when_to_use` at 1,536 characters in its listing (S022 `skills.md:389`).

## What this changes for craft

Between two skills with different names, no client compares the two descriptions by any documented
rule, and the documented advice is to make each description specific. The description is not the
author's only lever: Claude Code also documents `when_to_use` (appended to the description in the
listing), `disable-model-invocation: true` and `paths` globs that limit activation (S022
`skills.md:390, 393, 403`). The description is the lever every client listed here reads. kotoba's checklist box `trigger.05`
(`../../SKILL.md` § Trigger-fidelity checklist) and its error-pattern line in `../../SKILL.md` § Anti-patterns
apply this: an overlapping description names its neighbour and the split, and stays under 1,024
characters. kotoba's own description does this for the 9 census lanes classed `adjacent`, checked by
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md`
(`skill description names 9 of 9 non-none lanes`, exit 0 at lane `542f515`).

## Limits

- These are documentation statements, not measured router behaviour; no harness here runs the lane
  `SKILL.md` files (they are outside the omp discovery roots).
- Pages move: S026's `last-modified` equals the fetch time, so the recheck compares content hashes,
  not dates.
- The negative in finding 1 covers these eight pages only.
