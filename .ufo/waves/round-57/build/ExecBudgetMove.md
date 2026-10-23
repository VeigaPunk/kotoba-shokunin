Result: DONE — moved `## Decision tables — when to use one` verbatim out of `SKILL.md` (598→584 lines, 14 freed) into `corpus/knowledge/anatomy-and-compression.md` under `## Moved from SKILL.md § Decision tables (round 57)` with a pointer at the old site; moved bytes sha256-identical before and after (`8a71375c…`), all seven named gates measured before and after with unchanged verdicts.

Seat: KotobaR57.ExecBudgetMove (leaf executor). Work revision `01312a77e36317feb6e961aba77841ddab1225ca`; sandbox
`/fast/scratch/hyaku/kotoba-r57/ExecBudgetMove/kotoba-shokunin`; sandbox commit `b4d9e4d` (/fast/scratch/hyaku/kotoba-r57/ExecBudgetMove/kotoba-shokunin) on top of the work revision. No lane file was edited (this report and the patch are the only lane writes).

## Move (verbatim)

- Source block at base: `SKILL.md:203–217` — heading `## Decision tables — when to use one`, the 7-line `| Situation | Table? | Evidence |` table, and the 5-line `Table rule:` paragraph. 15 lines, 898 bytes.
- sha256 of the moved bytes at base (`sed -n '203,217p' SKILL.md | sha256sum`):
  `8a71375c1c5ef13e2fcb42f681d8f9eb8bb240b5b96d480407fb9557f83378e1`
- sha256 of the same 15 lines at the destination (`corpus/knowledge/anatomy-and-compression.md:100–114`):
  `8a71375c1c5ef13e2fcb42f681d8f9eb8bb240b5b96d480407fb9557f83378e1` — identical, 15 lines / 898 bytes.
- Destination layout (`anatomy-and-compression.md`, 91→114 lines): blank line, `## Moved from SKILL.md § Decision tables (round 57)` (:93), a 4-line provenance paragraph (:95–98, names `01312a77` and base lines 203–217), then the block verbatim (:100–114) including its original `## Decision tables — when to use one` heading, so name searches still find the title inside the moved copy.
- Pointer left at `SKILL.md:203` (one line, then blank, then `## Compression rules` at :205), round-56 idiom (cf. `SKILL.md:171` → `corpus/knowledge/render-mechanism-round7.md` § Moved from SKILL.md § Frontmatter craft (round 56)):
  ``Decision-table shape (situation → table or plain steps) and the action-cell rule — every row needs an action cell (command, route, named fallback, or verdict), need not be the last column: `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Decision tables (round 57), verbatim.``
- `wc -l`: `SKILL.md` 598 → 584 (`-14`, exactly the block minus the one-line pointer and its blank); `anatomy-and-compression.md` 91 → 114 (`+23`).
- Patch deliverable: `.ufo/waves/round-57/build/ExecBudgetMove.patch`, 58 lines, sha256 `54e13a5b75107d58062e7e6141d60debaeccaf9f450a981512ace3a66009b8a9`; `git diff 01312a77e36317feb6e961aba77841ddab1225ca` from the sandbox commit, prefixes `c/`…`w/` as the lane's diff config emits them. Replayed on a fresh clone of the lane at the work revision: `git apply --check -p1` → exit 0; after applying, `wc -l SKILL.md` = 584 and the destination block still hashes `8a71375c…`.

## Gates — before / after, same sandbox clone, same command

Before = work revision `01312a7`, clean tree. After = sandbox commit `b4d9e4d` (move applied). All commands run from the clone root with `python3 -B`; outputs kept under `/fast/scratch/hyaku/kotoba-r57/ExecBudgetMove/{pre4,post}/`.

| # | Gate | before exit | after exit | after output |
|---|------|-------------|------------|--------------|
| 1 | `python3 -B verifiers/verify_skill_checklist.py` | 0 | 0 | `PASS trigger.line_budget: evaluated 584 — 584 lines within budget 600 (from box at line 282)`; `PASS trigger.no_placeholder: evaluated 526`; `PASS trigger.citation_resolves: evaluated 129 — 129 repo-rooted citation token(s) resolve` (before: 598 / 538 / 128) |
| 2 | `python3 -B verifiers/verify_skill_checklist.py --self-test` | 0 | 0 | `0 failure(s) over 1852 assertions` |
| 3 | `python3 -B verifiers/verify_corpus_integrity.py` | 1 | 1 | byte-identical output after path normalization (`diff` exit 0) |
| 4 | `python3 -B verifiers/verify_corpus_independent.py` | 1 | 1 | byte-identical output (`diff` exit 0) |
| 5 | `timeout 900 bash verifiers/fault_injection_corpus.sh` | 1 | 1 | all 20 verdict rows identical after normalizing `head=`/`worlds=` (`diff` exit 0) |
| 6 | `python3 -B verifiers/check_assertion_floors.py` | 0 | 0 | 13 PASS lines, identical (`diff` exit 0); `corpus_independent observed=99 floor=93`, `checklist observed=1852 floor=1852` |
| 7 | `python3 -B verifiers/check_correction_sweep.py --root .` | 0 | 0 | `correction sweep: 0 stale block(s)` both runs |

Gate 1 detail — the only output that changed is the intended one: `trigger.line_budget` now evaluates 584, `trigger.no_placeholder` scans 10 fewer lines (526 vs 538, no markers either way), and `trigger.citation_resolves` counts one more token (129 vs 128) because the pointer adds a repo-rooted citation, which resolves. Every box still PASSes; no checklist box text was touched (41 boxes, `PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 4 delegated, 29 unexecuted)`).

Gates 3/4 drift is pre-existing at the work revision, not caused by the move — identical observed values both sides:
`DRIFT corpus.index.tracked_files: observed=88 expected=81`, `DRIFT corpus.index.unindexed: observed=1` (`corpus/lessons/round-56-verifier-spotcheck.md`), `DRIFT corpus.pointers.report_total: observed=58 expected=51`, `DRIFT corpus.pointers.commit_total: observed=33 expected=32`, `DRIFT corpus.pointers.commit_unresolvable: observed=1` (`corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff`); `4/9 checks pass`. **No baseline re-record** (`corpus-baseline.json`) was made or is needed: the counts that would feed it are unchanged by the move, and `checked=58` / `commit candidates=38` / `index_tokens` are the same before and after. Re-recording would have silently absorbed the round-56 drift, which is not this seat's to bless.

Gate 5 drift is likewise pre-existing: `fault-0-control | integrity | 1 | corpus.index.unindexed,corpus.pointers.commit_unresolvable | FAIL-control-dirty`, and because the control world is already dirty, `fault-f` cannot meet its exit-0-under-`--no-baseline` assertion (`fault-f | integrity | 1 | … | FAIL`). `verdict: FAILURES PRESENT` on both sides; every must-fire row (a, b, c, d1, d2, e) still PASS, `fault-g` `PASS(no new drift vs control)`, `fault-h` `PASS(context: quoted=2, control=1, checked=58 unchanged)`.

## Environment (so the receipts reproduce)

The lane's parent is the fleet root; the clone's parent is not. Read-only symlinks under `/fast/scratch/hyaku/kotoba-r57/ExecBudgetMove/` reproduce the exact paths the lane resolves: `.ufo -> /home/vgpnk/Projects/shokunin/.ufo`, plus `PROTOCOL.md`, `AXES.md`, `MISSION.md`, `SCORECARD.md`, `kasegi-shokunin`. Without them `trigger.citation_resolves` and `governance.citation_resolves` fail for clone geometry only. The clone directory is named `kotoba-shokunin` because `trigger.name_directory` compares `name:` with the directory name (`FAIL … name 'kotoba-shokunin' != directory 'repo'` was observed when cloned as `repo`, then eliminated). No lane, jj or fleet state was read-write touched; the two `/tmp`-world fault-injection runs cleaned themselves up.

## Retained risks / notes for the integrator

1. **`trigger.08` referent (silent, pre-existing class).** The frozen box at `SKILL.md:267–268` says "Every decision-table row contains an action cell (see the table rule above — need not be the last column)". Its text hash is unchanged and no gate fires, but "above" now lands on the pointer line instead of the paragraph. The pointer was written to carry the rule itself ("every row needs an action cell (command, route, named fallback, or verdict), need not be the last column"), so the box remains resolvable from where it sits. This is the round-22 B09 D2 defect class; I did not edit the box (41 box texts are out of scope).
2. **Corpus README row not changed.** `corpus/README.md:10` already indexes `knowledge/anatomy-and-compression.md` (and names the round-15 absorption). The round-56 move of § Frontmatter craft did not add a README note either, so this follows the current idiom; if the integrator wants the index to name the round-57 move, that is a one-sentence append to the same row and changes no corpus count.
3. **Inner heading retained.** The moved block keeps `## Decision tables — when to use one` verbatim under the mandated `## Moved from SKILL.md § Decision tables (round 57)` wrapper, so both the round-56 idiom (wrapper heading) and title search (inner heading) keep working; no `## Decision tables` heading remains in `SKILL.md`.
4. **C2 untouched.** No file under `verifiers/` was read-modified; the info-less fence handling in `verifiers/verify_skill_checklist.py` was not touched, sketched, or commented on. `git status --porcelain` in the sandbox after the commit: 0 entries.
5. Tooling: no install or upgrade was needed or attempted (no pacman transaction was opened; host-wide pause respected).
