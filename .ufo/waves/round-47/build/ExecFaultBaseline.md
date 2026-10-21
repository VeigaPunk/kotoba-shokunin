verdict: BASE harness exits 1 (control dirty on the round-46 lesson; self-test BROKEN). With the C3 index row alone, control and self-test go green but the harness stays exit 1 because the d1/d2 planters insert outside the coverage map (MISS; predicted and measured). Row plus tracked_files re-pin plus a scoped planter insertion reaches ALL PASS, exit 0, in scratch only; nothing landed.

# ExecFaultBaseline: fault-injection baseline at BASE c61a973

Target: `verifiers/fault_injection_corpus.sh` (433 lines) at `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.

- Scratch clone: `/fast/scratch/kotoba-r47/ExecFaultBaseline/lane` (detached at BASE, clean). What-if clones: `whatif` (states A–D), `d1cov`, `d2cov`.
- Production `/home/vgpnk/Projects/shokunin/kotoba-shokunin`: read-only. Only `git clone` (read) ran against it; no git mutation; the harness was not run against it. Writes: this report, two JSON artifacts and three what-if patches, all under `.ufo/waves/round-47/build/`.
- Installs or updates: none. Labrat probes: none.
- Axes for the milestone (freshness, operability, calibration): freshness in §2 and §4.5; operability in §4.7–§4.9 and §6; calibration in §4.1–§4.6.

## 1. BASE measurement (required)

Every harness run used `TMPDIR=/fast/scratch/kotoba-r47/ExecFaultBaseline/tmp` (see §6).

- `bash verifiers/fault_injection_corpus.sh --repo <lane>`: exit 1, `verdict: FAILURES PRESENT`. Three runs gave identical grids (runs 2 and 3 are a fresh process and `--keep-worlds`).
- `bash verifiers/fault_injection_corpus.sh --repo <lane> --self-test`: exit 1, `self-test: BROKEN`. Two runs, identical.
- Instrument SHA256 recorded by the harness (`verify_corpus_integrity.py`): `28224c76510dcafc4d7a52da41ffd2d366337414f65320cbb21e6d9de12aba9d`.

Verdict grid (run 1; the independent column is exit 1 in every fault row, control included, and is not shown separately):

| fault | integrity exit | integrity fired | verdict |
|---|---|---|---|
| 0-control | 1 | corpus.index.unindexed | FAIL-control-dirty (`:374`) |
| a | 1 | unindexed, pointers.report_dead | PASS |
| b | 1 | unindexed, pointers.commit_nonhash | PASS |
| c | 1 | unindexed, pointers.commit_unresolvable | PASS |
| d1 | 1 | unindexed | WRONG-CLASS(expected=index.missing_paths) |
| d2 | 1 | unindexed | WRONG-CLASS(expected=index.stale_patterns) |
| e | 1 | unindexed | PASS (confounded, §4.3) |
| f | 1 | unindexed | FAIL |
| g | 1 | unindexed | FALSE-POSITIVE |
| h | 1 | unindexed | FAIL |

Self-test at BASE: T1 PASS, T4 PASS, T2 FAIL (exit=1), T3 FAIL, so `BROKEN`. T2 and T3 fail only because the control is dirty (§2).

Instrument self-tests on the same code: `verify_corpus_integrity.py --self-test` exit 0 (150 assertions, 0 failures); `verify_corpus_independent.py --self-test` exit 0 (91 assertions, 0 failures).

## 2. The known BASE failure: root cause

- Commit `c61a973` (BASE) adds only `corpus/lessons/round-46-verifier-spotcheck.md` (17 lines, `git show --stat c61a973`). The file is tracked but no `corpus/README.md` row names it, and a tree-wide grep finds no reference to it.
- Integrity default mode at BASE: 2 DRIFT. `corpus.index.tracked_files` observed 59 vs expected 58 (`verifiers/corpus-baseline.json:15`), and `corpus.index.unindexed` = `["corpus/lessons/round-46-verifier-spotcheck.md"]`. Independent `--json`: 1 DRIFT, `corpus.index.unindexed` = 1. This matches the plan's "2 DRIFT / 1 DRIFT".
- Harness: control verdict FAIL-control-dirty (`fault_injection_corpus.sh:374`). The self-test's no-op and clean-world assertions (`:398`, `:407`) fail on the same dirt.
- Corpus README layout at BASE: coverage map `:5–62` (last row `:62`); `## Frontier` `:64–76`; `## Known gaps` `:77`.

## 3. Prediction for the C3 index row, and what was measured

The prediction was recorded before the state-A run: control PASS; a, b, c, e PASS; **d1 and d2 MISS**, not WRONG-CLASS; f, g, h PASS; harness exit 1; self-test OK. The reason is §4.1.

What-if states, all scratch-only:
- **A**: C3 row only, `corpus/README.md:63` (commit `e626a94`).
- **B**: A plus `verifiers/corpus-baseline.json:15` `tracked_files` 58→59 (commit `12211a0`).
- **C**: B plus `insert_index_row` restricted to the coverage-map section (`fault_injection_corpus.sh:117–119`; uncommitted working-tree diff).
- **D**: C with the pin reverted to 58 (working tree, restored afterwards).

| fault | A | B | C | D |
|---|---|---|---|---|
| 0-control | PASS | PASS | PASS | PASS |
| a, b, c | PASS | PASS | PASS | PASS |
| d1 | **MISS** (integrity exit 0) | **MISS** | PASS (stale+missing) | PASS |
| d2 | **MISS** (integrity exit 0) | **MISS** | PASS (stale) | PASS |
| e | PASS | PASS | PASS | PASS |
| f | PASS (blind-spot) | PASS | PASS | PASS (stale pin, §4.5) |
| g | PASS | PASS | PASS | PASS |
| h | PASS (quoted=1, checked=40) | PASS | PASS | PASS |
| harness | exit **1** FAILURES PRESENT | exit **1** | exit **0** ALL PASS | exit **0** ALL PASS |
| self-test | exit 0 OK | exit 0 OK | exit 0 OK | not run |
| integrity default mode | exit 1, 1 DRIFT (tracked_files 59≠58) | exit **0**, 9/9 | exit 0 | exit 1, 1 DRIFT |

Consequences:
- The C3 row alone clears the control and the self-test, but `fault_injection_corpus.sh` still exits 1.
- The plan's "0 DRIFT" for integrity needs the re-pin (B). The harness does not need it (D reaches exit 0).
- Harness exit 0 needs the planter scope fix (C).

## 4. Counterexamples and calibration defects (path:line at BASE)

**4.1 The d1/d2 planters land outside the coverage map (cause of MISS).** `insert_index_row` (`fault_injection_corpus.sh:111–121`) inserts after the last `|` line in the file (`:117`). At BASE that is `corpus/README.md:75`, under `## Frontier` (`:64–76`), not the coverage map (`:5–62`). Both instruments read only the coverage-map section: `verify_corpus_integrity.py:367–371` (`inside` gate) and `verify_corpus_independent.py:254` (`coverage_cells`). Evidence: the kept BASE world `fault-d1/corpus/README.md:76` holds the planted row under `## Frontier`. `git log -S'## Frontier' -- corpus/README.md` returns `f2f9ee1` only, the round-46 landing. Counter-test: the same rows placed in the coverage map (`d1cov`, `d2cov`, state A plus a row at README:64) fire the intended classes in both instruments. d1 gives `stale_patterns` and `missing_paths`; d2 gives `stale_patterns`. Integrity and independent both exit 1.

**4.2 WRONG-CLASS at BASE is a mislabel.** d1 and d2 detected nothing of their own. `unindexed` came from the pre-existing r46 file, so the planted classes never appear in the grid.

**4.3 e's BASE PASS is confounded.** `fault-e/out.json:15–17` lists `unindexed_detail` = [`corpus/knowledge/fault-injected-note.md`, `corpus/lessons/round-46-verifier-spotcheck.md`]. The must-fire check tests only the class name (`:274`), so the pre-existing file alone satisfies it.

**4.4 Independent column misreports.** `control_clean` (`:379`), `fault_known_blind_f` (`:322`) and `fault_must_not_fire` (`:365`) hard-code the fired class as `-`. The independent JSON does report `corpus.index.unindexed` at BASE. Only `fault_must_fire` (`:288`) computes it.

**4.5 f's blind-spot PASS can rest on the stale pin.** The verdict requires `base_ex != 0` (`:318`) and `delta = 1` (`:315`). `delta` comes from observed counts, not from the baseline. The comment at `:291–295` says the equal-mode detector notices report_total, but the code does not test that. In state A, the control's own baseline-mode run already exits 1 with only `tracked_files` DRIFT, so a non-zero `base_ex` in f's run says nothing about report_total. Only after the re-pin (B) does f's baseline run fail on report_total alone (`fault-f/out-baseline.txt`: `DRIFT corpus.pointers.report_total: observed=39 expected=40`). In D the harness is ALL PASS with the stale pin, and f still passes.

**4.6 Self-test header disagrees with the code, and the MISS branch is never run.** `:383–386` says T2 "MUST answer MISS". `:396–398` asserts a clean exit 0 instead. No self-test path calls `fault_must_fire`, so the MISS verdict (`:272–273`, `:281`) is untested. T2 and T3 also depend on corpus state, so the self-test cannot separate harness logic from corpus dirt.

**4.7 Environment faults become verdicts (exit 1, not 2).** `new_world` returns 2 on clone failure (`:76–78`). Its callers turn that into a FAIL row rather than exiting 2: `fault_must_fire` (`:262`), `control_clean` (`:370`), and the same pattern in `fault_known_blind_f` (`:298`, `:301`), `fault_h_context` (`:331`, `:334`) and `fault_must_not_fire` (`:352`). Exit 2 is documented only for the up-front guards (`:58–63`). [INFERENCE from code; not triggered.]

**4.8 Host coupling.** `plant_f` needs `/home/vgpnk/Projects/shokunin/.ufo/reports/round-4/kotoba.md` to exist and its moved target to be absent (`:225–227`). The guard passed on this host, since f is not INVALID-PLANT. On another fleet root, f would be INVALID-PLANT. [INFERENCE; code-read only.]

**4.9 Footprint.** One world is about 124 MB (`du -sh` of the kept `fault-a`: lane `.ufo` 98 MB tracked, `.git` 26 MB). A run creates 12 worlds and removes them only at EXIT (`:55–56`), so the peak is about 1.5 GB under `${TMPDIR:-/tmp}` (`:53`). `/tmp` was 99% full (1.4 GB free) when I started. [INFERENCE: ENOSPC at the default `/tmp` under that condition; not run.]

## 5. Recommendation for C3 (scratch-measured, not landed)

1. Add the r46 row inside the coverage map, after `corpus/README.md:62`.
2. Re-pin `verifiers/corpus-baseline.json:15` `tracked_files` 58→59. This is needed for integrity default mode to read 9/9 (B) and for f's check to test report_total (§4.5). It is not needed for harness exit 0 (D).
3. Scope `insert_index_row` to the coverage map (`fault_injection_corpus.sh:117`; the 3-line scratch diff is `ExecFaultBaseline.whatif-planter-fix.patch`). Harness: ALL PASS, exit 0; self-test OK (C).
4. Not tested: fixes for §4.4, §4.6 and §4.7. §4.5 is verified as a diagnosis only.

## 6. Runtime and environment

- Main harness: 17.27 s (run 1, shell `time`); 17.69 s real (run 2, fresh `bash -c`; user 12.57 s, sys 5.55 s); 14.40 s (run 3, `--keep-worlds`).
- Self-test at BASE: 2.64 s (first run).
- What-if A (main + self-test): 17.97 s. B: 13.90 s. C: 15.31 s. D (harness only): 11.98 s (tool wall, includes an integrity run and the restore).
- The persistent shell's CPU totals (1m51s user, 1m42s sys) include reaped children of the shared shell, so I did not use them.
- TMPDIR deviation: every harness run used `TMPDIR=/fast/scratch/kotoba-r47/ExecFaultBaseline/tmp`, because `/tmp` was 99% full (1.4 GB free) at my start. The variable only names the world directory (`:53`), so verdicts should not depend on it. I did not run the default-`/tmp` path. Later `/tmp` read 87% (17 GB free); cause not investigated.

## 7. Commands and exit codes

- `bash verifiers/fault_injection_corpus.sh --repo <lane>`: 1 (×3, `FAILURES PRESENT`).
- `… --repo <lane> --self-test`: 1 (×2, `BROKEN`).
- `python3 verifiers/verify_corpus_integrity.py --json` (lane): 1 (2 DRIFT).
- `python3 verifiers/verify_corpus_integrity.py --no-baseline --json` (lane): 1 (unindexed).
- `python3 verifiers/verify_corpus_independent.py --json` (lane): 1 (unindexed).
- `python3 verifiers/verify_corpus_integrity.py --self-test`: 0 (150 assertions, 0 failures).
- `python3 verifiers/verify_corpus_independent.py --self-test`: 0 (91 assertions, 0 failures).
- `git show --stat c61a973`, `git log -S'## Frontier' -- corpus/README.md`, `git show c61a973:corpus/README.md | grep -n '^|'`: 0 (read-only, scratch clone).
- State A: commit `e626a94` (0); harness `--keep-worlds` 1; self-test 0; integrity default 1 (8/9, tracked_files).
- d1cov and d2cov: integrity `--no-baseline` 1 each; independent 1 each.
- State B: commit `12211a0` (0); integrity default 0 (9/9); harness `--keep-worlds` 1; self-test 0.
- State C: harness (plain) 0 (`verdict: ALL PASS`); self-test 0 (`self-test: OK`).
- State D: harness (plain) 0 (`verdict: ALL PASS`); integrity default 1 (tracked_files); pin restored with `git checkout -- verifiers/corpus-baseline.json` (0).
- Cleanup: `rm -rf` on my kept world directories only (exit 0).

## 8. Artifacts (`.ufo/waves/round-47/build/`)

- `ExecFaultBaseline.md`: this report.
- `ExecFaultBaseline.base-grid.json`: BASE grid, runs, exits, self-tests.
- `ExecFaultBaseline.whatif-grid.json`: states A–D and the coverage-map mechanism check.
- `ExecFaultBaseline.whatif-c3-row.patch`: state A (README row). Scratch-only.
- `ExecFaultBaseline.whatif-c3-rebaseline.patch`: state B (pin 58→59). Scratch-only.
- `ExecFaultBaseline.whatif-planter-fix.patch`: state C (planter scope, `fault_injection_corpus.sh`). Scratch-only, uncommitted.

## 9. Not checked

- Production HEAD and working tree, and whether C1, C2 or C3 has landed. Production was not run against.
- `verify_harness_claims.py`, `check_substrate_pins.py`, `verify_surfaces.py` and the checklist gate. Out of scope.
- The default-`/tmp` path, a real ENOSPC, and a different fleet root for `plant_f` (§4.7–§4.9 are inferences).
- Plain (non-`--keep-worlds`) runs of states A and B. The keep flag did not change BASE verdicts (run 3 vs runs 1–2), so their grids should match.
- Fixes for §4.4, §4.6 and §4.7. State C changes one function and was tested only against this README layout.
- Other repo gates under state C. Only the fault harness and the two instruments' own checks were run.
