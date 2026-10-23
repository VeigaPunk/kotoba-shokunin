# ConnSibling — round-62 sibling-overlap scan (wave 1, seat ConnSibling)

Date: 2026-10-23 (sweep stamped `2026-10-23T20:56:06Z`). Assignment: does any sibling
lane already hold (a) an erratum/amendment absorption audit, (b) a self-derived-count or
honest-pass counter hardening, (c) a counter-audit gate of C1's shape? Read
`PROVINCE.md` § Adjacent + sibling corpora **index lines only** (read-only). No lane,
fleet, sibling, `.ufo/state`, or git/jj-index file was written; no dispatch; the only
write is this file. Scratch unused.

## Bottom line

No sibling holds any of the three round-62 surfaces at instrument level. All three are
kotoba-owned and landable. Four **technique-level** adjacencies must be *reported, not
absorbed*: the guard-disable sensitivity arm and kill-rate controls (tameshi), the
freeze/controls-before-data clause class (kumitate), the self-derived-count class
(kagi), and the "absorb" disposition vocabulary (chousa). The E2f finding belongs to
**kotoba**, uncontested.

## Scan basis (what was actually read)

- kotoba `PROVINCE.md` § Adjacent (20 sibling rows, census round 49/50) and
  `plans/round-62.md` (§C1/§C2, M90, S118).
- Sibling corpora indexes: `corpus/README.md` of all 20 sibling lanes (`audio`,
  `chousa`, `game-dev-2d`, `game-dev-3d`, `kagi`, `kaidoku`, `kake`, `kama`, `kasegi`,
  `kengaku`, `kotodama`, `kumitate`, `lore`, `mado`, `mori`, `revenger`, `souji`,
  `tabi`, `tameshi`, `tsukuroi`) — three pattern sweeps (surface-a
  `erratum|errata|absorb|amendment`; surface-b `self-derived|self-count|honest`;
  surface-c `sha256|fail.closed|frozen|counter-audit|harden`) plus a
  `memory\.md|code\.claude|scoped rule|SKILL.md registry|frontmatter` claim sweep, then
  targeted raw index lines (tameshi coverage map; kumitate `README.md:144`; mado
  `README.md:23`).
- Working-tree tips (read-only `git rev-parse HEAD`, exit 0, 2026-10-23):
  audio `7a2fcd4f`, chousa `f5b11357`, game-dev-2d `7753d49b`, game-dev-3d `89dd182b`,
  kagi `899c50b4`, kaidoku `f432c8e3`, kake `a377c5d0`, kama `0e6f8ed6`,
  kasegi `1fafde8f`, kengaku `1f3b0f1e`, kotoba `a1cb8abc`, kotodama `ff30a205`,
  kumitate `6927903f`, lore `380ef3ab`, mado `56ef773a`, mori `1f1e9968`,
  revenger `876630db`, souji `4edb25df`, tabi `e3cf4e0d`, tameshi `51d3f080`,
  tsukuroi `cefe752d`; `kaidoku-sh2` (`f50d178d`) has no `corpus/` and is out of scope.
  These are scan-time tips, not the round-49 census pins (chousa, kake, kama, kotodama,
  mado, tameshi, tsukuroi, kumitate have moved since their pin; the census commit check
  `verifiers/check_sibling_census.py --province PROVINCE.md` governs, unchanged here).
- Bound: index lines only. "No sibling holds X" below is **index-level** evidence; a
  body-level hold invisible to the index would be missed. Wave-2 seats should keep that
  bound stated, not re-derive it.

## Table — surface | owning lane | evidence path@rev | contested? | disposition

| surface | owning lane | evidence path@rev | contested? | disposition |
|---|---|---|---|---|
| (a) Erratum absorption audit: 5 erratum classes × 2 fresh instances scored by the landed counter's own arm functions, absorbed = rejected AND flipped accepted under a guard-disabled stub, sha-pinned subject counter, exit 2 on byte drift | **kotoba** | `plans/round-62.md` §C1 @ kotoba tip `a1cb8abc` (plan base `a745411c`); subject `verifiers/check_scoped_rules.py` r61 freeze sha `5a5adc94…` | no | **absorb** — instrument over kotoba's own r60 Core surface (scoped rule files S103–S109) and r61 errata; no sibling index shows any instrument that re-runs attack instances through a landed counter's arms (chousa r16 classifies findings; it does not measure landed bytes) |
| "absorb" as disposition vocabulary (fix / absorb / named-debt classification table) | chousa | `corpus/knowledge/verification-r16.md`, index row `corpus/README.md:21` @ `f5b11357` | no (term collision only) | **report** — r62 entry must distinguish: chousa "absorb" = record-correction disposition; C1 "absorbed" = measured two-direction arm verdict. Prevents wave-2 conflation |
| Frozen-counter amendment discipline (freeze before data, control-forced named pre-data amendment with re-scored controls, strictness-only, sha256-bound receipts, probe-verified at scored revision) | kumitate | `corpus/knowledge/counter-amendment-discipline.md` + `probe/doctrine49-probe.mjs` (rule D49), index row `corpus/README.md:144` @ `6927903f` | no (ex-ante discipline vs C1 ex-post audit) | **report** — kotoba M90 (controls committed before data) is an instance of kumitate's clause class; credit the correspondence in the routed items, do not import or restate their clauses as kotoba craft |
| Guard-disable sensitivity arm (disable exactly one guard in a disposable copy; binary per guard) + kill-rule controls (hollow/label auditor must fail; isolation arm) | tameshi (method), game-dev-2d (fourth pattern source) | tameshi `corpus/knowledge/verification-patterns-fleet.md` r2 addendum, index row `corpus/README.md:12` @ `51d3f080`; pattern P "cross-lane adversarial layer audits and reports, never fixes siblings" `README.md:9` | no — in-lane application | **apply in-lane, credit the method** — every lane's gate remains its own (kotoba § Adjacent tameshi ruling, round 50); C1 mutates kotoba's own counter, so no tameshi opt-in is triggered; the C1 lesson/registry rows must name the guard-disable class as tameshi-held method (fleet pattern D-series), not a kotoba invention |
| Kill-rate measurement / mutation-testing service over fleet gates | tameshi | `corpus/knowledge/fleet-kill-rate-ledger.md` ("stale successor rows open"), `fleet-suite-census.md`, `service-optin-protocol.md`, index rows `corpus/README.md:49,50,58` @ `51d3f080`; mado precedent: tameshi runner is "a read-only dependency, never mado-owned" (`mado corpus/README.md:23` @ `56ef773a`) | no | **report** — wave-2 "mutation-test both new gates" stays in-lane (own gates); report the three new r62 gates (`check_erratum_absorption.py`, `check_scoped_rules_v31.py`, `check_routed_repairs_v2.py`) to tameshi as candidate census/ledger rows via the routed-items section — never by writing tameshi files |
| (b) Self-derived count: claimed count bound to a live re-derivation command at a measured revision (C2 G-a: `committed <n>` must equal `git ls-tree` seat-file count at rev; claimed must exceed) | **kotoba** (instance) / kagi (technique class) | kotoba `plans/round-62.md` §C2 G-a @ `a1cb8abc`; kagi `corpus/self-counts.py` + `self-counts.tsv`, index lines `corpus/README.md:172-175,219-222` (ledger R25-01/R25-02) @ `899c50b4` | no | **absorb the claim, report the class** — kagi binds its own corpus prose numbers to re-derivation; kotoba binds its own wave-receipt counts; C2's novelty must be scoped to the routed-repairs surface, not to the self-derived-count technique |
| Count-statement reading discipline (no count circulates without its reading id) | kotodama | `knowledge/header-conformance-readings.md`, index line `corpus/README.md:437` @ `ff30a205` | no | **report-only note** — same family as C2's count honesty, domain-local to kotodama's corpus headers; nothing to absorb |
| (b) Honest-pass counter arm (dishonest rejected 6/6 AND honest passed 2/2, both computed from input blobs) | **kotoba** | `plans/round-62.md` §C2 @ `a1cb8abc`; nearest sibling evidence is the failure family, not a landed arm: kaidoku r32 "C2 calibration honest stop because negative prose and word bags pass its frozen counter" (`kaidoku corpus/README.md:214` @ `f432c8e3`); kake r26/r27 rejected-honest-stop rows (`kake corpus/README.md:186,221-232` @ `a377c5d0`) | no | **absorb** — no sibling index shows a hardened counter with an honest-pass arm; siblings recorded honest stops instead. Optional informational report to kaidoku: C2's honest-pass arm addresses the class their r32 stopped on |
| (c) Counter-audit gate of C1's shape: auditor pins a *different* frozen counter's sha256, exits 2 on byte drift, scores arm-level instances, carries hollow/label kill controls committed pre-data | **kotoba** | `plans/round-62.md` §C1 + §Controls @ `a1cb8abc`; nearest siblings: kumitate `doctrine49-probe.mjs` (sha-bound *clause/receipt* bindings, not counter arms) `corpus/README.md:144` @ `6927903f`; chousa gate-baseline r8/r12 self-pin + `--drift` byte-compare (`corpus/README.md:15,17` @ `f5b11357`); kagi claim-ledger "three audit teeth" over rows/stamps (`corpus/README.md:66` @ `899c50b4`); tameshi gates-survey kumitate/kagi (executed *surveys* of other lanes' gates, not committed fail-closed auditors) `corpus/README.md:7-8` @ `51d3f080` | no | **absorb** — no sibling gate audits another counter's arms fail-closed. Etiquette note: C1 audits kotoba's *own* counter, so the tameshi P-pattern cross-lane rule is not triggered; keep it untriggered (never point the auditor at sibling counters without reporting) |
| E2f finding: landed `check_scoped_rules.py` lacks the G7 raw-tokenizer event-claim conjunct and G9 compound-purpose conjunct, so erratum E2f is unabsorbed (plan's declared expectation) | **kotoba** | `plans/round-62.md:64-71` (expected result, declared before data) + `verifiers/check_scoped_rules.py` (r61 freeze, sha `5a5adc94…`); scoped-rules surface S103–S109 is kotoba Core (`PROVINCE.md` § Core, round-60 row) | no | **kotoba owns** — see ruling below |
| S118 source row (`https://code.claude.com/docs/en/memory.md`, Claude Code memory docs) | **kotoba** | `plans/round-62.md` §Frontier step @ `a1cb8abc`; claim sweep over all 20 sibling indexes for `memory\.md|code\.claude|scoped rule|SKILL.md registry|frontmatter`: 0 sibling claims (only kengaku's own census-script line and kumitate's kimi-plane rows match, both unrelated to Claude Code docs) | no | **absorb** — frontmatter/docs craft is kotoba Core; no sibling claims the page or the surface |

Lanes with **zero index hits** across all four sweeps: audio, game-dev-2d, lore, mori,
revenger, souji, tabi, tsukuroi (+ kasegi only domain uses of "honest"). Consistent with
their `none` census classification; no counter-craft adjacency at index level.

## E2f ruling

E2f belongs to **kotoba**, uncontested. Grounds:

1. *Subject instrument*: the finding is a property of kotoba's own frozen counter
   `verifiers/check_scoped_rules.py` (r61 freeze) — its `action_conjunct` lacks the G7/G9
   conjuncts — and its successor `verifiers/check_scoped_rules_v31.py` is a kotoba file.
   No sibling's index names this counter; tameshi's surveyed-gate set (kimi-census,
   surface-census, checklist-run, claims-check, mado-verify, tsukuroi-census) does not
   include it.
2. *Surface*: E2f is an erratum class on the round-60 scoped-rules-by-client surface
   (S103–S109), held as kotoba Core since round 60 (`PROVINCE.md` § Core). The sibling
   claim sweep found no sibling claiming scoped rule files, Claude Code rule/memory
   docs, or a SKILL.md registry audit.
3. *Method only*: what tameshi owns is the mutation/guard-disable **method** used to
   measure absorption (rows 4–5 above), not the finding. Kotoba applying it in-lane to
   its own counter is inside the round-50 ruling ("every lane's gate remains its own");
   the report owes the method credit, nothing more.

Honesty note: ownership is surface-based; I did not re-measure the G7/G9 gap — that is
C1's declared pre-data expectation (`plans/round-62.md:64-71`) and the matrix seats'
job. This scan claims nothing about whether E2f is in fact unabsorbed.

## Must be REPORTED to another lane (never absorbed)

1. **tameshi** — (i) method credit: C1's guard-mutation direction and hollow/label kill
   controls are the tameshi-held guard-disable/kill-rate classes (fleet pattern D-series
   + P-pattern); name them in the C1 lesson and registry rows. (ii) three new r62 gates
   as candidate `fleet-suite-census` / `fleet-kill-rate-ledger` rows (their ledger
   notes open successor rows). Route both via the r62 report's routed-items section
   through the L1; write nothing in tameshi's tree.
2. **kumitate** — M90 (controls committed before data) is an instance of
   `counter-amendment-discipline`'s freeze-before-data / control-forced-pre-data-amendment
   clause class; report the correspondence so the discipline's receipt set can cite a
   second lane's instance if kumitate wants it. Do not restate or import the clauses.
3. **kagi** — C2 G-a's self-derived count is the same technique class as kagi's
   `self-counts.py`/`self-counts.tsv` (R25-01/R25-02); the C2 novelty claim must stay
   scoped to the routed-repairs surface. Informational report.
4. **chousa** (vocabulary only) — r62 prose must keep "absorbed" (measured two-direction
   verdict) distinct from chousa r16's "absorb" (record-correction disposition); one
   sentence in the entry/lesson suffices.
5. Optional, **kaidoku** — informational: C2's honest-pass arm addresses the
   calibration-stop class kaidoku recorded at r32.

Nothing in this scan must be *ceded* to a sibling: all three surfaces stay kotoba.

## Contradictions / risks

- Term collision risk (chousa "absorb" vs C1 "absorbed") is the only wording hazard a
  wave-2 reviewer is likely to flag; pre-empted above.
- The scan is index-lines-only by assignment; a sibling holding an instrument without an
  index row would be invisible. Kotoba's own history shows exactly this failure mode
  (round-48/49/50 spot-checks landed "without an index row"), so the bound is real, not
  theoretical. Stated here so the report does not overclaim.
- Sibling tips moved past their census pins (8 lanes); per-row evidence cites scan-time
  tips. The census checker, not this scan, governs § Adjacent row validity.
- Second-order: if wave 2 mutation-tests the new gates, keep it in-lane (own gates) —
  pulling tameshi's runner in as mado did (read-only dependency, never mado-owned)
  would be the only acceptable external use, and this round does not need it.

Installs: none. Blockers: none.

Attacked/produced: sibling-overlap scan of the three round-62 surfaces across 20 sibling
corpora indexes — all three kotoba-owned and uncontested; four report-not-absorb
adjacencies named (tameshi method + gate-ledger rows, kumitate clause class, kagi
self-count class, chousa vocabulary); E2f ruled kotoba's.
