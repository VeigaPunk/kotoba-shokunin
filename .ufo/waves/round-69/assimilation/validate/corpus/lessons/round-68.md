---
author: kotoba L1 (round 68, hyaku run 5)
date: 2026-10-24
round: 68
lane: kotoba
---

# Round 68 — lesson (kotoba, hyaku run 5)

## Gate

The round assimilated from the read-only campaign package
`/home/vgpnk/Projects/shokuknow/merge/kotoba/` on **one theme**: **client trust gates** — what a
client documents about an UNTRUSTED skill body. Nothing in that tree was written, committed or
executed; only its bytes were read.

**Admit (5 source rows, 1 knowledge entry).** Every cited source was re-opened by this round —
the campaign's own `opened` date and quote prove nothing about this lane (CORPUS.md rule 1). The
access date below is **this round's** date, not the campaign's.

- **S198 — VT Code, `SKILLS_GUIDE.md`**, https://raw.githubusercontent.com/vinhnx/vtcode/main/docs/skills/SKILLS_GUIDE.md
  — opened 2026-10-24 by the L1 (`ScoutVtcode` seat, log
  `.ufo/waves/round-68/w1/logs/ScoutVtcode.log`). Located under `## Activation Context`; the
  located quote is: "Skill content is untrusted resource data; host tool and sandbox policy remains
  authoritative." (13 words). The same section records that an activated skill renders as a
  bounded `<untrusted_skill_instructions>` block.
- **S199 — Parallel Works, pw code skills**, https://parallelworks.com/docs/ai/code/skills —
  opened 2026-10-24 by the L1 (`ScoutParallel` seat). Located under `## Trust`; the located quote
  is: "Project skills are repository-controlled instructions, so they clear two independent gates."
  (12 words). The same section states the second gate and its bound: "Model invocation can never
  grant either gate." (7 words).
- **S200 — Kilo Code, Skills**, https://kilo.ai/docs/customize/skills — opened 2026-10-24 by the
  L1 (`ScoutKilo` seat). Located under `## Shell commands in skills`; the located quote is:
  "Project skills (.kilo/skills/ in a repository) and skills fetched from remote URLs never execute
  commands" (16 words). The same section names the approval prompt that precedes a trusted
  skill's commands.
- **S201 — Microsoft Agent Framework, Agent Skills**,
  https://learn.microsoft.com/en-us/agent-framework/agents/skills — opened 2026-10-24 by the L1
  (`ScoutMsAgentFramework` seat). Located under `## Security best practices`; the located quote is:
  "Agent Skills should be treated like any third-party code you bring into your project."
  (13 words). The same page states that the three skill tools "require approval by default".
- **S202 — Mistral AI Vibe, README**,
  https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md — opened 2026-10-24 by the
  L1 (`ScoutMistral` seat). Located under `### Skill Discovery`; the located quote is: "Standard
  Agent Skills path (project root, trusted folders only)" (9 words).

**Reject (2 staged claims, kept as refusals with a flip condition).**

- **Refused — the staged S198 anchor.** The staged row anchors the quote in "the Discovery section
  listing the four search roots, and the Prompting Behavior paragraph". The four-root list is
  real, but the untrusted-content sentence is **not** in that paragraph: the page places it in
  `## Activation Context`. The row was admitted with the anchor **re-pointed by document** (the
  URL is the evidence; the anchor follows the text, not the staged cell). Flip: if a later fetch
  shows the sentence in the "Prompting Behavior" paragraph, the anchor may be restored.
- **Refused — the staged S201 quote "All three skill tools require approval by default".** The
  page states the rule as a tool list — "load_skill, read_skill_resource, run_skill_script require
  approval by default" — not with the staged words "All three skill tools". The staged wording is
  a paraphrase, so it is not admitted as a located quote; the row was admitted with the verbatim
  sentence this round located. Flip: a fetch that renders the literal phrase "All three skill
  tools require approval by default" would clear it.

**Not adopted.** The package's other 169 staged rows and 81 entries — out of theme, neither
screened nor admitted. One staged entry was refused on scope grounds for the record:
`aaf-governance-and-the-standard-s-move.md` (the standard's foundation and governance move) is
organisational metadata, not prompt-and-skill craft, and is outside this lane's province
(PROVINCE.md § Core). Flip: if a later round shows the move changes what a skill body may assert
in a client's rules, it can be re-screened.

**Id collision (checked in scratch, before the first append).** 123 registry ids, 174 staged ids,
**0 collisions** (`.ufo/waves/round-68/assimilation/collisions`). The guard was proved
non-vacuous on a scratch fixture: a registry row with two leading spaces is caught by the
census parser's 0–3-space pattern (2 hits) and missed by a column-zero-only pattern (1 hit). The
adopted ids continue the lane's registry as staged (S198–S202); no renumbering was needed and no
citation was re-pointed by arithmetic.

**Scratch transformation and validation, before the first append.** The append block was built in
scratch from the rows the admitted entry cites, normalized to the lane's 11-column schema (the
`recheck` cell reduced to a bare `90d`, no literal or escaped `|` in any cell, `used-by` exactly
`corpus/knowledge/client-trust-gates-round68.md`, `status mined`, `opened 2026-10-24`), and
mirrored over a copy of the lane's `corpus/` plus `SKILL.md`:
`scripts/sources-census.sh validate --file .ufo/waves/round-68/assimilation/validate/corpus/SOURCES.md`
→ **exit 0** (`file ok`, warnings only). The first two scratch attempts failed and were fixed in
scratch, never in the registry: an append at end-of-file drew `E12 row outside Registry section`
(the rows belong inside the `## Registry` table, before `## Paths`), and a mirror without
`SKILL.md` drew `E11 missing used-by SKILL.md`.

**Stripped `recheck` prose** (from the staged rows, kept here per the contract):

- S198 — "re-fetch the raw file and confirm the four-root list and the untrusted-resource-data sentence are unchanged (ran 2026-10-24)"
- S199 — "re-fetch the page and confirm the two-gate description and the `/skills trust <name>` command are unchanged (ran 2026-10-24)"
- S200 — "re-fetch the page and confirm the trusted-skills-only rule and the approval-prompt wording are unchanged (ran 2026-10-24)"
- S201 — "re-fetch the English page and confirm the approval-by-default sentence and the untrusted-input instruction are unchanged (ran 2026-10-24)"
- S202 — "re-fetch the raw README and confirm the discovery list and the trusted-folders-only annotation are unchanged (ran 2026-10-24)"

**Quarantine — the campaign's absent-defect register, this lane's slice.** Derived in scratch
(`awk` over the register's data rows: the lane cell, a round cell and an id cell): **13 rows** —
7 `payload-absent` and 6 `unreachable`. Verdict per row:

| id | class | cited source | verdict |
|---|---|---|---|
| S151 | payload-absent | agentskills.io/skill-creation/optimizing-descriptions.md | refused — the quoted span is not on the page this round fetched; fabrication class, not appendable |
| S167 | payload-absent | agentskills.io/client-implementation/adding-skills-support.md | refused — the quoted span is a campaign note about the lane's own S002, not a source quotation; nothing appendable |
| S168 | payload-absent | vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | refused — the quoted span was not located on the page this round fetched |
| S172 | payload-absent | junie.jetbrains.com/docs/agent-skills.html | refused — the quoted span was not located on the page this round fetched |
| S176 | payload-absent | agentskills.io/client-implementation/adding-skills-support.md | refused — the quoted span was not located on the page this round fetched |
| S180 | payload-absent | web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja | refused — the quoted span was not located on the page this round fetched |
| S185 | payload-absent | docs.roocode.com/features/skills | refused — the quoted span was not located on the page this round fetched |
| S169 | unreachable | ai.google.dev/gemini-api/docs/coding-agents | unverifiable — the register never checked the quote; unreachable is not fabrication |
| S236 | unreachable | skills.sh/docs | unverifiable — same class |
| S237 | unreachable | skills.sh/audits | unverifiable — same class |
| S238 | unreachable | code.claude.com/docs/en/security.md | unverifiable — same class |
| S239 | unreachable | skills.sh/agent | unverifiable — same class |
| S243 | unreachable | skills.sh/docs/api | unverifiable — same class |

Nothing from the register was adopted this round: every `payload-absent` row failed the
hand-check, and an `unreachable` row is unverifiable rather than refused. Flip condition for a
`payload-absent` row: the quoted span is located verbatim on a re-fetch of the cited source (the
row may then be admitted with the anchor this round located). Flip condition for an
`unreachable` row: the source becomes fetchable and the quote is then checked — an unreachable
row is never a fabrication claim.

**considerthese.** One still-unimplemented proposal mined from the operator-authored
`considerthese/2026-10-24.md` (never edited): the skill-description audit against the committed
per-client threshold table. Grounded through the lane's own bar — the reflection is a pointer,
not evidence — by measuring the lane's own `SKILL.md` frontmatter `description` against the
1024-character cap documented in `corpus/knowledge/skill-listing-thresholds-round54.md`: the
value is 1,019 characters stripped and 1,020 parsed, i.e. 4–5 characters of headroom against the
cap the table documents for VS Code, Copilot CLI and opencode. No documented per-entry cut fires
at that length. The measurement is the evidence; the proposal stays open.

## Mistakes

- **M107 — class: an unobserved line asserted as observed.** Evidence: the round-67 report's
  *Before → after measurements* section states that the r67 C2 base "prints `authority ladder
  grounded 0 of 1`, **exit nonzero**", and the r67 `LOG.md`/`SCORECARD.md` entries repeat it.
  Re-running the counter at the r67 base revision `2a8eba56b3f9321b70c569fa2816d42237ca49a2`
  prints on stderr `environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md at 2a8eba56b3f9321b70c569fa2816d42237ca49a2` and exits **2** — stdout carries nothing. The lane's own committed receipt
  (`.ufo/waves/round-67/receipts/C2-authority-measure.txt`) records that exit-2 line, so the
  report contradicted the lane's own evidence. Captured by: the round-67 plan's kill rule ("if the
  base control does not print `0 of 1`, C2 is a miss as declared") — the rule was declared and
  the data disagreed, but nothing forced the *report* to be checked against the receipt before it
  was written. **Fix (shown able to fail):** the r67 report is append-only and is never
  rewritten; round 68 appends the correction to `LOG.md`, `SCORECARD.md` and this lesson, and the
  round-68 counter `verifiers/check_client_trust_gates.py` is built with the corrected
  classification from the start — a missing entry is a content verdict (`0 of 5`, exit 1), not an
  environment error (exit 2) — and its self-test pins that classification as an assertion, so a
  future counter that re-introduces the r67 classification fails its own self-test.
- **M108 — class: a path cited that does not exist.** Evidence: the round-67 report cites the
  census receipt `.ufo/waves/round-67/w1/controls/census-validate-append.txt`; the file that
  exists is `.ufo/waves/round-67/controls/census-validate-append.txt` (the `w1/` segment was
  added). Captured by: the round-67 plan's evidence-pointer rule (every pointer is a path that
  must resolve). **Fix:** the correction is appended here and in the r68 report; the r67 report
  is not edited.
- **M109 — class: an untracked working-tree artefact left undisclosed.** Evidence:
  `.ufo/waves/round-67/w1/controls/junk-world/` — a 254 MB junk-world control mirror, untracked,
  and named nowhere in the r67 report, `LOG.md` or lesson although the r67 lesson asserted that
  `git status --porcelain` "lists nothing after it". Captured by: the round prompt's inherited-state
  rule and the r67 lesson's own sentence. **Fix:** round 68 discloses it (here and in the r68
  report) and removes it from the working tree; it was control scratch, never claim evidence.
- **M110 — class: a closure artefact left unindexed.** Evidence:
  `corpus/lessons/round-67-verifier-spotcheck.md` was written by the hyaku closure and never
  indexed, so `verify_corpus_integrity.py` read `6/9 checks pass`, exit 1, with
  `unindexed: corpus/lessons/round-67-verifier-spotcheck.md`, and the independent gate exited 1.
  Captured by: the corpus coverage-map contract (every corpus file carries a coverage-map row)
  — the same class the round-67 repair closed for the r66 spot-check. **Fix:** one coverage-map
  index row plus a baseline re-record derived from the gate's own measurement; the two halves
  are separately red (the index row alone and the re-record alone each leave the gate red).

## Status changes

- S198, S199, S200, S201, S202 — `mined` at landing (2026-10-24), tier B, kind `docs`, recheck
  `90d`, `used-by corpus/knowledge/client-trust-gates-round68.md`.
- No prior row's `status`, `recheck` or `used-by` was changed: `corpus/SOURCES.md` gained five
  rows and lost none.
