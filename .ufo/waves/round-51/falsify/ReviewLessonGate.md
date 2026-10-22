# ReviewLessonGate: round-51 lesson (M33, M34, Q27, Gate, used-by log)

Verdict: HOLDS-BOUNDED. Q27 is shown able to fail on the round-50 record, the Gate numbers, pins, quotes and the used-by log all hold, but four statements do not hold as written: the M34 class text and the Q27 reason for D2D4Wording, the S031 row's `disabledSkills` clause, and the S024 reject reason (the W04 part). Correct these before the lesson is treated as accurate.

Scope: `corpus/lessons/round-51.md` (M33/M34, Q27 demonstration, `## Gate`, used-by log), `corpus/QUALITY.md` Q27 row, and `corpus/SOURCES.md` diff from 43ca0bfb to 59903b26. Read-only: nothing in the lane was edited. Peers were not messaged.

## Findings (most serious first)

1. **Medium. M34 class text and Q27's reason are false for D2D4Wording.** M34 says "a seat recorded as cancelled wrote its report after the round report was filed". That is true for DescDraft only. D2D4Wording was first committed in lane commit 1cb2e65 at 2026-10-22 10:51:01 -0300, with 169 lines. That is 68 s before the fleet report was filed (cc7d642, 10:52:09 -0300). Its last edit (written 10:51:16, 26 insertions and 1 deletion) was committed in 2abd290 at 10:51:22. The lesson's Q27 paragraph says "both seats wrote files after that point", and D1 says "committed in 2abd290, 6 s later". Both are wrong for D2D4Wording. The seat report `.ufo/waves/round-51/build/MineMistake.md` § Q27 repeats the error; its evidence (`git show 2abd290 --numstat`) missed 1cb2e65. The round-50 record still fails Q27 for D2D4Wording, but for a different reason: the record says "without a report" while the file had been in the lane 68 s before filing. Fix: M34 should say that DescDraft was written after the filing. D1 should record the 1cb2e65 first commit.

2. **Medium. The Q27 sweep failure has three causes; the lesson names one.** Line 112-113 of the round-50 report fails Q27 because (a) the sweep ran at or before the 10:52:09 filing, and DescDraft was written at 10:52:19; (b) it prints no command, and Q27 requires "with its command printed"; (c) it names only the fleet root, but the untracked DescDraft sits in the lane's `.ufo/waves/round-50/build/`, which is a directory a seat writes to. So "nothing from round-50 seats" is unsupported for the lane. The Q27 demonstration holds; its explanation should list (a) to (c).

3. **High for one row. S031 teaches cell overreaches its page.** S031 says Copilot CLI "documents ... a `disabledSkills` settings key". The fetched S031 page (461,944 B, sha256 `c61997ef…`) has zero occurrences of `disabledSkills`. A case-insensitive search for `disabled[ _-]?skill` finds only line 21, the description of the `copilot skill` command. The key is on the SDK page (S030, lines 288, 697, 706, 809), so the row misattributes it. The clause "while `/SKILL-NAME` stays available" is also not on the page; line 1277 gives only the default of `user-invocable`. The Gate's quote (line 1300, 22 words, verified) grounds only the `ignoredSkillsLocations` clause. Fix: delete the `disabledSkills` clause and the gloss, or cite the page that actually holds them.

4. **Medium. S024 reject reason cites a census rule that does not fire.** The reason says "a superseding row with the same URL would add a W04 duplicate-URL warning". In `scripts/sources-census.sh`, the duplicate test is keyed on URL plus scope (lines 643-645). W04 fires only when that URL-and-scope pair is new, and it is a warning that "does not affect clean lanes" (line 33). E04 is exempted when teaches opens `supersedes S0NN` (line 648). So a superseding row in the same scope triggers neither check. Contract rule 2 (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` lines 49-51) names the superseding row as the route for a correction. The page-line part of this reject holds (opencode `skills.md:133-156` and `:230`, verified). Fix: write the superseding row the contract prescribes, or state the real reason, which is a judgment that the narrower teaches cell stays.

5. **Low. M33 fix cell misplaces the erratum.** M33 says "Round 51 appends the correction to the round-50 Gate". `git diff --stat 43ca0bfb 59903b26 -- corpus/lessons/round-50.md` prints nothing, so round-50.md is unchanged. The erratum sits in round-51.md's `## Gate`, as the lesson's own text says. Fix the M33 wording.

6. **Low. Two rejects cite no skills-page line for "duplicates the skills page".** Claude `permissions.md:138` is cited alone; the skills page lines are `skills.md:855-866` ("Allow or deny specific skills", `Skill(deploy *)`), verified. Codex `config-reference.md:381-393` is cited alone; the duplicate is `build-skills.md:183-189` (`[[skills.config]]`, `enabled = false`), verified. The omp reject carries no page line, but its reason is an access fact (`omp://` is not a fetchable URL), not a claim about page content, so the M33 class does not apply.

## Verified and holding

M33 and M34 pointers (each re-read or recomputed):
- `corpus/lessons/round-50.md:44-45` reads "the Copilot SDK skills page (provider catalogs, not" / "SKILL.md routing)". Line 18 (M32 fix) reads "the last seat returns". Both hold.
- Copilot SDK page: line 11, line 289 and lines 809-810 carry the quoted sentences exactly; line 805 is "### Skill conflicts". Hold.
- `.ufo/reports/round-50/kotoba.md:96-97` and `:112` carry the quoted text. Hold.
- Fleet commit cc7d642 is 2026-10-22 10:52:09 -0300. `.ufo/watchdog.log:705` is "10:52:49 complete kotoba round=50". Hold.
- D2D4Wording.md: 18,592 B, sha256 `bb7679ad…`, mtime 10:51:16.487; blob `c26b2465…` at 43ca0bfb. Hold.
- DescDraft.md: 10,079 B, sha256 `0181a459…`, mtime 10:52:19.554; absent at 43ca0bfb; first tracked in e621902 (2026-10-22 12:11:48 -0300). Hold.
- `.ufo/waves/round-50/build-spec.json` has 33 items. At 43ca0bfb the build and falsify folders hold 70 `.md` seat reports (32 build, 38 falsify). With DescDraft that is 71 = 33 + 38, so D1's count holds.
- Q27 is the single added row (QUALITY.md line 38; the diff adds one line).
- Q27 applied to the record: clause one fails on DescDraft (written after filing; see finding 1), and clause two fails on timing and the missing command (finding 2).

Gate, rule 1 (new rows):
- S030: URL https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills; access 2026-10-22T14:19:11Z (anchor cell); quote "Use `disabledSkills` to exclude conflicting skills" is 6 words, at line 809. My fetch at 15:18:44Z: HTTP 200, 35,455 B, sha256 `64856ff4…`, matches. Pins verified: 11, 177-179, 252, 262, 288-289, 648, 683-685 (685 is the name-keyed replacement rule), 697/700/703/706, 711-724, 805-810. Its negative claim (no rule for choosing between two differently named skills) holds on my sweep of 58 matching lines.
- S031: URL https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference; access 2026-10-22T14:19:21Z (anchor cell); quote 22 words, exact match at line 1300. My fetch at 15:18:45Z: HTTP 200, 461,944 B, sha256 `c61997ef…`, matches. Pins verified: 1269-1279, 1278 (5 pipes), 1282 ("first found wins"), 1300, 1302, 1324 (`copilot skill disable`). The row's teaches cell itself carries no quote; the Gate does, which meets rule 1 for the quoted clause only (finding 3).
- Re-opened pages S021, S022, S024, S025, S029, each re-fetched at 15:21Z: HTTP 200, hashes `ed6e324f…`, `cdfcb0df…`, `f10ced73…`, `de5ba34f…`, `8e1b4cbe…`, all match. Lines cited in the Gate hold: build-skills 218, skills 886, opencode 230, agent-skills 289, skills.md 94.
- Reject quotes checked: Gemini skills 75 and 94 (75 states the user-scope default, 94 the effect); VS Code agent-skills 150 ("hide the skill from the `/` menu while still allowing the agent to load it automatically"); Claude skills 390 ("Appended to `description` in the skill listing"); VS Code manage-ai-settings 294 and Gemini settings 189 (both global switches); opencode skills 143 and 153 (`deny`), verified; Copilot CLI 1278 (table row with pipes). Fetched 15:21:38-15:21:40Z; hashes match the recorded values for all nine secondary and cited pages.

used-by, rule 2:
- `git --no-pager diff --no-ext-diff --no-textconv 43ca0bfb 59903b26 -- corpus/SOURCES.md` shows 7 insertions and 5 deletions. The changed rows are S021, S022, S024, S025, S029, and each differs only in used-by, by an appended ", corpus/knowledge/skill-overlap-levers-round51.md". Their old values match the lesson's log exactly. Status, opened and recheck are unchanged in all five. S030 and S031 are new rows.

## Residual risk and gaps

- The round-51 sweep (D1 says it runs after the last seat write, output in the round-51 report) was not checked. That report is not written yet.
- D1's claim that DescDraft is misdated as `956ee167` (landed at `542f515`) was not checked.
- The seats' own times (M33's 14:19:50Z fetch) were not independently checked beyond the page hashes.
- Cancellation timing for D2D4Wording is unknown. I did not search for a cancel record in the watchdog log beyond lines 699-710.
- Knowledge entry lines 94-96 say the secondary pages "add only all-or-nothing switches". The seat's own table lists four duplicate per-skill levers, so the summary is loose. Not in my scope; noted for the integrator.

## Evidence (commands and exit codes)

- Lane reads, all read-only, through a Python subprocess calling `git -C <lane>`: `show`, `diff`, `log`, `ls-tree`, `diff --stat`. Every call returned exit 0.
- `git log --format='%h %ci %s' -- .ufo/waves/round-50/build/D2D4Wording.md` gave 2abd290 at 10:51:22 and 1cb2e65 at 10:51:01. `git ls-tree 1cb2e65 .ufo/waves/round-50/build/D2D4Wording.md` gave blob `2b46edb2…`. `git show --numstat 2abd290` gave 26 and 1 (per the seat's own check).
- `git show 43ca0bfb:…/D2D4Wording.md | sha256sum` gave `bb7679ad…`; `| wc -c` gave 18592. `git show 59903b26:…/DescDraft.md | sha256sum` gave `0181a459…`; `| wc -c` gave 10079. Both exit 0.
- `git -C /home/vgpnk/Projects/shokunin log -1 --format='%h %ci %s' cc7d642` gave 2026-10-22 10:52:09 -0300, exit 0.
- `python3 -c` reading `.ufo/waves/round-50/build-spec.json` gave 33 items, exit 0.
- `git ls-tree -r --name-only 43ca0bfb -- .ufo/waves/round-50/build .ufo/waves/round-50/falsify`: 72 paths, of which 70 end in `.md` (the other two are `swarm-registry.json`), exit 0.
- `git ls-tree 43ca0bfb -- .ufo/waves/round-50/build/DescDraft.md` printed nothing; `git log -- …/DescDraft.md` listed only e621902, exit 0.
- `curl -sS -L -w '%{http_code} %{size_download}'` for 11 pages: each exit 0, HTTP 200. Byte counts and sha256 as in the Gate section above. Scratch copies are in `/fast/scratch/hyaku/kotoba-r51/falsify/ReviewLessonGate/`.
- Python searches on the fetched pages: S031 `disabledSkills` count 0 (exit 0); S031 `disabled[ _-]?skill` case-insensitive gives line 21 only; S030 rule-term sweep gives 58 matching lines.
- `scripts/sources-census.sh` lines 612-660 read through the read tool (lines 33, 643-653 for W04 and E04).
- Contract `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` lines 45-51 read.
- Tools: none installed or upgraded. `curl`, `git`, and `python3` were already present.
