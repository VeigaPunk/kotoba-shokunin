# ScribeLesson
role: UFO-FSD scribe — calibration
item: Draft the full frontmatter-free `corpus/lessons/round-63.md` body; report only.

## Findings

1. **Axes and scope.** The plan names depth plus consistency/calibration and assigns C1 to depth and C2 to calibration (`plans/round-63.md:5-10`). I drafted only the lesson body below; I did not write `corpus/lessons/round-63.md` or any other product path.

2. **C1 result and receipt limit.** The scratch run in `RevClaimC1.md:12-20` reports `worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`, `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, exit 0. The lane receipt `C1-g9-measure.txt:1-14` records the v32 digest, all six survivor verdicts, the G9-disabled arm and exit 0, but omits the required worlds/eligible aggregate line. I preserve that distinction in the draft rather than saying the receipt contains all three frozen lines.

3. **C2 before-state and declared correction.** `.ufo/waves/round-63/controls/C2-before-r62tip.txt:1-7` records the amended base control as 0 of 5, exit 1. The plan's appended Erratum E1 says check 4 now requires both prefix preservation and at least one appended line (`plans/round-63.md:150-159`). Before that amendment, `ExecCalibBefore.md:28-36` records the five-check vector as FAIL/FAIL/FAIL/PASS/FAIL and `1 of 5`; the four content checks are 0 of 4. At my last read, the receipts directory contained only `C1-g9-measure.txt`; no C2 after-measurement receipt was available, so the draft does not claim the 5-of-5 target.

4. **Frozen-plan conflict, verbatim for the canonical judge.** `plans/round-63.md:111-117` originally says:

   > At the r62 tip `35d44b4b` (before this round's corrections) the counter prints `r62 routed defects closed 0 of 5`, exit 1: check 1 fails (the file is untracked), 2–3 fail (no correction line names the receipt revision or the sizes), 4 passes (an empty delta is a prefix — recorded honestly as a check that only bites when text is rewritten), 5 fails. At the measured r63 tip it prints `5 of 5`, exit 0.
   > The target is 5 of 5; the do-nothing control (the r62 tip) scores 0 of 5 on the four content checks, so it cannot meet the target.

   The first paragraph's five-check total conflicts with its explicit check-4 PASS; the later four-content-check subtotal is 0 of 4. E1 is a subsequent, explicit refinement, not evidence that the original wording was internally consistent.

5. **Calibration-axis mapping conflict.** The plan says “Lowest owned axis: calibration/consistency (8.5) below depth (9)” (`plans/round-63.md:5-10`), while `SCORECARD.md:29` gives “consistency (calibration sub-axis)” a score of 10; `SCORECARD.md:365` separately gives advisory calibration 8.5. The draft claims no numeric score delta and does not silently choose between these labels.

6. **S119 opened and quote located.** My command `date -u +%Y-%m-%dT%H:%M:%SZ && curl -sSL --max-time 30 -D /tmp/kotoba-r63-s119-acta-scribe.headers -o /tmp/kotoba-r63-s119-acta-scribe.body -w 'http=%{http_code}\nfinal=%{url_effective}\ncontent_type=%{content_type}\nbytes=%{size_download}\n' 'https://actaorthop.org/actao/correctionsandappeals' && wc -c /tmp/kotoba-r63-s119-acta-scribe.body && sha256sum /tmp/kotoba-r63-s119-acta-scribe.body` returned `2026-10-23T23:05:26Z`, HTTP 200, 21,024 bytes, SHA-256 `39e51269ad0eef9888e011a7bc5e9cd253dbbfb1cd1e3edcf5b76761ad1b9494`. The selected row in `corpus/SOURCES.md:131` is ICMJE, not Acta; my separate ICMJE re-open returned HTTP 200, 22,722 bytes, SHA-256 `b7e674fbda666dc6c4f3f8eb0db31cc7530afb6a50dee262a0a61234a57795d0` at 23:05:00Z. Its located quote is in `.ufo/waves/round-63/snapshots/S119.page:171`; `RevSourceQuote.md:17-22` reports a per-request Cloudflare script tail and confirms the quote region is stable. The Gate therefore uses the selected ICMJE row and does not claim cross-fetch byte identity.

7. **S049 negotiation correction.** At 23:03:27Z, `curl -sSL --max-time 30 -H 'Accept: */*' ... 'https://cursor.com/docs/rules.md'` returned HTTP 200, `text/markdown`, 17,252 bytes, SHA-256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0`; with `Accept: text/markdown`, the same URL returned HTTP 404, 389 bytes, SHA-256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1`. The response body quotes are at `/tmp/kotoba-r63-s049-any.body:32` and `/tmp/kotoba-r63-s049-md.body:1`. `ExecSourceProbe.md:8-10` independently reports both Cursor `.md` routes have this Accept-dependent behavior. This changes the rejection reason, not the decision to avoid a duplicate source row.

8. **M94 evidence.** `ExecLessonMistake.md:12-35,48` records the read-only commands and outputs: the late write has no r62-tip tree row; the C2 receipt names `3f911504…` rather than the report's `e6da78bb…`; `wc -lw` is `64 1044`, not `50 723`; and the no-harm receipt records both interim reds. The report also notes the r63 instrument does not explicitly check the false post-report child-commit assertion.

9. **Verification and touched surfaces.** I opened the listed URLs and read lane evidence; I did not run a gate, build, test, linter or formatter, install/update a tool, or mutate Git/JJ. My only intended lane write is this report file. The complete lesson below is a draft for L1 integration, not a product-file change.

## Artifacts

Draft body for `corpus/lessons/round-63.md` (verbatim text produced by this seat; not written to the product path):

````markdown
source: S119
source: S049

## What changed

C1 adds the v32 G9 clause-support guard for the frozen `e2f-compound-purpose-outside-citation` survivor. The scratch run in `.ufo/waves/round-63/w1/RevClaimC1.md:12-20` prints `worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`, and `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, exit 0. The dedicated `.ufo/waves/round-63/receipts/C1-g9-measure.txt:1-14` records the G9 closure and disabled-guard arm, but not the worlds/eligible aggregate line; keep the receipt limitation visible until the complete frozen transcript is recorded. This is lexical clause-local support, not general semantic entailment: the guard splits at `;` and standalone `and` outside backticks, skips clauses below three content words, and only rejects clauses also present on the page (`plans/round-63.md:51-68`; `CriticC1Bound.md:10-14`).

C2 introduces the revision-bound `verifiers/check_r63_routed_repairs.py` instrument for the r62 spot-check. The r62-tip control after plan Erratum E1 prints `r62 routed defects closed 0 of 5`, exit 1 (`.ufo/waves/round-63/controls/C2-before-r62tip.txt:1-7`). No after-measurement receipt was available for this draft, so `5 of 5` remains a target, not a reported result. Its five checks are a bounded reconciliation, not independent evidence of general calibration; the named checks do not by themselves close every obligation in spot-check §6 (`CriticCalib.md:16-37`). No numeric calibration score change is claimed.

S119 is the new correction-practice source. It supports dated new versions, linked correction notices and preserved prior versions; it does not prescribe literal append-only log edits (`corpus/SOURCES.md:131`). S049's Cursor `.md` rejection reason is corrected below: the live route is Accept-dependent, not universally dead. The distinct-source rejection remains; S049's old row is not rewritten and the SOURCES note is appended (`corpus/SOURCES.md:221-235`).

## Gate

| Row / change | URL and access | Located quote (≤25 words) |
|---|---|---|
| **S119 — new row** | https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html — opened 2026-10-23T23:04:00Z (HTTP 200, 22,722 B; snapshot `.ufo/waves/round-63/snapshots/S119.page`); this seat re-opened it at 23:05:00Z with the same size. The source row records the fetched digest and explains that its Cloudflare tail varies by request (`corpus/SOURCES.md:131`). | “post a new article version with details of the changes from the original version and the date(s) on which the changes were made” (23 words; § Corrections, `S119.page:171`). |
| **S049 correction — rejection reason only; not a new row** | https://cursor.com/docs/rules.md — opened 2026-10-23T23:03:27Z with `Accept: */*` (HTTP 200, `text/markdown`, 17,252 B, SHA-256 `dae9d3ec…`); the same URL with `Accept: text/markdown` returned HTTP 404 (389 B, body SHA-256 `4f98eb06…`). | “Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled.” (11 words; accepted body `rules.md:32`); “# Page not found” (3 words; 404 body line 1). |

S119's source supports transparent versioning and preserved history, not literal append-only files. The S049 probe corrects the reason for the old 404: under the seat's `Accept: text/markdown` request the `.md` route returns 404, while `Accept: */*` returns the rules body. It is not a dead URL. S049 remains rejected as a distinct source because the extensionless Cursor rule page is already represented in the existing registry; the S049 row itself is unchanged (`corpus/SOURCES.md:120,127`).

## Mistakes

- **M94 — class: close self-assessment not reconciled against the final committed tree** · Evidence: the r62 non-author spot-check routes the missing late write, three stale report citations (receipt revision, entry size, and a claimed post-report child commit), and omitted interim no-harm reds (`corpus/lessons/round-62-verifier-spotcheck.md:45-58,159-175`). At the r62 close tip, `git ls-tree -r e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02 -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md` printed no rows; the committed C2 receipt says `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`, while the report named `e6da78bb…`; `git show e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02:corpus/knowledge/erratum-absorption-round62.md | wc -lw` printed `64 1044`, not `50 723`; and the committed no-harm receipt records `reg_gate` 36 of 38 plus `corpus-idx` (`ExecLessonMistake.md:12-35`). · captured-by: `plans/round-62.md:193-197` required a wave-2 check of report claims and the lesson/no-harm/census, but that check did not catch these mismatches. · fix: the r63 `--rev` counter checks the late-file tree entry, receipt revision, entry size, append-only growth and no-harm tokens (`plans/round-63.md:91-109,150-159`). These checks are specified and a base control is recorded, but no after receipt is present in this draft; moreover, the frozen checks do not validate the false post-report child-commit assertion. Do not claim all §6 defects closed from the counter headline alone.

## Routed

1. **Late write / H1 bound.** The r62 late report must be tracked; `late-write-tracked` only establishes the tree entry. The H1 report says its honest variants are rejected by the narrow R-c/ancestry checks, so the entry/Q57 must carry that fixture-level bound before claiming broader honest-repair acceptance (`ExecLateWriteFold.md:7-12,24-32`).
2. **Report citations.** C2 checks the receipt revision and entry size and now requires an appended LOG line while preserving the base prefix (`plans/round-63.md:97-109,150-159`). The false post-report child-commit claim is outside those five checks and needs its own correction. A 5-of-5 check score is not a five-defect closure count.
3. **Cursor source.** The S049 correction is a source-freshness repair outside the C2 counter. Keep the `Accept` condition and the still-valid distinct-source decision; append the correction instead of rewriting the old Gate text or S049 row (`corpus/lessons/round-62-verifier-spotcheck.md:170-172`; `corpus/SOURCES.md:221-235`).
4. **No-harm summary.** The r62 receipt's interim `reg_gate` failure (36 of 38) and `corpus-idx` failure are real historical results; later r62 evidence records both fixed at 39 of 39 and zero unindexed files (`ScoutR62Defects.md:53-71`). The r63 check's token-presence condition is not, by itself, proof that both were fixed at the measured tip.
5. **SHONEN.** Operator-owned; four `[~]` boxes remain unchanged and no promotion is claimed (`plans/round-63.md:79-86`; `corpus/lessons/round-62-verifier-spotcheck.md:176-177`).
6. **C2 baseline arithmetic.** Erratum E1 amends check 4 to require both prefix preservation and at least one appended line; the unchanged r62 tip then fails that check as well, yielding the recorded 0 of 5. This differs from the original prefix-only wording, whose explicit PASS would make the five-check total 1 of 5; the four content checks alone are 0 of 4 (`plans/round-63.md:111-117,150-159`; `.ufo/waves/round-63/controls/C2-before-r62tip.txt:1-7`).

## Round shape

The dispatch is wave 1 build with 32 spawned seats and no resumes (`.ufo/waves/round-63/w1-dispatch.json:16-20`). The plan permits wave 2 falsification with 32–64 seats only if wave 1 yields at least 32 distinct attack items, plus a residual review of at most 8 if needed; total round size is at most 128 (`plans/round-63.md:12-15,140-148`). Axes are depth and consistency/calibration; no numeric score movement is asserted here while the ownership mapping above remains unresolved.
````

## Verdict

**PROPOSES** — the draft reports observed source opens and bounded evidence without claiming an unobserved C2 after-result, a complete C1 receipt, or a numeric calibration increase. I would change the lesson only when the measured C2 after receipt and complete C1 receipt are available, the correction destinations are committed, and the calibration ownership mapping is resolved. This seat installed no tools.