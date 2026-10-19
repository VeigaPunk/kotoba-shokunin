# Round-37 report § SHONEN — paste-ready draft (seat B2|scribe-shonen)

> Measured at HEAD `041f6ba`, 2026-10-19 (this wave). One line per box, mark + pointer,
> **no `[x]`**: no named non-author verifier exists this round (PROTOCOL.md:63-68 — "a
> subagent the lane dispatched is still the lane"; every check below is lane-run,
> `SHONEN.md:44-50`). The marks in `SHONEN.md` itself stay `[~]`; this section is the
> round's assessment, not a mark edit. Replace B1's placeholder § SHONEN with the block
> between the rulers; keep the note line after it.
> **Re-run before pasting** if C2/C3 land: builder edits to `verifiers/verify_skill_checklist.py`
> and `verifiers/check_assertion_floors.py` change the box-3 counts and the floors in-step
> (the counts below are the clean-HEAD values ~13:03Z; the tree carried uncommitted edits by 13:06Z).

---

## SHONEN

- [~] box 1 (decision tables / error patterns / checklists / cited sources, `SHONEN.md:5`) —
  pointers re-measured this round: `git show HEAD:SKILL.md | awk '/^## /…'` → `15; 9; 9; 8; total: 41` boxes
  over four checklists (SKILL.md :177/:252/:298/:329); § Decision tables :151; § Sources :367 = 38 bullets,
  `PASS trigger.citation_resolves: evaluated 38 — 38 repo-rooted citation token(s) resolve`;
  anti-pattern home `corpus/knowledge/fail-closed-and-anti-patterns.md` = 22 pipe rows / 20 data rows
  (`SKILL.md:349-353` "Twenty rows"). Still true; stale-count defect carried (see report § Defects: `corpus/README.md:11` "18-row").
- [~] box 2 (end-to-end task executed and logged, `SHONEN.md:16`) —
  `python3 verifiers/verify_harness_claims.py` → `28/28 checks pass`, exit 0 (live this round);
  LOG.md round-5 / round-7 / round-10 / round-11 arcs; artifacts present:
  `corpus/knowledge/harness-verifier-round10.md`, `corpus/knowledge/cold-run-round11.md`. Still true;
  the newest non-author cold run on record remains the round-11 one — nothing this round restores `[x]`.
- [~] box 3 (instructions executable without oral context, `SHONEN.md:22`) —
  `python3 verifiers/verify_skill_checklist.py` → 10 × PASS exit 0 (`line_budget evaluated 521 within budget 600`,
  `box_map evaluated 41 — 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)`);
  `--self-test` → `0 failure(s) over 1504 assertions` over 71 fixture dirs (`verifiers/fixtures/checklist` = 71).
  The box's embedded round-16 snapshot (67 cases / 1283 assertions) is superseded by the round-32 recount,
  which matches live (71 / 1504).
- [~] box 4 (no cross-domain bleed; `PROVINCE.md` accurate, `SHONEN.md:41`) —
  `git log -1 --format="%h %ad %s" --date=short -- PROVINCE.md` → `43e0c02 2026-09-28 seed: kotoba shonen`
  (unchanged since seed); LOG.md:135-137 records the round-7 cross-domain audit as routed-not-fixed;
  this wave wrote only inside the lane repo (`.ufo/round-37/`).

No `[x]` this round: no external verifier is named; the machine form corroborates — the fleet gate
`checkShonen` refuses `[x]` without a `<verifier-id>` token (`#no-verifier-id` rule) and the file carries none.

---

Note line (keep after the block):

Verifier note: all four boxes were last actually checked by the aggregator lane's round-8 cold run
(`corpus/lessons/round-8-aggregator-box3-coldrun.md`); the [x]-readiness pack for an outside verifier is
scout C2's round-25 dossier (`.ufo/round-25/scouts/C2.md`). No `[x]` is justified at this HEAD.

## Preconditions for a non-author to flip a box (do not paste; integrator reference)

- Box 1–3 flip only after the outside verifier runs the box-specific checks in `.ufo/round-25/scouts/C2.md`
  § Findings 1-3 on a frozen SHA and commits a dossier under `corpus/lessons/`; a kotoba-dispatched seat's
  output cannot.
- Box 4 flips only after a per-commit changed-path audit vs `PROVINCE.md` (C2 § Findings 4).
- The 11 SHONEN canonical-form findings on this file (see report § Defects — 3 × `#evidence-count`, 8 × `#other-line`)
  are independent of marks — they do not block `[~]`, but they must be named in the report, not smoothed.