# Round 95 — kotoba (Linux host, omp): lesson

Author: **ScribeCorpusR95** (scribe seat). This file is the round-95 **scaffold**: the Gate record,
the Mistakes row, the Status-changes record and the Considerthese entry below are written;
**the L1 completes the settlement** (the seat record, the claim verdicts, the wave disposition and
the final numbers).
Round: 95, plan `plans/round-95.md` (frozen at `673d1e2e6f850bb54dda9698cf825cf6788c7d0d`), base
`2d886a91e57efd3555ec9076a63209e2d8bfbb8d`.
Pre-data receipts (frozen with the plan, before any scored reading):
`.ufo/waves/round-95/receipts/redbefore-c1-base.txt` (`C1-PREDICATE-UNMET` at the base),
`poscontrol-r94c1-base.txt` (`R94C1-PREDICATE-MET` at the base), the six
`forgery-f1..f6-*.txt` control worlds (all `C1-PREDICATE-UNMET`) and `census-before.txt` (rc 0).

## Gate

Candidates considered, with the decision and the reason.

- **S270** — Python documentation, `unittest`
  (`https://docs.python.org/3/library/unittest.html`). **Admitted** as tier A, kind `docs`, status
  `mined`, opened 2026-11-05, recheck `90d`, used-by `corpus/lessons/round-95.md,plans/round-95.md`.
  - Access record (rule 1): access date 2026-11-05; HTTP 200; 336978 B; sha256
    `f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d`. The fetch was made
    independently by this seat (`curl -sS -L -o unittest.html -w '%{http_code} %{size_download}'`
    then `sha256sum unittest.html`) and by the scout
    (`.ufo/waves/round-95/w1/ScoutSourcesR95.md` §1a); both read the same byte count and the same
    digest, and the digest equals the one the plan records for S270 — three independent readings,
    one value.
  - Located quote (≤25 words): "Each tuple represents a test which raised an unexpected exception."
    — **10 words** (`printf '%s\n' "Each tuple represents a test which raised an unexpected
    exception." | wc -w` → 10), at **HTML lines 2413–2414** of the fetched bytes (the `errors`
    attribute body), quote-equal after joining the fold (line 2413 ends `…raised an`, line 2414
    begins `unexpected exception.</p>`) — no bytes dropped (Q42/Q56).
  - Its counterpart, on the neighbouring `failures` attribute body (HTML lines 2421–2422): "Each
    tuple represents a test where a failure was explicitly signalled using the assert* methods." —
    **15 words**, quote-equal after joining the fold after "failure" and taking the rendered link
    text of the `assert* methods` span. The two sentences together are the row's substance: an
    *error* is a test that raised an unexpected exception; a *failure* is a test where a failure
    was explicitly signalled. The counter's rule 1 reads exactly this pair — a reported failure
    (an explicit signal, with a `FAIL ` line and an `N failure(s)` summary) is a kill; an
    uncaught exception is a RUN-ERROR and never a kill.
  - The page's own pins: the `<title>` carries `Python 3.15.2 documentation` (HTML line 20) and the
    footer reads `Last updated on Nov 05, 2026 (22:32 UTC)` (HTML line 3179) — so the row's anchor
    is re-locatable, not a bare homepage (Q70).
  - **What this row adds** to the registry: nothing else holds this URL (scout §5 grep: no
    `docs.python.org/3/library/unittest` row; the existing `docs.python.org` rows are S007 json,
    S253 tempfile, S263/S265 subprocess, S266 exceptions). It is a **new document**, not a new
    fetch of a held URL — the pitfall the scout names as already held by the lane (S262/S269 on
    the PIT URL, S263/S265 on the subprocess URL).
- **S260 re-opened as corroboration — no new row.** The plan (§C1 "Sourced") re-opens the Stryker
  "Mutant states and metrics" page as corroboration for rule 1. Re-opened 2026-11-05: HTTP 200;
  27068 B; sha256 `8641c38959222238f34aba0e20d3c51919cf183bf19a53f436257614cab656da` — byte-identical
  to the record the plan carries and to the scout's independent fetch (scout §1b: MATCH). The
  located quote, at **HTML line 24**: "The running of the tests resulted in an error (rather than
  a failed test)." — **14 words** — which is the same split S270 grounds, stated tool-side: an
  error is not a failed test. The `Killed` sentence at HTML line 12 ("When at least one test
  failed while this mutant was active, the mutant is killed." — 15 words) still sits where S260's
  row says it does, so S260's anchor holds against the current bytes (scout §1b cross-check).
  **Why no new row:** the registry already holds this URL at **S260** (`corpus/SOURCES.md` line
  201), so a second row would be the same-URL duplicate the round-94 closure called out as
  **defect 1** — "a frozen plan naming a row must not force an admit the scout argued against —
  record the rule in `QUALITY.md` if kept". The plan itself says "no new row on its URL"; the
  re-open is corroboration for the *kill rule*, and its used-by cell is left alone (append-only;
  see § Status changes). **Flip condition:** a fetch whose "Runtime error" or "Killed" wording
  changes re-opens S260's anchor (recheck `90d`).
- **Rejected candidate — the Apache Ant `junit` task manual**
  (`https://ant.apache.org/manual/Tasks/junit.html`), screened by the scout (§4) and re-verified
  by this seat. Access 2026-11-05; HTTP 200; 33365 B; sha256
  `3f1ee369f541938791d02b8a09506e48ef33472bccb6c237c4280730c7bcc4a1` (byte-identical to the
  scout's copy). **Reason (observed fact, Q62):** the page does not define error-vs-failure at
  all — `grep -ic 'unexpected exception'` over the fetched bytes prints **0** — and its only
  statement on the subject **conflates** the two: at HTML line 104 (14 words) "Stop the build
  process if a test fails (errors are considered failures as well)." Admitting it would teach the
  gate that an error *is* a failure, the opposite of the distinction rule 1 rests on.
  **Flip condition:** the Ant manual (or its JUnit-XML successor page) again defines `<error>` as
  an unexpected exception against `<failure>` as an assertion failure — then it becomes
  admissible, scoped to Ant's own reporting.
  Two further scout candidates (**pytest's exit codes**,
  `https://docs.pytest.org/en/stable/reference/exit-codes.html`, HTTP 200, 25787 B, sha256
  `a403306a1d763fc8123749544905dd64e8e0cfa5ed46a416679001c3142e3977`; and the **TAP 13
  specification**, `https://testanything.org/tap-specification.html`, HTTP 200, 22741 B, sha256
  `d4d82502f11cae2bad4960586cb2a7bbead03bd55eabe1d85c76c86266d9b09a`) are **not written this
  round**: this seat's ownership is the single row **S270**, and the plan's Sourced section names
  only S270 and S260. The pytest page is process-level only — it does not define the within-run
  error-vs-failure split that grounds rule 1 — and the TAP page is protocol-side, neither
  contradicting nor extending S270/S260. Both are left for a later round (the scout proposes them
  as the next unused ids). The scout's first guess at the pytest URL
  (`…/explanation/exit-codes.html`) answers **404** (2531 B error body) and was replaced by the
  real path found from the reference toctree; the mutmut README URL
  (`raw.githubusercontent.com/boxed/mutmut/main/README.md`) answers **404** (14 B).

**Census before → after.** Rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → **195** before this round (receipt
`.ufo/waves/round-95/receipts/census-before.txt`, rc 0 with the 34 pre-existing `W04`
duplicate-URL warnings) and **196** after — the one row appended above (S270), no row dropped, no
row rewritten. Validation: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
--file "$D/corpus/SOURCES.md"` → exit **0**, the same **34** `W04` warnings as before (no new one:
S270's URL is new to the registry) and no `E`-code (receipt
`.ufo/waves/round-95/w1/ScribeCorpusR95/census-after.txt`). The new row is an ordinary append, not
a correction, so no row's `teaches` cell opens `supersedes S0NN — `.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `run-error-scored-as-kill`: a kill counter that reads only the self-test's exit code scores a **run error** — the instrument itself crashing with an uncaught exception — as a kill, because a crash also exits non-zero; the counter then reports a mutant as killed when nothing was ever reported | `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-94/w1/CriticClaimsR94.md` defect **D8** ("KILLED is `rc != 0`, so a run error scores as a kill"; probe `375b0d67` read `C1-PREDICATE-MET`, rc 0, on a counter that raises `RuntimeError` instead of returning 1) | `none` | **rule 1** of `verifiers/fixtures/round-95/selftest-kills.py`: a run is classified from its output, not from its exit code alone — REPORTED-FAILURE = exit 1 **and** the summary `<N> failure(s) over <M> assertions` with N ≥ 1 **and** at least one `FAIL ` line; CLEAN = exit 0 with N = 0; anything else (a traceback, a crash exit, a missing summary) is RUN-ERROR, and a mutant is KILLED iff its run is REPORTED-FAILURE. The rule is grounded by S270 (`TestResult.errors` = a test that raised an unexpected exception; `TestResult.failures` = a test where a failure was explicitly signalled) and corroborated by the re-opened S260 ("The running of the tests resulted in an error (rather than a failed test)"). **Shown able to fail** by `.ufo/waves/round-95/receipts/forgery-f6-crash-report.txt`: the f6 control world drives the N11 behaviour and signals it by an uncaught `RuntimeError`; the receipt reads `mutant n11-accept-plus-two rc 1 RUN-ERROR (not a kill): RuntimeError: r95 forgery f6: two added kill rows accepted` and `C1 targets killed 0 of 3 (run errors 1); … C1-PREDICATE-UNMET`, rc **1** — where the round-94 rule (`rc != 0`) would have scored the same run KILLED and the counter would have read MET. |

## Status changes

- **None.** The registry is append-only and this seat's ownership of `corpus/SOURCES.md` is
  append-rows-only: **S270 is a new row** (`mined` at opening, 2026-11-05, tier A, kind `docs`,
  recheck `90d`, used-by `corpus/lessons/round-95.md,plans/round-95.md`), and **no existing row's
  `status`, `recheck` or `used-by` cell was changed** — so there is no old→new pair to log here.
- **S260 — re-opened, deliberately not edited.** The re-open (above) verified S260's anchor against
  the current bytes, but the row's cells are left as they are: its `used-by` still reads
  `corpus/knowledge/mutation-battery-round90.md` and its `recheck` still reads `90d`, both already
  correct for a page re-opened today. **The L1 may add `corpus/lessons/round-95.md` to S260's
  `used-by` cell at settlement** (old → new: `corpus/knowledge/mutation-battery-round90.md` →
  `corpus/knowledge/mutation-battery-round90.md,corpus/lessons/round-95.md`); that is a permitted
  in-place change and would be logged old→new there, exactly as the round-94 lesson did for S262.
  This seat did not make it, because the ownership is append-rows-only.

## Sources

- **S270** — Python documentation, `unittest`; URL `https://docs.python.org/3/library/unittest.html`;
  access 2026-11-05; HTTP 200; 336978 B; sha256
  `f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d`; the page's own version pin
  `Python 3.15.2 documentation` (HTML line 20) and footer `Last updated on Nov 05, 2026 (22:32
  UTC)` (HTML line 3179); the located quote "Each tuple represents a test which raised an
  unexpected exception." (10 words) at HTML lines 2413–2414 and its counterpart "Each tuple
  represents a test where a failure was explicitly signalled using the assert* methods." (15
  words) at HTML lines 2421–2422. Tier A, scoped to the error-vs-failure distinction the counter's
  rule 1 reads; not a mutation-testing vocabulary row and not a kill-rule formula. Status
  `mined`; used-by `corpus/lessons/round-95.md,plans/round-95.md`.
- **S260 (re-opened, no new row)** — Stryker Mutator documentation, "Mutant states and metrics";
  URL `https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/`;
  access 2026-11-05; HTTP 200; 27068 B; sha256
  `8641c38959222238f34aba0e20d3c51919cf183bf19a53f436257614cab656da`; the located quote "The
  running of the tests resulted in an error (rather than a failed test)." (14 words) at HTML line
  24, the `Killed` sentence at HTML line 12. Corroboration for rule 1 only; the URL is already
  held at S260 and no second row is added.

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented).

- **No proposal implemented this round.** The round's single claim (C1) is depth — behavioural
  self-test arms in the mutation battery — and the mined-mistake fix is a repair to the round-95
  counter, so no proposal of this file is inside the claim's scope, and nothing is implemented
  outside it.
- **Proposal 2** (move `## Gate registry` out of `SKILL.md`) stays an **L0 question** rather than a
  claim (`corpus/QUALITY.md` Q67: a move that takes a protocol-named home elsewhere is an L0
  question). Measured for this round: `SKILL.md` is 600 lines / 92672 B and the `## Gate registry`
  section is **37417 B** of it (40.4 %) — the move would be worth more than ever, and is still not
  a lane act.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried and is **still unimplemented**: the round-74 rejection was a W04 duplicate (the URL is
  held twice, at S210 and S213), and the skill's own description is unchanged at **1021** characters
  with a 150-character first sentence (`corpus/knowledge/description-trigger-discipline-round85.md`
  §Limits). `SKILL.md` is at the 600-line box (600 of 600), so a rewrite of the frontmatter
  description has to be paid for by lines saved elsewhere — and this wave's context gives the
  600-line skill budget to no seat, so the claim-adjacent edit is not available.
- **Proposal 1** (a byte ceiling and a 200-character max-line check in the floors guard) stays
  carried: measured at this round's freeze, `SKILL.md` is 600 lines / 92672 B with **165** lines
  over 120 characters, **94** over 300, and the longest line **1491** characters at line 518 —
  the ratchet Q78 asks for, but the instrument that would hold it is not this claim's scope.
- **Proposals 4 and 5** are carried unchanged from the previous rounds; proposal 5 is already
  mined as criterion Q82 and is not re-mined here.

## Settlement

L1 settlement (KotobaR95, after WAVE-DONE) — **placeholder, to be completed by the L1**: the seat
record, the C1 claim verdict (`C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1;
honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`), the no-harm battery readings
at the landing revision, the wave disposition, and the census numbers at the landing revision.
