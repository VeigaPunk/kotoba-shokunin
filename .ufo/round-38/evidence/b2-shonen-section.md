# Round-38 report § SHONEN — paste-ready draft (seat B2|scribe-shonen)

> Measured at dispatch HEAD `cb4e0f3`, 2026-10-19 (this wave). One line per box, mark + pointer,
> **no `[x]`**: no named non-author verifier exists this round (PROTOCOL.md:63-68 — "a subagent
> the lane dispatched is still the lane"; every check below is lane-run, `SHONEN.md:44-50`).
> The marks in `SHONEN.md` itself stay `[~]`; this section is the round's assessment, not a mark edit.
> Replace B1's placeholder § SHONEN with the block between the rulers; keep the note line after it.
> **Re-run before pasting** if C1/C2/C3 land: builder edits to `verifiers/verify_skill_checklist.py`
> (C3 container fences), `verifiers/check_assertion_floors.py` (C2 residuals) and the C1 registry
> registration all change the counts below, and the floors move in-step. Values here are dispatch-HEAD
> bytes; `verifiers/check_assertion_floors.py` was already dirty (` M`, +47/-6, another seat's C2 work)
> when the box commands were re-run — the floors line was therefore also re-run from `git show HEAD`
> bytes (`drafts/b2/at-head/`), where it reads the same 6 × PASS.

---

## SHONEN

- [~] box 1 (decision tables / error patterns / checklists / cited sources, `SHONEN.md:5`) —
  pointers re-measured this round: `git show HEAD:SKILL.md | awk '/^## /…'` → `15; 9; 9; 8; total: 41`
  boxes over four checklists (`SKILL.md:177/252/298/329`); § Decision tables :151; § Sources :367 = 38
  bullets, `PASS trigger.citation_resolves: evaluated 38 — 38 repo-rooted citation token(s) resolve`;
  anti-pattern home `corpus/knowledge/fail-closed-and-anti-patterns.md` = 22 pipe rows / 20 data rows
  (`SKILL.md:349` "Twenty rows"). Still true; stale-count defect carried (see report § Defects:
  `corpus/README.md:11` "18-row").
- [~] box 2 (end-to-end task executed and logged, `SHONEN.md:16`) —
  `python3 verifiers/verify_harness_claims.py` → `28/28 checks pass`, exit 0 (re-run this wave);
  LOG.md round-5 / round-7 / round-10 / round-11 arcs; artifacts present:
  `corpus/knowledge/harness-verifier-round10.md`, `corpus/knowledge/cold-run-round11.md`. Still true;
  the newest non-author cold run on record remains the round-11 one — nothing this round restores `[x]`.
- [~] box 3 (instructions executable without oral context, `SHONEN.md:22`) —
  `python3 verifiers/verify_skill_checklist.py` → **exit 1: 9 × PASS, 1 × FAIL**
  (`governance.citation_resolves evaluated 293` names `SCORECARD.md:131-133`, the r37 brace-glob scout
  lists — a **carried red landed by r37**, see report § C0); `--self-test` → `0 failure(s) over 1584
  assertions` exit 0; `python3 verifiers/check_assertion_floors.py` → 6 × PASS `floor == observed`
  (`10 / 119 / 59 / 87 / 1584 / 62`) exit 0; `verifiers/fixtures/checklist` = 71 dirs.
  The box's own pointers hold, but the live gate that carries them is red at this HEAD — not smoothed.
- [~] box 4 (no cross-domain bleed; `PROVINCE.md` accurate, `SHONEN.md:41`) —
  `git log -1 --format="%h %ad %s" --date=short -- PROVINCE.md` → `43e0c02 2026-09-28 seed: kotoba shonen`
  (unchanged since seed); LOG.md:96 and :481 record the round-7 cross-domain audit as routed-not-fixed;
  this wave wrote only inside the lane repo (`.ufo/round-38/`).

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
- The 11 SHONEN canonical-form findings on this file (fleet gate `shonen` rule, re-measured this wave as
  `CR-kotoba-shokunin-shonen-1..11`: `-1..-3` = `:5`/`:16`/`:22` carry 10/5/18 indented evidence lines vs
  the one-line canonical form; `-4..-11` = `:43`-`:50` are blank/prose lines that are neither header, box
  nor evidence line) are independent of marks — they do not block `[~]`, but they must be named in the
  report, not smoothed.
