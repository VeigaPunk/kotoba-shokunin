# ReviewEntry: `corpus/knowledge/skill-overlap-levers-round51.md` against QUALITY Q12, Q14, Q23, Q26

VERDICT: FAILS. Q12 HOLDS. Q14, Q23 and Q26 FAIL on the named clauses below. The seven table quotes are on the live pages (7 of 7), and the nine line references in the "other levers" paragraph that carry numbers are right. The finding-2 negative is true on the seven pages, but the entry neither carries nor bounds its sweep, one counted row contradicts the headline, and the recheck cannot fail on drift.

Scope: lane HEAD 59903b2637689739a5b9901956301da72d0effe1 (BASE 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10). All probes ran in `/fast/scratch/hyaku/kotoba-r51/falsify/ReviewEntry/` (clone `lane/`, fetched pages `pages/`, omp doc copy `omp/`, mutant `mut1/`). The only lane write is this file. Installs or upgrades: none. Tools used: curl 8.23.0, python3 3.14.8, omp 18.12.6 (read-only `omp read`). uv 0.13.0 is present and was not used.

## Findings

### HIGH

H1. The counted Copilot CLI row is a directory setting, not a named-skill lever (Q26, Q23).
- Headline (entry lines 10-12) and finding 2 (lines 45-46, "Each removes one skill") say the lever removes a named skill.
- Row S031 (line 21) quotes `cli-command-reference.md:1300`: "Use the `ignoredSkillsLocations` setting to exclude specific directories (and their descendants) from discovery, regardless of which location above would otherwise surface them." The fetched bytes match (`pages/S031.md:1300`).
- Finding 1 (lines 42-44) puts "directory or path settings" in the "outside a scope" class, "not counted here". SKILL.md line 397 nevertheless counts S031 as "exclude the skill's directory from discovery | user or operator | removed everywhere".
- Limits line 91 concedes the lever "works per directory, not per skill name". Limits lines 86-90 say the term was added to the reviewed list so the quote could carry a backtick span (commit 34cfffb, "reviewed list +3 terms").
- The per-named-skill lever on the same page is left uncounted: `:1313` "`enable <name>` / `disable <name>` | Enable or disable a skill by name." and `:1324` `copilot skill disable my-skill`. Line 30 lists `copilot skill disable <name>` as "not counted" with no reason.
- Effect: the S031 row fails the named-skill clause, yet "7 of 7" counts it.
- Fix: quote `:1313` with key term `copilot skill disable`, add that term to `REVIEWED_LEVERS`, and keep the directory setting out of the named-skill count (or say six rows meet the headline).

H2. The `recheck:` hash step cannot fail (Q26 guard; Q12 "a recheck that runs"; Q04 intent).
- Entry line 3 runs `curl | sha256sum | grep -q || echo DRIFT` for seven pages. The loop's exit status is that of its last `grep || echo`, so it is 0 whether or not a hash matches.
- Line 14 says "the hashes in the recheck above are the bytes quoted"; line 92 says the recheck "compares content hashes". A mismatch prints a line and exits 0.
- Mutant (scratch; opencode hash set to `00000000`): output `DRIFT https://opencode.ai/docs/skills.md`, `loop-rc=0`, then `overlap levers backed 7 of 7 clients` and `quotes found on live pages 7 of 7`, `RECHECK_EXIT_WITH_DRIFT=0`.
- The checker's exit ladder (`verifiers/check_overlap_levers.py` lines 59-62) does not include the hash step.
- Fix: set a flag on DRIFT and exit 1, or move the hash comparison into `--fetch`.
- Credit: the quote clause does turn the exit code. Mutant (scratch): S030 quote "exclude" changed to "rank" gives `FETCH GitHub Copilot SDK: quote not found`, `quotes found on live pages 6 of 7`, exit 1.

### MEDIUM

M1. Finding 2's negative: sweep not carried, cited to the wrong report, bound not stated (Q14, Q23, Q26).
- Lines 45-50 say none of the levers decides between two candidates, the description is "the only lever the pages document", and the one page that ties a lever to conflicts is the Copilot SDK's § Skill conflicts. The only citation is `CriticLearning.md`. That report has no page sweep: its F2 is a reading, and its evidence section counts corpus terms at BASE only.
- Page sweeps exist in other seat reports, which I checked: `SrcCodex.md` (S021; grep at line 32, 7 lines, all lever text), `SrcCopilotSdk.md` (S030; overlap 1, conflict 3, tie-break 0, ambig 0), `SrcCopilotCli.md` (S031; sweep block lines 39-48), `SrcGemini.md` (S029; lines 71-78), `SrcOpencode.md` (S024; line 35), `SrcClaudeCode.md` (S022; F3), `SrcVSCode.md` (S025; F8). None is cited from the entry.
- My sweep agrees with the negative: case-insensitive grep over the seven scratch pages for conflict, collision, precedence, priority, tie-break, ambiguous, overlap, same name, duplicate, first found, wins, more specific, multiple skills, both match, two skills, override, higher (exit 0). Every arbitration hit is name-keyed (S021:138; S022:198-203, 278-280; S025:64, 129; S029:51-53; S030:685; S031:1282, 1298, 1302) or not arbitration (S022:49; S025:15). No hit ranks two differently named skills whose descriptions both match.
- Bound problems: (a) "the pages" is not stated as the seven pages. The SKILL.md error-pattern paragraph says round 50 read "eight client pages", and "Round-50 finding 1 stands" imports that set. (b) "The one page that ties a lever to conflicts" holds only for the heading. S031 ties its counted lever to location priority (`:1282` "first found wins for duplicate names"; `:1300` "regardless of which location above would otherwise surface them"). (c) S022:682 ("Through the Agent SDK or `claude -p`, Claude Code loads only the first skill") is a which-one-loads rule for stacked skills, outside candidate choice. It should be named as excluded.
- The same wording appears in SKILL.md (paragraph above the table; the table header is at line 394), so the defect propagates.
- Fix: write "On the seven pages (S021-S025, S029-S031) ...", cite the seven seat sweeps, and name the heading and the excluded rules.

M2. "Six of the seven rows are new to the corpus" is false as stated and has no sweep (Q14).
- Line 60. `git show 43ca0bf:corpus/SOURCES.md | grep -c -E '^\| S0(21|22|24|25|29|30|31) '` → 5. The rows for S021, S022, S024, S025 and S029 exist at BASE (their HEAD used-by cells name round-48, 49 and 50 files). Only S030 and S031 are absent.
- URL sweep (`git grep -l -F <url> 43ca0bf -- corpus SKILL.md PROVINCE.md`, exit 0): the six URLs other than S031's appear in BASE corpus files (e.g. `corpus/knowledge/skill-selection-rules-round50.md`, `corpus/lessons/round-50-verifier-spotcheck.md`). S031's URL appears in none.
- The seat's own count (`CriticLearning.md` lines 11 and 14) was "six more clients" and "6 of 7 rows as new ground". The entry turns that into a corpus claim it does not support.
- Fix: "Two rows are new (S030, S031); the lever claims for six clients are new to the corpus", with the git grep command.

M3. Several "other levers" attributions and one registry teaches cell are not located on the page named (Q23).
- "Other levers on the same pages, not counted" starts at line 28. `disabledSkills` (lines 31-32) is attributed to the config directory reference, which is not one of the seven pages; `grep -n -i disabledskills pages/S031.md` → no output, exit 1.
- "Gemini CLI `gemini skills disable` and the `skills.disabled` settings list" (line 35): `skills.disabled` appears in the lane only in the entry and in the checker's self-test fixture (`verifiers/check_overlap_levers.py` lines 850-858). `gemini skills disable` appears only in the entry. `pages/S029.md` has `/skills disable <name>` at :94 and `gemini skills list/install/uninstall` at 101-112, nothing else. Neither item is on a page the entry names.
- SOURCES.md line 44 (S031 teaches) says Copilot CLI documents "a `disabledSkills` settings key" on this command reference. The page does not.
- Effect scope: SKILL.md line 401 gives Gemini "session command disabling one named skill | removed everywhere". S029 `:94` says only "Prevents a specific skill from being used." The scope is not located, and the row's own lever text says "session command". Opencode "removed everywhere" (S024 `:153`) needs the qualifier from the same page's "Override per agent" (`:160-170`).

M4. Five of the seven source-line anchor sets are not named in their registry rows (Q12).
- Entry lines 1-2 name line ranges per row. The SOURCES rows (lines 34-44) name different ranges for five rows: S021 (entry `183-189, 218`; registry `md:37-40, 43-44, 91, 98-99`); S022 (entry `549, 577, 886, 894-907`; registry `389, 390, 114, 196-208, 682, 1190-1195, 1205-1213`); S024 (entry `133-156`; registry `29-48, 70-73, 108-129, 223-231`); S025 (entry `150-151, 289-296`; registry `148, 302, 308, 64, 129`); S029 (entry `94`; registry `20-24, 37-47, 49-53`, plus best-practices 8-17).
- Counts over SOURCES lines 34-44 for `150-151`, `289-296`, `183-189`, `133-156`, `549`, `886`, `894-907` and `94` → 0 each. S030 and S031 agree with the entry.
- The content is supported: the seat reports quote these lines (e.g. `SrcVSCode.md`, `SrcGemini.md`, `SrcCodex.md`). But SOURCES rule 2 bars in-place anchor edits (quoted in `SrcCopilotCli.md`, line 68), so the fix is a superseding row or citing only registry-named lines.

### LOW

L1. The approximating check carries no run counterexamples (Q23).
- The counter is a key-term check against a frozen list (`REVIEWED_LEVERS`, lines 142-152). Lines 83-91 call the list a reviewer's judgment but give no misses or over-flags. The S031 row supplies both, unremarked: an over-flag (H1, a directory setting counted) and a miss (`copilot skill disable` not counted).
- The self-test has no same-name or location-precedence mutant: `grep -n -i -E 'precedence|same.name|higher' verifiers/check_overlap_levers.py` → no output, exit 1. `CriticLearning.md` F6 asked for one.
- Self-test: `python3 -B verifiers/check_overlap_levers.py --self-test` → "0 failures / 22 assertions", exit 0.
- Small point: the S025 row (entry line 22) quotes a lead-in. The effect ("stops the agent loading the skill on its own; the `/` command still works") is at `:151` and `:295`, cited in the source line but not quoted.

L2. The omp negative has a narrow sweep and no scope (Q14).
- Line 74: "omp documents no tie-break either." `omp/LeverOmp.md` §1 sweeps the binary's strings for six phrases only; none of conflict, overlap, ambiguity, precedence or tie-break is in that list.
- My sweep of `omp read omp://skills.md` (omp/18.12.6; 258 lines; 17971 bytes; sha256 `bfda0415…`; exit 0) found precedence text at lines 81, 85-104, 126-135 and 258. All are name-keyed or provider-keyed; line 104 reads "Capability dedup key is skill name; the first item with a given name wins." The claim holds only for differently named skills. The entry should say that and cite the sweep.

## What holds (calibration)
- Line 1 names all seven S### rows, with URLs that match SOURCES exactly (without the `.md` suffix). `verified-at` (line 2) is present.
- All seven table quotes sit verbatim at the cited lines (S030 :809; S031 :1300; S025 :289; S022 :886; S024 :230; S029 :94; S021 :218). The line-number checks in the table are right.
- Finding 4's correction holds: S022 `:1194` "Make the description more specific" and `:1195` "Add `disable-model-invocation: true` if you only want manual invocation".
- The hash values match a fresh fetch (15:17:28-30Z, curl -sS -L, all HTTP 200): S030 35455 B `64856ff4…`; S031 461944 B `c61997ef…`; S025 22871 B `de5ba34f…`; S022 111557 B `cdfcb0df…`; S024 5365 B `f10ced73…`; S029 5763 B `8e1b4cbe…`; S021 11035 B `ed6e324f…`. The "15:08Z re-fetch" claim is corroborated.
- Limits lines 83-84 disclose that these are documentation statements, not measured behaviour.

## Q verdicts
| criterion | verdict | basis |
|---|---|---|
| Q12 | HOLDS | source line names seven S### rows with matching URLs; verified-at present; recheck runs (exit 0). Caveats: H2 (drift cannot fail), M4 (anchors). |
| Q14 | FAILS | M1 (finding-2 negative cited to a report with no sweep, unbounded); M2 (false absence claim, no sweep); L2 (omp sweep narrow, unscoped). |
| Q23 | FAILS | H1 (S031 attributed as a per-skill lever); M3 (unlocated or misplaced attributions, including the SOURCES S031 teaches cell); L1 (no run counterexamples). |
| Q26 | FAILS | H1 (named-skill clause not turned on for S031); H2 (hash clause, guard exit does not change); M1 (bound "the pages" not stated); M2 (absence clause). Surviving clauses: quotes on live pages; the counter fails on the quote mutant. |

Finding 2, direct answers: (1) The sweep that supports "none decides between two candidates" is in the seat reports for all seven pages (listed in M1), not in `CriticLearning.md`, and my own sweep agrees. (2) The claim is not bounded to seven pages in the text. It says "the pages", and round 50's sentence was about eight.

## Commands and exit codes
- `git clone -q <lane> <scratch>/lane && git -C <scratch>/lane checkout -q 59903b26…`: exit 0; `rev-parse HEAD` = 59903b2637689739a5b9901956301da72d0effe1.
- Recheck (scratch clone, 15:15:40Z, 3.2 s): seven `curl|sha256sum|grep` lines printed no DRIFT; then `python3 -B verifiers/check_overlap_levers.py --fetch` printed seven `BACKED` lines, `overlap levers backed 7 of 7 clients`, seven `FETCH … quote found` lines, `quotes found on live pages 7 of 7`. `RECHECK_EXIT=0`. A second run (about 15:22) gave the same result, `RECHECK_EXIT_HEAD=0`.
- Drift mutant (H2): `loop-rc=0`, `DRIFT https://opencode.ai/docs/skills.md`, `RECHECK_EXIT_WITH_DRIFT=0`.
- Quote mutant (`mut1/`, S030 "exclude"→"rank"): `quotes found on live pages 6 of 7`, `MUTANT_EXIT=1`. Control `--root lane` (no fetch): `overlap levers backed 7 of 7 clients`, `CONTROL_EXIT=0`.
- `--self-test`: "0 failures / 22 assertions", exit 0.
- `git show 43ca0bf:corpus/SOURCES.md | grep -c -E '^\| S0(21|22|24|25|29|30|31) '` → 5. `git grep -l -F` for the seven URLs at 43ca0bf: exit 0 each; S031's URL has no match.
- `grep -n -i disabledskills pages/S031.md` → no output, exit 1. `grep -rn -F skills.disabled lane --exclude-dir=.git` → entry line 35 and checker lines 850, 851, 858. `grep -rn -F 'gemini skills disable' lane` → entry line 35 only.
- Conflict sweep over the seven pages (case-insensitive, 18 terms): exit 0; hits as in M1.
- `omp --version` → `omp/18.12.6`, exit 0. `omp read omp://skills.md` → exit 0, 258 lines, 17971 bytes; conflict sweep exit 0 (hits as in L2).
- SOURCES anchor sweep for lines 34-44 (`150-151`, `289-296`, `183-189`, `133-156`, `549`, `886`, `894-907`, `94`) → 0 each.

## Residual risk and gaps
- Not opened: the config directory reference (where `disabledSkills` actually sits), the scribe's copy of Gemini `cli-reference.md:130`, Claude Code `paths` lines, the round-51 plan, and the lesson's `## Gate` section.
- No client or model run. Effects are documentary; the entry says so. I did not test whether `copilot skill disable` or `/skills disable` persist across sessions.
- The omp check covers the installed binary's shipped docs only; omp code-only claims in `LeverOmp.md` §2 are not re-verified.
- The hash comparison uses an 8-character prefix. I confirmed full sha256 equality for the seven pages at 15:17Z only.
