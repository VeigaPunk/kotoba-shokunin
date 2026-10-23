Result: DONE — The checker now rejects the routed probe shortcut and borrowed self-test flags; the required sandbox controls were exercised.

## Changed files

- `verifiers/check_gate_registry.py` — delivered as `.ufo/waves/round-55/build/ExecRegistryHarden.patch` (based on plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`).
- This report. No lane implementation file was edited directly; the checker patch and control mutations were run in `/fast/scratch/hyaku/kotoba-r55/ExecRegistryHarden`.

## Behavior

- A `probe` row is rejected if its verdict pairs include `1=failed` **or** the matching source has an exact active `--self-test` handler. The check reads only the row's parsed verdict pairs and the script source: Python AST calls to `add_argument` with an exact string argument, or a shell `case` arm with the exact pattern. It does not execute the script. This narrow rule and its Q31 limit are documented in the checker docstring.
- A self-test flag named in a row must match that exact active handler. A flag mentioned only in a comment or as a longer lookalike is not accepted.
- The self-test now has must-fail cases for a borrowed Python flag in a comment and an all-probe/none registry, plus exact-shell-arm, shell-comment and lookalike checks.
- The checker’s `--rev` and git-unavailable error paths were not changed.

## Receipts

All commands below ran in the sandbox clone. `timeout 900` was used for each command.

1. `timeout 900 python3 -B verifiers/check_gate_registry.py --self-test` — exit **0**:

   `self-test: 0 failure(s) over 28 assertions`

2. Honest registry at plan commit: `timeout 900 python3 -B verifiers/check_gate_registry.py --rev a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` — exit **1**. It printed `gate registry rows conformant 24 of 26 lane verifiers; phantom 0`. The two absent rows printed as `verifiers/check_could_not_evaluate.py no registry rows naming it: 0 (need 1)` and `verifiers/check_explicit_invocation.py no registry rows naming it: 0 (need 1)`. The 24 rows in `SKILL.md:455-478` otherwise conform. So it does **not** print the requested `24 of 24`: the plan revision's universe has 26 scripts, including these two unregistered round-55 counters. This is reported, not changed in the scoped checker patch.

3. Cheapest control: all 24 registry rows were changed in a sandbox commit based on the plan to `probe`, with self-test and pinned-values cells set to `none`. `timeout 900 python3 -B verifiers/check_gate_registry.py --rev 9b9f2b0` — exit **1**, summary `gate registry rows conformant 0 of 26 lane verifiers; phantom 0`. The 24 table rows were each rejected with `probe verdict map declares 1=failed; probe script has an exact --self-test handler`; the two unregistered counter files remained unregistered. The control therefore fails rather than reaching M of M.

4. C2 control paths on checker-patch commit `510b752d1b3549ac48515a22eaa8f69d8fb93d77`: `timeout 900 python3 -B verifiers/check_could_not_evaluate.py --rev 510b752` — overall exit **1** (`could-not-evaluate probes honoured 13 of 25; controls held 13 of 13`). Its checker-specific receipt was:

   ```
   check_gate_registry.py             R expect 2   got 2 ok
   check_gate_registry.py             G expect 2   got 2 ok
   check_gate_registry.py             S expect 0   got 0 ok
   check_gate_registry.py             V expect 0|1 got 1 ok
   ```

   Thus class R and G remain exit 2, and `--self-test` exits 0. The overall C2 exit 1 is due to other gates' pre-existing misses: `box_proof_case_deletion.py` R/G; `check_gate_finding_delta.py` both R probes and G; `check_overlap_levers.py` R; `check_mcp_instructions.py` R/G; `check_description_thresholds.py` R; `check_correction_sweep.py` G; `check_assertion_floors.py` G; and `verify_corpus_independent.py` G. The counter's 13/13 controls held.

## Risks and blockers

- The probe rule is intentionally bounded: it catches a declared `1=failed` or an in-file `--self-test` handler, not every possible failure mechanism. It does not claim to prove runtime verdict behavior; review remains required as stated in the docstring.
- The honest plan-commit registry is 24/26 because the two round-55 counters have no registry rows. Fixing that table is outside this checker-only assignment.
- No tooling was installed or updated.
