# R75Attack25 — Facet 25

Axes: factual calibration (does the cited evidence support the candidate finding), actionability (does the control test a concrete claim rather than prescribe process).

## Verdict
The general distinction survives; the report does not establish a concrete r75 defect. Its strongest wording is explicitly a risk/candidate, not a finding that a current r75 claim is false. The proposed claim-to-source workflow is sound but generic and untested against an identified r75 headline, description, or counter. Treat as a useful audit control, not as a demonstrated in-scope defect.

## Evidence
Measured lane revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe`. Independently reopened `corpus/lessons/round-74-verifier-spotcheck.md:58-64`: line 58 reports a separately performed page-fidelity judgment (rule groups 5/5 per page, table rows 3/3, no overreach/unsupported claim); lines 60-64 label counter behavior and self-test evidence-verified, explicitly distinguishing those measurements from the fidelity judgment. This supports Facet25's central warning that a counter/row coverage result alone cannot prove source fidelity. It also shows the historical spotcheck itself did not make that conflation.

`corpus/QUALITY.md:36-37` (Q25/Q26) substantively requires mutant-sensitive content guards and bounds headlines to what the counter or falsification-sensitive guard measures; `:34` Q23 requires authority quotes and a sweep. These criteria support the proposed controls rather than falsify them. The cited round-70 precedent at `corpus/knowledge/skill-eval-artefacts-round70.md:76-82` is explicitly bounded and distinguishes native client execution from an opt-in plugin; it illustrates calibration, but is not evidence about an r75 candidate.

The report itself disclaims auditing the candidate descriptions or source pages (`R75Facet25.md:16-17`). Round-75 lesson `corpus/lessons/round-75.md:5` likewise says description-evaluation guidance is only a scoped-advice candidate, no controlled experiment has been run, and the non-author spot-check is pending. Consequently, no exact r75 phrase/source mismatch is demonstrated here. Nor does the report name a command/control to run: its “control” is a proposed review protocol, so there is no safe execution result to report. Q25's falsification arm is a legitimate acceptance test if a concrete content guard is proposed; merely making a claim-to-source table would not itself satisfy it.

## Residual risk / verification gaps
No live fetch, source-page re-audit, or counter mutation was performed. This is appropriate to the report's own stated limits, but leaves its risk hypothetical. A follow-up assertion requires a specific r75 clause, pinned source evidence, and its actual guard/mutant behavior; absent that, do not elevate this candidate into a verified defect. No lane changes made.

Report trailer: Facet 25; measured tip `65a5c7a663249e0522cc49e4a148424200d9ddfe`; evidence from committed bytes cited above; no live fetch or source edit.