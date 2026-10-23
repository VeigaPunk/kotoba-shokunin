Result: DONE — The scoped description-threshold gate now honors both C2 probe classes; the aggregate counter still has misses in other gates.

## Files and behavior

- Sandbox commit `4a27570a0114fb90a340da160d18eaee18102d88` changes only `verifiers/check_description_thresholds.py` (30 insertions). Unified diff: `.ufo/waves/round-55/build/FixDescThresholds.patch`.
- Before reading revision data, the gate now verifies `--rev` with `git rev-parse --verify --quiet <rev>^{commit}`. A failed check flows through the existing `could-not-evaluate:` stderr / exit-2 handler. Missing `git` remains an OSError handled by that same path. The self-test adds subprocess assertions for an unknown revision and for a PATH containing only a `python3` link.
- Judging logic and clean-path output were not changed.

## Probe causes and evidence

- **R:** At the plan commit, `verifiers/check_description_thresholds.py:114-123` ran `git show <rev>:<path>` and treated stderr containing `does not exist` as an absent file. For an unknown revision, all reads became empty input; the gate then returned its ordinary verdict 1. Before-fix sandbox command `timeout 900s python3 -B verifiers/check_description_thresholds.py --rev 0000000000000000000000000000000000000000` exited 1 and printed `description thresholds backed 0 of 7 clients`. Base receipt also records R got 1 (`.ufo/waves/round-55/controls/C2-base.txt:25`). The new preflight is at patch lines 21-28; the existing error handler is at base lines 414-416.
- **G:** G was already honored at base: `C2-base.txt:26` records got 2. The base `subprocess.run` in `read_file` (line 116) lets `FileNotFoundError` propagate to the `OSError` handler at lines 414-416, which emits the could-not-evaluate line and returns 2. The new preflight is within that same handler. The regression assertions are in the patch at lines 36-52.

## Retained check evidence

- Before: gate `--self-test` at the plan commit → `self-test: 0 failure(s) over 22 assertions`; exit 0.
- After: `timeout 900s env TMPDIR=/fast/scratch/hyaku/kotoba-r55/FixDescThresholds/tmp python3 -B verifiers/check_description_thresholds.py --self-test` → `self-test: 0 failure(s) over 24 assertions`; exit 0.
- Real verdict before the edit at plan commit: `description thresholds backed 7 of 7 clients`; exit 0. After commit, the same real verdict at both plan revision `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` and sandbox `HEAD` was `description thresholds backed 7 of 7 clients`; exit 0 for each.
- C2 command in the sandbox: `timeout 900s env TMPDIR=/fast/scratch/hyaku/kotoba-r55/FixDescThresholds/tmp python3 -B verifiers/check_could_not_evaluate.py --rev HEAD`. It printed `check_description_thresholds.py R expect 2   got 2 ok`, `check_description_thresholds.py G expect 2   got 2 ok`, `check_description_thresholds.py S expect 0   got 0 ok`, and `check_description_thresholds.py V expect 0|1 got 0 ok`; summary: `could-not-evaluate probes honoured 14 of 25; controls held 13 of 13`; exit 1. The target gate's probes and controls pass; 11 misses remain in other gates and are outside this assignment.
- Diff stat: `verifiers/check_description_thresholds.py | 30 ++++++++++++++++++++++++++++++`; `1 file changed, 30 insertions(+)`.

## Risks and blockers

No blocker to the assigned gate fix. The frozen aggregate C2 predicate remains unmet by the other gates' misses. No LSP interface was exposed in the available tool inventory, so no LSP query was available. No tools were installed.