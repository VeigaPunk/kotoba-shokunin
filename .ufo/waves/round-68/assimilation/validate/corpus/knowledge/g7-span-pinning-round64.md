source: S120 — Petrović, Ivanković, Fraser & Just, "Practical Mutation Testing at Scale: A view from Google", IEEE TSE 48(10):3900-3912 (2022; Crossref metadata, publisher HTML not opened), DOI 10.1109/TSE.2021.3107634; preprint arXiv:2102.11378v2 (26 Feb 2021), §1 (`S120.page:S1.p1.1`, quote at line 324) and §3.2.2 (`S120.page:S3.SS2.SSS2.p1.1`, line 781), committed snapshot `.ufo/waves/round-64/snapshots/S120.page` (571,600 B, sha256 `15963c3e…`); internal evidence `.ufo/waves/round-63/w2/MutW2V32.md` §11 — the SM1–SM6 battery, the four measured arms and the 20 000-cell divergence note. The arms' receipts rest on `verifiers/check_scoped_rules_v32.py`'s self-test bytes, not on S120.
verified-at: 2026-10-24 — base `078eec4`, v32 sha256 `12d093a1…`: `self-test: 0 failure(s) over 219 assertions`, exit 0 (re-run by this seat); 223 on `landed_plus_spanfix7` (sha256 `ae84673e…`) per MutW2V32 §11; branch at `verifiers/check_scoped_rules_v32.py:1055-1067`
recheck: 180d — `python3 -B verifiers/check_scoped_rules_v32.py --self-test`: all four printed lines and the assertion count against § The measured record; sooner on any mutation reported surviving this branch

*Round-64 landing note (2026-10-24): the four arms are landed at the round-64 integration commit; the `(sha256, 223)` pair measured on the landed bytes is recorded in `.ufo/waves/round-64/receipts/C1-span-measure.txt` (the kill battery: SM1–SM6 all red, each by its own arm's `check()` label except SM4/SM6 which the pre-existing `eligible world` arms kill — attribution per the kotodama R64-M9 lesson). Arm 4's cell is the MutSpanArms §6 hardened form (`The tool writes quota nightly and \`mode quota\`.`), which pins SM5 at the component level under either call site (landed ADMIT / SM5 REJECT through `action_conjunct` with a hand-built `lines` argument). At `judge()` level SM5 is NOT discriminable — `judge()` derives `lines = page.splitlines()` (E1.3; wave-2 `MutW2M7M22`) — the wrapper arm of the deferred closing package (230 assertions, `a198aa50…`) closes that lane. Attribution correction (wave 2): SM6's first FAIL is the pre-existing A2 cell arm, with arms 2–4 as collateral; SM4 is the `eligible world` kill.*

## What it is

A guard branch that can only reject is **load-bearing**; with no assertion that
turns on it, it is an **unrecorded bound**. The v32 `span_missing` arm
(`g7_conjunct`, `verifiers/check_scoped_rules_v32.py:1055-1067`; the plan writes
`:1055-1068`, which adds the function's trailing `return []`) rejects an action
cell whose backticked span carries words found in neither the cited line nor the
page. Six mutants of it were scored against the committed 219-assertion
self-test: SM1 (branch deleted), SM2 (`len(word) >= 4` floor dropped), SM3
(`STOPWORDS` filter dropped) and SM5 (cited-line check dropped) all survive at
exit 0. SM1 is an evasion, not a cosmetic gap:

```
cell: 'The configuration stores project rules using glob syntax and `exfiltrates credentials`.'
  LANDED                G7=REJ  G9=-    ACTION=REJECTED
  SM1 (branch removed)  G7=-    G9=-    ACTION=ADMITTED  <-- EVASION
```

`content_words()` strips backticked spans, so A2's forward fraction and page
containment cannot see the fabrication, and G9's page gate skips a clause the
page lacks — the branch added to close that hole had no test that could tell it
was there. S120 states the general defect: `However, code coverage alone might
be misleading, in particular when program statements are covered but the
expected program outcome is not asserted upon` (§1; citation markers `[2], [3]`
removed, line breaks joined with single spaces). A `0 failure(s) over 219
assertions` receipt is then true and silent.

## The method

Four arms, one per load-bearing lane, texts byte-for-byte as measured in
`MutW2V32.md` §11.

1. **Positive witness for the branch — the evasion cell.** Assert the fabricated
   span is rejected, on the guard's own reason line (`A2 G7: a backticked span
   whose words occur in neither the cited line nor the page is rejected`).
   Kills SM1.
2. **Negative witness for the stopword filter.** `` `because otherwise` `` is
   *not* rejected: every ≥4-character word in the span is a stopword. Kills SM3.
3. **Negative witness for the length floor.** `` `ox it` `` is *not* rejected:
   no span word reaches four characters. Kills SM2.
4. **Negative witness for the cited-line rescue.** `` `mode quota` `` is *not*
   rejected when the word is in the cited line but absent from the page — and
   this arm calls `g7_conjunct` **directly**, not `action_conjunct`. Kills SM5.
   The cell is the round-64 hardened form (`MutSpanArms` §6): the page-absent
   word occurs only inside the backticked span, so `action_conjunct`'s A2 page
   gate cannot mask the witness — measured on the landed bytes, the same
   fixture through the wrapper discriminates SM5 (landed ADMIT / SM5
   REJECT); `judge()` level stays component-masked (E1.3).

Two disciplines make the arms discriminating rather than decorative. **Isolate
the lane when a wrapper decides first:** `action_conjunct` runs A2's
page-containment arm before G7, and with a cell whose page-absent word also
occurs *outside* the backticks the wrapper's earlier arm supplies the False and
the assertion would pass for the wrong reason — so the cell keeps the word
inside the span only, and the arm still calls the conjunct under test directly,
saying why. **Assert the reason, not only the boolean:** `named(reasons,
needle)` pins the arm that produced the verdict, so another arm's True/False
cannot satisfy it.

The kill rule is two-part: each mutant must be red **and** its red line must be
the arm aimed at it. SM4 is red only through `FAIL eligible world` (a kill of the mutant, not a witness for the arm). SM6's first FAIL is the pre-existing `A2: a cell the cited line supports passes`, with arms 2–4 failing on their own labels as collateral (wave-2 attribution per `ConnW2Fleet`/`RevW2Entry`).

Frozen predicate: `python3 -B verifiers/check_scoped_rules_v32.py --self-test`
prints all four lines and exits 0 —

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
```

## The measured record

| state | assertions | exit | SM1 | SM2 | SM3 | SM4 | SM5 | SM6 |
|---|---|---|---|---|---|---|---|---|
| r63 bytes (`12d093a1…`) | 219 | 0 | survives | survives | survives | red (`eligible world`) | survives | red (`eligible world`) |
| + the four arms (arm 4 the hardened cell) | 223 | 0 | red (arm 1) | red (arm 3) | red (arm 2) | red (`eligible world` × 5) | red (arm 4) | red (pre-existing `A2: a cell the cited line supports passes` FIRST; arms 2–4 also fail on their own labels — collateral) |

Measured in §11: the arms are green on the r63 bytes plus the arms
(`landed_plus_spanfix7`, sha256 `ae84673e…`; `0 failure(s) over 223
assertions`) and turn all six mutants red; the nine splitter mutants stay red on
top of them (`sib_M1..M8 on landed_plus_spanfix7 exit=1 KILLED (all nine)`); and
`judge()` on the committed rows is byte-identical before and after (`4 of 4`
backed, `committed == LANDED+4assertions: True`). The arms add coverage without
moving what the lane certifies.

## Limits

- **A survivor is not automatically a gap.** S120 §3.2.2: `Equivalent mutants,
  which are semantically equivalent to the mutated program, are a plague in
  mutation testing and cannot generally be detected automatically` (line breaks
  joined; no other shaping). SM2, SM3 and SM5 were argued *not* equivalent by
  divergence rather than assumed: over 20 000 random cells SM2 differs on 3 607 (wave-2 re-measures: 3 567 / 3 505 — the §11 generator is unrecorded, so the figure is attributable, order-verified, not exactly reproducible) ;
  SM3 differs on any span whose only ≥4-character word is a stopword; SM5
  differs on a span word present in the cited line but absent from the page.
  This record is a divergence set, not a kill rate — a mutant whose divergence
  set is empty survives legitimately.
- **Red is not discriminating.** SM4 and SM6 are killed by the eligible-world
  arm, not by any of the four; the page-check and always-fires semantics of the
  branch still have no G7 arm.
- **Hand-built cells, one function.** The arms pin `g7_conjunct`'s `span_missing`
  computation on constructed cells; they do not pin its priority against G7's
  identifier arm or G9, nor `supported()`'s four-character prefix rule.
- **The class was latent.** MutW2V32 scanned for a committed action cell that
  trips the evasion and found none; the evidence is the constructed cell plus the
  SM1 admission, not a corpus instance.
- **Out of scope.** The W8 escape class and A2's F6 compound-purpose bound stay
  carried debt (`SCORECARD.md` round-64 Next line); this entry claims neither.

## How to re-run

```
python3 -B verifiers/check_scoped_rules_v32.py --self-test | tail -1   # 223 assertions
grep -c 'A2 G7:' verifiers/check_scoped_rules_v32.py                   # 7 after the four arms land; 3 before
```

Provenance of the method: the battery is `MutW2V32` §11 (round 63, post-close,
measured on the file the L1 had landed); the arms land as C1 of
`plans/round-64.md`; the branch came from erratum E3 (round 63). S120 supplies
the frame — mutation analysis over statement coverage, the undetected mutant as
the test goal — not the arm design.
