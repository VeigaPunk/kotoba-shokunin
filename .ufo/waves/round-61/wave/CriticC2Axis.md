# CriticC2Axis — C2 measures repair-record completion, not calibration error

Seat: `kotoba-r61-wave-CriticC2Axis-3`. Review only; no judgment, admission, integration, runtime invocation, or git/jj mutation. The only file written is this report.

## Recommendation

The SCORECARD observation reporting `routed repairs verified K of 6` should carry **`operability (advisory; routed-repair record completion)`**, not an unqualified `calibration` label. Calibration is a plausible benefit of some repairs, but the frozen counter does not measure that benefit. In particular, **`6 - K` is not a measured count of self-assessment mismatches**.

Preserve the original declaration separately: **C2 was declared calibration** in `plans/round-61.md:61-74`. Do not silently replace that declared claim with an operability success, change the frozen predicate, or claim two axis wins from one count. This critique does not reassign the canonical round's axes or supply its verdict. The canonical judge must see both the declared axis and what the evidence actually measures.

## Authority and evidence

All lane-relative paths below resolve under `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. No scratch artifact is evidence.

- Fleet `/home/vgpnk/Projects/shokunin/AXES.md:13`: operability is **“Runnable artifacts: checklists that are executable, commands that exist, scripts that run”**; its signal is **“A checklist item can be run and produces the stated outcome.”**
- The same `AXES.md:15`: calibration is **“Self-assessment quality: gaps named honestly, confidence graded, overreach caught”**; its signal is **“SHONEN.md/SCORECARD entries match observed repo state.”**
- `AXES.md:27-38` requires a falsifiable before→after for each claim, causal separability, distinct axes, and no harmed axis. `AXES.md:79-81` binds SCORECARD evidence and planned target axes.
- Canonical `/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/AXES.md:13-16,27-38,75-83` was also opened and carries the same relevant wording. The opened AXES text does **not** literally contain the sentence “count mismatches”; the assignment's mismatch-count requirement operationalizes its self-assessment-versus-observation signal and measurable-before→after requirement. I do not misattribute that sentence as a quotation.
- `plans/round-61.md:61-74` freezes six repair obligations and a counter result, not a self-assessment comparison table.
- `verifiers/check_routed_repairs.py:63-112` calculates six booleans over text; `:135-151` reads five committed file blobs and returns success when their boolean sum is six. `:34-37` explicitly disclaims judging whether repair text is substantively honest.
- `corpus/lessons/round-60-verifier-spotcheck.md:112-143` supplies the independent grounds for the repairs. It distinguishes disclosure/pointer/count defects, a missing standalone census file despite a passing census, quote-shaping overstatement, and control-process debt.
- `SCORECARD.md:7-15` maps the lane's `consistency` label to calibration through claim-scope coherence. That mapping does not turn any record-completion count into a calibration measurement.
- `corpus/QUALITY.md:39` (Q28) preserves the declared counter and requires later judgment-table changes to be reported as a second measurement, not substituted. `:42` (Q31) limits descriptions of a counter to checks it actually runs; additional checks belong to reviewer judgment.

## Reading 1 — the strongest charitable calibration interpretation

The repair list is not arbitrary paperwork. The non-author r60 closure already compared the lane's account with evidence:

- R-a responds to the build-wave self-report “32 reports, 0 dead” versus 29 committed build reports (`round-60-verifier-spotcheck.md:120-124`).
- R-b responds to an incomplete landed-scope account: `plans/round-60.md` and `considerthese/2026-10-23.md` were changed but not named (`:114-116`).
- R-c responds to a base-measurement citation that pointed at the wrong receipt (`:117-119`).
- R-e originates in “byte-exact” overreach despite the documented S106 escape and S107 whitespace normalization (`:129-132`).

Honest, explicitly linked errata for those discrepancies can improve calibration: the revised account becomes closer to observed state, with original filed history retained. AXES does not exclude LOG/report self-assessments merely because its illustrative signal names SHONEN/SCORECARD. Nor must a bounded calibration claim demonstrate global perfection.

Under this reading, a repair count can be a **proxy** for resolution of a fixed, independently established mismatch cohort. To support that reading here, the evidence must bind each original assessment to its observed value, its correction, and an after-state comparison. Substantive review would then establish the calibration benefit; the frozen counter could at most locate the repair records. Its own honesty disclaimer acknowledges precisely this missing step.

This is the best case for the plan's label. It is not evidence that the proxy has been validated, or that six repair records correspond to six calibration mismatches.

## Reading 2 — what the frozen measurement actually discriminates

| Arm | Actual code predicate | Calibration significance and missing comparison |
|---|---|---|
| R-a | Four substrings occur somewhere in LOG (`:69-75`). | Motivated by a real self-report mismatch, but the code does not count committed reports, execute the printed counting command, or establish that the text corrects the report. |
| R-b | Both filenames occur somewhere in LOG (`:77-78`). | Could repair scope disclosure; mentioning both filenames is not a comparison of the declared scope with the landed diff. |
| R-c | Both receipt names occur on one LOG line (`:80-84`). | Could repair evidence attribution; either direction of attribution, or even a denial of the correction, has the same predicate value. |
| R-d | A file exists and its last nonempty line is `exit=0` (`:86-93`). | Receipt completion. The r60 closure already found census conformance satisfied and a live census passing (`spotcheck:125-128`); missing a standalone output file is not automatically a false self-assessment. |
| R-e | QUALITY contains `Q56` and `byte-exact`; the lesson contains `M91` (`:95-102`). | A new criterion and mistake marker do not themselves correct the historical overstatement or establish current wording agrees with the shaped bytes. |
| R-f | A receipt contains `merge-base --is-ancestor` and `exit 0` (`:104-110`). | Control-process receipt presence, not a comparison of an assessment with observed state. The code does not run ancestry, bind commit identities, or check dispatch chronology. |

The observed variable is **repair-record pattern presence**. It is neither a residual-mismatch count nor a confidence/error calibration measurement. R-d and R-f expose the category error even if every record is honest: they concern evidence packaging and process ordering. R-e is a preventive rule, not an after-state comparison. Existing calibration motivations do not make this heterogeneous denominator a calibration-error denominator.

The base control establishes that the base lacks these new record patterns. It does not establish “six inaccurate self-assessments before,” and a later six-of-six output would not establish “zero mismatches after.”

## Strongest local counterexample — assertions alone satisfy all six arms

This is a **static counterexample, not an executed fixture or receipt**. The committed code's own `self_test()` constructs an assertion-only `all-repairs` blob map and expects six (`check_routed_repairs.py:166-184`), including `$CTL`/`$DATA` text rather than authenticated ancestry. Production `main()` adds committed-blob retrieval but no substantive comparison before calling the same helper (`:135-151`).

A stronger assertion-only world can expressly deny that it supplies corrections while retaining the recognized tokens. Full hypothetical blob contents follow; these paths are inputs to the argument, not edits I performed.

Target: `LOG.md`

```text
Vocabulary only; this is not a correction: build reports claimed 32 committed 29 .ufo/waves/round-60/build
Mentioned filenames, not a landed-scope reconciliation: plans/round-60.md considerthese/2026-10-23.md
Both names are mentioned without identifying the base measurement: receipts/freeze2-selftest.txt C1-measure.txt
```

Target: `corpus/QUALITY.md`

```text
Q56 byte-exact — vocabulary only; no equality requirement is established here.
```

Target: `corpus/lessons/round-61.md`

```text
M91 — vocabulary only; no mistake analysis or correction is supplied.
```

Target: `.ufo/waves/round-61/census-after.txt`

```text
This census was not run.
exit=0
```

Target: `.ufo/waves/round-61/receipts/controls-ancestry.txt`

```text
Not executed: merge-base --is-ancestor
exit 0
```

Static branch trace against the opened code:

- R-a: all four required substrings are present → true.
- R-b: both required paths are present → true.
- R-c: both receipt names share a line → true.
- R-d: the final nonempty line is exactly `exit=0` → true.
- R-e: both QUALITY tokens and the lesson token are present → true.
- R-f: both ancestry tokens are present → true.

**[INFERENCE]** With these five blobs committed in an otherwise readable revision, `check_repairs()` returns six and production `main()` prints `routed repairs verified 6 of 6` and returns 0. This follows directly from `:63-112,135-151`; I did not create that revision or invoke the checker. None of the hypothetical records performs an assessment-versus-observation comparison; some explicitly disclaim the purported action. Thus the six-of-six predicate cannot distinguish calibrated reconciliation from asserted completion.

This is not an allegation that the live L1 will use false receipts. It is a failure of the measurement's discrimination. It also means merely renaming the metric **does not** establish substantive operability: an ancestry command printed in an unrun receipt has not produced the stated outcome.

## Impacted axes and limits of correction

- **Calibration / mapped consistency:** using the repair count as a measured mismatch reduction would itself overstate the evidence. Neither a calibration band increase nor saturation/retirement follows from it.
- **Operability:** the most accurate label for the counted work is runnable record-checklist/receipt completion, bounded by the fact that the checker recognizes text and the L1/reviewer must authenticate outcomes. Label honesty is not gate hardening.
- **Claim separability:** the substantive R-f obligation names the C1 data commit (`plan:72-74`). It therefore requires C1 data to exist before that obligation can be evaluated. AXES `:31-32` requires verification without other claims having landed. A label correction does not remove this dependency; I did not audit C1 here.
- **Depth and adjacency:** this review supplies no measurement or verdict on C1 or C3. Reclassifying C2 must not borrow their evidence or their axis credit.

The fixable defect is the description/axis attribution of what the counter reads. The predicate's acceptance of assertion-only worlds is a separate measurement-integrity problem for the canonical judge. A successful count under the frozen predicate is not, by itself, authority to admit the declared calibration move. I assign no formal claim or round status.

## Smallest safe correction

1. Put **`operability (advisory; routed-repair record completion)`** on the SCORECARD observation carrying this counter, and explicitly state it counts record patterns. Preserve the fact that frozen C2 was declared calibration; do not retroactively present a new axis as the original declaration or a second success.
2. State that calibration improvement remains a substantive assessment-versus-observation question, not an inference from `K`. Keep any calibration/consistency score unchanged on the strength of this count alone.
3. If the L1 wants evidence for the declared calibration reading, present original assessment → independently observed state → linked erratum → after-state comparison for the genuine discrepancy cohort. Do not manufacture “six mismatches” from the six repair obligations. A new mismatch counter/guard is a separately identified measurement, never a replacement for the frozen result (Q28). This report neither changes nor supplies such a counter.

Complete suggested annotation, for the integrator only:

Target: `SCORECARD.md` — appended C2 measurement note

```markdown
**Round 61 C2 axis/evidence note.** The frozen plan declared C2 as calibration. Its counter, `python3 -B verifiers/check_routed_repairs.py --rev <rev>`, counts six routed repair-record patterns; the corresponding observation is labelled **operability (advisory; routed-repair record completion)**. This count is not a count of self-assessment mismatches and does not establish a calibration/consistency improvement or substantive receipt authenticity. The declared calibration claim and its frozen result remain visible for the canonical judge; this annotation neither substitutes a new predicate nor claims a second axis win. The committed base control records `routed repairs verified 0 of 6`, `base-exit=1`; no tip measurement is supplied by this note.
```

The annotation deliberately contains no invented tip result, scalar change, admission, or completed comparison.

## Receipts and honesty boundary

Review clock command actually executed:

```sh
date -u '+%Y-%m-%dT%H:%M:%SZ'
```

Pasted output:

```text
2026-10-23T19:11:24Z
```

Exit code: 0. This is the review timestamp, not the timestamp of any checker run.

Existing base evidence read, **not rerun**: `.ufo/waves/round-61/controls/C2-base.txt:1-8`.

```text
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
base-exit=1
```

Command association: `plans/round-61.md:63-65` identifies `python3 -B verifiers/check_routed_repairs.py --rev f3246d14`; the assignment supplies full base `f3246d1493b60ea1c0d947a19c39f9e08e92f326`. The receipt itself contains neither the command line nor `date -u`; its measurement UTC is **not recorded in that file**. I do not fill that gap from the review clock or claim a fresh base measurement.

No lane checker, self-test, mutation runtime, build, formatter, Rust judge, or network fetch was invoked. No integrated-tip result, semantic receipt authenticity, after-state mismatch count, or independent non-author judgment was verified by this seat. The counterexample result above is explicitly static inference.

Installs: no installs.
Blockers: none.
Attacked: C2's calibration-axis attribution and the inference from six repair-record predicates to measured self-assessment accuracy.
