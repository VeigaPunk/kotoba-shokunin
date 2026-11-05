# Connector r89-w1 — sibling-overlap scan: freeze gate / instance drift / preregistration grounds

Seat: Connector (read-only over sibling lanes; writes only this file, `../Connector.md`, `../CONNECTOR_READY`).
Date: 2026-11-05. Scope: every sibling lane repo under `/home/vgpnk/Projects/shokunin/<id>-shokunin`
except kotoba itself — 20 dirs scanned (`kengaku, kasegi, kama, kaidoku, kumitate, kake, kotodama, mado,
tameshi, mori, tsukuroi, chousa, souji, kagi, tabi, revenger, lore, game-dev-2d, game-dev-3d, audio`) plus
the stray dir `kumitate-shokinin/` (0 hits; a misnamed copy, not an active lane).

Method: case-insensitive regex greps over durable surfaces (`SKILL.md`, `PROVINCE.md`, `QUALITY.md`,
`corpus/**`, `tools/**`, `quality/**`, `plans/**`, `counters/**`, `census/**`, `scripts/**`) for
`freeze[-_ ]?gate | pre[-_ ]freeze | preregist | pre-regist | executed before the freeze | instance drift |
name, observed | routed[-_ ]repair`, then targeted `grep`/`read` of every instrument a hit names.
Quotes are verbatim, ≤ 25 words, path:line anchored in the sibling's own working tree at scan time.
No sibling file was executed or written; no git/jj write anywhere.

Classification: **owns** = the sibling's own instrument or criterion does this ground; **adjacent-owns** =
own instrument on a neighbouring ground; **cites/practices** = follows the discipline without a general
instrument; **no ground** = no hit beyond false-positive senses.

## Ground A — freeze gate / freeze refusal (kotoba C1 `check_freeze_gate.py`)

| lane | hit | classification | quote |
|---|---|---|---|
| kaidoku | `tools/round-30/prefreeze-gate.py:1` | owns (data-order refusal ground) | "Round-30 pre-freeze gate: round-29 routed defect 3 (M29-3) as an exit-code check." |
| kaidoku | `tools/round-84/freeze-precheck.py:1` | owns (claim-metadata pin ground) | "Round-84 prefreeze claim-metadata gate: a claim names its counter, the container pins it." |
| kaidoku | `corpus/QUALITY.md:43` (crit 33) | owns (criterion + r24 gate) | "the freeze commit is the one that first adds `claims.json`" … "instrument absent at freeze is a finding, never a clean freeze" |
| kaidoku | `corpus/QUALITY.md:46` (crit 46) | owns | "`tools/round-29/freeze-gate.py` audits 19 freezes" |
| kaidoku | `corpus/QUALITY.md:89` (crit 80) | owns — mechanism twin of C1 | "Control generators and control receipts land in the freeze commit, and a control replays at the freeze revision" |
| kaidoku | `corpus/QUALITY.md:91-92` (crit 83/84) | owns (pre-freeze dry run) | "The pre-freeze dry run runs the **frozen counter itself** (not a stand-in scorer) on every claim" |
| kagi | `SKILL.md:820` (`corpus/prefreeze-control.sh`) | owns (declared-vs-observed controls gate) | "`0` `PREFREEZE: CLEAN (controls=N mismatch=0)`; `1` `PREFREEZE: MISMATCH (controls=N mismatch=M)`" |
| kagi | `corpus/README.md:92` | owns | "Revision-extracted numeric declarations; round35 accepts one nonempty unsigned-integer stdout line, no stderr" |
| kagi | `corpus/SOURCES.md:95` (S088) | owns (own-work source row) | "Own-work pre-freeze control source … shipped numeric BASE-control implementation" |
| mori | `corpus/knowledge/freeze-order-r18.md:7` | owns (principle mechanized) | "Preregistration separates prediction from postdiction only when the plan is fixed before outcomes are seen" |
| mori | `PROVINCE.md:564` | owns | "`tools/mori-freeze-order.py` … Check whether frozen claim inputs predate their implementation commits." |
| mado | `corpus/QUALITY.md:657-661` (crit 110a) | owns — closest criterion to C1's exit-2 arm | "a command that dies on an argument the instrument does not accept (`rc 2`, "unrecognized arguments") is a freeze defect" |
| kama | `corpus/QUALITY.md:379` (KQ64) | owns | "Every freeze file passes `python3 tools/prereg-time-check.py …` (exit 0) before the freeze is cited." |
| kama | `corpus/QUALITY.md:283` (KQ38) | owns (pre-freeze control call) | "A non-author pre-freeze control call, dispatched by the L1 before any data-collecting seat runs" |
| souji | `corpus/knowledge/freeze-record-substance-binding.md:45-46` | owns (named limit C1 must not overclaim past) | "it says the receipt's `rev=` predates the freeze *in history*, not that the control was executed before the freeze in wall-clock time" |
| kasegi | `corpus/QUALITY.md:215` (R22 block) | owns (pre-freeze satisfiability) | "Round-34 additions — pre-freeze satisfiability and reflection cadence" |
| kasegi | `corpus/lessons/round-39.md:76` (M39-1) | owns — same defect class as kotoba r88 F1 | "r38 C1 frozen unsatisfiable: predicate required 8/8 at J while G2 required the receipt inside the export" |
| kotodama | `SKILL.md:726` (accept-ca-74) | adjacent-owns (freeze-keyed acceptance gate) | refusal leg "`lands` equal to the frozen base" |
| lore | `corpus/knowledge/r102-push-synthesis-r95-r102.md:61` | adjacent-owns (own canon domain) | "sixth registry gate **dependency_freeze** (14 cases) closing BR-01's JSON half" |
| tsukuroi | `SKILL.md:2125` | cites/practices (declarations only) | "Primary review snapshots and exact predicates are preregistered before dispatch; the receipt gate checks declarations only" |

## Ground B — instance-level drift / `(name, observed)` tuple gates (kotoba C2 D5(iii))

| lane | hit | classification | quote |
|---|---|---|---|
| kengaku | `.ufo/waves/round-29/falsify/FConnectPattern.md:192` | cites (fleet-lesson principle; no gate) | "a control must be shown to fail on a witness the frozen population cannot supply. Instance-level increments" |
| tameshi | `.ufo/waves/round-55/w1/T55W1ScribeMistakeSweep.md:99` | cites (method note) | "each round's disposition is instance-level ("commit these files") — never an instrument" |

No sibling owns a `(name, observed)`-tuple gate or an instance-non-growth freeze leg. False-positive senses
excluded: mado `ScoutTransport.md:40` ("No instance drift" = compositor instance), kengaku novelty pricing
"instance-level" (prior-art pricing, r52), kasegi G19 "instance-level" (fixture-conformance tagging), kaidoku
`E23.md:82` (receipt prose). **C2's instance-level leg is new ground fleet-wide.**

## Ground C — routed-repairs successor gates (kotoba `check_r86_routed_repairs_v3.py`)

| lane | hit | classification | quote |
|---|---|---|---|
| mori | `PROVINCE.md:590-591` | owns (own-lane series) | "Recheck round-23 routed defects R1–R4 from committed Git objects" |
| kasegi | `corpus/instruments/r44-routed-defects.py`, `r45-routed-defects.py`, `r47-routed-defects.py` | owns (own-lane series; files verified present by glob) | (instruments on disk; no quote needed) |
| kumitate | `scripts/routed-ledger.mjs` | owns (ledger, not a gate; verified present by glob) | (script on disk) |
| kaidoku | `SKILL.md:1034` | owns (own-lane gate) | "`0` all six R17 routed defects closed, `1` any open (named correction or substance), `2` could-not-evaluate" |
| kotodama | `corpus/lessons/round-14.md:1` | cites | "Round 14 — gate-keeper survey: receipt preservation, routed repairs, retrospective" |
| kengaku | `.ufo/waves/round-69/w1/SiblingOverlap.md:157` | cites (a sibling connector already mapped this ground) | "**Status: routed.** Same *method class* … **different surface**" |

No sibling claims a successor gate over kotoba's routed series; v3 stays inside kotoba's lane ground.
kengaku's r90 connector scan (`w1/ConnectorOverlap/overlap.md` A4–A8) reached the same keep verdicts —
independent agreement, not a dependency.

## Ground D — "controls executed before the freeze" (phrasing + discipline)

| lane | hit | classification | quote |
|---|---|---|---|
| chousa | `corpus/evidence/round29/claims.md:149` | cites/practices | "## Pre-freeze controls" |
| chousa | `corpus/evidence/round30/claims.md:224` | cites/practices | "## Pre-freeze controls (filled by the control wave before data)" |
| chousa | `SKILL.md:84` (research-gate verify-claims) | owns (expect-vs-observed schema lineage for C1's `expect:` shape) | "`0` clean (`RESEARCH_GATE: CLEAN`; every claim matches its pre-registered `expect`)" |
| tameshi | `corpus/lessons/round-29.md:85` | cites/practices | "the orchestrator's pre-freeze control rule (controls scored before data)" |
| tameshi | `corpus/knowledge/guard-kill-closure.md:16-19` | owns (mutation-method ground behind Q47 batteries) | "A guard G is covered by its owning `--selftest` only when both hold at the same rev" |
| tameshi | `corpus/knowledge/guard-kill-closure.md:25` | owns (meta-cheat = C1's parse-shortcut arm) | "A selftest case that hashes or greps its own source kills every mutant with no behavioural coverage" |
| kumitate | `corpus/lessons/round-45.md:71` | cites/practices | "## Controls (pre-freeze control wave, attempt 2)" |
| kake | `corpus/lessons/round-43.md:56` | cites/practices | "Freeze before ANY seat scores → this round's counter v4, predicate, kill rule, control classes" |
| kengaku | `corpus/QUALITY.md:167` (R7) | owns (criterion) | "No live request is sent before the frozen battery/table file exists" |
| kengaku | `PROVINCE.md:61-63` | owns (standard claim; fleet referral open) | "the preregistration standard (hashed predictions + filed power analysis + Brier scoring + ordering proof + hermetic replay gate) has no sibling owner" |
| mori | `corpus/SOURCES.md:62` (S056) | owns (the external preregistration source S258 duplicates) | "The preregistration revolution" — "full text via https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/" |
| kasegi | `corpus/QUALITY.md:477` (R80) | owns | "The extended pre-freeze screen and anchor-referent table carry a receipt timestamp before the freeze commit" |
| kasegi | `corpus/QUALITY.md:393` (R53) | owns (two-sided falsification, Q47 kin) | "A counter's pre-freeze falsification runs BOTH attack classes: single-edit mutants of the counter AND tree-level false-green probes" |

## Boundary verdicts (the two flagged provinces)

**1. chousa — preregistration-as-a-source is NOT chousa's province.** `chousa/PROVINCE.md:3-9` owns
"question framing; source hierarchy …; citation chaining and hop resolution; claim-vs-source verification;
search-strategy taxonomy" — no preregistration, no freeze discipline. chousa's gates *practice* pre-registered
expects (its verify-claims schema), and kotoba cites chousa and never re-derives it
(`kotoba/PROVINCE.md:60`, `SKILL.md:12`, `QUALITY.md:7-8` "the research method stays chousa's"). The
*principle* ground is held elsewhere: **mori S056** (Nosek et al. 2018, *PNAS* 115(11), full text
PMC5856500, opened 2026-10-21, mined) mechanized in `mori/corpus/knowledge/freeze-order-r18.md` +
`tools/mori-freeze-order.py`; **kengaku** claims the probe-battery preregistration standard
(`PROVINCE.md:61-63`, referred to a fleet protocol lane round 11 — `corpus/evidence/round11-fleet/r11-connector.md:15` —
never adopted fleet-wide). ScoutSource's S258 resolution landed on **PMC5856500 — the same full-text URL
mori's S056 row already carries** (ScoutSource.md FINDING: the assignment's route (a) PMC5813543 serves a
different article; (b)/(c) 403; idconv resolved DOI → PMC5856500). See `../Connector.md` finding F1.

**2. tameshi — the Q47 mutation batteries on the new gates sit on tameshi's declared method ground.**
`tameshi/PROVINCE.md:3-8`: "verification-fixture craft … mutation testing, fail-closed arms, verdict-line
discipline"; its Refuses clause keeps "every lane's gate … its own; tameshi owns only the reusable craft"
(PROVINCE.md:14-15). kotoba's C1 battery (expectation-flip / control-skip / parse-shortcut mutants;
semantics-preserving equivalent survives) is a per-lane *application* — permitted — and kotoba already
credits the craft (`QUALITY.md:68` Q57: "tameshi guard-kill/hollow controls
(`tameshi-shokunin/corpus/knowledge/guard-kill-closure.md:14-29`)"). The battery receipt and the round-89
lesson must carry that credit (cited, not re-derived); any *general* new pattern admission routes to tameshi
under its two-independent-lanes rule. See `../Connector.md` finding F2.

## Coverage and negatives

- revenger, tabi, game-dev-2d, game-dev-3d, audio: **no ground** — only per-round pre-freeze smoke/battery
  prose in lessons and receipts (e.g. `tabi/corpus/knowledge/webview2-control-keys-round-55.md:16` "the
  pre-freeze smoke run caught Backspace then deleting a middle character"); audio's "freeze leg" is a
  PipeWire stream freeze (false positive), game-dev receipts say "pre-freeze revision" prose only.
- souji's SKILL census gates and `tools/souji-freeze-check.py` (FROZEN-EDITED / DISPATCH-BEFORE-FREEZE)
  are pin/order gates — covered by the souji rows above.
- `kumitate-shokinin/` (stray dir): 0 hits.
- Handoff dependencies: none — this scan reads only committed sibling bytes and kotoba's `SOURCE_READY`
  (content "S258 S259") and `ScoutSource.md`, both present at scan time.
