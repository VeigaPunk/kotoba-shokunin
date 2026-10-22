Result: DONE — the lane already holds a documented description number for five of the seven C1 clients (two of those only inside SOURCES `teaches` cells, one of them a soft budget rather than a cap), held only an adjacent plugin-manifest number for Copilot CLI, and held nothing at all for Cursor before this round; no admitted statement is falsified by the new table, but several specific cell wordings would contradict admitted knowledge, and plan erratum 3's guard (a) forbids reusing the four old rows.

Seat: `KotobaR54.ScoutPriorHolds` (scout, build wave). Lane corpus read-only; the only file written is this
report. No source page was fetched by this seat: every "quote" below is quoted from a lane file and its
location is a lane path, not a URL. Nothing here is a fetch record.

## Measured at

- Lane tip `bf65974c7845a06d7ef621ad998c6378ff735cd5` (C2 registry landed), read 2026-10-22T21:32Z.
- `SKILL.md` 585 lines, sha256 `8c3584a9842140deee86663a94572c9b7eddf5d1ff67a55d1dde0b0c4ce572eb`.
- `corpus/SOURCES.md` 52 rows, sha256 `ce96ed5ffa8569b580a749514c8ea1b5794e09803b7ab6d5d66c4fcd85db0ec8`.
- At `bf65974`, `corpus/lessons/round-54.md` and `corpus/knowledge/skill-listing-thresholds-round54.md` were
  absent from the tree (`git ls-tree HEAD` lists neither). The working tree moved again after this walk; this
  report describes `bf65974` and the wave files it reads, not the later landing.
- The file moved during this walk: `SKILL.md` was 552 lines at `7ad05d34` when the walk started. Line numbers
  below are at `bf65974`; every `SKILL.md` line I cite is below 433 (the C2 insertion point) and therefore also
  correct at `7ad05d34`, with two exceptions: `:573` (the truncation-era note, `:540` at `7ad05d34`) and the
  585-line count itself.
- Counter read at `bf65974`: `verifiers/check_description_thresholds.py` (rules `:81-108`, matchers `:135`,
  `:181`, `:197`, `:218`, `judge` `:239`). Its docstring pins the seven clients, the hosts, the anchors and the
  target; it does not pin whether a number is an authoring maximum, a listing cut or a budget (docstring, Q31).

## A. Every description-length fact the lane already holds

Kind readings are mine from the cited text. "admitted" = a `corpus/knowledge/` file that has a row in
`corpus/README.md` § Coverage map. "wave evidence" = a `.ufo/waves/**` seat report, which is not admitted
knowledge and not a SOURCES row.

### A1. The seven C1 clients

| # | fact (file:line) | client | number(s) | kind | SOURCES row | where it lives | verbatim page quote held? |
|---|---|---|---|---|---|---|---|
| 1 | `SKILL.md:106` ("Full `description` byte-for-byte … no truncation"); `harness-router-models-round9.md:111-117`; `opencode-offer-trace-round8.md:180-182`; `fail-closed-and-anti-patterns.md:83` | opencode | none — "untruncated" | measured render (from `skill/index.ts:332-333`) | none (S016 covers discovery only) | admitted + SKILL.md prose | code lines quoted, not a docs sentence |
| 2 | `SKILL.md:164-165` | opencode | none | same render, one-sentence form | none | SKILL.md prose | — |
| 3 | S024 `teaches` (`skills.md:72`); `sibling-overlap-census-round49.md:202`; `skill-selection-rules-round50.md:46-47`; `lessons/round-48-verifier-spotcheck.md:133` ("It documents the name regex, 1–64, 1–1024 and directory-match rules") | opencode | 1-1024 | authoring maximum | **S024** (docs, A, mined, opened 2026-10-22, host `opencode.ai`) | admitted clause (round-50 finding 5) + SOURCES | only in wave evidence: `.ufo/waves/round-48/build/C2CodexOpencodeDocs.md:76`, `.ufo/waves/round-50/build/SrcOpencodeDocs.md:27` — "`description` must be 1-1024 characters." (5 words) |
| 4 | S025 `teaches` (`agent-skills.md:148`); `skill-selection-rules-round50.md:46-47`; `sibling-overlap-census-round49.md:334` | VS Code | 1024 | authoring maximum | **S025** (docs, A, mined, 2026-10-22, `code.visualstudio.com`) | admitted clause + SOURCES | only in wave evidence: `.ufo/waves/round-50/build/SrcVSCodeSkills.md:45` ("Maximum 1024 characters.") and `:103` ("Be specific about both capabilities and use cases to help Copilot decide when to load the skill. Maximum 1024 characters.", 20 words) |
| 5 | S022 `teaches` (`skills.md:389`, `:390`, `:1213`); `sibling-overlap-census-round49.md:221-222`; `skill-selection-rules-round50.md:46-48` | Claude Code | 1,536 | per-entry cut in the listing, over `description` + `when_to_use` | **S022** (docs, A, mined, 2026-10-22, `code.claude.com`) | admitted + SOURCES | yes, in a lesson Gate table: `lessons/round-50.md:70` — "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage" (19 words) |
| 6 | S022 `teaches` (`skills.md:1207-1213`); `sibling-overlap-census-round49.md:154-156` | Claude Code | 1% | listing budget (descriptions of least-used skills dropped first) | **S022** | admitted + SOURCES | no (paraphrase in both places) |
| 7 | S021 `teaches`; `lessons/round-48.md:36` (quote, `md:37-39`); `lessons/round-47.md:36` (S013's copy) | Codex | 2% of context; 8,000 characters when unknown; `skills.max_context_tokens` up to 10,000 tokens | listing budget over the whole initial list | **S021** (docs, A, mined, 2026-10-22, `learn.chatgpt.com`); S013 queued and superseded | **SOURCES only** — no admitted entry states it | yes, in a lesson Gate table: `lessons/round-48.md:36` — "By default, this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown." (22 words) |
| 8 | S028 `teaches` (`cli-plugin-reference.md:195`) | Copilot CLI | 1,024 | plugin-manifest description cap, **not** a SKILL.md `description` cap ("the page states no cap for the SKILL.md `description`") | **S028** (docs, A, mined, 2026-10-22, `docs.github.com`) | **SOURCES only** | no verbatim quote recorded |
| 9 | S029 `teaches` (`skills-best-practices.md:24`) | Gemini CLI | ~100 words of metadata; `1024` → 0 hits | soft per-skill metadata budget; no cap | **S029** (docs, A, mined, 2026-10-22, `geminicli.com`) | **SOURCES only** | no (paraphrase only) |
| 10 | `alwayson-rule-files-round53.md:69`; S049 (`rules.md:155`) | Cursor | 500 lines | **rule-file** length guidance, not a skill description | **S049** (docs, A, mined, 2026-10-22, `cursor.com`) | admitted + SOURCES, wrong topic | yes, in that entry ("Keep rules under 500 lines") |
| 11 | (nothing in the lane corpus) | Cursor | — | — | none | no Cursor skill-description statement in any SOURCES row, admitted entry or `SKILL.md` line; S049/S052 are rules pages, and the round-53 rejected list shows Cursor help, CLI and changelog pages were opened for other topics. A round-54 seat has since sourced one number from the release notes (§E) | — |
| 12 | S024 `teaches` (`skills.md:110`); `skill-selection-rules-round50.md:24` | opencode | none | the listing is rendered inside the `skill` **tool description**, which is where a tool-description budget would bite; none is documented | **S024** | admitted + SOURCES | yes (round-50 Gate, S024 row) |
| 13 | S027 `teaches` | GitHub Copilot (cloud agent, not the CLI) | none — "states no character cap" | negative | **S027** (docs, A, mined, 2026-10-22, `docs.github.com`) | **SOURCES only** | only for the positive half: the round-50 Gate S027 row quotes the field description, not the negative |

### A2. Adjacent numbers in the lane that are not per-client description thresholds

| # | fact (file:line) | object | number | why it matters here |
|---|---|---|---|---|
| 14 | `SKILL.md:105`, `:161`, `:171`, `:573`; `render-mechanism-round7.md:15-17`, `:77-78`; `frontmatter-trigger-surface.md:68`, `:116-120`; `fail-closed-and-anti-patterns.md:83`; `harness-router-models-round9.md:90`; `sibling-description-rewrites-round8.md:52` | omp render (not a C1 client) | 99 hard cut, threshold 100, effective keep 55–96 | a measured render cut, no docs row; must stay a separate statement |
| 15 | `render-mechanism-round7.md:21-24` | omp LLM compressor | `maxTokens 1024` | a "1024" in the omp context that is **not** a description cap |
| 16 | `frontmatter-trigger-surface.md:70`; `harness-router-models-round9.md:90` | omp truncation-era loss | 17.7% of chars, 53/62 spans, 13/13 `Triggers:` clauses | truncation-era; `SKILL.md:573` already marks it as such |
| 17 | `sibling-description-rewrites-round8.md:493` | round-7 doc's render size | "104" chars, **did not reproduce** (measured 94) | a recorded correction; do not revive 104 |
| 18 | `SKILL.md:177`, `:399`; `frontmatter-rule-authorities-round48.md:44`; S018, S017 | the open spec / its validator | 1-1024 (`MAX_DESCRIPTION_LENGTH = 1024`) | the portability floor. S018's host (`agentskills.io`) is in **no** client's `HOSTS` pin, so the spec can never back a C1 client |
| 19 | `frontmatter-rule-authorities-round48.md:44`; S019 | Anthropic best practices | "Maximum 1,024 characters" | `platform.claude.com` **is** in Claude Code's host pin, so S019 could back "Claude Code" — an authority/scopes error, since S022 (the Claude Code skills page) carries no 1,024 cap |
| 20 | S033; `mcp-server-instructions-round52.md:50` | Claude Code MCP server instructions | cut at 4,096 characters | different object; already a "4,096" in SKILL.md (guard-b grep: 1 hit) |
| 21 | S035; `mcp-server-instructions-round52.md:51` | Codex MCP server instructions | first 512 characters self-contained | different object |
| 22 | S043, S044 | always-on files | 4 MiB skip; 32 KiB combined | different object |
| 23 | `frontmatter-rule-authorities-round48.md:51`; `.ufo/waves/round-48/build/C2CodexOpencodeDocs.md:75` (`codex-rs/ext/skills/src/render.rs:23-24`, `MAX_CATALOG_SKILL_DESCRIPTION_CHARS: usize = 1_024`) | Codex, **code not docs** | 1,024 per catalog description | a measured per-entry cut in the shipped parser, admitted in prose but "not tabled because no source row pins that code". The docs' 2% list budget and this 1,024 are different objects; a Codex cell must not let either stand for the other |

## B. Coverage verdict for the seven

| client | prior hold | strength | uncovered ground |
|---|---|---|---|
| Claude Code | 1,536 listing cut + 1% budget (S022, admitted twice, verbatim quote already in a lesson Gate) | strongest of the seven | none; needs a round-54 row (guard a), an entry row and a SKILL table row |
| Codex | 2% / 8,000 / 10,000-token override (S021, verbatim quote in a lesson Gate) | strong for the docs; the lane also admits a code-level 1,024 per-description truncation (round-48:51) | the 2% / 8,000 numbers have **never been admitted** — SOURCES only; the entry is the first admitted statement of them |
| VS Code | 1024 authoring maximum (S025, admitted only as a clause of round-50 finding 5) | medium | no dedicated entry row, no verbatim quote outside wave evidence |
| opencode | 1-1024 authoring maximum (S024) + the measured "untruncated" render | medium (two different kinds share the client) | the authoring cap is admitted only as a clause; the render statement is admitted but is a measurement, not a client number |
| Copilot CLI | 1,024 **plugin-manifest** cap + a negative for SKILL.md (S028) | **weak/adjacent** | no skill-`description` number was held before this round; the lane's own record says the page states no cap for it |
| Gemini CLI | ~100 words soft metadata budget; no 1024 cap (S029) | **weak** — a soft budget, SOURCES only | the entry is the first admitted statement; any "cap" wording would be new and wrong |
| Cursor | nothing in the lane corpus about skill descriptions (only rule-file guidance, S049) | **none before this round** | everything — now filled in-flight by S058 (release notes: a `description` over 1,024 characters is a `/skills` warning); no Q30 negative is needed if that row is used |

Strictly uncovered before this round: **Cursor** (no prior hold of any kind). Weak (adjacent number only):
**Copilot CLI**. Held only in SOURCES: **Codex, Gemini CLI, Copilot CLI** (plus the cloud-agent negative in
S027). The target of 4 is reachable from rows whose pages the lane already cites (Claude Code, Codex, VS Code,
opencode); as of 21:33Z all seven clients have an in-flight round-54 source seat (§E).

## C. What the new entry would supersede, and must not contradict

Supersede: **nothing.** No admitted statement is falsified. `skill-selection-rules-round50.md:46-48`
(finding 5, "Length caps differ by client") is *extended*, not replaced: it states 1,024 for `description`
(S024, S025, S019) and 1,536 for `description` + `when_to_use` (S022), and both numbers must reappear unchanged.
Because nothing is superseded, no `check_correction_sweep.py` registry line is triggered by the entry itself
(Q29).

Must not contradict, cell by cell:

1. `SKILL.md:106` + `harness-router-models-round9.md:111-117`: opencode's *render* is uncut. Any opencode cell
   that reads "cut at 1,024" contradicts a measured, admitted statement. The honest cell: an authoring maximum,
   with the render stated as uncut.
2. `SKILL.md:164-165`: same fact in prose, in the same file as the table. Any opencode wording must be one that
   reads true next to "the full description reaches the model untruncated".
3. `SKILL.md:177` + `:399` + `frontmatter-rule-authorities-round48.md:44`: the portable authoring floor is 1,024
   and comes from the spec (S018), not from a client. A per-client table must not present 1,536 or 2% as the
   authoring rule.
4. `skill-selection-rules-round50.md:46-48`: 1,536 is `description` **plus** `when_to_use`; 1,024 is
   `description`. Swapping the subjects contradicts the entry and S022's teaches cell.
5. `frontmatter-rule-authorities-round48.md:44`: three authorities differ (spec "Must be 1-1024 characters";
   Anthropic "Maximum 1,024 characters"; Anthropic's packager enforces no maximum). A single "the docs say
   1,024" sentence flattens that and contradicts the entry's own table.
6. S027: the cloud-agent page states **no** cap. S028: the CLI page states **no** SKILL.md cap, and its 1,024 is
   a plugin-manifest field. Reusing S028's number as the CLI's description threshold contradicts S028's own
   teaches cell.
7. S029: Gemini's prose has **no** description length cap; ~100 words is a soft metadata budget. A cell reading
   "100 words" as a cap contradicts the row and widens the record (Q26).
8. S021: 2% is a budget over the whole initial skill list, "may omit skills", and descriptions are shortened
   first. A cell reading "8,000 characters" as a per-description cut mis-states the unit. Note the lane also
   admits a *code* measurement of 1,024 per catalog description for Codex
   (`frontmatter-rule-authorities-round48.md:51`); the docs number is a different object, and a cell reading
   "Codex: no per-description limit" would sit uneasily beside that admitted measurement — say "not documented",
   not "not there".
9. `sibling-description-rewrites-round8.md:493` and `SKILL.md:573`: do not revive the truncation-era figures or
   the "104" render size.
10. `SKILL.md:105` and `render-mechanism-round7.md`: omp's 99 is a measured render cut on a harness outside the
    counter's seven. It may sit beside the table; it may not be counted as a client's documented threshold.

## D. Contradiction and counter risks, most likely first

1. **Guard (a) forbids the cheap route.** Plan erratum 3 requires each backed client's `S###` to be *absent* at
   `e3371548`. Appending the entry path to S021/S022/S025/S024 (allowed for the counter, and by contract rule 2
   with a logged old→new) would pass the counter and fail the round's own guard. New rows are mandatory.
2. **S024 is half-superseded.** S039 "supersedes S024" but its teaches cell does not restate 1-1024. Citing
   S039 for the cap rests on a cell without the number; citing S024 cites a superseded row. A fresh row for the
   same page is the only clean move.
3. **Copilot CLI's number is the wrong kind.** The lane's held number (S028) is a manifest cap and its own cell
   says the skill description has none. A round-54 seat has since found "Max 1024 characters" on the command
   reference's skill frontmatter table (`.ufo/waves/round-54/build/SrcCopilotCLI.md:49`, S056 draft; I read it,
   I did not fetch it). Using either number without naming the object is the round's biggest over-wide-record
   risk. S028's negative is page-scoped ("the page states no cap"), so a cap on the command reference does not
   falsify it; a table that reads "Copilot CLI documents no cap" would.
4. **Cursor's number rests on release notes, not a skills page.** The lane held nothing before this round, so the
   in-flight S058 is the only support (`release-notes.md:122`: the `/skills` warning set names a description over
   1,024 characters). That is a legitimate Q30 leg, but the cell must not say "the docs say" and must not imply a
   truncation: the seat's own reading is that an over-length description still loads. Any *negative* written
   instead needs the three legs — changelog or release notes, current docs source tree, lane-corpus grep — or
   the client is `not checked`. The 500-line rule at `alwayson-rule-files-round53.md:69` is evidence for a
   different object and cannot stand in.
5. **Number spelling must match the page, not the house style.** `has_token` (`:218`) requires the SKILL cell's
   token to appear in the quote as a whole token: a cell of `1,024` fails against a page that writes `1024`
   (opencode, VS Code) and against `1-1024`. Write the cell as the page writes it.
6. **Client names are whole-cell equalities** (`clean`, `:135`). `GitHub Copilot CLI`, `OpenCode`,
   `Claude Code (skills)`, `Gemini CLI docs` all fail. The seven strings are fixed at `:84`.
7. **Quote identity is byte-level.** The entry quote must be exactly one double-quoted string in a Gate table
   row whose first cell is that `S###` (`gate_quotes_by_id`, `:197`); 3–25 words; no inner double quotes (the
   regex stops at the first `"`). Backticks must match on both sides. The Claude Code quote already used at
   `lessons/round-50.md:70` is 19 words and carries two backticked field names — safe, if copied exactly.
8. **One row per client per table.** A second Claude Code row (skills and subagents) or a second opencode row
   makes that client unbacked (`:250`, `:260`).
9. **The `1%` figure is optional in the SKILL cell but must not displace the counted number.** If the cell holds
   both `1,536` and `1%`, either token satisfies the quote test; if it holds only `1%`, the quote must then
   carry `1%`, which the recorded sentence does not.
10. **Line budget.** `SKILL.md` is 585 lines at `bf65974`; a 7-row table adds ~12 lines (heading, blank, header,
    separator, 7 rows, blank) → ~597 of 600. Any prose paragraph, a second blank line, or a wider table fails
    the executed `trigger.line_budget` box. The plan's 552-line figure is the pre-C2 state.
11. **Entry admission debt.** The new entry must open with `source:` naming an S### row plus anchor,
    `verified-at:` and a runnable `recheck:` (QUALITY Q12, `CORPUS.md:17`) and must gain a
    `corpus/README.md` § Coverage map row in the same commit, or `verify_corpus_integrity.py` reads
    `corpus.index.unindexed 1` (`:443-456`) — the failure rounds 49 and 50 recorded.
12. **Adjacent numbers drifting in.** 4,096 / 512 / 4 MiB / 32 KiB / 64 are other objects (MCP instructions,
    AGENTS.md, name caps). The table has four columns and no room to explain a wrong-kind number.

## E. In-flight state (read, not verified by me; snapshot 21:27–21:33Z)

Source drafts exist for all seven clients. The ids were still moving while this walk ran; one is malformed and
one is flagged by its own seat for renumbering. Read this as a snapshot, not the integration map:

| draft | client | id proposed | note |
|---|---|---|---|
| `SrcClaudeCode.md` | Claude Code | S053, plus `S053b` | quote "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing" (`:80`) |
| `SrcCodex.md` | Codex | S054, plus `S054b` | `S054b` is not a valid id (`S` + 3+ digits, contract § Shape), and the Claude Code draft's `S053b` is also flagged there for renumbering: the SOURCES row regex and the corpus census skip a `b`-suffixed row, so it would be invisible and its quote unverifiable |
| `SrcVSCode.md` | VS Code | S055 | quote "Maximum 1024 characters." (`agent-skills.md:148`) |
| `SrcCopilotCLI.md` | Copilot CLI | S056 | quote "What the skill does and when to use it. Max 1024 characters." (`cli-command-reference.md:1274`) |
| `SrcGeminiCLI.md` | Gemini CLI | S057 | quote "Metadata (name + description): Always in context (~100 words)." |
| `SrcCursor.md` | Cursor | S058 | release notes `:122`: the `/skills` warning set names "a description over 1,024 characters" (25 words when quoted whole) |
| `Srcopencode.md` | opencode | S059 | quote "`description` must be 1-1024 characters." (`skills.md:72`) |

Correction rows are also in flight: `ScribeS046Fix.md` (S060) and `ScribeS050Fix.md` (S061). The id map must be
reconciled before integration; a `b` suffix must be renumbered, not landed.

## F. What this walk says the planner should do

1. Back at least four clients with **new** rows (guard a): Claude Code, Codex, VS Code, opencode. Codex is the
   only one whose number has never been admitted; it is also guard (b)'s cheapest new ground (`2%`, `8,000`,
   `1,536`, `1%` all count 0 at `e3371548`; `1024`/`1,024` count 1, `~100 words` counts 0 — measured with
   `git show e3371548:SKILL.md | grep -c -F`).
2. Add Gemini CLI as a fifth if its quote is accepted: the number is new ground (`100 words` → 0) but the
   reading must be "soft metadata budget", not a cap.
3. Treat Copilot CLI and Cursor as optional. For Copilot CLI, name the object — the command reference's
   frontmatter cap, not the plugin manifest. For Cursor, cite the release-notes `/skills` warning and call it a
   warning, not a cut; no negative is needed, and a negative would require the full Q30 sweep.
4. Write the SKILL cells with the pages' own number spelling, the seven exact client strings, and the shortest
   honest kind label; put the kind qualifier in "Past the threshold" or "Action", not by widening the number.
5. Reserve ~12 lines and no prose in `SKILL.md`; add the entry's coverage-map row and Q12 header in the same
   commit as the entry.

## G. Remaining unknowns

- Whether any of the four wave-evidence quotes is still on its live page today: no fetch was made by this seat,
  and only the counter's `--fetch` tests that.
- Whether the Cursor `/skills` warning is also described on a Cursor docs page, not only in the release notes,
  and whether Cursor documents any cut past 1,024 — the in-flight S058 is the seat's claim, unverified by me.
- Whether Gemini CLI's ~100-word sentence is the only number on that page (`skills-best-practices.md`): the
  lane's record states a `1024` → 0 sweep but no full digit enumeration. [INFERENCE]
- Whether Claude Code's 1,536 cut and its 1% drop-first rule apply to the same listing (they are adjacent
  sections of one page, `:389` and `:1207-1213`); the lane states both, not their interaction.
