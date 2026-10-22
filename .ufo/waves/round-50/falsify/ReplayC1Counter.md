# ReplayC1Counter — C1 counter replay + independent cross-check (kotoba round 50 falsify)

HOLDS — the declared C1 counter transition reproduces at both pinned revs (guard: `5 of 9` exit 1 at
f3046466, `9 of 9` exit 0 at 542f5156, run from a private clone at 956ee1676), and an independent
PyYAML whole-token case-folded count plus per-lane clause parse agrees (base 5 of 9; claims 9 of 9,
every named lane in a clause carrying an ownership word). No finding against C1 in this scope.

## Method

- Private clone: `git clone` of the lane + `git checkout 956ee1676e4c18480bce8ac3993541462be76e11`
  in `/fast/scratch/hyaku/kotoba-r50/falsify/ReplayC1Counter/lane` (read-only lane untouched).
- Both SKILL.md bytes saved from the clone: `git show f3046466...:SKILL.md > SKILL.base.md` (35,930 B),
  `git show 542f5156...:SKILL.md > SKILL.claims.md` (36,128 B).
- Guard: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
  --province PROVINCE.md --skill <saved file>`, run from the clone root.
- Independent method: PyYAML 6.0.3 (preinstalled; no tool installed this run) `yaml.safe_load` of the
  frontmatter; `\b<lane>\b` whole-token case-folded count over the parsed `description` for the 9
  non-`none` census lanes (chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate, tameshi);
  clause split on `;` and `.`; per-lane clause listing with ownership/routing words.

## Evidence (outputs verbatim, exit codes as returned)

1. Guard at base f3046466 — **exit 1**:

   ```
   FAIL skill description does not name the non-none census lane chousa
   FAIL skill description does not name the non-none census lane kama
   FAIL skill description does not name the non-none census lane kotodama
   FAIL skill description does not name the non-none census lane tameshi
   rows 20 verified 20
   province rows 20 matched 20
   skill description names 5 of 9 non-none lanes
   skill description length 814 of 1024
   ```

2. Guard at claims 542f5156 — **exit 0**:

   ```
   rows 20 verified 20
   province rows 20 matched 20
   skill description names 9 of 9 non-none lanes
   skill description length 1008 of 1024
   ```

3. Independent PyYAML count (whole token, case-folded, over the parsed description):
   - base: chousa 0, kagi 1, kake 1, kama 0, kasegi 1, kengaku 1, kotodama 0, kumitate 1,
     tameshi 0 → **5 of 9** (kagi, kake, kasegi, kengaku, kumitate); description 814 chars.
     Plan pipeline with case-fold on the parsed description: same 5.
   - claims: chousa 1, kagi 1, kake 1, kama 1, kasegi 1, kengaku 2, kotodama 2, kumitate 1,
     tameshi 1 → **9 of 9**; description 1,008 chars (matches the census's "1,008 characters").
     Plan pipeline with case-fold: same 9.

4. Per-lane clause parse of the claims description (split on `;`/`.`): kagi, kake, kasegi, kengaku,
   kumitate sit in "Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own their own SKILL"
   (word: own); chousa in "chousa owns the research method" (owns); kama in "kama owns endpoint
   verification" (owns, verification); kengaku also in "kengaku owns measured effects of prompt
   format" (owns); tameshi in "tameshi owns the fixture and mutation method" (owns); kotodama in
   "NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds despite the
   similar name" (not, owns — a refusal that routes by name). Base: the 5 named lanes share one
   clause ("... own their own SKILL" + "fixes route to the owning lane" later in the sentence).
   Every clause a lane sits in carries an ownership or routing word — the statement's second clause
   is true of the bytes, not only of the guard's lexical pass.

5. Q25 mutant (counter able to fail): claims description with the clause
   "; tameshi owns the fixture and mutation method" removed (962 chars) → guard **exit 1**:
   `FAIL skill description does not name the non-none census lane tameshi`,
   `skill description names 8 of 9 non-none lanes`.

6. Q26 probe (marker clause turned on): claims description with "tameshi owns" replaced by
   "tameshi and" (lane named, no marker) → guard **exit 1**:
   `FAIL skill description mentions the non-none census lane tameshi, but no clause that names it
   carries an ownership or routing marker (owns/own/owned/route/routes/routing/NOT/see above/as
   above/see also): naming a lane is not a split.  This marker rule is a lexical approximation,
   not a parse of intent`, `skill description names 8 of 9 non-none lanes`. So the statement's
   "each in a clause with an ownership or routing word" is measured by the counter, not asserted
   past it; the guard itself labels its marker rule a lexical approximation.

## Findings

- None against C1 in this scope. Declared `5 of 9` (exit 1) → `9 of 9` (exit 0) reproduces
  exactly; the independent count agrees on both sides; the marker clauses are real ownership
  statements; the counter fails on both mutant directions (lane removed; lane named without a
  marker).
- Note (not a defect, already recorded by the lane): the guard's marker test is lexical, so a lane
  next to a false ownership word would pass; the census entry states this (mutant m9) and the
  guard's FAIL text says so. My parse shows the landed words are genuine ownership/routing words,
  so the claim's substance does not rest on the lexicality.
- Note (method artifact): splitting the claims description on every `.` cuts "SKILL.md" mid-token
  ("own their own SKILL"); the guard's own splitter does not split there (docstring lines 437-439).
  No effect on any count; the ownership word precedes the cut in every case.

## Residual risk / verification gaps

- I verified only C1 in this scope: the guard runs at 956ee16 against saved bytes of the two named
  revs. I did not re-run the census table verification against sibling repos, C2, D1-D6, S024-S029,
  Q26/M31 records, or the LOG claims beyond reading them.
- The guard's census-side checks (rows 20 verified 20) ran inside both commands above and passed,
  but the pinned sibling bytes were not independently re-fetched by this seat.
- Scratch clone retains the four saved files (`SKILL.base.md`, `SKILL.claims.md`,
  `SKILL.claims.mutant.md`, `SKILL.claims.nomarker.md`), descriptions (`desc.base.txt`,
  `desc.claims.txt`) and `crosscheck.py` for rerun.

## Rules

- No tool installed or upgraded (PyYAML 6.0.3 already present; pacman untouched per host pause).
- Lane repo untouched except this Report file; no git/jj write commands anywhere.
