Result: DONE — `check_correction_sweep.py` now verifies revisions before reading and maps Git execution errors to exit 2; the frozen C2 counter still has misses in other gates.

## Files and change
- Sandbox change: `verifiers/check_correction_sweep.py`, committed at `16f2b2f4ff1b750ab4390b2531f1ee5d2b5b0439` (plan base `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`).
- Delivered unified diff: `.ufo/waves/round-55/build/FixCorrectionSweep.patch`.
- Diff stat against plan: `1 file changed, 35 insertions(+), 1 deletion(-)`.
- Regression arm: self-test runs the CLI with an unknown 40-hex revision and with PATH containing only a `python3` symlink, asserting exit 2 and a `could-not-evaluate:` diagnostic. Existing sweep fixtures and verdict logic remain in place.

## Probe causes at plan base
- R: `verifiers/check_correction_sweep.py:128-130` ran `git show` without a revision preflight and converted any failed read to `None`; `sweep` then raised for the missing registry file (`:112-113`), and `main` mapped that `RuntimeError` to exit 2 (`:207-209`). Thus R already passed at base, but only indirectly; the fix now runs `git rev-parse --verify --quiet <rev>^{commit}` before reading and reports an unresolvable revision as could-not-evaluate.
- G: the same `subprocess.run` at `:128` raised `FileNotFoundError` when PATH lacked git, but base `main` caught only `RuntimeError` (`:207-209`), so the process exited 1. The base receipt records `check_correction_sweep.py G expect 2 got 1 MISS` at `.ufo/waves/round-55/controls/C2-base.txt:41-44`. `main` now catches `OSError` and returns 2 with the required stderr prefix.

## Retained evidence
Commands below ran in the sandbox clone. At plan base, `python3 -B verifiers/check_correction_sweep.py --self-test` printed `0 failure(s) over 11 assertions`, exit 0; `--rev HEAD` printed `correction sweep: 0 stale block(s)`, exit 0.

At final commit:
- `python3 -B verifiers/check_correction_sweep.py --self-test`: `0 failure(s) over 13 assertions`; exit 0. Assertion count: 11 before, 13 after.
- `python3 -B verifiers/check_could_not_evaluate.py --rev HEAD`: this gate's lines were `check_correction_sweep.py R expect 2 got 2 ok`, `G expect 2 got 2 ok`, `S expect 0 got 0 ok`, and `V expect 0|1 got 0 ok`. Summary: `could-not-evaluate probes honoured 14 of 25; controls held 13 of 13`; counter exit 1. The remaining misses are other gates, outside this assignment.
- Real verdict on plan commit (`--rev a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`): `correction sweep: 0 stale block(s)`, exit 0.
- Real verdict on final sandbox commit (`--rev HEAD`, measured `16f2b2f4ff1b750ab4390b2531f1ee5d2b5b0439`): `correction sweep: 0 stale block(s)`, exit 0. Summary and exit code match the plan verdict.

An intermediate commit's self-test exposed an overly narrow assertion expecting the phrase `git not runnable`; the actual OSError text named `'git'`. That assertion was corrected, the original green fixture retained, and the final self-test and C2 evidence above were rerun on the final commit.
