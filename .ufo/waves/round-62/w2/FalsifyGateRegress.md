# FalsifyGateRegress — r61 no-harm-critical gates at r62 tip (wave-2, self-run)

**Seat:** `L1kotoba62.FalsifyGateRegress` (leaf; no subagent dispatch, no tool installs — RULES.md read, pacman paused, nothing installed).
**Assigned tip:** `e6da78bbe420722dd18a13182a7c4b64ce02f005`. **Observed lane HEAD during the runs:** `3f91150` (`git rev-parse HEAD`, run in lane) — the integrator landed the wave-2 dispatch commit while this seat ran; working tree additionally carried uncommitted modifications (`LOG.md`, `SCORECARD.md`, `corpus/*`, `verifiers/check_routed_repairs_v2.py`, `M` in `git status --porcelain`) and untracked wave-2 reports. To attribute committed bytes I cloned to `/tmp/r62base/kotoba-shokunin` (read-only `git clone`/`git checkout` — sandbox clone under /tmp per bounds; fleet root `/tmp/r62base` populated with symlinks to `/home/vgpnk/Projects/shokunin/*` so `../`-relative citation tokens resolve exactly as in the lane).

## Six gate commands — run verbatim, one at a time

| # | Command (cwd = lane root) | Exit | Summary line |
|---|---|---|---|
| 1 | `python3 -B verifiers/verify_corpus_integrity.py` | **1** | `5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable` |
| 2 | `python3 -B verifiers/verify_skill_checklist.py` | **1** | `FAIL governance.citation_resolves: evaluated 1155 — LOG.md:2533 …; SCORECARD.md:158 …; SCORECARD.md:369 … does not resolve` |
| 3 | `python3 -B verifiers/check_assertion_floors.py` | **0** | 14 lines, all `PASS`; last `PASS correction_sweep observed=25 floor=25` (109.8 s) |
| 4 | `python3 -B verifiers/check_gate_registry.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005` | **0** | `gate registry rows conformant 39 of 39 lane verifiers; phantom 0` |
| 5 | `python3 -B verifiers/check_seat_counts.py --self-test` | **0** | `self-test: 0 failure(s)` (5 arms) |
| 6 | `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | **0** | `boxes proven 2` |

Gate 3's printed output (verbatim tail): `PASS harness_independent observed=123 floor=123`, `PASS compare_harness_independent observed=330 floor=330`, `PASS floors_guard observed=165 floor=150`, `PASS dispatch_prompts observed=56 floor=56`, `PASS sibling_census observed=68 floor=68`, `PASS overlap_levers observed=55 floor=51`, `PASS alwayson observed=89 floor=89`, `PASS correction_sweep observed=25 floor=25`, `EXIT=0`.

## Base comparison (base set named by `.ufo/waves/round-61/noharm-tip.txt`)

r61's committed no-harm receipt (`noharm-battery.sh` arms) names the comparison semantics: `corpus` = no **new DRIFT kind** vs base set {tracked_files, unindexed, commit_total, commit_unresolvable, report_total}; `corpus-idx` = no new unindexed corpus file (base set: `corpus/lessons/round-60-verifier-spotcheck.md`); `checklist` = no new failing **check id** (base set: `governance.citation_resolves`); `check-ptr` = unresolved citation pointers did not grow (base=2).

### 1. `verify_corpus_integrity` — FAIL both columns, no r62 regression (PASS under battery semantics)

- Sandbox base `a745411c` (verbatim tail): `DRIFT corpus.index.tracked_files: observed=103 expected=81`, `DRIFT corpus.index.unindexed: observed=1` (the r60 spotcheck lesson), `DRIFT corpus.pointers.report_total: observed=67 expected=51`, `commit_total: 34 expected=32`, `commit_unresolvable: 1` → `4/9 checks pass; EXIT=1`.
- Clean committed tip `e6da78b` in the sandbox: `5/9 checks pass`; DRIFT set ⊆ r61 base set, and `unindexed` dropped 1→0 (r62's README index absorbed both spotcheck lessons) — `corpus` arm **PASS**, `corpus-idx` arm **PASS** (this exact arm FAILED at wave-1 receipt `3e7aed9b` and was fixed by `e6da78b`).
- Root cause of standing DRIFT: `verifiers/corpus-baseline.json` is byte-identical at base and tip (`git diff --stat a745411c..e6da78b -- verifiers/*.json` → empty), `as_of 2026-09-29`, `measured_against head d85982d` — a round-17 baseline never re-recorded. `equal`-mode checks drift whenever the corpus legitimately grows; this is a chronic gate-design defect predating r62, not an r62 regression.

### 2. `verify_skill_checklist` — FAIL both columns; check-id set unchanged but **dead-pointer count grew** (check-ptr arm regression)

- Sandbox base `a745411c`, faithful root: `FAIL governance.citation_resolves: evaluated 1113 — LOG.md:2533: '.ufo/reports/round-60/kotoba.md' …; SCORECARD.md:156: '.ufo/reports/round-60/kotoba.md' …` → **2 dead tokens**, `EXIT=1`. `checklist` arm at tip: **PASS** (same check id).
- Clean committed `e6da78b`: **4 dead tokens** — the same round-60 pair **plus** `SCORECARD.md:369: '.ufo/reports/round-62/kotoba.md'` and `LOG.md:2558: '.ufo/waves/round-62/census-after.txt'` (then untracked). `check-ptr` arm at e6da78b would score **4 vs base 2 → FAIL**.
- At observed HEAD `3f91150` (committed `census-after.txt` now on disk): **3 dead tokens**, `EXIT=1`. `check-ptr` still fails: **3 vs base 2**.
- **FINDING (r62-caused):** `git log -S 'round-62/kotoba.md' -- SCORECARD.md` → introduced by `e6da78b`; `git log -S 'census-after' -- LOG.md` → `e6da78b`. The `SCORECARD.md:369` pointer repeats the known dead pattern: the report lives at the **fleet root** (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-62/kotoba.md` exists on disk; so does `round-60/kotoba.md`), and tokens resolve lane-rooted, so `.ufo/reports/…` is dead permanently — it would need `../.ufo/reports/…` or the GOVERNANCE_ERRATA recorded-absence mechanism (LOG.md-only, horizon+baseline-pinned; does not cover SCORECARD or this forward reference).

### 3–6. Green

- `check_assertion_floors.py`: exit 0, all 14 floors observed ≥ floor. (Slow: 109.8 s — near the 120 s cap.)
- `check_gate_registry.py --rev e6da78b`: 39/39 OK. The wave-1 `noharm-tip.txt` recorded `FAIL reg_gate … tip=1` (absorption + routed_repairs_v2 lacked registry rows at `3e7aed9b`); e6da78b's registry rows fixed it — now includes the three new gates (`check_erratum_absorption.py`, `check_routed_repairs_v2.py`, `check_scoped_rules_v31.py`) plus `check_seat_counts.py`.
- `check_seat_counts.py --self-test`: exit 0. **Note:** `git cat-file -e a745411c:verifiers/check_seat_counts.py` → absent (also absent at `f3246d14`); the gate is **new in r62** (`9f03dcd`), not an r61 gate — the assignment's "r61 gates" framing is off; there is no base column to compare, and its own exit-0 self-test stands.
- `verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json`: `boxes proven 2`, exit 0 (= r61 `boxproof` arm: exit 0 both columns).

## Findings by severity

1. **check-ptr arm regression (r62-caused, `noharm-battery.sh` semantics).** Dead citation pointers grew base=2 → 4 at committed `e6da78b` → 3 at `3f91150`. Two r62 lines cite paths that never resolve lane-rooted: `SCORECARD.md:369` (`.ufo/reports/round-62/kotoba.md` — permanent dead token, mirrors the standing r60 defect), `LOG.md:2558` (`census-after.txt` — dead only at `e6da78b`, healed when `3f91150` tracked the file). Severity: low severity for the corpus arm (same check id), but it **breaks the "pointers did not grow" arm** the r61 battery names, and SCORECARD's new row carries a permanently unresolvable citation.
2. **Standing battery-level defects re-confirmed, not r62-caused:** corpus-integrity `equal`-mode baseline frozen at round-17 (`d85982d`) — every growing round guarantees DRIFT exit 1; the two r60 dead report pointers remain unexcused. Severity: chronic gate design; r62 shrank it on one axis (`unindexed` 1→0).
3. **Assignment-frame erratum:** `check_seat_counts.py` is an r62-added gate (`9f03dcd`), absent at both `a745411c` and `f3246d14`; treating it as an "r61 no-harm-critical gate" has no base column. Its self-test passes.

## Residual risk / verification gaps

- `noharm-battery.sh` itself was **not** re-run end-to-end by this seat (assignment scoped the six gates); the wave-1 receipt at `3e7aed9b` died `exit=124` after 8 arms — a fresh full battery at the final tip remains open; my arm-level results above are direct re-derivations, and `check-ptr` is the arm that now fails where the wave-1 receipt scored it PASS.
- Working tree was dirty during the lane runs (integrator in-flight edits, untracked w2 reports). Committed-bytes verdicts above come from the sandbox clone at `e6da78b`; gate 2's committed tip run in the sandbox is authoritative (4 dead tokens at e6da78b), the lane WT run (3 dead tokens) matches the `3f91150` commit + `census-after.txt` on disk.
- `verify_corpus_integrity` gate-1 lane run's `report_dead=0/69` confirms no dead report pointers were added by r62; DRIFT deltas are volume, not new kinds.
- No LSP diagnostics used (shell/Python gates; not applicable to this audit's questions).

**Verdict:** 4 of 6 gates green; the two red gates are red at base (r61) too. One genuine r62 regression: the unresolved-citation-pointer count grew (check-ptr arm), with `SCORECARD.md:369` adding a permanently dead fleet-report citation — recommended fix `../.ufo/reports/round-62/kotoba.md` (or a recorded-absence row), same class as the unexcused r60 pair.
