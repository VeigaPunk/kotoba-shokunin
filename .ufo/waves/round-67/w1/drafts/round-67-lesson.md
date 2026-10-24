---
author: kotoba L1 (round 67, hyaku campaign)
date: 2026-10-24
round: 67
lane: kotoba
---

# Round 67 — lesson (kotoba, hyaku campaign)

## Gate

The bounded candidate set is the staged instruction-authority-ladder entry and the sources it
names: S123, S124 and S129 in its `source:` lines, plus S125 inline. The decisions below are
for this round's one ladder entry; they are not a claim that a rejected source has no craft
value elsewhere. The adopted-row draft is `.ufo/waves/round-67/w1/drafts/SOURCES.append.r67.md`.

- **ADMIT S123 — OpenAI Model Spec (2026/08/18).**
  https://model-spec.openai.com/2026-08-18 — opened 2026-10-24. In § *Instructions and
  levels of authority*, the located quote is: “Instructions with higher authority override
  those with lower authority.” The § *The chain of command* list separately names **No
  Authority** for assistant/tool messages and quoted or untrusted content. Admit the row as
  `mined`, scoped to OpenAI's own ladder and override rule, not as evidence that another
  client implements that ladder. It is used by
  `corpus/knowledge/instruction-authority-ladder-round67.md`.
- **ADMIT S124 — Anthropic's pinned skill-creator reference.**
  Canonical source:
  https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md
  — opened 2026-10-24 through the same pinned file's official raw bytes:
  https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md
  At `skills/skill-creator/SKILL.md:335`, under `## Description Optimization`, the located
  quote is: “The description field in SKILL.md frontmatter is the primary mechanism that
  determines whether Claude invokes a skill.” The adjacent procedure at `:337-398` carries
  the trigger-evaluation details. Admit as `mined`, scoped to Anthropic's reference skill and
  not to other clients; used by the same round-67 ladder entry.
- **ADMIT S129 — Many-Tier Instruction Hierarchy in LLM Agents (ManyIH).**
  https://arxiv.org/abs/2604.09443 — opened 2026-10-24 at v4 (last revised 2026-09-04). In
  the abstract, the located quote is: “ManyIH-Bench requires models to navigate up to 12
  levels of conflicting instructions with varying privileges, comprising 853 agentic tasks
  (427 coding and 426 instruction-following).” Admit as `mined`, tier B scoped to the
  abstract's empirical measurement rather than a normative ladder; used by the same round-67
  ladder entry.
- **REJECT S125 as staged for this ladder entry — Qwen Code Agent Skills.**
  https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/ — opened 2026-10-24. The
  staged entry names S125 only inline, without a `source: S125` provenance line, and ends its
  quotation as “prompt text.” The served sentence under *Optional: enforce a rule
  deterministically (`hooks:`)* instead continues: “Everything in a SKILL.md body is an
  instruction to the model: it is prompt text, so following it depends on the model.” Reject
  this staged citation for missing provenance and punctuation-changing quote shaping; do not
  append S125 in this round's three-row ladder set. **Flip condition:** admit S125 when a
  client-scoped prompt-versus-hook entry cites it in a real `source:` line, quotes the complete
  served sentence, and makes that admitted entry the row's only new `used-by` target.

### Recheck transformations

The registry keeps only the cadence. The condition stripped from each staged `recheck` cell is
preserved verbatim here; the parenthesized run date is the staged record, not a new run claim.

- **S123 — adopted cadence `90d`.** Old cell:
  `90d — re-fetch https://model-spec.openai.com/2026-08-18 and confirm the five levels and the override sentence are unchanged (ran 2026-10-23)`.
  New cell: `90d`. Stripped condition:
  `re-fetch https://model-spec.openai.com/2026-08-18 and confirm the five levels and the override sentence are unchanged (ran 2026-10-23)`.
- **S124 — adopted cadence `90d`.** Old cell:
  `90d — re-fetch the pinned tree and confirm the 20-query, 60/40, 3-run, 5-iteration numbers still read the same (ran 2026-10-23)`.
  New cell: `90d`. Stripped condition:
  `re-fetch the pinned tree and confirm the 20-query, 60/40, 3-run, 5-iteration numbers still read the same (ran 2026-10-23)`.
- **S129 — adopted cadence `180d`.** Old cell:
  `180d — re-fetch the arXiv abstract and confirm the 853-task, 12-level and ~40% figures (ran 2026-10-23)`.
  New cell: `180d`. Stripped condition:
  `re-fetch the arXiv abstract and confirm the 853-task, 12-level and ~40% figures (ran 2026-10-23)`.

**Spot-check:** this lane-authored draft claims no independent non-author admit/reject
spot-check. Wave-1 review is not outside review; that check remains for closure.

## Mistakes

- **M104 — class: landing (closure corpus file left unindexed).** Evidence: the hyaku run
  card `/home/vgpnk/Projects/shokunin/.ufo/waves/hyaku/inline-run-20261023.md:181-185`
  routes the r66 closure's unindexed `corpus/lessons/round-66-verifier-spotcheck.md` to r67.
  At the pinned base `2a8eba56b3f9321b70c569fa2816d42237ca49a2`,
  `python3 -B verifiers/verify_corpus_integrity.py` printed `5/9 checks pass`, named that file
  under `unindexed`, and exited 1; `python3 -B verifiers/verify_corpus_independent.py --json`
  also exited 1. The verbatim receipt is `.ufo/waves/round-67/w1/controls/C1-base.txt`.
  **Captured-by:** the two existing corpus-integrity gates did detect the defect, but only
  after closure; round-47 M21 is the same class, and the r66 closure spot-check explicitly
  says it did not execute the lane's gates. **Fix:** add the closure-authored spot-check to
  the coverage map and re-record the baseline from the gate's own measurement. Shown able to
  fail: the base is red as above; the paired half-repair controls in
  `.ufo/waves/round-67/w1/controls/C1-half-controls.txt` leave index-only K2 at `6/9`, exit 1,
  and baseline-only K3 at `8/9`, exit 1. This draft records no unobserved repaired-tip verdict.
- **M105 — class: landing (campaign `recheck` schema mismatch).** Evidence: staged rows
  S123/S124/S129 in `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` append
  conditions to their cadences, while the lane contract permits a date, `NNd`, or symbolic
  cadence. In the paired scratch control recorded in
  `.ufo/waves/round-67/w1/ScribeLesson.md`, the before registry exited 1 with E09 at each of
  those ids; changing only the three `recheck` cells to their bare cadences made the otherwise
  identical after registry exit 0. **Captured-by:**
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate` E09 and the frozen SOURCES
  grammar. **Fix:** retain `90d`, `90d`, and `180d` in the adopted rows and move the stripped
  conditions into this Gate. Shown able to fail by that paired before/after control; the
  scratch knowledge files were existence fixtures only, not C2 content evidence.

## Status changes

No pre-existing lane registry row changed. For the adopted staged rows, `status` remains
`mined`; `opened` changes from the staged `2026-10-23` to the re-opened `2026-10-24` for
S123/S124/S129. Their `used-by` transformations are:

- S123: `corpus/knowledge/instruction-authority-ladder.md` →
  `corpus/knowledge/instruction-authority-ladder-round67.md`.
- S124: `corpus/knowledge/instruction-authority-ladder.md, corpus/knowledge/description-writing-and-trigger-testing.md`
  → `corpus/knowledge/instruction-authority-ladder-round67.md` only; the description-writing
  entry was not admitted in this round.
- S129: `corpus/knowledge/instruction-authority-ladder.md` →
  `corpus/knowledge/instruction-authority-ladder-round67.md`.

The `recheck` old → new values and their stripped conditions are recorded in § Gate. S125 was
not appended, so it has no adopted status, recheck, or used-by state.

## Evidence pins

- The frozen claims and repair bounds are in `plans/round-67.md`.
- C1 red-before and half-repair controls are under `.ufo/waves/round-67/w1/controls/`; they
  are not after receipts.
- Source URLs, access evidence, content hashes, and the paired campaign-schema control are
  recorded in `.ufo/waves/round-67/w1/ScribeLesson.md`.
- The coverage-index and source-row artifacts cited here are wave drafts, not evidence of
  production integration.
