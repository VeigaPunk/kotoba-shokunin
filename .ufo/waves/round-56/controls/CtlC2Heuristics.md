Result: BREAKS — tuned surface heuristics score 5 of 9 on all three fresh seeds; a smaller combination scores 3 of 9.

## Counterexample and evidence

Best world: sandbox commit `40c2b5eb530fac42f26abc7d391651ef9caf92bd`, under `/fast/scratch/hyaku/kotoba-r56/CtlC2Heuristics`.

Command (three independent invocations):

```text
timeout 240 python3 -B verifiers/check_agentdef_boxes.py --rev 40c2b5eb530fac42f26abc7d391651ef9caf92bd
```

Every invocation printed `agent-definition boxes executed and discriminating 5 of 9`, counted .01/.02/.05/.06/.07, and exited 0. Seeds:

- `521b3a12df3937e5796e82a079e06133`
- `2e8487613976ca016f9f7dec98a435ad`
- `c944b7890ab701ab5f01f11e2b410727`

C2 predicate: exit 0 (N>=3) — MET

The counter was the unchanged frozen file from `0f58a469b0e3c4fcefaa11d2a01648b2e88cb257`:

```text
8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe  verifiers/check_agentdef_boxes.py
```

Full commands, stdout, stderr, exit codes, profiles and hashes for all 24 runs are in `CtlC2Heuristics.txt`; line pointers below are to that receipt. Only nine dispositions and sandbox control files changed; the counter and box text hashes were not changed.

## All worlds

Each row is three fresh frozen-counter CLI runs, not a seed override or a modified counter. N is out of T=9.

| World | Sandbox commit | N by run | Exits | C2 predicate | Receipt line |
|---|---|---|---|---|---|
| naive-multifile | `9d714bea7be987a8c8757a6d449ca96664a464e5` | 0,0,0 | 1,1,1 | NOT MET | 14 |
| naive-any-stem-difference | `f5781a4c9459f9e7707b2550a44f721b917f4f5f` | 0,0,0 | 1,1,1 | NOT MET | 78 |
| naive-stem-membership | `7b3fdd033aa3d3763c4ae036d31da50bd811b352` | 0,0,0 | 1,1,1 | NOT MET | 142 |
| tuned-identity-only | `2df8ab35834c732993baa688e723931c40df7cd7` | 1,1,1 | 1,1,1 | NOT MET | 206 |
| tuned-identity-and-roster | `ef55fd0c19696a5981f9f606ddd13194d2577311` | 2,2,2 | 1,1,1 | NOT MET | 270 |
| tuned-three-boxes | `5a29592899940fcf83d526885a4d8ea2c15dd047` | 3,3,3 | 0,0,0 | MET | 334 |
| tuned-all-five | `6df3156b73a5952e9d8be5ed5d2c58a6ee7bca5d` | 4,4,4 | 0,0,0 | MET | 398 |
| tuned-all-five-refined | `40c2b5eb530fac42f26abc7d391651ef9caf92bd` | 5,5,5 | 0,0,0 | MET | 462 |

The first three worlds combine the requested naive heuristics across all five boxes: .05 any four-digit number/month-name date anywhere; .02 missing config or any stem absent from raw config text; .06 any word `task` or `round`; .07 any repeated line (third world ignores empty lines). The .01 alternatives are respectively more than one file, a name differing from any stem, and a name not belonging to the stem set. All score zero. The counter rejects the body-only date, bare-task, reachability-via-roster and name hard negatives. The literal repeated-line rule also sees frontmatter delimiters.

The tuned ladder deliberately exploits generator shape:

- **.01:** flatten all `name:` lines; if any exist, require their count and set to equal the file count and stem set. No per-file name binding or sibling semantics.
- **.02:** accept if all stems occur anywhere in config text, OR any stem occurs there and any file contains `subagents:`. No JSON agent-map parsing or reachability traversal.
- **.05:** scan exactly the first five lines for four digits or `PROPOSE round`. No frontmatter-boundary parser, month-date handling, or general round-index handling.
- **.06:** search the entire file for `current task`, the word `round`, or `one-shot`. No body boundary or complete one-shot vocabulary. An earlier variant searching bare `current` scored only four boxes because the ordinary body says `roster current`; that miss is retained above.
- **.07:** compare only paragraph-leading lines of length >=40, plus heading lines. No full-paragraph normalization or section-content comparison.

The .01/.02/.05 combination alone scores N=3 and exits 0 on all three seeds at `5a29592899940fcf83d526885a4d8ea2c15dd047`. The refined five-way combination scores N=5, the maximum number of generated boxes, without implementing any of the five readings in full.

## These are shortcuts, not real box implementations

Ten direct probes of the accepted-world delegate contradict its frozen reading. Expected statuses below are derived from the frozen docstring, not another judge or a counter modification. Actual JSON output and exit are recorded verbatim in the receipt.

| Witness | Required status | Observed status / exit | Frozen contract | Receipt line |
|---|---|---|---|---|
| Names swapped across two stems | FAIL | PASS / 0 | `verifiers/check_agentdef_boxes.py:68–77` | 529 |
| Three files: one named, two unnamed | PASS | FAIL / 1 | `verifiers/check_agentdef_boxes.py:71–77` | 557 |
| Unrelated subagent roster leaves gamma orphaned | FAIL | PASS / 0 | `verifiers/check_agentdef_boxes.py:79–91` | 591 |
| Stem occurs only under theme; no agent map | FAIL | PASS / 0 | `verifiers/check_agentdef_boxes.py:80–88` | 624 |
| ISO date at frontmatter line 8 | FAIL | PASS / 0 | `verifiers/check_agentdef_boxes.py:93–105` | 647 |
| Frontmatter updated: November 1 | FAIL | PASS / 0 | `verifiers/check_agentdef_boxes.py:100–105` | 672 |
| Body says Once only | FAIL | PASS / 0 | `verifiers/check_agentdef_boxes.py:112–115` | 693 |
| Trigger in frontmatter only | PASS | FAIL / 1 | `verifiers/check_agentdef_boxes.py:107–115` | 713 |
| Same first line, different complete paragraphs | PASS | FAIL / 1 | `verifiers/check_agentdef_boxes.py:117–130` | 734 |
| Same heading and identical short section content | PASS | FAIL / 1 | `verifiers/check_agentdef_boxes.py:125–129` | 762 |

Generator evidence: `verifiers/check_agentdef_boxes.py:429–477` does not permute declared names across files or include the mixed three-file unnamed case; `:480–544` only exercises direct enrollment and one-hop rosters with no decoy config text; `:547–613` keeps all tested frontmatter defects in the first five lines and omits month-name dates; `:616–673` uses only current-task, numeric round and one-shot forms and no frontmatter-only trigger; `:676–747` uses paragraph leads and section names that the shortcut can distinguish. These are statements about the frozen local generator, not external client behavior.

## Impacted axes

- **Operability:** the claimed executed/discriminating count accepts delegates that do not implement its operational readings.
- **Calibration and consistency:** randomizing stems, words and dates does not randomize the semantic relations the shortcuts skip. N=5 is sample saturation, not five implemented boxes. No axis scores or canonical judgment were assigned here.

This is a fixable measurement defect in the pre-data control gate, not a genuine implementation tradeoff to silently accept. The literal frozen predicate is met by the control. Plan `plans/round-56.md:82–91` already specifies redesign before data or exploratory treatment when a control meets it.

## Smallest safe correction

Do not edit the frozen counter in place or integrate these control delegates. Route a pre-data erratum (or use the plan's exploratory route). To kill this observed N=5 control at the N>=3 threshold, at least three counted boxes must acquire discriminating countercases. A minimal witnessed set is:

1. .01: swapped declared names across matching stem sets (must FAIL).
2. .02: a stem mentioned outside the JSON agent map with no enrollment (must FAIL).
3. .05: a valid ISO date beyond the fifth frontmatter line (must FAIL).

All three are concrete, exercised semantic witnesses above. Adding randomized twin families for them would reject these observed N=3 and N=5 worlds [INFERENCE; no counter edit or corrected-counter run was performed]. The .06 frontmatter-only trigger and .07 same-lead/different-tail witnesses should also become cases if the revised counter continues to claim fidelity to those full readings. Re-run the controls before any data seat; do not treat a threshold increase as evidence of implementation.

## Scope and hygiene

All executable work and commits were in the named sandbox. Only this report and the required plain-text receipt were written in the lane. No counter, lane index, fleet state, external client, source URL, paid model call, other runtime, or tool installation was involved. All started commands returned; no long-lived processes were started. The scratch clone retains the committed worlds and probe fixtures as evidence.
