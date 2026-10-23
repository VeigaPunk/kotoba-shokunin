# FalsifyBeforeState — C1 before-state re-measure (round 62 wave 2)

Seat: `KotobaR62.FalsifyBeforeState` (reviewer, leaf; no subagents). Date: 2026-10-23.
Scope: re-run the targeted searches behind `.ufo/waves/round-62/controls/absorption-before.txt`
("before-state = 0 of 5 errata measured arm-level against the landed counter"), attack the
filter's breadth (missed arm-level receipt vs. non-arm hit), over `.ufo/waves/round-61/` at
the r61 tip `a745411c66d4765e9ac0ce48f1d96c34f425dab4` and over the fleet r61 report
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-61/kotoba.md`. Lane read-only; only this
file was written. Installs: none (`git`/`grep`/`sha256sum`/`python3` suffice; RULES.md read).

## Verdict (one line, as requested)

**The 0 does NOT stand under the control's own stated criterion** — `C1-worlds.txt` is a
committed receipt naming the landed sha that records arm-attributed reject verdicts for
genuine **E2b (W2)** and **E2c (W1)** class instances, so the criterion's (a)∧(b) is met
for 2 of 5, not 0. The narrower claim "0 of 5 seat attack tables re-scored on the landed
counter" still stands and is the honest before-state.

## Commands re-run (exact, with outputs)

R61 tip pinned: `git rev-parse HEAD` at lane tip `e6da78bbe420722dd18a13182a7c4b64ce02f005`;
`git diff --stat a745411…e6da78b -- .ufo/waves/round-61/` → **empty, exit 0** (no drift; the
working-tree census equals the tip census). Instrument absent at r61 tip confirmed:
`git cat-file -e a745411:verifiers/check_erratum_absorption.py` → exit 128 "exists on disk,
but not in 'a745411…'".

```
$ sha256sum verifiers/check_scoped_rules.py
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  verifiers/check_scoped_rules.py   (matches control)

$ python3 -B verifiers/check_scoped_rules.py --self-test | tail -2
worlds reject 7 of 7; eligible rows pass 4 of 4
self-test: 0 failure(s) over 189 assertions          (exit 0; matches control)

$ git grep -l '5a5adc' a745411 -- .ufo/
C1-v3-measure.txt, controls/C1-base.txt, receipts/C1-worlds.txt, wave/ExecCounterV3.md
   (same four files as the control; 6-char prefix catches every longer spelling)

$ git grep -l '5a5adc' a745411            # whole tree
   the same four + LOG.md + SCORECARD.md + corpus/knowledge/scoped-rules-counter-round61.md
   (three prose artifacts outside .ufo/waves/round-61/, none a receipt recording verdicts)

$ git grep -c -E 'MutA1|MutA2|MutA3|MutA4|MutFixtures' a745411 -- \
    .ufo/waves/round-61/receipts/ .ufo/waves/round-61/controls/ .ufo/waves/round-61/C1-v3-measure.txt
   exit 1 — 0 files. Five-seat hit count = 0 (matches control lines 27–31).

$ git grep -n -E 'E2b|E2c|E2e|E2f' a745411 -- <same receipt set>
   only receipts/C1-worlds.txt:7  ("errata E2-E2e" comment) — matches ScoutPriorReceipts.

$ for f in MutA1 MutA2 MutA3 MutA4 MutFixtures; \
    do git grep -c '5a5adc' a745411 -- .ufo/waves/round-61/wave/$f.md; done
   0 / 0 / 0 / 0 / 0 — all five seat greps reproduce.

$ git grep -c 'check_scoped_rules' a745411 -- <same receipt set>
   C1-v3-measure.txt:1, controls/C1-base.txt:1, receipts/C1-worlds.txt:2
   → no receipt names the counter file without naming its sha (sha filter is not leaky here).

$ git grep -l -i -E 'errata|erratum' a745411 -- .ufo/waves/round-61/ (non-wave)
   C1-worlds.txt, wave-dispatch.json, wave-spec.json → no extra verdict receipts.
```

r61 report (fleet checkout, 53 lines): `5a5adc94` appears only on lines 9 (draft
provenance) and 28 (self-test/--fetch/base receipts); the five seat names appear only on
lines 9 and 40, and line 40 calls the amendments "pre-data" attacks. `grep -icE
'arm-level|landed counter'` → **0**. Confirmed: the r61 report claims no arm-level
re-measurement of the attack rows against the landed bytes.

## Breadth attack — where the filter is wrong

**No false hits.** Nothing counted that should not be — the count was 0, so no false hit is
possible; the exclusion set (the four sha-naming files) was correctly enumerated and every
exclusion reason was verified: C1-base.txt = `--rev f3246d14` base-exit only, C1-v3-measure
= `--fetch` snapshot/live counts, ExecCounterV3.md = the draft's own self-test.

**A false 0 exists under the stated criterion.** The control's criterion (lines 15–16):
a receipt "(a) names the landed counter sha 5a5adc94 AND (b) records a reject/accept
verdict for an instance of one of the five erratum classes". `receipts/C1-worlds.txt`
(`b4a8d2ee`, sha256 `70f53c9f…` at r61 tip) satisfies (a) at lines 6/14/52 and satisfies
(b) on the counter source's own class mapping (`verifiers/check_scoped_rules.py` comments
at r61 tip, lines 2373–2419):

- **E2b — W2 (line 16): `reject=True arm=A3`, reason "URL …/de/memory.md is a rendering
  alias of the committed row S112 URL".** Class-faithful: W2 is a fresh row rejected *by*
  the added A3(b) disjunct — exactly E2b's class. The r61 plan calls W2's fixture receipt
  "pins A3(b)" (plans/round-61.md:158).
- **E2c — W1 (line 15): `reject=True arm=A4`, reason "snapshot sha256 … is already
  recorded by base row S010 and the teaches cell declares no supersedes".** Class-faithful:
  rejected *by* E2c conjunct (iv) — i–iii pass (committed fixture bytes, verbatim quote,
  honest stamp); plan: "W1's forged S103 row … → A4(iv) rejects" (round-61.md:175).
- **E2f — W6 (line 20): `reject=True arm=A2` by the pre-E2f support fraction
  (5 of 8 < 6).** Member of E2f's *surface* class (invented-action cell, "ExecKeyForms
  invented action") but the firing reason is the unamended conjunct — a true E2f instance
  (passes support, caught only by G5/G7/G9) would *survive* this counter, so W6 records a
  verdict but carries **zero absorption information**. Literal-(b) would count it; it is
  still not an erratum-guard measurement.
- **E2e — no instance.** W3 (`rules`) and W5 (`patterns`) fail the *key-name* conjunct
  (pre-E2e letter); E2e's class is guarded-form mutants on canonical keys — none present.
  W7 is generic A1. **E2 — no instance:** no world is a re-open failing url_key identity.

So under the stated (a)∧(b) criterion the before-state is **2 of 5** (E2b, E2c; 3 of 5 if
W6's surface-instance verdict is admitted literally), and the control's exclusion sentence
"none runs an instance of E2/E2b/E2c/E2e/E2f" (lines 23–25) is **false as written** — W1
and W2 are committed, sha-named, arm-attributed class instances. ScoutPriorReceipts's own
W-line table (lines 116–122) concedes W2 arm=A3 rendering-alias and W1 arm=A4 sha-alias.

**What survives:** every narrower claim. The five seat attack tables (MutA3's 19 rows,
MutFixtures S1, MutA4's 12+3, MutA1's 15, MutA2's 10) were never re-scored on the landed
bytes (0 sha-mentions in all five reports; each report disclaims v3 — draft/v2-only);
`C1-worlds.txt` runs *one synthetic instance per arm*, not the attack rows, and has **no
disabling/guard-mutation direction** — C1's absorption matrix (fresh instances ×2 per
class + admit-stub mutation) measures something no r61 receipt measures for any class,
including E2b/E2c. The plan's honest delta is "0 of 5 attack-class measurements with
both directions," not "0 of 5."

## Findings

- **M — before-state overstated as recorded** (`controls/absorption-before.txt` lines
  15–25, 33; `plans/round-62.md` line 90 "grep … prints 0 of 5"; erratum-E1 item 4 "0 of 5
  committed erratum-level measurements"). Stated criterion counts `C1-worlds.txt` for E2b
  (W2, `arm=A3`, A3(b) reject) and E2c (W1, `arm=A4`, A4(iv) reject): 2 of 5, not 0 of 5.
  Impact: bounded — does not touch the matrix result, the successor, or any receipt; the
  defensible claim is the narrower one above. Severity M (a committed control asserts a
  criterion its own evidence contradicts; wave-2's job is exactly this).
- **L — seat-level greps, report, pin, absence checks: all reproduce** (0/0/0/0/0; sha
  prefix census whole-tree clean; no drift a745411→e6da78b; instrument absent at r61 tip;
  counter sha and `--self-test` line byte-identical).
- **L — no false-hit risk found:** every sha-naming file's exclusion reason verified
  against its body.

Residual: if the L1 adopts the class-faithful reading (instance = member of the erratum's
attack class, rejected by the amendment itself), the honest before-state is "2 of 5 classes
have one committed synthetic arm-level reject (E2b W2, E2c W1); 0 of 5 have the seat
attack tables re-scored or the disabling direction run."
