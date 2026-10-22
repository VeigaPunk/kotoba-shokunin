Result: DONE — Cursor documents exactly one number for this area: a `description` over 1,024 characters is flagged by `/skills` and the skill still loads; row S058 is counter-conformant and its quote is found on the live page.

Seat: KotobaR54.SrcCursor (scribe, round-54 build wave). Target client `Cursor`, reserved row `S058`.
No lane edits, no git or jj writes in the lane, no installs, no paid model calls. Everything below was
read or run in this seat's own scratch and sandbox clone.

## 1. What Cursor documents (the finding)

Cursor's only numeric limit on how much of a skill's `description` is accepted is an **authoring maximum
with a warning, not a cut**: a description over 1,024 characters draws a warning count in `/skills`, and
the skill still loads.

Full sentence, `https://cursor.com/docs/release-notes.md:122` (§ v2026.10.08 → § Skills, heading at
`:110`, `:120`), 484 bytes on one line:

```
- **`/skills` flags skills that break the Agent Skills limits.** Skills that load but exceed the spec's limits now show a yellow warning count in `/skills`, and selecting one lists what to fix under it. Warnings cover a name over 64 characters or not in lowercase-hyphen form, a frontmatter `name` that doesn't match the folder, a description over 1,024 characters, and a body over about 5,000 tokens. See the [SKILL.md format](https://cursor.com/docs/skills.md#skillmd-file-format).
```

The same sentence is byte-identical at `https://cursor.com/docs/cli/changelog.md:17` (verified by string
equality on the two fetched files: `identical sentence: True`).

The numbers in it, and what each limits:

| number | object | effect past it |
|---|---|---|
| 1,024 characters | `description` | warning in `/skills`; skill loads |
| 64 characters | `name` | warning in `/skills` |
| about 5,000 tokens | SKILL.md body | warning in `/skills` |

The description number is the one the C1 table uses. The render side is documented only qualitatively:
`docs/skills.md:27` "The agent is presented with available skills"; `docs/agent/prompting.md:49`
"**Skills**: skill descriptions injected into the system context"; the only documented budget is the
shared context window (`docs/agent/prompting.md:42`), which describes conversation compaction, not a
per-skill cut. `docs/rules.md:155` "Keep rules under 500 lines" is a rule-file limit, a different object,
and is not used as a Cursor number here (the critic's attack 3 used exactly that line for Cursor, world
B-other-sense-numbers, `CriticC1Sizing.md` § 3).

## 2. Delivered rows (verbatim, as verified below)

`corpus/SOURCES.md` row (11 cells; inserted after S052, inside the registry table, before `## Paths`):

```
| S058 | Cursor Docs — Release notes — https://cursor.com/docs/release-notes.md | docs | A | Cursor's documented `/skills` warning set for a skill's name and description length | § v2026.10.08 → § Skills (`release-notes.md:120-122`); served text/markdown, fetched 2026-10-22T21:19:23Z (301,193 B, sha256 fd4d830a…); the same sentence is byte-identical at `cli/changelog.md:17`; the bullet also lists a body over about 5,000 tokens | Warnings cover a name over 64 characters, a folder-name mismatch and a description over 1,024 characters | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md |
```

`corpus/knowledge/skill-listing-thresholds-round54.md` § `## Per-client record` row:

```
| Cursor | S058 | "Warnings cover a name over 64 characters or not in lowercase-hyphen form, a frontmatter `name` that doesn't match the folder, a description over 1,024 characters" | `release-notes.md:122` | Authoring maximum, not a listing cut: the release notes place it in the `/skills` warning set, so an over-length description still loads and no truncation, shortening, drop or refusal is documented. |
```

`SKILL.md` § `### Description thresholds by client` row:

```
| Cursor | 1,024 characters for `description` | Warned, not cut: the skill still loads and `/skills` shows a yellow warning count listing what to fix (a body over about 5,000 tokens is warned the same way) | Keep `description` at or under 1,024 characters; move detail into `references/` rather than the body |
```

`corpus/lessons/round-54.md` § `## Gate` row:

```
| S058 | https://cursor.com/docs/release-notes.md | 2026-10-22T21:19:23Z | 301,193 B, sha256 fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd | "Warnings cover a name over 64 characters or not in lowercase-hyphen form, a frontmatter `name` that doesn't match the folder, a description over 1,024 characters" | `release-notes.md:122` | SrcCursor |
```

The quote is exactly 25 words (the counter's `MAX_WORDS` ceiling) and occurs once in the page bytes, at
byte offset 21,968. It is the clause that carries both the number and the mechanism ("Warnings cover"),
so the entry reading and the registry `teaches` cell assert nothing the quote does not say. The body
limit is in the past-the-threshold cell and the SOURCES anchor, not in the quote.

## 3. Fetch record

Primary source:

| field | value |
|---|---|
| URL | https://cursor.com/docs/release-notes.md |
| UTC | 2026-10-22T21:19:23Z (curl started and finished in the same second) |
| HTTP | 200 |
| bytes | 301,193 |
| sha256 | fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd |
| content-type | text/markdown; charset=utf-8 |
| response date header | Thu, 22 Oct 2026 21:16:43 GMT (cache-control: public, max-age=3600; differs from the local clock by ~2m40s) |

Stability: the same URL was fetched three times this session (the 21:16Z batch, the bulk docs-tree fetch,
and the header capture at 21:19:23Z); all three copies hash to `fd4d830a…` — the bytes did not move
during the seat. Command:

```
curl -sS -L --max-time 60 -A 'Mozilla/5.0 kotoba-research/54' -D headers-release-notes.txt \
  -o refetch-release-notes.md -w "status=%{http_code} bytes=%{size_download} content_type=%{content_type}\n" \
  https://cursor.com/docs/release-notes.md
status=200 bytes=301193 content_type=text/markdown; charset=utf-8
```

Supporting pages. `skills.md` and `agent/prompting.md` were re-fetched at 2026-10-22T21:29:48Z and hash the
same as the round's first fetch; `cli/changelog.md` was fetched in the 21:16Z batch and hashed then;
`rules.md` was fetched in the same batch and is cited by line only.

| URL | bytes | sha256 | line cited |
|---|---|---|---|
| https://cursor.com/docs/skills.md | 18,477 | a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d | `:27` |
| https://cursor.com/docs/agent/prompting.md | 4,485 | 438f77bf7295d28002c81ce0658134ce7debe6dfa76bae926058b918ed378410 | `:42`, `:49` |
| https://cursor.com/docs/cli/changelog.md | 56,159 | 70d57616d76ddfa089d42b23a149fad68436ecd8711a94b33c13c3c64795167b | `:17` |
| https://cursor.com/docs/rules.md | 17,403 | not hashed here (S049 records `884c67ca…`) | `:155` |

## 4. Verification (counter, run only in the sandbox clone)

Sandbox: `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q … /fast/scratch/hyaku/kotoba-r54/SrcCursor/clone && git -C … checkout -q 7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`
→ `7ad05d3 round-54: move SKILL.md verifier bullets verbatim …`. The four rows above were written into the
clone (SKILL.md table appended, entry created, S058 inserted, lesson created) and the frozen counter run:

```
python3 -B verifiers/check_description_thresholds.py --rev 7ad05d342d7505ab674a5ebcf5ac1106b2f45c39
description thresholds backed 0 of 7 clients                    exit 1   (before)

python3 -B verifiers/check_description_thresholds.py --root .
Cursor       BACKED
description thresholds backed 1 of 7 clients                   exit 1   (1 < target 4; Cursor-only fixture)

python3 -B verifiers/check_description_thresholds.py --root . --fetch
Cursor       BACKED found=True
description thresholds backed 1 of 7 clients
description thresholds found on the live page 1 of 1            exit 1
```

Must-fail arms against this row (each applied to the fixture, then restored; restored run prints
`Cursor BACKED`, `backed 1 of 7`, exit 1):

| mutant | observed |
|---|---|
| A entry + Gate quote `1,024`→`1,025`, SKILL cell stays 1,024 | `Cursor no quote holds none of the threshold numbers ['1,024']` — backed 0 of 7 |
| B source URL `cursor.com`→`cursor.com.evil.io` | `Cursor no S058 source URL 'https://cursor.com.evil.io/…' not on a pinned host` |
| C Gate records a fragment (`"Warnings cover a name over 64 characters"`) | `Cursor no round-54 Gate does not record this quote for S058` |
| D SKILL action cell set to `—` | `Cursor no SKILL.md action cell empty` |
| E control: cell and both quotes agree on 1,025 | `Cursor BACKED` (match is by number, not by literal string) |

## 5. What Cursor does *not* document (Q30 three-part sweep)

No per-entry cut in the skill listing, no listing budget, no truncation, shortening, drop or refusal for
an over-length description. The three Q30 legs, with commands and observed output:

**(a) Changelog and release notes.**

```
$ grep -c -i "skill" cursor.com_changelog            # https://cursor.com/changelog(.md), served as HTML
0
$ grep -n -iE "skill" cursor.com_docs_release-notes.md | grep -E "[0-9]"
… 25 lines; the only numeric skill-limit line is 122 …
$ grep -n -iE "skill" cursor.com_docs_release-notes.md | grep -iE "truncat|shorten|budget|character|token"
122
$ grep -n "1,024" cursor.com_docs_cli_changelog.md
17
```

**(b) Current docs tree and help tree.** All `.md` pages indexed by `https://cursor.com/llms.txt` were
fetched: 168 docs pages and 109 help pages, every response 200 (`fetch-codes.txt`, `help-codes.txt`).

```
$ grep -rniE "skill.{0,80}(truncat|shorten|budget|character|token|limit|max)|(truncat|shorten|budget|character|token|limit|max).{0,80}skill" docs help
docs/cli__changelog.md:17            … the /skills warning block (same sentence) …
docs/enterprise__security-hardening.md:96   plugin review advice, no number
docs/enterprise__opentelemetry-export.md:3,308  telemetry recipe, no number
docs/release-notes.md:122            … the /skills warning block …
docs/skills.md:182                   `paths` scoping, no number
```

**(c) Lane corpus.**

```
$ grep -rn -iE "cursor" corpus/ SKILL.md | grep -icE "skill|descri|1,024|1024|threshold|truncat"
5
$ … same without -c
corpus/knowledge/instruction-surface-remeasure-round13.md:58
corpus/knowledge/alwayson-rule-files-round53.md:1
corpus/knowledge/instruction-surface-census-round13.md:88, :379
corpus/README.md:40
```

None of the five is a Cursor skill-description threshold. `corpus/knowledge/skill-selection-rules-round50.md:46`
records 1,024-character caps for opencode, VS Code and Anthropic; it does not name Cursor.

Conclusion: the only Cursor number in this area is the 1,024-character authoring maximum (with the 64-char
name and ~5,000-token body warnings in the same bullet). "No per-entry cut and no listing budget" is a
documented-absence claim with the sweep above; it is not a claim that Cursor's loader behaves that way in
practice — the lane has no Cursor render measurement.

## 6. Findings

- **F1 — the reference page is silent.** The release note links to `cursor.com/docs/skills.md#skillmd-file-format`,
  but that section (`docs/skills.md:141-178`) lists `name`, `description`, `paths`,
  `disable-model-invocation`, `icon`, `color`, `metadata` with no numbers at all; a digit grep over the
  whole page returns only step numbers (`:286-306`, `:318`, `:327-329`). An author who reads only the
  reference will not learn the cap.
- **F2 — authoring maximum, not a render cut.** The documented consequence is a warning count in `/skills`
  ("Skills that load but exceed the spec's limits now show a yellow warning count"); the skill loads. This
  is a different shape from Claude Code's 1,536-character listing truncation recorded in the round-50
  entry (`skill-selection-rules-round50.md:46-48`), so Cursor must not be written as a truncating client.
- **F3 — counter drafting hazard, observed.** The counter matches *any* number in the threshold cell
  against the quote. A first draft quote carrying the body number as well
  (`"a description over 1,024 characters, and a body over about 5,000 tokens"`), with a threshold cell that
  named both numbers, still printed `Cursor BACKED` after the description number was changed to 1,025 in
  both the entry and the Gate — the 5,000 satisfied the token match. Observed:
  `A2 quotes 1,025 vs cell 1,024  Cursor BACKED`. The delivered row removes the second number from the
  threshold cell, and mutant A now kills it. Other scribes should keep one number in the threshold cell.
- **F4 — new ground.** S058 is not a reuse of rounds 48-53: the lane held no Cursor skill-description
  number before this round (sweep § 5c), and the row's URL is the client's own release notes. This is the
  new-ground count the C1 critic (attack 2) asks the judge to read beside the declared line.
- **F5 — the HTML changelog is a false silence.** `https://cursor.com/changelog` and
  `https://cursor.com/changelog.md` are served as HTML with zero occurrences of "skill" in the bytes
  (client-rendered payload). A changelog sweep that stops there records Cursor as silent and misses the
  number; the markdown `docs/release-notes.md` and `docs/cli/changelog.md` carry it.
- **F6 — one-side page-vs-source comparison.** No docs source repository is linked anywhere in the 277
  fetched pages; the only GitHub repositories referenced are product SDKs (`cursor/sdk-bridge`,
  `cursor/cookbook`, `anysphere/k8s-workers`) and placeholder `your-org` examples. Cursor publishes the
  served `.md` only, so there is no separate source tree to diff; the fetched page is the source.
- **F7 — the quote sits at the word ceiling.** Exactly 25 words; the counter accepts 3–25. Do not add
  words when integrating, or the client drops.

## 7. For the L1 (integration notes)

- Target files and anchors: SOURCES row after `| S052 |` inside the registry table (before `## Paths`);
  SKILL.md row under `### Description thresholds by client` with header
  `| Client | Documented threshold | Past the threshold | Action |`; entry row under `## Per-client record`
  with header `| client | row | quote | location | reading |`; Gate row under `## Gate`.
- At lane tip `bf65974`: `SKILL.md` is 585 lines, has `## Gate registry` (`:433`) and no
  `Description thresholds by client` heading yet; `corpus/knowledge/skill-listing-thresholds-round54.md`
  and `corpus/lessons/round-54.md` do not exist yet. A 7-client table costs ~12 lines (heading, header,
  separator, 7 rows), putting SKILL.md at ~597 of the 600-line budget — no room for extra prose.
- The SOURCES row parses as exactly 11 cells under the counter's `sources_table` (13 pipe fields), no pipe
  inside any cell (checked with the counter's own cell split).
- `--fetch` fetched only the backed row and found the quote (`found=True`), so the row's provenance is
  live-checked, not only Gate-consistent.

## 8. Not done / out of scope

No lane file was edited (only this report was written); no entry assembled; no counter changed; no C2 work;
no other client opened as a threshold source; no jj; no commits; no tool installs. The "no per-entry cut /
listing budget" negative is documented-absence only, and Cursor's runtime behavior was not measured.

## 9. Artifacts

Scratch root `/fast/scratch/hyaku/kotoba-r54/SrcCursor/`:

- `fetch/refetch-release-notes.md`, `fetch/headers-release-notes.txt` — the 301,193 B page and its headers.
- `fetch/cursor.com_docs_release-notes.md`, `cursor.com_docs_cli_changelog.md`, `cursor.com_docs_skills.md`,
  `cursor.com_docs_agent_prompting.md`, `cursor.com_docs_rules.md`, `cursor.com_help_customization_skills.md`.
- `fetch/docs/` (168 pages), `fetch/help/` (109 pages), `fetch/docs-urls.txt`, `help-urls.txt`,
  `fetch-codes.txt`, `help-codes.txt`.
- `fetch/quote.txt` — the 25-word quote as extracted from the page bytes.
- `clone/` — sandbox at `7ad05d3` holding the four-row fixture (SKILL.md appended, entry, S058, lesson).
- `before.txt`, `after.txt` — counter output for the before run and the `--fetch` after run.
