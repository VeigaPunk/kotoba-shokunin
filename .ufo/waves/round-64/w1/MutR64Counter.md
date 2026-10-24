# MutR64Counter — mutation probe of the r64 C2 routed-repairs counter

Seat: `kotoba-r64.MutR64Counter` (mutation-tester, wave 1). Round 64, 2026-10-24.
Probe target: `plans/round-64.md` §C2 (frozen at `c04fffb`), the counter that must
print `r63 routed defects closed 4 of 4` at the corrected tip and `0 of 4` at the
pinned base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`.

**Result in one line.** The honest minimal counter satisfies both frozen conjuncts
(`0 of 4` exit 1 at base; `4 of 4` exit 0 at a simulated corrected tip). **Two of the
six assigned mutants (M1, M2) survive a plan-conforming self-test, and both survive
against real lane bytes**; M3–M6 are killed, with the killing assertion named in each
case. Exact, test-validated arm text for M1 and M2 is in §5/§6. The probe also
independently measured the plan's check-4 arithmetic defect (the literal `check(`
count is 19 call sites / 20 tokens, the runtime tally 23) before reading it in the
wave-1 erratum E1 now in the working-tree plan.

## 1. Provenance — the counter is SELF-IMPLEMENTED, not the seat's source

`verifiers/check_r64_routed_repairs.py` **does not exist** at probe time:

```
$ ls verifiers/check_r64*
ls: cannot access 'verifiers/check_r64*': No such file or directory
$ grep -rl "check_r64_routed_repairs" --exclude-dir=.git .
./plans/round-64.md
./.ufo/waves/round-64/w1-spec.json
./.ufo/waves/round-64/w1-dispatch.json
```

So there is **no `ExecR64Counter` source to mutate**. I implemented the plan's four
checks minimally on scratch and mutated that — every verdict below is about *that*
implementation, labelled throughout as `MIN`. **The L1 must re-run this probe on the
landed counter (see §9): these verdicts transfer only where the landed self-test has
the same arm inventory.**

| item | value |
|---|---|
| scratch implementation | `/tmp/r64mut/check_r64_routed_repairs_min.py` |
| sha256 | `0786cd803b775e977c98eb546655d29552dcedde617a4ea36d9e9643658edf13` |
| armed variant (both delivered arms) | `/tmp/r64mut/check_r64_routed_repairs_min_arms.py`, sha256 `5450492e6fbdba17f2355a64cf7f2e38685e1990acc0f90ff4be87f321381bbe` |
| mutants | `/tmp/r64mut/mutants/M1.py … M6.py`, `M1armed.py`, `M2armed.py` |
| baseline self-test | `self-test: 0 failure(s) over 18 assertions`, rc 0 |
| armed self-test | `self-test: 0 failure(s) over 20 assertions`, rc 0 |
| lane writes by me | **none** (read-only `git show` / `git log`); the only file I write is this report |

`MIN` designs the four checks as the plan says they must be *computed*, not compared:
check 2 derives the committing revisions with `git log --diff-filter=A --format=%H -1`
and scans only the LOG suffix appended after `BASE_REV`; check 3 parses the `## axes`
table, takes owned rows (`Owned?` cell starts with `owned`), fails closed on a tie, and
requires a suffix line naming the computed lowest axis as a word, `lowest`, and **both**
owned scores; check 4 **materializes** the r63 counter blob into a temp dir, runs
`python3 -B <blob> --self-test`, and parses `over (\d+) assertions` before requiring
`ExecW2E2Patch.md` to name that number. Check 1 tests the marker in the blob.
`BASE_REV` is a module literal; the CLI has no base argument.

Note on §C1's site of truth: the plan file is dirty in the lane working tree during my
probe (` M plans/round-64.md`, +50 lines: erratum E1). E1 is **not mine** and I did not
edit it. My measurements were taken against the four checks as frozen at `c04fffb`;
E1 items 1–2 independently state the same two defects my probes measured (§7/§8), so
the findings below also corroborate E1 before its data.

## 2. Honest counter — both frozen conjuncts hold

Base (real lane repo, read-only; the r63 counter is materialized from a temp copy):

```
$ python3 -B check_r64_routed_repairs_min.py \
    --root /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
FAIL seat-edit-committed    marker 'temporal mismatch' absent at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
FAIL control-revs-named     no appended-suffix LOG line names 8c4cefa, cbbee56 and base 35d44b4b
FAIL lowest-axis-corrected  no appended-suffix LOG line names depth as the lowest owned axis with the scores 9+10
FAIL assertion-count-named  r63 self-test prints 23 assertions; .ufo/waves/round-63/w2/ExecW2E2Patch.md names it: False
r63 routed defects closed 0 of 4
the do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc is never a certification
base_rc=1
```

Simulated tip — scratch clone `/tmp/r64mut/tip` of the lane (clone only; no lane
write), then three commits' worth of corrections in **one** commit
`4a2152b8c47b0064f6f75dd5b9e8dac22eff018c`:

1. copy the lane working-tree `.ufo/waves/round-63/w2/MutW2SplitClauses.md`
   (the seat edit carrying the marker; the r63 routed defect 1);
2. append to `LOG.md` a block whose defect-2 line names
   `8c4cefa8e1b7`, `cbbee56e9a35` and base `35d44b4b`, and whose defect-3 line reads
   ``depth (9) is the lowest owned axis; consistency (10) sits above it``;
3. append to `.ufo/waves/round-63/w2/ExecW2E2Patch.md` the amendment naming
   **23** assertions.

```
$ python3 -B check_r64_routed_repairs_min.py --root /tmp/r64mut/tip \
    --rev 4a2152b8c47b0064f6f75dd5b9e8dac22eff018c
PASS seat-edit-committed    marker 'temporal mismatch' present at 4a2152b8c47b0064f6f75dd5b9e8dac22eff018c
PASS control-revs-named     suffix names 8c4cefa, cbbee56 and base 35d44b4b
PASS lowest-axis-corrected  computed lowest owned axis depth (9) named with 9+10
PASS assertion-count-named  r63 self-test prints 23 assertions; .ufo/waves/round-63/w2/ExecW2E2Patch.md names it: True
r63 routed defects closed 4 of 4
tip_rc=0
```

This is a **simulation of the L1's future bytes**, not the lane tip: it proves the four
checks are jointly satisfiable by a genuine correction block, and that the pinning of
check 4 to the materialized 23 is reachable. The L1 must still run the landed counter
on the landed tip.

## 3. Mutants — verdict table

Each mutant is a minimal textual transform of the same `MIN` source
(`src.count(old) == 1` asserted for every transform); each was run as its own process;
the pristine file was never modified (`sha256` before and after identical, §9).

| # | mutant (behaviour-bearing point) | self-test output | verdict |
|---|---|---|---|
| M1 | `BASE_REV` unpinned: `--base` CLI arg re-binds the module global | `rc=0 self-test: 0 failure(s) over 18 assertions` | **SURVIVED** |
| M2 | check 2 scans the whole LOG blob instead of the appended suffix | `rc=0 self-test: 0 failure(s) over 18 assertions` | **SURVIVED** |
| M3 | check 1 tests blob existence instead of the marker | `rc=1 self-test: 3 failure(s) over 18 assertions` | killed |
| M4 | check 3 hardcodes `depth`/`9`/`10`, axes table unparsed | `rc=1 self-test: 1 failure(s) over 18 assertions` | killed |
| M5 | check 4 hardcodes `tally = 23`, blob never materialized | `rc=1 self-test: 3 failure(s) over 18 assertions` | killed (substantive, see §7 note) |
| M6 | headline printed from a constant (`4 of 4`) + `return 0` | `rc=1 self-test: 3 failure(s) over 18 assertions` | killed |

Killing assertions, verbatim:

```
M3  FAIL base: seat-edit-committed is red: got True, expected False
    FAIL base: the do-nothing control scores 0 of 4: got 1, expected 0
    FAIL worktree: an uncommitted marker leaves check 1 red: got True, expected False
M4  FAIL lowest-axis: a re-ordered axes table fails check 3: got True, expected False
M5  FAIL target: all four checks pass: got {..., 'assertion-count-named': False}, expected {... True}
    FAIL target: the counter scores 4 of 4: got 3, expected 4
    FAIL counter arm: the honest counter passes in the target world: got False, expected True
M6  FAIL counter arm: the honest counter passes in the base world: got False, expected True
    FAIL counter arm: the honest counter passes in the partial world: got False, expected True
    FAIL counter arm: the honest counter passes in the target world: got False, expected True
```

Why each kill is real, not incidental:

- **M3** is killed because the constructed *base* world carries the pre-correction seat
  file (`MARKER` absent, blob present), mirroring the real base where the file exists at
  `38defdc`:
  ```
  $ git show 078eec4:.ufo/waves/round-63/w2/MutW2SplitClauses.md | grep -c 'temporal mismatch'
  0
  ```
  A self-test whose base tree omits the file would let an existence-only check 1 pass
  and M3 survive. **Keep the pre-correction file in the base world.**
- **M4** is killed by the re-order arm (axes table `depth 8` / `consistency 9` while the
  LOG still claims depth lowest with `9`/`10`). A *weaker* arm that only nudges a score
  (`depth 9 → 9.5`) would not kill it: the hardcoded mutant only ever looks for
  `depth`+`9`+`10`+`lowest`, so the arm must move the minimum to another axis.
- **M5** is killed **substantively**: the target world materializes a fixture tally of
  `3` and the patch names `3`, so a `23`-hardcoding check 4 is red at the target while
  the honest one is green. The kill depends on the fixture tally differing from the
  literal `23`; a self-test that uses a copy of the real 23-assertion counter as its
  fixture would let M5 survive. **Keep the fixture tally ≠ 23.**
- **M6** is killed by the plan-mandated label-only arm *and* by the honest-world process
  assertions (the counter must print `count<4` at base/partial and `count=4` at target).

## 4. Surviving mutant M1 — `BASE_REV` from the CLI

Mutant text (the only change from `MIN`):

```python
    ap.add_argument("--base", default=None)   # MUTANT: unpinned control rev
    args = ap.parse_args(argv)
    if args.base:
        globals()["BASE_REV"] = args.base
```

Self-test: `rc=0 self-test: 0 failure(s) over 18 assertions` — **survives**, because
every process arm and every world is driven with `--root`/`--rev` only, and the
`--base` default reproduces the honest behaviour.

Real-byte effect at the frozen base revision (the second conjunct is caller-dependent
once the flag exists):

```
$ python3 -B mutants/M1.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc \
    --base 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL seat-edit-committed    marker 'temporal mismatch' absent at 078eec4a...
PASS control-revs-named     suffix names 8c4cefa, cbbee56 and base 35d44b4b
FAIL lowest-axis-corrected  ...
FAIL assertion-count-named  ...
r63 routed defects closed 1 of 4
rc=1
```

The frozen predicate says the base command "prints `r63 routed defects closed 0 of 4`".
With M1, the same binary prints `1 of 4` when handed `--base`; the control revision is
no longer pinned by the program. (The whole-LOG green at `1 of 4` comes from the r63
corrections line — §5.) Under the working-tree erratum E1 (checks 2–3 anchored to the
round-64 LOG header rather than `BASE_REV`) M1's payoff shrinks to control-anchor drift,
but §C2's sentence "pinned in code as `BASE_REV`, never a command-line argument" is still
unenforced by a self-test.

### Delivered arm M1 (exact, test-validated)

Insert in `self_test()`, inside the existing `for arm_label, mode, cand_src, cand_name`
loop, immediately after `cand = candidate(world, cand_name, cand_src, world_base)`:

```python
                if mode == "target":
                    # M1 arm (MutR64Counter probe): the control revision is
                    # pinned in code; a command-line override must be an
                    # argparse usage error (rc 2), never a silent re-pinning
                    # of the do-nothing control.
                    cli = candidate(world, "cli_probe.py", source, world_base)
                    proc = subprocess.run(
                        [sys.executable, str(cli), "--root", str(world),
                         "--rev", world_rev, "--base", world_rev],
                        capture_output=True, text=True, timeout=60)
                    check("cli: --base is not a counter argument "
                          "(BASE_REV is pinned in code)", proc.returncode, 2)
```

`world`, `world_rev`, `world_base`, `source` and `candidate()` are all already bound at
that point in the r63-style loop. Measured on `MIN` + this arm (source
`check_r64_routed_repairs_min_arms.py`):

```
honest   rc=0 self-test: 0 failure(s) over 20 assertions          (was 18)
M1armed  rc=1 self-test: 1 failure(s) over 20 assertions
         FAIL cli: --base is not a counter argument (BASE_REV is pinned in code): got 1, expected 2
```

## 5. Surviving mutant M2 — whole-LOG instead of appended suffix

Mutant text (check 2 only):

```python
    lines = (show(root, rev, LOG) or "").splitlines()  # MUTANT: whole LOG
```

Self-test: `rc=0 self-test: 0 failure(s) over 18 assertions` — **survives**: every
constructed world's *base* LOG is clean, so whole-LOG and suffix agree on all of them.
The substitution arms change the appended line, not the base LOG.

Real-byte effect — the whole-LOG mutant false-greens check 2 **at the do-nothing base**:

```
$ python3 -B mutants/M2.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
FAIL seat-edit-committed    marker 'temporal mismatch' absent at 078eec4a...
PASS control-revs-named     suffix names 8c4cefa, cbbee56 and base 35d44b4b
FAIL lowest-axis-corrected  ...
FAIL assertion-count-named  ...
r63 routed defects closed 1 of 4
rc=1
```

Cause, measured: `LOG.md` at base already co-locates all three tokens in its
corrections-to-corrections block:

```
$ git show 078eec4:LOG.md | grep -n '8c4cefa' | grep 'cbbee56' | grep '35d44b4b' | cut -c1-120
2576:- **Corrections to this block (appended in round 63; the committed lines above stand).**
$ git show 078eec4:LOG.md | sed -n '2576p' | grep -o '8c4cefa8\|cbbee56e\|35d44b4b' | sort -u
35d44b4b
8c4cefa8
cbbee56e
```

This is exactly the hazard erratum E1 item 1 names ("the r63 corrections-to-corrections
block … already co-locates … so a whole-LOG or r63-suffix scan would false-green check 2
at base"). My probe measured it: the honest suffix scan stays `0 of 4` at base, the
whole-LOG mutant prints `1 of 4`.

### Delivered arm M2 (exact, test-validated)

Insert in `self_test()` **before** the `# ---- counter arms` section (needs `tmp`,
`check`, `_base_tree`, `_commit`, `_write`, `show`, `CONTROLS`, `PINNED_BASE`,
`check_control_revs`, `BASE_REV` — all in scope there):

```python
            # M2 arm (MutR64Counter probe): scope.  A baseline commit whose LOG
            # already names both committing revisions and the pinned base --
            # followed by a rev with NO correction line -- must leave check 2
            # red.  Only lines of the round-64 correction block count; a
            # whole-LOG (or r63-suffix) scan false-greens here.
            pre = tmp / "prenamed"
            pre.mkdir()
            subprocess.run(["git", "-C", str(pre), "init", "-q"], check=True)
            _base_tree(pre)
            c1 = _commit(pre, "control-1")
            _write(pre, CONTROLS[1], "control receipt\n")
            c2 = _commit(pre, "control-2")
            _write(pre, LOG, (show(pre, c2, LOG) or "")
                   + ("\n## Round 63\n- C1-do-nothing-v31.txt committed at %s; "
                      "C2-before-r62tip.txt committed at %s; base %s.\n"
                      % (c1[:10], c2[:10], PINNED_BASE)))
            pinned = _commit(pre, "pinned-baseline")
            _write(pre, LOG, (show(pre, pinned, LOG) or "")
                   + "\n## Round 64\n- unrelated appendix line\n")
            later = _commit(pre, "no-correction")
            saved_pre = BASE_REV
            BASE_REV = pinned
            try:
                check("suffix: a pre-named baseline LOG does not satisfy "
                      "check 2", check_control_revs(pre, later)[0], False)
            finally:
                BASE_REV = saved_pre
```

If the landed counter adopts E1's header anchor (round-64 `##` header, not
`BASE_REV`), keep the same world and change only the assertion's intent: the naming
line sits **before** the round-64 header and must not credit. Measured on `MIN` + this
arm:

```
honest   rc=0 self-test: 0 failure(s) over 20 assertions          (was 18)
M2armed  rc=1 self-test: 1 failure(s) over 20 assertions
         FAIL suffix: a pre-named baseline LOG does not satisfy check 2: got True, expected False
```

(With both arms in one file: `0 failure(s) over 20 assertions`, rc 0 — the two arms
share the honest baseline and add 2 assertions, 18 → 20.)

## 6. What the surviving mutants are NOT

A surviving mutant is a coverage finding, not licence to change the predicate. Both
surviving mutants are defeated by *adding an assertion*, not by weakening §C2: the
`4 of 4`/`0 of 4` headlines, the pinned base and the four computed checks are unchanged.
Do not relax `BASE_REV` into a documented flag "because a test wants one", and do not
justify whole-LOG scans as "equivalent on the measured tree" — M2's base print is direct
evidence they are not.

## 7. Calibration finding — check 4's literal method cannot certify (corroborates E1.2)

Measured at the base revision, on `verifiers/check_r63_routed_repairs.py`:

```
$ git show 078eec4:verifiers/check_r63_routed_repairs.py | grep -o 'check(' | wc -l
20
$ git show 078eec4:verifiers/check_r63_routed_repairs.py | grep -c 'check("'
19
$ python3 -B verifiers/check_r63_routed_repairs.py --self-test | tail -1
self-test: 0 failure(s) over 23 assertions
```

The plan's check-4 sentence says the tally is computed "by counting `check(` invocations
… (expected 23)". The file has **20 `check(` tokens, of which one is the `def`** → 19
call sites. The runtime tally is **23** only because two of those call sites live inside
a 3-iteration `for arm_label, mode, …` loop (17 + 2×3 = 23). Consequences for the L1:

- A literal static count yields 19 (call sites) or 20 (tokens). A counter that hardcodes
  the *static* count as "expected" can never certify the honest correction text — which
  must name **23** — and would report `0 of 4` at the corrected tip. This is the M95
  number-drift class reproduced inside the counter's own specification.
- Therefore check 4 **must materialize** (write the blob at `<rev>` to a temp dir, run
  it with `--self-test`, parse `over (\d+) assertions`), which is what `MIN` does and
  what erratum E1.2 now states. My probe measured `23` this way at base and at the
  simulated tip.
- Keep the static call-site count as a **diagnostic** in the detail line, never as the
  expected value.

Secondary spec detail the L1 will hit when writing the LOG correction: `MIN`'s
`_names()` (and any boundary-tight rule) requires the **pinned base to appear as its own
≥7-hex run**. A LOG line that writes the full 40-hex `35d44b4b4dcd…` has no trailing
non-hex boundary after `35d44b4b`, so the 8-char pinned token is *not* named. The r63
report's own text (the thing being corrected) writes `35d44b4b`; keep that spelling in
the round-64 correction line and put the full rev elsewhere.

## 8. Claims — support / falsify

- **Supports C2's frozen predicate as satisfiable**: `0 of 4` exit 1 at `078eec4`
  (measured), `4 of 4` exit 0 at a simulated genuine correction commit (measured). Both
  conjuncts are reachable by one counter, and the do-nothing control cannot reach the
  target (it prints `0 of 4` and the control-refusal line).
- **Supports erratum E1 item 1** with an executed counter-example: whole-LOG check 2
  prints `1 of 4` at base because LOG:2576 already names `8c4cefa8`, `cbbee56e`,
  `35d44b4b`.
- **Supports erratum E1 item 2** with the arithmetic: 20 `check(` tokens / 19 call
  sites, runtime 23; materialization is the only method that yields the expected 23.
- **Falsifies the plan-v1 check-4 mechanism sentence** ("computes the tally by counting
  `check(` invocations … expected 23"): the literal method cannot produce 23. The frozen
  predicate sentence is untouched; only the mechanism sentence is wrong, and E1.2
  already repairs it.
- **Falsifies "the self-test alone would catch a dishonest counter" for two of the six
  assigned mutant classes**: M1 and M2 survive a self-test with the plan-mandated arm
  inventory (label-only, fingerprint, worktree-read, receipt-side substitutions,
  short-token). The two delivered arms close them (18 → 20 assertions, both mutants red,
  honest green).
- **Does not speak to C1** (the G7 `span_missing` arms): out of this probe's scope.

## 9. Restoration & handoff

Restoration: mutants were written as **separate files** under `/tmp/r64mut/mutants/`;
the pristine probe was never edited in place.

```
pristine sha before: 0786cd803b775e977c98eb546655d29552dcedde617a4ea36d9e9643658edf13
pristine sha after : 0786cd803b775e977c98eb546655d29552dcedde617a4ea36d9e9643658edf13  restored: True
```

Lane state at probe end (unchanged by me; the `M` on `plans/round-64.md` is erratum E1,
authored by another seat, and `w1/` is this wave's evidence tree):

```
$ git status --porcelain | head -8
 M .ufo/waves/round-63/w2/MutW2SplitClauses.md
 M plans/round-64.md
?? .ufo/waves/round-64/snapshots/
?? .ufo/waves/round-64/w1-dispatch.err
?? .ufo/waves/round-64/w1-dispatch.json
?? .ufo/waves/round-64/w1-spec.json
?? .ufo/waves/round-64/w1/
```

No tool installs or upgrades were made (python3 + repo `git` sufficed).

**What the L1 must do with this report**

1. Land both arms (§4, §5) in `verifiers/check_r64_routed_repairs.py`'s self-test; the
   arm texts are validated against a 20-assertion suite (18 + 2). Adjust variable names
   to the landed self-test's scope, not the semantics.
2. Keep `BASE_REV` a module literal and the CLI free of any base argument.
3. Implement check 4 by materialization (E1.2), keep the static call-site count in the
   detail line only, and keep the self-test's fixture tally ≠ 23.
4. Keep the base world's seat file **present and marker-free** (the M3 killer) and the
   axes-table arm's re-order **minimum-moving** (the M4 killer).
5. Re-run this probe on the landed bytes: re-apply M1–M6 as minimal transforms and
   require the landed self-test to exit nonzero for all six (the expected new verdict is
   six killed, 20 assertions).

## 10. Reproduction

```
# honest baseline / armed baseline
python3 -B /tmp/r64mut/check_r64_routed_repairs_min.py --self-test
python3 -B /tmp/r64mut/check_r64_routed_repairs_min_arms.py --self-test

# the six mutants (each its own process; rc printed by the harness)
for f in /tmp/r64mut/mutants/M{1,2,3,4,5,6}.py; do python3 -B "$f" --self-test; echo "$f rc=$?"; done

# honest measurements
python3 -B /tmp/r64mut/check_r64_routed_repairs_min.py \
  --root /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc            # 0 of 4, rc 1
python3 -B /tmp/r64mut/check_r64_routed_repairs_min.py \
  --root /tmp/r64mut/tip --rev 4a2152b8c47b0064f6f75dd5b9e8dac22eff018c   # 4 of 4, rc 0

# the two surviving mutants against real bytes
python3 -B /tmp/r64mut/mutants/M2.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc            # 1 of 4 (false-green check 2)
python3 -B /tmp/r64mut/mutants/M1.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc \
  --base 35d44b4b4dcdda234b5dbff7af37e432fec55f05           # 1 of 4 (control re-pinned)
```

Scratch clone of the simulated tip: `/tmp/r64mut/tip` at
`4a2152b8c47b0064f6f75dd5b9e8dac22eff018c` (disposable; the lane's own bytes are
untouched and the L1's landed correction will differ).
