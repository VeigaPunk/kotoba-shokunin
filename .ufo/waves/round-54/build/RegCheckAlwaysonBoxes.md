Result: DONE — Added an isolated `--self-test`; it asserts counted and not-counted results, while the normal counting line remains unchanged.

Registry row for SKILL.md:

| `verifiers/check_alwayson_boxes.py` | gate | `python3 -B verifiers/check_alwayson_boxes.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | Temporary archive/cases and self-test Git repos (removed) | kotoba |

Patch artifact: `.ufo/waves/round-54/build/RegCheckAlwaysonBoxes.patch` (git diff from sandbox clone `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`). The lane verifier itself was not edited.

Evidence:

- **Entry / self-test:** `python3 -B verifiers/check_alwayson_boxes.py --help` in the clone exited 0 and listed `--self-test  exercise isolated fixtures`. Parser and branch are at `verifiers/check_alwayson_boxes.py:199-210`; `--rev` remains required for normal runs.
- **Self-test behavior:** `verifiers/check_alwayson_boxes.py:96-170` creates two temporary local Git repos, copies the current delegated verifier into them, and invokes the counter against them. It asserts exit 0 plus both counted findings, then exit 1 plus one counted finding and the stable missing-delegate finding; expected output strings are in-file. The only source read outside the temp repos is `LANE/verifiers/verify_alwayson.py:141-143`; no live-tree write or network call is used.
- **Self-test command/output:** `TMPDIR="$PWD/.tmp" python3 -B verifiers/check_alwayson_boxes.py --self-test` from the sandbox clone — exit 0; output: `self-test PASS: counted box exit 0; missing delegate exit 1`.
- **Before patch:** `TMPDIR="$PWD/.tmp" python3 -B verifiers/check_alwayson_boxes.py --rev 422ffd10` — exit 0. Counting line: `always-on boxes executed and discriminating 2 of 8`.
- **After patch:** same command — exit 0 and the identical counting line: `always-on boxes executed and discriminating 2 of 8`. Both runs also printed `alwayson.04: counted (6 of 6 cases as pinned)` and `alwayson.07: counted (6 of 6 cases as pinned)`.
- **Verdict map:** 0 iff both pinned boxes count, 1 otherwise (`verifiers/check_alwayson_boxes.py:248-250`); 2 on caught evaluation errors (`:245-247`). The self-test explicitly exercises 0 and 1; the existing `--rev` path remains unchanged.
- **Pinned values:** `in-file`; `RULES_A`, `RULES_B`, and `CASES` carry fixture data and expected statuses (`:61-88`). The revision's `verifiers/checklist-baseline.json` is a map input (`:213`), not the source of expected case statuses.
- **Write scope:** normal measurement extracts the revision and plants cases in `TemporaryDirectory` (`:214-219,233-236`); self-test Git repos and nested runs are under its own `TemporaryDirectory` (`:116-158`). The context managers remove these temporary trees.

Documentation note at the frozen tip: `SKILL.md:365-368` and `verifiers/floors-registry.json:53-56` name `verifiers/verify_alwayson.py`, the delegated box checker, not this counter. `verifiers/README.md:1-6` places descriptions there and registry rows in SKILL.md; an exact search found no counter mention in SKILL.md or README. This patch supplies the self-test needed for its gate row; the row itself is included above for integration.