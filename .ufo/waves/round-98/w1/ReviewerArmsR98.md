# ReviewerArmsR98 — review of the C1 patch (ExecArmsR98)

Status: review complete on the evidence below; positive controls and box proof read in the final section.

## Subject
- Patch: `.ufo/waves/round-98/w1/ExecArmsR98/ExecArmsR98.patch`, sha256 `27b412a58bf7583beb3d47013903a9d47203374b7ca0e1843aff816b90ffa6bf` (matches READY).
- Base: freeze `63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`. Candidate (scratch commit, identity `scratch <scratch@invalid>`, inside my clone only): `db1fe1075427dfa85f8796232861391227637790`.
- Scratch: `/fast/scratch/hyaku/kotoba-r98/ReviewerArmsR98` (repo clone: `.../repo`, `rev-parse --show-toplevel` = clone path).

## Production bytes (blocking check: PASS)
- `git apply --check` on the freeze: OK.
- `git diff --stat 63cd48d..db1fe10`: `verifiers/verify_dispatch_prompts.py | 183 +++` — 183 insertions, 0 deletions, ONE hunk (`@@ -1331,6 +1331,189 @@`).
- The hunk lies inside `self_test()` (defined base line 679, `return 1 if failures else 0` at base line 1337). Production code (`lane_of` through `box_proof`/`main`) is byte-identical.
- Frozen anchors each match exactly once on the candidate: ROUND_FILE_RE line; `dirs = sorted({r for r, _s in paths})`; `    for f in result["files"]:`; `        if entry.get("disposition") != want:`; `        if live.get(cid) != pinned:`; `        if m and m.group(1)[0] * 3 == fence:`; `    if legacy.is_file():`; dispatch.04 docstring + `names = sorted(...)` pair; `        if stem.endswith(".md"):`; `stem = stem[:-3]`; `if note:`; `    if fails:` + `status = "FAIL"` (the two-line form; the bare `    if fails:` text occurs twice in base, which is pre-existing and not a frozen anchor). No new occurrence of any anchor in the patch.
- Helpers the arms use (`lane_case`, `run_proof`, `write_manifest`, `map_path`, `proof`, `skill_src`, `box_map`, `cases`, `fx`) are nested closures or module constants already in base `self_test()` (lines 985–1114); no new helper is added outside self_test.

## Anti-sniffing (PASS)
- Every new arm calls a production function or in-process `box_proof` (via `run_proof`, which uses `contextlib.redirect_*` and the return code) and asserts on the observed result: `lane_of`, `evaluate_dispatch_04/08`, `_verdict_of`, `report_paths`, `state_source`, `dispatch_box_sha256`, `box_proof`. None reads `verify_dispatch_prompts.py` source.
- The t05 arm rewrites a copy of SKILL.md inside its own proof tree (not the checker source) and restores it.
- Every assertion goes through `rec(...)` (the `self-test FAIL: ` prefix). t08's arm catches the `EnvError` a mutant raises and records it as a failed `rec`, not a crash, so the kill is REPORTED, not RUN-ERROR.
- No new fixture directory name collides with an existing case name (checked: no duplicate `lane_case` / `_write_case` / `root /` names in the candidate).

## Fixtures and TMPDIR (PASS)
- All new fixtures live under the base `root` from `tempfile.TemporaryDirectory`, or under `proof`/`fx`, all inside that temp root. No network, git, or environment variable is used by the arms.
- Hand run (below): TMPDIR contents after each run = 0 entries left; honest run passes under a minimal env (PATH, LANG, TMPDIR, HOME, PYTHONDONTWRITEBYTECODE only).

## Per-mutant kill attribution (hand-applied, each mutant text substituted into a copy of the candidate's `verifiers/` + `SKILL.md`, run as `python3 -B verify_dispatch_prompts.py --self-test` with a minimal env)
Source: `.ufo/waves/round-98/w1/ReviewerArmsR98/hand-mutants.txt`.

- t01-lane-suffix-unanchored — rc 1, `3 failure(s) over 128 assertions`:
  - `self-test FAIL: r98-t01-lane-suffix-unanchored: lane_of rejects a '.bak' name: got ('kote', 7, 'round')`
  - `... a '.bak' prompt evaluates 0 files: got 1`
  - `... a '.bak' prompt is out of scope: got []`
- t02-dirs-first-only — rc 1, `2 failure(s) over 128`: `r98-t02-dirs-first-only: a round-8 path beside the round-7 path leaves conjunct filename_report_dir_round_equal FAIL: got {'status': 'PASS', ...}` and `... the round-8 path makes the dispatch.08 file FAIL: got {... 'verdict': 'PASS' ...}`.
- t03-verdict-first-file — rc 1, `2 failure(s)`: `r98-t03-verdict-first-file: the verdict of the second file is found: got None` and `... second file's verdict is PASS: got None`.
- t04-proof-disposition-unenf — rc 1, `2 failure(s)`: `r98-t04-proof-disposition-unenf: an 'executed:' disposition proves no box: got (0, 'boxes proven 2\n', '')` and `... refusal names the disposition: got ''`.
- t05-proof-live-hash-unenf — rc 1, `2 failure(s)`: `r98-t05-proof-live-hash-unenf: a reworded live dispatch.04 box refuses the proof: got (0, 'boxes proven 2\n', '')` and `... refusal names the live hash: got ''`.
- t06-fence-any-close — rc 1, `1 failure(s)`: `r98-t06-fence-any-close: a '~' line inside a backtick block keeps the block open: got {'dispatch.01': 'fd8667c9...'...}`.
- t07-legacy-exists — rc 1, `2 failure(s)`: `r98-t07-legacy-exists: a directory '<lane>.round' has no state source: got ('stale', None, 'state-stale: only kote.round present ...')` and `... is not state-stale`.
- t08-prompts-include-dirs — rc 1, `2 failure(s)`: `r98-t08-prompts-include-dirs: a prompt-named directory raises no EnvError: got EnvError(...)` and `... ignored (evaluated 1): got None`.
- t09-md-uppercase — rc 1, `3 failure(s)`: `r98-t09-md-uppercase: report_paths keeps an upper-case '.MD' suffix: got [(7, 'kote')]`, `... '.MD' stem leaves conjunct report_stem_is_lane_id FAIL: got {'status': 'PASS', ...}`, `... '.MD' stem makes the dispatch.04 file FAIL: got {... 'verdict': 'PASS' ...}`.
- honest (unmutated candidate, minimal env): rc 0, `0 failure(s) over 128 assertions` (base was 105; the patch adds 23 assertions).

## Counter readings on the candidate (db1fe10)
Receipts: `.ufo/waves/round-98/w1/ReviewerArmsR98/cand-*.txt`.
- `selftest-kills.py c1 db1fe10` (v6): `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9`; `rules v6: honest runs CLEAN 3 of 3; mirror runs reported 10 of 10`; `C1-PREDICATE-MET`, rc 0.
- `selftest-kills.py c1 db1fe10 --rules v5`: identical tally; `rules v5: honest runs CLEAN 3 of 3`; `C1-PREDICATE-MET`, rc 0. C1 does not depend on C2's rules 8–10.
- Pre-data do-nothing (base, for contrast): `C1 targets killed 0 of 9` UNMET (v6 and v5).

## Findings
1. (non-blocking, documentation) The t02 comment block at the top of the new arms (`# Note: the t02 witness is a file of round 7 ... so no kill is possible under that reading, and the MutTesterDispatchR97 witness table (round-7 file) is what kills.`) is garbled and wrong: the arm's own round-8 path is what kills t02 (shown by the hand run above). It should say the arm kills it. No behaviour change; the L1 may request a one-comment fix in a follow-up patch or accept as is.
2. (non-blocking, scope) The patch appends 23 assertions and no production change; no C2 interaction.
3. No blocking finding in the patch against the C1 spec or the anti-sniffing / frozen-anchor / TMPDIR rules.

## Pending (final section below once read)
- positive controls `r97c1`, `r96c1`, `r95c1` and `--box-proof` on the candidate (job running; receipts `cand-r97c1-v6.txt`, `cand-r96c1-v6.txt`, `cand-r95c1-v6.txt`, `cand-box-proof.txt`).

## Positive controls and box proof on the candidate (db1fe10) — all as frozen
- `selftest-kills.py r97c1 db1fe10`: `R97C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13`; `R97C1-PREDICATE-MET`, rc 0.
- `selftest-kills.py r96c1 db1fe10`: `R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11`; `R96C1-PREDICATE-MET`, rc 0.
- `selftest-kills.py r95c1 db1fe10`: `R95C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN`; `R95C1-PREDICATE-MET`, rc 0.
- `verifiers/verify_dispatch_prompts.py --box-proof` in the candidate clone: `boxes proven 2`, rc 0.
- Candidate honest `--self-test` run directly in the clone: `0 failure(s) over 128 assertions`.

## Verdict
- Blocking findings: none.
- Non-blocking: finding 1 (t02 comment wording). Everything else in the C1 spec checks out: 9 of 9 kills under v6 and v5, each attributable to named new assertions, with production bytes unchanged outside self_test().

## Residual risk / verification gaps
- The counter runs and the hand-mutant runs used the same instrument text, so the hand run is not independent of the counter's mutant table. Each mutant anchor was read from `CLAIMS["c1"]` in the frozen counter, and the replacement was applied with the counter's own rule (count must equal 1).
- I did not run the lane-level no-harm battery (census, gate registry, tip battery, round-96/95/93/92 pins); those belong to the landing step, not this review.

## Tooling
- No tools installed or upgraded. No host setting changed. No pacman.
- Scratch directory removed at the end of this seat.
