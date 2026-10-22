# ReopenS026: re-open of SOURCES row S026 (Claude Code subagents page)

**HOLDS-BOUNDED.** Applies to SOURCES row S026 (`corpus/SOURCES.md:39`), its Gate row (`corpus/lessons/round-50.md:59`) and the census round-50 bullet (`corpus/knowledge/sibling-overlap-census-round49.md:209-213`), at judged revision 956ee1676e4c18480bce8ac3993541462be76e11.

The bytes, sha256, quotes, line pins and all ten sweep counts hold. Four wording clauses overstate the page (F2-F5). The "no rule for two matching descriptions" clause is true of the page but is not evidenced by the sweep the row cites (F1). No fact in the row is false.

Scope: read-only. The lane was not edited. Private clone at `/fast/scratch/hyaku/kotoba-r50/falsify/ReopenS026/lane` (checked out 956ee16). Tooling: nothing installed or upgraded (curl 8.23.0, git, python3, grep, sha256sum were already present). No subagents spawned.

## Verdict per check

| # | Check | Verdict | Basis |
|---|---|---|---|
| 1 | Bytes and sha256 match the recorded fetch | HOLDS | Re-fetched 2026-10-22T13:32:29Z. `.md`: 110,784 B, sha256 `89aa73eb3f28…`. HTML: 1,334,165 B, sha256 `31baba2df4a0…`. Both match the row and the seat report. No drift in the hour since the recorded 12:28:30Z fetch. |
| 2 | Quotes verbatim at cited location, at most 25 words | HOLDS | Five distinct quoted spans, all verbatim: row `:1293` (11 words), row `:176` (9 words), census `:176` (10 words), census `:1293` (line-wrapped at census lines 212-213, no content change), Gate `:11` (21 words). |
| 3 | Tier and scope cells honest | Tier HOLDS; scope FAILS on one clause | Tier A is vendor documentation; the instrument only bars community at tier A. Scope cell says "the `description` field decides delegation"; the page at `:839` names three inputs (F2). |
| 4 | `teaches` cell says no more than the page | FAILS on the precedence clause (F3); "no rule" clause BOUNDED (F1) | "The only precedence it documents is over same-name subagents" is false read literally. The "no rule for two matching descriptions" clause is true of the page (manual read) but the cited sweep cannot show it. |
| 5 | Census round-50 bullet for S026 matches the page | HOLDS-BOUNDED | Bytes, quotes and line pins match. "Delegation follows the `description`" overstates (F4). "The only arbitration" needs "between subagents" (F5). "Remedy for overlap" is a paraphrase: the page never says "overlap" (F5). |
| 6 | Ten-pattern sweep counts reproduce | HOLDS (counts); BOUNDED (as evidence) | All ten reproduce the seat's counts exactly. Positive controls return 1 for each pattern. The counters fail the Q25 mutant test and have blind spots (F1, F6). |
| G | Gate line (`round-50.md:59` at 956ee16) | HOLDS | URL, accessed time 2026-10-22T12:28:30Z, quote and location match the row. |
| A | Adjacency: `used-by` and dependence | HOLDS | Census and lesson cite S026 (grep). SKILL.md does not cite S026 or the Claude Code subagents page (grep). |
| F | Freshness | HOLDS | See F10 for the HTML cache note. |

Q25 (a counter must be shown able to fail on a mutant) and Q26 (a statement may claim only what its counter measures) are the lane's criteria.

## Findings, by severity

**F1 — Medium (Q25/Q26). The sweep cannot carry the "no rule" clause.** The row says the page "states no rule for two descriptions that both match (sweeps: …)". Mutant test: I added one ordinary sentence to a scratch copy after line 11: "When two subagents' descriptions both match a request, Claude picks the one whose description fits best and runs it first." All ten sweep counts stayed the same (see evidence). My wider probes moved: `match` 19→20, `pick` 3→4, `best` 9→10, "fits best" 0→1. So the cited sweep prints the same zeros on a page that does state a tie-break. The substance holds on the page as fetched: of the lines containing "match", the only one about delegation is `:11`; `:839` names the inputs; no line picks between two matching subagents. The row should cite that reading, or bound the clause to "none in the ten words searched; none on a manual read of `:11` and `:839`".

**F2 — Medium (scope cell). "The `description` field decides delegation" contradicts the page.** `sub-agents.md:839` says delegation is "based on the task description in your request, the `description` field in subagent configurations, and current context." The row's own `teaches` cell says "one of three matching inputs". Fix: "the `description` field is one of three delegation inputs".

**F3 — Low-medium (teaches cell). "The only precedence it documents is over same-`name` subagents" is literally false.** The page states precedence elsewhere: `:316` ("cache lifetime precedence"), `:390` (a subagent's definition or a model Claude passes "still takes precedence over" `CLAUDE_CODE_SUBAGENT_MODEL`), `:417` (`CLAUDE_CODE_EFFORT_LEVEL` "takes precedence over both"). `:604` is only a link anchor to permission-rule precedence. Fix: "the only precedence it documents between subagents".

**F4 — Low-medium (census line 209). "Delegation follows the `description` (`sub-agents.md:839`)".** The cited line lists three inputs. Fix: "delegation follows the request's task description, the `description` field and current context".

**F5 — Low (census lines 210 and 212).** (a) "The only arbitration is between same-name subagents" holds only when read as "between subagents" (same point as F3). (b) "Its remedy for overlap is craft": the page never uses the word "overlap" (count 0). Its advice is the bullet "Write descriptions that single out one subagent" (`:1293`). Fix: say "its advice for two similar subagents".

**F6 — Low (Q26, counter blind spots).** The counts reproduce, but some zeros cannot speak to this page:
- `multiple skills` is zero by construction on a subagents page. `multiple subagents` gives 3 (`:156`, `:180`, `:1013`).
- `prioriti` cannot match the word "priority". The page uses "priority" at `:156` (same-name rule), `:158` (table header) and `:1326`; `priorit` gives 3, `prioriti` gives 0.
- `same name` misses `:168` ("defines the same `name`"). `same .?`?name` gives 5.
None of these flips the reproduce check. They do mean three of the zeros are not evidence about subagent descriptions.

**F7 — Low (summary wording, lesson lines 31-32 and census lines 225-226).** "Every documented 'which one wins' rule … is keyed on the skill name." The S026 rules are keyed on the subagent name (`:156`, `:176`, `:228`, `:890`). Fix: "name (skill or subagent)". The substance holds for S026: none compares descriptions.

**F8 — Low (locator). "§ Example subagents → § Best practices (`:1293`)".** There is no "Best practices" heading. It is a bold label `**Best practices:**` inside a TIP callout at `:1290`, under `## Example subagents` (`:1284`). Fix: cite `:1290-1293`.

**F9 — Low (adjacency). Census line 195 counts S026 among "nine pages" of skill descriptions.** S026 is a subagents page. It supports the analogy but is not a skills page. Fix: "eight skill pages and one subagents page".

**F10 — Info (freshness). The HTML body came from the CDN cache.** My HTML response had `cf-cache-status: HIT` and `age: 31455` (about 8 h 44 min old at request time). The row gives no time for the HTML route, so nothing false is stated, and the sha256 matches. The `.md` route was rendered fresh (`cf-cache-status: EXPIRED`; `last-modified` equals the request time), which confirms the seat's note that `last-modified` tracks the request.

**F11 — Info (working copy ahead of judged bytes).** The lane's working copy differs from 956ee16 by one added line in the lesson's Mistakes table (M32, working-copy line 18); I did not check whether that edit is committed. The S026 Gate row therefore sits at line 60 there and line 59 at 956ee16. The S026 text is the same in both. Census, SOURCES and QUALITY are byte-identical between the two. This report uses 956ee16.

## What holds (evidence)

- Row fields: 13 pipe fields (NF=13). Tier A, status `mined`, opened 2026-10-22, recheck `90d`. Instrument: `validate` exits 0 with `ok`. Only warnings are W04 for S018, S019, S021 (the same as the seat report).
- Locators checked against the `.md` file: `:11` (heading "Create custom subagents", H1 at `:5`); `:156` and `:176` (heading "Choose the subagent scope", `:154`); `:158-164` (location priority table); `:228`; `:299` ("When Claude should delegate to this subagent", heading "Frontmatter reference", `:287`); `:306`; `:839` (heading "Understand automatic delegation", `:837`); `:890`; `:1293`.
- HTML parity: the row says the HTML "serves the same prose". Seven of eight sentences match exactly after tag stripping. The eighth (the `:11` sentence) matches with a typographic apostrophe (U+2019) in the HTML.
- Used-by: `corpus/knowledge/sibling-overlap-census-round49.md` and `corpus/lessons/round-50.md` both cite S026. SKILL.md has no S026 or Claude Code subagent citation; its "subagent" hits concern opencode rosters.

## Evidence (commands and exit codes)

- `git clone -q <lane> <scratch>/lane && git -C <scratch>/lane checkout -q 956ee16… && git -C <scratch>/lane rev-parse HEAD` → `956ee1676e4c18480bce8ac3993541462be76e11`, exit 0.
- `curl -s -o fetch_md_1 -D headers_md_1.txt -w '%{http_code} %{size_download} %{num_redirects} %{content_type}' https://code.claude.com/docs/en/sub-agents.md` → `200 110784 0 text/markdown; charset=utf-8`, exit 0. HTML route (`…/sub-agents`) → `200 1334165 0 text/html; charset=utf-8`, exit 0.
- `sha256sum fetch_md_1 fetch_html_1` → `89aa73eb3f28e274650634620113a19585dd09b7f40be3dd16d584800cb60aed`, `31baba2df4a0e54ad2e0a8a4651f9bb84ae96adcfe9851993ef4b740985cdc7b`. `wc -l fetch_md_1` → 1480.
- `grep -ciE <pattern> fetch_md_1`, in pattern order: overlap 0 (rc 1); ambigu 1 (rc 0); precedence 6 (rc 0); tie[- ]?break 0 (rc 1); conflict 0 (rc 1); multiple skills 0 (rc 1); same name 4 (rc 0); prioriti 0 (rc 1); 1024 0 (rc 1); truncat 2 (rc 0). Seat counts identical.
- `grep -niE` locations: ambigu `:890`; precedence `:176`, `:228`, `:316`, `:390`, `:417`, `:604`; same name `:156`, `:176`, `:228`, `:890`; truncat `:709`, `:1454`.
- Positive controls (`grep -ciE` on a one-line input): each of the ten patterns → 1. `tie-break`, `tie break`, `tiebreak` → 1 each.
- Mutant (F1): ten counts before and after → all unchanged. `match` 19→20; `pick` 3→4; `best` 9→10; `fits best` 0→1.
- Blind spots (F6): `prioriti` on "priority" → 0; `priorit` on the page → 3; `multiple subagents` on the page → 3, `multiple skills` → 0 (rc 1); `same .?`?name` → 5, `same name` → 4.
- `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <clone>/corpus/SOURCES.md --today 2026-10-22` → W04 lines for S018, S019, S021; `ok`; exit 0. Same command on the working-copy SOURCES → exit 0.
- `diff <clone>/corpus/lessons/round-50.md <working copy>/corpus/lessons/round-50.md` → one added line at working-copy line 18; exit 1. `cmp`-equivalent byte comparison of SOURCES, census and QUALITY → identical.
- `git -C <clone> show -s --format=… 542f515 956ee16` → exit 0. Committer dates are later than the S026 fetch, so no timestamp conflict.

## Residual risk and gaps

- I did not re-run the seat's HTML-route ten-pattern counts (not cited in the row).
- The wider synonym probes are a targeted reading, not an exhaustive read of all 1,480 lines. I read the cited lines, the filtered hits for "match", "priority", "multiple" and "order", and the `:316`, `:390`, `:417`, `:604` precedence lines.
- The "no rule" finding covers this page only. The skills page and other Claude Code pages are out of scope.
- No web source other than the two routes was opened.
