VERDICT: FAILS (fixable): 3 of the 7 `effect` cells contradict the vendor page, 2 more hold only within a bound, and 1 `held by` cell holds only within a bound. The verifier checks neither column, so its count of 7 of 7 cannot detect these errors.

Seat: KotobaR51.CriticLeverSemantics (critic). Attacks the `held by` and `effect` columns of `SKILL.md` § Anti-patterns, "Overlap levers by client" (`SKILL.md:394-402`), at HEAD 59903b26. The cells were checked against the seven vendor pages, which I fetched at 15:14:28-29Z. Every hash matches the recheck pins in the knowledge entry.

## Findings, row by row

| client (row) | landed held by / effect | page says | judgment | corrected cells |
|---|---|---|---|---|
| Copilot SDK (S030) | app developer / removed everywhere | `disabledSkills` is a `SessionConfig` field (sdk.md:697-700). The page lists "Enable/disable capabilities per session" (sdk.md:18). | held by HOLDS; effect FAILS (it is per session) | lever "list the name in `disabledSkills` when the app creates a session"; effect "removed from that session" |
| Copilot CLI (S031) | user or operator / removed everywhere | "exclude specific directories (and their descendants) from discovery" (cli.md:1300) | held by HOLDS; effect FAILS (it is per path, and the name can still surface) | effect `outside a scope`; or swap the lever (see finding 2) |
| VS Code (S025) | skill author / automatic choice off | "Set to `true` to require manual invocation through the `/` slash command only." (vscode.md:151) | HOLDS | none |
| Claude Code (S022) | skill author / automatic choice off | "Description not in context, full skill loads when invoked" (claude.md:577) | HOLDS | none |
| opencode (S024) | user or operator / removed everywhere | The skill permission can be overridden per agent (opencode.md:160-188). Custom agents set it in their own frontmatter (:164-171). | held by HOLDS-BOUNDED; effect FAILS (a per-agent `allow` overrides a global `deny`) | effect "removed for the agents the rule covers"; or swap the lever (see finding 2) |
| Gemini CLI (S029) | user or operator / removed everywhere | "`/skills disable` and `/skills enable` default to the `user` scope." (gemini.md:75). `--scope` is "`user` (global, default) or `workspace` (local to the project)" (:120-121) | held by HOLDS; effect HOLDS-BOUNDED (only the default user scope is global) | lever "`/skills disable <name>` (user scope by default; `--scope workspace` for one project)"; effect "removed everywhere (default user scope)" |
| Codex (S021) | skill author / automatic choice off | "explicit `$skill` invocation still works" (codex.md:218). The policy is set in the skill's `agents/openai.yaml` (:195-207). | HOLDS | none |

1. **Copilot CLI: the row breaks the entry's own rules.** Finding 1 of the knowledge entry
   (`skill-overlap-levers-round51.md:40-44`) sorts "directory or path settings" under `outside a scope` and says
   these are "not counted here". Yet the Copilot CLI row counts exactly such a setting and labels it `removed everywhere`.
   The entry's Limits concede "The Copilot CLI row's lever works per directory, not per skill name" (:91). `SKILL.md:387` says "each
   client documents a lever that removes one named skill".
   - **Counterexample** (from the page): the CLI loads skills "in priority order (first found wins for duplicate names)"
     (cli.md:1282). Suppose a user excludes the project's `.github/skills/foo/`. A personal `~/.copilot/skills/foo/` with the same name then
     wins and is still offered, so the named skill is not removed. The reverse also fails: excluding `.github/skills/` drops
     every project skill, not one.
   - **Why it happened:** the lesson rejected the name-keyed `:1278` quote because a table row contains `|` characters
     (`corpus/lessons/round-51.md` § Rejected). That quoting constraint chose the lever, but the effect cell was not adjusted to match.
2. **The `held by` column lists the user-held lever even where the same page also documents an author-held one.** The build critic asked: "Where a client has both,
   list the author-held lever first" (`.ufo/waves/round-51/build/CriticLearning.md` F3). The landed table does not do this for two clients:
   - Copilot CLI documents `disable-model-invocation`, "Prevent the agent from automatically invoking this skill" (cli.md:1278).
   - opencode documents `opencode/autoinvoke` "to keep the skill out of model-facing auto-selection guidance" (opencode.md:45, :128-129).

   On the opened pages, an author-held "automatic choice off" lever exists for 5 of 7 clients (Copilot CLI, VS Code,
   Claude Code, opencode, Codex). The Copilot SDK maps the same field only for skills its provider serves (sdk.md:648).
   Only Gemini's page has none. The table shows 3 of 7. A skill author reading `SKILL.md` "when you do not own the other skill"
   would conclude that on opencode and Copilot CLI only the operator can act, and the pages say otherwise.
3. **The SDK and Gemini cells blur two questions: where the lever is set, and what it removes.** The `effect` vocabulary
   (`check_overlap_levers.py:119`) has no value for "removed, but only in a session, settings or agent scope". So four rows
   with four different scopes all became `removed everywhere`. The knowledge entry also calls Gemini's lever "a session command"
   (`:25`). The command does run inside a session, but by `:75-76` it acts on a settings scope. [INFERENCE: the setting outlives the session; the page does not say so outright.]
4. **No check covers the columns.** The verifier checks only the vocabulary (`check_overlap_levers.py:345-351`). In probe A
   I relabelled VS Code as `app developer` / `removed everywhere` and Codex as `user or operator` / `outside a scope`.
   The counter still printed `overlap levers backed 7 of 7 clients` with exit 0. The entry's Limits call `REVIEWED_LEVERS` a judgment,
   but they say nothing of the two classification columns, so the 7 of 7 result reads as if it covered them.

## Smallest safe correction (a fixable defect, not a tradeoff)

- **Copilot CLI:** set effect to `outside a scope`, and set lever to "exclude a skills directory (and all below it) from discovery;
  by path, not name". This passes the verifier as-is (probe B: Copilot CLI BACKED).
- **opencode:** swap to the author-held lever. Use lever "`opencode/autoinvoke` set to false in skill metadata", held by `skill author`,
  effect `automatic choice off`, and key term `opencode/autoinvoke`. Change the entry quote to "`opencode/autoinvoke`: set to"
  (skills.md:45). With this quote, probe C printed 7 of 7, exit 0. A quote with inner double quotes is rejected ("entry quote malformed", probe B2).
  If `deny` is kept instead, its effect cell must name the per-agent override.
- **Copilot SDK and Gemini:** replace the vocabulary value `removed everywhere` with `removed in its scope`, and name the scope in
  the lever cell: "per session" for the SDK, "user scope by default, or `--scope workspace`" for Gemini. This needs `ALLOWED_EFFECTS` edited
  (probe B: "effect not allowed ('removed from that session')", exit 1).
- **Entry:** fix finding 1's grouping and finding 3's per-client sentence ("the user or operator holds ... (Copilot CLI,
  opencode, Gemini CLI)") to match.
- **Counter:** unaffected by the cell edits. The C2 claim of 7 of 7 counts backing, not classification, and should say so.

Impacted axes: depth (the C2 claim content), correctness of `SKILL.md` § Anti-patterns, and provenance (how far the quotes are allowed to stretch).
Not attacked: the existence of each lever, and the quotes themselves. All seven quoted lines are verbatim on the fetched bytes.

## Evidence

Sources (curl -sSL, read-only, no code executed). All fetched 2026-10-22 and returned HTTP 200:

| page | time (UTC) | bytes | sha256 |
|---|---|---|---|
| https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md | 15:14:28 | 35455 | 64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3 |
| https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 15:14:28 | 461944 | c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9 |
| https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 15:14:28 | 22871 | de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5 |
| https://code.claude.com/docs/en/skills.md | 15:14:28 | 111557 | cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456 |
| https://opencode.ai/docs/skills.md | 15:14:29 | 5365 | f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561 |
| https://geminicli.com/docs/cli/skills.md | 15:14:29 | 5763 | 8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590 |
| https://learn.chatgpt.com/docs/build-skills.md | 15:14:29 | 11035 | ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5 |
| https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md (context only) | 15:15:18 | 166811 | 8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0 |

The config-dir page shows that Copilot CLI also has a name-keyed `disabledSkills`: "Skill names to disable. Listed skills are discovered but not loaded." (clicfg.md:461). A repository can add entries: "Union—repository can add entries, never remove" (:566). `ignoredSkillsLocations` is not among the repo-overridable keys (`rg` matched only :473).

Commands. The private clone is at /fast/scratch/hyaku/kotoba-r51/falsify/CriticLeverSemantics/lane, checked out at 59903b26. Every probe was restored afterwards, and `git status --short | wc -l` printed 0.
- `python3 -B verifiers/check_overlap_levers.py` (lane, read-only): `overlap levers backed 7 of 7 clients`, exit 0.
- Probe A, the VS Code and Codex cells relabelled: `overlap levers backed 7 of 7 clients`, exit 0.
- Probe B, Copilot CLI set to `outside a scope`, the SDK set to `removed from that session`, opencode swapped without an entry quote: `overlap levers backed 5 of 7 clients`, exit 1. The SDK failed with "effect not allowed"; Copilot CLI passed.
- Probe B2, the opencode quote with inner double quotes: `entry quote malformed (opencode)`, 6 of 7, exit 1.
- Probe C, the opencode swap with the quote "`opencode/autoinvoke`: set to": `overlap levers backed 7 of 7 clients`, exit 0.

Tools installed: none. No lane file was touched except this report.
