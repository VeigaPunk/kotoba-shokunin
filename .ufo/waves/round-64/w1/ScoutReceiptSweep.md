# ScoutReceiptSweep — M95 path@rev census

Seat: `kotoba-r64.ScoutReceiptSweep`. Question: every artifact-path citation of the form `` `path` @ `rev` `` or `at `rev`` in the enumerated lane paperwork, tested with `git cat-file -e <rev>:<path>`, classed as M95 (receipt/control cited at a rev that does not yet contain it) versus content that exists at the cited rev. Then: does the planned LOG check-2 line (committing revs of the two r63 controls + base `35d44b4b`) cover every ABSENT instance?

Scope tested: `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-6*.md` (12 files: `round-6.md`, `round-6-aggregator-audit.md`, `round-60` through `round-63` lessons and spot-checks). Fleet `.ufo/reports` not in the lane; not opened. No production file edited. No tool installed.

Base at dispatch `078eec4` is the tree these citations were read from. Add commits below are `git log -1 --diff-filter=A --format=%H -- <path>` from HEAD (the plan's command). `--all` is wrong here: jj keep-refs duplicate the add and the newest `--all` hash for `C1-do-nothing-v31.txt` was `5b0f393b`, not the master add `8c4cefa8e1b7`.

## Answer

**Strict M95 instances: 15** (10 unique path@rev pairs). **Check 2 as planned covers 2 of those 15** — the two routed r63 controls cited at base `35d44b4b`. It does not cover the other 13. A LOG suffix that names only `8c4cefa`, `cbbee56` and `35d44b4b` leaves eight other receipt/control pairs still cited at a pre-commit rev. Covering the class means more lines (one per uncovered pair: cited rev + committing rev). Keeping the frozen bound (spot-check defect 2 only) is consistent with the plan's own bound sentence, but then the other 13 are surviving debt, not closed by C2.

The two covered instances are not both in LOG. LOG cites `C2-before-r62tip.txt` at `35d44b4b` (line 2582). SCORECARD cites `C1-do-nothing-v31.txt` at `35d44b4b` (line 373). Check 2 still names both committing revs, so one LOG suffix covers both routed sites as a correction record. It does not edit SCORECARD, and it does not name the other pairs.

## Strict M95 table

Every row: `git cat-file -e <rev>:<path>` exit 128, and `git merge-base --is-ancestor <rev> <add>` exit 0 (cited rev is a strict ancestor of the HEAD add, so the file is not in that commit). Class = receipt/control cited at the rev the run was *against*, committed later.

| file:line | path | cited rev | cat-file | HEAD add (`log -1 --diff-filter=A`) | check 2 covers? |
|---|---|---|---|---|---|
| `LOG.md:2303` | `.ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt` | `78ee57e` | ABSENT (128) | `f2f9ee1d88bc` | no |
| `LOG.md:2465` | `.ufo/waves/round-55/C2-measure-e966cd59.txt` | `e966cd59` | ABSENT (128) | `722e474ad242` | no |
| `LOG.md:2493` | `.ufo/waves/round-57/C1-measure.txt` | `ac22ca87` | ABSENT (128) | `07c33d73ddce` | no |
| `LOG.md:2509` | `.ufo/waves/round-58/C1-measure.txt` | `46b4a706` | ABSENT (128) | `8e52f064f215` | no |
| `LOG.md:2510` | `.ufo/waves/round-58/noharm-tip.txt` | `46b4a706` | ABSENT (128) | `8e52f064f215` | no |
| `LOG.md:2512` | `.ufo/waves/round-58/noharm-tip.txt` | `46b4a706` | ABSENT (128) | `8e52f064f215` | no |
| `LOG.md:2548` | `.ufo/waves/round-62/C1-absorb-measure.txt` | `3e7aed9b` | ABSENT (128) | `f9ab0812a574` | no |
| `LOG.md:2582` | `.ufo/waves/round-63/controls/C2-before-r62tip.txt` | `35d44b4b` | ABSENT (128) | `cbbee56e9a35` | yes — names this add + base 35d44b4b |
| `SCORECARD.md:28` | `.ufo/waves/round-56/C1-measure.txt` | `c22fdd39` | ABSENT (128) | `f897d18ae9ec` | no |
| `SCORECARD.md:28` | `.ufo/waves/round-57/C1-measure.txt` | `ac22ca87` | ABSENT (128) | `07c33d73ddce` | no |
| `SCORECARD.md:28` | `.ufo/waves/round-58/C1-measure.txt` | `46b4a706` | ABSENT (128) | `8e52f064f215` | no |
| `SCORECARD.md:28` | `.ufo/waves/round-59/C1-measure.txt` | `c63ccc68` | ABSENT (128) | `d64d945b3435` | no |
| `SCORECARD.md:36` | `.ufo/waves/round-62/C1-absorb-measure.txt` | `3e7aed9b` | ABSENT (128) | `f9ab0812a574` | no |
| `SCORECARD.md:369` | `.ufo/waves/round-62/C1-absorb-measure.txt` | `3e7aed9b` | ABSENT (128) | `f9ab0812a574` | no |
| `SCORECARD.md:373` | `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` | `35d44b4b` | ABSENT (128) | `8c4cefa8e1b7` | yes — names this add + base 35d44b4b |

Unique pairs check 2 does **not** name (8), with the committing rev a corrected line would have to carry:

| path | wrongly cited at | committing rev on master | sites |
|---|---|---|---|
| `.ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt` | `78ee57e` | `f2f9ee1d88bc` | LOG:2303 |
| `.ufo/waves/round-55/C2-measure-e966cd59.txt` | `e966cd59` | `722e474ad242` | LOG:2465 |
| `.ufo/waves/round-56/C1-measure.txt` | `c22fdd39` | `f897d18ae9ec` | SCORECARD:28 |
| `.ufo/waves/round-57/C1-measure.txt` | `ac22ca87` | `07c33d73ddce` | LOG:2493, SCORECARD:28 |
| `.ufo/waves/round-58/C1-measure.txt` | `46b4a706` | `8e52f064f215` | LOG:2509, SCORECARD:28 |
| `.ufo/waves/round-58/noharm-tip.txt` | `46b4a706` | `8e52f064f215` | LOG:2510, LOG:2512 |
| `.ufo/waves/round-59/C1-measure.txt` | `c63ccc68` | `d64d945b3435` | SCORECARD:28 |
| `.ufo/waves/round-62/C1-absorb-measure.txt` | `3e7aed9b` | `f9ab0812a574` | LOG:2548, SCORECARD:36, SCORECARD:369 |

The r62 absorb file is also cited correctly, at its add: `round-62-verifier-spotcheck.md:72` `` `…/C1-absorb-measure.txt` at `f9ab0812` ``, cat-file exit 0. The three SCORECARD/LOG sites that pin it at `3e7aed9b` (the `receipt_rev` inside the file) are the M95 mis-cite; the spot-check site is not.

## What was counted

Shapes extracted (method, plus the no-paren form `` `path` at `rev` ``):

- `` `path` @ `rev` ``
- `at `rev` (`…path…`)` and `@ `rev` (`…path…`)`, including `at receipt rev `rev` (`
- `` `rev` (`…path…`)`` when the paren holds a path and an earlier rule did not already take it
- `rev:path` / `git show rev:path`
- extra pass: `` `path` at `rev` `` with no parenthesis

A path token has a slash or a file extension, no spaces, no URL, no ellipsis. Relative paths (`controls/C1-base.txt`) were also tested at every HEAD path with that suffix; a citation is EXIST if the round-context path exists at the rev (round-56's `controls/C1-base.txt` at `0f58a469` exists as `.ufo/waves/round-56/controls/C1-base.txt`, exit 0; same for round-57 at `ee50d8fa`).

Not in the strict 15 (disclosed, not hidden):

| file:line | why excluded | cat-file if forced |
|---|---|---|
| `LOG.md:2582` `receipts/C2-before-rerun.txt` beside `35d44b4b` | second clause after `;` ("re-run … in `receipts/C2-before-rerun.txt`"). Not the object of `at `35d44b4b``. Full path `.ufo/waves/round-63/receipts/C2-before-rerun.txt` | ABSENT at `35d44b4b` (128); HEAD add `849a546effbc`; exists there (the spot-check's `git show 849a546e:…` form) |
| `round-61-verifier-spotcheck.md:115` | table cells differ: artifact column is the path; observed column is `` `base-exit=1` @ `f3246d14` ``. Not `path @ rev`. | full path ABSENT at `f3246d14` (128); HEAD add `7827628a939b` |
| `SCORECARD.md:138` bare `check_description_thresholds.py` / `check_gate_registry.py` joined to `@ `422ffd10`` | the `@` binds `` `0 of 7` `` / `` `0 of 21` ``, not the script name | not a path claim |
| `LOG.md:2306` `snapshot2/` at `` `ccf41c23…` `` | prefix is not an object (`git cat-file -t ccf41c23` → `fatal: Not a valid object name`, exit 128). Same for `LOG.md:282` `SKILL.md` @ `143fe473` and `LOG.md:2350` `after-configured-root.json` @ `01af33a6` | REV_UNRESOLVED |
| `LOG.md:1213` `` `19/19` at `d49dfa5` `` | not a path | skipped |

`C1-g9-measure.txt` at `849a546effbc081e44f2dcd5c49d1055074b7ebb` (SCORECARD:373, paren after the measured-rev) is **EXIST** (exit 0). That is not this absence class. The lesson's M95 item (i) is different: the bytes inside that commit name an unshipped sha `55230880…`. Absence-at-rev and stale-bytes-inside-a-present-file are both called M95 in the paperwork; only the absence class is what check 2's rev-naming fixes.

`MutW2V32` §11 at `75370a5` (LOG:2588, lesson row t) is a seat name, not a repo path. Resolved `.ufo/waves/round-63/w2/MutW2V32.md` at `75370a5` is EXIST (exit 0). Not M95.

Same-sentence juxtaposition the three shapes do not attribute, already covered as a pair: `corpus/lessons/round-63.md` names `C2-before-r62tip.txt` in the parenthesis of the before-state whose command carries `--rev 35d44b4b…`. Same ABSENT pair as LOG:2582.

## Check 2 against the plan

Plan check 2 (`plans/round-64.md`) requires an appended LOG line at `<rev>` to name both committing revs (≥7 hex) and base `35d44b4b`. Expected adds, re-measured here and matching the plan:

- `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` → `8c4cefa8e1b7` (plan `8c4cefa`)
- `.ufo/waves/round-63/controls/C2-before-r62tip.txt` → `cbbee56e9a35` (plan `cbbee56`)

Positive controls (the citation that does not misstate bytes): `git cat-file -e 8c4cefa:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` exit 0; `git cat-file -e cbbee56:.ufo/waves/round-63/controls/C2-before-r62tip.txt` exit 0. The spot-check already uses that form (`round-63-verifier-spotcheck.md:49` and `:83`).

So the planned line is necessary and, for defect 2, sufficient. It is not sufficient for the census. Of 15 strict ABSENT receipt citations, 13 name a different path or a different rev. A counter that only greps the LOG suffix for `8c4cefa`, `cbbee56` and `35d44b4b` will go green while SCORECARD:28 still cites four measure-receipts at the rev they were run against, and while LOG still does the same for rounds 46, 55, 57, 58 and 62.

[INFERENCE] Widening check 2 to those eight pairs would change the frozen predicate's defect-2 scope (the plan binds "these four routed defects of one spot-check"). The empirical ground for that bound decision is the table above, not a guess that the two r63 controls are the only ABSENT sites.

## Full instance table

92 rows. Status is `git cat-file -e` on the cited path, or on the unique/round-context full path when the prose used a suffix. `REV_UNRESOLVED` means the hex is not a commit object.

| file:line | path | rev | status | class |
|---|---|---|---|---|
| `LOG.md:282` | `SKILL.md` | `143fe473` | REV_UNRESOLVED | rev does not resolve (not a commit object) |
| `LOG.md:1452` | `verifiers/compare_harness_independent.py` | `b1be35f` | EXIST | content exists at cited rev |
| `LOG.md:1681` | `verifiers/baseline.json` | `6fbbff5` | EXIST | content exists at cited rev |
| `LOG.md:1705` | `verifiers/compare_harness_independent.py` | `6fbbff5` | EXIST | content exists at cited rev |
| `LOG.md:1767` | `verifiers/compare_harness_independent.py` | `032f47b` | EXIST | content exists at cited rev |
| `LOG.md:1767` | `verifiers/compare_harness_independent.py` | `6881ce3` | EXIST | content exists at cited rev |
| `LOG.md:1789` | `verifiers/compare_harness_independent.py` | `032f47bd` | EXIST | content exists at cited rev |
| `LOG.md:1842` | `verifiers/compare_harness_independent.py` | `032f47bd` | EXIST | content exists at cited rev |
| `LOG.md:1874` | `verifiers/compare_harness_independent.py` | `032f47bd` | EXIST | content exists at cited rev |
| `LOG.md:1978` | `verifiers/compare_harness_independent.py` | `032f47bd13fdff0cd2ccea5f902df9690ad09376` | EXIST | content exists at cited rev |
| `LOG.md:2015` | `verifiers/compare_harness_independent.py` | `055d3b9` | EXIST | content exists at cited rev |
| `LOG.md:2054` | `verifiers/compare_harness_independent.py` | `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` | EXIST | content exists at cited rev |
| `LOG.md:2066` | `verifiers/compare_harness_independent.py` | `055d3b9` | EXIST | content exists at cited rev |
| `LOG.md:2255` | `.ufo/round-46/scouts/R2.md` | `ccf41c23` | REV_UNRESOLVED | rev does not resolve (not a commit object) |
| `LOG.md:2303` | `.ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt` | `78ee57e` | ABSENT | M95 pre-commit receipt |
| `LOG.md:2330` | `considerthese/` | `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` | EXIST | content exists at cited rev |
| `LOG.md:2350` | `.ufo/round-48/verification/after-configured-root.json` | `01af33a6` | REV_UNRESOLVED | rev does not resolve (not a commit object) |
| `LOG.md:2432` | `plans/round-52.md` | `4c003a4b` | EXIST | content exists at cited rev |
| `LOG.md:2462` | `.ufo/waves/round-55/controls/` | `a10240c0` | EXIST | receipt exists at cited rev |
| `LOG.md:2462` | `plans/round-55.md` | `a10240c0` | EXIST | content exists at cited rev |
| `LOG.md:2465` | `.ufo/waves/round-55/C2-measure-e966cd59.txt` | `e966cd59` | ABSENT | M95 pre-commit receipt |
| `LOG.md:2480` | `controls/C1-base.txt` | `0f58a469` | EXIST | receipt exists at cited rev |
| `LOG.md:2480` | `controls/C2-base.txt` | `0f58a469` | EXIST | receipt exists at cited rev |
| `LOG.md:2480` | `plans/round-56.md` | `0f58a469` | EXIST | content exists at cited rev |
| `LOG.md:2480` | `verifiers/check_agent_definitions.py` | `0f58a469` | EXIST | content exists at cited rev |
| `LOG.md:2480` | `verifiers/check_agentdef_boxes.py` | `0f58a469` | EXIST | content exists at cited rev |
| `LOG.md:2490` | `check_infoless_fences.py` | `ee50d8fa` | EXIST | content exists at cited rev |
| `LOG.md:2490` | `check_plugin_manifests.py` | `ee50d8fa` | EXIST | content exists at cited rev |
| `LOG.md:2490` | `controls/C1-base.txt` | `ee50d8fa` | EXIST | receipt exists at cited rev |
| `LOG.md:2490` | `controls/C2-base.txt` | `ee50d8fa` | EXIST | receipt exists at cited rev |
| `LOG.md:2493` | `.ufo/waves/round-57/C1-measure.txt` | `ac22ca87` | ABSENT | M95 pre-commit receipt |
| `LOG.md:2506` | `check_command_files.py` | `3de87aad` | EXIST | content exists at cited rev |
| `LOG.md:2506` | `check_sweep_mutants.py` | `3de87aad` | EXIST | content exists at cited rev |
| `LOG.md:2509` | `.ufo/waves/round-58/C1-measure.txt` | `46b4a706` | ABSENT | M95 pre-commit receipt |
| `LOG.md:2510` | `.ufo/waves/round-58/noharm-tip.txt` | `46b4a706` | ABSENT | M95 pre-commit receipt |
| `LOG.md:2512` | `.ufo/waves/round-58/noharm-tip.txt` | `46b4a706` | ABSENT | M95 pre-commit receipt |
| `LOG.md:2512` | `build/noharm-base.txt` | `46b4a706` | EXIST | receipt exists at cited rev |
| `LOG.md:2520` | `corpus/knowledge/anatomy-and-compression.md` | `c63ccc68` | EXIST | content exists at cited rev |
| `LOG.md:2547` | `verifiers/check_seat_counts.py` | `9f03dcd7` | EXIST | content exists at cited rev |
| `LOG.md:2548` | `.ufo/waves/round-62/C1-absorb-measure.txt` | `3e7aed9b` | ABSENT | M95 pre-commit receipt |
| `LOG.md:2582` | `.ufo/waves/round-63/controls/C2-before-r62tip.txt` | `35d44b4b` | ABSENT | M95 pre-commit receipt |
| `LOG.md:2582` | `receipts/C2-before-rerun.txt` | `35d44b4b` | ABSENT | paren-later cooccupant — not the at-rev subject; full path also ABSENT (add 849a546effbc) |
| `SCORECARD.md:28` | `.ufo/waves/round-56/C1-measure.txt` | `c22fdd39` | ABSENT | M95 pre-commit receipt |
| `SCORECARD.md:28` | `.ufo/waves/round-57/C1-measure.txt` | `ac22ca87` | ABSENT | M95 pre-commit receipt |
| `SCORECARD.md:28` | `.ufo/waves/round-58/C1-measure.txt` | `46b4a706` | ABSENT | M95 pre-commit receipt |
| `SCORECARD.md:28` | `.ufo/waves/round-59/C1-measure.txt` | `c63ccc68` | ABSENT | M95 pre-commit receipt |
| `SCORECARD.md:31` | `verifiers/fixtures/dispatch-prompts/manifest.json` | `542f515` | EXIST | content exists at cited rev |
| `SCORECARD.md:31` | `verifiers/fixtures/dispatch-prompts/manifest.json` | `f3046466` | EXIST | content exists at cited rev |
| `SCORECARD.md:34` | `plans/round-49.md` | `f054b8e` | EXIST | content exists at cited rev |
| `SCORECARD.md:36` | `.ufo/waves/round-62/C1-absorb-measure.txt` | `3e7aed9b` | ABSENT | M95 pre-commit receipt |
| `SCORECARD.md:82` | `.ufo/round-40/claims.json` | `b1be35f9522f21c0c5b39879358a011806ab9200` | EXIST | content exists at cited rev |
| `SCORECARD.md:138` | `SKILL.md` | `422ffd10` | EXIST | content exists at cited rev |
| `SCORECARD.md:138` | `SKILL.md` | `bf65974c` | EXIST | content exists at cited rev |
| `SCORECARD.md:138` | `check_description_thresholds.py` | `422ffd10` | n/a | false-join (result `0 of N` @ rev beside a script name) — not a path@rev claim |
| `SCORECARD.md:138` | `check_description_thresholds.py` | `5a097e12` | EXIST | content exists at cited rev |
| `SCORECARD.md:138` | `check_gate_registry.py` | `422ffd10` | n/a | false-join (result `0 of N` @ rev beside a script name) — not a path@rev claim |
| `SCORECARD.md:138` | `check_gate_registry.py` | `bf65974c` | EXIST | content exists at cited rev |
| `SCORECARD.md:142` | `corpus/knowledge/explicit-invocation-round55.md` | `96155796` | EXIST | content exists at cited rev |
| `SCORECARD.md:190` | `corpus/knowledge/claim-scope-audit-round9.md` | `e997d45` | EXIST | content exists at cited rev |
| `SCORECARD.md:193` | `corpus/knowledge/cold-run-round11.md` | `4dd7753` | EXIST | content exists at cited rev |
| `SCORECARD.md:193` | `corpus/knowledge/corpus-integrity-round11.md` | `4dd7753` | EXIST | content exists at cited rev |
| `SCORECARD.md:195` | `corpus/knowledge/opencode-extraction-round14.md` | `29c17be` | EXIST | content exists at cited rev |
| `SCORECARD.md:195` | `verifiers/verify_surfaces.py` | `29c17be` | EXIST | content exists at cited rev |
| `SCORECARD.md:369` | `.ufo/waves/round-62/C1-absorb-measure.txt` | `3e7aed9b` | ABSENT | M95 pre-commit receipt |
| `SCORECARD.md:373` | `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` | `35d44b4b` | ABSENT | M95 pre-commit receipt |
| `SCORECARD.md:373` | `.ufo/waves/round-63/receipts/C1-g9-measure.txt` | `849a546effbc081e44f2dcd5c49d1055074b7ebb` | EXIST | receipt exists at cited rev |
| `corpus/lessons/round-6-aggregator-audit.md:39` | `SKILL.md` | `8c300ad` | EXIST | content exists at cited rev |
| `corpus/lessons/round-60-verifier-spotcheck.md:42` | `verifiers/check_scoped_rules.py` | `79cf2638` | EXIST | content exists at cited rev |
| `corpus/lessons/round-60-verifier-spotcheck.md:48` | `SKILL.md` | `31092dc6` | EXIST | content exists at cited rev |
| `corpus/lessons/round-60.md:58` | `plans/round-60.md` | `b1cd64bb45eee744c4ec93be8631f1eddb28fddd` | EXIST | content exists at cited rev |
| `corpus/lessons/round-60.md:58` | `plans/round-60.md` | `bfe8cc2b` | EXIST | content exists at cited rev |
| `corpus/lessons/round-61-verifier-spotcheck.md:60` | `corpus/knowledge/writing-revision-calibration-round61.md` | `a745411c` | EXIST | content exists at cited rev |
| `corpus/lessons/round-61-verifier-spotcheck.md:63` | `verifiers/check_routed_repairs.py` | `7827628a` | EXIST | content exists at cited rev |
| `corpus/lessons/round-61-verifier-spotcheck.md:97` | `verifiers/check_scoped_rules.py` | `6a7f722e` | EXIST | content exists at cited rev |
| `corpus/lessons/round-61-verifier-spotcheck.md:100` | `.ufo/waves/round-61/receipts/C1-worlds.txt` | `a745411c` | EXIST | receipt exists at cited rev |
| `corpus/lessons/round-61-verifier-spotcheck.md:103` | `corpus/SOURCES.md` | `f3246d14` | EXIST | content exists at cited rev |
| `corpus/lessons/round-61-verifier-spotcheck.md:115` | `.ufo/waves/round-61/controls/C2-base.txt` | `f3246d14` | ABSENT | weak-join (base-exit @ rev; path is another table cell) — not strict M95 |
| `corpus/lessons/round-61-verifier-spotcheck.md:118` | `plans/round-60.md` | `a745411c` | EXIST | content exists at cited rev |
| `corpus/lessons/round-62-verifier-spotcheck.md:32` | `.ufo/waves/round-62/C2-successor-measure.txt` | `e6da78bb` | EXIST | receipt exists at cited rev (prose abbreviates the path; root-basename cat-file is ABSENT, full path EXIST) |
| `corpus/lessons/round-62-verifier-spotcheck.md:33` | `.ufo/waves/round-62/w1/ScribeEntry62.md` | `3e7aed9b` | EXIST | content exists at cited rev |
| `corpus/lessons/round-62-verifier-spotcheck.md:72` | `.ufo/waves/round-62/C1-absorb-measure.txt` | `f9ab0812` | EXIST | receipt exists at cited rev (this is the committing rev) |
| `corpus/lessons/round-62-verifier-spotcheck.md:76` | `verifiers/check_erratum_absorption.py` | `e53b6e5c` | EXIST | content exists at cited rev |
| `corpus/lessons/round-62-verifier-spotcheck.md:95` | `.ufo/waves/round-62/C2-successor-measure.txt` | `e424f2a4` | EXIST | receipt exists at cited rev |
| `corpus/lessons/round-63-verifier-spotcheck.md:40` | `plans/round-63.md` | `8c4cefa` | EXIST | content exists at cited rev |
| `corpus/lessons/round-63-verifier-spotcheck.md:45` | `verifiers/check_scoped_rules_v32.py` | `849a546e` | EXIST | content exists at cited rev |
| `corpus/lessons/round-63-verifier-spotcheck.md:49` | `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` | `8c4cefa` | EXIST | receipt exists at cited rev |
| `corpus/lessons/round-63-verifier-spotcheck.md:53` | `.ufo/waves/round-63/receipts/C1-g9-measure.txt` | `2ba4547` | EXIST | receipt exists at cited rev |
| `corpus/lessons/round-63-verifier-spotcheck.md:83` | `.ufo/waves/round-63/controls/C2-before-r62tip.txt` | `cbbee56` | EXIST | receipt exists at cited rev |
| `corpus/lessons/round-63-verifier-spotcheck.md:93` | `verifiers/check_r63_routed_repairs.py` | `849a546e` | EXIST | content exists at cited rev |
| `corpus/lessons/round-63-verifier-spotcheck.md:104` | `corpus/lessons/round-62-verifier-spotcheck.md` | `35d44b4b` | EXIST | content exists at cited rev |
| `corpus/lessons/round-63-verifier-spotcheck.md:169` | `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` | `8c4cefa` | EXIST | receipt exists at cited rev ("was committed at"; full path EXIST) |
| `corpus/lessons/round-63-verifier-spotcheck.md:170` | `.ufo/waves/round-63/controls/C2-before-r62tip.txt` | `cbbee56` | EXIST | receipt exists at cited rev (basename in prose; full path EXIST — this sentence names the committing rev) |

## Evidence (exit codes)

Commands run from this seat against `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. `cat-file -e` prints nothing; the exit is the result. `merge-base --is-ancestor A B` exits 0 when A is an ancestor of B (including equality; none of these cited revs equal the add).

```
$ git cat-file -t 35d44b4b
commit
$ git rev-parse --verify 35d44b4b^{commit}
35d44b4b4dcdda234b5dbff7af37e432fec55f05

# ABSENT at the cited rev; cited rev is an ancestor of the HEAD add
78ee57e:.ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt          cat-file=128  ancestor_of f2f9ee1d88bc=0
e966cd59:.ufo/waves/round-55/C2-measure-e966cd59.txt                        cat-file=128  ancestor_of 722e474ad242=0
c22fdd39:.ufo/waves/round-56/C1-measure.txt                                 cat-file=128  ancestor_of f897d18ae9ec=0
ac22ca87:.ufo/waves/round-57/C1-measure.txt                                 cat-file=128  ancestor_of 07c33d73ddce=0
46b4a706:.ufo/waves/round-58/C1-measure.txt                                 cat-file=128  ancestor_of 8e52f064f215=0
46b4a706:.ufo/waves/round-58/noharm-tip.txt                                 cat-file=128  ancestor_of 8e52f064f215=0
c63ccc68:.ufo/waves/round-59/C1-measure.txt                                 cat-file=128  ancestor_of d64d945b3435=0
3e7aed9b:.ufo/waves/round-62/C1-absorb-measure.txt                          cat-file=128  ancestor_of f9ab0812a574=0
35d44b4b:.ufo/waves/round-63/controls/C2-before-r62tip.txt                  cat-file=128  ancestor_of cbbee56e9a35=0
35d44b4b:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt                 cat-file=128  ancestor_of 8c4cefa8e1b7=0
35d44b4b:.ufo/waves/round-63/receipts/C2-before-rerun.txt                   cat-file=128  ancestor_of 849a546effbc=0
f3246d14:.ufo/waves/round-61/controls/C2-base.txt                           cat-file=128  ancestor_of 7827628a939b=0

# EXIST at the committing rev (the citation that does not misstate bytes)
8c4cefa:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt                  cat-file=0
cbbee56:.ufo/waves/round-63/controls/C2-before-r62tip.txt                   cat-file=0
f9ab0812:.ufo/waves/round-62/C1-absorb-measure.txt                          cat-file=0
e6da78bb:.ufo/waves/round-62/C2-successor-measure.txt                       cat-file=0
e424f2a4:.ufo/waves/round-62/C2-successor-measure.txt                       cat-file=0
849a546effbc081e44f2dcd5c49d1055074b7ebb:.ufo/waves/round-63/receipts/C1-g9-measure.txt  cat-file=0
75370a5:.ufo/waves/round-63/w2/MutW2V32.md                                  cat-file=0

# rev prefix is not an object
$ git cat-file -t ccf41c23    → fatal: Not a valid object name ccf41c23   (exit 128)
$ git cat-file -t 143fe473    → fatal: Not a valid object name 143fe473   (exit 128)
$ git cat-file -t 01af33a6    → fatal: Not a valid object name 01af33a6   (exit 128)

# HEAD add, one path per invocation (a multi-path log -1 returns only the newest)
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-63/controls/C2-before-r62tip.txt
cbbee56e9a3589b0b46736ad36f1b77701def80e
$ git log -1 --diff-filter=A --format=%H -- .ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt
f2f9ee1d88bc42d80fb96075db0fc3b43fb8a321
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-55/C2-measure-e966cd59.txt
722e474ad24291e530bb58bab0ea6f2f69924624
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-56/C1-measure.txt
f897d18ae9eca90da3a8f0fc46a9ea0d5ecb6b54
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-57/C1-measure.txt
07c33d73ddce769d9cea2846a6313164401b5478
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-58/C1-measure.txt
8e52f064f21580dff368b50a2a2d304ecccaaea9
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-58/noharm-tip.txt
8e52f064f21580dff368b50a2a2d304ecccaaea9
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-59/C1-measure.txt
d64d945b3435e2532203c505ad64ecf5d91b780e
$ git log -1 --diff-filter=A --format=%H -- .ufo/waves/round-62/C1-absorb-measure.txt
f9ab0812a574c369aa5cb94616e6ddffd1c5202b
```

Tables above use the first 12 hex of these. `git cat-file` and `git merge-base --is-ancestor` accepted each prefix. The two routed adds match the plan's `8c4cefa` and `cbbee56`.

## Claims

- Supports C2 check 2's expected adds: `8c4cefa` for `C1-do-nothing-v31.txt`, `cbbee56` for `C2-before-r62tip.txt`, both absent at `35d44b4b`, both present at those adds.
- Falsifies the assumption that those two sites are the only M95 absences in lane paperwork. They are 2 of 15 strict instances.
- Does not falsify the plan's bound sentence if C2 stays limited to the four routed defects. It does say the LOG block needs more lines to close the class the spot-check named ("the M95 citation class"), because that class recurs in LOG and SCORECARD for rounds 46 and 55–59 and 62.

## Unknowns

- `ccf41c23…`, `143fe473`, `01af33a6` do not resolve. A longer hash may exist in the prose past the ellipsis; not recovered here.
- Whether the L1 widens check 2 is a bound decision. This census does not edit the counter.
- Fleet report text was not opened (out of scope). The spot-check already quotes the report's `@ `35d44b4b`` pair; the lane copies of that pair are the LOG and SCORECARD rows above.

## Tools

None installed. Census used system `git` and `python3`.

