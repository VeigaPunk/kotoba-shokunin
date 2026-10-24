# Lessons — round 47

Round: 47 (hyaku campaign, first hyaku round for this lane; claim `kotoba=47` attempt 1,
BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`). Claims: C1 freshness (re-derive and
re-pin omp 18.12.5 / opencode 1.19.3), C2 operability (`trigger.no_xml_tag`, this file's
own description loses `<skills>`), C3 calibration (pinned governance erratum for
`LOG.md:2111`; the round-46 spot-check file indexed). Plan: `plans/round-47.md`. Wave
evidence: `.ufo/waves/round-47/` (build reports under `build/`, before-run under
`before/`). The first coordinator died with the host session; the replacement integrated
the surviving wave-1 reports — the LOG.md round-47 entry names inherited and dead seats.

## Mistakes

`captured-by` names the criterion or instrument that should have caught the class;
`none → Qnn` means nothing caught it and this round adds the criterion.

| class | evidence pointer (command → output) | captured-by | fix |
|---|---|---|---|
| M20 Stale planned premise (before-values copied, not re-measured) | `git show c61a973:SCORECARD.md \| grep -c 'installed omp 18.12.3'` → 1 (the round-47 plan row); the figures "surfaces 5/7, pins 1/3" are the round-44 pre-repin before-column, copied verbatim (`.ufo/waves/round-47/build/MistakeStalePremise.md`); at BASE `omp --version` → `omp/18.12.5` and `.ufo/waves/round-47/before/SUMMARY.md` → surfaces exit 2, pins exit 2 DRIFT 3/3; `corpus/lessons/round-46.md` itself recorded `DRIFT 2/3` | none → Q19 (Q09 covers a rebuild, not a copied premise) | Q19: a planned before-value is re-measured at round start and recorded with its command and commit, or struck. Shown able to fail: the prototype premise check in `.ufo/waves/round-47/build/MistakeStalePremise.premise-check.txt` fails on all three stale copies (`SCORECARD.md`, `corpus/README.md`, `PROVINCE.md`) and passes a fresh control. |
| M21 Corpus file landed without its index row (closure commit) | `git show --stat c61a973` → adds `corpus/lessons/round-46-verifier-spotcheck.md` only; at `c61a973` `python3 -B verifiers/verify_corpus_integrity.py --json` → exit 1 (`tracked_files` 59≠58, `unindexed` 1) and at parent `04192c2` → exit 0 (`.ufo/waves/round-47/build/MistakeUnindexedLanding.md`) | `verifiers/verify_corpus_integrity.py` + `verifiers/verify_corpus_independent.py` (they caught it, but only at the next round's start: no closure-time run) | Indexed this round (`corpus/README.md` row) with the baseline re-recorded; the closure-time run belongs to the integrator writing the file — routed in the round report, not fixable from this lane. |
| M22 A lesson's own evidence pointers stale at landing | `corpus/lessons/round-46.md` M2 cites `SCORECARD.md:80` for "complete-census condition is UNMET", but `grep -n 'complete-census condition is UNMET' SCORECARD.md` → line 76 at `78ee57e` and at BASE (wrong at birth); M5 cites `SCORECARD.md:165`/`:100`, which rotted +8 lines at `f2f9ee1`; M13 cites `SKILL.md:15`, the token sat on `:14` (`.ufo/waves/round-47/build/MistakeSweepOthers.md` N1–N3) | none (`governance.citation_resolves` resolves path tokens in LOG/SCORECARD only, never `file:line` content) | Not fixed by an instrument this round. The round-46 lesson stays append-only; this row is its erratum. This lesson cites anchor text with its `grep -n` command instead of bare line numbers wherever a line can move. |

Sweep that found no further class in this round's own work: every pointer above was re-run
at BASE by the wave-1 scribes (`MistakeStalePremise.md`, `MistakeUnindexedLanding.md`,
`MistakeSweepOthers.md`, all under `.ufo/waves/round-47/build/`).

## Gate

**Rows written this round (each opened this round by a wave-1 seat; the seat report holds
the full fetch record).** All four rows are new; no existing row's `status`, `recheck` or
`used-by` changed (old→new: none).

| row | URL | accessed | ≤25-word quote (location) | record |
|---|---|---|---|---|
| S012 | https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator | 2026-10-21T15:55:51Z | "Description cannot contain angle brackets (< or >)" (`skills/skill-creator/scripts/quick_validate.py:81`, sha256 `67cf5703…`) | `.ufo/waves/round-47/build/SrcNewSkillCreator.md` |
| S013 | https://learn.chatgpt.com/docs/build-skills (308 from https://developers.openai.com/codex/skills) | 2026-10-21T15:54:43Z | "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown" (§ How ChatGPT and Codex use skills) | `.ufo/waves/round-47/build/SrcNewCodexSkills.md` |
| S014 | https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills | 2026-10-21T15:57:06Z | "At startup, the agent pre-loads the name and description of every installed skill into its system prompt." (§ The anatomy of a skill) | `.ufo/waves/round-47/build/SrcNewAnthropicEng.md` |
| S015 | own work — `sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` | 2026-10-21 (exit 0, 4/4 OK) | `bin/omp-18.12.5` `fdbc8136…`, `bin/opencode-1.19.3` `179ca421…` (SHA256SUMS lines) | `.ufo/waves/round-47/build/SrcOwnWorkSubstrate.md` |

**Sourced claim:** C2 rests on S003 (re-opened this round, `.md` byte-identical to the
round-46 fetch, sha256 `727f3fa1…`; quote "Cannot contain XML tags", `best-practices.md`
§ Skill structure — `.ufo/waves/round-47/build/SrcS003.md`) and on S012, which the check's
detail line and `SKILL.md` § Portability floor cite as the stricter vendor packager rule.
C1 rests on S015 (the pinned bytes are the snapshot bytes).

**Existing rows re-opened (no status change):** S001 content still holds, but its anchor
label "§ Skill metadata table" names no heading on the live page (`SrcS001.md`); contract
rule 2 forbids an in-place anchor edit, so the defect is recorded here and a superseding
row waits for the next round that cites S001. S002, S003, S004, S005, S008 still hold
(`SrcS002.md` … `SrcS008.md`). S006, S007 not re-opened.

**Rejected candidate (not a row):** `anthropics/skills` `spec/agent-skills-spec.md` — 3
lines, a pointer to agentskills.io, no rule content (`SrcNewSkillCreator.md`); S001 already
carries the normative spec.

**C1 class ledger:** `corpus/knowledge/instruction-surface-census-round13.md`
§ Superseded class rows and the round-47 opencode ledger — every opencode id the census
ever declared, with its verdict and the dump count that decides it.

## Falsify wave (wave 2, post-crash, lane-dispatched — not a non-author spot-check)

77 seats attacked landing `7ad7fad` (reports `.ufo/waves/round-47/falsify/`). Every
counting command reproduced; the defects below were found in the landing's own records.

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| M23 Landing record quotes a count measured on a different tree | LOG.md round-47 landing entry says "governance evaluated 804"; at `7ad7fad` `python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves` → PASS evaluated 848 (804 = the BASE-prefix count from `.ufo/waves/round-47/build/C3CriticDesign.md`; the landing's own 44 new citations moved it) — `W2ErrataRerun.md`; same class: `SKILL.md` "10 checks" after an 11th check landed (`W2CheckIdsContract.md`), a SCORECARD pointer to a landing-pin entry not yet written (`W2MistakeSweep.md`) | none (gates resolve paths, not counts) | Counts in a landing record are copied from the after-battery receipts of the landed tree (`.ufo/waves/round-47/after/`), never from a build-wave report; corrected in the round-47 landing-pin LOG entry, `SKILL.md`, `SCORECARD.md`. |

Gate corrections from the wave: the C2 check's detail line names S003 only — S012 is
cited by `SKILL.md` § Portability floor, not by the verifier (`W2LessonGate.md`); S015's
`used-by` file now cites S015 (census round-47 falsify errata); S003's teaches cell
calls the 500-line body rule "Anthropic-only" although the open spec also states it
(`SrcS003.md` D2) and S010's teaches cell is stale since `trigger.no_xml_tag` landed —
both need superseding rows (contract rule 2), carried to round 48. `SKILL.md` is 528
lines against S001/S003's 500-line guidance; its own 600-line box is the disclosed
deviation.
