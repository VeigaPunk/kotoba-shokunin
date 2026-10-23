Result: DONE — recorded copy-ready, conditional Round 56 Frontier/Core notes without changing the lane documents.

## Findings and evidence

- C1 is a documentation/learning claim about agent-definition file locations and what files set, backed by a new knowledge entry and `SKILL.md` table; it is not a measured client-loading claim. The frozen command is `python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch`; its pass predicate requires the exact output `agent-definition locations found on the live page F of K; new ground G` with `F >= 5` and `G >= 2`. The counter's scope limits are stated in the plan: actual loading, completeness/correctness of “What the file sets,” and clients outside the seven are not measured (`plans/round-56.md:19-45`).
- C2 is explicitly withdrawn before data, a gate reject rather than a miss. The v1 counter was met by two controls without implementing a box, remains the broken v1, and no agent-definition delegate or map disposition is to change this round (`plans/round-56.md:47-62,108-123`). Its frozen invocation is `python3 -B verifiers/check_agentdef_boxes.py --rev <rev>` (`plans/round-56.md:50-58`); do not describe its control result as checklist execution evidence.
- At plan base, all nine agent-definition boxes were `unexecuted`; generators exist for `.01`, `.02`, `.05`, `.06`, `.07` only, so `.03`, `.04`, `.08`, `.09` are the other four the C2 counter cannot count (`plans/round-56.md:12-15,53-59`). With C2 withdrawn and no map change, this round claims no agent-definition box execution.
- The README Frontier table currently says the agent-definition and always-on checklists have no executed or delegated box; its Round 53 note likewise says no agent-definition box is executed (`corpus/README.md:94-96,114-121`). The Province Core/Frontier layout is at `PROVINCE.md:8-28`; add the conditional Core entry and append a Round 56 note within Frontier without rewriting earlier history.

## Copy-ready append-only text (proposed; not applied)

### `corpus/README.md` § Frontier

Add a row to the Frontier table:

```markdown
| Agent-definition files by client | If C1 lands as measured, the sourced result holds only to the counter's threshold (at least 5 of 7 clients and 2 distinct new paths); it does not establish that clients load files as documented. The agent-definition checklist remains opencode-only, and non-opencode agent files are not checklist-tested. | Re-measure the sourced table with `python3 -B ../verifiers/check_agent_definitions.py --rev <rev> --fetch`; separately measure loading behavior and checklist coverage |
```

Append after the existing Round 55 note:

```markdown
**Round 56 (append-only note on the agent-definition half of checklist coverage and agent-definition files):** *Executed checklist coverage* — C2 is not a Round 56 claim: it was withdrawn before data, and no agent-definition delegate or map disposition changed. Thus no agent-definition box is claimed executed or delegated. The frozen-v1 command is `python3 -B ../verifiers/check_agentdef_boxes.py --rev <rev>`, but its predicate was met by controls that did not implement boxes; do not treat a pass as execution evidence. The other four boxes without case generators are `agentdef.03`, `.04`, `.08` and `.09`. *Agent-definition files by client* — if C1 lands as measured, the new sourced entry and `SKILL.md` decision table support only the live-document result that passes `python3 -B ../verifiers/check_agent_definitions.py --rev <rev> --fetch` (exit 0 only with `agent-definition locations found on the live page F of K; new ground G`, `F >= 5`, `G >= 2`). This is not a claim about measured client behavior or complete/correct “What the file sets” cells. Still not held: whether clients load the files as documented, the other four agent-definition boxes, and applying the checklist to non-opencode agent files.
```

The `../verifiers/` forms above follow the README's existing command convention from `corpus/`; the plan's frozen commands are root-relative as quoted in Findings.

### `PROVINCE.md`

Add under `## Core`, conditionally:

```markdown
- Agent-definition files by client (Round 56, if C1 lands as measured): the source-backed documentation of where the seven clients' agent-definition files live and what a file sets, in `corpus/knowledge/agent-definition-files-round56.md` and `SKILL.md` § Agent-definition files by client; checked by `verifiers/check_agent_definitions.py` (`python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch`, exit 0 at `F >= 5`, `G >= 2`). This is documentation evidence, not measured client loading behavior.
```

Append a Round 56 note inside `## Frontier` (preserving existing bullets):

```markdown
**Round 56 (append-only):** *Executed checklist coverage* — the agent-definition half does not move: C2 was withdrawn before data, no delegate or map disposition changed, and no box is claimed executed. Its frozen-v1 invocation is `python3 -B verifiers/check_agentdef_boxes.py --rev <rev>`; its control-bypassed predicate is not execution evidence. The four boxes without generators remain `agentdef.03`, `.04`, `.08` and `.09`. *Agent-definition files by client* — if C1 lands as measured, only the documented locations/purpose meeting the frozen sourced-page predicate move to Core; `python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch` must print `agent-definition locations found on the live page F of K; new ground G` with `F >= 5`, `G >= 2`. Still Frontier/not held: measured client behavior (whether the files are loaded as documented), checklist coverage of non-opencode agent files, and the four boxes without generators.
```

## Surfaces and bounds

Only this report file was written: `.ufo/waves/round-56/build/ScribeFrontier.md`. `corpus/README.md` and `PROVINCE.md` were read only; the lane-seat bound permits writing only this seat's report. No counter, test, verifier, or other command was run, so no Round 56 predicate result is asserted. No tools were installed or updated. The proposed wording is conditional and does not promote C2 to a claim.
