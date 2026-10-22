ROW | revenger | main(detached) | 876630dbb4d630e016d7d8c32a19ea04c646cbae | NONE | none | no | no | PROVINCE.md:3-5 | "Owns: reverse engineering of shipped artifacts — native binaries, managed assemblies, Electron/JavaScript packages, Android APKs, archives, firmware, browser/Electron runtime evidence"

# CensusRevenger — C1 sibling-overlap census row: revenger-shokunin

Measured 2026-10-22 (UTC) against the sibling repo read-only; lane base kotoba
`a5adc146a2995dcc5a95a6d8db6e5674f75191ac`.

## Findings

1. **Pin.** `revenger-shokunin` has no `master` branch; HEAD is **detached** at
   `876630dbb4d630e016d7d8c32a19ea04c646cbae`, which is exactly `refs/heads/main`
   (2026-10-21 19:26:01 -0300, "round-62: measured K4/14 to6/14 …"). The repo is
   jj-colocated (`.jj` present), which explains the detached HEAD. The one other branch,
   `hyaku/s3-ready66-revenger` (`d977619`), is an ancestor of the pin. Working tree clean
   (`git status --porcelain` → 0 lines).
2. **No SKILL.md anywhere at the pin** — not at top level, not under `skills/*/`, and no
   file in the 864-entry tree has "skill" in its name (three sweeps below; each exits 1 with
   no match, the `-c` forms printing 0). There is likewise no `AGENTS.md`,
   `CLAUDE.md`, `.claude/` tree, plugin manifest or `verifiers/` directory. The lane's only
   instruction surfaces are `PROVINCE.md` (32 lines), `README.md` (58), `SHONEN.md` (12),
   `SCORECARD.md` (301), `LOG.md` (857) and `corpus/`. Read per the fallback in the task:
   README/PROVINCE plus SHONEN (its promotion checklist).
3. **Classification: `none`.** kotoba's Core is craft *over* skill/agent/dispatch surfaces
   plus instruments over them, and it refuses domain content inside other skills. revenger
   claims the complementary half: reverse engineering of shipped artifacts via the REA skill
   and toolset, under its own evidence-ledger discipline (`PROVINCE.md:3-7`). It does **not**
   claim writing or auditing SKILL.md, prompts or AGENTS.md — for itself or any other lane.
   It explicitly refuses "harness/evidence auditing (harness-integrity, gate-evidence,
   rlm-dispatch)" (`PROVINCE.md:22`) and refuses "game mechanics verification (game-dev-2d);
   narrative canon (lore)" (`PROVINCE.md:23`), and its write scope is "only this
   `revenger-shokunin/` repository … sibling repositories remain read-only" (`PROVINCE.md:25-29`).
   It is a **subject** of kotoba's surfaces, not an owner: its own SKILL.md and AGENTS.md are
   recorded as *absent named debt* (`SCORECARD.md:109-110`, `:124-125`; `SHONEN.md:5-6`
   "`SKILL.md` is absent"), and `README.md:10-11` advertises `SKILL.md` as a file it still
   owes. A lane that owes a SKILL.md cannot contest the lane that governs SKILL.md craft.
4. **Sweep (the `none` evidence).** Prescribed grep over the five pinned top-level docs:
   **10 matches** across PROVINCE 1, README 1, SHONEN 2, LOG 4, SCORECARD 2 — every one
   enumerated below. All ten concern revenger's *own* absent SKILL.md/AGENTS.md, its own
   received dispatch prompt (`.ufo/prompts/revenger-round-1-continuation-kaika.md`), or its
   own evidence-ledger prose. Zero concern another lane's surfaces. Whole-tree sweep for
   `prompt` reaches 17 files / 377 matches, but the sampled hits are its own wave dispatch
   files (`build-dispatch.json`, `falsify-dispatch.json`), its own received prompt, and EVM
   *opcode* dispatch bytes — no authored prompt for a sibling.
5. **kotoba naming.** Zero occurrences, at both the file and line level:
   `git grep -ci kotoba <pin> -- .` → **0 files**; `git show <pin>:PROVINCE.md | grep -c kotoba`
   → **0** (exit 1); same for README.md and SHONEN.md (0, exit 1 each). So the description
   field is `no` vacuously (no frontmatter description exists at all) and the arbitration
   field is `no`.
6. **Arbitration clause: no (frontmatter), and no province-level clause naming kotoba.**
   The closest thing is the refusal list at `PROVINCE.md:22-23`, which names *domains*
   (`game-dev-2d`, `lore`) plus three role aliases (`harness-integrity`, `gate-evidence`,
   `rlm-dispatch`) that are **not** directories under `/home/vgpnk/Projects/shokunin`
   (`ls -d` exit 2). That is a refusal of foreign work, not a priority rule between
   overlapping claims, and it does not mention kotoba or skill/prompt craft.
7. **Cross-check against prior kotoba records (consistency, not new evidence).** kotoba
   already lists revenger in `PROVINCE.md:34` as "revenger (shipped-artifact RE) … no overlap
   observed"; round-47 `C2FleetScan.md:83,137` classed `revenger-shokunin` as "no top-level
   SKILL.md → N/A (absent, not FAIL)" at pin `e0a4b0c4348e`; round-46 `w2-connector.md:19,26`
   records the same split. This round's independent row agrees; the pin has advanced **15
   commits** since the round-47 pin (2026-10-21 12:10:10 -0300) with no SKILL.md at either end.
   For the census, cite the 40-hex `876630dbb4d630e016d7d8c32a19ea04c646cbae`, not the prefix.

## Evidence (exit codes are each command's own; for pipelines, the last stage's; run 2026-10-22, read-only)

Pin:
```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse master
fatal: ambiguous argument 'master': unknown revision or path not in the working tree.   exit 128
$ git -C … symbolic-ref -q HEAD        # (no output)                                    exit 1  (detached)
$ git -C … branch --show-current       # (no output)                                    exit 0
$ git -C … rev-parse HEAD
876630dbb4d630e016d7d8c32a19ea04c646cbae                                               exit 0
$ git -C … rev-parse main
876630dbb4d630e016d7d8c32a19ea04c646cbae                                               exit 0  (HEAD == main tip)
$ git -C … for-each-ref --format='%(refname) %(objectname:short)' refs/heads
refs/heads/hyaku/s3-ready66-revenger d977619
refs/heads/main 876630d                                                               exit 0
$ git -C … merge-base --is-ancestor d977619 876630d → exit 0 (ancestor)
$ git -C … log -1 --format='%H %ci %s'
876630dbb4d630e016d7d8c32a19ea04c646cbae 2026-10-21 19:26:01 -0300 round-62: measured K4/14 to6/14 … exit 0
$ git -C … status --porcelain | wc -l  → 0                                            exit 0
$ git -C … rev-list --count e0a4b0c4348e..876630dbb4d630…  → 15                       exit 0
```
Tree (no SKILL.md):
```
$ git -C … ls-tree --name-only 876630dbb4d630…
.gitignore .ufo LOG.md PROVINCE.md README.md SCORECARD.md SHONEN.md considerthese corpus reports   exit 0
$ git -C … ls-tree -r --name-only 876630dbb4d630… | grep -E '^(skills?/[^/]+/)?SKILL\.md$'   (no output) exit 1
$ git -C … ls-tree -r --name-only 876630dbb4d630… | grep -ci skill  → 0                 exit 1
$ git -C … ls-tree -r --name-only 876630dbb4d630… | grep -cE '(^|/)(AGENTS|CLAUDE)\.md$' → 0 exit 1
$ git -C … ls-tree -r --name-only 876630dbb4d630… | grep -cE '\.claude|plugin|manifest\.json' → 2 (both its own .ufo wave manifests) exit 0
$ git -C … ls-tree -r --name-only 876630dbb4d630… | wc -l → 864                         exit 0
```
Sweep and kotoba counts:
```
$ git -C … grep -nEi 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba' \
    876630dbb4d630… -- PROVINCE.md README.md SHONEN.md LOG.md SCORECARD.md | wc -l → 10  exit 0
  per file: PROVINCE.md 1, README.md 1, SHONEN.md 2, LOG.md 4, SCORECARD.md 2
  the 10 hits, by line: PROVINCE.md:10 (REA skill SKILL.md, external path);
  README.md:10 (own SKILL.md); SHONEN.md:5,6 (own SKILL.md absent);
  LOG.md:63,441,757,769 (own fixture review, REA SKILL.md, own absent AGENTS.md/SKILL.md, own received dispatch prompt);
  SCORECARD.md:109,124 (own SKILL.md/AGENTS.md named debt)
$ git -C … grep -ci kotoba 876630dbb4d630… -- . | wc -l → 0                            exit 0
$ git -C … show 876630dbb4d630…:PROVINCE.md | grep -c kotoba → 0                       exit 1
$ git -C … show 876630dbb4d630…:README.md | grep -c kotoba → 0                         exit 1
$ git -C … show 876630dbb4d630…:SHONEN.md | grep -c kotoba → 0                         exit 1
$ git -C … grep -ci prompt 876630dbb4d630… | awk -F: '{s+=$NF} END {print NR" files "s" matches"}'
17 files 377 matches                                                                   exit 0
$ git -C … grep -ciE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description' 876630dbb4d630… \
    | awk -F: '{s+=$NF} END {print NR" files "s" matches"}' → 82 files 493 matches     exit 0
```
Quote (verbatim, `PROVINCE.md:3-5`, 20 whitespace tokens incl. the em dash):
```
$ git -C … show 876630dbb4d630…:PROVINCE.md | sed -n '3,5p'
Owns: reverse engineering of shipped artifacts — native binaries, managed
assemblies, Electron/JavaScript packages, Android APKs, archives, firmware,
browser/Electron runtime evidence — using the REA skill and its toolset,
```
Anchors: `PROVINCE.md:3-7` Owns; `:19-23` Refuses (harness/evidence auditing; game-dev-2d;
lore); `:25-29` writes only this repo, siblings read-only; `SHONEN.md:5-6` "`SKILL.md` is
absent"; `SCORECARD.md:109-110,124-125` named debt; `README.md:10-11` own SKILL.md;
`reports/round-1/connector.md:21-29` its own sibling-overlap scan (states "no overlap that
requires or permits a sibling edit", "Author-side L2 evidence only; no promotion or
outside-discernment authority").
kotoba side: `PROVINCE.md:34` already names revenger "no overlap observed"; round-47
`.ufo/waves/round-47/build/C2FleetScan.md:83,137`; round-46
`.ufo/round-46/scouts/w2-connector.md:19,26`. kotoba tooling does not target the sibling:
`grep -rn revenger verifiers/*.py` → exit 1 (sibling absolute paths occur only inside
`verifiers/__pycache__/*.pyc` path strings, not source).

## Inference (labelled)

- `[INFERENCE]` The 15-commit drift (round-61 → round-62 admission) is ordinary lane
  progress; the tree gained `.ufo/waves/round-62/**`, `corpus/knowledge/round-62-*`,
  `reports/round-62/**` and no SKILL.md at either pin. Not exhaustively diffed — unknown 1.
- `[INFERENCE]` revenger's own sibling-overlap scan (round-1 connector) is per-round impact
  analysis of its own fix, not fleet arbitration maintenance; it claims no authority over
  another lane's wording, so it does not make the pair `contested`.

## Remaining unknowns

1. Not diffed file-by-file across `e0a4b0c4348e..876630d` (only endpoint trees sampled); a
   prompt-craft claim hidden in round-62 wave prose would be missed by the file-name and
   top-level-doc sweeps. The whole-tree `prompt` sample showed none.
2. Whether revenger will, on promotion, author a SKILL.md that kotoba's instruments then
   verify — expected (its SHONEN gate requires it), but no date or claim exists at the pin,
   so this row records `none` at the measured commit only.
3. `harness-integrity`, `gate-evidence`, `rlm-dispatch` (`PROVINCE.md:22`) are neither fleet
   directories nor 20-list lane names; what they denote (program aliases? retired lanes?) is
   not resolvable from this repo.
