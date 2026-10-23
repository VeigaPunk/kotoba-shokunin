# ScribeQuality — kotoba round 61, attempt 1

## Behavior

Prepared a copy-ready Q56 row for `corpus/QUALITY.md`, using the Q54/Q55 table shape, plus a matching proposed M91 lesson entry so the row's grounding link resolves. The row reserves `byte-exact` for literal bytes and names the required alternative phrase for shaped quotes. No lane source or lesson was edited; this report is the sole lane write from this seat.

## Drafts

Append the row after Q55 in `corpus/QUALITY.md`:

```text
| Q56 | Reserve `byte-exact` for literal byte-for-byte equality between the recorded quote and the cited source bytes; when an HTML-entity escape or whitespace normalization is required, describe the result as `quote-equal after documented shaping`, never `byte-exact`. | report, lesson, and knowledge-entry descriptions of quote/source equality | M91 `report-evidence-overclaim` (`corpus/lessons/round-61.md` § Mistakes); round-60 verifier spot-check §7 defect 5 (`corpus/lessons/round-60-verifier-spotcheck.md:129-132). | — |
```

Proposed grounding entry under `## Mistakes` in `corpus/lessons/round-61.md`:

```text
- **M91 `report-evidence-overclaim`** · The round-60 report said “32 reports, 0 dead” although the closure found 29 committed build reports (59/65 seat reports committed overall); it pointed to `C1-measure.txt` for the base measurement that is recorded in `receipts/freeze2-selftest.txt`; and its summary called the S106/S107 quotes “byte-exact” despite S106's documented `&#124;` escape and S107's whitespace normalization (`corpus/lessons/round-60-verifier-spotcheck.md` §7 defects 2, 3, and 5). · captured-by: round-60 non-author closure, §7 · fix: reconcile report counts with committed outputs, name the exact base-measurement receipt, and reserve `byte-exact` for literal byte equality; call a quote requiring the documented escape or normalization “quote-equal after documented shaping” (Q56). · used-by: `corpus/QUALITY.md` Q56.
```

The Q56 `grounded in` cell points to the M91 entry at `corpus/lessons/round-61.md` § Mistakes; the M91 draft carries the reciprocal `used-by` pointer to Q56. Draft name `report-evidence-overclaim` is proposed, not an already observed landed M91 label.

## Findings and provenance

- `plans/round-61.md:91-93` defines M91 as the round-60 “32 reports, 0 dead” overstatement and accompanying pointer sloppiness, names `corpus/lessons/round-61.md` § Mistakes as its destination, and calls for Q56. The round-61 lesson file was absent when read; therefore M91 above is proposed text, not a landed entry.
- `corpus/QUALITY.md:65-66` shows Q54/Q55's five-column table format and append-only row placement. Q56's scope is quote/source equality claims across reports, lessons, and knowledge entries.
- `corpus/lessons/round-60-verifier-spotcheck.md:129-132` records defect 5 verbatim: S106 used the documented `&#124;` escape, S107 matched after whitespace normalization, and the report's “byte-exact” summary overstated. The draft addresses both examples without treating shaped equality as byte equality.
- The same closure at §7 defects 2-3 records the base-measurement pointer mismatch and the 32-versus-29 committed build-report discrepancy cited in the proposed M91 entry.
- `plans/round-61.md:63-74` freezes R-e as the Q56/M91 repair. The inspected `verifiers/check_routed_repairs.py` says R-e checks for `Q56`, `byte-exact`, and an existing lesson containing `M91`; its header explicitly says it does not judge repair substance. The proposed text therefore supplies reviewer-facing semantics beyond that structural count.
- The existing `.ufo/waves/round-61/controls/C2-base.txt` contains `R-e byte-exact criterion + M91: missing`, `routed repairs verified 0 of 6`, and `base-exit=1`. The plan identifies it as the committed base control. This seat only read the receipt; it did not run the counter or remeasure the base.

## Gates and measurements

No shell command, counter, test, build, lint, or other measurement was run by this seat. No measurement date, command output, or exit code is claimed as newly executed. The C2 output above is quoted from the existing control receipt, not represented as this seat's run. No installs.

## Touched surfaces and boundaries

- Lane write: `.ufo/waves/round-61/wave/ScribeQuality.md` only.
- Read-only source surfaces: `plans/round-61.md`, `corpus/QUALITY.md`, `corpus/lessons/round-60-verifier-spotcheck.md`, `.ufo/waves/round-61/controls/C2-base.txt`, and `verifiers/check_routed_repairs.py`.
- No edits to `corpus/QUALITY.md` or either lesson, no Git/jj/index/state mutation, no commit or push, no dispatch, no ask, and no scratch artifact.

## Out of scope and limits

This is a report-only draft, not an integrated or measured Q56/M91 repair. The target round-61 lesson did not exist at inspection time. The draft does not establish a current tip result or claim that C2 has passed; the only observed C2 result is the pre-repair base receipt.

## Artifact paths

- Report: `.ufo/waves/round-61/wave/ScribeQuality.md`
- Proposed QUALITY row target: `corpus/QUALITY.md` (append after Q55)
- Proposed M91 target: `corpus/lessons/round-61.md` (`## Mistakes`)

Installs: no installs.
Blockers: none.
Produced: copy-ready Q56 and M91 drafts with reciprocal lesson/criterion pointers, grounded in the r60 closure's quote-shaping defect.
