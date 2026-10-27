# S03Considerthese — report (round 77, w1)

Task: dispose each proposal in `considerthese/2026-10-26.md`, check for a mineable un-implemented one, table with resolving pointers.
Deliverable: `.ufo/waves/round-77/build/S03Considerthese.table.md` (pointers opened in this seat; line numbers re-checked with grep after writing).
Method: read-only reads of considerthese 10-21…10-26, `plans/round-76.md`, `plans/round-77.md`, r76 lesson draft, r76 spot-check lesson, QUALITY, fleet PROTOCOL/l0-questions; one PyYAML measurement; no installs, no scratch dir, no git writes.

Findings (observed):
1. Of the five 10-26 proposals, none is implemented at HEAD 6523aced. #3 (description-craft page + self-audit) is mined twice (r76 stopped without data; r77 C1 re-lands it). #1 byte ceiling, #2 registry move, #4 provisional-until-falsify, #5 evidence budget are declined.
2. Premises still current at HEAD: SKILL.md 590 lines / 78,647 B (proposal: 78,569 B), 147 lines >120, 77 >300, longest 1,095; description renders 1,022 (1,021 stripped), first sentence 151; Gate registry = SKILL.md:445-513, 24,897 B; `.ufo` 202 MB.
3. Decline reasons: #2 resolves fully (QUALITY.md:83 Q67, fleet l0-questions.md:174, PROTOCOL.md:398,418-421, round-73-addendum-1.md:14-17). #1/#4/#5 reasons resolve only to plans/round-76.md:11 and to a *draft* (`.ufo/waves/round-76/build/lesson-draft.md:89-103`): `corpus/lessons/round-76.md` does not exist at HEAD, so the plan's "recorded in the round-76 lesson Gate" pointer is dead until R76-D2 lands (closure: round-76-verifier-spotcheck.md:26,64,80).
4. Draft defect for r77: lesson-draft.md:99-101 justifies declining #4 with "inside the one wave, so a 'wave 2 pending' state does not arise". True for r76, false for r77 (two v1 waves, plans/round-77.md:50-53). Do not copy the sentence. It also uses the corrected attack taxonomy (22/64, lesson-draft.md:121 M76-6) against plans/round-76.md:64's superseded "34 attack / 53%".
5. C1 only audits the description; it does not rewrite it, and the "omp 99-char cliff" is not on the S213 page (lesson-draft.md:87). The act-on row adds lines/bytes to SKILL.md (draft: +3 lines → 593; skill-patch.md:7), so proposal 1's metric worsens again — disclose, don't fix.

Mineable extra item: none without widening. Proposal 3 is the one allowed item. Only proposal 4 has a zero-cost honest handling: one sentence in the r77 lesson Gate that no SCORECARD row lands before w2 settles (plans/round-77.md:56-57), labelled "practised, not adopted"; no new gate or file. Others (1, 2, 5) need an L0/protocol decision or a new claim. Carry-over items from older files (client×surface grid, reader diff, STATUS.json, cold-routing run) remain open and are listed in the table § C.

Limits: pointers to the draft resolve to uncommitted drafts (r76 build dir is untracked/committed per task statement; I did not check its git status). Proposal-3 "audit-half implemented" language is conditional on C1 landing.

VERDICT: no 10-26 proposal is implemented at HEAD; #3 = C1 is the only allowed item (no widening needed); declines 1/4/5 resolve to a plan + draft only until corpus/lessons/round-76.md lands, and the draft's #4 reason ("one wave") must be reworded for r77.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S03Considerthese.table.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/S03Considerthese.md
