Result: DONE — one of five assigned debt items is closed (corpus_integrity baseline re-record, by round-66 commits); the other four remain OPEN at tip `2a8eba56`, and the integrity gate is red again at tip on a fresh, smaller instance of the same class.

# ScoutQualityDebt3 — carry-forward quality debt sweep (round-65 wave 1)

Measured revision: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (`git rev-parse HEAD`, exit 0) — "round-66 verifier spot-check". Run at 2026-10-24T07:39Z. Axis: freshness. Read-only sweep; only this report was written. No subagents, no git/jj writes, no installs.

**Ledger note:** the assignment names the debt in "SCORECARD 'Next: round 66'"; that block is frozen at commit `0e104f4` `SCORECARD.md:371`. At tip the same block is re-headed "**Next: round 67**" (still `:371`) — the lane advanced through round 66 (`e7d1d8c…2a8eba5`) after the wave was prepared. The debt items carry verbatim into Next-67, which asserts their status; each was re-verified against current bytes anyway.

## Status table

| Debt item | Status at `2a8eba5` | Evidence |
|---|---|---|
| SentBounds pre-wave baseline receipt | **OPEN** (process deferral; both rounds since had no seat dispatch to bound) | No `baseline.json`/`bounds_audit` capture exists for any round. `find .ufo/waves -name '*bounds*' -o -name '*baseline*' -o -name '*invo*'` finds only `.ufo/waves/round-57..60/bounds.md` — those are seat-policy text, not the frozen pre-dispatch snapshot `SentBounds.md:60-70,172-181` requires (`base`, `fleet_status`, `lane_status`, `runtime`, `siblings`, `jj_op_head`). Repo-wide grep for the payload keys `fleet_status|jj_op_head|op_before|op_after|helper_argv|before_op_id|after_op_id` (excluding the proposal/specs/registries/prior debt reports) returns **0 captures**. `bounds_audit` is referenced only inside `SentBounds.md` itself. Rounds 65/66 were prepared-but-undispatched (L1-executed), so no new wave owed a capture — the requirement text is unchanged and no receipt discharges it. Fleet `.ufo/state/kotoba.report-baseline` is a watchdog counter (`66` + e3b0 sha of empty), not this artifact. |
| Helper-invocation receipts | **OPEN** (same deferral) | `SentBounds.md:72-80` requires trusted before/after op IDs + helper path/hash/argv. Live helper `scripts/hyaku/jj-lane.sh` sha256 `319a56f7f0641915bdb636d88b2d6b34987a20f430d7b06896150f8ae4c1e429` — byte-identical to the hash `ScoutW2QualityDebt2` recorded at c019919c, so no ledger was added since. `grep -in 'receipt|ledger|argv|op log|invocation' scripts/hyaku/jj-lane.sh` → no matches. `ls scripts/hyaku/` shows no ledger file. No committed op-ID receipt found anywhere under `.ufo/`, `corpus/`, `LOG.md`, `SCORECARD.md`. |
| r62 w2 remainder (a) M93 hollow-diagnostic wording | **OPEN** | `corpus/lessons/round-62.md:25` still states the hollow variant's "diagnostic is a missing `check_scoped_rules.py` path". The recorded bytes `.ufo/waves/round-62/controls/absorption-hollow.txt:7-9` print `absorption self-test failed: guard-mutation direction is missing for one or more errata`, `exit=1` — the intended guard-direction rejection, not a missing-path error. File last touched by r62 commits (`git log --follow`: `849a546`, `e681737`, `e424f2a`, `3f91150`); the wrong sentence survived every later correction. |
| r62 w2 remainder (b) `LOG.md:2549` clock | **OPEN** | `LOG.md:2549` still dates `absorption-before.txt` `2026-10-23T20:53:36Z`; the control itself records `date_utc=2026-10-23T20:57:43Z` (`:2`). Off by ~4 min; LOG.md's last substantive correction is `849a546` (round-63), before the r64 debt note — no fix landed since. |
| r62 w2 remainder (c) SCORECARD r62 no-harm sentence vs two interim reds | **OPEN** | `SCORECARD.md:36` (r62 annotation) still ends "No axis harmed: the frozen counter is byte-identical (`5a5adc94…`) and the successor self-test imports the frozen six unchanged." The battery receipt `.ufo/waves/round-62/noharm-tip.txt` records `FAIL reg_gate` (missing registry rows), `FAIL corpus-idx` (unindexed `round-61-verifier-spotcheck.md`), `Battery exit code: 124`. `LOG.md:2573` still qualifies only the report's summary, not this sentence. |
| r62 w2 remainder (d) r61 R-b corpus-idx omission | **OPEN** (list omission only; the index gap itself stays closed) | `LOG.md:2557` "R-b landed scope (round 62, complete list to date)" still omits `corpus/lessons/round-61-verifier-spotcheck.md`; the r61 list at `LOG.md:2541` omits it too. The file exists and is indexed at `corpus/README.md:108` (closure-fixed in r62) — so the only standing defect is the two "complete list" sentences being incomplete. |
| corpus_integrity baseline re-record debt | **CLOSED at round 66 — but the gate is RED AGAIN at tip on a new instance** | Debt form (per assignment; the r65 receipt notation): `verify_corpus_integrity.py` red identically at `c98d137` and `80bb8921` — equal-mode pins `tracked_files 113`, `report_total 76`, `commit_total 37` vs observed `81`/`3 unindexed`/`51`/`32`, `commit_unresolvable 2`. Closure evidence: commits `4119647` (reconcile baseline), `daedcdf` (index r62–r65 spot-check lessons), `fc1b71e` (independent resolver). `verifiers/corpus-baseline.json` `round66_rerecord` note: `tracked_files 116→118`, `unindexed 4→0`, `report_total` re-recorded `51→79` (expect now 79), `commit_total 38→37`, `commit_unresolvable 3→0`. Receipts `receipts/C2-reconcile-measure.txt`, `C2-integrity-after.txt` (9/9, exit 0 @ `fc1b71e`), `C2-routed-after.txt` (`D2-corpus-integrity-reconciled: PASS`, `2 of 2`), `C2-independent-after.txt` (`commit_unresolvable=0`, exit 0). **Fresh run at tip (below): exit 1, 4 DRIFTs** — `tracked_files observed=119 expected=118`, `unindexed=1` (`corpus/lessons/round-66-verifier-spotcheck.md`, landed by `2a8eba5` without an index row — the recurring closure-file-index class), `report_total 82 vs 79`, `commit_total 38 vs 37`. The original named debt is discharged; a fresh same-class re-record/index obligation now stands for round 67 (the r66 spot-check's own N-routes do not name it — N1/N2/N3 only; [INFERENCE] it is new since `fc1b71e`). |

## Adjacent debt in the same frozen sentence (not in my assigned list, noted once)

- The append-only `sources` S120-cell breach / contract-compliant supersede-row correction: still named in Next-67 ("the contract-compliant S120 supersede-row correction") → OPEN by the ledger's own assertion. SHONEN D3 remains operator-owned (r66 spot-check N3 agrees).
- r65 routed D1/D2: closed by round 66 per `C2-routed-after.txt` `2 of 2` and the r66 spot-check `✓` re-derivation — confirms the assignment's integrity item mapping.

## Command evidence (all at tip, lane cwd)

```text
$ git rev-parse HEAD
2a8eba56b3f9321b70c569fa2816d42237ca49a2          exit=0
$ sha256sum scripts/hyaku/jj-lane.sh
319a56f7f0641915bdb636d88b2d6b34987a20f430d7b06896150f8ae4c1e429   exit=0
$ timeout 120 python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=119 unindexed=1 stale=0 missing=0  (136 FILE-column patterns over 118 md files)
corpus.pointers report_dead=0/82 commit_total=38 unresolvable=0 nonhash=0 (...)
           unindexed: corpus/lessons/round-66-verifier-spotcheck.md
DRIFT   corpus.index.tracked_files: observed=119 expected=118
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=82 expected=79
DRIFT   corpus.pointers.commit_total: observed=38 expected=37
5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total
exit=1
$ grep -n 'complete list' LOG.md  → 2541 (r61 list, no spotcheck file), 2557 (r62 list, no spotcheck file)
$ grep -n 'round-61-verifier-spotcheck' corpus/README.md → :108 (indexed)
$ git log -1 --format='%h %s' -- corpus/lessons/round-66-verifier-spotcheck.md
2a8eba5 round-66 verifier spot-check (integrator, hyaku): non-author admit/reject   exit=0
```

## Claims this supports / falsifies

- **Supports (as recorded debt, still true):** SentBounds baseline receipt, helper-invocation receipts, and all four r62-w2 remainder items are genuinely open at tip — the Next-67 carry-forward is accurate on those.
- **Falsifies (a stale debt assumption):** the corpus_integrity "red identically at c98d137 and 80bb8921" statement no longer describes tip — the original defect was closed at `fc1b71e`; what stands now is a *new* same-class red (unindexed r66 spot-check + 3 equal-mode drifts), which no named debt sentence yet records.
- **No-aims note for the wave:** the four open documentation items each have a known one-sentence correction (recommended texts already drafted in `.ufo/waves/round-64/w1/ScoutQualityDebt.md:225-229`); the two process debts need a mechanism (pre-wave capture + helper ledger), not a wording fix; the fresh integrity red needs an index row + baseline re-record, mirroring the round-66 procedure.

## Remaining unknowns

- Whether the prepared r66 W1 `ExecIntegrityNoBaseline.md` (uncommitted sibling report now in the worktree) already scopes the fresh `unindexed=1` — [INFERENCE] it likely does; I did not adjudicate it.
- Whether the orchestrator intends the SentBounds/helper receipts to apply to L1-executed (undispatched) rounds — the contract was written for dispatched waves; no wave since its adoption has dispatched.
- Worktree shows uncommitted sibling-wave writes (`swarm-registry.json` modified, sibling reports untracked) — other live seats; left untouched.
