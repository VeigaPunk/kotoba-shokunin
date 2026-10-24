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

## Erratum E1 (pre-data, declared before any C2 measurement; wave-1 findings)

Three wave-1 findings correct the C2 check definitions before any
after-measurement; the frozen predicate sentences (the `4 of 4` / `0 of 4`
headlines and the pinned base) are unchanged.

1. **Checks 2 and 3 are suffix-anchored to the round-64 LOG entry.** The
   r63 corrections-to-corrections block (LOG.md at base, line ~2576) already
   co-locates `8c4cefa`, `cbbee56` and `35d44b4b`, so a whole-LOG or
   r63-suffix scan would false-green check 2 at base (`ScoutQualityDebt`
   hazard). Fix: checks 2 and 3 scan only lines after the first
   `## 2026-10-24 — Round 64` header of LOG.md at `<rev>`; the header absent
   ⇒ both checks fail. (Base has no round-64 header, so the `0 of 4`
   expectation stands; verified by the counter's base arm before data.)
2. **Check 4 computes the tally by running the materialized self-test.**
   A literal `check(` count can never certify: the committed r63 counter has
   20 `check(` tokens / 19 call sites, and its runtime tally is 23 only
   because two arms sit in a 3-iteration loop (`ScribeReportSkeleton`
   finding 1). Fix: materialize `verifiers/check_r63_routed_repairs.py` at
   `<rev>` into a temp dir, run `python3 -B <file> --self-test`, parse
   `over N assertions` (expected 23), and require the amended
   `ExecW2E2Patch.md` at `<rev>` to name that number with non-hex
   boundaries.
3. **SM5 is pinned at the component level (C1 bound clarification).**
   `CriticC1Bound` showed the full `judge()` path derives lines from the
   page, making the cited-line filter redundant for reachable judge inputs;
   arm 4's witness is a direct `g7_conjunct` call per MutW2V32 §11. The
   four arms and the 223-assertion predicate are unchanged; C1's Bound
   records that SM5's pin is component-level, not a judge-level evasion
   lane.

**Disposition of the newly found M95-class instances (wave-1, pre-data).**
`ScribeQ60` F2 found the receipt citations in SCORECARD.md's round-63
annotation: `C1-g9-measure.txt` exists at `849a546e` but its bytes there are
the stale wave-1 version (sha `552308806b…`, 205 assertions) — the described
219-assertion refresh committed at `2ba4547f` — and the C2 annotation's
receipt citation at the same rev is the interim file. These are the M95
class in this lane's own scorecard, one bound outside the spot-check's four
routed defects. Disposition (pre-data): the round-64 SCORECARD annotation
carries an erratum line naming the refreshed receipts' committing rev
`2ba4547f` and the stale-content fact; the repair is verified by the
`ScoutReceiptSweep` census and wave-2 re-derivation but is NOT one of the
four counted checks — the counter's bound (below) names exactly the
spot-check's four routed defects.

**C2 bound (amended, pre-data).** The counter binds these four routed
defects of one spot-check; a new self-assessment mismatch class is outside
it (the SCORECARD receipt-citation instance above is repaired and recorded,
not headline-counted; the SCORECARD Next-line debt remains named there).

## Erratum E2 (pre-data, declared before any C2 measurement; wave-1 findings)

`RevC2Checks` attacked all four checks and the control rule; three sibling
seats (`ScribeLesson`, `CriticC2Bound`, `ScribeReportSkeleton`) independently
corroborated. The frozen predicate headlines are unchanged; the check
implementations are hardened as follows — all verified FAIL-at-base before
any after-measurement.

1. **Check 1 gains a discrimination floor.** The marker `temporal mismatch`
   alone credits the check from a one-sentence note (the phrase also sits in
   committed `plans/round-64.md`). Fix: the check requires, all computed at
   `<rev>`: marker present; the marker line is an addition vs `38defdc`; and
   `git diff --numstat 38defdc <rev> -- <path>` reports ≥60 added lines (the
   inherited edit measures 82+/29-). (A full-blob sha pin was rejected: it
   would freeze the seat file against later honest appends.)
2. **Check 2's suffix line is content-shaped.** One line under the round-64
   header must carry both computed committing revs, the computed base
   `35d44b4b…`, both control basenames, and the word `committed`;
   derivations that yield no commit (e.g. `git log <rev>` for a rev
   predating the file, which exits 0 with empty output) must FAIL. Self-test
   arms: look-alike line, one-sided line, wrong rev, repinned base, empty
   derivation, full/short-hash acceptance.
3. **Check 3's parse is section-bounded.** The axes parse is bounded to the
   `## axes` section (a second table exists under `## Move log`); the owned
   set derives from the header sentence; the score is `cells[1]`'s leading
   number; the suffix line must contain `lowest` + `depth` + `consistency`
   + both digit-bounded scores.
4. **Check 4 pairs the runtime tally with a static cross-check.** The
   materialized self-test's `over N assertions` is cross-checked against the
   static call-site reconstruction (17 fixed + 2 loop-body sites × 3 arms =
   23); both must agree. The amended `ExecW2E2Patch.md` line must carry the
   bounded tally, the word `assertions`, and be an addition vs `BASE_REV`.
   Failure modes fail closed: absent path → 128, bogus rev → 128, missing
   `git` → OSError.
5. **Control rule: refuse unless `base_closed == 0`.** The r63 rule (refuse
   while the control is green) admits a counter whose checks are vacuous
   token scans: they print `1 of 4` at base (the `LOG.md:2576` leak) and
   `4 of 4` at target, passing both conjuncts. The r64 counter refuses to
   certify any revision unless the pinned base scores exactly `0 of 4`, and
   its self-test carries a partial-world arm (suffix present, wrong values
   → still refuse) plus a repointed-`BASE_REV` arm.

**Spot-check size-quote erratum (recorded, not repaired by us).** The r63
spot-check's defect 1 quotes the working-tree edit as "41+/13-"; the
measured diff at base is 82+/29- (`git diff --numstat`). The spot-check file
is non-author — never edited; the misquote is recorded in the round-64
lesson and report (the substantive routing stands: the edit was uncommitted
at closure; it lands under round 64).

## Erratum E3 (pre-data, declared before any C1/C2 after-measurement)

Wave-1 falsifiers (`RevC1Predicate`, `MutSpanArms`, `RevC2Checks`,
`RevSpotcheckCrosswalk`, `CriticC1Bound`) attacked both predicates; the
frozen headlines stand, the instruments and receipts are hardened, all
pre-data.

1. **C1's counted predicate gains its kill conjunct and pin pair.**
   `RevC1Predicate` Q1 built a dishonest counter that prints the four
   predicate lines with four tautology checks while SM1 still admits the
   evasion — the printed lines alone are satisfiable with zero pinning.
   The counted predicate (one sentence, same in plan, receipt and
   SCORECARD) is therefore: `python3 -B verifiers/check_scoped_rules_v32.py
   --self-test` prints the four frozen lines and exits 0, AND the receipt
   pins the `(sha256, 223)` pair recomputed from the landed bytes, AND the
   kill conjunct holds: each of SM1–SM6 scores exit 1 on the landed bytes
   with its own discriminating FAIL label — an arm is credited only when
   its own `check()` label is the FAIL line (the kotodama R64-M9 lesson via
   `ConnSibling`: SM4/SM6 are red on pre-existing `eligible world` arms and
   are not new-arm pins). Honest-padding objection (Q2: an unrelated future
   arm moves N to 224 and the literal predicate says no): a later
   measurement on later bytes is a second measurement under Q28, never the
   declared one; the declared claim is measured at this round's rev.
2. **Arm 4 lands with the hardened fixture (`MutSpanArms` §6).** Cell
   `The tool writes quota nightly and \`mode quota\`.` — the page-absent
   word occurs only inside the backticked span, so A2's page gate cannot
   mask the witness; measured green at 223 assertions and kills SM5 under
   either call site. Same arm name, same expectation, all prior lines
   unchanged.
3. **E1 item 3 is falsified and withdrawn.** `RevC1Predicate` Q4 showed SM5
   IS judge-reachable (cell with the word only inside backticks: landed
   ADMIT / SM5 REJECT); the "redundant for reachable judge inputs" premise
   is false. The wrapper-level SM5 witness arm is part of the deferred
   closing package below, not landed this round.
4. **The M7–M22 lanes are newly found surviving debt, not claim scope.**
   `RevC1Predicate` Q3 found six verdict-flipping lanes beyond SM1–SM6
   (M8 `len>=4`→`>=5` admits a fabricated four-char span word; M12 line
   check via `page_words` admits a word present only inside another
   backticked span; M7 floor 3; M9/M10 case-sensitivity on STOPWORDS and
   the line set; M17 exact-vs-prefix match) plus diagnostic lanes, with a
   measured closing package (6 arms → 229 assertions, sha `f3c82574…`;
   plus the wrapper SM5 arm → 230, sha `b614e8b1…`). These lanes are outside
   the deferred row-(t) obligation; they are recorded in the SCORECARD
   Next-line debt and the round-64 lesson as round-65 candidates with the
   seat's byte-exact package cited. The claim's motivating evidence (row
   (t): SM1/SM2/SM3/SM5 survive, four arms measured green, all six red)
   is exactly what lands.
5. **C2 matcher discipline (from `RevSpotcheckCrosswalk` D3/D4).** Checks 2
   and 3 use ordered, content-shaped matchers (a suffix line carrying
   basename↔rev pairing and the word `committed`; a suffix line carrying
   `lowest` + `depth` + `consistency` + both digit-bounded scores) — token
   scans green-light inverted statements. The SCORECARD parse is
   right-split, section-bounded to `## axes`. The C2 `Bounds` paragraph
   (D2) names the non-counted items: spot-check items 5 (C1's deferred
   arms) and 6 (operator-owned SHONEN).
6. **Remedy-choice bound (F3).** Checks 1 and 4 each hard-code one of two
   admitted remedies (commit vs revert; amend vs drift-note). The plan
   elects: commit the edit (it is a verified seat self-correction) and
   append the drift note (M95 discipline: never rewrite a dated seat cell).
   The alternative remedies remain recorded in the lesson.

**Stale-219 repairs (freshness, landed with the arms).** After the arms
land, `corpus/README.md:112` and
`corpus/knowledge/compound-clause-citation-round63.md:120` carry stale
`219` citations — corrected in the same round (no source row rewrite).
**Carried gate debt.** `check_scoped_rules_v32.py` has no
`floors-registry.json` row (the r62 F17 debt re-found by
`RevC1Predicate` Q2); the round-65 candidate list names it.
