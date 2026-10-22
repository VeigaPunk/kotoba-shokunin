# ReopenS028: re-open of SOURCES row S028 (GitHub Copilot CLI plugin reference)

**Verdict: FAILS.** It applies to the `teaches` cell of SOURCES.md row S028 (the "one GitHub surface" clause and the 1,024-cap clause) and to the census sentence that governs the S028 sweep (census lines 200-201). Bytes, sha256, the Gate quote, the census S028 bullet, the ten-pattern counts and freshness HOLD.

Judged bytes: lane rev 956ee1676e4c18480bce8ac3993541462be76e11 (private clone at `/fast/scratch/hyaku/kotoba-r50/falsify/ReopenS028/lane`). SOURCES.md, census and QUALITY.md match the working copy by sha256 (E9). The round-50 lesson differs by one added row (F7).

## Verdict per check

| # | Check | Verdict | Basis |
|---|---|---|---|
| 1 | Bytes and sha256 match the recorded fetch (47,200 B, `d0d362cc…`) | HOLDS | E1-E4 |
| 2 | Gate quote and census quote are verbatim at `cli-plugin-reference.md:415`, 25 words or fewer | HOLDS | E6; 7 words |
| 3 | Tier cell `A` is honest | HOLDS-BOUNDED | Matches the lane's practice (round-48 spot-check, `corpus/lessons/round-48-verifier-spotcheck.md:130`). No tier rubric exists in the lane (F6) |
| 4 | Scope cell is honest | HOLDS | Duplicate component names, including skills; caps on manifest descriptions |
| 5 | `teaches` says no more than the page | FAILS | F1, F4, F5 |
| 6 | Census round-50 bullet for S028 matches the page (census 216-217) | HOLDS | Quote and location match; "name-keyed" is supported by :417 and diagram :447 |
| 7 | Census sentence governing the sweep ("located in the seat report", "about something else") | FAILS (Q26) | F2 |
| 8 | Ten-pattern `grep -ciE` counts reproduce | HOLDS | E5; all ten match the seat table |
| 9 | Adjacency | HOLDS-BOUNDED | F1, F3 |
| 10 | Freshness | HOLDS | E2, E3; no drift in about 65 minutes |

## Findings, most severe first

**F1 (high): `teaches` says "Copilot CLI is the one GitHub surface that documents a deterministic tie-break." This is false by the lane's own evidence.**
- The Copilot SDK skills page, which the lane fetched, documents a deterministic same-name rule. `how-tos/copilot-sdk/features/skills.md:685`, under `## Skill providers (experimental)` (:293) and `### Provider lifecycle` (:679): "A provider skill with the same name as a file-based skill replaces the file-based skill, and `skills.reload` reports a warning." Origin copy, 35,455 B, sha256 `64856ff4…` (E3, E4, E7).
- The seat report says the same thing. `.ufo/waves/round-50/build/SrcCopilotSkills.md` lines 17-19 list that sentence as one of GitHub's deterministic skill precedence rules.
- The lesson's rejection reason for the SDK page ("provider catalogs, not SKILL.md routing", `corpus/lessons/round-50.md:43-44`) does not address line 685. No row records the SDK page, so SOURCES.md alone hides the conflict.
- "The one" is a claim about all of GitHub. One page cannot establish it.
- Fix: delete "the one GitHub surface". Either record the SDK page as its own Tier A row or name the SDK rule in the S028 scope.

**F2 (medium, Q26 fails): census lines 200-201 say "Every non-zero hit is located in the seat report and is about something else (a same-name collision, a length cap, site chrome or an unrelated sense)."**
- The seat report does not locate five CLI-page lines: :31 (`conflict`), :107 and :402 (`precedence`), :152 (`same name`), :425 (`precedence`). Its quotes cover :411, :415 and :417 (seat line 93). Its anchors give :195 and :349 (seat line 107). The seat table gives counts only (E12).
- :107 and :402 are a which-one-wins rule for manifest files. A root `plugin.json` "takes precedence over" `.plugin/plugin.json` and `.claude-plugin/plugin.json`. None of the four categories in the sentence covers it.
- :152 is a substring false positive: "with the same namespace" matches `same name` (E10). The true same-name hits are :417 and :421, so the counter's 3 overstates by one.
- :31 ("refuses a conflicting toggle", managed policy) is an unrelated sense. That part holds.
- Q26 (`corpus/QUALITY.md:37`) requires every clause to be turned on by the counter's output or by a cited guard whose exit code changes when that clause is falsified. "Located in the seat report" and "about something else" are turned on by neither: the grep prints counts, and no guard checks locations.
- Fix: drop "located in the seat report", or state the hit list per page and bound the sentence to the printed counts.

**F3 (medium-low): universal "Every documented 'which one wins' rule found so far is keyed on the skill name" (census 225-226; lesson Gate line 32).**
- The S028 page documents other which-one-wins rules: managed value wins (:31); manifest-file location (:107, :402); MCP servers last-wins keyed on server name (:419, :421); and "skills override commands" with no key stated (diagram :456).
- The universal holds for skill and agent arbitration only.
- Fix: "every documented skill or agent arbitration rule found so far is keyed on the skill name".

**F4 (low): `teaches` cap clause, "the page's 1,024-character cap is on plugin-manifest descriptions, not on the SKILL.md `description`."**
- The cap at :195 sits under `### Legacy manifest fields` (heading :183). The cap at :349 is a marketplace plugin-entry field (:343). The Agent Plugins 1.0 manifest table (:111-130, `description` row) states no cap.
- "Not on the SKILL.md description" is a negative claim about a file the page never mentions. Seat Finding 5 (`SrcCopilotSkills.md`, line 133) agrees that no GitHub page states a SKILL.md cap.
- Fix: "the page states 1,024 characters for legacy plugin.json and marketplace plugin-entry descriptions (:195, :349); it says nothing about SKILL.md descriptions."

**F5 (low): `teaches` says "keyed on the **name**, not the description."**
- The name key holds (:415, :417; diagram :447 "dedup by name"). "Not the description" is inference: the page never discusses description-based resolution. Mark it [INFERENCE] or drop it.

**F6 (info): no tier rubric in the lane.**
- QUALITY.md:6-7 and the lane README say tier definitions live in `corpus/SOURCES.md`. The judged SOURCES.md has none (E9 grep). The fleet `SOURCES-CONTRACT-v1.md` was not found by a glob of the fleet root and lane root. I did not search deeper.
- Tier A was judged against the rows' practice only.

**F7 (info): drift in the working copy, not in S028.**
- The working-copy `corpus/lessons/round-50.md` (135 lines) has one row added after rev 956ee167 (134 lines). The row is `M32 Misroot sweep run before the last seat returned`, inserted at working line 18.
- The S028 Gate row is identical in both: judged line 61, working line 62. The judged file is the one checked.

## Evidence (commands and exit codes)

- **E1** First fetch, `curl -sS -L -D headers.md.txt -o cli-plugin-reference.md -w …`, 2026-10-22T13:32:19Z. Printed `http=200 bytes=47200 type=text/markdown; charset=utf-8` and `curl_exit=0`. Headers: `age: 43`, no Last-Modified, no ETag.
- **E2** Cache-busted refetch (`?r50falsify=20261022133658`), 2026-10-22T13:36:59Z. CLI: `http=200 bytes=47200`. SDK: `http=200 bytes=35455`. Headers: `x-cache: MISS, MISS`, `age: 0`. The curl exit code was not echoed for this batch; HTTP 200 and full length were observed.
- **E3** `sha256sum` (exit 0). CLI first fetch, CLI cache-busted copy and seat copy all give `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0`. `cmp` on both pairs printed "identical" (exit 0). Seat copy mtime is 09:31:52 -0300, which is 12:31:52Z and matches the row's 12:31:51Z.
- **E4** SDK: cache-busted copy and seat copy both give `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3` (exit 0). An earlier SDK fetch was a CDN copy with `age: 3814`; it was superseded by E2.
- **E5** Sweep, `grep -ciE` on the CLI page (grep exit 1 means no match, not failure):
  overlap 0 (exit 1); ambigu 0 (1); precedence 8 (0); tie[- ]?break 0 (1); conflict 1 (0); multiple skills 0 (1); same name 3 (0); prioriti 0 (1); 1024 2 (0); truncat 0 (1); `grep -cE '1,024'` 0 (1); description 23 (0).
  Seat table `SrcCopilotSkills.md` lines 60-73, CLI column: identical on all ten.
- **E6** Lines read verbatim on the CLI page. :415 "* **Agents and skills** use first-found-wins precedence." :417 "Skills are deduplicated by their name field inside the `SKILL.md` file." and "The plugin cannot override project-level or personal configurations." :195 "Max 1024 chars." :349 "Plugin description. Max 1024 chars." :31, :107, :152, :402, :419, :421, :425, :447, :456 as cited above.
- **E7** `sed -n '685p'` on the SDK copy (cache-busted and seat copies): the same verbatim line.
- **E8** `git clone -q` of the lane to scratch: exit 0. `git -C … checkout -q 956ee1676…`: exit 0. `rev-parse HEAD` = 956ee1676e4c18480bce8ac3993541462be76e11.
- **E9** sha256 prefixes at judged rev vs working copy: SOURCES.md `4236b783072be3b7` both; census `40ea8f98b7da2f82` both; QUALITY.md `0ff14ac33b6114cb` both; round-50.md `0b90fe2cbb0d5e44` vs `2cb6a17dc46e2f58` (differs). `diff -u` exit 1, one hunk, one added line (F7). `grep -c '^| S0'` on judged SOURCES.md = 29 (exit 0).
- **E10** `grep -ciE 'same name'` on page line 152 alone: 1 (exit 0). The match is "same namespace".
- **E11** S028 row at judged rev: line 41, 11 pipe-separated fields, teaches in field 7, status `mined`, opened 2026-10-22, recheck 90d.
- **E12** `_grep` for seat-report citations of CLI lines :31, :107, :152, :402, :425: no citation matches. The hits it printed were timestamps such as `12:31:51Z`.

No jj command was executed. One jj command in an aborted batch never ran, because the shell stopped at the nonzero `diff` exit. Nothing was written in the lane except this file. Tooling: none installed or upgraded. curl, git, sha256sum, grep, awk, diff, cmp and stat were already present. Scratch: `/fast/scratch/hyaku/kotoba-r50/falsify/ReopenS028/`.

## Residual risk and gaps

- The page carries no date and no Last-Modified or ETag header. Freshness therefore means unchanged bytes between 12:31:51Z and 13:36:59Z (origin MISS, age 0). It is not a revision date. The 90-day recheck is the only refresh guard.
- I did not check the HTML route; the row names the `.md` route.
- I checked the SDK page at line level for :685 and :805-810 only.
- I did not verify S024-S029 other than S028, S019, S022, the D1-D6 repairs, or C1/C2.
- Tier A rests on the lane's practice (F6).
