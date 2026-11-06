# ExecArmsR100 — C1 build (round 100, wave r100-w1)

Seat: ExecArmsR100. Job: insert-only behavioural arms inside `self_test()` of
`verifiers/verify_dispatch_prompts.py` killing t01..t06 of CLAIMS["c1"]
(`verifiers/fixtures/round-100/selftest-kills.py` v6.2).

Status: **complete** — `C1-PREDICATE-MET` measured at scratch rev
`170bb1220fa158349a81a45befa9eb0ac826cddd` (scratch clone
`/fast/scratch/hyaku/kotoba-r100/ExecArmsR100/repo`, `git -C "$D" rev-parse
--show-toplevel` = `$D`; freeze 03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687).
Patch sha256 `7b4e2dbc2450ebbc34360c557897b9b60f0895005cd1d0d631b4dac1746c857e`
(8229 bytes). An early draft accidentally wrote the same insert to the lane
tree via an edit-anchor miss; it was reverted with `git checkout --` in the
lane before any lane read/commit, and the final patch regenerates from a
clean touch (`git diff --stat` in the scratch clone: 144 insertions, 0
deletions, one insert-only region inside `self_test()`).

## Arms (`r100-tNN-*`, all via `rec(...)`, all surviving a raised exception)

- t01 `r100-t01-notdir-exit-zero`: `main()` with a plain file as `--prompts`
  → rc 2, and separately a missing path → rc 2 (m01).
- t02 `r100-t02-enverror-exit-one`: `main()` over a prompts dir holding a
  mode-000 round prompt → rc 2, not 1 (m02). Guarded: if `os.access` says
  the chmod-000 file is still readable (root), prints a skip note instead of
  a false failure (uid here: 1000, guard not taken).
- t03 `r100-t03-json-exitcode-zero`: `main(["--json", ...])` with a plain
  file as `--prompts` → emitted JSON payload's `exit_code` is 2 (m03).
- t04 `r100-t04-dircheck-exists`: `main()` with a plain file as `--prompts`
  → rc 2 and an `ERROR ... not a directory` line, catching a raised exception
  and recording a failure (m22; the mutant raises `NotADirectoryError`).
  Sourced comment cites S282 (Python 3.15.2 pathlib `Path.is_dir`,
  `receipts/sources-opened.txt`): `False will be returned if the path is
  invalid, inaccessible or missing, or if it points to something other than
  a directory` — a plain file must fail the directory check, which
  `exists()` does not.
- t05 `r100-t05-readtext-latin1`: `read_text()` on a UTF-8 file holding
  `café` returns exactly `café\n` (m08).
- t06 `r100-t06-runchecks-sorted`: `run_checks(..., ["dispatch.08",
  "dispatch.04"])` returns ids `["dispatch.08","dispatch.04"]` in request
  order (F3 stable-sort permutation).

Arms are behavioural only (call `main` with explicit argv + in-process
stdout/stderr capture via the existing `_run_main`, `run_checks`,
`read_text`), need no git/network/env beyond TMPDIR/HOME, and never read the
checker's source. All six frozen anchors verified 1 occurrence each after
the insert; no anchor text duplicated.

## Evidence

- Baseline (freeze, unmodified): `--self-test` → `0 failure(s) over 154 assertions`;
  `--box-proof` → `boxes proven 2` rc 0.
- With arms: `--self-test` → `0 failure(s) over 168 assertions` rc 0;
  `--box-proof` → `boxes proven 2` rc 0.
- `selftest-kills.py c1 170bb122... repo` → `C1 targets killed 6 of 6
  (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held
  6 of 6; code decoys held 6 of 6`, `rules v6: honest runs CLEAN 3 of 3;
  mirror runs reported 7 of 7; seed 3fbf030004da4841`, `C1-PREDICATE-MET`.
- Same with `--rules v5` → `C1-PREDICATE-MET` (seed 95f4c40a7554e797).
- `r99c1` → `R99C1 targets killed 12 of 12 ... R99C1-PREDICATE-MET`;
  `r98c1` → `R98C1 targets killed 9 of 9 ... R98C1-PREDICATE-MET`.
- Fresh second scratch clone at the freeze: `git apply --check` OK, applied,
  `--self-test` `0 failure(s) over 168 assertions`, `--box-proof`
  `boxes proven 2`, clone removed.

## Files written

- `verifiers/verify_dispatch_prompts.py` — one insert-only region inside
  `self_test()` (144 insertions, 0 deletions) — via patch
  `.ufo/waves/round-100/w1/ExecArmsR100/ExecArmsR100.patch`.
- `.ufo/waves/round-100/w1/ExecArmsR100.md` (this report; update-in-place).
- `.ufo/waves/round-100/w1/ExecArmsR100_READY`.

## Findings / risks

- No FROZEN ANCHOR duplication; all six `CLAIMS["c1"]` anchors still match
  exactly once (checked by byte count on the patched file).
- The t02 mode-000 arm is uid-guarded exactly as the existing t09 arm; on
  this host (uid 1000) it exercises the real path.
- Tool installs: none. Pacman untouched (host pause respected). Scratch
  removed before yield.
