verdict: HOLDS — round-47 governance additions resolve canonically; plain-clone failure is the unchanged 24-subject fleet dependency, not new round-47 fragility

## Scope and axes

Attacked LOG/SCORECARD path growth and the C3 governance-PASS claim at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`, versus BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Axes: freshness (correct HEAD/BASE attribution), operability (canonical versus plain checkout), calibration (what PASS and token counts actually establish). This is lane-authored review, not admission or closure.

## 1. Count actual additions, not retained citations on replaced lines

Using the gate's own `citation_subjects(..., exclude_quoted=True, exclude_schematic=True)` and token multisets per file:

| File | BASE raw subjects | HEAD raw subjects | Added occurrences | Removed occurrences | Newly introduced distinct token spellings in that file |
|---|---:|---:|---:|---:|---:|
| LOG.md | 589 | 622 | 33 | 0 | 15 |
| SCORECARD.md | 216 | 227 | 11 | 0 | 3 |
| Total | 805 | 849 | 44 | 0 | — |

The three novel SCORECARD spellings already appear among LOG's 15 novel spellings: `.ufo/waves/round-47/before/SUMMARY.md`, `.ufo/waves/round-47/build/C2CriticRule.md`, `corpus/lessons/round-47.md`. Thus 15 spellings are new across the pair. All 44 added subject occurrences resolve in both HEAD layouts.

Anchors: LOG additions `LOG.md:2319-2326`; modified score rows `SCORECARD.md:31-33`; appended recap `SCORECARD.md:106`. The raw HEAD total 849 becomes 848 evaluated subjects after the pinned absence exemption (`verifiers/verify_skill_checklist.py:1570-1574`). Quoted/schematic exclusions remain 9/3.

**Counting counterexample:** counting every citation on added diff lines produces 59 occurrences (33 LOG + 26 SCORECARD), but 15 SCORECARD occurrences were carried forward from replaced lines. In particular, `SCORECARD.md:31` contains `../.ufo/reports/round-16/kotoba.md` in both BASE and HEAD at line 31. Calling that a new round-47 nonportable citation is false. A line-text-keyed comparison also reports these retained tokens as new; compare normalized token multisets instead.

These are governance-eligible backtick path subjects, not every backtick or every possible repository pathname. The closed root vocabulary intentionally excludes, for example, `plans/round-47.md` at `LOG.md:2319`; glob-bearing `verifiers/fixtures/checklist/xml-tag-*` at `LOG.md:2322` is also excluded. Do not represent 44 as an unrestricted lexical count of all paths.

## 2. Strongest layout counterexample: plain checkout is red, already before this round

Commands exercised concurrently, each from the stated clone's `kotoba-shokunin/` directory:

`python3 -B verifiers/verify_skill_checklist.py --json`

| Clone parent under `/fast/scratch/kotoba-r47/w2/` | Revision | Process exit | Governance result |
|---|---|---:|---|
| W2GovSurfaces | HEAD | 0 | PASS, evaluated 848; 9 quoted, 3 schematic, 1 absence excused |
| W2GovSurfacesPlain | HEAD | 1 | FAIL, evaluated 848; 24 unresolved fleet subjects |
| W2GovSurfacesBase | BASE | 1 | FAIL, evaluated 805; only LOG.md:2111's recorded-absent runner |
| W2GovSurfacesBasePlain | BASE | 1 | FAIL, evaluated 805; same 24 fleet subjects plus LOG.md:2111 |

`git rev-parse HEAD` exited 0 in all four and returned the revisions above. The HEAD canonical gate detail was exactly: `848 governance citation token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused`.

The HEAD plain failure begins `LOG.md:177: '../.ufo/reports/round-9/kotoba.md' does not resolve ...`, followed by lines 255, 311, 779 and `(+20 more)`. The independent enumeration below recovers all 24, rather than assuming that truncated diagnostic identifies them. It finds 13 distinct spellings. BASE and HEAD have **identical `(source file, ../token)` multisets**, 9 LOG subjects plus 15 SCORECARD subjects. No new `../` dependency landed.

### All HEAD subjects that die without fleet siblings

| HEAD source location(s) | Token |
|---|---|
| LOG.md:177 | `../.ufo/reports/round-9/kotoba.md` |
| LOG.md:255 | `../.ufo/reports/round-11/kotoba.md` |
| LOG.md:311; SCORECARD.md:5 | `../PROTOCOL.md` |
| LOG.md:779,1221; SCORECARD.md:15,34,148 | `../.ufo/l0-questions.md` |
| LOG.md:824; SCORECARD.md:34 | `../kasegi-shokunin/corpus/instruments/resolve.py` |
| LOG.md:824; SCORECARD.md:34 | `../kasegi-shokunin/corpus/instruments/anchorcheck.py` |
| LOG.md:974 | `../.ufo/waves/shokunin12h-20261014-p1-repair/members/` |
| LOG.md:1203; SCORECARD.md:100,127,244 | `../AXES.md` |
| SCORECARD.md:3 | `../MISSION.md` |
| SCORECARD.md:5 | `../SCORECARD.md` |
| SCORECARD.md:31 | `../.ufo/reports/round-16/kotoba.md` |
| SCORECARD.md:34 | `../kasegi-shokunin/corpus/instruments/` |
| SCORECARD.md:137 (twice) | `../.ufo` |

Raw dead-subject enumeration also finds `.ufo/round-45/drafts/v10/post-r44-hunt.py` at `LOG.md:2111` in both HEAD layouts. It is not a 25th layout regression: it is the deliberately absent, now-excused erratum. `trigger.citation_resolves` separately fails in HEAD plain on `SKILL.md:518`, `../.ufo/reports/round-7/kotoba.md` (BASE: line 515); this is not included in the governance count.

The resolver explicitly supports ancestor-relative fleet citations (`verifiers/verify_skill_checklist.py:1360-1383`); the governance check uses it for every unexcused subject (`:1584-1593`). This is an observable pre-existing deployment constraint, not evidence that round 47 silently weakened the gate.

## Reproduction and commands

Saved executable-as-Python census source: `.ufo/waves/round-47/falsify/W2GovSurfaces.repro.txt`.

Run:

```
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/W2GovSurfaces.repro.txt /fast/scratch/kotoba-r47/w2/W2GovSurfaces/kotoba-shokunin
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/W2GovSurfaces.repro.txt /fast/scratch/kotoba-r47/w2/W2GovSurfacesPlain/kotoba-shokunin
```

Both census processes exited 0 (completed enumeration, **not** a gate PASS). Their embedded governance results were respectively PASS/848 and FAIL/848, `same_dotdot_multiset: true`, and 44 added occurrences in each. The census loads HEAD's extractor and reads both revisions with `git show`, which exited 0 through `check=True`. It lists all unresolved raw subjects, including the separately excused erratum.

To reproduce the counterexample independently, clone the pinned revision into an empty parent without sibling symlinks and run the checklist command there; compare with the assignment's canonical-layout symlink recipe. No production file mutation is needed. These four prepared scratch clones were available and used; no fleet-sibling files were changed.

## Smallest safe correction / disposition

No code correction is supported by this attack. Preserve canonical-layout qualification when reporting the gate's PASS; do not reinterpret it as standalone-clone portability or source-content authentication. Preserve the 44-occurrence versus 59-added-line distinction in any census. Suppressing `../` failures, quoting live citations, or extending errata would conceal the dependency rather than fix it. A standalone-portability requirement would be separate scope and needs explicit treatment of these 24 pre-existing subjects, not a round-47 regression attribution.

## Not checked

Did not re-derive binary loaders, npm lineage, XML-tag rules, corpus or fault-harness mutations, C3 erratum tamper resistance, citation content support, source rows, or other frontier claims; those are outside this assigned LOG/SCORECARD layout scan. No full verification battery, installs/updates, subagents, sessions, or production edits were performed. Only the checklist/gate and census commands reported above were exercised in this review. Historical numerical claims elsewhere in LOG/SCORECARD are not independently certified by this result.
