Result: DONE — verified the `verify_alwayson.py` registry row against its source, help, and self-test in the isolated 7ad05d342d7505ab674a5ebcf5ac1106b2f45c39 clone.

| `verifiers/verify_alwayson.py` | gate | `python3 -B verifiers/verify_alwayson.py --check alwayson.04 --target <dir>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |

### Evidence by cell

- **Name:** `verifiers/verify_alwayson.py:1-2,57-64` identifies the instrument and its two box IDs.
- **Kind:** `verifiers/verify_alwayson.py:4-8,284-296,367-384,654-664` returns PASS/FAIL/ERROR from rule checks, so it is a gate, not a probe.
- **Entry command:** `SKILL.md:360-368` says run `--check alwayson.04` and `--check alwayson.07` one at a time. `verifiers/verify_alwayson.py:624-653` defines those choices and requires `--target`; the row uses the shortest documented form for one box. `--json` is optional (`:632-633`).
- **Verdict map:** `0=clean` for PASS (`verifiers/verify_alwayson.py:654-656`); `1=failed` for FAIL, self-test failures, or incomplete box proof (`:555,605-614`); `2=could-not-evaluate` for input errors, unreadable proof inputs, or argparse usage errors (`:657-659,560-565,573-583,641-653`). These are all source-defined non-help exit codes; `sys.exit(main())` is at `:667-668`.
- **Self-test:** exact flag `--self-test` is in `verifiers/verify_alwayson.py:7,620-621`. In the clone, `python3 -B verifiers/verify_alwayson.py --self-test` exited **0**; last output line: `0 failure(s) over 89 assertions`. `python3 -B verifiers/verify_alwayson.py --help` exited **0**; last help line: `  --json                machine-readable output`.
- **Pinned values:** `in-file` is accurate: `PINNED_BOX_SHA` is in `verifiers/verify_alwayson.py:67-70`, and expected fixture statuses/paths are `CASE_EXPECTATIONS` at `:406-438`. The self-test reads the committed fixture map `verifiers/fixtures/alwayson/manifest.json:1-31` (`:441-458`) and checks fixture results against those constants (`:493-510`). `--box-proof` also compares the in-file hashes with `verifiers/checklist-baseline.json:223-244` and the live checklist in `SKILL.md` (`:573-603`).
- **Write scope:** none to the filesystem. The source reads targets and fixtures (`verifiers/verify_alwayson.py:202-239,441-458,560-605`) and states it uses no network (`:40-42`). Self-test temporarily changes only process-local `MAX_FILE_BYTES`, then restores it in `:530-547`; box-proof only inserts into process-local `sys.path` (`:575-578`). No host-only inputs were needed for the self-test. No slow or persistent mutation was observed.
- **Owner:** the C2 counter pins owner `kotoba` (`verifiers/check_gate_registry.py:59-67`). Its row rules require gates to declare `0=clean`, `1=failed`, a literal self-test flag, and non-`none` pinned values (`:20-36`).

### Documentation comparison

- `SKILL.md:360-368` agrees with the script's two check choices and one-box-at-a-time invocation. At this pre-integration tip, a `## Gate registry` row is not present; the round-54 plan expects C2 to add it.
- `verifiers/README.md:1-6` points registry rows to `SKILL.md`, but a repository search for `verify_alwayson.py`, `alwayson.04`, and `alwayson.07` found no README match. This is an omission, not a conflicting CLI or verdict claim.
- `verifiers/floors-registry.json:53-56` records `alwayson` with floor 89 and the correct script path. `verifiers/check_assertion_floors.py:178-179` defines that floor as the self-test assertion-count floor; the observed count was 89. No mismatch found.

### Execution scope

Clone command: `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r54/RegVerifyAlwayson && git -C /fast/scratch/hyaku/kotoba-r54/RegVerifyAlwayson checkout -q 7ad05d342d7505ab674a5ebcf5ac1106b2f45c39` — completed with exit 0 and no output. Help and self-test above were run in that clone; no lane code was executed or changed.
