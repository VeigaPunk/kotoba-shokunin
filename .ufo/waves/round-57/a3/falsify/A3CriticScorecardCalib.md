Result: MIXED — the declared C1 miss reproduces, but five calibration mismatches remain in the scorecard and SHONEN evidence labels.

# Scope and counting convention

Reviewed committed revision `07c33d73ddce769d9cea2846a6313164401b5478`, not the lane's changing working tree. Execution was confined to `/fast/scratch/hyaku/kotoba-r57a3/A3CriticScorecardCalib`, cloned from the lane and checked out at that revision. No lane file or counter was edited; no candidate patch was applied. No forbidden earlier-attempt scratch artifact was used.

Axis under review: **calibration**. Other axes below identify consequences, not admission verdicts. I did not invoke a judge, another agent/runtime, or any client model call.

**Mismatch count: 5 distinct assertions**, numbered M01–M05. M02 and M03 are separate stale facts in one SHONEN annotation; M05 groups the R5 closure/provenance problem rather than counting its two scorecard occurrences twice. Historical, expressly dated measurements are not compared indiscriminately with today's numbers. In particular, the B2 report itself is a valid historical snapshot; the problem in M02/M03 is its undated inventory being presented in the standing SHONEN assessment.

Count command, run after writing this report:

```sh
timeout 10s python3 -B -c 'import pathlib,re; p=pathlib.Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/a3/falsify/A3CriticScorecardCalib.md"); print(sum(bool(re.match(r"^## M[0-9]{2} —",s)) for s in p.read_text().splitlines()))'
```

Observed output: `5`, exit 0. This counts the independently reviewed assertions below; it is not a replacement claim counter or canonical grade.

## M01 — the band-10 witness attribution contradicts the recorded dispatch provenance

- **Location:** `SCORECARD.md:29`; its rubric is `SCORECARD.md:19-22`.
- **Counterexample:** the consistency row explicitly bases repeated *non-author* verification on round 11's `ColdRunRecord` and round 12's `ExecIndependentVerifier`. Both were dispatched by kotoba. The standing `SHONEN.md:8` already correctly describes the former as lane-dispatched. Independent implementations are not independent lane provenance.
- **Evidence:** `corpus/knowledge/independent-verification-round12.md:17` calls the latter an L2 lane. The original dispatch lists resolve at `../.ufo/reports/round-11/kotoba.md:168` and `../.ufo/reports/round-12/kotoba.md:191-193`. The current canonical PROTOCOL promotion/non-author rule says a lane-dispatched subagent is still the lane. `SCORECARD.md:33` itself acknowledges that review lanes remain lane-authored under protocol.
- **Command:** the composite fact-certificate command below, exit 0, printed both actual dispatch-list lines and the L2 author row. The two current corpus instruments were also rerun: both exit 1 and agree on the same substantive defects; that agreement does not supply external provenance.
- **Impacted axes:** calibration/owned consistency; not a refutation of the technical value of a second instrument.
- **Smallest safe correction:** withdraw the *non-author* justification and present 10 as a historical attribution pending the canonical judge's score-band decision. Do not manufacture a new external witness or silently assign a replacement grade.

Exact text corrections inside `SCORECARD.md:29`:

1. `**Band 10 = repeated non-author verification in the opposite direction:**` → `**Historical band-10 attribution (not established by these lane-dispatched witnesses under the current non-author rule):**`
2. `(non-author checking the author's numbers)` → `(lane-dispatched checking of the author's numbers)`
3. `(non-author deriving the verdicts, the author's instrument required to agree)` → `(lane-dispatched independent derivation, the author's instrument required to agree)`

The current numeric band cannot be justified by relabeling these same witnesses; that evidentiary decision belongs to the canonical judge.

## M02 — SHONEN still places the old five-row decision-shape table in SKILL.md

- **Location:** `SHONEN.md:6`, the `5 decision rows` portion of `SKILL.md inventory`.
- **Counterexample:** the five-row `Situation | Table? | Evidence` table was moved out in this round. `SKILL.md:217` is now its pointer; the actual five rows are `corpus/knowledge/anatomy-and-compression.md:102-108`. Other current decision tables exist, so this is a stale inventory/location claim, not loss of all decision surfaces or failure of box 1's broad substance.
- **Evidence:** `corpus/knowledge/anatomy-and-compression.md:93-100` dates and identifies the move. The fact certificate printed `five-row Situation table in SKILL.md = False` and `moved Situation data rows = 5`, exit 0.
- **Impacted axes:** calibration; the move itself is not shown harmful to depth.
- **Exact old → new:** `5 decision rows` → `5 decision-shape rows now in corpus/knowledge/anatomy-and-compression.md:102–108 (round-57 move; SKILL.md:217)`.

## M03 — SHONEN's current Sources-entry count is 38 instead of 33

- **Location:** `SHONEN.md:6`, `38 Sources entries`.
- **Counterexample:** counting top-level source bullets in the current `SKILL.md` Sources section gives **33**, not 38. The anatomy count is still 7, and the 41 checklist boxes still split 15/9/9/8; those are not mismatches.
- **Command:** the fact certificate below, exit 0, printed `SHONEN.md:6 current Sources entries = 33`. Section boundaries are `SKILL.md:479-598`.
- **Impacted axes:** calibration only; the source count is not a source-quality grade.
- **Exact old → new:** `38 Sources entries` → `33 Sources entries at 07c33d73`.

Together with M02, label B2 explicitly as the *round-46 historical inventory* rather than suggesting that B2 independently measured the current file. Do not rewrite B2's historical counts.

## M04 — SHONEN attributes the current Adjacent section to the superseded round-46 scan

- **Location:** `SHONEN.md:12`.
- **Counterexample:** the pointer resolves, but the section itself states it was **rewritten in round 49** from the sibling census; the round-46 scan is explicitly the list it *replaced*. See `PROVINCE.md:33-38`.
- **Commands:** the fact certificate printed `PROVINCE.md:33 = Sibling-owned ground (report, don't absorb). Rewritten round 49 from the fleet census`, exit 0. The current sibling guard also exits 0 with `rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 9 of 9 non-none lanes`, and `skill description length 1019 of 1024`.
- **Impacted axes:** calibration and adjacency evidence provenance; not proof of cross-domain bleed.
- **Exact old → new:** `(round 46, sibling-overlap scan `.ufo/round-46/scouts/w2-connector.md`)` → `(round-49 census `corpus/knowledge/sibling-overlap-census-round49.md`; current guard verifies 20 census rows and 20 matching province rows)`.

## M05 — R5's completion shorthand and survivor count do not identify the counter actually audited

- **Locations:** `SCORECARD.md:148` (`R1–R7 worked`) and `SCORECARD.md:150` (129 of 387 survivors).
- **Counterexample:** the independent 387-mutant receipt is explicitly for **v1 at `ee50d8fa`**, SHA-256 `2ac51d2a…`, not frozen v2 at `01312a77`, SHA-256 `bf11a4ef…`. Its result cannot be stated as a measured survivor count for current v2. The v2 author's narrower table is 72 killed of 73, with one equivalent survivor, not an independent re-run of all 387.
- **Evidence:** `.ufo/waves/round-57/controls/MutC1Counter.md:4-6,14,429`; `.ufo/waves/round-57/w0/ExecCounterC1.md:372-392`. R5's whole-guard condition is `plans/round-57.md:39-40`.
- **Strongest current local counterexample:** the unchanged v2 self-test calls `main()` only with an invalid revision (`check_plugin_manifests.py:1125-1129`), which returns before the real measurement/predicate path. It tests `predicate()` directly (`:1738-1741`), but never exercises the final CLI return at `:1858`. The fact certificate's AST inspection printed exactly `["main(['--rev', 'not-a-hash'])"]`. The actual pristine v2 self-test exits 0, `0 failure(s) over 235 assertions`.
- **Limit:** [INFERENCE from the call graph] changing only the final CLI return to unconditional success is outside those self-test executions. I did not mutate any counter or claim a v2 mutation run. The committed v1 audit's corresponding real mutant is M387; its observed v1 result is not relabeled v2.
- **Impacted axes:** calibration and operability confidence. The declaration's *MISS* remains unchanged; a self-test green is not the missing CLI discriminator.
- **Smallest safe correction:** record R5 as partial and separate v1's independent census from v2's authored sample. Do not change a frozen counter during falsification.

Exact old → new:

1. `R1–R7 worked (lesson § Corrections, Q41–Q44); R8 carried.` → `R1–R7 were worked (lesson § Corrections, Q41–Q44); R5 remains partial, including the unexercised successful main() path. R8 carried.`
2. `the C1 counter self-test gaps (`controls/MutC1Counter.md`: 129 of 387 mutants survive, unconditional CLI success among them);` → `a fresh whole-counter self-test audit of frozen C1 v2 (`controls/MutC1Counter.md` measured 129 of 387 survivors on v1 at ee50d8fa, not v2; the v2 self-test still exercises only an invalid-revision main() path);`.

# Executed fact certificate

Command argv: `timeout 30s python3 -B -c PROGRAM`, with the following exact PROGRAM, from the pinned sandbox root:

```python
from pathlib import Path
import ast,re
s=Path("SKILL.md").read_text().splitlines()
h=s.index("## Sources")
print("SHONEN.md:6 current Sources entries =",sum(x.startswith("- ") for x in s[h+1:]))
a=s.index("## Skill-file anatomy"); b=s.index("## Instruction surfaces — pick the file before the fix")
print("anatomy rows =",sum(bool(re.match(r"^\| [0-6] \|",x)) for x in s[a:b]))
print("five-row Situation table in SKILL.md =", any(x.startswith("| Situation |") for x in s))
p=Path("corpus/knowledge/anatomy-and-compression.md").read_text().splitlines()
a=p.index("| Situation | Table? | Evidence |"); b=next((i for i in range(a+1,len(p)) if i>a+1 and not p[i].startswith("|")),len(p))
print("moved Situation data rows =",len(p[a+2:b]))
print("PROVINCE.md:33 =",Path("PROVINCE.md").read_text().splitlines()[32])
t=ast.parse(Path("verifiers/check_plugin_manifests.py").read_text())
f=next(x for x in t.body if isinstance(x,ast.FunctionDef) and x.name=="self_test")
print("self_test main calls =",[ast.unparse(x) for x in ast.walk(f) if isinstance(x,ast.Call) and isinstance(x.func,ast.Name) and x.func.id=="main"])
print("counter report freeze line =",Path(".ufo/waves/round-57/controls/MutC1Counter.md").read_text().splitlines()[3])
p=Path("corpus/knowledge/independent-verification-round12.md").read_text().splitlines()
print("independent witness provenance =",p[16])
for p,n in [("/home/vgpnk/Projects/shokunin/.ufo/reports/round-11/kotoba.md",168),("/home/vgpnk/Projects/shokunin/.ufo/reports/round-12/kotoba.md",191)]:
    print(p+":"+str(n),Path(p).read_text().splitlines()[n-1])
```

Exit 0; decisive stdout:

```text
SHONEN.md:6 current Sources entries = 33
anatomy rows = 7
five-row Situation table in SKILL.md = False
moved Situation data rows = 5
PROVINCE.md:33 = Sibling-owned ground (report, don't absorb). Rewritten round 49 from the fleet census
self_test main calls = ["main(['--rev', 'not-a-hash'])"]
independent witness provenance = | author | L1 / round-11 lanes | L2 lane `ExecIndependentVerifier` — did not author the other script, **did not read its source**, and was given the class spec only |
/home/vgpnk/Projects/shokunin/.ufo/reports/round-11/kotoba.md:168 Batch 2 (after landing): `ColdRunRecord` (non-author cold run),
/home/vgpnk/Projects/shokunin/.ufo/reports/round-12/kotoba.md:191 Batch 1: `ExecIndependentVerifier`, `ScoutWorlds`, `LabratFaults`, `CriticSpec`,
```

# Axis-cell evidence replay

All commands below ran from the pinned sandbox root with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` removed, `GIT_OPTIONAL_LOCKS=0`, `PYTHONDONTWRITEBYTECODE=1`, and `TMPDIR=/fast/scratch/hyaku/kotoba-r57a3/A3CriticScorecardCalib`. Each invocation had the displayed `timeout`; no contention/load test was run. Let **R** = `07c33d73ddce769d9cea2846a6313164401b5478`, **B** = `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`, and **C** = `ac22ca8791980314a37eb1daa69b846f80a1b9e2`; these variables expand to literal hashes in the executed argv.

| Scorecard cell | Command | Observed output; exit |
|---|---|---|
| depth / round 57 | `timeout 180s python3 -B verifiers/check_plugin_manifests.py --rev B --fetch` | `plugin manifests found on the live page 0 of 0; new ground 0`; 1 |
| depth / round 57 | same command with `--rev C` | `plugin manifests found on the live page 4 of 4; new ground 4`; 1 |
| depth / round 57 | same command with `--rev R` | `plugin manifests found on the live page 4 of 4; new ground 4`; 1 |
| depth / counter identity | `timeout 120s python3 -B verifiers/check_plugin_manifests.py --self-test` | exact frozen SHA `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`; 235 assertions, 0 failures; 0 |
| depth / round 56 | `timeout 60s python3 -B verifiers/check_agent_definitions.py --rev R` | `agent-definition locations backed 7 of 7`; 1, as non-fetch is not its predicate |
| depth / round 54 | `timeout 60s python3 -B verifiers/check_description_thresholds.py --rev R` | `description thresholds backed 7 of 7 clients`; 0 |
| depth / round 54 dated point | same command with `--rev 5a097e12` | same 7 of 7; 0 |
| depth / round 51 later counter | `timeout 60s python3 -B verifiers/check_overlap_levers.py --rev R` | `overlap levers backed 7 of 7 clients`; 0; not substituted for the old frozen-counter 4 of 7 |
| depth / carried live harness | `timeout 90s python3 -B verifiers/verify_harness_claims.py` | `21/28 checks pass`; seven named host-state DRIFTs; 1 |
| consistency | `timeout 60s python3 -B verifiers/check_gate_registry.py --rev R` | `gate registry rows conformant 30 of 30 lane verifiers; phantom 0`; 0 |
| consistency / dated point | same command with `--rev bf65974c` | `24 of 24 ... phantom 0`; 0; the historical 24 is not a mismatch |
| coverage | `timeout 60s python3 -B verifiers/check_mcp_instructions.py --rev R` | `mcp instructions backed 7 of 7 clients`; 0 |
| coverage / declared dated point | same command with `--rev c8407a45` | `mcp instructions backed 5 of 7 clients`; 0; agrees with the declared historical measurement |
| operability | `timeout 120s python3 -B verifiers/check_alwayson_boxes.py --rev R` | `always-on boxes executed and discriminating 2 of 8`; both boxes 6/6 cases; 0 |
| operability / dated point | same command with `--rev 55973a20` | same 2 of 8; 0 |
| operability | `timeout 120s python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | `boxes proven 2`; 0 |
| operability | `timeout 120s python3 -B verifiers/box_proof_case_deletion.py --rev R` | six cases killed; controls killed 2/2; N/A killed 1/1; 0 |
| freshness | `timeout 180s python3 -B verifiers/check_opencode_repin.py --rev R` | surfaces 7/7, opencode PASS, pins 3/3, classes 9/9; self-test 0/175; 0 |
| freshness / dated point | `timeout 120s python3 -B verifiers/check_opencode_repin.py --rev 6dd31164` | same headline; self-test 0/155; 0; matches the recorded 155 |
| freshness | `timeout 180s python3 -B verifiers/check_callee_rename.py --rev R` | `callee-rename robust 4 of 4 fixtures`; 0 |
| freshness / dated point | `timeout 120s python3 -B verifiers/check_callee_rename.py --rev c2107ecf` | same 4 of 4; 0 |
| freshness | `timeout 90s python3 -B verifiers/verify_surfaces.py --json` | all 7 checks PASS; 0 |
| freshness | `timeout 60s python3 -B verifiers/check_substrate_pins.py` | `OK 3/3 pins hold`, mtime delta 0 ns; 0 |
| calibration | `timeout 120s python3 -B verifiers/verify_skill_checklist.py --json` | 8 PASS / 3 FAIL in this off-layout clone; 1 — see exclusions below |
| calibration | `timeout 60s python3 -B verifiers/verify_corpus_integrity.py --json` | 4 PASS / 5 DRIFT; 1 — current corpus observations below |
| calibration / consistency | `timeout 60s python3 -B verifiers/verify_corpus_independent.py --json` | same unindexed and unresolved-commit classes; 1 |
| calibration | `timeout 180s bash verifiers/fault_injection_corpus.sh` | `FAIL-control-dirty`, fault-f FAIL, `verdict: FAILURES PRESENT`; 1 |
| adjacency | `timeout 120s python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` | 20/20 census, 20/20 province, 9/9 named; 1019/1024 characters; 0 |

Additional inexpensive self-tests actually run: `timeout 60s python3 -B verifiers/verify_harness_claims.py --self-test` → 0/10, exit 0; `timeout 60s python3 -B verifiers/verify_corpus_integrity.py --self-test` → 0/152, exit 0; `timeout 60s python3 -B verifiers/verify_corpus_independent.py --self-test` → 99 assertions / 0 failures, exit 0; `timeout 120s python3 -B verifiers/verify_skill_checklist.py --self-test` → 0/1852, exit 0. These do not turn the live corpus reds into greens.

Not rerun: old carrier/mutation drivers, entire historical fault matrices, alternate callee seeds, all historical `--fetch` variants, or the nested aggregate assertion-floor battery. This audit reran each axis cell's principal inexpensive evidence path, with selected historical revision controls; it does not claim an exhaustive replay of every historical subexperiment in the very long cells.

# SHONEN pointer resolution and non-mismatches

The pointer-resolution command was part of `timeout 30s python3 -B -c PROGRAM` (the inventory/pointer probe), exit 0. It printed `exists True` for all five named files:

- Box 1: `.ufo/round-46/scouts/B2.md` exists; its inventory is at lines 42–44. Its old counts are correctly historical there; M02/M03 address the standing SHONEN label.
- Box 2: `corpus/knowledge/cold-run-round11.md` exists; red-before runs are at lines 55–91 and the later green capture at lines 369–384. Its own lines 19–28 explicitly disclose the unreachable worktree hashes. SHONEN calls the reviewer lane-dispatched and keeps `[~]`: calibrated, not a mismatch.
- Box 3: `corpus/lessons/round-8-aggregator-box3-coldrun.md` exists. Its `[~]` and B1/B2 basis are at lines 33–44, with later qualifications. The assessment does not invent a fresh non-author re-run: no mismatch found in this box's mark or pointer.
- Box 4: `PROVINCE.md` exists and has `## Adjacent` at line 31; `.ufo/round-46/scouts/w2-connector.md` also exists. M04 is provenance drift, not a broken path.

All four marks are `[~]`, not anonymous `[x]`. No promotion readiness or complete absence of bleed is inferred merely from their existence.

## Current reds: recorded, not falsely counted as historical scorecard contradictions

The checklist clone's three FAILs are its name-directory mismatch (`A3CriticScorecardCalib` versus `kotoba-shokunin`) and absent parent-fleet relative citations in the off-layout sandbox. Its box map is PASS: **41 boxes, 8 executed / 4 delegated / 29 unexecuted**, both delegates' box proofs green; line budget **598/600**. I do not count the off-layout FAILs as lane regressions, and I do not claim to have rerun the gate on the live lane.

Both corpus instruments agree on **3 unindexed files**: `corpus/knowledge/plugin-manifests-round57.md`, `corpus/lessons/round-56-verifier-spotcheck.md`, `corpus/lessons/round-57.md`. They also both flag one commit token, `corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff`. That token is actually quoted metagrammar in a historical correction (`:146-148`), so it is a lexical false red, not proof of a newly broken Gemini source citation. The primary additionally has equal-count baseline drift: tracked 90 versus 81, report pointers 60 versus 51, commit tokens 33 versus 32. These observations explain the fault harness's dirty control. The old round-47 green records are dated; their age alone is not a fabricated historical result. A present-tense all-green/no-harm claim would need to account for these observations, not merely repeat unchanged scores.

# Live C1 metadata receipts

The frozen counter reproduced the exact declared miss at B, C, and R. Four FOUND rows do not themselves prove that no other honest content could meet the frozen target; this report does not retarget C1 or turn its miss into admission.

For ordinary source-opening provenance, I also reopened the four counted URLs using the following command template, each exit 0, HTTP **200**, no redirect to a different URL, stderr empty:

```sh
timeout 60s curl --silent --show-error --location --max-time 45 --max-filesize 5242880 --write-out '\n__CALIB_FETCH_META__\n%{http_code}\n%{url_effective}\n' URL
```

A preceding `timeout 10s date -u` for **each** invocation printed exactly:

```text
Fri Oct 23 06:53:13 AM UTC 2026
```

Byte counts and SHA-256 below cover the fetched body, excluding curl's appended metadata. Quotes are bare, contiguous token substrings from the indicated fetched-byte lines; no Markdown stripping, whitespace folding, or interior-byte edits were performed. They establish token presence only, not runtime behavior.

| URL | bytes | SHA-256 | verbatim token quote; fetched line |
|---|---:|---|---|
| https://code.claude.com/docs/en/plugins-reference.md | 42124 | `f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e` | `.claude-plugin/plugin.json`; 34 |
| https://developers.openai.com/plugins/build/plugins.md | 38036 | `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1` | `.codex-plugin/plugin.json`; 26 |
| https://geminicli.com/docs/extensions/reference.md | 12022 | `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72` | `gemini-extension.json`; 4 |
| https://cursor.com/docs/plugins.md | 20323 | `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62` | `.cursor-plugin/plugin.json`; 28 |

No tool installs or upgrades. No counter changes, integration, report admission, or shipping performed. The five findings are fixable record/calibration defects; whether an unchanged historical 10 is acceptable, and whether any no-harm trade is admissible, remains for the canonical Rust judge.
