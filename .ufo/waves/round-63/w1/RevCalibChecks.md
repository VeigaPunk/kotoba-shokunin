# RevCalibChecks

role: reviewer (attack: C2 instrument honesty)
item: Attack the C2 instrument design — are the five checks genuinely computed; label-only and fingerprint counters; which checks pass at do-nothing tip `35d44b4b`; can check 4 ever fail; minimum assertion killing the label-only shortcut.

Axes exercised: calibration (does the counter measure what it prints), depth (does the predicate bind computation at all).

## Findings

1. **The frozen predicate admits the label-only counter at the letter; the honest-computation clause is enforced only by untested prose.**
   `python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>` is satisfied by "prints `r62 routed defects closed 5 of 5`, exit 0". The words "each of the five checks is computed from committed bytes at `<rev>`, never from a literal comparison" sit inside a `where` clause with no arm that tests them, and the predicate binds neither *which* rev `<rev>` is nor any rev where the count must be <5. C1's predicate wraps `--self-test` carrying a must-fail arm; r62's v2 was re-hardened mid-round (`FalsifyC2Shortcuts`) after exactly this hole; the r63 plan writes the same hole back in.
   Evidence — `/tmp/r63cb/check_label_only.py` (17 lines, never opens git):
   `python3 -B check_label_only.py --rev garbage-rev-xyz` → `r62 routed defects closed 5 of 5`, exit 0. Identical output at `35d44b4b` and tip `8c4cefa8`.

2. **A bytes-derived fingerprint survives a base control and is arguably admitted even by the honest-computation clause.**
   `/tmp/r63cb/check_fingerprint.py` prints `5 of 5` iff `git rev-parse <rev>:LOG.md` differs from base's blob AND the late-write path is tracked — computed from committed bytes, no output literal-compared. Scores: base `0 of 5` exit 1; tip `0 of 5`; synthetic lookalike-fix rev `d4b86ac5` (adds the file, appends two token-free "Correction:" lines to LOG) → honest reference prints `2 of 5`, fingerprint prints `5 of 5` exit 0. The plan's wording does not exclude it: it never literal-compares an output, and "computed from committed bytes" is literally true. The base-control addition (F5) does NOT kill this class.

3. **Do-nothing tip `35d44b4b` honestly passes exactly one of the five checks: check 4.** Base probe: `git ls-tree -r 35d44b4b -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md` → empty (check 1 fails; still untracked at `8c4cefa` — `git status` shows `??`). Base LOG lacks `3f911504` (check 2), has no appended correction lines (checks 3, 5). Check 4 compares base-LOG to base-LOG: identity, `ok`. Honest counter output at base: `late-write-tracked: missing / receipt-rev-named: missing / entry-size-named: missing / append-only: ok / noharm-arms-named: missing` → `1 of 5`.
   **The plan's declared expected `0 of 5` is internally inconsistent with its own check-4 wording** — or it presumes check 4 means "base LOG is a *proper* prefix" (suffix non-empty), which the spec never states. Pick one: either print `1 of 5` at base (and fix the expected-result prose), or define check 4 as proper-extension so base prints `0 of 5` (also closes the vacuous-pass hole in F4).

4. **Check 4 cannot ever fail while corrections are appended, and cannot detect past or future mid-file rewrites.**
   `prefix(b,a) = a.startswith(b)` fails iff rev LOG's first `len(b)` bytes differ — i.e., only under displacement of base content (insert, delete, in-place edit, rename, deletion of LOG.md). Under pure appends it is vacuously true — including the do-nothing case where zero bytes were appended (F3). Two deeper bounds, demonstrated:
   - It certifies nothing inside the frozen prefix: `git show e424f2a4 -- LOG.md` (ancestor of base) shows `-`/`+` rewrites of committed LOG lines; `git diff --numstat e6da78bb e424f2a4 -- LOG.md` → `5 4` (CriticCalib independently found the same via `a745411c..e53b6e5c` vs `e6da78bb..e424f2a4`). The append-only norm was already violated inside history the check declares clean.
   - It protects nothing after the tip snapshot: a later commit rewriting this round's appended corrections still passes (endpoints only).
   Verdict: check 4 is a no-rewrite invariant for base bytes, not a closure check. As specified it contributes zero discrimination to `closed N of 5` unless read as proper-extension (F3).

5. **Minimum assertion that kills the label-only shortcut: put a base control in the frozen predicate, not in expected-result prose.**
   Add to the predicate: `python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05` MUST NOT print `5 of 5` and MUST exit nonzero (state the exact count per F3: `1 of 5` under prefix, `0 of 5` under proper-extension). This kills every rev-agnostic constant/label counter unconditionally — one arm, zero fixtures. It does NOT kill the bytes-fingerprint (F2): killing that class requires either a mid-score fixture (synthetic commit scoring strictly 1–4 of 5 — I built one in /tmp objects via `GIT_OBJECT_DIRECTORY` alternates, no lane writes: `d4b86ac5` honest 2/5 vs fingerprint 5/5) or the r62 v2 structural fix — factor `check_blobs(blobs)` and run the self-test's fingerprint-lookup + partial-population controls over supplied blob dicts (pattern at `verifiers/check_routed_repairs_v2.py:468-533`, receipt line `fingerprint lookup rejected=True (8 memorized inputs)` in `.ufo/waves/round-62/C2-successor-measure.txt`). Recommended floor: base control in the predicate + one mid-score arm in the counter's own `--self-test` or a committed controls rev.

6. **Spec-precision defects that decide honest fix ↔ counter agreement (secondary):**
   a. **Check 2 "that exact token"** — receipt carries 40-hex `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`; a correction line naming `3f911504` (repo's own short-sha convention) fails a strict full-token check: my synthetic `a4ed0db3` with `3f911504` printed `receipt-rev-named: missing`. Decide now: accept full token or unambiguous hex prefix ≥7 chars, else the honest fix may not satisfy its own counter.
   b. **Check 3 numbers need boundary + scope.** `1044` occurs inside a SHA on base-LOG line 1793 (`…ed41044b…`); `64` occurs as prose ("full 64-lane dispatch", line 1229). A whole-LOG substring scan passes check 3 at base. Require: the two numbers on a single *appended-suffix* line with non-hex/non-digit boundaries.
   c. **Suffix scoping for all of checks 2/3/5.** Base LOG ends with `.` + `\n` (verified tail bytes); any mid-file insertion already fails check 4, so corrections are end-appends — but if the r63 heading lands in the same commit, "the round-62 LOG entry" is no longer the tail. Spec should scope matching to the appended suffix (or the r62 heading's bullet block, naming the rule).
   d. **Check 5's "measured 36 of 38"** appears in `noharm-tip.txt` only inside the `reg_gate` diagnostic `gate registry rows conformant 36 of 38` — extract it from there, not from `FAIL` lines (which carry no counts).
   e. **Defect-2 third sub-item uncounted** (with CriticCalib): spot-check §6.2 also routes the false "post-report child commit" claim; no check binds it — it rides on whatever the correction line happens to say.
   f. **`--rev` unbound**: predicate never says which rev must print 5/5; a counter ignoring `--rev` and reading the worktree/HEAD also satisfies the letter. Pin it ("the round's measured tip receipt rev") or make the base-control arm the only named rev and derive the success rev from the C2 receipt.

## Artifacts

`/tmp/r63cb/check_label_only.py` — verbatim:

```python
#!/usr/bin/env python3
"""Dishonest counter A: label-only. Never reads the rev, git, or any byte."""
import argparse, sys
p = argparse.ArgumentParser()
p.add_argument('--rev', required=True)
p.parse_args()
print('r62 routed defects closed 5 of 5')
sys.exit(0)
```

`/tmp/r63cb/check_fingerprint.py` — verbatim:

```python
#!/usr/bin/env python3
"""Dishonest counter B: fingerprint-keyed.
Reads committed bytes (so it literally 'computes from committed bytes at <rev>')
but scores no check: LOG.md blob fingerprint != base => 5 of 5."""
import argparse, subprocess, sys
REPO = '/home/vgpnk/Projects/shokunin/kotoba-shokunin'
BASE = '35d44b4b4dcdda234b5dbff7af37e432fec55f05'
LATE = '.ufo/waves/round-62/w2/FalsifyC2HonestH1.md'
ap = argparse.ArgumentParser(); ap.add_argument('--rev', required=True)
rev = ap.parse_args().rev
def g(*a):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True, text=True)
base_log = g('rev-parse', f'{BASE}:LOG.md').stdout.strip()
rev_log  = g('rev-parse', f'{rev}:LOG.md').stdout.strip()
tracked  = bool(g('ls-tree', '-r', rev, '--', LATE).stdout.strip())
n = 5 if (rev_log != base_log and tracked) else 0
print(f'r62 routed defects closed {n} of 5')
sys.exit(0 if n == 5 else 1)
```

`/tmp/r63cb/check_honest.py` — honest five-check reference (excerpt; full file in /tmp): computes checks 1–5 from `git show`/`ls-tree` bytes, scopes 2/3/5 to the appended suffix with hex/digit-boundary regexes, extracts `receipt_rev` and the conformant `N of M` from the two receipts at `<rev>`.

Measured outputs (all real runs):

```
rev=35d44b4b: honest 1 of 5 (append-only ok) exit 1 | fingerprint 0 of 5 | label-only 5 of 5
rev=8c4cefa8 (tip, plan freeze): same as base — late write STILL untracked
rev=d4b86ac5 (synthetic lookalike fix): honest 2 of 5 | fingerprint 5 of 5 exit 0  ← fingerprint fooled
rev=a4ed0db3 (short-token fix): honest 3 of 5 — receipt-rev-named missing on "3f911504"
rev=30ca0d5f (full-token fix): honest 5 of 5 exit 0  ← sane calibration curve
rev=garbage-rev-xyz: label-only 5 of 5 exit 0 (predicate satisfied on a nonexistent rev)
```

Synthetic revs were built in `/tmp/r63cb/objects` via `GIT_OBJECT_DIRECTORY`+`GIT_ALTERNATE_OBJECT_DIRECTORIES` and `commit-tree` — zero writes to the lane `.git` (method receipt for the L1's own control fixtures).

## Verdict

**ATTACKS** the C2 instrument design as frozen. The five checks as *specified* are computable honestly (my reference does it and produces a sensible curve), but the frozen predicate as *written* admits a pure label-only printer and a bytes-derived fingerprint — the exact class r62's own wave 2 closed mid-round — and its declared `0 of 5` base expectation contradicts check-4's prefix semantics. To change my mind: (a) put the base-rev control inside the frozen predicate with an explicit count; (b) state check 4 as proper-extension or accept `1 of 5` at base; (c) answer whether a blob-diff fingerprint counts as "computed from committed bytes" — if not, adopt the v2 supplied-blobs self-test or a mid-score control rev; (d) pin down "that exact token" (full vs prefix) and suffix-scoping before the correction line is written.
