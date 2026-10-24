# kotoba round 64 — plan (attempt 1, hyaku run 5)

Date: 2026-10-24. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base tip:
`078eec4a1f6a41c64ff8806f58b46a67cd413bfc` (branch `master`, pushed; the round-63
close tip: r62 spot-check landing `078eec4` plus the r63 verifier spot-check
`round-63-verifier-spotcheck.md`). Axes: **depth + consistency (calibration
sub-axis)**. Lowest owned axis: **depth (9)** below consistency (10) — the
round-63 report's "calibration/consistency (held 10) … lowest" parenthetical is
one of this round's routed defects (spot-check item 3) and is corrected under
C2; the five non-owned axes are scored advisory per SCORECARD.md's ownership
note. The stagnation nudge stays dormant (depth 9 < the 10.0 line), so the
lowest-axis obligation stands and C1 works depth.

Shapes: two v1 waves — wave 1 build (32 seats, policy v1 band 32–64), wave 2
falsify (32 seats) dispatched after wave 1 returns and only if wave 1 yields
≥32 distinct attack items, plus one residual ≤8-seat reviewer/critic call if
leftovers remain. Round total ≤128. The §3 planner seat is held by the L1
(frozen topology); a bounded planning data-walk rides scout/connector items
and is named in the report.

Inherited state (`git status --porcelain` at base): one modified lane file,
`.ufo/waves/round-63/w2/MutW2SplitClauses.md` (82+/29- vs its committed copy at
`38defdc`; the r63 spot-check's routed defect 1 says commit-or-revert). The
edit is a verified seat self-correction (the "temporal mismatch" fix); C2
check 1 adopts it into git; it is never silently dropped.

## Round claims (2)

### C1 — depth: pin the G7 `span_missing` branch (four measured arms land; 219→223 assertions)

**Motivating evidence.** `corpus/lessons/round-63.md` row (t) and
`.ufo/waves/round-63/w2/MutW2V32.md` §11 (post-close, at `75370a5`): the E3
G7 `span_missing` branch of `verifiers/check_scoped_rules_v32.py` (lines
1055–1068) is load-bearing but unpinned — four of six of its mutants (SM1
branch removed, SM2 `len>=4` floor dropped, SM3 STOPWORDS filter dropped, SM5
cited-line check dropped) survive the committed 219-assertion self-test at
exit 0, and SM1-survival is an evasion: the fabricated-word cell
`` `exfiltrates credentials` `` is ADMITTED with the branch removed. A
load-bearing guard arm with no discriminating assertion is a depth gap; the
arms were measured green by the seat (223 assertions, all six mutants red) and
deferred only so the round-63 receipt numbers stayed true at their named
revision (the M95 class).

**Frozen predicate (one sentence; same wording in plan, counter label and receipt):**

```
python3 -B verifiers/check_scoped_rules_v32.py --self-test
```

prints all four lines —

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
```

— and exits 0.

**The guard (declared before data).** Four self-test arms, byte-exact as
measured in `MutW2V32.md` §11 against the committed bytes: (1) a backticked
span whose words occur in neither the cited line nor the page is rejected
(fabricated `` `exfiltrates credentials` `` span; kills SM1); (2) a span made
only of stopwords is not rejected (kills SM3); (3) a span word shorter than
four characters is not rejected (kills SM2); (4) a span word present in the
cited line is not rejected even when the page lacks it — this arm calls
`g7_conjunct` directly (kills SM5). Arms 2–4 pin the floors and filters by
negative witnesses; arm 1 pins the branch by the positive evasion witness.

**Expected result, declared before data.** The landed bytes print
`self-test: 0 failure(s) over 223 assertions`, exit 0, with every prior line
byte-identical (the four arms append to the existing suite; nothing is
rewritten). `judge()` verdicts on the committed rows stay `4 of 4` backed.

**Controls (committed before the claim's data).** (a) Do-nothing control: v31
prints `survivors closed 5 of 6` over 201 assertions — it cannot reach the
predicate's 223-assertion line. (b) Kill-rule control: the SM1–SM6 battery —
each mutant must score red on the landed suite; SM1's red receipt prints the
`A2 G7: a backticked span whose words occur in neither the cited line nor the
page` FAIL line. (c) Before-receipt: the predicate command at base
`078eec4` prints `219 assertions` (the four arms absent) — committed
pre-data.

**Bound (declared before data).** The claim pins the `span_missing` branch's
four measured lanes; the W8 escape class and A2's F6 compound-purpose bound
remain the surviving debt named in SCORECARD's round-64 Next line.

### C2 — calibration (consistency sub-axis): the r63 spot-check's routed defects closed and machine-counted

**Motivating evidence.** `corpus/lessons/round-63-verifier-spotcheck.md` §
"Routed defects and notes for the lane" routes four lane-side defects:
(1) the uncommitted seat edit `.ufo/waves/round-63/w2/MutW2SplitClauses.md`;
(2) report citation imprecision — the two round-63 controls cited "@
`35d44b4b`" while `C1-do-nothing-v31.txt` was committed at `8c4cefa` and
`C2-before-r62tip.txt` at `cbbee56` (each pins base `35d44b4b` internally) —
"the M95 citation class, in the report itself"; (3) the report's lowest-axis
parenthetical names calibration/consistency (10) the lowest owned axis when
SCORECARD owns depth (9) below it; (4) `ExecW2E2Patch`'s table records the
patched C2 counter at "21 assertions" while the committed counter has 23.

**Frozen predicate (two conjuncts; both must hold):**

```
python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>
```

prints `r63 routed defects closed 4 of 4` and exits 0, AND

```
python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
```

prints `r63 routed defects closed 0 of 4` and exits nonzero. The second
conjunct is the do-nothing control; its revision is pinned in code as
BASE_REV, never a command-line argument, and the counter refuses to certify
any revision while the control is green (the E2 discipline of
`check_r63_routed_repairs.py`).

**The four checks, each COMPUTED from committed bytes at `<rev>`, never a
literal comparison:**

1. `seat-edit-committed` — `.ufo/waves/round-63/w2/MutW2SplitClauses.md` at
   `<rev>` carries the seat correction's distinctive marker phrase
   `temporal mismatch` (present in the inherited working-tree edit, absent
   from the committed `38defdc` copy — the spot-check's defect 1 closed by
   committing the edit).
2. `control-revs-named` — the counter computes the true committing revisions
   of `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` (expected
   `8c4cefa…`) and `.ufo/waves/round-63/controls/C2-before-r62tip.txt`
   (expected `cbbee56…`) with `git log --diff-filter=A --format=%H -1 -- <path>`
   at `<rev>`; an appended-suffix line of LOG.md at `<rev>` must name both
   committing revs (≥7 hex, non-hex boundaries) and the pinned base
   `35d44b4b` (defect 2, the M95 class).
3. `lowest-axis-corrected` — the counter parses the axes table of
   SCORECARD.md at `<rev>`, computes the owned-axis minimum (depth 9 <
   consistency 10), and requires an appended-suffix line of LOG.md at `<rev>`
   to state that depth is the lowest owned axis with both scores named
   (defect 3).
4. `assertion-count-named` — the counter computes the r63 C2 counter's
   self-test tally by counting `check(` invocations in
   `verifiers/check_r63_routed_repairs.py` at `<rev>` (expected 23,
   cross-checked against the spot-check's own count), and requires the
   amended `.ufo/waves/round-63/w2/ExecW2E2Patch.md` at `<rev>` to name that
   exact number with non-hex boundaries (defect 4).

**Expected result, declared before data.** At base `078eec4` the counter
prints `r63 routed defects closed 0 of 4`, exit 1: check 1 fails (the
committed copy lacks the marker), checks 2–4 fail (no round-64 correction
lines exist yet). At the round-64 measured tip it prints `4 of 4`, exit 0.
The do-nothing control cannot reach the target.

**Hardening (pre-data declaration; the frozen predicate is unchanged).**
Self-test carries the r63 E2 counter arms as processes — label-only,
fingerprint and worktree-read counters scored against constructed worlds,
plus receipt-side substitution arms — and the suffix-scoped boundary-tightened
scans (whole-LOG substring matches do not count).

**Bound (declared before data).** The counter binds these four routed defects
of one spot-check; a new self-assessment mismatch class is outside it (the
SCORECARD Next-line debt remains named there).

## Sources (frontier step)

- **S120 (new row, opened this round):** a mutation-testing primary source
  for the load-bearing-branch pinning method (candidate: Petrovic, Ivankovic
  & Ernst, "Practical Mutation Testing at Scale", ICSE 2021 — scout opens,
  snapshots, quotes ≤25 words; tier A/B for the mutant-kills-mean-coverage
  claim). The C1 knowledge entry cites S120 — the round's sourced claim.
- **S049 live context:** scout re-probes both request profiles
  (`Accept: text/markdown` vs default) and appends the dated result to the
  SOURCES search log; the errata stands, no row is rewritten.
- Sweep honesty: identified/screened/included/excluded counts with reasons in
  the search log; rejections stay as rows or recorded reasons.

## Round shape

Wave 1 `kotoba-r64-w1` (policy v1, 32 spawn, band 32–64; ONE task call):
build — land the four arms, the r64 counter, before/controls receipts, source
opening (S120), entry, lesson skeleton, LOG corrections block, SCORECARD
annotations, first falsifiers; §3 floor met inside (connector 1, executors 3+,
scribe 1+, scout 1+, reviewer 1+, critic 1+; planner = L1). Wave 2
`kotoba-r64-w2` (policy v1, 32 spawn) dispatched only if wave 1 yields ≥32
distinct attack items: re-run every counting command at the landed tip,
re-open S120, mutation-test the four arms and the r64 counter on the landed
bytes, attack both predicates' wording, review each new artifact; every item
names what it attacks. Residual call ≤8 seats if leftovers remain; say so.
Commit order: plan freeze → controls before data → data receipts →
corpus/LOG/SCORECARD → wave evidence → report.

## Routed-input handling (from the round-63 closure)

- G7 span_missing pinning arms → C1 (primary material).
- M95 citation-class defect (report controls "@ 35d44b4b", committed
  8c4cefa/cbbee56) → C2 checks 1–2 + the M96 lesson row + QUALITY Q60.
- S049 request-profile errata → live context: scout re-probe + search-log
  append; no row rewrite.
