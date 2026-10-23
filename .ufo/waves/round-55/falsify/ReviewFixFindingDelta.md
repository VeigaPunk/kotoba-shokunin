# ReviewFixFindingDelta — C2 patch review: `verifiers/check_gate_finding_delta.py`

Result: DONE — The C2 change to `check_gate_finding_delta.py` (a10240c0 → e966cd59, identical to tip f0e6b695) conforms to every checked item: judging lines unchanged, no exit-1→2 remap, self-test arms assert the fixed exit codes (proven by revert/mutation), red anchor still exits 1 on both code versions, real verdict prints the same summary at the same revision, and default/explicit `--repo` forms without git exit 2.

Scope: lane frozen counter `verifiers/check_could_not_evaluate.py` is byte-identical at a10240c0 and tip (`git diff a10240c0 f0e6b695 -- verifiers/check_could_not_evaluate.py` → empty). The patch under review is the whole change to this gate (`git diff a10240c0 e966cd59 -- verifiers/check_gate_finding_delta.py` → 57 insertions, 2 deletions; `git diff e966cd59 f0e6b695 --` for this file → empty). All runs happened in the sandbox clone `/fast/scratch/hyaku/kotoba-r55/ReviewFixFindingDelta` at f0e6b695 (restored and byte-verified afterward: sha256 `c2d5d80b599db71ddfbcd18b184f27e5505df812b36cd5b92f034dcc0d958b48`). No tools installed; no lanes touched besides this report. `date -u` at run time: `Fri 23 Oct 2026 12:15:21 AM UTC`.

## Check 1 — judging lines unchanged (PASS)

The only production changes are additive: `validate_revision()` (git `rev-parse --verify --quiet <rev>^{commit}` precheck raising `CouldNotEvaluate`) called at the top of `run()` (`check_gate_finding_delta.py:99-100`), and `main()` now wraps `run()` in `except (CouldNotEvaluate, OSError, subprocess.CalledProcessError)` → prints `could-not-evaluate: ...` to stderr → returns 2 (`:220-222`). `delta()`, `findings()` (red-list extraction, exit-tracker, `SystemExit(2)` on non-0/1 child exit), `extract()`, `revision_env()`, all `run()` summary prints, and the return `1 if new else 0` are byte-identical to base. The `--self-test` change only adds an assertion counter and new arms; the original nine assertions are untouched.

## Check 2 — no remap of exit 1 to 2 / no catch-all / no keying (PASS)

- The catch tuple is specific and does not include `Exception`; `SystemExit(2)` from `findings()` bypasses it. A real finding (`new` non-empty) returns 1 through the normal path and raises nothing. `CalledProcessError` can only come from the `check=True` git calls in `extract()`/`revision_env()`; `OSError` covers the absent-git `FileNotFoundError`. Both are environment inability, not verdicts.
- No code inspects argv shape, temp-dir names (prefixes `finding-delta.`/`finding-delta-selftest.`/`finding-delta-nogit.` are cosmetic), or PATH strings; `validate_revision` runs unconditionally on both base and head regardless of how they were passed.
- Red anchor proves exit 1 survives both code versions (Check 4).

## Check 3 — self-test arms assert exit codes and fail when the fix is reverted (PASS)

- Tip self-test: `timeout 300 python3 -B verifiers/check_gate_finding_delta.py --self-test` → `self-test: 0 failure(s) over 12 assertions`, exit 0.
- The three new arms (`arm/unknown-base-revision`, `arm/unknown-head-revision`, `arm/git-unavailable`, at `:172-196`) assert `(returncode, stderr.startswith("could-not-evaluate: ")) == (2, True)` for: random 40-hex rev in each slot, and PATH holding only a `python3` symlink with `--base HEAD --head HEAD`.
- Mutation (production fix reverted, new arms kept): removed the two `validate_revision` calls and restored `main()`'s direct `return run(...)`; then `--self-test` → `self-test: 3 failure(s) over 12 assertions` with `FAIL arm/unknown-base-revision: got (1, False), want (2, True)`, `FAIL arm/unknown-head-revision: ...`, `FAIL arm/git-unavailable: ...`, exit 1. The same mutated code returns exit 1 on the actual R probe (`git archive` `CalledProcessError`) and G probe (`FileNotFoundError`), i.e. the arms detect the exact pre-fix behavior.
- Note: an exact revert to the a10240c0 file also reverts the arms; that old self-test passes (`0 failure(s) over 9 assertions`, exit 0). The guard only fires when production is reverted while the arms are kept — inherent to shipping test and fix in one commit; not a defect.

## Check 4 — red anchor: real finding exits 1 at base and stays 1 at tip (PASS)

Anchor `--base e3371548 --head a10240c0` (from `build/CriticC2Sizing.md:26`):

- Base code (a10240c0 bytes, `/tmp/base_gate_fd.py`): `gate finding delta e3371548 -> a10240c0: base drift 3, head drift 5; new: corpus.pointers.commit_total, corpus.pointers.commit_unresolvable; resolved: none; finding delta: new 2, resolved 0` → exit 1.
- Tip code: byte-identical output → exit 1.

## Check 5 — real verdict (V) prints the same summary (PASS)

- Base code at f0e5de82→f0e5de82: `base drift 5, head drift 5; new: none; resolved: none; finding delta: new 0, resolved 0`, exit 0.
- Tip code at the same f0e5de82→f0e5de82: byte-identical summary, exit 0 — the code change does not alter the verdict.
- Tip code at f0e6b695→f0e6b695: `base drift 4, head drift 4; new 0, resolved 0`, exit 0. The drift count differs (5 vs 4) because the measured revision itself changed (that revision's own `verify_corpus_integrity.py`/baseline), not because of the patch; the predicate-relevant line `finding delta: new 0, resolved 0` and the exit are identical at both measured revisions.

## Check 6 — default/`--repo` forms without git keep the could-not-evaluate exit (PASS)

With PATH set to a dir holding only a `python3` symlink (`env PATH=/tmp/nogit-bin`):

- Default form (no `--repo`, cwd = clone): tip code → `could-not-evaluate: [Errno 2] No such file or directory: 'git'`, exit 2. (The gate exposes `--repo`, not `--root`; there is no `--root` argument.)
- Explicit `--repo`: same stderr line, exit 2.
- Base code, default form: `FileNotFoundError` traceback, exit 1 — the pre-fix miss the patch corrects.

## Counter-probe replication (this gate's five frozen lines)

Counter commands replicated exactly (`check_could_not_evaluate.py:66-70`, `:124-136`): R probes (unknown 40-hex `67bebe0c70ccc926f98108adb36ec962e5c593b2`, verified absent via `git cat-file -e` failing) in both `--base` and `--head` slots → exit 2 with `could-not-evaluate:` stderr; G probe (git absent) → exit 2; S → exit 0; V → exit 0. Matches the committed measurement receipt `.ufo/waves/round-55/C2-measure-e966cd59.txt:9-13` (all five lines `ok`).

## Residual risk / verification gaps

1. The `OSError` branch could in principle convert a computed real finding to 2 if an OSError fired after `delta()` (e.g. tempdir cleanup failure); unreachable by the counter's probes and not realistic on this filesystem. Worth knowing, not a defect.
2. `ValueError` (`json.loads`) and other non-OSError crashes are not caught and still exit 1 via traceback, matching base; out of the frozen R/G scope.
3. I did not re-run the whole 25-probe counter; this gate's five lines were exercised directly with the counter's own argument shapes and environment mechanics, and the committed tip receipt shows all five `ok`.
