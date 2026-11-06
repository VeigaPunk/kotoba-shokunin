# Round 94 — addendum 1 (KotobaR94, L1; after the wave, before the record commit)

No frozen predicate, counter, kill rule or target changes here. C1 and C2 were scored at the landing
commit `f65347a664a9286fecfc41c9e429609bc5b2b284` with the counter frozen at
`edc731a91a956f6df20c27a74fb981b286f6ba58`; this addendum records an integration repair to the
mined-mistake fix (not a claim) and the bounds the attack seats measured.

## A1 — receipt check: two more fail-open shapes closed (not a claim)

CriticClaimsR94 D1 and D2, MutTesterTip94 r1: the round-94 fix to
`verifiers/fixtures/round-93/check-receipt-revs.sh` still dropped (D1) a header-shaped line with a bad
hex run when the line also carried a scratch tag (`REV=<41 hex> forgery` → rc 0), and (D2) a second,
malformed declaration on a well-formed header line (`REV=<40> REV=<41>` → rc 0); and no committed fixture
held a 39-hex header (r1). Repair: a scratch tag exempts a line from resolution, not from the header
shape rule; every declaration on a header line is shape-checked (`(?<![A-Za-z])` keeps `prev …` out).
New committed fixtures `verifiers/fixtures/round-94/receipt-headers/{hex39,scratch-hex41,double-decl}/`,
each rc 1 naming `MALFORMED`; `good/` rc 0; round-93 receipts `9 resolved, 0 unresolved over 19 files`;
round-92 landing receipts still `1 resolved, 5 unresolved` (rc 1). Receipts:
`.ufo/waves/round-94/receipts/landing/receipt-hdr-*-a1.txt`.
Not closed (CriticClaimsR94 D3, stated bound): declarations that do not start the line
(`receipt: REV=…`, `REV: …`, `rev<TAB>…`) are outside the check's line-anchored definition.

## A2 — the counter's anti-sniffing guard is narrower than the plan's wording (disclosure)

MutTesterBattery94 (tokenize-based) and CriticClaimsR94 D4 (line filter that drops `#` lines) each built
a source-sniffing self-test that reads `C1-PREDICATE-MET` under the frozen counter: the decoy guard only
catches sniffers that read comment lines. The counter header states the bound as "a sniffer that skips
comments (e.g. AST-based) is not caught"; the plan's § Disclosed bounds said only "AST-aware" and
understated it. Consequence for the claims: a `MET` reading from the counter alone does not prove
behavioural arms. For the landed C1 and C2 arms that proof is the non-counter reading by three seats
(ReviewerBatterySelfTest, ReviewerTipSelfTest, CriticClaimsR94), each of which applied the mutants by
hand and named the behavioural assertion that fails. Routed to round 95: a decoy that is code, not a
comment (a dead branch carrying the replacement), so comment-skipping sniffers trip it too.

## A3 — S269 duplicates the URL of S262 (disclosure)

ScribeCorpusR94 and ScoutMutSources found that S262 already holds the PIT "Basic concepts" page (URL
without the trailing slash). The plan names S269, so S269 was appended as declared; its `teaches` cell is
scoped to what each outcome class means for a kill rule, and the census reads one more `W04`
(cross-scope duplicate URL), no `E`-code. CriticClaimsR94 D7: the page does not say a timed-out mutant is
not a kill; the counter's timeout rule is the lane's choice, and the lesson records that S269 grounds the
Killed definition and the separate non-viable class only.

## A4 — label of C2 (disclosure)

CriticClaimsR94 D6: C2 adds self-test arms that keep `BATTERY` and `INSTRUMENT_PINS` in parity —
consistency; the calibration sub-axis is this lane's container for consistency (SCORECARD § axes) and no
separate calibration measurement is claimed.
