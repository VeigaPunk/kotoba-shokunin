# ExecBattery — round-90 C1 mutation-battery runner (findings)

Seat: ExecBattery. Predicate: plans/round-90.md § C1 (frozen). No plan, controls, or frozen instrument edited.

## Built

- `verifiers/check_mutation_battery.py` (stdlib, `python3 -B`), sha256 `0828fd9b6277c98826521109b7abac5930dea9c9e5bb26314d84b54218477e3b`.
  - `--rev` (full hash, lane commit), `--work` (scratch), `--self-test`, and `--allow-unregistered` (pre-registry opt-in; G3 reported, not enforced; not in the frozen line).
  - Targets read via `git show <rev>:<path>`; a scratch clone is detached at `<rev>` and probed (G1). Each probe's copy is read back and compared to the recorded sha256 (G2). G3 counts SKILL.md lines naming the battery.
  - Probes: the frozen set (fg `--self-test`, `--plan` fixed/unsat; d5 `--self-test`, `--base-receipt` round-89 receipt). Baseline is observed first; fg declared exits are checked (exit 2 otherwise).
  - Kill = any probe exit or result-bearing output differs from baseline. Output lines carrying 12+ hex runs or scratch paths are excluded from the observation (run-specific tokens); exit codes are always compared. A probe timeout counts as a flip.
  - Equivalents are generated at run time from the revision bytes: comment before each top-level statement (AST), a marker in each docstring (AST), trailing spaces on code lines outside strings (tokenize). Each row is one rewrite applied to every eligible site of its target. A rewrite that changes no bytes, or does not compile, is could-not-evaluate.
- `verifiers/fixtures/mutation-battery/manifest.tsv`: 13 `kill` rows (r89 kill rows ported as anchor-regex edits), 1 `survivor` row (d5-m1a, see finding 1), 6 `equivalent` rows (3 rewrites x 2 targets). Recipes are JSON in the recipe column.
- Self-test: 19 assertions. Satisfying world (exit 0, exact line), dirty working tree (G1), broken conjunct K != M (exit 1), short rev (G1 trip), tampered copy (G2 trip), no SKILL row (G3 trip, and the `--allow-unregistered` waiver), missing anchor (exit 2), E != E world (a probe reads its own source line count), observation filter, and the three rewrites.

## Evidence (lane tip 6fa5bb6; the battery reads its manifest from `--rev`, so the measurement used a scratch landing candidate)

- Scratch candidate `1c5c1cb5ed41fbe5d2216eb15500831d7b4f33a6` = lane tip + the two owned files (scratch clone only; nothing committed in the lane; deleted after this report).
- Self-test: `0 failure(s) over 19 assertions`, exit 0 (`battery-selftest.txt`).
- Reading (a), `--allow-unregistered`: `mutation battery killed 13 of 13 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 1`, exit 1 (`battery-run.txt`). The G3 line reads `0 SKILL.md line(s) name check_mutation_battery.py`.
- Reading (b), frozen form: same counts, `G3 registry presence FAIL: 0 SKILL.md line(s)`, exit 1 (expected until the L1 lands the registry row). Confirmed the frozen line is printed verbatim.
- Lane tip not modified by the battery: `git status` shows only the two new owned files plus other seats' files.

## Findings (routed to L1; nothing repaired into frozen bytes)

1. **d5-m1a is killed at final bytes; the survivor-class classification does not hold.** The plan and the r89 record put `d5-m1a-d5iii-leg-only` in class `survivor`. At final bytes it flips both frozen probes: the d5 self-test fails arm `w_added_instance` (exit 0 -> 1), and the base-receipt probe flips `PASS d5iii` -> `FAIL d5iii instance growth under: [tracked_files 181>180, unindexed 1>0, commit_total 62>61, report_total 146>144]`. That d5iii leg is active at the lane tip, so the "not reached by the lane probes" premise is false. Measured reading: `disclosed survivors 0 of 1`, exit 1. Evidence: `d5-m1a-evidence.txt`, `d5-m1a-base-receipt-{baseline,mutant}.txt`.
   - The disposition text I drafted for d5-m1a in the manifest is therefore wrong. I did not change the class or the text (frozen by plan, and changing them after a reading is an amendment). L1 must decide via `plans/round-90-addendum-*.md` before any scored reading: reclassify to `kill` (then `killed 14 of 14 ...; disclosed survivors 0 of 0`, which reads exit 0 once the registry row lands), or keep it as a survivor with a true disposition that cannot be satisfied at these bytes.
2. **The r89 d5-m1a anchor is absent from the final bytes.** The r89 text `    if not grew:\n` does not occur in `check_r86_routed_repairs_v3.py` at 39704ad or later (the d5iii condition is `if not grew and not added:`). The r89 `SURVIVED` row therefore cannot be reproduced at the frozen bytes; it was measured against an earlier revision. Ported recipe: `if not grew and not added:` -> `if True:`. Curator note for the r89 record.
3. **Lane shape is required for the d5 probe.** The d5 gate's Q79 location probe requires the measured root's parent to hold `.ufo/reports/round-76/kotoba.md`. A bare clone exits 2 (`SKIP location_flipped ... could-not-evaluate`). The battery mirrors the lane's parent shape by symlinking that single file into `<work>/fleet/` (a read-only symlink to the fleet report; no fleet write).
4. **The battery reads its manifest and checker from `--rev`.** At the lane tip (6fa5bb6) it exits 2 (`git show ...manifest.tsv failed`). The L1 landing commit must include both `verifiers/check_mutation_battery.py` and the manifest before the predicate is measured.
5. **Measurement choices the L1 should know about.** G2 checks sha256 read-back against the revision bytes (the manifest has no sha column). The equivalence rewrites are generated per run, not a fixed list. The docstring rewrite appends a marker rather than changing words. The d5 `--self-test` output contains run-specific hashes and temp paths, which the observation filter drops by design; only exit codes and non-run-specific lines decide flips.

## Tools

None installed or updated. No pacman, no kernel or sysctl change.

## Checks for the main agent

- `python3 -B verifiers/check_mutation_battery.py --self-test` (expect `0 failure(s) over 19 assertions`).
- After the L1 lands the SKILL.md row and the manifest decision: `python3 -B verifiers/check_mutation_battery.py --rev <landing> --work <scratch>` from a lane-shaped clone.
