Result: HOLDS — the C2 patch to `verifiers/check_description_thresholds.py` (a10240c0 → e966cd59, commit e966cd5, 30 insertions / 0 deletions) leaves every judging line byte-identical, adds only could-not-evaluate paths and self-test arms, and all six scoped checks pass in a sandbox clone at f0e6b695.

Seat: KotobaR55.ReviewFixDescThresholds (wave 2 FALSIFY, read-only on the lane). Sandbox: `/fast/scratch/hyaku/kotoba-r55/ReviewFixDescThresholds` (fresh clone of the lane, checked out at f0e6b695b746775823b65a8c45de7d50ea33e84f). All runs below were executed there with `timeout` caps; no git write of any kind was performed anywhere (the patch-under-test and the base blob were compared as untracked scratch copies; no sandbox commit was needed). No tools were installed (python3 and git were already present).

## Findings by severity

### Low

- **L1 — the patch narrows the accepted `--rev` domain beyond "unknown revision" (valid non-commit objects that the clean path previously judged now exit 2).** `verify_rev` (`verifiers/check_description_thresholds.py:116-122` at tip) demands `rev-parse --verify --quiet "<rev>^{commit}"`. Base accepted e.g. a tree object via `git show <tree>:<path>`; tip rejects it as could-not-evaluate.
  - `TREE=90b479f17cfdc012b4ebc39013e78b609dee7619` (tree of f0e5de82). Base: `python3 -B verifiers/gate_base.py --rev $TREE` → EXIT=0 (real verdict). Tip: → `could-not-evaluate: revision '90b479f…' is not a commit in <sandbox>`, EXIT=2. Same for the rev spec `f0e5de82…^{tree}`: base EXIT=0, tip EXIT=2.
  - Mitigation: the frozen docstring's contract is `--rev <rev>` with "2 = could not evaluate"; the counter's probe table (`verifiers/check_could_not_evaluate.py:74`) only ever passes `--rev {RAND}` (40-hex commits) and `--rev {REV}`; every observed caller passes commits. What the gate reads/compares/counts on inputs it still accepts is unchanged. Reported, not judged a violation.

### Informational

- **I1 — base R-miss mechanism confirmed as diagnosed.** Base `read_file` (`a10240c0` lines 114-133, byte-identical to tip 124-135) returns `None` when `git show` stderr contains `"does not exist"`; for an unknown rev git prints `fatal: path 'SKILL.md' does not exist in '0000…'`, so base judged a repository it could not see. The fix intercepts before `read_file` (`main`, tip line 438-439) and raises `RuntimeError`, caught by the pre-existing `except (RuntimeError, UnicodeDecodeError, OSError)` (tip 444-446, identical text at base 414-416). The fix lives entirely in the could-not-evaluate path.
- **I2 — no second measurement risk.** `git diff e966cd59 f0e6b695 -- verifiers/check_description_thresholds.py` is empty (exit 0): the gate did not change again after the C2 commit.

## Evidence per assigned check

All commands run in `/fast/scratch/hyaku/kotoba-r55/ReviewFixDescThresholds`. `gate_base.py` / `gate_tip.py` are byte copies (sha256 base 4edad582973786a8…, tip 328ccc254fdb311e…; difflib: 30 added, 0 removed lines — matching `git diff --stat a10240c0 e966cd59 -- verifiers/check_description_thresholds.py`) placed under `verifiers/` so `LANE` (`Path(__file__).resolve().parent.parent`) resolves to the clone. An earlier run with the copies at the clone root mis-resolved LANE to `/fast/scratch/hyaku/kotoba-r55` (not a repo); those runs were discarded and repeated from `verifiers/`.

**(1) Judging lines unchanged.** 30 insertions, 0 deletions (git diff and difflib agree; removed lines: NONE). `read_file` identical; `judge`, the per-client prints and `print("description thresholds backed %d of %d clients")` (tip 468) untouched; the only main-path addition is the two-line `verify_rev` hook (tip 438-439). Behavioral proof below: identical verdict lines at identical revisions for base and tip code.

**(2) No exit-1→2 remap, no catch-all, no keying.** The except tuple and `return 2` (tip 444-446) are base text, not patch text; `verify_rev` raises `RuntimeError` only when the revision does not resolve to a commit. Greps over the tip file: `argv|PATH|environ|temp|self_test` hit only argparse plumbing (422, 430), the self-test dispatch (317, 431-434) and the self-test G arm's own temp PATH (73, 407-410). No test for `--self-test` in raw argv (the arms invoke the script with only `--rev`, so any argv keying would break the arms themselves), no temp-dir name or PATH-string logic outside the self-test arm.

**(3) Self-test arms assert exit codes and fail on revert.** Tip: `timeout 300 python3 -B verifiers/check_description_thresholds.py --self-test` → `self-test: 0 failure(s) over 24 assertions`, EXIT=0. The two new arms (`check_description_thresholds.py:404-405, 414-415`) compare the tuple `(returncode, stderr.startswith("could-not-evaluate:"))` against `(2, True)`. Mutants of the tip copy:
  - M1 (fix reverted on the clean path: `if False and r.returncode != 0:` in `verify_rev`) → `--self-test` EXIT=1: `FAIL unknown revision exits 2 with could-not-evaluate: got (1, False), expected (2, True)` — 1 failure over 24 assertions.
  - M2 (could-not-evaluate `return 2` → `return 1`) → EXIT=1: both arms FAIL (`got (1, True)`) — 2 failures over 24 assertions.
  So each arm independently pins the exit code and the stderr prefix.

**(4) Red anchor — a real finding at base still exits 1 at tip.** Rev `bf65974c7845a06d7ef621ad998c6378ff735cd5` (parent of 5a097e1, before the round-54 table/entry/SOURCES rows exist — a genuine under-threshold state):
  - base: `python3 -B verifiers/gate_base.py --rev bf65974…` → `description thresholds backed 0 of 7 clients`, EXIT=1.
  - tip: same command on `gate_tip.py` → `description thresholds backed 0 of 7 clients`, EXIT=1.
  Complementary probe (the exact counter probe shape, `--rev` = 40 zero hex): base printed a fabricated clean verdict `backed 0 of 7 clients`, EXIT=1 on a revision that does not exist anywhere (the class-R miss the plan records); tip printed `could-not-evaluate: revision '0000…' is not a commit in <sandbox>`, EXIT=2.

**(5) Real verdict at f0e5de82 and f0e6b695 — same summary line.** Four runs, each `timeout 120 python3 -B verifiers/gate_{base,tip}.py --rev <rev>`:
  - base@f0e5de82 → `description thresholds backed 7 of 7 clients`, EXIT=0
  - tip@f0e5de82 → `description thresholds backed 7 of 7 clients`, EXIT=0
  - base@f0e6b695 → `description thresholds backed 7 of 7 clients`, EXIT=0
  - tip@f0e6b695 → `description thresholds backed 7 of 7 clients`, EXIT=0

**(6) `--root` without git keeps its base exit code.** Temp dir holding only a `python3` symlink, `env PATH="$d"` (no `git` reachable): `--root <sandbox tree>` → base EXIT=0 and tip EXIT=0, both printing `description thresholds backed 7 of 7 clients`. `verify_rev` is skipped for `--root` (tip 438: `if args.rev:`), and no git call exists on the root path in either version.

**Counter coupling (probe shapes the gate must honour, `check_could_not_evaluate.py:71-86`).** R: `["--rev", <random40>]` → verified exit 2 above. G: real args with git absent → FileNotFoundError (an OSError) at the first git call → exit 2 (also exercised by the passing self-test arm; G already held at base). S: `--self-test` → 0 (above). V: real-revision run → 0 (above).

## Residual risk and verification gaps

- The full C2 counter run (25 probes / 13 controls) was not re-run by this seat — out of this item's scope; the evidence here is per-gate and per-probe-shape. TsukuroiR31.RerunC2Probe owns the counter rerun.
- `--fetch` was not exercised (network path); the diff adds no lines in the fetch region, so this is diff-locality reasoning, not a run.
- L1 stands as the one behavioral delta beyond the could-not-evaluate paths: accepted-input narrowing, not a judging change. If the seat wants strict conformance to "only its could-not-evaluate paths and its self-test arms", `verify_rev` could resolve any object (`git cat-file -e <rev>^{object}`-style) instead of `^{commit}` — but that would reintroduce the base miss for non-commit revs passing `{REV}`-shaped probes, so the current strictness is the safer side; leave as recorded.

Report: .ufo/waves/round-55/falsify/ReviewFixDescThresholds.md
