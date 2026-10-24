# RevW2S120Reopen — round 64, wave 2 (kotoba, hyaku run 5)

Seat: `kotoba-r64.RevW2S120Reopen-2` (reviewer, independent leaf). Date: 2026-10-24.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Measured tip
`c019919c97ab5fe98e87a7754b4449ea4e699c99` (base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`).
Assignment: independently re-open S120 (`https://arxiv.org/html/2102.11378`, default request
profile), record status/bytes/sha256, compare with `.ufo/waves/round-64/snapshots/S120.page`
(committed sha `15963c3e67b5…`), test the three Gate quotes as substrings of the live bytes and of
the snapshot, check the row's anchor cell and teaches cell.

**Write bounds honored.** Read-only outside this file. Scratch under `/tmp/s120live/`. No git/jj
write, no production file touched, no subagent. **No tool installed or upgraded** (nothing was
needed; pacman untouched).

---

## Verdict

**Identity, freshness and quote support: ROW STANDS — live bytes are byte-identical to the
committed snapshot (same size, same hash), and all three Gate quotes resolve in both.** The
byte-identity survives a cache-busted fetch (`x-cache: MISS, MISS, MISS`), so it is origin
identity, not CDN-cache identity.

**Two landed cell/section defects, both one-line fixes already written verbatim by wave-1 seats
and neither applied nor dispositioned: row NEEDS CORRECTION** on (F1) the `teaches` cell's
section locator and (F2) the blank line splitting the registry table. The row's `tier`,
`scope`, `anchor` evidence, `status` and `used-by` stand unchanged. Tier inflation: **none in
the teaches cell** (checked below).

---

## 1. Live re-open (default request profile)

```
$ curl -sS -o S120.live.html -w 'http_code=%{http_code}\n...' https://arxiv.org/html/2102.11378
http_code=200
content_type=text/html; charset=utf-8
size_download=571600
curl_exit=0
$ wc -c S120.live.html      → 571600
$ sha256sum S120.live.html
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8
```

Response headers (`curl -sSI`, same URL):

```
HTTP/2 200            server: Google Frontend
last-modified: Mon, 24 Aug 2026 19:56:57 GMT
etag: "CMD775uGupYDEAE="
x-cache: MISS, HIT, HIT        age: 151340
content-length: 571600
```

The first fetch was a shared-cache HIT (~42 h old), so I re-fetched cache-busted
(`-H 'Cache-Control: no-cache' -H 'Pragma: no-cache' 'https://arxiv.org/html/2102.11378?r64probe=20261024'`):

```
http=200 bytes=571600 ct=text/html; charset=utf-8
x-cache: MISS, MISS, MISS      age: 1
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8  S120.bust.html
cmp S120.bust.html S120.live.html → BYTE_IDENTICAL   (exit 0)
```

Identity in the bytes: `arXiv:2102.11378v2 [cs.SE] 26 Feb 2021` (line 255), `/abs/2102.11378v2`
back-link (line 135), authors `Goran Petrović`, `Marko Ivanković`, `Gordon Fraser`, `René Just`
(lines 262–271). This is the titled paper, v2 — not 2103.02722, not the ICSE paper.

## 2. Same size? Same hash? — yes to both

```
$ sha256sum .ufo/waves/round-64/snapshots/S120.page
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8
$ wc -c .ufo/waves/round-64/snapshots/S120.page        → 571600
$ git cat-file -p c019919:.ufo/waves/round-64/snapshots/S120.page | sha256sum
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8  -
$ git show HEAD:.ufo/waves/round-64/snapshots/S120.page | sha256sum   → same
$ git log --diff-filter=A -1 -- .ufo/waves/round-64/snapshots/S120.page
c019919c97ab5fe98e87a7754b4449ea4e699c99  2026-10-24 00:43:39 -0300
```

571,600 B and sha256 `15963c3e…` in four places: the live default fetch, the cache-busted fetch,
the committed blob at `c019919`, and HEAD. The snapshot has not drifted since it landed, and the
origin still serves exactly those bytes. Working tree is clean for both this snapshot and
`corpus/SOURCES.md` (`git status --porcelain` shows only ` M …/receipts/noharm-tip.txt` and
`?? .ufo/waves/round-64/w2/`).

## 3. The three Gate quotes — substring matrix

Quotes tested exactly as they are stored in the artifacts (apostrophe is U+2019 in the snapshot
and in the cells: `[0x2019]`), against the live bytes and the committed snapshot, at four
normalization levels:

| quote (word count) | anchor | raw | ws-collapsed | tag-stripped | tags+ws |
|---|---|---|---|---|---|
| Q1 `Mutation analysis assesses a test suite’s adequacy … systematically seeded into the tested program` (22) | `#abstract1.1`, lines 283-284 | 0 / 0 | **1 / 1** | 0 / 0 | 1 / 1 |
| Q2 `However, code coverage alone might be misleading, in particular when program statements are covered but the expected program outcome is not asserted upon` (23) | `#S1.p1.1`, quote starts line 324 | 0 / 0 | **1 / 1** | 0 / 0 | 1 / 1 |
| Q3 `Equivalent mutants, which are semantically equivalent to the mutated program, are a plague in mutation testing and cannot generally be detected automatically` (22) | `#S3.SS2.SSS2.p1.1`, lines 780-782 | 0 / 0 | **1 / 1** | 0 / 0 | 1 / 1 |

(column pairs are live / snapshot; every pair agrees because the byte streams are identical.)

- All three are ≤25 words. All three are present in both bodies **after collapsing the HTML
  source line breaks to single spaces** (Q1 breaks between `artificial`/`faults`; Q2 between
  `asserted`/`upon`; Q3 twice). None is a raw byte substring — that is the artifact's source
  wrapping, not a quote defect, and the round-64 lesson's `## Gate` declares the method
  ("`grep -c` with the whitespace-normalized form → 1 against the snapshot") for Q1 and records
  "line breaks joined with single spaces" for the support quotes. Raw-byte `grep -c` returns 0
  for every one of the three, so any future gate that tests raw bytes will false-red this row;
  record the normalization, do not "correct" the quote.
- The cited ids and line numbers resolve: `id="abstract1.1"` opens line 283 and its first
  sentence ends line 284; `id="S1.p1.1"` opens line 319 and the quoted sentence starts on 324;
  `id="S3.SS2.SSS2.p1.1"` opens line 780 and the quoted sentence runs 780-782, under the heading
  `III-B 2 Heuristics to Prevent Equivalent Mutants` (line 777) — so the row's `§III-B2` label for
  Q3 is the right section.

## 4. Anchor cell — names the snapshot and its sha

`corpus/SOURCES.md:132`, cell 7, verbatim tail:

```
… §III-B2 Heuristics to Prevent Equivalent Mutants `#S3.SS2.SSS2.p1.1` lines 780-782; journal
version IEEE TSE 48(10):3900-3912 issue Oct 2022 (online Aug 2021), DOI 10.1109/TSE.2021.3107634,
metadata from `curl -sS https://api.crossref.org/works/10.1109/TSE.2021.3107634` only — the IEEE
HTML was not opened; fetched 2026-10-24 (HTTP 200, 571,600 B, sha256
`15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`); snapshot
`.ufo/waves/round-64/snapshots/S120.page`
```

- Snapshot path: named and exact. Sha256: named, full 64 hex, and equal to the measured bytes.
  Byte count `571,600 B` equals `wc -c`. Access date `2026-10-24` and `HTTP 200` reproduced.
- Version/date `v2 (26 Feb 2021)` matches the page's own version line; line numbers resolve (§3).
- Row shape intact: `awk -F'|'` on the row → `NF=13` (11 cells), no `|` inside cells, at the
  measured tip as well as in the working tree.
- Journal metadata re-derived independently (`GET https://api.crossref.org/works/10.1109/TSE.2021.3107634`
  → HTTP 200, 6804 B): title `Practical Mutation Testing at Scale: A view from Google`,
  container `IEEE Transactions on Software Engineering`, `volume 48`, `issue 10`, `page
  3900-3912`, `published-print 2022-10-01`, DOI `10.1109/tse.2021.3107634`. Matches the anchor.
  Note for the record, not a defect: `published-online` is `null`; "online Aug 2021" is only
  derivable from Crossref's `created` = `2021-08-27` [INFERENCE: deposit/online-first date], and
  the anchor's stated provenance (Crossref only) still holds.

## 5. teaches cell — tier-inflation check

Cell 8, verbatim tail:

```
… "Mutation analysis assesses a test suite’s adequacy … systematically seeded into the tested
program" — mutant-kill is the adequacy witness, so a survivor on a covered branch is a lead that
its assertion is missing, not proof of a gap (equivalent mutants can be productive, §III-B2)
```

- **The load-bearing-branch application is not attributed to the paper.** The cell contains the
  word `branch` only inside `a survivor on a covered branch`; it names no arm, no guard, no
  `span_missing`, no lane instrument, and makes no claim about how the lane pins a branch. The
  `scope` cell carries the explicit disclaimer ("the lane's load-bearing-branch application is
  the lane's inference, not the paper's study object"), and the knowledge entry repeats it
  ("S120 supplies the frame … not the arm design"). The framing claim that *is* asserted
  ("mutant-kill is the adequacy witness") is Q1's own sentence, and "survivor ⇒ improve the
  suite" is the paper's abstract wording (`uses mutants as test goals to create or improve a
  test suite`). No inflation found on this axis.
- **One mis-cited locator inside the cell** — see F1.

---

## 6. Findings by severity

### F1 — MAJOR (landed): `teaches` cites `§III-B2` for a claim that section does not contain; the exact fix was written in wave 1 and never landed, and no disposition is recorded

`corpus/SOURCES.md:132` cell 8 ends `(equivalent mutants can be productive, §III-B2)`. Measured:

```
$ awk 'NR>=776 && NR<=845' S120.live.html | grep -c 'productive'     → 0   (exit 1)
$ grep -n '<h2' S120.live.html | awk -F: '$1<1913' | tail -1
1884:<h2 …><span class="ltx_tag ltx_tag_section">VI </span>…Related Work</…>
$ sed -n '1911,1916p' S120.live.html
<p id="S6.p3.1" …>Effectiveness for mutants is primarily defined in terms of redundacy and
equivalence. This approach fails to consider the notion that non-reduntant
mutants might be unproductive or that equivalent mutants can be
productive <cite …>[33]</cite>. From our experience, reporting
equivalent mutants has been a vastly easier problem than reporting unproductive
non-reduntant non-equivalent mutants.</p>
```

§III-B2 (`#S3.SS2.SSS2`, lines 776-845) says the opposite emphasis — equivalent mutants "are a
plague … cannot generally be detected automatically" and the section's subject is *preventing*
them; the word `productive` never appears in it. The "can be productive" clause lives in **§VI
Related Work, `#S6.p3.1`, lines 1911-1916**, and there it is a *reported* notion (citing `[33]`)
that the paper then qualifies from its own experience. The cell therefore cites bytes that check
a different proposition — the M95/M96 citation-imprecision class this round closes.

Not a new discovery: both wave-1 seats measured it and wrote the replacement verbatim —
`.ufo/waves/round-64/w1/ScribeSOURCESRow.md:46-68` ("R2 — the teaches cell attributes a caveat to
the wrong section … `$ grep -n 'can be productive' → no match (the text wraps: "can be\nproductive")`")
and `.ufo/waves/round-64/w1/RevSourcesGate.md:698-727` ("§III-B2 … holds the **plague** sentence,
and 'can be productive' lives in §VI Related Work"). Both give the same one-substring swap:

```
old: (equivalent mutants can be productive, §III-B2)
new: (equivalent mutants can be productive, §VI Related Work `#S6.p3.1`)
```

The landed bytes at `c019919` still carry `§III-B2`. No disposition exists: `grep -n
'III-B2\|S6.p3.1\|equivalent mutants can be' corpus/lessons/round-64.md LOG.md SCORECARD.md` →
no output. **Recommendation:** apply the recorded swap, and because the paper *reports* the notion
and then partly disagrees, prefer wording that marks it reported (e.g. `(equivalent mutants can
be productive — reported, §VI Related Work `#S6.p3.1`)`) or drop the parenthetical: the caveat the
lane actually uses is §III-B2's "plague / cannot generally be detected" sentence, and the
knowledge entry's `## Limits` already cites it correctly at `§3.2.2`.

### F2 — MAJOR (landed): the blank line at `corpus/SOURCES.md:131` splits the registry table; S120 renders outside it

```
$ awk 'NR>=129 && NR<=133 {printf "%d:[%s]\n", NR, substr($0,1,40)}' corpus/SOURCES.md
129:[| S118 | Claude Code Docs — How Claude remembers …]
130:[| S119 | ICMJE — Corrections and Version Control — h…]
131:[]
132:[| S120 | Practical Mutation Testing at Scale: A view…]
133:[]
$ grep -n '^## Registry\|^## Paths' corpus/SOURCES.md   → 10:## Registry / 134:## Paths
```

A blank line terminates a Markdown table, so in the rendered `corpus/SOURCES.md` the registry's
last row is S119 and S120 becomes a paragraph of pipes. The census cannot see it (E01–E12 are
line-based and the row is still inside `## Registry`), so a green census does not clear this row.
Also recorded in wave 1 with the same fix: `ScribeSOURCESRow.md:42-44` ("R1 — a blank line splits
the registry table … One-line fix: delete line 131") and `RevSourcesGate.md:691-693` ("Fix: delete
the blank line at `corpus/SOURCES.md:131`"). Deletion
changes no row byte; gate it with a "no blank line inside the registry table" check, since the
census cannot.

### F3 — LOW (informational): the quote is not a raw-byte substring

All three quotes return `0` under literal raw-byte search and `1` under whitespace-normalized
search (§3). The Gate declares the normalization for Q1 and the support quotes, so nothing is
misrepresented — but the row's own cells do not, and a raw-byte substring gate would false-red
it. Recommend one clause in the Gate/anchor convention ("HTML source line breaks joined with
single spaces"), not an edit to the quotes.

### F4 — LOW (informational): "online Aug 2021" is Crossref `created`, not `published-online`

Crossref carries `created: 2021-08-27T20:11:27Z` but `published-online: null`. The anchor's
"online Aug 2021" is therefore an interpretation of the deposit/online-first timestamp, not a
field value. It is not contradicted by anything I measured, and the anchor's "Crossref only"
provenance holds. [INFERENCE] if the anchor is edited for F1, write `online-first 2021-08` or the
Crossref field it derives from.

---

## 7. Residual risk

- **The URL is unversioned.** `https://arxiv.org/html/2102.11378` serves "latest"; today latest is
  v2, so the row's `v2 (26 Feb 2021)` label and the pinned bytes agree. If arXiv publishes v3, the
  same URL returns different bytes while the anchor still says v2. The `recheck: 180d` cadence and
  the sha pin are the guard; the row already names v2, so no edit is required today.
- **The paper is served through a shared cache.** Byte identity was proven twice (HIT, then
  cache-busted MISS×3); the second fetch is the origin evidence. `last-modified: 2026-08-24` on an
  artifact dated 2021 is the CDN's object timestamp, not a content revision.
- **Quote-support is at sentence granularity.** All three quotes are grounded, but none of them
  states the mutation-score caveat the row's `scope` avoids ("87.5% … not the traditional mutation
  score", §V-C) — the row correctly does not teach a kill rate, and I did not re-open that lane.
- **F1's substantive risk is small, its provenance risk is not.** No admitted knowledge entry rests
  on the parenthetical (the entry's `## Limits` uses §III-B2 correctly), so the mis-citation does
  not propagate a false fact; what it does is reproduce, in the row that closes the citation class,
  the exact defect two seats caught and the landing skipped.

## 8. Verification gaps (what I did not do)

- Default request profile only, per assignment. I did not re-probe `Accept: text/markdown`, the PDF,
  or the IEEE TSE HTML (the version trap is recorded in the lesson's Gate; the row claims Crossref
  only for the journal record).
- I did not run `scripts/sources-census.sh`. Both F1/F2 are invisible to it by construction, and a
  wave-2 census seat owns the full run; a green census here would not have changed the verdict.
- The `teaches` cell's surrounding prose (before the quote) was read in full; the `source` cell's
  "Fraser & Just" and the arXiv URL were checked against the page (authors confirmed at lines
  262-271) and treated as cosmetic per wave 1's R3.
- No `receipts/` file exists for the S120 fetch (`.ufo/waves/round-64/receipts/` holds
  `C1-span-kill.txt`, `C1-span-measure.txt`, `C2-r64-measure.txt`, `noharm-tip.txt`); the fetch
  evidence lives in the row's anchor, the lesson's `## Gate`, and `ScoutS120.md`. Not a contract
  requirement, recorded as a gap only.

## 9. Command receipts (all exit 0 unless shown)

| # | command | result |
|---|---|---|
| 1 | `curl -sS -o S120.live.html -w … https://arxiv.org/html/2102.11378` | `http_code=200`, `size_download=571600`, `text/html; charset=utf-8` |
| 2 | `sha256sum S120.live.html` | `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8` |
| 3 | `curl -sSI …/2102.11378` | `x-cache: MISS, HIT, HIT`, `age: 151340`, `content-length: 571600` |
| 4 | `curl -sS -H 'Cache-Control: no-cache' …?r64probe=20261024` | `http=200 bytes=571600`, `x-cache: MISS, MISS, MISS`, `age: 1` |
| 5 | `cmp S120.bust.html S120.live.html` | `BYTE_IDENTICAL` |
| 6 | `sha256sum` + `wc -c` on snapshot | `15963c3e…`, `571600` |
| 7 | `git cat-file -p c019919:…/S120.page \| sha256sum` | `15963c3e…` |
| 8 | `git show HEAD:…/S120.page \| sha256sum` | `15963c3e…` |
| 9 | quote matrix (python, four normalizations × live/snapshot) | raw 0, ws 1 for all three |
| 10 | `awk -F'\|' … S120` on tip and worktree | `NF=13` |
| 11 | `awk 'NR>=776&&NR<=845' \| grep -c productive` | `0`, grep exit 1 |
| 12 | `grep -n '<h2'` before line 1913 | `1884 … VI … Related Work` |
| 13 | `sed -n '129,133p'` with line numbers | blank at 131 |
| 14 | `curl … api.crossref.org/works/10.1109/TSE.2021.3107634` | `http=200 bytes=6804`, vol 48 iss 10 pp 3900-3912, print 2022-10-01 |
