# Lessons — round 49

Round: 49 (hyaku campaign, attempt 1). Lane base `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`. Claims:
C1 adjacency — the fleet sibling-overlap census `corpus/knowledge/sibling-overlap-census-round49.md`
and the `PROVINCE.md` § Adjacent table joined to it by `verifiers/check_sibling_census.py`; C2
operability — `verifiers/verify_dispatch_prompts.py` executing dispatch-prompt boxes `dispatch.04` and
`dispatch.08`. Plan: `plans/round-49.md`. Wave evidence: `.ufo/waves/round-49/build/`.

## Mistakes

`captured-by` names the criterion or instrument that should have caught the class;
`none → Qnn` means nothing caught it and this round adds the criterion.

|class|evidence pointer (command → output)|captured-by|fix|
|---|---|---|---|
| M29 A claim's counter counted file names, so it could not fail on an empty or uncited file (routed defect R2) | `git ls-tree -r --name-only 75f671b corpus/knowledge \| grep -c '\.md$'` → 34; committing an empty `corpus/knowledge/zz-empty.md` (0 B, no `source:`) at `75f671b` also prints 35, the round-48 declared after-value (`.ufo/waves/round-48/falsify/A09ClaimSizingC1.md`; reproduced in seat `.ufo/waves/round-49/build/MineMistake.md`, 2026-10-22). This round's first plan repeated the class twice before landing: a 20-bare-names `PROVINCE.md` printed 20 for C1 (`CriticC1Sizing.md`), and two map dispositions pointing at an unrelated instrument or a ten-byte shell stub printed 2 for C2 with the map check passing (`CriticC2Sizing.md`). | none → Q25 (Q13 was met in form: the count carried its command and date) | Q25. Both claims were re-sized before landing (`plans/round-49.md`, re-sizing notes). Shown able to fail on 2026-10-22: C1's row counter reads 0 on the base `PROVINCE.md`, and the guard `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province <file>` exits 1 on the base file ("a bare-name list is not a table"), exits 1 on a copy with kasegi reclassified `adjacent` ("province rows 20 matched 19") while the row counter still reads 20, and exits 1 on a census copy with one quote altered ("rows 20 verified 19"); unmutated it exits 0 ("rows 20 verified 20", "province rows 20 matched 20"). C2's after-value is the instrument's own box proof over committed fixtures (see `## C2 box proof` below). |
| M30 An adjacency line written without opening the sibling's bytes | Base `PROVINCE.md` § Adjacent: "kasegi — security research incl. prompt-injection exploits". `git -C ../kasegi-shokunin grep -qiE 'prompt[- ]injection' 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` → exit 1 (no match); kasegi's `PROVINCE.md` never contained `prompt` or `injection` (`git log -S` empty; seat `.ufo/waves/round-49/build/CensusKasegi.md`). The round-46 source it cites (`.ufo/round-46/scouts/w2-connector.md:22`) does not carry the clause either. | none (Q12 binds knowledge entries, not `PROVINCE.md` lines; Q14 binds negative claims) | `PROVINCE.md` § Adjacent is now a table whose every row must match a census row read at a pinned sibling commit; `verifiers/check_sibling_census.py --province` fails on any mismatch. Shown able to fail: the kasegi-reclassified mutant above exits 1. |

## Gate

**Knowledge entries:** candidates 1, admitted 1 (`corpus/knowledge/sibling-overlap-census-round49.md`),
rejected 0. Basis: each of the 20 rows was read by its own seat at a pinned commit; the L1 re-read every
quote at its pin (20 of 20 found) and the committed recheck prints `rows 20 verified 20`. One seat
classification was overridden (kotodama `none` → `adjacent`), with the reason stated in the entry.

**Round-48 erratum (routed defect R4):** the round-48 Gate had no entry-level line. Candidates 1, admitted
1 (`corpus/knowledge/frontmatter-rule-authorities-round48.md`), rejected 0 — derived from
`plans/round-48.md:42` (one entry declared) and re-measured as `ls corpus/knowledge/*.md | wc -l` → 35 at
`a5adc146` (seat `.ufo/waves/round-49/build/R4CountProvenance.md`, 2026-10-22T09:47:42Z). The entry's
counts now carry their commands in its appended `## Count provenance (round 49, routed defect R4)`
section: 21 of 23 reproduce; line 56's printed sweep pattern does not produce its stated 0 and line 32's
"24 probe fixtures" has no run list. Both are recorded there, not reworded.

**Rows written this round** (each opened on 2026-10-22 by a build-wave seat; the seat report holds the
full fetch record):

| row | URL | accessed (UTC) | quote, at most 25 words (location) |
|---|---|---|---|
| S022 | https://code.claude.com/docs/en/skills | 2026-10-22T09:41:02Z | "What the skill does and when to use it. Claude uses this to decide when to apply the skill." (§ Frontmatter reference, `skills.md:389`) — seat `.ufo/waves/round-49/build/SrcClaudeCodeSkills.md` |
| S023 | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | 2026-10-22T09:38:50Z | "Claude loads this metadata at startup and includes it in the system prompt." (§ Level 1: Metadata (always loaded), `overview.md:59`) — seat `.ufo/waves/round-49/build/SrcAgentSkillsOverview.md` |

**Existing row re-opened:** S018 (Agent Skills — Specification), `https://agentskills.io/specification.md`,
fetched 2026-10-22T09:38:59Z and again at 10:00:12Z: 200, 7,608 B, sha256 `9a67de89…`, byte-identical to
the bytes the row records. Quote: "Should describe both what the skill does and when to use it"
(§ `description` field, `specification.md:102`). Status `mined` → `mined`; recheck `90d` → `90d`;
`used-by` `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md` → `SKILL.md,
corpus/knowledge/frontmatter-rule-authorities-round48.md, corpus/knowledge/sibling-overlap-census-round49.md`
(seat `.ufo/waves/round-49/build/SrcSpecDescriptionField.md`).

Status changes logged old→new: S022 and S023 created as `mined`; S018 `used-by` as above. No other row
moved. Rows 21 → 23 (`grep -c '^| S0' corpus/SOURCES.md`).

**Not opened, so not rows:** none attempted this round beyond the three above.

## Routed items from the round-48 spot-check

- **R1 (depth):** see `## R1 repair` below.
- **R2 (claim sizing):** M29 and Q25 above; both claims re-sized before landing.
- **R3 (calibration):** correction appended under `SCORECARD.md` `Next: round 49`.
- **R4 (corpus rule):** the Gate erratum and the entry's count-provenance section above.
- **R5 (carried):** (a) the built-in marker join cannot be closed by any oracle case: the independent side
  fixes built-ins at zero, the live join exits 2 at both revisions, and S016 `index.ts:274-281` supports a
  third, unfrozen reading (the built-in is a name slot a same-name disk skill overrides). (b) The frozen
  13-case oracle `1d09a38c…` cannot hold a nested or frontmatter-name case: its contract excludes a
  name-identity rule, and all 13 cases carry frontmatter name equal to directory name at a root's direct
  child, so 13 of 13 stay green under the R1 re-key and under a recursive operator (measured). A v2 oracle is
  specified, not frozen: seven new case ids with expected values and sources (seat
  `.ufo/waves/round-49/build/R5Disposition.md`). Carried to a later round.
