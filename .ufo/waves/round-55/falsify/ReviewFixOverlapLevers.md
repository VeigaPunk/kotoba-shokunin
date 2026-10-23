Result: HOLDS — the C2 patch to `verifiers/check_overlap_levers.py` adds could-not-evaluate handling for unknown revisions without touching judging lines, exit-1 semantics, or root/default behavior; both new self-test arms revert-fail as required.

Scope: `git diff a10240c0 e966cd59 -- verifiers/check_overlap_levers.py` (53 insertions, 3 deletions). Verified byte-identical to `a10240c0..f0e6b695` (both diffs sha256 `ce1f991a50291ff693b930c942bd4478b8013e5d6c3aaac64b5f1ce5016c9fe8`), so the reviewed patch is exactly what the tip carries. Sandbox: `/fast/scratch/hyaku/kotoba-r55/ReviewFixOverlapLevers` at `f0e6b695`; base gate saved as `verifiers/.base_gate_copy.py` from `a10240c0:verifiers/check_overlap_levers.py`. All runs `timeout 900 python3 -B`; UTC of runs 2026-10-23 ~00:14 (host clock), recorded via `date -u`.

## 1. Judging lines unchanged — PASS

The diff's 3 hunks are purely additive to the could-not-evaluate path plus one mechanical wrap:
- `+class EnvError(Exception)` and `+def verify_rev(repo, rev)` (`git rev-parse --verify --quiet <rev>^{commit}`; nonzero -> `EnvError`; `OSError` -> `EnvError`), tip lines 526-540.
- `git_show` gains `try/except OSError -> EnvError` around the existing `git show` call; `rc != 0 -> return None` and the decode line are untouched context lines (tip 543-553).
- `main` gains `if args.rev: verify_rev(repo, args.rev)` and `except EnvError -> print("could-not-evaluate: %s") -> return 2`, placed before the pre-existing `except OSError` (tip 598-610).
- Self-test gains two `check(...)` arms (tip 1220-1244).

`evaluate()`, `CLIENTS`, `REVIEWED_LEVERS`, the BACKED/UNBACKED print loop, `overlap levers backed %d of %d clients`, `rc = 0 if k == len(CLIENTS) else 1`, and the `--fetch` tally are all unchanged context. `except` count: base 3 -> tip 6 (the three new ones are `OSError`-in-`verify_rev`, `OSError`-in-`git_show`, `EnvError`-in-`main`); no `except Exception` or bare `except` added.

## 2. No 1->2 remap, no catch-all, no argv/PATH keying — PASS

- Exit 2 is reachable only via `EnvError` (git unrunnable / revision not a commit) and the pre-existing `OSError` root-reader path. A real finding cannot wear exit 2: `verify_rev` passes for every committish (`v=<commit>^{commit}`), and valid-revision semantics (missing file -> `git_show` rc!=0 -> `None` -> absent table -> backed count falls -> exit 1) are preserved verbatim — proven in §4 where a real finding still exits 1 with byte-identical output.
- `grep -n 'os\.environ\|sys\.argv\|PATH\|TMPDIR'` shows no argv-shape, temp-dir-name, or PATH-string keying in production code; the only PATH touch is inside the new self-test arm itself.

## 3. Self-test arms assert exit codes and fail on revert — PASS

- Tip self-test: `python3 -B verifiers/check_overlap_levers.py --self-test` -> `0 failures`, `53 assertions`, exit 0.
- Both arms assert `rc == 2` AND `"could-not-evaluate:"` in stderr (tip:1223-1226, 1241-1244).
- Revert mutant A (verify_rev call dropped, git_show wrap kept): `--self-test` -> `FAIL unknown --rev is could-not-evaluate: rc=1 stderr=''`; `1 failures`, exit 1.
- Revert mutant B (verify_rev def+call dropped, git_show wrap reverted; arms kept): `--self-test` -> two FAILs: `unknown --rev is could-not-evaluate: rc=1 stderr=''` and `unavailable git is could-not-evaluate: rc=2 stderr="ERROR reading input: [Errno 2] No such file or directory: 'git'\n"`; `2 failures`, exit 1. So each arm independently catches its own reverted fix.
- Note (not a defect): the G arm's discriminating signal on full revert is the missing `could-not-evaluate:` marker — the pre-existing `except OSError` already returns 2, so `rc` alone cannot see this revert. Asserting the marker is the correct stronger check.
- Caveat (inherent, recorded honestly): a full revert that also deletes the arm code trivially passes — the arms detect production-code reverts, not their own deletion.

## 4. Red anchor: real finding still exits 1 at tip — PASS

`--rev 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` (pre-round-51 lane revision, resolves in the lane clone):
- tip code: exit 1; base code: exit 1; `diff .base_red.out .tip_red.out` -> byte-identical, ending `overlap levers backed 0 of 7 clients` (all seven `UNBACKED: SKILL.md table absent`). The exit-1 path is observably untouched, not just unremapped.

## 5. Same verdict at both pinned revisions — PASS

Tip code, `python3 -B verifiers/check_overlap_levers.py`:
- `--rev f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c` -> exit 0, `overlap levers backed 7 of 7 clients` (7x BACKED).
- `--rev f0e6b695b746775823b65a8c45de7d50ea33e84f` -> exit 0, identical summary line.

## 6. R/G probes and --root/default without git — PASS

- R (fresh `os.urandom(20).hex()` = `08e4cfeed17eafe26133cad6f673e920a569225a`, same shape as the counter's `os.urandom(20).hex()`): tip -> exit 2, stderr `could-not-evaluate: revision '08e4...' is not a commit in /fast/scratch/...`. Base -> exit 1 (`backed 0 of 7`), matching frozen receipt `.ufo/waves/round-55/controls/C2-base.txt:13` (`R expect 2 got 1 MISS`).
- G (`env PATH=$PWD/.nogit`, `.nogit` holds only a `python3` symlink; git's absence proven by the gate's own `Errno 2` message): tip `--rev f0e5de82` -> exit 2, `could-not-evaluate: git not runnable: [Errno 2] No such file or directory: 'git'`. Base -> exit 2 via the pre-existing `except OSError` (`ERROR reading input: ... 'git'`), matching `C2-base.txt:14` (`G got 2 ok`) — the G line was never a counter miss; the patch only strengthens the message class.
- `--root` and default forms touch no git at base or tip (`verify_rev`/`git_show` run only under `args.rev`). With `PATH=.nogit`:
  - `--root .redtree` (SKILL.md present but empty): tip exit 1, `backed 0 of 7 clients`; base exit 1 — real-finding exit preserved.
  - default (working tree at tip): tip exit 0, base exit 0.
- Counter agreement: `.ufo/waves/round-55/C2-measure-e966cd59.txt:14-17` shows this gate `R 2 / G 2 / S 0 / V 0` all `ok`.

## Observations (non-blocking)

- `verify_rev` runs one extra `git rev-parse` subprocess before the four `git show` reads on every `--rev` call; a git disappearance between the two lands in the new `git_show` wrap -> exit 2. Honest could-not-evaluate; no semantic change.
- `--rev` naming a non-commit object (tag/blob/tree) fails `^{commit}` -> `could-not-evaluate` -> 2. Base behavior would have been a silent 0-of-7 -> 1; the new reading (can't evaluate a non-commit) is the intended contract and strictly more truthful.
- `--rev ""` remains falsy -> treated as root mode, identical at base and tip (pre-existing quirk, out of scope).

## Residual risk / gaps

- `verify_rev` validates the revision once; a repo mutation mid-run is not defended (irrelevant for the counter's frozen-rev use).
- No probe was run for `--rev` on a revision where `git show` partially succeeds (e.g., one of the four paths unreadable at a valid rev) — unreachable without repo corruption; the `None`->absent-table path is unchanged anyway.
- Frozen-counter re-run at tip is owned by another seat (`W2RerunC2`); this report covers gate-level probes only.

No installs used or needed (python3, git, coreutils already present).
