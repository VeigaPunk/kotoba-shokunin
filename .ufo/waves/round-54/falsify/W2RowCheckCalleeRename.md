Result: HOLDS — every cell of the `check_callee_rename.py` registry row is accurate; no cell breaks.

# Scope

Attack the C2 `## Gate registry` row landed at `bf65974c` (SKILL.md:444 there; SKILL.md:458 at tip `58db81c`):

```
| `verifiers/check_callee_rename.py` | gate | `python3 -B verifiers/check_callee_rename.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | temp dirs under `$TMPDIR` (removed) | kotoba |
```

`git diff bf65974c..58db81c -- verifiers/check_callee_rename.py` is empty and the row text is byte-identical at the two revisions, so attacks at tip are attacks on the landed row. All executions ran in sandbox clone `/fast/scratch/hyaku/kotoba-r54/KotobaR54.W2RowCheckCalleeRename` @ `58db81c`. Line numbers cite the script at `58db81c` (293 lines).

# Cell-by-cell verdicts

## Name — HOLDS

`verifiers/check_callee_rename.py` is a blob directly under `verifiers/` (it executed; `check_gate_registry.py --rev 58db81c` prints `verifiers/check_callee_rename.py OK`, part of `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0).

## Kind `gate` — HOLDS

Per PROTOCOL.md § Gate standard, a gate is a committed re-runnable verdict script that compares against repo-persisted expected values and can fail. This script can fail: `main` returns `0 if robust == len(CASES) else 1` (line 289), and its own self-test demonstrates the failure mode — the injected `check_no_uncovered_class` suppression mutant produces `exit=1` (line ~200-211; observed output `PASS self-test non-robust case: strings-omp-clean.txt exit=1`). It compares measured gate output against pinned fixtures, a pinned planted finding (`PLANT_ID = "omp:rnplant/RNPLANT.md"`, line 87), and a pinned callee list — not a passive probe. `gate` is the right kind, and erratum 2's guard (row says `gate`, declared flag exits 0 in sandbox) is satisfied.

## Entry command `python3 -B verifiers/check_callee_rename.py --rev <rev>` — HOLDS

`--rev` is a declared mutually-exclusive source argument (line 225; help at line 225). Ran verbatim in the clone:

```
$ python3 -B verifiers/check_callee_rename.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6
strings-omp-clean.txt        control=[0, True] renamed=[0, True] planted=[1, True] robust=True ...
strings-omp-newcallees.txt   control=[0, True] renamed=[0, True] planted=[1, True] robust=True ...
strings-omp-18.12.5.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True ...
strings-omp-18.12.6.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True ...
callee-rename robust 4 of 4 fixtures
ENTRY-EXIT=0   (real 0m0.899s)
```

Read-only over the clone (`git status --porcelain` empty after all runs), no network, ~1s.

## Verdict map `0=clean, 1=failed, 2=could-not-evaluate` — HOLDS

- `0`: produced at line 289 (`return 0 if robust == len(CASES)`); observed live, `ENTRY-EXIT=0` above.
- `1=failed`: produced at line 289 when robust < 4, and at line 219 for failed self-test assertions. Observed: the self-test's non-robust case asserts `code == 1` against a mutant gate and passed (`... exit=1 finding=self-test injected suppression`).
- `2=could-not-evaluate`: produced at lines 215 (self-test exception path) and 278 (main exception path over `RuntimeError | TimeoutExpired | OSError`). Observed live:
  ```
  $ python3 -B verifiers/check_callee_rename.py --rev 0000000000000000000000000000000000000000
  could-not-evaluate: git show 0000…0000:verifiers/verify_surfaces.py failed: fatal: path 'verifiers/verify_surfaces.py' exists on disk, but not in '0000…0000'
  BADREV-EXIT=2
  ```
- No produced code is missing from the map: `sys.exit(main())` (line 293) returns only 0/1/2; the only other nonzero exit is argparse's `ap.error` (line 233) → exit 2, which falls under the declared `2=could-not-evaluate` class per PROTOCOL's default rule anyway.

Residual (not a row defect): exceptions outside main's catch tuple (e.g. `UnicodeDecodeError`, `StopIteration`, `KeyError`, `ValueError` in `main`) propagate as traceback → process exit 1, a declared code, so the map stays truthful though such a failure is arguably could-not-evaluate in spirit. `KeyboardInterrupt` → 130 is undeclared; per the Protocol bullet an undeclared nonzero code reads `could-not-evaluate`, which is right.

## Self-test cell `` `--self-test` `` — HOLDS

- Real flag spelled exactly: `src.add_argument("--self-test", action="store_true")` (line 227), dispatched at line 231-234 to `self_test(args.seed)` (line 145). The flag text occurs literally in the file — not a comment-only or borrowed flag.
- It is the script's own self-test, not usage text: it fetches the gate source at pinned `SELF_TEST_REV` (line 65, `git_show(SELF_TEST_REV, GATE)`, line 172), runs `main()` in-process over an isolated `TemporaryDirectory` copy (lines 170, 167), then runs a mutation-injection case that replaces `check_no_uncovered_class` with a suppression stub (lines ~190-197) — exercising both the exit-0 and exit-1 verdicts plus stable finding-ids (`omp:rnplant/RNPLANT.md`, `self-test injected suppression`), matching PROTOCOL § Self-test.
- Ran:
  ```
  $ python3 -B verifiers/check_callee_rename.py --self-test
  PASS self-test robust case: strings-omp-clean.txt exit=0 finding=omp:rnplant/RNPLANT.md
  PASS self-test non-robust case: strings-omp-clean.txt exit=1 finding=self-test injected suppression
  self-test: 0 failure(s) over 2 assertions
  SELFTEST-EXIT=0   (real 0m1.352s)
  ```
- `--seed 99 --self-test` also exits 0 (`self-test: 0 failure(s) over 2 assertions`), so no fresh-name hardcoding.

## Pinned values `in-file` — HOLDS (true)

Every expected value is a module constant in the script: `FIXTURE_REV` (line 64), `SELF_TEST_REV` (line 65), `FIXTURE_DIR`/`GATE` (66-67), `CASES` pairings (69-74), `OC_FIXTURE` (76), `BASE_CALLEES` (77-78), `GENERIC_CALL_RE` (80-83), `PLANT_PAIR`/`PLANT_ID` (86-87), `CHECKS` (88). Fixture bytes are read read-only from pinned rev `c8579a4c` via `git show` (lines 94-100, 240-242). No external expected-values file exists or is needed; `in-file` is accurate.

## Write scope `temp dirs under $TMPDIR (removed)` — HOLDS

Every write happens inside `tempfile.TemporaryDirectory()` contexts: self-test at line 170 (`root/verifiers/verify_surfaces.py` copies, mutant copy), main at line 237 (fixture copies, `A-*`/`B-*` renamed+planted strings, gate copy). `TemporaryDirectory` removes the tree on exit. Subprocesses are `git -C LANE show` (read-only, lines 94-97) and `sys.executable -B` gate runs (lines 130-135) pointed at the temp `--repo`; `-B` suppresses `__pycache__`. Observed: `git status --porcelain` in the clone empty after entry+self-test+bad-rev runs; `find /tmp -maxdepth 1 -name 'tmp*' -newermt '-10 minutes'` returned nothing — temp dirs removed, nothing outside the clone written, nothing inside it either.

## Owner `kotoba` — HOLDS

Matches the counter's pinned `OWNER = "kotoba"` (check_gate_registry.py) and every sibling row.

# Summary

| Cell | Verdict |
|---|---|
| name | HOLDS |
| kind (`gate`) | HOLDS |
| entry command | HOLDS (`robust 4 of 4`, exit 0, 0.9s) |
| verdict map | HOLDS (0,1,2 all produced with declared meaning; no missing code) |
| self-test | HOLDS (`--self-test`, exit 0, asserts exit codes + finding-ids incl. mutant→1) |
| pinned values | HOLDS (`in-file` true) |
| write scope | HOLDS (temp dirs under $TMPDIR, removed; clone untouched) |
| owner | HOLDS |

No corrected row text needed — the landed row is accurate as written.

Tooling: no installs. Evidence commands all ran with the exits shown above in the named sandbox clone; nothing was run in or written to the lane.
