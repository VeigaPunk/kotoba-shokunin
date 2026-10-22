# ReviewSkillWording: round-51 SKILL.md wording (falsify wave)

Verdict: FAILS (wording only; no gate result changes). The box-proof sentence (SKILL.md:135-139) HOLDS. The error-pattern rewrite (SKILL.md:377-384) HOLDS-BOUNDED: the eight-page bound is kept and the "documented remedy" clause is gone. The new overlap-levers block (SKILL.md:386-402) FAILS: three sentences or cells there are wider than their sources.

Scope: every changed line of SKILL.md in `git diff 43ca0bfb 59903b26 -- SKILL.md` (30 insertions, 7 deletions; hunks at 132 and 370). Judged at HEAD 59903b2637689739a5b9901956301da72d0effe1 in a private clone under the fleet shape: `fleet/kotoba-shokunin` is the clone, `fleet/.ufo` and `fleet/PROTOCOL.md` are copies, 47 fleet entries are symlinks, and `.git` and `.jj` are not linked. "Repro" below means a run in a scratch copy, with the delegate file restored and compared byte for byte to HEAD afterwards.

## Findings, by severity

### Medium

**M1. "Each lever removes one skill" (SKILL.md:388) is wider than its source and contradicts the entry's own limits.**
- The Copilot CLI row (SKILL.md:397) counts `ignoredSkillsLocations`, which excludes "specific directories (and their descendants)" (`corpus/knowledge/skill-overlap-levers-round51.md:21`, quoting `cli-command-reference.md:1300`). That removes every skill under a directory, not one named skill.
- The entry says so: "The Copilot CLI row's lever works per directory, not per skill name" (entry line 91).
- The entry's Finding 1 (lines 41-44) puts "directory or path settings" under "outside a scope (not counted here)". The table counts this directory setting as "removed everywhere". The "outside a scope" category in the SKILL sentence has no row in the table.
- The 7-of-7 count depends on this row. Whether S031 should count is a judgment for the L1; I did not measure it.
- Fix: state that S031 works per directory, or drop the "one skill" sentence for S031 and recount.

**M2. The effect cells say "removed everywhere" where the same row says "session" or "user scope".**
- SKILL.md:396 (Copilot SDK): the row says "the session's disabled skills". The seat report says the lever is "session-creation config in the SDK call — not a settings file" (`.ufo/waves/round-51/build/SrcCopilotSdk.md:32`).
- SKILL.md:401 (Gemini CLI): the row says "session command". The Gemini page says `/skills disable` and `/skills enable` "default to the `user` scope", with `--scope workspace` for project scope (`skills.md:75`, quoted in `SrcGemini.md:79`).
- SKILL.md:397 (Copilot CLI): per directory (M1).
- SKILL.md:400 (opencode): "hidden from agents" supports "removed everywhere".
- Fix: put the scope in the effect cell (session; user by default; directory) and keep "everywhere" only where the quote supports it.

**M3. "where the description is still the only lever" (SKILL.md:389) drops the bound the entry states.**
- The entry says "the description is still the only lever the pages document" (entry lines 46-47).
- The error-pattern rewrite keeps its own bound ("On the eight client pages that entry read", SKILL.md:378). This sentence does not, so it reads as a claim about every client.
- Fix: restore "the pages read document". This is the smallest of the three Medium items.

### Low

**L1. The documented-rules sentence omits an exception the same round records.** SKILL.md:380-381 says "the documented rules decide between copies of one name, component types or configuration sources". `corpus/README.md:72` (same round) adds "except Claude Code's built-in catch-all agent (fit-based default)", and `corpus/knowledge/skill-selection-rules-round50.md:37-39` (Finding 2) says the same. Add the exception. Low, because the catch-all is a subagent rule, not a skill-matching rule.

**L2. "the eight client pages" (SKILL.md:378) is one client short.** The entry says "eight more pages from five clients" (`skill-selection-rules-round50.md:9`). The eighth page is S019, "Anthropic best practices" (line 25). The count of eight is right. Suggest: "the eight pages that entry read (five clients and one Anthropic best-practices page)".

**L3. The "use one when" advice (SKILL.md:390-392) leaves out two limits the entry states.**
- "when you do not own the other skill": Finding 3 (entry lines 51-55) says a non-owner can use only the user, operator or app-held levers. The table's held-by column is never tied to this advice.
- "the removed skill also stops firing on prompts only it matches": for the three automatic-choice-off rows (VS Code, Claude Code, Codex) the skill still runs when a person invokes it. "Stops firing automatically" is the accurate phrase.

**L4. Omission, not a wider claim (box-proof paragraph).** The sentence cites F1-F3 of the round-50 review only. F5 is still live at HEAD: a non-UTF-8 `--help` ends the gate with `UnicodeDecodeError`, exit 1, no JSON (repro E). F4 (the red detail drops the instrument's stderr reason) was not re-run. The sentence does not claim completeness, so no edit is required.

## Holds, item by item

**H1. Box-proof sentence (SKILL.md:135-139): HOLDS.** Each clause traced to code and to a run at HEAD:
- "runs `--box-proof` only when the `--help` probe advertises the flag": `verifiers/verify_skill_checklist.py:999-1002` returns "not run" unless `supports_box_proof` (lines 960-973) finds the flag in stdout or stderr. Repro C (flag hidden from help): exit 0, PASS, "no --box-proof support (the --help probe does not advertise --box-proof), not run". Repro D (flag advertised, exit 1): exit 1, FAIL.
- "times out": lines 967-968. Background run at HEAD with a `--help` that sleeps: exit 0, PASS, "no --box-proof support (the --help probe timed out), not run" (154 s wall; the probe timeout is 120 s).
- "cannot execute": lines 969-970 (OSError) and `instrument_command` returns None for a non-executable file with no suffix (lines 955-957, 996-998). Direct call `supports_box_proof(['/nonexistent/interp-xyz'])` returns `(False, "the --help probe failed ([Errno 2] ...)")`.
- "fails open there": same as repro C.
- "a relative `--map` run from another directory gives a false red": repro B (relative map, run from one directory up): exit 1, FAIL "failed its --box-proof (exit 2): boxes proven 0". Repro A (absolute map, same cwd): exit 0, PASS. Cause: `main` keeps `Path(args.map)` unresolved (line 2534), and the child runs with `cwd=base` (line 1008).
- "(F1-F3, carried)": `git diff --stat 43ca0bfb 59903b26 -- verifiers/verify_skill_checklist.py` is empty, so the gate code the round-50 review measured is unchanged.

**H2. Error-pattern rewrite (SKILL.md:377-384): HOLDS-BOUNDED.** The bound and the clause removal hold; L1 and L2 are wording bounds.
- The eight-page bound is kept: "On the eight client pages that entry read" (line 378) matches "The negative in finding 1 covers these eight pages only" (entry line 69) and `corpus/README.md:72`.
- The superseded clause is gone: `grep -c -i 'documented remedy' SKILL.md` prints 0 (exit 1); `grep -c -i 'more specific'` prints 0 (exit 1). The entry records finding 4 as superseded (lines 92-98), which is where that record belongs.
- "no client documents a rule between two differently named, author-written skills whose descriptions both match" matches Finding 1 word for word (entry lines 29-30).
- "stay under 1,024 characters": the gate reads "description 1019 chars" (`trigger.frontmatter_parses`, PASS).
- "name the neighbour and the split in the description (`trigger.05`)": the box at SKILL.md:218-221 reads "Overlapping sibling skills are named concretely with an arbitration rule in the description". Matches.

**H3. The counter the table cites: HOLDS.** `python3 -B verifiers/check_overlap_levers.py` (no `--fetch`) exits 0 and prints "overlap levers backed 7 of 7 clients". The Codex "skill author" holder matches the per-skill `agents/openai.yaml` file (`SrcCodex.md:23`).

## Verification gaps and residual risk
- The table's quotes were checked against the entry's text and the seat reports. I did not re-fetch the pages live and did not run `--fetch` (network).
- The scope claims in M2 rest on the seat reports (`SrcCopilotSdk.md:32`, `SrcGemini.md:47`) and on the Gemini page line 75 as quoted there. I did not open the Gemini page live.
- Nothing here changes a gate result. All findings are wording, except M1's question of whether S031 should count, which is the L1's judgment.
- Not checked: the other 16 no-harm gates and the C1 surfaces gate (outside this item).

## Evidence (commands and exit codes)
- `git clone -q …/kotoba-shokunin …/fleet/kotoba-shokunin` then `git checkout -q 59903b26…`: exit 0; `rev-parse HEAD` = `59903b2637689739a5b9901956301da72d0effe1`.
- `git --no-pager diff --no-ext-diff 43ca0bfb… 59903b26… -- SKILL.md`: exit 0; `1 file changed, 30 insertions(+), 7 deletions(-)`.
- `python3 -B verifiers/verify_skill_checklist.py --json` (in the fleet clone): exit 0; `pass 11, fail 0, na 0`; `trigger.line_budget` PASS "572 lines within budget 600 (from box at line 260)".
- `python3 -B verifiers/verify_skill_checklist.py --self-test`: exit 0; `0 failure(s) over 1851 assertions`.
- `wc -l SKILL.md`: `572` (exit 0), against the 600-line box.
- Repro, scratch clone: A exit 0 PASS; B exit 1 FAIL; C exit 0 PASS "not run"; D exit 1 FAIL; E rc 1, `UnicodeDecodeError`; timeout probe (background, separate clone) rc 0, PASS "(the --help probe timed out), not run".
- `grep -c 'Each lever removes one skill' SKILL.md`: 1 (exit 0). `grep -c 'removed everywhere' SKILL.md`: 4 (exit 0).
- `git --no-pager diff --no-ext-diff --stat 43ca0bfb… 59903b26… -- verifiers/verify_skill_checklist.py`: empty (exit 0).

## Tooling
Nothing installed or updated. No pacman, uv or npm used. Python and git were already present. Writes: scratch directories under `/fast/scratch/hyaku/kotoba-r51/falsify/ReviewSkillWording/` and this report. No lane file other than this report was written, and no subagents were used.
