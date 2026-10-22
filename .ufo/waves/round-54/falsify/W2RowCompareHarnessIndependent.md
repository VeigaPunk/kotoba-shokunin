Result: HOLDS — the registry row for `verifiers/compare_harness_independent.py` (SKILL.md § Gate registry) is accurate cell by cell; entry command ran and returned a real verdict (exit 1, six honest disagreements), self-test is the script's own and passes 330/330, all four declared exit codes are produced with the declared meanings and no produced code is undeclared, both pinned paths are read as expected values, and the write-scope cell covers every write the script performs.

Scope: row at SKILL.md:469 at tip 58db81c4 (identical text at landed commit bf65974c:455 — verified via `git show <rev>:SKILL.md` in the sandbox clone). Counter rules read from `verifiers/check_gate_registry.py:3-44` (per its own docstring, "declared code really produced" and "gate vs probe" are explicitly reviewer judgment, Q31 — that is this attack).

Sandbox: `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r54/W2RowCompareHarnessIndependent && git checkout -q 58db81c4…`; all runs in the clone, read-only in the lane.

## Cell-by-cell verdict

### Name — HOLDS
`verifiers/compare_harness_independent.py` exists at the revision (`ls-tree` blob, 126784 bytes). Entry-command cell contains the literal path text, satisfying the counter rule (check_gate_registry.py:25).

### Kind: `gate` — HOLDS
The script produces a pass/fail verdict over the repository state: it runs both instruments, joins on check id, and its docstring states the verdict contract (`verifiers/compare_harness_independent.py:117-120`). It reads inputs and emits a judgment — a gate, not a probe. Verified by exercise: the entry run produced verdict `exit 1 — disagreements: …` (see below).

### Entry command: `python3 -B verifiers/compare_harness_independent.py` — HOLDS
Ran in the sandbox clone, read-only eligible: normal path writes nothing except optional `--report`/`--receipt` targets (not passed) and self-test temp dirs (not reached without the flag). No network. Command:

```
$ timeout 590 python3 -B verifiers/compare_harness_independent.py   # cwd = clone root
EXIT=1   (wall time 86.51 s, under the 10-min bound)
agreement: 18/24 (mode-aware protocol headline; 28 live checks, 4 scoped out by the independent instrument)
columns: protocol 18/24; strict 14/24; adjudicated rows: 4; un-adjudicated modes: 0
disagree: 6; uncovered: 0; unknown: 0; provisional (unlanded-based agreement): 0; scoped-out: 4
live: /usr/bin/python3 verifiers/verify_harness_claims.py --json -> exit 1, 28 checks, 21 PASS
independent: /usr/bin/python3 …/verifiers/verify_harness_independent.py --json -> exit 0, 28 checks
verdict: exit 1 — disagreements: oc.roots.names_plus_builtin (expected 10, observed 12),
  omp.cache.misses (3 vs 4), omp.cache.verified_skills (7 vs 11), omp.descriptions.over_cliff (10 vs 11),
  omp.descriptions.unmodelled (3 vs 0), omp.offered.skills (10 vs 11)
```

The non-zero exit is the gate doing its job on this host (the source-blind re-derivation's frozen numbers predate host config changes), not a row defect: exit 1 maps to `failed` and the six named disagreements are substantive join output. After the run, `git status --porcelain` in the clone printed 0 lines — no residual writes in the repo tree.

### Verdict map: `0=clean, 1=failed, 2=could-not-evaluate, 3=failed` — HOLDS
Gate requirements met (declares `0=clean`, `1=failed`, no code twice, all classes in {clean, failed, could-not-evaluate}). Semantic check — every declared code is produced with that meaning:

- **0** = all checks agree, both instruments green: `decide_exit` returns `(0, "all checks agree, both instruments green")` only after disagreement, un-adjudicated, provisional and instrument-failure branches are exhausted — `compare_harness_independent.py:1234`. `main` returns `meta["exit"]` (lines 2585, 2591).
- **1** = failed: protocol disagreements (1215-1219), un-adjudicated modes (1210-1213), agreement resting on unlanded derivations (1220-1223); `--self-test` failures (2559: `return 1 if self_test() else 0`); uncaught exceptions also exit 1.
- **2** = could-not-evaluate: every `raise CompareError` (≈60 sites, lines 305-2447 — unreadable/unparseable payloads, channel splits, scope-file errors, probe failures, instrument-with-no-stdout) is caught in `main` and returns 2 (2563-2568); `OSError`/`SubprocessError`/`ValueError` likewise (2566-2568, so a `TimeoutExpired` from `run_cmd`, line 692-694 with `timeout=RUN_TIMEOUT_S=300`, is 2); count shortfall and coverage gaps are 2 (1201-1209); unwritable receipt path is 2 (2574-2576). Argparse usage errors also exit 2 — correctly classed.
- **3** = failed (joined but an instrument reported failure): `decide_exit` returns `(3, "all checks agree but live exit N / independent exit N / live non-PASS: …")` at 1224-1233, reached only when every check agreed — correctly `failed`, not `clean`.

No produced code is missing from the map: the script's own returns are only 0/1/2/3 (grep for `sys.exit`/`SystemExit`/`os._exit`/`parser.error` finds only `sys.exit(main())` at 2595; the `sys.exit(1)` at 2032 is a string literal inside a self-test fixture body, not executed code). Signals/KeyboardInterrupt (130+) fall outside the map — covered by the table preamble's "an undeclared nonzero code reads as could-not-evaluate" (SKILL.md:450).

Self-test directly asserts all four codes in-process: exit 0 (1875-1876), exit 1 disagreement and un-adjudicated (1877-1879, 1904-1906), exit 2 uncovered/unknown/count (1880-1885, 1888-1889), exit 3 non-PASS verdict (1886-1887). Fixture `case.json` `expect.exit` values exercised end-to-end: 4× exit 0, 36× exit 2.

### Self-test: `--self-test` — HOLDS
`main` dispatches `--self-test` to the script's own `self_test()` (2558-2559, defined 1726-2391) — in-process model assertions plus a fixture battery that invokes the driver itself on `verifiers/fixtures/compare-harness-independent` cases (1586-1622), plus $TMPDIR-staged instrument arms (2053+). Not a nested call into another script's self-test and not usage text. Ran:

```
$ timeout 590 python3 -B verifiers/compare_harness_independent.py --self-test
EXIT=0
…
self-test: 0 failure(s) over 330 assertions   (wall 3.32 s)
```

### Pinned values: `verifiers/harness-independent-scope.json`, `verifiers/fixtures/compare-harness-independent` — HOLDS
Both exist at the revision (`cat-file -e` would pass; visible in `ls verifiers/`). Both are read by the script as expected values:

- `verifiers/harness-independent-scope.json` is `DEFAULT_SCOPE` (137), loaded by `load_scope_file` (895-936) via `build_meta` (2457-2461): the committed scope-out set and `probe_contract` the payload under test is checked against — exactly "expected values" (docstring 81-86: "a scope-out must be committed, never self-declared"). The self-test's planted-control receipt also checks this file's sha256 (2293).
- `verifiers/fixtures/compare-harness-independent` is `FIXTURE_DIR` (1433), the pinned fixture corpus whose `case.json` `expect` blocks supply expected exit codes/named tokens for the self-test battery (1486-1635).

Grep over the file confirms no other committed path is read as an expectation: `DEFAULT_LIVE`/`DEFAULT_INDEPENDENT` (136-138) are instruments executed (they have their own rows pinning their own inputs), and probe targets are observed values recomputed from the substrate, not expectations. Docstring (1277) confirms no baseline file is read.

### Write scope: ``--report`/`--receipt` targets; temp dirs` — HOLDS
Complete inventory of writes (grep `write_text|\.write(|TemporaryDirectory|mkdtemp`):
- Normal path: `Path(args.receipt).write_text` (2573), `Path(args.report).write_text` (2582, 2589) — only under caller-named flags. Matches "`--report`/`--receipt` targets".
- Self-test only: `tempfile.TemporaryDirectory()` under `$TMPDIR` (2053) and two temp dirs **inside `verifiers/fixtures/compare-harness-independent`** with prefixes `.scope-cwd-`/`.fixture-` (1499, 1576) — all removed via `TemporaryDirectory` cleanup/`finally` (1615-1619). Matches "temp dirs".
- No other writes. `git status --porcelain` after both runs: empty.

Precision note (not a break): sibling rows name the temp-dir location (`under $TMPDIR`); this cell's bare "temp dirs" also covers the in-fixture `dir=FIXTURE_DIR` dirs, so it is accurate but less specific. Optional tightening: "`--report`/`--receipt` targets; self-test temp dirs (`$TMPDIR` and in-fixture, removed)".

### Owner: `kotoba` — HOLDS
Matches the pinned owner constant (check_gate_registry.py:65).

## Findings by severity

No defects. Residual risk / verification gaps:

- The 10-minute bound: entry run took 87 s here with both instruments green-ish on this host; a slower box or a wedged instrument could approach `RUN_TIMEOUT_S=300` × 2 = 600 s worst case. Not a row defect — runtime is environment-bound — noted for whoever re-runs.
- Verdict-map honesty: exit 3 is declared `failed`, and the code path shows it fires only when all checks agree but an instrument reported failure — a truthful failure class, consistent with the docstring (117-120).
- No install/tooling changes were needed (system python3, no packages).
- Sources consulted were all local; no network fetches performed for this row.
