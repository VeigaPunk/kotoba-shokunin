# ReopenS019S022: falsify seat, round 50 (kotoba lane)

FAILS, for the S019 and S022 `anchor` and `teaches` cells in corpus/SOURCES.md at 956ee1676e4c18480bce8ac3993541462be76e11. Three clauses say more than their page or sweep supports, one sweep needs a case fold the row does not state, and two cells cite the wrong line. HOLDS for byte identity, the quoted lines, the row diff, and the lesson Gate old→new log. Freshness HOLDS: today's bytes equal the recorded bytes.

Scope: S019 (`best-practices.md`) and S022 (`skills.md`) `.md` routes; the round-50 quotes; the changed cells; the Gate log. Judged on adjacency and freshness.
Lane: read-only. This report is the only file written. Private clone and pages: /fast/scratch/hyaku/kotoba-r50/falsify/ReopenS019S022/.
Tooling: no installs or updates. Used curl 8.23.0, sha256sum (reports version 0.8.0), python3 for table parsing only.

## Findings (by severity)

**F1 (medium, Q26): S022 row says "the page's only 'which one wins' rules are for name collisions (settled by origin)" and "a name clash is settled by origin."** (SOURCES.md:35)
- skills.md:183-185 gives a which-one rule for nested same-name skills. Claude is told "to invoke the one whose directory holds the files it's working on." That keys on the working directory, not origin.
- Origin decides only the typed `/name` (skills.md:198, :202).
- The seat's list of read lines (SrcReopenS022.md:117) skips 183-186, so "only" was never checked against that paragraph.
- Still holds: no rule keys on two matching descriptions, because the nested rule keys on directory. The census paraphrases the same way at corpus/knowledge/sibling-overlap-census-round49.md:30 ("settled by origin"), though its quote is limited to `/name`.
- Fix: name the nested rule, scope "by origin" to `/name`, drop "only".

**F2 (medium, Q26): S019 row says "so the description is the only arbitration surface this page offers (:215)."** (SOURCES.md:32)
- The row's own anchor cites :846: "The `name` and `description` in your Skill's metadata are particularly critical. Claude uses these when determining whether to trigger the Skill." The page names two inputs.
- A keyword sweep cannot establish "only." A wider sweep (`both`, `two skills`, `more than one`, `either`, `picks`, `chooses`, `selects`, `best match`, `which one`, `competing`) finds no tie-break rule on best-practices.md. The no-tie-break claim itself holds.
- The seat quotes :846 (SrcReopenS019.md:39) and still writes "only" (lines 56-58).
- Fix: "the description (:215) and name (:846) are the triggering inputs; the page states no tie-break."

**F3 (medium-low, reproducibility): both sweep counts depend on case folding the rows do not state.** (SOURCES.md:32, :35)
- The seats ran `grep -ciE` (SrcReopenS019.md:43; SrcReopenS022.md:87, :116). Neither row says so.
- Case-sensitive counts differ: S019 `conflict` 2 (row says 3); S019 `multiple skills` 0 (row says 1); S022 `same name` 1 (row says 2).
- Fix: add "case-insensitive" to both sweep statements.

**F4 (low): S019 row labels the :474 hit as "PDF-form text."** (SOURCES.md:32)
- best-practices.md:466-474 is the research-synthesis template (Step 4, "Conflicting viewpoints (if any)"). The seat calls it a "report template" (SrcReopenS019.md:54), but its Deliverable 2 says "the last four are PDF-form guidance" (line 92).
- Fix: name :474 as a research-template line; PDF-form is :976, :980, :1016.

**F5 (low): S022 row cites `:200` as "the name-comparison rule."** (SOURCES.md:35)
- skills.md:200 is the header row of the name-collision table ("| Same name in | Which one runs |"). The comparison rule is :278 (look-alikes :280).
- Fix: cite :278 and :280.

**F6 (low, record): S022 access dates disagree between row and Gate.**
- Row: fetched 2026-10-22T09:41:02Z, re-opened 2026-10-22T12:28:45Z.
- Lesson (corpus/lessons/round-50.md:67-73): "fetched 2026-10-22T12:28:45Z and again at 13:04:07Z." The 13:04:07Z re-fetch appears only in the seat (SrcReopenS022.md:115), not in the row.
- Fix: the row records every fetch the Gate cites, and the Gate's first fetch matches the row.

**F7 (low, not settleable from the repo): S019 anchor says the round-47 fetch was 42,028 B, sha256 `727f3fa1…`, "editorial drift only, the rule lines are unchanged."**
- The round-47 bytes are not held. The prefix appears only as text in round-47 seat reports.
- The round-47 seat printed best-practices lines 155 and 162 (SrcNewAnthropicPlatformSkills.md:220-222): both "Cannot contain XML tags." Today's lines 155 and 162 match (`sed -n '155p;162p'`).
- Line 161 (the 1,024 cap) appears in no round-47 record of best-practices.md. The round-47 "Maximum 1024" quotes (SrcNewAnthropicPlatformSkills.md:31, :69, :80) come from S012 skills-guide.md.
- Fix: say "lines 155 and 162 unchanged," or drop "the rule lines are unchanged."

## Holds (with evidence)

1. **Byte identity.** Fetched 2026-10-22T13:32:07Z with `curl -sS -L`:
   - best-practices.md: HTTP 200, 42,169 B, sha256 `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960`. Prefix matches. Full hash matches the seat record (SrcReopenS019.md:20).
   - skills.md: HTTP 200, 111,557 B, sha256 `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456`. Prefix matches. Full hash matches the round-48 record: `git show 956ee16:.ufo/waves/round-48/build/C2ClaudeDocs.md | grep -c cdfcb0df93…` → 1.
   - HTML route (skills): HTTP 200, 0 redirects, 1,233,129 B, sha256 `10219534…`. The "same prose" claim is checked by hash and size only.
2. **Quotes at their locations** (`sed -n` on the fetched pages):
   - S019 :215 "Your description must provide enough detail for Claude to determine when to select this Skill": exact.
   - S019 :161 "Maximum 1,024 characters": exact. The same cap is at :1134, written with a comma.
   - S019 :206 "**Always write in third person**. The description is injected into the system prompt…": exact. The census cites it at corpus/knowledge/sibling-overlap-census-round49.md:223.
   - S022 :389 "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage": exact, 19 words.
3. **Row diff.** `git diff f3046464 956ee16 -- corpus/SOURCES.md`: one hunk, `@@ -29,11 +29,17 @@`, 8 insertions and 2 deletions. S019 and S022 replaced; S024-S029 added; no other row moved. Rows 23 → 29.
4. **Lesson Gate old→new log** (corpus/lessons/round-50.md:64-78), checked against the diff and a python3 parse of both revisions:
   - S019 used-by: base `SKILL.md, …frontmatter-rule-authorities-round48.md` → adds the census and the lesson.
   - S022 used-by: base census → adds the lesson.
   - S024-S029: status mined, opened 2026-10-22, recheck 90d, used-by census and lesson (6 of 6).
   - S019 and S022: status mined → mined; recheck 90d → 90d.
   - Anchor, scope and teaches changed as the Gate says. Seat Deliverable 1 tables carry each old and new cell (SrcReopenS019.md:76-81; SrcReopenS022.md:66-71).
5. **S022 teaches claims that hold:** names always listed; 1% budget and least-invoked-first (skills.md:1207); 1,536 cap "regardless of budget … configurable via `skillListingMaxDescChars`" (:1213); "make the description more specific" and `disable-model-invocation` (:1194-1195); enterprise over personal over project (:202); `claude -p` loads only the first (:682); the three `1024` hits are byte formatting (:1085, :1086, :1134); `precedence` (:920) is a skillOverrides alias; `conflict` (:49) is `/doctor prompt-audit`; `truncat` (:389, :747).
6. **S019 teaches claims that hold:** 1,024 cap (:161, :1134); non-empty and no XML tags (:160, :162, :1134); what plus when (:163, :203); anchor headings exist (146, 201, 251, 837, 1127, 1129).

## Commands and counts (pages fetched 13:32Z)

- `git clone` and checkout 956ee16; `cmp` of the clone's corpus/SOURCES.md against the records blob: identical (exit 0).
- `cmp -s` base vs records SOURCES.md: exit 1 (they differ).
- `grep -c '^| S0'`: base 23, records 29.
- `grep -ci` on best-practices.md: overlap 1, ambigu 0, precedence 0, tie-?break 0, conflict 3, multiple skills 1, same name 0, prioriti 0, 1024 0 (`1,024` on 2 lines), truncat 0.
- `grep -ci` on skills.md: overlap 0, ambigu 0, precedence 1, tie-?break 0, conflict 1, multiple skills 0, same name 2, prioriti 0, 1024 3 (3 lines), truncat 2, arbitrat 0.
- `grep -c` (case-sensitive), same pages: S019 conflict 2, multiple skills 0; S022 same name 1.
- `git -C <lane> grep -n 'arbitration surface\|settled by origin\|name clash' 956ee16 -- corpus`: exit 0; hits at SOURCES.md:32, :35 and census :30.
- Exit codes for the individual count runs were not captured; counts are as printed.
- Installs: none.

## Residual risk and verification gaps

- The "no tie-break" conclusion rests on keyword sweeps plus reads of the selection sections. I did not read the full 1,191-line S019 page or the 1,234-line S022 page. An unindexed rule would not appear.
- S024-S029 page content is outside this seat. I checked only their status, opened, recheck and used-by cells.
- The round-47 S019 bytes are not held, so F7 cannot be closed from the repo.
- Recommended checks for Main after landing: re-run `grep -ci` on both pages with the wording fixes from F1-F5 applied, and confirm the rows' statements match the seat reports after the fixes.
