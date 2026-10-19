source: `.ufo/round-41/drafts/v10/probe-results.json`, `.ufo/round-41/drafts/v10/subprocess-replay.json`, `.ufo/round-41/drafts/v10/channel-census.json`, `.ufo/round-41/drafts/v10/union-live/union-battery.json`; reproduced with `python3 .ufo/round-41/drafts/v10/replay-probes.py` and `python3 .ufo/round-41/drafts/v10/channel-census.py`.
verified-at: 2026-10-19T16:56:09Z
recheck: When the comparator, its input schema, scope file, or receipt code changes, rerun the saved-arm subprocess replay and the live join commands below; check every arm classification and rerun both corpus gates.

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
