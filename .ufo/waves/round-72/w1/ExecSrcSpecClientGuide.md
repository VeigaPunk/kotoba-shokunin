verdict: source opened and every quoted sentence located — the staged row S256 and the entry that cites it are **confirmed** on the loading/validation/disclosure axes (two clauses **confirmed-after-shaping**: an escaped tilde/angle bracket in the `.md` export and one "only when referenced" paraphrase). Both quarantine rows (register S167, S176) flag *prose*, not page quotes: their `payload-absent` class is a checker-scope artifact, **not fabrication**, and the payload each row describes is on the page. The lane must **not append S256 as a new row** — it already holds the document as S002 under the extensionless URL, and the census cannot see the `.md`/extensionless pair as a duplicate (probe below).

# S256 source open — agentskills.io "How to add skills support to your agent"

Seat ExecSrcSpecClientGuide, round 72 wave 1. Staged row read: `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:60` (1610 bytes on that line).
Host+path for duplicate detection: **`agentskills.io` + `/client-implementation/adding-skills-support.md`** (rendered form: same path without `.md`). Lane occurrence: `corpus/SOURCES.md:15` (S002). Staged rows on this URL: S247 and S256 (both `.md`). Register rows on this URL: S167, S176.

## 1. What I fetched (metadata; bytes saved as the snapshot)

| form | URL | HTTP | final url_effective | UTC | bytes | sha256 |
|---|---|---|---|---|---|---|
| markdown export | `https://agentskills.io/client-implementation/adding-skills-support.md` | 200 | same | 2026-10-25T21:39:21Z | 20446 | `07511caadbe1bad84d81477d0efce87bc2c7eaff562179522c083910586dfb06` |
| rendered page | `https://agentskills.io/client-implementation/adding-skills-support` | 200 | same | 2026-10-25T21:39:22Z | 388444 | `c5475abc5011bca200aa14b24f3b473c36835276270f80bb18006c4e0e3b2e90` |
| Wayback raw `id_` 20260914113657 (comparison only) | `https://web.archive.org/web/20260914113657id_/https://agentskills.io/client-implementation/adding-skills-support.md` | 200 | not printed | ~2026-10-25T21:44Z | 20898 | `053f470d59333548d1338e2c4ea1aa69cb2da47ff12d7977d180c7ab70611ea6` |

Command (scratch dir `/tmp/k72w1-ExecSrcSpecClientGuide.IWaf`, since deleted):

```
curl -sS -A 'Mozilla/5.0' -w '%{http_code} %{url_effective} %{size_download}\n' \
  -o s256.md 'https://agentskills.io/client-implementation/adding-skills-support.md'
→ 200 https://agentskills.io/client-implementation/adding-skills-support.md 20446
sha256sum s256.md
→ 07511caadbe1bad84d81477d0efce87bc2c7eaff562179522c083910586dfb06  s256.md
```

No redirects (`url_effective` == requested on both live fetches; the Wayback fetch printed only status and size, and its bytes match the r47 archive read exactly — `053f470d…1ea6`). The `.md` export is the canonical form for this row (the row cites the `.md` URL, and the lane's r47 record used it).

**Snapshot (committed-shaped write, the only one outside my build dir):**

- `.ufo/waves/round-72/snapshots/S256-adding-skills-support.md` — raw fetched bytes, 20446 B, unmodified.
- `.ufo/waves/round-72/snapshots/S256-adding-skills-support.html` — the rendered page, 388444 B (same bytes on a second fetch at 2026-10-25T21:49Z: `sha256sum` → `c5475abc…`, identical).
- `.ufo/waves/round-72/snapshots/S256.sha256` — both pins, the sibling-seat format (`S248.sha256`, `S264.sha256`); `sha256sum -c S256.sha256` from that directory → `.md: OK`, `.html: OK`, exit 0.
- `.ufo/waves/round-72/snapshots/S256-adding-skills-support.provenance.txt` — the table above plus the freshness reconstruction.

The `.md` snapshot starts with the site's own index blockquote (`> ## Documentation Index`), i.e. it is the page bytes, not a wrapper.

## 2. Located quotes — row S256

Line numbers are lines of the committed snapshot (`sed -n '<L>p'` on `.ufo/waves/round-72/snapshots/S256-adding-skills-support.md`).

| # | row's quoted text | located | section heading | line | bytes dropped / shaping |
|---|---|---|---|---|---|
| 1 | `The core principle: progressive disclosure` | yes | `## The core principle: progressive disclosure` | 20 | dropped `## ` (3 bytes); heading text otherwise literal |
| 2 | `~50-100 tokens per skill` | yes, after shaping | `## The core principle: progressive disclosure` (tier table) | 26 | the `.md` escapes the tilde: raw is `\~50-100 tokens per skill`; dropped `\` (1 byte) |
| 3 | `<5000 tokens (recommended)` | yes, after shaping | same tier table | 27 | raw is `\<5000 tokens (recommended)`; dropped `\` (1 byte) |
| 4 | `### Lenient validation` | yes | `### Lenient validation` | 130 | none — literal line |
| 5 | `The lenient approach above deliberately relaxes these to improve compatibility with skills authored for other clients.` | yes | `### Lenient validation` (NOTE alert) | 143 | the quote is the sentence tail of L143; dropped prefix `> The [specification](https://agentskills.io/specification.md) defines strict constraints on the `name` field (matching the parent directory, character set, max length). ` |
| 6 | `### Behavioral instructions` | yes | `### Behavioral instructions` | 198 | none — literal line |
| 7 | "three-tier table" (the row's noun phrase for the loading model) | yes, after shaping | `## The core principle: progressive disclosure` | 22 + 24–28 | the page's own wording is `three-tier loading strategy:` (L22); the table rows are L26–28 (L24–25 are the header and delimiter) |
| 8 | "the two behavioural-instruction blocks a client is told to put beside the catalog" | yes | `### Behavioral instructions` | 200, 204–210, 214–218 | two fenced blocks at L204–210 (file-read) and L214–218 (dedicated tool); the lead sentence is L200 |

Pasted from `sed -n`:

- L20 → `## The core principle: progressive disclosure`
- L26 → `| 1. Catalog | Name + description | Session start | \~50-100 tokens per skill |`
- L27 → `| 2. Instructions | Full `SKILL.md` body | When the skill is activated | \<5000 tokens (recommended) |`
- L28 → `| 3. Resources | Scripts, references, assets | When the instructions reference them | Varies |`
- L130 → `### Lenient validation`
- L143 → `> The [specification](https://agentskills.io/specification.md) defines strict constraints on the `name` field (matching the parent directory, character set, max length). The lenient approach above deliberately relaxes these to improve compatibility with skills authored for other clients.`
- L198 → `### Behavioral instructions`

**Which form the quote lives in.** Both. The `.md` carries every row quote; the token-table strings are the only ones shaped by the export (escaped `\~` and `\<`). The rendered page carries them unescaped — `grep -o "50-100 tokens per skill" S256-adding-skills-support.html` → 2 hits, `grep -o "5000 tokens (recommended)" S256-adding-skills-support.html` → 2 hits (the Next.js payload duplicates strings) — and the three headings appear in the rendered payload too (`The core principle: progressive disclosure`, `Lenient validation`, `Behavioral instructions`, 2 hits each). Anchor ids exist in the rendered page for `lenient-validation`, `behavioral-instructions`, `trust-considerations`, `what-to-store` (1 each); the core-principle heading's id appears as `progressive-disclosure` (9 occurrences in the payload).

## 3. Located quotes — the entry that cites S256

`/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/context-rot-and-always-on-context.md:29` is the only sentence in that entry that cites S256:

> "(S256) puts the catalog at ~50-100 tokens per skill, the instructions under 5000 tokens on activation, and the resources only when referenced."

| clause | located | line | verdict |
|---|---|---|---|
| catalog at ~50-100 tokens per skill | yes | 26 | confirmed (en dash `–` in the entry vs hyphen in the page is typography, not content) |
| instructions under 5000 tokens on activation | yes | 27 (`When the skill is activated` + `\<5000 tokens (recommended)`) | confirmed |
| resources only when referenced | yes | 28 (`When the instructions reference them`) | **confirmed-after-shaping** — the entry drops "the instructions" and adds "only"; the page's condition is "when the instructions reference them" |

No other sentence in that entry quotes S256. (The entry's `~50-100 tokens per skill` phrase in the same sentence is quoted from S255, not S256 — out of this seat's scope.)

## 4. Located quotes — the two entries the row's `used-by` cell names

Row S256 `used-by` cell: `corpus/knowledge/client-frontmatter-and-discovery-divergence.md, corpus/knowledge/client-implementation-loading-model-amendment-2026-10-23.md`. Both files exist in the package and both carry `source: S256` lines (divergence :7, amendment :4). Every S256-attributed quote in them:

| entry:line | quote (≤25 words) | snapshot line | verdict |
|---|---|---|---|
| amendment :15–16 | `Every skills-compatible agent follows the same three-tier loading strategy:` | 22 | confirmed-after-shaping (entry lowercases `Every` → `every`) |
| amendment :21 | `~50-100 tokens per skill` | 26 | confirmed (entry unescapes the export's `\~`) |
| amendment :22 | `<5000 tokens (recommended)` | 27 | confirmed (entry unescapes the export's `\<`) |
| amendment :23 | `when the instructions reference them` | 28 | confirmed-after-shaping (entry lowercases `When`) |
| amendment :32 | `Include a short instruction block alongside the catalog telling the model how and when to use skills.` | 200 | confirmed-after-shaping (entry lowercases `Include` → `include`) |
| amendment :34 | `use your file-read tool to load` | 206 | confirmed; the entry's quote continues across the page's line break into L207 (`the SKILL.md at the listed location before proceeding.`) — dropped bytes: the newline between L206 and L207 |
| amendment :36 | `call the activate_skill tool` | 216 | confirmed; same line-join across L216→L217 |
| amendment :37 | `the skill content itself provides the detailed instructions once loaded` | 220 | confirmed, literal substring |
| amendment :51 | `a description is essential for disclosure` | 136 | confirmed, literal substring |
| amendment :52–53 | `don't block skill loading on cosmetic issues` | 139 | confirmed, literal substring |
| amendment :53 | `defines strict constraints on the `name` field` | 143 | confirmed, literal substring |
| amendment :54 | `deliberately relaxes these to improve compatibility with skills authored for other clients` | 143 | confirmed, literal substring |
| divergence :27 | `Name doesn't match the parent directory name` | 134 | confirmed, literal substring |
| divergence :27 | `Name exceeds 64 characters` | 135 | confirmed, literal substring |
| divergence :29–30 | the `defines strict constraints…` and `deliberately relaxes these…` pair | 143 | confirmed (same substrings as above) |

All quotes are ≤25 words as recorded; the two long ones I split are the file-read and activate-tool sentences, whose joined form spans two page lines.

## 5. Freshness: the raw sha changed, the prose did not (byte-exact proof)

The lane's prior pin for this file is `79489bd252377681a31958e75ee3e6e96f7f791719eaac3b3e870a0d193be172` at 20349 bytes, 2026-10-21 (`.ufo/waves/round-47/build/SrcS002.md:14`). Today's `.md` is 20446 bytes — a 97-byte drift. It is entirely publisher-side link rewriting:

```
python3 - <<'EOF'   # in scratch
import hashlib
b=open('s256.md','rb').read()
r=b.replace(b'https://agentskills.io/specification.md',b'/specification') \
   .replace(b'https://agentskills.io/specification#compatibility-field',b'/specification#compatibility-field')
print(len(r), hashlib.sha256(r).hexdigest())
EOF
→ 20349 79489bd252377681a31958e75ee3e6e96f7f791719eaac3b3e870a0d193be172
```

Reverting the four absolutized links reproduces the r47 pin **byte-exactly**. Cross-check against the 2026-09-14 Wayback capture: `diff -u wb.md s256.md` → exit 1, 6 hunks, all renderer-level (absolute links ×3, padded→compact tables ×2, `<Note>`/`<Tip>` → GFM alerts ×3); with tables, alert markers and link targets normalized both files hash to `d48c2265c0de3d62179305d26e473ea2b1eca755e57e43ffccfc8b12d55fc338` at 190 normalized lines each. Publisher payload `lastModified` for this file: `2026-03-10T13:40:59.504Z`.

**Consequence for C2 / the recheck method:** a raw `.md` sha256 is the wrong freshness signal for this page (the exporter has changed twice under the lane's feet: r47 recorded MDX→GFM alerts plus table padding; today adds absolute link rewriting), and today's raw hash matches neither pin on file (r46 `9c0e85ee…` is an inverse-rendered transform; r47 `79489bd2…` is the pre-absolutization bytes). Recheck on the heading strings plus the link-reverted hash above.

The staged row's `fetched as `.md` 20 446 B on 2026-10-23` — **size confirmed** (20446 B today, HTTP 200); the 2026-10-23 bytes themselves are **not retrievable** (CDX for the `.md` form lists one capture, 20260914113657; the extensionless URL has captures at 20260924100801/20260924100803 only), so the date is unverified, not contradicted.

## 6. Quarantine hand-checks (register rows on this URL)

Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`, data rows only.

**S167 — register:108.** Flagged span (the register's `quote` cell): `The lane holds this page as S002; this row records only that` — `payload-absent`.

- That string is **not a page quote**: it is the row's own `teaches`/`recheck` prose (it continues `paragraph, which no lane entry cites. Re-check: refetch the`). It is absent from the page for the trivial reason that it was never meant to be there. `grep -c "The lane holds this page as S002" S256-adding-skills-support.md` → 0.
- The row's *claims*: "the lane holds this page as S002" → **confirmed** (`corpus/SOURCES.md:15`, same document, extensionless URL). "records only that paragraph" — the paragraph in question is `### Trust considerations` (L91–L94, anchor `id="trust-considerations"`); S002's anchor cell reads `§ Handling malformed YAML, § Lenient validation`, i.e. S002 does **not** record the trust paragraph either. The row said S164 did; **S164 does not resolve** at the lane tip — the registry ids run `… S129 S198 …` (`grep -o "^| S[0-9]\{3\}" corpus/SOURCES.md`), and no S164 row exists in the staged package either (`grep -rn "S164" SOURCES.append.md knowledge/corpus/knowledge/*.md` → only S256's own row mentions the id in its teaches cell).
- **Verdict: register class mislabeled — not fabrication; the flagged span is meta prose. Row's S002 claim confirmed, its S164 claim unverifiable (id absent at the lane tip).**

**S176 — register:114.** Flagged span: `The three-tier progressive disclosure table and the two` — `payload-absent`.

- Not a verbatim quote either; it is a description of the payload. The literal string is absent (`grep -c "three-tier progressive disclosure" S256-adding-skills-support.md` → 0), but the described payload is present: the heading `## The core principle: progressive disclosure` (L20), the sentence `Every skills-compatible agent follows the same three-tier loading strategy:` (L22), the three-row table (L26–28), and the two behavioural-instruction blocks (L204–210, L214–218).
- **Verdict: register literal-true, class mislabeled — a paraphrase, not fabrication; the payload is confirmed on the page.** This is the same page the row S256 records, so S176 and S256 are one document under two rounds.

Neither register row is appendable as written (their quote cells are prose); both underlying payloads are on the page, so the honest resolution is "adopt the payload under S002/S256, refuse the register's quote text". S151 (register:103) is `agentskills.io/skill-creation/optimizing-descriptions.md` — a different URL, out of this seat's scope.

## 7. Duplicate detection for the L1 — S256 must not become a second row

The lane already holds this document once, as **S002** under the **extensionless** URL (`corpus/SOURCES.md:15`). Staged S247/S256 use the **`.md`** form. The census cannot see that pair:

```
# scratch fixture: lane SOURCES.md with a probe row inserted inside the Registry table
awk 'NR==15{print; print "| S900 | Agent Skills — client-implementation guide (probe) — https://agentskills.io/client-implementation/adding-skills-support.md | docs | A | probe row for the duplicate-URL rule | § Lenient validation | probe | queued | 2026-10-25 | 90d | — |"; next}1' \
  /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md > $S/census/kotoba/SOURCES.md
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file $S/census/kotoba/SOURCES.md
→ (20 pre-existing W04 lines, no S900 line at all)  exit 0
# same probe with the extensionless URL (row id S901)
→ file  W04  S901 duplicate url agentskills.io/client-implementation/adding-skills-support across scopes
```

(`E11 … missing used-by` lines from that fixture are an artefact of validating a copy outside the lane root and were filtered out of both runs with `grep -v E11`.)

So a `.md`-form append is **silent** (exit 0, no E04, no W04), while the extensionless duplicate at least warns. Appending S256 as its own row would leave two rows for one document with no gate objecting. **Recommended:** keep S002 as the row, extend its `teaches`/`used-by`, or supersede it explicitly per CORPUS.md rule 2 — do not append a second row.

## 8. Provenance and consistency gaps found while opening (all re-checked by me, file:line)

1. **`context-rot-and-always-on-context.md` cites S256 in prose but not in its provenance trio.** Body line 29 cites `(S256)`; the `source:` lines are only `S254` (:4) and `S248` (:5), then `verified-at:` (:6) and `recheck:` (:7). Any C1-style rule of the shape "the entry opens with `source:` lines naming every cited id" fails on this entry as it stands. The two entries the row's `used-by` names do have `source: S256` lines (divergence :7, amendment :4), so the row's `used-by` cell is consistent with *those* files only — it **omits** `context-rot-and-always-on-context.md`, the entry this seat was sent to check.
2. **S002's `teaches` cell is a synthesis, not a page sentence** (`corpus/SOURCES.md:15`: "Unquoted values containing colons are technically invalid YAML; lenient clients warn and load anyway on name mismatch…"). Its parts are on the page — L121 `The most common issue is unquoted values containing colons:` and L134 `* Name doesn't match the parent directory name → warn, load anyway` — but no single sentence says it. Fine as a synthesis; it must not be quoted as verbatim.
3. **S002 still omits the two hard skips** (r47 finding 8, `.ufo/waves/round-47/build/SrcS002.md`): L136 `* Description is missing or empty → skip the skill (a description is essential for disclosure), log the error` and L137 `* YAML is completely unparseable → skip the skill, log the error`. Unchanged today; a lesson drawn from S002 alone still overstates client leniency.
4. **The trust paragraph the row attributes to S164** is L91–L94 and is recorded by no current lane row (`grep -n "Trust considerations" corpus/SOURCES.md` → no hit; the S198–S208 rows are other clients' trust models).

## 9. Facts the L1 can cite for C1 (A4 / rung rule)

- Committed snapshot: `.ufo/waves/round-72/snapshots/S256-adding-skills-support.md`, sha256 `07511caa…dfb06`, pinned in `snapshots/S256.sha256` (verified with `sha256sum -c`).
- Located quote candidates for a 5–25-word `quote` cell, each word-bounded in that snapshot: L143 (16 words, the lenient sentence), L22 (9 words), L200 (17 words), L136 substring (6 words), L139 substring (7 words), L134 (11 tokens incl. the `→`).
- If a rule cites S256, its `used-by` must list that entry — and the row id must resolve: staged S256 does **not** exist in the lane registry, and appending it duplicates S002 (§7). The clean route is S002 + extended cells.

## 10. What I did NOT check

- No browser/JS render; the rendered page was read as bytes only (its Next.js payload carries duplicated strings, which is why the HTML hit counts are 2).
- Did not re-open S255, S254, S248, S247, S164 (absent), or any row other than the two quarantine rows on this URL; the S255 attribution inside `context-rot` is taken from that entry's own `source:` line, not from a fetch.
- Did not run any lane verifier or gate (wave-1 editing window; the L1 owns post-integration gates). The only gate-shaped command I ran was `sources-census.sh validate --file` against scratch fixtures (§7), never against the live lane.
- Did not fetch the extensionless rendered page's Wayback captures (20260924100801/…03); the `.md` link-revert match to r47 made them unnecessary.
- No tools installed or upgraded; `pacman` untouched; no lane tracked file modified (`git status --porcelain` at the lane root showed only untracked `.ufo/waves/round-72/` paths).

## Report

`.ufo/waves/round-72/w1/ExecSrcSpecClientGuide.md`
