# Round-50 seat report — SrcReopenS022 (C1 frontier source: re-open of SOURCES row S022)

**HOLDS-BOUNDED — the re-opened source opens by ordinary means and is byte-identical to the bytes row S022 already records (HTTP 200, 111,557 B, sha256 `cdfcb0df…`, fetched 2026-10-22T12:28:45Z and re-fetched 2026-10-22T13:04:07Z with the same digest), so the row's freshness stands; the page documents NO tie-break between two overlapping skills (the ten-pattern sweep is the negative evidence, Q14); and it adds one fact the row did not carry — the listing entry's combined `description` + `when_to_use` text is truncated at **1,536** characters, and the page carries **no 1,024-character description cap** (its three `1024` hits are byte-formatting code). It therefore hands D3 no vendor precedence rule to borrow, and it widens C1's description-length budget beyond the spec's 1,024 cap.**

Seat scope: re-open existing registry row **S022** (Claude Code — Extend Claude with skills); record the description/`when_to_use` length cap and truncation, how the skill listing works under the context budget, and any tie-break between two matching skills; sweep the fetched text; draft the changed SOURCES cells plus the round-lesson `## Gate` line. Lane base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`; **read-only on the lane** — only this report was written there. Fetch, clone and drafts in `/fast/scratch/hyaku/kotoba-r50/build/SrcReopenS022/`.

## Fetch record

| route | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| `…/skills.md` (`.md` variant, the quotable one) | 2026-10-22T12:28:45Z | 200 | 111,557 | `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456` |
| `…/skills.md` (re-fetch) | 2026-10-22T13:04:07Z | 200 | 111,557 | `cdfcb0df…` — `cmp` byte-identical to the 12:28:45Z bytes |
| `…/skills` (HTML) | 2026-10-22T12:28:51Z | 200 | 1,233,129 | `102195341251387cee65e8d8f47809878c3c118a12f53fff64bea966a6c42ee2` |

0 redirects on both routes (`curl -w '… redirects %{num_redirects} final %{url_effective}'`); the HTML route carries the same prose (grep `1,536 characters` → 3, `when_to_use` → 4, `skillListingMaxDescChars` → 2). The `.md` digest equals the one the round-48 seat recorded (`.ufo/waves/round-48/build/C2ClaudeDocs.md:104`) and the one row S022 records: **the page has not changed since round 48**, so the row's `90d` recheck still rests on the same bytes and there is no editorial drift to re-teach (freshness axis).

## Findings

**F1 — The length cap is 1,536 characters, and it is a listing cap, not a field cap.**
- § Frontmatter reference, `description` row, `skills.md:389` — "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage."
- `skills.md:390` (`when_to_use` row) — "Appended to `description` in the skill listing and counts toward the 1,536-character cap."
- § Troubleshooting → § Skill descriptions are cut short, `skills.md:1213` — "each entry's combined text is capped at 1,536 characters regardless of budget"; same line — "The cap is configurable with [`skillListingMaxDescChars`]".
- **No 1,024-character cap is stated anywhere on this page.** The `1024` sweep's 3 hits are byte-formatting code in an example (`skills.md:1085`, `:1086`, `:1134` — `if b < 1024: return f"{b} B"`). The spec's and Anthropic's 1,024 cap (S018, S019) governs the field; this page's 1,536 governs what reaches the model in the listing. Two different caps, and a description of 848–961 characters (the C1 draft's range) satisfies both.

**F2 — How the listing works under the context budget.**
- `skills.md:1207` — "The listing always contains every skill name"; same line — "The budget scales at 1% of the model's context window."; same line — "When the listing overflows, Claude Code drops descriptions starting with the skills you invoke least".
- `skills.md:1213` — "To raise the budget, set the [`skillListingBudgetFraction`] setting (for example, `0.02` = 2%) or the `SLASH_COMMAND_TOOL_CHAR_BUDGET` environment variable to a fixed character count."
- `skills.md:1213` — "To free budget for other skills, set low-priority entries to `\"name-only\"` in [`skillOverrides`] so they list without a description."
- `skills.md:928` (§ Find unused skills) — "Every skill in the [skill listing](#skill-descriptions-are-cut-short) adds to your context on every turn, whether or not Claude ever uses it."
- Consequence for craft: the listing is a **name-complete, description-budgeted** surface. Dropping descriptions is keyed to how often a skill is invoked, not to how specific it is — so a rarely used skill with an excellent description can be reduced to its name. That is a listing-priority fact, and it is **not** a tie-break between two matching skills.

**F3 — Plain answer on the tie-break (Q14): the page does NOT document a tie-break between two overlapping skills.** Sweep over the fetched 111,557 B markdown (`grep -ciE <pattern> skills.md`, 2026-10-22; counts and per-pattern exit codes verbatim):

| pattern | count | exit | pattern | count | exit |
|---|---|---|---|---|---|
| `overlap` | 0 | 1 | `same name` | 2 | 0 |
| `ambigu` | 0 | 1 | `prioriti` | 0 | 1 |
| `precedence` | 1 | 0 | `1024` | 3 | 0 |
| `tie[- ]?break` | 0 | 1 | `truncat` | 2 | 0 |
| `conflict` | 1 | 0 | combined (all ten) | 9 | 0 |
| `multiple skills` | 0 | 1 | widened `1024\|1,536` | 6 | 0 |

Every non-zero count is located and none is about skill selection:
- `precedence` → `skills.md:920`: a `skillOverrides` **alias** rule ("that entry takes precedence" — a settings entry over an alias), not two skills competing.
- `conflict` → `skills.md:49`: `/doctor prompt-audit` checking "for outdated or conflicting instructions".
- `same name` → `skills.md:200` (the table heading "| Same name in | Which one runs |") and `:278` ("Claude Code ignores case, spacing, and invisible characters" when comparing names; `:280` — "A name that differs only by a look-alike letter from another alphabet counts as a different name").
- `1024` → `:1085`, `:1086`, `:1134`: byte-formatting code in an example, not a description cap.
- `truncat` → `:389` (the 1,536 listing cap) and `:747` (Bash tool output ceiling).

The HTML route gives `overlap` 2 (both site CSS/JS: `:1505` "the panels overlap again", `:2298` minified script), `precedence` 3, `conflict` 2, `same name` 3, `1024` 7 (CSS breakpoints + the same code), `truncat` 5, `ambigu`/`tie[- ]?break`/`multiple skills`/`prioriti` 0 — the same picture. Extended negative sweep on the markdown: `arbitrat` 0, `disambiguat` 0, `if two` 0, `both match` 0, `both apply` 0, `more than one` 0, `both skills` 1 (`:682`, about *stacked* skills), `one skill` 2 (`:321`, `:397`), `select` 1 (`:397`, a `model` field), `which skill` 3, `choose` 2, `picks` 3 — none is a rule for choosing between two matching skills.

**F4 — The only "which one wins" rules the page states, and why neither is a tie-break.**
1. **Name collisions** — § Resolve skills that share a name, `skills.md:198` — "When two skills share a directory or file name, where each one came from decides which one `/name` runs."; the table `skills.md:200-208` gives the order: `:202` — "Enterprise over personal, and personal over project." This is arbitration over an **identity** clash, not over two descriptions that both match.
2. **Stacking** — § Stack several skills in one message, `skills.md:682` — "Claude Code loads only the first skill, with the rest of the line as its arguments." That is a user-typed order, not a model-chosen one.

So D3's precedence ruling (between the `contested` arm and a stated split) has **no vendor authority on this page**; it must be stated as kotoba's own rule, as the S019 and VS Code seats concluded for their pages.

**F5 — What the page does give an author, for over-triggering.** § Skill triggers too often, `skills.md:1194` — "Make the description more specific"; `:1195` — "Add `disable-model-invocation: true` if you only want manual invocation". And § Control who invokes a skill, `skills.md:577` — the `disable-model-invocation: true` row reads "Description not in context, full skill loads when invoked". That is the vendor-side warrant for C1's edit: with no tie-break, the description text is the only arbitration surface, and specificity is the documented remedy for a skill that fires where it should not.

**F6 — Rule-attribution check (Q23): the 1,024 cap is nowhere attributed to Claude Code, and one line elsewhere is now stale.** Checked read-only in the lane on 2026-10-22: `grep -rn '1024\|1,024'` over `corpus/knowledge/sibling-overlap-census-round49.md` → 0 hits (the census never attributes a cap to Claude Code); over `corpus/knowledge/frontmatter-rule-authorities-round48.md` → the "description length" row (`:44`) attributes 1-1024 to spec (S018), skills-ref (S017) and Anthropic docs (S019) only, and that table has no Claude Code column; `SKILL.md:157` (portability floor) cites S018, S002, S019, S008, S012 — not S022 or S023 — for `description` ≤1024. The landed S022 row states the cap's **absence** explicitly ("the page carries no 1,024-character description cap"), which is what prevents the round-48 M24-class misattribution from recurring. **Stale line, for its owner (not mine to edit):** `frontmatter-rule-authorities-round48.md:132-135` says Claude Code's skills page and the Anthropic Skills API guide state further rules "recorded in `C2ClaudeDocs.md` and not yet opened into source rows" — that is now false, since S022 (skills page) and S026 (sub-agents page) exist as rows and S022 was re-opened today byte-identical. The entry is append-only, so the fix is an appended correction, not a rewrite of `:132-135`.

## Deliverable 1 — `corpus/SOURCES.md`, row S022: old → new for every changed cell

Unchanged cells: `id` (S022), `source`, `kind` (docs), `tier` (A), `status` (mined), `opened` (2026-10-22), `recheck` (90d).

| cell | old | new |
|---|---|---|
| scope | How Claude Code decides which of several available skills to use (the `description`'s role) and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode) | How Claude Code decides which of several available skills to use (the `description`'s role), how its skill listing is truncated and budgeted, and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode) |
| anchor | § Frontmatter reference, `description` row (`skills.md:389`); § Create your first skill (`skills.md:114`); § Resolve skills that share a name (`skills.md:196-198`); § Troubleshooting → § Skill triggers too often (`skills.md:1190-1195`); fetched as https://code.claude.com/docs/en/skills.md (200, 111557 B, sha256 `cdfcb0df…`) on 2026-10-22T09:41:02Z, byte-identical to the round-48 fetch of the same route; the HTML route (200, 1233129 B, sha256 `10219534…`) serves the same prose and did not redirect | § Frontmatter reference, `description` row (`skills.md:389`) and `when_to_use` row (`:390`); § Create your first skill (`skills.md:114`); § Resolve skills that share a name (`skills.md:196-208`); § Stack several skills in one message (`skills.md:682`); § Troubleshooting → § Skill triggers too often (`skills.md:1190-1195`) and § Skill descriptions are cut short (`skills.md:1205-1213`); fetched as https://code.claude.com/docs/en/skills.md (200, 111557 B, sha256 `cdfcb0df…`) on 2026-10-22T09:41:02Z and re-opened 2026-10-22T12:28:45Z byte-identical to those bytes and to the round-48 fetch of the same route; the HTML route (200, 1233129 B, sha256 `10219534…`) serves the same prose, did not redirect, and re-fetched byte-identical |
| teaches | The `description` is the field Claude uses to decide whether a skill applies (with `when_to_use` appended in the listing; names are always listed, and under a 1% context budget the least-used skills' descriptions are dropped first, `skills.md:1207-1213` — listing priority, not a tie-break) — and the page states no arbitration rule for overlapping descriptions (sweeps: `arbitrat`, `tie-?break`, `ambigu`, `overlap` → 0 each); a name clash is settled by origin (enterprise over personal over project), and a skill that fires where it should not is fixed by making the description more specific or by setting `disable-model-invocation: true` | …the same text, plus: re-opened 2026-10-22T12:28:45Z, byte-identical, adding that a listing entry's combined `description` + `when_to_use` text is truncated at 1,536 characters regardless of budget (configurable via `skillListingMaxDescChars`, `skills.md:389`, `:390`, `:1213`) — the page carries no 1,024-character description cap (the `1024` sweep's 3 hits are byte-formatting code, `skills.md:1085-1086`, `:1134`) — and that the ten-pattern sweep over the 111,557 B fetch gives `overlap` 0, `ambigu` 0, `precedence` 1, `tie[- ]?break` 0, `conflict` 1, `multiple skills` 0, `same name` 2, `prioriti` 0, `1024` 3, `truncat` 2, every hit located and none about skill selection: `precedence` (`skills.md:920`) is a `skillOverrides` alias rule, `conflict` (`:49`) is `/doctor prompt-audit`, `same name` (`:200`, `:278`) is the name-comparison rule (case, spacing, invisible characters and dash variants ignored; a look-alike letter from another alphabet is a different name, `:280`), `truncat` (`:389`, `:747`) is the listing cap and Bash output; the page's only "which one wins" rules are for name collisions (settled by origin) and for explicitly stacked skills (`claude -p` loads only the first, `skills.md:682`), neither of which arbitrates two matching descriptions |
| used-by | corpus/knowledge/sibling-overlap-census-round49.md | corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md |

The landing form of the row (13 pipe-separated fields, NF=13, verified) is `…/SrcReopenS022/draft_row_S022.md`, with its unified diff against `f3046466` at `…/SrcReopenS022/draft_S022_row.diff` (1 insertion, 1 deletion, `corpus/SOURCES.md`).

## Deliverable 2 — round-lesson `## Gate` line for `corpus/lessons/round-50.md`

```markdown
**Existing row re-opened:** S022 (Claude Code — Extend Claude with skills), `https://code.claude.com/docs/en/skills.md`,
fetched 2026-10-22T12:28:45Z and again at 13:04:07Z: 200, 111,557 B, sha256 `cdfcb0df…`, byte-identical to the
bytes the row records and to the round-48 fetch of the same route. Quote: "the combined `description` and
`when_to_use` text is truncated at 1,536 characters in the skill listing to reduce context usage"
(§ Frontmatter reference, `skills.md:389`). Status `mined` → `mined`; recheck `90d` → `90d`; `used-by`
`corpus/knowledge/sibling-overlap-census-round49.md` → `corpus/knowledge/sibling-overlap-census-round49.md,
corpus/lessons/round-50.md` (seat `.ufo/waves/round-50/build/SrcReopenS022.md`).

**Tie-break (Q14):** this page documents no tie-break between two overlapping skills. Sweep over the fetched
111,557 B markdown, 2026-10-22 (`grep -ciE <pattern> skills.md`): `overlap` 0 (exit 1), `ambigu` 0 (exit 1),
`precedence` 1 (exit 0), `tie[- ]?break` 0 (exit 1), `conflict` 1 (exit 0), `multiple skills` 0 (exit 1),
`same name` 2 (exit 0), `prioriti` 0 (exit 1), `1024` 3 (exit 0), `truncat` 2 (exit 0); the ten combined give
9 (exit 0). The five hits are a `skillOverrides` alias precedence (`skills.md:920`), `/doctor prompt-audit`
"conflicting instructions" (`:49`), the same-name table and the name-comparison rule (`:200`, `:278`), and
byte-formatting code (`:1085-1086`, `:1134`) plus the listing cap and Bash output (`:389`, `:747`) — none is
about choosing between two matching descriptions. The page's only "which one wins" rules settle an identity
clash (name collision, by origin, `skills.md:198`, `:202`) and a user-typed stack (`:682`); neither arbitrates
two matching descriptions. The page also states no 1,024-character description cap — its three `1024` hits are
byte-formatting code — and gives a 1,536-character listing cap for the combined `description` + `when_to_use`
(`:389`, `:390`, `:1213`).
```

## Deliverable 3 — citation line for the census entry's appended section (draft, for the census owner)

```markdown
- Claude Code's own skills page states no tie-break either: "What the skill does and when to use it. Claude
  uses this to decide when to apply the skill." (S022, `skills.md:389`), and the page carries no rule for two matching descriptions
  (sweep over the 111,557 B fetch: `overlap` 0, `ambigu` 0, `precedence` 1, `tie[- ]?break` 0, `conflict` 1,
  `multiple skills` 0, `same name` 2, `prioriti` 0, `1024` 3, `truncat` 2; the five hits are a settings-alias
  rule, a prompt-audit check, the name-comparison rule and byte-formatting code — seat
  `.ufo/waves/round-50/build/SrcReopenS022.md`). Its one listing cap is 1,536 characters for the combined
  `description` + `when_to_use` (`skills.md:389`, `:390`, `:1213`), and it states no 1,024-character
  description cap.
```

## Evidence (commands, exit codes, paths)

- Fetch: `curl -sS -L -o skills.md -w 'HTTP %{http_code} bytes %{size_download} url %{url_effective}\n' https://code.claude.com/docs/en/skills.md` → HTTP 200, 111,557 B, exit 0; `sha256sum skills.md` → `cdfcb0df…`; `date -u +%Y-%m-%dT%H:%M:%SZ` → 2026-10-22T12:28:45Z. Re-fetch 2026-10-22T13:04:07Z: 200, 111,557 B, `redirects 0`, same sha256, `cmp` byte-identical (exit 0). HTML route → HTTP 200, 1,233,129 B, `redirects 0`, sha256 `10219534…`.
- Sweep: `for p in 'overlap' 'ambigu' 'precedence' 'tie[- ]?break' 'conflict' 'multiple skills' 'same name' 'prioriti' '1024' 'truncat'; do c=$(grep -ciE "$p" skills.md); rc=$?; …; done` → counts and per-pattern exit codes in the F3 table; combined ten → 9 (exit 0); `grep -ciE '1024|1,536'` → 6 (exit 0). Located hits: `grep -niE 'overlap|ambigu|precedence|tie[- ]?break|conflict|multiple skills|same name|prioriti|1024|truncat' skills.md` → lines 49, 200, 278, 389, 747, 920, 1085, 1086, 1134.
- Quoted lines read with `grep -n '' skills.md | sed -n '<n>p'`: 49, 198, 200, 202, 278, 280, 389, 390, 682, 920, 928, 1085, 1086, 1134, 1194, 1195, 1207, 1213.
- Row shape: `awk -F'|' '/^\| S022 /{print NF}'` → 13 (exit 0), as for every other row.
- Registry validation with the fleet instrument on a private clone at `f3046466` (`…/SrcReopenS022/lane`): `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file lane/corpus/SOURCES.md` → exit 1 with `E11 S022 missing used-by corpus/lessons/round-50.md` plus the three pre-existing W04 (S018, S019, S021); after `touch lane/corpus/lessons/round-50.md` → exit 0, `ok`, the same three W04, no new warning; the unmodified lane file → exit 0, `ok`, the same three W04. **Landing constraint (not mine to land): `corpus/lessons/round-50.md` must exist when the row lands.**
- C1 counter on the lane base (read-only `git show f3046466:SKILL.md | awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' | grep -oiwE 'chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi' | sort -u | wc -l`) → 5 (exit 0), matching the plan's before-value.
- Description length: `yaml.safe_load` of the lane `SKILL.md` frontmatter → 815 characters (120 words) at the base; an illustrative edit that adds the four missing lane names and turns "five" into "nine" → 848 characters, i.e. 176 under the spec's 1,024 cap and 688 under this page's 1,536 listing cap. The lane's frontmatter has `name` and `description` only, so no `when_to_use` text counts against the listing cap. The exact C1 edit is another seat's; this is a length bound, not a draft.
- Census lanes classed non-`none` at `f3046466` (`grep -nE '^\| (chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi) ' corpus/knowledge/sibling-overlap-census-round49.md`): all nine present, each classed `adjacent` — the 9-lane list the C1 counter targets.
- Rule attribution (F6, read-only on the lane, 2026-10-22): `grep -c '1024\|1,024' corpus/knowledge/sibling-overlap-census-round49.md` → 0 (exit 1); `grep -rn '1024\|1,024' corpus/knowledge/frontmatter-rule-authorities-round48.md SKILL.md | grep -i 'claude code\|S022\|S023'` → no output; `sed -n '157p' SKILL.md | grep -o 'S0[0-9][0-9]'` → `S018 S002 S019 S008 S012`; `sed -n '38p' corpus/knowledge/frontmatter-rule-authorities-round48.md | tr '|' '\n'` → the six table columns are spec (S018), skills-ref (S017), Anthropic docs (S019), Anthropic packager (S012), Codex docs (S021), lane checker (S020) — no Claude Code column.
- Landing (read-only on the lane): `sed -n '35p' corpus/SOURCES.md | diff - <(sed -n '1p' …/draft_row_S022.md)` → exit 0 (identical); `git diff --stat corpus/SOURCES.md` → 8 insertions, 2 deletions (S022 plus S024–S029, another seat's landing); `bash scripts/sources-census.sh validate --file corpus/SOURCES.md` → exit 1 with eight E11 rows (S019, S022, S024–S029, all "missing used-by corpus/lessons/round-50.md") and the three pre-existing W04.

## Landing state (observed 2026-10-22T13:1xZ, read-only)

The L1 has already landed my S022 row together with S024–S029: `sed -n '35p' corpus/SOURCES.md` is **identical** to `…/SrcReopenS022/draft_row_S022.md` (`diff` exit 0) and `awk -F'|' '/^\| S022 /{print NF}'` → 13. `bash scripts/sources-census.sh validate --file corpus/SOURCES.md` currently exits **1** with E11 for eight rows (S019, S022, S024–S029): "missing used-by corpus/lessons/round-50.md" — `corpus/lessons/round-50.md` does not exist yet, and the three pre-existing W04 (S018, S019, S021) are unchanged. That is one landing constraint for the whole batch, not an S022-specific defect: the round-50 lesson file must exist for the batch to validate.

## Out of scope

- Editing `corpus/SOURCES.md`, `corpus/lessons/round-50.md` or the census entry: drafts only (lane bound; the L1 integrates). Nothing outside this report was written in the lane.
- The C1 description edit itself, and the wording of the D3 precedence ruling (other seats).
- **C1's "at least one new `corpus/SOURCES.md` row opened this round" is not satisfied by this seat.** S022 is an existing row (opened 2026-10-22 by the round-49 build wave, per `corpus/lessons/round-49.md` § Gate), so this re-open is freshness and adjacency evidence for a row that already exists, not a new row. The new-row requirement is carried by the S024+ seats (opencode docs, VS Code, Claude subagents, Copilot, Gemini CLI). If the L1 needs C1's source clause met by a row *created* this round, it must land one of those rows alongside the census appended section.
- Measuring how omp or opencode actually arbitrate between two loaded skills: this is vendor documentation, and the census's own limit (`corpus/knowledge/sibling-overlap-census-round49.md:38-41`) says the shokunin lane files are not in an omp discovery root, so no router effect exists here to measure.

## Artifacts

- `…/SrcReopenS022/skills.md` — the swept text (111,557 B, 1,234 lines, sha256 `cdfcb0df…`); `skills.html` — the HTML route (1,233,129 B, sha256 `10219534…`); `skills2.md` — the 13:04:07Z re-fetch.
- `…/SrcReopenS022/draft_row_S022.md` — the landing row; `…/SrcReopenS022/draft_S022_row.diff` — its unified diff against `f3046466` (1 insertion, 1 deletion, `corpus/SOURCES.md`).
- `…/SrcReopenS022/lane/` — private clone of the lane at `f3046466` carrying the draft row (mirror only; the lane checkout was not modified).

## Tooling

None installed or upgraded: `curl`, `grep`, `sed`, `awk`, `sha256sum`, `cmp`, `date`, `git`, `python3` (interpreter only) and the fleet's `scripts/sources-census.sh` were already present. No `pacman`, `uv tool`, `cargo` or `npm -g` transaction was run, and no host service was restarted.
