# ExecW2E2Patch

role: leaf executor (wave-2 falsify) — draft the C2-hardening patch as report content; **no lane writes**
item: draft the exact C2-hardening patch (argparse/base-arm code with `BASE_REV` pinned in-code, three
self-test arms, plan erratum E2 paragraph) and verify it in `/tmp`; the L1 decides adoption.
Axes exercised: calibration (does the counter measure what it prints), depth (does the predicate bind
the computation at all).

Lane bounds honoured: this seat wrote **only this report file**. Every probe ran on `/tmp` copies or
revision-pinned `git show`/`ls-tree` reads. The lane's `git status --porcelain` is unchanged from the
pre-seat state (6 untracked entries, all pre-existing: `w2-dispatch.err`, `w2-dispatch.json`,
`w2-spec.json`, `w2/`, `receipts.new-C1.txt`, `receipts.new-C2-interim.txt`). No lane file, no
sibling lane, no jj state and no lane Git index was touched.

Tools installed: **none** (no `pacman`, no `uv`, no `npx`, no binary download). The `pacman` pause
was not exercised because nothing needed installing; Python 3 and `git` were already present.

---

## 1. Baseline measured at the committed tip (cbbee56e)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ git log --oneline -3
cbbee56 round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32), r62 routed-repairs counter, S119 + entry, LOG corrections (defects 1-4), w1 evidence
8c4cefa round-63: plan freeze and C1 do-nothing control (v31 5 of 6), census-before
35d44b4 round-62 verifier spot-check (integrator, hyaku): non-author admit/reject

$ python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
exit=1

$ python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
exit=0

$ python3 -B verifiers/check_r63_routed_repairs.py --self-test
self-test: 0 failure(s) over 15 assertions
exit=0
```

Committed bytes, sha256:

```
5a15feac0358fd537ad3a54cad589fa5f41743971e02f9d3e742fa4c3528c6ec  verifiers/check_r63_routed_repairs.py
4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33  verifiers/check_scoped_rules_v32.py
```

---

## 2. The attack I ran — three mutants against the frozen predicate (RED-BEFORE)

Inputs: `RevCalibChecks` F1 (label-only process counter), F2 (fingerprint counter), and
`MutCalibInstrument` M1 (worktree read). I rebuilt each as a standalone program in `/tmp/r63e2/` and
ran it against the **committed** counter's own revisions. Transcript: `/tmp/r63e2/red-before.txt`
(produced by `/tmp/r63e2/redbefore.py`).

### RED-BEFORE 1 — label-only process counter

```
$ python3 -B mut_label_only.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
r62 routed defects closed 5 of 5
exit=0
$ python3 -B mut_label_only.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e   # the measured tip
r62 routed defects closed 5 of 5
exit=0
$ python3 -B mut_label_only.py --rev garbage-rev-xyz
r62 routed defects closed 5 of 5
exit=0
```

The frozen predicate ("prints `r62 routed defects closed 5 of 5` and exits 0") is satisfied by a
counter that opens no file and reads no byte — at the base rev, at the tip, and at a revision that
does not exist. **NOT KILLED by the predicate as written.**

### RED-BEFORE 2 — fingerprint counter

```
$ python3 -B mut_fingerprint.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05   # the r62 tip
r62 routed defects closed 0 of 5
exit=1
$ python3 -B mut_fingerprint.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e   # the measured tip
r62 routed defects closed 5 of 5
exit=0
```

**This is the load-bearing finding for the patch design.** At the r62 tip the fingerprint prints
`0 of 5` and exits nonzero — it *satisfies* a base-arm conjunct. A base arm alone therefore does
**not** kill this class (RevCalibChecks F5 says the same). Only a **mid-score (look-alike)**
revision separates it from the honest counter. My patch therefore adds a third arm: a `partial`
world (late-write path committed, LOG appended, no correction naming a measured value) where the
honest counter scores `2 of 5` and the fingerprint scores `5 of 5`.

### RED-BEFORE 3 — worktree-read counter (M1)

```
$ python3 -B mut_worktree.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
PASS late-write-tracked   worktree has .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 1 of 5
exit=1
$ python3 -B pre.py --root ... --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
... (all five FAIL)
r62 routed defects closed 0 of 5
exit=1
$ python3 -B mut_worktree.py --root ... --rev cbbee56e9a3589b0b46736ad36f1b77701def80e   # the measured tip
PASS late-write-tracked   worktree has .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
exit=0
```

The lane working tree still holds the late-write file (`-rw-r--r-- 1 vgpnk vgpnk 10224 … FalsifyC2HonestH1.md`),
so a worktree-reading counter reports the defect closed at a revision where it was never committed
(`1 of 5` where the honest counter prints `0 of 5`). The frozen predicate names only a 5-of-5
revision, so this class is **NOT KILLED** by the predicate as written.

### In-file variants (same class, mutated inside the counter file)

`/tmp/r63e2/mutants.py` → `/tmp/r63e2/mutants.txt`; `/tmp/r63e2/infile_fp.py` →
`/tmp/r63e2/infile_fp.txt`:

```
M-A (all five checks stubbed True):
  at the r62 tip : 5 PASS stubs, [stderr] base arm failed … closed 5 of 5, exit=1
  at the tip    : 5 PASS stubs, [stderr] base arm failed … closed 5 of 5, exit=1   ← the patched guard kills it

M-B / in-file fingerprint (CHECKS swapped, run() intact):
  at the tip    : 5 of 5, exit=0   ← still certifies; the self-test is what kills it
  --self-test   : self-test: 2 failure(s) over 21 assertions, exit 1
```

The in-file fingerprint still certifies the tip, so the patch's protection is **two-sided**: the
in-code base guard kills the label-only class, and the self-test's per-arm world kills the
fingerprint and worktree classes.

---

## 3. Deliverable (1) — the exact argparse / base-arm code

Pinned in code, **not** a command-line argument, so no caller can point the control at a revision
the counter would close.

```python
# --- constants (replaces the single R62_TIP line) ---
BASE_REV_LITERAL = "35d44b4b4dcdda234b5dbff7af37e432fec55f05"
# The do-nothing control, pinned in code: the r62 tip, before any of the five
# routed corrections.  BASE_REV is also the append-only baseline (the r62 tip
# IS the revision the corrections are appended to).
BASE_REV = BASE_REV_LITERAL
R62_TIP = BASE_REV_LITERAL

# --- new function, placed just above run() ---
def base_control(root: Path) -> tuple[int, int]:
    """The five checks at the pinned do-nothing control (BASE_REV).

    The control must stay red.  If all five closed there, the counter would
    certify revisions that carry none of the r62 corrections, so the counter
    refuses to certify anything while the control is green.
    """
    closed = 0
    for _, fn in CHECKS:
        ok, _ = fn(root, BASE_REV)
        closed += 1 if ok else 0
    return closed, len(CHECKS)

# --- run(): the two guards ---
def run(root: Path, rev: str) -> int:
    closed = 0
    for name, fn in CHECKS:
        ok, detail = fn(root, rev)
        closed += 1 if ok else 0
        print("%-4s %-20s %s" % ("PASS" if ok else "FAIL", name, detail))
    base_closed, total = base_control(root)
    if base_closed >= total:
        print("base arm failed: the do-nothing control at %s closed %d of %d; "
              "the counter refuses to certify any revision"
              % (BASE_REV, base_closed, total), file=sys.stderr)
        return 1
    print("r62 routed defects closed %d of %d" % (closed, len(CHECKS)))
    if rev.lower() == BASE_REV:
        # the do-nothing control is never a certification
        print("the do-nothing control at %s is never a certification"
              % BASE_REV, file=sys.stderr)
        return 1
    return 0 if closed == len(CHECKS) else 1

# --- argparse: the new flag ---
    ap.add_argument("--base-arm", action="store_true",
                    help="evaluate the pinned do-nothing control (BASE_REV); "
                         "prints its count and exits 0 iff fewer than five "
                         "checks close there (the control is red)")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.base_arm:
        root = Path(args.root).resolve()
        if not (root / ".git").exists():
            print("error: %s is not a git checkout" % root, file=sys.stderr)
            return 2
        closed, total = base_control(root)
        print("base control at %s: r62 routed defects closed %d of %d"
              % (BASE_REV, closed, total))
        return 0 if closed < total else 1
```

Exit codes stay inside the registry's declared verdict map (`0=clean, 1=failed, 2=could-not-evaluate`,
`SKILL.md:492`): the base-arm failure and the base-rev refusal both return **1**, never 3.

The module docstring's frozen-predicate block becomes:

```
Frozen predicate (two conjuncts; both must hold):
  python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>
prints `r62 routed defects closed 5 of 5` and exits 0, AND
  python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
must print `r62 routed defects closed 0 of 5` and must exit nonzero.

The second conjunct is the do-nothing control: the r62 tip, before any of the
five routed corrections.  Its revision is pinned in code as BASE_REV and is
never a command-line argument, so no caller can point the control at a
revision the counter would close.  The counter refuses to certify any
revision while that control is green, and its --self-test carries the counter
arms (label-only, fingerprint, worktree-read) that show the second conjunct
is not satisfied by a counter that prints a headline instead of computing
five checks.
```

### Verified behaviour of the patched counter (in `/tmp`, against the real lane)

```
$ python3 -B /tmp/r63e2/patched.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
exit=1

$ python3 -B /tmp/r63e2/patched.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
exit=0

$ python3 -B /tmp/r63e2/patched.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin --base-arm
base control at 35d44b4b4dcdda234b5dbff7af37e432fec55f05: r62 routed defects closed 0 of 5
exit=0
```

**0 of 5 at base (exit 1) and 5 of 5 at cbbee56e (exit 0)** — as required.

---

## 4. Deliverable (2) — the three self-test arms

The arms run each dishonest counter as a **process** against constructed worlds and require the
frozen predicate to reject it, while requiring the honest counter to pass the same worlds. A
candidate is *this file* with the pinned control revision repointed at the constructed control
commit, so a candidate differs from the honest counter only in the cheating step.

```python
# --- three constructed worlds ---
def _arm_world(root: Path, mode: str) -> tuple[str, str]:
    """Build one constructed world for the counter arms.

    mode "base"    -- the do-nothing control: no corrections, the late-write
                      path never committed.
    mode "partial" -- a look-alike: the late-write path committed and the
                      LOG appended, but no correction names a measured value.
    mode "target"  -- the repaired tree; the late-write path is committed and
                      then removed from the working tree, so a counter that
                      reads the working tree instead of the tree at <rev>
                      scores it differently from an honest one.
    Returns (base_rev, rev).
    """
    _base_tree(root)
    base_rev = _commit(root, "base")
    if mode == "base":
        return base_rev, base_rev
    _write(root, LATE, "seat finding\n")
    base_log = show(root, base_rev, LOG) or ""
    if mode == "partial":
        _write(root, LOG, base_log + "\n## Corrections\n- Correction: below.\n")
        return base_rev, _commit(root, "partial")
    _write(root, LOG, base_log + _corrections(root))
    rev = _commit(root, "target")
    (root / LATE).unlink()
    return base_rev, rev

# --- the process-level predicate evaluator ---
def _candidate_run(cmd: list[str], root: Path, rev: str) -> tuple[int, int]:
    """Run a candidate counter process at <rev>: (returncode, closed count)."""
    proc = subprocess.run(cmd + ["--root", str(root), "--rev", rev],
                          capture_output=True, text=True, timeout=60)
    m = re.search(r"r62 routed defects closed (\d+) of (\d+)", proc.stdout)
    return proc.returncode, (int(m.group(1)) if m else -1)


def audit_counter(cmd: list[str],
                  worlds: list[tuple[str, Path, str, bool]]) -> tuple[bool, str]:
    """Apply the frozen predicate to a candidate counter process.

    A world is (label, root, rev, expect_closed).  With expect_closed True the
    candidate must print `r62 routed defects closed 5 of 5` and exit 0; with
    expect_closed False it must NOT print that count and must exit nonzero.
    The base world is the do-nothing control and the partial world is a
    look-alike revision (the late-write path committed, the LOG appended, no
    correction naming a measured value); only the target world may certify.
    """
    ok = True
    notes = []
    for label, root, rev, expect_closed in worlds:
        rc, count = _candidate_run(cmd, root, rev)
        if expect_closed:
            good = rc == 0 and count == 5
            want = "rc=0 count=5"
        else:
            good = rc != 0 and count < 5
            want = "rc!=0 count<5"
        notes.append("%s: rc=%d count=%d (want %s)" % (label, rc, count, want))
        ok = ok and good
    return ok, "; ".join(notes)

# --- the three arms, added at the end of self_test() ---
            # ---- the counter arms -------------------------------------
            # Three dishonest counters are run as processes against
            # constructed worlds, and the frozen predicate must reject each.
            #   label-only  -- prints the headline for every revision
            #   fingerprint -- reads the LOG blob and the tree, scores no check
            #   worktree    -- reads the working tree instead of the tree at <rev>
            # Each candidate is this file with the pinned control revision
            # pointed at the constructed control commit, so a candidate
            # differs from the honest counter only in the cheating step.
            source = Path(__file__).read_text()
            m1_source = (source[:source.index("def check_late_write(")]
                         + M1_CHECK
                         + source[source.index("def check_receipt_rev("):])

            def candidate(world: Path, name: str, text: str,
                          base: str) -> Path:
                p = world / name
                p.write_text(text.replace(BASE_REV_LITERAL, base))
                return p

            # (arm label, world mode, candidate source, candidate file)
            for arm_label, mode, cand_src, cand_name in (
                    ("label-only", "base", LABEL_ONLY_SRC, "label_only.py"),
                    ("fingerprint", "partial", FINGERPRINT_SRC,
                     "fingerprint.py"),
                    ("worktree-read", "target", m1_source, "worktree.py")):
                world = tmp / ("world_" + mode)
                world.mkdir()
                subprocess.run(["git", "-C", str(world), "init", "-q"],
                               check=True)
                world_base, world_rev = _arm_world(world, mode)
                if mode == "base":
                    worlds = [("base", world, world_base, False)]
                elif mode == "partial":
                    worlds = [("base", world, world_base, False),
                              ("partial", world, world_rev, False)]
                else:
                    worlds = [("base", world, world_base, False),
                              ("target", world, world_rev, True)]
                cand = candidate(world, cand_name, cand_src, world_base)
                ok, detail = audit_counter([sys.executable, str(cand)],
                                           worlds)
                check("counter arm: the %s counter is rejected" % arm_label,
                      ok, False)
                print("      %s: %s" % (arm_label, detail))
                honest = candidate(world, "honest.py", source, world_base)
                ok, detail = audit_counter([sys.executable, str(honest)],
                                           worlds)
                check("counter arm: the honest counter passes the predicate "
                      "in the %s world" % mode, ok, True)
                print("      honest/%s: %s" % (mode, detail))
```

The three candidate sources (`LABEL_ONLY_SRC`, `FINGERPRINT_SRC`, `M1_CHECK`) are inlined in the
file as string constants — verbatim in `/tmp/r63e2/patched.py` (lines 178–227 of the patched file);
`M1_CHECK` replaces `check_late_write` with `tracked = (root / LATE).exists()`.

### GREEN-AFTER — the patched self-test

```
$ python3 -B /tmp/r63e2/patched.py --self-test
      label-only: base: rc=0 count=5 (want rc!=0 count<5)
      honest/base: base: rc=1 count=0 (want rc!=0 count<5)
      fingerprint: base: rc=1 count=0 (want rc!=0 count<5); partial: rc=0 count=5 (want rc!=0 count<5)
      honest/partial: base: rc=1 count=0 (want rc!=0 count<5); partial: rc=1 count=2 (want rc!=0 count<5)
      worktree-read: base: rc=1 count=0 (want rc!=0 count<5); target: rc=1 count=4 (want rc=0 count=5)
      honest/target: base: rc=1 count=0 (want rc!=0 count<5); target: rc=0 count=5 (want rc=0 count=5)
self-test: 0 failure(s) over 21 assertions
exit=0
```

Read the three arm lines: each dishonest candidate **fails** the arm (label-only prints `5 of 5`
at the control; fingerprint prints `5 of 5` at the look-alike; worktree-read prints `4 of 5` at the
target), and each honest counter **passes** the same worlds.

### GREEN-AFTER — the mutants turn the patched self-test red

```
$ python3 -B /tmp/r63e2/mut_infile_fp.py --self-test
        FAIL counter arm: the honest counter passes the predicate in the partial world: got False, expected True
        FAIL counter arm: the worktree-read counter is rejected: got True, expected False
self-test: 2 failure(s) over 21 assertions
exit=1
$ python3 -B /tmp/r63e2/mut_M_A.py --self-test
self-test: 14 failure(s) over 21 assertions
```

### RED-BEFORE transcripts

| arm | transcript | red-before evidence | green-after evidence |
|---|---|---|---|
| label-only process counter | `/tmp/r63e2/red-before.txt` §1 | `5 of 5`, exit 0 at base, tip and `garbage-rev-xyz` | arm RED under the patched self-test (`base: rc=0 count=5`) |
| fingerprint counter | `/tmp/r63e2/red-before.txt` §2 | `0 of 5` at base (satisfies a base arm!) / `5 of 5` at tip | arm RED via the `partial` world (`partial: rc=0 count=5`) |
| worktree-read probe | `/tmp/r63e2/red-before.txt` §3 | `1 of 5` at base vs the honest `0 of 5`; `5 of 5` at tip | arm RED via the `target` world (`target: rc=1 count=4`) |

---

## 5. Deliverable (3) — the plan erratum E2 paragraph

Proposed text for `plans/round-63.md`, appended after Erratum E1. It keeps E1's sentence shape
(one sentence naming the defect, one sentence naming the refinement, one sentence naming the
effect, one sentence naming what is unchanged) and its pre-data discipline.

> ## Erratum E2 (pre-data, declared before any C2 measurement)
>
> `§C2`'s frozen predicate as first written ("`python3 -B
> verifiers/check_r63_routed_repairs.py --rev <rev>` prints `r62 routed defects closed 5 of 5` and
> exits 0") names no revision at which the count must be below five, so a counter that prints that
> constant string for every `--rev` — including a revision that does not exist — satisfies it, and
> so does one that reads the LOG blob without scoring a check. E2 refines the predicate to **two
> conjuncts**, both reported separately: the counter prints `r62 routed defects closed 5 of 5` and
> exits 0 at the measured round-63 revision, **and** the same counter prints `r62 routed defects
> closed 0 of 5` and exits nonzero at the r62 tip `35d44b4b4dcdda234b5dbff7af37e432fec55f05`, a
> revision pinned in the counter's code as `BASE_REV` and never supplied on the command line. The
> base arm alone does not kill the blob-fingerprint class (it prints `0 of 5` at that tip), so the
> counter's `--self-test` additionally carries three arms — a label-only process counter, a
> blob-fingerprint counter and a working-tree-reading counter — each run as a process against a
> constructed world and each required to be rejected by the two conjuncts while the honest counter
> passes. The target and the five checks are unchanged.

**Note for the L1 (a real choice, not a formality).** Erratum E1 was declared *before* the C2
measurement; E2, drafted in wave 2, arrives *after* the wave-1 measurement at `cbbee56e`. `corpus/
QUALITY.md` Q28 says a counter's judgment tables are frozen at the plan commit and a later change is
reported as a **second measurement beside** the declared one, never in its place. Two options:

* **Option A (adopt as written).** E2 is a *hardening of the instrument*, not a re-reading of the
  data: the five checks, their byte computations and the `5 of 5` at `cbbee56e` are unchanged, and
  the base arm's `0 of 5` at `35d44b4b` was already measured and committed at
  `.ufo/waves/round-63/controls/C2-before-r62tip.txt`. The paragraph is then honest as a
  *wave-2 falsify* instrument change, and its header should read
  `## Erratum E2 (wave-2 falsify; the five checks and their measurements are unchanged)`.
* **Option B (strict pre-data).** Keep the header `## Erratum E2 (pre-data, declared before any C2
  measurement)` **only** if the L1 treats the C2 measurement as not yet closed — i.e. the L1 has not
  yet written the round-63 report's C2 receipt, so the C2 measurement is still open and E2 can be
  declared before it is *reported*. This is the reading I recommend, and it is the one the header
  above assumes: the C2 measurement exists in the tree (`cbbee56e`) but no C2 receipt has been
  written yet, so an erratum declared now still precedes the reported measurement.

If the L1 prefers the strict reading, use the header `## Erratum E2 (pre-data, declared before any
C2 measurement is reported)`. Either way the sentence body is unchanged.

---

## 6. Verification performed (all in `/tmp`; the lane was never written)

| check | result |
|---|---|
| patched counter `--rev 35d44b4b…` (base) | `r62 routed defects closed 0 of 5`, exit 1 |
| patched counter `--rev cbbee56e…` (tip) | `r62 routed defects closed 5 of 5`, exit 0 |
| patched counter `--base-arm` | `base control at 35d44b4b…: r62 routed defects closed 0 of 5`, exit 0 |
| patched counter `--self-test` | `self-test: 0 failure(s) over 21 assertions`, exit 0 |
| in-file label-only mutant (M-A) | base arm refuses: exit 1 at both revs |
| in-file fingerprint mutant | `--self-test` → `2 failure(s) over 21 assertions`, exit 1 |
| **v32 self-test untouched** | `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes` / `self-test: 0 failure(s) over 208 assertions`, exit 0; file sha256 `42460691…` unchanged |
| lane `git status --porcelain` | unchanged (6 pre-existing untracked entries) |

Lane verifier battery re-run on a `/tmp` clone at `cbbee56e` with the patched counter committed
(`/tmp/r63e2/clone`): `check_gate_registry` 41 of 41 conformant / phantom 0, `check_command_files`
0 failures over 244 assertions, `check_explicit_invocation` 0/44, `check_gate_finding_delta` 0/13,
`check_correction_sweep` 0/25, `check_sources_append_only` 0/21, `check_agentdef_boxes` 0/109,
`check_assertion_floors` 0/165, `check_hook_files` 0/323, `check_overlap_levers` 55, 
`check_sibling_census` 0/68, `check_substrate_pins` 0/62 — every one exit 0.
`check_gate_registry.py --rev <clone tip>` reports `gate registry rows conformant 41 of 41 lane
verifiers; phantom 0`, so the new `--base-arm` flag does **not** break the `SKILL.md:492` registry
row (`0=clean, 1=failed, 2=could-not-evaluate`; the row's self-test cell names `--self-test`, and
the new flag is additive).

---

## 7. Risks, bounds and what this patch does NOT fix

1. **The patch is a proposal, not an adoption.** The L1 owns `verifiers/check_r63_routed_repairs.py`
   and `plans/round-63.md`. This seat wrote no lane file but this report.
2. **The self-test assertion count changes 15 → 21.** `corpus/knowledge/compound-clause-citation-round63.md:105`
   cites `self-test: 0 failure(s) over 15 assertions`; if the L1 adopts the patch, that citation and
   `SCORECARD.md`/lesson text quoting `15 assertions` must be updated to `21`. Not touched here.
3. **The base arm changes the *predicate*, not the checks.** A counter that ignores `--rev` and
   reads HEAD still satisfies the target conjunct; it does not satisfy the base conjunct only if
   it is honest at `35d44b4b`. The base arm kills *rev-agnostic* printers; it does not by itself
   bind `<rev>` to the round-63 tip. Binding the target revision explicitly (Q28's "a second
   measurement beside the declared one") is a separate L1 decision.
4. **The fingerprint class is killed by the self-test, not by the base arm.** The in-file fingerprint
   still certifies the tip (exit 0) — only `--self-test` turns red. If the L1 wants the *predicate*
   alone to kill it, the plan must additionally name a mid-score revision as a third conjunct; my
   `partial` world shows the mechanism but it is a constructed tree, not a lane revision.
5. **Check 4 (append-only) remains a no-rewrite invariant, not a closure check.** It contributes zero
   discrimination under pure appends, and it cannot detect a rewrite that happened *before* the r62
   tip (`git diff --numstat e6da78bb e424f2a4 -- LOG.md` → `5 4`, RevCalibChecks F4). My patch does
   not change this.
6. **The `--base-arm` exit code is 0 when the control is red.** That is the opposite polarity to
   `--rev` (0 = certified). The L1 should confirm this reads unambiguously against the registry's
   `0=clean, 1=failed` map, or drop the flag entirely — the in-code guard in `run()` already
   delivers the base arm, so `--base-arm` is a convenience, not a load-bearing element.
7. **The `partial` world is a look-alike, not a lane revision.** It is constructed inside the
   self-test's temp repo. It proves the honest counter is strictly stronger than a fingerprint; it
   does not produce a lane revision at which the fingerprint is red.
8. **`check 1`'s substance floor is only "blob size > 0".** A 68-byte placeholder still closes
   check 1 (MutCalibInstrument finding 8). The patch does not change this; a `len(blob) >= 1024 and
   b"R-c" in blob and b"ancestry" in blob` floor is the next tightening and belongs in a separate
   decision.

---

## 8. Artifacts (all under `/tmp/r63e2/`, all disposable)

| file | what it is |
|---|---|
| `pre.py` | verbatim copy of the committed counter at `cbbee56e` (sha256 `5a15feac…`) |
| `patched.py` | the patched counter (sha256 `feda1bdd…`) — the deliverable, **not** in the lane |
| `apply_patch.py` | the deterministic patch script (anchored replacements; re-runnable) |
| `patch.diff` | `diff -u pre.py patched.py` (320 lines) — the exact patch to apply |
| `redbefore.py` / `red-before.txt` | the three RED-BEFORE transcripts against the committed counter |
| `mutants.py` / `mutants.txt` | in-file label-only (M-A) and fingerprint (M-B) mutants |
| `infile_fp.py` / `infile_fp.txt` | in-file CHECKS-swap fingerprint + its red self-test |
| `mut_label_only.py`, `mut_fingerprint.py`, `mut_worktree.py` | the three standalone dishonest counters |
| `clone/` | `/tmp` clone of the lane at `cbbee56e` with the patched counter committed (battery runs) |
| `bat_*.txt`, `floors.txt` | the verifier-battery transcripts |

Reproduce:

```
python3 /tmp/r63e2/apply_patch.py          # rebuilds patched.py from pre.py
python3 -B /tmp/r63e2/patched.py --self-test
python3 /tmp/r63e2/redbefore.py             # the three red-before transcripts
python3 /tmp/r63e2/mutants.py               # in-file mutants
python3 /tmp/r63e2/infile_fp.py             # in-file CHECKS-swap fingerprint
```

---

## Verdict

**ATTACKS the C2 instrument's calibration.** The committed counter's five checks compute honestly
from committed bytes, and its `--self-test` is green at `cbbee56e` — but the **frozen predicate**
admits a constant-label counter at every revision (including a nonexistent one), a blob-fingerprint
counter, and a working-tree-reading counter; the base rev alone does not kill the fingerprint class,
and the worktree class differs from the honest counter at the base rev (`1 of 5` vs `0 of 5`) with
no predicate clause noticing. The smallest safe correction is the patch in §3–§5: pin `BASE_REV` in
code and make it the predicate's second conjunct, refuse to certify while that control is green,
and add three process-level self-test arms (label-only / fingerprint / worktree-read) each required
to be rejected while the honest counter passes, plus the plan erratum E2 paragraph.

**Verified green in `/tmp`:** patched counter `0 of 5`/exit 1 at `35d44b4b…`, `5 of 5`/exit 0 at
`cbbee56e…`, `--self-test` `0 failure(s) over 21 assertions`; the v32 self-test still prints
`survivors closed 6 of 6` and `0 failure(s) over 208 assertions` with its file sha256 unchanged;
the lane's own verifier battery is 41/41 conformant with the patch applied in a `/tmp` clone.

**Bounds carried forward** (see §7): the fingerprint class is killed by the self-test rather than by
the predicate alone; the patch does not bind `<rev>` to the round-63 tip; check 4 remains a
no-rewrite invariant; the assertion count moves 15 → 21 and every citation of `15 assertions` must
be updated on adoption.

Report: .ufo/waves/round-63/w2/ExecW2E2Patch.md
