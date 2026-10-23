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
  - `:170` — “publish a correction notice  as soon as possible detailing changes from and citing the original publication” — 16 words (`wc -w` on the extracted line prints 16).
  - `:172` — “archive all prior versions of the article” — 7 words.
- Round-start census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` — exit 0, 16 `W04` (`.ufo/waves/round-63/census-before.txt:2-20`). Round-end census: see the report's Sources & frontier section; the interim census at the moment the row landed printed `E05` (kind `guidance`) and two `E11` (the `used-by` targets this lesson and the entry did not exist yet), the first fixed immediately and the second by this commit landing both files.

### S049 errata (appended; the row and its receipt are preserved)

The round-62 spot-check's Cursor `.md` rejection is request-profile-dependent, and the held
receipt no longer reproduces:

- `curl -sS -L -H 'Accept: text/markdown' https://cursor.com/docs/rules.md` → HTTP 404, 389 B body.
- `curl -sS -L https://cursor.com/docs/rules.md` (default `Accept`) → HTTP 200, `text/markdown; charset=utf-8`, 17,252 B, sha256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0` (2026-10-23T23:03:45Z, seat `ExecSensorS049`; re-run by the L1 at 23:04Z with the same digest).
- S049's recorded receipt is 17,403 B, sha256 `884c67ca…`, fetched 2026-10-22T20:09:33Z (`corpus/SOURCES.md:62`). It is retained as the dated original; the errata is in `corpus/SOURCES.md`'s round-63 search-log note.
- The `.md` form remains a reject for minting a *new row* because S108 already re-opens S049 at the same URL — the rejection reason, not the decision, changes.

Rejected (with reason):

- `https://publicationethics.org/guidance/correction` — HTTP 403; no body to quote (`ExecSourceS119.md` § Findings 1).
- `https://publicationethics.org/retraction-guidelines` — HTTP 403; no body.
- `https://www.niso.org/publications/rp-8-2008-jav` — HTTP 404; no body.
- Acta Orthopaedica's correction policy — byte-verified and stable (`39e51269…`) but its text reads “Necessary corrections will be made to published articles however as authorized by the Editor”, which authorizes in-place correction; it is counter-evidence for this round's practice and was not admitted (`RevSourceQuote`, round 63).

## Mistakes

- **M94 — class: the frozen plan's expected headline contradicted the check it described.** Evidence: `plans/round-63.md` § C2 as frozen said the do-nothing tip prints `0 of 5` while its own check 4 (“the r62-tip LOG is a byte-prefix of the LOG at `<rev>`”) is necessarily true at the tip, so the honest total was `1 of 5`. Two independent seats found it before any data (`ExecCalibInstrument` IRC, `ExecCalibBefore.md`, `ScribeReportSkeleton.md` § Verdict). Captured-by: none existed — no rule required the plan to score its own before-state with the checks as written; the nearest is Q48's printed-vs-computed class, which names headlines, not plans. Fix: erratum E1 (pre-data) splits check 4 into prefix **and growth**, and the round records both readings: the pristine formulation scores `1 of 5` and E1's scores `0 of 5`; the report carries both. The fix is able to fail: the instrument's `--self-test` contains the rewritten-LOG arm (prefix false → check 4 FAIL) and the base arm (growth zero → FAIL), measured `0 failure(s) over 10 assertions`.

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

Filled after wave 2; every correction lands before the report.
