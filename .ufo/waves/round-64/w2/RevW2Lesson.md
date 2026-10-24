# RevW2Lesson — round-64 lesson falsification (wave 2)

Seat: `kotoba-r64.RevW2Lesson-2` (reviewer, leaf; no subagent dispatch). Lane repo
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, measured tip
`c019919c97ab5fe98e87a7754b4449ea4e699c99` (HEAD while reviewing: `b99fb79c`, the
measurements commit). Read-only outside this file; scratch in `/tmp/r64probe/`.
No tools installed or upgraded this seat.

Reviewed artifact: `corpus/lessons/round-64.md` at `c019919c`
(`git cat-file -p c019919c:corpus/lessons/round-64.md | sha256sum` →
`7ac44b54a0af4a0d5f575a50473fc0d1cacb24c315a0f02ff93e0153aa3dc9e2`, identical to the
worktree copy; exit 0).

## Verdict

Wave 1's lesson is mostly sound: M96's evidence and fix are real and reproducible, the
S120 snapshot hash/size/line anchors are exact, the S049 re-probe digests are internally
consistent, and nine of the twelve Falsify rows match their seats' w1 findings on
inspect. Three items do not hold as landed — one disposition claims a fix the landed
counter does not implement, one mistake row's fix was never applied (and its evidence is
attributed to the wrong artifact), and the LOG entry that the Gate leans on cites two
receipts that do not exist. Details and reproductions below.

## HIGH

### H1 — Falsify row (k) says F5/F6 are "fixed pre-data (E3.5)"; the landed C2 matchers are still flat token scans

Lesson `corpus/lessons/round-64.md:101` (row k) and `plans/round-64.md` E3.5 claim
"ordered, content-shaped matchers" and say "token scans green-light inverted statements".
The landed counter does not implement ordering, subject↔predicate binding, or distinct
suffix lines:

- `verifiers/check_r64_routed_repairs.py:185-194` (`check_control_revs`) passes a line
  that contains **both** basenames, **both** computed hash prefixes, the base, and
  `committed` — in any arrangement.
- `verifiers/check_r64_routed_repairs.py:288-297` (`check_lowest_axis`) passes a line
  containing `lowest`, `depth`, `consistency` and the two number tokens — no proximity,
  no direction.
- No code anywhere in the module tracks distinct matched line indices across checks; the
  self-test's only check-3 world is the honest reordered-table case
  (`:823-827`), and no inverted/swapped world exists (F5 explicitly required two such
  worlds; F6 required a bundled-line arm).

Reproduced in the counter's **own fixture builders** (scratch, `/tmp/r64probe/probe.py`,
`python3 -B probe.py`, EXIT:0):

```
SWAPPED_ATTRIBUTION check2 -> (True, 'round-64 LOG line names committed controls 975efae4 + 999289ca and base 35d44b4b')
INVERTED_AXIS check3 -> (True, 'round-64 LOG suffix names depth 9 < consistency 10 as lowest')
BUNDLED one-line: check2 -> (True, 'round-64 LOG line names committed controls 975efae4 + 999289ca and base 35d44b4b')
BUNDLED one-line: check3 -> (True, 'round-64 LOG suffix names depth 9 < consistency 10 as lowest')
```

The swapped world pairs `C1-do-nothing-v31.txt` with `C2-before-r62tip.txt`'s committing
rev; the inverted world is the sentence F5 names ("consistency 10 is the lowest owned
axis; depth 9 is higher"). Both score GREEN. Impact: r63 spot-check defect 3 — the exact
defect C2 check 3 exists to close — would score green in inverted form, and F6's bundling
lets one line serve checks 2 and 3. The landed honest lines are truthful, so the `4 of 4`
claim is not itself false; the **hardening claim** is.

Disposition to record: row (k) is `not fixed as described` — matcher hardening is
open debt, or E3.5's prose must be narrowed to the co-occurrence property that actually
landed (plus the two required self-test worlds).

### H2 — M97's stated fix is absent from the plan, and two of its three "plan fields" were never in the plan

M97 (`corpus/lessons/round-64.md:66-74`) says: "`plans/round-64.md` § Sources named
arXiv:2103.02722 / DOI 10.1109/ICSE43902.2021.00068 / author 'Ernst'" and "Fix: … the plan
now records it for candidates".

Measured at the tip:

```
$ git show c019919c:plans/round-64.md | sed -n '164,168p'
- **S120 (new row, opened this round):** a mutation-testing primary source
  for the load-bearing-branch pinning method (candidate: Petrovic, Ivankovic
  & Ernst, "Practical Mutation Testing at Scale", ICSE 2021 — scout opens,
  snapshots, quotes ≤25 words; tier A/B for the mutant-kills-mean-coverage claim).

$ git show c019919c:plans/round-64.md | grep -n "2103\.02722\|ICSE43902"   # no output, exit 1
$ git show c019919c:plans/round-64.md | grep -n "candidate\|lead\|opened byte"
166:  ... (candidate: Petrovic, Ivankovic
341:   Next-line debt and the round-64 lesson as round-65 candidates ...
365:`RevC1Predicate` Q2); the round-65 candidate list names it.
```

Consequences:

1. The plan still carries the wrong author (`Ernst`) and wrong venue (`ICSE 2021`) —
   uncorrected at the measured tip — so "the plan now records it for candidates" is
   false as written; no candidate rule exists anywhere in the plan at `c019919c`.
2. The arXiv id and DOI are not in the plan at any rev I can see; they live in the
   wave-1 dispatch prompt (`git grep -n "2103\.02722" c019919c` →
   `.ufo/waves/round-64/w1-spec.json:91`, `w1-dispatch.json:407`). The plan froze **two**
   wrong fields, the dispatch froze three; the lesson attributes all three to the plan.
   `ScoutS120.md:85` and `RevSourcesGate.md:139-140` then quote "plan candidate …,
   arXiv:2103.02722, DOI …" — i.e. the seats read the dispatch text as the plan's.

This is the M97 class recurring inside the round that named it: the artifact cited as
repaired still contains the defect, and the row has no demonstrable fix.

Disposition to record: M97 `fix not landed`; the plan's § Sources candidate needs the
identity correction in place (or an erratum line pointing at it), and the row's evidence
should name `w1-spec.json` for the id/DOI.

### H3 — the round-64 LOG entry asserts the after-census and cites two receipts that do not exist

`LOG.md:2606` (round-64 entry, committed at `c019919c`): "Census: before 16 W04 exit 0 →
after 16 W04 exit 0 (`census-before.txt` / `census-after.txt`)". `LOG.md:2610`: "Receipts.
`.ufo/waves/round-64/receipts/`: `C1-span-measure.txt`, `C1-span-kill.txt`,
`C2-r64-measure.txt`; `.ufo/waves/round-64/controls/`: `C1-before.txt`, `C2-before.txt`,
`noharm-base.txt`."

```
$ git ls-tree -r b99fb79c --name-only | grep "round-64/census"
.ufo/waves/round-64/census-before.txt
$ git ls-tree -r b99fb79c --name-only | grep "round-64/controls"
.ufo/waves/round-64/controls/C1-before.txt
.ufo/waves/round-64/controls/C2-before.txt
$ ls .ufo/waves/round-64/controls/            # worktree, exit 0
C1-before.txt  C2-before.txt
```

`census-after.txt` and `noharm-base.txt` exist at no revision examined (tip, measurements
commit, worktree). Yet the LOG states the after-census **result** and names both paths.
This is Q50 (a stated gate result needs a committed receipt) and the M95/Q60 class (a
citation to a path the revision does not carry) in the round-64 LOG, one round after M96
named the class. The lesson's own Gate is honest here — "After …
`census-after.txt` (round end; appended below when run)" — so the defect is the LOG
bullet, not the lesson sentence; the two must not be read together as one receipt.

## MEDIUM

### M1 — the S120 abstract Gate quote is not a literal substring of the committed snapshot

Lesson `:23-27` quotes `#abstract1.1` with an ASCII apostrophe (`suite's`), states
"(22 words)", and claims "Substring check (Q54): `grep -c` with the whitespace-normalized
form → 1 against the snapshot".

Measured (whitespace-only normalization, no character folding):

```
abstract_ascii wsnorm_count= 0
abstract_uni   wsnorm_count= 1
S1 wsnorm_count= 1
S3 wsnorm_count= 1
```

The snapshot carries U+2019: `sed -n '283p' | cat -A` →
`… assesses a test suiteM-bM-^@M-^Ys adequacy …`. The quote is a substring only after
whitespace collapse **and** an undeclared `’`→`'` transliteration. The stated `grep -c`
returns 0 for the quote as printed; the claim "→ 1" does not reproduce. This is the r62
F1 class ("The first draft quoted … which is not a literal substring of `S118…`",
`corpus/lessons/round-62.md:32`), at a low semantic severity — the words are identical —
but the check as stated is false. Q53 also applies: no `sed -n '<L>p'` output is pasted
and neither the line joins (283-284, 324-326) nor the apostrophe shaping is disclosed.
Q56 is not violated (no `byte-exact` claim is made).

Fix: print `’` in the lesson quote (or state "apostrophe transliterated"), paste the
`sed` lines, and give the runnable check (`sed -n '283,284p' … | tr '\n' ' '` →
`grep -c`/`wc -w`). Word counts re-derived independently: 22 / 23 / 22 — all ≤25.

### M2 — the C2 receipt names no measured revision

`git ls-tree` shows `receipts/` lands at `b99fb79c`, one commit after the measured tip
(commit subject: "round-64: measurements — C1/C2 receipts at c019919c"), which is fine;
`C1-span-measure.txt` opens with "C1 measure — frozen predicate at the measured rev
c019919c97ab5fe98e87a7754b4449ea4e699c99". `C2-r64-measure.txt` (570 B) does not:

```
$ grep -c "c019919c\|078eec4a" .ufo/waves/round-64/receipts/C2-r64-measure.txt
0
```

Under Q50 the receipt for a stated tip result must name that revision; the C2 receipt
names only the counter sha256 (`8f5b9f91…`) and the self-test count. Recommend a one-line
measured-rev header regenerated from the counter (the counter computes it; the file just
is not recording it).

### M3 — M98 is a mistake row with no fix by construction

`corpus/lessons/round-64.md:76-80` carries class/evidence/captured-by/fix, and its fix is
"none by this lane; the routing … stands and is executed under C2 check 1". The evidence
is reproducible (`git diff --numstat 38defdc c019919c -- .ufo/waves/round-63/w2/MutW2SplitClauses.md`
→ `82  29`, matching `LOG.md:2599` and `RevSpotcheckCrosswalk.md` F7, and the spot-check's
"41+/13-" does not reproduce — `RevSpotcheckCrosswalk.md:32`) and the non-author rule
justifies not editing. But the row meets the letter of the Mistakes shape while failing
the "fix shown able to fail" bar; only M96 of the three rows does (see Verified below).
Recording it as a `recorded-only` class row, not a fixed one, is the honest label.

## LOW

### L1 — Q54: two of the three word counts carry no `wc -w` command

The lesson cites Q54 as its own warrant. Q54 requires the command "on that line or one of
the next two lines". Line 25 "(22 words)" → line 27 has a bare `wc -w → 22` (command name
and result, no input pipeline); line 30 "(23 words)" → lines 31-32 are quote
continuation, no command; line 33 "(22 words)." → lines 34-35 are the identity
correction, no command. Two of three counts are exactly the M86 pattern Q54 exists to
prevent.

### L2 — support-quote citation shape: `#S1.p1.1` is cited as "line 324" but spans 324-326

`awk 'NR==324'` is the quote's first line; 325-326 carry the rest (the paragraph's id
marker is at 319). The `#abstract1.1` quote uses a range for a 2-line span (283-284), so
the support quote should read 324-326. `#S3.SS2.SSS2.p1.1` lines 780-782 and
`#abstract1.1` 283-284 are exact. Inside the round that mints Q60, this is the same
under-specified-citation shape at the line level.

### L3 — row (h) is labelled "bound-recorded" for something E2.5 fixed

`CriticC2Bound` §2's counterexample was moving `BASE_REV` to another red/partial revision
(the r63 guard tested `>= total`). The landed r64 counter refuses unless the base scores
exactly zero:

```
$ sed -n '391,395p' verifiers/check_r64_routed_repairs.py
    base_closed, total = base_control(root)
    if base_closed != 0:
        ... refuse ...
```

and its self-test carries the repointed-green arm (`:880-887`). The named attack is
blocked by E2.5, so "bound-recorded" understates the landed state; either say
"fixed pre-data (E2.5)" or state the remaining exposure precisely (a relocation to a
different 0-of-4 revision). Underclaiming, not a false statement.

## Spot-checks against w1 seat reports (three named, all twelve rows inspected)

| row | source seat(s) cited | what the w1 report actually says | verdict |
|---|---|---|---|
| c | `RevC1Predicate` Q1 | "C1's frozen predicate is necessary but not sufficient: it can be met, with zero mutation resistance, by four dead assertions — and I built the file." (`RevC1Predicate.md:119-122`) | accurate |
| i | `ScoutReceiptSweep` | "Strict M95 instances: 15 (10 unique path@rev pairs). Check 2 as planned covers 2 of those 15" (`ScoutReceiptSweep.md:11`); the 8 uncovered pairs are named in `LOG.md:2596` with committing revs | accurate, and the census line exists |
| k | `RevSpotcheckCrosswalk` F5/F6 | F5: "token-only matchers pass the exact false statements the routed items correct… A correction that repeats item 3's error in swapped form would score GREEN" (`:159-176`); F6: "checks 2/3/4 do not require distinct suffix lines" (`:177-183`) — both still true of the landed counter | **misstated: row says fixed** (H1) |

Also checked and holding: row a (`ScoutQualityDebt.md:189` names `LOG.md:2576` and its
three tokens; `MutR64Counter.md:116` M2 "check 2 scans the whole LOG blob" SURVIVED),
row b (`ScribeReportSkeleton.md:20` 19 call sites, 2 in a 3-iteration loop; E1.2/E2.4
arithmetic 17 + 2×3 = 23 agrees with the receipt's `runtime 23 matches static 17 fixed + 2
loop sites x 3 arms = 23`), row d (`CriticC1Bound` §3 off-manifold witness), row e
(`RevC1Predicate` Q4/E3.3), row f (`RevC1Predicate.md:332-335` shas `f3c82574…`/`b614e8b1…`,
229/230 assertions), row g (`RevC2Checks.md:46` "three vacuous LOG checks give base 1 of
4, target 4 of 4"), row h attribution (`CriticC2Bound` §2), row j
(`SCORECARD.md:375` carries the erratum naming `849a546e`, the 205-assertion stale bytes
and `2ba4547f`), row l (`SHONEN.md:10` "the earlier 'both fixed in round 13' wording is
withdrawn here as falsified per `ScribeSHONEN` F1", box stays `[~]`).

## Verified at the measured tip (what held)

- M96: both controls absent at `35d44b4b` (`git cat-file -e` exit 128 for each, measured);
  `LOG.md:2604` names both committing revs, base `35d44b4b`, both basenames and
  `committed`; the counter prints `r63 routed defects closed 0 of 4` at the pinned base
  (`.ufo/waves/round-64/controls/C2-before.txt`, committed at `c019919c`) and `4 of 4` at
  the tip (`receipts/C2-r64-measure.txt`, committed `b99fb79c`, exit 0). The fix is shown
  able to fail in both directions.
- S120 Gate metadata: snapshot committed, 571,600 B, sha256 `15963c3e…` recomputed
  identical; `#abstract1.1` at lines 283-284, `#S1.p1.1` text at 324-326,
  `#S3.SS2.SSS2.p1.1` at 780-782; all three quotes ≤25 words (22/23/22, own count after
  normalization).
- S049 re-probe: `SOURCES.md:236-237` (17,252 B / `dae9d3ec…`; 404 / 389 B) and the
  2026-10-24 search-log entry agree with `ScoutS049.md:13-31,83-85` on bytes, digests and
  all three timestamps; the lesson's "Vercel cache HIT" caveat matches the scout's own
  residual (`ScoutS049.md:111`).
- Census before: `.ufo/waves/round-64/census-before.txt` has 16 `W04` rows plus the `ok`
  line (117-row registry total is not restated in the file; the 16 count reproduces).
- Errata E1-E3 present in `plans/round-64.md` at `5613392d` (pre-data claim holds for E3:
  `grep -c "Erratum E3"` → 1) and the row-to-erratum keys (E1.1/E1.2/E1.3, E2.4/E2.5,
  E3.1/E3.2/E3.3/E3.5) each resolve to a real item.

## Residual risk and verification gaps

- No live S049 re-probe from this seat (no network fetch run): the digests are verified
  as internally consistent, not as today's server behaviour.
- H1's probe drives the counter's own fixture builders and the real `check_*` functions
  under a temp repo, but I did not run `--self-test` in-lane (it would write under the
  lane root; read-only bound).
- Line citations are from the committed bytes at `c019919c`; the lesson's own line
  numbers were checked against that file only.
- The 117-row census total is taken from the lesson/LOG; the receipt itself prints 16
  `W04` findings and one `ok` line, so the row total is [INFERENCE] from the registry
  size, not from the receipt text.
- Not reviewed here (other wave-2 seats own them): the v32 arm bytes, the r64 counter's
  four checks' semantics beyond the matcher issue above, the SCORECARD/LOG other lines,
  and the receipt-template wording.
