# Round 49 falsify — RowAudio (C1 census row `audio`)

**Verdict: HOLDS-BOUNDED** for the `audio` row (census `corpus/knowledge/sibling-overlap-census-round49.md:63`) and its PROVINCE.md § Adjacent row (`PROVINCE.md:37`). Classification `none` is correct under the § Classification rule at audio pin `7a2fcd4f08831154686e4e323031f41fffdb077f`, judged against kotoba master `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`. Bounded because (a) the content guard checks none of the row's branch, skill-file, names-kotoba, arbitration or boundary-text cells, and (b) the lane working copy of the guard changed during this review, so it no longer matches the judged bytes.

Scope: census row audio, PROVINCE.md:37, `.ufo/waves/round-49/build/CensusAudio.md`, `verifiers/check_sibling_census.py` at master. Sibling reads used only `git show`, `ls-tree`, `rev-parse`, `log`, `grep`. Guard runs and mutants ran only in the private clone `/fast/scratch/hyaku/kotoba-r49/falsify/RowAudio/kotoba` (checked out at c48793db). Tools installed or upgraded: none (git and python3 already present; no pacman). No subagent.

## Findings, by severity

1. **Medium — the guard does not check the audio row's non-quote cells or the PROVINCE boundary text.** `check_census` (verifier lines 329–457 at c48793db) checks cell presence, a 40-hex commit, the classification set, `path:line`, the quote within ±2 lines, and headings. Lines 410–413 say the `path` (skill file) cell is not used. `_check_province` (478–550) compares only the lane set, classification and commit. Three mutants in the clone each exit 0:
   - A: audio branch `main` → `master` (no such ref at the pin). Guard exit 0.
   - B: audio skill-file `NONE` → `SKILL.md`, and names-kotoba `no SKILL.md` → `yes: kotoba`. Guard exit 0.
   - C: PROVINCE.md:37 boundary → "game audio production; SKILL.md present at the pin; claims kotoba ground". Guard exit 0.
   The row itself is right, so this is a coverage gap. The audio facts "main", "NONE", "no SKILL.md" and "no skill file at the pin (seed form)" rest on the manual sweep only.

2. **Medium — the guard in the lane is not the judged bytes.** At the first read, the lane `verifiers/check_sibling_census.py` had tag #1158 and 923 lines, equal to master. At a later read it had tag #A8A0 and 1002 lines. The newer copy adds `MIN_QUOTE_WORDS` (about line 509) and `mechanical_findings(...)` (about lines 514–519), which master lacks. Master still has 923 lines (`git -C kotoba-shokunin show master:verifiers/check_sibling_census.py | wc -l` → 923, exit 0), and `master` resolves to c48793db (`rev-parse --verify --quiet master`, exit 0). The lane census and PROVINCE files match master (tags #EB32 and #9863). Someone edited the guard in the lane working copy during this review. I judged master. The working-copy guard may catch mutants A and B; I did not run it. Any guard verdict must name the bytes it judged.

3. **Low — evidence defects in the build seat's sweep (`CensusAudio.md`). None changes `none`.**
   - Per-file counts are case-sensitive: README 1, PROVINCE 3, SHONEN 1, SCORECARD 3, LOG 9, total 17. The report's per-pattern totals are case-insensitive (`trigger` 12). With `git grep -n -o -i`, LOG has 11 matching lines; the two extra are LOG.md:1588 and :1592 (`Trigger:` ledger rows, audio sense).
   - The report enumerates 12 of 17 lines. Not enumerated: LOG.md:111, 180 (triggers a section path / other checks), 258 (scaling "description"), 422 (engine triggers), 1355 (pactl description). I read each: all are audio or measurement senses.
   - "SCORECARD.md:70 … `description`" is wrong. Line 70 matches `trigger` in "would not have triggered the old exception" (exception-path sense).
   - The census writes "no SKILL.md" in the names-kotoba and arbitration cells (the rule's marker). The build's ROW line writes "no". Same meaning, different wording.

4. **Low — branch cell is right but incomplete.** `main` is a real ref at the pin: `refs/heads/main` → 7a2fcd4f…, exit 0; `origin/main` decorates the same commit. `master` does not exist (`--verify`, exit 1). HEAD is detached at the pin (`rev-parse --abbrev-ref HEAD` → `HEAD`, exit 0). The census drops "(detached HEAD)", which the build's ROW line keeps.

5. **Low — the word "trigger" is not addressed.** Audio uses "trigger" for engine and runtime triggers (PROVINCE.md:26, 27, 53; LOG.md:422). Kotoba's "trigger" means skill-description activation (`trigger.05`). These are different areas, so `none` holds. The row's evidence should say the word was read and set aside.

6. **Residual, not a defect of the row — promotion-gate wording.** audio SHONEN.md:5 and :8 use SKILL.md form language ("decision tables, error patterns, checklists"; "instructions executable by an agent without oral context"). The first criteria lines match game-dev-2d's SHONEN.md at 7753d49 (the files differ overall: sha256 prefixes 0c39b180… vs 2914ee45…). This is the seed template and states no split with kotoba. Build Finding 5 (latent boundary) stands and belongs in the next census round, not in a reclassification.

7. **Nit — quote cut.** The census quote ends at "(adaptive layers)" and drops "— verified by headless analysis …" with no ellipsis. It is still a verbatim substring (check below), so the row passes.

## Checked and correct

- **Commit and branch.** `cat-file -t 7a2f…` → `commit`, exit 0. Pin = `main` = `origin/main`. All 11 worktree refs (`wt-r90` … `wt-r100`) plus `main`: kotoba 0, SKILL.md 0, AGENTS.md 0 each (I checked all 11; the build checked 2).
- **Scope quote.** `git show 7a2f…:PROVINCE.md`, exit 0: line 3 `Owns: game audio production — SFX (UI, impacts, movement, ambience) and`; line 4 `soundtrack (motifs, loops, stems, adaptive layers) — verified by headless`. Python check (whitespace collapsed; reads only): census quote is a substring → `QUOTE_IN_PIN_PROVINCE True`, exit 0. Guard pristine: `rows 20 verified 20`, `province rows 20 matched 20`, exit 0.
- **Mechanical markers.** `git show 7a2f…:SKILL.md` → `fatal: path 'SKILL.md' does not exist`, exit 128. `ls-tree -r --name-only 7a2f… | grep -ciE skill` → 0 (grep exit 1). `git log --all --diff-filter=A --name-only -- '*SKILL.md' '*skill*' '*SKILL*' | grep -c .` → 0, exit 0: no skill-named path was ever added on any ref. So "no SKILL.md" is right.
- **Contested sweep (none found).** `git grep -il -E 'AGENTS\.md|CLAUDE\.md|frontmatter|skill craft|prompt craft|prompt engineering|system prompt|agent definition|trigger fidelity|kotodama|kotoba' 7a2f…` → no output. `git grep -l 'SKILL\.md' 7a2f… | wc -l` → 11: README.md:12, SHONEN.md:5, five `reports/round-1-calibration/` files (its own SKILL.md absence and a proposed SHONEN patch), `reports/round-93/r93-critic.md:258-259`, `r93-reviewer.md:6-7`, `r98-verifier.md:21`, `r99-scribe.md:8` (a fleet model-pin skill, `glmseat`, read as a first action; no craft claim). `git grep -il 'prompt' 7a2f… | wc -l` → 23; all are sox, PipeWire, labrat or dispatch-brief senses (for example `reports/round-95/r95-scribe.md:176`, `corpus/live/r85-reviewer/labrat/labrat-report.md:23`). None writes or audits another lane's prompts. `considerthese/` (3 daily reflections: 2019 read in full; 2020 and 2021 grep'd for craft, skill, prompt and agent terms, zero hits) and `ports/frontier/fb-pipewire.md` (one keyword hit, a seat brief path) hold no craft claim.
- **Adjacent sweep (none found).** `git grep -liw -- <name> 7a2f… | wc -l`: game-dev-2d 61, game-dev-3d 60, lore 13, revenger 7, mori 4, chousa 2; the other 13 lane names 0; `kotoba` 0 in all 50,576 files (`ls-tree -r … | wc -l`). `git log --all -i --grep=kotoba`, `--grep=skill`, `--grep=prompt` → 0 lines each. Kotoba side: `git -C kotoba-shokunin grep -n -i -w -E 'audio|sfx|soundtrack|sound|music|game|games' c48793db -- SKILL.md PROVINCE.md corpus/README.md corpus/QUALITY.md` → PROVINCE.md:37, 39, 40 only, exit 0. `git grep -il -w -E 'audio|soundtrack|sfx' c48793db | wc -l` → 29, mostly `.ufo` wave reports. So neither side states a split with the other.
- **Boundary-note facts** (PROVINCE.md:37). "game audio production" → PROVINCE.md:3–4 ✓. "no skill file at the pin" ✓ (above). "(seed form)" ✓: README.md:12–13 says SKILL.md is "absent on lanes still in shonen seed form"; README's list says SHONEN.md is "deleted on promotion", and it is present at the pin with its SKILL.md box `[ ]` (SHONEN.md:5). "no claim on kotoba ground" ✓ by the sweeps above.
- **Build's cited lines.** README.md:6, 12–13 ✓; SHONEN.md:5 ✓; PROVINCE.md:13–15 ✓, 26–27 ✓, 53 ✓; LOG.md:311 ✓ (matches `prompt`; not read beyond the build's quote); LOG.md:1622–1624 ✓; SCORECARD.md:831–832 ✓; SCORECARD.md:70 ✗ (see finding 3).

## Evidence (commands, exit codes)

- `git -C …/audio-shokunin rev-parse --abbrev-ref HEAD` → `HEAD`, exit 0; `rev-parse --verify --quiet refs/heads/master` → exit 1; `rev-parse --verify --quiet refs/heads/main` → pin, exit 0.
- `git -C …/audio-shokunin log -1 --format='%H|%D' 7a2f…` → `…|HEAD, origin/main, origin/HEAD, main`, exit 0.
- `git ls-tree -r --name-only 7a2f… | wc -l` → 50576; corpus 49559, reports 1006, ports 1, considerthese 3.
- Pristine guard in clone (`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`): exit 0, `rows 20 verified 20`, `province rows 20 matched 20`.
- Mutant A: exit 0. Mutant B: exit 0. Mutant C: exit 0. Each restored with `git checkout -q --`; final `git status --short` empty, exit 0.
- Lane (read-only): `git -C …/kotoba-shokunin rev-parse --verify --quiet master` → c48793db, exit 0; `show master:verifiers/check_sibling_census.py | wc -l` → 923, exit 0; lane working copy read at tag #A8A0, 1002 lines (finding 2).

## Residual risk and gaps

- Not run: the lane working-copy guard (finding 2); mutants on the other 19 rows (other seats' items).
- `none` is a judgement. The sweeps are literal and tree-wide (all refs), so the residual is interpretive (findings 5–6), not a missed file.
- No web sources used; none needed for this row.
