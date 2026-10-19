source: `.ufo/round-41/drafts/v10/probe-results.json`, `.ufo/round-41/drafts/v10/subprocess-replay.json`, `.ufo/round-41/drafts/v10/channel-census.json`, `.ufo/round-41/drafts/v10/union-live/union-battery.json`; reproduced with `python3 .ufo/round-41/drafts/v10/replay-probes.py` and `python3 .ufo/round-41/drafts/v10/channel-census.py`.
verified-at: 2026-10-19T16:56:09Z
recheck: From repo root, run `PYTHONDONTWRITEBYTECODE=1 python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` for the exact-input R45 replay; run the fresh live join, comparator self-test, assertion floors, and both corpus gates using the commands in `.ufo/round-45/scouts/V10.md`.

# Round 41 V10 — frozen comparator channel census

## Measurement boundary

The replayed target is the frozen comparator at HEAD `b1be35f9522f21c0c5b39879358a011806ab9200`, tree `8bb24450a9c500c427019c7147013b4946525b09`, SHA-256 `1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`. The frozen scope-file SHA-256 is `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`; the captured live and independent payload SHA-256 values are `0bc250f5197c9dbbdbdce7e15c4220e0904118a8c290f81295aa18464b0b0341` and `eb1068a4f7b934d5553106d60737c05d8f1cd8d9ef827467f80281cac3853887` respectively.

`subprocess-replay.json` records every arm's exact argv, process CWD, `--cwd`, scope argument, exit, headline, reason and before/after input hashes. The replayer executes actual subprocesses; it reproduced 46/46 saved outcomes and all input hashes were unchanged. `channel-census.json` applies an explicit static classification to each unique arm ID and validates exact set equality: 46 expected, 46 classified, no missing or extra IDs.

Classification counts are **25 open, 15 closed, 4 controls, 1 diagnostic and 1 caller-selected trust input**. “Open” means a deliberately adversarial representation or shadow reached exit 0; it does not mean the ordinary producer path emitted that payload. “Closed” means the inconsistency was rejected or reported as a disagreement. The four controls are not exploit passes. The absolute scope-file arm is separate: the caller explicitly selected that file, so its acceptance tests the caller's trust choice, not bypass of the selected file.

## Open channels

- **Expected/value representations and identity aliases:** `heldout-expected-only-full-copy`, `heldout-expected-value-secondary-shadow`, `heldout-flat-dotted-map`, `heldout-id-alias-conflict`, `heldout-nested-checks-map`, `heldout-nested-expected-wrapper`, `heldout-nested-observations-wrapper`, `heldout-observed-key-shadow`, `heldout-rederived-vs-value-shadow`, and `heldout-wrapper-precedence-expected-over-observations` all exit 0. The wrapper-precedence arm specifically supplies `expected=7` and `observations=999`; the secondary-key arms show that conflicting aliases can be ignored while the ordinary join remains green.
- **Status/metadata:** `heldout-duplicate-id-status-shadow`, `status-nonstring-hides-state`, `x2-state-shadow`, and `top-level-status-and-alternatives` exit 0. In particular, duplicate `UNLANDED` versus `DERIVED`, non-string `status` with `state=UNLANDED`, and `status=DERIVED` with `state=UNLANDED` do not force a non-green result.
- **Scope/evidence/probes:** `r1-f4-payload-chosen-probe-target`, `record-probe-fallback-reads-results-only`, `record-probe-shadowed-by-top-level-map`, `unmatched-extra-scoped-out-probe`, `scoped-out-reason-and-evidence-drift`, and `w1-scoped-row-carries-value` exit 0. The arms demonstrate that the payload can select a probe target, probe channels can be ignored or shadowed, unmatched probes are accepted, and scoped-out reason/evidence or a scoped-out row's value can change without rejecting the join.
- **Relative scope-file resolution:** `r1-f3-prime-scope-file-cwd` exits 0 at 23/23 with five scope-outs when launched from `planted-cwd` using relative `--scope-file verifiers/harness-independent-scope.json`. `cwd-replay-receipt.json` records the five-row planted set but its scope digest resolves relative to `--cwd` and identifies the honest scope file instead. The paired `r1-f3-prime-scope-file-honest-cwd-control` exits 2 with the honest process CWD. This is a process-CWD versus `--cwd` resolution split, not a claim that the honest invocation passes.
- **Caller-supplied live JSON:** `live-mode-positive-masks-independent-drift`, `live-mode-split-across-row-channels`, `live-top-level-observed-summary-divergence`, and `live-verdict-shadow-in-row-channel` exit 0. These arms mutate caller-provided live JSON. They do not establish that `verify_harness_claims.py`'s normal producer emits these mutations; the fresh producer capture and join below passed.

## Closed cases and diagnostic

The direct `NOT DERIVED` expected-value claim (`r1-f2-expected-not-derived`), a consistent value disagreement (`f3-consistent-value-disagreement`), missing or divergent record channels (`checks-record-list-divergent`, `f3-rows-missing`, `r1-f3-rows-shadow`, `results-dotted-map-divergent`, `row-map-divergent`, `v1-a7-checks-shadow`, `w1-stringified-rows`), duplicate-id divergent values (`t1-duplicate-id-divergent-copy`), an explicit primary `UNLANDED` (`status-primary-unlanded`), scope-set laundering (`scope-uncommitted-extra-row`), and a SCOPED_OUT record missing its map (`scoped-out-record-without-map`) are rejected or reported non-green. `live-mode-equal-with-independent-drift` likewise reports exit 1. Four ordinary format/baseline controls pass: `checks-record-list-control`, `control`, `results-dotted-map-control`, and `row-map-agreeing-control`.

`headline-uncovered-count` rejects the missing row with exit 2, but reports `headline.live_checks=29` although its captured live input contains 28 checks. Treat this as a diagnostic count/reporting defect, not a passed arm or an open bypass.

The separate C2 attempt in `union-live/union-battery.json` is invalid evidence: its control and every C2 arm failed to launch the guard because the working-directory path was duplicated (`can't open file .../guard-world/.ufo/round-41/drafts/v10/union-live/work/guard-world/verifiers/check_assertion_floors.py`). Only that invalid `work/guard-world/` scratch tree and its C2-only `work/outside-stub.py` were pruned. The adjacent C1 `work/ind-*.json` payloads, `work/live.json`, outer C1 captures/results, planted carrier, receipts and useful probes were retained. No comparator or floors/verifier source was changed for this census.

## Fresh live-path check

The current producer capture and join were rerun from the repository root:

```bash
python3 verifiers/verify_harness_claims.py --json > .ufo/round-41/drafts/v10/live-current.json
python3 verifiers/verify_harness_independent.py --json > .ufo/round-41/drafts/v10/independent-current.json
python3 verifiers/compare_harness_independent.py --live-json .ufo/round-41/drafts/v10/live-current.json --independent-json .ufo/round-41/drafts/v10/independent-current.json --cwd /home/vgpnk/Projects/shokunin/kotoba-shokunin --scope-file verifiers/harness-independent-scope.json --no-stamp --json --receipt .ufo/round-41/drafts/v10/current-join-receipt.json
```

Observed: both producer commands exit 0 with 28 records; the join exits 0 with protocol 24/24, strict 20/24, four adjudicated rows, four scoped out, and zero disagreements, unknowns or uncovered rows. Full outputs and the freeze-before-compare receipt are retained as `live-current.json`, `independent-current.json`, `current-join.json` and `current-join-receipt.json` under `.ufo/round-41/drafts/v10/`.

## Round 45 calibration annotation (append-only)

This annotation preserves the R41 measurement above; it does not replace or reinterpret the original 25-open / 15-closed / 4-control / 1-diagnostic / 1-trust-input baseline. The census `source` paths point into the pruned `.ufo/round-41/drafts/v10/` tree, so this recheck is bounded by retained sidecars and payload copies.

Using settled comparator blobs from `6881ce31912cf52982de733d18d25e7ab7aae5c4` (SHA-256 `d8b8c7f6001db7f47a294dc2a98db9179f61a281be20293dc5b104906073679d`) and `032f47bd13fdff0cd2ccea5f902df9690ad09376` (SHA-256 `13b6d791705be81a349178f2e392adf19012a64315a51c77856fcf2f98e8ca56`), the 46-arm regenerated comparison reported R43 counts of 15 open / 25 closed / 4 controls / 1 diagnostic / 1 trust input, then R44 counts of 11 open / 29 closed / 4 controls / 1 diagnostic / 1 trust input. R43's first-close set in that regenerated comparison was `heldout-flat-dotted-map`, `heldout-nested-checks-map`, `heldout-nested-expected-wrapper`, `heldout-nested-observations-wrapper`, `heldout-wrapper-precedence-expected-over-observations`, `r1-f3-prime-scope-file-cwd`, `status-nonstring-hides-state`, `top-level-status-and-alternatives`, `w1-scoped-row-carries-value`, and `x2-state-shadow`. R44 added `heldout-expected-only-full-copy`, `heldout-id-alias-conflict`, `heldout-observed-key-shadow`, and `heldout-rederived-vs-value-shadow`. The regenerated R44 replay reported these 11 remaining exit-0 arms: `heldout-duplicate-id-status-shadow`, `heldout-expected-value-secondary-shadow`, `live-mode-positive-masks-independent-drift`, `live-mode-split-across-row-channels`, `live-top-level-observed-summary-divergence`, `live-verdict-shadow-in-row-channel`, `r1-f4-payload-chosen-probe-target`, `record-probe-fallback-reads-results-only`, `record-probe-shadowed-by-top-level-map`, `scoped-out-reason-and-evidence-drift`, and `unmatched-extra-scoped-out-probe`. Counts, comparator pins, generated inputs, and per-arm outcomes are in `.ufo/round-45/drafts/n3/r43-r44-census-compare.json` (SHA-256 `bc7a9bd4f8a8c511b88b33edd60a7169948737ace29809535649cc9d3682874a`); the run used `.ufo/round-41/evidence/v10-census-probes.py` and fresh producer captures, not the exact archived arm payload set.

**Input-generation caveat:** the original probe/replay sidecars named by this census are retained as `.ufo/round-41/evidence/v10-probe-results.json` (SHA-256 `cf60e7a9f374684e80c173de32f56fd8efbf58eefd6d88069daa9e2b49029d70`) and `v10-subprocess-replay.json` (SHA-256 `991d8d95eb53c196ed5d74d9e4f23a9f948e29bc8e8480b81cbd430648baedb5`). N1's rebound check (`.ufo/round-45/drafts/n1/probe-results-rebound.json`, SHA-256 `3050b51f754be1d7834758ed84c72a2e18433a93a50978b715840263dc738d82`) and N2's comparison matrix (`.ufo/round-45/drafts/n2/v10-rerun-matrix.json`, SHA-256 `3c1f349296bd46c2b4f08001b74f53c7e22da3f765ce9a1648b8039c1d84d1e6`) both identify seven independent payload hash mismatches against those R41 pins: `r1-f3-prime-scope-file-cwd`, `r1-f3-prime-scope-file-honest-cwd-control`, `r1-f4-payload-chosen-probe-target`, `record-probe-fallback-reads-results-only`, `record-probe-shadowed-by-top-level-map`, `scope-file-caller-selected-absolute`, and `scope-uncommitted-extra-row`. N2 records saved-arm hash matches for 39/46. The `r1-f3-prime-scope-file-cwd` mismatch is in the R43 first-close set; therefore its first-close attribution is only demonstrated for the regenerated/rebound payload, not established for the exact original R41 bytes. The four new R44 closures and the other nine R43 first-closures have matching saved input hashes in N2's matrix. N3's `.ufo/round-45/drafts/n3/replay-13b6.json` (SHA-256 `01e42622eac20fe063e1c376edbc2f4ed6f34666b758f18d7ab4c35135638d47`) records before/after stability for its path-rebound inputs; `all_inputs_unchanged` does not establish equality to the original pins. H06/H07 replay sidecars use the distinct unprefixed `probe-results.json` / `subprocess-replay.json` pair (SHA-256 `b6293543fcc16b510846cad7f435a3c0fc2a6aa090e4b494f6d9653b021876da` / `9f187342c9d2f0676b0a7851d58ff45a19ba335bc0216cbd1ea8da0666f4ec5c`); those are internally matched but share the seven differences and are not an independent exact-byte confirmation of the original V10 inputs. Thus 13 first-closure attributions are supported by matching saved-input hashes (nine at R43 and four at R44); the exact R43/R44 classification of the four changed originally-open inputs is not fully re-established. Keep the recorded counts above labeled as regenerated-input results until the original payload bytes are recovered and replayed.

## Round 45 exact-input reconciliation (append-only)

This annotation preserves the R41 baseline and N3's regenerated-input caveat above. `PYTHONDONTWRITEBYTECODE=1 python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` replayed the 46 registered R41 arms against the Git-frozen landed comparator `032f47bd13fdff0cd2ccea5f902df9690ad09376:verifiers/compare_harness_independent.py` (SHA-256 `13b6d791705be81a349178f2e392adf19012a64315a1c77856fcf2f98e8ca56`), not the moving worktree file. The source replay and census JSON pins are `991d8d95eb53c196ed5d74d9e4f23a9f948e29bc8e8480b81cbd430648baedb5` and `5cb218e133ef07a973e0a02ea1fd86f809eda213e9259a652fe92e949c6501b0`; reconstructed arm payloads were verified against all 138 live/independent/scope hashes and remained unchanged. The durable replay is `.ufo/round-45/evidence/v10-post-r44-hunt.json`; the source payload reconstruction and runner are under `.ufo/round-45/evidence/v10-reconstructed-inputs/` and `.ufo/round-45/drafts/v10/post-r44-hunt.py`.

Of the 25 arms historically classified open, 10 remain exit 0 and 15 exit nonzero on these exact saved inputs:

| R41-open arm | R45 exit | Replayed result |
| --- | ---: | --- |
| `heldout-duplicate-id-status-shadow` | 0 | Still accepted: duplicate-id status shadow |
| `heldout-expected-only-full-copy` | 2 | Derived-set overflow |
| `heldout-expected-value-secondary-shadow` | 0 | Still accepted: conflicting secondary `expected_value` shadow |
| `heldout-flat-dotted-map` | 2 | Scope-out value laundering rejected |
| `heldout-id-alias-conflict` | 2 | Record identity aliases conflict |
| `heldout-nested-checks-map` | 2 | Scope-out value laundering rejected |
| `heldout-nested-expected-wrapper` | 2 | Scope-out value laundering rejected |
| `heldout-nested-observations-wrapper` | 2 | Scope-out value laundering rejected |
| `heldout-observed-key-shadow` | 2 | Derived-value aliases conflict |
| `heldout-rederived-vs-value-shadow` | 2 | Derived-value aliases conflict |
| `heldout-wrapper-precedence-expected-over-observations` | 2 | Scope-out value laundering rejected |
| `live-mode-positive-masks-independent-drift` | 0 | Still accepted: supplied positive live mode masks drift |
| `live-mode-split-across-row-channels` | 0 | Still accepted: live mode split across row channels |
| `live-top-level-observed-summary-divergence` | 0 | Still accepted: top-level observed/summary divergence ignored |
| `live-verdict-shadow-in-row-channel` | 0 | Still accepted: live verdict shadow |
| `r1-f3-prime-scope-file-cwd` | 2 | Scope-out value laundering rejected on the planted-CWD input |
| `r1-f4-payload-chosen-probe-target` | 2 | False blocker: archived target `.ufo/round-41/drafts/v10/builder-carrier` is absent; this does not prove semantic closure |
| `record-probe-fallback-reads-results-only` | 0 | Still accepted: results-only probe fallback |
| `record-probe-shadowed-by-top-level-map` | 0 | Still accepted: top-level map shadows record probe |
| `scoped-out-reason-and-evidence-drift` | 0 | Still accepted: scoped-out reason/evidence drift |
| `status-nonstring-hides-state` | 2 | Non-string `status` / `UNLANDED` state split rejected |
| `top-level-status-and-alternatives` | 2 | Uncontracted top-level `provisional` rejected |
| `unmatched-extra-scoped-out-probe` | 0 | Still accepted: unmatched extra scope-out probe |
| `w1-scoped-row-carries-value` | 2 | Scope-out value laundering rejected |
| `x2-state-shadow` | 2 | Conflicting status/state aliases rejected |

The `r1-f4-payload-chosen-probe-target` nonzero is an environment-dependent false blocker: the archived probe target directory no longer exists, so this result cannot establish whether target selection was semantically corrected. `r1-f3-prime-scope-file-cwd` rejected during metadata construction before receipt writing; the absent `.ufo/round-45/evidence/v10-post-r44-cwd-replay-receipt.json` is expected for that early error, not a missing successful-run receipt.

The two separately replayed R44 X2 residuals remain exit 0 on the same frozen comparator: `x2-expected-expected-value-conflict` and `x2-lone-nonstring-status`. These 46 arms are the R41 registered census only; this annotation does not claim completeness across other Round 45 held-out hunts.
