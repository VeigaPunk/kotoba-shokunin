# F30CheckStale — stale/duplicate assimilation falsification (r77 w2)

Axes inspected: consistency (duplicate/stale claims), calibration (counter result), freshness (landed revision), operability (reproducible commands).

## Evidence and result

Lane HEAD observed with `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD`: `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (the frozen base named by the r77 dispatch). The w1 assimilation report `.ufo/waves/round-77/w1/S04Assimilation.md` is present as an untracked wave artifact; it is not a claim-data commit. At HEAD the expected C1 entry `corpus/knowledge/description-craft-round76.md` and lesson `corpus/lessons/round-76.md` are absent (confirmed by the failed gate below and lane directory listing). Thus the round-77 claim data is not landed; no landed assimilation assertion can be accepted as verified.

Ran exact frozen counters against HEAD:

`python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_desc_craft.py --rev HEAD` — exit 1; output includes `description craft backed 0 of 6` and conjuncts (a)–(f) all fail, specifically missing committed lesson and entry, Body craft row, S213 used-by update, and provenance.

`python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py --rev HEAD` — exit 1; output `r75 routed repairs closed 0 of 4`; R1–R4 open, including missing r76 lesson/receipts/registry note and absent LOG corrections.

The relevant existing lane evidence does support the *historical* duplicate concern: `corpus/SOURCES.md:153` identifies S213 as the optimizing-descriptions page; `corpus/lessons/round-75.md:148` says S213 is opened in r75; `corpus/lessons/round-76-verifier-spotcheck.md` is indexed but the expected r76 round lesson is absent. W1's S04 report alleges S231 duplicate of S213 and staged-id collisions, but those are report assertions, not verified landed assimilation at this HEAD. Proposal #3 is named in plans/round-77.md:11 as the mined motivation, while assimilation remains explicitly none; there is no new assimilation data to verify.

## Scope and repair

No mutation or no-harm battery was run: the assignment requires testing landed r77 changes, but no claim-data changes are committed at this revision, and this leaf item is specifically the stale/duplicate assimilation check. Minimal repair is to land only the frozen data already required by the plan (after the L1 freeze/controls order), without assimilating staged duplicate rows or widening the claims; then re-run C1/C2 and all round no-harm checks. This is a sequencing/blocker, not evidence of a counter defect. No axis harm is established; any additional assimilation or renumbering would introduce an unfrozen scope/consistency risk.

No installs. No scratch clone or writes outside this report. Lane index/jj untouched.

VERDICT: BLOCKED — r77 claim data is not committed at HEAD 6523aced; both frozen counters remain red (C1 0/6, C2 0/4), so stale/duplicate assimilation is not verifiable as a landed change.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F30CheckStale.md