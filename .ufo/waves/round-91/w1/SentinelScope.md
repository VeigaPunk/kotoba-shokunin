# SentinelScope scoped findings (r91-w1)

Candidate `d3f5e1920c315d2ec49faade5b9e6cf6b0f4172a` = `9af1a7af2adf0ab07cfd53f92affc1ed8d992262` + ExecBatteryArms, ExecFloorsCap, ExecLadder (REPAIRABLE), ScribeCorpus patches. Full verdicts: `.ufo/waves/round-91/w1/SentinelScope/sentinel.md`.

Results: checks 2, 3, 4, 5, 6 PASS. Check 1 passes at file level.

FINDINGS
- F1 (scope, needs L1 decision): `verifiers/floors-registry.json` also bumps `freeze_gate` 30→31. The touch list and ExecFloorsCap ownership name `floors_guard` only. Amend before scoring or revert that one line.
- F2 (plan arithmetic): frozen plan expects SOURCES census 187→189; the item's three appended rows (S262, S263, one rejection) give 190, which the candidate measures. Record, do not edit the plan.

RESIDUALS (L1 integration): `corpus/README.md` index rows, `LOG.md`, `SCORECARD.md`, `PROVINCE.md` are touch-list items no builder owns.
