# C1RulerRerun — round 48 (attempt 2) independent re-run of the committed configured-root ruler

Seat: `KotobaR48.C1RulerRerun` (leaf executor; no delegation). Lane base `75f671b109d8eddd0d64c1429bd6379fe577175a`.
Scratch candidate: `/fast/scratch/hyaku/kotoba-r48-a2/cand`, branch `r48-cand`, commit `26035dcec54d8e42f3a8b47ae8ca551c18aec295`.
My scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/KotobaR48.C1RulerRerun/` (`ruler-01` candidate, `ruler-02` BASE, `ruler-03` candidate determinism repeat).
Lane write: this report only. No lane/fleet/sibling VCS write, no commit, no push.

## Verdict

**The C1 counting command reproduces exactly as declared, and the committed before receipt is reproducible to the byte modulo paths and timestamps.**

| Run | Revision | Consumer sha256 | Exit | Verdict | target_failures | behavioral_mismatches | evaluation_errors |
|---|---|---|---|---|---|---|---|
| Candidate (ruler-01) | `26035dcec54d8e42f3a8b47ae8ca551c18aec295` | `2d824c0b3d4954c9a01868ee7c9b44c72b77bb5054419cf0539f6e4082f1b88a` | **0** | **clean** | **[]** | **[]** | [] |
| Candidate repeat (ruler-03) | same | same | **0** | **clean** | [] | [] | [] |
| BASE (ruler-02) | `197b5a4087bad49a465df7d13d7e821fe4cf227b` | `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1` | **1** | **failed** | `["singular-unlogged","plural-unlogged","both-distinct-unlogged","same-name-both-config-roots","configured-plus-other-log-root"]` | [] | [] |

13/13 oracle cases settled in every run; `current_unsettled` null, `remaining_not_observed` empty.
BASE failures are exactly the oracle's `expected_before_target_failures` and exactly the committed receipt's list, in the same order.
Oracle target check is `oc.roots.names_plus_builtin`; the candidate moves that row only, from 5 red cases to 0, and changes **no** non-target value.

## Findings

**F1 — The committed before receipt is reproducible, value-identical and byte-identical after path substitution.** My BASE re-run (fresh scratch, fresh clone path) matches the committed `.ufo/round-48/verification/before-configured-root.json` on every per-case `checks` map (28 values), every `statuses` map, `observed_count`, `target_met`, `base_prediction_met`, `exit`, `state`, `expected_target_count`, `predicted_base_count` — 13/13 cases. Top-level: identical `revision`, `verdict`, `target_failures`, `behavioral_mismatches`, `evaluation_errors`, `consumer_sha256_before/after`, `oracle_sha256`, `ruler_sha256`, `scope`, `expected_before_target_failures`, `schema`, `current_unsettled`, `remaining_not_observed`, `baseline_receipt_sha256` (null).

**F2 — The only differences are paths and the timestamp, and each is accounted for.**
- `recorded_at` differs (timestamp by design): committed `2026-10-22T01:15:33.359887+00:00` vs mine `2026-10-22T08:12:30.486911+00:00`.
- `source_command` differs only in the `-C` repo path (`…/kotoba-r48-author-handoff` vs `…/kotoba-r48-a2/cand`).
- Per-case `argv`, `cwd`, `environment` differ only by the scratch root prefix.
- `stdout_sha256` differs in 13/13 cases **only because the consumer's stdout embeds the absolute oc.log path**; substituting my scratch root with the committed scratch root reproduces the committed digest in **13/13** cases. Same for `stderr_sha256`: **13/13**.
- `inputs_before`/`inputs_after` differ in 4/13 cases **only in the `oc.log` digest** (the log line embeds the absolute path); substituting the scratch root reproduces the committed `oc.log` digest in **13/13** cases, and every other file digest is identical.

**F3 — Candidate delta is confined to the target row.** Per case, BASE → candidate `oc.roots.names_plus_builtin`: `both-distinct-unlogged` 2→4, `configured-plus-other-log-root` 3→4, `plural-unlogged` 2→3, `same-name-both-config-roots` 2→3, `singular-unlogged` 2→3; the other 8 cases unchanged (2/2, 2/2, 3/3, 3/3, 2/2, 2/2, 2/2, 3/3). All 27 non-target values and all 28 statuses are identical between BASE and candidate in every case. The 8 clean controls stay clean.

**F4 — Risk: this measurement is pinned to consumer sha256 `2d824c0b…`.** The candidate diff (`verifiers/verify_harness_independent.py`, +13/−8) touches only the `derive()` block; the `--self-test` region is **byte-identical** between BASE and candidate, so the candidate ships **no new regression arm** (plan Q05 unmet at this commit; consistent with `C1ClaimCritic` F4). Both consumers' `--self-test` still print `0 failure(s) over 104 assertions`, exit 0, so the existing `oc.roots.names_plus_builtin == 2` arm still holds, but nothing new guards the configured-root union. When the regression arm lands, the consumer sha changes, the ruler's `--consumer-sha256` must be re-pinned, and the L1 pre-run (`ruler-l1-01.json`, receipt sha256 `536b3687…`) no longer measures the landed bytes; `verifiers/floors-registry.json`'s `harness_independent` floor 104 must be bumped in step.

**F5 — Lane observation, not my change.** The lane working copy carried an uncommitted `M verifiers/verify_harness_independent.py` **before** this seat started and is unchanged by me; `git status --short` in the lane is identical before and after my run. Lane HEAD is still `75f671b109d8eddd0d64c1429bd6379fe577175a`. The candidate commit `26035dc` exists only in the scratch clone.

**F6 — Ruler bytes are the committed ones.** The ruler, oracle and before receipt I executed are byte-identical to the lane's and to the copy committed in the candidate clone: ruler `01af33a6724cb91ddcfd09b690fa7ba68114d799cc4552fa65d6519c3f78bd45`, oracle `1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883`, before receipt `8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312`. The ruler is not hash-checked by its own invocation (see `C1ClaimCritic` F5), so I verified it out of band by `sha256sum` on both the lane file and `git show 26035dc:.ufo/round-48/tools/config-root-ruler.py`.

## Evidence (commands, exit codes, paths)

```
# candidate run (exit 0, clean)
cd /fast/scratch/hyaku/kotoba-r48-a2/cand
python3 -B .ufo/round-48/tools/config-root-ruler.py \
  --repo /fast/scratch/hyaku/kotoba-r48-a2/cand \
  --revision 26035dcec54d8e42f3a8b47ae8ca551c18aec295 \
  --consumer-sha256 2d824c0b3d4954c9a01868ee7c9b44c72b77bb5054419cf0539f6e4082f1b88a \
  --oracle .ufo/round-48/oracle/config-root-cases.json \
  --oracle-sha256 1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883 \
  --scratch /fast/scratch/hyaku/kotoba-r48-a2/seats/KotobaR48.C1RulerRerun/ruler-01 \
  --baseline-receipt .ufo/round-48/verification/before-configured-root.json \
  --baseline-sha256 8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312
# -> {"behavioral_mismatches": [], "current_unsettled": null, "evaluation_errors": [],
#     "receipt": ".../ruler-01/receipt.json", "remaining_not_observed": [],
#     "settled_cases": 13, "target_failures": [], "verdict": "clean"}   EXIT=0

# BASE run, no baseline args (exit 1, failed, 5 target failures)
python3 -B .ufo/round-48/tools/config-root-ruler.py \
  --repo /fast/scratch/hyaku/kotoba-r48-a2/cand \
  --revision 197b5a4087bad49a465df7d13d7e821fe4cf227b \
  --consumer-sha256 872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1 \
  --oracle .ufo/round-48/oracle/config-root-cases.json \
  --oracle-sha256 1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883 \
  --scratch /fast/scratch/hyaku/kotoba-r48-a2/seats/KotobaR48.C1RulerRerun/ruler-02
# -> target_failures ["singular-unlogged","plural-unlogged","both-distinct-unlogged",
#     "same-name-both-config-roots","configured-plus-other-log-root"], verdict failed  EXIT=1

# determinism repeat of the candidate run -> identical stdout, EXIT=0 (ruler-03)
# one aborted invocation (my own typo: duplicated oracle sha) -> EXIT=2 "oracle_sha256 mismatch";
#   it failed before scratch creation, so no receipt and no side effect.
```

Receipt digests: `ruler-01/receipt.json` sha256 `613a6b5f88728f580ad953ba28314a84c405044df7c1c7e541ca5a6a86c175de`; `ruler-02/receipt.json` sha256 `4536e194069ecc599fed142a8ec78449061e91a58e3426444b3eeeba7de71999`; `ruler-03/receipt.json` sha256 `72f0f650c729f904b7d9102f5e818abd0df7bc6ff60f1f4f42393c9e8a321606`. All three record `consumer_sha256_before == consumer_sha256_after` (source custody intact).

Self-test (not part of the counting command, measured for the Q05 arm question): BASE consumer extracted with `git archive 197b5a4 verifiers` into `/fast/scratch/hyaku/kotoba-r48-a2/seats/KotobaR48.C1RulerRerun/base-tree` (sha256 `872993f8…`) and the candidate consumer in the clone both print `0 failure(s) over 104 assertions`, EXIT=0. Caveat observed: the self-test resolves `FIXTURE_DIR` relative to the script's own directory, so running a copy from `/tmp` instead of the repo path fails with `FAIL fixture dir present: /tmp/fixtures/harness-independent` (EXIT=1, 67 assertions) — an environment artifact, identical for BASE and candidate, not a candidate regression.

## Risk / blockers

- R1 — No blocker for the claim as written. The declared after-state (ruler exit 0, 0 target failures, 0 behavioral mismatches over the 13-case frozen matrix) is measured and reproducible.
- R2 — The measurement is bound to consumer sha256 `2d824c0b…`; the pending Q05 regression arm will change the consumer bytes, so the L1 must re-run the same command with the new sha and re-pin `--consumer-sha256` (and bump the `harness_independent` floor 104 in step).
- R3 — The matrix is 13 synthetic cases over one independent instrument; it does not exercise the producer, the comparator or a live opencode binary, and it says nothing about the unresolved built-in-marker join. "0 behavioral mismatches" must not be written as "no harm" or "the join is repaired".
- R4 — The lane working tree still holds an uncommitted consumer modification that is not mine; integration order should settle it before any landed-revision measurement.

## Tooling

Nothing installed or upgraded. Stock `python3` 3.14.8, `git` 2.56.0. No pacman transaction, no `uv`/`npm`/cargo install, no host service touched, no web source fetched or executed in this seat.
