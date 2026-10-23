Result: DONE — Q49–Q51 are drafted as exact rows for routes R1–R3, with the requested M79–M81 references.

# Scope and provenance

Draft only for `corpus/QUALITY.md`; no lane QUALITY or lesson file was edited. Read `corpus/QUALITY.md:1-11,41-63` and the round-58 spot-check findings at `corpus/lessons/round-58-verifier-spotcheck.md:96-104,241-262`. The append-only supersedes cells below make Q49 a fuller R1 rule for Q40, Q50 the fuller R2 receipt rule for Q36, and Q51 the fuller R3 source-coverage rule for Q31.

The M79–M81 classes below use the draft mappings supplied by `ScribeMistakes`: M79 `misrooted-seat-report-and-premature-sweep`, M80 `tip-receipt-asserted-not-committed`, and M81 `counter-blind-fields-and-ua-sensitive-fetch`. At the time of this draft, `corpus/lessons/round-59.md` was not present, so these are pointers to the lesson entries being drafted, not a claim that those entries have landed.

# Proposed QUALITY rows (verbatim)

```markdown
| Q49 | Every seat's declared `Report:` path is lane-local; return or cancellation does not close its output window, and the recorded final misroot sweep covers every seat-writable directory only after the last seat settles. Any report the sweep finds is counted as written and, before the round report, either committed into the lane with its provenance/correction or removed with its disposition recorded. | seat report paths, round seat accounting and final misroot sweeps | M79 `misrooted-seat-report-and-premature-sweep` (`corpus/lessons/round-59.md` § Mistakes, draft); round-58 R1 found `ReviewBudgetMove.md` written under the fleet root, omitted from the seat paragraph, after the 08:27:59Z misroot sweep (`corpus/lessons/round-58-verifier-spotcheck.md:243-252`; `.ufo/waves/round-58/falsify/ScoutMisroot.md:5-46`). | Q40 |
| Q50 | Every gate result a report states for the lane tip has a committed receipt that names that exact tip revision and the observed result; a result asserted only in prose or a commit message, or covered only by receipts for another revision, is not tip evidence. | round reports, LOG entries and lesson Gate records stating tip gate results | M80 `tip-receipt-asserted-not-committed` (`corpus/lessons/round-59.md` § Mistakes, draft); round-58 R2 found the checklist exit 0 and `4 DRIFT at tip` stated without committed tip receipts, while cited receipts covered base/`46b4a706` and the C1 remeasure at `6de8e2eb` recorded FAIL (`corpus/lessons/round-58-verifier-spotcheck.md:253-257`). | Q36 |
| Q51 | A report credits a counter with checking only field cells or source-page facts its code reads from committed bytes at the measured revision; a live `--fetch` without a committed page snapshot is not page evidence. Each field or semantic judgment the counter does not make is explicitly assigned to named non-author seats, with their committed review cited. | source-claim counters and reports describing counter coverage or source validation | M81 `counter-blind-fields-and-ua-sensitive-fetch` (`corpus/lessons/round-59.md` § Mistakes, draft); round-58 R3 found the C1 counter read neither `What a file sets` cells nor a frozen page snapshot and that the Cursor urllib 403/curl 200 window moved G to its floor; the field judgments were separately checked by named seats (`corpus/lessons/round-58-verifier-spotcheck.md:96-104,258-262`). | Q31 |
```

# Behavior, gates, surfaces, and limits

- **Behavior:** rows Q49–Q51 are supplied for integration after Q48. The R1/R2/R3 failure evidence is from the cited committed round-58 spot-check; no new counter, gate, or source run was made.
- **Gates:** none run. This was a report-only draft; no tools were installed or updated.
- **Touched surface:** `.ufo/waves/round-59/build/ScribeQuality.md` only. `corpus/QUALITY.md` and `corpus/lessons/round-59.md` remain unchanged by this seat.
- **Out of scope:** integrating the rows or lesson text, editing round-59 routes/counters, and adjudicating the R4/R5 routes.
- **Evidence limit:** M79–M81 are draft lesson references at this point. The source `corpus/lessons/round-59.md` read returned “not found”; the class names were confirmed by ScribeMistakes' draft mapping, not by an integrated lesson artifact.

Report: .ufo/waves/round-59/build/ScribeQuality.md
