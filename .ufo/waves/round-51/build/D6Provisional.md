# D6Provisional — routed defect D6, rule status and the generic-refusal bound

**HOLDS-BOUNDED** for the census entry's round-50 precedence rule and the tameshi row it clears:
the rule is marked provisional pending the operator's L0 answer, the after-the-rows ordering is
recorded, the generic-refusal exit is bounded, and round 51 neither extends nor relies on the rule.
No classification, count, commit or basis changes. The patch collides with the D5 seat's append on
the same file tail; an ordered variant is supplied.

## Behaviour

**Two appends, both append-only.**

1. `corpus/knowledge/sibling-overlap-census-round49.md` — one new section
   `## Round 51 status of the precedence rule (routed D6)` (43 lines), appended at the file end.
   Four bullets:
   - *The rule is provisional until the operator answers.* The rule and its three rulings are
     kotoba's own reading, not an integrator ruling. The question is the `kotoba | round-50` line of
     the fleet file `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`, **line 105** (read
     read-only on 2026-10-22). That line carries the request "Accept, or rule otherwise?" and carries
     no answer; the file's two `L0 ANSWER` markers are on lines 52 and 53 and answer other lanes'
     questions (kama round-11, tsukuroi round-12).
   - *The rule was written after the rows it decides were known.* The round-49 section already listed
     kama, kengaku and tameshi as open "possible `contested`" items (entry lines 165, 180, 185-186),
     and the rule and its three rulings landed together in the round-50 landing at `956ee16`. The
     non-author spot-check says the exit clause "clears exactly those three"
     (`corpus/lessons/round-50-verifier-spotcheck.md:207-213`). Those three are the only rows whose
     class the rule settled; mado stays `none` on the Classification rule alone. For kama and tameshi
     the sibling-split exit is the operative clause (the falsify-wave corrections above already record
     that the arm fires and the sibling's own split clears each); for kengaku the arm never fires,
     because its cross-lane runs appear only in wave reports, which § Classification rule excludes.
   - *Bound on the generic-refusal exit.* The exit as written fires on any sibling sentence that
     assigns the claimed element away from the claimant, and it does not require that sentence to name
     the element. A generic refusal therefore clears any gate claim, whatever gate is at issue:
     tameshi's "every lane's gate remains its own" (tameshi `PROVINCE.md:14` at `3b20f073`) is such a
     sentence (`../.ufo/waves/round-50/falsify/RowTameshiR50.md:37`, finding F4). **A row cleared
     only by a generic refusal is marked as such, and the tameshi row is marked.** Under the literal
     round-49 wording the arm fires and only the generic refusal clears it; under the round-50
     definition no claim exists at all, so the row is `adjacent` either way. Its class is unchanged.
     kama is not so marked: its exit is a specific assignment (kama
     `corpus/knowledge/cross-lane-scope.md:29` at `c808ba07`), and the falsify seat records the same
     (`../.ufo/waves/round-50/falsify/RowKamaR50.md:33-43`, findings F4 and F5). kengaku is not so
     marked either: its claim never arises.
   - *Round 51 neither extends nor relies on the rule.* No round-51 claim uses it, no row outside the
     three it already decided is measured under it, and no clause of it is amended. Round 51's claims
     are the omp 18.12.6 surface re-derivation and the overlap-lever learning table; neither reads
     this entry's precedence.

2. `PROVINCE.md` § Adjacent intro — one appended line, before the table, pointing at the census
   section and recording that the rule is provisional and that no row or classification changes. One
   line, one paragraph, no table row touched.

**Not changed:** every census row, the counts (9 adjacent, 11 none, 0 contested), every commit, the
basis labels, `§ Classification rule`, the round-50 precedence section and its rulings, the
`## Counts` section, and the round-49 falsify-wave corrections.

## Touched surfaces

- `corpus/knowledge/sibling-overlap-census-round49.md`: +43 lines at the file end (one section).
- `PROVINCE.md`: +2 lines (§ Adjacent intro paragraph, before the `| lane |` table).
- Nothing else. The lane checkout was not written to; all edits are in a private clone.

## Gate results

| check | base | after | exit |
|---|---|---|---|
| `check_sibling_census.py <census> --province PROVINCE.md --fleet <fleet>` | rows 20 verified 20 / province rows 20 matched 20 | identical | 0 |
| same, `--skill SKILL.md` added | skill description names 9 of 9 non-none lanes; length 1019 of 1024 | identical | 0 |
| `check_sibling_census.py --self-test` | self-test: 0 failure(s) over 68 assertions | identical | 0 |
| `verify_corpus_integrity.py --json` | 4 DRIFT (`corpus.index.tracked_files` 70→69, `corpus.index.unindexed` 1, `corpus.pointers.report_total` 45→44, `corpus.pointers.report_dead` 2) | identical; verdict deltas base→after: none (empty) | 1 (pre-existing) |
| `verify_skill_checklist.py` (lane checkout, read-only) | — | all PASS, incl. `trigger.citation_resolves` 49/49 and `governance.citation_resolves` 962/962 | 0 |
| `git apply --check patch.diff` against base `43ca0bfb` | — | applies cleanly | 0 |

The four corpus-integrity DRIFT lines are pre-existing at base and byte-identical after: the
unindexed file is `corpus/lessons/round-50-verifier-spotcheck.md` and the two `report_dead` are the
round-48 closure's, neither mine. `check_sibling_census.py` is the only verifier that reads
`PROVINCE.md`, and it checks lane set, classification and commit — not boundary text, and not the
intro paragraph.

## Patch delivery (collision with the D5 seat — order matters)

D5Rows and I both append at the same EOF of `corpus/knowledge/sibling-overlap-census-round49.md`
(both hunks are `@@ -368,3 +368,NN @@` off the same base tail). Only one can go first:

| route | result |
|---|---|
| `patch.diff` (mine) → `D5Rows/patch.diff` | exit 1, `patch failed: corpus/knowledge/sibling-overlap-census-round49.md:368` |
| `D5Rows/patch.diff` → `patch.diff` (mine) | exit 1, same error |
| `D5Rows/patch.diff` → `patch-after-D5.diff` (mine) | both apply, exit 0; guard exit 0 |
| `D5Rows/patch-combined-D5-then-D6.diff` (one diff, D5Rows' merged artifact) | applies to base, exit 0; guard exit 0; corpus-integrity verdicts identical to base |

Artifacts (all under `/fast/scratch/hyaku/kotoba-r51/build/`):
- `D6Provisional/patch.diff` — mine against base `43ca0bfb`; applies cleanly to base alone.
- `D6Provisional/patch-after-D5.diff` — the same content as a delta that applies **after** D5's patch.
- `D5Rows/patch-combined-D5-then-D6.diff` — D5Rows' single merged diff (both sections, both
  PROVINCE edits) that applies to base in one step; verified by me: guard exit 0, corpus-integrity
  verdicts identical to base, `check_sibling_census.py --self-test` 0 failures over 68 assertions.
- `D6Provisional/d6_section.md` and `D6Provisional/d6_prov_line.txt` — my text verbatim, if the L1
  prefers to place it by hand. (Both live under `/fast/scratch/hyaku/kotoba-r51/build/D6Provisional/`.)

D5Rows independently reproduced the failure and the ordered route, and produced the combined diff.
Both sections coexist in one file with no stray pipe-leading lines (D5's at line 372, mine at 416 in
the combined tree). My section cites entry lines 165, 180 and 185-186 only, so neither section's line
references depend on the other's position. `PROVINCE.md` does not collide: D5's hunk is the kama row
(line 44), mine is the § Adjacent intro (line 35); I verified the PROVINCE-only hunk applies after
D5's patch (exit 0).

**The lane working tree already carries D5's change** (observed 2026-10-22T12:05Z: `PROVINCE.md` and
`corpus/knowledge/sibling-overlap-census-round49.md` are modified in the checkout, the census carrying
D5's section at line 372 and the kama row corrected; the modified `verifiers/` files are other seats'
work, not mine). I copied that exact two-file state into a scratch clone and ran
`git apply --check patch-after-D5.diff`: **applies cleanly, exit 0**. Applying it there and running
the gates: `check_sibling_census.py --province --skill` prints "rows 20 verified 20 / province rows 20
matched 20 / skill description names 9 of 9 non-none lanes / length 1019 of 1024", exit 0; the census
then carries D5's section at 372 and mine at 416; `PROVINCE.md` carries my intro line; and
`verify_corpus_integrity.py --json` verdict deltas against base are none (the same 4 pre-existing
DRIFT). So the L1 can apply `patch-after-D5.diff` directly to the lane's current state, with no
ordering step. I did not write to the lane: my only lane write is this report file.

## Out of scope

- The L0 answer itself. The question is open at fleet `4bb23af`; this seat cannot answer it and does
  not try. The section marks the rule provisional until it is answered.
- The `## Classification rule` two-definition conflict (round-49 `:45-46` vs round-50 `:253-260`).
  Recorded in the section as the reading in force, not rewritten: the generic-refusal bound says what
  the exit does, and the falsify seat owns the definition repair.
- D5's kama quote and deletion-citation repair, and D3's `corpus/README.md:72` / `SKILL.md:375-377`
  sweep. Other seats.
- The `corpus/README.md` index row for this entry. The entry is already indexed
  (`corpus/README.md:69`); its basis cell describes the round-49 census, not the round-51 status
  section, so no index change is needed and none is made. Flagging it for the L1: if the L1 wants the
  index row to mention the provisional status, that is a separate edit in a file this seat does not own.
- Any round-51 claim. This seat changed no claim, no counter and no classification.

## Findings

- The rule's exit clause has no specificity requirement, so a sibling's blanket refusal discharges
  any gate claim it happens to cover. tameshi is the row that rests on such a refusal; kama's exit is
  a specific assignment and kengaku's claim never arises. That asymmetry is now written down rather
  than left in the falsify wave's findings.
- The rule was written after the three rows it settles were known, and it settles exactly those three.
  The rule landed with its rulings in one commit (`956ee16`), and the round-49 section already carried
  all three as open "possible `contested`" items. The ordering is a fact about how the rule was
  authored, and the L0 question exists because of it; the section says so plainly.
- The operator's question is unanswered as of 2026-10-22: the kotoba round-50 line at
  `.ufo/l0-questions.md:105` carries the request and no answer. The file's only two `L0 ANSWER`
  markers are on lines 52 and 53, for kama round-11 and tsukuroi round-12. So "provisional" is a
  statement about the current state of the queue, not a prediction about the answer.
- No round-51 claim reads this rule, so recording its status cannot move a counter. Verified against
  the plan: C1 is the omp 18.12.6 surface re-derivation, C2 the overlap-lever table.

## Evidence (commands with exit codes)

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD
43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10
$ grep -n "^kotoba | round-50" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
105:kotoba | round-50 | Integrator ruling requested on kotoba's own boundary rule ...
$ grep -c "" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
106
$ grep -n "L0 ANSWER" /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md | cut -c1-60
52:kama | round-11 | Planner taxonomy conflict: the mandator
53:tsukuroi | round-12 | Reconcile required planner-role sea
$ git -C /home/vgpnk/Projects/shokunin show 8d56eb1:.ufo/l0-questions.md | grep -n "^kotoba | round-50"
105:kotoba | round-50 | Integrator ruling requested on kotoba's own boundary rul
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log --oneline -- corpus/knowledge/sibling-overlap-census-round49.md
1cb2e65 ... 87eeae2 ... bf109ca ... a78fec1 ... 956ee16 round-50: D3 precedence rule and rulings (no row moves) ...
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show --stat 956ee16 | head -8
956ee16 round-50: D3 precedence rule and rulings (no row moves), PROVINCE rows ruled, ...
 corpus/knowledge/sibling-overlap-census-round49.md | 51 ++++++++++++++++++++++
$ grep -n "possible `contested` element\|Recorded, not ruled\|recorded for the integrator" .../sibling-overlap-census-round49.md
165, 180, 185-186   (kengaku, tameshi, kama — the round-49 open items)
$ grep -n "clears exactly those three" .../round-50-verifier-spotcheck.md
209: ... its exit clause
210:clears exactly those three. Under a "claim always wins" reading, kama and tameshi would flip
$ git -C /home/vgpnk/Projects/shokunin/tameshi-shokunin show 3b20f073c7305a582562cd323982991464c324f3:PROVINCE.md | sed -n '10,20p'
  14: **Refuses:** product domains — every lane's gate remains its own; tameshi
$ git -C /home/vgpnk/Projects/shokunin/kama-shokunin show c808ba07f09c4be55413d3d6516c542ab69b64f8:corpus/knowledge/cross-lane-scope.md | sed -n '29p'
| A model/baseURL/fallback statement in an agent file versus truth about the service. | **Kotoba** owns the instruction/agent surface and its model/fallback wording; **kama** owns independent verification of the target endpoint. ...
$ grep -n "F4 MEDIUM (two definitions of contested)" .../round-50/falsify/RowTameshiR50.md
37: - **F4 MEDIUM (two definitions of contested).** ...
$ grep -n "^\*\*F4\|^\*\*F5" .../round-50/falsify/RowKamaR50.md
33:**F4 (Medium). The excuse, not the premise, keeps the row `adjacent`.**
39:**F5 (Medium). Claim-always-wins flips the row, on living text.**

$ cd .../D6Provisional/verify_base && python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md --fleet /home/vgpnk/Projects/shokunin
rows 20 verified 20
province rows 20 matched 20
skill description names 9 of 9 non-none lanes
skill description length 1019 of 1024
=== exit 0 ===
$ python3 -B verifiers/check_sibling_census.py --self-test
self-test: 0 failure(s) over 68 assertions
=== exit 0 ===
$ python3 -B verifiers/verify_corpus_integrity.py --json
=== exit 1 === (4 DRIFT, all pre-existing; verdict deltas base->after: none)
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py
PASS trigger.citation_resolves: evaluated 49 — 49 repo-rooted citation token(s) resolve from the repo root
PASS governance.citation_resolves: evaluated 962 — 962 governance citation token(s) resolve across 2 files; ...
=== exit 0 ===
$ git apply --check .../D6Provisional/patch.diff   # against base 43ca0bfb
=== exit 0 ===
$ git apply .../D5Rows/patch.diff && git apply .../D6Provisional/patch.diff
error: patch failed: corpus/knowledge/sibling-overlap-census-round49.md:368
=== exit 1 === (shared EOF hunk; reverse order fails the same way)
$ git apply .../D5Rows/patch.diff && git apply .../D6Provisional/patch-after-D5.diff
=== exit 0 === (both applied; guard exit 0)
$ git apply .../D5Rows/patch-combined-D5-then-D6.diff   # against base
=== exit 0 === (guard exit 0; corpus-integrity verdicts identical to base)
$ # lane working tree state (D5's change already applied), copied into a scratch clone:
$ git apply --check .../D6Provisional/patch-after-D5.diff
=== exit 0 === (applies cleanly to the lane's current two-file state)
$ git apply .../D6Provisional/patch-after-D5.diff && python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md --fleet /home/vgpnk/Projects/shokunin
rows 20 verified 20
province rows 20 matched 20
skill description names 9 of 9 non-none lanes
skill description length 1019 of 1024
=== exit 0 ===
$ grep -n "^## Round 51" corpus/knowledge/sibling-overlap-census-round49.md
372:## Round 51: corrections to the round-50 rulings (append-only)
416:## Round 51 status of the precedence rule (routed D6)
$ python3 -B verifiers/verify_corpus_integrity.py --json   # verdict deltas base->lane+D6: none
=== exit 1 === (4 pre-existing DRIFT, unchanged)
```

## Tooling

No installs or upgrades; nothing was installed. Host tools already present: git, python3, grep, sed,
diff. All writes are in `/fast/scratch/hyaku/kotoba-r51/build/D6Provisional/` (private clone
`lane/`, verification clones `verify_base/`) plus the D5 seat's scratch tree. The lane checkout was
not modified: the only lane write is this report file.

## Report

`.ufo/waves/round-51/build/D6Provisional.md`
