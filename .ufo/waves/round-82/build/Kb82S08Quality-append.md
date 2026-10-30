# Append-only integration candidate — not admitted or applied

Base: 47dbe8781657de563ff867caca6244d28e3db504.

Append the lesson class below to the round-82 lesson's Mistakes section, then append the criterion row to corpus/QUALITY.md. Q76 is provisional: L1 must allocate the next unused identifier at integration. Do not rewrite Q09, Q19 or Q65. The new row extends Q65's live-read clause; it does not supersede Q65's other requirements.

## Lesson class candidate: fixture-selftest-live-tree-coupling

Evidence: `.ufo/waves/round-82/receipts/before-checklist-selftest.txt` records `python3 -B verifiers/verify_skill_checklist.py --self-test` against base `47dbe8781657de563ff867caca6244d28e3db504`, exit 1, `1 failure(s) over 1863 assertions`. The failing arm is `governance: live round-65 corrections land, errata-excused`. At that base, `verifiers/verify_skill_checklist.py:2521-2527` derives the real repository from `__file__`, checks its live governance citations, and asserts PASS. Unrelated dead SCORECARD citations therefore fail the fixture self-test. Round-72 M125 already recorded the same live-arm dependency; its remedy refreshed the expected live verdict rather than isolating inputs. Captured-by: Q65 captures the need to re-run after record changes, but no existing QUALITY row requires fixture isolation. Fix requirement: retain correction/erratum semantics in explicit isolated fixtures; keep the public live gate able to reject genuinely dead citations; do not delete the failing coverage or remap its outcome. This is a lesson-backed proposed remedy, not evidence of a landed fix.

| id | criterion | applies to | grounded in | supersedes |
|---|---|---|---|---|
| Q76 (provisional) | A fixture self-test obtains its corpus/governance inputs from explicit isolated fixtures, never the evolving live checkout. Its receipt shows that an unrelated live-governance change leaves the fixture result unchanged, while valid correction passes and missing correction, restored stale target, and unrelated dead fixture subject fail; disabling the corresponding replacement guard makes its regression assertion fail. Public live validation remains separate and must still reject genuinely dead live citations. | fixture self-tests and claims of hermetic self-test repair | M125 reference-drift (`corpus/lessons/round-72.md:77-81`), plus round-82 lesson class `fixture-selftest-live-tree-coupling` proposed above; real red-before `.ufo/waves/round-82/receipts/before-checklist-selftest.txt` | —; extends Q65 |

Admission limit: append the round-82 lesson class before citing it as an existing lesson. The differential, guard-disable and green-after receipts are required integration evidence, not results observed by this scribe.
