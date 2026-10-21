verdict: HOLDS — attacked the round-47 S001 anchor-label defect ("§ Skill metadata table" names no heading) and the "open spec says nothing about XML/angle brackets in description" claim against a fresh fetch at 7ad7fad; both reproduce, and the anchor defect is a birth defect rather than drift, with one measurement-scope trap and two nits confined to unlanded recommendations.

# W2S001Anchor — S001 re-open (`agentskills.io/specification`)

Row under attack: `corpus/SOURCES.md:14`. Lesson claim: `corpus/lessons/round-47.md:46-47`
("S001 content still holds, but its anchor label '§ Skill metadata table' names no heading on
the live page"). Build evidence: `.ufo/waves/round-47/build/SrcS001.md:1,22-23,46-49,83`.
Base: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (lane root HEAD; scratch clone detached
there; `git show 7ad7fad:corpus/SOURCES.md | sed -n 14p` hashes identically to the working
tree line, `1f3c744a…`).

## 1. F1 — "§ Skill metadata table" names no heading: HOLDS (stronger than recorded)

Fresh fetch, 2026-10-21T16:54:45Z: HTTP 200, 459866 B, sha256
`3d4955d339d6a160a853187a0428c0c004ecf34a5762bda11c3903f707119e57` — **byte-identical to
the build report's recorded value** (`SrcS001.md:11` table), same `etag:
W/"j06n6swtos9ur8"` and `x-served-version: dpl_8AUWT8nFRmT7D3RgoEGEPVymfFQP` as the HEAD
request at 16:56:13Z.

Heading enumeration (independent of the build report's method):

- live HTML, all `<h1>…<h6>` → 22 headings, none containing "skill metadata"; the only
  metadata heading is `metadata field` (h4, `id="metadata-field"`, `specification.md:156`).
- `.md` endpoint → 18 headings (`# Specification` … `## Validation`), none metadata-named
  except `#### metadata field`.
- TOC anchor ids → `metadata-field` only; no `skill-metadata*` slug.
- literal `Skill metadata` in raw HTML → **0**; `skill-metadata` → **0**.
- tables on the page → **1** (the Frontmatter field table), `<caption>` → 0, no aria-label
  naming it.

Charitable reading: the label can only intend the Frontmatter field table, which is a real
target at `## SKILL.md format › ### Frontmatter` (`.md:26-34`). But the contract requires
"exact section / heading / page / line" (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:32-33`),
and no heading, caption, slug, or TOC entry carries that name. The defect is real and
navigational, not a content misstatement — exactly how the lesson describes it.

**Strengthening the lesson does not state:** the 2026-10-16 Wayback raw capture
(`20261016083235id_`, `--compressed`, 446824 B, sha256 `05fce2d2…`, = the build report's
wb.html hash) renders to the *same* 7272-char text, sha256 `5ae3a105…`, `difflib` non-equal
opcodes **0**, and has the same 22 headings — no metadata-named heading on 10-16 either.
The row was written 2026-10-19 `[INFERENCE]` between two identical endpoints, so the label
was wrong at birth (the M22 class), not renamed by drift. The lesson only says the heading is
absent "on the live page"; that understates it.

## 2. F2 — spec says nothing about XML / angle brackets in description: HOLDS

Rendered live text (script/style stripped, tags→space, entities unescaped, whitespace
collapsed): 7272 chars, sha256 `5ae3a105…`. Counts: `xml` case-insensitive **0**,
`\btags?\b` **0**, `angle bracket` **0**. `.md` endpoint: `grep -inE 'xml|tag\b|tags\b|angle'`
→ exit **1** (no matches). The `description` section (`.md:97-115`) has exactly three bullets
— length (`Must be 1-1024 characters`), what+when, keywords — and the frontmatter table row
(`.md:31`) adds only `Max 1024 characters. Non-empty.` A sweep for `character|markup|special|escape`
returns only length limits and the `name` charset (`.md:30,31,33,63,64,101,134`); the
`compatibility` field (`.md:130-155`) has no character rule either. So the build report's
negative half for C2 (`SrcS001.md:42`, `SrcS001.md:1`) is confirmed on the whole page,
not just the description block.

**Measurement-scope counterexample (repro below):** the 0 is true of *rendered/reader* text
only. `grep -oi xml` on the raw HTML returns **103**, and `\btags?\b` returns **2**. All 103
are markup or site chrome (`<svg xmlns=…>` ×96, `sitemap.xml`, `browserconfig.xml`,
`application/xml`, and the upload widget's `accept` list `.txt,.yaml,.yml,.xml,.sql`); the 2
`tag` hits are Next.js flight data for the sidebar tag names "For skill creators"/"For client
implementors". The build report measured the rendered text and `.md`, so its 0 is correct;
a future rechecker that greps the wire bytes will false-alarm — the same class as its own
mojibake counterexample (`SrcS001.md:87`).

## 3. F3 — freshness of the fetch record: HOLDS

Same URL, an hour after the build seat, returns the identical HTML hash, size, etag and
deployment id — the report's fetch record is reproducible, not a one-off capture. The `.md`
drift is real and its old hash is grounded: `.ufo/round-46/evidence/w2/sources/fetch-log.json`
rows[0] records `4c649bdf…` at `2026-10-19T18:40:53Z` with `quote_location` "spec.md line
251"; today the same sentence sits at `specification.md:237` in a 260-line file — a **14-line
shift above the quote**. Because the 10-16 and 10-21 rendered page texts are byte-identical,
`[INFERENCE]` the 14 lines were reader-shell/preamble (Documentation-Index block or blank
lines), not body content; the report's "cause cannot be located at byte level" is true at
byte level and this narrows it to a region that cannot change page text.

No gate consumes the hash: `grep -rn "fetch-log" verifiers/ scripts/` → no hits (exit 1);
`grep -rn "4c649bdf\|9a67de89"` outside `.ufo/` → only `corpus/lessons/round-46.md:63`.
So the drift breaks no gate today (`SrcS001.md:32` holds).

## 4. F4 — two nits, both in unlanded recommendations (not landed defects)

The lesson applied **none** of the build report's row deltas — `corpus/SOURCES.md:14` is
unchanged (`used-by: SKILL.md`, `recheck: on-release`, `opened: 2026-10-19`) and
`corpus/lessons/round-47.md:30-31` says "no existing row's `status`, `recheck` or `used-by`
changed (old→new: none)". That is contract-conformant. Two of the *recommendations* are not:

1. `SrcS001.md:63` recommends changing `opened` 2026-10-19 → 2026-10-21 in place. Rule 2
   (`SOURCES-CONTRACT-v1.md:49`) permits in-place change of `status`, `recheck`, `used-by`
   only. Applying the delta table as written would breach the contract; the lesson correctly
   ignored it.
2. `SrcS001.md:65` recommends `used-by` → `SKILL.md; verifiers/verify_skill_checklist.py`.
   The column is defined as "repo-relative paths of the knowledge entries or lessons citing
   the row" (`SOURCES-CONTRACT-v1.md:40`), and all 15 landed cells are `SKILL.md` or
   `corpus/knowledge/*` — none is a verifier. The verifier does cite S001
   (`verifiers/verify_skill_checklist.py:103,1307`), but that citation does not belong in
   this column.

The `recheck: on-release → 90d` recommendation (`SrcS001.md:64`) is sound: `on-release` is
contract-legal but undated, `E09` accepts it via `symbolic()` (`scripts/sources-census.sh:582,665`)
and `overdue` reports it as `cadence … recheck=on-release` with `due=INVALID_EPOCH`
(`:676-682`) — the report's description of the consequence is accurate.

## 5. F5 — the deferred remedy is executable (executed, not reasoned)

The lesson defers the correction: "a superseding row waits for the next round that cites
S001" (`corpus/lessons/round-47.md:46-49`). I tested the mechanism on `/tmp` fixture
registries with the fleet census (target dir resolution uses `dirname(file)/..`, so the
fixture lives at `<tmp>/corpus/SOURCES.md` with `SKILL.md`/`knowledge` symlinks):

| fixture | result | exit |
|---|---|---|
| unmutated clone | `ok` | 0 |
| S016, same URL **and scope**, `teaches` contains `supersedes S001`, inside `## Registry` | `ok` | 0 |
| same-scope duplicate without the `supersedes S001` phrase | `E04` | 1 |
| S016 appended after `## Paths` | `E12` | 1 |

This matches the code (`scripts/sources-census.sh:648-649` exempts a duplicate URL+scope only
when `teaches ~ /supersedes S[0-9]{3}/`; `:621` rejects a row outside the Registry). So the
lesson's plan is mechanically supported and the census will accept the replacement row, but
only inside the table and only with the literal supersedes phrase in `teaches`.

## 6. Commands run (exit codes)

1. canonical scratch clone + `git checkout --detach 7ad7fad` → 0; `rev-parse HEAD` = 7ad7fad.
2. `curl -sSL -w … https://agentskills.io/specification -o spec.html` → 0; `HTTP=200 SIZE=459866`; `sha256sum` → `3d4955d3…`.
3. `curl … https://agentskills.io/specification.md` → 0; `MD_HTTP=200 MD_SIZE=7608`; `sha256sum` → `9a67de89…`; `wc -l` → 260; `grep -n '^#\+ '` → 18 headings.
4. python render + counts (live) → 7272 chars, `5ae3a105…`; `xml_ci 0`, `tag_word 0`, `angle_bracket 0`, `skill metadata 0` (0).
5. python `<h[1-6]>` extraction (live) → 22 headings, none matching (0).
6. `curl -sSL --compressed …/20261016083235id_/…` → 0; 446824 B on disk, `05fce2d2…`; python render → 7272 chars, `5ae3a105…`, `equal True`, `non_equal_opcodes 0`.
7. `grep -oi xml spec.html | wc -l` → 103; `grep -oiE '\btags?\b'` → 2; context extraction → markup/flight data only (0).
8. `grep -inE 'xml|tag\b|tags\b|angle' spec.md` → **1** (no matches, expected).
9. `grep -inE 'character|markup|special|escape' spec.md` → only length/charset lines (0).
10. `curl -sSI https://agentskills.io/specification` → `HTTP/2 200`, `date: Wed, 21 Oct 2026 16:56:13 GMT`, etag/deployment identical (0).
11. read `.ufo/round-46/evidence/w2/sources/fetch-log.json` via python → rows[0] `4c649bdf…`, `2026-10-19T18:40:53Z`, "spec.md line 251" (0).
12. `grep -rn "fetch-log" verifiers/ scripts/` → no hits (**1**); `grep -rn "4c649bdf\|9a67de89"` outside `.ufo/` → `corpus/lessons/round-46.md:63` only (0).
13. `scripts/sources-census.sh validate <clone> --today 2026-10-21` → `ok` (0); three fixture runs as §5 (0, 0, 1, 1).
14. `git shows/status` at lane root → HEAD 7ad7fad; only untracked wave dirs (0).

Tooling installs: **none** (no pacman, no uv/npm; no `opencode` wrapper run, no omp session).

## 7. Counterexamples with repro

1. **Raw-byte XML grep false positive.** `grep -oi xml /tmp/spec-20261021.html | wc -l` → 103;
   `grep -oiE '\btags?\b' … | wc -l` → 2. Repro contexts: 96 `<svg xmlns=…>`, `sitemap.xml`,
   `browserconfig.xml`, `application/xml`, `accept="…,.xml,.sql,…"`, and Next.js flight data
   `{"tag":"For skill creators"…}`. The claim is only valid for rendered text and the `.md`.
2. **Applying the build report's delta table in place.** Rule 2
   (`SOURCES-CONTRACT-v1.md:49`) allows in-place edits only to `status`/`recheck`/`used-by`;
   `SrcS001.md:63` recommends an `opened` edit and `SrcS001.md:65` a `used-by` value outside
   the column's definition. The lesson applied neither — the counterexample is to a reader
   who treats the recommendation as a patch.
3. **Superseding row outside the Registry.** Appending S016 after `## Paths` yields
   `E12 S016 row outside Registry section`, exit 1 — the remedy must be inserted inside the
   `## Registry` table (repro in §5).

## 8. What I did NOT check

- The `.md` bytes as served on 2026-10-19: unavailable (no Wayback capture of the `.md`
  endpoint), so the 14-line preamble explanation is `[INFERENCE]`, not observed.
- `skills-ref` (the validator the page links): whether it enforces more than page text. It is
  a different source; S001 only says it "checks that your `SKILL.md` frontmatter is valid and
  follows all naming conventions" (`.md:260`).
- Any other `agentskills.io` page, `/llms.txt`, or the linked best-practices pages.
- Lane verifiers (`verify_surfaces.py`, `check_substrate_pins.py`, `verify_skill_checklist.py`,
  corpus integrity) — not run; other falsify seats own them.
- `corpus/lessons/round-46.md` beyond its S001 hash/line record, and `corpus/SOURCES.md`
  row S002's drift control.
- The live page between 2026-10-17 and 2026-10-20 (Wayback gap).

## 9. Lane-state observation (not mine, not touched)

While I was writing this report the lane working tree showed an uncommitted modification:
`verifiers/verify_surfaces.py` (`git diff --stat` → 12 insertions, 2 deletions; mtime
2026-10-21 14:05:21 -0300), whose added comment reads "Round-47 falsify candidate
(W2DropOC2, not landed)". I did not make, revert, or commit it; my only writes are the two
files under `.ufo/waves/round-47/falsify/`. Because it is uncommitted, committed-state gates
and the fault harness are unaffected. I re-ran the one grep this could have influenced
against the committed tree: `git grep -n fetch-log 7ad7fad -- verifiers scripts` → no hits;
`git grep -n S001 7ad7fad -- verifiers/verify_skill_checklist.py` → `:103` and `:1307`, as
cited. Every other path I cite was clean in `git status`.
