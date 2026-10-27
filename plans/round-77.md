# Round 77 — plan (kotoba, hyaku run 10, attempt 1)

Date: 2026-10-27. Base: `2f675548eaad2a037a899d39247c1fd7a88aaf48` (r76 closure spot-check tip; lane clean, `ahead=0`). Author: L1 `KotobaR77`.
Two claims on distinct owned axes: **C1 depth (sourced)**, **C2 consistency (calibration sub-axis)**. Depth (9) is the lowest owned axis and C1 works it.

## Trigger

- Round 76 ended as an honest stop: both frozen counters and their self-tests landed, **no claim data landed** (`corpus/lessons/round-76-verifier-spotcheck.md` §1–§5, routed defects R76-D1…D5). Round 77 is the re-land of the same two claims; nothing is narrowed or widened.
- The counters are **not edited**. Their bytes are pinned here (sha256 below). Their file and path names carry `round76` / `round-76` (the entry `corpus/knowledge/description-craft-round76.md`, the lesson `corpus/lessons/round-76.md`, the snapshot set `.ufo/waves/round-76/snapshots/`, the receipts `.ufo/waves/round-76/receipts/…`): the data lands at those names because the counters read them; the report says plainly that it landed in round 77 (R76-D2 asks for `corpus/lessons/round-76.md` explicitly).
- Routed r76 defects handled: **R76-D1** stray `kotoba-shokukin/` path removed; **R76-D2** `corpus/lessons/round-76.md` written (Gate + Mistakes); **R76-D3** = this round's C1/C2; **R76-D4** the two corpus gates (red at base: 2 unindexed spot-check files; baseline totals 144/99/43 vs observed 146/102/44) repaired and the no-harm battery run at the final tip; **R76-D5** an explicit dead-seat count per wave, plus the r76 52-vs-64 report-file reconciliation.
- `considerthese/2026-10-26.md` proposal 3 (description-craft advice + audit of kotoba's own description) is the one proposal mined (it is C1's motivation again); proposals 1/2/4/5 stay declined with the r76 reasons (lesson Gate). Assimilation: none (frozen claims; § Frozen and resumed rounds).

## Frozen counters (bytes unchanged from r76 freeze `ec7f853`)

| counter | sha256 | pre-data base receipt (r77 base) | self-test at base |
|---|---|---|---|
| `verifiers/check_desc_craft.py` | `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` | `.ufo/waves/round-77/receipts/c1-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`: `description craft backed 0 of 6`, exit 1 | `receipts/selftests-base.txt`: 0 failures / 53 assertions, exit 0 |
| `verifiers/check_r75_routed_repairs.py` | `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` | `.ufo/waves/round-77/receipts/c2-base-2f675548eaad2a037a899d39247c1fd7a88aaf48.txt`: `r75 routed repairs closed 0 of 4`, exit 1 | `receipts/selftests-base.txt`: 0 failures / 27 assertions, exit 0 |

The control worlds the r76 receipts hold (`.ufo/waves/round-76/receipts/c1-controls.txt`) were scored on an earlier counter blob (`87837d7a…`, not the frozen `cf3c45d9…`). **They are re-run in this round on the frozen bytes** (seats E01/E02) and committed **before any data commit**; a control that meets the target is a counter defect and stops the round.

## C1 — depth (sourced): description-craft guidance admitted and turned on the lane's own description

Frozen predicate (same sentence in the plan, the counter docstring (r76 base hash there), the receipt label and the SCORECARD row):

> `python3 -B verifiers/check_desc_craft.py --rev <rev>` prints `description craft backed K of 6` and exits 0 only when all six conjuncts hold at `<rev>`; at the r77 base `2f675548eaad2a037a899d39247c1fd7a88aaf48` (the r76 base was `b7f13f4b39cbd43076a85568adca763a6f674e7a`) it prints `description craft backed 0 of 6` and exits 1.

Conjuncts (a)–(f) are exactly `plans/round-76.md` § C1 as corrected by `plans/round-76-addendum-1.md` (digest pinned in four places, not in the S213 anchor), measurement conventions per addenda 1 and 4 (clip-preserving render 1022 / stripped 1021; first sentence 151 characters including the period). Target: K = 6.

Do-nothing controls: base (`0 of 6`); stub entry + empty snapshot set; wrong-page real text; token dump naming all six conjuncts (all four in the counter's self-test and re-run on the frozen blob).

Sourced: S213 (`https://agentskills.io/skill-creation/optimizing-descriptions.md`) is re-opened **in this round** by two independent seats; each records URL, access date, a ≤25-word located quote and the sha256 of the bytes; any digest that differs from the pinned `7cc54fbb…bd837` stops C1 (the page moved) until re-pinned by a new, pre-data addendum.

## C2 — consistency (calibration sub-axis): r75-closure routed defects R1–R4 closed with committed corrections

Frozen predicate:

> `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` prints `r75 routed repairs closed 4 of 4` and exits 0 only when all four repairs hold at `<rev>`; at the r77 base `2f675548eaad2a037a899d39247c1fd7a88aaf48` (r76 base `b7f13f4b39cbd43076a85568adca763a6f674e7a`) it prints `r75 routed repairs closed 0 of 4` and exits 1.

R1–R4 as in `plans/round-76.md` § C2 with `plans/round-76-addendum-5.md` (R2 is the receipt for the r75 final tip `ac9f29510d3914a6edb97c8dbdb3445cab9141de`; the counter re-runs both corpus gates at that revision and compares normalized stdout). Target: 4 of 4.

## Disclosed hygiene work outside the two counters

R76-D1 (stray path), R76-D2 (round-76 lesson, also required by C1 (a)/(e)), R76-D4 (index + baseline + battery), D2/D3 of r74 (`LOG.md` § Round 74 `d5aebcf` line; forward pointer in `corpus/knowledge/sibling-overlap-census-round49.md`; drafts `.ufo/waves/round-76/build/B10RepairD2D3.*`), R76-D5. None of these is claimed as an axis move; they are reported as landed or open.

## No-harm battery (every item re-run at the final tip, receipts in `.ufo/waves/round-77/receipts/`)

`verify_corpus_integrity.py --json`, `verify_corpus_independent.py --json` (both exit 0 after the repair), `check_gate_registry.py --rev`, `check_assertion_floors.py`, `check_tip_battery.py --rev`, `verify_skill_checklist.py --json`, `check_skill_evals_v2.py --rev`, census (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`, exit 0), `SKILL.md` ≤ 600 lines (590 at base). Every receipt captures the **gate's own** exit status (no `| tail` pipelines — the r76 pipeline-exit defect).

## Wave shape (two v1 waves, ≤128 seats)

- **w1 build (≈40 seats, policy v1):** controls on the frozen blobs, the data drafts verified in a scratch clone against the frozen counters, S213 re-opens, hygiene repairs, scribes for lessons/LOG/SCORECARD drafts, a connector sibling-overlap scan, and first falsifiers (counter mutation, hollow-claim critics, quote/row reviewers, sentinel). L1 integrates after w1 settles; no claim data lands in the lane before the freeze + controls commits.
- **w2 falsify (≥32 seats, policy v1):** reviewers/critics/mutation-testers/scouts attack the **landed** tip: re-run each counter, re-open each quote, attack each claim, review each new entry/row/criterion, mutate each touched gate, re-run the no-harm battery.
- The L1 holds the canonical planner seat; a bounded planning data-walk rides a scout/connector item.

## Landing order (lane commits only through `jj-lane.sh`)

1. freeze: this plan + base receipts; 2. controls + wave-1 evidence; 3. data: entry, snapshot-chain data is already committed from r76, SKILL.md row, S213 used-by, lessons, R1–R4 repairs, index + baseline; 4. after w2: corrections, SCORECARD/LOG/QUALITY rows, round lesson; report on the fleet repo last, citing the pushed lane hash.
