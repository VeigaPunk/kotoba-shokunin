# ScribeSOURCESRow — round 64 wave 1 (kotoba, hyaku run 5)

Seat: `kotoba-r64.ScribeSOURCESRow` (scribe). Date: 2026-10-24. Base tip at dispatch:
`078eec4a1f6a41c64ff8806f58b46a67cd413bfc`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

Assignment: draft the S120 registry row (11 columns, contract v1) and the search-log append for
`corpus/SOURCES.md`, `<PENDING:…>` tokens where ScoutS120's evidence lands, and prove the row parses
with the `awk NF==13` check.

**Write bounds honored.** I wrote exactly one file: this report. `corpus/SOURCES.md` and every other
production file are untouched; no git/jj write was run. Scratch is under `/tmp/s120/`. No tool was
installed (no pacman, uv, cargo or npm transaction — the pacman guard was not approached).

**What changed mid-seat.** Two things. (a) `ScoutS120.md`, `ScoutS120Alt.md` and `ScoutS049.md`
landed while I was working, so the row is delivered **filled**, not tokenized: §2 is the apply-as-is
line, and the tokenized form the assignment asked for is kept in §2.3 for the record. (b) **The L1
applied its own S120 row to the live table at 00:5x** (line 132, after a blank line at 131) and both
`used-by` files landed, so the live table is now `ok`, exit 0. My row is no longer an insert — it is
a **reviewed variant**, and what this report owes the L1 is the verification of the live bytes plus
the residuals I can prove against them (§0.1).

## 0. Live state at hand-off, and the three residuals

`corpus/SOURCES.md` now carries an S120 row that is **not mine** (source cell points at the arXiv HTML
rather than the DOI; scope cell carries the bound as prose). It is a good row: its ids and its
snapshot line numbers check out against the committed snapshot, its scope cell already lands the
reviewer's F5 (the lane's branch application is marked as the lane's inference, not the paper's study
object), and its `used-by` paths both exist. Live receipts:

```
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
118
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {print "MALFORMED line "NR": NF="NF}' corpus/SOURCES.md
                        # none
$ scripts/sources-census.sh validate . --today 2026-10-24 | grep -v W04
kotoba-shokunin	ok	…/corpus/SOURCES.md
exit=0
```

Three residuals against those bytes, all proved, none of them machine-caught:

**R1 — a blank line splits the registry table.** Line 131 is empty, so S120 begins a new block. The
validator is line-based and stays `ok`; a Markdown renderer ends the table at the blank line, so the
row renders outside the table. One-line fix: delete line 131.

**R2 — the teaches cell attributes a caveat to the wrong section.** The cell reads
"… (equivalent mutants can be productive, §III-B2)". In the committed snapshot the plague sentence is
at §III-B2 (`S3.SS2.SSS2.p1.1`, line 780), but the clause "equivalent mutants can be productive [33]"
is in **§VI (Related Work)**, snapshot lines 1911–1914:

```
$ grep -n 'can be productive' …/S120.page      → no match (the text wraps: "can be\nproductive")
$ sed -n '1911,1914p' …/S120.page
  mutants might be unproductive or that equivalent mutants can be
  productive [33]. From our experience, reporting
$ awk (last ltx_title_section before 1914) → 1884: <h2 … III…> "VI"
```

This is the M95 citation-imprecision class, in a cell: §III-B2's own bound is the narrower "some
categories of equivalent mutants that can be accurately detected". **Ownership: RevSourcesGate wrote
the parenthetical and records it as its own defect (§13.2 of its report), not as a landing error.**
It reproduced my evidence independently (`grep` → 0 hits because the sentence wraps 1912–1913;
whitespace-normalized → hit; nearest heading above 1911 → `VI Related Work`; `#S6.p3.1` opens at
1911) and supplies the exact cell swap:

```
(equivalent mutants can be productive, §III-B2)
→ (equivalent mutants can be productive, §VI Related Work `#S6.p3.1`)
```

Its §13.3 applies both R1 and R2 to a `/tmp` copy and reports the table contiguous, NF=13, validator
`ok` exit 0 — so the pair is a one-line edit plus one cell, with no machine risk. I did not apply
either: the live row is not mine.

**R3 — cosmetic, recorded not fixed.** The source cell writes "Fraser & Just" where the paper prints
"Gordon Fraser, René Just", and it carries the arXiv HTML URL where the contract allows "canonical URL
or DOI". Neither is a finding; both are the kind of thing a later editor should not "correct" into a
different row.

**Disposition of my variant: do not apply it.** RevSourcesGate's ruling (IRC, 2026-10-24): the live
row is its own, its narrowed cell 5 already discharges F5, and applying my row would E03 on the
duplicate id *and* regress cell 5 to the bound-in-`teaches`-only form. §2.1 therefore stays as the
record of the alternative shape — DOI in `source`, paragraph ids instead of snapshot line numbers in
`anchor`, quote in the lesson rather than in `teaches` — not as a pending edit.

## 1. Behavior (what was actually done)

1. Read `plans/round-64.md` (C1, C2, § Sources), the frozen fleet contract
   `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (11 columns, rules 1–6, census block), and the lane's
   existing 117 rows (S001–S119) for cell style and the S119 anchor shape.
2. Verified the plan's candidate independently: two web searches, the arXiv abs record, the arXiv
   PDF fetched **twice**, and a Crossref query on the DOI — then read `ScoutS120.md` and compared.
3. Located the quotes the `teaches` cell needs, word-counted them, mapped them to PDF pages, and
   re-verified both against the scout's committed snapshot including their HTML paragraph ids.
4. Built the filled row in `/tmp/s120/row-filled.md`, ran `awk -F'|'` on it, applied it to a `/tmp`
   copy of the real table, and ran both the contract's awk census and the fleet validator
   `scripts/sources-census.sh validate` against a mirrored lane root — before and after.
5. Read `ScoutS049.md` once it landed and probed the two S049 request profiles myself; my digests
   reproduce the scout's exactly, independently.
6. Checked `agent://kotoba-r64.ScoutS120` three times before its artifact existed; the wait was
   never a block — the row was drafted with tokens first and filled after.

## 2. Deliverable A — the S120 row as this seat would write it (variant; the live row differs, §0)

### 2.1 The line

**Do not insert this: the live table already carries an S120 row at line 132 (§0).** This is the
variant this seat would write, kept byte-exact so the L1 can diff the two shapes rather than retype
either. If it is ever chosen over the live row, the S119 anchor is line 130 of `corpus/SOURCES.md` at
base `078eec4`, inside `## Registry` and before the blank line that precedes `## Paths` — and the
live row must be removed in the same edit (otherwise E03, duplicate id). Byte-exact, 1489 B, one
line, no `|` inside any cell:

```
| S120 | Practical Mutation Testing at Scale: A view from Google (Petrović, Ivanković, Fraser, Just) — https://doi.org/10.1109/TSE.2021.3107634 | paper | A | mutant-kill (detection of a seeded fault) as the test-suite adequacy witness the paper states, applied by the lane to load-bearing guard branches, and the equivalent-mutant caveat | Abstract paragraph `abstract1.1` first sentence, and §3.2.2 Heuristics to Prevent Equivalent Mutants paragraph `S3.SS2.SSS2.p1.1`, in the opened snapshot https://arxiv.org/html/2102.11378 (`arXiv:2102.11378v2`, HTTP 200, 571,600 B, sha256 `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`, `.ufo/waves/round-64/snapshots/S120.page`, opened 2026-10-24); the 728,951 B PDF https://arxiv.org/pdf/2102.11378 is byte-identical across two independent fetches (sha256 `a9bdf44159a7b8a6f4b77d7e347650e52d9915bf68f765ff5333f7feee56a081`); journal version IEEE TSE 48(10):3900–3912 (Crossref published-print 2022-10-01, created 2021-08-27), DOI 10.1109/TSE.2021.3107634, Crossref only, not opened | Mutation analysis measures adequacy by whether the suite detects seeded faults, so a killed mutant is the coverage witness statement coverage is not; and because equivalent mutants are a plague that cannot generally be detected automatically, a survivor is a lead to inspect, not proof of a gap and not a traditional mutation score | mined | 2026-10-24 | 180d | corpus/knowledge/g7-span-pinning-round64.md, corpus/lessons/round-64.md |
```

### 2.2 Cell by cell, with the source of each value

| # | column | value | provenance |
|---|---|---|---|
| 1 | id | `S120` | next unused (117 rows at base, highest `S119`) |
| 2 | source | `Practical Mutation Testing at Scale: A view from Google (Petrović, Ivanković, Fraser, Just) — https://doi.org/10.1109/TSE.2021.3107634` | title + authors from the opened snapshot (`ltx_personname`); DOI is the canonical record (Crossref), the opened body is the HTML in cell 6 |
| 3 | kind | `paper` | contract enum; first `paper` row in this registry |
| 4 | tier | `A` | ScoutS120's proposal, scoped as in §6; contract's "original paper" clause |
| 5 | scope | `mutant-kill (detection of a seeded fault) as the test-suite adequacy witness the paper states, applied by the lane to load-bearing guard branches, and the equivalent-mutant caveat` | assignment wording, **flipped** per RevSourcesGate §12.3: the bound lives in `scope` (in-lane precedent S118 and S101 both carry a parenthetical bound) because the tier is graded against `scope` by a non-author spot-check; the live row lands the same separation in prose |
| 6 | anchor | `abstract1.1` + `S3.SS2.SSS2.p1.1` in the opened snapshot, with bytes/sha and snapshot path; PDF refetch hash; journal record marked Crossref-only | scout's snapshot receipt + my re-verification (§5.3); PDF hash cross-checked against the scout's independent fetch (§5.2) |
| 7 | teaches | one benefit: detection-of-seeded-faults is the adequacy witness; equivalent mutants bound a survivor to a lead, not proof and not a mutation score | both quotes located (§5.4); bound taken from the paper's own next sentence ("some categories … can be accurately detected") and the scout's warning that 87.5% is not the mutation score |
| 8 | status | `mined` | C1's knowledge entry cites it (ScribeEntry confirms the path); see the landing-order finding, §7.3 |
| 9 | opened | `2026-10-24` | snapshot response `date: Sat, 24 Oct 2026 03:37:19 GMT`; my fetches same date |
| 10 | recheck | `180d` | assignment; due 2027-04-22 |
| 11 | used-by | `corpus/knowledge/g7-span-pinning-round64.md, corpus/lessons/round-64.md` | ScribeEntry (IRC 2026-10-24) confirms this exact path against its draft entry |

### 2.3 The tokenized form — SUPERSEDED, DO NOT APPLY (record only)

**The row to apply is §2.1, line 45 of this file.** This block preserves the pre-fill draft that the
assignment's `<PENDING:…>` instruction produced, so every fill can be audited against it. It differs
from the apply-as-is line by design (PDF-page anchors instead of snapshot ids, and four unfilled
tokens); `diff` against line 45 will report a difference, and that difference is the point. It parses
(NF=13) only so that a paste cannot break the table if it ever happens by mistake:

```
| S120 | Practical Mutation Testing at Scale: A view from Google (Petrović, Ivanković, Fraser, Just) — https://doi.org/10.1109/TSE.2021.3107634 | paper | A | mutant-kill as the witnessed-coverage signal for load-bearing guard branches, and the equivalent-mutant caveat | §1 Introduction paragraph 2 (PDF p.1) and §3.2.2 Heuristics to Prevent Equivalent Mutants (PDF p.5) of arXiv:2102.11378v2; journal version IEEE TSE 48(10):3900–3912, Oct 2022 (Crossref published-print 2022-10-01, created 2021-08-27); fetched 2026-10-24T03:36Z, re-fetched 2026-10-24T03:39:14Z byte-identical, HTTP 200, <PENDING:size> B, sha256 <PENDING:sha256>; snapshot <PENDING:snapshot-path> | Mutation-kill is the witnessed-coverage signal that statement coverage is not — a guard branch can be covered and still unasserted, so a surviving mutant names the untested branch; and because equivalent mutants are a plague that cannot generally be detected automatically, a survivor is a lead to inspect, not proof of a gap [quote: <PENDING:quote>] | mined | 2026-10-24 | 180d | corpus/knowledge/g7-span-pinning-round64.md, corpus/lessons/round-64.md |
```

*(block ends; the line above is the superseded draft, not the deliverable — go to §2.1)*

Verified byte-identical to `/tmp/s120/row-pending.md` (NF=13). Superseded by §2.1 as soon as
`ScoutS120.md` landed.

### 2.4 Cell 5 wording — F5, closed by flipping

RevSourcesGate's objection: "for load-bearing guard branches" inflates the scope, because the paper
never studies guard branches and A's warrant ("original paper") reaches only what the paper
establishes — changelists, files, mutated statements. My first answer defended the assignment's
wording on the contract's definition of `scope`; the reviewer's rebuttal settles it, and I accept it:
a locus of trust is only as good as the claim standing on it, so A cannot be asserted *for* a
branch-application claim unless the cell marks the application as the lane's. Three of their points I
verified myself rather than taking on trust:

- **In-lane precedent.** Two adjacent rows already carry the bound inside `scope`: S118 — "…matching
  syntax (vendor documentation; not a runtime test)" — and S101 — "…execution scopes (vendor
  documentation; not runtime behavior)". This row was the outlier.
- **The bound must live where the tier is graded.** Rule 1 has a non-author spot-check re-open a
  sample and grade the tier against `scope`; a bound that lives only in `teaches` is unreviewable at
  the cell the tier is defined against, and `teaches` is defined as "one grounded learner benefit",
  not a scope-limitation field.
- **Zero machine risk, measured.** Their swap receipt: cells 11/11, differing cells `[5]`, NF=13,
  `validate` → `ok`, exit 0. My own re-run of the swapped row agrees on NF=13 and produces a
  validator output byte-identical to the pre-swap run (`diff validate.out validate.after.out` → no
  difference), so the swap changes nothing any gate can see.

So the variant in §2.1 now carries the flipped cell, verbatim:

```
mutant-kill (detection of a seeded fault) as the test-suite adequacy witness the paper states, applied by the lane to load-bearing guard branches, and the equivalent-mutant caveat
```

The L1's original assignment string was `mutant-kill as the witnessed-coverage signal for
load-bearing guard branches, and the equivalent-mutant caveat`; if the L1 prefers it, that is a
one-cell revert and F5 reopens with it. The **live** row already lands F5 in its own wording (§0), so
no action is owed there. The reviewer's smaller-diff alternative — deleting the four words "for
load-bearing guard branches" — also lands F5 but drops the application from the scope entirely; the
flipped wording keeps both, which is why I did not take it.

## 3. Parse proof (real output)

`awk -F'|'` on the filled row — 13 fields = 11 data columns + the two empty edge fields:

```
$ awk -F'|' '{print "NF="NF}' /tmp/s120/row-filled.md
NF=13
```

Per-cell decomposition (proof that no cell swallowed a `|`; 11 data cells, each one field):

```
[1]
[2] S120
[3] Practical Mutation Testing at Scale: A view from Google (Petrović, Ivanković, Fraser, Just) — https://doi.org/10.1109/TSE.2021.3107634
[4] paper
[5] A
[6] mutant-kill as the witnessed-coverage signal for load-bearing guard branches, and the equivalent-mutant caveat
[7] Abstract paragraph `abstract1.1` first sentence, and §3.2.2 Heuristics to Prevent Equivalent Mutants paragraph `S3.SS2.SSS2.p1.1`, in the opened snapshot https://arxiv.org/html/2102.11378 (`arXiv:2102.11378v2`, HTTP 200, 571,600 B, sha256 `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`, `.ufo/waves/round-64/snapshots/S120.page`, opened 2026-10-24); the 728,951 B PDF https://arxiv.org/pdf/2102.11378 is byte-identical across two independent fetches (sha256 `a9bdf44159a7b8a6f4b77d7e347650e52d9915bf68f765ff5333f7feee56a081`); journal version IEEE TSE 48(10):3900–3912 (Crossref published-print 2022-10-01, created 2021-08-27), DOI 10.1109/TSE.2021.3107634, Crossref only, not opened
[8] Mutation analysis measures adequacy by whether the suite detects seeded faults, so a killed mutant is the coverage witness statement coverage is not; and because equivalent mutants are a plague that cannot generally be detected automatically, a survivor is a lead to inspect, not proof of a gap and not a traditional mutation score
[9] mined
[10] 2026-10-24
[11] 180d
[12] corpus/knowledge/g7-span-pinning-round64.md, corpus/lessons/round-64.md
[13]
```

Contract census block, on `/tmp/s120/SOURCES.applied.md` (byte copy of the lane table with the filled
row inserted after S119), run from the lane root so repo-relative `used-by` paths resolve:

```
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' /tmp/s120/SOURCES.applied.md
118                     # 117 at base + S120
$ awk -F'|' '... NF!=13 {n++} END{print n+0}' ...
0                       # malformed rows: none
$ awk -F'|' '... tier histogram ...' ...
A=115 B=2 C=1           # S120 counted as A
$ awk -F'|' '... status histogram ...' ...
mined=110 queued=7 rejected=1
$ awk -F'|' '... duplicate ids ...' | sort | uniq -d
                        # empty: no duplicate id
$ awk -F'|' '... enum + tier inflation ...' ...
                        # empty: paper is a valid kind, mined is a valid status, no community at A
$ awk -F'|' '... mined used-by existence ...' | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
missing: corpus/knowledge/g7-span-pinning-round64.md
missing: corpus/lessons/round-64.md
```

Draft-time caveat: earlier in this seat's run both `used-by` files were absent, so the census printed
two `missing:` lines and the validator two E11s. Both files have since landed
(`corpus/knowledge/g7-span-pinning-round64.md` 8,706 B, `corpus/lessons/round-64.md` 12,353 B), so the
current receipts are clean — the numbers above come from a 117-row base (the live table with the L1's
S120 row removed) plus my variant inserted after S119, which is the "my row instead of the live row"
state:

```
$ validator on appliedB (my variant, used-by files present) → ok, exit 0
$ validator on appliedA (same row, pre-flip cell 5)          → ok, exit 0
$ diff valA.out valB.out                                     → no difference
```

That last diff is the clean measurement of RevSourcesGate's "zero machine risk" for the cell-5 swap;
my earlier `validate.out`/`validate.after.out` comparison was contaminated by the live row landing
mid-run (it surfaced as E03, duplicate id), which is itself the proof that two S120 rows cannot
coexist.

The fleet validator (fleet repo `…/scripts/sources-census.sh`; not in the lane):

```
$ scripts/sources-census.sh validate . --today 2026-10-24          # live table, with the L1's row
kotoba-shokunin	W04	S018 duplicate url ...      (16 W04 lines, all pre-existing)
kotoba-shokunin	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

Both validator targets are mirrored lane roots (`/tmp/s120/root/kotoba-shokunin`: the applied table
plus symlinks to the lane's real `corpus/knowledge`, `corpus/lessons` and `SKILL.md`), so E11 resolves
repo-relative paths exactly as it would in the lane. With the `used-by` files now present, **no
E01–E11 and no E12 fire**: the row is well formed, the id is unique, kind/tier/status are in-enum,
`opened` and `recheck` parse, the paths resolve, and the row sits inside `## Registry` rather than
after `## Search log`.

Mode caveat: with `--file /tmp/s120/…/SOURCES.md` instead, every `used-by` resolves relative to the
draft's own directory, so all 110 mined rows report E11. That is an artifact of `--file`, not a
finding about the table; I mention it so a reviewer who reproduces with `--file` does not mistake the
flood for damage.

## 4. Deliverable B — search-log append

### 4.1 The note (apply as-is)

Prose only, no `|` characters. **Placement: end of `## Search log`, unsplit** — after line 200 and
before `## Leads (unopened)` at line 202, S120 sweep first then ScoutS049's note. That is
RevSourcesGate's ruling, adopted here; the reasons, the measured absence of any machine check and the
line numbers to cite in the lesson are in §7.4. Do not relocate the round-63 note (rule 2 forbids
rewriting existing prose), and do not append this note at EOF.

```
- **2026-10-24 — round-64 S120 opening (C1's method source).** Question: which primary source teaches
  mutation-kill as witnessed coverage — a surviving mutant as the signal that a load-bearing guard
  branch is exercised but never witnessed — and states the equivalent-mutant caveat. Where: two web
  searches (the plan's named candidate; then the mutant-versus-real-fault validity line), the arXiv
  record and PDF for `2102.11378` (fetched twice byte-identical), the arXiv HTML the snapshot pins,
  Crossref for both DOIs the plan named and for the journal version, and the included paper's own
  bibliography. Identified 8 distinct candidate works; screened 8; included 1 (S120); excluded 7 —
  (a) Just, Jalali, Inozemtseva, Ernst, Holmes and Fraser, "Are Mutants a Valid Substitute for Real
  Faults in Software Testing?", FSE 2014, DOI 10.1145/2635868.2635929: grounds a different claim
  (mutant detection correlates with real-fault detection beyond coverage), so carrying it would widen
  S120's scope against rule 2, and it was not opened this round, so rule 1 forbids a row; (b)
  Petrović and Ivanković, "State of Mutation Testing at Google", ICSE-SEIP 2018, pp. 163–171, DOI
  10.1145/3183519.3183521: the same authors' earlier, smaller report (6,000 engineers against the
  included paper's 24,000 developers on 1,000+ projects), superseded for this scope; (c) Jia and
  Harman, "An Analysis and Survey of the Development of Mutation Testing", IEEE TSE 37(5):649–678,
  2011: secondary survey, tier B at best, and it is the included paper's own reference [28] for the
  equivalent-mutant problem, so it duplicates S120's scope; (d) "Mutation Testing in the Wild:
  Challenges and Lessons from Bitcoin" (SBC/SAST, surfaced 2026): single-system experience report in
  another domain, no scale claim for this scope, not opened; (e) "Does mutation testing improve
  testing practices" (ICSE 2021, pp. 910–921, the same four authors, identified by RevSourcesGate's
  independent record check and surfaced by my search only as a secondary index page): a different
  question — whether mutation testing changes developer testing behaviour — and a different venue
  class from the included journal article, not opened; (f) `arXiv:2103.02722`, the plan's identifier:
  opened, and it is Peralta, "A Markov jump process associated with the matrix-exponential
  distribution" — wrong work, rejected; (g) DOI 10.1109/ICSE43902.2021.00068, the plan's DOI:
  resolved through Crossref, and it is Chen et al., "An Empirical Study on Deployment Faults of Deep
  Learning Based Mobile Applications", ICSE 2021, pp. 674–685 — wrong work, rejected. The plan's
  candidate citation is therefore corrected by the opened record in three places: the authors are
  Petrović, Ivanković, Fraser and Just (no Ernst), the venue is IEEE Transactions on Software
  Engineering 48(10):3900–3912, published in issue Oct 2022 (Crossref published-print 2022-10-01,
  created 2021-08-27), not ICSE 2021, and the preprint is `arXiv:2102.11378v2` (26 Feb 2021), not
  `2103.02722`. Stop rationale (rule 5): the plan's two identifiers were opened and rejected rather
  than silently skipped, and the title-matched primary then opened and carries both located quotes
  the `teaches` cell needs — the adequacy definition at `abstract1.1` and "are a plague in mutation
  testing and cannot generally be detected automatically" at `S3.SS2.SSS2.p1.1` — so the sweep stops
  at full inclusion of the one qualifying source; every other screened work grounds a different
  claim, is secondary, or was not opened, and ScoutS120Alt's three fallbacks (a Google engineering
  blog post, a university mutation-testing chapter, PIT's equivalent-mutant docs) stay unscreened
  because the title match succeeded — recorded there, not counted here.
```

### 4.2 The S049 re-probe line (placeholder, now resolved — do not retype)

The assignment asked for a placeholder, and this is the slot. **The line has since landed**: ScoutS049
wrote its own append-only note and its exact bytes sit in
`.ufo/waves/round-64/w1/ScoutS049.md` § "Exact append text". The L1 should apply **that** text, not a
retyping, immediately after my note (same date; S120 sweep first, S049 re-probe second). Do not use
my numbers in place of theirs: ours agree, theirs carry the response headers, the `vary: Accept`, the
Vercel cache state and the control fetch of the extensionless URL, which mine do not.

Independent confirmation that the two runs agree (mine, `2026-10-24T03:37:24Z`; theirs,
`03:35:37Z`): default profile → HTTP 200, 17,252 B, sha256 `dae9d3ec…ce0`; `Accept: text/markdown` →
HTTP 404, 389 B, sha256 `4f98eb06…fb1`. Both digests are identical in the two seats' reports.

## 5. Evidence receipts

### 5.1 The source opened, by me

```
$ curl -sS -w 'HTTP %{http_code} %{size_download}B %{content_type}\n' -o S120.pdf https://arxiv.org/pdf/2102.11378
HTTP 200 728951B application/pdf
$ sha256sum S120.pdf
a9bdf44159a7b8a6f4b77d7e347650e52d9915bf68f765ff5333f7feee56a081  S120.pdf
# re-fetch at 2026-10-24T03:39:14Z
$ curl -sS -o S120.recheck.pdf … ; sha256sum S120.pdf S120.recheck.pdf ; cmp S120.pdf S120.recheck.pdf && echo BYTE_IDENTICAL
a9bdf44159a7b8a6f4b77d7e347650e52d9915bf68f765ff5333f7feee56a081  S120.pdf
a9bdf44159a7b8a6f4b77d7e347650e52d9915bf68f765ff5333f7feee56a081  S120.recheck.pdf
BYTE_IDENTICAL
$ grep -o 'arXiv:2102\.11378v[0-9]*[^ ]*' S120.plain.txt | sort -u
arXiv:2102.11378v2
```

### 5.2 Cross-seat byte agreement

ScoutS120 fetched the same PDF with a Chrome-like UA and `Accept: application/pdf,*/*`; its receipt is
728,951 B, sha256 `a9bdf441…` — **identical to mine**, from a different request profile, an
independent process and a separate clock. Two request profiles agreeing on the digest is the
strongest form of "the bytes are stable" this lane can produce without a publisher copy. The scout
also confirms the HTML twice (`arxiv.org/html` and `export.arxiv.org/html/2102.11378v2`, 571,600 B,
sha256-identical), which is the snapshot the row anchors to.

### 5.3 Both quotes verified inside the committed snapshot (not copied on trust)

```
$ sha256sum .ufo/waves/round-64/snapshots/S120.page
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8  …/S120.page
$ grep -c 'id="abstract1.1"' …/S120.page            → 1
$ grep -c 'id="S3.SS2.SSS2.p1.1"' …/S120.page        → 1
python3: both quote strings found in the whitespace-normalized snapshot (22 words each)
id "S3.SS2.SSS2.p1.1" sits 114 characters before the plague sentence, on the same <p class="ltx_p">
```

So the snapshot's own hash matches the scout's receipt, both anchor ids exist exactly once, and each
quote is inside the paragraph its id names.

### 5.4 Quotes, word counts, locations

| # | quote | words | anchor | role in the cell |
|---|---|---|---|---|
| G | "Mutation analysis assesses a test suite's adequacy by measuring its ability to detect small artificial faults, systematically seeded into the tested program" | 22 | `abstract1.1`, first sentence | the witness half; ScoutS120's gate quote, apostrophe U+2019 as printed |
| C | "Equivalent mutants, which are semantically equivalent to the mutated program, are a plague in mutation testing and cannot generally be detected automatically" | 22 | `S3.SS2.SSS2.p1.1` | the caveat half; the paragraph continues "However, there are some categories of equivalent mutants that can be accurately detected", which is why the cell says "a lead to inspect, not proof" |
| S | "The statement-deletion mutation, on the other hand, explicitly points out this testing weakness" | 13 | §1 Introduction, PDF p.1 | support only, not in the cell |

PDF corroboration of the same two halves: §1 Introduction paragraph 2 (PDF p.1) reads "However, code
coverage alone might be misleading, in particular when program statements are covered but the
expected program outcome is not asserted upon" (23 words) — the coverage-versus-witness contrast the
scope names; §3.2.2 (PDF p.5) repeats C verbatim.

Page-count correction against my own earlier note: `pdftotext` split the PDF into 23 segments because
of a trailing form feed; `pdfinfo` (ScoutS120) reports **22 pages**. The 22-page number is the one to
carry.

### 5.5 S049 probe (mine, provisional; the scout's line is authoritative)

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-24T03:37:24Z
$ curl -sS -o body.default -w 'default: HTTP %{http_code} %{size_download}B\n' https://cursor.com/docs/rules.md
default: HTTP 200 17252B
dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0  body.default
$ curl -sS -H 'Accept: text/markdown' -o body.md -w 'text/markdown: HTTP %{http_code} %{size_download}B\n' https://cursor.com/docs/rules.md
text/markdown: HTTP 404 389B
4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1  body.md
```

Note on the word "default": my no-`-H` request sent `Accept: */*` (curl's default), which is what
ScoutS049 confirmed on a trace. The row-level claim is unaffected — the 404 is a
request-profile-dependent response, and the 200 body is byte-identical to the 2026-10-23 errata's.

## 6. Tier: A, per ScoutS120's proposal, with its bounds

The scout proposes **A** scoped to "mutant-kill (detection of a seeded fault) as the test-suite
adequacy witness, as stated by this paper", explicitly **not** A for Ernst as author, for ICSE 2021,
for the plan's identifiers, or for reading any kill rate as a traditional mutation score or as proof
that a kill is a real fault. I adopt that, and the row's scope cell (the assignment's wording) fits
inside it: both halves of the teaches sentence are the paper's own words, so A holds for the claim as
written. What A does **not** license, and the teaches cell avoids:

- a survivor proving a test gap (the paper's own next sentence concedes detectable equivalent
  categories, and § Related Work notes equivalent mutants "can be productive");
- the 87.5% kill rate in § V-C being read as a mutation score — the scout flags that the paper's own
  next sentence denies it, and the cell says "not a traditional mutation score";
- the external claim that mutation testing beats statement coverage as a general law (that line is
  the paper's argument in §1, not a controlled comparison here).

If a later round needs the cross-project validity claim, that is a new row (Just et al., FSE 2014),
not an edit to this one — rule 2 forbids widening a row in place.

## 7. Findings

1. **The plan's S120 citation is wrong in three places, and the row corrects all three** (supports
   C1's sourcing step; falsifies `plans/round-64.md` § Sources as written). The plan says "Petrovic,
   Ivankovic & Ernst, 'Practical Mutation Testing at Scale', ICSE 2021" and supplies
   `arXiv:2103.02722` / `10.1109/ICSE43902.2021.00068`. The opened record: Goran Petrović, Marko
   Ivanković, **Gordon Fraser, René Just** (no Ernst); IEEE **TSE 48(10):3900–3912**, issue Oct 2022
   (Crossref `published-print 2022-10-01`, `created 2021-08-27`), DOI 10.1109/TSE.2021.3107634 — a
   journal article, not ICSE; preprint **`arXiv:2102.11378v2`** (26 Feb 2021). The plan's two
   identifiers are *different papers*: `2103.02722` is Peralta (Markov jump process), and
   `10.1109/ICSE43902.2021.00068` is Chen et al. (deep-learning mobile deployment faults). Three
   seats agree: my fetch + Crossref query, ScoutS120's opened-and-rejected section, and
   RevSourcesGate's Crossref check (IRC). My own Crossref output:

   ```
   type: journal-article   container: ['IEEE Transactions on Software Engineering']
   volume/issue/page: 48 10 3900-3912   published-print: [[2022, 10, 1]]   created: 2021-08-27
   authors: [('Goran','Petrovic'), ('Marko','Ivankovic'), ('Gordon','Fraser'), ('Rene','Just')]
   ```

   The plan is frozen, so the correction belongs in the row, the lesson `## Gate` and the round
   report — never in a plan edit.
2. **The teaches cell needs two quotes, not one** (supports C1's sourced-claim requirement). The
   scout's gate quote is the adequacy **witness** and says nothing about equivalent mutants; the
   scope sentence also names the caveat, which is a different sentence in a different section
   (`S3.SS2.SSS2.p1.1`). Both are verified inside the committed snapshot (§5.3), so the row's two-id
   anchor is the honest minimum. A one-quote row would over-claim the scope the assignment fixed.
3. **Landing-order gate on `status: mined` — was open, now satisfied.** At draft time both
   `corpus/knowledge/g7-span-pinning-round64.md` and `corpus/lessons/round-64.md` were absent, so the
   census printed two `missing:` lines and the validator two E11s; both files have since landed
   (8,706 B at 00:51, 12,353 B at 00:53) and the live table now validates `ok`, exit 0. The surviving
   coupling is a **rename**: cell 11 must follow the entry's real filename (ScribeEntry confirms
   `g7-span-pinning-round64.md`; RevSourcesGate proposed `span-missing-pinning-round64.md` and logged
   the conflict as F8), and E11 fires on a typo or a rename. The second coupling is placement: the
   row must sit inside `## Registry` directly after S119 — validator **E12** fires on a row-shaped
   source appended after `## Search log`, which is where the search-log note goes, so keep the two
   apart. The live row is additionally separated from S119 by a blank line (residual R1, §0).
4. **Search-log placement — ruled by RevSourcesGate, and the ruling rests on a measured absence of
   any machine check.** Both round-64 notes go at the end of `## Search log` (after the last note,
   before `## Leads (unopened)` at line 202), unsplit, S120 sweep first then the S049 re-probe. The
   round-63 note at lines 220–243 is **not** relocated: contract rule 2 (fleet `CORPUS.md:113-114`,
   verified — "Only `status`, `recheck` and `used-by` change in place") permits no in-place rewrite of
   existing prose, so the misfiling is recorded once in the lesson's Gate/search-log paragraph with
   the line numbers (`## Search log` 150, `## Leads` 202, r63 note 220–243) instead of repaired. The
   reviewer measured the failure mode: a note inserted under `## Leads` left
   `sources-census.sh validate` at `ok`, exit 0 — prose placement has **zero** machine check, so E12
   will never catch it and the ruling has to be held by diff review. My earlier "append-at-EOF is an
   acceptable alternative" is withdrawn: it would reproduce a misfiling that no gate can see.
5. **First `paper` row in the registry.** All 117 base rows are `spec`/`docs`/`code`/`own-work`;
   the histogram after the row is `A=115 B=2 C=1`. The contract already covers papers, so no change
   is needed — but with no in-lane precedent, the anchor cell spells out three objects explicitly
   (snapshot bytes for the quotes, PDF bytes as refetchable corroboration, Crossref-only journal
   record marked "not opened") so a later reader cannot mistake which artifact a quote resolves in.
6. **The 87.5% kill rate must not become the teach** (ScoutS120's warning, adopted). § V-C's
   `S5.SS3.p2.1` says "Overall, 87.5% of all generated mutants are killed by the initial test suite",
   and its next sentence denies this is the traditional mutation score. The cell therefore says "not
   a traditional mutation score"; anyone quoting the number as a coverage witness would misstate the
   source.
7. **ScoutS120Alt's three fallbacks stay unscreened, by design.** The scout records that the title
   match made them unnecessary (Google engineering blog, a university mutation-testing chapter, PIT's
   equivalent-mutant docs). They are leads, not evidence, and are not counted in my 8/8/1/7 sweep.
8. **Self-correction carried into the report, not hidden**: my first PDF page map said 23 pages; the
   truth is 22 (`pdfinfo`), and the 23 was `pdftotext`'s trailing form feed (§5.4). Likewise my
   tokenized row anchored to PDF pages before the snapshot existed; §2.3 records the change and why
   the snapshot is the better anchor. I also caught and repaired a real defect in this report while
   answering review: a read-tool display truncation had carried `…` into the §2.3 block, which I then
   restored from `/tmp/s120/row-pending.md` and re-verified byte-identical (NF=13). The lesson general
   form: never round-trip a long row through a truncated display.
9. **Review status (RevSourcesGate, 2026-10-24).** Closed: the citation correction (F3); the
   snapshot-anchored row with its "Crossref only, not opened" disclosure (F6); the row's validator
   behavior; the §2.3 hazard; and **F5** — cell 5 is flipped in my variant and discharged on the live
   row by its author's own narrowed wording. R2 is **owned by RevSourcesGate** (its §13.2), with the
   exact `§III-B2` → `§VI Related Work \`#S6.p3.1\`` cell swap supplied and its §13.3 applying R1+R2
   to a `/tmp` copy (contiguous table, NF=13, `ok` exit 0). Open for whoever edits the live file: R1
   (delete the blank line at 131) and R2 (that cell swap). My variant is ruled a record, not a
   pending edit (§0). Neither residual is machine-caught — a validator run will never see them.

## 8. Gates not run, and out of scope

- No build/test/lint of the lane, by design; I never modified `corpus/SOURCES.md` (the L1 applied its
  own row while this seat ran, §0). Live state measured read-only: `118` rows, `0` malformed,
  validator `ok` exit 0 with only the 16 pre-existing W04 warnings. My variant's post-apply state was
  measured on a clean 117-row base: `118` rows, `0` malformed, `ok` exit 0, and identical output
  before and after the cell-5 swap.
- Not done (other seats): the round report's own citation of S120; ScoutS120Alt's fallback screen;
  the two live-row residuals R1/R2 (§0); and the **rejected-identifier lines in the round lesson's
  Gate** — the plan's `arXiv:2103.02722` (Peralta) and DOI `10.1109/ICSE43902.2021.00068` (Chen et
  al.) are opened-and-rejected works, recorded in my search-log note items (f)/(g) and in
  RevSourcesGate §3, but the lesson owner must carry them too (rule 1's Gate record).
- Not touched: C1's four arms, C2's counter, LOG, SCORECARD, the lesson, the live S120 row. I make no
  claim about their state beyond what §0 quotes.

## 9. Tool installs

None. No pacman/uv/cargo/npm transaction; nothing added to `~/.local/bin`. Tools used were already on
the host: `curl`, `sha256sum`, `cmp`, `awk`, `sed`, `grep`, `python3`, `pdftotext`. The pacman guard
(host-wide pause) was not approached.

## 10. Artifacts

- This report: `.ufo/waves/round-64/w1/ScribeSOURCESRow.md`
- Filled + flipped row (byte-exact, 1489 B, my variant — **not** the live row): `/tmp/s120/row-filled.md`
- Clean 117-row base (live table minus the L1's S120 row) and the two variants applied to it:
  `/tmp/s120/base117.md`, `/tmp/s120/appliedA.md` (pre-flip), `/tmp/s120/appliedB.md` (flipped);
  validator outputs `/tmp/s120/valA.out`, `/tmp/s120/valB.out` (identical)
- Superseded tokenized row (record only): `/tmp/s120/row-pending.md`
- Table with the filled row applied: `/tmp/s120/SOURCES.applied.md`
- Mirrored lane root for `scripts/sources-census.sh validate`:
  `/tmp/s120/root/kotoba-shokunin` (applied table + symlinks to the lane's `corpus/knowledge`,
  `corpus/lessons`, `SKILL.md`); validator stdout saved at `/tmp/s120/validate.out`
- Fetched bytes: `/tmp/s120/S120.pdf`, `/tmp/s120/S120.recheck.pdf` (byte-identical), extractions
  `/tmp/s120/S120.txt` (`-layout`), `/tmp/s120/S120.plain.txt` (reading order)
- S049 probe bodies: `/tmp/s120/body.default`, `/tmp/s120/body.md`
- Read-only cross-checks: `plans/round-64.md`, `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`,
  `corpus/SOURCES.md` (S001–S119), `.ufo/waves/round-64/w1/ScoutS120.md`,
  `.ufo/waves/round-64/w1/ScoutS049.md`, `.ufo/waves/round-64/snapshots/S120.page`,
  `scripts/sources-census.sh` (fleet)
