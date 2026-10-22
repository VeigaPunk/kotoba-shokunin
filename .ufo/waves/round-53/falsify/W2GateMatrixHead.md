Result: BREAKS — At c775d68, both red corpus gates add `corpus.pointers.commit_unresolvable` for S050’s external Zed revision; the unindexed corpus item also moved to a new round-53 entry.

## Scope and evidence

`git rev-parse HEAD` in the lane checkout returned `c775d6823bfca8f0de8c0874032a954438b38edc` (exit 0). Path-sensitive gates below ran from that lane checkout. `fault_injection_corpus.sh` ran only in the isolated clone `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2GateMatrixHead`; its output identifies `head=c775d68`. Base values are from `.ufo/waves/round-53/build/ExecGateMatrixBase.md` unless marked as the L1’s plan run (`plans/round-53.md:27-28, 40-42`).

| Gate / head command | Base exit + summary | Head exit + observed summary | Harm? |
|---|---|---|---|
| `check_opencode_repin.py --rev c775d6823bfca8f0de8c0874032a954438b38edc` | 1 — 6/7 surfaces, `opencode_extract FAIL`; pins 2/3; 9/9 classes; 0 failures over 129 assertions (plan:27-28). | 0 — 7/7 surfaces, `opencode_extract PASS`; pins 3/3; 9/9 classes; 0 failures over 155 assertions. Host opencode SHA `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`. | No; improved. |
| `check_alwayson_boxes.py --rev c775d6823bfca8f0de8c0874032a954438b38edc` | 1 — 0/8; `alwayson.04` and `.07` unexecuted (plan:41-42). | 0 — `always-on boxes executed and discriminating 2 of 8`; `.04` and `.07` each counted, 6/6 cases. | No; improved. |
| `verify_alwayson.py --self-test` (additional) | — (not in base matrix) | 0 — `0 failure(s) over 89 assertions`. | No baseline comparison. |
| `verify_alwayson.py --box-proof` (additional) | — (not in base matrix) | 0 — `boxes proven 2`. | No baseline comparison. |
| `check_gate_finding_delta.py --self-test` (additional) | — (not in base matrix) | 0 — `self-test: 0 failure(s) over 9 assertions`. | No baseline comparison. |
| `verify_harness_claims.py` live | Not run; base matrix withheld it. | Not run; intentionally withheld. At `verifiers/verify_harness_claims.py:391-408`, the live instrument walks session directories and opens `.jsonl` files, then scans their line contents. Reading session material would violate the shape-only restriction. | Blocked by privacy constraint; no result claimed. |
| `verify_harness_claims.py --self-test` | 0 — 0 failures over 10 assertions. | 0 — `self-test: 0 failure(s) over 10 assertions`. | No. |
| `verify_surfaces.py --json` | 1 — 6 pass, 1 fail; `surfaces.opencode_extract` FAIL (OC-4/OC-6 unmatched). | 0 — 7 pass, 0 fail; `surfaces.opencode_extract` PASS; 9/9 declared opencode classes from 7/7 rules. | No; improved. |
| `verify_surfaces.py --self-test` | 0 — 0 failures over 129 assertions. | 0 — `0 failure(s) over 155 assertions`. | No. |
| `verify_skill_checklist.py --json` | 1 — 8 pass, 3 fail: `trigger.name_directory`, `trigger.citation_resolves`, `governance.citation_resolves`. | 0 — 11 pass, 0 fail; `checklist.box_map_complete` PASS. | No; improved. |
| `verify_skill_checklist.py --self-test` | 0 — 0 failures over 1851 assertions. | 0 — `0 failure(s) over 1852 assertions`. | No. |
| `verify_corpus_integrity.py` | 1 — 4/9; drift: tracked_files 76/72, unindexed 1, report_total 49/46, report_dead 5, commit_total 31/30. | 1 — 4/9; drift: tracked_files 77/72, unindexed 1, report_total 49/46, commit_total 32/30, and **new** `commit_unresolvable=1`; report_dead is now 0. The unindexed path is `corpus/knowledge/alwayson-rule-files-round53.md`. | **Breaks:** new finding id `corpus.pointers.commit_unresolvable`; the existing `corpus.index.unindexed` id also now names a different file. |
| `verify_corpus_integrity.py --self-test` | 0 — 0 failures over 150 assertions. | 0 — `self-test: 0 failure(s) over 152 assertions`. | No. |
| `verify_corpus_independent.py` | 1 — tracked_files 76; unindexed 1, report_dead 5, commit unresolvable 0, nonhash 0. | 1 — tracked_files 77; unindexed 1, report_dead 0, commit unresolvable 1, nonhash 0. | **Breaks:** confirms the same new `corpus.pointers.commit_unresolvable` finding independently. |
| `verify_corpus_independent.py --self-test` | 0 — 91 assertions, 0 failures. | 0 — `self-test: 93 assertions, 0 failures`. | No. |
| `check_substrate_pins.py` | 1 — 1/3 pins failed: `opencode_binary_sha256`. | 0 — `OK 3/3 pins hold`. | No; improved. |
| `check_substrate_pins.py --self-test` | 0 — 0 failures over 62 assertions. | 0 — `0 failure(s) over 62 assertions`. | No. |
| `check_assertion_floors.py` | 0 — all 12 registry rows PASS; vector `10/150/91/129/1851/62/123/330/150/56/68/51`. | 0 — all 13 rows PASS at floor; vector `10/152/93/155/1852/62/123/330/150/56/68/51/89`; includes alwayson 89. | No; no floor lowered. |
| `compare_harness_independent.py --self-test` | 0 — 0 failures over 330 assertions. | 0 — `self-test: 0 failure(s) over 330 assertions`. | No. |
| `verify_harness_independent.py --self-test` | 0 — 0 failures over 123 assertions. | 0 — `0 failure(s) over 123 assertions`. | No. |
| `verify_dispatch_prompts.py` | 1 — dispatch.04: 315 evaluated, 287 PASS / 6 FAIL / 22 N/A; dispatch.08: 307 evaluated, 278 PASS / 0 FAIL / 29 N/A. | 1 — same evaluated counts, outcomes and failing ids (`dispatch.04`, `dispatch.08`); dispatch.04 still names the same six report files. | No new finding id; unchanged red gate. |
| `verify_dispatch_prompts.py --self-test` | 0 — 0 failures over 56 assertions. | 0 — `0 failure(s) over 56 assertions`. | No. |
| `verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 — boxes proven 2. | 0 — `boxes proven 2`. | No. |
| `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` | 0 — 20/20 rows; province 20/20; skill description 9/9 lanes, 1019/1024 chars. | 0 — same: 20/20 rows, 20/20 province rows, 9/9 lanes, 1019/1024 chars. | No. |
| `check_overlap_levers.py --rev c775d6823bfca8f0de8c0874032a954438b38edc` | 0 — overlap levers backed 7/7 clients. | 0 — `overlap levers backed 7 of 7 clients`. | No. |
| `check_mcp_instructions.py --rev c775d6823bfca8f0de8c0874032a954438b38edc` | 0 — MCP instructions backed 7/7 clients. | 0 — `mcp instructions backed 7 of 7 clients`. | No. |
| `check_callee_rename.py --rev c775d6823bfca8f0de8c0874032a954438b38edc` | 0 — robust 4/4 fixtures. | 0 — `callee-rename robust 4 of 4 fixtures`. | No. |
| `check_correction_sweep.py --root .` | 0 — 0 stale blocks. | 0 — `correction sweep: 0 stale block(s)`. | No. |
| `box_proof_case_deletion.py --rev c775d6823bfca8f0de8c0874032a954438b38edc` | 0 — killed 6/6; controls 2/2, N/A 1/1. | 0 — killed 6/6; controls 2/2, N/A 1/1. | No. |
| `bash verifiers/fault_injection_corpus.sh` (sandbox clone only) | 1 — control `FAIL-control-dirty`; faults a-e PASS, f/h FAIL, g FALSE-POSITIVE; `verdict: FAILURES PRESENT`. | 1 — same verdicts; head integrity output includes `corpus.pointers.commit_unresolvable` in the control and injected-world fired-class lists; `verdict: FAILURES PRESENT`. | **Breaks:** the newly observed corpus finding is present in this already-red gate’s output too. |

## Findings

1. **Moderate — new unresolved corpus commit citation.** Base independent-corpus output reported `commit unresolvable=0`; at head both `verify_corpus_integrity.py` and `verify_corpus_independent.py` report `corpus.pointers.commit_unresolvable=1`. The exact citation is `corpus/SOURCES.md:63` (S050): `zed-industries/zed@cfb894a5`. The same head ID is visible in the fault-injection output. The row identifies this as a Zed upstream source revision, not a Kotoba commit **[INFERENCE]**; the repository-local commit resolver appears to count it anyway. This is a new finding ID in gates that were already red, so it meets the specified no-harm break condition.

2. **Low — new unindexed corpus entry under an existing finding ID.** Base matrix notes the round-52 spot-check as the unindexed file (`ExecGateMatrixBase.md:41`). Head integrity output instead names `corpus/knowledge/alwayson-rule-files-round53.md`, with the count still 1. Thus the old unindexed item was replaced by a newly added, unindexed round-53 knowledge file. This is not a new check ID, but is a changed target and a remaining corpus-index defect.

## Blocker and risk

The live `verify_harness_claims.py` command was not run: its source opens and scans session `.jsonl` contents, which are protected shape-only material. The base matrix also records it as not run; the self-test did run and passed, but is not a substitute for live evidence. No tools were installed.