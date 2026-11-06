# ExecArmsR98 — C1 build (round 98, wave r98-w1)

Seat: ExecArmsR98 (builder, leaf). Status: complete.

Task: add behavioural arms to `self_test()` in
`verifiers/verify_dispatch_prompts.py` killing the nine frozen v6-counter
survivors t01..t09 (CLAIMS["c1"]), each a `rec(...)` naming the arm
(`r98-t01-...`), reporting (never crashing) on each mutant, honest-clean,
git-less safe. Production code byte-identical outside the self-test section;
frozen anchors kept unique; patch base
`63cd48d9de2c44eb40691ca05d3a41cc2f9a3248` from the seat scratch clone.

## Design (per-arm witness; F2–F6 of MutTesterDispatchR97.md)

- t01: `lane_of("kote-round-7.md.bak") == (None, None, None)` plus an
  `evaluate_dispatch_04` case whose only prompt file is a `.bak` name:
  honest `evaluated == 0`, mutant 1.
- t02: prompt with report paths in round-7 AND round-8, file round 7
  (the mutant's `[7]` slice matches only then; same mechanism as the
  witness in MutTesterDispatchR97.md): honest
  `filename_report_dir_round_equal` FAIL, mutant PASS.
- t03: two prompt files, target `kote-round-7.md` sorted second;
  `_verdict_of` must find it with verdict PASS; mutant returns None.
- t04: proof tree whose map dispositions are `executed:...` (both
  boxes): `box_proof` rc 1, `boxes proven 0`; mutant rc 0 / 2.
- t05: proof tree's copied SKILL.md with the dispatch.04 box reworded
  ("literal" → "literalx"): `box_proof` rc 1 with the live-hash detail;
  mutant rc 0.
- t06: `dispatch_box_sha256` over a backtick-fenced block containing a
  `~~~` line before a box line: honest `{}`, mutant hashes dispatch.01;
  plus an unfenced control that still hashes.
- t07: a DIRECTORY named `kote.round` in the state dir:
  `state_source` kind `none`, detail without `state-stale`; mutant `stale`.
- t08: a DIRECTORY named `ghost-round-7.md` in the prompts dir: honest
  `evaluated == 1`, no EnvError (the EnvError is caught and recorded as
  a failing `rec`, never a crash); mutant raises EnvError.
- t09: report path stem `kote.MD` kept whole: `report_paths` gives
  `(7, "kote.MD")` and `report_stem_is_lane_id` FAILs for lane `kote`;
  mutant strips `.MD` and reads PASS.

Note on and the seat item's t02 wording ("file round 8"): with dirs
{7,8} and file round 8 the mutant (`dirs[:1] == [7] != [8]`) also reads
FAIL, so no kill is possible under that reading; the witness table in
MutTesterDispatchR97.md (round-7 file) is what kills. I follow the
witness and record the deviation here rather than the unkillable reading.

## Candidate and verification

Candidate commit (scratch clone, identity scratch <scratch@invalid>):
`04f44b7c16a2bea54f4f57877d9cf0ede0c096fa` (parent
`63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`). Patch sha256
`27b412a58bf7583beb3d47013903a9d47203374b7ca0e1843aff816b90ffa6bf`.
Diff is add-only (183 insertions, 0 deletions) inside `self_test()`;
all frozen c1/r97c1/r96c1 anchor texts verified unique (count 1) after
the edit. Patch re-proven on a second fresh clone at the freeze
(`git apply --check` OK, then self-test 0/128 and `boxes proven 2`).

| command | observed |
|---|---|
| `python3 -B verifiers/verify_dispatch_prompts.py --self-test` | `0 failure(s) over 128 assertions`, rc 0 |
| `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 |
| `selftest-kills.py --rules v6 c1 <rev> $D` | `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9`, `C1-PREDICATE-MET`, rc 0 |
| same `--rules v5` | `C1 targets killed 9 of 9 ... C1-PREDICATE-MET`, rc 0 |
| `r97c1 --rules v6` and `--rules v5` | `R97C1-MET` 13 of 13 both rules, rc 0 |
| `r96c1 --rules v6` | `R96C1-PREDICATE-MET` 11 of 11, rc 0 |
| `r95c1 --rules v6` | `R95C1-PREDICATE-MET` 3 of 3, rc 0 |

Receipts under `.ufo/waves/round-98/w1/ExecArmsR98/`:
`selftest-honest.txt`, `box-proof.txt`, `counter-c1-v6.txt`,
`counter-c1-v5.txt`, `counter-r97c1-v6.txt`, `counter-r97c1-v5.txt`,
`counter-r96c1-v6.txt`, `counter-r95c1-v6.txt`, `ExecArmsR98.patch`.

## Files written

- `.ufo/waves/round-98/w1/ExecArmsR98.md` (this report)
- `.ufo/waves/round-98/w1/ExecArmsR98_READY`

Tool installs: none.
