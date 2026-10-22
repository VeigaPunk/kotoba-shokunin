# Falsify: C1 census row `game-dev-2d` (seat RowGameDev2d)

**Verdict: HOLDS-BOUNDED.** Applies to the `game-dev-2d` row of `corpus/knowledge/sibling-overlap-census-round49.md` and its `PROVINCE.md` § Adjacent row, judged at kotoba master c48793dbe5eb30cd661f42ecad7399ae94e3d7ad against sibling pin 7753d49b16674e122ed134403e7a9b301f2cbf7e. The commit, branch, quote, both mechanical cell values and the boundary-note facts hold. `none` holds on the rule's literal test, but one sibling sentence (`PROVINCE.md:32`, "generic harness/evidence audits → their owning lanes") is the closest reading that could make the row `adjacent`, and no census text rules on it. At the judged commit the guard does not check the row's mechanical cells. A later uncommitted working-copy edit does check them, but those bytes are not judged.

Attacked: (1) pin and branch cell; (2) quote location; (3) `none` against the rule, with sweeps over all text at the pin and kotoba's committed surfaces; (4) mechanical cells and the guard that checks them; (5) kotoba `PROVINCE.md` row (judged line 39) and every cited sibling line.

## Findings (severity order)

**F1 — Medium — `none` leaves one adjacency reading unexamined (judged bytes).**
- Sibling `PROVINCE.md:32` routes "generic harness/evidence audits" to "their owning lanes" and names none.
- Kotoba's committed Core claims harness-claim instruments: `PROVINCE.md:14` lists `verifiers/verify_harness_claims.py` and `verifiers/compare_harness_independent.py`. `verifiers/verify_harness_independent.py` is a "source-blind re-derivation of the harness claim set". `SKILL.md:470-476` calls `verify_harness_claims.py` "the authority for every harness number in this file".
- Against the reading: the sibling's refused names (`harness-integrity`, `gate-evidence`, `rlm-dispatch`, `art-east-asian-design`) are not fleet directories (E19). Kotoba's committed surfaces never use the first three; they appear only in `.ufo/waves/round-49/build/*.md`. Kotoba's instruments audit skill-router facts (omp and opencode catalogue, render, offer gate), not evidence gates.
- Across all 20 sibling `PROVINCE.md` files at their pins (E18), no sibling claims generic harness audits as its own. game-dev-3d (lines 34-35) and revenger (line 22) refuse them; revenger line 32 disclaims "generic harness gates". For generic evidence audits, the likelier fleet owner is tameshi (`PROVINCE.md:5`, "no-permissiveness audits"), not kotoba. The census does not say so.
- Effect: the rule ("state a split ... between the sibling and kotoba") is not met on its literal text, so `none` stands. But the build seat's report judges only the Refuses line and never tests whether "their owning lanes" includes kotoba. The census should record the reading and why it fails, or reclassify.

**F2 — Medium — the guard does not check this row's mechanical cells at the judged commit.**
- `verifiers/check_sibling_census.py` at c48793d: lines 383-386 test only that cells are non-empty. Lines 410-413 say the `path` cell is not used. So `NONE` / `no SKILL.md` / `no SKILL.md` would pass with any values.
- Docstring lines 40-41 say the `path:line` file "is one of the skill file(s) the row names". The code does not enforce that. For this row `PROVINCE.md:3` is the right location, so the docstring is wrong, not the row.
- By hand (E8): `git show 7753d49…:SKILL.md` fails with rc 128, so `no SKILL.md` is the correct value.

**F3 — Medium (records) — the lane working copy is not the judged bytes.**
- `cmp` against the c48793d blobs (E25): the census differs (rc 1), `PROVINCE.md` differs (rc 1), and `verifiers/check_sibling_census.py` differs (119 diff lines). Working-copy mtimes are 08:34:18 (PROVINCE) and 08:34:24 (census), local time.
- Uncommitted edits: a "Falsify-wave corrections" section appended at census line 140; `kake` and `kasegi` moved from `none` to `adjacent` (census lines 75 and 77, judged 69 and 71); the count line reads "9 adjacent, 11 none" (lines 99-100, judged 93-94); PROVINCE rows changed to match.
- Judged bytes read "7 adjacent, 13 none" (E24). Any count quoted must name which bytes it reads.
- For this row the working copy changes only wording. The game-dev-2d boundary note now reads "no split with kotoba on its scope surfaces (seat sweep in the census row's report)". That is more precise than the judged "no claim on kotoba ground", but it still rests on the seat report, which lacks the F1 analysis.

**F4 — Low — seat report `CensusGameDev2d.md` misses or mis-cites four items.**
- "Godot 4.7.2 (`Core`, line 14)": the Godot statement is on line 16. Line 14 is the `## Core` heading.
- "The 11 SKILL.md lines in 6 md files" omits `reports/round-105/r105-R105Connector.md:25`. It points at `chousa-shokunin/SKILL.md:6-21` as the "Chousa Research Method Location". That is a pointer, not an audit, so no classification effect. The `reports/round-102/r102-scr5.md` lines 7, 62, 145 and 158 are lumped under "its own promotion procedure" without a per-line check.
- Sibling `PROVINCE.md:35-38` (write-scope history: "kaika r105", "aborted 3D r107 side-round") is not analysed.
- Sibling `SHONEN.md:8` ("Instructions executable by an agent without oral context") sets content requirements on a SKILL.md, the artifact class kotoba audits. It states no split with kotoba, so `none` holds by the literal rule. The report should say that.

**F5 — Low — no action needed.** For a no-skill lane the `names kotoba` and `arbitration` cells read "no SKILL.md", not "no". The census counts filter on `$6=="yes"` and `$7 ~ /^yes/`, so the counts still work.

## Check-by-check

1. **Commit and branch — HOLDS.** The pin exists (E1, rc 0). `refs/heads/main`, `refs/remotes/origin/main` and `refs/remotes/origin/HEAD` all resolve to 7753d49 (E3). `master` does not exist (E2, rc 1). `main` contains the pin, with 0 commits ahead (E5). The checkout is detached at the same commit (E4). The census's `main` is correct.
2. **Quote at PROVINCE.md:3 (±2 lines) — HOLDS.** Line 3 reads "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness." The census quote matches after whitespace collapse, em dash included (E6, E7). The guard checks it (E22).
3. **Classification `none` — HOLDS-BOUNDED (F1).**
   - Skill and prompt file names: 0 matches for `skill|prompt|agents` in names (E9). 0 non-markdown matches for `AGENTS.md|SKILL.md|frontmatter` (E10). `frontmatter` has 0 matches in any file.
   - `kotoba` appears in 3 files and 3 lines, all outside any scope claim: `r102-connector.md:23` (census key count), `r103-connector.md:34` (staleness table row), `r105-R105Reviewer.md:84` (peer note) (E11).
   - `skill` (case-insensitive): 18 lines in 11 files, all read. None claims another lane's SKILL.md craft (E14).
   - `prompt`: 20 markdown files and 32 lines, all engine or environment prose (`PYGAME_HIDE_SUPPORT_PROMPT`, "promptly") or self-reference. 411 non-markdown lines; the top 25 contexts are all the PYGAME variable (job `bg_4593`). Excluding the PYGAME variable leaves 1 line, "promptly" in `corpus/live/r62-critic/drive_attacks.py:12` (E15).
   - `AGENTS.md`: one markdown hit, `reports/round-104/r104-scr5.md:70`, a read of game-dev-3d's file for a lifecycle check, "read, not modified" (E16). Not an audit.
   - `reports/fleet-round-1-calibration/dispatch.json` is the lane's own calibration record. `considerthese/2026-10-19..21.md` are lane reflections with no scope claim on kotoba's ground.
   - Kotoba's side: the `SKILL.md` frontmatter (lines 1-16) claims "audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts" and names kagi, kake, kasegi, kengaku and kumitate as owning their own SKILL.md content. game-dev-2d is not named.
   - Parent gate: `/home/vgpnk/.kimi-code/skills/shokunin/SKILL.md:160-176` requires review "by a reviewer who did not author the round's changes". It names no lane, so it is not a split.
4. **Mechanical cells — values HOLD; guard gap at the judged commit (F2).** Row cells: `NONE | none | no SKILL.md | no SKILL.md | PROVINCE.md:3`. Derivation: no `SKILL.md` at the pin (E8), so the rule's value is `no SKILL.md` for both cells. Judged-bytes counts (E24): 20 rows, 13 `none`, 7 `adjacent`; names kotoba = yes for kengaku and kotodama; arbitration starts with yes for 8.
5. **Boundary note (judged line 39) — HOLDS-BOUNDED.**
   - "2D game production" matches sibling `PROVINCE.md:3`.
   - "no skill file at the pin" holds (E8, E9).
   - "(seed form)": `README.md:12-13` says "absent on lanes still in shonen seed form"; `SHONEN.md:5` is an unchecked box; `SHONEN.md:6-10` are `[~]` boxes.
   - "no claim on kotoba ground" holds except for F1.
   - Cited sibling lines checked at the pin (E20): `PROVINCE.md:10` (Refuses) and `:29-33` (Adjacent) are accurate; `README.md:12-13`; `SHONEN.md:5`; `r102-scr5.md:12`; `r103-scr5.md:95`; `r104-scr5.md:70` and `:170`; `r102-connector.md:23`; `r103-connector.md:34`; `r105-R105Reviewer.md:84`. All exist at the pin.
   - Seat counts reproduce: 115 files and 171 lines for the prose sweep (E12); 49 `verify|audit|check` scripts (E17).

## Residual risk and verification gaps

- The only sentence that could flip the row is `PROVINCE.md:32`. Whether "generic harness/evidence audits" means kotoba's `verify_harness_independent.py` family needs the lane operator's reading. I did not settle it.
- Non-markdown hits for `AGENTS` (492 lines), `description` (1,867), `trigger` (1,097) and `harness` (4,068) were not read line by line. I checked the terms that matter for this row: `skill`, `SKILL.md`, `AGENTS.md`, `frontmatter`, and `prompt` minus the PYGAME variable.
- Narrow sweeps only for `trigger` and `description`: they found no skill-trigger or skill-description claim in markdown.
- No web sources consulted. No sibling repo was written.

## Tooling

None installed. Present on the host: Python 3.14.8, git 2.56.0. No pacman transaction. No write command ran in the lane, the fleet repo or any sibling repo. Scratch work is under `/fast/scratch/hyaku/kotoba-r49/falsify/RowGameDev2d/`.

## Evidence (run 2026-10-22; exit codes verbatim)

Sibling `R=/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin`, pin `C=7753d49b…`. Kotoba judged clone `K` = scratch clone checked out at c48793d.

- E1 `git -C R cat-file -t C` → `commit`, rc 0.
- E2 `git -C R rev-parse -q --verify master` → rc 1.
- E3 `git -C R for-each-ref` (main, origin/main, origin/HEAD) → all `7753d49b…`.
- E4 `git -C R branch -a --contains C` → `* (no branch)`, `main`, `remotes/origin/main`, rc 0.
- E5 `git -C R rev-list --count C..main` → 0; `git -C R merge-base --is-ancestor C main` → rc 0.
- E6 `git -C R show C:PROVINCE.md | cat -n` → line 3 as quoted; rc 0.
- E7 Python: census quote vs line 3 after whitespace collapse → `True`.
- E8 `git -C R show C:SKILL.md` → "path 'SKILL.md' does not exist", rc 128.
- E9 `git -C R ls-tree -r --name-only C | grep -Eic '(skill|prompt|agents)'` → 0.
- E10 `git -C R grep -c -E 'AGENTS\.md|SKILL\.md|frontmatter' C -- ':!*.md' | wc -l` → 0.
- E11 `git -C R grep -I -i -E kotoba C -- . | wc -l` → 3 lines (3 files).
- E12 `git -C R grep -l -E 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba' C -- '*.md' | wc -l` → 115; the same without `-l` → 171 lines.
- E13 `git -C R grep -c -E 'SKILL\.md' C -- '*.md'` → README 1, SHONEN 1, r102-scr5 5, r103-scr5 2, r104-scr5 1, r105-R105Connector 1 (11 lines, 6 files).
- E14 `git -C R grep -n -I -i -E skill C -- .` → 18 lines, 11 files.
- E15 `git -C R grep -h -i -E prompt C -- ':!*.md' | grep -v -i PYGAME_HIDE_SUPPORT_PROMPT | wc -l` → 1; `grep -c` of the non-markdown prompt lines in the earlier run → 411.
- E16 `git -C R grep -n -I -E 'AGENTS\.md' C -- '*.md'` → `reports/round-104/r104-scr5.md:70` only.
- E17 `git -C R ls-tree -r --name-only C | grep -Eic '/(verif|audit|check)[^/]*\.(py|sh)$'` → 49.
- E18 Python over the 20 census pins: `git show <pin>:PROVINCE.md`, harness/audit lines. Refusals only in game-dev-3d 34-35, revenger 22 and 32, tameshi 5.
- E19 `ls -d /home/vgpnk/Projects/shokunin/{harness-integrity,gate-evidence,rlm-dispatch,art-east-asian-design}*` → "No such file or directory". `/home/vgpnk/Projects/prymeagnt-archive/research/art-east-asian-design` exists.
- E20 `git -C R show C:<path> | sed -n Np` for the cited lines listed in check 5, plus `reports/round-105/r105-R105Connector.md` 18-25 → all present; line 25 names `chousa-shokunin/SKILL.md:6-21`.
- E21 `git -C K grep -n -i harness -- PROVINCE.md SKILL.md 'corpus/*.md' | wc -l` (judged c48793d) → 249. Lines cited: `PROVINCE.md:14`; `SKILL.md:100-119`, `470-476`; `corpus/README.md:34`, `38`.
- E22 Judged guard, from `K`: `TMPDIR=<scratch> python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --fleet /home/vgpnk/Projects/shokunin` → `rows 20 verified 20`, `province rows 20 matched 20`, exit 0.
- E23 `python3 -B verifiers/check_sibling_census.py --self-test` (TMPDIR in scratch) → `self-test: 0 failure(s) over 39 assertions`, exit 0.
- E24 Python over `git -C K show c48793d:corpus/knowledge/sibling-overlap-census-round49.md` → rows 20, `{'none': 13, 'adjacent': 7}`; names kotoba yes `['kengaku','kotodama']`; arbitration yes 8.
- E25 `cmp` judged blob vs lane working copy → census rc 1, PROVINCE rc 1; `diff` of the verifier → 119 lines.
- E26 Working-copy guard, copied to scratch and run there → `rows 20 verified 20`, `province rows 20 matched 20`, exit 0.
