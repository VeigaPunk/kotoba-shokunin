Result: MIXED — the S044 anchor (200, 9,149 B, sha256 `9d1f87a2…`) and all four locations the SOURCES row cites hold verbatim, but the knowledge entry misattributes the fallback default `[]` to lines that never state it and asserts a `CLAUDE.md` negative on a page with zero occurrences of `CLAUDE`, whose real support (`config-sample.md:286`) carries no SOURCES row.

# W2ReopenS044 — SOURCES row S044 (OpenAI Codex AGENTS.md guide), round-53 falsify

Judged revision: `c775d6823bfca8f0de8c0874032a954438b38edc` (read-only; no lane writes except this file).
`git rev-parse HEAD` = `c775d6823bfca8f0de8c0874032a954438b38edc`. The two audited lines are byte-identical
between HEAD and the working tree: `git show HEAD:corpus/SOURCES.md` line 57 sha256
`8fc4bf1e61fe0be04cfeef8ef6e675d5070e4ed46b109e54bdb413de13c053c8`, and
`git show HEAD:corpus/knowledge/alwayson-rule-files-round53.md` line 26 sha256
`17812658b8f520b016b39f7dc2c7e8d066af8703cbdb7852ffd72f38c452c548`; both match the working-tree lines, so
the verdicts apply to the judged revision and to the tree the L1 edits.
Seat: leaf scout, no dispatch. No LSP server answers a web markdown page, so line evidence below is a
numbered dump of the fetched bytes (text tooling is the only available form; recorded, not presented as
semantic proof).

## Fetch receipts (all ordinary curl, no browser)

| what | URL | UTC access | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| S044 primary (re-open) | https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | 2026-10-22T20:36:38Z | 200 | 9,149 | `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e` |
| route (row's anchor) | https://developers.openai.com/codex/guides/agents-md.md | 2026-10-22T20:37:10Z | 308, 15 B, `Location: https://learn.chatgpt.com/docs/agent-configuration/agents-md.md` | — | — |
| route, no-`.md` variant | https://developers.openai.com/codex/guides/agents-md | 2026-10-22T20:37:10Z | 308 → `https://learn.chatgpt.com/docs/agent-configuration/agents-md` | — | — |
| pinned pointer named in the anchor | https://raw.githubusercontent.com/openai/codex/8eaf5fd115f036d207be236009938261758e30f2/docs/agents_md.md | 2026-10-22T20:37:10Z | 200 | 126 | `56f5b6026b15fad40fe8b1f6f8910b9fccdf66da3b39dd943c91877e2299619e` |
| default-`[]` support page (not rowed) | https://learn.chatgpt.com/docs/config-file/config-sample.md | 2026-10-22T20:38:09Z | 200 | 34,474 | `626f16aed15a7c4906b5cfee22ec6f04d38fd5455f358a03b5f30342cf505d44` |

Primary response headers: `content-type: text/markdown; charset=utf-8`, `server: Vercel`,
`x-vercel-cache: MISS`, `age: 0`; the body is 218 lines. Curl exit 0, `http_code=200 size_download=9149`.

## Anchor cell — HOLDS

Row (corpus/SOURCES.md:57) anchor cell: "fetched 2026-10-22T20:08:31Z (200, 9,149 B, sha256
`9d1f87a2…`)". My 20:36:38Z refetch is byte-identical: 200, 9,149 B, sha256
`9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e`. The full sha starts with the row's
abbreviated `9d1f87a2…`, the byte count matches exactly, and the page did not change between the two
measurements (cache MISS, `age: 0`). The round-53 lesson Gate row (corpus/lessons/round-53.md:24) repeats
the same 20:08:31Z / 9,149 B / `9d1f87a2…` receipt and a quote that is verbatim at `agents-md.md:12`:
"In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any
fallback names in `project_doc_fallback_filenames`." (18 words). HOLDS.

Route claim: "route `https://developers.openai.com/codex/guides/agents-md.md` → 308 → this URL". Verified:
the request returns HTTP 308 with that exact `Location`. HOLDS. Precision note D4 below.

## SOURCES row, per cited location — all HOLD

| cited | what the row says it carries | observed at the numbered lines | verdict |
|---|---|---|---|
| `agents-md.md:9-15` | § How Codex discovers guidance — per-directory filename order, one file, size stop | `:9` "Discovery follows this precedence order:"; `:11` "Codex uses only the first non-empty file at this level."; `:12` "In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`." and "Codex includes at most one file per directory." (18 and 7 words) | HOLDS (section heading is `:7`; the cited range is the section's content) |
| `:47` | § Create global guidance — the global override lever | `:47` "Use `~/.codex/AGENTS.override.md` when you need a temporary global override without deleting the base file." (16 words) | HOLDS (line is inside § Create global guidance, heading `:17`; `:47` is not the heading) |
| `:145-159` | § Customize fallback filenames — fallback-name list, ignored names | `:147` "add it to the fallback list so Codex treats it like an instructions file"; `:153` `project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]`; `:159` "Filenames not on this list are ignored for instruction discovery." (10 words) and "Now Codex checks each directory in this order: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`." (12 words) | HOLDS |
| `:210-213` | § Troubleshoot discovery issues — the four bullets | `:210` nothing loads / empty ignored; `:211` override higher in tree; `:212` fallback names without typos; `:213` "Raise `project_doc_max_bytes` or split large files across nested directories to keep critical guidance intact." (16 words) | HOLDS (heading `:208`; cited range is exactly the bullets) |

Row's teaches sentence — HOLDS against `:12` (order, at most one file), `:159` (ignored names), `:15`
"Codex skips empty files and stops adding files once the combined size reaches the limit defined by
`project_doc_max_bytes` (32 KiB by default)." (21 words). Two bounded-summary notes, not breaks: the page
stops adding whole files (it does not say it truncates a file's text), and the walk is project root down
to the cwd, with "only checks the current directory" when no project root exists (`:12`); the row's "from
the project root down" compresses both. Severity Low (wording only; no cited line contradicted).

## Knowledge entry, per cited location — two BREAKS

Row checked: corpus/knowledge/alwayson-rule-files-round53.md:26 (the OpenAI Codex row of § Per-client
record). Header line 1 cites `agents-md.md:9-15, 145-159`.

| cited | what the knowledge says it carries | observed | verdict |
|---|---|---|---|
| `:12, 145-159` (names-read column) | `AGENTS.override.md`, then `AGENTS.md`, then `project_doc_fallback_filenames` | Exactly the `:12` order sentence above | HOLDS |
| `:12, 145-159` (parenthetical) | `project_doc_fallback_filenames` "(default `[]`)" | The page never states a default value for this key. `grep -i default` over the body hits only `:11` (`~/.codex`), `:19`, `:51`, `:212`, `:214`; `:12` says only "any fallback names in `project_doc_fallback_filenames`" and `:145-159` shows a non-empty example list with no default | **BREAK** — the cited lines do not say it (defect D1) |
| `:12` (both-files column) | "Codex includes at most one file per directory" | Verbatim at `:12` | HOLDS |
| no line cited (both-files column) | "`CLAUDE.md` is not read unless configured as a fallback name" | `grep -c 'CLAUDE'` on the body = 0 and `grep -c 'GEMINI'` = 0; the page never names `CLAUDE.md`. The conclusion needs `:159` (names not on the list are ignored) **and** the empty default from another page; neither is cited on the cell | **BREAK (attribution)** — S044 is silent on `CLAUDE.md` (defect D2) |
| `:15` (§6, size) | "Codex: 32 KiB combined by default (S044 `:15`)" | `:15` quote above, verbatim | HOLDS |
| `ScribeCodex.md` § 4 (redirect column) | "no `@` import (0 hits over 191 pages)" | ScribeCodex.md:132 (inside § 4, heading `:126`) records the 191-page full-text grep with `@AGENTS`/`@import` → 0 hits; my body has no import expansion and `grep -i 'symlink\|symbolic'` returns rc 1 (no hits) | HOLDS |

The `@`-import negative is properly swept (ScribeCodex § 4 carries the docs leg, the loader code leg
`agents_md.rs:150-169`, and the lane-corpus leg). The `CLAUDE.md` negative is true — I confirmed the
supporting fact myself: config-sample.md `:286` reads "Ordered fallbacks when AGENTS.md is missing at a
directory level. Default: []" (11 words), fetched 2026-10-22T20:38:09Z, 200, 34,474 B, sha256
`626f16ae…`. It is the citation, not the fact, that fails.

## Defects (severity, owner: L1 fixes)

- **D1 — knowledge line 26, misattributed default. Severity Low.** "(default `[]`)" is cited to
  `agents-md.md:12, 145-159`; those lines are silent on the default. The statement is true and traceable
  to config-sample.md:286 (verified above), but a reader following the citation lands on a page that
  cannot support it. Fix: cite the config-sample line (needs D3) or drop the parenthetical from the S044
  citation.
- **D2 — knowledge line 26, uncited client negative. Severity Medium.** "`CLAUDE.md` is not read unless
  configured as a fallback name" is attributed to S044, which has zero occurrences of `CLAUDE`. The
  nearest support in the same page is `:159` ("Filenames not on this list are ignored for instruction
  discovery."), which is inside the entry's own cited range but not attached to this clause, plus the
  empty default from config-sample. Q30 (round-52 `corpus/QUALITY.md:41`) exists for exactly this class:
  a client negative must name its three legs or be recorded unverified. The fact is corroborated, so no
  downstream claim is false; the admitted record is not verifiable from what it cites.
- **D3 — no SOURCES row for config-sample.md. Severity Low (coverage).** The page that supplies both the
  32 KiB numeric default's companion and the fallback `[]` default was opened this round (ScribeCodex.md
  Gate record `:168-182`, full receipt 200 / 34,474 B / `626f16ae…`), ScribeCodex drafted a row for it
  (ScribeCodex.md:145), and it did not land: `grep -c "config-sample\|Configuration sample"`
  corpus/SOURCES.md → 0 (rc 1), and the lesson Gate table (corpus/lessons/round-53.md:20-28) admits only
  S043–S051 (the `S051` slot went to the opencode release diff). Plan § Frontier says "rows for every
  always-on source opened this round"; this one underwrites the Codex default and is rowless.
- **D4 — anchor route wording, one hop loose. Severity Low (cosmetic).** "the path `docs/agents_md.md:3`
  names" — the pinned pointer's line 3 reads "For information about AGENTS.md, see [this
  documentation](https://developers.openai.com/codex/guides/agents-md)" (9 words), i.e. the `.md`-less
  URL, which 308s to the `.md`-less learn URL, not to the fetched `.md` URL. The row's `.md` route is a
  separate 308 to the fetched URL. Provenance is real; the sentence overstates the pointer by one hop.

## Positive checks (no defect)

- The landed S044 row (corpus/SOURCES.md:57) is cell-for-cell identical to ScribeCodex's drafted row
  (ScribeCodex.md:144) except the id `S0xx` → `S044`: a pipe-split comparison over 11 cells shows one
  differing column (`id`). No transcription drift between seat draft and registry.
- The lesson Gate row (round-53.md:24) matches the live fetch on URL, UTC, bytes and sha, and its quote
  is verbatim at `:12`.
- Every quote ScribeCodex's Gate record attributes to this page for the Codex cells (`:11`, `:12`, `:13`,
  `:15`, `:47`, `:147`, `:159`) reads the same in my fetch; none of them is a paraphrase presented as
  verbatim.
- Row columns are consistent with the header (`| id | source | kind | tier | scope | anchor | teaches |
  status | opened | recheck | used-by |`): 11 cells, kind `docs`, tier `A`, status `mined`, recheck
  `90d`, used-by names the knowledge entry that cites it.

## Verdicts per cited line (summary)

- SOURCES row `:9-15` — HOLDS.
- SOURCES row `:47` — HOLDS.
- SOURCES row `:145-159` — HOLDS.
- SOURCES row `:210-213` — HOLDS.
- SOURCES anchor (bytes/sha/status) — HOLDS; route — HOLDS (D4 wording).
- Knowledge `:12, 145-159` order — HOLDS; "(default `[]`)" — BREAKS (D1).
- Knowledge `:12` one-file quote — HOLDS.
- Knowledge `CLAUDE.md` negative — BREAKS as attribution (D2).
- Knowledge `:15` 32 KiB — HOLDS.
- Knowledge `@`-import sweep — HOLDS.

## Remaining unknowns / limits

- The 20:08:31Z timestamp is another seat's clock; I cannot re-measure it. Identical bytes and sha at
  20:36:38Z show the content is unchanged between the two receipts, which is the property the anchor
  needs.
- Whether the C2 instrument's `alwayson.07` or `alwayson.04` boxes actually consume S044's statements is
  outside this seat (instrument review is other seats' assignment); I only verified the source text.
- config-sample.md:286's "Default: []" is verified by my own fetch, but I did not audit the other
  config-sample claims (e.g. `project_doc_max_bytes` `:282`, "Default: 32768"), since S044 does not cite
  them.

## Bounds and tooling receipt

No installs or upgrades (nothing needed). No model calls. No git or jj commands anywhere. No writes in the
lane except this report; fetch artifacts live under `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReopenS044/`
(`s044.body`, `s044.hdr`, `dev.hdr`, `ptr.md`, `cs.body`). No browser, no challenge bypass. Commands and
exit codes: primary curl exit 0 (`http_code=200 size_download=9149`); route curls exit 0 (`code=308`);
pointer curl exit 0 (`code=200 size=126`); config-sample curl exit 0 (`code=200 size=34474`); `grep -c`
on `CLAUDE`/`GEMINI` = 0/0, `grep -i symlink` rc 1; `grep -c "config-sample"` corpus/SOURCES.md rc 1 (no
match).
