# Kb80S17ReceiptIndex — canonical receipt index (kotoba round 80, wave w1)

Seat: `Kb80S17ReceiptIndex` (scribe, leaf). Date: 2026-10-27. Lane root: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Authority: `plans/round-80.md` (L1-frozen) and the 64 seat prompts in `.ufo/waves/round-80/w1-spec.json`.
Scope: this file names every receipt the round-80 report (`.ufo/reports/round-80/kotoba.md`, draft `build/Kb80S04Report.md`) and the round-80 lesson (`corpus/lessons/round-80.md`, draft `build/Kb80S01Lesson.md`) cite, states the command that produced each, maps each to the claim/section/marker that cites it, and marks the **blocking** set. All paths below are lane-relative (the report and lesson cite lane-relative tokens; the fleet report is filed under the lane's `.ufo/reports/round-80/`).

## 1. What counts as a receipt here

A **receipt** is a committed evidence file whose bytes record (a) the command, (b) the command's own output and (c) **the command's own exit status**. Plan § Receipt discipline (Q50/Q65/R79-D4):

> `.ufo/waves/round-80/build/run-battery.sh` (written by the BatteryRunner seat) is the reusable battery runner; the report names the exact tip receipt for every battery value it cites. Every gate verdict is captured by the command's own exit status, never a pipeline's.

Three consequences are enforced by this index:

1. **Own-exit capture.** A receipt produced as `cmd | tail; echo $?` records the pipeline's status, not the gate's — the round-80 lesson's M80-1 (evidence `receipts/m80-1-pipe-vs-direct.txt`: pipe-read `rc=0`, direct `rc=1` on the same gate). Section 6 lists which committed receipts do and do not carry an own-exit line.
2. **Exact tip receipt per battery value.** Every value in report § Before → after names a file, not a directory (report markers `{{TIP_OUT}}/NN-*.txt` are already in that shape).
3. **Name authority.** A produced file's path is fixed by the plan or the producing seat's prompt; where the prompt leaves the name free, the producing seat's report (`w1/<Seat>.md`) is the authority and the file must be cited from there. This index uses the producer's own publish path and flags consumer prompts that look elsewhere (finding F5).

Presence is deliberately **not** inlined in § 3: it changes while the wave runs. The master table carries the blocking flag; the live present/missing list is `build/Kb80S17ReceiptIndex-check.py`, snapshot output `build/Kb80S17ReceiptIndex-status.txt` (last run 2026-10-27T23:34:38Z, exit 1). **EXISTS/MISSING** in that output is a presence check only — it is not a verdict on any claim value, and mid-wave absence is expected.

Blocking criterion used below: **blocking = true** iff the report or lesson states a value/claim that has *no other* receipt than this file. A blocking receipt that is missing makes the sentence citing it unwritable at integration.

## 2. Blocking set (must exist before the report is filed)

| # | Receipt (lane-relative) | Why it is blocking |
|---|---|---|
| 1 | `.ufo/waves/round-80/receipts/freeze-shas.txt` | The C1 and C2 predicates are frozen by sha256 in this file **before any after-value** (plan § C1/C2). Report markers `{{FREEZE_RECEIPT}}`, `{{E5_SHA}}`, `{{C2_SHA}}`. Must be written before the tip battery and the C2 tip run. |
| 2 | `.ufo/waves/round-80/receipts/tipbattery-base-abs.txt` | The plan's Trigger cites it for the base **absolute** `--repo <lane>` form; the frozen predicate's both-forms discipline is otherwise half-receipted. **Absent at this snapshot (F2).** |
| 3 | `.ufo/waves/round-80/receipts/tipbattery-base-dot.txt` | Base `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 — the C1 before-value, and the only receipt carrying all six base gate exit codes. Paper. |
| 4 | `.ufo/waves/round-80/receipts/tip/{index.txt,01-tip-battery-dot.txt,02-tip-battery-abs.txt}` | The C1 after-value in both forms, plus the tip revision/cwd the report quotes (`{{C1_AFTER_A}}`, `{{C1_AFTER_B}}`, `{{C1_TIP_REV}}`). Names fixed by the committed `run-battery.sh` (lines 190–196); only the out-dir is proposed here. |
| 5 | `.ufo/waves/round-80/receipts/tip/{03..09,15}-*.txt` | No-harm battery at the final pre-report tip: registry, floors, checklist, integrity, independent, sweep, census, report pointers (plan § No-harm battery). |
| 6 | `.ufo/waves/round-80/receipts/tip-extra-sibling-census.txt` | `check_sibling_census.py --skill SKILL.md` at the tip (Q72) — **not** run by `run-battery.sh` (F8). |
| 7 | `.ufo/waves/round-80/receipts/c2-base.txt` | C2 before-value `allowed-tools surfaces documented 0 of 6`, exit 1 (report `{{C2_BASE_RECEIPT}}`). |
| 8 | `.ufo/waves/round-80/receipts/c2-tip.txt` | C2 after-value plus the `generator world: M of 6` line the headline must print beside it (Q71/Q74). |
| 9 | `.ufo/waves/round-80/receipts/c2-selftest.txt` | The counter's own self-test (`{{C2_SELFTEST}}`); the registry row pins `--self-test`. |
| 10 | `.ufo/waves/round-80/receipts/c2-controls.txt` | C0–C8 scored on the frozen bytes before data (`{{C2_CTRL_RECEIPT}}`); any world reaching 6/6 is a counter defect. |
| 11 | `.ufo/waves/round-80/receipts/census-after.txt` | Report § Sources & frontier after-value (`{{CENSUS_AFTER_EXIT}}`, `{{CENSUS_AFTER_ROWS}}`, `{{ROWS_AFTER}}`); must carry its own exit and the row count (F1). |
| 12 | `.ufo/waves/round-80/build/Kb80E06CounterErratum.patch` + `.sha256` | The frozen amended counter (erratum E5) and its sha; without both the C1 predicate has no frozen bytes. |
| 13 | `.ufo/waves/round-80/build/Kb80E0{1,2,3,4,5}*.patch` (+ `Kb80E05GrammarFix.blobs`, `Kb80E04DeadPointer.blob`) | The five repairs the C1 after-value depends on; the blob files are the pin *inputs*; E5 must pin the composed post-E05 integrity blob (F12). |
| 14 | `.ufo/waves/round-80/build/Kb80E14C1Worlds.txt` | Control worlds W0–W7 with their own exits (`{{W_RECEIPT}}`); the report's "none reached 6 of 6" is otherwise unsourced. |
| 15 | `.ufo/waves/round-80/build/Kb80E16PinAudit.txt` | Independent recomputation of every freeze pin (V03 cross-checks it). |
| 16 | `.ufo/waves/round-80/build/check_allowed_tools.py` | The C2 counter's frozen bytes; landed as `verifiers/check_allowed_tools.py`. |
| 17 | `.ufo/waves/round-80/build/allowed-tools-surfaces-round80.md` | The C2 entry (lands as `corpus/knowledge/allowed-tools-surfaces-round80.md`); every row quote is verified against it. |
| 18 | `.ufo/waves/round-80/build/Kb80R03ReopenSix-S2{26..31}.fetch.json` + `w1/Kb80R03ReopenSix.md` | "The six pages were re-opened live on 2026-10-27" (`{{REOPEN_RECEIPT}}`) — the only evidence for the `opened` cell. |
| 19 | `.ufo/waves/round-80/build/Kb80R01NegSweep.md` | Grounds the S232+ rejection rows (`{{NEW_ROWS}}`) with 12 fetch records. |
| 20 | `.ufo/waves/round-80/build/Kb80S05SourcesEdits.md`, `Kb80S11GateQuotes.md`, `Kb80S16CensusLog.md`, `Kb80E12Census.txt` | The SOURCES edit text, the located-quote ledger, the old→new cell log and the census before/after runs that § Sources & frontier cites. |
| 21 | `.ufo/waves/round-80/build/Kb80R02TipRecon/`, `Kb80E11Receipts.txt` | Independent base re-derivation with **full** gate output (DRIFT lists, floors FAIL line, unindexed/unresolvable sites). `receipts/tipbattery-base-dot.txt` carries only the six exit codes, not the detail the Trigger quotes. |
| 22 | `.ufo/waves/round-80/build/Kb80S01Lesson.md`, `Kb80S04Report.md` | The lesson and report bodies themselves; every block/list row of this index is consumed by one of them. |
| 23 | `.ufo/waves/round-80/build/Kb80S02Log.md`, `Kb80S03Scorecard.md`, `Kb80S08ReadmeRows.md`, `Kb80S09SkillRule.md`, `Kb80S10Province.md`, `Kb80S07Quality.md`, `Kb80S12AssimDisp.md`, `Kb80S13L0.md`, `Kb80S06Shonen.md`, `Kb80S15FreezeShas.md` | LOG/SCORECARD/coverage/SKILL/PROVINCE/Q75/assimilation/L0/SHONEN drafts and the freeze-shas draft the L1 files and the report markers point at. |
| 24 | `.ufo/waves/round-80/build/Kb80R07ClosureScan.md` | Report § Landed changes' routed-defect table (R77-D1–D4, R78-D1–D4, R79-D1–D4). |
| 25 | `.ufo/waves/round-80/build/Kb80R06ShokuknowSlice.md`, `w1/Kb80K03Considerthese.md` | The assimilation verdict (`{{ASSIMILATION}}`) and the considerthese 2–5 dispositions (`{{PROPOSALS}}`), both cited in report § Sources & frontier and lesson § Gate. |

Counts at the 23:34:38Z snapshot: **60** fixed-path rows (**51** blocking) + **16** mandatory-subject rows + **65** seat-report slots (64 dispatched seats + the plan's `Kb80ReopenSix` name, which has no seat — F4). Then still missing: **11** blocking fixed-path rows and **all 16** subjects; seat reports present 45/65. Non-blocking rows never gate the report; they are listed so nothing is cited that no one produced.

## 3. Master table

`cited by` uses: R§WP Work performed · R§LC Landed changes · R§BA Before → after · R§SF Sources & frontier · R§TV Trend verdicts · R§SH SHONEN · R§END stale-lane/tool-installs/L0 · L§G lesson Gate · L§M lesson Mistakes · L§SF lesson Sources & frontier · LOG/SCORE/Q75/COVER/SKILL/PROV · `{{MARKER}}` = the report skeleton's marker whose value is this receipt.

| ID | Receipt | What it proves | Producing command | Cited by | Blocking |
|---|---|---|---|---|---|
| B01 | `receipts/tipbattery-base-dot.txt` | Base C1 value: `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1; the six base gate exit codes; `instruments added 22 / deleted 3 lines (cap 40)` | `python3 -B verifiers/check_tip_battery.py --rev 398cbe1… --repo . > f 2>&1; rc=$?` (lane root, fleet-shaped sandbox) | R§WP, R§BA, L§G, `{{C1_AFTER_A}}` base line | Y |
| B02 | `receipts/tipbattery-base-abs.txt` | Base absolute-form twin of B01 | same with `--repo /home/vgpnk/Projects/shokunin/kotoba-shokunin` | R§WP (base, both forms) | **Y — absent (F2)** |
| B03 | `receipts/census-before.txt` | Census at base: terminal `kotoba ok`; 24 W04 lines (**no exit line, no row count — F1**) | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | R§WP, R§SF, L§SF, `{{CENSUS_BEFORE_EXIT}}` | Y |
| B04 | `receipts/census-after.txt` | Census after SOURCES edits, own exit + row count | same command at the final pre-report tip | R§SF, `{{CENSUS_FINAL}}` | Y |
| B05 | `receipts/census-final.txt` | r79 round-end receipt name (parity for the R79-D2 notice) | r79 receipt (read-only reference) | L§G (R79-D2 notice) | N |
| B06 | `receipts/m80-1-pipe-vs-direct.txt` | Same gate, two capture forms: pipe-read `pipe-rc=0` vs direct `direct-rc=1` | the gate run both ways (`… | tail -1; echo $?` vs `… > f 2>&1; rc=$?`) | R§WP, L§M (M80-1) | Y |
| B07 | `receipts/freeze-shas.txt` | Frozen sha256 set: amended C1 counter, two instrument blobs, C2 counter, six patches — written before any after-value | `sha256sum` / `git hash-object` over the frozen bytes (draft: `build/Kb80S15FreezeShas.md`) | R§WP, R§BA, SCORE, `{{FREEZE_RECEIPT}}`, `{{E5_SHA}}`, `{{C2_SHA}}` | **Y — absent (ordering-critical)** |
| C1p01 | `build/Kb80E01Registry.patch` | SKILL.md gate-registry rows (2 withdrawn + `check_allowed_tools`); registry gate `63 of 63` at the patched world | scratch clone edit + `git diff --cached --binary > …` | R§LC, `{{SKILL_DIFFSTAT}}`, `{{V_REGISTRY_TIP}}` | Y |
| C1p02 | `build/Kb80E02Symlink.patch` | `.ufo/reports/round-76/kotoba.md` relative symlink (mode 120000); checklist greens | same (`git diff --cached --binary`), symlink added with `ln -s` | R§WP (§repair 2), `{{SYMLINK_SHA}}` | Y |
| C1p03 | `build/Kb80E03IndexBaseline.patch` | README coverage rows (3) before the baseline refresh | scratch edit + diff | R§WP (§repair 3), `{{BASELINE_NOTE}}` | Y |
| C1p04 | `build/Kb80E04DeadPointer.patch` | `verify_corpus_integrity.py` `<rev>:` pointer resolution + red-before arm | port of `.ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch` (sha256 `d7169dd8…`) | R§WP (§repair 4), `{{E04_DIFFSTAT}}` | Y |
| C1p05 | `build/Kb80E04DeadPointer.blob` | **Intermediate** blob after the E04 fix only (`051b8c5f…`, one-file patch); the pin E5 must add is the **post-E05 composition** of the same file (E05 patches both gates — F12) | `git -C "$S/clone" hash-object verifiers/verify_corpus_integrity.py > …` (format `<sha>  <path>`) | B07, `{{SNAP_NOTE}}`-adjacent pin table | Y |
| C1p06 | `build/Kb80E06CounterErratum.patch` | Erratum E5: `LINE_CAP` 40→60 + exactly two new pins + in-step self-test arms | scratch edit + diff | R§WP (erratum), `{{E5_DIFFSTAT}}` | Y |
| C1p07 | `build/Kb80E06CounterErratum.sha256` | sha256 of the amended `check_tip_battery.py` | `sha256sum verifiers/check_tip_battery.py > …` | B07, `{{E5_SHA}}` | Y |
| C1p08 | `build/Kb80E05GrammarFix.blobs` | Blob shas of both grammar-class-patched corpus gates | `git hash-object` each patched gate | B07, `{{GRAMMAR_RECEIPT}}` | Y |
| C1p09 | `build/run-battery.sh` | Reusable runner: one receipt per command, own-exit capture, `NN-<name>.txt` contract | authored (bash) + committed; contract at lines 29–37, 189–232 | R§WP, R§BA, `{{BATTERY_SUMMARY}}`, `{{TIP_OUT}}` | Y (EXISTS) |
| C1p10 | `build/Kb80E14C1Worlds.txt` | W0–W7 on the amended counter, each with world diff + own exit; W6 stub trips `instrument-pin`/`instrument-size` | per world: `python3 -B verifiers/check_tip_battery.py --rev <world> --repo "$S/clone"` | R§WP (controls), `{{W_SUMMARY}}`, `{{W_RECEIPT}}` | Y |
| C1p11 | `build/Kb80E16PinAudit.txt` | Independent recomputation of every pin/sha cited in the freeze set | `sha256sum` / `git hash-object` / `sha256sum -c MANIFEST` sweep | R§WP, V03 cross-check | Y |
| C1p12 | `build/Kb80E15BaselineOrder.md` | Integration order, dirty-tree precondition, `--carry` decision tree, refresh exit-code meanings | authored from E03/E04/E05/E10 outputs | R§LC, L1 integration | Y |
| C1p13 | `w1/Kb80E10Battery.md` | Stack world: full C1 stack reaches the target; original counter now fails the pin guard; maximal sub-stack named if a piece is missing | stack clone + `run-battery.sh`/direct counter runs | R§BA (pre-integration proof) | N |
| C2p01 | `build/check_allowed_tools.py` | The frozen C2 counter (headline `documented`, target 6, `generator world:` line, rider line) | authored port of `.ufo/waves/round-79/build/check_allowed_tools.py` + `--self-test` | R§WP, R§BA, `{{C2_DIFFSTAT}}` | Y |
| C2p02 | `build/allowed-tools-surfaces-round80.md` | The knowledge entry: source lines, 11-cell rows S226–S231, frozen table, semantics matrix, Limits | authored; per-surface quote-offset verification | R§WP, R§SF, `{{ENTRY_DIFFSTAT}}` | Y |
| C2p03 | `build/c2_controls.py` | C0–C8 control driver (isolated scratch repos, every git call `-C`'d, toplevel asserted) | authored (stdlib) | R§WP, `{{C2_CTRL_SUMMARY}}` | Y |
| C2p04–09 | `build/Kb80R03ReopenSix-S2{26..31}.fetch.json` | Six live re-opens: status/bytes/sha256/UTC ×2, byte-compare vs snapshot, quote offset | `curl -sSL -A 'Mozilla/5.0' --max-time 60 <url>` ×2 + `sha256sum` + `cmp` | R§WP, `{{REOPEN_RECEIPT}}`, L§G | Y |
| C2p10 | `w1/Kb80R03ReopenSix.md` | Re-open narrative, redirect chain (S228), S229 variance class, S230/S231 `main`-branch note | seat report | R§WP, `{{REOPEN_RECEIPT}}` | Y (plan cites a different name — F4) |
| C2p11 | `.ufo/waves/round-79/snapshots/` (18 files: 6 bodies + 6 `.manifest` + 6 `.fetch.json`) | The pinned snapshot bytes and per-snapshot pins | committed r79 fetch; re-verified this round | R§WP, R§SF, `{{SNAP_NOTE}}` | Y (no `MANIFEST.sha256` — F3) |
| C2p12 | `w1/Kb80E08C2Entry.md` | Entry verification: per-surface quote occurrence offsets | seat report | R§WP | N |
| C2p13 | `w1/Kb80E07C2Counter.md` | Counter self-test output + sha256 | seat report | R§WP | N |
| FR01 | `build/Kb80R01NegSweep.md` | 12 negatives re-opened: status/bytes/sha256/UTC ×2 + `allowed-tools` grep result each | 12× curl + grep | R§WP, L§G (`{{NEW_ROWS}}`), FR03/FR04 inputs | Y |
| FR02 | `build/Kb80R01NegSweep-admit.md` | Only if a negative mentions the field (then an admit, not a rejection) | same sweep | L§G | N |
| FR03 | `build/Kb80S05SourcesEdits.md` | Exact old→new `used-by` cells (S226–S231) + S232+ rows in census schema + Search-log note | authored from FR01 + current SOURCES cells | R§SF, L§G, `{{TOUCHED_ROWS}}` | Y |
| FR04 | `build/Kb80S11GateQuotes.md` | Located-quote ledger for every touched row: quote, snapshot, offset, access date (plus `-verify.json` occurrence proof) | authored; occurrence check against committed snapshots | R§SF, L§G | Y |
| FR05 | `build/Kb80S16CensusLog.md` | Per-cell old→new log + before/after row counts (157 → N) | authored; `grep -cE` + census | R§SF, L§G | Y |
| FR06 | `build/Kb80E12Census.txt` | Census before/after blocks with own exits + exact edit list applied | `sources-census.sh validate …` + `grep -cE` | R§SF, `{{CENSUS_FINAL}}` | Y |
| FR07 | `build/Kb80R06ShokuknowSlice.md` | Quarantine-slice extraction + per-row verdicts (adoption closed) | read-only awk over `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` | R§SF, L§G, `{{ASSIMILATION}}` | Y |
| FR08 | `w1/Kb80K03Considerthese.md` | considerthese 2026-10-26 proposals 2–5, measured dispositions | read-only reads + measure commands | R§SF, L§G, `{{PROPOSALS}}` | Y |
| FR09 | `build/Kb80R07ClosureScan.md` | One line per routed defect R77-D1–D4 / R78-D1–D4 / R79-D1–D4: addressed / carried / obsolete | reads of the r77–r79 closure docs | R§LC | Y |
| FR10 | `build/Kb80R05FleetGrammar.md` | Whether the grammar class is novel fleet ground (Q75 evidence) | `grep -rn` over `*/verifiers/*.py` | Q75, L§M (optional) | N |
| FR11 | `build/Kb80R04SiblingScan.md` | Sibling-lane overlap scan for C2 (negative result) | `grep -rl 'allowed-tools' <lane>/corpus/knowledge <lane>/SKILL.md` | R§TV (adjacency) | N |
| FR12 | `build/Kb80R02TipRecon/` | Independent base re-derivation: six gate outputs + `--json` site lists (DRIFT/unindexed/unresolvable/report_dead) + battery `1 of 6` | six gate runs with own exit; battery `--repo "$S/clone" --rev 398cbe1…` | R§WP (base detail) | Y |
| FR13 | `build/Kb80E11Receipts.txt` | Second independent base re-derivation + `git cat-file -t` for both external tokens in lane **and** fleet | gate runs + `git cat-file -t 451a02ff` / `cfb894a5` | R§WP (base detail), L§M | Y |
| S01 | `build/Kb80S01Lesson.md` | The lesson body (Gate admits, S232+ rejections, R79-D2 notice, assimilation, Mistakes M80-1) | authored | L§G/L§M/L§SF source | Y (EXISTS) |
| S02 | `build/Kb80S02Log.md` | `## Round 80` LOG entry with receipt paths and before-values | authored | LOG | Y |
| S03 | `build/Kb80S03Scorecard.md` | SCORECARD axis annotations: C1 predicate + 1→6; C2 form backbone 0→6 + rider pointer | authored | SCORE | Y (EXISTS) |
| S04 | `build/Kb80S04Report.md` | Report skeleton with every marker, counting command and evidence pointer | authored | R§ all | Y (EXISTS) |
| S06 | `build/Kb80S06Shonen.md` | Four SHONEN box states re-derived at base with live commands | authored + live commands | R§SH | Y |
| S07 | `build/Kb80S07Quality.md` | Q75 row (external-commit citation class), red-before evidence | authored | Q75 | Y |
| S08 | `build/Kb80S08ReadmeRows.md` | Three coverage-map rows + Frontier note | authored | COVER | Y |
| S09 | `build/Kb80S09SkillRule.md` | `allowed-tools` rule line (≥3 surfaces) + registry row coordination | authored | R§WP, SKILL | Y |
| S10 | `build/Kb80S10Province.md` | `## Core` bullet naming the entry; sibling-census stays green | authored | R§WP, PROV | Y (EXISTS) |
| S12 | `build/Kb80S12AssimDisp.md` | Assimilation disposition paragraphs (slice verdicts, merge read-only, proposals 2–5) | authored from FR07/FR08 | L§G, `{{ASSIMILATION}}` | Y (EXISTS) |
| S13 | `build/Kb80S13L0.md` | Either the L0 append line or the explicit no-question finding | authored | R§END, `{{L0_QUESTIONS}}` | Y |
| S15 | `build/Kb80S15FreezeShas.md` | The exact freeze-shas.txt text + erratum justification sentence | authored from the frozen bytes | B07 input | Y |
| S14 | `build/Kb80S14WaveRegistry.md` | Seat/build index with per-seat verdicts (PENDING where absent) | authored | L1 reconciliation | N |
| E13 | `build/Kb80E13FixtureGuard.md` | Tooling hygiene: `/tmp` roots, pacman, network at measure time, git outside sandbox | authored sweep | R§END (hygiene) | N |
| TIP01 | `receipts/tip/index.txt` | Runner index: rev/repo/fleet/utc + per-receipt exit + figure | `run-battery.sh <rev> <repo> receipts/tip <report>` | `{{TIP_OUT}}`, `{{BATTERY_SUMMARY}}` | Y (subject) |
| TIP02 | `receipts/tip/01-tip-battery-dot.txt` | C1 form 1 at tip (`--repo .`), own exit | runner line 193 | `{{C1_AFTER_A}}`, `{{C1_CWD_A}}`, `{{C1_EXITS}}` | Y (subject) |
| TIP03 | `receipts/tip/02-tip-battery-abs.txt` | C1 form 2 at tip (absolute `--repo`), own exit | runner line 195 | `{{C1_AFTER_B}}`, `{{C1_CWD_B}}` | Y (subject) |
| TIP04 | `receipts/tip/03-gate-registry.txt` | Registry gate at tip | runner line 199 | `{{V_REGISTRY_TIP}}`, `{{E_REGISTRY}}` | Y (subject) |
| TIP05 | `receipts/tip/04-assertion-floors.txt` | Floors gate at tip (~100 s) | runner line 201 | `{{V_FLOORS_TIP}}`, `{{E_FLOORS}}` | Y (subject) |
| TIP06 | `receipts/tip/05-skill-checklist.txt` | Checklist governance arm at tip | runner line 203 | `{{V_CHECKLIST_TIP}}`, `{{E_CHECKLIST}}` | Y (subject) |
| TIP07 | `receipts/tip/06-corpus-integrity.txt` | Integrity gate + DRIFT classes at tip | runner line 205 | `{{V_INTEGRITY_TIP}}`, `{{E_INTEGRITY}}` | Y (subject) |
| TIP08 | `receipts/tip/07-corpus-independent.txt` | Independent gate + DRIFT classes at tip | runner line 207 | `{{V_INDEPENDENT_TIP}}`, `{{E_INDEPENDENT}}` | Y (subject) |
| TIP09 | `receipts/tip/08-correction-sweep.txt` | Correction sweep at tip | runner line 209 | `{{E_SWEEP}}` | Y (subject) |
| TIP10 | `receipts/tip/09-census.txt` | Census at the final tip | runner line 211 | `{{V_CENSUS_TIP}}` | Y (subject) |
| TIP11 | `receipts/tip/15-report-pointers.txt` | Report-pointer gate at the report commit (Q68) | runner line 231 (`<report-path>` arg) | `{{V_POINTERS}}` | Y (subject) |
| EXT01 | `receipts/tip-extra-sibling-census.txt` | `check_sibling_census.py --skill SKILL.md` at tip (F8: not in the runner) | `python3 -B verifiers/check_sibling_census.py … --province PROVINCE.md --skill SKILL.md` | `{{V_SIBLING}}`, `{{SIBLING_RECEIPT}}` | Y (subject) |
| EXT02 | `receipts/c2-base.txt` | C2 base `documented 0 of 6`, exit 1 | `python3 -B verifiers/check_allowed_tools.py --rev 398cbe1… --repo .` | `{{C2_BASE_RECEIPT}}` | Y (subject) |
| EXT03 | `receipts/c2-tip.txt` | C2 tip `documented 6 of 6` + `generator world: M of 6`, exit 0 | same at the tip | `{{C2_TIP_RECEIPT}}`, `{{C2_AFTER}}`, `{{C2_GENERATOR_M}}` | Y (subject) |
| EXT04 | `receipts/c2-selftest.txt` | C2 counter self-test | `… --self-test` | `{{C2_SELFTEST}}` | Y (subject) |
| EXT05 | `receipts/c2-controls.txt` | C0–C8 per-world `documented`/`generator world`/exit | `python3 -B build/c2_controls.py --counter <counter> --base-tree <clone>` | `{{C2_CTRL_RECEIPT}}`, `{{C2_CTRL_SUMMARY}}` | Y (subject) |

Seat reports (`w1/<SeatName>.md`, 64) are cited where a free-named artifact or a verdict is produced; `build/Kb80S17ReceiptIndex-check.py` prints the live present/missing split.

## 4. Battery value → receipt map

Every battery-derived value the report can state, with the only receipt allowed to carry it:

| Value | Receipt |
|---|---|
| base `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1, `--repo .` | B01 |
| base same, absolute `--repo <lane>` | B02 (absent — F2) |
| base six gate exit codes (`registry 1, floors 1, checklist 1, integrity 1, independent 1, sweep 0`) | B01 (inside the battery output) |
| base DRIFT classes, `unindexed 1`, `commit_unresolvable 2` **site list** (attribution contested — F13), floors `FAIL … 1863 … self_test_failures=1` | FR12 + FR13 (full output). B01 carries exits only — do not cite it for the detail |
| census before `exit 0`, 157 rows, 24 W04 | B03 (terminal `ok`) + `build/Kb80S16CensusLog-rowcounts.txt` `rows=157 rc=0` for the count (B03 carries neither — F1) |
| amended-counter W0 `1 of 6`; W1/W2/W4/W5 `≤3 of 6`; W3 integrity still red; W6 guard failures; W7 `spotcheck-identity` failure | C1p10 (per-world block + own exit) |
| stack world `guards 5 of 5; tip battery exit 0: 6 of 6`; original counter fails the pin guard on the same world | C1p13 (+ its out-dir receipts named in that report) |
| **final tip** `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0, both forms | TIP02 + TIP03 (with TIP01 for rev/cwd/utc) |
| final tip six gates exit 0 / DRIFT 0 | TIP04–TIP09 |
| final tip census exit 0, N rows | TIP10 (+ B04) |
| final tip report pointers | TIP11 |
| final tip sibling census | EXT01 |
| C2 base `documented 0 of 6`, exit 1 | EXT02 |
| C2 tip `documented 6 of 6`, `generator world: M of 6`, exit 0 | EXT03 |
| C2 controls C0–C8 | EXT05 |
| C2 counter self-test | EXT04 |
| S229 admissibility under the frozen Q70 rule (F16) | the C2 counter's location rule + `w1/Kb80E08C2Entry.md`
| S230 anchor correction (F15) | `S230.fetch.json` + `S231.fetch.json` (bytes) → lesson erratum line |
| C1 cap arithmetic (22 spent + 17 E04 + grammar ≤21 = 60) | B01 (base `instruments added 22 / deleted 3`) + E06 patch numstat + E10 stack numstat + `build/Kb80S07Quality-world.patch` (171 added / 5 deleted, measured) |

## 5. Cross-check against plan § Receipt discipline — findings

Each finding is stated with the command that establishes it. None of these scores a claim; they are receipt-integrity observations for the L1.

**F1 (blocking, calibration).** `receipts/census-before.txt` carries **no own-exit line and no row count**, yet plan § Frontier and the report cite it for "exit 0, 157 rows". Evidence: `tail -3` shows the terminal `kotoba ok` line and nothing after; `grep -c '^exit='` = 0. The r79 counterparts *do* carry `exit=0` (`.ufo/waves/round-79/receipts/census-final.txt`, `census-before.txt`), so this is a round-80 regression in capture discipline. The count itself is true and separately receipted: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `157`, and `build/Kb80S16CensusLog-rowcounts.txt` records `rows=157 rc=0`. Fix: cite B03 for the terminal `ok` and the rowcount receipt for `157`; make B04 (after) carry both exit and count.

**F2 (blocking).** Plan § Trigger cites `receipts/tipbattery-base-abs.txt`; the file does not exist (`ls` → ENOENT; checker row B02). The absolute-form base reading is therefore unbased in the committed receipts. Fix: run the absolute form at `398cbe1…` with own-exit capture into that path, or correct the plan citation before the report quotes it.

**F3 (blocking, C2).** Plan § C2 and the E08 prompt require snapshot pins "equal in `MANIFEST.sha256`, the row's fetch record and the counter", but `.ufo/waves/round-79/snapshots/MANIFEST.sha256` does not exist (`ls` lists only `S2xx-{spec,claude,factory,msaf,pi,vibe}` bodies plus per-snapshot `.manifest` and `.fetch.json`). The pins live in the per-snapshot files (e.g. `S226.manifest` = `9a67de89…  S226-spec.md`, matching `S226.fetch.json`). Fix: either publish an aggregate `MANIFEST.sha256` (18 lines) or have the counter and the report name the per-snapshot `.manifest` as the manifest; the report's `{{SNAP_NOTE}}` must match whichever lands. Resolution path observed: E10 reports it **created** `.ufo/waves/round-79/snapshots/MANIFEST.sha256` in its stack world (the S09 registry row's pinned-values cell and the C2 conjunct (c) name it), so the file must be added at the final tip, not cited from r79; E16/V03 must pin it.

**F4 (naming).** Plan § C2 names the re-open receipt `.ufo/waves/round-80/w1/Kb80ReopenSix.md`; no such seat exists — the dispatched seat is `Kb80R03ReopenSix` and its report path is `w1/Kb80R03ReopenSix.md` (seat spec + `w1-spec.json`). `build/Kb80R07ClosureScan.md` repeats the plan's name, so the wrong token is propagating into the report's Landed-changes table. Fix: cite `w1/Kb80R03ReopenSix.md` (canonical) and correct the propagation; do not create a second file with the plan's name.

**F5 (operability).** Consumer/producer path mismatches in the dispatched prompts:
- `Kb80R01NegSweep` publishes `build/Kb80R01NegSweep.md`; `Kb80S05SourcesEdits` and `Kb80E12Census` read `w1/Kb80R01NegSweep.md`.
- `Kb80R06ShokuknowSlice` publishes `build/Kb80R06ShokuknowSlice.md`; `Kb80S12AssimDisp` (and the S01 prompt) read `w1/Kb80R06ShokuknowSlice.md`.
Producer path wins (authority rule). Result: the two consumers may have read nothing — S05/E12/S12 reports must say which path they used, or the L1 re-runs the affected step against the produced file. `Kb80K03Considerthese` is consistent (publishes and is read at `w1/`).

**F6 (arithmetic).** The `Kb80S02Log` prompt instructs "attack share 18/64 = 28.1 %", but the dispatched spec is 17/64 = 26.6 %: `python3 -c "import json,collections;c=collections.Counter(i['role'] for i in json.load(open('.ufo/waves/round-80/w1-spec.json'))['items']);print(c);print(sum(c[r] for r in ('critic','reviewer','mutation-tester','sentinel')))"` → `17` of `64`. Plan § Round shape and report § Work performed both say 17/64 = 26.6 %. Fix: the LOG draft must not carry 18/64; this is the same class of stale-arithmetic defect as R79-D2.

**F7 (naming, port source).** Plan § C1 repair 2 and the E02 prompt differ on the r79 port source (`Kb79E02LogCitation.patch` vs a possible `Kb80E02LogCitation.patch`). The r79 build dir holds only `Kb79E02LogCitation.patch` (plus a draft correction-row patch). The index pins `Kb79E02LogCitation.patch` as the source; the round-80 output is `build/Kb80E02Symlink.patch`.

**F8 (operability, Q72 coverage).** `build/run-battery.sh` runs the two battery forms, the six gates, the census, SKILL.md size figures and (optionally) report pointers — it does **not** run `check_sibling_census.py` (named by plan § No-harm battery) nor the C2 counter (needed by C2's after-value). Those need their own tip receipts: EXT01, EXT03. This is not a runner defect (it documents its command list), but the report's § Before → after assumes them.

**F9 (ordering).** `B07 freeze-shas.txt` is the plan's freeze instrument ("before any after-value is measured"). At this snapshot it does not exist while E06's erratum bytes and the control worlds (pre-data controls, permitted) already do. The enforceable rule the L1 must satisfy: B07 is written and committed **before** TIP02/TIP03 (C1 tip) and EXT03 (C2 tip) run; the receipt timestamps are the audit. If the L1 instead runs the tip battery first, the freeze is unprovable and the C1/C2 after-values cannot be cited. Related measured ordering (E10): the baseline refresh script refuses with exit 2 ("zero-mode … `commit_unresolvable` observed 2, not 0") until E05 lands, so the integration order is rows → E04 → E05 → refresh → commit → measure; `build/Kb80E15BaselineOrder.md` must match it.

**F10 (low, pointer content).** The S04 draft's HTML comment points at `.ufo/waves/round-80/w1/Kb80S04Report.md` as "the marker register … which also carries the exact commands and the pointer rules". That path is the S04 *seat report* (the universal seat-report rule), not this build draft; it can only serve as the marker register if its body actually carries it. V05Report's pointer scan will judge the content; the index records the ambiguity so it is not mistaken for a dead path (`w1/<Seat>.md` is created for every seat).

**F11 (lane hygiene, not a receipt).** An untracked regular file `.ufo/wapes` (594 B, created 2026-10-27 20:17 local) exists in the lane root — a typo of `.ufo/waves` produced by a sibling seat's quote probe (content: four `words=… ok=False why='quote lies in the first-heading block (Q70)'` lines and `exit=0`). It is outside this seat's write scope, so it was left in place. It is untracked (no commit needed to remove) and will otherwise appear in the report's misroot sweep and in `git status` at filing. The L1 removes it before the report; the seat whose probe wrote it should be identified from its report — the same defect class as R78-D4 worktree residue.

**F12 (cross-seat pin composition, blocking).** `build/Kb80E04DeadPointer.blob` reads `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f  verifiers/verify_corpus_integrity.py` — the blob after the E04 `<rev>:` fix **only** (the patch touches that single file: `+++ b/verifiers/verify_corpus_integrity.py`). E05's grammar class edits **both** corpus gates, so the final integrity blob differs from this value; erratum E5 must pin the composed (E04∘E05) integrity blob and the E05 independent blob. Pinning the E04-only value makes the full stack fail `instrument-pin` **by construction** — C1 would stop honestly for a pin-ordering reason, not a repo-state reason. The E06 prompt's fallback ("apply `Kb79E04DeadPointer.patch` yourself and compute it") yields the same E04-only value, so the prompt under-specifies the composition order. Fix: E06 takes the integrity line of `build/Kb80E05GrammarFix.blobs` (which must be computed on the E04-patched file) — commands: `cat build/Kb80E04DeadPointer.blob`; `grep '^+++' build/Kb80E04DeadPointer.patch`.

**F13 (attribution conflict, blocking).** Plan §Trigger names the two base `commit_unresolvable` tokens as `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`. The `Kb80V03Instruments` audit broadcast (full table in `w1/Kb80V03Instruments.md`) reports the real blockers at `corpus/SOURCES.md:171-172` (rows S230/S231) as **pure-hex backticked** tokens `7bb48f213ac677f943d5c791199ed3dddf302f00`, with the third-repository name (`badlogic/pi-mono`) in a separate code span on the same line — no `owner/repo@<hex>` shape, so a grammar class keyed only on that shape would not clear C1's corpus gates. Bytes I verified myself: line 171 has the shape `resolved to` + code-span repo + `commit` + code-span hex (repo `badlogic/pi-mono`, hex `7bb48f21…`), and line 172 carries the same token; `451a02ff` appears in SOURCES only inside raw URLs (lines 59/70/73) and `cfb894a5` does not appear there at all, while both quoted-commit occurrences live in the round-54 lesson (lines 147–148 and 52). I did **not** run either corpus gate: the attribution must be settled by FR12/FR13's `--json` site lists, and the report must not repeat the plan's Trigger attribution without that receipt. The SOURCES rows must not be rewritten (M45 pattern).

**F14 (C2/C1 seam, blocking).** The C2 entry `build/allowed-tools-surfaces-round80.md:125` reads *The mistral-vibe README was served from commit* followed by the hex token in a code span (`7bb48f21…`) — a full-hex commit citation whose only repo hint on that line is the bare name `mistral-vibe` (no `owner/repo` token, no raw URL). Under the grammar class's red-before arm shape (an unmarked absent token keeps the red path), landing the C2 entry would add a third `commit_unresolvable` and keep both corpus gates red — C1 blocked by C2's own artifact. Resolution is one of: the class treats a bare repo name adjacent to the hex as the external marker (the V03/E10 reading), or the entry's line carries an explicit `owner/repo` marker (the `mistralai/mistral-vibe` name or its commit-pinned raw URL). Verified: `grep -n '7bb48f21' build/allowed-tools-surfaces-round80.md` → line 125. The entry and the class must be co-designed; this index records the seam, not the fix. **Status 2026-10-27T23:34:31Z: fixed in the entry and verified by me** — `grep -cE '7bb48f21|bb65e3e4|25cc5c7b' build/allowed-tools-surfaces-round80.md` → `0`, and a per-line scan for the six pinned basenames finds `0` lines carrying more than one. The class requirement stands for the SOURCES tokens (F13).

**F15 (S230 anchor erratum, blocking for Sources & frontier).** `corpus/SOURCES.md:171` (row S230) says pi-mono `main` "resolved to `badlogic/pi-mono` commit `7bb48f21…`", but the fetch record says otherwise: `S230.fetch.json` records head `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923` with the last commit touching the path `25cc5c7bf4cbc76b2e134c729eb8d57d521ed749`, while `7bb48f213ac677f943d5c791199ed3dddf302f00` is S231/mistral-vibe's commit (`S231.fetch.json`). The row cites the wrong repository's commit. Verified by me: `grep -o 'bb65e3e4[0-9a-f]*\|25cc5c7b[0-9a-f]*' S230.fetch.json | sort -u` → both; `grep -o '7bb48f21…' S231.fetch.json` → the token. The anchor cell may not be edited this round (frontier step / M45), so the correction belongs in the round-80 lesson `## Gate` as an erratum line and in report § Sources & frontier; the S230 row's *claim* (the page prints no value syntax) is unaffected.

**F16 (C2 reachability, blocking).** S229 (Microsoft Learn, HTML snapshot) names the field **exactly once** — `grep -c 'allowed-tools' .ufo/waves/round-79/snapshots/S229-msaf.html` → `1`, at raw line 818 (`<td><code>allowed-tools</code></td>`). The draft counter's heading heuristic takes a `#`-prefixed **Python comment inside a code sample** (text-view line 168, `# Auto-approve load_skill…`) as the page's first heading, so it admits only quotes starting after ~line 169 — later than the page's single occurrence (text-view line 95). The page's real heading is `<h1 id="agent-skills">` at raw 676. Consequence: under the frozen conjuncts as implemented, **S229 cannot be documented**, so `documented 6 of 6` is unreachable and C2 would stop honestly (or the location rule must be corrected — a conjunct-level change the plan forbids after the freeze). I verified the occurrence count and raw line; the text-view line numbers and the heuristic's rejection are E08/V02C2's measurements, not mine. The two seats' readings differ by one text-view line (E08: field at 95, first `#`-prefixed line at 168; S01: 96 and 169) — the structural conclusion is identical and the counter's own view decides. Non-narrowing fix if the heuristic is wrong: a **declared counter erratum for heading detection** (an HTML/GFM heading test, not a `#`-prefix test), not a quote chosen to dodge it. This index records the reachability seam; E07/V02C2 and the L1 own the resolution.

**Checked and clean.** (a) The base cap figure matches: B01 prints `instruments added 22 / deleted 3 lines (cap 40)` and E10 measures all 22 in `check_assertion_floors.py`, so with E04 (+17) the running total is 39 and the grammar class has **21** added lines across both corpus gates. That budget is the binding constraint: the only published grammar candidate, `build/Kb80S07Quality-world.patch`, measures **171 added / 5 deleted** (counted over the patch's own `+`/`-` lines), so `instrument-size` fails under cap 60 and the plan's kill rule ("repairs 4 or 5 … exceeds the declared cap arithmetic") is **live** — C1 stops honestly unless a ≤21-line class exists. Not a base defect; the constraint the E05 seat and the L1 must confront. (b) `run-battery.sh` implements the own-exit contract literally (`cmd >> f 2>&1; rc=$?; printf 'exit=%s\n' "$rc" >> f`, lines 159–160) and writes the `# rev=… cmd=… utc=…` header the report relies on. (c) The report skeleton already names one receipt per battery value using `{{TIP_OUT}}/NN-*.txt`, i.e. the runner's own names — no invented names enter the report. (d) The base six exits are receipted inside B01; the base *detail* (DRIFT names, floors FAIL line) is in FR12/FR13, not in B01.

## 6. Own-exit audit (committed receipts, snapshot 2026-10-27T23:34:38Z)

| Receipt | Own exit? |
|---|---|
| `receipts/tipbattery-base-dot.txt` | yes (`exit=1`) |
| `receipts/m80-1-pipe-vs-direct.txt` | records both forms (`pipe-rc=0`, `direct-rc=1`) — no single `exit=` line by design |
| `receipts/census-before.txt` | **no** (F1) |
| `.ufo/waves/round-79/receipts/census-before.txt`, `census-final.txt` | yes (`exit=0`) |

## 7. Re-run this index's presence gate

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
python3 -B .ufo/waves/round-80/build/Kb80S17ReceiptIndex-check.py
```

Exit codes: `0` all fixed-path blocking receipts and all mandatory subjects present · `1` a fixed-path blocking receipt is missing · `2` fixed paths complete but a mandatory-subject receipt is missing under the proposed name (write it, or write it elsewhere and update the `SUBJECTS` list + the report citation). Snapshot output: `build/Kb80S17ReceiptIndex-status.txt`.

## 8. Limits

- **Presence, not verdicts.** This index ran no claim counter, scored no value and re-ran no gate. The only measurements it took are existence checks, the `grep -cE` row count (`157`), the role census (`17/64`), and `ls`/`grep` on receipt bytes — each with its command quoted above.
- **Snapshot, not final state.** The wave was in flight at the 23:16:22Z check; 54 blocking fixed-path rows and 16 subjects were then missing. Absence mid-wave is expected and is not a defect of the producing seat; it becomes one only if still missing at integration.
- **Naming.** Where the plan fixes a path this index uses it exactly; where a prompt fixes it the producer's report is named as authority; where nothing fixes it the proposed name is marked "(subject)" and the L1 may rename by updating the checker list and the report citation in one edit.
- **No write outside the wave.** No product file, verifier, plan, SKILL.md or PROVINCE.md was touched; the lane git index was not mutated. Scratch (`/fast/scratch/hyaku/kotoba-r80/Kb80S17ReceiptIndex/`) held only the extracted prompt texts and the marker list and was removed before yielding.
- **Tool installs:** none; pacman untouched.
