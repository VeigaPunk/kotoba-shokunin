# RevSourcesGate — round 64, wave 1 (kotoba, hyaku run 5)

Seat: `kotoba-r64.RevSourcesGate` (reviewer). Date: 2026-10-24. Base tip at dispatch:
`078eec4a1f6a41c64ff8806f58b46a67cd413bfc`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

Assignment: pre-review the planned S120 row and the sourced-claim linkage against the corpus
contract v1 — row shape, the Gate requirement, the sourced-claim requirement, and tier inflation.
Deliver a per-check verdict plus the exact row text that passes the census validator.

**Contract read.** `/home/vgpnk/Projects/shokunin/CORPUS.md:64-156` carries SOURCES contract v1 in
full (shape, rules 1–6, the frozen census block); the kaika campaign rules at `:157-184` carry the
provenance-trio rule. The maintained validator is `scripts/sources-census.sh` (E01–E12, W01–W04;
header `:24-33`). **Scripture vs. artifact:** the artifact wins. `corpus/SOURCES.md` was never
edited by this seat; every census run below is against a `/tmp` byte-copy of the live table with
the proposed row inserted.

**Write bounds honored.** I wrote exactly one file: this report. Scratch under `/tmp/r64src/`.
No git/jj write, no production file touched, no subagent dispatched, no tool installed.

---

## 0. Per-check verdicts (summary)

| # | Check | Verdict | Highest-severity defect found |
|---|---|---|---|
| 1 | Row shape (11 columns, no `|` in cells, enums, `mined` ⇒ used-by) | **PASS for the row text in §2; FAIL as drafted by `ScribeSOURCESRow`** | drafted row carries `<PENDING:…>` tokens in three cells and a `mined` status whose `used-by` targets do not exist (`g7-span-pinning-round64.md`, `round-64.md` both ABSENT) — E11 ×2 if landed today |
| 2 | Gate (URL, access date, ≤25-word quote for the row) | **NOT MET yet** — lesson Gate is a skeleton with 22 `PENDING` tokens | the lesson Gate repeats the plan's wrong candidate without recording the rejection; the three quotes that exist are all ≤25 words and all literal in the committed snapshot, so the Gate is fillable today |
| 3 | Sourced claim (C1 entry's trio cites S120; used-by paths exist at round end) | **PASS in entry revision 2 (§11.1); was FAIL in the first draft** | first draft located both quotes ~280 and ~257 lines away from where they are in the committed snapshot (`:40-52` chrome, `:524-527` §2.2 operator list) — the exact M95/M96 class C2 closes, reproduced inside the entry that closes it. Fixed to `#S1.p1.1` (line 324) / `#S3.SS2.SSS2.p1.1` (line 781); `verified-at:` now separates the 219 hash from the 223 hash, both real (MutW2V32.md:864 / :934) |
| 4 | Tier inflation (single paper: A or B) | **A is correct, with the scope narrowed — conditional PASS** | the drafted `scope` cell ("…for load-bearing guard branches…") attributes the lane's application to the paper; the paper never studies guard branches |

Root cause of 3 is a **version conflation**: three different artifacts were measured this wave and
their text does not cross (arXiv HTML v2 → the committed snapshot; arXiv PDF v2; IEEE TSE accepted
PDF). The quotes are only valid against the bytes that are cited. §4 pins the one artifact to cite.

---

## 1. Check 1 — row shape

### 1.1 Contract form, restated from the contract itself

`CORPUS.md:79-107`: 11 cells between the boundary bars, i.e. `awk -F'|'` → `NF=13`; "No `|` inside
any cell"; `kind` ∈ 10 values incl. `paper`; `tier` ∈ A/B/C "scoped to `scope`, never global";
`status` ∈ `queued|mined|rejected`, with `mined` = "cited by ≥1 path in `used-by`"; `anchor` = "exact
section / heading / page / line plus revision (version, commit, or publication date). Never a bare
homepage."

### 1.2 The drafted row (`ScribeSOURCESRow.md` §2)

Shape is right — the seat measured `NF=13` and decomposed all 11 cells (`:44-70`). Three defects,
all fatal at commit time:

1. **Placeholder tokens in production cells.** `<PENDING:size>`, `<PENDING:sha256>`,
   `<PENDING:snapshot-path>` in the `anchor` cell and `[quote: <PENDING:quote>]` in `teaches`. A row
   is a claim (`CORPUS.md:112`, rule 1); a row whose access evidence is a token is an unverified
   claim. The token count is the check: `grep -c '<PENDING' .ufo/waves/round-64/w1/ScribeSOURCESRow.md`
   → `12` — lines containing a token, not tokens (`grep -o` counts more). **Fix: zero tokens before
   the row lands.**
2. **`mined` with absent `used-by` targets.** Both paths are ABSENT today (evidence §4.4); the census
   prints `E11` ×2 and exit 1 (evidence §7.2). The seat acknowledges this (`:181-186`) and proposes
   the landing order; that is correct but the row must then land **`queued`/`—` first** and flip at
   round end, with the old→new flip logged in the lesson (rule 2, `CORPUS.md:113-114`).
3. **`anchor` locates the quote in a file that is not the cited bytes.** The drafted anchor names
   "§1 Introduction paragraph 2 (PDF p.1) and §3.2.2 (PDF p.5)" while the committed snapshot is an
   **HTML** document (`.ufo/waves/round-64/snapshots/S120.page`, 571,600 B, HTML/LaTeXML). A reader
   cannot resolve "p.5" in an HTML file, and the PDF the seat hashed (`728,951` B) is **not** the
   committed snapshot. Contract: "A quote names its location." **Fix: locate by HTML id + snapshot
   line, as in §4.**

Everything else in the drafted row is contract-clean: `kind=paper` valid, `tier=A` valid, no `|`
inside cells, `recheck=180d` a legal cadence, `opened=2026-10-24` a present ISO date, `id=S120` the
next unused (highest at base is `S119`, `corpus/SOURCES.md:130`).

### 1.3 Placement (this is a shape rule, not a nicety)

E12 fires for a row-shaped line outside `## Registry` (`scripts/sources-census.sh:620-624`; the
branch `next`s, so a misplaced row also skips E01/E11 — it hides its own defects). I hit it: appending
the row at EOF (after `## Search log`) printed `E12 S120 row outside Registry section` and exit 1.
**Insert directly after the S119 row (`corpus/SOURCES.md:130`), before the blank line and `## Paths`
at `:132`.** Registry table bounds: `## Registry` at `:10`, `## Paths` at `:132`.

---

## 2. The exact row text that passes the validator

Byte-exact, one line, 1,621 B, `NF=13`. Cite the artifact that was opened and quoted (the snapshot),
and name the journal record as Crossref metadata only — see §4 for why.

```
| S120 | Practical Mutation Testing at Scale: A view from Google (Petrović, Ivanković, Fraser & Just) — https://arxiv.org/html/2102.11378 | paper | A | Primary peer-reviewed study for the claim this row scopes: mutation analysis measures a test suite's adequacy by whether it detects seeded faults — so survival, not line coverage, locates an unasserted effect at covered code. Scoped to the paper's own statement; the lane's load-bearing-branch application is the lane's inference, not the paper's study object. Not a survey | arXiv:2102.11378v2 HTML (26 Feb 2021), the artifact opened and quoted: abstract `#abstract1.1` snapshot lines 283-284, §1 Introduction `#S1.p1.1` line 324, §III-B2 Heuristics to Prevent Equivalent Mutants `#S3.SS2.SSS2.p1.1` lines 780-782; journal version IEEE TSE 48(10):3900-3912 issue Oct 2022 (online Aug 2021), DOI 10.1109/TSE.2021.3107634, metadata from `curl -sS https://api.crossref.org/works/10.1109/TSE.2021.3107634` only — the IEEE HTML was not opened; fetched 2026-10-24 (HTTP 200, 571,600 B, sha256 `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`); snapshot `.ufo/waves/round-64/snapshots/S120.page` | "Mutation analysis assesses a test suite’s adequacy by measuring its ability to detect small artificial faults, systematically seeded into the tested program" — mutant-kill is the adequacy witness, so a survivor on a covered branch is a lead that its assertion is missing, not proof of a gap (equivalent mutants can be productive, §III-B2) | mined | 2026-10-24 | 180d | corpus/knowledge/g7-span-pinning-round64.md, corpus/lessons/round-64.md |
```

Note the apostrophe in `suite’s` is U+2019 in the snapshot; `teaches` reproduces it (the ASCII form
would still be a fair quote, but the byte-identical form is free).

**If the row must land before the entry and lesson:** replace the last three cells with
`| queued | 2026-10-24 | 180d | — |` and flip at round end with the flip logged (rule 2).

**If the L1 prefers the scribe's `source` cell** (`https://doi.org/10.1109/TSE.2021.3107634`), that is
also contract-legal — but then no quote may be attributed to the DOI record, because the IEEE HTML
was never opened by any seat this wave (scout: HTTP 202 WAF interstitial). The quote belongs to the
arXiv v2 artifact either way. My version keeps the opened URL in `source` because rule 1 says the row
is written after opening the source.

---

## 3. Check 2 — the Gate requirement

Rule 1 (`CORPUS.md:110-112`): "The round lesson's `## Gate` records, for every new row, the URL, the
access date, and a ≤25-word quote with its location grounding `teaches`."

**State today: NOT MET.** `ScribeLesson.md:124-134` is a skeleton — `URL: **PENDING (ScoutS120)** —
https://<PENDING — the URL actually opened; no URL is asserted here>`, "Accessed 2026-10-24", and 22
`PENDING` tokens file-wide (`grep -c PENDING .ufo/waves/round-64/w1/ScribeLesson.md` → `22`).

**Everything needed to fill it exists and is verified** (all three quotes are literal substrings of
the committed snapshot after `re.sub(r'\s+',' ')`; word counts by `wc -w`):

| # | quote | words | location in the committed snapshot | role |
|---|---|---|---|---|
| G1 | "Mutation analysis assesses a test suite’s adequacy by measuring its ability to detect small artificial faults, systematically seeded into the tested program" | **22** | `#abstract1.1`, lines 283-284 (**and the same file's `id="abstract1.1"`** is what the scout cites) | the gate quote — grounds `teaches`; this is the one the contract asks for |
| G2 | "However, code coverage alone might be misleading, in particular when program statements are covered but the expected program outcome is not asserted upon" | **23** | §1 Introduction, `#S1.p1.1`, line 324 (sentence continues on 325 before `<cite>`) | the coverage-vs-witness contrast |
| G3 | "Equivalent mutants, which are semantically equivalent to the mutated program, are a plague in mutation testing and cannot generally be detected automatically" | **22** | §III-B2, `#S3.SS2.SSS2.p1.1`, lines 780-782 | the caveat that keeps `teaches` honest |

G1 + G2 + G3 are all ≤25 words; the Gate can carry G1 as the required quote and G2/G3 as support, as
round 63 did with S119 (two quotes, `corpus/lessons/round-63.md:21-23`).

**Gate text that satisfies the rule and records the identity correction** (no `|` needed, prose is
free here; the round-63 Gate shape at `:21-24` is the template):

```
- **S120 — Practical Mutation Testing at Scale: A view from Google** (Petrović, Ivanković, Fraser,
  Just) — https://arxiv.org/html/2102.11378 — accessed 2026-10-24 (HTTP 200, 571,600 B,
  `text/html; charset=utf-8`, sha256
  `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`) — snapshot
  `.ufo/waves/round-64/snapshots/S120.page`.
  - `#abstract1.1` (snapshot lines 283-284) — "Mutation analysis assesses a test suite’s adequacy by
    measuring its ability to detect small artificial faults, systematically seeded into the tested
    program" — 22 words.
  - Rejected identifiers, both opened: `arXiv:2103.02722` is "A Markov jump process associated with
    the matrix-exponential distribution" (Peralta); `10.1109/ICSE43902.2021.00068` is "An Empirical
    Study on Deployment Faults of Deep Learning Based Mobile Applications" (Chen et al.). Neither is
    this work. The plan's "ICSE 2021" is the venue of a DIFFERENT paper by the same four authors
    ("Does mutation testing improve testing practices?", ICSE 2021, pp. 910-921); the journal record
    for this title is IEEE TSE 48(10):3900-3912 (Oct 2022), DOI 10.1109/TSE.2021.3107634, obtained
    from Crossref only — the IEEE HTML was never opened.
```

---

## 4. Check 3 — the sourced claim (C1 entry trio + used-by existence)

### 4.1 Trio presence — PASS in form

`ScribeEntry.md:15-17` opens the entry with `source:`, `verified-at:`, `recheck:` before any heading,
and `source:` names `S120` with the URL and anchors. That is the kaika rule
(`CORPUS.md:172-177`) and the r63 precedent (`corpus/knowledge/compound-clause-citation-round63.md:1-3`).
The entry also keeps the "what it does not rest on" discipline the r63 entry used ("the depth half
rests on … not on S119"): `ScribeEntry.md:15` names `MutW2V32.md` §11 for the arms. Good.

### 4.2 Trio content — **FAIL (critical): the anchors point at the wrong lines**

Measured against the committed snapshot (`sed -n`, `grep -n`):

```
$ sed -n '40,52p' .ufo/waves/round-64/snapshots/S120.page | cut -c1-60
  }                                     # … HTML chrome: reading-preferences JS, apple-touch-icon,
  // Run as soon as JS starts …          #    icon/png links, typekit CSS —
  …
$ grep -n "code coverage alone might be" .ufo/waves/round-64/snapshots/S120.page
324:to compute, and well supported by commercial-grade tools. However, code coverage alone might be misleading, in particular
$ sed -n '522,529p' .ufo/waves/round-64/snapshots/S120.page | cut -c1-100
<div id="S2.SS2.p4" class="ltx_para">     # the §2.2 mutation-OPERATOR list (AOR/LCR/ROR), not §3.2.2
$ grep -n "are a plague in mutation testing" .ufo/waves/round-64/snapshots/S120.page
781:are a plague in mutation testing and cannot generally be
```

So `S120.page:40-52` (cited for §1 Introduction) is head-chrome, and `:524-527` (cited for §3.2.2) is
the mutation-operator list; the real locations are **line 324** and **lines 780-782**. This is the
M95 / M96 citation class — a containing-file reference standing in for a located one — reproduced in
the very entry that closes the class. **Fix the `source:` line to:**

```
source: S120 — Petrović, Ivanković, Fraser & Just, "Practical Mutation Testing at Scale: A view from Google" (arXiv:2102.11378v2, 2021-02-26; opened artifact `https://arxiv.org/html/2102.11378`, snapshot `.ufo/waves/round-64/snapshots/S120.page`), abstract `#abstract1.1` (snapshot lines 283-284), §1 Introduction `#S1.p1.1` (line 324), §III-B2 `#S3.SS2.SSS2.p1.1` (lines 780-782); journal record IEEE TSE 48(10):3900-3912 (Oct 2022), DOI 10.1109/TSE.2021.3107634, from `curl -sS https://api.crossref.org/works/10.1109/TSE.2021.3107634` (metadata only — the IEEE HTML was not opened); internal evidence `.ufo/waves/round-63/w2/MutW2V32.md` §11 — the SM1–SM6 battery, the four measured arms and the 20 000-cell divergence note
```

### 4.3 Trio's venue claim — **FAIL: "venue not confirmed this round" is false as stated**

`ScribeEntry.md:15` says "venue not confirmed this round — the IEEE DOI link answered 202 with 0
bytes". The publisher HTML is indeed closed (WAF interstitial), but the venue is one command away and
I ran it:

```
$ curl -sS -o /tmp/r64src/crossref.json -w 'HTTP %{http_code} bytes=%{size_download}\n' https://api.crossref.org/works/10.1109/TSE.2021.3107634
HTTP 200 bytes=6804
$ python3 -c "import json; d=json.load(open('/tmp/r64src/crossref.json'))['message']; print(d['type'], d['container-title'], d['volume'], d['issue'], d['page'], d['published-print'])"
journal-article ['IEEE Transactions on Software Engineering'] 48 10 3900-3912 {'date-parts': [[2022, 10, 1]]}
```

Authors in the same record: Petrović, Ivanković, Fraser, Just — no Ernst. Leaving the venue
unconfirmed while the frozen plan asserts "ICSE 2021" leaves the wrong venue standing in the record.
Name the venue and cite Crossref; the plan's ICSE 2021 belongs to the sibling paper (§3).

### 4.4 used-by existence at round end — currently ABSENT (expected), and the two drafts agree

```
$ for p in corpus/knowledge/g7-span-pinning-round64.md corpus/lessons/round-64.md; do [ -e "$p" ] && echo "EXISTS $p" || echo "ABSENT $p"; done
ABSENT corpus/knowledge/g7-span-pinning-round64.md
ABSENT corpus/lessons/round-64.md
```

`ScribeSOURCESRow.md:144` and `ScribeEntry.md:4` both name `corpus/knowledge/g7-span-pinning-round64.md`
— the row's `used-by` and the entry's filename agree, which is the coupling that E11 tests. My earlier
suggestion (`span-missing-pinning-round64.md`) is superseded; **keep `g7-span-pinning-round64.md`,
because both drafts already use it.** The row and both targets must land in one commit, or the row
lands `queued` and flips.

---

## 5. Check 4 — tier inflation

### 5.1 Verdict: **A, with the scope narrowed.** Not inflation under this contract.

`CORPUS.md:95-99`: "**A**: primary or authoritative for that scope (spec, official docs, source code,
original paper, maintainer statement, the lane's own re-runnable gate output). **B**: strong secondary
(expert write-up with reproducible detail, survey, textbook)." An original peer-reviewed paper is
named in A. So A is not inflation *for a scope confined to what the paper itself states*. B would be
correct only if the row taught the paper's finding as a general law of testing across projects.

The class of inflation the census can see (`E10`, community-at-A) does not apply; the inflation this
row can actually commit is a **scope inflation**, and the drafted `scope` cell commits a mild form of
it: "mutant-kill as the witnessed-coverage signal for load-bearing guard branches" — the paper studies
Google's deployment and a statement-deletion example; it never studies guard branches, and it never
claims test-suite adequacy *for branches*. That phrase is the lane's application (C1's own object).
The row text in §2 states that separation in the cell itself ("the lane's load-bearing-branch
application is the lane's inference, not the paper's study object").

Secondary reasons A is defensible for the narrowed scope: the paper is the industrial-scale primary
report (more than 24,000 developers, more than 1,000 projects — abstract, verified in the snapshot:
`grep -c '24,000' → 1`), peer-reviewed in TSE, and the claim is the authors' own definition of the
measure. Not a survey (B's clause), not a `community` source (never A).

### 5.2 Precedent evidence: this is the registry's first `paper` row

```
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {k=$4; gsub(/[[:space:]]/,"",k); t=$5; gsub(/[[:space:]]/,"",t); n[k" "t]++} END{for(x in n) printf "%s=%d\n", x, n[x]}' corpus/SOURCES.md | sort
code A=4
community C=1
docs A=98
docs B=2
own-work A=4
spec A=8
$ awk -F'|' '… k=="paper" …' corpus/SOURCES.md      # (no output)
```

So there is no in-lane precedent for a paper row's anchor style. The two usable precedents are S118
(`docs`/A, vendor docs, `scope` carries a parenthetical limit: "(vendor documentation; not a runtime
test)") and S119 (`docs`/A, fetched timestamp + bytes + sha256 + snapshot path in `anchor`). The row
in §2 follows both, and adds the id-based locators the HTML artifact needs.

---

## 6. The version trap that produced the citation defects (evidence)

Three artifacts were measured this wave; their wording differs, so a quote copied from one into
another silently becomes a misquote:

| artifact | bytes | sha256 | quote wording |
|---|---|---|---|
| arXiv **HTML v2** — the committed snapshot | 571,600 | `15963c3e…` | "code coverage alone **might be misleading**… the expected program outcome is not asserted upon" |
| arXiv **PDF v2** (scribe's alternate profile) | 728,951 | `a9bdf441…` | same version as the HTML (v2) |
| IEEE **TSE accepted PDF** (my check) | 1,032,428 | `fa0423de…` | "code coverage alone **is insufficient and may give a false sense of efficacy**… their expected outcome is not asserted upon" |

Measured:

```
$ pdftotext S120.pdf - | tr -s '[:space:]' ' ' > flat.txt            # TSE accepted PDF
$ grep -qF "code coverage alone is insufficient and may give a false sense of efficacy" flat.txt && echo HIT
HIT
$ python3 - <<'EOF'  # against the COMMITTED snapshot
flat = re.sub(r'\s+',' ', re.sub(r'<[^>]+>',' ', html.unescape(open('.ufo/waves/round-64/snapshots/S120.page').read())))
print('TSE-variant' , 'code coverage alone is insufficient and may give a false sense of efficacy' in flat)  # False
EOF
TSE-variant False
```

Two consequences the L1 must not lose:
- **The row must hash the artifact it cites.** The scribe's anchor would hash the 728,951-B PDF; the
  committed snapshot is 571,600 B. My §2 row hashes the snapshot.
- **The PDF's two-column layout breaks literal quoting.** On the TSE PDF, `pdftotext -layout` MISSES
  two of three candidate sentences (columns interleave); the default mode and `-raw` hit all three.
  This does not affect the snapshot (HTML), but it does affect anyone who re-verifies against a PDF:
  the Gate must name the extraction mode. For the snapshot the check is `grep -F` on the raw file
  with `tr -s '[:space:]' ' '` applied to the line, or `python3 -c` with `re.sub(r'<[^>]+>',' ')`
  first (tags split sentences).

---

## 7. Real command output — the checks that must pass, and that can fail

### 7.1 Proposed row (the §2 bytes), against a `/tmp` byte-copy of the live table

```
$ awk -F'|' '{print NF}' /tmp/r64src/row-v2.txt
13
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
118                     # 117 at base + S120
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0                       # malformed rows: none
$ awk -F'|' '… tier histogram …' corpus/SOURCES.md
A=115 B=2 C=1           # S120 counted A
$ awk -F'|' '… status histogram …' corpus/SOURCES.md
mined=110 queued=7 rejected=1
$ awk -F'|' '… duplicate ids …' | sort | uniq -d
                        # empty
$ awk -F'|' '… enum + tier-inflation …' corpus/SOURCES.md
                        # empty: paper valid, A valid, mined valid, no community+A
$ awk -F'|' '… mined used-by existence …' | while read p; do [ -e "$p" ] || echo "missing: $p"; done
                        # empty — with both targets present (round-end state)
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
      --root /tmp/r64src/t/fleet-v2 --today 2026-10-24 /tmp/r64src/t/fleet-v2/kotoba-shokunin
kotoba-shokunin	ok	/tmp/r64src/t/fleet-v2/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

Baseline on the live lane, same command family (read-only, for the after-comparison):

```
$ bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin --today 2026-10-24 /home/vgpnk/Projects/shokunin/kotoba-shokunin
… 16 × W04 …                                            # same 16 the round-63 Gate records
kotoba-shokunin	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
$ bash scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin /home/vgpnk/Projects/shokunin/kotoba-shokunin
kotoba-shokunin	rows	117
kotoba-shokunin	tier.A	114 … tier.B 2 … tier.C 1
kotoba-shokunin	status.mined	109 … status.queued 7 … status.rejected 1
FLEET	missing	0
exit=0
```

Round-end expectation after the row lands: `rows 118`, `tier.A 115`, `status.mined 110`, `missing 0`,
`E`-codes none.

### 7.2 The checks shown able to fail (mutants of my own row)

Each mutant was applied to a copy and re-validated with the same command; the row was otherwise
byte-identical. Contract `:184`: "A fix is shown able to fail before it counts."

```
M1 | paper | A |  → | paper | Z |        → mutlane	E06	S120 tier=Z
M2 | paper | A |  → | paperx | A |       → mutlane	E05	S120 kind=paperx
M3 | paper | A |  → | community | A |    → mutlane	E10	S120 community-at-A
M4 mined … used-by two paths → mined … | — |  → mutlane	W03	S120 mined but unused
M5 teaches cell: "survival, not line coverage" → "survival | not line coverage"
                                         → mutlane	E01	S120 fields=12
```

Landing-order control (the same row, `mined`, with the two targets absent):

```
kotoba-shokunin	E11	S120 missing used-by corpus/knowledge/g7-span-pinning-round64.md
kotoba-shokunin	E11	S120 missing used-by corpus/lessons/round-64.md
exit=1
```

and the same bytes as `queued | 2026-10-24 | 180d | —`:

```
kotoba-shokunin	ok	…/corpus/SOURCES.md
exit=0
```

Placement control (row appended after `## Search log`):

```
kotoba-shokunin	E12	S120 row outside Registry section
exit=1                        # and no E11 for the same row — E12 short-circuits the row's other checks
```

### 7.3 Snapshot identity

```
$ wc -c .ufo/waves/round-64/snapshots/S120.page
571600 .ufo/waves/round-64/snapshots/S120.page
$ sha256sum .ufo/waves/round-64/snapshots/S120.page
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8  .ufo/waves/round-64/snapshots/S120.page
$ grep -o 'arXiv:2102\.11378v[0-9]*' .ufo/waves/round-64/snapshots/S120.page | head -1
arXiv:2102.11378v2
```

Matches `ScoutS120.md` § "Opened source" exactly (same URL, same byte count, same digest, plus a
byte-identical `export.arxiv.org/html/2102.11378v2` confirmatory fetch).

---

## 8. Findings, by severity

**F1 (blocker, check 2).** The lesson's `## Gate` cannot ship as a skeleton: `ScribeLesson.md:124-134`
carries `URL: PENDING`, 22 `PENDING` tokens file-wide, and repeats the plan's wrong candidate with no
rejection recorded. Contract rule 1 makes the Gate the row's only access evidence; without it the row
is an unbacked claim. Fill from §3, whose quotes are already verified literal in the committed
snapshot.

**F2 (blocker, check 3 — citation class).** `ScribeEntry.md:15` mis-locates both quotes:
`S120.page:40-52` is HTML chrome (real: line 324, `#S1.p1.1`) and `:524-527` is §2.2's mutation-operator
list (real: lines 780-782, `#S3.SS2.SSS2.p1.1`). This is the M95/M96 class C2 exists to close,
reproduced inside the entry that closes it. Use the replacement line in §4.2.

**F3 (major, check 1).** `ScribeSOURCESRow.md` §2's row carries `<PENDING:…>` in `anchor` and
`teaches`; it must not land with a single token. Replace with the §2 row (1,621 B, validator clean).

**F4 (major, check 3).** "venue not confirmed this round" (`ScribeEntry.md:15`) is false as stated —
Crossref returns the venue, volume, issue, pages and author list in one command (§4.3). Unconfirmed
venue + the plan's wrong "ICSE 2021" leaves the record contradictory; name TSE 48(10):3900-3912 and
attribute ICSE 2021 to the sibling paper.

**F5 (major, check 4).** Tier A is correct; the drafted `scope` cell inflates it by attributing
"load-bearing guard branches" to the paper. The narrowed wording is in §2. Tier must not be raised
(no A+), and B is not required: B describes surveys/secondary write-ups, which this is not.

**F6 (major, consistency).** Three different artifacts are being quoted across the wave (snapshot
571,600 B; arXiv PDF 728,951 B; TSE PDF 1,032,428 B) and their wording differs (§6). The row, the
entry and the Gate must all name the snapshot's digest and locate quotes by HTML id, or the Gate's
"quote is literal" claim is false for whoever re-checks against a different file.

**F7 (minor, search log).** `ScribeSOURCESRow.md` §4's search-log note counts "Identified 6; screened
6" but does not screen the **two wrong plan identifiers** (Peralta's Markov paper; Chen et al.'s DL
mobile-fault study) that rule 5's honesty clause most needs recorded — the plan named them. Count
them: identified 8 / screened 8 / included 1 / excluded 7, with the two identifiers rejected as
"wrong work" (they are, measurably: §9). Also: the note says "arXiv record and PDF for
arXiv:2102.11378 (v2, fetched twice byte-identical)" while the snapshot is the **HTML**; name the HTML
as the snapshot and the PDF as an alternate profile (the scout's own report already distinguishes
them).

**F8 (minor, note).** `ScribeSOURCESRow.md:44-70` decomposes 11 cells but numbers the `awk` fields
`[1]…[13]` starting at the empty left field; the cell numbering in the report's table is off by one
against that list. Harmless in the report, but the L1 should not copy the decomposition as the row's
field map.

**F9 (minor, scope boundary for the wave's honesty).** The C1 knowledge entry rests on the lane's own
verifier bytes for the arms; S120 warrants only the method. `ScribeEntry.md:15` already says this for
`MutW2V32.md` §11; the row's `scope` cell must not be read as endorsing the 223-assertion receipt.
That belongs to C1's own review (`RevC1Predicate`), and I make no claim about it.

---

## 9. Findings that falsify a frozen-plan line (record as plan erratum, do not edit the plan)

`plans/round-64.md` § Sources: "candidate: Petrovic, Ivankovic & Ernst, 'Practical Mutation Testing at
Scale', ICSE 2021 — scout opens, snapshots, quotes ≤25 words". All three identifiers are wrong except
the title, and each was opened:

```
$ curl -sS -L https://arxiv.org/abs/2103.02722  → title: "A Markov jump process associated with the
  matrix-exponential distribution" (Peralta)                     # HTTP 200, 39,320 B
$ curl -sS -L https://doi.org/10.1109/ICSE43902.2021.00068 → HTTP 202, 0 B, lands on IEEE doc 9401981;
  Crossref for that DOI: "An Empirical Study on Deployment Faults of Deep Learning Based Mobile
  Applications", Chen et al., ICSE 2021, pp. 674-685
$ curl -sS https://api.crossref.org/works/10.1109/TSE.2021.3107634 → journal-article, IEEE TSE,
  48(10):3900-3912, 2022-10-01; authors Petrović, Ivanković, Fraser, Just
```

The corpus record must carry the correction (row + Gate + lesson M-row); the plan stays frozen. The
scout reached the same conclusion independently (`ScoutS120.md` § Verdict), which is corroboration,
not shared provenance.

---

## 10. Residual risk and verification gaps

- **Not run:** the live `corpus/SOURCES.md` was never modified, so no census ran against it; every
  receipt in §7 is against a `/tmp` byte-copy with the row inserted. Re-run the block after the L1
  applies the row and both `used-by` files exist — the gate that must print `118 / 0 /` no `missing:`
  and no `E`-codes.
- **Coupling not yet discharged:** the entry filename `corpus/knowledge/g7-span-pinning-round64.md`
  appears in both drafts and in the row's `used-by`; if either draft is renamed, E11 fires. Verify the
  three strings agree at landing (`grep -c g7-span-pinning-round64 corpus/SOURCES.md` → 1 in the row).
- **Version risk if a re-fetch is used:** arXiv HTML can be re-rendered (the snapshot's
  `last-modified` is 2026-08-24, after the v2 date). Any re-fetch that changes the digest invalidates
  the Gate's byte claim; the Gate should pin the digest *and* the access date, and treat a later
  different render as version drift (S119's Q56 shape, `corpus/lessons/round-63.md:16-19`).
- **Unverified by me, by scope:** C1's four arms and the 223-assertion receipt (RevC1Predicate);
  C2's counter (RevC2Checks); the entry's `verified-at:` hash `12d093a1…`; whether `Q60`'s proposed
  row text lands (ScribeQ60). I make no gate claim on any of them.
- **One inference, labelled:** that the arXiv v2 HTML and the IEEE TSE article are the same work is
  an identity inference, not an opened equivalence — the abs page says only "submitted to the IEEE"
  and the IEEE HTML never opened. The row therefore cites the arXiv record as the artifact and the
  DOI as metadata; that is the honest form until someone opens the TSE HTML ([INFERENCE]).

## 11. Addendum — post-write re-check (the entry draft moved while this report was being written)

`ScribeEntry` published a revised trio after §4 above was measured. Status changes, so the L1 does not
apply a stale finding:

| finding | status now | evidence |
|---|---|---|
| F2 (mis-located anchors `:40-52`, `:524-527`) | **RESOLVED in the current draft** | `ScribeEntry.md:15` now cites `S120.page:S1.p1.1` and `S120.page:S3.SS2.SSS2.p1.1`; both ids exist and contain the quotes: `grep -n 'id="S1.p1.1"\|id="S3.SS2.SSS2.p1.1"\|id="abstract1.1"' .ufo/waves/round-64/snapshots/S120.page` → `283:…abstract1.1`, `319:<p id="S1.p1.1" …`, `780:<p id="S3.SS2.SSS2.p1.1" …`. The quote sits at line 324 inside the `S1.p1.1` paragraph (319-326) and at 781 inside `S3.SS2.SSS2.p1.1` (780-782). The earlier revision's `:40-52`/`:524-527` are recorded in §4.2 as the measured before-state. |
| F4 (venue unconfirmed) | **RESOLVED in the current draft** | `ScribeEntry.md:15` now names "IEEE TSE 48(10):3900-3912 (2022), DOI 10.1109/TSE.2021.3107634" — the Crossref identity (§4.3). |
| F1 (lesson Gate skeleton) | **OPEN** | unchanged: 22 `PENDING` tokens in `ScribeLesson.md`. |
| F3 (`<PENDING:…>` in the row) | **OPEN** | unchanged in `ScribeSOURCESRow.md` §2 (12 token lines). |
| F5 (scope inflation in the row's `scope` cell) | **OPEN** | the §2 row text above is the narrowed form. |
| F6 (three artifacts, divergent wording) | **OPEN** | pin to the snapshot digest `15963c3e…`; §6. |

Two precision requirements the revised trio still needs:

1. **Anchor locators should be line-anchored as well as id-anchored.** "verified at byte offsets" is
   not re-checkable without the offset arithmetic; the id plus the snapshot line range is. Exact
   ranges in the committed bytes (`.ufo/waves/round-64/snapshots/S120.page`):
   abstract `#abstract1.1` = lines **283-284**; §1 `#S1.p1.1` = paragraph at **319**, quoted sentence
   at **324** (continues on 325, then `<cite>` markers `[2], [3]`); §III-B2 `#S3.SS2.SSS2.p1.1` =
   **780-782**.
2. **If the row's `source` cell stays the DOI URL, the `anchor` cell must say the DOI record is
   Crossref metadata only and the IEEE HTML was never opened.** Otherwise the row implies a publisher
   page was read, which no seat did (scout: HTTP 202 WAF interstitial). This is the one place the
   entry (preprint snapshot) and the row (DOI URL) could drift: both name arXiv:2102.11378v2 and the
   same two sections, so they are consistent **as long as** the row's quote and digest are attributed
   to the snapshot and not to the DOI. My §2 row puts the opened arXiv URL in `source` and the DOI in
   `anchor` as metadata-only — that spelling cannot drift.

### 11.1 Revision 2 verified (entry trio now passes check 3)

`ScribeEntry.md` fenced block lines 18-20 (`sed -n`, verified 2026-10-24):

```
source: S120 — Petrović, Ivanković, Fraser & Just, "Practical Mutation Testing at Scale: A view from
  Google", IEEE TSE 48(10):3900-3912 (2022; Crossref metadata, publisher HTML not opened), DOI
  10.1109/TSE.2021.3107634; preprint arXiv:2102.11378v2 (26 Feb 2021), §1 (`S120.page:S1.p1.1`,
  quote at line 324) and §3.2.2 (`S120.page:S3.SS2.SSS2.p1.1`, line 781), committed snapshot
  `.ufo/waves/round-64/snapshots/S120.page` (571,600 B, sha256 `15963c3e…`); internal evidence
  `.ufo/waves/round-63/w2/MutW2V32.md` §11 …
verified-at: 2026-10-24 — base `078eec4`, v32 sha256 `12d093a1…`: `self-test: 0 failure(s) over 219
  assertions`, exit 0 (re-run by this seat); 223 on `landed_plus_spanfix7` (sha256 `ae84673e…`) per
  MutW2V32 §11; branch at `verifiers/check_scoped_rules_v32.py:1055-1067`
recheck: 180d — `python3 -B verifiers/check_scoped_rules_v32.py --self-test`: all four printed lines
  and the assertion count against § The measured record; sooner on any mutation reported surviving
  this branch
```

Both hashes are real and correctly separated — `MutW2V32.md:864` carries `12d093a1…` with 219
assertions, `:934` carries `ae84673e…` as `landed_plus_spanfix7` (the 223 file). F2, F4 and the
sha-contradiction I flagged in the IRC thread are **resolved**; the line numbers 324/781/283-284 are
the ones this seat measured. Nothing in the trio now needs a plan edit — the plan erratum (F, §9)
still does.

### 11.2 Ruling on the entry-snapshot vs row-DOI question

The two spellings are both contract-legal, so the answer is a disclosure requirement, not a
preference: with the DOI in the row's `source`, the row's `anchor` must carry
"(Crossref metadata, publisher HTML not opened)" — the same clause the entry now uses — and the
quote + digest must stay attributed to `arXiv:2102.11378v2`. I verified this spelling too: a row with
`https://doi.org/10.1109/TSE.2021.3107634` as `source` is `NF=13`, validates exit 0, and produces the
same E11 landing-order behaviour (`/tmp/r64src/row-mined.txt` and `t/SOURCES.mined.md` receipts in
§7). My §2 row prefers the opened URL in `source` only because rule 1 defines the row as a record of
the source opened this round; either way the DOI record is never a quote's provenance.

## 12. Addendum 2 — the row as filled (`ScribeSOURCESRow` revision) and the search-log placement ruling

### 12.1 The filled row passes, with two open items

`ScribeSOURCESRow.md:45` now carries the filled row (no tokens in the canonical copy; id anchors
`abstract1.1` + `S3.SS2.SSS2.p1.1`; snapshot 571,600 B / `15963c3e…`; "journal version … Crossref only,
not opened"). I re-ran the validator against a mirrored lane root with those exact bytes:

```
$ awk -F'|' '{print NF}' /tmp/r64src/row-scribe-final.txt
13
$ … validate --root /tmp/r64src/t/fleet-scribe --today 2026-10-24 …/kotoba-shokunin
kotoba-shokunin	E11	S120 missing used-by corpus/knowledge/g7-span-pinning-round64.md
kotoba-shokunin	E11	S120 missing used-by corpus/lessons/round-64.md
exit=1                        # targets absent — the expected landing-order state
$ … same command after creating the two targets
kotoba-shokunin	ok	…/corpus/SOURCES.md
exit=0
```

Enum/tier-inflation: empty. So F3 (tokens) and F6 (one-artifact pin) are **closed** in the canonical
row — the digest and the ids are the snapshot's, and the DOI carries the Crossref-only disclosure,
which is exactly the condition §11.2 set for keeping the DOI in `source`.

Two items remain open in that row:

1. **F5 stands**: cell 5 still reads "…for load-bearing guard branches…", attributing the lane's
   application to the paper. Use the narrowed scope from §2 (or the equivalent: state that the
   branch application is the lane's inference).
2. **Stale duplicate landing hazard**: the report still carries the *old placeholder* row at
   `ScribeSOURCESRow.md:70` (PDF-page anchors and a `<PENDING…>` tail), and the two lines differ
   (`diff` → DIFFERENT). Only `:45` is current. Mark `:70` superseded, or the L1 can paste the line
   that carries the tokens this review told it to drop.

### 12.2 Search-log placement — the scribe's read is right; I add the measured reason

Contract shape (`CORPUS.md:76-84`): `## Search log` holds "one prose note per bounded search";
`## Leads (unopened)` is bullets only ("a lead is not evidence and never a row"). Measured state of
the live file:

```
$ grep -n "^## Search log\|^## Leads" corpus/SOURCES.md
150:## Search log
202:## Leads (unopened)
$ sed -n '218,222p' corpus/SOURCES.md
- **2026-10-23 — round-63 sources sweep (C2's repair method) and the S049 errata.**   ← under ## Leads
```

So the round-63 note is misfiled under the Leads heading — a real shape violation, inherited.

Ruling for round 64:

- Place **both** round-64 notes at the end of `## Search log`, i.e. after the last round-63 note's
  final line and **before line 202** (`## Leads (unopened)`). Do not split them.
- Do **not** move the round-63 note: rule 2 (`CORPUS.md:113-114`) allows only `status`, `recheck` and
  `used-by` to change in place, so relocating existing prose is a rewrite. Record the misfiling once
  in the round lesson's Gate/search-log paragraph, with the line numbers above.
- Appending at EOF is **not** equivalent even though no validator catches it: prose placement has no
  machine check at all. I probed it — a note inserted under `## Leads` left the validator at `ok
  exit=0`:

```
$ … validate (with a prose note added under ## Leads)
kotoba-shokunin	ok	…/corpus/SOURCES.md
exit=0
```

That blindness is why this rule has to be held by the human/diff review, and why the scribe's
recommendation (Search log end, one recorded misfiling) is the one to follow rather than the
"acceptable alternative".

### 12.3 Ruling on F5 — the `scope` reading, and why the apply-as-is cell should flip

The scribe's contract reading is half right, and the half it gets right is what makes the fix cheap.
`CORPUS.md:100` defines `scope` as "the claim or topic the tier applies to" and `:95` says tier is
"scoped to `scope`, never global" — so `scope` is the **locus of trust**, not a paper summary. Agreed.
But a locus is only as good as the claim standing on it: A's warrant is "original paper", and that
warrant reaches exactly the proposition the paper establishes. "mutant-kill as the witnessed-coverage
signal for load-bearing guard branches" is not that proposition — the paper's units are changelists,
files and mutated statements, and it never studies guard branches. So the apply-as-is cell asserts A
for a claim the paper does not establish, which is inflation in the only sense this check can catch.

Three reasons the bound belongs in `scope` and not only in `teaches`:

1. **The lane's own precedent puts it there.** S118's `scope` is "Current Claude Code `.claude/rules/`
   `paths` frontmatter matching syntax (vendor documentation; **not a runtime test**)" — the parenthetical
   is a bound inside `scope`. The convention exists; this row is the outlier.
2. **A tier reviewer reads `scope`.** `tier` is defined relative to `scope`, so a non-author spot-check
   (rule 1's "Non-author verification re-opens a sample") grades the tier against `scope`; if the bound
   lives only in `teaches`, the tier claim is unreviewable at the cell it is defined against.
3. **`teaches` has its own contract job** — "one grounded learner benefit" — and lengthening it to carry
   a scope limitation overloads a cell the census does not read for tier.

Cost of flipping, measured rather than asserted: the swap touches cell 5 only and changes nothing a
machine checks.

```
$ diff of the two spellings → cells 11 11 | differing cells: [5]
$ awk -F'|' '{print NF}' row-scribe-swap.txt
13
$ … validate --root /tmp/r64src/t/fleet-scribe (swap bytes, targets present)
kotoba-shokunin	ok	…/corpus/SOURCES.md
exit=0
```

**Verdict: flip the apply-as-is cell to the separating wording** (the scribe's §2.4 text is accepted
verbatim):

```
mutant-kill (detection of a seeded fault) as the test-suite adequacy witness the paper states, applied by the lane to load-bearing guard branches, and the equivalent-mutant caveat
```

If the L1 prefers the shorter repair instead of the scribe's phrasing, dropping only the words "for
load-bearing guard branches" from the existing cell does the same work with a smaller diff. Either
lands F5; the apply-as-is line does not.

## 13. Addendum 3 — the live row as the L1 applied it: two verified residuals, and the Gate now met

The L1 applied the §2 row of this report to `corpus/SOURCES.md:132`, landed
`corpus/knowledge/g7-span-pinning-round64.md` (trio correct, zero `PENDING`) and filled
`corpus/lessons/round-64.md` § Gate (zero `PENDING`). So **check 2 is now MET** and **check 3's entry
side PASSES**; both are re-verified below. Two residues remain in the live table, both invisible to the
validator, one of them mine.

### 13.1 R1 — the S120 row is outside the table block (confirmed)

```
$ awk 'NR>=129 && NR<=134 {printf "%d: %s\n", NR, ($0==""?"<BLANK>":substr($0,1,60))}' corpus/SOURCES.md
129: | S118 | Claude Code Docs — How Claude remembers your project — https://code.clau
130: | S119 | ICMJE — Corrections and Version Control — https://www.icmje.org/…
131: <BLANK>
132: | S120 | Practical Mutation Testing at Scale: A view from Google (Petrović, Iv…
133: <BLANK>
134: ## Paths
```

A blank line terminates a Markdown table, so S120 renders as a paragraph of pipes directly under the
registry rather than as its last row. The census cannot see this — it is line-based and stays `ok`
(`validate` → `ok`, exit 0 on the live file). **Fix: delete the blank line at `corpus/SOURCES.md:131`**,
which puts S120 immediately after S119.

### 13.2 R2 — my own `teaches` cell mis-cites the section (confirmed; the scribe found it)

Cell 7 currently ends `(equivalent mutants can be productive, §III-B2)`. Measured in the snapshot:

```
$ grep -c "equivalent mutants can be productive" .ufo/waves/round-64/snapshots/S120.page
0                       # it does not occur on any single line — the sentence wraps
$ python3 -c "…whitespace-normalized grep…"
HIT  | equivalent mutants can be productive
$ sed -n '1911,1913p' snapshot | sed -e 's/<[^>]*>//g'
<p id="S6.p3.1" …>Effectiveness for mutants is primarily defined in terms of redundacy and
equivalence. This approach fails to consider the notion that non-reduntant
mutants might be unproductive or that equivalent mutants can be
productive [33]. …
$ … nearest heading above 1911 …
(1884, 'VI Related Work')
$ sed -n '780,782p' snapshot | sed -e 's/<[^>]*>//g'
Equivalent mutants, which are semantically equivalent to the mutated program,
are a plague in mutation testing and cannot generally be
detected automatically.
```

So §III-B2 (`#S3.SS2.SSS2.p1.1`, lines 780-782) holds the **plague** sentence, and "can be productive"
lives in **§VI Related Work** (`#S6.p3.1`, lines 1911-1914). The cell's parenthetical is the M95 class —
a citation that resolves and checks different bytes — and it is **my text**, applied by the L1; the
scribe caught it, not me. Recorded as mine, not as a landing error.

**Fix (exact substring swap inside cell 7):**

```
old: (equivalent mutants can be productive, §III-B2)
new: (equivalent mutants can be productive, §VI Related Work `#S6.p3.1`)
```

### 13.3 The repaired table, validated (both fixes together)

Applied to a `/tmp` copy of the live file (blank removed, substring swapped) —

```
$ … lines 130-133 of the repaired copy
130 | S119 | ICMJE — Corrections and Version Control — https://www.icmje.o…
131 | S120 | Practical Mutation Testing at Scale: A view from Google (Petrović, I…
132 <BLANK>
133 ## Paths
$ awk -F'|' '/^\| S120 /{print "NF="NF; print "c7: "$8}' repaired
NF=13
c7:  "Mutation analysis assesses a test suite's adequacy … not proof of a gap (equivalent mutants can
     be productive, §VI Related Work `#S6.p3.1`)
$ … validate --root /tmp/r64src/t/fleet-live --today 2026-10-24 …/kotoba-shokunin
kotoba-shokunin	ok	…/corpus/SOURCES.md
exit=0
```

Table block contiguous, enums unchanged, `NF=13`, validator clean. Nothing else in the live row needs a
change: cell 5 already carries the narrowed scope, cell 6 the snapshot digest and id anchors, cell 11
the two `used-by` paths, and both targets exist.

### 13.4 Gate, landed — MET

`corpus/lessons/round-64.md:16-28` now records the URL (`https://arxiv.org/html/2102.11378`), the access
date (2026-10-24), the HTTP status, the byte count, the sha256, the snapshot path, and the gate quote
with its location and word count (`#abstract1.1`, lines 283-284, 22 words, substring check recorded).
Zero `PENDING` in the lesson and zero in the entry. That satisfies rule 1 as written; the only thing I
would add is the explicit rejection of the plan's two wrong identifiers (§3 supplies the wording), so
the round records *why* the candidate changed rather than only what replaced it.

## 14. Tool installs

None. No pacman/uv/cargo/npm transaction, nothing written to `~/.local/bin`. Tools used were already
present: `curl`, `sha256sum`, `awk`, `grep`, `sed`, `wc`, `bash`, `python3`, `pdftotext`/`pdfinfo`
(poppler). The host-wide pacman pause was not approached.

## 15. Artifacts

- This report: `.ufo/waves/round-64/w1/RevSourcesGate.md`
- Proposed row bytes: `/tmp/r64src/row-v2.txt` (1,621 B) — reproduced verbatim in §2
- Census fixtures: `/tmp/r64src/t/fleet-v2` (round-end state), `/tmp/r64src/t/fleet-mined` and
  `fleet-queued` (landing-order controls), `/tmp/r64src/t/fleet-final` (earlier variant)
- Fetched bytes: `/tmp/r64src/S120.pdf` (TSE accepted, `fa0423de…`), `/tmp/r64src/crossref.json`,
  `/tmp/r64src/abs-2103.02722.html`, `/tmp/r64src/doi-icse.html`
- Read-only references: `CORPUS.md` (fleet root, `:64-184`), `scripts/sources-census.sh`,
  `corpus/SOURCES.md:1-20,127-132,202-245`, `corpus/lessons/round-63.md:10-40`,
  `corpus/knowledge/compound-clause-citation-round63.md:1-3`,
  `.ufo/waves/round-64/w1/{ScoutS120,ScribeSOURCESRow,ScribeEntry,ScribeLesson}.md`,
  `.ufo/waves/round-64/snapshots/S120.page`
