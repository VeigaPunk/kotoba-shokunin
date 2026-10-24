# RevW2C2Count — round-64 wave 2 (falsify), C2 counter re-run + refuse-to-certify attack

- Seat: `kotoba-r64.RevW2C2Count-2` (independent leaf, no subagent dispatch).
- Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (jj-colocated). Read-only outside this file.
- Measured tip: `c019919c97ab5fe98e87a7754b4449ea4e699c99`; pinned base:
  `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`. Branch head at review: `b99fb79c27042e0f8a598cbbb4d81479a806b518`
  (`git merge-base --is-ancestor c019919 HEAD` → exit 0).
- Canonical runtime: lane worktree, `python3 -B` (Python 3.14.8), counter `verifiers/check_r64_routed_repairs.py`.
  All scratch worlds live under `/tmp/r64-c2-refuse/`; scratch copies were run with an explicit `--root`
  and were never used to measure the lane.
- `lsp` device: **not exposed to this seat** (tool inventory is read/bash/edit/eval/glob/grep/task/wait/web_search/write).
  Caller/definition checks were done by reading the source and by executing it; no semantic-server result is claimed.
- Tools installed: none (pacman paused host-wide; nothing needed).

## Verdict

Both frozen conjuncts reproduce **exactly** at their pinned revisions, the receipt sha256 matches the landed
bytes, and the refuse-to-certify guard is real and load-bearing (demonstrated below). One actionable
falsification: the counter's own 32-assertion self-test **does not pin the "exactly 0 of 4" threshold** —
a mutant relaxed to `base_closed > 1` passes 32/32 and certifies a base that scores 1 of 4 (F1). The landed
code is correct; the self-test cannot catch that regression. F2–F4 are receipt/robustness findings.

## 1. Frozen predicate, re-run (verbatim output)

Conjunct 1 — measured tip:

```
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
EXIT:0
```

Conjunct 2 — pinned base:

```
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
the pinned do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc is never a certification
EXIT:1
```

Cross-checks:
- `--rev` with the tip's **uppercase** hash prints `4 of 4`, exit 0 (rev is lowercased before `run`).
- A **tree** object (`361d2f8f…`, tip tree) prints `3 of 4`, exit 1 — non-commit objects cannot certify.
- Same predicate at current head `b99fb79c…` prints `4 of 4`, exit 0.
- `--base 078eec…` → argparse `error: unrecognized arguments`, **exit 2**; the base is pinned in code only.
- `--self-test` → `self-test: 0 failure(s) over 32 assertions`, exit 0 (reproduces the receipt line).
- `git diff --numstat 38defdc c019919c -- .ufo/waves/round-63/w2/MutW2SplitClauses.md` → `82	29` (E2 floor is 60 added; holds).

## 2. Receipt sha256 and evidence fidelity

```
$ sha256sum verifiers/check_r64_routed_repairs.py
8f5b9f915abe6ae42bf84c4c8842ed341c1e03afc184ca23351f33545e5294bf  verifiers/check_r64_routed_repairs.py
$ git show c019919c…:verifiers/check_r64_routed_repairs.py | sha256sum
8f5b9f915abe6ae42bf84c4c8842ed341c1e03afc184ca23351f33545e5294bf  -
$ git diff --stat c019919c… -- verifiers/check_r64_routed_repairs.py   # (empty)
```

Receipt `.ufo/waves/round-64/receipts/C2-r64-measure.txt` pins `counter sha256: 8f5b9f91…5294bf` — **match**
(worktree and `git show` at the measured tip agree; the file is byte-identical to the measured commit).

The base-conjunct receipt `.ufo/waves/round-64/controls/C2-before.txt` is **byte-identical** to the live
base run (stdout+stderr concatenated; `diff -u` exit 0), and the live base run exits 1.

## 3. Refuse-to-certify: exact mechanism, and a demonstration

Mechanism (`verifiers/check_r64_routed_repairs.py`):

- `base_control` (lines 385–387) scores the four `CHECKS` against the module constant `BASE_REV`
  (line 386: `closed = sum(1 for _, function in CHECKS if function(root, BASE_REV)[0])`).
- `run` (lines 390–397) evaluates it **before** scoring the target:
  line 391 `base_closed, total = base_control(root)`, line 392 `if base_closed != 0:`, lines 393–395 print
  `base arm failed: pinned do-nothing control at <BASE_REV> closed N of 4; refusing to certify any revision
  unless the base is exactly 0 of 4` to **stderr**, line 396 `return 1`. The target is never scored, so no
  `closed N of 4` verdict line reaches stdout — refusal is unparseable as a certification.
- `BASE_REV` is the module literal `BASE_REV_LITERAL` (line 10); there is no CLI path to it (`--base` → rc 2).

Scratch demonstration (`/tmp/r64-c2-refuse/refuse_world.py`, built from the counter's own fixture helpers in a
temp dir; `/tmp/r64-c2-refuse/relaxed_guard_behavior.py` rebuilds the same world persistently at
`/tmp/r64-c2-refuse/one-of-four-world`). The world's pinned base scores **exactly 1 of 4**
(only `control-revs-named` passes: the round-64 control line is present, the axis line and seat edit are not):

```
in-process base1 per-check: {'seat-edit-committed': False, 'control-revs-named': True,
 'lowest-axis-corrected': False, 'assertion-count-named': False} sum = 1
in-process base_control(base1): (1, 4)
in-process target per-check: {... all True ...} sum = 4

(a) honest counter --rev <target 4-of-4>: rc=1
    stdout=''
    stderr='base arm failed: pinned do-nothing control at 9636b7c0… closed 1 of 4; refusing to certify
            any revision unless the base is exactly 0 of 4'
    refusal? rc!=0:True verdict-line-absent:True
(b) guard-deleted counter --rev <target>: rc=0
    stdout='… r63 routed defects closed 4 of 4'
(c) guard-deleted counter --rev <base1>: rc=1
    stdout='… r63 routed defects closed 1 of 4'
DEMONSTRATION HOLDS
```

(a) is the required result: a base scoring 1 of 4 does **not** certify, and no verdict line is printed.
(b) shows the guard is load-bearing — delete line 392 and the identical world certifies 4 of 4 at rc 0.
(c) establishes the base score really is 1, not 0.

## 4. Findings

### F1 — MEDIUM (actionable): the 32-assertion self-test does not pin `base_closed == 0`; a `> 1` mutant passes 32/32 and certifies a 1-of-4 base

Evidence (mutant = copy of the landed file with one line changed, `verifiers/check_r64_routed_repairs.py:392`):

```
$ # M1: "    if base_closed != 0:"  ->  "    if base_closed > 1:"
$ python3 -B /tmp/r64-c2-refuse/m1_relaxed_guard.py --self-test
self-test: 0 failure(s) over 32 assertions
EXIT:0
$ # M2 control: base_control body replaced with "closed = 0"
$ python3 -B /tmp/r64-c2-refuse/m2_zero_base.py --self-test
FAIL base arm: repointed green BASE_REV refuses certification: got False, expected True
self-test: 3 failure(s) over 32 assertions
EXIT:1
```

M1 is not merely self-test-invisible; it is behaviourally wrong on the exact world the guard exists for
(`/tmp/r64-c2-refuse/relaxed_guard_behavior.py`, same 1-of-4-base / 4-of-4-target world):

```
landed (!= 0)  rc=1 verdict='<no verdict line>' stderr='base arm failed: pinned do-nothing control …'
mutant (> 1)   rc=0 verdict='r63 routed defects closed 4 of 4' stderr=''
```

Why the suite misses it: the only nonzero-base arms are `wrong_rev` (a look-alike whose honest score is
**3 of 4** — the source comment at line 880 says "partial suffix (three checks close)"; observed
`honest/label-only: look-alike rc=1 count=3`) and the green/repointed arms (**4 of 4**). Any threshold in
1..3 therefore survives all 32 assertions. The 1-of-4 base is exactly the r63 leak class E2.5 was written to
refuse (`LOG.md:2582`/`2576`: vacuous checks print `1 of 4` at base and `4 of 4` at target), so the missing
arm is the decisive one. `RevC2Checks.md:646` recommended "a partial-world arm … names wrong values" modeled
on r63's `2 of 5`; the landed arm scores 3 and still does not discriminate 1.

Landed behaviour is correct (`!= 0`), so this is a **coverage** defect, not a predicate failure: the LOG/SCORECARD
claim "refuses to certify any revision unless the control scores exactly `0 of 4` (erratum E2.5)" is enforced by
code but is not pinned by the shipped suite. Suggested repair (not applied — leaf): add a base arm whose
world scores exactly 1 of 4 (control line present, axis line and seat edit absent) and assert
`rc != 0 and count == -1`; the fixture is the one demonstrated in §3.

### F2 — LOW/MEDIUM: `C2-r64-measure.txt` omits the measured rev, the command, the exit code, and the predicate header

The w1 template (`.ufo/waves/round-64/w1/ExecReceiptTemplates.md`, C2 block) requires the frozen-predicate
header, `command:`, `measured rev:`, `counter sha256`, the verdict line and `exit=0`. The committed receipt
contains only the four PASS lines, the verdict, `counter sha256: 8f5b9f91…`, and the self-test line. The
sibling `receipts/C1-span-measure.txt` **does** name `the measured rev c019919c…` and the command, and
`controls/C2-before.txt` (the base conjunct) records neither the rev it was run against, nor the command,
nor `exit=1`. The measured revision is therefore recoverable only from commit message `b99fb79`
("… receipts at c019919c") and from the counter sha256 — not from the receipt. For a calibration axis whose
witness is the receipt, that is the M95 citation class one level down. Suggested repair: prepend the
template header (rev, command, exit) to both files at the next measurement commit; do not rewrite the
committed bytes in place.

### F3 — LOW: checks 2 and 3 scan the LOG to EOF, not to the end of the round-64 entry

`_r64_suffix_lines` (lines 99–115) returns everything after the **first** round-64 heading. In a scratch world
whose round-64 entry carries no counted lines but whose later `## … Round 65` section does
(`/tmp/r64-c2-refuse/suffix-world`):

```
check2 (control-revs-named) at later-round rev: (True, 'round-64 LOG line names committed controls …')
check3 (lowest-axis-corrected) at later-round rev: (True, 'round-64 LOG suffix names depth 9 < consistency 10 as lowest')
```

At `c019919` there is exactly one round-64 heading (`grep -c` → 1) and no later heading, so the frozen
measurement is unaffected. [INFERENCE] after round 65 lands, a re-run at a later rev can satisfy checks 2–3
with lines that are not in the round-64 entry; the check message would still say "round-64 LOG line".

### F4 — INFO: the guard cannot distinguish "base failed 0 of 4" from "base absent"; the protection is incidental

`base_control` maps an absent `BASE_REV` to `0 of 4` (every `show()` returns `None` → `False`). A world with no
`078eec…` object and a 4-of-4 target (`/tmp/r64-c2-refuse/absent_base.py`) refuses, but only because
`check_assertion_count` internally diffs the patch receipt against `BASE_REV`
(`_added_lines(root, BASE_REV, rev, PATCH_RECEIPT)`) and prints
`could not compare … with BASE_REV` → `3 of 4`, rc 1. If that coupling were ever removed, a `--root` pointed at
an unrelated history would pass the guard vacuously. The guard is root-scoped; the receipt's plain command
(default root = lane) is what makes the predicate meaningful. Worth one sentence in the check docstring.

### F5 — INFO (residual, accepted by E2): the four checks are artifact-presence checks

Check 1's floor is "marker line added + ≥60 added lines", so 60 junk lines with the marker would credit it;
check 2/3 credit a self-authored LOG line; check 4 executes committed r63 bytes inside the verifier (temp
cwd). These are the E2 trade-offs (a blob-sha pin was explicitly rejected), and the base guard plus the
look-alike/substitution arms are the mitigation. They bound the claim to "the artifacts are present and
consistent", not "the repair is independently verified".

## 5. Residual risk and verification gaps

- Did not independently re-derive the r63 `23 assertions` tally beyond what the counter itself reports
  (static reconstruction + one temp execution of the committed r63 source); the counter's own static/runtime
  agreement and the `over 23 assertions` output were observed at both revs.
- Did not audit all 32 self-test assertions one by one; the two mutations above plus the honest-arm output
  (`base 0/4`, `look-alike 3/4 rc1`, `target 4/4 rc0`, `worktree-read target 3/4 rc1`, `hardcoded-count 4/4
  on the substituted world → rejected`) were read from live runs.
- `noharm-tip.txt` is modified and `.ufo/waves/round-64/w2/` untracked in the worktree; not mine, not touched.
- The frozen predicate is stable at `c019919` by construction (all checks read committed bytes via
  `git show`); only F3 affects re-runs at future revs.
- No claim is made about C1; this seat audited C2 only.
