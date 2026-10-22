# A30Governance — records commit 84b9c9ba: governance.citation_resolves falsify

## Verdict

CONFIRMED — the expected red is the only red. At records commit
`84b9c9ba89559b51a72c83c2b9605b184df4ae9e`, `governance.citation_resolves` fails with exactly
one canonical unresolved token, and it is the anticipated one: SCORECARD's fresh pointer to the
round-48 report `.ufo/reports/round-48/kotoba.md`, which lands last. Every other citation token
in the new LOG.md entry and in SCORECARD.md's round-48 clauses resolves. No DEFECT found in the
records commit's citation surface.

## Run evidence (private clone, pinned)

- Clone: `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A30Governance/clone`, `git checkout`
  `84b9c9ba89559b51a72c83c2b9605b184df4ae9e` (clean tree, HEAD `84b9c9b round-48: records …`).
- Command: `python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves`
  → exit code 1; JSON: `status FAIL`, `evaluated 901`, `fail 1`, detail ends
  `9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused`.
- The raw detail names 4 tokens + "(+21 more)" = 25 raw failures — but only 1 survives canonical
  interpretation (next section); the raw FAIL count in a private clone is NOT the red count.

## Naive-clone artifacts (24 of 25 raw failures)

`citation_resolve` resolves `../`-hop tokens against the repo's ancestors (verifier lines
1360-1385). A private clone's parents are scratch dirs, not the fleet repo, so 24 historical
`../` tokens fail spuriously there. All 24 resolve canonically (repo parent = fleet
`/home/vgpnk/Projects/shokunin`); representative targets verified to exist fleet-side:
`.ufo/reports/round-9/kotoba.md`, `.ufo/reports/round-11/kotoba.md`, `PROTOCOL.md`,
`.ufo/l0-questions.md` (EXISTS). Full artifact list (naive=FAIL, canonical=OK):

- LOG.md:177 `../.ufo/reports/round-9/kotoba.md`; LOG.md:255 `../.ufo/reports/round-11/kotoba.md`;
  LOG.md:311 `../PROTOCOL.md`; LOG.md:779, 1221 `../.ufo/l0-questions.md`;
  LOG.md:824 `../kasegi-shokunin/corpus/instruments/resolve.py` and `…/anchorcheck.py`;
  LOG.md:974 `../.ufo/waves/shokunin12h-20261014-p1-repair/members/`; LOG.md:1203 `../AXES.md`.
- SCORECARD.md:3 `../MISSION.md`; :5 `../PROTOCOL.md`, `../SCORECARD.md`; :15 `../.ufo/l0-questions.md`;
  :31 `../.ufo/reports/round-16/kotoba.md`; :34 `../.ufo/l0-questions.md`,
  `../kasegi-shokunin/corpus/instruments/`, `…/resolve.py`, `…/anchorcheck.py`;
  :100, 131, 250 `../AXES.md`; :141 `../.ufo` (×2); :152 `../.ufo/l0-questions.md`.

## Canonical re-derivation (the decisive count)

Re-ran the verifier's own `citation_subjects(exclude_quoted=True, exclude_schematic=True)` +
`citation_resolve` over the pinned LOG.md/SCORECARD.md, resolving plain tokens against the pinned
clone and `../` tokens against the real lane checkout. Reproduces the CLI run exactly:
evaluated 901, quoted excluded 9 (LOG 8 + SCORECARD 1), schematic excluded 3 (LOG 280
`../.ufo/…`, LOG 370 `.ufo/reports/round-N/`, SCORECARD 137 `.ufo/reports/round-N/kotoba.md`),
erratum excused 1 (LOG.md:2111 `.ufo/round-45/drafts/v10/post-r44-hunt.py`, line sha256 matches
`7dcbf123…0135`). Canonical failures: **1**.

## The only canonical red

- `SCORECARD.md:110` — `.ufo/reports/round-48/kotoba.md` — added by this commit
  (hunk `@@ -109,0 +110,4 @@`). Sentence: "…configured-root enumeration landed at `d1ae458`
  (ruler target failures 5 → 0; does not resolve routed defect 1). Verdicts belong to the
  non-author closure. Report `.ufo/reports/round-48/kotoba.md`."
- Token is lane-rooted (no `../`), unquoted, non-schematic (`round-48`, not `round-N`), so the
  check demands it exist now. Absent today in both the lane worktree
  (`kotoba-shokunin/.ufo/reports/round-48/kotoba.md` ABSENT; lane `.ufo/reports/` holds rounds
  through 45) and fleet-side (`ABSENT`). This is the deliberate "lands last" pointer; it clears
  when the round-48 report lands at that path.

## Unresolved tokens in the new clauses (the assignment's list)

New-line universe from `git show 84b9c9ba -U0 -- LOG.md SCORECARD.md`; every subject extracted
and resolved:

- LOG.md new entry (lines 2344-2354): 20 subjects — `.ufo/waves/round-48/build-spec.json`,
  `build-dispatch.json`, `build-assignments.json`, `build/`, `build/C1RulerTargetMutants.md`,
  `build/C1RegressionArm.md`, `.ufo/round-48/verification/after-configured-root.json`,
  `corpus/lessons/round-48.md`, `corpus/QUALITY.md`,
  `verifiers/verify_harness_independent.py`, `corpus/knowledge/frontmatter-rule-authorities-round48.md`,
  `corpus/SOURCES.md`, `corpus/README.md`, `verifiers/corpus-baseline.json`,
  `verifiers/check_substrate_pins.py`, `verifiers/verify_surfaces.py`,
  `verifiers/compare_harness_independent.py`, `build/FrCensusAndScorecard.md` — ALL RESOLVE
  (committed lane files).
- SCORECARD.md round-48 clauses: depth row (line 28, 15 subjects), freshness row (line 32,
  7 subjects), completed/next block (lines 110-113), round summary table (lines 201-202,
  4 subjects) — all resolve EXCEPT the single red above (SCORECARD.md:110). Lines 111-113 carry
  no citation subjects. No new-range token is quoted-excluded or schematic.

## Residual risk / verification gaps

- I did not execute the CLI inside the live lane checkout (read-only bounds; worktree drift
  risk). The canonical count is a module-level re-derivation using the verifier's own functions
  with identical parameters, cross-checked against the CLI's exact counters (901/9/3/1). An
  in-lane CLI run should reproduce: FAIL, evaluated 901, exactly the SCORECARD:110 red.
- `../` resolution is environment-sensitive by design; any re-run outside the fleet-layout
  parent chain will show the 24 artifacts above — they are not defects in this commit.
- The red's disappearance depends on the report landing at the lane-rooted path
  `.ufo/reports/round-48/kotoba.md` specifically (not a fleet-rooted path) — worth confirming at
  wave close, since the plan prose calls it "the fleet report".

No tools installed or upgraded (none needed).
