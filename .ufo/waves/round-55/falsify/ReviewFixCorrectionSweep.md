Result: HOLDS — the C2 patch to verifiers/check_correction_sweep.py adds could-not-evaluate handling without touching judging lines, red paths, or verdict output; all six review axes verified empirically in a sandbox clone.

# Scope
Reviewed `git diff a10240c0 e966cd59 -- verifiers/check_correction_sweep.py` (+35/-1). File is byte-identical between a10240c0 and f0e5de82 (diff-lines=0) and between e966cd59 and f0e6b695 (diff-lines=0), so the tip copy is the reviewed change. Sandbox: `git clone` of the lane to /fast/scratch/hyaku/kotoba-r55/ReviewFixCorrectionSweep, `git checkout -q f0e6b695…` (HEAD=f0e6b695). Lane untouched except this report. No installs needed (python3, git already present); no tool installs performed.

# The change
New: `import os`; `verify_revision(rev)` running `git -C <LANE> rev-parse --verify --quiet <rev>^{commit}` and raising RuntimeError on nonzero rc; two self-test CLI arms; `main` calls `verify_revision(a.rev)` and widens `except RuntimeError` to `except (OSError, RuntimeError)`.

# (1) Judging lines unchanged
The diff never touches: `blocks` (tip :86-106), `sweep` (:109-123) — every regex, the `lead` order comparison, the `"stale claim without the declared result"` string, `reader` (:126-134), the REGISTRY and SEEDED tables (:31-83), the clean-path output lines `FAIL %s`/`correction sweep: %d stale block(s)` and `return 1 if bad else 0` (:244-247), or any pre-existing self-test case (:147-197). Verified by reading the full tip file against the raw diff (69 lines, all hunks accounted for) — no hunk overlaps a judging line.

# (2) No banned remap / keying
- Exit 1→2 remap: `return 1` still fires only when `bad` is non-empty; `bad` is populated only by `sweep`, which is unchanged. The OSError widening can only fire when an exception is raised — a real finding still returns exit 1 (proven empirically below: aeed089 → 1).
- Catch-all: `except (OSError, RuntimeError)` is keyed on exception type, not message text or context. No swallowing of findings: findings are a returned list, not exceptions.
- No keying on argv shape (only `a.self_test`, `a.rev` truthiness), temp-dir names, or PATH strings anywhere in the gate.

# (3) New self-test arms assert exit codes and fail when the fix is reverted
Arms at tip :199-220 assert `returncode == 2`, `stderr.startswith("could-not-evaluate: ")`, and message substrings ("is not a commit" / "'git'"). Revert experiment: copied tip file to `verifiers/cs_revert.py` with the production half reverted (dropped `verify_revision` call, `except (OSError, RuntimeError)` → `except RuntimeError`), arms kept intact:
```
$ python3 -B verifiers/cs_revert.py --self-test
2 failure(s) over 13 assertions
FAIL unknown revision: exit 2, stderr 'could-not-evaluate: missing corpus/README.md\n'
FAIL git unavailable: exit 1, stderr 'Traceback (most recent call last):…'
exit=1
```
Both new arms go red (the second catches the uncaught FileNotFoundError traceback). Tip code itself: `python3 -B verifiers/check_correction_sweep.py --self-test` → `0 failure(s) over 13 assertions`, exit 0.

# (4) Red anchor — a real finding still exits 1
Revision `aeed089` (post-gate-introduction, pre-round-53 corrections) is a real finding at base: all 8 registry files present, round-53 rows red.
```
$ python3 -B verifiers/cs_base.py --rev aeed089     # base code (f0e5de82 copy)
FAIL r53-c2-claudemd-semantics … (8 FAIL lines)
correction sweep: 8 stale block(s)
exit=1
$ python3 -B verifiers/check_correction_sweep.py --rev aeed089   # tip code
correction sweep: 8 stale block(s)
exit=1
```
`diff` of the two outputs: identical. (c8407a4 → 11 stale blocks, a44196d → 8, same result.)

# (5) Same verdict line at the two pinned revs
```
base code --rev f0e5de82…  → "correction sweep: 0 stale block(s)"  exit=0
tip  code --rev f0e5de82…  → "correction sweep: 0 stale block(s)"  exit=0
base code --rev f0e6b695…  → "correction sweep: 0 stale block(s)"  exit=0
tip  code --rev f0e6b695…  → "correction sweep: 0 stale block(s)"  exit=0
```

# (6) `--root`/default forms without git keep base exit codes
PATH = a temp dir containing only a `python3` symlink (`env -i PATH=$T`):
```
tip  --root .              → "correction sweep: 0 stale block(s)"  exit=0
base --root .              → "correction sweep: 0 stale block(s)"  exit=0
tip  --root /nonexistent-xyz → "could-not-evaluate: missing corpus/README.md" exit=2
base --root /nonexistent-xyz → "could-not-evaluate: missing corpus/README.md" exit=2
```
`--root` never invokes git, so identical behavior by construction; confirmed empirically. (`--self-test` without git is expected to report the git-absent arm red — that is the counter's intent, not a defect.)

# Counter-contract spot check
`verify_revision` is a read-only `rev-parse` (no mutation). With git present, unknown rev → exit 2 (`could-not-evaluate: revision '…' is not a commit in …`), a nonsense string (`not-a-rev-zzz`) → exit 2. With git absent, `--rev HEAD` → exit 2 (`could-not-evaluate: [Errno 2] No such file or directory: 'git'`) where base produced an uncaught traceback + exit 1 — exactly the class-G fix. Matches the counter's GATES row at verifiers/check_could_not_evaluate.py:78 (R/G → expect 2, S → 0, V → 0|1).

# Minor observations (non-blocking, informational)
- Cosmetic only: unknown-rev stderr wording changed from `missing corpus/README.md` to `revision '…' is not a commit in …` — the class-R probe's stderr now names the real cause. Exit code unchanged (2 both ways).
- `Path.read_text` OSError on `--root` now → 2 instead of an uncaught traceback exit 1. Consistent with the could-not-evaluate contract; unreachable for a genuinely missing file (`is_file` guard → RuntimeError → 2 as before).
- Self-test git-absent arm supplies `python3` in the scratch PATH only so the script invocation works; `sys.executable` is absolute. Sound.

# Verdict
No falsifying finding. The patch is confined to could-not-evaluate paths and self-test arms; judging, red detection, and verdict lines are untouched and behavior-verified at a red revision, at both pinned revs, and across `--root` forms with and without git.

Report: .ufo/waves/round-55/falsify/ReviewFixCorrectionSweep.md
