# Round-37 per-axis verdict table — template (seat B2|scribe-shonen)

> Fill at the landing commit. Rule: **per-axis verdicts only, no scalars**
> (`.ufo/round-37/claims.json` round_contract); `harmed`/`unprovable` are recorded as such,
> never forced. A verdict is `improved` only when the claim's pre-registered
> before→after pair has been re-run **at the landing commit** and the counting command
> is pasted with its observed output. A SCORECARD score number may move only via the
> rubric bands and only alongside its counting command.
> Vocabulary: `improved` | `held` (= unchanged) | `failed-as-declared` | `unprovable` | `harmed`.

| Axis (ownership; r36 score) | Claim | Verdict | Counting command @ landing commit (paste output) | Evidence pointer | Limit / residual |
|---|---|---|---|---|---|
| depth (owned; 9) | C1 — source-blind re-derivation | `[PENDING: improved / failed-as-declared / unprovable]` | `python3 verifiers/verify_harness_independent.py` → exit 0, agreement N/28; `... --self-test` → `0 failure(s) over M assertions`; pinned-mutant tree → exit 1 naming the mutant | `corpus/knowledge/harness-independent-round37.md`; routing-registry pin | Source-blindness is unprovable post hoc if any builder opened `verify_harness_claims.py` / `baseline.json` harness rows — record who asserted blindness, not that it holds |
| operability (advisory; 8.5) | C2 — floors-guard pair | `[PENDING]` | `python3 verifiers/check_assertion_floors.py` on the two mutant copies: (a) two-table deletion → before exit 0 (M7 `scouts/M7.md`, re-measurable), after exit ≠0 class-named; (b) repointed `--script NAME=PATH` → before exit 0, after exit ≠0 class-named. Live run exit 0 all-PASS **byte-invariant** (diff vs pre-patch stdout); `--self-test` count vs floor | `verifiers/check_assertion_floors.py`; `drafts/b1/c2-before-probe.txt`; `scouts/M7.md` | M7 probed only the `pins` row of six; row-carrier ≠ all-rows claim. Timeout/hang class already closed r31 — do not re-claim it |
| freshness (advisory; 8.0) | C3 — CommonMark fence spec | `[PENDING]` | `python3 verifiers/verify_skill_checklist.py --self-test` → `0 failure(s) over N assertions` (floor bump in-step); planted-shape matrix vs pinned expected classification → 0 misclassifications; `diff -r` of 71 `verifiers/fixtures/checklist` dirs vs pre-state → byte-identical (paste `git status` or a sha before/after) | `verifiers/verify_skill_checklist.py`; new fixtures; `drafts/s2/spec-{0.30,0.31.2}.txt` (oracle text) | If the oracle is a library (`cmark`), the install command + receipt must be in the report or the oracle is unpinned prose |
| consistency (owned sub-axis of calibration; 10) | — (no claim) | `held` unless a claim's record changed it | re-run only if a r37 record correction lands: `python3 verifiers/verify_corpus_integrity.py` + `verify_corpus_independent.py` both exit 0 and agree | SCORECARD consistency row | Band 10 rests on r12; no new non-author act this round |
| coverage (advisory; 8.5) | — (no claim) | `held` | `python3 verifiers/verify_surfaces.py` → 7 × PASS exit 0 (regression guard only) | SCORECARD coverage row | Census-vs-prose parity stays id-level (r13 limit) |
| calibration (advisory; 8.5) | — (no claim) | `held` unless r37 lands corrections | the corrections' own commands (e.g. `grep -n '10/88/52/82/1504/51\|corpus_integrity 88' SCORECARD.md` → :117/:166 stale-floor sites) | SCORECARD calibration row | If the stale-floor sites land, the calibration verdict is `improved` only with the landing seat's diff + the re-run command |
| adjacency (advisory; 8.0) | — (no claim) | `held` | `git -C ../<sibling> log --oneline -1` ack probe only if a route lands | SCORECARD adjacency row | Acks were 0/5; not re-measured this round unless a seat did |

## Cross-check rows (must hold for any `improved` above — a trade is recorded, never smoothed)

| Check | Command | Gate |
|---|---|---|
| No regression elsewhere | the eight-gate battery: harness / floors / checklist (live + `--self-test`) / corpus_integrity / corpus_independent / surfaces / pins / fault `--self-test` | all exit 0 at the landing commit; any red → `harmed` on the touched axis |
| Self-test floors bumped in-step | `python3 verifiers/check_assertion_floors.py` → 6 × PASS with `floor == observed` | observed floor values at 041f6ba: `10 / 119 / 59 / 87 / 1504 / 62` — the dispatch brief's `82 / 51` are stale (r31/r32 bumps) |
| Fixture byte-invariance | `diff -r` or sha256 manifest of `verifiers/fixtures/checklist` (71 dirs) before vs after | any diff → named in the report, not silently accepted |
| Disclosure | every seat's `[PENDING]`-cell filled from its report, never by smoothing | a red or unprovable cell stays red/unprovable in the table |

## Reporting form (one line under the table, r35/r36 precedent)

`Axis verdicts: <axis> — <verdict> (<one-clause reason>); all others <held>[, or list>. No trade.`
then `Drift handling: <record corrections, dead rejections, residuals>.`