# ScoutQuarantine — round 69 / wave 1 — quarantine rows S185 (Roo Code) and S172 (Junie)

Assignment: hand-check the two campaign absent-defect-register rows this round's theme (skill
name-collision precedence) touches, and the lane's S203/S206 rows that now carry quotes from the
same two pages. Question: is each register row's cited span present or absent **today**, and what
is the exact quote.

Register (read-only, never edited):
`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
(`payload-absent` = "the fabrication class": every relevant source fetched cleanly and the quote is
in none of them).

Method: live fetch 2026-10-25 (curl, `Mozilla/5.0`, scripts/styles stripped, entities decoded,
case-sensitive probe plus a case-insensitive whole-file scan), Wayback raw snapshots for history,
and DOM heading offsets to test each anchor's section claim. All work in `/tmp/q69`; no lane file,
Git index or jj state touched; no installs. Register rows are historical and are not mine to
rewrite — dispositions below are recommendations to the owner.

## Verdict table

| row | cited source | quoted span in register | literal span today | disposition |
|---|---|---|---|---|
| S185 | `https://docs.roocode.com/features/skills` | `Skill locations` | **ABSENT** | payload-absent **holds**; do not append; phrase belongs to the *Junie* page |
| S172 | `https://junie.jetbrains.com/docs/agent-skills.html` | `If a project-level and a / user-level skills share the same name, the project-level skill takes precedence and the / user-le…` | **ABSENT literally, PRESENT in substance** (16-word contiguous tail verbatim) | **falsified as a fabrication**: re-derive the quote, do not carry `payload-absent` |

Confidence: high for both (two independent evidence lines each: current bytes + dated archives).

---

## S185 — Roo Code, quote `Skill locations` → ABSENT today (verdict holds)

Register row (verbatim): `| kotoba | round6 | S185 | payload-absent |
https://docs.roocode.com/features/skills | Skill locations | cited source, companion URLs and local
artifacts were all checked; the quote is in none of them |`

- Cited URL 2026-10-25: **HTTP 301** → `https://roocodeinc.github.io/Roo-Code/features/skills/`
  (final URL, HTTP 200). The question was settled on the redirected page, i.e. what a reader
  actually sees at the cited URL.
- `Skill locations` occurs **0 times**, case-insensitive, in the whole served document
  (sha256 `fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2`, 71 129 bytes,
  `dateModified` 2026-05-15T18:04:45Z).
- The page's section headings are: `Why It Matters`, `What Skills Let You Do`, `How Skills Work`,
  `Creating Your First Skill`, `Directory Structure`, `Override Priority`, `Skill Discovery`,
  `Troubleshooting`, `Skills vs Custom Instructions vs Slash Commands`, `Skill Specification`,
  `See Also`. Nothing named "Skill locations"; the nearest real strings are the bullets
  `Roo-specific locations: .roo/skills/, ~/.roo/skills/ (higher priority)` and
  `Cross-agent locations: .agents/skills/, ~/.agents/skills/ (shared with other agent tools)`.
- History, so this is not a page that changed yesterday: **absent in all six Wayback snapshots**
  Jan–Jun 2026 (`20260101234333`, `20260115183009`, `20260117172126`, `20260221201028`,
  `20260411150854` all 200; `20260620122805` 301). The same April snapshot *does* contain
  `Override Control`, `Project skills override global skills` and `Roo-specific (higher priority)`.
- Provenance of the phrase: it **is** present on the sibling page named by S172 —
  `https://junie.jetbrains.com/docs/agent-skills.html` carries it 3× raw: the site search index
  (`"title":"Skill locations and configuration"`), an inline cross-reference
  (`Skill locations and configuration`), and the heading
  `<h2 id="skill-locations-and-configuration">Skill locations and configuration</h2>`. S185's quote
  is therefore not invented text; it is a **cross-page fragment filed under the Roo URL** (a
  citation mix-up, not a fabricated span).

Recommendation: keep S185 `payload-absent` for the Roo citation; supersede/refuse rather than
append. Do **not** repair it by substituting a different Roo span after data; the Roo rule this
round actually needs is already carried by S203 (below).

## S172 — Junie, precedence sentence → literal span ABSENT, content PRESENT (verdict falsified in substance)

Register row (verbatim): `| kotoba | round5 | S172 | payload-absent |
https://junie.jetbrains.com/docs/agent-skills.html | If a project-level and a / user-level skills
share the same name, the project-level skill takes precedence and the / user-le… | cited source,
companion URLs and local artifacts were all checked; the quote is in none of them |`

**Exact text on the page today** (section `Skill location`, h2 at raw offset 12 825; the sentence at
offset 16 092, next heading `Skill directory structure` at 16 192):

> If a project-level (`<projectRoot>/.junie/skills/<skill-name>/`) and a user-level
> (`~/.junie/skills/<skill-name>/`) skills share the same name, the project-level skill takes
> precedence and the user-level skill is ignored.

- The register's quoted string is **not** contiguous on the page: the page interleaves two inline
  `<code>` parentheticals (`(<projectRoot>/.junie/skills/<skill-name>/)` and
  `(~/.junie/skills/<skill-name>/)`). Strip them and the register's quote matches the sentence
  word-for-word — it is a **normalization of a real sentence**, not fabricated text.
- **16-word contiguous tail is verbatim present** (this is exactly the lane's S206 quote):
  `skills share the same name, the project-level skill takes precedence and the user-level skill is ignored.`
- Not a recent page edit: the identical sentence, with the same parentheticals, appears in Wayback
  `20260303165915` and `20260814181504` (both 200). A derived quote could therefore never have
  matched those folds — the row records a fold limitation, not an absent payload.
- A second, independent conflict statement exists on the page: `Check for name conflicts: if a
  project-level and a user-level skills have the same name, the user-level skill will be skipped.`
- Page freshness marker: `Last-Modified: Fri, 23 Oct 2026 18:43:22 GMT`, `ETag "6adbaaca-966d"`
  (38 509 bytes, sha256 `b3c676900e3de8a0d34754bb223685e1734c95ecc635280d8b8b159928f5a915`); the
  quote was re-confirmed against those bytes today.

Recommendation: reclassify/repair S172 to the contiguous 16-word span (or drop it) and record that
`payload-absent` here was a **fold artifact** — the fabrication reading is wrong. Do not re-append
the parenthetical-stripped sentence as a quote; it is not a located span.

---

## The lane's rows carrying these pages (freshness cross-check)

Both quotes verified against today's bytes, not against the register:

- `corpus/SOURCES.md:144` (S203) — quote
  `Project skills override global skills, mode-specific override generic`:
  **present verbatim** (8 words; page has no trailing period, and the row's quote has none).
  Anchor checks: `Override Control` (offset 28 093) sits inside section `What Skills Let You Do`
  (27 041–28 201) — true; `Choose a location` (29 906) and `Roo-specific (higher priority)`
  (30 574) are inside `Creating Your First Skill` (29 540–41 554) — true. Landing text of this
  bullet: `Override Control: Project skills override global skills, mode-specific override generic`.
  Stable in Wayback `20260411150854`.
- `corpus/SOURCES.md:147` (S206) — quote
  `the project-level skill takes precedence and the user-level skill is ignored.`:
  **present verbatim** (with the period). Anchor `the "Skill location" section` is **exact** — a
  real h2 titled `Skill location` (offset 12 825) is the section containing the sentence; the later
  h2 `Skill locations and configuration` (22 148) is a different section. Both quotes are also in
  `corpus/knowledge/skill-name-precedence-round69.md` lines 21 and 24 as the per-client quotes, so
  the C1 counter's quote↔anchor and quote↔table matches are satisfied on today's bytes.
- One precision defect, annex prose only: S206's `(12 words)` is **11** words by the counter's own
  measure (`verifiers/check_skill_precedence.py:156`:
  `0 < len(q.split()) <= 25`; the quote splits to
  the|project-level|skill|takes|precedence|and|the|user-level|skill|is|ignored). The `<= 25`
  conjunct is unaffected, so C1 does not fail on it; S203's `(8 words)` is correct.

## Freshness evidence (reproducible)

| item | value |
|---|---|
| live fetch time | 2026-10-25 10:15 UTC |
| Roo cited URL | `https://docs.roocode.com/features/skills` → 301 → `https://roocodeinc.github.io/Roo-Code/features/skills/` |
| Roo page modified | 2026-05-15T18:04:45Z (`dateModified`) |
| Roo live sha256 | `fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2` |
| Junie live headers | `Last-Modified: Fri, 23 Oct 2026 18:43:22 GMT`, `ETag "6adbaaca-966d"` |
| Junie live sha256 | `b3c676900e3de8a0d34754bb223685e1734c95ecc635280d8b8b159928f5a915` |
| Wayback snapshots read | Roo `2026-01-01/01-15/01-17/02-21/04-11` (200) + `06-20` (301); Junie `2026-03-03`, `2026-08-14` (200, id_ raw) |
| scratch | `/tmp/q69` only |

## Residual unknowns

- No JS-rendered or client-only variant was exercised; both pages ship their prose in the served
  HTML, so the probes are on the real bytes, but a CDN/A-B variant at another edge was not sampled.
- Roo's docs source repository (the MkDocs markdown behind the 301 target) was not searched for a
  removed `Skill locations` heading; the verdict rests on the cited page + six dated snapshots.
- Register rows are historical artefacts of another lane's census; whether the owner reclassifies
  S172 or leaves it as a documented fold limitation is outside this seat.
