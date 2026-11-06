# Round 96 — addendum 1 (integration disclosures; L1 KotobaR96)

Written after wave `r96-w1` returned and before the landing reading. It changes no predicate, target,
counter, kill rule or control: every item below is a disclosure or a routed defect. The frozen C1 claim
is judged on `plans/round-96.md` as frozen at `679775abb9277a7b8d17f060b0f5b4ced2b127b6`.

## A1 — sweep count corrected (CriticClaimR96 D1, ReviewerCounterV4 F2)

`plans/round-96.md` § C1 says "22 hand mutants, 17 survive". The receipt
`.ufo/waves/round-96/receipts/recon-sweep.txt` reads 22 mutants: **18 rc 0 (survivors)**, 3 reported
failures (`m-legacy-as-baseline`, `m-md-strip`, `m-file-na-over-fail`) and 1 crash (`m-l1-in-08`,
`TypeError`; a RUN-ERROR under the v4 classes, not a kill). The plan's figure 17 is wrong; the
receipt's 18 is the count. The seven non-target survivors are `m-rstrip-dot`,
`m-fleetroot-no-baseline`, `m-fleetroot-stem-pass`, `m-empty-baseline-pass`, `m-noreport-08-pass`,
`m-placeholder-re-angle` (near-equivalent: differs only on an empty `<>`) and `m-stem-sibling-pass`;
the plan's disclosed bound named three of them as examples. MutTesterDispatchR96 adds 19 new mutants
(15 survive at base and at the candidate, 3 named equivalent) — routed to round 97.

## A2 — word count in the frozen sources receipt (CriticClaimR96 D2)

`receipts/sources-opened.txt` gives the POSIX quote as 19 words; it is **22** words (the quote is
unchanged and within the 25-word bound). The receipt stays frozen; the lesson Gate records 22.

## A3 — v4 counter forgery findings (ExecCounterForgeryR96; routed defect 4 of round 95)

Eight new forgery worlds were built against the frozen v4 counter at the freeze commit
(`.ufo/waves/round-96/w1/ExecCounterForgeryR96.md`). Five read UNMET (g1, g2 naive code-object
sniffers — code decoy; g4 inspect/linecache — source-blind rule; g5 harness sniffer — honest
conjunct; g6 fake failure line without a summary — rule 1). Three classes read **MET with no
behavioural arm**:

- **g7/g8 stateful fake (new, high).** The self-test writes a marker on its first run (the counter
  runs the honest self-test first, with one shared `TMPDIR` and one shared clone) and prints a fake
  reported failure on every later non-decoy run, reading the on-disk decoy text to hold the decoys.
  The v4 counter cannot tell a run's order from its behaviour.
- **g3 recompile-compare.** Recompiles the on-disk source and compares code objects with the running
  functions: the source-blind run is detectable.
- **g2b guard-aware code-object sniffer** — the v3 disclosed bound, unchanged in v4.

These are counter bounds, not C1 failures: the C1 kills are shown behaviourally by two independent
seats that applied each mutant by hand and named the failing `self-test FAIL:` assertion
(`w1/ReviewerArmsR96.md` § 2, `w1/CriticClaimR96.md` `armmap.txt`, failure counts
2,1,1,2,3,2,1,1,1,3,5 identical to the counter's). Routed to round 97: a v5 counter with a fresh
`TMPDIR` and clone per run, an honest run after the mutant runs ("honest-final"), and a mirror run
(the mutant's text executed with the mutant bytes on disk), as simulated by the seat (g3, g7, g8 →
UNMET; g2b remains MET).

## A4 — counter exit ladder (CriticClaimR96 D4; ReviewerCounterV3 F1/F3 of round 95)

Carried, not fixed: an instrument that is not valid UTF-8 makes the v4 counter exit 1 with a
traceback instead of 2 could-not-evaluate (probe `w1/CriticClaimR96/f1-exit-ladder.txt`); F3 is
unreachable for the frozen tables (the mutant compile guard raises first). Round 97 candidate.

## A5 — v4 drops the v3 `r94c1` table (ReviewerCounterV4 F1)

The plan says v4's changes are "exactly" three; v4 also removes the v3 `r94c1` table (the no-harm
battery runs `r94c1` on the round-95 counter, which is unchanged). No reading depends on it; a v4
`r94c1` call is a usage error (exit 2).

## A6 — label correction at integration (CriticClaimR96 D3, ReviewerArmsR96 M1/M2)

Three assertion labels in the landed arms were corrected before the landing commit, behaviour
unchanged: the parameter-expansion arms are labelled `t01/t03 brace form` (`${LANE}`; kills t01 and
t03) and `t01/t02 bare form` (`$LANE`; kills t01 and t02) — the builder had the t02/t03 suffixes
swapped — and the no-report-path `evaluated` assertion is labelled `t11-noreport-04-pass` (it guards
the t11 fixture). The counter does not read labels; the landing reading is taken on the corrected
bytes at the landing commit.
