# ExecNoHarmBaseline

role: executor — establish the C2 check-5 no-harm BEFORE state
item: ExecNoHarmBaseline

Axes: operability and calibration/evidence fidelity.

## Findings

1. Evidence command: `git show 35d44b4b:.ufo/waves/round-62/noharm-tip.txt`

   PASS/FAIL arm lines and requested diagnostics (verbatim):
   ```text
   FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1
           tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0
   PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
   FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md 
   PASS  sources     exit 0 in both columns (base=0 tip=0)
   PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
   PASS  check-ptr   unresolved citation pointers did not grow (base=2 tip=2)
   PASS  boxproof    exit 0 in both columns (base=0 tip=0)
   ```

   The receipt prints 7 arms: 5 PASS and 2 FAIL. Both interim reds are present: `reg_gate` reports 36 of 38 conformant lane verifiers (phantom 0), and `corpus-idx` reports the unindexed round-61 verifier spot-check lesson.

2. Evidence command: `python3 -B verifiers/check_gate_registry.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05` (run from the lane; exit code captured immediately after the command).

   Output:
   ```text
   verifiers/box_proof_case_deletion.py         OK 
   verifiers/check_agent_definitions.py         OK 
   verifiers/check_agentdef_boxes.py            OK 
   verifiers/check_alwayson_boxes.py            OK 
   verifiers/check_assertion_floors.py           OK 
   verifiers/check_callee_rename.py              OK 
   verifiers/check_command_files.py              OK 
   verifiers/check_correction_sweep.py           OK 
   verifiers/check_could_not_evaluate.py         OK 
   verifiers/check_description_thresholds.py     OK 
   verifiers/check_erratum_absorption.py         OK 
   verifiers/check_explicit_invocation.py        OK 
   verifiers/check_gate_finding_delta.py         OK 
   verifiers/check_gate_registry.py              OK 
   verifiers/check_hook_files.py                 OK 
   verifiers/check_infoless_fences.py             OK 
   verifiers/check_mcp_instructions.py            OK 
   verifiers/check_opencode_repin.py              OK 
   verifiers/check_overlap_levers.py              OK 
   verifiers/check_plugin_manifests.py            OK 
   verifiers/check_routed_repairs.py              OK 
   verifiers/check_routed_repairs_v2.py           OK 
   verifiers/check_scoped_rules.py                OK 
   verifiers/check_scoped_rules_v31.py            OK 
   verifiers/check_seat_counts.py                 OK 
   verifiers/check_sibling_census.py              OK 
   verifiers/check_sources_append_only.py          OK 
   verifiers/check_substrate_pins.py               OK 
   verifiers/check_sweep_mutants.py                OK 
   verifiers/compare_harness_independent.py       OK 
   verifiers/fault_injection_corpus.sh             OK 
   verifiers/verify_alwayson.py                    OK 
   verifiers/verify_corpus_independent.py          OK 
   verifiers/verify_corpus_integrity.py            OK 
   verifiers/verify_dispatch_prompts.py            OK 
   verifiers/verify_harness_claims.py              OK 
   verifiers/verify_harness_independent.py         OK 
   verifiers/verify_skill_checklist.py             OK 
   verifiers/verify_surfaces.py                    OK 
   gate registry rows conformant 39 of 39 lane verifiers; phantom 0
   ```

   Exit code: `0`.
   Observation: this invocation reports 39 of 39, while the frozen receipt's interim `reg_gate` reports 36 of 38 at its measured tip. These are the observed outputs for the two stated evidence sources; I do not infer a cause.

## Artifacts

Correction text suitable for the round-63 correction:

```text
The r62 no-harm receipt printed 7 arms: 5 PASS and 2 FAIL. The interim reg_gate failure reported 36 of 38 lane verifiers conformant (phantom 0); corpus-idx failed because corpus/lessons/round-61-verifier-spotcheck.md was unindexed.
```

## Verdict

INFORMS — the frozen receipt confirms both omitted interim reds and the requested lane command exited 0. I would change this finding only if re-reading the specified base revision yields different receipt tokens or output.
