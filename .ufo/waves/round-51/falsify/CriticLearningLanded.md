HOLDS-BOUNDED — C2 as landed meets the learning-claim bar. It is a stronger entry superseding round-50 finding 4, plus a SKILL.md decision table, on PROVINCE Core ground ("Sibling arbitration"). The counter reproduces 0 of 7 at BASE and 7 of 7 at HEAD. Two bounds are needed before the report credits it. First, the entry's "Six of the seven rows are new to the corpus" is false: by grep over `corpus/` at BASE, 4 of 7 rows are new and 3 are carried. Second, the "held by" column misleads an author on 2 clients: Copilot CLI and opencode also document a lever the skill author holds, and the table omits it.

Seat: KotobaR51.CriticLearningLanded (critic, falsify wave, round 51). BASE `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`, HEAD `59903b2637689739a5b9901956301da72d0effe1`. Started 2026-10-22T15:14Z. No tools installed. The only lane file written is this report. The private clone is at `/fast/scratch/hyaku/kotoba-r51/falsify/CriticLearningLanded/lane`.

## Bar (goal file § Quality bar, lines 145-149)

The bar requires "a stronger entry superseding a weaker one" or "a SKILL.md decision table or error pattern grounded in admitted entries". C2 lands both. Before C2, the error pattern at `SKILL.md` (BASE) said "the documented remedy is a more specific description". That was a cut-short reading of S022 (`skills.md:1194-1195`). At HEAD, `SKILL.md` § Anti-patterns says when to rewrite the description and when to use a lever, and it states the cost. So kotoba now knows more about Core ground and can act on it. The defects below bound the claim. None of them voids it.

## Checklist: the four bounds from build critique `CriticLearning.md`

1. Claude Code row labelled carried: MET in the entry (finding 4, lines 56-60). It is NOT MET for the novelty count: see F1.
2. A sentence saying no lever is a tie-break: MET. It is in `SKILL.md` (the "Overlap levers by client" paragraph, "none decides between two skills that both remain candidates") and in entry finding 2.
3. A "held by" column: the column is PRESENT but WRONG for 2 clients. It ignores the critique's own correction, "Where a client has both, list the author-held lever first". See F2.
4. An "effect" column that does not carry Claude Code's context statement over to other clients: MET. The values are `removed everywhere` and `automatic choice off`. "out of Claude's context" appears only in the Claude Code lever cell. The VS Code cell says only "manual `/` invocation only".

## Findings

F1 — The novelty count is overstated: 4 of 7 rows are new to the corpus, not 6 of 7. (Attacks: entry finding 4, "Six of the seven rows are new to the corpus".)
- Claude Code (carried, as the entry says): `disable-model-invocation` is already in BASE `sibling-overlap-census-round49.md:32`, `skill-selection-rules-round50.md:55` and `lessons/round-50.md:153`.
- Copilot SDK (carried, NOT labelled): BASE `corpus/lessons/round-50-verifier-spotcheck.md:189` already quotes the row's exact sentence, "Use `disabledSkills` to exclude conflicting skills", with the same page hash `64856ff4…`. That file is a spot-check lesson, not admitted knowledge. So the new part is "admitted as knowledge, with a row", not "new to the corpus". The build critique's own evidence line already shows `disabledSkills 1 (the spot-check lesson only)`, yet it still said 6 of 7.
- opencode (carried, NOT labelled): two earlier records exist.
  - BASE `corpus/SOURCES.md:37` (row S024, `mined`) already says the page's "only collision controls are name uniqueness across locations and `opencode/autoinvoke: "false"`, which removes a skill from model-facing guidance".
  - The per-skill `deny` lever (this row's key term) is in admitted knowledge from opencode source since round 9: "per-skill deny filtered at `skill/index.ts:314`" (`harness-router-models-round9.md:125-126`; `lessons/round-8.md:89-90`).
  - So the opencode row is a documentation quote for a lever the lane already knew from source code.
- New at BASE, 0 files under `corpus/` for the term: Copilot CLI `ignoredSkillsLocations`, Gemini CLI `/skills disable`, Codex `allow_implicit_invocation`. VS Code is also new: the term `disable-model-invocation` occurs at BASE only in Claude Code contexts (all 5 hits are S022 or Claude Code text), and `user-invocable` has 0 files.
- Impacted axes: depth (provenance), the honesty of the learning claim. The counter's 7 of 7 still stands, because it counts backing, not novelty.
- Smallest correction: one appended line in the entry. It should say "4 of 7 rows are new (Copilot CLI, VS Code, Gemini CLI, Codex). Claude Code, Copilot SDK (round-50 spot-check, line 189) and opencode (S024 cell; round-9 source reading) are carried." The round report should state the learning as 4 new clients plus the corrected decision rule.

F2 — The "held by" column tells an author that Copilot CLI and opencode give them no lever. Both pages document one. (Attacks: entry finding 3, the `SKILL.md` table, bound 3.)
- Copilot CLI `cli-command-reference.md:1278` (fetched bytes, sha256 prefix `c61997efd7c93932`, same as S031): "`disable-model-invocation` | boolean | No | Prevent the agent from automatically invoking this skill." This is a frontmatter field, held by the skill author.
- opencode `skills.md:128-129` (sha256 prefix `f10ced73971ce83b`, same as S024): "Skills with `metadata["opencode/autoinvoke"]` set to `"false"` are not included in `<available_skills>`." This is set in the skill file, so the author holds it.
- The entry lists both under "Other levers on the same pages, not counted" (lines 29-34). Its finding 3 still classifies both clients as operator-held ("the user or operator holds settings, permissions and commands (Copilot CLI, opencode, Gemini CLI)"). Its Limits give the cause: the per-skill Copilot CLI lever "sits in a table row whose pipes cannot be quoted inside a table cell" (lines 87-89). A counter-mechanics constraint picked the operator-held lever.
- Effect on an author: the paragraph tells authors to use a lever "when you do not own the other skill". The table then shows an author-held lever for 3 of 7 clients. The pages document one for 5 of 7. Only Gemini CLI and the Copilot SDK lack one.
- Impacted axes: depth, and the correctness of `SKILL.md` § Anti-patterns as a decision aid.
- Smallest correction: add the author-held lever to the Copilot CLI and opencode lever cells as a second clause ("also frontmatter `disable-model-invocation`, skill author"), or add an appended line in the entry correcting finding 3. The counted key term need not change.

F3 — The "split by location" branch of the decision rule has no row to act on. (Attacks: whether `SKILL.md` lets an author act.)
- `SKILL.md` says to use a lever "when the split is by location rather than intent". Every table row has effect `removed everywhere` or `automatic choice off`. The only location-scope lever on the pages, Claude Code `paths` (`skills.md:403`, "loads the skill automatically only when working with files matching the patterns"), is not in the table. The entry also says scope levers are "not counted here" (finding 1).
- Counterexample to the entry's "rewriting the description is the only lever that keeps both skills automatic" (line 64): a `paths` glob keeps a skill automatic inside its scope. So two skills split by `paths` both stay automatic.
- Smallest correction: name `paths` (Claude Code) in the location branch of the `SKILL.md` sentence. In the entry, change "keeps both skills automatic" to "keeps both skills automatic everywhere".

F4 — The "never fires unasked" branch has a vendor basis that the entry does not cite. (Bounded. Not a defect in the claim.)
- Claude Code `skills.md:347` (same bytes as S022, `cdfcb0df`): "These are often actions you want to invoke directly with `/skill-name` rather than letting Claude decide when to run them." The entry's "side effects or timing, such as deploy or commit" has no location. The other two branches ("location", "do not own") are the lane's own inference, which is acceptable for a craft rule but should be marked as such.
- Correction (optional): cite `S022 skills.md:347` beside the side-effects branch.

## Restated or new (summary)

- New knowledge: levers for 4 clients (Copilot CLI, VS Code, Gemini CLI, Codex); the three-way effect typology; the holder distinction (needs F2 to be right); and the explicit "no lever is a tie-break" bound over 7 clients.
- Restated with a better source: Claude Code (round 49 and 50), Copilot SDK (round-50 spot-check), opencode (S024 cell; round-9 source reading).
- New capability for an author: a decision rule for when to rewrite the description and when to use a lever, with the cost stated. The F2 and F3 fixes are needed for it to send authors to the right lever on every client.

## Evidence (commands, exit codes)

- `git rev-parse HEAD` (lane) → `59903b2637689739a5b9901956301da72d0effe1`, exit 0.
- `git diff 43ca0bfb 59903b26 -- SKILL.md` → shows the rewritten error pattern and the new paragraph with its 7-row, 6-column table, exit 0.
- Term counts: `git grep -l -F -e <term> 43ca0bfb -- corpus | wc -l`, exit 0. Results:
  - 1 file: `disabledSkills`, `skillOverrides`, `autoinvoke`
  - 0 files: `ignoredSkillsLocations`, `/skills disable`, `skills disable`, `allow_implicit_invocation`, `user-invocable`, `enabled = false`
  - 4 files: `disable-model-invocation`
  - 3 files: `disable-model-invocation: true`, `deny`
  - Every `deny` hit is in round-8, round-9 or round-10 opencode source or harness text.
- `git grep -n -F -e 'exclude conflicting' 43ca0bfb -- corpus` → `corpus/lessons/round-50-verifier-spotcheck.md:189`, exit 0.
- `git show 43ca0bfb:corpus/knowledge/harness-router-models-round9.md | sed -n '118,132p'` → line 126 "per-skill deny filtered at `skill/index.ts:314`", exit 0.
- The same five terms (`disabledSkills`, `ignoredSkillsLocations`, `disable-model-invocation`, `/skills disable`, `allow_implicit_invocation`) in `SKILL.md PROVINCE.md` at BASE → 0 files each, exit 0.
- Private clone at HEAD, `python3 -B verifiers/check_overlap_levers.py` → `overlap levers backed 7 of 7 clients`, exit 0. With `--rev 43ca0bfb…` → `overlap levers backed 0 of 7 clients` (each row "SKILL.md table absent"), exit 1.
- Page bytes reused from the build seat's fetch at `/fast/scratch/hyaku/kotoba-r51/build/CriticLearning/pages/`. No new fetch was made. `sha256sum cliref.md opencode.md` → prefixes `c61997efd7c93932`, `f10ced73971ce83b`, which match S031 and S024, exit 0. Lines read: `cliref.md:1278`, `opencode.md:128-129`, `opencode.md:231`, `cc.md:347`, `cc.md:403`.
- Not run: `--fetch`, the counter's `--self-test`, and any model or client call.
