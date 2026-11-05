# Connector r89-w1 — scoped findings (sibling-overlap scan)

Seat: Connector · date 2026-11-05 · read-only scan; details and full quote table in
`.ufo/waves/round-89/w1/Connector/overlap.md`. Headings carry this seat's name only.

## F1 — CONTESTED: S258 duplicates sibling-held source ground (mori S056)

- **Evidence.** kotoba `SOURCE_READY` = "S258 S259"; `w1/ScoutSource.md` resolves S258 to Nosek,
  Ebersole, DeHaven & Mellor 2018, *PNAS* 115(11), DOI `10.1073/pnas.1708274114`, full text fetched at
  `https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/` (HTTP 200; quotes saved). mori
  `corpus/SOURCES.md:62` already holds the same paper: "S056 | Nosek, Ebersole, DeHaven & Mellor (2018),
  'The preregistration revolution' — … (full text via https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/;
  pnas.org HTTP 403 on 2026-10-21) | paper | A | … preregistration as a plan committed before outcomes
  are observed", status mined, used-by `corpus/knowledge/freeze-order-r18.md`, mechanized by
  `tools/mori-freeze-order.py` (mori `PROVINCE.md:564`: "Check whether frozen claim inputs predate their
  implementation commits"). mori's knowledge entry states the principle verbatim:
  "Preregistration separates prediction from postdiction only when the plan is fixed before outcomes are
  seen (S056)."
- **Second holder.** kengaku `PROVINCE.md:61-63` claims the preregistration *standard* for probe
  batteries ("the preregistration standard (hashed predictions + filed power analysis + Brier scoring +
  ordering proof + hermetic replay gate) has no sibling owner"), and its r11 connector referred a
  fleet-wide standard to a protocol lane that never adopted it
  (`corpus/evidence/round11-fleet/r11-connector.md:15`; kengaku `PROVINCE.md:161` "referred round
  11/12–14, not imposed").
- **Not chousa.** `chousa/PROVINCE.md:3-9` owns "claim-vs-source verification; search-strategy taxonomy"
  — no preregistration clause. Preregistration-as-a-source is not chousa's method ground; kotoba's
  standing citation split (`PROVINCE.md:60`, `SKILL.md:12-14`, `QUALITY.md:7-8`) does not cover it.
- **Proposed move (sourcing discipline, no predicate change).** `corpus/knowledge/freeze-gate-round89.md`
  must open its provenance trio with S258 *and* name mori S056 + `freeze-order-r18.md` (and kengaku's
  standard) as held sibling ground — cited, not re-derived, and no "first opening" claim. A lane-local
  S258 row is mechanically fine (each lane keeps its own registry), but the entry that claims the
  principle as newly opened would overstate novelty against a sibling-held row — the same defect family
  as the round's open 55-id assimilation collision. Route to ScribeEntry/L1 before the freeze commit.
  No counter, fixture, floors row or predicate sentence is touched (frozen plan unchanged).

## F2 — CONTESTED: mutation batteries on the new gates sit on tameshi's method ground

- **Evidence.** `tameshi/PROVINCE.md:3-8` declares ownership of "mutation testing, fail-closed arms,
  verdict-line discipline"; Refuses clause: "every lane's gate remains its own; tameshi owns only the
  reusable craft" (`:14-15`). Its two-leg rule — "A guard G is covered by its owning `--selftest` only
  when both hold at the same rev" (pristine green + kill) — and meta-cheat rule ("A selftest case that
  hashes or greps its own source kills every mutant with no behavioural coverage",
  `guard-kill-closure.md:16-25`) are the method behind kotoba's declared C1 battery
  (expectation-flip / control-skip / parse-shortcut mutants; semantics-preserving equivalent survives)
  and the Q47 two-sided scoring. kotoba's own Q57 already credits "tameshi guard-kill/hollow controls
  (`tameshi-shokunin/corpus/knowledge/guard-kill-closure.md:14-29`)" (`corpus/QUALITY.md:68`).
- **Proposed move.** MutTesterGates' battery receipt and the round-89 lesson name tameshi's craft as the
  method source (cite, don't re-derive); any *general* pattern admission routes to tameshi under its
  two-independent-lanes rule. Omitting the credit would repeat the r88 record-correction class
  (count/claim without its artifact). No predicate change.

## F3 — the freeze-refusal ground is NOT unowned: the citation set for `freeze-gate-round89.md`

The gate's knowledge entry should cite these four sibling anchors so the mechanism is positioned as a
successor, not a discovery:

1. **kaidoku criterion 80** (`corpus/QUALITY.md:89`) — mechanism twin: "Control generators and control
   receipts land in the freeze commit, and a control replays at the freeze revision to the receipt's
   verdict." kaidoku also owns the freeze-gate family: `tools/round-30/prefreeze-gate.py`,
   `tools/round-84/freeze-precheck.py`, criteria 33/46/55/79 (`freeze-gate.py` r24/r29,
   `freeze-integrity.py`, `freeze-drift.py`), criteria 83/84 (pre-freeze dry run of the frozen counter
   itself). Refusal grounds differ (data order, pin completeness) — C1's ground (declared control
   expectation not observable) is distinct; say so explicitly.
2. **kagi `corpus/prefreeze-control.sh`** (`SKILL.md:820`, `corpus/README.md:92`, own-work row S088) —
   declared-vs-observed pre-freeze controls gate: `PREFREEZE: CLEAN (controls=N mismatch=0)` /
   `MISMATCH` / `SETUP`. Numeric-extraction variant; same verdict-ladder shape as C1.
3. **mado criterion 110(a)** (`corpus/QUALITY.md:657-661`) — C1's exit-2 arm as a defect class: "a
   command that dies on an argument the instrument does not accept (`rc 2` …) is a freeze defect".
4. **kasegi R22 / M39-1** (`corpus/QUALITY.md:215`; `corpus/lessons/round-39.md:76`) — the r88-F1
   defect class one lane earlier: "r38 C1 frozen unsatisfiable: predicate required 8/8 at J while G2
   required the receipt inside the export", fixed by a pre-freeze satisfiability step. Plus R53
   (two-sided pre-freeze falsification) as the kasegi twin of Q47.

## F4 — honest-limit citation (souji)

`souji/corpus/knowledge/freeze-record-substance-binding.md:45-46`: "it says the receipt's `rev=` predates
the freeze *in history*, not that the control was executed before the freeze in wall-clock time. A commit
made early and measured late satisfies it." Kotoba's C1 *re-executes* declared controls at gate-run time
and compares declared-vs-observed — it closes the observable-expectation gap (r88 F1) but does not prove
wall-clock pre-freeze execution. The entry must scope its claim this way or it overclaims past a named
sibling limit.

## F5 — instance-level leg (C2 D5(iii)) is new ground fleet-wide

No sibling owns a `(name, observed)` tuple gate or instance-non-growth freeze leg. Nearest prior art:
kengaku's fleet-lesson principle "a control must be shown to fail on a witness the frozen population
cannot supply. Instance-level increments only" (`.ufo/waves/round-29/falsify/FConnectPattern.md:192`)
and its r94/r95-adjacent sibling mori's routed item "control-battery-gap" (mori
`corpus/lessons/round-94.md:37`, frozen battery lacking flipping fixtures). The `w_added_instance`
control's do-nothing/discrimination pairing is the concrete instance of kengaku's principle — cite it;
claim no sibling overlap.

## Second-order effects (traced, none harmful)

- **Runtime:** none — scan read bytes only; no sibling command executed.
- **Contract:** all moves are sourcing-discipline routes into the lesson/knowledge entry; the frozen plan
  predicates, targets, controls and kill rules are untouched (ScoutSource's route-correction note and this
  seat's flags both change no predicate sentence).
- **Substrate:** no installs (pacman paused respected; nothing needed). No kernel/host setting requested.
- **Verification surface:** ReviewerFreezeGate can grep `freeze-gate-round89.md` for the F3/F4 citations
  (mori S056, kagi prefreeze-control, mado 110a, kasegi R22, souji wall-clock limit) at the freeze; the
  lesson's Gate can carry the F1/F2 credits.

## Risks

- If ScribeEntry's entry lands citing only S258/S259, the round overstates the principle's newness against
  mori's held row; a cross-lane reviewer may route it as an assimilation/attribution defect beside the
  open 55-id collision question.
- If the battery receipts omit the tameshi credit, Q76-class attribution recurrence.
- If the entry claims wall-clock pre-freeze execution, souji's named limit contradicts it on re-read.

## Verification (commands as run; observed lines quoted in overlap.md)

- Fleet listing: `read /home/vgpnk/Projects/shokunin` → 20 sibling lane dirs + stray `kumitate-shokinin/`.
- Per-lane greps (case-insensitive) over `SKILL.md;PROVINCE.md;QUALITY.md;corpus/**;tools/**;quality/**;
  plans/**;counters/**;census/**;scripts/**` for `freeze[-_ ]?gate|pre[-_ ]freeze|preregist|pre-regist|
  executed before the freeze|instance drift|name, observed|routed[-_ ]repair` — outputs summarized in
  `overlap.md`; every quoted line read verbatim via targeted `read`/`grep`.
- Direct verifications: kaidoku `freeze-precheck.py:1` + `prefreeze-gate.py:1` docstrings; kagi
  `SKILL.md:820` + `corpus/README.md:92`; mori `SOURCES.md:62` + `freeze-order-r18.md:1-10` +
  `PROVINCE.md:564,590-591`; chousa `PROVINCE.md:3-9` + `SKILL.md:84`; tameshi `PROVINCE.md:3-15` +
  `guard-kill-closure.md:14-29`; kengaku `PROVINCE.md:61-63,161` + `corpus/evidence/round11-fleet/
  r11-connector.md:15` + `corpus/QUALITY.md:167`; kasegi `QUALITY.md:215,393,477` + glob
  `corpus/instruments/r4{4,5,7}-routed-defects.py`; kumitate glob `scripts/routed-ledger.mjs`; kaidoku
  `SKILL.md:1034`; kotoba `SOURCE_READY` + `ScoutSource.md` + `SKILL.md:12-14` + `PROVINCE.md:60,77` +
  `corpus/QUALITY.md:7-8,68`.
- Negatives confirmed: revenger/lore/game-dev-2d/game-dev-3d/audio (no grounds; lore's `dependency_freeze`
  gate is its own canon domain), `kumitate-shokinin/` stray (0 hits), no S258/S259 rows yet in kotoba
  `corpus/SOURCES.md` at scan time.
