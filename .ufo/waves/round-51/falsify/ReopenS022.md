VERDICT: FAILS. C2 Claude Code row: quote, lever wording and row metadata hold; the negative "none decides between two remaining candidates" is contradicted by skills.md:183-186 (same-named nested skills); the held-by cell omits user-held levers the page documents.

Scope: entry corpus/knowledge/skill-overlap-levers-round51.md (table row S022; Findings 2-4); SKILL.md lines 385-389 and 399; corpus/SOURCES.md:35 (S022); corpus/lessons/round-51.md Gate (lines 51-61). Lane HEAD 59903b2637689739a5b9901956301da72d0effe1; the five files read match their HEAD blobs by sha256. Not attacked: C1, the other six rows.
Freshness: https://code.claude.com/docs/en/skills.md fetched 2026-10-22T15:15:30Z (UTC), HTTP 200, 111,557 B, sha256 cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456 (matches the recorded prefix and the recheck). Bytes kept at /fast/scratch/hyaku/kotoba-r51/falsify/ReopenS022/skills.md.

## Verdicts per point
1. Quote verbatim at the cited line, at most 25 words, key term as exact backtick span: HOLDS.
2. Lever, held-by and effect cells against the surrounding section: HOLDS-BOUNDED. Lever and effect hold; held-by is right for the frontmatter flag but one-sided (F3).
3. S022 row (tier A, docs, mined, vendor URL, used-by names the entry, Gate records it): HOLDS on all six. Teaches cell: HOLDS-BOUNDED (F5).
4. Any rule deciding between two skills that both remain candidates: FAILS as worded (F1). Holds for the narrower round-50 claim (differently named skills; no rule keys on two matching descriptions), with a borderline (F4).

## Findings (by severity)

F1 HIGH. The negative is contradicted by a documented rule for same-named nested skills.
- skills.md:183: "When a nested skill's directory name matches another skill's name, both stay available."
- skills.md:185: Claude "lists the directory-qualified variants for Claude, with an instruction to invoke the one whose directory holds the files it's working on."
- Two candidates remain, and a non-description rule (working directory) decides between them.
- SKILL.md:388-389 has no qualifier: "none decides between two skills that both remain candidates, where the description is still the only lever." Entry Finding 2 line 45 is the same in its first sentence; only its second sentence (lines 46-47) limits round-50's claim to "differently named" skills. The nested case is same-named, so the unqualified sentences are false for it.
- The S022 teaches cell (SOURCES.md:35) cites this rule, so the row and the entry disagree.
- Counted rows are unaffected (each removes one skill). The claim as worded is overstated.
- Fix: add "differently named" to SKILL.md:388-389 and to entry line 45; name this rule as the location-based exception.

F2 MEDIUM. The round-51 sweep repeats the round-50 reading miss.
- .ufo/waves/round-51/build/SrcClaudeCode.md:55-56: "The page's only 'which one wins' rules are same-name collisions settled by origin (`:196-208`) and explicitly stacked skills (`:682`)."
- Round-50 falsify .ufo/waves/round-50/falsify/ReopenS019S022.md:11-16 (F1) recorded the same omission at 183-186 and asked to drop "only". SOURCES.md:35 still says "the page's only 'which one wins' rules".
- The keyword counts are right; the reading step failed. Gate Q14 ("sweeps pasted") does not show the nested paragraph was read.

F3 MEDIUM-LOW. Held-by for Claude Code is one-sided.
- skills.md:894: `skillOverrides` "controls skill visibility from your settings instead of the skill's own frontmatter. Use it for skills whose SKILL.md you don't want to edit." Values (898-903): "off" hides from Claude and the `/` menu; "user-invocable-only" hides from Claude; "name-only" lists the name only.
- skills.md:855-866: permission rules `Skill(name)` deny, under "Restrict Claude's skill access" (842).
- The entry counts opencode's permission `deny` (S024, held by user or operator). For Claude Code it names skillOverrides only as "not counted" and never mentions the permission rule. Finding 3 lists Claude Code among author-held frontmatter clients.
- Counter gap (read in code, not run): verifiers/check_overlap_levers.py:345-352 checks held-by and effect only for membership in ALLOWED_HELD_BY and ALLOWED_EFFECTS. REVIEWED_LEVERS["Claude Code"] (lines 147-148) includes `skillOverrides`, a user-held lever, so a row pairing it with "skill author" would pass.
- Fix: held-by "skill author (frontmatter); user or admin (skillOverrides, permission rules)"; have the counter tie holder to lever.

F4 MEDIUM-LOW. Two documented non-removal rules sit outside the entry's definition and are not named.
- skills.md:901 and :1213 ("To free budget for other skills, set low-priority entries to `name-only`"): the skill stays listed by name and loses its description. Of two overlapping skills, only the other description can match. Held by the user.
- skills.md:1207: "drops descriptions starting with the skills you invoke least".
- Both change which of two differently named skills Claude can match without changing description wording. They are not removal levers, so the entry leaves them out; entry lines 46-47 ("the description is still the only lever") read broader than that.
- Fix: name both in the "not counted" paragraph; scope the negative.

F5 LOW-MEDIUM. Three statements in the S022 teaches cell (SOURCES.md:35) are wrong or unfixed.
a. "the page's only 'which one wins' rules are for name collisions (settled by origin)": false (F1). Origin decides only the typed `/name` (skills.md:198).
b. "`same name` (`:200`, `:278`) is the name-comparison rule": skills.md:200 is the table header "Same name in | Which one runs". The comparison rule is :278 (look-alikes :280). Round-50 F5 said this.
c. "`same name` 2": true only under case folding (case-insensitive 2, case-sensitive 1). The row does not say so. Round-50 F3 said this.

F6 LOW (freshness). The row's HTML-route claim is stale.
- Row: "the HTML route (200, 1233129 B, sha256 `10219534…`) ... re-fetched byte-identical."
- Today: 200, 1,233,172 B, 0 redirects, sha256 d42066f2170a5e839651ca0e84d3c25533d4bece0267028c9dbdfabfc87e665d; two fetches identical.
- The HTML route writes "Claude’s" with a curly apostrophe; the .md has a straight one. The counter's probe returns False on the HTML bytes and True on the .md bytes, so the --fetch pass for Claude Code comes from the .md route.
- The recheck covers only the .md hash, so no check fails today.

F7 LOW. Effect cell is narrower than the page: skills.md:393 also keeps the skill out of subagent preloading and session-scheduled task runs. "Automatic choice off" is not wrong, only incomplete.

## Points 1-3: evidence
- Exact bytes (python, exact match, .md): one occurrence, on line 886; 18 words; span `disable-model-invocation: true` present; no CRLF; line 886 is ASCII.
- Line 886: "**Hide individual skills** by adding `disable-model-invocation: true` to their frontmatter. This removes the skill from Claude's context entirely."
- Lever support: 393 "Use for workflows you want to trigger manually with `/name`"; 549 "Claude can't invoke the skill on its own."; 577 table row "Yes | Not on its own | Description not in context"; 844 "By default, Claude can invoke any skill that doesn't have `disable-model-invocation: true` set."
- Entry header citations 549, 577, 886, 894-907, 1194-1195 all match the page.
- S022 row: kind docs; tier A; status mined; opened 2026-10-22; recheck 90d; URL https://code.claude.com/docs/en/skills (counter prefix https://code.claude.com/docs/); used-by ends with corpus/knowledge/skill-overlap-levers-round51.md.
- Gate: round-51.md lines 51-55 (re-open, hash, quote at skills.md:886) and 60-61 (used-by change). Commit 34cfffb changed only the S022 used-by cell (cell-by-cell diff against parent). The nested clause in teaches came from bf109ca (round-50 corrections), so the Gate's "only in-place changes are used-by" holds for round 51.
- Routed defects (round-51.md lines 98-137): grep finds no mention of ReopenS019S022, `:200`, or case folding.

## Point 4: sweep
- Exact pattern, case-insensitive, every match read: 183 (F1); 196-208 (origin precedence for typed `/name`, line 198; "Both load" rows 206-207; not automatic choice); 49 (`/doctor prompt-audit`); 152 (location loading); 682 (`claude -p` loads only the first of explicitly stacked skills); 920 (precedence between two skillOverrides entries for one skill); 1213 (F4); 7 and 982 ("capabilities" contains "tie"); 397 (URL slug `restrict-model-selection`); other matches are "both" in prose (17, 267, 287, 303, 484, 496, 504, 547, 631, 938).
- Extended sweep (adds overlap, ambigu, arbitrat, shadow, prefer, pick, decid, wins, which one, multiple, same name, share a name, both stay, both load, first): 181 (nested skills load when Claude first touches a file there; scope, not a tie-break); 403 (`paths` loads a skill "only when working with files matching the patterns"; scope, not counted); 1207 (F4); 114 and 389 (description decides when to load; supports the description claim).
- Counts (python re on fetched bytes; case-insensitive / case-sensitive): overlap 0/0; ambigu 0/0; arbitrat 0/0; tie-?break 0/0; multiple skills 0/0; prioriti 0/0; precedence 1/1 (920); conflict 1/1 (49); 1024 on lines 1085, 1086, 1134 (4 occurrences); truncat 2/2 (389, 747); same name 2/1 (200, 278).

## Evidence and commands (exit codes verbatim where printed)
1. `curl -sS -o …/skills.md -w 'status=%{http_code} bytes=%{size_download} url_eff=%{url_effective}\n' https://code.claude.com/docs/en/skills.md && sha256sum … && date -u`: status=200 bytes=111557 url_eff=https://code.claude.com/docs/en/skills.md; cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456; 2026-10-22T15:15:30Z. Chain ran to completion (no exit code printed). A first attempt was rejected by the tool before it ran.
2. HTML route, same curl form: status=200 bytes=1233172 redirects=0; sha256 d42066f2…; second fetch identical; `cmp -l` of the two copies piped to `wc -l` printed 0.
3. `git rev-parse HEAD` printed 59903b2637689739a5b9901956301da72d0effe1. sha256 prefixes of the working files equal `git show 59903b26:<path>`: entry 5586347918c9d37d; SKILL.md 60786fb4d890e21f; SOURCES.md 5608806fe8020829; lesson 437cdcc04c3e1440; verifier e871fa03d0587f3f. Chain completed.
4. Counter at HEAD in a private clone (`git clone -q <lane> /fast/scratch/hyaku/kotoba-r51/falsify/ReopenS022/lane`, then `git -C … checkout -q 59903b26…`): `python3 -B verifiers/check_overlap_levers.py` printed "overlap levers backed 7 of 7 clients", exit_default=0. `--fetch` printed "quotes found on live pages 7 of 7", exit_fetch=0; line "FETCH Claude Code: quote found (https://code.claude.com/docs/en/skills)". Python 3.14.8.
5. Probe test (clone module imported with bytecode writing off): quote_on_page(.md bytes) True; quote_on_page(HTML bytes) False.
6. Row history (python `git show` at 956ee16, a78fec1, bf109ca, 34cfffb^, 34cfffb, HEAD): nested clause absent at a78fec1, present from bf109ca; 34cfffb changed only used-by. `git log 956ee16..HEAD -- corpus/SOURCES.md` lists 34cfffb, bf109ca, a78fec1.
7. Read: .ufo/waves/round-51/build/SrcClaudeCode.md lines 51-58 (F3).

## Residual risk and verification gaps
- All evidence is documentation. How Claude Code actually selects under the nested rule is unmeasured.
- Keyword search plus reads of matches and selection sections; I did not read all 1,234 lines. An unindexed rule would not appear (round-50 had the same gap).
- The counter does not check the cited line; the line 886 check is mine.
- The F3 counter gap comes from reading code; I did not mutate the row to prove it.
- Not run: `--self-test`; checks on the other six rows; C1 freshness.
- The HTML route changed since its recorded hash; the .md route did not.

## Tooling
No installs or updates. Used system curl, sha256sum, cmp; python3 3.14.8 (standard library only); git in the lane with read commands only (show, log, cat-file, rev-parse); clone and checkout only in my scratch directory.
