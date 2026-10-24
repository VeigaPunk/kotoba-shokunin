source: S121 — Madeyski, Orzeszyna, Torkar, Józala, "Overcoming the Equivalent Mutant Problem: A Systematic Literature Review and a Comparative Experiment of Second Order Mutation", IEEE TSE 40(1):23-42 (Jan 2014), DOI 10.1109/TSE.2013.44 (from the opened PDF's header line 90); author-hosted preprint v.2 PDF, the artifact opened and quoted — abstract (PDF text line 64) and the HOM-generation-strategies paragraph (lines 1174-1176), committed snapshot `.ufo/waves/round-65/snapshots/S121.pdf` (1,126,684 B, sha256 `bad1b681…`) with extracted text `S121.txt`; S120 (the round-64 pinning-method source) and the internal evidence `.ufo/waves/round-64/w2/MutW2M7M22.md` §5/§8 (the M20/SPAN_FIRST/SPAN_LAST/M11 lanes measured at judge level on the round-64 landed bytes). The arms' receipts rest on `verifiers/check_scoped_rules_v32.py`'s self-test bytes, not on S121.
verified-at: 2026-10-24 — tip `80bb8921`, v32 sha256 `b6cfc764…`: `self-test: 0 failure(s) over 234 assertions`, exit 0 (re-run on committed bytes via `git archive`, receipt `.ufo/waves/round-65/receipts/C1-close-measure.txt`); the span branch at `verifiers/check_scoped_rules_v32.py:1055-1067`
recheck: 180d — `python3 -B verifiers/check_scoped_rules_v32.py --self-test`: all printed predicate lines and the assertion count against § The measured record; sooner on any mutation reported surviving this branch

*Round-65 landing note (2026-10-24): the deferred round-64 closing package lands — six arms of `RevC1Predicate` §3 plus the wrapper-level SM5 arm, and four new arms for the judge-level lanes `MutW2M7M22` found the package leaves open. Suite 223 → 234 assertions; the `(sha256, 234)` pair is measured on the committed bytes at `80bb8921` (receipt `C1-close-measure.txt`; kill battery `C1-close-kill.txt`: 17 named lanes red with per-arm attribution, the equivalents M19/M22 green, and the pkg7 control world — the same bytes minus the four round-65-new arms, 230 assertions — killing nothing the new arms own: SPAN_FIRST, SPAN_LAST and M20 each survive it, so those three arms are the load-bearing pins; the M11-exact-case arm is a named witness only, the M11 lane being killed first by pre-existing main-world collateral in every world per `MutW2M7M22` F7). The wrapper SM5 arm is a component-level pin — through `judge()` SM5 is indiscriminable (E1.3 stands, `MutW2M7M22` §2b). A `floors-registry.json` row registers the instrument at 234 so the arms cannot be deleted with every gate green (r62 F17, re-found by `RevC1Predicate` Q2).*

## What it is

The round-64 landing pinned the `span_missing` branch with four arms but
deferred its seat-measured closing package, and the round-64 wave-2 mutation
seat then found the package itself leaves lanes open. The round-65 landing
closes the deferred debt and the newly found lanes in one suite:

- **The six package arms** (`RevC1Predicate` §3, byte-exact; counts re-measured
  by `MutW2M7M22` §4): the M8 fabricated-span admission (floor 4→5), the M7
  over-rejection floor (4→3), the M12 backticked-only line presence, the M17
  page-prefix support, the M9 capitalised stopword, and the M10 capitalised
  line word.
- **The wrapper SM5 arm** (the package's 7th arm): pins the cited-line check at
  the component level with a page that deliberately lacks the line — a
  judge-equivalent mutant, kept as a component pin like the M12 arm.
- **SPAN_FIRST / SPAN_LAST** (`MutW2M7M22` §8a — judge-level evasion): a cell
  with two backticked spans smuggles the fabrication past the branch whenever
  the fabricated span is not the one the mutant inspects. Two arms, one per
  direction: a fabricated first span is rejected when an honest second span
  follows it, and a fabricated second span is rejected when an honest first
  span precedes it. S121 is the design source for this witness shape: coupling
  two first-order sites into one second-order mutant is a studied strategy,
  measured to reduce equivalent mutants and test effort — the coupled
  honest-plus-fabricated cell is a first-class adequacy witness, not an
  artificial one.
- **M20** (`MutW2M7M22` §5 — judge-level over-rejection): the page-set
  construction (`page_words`, which keeps backticked occurrences) differs from
  `content_words` (which strips them); a span word whose only page support is a
  backticked occurrence must NOT be rejected. One arm pins the distinction.
- **M11-exact-case** (`MutW2M7M22` §8b — judge-level over-rejection): a
  capitalised span word whose exact-case occurrence is on the page (and not on
  the cited line) must NOT be rejected; the lowercase-only reading of the page
  set is the correct one. The arm is a named witness — the M11 lane dies on the
  pre-existing main-world arms first (F7 attribution), in every world.

## The measured record

`python3 -B verifiers/check_scoped_rules_v32.py --self-test` on the committed
bytes at `80bb8921` (sha256 `b6cfc764…`):

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 234 assertions        # exit 0
```

Kill battery (receipt `C1-close-kill.txt`, one exact-string replacement per
lane on the committed bytes): SM1←arm 1 of the round-64 four, SM2←arm 3, SM3←
arm 2, SM5←arm 4 (own labels); SM4 first via the M17 prefix arm (then the
pre-existing `eligible world` lines); SM6 first via the pre-existing A2 cell
arm (attribution per the kotodama R64-M9 rule); M7/M8/M9/M10/M12/M17 each by
their own package arm; M14 by the M12 arm; SPAN_FIRST and SPAN_LAST by their
own new arms; M20 by its own new arm; M11 by pre-existing collateral with the
new arm FAILing as witness. Two-sided measure per Q47: the
semantics-preserving equivalents M19 (`sorted`→`list`) and M22 (the `L`-guard)
both survive green on the landed bytes, and the set is not a fixed published
list — the witnesses are generated from the branch's own filters.

Do-nothing controls (Q25/Q37): the pkg7 control world (candidate minus the four
round-65-new arms, 230 assertions) admits SPAN_FIRST, SPAN_LAST and M20 at exit
0 — padding or partial adoption cannot reach the declared predicate; and the
v31 predecessor prints `survivors closed 5 of 6` over 201 assertions.

## Limits

The M11 arm never becomes the first kill (the unlowered page set breaks the
main eligible-world fixtures in every world) — it guards the named witness for
a future fixture rewrite, it does not carry the lane today; M18/M19/M22 remain
deliberately unpinned diagnostic/equivalent lanes per `MutW2M7M22` F7; the
suite is a self-test — the trust boundary recorded in
`verifiers/check_assertion_floors.py` (the guard detects silent arm deletion
via the new registry row, not a self-test that prints a fake count).
