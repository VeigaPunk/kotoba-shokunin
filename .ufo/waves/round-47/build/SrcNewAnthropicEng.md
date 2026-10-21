verdict: ADMIT S012 — the source exists and says it: HTTP 200, 216,618 bytes, sha256 `c2a4f973…`, grounding quote "At startup, the agent pre-loads the name and description of every installed skill into its system prompt." (§ The anatomy of a skill, published 2025-10-16, modified 2026-10-18T21:26:58Z); the draft row validates clean in a BASE clone (exit 0), but the `S012` id is contested by two sibling drafts and must be assigned at integration.

# SrcNewAnthropicEng — candidate SOURCES.md row (round 47, frontier SOURCES step)

Seat `MoriR22R.SrcNewAnthropicEng-9`; BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git rev-parse HEAD`, exit 0).
Production files were read only. Writes: this report, `SrcNewAnthropicEng.json`, `SrcNewAnthropicEng.patch` in
`.ufo/waves/round-47/build/`, plus a BASE clone and fixtures under `/fast/scratch/kotoba-r47/MoriR22R.SrcNewAnthropicEng-9/`.

## 1. What was fetched (observed)

| fact | value |
|---|---|
| assigned URL | `https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills` |
| response | **308**, `location: /research/equipping-agents-for-the-real-world-with-agent-skills`, 63-byte body, `date: Wed, 21 Oct 2026 15:57:06 GMT` |
| canonical URL | `https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills` (`<link rel="canonical">` and JSON-LD `mainEntityOfPage`) |
| final response | **200**, `text/html; charset=utf-8`, **216,618 bytes**, sha256 `c2a4f973df7224e481dfc19fc14a9457818f6b166fffc07a3abd66d7f16e0c6d` |
| access (UTC) | **2026-10-21T15:57:06Z** (`date -u` before fetch: `2026-10-21T15:54:48Z`) |
| refetch stability | 3 body fetches, byte-identical (same sha256); recorded times 15:54:48Z and 15:57:06Z, the middle fetch's time not recorded |
| tool | `curl 8.23.0 (x86_64-pc-linux-gnu) libcurl/8.23.0 OpenSSL/3.6.5` |
| robots | `https://www.anthropic.com/robots.txt` → 200, `User-Agent: *` / `Allow: /` |
| rendering | server-rendered: the quoted paragraph is in the initial HTML response (byte 42765), not client-injected |

Article metadata, two sources agreeing:

- visible: `Published Oct 16, 2025`
- `<meta property="article:published_time" content="2025-10-16T00:00:00.000Z">`, `<meta property="article:modified_time" content="2026-10-18T21:26:58.000Z">`
- JSON-LD `datePublished` / `dateModified` hold the same two values
- h1 and JSON-LD `headline`: **"Equipping agents for the real world with Agent Skills"** (the lead's title)
- `<title>` and `og:title`: **"Equipping agents with Agent Skills"** — a shortened title at the current revision; the URL slug and h1 keep the original. A verifier grepping `<title>` for the lead's exact title sees a mismatch that is **not** an identity change.
- an `Update` callout near the top reads "We've published Agent Skills as an open standard for cross-platform portability." — the page defers normative authority to the open standard; S001 remains the contract row.

Quote location: `§ The anatomy of a skill` (h2, `id="the-anatomy-of-a-skill"`, deep link `#the-anatomy-of-a-skill`), first paragraph, which begins "At its simplest, a skill is a directory that contains a SKILL.md file." The quote is 17 words. In raw HTML the words `name` and `description` are wrapped in `<code>` elements, so the sentence is not a literal substring until that inline markup is stripped; after strip it occurs exactly once (byte 42765, single-line document). Rendered text line 77 of my local extraction (scratch-only, not committed).

Corroborating sentences in the same section, for the `teaches` cell (locations, not additional row quotes): level-1 label at HTML byte 43113 ("This metadata is the first level of progressive disclosure…"), level 2 body sentence, level 3 "These additional linked files are the third level (and beyond) of detail, which Claude can choose to navigate and discover only as needed.", and the principle sentence at byte 48036 ("Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable.").

## 2. Candidate row

Insertion point at BASE: after `corpus/SOURCES.md:24` (row S011), before `corpus/SOURCES.md:26` (`## Paths`); registry header at `corpus/SOURCES.md:12`.

```
| S012 | Anthropic Engineering — Equipping agents for the real world with Agent Skills — https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills | docs | A | Anthropic's own three-level progressive-disclosure loading model for skills | § The anatomy of a skill, "At startup" paragraph (heading id the-anatomy-of-a-skill); published 2025-10-16, modified 2026-10-18T21:26:58Z | Metadata (name and description) is preloaded for every installed skill as progressive-disclosure level one; the SKILL.md body loads only when Claude judges the skill relevant | queued | 2026-10-21 | 90d | — |
```

Cell rationale, against the frozen contract (`/home/vgpnk/Projects/shokunin/CORPUS.md:89-108`, carried in full at `:64` onward):

- `source` — title as h1/JSON-LD, canonical `/research/` URL (not the 308'ing `/engineering/` path). Contract line 90: canonical URL.
- `kind: docs` — enum at CORPUS.md:91-92 has no `blog`; the page is vendor-authored, not `community`.
- `tier: A`, scoped narrowly to **Anthropic's own description of its own loading model** — "maintainer statement" is an A example at CORPUS.md:93-96. Counter-position recorded: if the scope is widened to cross-client loading behavior, the row is **B**, because the page makes no measurement and its `Update` callout defers to the open standard.
- `anchor` — section + heading id + paragraph + both published and modified timestamps, satisfying CORPUS.md:99-100 ("never a bare homepage").
- `teaches` — 25 words, one benefit, grounded in the quoted sentence plus the level-1 label immediately after it.
- `status: queued`, `used-by: —` — no knowledge entry or lesson cites the row yet. `SKILL.md:63` ("Frontmatter | Trigger index; the only always-loaded bytes") asserts the same model **without** an S-id; adding one is a production edit and a knowledge entry, outside this seat's write scope. Contract line 103: `mined` requires ≥1 path in `used-by`.
- `recheck: 90d` — living vendor prose amended 3 days before access (`dateModified` 2026-10-18); `on-release` keys to a release event that prose does not have.
- `opened: 2026-10-21` — UTC access date.

ID caveat (decision for L1): `S012` is next-unused at BASE only. Two sibling drafts already use the same id — `.ufo/waves/round-47/build/SrcNewSkillCreator.json:6` and `.ufo/waves/round-47/build/SrcNewCodexSkills.json:100`; the latter's own report notes the same caveat at `SrcNewCodexSkills.md:52`. Contract: id is "next unused, never reused" (CORPUS.md:89). If another seat lands first, renumber this row (S013 or later); no other cell changes.

## 3. Gate record (ready for the round lesson `## Gate`)

```
- S012 — https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills
  (308 from https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills),
  HTTP 200, 216,618 bytes, sha256 c2a4f973df7224e481dfc19fc14a9457818f6b166fffc07a3abd66d7f16e0c6d,
  accessed 2026-10-21T15:57Z; byte-identical on refetch.
  Quote (17 words): "At startup, the agent pre-loads the name and description of every installed skill
  into its system prompt." — § The anatomy of a skill (h2 id the-anatomy-of-a-skill), first paragraph.
  Revision: published 2025-10-16, dateModified 2026-10-18T21:26:58Z (og + JSON-LD agree).
  Kind docs / tier A, scoped to Anthropic's own loading model.
```

## 4. Gate evidence (commands, exits, key output)

All census runs on the BASE clone `/fast/scratch/kotoba-r47/MoriR22R.SrcNewAnthropicEng-9/lane`, row inserted at line 25.

| command | exit | key output |
|---|---|---|
| `sources-census.sh validate .` — before row | 0 | `lane ok <scratch>/corpus/SOURCES.md`; rows 11, tier.A 10, queued 6 |
| `sources-census.sh validate .` — after row | **0** | `lane ok …`; no E/W code on S012 |
| `sources-census.sh census .` — after row | 0 | rows **12**, tier.A **11**, tier.C 1, status.queued **7**, status.mined 4, status.rejected 1, missing 0 |
| frozen contract awk (CORPUS.md census block) | — | rows 12; malformed **0**; duplicate ids **none**; enum/tier-inflation **none**; mined used-by missing **none** |
| `sources-census.sh selftest` | 0 | `selftest ok` (own fixtures killed) |

Discriminating fixtures (same row, one field mutated; written under `fixtures/<case>/corpus/SOURCES.md`):

| mutation | exit | finding |
|---|---|---|
| `kind=blog` | 1 | `E05 S012 kind=blog` — the validator reads my row's cells |
| `kind=community, tier=A` | 1 | `E10 S012 community-at-A` — tier inflation is caught |
| `anchor=homepage` | **0** | `ok` — a bare anchor is **not** a finding |
| empty `teaches` cell | **0** | `ok` — an empty teaches cell is **not** a finding |

Corpus drift delta, `verify_corpus_integrity.py --json` and `verify_corpus_independent.py --json`: identical before and after the row — `tracked_files 59, md_files 58, unindexed 1, index_tokens 76, index_tokens_outside_coverage_map 1, stale_tokens 0, missing_paths 0`. The pre-existing drift (`corpus/lessons/round-46-verifier-spotcheck.md` unindexed) is unchanged and belongs to C3.

Patch: `SrcNewAnthropicEng.patch`, one insertion, sha256 `760e35ef7eeac6ae2791039dd9b7990bf23907cf11eb7d2f28adf7e102f7e4cd`; generated with `git diff` in the clone, applied with `git apply` on a `git checkout --`-reverted BASE tree (exit 0), and `git apply --check -R` against the final tree (exit 0). The patch uses `i/`/`w/` prefixes (jj-colocated diff config); default `-p1` handles them.

## 5. Calibration — counterexamples and gaps found

1. **The source gate is shape-only.** `E05`/`E10` fire on my row's cells, but a row with `anchor=homepage` and a row with an empty `teaches` both validate clean at exit 0. The contract's anti-homepage anchor rule (CORPUS.md:99-100) and the "one grounded learner benefit" rule (`:101`) have no machine check. My row's revision and quote discipline therefore rests on this gate record and human re-open, not on `sources-census.sh`. This is a concrete gap for the calibration axis, alongside C3's errata registry.
2. **Title drift vs identity.** `<title>`/`og:title` now say "Equipping agents **with** Agent Skills"; h1 and JSON-LD keep "Equipping agents **for the real world** with Agent Skills". The archived lead title and the page agree only in h1; the canonical URL is the stable identifier. Recorded so a later reader does not file a false `reference-drift`.
3. **308 move.** The `/engineering/` path (the URL most likely copied from round-46 notes) permanently redirects to `/research/`. A row citing `/engineering/` would still resolve today but would duplicate an E04-normalized URL only if normalization follows redirects — the row uses the canonical target instead.
4. **No primacy claim.** The lead describes this page as the "origin of the 3-level progressive-disclosure model" (`corpus/SOURCES.md:70`). I verified that the page states the three levels; I did **not** verify first-publication priority, so the `teaches` cell does not assert "origin".
5. **ID collision** (§2) — three drafts, one id; integration must renumber.
6. **Relevance is real, not decorative.** `SKILL.md:63` already ships the level-1 claim ("Frontmatter … the only always-loaded bytes") unsourced; `SKILL.md:151` shows the lane's citation idiom (S001/S002/S003/S008 inline). Routing frontmatter-trigger facts through this row would make it `mined`; that edit is production and out of scope here.

## 6. What this row does and does not carry

- Carries: metadata-only routing as an explicit, vendor-stated three-level model — level 1 name+description preloaded for **every** installed skill, level 2 body on judged relevance, level 3+ linked files navigated as needed. This is the primary support for why a description is a routing surface and why body depth is free.
- Does not carry: the open normative field contract (S001), Anthropic's authoring rules such as the XML-tag ban (S003), lenient-client behavior (S002), or any measured harness behavior on this host (omp's 99-char truncation, opencode's full-description catalogue — both local observations recorded in `SKILL.md:83-103`).

## 7. Not checked

- Non-author re-open of the live page (contract rule 1 requires a sample; that is a reviewer's step, not mine).
- Whether Anthropic edits the article after 2026-10-18T21:26:58Z; no Wayback/archived revision history was consulted.
- The progressive-disclosure diagram's image contents (caption only; the article states the model in prose, which is what the row quotes).
- Any harness's measured behavior against the model; no host artefacts were opened for this row.
- Sibling lanes' rows beyond a URL reuse sweep: `for f in */corpus/SOURCES.md; do grep -l 'equipping-agents-for-the-real-world-with-agent-skills' "$f"; done` → no matches (exit 1). A broader fleet grep timed out at 300 s and was abandoned; it had surfaced only `.ufo/waves/kaika-w1/kotoba-art.md` before the timeout.

## 8. Tooling

None installed or upgraded. `curl 8.23.0` was already present; no network fetch beyond the source page, its redirect target, `robots.txt`, and the single web search used to locate the canonical path.

Artifacts: `SrcNewAnthropicEng.md` (this report), `SrcNewAnthropicEng.json` (fetch/revision/gate record, valid JSON, 19 top-level keys), `SrcNewAnthropicEng.patch` (1-line row insertion).
