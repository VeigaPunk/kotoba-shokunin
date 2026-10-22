Result: MIXED — C2 prints an honest structural 24 of 24 and meets its four-gate guard, but that is not 24 healthy or fully protocol-conformant gates: the fault-harness self-test remains red and a new box-proof self-test misses a load-bearing mutation.

# Scope and custody

Seat: KotobaR54.W2CriticC2. Axes: consistency, calibration. Reviewed C2 at bf65974c7845a06d7ef621ad998c6378ff735cd5 and the supplied tip 58db81c4465b0e9b07ef2485b87d8970683afac6. Read plans/round-54.md, all three append-only errata, build/CriticC2Sizing.md, build/ReviewCounters.md, the landed rows and verifier code, and PROTOCOL.md Gate standard. This is a critic report, not admission or native judgment.

Execution sandbox: /fast/scratch/hyaku/kotoba-r54/W2CriticC2, cloned from the lane and checked out at the supplied tip. All execution/mutations/git worktrees were inside that clone. Only this report is written in the lane. No installs, external source fetches, paid client calls, or runtime/judge invocation. Some self-tests initially used default system temp directories rather than TMPDIR inside the clone; this violated the scratch-location bound. Subsequent probes set TMPDIR to the clone's scratch directory. No resulting lane mutation was observed or performed. Commands were accidentally repeated while background results were delayed; the completed background results are evidence, not independent fixed-substrate replicas.

# Direct answer

**HOLDS: the exact counter statement and Erratum 2 guard.**

From the sandbox, at 2026-10-22T21:52:14Z:

```
python3 -B verifiers/check_gate_registry.py --rev bf65974c7845a06d7ef621ad998c6378ff735cd5
# exit 0
gate registry rows conformant 24 of 24 lane verifiers; phantom 0
```

The same command for 5a097e12b9409a1f425fbc76334f36f1402eb4cc and 58db81c4465b0e9b07ef2485b87d8970683afac6 printed that same line, exit 0. At b55550b9bf3916e5d11a8b596ac92f0dbce9e681, before the table, it printed `gate registry rows conformant 0 of 23 lane verifiers; phantom 0`, exit 1. `git ls-tree --name-only bf65974 verifiers/` filtered to .py/.sh blobs counted 24. The extra verifier is check_sources_append_only.py; this is the frozen per-revision universe, not a changed universe rule.

Counter SHA256 at tip and from plan commit e33715486a45a4a857b64c30e6b695f7995858b8 is identical:
`86c003952f9b5fda2593ede55607dab06d772328753648e1c37775fdd873e6f0`.
The diff of both round-54 counters from plan to tip was empty. The diff of verifiers/ between bf65974 and tip was also empty. Thus the tip self-test executions below exercise the C2-landed verifier bytes.

All four guarded rows (SKILL.md:455-458,464) say gate, expose their OWN --self-test option, and exit 0. They do not borrow the nested verify_surfaces.py flag anymore. The original honest 19 of 23 obstacle was repaired, not dodged with probe labels. The plan's printed-line statement, with Erratum 2's qualifications, matches what is printed. It does not print a count of passing self-tests.

**Important distinction:** a red self-test does not by itself make the registry's flag spelling false, and the frozen counter has no self-test-green predicate. Do NOT rewrite the observed count as 23 of 24. That would invent a different counter. The honest statement is structural 24/24, self-tests green 23/24, four-gate guard 4/4. Nor does protocol force missing-baseline exit 3 to one particular class: its vocabulary is explicitly lane-owned (PROTOCOL.md:393-397).

# Counterexamples and smallest safe corrections

## F1 — BREAKS: reading 24 of 24 as all gates healthy / fully self-tested

**Counterexample:** `fault_injection_corpus.sh --self-test` returns 1 while its registry row counts as conformant.

Commands in sandbox:

```
bash verifiers/fault_injection_corpus.sh --self-test
# exit 1
self-test T1 must-fire assertion fires on planted (a): PASS
self-test T2: FAIL (exit=1)
self-test T4 plant guard rejects unmutated world (marker absent): PASS
self-test T3: FAIL
self-test: BROKEN
```

Reproduced in sandbox detached worktrees at 422ffd1 and bf65974, with TMPDIR inside the sandbox: both exit 1, `self-test: BROKEN`. This is inherited at the base, not introduced by C2 or C1. At bf65974, the no-baseline integrity run reports `corpus.index.unindexed` for corpus/lessons/round-53-verifier-spotcheck.md; at tip that finding is resolved but the new entry produces commit_unresolvable instead.

Mechanism: fault_injection_corpus.sh:73-84 constructs each world by cloning current committed state. Lines 398-409 demand its unmutated worlds have exit 0 and no drift. Therefore corpus drift makes the self-test red independently of whether the assertion machinery works. The test has temporary clones but not an independently clean committed fixture population.

The wave-1 RegFaultInjectionCorpus.md already disclosed exit 1/BROKEN. Registry row SKILL.md:470 faithfully names an accepted flag but omits its known red status. Erratum 2's additional exit-0 condition names only four other gates, so it does not catch this fifth problem. PROTOCOL.md:398-410 calls for isolated fixtures and independent expected evidence; :425-430 makes redness a routed conformance defect, not an automatic round failure absent a round-specific rule.

**Axes:** calibration (false confidence if structural conformity is promoted to health), consistency (known red evidence needs explicit disposition).

**Smallest safe correction:** retain the frozen counter and 24/24 line; record the fault self-test as red and route it. Do not relabel it probe or hide the flag. A code repair, if authorized separately, should give this self-test a committed clean fixture/control independent of the current corpus, with a deliberately dirty control. No such repair was made here.

## F2 — BREAKS: new box-proof self-test proves all its kill conditions discriminate

box_proof_case_deletion.py:193-208 says a kill requires exit exactly 1, a `boxes proven 0/1` line, AND a named deleted conjunct/case. In a sandbox-only copy I replaced just:

```
return "killed" if (proven and named) else "survived"
```

with:

```
return "killed"
```

leaving the earlier exit-0 and non-1 branches intact. Command `python3 -B verifiers/zz_box_mut.py --self-test` exited 0, printing `self-test: 0 failure(s) over 10 assertions`. The retained mutant is scratch/mut/box_mut.py, SHA256 `9bff7b2ee5721023d2e2a34db3e198f909bef4c8f2067135d4f77f65087cdc2b`. Temporary executable copies under verifiers/ were removed.

The new tests (:347-370) cover actual exit-1 kills and exit-0 survivors, but not exit-1 responses lacking proof text or the named conjunct. A coarser mutant changing the earlier exit-0 survivor branch to killed WAS detected: exit 1, `self-test: 4 failure(s) over 10 assertions`. Thus this is a specific coverage hole, not an always-green self-test. As a positive control, changing opencode_repin's retained-class count to len(base) was caught by its self-test: exit 1, `1 failure(s) over 2 assertions`.

**Axes:** calibration, with a bounded consistency risk if the self-test is described as proving every kill requirement.

**Smallest safe correction:** add isolated exit-1/no-proof-line and exit-1/no-matching-name must-not-kill arms with stable expected results. Keep the round-54 counter frozen. This is not failure of Erratum 2's narrow run-exits-0 guard; it limits how much capability can be inferred from that guard.

## F3 — BREAKS: ancillary descriptions are uniformly accurate

- SKILL.md:449 points to verifiers/README.md for “what each one checks.” Eighteen of the 24 verifier basenames have no occurrence there. It is the verbatim historical bullet move, not a complete contemporary description index.
- verifiers/README.md:48-50 says the fault self-test runs “without cloning the repo.” The actual self_test calls new_world three times (:393,398,407), and new_world invokes git clone (:76-79). The new registry's temp-clone scope is more accurate than this duplicate authority.
- SKILL.md:470 says fault temp clones are removed, but the parser accepts --keep-worlds and intentionally retains them. The wave-1 row draft included the exception; the landed row dropped it.
- SKILL.md:139 says checklist exit 3 includes a map “bound elsewhere.” A parsed map bound to another target is instead a check failure returning 1; required MapError load/parse/schema failures return 3 (:2550-2558), as RegVerifySkillChecklist.md:21 also found.

**Axes:** consistency and calibration. These are fixable textual defects, not evidence for replacing the counter or automatically rejecting C2.

**Smallest safe correction:** narrow the README pointer to historical descriptions, correct the cloning statement, restore the keep-worlds exception, and remove “bound elsewhere” from the exit-3 prose. Preserve one verdict-map authority in the registry.

# All-row attack ledger

Rows: SKILL.md:455-478 at tip (the C2 table content is unchanged from bf65974). All 24 accept their own declared --self-test spelling; no borrowed-flag or probe-label dodge found. All declared pinned paths exist. Pin references were traced beyond literal matching: finding_delta delegates to each revision's integrity script/baseline; in-file rows contain expected constants even where they also consume JSON as input. No listed path was demonstrated to be unrelated to the gate. Each gate has a real nonzero failure path; verify_harness_independent's entry includes --freeze, avoiding its derive-only mode.

Below, normal-mode exit is the first completed full entry-command batch at supplied tip. For each Python row run `python3 -B verifiers/<name>` with the arguments shown; fault was invoked directly as its executable path. Self-tests used `python3 -B verifiers/<name> --self-test`, or bash for fault. Detailed logs: sandbox scratch/st/<name>.out and scratch/entry/*.out. Mutable-host repeats are not frozen evidence.

| Verifier | Normal-mode arguments / observed exit | Self-test exit / tally | Attack result |
|---|---|---|---|
| box_proof_case_deletion.py | --rev 58db81c… / 0; killed 6 of 6 | 0 / 10 | HOLDS row and guard; F2 coverage break |
| check_alwayson_boxes.py | --rev 58db81c… / 0; 2 of 8 | 0 / PASS counted and missing-delegate cases | HOLDS |
| check_assertion_floors.py | no args / 0; all listed floors PASS | 0 / 150 | HOLDS |
| check_callee_rename.py | --rev 58db81c… / 0; robust 4 of 4 | 0 / 2 aggregate assertions | HOLDS |
| check_correction_sweep.py | --root . / 0; 0 stale blocks | 0 / 11 | HOLDS |
| check_description_thresholds.py | --rev 58db81c… / 0; backed 7 of 7 | 0 / 22 | HOLDS C2 row; no C1 source admission inferred |
| check_gate_finding_delta.py | --base 422ffd1… --head 58db81c… / 1; new 2, resolved 1 | 0 / 9 | HOLDS map; red finding retained below |
| check_gate_registry.py | --rev 58db81c… / 0; 24 of 24, phantom 0 | 0 / 22 | HOLDS frozen claim, not semantic certification |
| check_mcp_instructions.py | --rev 58db81c… / 0; backed 7 of 7 | 0 / 10 | HOLDS |
| check_opencode_repin.py | --rev 58db81c… / 0; pass 7/7, pins 3/3, kept 9/9 | 0 / 2 | HOLDS own flag and guard |
| check_overlap_levers.py | --rev 58db81c… / 0; backed 7 of 7 | 0 / 51 | HOLDS |
| check_sibling_census.py | corpus/knowledge/sibling-overlap-census-round49.md / 0; rows 20 verified 20 | 0 / 68 | HOLDS |
| check_sources_append_only.py | --base 422ffd1… --rev 58db81c… / 0; 1 touching commit, 0 protected-cell changes | 0 / 14 | HOLDS scoped row, not full-history clearance |
| check_substrate_pins.py | no args / 0; OK 3/3 | 0 / 62 | HOLDS |
| compare_harness_independent.py | no args / 2; false blocker observable drift | 0 / 330 | HOLDS declared could-not-evaluate; repeat later exited 1 on named disagreements |
| fault_injection_corpus.sh | no args / 1; FAILURES PRESENT | 1 / BROKEN | F1; valid flag, red evidence |
| verify_alwayson.py | --check alwayson.04 --target . / 0; PASS | 0 / 89 | HOLDS |
| verify_corpus_independent.py | no args / 1; exit 1 | 0 / 93 | HOLDS declared failure; clone/path dependence not erased |
| verify_corpus_integrity.py | no args / 1; 5/9 checks pass | 0 / 152 | HOLDS declared failure; see no-harm observation |
| verify_dispatch_prompts.py | no args / 1 | 0 / 56 | HOLDS declared failure; sandbox/fleet live input, not C2 regression proof |
| verify_harness_claims.py | no args / 1; 21/28 checks pass | 0 / 10 | HOLDS declared failure; mutable installed substrate |
| verify_harness_independent.py | --freeze scratch/freeze.json / 0; 24 landed rows match | 0 / 123 | HOLDS entry shape, NOT independent frozen-run evidence |
| verify_skill_checklist.py | no args / 1; governance citation resolves FAIL | 0 / 1852 | HOLDS map; inherited clone-relative dead pointer observed |
| verify_surfaces.py | no args / 0; all seven PASS | 0 / 175 | HOLDS; file untouched |

The freeze input above was made immediately beforehand with --write-freeze (exit 0), so matching it does not prove independent expected values or satisfy Two evidences. This was only an entry-command executability/classification check.

Verdict-map attack: all observed exits are declared. compare_harness_independent's exit 3 explicitly means joined inputs but instrument failure (:117-120,1233); its failed class is reasonable. verify_skill_checklist's 3=failed differs from the missing-baseline class chosen in other rows, but PROTOCOL.md:393-397 leaves vocabulary, including missing-baseline treatment, lane-owned. Calling that a mandatory misclassification would overstate the evidence. This is a policy choice to document, not a proven registry lie.

Normal-mode stability attack on the four self-test additions: old blobs from 7ad05d3 and landed blobs of box_proof_case_deletion, check_alwayson_boxes, and check_callee_rename were run against the SAME supplied tip. Each old/new pair exited 0 with byte-identical captured output (diff 0 lines): killed 6/6, always-on 2/8, callee-rename 4/4. check_opencode_repin's old/new normal-mode equivalence was not measured; its self-test and class-count mutant were exercised. No claim of exhaustive behavioral equivalence follows.

# No-harm observation outside C2's table delta

`python3 -B verifiers/check_gate_finding_delta.py --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --head 58db81c4465b0e9b07ef2485b87d8970683afac6` exited 1:

```
gate finding delta 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 -> 58db81c4465b0e9b07ef2485b87d8970683afac6: base drift 3, head drift 4
  new: corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
  resolved: corpus.index.unindexed
finding delta: new 2, resolved 1
```

`verify_corpus_integrity.py --repo . --no-baseline` at tip exits 1 with `commit_unresolvable: corpus/knowledge/skill-listing-thresholds-round54.md:43: 451a02ff`. `git cat-file -t 451a02ff` cannot resolve that object. The entry uses `commit` plus a backticked upstream hash. At bf65974 this finding is absent; it appears with C1's entry. This is not a C2 code regression. Smallest safe correction: write the upstream identity in a form that does not claim it is a lane revision, preserving provenance; route baseline population changes separately rather than silently fitting zero-defect expectations. No lane correction was made.

The new append-only gate's clean base-to-tip run says nothing about old protected-cell edits. Lesson round-54.md:13 and :55-56 explicitly carry twelve earlier changes, and M45 says landing needs their disposition. This report does not turn a range-local clean run into historical clearance.

# Calibration versus bookkeeping

[INFERENCE] The registry's numeric delta alone is largely inventory/schema bookkeeping: before zero meant no table, and the frozen predicate still accepts row-only class/scope assertions plus substring flags. Erratum 2 correctly bounds that and adds a real external guard. Four OWN runnable self-tests, each with a pass/fail exercise and stable expected output, are a genuine bounded calibration/consistency improvement; the opencode retained-class mutation was detected. Calling the entire move pure bookkeeping would ignore that repair.

Conversely, calling 24/24 full gate conformance or saturation would ignore F1, F2 and the duplicate-authority errors. The strongest supportable description is: **complete structural registry, four previously missing self-test modes repaired and green, one inherited self-test still red, semantic and fixture-coverage residuals explicit; score/band judgment remains with the canonical judge.**

No counter widening or probe relabeling is needed. Keep the exact printed statement, attach the exercised caveats, correct the small prose errors, and route the isolated-fixture/coverage defects rather than treating the counter as a substitute for their evidence.
