FAILS — C1 as planned (`plans/round-50.md` counter plus the `--skill` guard specified in build item 0, CensusGuard): the counter prints 9 with 7 lanes named, and neither instrument can fail on a description that arbitrates nothing. Six required changes below make it landable as a "names" claim.

Seat: KotobaR50.CriticC1Sizing (critic, build wave, round 50). Base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Scratch: `/fast/scratch/hyaku/kotoba-r50/build/CriticC1Sizing/` (clone `lane/`, mutants `mut/`, `counter.sh` = the plan's pipeline reading a file). No lane file touched except this report. No tools installed.

## Findings

### F1 — The counter can print 9 with fewer than 9 lanes (statement wider than counter)
`sort -u` is case-sensitive, so a capitalised repeat counts as a new lane. Mutant `m7` (base plus the line `Kagi, Kake: see above. kotodama, tameshi.`) names 7 distinct lanes and the counter prints **9**. Mutant `m2` adds only capitalised repeats of three lanes already named: distinct lanes stay 5, the counter prints 8.
- Impacted axes: adjacency, calibration (the after-value can be met without the claimed state).
- Fix: fold case before deduplicating: `grep -oiwE '…' | tr '[:upper:]' '[:lower:]' | sort -u | wc -l`. Better (F3): drop the second authority and use the guard's own line as the counter.

### F2 — Counter and guard measure different text (two authorities that disagree)
The counter reads every frontmatter line. The guard reads the `description` value. The plan's statement says "frontmatter names", but the milestone and build items 0 and 5 say "description names".
- `m3` (YAML comment `# siblings: chousa kama kotodama tameshi` after the description) and `m4` (`metadata:\n  siblings: …`): counter **9**, guard (simulated from the base `description_of` + `token_in`) **5 of 9**, PyYAML-parsed description 5 of 9.
- `m8` (column-0 comment with no colon, `# chousa kama kotodama tameshi`): counter **9**, planned guard **9 of 9**, but the parsed description has **5 of 9**. `description_of` (`check_sibling_census.py:345`) ends the value only at a column-0 line containing `:`, so a colon-free comment is swallowed into the "description". The planned guard therefore passes a file whose real description names 5 lanes.
- Fix: (a) state C1 as "the frontmatter `description` value names…"; (b) in `description_of`, end the value at any column-0 line (block-scalar content is indented), and add `m8` as a self-test red arm. `description_of` also derives the sibling cells, so rerun `--self-test` and the live census run after the change.

### F3 — Neither instrument checks arbitration: a bare list prints 9 (question 1)
| mutant (added to the base description) | counter | planned guard | parsed description |
|---|---|---|---|
| `m1` bare list `chousa kama kotodama tameshi.` | 9 | 9 of 9, exit 0 [INFERENCE: exit follows from the spec "fail naming each missing lane"] | 9 |
| `m5` negated `Never mention chousa, kama, kotodama or tameshi.` | 9 | 9 of 9 | 9 |
| `m6` suffixed `chousa-shokunin, …` | 9 | 9 of 9 | 9 |
| `m9` false split `chousa, kama, kotodama and tameshi own SKILL.md audits; kotoba does not.` | 9 | 9 of 9 | 9 |

`m6` is a legitimate pass. `m1`, `m5` and `m9` contain no arbitration or the opposite of it, and both instruments pass them. Under `corpus/QUALITY.md` Q25 a name counter "is a census observable, never the whole evidence", and the content guard's exit code must change on a mutant "with the claimed content removed or falsified". The plan's only shown mutant removes a lane name (`plans/round-50.md:24-25`), so the guard is shown to fail on missing names but never on false or empty content.

Guard conditions that would catch a bare list (none are in item 0's specification):
- G1 (clause binding): split the parsed description into clauses on `;` and `.`. Each non-`none` lane must sit in a clause that also contains an ownership or routing marker from a fixed list (`owns`, `own`, `route`, `routes to`, `NOT`, `not`). This catches `m1`, but `m5` and `m9` still pass. It is a lexical approximation and, under Q20/Q23, must say so and carry counterexamples in both directions.
- G2 (direction): every clause that names a lane must also name kotoba's side (`audits`, `reports`, `kotoba`) or carry a routing-away marker. Catches `m5` (no split) but not `m9`.
- G3 (split content pinned): give each non-`none` row in the PROVINCE.md § Adjacent table (or the census) one short "owner phrase" column, such as `research method` for chousa or `fixture and mutation method` for tameshi. The guard then requires that phrase in the same clause as the lane name. This catches `m1`, `m5` and `m9`, and it turns the unchecked PROVINCE boundary text (PROVINCE.md:32, "the boundary text is not checked") into a pinned contract.
- G4 (cap): the parsed description is 1 to 1024 characters (S018 "Must be 1-1024 characters", `specification.md:101`). Nothing checks this today: `rg -n '1024|1,024' verifiers/` finds only fixture and test literals, none in `verify_skill_checklist.py` or `check_sibling_census.py`.

Smallest safe correction: either add G1, G4 and the `m8` parse fix to item 0 with red arms for `m1`, `m8` and an over-length mutant, and keep the claim worded as "names"; or add G3 as well and then the claim may say "names with a stated split". Without G1 or G3, the round must not use "arbitrates" or "split" anywhere a C1 headline appears (round-49 closure: "each headline is wider than its counter").

### F4 — Length and caps (question 2)
- Measured: base description 815 characters (PyYAML parse of the folded scalar), 120 words, about 203 tokens at 4 characters per token [INFERENCE ratio]. A terse 9-lane draft (`mut/draft-min.md`) keeps all triggers, anti-triggers and the discovery-root note and gives each lane a 2–5 word split. It is **961 characters**, leaving 63 under the 1024 cap. Build item 5 asks for each lane "with the split the census and PROVINCE.md § Adjacent record" plus a kotodama clause that covers routing and the name collision. Fuller wording is likely to pass 1024 [INFERENCE: each extra 5-word split costs about 35 characters]. Without G4, nothing would catch it.
- S018: the spec budgets "Metadata (~100 tokens)" (`specification.md:233`, guidance, not a Must). The base is already about twice that; the draft is about 240 tokens.
- S022: the 1,536-character listing cap (`skills.md:389`, "truncated at 1,536 characters in the skill listing") is not binding below 1024. The listing budget "scales at 1% of the model's context window" and drops "descriptions starting with the skills you invoke least" (`skills.md:1207`). A longer description spends shared budget but is not dropped for its own length.
- S021: Codex's list uses "at most 2% of the model's context window, or 8,000 characters", and "Codex shortens skill descriptions first" (`build-skills.md:37-40`). The page does not say how it shortens. If shortening cuts from the tail [INFERENCE], the sibling clause and the discovery-root note go first, so arbitration material belongs ahead of the note, not after it.
- omp: the description edit changes the cache key. The first 99 characters (the omp truncator's keep) are unchanged in the draft. The lane SKILL.md is not under an omp discovery root (census `:38-41`), so this host has no live router effect.
- Precision: four more sibling names add four lexical hooks for requests that mention those lanes. S022's remedy for over-triggering is "Make the description more specific" (`skills.md:1194`). Routing-away wording ("fixes route to the owner", "Not kotodama-shokunin") is the specific form; a bare list (`m1`) is the unspecific form. No measurement of the precision effect exists on any harness here, so it is [INFERENCE] either way.
- Fit with kotoba's own box `trigger.05` (SKILL.md:210): the box asks for **overlapping** siblings named concretely with an arbitration rule. The census `adjacent` class is not the same as overlapping triggers. kake and kasegi are `adjacent` only because kotoba's own base description names them (census `:49-51`, spot-check `:79`). Their descriptions at the pins contain none of kotoba's trigger vocabulary (sweep below → empty for both). Naming them separates no realistic request; it inflates the count with two self-referential lanes. Keeping them is defensible for the adjacency axis, but the round must not credit them as trigger-precision craft, and D4's qualifier must also cover the after-state.

### F5 — Is the statement exactly what the counter proves? (question 3)
No, in four places: (1) F1 over-count; (2) F2 frontmatter versus description; (3) the counter hard-codes 9 names and reads no census, so "the census lanes classed adjacent or contested" is true only while the D3 ruling leaves classifications unchanged (the plan already requires re-declaring before landing; the guard's `K of N` reads the census and should replace the counter); (4) the counter prints a bare integer and "of 9" is the plan's denominator. Corrected statement: "kotoba's `SKILL.md` frontmatter `description` value names, as whole case-insensitive tokens, each census lane classed non-`none`: guard line `skill description names K of N non-none lanes`, 5 of 9 → 9 of 9."

### F6 — Learning-claim bar (question 4)
`LEARNING.md:16-18` (step 3, Understanding): "distill what was admitted … fold durable understanding into `SKILL.md`". Grounding exists in admitted material. The census entry was admitted at round 49 (spot-check `:171`, "agree"), and its Findings 2 and 3 (`census :115-124`) call for exactly this edit (kotodama non-reciprocal; description names 5, § Adjacent names 20). S022 and S023 are admitted `mined` rows. The bar is met for kagi, kake, kasegi, kumitate and kotodama. It is not met for three of the four new splits unless the description stays within what is admitted:
- kama: the admitted split quotes kama `cross-lane-scope.md:29`, which names agent files deleted on 2026-10-14 (PROVINCE.md:44), and kama's registry audits sibling prompt text, a possible `contested` element left unruled.
- kengaku and tameshi: the spot-check says the literal `contested` arm "would apply" and is unruled (D3, spot-check `:89-91`).

A split written into the always-loaded description before D3 is ruled and admitted moves an open, integrator-owned question (`AXES.md:16`, "integrator arbitrates") into kotoba's trigger text as settled. That would be absorption and false provenance on the adjacency axis.

Other gaps:
- The plan's sourced-claim rule (round-50 goal § 2b item 4) needs a SOURCES row opened this round, cited by the census appended section. Source IDs must not go into the description itself (they cost characters against the cap and do nothing for triggering).
- C1 adds no new knowledge entry, so it does not by itself move the expansion trend (`LEARNING.md:33`). It counts as understanding, not expansion.

### F7 — No-harm item
The admitted census cites kotoba's description by bare line, `../SKILL.md:12-15` (census `:39`), without a pinned revision. A 2–3 line description growth moves that text, so the citation goes stale. Append a correction in the census's round-50 section that pins it (`SKILL.md:12-15` at `f3046466`); the entry is append-only, so do not rewrite the line.

## Required changes (smallest safe set)
1. Counter: fold case (`tr '[:upper:]' '[:lower:]'` before `sort -u`), or replace the counter with the guard's `skill description names K of N non-none lanes` line, so one authority remains.
2. Statement and milestone: say "frontmatter `description` value names" and nothing wider. No "arbitrates" or "split" in any SCORECARD, LOG, report or commit headline unless change 4 lands.
3. Guard (item 0): add G4 (parsed length 1–1024, exit 1 above it). Fix `description_of` to end at any column-0 line. Add self-test red arms for `m8` (colon-free comment), an over-length description and `m7` (case duplicates, which must report 7 of 9).
4. Guard: add G1 clause binding (minimum) with red arms `m1` and `m5`; or G3 owner phrases pinned in the PROVINCE.md table (stronger; catches `m9`). Name it as a lexical approximation with counterexamples in both directions (Q20/Q23).
5. Description (item 5): ≤1024 parsed characters, with the sibling clause before the discovery-root note. For kama, kengaku and tameshi, state only the admitted, uncontested side, or wait for an admitted D3 ruling, never one decided in the same round by kotoba alone. Keep the first 99 characters unchanged. Keep the triggers and anti-triggers (`trigger.literal_trigger_string`, `trigger.anti_trigger_clause`, `trigger.no_xml_tag` must still pass).
6. Records: the D4 qualifier also covers the after-state (kake and kasegi are self-referential); append the `SKILL.md:12-15`-at-`f3046466` pin to the census entry; and do not claim a trigger-precision gain (not measured anywhere).

## Evidence (commands and exit codes)
- Plan counter, verbatim, lane checkout: `git show f30464660c675d1c1e2851a3bf0366a3aaffe5a8:SKILL.md | awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' | grep -oiwE 'chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi' | sort -u | wc -l` → `5`, exit 0.
- Mutants, scratch (`./counter.sh mut/<f>`, same pipeline on a file; `LC_COLLATE="en_US.UTF-8"`), exit 0 each: base 5; m1 9; m2 8; m3 9; m4 9; m5 9; m6 9; m7 9; m8 9; m9 9. sha256: base `f290e89e…`, m1 `87bc4e10…`, m2 `e539e043…`, m3 `c5cfa446…`, m4 `4dc4f392…`, m5 `53b59669…`, m6 `3d1d7931…`, m7 `d90c68a9…`, m8 `d211c5ba…`, m9 `2ea5ecdd…`, draft-min `35dae71d…`, counter.sh `d15b538e…`.
- m7 distinct lanes: the same pipeline with `tr A-Z a-z` before `sort -u` → 7 (m2 → 5). m2 raw `sort -u` output: `kagi Kagi kake Kake kasegi Kasegi kengaku kumitate`.
- Planned guard simulation: Python importing `description_of` and `token_in` from `lane/verifiers/check_sibling_census.py` at base, over `mut/*.md`, plus PyYAML `safe_load` → base 5/5; m1 9/9; m2 5/5; m3 5/5; m4 5/5; m5 9/9; m6 9/9; m7 7/7; m8 **9 (guard) / 5 (YAML)**; m9 9/9. Exit 0. Parsed lengths: base 814 (815 with the folded scalar's final newline), draft-min 961.
- `--skill` absent at base and in the CensusGuard clone: `rg -n -- '--skill|skill_names|non-none' …/CensusGuard/lane/verifiers/check_sibling_census.py` → no output. No cap check: `rg -n '1024|1,024' lane/verifiers/` → 3 hits, all fixture or test literals.
- Sources, from fetched copies whose hashes match the SOURCES rows: S022 `skills.md` sha256 `cdfcb0df…` lines 389, 1194, 1207, 1213; S021 `build-skills.md` sha256 `ed6e324f…` lines 37-40; S018 `specification.md` sha256 `9a67de89…` lines 101, 233; S019 `best-practices.md` sha256 `f0a5d61b…` line 215 ("Claude uses it to choose the right Skill from potentially 100+ available Skills"). These are previously fetched files under `/fast/scratch/hyaku/kotoba-r49/…` and `/fast/scratch/hyaku/kotoba-r50/build/src-reopen-s019/`; this seat opened no new URL.
- kake and kasegi trigger-vocabulary sweep: frontmatter at pins `e73d48bb…` and `1fafde8f…`, `grep -oiE 'skill file|SKILL\.md|frontmatter|trigger word|prompt craft|write a skill|audit this skill|skill quality|AGENTS\.md|dispatch prompt|system prompt'` → empty for both, exit 0 overall. kotodama `SKILL.md:3` at `35f0d49f…` contains `NOT prompt/skill craft (kotoba-shokunin)` (grep exit 0).
- Admission basis: `rg -n … corpus/lessons/round-49-verifier-spotcheck.md` → `:16` "Admitted.", `:89-91` D3 unruled, `:171` census admit "agree".
