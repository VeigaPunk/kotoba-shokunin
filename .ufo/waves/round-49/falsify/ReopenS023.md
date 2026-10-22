# Falsify — re-open S023 (Claude Agent Skills overview) and S018 (Agent Skills spec)

**Verdict: HOLDS-BOUNDED** — applies to row S023's `.md` pin (bytes, sha256, every anchor line), its
Gate quote and the census entry's two quotes, the nine negative sweeps, the S018 re-open (7,608 B,
`9a67de89…`, quote at `specification.md:102`, overlap sweep), and the C1 census↔`PROVINCE.md`
§ Adjacent join. Bounded on two points: the row's HTML-route byte/sha cell is not a reproducible
pin (F1), and the Gate quote grounds only half of S023's `teaches` (F2).

## Findings

- **F1 (bounded, evidence hygiene).** The S023 row records the HTML route as
  "200, 557288 B, sha256 `0c1d8f68…`". That cell cannot be reproduced: two fetches of the same
  route, same UA, minutes apart, gave 557,341 B / `2bece998…` (11:25:54Z) and 557,317 B /
  `a3b03efd…` (11:27Z). The route returns no `Content-Length` and no `Last-Modified`
  (`cache-control: private, no-cache, no-store`), so the shell is regenerated per request. Both
  fetches still carry both quoted sentences twice, so the row's assertion "carries the same
  sentences inside a client app shell" is true; only the byte/hash cell is unpinnable. The seat
  report's own F5 says the `.md` route is "the reproducible, quotable artifact and the hash
  recorded on the row" — the row then records the unreproducible HTML hash unqualified. S022 has
  the identical defect (1233129 B, `10219534…`), so this is lane-wide, not S023-only. Fix: drop the
  HTML hash, or mark the HTML observation time-local; keep the `.md` pin.
- **F2 (bounded, contract rule 1).** `CORPUS.md:112-115` requires the Gate to record "a ≤25-word
  quote with its location grounding `teaches`". The Gate's S023 quote ("Claude loads this metadata
  at startup and includes it in the system prompt.", 13 words, `overview.md:59`) grounds only the
  loading half. The half the C1 census actually rests on — the description as the matching input —
  sits eight words later on the same line and is quoted in the census entry (14 words), not in the
  Gate. The pair would still fit the 25-word cap; append it to the Gate row.
- **F3 (holds).** `.md` pin reproduced exactly: 200, 21,840 B, sha256
  `7913d4556c014c6bf7f23e186efded1b36da63d7b29d73898267ebe8d2f6258f`, two fetches byte-identical
  (`cmp` clean), and equal to the round-48 record at `.ufo/waves/round-48/build/C2ClaudeDocs.md:103`
  — the row's "byte-identical to the round-48 fetch" is grounded, not asserted.
- **F4 (holds).** Anchors resolve in the fetched bytes: `:48` = `### Level 1: Metadata (always
  loaded)`; `:59` carries both quoted sentences verbatim; `:82` = "When you request something that
  matches a Skill's description, Claude reads `SKILL.md` from the filesystem using bash." (inside
  § Level 2, whose heading is at `:61`); `:106` = the Level-1 row of the § How Skills work table.
  Nit: the Level-1 cell names the heading line (48) plus "text at :59", the Level-2 cell names a
  body line (82) and never the heading (61) — two conventions in one cell. Not an error.
- **F5 (holds).** Nine negative sweeps re-run on the fetched `.md`, 0 each, case-insensitive and
  case-sensitive: `tie[- ]break`, `overlap`, `ambigu`, `multiple skills`, `one skill`, `arbitrat`,
  `conflict`, `both skills`, `select`. Positive controls on the same file: `trigger` 4,
  `description` 9, `context` 12, so the zeros are not an empty-file artefact. Wider probes for a
  tie-break rule also 0: `priorit`, `choose`, `which Skill`, `routing`, `rank`, `best match`,
  `if multiple`, `more than one`, `competing`, `decid`. The row's "the page states no rule for
  choosing between overlapping descriptions" survives a pattern set three times wider than the
  nine it reports.
- **F6 (holds).** `teaches`'s paraphrase is the page's own sentence, not an overreach: line 59 ends
  "until a Skill is triggered, only its name and description occupy context", and the level table
  at `:106` gives Level 1 content as "`name` and `description` from YAML frontmatter". The
  row's "description decides whether a skill applies" is a paraphrase — the page's word is
  "determining whether to trigger" (`decid` counts 0 in the file) — but a fair one, and S022 makes
  the same move.
- **F7 (holds).** S018 re-open: 200, 7,608 B, sha256
  `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` = the row's `9a67de89…`;
  the quote "Should describe both what the skill does and when to use it" is verbatim at
  `specification.md:102` as the second bullet under "The required `description` field:", 12 words.
  The entry's overlap sweep
  `grep -cinE 'overlap|ambiguit|precedence|disambiguat|tie[- ]?break|arbitrat|multiple skills'` → 0
  (also 0 without `-i`). Wider probes surface only unrelated senses: `conflict` 1 (`:162`, "unique
  key names to avoid accidental conflicts"), `decid` 1 (`:195`, "once it's decided to activate a
  skill") — neither states a rule between overlapping skills, so the negative claim stands within
  its declared pattern set. The row's pinned-source anchors also resolve: `docs/specification.mdx`
  at `69ef37e9` line 27 = the frontmatter `name` row, 61-65 = the five `name` bullets, 94 = "Must be
  1-1024 characters", 224 = "Keep your main `SKILL.md` under 500 lines".
- **F8 (holds, append-only).** S018 at `a5adc146` versus the judged tree differs in exactly one
  field, `used-by` (adds `corpus/knowledge/sibling-overlap-census-round49.md`); `status`, `recheck`
  and `opened` are untouched and the change is logged old→new. S022/S023 are appended, and
  `grep -c '^| S0'` → 23, matching the Gate's "Rows 21 → 23".
- **F9 (holds, C1 join).** The census table carries 20 lane rows and `PROVINCE.md` § Adjacent 20
  (lines 37-56); the lane/classification/commit triples are identical across the two files
  (`diff` exit 0). `check_sibling_census.py … --province PROVINCE.md` → "rows 20 verified 20",
  "province rows 20 matched 20", exit 0. `scripts/sources-census.sh validate --root … kotoba` →
  exit 0, `kotoba ok`, three W04 duplicate-URL warnings (S018/S019/S021) — exactly the LOG's
  "three W04 warnings both times", and W04 is by design the superseded-URL pair, not a row fault.

## Evidence (commands, verbatim exit codes)

All web fetches in `/fast/scratch/hyaku/kotoba-r49/falsify/ReopenS023/`; none of them installed or
upgraded anything.

- `curl … overview.md` → `md_route http=200 bytes=21840`; `sha256sum` →
  `7913d4556c014c6bf7f23e186efded1b36da63d7b29d73898267ebe8d2f6258f`; `wc -l` → 338; repeat fetch
  `cmp` → identical; `curl -I` → `content-length: 21840`, `content-type: text/markdown`.
- `curl … overview` (HTML) ×3 → 557,288 B `0c1d8f68…` (seat, 09:38:50Z, from
  `.ufo/waves/round-49/build/SrcAgentSkillsOverview.md:104-105`), 557,341 B `2bece998…`, 557,317 B
  `a3b03efd…` (mine); `curl -I` → no `content-length`, no `last-modified`.
- `grep -coF '<quote>' s023.html` → 2 for each quoted sentence.
- Nine sweeps loop over `s023.md`: all `-i=0 case=0`; broader probe loop: all 0 except `match.*Skill`
  4; `grep -ci` controls `trigger=4 description=9 context=12`.
- `grep -nF 'Should describe both…' s018.md` → `102:`; `sha256sum s018.md` →
  `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`; `wc -c` → 7608; overlap sweep
  → `0`, exit 1 (grep no-match).
- `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md
  --province PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20`, exit 0.
- `./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → three W04
  lines and `kotoba ok …/corpus/SOURCES.md`, exit 0.
- `git -C … show a5adc146:corpus/SOURCES.md` vs tip, S018 row split on `|` → one differing field
  (`used-by`), diff exit 1.

## Web sources opened (UTC 2026-10-22, this seat)

| URL | access | bytes | sha256 | located quote (≤25 words) |
|---|---|---|---|---|
| https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md | 11:25:54Z, 11:27:06Z | 21,840 | `7913d455…f6258f` | "Claude loads this metadata at startup and includes it in the system prompt." (`overview.md:59`) |
| https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | 11:25:54Z, 11:27Z | 557,341 / 557,317 | `2bece998…` / `a3b03efd…` | same sentence present twice; bytes vary per request |
| https://agentskills.io/specification.md | 11:26Z | 7,608 | `9a67de8913…de16` | "Should describe both what the skill does and when to use it" (`specification.md:102`) |
| https://raw.githubusercontent.com/agentskills/agentskills/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx | 11:26Z | 7,166 | `b9079c0c…29b220` | "Lowercase letters, numbers, and hyphens only." (`specification.mdx:27`) |

## Unknowns left open

- Whether the fleet intends the HTML-route hash to be a pin at all: S021's row instead tracks the
  HTML route by its `Last-Modified` header, which this route does not serve, so no stable HTML
  anchor exists here.
- Whether any later round would re-check the HTML cell; if none does, F1 is cosmetic rather than a
  routing defect — but it is presented in the same "fetch (200, N B, sha256 …)" form as the pins.
