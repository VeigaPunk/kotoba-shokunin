# Plan — round 50 (hyaku campaign, attempt 1)

Base: branch `master` at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` (round 49 admitted; spot-check
`corpus/lessons/round-49-verifier-spotcheck.md`). Shape: default, two v1 waves (build, then falsify).
The L1 holds the planner seat; no swarm planner item.

## Claims (each statement is exactly what its counter prints)

**C1 — adjacency (lowest-scoring non-retired axis, tied with freshness at 8.0; the learning claim).**
Statement: kotoba's `SKILL.md` frontmatter names the census lanes classed `adjacent` or `contested`
in `corpus/knowledge/sibling-overlap-census-round49.md`: 5 of 9 → 9 of 9.

Counter (runs at any revision `<rev>`):

    git show <rev>:SKILL.md | awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' \
      | grep -oiwE 'chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi' | sort -u | wc -l

Before: 5 at `f3046466` (measured 2026-10-22T12:18Z; the names are kagi, kake, kasegi, kengaku,
kumitate). After: 9. The lane list is the 9 census rows whose classification is not `none` at
`f3046466`; if the round-50 precedence ruling (routed defect D3) moves a row between `none` and
non-`none`, the list and the target are re-declared before landing, not after.

Content guard (Q25): `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md`
fails (exit 1) and names the lane when a non-`none` census lane is missing from the description.
Shown able to fail: the base description fails it (4 lanes missing), and a mutant with one lane
name removed fails it.

Source: at least one new `corpus/SOURCES.md` row opened this round on how a client presents skill
descriptions and whether it documents a tie-break between overlapping skills; the description
edit and the census entry's appended section cite it.

**C2 — operability.** Statement: deleting any one of the 6 must-fail cases from
`verifiers/fixtures/dispatch-prompts/manifest.json` makes `--box-proof` exit 1: 0 of 6 → 6 of 6.

Counter: a committed driver that, for revision `<rev>`, extracts the instrument and fixtures into a
temporary tree, deletes each must-fail case in turn and runs
`python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json`;
it prints `killed K of 6`. Before: 0 of 6 at `f3046466` (round-49 falsify `ReplayC2BoxProof` M5/M6
and `ReviewLessonQ25` saw `boxes proven 2` after deleting a case). After: 6 of 6.

## Routed defects from the round-49 spot-check (fixed or explained; not claims)

- D1: report addenda append at the end; line 4 is never rewritten.
- D2: `box_proof` docstring and help text stop saying "every conjunct"; the SCORECARD operability
  row gains the six-conjunct bound; the decision on running `--box-proof` from a gate is recorded.
- D3: a precedence rule between the `contested` arm and a stated split, appended to the census
  entry; kengaku and tameshi (and kama) ruled; the guard rejects duplicate rows; the guard enters
  `verifiers/floors-registry.json`.
- D4: the SCORECARD adjacency row gets the qualifier (kake and kasegi rest on kotoba's own
  description; contested arm unruled until D3).
- D5: this round's lesson § Gate records rejections with reasons, and an erratum for the
  round-49 Gate.
- D6: R4, R5 and the R1 no-name fallback are carried with a stated reason.

## Frontier step

Census before/after; new SOURCES rows for C1; one mined mistake (candidate: a claim headline wider
than its counter, twice in round 49) into `corpus/lessons/round-50.md`.

## Waves

- build (32–40 seats): `.ufo/waves/round-50/build-spec.json`.
- falsify (32–40 seats), only if build yields at least 32 distinct attack items.

## Re-sizing before landing (build-wave critics, 2026-10-22T12:35Z)

Both counters were re-sized before any landing. No target value moved.

- **C1** (`.ufo/waves/round-50/build/CriticC1Sizing.md`, FAILS as first planned): the pipeline above is
  case-sensitive (`Kagi` and `kagi` counted twice: 7 lanes printed 9), reads the whole frontmatter
  instead of the `description` value (a YAML comment printed 9), and a bare list of names printed 9.
  New statement: kotoba's `SKILL.md` frontmatter `description` value names each census lane classed
  non-`none`, each in a clause that carries an ownership or routing word: guard line
  `skill description names K of N non-none lanes`, 5 of 9 → 9 of 9. Counter: the round-50 guard
  `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill <file>`
  run on `git show <rev>:SKILL.md` saved to a file. Cross-check: the pipeline above with
  `tr '[:upper:]' '[:lower:]'` before `sort -u`, applied to the parsed description. The guard also
  enforces the 1024-character cap and ends the value at any column-0 line. The description states
  only the admitted, uncontested side of each split, and no "arbitrates" headline is claimed.
- **C2** (`.ufo/waves/round-50/build/CriticC2Sizing.md`, FAILS as first planned): a manifest hash pin
  also prints 6 of 6; a deleted fixture directory exits 1 by traceback; the driver must not take its
  denominator from the revision it measures. New counter rules: the denominator is pinned to the six
  conjunct names; delete means removing a manifest entry; a kill needs exit 1, `boxes proven 1` or
  `0`, and a stderr line naming the deleted case's conjunct. Coverage is checked on observed
  conjunct statuses (with one pinned co-failure: the placeholder sits inside the stem), and the
  laundering arms (twin then delete passes; relabelled copy fails) are self-test arms. Statement
  unchanged: 0 of 6 → 6 of 6.
