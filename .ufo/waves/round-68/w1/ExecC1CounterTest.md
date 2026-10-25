# ExecC1CounterTest — round 68 wave 1, executor seat (C1 counter `--self-test` arm)

**Deliverable:** `.ufo/waves/round-68/w1/drafts/check_client_trust_gates.py` (573 lines) — the
full C1 counter with the required `--self-test` arm, ready for the L1 to install over
`verifiers/check_client_trust_gates.py` (clean cutover; nothing else in the lane tree was
written).

## What the self-test arm does

- **Hermetic.** Synthesizes ONE honest world and the named broken worlds inside a single
  `tempfile.TemporaryDirectory(prefix="k68-selftest-")`. It never reads the lane tree, never
  touches the network, never runs a mutating git command (the only git use is `git init -q`
  inside the scratch dir, for the unknown-revision pin). Fixtures use synthetic clients
  `S701–S705` on `.example` hosts that cannot collide with the lane registry.
- **Drives the public paths.** Every world is measured twice: directly via `check(root)` and
  through the public `main(["--repo", world])` with both streams captured (exit code + the
  frozen verdict line).
- **The honest world** asserts `check() == (5, [])` and `main()` exit 0 printing
  `client trust gates backed 5 of 5`.
- **One broken world per named conjunct break** (the task header says "9"; its own list
  enumerates ten — all ten implemented, one world each):
  `entry-missing`, `no-source-line`, `id-does-not-resolve`, `row-not-mined`,
  `source-cell-absent`, `no-verified-at`, `no-recheck`, `no-coverage-row`,
  `quote-absent-from-anchor`, `client-name-absent`. Each must yield backed `0 of 5`, findings
  nonempty, exit 1, and the printed line `client trust gates backed 0 of 5`.
- **Classification pins** (the r67 lesson, routed defect R67-1):
  - (a) missing entry: `main()` exits **1**, prints `client trust gates backed 0 of 5`, and
    `environment error` appears **nowhere** in the output (content verdict, not env error);
  - (b) unknown revision: `main(["--rev", "f"×40, "--repo", <scratch git repo>])` exits **2**
    with `environment error` in the output.
- **Output contract:** prints `self-test: N failure(s) over M assertions` and exits 0 only
  when no failure. Current tally: **49 assertions** (4 honest + 10×4 worlds + 3 class-a +
  2 class-b).
- **Regression tripwire built in:** every fixture `source:` line carries a quoted section name
  (`the "Gates" section`) that occurs in the row's anchor cell but not in the table row. Under
  first-match quote selection (`matched[0]` — an earlier revision of the landed counter) the
  honest world fails; under the current longest-match selection (`max(matched, key=len)`) it
  passes. The honest-world assertion therefore pins the selection logic for free.

## Two real defects the self-test caught on its own first run

1. **Conjunct 7's client-cell half was vacuous** (first self-test run:
   `FAIL client-name-absent/count: got 5 want 0`). `_split_row` popped a leading empty cell, so
   an emptied client cell (`| | quote | S705 |`) collapsed into a shape whose first cell was
   the gate text — the named break survived at 5 of 5. **Fix (the draft's only semantic change
   to the landed `check()` path):** `_split_row` no longer drops the leading empty; only the
   trailing `|` padding is dropped. Blast radius verified: honest rows, README index rows, and
   `_source_rows` (own splitter) are unaffected — see parity evidence below.
2. **`git -C <dir> init` failed in scratch** (`fatal: cannot change to …`) because `-C`
   requires the directory to exist. Fixed by `mkdir` first; init failures now surface the git
   stderr inside the FAIL label instead of crashing.

## Mid-flight reconciliation (the installed file changed during the round)

Between my first read and my measurement, `verifiers/check_client_trust_gates.py` changed
under the L1's hand: quote selection `matched[0]` → `max(matched, key=len)`; verdict gating
tightened to `if global_findings or findings: return 0, …`; `_materialize` now materializes a
rev without the entry instead of raising (making the base control observable as `0 of 5`).
**The draft is aligned to those current landed bytes:** `check`, `fetch`, `_materialize` are
byte-identical (verified by diff; differences are confined to the docstring self-test section,
two stdlib imports, `_split_row`, and the replaced `_world`/`selftest`/`main` default-repo +
`--rev`/`--self-test` guard, r66 house pattern). `--repo` now defaults to the first ancestor
holding `corpus/SOURCES.md`, so the same file runs from `drafts/` and installs unchanged at
`verifiers/`.

## Evidence (commands run at the lane root; quoted output verbatim)

```
$ python3 -B .ufo/waves/round-68/w1/drafts/check_client_trust_gates.py --self-test
PASS honest world: backed 5 of 5
PASS broken world rejected: entry-missing
… (8 more PASS lines, one per broken world) …
PASS broken world rejected: client-name-absent
self-test: 0 failure(s) over 49 assertions
selftest-exit=0

$ python3 -B .ufo/waves/round-68/w1/drafts/check_client_trust_gates.py          # worktree
client trust gates backed 5 of 5          (draft-worktree-exit=0)
$ python3 -B .ufo/waves/round-68/w1/drafts/check_client_trust_gates.py --rev e94ae32a5cd8dc3ee8e2d247816784bec2750cc0
client trust gates backed 0 of 5          (draft-base-exit=1)
  - entry missing: corpus/knowledge/client-trust-gates-round68.md
$ python3 -B verifiers/check_client_trust_gates.py                               # installed, for parity
client trust gates backed 5 of 5          (installed-worktree-exit=0)
$ python3 -B verifiers/check_client_trust_gates.py --rev e94ae32a5cd8dc3ee8e2d247816784bec2750cc0
client trust gates backed 0 of 5          (installed-base-exit=1)
$ python3 -B .ufo/waves/round-68/w1/drafts/check_client_trust_gates.py --rev ffff…ff
environment error: cannot read corpus/SOURCES.md at ffffffffffffffffffffffffffffffffffffffff
unknown-rev-exit=2
$ python3 -B .ufo/waves/round-68/w1/drafts/check_client_trust_gates.py --self-test --rev deadbeef
check_client_trust_gates.py: error: --self-test cannot be combined with --rev
guard-exit=2
```

First-run failures (kept as the record of what the arm is for): `self-test: 5 failure(s) over
48 assertions`, exit 1 — the four `client-name-absent` gate failures and the git-init setup
failure quoted above.

## Bounds kept

Wrote only `drafts/check_client_trust_gates.py` and this report, both under
`.ufo/waves/round-68/`. No writes to `verifiers/`, `corpus/`, or any tracked lane file; no
mutating git/jj command; no pacman; no network (the `--fetch` arm is unchanged and not
exercised by the self-test — it is the L1's separate live-page measurement). Stdlib only:
`argparse, contextlib, io, re, subprocess, sys, tempfile, urllib.error, urllib.request, pathlib`.

## Remaining risks / handoff notes for the L1

- **Accept the `_split_row` delta.** It is the one behavioral change to the landed counter; it
  makes conjunct 7's client-cell check real. Without it the self-test cannot honestly exit 0 —
  the named `client-name-absent` world survives the landed parser. Verified no regression on
  the real tree (worktree `5 of 5` exit 0, base `0 of 5` exit 1, both before/after).
- **Spec arithmetic:** the task says "9 broken worlds" but enumerates ten; all ten are
  implemented (over-coverage, no harm). If the L1 wants exactly nine, dropping one named world
  is a one-line deletion — not recommended.
- The classification (b) pin needs `git` on PATH (a lane hard dependency already); if git were
  absent the self-test reports an assertion failure with the stderr, not a crash.
- No blockers.
