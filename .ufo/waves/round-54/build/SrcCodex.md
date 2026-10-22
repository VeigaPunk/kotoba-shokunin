Result: DONE — Codex documents one listing budget (2% of the model's context window, or 8,000 characters when the window is unknown), a 10,000-token cap on the override, and what it does past the budget (shorten descriptions first, then omit skills with a warning); the S054 row, entry row, Gate row and SKILL.md row below make the Codex client backed in a sandbox run, and none of the five skill pages in the docs map states a per-description authoring maximum.

Seat: `KotobaR54.SrcCodex` (leaf, C1 client *Codex*, reserved SOURCES id S054). Lane read-only; the only lane file written is this report. Sandbox clone `/fast/scratch/hyaku/kotoba-r54/SrcCodex` at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`; all fixture writes and the counter runs happened there. No installs, no paid model calls.

## 1. What Codex documents (item 1 of the assignment, enumerated rather than sampled)

The client's own page is `https://learn.chatgpt.com/docs/build-skills.md` (11,035 B, 232 lines). Every line in those bytes that carries a digit (`grep -n '[0-9]' build-skills.md`), classified:

| line | text (excerpt) | what it is |
|---|---|---|
| `38-39` | "this list uses at most 2% of the model's / context window, or 8,000 characters when the context window is unknown." | the listing budget (two forms) |
| `44` | "different budget, up to 10,000 tokens." | the override ceiling |
| `95`, `98` | `1.` / `2.` explicit and implicit invocation | ordinals |
| `51`, `203` | `class="mt-4"`, a hex colour in a code sample | markup |

That is the complete set. On this page the topic has exactly three numbers, and all three bound the **initial skills list**, not one `description`.

What the page says around them, verbatim and by line:

- `:33-35` — "ChatGPT and Codex start with each skill's name and description, then load the full `SKILL.md` instructions when they decide to use that skill."
- `:37-41` — "In Codex, the initial list also includes each skill's file path. By default, this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown. If many skills are installed, Codex shortens skill descriptions first. For large skill sets, Codex may omit some skills from the initial list and show a warning."
- `:43-44` — "Use `skills.max_context_tokens` to set a different budget, up to 10,000 tokens."
- `:46` — "This budget applies only to the initial skills list. When Codex selects a skill, it still reads the full SKILL.md instructions for that skill."
- `:101-103` — "Because implicit matching depends on `description`, write concise descriptions with clear scope and boundaries. Front-load the key use case and trigger words so a host can still match the skill if descriptions are shortened."

A second page on the same pinned host states the budget in config terms, `https://learn.chatgpt.com/docs/config-file/config-reference.md` (136,297 B), `skills.max_context_tokens` block at `:375-379`, description at `:378`: "Token budget for the available-skills catalog. Defaults to 2% of the model's context window. Explicit values are capped at `10000` tokens."

Reading, in the terms the assignment asks for:

- **Listing budget** (the counted number): 2% of the model's context window, or 8,000 characters when the window is unknown. It is a budget over the whole initial skills list, which in Codex carries name, description and file path (`:37`).
- **Past the threshold, documented:** descriptions are shortened first, then for large skill sets skills may be omitted from the initial list with a warning (`:40-41`). No truncate/drop/refuse per description is stated. The budget does not touch the on-selection read: full `SKILL.md` still loads (`:46`).
- **Per-entry cut:** documented as an action (shortening), with **no number**. The page gives no character or token size for one entry's description.
- **Authoring maximum:** none on this page. Nothing here caps a `description`'s length; the only authoring advice is positional (front-load the use case and trigger words, `:101-103`).
- **Override:** `skills.max_context_tokens`, integer (positive), explicit values capped at `10000` tokens (config-reference `:376-378`); the 8,000-character fallback is stated only on build-skills.

## 2. Item 2 — fetch records (every quoted byte comes from these fetches)

| what | URL | opened (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| skills page (counted row) | https://learn.chatgpt.com/docs/build-skills.md | 2026-10-22T21:15:49Z | 200 | 11,035 | `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` |
| same page, rendered HTML (cross-check) | https://learn.chatgpt.com/docs/build-skills | 2026-10-22T21:16:58Z | 200 | 417,724 | `d3099440e88f158e97e83825c142352058a7c23d538a4a1cb96ab4e1f941d5ac` |
| config reference (second row) | https://learn.chatgpt.com/docs/config-file/config-reference.md | 2026-10-22T21:16:19Z | 200 | 136,297 | `fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21` |
| docs map used as the docs tree | https://learn.chatgpt.com/docs/llms.txt (307 from `/llms.txt`) | 2026-10-22T21:17:24Z | 200 | 33,447 | `fc7b20eaea56f8fe5dcc0280262009f9546172c521f69cb08b8befc89f03b943` |
| siblings swept, no limit numbers | `/docs/guides/tools-skills.md` | 2026-10-22T21:17:2xZ | 404 | 9 | `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31` |
| siblings swept, no limit numbers | `/docs/skills-and-plugins.md` | 2026-10-22T21:17:2xZ | 200 | 5,217 | `39aa27568d3b43caa874ddb3be384787ad57c83814d87723d3b1b8cde49ae153` |
| siblings swept, no limit numbers | `/docs/customization/overview.md` | 2026-10-22T21:17:2xZ | 200 | 9,482 | `e4f466bb13521bc8d4e193962192c45319d5abc0cb58875d4a7eed2a9f9a20d6` |
| siblings swept, no limit numbers | `/docs/enterprise/skills.md` | 2026-10-22T21:17:2xZ | 200 | 3,551 | `cea03f3708d47495b2a59949f516e9e9ab6575407c4ad1c4db38c3e4dd5125ee` |
| siblings swept, no limit numbers | `/docs/extend/record-and-replay.md` | 2026-10-22T21:20:2xZ | 200 | 3,607 | `36f40000558f2bf2d52fb7b24bf75b1daf2f94d58d7ec2e3a384403814cbe757` |

Honesty note: the four sibling `.md` files and the 404 were fetched in two batches and their stamps are the batch time after the fetches (`21:17:24Z` for the first four, `21:20:2xZ` for record-and-replay beside a `21:20:28Z` stamp), not per-request stamps; their bytes are the files hashed above. `/docs/guides/tools-skills` is linked from the rendered skills page and answers 404 in both forms (its 9-byte body is the site's "Not Found"), so it is a stale link, not a source.

## 3. Item 3 — SOURCES.md rows (single physical lines, 11 cells each)

```
| S054 | OpenAI — Build skills (ChatGPT and Codex) — https://learn.chatgpt.com/docs/build-skills | docs | A | Documented Codex skill-listing budget: the initial skills list and what changes past it (vendor documentation, not a measurement of an installed CLI) | § How ChatGPT and Codex use skills, md:33-46 — budget md:38-39, shortening and omission md:40-41, override md:43-44, scope md:46, authoring advice md:101-103; revision = build-skills.md sha256 ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5 (11,035 B, 232 lines), fetched 2026-10-22T21:15:49Z, HTTP 200, byte-identical to the S021 fetch of 2026-10-22T08:13:33Z | the initial skills list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md, corpus/lessons/round-54.md |
```

```
| S054b | OpenAI — Codex config reference — https://learn.chatgpt.com/docs/config-file/config-reference | docs | A | The skills.max_context_tokens setting: documented default and explicit-value cap (vendor documentation, not a measurement) | skills.max_context_tokens block, config-reference md:375-379 (description md:378); revision = config-reference.md sha256 fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21 (136,297 B), fetched 2026-10-22T21:16:19Z, HTTP 200 | the token budget for the available-skills catalog defaults to 2% of the model's context window, and explicit values are capped at 10000 tokens | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md, corpus/lessons/round-54.md |
```

Each `teaches` cell says no more than the Gate quote recorded for the same id (Q26); the "past it" behaviour and the authoring advice live in `anchor`, not in `teaches`.

## 4. Item 4 — entry row for `corpus/knowledge/skill-listing-thresholds-round54.md` § Per-client record

```
| Codex | S054 | "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown" | build-skills.md:38-39 (past-it md:40-41; scope md:46) | A listing budget over the whole initial skills list, not an authoring maximum on one description and not a documented per-entry cut: past it Codex shortens skill descriptions first and, for large skill sets, may omit skills from the initial list with a warning, while the full SKILL.md still loads once the skill is selected. |
```

The quote is 20 words, is a contiguous substring of the fetched bytes across the newline at `:38/:39`, and holds both numbers exactly as the page writes them (`2%`, `8,000`).

## 5. Item 5 — Gate rows for `corpus/lessons/round-54.md` § Gate

```
| S054 | https://learn.chatgpt.com/docs/build-skills.md | 2026-10-22T21:15:49Z | 11,035 B, `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` | "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown" | `build-skills.md:38-39` | SrcCodex |
| S054b | https://learn.chatgpt.com/docs/config-file/config-reference.md | 2026-10-22T21:16:19Z | 136,297 B, `fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21` | "Token budget for the available-skills catalog. Defaults to 2% of the model's context window. Explicit values are capped at `10000` tokens." | `config-reference.md:378` | SrcCodex |
```

The S054 quote here must be byte-identical to the entry row above; it is (Q32). The S054b quote is 21 words and backs the "past the threshold" and override cells, not the counted row.

## 6. Item 6 — draft SKILL.md row for `### Description thresholds by client`

```
| Codex | Initial skills list: 2% of the model's context window, or 8,000 characters when the context window is unknown; `skills.max_context_tokens` raises the default, capped at 10,000 tokens | Codex shortens skill descriptions first, then for large skill sets may omit skills from the initial list and show a warning; selecting the skill still reads the full `SKILL.md` | Front-load the use case and trigger words in `description` so matching survives shortening; do not rely on a long tail |
```

## 7. Did the bytes or quotes change since the lane last held this page? No

- S021 (`corpus/SOURCES.md:34`) was opened `2026-10-22` and records "build-skills.md sha256 `ed6e324f…` (11,035 B, 232 lines), fetched 2026-10-22T08:13:33Z". My fetch 12 hours later returns the same full sha256, bytes and line count, so the bytes are identical and every quote on the page is unchanged.
- S013 (`corpus/SOURCES.md:26`) is `queued`, opened `2026-10-21`, from a `308` of `developers.openai.com/codex/skills`; it carries no hash. The quote recorded for it in `corpus/lessons/round-47.md:36` at `2026-10-21T15:54:43Z` is *the same sentence I chose* ("this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown"), so the sentence is stable across 2026-10-21 → 2026-10-22 by two independent fetches.
- The rendered HTML's `Last-Modified` did move: `Thu, 22 Oct 2026 21:00:03 GMT`, `etag "c8fb91b9b049f1936f521e990684054b"`, while the `.md` twin carries no `Last-Modified` and is byte-identical to 08:13Z — the pattern S021 already recorded ("byte-identical … while the HTML Last-Modified moved"). I did not diff HTML versions (no earlier HTML bytes kept).
- Redirects still hold: `developers.openai.com/codex/skills` → `308` → `learn.chatgpt.com/docs/build-skills`, and the `.md` variant → `308` → `learn.chatgpt.com/docs/build-skills.md` (`curl -o /dev/null -D -`, 2026-10-22T21:16Z).

## 8. Served page versus docs source

The site serves `.md` twins as its ingestible source ("Each page has a Markdown twin at `/docs/<slug>.md`", docs map `llms.txt:5`). The rendered HTML of the same page contains my quoted sentence exactly once (`grep -c '8,000 characters when the context window is unknown' page.html` → `1`), so the served page and the served source agree on the counted quote. I could not compare against a public docs *repository*: `learn.chatgpt.com/sitemap.xml` → 404, and `api.github.com/repos/openai/codex/contents/docs` → 403 (unauthenticated rate limit), so the docs tree I used is the site's own `llms.txt` map, which lists exactly five skill pages: `build-skills`, `customization/overview`, `enterprise/skills`, `skills-and-plugins`, `extend/record-and-replay`. Four of those are swept above; all four return no number about description length or a listing budget (grep for `description|character|token|budget|truncat|shorten|limit|maximum|[0-9]+%`). This is a bounded statement about the five pages in the map, not a claim that Codex documents nothing anywhere.

## 9. Verification run (sandbox only)

Fixture: the clone at `7ad05d34` plus (a) the table row above appended to `SKILL.md` under a `### Description thresholds by client` heading, (b) a probe `corpus/knowledge/skill-listing-thresholds-round54.md` with a `## Per-client record` table holding my entry row, (c) a probe `corpus/lessons/round-54.md` with a `## Gate` table holding both Gate rows, (d) the two SOURCES rows appended.

```
python3 -B verifiers/check_description_thresholds.py --root . --json
  Codex: {"row": "S054", "url": "https://learn.chatgpt.com/docs/build-skills",
          "quote": "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown",
          "tokens": ["2%", "8,000", "10,000"], "backed": true, "why": []}
  other six clients: "SKILL.md rows naming client: 0 (need 1)" and "entry rows naming client: 0 (need 1)"
  printed line "description thresholds backed 1 of 7 clients", exit 1 (TARGET 4; a single-client world cannot reach it)

python3 -B verifiers/check_description_thresholds.py --root . --fetch --json
  "description thresholds backed 1 of 7 clients"
  "description thresholds found on the live page 1 of 1"   exit 1
  Codex: backed true, found true, no fetch_error — the quote is present on the live page after the counter's normalisation
```

Registry shape on the fixture (`SOURCES.md` contract census commands, run from the clone root):

```
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md      -> 53
awk -F'|' '/^\|…S[0-9][0-9][0-9]+…/ && NF!=13 {n++} END{print n+0}'       -> 0
awk duplicate-id check                                                     -> (no output)
grep -c '^| S' corpus/SOURCES.md                                           -> 54
```

53 versus 54 is the S054b problem, stated next.

## 10. Notes and conflicts for the L1

1. **`S054b` is not a contract-conformant id and is invisible to every reader.** `CORPUS.md` § SOURCES.md — Shape: "`id` — `S` + 3 or more digits". The census regexes, the two counters' row pattern (a pipe, spaces, `S`, three or more digits, spaces, a pipe) and the Gate reader's id pattern (an optional backtick, `S`, three or more digits, an optional backtick) all stop at the `b`: the fixture above counts 53 census rows against 54 literal `S` lines, and a `| S054b |` Gate row's quote is never indexed. Renumber S054b to the next free numeric id (the highest id at the tip is S052) before it goes live; the row's content needs no change.
2. **This page is already held twice and the counted sentence is already recorded in a Gate.** S013 (`queued`, opened 2026-10-21) and S021 (`mined`, opened 2026-10-22, used-by `frontmatter-rule-authorities-round48.md` and `skill-overlap-levers-round51.md`) are both this page, and S021 already teaches "at most 2% … or 8,000 characters … `skills.max_context_tokens` overrides it (up to 10,000 tokens)". The round-47 Gate (`corpus/lessons/round-47.md:36`) already holds my exact quote for S013. So the Codex *number* is not new learning, and the C1 sizing critic's finding 2 (`CriticC1Sizing.md` § 2) already showed Codex is reachable from S021 with the round-48 quote. What S054 adds is a round-54 row for a round-54 claim; what is genuinely new in this seat's material is the config-reference page (no row existed for it — `grep -n 'config-reference' corpus/SOURCES.md` → no row) and the exact `10000`-token cap wording.
3. **Contract-conforming alternative, if the L1 prefers no third row on one page:** cite S021 in the entry instead (opened `2026-10-22`, tier A, `mined`, 11 cells), append `corpus/knowledge/skill-listing-thresholds-round54.md` to its `used-by` in place (contract rule 2 permits `used-by` in place with an old→new log in the lesson), and record the S021 Gate row in `corpus/lessons/round-54.md` with my quote. Verified in the sandbox world `.scratch/world-s021` (entry row switched to `S021`, the entry path appended to S021's `used-by`, Gate row under `S021`, no S054 rows): `python3 -B verifiers/check_description_thresholds.py --root .scratch/world-s021 --json` → Codex `backed: true`, `row: "S021"`, `why: []`, printed `description thresholds backed 1 of 7 clients`, exit 1 (target). S013 cannot serve because it is `queued` and opened 2026-10-21.
4. **The entry's Codex `row` cell must stay `S054` alone** — the counter demands one `S###` there, and S054b will not parse.
5. No lane file other than this report was written by this seat; no git write and no jj command was issued in the lane (all git writes ran inside the sandbox clone). Read-only check at the end: `git --no-optional-locks status --porcelain` in the lane → ` M corpus/README.md` and `?? .ufo/waves/round-54/`, exit 0; the `corpus/README.md` modification is another seat's (this seat did not open it for writing, and its content is not part of this report).

## 11. Limits of this record

- Documentation only: I did not read Codex's shipped source, so I cannot say what the binary does past the budget; the page's shorten/omit/warn sequence is the vendor's statement, not a measurement.
- The 2% figure is a share of a context window whose size this page never names, and the page does not say how the 8,000-character fallback is chosen when a window's size is unknown to the loader; [INFERENCE] the fallback is a character count used because no window size is available, but the page states the fallback without saying how it is detected.
- I did not diff the HTML page against any earlier HTML capture, so the `Last-Modified` move is recorded as an observation, not as a content change.
- The docs-tree sweep covers the five pages in `llms.txt` plus the config reference; pages outside that map (changelog and release notes pages were not fetched) were not opened, so no negative statement is made about them.
