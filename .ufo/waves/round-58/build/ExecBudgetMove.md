Result: DONE — `SKILL.md` § Skill-file anatomy (19 consecutive lines) moved byte-identically into the existing `corpus/knowledge/anatomy-and-compression.md` behind a one-line pointer; `SKILL.md` 600 → 582 lines, checklist 10/10 PASS before and after the move in a fleet-shaped copy.

## Deliverables

| file | content | sha256 |
|---|---|---|
| `.ufo/waves/round-58/build/ExecBudgetMove.patch` | `git diff` in the sandbox clone at freeze `3de87aad`, 65 lines, `2 files changed, 27 insertions(+), 19 deletions(-)` | `d5948bd819d0310cc5f0fee8a2d1a9bcaa436926446b62d8b5b1ed21d95c8a36` |
| moved block (19 lines), SKILL.md side `58–76` at `3de87aad` | `git show HEAD:SKILL.md \| sed -n '58,76p' \| sha256sum` | `038880d040d8c4c5f007d8bb6a5cfc5b1aa02d5df02e270f2eaaa4690fb74024` |
| moved block (19 lines), knowledge-file side `122–140` after the patch | `sed -n '122,140p' corpus/knowledge/anatomy-and-compression.md \| sha256sum` | `038880d040d8c4c5f007d8bb6a5cfc5b1aa02d5df02e270f2eaaa4690fb74024` |

- `diff <(git show HEAD:SKILL.md | sed -n '58,76p') <(sed -n '122,140p' corpus/knowledge/anatomy-and-compression.md)` → **exit 0, no output** (VERBATIM-OK).
- Files touched by the patch: `SKILL.md`, `corpus/knowledge/anatomy-and-compression.md`. No other path is in the diff.
- Nothing committed. No sandbox commit hashes are cited because none were made.

## What the patch does

1. `SKILL.md` (hunk `@@ -55,25 +55,7 @@`): deletes the 19-line `## Skill-file anatomy` section (`3de87aad` lines 58–76: heading, blank, the "Observed load order" paragraph, the 7-row `| # | Section | Function | Exemplar |` table, the "Not every file needs every section" note) and leaves exactly one line at `SKILL.md:58`:

    Skill-file anatomy (observed load order, the seven-section table, and the "not a mandatory skeleton" note) moved verbatim to `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Skill-file anatomy (round 58).

   `SKILL.md:57` and `:59` stay blank; `## Instruction surfaces — pick the file before the fix` is now `SKILL.md:60`.
2. `corpus/knowledge/anatomy-and-compression.md` (hunk `@@ -112,3 +112,29 @@`): appends a provenance section `## Moved from SKILL.md § Skill-file anatomy (round 58)` (3-line blurb naming the source revision, the 19-line count, the sha256-invariance check and the round-58 build report receipt) followed by the 19 moved lines verbatim under their original `## Skill-file anatomy` heading. The pointer's `§ Moved from SKILL.md § Skill-file anatomy (round 58)` matches that heading exactly.

Line budget after the move: `wc -l SKILL.md` → **582**; `600 - 582 = 18` lines of headroom for C1 (plan: ≤ 12).

## Why this block is eligible (the exclusion checks, run before drafting)

- `grep -rn "Skill-file anatomy\|Section | Function | Exemplar\|Observed load order" verifiers/` → **exit 1, 0 hits**. No counter reads the moved heading, table header or sentence.
- Not the gate registry: `## Gate registry` is untouched at `SKILL.md:422` after the move (was `:440` at `3de87aad`; the only change is the 18-line shift), and `verifiers/check_gate_registry.py:68` still finds `HEADING = "## Gate registry"`.
- Not a checklist: the four checklist sections are untouched — after the move `## Trigger-fidelity checklist` (`SKILL.md:211`), `## Agent-definition fidelity checklist` (`:286`), `## Dispatch-prompt fidelity checklist` (`:332`), `## Always-on constraint-file checklist (AGENTS.md-class)` (`:366`) (at `3de87aad`: `:229`, `:304`, `:350`, `:384`), i.e. exactly the sections read by `verifiers/verify_skill_checklist.py` (41 boxes still mapped, PASS), `check_agentdef_boxes.py:242`, `verify_dispatch_prompts.py:260`, `check_alwayson_boxes.py:58`.
- Not a decision table a counter reads: the counters that parse SKILL.md tables read only their own heading's first table — `check_agent_definitions.py:153`, `check_command_files.py:284`, `check_description_thresholds.py:105`, `check_explicit_invocation.py:141`, `check_plugin_manifests.py:254`; `check_overlap_levers.py:259-271` reads only `## Anti-patterns` (untouched). The moved table (`# | Section | Function | Exemplar`) is an anatomy listing, not an action-cell decision table, and no counter names it.
- Destination is an **existing** corpus file already in the coverage map (`corpus/README.md:10`), so no new tracked corpus file and no `verifiers/corpus-baseline.json` re-record (contrast `.ufo/round-22/scouts/B05.md:53` — a new corpus file trips `corpus.index.tracked_files` DRIFT until re-recorded).
- Precedents: round 57's identical idiom in the same file (`corpus/knowledge/anatomy-and-compression.md:93` `## Moved from SKILL.md § Decision tables (round 57)`), and `.ufo/round-22/scouts/B05.md:35,54` measured this exact move as prototype D (586 lines then, checklist rc 0).

## Evidence — commands, exits, output

Sandbox (bounds-compliant clone; no lane writes beyond the two report-dir files):

```
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/ExecBudgetMove
git -C /fast/scratch/hyaku/kotoba-r58/ExecBudgetMove checkout -q 3de87aad29e960c95ed35840442f424c48c29729
git log -1 --format='%H %s'
3de87aad29e960c95ed35840442f424c48c29729 round-58: pre-freeze — C1/C2 counters (targets F>=4, G>=3 after the Q45 census 6/4), gate-registry rows, census record, W0 evidence
wc -l SKILL.md  →  600
```

1. **Checklist BEFORE, clone** — `timeout 600 python3 -B verifiers/verify_skill_checklist.py` → **exit 1**:
   - `PASS trigger.line_budget: evaluated 600 — 600 lines within budget 600 (from box at line 296)`
   - FAILs: `trigger.name_directory: name 'kotoba-shokunin' != directory 'ExecBudgetMove'`; `trigger.citation_resolves: line 590: '../.ufo/reports/round-7/kotoba.md' does not resolve from /fast/scratch/hyaku/kotoba-r58/ExecBudgetMove`; `governance.citation_resolves: LOG.md:177: '../.ufo/reports/round-9/kotoba.md' does not resolve … (+20 more)`. These three are clone artifacts (directory name; `../` is not the fleet root), measured again below.
2. **Checklist AFTER, clone** — same command → **exit 1**, same three FAILs, `PASS trigger.line_budget: evaluated 582 — 582 lines within budget 600 (from box at line 278)`; `trigger.citation_resolves: evaluated 136` (was 135: the pointer adds one repo-rooted token).
3. **Fleet-shaped copy, BEFORE** — copy of the clone at `world/kotoba-shokunin` (directory name must equal the skill name for `trigger.name_directory`) with the fleet root's entries symlinked into `world/` (`for f in /home/vgpnk/Projects/shokunin/*; do ln -s "$f" world/; done` and `ln -s /home/vgpnk/Projects/shokunin/.ufo world/.ufo`; read-only links), `SKILL.md` restored from HEAD (600 lines):
   `timeout 600 python3 -B verifiers/verify_skill_checklist.py` → **exit 0, 10/10 PASS**, incl.
   `PASS trigger.name_directory: name 'kotoba-shokunin' == directory 'kotoba-shokunin'`,
   `PASS trigger.line_budget: evaluated 600 — 600 lines within budget 600 (from box at line 296)`,
   `PASS trigger.citation_resolves: evaluated 135 — 135 repo-rooted citation token(s) resolve from the repo root`,
   `PASS governance.citation_resolves: evaluated 1062 …`.
   This shows the three clone FAILs are environment artifacts, not round-58 defects.
4. **Fleet-shaped copy, AFTER** — `git apply` of `ExecBudgetMove.patch`, then the same command → **exit 0, 10/10 PASS**, incl.
   `PASS trigger.line_budget: evaluated 582 — 582 lines within budget 600 (from box at line 278)`,
   `PASS trigger.citation_resolves: evaluated 136`, `PASS governance.citation_resolves: evaluated 1062`, `checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 4 delegated, 29 unexecuted)`.
5. **Patch integrity**:
   - `git apply --check <patch>` on the pristine freeze tree (`world/kotoba-shokunin` at `3de87aad`) → **exit 0**; `git apply` → **exit 0**, giving `SKILL.md` sha256 `1c03112f2a40eddefbcf149f290a55c78994dc01480ee3bd0c41536c31c72db7` (582 lines) and `corpus/knowledge/anatomy-and-compression.md` sha256 `1213890bfdb8f1b2e3544b13ee44d97e8f2945fd47cd0992a854edec49478b34`, both **identical to the clone's edited files**.
   - `git apply --check <patch>` on base `f56f6e191762c27c1aa2af11a204db9e2ca4edec` (`SKILL.md` 598 lines) → **exit 0**; the patch is revision-tolerant across base→freeze. Restored to freeze + patch afterwards (same two sha256s).
6. **Corpus instrument, informational** — `timeout 600 python3 -B verifiers/verify_corpus_integrity.py` in the fleet-shaped copy, run once with the corpus edit and once with it reverted: both **exit 1** with byte-identical output (`diff` → exit 0):
   `corpus.index tracked=91 unindexed=1 stale=0 missing=0`, `corpus.pointers report_dead=0/62 commit_total=33 unresolvable=1`, `DRIFT corpus.index.tracked_files: observed=91 expected=81`, `DRIFT corpus.index.unindexed: observed=1 expected=0`, `DRIFT corpus.pointers.report_total: observed=62 expected=51`, `DRIFT corpus.pointers.commit_total: observed=33 expected=32`, `DRIFT corpus.pointers.commit_unresolvable: observed=1 expected=0` (the pre-existing `451a02ff` Gemini CLI commit in `corpus/lessons/round-54-verifier-spotcheck.md:147`), `4/9 checks pass`.
   The drift is pre-existing at the freeze revision and my append adds no finding: the two runs are textually identical.

## Integration notes for the L1

- Apply from the lane root: `git apply .ufo/waves/round-58/build/ExecBudgetMove.patch`. Context-anchored, no line-number dependence.
- Order vs C1: independent. C1 inserts `### Custom command files by client` after `## Instruction surfaces` (line 60 region unchanged by C1's insertions), and this hunk sits above it at old `SKILL.md:55-79`; neither rewrites the other's context. Combined size: 582 + C1 lines; C1 at ≤ 12 lands 594 ≤ 600 (18 lines of headroom, so C1 up to 18 lines still fits).
- Order vs R5 (dead lowercase `/home/vgpnk/projects/` at `SKILL.md:514-515`): this patch shifts every line after old 76 up by 18, so R5's site becomes **`SKILL.md:496-497`** once this lands. Integrate R5 by text, not by line number.
- `corpus/README.md:10` is deliberately unchanged: round 57's decision-table move into the same file also left the index row alone, and the row's basis text already describes the file as SKILL.md depth. No baseline re-record is needed (no new tracked corpus file).
- The pointer keeps a repo-rooted backticked token (`corpus/knowledge/anatomy-and-compression.md`), so `trigger.citation_resolves` covers the destination; the knowledge-file provenance heading is the pointer's `§` target.

## Risks

- A reader landing on the pointer line sees no `##` heading above it; that matches round 57's inline pointer idiom (the decision-table pointer at `SKILL.md:199` after this move, `:217` at `3de87aad`) and the section heading survives in the corpus file, but a reviewer preferring a heading-plus-pointer shell would get 1 fewer line of headroom.
- The moved lines carry exemplar citations (`wwkd L16–24`, `bailian-cli "CRITICAL …"`, `反触发表`). They were never repo-rooted backticked tokens, so no instrument loses coverage; in the corpus file they are likewise not resolved by any checker (out of corpus-integrity scope, measured unchanged).
- `corpus.index.*` drift at the freeze revision (above) is not caused by this patch; if the round's corpus gate is expected green, it needs the round's own baseline re-record, independent of this item.
- [INFERENCE] C1's final section length is not known to me (written by `KotobaR58.ScribeSkillSection`); 18 lines of headroom is the margin.

## Limits / not run

- Lane gates, self-tests, fault harness, `--fetch` counters: not run (out of scope; L1 owns post-integration gates). The four `verify_skill_checklist.py` runs (clone before/after, fleet-shaped copy before/after) plus the informational corpus-integrity pair are the only gate-class runs.
- No network access, no sources opened, no SOURCES/lesson writes — this item is budget-only.
- No tool installed or updated; no pacman/uv/npx/cargo invocation.
- Lane writes: only `.ufo/waves/round-58/build/ExecBudgetMove.patch` and this report. All other work happened in `/fast/scratch/hyaku/kotoba-r58/ExecBudgetMove` (clone + `world/` scratch copy + `.corpus-before.txt`/`.corpus-after.txt`/`.skill-after.md`).
