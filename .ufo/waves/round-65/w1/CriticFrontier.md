# CriticFrontier — round-65 wave-1 frontier attack (S121 + census)

Seat: `kotoba-r65.CriticFrontier` (critic, leaf — no dispatch). Axes: coverage.
Attack surface: the frontier step of `plans/round-65.md` as landed at tip
`0e104f49` (L1 landed; wave executes post-landing). Current HEAD `2a8eba5`
includes round-66 commits; both tips probed below.

No tools installed (pacman paused per orchestrator ruling; nothing needed —
pdftotext-extracted snapshot `S121.txt` was already committed).

## Verdict table

| # | Frontier question | Verdict | Severity |
|---|---|---|---|
| Q1 | S121 tier-A defensible (author-hosted preprint, not the IEEE record)? | **Yes — defensible** | holds |
| Q2 | teaches cell scoped, not global? | **Yes — scoped** (row + teaches both carry the disclaimer) | holds |
| Q3 | sourced claim honestly met — does the two-span design text rest on S121? | **Mostly — one loose sentence + one misattributed support quote** | low (fixable) |
| Q4 | census exit-0 at the tip? | **Yes — holds at `0e104f49` AND at live HEAD `2a8eba5`** | holds |

## Q1 — tier A defensible: HOLDS

The artifact is self-identifying as the journal version: `S121.txt:106`
`IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, VOL. 40, NO. 1, JANUARY 2014
(PREPRINT V.2)`; DOI at line 90 `Digital Object Identifier no.
10.1109/TSE.2013.44`; author-affiliation block at lines 74-84 names
`madeyski.e-informatyka.pl` — the very host the URL is served from, so the
host's authority over this file is internal evidence, not inference. Embedded
page markers `31`/`32`/`41`/`42` (lines 1359, 2525, 2855…) corroborate the
`23-42` pagination.

```
$ sha256sum .ufo/waves/round-65/snapshots/S121.pdf
bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3   ✓ = lesson/row/plan
$ wc -c .ufo/waves/round-65/snapshots/S121.pdf
1126684   ✓ = 1,126,684 claimed
```

Disclosure is honest: the row anchor says "author-hosted preprint v.2 … the
artifact opened and quoted"; the lesson Gate says "the publisher record was not
opened"; quotes are located at *preprint-text* line numbers, never IEEE page
numbers. Precedent: S120's tier A rests on the arXiv HTML with the IEEE HTML
never opened — same disclosure pattern, accepted by the r64 gate and r65/r66
spotchecks. The independent r65 verifier spotcheck re-confirmed via Crossref
(`round-65-verifier-spotcheck.md:60`, **agree**). No counterexample found.

## Q2 — teaches scoped: HOLDS

Row scope cell (SOURCES.md:132): "…**Scoped to SOM's measured advantages; the
lane's two-span verifier arm is the lane's application, not the paper's
object.** Author-hosted preprint v.2…" — explicit boundary, mirrors the r64
S120 convention. Teaches cell = the 16-word abstract quote + support quote;
both verified whitespace-normalized, each count 1:

```
q1 "The experiment indicated that SOM in general and JudyDiffOp strategy
    in particular provide the best results"  count=1, 16 words, S121.txt:64-65 ✓
q2 "Empirical results suggest that applying SOMs reduced the number of
    mutants by approximately 50%, without much decrease in the quality of
    the test suite."                          count=1, 24 words, S121.txt:1174-1176 ✓
```

## Q3 — sourced claim: HOLDS with two defects (fixable, low)

The plan's cited use — "cites S121 for the second-order (two-span) witness
design" — is met literally: `g7-span-closure-round65.md:27` "S121 is the
design source for this witness shape". Two attacks land:

**D1 (low): "design source" overstates provenance.** The SPAN_FIRST/SPAN_LAST
arms' actual design is measured `MutW2M7M22` §8a (round-64 wave-2, lines
309-345: `BACKTICK_RE.findall(cell)[:1]`/`[-1:]` iterator-restriction mutants
surviving all three suites — internal evidence the entry's `source:` line
already cites). S121 entered only this round, post-design; what it lends is
*class legitimacy* (a coupled mutant is a studied, first-class witness), not
the shape. Worse, the analogy is inexact: SOM couples **two faults**; the
lane's arm couples a **fault + a control** (honest span). The S121 mechanism
the row tacitly relies on — "[if] one of the two first-order mutants is
non-equivalent, then the second order mutant is non-equivalent" ([65, Table I],
S121.txt:2634-2638) — is about equivalent-mutant avoidance, not iterator
coverage. Smallest safe correction: entry line 27 → "S121 grounds the class:
coupling first-order sites into one second-order mutant is a studied,
measured strategy; the lane's honest-plus-fabricated cell is its analogue
(the lane's inference, designed at `MutW2M7M22` §8a)". One sentence; the row
needs no change since its scope already disclaims the application.

**D2 (low): support quote provenance + wrong section number.**
(a) q2 (lines 1174-1176) is the paper *reporting Polo et al. [65]'s* result —
paragraph opens "The opposite approach … is a technique used by Polo et al.
[65]. They introduced three different algorithms …" — yet row and lesson
present it unmarked alongside the paper's own abstract finding. The paper's
own equivalent claim exists (Finding 2, lines 2071-2073; conclusions line
2869-2871). Correction: label it "(the paper reporting Polo et al. [65])" or
swap to Finding 2.
(b) The row anchor says "**§5** HOM-generation strategies paragraph" — but
lines 1174-1176 sit in **§4 "Higher order mutation testing strategies"**
(heading at line 1126-1127; §5 "Experimental setup" opens at line 1465-1466).
Confirmed: `sed -n '1125,1135p'` shows `4 / Higher order mutation testing
strategies`; `1464,1470p` shows `5 / Experimental setup`. Correction: `§5` →
`§4` in SOURCES.md:132 anchor cell (the entry's `source:` line cites only the
text-line numbers, which are correct — no entry edit needed for this half).

Impact: coverage axis only. Neither defect reaches the kill battery, the
counted predicate, or the census — the S121 row's *substantive* claim (SOM is
measured; coupling is designed) is correctly supported by q1.

## Q4 — census exit-0: HOLDS at both revs

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
    --root /home/vgpnk/Projects/shokunin kotoba        # live HEAD 2a8eba5
16 W04 lines (identical set to census-before/after.txt)
kotoba	ok	…/corpus/SOURCES.md
EXIT=0                                          # 120 rows at HEAD (S122 added r66)

# against the exact frontier-tip registry bytes:
$ git show 0e104f49:corpus/SOURCES.md > /tmp/r65lane/corpus/SOURCES.md
  (symlinks for used-by roots: corpus/knowledge, corpus/lessons,
   corpus/QUALITY.md, SKILL.md → live lane; no used-by path was deleted
   0e104f49→HEAD, verified via `git diff --name-status`)
$ sources-census.sh validate --file /tmp/r65lane/corpus/SOURCES.md
16 W04 lines + file	ok	/tmp/r65lane/corpus/SOURCES.md
EXIT=0                                          # rows=119 — reproduces
                                                # census-after.txt byte-set
```

`git diff 0e104f49 HEAD -- corpus/SOURCES.md`: only `+S122` row + 2
search-log lines (round-66, append-only). The saved `census-after.txt`
(119 rows, exit 0) is internally consistent and independently reproduced by
`round-65-verifier-spotcheck.md:62` and this seat.

## Claims supported / falsified

- **Supports**: frontier step (S121 admit + census) — holds at both revs.
- **Falsifies** (narrow): the entry's claim text at line 27 "design source"
  (D1) and the row's `§5` section pin + unmarked [65] provenance (D2). All
  fixable with ≤3 localized cell/sentence edits; none reach a counted
  predicate. Recommend routing to next round's corrections, not a
  landing-blocker.

Report: `.ufo/waves/round-65/w1/CriticFrontier.md`
