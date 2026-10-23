# NoHarmGates — round-58 falsify wave: no-harm attack on `46b4a706`

Result: HOLDS — all ten commands of `build/noharm-base.txt` reproduce at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` with the same exits (nine 0, `check_plugin_manifests` 1 as the documented pre-existing red) and no count worse; two low-severity text drifts are found outside the ten (a stale `SKILL.md:217` pointer in `SHONEN.md`, and the round-12 anatomy recipe now printing 0), and one transient corpus-index red at this rev is measured green at the lane tip.

## What was run, where, when

- Sandbox clone named exactly `kotoba-shokunin`: `/fast/scratch/hyaku/kotoba-r58/NoHarmGates/kotoba-shokunin`, `git rev-parse HEAD` → `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`. No sandbox commit was made; the clone was checked out to the tip once for one read-only instrument run and returned to `46b4a70`.
- Fleet-root mirror, per `.ufo/waves/round-58/build/ExecNoHarmPremeasure.md` § Calibration 1: every top-level entry of `/home/vgpnk/Projects/shokunin` — **including the dot entries `.devin .git .gitignore .jj .omp .ruff_cache .scratch .tower .ufo`** — symlinked read-only into the clone's parent `/fast/scratch/hyaku/kotoba-r58/NoHarmGates` (the clone itself excluded, so `trigger.name_directory` sees `kotoba-shokunin`). The dot entries matter: see Calibration 1.
- Input receipt `build/noharm-base.txt` sha256 `1fa927ab45a7ccb4d176253cce17a25f59127228ca53f6dd1d0ca240f2c75658` — matches the digest its author reports.
- Every command capped `timeout 900`; timestamps from `date -u` in the same shell: `Fri 23 Oct 2026 08:26:13 AM UTC` (batch 1) … `08:26:28 AM UTC` (batch 2) … `08:26:57 AM UTC` → `08:28:13 AM UTC` (floors, 75 s) … `08:30:25 AM UTC` (corpus instrument). Logs retained at `/fast/scratch/hyaku/kotoba-r58/NoHarmGates/kotoba-shokunin/.noharm/*.log`; `git status --porcelain` in the clone after all runs shows only `?? .noharm/` — the counters wrote nothing into the tree.
- Nothing was installed or upgraded; no pacman, uv, npx or cargo call. No lane file was read-write opened; the only lane write is this report.

## Before / after table

Before = `build/noharm-base.txt` at base `f56f6e191762c27c1aa2af11a204db9e2ca4edec`. After = my run at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`, same flags (`--fetch` on #1–#3, `--base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` on #8).

| # | command (cwd = sandbox clone) | before exit | after exit | before summary | after summary | verdict |
|---|---|---|---|---|---|---|
| 1 | `check_agent_definitions.py --rev <r> --fetch` | 0 | 0 | live 7 of 7; new ground 3 | live 7 of 7; new ground 3 | same |
| 2 | `check_plugin_manifests.py --rev <r> --fetch` | 1 | 1 | live 4 of 4; new ground 4; rejects VS Code, Copilot CLI, opencode | live 4 of 4; new ground 4; **same three rejects, same wording** | same (pre-existing red, TARGET 5) |
| 3 | `check_explicit_invocation.py --rev <r> --fetch` | 0 | 0 | live 5 of 5; new ground 4 | live 5 of 5; new ground 4; same two unbacked rows (VS Code, Gemini CLI) | same |
| 4 | `check_description_thresholds.py --rev <r>` | 0 | 0 | backed 7 of 7 clients | backed 7 of 7 clients | same |
| 5 | `check_mcp_instructions.py --rev <r>` | 0 | 0 | backed 7 of 7 clients | backed 7 of 7 clients | same |
| 6 | `check_gate_registry.py --rev <r>` | 0 | 0 | rows conformant **30 of 30**; phantom 0 | rows conformant **32 of 32**; phantom 0 | same conformance; universe 30→32 (two new counters) |
| 7 | `check_correction_sweep.py --rev <r>` | 0 | 0 | 0 stale block(s) | 0 stale block(s) | same |
| 8 | `check_sources_append_only.py --base 422ffd10… --rev <r>` | 0 | 0 | **5** commits scanned, 0 protected-cell changes | **6** commits scanned, 0 protected-cell changes | same verdict; window end moved |
| 9 | `verify_skill_checklist.py` (mirror) | 0 | 0 | 11 PASS; `line_budget` **598**/600 (box at line 296); citations 131; placeholders scanned 537 | 11 PASS; `line_budget` **596**/600 (box at line 292); citations 137; placeholders scanned 535 | same; file 2 lines shorter |
| 10 | `check_assertion_floors.py` | 0 | 0 | 13 PASS; observed 10/152/99/175/1852/62/123/330/165/56/68/55/89 | 13 PASS; **identical observed vector** | same |

`verify_skill_checklist.py --json` after: `pass 11, fail 0, na 0, exit_code 0`.

Informational, outside the ten but inside the attacked layer:

| command | exit | output |
|---|---|---|
| `check_command_files.py --rev 46b4a70 --fetch` | 0 | `custom command files found on the live page 6 of 6; new ground 4`; counter sha256 `aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c` — **byte-identical to the L1 receipt** `C1-measure.txt`, per-row `BACKED`/`held-at-base` lines identical, `reject Copilot CLI: SKILL.md command token ':456' is not well-formed` identical, predicate label identical |
| `check_plugin_manifests.py` | 1 | its first line `counter sha256 7cefb997…` matches `.ufo/waves/round-58/noharm-tip.txt` |

The lane tip's own receipt `.ufo/waves/round-58/noharm-tip.txt` (measured at the same `46b4a70`) lists the same nine-green/one-red pattern plus `check_sweep_mutants` 11/11 & 5/5 exit 0; my independent run agrees on every line the two share.

### Worse-scan

No exit and no count in the ten got worse. Counts that moved, read in the only direction that matters:

- **gate registry 30 → 32**: the universe grew by `verifiers/check_command_files.py` and `verifiers/check_sweep_mutants.py`; both fully conformant, `phantom 0`. Conformance (the invariant) is 100 % before and after. Universe check: `git ls-tree <rev> verifiers/` (non-recursive, trailing slash) → **30 at base, 32 at rev**, equal to the row count at each rev.
- **sources append-only 5 → 6 commits scanned**: the `--rev` window end moved forward one commit; protected-cell changes stay **0**.
- **placeholders scanned 537 → 535** and **line budget 598 → 596**: the placeholder scan set is the file's lines (`537 − 535 = 598 − 596 = 2`).
- **citations 131 → 137**: +6 repo-rooted tokens from the pointer line and the C1 section; all resolve (`PASS`, exit 0).
- `check_plugin_manifests` remains 4 of 4 with the same three reject lines — no row lost, no new reject, no ground lost.

## Calibration findings

1. **The mirror must include dot entries; the raw parent fails.** My first mirror pass linked only non-dot top-level entries. `verify_skill_checklist.py` then exited 1 with exactly two FAILs — `trigger.citation_resolves: evaluated 137 — line 586: '../.ufo/reports/round-7/kotoba.md' does not resolve …` and `governance.citation_resolves … LOG.md:177, :255, :779, :974 … (+7 more)`. Adding `.ufo` (and the rest of `/home/vgpnk/Projects/shokunin/.[!.]*`) to the parent gave exit 0, 11 PASS. This reproduces the premeasure's Calibration 1 in a different shape: their raw clone also failed `trigger.name_directory` because the directory was the seat name; mine passed that (correct name) and failed only on the missing `../.ufo` hop. Both are location artifacts, never lane state. Exact recipe used:
   `for p in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.[!.]*; do b=$(basename "$p"); [ "$b" = kotoba-shokunin ] || ln -sfn "$p" <parent>/$b; done`
2. **Gate-registry universe is non-recursive — do not miscount it.** A recursive count (`git ls-tree -r … -- verifiers | grep -cE '\.(py|sh)$'`) gives **33** at this rev because of `verifiers/fixtures/checklist/delegated-py-suffix/probe.py`, a self-test fixture. The counter's `Tree.universe()` (`verifiers/check_gate_registry.py:118-129`) runs `git ls-tree -z <rev> verifiers/` and keeps blobs directly under `verifiers/` → 32, which is what "32 of 32" means. A reviewer using the recursive count would read a correct row set as a missing registration.
3. **The three `--fetch` counters do hit the network per run.** Each of the three has exactly one `urllib.request.urlopen` call site (`verifiers/check_agent_definitions.py:764`, and the same v2 family in `check_plugin_manifests.py` and `check_explicit_invocation.py`), and none references an on-disk HTTP cache (`grep -l '\.httpcache\|FETCH_CACHE\|CACHE_DIR'` → 0 files; the only `cache` hit is `git update-index --cacheinfo` inside the plugin counter's self-test). Each run's per-row `found=yes` and the 7-of-7 / 4-of-4 / 5-of-5 totals therefore require live HTTP 2xx at run time. Three pages' values can drift with the vendors; the premeasure's re-measure-at-base rule applies if a post-integration run diverges. [INFERENCE] the wall time (7 s for three fetch counters) is consistent with small fast pages, not with a local cache — the code path has none.
4. **#9 and #10 are working-directory/parent-sensitive and must be run in the lane or a properly mirrored clone.** They take no `--rev`; #10 shells out to the other verifiers in the same tree. Running either in a seat-named clone or an unmirrored parent produces FAILs that are not lane state.
5. **`check_assertion_floors` floors are hardcoded** (`check_assertion_floors.py:150`); the observed vector equals base element for element, so no floor was quietly lowered. `floors_guard observed=165 floor=150` and `corpus_independent 99/93` carry the same margins as base.

## Findings for the L1 to integrate (text only; I edited nothing)

**F1 (LOW) — `SHONEN.md:6` now carries a stale `SKILL.md` line pointer.**
The budget move deletes 18 lines above it and the C1 section adds 14, so the decision-table pointer shifted `:217 → :213`:
- base `f56f6e19`, `sed -n '217p'`: `Decision-table shape (situation → table or plain steps) and the action-cell rule …  § Moved from SKILL.md § Decision tables (round 57), verbatim.`
- `46b4a70`, `sed -n '217p'`: `Six rules with their evidence: 'corpus/knowledge/anatomy-and-compression.md'`; the pointer is at `:213` (`grep -n 'Decision tables' SKILL.md` → 213).
- `SHONEN.md:6` still says "(pointer `SKILL.md:217`)" at both revs (`diff` of that line base vs rev: empty — the wave did not touch it).
No counter covers line numbers in `SHONEN.md`; the SKILL.md preamble's "cited line numbers are points-in-time" covers SKILL.md, not its readers. Proposed text: in `SHONEN.md:6`, `pointer `SKILL.md:217`` → `pointer `SKILL.md:213``, or drop the number and cite "the inline pointer under § Frontmatter craft" so a further insertion does not re-drift it.

**F2 (LOW / record time-stamp) — the round-12 anatomy recipe now prints 0 instead of 9.**
`corpus/knowledge/claim-census-round12.md:102` (row F:6) records `awk '/^## Skill-file anatomy/,/^## Instruction surfaces/' SKILL.md | grep -c '^\|'` → `9` with verdict `AGREES`. Measured: **9 at base `f56f6e19`, 0 at `46b4a70`** (the heading left SKILL.md). The file's preamble defuses this as a live falsification — "the rows below keep the *pre-repair* values they measured, so several of them then read STALE — that is the record, not an error" — but unlike those rows this one is not annotated, and its command now returns an empty result rather than an error, the silent-flip class round 22 flagged (`.ufo/round-22/scouts/B08.md` D6 predicted this exact `9 → 0`). No instrument covers it: `check_correction_sweep` reports 0 stale blocks, and `verify_corpus_integrity` at `46b4a70` and at the tip prints the same pointer block as the freeze-rev runs `ExecBudgetMove.md` recorded with and without the move (that instrument never reads this row). Proposed text if the L1 wants it closed: append to that row "(heading moved to `corpus/knowledge/anatomy-and-compression.md` in round 58; recipe reads 0)".
The same class was checked across the live tree and no other wave-caused staleness was found: `PROVINCE.md:51,53` pin `SKILL.md:10-12` at `f3046466`; `corpus/knowledge/explicit-invocation-round55.md:56` pins `f0e5de82`; `considerthese/*` cite lines ≤ 17 (above the edit points); `corpus/knowledge/frontmatter-rule-authorities-round48.md:49` cites `SKILL.md:246`, which was already a different line at base (`- [ ] 'name' matches the directory / invocation surface.`), so it is round-48 staleness, not this wave's.

**F3 (observation) — corpus index is transiently redder at this rev, green at the tip.**
`verify_corpus_integrity.py` at `46b4a70`: **exit 1**, `corpus.index tracked=93 unindexed=3` — `corpus/knowledge/command-files-round58.md`, `corpus/lessons/round-58.md`, `corpus/lessons/round-57-verifier-spotcheck.md`. At lane tip `8e52f06` (sandbox checkout, same clone): **unindexed=0**, `tracked=93 … (111 FILE-column patterns over 92 md files)`; the remaining DRIFT lines are the pre-existing set `ExecBudgetMove.md` documented at the freeze rev (`corpus.index.tracked_files`, `corpus.pointers.report_total 62/51`, `commit_total 33/32`, `commit_unresolvable 1`) and both runs exit 1 for them. So the wave's own index edge is closed by the tip's three `corpus/README.md` rows; integrating `46b4a70` without them leaves this instrument at 3 unindexed. This instrument is **not** one of the ten and its red is not wave-caused in kind.

**F4 (positive) — the budget move is byte-verbatim at the integrated rev.** `git show 3de87aad:SKILL.md | sed -n '58,76p' | sha256sum` = `038880d040d8c4c5f007d8bb6a5cfc5b1aa02d5df02e270f2eaaa4690fb74024` = `sed -n '122,140p' corpus/knowledge/anatomy-and-compression.md | sha256sum`; `diff` of the two streams exits 0. The destination heading `## Moved from SKILL.md § Skill-file anatomy (round 58)` exists at `:116`, matching the pointer at `SKILL.md:58`. Line arithmetic: 600 (freeze) − 18 (move) + 14 (C1 section, `SKILL.md:107-120`) = **596** — so 4 lines of headroom remain against the 600 budget, not the 18 the move freed. Any later addition before `:600` has only 4 lines to spend.

**F5 (positive) — the C1 layer's own measurement reproduces exactly.** `check_command_files.py` at `46b4a70` prints `6 of 6; new ground 4`, exit 0, with counter sha256 `aae12d36…` identical to `C1-measure.txt`, and the same predicate label `C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) [TARGET=4, NEW_TARGET=3]`. The C1 predicate is independent of the ten and was not mixed into them.

## Risks and blockers

- Live-page drift is the only nondeterminism in #1–#3; a post-integration run that differs should be re-measured at base before attributing the delta to the wave.
- The mirror reproduces ancestor resolution by symlinking the fleet root; it does not snapshot it. `governance.citation_resolves` (1062 tokens) and `trigger.citation_resolves` depend on fleet-root content at run time.
- F1 and F2 are text the L1 may integrate or decline; neither is a counter regression, and neither changes any of the ten exits.
- **#10 will need a re-run if the in-flight floors patch lands.** At report time the lane working tree shows `M verifiers/check_assertion_floors.py`, `M verifiers/floors-registry.json` (the `ExecFloorsSweep` repair, not mine). My #10 vector is measured at the committed `46b4a70`; a floors change in the integrated rev makes that row a different measurement, so re-run #10 there and compare against the vector recorded in `noharm-base.txt`, not against this table alone.
- No blocker. The ten-command claim is measured, not inferred; nothing in this item contends for a lane write beyond this file.

## Files changed

- `.ufo/waves/round-58/falsify/NoHarmGates.md` (this report; new).
- Sandbox only: `/fast/scratch/hyaku/kotoba-r58/NoHarmGates/kotoba-shokunin/.noharm/*.log` (10 baseline logs + checklist JSON + `command_files.log` + two corpus-integrity logs) and the read-only fleet-root symlinks in `/fast/scratch/hyaku/kotoba-r58/NoHarmGates/`. No sandbox commit; nothing pushed.
