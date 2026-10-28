<!-- DRAFT — report body for .ufo/reports/round-80/kotoba.md (lane-relative; the L1
files it after the wave integrates). FILL NOTE, delete this block before filing:
every double-brace marker is a claim value the L1 fills from the receipt named on the
same line or listed in the marker register at .ufo/waves/round-80/w1/Kb80S04Report.md,
which also carries the exact commands and the pointer rules. Base values below are
transcribed from the committed base receipts named beside them; no after-value is
measured in this draft. Capture every verdict from the command's own exit status
(cmd > f 2>&1; rc=$?; printf 'exit=%s\n' "$rc" >> f) and never from a pipeline:
a pipeline reports its last element's status (round-80 lesson M80-1, shown in
.ufo/waves/round-80/receipts/m80-1-pipe-vs-direct.txt). -->

# Kotoba round 80 — {{ROUND_OUTCOME_HEADLINE}}

## Work performed

Declared claims, frozen in `plans/round-80.md` before any after-value was measured:

- **C1 consistency (calibration sub-axis).** `python3 -B verifiers/check_tip_battery.py --rev <rev>` — the round-72 frozen counter amended by erratum E5 (`LINE_CAP` 40→60 and `INSTRUMENT_PINS` gaining exactly the two reviewed instrument blobs, no other line; counter and pin sha256 recorded before data in `{{FREEZE_RECEIPT}}`) — is the claim's target at `guards 5 of 5` and `tip battery exit 0: 6 of 6`, exit 0, at the landed tip, in both the `--repo .` form and the absolute `--repo <lane>` form. Base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (measured, own status): `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 (`receipts/tipbattery-base-dot.txt`).
- **C2 depth (sourced; form backbone measured, grant-semantics rider exploratory).** `python3 -B verifiers/check_allowed_tools.py --rev <rev>` targets `allowed-tools surfaces documented 6 of 6`, exit 0 iff N == 6 and the tree conjuncts (g)–(i) hold, with the generator world's score printed beside the headline (`generator world: <M> of 6`). Base: `allowed-tools surfaces documented 0 of 6`, exit 1 ({{C2_BASE_RECEIPT}}). The headline asserts FORM-LEVEL documentation only (Q71/Q74); the grant-semantics matrix is the exploratory rider, reviewers of record the round-80 non-author closure spot-check ({{CLOSURE_POINTER}}).

- Read and bounded the mission, base and ports: `plans/round-80.md`; base receipts `receipts/tipbattery-base-dot.txt`, `receipts/census-before.txt`, `receipts/m80-1-pipe-vs-direct.txt`; r79 drafts `.ufo/waves/round-79/build/Kb79E01Registry.patch`, `.ufo/waves/round-79/build/Kb79E02LogCitation.patch`, `.ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch`, `.ufo/waves/round-79/build/refresh-corpus-baseline.py`, `.ufo/waves/round-79/build/check_allowed_tools.py`, `.ufo/waves/round-79/build/Kb79A02EntrySkeleton.md`, `.ufo/waves/round-79/w1/Kb79K03SemanticMatrix.md`, `.ufo/waves/round-79/snapshots/`. Ported anchors were re-derived from the bytes at `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`, not from the r79 diff context ({{PORT_NOTE}}).
- C1 repair 1, registry: `SKILL.md` § Gate registry gains the `check_desc_craft.py` and `check_r75_routed_repairs.py` rows (Q46 `claim withdrawn` cells) plus a conformant row for the new `verifiers/check_allowed_tools.py`; registry gate at the tip {{V_REGISTRY_TIP}} (`{{TIP_OUT}}/03-gate-registry.txt`).
- C1 repair 2, dead LOG citation: `.ufo/reports/round-76/kotoba.md` is a relative symlink to the fleet report (one artefact, one byte-stream, sha256 `{{SYMLINK_SHA}}` equal to the fleet file; the four-hop target string is never written backticked in tracked prose); the checklist governance arm returns `{{V_CHECKLIST_TIP}}` (`{{TIP_OUT}}/05-skill-checklist.txt`).
- C1 repair 3, index and baseline: coverage-map rows for `corpus/lessons/round-79-verifier-spotcheck.md`, `corpus/lessons/round-80.md` and `corpus/knowledge/allowed-tools-surfaces-round80.md`; `.ufo/waves/round-79/build/refresh-corpus-baseline.py` run as `--repo .` from the lane root then re-records `verifiers/corpus-baseline.json` at the final pre-report commit from a clean tree ({{BASELINE_NOTE}}).
- C1 repair 4, dead report pointer: `verifiers/verify_corpus_integrity.py` resolves `<rev>:<path>` report pointers as git object expressions, repo first then fleet (`git cat-file -e`), with its red-before regression arm; diff {{E04_DIFFSTAT}}.
- C1 repair 5, external-commit grammar class (both corpus gates): a hex token in the `owner/repo@<hex>` grammar is classified as an external commit citation, outside the gates' declared lane/fleet resolution set (Q61) and counted in its own INFO class instead of `commit_unresolvable`; lane and fleet tokens keep their exact current resolution behaviour; both self-tests carry red-before arms ({{GRAMMAR_RECEIPT}}).
- Erratum E5: `verifiers/check_tip_battery.py` changes exactly `LINE_CAP` 40→60 and the two reviewed instrument blobs in `INSTRUMENT_PINS`; no guard check edited (plan § C1 kill rule). Diff {{E5_DIFFSTAT}}; sha256 {{E5_SHA}} in `{{FREEZE_RECEIPT}}` before any after-value.
- C1 control worlds W0–W8 on the round-80 counter bytes, receipts committed before any after-value: {{W_SUMMARY}}; none reached `6 of 6` ({{W_RECEIPT}}). A two-line stub fails the size guard (W6) and any instrument edit outside the pin table fails `instrument-pin`.
- C2 counter built from the r79 draft and frozen: `verifiers/check_allowed_tools.py`, sha256 {{C2_SHA}} in `{{FREEZE_RECEIPT}}`; self-test {{C2_SELFTEST}}; base `allowed-tools surfaces documented 0 of 6`, exit 1 ({{C2_BASE_RECEIPT}}); controls C0–C8 scored on the frozen bytes before data: {{C2_CTRL_SUMMARY}} ({{C2_CTRL_RECEIPT}}); generator world `{{C2_GENERATOR_M}} of 6` (Q71/Q74).
- C2 entry and tree conjuncts: `corpus/knowledge/allowed-tools-surfaces-round80.md` holds rows S226–S231 with `used-by` moved to the round-80 entry ({{TOUCHED_ROWS}}); the six snapshot pins equal the manifest, the row fetch records and the counter ({{SNAP_NOTE}}); the six pages were re-opened live on 2026-10-27 ({{REOPEN_RECEIPT}}); `SKILL.md` carries one rule line naming ≥3 surfaces plus the counter's registry row ({{SKILL_RULE}}); `PROVINCE.md` `## Core` names the entry ({{PROVINCE_LINE}}).
- Frontier: census before exit `{{CENSUS_BEFORE_EXIT}}`, 157 rows, 24 W04 warnings, terminal line `ok` (`receipts/census-before.txt`; `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 157 at `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`). NEW rejection rows from the negative sweep, ids from S232, each opened this round with URL, access date and ≤25-word located quote in `corpus/lessons/round-80.md` `## Gate` ({{NEW_ROWS}}).
- Mistake mined into `corpus/lessons/round-80.md` `## Mistakes`: M80-1, a gate verdict read through a shell pipeline (`cmd | tail` printed `rc=0` while the gate's own exit was 1, and `--json | tail` hid the DRIFT lines); class `measurement`, captured-by `none`, fix own-status capture; both capture forms are receipted in `receipts/m80-1-pipe-vs-direct.txt`.
- Assimilation: the kotoba quarantine-register slice hand-checked {{ASSIMILATION}}; `merge/kotoba/` read-only with nothing appended; `considerthese/2026-10-26.md` proposals 2–5 dispositions recorded in the lesson `## Gate` ({{PROPOSALS}}).
- Round shape: one validated v2 wave, w1 = 64 seats, build + attack together — 16 executors, 17 scribes, 9 scouts, 3 connectors, 6 critics, 6 reviewers, 4 mutation-testers, 1 sentinel, 1 simplifier, 1 revenger; attack share 17/64 = 26.6 %. Role census: `python3 -c "import json,collections;c=collections.Counter(i['role'] for i in json.load(open('.ufo/waves/round-80/w1-spec.json'))['items']);print(c);print('attack',sum(c[r] for r in ('critic','reviewer','mutation-tester','sentinel')),'of',sum(c.values()))"` → `{{ROLE_CENSUS}}`. Results: {{SEAT_RESULTS}}.
- No-harm battery at the final pre-report tip, run by `.ufo/waves/round-80/build/run-battery.sh` into `{{TIP_OUT}}` (index `{{TIP_OUT}}/index.txt`); every value in § Before → after cites its own receipt from that directory ({{BATTERY_SUMMARY}}).
- Misroot sweep after the last seat settled: {{MISROOT}}.

## Landed changes

- Integration commits: {{LANE_COMMITS}}. Seats produced patches, drafts and receipts under `.ufo/waves/round-80/build/` and reports under `.ufo/waves/round-80/w1/`; the L1 is the only committer and integrated after the wave (freeze discipline; no seat scored a claim after-value).
- Files changed: `SKILL.md` ({{SKILL_DIFFSTAT}}); `.ufo/reports/round-76/kotoba.md` (symlink, {{SYMLINK_DIFFSTAT}}); `corpus/README.md` ({{README_DIFFSTAT}}); `verifiers/corpus-baseline.json` (refresh, {{BASELINE_DIFFSTAT}}); `verifiers/verify_corpus_integrity.py` ({{E04_DIFFSTAT}}) and `verifiers/verify_corpus_independent.py` ({{GRAMMAR_DIFFSTAT}}); `verifiers/check_tip_battery.py` (E5, {{E5_DIFFSTAT}}); `verifiers/check_allowed_tools.py` (new, {{C2_DIFFSTAT}}); `corpus/knowledge/allowed-tools-surfaces-round80.md` ({{ENTRY_DIFFSTAT}}); `corpus/lessons/round-80.md` ({{LESSON_DIFFSTAT}}); `corpus/SOURCES.md` ({{SOURCES_DIFFSTAT}}); `PROVINCE.md` ({{PROVINCE_DIFFSTAT}}); `LOG.md:{{LOG_LINE}}`; `SCORECARD.md:{{SCORECARD_LINE}}`; `plans/round-80.md` outcome append ({{PLAN_OUTCOME}}).
- No fleet-root tracked file was written and no sibling lane was touched; `shokuknow` stayed read-only.

## Before → after measurements

- **C1 consistency/calibration — {{C1_VERDICT}}.** Base `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 at `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (`receipts/tipbattery-base-dot.txt`) → tip `{{C1_TIP_REV}}`: form A `{{C1_AFTER_A}}` (`{{TIP_OUT}}/01-tip-battery-dot.txt`, receipt `cwd=` {{C1_CWD_A}}), form B `{{C1_AFTER_B}}` (`{{TIP_OUT}}/02-tip-battery-abs.txt`, receipt `cwd=` {{C1_CWD_B}}); exits {{C1_EXITS}}.
- **C2 depth (form backbone) — {{C2_VERDICT_FORM}}.** Base `allowed-tools surfaces documented 0 of 6`, exit 1 ({{C2_BASE_RECEIPT}}) → tip `{{C2_TIP_REV}}` `{{C2_AFTER}}`, `generator world: {{C2_GENERATOR_M}} of 6`, exit {{C2_EXITS}} ({{C2_TIP_RECEIPT}}).
- **C2 exploratory rider (grant semantics) — {{C2_SEMANTICS_VERDICT}}.** No number by design: `SCORECARD.md:{{SCORECARD_LINE}}` carries the verdict and the reviewer pointer {{CLOSURE_POINTER}}.
- **No-harm battery, own-status receipts in `{{TIP_OUT}}`.** Gate registry `{{V_REGISTRY_TIP}}` (`03-gate-registry.txt`, exit {{E_REGISTRY}}); assertion floors `{{V_FLOORS_TIP}}` (`04-assertion-floors.txt`, exit {{E_FLOORS}}); skill checklist `{{V_CHECKLIST_TIP}}` (`05-skill-checklist.txt`, exit {{E_CHECKLIST}}); corpus integrity `{{V_INTEGRITY_TIP}}` (`06-corpus-integrity.txt`, exit {{E_INTEGRITY}}); corpus independent `{{V_INDEPENDENT_TIP}}` (`07-corpus-independent.txt`, exit {{E_INDEPENDENT}}); correction sweep exit `{{E_SWEEP}}` (`08-correction-sweep.txt`); census `{{V_CENSUS_TIP}}` (`09-census.txt`); sibling census `{{V_SIBLING}}` ({{SIBLING_RECEIPT}}); report pointers `{{V_POINTERS}}` (`15-report-pointers.txt`).
- **SKILL.md size at the tip** (ceiling ≤600 lines): `{{TIP_OUT}}/10-skill-lines.txt` `{{SKILL_LINES}}`, `{{TIP_OUT}}/12-skill-long120.txt` `{{SKILL_LONG120}}`, `{{TIP_OUT}}/13-skill-long300.txt` `{{SKILL_LONG300}}`.

## Sources & frontier

- `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` before → exit `{{CENSUS_BEFORE_EXIT}}`, 157 rows, 24 W04 warnings (`receipts/census-before.txt`); after → exit {{CENSUS_AFTER_EXIT}}, {{CENSUS_AFTER_ROWS}} rows, {{CENSUS_AFTER_W04}} W04 warnings ({{CENSUS_FINAL}}). Row count command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 157 before, {{ROWS_AFTER}} after.
- Added by tier: A={{TIER_A}}, B={{TIER_B}}, C={{TIER_C}}; existing rows touched old→new {{TOUCHED_ROWS}} (S226–S231 `used-by` moved to the round-80 entry; no other cell changed); frontier rows advanced {{ADVANCED}}.
- Sourced claim: C2 rests on S226–S231, re-opened this round, plus {{NEW_ROWS}}; every quote is ≤25 words, located after the page's first heading (Q70), and every snapshot pin is equal in the manifest, the row's fetch record and the counter.
- Assimilation: {{ASSIMILATION}}; `merge/kotoba/` read-only; `considerthese/2026-10-26.md` proposals 2–5 {{PROPOSALS}}.

## Trend verdicts

- **expansion — {{EXPANSION_VERDICT}}:** {{EXPANSION_EVIDENCE}}
- **quality — {{QUALITY_VERDICT}}:** {{QUALITY_EVIDENCE}}
- **discernment — {{DISCERNMENT_VERDICT}}:** {{DISCERNMENT_EVIDENCE}}

## SHONEN

[{{SHONEN_MARK_1}}] Decision tables/error patterns/checklists: {{SHONEN_TEXT_1}} (`SHONEN.md:5-6`).
[{{SHONEN_MARK_2}}] End-to-end domain task executed and logged: {{SHONEN_TEXT_2}} (`SHONEN.md:7-8`; `LOG.md:{{LOG_LINE}}`).
[{{SHONEN_MARK_3}}] Instructions executable without oral context: {{SHONEN_TEXT_3}} (`SHONEN.md:9-10`).
[{{SHONEN_MARK_4}}] No cross-domain bleed and PROVINCE accurate: {{SHONEN_TEXT_4}} (`PROVINCE.md`; `SHONEN.md:11-12`).

Stale-lane: {{STALE_LANE}}.
Tool installs/updates: {{TOOL_INSTALLS}}.
Open L0 questions: {{L0_QUESTIONS}}.
Lane final pushed hash: {{LANE_FINAL_HASH}}. {{CLOSING_HONESTY}}
