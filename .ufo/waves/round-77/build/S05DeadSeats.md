# S05DeadSeats — R76-D5 dead-seat reconciliation (r76 w1, 64 seats vs 52 report files)

Inputs (committed at ec7f853): `.ufo/waves/round-76/w1-results.json`, `w1-dispatch.json`, `w1-spec.json`, `w1/*.md`.
Script: `build/S05DeadSeats.parse_results.py` (sha256 dc3d985476e6b994d3e4bb6f809e43ae8d993faf275c6f79c7523f0e32486a2b; stdout only, exit 0).
Raw run: `build/S05DeadSeats.r76-table.txt`.

## 1. Facts about the data (observed)
- results.json keys per seat: `name, agent, output, note`. **There is no status field.** `note` is null for 64/64; dispatch registry `agentId` is null for 64/64 and `kind` is `spawn` for 64/64 (no resumes). `agent` == spec `role` for 64/64 (executor 15, scribe 10, reviewer 10, scout 10, critic 6, mutation-tester 4, simplifier 3, revenger 3, sentinel 2, connector 1). Names: 64 unique in results == 64 in dispatch taskCall.tasks == 64 in spec items, same order.
- `ls w1/` = 53 entries: 52 `<Seat>.md` + `swarm-registry.json`. 64 - 52 = **12 seats without a report file** (exact names below). No extra report file lacks a seat.
- Every dispatched task text ends `Report: write your scoped findings to .ufo/waves/round-76/w1/<Seat>.md` (64/64 verified by regex), so the expected path is unambiguous. The 12 absentees did not write it anywhere else either: grep of their names in `build/`, `receipts/`, `w1/` hits only `swarm-registry.json` for 10 of them; B06 and B07 appear in *other seats'* reports/receipts (they are mentioned, not authors of a report).
- `output` shape (64): 57 JSON objects (all parse with `json.loads`; none fenced, none prose-wrapped), 5 plain text narration, 2 beginning `<think>`. **0 of 64 outputs has a top-level plain `VERDICT:` line**; 5 carry one nested in a JSON string/`verdict_line` (B03, B05, B14, B15, A26). So the r76 instruction "wrap your final text so a plain-line parser can read your verdict line" was not honoured; verdicts live under JSON keys (`verdict` 45, `verdict_line` 4, `finding` 2, `counterexample` 1, none 4). Of the 52 report files, 29 end in a `VERDICT:` line, 23 do not (the `VERDICT:`/`DELIVERABLES:` last-lines rule is new in r77).

## 2. Definitions and status values
Status is DERIVED from the final `output` (report file only supplies a fallback verdict text):
- DONE (45): verdict present. BLOCKED (8): structured `error`/`aborted` or verdict starting BLOCKED/INCONCLUSIVE/ABORT. NOVERDICT (4): JSON final but no verdict-ish key (B16, B17, B23, B24 — all have report files and landed work). UNYIELDED (7): final output is narration/`<think>`, i.e. the seat never reached `yield`. EMPTY (0).
- **Dead seat = UNYIELDED or EMPTY and no report file** (nothing recoverable). **Dead-seat count = 6** (B06, B07, A04, A07, A23, B28). Wider view: UNYIELDED = 7 (B11 also ended in narration but wrote its report: "unyielded with file", recoverable). NOREPORT = 12.
- Under the strictest reading (any seat that did not produce its assigned deliverable): 12.

## 3. The 12 seats with no report file, and why (read from their `output`)
| seat | role | class | what the final output shows |
|---|---|---|---|
| B06DescCounter | executor | DEAD (unyielded) | 2281 B narration ending "…then write my seat report" — died/cut before the report; its counter work DID land (`verifiers/check_desc_craft.py` is tracked) and its receipts exist (`receipts/c1-base-…`, `c1-controls.txt`) |
| B07RepairCounter | executor | DEAD (unyielded) | 947 B narration ending "write the controls receipt"; counter landed (`check_r75_routed_repairs.py` tracked), receipts `c2-*` exist, no report |
| A04RevCounterRepairs | reviewer | DEAD (unyielded) | narration mid-investigation about a clone HEAD (7eed80e9 vs 4de12b6), cut mid-sentence |
| A07RevNoHarm | reviewer | DEAD (unyielded) | 16700 B `<think>` stream mid-analysis, never wrote a report |
| A23ScoutSources | scout | DEAD (unyielded) | 571 B `<think>` deliberating whether it may write a snapshot/where to curl; never fetched/reported |
| B28EvidencePackager | executor | DEAD (unyielded) | narration while polling for counters owned by B06/B07; ended "wait for stability" |
| A03RevCounterDesc | reviewer | BLOCKED, inline | JSON verdict "BLOCKED — assigned verifier absent"; says `report: Could not write… no report file was created` (returned inline, chose not to write) |
| A10MutRepairs | mutation-tester | BLOCKED, inline | `{"aborted":true,"error":"Blocked: … no PLANS/ROUND-76.MD or verifiers/check_r75_routed_repairs.py"}` |
| A12MutArms | mutation-tester | BLOCKED, inline | `{"error":"Blocked: … plan, both verifiers, PLANS/ absent"}` |
| A31RevD4 | reviewer | BLOCKED, inline | INCONCLUSIVE — D4 floor bump absent in the working tree |
| A36ScoutReceiptGreen | scout | BLOCKED, inline | BLOCKED/NOT RUN — counter absent |
| A08RevFreeze | reviewer | inline finding | FINDING "freeze integrity cannot be verified … counter files absent"; `report_path: null` (parser tags it DONE because the verdict is a finding, but it is the same absence-of-inputs class) |

Cause pattern: 6 of 12 (A03, A08, A10, A12, A31, A36) were *attackers dispatched in the same wave as the artifacts they attack* (counters, D4 floors, freeze receipts) and found the lane tree empty — a wave-ordering defect (build seats and falsifier seats ran concurrently), they returned the blocker inline and did not write a report. The other 6 are unyielded deaths (no `yield`, output ends mid-narration). 4 of those are builders/packagers/reviewers racing on the same moving tree (B06/B07/B28/A07 mention peers/siblings in their tail); [INFERENCE] termination by session budget/timeout, since the data records no error object (`note` is null, no agentId).
Opposite direction: A01RevQuoteLocate HAS a 1476 B report but its output is `{"aborted":…,"error":…}` (blocked on missing draft), and A09/A11 are BLOCKED/INCONCLUSIVE with reports. So "report file present" does not imply "seat succeeded": 8 BLOCKED seats include 3 with a file.

## 4. Per-seat table (64 rows; generated by the script)
| name | agent | status | report | outlen | vsrc | verdict |
|---|---|---|---|---|---|---|
| B01PlanConsistency | executor | DONE | y | 16843 | json-key:verdict | 3 findings — 1 blocking, 2 material. The plan's Q73 sweep conclusion is FALSE as written: the planned touch l… |
| B02SkillBudget | executor | DONE | y | 10007 | json-key:verdict | SKILL.md is at 590 of 600 lines at HEAD; the planned three additions project to 593 lines (margin 7); anchors… |
| B03SnapshotFetch | executor | DONE | y | 9527 | json-line | PASS — 3/3 pages fetched HTTP 200 and pinned; pinned sentence at optimizing-descriptions.md:92. |
| B04QuotesScribe | scribe | DONE | y | 5942 | json-key:verdict | DONE — 13 page-unique located quotes verified against S213 snapshot bytes |
| B05AuditExec | executor | DONE | y | 16351 | json-line | kotoba's own committed description is COMPLIANT with S213's hard 1024-character ceiling and with its scope-st… |
| B06DescCounter | executor | UNYIELDED | n | 2281 | none | - |
| B07RepairCounter | executor | UNYIELDED | n | 947 | none | - |
| B08LessonDrafts | scribe | DONE | y | 6812 | json-key:verdict | 3 drafts delivered under .ufo/waves/round-76/build/, applied to zero lane files; numbers re-derived from comm… |
| B09RepairR3R4 | executor | DONE | y | 5630 | json-key:verdict | R3 and R4 drafts complete and grounded: R75Attack28 names the absent report kotoba-shokunin/.ufo/waves/round-… |
| B10RepairD2D3 | scribe | DONE | y | 7493 | json-key:verdict | DRAFTS-COMPLETE (report only; nothing applied) |
| B11RepairD4 | executor | UNYIELDED | y | 8920 | file | D4 CLOSED — floors landed in one change (registry + both in-file tables + docstring + the |
| B12EntryDraft | scribe | DONE | y | 1314 | json-key:verdict | DRAFT-COMPLETE (unchanged by the last message) |
| B13SkillPatch | scribe | DONE | y | 5984 | json-key:verdict | DRAFT COMPLETE, NOT APPLIED (593 lines, 2 pins, checklist byte-identical) |
| B14SourcesUpdate | scribe | DONE | y | 7563 | json-line | DRAFT-ONLY |
| B15Simplifier | simplifier | DONE | y | 3812 | json-line | report-only, no lane byte edited. 9 of 10 findings taken by the draft seats while measuring; 1 withdrawn as m… |
| B16ProseRead | scribe | NOVERDICT | y | 4611 | file | drafts read and recomputed — four claims still false or contradictory as written (F-02, F-04, F-06/F-08, F-09… |
| B17LessonScribe | scribe | NOVERDICT | y | 5940 | file | lesson draft delivered at `.ufo/waves/round-76/build/lesson-draft.md` (221 lines, sha256 |
| B18ScorecardScribe | scribe | DONE | y | 3230 | json-key:verdict | DRAFTED-PENDING-MEASUREMENT |
| B19LogScribe | scribe | DONE | y | 2290 | json-key:verdict | log-draft complete; counters absent so 0 of 6 / 0 of 4 unrun, not observed; four definition/consistency items… |
| B20ConnOverlap | connector | DONE | y | 621 | json-key:verdict | STRICT_HITS=0 ADJACENT=6 DUPLICATE_SIBLING=none DUPLICATE_INTRA_LANE=S213(existing) BLOCKER=PLANS/ROUND-76.MD… |
| B21RevMethod | revenger | DONE | y | 4475 | json-key:verdict | M75-1's five numbers reproduce byte-exactly and its conclusion is false; description renders 1022 chars (YAML… |
| B22ChecklistImpact | executor | DONE | y | 6527 | json-key:verdict | PASS |
| B23GateRegistryCalc | executor | NOVERDICT | y | 5105 | json-keys | (keys: seat,lane_repo,report_path,files_changed,lane_mutations,behavior) |
| B24TipBatteryScript | executor | NOVERDICT | y | 10913 | file | B24TipBatteryScript complete — tip-battery.sh landed (chmod +x) and base-tested; base receipt tip-battery-bas… |
| B25Census | executor | DONE | y | 5421 | json-key:verdict | PASS — census clean at base: exit 0, `kotoba ok`, 151 rows, 20 W04 warnings, 0 E-code findings. One land-orde… |
| B26FetchRecheck | executor | DONE | y | 6693 | json-key:verdict | fetch recheck agrees 3 of 3 — no drift |
| B27ReceiptVerifier | executor | DONE | y | 7835 | json-key:verdict | 5 receipts FAIL the Q36/Q50 revision-naming check; 1 further receipt is ABBREV; 1 is rule-pass but WEAK; tota… |
| A01RevQuoteLocate | reviewer | BLOCKED | y | 364 | json-key:error | ERROR: Quote-level review could not be completed because no draft exists at `.ufo/waves/round-76/build/` and … |
| A02RevHashChain | reviewer | DONE | y | 386 | json-key:verdict | FINDING — required hash-chain references were unavailable during inspection; report written to .ufo/waves/rou… |
| A03RevCounterDesc | reviewer | BLOCKED | n | 757 | json-key:verdict | BLOCKED — assigned verifier absent at this checkout; mutant arms were not run. |
| A04RevCounterRepairs | reviewer | UNYIELDED | n | 1238 | none | - |
| A05RevControls | reviewer | DONE | y | 701 | json-key:verdict | C2 R2 shortcut accepted by frozen counter core check: 4/4, exit 0. Receipt named valid ancestor R75_TIP but c… |
| A06RevEvidence | reviewer | DONE | y | 3143 | json-key:verdict | All 5 assigned measurements re-derived and confirmed: description length 1022 (clip-preserving YAML folded re… |
| A07RevNoHarm | reviewer | UNYIELDED | n | 16700 | none | - |
| A08RevFreeze | reviewer | DONE | n | 1293 | json-key:verdict | FINDING — freeze integrity cannot be verified: required frozen counter files are absent from the measured lan… |
| A09MutDesc | mutation-tester | BLOCKED | y | 271 | json-key:verdict | INCONCLUSIVE |
| A10MutRepairs | mutation-tester | BLOCKED | n | 257 | json-key:error | ERROR: Blocked: assigned lane path exists but contains no PLANS/ROUND-76.MD or verifiers/check_r75_routed_rep… |
| A11MutRedBefore | mutation-tester | BLOCKED | y | 816 | json-key:verdict | INCONCLUSIVE — expected red baseline not established. |
| A12MutArms | mutation-tester | BLOCKED | n | 340 | json-key:error | ERROR: Blocked: checked the assigned absolute lane path and searched beneath `/home/vgpnk/Projects/shokunin` … |
| A13CritHollowC1 | critic | DONE | y | 434 | json-key:verdict | NOT SCORED: frozen C1 verifier absent; no 6/6 claim. Plan contract implies wrong-page r74 quotes fail conjunc… |
| A14CritHollowC2 | critic | DONE | y | 944 | json-key:verdict | counter not hollow — token-dump rejected on all four repairs by content checks and recomputation/re-execution… |
| A15CritHeadlineC1 | critic | DONE | y | 268 | json-key:verdict | Bound self-audit headline to the audit-table measurements that the counter recomputes; counter does not estab… |
| A16CritHeadlineC2 | critic | DONE | y | 283 | json-key:verdict | C2 'closed' headline overstates specified counter coverage; recommends source-derived checks or narrower head… |
| A17CritAudit | critic | DONE | y | 633 | json-key:verdict | AUDIT TABLE NOT PRESENT; source-level checks flag unsupported first-sentence constraints and literal trigger-… |
| A18ScoutSnapshot | scout | DONE | y | 400 | json-key:verdict | NOT RUN — counter unavailable |
| A19ScoutAudit | scout | DONE | y | 398 | json-key:finding | At HEAD 4de12b61f75c73e3675ef0e422cc2be0f7da8960, manually unfolding the YAML folded scalar and parsing it wi… |
| A20ScoutCensus | scout | DONE | y | 675 | json-key:finding | The S213 used-by append does not validate cleanly with the required corpus-only mirror. Census validation ret… |
| A21ScoutSibling | scout | DONE | y | 498 | json-key:verdict | STRICT_HITS: 0 |
| A22ScoutAssimilation | scout | DONE | y | 245 | json-key:verdict | {"adoptable":1,"refused_quote_absent":6,"unverifiable":6} |
| A23ScoutSources | scout | UNYIELDED | n | 571 | none | - |
| A24ScoutFresh | scout | DONE | y | 310 | json-key:verdict | NO DRIFT |
| A25Sentinel | sentinel | DONE | y | 6154 | json-key:verdict | PASS on CORPUS.md rule 6 (no credentials, no tokens, no private URLs, no op://, benign snapshot domains, fetc… |
| A26SentinelAppend | sentinel | DONE | y | 9649 | json-line | PASS — no lane file the round touches is a rewrite of filed bytes at eab64394dba08a47f6797a2e23719be14675b44b… |
| A27SimplifierAudit | simplifier | DONE | y | 3067 | json-key:verdict | report-only: economy attack delivered; 9 of 11 cuts taken by the entry writer across two versions (110->101 l… |
| A28SimplifierRead | simplifier | DONE | y | 6560 | json-key:verdict | ADVISORY HOLD on SHONEN box-3 as drafted |
| A29RevengerR1 | revenger | DONE | y | 4124 | json-key:verdict | R1 correction quotes both superseded strings byte-exactly and the folded render reads 1022 (clip)/1021 (strip… |
| A30RevengerR3 | revenger | DONE | y | 3668 | json-key:verdict | R3-NOTE-RECONCILES (excerpt byte-equal, 63/64 recomputes, phantom attributed) WITH ONE FALSE PARENTHETICAL (s… |
| A31RevD4 | reviewer | BLOCKED | n | 1609 | json-key:verdict | INCONCLUSIVE — D4 floor bump is not present in the current lane working tree, so the requested pass/mutant at… |
| A32RevLesson | reviewer | DONE | y | 2540 | json-key:verdict | PASS-WITH-FINDINGS |
| A33CritBudget | critic | DONE | y | 840 | json-key:counterexample | The skill-patch draft calls the preamble replacement 2→3 lines (+1), while arithmetic describes it as +2; add… |
| A34ScoutReceipts | scout | DONE | y | 387 | json-key:verdict | INCOMPLETE: current receipt set has no claimed tip counter/no-harm receipts, no scanner output, and no log dr… |
| B28EvidencePackager | executor | UNYIELDED | n | 4420 | none | - |
| A35ScoutPaths | scout | DONE | y | 365 | json-key:verdict | SPEC PATHS LANE-LOCAL |
| A36ScoutReceiptGreen | scout | BLOCKED | n | 1345 | json-key:verdict | BLOCKED/NOT RUN — requested R2 scratch-world falsification cannot be exercised against the frozen counter bec… |

Totals: report_present=52, report_absent=12; DONE 45, NOVERDICT 4, BLOCKED 8, UNYIELDED 7, EMPTY 0; dead (no file) 6; unyielded-with-file 1 (B11).

## 5. Parse recipe for round-77 `w1-results.json` (what the L1 should run)
```
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/S05DeadSeats.parse_results.py \
  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1-results.json > $OUT 2>&1; echo "exit=$?" >> $OUT
```
Rules (implemented, tested on r76 and on 9 synthetic cases: plain line, `**VERDICT:**` bold, ```json fence, prose+JSON, JSON whose nested string holds `VERDICT:`, verdict key BLOCKED, `aborted`, `<think>` narration, empty, JSON without verdict):
1. Report dir = `<dir of results.json>/<wave>/` (`--report-dir` overrides); report present = `<name>.md` exists. Never trust `note`/`agentId` (always null).
2. Verdict, first hit: (a) last plain line `^[ >*_`]*VERDICT[ <seat>]: text` in raw output; (b) parse JSON (whole text, fence stripped, or first `{…}` via `raw_decode` — so prose-wrapped/JSON-wrapped both work) then any nested string value containing such a line, then keys `verdict_line, verdict, final_status, status, summary, finding, counterexample`, then `error/aborted`; (c) last `VERDICT:` line of the report file; else `-`.
3. Status as in section 2; the L1 acts on the footer: `dead_seats`, `unyielded_with_report_file`, `noreport_names`, and `dispatched=… missing_from_results=[] extra_in_results=[]` (names dispatched but absent from results).
4. Exit status of the script is 0 whenever the JSON loads; it does not gate. Gate on the footer lines. Read its OWN exit (`> out 2>&1; echo exit=$?`), never a pipe's.
5. Limit: the script cannot tell a seat that LIED in its verdict; it only classifies presence. A verdict recognised by key is weaker than a plain `VERDICT:` line — in r77 reports the plain last-line is required, so `vsrc` should read `line`/`json-line`/`file`; any `json-key:*` is a prompt-compliance miss to log.

## 6. Recommendations for r77 operations
- Dispatch falsifier seats only after the artifacts they attack are frozen/landed (r76: 6 of 12 report-less seats were blocked on absent inputs).
- Treat UNYIELDED as dead even when a report exists; recover from the file and note it.
- Record result counts as "N dispatched / N report files / N DONE / N BLOCKED / N dead" with the commands above; the "64 vs 52" gap is fully explained: 12 = 6 dead + 5 BLOCKED + 1 finding-of-absence.

Tooling: none installed.
