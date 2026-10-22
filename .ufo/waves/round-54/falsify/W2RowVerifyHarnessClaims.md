Result: HOLDS — every cell of the `verifiers/verify_harness_claims.py` registry row verified; entry command and `--self-test` both ran in the sandbox clone, all four declared exit codes are produced with the declared meanings, the pinned baseline is genuinely read as expected values, and the script writes nothing.

Row under attack (SKILL.md `## Gate registry`, line 461 at bf65974, line 475 at tip 58db81c; `diff` of the two cells is empty — identical text):

```
| `verifiers/verify_harness_claims.py` | gate | `python3 -B verifiers/verify_harness_claims.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/baseline.json` | none | kotoba |
```

Script blob 48030f9 and baseline blob 1a71a4e are identical at bf65974 and 58db81c (`git diff --stat` empty), so the line numbers cited below hold at both revisions. Sandbox clone: /fast/scratch/hyaku/kotoba-r54/W2RowVerifyHarnessClaims @ 58db81c.

## Cell-by-cell verdicts

**Name — HOLDS.** `verifiers/verify_harness_claims.py` is a real `.py` blob directly under `verifiers/` (git ls-tree at bf65974, mode 100755); not a phantom.

**Kind `gate` — HOLDS.** The script compares live host state against a pinned baseline and fails on disagreement: `evaluate()` returns verdicts PASS/DRIFT/OBSERVE (verify_harness_claims.py:556-580) and main exits `1 if drift else 0` (line 695-698). That is a clean/failed verdict on repository-asserted truth, not a report-only probe. Row also satisfies the counter's gate requirements `0=clean` and `1=failed`.

**Entry command `python3 -B verifiers/verify_harness_claims.py` — HOLDS.** Ran in the sandbox, exit 1 (a real verdict on today's host, not an evaluation failure), ~8 s, read-only (sqlite opened `mode=ro`, line 286; no other writes — grep for write/open/mkdir/shutil/tempfile finds only read paths at lines 286, 297, 398, 460 and the stdout `print` at 667). Command and tail output:

```
$ python3 -B verifiers/verify_harness_claims.py
omp      template=c1f03c8e248eb40e… (273 B)  db_rows=17  offered=11  keys_reproduced=7  misses=4
         newest catalogue 2026-10-22T21:56:00.122Z (7/10 lines from cache, 6192 session files scanned)
opencode init_count_max=0  rescan_skills_max=3  names+builtin=12  <available_skills>=0  skill_perm=0/0
DRIFT   omp.db.rows: observed=17 expected=14            (5 more DRIFT lines omitted)
21/28 checks pass; DRIFT: omp.db.rows, omp.offered.skills, omp.cache.misses, omp.catalogue.total, omp.catalogue.missing_names, omp.cache.verified_skills, oc.roots.names_plus_builtin
EXIT=1
```

The drift is host state legitimately ahead of the 2026-10-14 baseline (11 skills offered vs 7 pinned, catalogue total 10 vs 7) — the gate doing its job, not a row defect.

**Self-test `--self-test` — HOLDS.** Real self-test, not a nested call or usage text: `args.self_test` dispatches to `self_test()` at lines 636-637, which falsifies the script's own model of `H7s` preview truncation and YAML chomping over 10 assertions (lines 583-619). Ran in the sandbox:

```
$ python3 -B verifiers/verify_harness_claims.py --self-test
self-test: 0 failure(s) over 10 assertions
EXIT=0
```

The flag literally occurs in the file (line 625, `ap.add_argument("--self-test", …)`), satisfying the counter's substring check for the right reason — it is a first-class argparse flag.

**Verdict map `0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate` — HOLDS.** Every declared code is produced with the declared meaning, and no produced code is missing:

- `0` (clean): line 698 `return 1 if drift else 0` — all checks agree with baseline. Docstring line 29 agrees.
- `1` (failed): line 698 — any DRIFT verdict (line 695 collects them). Observed live this run: exit 1 with 7 DRIFT checks.
- `2` (could-not-evaluate): lines 642-647 — `Inconclusive` (missing omp binary / db / opencode log, raised at lines 282, 284, 459) and `sqlite3.Error`/`OSError` both print `INCONCLUSIVE:` and return 2.
- `3` (could-not-evaluate): lines 692-694 — `baseline is None` (no `verifiers/baseline.json` at `--baseline`, or `--no-baseline`) prints `no baseline — observations above only (exit 3)` and returns 3. Under the allowed classes (clean/failed/could-not-evaluate) this is the honest label: the script observed but could not compare, so it cannot certify clean and nothing asserted failed. Docstring line 30-31 agrees.
- Code twice / code missing: none — `sys.exit(main())` (line 702) returns exactly {0,1,2,3}; the self-test path returns only {0,1} (line 619), both already mapped; argparse usage errors exit 2, already declared.

**Pinned values `verifiers/baseline.json` — HOLDS.** The file exists at bf65974 (`git cat-file -e` → exit 0; blob 1a71a4e). The script reads it through `--baseline` default `BASELINE = Path(__file__).resolve().parent / "baseline.json"` (line 58 → `verifiers/baseline.json`), loads it at line 653, and uses `baseline["checks"][cid]["expect"]` as the expected values in `evaluate` (lines 570-575: `equal`/`zero` → equality, `positive`/`at_least` → `value >= want`). Confirmed the file carries the expected structure: top-level keys `as_of, checks, host, measured_against, notes`, 28 check entries each with `expect` + `mode` (e.g. `omp.elf.template_sha256.expect = c1f03c8e…`). The run above demonstrably compared against these values (observed=17 vs expected=14).

**Write scope `none` — HOLDS.** No repo or filesystem writes anywhere: sqlite connection is URI `file:…?mode=ro` (line 286); all other file access is `read_text`/`open` for reading (lines 297, 398, 460, 479, 505-506, 512) or existence checks (`is_file`, `is_dir`, `exists`). `__pycache__` emission is suppressed by the `-B` flag in the entry command; even without `-B` it is bytecode cache, not lane content. Baseline updates are explicitly manual per the docstring (lines 33-36: human re-runs `--json` and edits `verifiers/baseline.json` by hand).

**Owner `kotoba` — HOLDS.** Matches the counter's pinned `OWNER = "kotoba"` (check_gate_registry.py:65).

## Residual risks (not breaks)

1. Uncaught exceptions exit 1 via `sys.exit` traceback, which the map would label `failed` rather than `could-not-evaluate`. Generic Python limitation shared by every lane verifier; only `Inconclusive`/`sqlite3.Error`/`OSError` are funneled to exit 2 (lines 642-647). No fix needed for this row; a reviewer could note it as a lane-wide verdict-map caveat.
2. `--json` mode returns 0 when the baseline is missing (line 670: `baseline is None or …`), where the non-JSON path returns 3. The declared entry command is non-JSON, so the row is unaffected, but anyone treating the map as describing `--json` would see `0=clean` on a run that judged nothing. Flagging for a later round; the row text as written is correct for its declared command.
3. The gate currently FAILS (exit 1) against live host state — expected drift since the 2026-10-14 baseline, per its design. The registry row makes no claim that the gate passes today; the verdict map is about meaning, not current status. No defect.

## Proposed corrected row

None — no cell breaks; row stands as landed at bf65974.

## Environment / tooling

- Sandbox: `git clone` of the lane to `/fast/scratch/hyaku/kotoba-r54/W2RowVerifyHarnessClaims`, checkout 58db81c (confirmed by `git log --oneline -3`).
- No installs performed; `python3` (system), `git`, `grep`, `diff` only.
- No network use; no paid model calls; no lane files mutated (all writes confined to this report path).
