# Round-50 falsify: ReopenS029 (SOURCES row S029, lesson Gate line, census S029 bullet)

Verdict: HOLDS-BOUNDED. Applies to SOURCES.md row S029 (Gemini CLI Agent Skills docs), the Gate row at corpus/lessons/round-50.md:63, and the census bullet at corpus/knowledge/sibling-overlap-census-round49.md:218-220, judged at master 956ee1676e4c18480bce8ac3993541462be76e11. The bytes, the quote, the tier, the census bullet and all ten sweep counts hold. Three items need a fix before the row is fully evidenced: a companion page with no fetch record (F1), a universal "no tie-break" clause that its counter cannot turn on (F2, Q26), and a teaches sentence that says more than the primary page (F3). One Gate URL/time mismatch needs a fix (F4).

Scope: read-only on the lane. The only file written in the lane is this report. Scratch work: /fast/scratch/hyaku/kotoba-r50/falsify/ReopenS029/. Installs or upgrades: none (curl, sha256sum, grep, and Python 3 were already on the host). Subagents: none (leaf seat). No code changed, so the lsp device was not needed.

Adjacency: for Gemini the negative is name-keyed, the same shape the seat report calls the round-49 Claude rows (S022, S023; seat line 52; not re-checked here). It supports the census's craft consequence that an author controls arbitration between differently named skills only through description text. That consequence depends on the bounded claim in F2.

## Per-check verdicts

| # | Check | Verdict | Basis |
|---|---|---|---|
| 1 | skills.md bytes and sha256 vs row | HOLDS | 5763 B, sha256 8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590 (row prefix 8e1b4cbe… matches). Fetched 13:32:15Z; first answer came from edge cache (x-cache HIT). Cache-busted origin fetch at 13:33Z (x-cache MISS): same bytes and sha256. |
| 2 | HTML route bytes and sha256 | HOLDS | 114148 B, sha256 b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640 (row prefix b1789501… matches). |
| 3 | "byte-identical on re-fetch at 12:34:04Z" | HOLDS-BOUNDED | Not re-observed (the 12:34 bytes were not kept). Today's bytes equal the recorded hash, which is consistent with the claim. |
| 4 | Companion page skills-best-practices.md (cited at :8-17, :16, :24) | FAILS (record gap) | The row, the Gate and seat report SrcGeminiCliSkills.md give no URL, time, byte count or hash for it. Seat line 50 says only "fetched at the same time". My fetch: https://geminicli.com/docs/cli/skills-best-practices.md, 200, 3257 B, sha256 612c3b8396fdc6669702127975c5d4ec5ce59bd8355fdbfb837fdd83d3d524c3, 13:33Z. The only other record I found is a sibling falsify file, .ufo/waves/round-50/falsify/CriticFrontierSweep.md:79 (13:31:29Z, 3257 B, 612c3b83), and it matches. |
| 5 | Quote verbatim, location, at most 25 words | HOLDS | "If multiple skills share the same name, the version from the higher-precedence location is used." skills.md:51-52 (line 51 ends "higher-precedence"; line 52 begins "location is used."). 15 words. Also present in the HTML route. |
| 6 | Tier A | HOLDS | Vendor page with recorded bytes. The round-48 and round-49 verifier spot-checks call the same kind of row correctly tiered (corpus/lessons/round-48-verifier-spotcheck.md:130, "primary and correctly tiered"; round-49-verifier-spotcheck.md:172, "a primary vendor page and correctly tiered"). A grep over corpus/ found no single written tier legend, so this rests on that convention. |
| 7 | Scope cell | HOLDS-BOUNDED | "(vendor documentation, not a measurement of omp or opencode)" is honest. The opening clause "How Gemini CLI discovers and activates skills" reads as runtime behaviour, and the Gemini runtime was not exercised (seat, "Out of scope"). Suggest: "what Gemini CLI's documentation says about how it discovers and activates skills". |
| 8 | Teaches cell vs the page | HOLDS-BOUNDED | Confirmed as stated: tiers run lowest to highest, built-in < extension < user < workspace (skills.md:37-47); `.agents/skills/` beats `.gemini/skills/` within a tier (skills.md:52-53, "Within the same tier (user or workspace)"); the one "Avoid overlap" line is skills-best-practices.md:16; the soft budget "~100 words" is skills-best-practices.md:24. Overstatements are F2 and F3. |
| 9 | Census S029 bullet vs page | HOLDS | Says 5,763 B; the quote is at skills.md:51-52; overlap, ambigu, tie[- ]?break and conflict are each 0. All match (commands below). |
| 10 | Ten-pattern sweep counts | HOLDS | All ten reproduce exactly on skills.md (commands below). Each counter responds to its own variants (positive control) and to edits of the page (mutants m1-m3). |
| 11 | Gate row, lesson line 63 | HOLDS-BOUNDED | Quote is verbatim and the 12:28:45Z time matches the skills.md fetch. The URL cell names the HTML route, which the seat fetched at 12:28:34Z (seat line 11). See F4. |
| 12 | Former official host is dead | HOLDS | google-gemini.github.io/gemini-cli-docs/docs/cli/skills/ and the no-slash form both return HTTP 404, redirects=0 (13:33Z). |
| 13 | Upstream README points at geminicli.com | HOLDS | raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md: 200, 12107 B, sha256 7235196f55461732c246c20ce9996cc56ba2e52641f183ccf4e6493bd93c1c94 (13:35Z); line 28 "[documentation](https://geminicli.com/docs/)". |
| 14 | Freshness | HOLDS | Origin Last-Modified Fri, 16 Oct 2026 02:36:07 GMT; etag 0957231f9c46588b9bdf8e23f4ec7fb73d8ac709348b0d3735b6f5214e24058e (same as the seat's header); bytes unchanged at 13:33Z. Recheck 90d is consistent with the row's opened date. |

## Findings (by severity)

F1, medium: companion page has no fetch record. The S029 anchor cell cites skills-best-practices.md:8-17, and the teaches cell cites :16 and :24, with no URL, access time, byte count or hash. The Gate says "the seat report holds the full fetch record" (lesson lines 53-54), but seat report SrcGeminiCliSkills.md records only skills.md and the HTML route (lines 11-13). Fix: add https://geminicli.com/docs/cli/skills-best-practices.md (2026-10-22T13:33Z, 200, 3257 B, sha256 612c3b83…) to the row or the seat report, and name each companion page the row relies on.

F2, medium, Q26 (corpus/QUALITY.md:37): a universal negative is not turned on by its counter. The teaches cell says the page "states no tie-break between two skills with different names and overlapping scope". The census lead bullet (census lines 195-200) says "No page states a rule for two skills with different names whose descriptions both match", and "Every documented 'which one wins' rule found so far is keyed on the skill *name*". The counters only count words. Mutant m4 adds a tie-break with no sweep term and leaves all ten counts unchanged. Mutant m5 adds a 200-character cap and leaves 1024 at 0. My own full read of all five Gemini pages finds no distinct-name rule and no description cap, so the claim is true on reading. The row does not say that the counters cannot carry it. Fix: bound the clause to the swept terms, or add "a full read of the five pages found no such rule" with line numbers. Bound "no description length cap" the same way.

F3, low-medium: the teaches sentence "The description is the only skill text in context before a trigger" says more than the primary page. skills.md:20-22 says the system prompt receives "the name and description of all enabled skills", and skills.md:69-70 says "Only skill metadata (name and description) is loaded initially." The "only information the model has before activation" sentence is on the companion page (skills-best-practices.md:8-9). The row uses the companion's stronger wording and does not say the two pages differ. Fix: state both, for example "name and description are injected (skills.md:20-22); the companion page calls the description the only information before activation (skills-best-practices.md:8-9)".

F4, low: Gate row URL. Lesson line 63 gives the HTML URL with 12:28:45Z, which is the skills.md fetch time. The quote location skills.md:51-52 is the .md file. Fix: use https://geminicli.com/docs/cli/skills.md in the URL cell, or change the time to 12:28:34Z for the HTML route.

F5, low: the S029 anchor cell omits "§ Progressive disclosure (skills-best-practices.md:24)", which the teaches cell cites. Add it.

F6, low: scope wording, see table row 7.

## Counter controls (Q25, corpus/QUALITY.md:36)

- positive-control.txt, one line per target term: overlap 2, ambigu 2, precedence 1, tie[- ]?break 4, conflict 1, multiple skills 1, same name 1, prioriti 1, 1024 1, truncat 2. Every pattern matches.
- negative-control.txt, neutral text: every pattern gives count 0 (exit 1).
- Mutants of skills.md (base: overlap 0, ambigu 0, precedence 4, tie 0, conflict 0, multiple skills 1, same name 1, prioriti 1, 1024 0, truncat 0):
  - m1 adds "When two skills overlap in scope, a tie-break picks the more specific one.": overlap 0 to 1, tie[- ]?break 0 to 1.
  - m2 removes the same-name sentence: same name 1 to 0, multiple skills 1 to 0, precedence 4 to 3.
  - m3 adds "Descriptions are capped at 1024 characters.": 1024 0 to 1.
  - m4 adds "If two skills both match a request, the one listed first is used.": no count changes.
  - m5 adds "Descriptions must stay under 200 characters.": 1024 stays 0 (exit 1), and truncat, overlap and tie stay 0.

## Evidence (commands and exit codes)

- `curl -sS -D md.headers -o skills.md -w '%{http_code} %{size_download}' https://geminicli.com/docs/cli/skills.md` gives 200, 5763 B. `sha256sum skills.md` gives 8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590 (exit 0).
- The same command with `https://geminicli.com/docs/cli/skills/` gives 200, 114148 B, sha256 b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640.
- `curl ... 'https://geminicli.com/docs/cli/skills.md?cachebust=r50-falsify-20261022'` gives 200, 5763 B, x-cache MISS, same sha256.
- Companion pages (same curl pattern): skills-best-practices.md 200, 3257 B (612c3b83…); creating-skills.md 200, 6705 B (b7061545…); using-agent-skills.md 200, 3052 B (9e61fb7c…); tutorials/skills-getting-started.md 200, 5866 B (b4169fbd…).
- The old host URLs return 404 with `-o /dev/null -w '%{http_code}'`.
- Sweep, `grep -ciE '<pattern>' skills.md` (grep exit 0 when count is 1 or more, exit 1 when count is 0):

| pattern | count | exit | matching lines |
|---|---|---|---|
| overlap | 0 | 1 | none |
| ambigu | 0 | 1 | none |
| precedence | 4 | 0 | 38, 49, 51, 53 |
| tie[- ]?break | 0 | 1 | none |
| conflict | 0 | 1 | none |
| multiple skills | 1 | 0 | 51 |
| same name | 1 | 0 | 51 |
| prioriti | 1 | 0 | 33 ("prioritize the skill's procedural guidance") |
| 1024 | 0 | 1 | none |
| truncat | 0 | 1 | none |

- The same grep over the other pages: skills-best-practices.md has overlap 1 (line 16) and 0 for the rest. creating-skills.md has precedence 1. using-agent-skills.md has precedence 2, multiple skills 1 and same name 1. skills-getting-started.md has 0 for all ten. These match the seat's numbers.
- I read all five pages in full. Only the same-name rule (skills.md:51-52, using-agent-skills.md:19-20) and the tier order states a collision rule. No page gives a rule for distinct names or a description length cap.

## Residual risk and verification gaps

- The 12:34:04Z re-fetch was not re-observed; its bytes were not kept.
- The Gemini CLI runtime was not exercised. Every claim is documentation-level.
- The HTML-route sweep (the seat's "precedence 5" on the navigation) was not re-run. The row cites skills.md only.
- The seat reports a 1024-character cap in Gemini's skill-creator validator (vendor code, seat F4). I did not check it. That code row was drafted but not written, so nothing in SOURCES.md depends on it.
- Sibling file CriticFrontierSweep.md was used only to locate a companion fetch record. My verdicts rest on my own fetches.
