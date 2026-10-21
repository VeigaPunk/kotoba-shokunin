verdict: HOLDS — S014's 17-word quote, its section anchor and all eleven row cells survive an independent live re-open at `7ad7fad`; the seat's fetch record carries two precision defects and a whole-page-hash trap, none of them in the corpus row or the lesson Gate.

# W2S014Reopen — Anthropic "Equipping agents for the real world with Agent Skills" (SOURCES S014) at `7ad7fad`

Scope: re-open `https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills`
and check the landed row `corpus/SOURCES.md:27`, its Gate record
`corpus/lessons/round-47.md:37` (section header `:27`), and the referenced seat receipt
`.ufo/waves/round-47/build/SrcNewAnthropicEng.md` / `.json` against the frozen contract
(`/home/vgpnk/Projects/shokunin/CORPUS.md:80-124`, SOURCES-CONTRACT-v1).
Read-only against the fleet lane; all scratch work in
`/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2S014Reopen-2/kotoba-shokunin` at `7ad7fad`
(`git rev-parse HEAD` exit 0, `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`).
Access window: `2026-10-21T16:54:54Z`–`16:56Z` (response `date` headers).

## Target question — answered YES

The live page still contains the exact sentence, in the named section, in the
server-rendered HTML:

- `curl` exit 0, HTTP **200**, **216,618 bytes**, canonical URL, response
  `date: Wed, 21 Oct 2026 16:54:54 GMT`.
- Quote at raw byte **42,743**: `At startup, the agent pre-loads the <code …>name</code>
  and <code …>description</code> of every installed skill into its system prompt.`
  After tag-stripping it occurs **exactly once** in the page text and is **17 words**.
- Enclosing heading: `<h2 … id="the-anatomy-of-a-skill">The anatomy of a skill</h2>`
  at byte **41,507**; the next `<h2>` is "Developing and evaluating skills" at byte
  **54,411**, so the quote is inside the named section.
- Revision metadata: `article:published_time` `2025-10-16T00:00:00.000Z`,
  `article:modified_time` `2026-10-18T21:26:58.000Z`; JSON-LD `datePublished`/
  `dateModified` agree; visible "Published Oct 16, 2025"; h1 and JSON-LD headline are
  the row's exact title; `<link rel="canonical">` and `mainEntityOfPage` are the row's
  exact URL.
- The `/engineering/` path still returns **308** → `/research/…` (verified this run);
  the row cites the canonical target, as the contract requires.

The row's eleven cells, against `CORPUS.md:89-108`:

| cell | value at `corpus/SOURCES.md:27` | check |
|---|---|---|
| id | `S014` | next-unused sequence S012–S015; no duplicate id in the table (`awk`/`uniq -d` empty) |
| source | `Anthropic Engineering — Equipping agents for the real world with Agent Skills — https://www.anthropic.com/research/…` | title = h1/JSON-LD headline; "Engineering" = hero metadata team label + page slug; canonical URL unique to this row (1 hit in `SOURCES.md`) |
| kind | `docs` | valid enum; vendor-authored prose, not `community` (see F5) |
| tier | `A` | "maintainer statement", scoped narrowly (see F5) |
| scope | `Anthropic's three-level progressive-disclosure loading model for skills` | p1/p2/p3/p4 state metadata → body → linked files |
| anchor | `§ The anatomy of a skill, "At startup" paragraph; published 2025-10-16, modified 2026-10-18; opened 2026-10-21` | section + paragraph + revision, not a bare homepage |
| teaches | `Name and description are preloaded for every installed skill as disclosure level one; the SKILL.md body loads only when the skill is judged relevant` | 24 words, grounded by the quote + p2 |
| status | `queued` | no production citation of S014 outside the Gate table (grep) |
| opened / recheck | `2026-10-21` / `90d` | ISO date; valid cadence for living vendor prose |
| used-by | `—` | matches `queued`; see F5 on precedent |

## F1 — positive: quote, anchor and Gate record hold

The Gate row `corpus/lessons/round-47.md:37` carries the same 17-word quote, the access
date `2026-10-21T15:57:06Z`, and the location `(§ The anatomy of a skill)`. Mechanically
extracted from the lesson line, the quote is an exact substring of the live tag-stripped
page text; the location names the section that contains it. The row is not merely
plausible: the sentence is present in the initial HTML response, not client-injected.

## F2 — calibration: the seat receipt's raw byte offset is wrong by 22 bytes

`.ufo/waves/round-47/build/SrcNewAnthropicEng.json:74` says
`"raw_html_byte_offset_of_quote": 42765`; `SrcNewAnthropicEng.md:21`, `:32`, `:65` repeat
`byte 42765` / "first paragraph". In **both** the wave-1 saved bytes
(`/fast/scratch/kotoba-r47/MoriR22R.SrcNewAnthropicEng-9/anthropic-eng.html`, sha256
`c2a4f973…`) and the live fetch, byte **42,743** is `At startup…`; byte **42,765** is
`pre-loads the …`. The offset is off by the length of `At startup, the agent ` (22 bytes),
i.e. it points into the quote rather than at its start. This does not touch the corpus
row, but a re-checker following the receipt's offset lands mid-sentence.

Repro:

```
$ python3 - <<'PY'
s=open('anthropic-eng.html').read()
print(repr(s[42743:42783]))   # 'At startup, the agent pre-loads the <cod'
print(repr(s[42765:42805]))   # 'pre-loads the <code class=…'
PY
```

## F3 — calibration: "first paragraph" is the second `<p>` under the heading

`SrcNewAnthropicEng.json:73` and `:82`, and `SrcNewAnthropicEng.md:32`/`:65`, call the
quote's paragraph "the first paragraph under the heading, beginning 'At its simplest…'".
The first `<p>` after `</h2>` is at byte **41,585** and begins "To see Skills in action,
let's walk through a real example…"; the quote's paragraph `<p>` starts at **42,267** and
begins "At its simplest, a skill is a directory…". So the quote is in the **second**
paragraph of the section. The receipt's "rendered text line 77" is correct for the
paragraph, but the ordinal label is wrong. The row's own anchor avoids the error by
naming the paragraph by its opening words ("At startup" paragraph), which is unique in
the visible text (the second "At startup" hit is the RSC JSON payload, not prose).

Repro:

```
$ python3 - <<'PY'
s=open('page.html').read(); i=s.find('id="the-anatomy-of-a-skill"'); he=s.find('</h2>',i)+5
print(s.find('<p',he), s.find('<p',s.find('<p',he)+2))  # 41585 42267
PY
```

## F4 — freshness/calibration: the recorded whole-page sha256 is not a stable identity

The seat recorded 3 byte-identical fetches at `c2a4f973…` (`SrcNewAnthropicEng.json:29,34`,
`SrcNewAnthropicEng.md:1,16,62`). My seven fetches (initial, three refetches, three with the
seat's UA) are byte-identical to **each other** at
`7dfd6f15b8f6e7e30352d569203a8d0c285d4073c3a5793434396551f164e892`, same 216,618-byte
length. The two windows differ in **879 bytes across 67 equal-length runs**: 66 runs are
two fixed-width Next.js chunk filenames
(`38z_-z-jmbkf2.js`→`0cnlhm4w0r7-k.js`, `3npkduc0fgs_j.js`→`1dc3i2n5ay6gx.js`) and one
21-byte token (`FP6NAU4RJSHJIq_w8pFJt`→`p5eekIdddzFvTRjLZQz0O`). Both old and new chunk
URLs return HTTP 200, so this is a rebuild/edge-variant difference, not article drift.
After stripping scripts/styles/tags the article text is **identical**: 10,046 characters,
sha256 `a71e804197ed6fde47839aaee241dbb649c810c039296867f302307a73603f5c` for both files.
Consequence: a future freshness check that compares the receipt's whole-page sha256 will
report false drift even though the quoted prose is unchanged. The lesson Gate does not
carry the hash (good); the seat report does. Pin the stripped-text digest or quote
presence, not the raw page hash.

## F5 — cells that are judgment calls, not defects

- `kind: docs` — the enum (`CORPUS.md:91-92`) has no `blog`; the page is vendor-authored
  official prose, and `community` is never A. `docs` is the least-wrong enum. If the
  contract ever adds a vendor-blog kind, this row should be re-kinded, not re-tiered.
- `tier: A` — A includes "maintainer statement"; the scope is explicitly Anthropic's own
  loading model. Widening the scope to cross-client behavior would make it B, as the seat
  itself recorded.
- `teaches` level-one label — the Gate's 17-word quote grounds the preload clause; "as
  disclosure level one" is carried by the next paragraph (p2: "This metadata is the first
  level of progressive disclosure"), still inside the anchored section. The row's wording
  is accurate to the page; the single-quote Gate format cannot carry both sentences under
  25 words.
- `status: queued` / `used-by: —` — the Round-47 Gate table lists S014, but precedent is
  that a Gate listing is provenance, not a `used-by` citation: S009/S010 were listed in
  the Round-46 Gate (`corpus/lessons/round-46.md:71-72`) and remain `queued`/`—`, and
  S013 is in the same position this round. No production file cites S014 as support
  outside the Gate table.
- `source` prefix "Anthropic Engineering" — the phrase is not in the h1, but the hero
  metadata lists the article's team as **Engineering** (stripped text: "Published Oct 16,
  2025 Team Engineering Topics …") and the page data's slug is `engineering`, so the label
  is grounded rather than inferred.

## Commands run (exit codes and key output)

| command | exit | key output |
|---|---|---|
| `curl -sS -D headers.txt -o page.html <canonical URL>` | 0 | `200`, 216,618 bytes, `date: Wed, 21 Oct 2026 16:54:54 GMT` |
| 3× refetch, plus 3× with the seat's UA (`kotoba-source-audit/1.0`, `Accept: text/html`) | 0 | all `200`, 216,618 bytes, sha256 `7dfd6f15…` |
| `curl -D - <old /engineering/ URL>` | 0 | `308`, `location: /research/…` |
| Python tag-strip + hash of both saved bodies | 0 | stripped text equal, 10,046 chars, sha256 `a71e8041…`; quote count 1; 17 words |
| Python `cmp`-style byte diff wave-1 vs live | 0 | 879 differing bytes, 67 equal-length runs, 0 article-prose runs |
| `curl` GET the four chunk URLs (body discarded) | 0 | all `200` |
| `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | **0** | `kotoba ok …/corpus/SOURCES.md` |
| `… census --root … kotoba` | **0** | `rows 15`, `tier.A 14`, `status.queued 8`, `status.mined 6`, `missing 0` |
| `… selftest --root …` | **0** | `selftest ok` (both fixtures killed) |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | **0** | all checks PASS |
| `python3 -B verifiers/verify_corpus_independent.py --json` | **0** | all checks PASS |
| `git diff -U0 c61a973… 7ad7fad -- corpus/SOURCES.md \| grep '^-'` | 0 | only the two intro evidence lines removed; no `S0xx` row line changed |
| `git ls-files .ufo/waves/round-47/build/ \| grep -i anthropic` | 0 | receipt `.md`, `.json`, `.patch` tracked at `7ad7fad` |

No tool was installed or upgraded; `curl 8.23.0` and the repo's `python3` were already
present.

## What I did NOT check

- Wayback/archived revision history; whether Anthropic edits the page after
  `2026-10-18T21:26:58Z`. My own fetches span ~2 minutes; the cross-window comparison is
  against the wave-1 snapshot taken ~57 minutes earlier, not against an archive.
- The progressive-disclosure diagram image; the row quotes prose, not the figure.
- The other new rows S012/S013/S015 and the C1/C2/C3 claims/pins; sibling seats own them.
  (S013 has its own falsify report in this directory.)
- The seat's `SrcNewAnthropicEng.patch` was not applied; I compared the landed row
  (`corpus/SOURCES.md:27`) with the seat's candidate in §2 of
  `SrcNewAnthropicEng.md`, which shows the integrator renumbered S012→S014 and shortened
  the `anchor`/`teaches` cells. Both landed wordings remain grounded.
- Any live Claude/Codex behavior against the stated model; the row reports the vendor's
  description, not a measurement.
- Primacy/origin of the three-level model (the row does not assert it).
- Non-author closure; this is lane-authored review, not a SHONEN mark.
