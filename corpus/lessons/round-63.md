---
author: kotoba L1 round 63
date: 2026-10-23
round: 63
lane: kotoba
---

# Round 63 — lesson (kotoba, hyaku run 5, attempt 3)

## Gate

S119 was opened on 2026-10-23 by the L1 and re-fetched by a seat (`ExecSourceS119`);
the fetch command and its full output are in `.ufo/waves/round-63/w1/ExecSourceS119.md`
§ Findings 2, and the committed snapshot is `.ufo/waves/round-63/snapshots/S119.page`
(sha256 of the committed bytes `d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2`).
The ICMJE page carries a dynamic injected element: a seat's fetch of the same URL the
same day returned the same byte count (22,722) with a different digest
(`e2c3db05…`), so the row pins the located quotes and the access date, **not**
byte-identity across fetches (Q56: this is not `byte-exact`).

- **S119 ICMJE — Corrections and Version Control** — https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html — accessed 2026-10-23T23:04Z (HTTP 200, 22,722 B, `text/html`) — quotes, each a literal substring of the committed snapshot:
  - `:170` — “publish a correction notice  as soon as possible detailing changes from and citing the original publication” — the quoted span is 16 words; line 170 of the snapshot carries 49 words (`sed -n '170p' .ufo/waves/round-63/snapshots/S119.page | wc -w` prints 49), so the count below names the span, not the line.
  - `:172` — “archive all prior versions of the article” — the quoted span is 7 words; line 172 carries 31.
- Round-start census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` — exit 0, 16 `W04` (`.ufo/waves/round-63/census-before.txt`: the 16 `W04` lines, file lines 2–17 of 18). Round-end census: exit 0, 16 `W04` (`.ufo/waves/round-63/census-after.txt`, same command; the plan's 17-`W04` prediction is corrected by plan erratum E4 — S119's URL is new to the registry, so no 17th duplicate-scope warning arises). The interim census at the moment the row landed printed `E05` (kind `guidance`) and two `E11` (the `used-by` targets this lesson and the entry did not exist yet), the first fixed immediately and the second by the wave-1 build commit (`cbbee56e`) landing both files. Non-author re-open: `ScoutW2S119Reopen` re-fetched the page (HTTP 200, 22,722 B, new digest), confirmed both quotes still literal at the committed snapshot, and changed nothing.

### S049 errata (appended; the row and its receipt are preserved)

The round-62 spot-check's Cursor `.md` rejection is request-profile-dependent, and the held
receipt no longer reproduces:

- `curl -sS -L -H 'Accept: text/markdown' https://cursor.com/docs/rules.md` → HTTP 404, 389 B body.
- `curl -sS -L https://cursor.com/docs/rules.md` (default `Accept`) → HTTP 200, `text/markdown; charset=utf-8`, 17,252 B, sha256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0` (2026-10-23T23:03:45Z, seat `ExecSensorS049`; re-run by the L1 at 23:04Z with the same digest).
- S049's recorded receipt is 17,403 B, sha256 `884c67ca…`, fetched 2026-10-22T20:09:33Z (`corpus/SOURCES.md:62`). It is retained as the dated original; the errata is in `corpus/SOURCES.md`'s round-63 search-log note.
- The `.md` form remains a reject for minting a *new row*; the reason is corrected
  (the committed sentence "S108 already re-opens S049 at the same URL" is false — S049
  holds `https://cursor.com/docs/rules.md`, S108/S115 hold `https://cursor.com/docs/rules`,
  and S088 already holds the non-`.md` URL): the standing reason is that the `.md` spelling
  serves the same content modulo the request profile, so a second row would duplicate the
  scope S088/S115 already govern. The decision, not the justification, is unchanged.

Rejected (with reason):

- `https://publicationethics.org/guidance/correction` — HTTP 403; no body to quote (`ExecSourceS119.md` § Findings 1).
- `https://publicationethics.org/retraction-guidelines` — HTTP 403; no body.
- `https://www.niso.org/publications/rp-8-2008-jav` — HTTP 404; no body.
- Acta Orthopaedica's correction policy — byte-verified and stable (`39e51269…`) but its text reads “Necessary corrections will be made to published articles however as authorized by the Editor”, which authorizes in-place correction; it is counter-evidence for this round's practice and was not admitted (`RevSourceQuote`, round 63).

## Mistakes

- **M94 — class: the frozen plan's expected headline contradicted the check it described.** Evidence: `plans/round-63.md` § C2 as frozen said the do-nothing tip prints `0 of 5` while its own check 4 (“the r62-tip LOG is a byte-prefix of the LOG at `<rev>`”) is necessarily true at the tip, so the honest total was `1 of 5`. Two independent seats found it before any data (`ExecCalibInstrument` IRC, `ExecCalibBefore.md`, `ScribeReportSkeleton.md` § Verdict). Captured-by: none existed — no rule required the plan to score its own before-state with the checks as written; the nearest is Q48's printed-vs-computed class, which names headlines, not plans. Fix: erratum E1 (pre-data) splits check 4 into prefix **and growth**, and the round records both readings: the prefix invariant is true at the tip (a no-harm guard, per `RevW2Check4`), and the honest before total under E1's growth conjunct is `0 of 5`. Shown able to fail: `python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05` at the wave-1 build prints `FAIL append-only prefix=True grew_by=0 line(s)` and `r62 routed defects closed 0 of 5`, exit 1 (`.ufo/waves/round-63/controls/C2-before-r62tip.txt`; re-run under the E2-hardened counter in `receipts/C2-before-rerun.txt`). The M94 line as first committed cited `0 failure(s) over 10 assertions`; the committed self-test prints 15 at the build tip and 23 after erratum E2 — assertion counts are measured at the revision named, never carried.

- **M95 — class: reference-drift / number-drift (committed paperwork falsified by committed bytes).** Evidence: three round-63 artifacts claimed what the bytes did not hold — (i) the wave-1 C1 receipt named v32 sha256 `552308806b…` over 205 assertions, a revision that exists in neither git nor the jj store (the committed counter is `42460691…` / 208, later `12d093a1…` / 219 after E3); (ii) the LOG corrections block's clause "nothing else descends from `e53b6e5c`" was false (`8c4cefa8` and `cbbee56e` descend from it; only `35d44b4b` did at report time); (iii) the block's, the lesson's and the SOURCES note's sentence "S108 already re-opens S049 at the same URL" was false (S049 is `…/rules.md`; S108/S115 are `…/rules`). Captured-by: none — no criterion required a receipt's named revision to exist as a blob, or a correction sentence to be re-derived against the graph it describes; the nearest is Q48 (printed-vs-computed). Fix (all appended, none rewriting): the receipt refresh at the measured tip (`receipts/C1-g9-measure.txt` supersedes the stale one), the corrections-to-the-corrections block in `LOG.md`, and the corrected S049 reason in this lesson and `corpus/SOURCES.md`. Found by `ScribeW2LOGEntry` (findings 1–2), `ScoutW2R62SpotcheckSweep` (items 2c, 3c) and `RevW2C1Predicate`.
## Status changes (contract rule 2, old → new)

- S119 — new row → `mined`; `used-by` names `corpus/knowledge/compound-clause-citation-round63.md` and this lesson.
- S049 — `mined` unchanged; `recheck 90d` not due (opened 2026-10-22); errata appended to the search log, no field rewritten.

## Method provenance

The G9 guard extends A2's own forward-support check and reuses its helpers unchanged; the
attack class and the survivor catalogue come from the round-62 erratum-absorption matrix and
its `CriticC1Hollow` finding; the guard-mutation direction follows Q57 (tameshi's guard-kill /
hollow method). The correction-practice half follows the r62 spot-check's preference for
appended LOG corrections, with S119 as the primary source opened this round; the counter
design (computed-from-`<rev>` checks, a do-nothing before receipt, label-only and
append-only negative arms) follows `check_routed_repairs_v2.py`'s round-62 hardening.

## Falsify corrections

Filled after wave 2; every correction lands before the report. Grouped and
deduplicated by `DistW2Findings` (23 wave-1/wave-2 attack instances → 14
distinct items); the landed dispositions below are the L1's, against the
hardened instruments.

| # | distinct attack | source seat(s) | disposition as landed |
|---|---|---|---|
| a | check-4 arithmetic (`0 of 5` vs the arm's literal `1 of 5` at the tip) | CriticCalib F1, MutCalibInstrument F1, RevCalibChecks F3 | **fixed** — erratum E1 (prefix + growth); re-run receipt `receipts/C2-before-rerun.txt` |
| b | five counted checks ≠ the spot-check's five routed obligations | CriticCalib F2, RevCalibChecks F6e | **fixed (wording + closures)** — headline now "repair checks" (`CriticW2Headline` wording); 1b closes as QUALITY Q59, 2c as the LOG corrections-to-corrections block, 3b/3c as the round-62-lesson errata |
| c | check 4 free on a no-op / endpoint-only; blind to mid-history and suffix rewrites | CriticCalib F5, RevCalibChecks F4, MutW2C2Counter | **bound-recorded** — frozen-prefix preservation guard (`RevW2Check4` synthetic-object demonstrations; SCORECARD row wording) |
| d | committed-byte agreement is not receipt authenticity (co-change) | CriticCalib F4, MutCalibInstrument F8 | **bound-recorded** — docstring Bounds; receipt-side substitution arms now kill the single-sided mutation (E2) |
| e | in-sample reconciliation ≠ new calibration capability; no numeric move | CriticCalib F3/F6 | **wording-only** — SCORECARD C2 row: bounded reconciliation, delta 0, axis mapping unambiguous |
| f | label-only counter satisfies the predicate letter | RevCalibChecks F1/F5, RevW2LabelOnly | **fixed** — E2 base arm + process arm; demonstrated red on the patched counter |
| g | fingerprint counter satisfies the predicate | RevCalibChecks F2, RevW2Fingerprint | **fixed** — E2 fingerprint process arm (mid-score + look-alike worlds) |
| h | M1 worktree-read mutant survives | MutCalibInstrument F3, MutW2C2Counter | **fixed** — worktree process arm; per-check logic verified to kill M1 by `MutW2C2Counter` |
| i | M2/M3/M4/M5 literal mutants | MutCalibInstrument F4–F7 | **fixed** — receipt-side substitution arms (E2) + existing arms; all nine mutants killed per `MutW2C2Counter` §5 |
| j | spec precision (token, boundaries, suffix scoping, `36 of 38` locus, `--rev` unbound) | RevCalibChecks F6a–f, RevW2SpecPrec | **fixed** — suffix-scoped boundary-tightened scans (E2); honest bytes stay 5 of 5; docstrings aligned |
| k | G9 short-clause/backtick escape lanes | RevG9Guard F1/F2/F4, MutG9Guard F5, MutW2V32, MutW2SplitClauses | **fixed + bounds** — E3 pairing fix + 8 split arms + 3 floor/page-gate assertions; one-word tail recorded as a structural bound; `-and-`/quote arms pinned as bounds; all nine splitter mutants killed (§7f–§7g) |
| l | G9 over-rejection lanes | RevG9Guard F5/F6/F7 | **bound-recorded** — visibility arms labelled bounds, not endorsements; entry § Limits |
| m | 4-char prefix collision; vocabulary-specialised stub | RevG9Guard F3, RevClaimC1, CriticW2C1Bounds | **bound-recorded** — inherited from A2's `supported()`; single-instance bound carried in entry and SCORECARD |
| n | must-fail arm not a guard-quality assertion; eligible-row arm blind to under-strict guards | MutG9Guard F3/F4, MutW2SplitClauses | **fixed** — E3 arm set makes each mutant observable; the one-discriminating-assertion gap is closed |
| o | `6 of 6` must name its denominator; r62 limits carried forward; depth stays 9 | CriticC1Bound, CriticW2SemanticClosure, RevW2ScorecardWording | **fixed** — SCORECARD/entry wording; S103 published-event limit carried |
| p | boundary witnesses must be published | CriticC1Bound F3, MutW2GuardEvasion | **fixed** — replay table in `MutW2GuardEvasion.md` §1; entry § Limits names each lane |
| q | S119 quote discipline (dead URLs, Acta counter-evidence, sha non-reproduction) | RevSourceQuote, ExecSourceS119 | **fixed** — Gate counts corrected (span vs line), Acta recorded as screened-and-excluded, byte-identity disclaimer |
| r | pin v32's sha into the receipt | RevClaimC1 | **fixed** — refreshed receipt names the landed sha at the measured rev |
| s | H1 narrowness bound belongs in QUALITY | RevClaimC1, ScoutW2R62SpotcheckSweep 1b | **fixed** — QUALITY Q59 (red-before/green-after shown) |
