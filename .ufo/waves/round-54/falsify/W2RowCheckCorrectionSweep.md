Result: HOLDS — every cell of the `check_correction_sweep.py` registry row matches the script as landed at bf65974; no corrected row text needed.

Seat: KotobaR54.W2RowCheckCorrectionSweep. Sandbox: `/fast/scratch/hyaku/kotoba-r54/KotobaR54.W2RowCheckCorrectionSweep` at 58db81c4 (`git status --porcelain` empty before and after all runs). `git diff bf65974..58db81c4 --stat -- verifiers/check_correction_sweep.py` is empty (only SKILL.md gained the C1 table, +14), so tip behavior is the landed behavior. Row text at bf65974:SKILL.md:445 identical to tip SKILL.md:459; row is the only `verifiers/check_correction_sweep.py` row (grep -c = 1).

## Cell-by-cell

**Entry command `python3 -B verifiers/check_correction_sweep.py --root .` — HOLDS.**
Ran in the clone: exit 0, output `correction sweep: 0 stale block(s)`. Read-only (`--root` mode never writes; `git status` clean after), no network, <1s. Implemented at verifiers/check_correction_sweep.py:196-213 (`--root` → `reader(None, root)` :131-132 → `sweep` :108-122). The section preamble (SKILL.md:449-450) pins "run from the repo root", matching the relative `--root .`.

**Self-test `--self-test` — HOLDS.**
`python3 -B verifiers/check_correction_sweep.py --self-test` → `0 failure(s) over 11 assertions`, exit 0. It is the script's own self-test: argparse flag :201 dispatches to `self_test()` :136-193, which builds isolated `tempfile.TemporaryDirectory` fixture roots (:143-152), runs the real `sweep()` + `reader()` (:153), and asserts expected finding-id lists (`want` vs `ids`, :154-156) across 11 `case()` calls. Not a nested call, not usage text (usage prints only on argparse error, exit 2 — observed).

**Verdict map `0=clean, 1=failed, 2=could-not-evaluate` — HOLDS.**
- 0=clean: :213 `return 1 if bad else 0`; observed exit 0 on the clean tree (above) and `--rev 58db81c4` → exit 0.
- 1=failed: :213 when `bad` non-empty; :193 in self-test. Observed: fixture root with `overlap levers backed 7 of 7 clients` and no declared result → `FAIL r51-c2-readme corpus/README.md:1 stale claim without the declared result` / `correction sweep: 1 stale block(s)`, exit 1.
- 2=could-not-evaluate: :207-209 (`RuntimeError` from :113 `missing %s` → `could-not-evaluate:` stderr, return 2). Observed: `--root` on a dir missing registry files → `could-not-evaluate: missing corpus/README.md`, exit 2; `--rev 0000…` → same, exit 2; argparse errors (no arg, bogus flag, `--self-test --root` mix) all exit 2 → could-not-evaluate per the map.
- Missing/extra codes: no other exit path exists (`main` returns only 0/1/2; `KeyboardInterrupt`=130 would read as could-not-evaluate per preamble "an undeclared nonzero code reads as could-not-evaluate", SKILL.md:449).

**Pinned values `in-file` — HOLDS.**
Expected values are the in-file `REGISTRY` literals (:30-73: stale/declared patterns, `lead` flags) and `SEEDED` (:77-82). No expected value is read from any file; subject files under `--root`/`--rev` are what is graded, not expectations. Counter rule satisfied (`in-file` allowed for a gate; docstring of check_gate_registry.py).

**Write scope `none; self-test fixtures under $TMPDIR` — HOLDS.**
All writes are `Path(t)/…​.write_text` inside `tempfile.TemporaryDirectory()` (:143-152); `--root` and `--rev` modes write nothing. Observed: run with `TMPDIR=/fast/scratch/hyaku/kotoba-r54/tmp-sweep` → exit 0, directory absent after (auto-removed); clone worktree clean throughout; `-B` keeps `__pycache__` off.

**Kind `gate` — HOLDS.**
Verdict script per PROTOCOL.md § Gate standard (kimi-shokunin/skills/shokunin/protocol/PROTOCOL.md:390-392): reads surfaces, compares against committed in-file expected values, can fail (exit 1 observed on a red fixture). Not a probe.

**Owner `kotoba` — HOLDS.**

## Residual observations (not row defects)

1. An uncaught exception also exits 1 — demonstrated: non-UTF-8 subject file → `UnicodeDecodeError` traceback, exit 1, which the map classifies as `failed` though nothing was evaluated (the deliberate could-not-evaluate path :207-209 catches only `RuntimeError`). Every produced code is still declared; the `1=failed` mapping is over-wide for crashes. [INFERENCE] classifying a crash as `failed` rather than `could-not-evaluate` is a small honesty gap shared with most lane Python gates; no row change needed, a lane-owned code fix could wrap `read()` errors.
2. The self-test asserts `sweep()`'s finding ids but never an end-to-end `main()` exit code; the verdict wiring :203-213 is unasserted (a `return 0` regression in `main` would keep `--self-test` green). PROTOCOL's self-test clause (:398-402) says "asserting both the exit code and a stable expected finding-id" — arguably under-met, though the row cell `--self-test` remains accurate and the Erratum-2 guard names only the four previously self-test-less gates.
3. Entry command grades the mutable worktree (`--root .`) where sibling rows mostly pin `--rev <rev>`; the script supports `--rev` (observed exit 0 at tip). Honest as declared; comparability caveat only (PROTOCOL "Two evidences", :403-407).

All eight REGISTRY-named subject files verified present at bf65974 via `git cat-file -e`. No installs used; only git/python3 in the sandbox.
