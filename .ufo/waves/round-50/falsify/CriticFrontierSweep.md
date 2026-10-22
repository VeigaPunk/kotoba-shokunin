# CriticFrontierSweep — round 50 falsify: the negative "no documented tie-break between overlapping descriptions"

**Verdict: HOLDS-BOUNDED** for the headline negative. No page among S024, S026 and S029 (plus S022, S025, S027 and S028, re-fetched as a bonus) states how the model chooses between two differently named skills or subagents whose descriptions both match.
**FAILS** for three universality sentences, all disproved by one located counterexample on S026:
- census `sibling-overlap-census-round49.md:210`: "the only arbitration is between same-name subagents";
- census `:225-226`: "Every documented 'which one wins' rule found so far is keyed on the skill *name* … None compares descriptions";
- census `:250` and lesson `corpus/lessons/round-50.md:32-33`, which repeat the same claim.

**Q14 also fails for the sweep as the evidence.** The ten-pattern sweep cannot fail on a selection rule worded in choice vocabulary, and neither can the six suggested synonyms.

Seat: leaf critic, read-only on the lane; this report is the only lane write. Scratch: `/fast/scratch/hyaku/kotoba-r50/falsify/CriticFrontierSweep/fetch/`. No tool was installed or upgraded (curl, grep, sha256sum, sed only).

## Counterexample

S026, Claude Code subagents, `sub-agents.md:77`, in the built-in agents table under the column "When Claude uses it". For the `claude` agent it says:

> "When a task doesn't fit a more specialized agent. A catch-all with every tool available to subagents."

(22 words; the markdown link markup is removed from the quote.)

This is a documented preference between two agents with **different names** that could both take a task: the catch-all is used only when no more specialized agent fits. The rule is keyed on fit or specificity, not on name, origin, location tier or first-found order. So the census bullet for S026 ("the only arbitration is between same-name subagents") is false as written, and so is the cross-page sentence that every documented "which one wins" rule is keyed on name.

Its bounds, which keep the headline negative standing:
- It covers one built-in catch-all against every specialized agent.
- It is not a rule between two descriptions an author writes.
- It does not say how Claude picks between two specialized agents that both fit.

It also agrees with the census's craft conclusion: the more specific description is the one routed to.

Neither sweep detects it. Line 77 against the ten census patterns gives `grep -ciE` 0 (exit 1). Against the six suggested synonyms (`choose between|which skill|most relevant|best match|select|priority`) it also gives 0 (exit 1). Only the wider pattern `more speciali` matches it (1, exit 0).

## Findings

1. **Freshness holds.** All seven re-fetched pages are byte-identical to the sha256 values recorded in `corpus/SOURCES.md`: S024 (both the `.md` and HTML routes), S026, S029, S025, S027, S028 and S022 (fetch table below). The census bytes are therefore current as of 2026-10-22T13:31Z.
2. **The ten-pattern counts replay exactly** on my bytes:
   - S024: `0 0 0 0 0 0 0 0 1 0`
   - S026: `0 1 6 0 0 0 4 0 0 2`
   - S029: `0 0 4 0 0 1 1 1 0 0`

   These match the counts in the seat reports `SrcOpencodeDocs.md`, `SrcClaudeSubagents.md` and `SrcGeminiCliSkills.md`.
3. **The ten-pattern sweep is inadequate as Q14 evidence for this claim.** The claim is about *selection* ("how the model picks"). Eight of the ten patterns are collision or identity vocabulary (`same name`, `precedence`, `conflict`, `multiple skills`). The other two are length vocabulary (`1024`, `truncat`). None is a choice verb or a specificity word, so the sweep cannot fail on a selection rule worded in ordinary English. Q25 asks that a counter be shown able to fail, and line 77 is the demonstration. The six suggested synonyms are also too narrow: they miss line 77 too. A wider 32-pattern sweep (table below) does surface it.
4. **Synonym hits, all located; none is a selection rule.** Every pattern was matched case-insensitively.
   - `choose between`: S026 `:1035` is the heading "Choose between subagents and main conversation", which is advice to the user.
   - `which skill`: S024 `:135` (permissions); S026 `:624` ("controls which skills are preloaded").
   - `most relevant`: 0 on all ten files. `best match`: 0 on all ten files.
   - `select`: S024 `:45` (the autoinvoke opt-out from "auto-selection guidance") and `:129` ("selected manually and loaded by exact name"). S026 has 14 hits, all about model selection, the user interface, or SQL `SELECT` (`:222`, `:358`, `:375`, `:377`, `:624`, `:710`, `:723`, `:959`, `:1249`, `:1250`, `:1425`, `:1429`, `:1441`, `:1455`, `:1472`; one `grep -c` line can hold two hits).
   - `priority`: S026 `:156` and `:158` (same-name location table) and `:1326` (review feedback). On S029 the only `priorit` hit is `:33` (follow the skill's guidance after activation).
5. **Wider-sweep hits that bear on the question but are not tie-breaks.** Each is worth recording next to the negative:
   - S026 `:860`: an @-mention "ensures that specific subagent runs rather than leaving the choice to Claude". The page assigns the choice to the model and states no rule for it, and the only deterministic override is the user's.
   - S024 `:73`: "Keep it specific enough for the agent to choose correctly." This is opencode's version of S026 `:1293`. The census S024 bullet omits it.
   - S029 companion page `skills-best-practices.md:16-17`: "Avoid overlap: Ensure your skill descriptions are distinct from one another…".
   - S025 `:64`: discovery "does not guarantee that it invokes a skill for every relevant prompt".

   All four are craft remedies or disclaimers, not arbitration. Together they make the negative stronger.
6. **Other name-keyed rules; no selection rule elsewhere.** S026 `:168` (among nested `.claude/agents/` directories with the same `name`, "Claude Code uses the definition closest to the working directory") is name-keyed and missing from the census's S026 list, but does not contradict it. On the bonus pages, S022 `:198-200` and `:680-682`, S027 `:233`, and S028 `:415` and `:419` are keyed on name or position.

## Impacted axes

**Adjacency:** the craft consequence holds, but the universality sentences overstate the sources (S026 documents one non-name preference). **Freshness:** holds; the bytes are unchanged. **Q14 / Q25:** the evidence sweep has not been shown able to fail on selection vocabulary. **Q26:** the headline "now on nine pages" claims more than its counter measures.

## Smallest safe correction

- Census `:210`: change "the only arbitration is between same-name subagents" to "apart from the built-in catch-all, which Claude uses 'When a task doesn't fit a more specialized agent' (`sub-agents.md:77`), the only arbitration is between same-name subagents".
- Census `:225-226`, census `:250` and lesson `:32-33`: change "every … rule is keyed on the skill name" to "every rule between two *authored* skills or subagents is keyed on the name; the one specificity rule found (S026 `:77`) involves a built-in catch-all".
- Add the selection vocabulary to the recorded sweep: `choos|chosen|choice`, `decid`, `pick`, `select`, `which (one|skill|agent|subagent)`, `relevan`, `speciali`, `specific enough`, `distinct`, `rout`, `priorit`, `prefer`, `best match`, `most relevant`, `fit`. Record line 77 as its one rule-like hit, so the negative carries a sweep shown able to fail (Q14, Q25).

No row moves, and the D3 precedence ruling stays kotoba's own rule. Line 77 does not decide `contested` versus a stated split.

## Evidence (in the scratch directory `fetch/`)

The page fetches. Every one used `curl -sS -L -o <file> -w '%{http_code} %{size_download} %{content_type}' <url>`, and every curl exited 0.

| file | URL | UTC | HTTP | bytes | sha256 (first 8) | registry |
|---|---|---|---|---|---|---|
| s024.md | https://opencode.ai/docs/skills.md | 13:31:27Z | 200 | 5365 | f10ced73 | = S024 |
| s024.html | https://opencode.ai/docs/skills | 13:31:28Z | 200 | 73201 | 4d96fa56 | = S024 |
| s026.md | https://code.claude.com/docs/en/sub-agents.md | 13:31:28Z | 200 | 110784 | 89aa73eb | = S026 |
| s029.md | https://geminicli.com/docs/cli/skills.md | 13:31:28Z | 200 | 5763 | 8e1b4cbe | = S029 |
| s029-bp.md | https://geminicli.com/docs/cli/skills-best-practices.md | 13:31:29Z | 200 | 3257 | 612c3b83 | (companion) |
| s029-using.md | https://geminicli.com/docs/cli/using-agent-skills.md | 13:31:29Z | 200 | 3052 | 9e61fb7c | (companion) |
| s029-create.md | https://geminicli.com/docs/cli/creating-skills.md | 13:31:29Z | 200 | 6705 | b7061545 | (companion) |
| s025.md | https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 13:31:29Z | 200 | 22871 | de5ba34f | = S025 |
| s027.md | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills.md | 13:31:35Z | 200 | 11790 | 18c361b5 | = S027 |
| s028.md | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 13:31:35Z | 200 | 47200 | d0d362cc | = S028 |
| s022.md | https://code.claude.com/docs/en/skills.md | 13:31:35Z | 200 | 111557 | cdfcb0df | = S022 |

"Registry" means the prefix was found in `rg -o 'sha256 \`[0-9a-f]{8}…\`' corpus/SOURCES.md` (exit 0).

Replay of the ten census patterns, with `for t in overlap ambigu precedence 'tie[- ]?break' conflict 'multiple skills' 'same name' prioriti 1024 truncat; do grep -ciE "$t" $f; done`:
- s024.md: `0 0 0 0 0 0 0 0 1 0`
- s026.md: `0 1 6 0 0 0 4 0 0 2`
- s029.md: `0 0 4 0 0 1 1 1 0 0`

Wider sweep, `grep -ciE <p> <file>`. The columns are, in order: s024, s026, s029, s029-bp, s029-using, s029-create, s025, s027, s028, s022.

| pattern | counts |
|---|---|
| choose between | 0 1 0 0 0 0 0 0 0 0 |
| which skill | 1 1 0 0 0 0 0 0 0 3 |
| most relevant | 0 0 0 0 0 0 0 0 0 0 |
| best match | 0 0 0 0 0 0 0 0 0 0 |
| select | 2 14 0 0 0 0 15 0 1 1 |
| priority | 0 3 0 0 0 0 0 0 2 1 |
| which (one\|agent\|subagent\|skill) | 1 7 0 0 0 0 0 0 0 8 |
| decid | 0 5 0 0 0 1 1 1 1 7 |
| pick | 0 3 0 0 0 0 1 0 0 7 |
| relevan | 0 3 0 0 0 0 7 3 0 6 |
| choose\|chosen\|choice | 1 28 0 0 0 0 2 1 0 3 |

`rank` and `compet` are 0 on every file. `disambig`, `more than one` and `specific enough` hit only S026 (1 each) and, for `specific enough`, S024 (1). The full 32-pattern run is in this seat's transcript; it exited 0.

Specificity probe: `grep -nHiE "more speciali|speciali[sz]ed agent|catch-all|fallback|doesn't fit|does not fit|general capabilit|guarantee"` over the ten files exited 0. Its only rule-like hit is `s026.md:77`; the other hits are `:510` (an example description), `:850` (@-mention), `:978` and `:984` (fallback model), S029-bp `:17`, S025 `:64`, S028 `:148` and `:405`, and S022 `:441` and `:1228`.

Line 77 against each sweep, with `sed -n 77p s026.md | grep -ciE ...`:
- the ten census patterns: `0` (exit 1);
- the six suggested synonyms: `0` (exit 1);
- `more speciali`: `1` (exit 0).

Lane rev read: `git rev-parse HEAD` gives `956ee1676e4c18480bce8ac3993541462be76e11` (exit 0). The location of the repeated wording comes from `rg -n "only arbitration|keyed on|None compares|name-keyed|no tie-break|No page states" corpus/... LOG.md plans/round-50.md` (exit 0): census `:34`, `:199`, `:210`, `:217`, `:219`, `:225-226`, `:250`; lesson `:32-33`, `:45`.
