Result: DONE — added the counter's own isolated `--self-test` and delivered its sandbox diff and retained run evidence.

Changed/delivered: sandbox clone `verifiers/check_opencode_repin.py`; patch `.ufo/waves/round-54/build/RegCheckOpencodeRepin.patch`; this report. No lane implementation file was edited.

| `verifiers/check_opencode_repin.py` | gate | `python3 -B verifiers/check_opencode_repin.py --rev REV` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/surfaces-baseline.json`, `verifiers/baseline.json`, `corpus/knowledge/instruction-surface-census-round13.md` | temporary trees/fixtures under `$TMPDIR` (removed) | kotoba |

Evidence by cell:

- **Name:** source `verifiers/check_opencode_repin.py:1-2`.
- **Kind / verdict map:** return 0 iff every pinned check passes, otherwise 1 (`:251-253`); return 2 if evaluation raises one of the handled errors or required scripts are absent (`:212-216, 243-246`). `argparse` usage errors also exit 2; help exits 0. No defined code 3. The script can fail and 1 means failed, so this is a gate.
- **Entry command:** help before the change exited 0 and showed `check_opencode_repin.py [-h] --rev REV [--repo REPO]`; `--repo` defaults to the script's repository (`:195-201`). The new usage is in `:41-45`; `--rev` remains required for normal runs (`:204-205`).
- **Self-test:** the target now declares and dispatches its own `--self-test` (`:43, 199-203`). It builds an isolated temporary git repository, runs a retained-class world and a retired-class world, and asserts each exit code and stable finding (`:100-187`). It does not use host binaries; child responses are fixtures generated in that temporary repository.
- **Pinned values:** the target reads the frozen baseline at `BASE_REV:verifiers/surfaces-baseline.json`, compares it to the measured revision's baseline, then runs the surface and pin verifiers (`:53-56, 208-232`). `verify_surfaces.py` checks its baseline against `corpus/knowledge/instruction-surface-census-round13.md` (`verify_surfaces.py:71-75, 167, 1789-1790, 1813-1817`); `check_substrate_pins.py` reads `verifiers/baseline.json` (`check_substrate_pins.py:2, 302-319`; its measured pins are at `baseline.json:4-11`). The counts and floor are in-file (`check_opencode_repin.py:53-56`).
- **Write scope:** normal evaluation extracts the measured tree under `TemporaryDirectory` (`:209-211`); the own self-test writes its local fixture repo under `TemporaryDirectory` (`:100-152`). Both are removed at exit. All recorded runs set `TMPDIR` inside the sandbox clone.
- **Owner:** `kotoba`, per the requested owner and registry rule (`check_gate_registry.py:65`).

Self-test evidence:

- Final command: `TMPDIR="$PWD/.repin-tmp-selftest" python3 -B verifiers/check_opencode_repin.py --self-test` — exit 0; last line `0 failure(s) over 2 assertions`.
- Its two assertions cover `retained class is clean` (exit 0, 7/7 PASS, 1/1 kept) and `retired class is failed with stable finding` (exit 1, 6/7 PASS, `opencode_extract FAIL`, 0/1 kept), checked against exact expected output lines (`:164-185`).
- Two initial fixture attempts failed and were corrected: first exit 1 with `UnboundLocalError` at `BASE_REV` (fixed by declaring/restoring the global); second exit 1 with `git archive` rejecting missing `corpus` pathspec (fixed by adding a tracked fixture file). Final run above passed.

Normal-run stability evidence (host-read-only; 0 network calls observed; 14.96 s before and 14.80 s after):

- Before: `TMPDIR="$PWD/.repin-tmp-before" python3 -B verifiers/check_opencode_repin.py --rev 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --repo "$PWD"` — exit 0.
- After: `TMPDIR="$PWD/.repin-tmp-final" python3 -B verifiers/check_opencode_repin.py --rev 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --repo "$PWD"` — exit 0. Output identical to before:
  `opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 175 assertions`
  `substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032`
  The run reads installed opencode/omp binaries (`check_opencode_repin.py:38-40`); temp output stayed under the clone and was removed.

Documentation notes:

- The pre-integration clone's SKILL.md had no `## Gate registry` row and `verifiers/README.md` had no reference to this script; searches for `check_opencode_repin`, `opencode re-pin`, `opencode repin`, and `repin` found no matches. This report supplies the row to paste once the patch lands.
- `SELFTEST_FLOOR = 129` is explicitly pinned to `floors-registry.json` at `BASE_REV` (`:53-56`). The current registry says 175 (`floors-registry.json:41-43`); `git show e78dff667237fba2e3cf9eccb802eff5bc9ea302:verifiers/floors-registry.json` showed 129. Historical pin is consistent; the target does not read the current floor file.

Risk: the isolated self-test uses fixture child scripts to provide deterministic child-verifier responses; it covers the counter's aggregation and verdict mapping, not the child verifiers' implementation. The normal run provides separate live-host integration evidence.