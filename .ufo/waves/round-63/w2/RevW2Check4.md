# RevW2Check4

role: revenger / reviewer (attack: C2 counter check 4 `append-only` — endpoint scope vs history-level claim)
item: Verify at `cbbee56e` that check 4 prints `prefix=True` with `grew_by=9` (the r63
corrections block); demonstrate in /tmp with synthetic git objects that the check cannot
detect a suffix rewrite of this round's own appended corrections (endpoint-only) and could
not detect r62's own historical mid-file rewrite (`git diff e6da78bb e424f2a4 -- LOG.md`
shows `5/4`); deliver the disposition wording — check 4 is a frozen-prefix preservation
guard, not history-level append-only enforcement — with the exact bounded sentence for the
SCORECARD row and report.

Axes: calibration (does the counted arm mean what its label says).

## Instrument under attack (committed bytes)

`verifiers/check_r63_routed_repairs.py` @ `cbbee56e` (worktree sha256 `5a15feac…` ==
`git show cbbee56e:…` sha256 `5a15feac…`):

```python
def check_append_only(root: Path, rev: str) -> tuple[bool, str]:
    base_log = show(root, R62_TIP, LOG)          # R62_TIP = 35d44b4b4dcd…
    rev_log = show(root, rev, LOG)
    if base_log is None or rev_log is None:
        return False, "LOG.md unreadable at one of the two revisions"
    prefix = rev_log.startswith(base_log)
    grew = len(rev_log.splitlines()) > len(base_log.splitlines())
    return prefix and grew, ("prefix=%s grew_by=%d line(s)" % (…))
```

Two inputs only: the frozen base snapshot and the `<rev>` snapshot. Nothing between
them is ever read.

## 1. Verification at `cbbee56e` — check 4 fires as committed

```
$ python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
exit=0
```

`grew_by=9` is exactly the r63 corrections block (blank, `### Round-62 corrections…`
heading, blank, six defect bullets):

```
$ git diff 35d44b4b cbbee56e -- LOG.md
LOG.md | 9 +++++++++
 @@ -2564,3 +2564,12 @@
```

Base control — prefix conjunct passes vacuously, E1's growth conjunct supplies the failure:

```
$ python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
…
FAIL append-only          prefix=True grew_by=0 line(s)
r62 routed defects closed 0 of 5
exit=1
```

## 2. Demonstration — the check is blind to suffix rewrites (endpoint-only)

Method: `/tmp/r63ck4/repo` — `git init`, `.git/objects/info/alternates` →
`$LANE/.git/objects` (read-only), committed verifier materialised to
`/tmp/r63ck4/repo/verifiers/`, commits built with `read-tree`/`hash-object`/`update-index`/
`write-tree`/`commit-tree` on top of `cbbee56e`. **Zero writes to the lane `.git`, index,
or worktree.** The counter's `LANE` resolves to the /tmp repo, which sees every lane object
through the alternate.

**R1 — full post-commit rewrite of the appended corrections block, tokens retained**
(`8b9581350142859eed1ee054a7dd3c10b241a2cd`; all six committed bullets deleted and
replaced; `git diff --numstat cbbee56e 8b958135 -- LOG.md` → `7 7`):

```
PASS append-only          prefix=True grew_by=9 line(s)
r62 routed defects closed 5 of 5        exit=0
```

Identical transcript to the honest tip. The instrument accepts a history in which the
committed r63 correction prose was silently replaced wholesale — the exact behaviour
"append-only" names — because both endpoints it samples are satisfied.

**R2 — appended block replaced with token-free text**
(`a4beed1d3f2dbd55879f87351fe477bd0eba216a`; `numstat 1 7`):

```
FAIL receipt-rev-named / FAIL entry-size-named
PASS append-only          prefix=True grew_by=3 line(s)
FAIL noharm-arms-named
r62 routed defects closed 2 of 5        exit=1
```

Check 4 itself still passes — the only failure signal comes from the token checks (2/3/5).
Check 4 contributes **zero** suffix-integrity discrimination on its own.

**R3 — single committed line rewritten inside the frozen prefix**
(`8e65593b278adbfff24893cf56ddc6af4b306ad6`; `numstat 1 1`):

```
FAIL append-only          prefix=False grew_by=9 line(s)
r62 routed defects closed 4 of 5        exit=1
```

The arm is not vacuous: displacing frozen-base bytes is the one mutation class it sees.
Scope confirmed by elimination: the guard covers the prefix endpoint only.

## 3. Demonstration — the certified prefix already embeds a mid-file rewrite

```
$ git diff --numstat e6da78bb e424f2a4 -- LOG.md
5	4	LOG.md
$ git merge-base --is-ancestor e424f2a4 35d44b4b   → yes
$ git merge-base --is-ancestor e6da78bb e424f2a4   → yes
```

`e6da78bb` (r62 corpus + v3.1 successor) → `3f91150` (w2 dispatch) → `e424f2a4` (r62
wave-2 falsification + C2 hardening, "F1-F15 corrections in the lesson/entry/LOG/SCORECARD").
Hunks at lines 2547, 2549, 2552→2552,2, 2563→2564 of a 2564-line file: four
already-committed r62 bullets replaced in place plus one insert — the wave-2 correction
pass rewriting committed receipt/claim bullets (the appended r63 block itself records
`receipt_rev=…` "re-recorded at `e424f2a4`"). Measured probe:

```
e424f2a4 LOG startswith e6da78bb LOG (check-4 semantics on the transition): False
35d44b4b embeds e424f2a4's rewritten line 2547: True; e6da78bb's original differs: True
```

The check's own criterion, applied to that transition, would have failed it — but the
instrument never performs that measurement: both frozen endpoints carry the post-rewrite
bytes, so `prefix=True` at `35d44b4b` and `prefix=True` at `cbbee56e` certify a prefix
whose history contains the rewrite. A history-level append-only claim over this file is
already falsified inside the bytes the check declares preserved.

## Verdict on the committed bytes

**CONFIRMED-WITH-BOUND — ATTACKS the unbounded "append-only" reading, not the predicate.**
The committed instrument behaves exactly as committed and is not vacuous: prefix
displacement fails it (R3), E1's growth conjunct kills the trivial base pass. The defect
is scope: plan §C2.4's parenthetical "corrections are appended; no committed line is
rewritten" overstates the enforcement. Correct bound — check 4 is a **frozen-prefix
preservation guard**: it proves `35d44b4b`'s `LOG.md` bytes survive as a byte-prefix at
`<rev>` with ≥1 appended line. It cannot see (a) any rewrite inside the appended suffix —
including a complete post-commit rewrite of this round's own corrections block (R1 scores
`5 of 5`, exit 0) — nor (b) any rewrite inside history embedded in the prefix (r62's own
`e6da78bb`→`e424f2a4` `5/4`). Suffix integrity today rides only on checks 2/3/5's token
scans (R2). No arithmetic defect: `5 of 5` at tip and `0 of 5` at base are both truthful
under the arm's real semantics.

## Smallest safe correction — exact proposed text

Bound the label in prose; the instrument needs no code change. Proposed sentence for the
SCORECARD round-63 C2 annotation (the row has not landed — `SCORECARD.md` unchanged at
`cbbee56e`; `w1/ExecScorecardRow.md` drafted it), appended to the C2 clause:

> the `append-only` arm is a frozen-prefix guard, not history-level enforcement: it proves
> `35d44b4b`'s `LOG.md` is a byte-prefix of the measured rev's with ≥1 appended line (E1),
> and is blind to rewrites inside the appended suffix — this round's own corrections block,
> rewritten post-commit, still passes (`RevW2Check4` rev `8b958135`) — and to rewrites
> embedded in the prefix's history (r62's `e6da78bb`→`e424f2a4`, `5/4`).

And the matching sentence for the report's C2 bounds paragraph:

> Check 4 (`append-only`) is an endpoint guard: it certifies the r62-tip `LOG.md` prefix
> survives at the measured rev with growth (E1); it enforces nothing about the appended
> suffix — a committed-then-rewritten corrections block keeps `prefix=True` and `5 of 5` —
> and nothing about the prefix's own history, which already embeds r62's
> `e6da78bb`→`e424f2a4` in-place rewrite of four committed bullets.

If history-level append-only is ever claimed instead, the instrument would need a
per-parent→child LOG transition check plus a committed suffix-rewrite negative fixture —
out of scope for a prose correction.

## Artifacts

- `/tmp/r63ck4/repo` — /tmp git repo (alternates → lane objects; no lane writes).
  Synthetic revs: `8b958135…` (R1 tokens-kept rewrite), `a4beed1d…` (R2 tokens-dropped),
  `8e65593b…` (R3 prefix edit). Verifier copy = committed bytes at `cbbee56e`.
- Prior independent findings this confirms and quantifies: `w1/RevCalibChecks.md` F4,
  `w1/CriticCalib.md` F5 ("describe this arm as frozen-prefix preservation"), `w1/
  MutCalibInstrument.md` M4/RW fixture (equal-line-count rewrite of a committed bullet).

## Lane hygiene

No production file edited, no lane git/jj state touched (all git reads; synthetic commits
live only in `/tmp/r63ck4/repo`). No installs: `git` 2.x and `python3` already present;
pacman untouched per the pause. Suggested L1 follow-up: apply the bounded sentences above
to `SCORECARD.md`'s C2 clause and the report bounds paragraph.

Report: `.ufo/waves/round-63/w2/RevW2Check4.md`
