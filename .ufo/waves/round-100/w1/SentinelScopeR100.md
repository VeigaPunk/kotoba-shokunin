# SentinelScopeR100 — scope, safety and no-harm on the round-100 candidate

Seat: SentinelScopeR100. Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin.
Base/freeze: 03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687. Instrument: d1e1170d950fc378bb6a28bbfc5a62802669be86.
Scratch: /fast/scratch/hyaku/kotoba-r100/SentinelScopeR100 (TMPDIR/HYAKU_SCRATCH exported; removed before yield).
Receipts: `.ufo/waves/round-100/w1/SentinelScopeR100/` (scripts + raw outputs).

Status: COMPLETE. All three builder READY files landed (ScribeCorpusR100 at 13:00, ExecAnchorR100 at
12:36, ExecArmsR100 at 12:39); every reading below is on the final candidate built from the READY
patches. **Verdict: SCOPE PASS, SAFETY PASS, NO-HARM PASS** (one expected, reported drift: the two
corpus gates).

## Candidate

Built in `/fast/scratch/hyaku/kotoba-r100/SentinelScopeR100/cand` — a fresh `git clone --shared` of the
lane at 03a98eb, patches applied in the frozen order ScribeCorpusR100 → ExecAnchorR100 → ExecArmsR100,
committed with the scratch identity (`git rev-parse --show-toplevel` = the clone dir).

**Candidate revision: `548d911b2a1e810451784eabcc2478a33efe0b0c`**

`git -C <cand> diff --stat 03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687 HEAD`:
```
 corpus/SOURCES.md                    |   4 +
 corpus/lessons/round-100.md          | 347 +++++++++++++++++++++++++++++++++++
 verifiers/check_tip_battery.py       |   5 +-
 verifiers/verify_dispatch_prompts.py | 144 +++++++++++++++
 verifiers/verify_skill_checklist.py  |  85 ++++++++-
 5 files changed, 579 insertions(+), 6 deletions(-)
```
(the 6 deletions are the 4 correction-row lines, the old fix line and the old pin line)

| seat | patch sha256 | matches its READY |
|---|---|---|
| ScribeCorpusR100 | `042c22700eb5b0ac343686ba67cbaf6ba77acbcabdbccf234d971b964ccc67d1` | yes |
| ExecAnchorR100 | `f2d1efee8815ef635859fdb2b805e09973ceb6c70a34b447d0005b92c87d9c92` | yes |
| ExecArmsR100 | `7b4e2dbc2450ebbc34360c557897b9b60f0895005cd1d0d631b4dac1746c857e` | yes |

Each patch applied with `git apply --check` first. The scribe patch changed between 12:51
(`76b30aad…`) and its 12:56 READY (`042c2270…`); the candidate was rebuilt and every reading re-taken
on the final bytes.

## Baseline at 03a98eb (pre-candidate reference, measured by this seat)

| check | observed |
|---|---|
| `check_gate_registry.py --rev 03a98eb…` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0 |
| `verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 |
| `check_assertion_floors.py --self-test` | `0 failure(s) over 176 assertions`, rc 0 |
| dispatch live over `/home/vgpnk/Projects/shokunin/.ufo/prompts` | rc 1; `FAIL dispatch.04: evaluated 1229 — 1201 PASS, 6 FAIL, 22 N/A; 29 out of scope`; `FAIL dispatch.08: evaluated 1221 — 1182 PASS, 10 FAIL, 29 N/A; 14 out of scope` (fleet prompt files, not the checker) |
| checklist real tree (fleet-shaped sandbox) | rc 0, 11 `PASS ` ids |
| census `--file …/corpus/SOURCES.md` | rc 0, 34 `W04`, `file ok …` |
| round-99 counter `c1` | `C1 targets killed 12 of 12 (run errors 0); … C1-PREDICATE-MET`, rc 0 |
| round-99 counter `r98c1` | `R98C1-PREDICATE-MET`, rc 0 |
| tip battery | `guards 5 of 5; tip battery exit 0: 4 of 6`; red: verify_corpus_integrity.py exit 1, verify_corpus_independent.py exit 1 |

## Scope checks (independent of the counters; `scope_check.py`, receipts in the seat dir)

| # | check | result |
|---|---|---|
| 1 | changed file set ⊆ owned files | **PASS** — exactly `corpus/SOURCES.md`, `corpus/lessons/round-100.md`, `verifiers/check_tip_battery.py`, `verifiers/verify_dispatch_prompts.py`, `verifiers/verify_skill_checklist.py`; no extra file, none missing |
| 2 | SKILL.md and frozen instruments byte-identical | **PASS** — SKILL.md, verify_corpus_integrity.py, verify_corpus_independent.py, floors-registry.json, corpus-baseline.json identical; no `*verifier-spotcheck*` file and no `verifiers/fixtures/` path touched |
| 3 | dispatch production code outside `self_test()` | **PASS** — byte-identical; the `self_test()` diff opcodes are `['equal','insert']` only (one insert-only region) |
| 4 | checklist fix line | **PASS** — FIX_LINE (`^(.+\.\w+):\d+(-\d+)?(,\d+(-\d+)?)*$`) occurs once, BASE_LINE zero times |
| 5 | checklist confined | **PASS** — after (BASE_LINE→FIX_LINE, delete `self_test` body, delete `GOVERNANCE_CORRECTIONS`) both revisions are identical; corrections rows 20 → 19, removed exactly `(3598, 4941…, 'SCORECARD.md', 529, 'corpus/lessons/round-80-verifier-spotcheck.md:30,37', …)`, nothing added |
| 6 | battery pins-only | **PASS** — identical outside the `INSTRUMENT_PINS` block |
| 7 | SOURCES.md append-only rows | **PASS** — pure-addition diff (0 deleted lines), 4 added 11-column rows S282, S283, S284, S285; next heading `## Paths` |
| 8 | round-100 lesson new | **PASS** — absent at base, present at candidate (347 lines) |
| 9 | frozen C1 anchors | **PASS** — all 49 distinct anchor texts of CLAIMS `c1`/`r99c1`/`r98c1`/`r97c1`/`r96c1` (targets + positive) occur exactly once in the candidate `verify_dispatch_prompts.py` |

## No-harm checks (base vs. candidate)

| check | base | candidate | verdict |
|---|---|---|---|
| `check_gate_registry.py --rev` (run from the clone so `LANE` resolves there) | 74 of 74, phantom 0, rc 0 | 74 of 74, phantom 0, rc 0 | **PASS** |
| round-99 counter `c1` | MET 12 of 12 | `C1 targets killed 12 of 12 (run errors 0); … C1-PREDICATE-MET`, rc 0 | **PASS** |
| round-99 counter `r98c1` | MET | `R98C1-PREDICATE-MET`, rc 0 | **PASS** |
| `check_assertion_floors.py --self-test` | 0 of 176, rc 0 | 0 of 176, rc 0 | **PASS** |
| `verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 | `boxes proven 2`, rc 0 | **PASS** |
| dispatch live over `/home/vgpnk/Projects/shokunin/.ufo/prompts` | rc 1, 2 FAIL lines | rc 1, byte-identical verdict lines (`diff` empty) | **PASS** |
| checklist real tree (fleet-shaped sandbox) | rc 0, 11 PASS ids | rc 0, 11 PASS ids, `diff` empty | **PASS** |
| census `--file` candidate SOURCES.md | 34 W04, rc 0 | 35 W04 (S285 shares S279's URL — a warning), rc 0 | **PASS** |
| tip battery (candidate bytes: `$D/verifiers/check_tip_battery.py --repo $D --rev cand --fleet fleet`) | guards 5 of 5, 4 of 6 | `guards 5 of 5; tip battery exit 0: 4 of 6` | **PASS (expected drift)** |

**Reported drift (not a C1/C2 failure):** at the candidate `verify_corpus_integrity.py` and
`verify_corpus_independent.py` exit 1 with
`DRIFT corpus.index.tracked_files: observed=206 expected=204`, `corpus.index.unindexed: observed=2
expected=0`, `corpus.pointers.report_total: 176 vs 175`, `corpus.pointers.commit_total: 75 vs 72` — the
unindexed round-99 spot-check lesson plus the new round-100 lesson; the L1's coverage-map rows and
equal-mode baseline re-record heal it at integration. The C2 counter does not read these gates.

## Safety checks

| check | result |
|---|---|
| no hardcoded `/tmp` in added code | **PASS** — no added line (python or corpus) contains `/tmp` |
| no network in the new self-test code | **PASS** — no socket/urllib/http/requests/subprocess in any added line |
| fixtures under TMPDIR | **PASS** — checklist arms use `tempfile.TemporaryDirectory(prefix="kotoba-comma-anchor-")`; dispatch arms use the existing `root` TemporaryDirectory (`prefix="dispatch-selftest-"`) |
| chmod-000 fixture | **PASS** — `victim.chmod(0o000)` inside `try`, restored `0o600` in `finally`; the fixture lives under the self-test's TemporaryDirectory and is removed with it |
| no credential-shaped strings | **PASS** — no api-key/secret/password/bearer/private-key shapes in any added line |
| no source-sniffing in new arms | **PASS** — no `__file__`, `inspect`, `getsource`, or read of the instrument's own path; arms call `main`/`run_checks`/`read_text`/`check_citation_resolves`/`check_governance_citations` and read the result; every assertion goes through `rec(...)` inside `try/except` |
| lane untouched by seats | **PASS** — `git -C lane status --porcelain` lists only the L1's wave artifacts (`r100-w1-*.json`, `r100-w1.ready*`, `.ufo/waves/round-100/w1/`); `ls` shows no clone at the lane root (`kotoba-shokukin` is tracked since round 75/76, `receipts_tmp` is empty and predates the round) |

## Findings

1. **No scope or safety defect found.** Every changed path is owned; every frozen byte is intact; the
   two code changes are confined exactly as the plan admits (one insert-only `self_test()` region in
   the dispatch checker; the fix line + `self_test()` arms + one corrections row in the checklist; one
   `INSTRUMENT_PINS` admission in the battery).
2. **Invocation note (not a defect).** `check_tip_battery.py` reads `INSTRUMENT_PINS` from the module
   it executes, so a battery run must use the candidate's own bytes (`$D/verifiers/check_tip_battery.py`)
   — running the lane's round-base copy against the candidate reads `FAIL guard instrument-pin … not a
   pinned blob` (guards 4 of 5). With the candidate's bytes the guard is 5 of 5. `check_gate_registry.py`
   pins `LANE = Path(__file__).parent.parent`, so it must likewise be run from the candidate clone.
3. **`corpus/SOURCES.md` +1 W04** (S285 shares S279's URL with a different scope): a warning, census
   rc 0; the scribe's READY states it.
4. **Checklist real-tree token count moves by one** (`governance.citation_resolves` 1665 → 1666,
   corrections excused 19 → 18): the retired correction row's token is now evaluated and resolves
   through the fix line — the intended behaviour, gate still GREEN with the same 11 PASS ids.

## Risks

- The two corpus gates stay red at the candidate until the L1's index rows and baseline re-record; a
  landing that skips them would ship a red battery (already the base state for the round-99 lesson).
- The C2 kill conjunct runs the revert mutant on disk only (the counter discloses this); the arm's
  behaviour-only construction was reviewed here and reads no source, so the disclosed bound is not
  exercised by this candidate.
- Disclosed counter bounds (cmdline readable to a child, state outside per-run dirs) are unchanged by
  this candidate and are not this seat's surface.
