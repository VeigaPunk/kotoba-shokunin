# FrAttempt1Audit — inherited state audit of attempt-1 commits (read-only)

Scope: verify attempt 1's landed state `c0185da` (instrument+ruler+oracle) and `75f671b`
(before receipt) at lane HEAD `75f671b109d8eddd0d64c1429bd6379fe577175a`, base `197b5a4`.
Method: sha256 of committed bytes, plus a full independent re-derivation of the BASE matrix
with the committed ruler+oracle against the lane repo (fresh scratch under my seat;
lane repo untouched — read-only `git show` inside a private clone).

## Verdict: attempt-1 state is internally consistent and re-derivable; reuse it

No defect found in the four committed artifacts. All hash chains close. The BASE
receipt's case values were reproduced byte-identically in every graded field from lane
bytes alone. Closure needs none of attempt 1's private scratch.

## Findings

1. **instrument.json ↔ committed ruler/oracle/consumer hashes: MATCH.**
   - `instruments[0]` ruler `01af33a6724cb91ddcfd09b690fa7ba68114d799cc4552fa65d6519c3f78bd45`
     = sha256(`.ufo/round-48/tools/config-root-ruler.py`) at `75f671b`.
   - `instruments[1]` oracle `1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883`
     = sha256(`.ufo/round-48/oracle/config-root-cases.json`); same value as the plan's
     `--oracle-sha256`.
   - `consumer` sha256 `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1`
     and git_blob `06322fc5b0231d9bdc6cb4128c336cc5f1d53597` both verified against
     `git show 197b5a4:verifiers/verify_harness_independent.py` (byte hash and
     `git rev-parse` agree). Working tree is clean for all four files vs HEAD (only the
     consumer is locally modified, uncommitted, by this attempt — not part of the audited state).

2. **Before receipt hash triples: MATCH.**
   Receipt `.ufo/round-48/verification/before-configured-root.json` records
   `ruler_sha256` = committed ruler hash, `oracle_sha256` = committed oracle hash,
   `consumer_sha256_before` = `consumer_sha256_after` = base consumer hash,
   `revision` = `197b5a4087bad49a465df7d13d7e821fe4cf227b`. File sha256 is
   `8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312` = the plan's
   `--baseline-sha256`, and equals the private `immutable_before_receipt` copy on disk,
   so the lane copy is canonical, not a divergence.

3. **Receipt case values follow from the base consumer: PROVEN by re-derivation.**
   Re-ran the committed ruler: `/usr/bin/python3 -B …/config-root-ruler.py --repo <clone of
   lane> --revision 197b5a4… --consumer-sha256 872993f8… --oracle …/config-root-cases.json
   --oracle-sha256 1d09a38c… --scratch <fresh seat dir>`. Exit code 1 (verbatim;
   = `expected_ruler_exit`), stdout: `"verdict": "failed"`, `target_failures` exactly
   `["singular-unlogged","plural-unlogged","both-distinct-unlogged","same-name-both-config-roots",
   "configured-plus-other-log-root"]`, `behavioral_mismatches: []`, `evaluation_errors: []`,
   13/13 cases settled, `current_unsettled: null`.
   Deep diff committed vs reproduced receipt: the only differing fields are
   `recorded_at` (timestamp), `source_command[2]` (repo path), all 13 `stdout_sha256`
   and the `oc.log` input digests of cases with non-empty `log_sources`. A field-level
   diff of the actual stdout JSON (old scratch vs mine, case `control-agents-only`)
   shows every byte difference sits inside `probe`/`evidence`/`target` free-text that
   embeds the absolute scratch path; every `check` value, `status`, count, and
   `target_met`/`base_prediction_met` is identical. Per-case CLI exits all 0 =
   `expected_cli_exits` (13×0); 8 clean controls = `expected_clean_controls`; oracle
   self-checks (`consumer_sha256`, `expected_before_ruler_exit: 1`,
   `expected_candidate_ruler_exit: 0`) agree with instrument.json.

4. **Private-path references (`/fast/scratch/hyaku/kotoba-r48-author*`): present but
   non-load-bearing for closure.** 183 matching lines: ruler **0**, oracle **0**,
   instrument.json **13**, receipt **170**. In the receipt they are historical records of
   attempt 1's run environment (per-case `argv`/`cwd`/`environment`/`inputs_*` and
   `source_command`), superseded by the reproduction above — the consumer bytes are
   pinned by hash and re-derivable from the lane at `197b5a4`. In instrument.json:
   `writer_tree`, `literal_parent_base_argv`, and seven artifact pointers (below).

## Not re-verifiable from the lane (name as such in closure)

All exist on disk today (verified this session) but are attempt-1 private scratch with no
custody contract; the plan already says attempt-1 private trees "are not continued":

- Superseded ruler intermediates `config-root-ruler.a12f8542.py` (hash-verified
  `a12f8542…`), `.51012dbd.py` (`51012dbd…`), `.abe965ec.py` (`abe965ec…`) — the
  instrument's pre-I/outside-review/guard amendment history; hashes recorded, bytes
  private-only.
- `instrument-history/instrument-meta.02ce596f.json` (obsolete broad-gates key history,
  hash-verified `02ce596f…`).
- `initial-census.json` (authorized root census evidence; its recorded census commands
  also reach into `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`, a fleet-repo
  dependency, not lane-reproducible).
- `proposal-void-ledger.json` (source qualification; recorded `void_report_sha256
  99e9377d…` refers to report text inside it — no independent way to recompute that
  mapping from lane bytes).

## Reusable as-is

- `c0185da` ruler + oracle bytes and `75f671b` receipt: reuse directly; the plan's C1
  re-run command's `--oracle-sha256`/`--baseline-sha256` values are correct against
  committed bytes.
- The before receipt as candidate-comparison baseline: its full graded content is
  re-derivable, so comparing a candidate run against it does not depend on attempt-1
  custody.
- Consumer pin `872993f8…` at `197b5a4` (git blob `06322fc5`): verified two ways.

## Residual risk / gaps

- Reproduction ran on one host/session (this one); no cross-host determinism claim.
- `stdout_sha256` and `oc.log` digests in the committed receipt are path-dependent
  strings; they can never be reproduced byte-for-byte at a different scratch path — a
  closure that diffs receipts naively will see 22 field diffs; grade on values/statuses
  only, as done here.
- Attempt-2's uncommitted `verifiers/verify_harness_independent.py` edit is outside this
  audit's scope (audited state is the committed base consumer at `197b5a4`).
