# RowMori: C1 falsify of census row `mori` and PROVINCE.md § Adjacent row 51

**Verdict: HOLDS-BOUNDED.** Applies to census row `mori` (branch `master`, commit 28b79d3d1b76824f0c825aabe6cb6c5dc49961bf, classification `none`) and PROVINCE.md § Adjacent row `mori`, at the pinned bytes, under the census § Classification rule. `none` holds: no committed mori surface claims kotoba's core, and no committed surface on either side states a split. Bounds: (F1) the boundary note's "no claim on kotoba ground" leaves out a shared dispatch-artifact overlap that mori and kotoba both touch; (F2) the guard does not check the mechanical cells it is documented to check. The mechanical values for mori are correct.

Judged bytes: kotoba-shokunin master `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad` (base `a5adc146`). Sibling read only: `git -C mori-shokunin` with rev-parse, cat-file, show, ls-tree, grep, log, branch, merge-base. Private clone for the guard and mutants: `/fast/scratch/hyaku/kotoba-r49/falsify/RowMori/kotoba` at c48793db. Tool installs: none.

## Findings (severity order)

**F1, medium. The boundary note omits a shared dispatch-artifact overlap, so "no claim on kotoba ground" is one-sided.**
- Mori's committed PROVINCE.md:145-148 claims a settlement scan "for every `ufo-swarm-wave-dispatch-v1` file under a lane's `.ufo/waves/`", reading each member's `Report:` trailer path. The seat's item 7 says no tool "reads another lane's … prompt text". That is wrong as capability: `tools/mori-wave-settlement.py:36` (REPORT_RE) and `:214` (`_trailer`) read the trailer from any `--lane-root`.
- Run on the pinned tool (extracted from `28b79d3d:tools/`, sha256 `79e7f9de…`): `python3 -I mori-wave-settlement.py scan --lane-root <kotoba clone> --out …` → exit 1; members 272, present 248, missing 24, waves 5; includes `.ufo/waves/round-49/build-dispatch.json` (settled, present 36).
- Ledger: PROVINCE.md:134-138 says "one ledger row per whole-wave task call". `tools/mori-dispatch-ledger.py:556-562` takes `--repo` as any path; `_validate_repo_and_rev` (:84-89) checks only that the rev exists. SKILL.md:180 documents `verify --repo <repo>`. Run: `python3 -I mori-dispatch-ledger.py bind --repo <kotoba clone> --rev c48793db… --dispatch .ufo/waves/round-49/build-dispatch.json` → exit 0, `tasks_count` 36, `payload_bytes` 87100, PAYLOAD_BOUND. The "mori's own waves only" limit is a usage convention, not code.
- Kotoba side, committed: SKILL.md:128-129 (dispatch.04/08 executed by `verifiers/verify_dispatch_prompts.py`); SKILL.md:410-412 (population `.ufo/prompts/*-round-*.md`, 50 files at round 9); corpus/README.md:21 (applied to 43 `.ufo/prompts/*.md`); corpus/README.md:92-94 ("executes them over `.ufo/prompts/`"). The fleet directory holds 16 mori round prompts now: `ls …/.ufo/prompts | grep -c '^mori-round-'` → 16.
- No stated split exists on either side, so the literal rule gives `none`. The row still says mori has no claim on kotoba ground, while both lanes read the same dispatch lineage and neither names the other's use. Integrator decision: record the overlap in the mori boundary note, or rule whether artifact-level overlap without a stated split counts as adjacency. This is the closest call to `adjacent` in the round.

**F2, medium. The guard does not check the mechanical cells, though its header says it does.**
- `verifiers/check_sibling_census.py:10-14` says each row carries "whether the sibling's description carries an arbitration clause". The code reads `values["arbitration"]` only in the empty-cell test (:383). `names kotoba` and `branch` get the same treatment.
- Mutant (scratch copy; mori row changed to branch `main`, names kotoba `yes`, arbitration `no`): `python3 -B verifiers/check_sibling_census.py <mutant> --province PROVINCE.md` → "rows 20 verified 20 / province rows 20 matched 20", exit 0. The guard passes a wrong row.
- Positive control (quote word `progressing` → `progressed`): same command → "FAIL row 15 (census line 77) (lane mori): quote not found at PROVINCE.md:3 (+/-2 lines)", exit 1. The quote check is live.
- Unmutated census at c48793db: same command → exit 0, "rows 20 verified 20", "province rows 20 matched 20". The census Counts section (lines 88-98) depends on the unguarded columns.

**F3, low. Branch and HEAD evidence is stale; classification not contradicted at the tip.**
- `git -C mori-shokunin rev-parse master` → e5e1b7bc1c8dd3dc838585f5ebacfd1bc39e1098 (exit 0), not 28b79d3d (seat item 1). `git rev-list --count 28b79d3d..master` → 26. `git merge-base --is-ancestor 28b79d3d master` → exit 0. `symbolic-ref -q HEAD` → exit 1 (detached, now at e5e1b7bc). The newest of the 26 is 2026-10-22 08:14:02 -0300.
- Census Limits (census line 128) names kake, kama and tameshi as moved pins; mori also moved after its seat read it.
- Post-pin commits 8ef481e and 1888bc6 change mori's SKILL.md and PROVINCE.md (round-25 harness-capacity text, FR15 note) and add `tools/mori-job-runway.py`. `git log -p 28b79d3d..master -- SKILL.md PROVINCE.md tools corpus | grep -ci kotoba` → 0. At the tip, `git grep -ci kotoba e5e1b7bc… -- SKILL.md PROVINCE.md AGENTS.md corpus tools` → 37 lines, unchanged.

**F4, low. The seat's sweep covered top-level names, not contents. Nothing it missed changes the row.**
- `git show <c>:<dir>` prints a tree listing, so the "top-level sweep" never read corpus/, tools/, considerthese/ or .ufo/. Its 45 reproduces: `git ls-tree --name-only C | while read f; do git show C:$f; done | grep -cEi 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'` → 45, exit 0.
- Uncovered trees, read now: `git grep -n -i kotoba C -- corpus tools considerthese | wc -l` → 37 lines, all lane-id roster, census or log data (e.g. `corpus/knowledge/roster-truth-r12.md:9`). `considerthese/2026-10-19..21.md` (22-24 lines each) mention only mori's own SKILL.md.
- `git grep -ci prompt C -- ':!.ufo' | awk` → 34 lines in 21 files. The seat's "3 prompt hits, all LOG.md prose" is top-level only. Corpus lessons (round-13, 18, 23, 24 verifier spot-checks) check mori's own dispatched round prompts (round-18 lesson line 30: §1-§5 against `templates/round-prompt.md`). Self-scoped, so not contested; recorded so the sweep is not misread.
- `tools/mori-routed-check.py:57-64` (R2_SCAN_SCOPE, applied at :243 to whatever `--repo` names) scans for privacy-clearance wording. Intent is mori's own repo (SKILL.md:642). Not a craft audit; the capability is repo-generic.
- Tools grep for `SKILL\.md|AGENTS\.md|frontmatter|prompt`, excluding GIT_TERMINAL_PROMPT, returns only mori's own SKILL.md references (`tools/mori-round13-regressions.py`, `REPO` = the tool's own tree at :167) and one comment (`mori-misroot-sweep.py:93`).

**F5, low. The seat's base cross-check is a paraphrase, not verbatim.** `git -C kotoba-shokunin show a5adc146:PROVINCE.md | sed -n 34p` → "… mori (fleet observability), kama (model serving) — no overlap observed." The seat's quote "fleet observability — no overlap observed" joins two parts of the line. Not in the row; no effect on the verdict.

## Checks as asked

1. **Commit and branch.** `git rev-parse --verify 28b79d3d…^{commit}` → exit 0; `cat-file -t` → commit, exit 0; `branch -a --contains` lists master and origin/master; `merge-base --is-ancestor` → exit 0. The `master` cell holds as containment at read time, stale as tip (F3).
2. **Scope quote.** PROVINCE.md:3 = "**Domain:** fleet & host observability (森) — whether the fleet, its waves and"; :4 = "its host are alive and progressing." Joined and collapsed, this matches the census quote byte for byte (U+2014 em dash, 森 U+68EE). The guard locates it within ±2 lines. Holds.
3. **Classification `none`.** Holds under the stated rule.
   - Contested: no committed mori surface claims writing or auditing other lanes' SKILL.md, AGENTS.md or prompt wording. Tools that read other lanes' dispatch text (F1) grade settlement and bind payloads; neither judges wording. Mori's Refuses list (PROVINCE.md:12-16) routes dispatch to kumitate, OS state to tsukuroi, endpoints to kama, credentials to kagi. Kotoba is not named.
   - Adjacent: no stated split. Pinned SKILL.md has 0 `kotoba` (case-insensitive: `git show C:SKILL.md | grep -ci kotoba` → 0) and PROVINCE.md has 0. Kotoba's committed surfaces name mori only at PROVINCE.md:51 and census line 77.
4. **Mechanical cells, re-derived from `git show 28b79d3d:SKILL.md`, lines 1-5.**
   - `names kotoba` = no (case-insensitive count 0).
   - `arbitration` = kama, kumitate, tsukuroi. Description line 3 names exactly those three (anti-trigger clause). `mori` appears only in line 2 (`name: mori-shokunin`), the lane's own name, and is correctly excluded. Census cell matches. Neither cell is checked by the guard (F2).
5. **PROVINCE.md row 51**: "fleet and host observability; no claim on kotoba ground".
   - "fleet and host observability" matches PROVINCE.md:3.
   - Commit matches the census row; the guard's PROVINCE cross-check passes ("province rows 20 matched 20").
   - "no claim on kotoba ground" is accurate for craft. F1 covers the artifact overlap it omits.
   - The note has no line citations.

## Evidence (commands and exit codes, verbatim where stated)

- Pinned bytes: `git show C:SKILL.md | sha256sum` → b043f709…aa04d68 (matches seat); `git show C:PROVINCE.md | sha256sum` → 81325bde…23e53540 (matches seat); line/byte counts 642/75830 and 290/28789.
- `git ls-tree --name-only C` → 13 entries (matches seat). `git ls-tree --name-only C tools/` → 24 entries, no `verifiers/`.
- Guard at c48793db: exit 0, "rows 20 verified 20", "province rows 20 matched 20". Mutant (F2): exit 0. Control (F2): exit 1.
- Kotoba mentions in mori's `.ufo/` (wave records, not scope): 214 lines, `git grep -c -i kotoba C -- .ufo` summed.
- Kotoba-side `mori` mentions, judged commit: `git -C kotoba-shokunin grep -n -w -i mori c48793db…` → 180 lines in 33 files; scope surfaces only PROVINCE.md:51 and census line 77.
- Per-term counts (seat's terms, top-level loop): SKILL.md 23, trigger 16, prompt 3, description 3, AGENTS.md 1, frontmatter 0, kotoba 0 (each reproduced; the `kotoba` grep exits 1 at zero matches).
- Post-pin: `git rev-list --count 28b79d3d..master` → 26; `git log -p 28b79d3d..master -- SKILL.md PROVINCE.md tools corpus | grep -ci kotoba` → 0.
- Round-20 live fleet record `.ufo/waves/round-20/evidence/c2-live-fleet-final.json`: kotoba-shokunin row shows `members` 0, `waves` 0, `exit` 0 at that time. Kotoba now has dispatch files (F1).
- Guard source: `verifiers/check_sibling_census.py:383` (empty-cell test only), `:325-326` (cell names), `:10-14` (header claim).

## Residual risk and verification gaps

- Not checked: whether mori ever ran `verify --repo` or `scan --lane-root` against a non-mori repo in committed evidence. I found 9 mori-own `--repo` uses and placeholders only, so no committed run of that kind.
- Not run: `verify_dispatch_prompts.py --box-proof` (another seat's claim).
- Judgment: `none` versus `adjacent` depends on whether artifact-level overlap without a stated split counts (F1). I read the rule as requiring a stated split and found none. A different reading of "state a split" would reclassify mori.
- No lane file was edited. This report is the only file written in the lane.
