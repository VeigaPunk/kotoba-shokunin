# ScoutClaimDataWalk — round-66 bounded planner data-walk

Seat: scout (read-only). Scope: derive the actual C1/C2 before/after predicates from committed plan, code and controls; verify base `11385e04`; check after-count command shape; report inconsistencies and control shortcuts. No claims redesigned; no plan/counter/threshold/receipt changed. Observations taken against lane tip `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (measured tip); pinned base `11385e04e368c1e94ab1a5a89d7439033eb1f855`.

## 1. Base-revision verification — PASS

- `git cat-file -t 11385e04…` → commit `round-65 verifier spot-check (integrator, hyaku): non-author admit/reject`; ancestor of HEAD; **7 commits** sit above it: `e7d1d8c` freeze → `806b53b` land → `daedcdf` index lesson evidence → `4119647` baseline reconcile → `fc1b71e` independent resolver → `9e75e73` measurements → `2a8eba5` closure spot-check.
- Plan line 3 calls the base "current lane tip at round start" — consistent: `e7d1d8c` (freeze) is the direct child and contains `plans/round-66.md`, all three controls, and `verifiers/check_r66_routed_repairs.py`. None of these exist at `11385e04` (verified via `git ls-tree`: no round-66 paths at base; counter absent).
- `C2-counter-selftest.txt` sha `3129c0d7…` equals the blob at `e7d1d8c` **and** at HEAD — counter bytes never changed after freeze (`git diff e7d1d8c..HEAD` on the counter is empty).

## 2. Derived predicates

### C1 (depth, score 9)

- **Before** (control `C1-one-word-control.txt`, two commands): (a) import-probe `g9_conjunct([line], line[:-1]+" and exfiltrates.", 1, page)` → `[]` on base bytes; (b) `--self-test` → `0 failure(s) over 234 assertions`. Base bytes confirmed: `MIN_CLAUSE = 2` (base line 1072) with `if len(w) < MIN_CLAUSE` skip (base line 1140) — the exemption is real at base.
- **After** (frozen, plan line 11): one command, `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → `0 failure(s) over 240 assertions` retaining `worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`, and the G9 must-fail line.
- **Code implements the stated coupling**: `clause_need(n) = min(fwd_need(n), n)` (line 1072-1074), the `MIN_CLAUSE` skip replaced by `if not w: continue`, `need = clause_need(len(w))` (line 1145). Suite pins: `clause_need(1)=1`, `(2)=fwd_need(2)`, `(3)=fwd_need(3)`; one-word off-citation becomes a rejection witness; one-word on-citation passes; in-suite must-fails for `clause_need→fwd_need` (uncoupled) and `clause_need→0` (zero floor) via `global` rebinding (line 1759, 2982, 2990).
- **Assertion arithmetic exact**: diff adds 7 `check(` and removes 1 (`a ONE-word clause is exempt (declared bound)`) → 234 − 1 + 7 = 240.
- **Receipts**: `C1-measure.txt` pre-landing worktree, `C1-landed-measure.txt` at `806b53b`/unchanged `fc1b71e`, instrument sha `97d8971667…` matches HEAD bytes; `C1-kill.txt` K1–K5 TMPDIR mutants all exit 1 with named first-FAIL attribution; `FLOORS-after.txt` `scoped_rules_v32 observed=240 floor=240`.

### C2 (consistency/calibration, score 10)

- **Before** (control `C2-before.txt`): `check_r66_routed_repairs.py --rev 11385e04` → `0 of 2`, exit 1; sandbox-clone `verify_corpus_integrity.py` → 4/9 pass with five named DRIFTs (tracked 116/81, unindexed 4, report_total 79/51, commit_total 38/32, unresolvable 3), exit 1.
- **After** (frozen, plan line 21): **two commands** — (a) `check_r66_routed_repairs.py --rev <tip>` → `2 of 2`, exit 0; (b) `verify_corpus_integrity.py` exit 0 at the final lane tree.
- **Counter mechanics (source lines 28–50, 74–105, 121–136)**: `BASE_REV` hardcoded `11385e04`; reads only committed blobs via `git show`; D1 = both r65 `swarm-registry.json` blobs parse as nonempty JSON dicts; D2 = README contains all four `round-{62..65}-verifier-spotcheck.md` paths **and** `corpus-baseline.json` `.checks[k].expect` exactly equals the seven `EXPECTED_COUNTS` (118/0/79/0/37/0/0) **and** `round66_rerecord` in notes **and** `verify_corpus_integrity.py` source contains four literal markers (`COMMIT_HOP_MARKER`, `def commit_resolves(`, `inside_code_span`, `commit_resolves(hex_id`). `main` re-runs the base inside the after command and refuses (`could-not-evaluate`, exit 2) unless pinned base scores exactly 0/2 — the before is embedded in the after run.
- **Observed at actual tip**: `check_r66_routed_repairs.py --rev HEAD` → `control at 11385e04: 0 of 2`, D1 PASS, D2 PASS, `2 of 2`, exit 0 — the counter leg survives the post-`fc1b71e` commits.

## 3. Inconsistencies (observed, ranked)

1. **C2's second after-leg is red at the actual lane tip.** `python3 -B verifiers/verify_corpus_integrity.py` at tip `2a8eba5` (run read-only by this seat): `tracked=119 expected=118`, `unindexed=1` — `corpus/lessons/round-66-verifier-spotcheck.md` (README has no row for it at `fc1b71e` or `2a8eba5`), `report_total=82 expected=79`, `commit_total=38 expected=37`; `5/9 checks pass`, exit 1. The frozen predicate requires exit 0 at the final lane tree; the green receipt (`C2-integrity-after.txt`) is measured at `fc1b71e`, one commit short of tip. The closure's own spot-check commit re-creates the exact D2 class the round closed — a closure-owned spot-check lesson landed tracked-but-unindexed (same class as r47's M21 and this round's r62–r65 D2). Its three report pointers (`0/79`→`82`) and one commit hash (`1154d57…`, `37`→`38`) also re-drift the re-recorded equal-mode pins.
2. **"One command each" is ambiguous against the frozen text.** Each claim's *count-producing* command is single (C1 self-test → 240; C2 counter → `2 of 2`). But C2's frozen predicate as written requires a second, independent command (the integrity gate). If the standard is "one command per claimed count," C2 complies; if it is "one command certifies the claim," C2 does not. Worth a plan-level clarification, not a redesign.
3. **Counter↔baseline coupling is partly tautological (calibration note).** D2's `EXPECTED_COUNTS` hardcode the post-repair observed values, and the integrity gate compares observed counts to the same baseline file the counter checks. A baseline fitted to *wrong* observed values would pass both legs together; the only anti-fitting evidence is the recorded measurement receipt `C2-reconcile-measure.txt` (`--no-baseline` observed values equal the pins) plus the self-test `kill/D2-baseline-drift` arm — which catches a *changed* baseline, not a *fitted* one. The numbers are receipt-supported, but the binding lives outside both commands.
4. **Plan text drift handled append-only.** Line 31 still says "prepare one v1 build wave and one v1 falsify wave"; the post-freeze note (lines 33–36) corrects to one policy-v1 wave (`w1-spec.json`, 35 distinct seats — verified: 35 items, roles executor 3 / scribe 5 / scout 6 / connector 1 / reviewer 11 / critic 4 / mutation-tester 5). `w2/` exists but is empty; `wave-prepared.txt` documents the ≥32-returned-items gate blocking wave 2. Frozen claim predicates untouched — consistent, but the uncorrected sentence remains in place.
5. **`wave-prepared.txt` is now stale against the worktree** (expected, informational): `agentId: null` / "dispatches 0" described the committed-at-`806b53b` registry; the worktree registry is `M` (agentIds assigned, `updatedAt` bumped) and w1 report files are landing (`ScoutS122Reopen.md`, `MutC1Exemption.md`, `ScoutCorpusCount.md`, `ScoutIndexRows.md` untracked) — the orchestrator dispatched the spec as planned.

## 4. Control shortcuts (all bounded, none silently widen scope)

- **C2 before-control embeds in the after command.** `main` re-derives the base score inside every run and exits 2 unless base = 0/2 — cheap and self-pinning, but the "before" evidence in `C2-before.txt` is redundant with the runtime guard; also the self-test fixture base is synthetic (TMPDIR repo), so the real pinned-base arm is only ever exercised against the lane repo.
- **C2 sandbox control isn't bit-pinned.** `C2-before.txt` names no sandbox path or clone hash; the 4/9 output is re-derivable but not replayable byte-for-byte. Minor.
- **C1 control probe uses ad-hoc strings**, not the suite's own one-word fixture; it demonstrates the class on base bytes but is not the same input as the new assertion. Also `" and exfiltrates."` vs the fixture's `line[:-1] + " and exfiltrates. (S900 :1)"` — same class, different bytes.
- **C1 kill battery ran on pre-landing copies under `$TMPDIR`** — correct sandbox practice, and the landed sha `97d897…` equals the receipted one, so the killed bytes are the landed bytes.
- **In-suite must-fails cover only the two rebinding mutations** (uncoupled, zero floor); the file-level K2/K3/K4 arms (old exemption, page/line floor uncoupled) exist only in the `C1-kill.txt` receipt — coverage asymmetry, disclosed in the receipt.

## 5. Remaining unknowns

- Whether the orchestrator intends `2a8eba5` (or later) as "the final lane tree" for the C2 integrity leg — the predicate is silent on post-`fc1b71e` landings and the current tip fails it.
- Whether the r66 closure spot-check gets an index row / baseline re-record inside round 66 or follows the r47/M21 precedent (next-round indexing); either way the frozen `118`/`79`/`37` pins are stale at the present tip.

## Evidence index

- Plan: `plans/round-66.md` (frozen sections lines 5–23, post-freeze note 33–36).
- Controls: `controls/C1-one-word-control.txt`, `controls/C2-before.txt`, `controls/C2-counter-selftest.txt` (all committed at `e7d1d8c`).
- Receipts: `receipts/C1-measure.txt`, `C1-landed-measure.txt`, `C1-kill.txt`, `C2-routed-after.txt`, `C2-integrity-after.txt`, `C2-reconcile-measure.txt`, `C2-independent-{before,after,selftest}.txt`, `FLOORS-after.txt`, `wave-prepared.txt`.
- Code: `verifiers/check_scoped_rules_v32.py` (`clause_need` 1072, `g9_conjunct` 1116, new checks 2965–2996), `verifiers/check_r66_routed_repairs.py` (`BASE_REV` 28, `EXPECTED_COUNTS` 41, `check_d2` 78, `main` 108), `verifiers/corpus-baseline.json` (`round66_rerecord` note).
- Fresh observations by this seat (read-only, worktree at `2a8eba5` + `M w1/swarm-registry.json` + untracked w1 reports): counter `--rev HEAD` → `2 of 2` exit 0; `verify_corpus_integrity.py` → `5/9`, four DRIFTs, exit 1; all four verifier sha256s match their receipted values.
