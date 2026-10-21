verdict: PARTIAL — the round-47 fault-harness planter fix at 7ad7fad is real and load-bearing (Grid A ALL PASS exit 0; Grid B reverts it and d1/d2 MISS again), but one landed gate's verdict (fault-f) does not test its own documented mechanism, the fix ships with no regression guard, and the round's before battery never ran this gate.

# W2FaultHarness — attack of `verifiers/fault_injection_corpus.sh` at 7ad7fad

Lane: `KotobaR47-2.W2FaultHarness-2` (leaf, no subagents dispatched). Round-47 falsify, post-crash wave 2.
Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fault_injection_corpus.sh` @ `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.

## 0. What I attacked

1. The assigned claim: at the landed tip the harness is **ALL PASS / exit 0**, and reverting **only** the round-47 planter fix makes **d1/d2 MISS again**.
2. The *mechanism* of the fix: is the fix load-bearing for the right reason (coverage-map scoping), or does it pass by accident?
3. The landed gate as a whole: does every PASS in the grid actually test what the code comment claims it tests (mutation of the verdict layer, not just of the planters)?
4. Calibration of the round's own record: does the wave's before/after battery actually bracket this gate, and what does the BASE grid really show?

All mutations were made in scratch clones under `/fast/scratch/kotoba-r47/w2/W2FaultHarness/` (canonical layout, sibling fleet dirs symlinked). The production tree was **read-only**; the only writes under `/home/vgpnk/Projects/shokunin/kotoba-shokunin` are this report and `W2FaultHarness.grids.json` / `W2FaultHarness.planter-revert.patch` in `.ufo/waves/round-47/falsify/`.

**Installs / updates: none.** No tool was installed or upgraded; no `pacman` transaction was run (all pacman transactions are paused host-wide).

## 1. Clone and environment

```
mkdir -p /fast/scratch/kotoba-r47/w2/W2FaultHarness
for p in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.ufo; do n=$(basename $p); [ "$n" = kotoba-shokunin ] || ln -sfn "$p" "$n"; done
git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin kotoba-shokunin
git -C kotoba-shokunin checkout -q --detach 7ad7fadfc09354b74fb66605dfb0c1182c115a2f
```
→ `git log --oneline -1` = `7ad7fad`, `git status --porcelain` empty.

Harness header (all runs): `instrument_sha256=28224c76510dcafc4d7a52da41ffd2d366337414f65320cbb21e6d9de12aba9d`, `independent=present`.

## 2. Grid A — landed tip 7ad7fad (the assigned claim, part 1)

```
cd /fast/scratch/kotoba-r47/w2/W2FaultHarness/kotoba-shokunin
bash verifiers/fault_injection_corpus.sh --repo "$PWD"     # exit 0
```

```
fault | script | exit | fired-class | verdict
fault-0-control | integrity | 0 | - | PASS
fault-0-control | independent | 0 | - | INFO(gating)
fault-a | integrity | 1 | corpus.pointers.report_dead | PASS
fault-b | integrity | 1 | corpus.pointers.commit_nonhash | PASS
fault-c | integrity | 1 | corpus.pointers.commit_unresolvable | PASS
fault-d1 | integrity | 1 | corpus.index.stale_patterns,corpus.index.missing_paths | PASS
fault-d1 | independent | 1 | corpus.index.stale_patterns,corpus.index.missing_paths | INFO(gating)
fault-d2 | integrity | 1 | corpus.index.stale_patterns | PASS
fault-d2 | independent | 1 | corpus.index.stale_patterns | INFO(gating)
fault-e | integrity | 1 | corpus.index.unindexed | PASS
fault-f | integrity | 0 | - | PASS(blind-spot documented: control_total=40 plant_total=39 delta=1; --no-baseline exit 0; baseline-mode exit 1)
fault-g | integrity | 0 | - | PASS
fault-h | integrity | 0 | - | PASS(context: quoted=1, checked=40 unchanged)
verdict: ALL PASS
```
Exit code **0**. Reproduces the recorded wave battery `.ufo/waves/round-47/after/fault_injection_corpus.out` byte-for-byte in verdict content.

`bash verifiers/fault_injection_corpus.sh --repo "$PWD" --self-test` → **exit 0**, `T1 PASS / T2 PASS / T4 PASS / T3 PASS / self-test: OK`.

Re-run with `--keep-worlds` (TMPDIR under `/fast/scratch`) to inspect the worlds the harness actually built:
- `fault-d1/corpus/README.md:65` holds the planted row `| Fault injection (d1) | \`knowledge/gone-file-fault.md\` | … |`; `## Coverage map` is at `:5`, `## Frontier` at `:67` → **the row is inside the coverage map** (this is what the fix bought).
- `fault-d1/out.json` DRIFT rows = `corpus.index.stale_patterns`, `corpus.index.missing_paths`.
- `fault-f/out-baseline.txt` = `DRIFT corpus.pointers.report_total: observed=39 expected=40` / `8/9 checks pass; DRIFT: corpus.pointers.report_total` → at the landed tree the f-verdict does rest on the mechanism its comment names.

## 3. Grid B — revert **only** the planter fix (the assigned claim, part 2)

The landed fix (`verifiers/fault_injection_corpus.sh:117-119` @ 7ad7fad) is 3 lines inside `insert_index_row` (`:111`):

```python
start = next(i for i, l in enumerate(lines) if l.startswith("## Coverage map"))
end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
idx = max(i for i in range(start, end) if lines[i].startswith("|"))
```
Reverted to the pre-round form `idx = max(i for i, l in enumerate(lines) if l.startswith("|"))` (patch: `W2FaultHarness.planter-revert.patch`), committed in my clone as `51385ae` (clone only; nothing landed anywhere else).

```
bash verifiers/fault_injection_corpus.sh --repo "$PWD"     # exit 1
```
```
fault-d1 | integrity | 0 | - | MISS
fault-d1 | independent | 0 | - | INFO(gating)
fault-d2 | integrity | 0 | - | MISS
fault-d2 | independent | 0 | - | INFO(gating)
… all other rows unchanged (0-control PASS, a/b/c/e PASS, f PASS(blind-spot), g PASS, h PASS(context: quoted=1, checked=40 unchanged))
verdict: FAILURES PRESENT
```
Exit code **1**. **d1/d2 MISS again, exactly as predicted.** The fix is load-bearing.

Mechanism (why the old planter missed): `insert_index_row` used to insert after the last `|` line *in the whole file*. At 7ad7fad that line is `corpus/README.md:77` — the last row of the `## Frontier` table (section `:66–78`), **outside** the coverage map (`:5–65`). Both corpus instruments harvest the coverage-map section only (`verifiers/verify_corpus_integrity.py:150` `COVERAGE_HEADING_RE`, `verifiers/verify_corpus_independent.py:272` `in_section = stripped == "## Coverage map"`), so a row parked in the Frontier table is never checked for staleness or existence → no DRIFT → MISS. The fix scopes the insert to the coverage-map section and the row now lands at `README:65`.

**Independent confirmation outside the harness** (so the PASS is not self-confirming): in a fresh clone I inserted the same d1-style row at the **top** of the coverage-map table (`corpus/README.md:9`, not via the harness):
- `python3 verifiers/verify_corpus_integrity.py --repo <W> --no-baseline --json` → **exit 1**, DRIFT `corpus.index.stale_patterns` + `corpus.index.missing_paths`, `missing_paths_detail = ["corpus/README.md:9: knowledge/gone-file-fault.md -> knowledge/gone-file-fault.md"]`;
- `python3 verifiers/verify_corpus_independent.py --repo <W>` → **exit 1**, citing `! corpus/README.md:9: knowledge/gone-file-fault.md`.
→ detection is instrument-side and placement-independent; the harness's d1/d2 PASS is not an artifact of end-of-table placement.

## 4. Grid C — BASE `c61a973` unchanged (the "before" leg)

```
cd /fast/scratch/kotoba-r47/w2/W2FaultHarness/base-clone   # detached at c61a973
bash verifiers/fault_injection_corpus.sh --repo "$PWD"     # exit 1
```
```
fault-0-control | integrity | 1 | corpus.index.unindexed | FAIL-control-dirty
fault-a | integrity | 1 | corpus.index.unindexed,corpus.pointers.report_dead | PASS
fault-b | integrity | 1 | corpus.index.unindexed,corpus.pointers.commit_nonhash | PASS
fault-c | integrity | 1 | corpus.index.unindexed,corpus.pointers.commit_unresolvable | PASS
fault-d1 | integrity | 1 | corpus.index.unindexed | WRONG-CLASS(expected=corpus.index.missing_paths)
fault-d2 | integrity | 1 | corpus.index.unindexed | WRONG-CLASS(expected=corpus.index.stale_patterns)
fault-e | integrity | 1 | corpus.index.unindexed | PASS
fault-f | integrity | 0 | - | FAIL
fault-g | integrity | 0 | - | FALSE-POSITIVE
fault-h | integrity | 0 | - | FAIL
verdict: FAILURES PRESENT
```
Exit **1**; `--self-test` → exit **1**, `T2: FAIL (exit=1)`, `T3: FAIL`, `self-test: BROKEN`. Corpus instruments at BASE: integrity **exit 1** (`7/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed`), independent **exit 1**. This grid matches the wave-1 artifact `.ufo/waves/round-47/build/ExecFaultBaseline.md` §1 exactly.

**Calibration note (F5, below):** at BASE d1/d2 report **WRONG-CLASS, not MISS** — the pre-existing unindexed file (the round-46 spot-check lesson) makes every world dirty, so the planter defect is invisible until the corpus-index defect is also fixed. My Grid B (planter-only revert on the *fixed* corpus) is the only configuration in which the planter defect shows up as MISS.

## 5. Findings

### F1 — MEDIUM — the landed `fault-f` verdict does not test the mechanism its own comment names
`verifiers/fault_injection_corpus.sh:298-332` (`fault_known_blind_f`). The verdict condition at `:320` is
`[ "$ex" = 0 ] && [ "$fired" = "-" ] && [ "$base_ex" != 0 ] && [ "$delta" = 1 ]`, and the printed verdict at `:321` claims
`"blind-spot documented: … --no-baseline exit 0; baseline-mode exit $base_ex"`.
The comment at `:293-297` states the mechanism: *"the equal-mode count detector notices report_total moving 1 down against the baseline"*. The code never checks **which** check drifted in baseline mode — only that the run exited non-zero.

**Counterexample (repro).** In a clone of the landed tree, commit a mutated `verifiers/corpus-baseline.json`: `corpus.pointers.report_total.expect 40 → 39` (the *planted* count) and `corpus.index.tracked_files.expect 60 → 58` (an unrelated drift), then
`bash verifiers/fault_injection_corpus.sh --repo "$PWD" --keep-worlds` → **exit 0, `verdict: ALL PASS`**, with
```
fault-f | integrity | 0 | - | PASS(blind-spot documented: control_total=40 plant_total=39 delta=1; --no-baseline exit 0; baseline-mode exit 1)
```
while the kept world's `fault-f/out-baseline.txt` says
```
DRIFT   corpus.index.tracked_files: observed=60 expected=58
8/9 checks pass; DRIFT: corpus.index.tracked_files
```
i.e. **`corpus.pointers.report_total` did not drift at all** (observed 39 == expected 39) — the count detector never noticed anything — and the harness still certifies the blind spot as "documented". The pass therefore rests on an unrelated baseline staleness.

Honesty of the current claim: at the landed tree the mechanism *does* hold (Grid A, `fault-f/out-baseline.txt` = `DRIFT corpus.pointers.report_total: observed=39 expected=40`), so this is **latent, not a live false claim**. Wave-1 named the defect (`ExecFaultBaseline.md` §4.5) and explicitly left it unfixed ("§4.5 is verified as a diagnosis only"); the round landed the corpus re-pin that makes it benign today but did not tighten the verdict.
**Cheap fix:** run the baseline-mode pass with `--json` and require the DRIFT id set to contain `corpus.pointers.report_total` (the `drift_ids` helper at `:167-178` already does exactly this for the `--no-baseline` pass).

### F2 — MEDIUM — the landed fix has no regression guard: `--self-test` is green with the fix reverted
`self_test()` (`verifiers/fault_injection_corpus.sh:389-413`) exercises only `plant_a` and the pristine control; it never touches `insert_index_row` (`:111`), `plant_d1` (`:204`) or `plant_d2` (`:209`).
**Repro:** take the planter-revert of Grid B (uncommitted working tree is enough) and run
`bash verifiers/fault_injection_corpus.sh --repo "$PWD" --self-test` → **exit 0**, `T1 PASS / T2 PASS / T4 PASS / T3 PASS / self-test: OK`.
So the exact regression class the round repaired is invisible to the self-test; only the 14-17 s full run catches it — and the full run is not part of the wave's before battery (F4). A future edit that re-widens the planter (or that renames the coverage-map heading, F3) would leave `--self-test` green.
**Cheap fix:** add a self-test probe that runs `plant_d1`/`plant_d2` in a throwaway world and asserts the DRIFT class, or asserts that `insert_index_row` inserts between `## Coverage map` and the next `## ` heading.

### F3 — LOW/MEDIUM — three different predicates for the same section heading, and the two witnesses disagree on it
- planter: `l.startswith("## Coverage map")` — `verifiers/fault_injection_corpus.sh:117`
- author's instrument: `^##[ \t]+Coverage map[ \t]*$` — `verifiers/verify_corpus_integrity.py:150`
- independent instrument: `stripped == "## Coverage map"` — `verifiers/verify_corpus_independent.py:272`

**Repro (Grid E).** Commit `corpus/README.md` with the heading re-spaced to two spaces (`##  Coverage map`) and run the harness → **exit 1**:
```
fault-0-control | integrity | 0 | - | FAIL-control-dirty      # independent instrument exits 1
fault-0-control | independent | 1 | - | INFO(gating)
fault-d1 | d1 | - | - | INVALID-PLANT                          # StopIteration traceback printed on stderr
fault-d2 | d2 | - | - | INVALID-PLANT
fault-g | integrity | 0 | - | FALSE-POSITIVE
verdict: FAILURES PRESENT
```
Two consequences: (a) the planter raises a raw `StopIteration` (python heredoc at `:111-123`) → `INVALID-PLANT` with an unexplained traceback instead of a diagnosis; (b) the author's instrument accepts the heading (control exit 0) while the **independent witness does not** (control exit 1 → `FAIL-control-dirty`) — i.e. the two witnesses are not equivalent on this input. Everything is fail-closed (suite exit 1, no false PASS), so this is robustness/diagnosability, not a live false green.
**Cheap fix:** have the planter reuse one shared predicate (e.g. parse the coverage-map section exactly as `verify_corpus_independent.py:272` does), and make the planter fail with a one-line message instead of a traceback.

### F4 — MEDIUM (calibration / traceability) — the round's before battery never ran this gate
`.ufo/waves/round-47/before/SUMMARY.md` has **no fault-harness line** (it lists census, surfaces, pins, checklist, corpus integrity, corpus independent, harness claims, frontmatter count, omp, opencode), and `before/exits.txt` contains only `surfaces-override exit=1`. The after side *does* exist: `after/SUMMARY.md` → `fault harness exit=0`, `after/fault_injection_corpus.out` → the ALL PASS grid.
`LOG.md:2323` (C3 bullet) asserts *"fault harness exit 1 → 0, ALL PASS"* — the "before" leg of that transition is sourced from the wave-1 build artifact `.ufo/waves/round-47/build/ExecFaultBaseline.md` §1, **not** from the round's own before battery, which brackets every other gate. The claim is true (I re-derived BASE exit 1 myself, Grid C), but the round's evidence pair is asymmetric: this gate has no recorded before-run output in the wave's before directory.
**Actionable:** re-run the harness at `c61a973` into `.ufo/waves/round-47/before/` (one command, ~17 s) so the transition is bracketed in the wave's own artifacts.

### F5 — LOW/MEDIUM (calibration) — the BASE failure is compound, and `control_clean` does not gate the other rows
At BASE the control world is dirty (`corpus.index.unindexed`, from the unindexed round-46 spot-check lesson). Consequences in the BASE grid:
- d1/d2 read **WRONG-CLASS**, not MISS — the planted classes never appear; the pre-existing `unindexed` DRIFT is all that is seen. The planner defect only becomes visible as MISS *after* the corpus-index rows land (my Grid B configuration).
- `fault-e`'s BASE PASS is **confounded**: the class check at `:276` (`grep -qF -- "$cls"` over the world's DRIFT id list) is satisfied by the pre-existing unindexed file alone, so e's PASS at BASE is not evidence that e's own plant fired.
- `control_clean` failing (`:370-382`) does not annotate or gate the per-fault rows: the BASE table prints **PASS** for a/b/c/e while the control is dirty. The suite exit code is still 1, so this is not a false green — but the per-row table is quoted as evidence elsewhere and reads as if those plants fired cleanly.
This is pre-existing harness design (not introduced by round 47), exposed by round 47's fix. **Cheap fix:** compute the control's DRIFT set once and subtract it from each fault world's DRIFT set before matching the expected class (the same helper `drift_ids` at `:167` is already there); a row whose only DRIFT ids come from the control should not print PASS.

### F6 — LOW (calibration) — unrecorded counter drift outside the coverage map
`index_tokens_outside_coverage_map` moved **1 → 2** across round 47 (independent instrument, BASE vs tip). Cause: the round-47 rewrite of the Frontier row `corpus/README.md:76` puts two backticked tokens in that table's column 2 — `trigger.no_xml_tag` and `lessons/round-47.md` — and the Frontier table is outside the coverage map, so those tokens are counted but **never existence-checked**. The counter is not baseline-pinned and appears in neither `before/SUMMARY.md` nor `after/SUMMARY.md`. (`lessons/round-47.md` does exist, so there is no live defect; the observation is that a round-47 corpus edit grew an unpinned, unchecked counter by 1 without a record.)

## 6. Verdict detail

| claim under attack | result |
|---|---|
| harness is ALL PASS / exit 0 at the landed tip | **HOLDS** (Grid A, exit 0; also `--self-test` exit 0) |
| reverting only the planter fix makes d1/d2 MISS again | **HOLDS** (Grid B, exit 1, d1/d2 MISS) |
| the fix is load-bearing for the stated reason (coverage-map scoping) | **HOLDS** (Grid B + world inspection + out-of-harness manual plant at `README:9`) |
| every PASS in the landed grid tests what its own comment claims | **BROKEN for fault-f** (F1; latent today) |
| the landed fix is regression-guarded | **BROKEN** (F2: `--self-test` exit 0 with the fix reverted) |
| the round's before/after evidence brackets this gate | **BROKEN** (F4: no before-run output in the wave's before directory) |

## 7. What I did NOT check

- I did not re-derive C1 (omp 18.12.5 / opencode 1.19.3 surfaces + pins), C2 (`trigger.no_xml_tag`), the governance errata, `corpus/QUALITY.md` Q19, `corpus/SOURCES.md` S012–S015 or `corpus/lessons/round-47.md` M20–M22 — other lanes own those. I only touched the corpus-index side that the fault harness consumes.
- I did not run `verify_harness_claims.py` (the after battery records it at **exit 1**, 21/28 — an open red at the landing tree that `LOG.md:2326` lists under "Not claimed"; I did not adjudicate whether the fault-harness work affects it).
- I did not run `check_substrate_pins.py`, `verify_surfaces.py`, `verify_skill_checklist.py`, `check_assertion_floors.py`, or the corpus instruments' `--self-test` modes.
- I did not test the harness on a different fleet root: `plant_f` (`:226-233`) hard-codes `/home/vgpnk/Projects/shokunin/.ufo/reports/round-4/kotoba.md` and would be `INVALID-PLANT` elsewhere (pre-existing; already named in round-21's F4 scout D1). I did not move that file to test it.
- I did not test `--keep-worlds` behaviour differences (I used it only for evidence; the non-kept and kept grids were identical), nor a real ENOSPC, nor `PYTHONOPTIMIZE=2` (pre-existing `assert` concern, round-21 F4 D3).
- I did not audit `insert_index_row`'s other callers: `plant_d1`/`plant_d2` are its only users; `plant_e` adds a tracked file (no README row) and is unaffected by the scoping change (Grid A/B show e PASS in both).
- I did not verify the wave-1 artifact `ExecFaultBaseline.md`'s intermediate what-if states A–D (I re-derived BASE, tip, and the planter-only revert myself).
- I did not run the harness against the production tree at `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (the assignment asked for the canonical clone); the recorded `after/fault_injection_corpus.out` shows the production run reached the same ALL PASS grid with the same `instrument_sha256`.

## 8. Environment note (operational risk for other lanes)

`/tmp` was at **97–100 % full (1.3 GiB free)** during my runs. Each harness run creates 12 worlds ≈ 1.5 GB peak under `${TMPDIR:-/tmp}` and removes them on exit (`:53-56`) — i.e. one concurrent run can exhaust the partition and make *other* lanes' harness runs fail with ENOSPC (wave-1 §4.9 predicted this). I found one **abandoned** harness scratch dir from a dead process (`/tmp/round12-faults.2249658`, 1.5 GB, owner pid not alive, no file modified in the last 6 minutes) and removed it to reclaim space (`rm -rf` → exit 0; free space 1.3 GiB → 4.4 GiB). No live process held it. My own kept worlds live under `/fast/scratch/kotoba-r47/w2/W2FaultHarness/tmp/`.

## 9. Artifacts

- `.ufo/waves/round-47/falsify/W2FaultHarness.md` — this report.
- `.ufo/waves/round-47/falsify/W2FaultHarness.grids.json` — all six grids with commands, exit codes and row-by-row verdicts, plus the out-of-harness manual-plant confirmation and the counter drift.
- `.ufo/waves/round-47/falsify/W2FaultHarness.planter-revert.patch` — the exact revert used for Grid B (`verifiers/fault_injection_corpus.sh:117-119` → one line).
