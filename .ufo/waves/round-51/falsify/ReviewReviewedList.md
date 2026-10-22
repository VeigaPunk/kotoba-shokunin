Verdict: FAILS (the Copilot CLI term `ignoredSkillsLocations` widens the counter's accepted levers to fit the data, and the rejection reason given for it is false; the Claude Code and Gemini CLI additions HOLD; opencode `deny` is HOLDS-BOUNDED: a real lever, but it backs a false world as listed)

Seat: KotobaR51.ReviewReviewedList (falsify, round 51). Attacks: the L1's three additions to `REVIEWED_LEVERS` in `verifiers/check_overlap_levers.py` (commit 34cfffbb compared with 7c81a787), plus the generic opencode term `deny`. Impacted axes: depth (C2 count), calibration (the Gate record and how the labels are worded).

## Per-term verdicts

| term (client) | real per-skill removal lever on its page? | held-by / effect labels | stricter alternative available? | verdict |
|---|---|---|---|---|
| `ignoredSkillsLocations` (Copilot CLI) | per directory, not per skill name | effect "removed everywhere" contradicts the source seat and the entry's own finding 1 | yes: `disable-model-invocation`, already on the list, same page, same row, checked live | FAILS |
| `disable-model-invocation: true` (Claude Code) | yes, same lever as the term already listed | skill author / automatic choice off: correct | yes (`:393` with the term already listed), but the `:886` quote states the effect better | HOLDS |
| `/skills disable <name>` (Gemini CLI) | yes ("Prevents a specific skill from being used.", `skills.md:94`) | user or operator / removed everywhere: correct for the default user scope | no: the only exact `/skills disable` code span is at `:75`, which was correctly rejected | HOLDS |
| `deny` (opencode, already on the list at 7c81a787) | yes on `skills.md:153,230` | correct | yes: bind the term to the skills page | HOLDS-BOUNDED |

## Findings

**F1. Copilot CLI: the term was added on a false reason, and a stricter term already on the list was available (FAILS).**
- The rejection reason in the lesson (`corpus/lessons/round-51.md:72-74`) says the `:1278` table row's cells "are separated by `|`, which cannot sit inside a markdown table cell". That is false on the counter's own code: `CELL_SPLIT = (?<!\\)\|`, and `split_row` turns `\|` back into `|`.
- It is also false on the seat evidence the L1 had. `SrcCopilotCli.md:63-65` gave the escaped-pipe quote, said "the counter's split_row unescapes them", and reported `BACKED` with the quote found by `--fetch` (`:83`).
- Counterexample (world `w_cli`): I put back the seat's row (`disable-model-invocation`, skill author, automatic choice off, quote `"`disable-model-invocation` \| boolean \| No \| Prevent the agent from automatically invoking this skill." (cli-command-reference.md:1278)`). Results: `BACKED GitHub Copilot CLI` with the pre-extension list from 7c81a787; `--fetch` gives `FETCH GitHub Copilot CLI: quote found` and `quotes found on live pages 7 of 7`, exit 0.
- So the addition was not needed, and it swapped a per-skill lever for a per-directory one.
- This is the M33 class (a Gate reason that is false on evidence the author had) in the same round that added the M33 fix.
- Labelling:
  - The source seat classified the term as "scope/outside-a-scope by path" (`SrcCopilotCli.md:32`).
  - The entry's finding 1 (`skill-overlap-levers-round51.md:40-44`) files "directory or path settings" under "outside a scope … not counted here", yet that is exactly the lever counted for Copilot CLI.
  - `SKILL.md:397` labels it "removed everywhere" and words it "exclude the skill's directory". The page (`cli-command-reference.md:1300`) says "exclude specific directories (and their descendants)", and the entry's own Limits say "per directory, not per skill name".
  - S031's own scope cell promises "The per-skill removal levers", and its teaches cell leads with `disable-model-invocation`.
- [INFERENCE] Because "Each skill lives in its own directory" (`:1267`), pointing the setting at one skill's directory probably excludes just that skill. The page does not say so.
- The counter cannot catch the label error: `held_by` and `effect` are only checked against the allowed vocabulary (`check_overlap_levers.py:345-352`), not fixed per client.
- Is this Q26-class? For this one term, yes. The accepted set gained a new lever class (directory discovery exclusion) in the same commit that makes the count pass, with no reviewer seat on that addition (`LeverGuard.md:46-50` lists the 7c81a787 terms only). The plan's wording "a key term from the script's reviewed per-client list" then overstates its review for this term.
- Smallest safe correction:
  - Drop `ignoredSkillsLocations` from `REVIEWED_LEVERS`.
  - Restore the seat's `:1278` row (`disable-model-invocation`, skill author, automatic choice off) with the escaped-pipe quote.
  - Replace the Gate reason with an erratum.
  - Make finding 1 list Copilot CLI under "automatic choice off".
  - Optional and wider: `disabledSkills` on `cli-config-dir-reference.md:461` ("Listed skills are discovered but not loaded", per `SrcCopilotCli.md:31`) is a per-name lever with the effect "removed everywhere". It needs a new row and a list entry.

**F2. Claude Code `disable-model-invocation: true`: same lever, written with its on value (HOLDS).**
- `skills.md:886` reads: "**Hide individual skills** by adding `disable-model-invocation: true` to their frontmatter. This removes the skill from Claude's context entirely."
- `:393` keeps `/name` usable, so "skill author / automatic choice off" is right.
- The added string can only match the lever already listed, so the accepted meanings do not grow.
- A stricter alternative existed. World `w_cc` (the seat's `:393` escaped-pipe quote with the listed `disable-model-invocation`) gives `BACKED Claude Code` with the 7c81a787 list and is found live by `--fetch`.
- The L1's choice of `:886` (it states the effect) is defensible. But the Limits sentence implies the addition was forced by the quote, when it was a choice of quote. Bound that wording.

**F3. Gemini CLI `/skills disable <name>`: completes a listed term to its documented form (HOLDS).**
- The 7c81a787 terms `/skills disable` and `skills disable` match only `skills.md:75`. That line states a scope default, and its rejection is correct on the page bytes ("default to the `user` scope").
- `:94` is the effect line, and its exact code span is `/skills disable <name>`. `SrcGemini.md:5,184` reported that span at 11:50 (-03:00), before the counter commit at 12:07. So the 7c81a787 list was never reconciled with the seat's spans, and this addition repairs that.
- Combined world `w_both` (the CLI and Claude Code alternatives together, pre-extension list): `overlap levers backed 6 of 7 clients`, and only `UNBACKED: key term not a reviewed overlap lever (Gemini CLI)` remains. Gemini is the one client whose 7 of 7 genuinely needed a list change.
- Minor: "session command" (`SKILL.md:401`) undersells the scope note at `:75`. [INFERENCE] The disable is written at user scope (or workspace scope with `--scope workspace`), not only for the session.

**F4. opencode `deny`: a real lever, but the term is generic and backs a false world (HOLDS-BOUNDED).**
- On S024 the lever is real and the labels are right: `skills.md:153` reads "`deny` | Skill hidden from agent, access rejected"; `:230` reads "Check permissions—skills with `deny` are hidden from agents".
- Counterexample (world `w_oc`): a new row S099 (`https://opencode.ai/docs/agents`, docs, A, mined, used-by the entry, listed under the Gate) quoting `agents.md:638`: "When set to `deny`, the subagent is removed from the Task tool description entirely, so the model won't attempt to invoke it."
  - That sentence is about subagents, not skills.
  - Result with the HEAD list: `BACKED opencode`, `overlap levers backed 7 of 7 clients`, exit 0.
  - `--fetch`: `FETCH opencode: quote found (https://opencode.ai/docs/agents)`, `quotes found on live pages 7 of 7`, exit 0.
- So `deny` alone does not tie the count to skills. Any opencode docs page with a backticked `deny` in a removal sentence passes. The permissions page uses `"deny"` with quotes, which does not match exactly, so the agents page is the live hit.
- Smallest safe correction: tie each reviewed term to the page that was reviewed for it (for example `REVIEWED_LEVERS["opencode"] = {"deny": "https://opencode.ai/docs/skills", ...}`, checked against the row's first URL), and add `w_oc` as a self-test mutant. The same pin closes this class for the other generic term, Codex `enabled = false` (not probed).

## Evidence (commands, exit codes; scratch `/fast/scratch/hyaku/kotoba-r51/falsify/ReviewReviewedList/`, clone `lane` at 59903b26)

- Pages fetched with plain curl, 2026-10-22T15:16:00-01Z, all HTTP 200, hashes as recorded:
  - `cli-command-reference.md` 461,944 B, `c61997efd7c9…`
  - Claude Code `skills.md` 111,557 B, `cdfcb0df9307…`
  - Gemini `skills.md` 5,763 B, `8e1b4cbe2cd3…`
  - opencode `skills.md` 5,365 B, `f10ced73971c…`
  - opencode `permissions.md` 7,436 B, `de5ba0670ecc…`
  - opencode `agents.md` 21,080 B, sha256 `f2523dcb03ddd36528653a30512fe6690488cd9583f465c866c1642b0770f8ff` (15:16:49Z)
- `python3 -B lane/verifiers/check_overlap_levers.py --root lane` → `overlap levers backed 7 of 7 clients`, exit 0.
- `python3 -B counter-7c81a787.py --root lane` (the 7c81a787 script from `git show`) → `UNBACKED: key term not a reviewed overlap lever` for Copilot CLI, Claude Code and Gemini CLI; `overlap levers backed 4 of 7 clients`, exit 1.
- Copilot CLI world (`w_cli`):
  - `--root w_cli`, pre-extension list → `BACKED GitHub Copilot CLI`, 5 of 7, exit 1.
  - HEAD list `--fetch` (15:18:08Z) → 7 of 7, `quotes found on live pages 7 of 7`, exit 0.
- Claude Code world (`w_cc`):
  - `--root w_cc`, pre-extension list → `BACKED Claude Code`, 5 of 7, exit 1.
  - HEAD list `--fetch` (15:18:10Z) → 7 of 7, exit 0.
- opencode false world (`w_oc`):
  - `--root w_oc`, HEAD list `--fetch` (15:18:11Z) → `BACKED opencode`, `FETCH opencode: quote found (https://opencode.ai/docs/agents)`, 7 of 7, exit 0.
  - Pre-extension list: 4 of 7, exit 1. opencode is backed under both lists.
- Combined world (`w_both`):
  - Pre-extension list → `overlap levers backed 6 of 7 clients`, exit 1; the only failure is Gemini CLI.
  - Pre-extension list `--fetch` → `quotes found on live pages 6 of 6`, exit 1.
- Page lines read with `sed -n`: `cli.md:1267,1278,1300,1304-1330`, `cc.md:393,577,886,1195`, `gem.md:75,94`. `grep -n '\`deny\`' oc*.md` → `oc-agents.md:638`, `oc.md:153`, `oc.md:230`.
- Commit times (`git log -1 --format=%cI`): 7c81a787 12:07:31-03:00, 34cfffbb 12:11:45-03:00. Seat report modification times: `SrcGemini.md` 11:50:35, `SrcCopilotCli.md` 11:57:59, `LeverGuard.md` 11:27:39.

No tools installed. Nothing written in the lane except this report.
