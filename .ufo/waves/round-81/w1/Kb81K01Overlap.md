# Kb81K01Overlap — sibling overlap for round 81 (C1 tip battery, C2 SDK allowed-tools)

Seat: Kb81K01Overlap (leaf, sibling-overlap + related-lane patterns). Read-only. No subagents, no edits outside this report.
Base: kotoba `b284223105f4d106f7e8f56ed4fd296c643cda0e` (lane HEAD read: `b2842231`).

## Method and sweeps

- Authority read: `plans/round-81.md` (C1 at lines 11–30; C2 at lines 32–42), `PROVINCE.md` § Adjacent (rows at lines 42–76), `corpus/knowledge/sibling-overlap-census-round74.md` (classification and boundary cells at lines 53–103).
- Sibling reads at **current** HEAD (not the round-74 freeze). Heads read by `git -C <lane>-shokunin rev-parse --short=8 HEAD`:
  - kengaku `3a548330` (round-74 pin `f9efce3b`; the pin is stale, and every grep below ran at HEAD, which is newer than the pin)
  - kumitate `14057f3e` (round-74 pin `2ca91a0c`; stale)
  - tameshi `abae0a04` (round-74 pin `a944eb55`; stale)
  - kotoba `b2842231`
- Negative sweep for kengaku, `git -C kengaku-shokunin grep -n -i -E "allowed|sdk|tool permission|pre-approv|permission" HEAD -- SKILL.md PROVINCE.md corpus/README.md` → one hit, `SKILL.md:845` ("the instruction's permission (`instruction.md:3`) is untested"), which concerns an instruction file, not a tool grant. `corpus/knowledge/` filenames grep for `tool|agent|skill|grant|harness` → only `agent-time-horizon-and-task-validity.md`.
- kumitate: `git grep` for `check_|counter|verifiers/|counter` over `PROVINCE.md SKILL.md`; `scripts/` listing for `counter|pin|rerun|gate`.
- tameshi: `git grep` for `do-nothing|shortcut world|control world|negative control|positive control|falsifying|killing world` over `PROVINCE.md SKILL.md corpus/knowledge/`; direct reads of `corpus/knowledge/guard-kill-closure.md:14-29`, `runner-tally-audit-v2.md:53`, `oracle-anchored-survivors.md:54`, `arm-class-matrix.md:81`, `repeated-control-precondition.md` head.
- kotoba-side: `grep -l sha256|INSTRUMENT_PINS verifiers/check_*.py` (20 files listed); import census across the 52 `verifiers/check_*.py` files (stdlib-only imports; no `from verifiers`/cross-lane import); `kotoba SKILL.md:12-16` and `erratum-absorption-round62.md:39` (precedent).
- Plan grep for `tameshi|kumitate|kengaku|counter-pins|counter-rerun|c1_controls|grant` in `plans/round-81.md` → only line 34 (`grant channel`, the SDK surface). The plan cites no sibling method.
- Existence checks: `verifiers/check_sdk*` → absent (expected: the counter is this wave's build output). `.ufo/waves/round-81/build/` → empty. `c1_controls.py` → not present anywhere in the lane yet. The C1 control designs can therefore be assessed at design level only (plan text plus the r80 receipts), and I make no claim about the file's code.

## Lane-by-lane

### (a) kengaku — measured-prompt-effects domain: **overlap NO** (confirmed; bleed not found)

- kengaku's PROVINCE (`kengaku-shokunin/PROVINCE.md:3`, Refusals at its § Refusals line "kotoba: prompt- and skill-craft rules, render/trigger behaviour — this lane keeps the *measured* effect of prompt format on capability and hands the reusable craft implication out") owns measured effects. kotoba's C2 (`check_sdk_allowed_tools.py`, S249, form-level documentation) reads only what the Agent SDK skills page documents about the `allowedTools`/`allowed_tools` channel and a managed-settings override. Nothing in kengaku HEAD mentions the SDK grant channel, `allowedTools`, or `allowed-tools` (sweep above).
- **Boundary line (for the census row, not yet present):** kotoba records what a client documents about a grant channel (form, grant wording, located quote); whether a grant changes model or tool behaviour when measured is kengaku's measured-capability ground. C2's grant-semantics rider is labelled exploratory and stays documentary; a client run of `allowedTools` against a model would be kengaku's, and kotoba must not report one.

### (b) kumitate — dispatch-tooling domain / counter infrastructure: **overlap PARTIAL — pattern-level yes, code-level NO**

- kumitate owns Node gates in its own `scripts/`: `counter-pins.mjs` (round 54, contract `kumitate-counter-pins-v1`, pins frozen counter sha256 from `.ufo/pins/counter-pins.json`) and `counter-rerun.mjs` (round 48, repeat-run stability comparator for a frozen counter; header says "knows nothing about what the counter measures"). Both are kumitate-internal.
- kotoba's `check_sdk_allowed_tools.py` does not import, read, or invoke either. kotoba's counters are stdlib-only Python (52 `verifiers/check_*.py` files; no cross-lane import found). Its own pin mechanisms already exist: `check_tip_battery.py` `INSTRUMENT_PINS`, `.ufo/waves/round-81/receipts/freeze-shas.txt`, and `check_gate_registry.py`.
- So the frozen-counter-with-pinned-bytes idea is shared method (kumitate `counter-pins` ↔ kotoba `INSTRUMENT_PINS`); the code is not shared, and nothing in C2 duplicates a kumitate script.
- **Boundary line:** kumitate's `counter-pins` and `counter-rerun` police kumitate's own counters; kotoba's counters police kotoba's bytes; neither lane imports the other's gate. The C2 counter is a corpus-documentation check over `corpus/` and does not touch dispatch tooling, so kumitate's `PROVINCE.md:28` routing ("Prompt and skill craft → kotoba") holds unchanged.
- **Recommendation (optional, not required for C2):** if C2 wants repeat-run evidence, it can apply kumitate's round-48 repeat-run rule as cited method (run the counter K times; the summary line must agree) without invoking kumitate's script. No code is to be copied. A decision to call kumitate's script read-only would be a new runtime coupling and is out of scope for this seat.

### (c) tameshi — fixture/mutation method: **overlap YES (method). Reuse is real but uncited in the plan.**

- tameshi owns the reusable method (`tameshi-shokunin/PROVINCE.md:3-15`; kotoba's own `SKILL.md:14` says "tameshi owns the fixture and mutation method"). Its published method for a guard-kill claim is `corpus/knowledge/guard-kill-closure.md:14-29`: a guard counts as covered only when (a) pristine green holds (the unmodified selftest exits 0; a nonzero pristine exit is could-not-evaluate, never "closed") and (b) the kill leg (the selftest exits nonzero when the guard text is removed). It also states "A mutant that survives is not behavioural coverage" and the meta-cheat rule (a case that hashes its own source kills everything).
- Tameshi's control taxonomy in `runner-tally-audit-v2.md:53`: "controls (do-nothing, always-pass, always-fail, sha-only) are authored by…". `oracle-anchored-survivors.md:54` adds a negative control; `arm-class-matrix.md:81` names positive controls.
- kotoba's round-81 designs map onto that taxonomy one-to-one in substance, but the plan does not name the source:
  - W0 "empty commit on base" = do-nothing control (tameshi `runner-tally-audit-v2.md:53`).
  - W4 "failing checks stubbed inside any battery instrument" = the kill leg of `guard-kill-closure.md:14-29`; the expected `instrument-pin`/`instrument-size` failure is the kill.
  - W5 "spot-check file edited" = a single-occurrence mutant on a guarded byte.
  - C4 "first-answer baseline (assert 1 with no files)" = do-nothing control on C2.
  - The pristine-green leg of `guard-kill-closure.md` §1(a) has no explicit row in the r81 plan's C1/C2 control lists.
- Precedent exists in kotoba's own corpus: `corpus/knowledge/erratum-absorption-round62.md:39` says "Guard-disabled flip arm, hollow/label kill controls, isolation arm — tameshi's method (`tameshi-shokunin/corpus/knowledge/guard-kill-closure.md:14-29`) … Borrowed as method, no tameshi domain content imported." The round-81 controls should follow that precedent.
- **Reuse versus reinvention verdict:** reuse of method, not reinvention. The control set is the tameshi taxonomy under kotoba names (W0…W10, C0…C4). The plan cites no tameshi source, which conflicts with the lane's own `SKILL.md:14` and with the round-62 precedent.
- **Boundary line:** kotoba applies tameshi's published method to its own gates and does not claim it as general. Per `tameshi PROVINCE.md` (a pattern is admitted from evidence in two independent lanes before it is general), kotoba's controls are a lane-local application.
- **Concrete repair (design, for the C1 control file header or the plan's control list):** cite `tameshi-shokunin/corpus/knowledge/guard-kill-closure.md:14-29` (two legs) and `runner-tally-audit-v2.md:53` (control taxonomy) as the method, with the line "borrowed as method, no tameshi domain content imported", and name the pristine-green leg explicitly as a row (the tip itself must exit 0 at the frozen `<rev>`, measured in both forms). Do not copy tameshi's selftest code into kotoba.

## Freshness and census findings (no verdict change)

- **Round-74 pins are stale at HEAD** for the three rows read: kengaku `f9efce3b`→`3a548330`, kumitate `2ca91a0c`→`14057f3e`, tameshi `a944eb55`→`abae0a04`. The census rows still show the round-74 commit cell; `check_sibling_reread.py` would report this. This seat re-read HEAD, not the freeze, so the negative findings above are stronger (newer bytes), but the census row itself is not re-pinned by this seat. Re-pin is out of this seat's scope (the census is L1-frozen).
- The `tameshi` census row (`PROVINCE.md:75`, `fleet-kill-rate-ledger.md:127`) says kotoba's `verifiers/*` are "unsurveyed sightings" there. The round-81 `check_sdk_allowed_tools.py` will be one more unsurveyed sighting unless a survey admits it. This is the same status as the r80 counter and is not a new overlap.

## Per-lane summary

| lane | overlap | boundary line |
|---|---|---|
| kengaku | NO | kotoba documents a grant channel's form and grant wording; a measured effect of a grant on model/tool behaviour is kengaku's ground. C2 rider stays documentary. |
| kumitate | PARTIAL: method yes (frozen-counter pins, repeat-run), code NO | kumitate's `counter-pins`/`counter-rerun` police kumitate's counters; kotoba's counters police kotoba's bytes; no import either way; dispatch routing `PROVINCE.md:28` unchanged. |
| tameshi | YES: method reuse, uncited in the plan | Applied as method (round-62 precedent). Cite `guard-kill-closure.md:14-29` and `runner-tally-audit-v2.md:53`; name the pristine-green leg as a row; never claim the method general. |

## Operational notes for the wave

- Nothing in this seat blocks C1 or C2. The overlap findings are citation and boundary repairs, not scope changes.
- No file under `verifiers/`, `corpus/`, `plans/` or the sibling repos was written. No scratch directory was created; nothing to clean.
- Tooling: none installed or updated by this seat. pacman not touched.

VERDICT: no sibling overlap blocks round 81; kengaku NO, kumitate partial (method-level only), tameshi YES on method and under-cited in the plan (add the tameshi citation and the pristine-green row to the C1/C2 control lists).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81K01Overlap.md
