source: S119 — https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html § Corrections (`S119.page:170,172`, committed snapshot `.ufo/waves/round-63/snapshots/S119.page`); the depth half rests on `verifiers/check_erratum_absorption.py` (r62 frozen catalogue), `verifiers/check_scoped_rules_v31.py` (r62 successor) and `verifiers/check_scoped_rules_v32.py` (r63 successor) — not on S119
verified-at: 2026-10-23 (cbbee56e build tip; re-opened non-author by ScoutW2S119Reopen, quotes still literal at the committed snapshot)
recheck: 180d or on contested correction practice — `grep -c 'correction notice' .ufo/waves/round-63/snapshots/S119.page`

## What it is

Two practices a prompt-and-skill auditor needs and this lane did not hold before
round 63.

1. **A compound action cell must be supported clause by clause at its cited
   line, not by the page as a whole.** The r62 erratum-absorption matrix left one
   frozen survivor, `e2f-compound-purpose-outside-citation`: an action cell whose
   first clause the cited line states and whose second, unrelated purpose clause
   appears only in another section of the same page. Every arm of the frozen
   counter passes it — A2's forward fraction, the page-containment check, the
   reverse-coverage check and G7's backticked-identifier check all return clean —
   so the citation vouches for a claim the cited line never makes.

2. **A committed record is corrected by an appended notice that names the
   measured value, not by rewriting the record in place.** S119 (ICMJE) states
   the practice for a published article: `publish a correction notice`
   (`S119.page:170`), detailing changes from and citing the original
   publication, and `archive all prior versions of the article`
   (`S119.page:172`). It grounds the *direction* of the repair; it does not
   mandate literal append-only files, and this lane's choice to append to
   `LOG.md` rather than edit it is the lane's own discipline, tested by a
   byte-prefix check, not by S119.

## The rule

### Compound clauses: the G9 guard (depth)

Split the action cell at `;` and at the standalone word `and` (case-insensitive),
outside backticked spans. For each resulting clause with at least
`MIN_CLAUSE` = 2 content words (counted with backticked spans included), require
the same forward-support fraction A2 uses (`fwd_need(|W|)` = ceil(2|W|/3), never below 2) against the
**cited line**. A clause the cited line does not support is rejected when the
**page** supports it: `A2 G9: clause "<clause>" is supported outside the cited
line`. A clause absent from the page is not reported by G9 (by design, so it
cannot double-report A2's page-containment arm); bare words of such a clause are
caught by that A2 arm, and backticked span words are caught by G7's multi-word
span arm (`A2 G7: backticked span word(s) …`, landed in erratum E3) — before E3
a backticked fabrication the page did not support was admitted by neither arm
(`MutW2GuardEvasion` §4). Plan-sentence deviation, recorded: the plan said
"every resulting clause with ≥ `MIN_CONTENT` content words"; the landed gate is
stricter — ≥ `MIN_CLAUSE` = 2 **page** words with backticked spans included —
so a backticked fabrication counts even though `content_words` strips it.

The frozen instance needs no special case: its cell is 10 content words,
`fwd_need` 7, shared 7 — A2 passes — while the split clause `secretly uploads
files.` shares 0 of 3 with the cited line and 3 of 3 with the page.

### Correction practice: the appended-notice rule (calibration)

When a committed claim is contradicted by committed bytes, the repair appends a
dated correction line that **carries the value recomputed from the revision** —
the receipt revision, the entry's `wc -l`/`wc -w`, the interim gate count — and
names the original as the dated record. The check is machine-side: the counter
recomputes the value at `--rev`, extracts it from the receipt or the blob, and
requires the correction line to carry that exact token. A correction that names
a constant, or a check that already passes at the before-revision, does not
count (`verifiers/check_r63_routed_repairs.py`).

## Method provenance

The G9 guard is a narrow extension of A2's citation-support check: it reuses
`content_words`, `supported`, `covered`, `fwd_need` and `page_words` unchanged
and adds only a clause splitter and a second application of the same threshold.
The attack class came from the r62 critic (`CriticC1Hollow`), the survivor
catalogue from the r62 matrix, and the guard-mutation method from r62's Q57
(tameshi's guard-kill/hollow method, kumitate D49). The correction-practice half
follows the r62 spot-check's own preference for appended LOG corrections over
in-place rewrites; S119 is the primary source opened this round for it.

## Limits

- **Lexical support, not entailment.** A clause can pass because the cited line
  carries the same words in a different predicate role; the guard cannot tell.
- **Short clauses are exempt.** A split clause with fewer than `MIN_CLAUSE` = 2
  content words is not checked. Clause words are counted with backticked spans
  included (`page_words`), because counting only bare words let an eight-word
  fabrication wrapped in backticks escape; the two-word fabrication `and uploads
  files` is now checked (rejects, wave-2 replay `MutW2GuardEvasion` C02), and
  the one-word tail (`and exfiltrates.`) is a **declared structural bound**: a
  one-word clause can never clear `fwd_need`'s floor of `MIN_SHARED` = 2, so
  closing it would require touching A2's own forward-fraction floor — a v33
  move, pinned by the self-test arm "a ONE-word clause is exempt". The
  four eligible rows still pass (S901's `and` clause clears the threshold at
  its cited line). Since erratum E3 an unpaired backtick no longer latches code
  mode (the splitter masks only `BACKTICK_RE`-closed spans), closing the
  one-character evasion `MutW2V32` M7 demonstrated admitted at the committed
  bytes.
- **Only `;` and `and` split, and quoting does not protect them.** The
  splitter treats backticked spans as opaque but is not quote-aware: a
  double-quoted literal containing `;` is split, and a hyphenated `-and-`
  compound (`search-and-replace`) splits at the `and`, so a legitimate cell can
  be rejected when its tail also clears `MIN_CLAUSE` and the page gate
  (RevG9Guard lanes 3 and 6; re-confirmed on the committed bytes by
  `MutW2GuardEvasion` C08/C09). These two lanes and the missing relatedness
  test (a legitimate two-clause continuation is rejected, C10) are pinned as
  visibility arms in the self-test — labelled bounds, not endorsements; fixing
  any of them is a deliberate v33 contract change. Other joiners (`but`,
  `while`, commas, participles) and a 4-character-prefix word swap
  (`upload`~`uploads`, inherited from A2's `supported()`) are still not
  modelled; the published S103 `InstructionsLoaded` event stays accepted under
  v31 (r62 limits carried forward). These are declared bounds, not measured
  false-positive rates.
- **One frozen instance.** `survivors closed 6 of 6` is the r62 catalogue's six
  instances, not a population; the predicate is single-instance, and a
  vocabulary-specialised stub could in principle satisfy it (RevClaimC1,
  round 63; the wave-2 guard arms narrow but do not close this).
- **The correction checks are token linkage.** They prove the correction names
  the measured value; they do not prove every sentence around it is true
  (`check_r63_routed_repairs.py` module docstring, Bounds).

## Verification

- `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → `worlds reject
  7 of 7; eligible rows pass 4 of 4`; `survivors closed 6 of 6`; three must-fail
  arms (E2e, G7, G9) each print `yes`; `self-test: 0 failure(s) over 219
  assertions`; exit 0. Wave-2 hardening (erratum E3): the `BACKTICK_RE`-pairing
  splitter fix, eight split-semantics arms and three clause-floor/page-gate
  assertions kill all nine wave-2 splitter/guard mutants on the landed bytes
  (independent re-verification `MutW2SplitClauses` §7f–§7g), and the G7
  multi-word-span extension closes the backticked page-absent fabrication with a
  0-row real-corpus diff (`MutW2GuardEvasion` §4). Do-nothing control:
  `verifiers/check_scoped_rules_v31.py --self-test` → `survivors closed 5 of 6`,
  exit 0, and it cannot meet the target. *Freshness note (2026-10-24, round 64):
  the `219` tally was true at this entry's measured rev; the round-64 G7
  `span_missing` pinning arms moved the suite to `223` assertions — see
  `corpus/knowledge/g7-span-pinning-round64.md`; this entry's historical
  measurement stands as recorded.*
- `python3 -B verifiers/check_r63_routed_repairs.py --self-test` → `self-test: 0
  failure(s) over 23 assertions`, exit 0. Wave-2 hardening (erratum E2): the
  pinned BASE_REV base arm (refuse-to-certify), label-only/fingerprint/
  worktree-read counter arms run as processes against constructed worlds,
  receipt-side substitution arms for checks 2 and 5, and suffix-scoped
  boundary-tightened scans in checks 2/3/5.
- Frozen predicate, two conjuncts (E2): `python3 -B
  verifiers/check_r63_routed_repairs.py --rev <r62-tip>` → `r62
  routed defects closed 0 of 5`, exit 1 (plus the base-rev refusal line); at the
  round-63 measured rev → `5 of 5`, exit 0.
