# ConnSibling2 — kotoba round 65 wave 1

role: connector (leaf — no subagent dispatch)
item: sibling-overlap scan of `corpus/knowledge/g7-span-closure-round65.md`, `corpus/lessons/round-65.md`, and the SCORECARD round-65 annotation
judged on: adjacency
tools installed: none (python3 stdlib already present; pacman paused; no install required)
production edits: none (this file only)

Axes named: **adjacency** (this seat). The bound below must not move **depth** (C1, 234 assertions, floors row, kill conjunct) or **consistency** (C2, `governance.citation_resolves`, checklist 1862, `GOVERNANCE_CORRECTIONS`).

## What the mandated command actually prints

The instrument does not emit `STRICT_HITS`. Without a census file it is a usage error.

```text
$ python3 -B verifiers/check_sibling_census.py --province /home/vgpnk/Projects/shokunin/kotoba-shokunin/PROVINCE.md
usage: check_sibling_census.py CENSUS.md [--fleet DIR] [--province PROVINCE.md] [--skill SKILL.md]
EXIT:2
```

The command `PROVINCE.md:40` itself names, with the round-49 census file, re-checks pinned rows. It does not read the three round-65 artifacts.

```text
$ python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province /home/vgpnk/Projects/shokunin/kotoba-shokunin/PROVINCE.md
rows 20 verified 20
province rows 20 matched 20
EXIT:0
```

`STRICT_HITS` below is the round-63/66 semantic count: an `**Owns:**` / `**Domain:**` / `**Refuses:**` line, or a province boundary-table cell, that claims one of this round's new items. A string hit that is not that claim is not strict. Exit 0 of the census guard is not that count.

## Strict scan

Live tree, read-only, 2026-10-24. Not the round-49 pins. Home lane excluded.

Items: (1) G7 span closure on this lane's `span_missing` branch (SPAN_FIRST / SPAN_LAST, M20, M11-exact-case, the v32 floors row); (2) `GOVERNANCE_CORRECTIONS` / `governance.citation_resolves` on this lane's own LOG and SCORECARD cells.

```text
LANE_COUNT 20
SIBLING_FILES 38
MISSING
audio-shokunin/SKILL.md
game-dev-2d-shokunin/SKILL.md
aggregator-shokunin: ABSENT
--- BOUNDARY HITS ---
PROSE	tameshi-shokunin/SKILL.md:2115	equivalent mutant	hermetic witness each; `S_EMPTY_GUARD` is an equivalent mutant (no input can
BOUNDARY_NEAREST 1
BOUNDARY_STRICT 0
STRICT_HITS 0
```

Lanes: audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotodama, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi. Pattern on all 38 files: `span_missing`, `SPAN_FIRST`, `SPAN_LAST`, `g7_conjunct`, `g7-span`, `GOVERNANCE_CORRECTIONS`, `citation_resolves`, `JudyDiffOp`, `Madeyski`, `equivalent mutant`, `second-order mutation`, `check_scoped_rules_v32`, `page_words`, `fixture-hermeticity`, `self-referential citation`. The one nearest line is tameshi's own round-26 case (`S_EMPTY_GUARD` on kumitate `cite-check`), not a claim on either item.

`PROVINCE.md` in this lane has zero matches for `span_missing`, `GOVERNANCE_CORRECTION`, `g7-span`, `second-order`, `JudyDiffOp`, or `Madeyski`. The new ground is not registered in Core. That is an unregistered surface, not a sibling claim.

SCORECARD line 381 (the round-65 annotation) names the 234-assertion predicate, the floors row, and `GOVERNANCE_CORRECTIONS`. It names no sibling domain. The lesson's Gate records S121's access and says the publisher record was not opened. Neither file is a scope claim another lane owns.

**STRICT_HITS 0.** No sibling boundary file claims the span-closure arms or the governance-correction mechanism.

## The statement that does cross

`corpus/knowledge/g7-span-closure-round65.md` (the two-span bullet) and SOURCES S121's scope cell both say the coupled honest-plus-fabricated cell is a first-class adequacy witness, not an artificial one, because S121 measured second-order mutation as reducing equivalent mutants and test effort.

That subject is tameshi's method, not this lane's gate:

- `tameshi-shokunin/PROVINCE.md:3-5` Domain is verification-fixture craft: hermetic suites, mutation testing, fail-closed arms.
- `tameshi-shokunin/PROVINCE.md:14-17` Refuses product domains: every lane's gate remains its own; tameshi owns only the reusable craft.
- The same PDF was already opened there. `tameshi-shokunin/.ufo/waves/round-26/w1/OpenEquivalentSource.md:34-41`: URL `https://madeyski.e-informatyka.pl/download/Madeyski13TSE.pdf`, preprint v.2, DOI `10.1109/TSE.2013.44`, publisher text not opened, tier therefore B (2026-10-22). The L1 then left it unmined: `tameshi-shokunin/corpus/SOURCES.md:346-347` and `corpus/lessons/round-26.md:63-64` ("tier B and not needed"; Stryker S089 was mined instead).

Kotoba S121 is that URL, mined 2026-10-24, tier A, scope cell: "Primary peer-reviewed study" and "a witness carrying an honest span beside a fabricated span is a first-class adequacy check, not an artificial one." The same cell's anchor, and `corpus/lessons/round-65.md` Gate, say the artifact opened is the author-hosted preprint and the publisher record was not opened. Byte identity with tameshi's 2026-10-22 fetch was not re-measured here; the shared identity is the URL, the preprint-v.2 header, and the DOI. [INFERENCE] same document, not proven same bytes.

The opened snapshot does not say what the scope cell says:

- `S121.txt:98` uses "artificial" for the seeded fault ("induces artificial faults"), not as a warrant that a mixed citation cell is non-artificial.
- `S121.txt:1114-1116` does support a reduction in equivalent mutants and in test effort, for second-order mutants of program operators.
- `S121.txt:1174-1176` (the lesson's support quote) is Polo et al. on about 50% fewer mutants, not a citation-span result. That quote matches.
- `S121.txt:2362-2363` records the opposite adequacy cost: second-order mutants could be easier to kill.
- `S121.txt:2779-2785` records the hiding caveat: the reduction may only hide equivalent mutants behind killable mutants, and may not be cost effective.

SPAN_FIRST / SPAN_LAST couple one honest backticked span and one fabricated span so this lane's branch cannot inspect only one of them. S121 couples two first-order mutants of program operators (Last2First, JudyDiffOp, RandomMix, NeighPair). The SOURCES cell already says the two-span arm is the lane's application, not the paper's object — and, in the same cell, calls that arm a first-class adequacy check. Those two clauses cannot both be the paper's result.

The arms themselves stay on this lane's gate, which tameshi's refusal already leaves here. The adequacy sentence does not.

## Contradictions (not smoothed)

1. `STRICT_HITS 0` and "the S121 sentence sits on tameshi's method" are both true. The first is about sibling Owns lines. The second is about a sentence this lane wrote. Collapsing them into "no overlap" hides the absorption.
2. Census exit 0 (`rows 20 verified 20`) and the usage exit 2 are both true. Neither is `STRICT_HITS`. The guard never opens the three round-65 artifacts.
3. The lesson says the publisher record was not opened. The S121 scope cell says "Primary peer-reviewed study" at tier A. Tameshi, on the same URL, recorded tier B for that reason and did not mine the row. The tier letters are each lane's own column; they are not one measurement. This report does not retier the row.
4. Chousa `PROVINCE.md:5-6` owns source hierarchy and claim-vs-source as research method. Kotoba `PROVINCE.md:49` says cite that method, never re-derive it. The tier-letter clash is the nearest chousa reading and is not a strict hit: no chousa line names S121, span closure, or `GOVERNANCE_CORRECTIONS`. Treating chousa as the owner of this lane's SOURCES column would re-derive the research method.
5. `GOVERNANCE_CORRECTIONS`, M99's `errata=()` pin, and M100's quoted-not-backticked notices are this checker's own fixture and scanner. They are not chousa's hop and not tameshi's mutation method. The nearest tameshi line (`SKILL.md:2115`) classifies a kumitate survivor. It does not claim these arms.

## Proposed move (one, not applied)

Append one paragraph to the existing `## Limits` section of `corpus/knowledge/g7-span-closure-round65.md`. Do not edit the design-source bullet in place, the S121 row, the 234-assertion suite, the floors row, or `GOVERNANCE_CORRECTIONS`. No new corpus file. No backtick, no `.ufo/` token, and no commit hash in the paragraph (those move other gates).

```text
Sibling bound (2026-10-24): 38 sibling SKILL.md and PROVINCE.md files, strict ownership hits 0 on the span-closure arms and on GOVERNANCE_CORRECTIONS. Those arms pin only this lane's span branch. S121's opened preprint measures second-order mutants of program operators. It records an equivalent-mutant reduction and a test-time reduction, and also a mutation-score cost and the caveat that the reduction may only hide equivalents behind killable mutants. Equivalent-mutant classification stays tameshi's method; tameshi opened this same preprint on 2026-10-22 and left it unmined. The honest-span-plus-fabricated-span cell is this lane's pin, not that paper's adequacy result.
```

That keeps the pins and the citation, and stops the entry from absorbing the mutation method the adjacent lane already refused to take from this PDF.

## Risks

- Rewriting the S121 scope cell in place to "fix" tier A would repeat the round-64 teaches-cell breach. The append does not touch SOURCES.
- Editing `PROVINCE.md` to register span closure in the same change would reopen the round-63 Core bullet and is not this move.
- Reading tameshi `PROVINCE.md:3-5` as owning the kill arms would hand this lane's gate away. The Refuses line forbids that reading; the arms stay.
- Reading chousa's source-hierarchy sentence as a veto on mining S121 would un-mine a row the lesson already opened. The contest is the adequacy gloss, not the snapshot.
- A backticked path or a hex commit inside the appended paragraph can move `governance.citation_resolves` or the corpus-integrity commit vector. The paragraph above has neither.

## Verification (for the L1; not run as a production edit)

1. Re-run the 38-file sweep. Expect `STRICT_HITS 0`, `aggregator-shokunin: ABSENT`, missing `audio-shokunin/SKILL.md` and `game-dev-2d-shokunin/SKILL.md`, and the single nearest line at `tameshi-shokunin/SKILL.md:2115`.
2. Re-run the census guard with the census file. Expect `rows 20 verified 20`, `province rows 20 matched 20`, exit 0. The no-census invocation remains exit 2. Do not report either as `STRICT_HITS`.
3. If the paragraph is appended, `python3 -B verifiers/check_scoped_rules_v32.py --self-test` must still print `0 failure(s) over 234 assertions`, exit 0, and `python3 -B verifiers/verify_skill_checklist.py --json` must still print `"fail": 0`, exit 0. Do not treat this report as that measurement.
