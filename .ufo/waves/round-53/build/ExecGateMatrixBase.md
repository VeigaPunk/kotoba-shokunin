Result: PARTIAL — 23 of 24 requested command invocations ran on the e78dff6 base clone; the live harness observation was withheld to avoid reading protected session JSONL content.

## Scope and invocation

Axes: calibration (recorded exits and outputs) and no-harm (before-matrix only). The sandbox clone was `/fast/scratch/hyaku/kotoba-r53/ExecGateMatrixBase`; `git rev-parse HEAD` returned `e78dff667237fba2e3cf9eccb802eff5bc9ea302`, matching `plans/round-53.md:3-8`. Commands ran from that clone root with `TMPDIR=/fast/scratch/hyaku/kotoba-r53/ExecGateMatrixBase/.tmp`; argv is shown in the table. The gate commands did not modify implementation files.

Arguments were checked with each Python gate's `--help`. `check_correction_sweep.py --root .` follows `LOG.md:2437`; the dispatch proof's explicit map and the sibling census arguments follow `SCORECARD.md:273-274`. The full fault-injection command uses the script's documented default repo (`verifiers/fault_injection_corpus.sh:21-31`). Dispatch's default live run uses the host fleet prompt/state paths shown by its `--help`, not paths from the clone.

| Gate | Command | Exit | Summary line / observed result |
|---|---|---:|---|
| Harness claims (live) | `python3 -B verifiers/verify_harness_claims.py` | — | Not run: the live instrument enumerates `~/.omp/agent/sessions` and reads each `.jsonl` line (`verifiers/verify_harness_claims.py:391-403`); this conflicts with the shape-only session-material rule. No host session content was read by this run. |
| Harness claims self-test (additional fixture-only evidence) | `python3 -B verifiers/verify_harness_claims.py --self-test` | 0 | `self-test: 0 failure(s) over 10 assertions` |
| Surfaces | `python3 -B verifiers/verify_surfaces.py --json` | 1 | JSON: `pass=6`, `fail=1`, `exit_code=1`; `surfaces.opencode_extract` FAIL (OC-4 and OC-6 matched no rules). Observed opencode SHA-256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`; omp SHA-256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`. |
| Surfaces self-test | `python3 -B verifiers/verify_surfaces.py --self-test` | 0 | `0 failure(s) over 129 assertions` |
| Skill checklist | `python3 -B verifiers/verify_skill_checklist.py --json` | 1 | JSON: `pass=8`, `fail=3`, `exit_code=1`; failed ids: `trigger.name_directory`, `trigger.citation_resolves`, `governance.citation_resolves`. |
| Skill checklist self-test | `python3 -B verifiers/verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over 1851 assertions` |
| Corpus integrity | `python3 -B verifiers/verify_corpus_integrity.py` | 1 | `4/9 checks pass`; DRIFT: tracked_files `76/72`, unindexed `1`, report_total `49/46`, report_dead `5`, commit_total `31/30`. |
| Corpus integrity self-test | `python3 -B verifiers/verify_corpus_integrity.py --self-test` | 0 | `self-test: 0 failure(s) over 150 assertions` |
| Independent corpus | `python3 -B verifiers/verify_corpus_independent.py` | 1 | `tracked_files=76`; `unindexed=1`, `report_dead=5`, commit `unresolvable=0`, `nonhash=0`; final `exit 1`. |
| Independent corpus self-test | `python3 -B verifiers/verify_corpus_independent.py --self-test` | 0 | `self-test: 91 assertions, 0 failures` |
| Substrate pins | `python3 -B verifiers/check_substrate_pins.py` | 1 | `DRIFT 1/3 pins failed: opencode_binary_sha256`; expected SHA `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`, observed `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`. |
| Substrate pins self-test | `python3 -B verifiers/check_substrate_pins.py --self-test` | 0 | `0 failure(s) over 62 assertions` |
| Assertion floors | `python3 -B verifiers/check_assertion_floors.py` | 0 | All 12 registry rows PASS at observed=floor; vector in output order: `10/150/91/129/1851/62/123/330/150/56/68/51`. |
| Harness comparator self-test | `python3 -B verifiers/compare_harness_independent.py --self-test` | 0 | `self-test: 0 failure(s) over 330 assertions` |
| Independent harness self-test | `python3 -B verifiers/verify_harness_independent.py --self-test` | 0 | `0 failure(s) over 123 assertions` |
| Dispatch prompts | `python3 -B verifiers/verify_dispatch_prompts.py` | 1 | `dispatch.04` FAIL: 315 evaluated, 287 PASS / 6 FAIL / 22 N/A (28 out of scope); `dispatch.08` PASS: 307 evaluated, 278 PASS / 0 FAIL / 29 N/A (13 out of scope). |
| Dispatch prompts self-test | `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | 0 | `0 failure(s) over 56 assertions` |
| Dispatch box proof | `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 | `boxes proven 2` |
| Sibling census | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` | 0 | `rows 20 verified 20`; `province rows 20 matched 20`; skill description `9 of 9` non-none lanes, `1019 of 1024` characters. |
| Overlap levers | `python3 -B verifiers/check_overlap_levers.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302` | 0 | `overlap levers backed 7 of 7 clients` |
| MCP instructions | `python3 -B verifiers/check_mcp_instructions.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302` | 0 | `mcp instructions backed 7 of 7 clients` |
| Callee rename | `python3 -B verifiers/check_callee_rename.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302` | 0 | `callee-rename robust 4 of 4 fixtures` |
| Correction sweep | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | `correction sweep: 0 stale block(s)` |
| Box-proof case deletion | `python3 -B verifiers/box_proof_case_deletion.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302` | 0 | `killed 6 of 6`; controls `2 of 2`, N/A `1 of 1`. |
| Corpus fault injection | `bash verifiers/fault_injection_corpus.sh` | 1 | `verdict: FAILURES PRESENT`; control `FAIL-control-dirty`, fault-f and fault-h `FAIL`, fault-g `FALSE-POSITIVE`. Faults a-e were `PASS`. Worlds were directed under clone-local `.tmp`. |

## Calibration notes and blocker

- The unrun live harness gate is the sole missing requested invocation. Its source opens every matching session `.jsonl` and scans line contents for embedded `<skills>` data (`verifiers/verify_harness_claims.py:391-403`). The separate fixture-only self-test passed; it is not a substitute for a live observation. A privacy-compliant way to measure the live gate without content-reading session material is the missing prerequisite.
- The checklist JSON run's failures include the clone basename (`ExecGateMatrixBase`) differing from the skill name and citations that do not resolve from this scratch layout. **[INFERENCE]** These may be location-sensitive baseline effects; no rerun against the lane checkout or adjustment to the clone was made, so they remain the observed clone results.
- Corpus integrity and the independent derivation both show the base's unindexed round-52 spot-check and five dead report pointers. The fault-injection control is correspondingly dirty at this base; the remaining fault-f/g/h statuses are recorded as printed, not normalized away.
- No tools were installed. The requested report is the only file written in the lane: `.ufo/waves/round-53/build/ExecGateMatrixBase.md`.
