Result: BREAKS — one harm: the C1 entry adds an upstream Gemini CLI hash in the lane's commit-citation form, so both corpus gates gain a new zero-mode finding (`commit_unresolvable` 0 → 1) and the finding-delta gate reports `new 2`. The two-word fix leaves the C1 and C2 counters unchanged. No floor, SCORECARD score or other gate verdict was lowered; the moved bullets are verbatim and SKILL.md is 599 of 600 lines.

Seat: `KotobaR54.W2CriticNoHarm`, falsify wave, round 54 (attempt 1). Base `422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`, tip `58db81c4465b0e9b07ef2485b87d8970683afac6`.
Sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2CriticNoHarm`, checked out at each revision in turn. Scratch output is under its `.git/noharm/`, outside the worktree, so the tree-walking verifiers never saw it. `git status --porcelain --untracked-files=all` was empty before and after every run set.
Runs: 2026-10-22, 21:52Z–22:03Z. No lane file was written except this report. No installs. No model calls.

## Attack 1 — the assigned gate set at base and tip: BREAKS (one new finding)

Runner: `.git/noharm/run.sh` (each command run from the checked-out revision; `--rev` set to that revision).

| Gate (command as assigned) | base exit | tip exit | Output base → tip |
|---|---|---|---|
| `verify_skill_checklist.py` | 1 | 1 | Same FAIL/PASS set (11 checks). The 3 FAILs are clone-environment failures at both revisions (see the note under the table). `line_budget` 593 → 599 of 600. |
| `verify_corpus_integrity.py` | 1 | 1 | `6/9` → `5/9`; **new DRIFT `corpus.pointers.commit_unresolvable: observed=1 expected=0 / empty`** with site `commit_unresolvable: corpus/knowledge/skill-listing-thresholds-round54.md:43: 451a02ff`; `unindexed` resolved |
| `verify_corpus_independent.py` | 1 | 1 | `corpus.pointers.commit_unresolvable zero observed=0 PASS` → **`observed=1 DRIFT`**; `unindexed` PASS at tip |
| `check_assertion_floors.py` | 0 | 0 | byte-identical; all 12 floors equal (e.g. `surfaces observed=175 floor=175`, `checklist observed=1852 floor=1852`) |
| `check_correction_sweep.py --root .` | 0 | 0 | byte-identical: `correction sweep: 0 stale block(s)` |
| `check_substrate_pins.py` | 0 | 0 | byte-identical: `OK 3/3 pins hold` |
| `check_mcp_instructions.py --rev <rev>` | 0 | 0 | byte-identical: `mcp instructions backed 7 of 7 clients` |
| `check_overlap_levers.py --rev <rev>` | 0 | 0 | byte-identical: `overlap levers backed 7 of 7 clients` |
| `check_alwayson_boxes.py --rev <rev>` | 0 | 0 | byte-identical: `always-on boxes executed and discriminating 2 of 8` |
| `check_callee_rename.py --rev <rev>` | 0 | 0 | byte-identical: `callee-rename robust 4 of 4 fixtures` |
| `check_gate_finding_delta.py --base 422ffd10… --head 58db81c4…` | 1 | 1 | identical from both checkouts: `base drift 3, head drift 4` / `new: corpus.pointers.commit_total, corpus.pointers.commit_unresolvable` / `resolved: corpus.index.unindexed` / `finding delta: new 2, resolved 1` |

The checklist's three FAILs are the same at both revisions and come from where the clone sits, not from lane content: `trigger.name_directory` (`name 'kotoba-shokunin' != directory 'W2CriticNoHarm'`), `trigger.citation_resolves` (`'../.ufo/reports/round-7/kotoba.md'`, base line 583 → tip line 589, the same citation shifted by the SKILL.md edits), and `governance.citation_resolves` (the same `LOG.md` sites; 1018 evaluated at both). `diff` of the verdict-prefix lines of both outputs → empty ("checklist verdict set identical").

### The harm, isolated

- Site: `corpus/knowledge/skill-listing-thresholds-round54.md:43`, Gemini CLI row, reading cell: "…(no truncation at `skillLoader.ts:211` or `snippets.ts:320`, commit `451a02ff`)…". Landed in `5a097e12` (C1).
- Mechanism: `verifiers/verify_corpus_integrity.py:149`, ``COMMIT_RE = re.compile(r"(?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)`")``, reads ``commit `<hex>` `` as a lane revision and checks it with `git cat-file -e <hex>^{commit}` (docstring lines 23–28). `451a02ff` is google-gemini/gemini-cli's commit (`.ufo/waves/round-54/build/SrcGeminiCLI.md:49`). `git cat-file -t 451a02ff` → `fatal: Not a valid object name` in the sandbox clone, in the lane, and in the fleet repo.
- The lane already knew this hazard. It is the round's own mistake M45 (`corpus/lessons/round-54.md:13`: S050's upstream Zed hash had been rewritten in place "to clear the lane gate's `commit_unresolvable` reading"). The round-48 baseline note (`verifiers/corpus-baseline.json`, `notes.round48`) says upstream hashes "are written without the backticked commit-token form, since they are not lane revisions". Seat `SrcClaudeCode` hit and rephrased the same shape (`.ufo/waves/round-54/build/SrcClaudeCode.md:268-270`). This is the same class of defect, recurring in the C1 entry.
- Why wave 1 missed it: `ExecTipRuns` measured `7ad05d34` and `b38c32a0` (the latter is the round-53 evidence commit, an ancestor of base; `.ufo/waves/round-54/build/ExecTipRuns.md:5`). No wave-1 run measured the corpus gates after `5a097e12`.
- Re-recording the baseline will not clear it. `commit_unresolvable` is `"mode": "zero"` in `verifiers/corpus-baseline.json`. It can only clear by fixing the text or by changing the mode, and changing the mode would lower a floor, which is itself a harm. `commit_total` is `equal` mode at 32, and the true lane count stays 32 after the fix. Re-recording 33 at the tip would bake the upstream hash into the denominator.
- Knock-on: `verifiers/fault_injection_corpus.sh` (base exit 1, tip exit 1). At base its control world is dirty with `corpus.index.unindexed`; at tip with `corpus.pointers.commit_unresolvable`. Every must-fire row at tip carries the extra class (e.g. `fault-c | integrity | 1 | corpus.pointers.commit_unresolvable | PASS`, where base had `corpus.index.unindexed,corpus.pointers.commit_unresolvable`).

### Smallest safe correction (text for the L1; tested in scratch only)

In `corpus/knowledge/skill-listing-thresholds-round54.md:43` replace ``commit `451a02ff` `` with ``google-gemini/gemini-cli@`451a02ff` ``. This is the repo-qualified form S050's row already uses. The entry is new this round and is not `corpus/SOURCES.md`, so editing it is not an append-only breach. The L1 MAY add the recurrence to lesson M45's evidence.

Tested in a scratch worktree `.git/noharm/fixwt` at the tip plus that one edit, committed in scratch as `2721c0cc738649a22eda96f16153fdadb71f37e7` (never pushed):
- `verify_corpus_integrity.py` → `7/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.pointers.report_total`, exit 1. The two remaining findings are the expected `equal`-mode counts that the L1's baseline re-record covers.
- `verify_corpus_independent.py` → `commits candidates=37 citations=32 hex=32 quoted=5 nonhash=0 unresolvable=0`; `corpus.pointers.commit_unresolvable zero observed=0 PASS`.
- `check_gate_finding_delta.py --base 422ffd10… --head 2721c0cc…` → `base drift 3, head drift 2` / `new: none` / `resolved: corpus.index.unindexed` / `finding delta: new 0, resolved 1`, exit 0 (tip: `new 2`, exit 1).
- `check_description_thresholds.py --rev 2721c0cc…` → `description thresholds backed 7 of 7 clients`, exit 0 (unchanged; `--root .` also 7 of 7).
- `check_gate_registry.py --rev 2721c0cc…` → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0 (unchanged).
- `fault_injection_corpus.sh` → control world clean (`fault-0-control | integrity | 0 | - | PASS`); a–g PASS; only `fault-h` FAILs. `fault-h` also FAILs at base and tip, so it predates this round and is not a round-54 harm.

## Attack 2 — the remaining registry gates at base and tip: HOLDS

Runner: `.git/noharm/run_extra.sh`, with `TMPDIR` pointed at scratch. I compared outputs with timestamps stripped.

| Gate | base | tip | Output |
|---|---|---|---|
| `box_proof_case_deletion.py --rev <rev>` | 0 | 0 | same |
| `check_opencode_repin.py --rev <rev>` | 0 | 0 | same |
| `verify_surfaces.py` (run only, file untouched) | 0 | 0 | same |
| `compare_harness_independent.py` | 1 | 1 | same `agreement: 18/24`; red from live host harness state (omp catalogue/cache counts) |
| `verify_harness_claims.py` | 1 | 1 | same 7 DRIFT host-state findings (`omp.offered.skills observed=11 expected=7`, …) |
| `verify_dispatch_prompts.py` | 1 | 1 | same `dispatch.04` FAIL on fleet dispatch files outside the lane |
| `fault_injection_corpus.sh` | 1 | 1 | see Attack 1 knock-on |

Self-tests, base → tip: every self-test that exited 0 at base exits 0 at tip (all 16 run that existed at base; for example `verify_skill_checklist`, `check_assertion_floors`, `verify_surfaces`, `verify_alwayson`, `check_sibling_census`). The four gates that gained a self-test in `b55550b9` go from exit 2 (no such flag) to exit 0:
- `check_alwayson_boxes`: `self-test PASS: counted box exit 0; missing delegate exit 1`.
- `check_callee_rename`: `0 failure(s) over 2 assertions`.
- `box_proof_case_deletion`: `0 failure(s) over 10 assertions`.
- `check_opencode_repin`: `0 failure(s) over 2 assertions`.

The strength of those self-tests is `W2MutNewSelfTests`'s seat, not this one.

`--rev` went from required to optional in three gates. Called with no arguments, the bare command still refuses at tip, so no silent pass:
- `box_proof_case_deletion.py` → `error: the following arguments are required: --rev`, exit 2.
- `check_alwayson_boxes.py` → `error: --rev is required`, exit 2.
- `check_opencode_repin.py` → `error: --rev is required unless --self-test is selected`, exit 2.

All three exit 2 at base as well.

## Attack 3 — floors, scores, frozen files: HOLDS

- `git diff --quiet 422ffd10 58db81c4 -- SCORECARD.md verifiers/floors-registry.json verifiers/corpus-baseline.json verifiers/checklist-baseline.json verifiers/surfaces-baseline.json verifiers/verify_surfaces.py` → exit 0 ("unchanged"). No SCORECARD score was lowered, no floor was lowered, and `verify_surfaces.py` is untouched (drift rule).
- Counters frozen: `git diff --stat e3371548… 58db81c4… -- verifiers/check_gate_registry.py verifiers/check_description_thresholds.py` → empty. The lesson's "now fails a `gate` row with `none` self-test" (`corpus/lessons/round-54.md:15`) describes the frozen counter's own rule (`check_gate_registry.py:29-31,157-159`), not a widening.
- Counters at base: `backed 0 of 7`, exit 1; `conformant 0 of 21 … phantom 0`, exit 1. At tip: `backed 7 of 7`, exit 0; `conformant 24 of 24 … phantom 0`, exit 0.
- `verifiers/baseline.json`: one line changed, the `opencode_round53_note` text only (routed defect 6); no pin value. `check_substrate_pins.py` is byte-identical at both revisions.
- `corpus/SOURCES.md`: one row changed in place. S046 differs only in cell 10 (`used-by`), from `corpus/knowledge/alwayson-rule-files-round53.md` to `…, corpus/lessons/round-54.md`. Contract rule 2 allows `used-by` to change in place. Rows S053–S064 are appended.
- Lines deleted outside SKILL.md across the round (`git diff --numstat 422ffd10 58db81c4 -- . ':!.ufo'`): S046's `used-by` cell; the baseline note; and in three verifiers, only the argparse `--rev required=True` lines and the `main()` signatures, all reworked for `--self-test`.

## Attack 4 — moved verifier bullets (`7ad05d34`) and the line budget: HOLDS

- `git show 422ffd10:SKILL.md | sed -n 532,574p` → 43 lines. That block occurs as one contiguous verbatim substring of `verifiers/README.md` at both `7ad05d34` and the tip (Python `in` test → `True` at both; README is 50 lines).
- None of the 43 moved non-empty lines remains in SKILL.md at `7ad05d34` or at the tip (exact-line match count 0).
- `git diff --numstat 422ffd10 7ad05d34 -- SKILL.md` → `2 43`. The 2 added lines are only the pointer bullet to `verifiers/README.md`.
- `git diff --numstat 7ad05d34 58db81c4 -- SKILL.md` → `47 0`, additions only. No other SKILL.md text was removed in the round.
- `wc -l SKILL.md` at the tip → 599, and `verify_skill_checklist.py` reports `trigger.line_budget: … 599 lines within budget 600`. One line of headroom: any integration edit to SKILL.md beyond a net +1 line would break `line_budget`. The proposed fix does not touch SKILL.md.

## Expected drift, not a harm

At base `verify_corpus_integrity.py` is already red (`tracked_files 79/78`, `unindexed 1`, `report_total 51/49`). At tip, after the fix above, it would be red only on `tracked_files 81/78` and `report_total 51/49`. Both are `equal`-mode counts that the L1's re-record of `verifiers/corpus-baseline.json` is expected to cover. For that re-record, `commit_total` should be recorded as 32 after the fix, not 33.

## Commands of record

- `bash .git/noharm/run.sh base 422ffd10…` / `… tip 58db81c4…` → summaries in `.git/noharm/{base,tip}/_summary.tsv` (name, exit, UTC start, command).
- `bash .git/noharm/run_extra.sh base …` / `… tip …` → `.git/noharm/{base,tip}-extra/_summary.tsv`.
- Fix test: `.git/noharm/fixwt` (scratch `git worktree` at the tip, plus one edit, commit `2721c0cc`); fault-injection output in `.git/noharm/fix_fault.out`.
