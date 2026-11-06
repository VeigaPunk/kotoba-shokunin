# ExecArmsR99 — C1 build: dispatch-prompt self-test kills t01..t12 (round 99)

Seat: ExecArmsR99 (executor, leaf). Status: **complete** — `C1-PREDICATE-MET` at the
scratch commit, patch READY.

- Base: freeze `b53e209603e7c480cd975ea543e415b66f695438`.
- Scratch candidate: `d3dfbc773dfe56d953e461fd62858486beae0adb` (scratch identity,
  in `$D=/fast/scratch/hyaku/kotoba-r99/ExecArmsR99/repo` only; `git -C "$D"
  rev-parse --show-toplevel` = `$D`).
- Arm assertions: 128 → 154; honest self-test `0 failure(s) over 154 assertions` (`self-test.txt`).
- `--box-proof`: `boxes proven 2` rc 0 (`box-proof.txt`).

## Files changed

- `verifiers/verify_dispatch_prompts.py` — `self_test()` only: 270 added lines,
  0 deleted lines (`git diff b53e209..HEAD` shows no `-` lines outside the
  `---` header; production code outside `self_test()` and its self-test
  helpers is byte-identical). Twelve behavioural arms `r99-tNN-...`, each a
  `rec(...)` named for the frozen survivor, reading observed results from
  `lane_of`, `evaluate_dispatch_04/08`, `run_checks`, `main` (argv explicit,
  stdout captured in-process), `box_proof`, `EnvError`, `os.access` guard:
  - t01 `kote-L1.md.bak` evaluates 0 files / out of scope.
  - t02 role round 8 above filename round 7 → `filename_role_round_equal` FAIL, file FAIL.
  - t03 map `text_sha256` = 64 zeros → `boxes proven` ≠ 2, rc 1, refusal names `map text_sha256`.
  - t04 SKILL.md deleted → rc 1, refusal names `live SKILL.md box hash`; restore proves 2 again.
  - t05 PASS-labelled duplicate of the stem must-fail case → rc 1, `verdict … expected` refusal.
  - t06 `run_checks(..., ["dispatch.04","dispatch.08"])` returns both results.
  - t07 `main()` on a wrong report stem exits 1, prints `FAIL dispatch.04`.
  - t08 `main(["--check","dispatch.04",...])` → exit 0, one result line, no `dispatch.08`
    (the same tree under `--check dispatch.08` exits 1); cites S281 in the arm comment
    (argparse `action='append'`, `.ufo/waves/round-99/receipts/sources-opened.txt`).
  - t09 mode-000 prompt → `EnvError`; guarded by `os.access` (root → recorded pass).
  - t10 control-case `file` = `kote-round-7` (prefix) → rc 1, `not evaluated`.
  - t11 two dispatch.04 map entries (bad first, good second) → last wins, `boxes proven 2` rc 0.
  - t12 one FAILing + one N/A round file → dispatch.08 status FAIL.
- FROZEN ANCHORS: no anchor text was added; the diff's only anchor-looking
  lines are comment/test-data strings, not replacements of the anchor
  statements (verified: no deleted lines, so each anchor survives byte-identical).

## Verdicts (receipts under `.ufo/waves/round-99/w1/ExecArmsR99/`)

| run | receipt | observed (tail) |
|---|---|---|
| `--self-test` | `self-test.txt` | `0 failure(s) over 154 assertions` rc 0 |
| `--box-proof` | `box-proof.txt` | `boxes proven 2` rc 0 |
| `c1` (rules v6) | `c1-v6.txt` | `C1 targets killed 12 of 12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 12 of 12; code decoys held 12 of 12` / `C1-PREDICATE-MET` |
| `c1` (`--rules v5`) | `c1-rulesv5.txt` | same tally, `C1-PREDICATE-MET` |
| `r98c1` | `r98c1.txt` | `R98C1 targets killed 9 of 9 … R98C1-PREDICATE-MET` |
| `r97c1` | `r97c1.txt` | `R97C1 targets killed 13 of 13 … R97C1-PREDICATE-MET` |

Counter command shape (seat spec): `HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r99/ExecArmsR99
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-99/selftest-kills.py --rules v5 c1 <rev> "$D"`
(v6 run identical without `--rules v5`; `r98c1`/`r97c1` same with those claim names).

## Patch / READY

- Patch: `.ufo/waves/round-99/w1/ExecArmsR99/ExecArmsR99.patch`
  (`git diff --cached --binary b53e209603e7c480cd975ea543e415b66f695438` after
  `git add -A -- verifiers/verify_dispatch_prompts.py`), sha256
  `9b705bc807855d0149a9eda9e2d45d2f024a34bb71606f99979f158f3f9af924`.
- Applies on a second fresh clone at the freeze: `git apply --check` OK
  (`PATCH_APPLIES_OK`), clone then removed.
- READY: `.ufo/waves/round-99/w1/ExecArmsR99_READY` (patch sha256 + one line).

## Bounds / risks

- Arms use only TMPDIR/HOME (plus `os.geteuid`-free `os.access`); no git,
  network, or env beyond the counter's minimal set. The t09 arm records a
  pass as root instead of a false failure.
- Every new assertion goes through `rec(...)` with in-arm try/except around
  `run_checks`/`main`/`evaluate_dispatch_04`, so mutants read
  REPORTED-FAILURE, never a crash (single deliberate exception: the t09
  `EnvError` test itself calls `evaluate_dispatch_04` under try/except).
- Baseline drift note: none — self-test/box-proof stay green.

## Files written

- `.ufo/waves/round-99/w1/ExecArmsR99.md` (this report; lane-relative path
  `.ufo/waves/round-99/w1/ExecArmsR99.md`)
- `.ufo/waves/round-99/w1/ExecArmsR99/ExecArmsR99.patch`,
  `.ufo/waves/round-99/w1/ExecArmsR99/{self-test,box-proof,c1-v6,c1-rulesv5,r98c1,r97c1}.txt`,
  `.ufo/waves/round-99/w1/ExecArmsR99/commit-diff.txt`
- `.ufo/waves/round-99/w1/ExecArmsR99_READY`
- Scratch only: `/fast/scratch/hyaku/kotoba-r99/ExecArmsR99/` (all counter
  runs; the scratch tree under `repo/` holds the commit but is not a
  lane artifact).

Tooling installs: none (no pacman per the host-wide pause; nothing else needed).
