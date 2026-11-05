# Round 90 — kotoba (Linux host, omp 18.15.0): lesson

Author: **ScribeCorpus** (scribe seat). This file is the round-90 **scaffold**: the Gate record, the Mistakes
row and the Considerthese entry below are written; **the L1 completes the settlement** (the seat record, the
claim verdicts, the wave disposition and the final numbers).
Round: 90, plan `plans/round-90.md` (frozen at `6af71591e7232a7eebbaff78e7db653a70c7218b`), base
`0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5`, freeze entry at `6fa5bb6d4ceeb51f0455e512a52d8b75628f404c`.
Pre-data controls: `plans/round-90-controls.md`, executed before any candidate score — receipt
`.ufo/waves/round-90/receipts/freeze-gate-r90.txt` (`freeze gate: 6 control(s) held`, exit 0).

## Gate

Candidates considered, with the decision and the reason:

- **S260** — Stryker Mutator documentation, "Mutant states and metrics"
  (`https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/`) and its sibling
  page "Equivalent mutants"
  (`https://stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants/`). **Admitted** as tier A,
  scoped to the mutation-testing vocabulary and metric definitions as the mutation-testing tool's own
  documentation states them (killed / survived / mutation score / equivalent mutant) — **not** this lane's
  battery mechanics. Access date 2026-11-05; HTTP 200; 27068 B and 38687 B; the sha256 digests are
  fetch-time metadata only (r89 spot-check note 1: ground external quotes in line anchors + size + title).
  Located quote, HTML line 12 of the primary snapshot (`wc -w` = 15): "When at least one test failed while
  this mutant was active, the mutant is killed." Second located quote, HTML line 14 (`wc -w` = 12): "When all
  tests passed while this mutant was active, the mutant survived." Third, HTML line 52 (`wc -w` = 12): "The
  total percentage of mutants that were detected. The higher, the better!" Fourth, the score formula at
  HTML line 51 (`wc -w` = 5): "detected / valid * 100". Fifth, the equivalent-mutant notion on the sibling
  page, HTML line 16 (`wc -w` = 17): "It is called equivalent mutant. There is no definitive way for Stryker to
  find and ignore them." (byte-shaped: the `<em>`/`</em>` tags removed, no word altered). Row written to
  `corpus/SOURCES.md`; cited by `corpus/knowledge/mutation-battery-round90.md`.
  - **S260 route (a)** — `https://mutmut.readthedocs.io/en/latest/` (mutmut docs index). **Rejected as the
    S260 support, not for access**: HTTP 200, 51074 B, and it grounds the killed/survived vocabulary, but it
    cannot ground leg (ii) — `grep -niE 'equiv'` finds no match, and the only "mutation score" mention is a
    `mutmut badge` / `export-cicd-stats` command pair, not a definition. **Flip:** if mutmut's docs gain a
    glossary naming equivalent mutants and the score formula, mutmut becomes a valid second tier-A source and
    this rejection flips to "admitted".
  - **S260 route (a′)** — the mutmut "How it works" / glossary subpages
    (`https://mutmut.readthedocs.io/en/{latest,2.4.0,3.0.0}/{howitworks,glossary,how-it-works,usage,mutations}.html`,
    15 probes). **Rejected: route absent** — all 15 answer HTTP 404, because the Sphinx build has exactly one
    document (`en/latest/searchindex.js` → `docnames: ['index']`). **Flip:** re-probe when mutmut publishes a
    glossary page.
  - **S260 route (a″)** — the mutmut repo README (the source of the same docs text), HTTP 200, 22381 B.
    **Corroboration of route (a)**, not a separate row: `docs/index.rst` is
    `.. include:: ../README.rst`, so the readthedocs page and the repo RST carry the same sentences at the
    same line numbers (README lines 617–618 ≡ index lines 537–538).
  - **S260 rejected route 1** — the ACM DL DOI landing
    `https://dl.acm.org/doi/10.1145/2382577.2382594`: **HTTP 403**, 5471 B, body title "Just a moment..."
    (Cloudflare JS/cookie challenge). **Rejected** — the peer-reviewed route is not readable without a JS
    challenge, so no quote may be taken from bytes that are not the article. **Flip:** re-open the same DOI
    through an institutional or open-access mirror (or the publisher's PDF endpoint) and re-judge if the
    article's own wording is needed for the equivalent-mutant definition.
  - **S260 rejected route 2** — Wikipedia "Mutation testing"
    (`https://en.wikipedia.org/wiki/Mutation_testing`): **HTTP 200**, 170845 B. **Rejected as sole support** —
    encyclopedia text is C-tier, a lead to the underlying papers, and the S260 claim is tier-A-scoped, so
    Wikipedia may not back it. **Flip:** it stays a lead; if a named paper is cited from its reference list,
    re-open that paper directly.
  - **S260 route (b)** — `https://stryker-mutator.io/docs/` (the docs entry page): HTTP 200, 30253 B.
    **Corroboration, not the row**: it carries the same two terms in one sentence at line 5 ("If your tests
    fail then the mutant is killed. If your tests passed, the mutant survived.") and links to the two pages
    the row anchors on.
- **S261** — own-work, the round-89 mutant matrix record:
  `git show 0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5:.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`
  (sha256 `bba3a5c0506274df8099beed7950af92805e80ac3459d5cd4ac1341de362e1cc`; 14 mutant rows over the two
  round-89 gate instruments — 8 freeze-gate, 6 D5 v3 — each row carrying the observed exit before and after
  the mutation; 13 rows killed, 1 row recorded SURVIVED, `d5-m1a-d5iii-leg-only`). **Admitted** as own-work,
  tier A, scoped to the r89 mutant matrix record. It is the prior round's own evidence for the battery's
  three classes: it shows a kill set, a recorded survivor and per-row exit flips, so the round-90 manifest's
  classes are ported from a measured matrix rather than asserted. Cited by
  `corpus/knowledge/mutation-battery-round90.md`.

**Census before → after.** Rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ **185** before this round (receipt `.ufo/waves/round-90/receipts/census-before-rows.txt`) and **187** after
(the two rows above). Validation: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate
--root /home/vgpnk/Projects/shokunin kotoba` → exit **0**, `kotoba ok`, with the same 33 pre-existing W04
duplicate-URL warnings and no E-code. Every row carries 13 pipe-delimited fields, no duplicate id, and the
kind/tier/status enums check clean.

**Assimilation: none.** The package at `/home/vgpnk/Projects/shokuknow/merge/kotoba/` (read-only) was not
adopted: its id space collides with the lane registry and the renumber-or-retire ruling is still open
(L0 `kotoba | round-88`). The 55 collisions measured in round 89 stand as measured (`.ufo/waves/round-89/
assimilation/collisions`, 55 lines). No row was appended from the package.

**Considerthese** (`considerthese/2026-10-26.md`, proposals only; read, not acted on beyond the one mined
below) — see § Considerthese.

Spot-check result: **pending** — the non-author closure samples one admit and one reject from this gate.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `number-drift`/`landing`: a floors-registry row landed without the guard tables and the `instrument_total` bump — the r89 freeze added the `freeze_gate` row to `verifiers/floors-registry.json` (19 entries) while `instrument_total` stayed 18 and neither guard table learned the row, so the guard read two reds at the round-90 base | `.ufo/waves/round-90/receipts/base-floors.txt` — `FAIL registry size drift: instrument_total=18 but 19 entries in verifiers/floors-registry.json` and `FAIL registry row vanish: freeze_gate (listed in verifiers/floors-registry.json, absent from both guard tables)`, rc=2; the half-bump state is visible at the r89 freeze revision `39704ad` (`git show 39704ad:verifiers/floors-registry.json` → `instrument_total` 18, 19 entries, `freeze_gate` present; `git show 39704ad:verifiers/check_assertion_floors.py` → 0 occurrences of `freeze_gate`) | the registry's own **BUMP-IN-STEP RULE** (stated in `verifiers/floors-registry.json`'s `$comment`: "when a row's floor moves, edit this file, both in-file tables and the guard docstring in the same change; a half-bump now fails loudly") **and** the guard anchor — `verifiers/floors-registry.json` is the anchor OUTSIDE the edited file, so the two-table disagreement was named by the guard itself rather than by a reviewer | the completed bump, in ONE change (ExecFloorsBump): `instrument_total` 18 → 19, the `freeze_gate` row into both guard tables (`EXPECTED_INSTRUMENTS` and `INSTRUMENTS`), the F6 self-test literal `'"instrument_total": 18'` → `'"instrument_total": 19'`, and the module docstring — plus the **half-bump regression arm**: the guard's own F6 arm and the scratch rebuild of the pre-bump tree (receipt `.ufo/waves/round-90/receipts/floors-regression.txt`) read the same two FAIL lines byte-for-byte, rc=2, so the fix is shown able to fail. The completed guard self-test reads `0 failure(s) over 165 assertions`, exit 0 (receipt `.ufo/waves/round-90/receipts/floors-selftest.txt`) |

Found in the wave and settled before any scored reading (routed defects, not repaired into frozen bytes):

- **The survivor-class row did not hold at the final bytes (settled by addendum A1).** The r89 matrix (S261)
  records `d5-m1a-d5iii-leg-only` as SURVIVED, but at the final bytes it flips both frozen D5 probes, so the
  measured line read `killed 13 of 13 …; disclosed survivors 0 of 1`. The r89 anchor `if not grew:` is absent
  from the revision bytes (the d5iii condition is `if not grew and not added:`). Resolved by
  `plans/round-90-addendum-1.md` A1: the row moves to `kill` before any scored reading, and the minimum pins
  M >= 8, E >= 4 enter the predicate. Evidence: `.ufo/waves/round-90/w1/ExecBattery.md` finding 1–2.
- **Curator note for the r89 record (append-only; no r89 file rewritten).** The r89 `SURVIVED` entry for
  `d5-m1a` was measured against an earlier revision whose anchor no longer exists; the r89 matrix is kept as
  filed and this row supersedes its classification for round 90 only.
- **The battery's own guard self-test has three surviving mutants** (wave seat MutTesterBattery,
  `.ufo/waves/round-90/w1/MutTesterBattery/mutants.tsv`): G1 commit-check skipped (`mb-m2`), G1 scratch
  clean-tree guard off (`mb-m15`), and revision-copy restore not re-read after each mutant (`mb-m16`). The
  frozen predicate does not measure these guards (it measures the two gates' probes), so they are disclosed
  as bounds in the knowledge entry and not counted in the predicate. The 19-assertion self-test was
  extended with five real fixture kills to reach the M >= 8 pin; the three survivors are not yet covered by
  an arm (routed to round 91, no repair here).
- **The G3 registry row is the L1's landing act.** Until `SKILL.md` names `check_mutation_battery.py` (landed in
  this round's commit), the frozen predicate exits 1 with `G3 registry presence FAIL`.
- **The pre-existing child-cap drift** reported by ExecFloorsBump (finding 1): the bare live guard walk can read
  exit 2 on an idle host because `verify_harness_independent.py --self-test` takes ~167 s against a flat 120 s
  cap. Not caused by the r90 bump; routed to the L1 as a host-load-dependent false red.

## Considerthese

`considerthese/2026-10-26.md` was read (proposals only; not acted on beyond the one mined below).

- **Proposal 5 → Q82 (mined this round).** "Evidence growth needs a budget … A per-round evidence cap, or
  compressing seat logs after closure, would keep clones and connector reads cheap." Mined as QUALITY criterion
  **Q82**, appended to `corpus/QUALITY.md`: a per-round wave-evidence byte budget measured at landing with
  `du -sb` of the round's wave tree, stated in the round report beside its date, compared with the two prior
  rounds, and — for a bundle over the stated budget — the oversized artifact named together with the claim it
  serves. Q82 extends Q11 and M15 and rewrites neither. Fix shown able to fail: the measurement command
  appears in this lesson (`du -sb .ufo/waves/round-90/`, read 2026-11-05) and not in the round-89 lesson.
- **Proposal 3 (carried, not landed).** Land the page round 74 rejected and use it on the skill's own
  description. Still needs the description self-audit round shape; out of this round's claim scope.
- **Proposal 4 (carried, not landed).** Do not close a round before its falsify wave runs. Answered
  structurally by this round's Q47 two-sided battery (the equivalent class is generated at measurement time),
  and it stays a shape rule for the rounds that have no mutation-tester seat.

## Sources

- **S260** — Stryker Mutator documentation, "Mutant states and metrics" and "Equivalent mutants";
  URLs `https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/` and
  `https://stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants/`; access 2026-11-05; HTTP 200;
  27068 B and 38687 B; located quotes at HTML lines 12, 14, 51, 52 and 16 (above). Tier A scoped. Status
  `queued`; used-by `corpus/knowledge/mutation-battery-round90.md`. The row is in `corpus/SOURCES.md`.
- **S261** — own-work; locator `git show 0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5:.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`;
  sha256 `bba3a5c0506274df8099beed7950af92805e80ac3459d5cd4ac1341de362e1cc`; 14 rows, 13 killed, 1 recorded
  SURVIVED. Tier A scoped. Status `queued`; used-by `corpus/knowledge/mutation-battery-round90.md`.

## Assimilation: none

See § Gate. The r89 collision count (55) stands; adoption is L0-blocked on `kotoba | round-88`.

## Seat record (this round)

*(placeholder — the L1 completes: the seat ledger for wave `r90-w1`, the claim verdicts for C1 and C2, the
landing measurements, and the closure status.)*
