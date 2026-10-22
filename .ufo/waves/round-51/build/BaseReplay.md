# BaseReplay — round-51 base column at 43ca0bf (falsify wave's no-harm reference)

**Result: BASE COLUMN MEASURED — 11 of 17 gates green at `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`; 6 red, every red attributed to a named cause (lane bytes or host state).** The falsify wave compares its head column against the table below. No gate is red for a scratch-shape reason in the final run; one gate (`g01`) was red only under an incomplete fleet shape and is green in the final run (finding F5).

Base commit: `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` ("round-50 verifier spot-check (integrator, hyaku): non-author admit/reject"), parent `2abd290`.

## Setup (reproduce before comparing)

- Scratch root `/fast/scratch/hyaku/kotoba-r51/build/BaseReplay/`; clone at `fleet/kotoba-shokunin` (`git clone` of the lane, `git checkout -q 43ca0bf…`; `rev-parse HEAD` confirmed).
- Fleet shape copied from `.ufo/waves/round-50/falsify/NoHarmGates.md` §Setup: `fleet/.ufo` and `fleet/PROTOCOL.md` are **copies**; every other fleet entry, **including every sibling lane directory** (`kasegi-shokunin`, `chousa-shokunin`, … `kaidoku-sh2`, `local`, `reports`, `write`), is a **symlink** to `/home/vgpnk/Projects/shokunin/`. The sibling-lane symlinks are required — see finding F5.
- All gates ran from the clone root with `python3 -B`. `check_sibling_census.py` reads the live fleet (`DEFAULT_FLEET = "/home/vgpnk/Projects/shokunin"`, `git show` only) — the same live fleet at base and head.
- Run window 2026-10-22T14:23:58Z–14:25:47Z. Python 3.14.8, git 2.56.0, `omp/18.12.6`. Logs: `logs/g01.log` … `logs/g17.log` (one per gate, `# cmd:` / `# exit_code:` headers). Shape-probe run archived at `logs-shape-no-siblings/`. No tool installed or upgraded; no web source opened; no git/jj write against the lane, the fleet root or any sibling repo.

## Table — command, exit code, summary line, cause of every red

| # | command (from the clone root) | rc | summary line | cause if red |
|---|---|---|---|---|
| 1 | `python3 -B verifiers/verify_skill_checklist.py --json` | 0 | `pass 11 fail 0 na 0` | — |
| 2 | `python3 -B verifiers/verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over 1851 assertions` | — |
| 3 | `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | 4 DRIFT: `tracked_files 70 vs 69`, `unindexed 1`, `report_total 45 vs 44`, `report_dead 2` | **lane bytes** (F1) |
| 4 | `python3 -B verifiers/verify_corpus_independent.py` | 1 | `DRIFT unindexed=1`, `DRIFT report_dead=2`, exit 1 (tracked 70 / report_total 45 are INFO) | **lane bytes** (F1) |
| 5 | `python3 -B verifiers/check_assertion_floors.py` | 0 | 11 PASS lines (harness 10, corpus_integrity 150, corpus_independent 91, surfaces 99, checklist 1851, pins 62, harness_independent 123, compare_harness_independent 330, floors_guard 150, dispatch_prompts 56, sibling_census 68 — all observed == floor) | — |
| 6 | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | 0 | `rows 20 verified 20` / `province rows 20 matched 20` | — |
| 7 | same command plus `--skill SKILL.md` | 0 | `skill description names 9 of 9 non-none lanes` / `skill description length 1019 of 1024` | — |
| 8 | `python3 -B verifiers/check_sibling_census.py --self-test` | 0 | `0 failure(s) over 68 assertions` | — |
| 9 | `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | 0 | `0 failure(s) over 56 assertions` | — |
| 10 | `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 | `boxes proven 2` | — |
| 11 | `python3 -B verifiers/verify_harness_independent.py --self-test` | 0 | `0 failure(s) over 123 assertions` | — |
| 12 | `python3 -B verifiers/compare_harness_independent.py --self-test` | 0 | `0 failure(s) over 330 assertions` | — |
| 13 | `python3 -B verifiers/verify_surfaces.py --json` | 1 | `pass 5 fail 2` — FAIL `surfaces.literal_present` (8 loader literals not verifiable) and `surfaces.no_uncovered_class` (0 of 8 loader classes extracted from the omp dump) | **host state** (F2) |
| 14 | `python3 -B verifiers/verify_harness_claims.py` | 1 | `21/28 checks pass; DRIFT: omp.db.rows, omp.offered.skills, omp.cache.misses, omp.catalogue.total, omp.catalogue.missing_names, omp.cache.verified_skills, oc.roots.names_plus_builtin` | **host state** (F2) |
| 15 | `python3 -B verifiers/check_substrate_pins.py` | 1 | `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` | **host state** (F2) |
| 16 | `bash verifiers/fault_injection_corpus.sh` | 1 | `verdict: FAILURES PRESENT` — 4 red rows: `fault-0-control FAIL-control-dirty`, `fault-f FAIL`, `fault-g FALSE-POSITIVE`, `fault-h FAIL`; the 6 must-fire rows are PASS | **lane bytes** (F3) |
| 17 | `python3 -B verifiers/box_proof_case_deletion.py --rev 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` | 0 | `killed 6 of 6` / `controls killed 2 of 2` / `na killed 1 of 1` | — |

## Findings

**F1 — rows 3, 4: `verify_corpus_integrity.py` is red at base because the closure-committed `corpus/lessons/round-50-verifier-spotcheck.md` has no index row in `corpus/README.md`. Confirmed, and it is not the only red check.**
- `unindexed_detail` at base is exactly `['corpus/lessons/round-50-verifier-spotcheck.md']`; `corpus/README.md` has index rows for the round-46/47/48/49 spot-checks but **no row for the round-50 spot-check** (last coverage-map row is line 73, `| Round-50 lessons |`).
- Causation proof: copying the clone and inserting **one** index row into the coverage map turns `corpus.index.unindexed` from DRIFT (1) into PASS (0) — everything else unchanged (`probe-index-row/`).
- The same closure commit also moved two other checks, so the D3 index row alone does **not** make rows 3/4 green. At the parent `2abd290` the gate reads `tracked_files 69 PASS`, `unindexed 0 PASS`, `report_total 44 PASS`, `report_dead 2 DRIFT`; at base it reads `70 DRIFT`, `1 DRIFT`, `45 DRIFT`, `2 DRIFT`. Decomposition of the base red:
  - `corpus.index.unindexed = 1` → the missing round-50 index row (the D3 item).
  - `corpus.index.tracked_files 70 vs 69` and `corpus.pointers.report_total 45 vs 44` → `verifiers/corpus-baseline.json` was not refreshed for that same commit (+1 tracked corpus file, +1 report pointer).
  - `corpus.pointers.report_dead = 2` → **older, independent**: `corpus/lessons/round-48-verifier-spotcheck.md:9` and `:23` carry repo-relative `.ufo/reports/round-48/kotoba.md`; the lane's `.ufo/reports/` stops at `round-45`, the report lives in the fleet repo. This one is already documented in `corpus/README.md:68`.
- Full repair set, measured: index row + baseline `tracked_files 69→70` + `report_total 44→45` leaves only `report_dead 2`; additionally rewriting the two round-48 pointers to the absolute fleet path gives **rc 0, all checks PASS** (`probe-full-repair/`).

**F2 — rows 13, 14, 15: host state, not lane bytes.** The installed omp is `omp/18.12.6`, sha256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`, mtime ns `1792625844615549837`; `verifiers/baseline.json` pins sha256 `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e` and mtime `2026-10-21T03:30:38.135013187-03:00` → row 15 `DRIFT 2/3`. Row 13's extractor reads the **live omp binary's** strings dump and finds 0 of 8 declared loader classes (the 18.12.6 callee allowlist no longer matches), which also makes `surfaces.literal_present` fail. Row 14 reads the **live** `~/.omp/agent/skill-descriptions.db` and `~/.omp/agent/sessions` (observed `db_rows=17`, `offered=11`, `catalogue.total=10` incl. `create-toolset`, `unreal-mcp`, `unreal-skill`) plus the live `~/.agents/skills` root (`names_plus_builtin=12`). These three reds are the C1 freshness target, not a base defect.

**F3 — row 16: the fault-injection harness is red at base for two independent lane-bytes reasons.**
- Three of the four red rows (`fault-0-control FAIL-control-dirty`, `fault-f FAIL`, `fault-g FALSE-POSITIVE`) are downstream of the base corpus being dirty: the harness's control world requires a pristine corpus, and at base the corpus carries `unindexed 1` and `report_dead 2`. Run at the parent `2abd290` the same three rows are red for the same reason (`report_dead 2` alone), so they predate round 50.
- `fault-h FAIL` is **independent of the dirt**: `verifiers/fault_injection_corpus.sh` asserts an absolute `report_pointers_quoted = 1`, while the corpus already carries one quoted pointer at base (measured `report_pointers_quoted = 1` at `2abd290` and at base). The planted (h) world therefore reports `quoted = 2` and the literal check fails. Rewriting the assertion as the relative `quoted == ctl_quoted + 1` on a repaired corpus gives **`verdict: ALL PASS`, rc 0** (`probe-h-assert/`). This is a stale absolute expectation in the harness itself, not listed in the round-51 D1–D7 set; it is offered to the L1 as an extra routable item.

**F4 — the C2-named counter present at base is green.** `verifiers/box_proof_case_deletion.py --rev 43ca0bf…` → rc 0, `killed 6 of 6`, `controls killed 2 of 2`, `na killed 1 of 1`. The plan's round-51 C2 counter (`verifiers/check_overlap_levers.py`) does not exist at base, so the head column's C2 number has no base counterpart in this table; row 17 is the base value of the round-50 C2 counter.

**F5 — fleet-shape sensitivity (the one trap for the falsify wave).** In a first run whose scratch fleet had **no sibling-lane symlinks**, row 1 was red (`governance.citation_resolves` FAIL: `../kasegi-shokunin/corpus/instruments/resolve.py` does not resolve from the scratch clone root; `pass 10 fail 1`). Adding the sibling-lane symlinks made it green (`pass 11 fail 0`). That red was a scratch-shape artifact, **not lane bytes**. Archived at `logs-shape-no-siblings/`. All other 16 gates are byte-identical between the two runs except row 16's temp-worlds path.

**F6 — the base column cannot see the lane's untracked files.** The live lane checkout carries untracked `plans/round-51.md`, `.ufo/waves/round-51/` and `.ufo/waves/round-50/build/DescDraft.md` (the D1 item). The clone at `43ca0bf` has none of them, and no verifier reads `.ufo/waves` at runtime (only comments and `checklist-baseline.json` prose), so the base column is unaffected — but any head column that reads untracked lane bytes would not be comparable.

**F7 — floors are equal to observed at base.** `check_assertion_floors.py` reports 11 instruments, every `observed == floor` (checklist 1851, dispatch 56, sibling_census 68, corpus_integrity 150, corpus_independent 91, surfaces 99, pins 62, harness_independent 123, compare_harness_independent 330, floors_guard 150, harness 10). Nothing is below its floor at base; a head column that lowers a floor would show here.

## Evidence (commands and exit codes, verbatim)

```
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin lane ; git -C lane checkout -q 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10   # rev-parse HEAD = 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10
bash run_gates.sh    # 17 gates, logs/g01.log … logs/g17.log   (run 2, full fleet shape)
  g01 rc=0  g02 rc=0  g03 rc=1  g04 rc=1  g05 rc=0  g06 rc=0  g07 rc=0  g08 rc=0  g09 rc=0
  g10 rc=0  g11 rc=0  g12 rc=0  g13 rc=1  g14 rc=1  g15 rc=1  g16 rc=1  g17 rc=0
python3 -B verifiers/verify_corpus_integrity.py --json        # in probe-index-row/  -> rc 1, unindexed PASS observed=0
python3 -B verifiers/verify_corpus_integrity.py --json        # in probe-parent/ (2abd290) -> rc 1, only report_dead DRIFT
python3 -B verifiers/verify_corpus_integrity.py --json        # in probe-full-repair/ -> rc 0, all checks PASS
bash verifiers/fault_injection_corpus.sh                      # in probe-full-repair/ -> rc 1, fault-h FAIL
bash verifiers/fault_injection_corpus.sh                      # in probe-h-assert/ -> rc 0, "verdict: ALL PASS"
bash verifiers/fault_injection_corpus.sh                      # in probe-parent/ (2abd290) -> rc 1, control/f/g/h red
sha256sum /home/vgpnk/.local/bin/omp                          # 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4 ; omp --version = omp/18.12.6
```
Run 1 (incomplete fleet shape, `logs-shape-no-siblings/`): identical except `g01 rc=1` and `g16`'s worlds path.

## Scope, and what I did not do

- I wrote only this report in the lane. Every probe and every mutation was in `/fast/scratch/hyaku/kotoba-r51/build/BaseReplay/` (`probe-index-row/`, `probe-parent/`, `probe-full-repair/`, `probe-h-assert/`, `probe-h-ctl-*/`, `probe-h-plant-*/`); the only git write was the throwaway commit inside `probe-full-repair/`.
- I did not repair anything in the lane: the index row (D3), the baseline refresh, the round-48 pointer repair and the fault-h assertion are all left to the L1's build wave, and F1/F3 are the measured effect sizes the falsify wave will compare against.
- Not run: nothing in the assignment was skipped. Checks outside the assignment (round-50's `--skill` arm absent-at-base row, the C1 counter at `542f515`) are out of scope for this seat and are not claimed here.
- Residual risk: rows 13–15 are red from host state at base and will be red at head unless the C1 re-pin lands; rows 6–8 read the live sibling fleet at run time, so a sibling commit landing during the falsify window can move them. Unrun checks are not passes.

Report: `.ufo/waves/round-51/build/BaseReplay.md`
