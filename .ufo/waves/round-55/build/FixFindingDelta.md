Result: DONE — the assigned gate now returns 2 for both frozen R positions and G; the frozen C2 run still misses other gates.

## Change

In sandbox commit `08e7db9b29a2c58e96207caac1a3919a5e1b0561`, `verifiers/check_gate_finding_delta.py` now verifies each revision with `git rev-parse --verify --quiet <rev>^{commit}` before extraction. An unknown base or head raises the gate's could-not-evaluate error; Git startup errors and failed checked Git commands are caught at `main`, printed with the `could-not-evaluate:` stderr prefix, and return 2. The clean verdict output and the finding comparison/counting logic are unchanged.

The self-test now exercises unknown revisions in both argument positions and Git unavailable with a PATH containing only a `python3` link. Its assertion count is computed from the checks.

## Routed causes

- **R, both `--base` and `--head`:** At the plan revision, `run` passed both revisions directly to `extract` (`verifiers/check_gate_finding_delta.py:85-93`); `extract` ran `git archive <rev>` with `check=True` and had no revision precheck (`:56-64`). An unknown revision therefore raised an uncaught `CalledProcessError`, producing exit 1 instead of 2.
- **G:** `extract` and `revision_env` spawn Git (`:58-60`, `:78-81`), while the plan revision's `main` directly returned `run(...)` without catching `OSError` (`:154-167`). With `git` absent, `FileNotFoundError` escaped and produced exit 1.

## Evidence

Baseline receipt `.ufo/waves/round-55/controls/C2-base.txt:8-12`: this gate's R, R, and G probes each got 1; S got 0 and V got 0. Baseline counter summary at `:55-60` was `could-not-evaluate probes honoured 13 of 25; controls held 13 of 13`, exit 1.

- Baseline self-test, using the plan-revision gate in the sandbox: `timeout 900 python3 -B /fast/scratch/hyaku/kotoba-r55/FixFindingDelta/.before/check_gate_finding_delta.py --self-test` — exit 0; output `self-test: 0 failure(s) over 9 assertions`.
- Repaired self-test: `timeout 900 python3 -B verifiers/check_gate_finding_delta.py --self-test` — exit 0; output `self-test: 0 failure(s) over 12 assertions`.
- Frozen counter: `timeout 900 python3 -B verifiers/check_could_not_evaluate.py --rev HEAD` — exit 1 overall. Its lines for this gate were:

```text
check_gate_finding_delta.py        R expect 2   got 2 ok
check_gate_finding_delta.py        R expect 2   got 2 ok
check_gate_finding_delta.py        G expect 2   got 2 ok
check_gate_finding_delta.py        S expect 0   got 0 ok
check_gate_finding_delta.py        V expect 0|1 got 0 ok
could-not-evaluate probes honoured 16 of 25; controls held 13 of 13
```

The counter's other nine misses were on `box_proof_case_deletion.py` (R, G), `check_overlap_levers.py` (R), `check_mcp_instructions.py` (R, G), `check_description_thresholds.py` (R), `check_correction_sweep.py` (G), `check_assertion_floors.py` (G), and `verify_corpus_independent.py` (G). The assigned gate passed all five of its counter runs.

Real verdict comparison, both with base=head at the measured revision:

- Plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`: `timeout 900 python3 -B /fast/scratch/hyaku/kotoba-r55/FixFindingDelta/.before/check_gate_finding_delta.py --repo /fast/scratch/hyaku/kotoba-r55/FixFindingDelta --base a10240c0940f770a5f2a5f32a7e3c363dd5d40c0 --head a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` — exit 0; output ended `finding delta: new 0, resolved 0`.
- Sandbox commit `08e7db9b29a2c58e96207caac1a3919a5e1b0561`: `timeout 900 python3 -B verifiers/check_gate_finding_delta.py --repo /fast/scratch/hyaku/kotoba-r55/FixFindingDelta --base 08e7db9 --head 08e7db9` — exit 0; output ended `finding delta: new 0, resolved 0`.

Diff stat against the plan commit: `1 file changed, 57 insertions(+), 2 deletions(-)` (`verifiers/check_gate_finding_delta.py`). Unified diff delivered at `.ufo/waves/round-55/build/FixFindingDelta.patch`.

LSP was not exposed in the available tool inventory; source and neighboring gate patterns were read directly. No tools were installed.