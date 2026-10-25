# ExecQuar05 — quarantine hand-check, register slice row 5 of 13 (campaign `S176`)

**Verdict: `absent`** — the row's quote cell is not on the cited page in any revision I could
reach (live `.md`, live HTML export, three Internet Archive snapshots), so the row is **refused as
fabrication class for its quote**. No fold is claimed (`present-after-fold` is explicitly *not*
asserted; reason in F4). The page itself is real, HTTP 200, and the *referent* of the quote cell —
a three-tier progressive-disclosure table — **is present** under a located anchor, so nothing the
row points at is lost; it is already staged for this lane as **S256** (F6). The row's own class cell
already read `payload-absent`, so this hand-check **confirms** a self-declared absence rather than
discovering a new fabrication (F7).

## F1 — The row, and the slice's truncation of it

Command (slice, verbatim line 5):

```
sed -n '5p' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt
| `kotoba` | round5 | S176 | `payload-absent` | https://agentskills.io/client-implementation/adding-skills-support.md | `The three-tier progressive
```

The slice line is 147 bytes and ends inside the quote cell, with no closing backtick:
`awk 'NR==5{print "len="length($0)}' …` → `len=147`.

The register the slice was cut from wraps the same cell over two lines:

```
sed -n '114,115p' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
| `kotoba` | round5 | S176 | `payload-absent` | https://agentskills.io/client-implementation/adding-skills-support.md | `The three-tier progressive
disclosure table and the two` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

`cmp` of slice line 5 against register line 114 → `IDENTICAL` (147 bytes each): **the slice kept the
first physical line of a wrapped row and dropped register line 115.** The complete quote cell is
therefore `` `The three-tier progressive disclosure table and the two` `` (9 words) — a dangling
descriptive fragment ending "and the two", not a sentence.

## F2 — Fetch record (the cited URL)

```
curl -sS -o page.html -w 'HTTP=%{http_code} FINAL=%{url_effective} SIZE=%{size_download} TYPE=%{content_type}\n' \
  -A 'Mozilla/5.0' -L --max-time 60 'https://agentskills.io/client-implementation/adding-skills-support.md'
HTTP=200 FINAL=https://agentskills.io/client-implementation/adding-skills-support.md SIZE=20446 TYPE=text/markdown; charset=utf-8
```

- access date `2026-10-25T21:37:22Z` (`date -u`), 337 lines
- `sha256 07511caadbe1bad84d81477d0efce87bc2c7eaff562179522c083910586dfb06`
- the URL is not a `web.archive.org` redirect (final URL == cited URL); archive checked anyway, F5

## F3 — Absence of the quote cell (and of every sub-fragment)

Named normalization used for the probe (case, whitespace collapse, Unicode dashes `U+2010/2011/2013/2014`→`-`, NBSP→space, HTML tags stripped, markdown `* _ # [ ] ( ) | >` stripped):

```
python3 - <<'EOF'   # norm() as above; counted with str.count on the normalized text
probes = ["three-tier progressive disclosure table and the two",
          "three-tier progressive disclosure table",
          "progressive disclosure table",
          "three-tier progressive disclosure"]
EOF
```

Observed hit counts — **0 for all four probes in all five artifacts**:

| artifact | bytes | sha256 (12) | hits |
|---|---|---|---|
| live `.md` (F2) | 20446 | `07511caadbe1` | 0 / 0 / 0 / 0 |
| live HTML export (`…/adding-skills-support`, `text/html`) | 388444 | `c5475abc5011` | 0 / 0 / 0 / 0 |
| archive `20260509224544` | 20898 | `053f470d5933` | 0 / 0 / 0 / 0 |
| archive `20260711201852` | 20898 | `053f470d5933` | 0 / 0 / 0 / 0 |
| archive `20260914113657` (gzip; `gzip.decompress` → 20898) | 7569 wire | `053f470d5933` after decompress | 0 / 0 / 0 / 0 |

Literal greps agree: `grep -c -i 'three-tier progressive' page.html` → `0`;
`grep -o -i '.\{0,40\}the three-tier.\{0,60\}' page-plain.html` → no output (the HTML contains
`three-tier` twice, never followed by `progressive`).

## F4 — Why `present-after-fold` is NOT claimed

The page carries the two halves in **two different sentences, in the opposite order**:

```
sed -n '20p;22p' page.html
## The core principle: progressive disclosure
Every skills-compatible agent follows the same three-tier loading strategy:
```

The register cell's order ("three-tier progressive disclosure") requires `three-tier` from line 22
to precede `progressive` from line 20. That is a cross-sentence reordering, not a case, whitespace
or markdown fold, and the fragment's tail ("table and the two") has no counterpart anywhere in the
bytes. Recording it as a fold would manufacture a quotation that does not exist; I do not.

## F5 — Archive: no revision ever contained it

```
curl -sS 'http://web.archive.org/cdx/search/cdx?url=agentskills.io/client-implementation/adding-skills-support.md&output=json&limit=20'
["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
["io,agentskills)/client-implementation/adding-skills-support.md","20260321234642",…,"9319"],
[…,"20260329074024",…,"9341"],
[…,"20260509224544",…,"8532"],
[…,"20260711201852",…,"8458"],
[…,"20260914113657",…,"8889"]
```

Five snapshots, two distinct payload digests. Round 5 landed `2026-09-28` (`LOG.md:39`:
`- 2026-09-28 — round 5: first end-to-end domain task + round-1 defect repairs.`), so the snapshot
nearest before that date is `20260914113657` — and it decompresses to the *same* bytes as
`20260509224544`/`20260711201852` (`053f470d5933`). No archived revision contains the fragment.

## F6 — Staged id for the URL: **S256** (and S247) — both by the identical host+path

```
awk 'NR==51 || NR==60' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
| S247 | Agent Skills — How to add skills support to your agent (trust-gate paragraph) — https://agentskills.io/client-implementation/adding-skills-support.md | docs | A | … | "Trust considerations"; quote "This prevents untrusted repositories from silently injecting instructions into the agent's context."; …
| S256 | Agent Skills — How to add skills support to your agent (loading model, validation and disclosure) — https://agentskills.io/client-implementation/adding-skills-support.md | docs | A | … | "The core principle: progressive disclosure" three-tier table, "### Lenient validation" and "### Behavioral instructions"; quote "The lenient approach above deliberately relaxes these to improve compatibility with skills authored for other clients."; …
```

So the row is **staged**, twice: `SOURCES.append.md:51` = S247 (trust-gate paragraph) and
`SOURCES.append.md:60` = S256 (loading / validation / disclosure). Both ids are in
`assimilation/staged-ids`. **The quarantined quote cell matches neither staged row's recorded
quote.** S256 is the semantically matching row: it is the one that stages the three-tier table my
F7 locates, and its own quote cell is a real page sentence (positive control, F8).

## F7 — The referent IS present, with its anchor (not adoptable as *this* row's quote)

Anchor: `## The core principle: progressive disclosure` (page line 20). Body sentence: line 22.
Table header and rows:

```
sed -n '24,28p' page.html
| Tier | What's loaded | When | Token cost |
| - | - | - | - |
| 1. Catalog | Name + description | Session start | \~50-100 tokens per skill |
| 2. Instructions | Full `SKILL.md` body | When the skill is activated | \<5000 tokens (recommended) |
| 3. Resources | Scripts, references, assets | When the instructions reference them | Varies |
```

Consequence for the L1: the row is refused **as a quotation** (its cell is a truncated description,
not page bytes), but the page content the register was reaching for is available, verified, and
already staged as S256 — so the refusal costs the lane no knowledge. Nothing is appended from S176.

## F8 — Positive controls (the probe is not broken)

Both staged quotes for the *same URL* locate literally in the same fetched bytes:

```
grep -n 'This prevents untrusted repositories from silently injecting' page.html
93:…Consider gating project-level skill loading on a trust check — only load them if the user has marked the project folder as trusted. This prevents untrusted repositories from silently injecting instructions into the agent's context.
grep -n 'The lenient approach above deliberately relaxes' page.html
143:…The lenient approach above deliberately relaxes these to improve compatibility with skills authored for other clients.
```

Both spans are verbatim substrings of those lines (I dropped leading context before the quoted
span; nothing inside the quoted span was dropped or altered).

## F9 — Campaign id, not a registry row

```
grep -c '^S176$' .ufo/waves/round-72/assimilation/reg-ids          → 0
git grep -n 'S176' c69711ee08279609374d895bb0f3c8c18ccf15c9 -- corpus/SOURCES.md   → (no output)
git show c69711ee…:corpus/SOURCES.md | grep -c '^| S'              → 139
```

`S176` is a campaign id only; the base registry has 139 rows and none is S176. The lane's own row
for this page is `S002` (`corpus/SOURCES.md:15`), untouched.

## F10 — Prior independent record (re-derived, not relied on)

`corpus/lessons/round-68.md:105`:
`| S176 | payload-absent | agentskills.io/client-implementation/adding-skills-support.md | refused — the quoted span was not located on the page this round fetched |`
and `corpus/lessons/round-70.md:111` lists S176 among the 7 `payload-absent` rows. I re-ran the
fetch and the probes myself (F2–F5); the prior record agrees with my observation but is not its
source.

## Calibration notes

- **Class:** `absent` for the quote cell (fabrication class for the quotation), with the register's
  own prose cell — "cited source, companion URLs and local artifacts were all checked; the quote is
  in none of them" — **accurate** as of my fetch. This is a self-declared absence, so the honest
  score is "confirmed", not "caught".
- **Not `unverifiable-class`:** the row's class cell is `payload-absent`, not a "could not be
  fetched" prose cell, and I reached the source, so the unverifiable branch does not apply.
- **Not `unreachable`:** HTTP 200 on the `.md`, the plain HTML and all archive fetches.
- **Slice defect (routed, not mine to fix):** the slice's `awk`/cut keeps only the first physical
  line of a wrapped register row, so this row reached the wave with a mid-cell fragment. A seat
  reading only the slice cannot know the cell ends "…disclosure table and the two" (F1).
- **Residual:** the register cell is itself dangling ("and the two") and the register's own author
  truncation cannot be recovered from any artifact I found; I do not guess what followed.

## Hygiene

Nothing edited: no committed lane file, no fleet repo, no `shokuknow` file, no jj state, no lane Git
index. Writes: this report only. Scratch `mktemp -d /tmp/k72w1-ExecQuar05.rZee` deleted before
return. No tool installed or upgraded (no install needed). No subagent dispatched. Longest single
command wall time: 4.2 s (three archive fetches in one loop), far under the 120 s / 4-process cap.
