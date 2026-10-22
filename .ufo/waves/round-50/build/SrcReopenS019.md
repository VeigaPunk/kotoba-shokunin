# Round-50 seat report — SrcReopenS019 (C1 frontier source: re-open of SOURCES row S019)

**HOLDS-BOUNDED — the re-opened source opens by ordinary means (HTTP 200, 42,169 B, sha256
`f0a5d61b…`, byte-identical to the bytes row S019 already records), it states the description rules
C1's edit must respect (1,024-character cap, third person, what plus when), and it documents NO
tie-break between two overlapping skills — the ten-pattern sweep is the negative evidence (Q14). It
therefore supports C1's edit as the only arbitration surface, and hands D3 no vendor precedence rule
to borrow.**

Seat scope: re-open existing registry row **S019** (Claude Docs — Agent Skills best practices);
record the description rules and any guidance for separating a skill from similar skills; sweep the
fetched text; draft the changed SOURCES cells plus the round-lesson `## Gate` line. Lane base
`f30464660c675d1c1e2851a3bf0366a3aaffe5a8`; **read-only on the lane** — only this report was
written there. Fetch and mirrors in `/fast/scratch/hyaku/kotoba-r50/build/src-reopen-s019/`.

## Fetch record

| route | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| `…/agents-and-tools/agent-skills/best-practices.md` | 2026-10-22T12:28:47Z | 200 | 42,169 | `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960` |
| `…/agents-and-tools/agent-skills/best-practices` (HTML) | 2026-10-22T12:28:48Z | 200 | 1,212,371 | `028c47fe17f43bfa855927849559f4a75d768d73a703bc74bbebfc3791d04b6c` |

The `.md` variant is the quotable route (1,191 lines); its sha256 equals the `f0a5d61b…` row S019
records, so **the page has not changed since the round-49 fetch** (freshness: the row's `90d` recheck
still rests on the same bytes; no editorial drift to re-teach).

## Findings

**F1 — Description rules (located, verbatim, ≤25 words each).**
- § Skill structure, `best-practices.md:161` — "Maximum 1,024 characters"; `:160` — "Must be non-empty"; `:162` — "Cannot contain XML tags"; `:163` — "Should describe what the Skill does and when to use it".
- § Writing effective descriptions, `best-practices.md:203` — "The `description` field makes Skill discovery possible and should include both what the Skill does and when to use it."
- `:206` (Warning block) — "Always write in third person. The description is injected into the system prompt, and inconsistent point-of-view can cause discovery problems."
- `:213` — "Be specific and include key terms. Include both what the Skill does and specific triggers/contexts for when to use it."
- § Technical notes → § YAML frontmatter requirements, `:1134` — "`description`: Maximum 1,024 characters, non-empty, no XML tags".

**F2 — Guidance for separating a skill from similar skills: none of the tie-break kind, but the page
does state the selection test the description must satisfy.**
- `:215` — "Your description must provide enough detail for Claude to determine when to select this Skill"; same line — "Claude uses it to choose the right Skill from potentially 100+ available Skills".
- § Observe how Claude navigates Skills, `:846` — "Claude uses these when determining whether to trigger the Skill in response to the current task."
- The three worked examples (`best-practices.md:219-246`) separate skills by *domain* (PDF / Excel / git commit), never by naming a sibling or by a rule for two matching descriptions; nowhere does the page tell an author to name neighbouring skills.

**F3 — Plain answer on the tie-break (Q14): the page does NOT document a tie-break between two
overlapping skills.** Sweep over the fetched 42,169 B markdown (`grep -ciE <pattern> best-practices.md`, 2026-10-22):

| pattern | count | exit | pattern | count | exit |
|---|---|---|---|---|---|
| `overlap` | 1 | 0 | `same name` | 0 | 1 |
| `ambigu` | 0 | 1 | `prioriti` | 0 | 1 |
| `precedence` | 0 | 1 | `1024` | 0 | 1 |
| `tie[- ]?break` | 0 | 1 | `truncat` | 0 | 1 |
| `conflict` | 3 | 0 | combined (all ten) | 5 | 0 |
| `multiple skills` | 1 | 0 | `1024\|1,024` (widened) | 2 | 0 |

Every non-zero count is located and none is about skill selection: `:198` "Organize and search through multiple Skills" (a benefit of consistent naming); `:474` "Conflicting viewpoints (if any)" (report template); `:976` "Check for overlapping bounding boxes" (PDF form validation); `:980` "lists conflicts"; `:1016` "create conflicting values". The `1024` count is 0 because the page writes the cap with a comma — "Maximum 1,024 characters" (`:161`, `:1134`); the widened `1024|1,024` sweep gives 2 (exit 0), those two lines. The same ten patterns over the HTML route give `overlap` 2, `precedence` 2, `conflict` 4, `multiple skills` 2, `1024` 4, `truncat` 1, `ambigu`/`tie[- ]?break`/`same name`/`prioriti` 0 — every one of those hits is site chrome (`data-precedence="next"`, the `truncate` CSS class, SVG `width="1024"`) or the same PDF/report prose, so the negative claim holds for both routes.

**F4 — Consequence for C1 and D3.** With no documented tie-break, the description text is the only
arbitration surface this page offers ("Your description must provide enough detail for Claude to
determine when to select this Skill", `:215`) — the vendor-side warrant for C1's edit: naming the nine
sibling lanes is how a skill says when it is *not* the one to load. And the D3 precedence ruling has
no vendor authority to cite from this page; it must be stated as kotoba's own rule (the same
conclusion the VS Code seat reached for its page).

**F5 — The description rules C1's edit must respect do not bind it.** `yaml.safe_load` of the lane
`SKILL.md` frontmatter: description = **815** characters; with the four missing lane names
(`chousa`, `kama`, `kotodama`, `tameshi`) and "five"→"nine": **848** characters — 176 under the
1,024-character cap (`:161`); no XML tag in the current description. On third person (`:206`): the
current description opens with a bare verb phrase ("Prompt & skill craft — audits, writes, and
rewrites SKILL.md / AGENTS.md"), not a third-person subject; the lane enforces no third-person rule
(`corpus/knowledge/frontmatter-rule-authorities-round48.md:46`, lane-checker column "no rule"), so
whether that is a defect is the lane's call, not this source's.

## Deliverable 1 — `corpus/SOURCES.md`, row S019: old → new for every changed cell

Unchanged cells: `id` (S019), `source`, `kind` (docs), `tier` (A), `status` (mined), `opened` (2026-10-22), `recheck` (90d).

| cell | old | new |
|---|---|---|
| scope | Anthropic's authoring rules for name and description | Anthropic's authoring rules for name and description, and what the page says about choosing between overlapping Skills (vendor documentation, not a measurement of omp or opencode) |
| anchor | § Skill structure field list, § Writing effective descriptions, § Progressive disclosure patterns; fetched as .../best-practices.md (200, 42169 B, sha256 `f0a5d61b…`) on 2026-10-22; the round-47 fetch was 42028 B, sha256 `727f3fa1…` — editorial drift only, the rule lines are unchanged | § Skill structure (`best-practices.md:146-166`), § Writing effective descriptions (`best-practices.md:201-215`), § Observe how Claude navigates Skills (`best-practices.md:846`), § Technical notes → § YAML frontmatter requirements (`best-practices.md:1129-1134`), § Progressive disclosure patterns; fetched as .../best-practices.md (200, 42,169 B, sha256 `f0a5d61b…`) on 2026-10-22, re-opened 2026-10-22T12:28:47Z byte-identical to the bytes this row records; the round-47 fetch was 42,028 B, sha256 `727f3fa1…` — editorial drift only, the rule lines are unchanged |
| teaches | supersedes S003 — the 500-line body rule is not Anthropic-only: the open spec states it too (S018 § Progressive disclosure); Anthropic-only are the no-XML-tags rule on both `name` and `description`, the reserved words "anthropic" and "claude", and the third-person description rule | supersedes S003 — the 500-line body rule is not Anthropic-only: the open spec states it too (S018 § Progressive disclosure); Anthropic-only are the no-XML-tags rule on both `name` and `description`, the reserved words "anthropic" and "claude", and the third-person description rule; the page states no tie-break between two overlapping Skills (sweep over the 42,169 B fetch: `overlap` 1, `ambigu` 0, `precedence` 0, `tie[- ]?break` 0, `conflict` 3, `multiple skills` 1, `same name` 0, `prioriti` 0, `1024` 0, `truncat` 0 — the five hits are `multiple Skills` at :198 about naming and PDF-form text at :474, :976, :980, :1016), so the description is the only arbitration surface this page offers (:215); the description cap is "Maximum 1,024 characters" (:161 and :1134, written with a comma), non-empty, no XML tags, and the page asks for what plus when (:163, :203) |
| used-by | SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md | SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md, corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md |

The landing form of the row (13 pipe-separated fields, NF=13, verified) is the diff at
`…/src-reopen-s019/draft_S019_row.diff` and `…/src-reopen-s019/draft_row_S019.md`; the four changed
cells above carry its complete text.

## Deliverable 2 — round-lesson `## Gate` line for `corpus/lessons/round-50.md`

```markdown
**Existing row re-opened:** S019 (Claude Docs — Agent Skills best practices), `https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md`, fetched 2026-10-22T12:28:47Z: 200, 42,169 B, sha256 `f0a5d61b…`, byte-identical to the bytes the row records. Quote: "Your description must provide enough detail for Claude to determine when to select this Skill" (§ Writing effective descriptions, `best-practices.md:215`). Status `mined` → `mined`; recheck `90d` → `90d`; `used-by` `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md` → `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md, corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md` (seat `.ufo/waves/round-50/build/SrcReopenS019.md`).

**Tie-break (Q14):** this page documents no tie-break between two overlapping Skills. Sweep over the fetched 42,169 B markdown, 2026-10-22 (`grep -ciE <pattern> best-practices.md`): `overlap` 1 (exit 0), `ambigu` 0 (exit 1), `precedence` 0 (exit 1), `tie[- ]?break` 0 (exit 1), `conflict` 3 (exit 0), `multiple skills` 1 (exit 0), `same name` 0 (exit 1), `prioriti` 0 (exit 1), `1024` 0 (exit 1), `truncat` 0 (exit 1); the ten combined give 5 (exit 0). The five hits are `Organize and search through multiple Skills` (`best-practices.md:198`, about naming), `Conflicting viewpoints` (:474), `overlapping bounding boxes` (:976), `conflicts` (:980) and `conflicting values` (:1016) — the last four are PDF-form guidance. The `1024` count is 0 because the page writes the cap as "Maximum 1,024 characters" (:161, :1134); `grep -ciE '1024|1,024'` → 2 (exit 0). The same ten patterns over the HTML route (1,212,371 B, sha256 `028c47fe…`) hit only site chrome (`data-precedence="next"`, the `truncate` CSS class, SVG `width="1024"`) and the same PDF prose. Bearing on C1: the description is the only arbitration surface this page offers, and its 1,024-character cap does not bind the nine-lane description (815 characters now, 848 with the four missing lane names).
```

## Deliverable 3 — citation line for the census entry's appended section (draft, for the census owner)

```markdown
- Anthropic's authoring guide states no tie-break either: the description "must provide enough detail for Claude to determine when to select this Skill" (S019, `best-practices.md:215`), and the page carries no rule for two matching descriptions (sweep over the 42,169 B fetch: `overlap` 1, `ambigu` 0, `precedence` 0, `tie[- ]?break` 0, `conflict` 3, `multiple skills` 1, `same name` 0, `prioriti` 0, `1024` 0, `truncat` 0; the five hits are about naming and PDF forms — seat `.ufo/waves/round-50/build/SrcReopenS019.md`).
```

## Evidence (commands, exit codes, paths)

- Fetch: `curl -sS -L -o best-practices.md -w 'HTTP %{http_code} bytes=%{size_download} url=%{url_effective}\n' <url>` → HTTP 200, 42,169 B, exit 0; `sha256sum best-practices.md` → `f0a5d61b…`; `date -u +%Y-%m-%dT%H:%M:%SZ` → 2026-10-22T12:28:47Z. HTML route → HTTP 200, 1,212,371 B, sha256 `028c47fe…`.
- Sweep: `for p in 'overlap' 'ambigu' 'precedence' 'tie[- ]?break' 'conflict' 'multiple skills' 'same name' 'prioriti' '1024' 'truncat'; do c=$(grep -ciE "$p" best-practices.md); rc=$?; …; done` (counts and per-pattern exit codes in the F3 table); combined ten → 5, exit 0; `grep -ciE '1024|1,024'` → 2, exit 0; `grep -niE 'overlap|ambigu|precedence|tie[- ]?break|conflict|multiple skills|same name|prioriti|1024|truncat' best-practices.md` → lines 198, 474, 976, 980, 1016.
- Quoted lines read with `grep -n '' best-practices.md | sed -n '<n>p'`: 160, 161, 162, 163, 203, 206, 213, 215, 846, 1134.
- Row shape: `awk -F'|' '/^\| S019 /{print NF}'` → 13 (exit 0), as for every other row.
- Registry validation with the fleet instrument on a private clone at `f3046466` (`…/src-reopen-s019/lane`): `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file lane/corpus/SOURCES.md` → exit 1 with `E11 S019 missing used-by corpus/lessons/round-50.md` (the round-50 lesson file does not exist in the clone) plus the three pre-existing W04 (S018, S019, S021); after `touch lane/corpus/lessons/round-50.md` → exit 0, `ok`, same three W04, no new warning; with `corpus/lessons/round-50.md` dropped from `used-by` → exit 0, `ok` as well; the unmodified lane file → exit 0, `ok`, same three W04. **Landing constraint (not mine to land): `corpus/lessons/round-50.md` must exist when the row lands.**
- C1 counter on the lane base (read-only `git show f3046466:SKILL.md | awk … | grep -oiwE 'chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi' | sort -u | wc -l`) → 5 (exit 0), matching the plan's before-value; the census lists all nine lanes as `adjacent` at that commit.
- Description length: `yaml.safe_load` of the lane `SKILL.md` frontmatter → 815 characters; + the four missing lane names and "five"→"nine" → 848 (176 under the documented 1,024 cap); the folded-scalar join of the same text gives 814 → 847 (the 1-character difference is the folded block's trailing newline).

## Out of scope

- Editing `corpus/SOURCES.md`, `corpus/lessons/round-50.md` or the census entry: drafts only (lane bound; the L1 integrates). Nothing outside this report was written in the lane.
- The C1 description edit itself, and the wording of the D3 precedence ruling (other seats).
- Other Anthropic pages (`overview`, `code.claude.com/docs/en/skills` — rows S023, S022): this seat's negative claim covers the best-practices page only, both routes. Measuring how omp or opencode actually arbitrate between two loaded skills is out of scope for a vendor page.

## Artifacts

- `…/src-reopen-s019/best-practices.md` — the swept text (42,169 B, 1,191 lines, sha256 `f0a5d61b…`); `best-practices.html` — the HTML route (1,212,371 B, sha256 `028c47fe…`).
- `…/src-reopen-s019/draft_row_S019.md` — the landing row; `…/src-reopen-s019/draft_S019_row.diff` — its unified diff against `f3046466` (1 insertion, 1 deletion, `corpus/SOURCES.md`).
- `…/src-reopen-s019/lane/` — private clone of the lane at `f3046466` carrying the draft row (mirror only; the lane checkout was not modified).

## Tooling

None installed or upgraded: `curl`, `grep`, `sed`, `awk`, `sha256sum`, `date`, `git`, `python3` (interpreter only) and the fleet's `scripts/sources-census.sh` were already present. No `pacman`, `uv tool`, `cargo` or `npm -g` transaction was run, and no host service was restarted.
