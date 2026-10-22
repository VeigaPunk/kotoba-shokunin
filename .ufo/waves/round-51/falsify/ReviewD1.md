VERDICT: FAILS (narrow). The byte-exact DescDraft commit and the 71-of-71 seat count HOLD. Two statements in the record FAIL: "LOG.md carries the correction" (LOG.md is unchanged) and "the last lane commit is 2abd290" (43ca0bf came later). "0 cancelled" is BOUNDED: it is an absence of records, not a positive finding.

Scope: judged at HEAD 59903b2637689739a5b9901956301da72d0effe1, as assigned. The lane HEAD moved to 533ff208 at 12:21:55 (round-51 commit touching PROVINCE.md, SCORECARD.md, corpus/README.md, verifiers/verify_surfaces.py). None of the D1 files changed there (`git diff --name-only 59903b26 533ff20` lists only those four), so the findings hold at 533ff20. Read-only throughout: git show, ls-tree, log, cat-file, diff-tree, grep and stat; no git write, no jj, no gate, no probe, no scratch needed. No tool installed or upgraded. No delegation (leaf seat).

## Findings, by severity

1. FAILS, medium. The lesson says LOG.md carries the correction. It does not.
   - corpus/lessons/round-51.md:108-109: "0 cancelled; 0 died; 70 of 71 ... this paragraph and LOG.md carry the correction."
   - LOG.md:2391 still says "`FloorsRegister` and `DescDraft` were overtaken" (two seats). LOG.md:2409 names four seats "without a usable report at landing", without "cancelled". Neither line says 71 of 71 or 0 cancelled.
   - LOG.md is clean in the working copy, so nothing is pending there: `git --no-optional-locks status --porcelain -- LOG.md` (empty, exit 0).
   - The fleet report keeps the wrong line (.ufo/reports/round-50/kotoba.md:96-97) and has no addendum: `grep -c Addendum` → 0, exit 1. D1Disposition § 2 (lines 133-138) said the LOG.md edit belongs to the L1, and it proposed a fleet addendum. The lesson dropped that addendum and did not say so.
   - Fix: correct LOG.md:2391 to four seats and add the 71-of-71 and 0-cancelled line. Or change the lesson to "should carry". Either the fleet report gets a pointer, or the lesson says the fleet line stays uncorrected.

2. FAILS, medium if the proposed addendum is applied as written. The uncommitted seat report states a false fact.
   - .ufo/waves/round-51/build/D1Disposition.md:87 "The last lane commit of round 50 is 2abd290…"; :122 (addendum text) "the last lane commit of the round is 2abd290e at 10:51:22"; :130 and :144 "57 s after the last lane commit".
   - `git log --format='%h %cI %s' 2abd290..59903b26` lists 43ca0bf at 11:04:58 ("round-50 verifier spot-check (integrator, hyaku)") after 2abd290. What is true: `git log 2abd290..59903b26 -- .ufo/waves/round-50` lists only e621902, so 2abd290 is the last round-50 commit that touched the wave tree.
   - The committed lesson is correct: "57 s after `2abd290`" (lesson lines 100-101).
   - Fix: write "last round-50 commit touching the wave tree", and drop "last lane commit" everywhere.

3. BOUNDED, medium. "0 cancelled" and "0 died" are stated as facts, but the evidence is missing records.
   - The registries cannot record status. All 71 members have agentId null: non-null count 0 for both registries and 0 for both dispatch files (python json, exit 0). Member keys are agentId, axes, item, kind, milestone, role. No status key exists.
   - No cancel text in any round-50 seat report: `git grep -c -i cancel 59903b26 -- .ufo/waves/round-50` → no output, exit 1.
   - No cancel record in fleet state: pattern "DescDraft|D2D4Wording|[Cc]ancel" over .ufo/watchdog.log and .ufo/state → no matches.
   - The only "cancelled" text is the fleet line at kotoba.md:96-97.
   - What the files do show: the DescDraft seat was still writing scratch files at 10:48:31 (`stat` of /fast/scratch/hyaku/kotoba-r50/build/DescDraft/patch.diff: 10:48:31.550907651 -0300). That is about 1 h 28 min after the build dispatch (registry createdAt 12:20:42Z = 09:20:42 -03:00). Its report followed at 10:52:19. If a cancel was sent, the seat did not stop. That supports "not stopped", not "never cancelled". Whether the L1 sent a cancel is unrecorded.
   - Fix: "no cancellation recorded; 71 of 71 seats kept working to a written report". Mark "0 died" as "no death seen in the files".

4. BOUNDED, low-medium. The D2D4Wording timing leaves out the strongest evidence.
   - The L1 first committed the path at 1cb2e65 (10:51:01, "falsify wave evidence") as a 16,392-byte version: `git cat-file -s 1cb2e65:.ufo/waves/round-50/build/D2D4Wording.md` → 16392. The final 18,592-byte version was written at 10:51:16 and committed at 2abd290 (10:51:22).
   - So the L1's own commit held a D2D4Wording report 67 s before the fleet line of 10:52:08 that calls the seat "without a report". The lesson's "committed in 2abd290, 6 s later" is true of the last write and hides this. Add 1cb2e65 to the correction.
   - PrecedenceDraft shows the same pattern: 22,616 bytes committed at a78fec1 (10:39:10), 23,707 bytes after the 10:39:45 write (committed at bf109ca, 10:41:43).

5. NOT YET EXERCISED, low. The sweep output is not on record.
   - Lesson lines 110-111 say the sweep "runs after the last seat write … its command and output are in the round-51 report." `ls .ufo/reports/round-51/` shows only kotodama.md (exit 0), so no such report exists yet.
   - The sweep in D1Disposition § 3 ran once, earlier. The lane HEAD has moved since. I did not re-run it.

6. HOLDS. DescDraft.md is byte-exact with the file the spot-check described.
   - `git show 59903b26:.ufo/waves/round-50/build/DescDraft.md | sha256sum` → 0181a45953242fcff7595a91d8c1036b10dc4dc7aaae5303baa1cb445c3d2348, exit 0. `… | wc -c` → 10079, exit 0. Both match the description (sha256 0181a459…, 10,079 B).
   - Lane working copy: `sha256sum` → same hash, exit 0. `git hash-object` of the lane file and `git rev-parse 59903b26:…` both → 8e79b5e240080b912f74d84ae301086f9fcf61da.
   - Added in one commit only: e621902 (12:11:48 -03:00). Not in the 533ff20 diff.
   - Misdating holds: `git diff-tree --no-commit-id --name-only -r 956ee167 | grep -c '^SKILL.md$'` → 0, exit 1. 542f515 changed SKILL.md (`git show --stat 542f515 -- SKILL.md` → 8 insertions, 6 deletions). DescDraft.md:11 names 956ee167 as the landing.

7. HOLDS. The seat counts match the files and the registries.
   - Reports in the tree: `git ls-tree -r --name-only 59903b26 .ufo/waves/round-50 | grep -c '^\.ufo/waves/round-50/build/.*\.md$'` → 33, exit 0. Falsify: 38, exit 0. Total 71.
   - Spec items: build-spec.json 33, falsify-spec.json 38. Dispatch counts: spawn 33 and resume 0; spawn 38 and resume 0. Registry members: 33 and 38. Names are equal sets across spec, dispatch, registry and report files (python, exit 0).
   - Role counts match the fleet report (kotoba.md:95 and :98): build scribe 12, scout 7, executor 5, critic 3, reviewer 3, mutation-tester 2, connector 1; falsify reviewer 26, critic 6, mutation-tester 5, scout 1.
   - No empty report: smallest is 5,554 bytes (`cat-file -s` over all 71, exit 0).
   - "70 of 71 committed in round 50": `git log --diff-filter=A --name-only` puts the 70 first additions in 542f515 (10:25:02), a78fec1 (10:39:10), bf109ca (10:41:43), 87eeae2 (10:43:41) and 1cb2e65 (10:51:01). All fall before the round-50 closure 43ca0bf (11:04:58). DescDraft's first addition is e621902 (12:11:48).

8. HOLDS. The recorded mtimes and the arithmetic are right.
   - `stat -c '%y %s %n'` in the lane (read-only): DescDraft 10:52:19.554935837 (10079 B); D2D4Wording 10:51:16.487390231 (18592 B); FloorsRegister 10:47:49.051571224 (11932 B); PrecedenceDraft 10:39:45.332993124 (23707 B). The recorded values (10:52:19.555, 10:51:16.487, 10:47:49.052, 10:39:45.333) match after rounding.
   - Corroborated by content changes at commit boundaries. PrecedenceDraft went 22,616 → 23,707 bytes between a78fec1 and bf109ca. D2D4Wording went 16,392 → 18,592 bytes between 1cb2e65 and 2abd290. FloorsRegister is 11,932 bytes at both 1cb2e65 and HEAD, and its mtime precedes its first commit.
   - Arithmetic: 2abd290 committed at 10:51:22 and the DescDraft write at 10:52:19 gives 57 s. The D2D4Wording write at 10:51:16 and commit at 10:51:22 gives 6 s.
   - The fleet report mtime is 10:52:08.988899180 (`ls -la --time-style=full-iso`, exit 0). DescDraft was written 11 s after the report was filed.

## Residual risk and verification gaps
- No round-50 dispatch or hub send log is in the lane or in the fleet state. A cancel message, if one was sent, is unrecorded. "0 cancelled" stays bounded.
- Tracked-file mtimes are plausible write times but not proven ones, because jj can rewrite working files. The size changes in finding 8 support the four used.
- I did not re-run the D1Disposition sweep (§ 3). No round-51 report exists yet to receive its output.
- Checks the main agent should run after the L1 edits: `git show HEAD:LOG.md | grep -c -E '71 of 71|0 cancelled'` should be 1 or more; `grep -n 'last lane commit' .ufo/waves/round-51/build/D1Disposition.md` should return nothing.

## Commands run (read-only; exit codes as observed)
- `git rev-parse HEAD` → 59903b2637689739a5b9901956301da72d0effe1, exit 0; at 12:22:44 → 533ff208e289dec050edeac10bbf2c510e45cc59, exit 0.
- `git log --format='%h %cI %s' 2abd290..59903b26` → 59903b2, e621902, 34cfffb, e032030, 7c81a78, 43ca0bf; exit 0.
- `git log --format='%h %cI %s' 2abd290..59903b26 -- .ufo/waves/round-50` → e621902 only; exit 0.
- `git cat-file -s 1cb2e65:.ufo/waves/round-50/build/D2D4Wording.md` → 16392; `… 2abd290:…` → 18592; `a78fec1:…/PrecedenceDraft.md` → 22616; `bf109ca:…` → 23707.
- `git --no-optional-locks status --porcelain -- LOG.md` → no output, exit 0.
- `git show HEAD:LOG.md | grep -c -E '71 of 71|0 cancelled'` → 0, exit 1.
- `grep -c Addendum .ufo/reports/round-50/kotoba.md` → 0, exit 1.
- `git grep -c -i cancel 59903b26 -- .ufo/waves/round-50` → no output, exit 1.
- `git diff-tree --no-commit-id --name-only -r 956ee167 | grep -c '^SKILL.md$'` → 0, exit 1.
- Registries and dispatch via python json over `git show 59903b26:…`, exit 0: spec items 33 and 38; dispatch counts spawn 33/38; agentId non-null 0 everywhere; createdAt build 12:20:42.668Z, falsify 13:28:46.918Z.
- `git log --diff-filter=A --name-only --format='ADD %h %cI' 59903b26 -- .ufo/waves/round-50` → first additions as in finding 7, exit 0.
- `git log -1 --format='%h %cI' 43ca0bfb…` → 11:04:58 -03:00, exit 0.
- `stat -c '%y %s %n'` on the four lane files and on /fast/scratch/hyaku/kotoba-r50/build/DescDraft/patch.diff → values in findings 3 and 8, exit 0.
- Fleet watchdog and state pattern search → "No matches found".
