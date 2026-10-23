# kotoba round 63 — plan (attempt 3, hyaku run 5)

Date: 2026-10-23. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base tip:
`35d44b4b4dcdda234b5dbff7af37e432fec55f05` (branch `master`, pushed; r62 close tip
`e53b6e5c` plus the r62 spot-check landing). Axes: **depth + consistency (calibration
sub-axis)**. Lowest owned axis: calibration/consistency (8.5) below depth (9);
the five non-owned axes are scored advisory by `SCORECARD.md`'s declared ownership note,
and the all-axes reading of "lowest non-retired axis" is the open round-47 L0 question.
C1 works depth, C2 works the lowest owned axis (calibration). The stagnation nudge stays
dormant (depth 9 < the 10.0 line).

Shapes: two v1 waves — wave 1 build (32–64 seats), wave 2 falsify (32–64 seats) only if
wave 1 yields ≥32 distinct attack items, plus one residual ≤8-seat reviewer/critic call if
leftovers remain. Round total ≤128. The §3 planner seat is held by the L1; any bounded
planning data-walk rides a scout/revenger item and is named in the report.

Inherited state: `git status --porcelain` at base shows one untracked lane file,
`.ufo/waves/round-62/w2/FalsifyC2HonestH1.md` (r62 late seat write, spot-check defect 1).
It is adopted by C2 (item 1), never silently dropped.

## Round claims (2)

### C1 — depth: close the sixth frozen erratum survivor (G9, compound purpose outside citation)

**Motivating evidence.** `verifiers/check_scoped_rules_v31.py` (sha256 `a07c2269…`)
prints `survivors closed 5 of 6`: five of the six r62 erratum survivors are rejected by the
successor, and the sixth, `e2f-compound-purpose-outside-citation`, is accepted and recorded
as a declared surviving bound (`Self-test line "bound: G9 remains unimplemented"`). G9's
class: an action cell that glues an unrelated purpose clause onto a sentence the cited line
does support, where the purpose words occur elsewhere on the page — so A2's forward
fraction, page containment, reverse coverage and G7's backticked-identifier check all pass.
The lane holds the guard-mutation method (`check_erratum_absorption.py`, r62) and has not
applied it to G9; a named survivor left as prose is a depth gap, not a bound.

**Frozen predicate (one sentence; same wording in plan, counter label and receipt):**

```
python3 -B verifiers/check_scoped_rules_v32.py --self-test
```

prints all three lines —

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
```

— and exits 0.

**The guard (declared before data).** `g9_conjunct(lines, cell, L, page_text)` splits the
action cell at coordinating boundaries (`;` and the word `and`, case-insensitive, outside
backticks), and for every resulting clause with ≥ `MIN_CONTENT` content words requires the
same forward-support fraction A2 uses (`fwd_need`) from the **cited line**. A clause that
the page supports but the cited line does not is rejected as
`A2 G9: clause "…" is supported outside the cited line`. The rule is scoped to page-present
clauses so it cannot double-report words the A2 page-containment check already rejects.
`action_conjunct` appends its reasons after `g7_conjunct`'s.

**Expected result, declared before data.** The frozen G9 instance is
`"The configuration stores project rules using glob syntax and secretly uploads files."`
against a cited line that stops after `glob syntax` and a page whose unrelated section holds
`secretly uploads files`. Its second clause has zero support on the cited line, so `after`
flips to rejected and `survivors closed` prints `6 of 6`. The four eligible fixture rows'
action cells are read before designing the split: S900 and S902 carry `;` clauses whose
second clause is supported by the same cited line (line 5 of their pages is the action text
itself), and S901/S903 carry no split boundary — so `eligible rows pass 4 of 4` must hold.
If it prints `5 of 6`, the guard is wrong and the round records a counter defect.

**Control (committed before the claim's data).** The do-nothing control is v31 itself:
`python3 -B verifiers/check_scoped_rules_v31.py --self-test` prints `survivors closed 5 of 6`
and only two must-fail arms, so it cannot meet the predicate. The label-only control is the
must-fail arm: with `g9_conjunct` replaced by an admitting stub in process, the frozen G9
instance is admitted again — the self-test requires that flip, so a guard that never fires
fails the same predicate.

### C2 — calibration (consistency sub-axis): the r62 spot-check's routed defects closed and machine-counted

**Motivating evidence.** `.ufo/reports/round-62/kotoba.md` §6 of the out-of-round
spot-check (`corpus/lessons/round-62-verifier-spotcheck.md` §6) routes five defects where
the round's self-assessment did not match committed state: (1) an untracked late seat write,
(2) three report citations wrong at tip (C2 `receipt_rev`, entry size, a claimed post-report
child commit), (3) a probe-dependent Cursor rejection reason, (4) a no-harm summary that
omits the receipt's two interim reds, (5) SHONEN boxes (operator-owned; no change).
Defects 1, 2 and 4 are self-assessment mismatches; defect 3 is a source-freshness repair,
worked in the same round and reported separately rather than counted here.

**Frozen predicate (one sentence; same wording in plan, counter label and receipt):**

```
python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>
```

prints `r62 routed defects closed 5 of 5` and exits 0, where each of the five checks is
**computed from committed bytes at `<rev>`**, never from a literal comparison:

1. `late-write-tracked` — `git ls-tree -r <rev> -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md`
   is non-empty (the file the spot-check found untracked is committed as wave evidence).
2. `receipt-rev-named` — the counter reads `receipt_rev=` out of
   `.ufo/waves/round-62/C2-successor-measure.txt` at `<rev>`, then requires the round-62
   LOG entry to carry an appended correction line naming **that exact token**.
3. `entry-size-named` — the counter computes `wc -l`/`wc -w` of
   `corpus/knowledge/erratum-absorption-round62.md` at `<rev>` and requires the correction
   line to state both numbers.
4. `append-only` — `git show <r62-tip>:LOG.md` is a byte-prefix of `git show <rev>:LOG.md`
   (corrections are appended; no committed line is rewritten).
5. `noharm-arms-named` — the counter extracts the `reg_gate` and `corpus-idx` result tokens
   from `.ufo/waves/round-62/noharm-tip.txt` at `<rev>` and requires the correction line to
   name both, including the measured `36 of 38`.

**Expected result, declared before data.** At the r62 tip `35d44b4b` (before this round's
corrections) the counter prints `r62 routed defects closed 0 of 5`, exit 1: check 1 fails
(the file is untracked), 2–3 fail (no correction line names the receipt revision or the
sizes), 4 passes (an empty delta is a prefix — recorded honestly as a check that only bites
when text is rewritten), 5 fails. At the measured r63 tip it prints `5 of 5`, exit 0.
The target is 5 of 5; the do-nothing control (the r62 tip) scores 0 of 5 on the four
content checks, so it cannot meet the target.

**Bound, declared before data.** The counter binds the named five defects of one spot-check
and the two receipts it reads; a new class of self-assessment mismatch is outside it.

## Sources (frontier step)

One new row is opened this round: **S119** — a primary source on correction/errata practice
(transparent, appended, linked correction rather than in-place rewrite), which C2's repair
method cites. The row lands with its URL, access date and a ≤25-word located quote in the
round-63 lesson `## Gate`, plus a snapshot under `.ufo/waves/round-63/snapshots/`. S049's
cursor `.md` rejection reason (spot-check defect 3) is re-probed under both `Accept` forms
and corrected in the round-62 lesson's Gate, with the SOURCES note appended, not rewritten.

Census command (before/after, both pasted in the report):

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
```

Before: exit 0, 16 W04 (`census-before.txt`). After: expected exit 0, 17 W04 (S119's URL is
new; if it duplicates an existing URL the counter names it and the row is a re-open instead).

## Round shape

Wave 1 build (32–64, policy v1), wave 2 falsify (32–64) if ≥32 attack items exist, residual
≤8 if not. Every wave context carries: lane repo is the only write target for the L1; seats
write only their own report file under
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-63/<wave>/`; tooling
authorization per `~/.omp/agent/RULES.md`; the pacman pause (no `pacman -S`/`-Sy`/`-Syu`;
use `uv tool`/`npx`/official binary); and the misroot rule (every `Report:` trailer is
relative to the lane repo).

## Erratum E1 (pre-data, declared before any C2 measurement)

`§C2` check 4 as first written ("`git show 35d44b4b:LOG.md` is a byte-prefix of
`git show <rev>:LOG.md`") passes trivially at the r62 tip, where the two texts are
identical, so the declared before `0 of 5` and the check's arithmetic disagreed. E1
refines the check to **two conjuncts**, both reported separately: the r62-tip bytes are a
prefix of the measured rev's LOG, **and** the measured rev's LOG adds at least one line
beyond that prefix. At the r62 tip the second conjunct is false (no correction appended),
so the check fails there and the before total is a truthful `0 of 5`; a tree carrying the
appended corrections passes both. The target and every other check are unchanged.
