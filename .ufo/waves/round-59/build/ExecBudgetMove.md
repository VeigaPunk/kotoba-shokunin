Result: DONE — 28-line verbatim move out of `SKILL.md` § Sources into `corpus/knowledge/anatomy-and-compression.md` plus a 4-line pointer leaves `SKILL.md` at **573** lines (patch state) and **586** with the 12-line hook-files section inserted after § Custom command files by client; `verify_skill_checklist.py` is exit 0 (11 PASS) in all three states, and `verify_corpus_integrity.py` returns the same pre-existing 5 DRIFTs before and after.

Seat: `KotobaR59.ExecBudgetMove`. Freeze `67b68e0f9a0c48e5aa5ced63e6117cfca69da491` (`SKILL.md` 597 lines, budget 600). No sandbox commit was made; all work is worktree-only. No tool was installed or upgraded.

## 1. What the patch does (two files, no placeholder)

- `SKILL.md` § Sources, bullets 2–15 (lines 482–509 at the freeze, 14 bullets, 28 lines: wwkd … `~/.config/opencode/skills/ufo/SKILL.md`) are removed and replaced by a 4-line pointer bullet that names the destination section by its exact heading.
- `corpus/knowledge/anatomy-and-compression.md` gains, at the end, a `## Moved from SKILL.md § Sources — production skill files (round 59)` heading, a 5-line provenance paragraph (rev, line range, line count, block sha256, receipt path) and a `### Production skill files studied` heading followed by the block, byte-for-byte.
- No file was added to `corpus/`: a new knowledge file would move `corpus.index.tracked_files` once committed and `corpus.index.unindexed` immediately (the coverage map in `corpus/README.md` has no row for it). The target is the existing anatomy entry whose `## Observed size distribution` table already names the same production skills, so the depth lands where its reader already is.
- The 12-line `### Hook files by client` placeholder was applied **only to measure the budget** and is **not** in the patch.

## 2. Moved block, both sides

| side | location | lines | sha256 |
|---|---|---|---|
| before | `SKILL.md` 482–509 at `67b68e0f` | 28 | `9d74c44e2167800809efd93aae526f39f0523f090e1dfb865e6d184ffcb9a3c8` |
| after | `corpus/knowledge/anatomy-and-compression.md` 152–179 | 28 | `9d74c44e2167800809efd93aae526f39f0523f090e1dfb865e6d184ffcb9a3c8` |

```
$ sed -n '482,509p' SKILL.md > moved-block.txt            # pristine clone at 67b68e0f
$ sha256sum moved-block.txt
9d74c44e2167800809efd93aae526f39f0523f090e1dfb865e6d184ffcb9a3c8  moved-block.txt
$ sed -n '152,179p' corpus/knowledge/anatomy-and-compression.md > moved-block-after.txt
$ sha256sum moved-block-after.txt
9d74c44e2167800809efd93aae526f39f0523f090e1dfb865e6d184ffcb9a3c8  moved-block-after.txt
$ cmp moved-block.txt moved-block-after.txt && echo CMP-IDENTICAL
CMP-IDENTICAL
```

The extracted range includes each line's terminating newline (`sed` prints the last line's newline), so the comparison is byte-exact over 28 lines / 1683 bytes on both sides (`wc -c` → 1683 and 1683).

## 3. Patch

Delivered at `.ufo/waves/round-59/build/ExecBudgetMove.patch` (lane-relative; full path `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/build/ExecBudgetMove.patch`).

```
$ sha256sum .ufo/waves/round-59/build/ExecBudgetMove.patch
169802fa87e3be5f7b74eb7c9b720b3985c2f4306548bb86ca7a0c9445594d94  …/build/ExecBudgetMove.patch
$ wc -l .ufo/waves/round-59/build/ExecBudgetMove.patch
90
$ git diff --stat                      # in the sandbox clone
 SKILL.md                                    | 32 +++--------------------
 corpus/knowledge/anatomy-and-compression.md | 39 +++++++++++++++++++++++++++++
 2 files changed, 43 insertions(+), 28 deletions(-)
```

`SKILL.md` = 4 insertions / 28 deletions; the knowledge file = 39 insertions (1 blank, 1 heading, 1 blank, 5 provenance lines, 1 blank, 1 heading, 1 blank, 28 block lines).

Apply proof, on a fresh clone checked out at the freeze:

```
$ git clone -q …/kotoba-shokunin applytest2 && git -C applytest2 checkout -q 67b68e0f…
$ cd applytest2 && git apply --check …/ExecBudgetMove.patch ; echo apply_check_exit=$?
apply_check_exit=0
$ git apply …/ExecBudgetMove.patch
$ wc -l SKILL.md
573 SKILL.md
$ sed -n '152,179p' corpus/knowledge/anatomy-and-compression.md | sha256sum
9d74c44e2167800809efd93aae526f39f0523f090e1dfb865e6d184ffcb9a3c8  -
$ diff -q SKILL.md <sandbox SKILL.md> && echo SKILL-IDENTICAL
SKILL-IDENTICAL
```

The patch is emitted with standard `a/`/`b/` prefixes (`git diff --src-prefix=a/ --dst-prefix=b/`); the lane's jj-colocated git config otherwise writes `i/`/`w/`, which `git apply` also accepts but which is not the house form. `git apply`/`git am` in the lane is the L1's call; the patch is relative to `67b68e0f`.

## 4. Gates — measured before and after

Run in the sandbox mirror at `/fast/scratch/hyaku/kotoba-r59/ExecBudgetMove/world/kotoba-shokunin` (clone at `67b68e0f`, directory named `kotoba-shokunin`, siblings `AXES.md`, `MISSION.md`, `PROTOCOL.md`, `SCORECARD.md`, `kasegi-shokunin/`, `.ufo` symlinked to the fleet root so the file's `../` citations resolve as they do in the lane). Each command capped with `timeout 600`.

| state | `verify_skill_checklist.py --json` | `verify_corpus_integrity.py --json` |
|---|---|---|
| A: freeze, no edit | exit 0 — 11 PASS, 0 FAIL (`trigger.line_budget`: 597) | exit 1 — 5 DRIFT / 4 PASS (identical rows to C) |
| B: patch state (573 lines) | exit 0 — 11 PASS, 0 FAIL (`trigger.line_budget`: 573; `trigger.citation_resolves`: 140 tokens; `governance.citation_resolves`: 1074 tokens) | 5 DRIFT / 4 PASS (same rows) |
| C: patch + 12-line section + 1 blank (586 lines) | exit 0 — 11 PASS, 0 FAIL (`trigger.line_budget`: 586; `trigger.no_placeholder`: 522 scanned lines) | 5 DRIFT / 4 PASS (same rows) |

### A (freeze) — checklist, exit 0

```
{'exit_code': 0, 'fail': 0, 'na': 0, 'pass': 11}
PASS checklist.box_map_complete | 41 boxes mapped (8 executed, 4 delegated, 29 unexecuted); delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2; delegated verifiers/verify_alwayson.py: --box-proof exit 0: boxes proven 2
PASS trigger.frontmatter_parses | frontmatter parses: name='kotoba-shokunin', description 1019 chars
PASS trigger.name_directory | name 'kotoba-shokunin' == directory 'kotoba-shokunin'
PASS trigger.literal_trigger_string | description carries literal 'Triggers:'
PASS trigger.anti_trigger_clause | exclusion marker 'Anti-triggers' present (vocabulary test, not semantics: …)
PASS trigger.no_xml_tag | no XML tag in name, description (…)
PASS trigger.line_budget | 597 lines within budget 600 (from box at line 292)
PASS trigger.no_placeholder | no placeholder markers in 536 scanned lines
PASS trigger.command_binary_resolves | 19 segments; 34 command subject(s) resolve
PASS trigger.citation_resolves | 139 repo-rooted citation token(s) resolve from the repo root
PASS governance.citation_resolves | 1074 governance citation token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused
```

### B (patch state, 573 lines) — checklist, exit 0

```
{'exit_code': 0, 'fail': 0, 'na': 0, 'pass': 11}
PASS checklist.box_map_complete | 41 boxes mapped (8 executed, 4 delegated, 29 unexecuted); …
PASS trigger.frontmatter_parses | frontmatter parses: name='kotoba-shokunin', description 1019 chars
PASS trigger.name_directory | name 'kotoba-shokunin' == directory 'kotoba-shokunin'
PASS trigger.literal_trigger_string | description carries literal 'Triggers:'
PASS trigger.anti_trigger_clause | exclusion marker 'Anti-triggers' present (…)
PASS trigger.no_xml_tag | no XML tag in name, description (…)
PASS trigger.line_budget | 573 lines within budget 600 (from box at line 292)
PASS trigger.no_placeholder | no placeholder markers in 512 scanned lines
PASS trigger.command_binary_resolves | 19 segments; 34 command subject(s) resolve
PASS trigger.citation_resolves | 140 repo-rooted citation token(s) resolve from the repo root
PASS governance.citation_resolves | 1074 governance citation token(s) resolve across 2 files; …
```

The citation count rises 139 → 140 because the pointer adds `corpus/knowledge/anatomy-and-compression.md` and the moved bullets carried no repo-rooted token. `trigger.command_binary_resolves` is unchanged (19 segments / 34 subjects): the moved block contains no fenced shell block and no vocabulary inline command.

### C (patch + 12-line section, 586 lines) — checklist, exit 0

```
{'exit_code': 0, 'fail': 0, 'na': 0, 'pass': 11}
PASS … (all eleven as in B, with:)
PASS trigger.line_budget | 586 lines within budget 600 (from box at line 305)
PASS trigger.no_placeholder | no placeholder markers in 522 scanned lines
PASS trigger.citation_resolves | 140 repo-rooted citation token(s) resolve from the repo root
```

The placeholder text used for C, inserted between the last `### Custom command files by client` table row and `## Router model — which harness, which gate` (12 lines plus the blank separator line that markdown requires before the next heading):

```
### Hook files by client

Stand-in for the C1 hook-files section (12 lines, replaced by the C1 seat; not part of the delivered patch).

| Client | Hook config | Events | Action |
|---|---|---|---|
| Claude Code | C1 | C1 | C1 |
| Codex | C1 | C1 | C1 |
| VS Code | C1 | C1 | C1 |
| Copilot CLI | C1 | C1 | C1 |
| Gemini CLI | C1 | C1 | C1 |
| Cursor | C1 | C1 | C1 |
```

### Budget arithmetic for the C1 seat

`597 − 28 + 4 = 573` without the section; `573 + 1 (blank) + N ≤ 600` leaves **N ≤ 26** lines for the real `### Hook files by client` section. A 12-line section lands at 586 with 14 lines to spare.

## 5. Corpus gate — pre-existing drift, identical before and after

`verify_corpus_integrity.py --json` exits 1 at the freeze and in both edited states, with the **same nine rows** (compared programmatically: `placeholder-state == patch-state: True`, and the freeze receipt equals both):

| check | observed | expected | verdict |
|---|---|---|---|
| `corpus.index.tracked_files` | 94 | 81 | DRIFT |
| `corpus.index.unindexed` | 1 (`corpus/lessons/round-58-verifier-spotcheck.md`) | 0 | DRIFT |
| `corpus.index.stale_patterns` | 0 | 0 | PASS |
| `corpus.index.missing_paths` | 0 | 0 | PASS |
| `corpus.pointers.report_total` | 64 | 51 | DRIFT |
| `corpus.pointers.report_dead` | 0 | 0 | PASS |
| `corpus.pointers.commit_total` | 33 | 32 | DRIFT |
| `corpus.pointers.commit_unresolvable` | 1 | 0 | DRIFT |
| `corpus.pointers.commit_nonhash` | 0 | 0 | PASS |

That is a stale `verifiers/corpus-baseline.json` at `67b68e0f` (expected 81 tracked files against 94 on disk), not a finding of this patch: the receipts at `before-corpus.json`, `after-placeholder-corpus.json`, `after-patch-corpus.json` are row-identical. The patch adds **no** new corpus file, so `tracked_files` and `unindexed` cannot move, and it adds no `commit <hex>` citation and no `.ufo/reports/round-N/*.md` pointer.

## 6. Dangle sweep (the moved lines and their anchors)

- `grep -rn -F 'posture-skill anatomy'` lane-wide → only `.ufo/round-33/SKILL.md:369`, a 521-line **snapshot copy** of `SKILL.md` committed at round 33 (a historical artifact, not a pointer into the live file). Same for `hub/routing tables`, `invariant lists (I1`, `plan-before-apply`, `sekhmet-l3/SKILL.md` — `.ufo/round-33/SKILL.md` only.
- No verifier parses § Sources: `grep -rn "§ Sources\|## Sources\|Sources section" verifiers/*.py` → empty. `check_command_files.py:284,444,449`, `check_agent_definitions.py`, `check_plugin_manifests.py`, `check_hook_files.py:292,472,475` all scope their row reads to their own frozen section heading, so this edit is outside every reader's subject.
- `## Sources` heading stays live with 20 bullets after the move (the new pointer plus the AGENTS.md sweep, both prompt sweeps, the opencode artifacts, the omp cache/session entries, six `corpus/knowledge/` entries and `verifiers/README.md`), so references of the form "SKILL.md § Sources" still resolve to a section — old `§ Sources` mentions in `.ufo/reports/round-23…45` are point-in-time receipts.
- Line-number citations in old receipts (`.ufo/round-21/scouts/G5.md:205`, `.ufo/round-35/scouts/N07.md:38`, …) refer to the file at their own rounds and were already stale; as with round 58, **integrate by text, not line number**: this patch shifts every line after old 481 up by 24 (28 out, 4 in). Round-49's `SKILL.md:509-520` and round-47's `SKILL.md:497-500` citations are in that shifted range and are historical.

## 7. Notes and risks for the L1

1. **Do not land the placeholder.** With a `### Hook files by client` heading present, `verifiers/check_hook_files.py` reads its first table as the C1 surface; the stand-in rows would be scored as unbacked rows. The patch contains no placeholder.
2. **Run `verify_skill_checklist.py` in the lane or a mirror, not a bare clone.** In a clone whose directory is not named `kotoba-shokunin`, `trigger.name_directory` FAILs; without the fleet-root siblings, `trigger.citation_resolves` FAILs on `../.ufo/reports/round-7/kotoba.md` and `governance.citation_resolves` FAILs on 25 `../` tokens in `LOG.md` (the run printed four named sites plus `… (+21 more)`), plus `SCORECARD.md`'s `../MISSION.md` / `../SCORECARD.md` until those two siblings exist. My first run in a bare clone showed exactly those three FAILs; the table above is the mirror run.
3. **`corpus/knowledge/anatomy-and-compression.md`'s `corpus/README.md` row (line 10) is behind.** Its prose note ends at "round 15 absorbed the six compression rules"; rounds 57, 58 and now 59 have since moved sections into the same file. Not touched here (rounds 57/58 did not touch it either) — a one-line index refresh is a separate, safe item.
4. The knowledge file now ends with the moved block; the `§ Moved from …` heading chain mirrors the round-57/58 form (`## Moved from SKILL.md § Decision tables (round 57)`, `## Moved from SKILL.md § Skill-file anatomy (round 58)`).
5. The moved bullets are host-path study entries (`~/.agents/skills/...`), which the checklist's citation box does not cover and the corpus verifier does not treat as a citation subject; their liveness was not re-measured this round and no claim about it is made.
6. `corpus/knowledge/anatomy-and-compression.md` carries no `source: / verified-at: / recheck:` frontmatter although `/home/vgpnk/Projects/shokunin/CORPUS.md:18` and `corpus/QUALITY.md` Q12 ask each entry to; 43 of the 45 tracked `corpus/knowledge/*.md` files are in the same state and no verifier enforces the field (`grep -rln "verified-at" verifiers/*.py` → empty). The moved section therefore states its own provenance in prose (rev, lines, sha256, receipt) instead of adding a frontmatter block to a file that has never had one. Flagged, not fixed — a frontmatter retrofit is a separate item.

## 8. Sandbox and receipts

- Clone (pristine): `/fast/scratch/hyaku/kotoba-r59/ExecBudgetMove` at `67b68e0f…`
- Mirror world (gates before/after): `/fast/scratch/hyaku/kotoba-r59/ExecBudgetMove/world/kotoba-shokunin` + symlinks `../AXES.md`, `../MISSION.md`, `../PROTOCOL.md`, `../SCORECARD.md`, `../kasegi-shokunin`, `../.ufo`
- Apply test: `/fast/scratch/hyaku/kotoba-r59/ExecBudgetMove/applytest2`
- Receipts (JSON + extracted blocks): `/fast/scratch/hyaku/kotoba-r59/ExecBudgetMove/receipts/{before-checklist,after-placeholder-checklist,after-patch-checklist,before-corpus,after-placeholder-corpus,after-patch-corpus}.json`, `moved-block.txt`, `moved-block-after.txt`, `ExecBudgetMove.patch`
- No sandbox commit; no lane write other than this report and the patch above; no git/jj write in the lane.
- Tooling: nothing installed or upgraded.
