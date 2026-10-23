Result: DONE — the routed-defect fixes are diagnostic-only plus a load-scaled child cap and a preflight returncode check; no judging line (what each gate reads, compares or counts) changed, all eight `--self-test`s pass, and both required probes reproduce.

# Seat ReviewRoutedFixes — diff-scope review, `git diff b0b7140b c22fdd3 -- verifiers/`

Scope as assigned: `verifiers/box_proof_case_deletion.py`, `check_correction_sweep.py`,
`check_description_thresholds.py`, `check_gate_finding_delta.py`, `check_mcp_instructions.py`,
`check_overlap_levers.py`, `verify_corpus_independent.py` (commit 250e3026, defect 5a) and
`check_assertion_floors.py` (a5314640, defects 4 and 5b). The two files new at c22fdd3
(`check_agent_definitions.py`, `check_agentdef_boxes.py`) are other seats' scope.

Sandbox: `git clone /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r56/ReviewRoutedFixes` +
`checkout -q c22fdd390e10623209024c9bbc2fa86b0cdfc333`. No lane mutation; no sandbox commits made (all runs read-only).

## Judging-line audit — PASS

Read both diffs in full (`/tmp/floors.diff` 217 lines, `/tmp/seven.diff` 477 lines in my sandbox):

- Defect 5a (seven gates): the only production change is the could-not-evaluate message emitted on a
  failed `git rev-parse --verify --quiet` (or `--git-dir` for `verify_corpus_independent`). Each file gains an
  identical `revision_error()` helper (box_proof_case_deletion.py:212, correction_sweep.py:137,
  description_thresholds.py:116, gate_finding_delta.py:88, mcp_instructions.py:311, overlap_levers.py:530;
  `git_unreadable` at verify_corpus_independent.py:74). Contract preserved: exit-1-with-empty-stderr still
  prints `revision %r is not a commit in %s` — verified live (probe 4 below). `--quiet` does suppress
  rev-parse's fatal line on unknown revs (`git rev-parse --verify --quiet 'no-such-rev^{commit}'` → rc 1,
  stderr empty), so the unknown-rev branch is reachable, not dead code. Every raise site keeps its old
  exception class (RuntimeError → exit 2 via existing handlers; CouldNotEvaluate; EnvError), so exit codes
  and channels are unchanged. No comparison, threshold, counter, or file-list line touched.
- Defect 4/5b (`check_assertion_floors.py`): adds `child_timeout_s` (line 170, `base * min(max(1.0, load),
  15.0)`), a per-child cap at line 591 feeding `subprocess.run(timeout=cap)` line 595, a `git --version`
  preflight returncode check at lines 511–517, and the `--load` argparse knob (line 495). The
  observed-vs-floor comparison (`re.search(pattern, proc.stdout)` and the floor arithmetic) is untouched;
  the preflight only moves "git cannot run" onto the could-not-evaluate channel instead of letting 14 child
  failures stand in for it.

## Self-tests — all pass (run in sandbox)

| gate | command result |
|---|---|
| box_proof_case_deletion | `0 failure(s) over 17 assertions`, exit 0 |
| check_correction_sweep | `0 failure(s) over 14 assertions`, exit 0 |
| check_description_thresholds | `self-test: 0 failure(s) over 26 assertions`, exit 0 |
| check_gate_finding_delta | `self-test: 0 failure(s) over 13 assertions`, exit 0 |
| check_mcp_instructions | `self-test: 0 failure(s) over 17 assertions`, exit 0 |
| check_overlap_levers | `0 failures` over `55 assertions`, exit 0 |
| verify_corpus_independent | `99 assertions, 0 failures`, exit 0 (arms 96–99 are the new refusing-git arm) |
| check_assertion_floors | `0 failure(s) over 165 assertions`, exit 0 (~12 s; new arms T1–T3, F31) |

## Required probes — reproduced

1. **Refusing-git probe (CLI, defect 5a).** `mkdir refusebin; ln -s python3 refusebin/python3;` git shim
   `echo "fatal: detected dubious ownership in repository at '/x/y'" >&2; exit 128`; then
   `PATH=<refusebin> python3 -B verifiers/check_description_thresholds.py --rev HEAD` →
   exit 2, stderr `could-not-evaluate: git rev-parse 'HEAD' failed in /fast/scratch/hyaku/kotoba-r56/ReviewRoutedFixes (exit 128): fatal: detected dubious ownership in repository at '/x/y'`. Git's own words quoted, revision not blamed.
2. **Floors `--load` probes (defect 4).**
   - `--self-test-timeout 0.5 --load 1` → exit 2; line `FAIL corpus_independent self-test timed out after 0.5s (base 0.5s x load 1.00 = cap 0.5s; hung?)` — load 1 pins the cap to the base exactly, timeout line names base/load/cap.
   - `--self-test-timeout 0.5 --load 40` → exit 2; line `FAIL harness_independent self-test timed out after 7.5s (base 0.5s x load 40.00 = cap 7.5s; hung?)` — also demonstrates the MAX_SCALE clamp (cap 7.5 = 15×0.5, not 20s) and honest reporting (prints the real load 40, not the clamped factor).
   - Edge: `--load nan` → exit 2, cap `0.5s` (`max(1.0, nan)` evaluates to 1.0 in this call; verified). No hang.

## Supporting checks

- Unknown-rev unchanged: `python3 -B verifiers/check_description_thresholds.py --rev no-such-rev-56` →
  exit 2, `could-not-evaluate: revision 'no-such-rev-56' is not a commit in ...` — the old contract intact.
- Non-repo probe: `verify_corpus_independent.py --repo /tmp/not-a-repo-56` → exit 2,
  `could-not-evaluate: git rev-parse --git-dir failed in /tmp/not-a-repo-56 (exit 128): fatal: cannot change to ...`.
  [INFERENCE-free note] A path that does not exist now reports git's chdir error instead of "not a git
  repository"; a real non-git directory still hits the `"not a git repository"` substring branch
  (verify_corpus_independent.py:78). Same exit 2 either way.
- Grep for consumers of the removed message strings (`is not a commit`, `not a git repository`): no hits in
  `verifiers/` or `corpus/`; hits are `.ufo/` history and docs only.

## Findings

- **None breaking.** Within the 15-minute box no defect found in the changed lines.
- **Minor (cosmetic):** `check_assertion_floors.py` timeout line prints `cap` twice (`timed out after %.1fs ... = cap %.1fs`), a leftover from the old `%g` wording; output only, no logic.
- **Minor (informational):** preflight `git --version` failure message can embed multi-line stderr/stdout
  (`(preflight.stderr.strip() or preflight.stdout.strip() or "(no output)")`, line 515), so the
  could-not-evaluate line may span lines; still exit 2, still prefixed.
- **Residual risk:** `revision_error`'s "unknown revision" branch keys on exit 1 + empty stderr; if a future
  git prints a warning to stderr while still exiting 1 for an unknown rev, the message shifts to the
  "git failed" form — same channel, same exit, only wording. Not exercised against non-GNU/git builds.
- **Verification gap:** did not re-run the gates' positive paths end-to-end against the lane (probes were
  negative-path only, per the item); the 8 self-test batteries cover the instrument walks on fixtures.

No tools installed (pacman paused; nothing needed beyond system python3/git).
