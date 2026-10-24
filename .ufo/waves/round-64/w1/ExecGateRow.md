# ExecGateRow — round 64 wave 1

## Files changed
- Wrote only this report. No lane production files were changed.

## C2 — proposed gate-registry row

`check_gate_registry.py` builds its universe from tracked `.py`/`.sh` blobs under `verifiers/` at the selected revision, requires exactly one `SKILL.md` registry row per verifier, and flags registry rows for missing verifiers as phantoms. For a gate row, the `entry command` cell must contain the verifier path; the verdict map must include `0=clean` and `1=failed`; the self-test cell must name a backticked flag with an exact handler (for Python, an `argparse.add_argument()` argument); the gate cannot use `self-test: none` or `pinned values: none`. The checker does not validate the rest of the command syntax beyond requiring the path in that cell. A conformant new row therefore needs `--self-test` implemented in the script, not just listed in the table.

Proposed one-line `SKILL.md` row, using the existing r63 row's columns and the frozen r64 C2 contract:

```text
| `verifiers/check_r64_routed_repairs.py` | gate | `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-64 C2 counter: four computed checks over the round-63 spot-check's routed defects (seat edit committed, control revisions named, lowest axis corrected, assertion count named); clean at `4 of 4`, failed at base `078eec4`'s `0 of 4` | `--self-test` | in-file | none (read-only) | kotoba |
```

The row content follows `plans/round-64.md` C2, which freezes `r63 routed defects closed 4 of 4` for the target and `0 of 4` at the pinned base. **Dependency:** `verifiers/check_r64_routed_repairs.py` was absent when read, so this report cannot confirm the future script's actual `--self-test` handler. The requested baseline check is of the 078eec4 tree and does not yet include the new verifier.

## Assertion-floor finding

**[INFERENCE] Yes, the new counter should receive a floor-registry row, provided its self-test emits an assertion count that the floor guard can parse.** Round-62 lesson F17 records that unfloored gate self-tests can lose arms without detection and names an assertion-count line plus registry rows as the smallest fix. `check_r63_routed_repairs.py` is absent from `verifiers/floors-registry.json` (no matching entry), so repeating that omission for r64 would leave its arms outside the floor guard. The guard also cross-checks the external JSON against its in-file `EXPECTED_INSTRUMENTS` and `INSTRUMENTS` tables; the guard docstring and instrument total must be updated consistently with a floor addition.

The required row shape is:

```json
"r64_routed_repairs": {
  "floor": <measured --self-test assertion total>,
  "path": "verifiers/check_r64_routed_repairs.py"
}
```

This is a shape only, not a valid numeric row. The new counter source was absent, and neither its compatible count-summary format nor its assertion total could be measured; supplying a numeric floor would be fabricated. The exact floor value is a dependency on the counter's landed source and measured `--self-test` output.

## Exact requested baseline evidence

Command run:

```text
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_gate_registry.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
```

Output and exit code:

```text
verifiers/box_proof_case_deletion.py         OK
verifiers/check_agent_definitions.py         OK
verifiers/check_agentdef_boxes.py            OK
verifiers/check_alwayson_boxes.py            OK
verifiers/check_assertion_floors.py          OK
verifiers/check_callee_rename.py             OK
verifiers/check_command_files.py             OK
verifiers/check_correction_sweep.py          OK
verifiers/check_could_not_evaluate.py        OK
verifiers/check_description_thresholds.py    OK
verifiers/check_erratum_absorption.py        OK
verifiers/check_explicit_invocation.py       OK
verifiers/check_gate_finding_delta.py        OK
verifiers/check_gate_registry.py             OK
verifiers/check_hook_files.py                OK
verifiers/check_infoless_fences.py            OK
verifiers/check_mcp_instructions.py           OK
verifiers/check_opencode_repin.py             OK
verifiers/check_overlap_levers.py             OK
verifiers/check_plugin_manifests.py           OK
verifiers/check_r63_routed_repairs.py         OK
verifiers/check_routed_repairs.py             OK
verifiers/check_routed_repairs_v2.py          OK
verifiers/check_scoped_rules.py               OK
verifiers/check_scoped_rules_v31.py           OK
verifiers/check_scoped_rules_v32.py           OK
verifiers/check_seat_counts.py                OK
verifiers/check_sibling_census.py             OK
verifiers/check_sources_append_only.py         OK
verifiers/check_substrate_pins.py              OK
verifiers/check_sweep_mutants.py               OK
verifiers/compare_harness_independent.py       OK
verifiers/fault_injection_corpus.sh             OK
verifiers/verify_alwayson.py                   OK
verifiers/verify_corpus_independent.py         OK
verifiers/verify_corpus_integrity.py           OK
verifiers/verify_dispatch_prompts.py            OK
verifiers/verify_harness_claims.py             OK
verifiers/verify_harness_independent.py        OK
verifiers/verify_skill_checklist.py            OK
gate registry rows conformant 41 of 41 lane verifiers; phantom 0
exit code: 0
```

This evidence supports only the baseline registry state: 41/41 existing lane verifiers conformant at the pinned revision, with zero phantom rows. It does not test the absent r64 counter or settle C2's target predicate.