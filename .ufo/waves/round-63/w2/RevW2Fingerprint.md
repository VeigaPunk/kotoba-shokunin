# RevW2Fingerprint

role: reviewer (UFO-FSD, wave-2 falsify; judged on calibration)
item: Attack the fingerprint-counter class (RevCalibChecks F2): a counter keyed on
`git rev-parse <rev>:LOG.md` differs from base's blob AND late-write path tracked passes
the plan's honest-computation clause while scoring nothing. Rebuild in /tmp; show base
`0 of 5`, tip `5 of 5` on a token-free synthetic fix (synthetic commits via
`GIT_OBJECT_DIRECTORY` alternates in /tmp, no lane writes). Decide: does the L1 need a
fingerprint-kill arm (mid-score fixture scoring strictly 1–4 of 5 printing its true
count), or is the base arm plus an honest-computation self-test sufficient? Draft the
exact self-test fixture code if recommended.

## Findings

### F1 — The fingerprint class is rebuilt and it beats every committed enforcement mechanism, including `--self-test`.

The committed counter `verifiers/check_r63_routed_repairs.py` (sha256
`5a15feac0358fd537ad3a54cad589fa5f41743971e02f9d3e742fa4c3528c6ec`, tip
`cbbee56e9a3589b0b46736ad36f1b77701def80e`) enforces honesty at three points:

1. the frozen predicate itself: `--rev <tip>` must print `r62 routed defects closed 5 of 5`, exit 0;
2. the base arm (r62 tip `35d44b4b…` must score `0 of 5`, exit 1 — verified below);
3. `--self-test`: **15 assertions, every one of them on `check_*` functions called directly** (`check_late_write(base, base_rev)`, `{name: fn(base, repaired_rev)[0] …}`, etc., `verifiers/check_r63_routed_repairs.py:244-338`). `run()` — the function the frozen predicate's CLI actually executes (`main → run`, `:365-366`) — is never invoked, the printed headline is never captured, and the exit status is never asserted.

So the honest-computation clause binds only the check *library*, not the published *command*. The whole seam is one function. My attack replaces exactly `run()` in a byte-identical copy of the committed file — every `check_*` function, the `CHECKS` table, `self_test()` and `main()` are untouched — with a 10-line fingerprint. Full verbatim diff (the only difference between the two files):

```diff
--- verifiers/check_r63_routed_repairs.py (committed, sha256 5a15feac…)
+++ /tmp/r63fp/verifiers/check_fingerprint.py (sha256 7d1c18fc…)
@@ -169,13 +169,17 @@
 def run(root: Path, rev: str) -> int:
-    closed = 0
-    for name, fn in CHECKS:
-        ok, detail = fn(root, rev)
-        closed += 1 if ok else 0
-        print("%-4s %-20s %s" % ("PASS" if ok else "FAIL", name, detail))
-    print("r62 routed defects closed %d of %d" % (closed, len(CHECKS)))
-    return 0 if closed == len(CHECKS) else 1
+    """Fingerprint counter (RevCalibChecks F2): every check_* function above is
+    intact and honest -- only run() is replaced.  It never calls CHECKS; it
+    scores 5 iff the rev's LOG.md blob differs from the base blob AND the
+    late-write path is tracked at <rev>.  Both facts are computed from
+    committed bytes, so the plan's honest-computation clause is met."""
+    base_log = git(root, ["rev-parse", "%s:%s" % (R62_TIP, LOG)]).stdout.strip()
+    rev_log = git(root, ["rev-parse", "%s:%s" % (rev, LOG)]).stdout.strip()
+    tracked = bool(git(root, ["ls-tree", "-r", rev, "--", LATE]).stdout.strip())
+    n = 5 if (rev_log != base_log and tracked) else 0
+    print("r62 routed defects closed %d of %d" % (n, len(CHECKS)))
+    return 0 if n == len(CHECKS) else 1
```

This is strictly worse than RevCalibChecks's wave-1 sketch: that counter had no
`check_*` functions at all, so its `--self-test` would not have existed. Mine keeps the
committed file's entire honest library, so it **passes the committed `--self-test`
verbatim** — see output below.

### F2 — Synthetic token-free fix revs, built with zero lane writes.

Object store: `/tmp/r63fp/objects` (empty dir). Construction ran with
`GIT_DIR=$LANE/.git`, `GIT_OBJECT_DIRECTORY=/tmp/r63fp/objects`,
`GIT_ALTERNATE_OBJECT_DIRECTORIES=$LANE/.git/objects`, `GIT_INDEX_FILE=/tmp/r63fp/index`
(removed afterward). Recipe:

```sh
BLOG=$(git hash-object -w --stdin <<< "synthetic w2 seat finding — token-free evidence bytes.")
git show 35d44b4b…:LOG.md > base.log
cat base.log > mid.log
printf '\n## Corrections (synthetic, token-free)\n- correction: bookkeeping only, names nothing.\n- correction: bookkeeping only, names nothing.\n' >> mid.log
BLOB=$(git hash-object -w mid.log)
git read-tree 4d442e432a02f87c2c2ae4aa22ceb641baf94fb5   # base tree
git update-index --add --cacheinfo 100644,$BLOG,.ufo/waves/round-62/w2/FalsifyC2HonestH1.md
git update-index --cacheinfo 100644,$BLOB,LOG.md
TREE_MID=$(git write-tree)                               # b0e2bb5ebcce1934e4e2d7cfcd2c804b8c83b295
MID=$(git commit-tree $TREE_MID -p 35d44b4b… -m 'synthetic token-free fix (fingerprint lookalike)')
# TWIN: from $TREE_MID, add notes/unrelated.txt ("unrelated scratch note, contents A."),
# commit-tree -p $MID → child of MID with unrelated perturbation
```

Resulting revs (objects live only in `/tmp/r63fp/objects`; the lane resolves them only
while `GIT_ALTERNATE_OBJECT_DIRECTORIES` is exported — no ref, index, or object in the
lane was touched, verified at the end of this report):

```
MID  = 93d45502f25b49856c8bcc31f19c309f48dc92be   (parent 35d44b4b; tree b0e2bb5e…)
TWIN = d036fa4972db59acada34d95e47011e40d8a9ea4   (parent MID;     tree 10c70d2a…)
```

MID is exactly the attack's "token-free synthetic fix": it tracks a non-empty blob at
the late-write path (check 1 evidence) and appends four LOG lines naming **none** of the
required tokens — no `receipt_rev` hex, no `64`/`1044`+entry-path line, no
`reg_gate`/`corpus-idx`/`36 of 38` line.

### F3 — Measured matrix (verbatim outputs; all runs against the committed counter and the fingerprint copy).

Environment for `--rev` runs: `GIT_ALTERNATE_OBJECT_DIRECTORIES=/tmp/r63fp/objects`
exported, `GIT_DIR`/`GIT_OBJECT_DIRECTORY`/`GIT_INDEX_FILE` unset. Fingerprint runs pass
`--root $LANE` because the copy lives outside `verifiers/` (the in-lane twin of this file
would need no flag — same `run()` signature and CLI).

Committed (honest) counter, `python3 -B verifiers/check_r63_routed_repairs.py --rev <r>`:

```
@ 35d44b4b (base, do-nothing):
FAIL late-write-tracked   not a tracked blob at 35d44b4b…
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5            exit=1

@ cbbee56e (tip):
PASS late-write-tracked   tracked at cbbee56e…
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5            exit=0

@ MID (synthetic token-free fix):
PASS late-write-tracked   tracked at 93d45502…
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
PASS append-only          prefix=True grew_by=4 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 2 of 5            exit=1

@ TWIN (MID + unrelated file):
PASS late-write-tracked / FAIL receipt-rev-named / FAIL entry-size-named /
PASS append-only (grew_by=4) / FAIL noharm-arms-named
r62 routed defects closed 2 of 5            exit=1
```

Fingerprint counter (identical file except `run()` above), same four revs:

```
@ 35d44b4b:  r62 routed defects closed 0 of 5   exit=1     ← base arm cannot discriminate
@ cbbee56e:  r62 routed defects closed 5 of 5   exit=0     ← FROZEN PREDICATE SATISFIED
@ MID:       r62 routed defects closed 5 of 5   exit=0     ← honest: 2 of 5  ✗
@ TWIN:      r62 routed defects closed 5 of 5   exit=0     ← honest: 2 of 5  ✗
```

And the decisive run — the fingerprint copy under the committed file's own self-test:

```
$ python3 -B /tmp/r63fp/verifiers/check_fingerprint.py --self-test
self-test: 0 failure(s) over 15 assertions
exit=0
```

A counter that calls **zero** of the five named checks passes the honest-computation
self-test with a clean score, because the self-test binds the library functions it never
calls. This is the strongest form of F2: not "a fingerprint could be written" but "here
is one, diff-minimal against the committed bytes, satisfying the predicate, the base
control, and every assertion the committed self-test makes."

### F4 — Verdict on the committed bytes.

**ATTACKS — the fingerprint-kill arm is REQUIRED; base arm + current self-test is
provably insufficient.** Reasoning:

- The base arm splits only `{0 of 5}` from `{≥1}`; the fingerprint prints `0` at base.
- The frozen predicate's `where`-clause ("each of the five checks is computed from
  committed bytes at `<rev>`") is unenforced prose — nothing executes it — and the
  fingerprint even satisfies its *letter*: it computes two byte-derived facts from
  committed bytes. It scores nothing about the named five defects.
- `--self-test` binds `check_*` in isolation only. Any `run()`/`main()`-level
  composition cheat — fingerprint, memorized-sha lookup, transcript — is unmeasured.
  (This also means MutW2-level check-function mutants are the *wrong layer* for this
  class: the attack isn't inside a check, it replaces the harness.)
- The discriminator that kills the class is an end-to-end fixture the cheat cannot
  shortcut: a rev whose true count is **strictly 1–4** (MID measures `2 of 5`), run
  through `main()`/`run()` so the printed count, the per-check lines, and the exit
  code are all asserted — plus a fresh-twin whose commit SHA is per-run random so a
  memorized-fixture-sha table cannot survive.
- Why a *mid-score* fixture rather than more base-style arms: the fingerprint returns
  the extremal values `{0,5}`; any arm whose expected answer is 0 or 5 cannot see it.
  Only an interior expected count forces the cheat to actually evaluate the linkage
  checks. A shortcut scoring anything ≠ 2 on MID dies; one scoring exactly 2 on MID and
  TWIN and 0 at base and 5 at tip has re-implemented all five checks — at which point it
  is the counter.
- Placement: inside `--self-test`, with the caveat that `--self-test` is **not part of
  the frozen predicate**; its binding force is the report carrying the self-test
  transcript/exit as a C2 receipt line (the wave-1 convention already produces
  `receipts.new-C2-interim.txt`). Recommend the receipt name the arm's assertion count
  so the run is observable in the claim's evidence, mirroring r62 v2's
  `fingerprint lookup rejected=True (8 memorized inputs)` receipt line
  (`.ufo/waves/round-62/C2-successor-measure.txt`).

## Smallest safe correction — exact proposed text (drafted, not integrated)

Add `import os` to `self_test()`'s import block (`:223-224`, next to
`import shutil`/`import tempfile`) — needed for the fresh-twin nonce.

Add a helper directly after `run()` (after `:178`), self-contained with
function-local imports matching the file's existing style:

```python
def _run_capture(root: Path, rev: str) -> tuple[int, int | None, str]:
    """Drive the public CLI path (argparse -> main -> run) in-process and return
    (exit status, printed count, stdout).  Asserting on check_* functions alone
    binds the library, not the published command; this binds the command."""
    import io
    from contextlib import redirect_stderr, redirect_stdout

    stdout = io.StringIO()
    stderr = io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        status = main(["--rev", rev, "--root", str(root)])
    match = re.search(r"^r62 routed defects closed (\d+) of 5$",
                      stdout.getvalue(), re.M)
    return status, (int(match.group(1)) if match else None), stdout.getvalue()
```

Add the arm inside `self_test()`'s `try:` after the `empty-late-write` check
(`:337-338`), before `finally:`:

```python
            # fingerprint-kill arm (RevCalibChecks F2 / RevW2Fingerprint): the
            # published command itself must print a true mid-range count.  A
            # counter that passes every check_* assertion above can still print
            # any headline it likes if run() never calls CHECKS -- this arm is
            # the only one that executes run().
            _write(base, LOG, base_log + "\n- bookkeeping only, names nothing.\n")
            _write(base, LATE, "seat finding\n")
            mid_rev = _commit(base, "mid-score")
            check("fingerprint-kill: run() prints a true mid-range count",
                  _run_capture(base, mid_rev)[:2], (1, 2))
            check("fingerprint-kill: run() reports the failing linkage checks",
                  all("FAIL %s" % name in _run_capture(base, mid_rev)[2]
                      for name in ("receipt-rev-named", "entry-size-named",
                                   "noharm-arms-named")), True)
            # fresh twin: an unpredictable un-looked-up rev must score the same,
            # so a memorized-fixture-sha table cannot survive.
            nonce = os.urandom(4).hex()
            _write(base, "notes/r63-st-%s.txt" % nonce, "unrelated %s\n" % nonce)
            twin_rev = _commit(base, "fresh twin")
            check("fingerprint-kill: a fresh rev scores the true count",
                  _run_capture(base, twin_rev)[:2], (1, 2))
```

Expected counts, honest counter on that fixture: check 1 PASS (non-empty LATE blob),
checks 2/3/5 FAIL (the appended line names no receipt token, no entry sizes, no
reg_gate/corpus-idx count), check 4 PASS (proper append under the patched `R62_TIP =
base_rev` already in scope at `:276-278`) → `2 of 5`, exit 1. The fixture mirrors the
measured lane result at MID (`2 of 5`, F3), so the arm's expected values are not
invented — they are the honest counter's output on the same tree shape.

Validation of the proposed text (verbatim, applied to /tmp copies):

```
$ python3 -B /tmp/r63fp/verifiers/check_armed.py --self-test            # honest + arm
self-test: 0 failure(s) over 18 assertions          exit=0
$ python3 -B /tmp/r63fp/verifiers/check_fingerprint_armed.py --self-test # fingerprint + arm
FAIL fingerprint-kill: run() prints a true mid-range count: got (0, 5), expected (1, 2)
FAIL fingerprint-kill: run() reports the failing linkage checks: got False, expected True
FAIL fingerprint-kill: a fresh rev scores the true count: got (0, 5), expected (1, 2)
self-test: 3 failure(s) over 18 assertions          exit=1
```

The arm raises the assertion count 15 → 18, passes clean on the honest counter,
and kills the demonstrated fingerprint on all three new assertions (mid count,
per-check FAIL lines, fresh-twin). The text above is therefore exercised, not
just drafted.

Residual bounds this arm does not close (stated, not hidden):

- A `run()` that computes honestly for unrecognized revs but hardcodes extremal
  outputs for *recognized* lane trees would still need the honest path for the
  random twin — surviving requires implementing all five checks; the arm reduces the
  surviving cheat class to "is the counter." Full closure of lookup-by-shape wants the
  v2-style refactor (pure `evaluate(blobs)` + invariance/fresh arms on the evaluator
  interface, `verifiers/check_routed_repairs_v2.py:463-535`); that is a larger change
  than needed to kill F2.
- `--self-test` is advisory to the frozen predicate (see above); the arm's force is
  evidentiary, via the receipt line.

## Lane non-mutation receipt

```
$ find $LANE/.git/objects -newer /tmp/r63fp/marker -type f | head   → [no output]
$ git -C $LANE for-each-ref | grep -E '93d45502|d036fa49'           → [no output]
$ git -C $LANE status --porcelain | head
?? .ufo/waves/round-63/w2-dispatch.err
?? .ufo/waves/round-63/w2-dispatch.json
?? .ufo/waves/round-63/w2-spec.json
?? .ufo/waves/round-63/w2/
?? receipts.new-C1.txt
?? receipts.new-C2-interim.txt
```

(Identical to the pre-attack snapshot; `w2/` holds sibling seats' reports plus this one.)
Synthetic objects exist only under `/tmp/r63fp/objects`. One process note for the record:
the construction command's `export GIT_OBJECT_DIRECTORY` leaked into the persistent
shell and briefly shadowed the lane store for two read-only probe runs — caught when
`git cat-file` on the *base* rev failed, env scrubbed (`unset GIT_DIR
GIT_OBJECT_DIRECTORY GIT_INDEX_FILE`), and all reported outputs re-run clean. No lane
writes occurred at any point (writes under `GIT_OBJECT_DIRECTORY` went to /tmp by
construction; verified by the `find` receipt).

## Tools

None installed or upgraded. Probes used system `git 2.56.0` and `python3` stdlib only;
no pacman/uv/npx transactions, so the update-safety gate was not touched.

## Verdict

**ATTACKS the committed counter's enforcement surface (not its check logic).** The five
`check_*` functions are honest and discriminate correctly (F3: base `0/5`, tip `5/5`,
token-free synthetic fix `2/5` — a sane calibration curve). But the fingerprint counter
`check_fingerprint.py` — the committed file with a 10-line `run()` swap — satisfies the
frozen predicate at tip, prints `0 of 5` at base, prints `5 of 5` on a rev honestly
worth `2`, and passes `--self-test` `0 failure(s) over 15 assertions`. The base arm plus
the committed honest-computation self-test is therefore insufficient as adjudged. The
L1 needs the fingerprint-kill arm: the drafted mid-score + fresh-twin fixture executed
through `main()` (proposed text above), plus a C2 receipt line carrying the self-test
result so the arm is observable. I would change my verdict if that arm lands verbatim
or stronger (e.g. the v2 supplied-blobs refactor) and the receipt shows it running.
