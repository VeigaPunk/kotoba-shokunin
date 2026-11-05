# SentinelScopeR93 — candidate scope & safety findings (round 93, wave 1)

Seat: SentinelScopeR93 · 2026-11-05 · lane tip observed: `6d7eee0570912d9f3b9d3e3d0137f3c755451233` (freeze commit; unchanged all wave)
Candidate built for gate naming: **`6c0d0aa8f364d49bcecec8e7ed93e80f4d52f6ce`** = freeze + the four builder patches, committed in my scratch clone with the scratch identity; scratch clone deleted after checks (patches under `w1/<seat>/<seat>.patch` are the scored artifacts).

READY files observed: ExecPinCoverage 18:02, ExecReceiptRevs 18:07, ExecKillPinRev 18:15, ScribeCorpusR93 18:25 (poll 4 of my 120 s loop). Patch sha256 ↔ READY first line: 4/4 match.

## Findings

**S1 — PASS (scope (a)): patch union touches exactly the six owned paths; per-seat ownership respected.**
Evidence: `git apply --numstat/--summary` per patch and the committed candidate diff:
`M corpus/README.md; M corpus/SOURCES.md; A corpus/lessons/round-93.md; M verifiers/check_mutation_battery.py; M verifiers/check_tip_battery.py; A verifiers/fixtures/round-93/check-receipt-revs.sh`.
ExecKillPinRev → only `check_mutation_battery.py` (48+/8−); ExecPinCoverage → only `check_tip_battery.py` (32+/2−); ExecReceiptRevs → only the new `check-receipt-revs.sh` (77+/0, mode 100755); ScribeCorpusR93 → only the three corpus paths. No rename/copy/binary/mode-change markers in any patch. Path-set delta base→candidate: added = exactly the two new files; removed = none.

**S2 — PASS (scope (a)): corpus appends-only contract holds.**
`diff base candidate` removed-line count: SOURCES.md **0** (2 inserted rows S267 gitrevisions(7) `<rev>:<path>`, S268 git-cat-file(1) `-e`; inserted in the S2xx section, not EOF — still zero existing lines changed), README.md **0** with exactly **1** added row (the round-93 lesson index row). New `corpus/lessons/round-93.md` is a fresh 182-line file; no spotcheck lesson touched (see S6).

**S3 — PASS (bounds (b)): no seat wrote outside `w1/<seat>/` (+ `<seat>.md`, `<seat>_READY`) and its scratch.**
`find .ufo/waves/round-93 -newer plans/round-93.md -type f` = only w1 seat files, the L1's own wave-management files (`gen-w1.py`, `r93-w1-spec.json`, `r93-w1-dispatch.json`, `r93-w1.ready*` — authored 17:49–17:56 before dispatch), and freeze-time pre-data receipts (mtime artifact). Lane `status --porcelain`: untracked wave files only, zero tracked modifications, lane HEAD never moved off `6d7eee0`. Fleet-root porcelain: `M .scratch/run15-kernel.py`, `M .scratch/run15-state.json`, `M .ufo/l0-questions.md`, `?? w4lines.txt` — none name kotoba round 93; not attributable to this wave. INFO only.

**S4 — PASS (safety (c)): no sysctl, pacman, `/proc/sys` use, credential material, or raw env dump in any seat receipt.**
Greps over `.ufo/waves/round-93`: sysctl/pacman/proc-sys hits only quote the orchestrator's bounds text (`gen-w1.py`, dispatch/spec JSON, my own seat prompt) or state "pacman pause respected" (ConnectorOverlapR93.md); `printenv`/`declare -x` none; credential-ish hits all false positives ("instrument-pin PASS", "can just pass '<commit>'", regex literals).

**S5 — PASS (safety (d)): scratch discipline clean in patched bytes.**
`grep -n '/tmp/'` and absolute-host-path grep over all four patches: none. New `check-receipt-revs.sh` derives LANE from `$0`, takes `<receipts-dir> [REPO]`, uses list-argv subprocess (no shell-injection surface), git calls read-only (`rev-parse --verify`, `cat-file -e`). Smoke run in my scratch: unresolved 40-hex → rc 1 with `UNRESOLVED` line; missing dir → rc 2; empty dir → rc 2; REV= header + G1 12-hex prefix both resolve; `bash -n` ok. Clones observed under `/fast/scratch/hyaku/kotoba-r93/<seat>/`.

**S6 — PASS (frozen-state (e)): all 54 protected paths byte-identical, base vs candidate.**
Per-path `cmp` of `git show 6d7eee0:<f>` vs `git show HEAD:<f>` over: SKILL.md (600/600 lines at candidate), `verifiers/fixtures/round-92/` (5 files), `verifiers/fixtures/mutation-battery/manifest.tsv`, and all 47 `corpus/lessons/round-*-verifier-spotcheck.md`. `git diff --name-only` over those pathspecs: empty.

**S7 — PASS (round-92 A1 coupling): mutation-battery anchors intact on the patched C1 build.**
Static sweep: all 23 manifest data rows' anchor regexes match their target bytes **exactly once** on base AND on the candidate tree (24 rows scanned incl. header), i.e. the named coupling rows `mb-m2-g1-commit-check-skipped`, `mb-m15-clean-tree-guard-off`, `mb-m16-restore-unverified` and every other probe row still anchor uniquely. Both patched checkers AST-parse; the receipt script's embedded python parses.

**S8 — PASS (counter compatibility, static): builder patches match the frozen counters' driving contracts.**
`c1-killpin-rev.sh` drives the public CLI `check_mutation_battery.py --rev <world> --work <dir>`; the patch's new `pinned` parameter defaults to `None` → `KILL_SET_PINNED` (17), so committed-manifest kill-count enforcement activates on the counter's own invocation. `c2-pinkey.sh` AST-edits the running checker's `INSTRUMENT_PINS` dropping `verifiers/check_correction_sweep.py` — which is `BATTERY[5][0]` — so the new missing-key guard fires and the tally reads `guards 4 of 5`. Real `INSTRUMENT_PINS` (7 keys) covers all 6 BATTERY scripts, so the honest world stays PASS/`guards 5 of 5` (`check_freeze_gate.py` pin is the plan-disclosed non-battery key).

**S9 — INFO (observations, no action):**
(i) C1 patch's `self_test()` mutates global `KILL_SET_PINNED` (9→10→…→9) and never restores 17; process exits after self-test and the frozen counter never combines `--self-test` with a later read in-process, so no scored path is affected.
(ii) ExecPinCoverage's new keydrop/keyswap self-test arms call bare `check`/`world`/`_last_line`/`_drive`/`saved_pins` — all confirmed defined in scope inside `self_test()` at base.
(iii) `MutTesterPinCov` had an empty receipt dir at last look (18:24) — that seat's wave output was still pending when I finished; outside my item list.

**S10 — INFO (my own writes, declared):** receipt copies of the four patches + READYs under `w1/SentinelScopeR93/inputs/`, this report at `w1/SentinelScopeR93/SentinelScopeR93.md` and (per the Report trailer and the round-92 precedent of `w1/SentinelScopeR92.md`) a copy at `w1/SentinelScopeR93.md`. Scratch `/fast/scratch/hyaku/kotoba-r93/SentinelScopeR93/` (incl. candidate clone `repo` at `6c0d0aa8…`) deleted before yielding. No tools installed; pacman pause respected.

## Verdict

No scope violation, no frozen-state breach, no hygiene defect found in the four-patch candidate. Candidate for the L1 gate: freeze `6d7eee0` + the four builder patches (my scratch naming: `6c0d0aa8f364d49bcecec8e7ed93e80f4d52f6ce`). Scored readings, self-test runs, and counter runs remain with the reviewer/mutation-tester seats and L1 per plan.
