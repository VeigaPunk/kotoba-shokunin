Result: HOLDS — all four VS Code cells (SOURCES S055, entry Per-client record, lesson Gate, SKILL.md table row) are verbatim-faithful to a byte-identical re-fetch of the page (sha256 match), the number is on the `description` field, no cell says more than the page and seat evidence support, and nothing contradicts older lane rows (S025, skill-selection-rules-round50, sibling-overlap-census-round49).

## Scope

Attack on the VS Code rows landed at `5a097e12b9409a1f425fbc76334f36f1402eb4cc` (tip `58db81c4`):
`corpus/SOURCES.md:68` (S055), `corpus/knowledge/skill-listing-thresholds-round54.md:42` (Per-client
record), `corpus/lessons/round-54.md:25` (Gate), `SKILL.md:187` (`### Description thresholds by client`).

## Re-fetch records (ordinary curl, no browser, no auth)

| what | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| served markdown (quoted source) | https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 2026-10-22T21:55:56Z | 200 | 22,871 | `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` |
| docs source file | https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d648/docs/agent-customization/agent-skills.md | 2026-10-22T22:06:47Z | 200 | 24,087 | `bae0c84d97f58b24a60611250db17d125fcccfe7217379494e055702167a8ccb` |

Command: `curl -sS -D headers.txt -o agent-skills.md -w 'HTTP %{http_code}, %{size_download} bytes\n' <url>`,
exit 0. Response headers: `content-type: text/markdown; charset=UTF-8`, `content-length: 22871`,
`last-modified: Thu, 22 Oct 2026 18:02:44 GMT` — same stamp the seat recorded.
The served bytes are sha256-identical to the Gate record and to the pin S025 already carried
(`corpus/SOURCES.md:38`, `de5ba34f…`, 22,871 B), so the S055 anchor claim "byte-identical to the
12:29:33Z pin recorded in S025" HOLDS.

## Cell-by-cell verdicts

### 1. `corpus/SOURCES.md` S055 (`:68`) — HOLDS

- 11 cells, `docs | A | … | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md`
  — satisfies every counter field (`check_description_thresholds.py` docstring; `90d` matches 41 other
  rows' recheck convention).
- `source` cell first URL `code.visualstudio.com/docs/agent-customization/agent-skills` is on the pinned
  host `code.visualstudio.com` (`HOSTS["VS Code"]`, `check_description_thresholds.py:91-94`).
- Anchor `§ SKILL.md file format → § Header (required), description row (agent-skills.md:148)`:
  page headings are `## SKILL.md file format` (fetched bytes `:137`) → `### Header (required)` (`:141`);
  the `description` row with the 1024 sentence is exactly `:148`. Anchors `§ How Copilot uses skills`
  step 1 Discovery (`:302`) and the three-level note (`:308`) verified verbatim in the fetched bytes.
- Anchor tail "upstream `docs/agent-customization/agent-skills.md:159` in microsoft/vscode-docs at
  `fd64d648` (24,087 B, sha256 `bae0c84d…`), same sentence": raw fetch at that commit is 24,087 B,
  `bae0c84d…`, and the sentence sits verbatim at `:159`. HOLDS.
- `teaches` cell "A skill's description helps Copilot decide when to load the skill, and its maximum is
  1024 characters" is a paraphrase no wider than the quote; it asserts no consequence past the cap.

### 2. Entry Per-client record (`skill-listing-thresholds-round54.md:42`) — HOLDS

- `row` cell `S055`; `location` `agent-skills.md:148` correct.
- Quote `"help Copilot decide when to load the skill. Maximum 1024 characters."` is verbatim inside the
  fetched bytes at `:148` (`grep -c -F` → 1, exit 0), 11 words (3–25 window), carries `1024` as a whole
  token, byte-identical to the Gate row's quote. It is the `description` field's table row, not another
  field — the `name` cap (64, `:147`) is a different sentence and is not quoted.
- `reading` cell "An authoring maximum: the page states a `description` maximum of 1024 characters and
  no consequence, cut or budget past it" — verified by my own sweep of the fetched bytes:
  `grep -n -iE '1024|truncat|budget|shorten|omitted|warning|refus|drop|limit|maximum|fail'` shows `1024`
  only at `:148`, and the only documented consequence on the page is "silently fail to load" on the
  `name` field for *invalid characters* (`:147`) and for plugin namespace prefixes (`:155`), neither of
  which is a description-length consequence. The reading says no more than the page.
- Findings §1's clause "(VS Code S055 …) documents 1,024 characters for `description`; none of their
  pages documents a cut at that number" — accurate for this page.

### 3. Lesson § Gate row (`round-54.md:25`) — HOLDS

URL, `2026-10-22T21:15:47Z`, `22,871 B`, sha256 `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5`,
quote, `agent-skills.md:148`, `SrcVSCode` — every cell matches my independent re-fetch byte-for-byte.

### 4. `SKILL.md:187` row — HOLDS (two nits, not breaks)

- Threshold cell "`description` maximum 1024 characters (authoring maximum; `name` 64)" — supported:
  `1024` at `:148`, `64` at `:147`. The counter reads tokens `["1024","64"]` and the quote carries `1024`.
- Past-the-threshold cell "Not documented: the page states no truncation, drop, warning or refusal past
  1024, and no listing budget" — page-scoped and true on the fetched bytes (sweep above; the "context
  efficient"/"without consuming context" lines at `:300,:308` state no number). The client-wide form of
  this negative is backed by the seat's three-part Q30 sweep (release notes v1_141–143 HTML, the
  vscode-docs tree at `fd64d648`, the lane corpus) in `.ufo/waves/round-54/build/SrcVSCode.md` § Absence
  sweep — Q30 satisfied, though the SKILL.md cell only needed the page scope.
- Action cell "Keep the description under 1024 characters, leading with what the skill does and when to
  use it" — the page says the description should say "what the skill does **and when to use it**", so
  the advice is grounded; "under" vs "at most" is conservative authoring advice, within the table's
  advisory convention (cf. Copilot CLI row's "at 1024 characters or fewer").

Nits (cosmetic, no correction needed):
- `(…; name 64)` puts a `name`-field number inside a `description` table; accurate but could mislead a
  skimmer. Optional fix: drop the parenthetical or move `name` 64 to a footnote.
- The table writes `1024` for VS Code/Copilot CLI (page-faithful) but `1,024` for Cursor for the same
  number — mixed typography, both match their own pages.

## Counter and guard verification (sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2SrcVSCode/lane` at `58db81c4`)

- `python3 -B verifiers/check_description_thresholds.py --root .` → `description thresholds backed 7 of 7
  clients`, exit 0; `--json` shows VS Code: row `S055`, `backed: true`, `why: []`, tokens `["1024","64"]`.
- `python3 -B verifiers/check_description_thresholds.py --root . --fetch` → `VS Code BACKED found=True`,
  `found on the live page 7 of 7`, exit 0 — erratum-3 guard (c) satisfied for this client.
- Guard (a): `git show e3371548:corpus/SOURCES.md | grep -c S055` → 0 (exit 1): S055 was opened this round.
- Guard (b): `git show e3371548:SKILL.md | grep -c -F '1024'` → 1, `'1,024'` → 1 — matches plan erratum 3's
  record, so VS Code supplies no new ground itself; the guard's ≥2-new-clients requirement is met by
  other clients (Codex `2%`/`8,000`, Claude `1,536`/`1%`), which is what the plan anticipated.
- Q28: counter blob untouched (frozen at plan commit; seats never edited it).

## Contradiction check vs older lane records

- S025 (`SOURCES.md:38`, same page, same bytes, 12:29Z pin): teaches the same 1024 cap — consistent.
- `skill-selection-rules-round50.md:19` (same page, `truncat 0` sweep) and `sibling-overlap-census-round49.md`
  (same page, 22,871 B) — consistent; the entry § Relation acknowledges the prior 1,024 record and scopes
  its new content to "which clients restate it". No older row claims a VS Code listing cut or budget
  (`grep -rn -i 'vs ?code|visualstudio' corpus/knowledge | grep -i 'truncat|listing|cut'` → only the new
  entry and the round-50 discovery quote).

## Evidence files

`/fast/scratch/hyaku/kotoba-r54/W2SrcVSCode/agent-skills.md` (22,871 B, `de5ba34f…`), `headers.txt`,
`upstream-agent-skills.md` (24,087 B, `bae0c84d…`), `lane/` sandbox clone.

## Bounds

No lane file written except this report; no git/jj writes in the lane; no client CLI invoked; no tools
installed (system curl/python3/git sufficed); no `model` parameter, no `ask`.
