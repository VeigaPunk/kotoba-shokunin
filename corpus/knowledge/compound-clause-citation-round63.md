source: S119 (correction practice); the depth half rests on `verifiers/check_erratum_absorption.py` (r62 frozen catalogue), `verifiers/check_scoped_rules_v31.py` (r62 successor) and `verifiers/check_scoped_rules_v32.py` (r63 successor) — not on S119

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
   the practice for a published article: publish "a correction notice as soon as
   possible detailing changes from and citing the original publication" and
   "archive all prior versions of the article" (`S119.page:170,172`). It grounds
   the *direction* of the repair; it does not mandate literal append-only files,
   and this lane's choice to append to `LOG.md` rather than edit it is the lane's
   own discipline, tested by a byte-prefix check, not by S119.

## The rule

### Compound clauses: the G9 guard (depth)

Split the action cell at `;` and at the standalone word `and` (case-insensitive),
outside backticked spans. For each resulting clause with at least
`MIN_CLAUSE` = 2 content words (counted with backticked spans included), require
the same forward-support fraction A2 uses (`fwd_need(|W|)` = ceil(2|W|/3), never below 2) against the
**cited line**. A clause the cited line does not support is rejected when the
**page** supports it: `A2 G9: clause "<clause>" is supported outside the cited
line`. A clause absent from the page too is already reported by A2's
page-containment arm, so G9 never double-reports it.

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
  content words is not checked, so a one-word false tail passes. Clause words are
  counted with backticked spans included (`page_words`), because counting only
  bare words let an eight-word fabrication wrapped in backticks escape
  (RevG9Guard's lane 2, closed before the report); the two-word fabrication
  `and uploads files` is now checked, and the four eligible rows still pass
  because S901's `and` clause clears the threshold at its cited line.
- **Only `;` and `and` split, and quoting does not protect them.** The
  splitter treats backticked spans as opaque but is not quote-aware: a
  double-quoted literal containing `;` or `and` is split, and a hyphenated
  `-and-` compound (`search-and-replace`) splits at the hyphen, so a legitimate
  cell can be rejected when its tail also clears `MIN_CLAUSE` and the page gate
  (RevG9Guard lanes 3 and 6, round 63). Other joiners (`but`, `while`, commas,
  participles) and `R and D`-style abbreviations are still not modelled; a
  4-character-prefix word swap (`upload`~`uploads`) can make a clause look
  supported. These are declared bounds, not measured false-positive rates.
- **One frozen instance.** `survivors closed 6 of 6` is the r62 catalogue's six
  instances, not a population; the predicate is single-instance, and a
  vocabulary-specialised stub could in principle satisfy it (RevClaimC1,
  round 63).
- **The correction checks are token linkage.** They prove the correction names
  the measured value; they do not prove every sentence around it is true
  (`check_r63_routed_repairs.py` module docstring, Bounds).

## Verification

- `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → `worlds reject
  7 of 7; eligible rows pass 4 of 4`; `survivors closed 6 of 6`; three must-fail
  arms (E2e, G7, G9) each print `yes`; `self-test: 0 failure(s) over 208
  assertions`; exit 0. Four G9 assertions discriminate the mutants MutG9Guard
  named: `;`-only split, `and`-only split, a clause with one shared word
  (threshold 1), and a backticked fabrication — each mutant turns the self-test
  red. Do-nothing control:
  `verifiers/check_scoped_rules_v31.py --self-test` → `survivors closed 5 of 6`,
  exit 0, and it cannot meet the target.
- `python3 -B verifiers/check_r63_routed_repairs.py --self-test` → `self-test: 0
  failure(s) over 15 assertions`, exit 0 (constructed repaired and unrepaired
  trees, a label-only shortcut and a rewritten LOG each fail as declared).
- `python3 -B verifiers/check_r63_routed_repairs.py --rev <r62-tip>` → `r62
  routed defects closed 0 of 5`, exit 1; at the round-63 measured rev → `5 of 5`,
  exit 0.
