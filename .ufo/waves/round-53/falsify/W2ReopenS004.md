Result: MIXED — every line the S004 row and `corpus/knowledge/alwayson-rule-files-round53.md` cite re-verifies verbatim on the live page and in the pinned source at `d001185d`, and the row's mined flip is contract-conformant, but one citation parenthetical attributes to agents.md a `CLAUDE.md`→`AGENTS.md` symlink the page never mentions (S3), plus one wording note (S4).

Round 53, wave 2 (falsify), seat `KotobaR53.W2ReopenS004`. Judged revision `c775d6823bfca8f0de8c0874032a954438b38edc` (`git rev-parse HEAD` → `c775d6823bfca8f0de8c0874032a954438b38edc`; `git diff --stat c775d682… -- corpus/SOURCES.md corpus/knowledge/alwayson-rule-files-round53.md` → empty, exit 0, so the working tree is the judged bytes). Target: `corpus/SOURCES.md:17` (row S004). I wrote only this report. Scratch bytes: `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReopenS004/`. No tool installed or upgraded; no model call; no lane write; no `ask`.

## 1. Fetch receipt (independent, this seat)

```
curl -sS -D headers.txt -o agentsmd.html -w 'HTTP %{http_code} bytes %{size_download}\n' https://agents.md/
HTTP 200 bytes 81690                     # 2026-10-22T20:36:42Z, exit 0
sha256sum agentsmd.html
06b65de9018141350fe45cdd9fccafa59787badc46f30d92a06c07e612713979  agentsmd.html
```
Headers: `server: Vercel`, `content-type: text/html; charset=utf-8`, `etag: "vt6j5odein1r0m"`,
`content-length: 81690`, `x-vercel-cache: HIT`, `age: 5792` (object generated ~19:00:10Z today, matching the `date` header).
Revalidation: `curl -H 'Cache-Control: no-cache'` at 2026-10-22T20:40:29Z → `HTTP 200 bytes 81690`, sha256 identical
(`06b65de9…`). So 81,690 B / `06b65de9…` is the live body now and is stable across 36 minutes.

Pinned source, same session (`raw.githubusercontent.com/agentsmd/agents.md/d001185d792eb6402a58e4cbef1c228b309ec25d/components/…`):
`FAQSection.tsx` HTTP 200, 3,152 B, sha256 `f884067162ad6b4a629904664f8ffe93bce92296b05ac971027176dbf1eb1e32`;
`HowToUseSection.tsx` HTTP 200, 2,065 B, sha256 `ea4b43e19c2cfdfc7d98d09ab0d4a67baad6973d751b0e474811b4f0c8226ef9`.
Both hashes equal the ones `ScribeAgentsMdSpec.md:99` recorded, so the pin is reproduced, not trusted.

## 2. Comparison with the row's anchor cell

Row S004 (`corpus/SOURCES.md:17`, cells: anchor `§ FAQ "What if instructions conflict?"; live page opened 2026-10-19`,
status `mined`, opened `2026-10-19`, recheck `90d`, used-by `corpus/knowledge/alwayson-rule-files-round53.md`).

The anchor cell carries **no bytes and no sha256** — it names a heading and a date — so a numeric comparison against the
anchor cell itself is impossible; the comparison runs against the two evidence stores the file's header names:

| evidence | accessed (UTC) | bytes | sha256 |
|---|---|---|---|
| round-46 record, `.ufo/round-46/evidence/w2/sources/fetch-log.json:33-37` (raw HTML) | 2026-10-19T18:40:55Z | — | `e3a5b9a4825ed894447dec3dbd96b8d73f1aa84dce19a1964642d63e2c3c9c75` |
| round-47 record, `.ufo/waves/round-47/build/SrcS004.json:28-32` (fetch block) | 2026-10-21T15:54:15Z | 81,690 | `b0a63496f7c71419d2df378246ce9e7fe4501a849818a941cc7f424c0559125b` |
| round-53 record, `corpus/lessons/round-53.md:36-39` | 2026-10-22T20:04:34Z | 81,690 | `06b65de9…` |
| this seat | 2026-10-22T20:36:42Z and 20:40:29Z | 81,690 | `06b65de9…` |

Byte length is 81,690 at all three of the last fetches; the hash is not stable across days but **is** stable within today,
and my fetch equals the round-53 lesson record exactly. The anchor's `2026-10-19` is a true historical open (round-46
`accessed_utc`), and its old raw hash is a stale pointer, which the round-53 lesson already states in the same sentence
(`corpus/lessons/round-53.md:36-37`: "the round-46 record carries `e3a5b9a4…`; the bytes changed, the quoted sentence did
not"). Cause of the delta is bounded, not proven: the body embeds per-deployment `dpl_` tokens (26 occurrences), GitHub
avatar URLs, and a data-driven `contributorsByRepo` map (`"total":679`, `"total":4734`, `"total":160`, `"total":8`), while
`"buildId":"DyM2DITjzBZhj49DSSTvz"` is identical to round-47's recorded build id at identical length, so the difference
sits in data/asset regions rather than in a content edit — `[INFERENCE]`, because neither earlier byte body was stored
(`SrcS004.json` "body_stored_in_lane": false).

## 3. Row cells — per-claim verdicts

- **Anchor heading `§ FAQ "What if instructions conflict?"` — HOLDS.** Deployed page: `<section id="faq">` at byte offset
  65,858, `<h2>FAQ</h2>`, and the `<h3>` question at 66,484; source `FAQSection.tsx:18` (`question: "What if instructions conflict?"`).
- **`teaches`: "the closest AGENTS.md to the edited file wins and explicit user chat prompts override everything" — HOLDS.**
  Deployed offset 66,581-66,675: "The closest AGENTS.md to the edited file wins; explicit user chat prompts override
  everything." (14 words); pinned `FAQSection.tsx:18-21`, answer string at `:20`. The corpus row's semicolon → "and" is a
  faithful paraphrase.
- **`status` `mined` + `used-by` — HOLDS.** The knowledge entry cites S004 in its `source:` line and twice in the body
  (`alwayson-rule-files-round53.md:1, 33, 44`) — contract definition of `mined` (`CORPUS.md:103`). Census
  `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, output
  `W04 S018`, `W04 S019`, `W04 S021`, `kotoba ok`; E11 (used-by missing) did not fire, `awk` field count 11 columns.
- **`opened 2026-10-19` — HOLDS, with the note that it is the round-46 open and not this round's.** The flip was made
  under `CORPUS.md:116-118` rule 2 ("Only `status`, `recheck` and `used-by` change in place, and each change is logged
  old→new in the round lesson"), and `corpus/lessons/round-53.md:36-39` logs exactly `status` queued → mined, `used-by`
  — → the entry, and carries the 2026-10-22 open with bytes, hash and quote. So the row's inline evidence (a dated
  open, no hash) is contract-compliant, not a break; the only stale hash sits in the round-46 fetch-log the file header
  names, and the lesson records the current one. `overdue` run: `bash scripts/sources-census.sh overdue --root … kotoba` → exit 0,
  `kotoba	cadence	S004 recheck=90d opened=2026-10-19` (due 2027-01-17 by the registry's own arithmetic).
- **`scope`, `tier A`, `kind spec` — HOLD by the registry's usage.** `CORPUS.md:93-97` admits tier A for a primary or
  authoritative page for the scope; agents.md is the format's own primary page and its `teaches` is one grounded benefit.
  `kind spec` is a curation choice for a format page that states no RFC-style normative language — **S4 note**, not a break
  (the entry itself calls it "agents.md convention").

## 4. Knowledge-file lines that cite S004 — per-line verdicts

`corpus/knowledge/alwayson-rule-files-round53.md:33` (row `| agents.md convention | S004 | … |`):

- **Name read `AGENTS.md` — HOLDS.** Deployed page: "Create an AGENTS.md file at the root of the repository." (offset 62,799);
  pinned `HowToUseSection.tsx:10-11`. (The cell does not line-anchor this sentence; the entry's frontmatter anchors
  `FAQSection.tsx:18-21, :31-48` only. The name is also carried by the page title/hero, so the claim is unambiguous — **S4 note**.)
- **"The closest AGENTS.md to the edited file wins" (`FAQSection.tsx:20`) — HOLDS.** Line 20 of the pinned file is the whole
  sentence verbatim; the quote is a prefix ending at the semicolon. 14 words total, ≤25.
- **"not addressed" (both `AGENTS.md` and `CLAUDE.md` in one directory) — HOLDS.** The deployed body has **0** occurrences of
  `CLAUDE` and **0** of `claude` (case-sensitive counts, 81,690 B), one `conflict` (the FAQ question), one `precedence`, one
  `nearest`, one `monorepo`, and no rule for two different names in one directory; the four `copilot` hits are only
  `copilot.svg` mask URLs in the logo marquee.
- **"a symlink from an old name to `AGENTS.md` (`:31-48`)" — HOLDS.** `FAQSection.tsx:31-48` is exactly that FAQ item:
  question at `:32`, "Rename existing files to AGENTS.md and create symbolic links for backward compatibility:" at `:36`,
  `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md` at `:40`, item closes at `:48`.
- **Aider `read:` and Gemini CLI `context.fileName` — HOLD.** `FAQSection.tsx:54-58` (quote at `:54`, `read: AGENTS.md`
  at `:58`) and `:72-80` (`{"context": {"fileName": "AGENTS.md"}}`); deployed offsets 75,726/75,977/79,993.

`corpus/knowledge/alwayson-rule-files-round53.md:44`:

- **BREAKS (S3, citation over-attribution).** The sentence "A `CLAUDE.md` symlink to `AGENTS.md` gives every client that
  reads either name the same bytes (S043 `:455`; S004 migration symlink; S045 `:182`)" lists S004 as support for a
  `CLAUDE.md`→`AGENTS.md` symlink, but S004's documented symlink is `AGENT.md`→`AGENTS.md` (`FAQSection.tsx:36-40`) and the
  page never names `CLAUDE.md` (0 hits). The proposition is true via the co-cited S043 `:455`; S004 supports only the
  symlink-as-documented-redirect shape, so this is an attribution error inside a true sentence, not a false claim. Fix:
  drop "S004 migration symlink" or write "S004's `AGENT.md`→`AGENTS.md` symlink, same shape".

## 5. Defects and severity

| # | defect | location | severity |
|---|---|---|---|
| 1 | S004 cited as support for a `CLAUDE.md`→`AGENTS.md` symlink; S004 documents `AGENT.md`→`AGENTS.md` and never names CLAUDE.md | `corpus/knowledge/alwayson-rule-files-round53.md:44` | S3 (citation over-attribution; content true via S043) |
| 2 | Row `teaches` category label "for always-on files" is broader than the page's domain (AGENTS.md files only); the entry's own table row says the cross-name case is "not addressed" | `corpus/SOURCES.md:17` (teaches cell) | S4 (wording precision, no false clause) |

Nothing at S1 (no cited text falsified) and nothing at S2 (no evidence-store mismatch: my fetch matches the round-53
lesson record byte for byte, and the pinned source hashes reproduce the seat's).

## 6. What I did not check

- Whether the Oct-19/Oct-21 bytes differed from today's only in data/deploy tokens: the earlier bodies were not stored, so
  that is `[INFERENCE]` from the `dpl_`/avatar/`contributorsByRepo` structure and the unchanged build id, not a diff.
- The page's JavaScript runtime or any client's loader: S004 is a format page; this seat measured documentation bytes only.
- The other 8 rows the entry uses (S043-S050), the C1/C2 counters, the erratum guards and the repairs — other seats' items.
- The `overdue` and `validate` runs are read-only stdout modes of the fleet script (`scripts/sources-census.sh`, header:
  "Read-only … writes only stdout or --out"); no `--out` was passed and nothing outside this report was written.
