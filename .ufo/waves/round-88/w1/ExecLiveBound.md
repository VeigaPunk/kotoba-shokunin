# ExecLiveBound — round-88 C1 v2 root counter (report)

Counter: `verifiers/check_omp_root_semantics_v2.py`, sha256 `b6412808f904a492937763ef995dfb751b48af454194f26fb3a30b1a6905c427`
(new, untracked in the worktree; L1 commits). Marker: `.ufo/waves/round-88/w1/C1_READY` (same sha256).
Receipts: `.ufo/waves/round-88/w1/ExecLiveBound/receipts.txt`.

## Results (final bytes)

- `--self-test`: `0 failure(s) over 69 assertions`; second line `forgery-class worlds rejected 7 of 7`.
- `--rev 4df1e8005016c75390a5e06b209462df58c95918`: `omp root semantics grounded 12 of 12`,
  `forgeries rejected 4 of 4`, `forgery-class worlds rejected 7 of 7`, S1–S5 PASS, `exit=0`.
  - M (r87 classes, reader-column mutations): `w_cross_row7` 11/12, `w_subdir_row9` 10/12,
    `w_misattr_row12` 9/12, `w_renderline_row6` 8/12 — all REJECTED.
  - K (disclosed): `w_both_ledgers` 11/12, `w_module_mislabel` 11/12, `w_home_escape` 9/12 — all REJECTED.
- Frozen-table digests (in the counter header and printed on every run):
  binding sets `98ed070b…cb0`, token pins `2f720772…1a0`, reader pins `fa0e8cc3…572`,
  module offsets `c96cda89…d44`, PATTERN_SET `f6aa379f…11f`.
- Pre-score/ELF_MAP digest: `21e3c518df2eafc17a233ad4232b7b0a852db47f9a9be522acf32ab938444897` (A1.8).

## Honest disclosures (read before ruling)

1. **Kill-rule exposure (needs L1 ruling).** The first `--rev` candidate score ran BEFORE a counter-defect
   fix. Its binary conjunct used `bytes in mmap`, which is always False on an mmap, so all 12 rows failed
   (`0 of 12`, forgeries "rejected" for the wrong reason). The pre-fix reading is kept verbatim in the
   receipts. After it I changed: the conjunct to `blob.find(...) >= 0`; added `conj5/mmap` self-test arms
   (the bytes-only self-test had masked the bug); added `os`/`tempfile` to the S5 hygiene allowlist; added the
   digest header comment. No predicate sentence, pin, token set, reader pin, module offset or target changed.
   Plan § C1 says a change after the first candidate score kills C1. I am not deciding that.
2. **Binding tokens are measured, not weakened.** A2.1 is applied as ruled. Five rows' tokens also occur
   outside their chunk (`eh` 3797 total / 6 in-chunk; `".codex"` 7/1; `".github"` 5/1; `we()` 88/7; `R.path` 64/4).
   Per row, the receipt prints total, in-chunk and out-chunk counts.
3. **Pins are a table** (A2.1 disclosed bound): lookup-oracle bound not closed by this counter; rests on
   ReviewerC1's independent reimplementation.
4. **Upstream check** for conjunct 4 is complete: ScoutUpstream's `agents.ts` v18.15.0 (sha256
   `976360027cee…2e`, blob `2e41428b…44`) lines 140–155 carry the same loop as the ELF.
5. **Floors registry side effect (not mine to fix).** I added `omp_root_semantics_v2` (floor 68) and set
   `instrument_total` 17→18 in `verifiers/floors-registry.json` (JSON parses, 18 = 18). The guard
   `verifiers/check_assertion_floors.py` keeps its own in-file tables; `registry_anchor_drift` will report
   `row vanish: omp_root_semantics_v2` until those tables carry the row. I did not edit that file (not named).
   Owner of the guard must add the row.
6. **A1.4 condition 2 ruling** applied as A2.1 (pinned-in-chunk), with out-of-chunk counts disclosed.

## Files written

- `verifiers/check_omp_root_semantics_v2.py` (new).
- `verifiers/floors-registry.json` (one row added; `instrument_total` 17→18).
- `.ufo/waves/round-88/w1/ExecLiveBound/receipts.txt`, `.ufo/waves/round-88/w1/ExecLiveBound.md`,
  `.ufo/waves/round-88/w1/C1_READY`.
- Scratch: `/fast/scratch/hyaku/kotoba-r88/ExecLiveBound` (removed at yield).

## Not touched

The r87 counter and its ledgers, the ELF (read-only mmap only, never exec'd), git (no writes), the other seats' files.
No tools installed; no subagents dispatched.

## Checks for the main agent to run

- `python3 -B verifiers/check_omp_root_semantics_v2.py --self-test` (expect `0 failure(s) over 69 assertions`).
- `python3 -B verifiers/check_omp_root_semantics_v2.py --rev <landing rev>` (expect `12 of 12`, forgeries `4 of 4`, exit 0).
- `python3 -B verifiers/check_assertion_floors.py` (expect the new `row vanish` drift until the guard tables are updated).
