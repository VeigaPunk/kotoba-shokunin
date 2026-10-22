# ReopenS029 — Gemini CLI row (C2), round 51 falsify, lane HEAD 59903b26

Verdict: HOLDS-BOUNDED. The quote, the lever and held-by cells, and the S029 registry facts hold on the bytes I fetched today. The effect cell "removed everywhere" needs its scope and its inference stated, and the entry's Limits bullet on secondary pages is wrong for Gemini. No counted row or count changes.

Scope: Gemini CLI row in corpus/knowledge/skill-overlap-levers-round51.md (line 25, § Levers by client); SKILL.md line 401 (§ Anti-patterns, "Overlap levers by client"); S029 in corpus/SOURCES.md line 42; corpus/lessons/round-51.md § Gate (line 28) and § Admitted (line 30). The four lane files are byte-identical to HEAD 59903b2637689739a5b9901956301da72d0effe1 (sha256 prefixes 5586347918c9, 60786fb4d890, 5608806fe802, 437cdcc04c3e; identical=True for each).

## Verdict per point

1. Quote: HOLDS.
   - Verbatim on line 94 of the fetched page (5,763 B): "- `/skills disable <name>`: Prevents a specific skill from being used." The quote is 10 words by whitespace split (the seat counted 11 with the bullet; both are under 25).
   - It contains the exact backtick span `/skills disable <name>`. The SKILL.md key-term cell is the same string.
   - The quote occurs on line 94 only.
2. Surrounding section: lever HOLDS; held by HOLDS; effect HOLDS-BOUNDED.
   - Lever "a session command disables one named skill": the section "### In an interactive session" (lines 86-97) lists the session commands; line 94 is the disable command.
   - Held by "user or operator": the NOTE at lines 73-76 says `/skills disable` and `/skills enable` default to the `user` scope, with `--scope workspace` as the other option. No Gemini page I read uses the word "operator".
   - Effect "removed everywhere": bounded three ways.
     a. Line 94 says "Prevents a specific skill from being used." Removal from the model's candidates is not stated. It follows from lines 20-22 ("injects the name and description of all enabled skills into the system prompt") and from tools/activate-skill.md § Usage ("You cannot invoke this tool manually."). The seat labelled this chain [INFERENCE] (SrcGemini.md, paragraph beginning "Lever 1 is the one", lines 53-60). The entry states it as documented.
     b. The NOTE at lines 73-76 limits the reach to the chosen settings scope. `--scope workspace` removes the skill in one project. "Everywhere" is true at user scope only.
     c. No page I read says whether `activate_skill` refuses a disabled name (gap, see below).
3. S029 row and lesson: HOLDS.
   - Row (SOURCES.md:42): id S029; kind docs; tier A; status mined. Source https://geminicli.com/docs/cli/skills/ sits under https://geminicli.com/docs/, the verifier's pinned Gemini prefix (check_overlap_levers.py line 132). used-by names corpus/knowledge/skill-overlap-levers-round51.md.
   - Lesson: S029 appears at lines 51, 55 and 61. Lines 51-55 (under ## Gate, ### Admitted) record the re-open with hash 8e1b4cbe… and quote skills.md:94; line 61 records the used-by change that adds the entry.
   - The row's recorded fetch (200, 5,763 B, 8e1b4cbe…) matches my fetch.
   - The row's teaches sweep counts reproduce on my bytes: overlap 0, ambigu 0, tie-break 0, conflict 0, "multiple skills" 1 (line 51), "same name" 1 (line 51), 1024 0.
   - The row cites skills-best-practices.md:16 ("Avoid overlap") and :24 ("~100 words"). Both match my fetch of that page (200, 3,257 B). The row's fetch record covers only skills.md. The best-practices fetch is recorded in SrcGemini.md lines 34-35, which the contract accepts as an evidence location.
4. Rule sweep: HOLDS-BOUNDED.
   - The sweep with the assignment's pattern on the fetched page hits lines 11, 21, 33, 35, 38, 41, 49, 51, 52, 53, 73, 97 and 101. Rule-bearing hits are line 38 (tier order) and lines 49-53 (precedence between skills that share a name, and alias precedence inside a tier). The rest are substring hits ("capabilities", "tiers", "prettier-ignore", "utilities") or line 33 ("prioritize the skill's procedural guidance"), which ranks guidance against other guidance, not one skill against another.
   - For two differently named skills whose descriptions both match, the page gives no rule. Lines 20-24 inject all enabled skills and activate on description match, with no tie-break.
   - So "none decides between two skills that both remain candidates" holds for levers (the SKILL.md sentence is lever-scoped) and for differently named skills. Read flat, it is false, because lines 51-53 decide between two skills that share a name. The seat's sentence "documents no rule at all for choosing between two skills whose descriptions both match" (SrcGemini.md lines 94-96) is overbroad for same-name copies.
5. Freshness: HOLDS.
   - Re-fetched 2026-10-22T15:14:59Z: 200, 5,763 B, sha256 8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590. The recheck prefix matches.
   - Verifier live run ended 15:18:28Z: "quotes found on live pages 7 of 7".
   - Not re-read: the Last-Modified header. The body hash matches, so the bytes are unchanged.

## Findings (severity order; all LOW, none changes a counted row)

F1 LOW: the Limits bullet is wrong for Gemini (knowledge file lines 94-96). It says the secondary pages checked by LeverOtherPages add only all-or-nothing switches, and that "none adds a per-skill lever missing from the skills pages". For Gemini, LeverOtherPages checked only the settings reference (LeverOtherPages.md line 19). It did not check the CLI reference or the configuration reference, and those two carry per-skill levers that the entry's own "Other levers" paragraph (line 35) names:
   - `gemini skills disable <name>`: cli-reference.md:130, "Disable an agent skill".
   - `skills.disabled`: configuration.md:2295-2296, "List of disabled skills." (a per-skill list, persisted).
   Fix: scope the bullet to the pages LeverOtherPages checked, or name these two levers. Both have the same effect as S029, so no count changes.

F2 LOW: the effect cell omits the scope (SKILL.md line 401; knowledge file line 42). The NOTE at lines 73-76 gives user scope by default and workspace scope with `--scope workspace`. "Removed everywhere" holds only at user scope. Suggested text: "removed in the chosen settings scope (user by default)".

F3 LOW: the effect's reasoning is unlabelled. The effect needs lines 20-22 and the activate_skill page. The seat labelled the chain [INFERENCE]; the entry cites neither the lines nor the label. Fix: cite the lines or mark the inference.

F4 LOW (seat report wording, not the entry): SrcGemini.md lines 94-96 says the page "documents no rule at all for choosing between two skills whose descriptions both match". Its own lines 84-88 record the same-name rule. It should say "differently named skills".

F5 NOTE (provenance): the row's source cell is the HTML route, https://geminicli.com/docs/cli/skills/ (trailing slash). The quoted line numbers are from the .md route. The HTML route (200, 114,148 B) contains "Prevents a specific skill from being used." but writes the code span as `/skills disable &#x3C;name>`. The literal string `/skills disable <name>` does not occur in the HTML bytes. The row's anchor cell says the page was fetched as .md, so the disclosure is there. The verifier's live check falls back to the .md route (SrcGemini.md lines 32-33). No action beyond the disclosure.

F6 NOTE: the best-practices fetch sits outside the row's own fetch record (point 3). Acceptable under the contract, but the row would be self-contained with that hash.

## Evidence

Fetches (UTC; curl exit 0 unless stated; bytes files kept in /fast/scratch/hyaku/kotoba-r51/falsify/ReopenS029/):
- skills.md: 2026-10-22T15:14:59Z; HTTP 200; 5,763 B; sha256 8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590.
- skills-best-practices.md: 15:17:45Z; 200; 3,257 B; sha256 612c3b8396fdc6669702127975c5d4ec5ce59bd8355fdbfb837fdd83d3d524c3.
- skills/ HTML route: 15:17:45Z; 200; 114,148 B; sha256 b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640.
- google-gemini.github.io former host: 15:17:45Z; 404; 9,115 B.
- cli-reference.md: 15:19:23Z; 200; 16,561 B; sha256 2d445008576bc09564f6a204482d8f980272f159781b2a79e07de6abc8a87840.
- reference/configuration.md: 15:19:23Z; 200; 102,704 B; sha256 4fb90004ef3e4aeb3705ceeea4ab8a0d8e0e3aa4553293a1df035990740cc9ca.
- tools/activate-skill.md: 15:20:38Z; 200; 1,514 B; sha256 780be95b02937cd7e6f8285b07505b374d201f31ca7c05e40c8c024225f987be.

Commands and exit codes:
- `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>/lane && git -C <scratch>/lane checkout -q 59903b2637689739a5b9901956301da72d0effe1 && git -C <scratch>/lane rev-parse HEAD` → exit 0; prints 59903b2637689739a5b9901956301da72d0effe1.
- `python3 -B verifiers/check_overlap_levers.py` in the scratch clone → "overlap levers backed 7 of 7 clients"; exit 0.
- `python3 -B verifiers/check_overlap_levers.py --fetch` in the scratch clone → "quotes found on live pages 7 of 7"; Gemini line "FETCH Gemini CLI: quote found (https://geminicli.com/docs/cli/skills/)"; exit 0.
- Python 3 read-only byte check on the fetched page: quote on line 94 True; hit lines [94]; 10 words; backtick span True; overlap 0; ambigu 0; tie-break 0; conflict 0; "multiple skills" [51]; "same name" [51]; 1024 0.
- Python 3 read-only lane check: four files identical to HEAD; knowledge line 25 holds the quote and "(skills.md:94)"; SKILL.md line 401 key term matches; S029 cells as in point 3; lesson S029 at lines 51, 55, 61.
- Tools: `_grep` for the sweep pattern on the fetched page and for the build seat reports. No installs. Only curl, git and python3 (already present) were used. No edits in the lane, no jj command, no git write command.

Quotes (verbatim; each under 25 words):
- skills.md:94: "- `/skills disable <name>`: Prevents a specific skill from being used."
- skills.md:21-22: "tiers and injects the name and description of all enabled skills into the system prompt." (15 words)
- skills.md:51-53: "If multiple skills share the same name, the version from the higher-precedence location is used." (15 words)
- skills.md:73-76 (NOTE): "`/skills disable` and `/skills enable` default to the `user` scope. Use `--scope workspace` to manage workspace-specific settings." (17 words)
- tools/activate-skill.md § Usage: "The `activate_skill` tool is used exclusively by the Gemini agent. You cannot invoke this tool manually." (16 words)
- configuration.md:2296: "List of disabled skills." (lines 2295-2296 give `skills.disabled`)
- skills-best-practices.md:16-17: "Avoid overlap: Ensure your skill descriptions are distinct from one another and from the general capabilities of the model." (19 words)

## Residual risk and verification gaps
- No page I read says whether `activate_skill` refuses a disabled skill's name. The "everywhere" effect depends on this (F3). Not checked: using-agent-skills.md:33 (quoted by the seat as "Prevents a skill from being triggered"; not re-fetched).
- "Operator" as a holder appears on no Gemini page I read.
- The Last-Modified header was not re-read. Only the four lane files were compared with HEAD.
- The verifier matches key terms by exact set membership and exact code span. Its Gemini list includes the bare "skills disable", but no exact code span "skills disable" exists on today's bytes, so nothing is falsely accepted. Noted, not a finding.
