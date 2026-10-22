# ReopenS030 — round 51 C2, GitHub Copilot SDK row

VERDICT: HOLDS-BOUNDED. The quote, key term, source row and gate record hold on the bytes I fetched at 2026-10-22T15:15:39Z. Two wordings go past the page: "never offered" / "removed everywhere" (F1), and the no-tie-break negative needs the words "differently named" (F2).

Scope: S030 row (`corpus/SOURCES.md:43`), SKILL.md row (`SKILL.md:396`), entry row (`corpus/knowledge/skill-overlap-levers-round51.md:20`), entry Finding 2 (`:45-50`), lesson gate (`corpus/lessons/round-51.md:37-43`). Other client rows not judged.
Tools: curl, git, python3, grep and sha256sum were already on the host. No installs or upgrades. Scratch: `/fast/scratch/hyaku/kotoba-r51/falsify/ReopenS030/`. Lane: read-only; this file is my only write.

## Verdict per point
1. Quote verbatim at the cited line, at most 25 words, key term as exact backtick span: HOLDS.
2. Page supports the lever, held-by and effect cells: HOLDS-BOUNDED (lever and held-by HOLD; effect BOUNDED, see F1).
3. S030 row (tier A, docs, mined, vendor prefix, used-by, Gate): HOLDS (teaches gloss overreaches, see F3).
4. Rule between two skills that both remain candidates: HOLDS-BOUNDED (none for differently named skills; one name-keyed rule at `:685` is not scoped out, see F2).
Freshness: HOLDS. The same full hash appears in the round-50 fetch (12:31:51Z), the build fetch (14:19:11Z) and mine (15:15:39Z).

## Fetch record
- `curl -sS` of https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md at 2026-10-22T15:15:39Z (UTC).
- HTTP 200; 35,455 bytes; text/markdown; charset=utf-8; no redirect.
- sha256 `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3` (prefix 64856ff4, as expected).
- Second request at 15:18:58Z: HTTP 200, content-length 35455, age 18 (CDN cache), cache-control max-age=60.

## Point 1 (HOLDS)
- Line 809 is `* Use `disabledSkills` to exclude conflicting skills`. The quote is that text without the bullet mark: 6 words, one code span equal to the key term in SKILL.md:396 and the entry. ASCII only, no CR bytes (E3).

## Point 2 (HOLDS-BOUNDED)
- Lever: HOLDS. Section "Disabling skills" (lines 177-179) says "Disable specific skills while keeping others active:". The example passes `disabledSkills` into `createSession` (185-188). Table row "Skills to disable" (697; also 700, 703, 706). The identifier matched is the `name` field, or the directory name if `name` is omitted (288).
- Held by app developer: HOLDS. It is a session-creation field set in application code (185-188, 697-706).
- Effect "removed everywhere" and lever wording "so those skills are never offered": BOUNDED. The page never says what a disabled skill loses. The 24 disable, exclude and remove hits (E8) say nothing about the skill catalog, the `skill` tool or user invocation. The only user-invocation sentence (line 298, "users can invoke them like any other skill") is about provider skills. The build report makes the same leap and then disclaims it: `SrcCopilotSdk.md:32` says "the model is never offered it", while its "Not claimed" bullet (lines 146-147) disclaims catalog removal.
- Conflict section (805-810): HOLDS for the entry's reading. Line 807 says "If multiple skills provide conflicting instructions:". Lines 11 and 291 say a skill body is injected when the skill loads, which supports "after both skills load".

## Point 3 (HOLDS)
- Tier A (column 4), kind docs, status mined, opened 2026-10-22, recheck 90d.
- URL begins `https://docs.github.com/en/copilot/`, the prefix the counter pins for this client (`verifiers/check_overlap_levers.py:127`).
- used-by names `corpus/knowledge/skill-overlap-levers-round51.md`, plus the lesson and `skill-selection-rules-round50.md`. That file's correction (lines 75-80) cites the page's `:685`.
- Lesson `## Gate` (line 28) records S030 at lines 37-43: fetch record, hash, quote and `skills.md:809`.
- Anchors checked against the bytes: 11, 252, 262, 286-291; 177-179; 697, 700, 703, 706; 805-810; 711-724; 683-685; 648. All match.

## Point 4 (HOLDS-BOUNDED)
- Requested sweep (E4), 15 lines. Lines 3, 18, 271, 278, 767, 779 are "tie" inside "abilities", "capabilities" and "vulnerabilities" (false positives). Lines 288, 449, 720 are "select" forms. Lines 647 and 687 are "both" ("Both are required"; "both operations"). Lines 805, 807, 809, 810 are the conflict section. None states a choice rule.
- Wider sweep (E9: match, candidate, rank, prefer, first, last, order, wins, priority, precedence, replace, instead, multiple, specific, best and more). No choice rule. Rule-like lines: 685 (name-keyed replacement), 661 (provider names unique, ignoring case), 727 (directories scanned when skills first load), 759 (agent preload names resolve from session-level `skillDirectories`).
- Result: no rule decides between two differently named skills whose descriptions both match. One rule decides between two same-named skills (685). See F2.

## Findings
F1 MEDIUM. The effect wording goes past the page.
- Entry line 20 ("so those skills are never offered") and SKILL.md:396 ("removed everywhere").
- The effect column tells an author whether a disabled skill still fires on a user's request (entry lines 67-68). The page is silent on that route for this lever. Its only wording is "Disable specific skills while keeping others active" (179) and "Skills to disable" (697).
- Fix: "turns the named skill off for the session (`skills.md:179`, `:697`); the page does not say whether a user can still invoke it." Effect: "removed for the session; user route not documented". Or mark the claim [INFERENCE].

F2 MEDIUM-LOW. The negative has no scope, and the lever list omits the same-name rule.
- SKILL.md:388-389 says "none decides between two skills that both remain candidates". That is false for two same-named skills: the SDK page decides them at line 685 ("A provider skill with the same name as a file-based skill replaces the file-based skill"). The round-50 paragraph (SKILL.md:378-381) already limits its claim to "copies of one name"; the round-51 sentence drops that limit.
- Entry lines 28-29 ("Other levers ... not counted") list `:262`, `:683`, `:648`, but not `:685`, `:711-724` or `includedBuiltinSkills` (`:720-722`). The S030 row cites `:683-685` and `:711-724`. The build report lists `includedBuiltinSkills` as a lever (`SrcCopilotSdk.md:36`) and calls `:685` "Not a lever" (line 38).
- My view: `:685` is a name-keyed removal held by the app developer, since a provider skill with the same name removes the file-based one. It cannot help with two differently named skills, so the counted answer stands. The entry should count it or say why not.
- Fix: add "differently named" at SKILL.md:388-389 and entry Finding 2; list `:685` and `:711-724` under "not counted", with reasons.

F3 LOW. The S030 `teaches` cell overreaches.
- SOURCES:43 says "The documented remedy for conflicting skills is to remove one, not to reword it". The page never mentions rewording. Its second remedy, "Reorganize skill directories to avoid overlaps" (810), removes no skill.
- Fix: "the documented remedies are to exclude a conflicting skill (`:809`) or reorganise directories (`:810`)".

F4 LOW. The counter does not check the cited line, and offline mode does not check the quote text.
- The only page check is `fetch_probe`, which runs `quote_on_page` (a substring test after `normalize`) on the page (`check_overlap_levers.py:446-456`, `:442-443`). `normalize` deletes `*`, `_`, backticks and HTML tags on both sides (`:106`, `:422-424`). So code-span formatting is compared only inside the entry text, never against the page.
- The S030 source URL has no `.md`, so the probe reads the rendered HTML page first. The markdown bytes that the recheck hashes are read only if that fails.
- No mode reads the cited line. Mutation A: `(skills.md:809)` changed to `(skills.md:999)` in a private clone; the counter still reports 7 of 7, exit 0 (E14). Mutation B: "conflicting" changed to "overlapping"; the offline counter still reports 7 of 7, exit 0 (E15). The page probe rejects the changed wording (E16), but only in `--fetch` mode.
- Consequence: "verbatim at the cited line" rests on my hand check and the 15:08Z re-fetch the lesson records (line 40), not on the counter. Fix: check the cited line against the fetched bytes, or state in the entry's Limits that line numbers are checked by hand.

F5 LOW. The negative's sweep output sits outside the repo, and the build report has one wrong line cite.
- Lesson lines 33-35 say the Q14 negative is backed by "the seven seats' sweeps, each pasted in its `Src*.md` report". For the SDK row the report gives the command and per-term counts (all eight match, E6), but the 51-line output is at `/fast/scratch/hyaku/kotoba-r51/build/SrcCopilotSdk/sweep_requested.txt`. It is not pasted.
- `SrcCopilotSdk.md:50` lists the invocation hits as `302,648,653,687`. Line 653 has no such word; line 98 (`PermissionInvocation`) is the fourth hit. The count of 4 is right (E7).

## Evidence (exit codes as captured)
- E1 `curl -sS -o skills.md -w 'HTTP %{http_code} bytes %{size_download}'` plus `date -u` and `sha256sum`: 2026-10-22T15:15:39Z, HTTP 200, 35455 bytes; exit 0.
- E2 `sha256sum skills.md`: 64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3; exit 0.
- E3 `grep -nF 'Use `disabledSkills` to exclude conflicting skills' skills.md`: `809:* Use ...`; exit 0. `grep -c $'\r'`: 0.
- E4 `grep -niE 'overlap|conflict|precedence|tie|both|choose|select|priorit' skills.md`: 15 lines; exit 0.
- E5 `grep -niE 'overlap|conflict|precedence|disable|deny|permission|hidden|invocation' skills.md`: 51 lines; exit 0. `diff` against the build report's `sweep_requested.txt`: no output; exit 0.
- E6 `grep -ciE` per term: overlap 1, conflict 3, precedence 0, disable 19, deny 0, permission 27, hidden 1, invocation 4. Each matches `SrcCopilotSdk.md:45-53`.
- E7 `grep -niE invocation skills.md`: lines 98, 302, 648, 687.
- E8 `grep -niE 'disabl|exclud|remov' skills.md`: 24 lines (5, 18, 177, 179, 187, 201, 212, 224, 241, 288, 302, 434, 472, 638, 648, 683, 684, 697, 700, 703, 706, 715, 730, 809); each read.
- E9 `grep -niE '<synonym list>' skills.md | grep -viE 'capabilit|vulnerabilit|abilit'`: exit 0; hits read by hand.
- E10 `curl -sS -D headers.txt -o /dev/null -w 'HTTP %{http_code} bytes %{size_download} redirects %{num_redirects}'` at 15:18:58Z: HTTP 200, 35455 bytes, 0 redirects; exit 0.
- E11 `grep -nE 64856ff4` on `.ufo/waves/round-50/build/SrcCopilotSkills.md` and `corpus/lessons/round-50-verifier-spotcheck.md`: SrcCopilotSkills.md:34 has the full hash equal to E2; exit 0.
- E12 `git clone -q <lane> <scratch>/lane`: exit 0. `git checkout -q 59903b2637689739a5b9901956301da72d0effe1`: exit 0. `git rev-parse --short HEAD`: 59903b2.
- E13 In the clone, `python3 -B verifiers/check_overlap_levers.py --root .`: "overlap levers backed 7 of 7 clients"; exit 0.
- E14 Mutation A in the clone (`sed -i`): `grep -c 'skills.md:999'` gives 1; counter gives 7 of 7, exit 0. Restored from a copy.
- E15 Mutation B in the clone (`sed -i`): `grep -c 'exclude overlapping skills'` gives 1; counter gives 7 of 7, exit 0. Restored; `git status --short` empty.
- E16 Python with `dont_write_bytecode` set, loading the clone's checker and the fetched bytes: `quote_on_page(original)` True; `quote_on_page(mutated)` False; `normalize("`x`") == "x"` True; words in the quote 6; `CODE_SPAN.findall` gives `['disabledSkills']`.
- E17 Reads: SOURCES.md:43 (raw); lesson 28-43; entry 1-96; SKILL.md 370-420; round-50 knowledge file 71-84; `SrcCopilotSdk.md` 1-149.

## Residual risk and gaps
- How a disabled skill behaves in a live SDK session (catalog, user invocation) is not measured; no SDK harness ran. F1 rests on this gap.
- The counter's `--fetch` mode was not run across all seven pages; E16 covers the S030 quote only.
- The 15:08Z re-fetch and the 14:19Z build fetch come from the lesson and build report; my 15:15:39Z fetch matches their hash.
- The other six client rows are not judged.
