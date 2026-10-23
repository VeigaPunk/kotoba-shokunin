Result: DONE — Drafted three append-only QUALITY rows (Q38–Q40) for L1 integration, with evidence of how each catches the round-55 finding.

## Scope and provenance

- Read `plans/round-56.md` (especially lines 34–38 and 97–105), `corpus/QUALITY.md` (lines 3–10, 38–52), `corpus/lessons/round-55-verifier-spotcheck.md` (lines 32–39, 61–73, 130–140), `corpus/lessons/round-51.md` (M34 and Q27, lines 18–23), and `.ufo/waves/round-55/falsify/W2RerunC2.md` (lines 13–16, 78–101, 107–116).
- `QUALITY.md` currently ends at Q37. Its existing table columns are `id | criterion | applies to | grounded in | supersedes`.
- `corpus/lessons/round-56.md` was not present when read. Thus M52 and M53 below are proposed lesson-class pointers, not existing rows. The rows must not be merged until those matching class rows are actually registered in the round-56 lesson. M34 already exists in `corpus/lessons/round-51.md`.
- No product file was edited, no command or gate was run, no tool was installed, and no sandbox commit was made. The sole written file is this scoped report. The observations below are from the cited committed/working-tree evidence; no claim is made that a new gate passed.

## Draft QUALITY rows

```markdown
| id | criterion | applies to | grounded in | supersedes |
|---|---|---|---|---|
| Q38 | A `new ground` count is the number of distinct normalized forms absent from all base text, not the number of rows or example tokens; compare against the whole declared base tree outside `.ufo/`, including SOURCES and lessons, so a held form cannot become new under another example name. | new-ground counters and learning claims | M52 `new-ground-form-collision` (`corpus/lessons/round-56.md` § Mistakes; proposed; evidence: `corpus/lessons/round-55-verifier-spotcheck.md:69-72,133`) | — |
| Q39 | A gate's nested self-test timeout is calibrated only when it has measured-duration headroom under a declared load; otherwise the timeout receipt records host load and elapsed wall time, and an unannotated timeout cannot distinguish a hang from load-delayed completion. | nested self-test timeouts, gate verdicts and their receipts | M53 `nested-self-test-timeout-under-load` (`corpus/lessons/round-56.md` § Mistakes; proposed; evidence: `corpus/lessons/round-55-verifier-spotcheck.md:82,135` and `.ufo/waves/round-55/falsify/W2RerunC2.md:13-16,78-101,113-116`) | — |
| Q40 | A seat's return or cancellation status does not close its output window: a final sweep after the last seat write covers every seat-writable directory and is recorded; any later report it finds is counted as written and, before the round report, either committed with its correction/disposition or removed. | round reports, seat accounting and wave-evidence dispositions | M34 `late report from a cancelled seat` (`corpus/lessons/round-51.md:18`; repeated in `corpus/lessons/round-55-verifier-spotcheck.md:32,36-37`) | Q27 |
```

Q40 intentionally subsumes Q27: it retains Q27's binding of seat records to actual writes and its post-last-write, all-directory sweep, while making the disposition of a discovered late report explicit. If the integrator judges Q27 already sufficient and declines supersession, retain Q27 and do not add duplicate Q40.

## Round-55 catch demonstrations

- **Q38:** The spot-check says the Codex `$…` and Copilot CLI `/…` forms were already held in base under other example names, while the v2 count reported `new ground 4`; only Cursor `/skill-name` and opencode `@skill-id` were new forms, for a substantive count of 2 (`round-55-verifier-spotcheck.md:65,69-72`). Q38 would search all base text and collapse to distinct forms, so the two relabelled held forms could not inflate G. This corrects the reported count from 4 to 2; it does not imply the frozen G≥2 predicate would fail.
- **Q39:** The round-55 C2 measurement missed the `check_assertion_floors.py` V control with exit 2 (`round-55-verifier-spotcheck.md:82`). The rerun records a 120-second nested limit and the child completing successfully in 221.96 seconds (`W2RerunC2.md:97,101`), with high load averages recorded at lines 16 and 71. Q39 would require the evidence needed to identify this as load-delayed completion rather than a hung child, and would expose that the 120-second cap was below the observed runtime under that load.
- **Q40:** The spot-check found `.ufo/waves/round-55/falsify/ReviewLessonMistakes.md` untracked; it came from a seat the report called cancelled without a report and was not counted (`round-55-verifier-spotcheck.md:32,36-37`). A post-last-write sweep would find it, and Q40 requires its commit with correction/disposition or removal before the round report. Q27 already catches the late-write/sweep failure; Q40 makes the required resolution explicit.

## Limits

The first two rows have exact evidence and proposed lesson classes but their round-56 class rows do not yet exist in the observed tree. This seat did not create lesson rows or modify `QUALITY.md`, as its write scope is only this report. The timeout evidence is specific to the reported high-load run; the cited rerun says idle-host behavior was not measured (`W2RerunC2.md:113-116`).