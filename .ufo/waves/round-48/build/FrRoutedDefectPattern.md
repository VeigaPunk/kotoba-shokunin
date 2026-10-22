# FrRoutedDefectPattern — cross-round routed-defect pattern (r46, r47, r48 plan)

Seat: `KotobaR48.FrRoutedDefectPattern` (connector, leaf, read-only). Lane master `75f671b109d8eddd0d64c1429bd6379fe577175a`.
Written 2026-10-22T08:14Z. Nothing in the lane was edited except this file. No tools installed. No web sources opened.

## Findings

1. **The drift sentinel fires for two classes under the strict reading.** "Strict" means the class was routed by the r46 spot-check, routed again by the r47 spot-check, and is worked again by the r48 plan.
   - **A. SKILL.md frontmatter validity (description rule against its authorities).** r46 routed `<skills>` in this lane's own description. r47 worked it (C2 `trigger.no_xml_tag`) and routed it again as defect 3 (parsed value versus lexical mirror; alias, Unicode and escape counterexamples). The r48 plan works it a third time: C2 is the frontmatter-authorities entry, plus a QUALITY criterion for defect 3. The lane also *worked* this class in all three rounds: r46 folded "§ Frontmatter craft portability floor" and added Q08/M13, r47 ran C2, r48 runs C2.
   - **B. A published recipe or record that does not reproduce as written.** r46 routed "the printed C1 counting command exits 2 as written" (kaika review D-1: argparse needs `--worktree --comparator --source --arm`). r47 routed defect 2 (the stale "live 24/24" recipe, the erratum horizon, receipt revision populations). The r48 plan's frontier step qualifies the README by hand again. The lane's own lessons show the same class five times: M3, M4 (r46), and M20, M22, M23 (r47).
2. **The r48 frontier step enters no new frontier area.** Every frontier-step item in the plan (SOURCES superseding rows, lesson, QUALITY criteria for defects 3–5, README) repairs a routed defect. None of the six areas in `PROVINCE.md` § Frontier is entered. The plan also takes none of SCORECARD's own `Next: round 48` candidates (a rename-robust omp call-shape rule, `verify_harness_claims.py` 21/28, the r46 residuals). `grep -c` on the plan for `call-shape`, `21/28`, `mirror` and `NaN` returns 0 for each.
3. **Contradiction (stated, not smoothed).** C2 is new *knowledge* ground: the plan's sweep found no entry on per-authority frontmatter validity. But it is the same *defect class* for the third round, and `PROVINCE.md:15` lists the frontmatter XML-tag rule under **Core** ("round 47, moved from Frontier"). The coverage reading says "new area". The sentinel reading says "repeat". Both readings hold.
4. **r48 C1 is a new defect inside a recurring subsystem. It is not "half" of r47 defect 1.** Defect 1 is about the join definition: the producer sees a `customize-opencode` built-in marker, while the instrument fixes built-ins at 0. The plan leaves that disagreement routed. The configured-root text appears in none of the r47 routed material. In lane master outside round 48, the only hit is the r44 strings dump. In the fleet `.ufo`, the only kotoba hits are `kotoba48-prerequisite/*`. Taken narrowly, the class has run 2 rounds (r47 routed, r48 still routed). Taken broadly as "harness-independent stack correctness" (r46 comparator residuals, r47 join, r48 C1), it has run 3 rounds and the sentinel fires.
5. **One class was dropped silently (the opposite of drift).** The r46 comparator trust-boundary residuals are: mirror opt-out, missing verdict, NaN and case-variant keys, row-level `kind`, and payload-selectable scope-outs. The r47 plan promised that "each gets a why-not line in the report". The r47 report (fleet `72e0506`) contains 0 `mirror` hits and no line for any of them. The r47 spot-check does not route them. SCORECARD carries them only as standing debt (lines 104 and 108). The r48 plan has 0 hits for them. The class is neither repaired nor routed: it is fading out without a closing line.
6. **One class is confirmed closed at the r47 closure (M21, landing without an index row).** The r46 spot-check landed unindexed, but `corpus/lessons/round-47-verifier-spotcheck.md` is indexed at `corpus/README.md:65` (commit `197b5a4`, "index parent metadata").

## Table — class, r46, r47, r48 plan

| class | r46 (spot-check routed) | r47 (spot-check routed) | r48 plan | sentinel |
|---|---|---|---|---|
| A frontmatter validity | routed: own description carries `<skills>` | routed #3 (after C2 worked it) | **C2 claim** + QUALITY criterion for #3 | **fires** (3 routed, 3 worked) |
| B recipe or record does not reproduce | routed: printed C1 command exits 2 | routed #2: README 24/24, erratum horizon, revision populations | frontier step: README qualify | **fires** (3) |
| C comparator trust boundary (caller payload) | routed: 4 residuals | not routed; SCORECARD debt only; no why-not line | absent | dropped, not closed |
| D independent join definition (built-in marker) | observed only (20/24 strict); not routed | routed #1 | left routed; C1 works an adjacent new defect | 2 narrow, 3 broad (with C and C1) |
| E source-row labels and teaches (S001, S003, S010, S013) | not routed (3/3 agree); lane found the S001–S008 UTC-hour mislabel | routed #2 (first half) | frontier step: superseding rows | 2 |
| F custody and evidence preservation | not routed (lane M14, M15, M19) | routed #4 | QUALITY criterion (#3–5) | 1–2 |
| G closure metadata indexing | not routed (r46's own file landed unindexed) | routed #5 | QUALITY criterion; r47 file is indexed | closed at r47 closure |
| H lowest-axis ownership ambiguity | not routed | routed (prose, not numbered) | carried explicitly: C1 owned-axis lowest, C2 all-axes lowest | 1–2, addressed |

Verdict: the r48 plan **repeats** classes A and B (sentinel fires), **extends** D's subsystem with a new defect (C1), and is the **second** pass for E, F and H. It works **no new frontier area**.

## Second-order effect (runtime and contract)

C1 changes `oc.roots.names_plus_builtin`. The join consumes that row with an `equal` rule (`verifiers/verify_harness_claims.py:544`). That is the join behind the stale recipe at `corpus/README.md:38` ("**live 24/24 over the landed scope, exit 0**"). If the README qualification is written before C1 lands, its join number can be stale on the landed tree. That would be class B (M23) repeating inside round 48. The top-level `README.md` has 0 `24/24` and 0 `horizon` hits. The erratum horizon is only in the verifier constant (`GOVERNANCE_ERRATA_HORIZON = 2315`) and at `SCORECARD.md:33`. I sent `KotobaR48.FrReadmeQualify` a short note with these locations, and a second note on this ordering dependency. The peer confirmed `corpus/README.md:38` and `:59` ("remains protocol 24/24") as the recipe rows, and the horizon at `verify_skill_checklist.py:377` = 2315 while LOG.md is 2343 lines (peer-reported, not re-measured here). That puts LOG 28 lines past the horizon, which is the concrete form of r47's "erratum horizon" defect.

## Proposed move (one, bounded; a synthesis of three items already in the plan)

Combine three plan items: the lesson's "one mined mistake with a fix shown able to fail", the README item for defect 2, and the QUALITY criterion. Each round so far has re-fixed class B by hand, and the class keeps returning. The root cause is that Q04 ("every `recheck:`/source command resolves and runs today") has no instrument. Its instrument column in `corpus/QUALITY.md:15` is "—", and `git grep -l -i recheck master -- 'verifiers/*.py'` returns nothing (exit 1). The move:
- Mine class B as the r48 lesson's mistake.
- Make its "fix shown able to fail" a recipe-execution arm. The arm runs the qualified `corpus/README.md:38` join recipe on the **landed C1 commit**. It must fail on the 24/24 wording and pass on the qualified wording.
- Record the move as entering `PROVINCE.md` § Frontier "executed checklist coverage (33 of 41 boxes still lane-attested prose)". This is a different remedy surface (an instrument, not prose), which is what the sentinel asks for.
- Declare class A "closed to knowledge" in the C2 entry. Then round 49 cannot plan a frontmatter operability or freshness claim unless a new authority appears.

Affected axes: calibration and operability improve (one prose criterion becomes executed). Expansion: an explicit frontier area is entered. C1 and C2 are unchanged: no new claim, inside the cap.

## Risks

- The default live join exits 2 at r47 base and at landing (r47 spot-check). An arm that runs the live path would be red at landing. It must use a fixed carrier, or assert the declared non-zero exit.
- The arm must be measured after C1 lands. Ordering is a true dependency.
- The plan freezes C1 and C2, and the frontier step is at the L1's discretion. The move must not be scored as a claim.
- "Same class" depends on how classes are defined. Under per-file classes, A could be split into "XML-tag check" and "authority map", and B into "command does not run" and "command runs but the stated result differs". Under that reading only D is borderline. This report uses the definitions given in the table.

## Verification the L1 should run (not run here)

- After C1 lands: run the join with the committed recipe and the landed revision, then record the exit code and the N/24 value before writing the README qualification.
- Mutation check: the arm fails on the unqualified 24/24 line and passes on the qualified line.
- `git ls-tree -r --name-only <landed> corpus/knowledge | grep -c '\.md$'` → 35 (C2), unchanged by this move.

## Evidence (all read-only; exit codes verbatim)

- Input sha256: plans/round-48.md `aecfc904…658e8f`; round-46.md `1e99174b…f310`; round-46-verifier-spotcheck.md `d8aa580b…444a`; round-47.md `c6db414f…4e20`; round-47-verifier-spotcheck.md `fbd5a1fb…32dc`.
- `git rev-parse master` → `75f671b1…`; `git log --oneline 92aa937..master` → `75f671b`, `c0185da`, `197b5a4`.
- Drift-sentinel definition: grep for `drift sentinel|3 rounds|forces a different` in the fleet root `*.md`, `~/.agents`, `~/.omp` → no match. The rule is taken from the assignment text.
- `git show 72e0506:.ufo/reports/round-47/kotoba.md | grep -ci mirror` → 0 (exit 1).
- Plan omissions: `grep -c` for mirror, NaN, call-shape, 21/28, kind, payload on plans/round-48.md → 0 each (exit 1).
- `git show master:corpus/README.md | grep -n '24/24'` → lines 37, 38, 59. Top-level README.md → 0. `horizon` in both READMEs → 0.
- Configured-root origin: `git grep -l -i -E 'configured.root|oc-config/skill' master -- ':!.ufo/round-48/**' ':!plans/round-48.md'` → only `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` (exit 0). Fleet `.ufo` kotoba hits are only in `kotoba48-prerequisite/`.
- C1 premise at master: in `verify_harness_independent.py:595-611`, `root_dirs` is reported but never enumerated; only log-named `sources` add names.
- Join coupling: `verify_harness_claims.py:544` `"oc.roots.names_plus_builtin": ("equal", "roots_plus_builtin")`.
- `corpus/QUALITY.md`: 19 criteria; Q04 instrument "—". `git grep -l -i recheck master -- 'verifiers/*.py'` → exit 1.
- SCORECARD.md:104 and :108 carry the r46 residuals as debt and list the r48 candidates. PROVINCE.md:15 puts the XML-tag rule in Core; :21 is the Frontier list.
- r46 frontmatter work: round-46.md Gate "S001, S002, S003, S008 `queued`→`mined`, used-by … § Frontmatter craft portability floor, folded this round"; M13 → Q08.
