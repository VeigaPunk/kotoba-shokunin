Result: DONE — `verifiers/check_command_files.py` @ `3de87aad29e960c95ed35840442f424c48c29729` implements every plan-§-C1 conjunct (verified sentence by sentence, all changes vs v2 are the planned swaps); one genuine prose divergence found: the plan defines G over "backed rows" while the counter counts only FOUND rows (code/docstring consistent, stricter); plus several unstated-but-stricter or unstated-but-looser checks itemized under Q31.

Seat: ReviewC1Counter (BUILD wave, depth axis). Scope: counter vs `plans/round-58.md` § C1 at the freeze commit.
Reviewed revision: `3de87aad29e960c95ed35840442f424c48c29729` in sandbox clone `/fast/scratch/hyaku/kotoba-r58/ReviewC1Counter` (lane file sha256 `aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c` == sandbox copy; lane working copy currently identical). File: 1968 lines.
Method: full read of the counter; AST/source comparison against `check_plugin_manifests.py` v2 (sha `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`, byte-identical at base `f56f6e1` and freeze `3de87aa`, so "the v2 pinned map"/"v2 behaviour" is unambiguous); `--self-test` and two end-to-end runs in the sandbox.

## 1. Self-test run (pasted, sandbox `/fast/scratch/hyaku/kotoba-r58/ReviewC1Counter`)

```
$ timeout 900 python3 -B verifiers/check_command_files.py --self-test
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
EXIT=0
```

End-to-end spot runs (no `--fetch`, read-only git against the sandbox clone; the counter resolved the sandbox itself via `lane_dir()`, not the lane):

```
$ python3 -B verifiers/check_command_files.py --rev 3de87aad29e960c95ed35840442f424c48c29729
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
counter rev 3de87aad29e960c95ed35840442f424c48c29729
custom command files backed 0 of 0; new ground not computed (needs --fetch)
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
EXIT=1

$ python3 -B verifiers/check_command_files.py --rev deadbeef
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
could-not-evaluate: --rev 'deadbeef' is not a full 40-hex commit hash
EXIT=2
```

## 2. Plan § C1 conjunct → implementing code (sentence by sentence)

Plan: "Surface: `SKILL.md` gains `### Custom command files by client` … grounded in `corpus/knowledge/command-files-round58.md` and new `corpus/SOURCES.md` rows opened 2026-10-23."
→ anchors `SKILL_HEADING`/`ENTRY`/`SOURCES`/`OPENED` at check_command_files.py:284,243,244,250; enforced via `skill_rows` :444-456, `entry_rows` :459-465, `sources_table` :469-477, opened check :722-723.

Plan: "Counter: `python3 -B verifiers/check_command_files.py --rev <rev> --fetch` (built pre-freeze from `check_plugin_manifests.py` v2; everything not named here is v2 behaviour)."
→ docstring :4-48; verified: 48 top-level functions byte-identical to v2 (incl. `host_ok`, `url_key`, `url_is_change_note`, `fetch` body, `held_*`, `predicate`, `new_ground`, `judge` plumbing); 29 constants byte-identical (incl. `HOSTS`, `TOKEN_RE`, `CLIENTS`, `MARKERS`, `REV_RE`). 13 functions differ; every diff is a planned swap (names/strings/grammar) or the plan-mandated boundary tightening in `token_span` — see §4.

Row-rule bullet → code:
- "Section heading line exactly `### Custom command files by client`" → :284 + `section_lines` exact-line match :433 (note: `ln.rstrip()` tolerates trailing whitespace; fence-awareness absent — see Q31-6).
- "first table header `| Client | Command files | What a file sets | Action |`" → `SKILL_HEADER` :285 + `skill_rows` :449-452 (FIRST table only, 4-cell prefix compare after `clean()` — see Q31-5).
- "clients Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode" → `CLIENTS` :255-256; exact-match `client_name` :387-389 at :759,:785; duplicate-client disqualify :760-761.
- "HOSTS = the v2 pinned map" → :257-274, AST-identical to v2 :227-244.
- "token = first backticked span of the Command files cell" → :764-765 (`BACKTICK_RE` :294).
- "action cell ≥ 3 words" → :782-784.
- "path regex of v2" → `TOKEN_RE` :288, AST-identical to v2 :258; applied :579.
- "after stripping one leading `~/` or `./` it has ≥ 2 path segments and its first segment starts with `.`" → :580-584 (one `~/`/`./` stripped :580; one trailing `/` stripped :581-582 — the plan's "final non-empty segment" phrasing covers this; `parts[0].startswith(".")` :584).
- "final non-empty segment, split on `-`, `.`, `_`, holds `command|commands|prompt|prompts` case-insensitively" → :588-589 with `COMMAND_WORDS` :290, `seg_words` :564-565, `SEG_SPLIT_RE` :289.
- "no segment split on `-._` holds skill/skills/agent/agents/rule/rules/plugin/plugins/extension/extensions" → :590 with `NOT_COMMAND_WORDS` :291-293.
- "no non-final segment holds a dot other than as its first character (E7)" → :586-587.
- "no other client's marker (foreign-name guard)" → `MARKERS` :275-283, `foreign_marker` :592-598, applied :773-776 (only when token well-formed; token still counts in K via `in_k=True` :772 — see §4.3).
- "E5 (a token shared by two client rows disqualifies both)" → `shared_tokens` :666-675 (casefold of `normalise(first backticked span)`, any row incl. unlisted names) + :777-781.

"Backed iff v2's backing conjuncts hold with the entry table `| Client | Command files | Source | Quote |`":
- entry table → `ENTRY_HEADER` :286, `entry_rows` :459-465 (first header-matching table anywhere in the file); row picked = first clean row for the client :788-797.
- "the quote 6–25 words" → `MIN_WORDS`/`MAX_WORDS` :248-249, enforced :697-699 (on the backtick-stripped quote `q_plain` :696).
- "containing the token (or its normalised form) case-sensitively at segment boundaries" → :700-704 via `token_span` :615-630 using `first_boundary` :862-879 (BOTH ends: left ∈ `BOUNDARY_PREV` :300, right not letter/digit/`_`/`-`; round-58 change vs v2, plan-mandated).
- "matching `(?i)\b(commands?|prompts?)\b` outside the token span" → `COMMAND_WORD_RE` :298, `command_word_outside` :632-637, enforced :705-706.
- "the source a new tier-A `mined` row opened 2026-10-23" → S###-id shape :691-694 (`SID_RE` :295); id-not-at-base :710-711; row present :712-714; tier `A` :718-719; status `mined` :720-721; opened `2026-10-23` :722-723; URL-not-a-base-URL under v1.3 normalisation :729-730 (`url_key` :494-512, `base_url_keys` :515-523).
- "on the client's pinned host" → :731-732 via `host_ok` :546-561 (host or subdomain for bare hosts; exact path prefix for `github.com/<org>/<repo>`; dot-dot escape rejected :549-550).
- "(not changelog/release/news/blog)" → :736-738 via `url_is_change_note` :539-543 (`CHANGE_NOTE_WORDS` :536, decoded path, substring, case-insensitive).
- "the quote in the lesson `## Gate`" → :707-708 via `quote_in_gate` :653-655 + `gate_section` :809-821 (`## Gate` line-exact :815; section ends at the next `## ` line; `### ` lines inside count).
- "with `--fetch` the quote found on the live page" → fetch loop :1923-1932; `found_on_page` :933-941 requires the quote under v1.3 normalisation AND a token form at a boundary on the case-preserved page (see Q31-10: plan literally says only "the quote found"); `fetch` :904-931 (UA `…/58` :912, 30 s :914, ≤5 MiB :915,:925-926, one retry :909, redirect checks :918-923).

"Prints `custom command files found on the live page F of K; new ground G`" → `summary_line` :1061-1065; printed :1950. Byte-exact match (also self-tested :1768-1771). Non-fetch line :1066-1067 matches docstring :197-198.

"G = distinct casefold(normalise(token)) of backed rows with 0 case-insensitive segment-boundary hits in the base tree (`':!.ufo'`)" → `new_ground` :1079-1087 over `held` from `held_in_base` :1040-1057 (`ls_tree` :943-965 skips `.ufo` :959-960; NUL-byte blobs skipped :1034-1035; `held_in_text` :999-1019 casefold + `HELD_PREV` :303 left boundary + `held_right_ok` :1021-1031). BUT the code computes G over `counted` = FOUND rows :1933,:1936-1944, not over all backed rows — the plan's word "backed" vs docstring :170-171 "the FOUND clients". **Mismatch M1** (§3).

"Targets: T_F = 4 (margin 2 below the census 6), T_G = 3 (margin 1 below 4). Predicate … exit 0 iff F ≥ 4 and G ≥ 3 on `--rev <rev> --fetch`; receipt label `C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET)`."
→ `TARGET = 4` :246, `NEW_TARGET = 3` :247 (the plan's margins); `predicate` :1073-1076 returns 0 iff `found >= TARGET and ground >= NEW_TARGET` with fetch, always 1 without; called :1964. Receipt label is verbatim in the docstring :203-207 (`C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET)`). **Exact match.**

R4 routed defect ("the new C1 counter carries [a successful `main()` self-test arm] from birth") → :1805-1869: satisfying world → `main(["--rev", measured, "--fetch"])` exit 0 + exact found line :1841-1846; one-conjunct-broken world → exit 1 + correct partial line :1847-1862; `None`-target sentinel → exit 2 + `targets not frozen` :1863-1869. Docstring requirement stated :192-196; satisfied (self-test output above).

## 3. Findings (severity order)

**M1 — Low (text divergence; direction is stricter, cannot inflate the claim): plan says G counts tokens "of backed rows"; the counter counts only rows confirmed on the live page.**
`plans/round-58.md` § C1: `G = distinct casefold(normalise(token)) of backed rows with 0 … hits in the base tree`. Code: `counted = [r for r in backed if r.get("found")]` (:1933) and `ground = new_ground([r["norm"] for r in counted], held)` (:1944); held scan seeded from found tokens only :1936-1938. The counter's own frozen docstring says "among the FOUND clients" :170-171, so code and docstring agree; the plan prose is the loose reading. Consequence: a row that is backed but whose page fetch fails or whose token is absent on the live page contributes to G under the plan's wording but not under the counter; since G ≥ 3 must be met, the code can only under-deliver G vs the plan wording — it cannot make a weak claim pass. No predicate risk; flagging so receipts and the FALSIFY wave cite the docstring/code semantics (G-over-found), not the plan's "backed" wording. [INFERENCE on intent: the frozen spec + R7-style freeze discipline suggest the docstring is authoritative; no rule change proposed.]

**M2 — Info (looser than the plan's literal text, harmless): header/heading comparison is normalised.**
`clean()` :382-384 strips `` ` ``/`*` and lowercases before comparing, and only the first 4 cells are compared (`head[:len(SKILL_HEADER)]` :450), so `| **Client** | Command Files | … | Extra |` and a 5-column table pass; a heading line with trailing whitespace passes (`ln.rstrip() == heading` :433); a `### Custom command files by client` line inside a fenced code block also passes (no fence tracking, v2 behaviour). Plan literal text: "Section heading line exactly …; first table header `| Client | …`". All directions are lenient, not claim-inflating beyond what a reasonable reading already permits; recorded for completeness.

**M3 — Info: K (the "of K" denominator) is not defined in the plan; the code counts foreign-marker tokens in K.**
`in_k = True` at :772 precedes the foreign-marker rejection :773-776, so e.g. a Copilot-CLI row carrying a well-formed `.claude/commands/` token counts in K although it can never be backed. Docstring :113 defines K exactly this way; consistent, just unstated in the plan.

**M4 — Info: `TOKEN_RE` admits `*` in non-final segments.**
`TOKEN_RE` :288 allows `*` in any segment after the first, so `.claude/*/commands/` is well-formed; docstring :111 advertises only "a glob `*` … in the final segment". Plan is silent; self-test covers only final-segment globs. Tightening candidate for a later round, not a defect against the plan.

No other divergences found. The predicate, printed line, receipt label, targets, frozen constants and the R4 arm all match the plan verbatim.

## 4. Code checks the plan does not state (Q31)

Plan § C1 says "everything not named here is v2 behaviour"; the following are code checks (or behaviours) not named in the plan text. Verified present in the counter; where shared with v2, byte-identical by AST/source comparison.

1. `counter sha256 <hex>` first line :1893 (`self_sha` :337-341); `counter rev <rev>` second line :1918 (docstring :193-195).
2. Could-not-evaluate exit 2: non-40-hex rev :1903-1906 + `rev_ok` :351-353; rev not resolving `verify_rev` :356-360; missing lane `lane_dir` :314-334 (`LANE_FALLBACK` :254); git failure `git` :343-349; unreadable ls-tree/cat-file :946-948,:994-997; unreadable own bytes :1894-1896; `targets not frozen` :1961-1963.
3. `--json` :1889,:1945-1948 and `--self-test` exclusivity :1897-1900 (`argparse` error → exit 2 via ap.error).
4. (same as M2) header prefix-compare + normalisation; section_lines heading-in-code-block.
5. SOURCES row must have exactly 13 pipe-cells :474-476 (else "absent or malformed" :713-714); only the FIRST URL of the source cell is used :725.
6. Tracker-URL rejection :733-735 (`TRACKER_SEGMENTS` :526-527 — issue/pull/discussion/commit/compare path segments, any host).
7. E4: entry `Command files` cell must equal the SKILL.md token or its normalised form, case-sensitive :688-690 (`command_cell_matches` :660-663); entry source cell must be exactly one `S###` :691-694; a SECOND/garbage entry row for the client is ignored if a clean row exists :788-797.
8. Fetch guards: redirect off pinned hosts :918-919; redirect onto a base SOURCES URL :920-921; redirect onto a change-note URL :922-923; >5 MiB :925-926; any exception → not found :1929-1931.
9. FOUND requires a token form at a boundary on the case-preserved page :938-941 + `token_forms` :890-901 — stricter than the plan's "the quote found on the live page" (docstring states it :164-169). Also, token forms are passed through `page_plain` (`*`/`_`/backticks stripped), so e.g. a glob token can match its normalised form.
10. Quote-side checks run on the backtick-stripped quote `q_plain` :696-705.
11. Held-scan details: `.ufo/`-prefix exclusion only :959-960; NUL-byte blobs skipped :1034-1035; gitlink entries (kind `commit` in ls-tree) never read :951-952; line-based scan with `HELD_PREV` left chars :1006-1018 and the dot-suffix rule `held_right_ok` :1021-1031 (`.x` followed by alnum does not hold; bare `.`/`/` do).
12. E5 counts unlisted client-cell names as users :673-674 (self-test :1573-1575); two same-client-name rows sharing a token also flag E5 (:777-781; moot — :760-761 already rejects duplicates; self-test :1576-1578).
13. `skill_rows` reads only the FIRST table of the section; if its header mismatches, no later table is consulted :449-455. `entry_rows` scans ALL tables for the first header match, anywhere in the file :459-465 (not tied to a heading).
14. Missing measured-revision files are scored as empty (`git_show(...) or ""` :1910-1914) — reject-all exit 1, not exit 2; observed in the freeze-rev run above.
15. Self-test totals 244 assertions incl. the full R4 end-to-end block :1805-1869, `held_world` git-guard probes :1090-1122, predicate :1795-1803, output lines :1767-1793; `main`/`lane_dir`/`fetch`/`BASE`/`TARGET`/`NEW_TARGET` patched and restored (:1834-1838,:1870-1871,:1795-1803).

## 5. Residual risk & verification gaps

- The `--fetch` path against live pages was NOT executed (assignment scopes to `--self-test`; fetch path is exercised via stubbed `fetch` in the R4 self-test block :1838). The falsify wave's first real run will exercise redirects/limits live.
- M1 should be resolved in wording before receipts cite G: counter semantics = G over FOUND rows.
- `TOKEN_RE` middle-segment `*` (M4) and fence-unaware heading match (M2) are lenient spots a hostile SKILL.md could exploit only toward trivially-detectable forms; both predate this counter (v2).
- No mutants/controls run against this counter — out of scope (controls are the W0 pre-freeze receipts under `.ufo/waves/round-58/controls/`).

Tooling: no installs (system `git`, `python3` suffice). Lane untouched except this report; all execution confined to `/fast/scratch/hyaku/kotoba-r58/ReviewC1Counter` (checkout only, no commits).
