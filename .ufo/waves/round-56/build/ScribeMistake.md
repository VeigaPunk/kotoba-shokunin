Result: DONE — Both candidates are evidence-backed; M52 has a held-form control, and M53 is a recurrence of the already-covered M34/Q27 class.

## Findings and proposed lesson rows

Drafts below use the requested `class · evidence pointer · captured-by · fix` order. M53 should be described as a recurrence, not a new quality criterion.

- **M52 — `example-name-new-ground`** · `corpus/lessons/round-55-verifier-spotcheck.md:69-73,132-133` records the old v2 result (`new ground 4`) against only two substantive forms and routes defect 2. The round-56 rule is `plans/round-56.md:35-38`; it counts distinct normalized paths against all base text outside `.ufo/`. The concrete held-form world is `.ufo/waves/round-56/controls/CtlC1HeldVariant-v12.md:240-267` and its receipt `.../CtlC1HeldVariant-v12.txt:240-267`: `opencode-held-new-page`, commit `49ba2ca0a57923ff2348a5fd8db7b427492b7803`, uses `.opencode/agents/`, whose normalized form has `base_count=10`; the recorded run prints `agent-definition locations found on the live page 1 of 1; new ground 0`, `opencode BACKED ... found=yes base_count=10`, exit 1. The post-v1.3 rescore is `.ufo/waves/round-56/controls/C1-v13-rescore.txt:15-25`; it again prints `1 of 1; new ground 0`, `opencode BACKED ... found=yes base_count=10`, exit 1. · Captured by the round-55 outside spot-check and the round-56 `CtlC1HeldVariant` control. · Count distinct normalized forms absent from the whole base tree, not row/example names; the held-world output demonstrates that a live, backed held path contributes zero new ground. **Calibration:** this one-client world exercises the G component, but its exit 1 also has F=1; it is not evidence that the full C1 predicate failed solely because of G, nor a full-predicate control.

- **M53 — `cancelled-seat-output-untracked` (repeat of M34/Q27)** · `corpus/lessons/round-55-verifier-spotcheck.md:31-37` records `git status --porcelain` → `?? .ufo/waves/round-55/falsify/ReviewLessonMistakes.md`, one untracked seat report; line 37 states it came from a seat the round report listed as cancelled without a report. The artifact identifies itself at `.ufo/waves/round-55/falsify/ReviewLessonMistakes.md:1,3,60`. The same class is M34 at `corpus/lessons/round-51.md:18-23`; Q27 is `corpus/QUALITY.md:38`. · Captured by the round-55 outside spot-check (defect 1, `corpus/lessons/round-55-verifier-spotcheck.md:36-37,132`). · Apply Q27: count the seat output, not its return/cancellation status, and run the printed leftover sweep after the last seat write over every seat-writable directory. Q27 was shown able to fail on the round-50 record at `corpus/lessons/round-51.md:20-23` (it rejects the cancellation/sweep record because seat files existed beyond the return-gated sweep). The round-55 recurrence means this is not evidence that the fix was applied successfully in round 55; do not mark the class resolved.

## Gates and provenance

- No counter, test, or other executable check was run by this scribe. The C1 command and outputs above are quoted from the committed control receipts, not represented as this seat's execution. The recorded command for the v1.2 held-world is `timeout 70 python3 -B verifiers/check_agent_definitions.py --rev 49ba2ca0a57923ff2348a5fd8db7b427492b7803 --fetch` (`CtlC1HeldVariant-v12.txt:245-267`); the current v1.3 rescore command and output are at `C1-v13-rescore.txt:15-25`.
- The round-55 spot-check records the leftovers command/output but gives no exit code at `corpus/lessons/round-55-verifier-spotcheck.md:31-32`; none is inferred here.
- `corpus/lessons/round-56.md` was not present when read, so these are proposed rows, not claims that lesson content has landed.

## Touched surfaces, scope, and artifacts

- Touched: only `.ufo/waves/round-56/build/ScribeMistake.md` (this report).
- No lesson, product code, counter, judge, commit, push, source fetch, install, or other lane file was changed; no subagent or runtime was invoked.
- Evidence artifacts: `plans/round-56.md:35-38`; `corpus/lessons/round-55-verifier-spotcheck.md:31-37,69-73,132-133`; `corpus/lessons/round-51.md:18-23`; `corpus/QUALITY.md:38`; `.ufo/waves/round-56/controls/CtlC1HeldVariant-v12.md:240-267`; `.ufo/waves/round-56/controls/CtlC1HeldVariant-v12.txt:240-267`; `.ufo/waves/round-56/controls/C1-v13-rescore.txt:15-25`; `.ufo/waves/round-55/falsify/ReviewLessonMistakes.md:1,3,60`.

Report: .ufo/waves/round-56/build/ScribeMistake.md
