# Round 64 wave 1 — no-harm baseline

## Result

The round-62 battery interface accepted the requested identity invocation. Base and tip both resolved to `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`. The run ended `no-harm OK`, wrapper-recorded command exit code 0. The gate registry also passed at base: `gate registry rows conformant 41 of 41 lane verifiers; phantom 0` (exit 0).

The battery reports an inherited `plugin` arm as `PASS` because normalized results match, although that arm's underlying command exits 1 in both columns. The optional live `scoped-rules-v31 --rev 43fe0180 --fetch` informational check returned exit 2 because the supplied revision is not a full hash; it is not a gating arm and did not change the battery verdict.

## Invocation and later run

Accepted usage, as read from `.ufo/waves/round-62/noharm-battery.sh`:

```text
bash .ufo/waves/round-62/noharm-battery.sh [--base REV] [--tip REV] [--sandbox DIR] [--keep]
```

No interface correction was needed. Exact identity-run command:

```bash
bash .ufo/waves/round-62/noharm-battery.sh --base 078eec4a1f6a41c64ff8806f58b46a67cd413bfc --tip 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
```

Exact command template for the later integrated-tip run (from the lane root; substitute the measured round-64 tip):

```bash
bash .ufo/waves/round-62/noharm-battery.sh --base 078eec4 --tip <round-64 tip>
```

## Full battery output

```text
noharm: lane        /home/vgpnk/Projects/shokunin/kotoba-shokunin
noharm: base        078eec4a1f6a41c64ff8806f58b46a67cd413bfc
noharm: tip         078eec4a1f6a41c64ff8806f58b46a67cd413bfc
noharm: sandbox     /tmp/kotoba-r62-noharm.GXxQC8
noharm: date -u     2026-10-24T03:35:20Z
noharm: column base ready (078eec4a1f6a41c64ff8806f58b46a67cd413bfc)
noharm: column tip ready (078eec4a1f6a41c64ff8806f58b46a67cd413bfc)
--- arms ---
PASS  reg_gate    exit 0 in both columns (base=0 tip=0)
PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
PASS  corpus-idx  no new unindexed corpus file at tip (base set: corpus/lessons/round-62-verifier-spotcheck.md corpus/lessons/round-63-verifier-spotcheck.md )
PASS  sources     exit 0 in both columns (base=0 tip=0)
PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
PASS  check-ptr   unresolved citation pointers did not grow (base=3 tip=3)
PASS  boxproof    exit 0 in both columns (base=0 tip=0)
PASS  floors      exit 0 in both columns (base=0 tip=0)
PASS  agentdefs   exit 0 and normalized output identical in both columns
PASS  explicit    exit 0 and normalized output identical in both columns
PASS  desc        exit 0 and normalized output identical in both columns
PASS  mcp         exit 0 and normalized output identical in both columns
PASS  plugin      exit 1 and normalized output identical in both columns
PASS  hooks       exit 0 and normalized output identical in both columns
PASS  scoped      exit 0 in both columns (base=0 tip=0)
PASS  absorption  check_erratum_absorption.py self-test exited 0 at tip
PASS  repairs-v2  check_routed_repairs_v2.py self-test exited 0 at tip
PASS  scoped-v31  check_scoped_rules_v31.py self-test exited 0 at tip
PASS  battery-self a mutated verdict line was detected by the comparison (battery is not vacuous)
PASS  battery-self2 an injected new corpus DRIFT kind was detected by the comparison
PASS  battery-self3 an exit-2 (could-not-evaluate) column is caught by the comparison guard
--- informational ---
INFO  routed-repairs (C2 predicate; the L1 measures it) exit=0: routed repairs verified 6 of 6
INFO  scoped-rules self-test at tip: self-test: 0 failure(s) over 189 assertions
INFO  scoped-rules --rev tip  --fetch: exit=0: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
INFO  scoped-rules --rev base --fetch: exit=0: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
INFO  (the inherited C1 control: tip counter code, --rev base -> exit 1; --rev tip -> exit 0)
INFO  scoped-rules-v31 --rev 43fe0180 --fetch (optional/live): exit=2: could-not-evaluate: --rev '43fe0180' is not a full 40-hex commit hash
--- verdict ---
no-harm OK

COMMAND_EXIT_CODE=0
```

## Gate registry output

Command:

```bash
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_gate_registry.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
```

```text
verifiers/box_proof_case_deletion.py         OK 
verifiers/check_agent_definitions.py         OK 
verifiers/check_agentdef_boxes.py            OK 
verifiers/check_alwayson_boxes.py             OK 
verifiers/check_assertion_floors.py           OK 
verifiers/check_callee_rename.py              OK 
verifiers/check_command_files.py              OK 
verifiers/check_correction_sweep.py           OK 
verifiers/check_could_not_evaluate.py         OK 
verifiers/check_description_thresholds.py    OK 
verifiers/check_erratum_absorption.py         OK 
verifiers/check_explicit_invocation.py        OK 
verifiers/check_gate_finding_delta.py         OK 
verifiers/check_gate_registry.py              OK 
verifiers/check_hook_files.py                 OK 
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
verifiers/check_sources_append_only.py        OK 
verifiers/check_substrate_pins.py             OK 
verifiers/check_sweep_mutants.py              OK 
verifiers/compare_harness_independent.py      OK 
verifiers/fault_injection_corpus.sh            OK 
verifiers/verify_alwayson.py                  OK 
verifiers/verify_corpus_independent.py        OK 
verifiers/verify_corpus_integrity.py           OK 
verifiers/verify_dispatch_prompts.py          OK 
verifiers/verify_harness_claims.py             OK 
verifiers/verify_harness_independent.py        OK 
verifiers/verify_skill_checklist.py            OK
gate registry rows conformant 41 of 41 lane verifiers; phantom 0

COMMAND_EXIT_CODE=0
```

## Claim scope, risk, and blockers

- C1 (G7 `span_missing` arm pinning) is neither supported nor falsified by this identity battery: it is a base==tip no-harm baseline, and its listed scoped self-tests are not the frozen v32 223-assertion predicate. [INFERENCE]
- C2 (round-63 routed-repairs counter) is neither supported nor falsified by this run: the battery's informational `routed-repairs` line is the existing routed-repairs check (`6 of 6`), not the new frozen r64 counter predicate. [INFERENCE]
- The measured evidence supports the requested round-64 base baseline: all listed gating arms pass at identity and the battery self-checks detect their injected differences. Registry count is 41/41 with zero phantom entries.
- No tools were installed or updated. No blockers for this assigned baseline task.
