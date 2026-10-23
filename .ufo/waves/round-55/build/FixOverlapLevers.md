Result: DONE — `check_overlap_levers.py` now returns 2 for unknown revisions and unavailable git, with both cases covered by its self-test.

## Findings

- **Class R root cause:** At the plan source, `verifiers/check_overlap_levers.py:526-533` treated every nonzero `git show` result as a missing file (`None`). `main` at `:560-565` did not first validate the revision, so the unknown revision became empty input and was judged as exit 1. Frozen receipt `.ufo/waves/round-55/controls/C2-base.txt:13` records R as `got 1 MISS`.
- **Class G root cause/status:** At the plan source, an unavailable `git` raised `OSError` from `subprocess.run` (`:528-530`); `main` caught it at `:583-585` and returned 2. The frozen receipt `C2-base.txt:14` confirms G was already `got 2 ok` (not a base miss), but used the generic `ERROR reading input` path and had no regression assertion. The repair catches this as `EnvError` and emits a `could-not-evaluate:` diagnostic.
- Added a `git rev-parse --verify --quiet <rev>^{commit}` preflight before `git show`, maps verification failure and git-launch `OSError` to exit 2, and added two self-test assertions. The judging logic and clean-path output were left unchanged; the patch is `.ufo/waves/round-55/build/FixOverlapLevers.patch:5-84`.
- Sandbox commit: `98aaea8bd04b626ec2acbbb25377d2529ed04212`. Diff stat: `verifiers/check_overlap_levers.py | 56 ++++++++++++++++++++++++++++++++++++---`; `1 file changed, 53 insertions(+), 3 deletions(-)`.

## Evidence

- Before change, sandbox self-test: `timeout 900 python3 -B verifiers/check_overlap_levers.py --self-test` — exit 0; output `0 failures`, `51 assertions`.
- After change: `timeout 900 mkdir -p /fast/scratch/hyaku/kotoba-r55/FixOverlapLevers/.tmp && TMPDIR=/fast/scratch/hyaku/kotoba-r55/FixOverlapLevers/.tmp timeout 900 python3 -B verifiers/check_overlap_levers.py --self-test` — exit 0; output `0 failures`, `53 assertions`.
- Real verdicts after commit, from the sandbox:
  - `timeout 900 python3 -B verifiers/check_overlap_levers.py --rev a10240c0940f770a5f2a5f32a7e3c363dd5d40c` — exit 0; `overlap levers backed 7 of 7 clients`.
  - `timeout 900 python3 -B verifiers/check_overlap_levers.py --rev 98aaea8bd04b626ec2acbbb25377d2529ed04212` — exit 0; `overlap levers backed 7 of 7 clients`.
- Frozen C2 counter: `TMPDIR=/fast/scratch/hyaku/kotoba-r55/FixOverlapLevers/.tmp timeout 900 python3 -B verifiers/check_could_not_evaluate.py --rev HEAD` — exit 1 overall; target gate evidence:
  ```
  check_overlap_levers.py            R expect 2   got 2 ok
  check_overlap_levers.py            G expect 2   got 2 ok
  check_overlap_levers.py            S expect 0   got 0 ok
  check_overlap_levers.py            V expect 0|1 got 0 ok
  could-not-evaluate probes honoured 14 of 25; controls held 13 of 13
  ```
  The remaining 11 probe misses belong to other gates and are outside this assignment.

## Files and risks

- Lane deliverables: `.ufo/waves/round-55/build/FixOverlapLevers.patch` and this report. The implementation was committed only in the sandbox clone; no lane source file was edited.
- No blocker for this gate. The frozen C2 counter remains below its overall target (14/25) because of other gate probes.
- No LSP tool was exposed in this session's tool inventory; implementation used the source reads and anchored edits above. No tools were installed or updated.
