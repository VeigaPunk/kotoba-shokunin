# ReopenS024: opencode row of C2 (round 51 falsify)

VERDICT: HOLDS-BOUNDED. Point 1 HOLDS; point 2 HOLDS-BOUNDED; point 3 HOLDS-BOUNDED; point 4 HOLDS. The quote and the no-tie-break finding hold. The effect cell needs a per-agent bound, the S024 teaches cell contradicts its own page, and the Gate's reason for not correcting that cell is wrong.

Scope: lane HEAD 59903b2637689739a5b9901956301da72d0effe1 (rev-parse matched). Working-copy bytes equal HEAD for the five files in Evidence item 6. Scratch: /fast/scratch/hyaku/kotoba-r51/falsify/ReopenS024/. Tools installed or updated: none. Messages sent: none. Lane writes: this report only.

## Freshness (UTC)
- 2026-10-22T15:15:10Z, https://opencode.ai/docs/skills.md: HTTP 200, 5365 B, text/plain; sha256 f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561 (prefix as expected). The entry's own recheck line exits 0 at 15:21:33Z.
- 2026-10-22T15:17:50Z, https://opencode.ai/docs/skills (HTML route): HTTP 200, 73201 B, sha256 4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0 (matches the S024 row); footer "Last updated: Oct 20, 2026" present once.
- The page has no version string. The round-47 sweep excluded these docs; its note reads "documents keys 1.19.3 lacks" (SOURCES.md:98). This item did not test the pinned 1.19.3 binary.

## Point 1: quote, HOLDS
- Entry line 24 and SKILL.md line 400 cite "Check permissions—skills with `deny` are hidden from agents" (skills.md:230).
- Page line 230, verbatim: `4. Check permissions—skills with `deny` are hidden from agents`. Eight words. The `deny` span is an exact backtick span.
- Caveat: line 230 is a troubleshooting bullet under "If a skill does not show up". The lever cell's "rejects loading it" is not in the quote. It appears only in the permission table at line 153, which the entry does not cite.

## Point 2: lever, held by, effect, HOLDS-BOUNDED
- Lever: HOLDS. § Configure permissions (lines 133-156) defines `permission.skill` patterns in opencode.json (135-148), the table at 150-154 ("`deny` | Skill hidden from agent, access rejected", line 153), and wildcards that match skill names (156).
- Held by "user or operator": BOUNDED. A custom agent's own frontmatter can set `permission: skill:` (164-171), so the agent-definition author also holds the lever.
- Effect "removed everywhere" (SKILL.md line 400; entry Finding 1, line 42): OVERSTATED. The page names "global defaults" (162) that "specific agents" can override, and its built-in `plan` example re-allows `internal-*` (174-188). The entry's Limits do not mention this. Suggested wording: "removed from every agent by default; a per-agent permission can allow it back". The counter accepts "removed everywhere" as a fixed string (check_overlap_levers.py:119-120, 351-352) and never checks it against the page.

## Point 3: S024 row, HOLDS-BOUNDED
Holds (SOURCES.md line 37; counter evaluate, check_overlap_levers.py:364-381): tier A; kind docs; status mined; URL https://opencode.ai/docs/skills under the counter prefix https://opencode.ai/docs/ (line 131); used-by names corpus/knowledge/skill-overlap-levers-round51.md; the round-51 lesson § Gate names S024 (lines 51-55 re-open at the 15:08Z fetch; 60-61 used-by; 63-67 teaches note; 71-72 rejected superseding row).

Defects:
- 3a. The teaches cell says "its only collision controls are name uniqueness across locations and `opencode/autoinvoke: "false"`". The page's § Configure permissions and line 230 name a third control that removes a named skill from the candidates, which the entry counts as a lever. The Gate concedes the gap (lines 63-65).
- 3b. The row's scope (it asks how a skill's description reaches the model and whether the page documents a tie-break) and anchor (skills.md 29-48, 70-73, 108-129, 223-231) do not name § Configure permissions (133-156). The counter does not check teaches or scope (lines 364-412), so "7 of 7" does not show that the row teaches the lever.
- 3c. The Gate declines the contract's correction route. Contract rule 2 (.ufo/waves/kaika/SOURCES-CONTRACT-v1.md) says "A correction is a new row whose `teaches` opens `supersedes S0NN —`". The Gate refuses because a superseding row "would add a W04 duplicate-URL warning" (lines 65-67, 71-72). The fleet census validate mode does not support that reason (Evidence item 9):
  - same scope, superseding row below S024: no E04, no W04, exit 0;
  - same scope, superseding row above S024: E04 on S024, exit 1, so placement matters;
  - different scope: W04 warning only, exit 0; the real registry already carries three W04 warnings at exit 0;
  - control, same scope, no "supersedes": E04, exit 1.
  Fix: a new row placed below S024 whose teaches opens "supersedes S024 —" and whose anchor names lines 133-156.

## Point 4: tie-break sweep, HOLDS
- Assigned command (Evidence item 4): 3 hits, exit 0. Line 45 (opencode/autoinvoke keeps a skill "out of model-facing auto-selection guidance"); line 73 ("Keep it specific enough for the agent to choose correctly."); line 129 ("They can still be selected manually and loaded by exact name."). None decides between two candidate skills.
- Broader case-insensitive sweep (same terms plus deny, permission, duplicate, same name, unique): line 23 "loads any matching" (every match loads; no selection rule); line 229 "Ensure skill names are unique across all locations" (a precondition; no outcome stated if violated).
- Residual gap, between permission rules rather than skills: lines 139-147 put `"*": "allow"` and `"internal-*": "deny"` in one object. `internal-docs` matches both, and the page names no winner. The entry's claim that a `deny` pattern hides a skill holds where that deny rule is the applicable one.

## Extra finding: author-held lever left out of the opencode row (medium)
- Lines 42-48 and 128-129: a skill's own frontmatter `metadata["opencode/autoinvoke"]` set to `"false"` keeps it out of `<available_skills>`, and manual selection stays. That is the "automatic choice off with manual use kept" effect the entry gives VS Code, Claude Code and Codex (Finding 1, lines 42-43). The holder is the skill author, yet Finding 3 (lines 51-53) lists author-held flags for those three only.
- The entry says "not counted" with no reason (lines 28-36). The counter's REVIEWED_LEVERS already lists `opencode/autoinvoke` as a reviewed removal key term (check_overlap_levers.py:149). The entry and the counter disagree.
- SKILL.md line 400 gives opencode one lever, held by "user or operator". An author who owns an opencode skill is not told they hold one.

## Instrument notes
- The citation location is never checked. QUOTE_CELL (check_overlap_levers.py:109) matches the location but captures only the quote; parse_entry_table keeps only the quote (lines 259-263), and evaluate never sees the location. Probe (Evidence item 10): scratch line 24 changed to "(skills.md:5)"; the counter still says "7 of 7", exit 0.
- The live probe tries the bare URL first (fetch_probe, lines 446-453). For opencode it matched the HTML route (`<code dir="auto">deny</code>`), not the hash-pinned .md. The .md also contains the sentence (Evidence item 3), but this check did not test the pinned bytes.
- held by and effect are checked against fixed vocabularies only (lines 118-120, 345-352).

## Evidence (commands and exit codes)
1. `date -u +%Y-%m-%dT%H:%M:%SZ && curl -sS -o <scratch>/opencode-skills.md -w 'status=%{http_code} bytes=%{size_download} url_effective=%{url_effective} content_type=%{content_type}\n' https://opencode.ai/docs/skills.md; echo curl_exit=$?` gives 2026-10-22T15:15:10Z, status=200 bytes=5365, curl_exit=0. `sha256sum` gives f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561. `wc -l` gives 230 newline-terminated lines (231 lines as the read tool counts them).
2. `curl -fsSL https://opencode.ai/docs/skills.md | sha256sum | grep -q '^f10ced73'; echo recheck_exit=$?` gives recheck_exit=0 (15:21:33Z).
3. `grep -nF 'Check permissions—skills with `deny` are hidden from agents' <page>; echo grep_exit=$?` gives "230:4. Check permissions—skills with `deny` are hidden from agents" and grep_exit=0. `printf '%s' '<quote>' | wc -w` gives 8. `grep -c deny <page>` gives 3 (lines 143, 153, 230).
4. `grep -niE 'overlap|conflict|precedence|tie|both|choose|select|priorit' <page>; echo sweep_exit=$?` gives lines 45, 73, 129 and sweep_exit=0. `grep -ciE` with the same pattern gives 3, exit 0.
5. `curl -sS -o <scratch>/opencode-skills.html -w 'html_status=%{http_code} html_bytes=%{size_download}\n' https://opencode.ai/docs/skills; echo html_curl_exit=$?` gives html_status=200 html_bytes=73201, html_curl_exit=0. sha256 4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0. `grep -c 'Oct 20, 2026' <html>` gives 1.
6. `git -C <lane> rev-parse 59903b2637689739a5b9901956301da72d0effe1` gives the same full hash. For five paths, `git -C <lane> show 59903b26…:<path> | sha256sum` equals `sha256sum <lane>/<path>`: SKILL.md 60786fb4…; corpus/knowledge/skill-overlap-levers-round51.md 55863479…; corpus/SOURCES.md 5608806f…; corpus/lessons/round-51.md 437cdcc0…; verifiers/check_overlap_levers.py e871fa03… (all five pairs equal).
7. `git clone -q <lane> <scratch>/lane; echo clone_exit=$?` gives 0. `git -C <scratch>/lane checkout -q 59903b26…; echo checkout_exit=$?` gives 0.
8. `python3 -B <scratch>/lane/verifiers/check_overlap_levers.py --root <scratch>/lane; echo counter_exit=$?` gives "overlap levers backed 7 of 7 clients", counter_exit=0. With `--fetch`: "quotes found on live pages 7 of 7", fetch_counter_exit=0.
9. Census probes, fleet script run read-only from scratch: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-22 --file <probe>; echo exit=$?`. t1 (same scope, below S024): W03 only, exit 0. t2 (same scope, above S024): E04 for S024, exit 1. t3 (different scope): W04 for S099, exit 0. t4 (control, same scope, no supersedes): E04 for S099, exit 1. Real registry copy at 59903b26: W04 for S018, S019, S021, exit 0.
10. Mutated counter: scratch entry line 24 changed to "(skills.md:5)" with the edit tool, then `python3 -B … --root <scratch>/lane; echo counter_exit=$?` gives "overlap levers backed 7 of 7 clients", counter_exit=0.
11. Reads (no exit code): page lines 1-231; SKILL.md 380-410; SOURCES.md 1-26 and line 37 raw; lesson lines 5-8 and 28-72 (grep output); counter lines 71-161, 250-268, 319-417; contract rules 1-2; census script header lines 1-48 and code lines 626-655 (fleet root, read-only).

## Residual risk and gaps
- Documentation only. No opencode runtime was run, so overlapping permission precedence and per-agent override behaviour are unverified at runtime.
- The page is unversioned and the lane pins opencode 1.19.3 (S015, S016). This item did not test whether 1.19.3 implements `permission.skill` or `opencode/autoinvoke`.
- No row or entry was edited. The fixes above are for the L1 to decide.
