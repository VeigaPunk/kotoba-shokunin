Result: DONE — no-harm holds for every assigned prior-round counter and the census: all five counters exit 0 with byte-identical output at base `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a` and tip `07c33d73ddce769d9cea2846a6313164401b5478`; `sources-census.sh validate` exits 0 with lane kotoba `ok` (7 W04 warnings, all pre-existing duplicate-URL-across-scope rows).

All commands run in `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (cwd) except the census; every run wrapped in `timeout` (600 s counters, 300 s census), all finished in < 2 s wall. UTC window 2026-10-23 ~06:45-06:51 (recorded `date -u` at 06:51:05 UTC; lane HEAD then 07c33d7). No tool installs/updates were needed.

## Matrix base vs tip

| Counter (as assigned) | Base 47c0555 exit | Tip 07c33d7 exit | Same? |
|---|---|---|---|
| `check_agent_definitions.py --rev <rev> --fetch` (round 56; SKILL.md:109 changed this round) | `agent-definition locations found on the live page 7 of 7; new ground 3`, 0 | identical output, 0 | byte-identical (well 7/7, G=3) |
| `check_explicit_invocation.py --rev <rev> --fetch` (round 55) | `user-typed invocation forms found on the live page 5 of 5; new ground 4`, 0 | identical, 0 | byte-identical |
| `check_description_thresholds.py --rev <rev>` (round 54) | `description thresholds backed 7 of 7 clients`, 0 | identical, 0 | byte-identical |
| `check_mcp_instructions.py --rev <rev>` (round 52) | `mcp instructions backed 7 of 7 clients`, 0 | identical, 0 | byte-identical |
| `check_alwayson_boxes.py --rev <rev>` (round 53) | `always-on boxes executed and discriminating 2 of 8` (alwayson.04 and .07, 6 of 6 cases pinned each), 0 | identical, 0 | byte-identical |
| `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | n/a (disk-based; lane working tree at tip 07c33d7) | `kotoba ok .../corpus/SOURCES.md`, 0; W04 x7 | clean |

## Evidence (command + exit code + output)

Round-56 counter, base:
```
$ timeout 600 python3 -B verifiers/check_agent_definitions.py --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a --fetch; echo "EXIT=$?"
agent-definition locations found on the live page 7 of 7; new ground 3
Claude Code  BACKED token=.claude/agents/ norm=.claude/agents found=yes base_count=3
Codex        BACKED token=.codex/agents/ norm=.codex/agents found=yes base_count=5
VS Code      BACKED token=.github/agents norm=.github/agents found=yes base_count=0
Copilot CLI  BACKED token=.github/agents/ norm=.github/agents found=yes base_count=0
Gemini CLI   BACKED token=.gemini/agents/*.md norm=.gemini/agents found=yes base_count=0
Cursor       BACKED token=.cursor/agents/ norm=.cursor/agents found=yes base_count=0
opencode     BACKED token=.opencode/agents norm=.opencode/agents found=yes base_count=10
EXIT=0
```
Tip: identical output, EXIT=0.

Round-55 counter, base and tip (identical):
```
$ timeout 600 python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch; echo "EXIT=$?"
Claude Code  BACKED token=/skill-name new=False found=True
Codex        BACKED token=$setup-demo-app new=True found=True
VS Code      no quote does not contain the word skill
Copilot CLI  BACKED token=/frontend-design new=True found=True
Gemini CLI   no SKILL.md form cell has no backticked invocation token
Cursor       BACKED token=/skill-name new=True found=True
opencode     BACKED token=@skill-id new=True found=True
user-typed invocation forms found on the live page 5 of 5; new ground 4
EXIT=0
```

Round-54 counter, base and tip (identical):
```
$ timeout 600 python3 -B verifiers/check_description_thresholds.py --rev <rev>; echo "EXIT=$?"
description thresholds backed 7 of 7 clients
EXIT=0
```

Round-52 counter, base and tip (identical):
```
$ timeout 600 python3 -B verifiers/check_mcp_instructions.py --rev <rev>; echo "EXIT=$?"
mcp instructions backed 7 of 7 clients
EXIT=0
```

Always-on boxes, base and tip (identical):
```
$ timeout 600 python3 -B verifiers/check_alwayson_boxes.py --rev <rev>; echo "EXIT=$?"
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
EXIT=0
```

Census (tip disk state):
```
$ timeout 300 /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba; echo "EXIT=$?"
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
EXIT=0
```

## Difference explanation

No observable difference exists between base and tip for any assigned counter; each output is byte-identical and exit codes are 0 at both revs. Why the tip changes do not move them:

- **Round-56 counter (check_agent_definitions) vs SKILL.md:109 / opencode row edit:** the changed row (`git diff 47c0555..07c33d7 -- SKILL.md` hunk at old line 106-112) rewrote opencode's cell text ("singular `agent/` still loads per a 2026-01-17 docs commit" -> "V2 still discovers `agent/`, `agents/`, `mode/` and `modes/` per its pinned migration page ...") but retained the token `.opencode/agents` and the knowledge-file row, so the opencode backing (token + found=yes) is unchanged. New-ground counting is fixed against the counter's own frozen BASE (`BASE = "b0b7140b5a7cf8a50f13989ee6285fc8ee245c41"`, check_agent_definitions.py:120), not against this round's base, so the round-57 corpus additions cannot change G retroactively; G stays 3.
- **SKILL.md "Decision tables" section removal (hunk @@ -200,21 +214,7 @@):** that section's content (bailian-cli/bailian-protocol evidence) is not used as a token/quote source by any of the five counters; each counter backs clients from its own ENTRY knowledge file + SKILL.md + SOURCES rows, and the backed output is identical, confirming no token loss.
- **Round-54/52/53 counters:** their ENTRY files (`corpus/knowledge/skill-listing-thresholds-round54.md`, `mcp-server-instructions-round52.md`) and `verifiers/checklist-baseline.json` are unchanged between the revs; outputs identical.
- **Counter code parity:** none of the five assigned verifier scripts changed between base and tip (base..tip diffstat touches only `verifiers/check_correction_sweep.py` +19, which is outside this assignment), so base runs used the same counter code as tip runs.
- **Census:** `validate` returns 0 with lane `ok`; the 7 W04 rows are duplicate-URL-across-scope warnings, which by the script's contract never change a clean lane's status (sources-census.sh header: "W04 same URL across scopes (warnings do not affect clean lanes)").

## Findings

1. [INFO] No-harm confirmed: all prior-round claim counters exit 0 and print the same measured values at tip as at base. Round-56 (7/7, G=3), round-55 (5/5, G=4), round-54 (7/7), round-52 (7/7), round-53 (2/8 discriminating) — all exit 0 at both revs.
2. [INFO] Census validate clean (exit 0, kotoba ok) at tip; W04 x7 are pre-existing warnings, not regressions.
3. [INFO] The `--fetch` runs are live-page dependent; base and tip runs were ~1 minute apart and hit identical URLs with identical results. A later re-run can vary only if the live pages change (out of lane control; same risk as when each round measured).
4. [OUT-OF-SCOPE OBSERVATION] `verifiers/check_correction_sweep.py` changed +19 lines between base and tip at that counter is not part of this assignment's counter list; the L1 may want a return seat to re-run it as its own check.

## Residual risk / verification gaps

- `check_alwayson_boxes` reports 2 of 8 boxes "executed and discriminating" at both revs. This matches its pinned baseline (checklist-baseline.json at each rev), but the low 2/8 ratio is the counter's own contract; I did not investigate why only 2 boxes are discriminating (that is round-53's claim, not mine).
- Fetch-based "found=yes" results were not separately re-verified byte-by-byte against the live pages (the counter does its own normalisation and the read bytes are not emitted); identical base vs tip output is the no-harm evidence.
- I did not run `--self-test` on any counter (not part of the assignment; would have been extra runtime).

Report path: .ufo/waves/round-57/a3/falsify/A3NoHarmPriorClaims.md
