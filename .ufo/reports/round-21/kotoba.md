# kotoba — round 21 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 21, loop 1 (loop-round 1), dispatched and admitted.
Dispatch HEAD: `4e92f36`. Work commit: `2ca8d01` (this report + evidence land in the follow-up publish commit, round-11 precedent).
Lane identity for the commits: `kotoba-shokunin <kotoba@shokunin.local>`.
Claims: **F** freshness (every live gate re-run at HEAD + substrate re-measure vs round-18 pins) · **A** adjacency (live per-sibling dead-token re-measure vs round-16 counts) — `.ufo/round-21/claims.json` (its stated kasegi baseline of 1 is retained as filed; the claim's own counting command falsified it — see A below).
Status: **completed craft round, admitted** — every claim verified, no axis harmed.

## Work performed

- **F — live gate sweep at HEAD `4e92f36`** (64-lane scout swarm, `opencode-go/deepseek-v4.1-flash` key 1 of 7; fragments `.ufo/round-21/scouts/{F,R,S,M}*.md`):
  - `python3 verifiers/verify_harness_claims.py` → **28/28, exit 0** (pre- and post-repair).
  - `python3 verifiers/verify_corpus_integrity.py` → **9/9, exit 0** post baseline re-record (51→52 tracked, 32→34 report pointers — both instruments green).
  - `python3 verifiers/verify_corpus_independent.py` → **exit 0** (agreement with the primary instrument holds live).
  - `python3 verifiers/verify_surfaces.py` → **RED exit 1 pre-repair** (8 `literal_present` FAILs: omp rebuilt 2026-10-16 `ff59fc1b`→`bf1e86a9` v18.11.1, registration callees renamed `Co`/`Dl`/`Hj`, the `CALL_RE` allowlist extracted 0, and `no_uncovered_class` passed vacuously on 0 extractions) → **7/7 PASS, exit 0 post-repair** (per-harness `OMP_CALL_RE` + extraction-vacuity guard).
  - `python3 verifiers/verify_skill_checklist.py` → live **exit 1** on the carried `trigger.line_budget 601>600` (inherited `02302c5`; deliberately not budget-raised); `--self-test` was **RED 2/1504 pre-repair** (fixture `delegated-directory/map.json:15` delegates to `probe-dir`, an empty dir git cannot track — the round-16/17 `0/1504` records were false in any clone) → **0/1504 post-repair** via `probe-dir/.gitkeep`.
  - `bash verifiers/fault_injection_corpus.sh --self-test` → **OK, exit 0** (full harness ALL PASS on a /tmp clone; two planted-fault demos fired both instruments).
  - Non-vacuity red probes M1–M8 (all on /tmp copies): **8/8 flipped their target gates as designed** (harness pin, catalogue anchor, corpus dead pointer, box-map tamper, OC-1 anchor, fault class (e), planted governance dead path, independent-instrument hash).
- **F — substrate re-measure vs round-18 pins:** omp `ff59fc1b` → **`bf1e86a9` (MOVED 2026-10-16, omp 18.11.1, unminified chunks; sha256 measured live, `stat` mtime 2026-10-16 05:15:11 -0300)** — repaired (allowlist + guard) and re-pinned in `verifiers/baseline.json` (the pin remains unenforced by any check: named debt); opencode `d9123b9b` / v2.0.26 **HOLDS** (byte-identical; all six OC rules re-verified live by scouts S2/M5).
- **A — live sibling dead-token predicate** (round-16 R3 shape, instrument byte-identical `02ccf1b3…`; siblings read-only): **kagi 2, kake 1, kasegi 5, kengaku 1, kumitate 5 = 14, delta 0 vs the round-16 ledger** (scouts A1–A5; frozen replay reproduces 226/14/14/0 exactly; packaged live recheck exits 1 `source_drift` — kake/kengaku bytes drifted without count drift).
- **L2 lanes:** one batched AgentSwarm, **64/64 completed**, zero lost; per-lane fragments under `.ufo/round-21/scouts/`. Claim-critic verdict (scout C1): F unsound-as-written pre-repair (its falsifier had fired), A sound-with-conditions — both discharged by the in-round repairs/records.
- **Deliberately not run / not touched:** no push (repo diverged from remote — H1; git correctness is loop-round-14's audit); `SKILL.md` content untouched (line budget debt is not to be laundered by this round); sibling repos read-only, no repairs absorbed; `SHONEN.md` untouched; round-20 evidence preserved.

## Landed changes

- `verifiers/verify_surfaces.py` — per-harness callee allowlist (`OMP_CALL_RE`: historical + `Co|Dl|Hj`; opencode keeps the conservative list) + `check_no_uncovered_class` extraction-vacuity guard; five new self-test assertions (70→75: `strings-omp-newcallees.txt` positive case, `extract-vacuity` negative case). [LOG § Round 21]
- `verifiers/fixtures/surfaces/strings-omp-newcallees.txt` — new fixture (2026-10-16 omp callee names).
- `verifiers/fixtures/checklist/delegated-directory/probe-dir/.gitkeep` — makes the `delegated-directory` self-test case pass from a fresh clone.
- `.gitignore` — restored `__pycache__/` + `*.pyc` (deleted by `c8b53ac` while it committed two pycs; `4e92f36`'s "already covered" claim was false — scout H3).
- `verifiers/baseline.json` — omp sha/mtime re-pinned to `bf1e86a9` + round-21 note.
- `corpus/knowledge/sibling-citation-routing-round21.md` + `corpus/README.md` index row — claim-A route evidence (14/14 correction, drift, prior art).
- `verifiers/corpus-baseline.json` — re-recorded 51→52 tracked / 32→34 report pointers + round-21 note.
- `SCORECARD.md` — freshness/adjacency rows annotated (round-21 blocks; round-16 kasegi transcription corrected in-row), malformed axes rows repaired (operability/freshness/adjacency Owned?/Last-change cells), move-log rows for 21, §Saturation declared (line 10.0 owned, N=3 prospective from 22), §planned refreshed.
- `LOG.md` — § Round 21 (2026-10-19) appended.
- Intentionally unchanged: `SKILL.md`, `PROVINCE.md`, `SHONEN.md`, `AGENTS.md`, protocol files, sibling repos.

## Before → after measurements

| Claim | Measurement | Before | After (round 21) | Command/evidence |
|---|---|---|---|---|
| F | six live gates at HEAD | no sweep existed at HEAD; 2 gates red unrecorded | harness 28/28 · corpus 9/9 + independent exit 0 · surfaces **7/7 exit 0** · fault ALL PASS · checklist exit 1 (carried 601>600 only) · self-tests 0/75 + 0/1504 | sweep above; scouts F1–F7 |
| F | omp vs pin `ff59fc1b` | `ff59fc1b` (round-18 pin, stale since 2026-10-16) | `bf1e86a9` measured, gate repaired, pin re-pinned | `sha256sum /home/vgpnk/.local/bin/omp`; scouts F1/S1 |
| F | opencode vs pin `d9123b9b` / v2.0.26 | `d9123b9b` | **HOLDS** byte-identical | scouts S2/M5 |
| F | gate non-vacuity | asserted at rounds 14–17 only | 8 fresh red probes, 8/8 flipped | scouts M1–M8 |
| A | kagi / kake / kasegi / kengaku / kumitate dead tokens | ledger 2/1/5/1/5; **recorded headline wrong (kasegi 1, total 10)** | live **2/1/5/1/5 = 14, delta 0**; headline corrected | scouts A1–A5; `sibling-citation-routing-round21.md` |
| A | route evidence | round-16 packet, frozen since | refreshed live re-measure + kasegi delegated-root delta + new prior art | same file |

Axis verdicts: **freshness — improved** (score held 8.0, repair-hold: the sweep existed, both reds repaired or deliberately carried with evidence; non-vacuity strengthened); **adjacency — improved** (score held 8.0: live re-measure, transcription corrected, evidence refreshed); coverage / operability / calibration / depth / consistency — **unchanged** (their rows' supporting gates all green; no claim made or harmed). No trade: the only edits touching other axes' instruments were repairs that returned them to green.
Drift handling: every drift found is either repaired in-round (above) or filed as named debt in LOG § Round 21 (remote divergence, inert pins, census errata, crash-class robustness, `--json --no-baseline` exit-code defect).

## SHONEN

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources — unchanged; no non-author verifier this round (a lane-dispatched swarm is the lane, PROTOCOL promotion gates); SHONEN.md box 1 evidence stands as recorded.
- [~] At least one end-to-end domain task executed and logged in LOG.md — unchanged; round 21's sweep + repairs are logged in LOG § Round 21 but are lane-authored work, not fresh non-author verification.
- [~] Instructions executable by an agent without oral context — unchanged; scouts S5/S6 re-ran two recorded recipes (one matched its round-20 snapshot, one is stale and now named debt).
- [~] No cross-domain bleed (PROVINCE.md still accurate) — unchanged; sibling repos were read-only throughout; kasegi's `anchorcheck.py` exit-0 defect is routed, not fixed.
