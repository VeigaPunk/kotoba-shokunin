Result: MIXED — all six mutations are killed by `--self-test`, while five survive the narrower frozen counter.

## Scope and baseline

Target: `verifiers/verify_alwayson.py` at judged revision `c775d6823bfca8f0de8c0874032a954438b38edc`. The relevant logic is `_has_import_line` and `_redirects_to` (`verifiers/verify_alwayson.py:292-357`) plus canonical-name selection (`:360-377`). Self-test cases pin these attacks at `:416-430`; the frozen counter pins only six `alwayson.07` cases at `verifiers/check_alwayson_boxes.py:76-86`.

Pristine bytes SHA-256: `e4a8b3f230bb5c467798b6cb8bf31b420069d972844315dc4a85f243d9adc890`.

On pristine local revision `c775d6823bfca8f0de8c0874032a954438b38edc`:

- `python3 -B verifiers/verify_alwayson.py --self-test` → `0 failure(s) over 89 assertions`, exit 0.
- `python3 -B verifiers/check_alwayson_boxes.py --rev c775d6823bfca8f0de8c0874032a954438b38edc --repo .` → `always-on boxes executed and discriminating 2 of 8`; both `alwayson.04` and `.07` counted `6 of 6 cases as pinned`; exit 0.

## Kill table

For each mutant, the self-test was run on its local mutation commit and the counter was run with `--rev` set to that same commit. “Killed” means the detector returned the pinned failing result; counter survivors are coverage findings, not changes to the frozen contract. Severity is for the counter coverage gap; the target self-test kills every named mutant.

| Mutant | Expected detector | Actual output and verdict |
|---|---|---|
| Accept any `@AGENTS.md` substring | Self-test `inline-import-mention` expects FAIL. Mutation commit `9586f14020733abd677ed56115bdbd8b52006b48`, instrument SHA-256 `494c8d85a9b166cb4047cbbe4978fb6c354c6b909dbd634670978b93de3ef1f9`. | Self-test emitted `self-test FAIL: inline-import-mention direct result` and `... JSON and exit contract`; `2 failure(s) over 89 assertions`, exit 1 — killed. Counter printed `2 of 8`, both boxes counted, exit 0 — survived. **HOLDS** for self-test; **low** counter-coverage gap (no inline-import case). |
| Accept any symlink target | Self-test `wrong-symlink-target` expects FAIL. Mutation commit `08f906f10b1e85cd185e010874d436bcb7f5be9b`, SHA-256 `13b02716387db353ce7d47c92d5037f7f2f29c71880721ec66470190f9bfb1e7`. | Self-test emitted `self-test FAIL: wrong-symlink-target direct result` and `... JSON and exit contract`; `2 failure(s) over 89 assertions`, exit 1 — killed. Counter printed `2 of 8`, both boxes counted, exit 0 — survived. **HOLDS** for self-test; **low** counter-coverage gap (counter pins a valid redirect, not a wrong-target symlink). |
| Ignore `CLAUDE.local.md` | Self-test `local-conflict` expects FAIL. Mutation commit `890198ccab41e3f7559acf61b2a0aa8bbcd0d8f7`, SHA-256 `649994cc1712bc6532edda75b07d3e9458a3a2b97b4dbbaec2509039411878d5`. | Self-test emitted `self-test FAIL: local-conflict direct result` and `... JSON and exit contract`; `2 failure(s) over 89 assertions`, exit 1 — killed. Counter printed `2 of 8`, both boxes counted, exit 0 — survived. **HOLDS** for self-test; **low** counter-coverage gap (no local-file conflict case). |
| Ignore `.claude/CLAUDE.md` in pair checking | Self-test `nested-pair` and `nested-claude-conflict` expect FAIL. Mutation commit `705edc3f3777555db9e9f8dbd522a4693978ef7e`, SHA-256 `95bd3f44fb16ef34db29180aade94da7fea6ea30569c3fd7ab19503d7b3a72ed`. | Self-test emitted direct-result and JSON/exit failures for both cases; `4 failure(s) over 89 assertions`, exit 1 — killed. Counter printed `2 of 8`, both boxes counted, exit 0 — survived. **HOLDS** for self-test; **low** counter-coverage gap (no nested-pair case). |
| Accept prose mentions | Self-test `prose-mention` expects FAIL; frozen counter also pins this case. Mutation commit `0b43e75b77592e055b158cd1fd3dfa8f2aa45425`, SHA-256 `d7b7b8629d7b6b1cfa5db4b607f2827ec4affc164da967b327b1533252d57018`. | Self-test emitted direct-result and JSON/exit failures for `prose-mention`, `fenced-import-mention`, and `inline-import-mention`; `6 failure(s) over 89 assertions`, exit 1. Counter printed `1 of 8`; `.04` counted, `.07` not counted (`prose-mention expect FAIL, saw exit 0, PASS`), exit 1. **HOLDS**; killed by both detectors. Severity: none. |
| Treat imports inside code fences as real | Self-test `fenced-import-mention` expects FAIL. Mutation commit `97b477cb02132a83f747228c2fef69662a75a89f`, SHA-256 `cbebb035f8f4d139ca59386f5fca153f7a947100cffd6f6630de391c282e5079`. | Self-test emitted `self-test FAIL: fenced-import-mention direct result` and `... JSON and exit contract`; `2 failure(s) over 89 assertions`, exit 1 — killed. Counter printed `2 of 8`, both boxes counted, exit 0 — survived. **HOLDS** for self-test; **low** counter-coverage gap (no fenced-import case). |

Commands for every mutated row were `python3 -B verifiers/verify_alwayson.py --self-test` and `python3 -B verifiers/check_alwayson_boxes.py --rev <mutation-commit> --repo .`; exit codes and observed output are recorded above. No baseline failure occurred.

## Restoration evidence

After each mutation, copied the saved pristine instrument bytes back and made a local path-limited restoration commit. Restoration commits in order: `a43f7bb7eb91c5e4651491df7d16378a1322297c`, `c4bf7f0c7eed29ed10716d827226365a47f8159d`, `bc802f885255983215a4b19e54a0354a4dbb6707`, `46babafe09be6b84118edd37ceeff3ebcc3ebd07`, `e2a2e713e12aa06790f64df97856e0697a7b9b4f`, `72b73b604dc40ddaaa61cc37b09aea2165ae9320`. On every restoration, `sha256sum verifiers/verify_alwayson.py W2MutAlwaysOn07.pristine.py` printed the same `e4a8b3f230bb5c467798b6cb8bf31b420069d972844315dc4a85f243d9adc890` hash for both files.

Both detectors were rerun after every restoration commit: self-test printed `0 failure(s) over 89 assertions`, exit 0; the counter printed `2 of 8`, `.04` and `.07` each counted `6 of 6 cases as pinned`, exit 0. The final restored local revision is `72b73b604dc40ddaaa61cc37b09aea2165ae9320`; its instrument bytes match pristine exactly.
