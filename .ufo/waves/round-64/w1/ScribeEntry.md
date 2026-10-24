# ScribeEntry — C1 knowledge entry draft (round 64, wave 1)

role: scribe (leaf; no subagent dispatch, no installs)
item: draft `corpus/knowledge/g7-span-pinning-round64.md` and the S120 `used-by` list
lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base tip `078eec4`
status: **draft delivered below; the tree was not written.** Only this report file exists from
this seat. Scratch: `/tmp/r64` (entry draft), `/tmp/s120*` (source fetch).

## 1. Deliverable — full content of `corpus/knowledge/g7-span-pinning-round64.md`

120 lines (`wc -l /tmp/r64/entry.md` → `120`, budget ≤120), provenance trio on lines 1–3.
Land this block byte-for-byte; it is the whole file. **Revision 4** (this version): snapshot line
**spans** beside the paragraph ids (R2/R3), journal fields labelled Crossref-only (R2), and the
223 measurement pinned to the arms-application digest `7791504715f3…` from MutSpanArms rather
than §11's prototype `ae84673e…` (R4) — ScribeLesson's finding-12 caution. § Limits gains the two
suite gaps MutSpanArms measured on those same 223 bytes (A2 wrapper swap survives; arms 2–3
deletion leaves `0 failure(s) over 221`).

````markdown
source: S120 — Petrović, Ivanković, Fraser & Just, "Practical Mutation Testing at Scale: A view from Google", IEEE TSE 48(10):3900-3912 (2022; Crossref metadata, publisher HTML not opened), DOI 10.1109/TSE.2021.3107634; preprint arXiv:2102.11378v2 (26 Feb 2021), §1 (`S120.page:S1.p1.1`, quote at lines 324-326) and §3.2.2 (`S120.page:S3.SS2.SSS2.p1.1`, lines 780-782), committed snapshot `.ufo/waves/round-64/snapshots/S120.page` (571,600 B, sha256 `15963c3e…`); internal evidence `.ufo/waves/round-63/w2/MutW2V32.md` §11 and `.ufo/waves/round-64/w1/MutSpanArms.md`. The arms' receipts rest on `verifiers/check_scoped_rules_v32.py`'s self-test bytes, not on S120.
verified-at: 2026-10-24 — base `078eec4`, v32 sha256 `12d093a1…`: `self-test: 0 failure(s) over 219 assertions`, exit 0 (re-run by this seat); the four arms' worktree bytes (sha256 `f8f69cad…`, 147,512 B, uncommitted) print `0 failure(s) over 223 assertions`, exit 0 (re-run by this seat); the committed digest is the C1 receipt's to pin; branch at `verifiers/check_scoped_rules_v32.py:1055-1067`
recheck: 180d — `python3 -B verifiers/check_scoped_rules_v32.py --self-test`: all four printed lines and the assertion count against § The measured record; sooner on any mutation reported surviving this branch

## What it is

A guard branch that can only reject is **load-bearing**; with no assertion that
turns on it, it is an **unrecorded bound**. The v32 `span_missing` arm
(`g7_conjunct`, `verifiers/check_scoped_rules_v32.py:1055-1067`; the plan writes
`:1055-1068`, which adds the function's trailing `return []`) rejects an action
cell whose backticked span carries words found in neither the cited line nor the
page. Six mutants of it were scored against the committed 219-assertion
self-test: SM1 (branch deleted), SM2 (`len(word) >= 4` floor dropped), SM3
(`STOPWORDS` filter dropped) and SM5 (cited-line check dropped) all survive at
exit 0. SM1 is an evasion, not a cosmetic gap:

```
cell: 'The configuration stores project rules using glob syntax and `exfiltrates credentials`.'
  LANDED                G7=REJ  G9=-    ACTION=REJECTED
  SM1 (branch removed)  G7=-    G9=-    ACTION=ADMITTED  <-- EVASION
```

`content_words()` strips backticked spans, so A2's forward fraction and page
containment cannot see the fabrication, and G9's page gate skips a clause the
page lacks — the branch added to close that hole had no test that could tell it
was there. S120 states the general defect: `However, code coverage alone might
be misleading, in particular when program statements are covered but the
expected program outcome is not asserted upon` (§1; `[2], [3]` markers removed,
line breaks joined — `quote-equal after documented shaping`). A `0 failure(s)
over 219 assertions` receipt is then true and silent.

## The method

Four arms, one per load-bearing lane, texts byte-for-byte as measured in
`MutW2V32.md` §11.

1. **Positive witness for the branch — the evasion cell.** Assert the fabricated
   span is rejected, on the guard's own reason line (`A2 G7: a backticked span
   whose words occur in neither the cited line nor the page is rejected`).
   Kills SM1.
2. **Negative witness for the stopword filter.** `` `because otherwise` `` is
   *not* rejected: every ≥4-character word in the span is a stopword. Kills SM3.
3. **Negative witness for the length floor.** `` `ox it` `` is *not* rejected:
   no span word reaches four characters. Kills SM2.
4. **Negative witness for the cited-line rescue.** `` `mode quota` `` is *not*
   rejected when the word is in the cited line but absent from the page — and
   this arm calls `g7_conjunct` **directly**, not `action_conjunct`. Kills SM5.

Two disciplines make the arms discriminating rather than decorative. **Isolate
the lane when a wrapper decides first:** `action_conjunct` runs A2's
page-containment arm before G7, and on arm 4's cell the page lacks `mode`, so
the wrapper's earlier arm supplies the False and the assertion would pass for
the wrong reason. **Assert the reason:** `named(reasons, needle)` pins the arm
that produced the verdict, so another arm's True/False cannot satisfy it.

The kill rule is two-part: each mutant must be red **and** its red line must be
the arm aimed at it. SM4 and SM6 are red only through `FAIL eligible world: the
four counted rows are backed` — a kill of the mutant, not a witness for the arm.

Frozen predicate: `python3 -B verifiers/check_scoped_rules_v32.py --self-test`
prints all four lines and exits 0 —

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
```

## The measured record

| state | assertions | exit | SM1 | SM2 | SM3 | SM4 | SM5 | SM6 |
|---|---|---|---|---|---|---|---|---|
| r63 bytes (`12d093a1…`) | 219 | 0 | survives | survives | survives | red (`eligible world`) | survives | red (`eligible world`) |
| + the four arms | 223 | 0 | red (arm 1) | red (arm 3) | red (arm 2) | red (`eligible world`) | red (arm 4) | red (`eligible world`) |

Measured in §11 on the prototype (`landed_plus_spanfix7`, sha256 `ae84673e…`):
green at 223, all six mutants red, the nine splitter mutants red on top
(`sib_M1..M8 … (all nine)`), `judge()` unchanged (`4 of 4` backed,
`committed == LANDED+4assertions: True`); re-measured on the applied arms
(`7791504715f3…`, MutSpanArms): SM1–SM6 red again (SM4 5 failures, SM6 10).

## Limits

- **A survivor is not automatically a gap.** S120 §3.2.2: `Equivalent mutants,
  which are semantically equivalent to the mutated program, are a plague in
  mutation testing and cannot generally be detected automatically` (line breaks
  joined — `quote-equal after documented shaping`). SM2, SM3 and SM5 were
  argued *not* equivalent by divergence: over 20 000 random cells SM2 differs on
  3 607; SM3 differs on any span whose only ≥4-character word is a stopword; SM5
  differs on a span word in the cited line but absent from the page. This is a
  divergence set, not a kill rate.
- **Two gaps the suite itself has, measured on MutSpanArms' 223 bytes.** Swapping arm 4's
  `g7_conjunct` for `action_conjunct` **survives** (0 failures over 223, mutant
  A2): the arm asserts `named(…, "G7")` False, so the wrapper's earlier A2
  rejection satisfies it — the direct call is a discipline, not a witnessed
  rule. Deleting arms 2 and 3 also leaves `0 failure(s) over 221` (A5): their
  presence is pinned only by the count literal, so a receipt that pins
  `0 failure(s)` alone cannot see their removal — pin sha256 and count as a pair.
- **Red is not discriminating.** SM4 and SM6 are killed by the eligible-world
  arm, not by any of the four; the page-check and always-fires semantics of the
  branch still have no G7 arm.
- **Hand-built cells, one latent class.** The arms pin `g7_conjunct`'s
  `span_missing` computation on constructed cells — not its priority against
  G7's identifier arm or G9, nor `supported()`'s four-character prefix rule — and
  MutW2V32's scan found no committed cell that trips the evasion, so the
  evidence is the constructed cell plus the SM1 admission, not a corpus instance.
- **Out of scope.** The W8 escape class and A2's F6 compound-purpose bound stay
  carried debt (`SCORECARD.md` round-64 Next line); this entry claims neither.

## How to re-run

```
python3 -B verifiers/check_scoped_rules_v32.py --self-test | tail -1   # 223 assertions
grep -c 'A2 G7:' verifiers/check_scoped_rules_v32.py                   # 7 after the four arms land; 3 before
```

Provenance: battery `MutW2V32` §11 (round 63, post-close); landing C1 of
`plans/round-64.md`; branch from erratum E3; S120 supplies the frame (mutation
analysis over coverage, the undetected mutant as the test goal), not the arms.
````

**Two optional L1 edits.** (a) If the lane's convention requires the landing revision inside
`verified-at:`, append `; landed at <rev>` at the end of line 2 — the rest of the line stays true.
(b) The recheck names `§ The measured record`; if the § heading is renamed, re-point it.

## 2. Deliverable — S120 `used-by` cell

```
corpus/knowledge/g7-span-pinning-round64.md, corpus/lessons/round-64.md
```

This matches `ScribeSOURCESRow.md` §2 row 11 (which also names the lesson). Constraints for the
row to keep this entry's provenance true:

- The row's `source` URL is the DOI (`https://doi.org/10.1109/TSE.2021.3107634`) while this
  entry's anchor resolves against the **preprint snapshot**; both name arXiv:2102.11378v2 and the
  same two sections, so the pair is consistent. If the row's anchor cell later changes section
  numbering, only the two `S120.page:` ids in line 1 change.
- `status: mined` needs a non-`—` `used-by` — the cell above is why, and both paths must exist at
  round end (`ScribeSOURCESRow.md` §7.2 already flags the landing-order gate).
- `corpus/README.md`'s Coverage-map row is an **index** row, not a used-by entry; it is still
  required (F6).

## 3. Evidence — commands, outputs, exit codes (all read-only)

| # | command | observed |
|---|---|---|
| E1 | `sha256sum verifiers/check_scoped_rules_v32.py` | `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43` — the tree file is the sha §11 measured |
| E2 | `python3 -B verifiers/check_scoped_rules_v32.py --self-test \| tail -5` | **committed base** `12d093a1…`: `survivors closed 6 of 6` … `self-test: 0 failure(s) over 219 assertions`, `EXIT=0`; **worktree now** `f8f69cad…` (147,512 B, ` M`, uncommitted): self-test header prints `counter sha256 f8f69cad…`, tail prints `self-test: 0 failure(s) over 223 assertions`, `EXIT=0` |
| E3 | `grep -c 'A2 G7:' verifiers/check_scoped_rules_v32.py` | committed base `3` (reason strings 1063, 1066; the identifier assertion 2116); worktree now `7` — the four arm labels have landed uncommitted, and `span_missing` still opens at 1055 |
| E4 | `sed -n '1066,1070p' verifiers/check_scoped_rules_v32.py` | span-word `return` at 1066-1067, `return []` at 1068 — the plan's `1055-1068` includes the trailing return |
| E5 | `read https://arxiv.org/abs/2103.02722` (the dispatched id) | *A Markov jump process associated with the matrix-exponential distribution*, Oscar Peralta, math.PR, 2021-03-03 — not the mutation paper |
| E6 | `wc -c` + `sha256sum` on `.ufo/waves/round-64/snapshots/S120.page` | `571600` B, `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8` — ScoutS120's snapshot, the anchor target |
| E7 | `sed -n '319p;324,326p;780,782p'` on the snapshot | paragraph ids open at `319` (`S1.p1.1`) and `780` (`S3.SS2.SSS2.p1.1`); quote 1 occupies lines **324-326**, quote 2 **780-782** (minimal windows found by joining candidate spans, stripping tags and matching the sentence; RevSourcesGate re-verified 319/324 and 780/781, ScribeLesson 319/780) |
| E8 | quote presence, snapshot text with tags stripped and whitespace normalized | quote 1 `True` (23 words, citation markers `[2], [3]` follow the sentence and are outside it); quote 2 `True` (22 words) |
| E9 | `wc -l /tmp/r64/entry.md` | `120` |
| E10 | `curl -sL https://doi.org/10.1109/TSE.2021.3107634` (this seat) | HTTP 202, 0 bytes → publisher HTML not opened here; the venue/DOI fields come from ScoutS120's Crossref fetch (`ScribeSOURCESRow.md` cites it), not from this seat |
| E11 | MutSpanArms' table and lines (read-only) | v32+arms at `7791504715f3…` (147,220 B) prints `0 failure(s) over 223 assertions`, exit 0; SM1–SM6 all KILLED there (SM4 5 failures, SM6 10); A2 (`g7_conjunct`→`action_conjunct` in arm 4) **SURVIVED**, 0/223; A5 (arms 2–3 deleted) **SURVIVED behaviourally**, 0/221 |

Quote shaping, disclosed per Q42/Q53. Both quotes are substrings of the committed snapshot after
tags are stripped and whitespace normalized; the entry quotes them with their internal line breaks
**joined by single spaces** and nothing else changed. Quote 1 in the entry begins at `However,`
(the sentence start) and stops before the paper's citation markers `[2], [3]`; quote 2 is the
sentence as printed. `pdftotext` was used only to *map* the sentences to pages (p.1 / p.5) for the
first draft; the anchors that remain in the entry are a paragraph id **plus the snapshot line span**
(`sed -n '324,326p'`, `sed -n '780,782p'`, each re-checkable in one command); each quote is
`quote-equal after documented shaping` (line-join only; quote 1 also drops the paper's own
`[2], [3]` markers), never `byte-exact` in the Q56 sense, and the earlier PDF-text-layer ranges
were chrome and have been dropped.

## 4. Findings

**F1 (routed to L1, RevSourcesGate, ScoutS120) — the dispatched S120 identifier names an unrelated
paper, and the plan is wrong on two more fields.** The seat prompt ("Petrovic, Ivankovic, Ernst —
'Practical Mutation Testing at Scale', ICSE 2021; arXiv:2103.02722 or DOI
10.1109/ICSE43902.2021.00068") does not resolve: arXiv:2103.02722 is a probability paper by Oscar
Peralta (E5); the ICSE DOI resolves (via Crossref, per `ScoutS120.md`) to a deep-learning
deployment-faults paper by Chen et al.; the title-matching preprint is arXiv:2102.11378v2, whose
authors are Petrović, Ivanković, Fraser and Just, with no author named Ernst, published "submitted
to the IEEE" (venue TSE per Crossref, not ICSE). Three seats now agree independently
(ScoutS120, ScribeSOURCESRow, this seat). The plan is frozen, so the correction lives in the row,
the lesson `## Gate` and the round report — never in a plan edit.

**F2 — venue tier.** ScoutS120 proposes tier **A** for the scoped witness ("mutation analysis
measures adequacy by whether the suite detects seeded faults"). This entry's `source:` line now
names the row identity as the row will carry it (TSE via Crossref). My earlier reservation (the
assertion-coverage sentence is the paper's framing of `[2], [3]`) does not move the tier: the tier
is scoped to the detection-witness statement, which the paper does state and evaluates. RevSourcesGate
decides; the entry reads correctly under A or B.

**F3 — line range.** Plan says `v32:1055-1068`; the `span_missing` computation is 1055-1067, and
1068 is the function's trailing `return []` (E4). The entry names both so a later reader does not
score the difference as drift.

**F4 — the cheap content guard in the entry's recheck section.** `grep -c 'A2 G7:'` is `3` at base
(E3) and must be `7` once the four arms land (4 new assertion labels + the 3 existing). If the
landed patch writes a different number of `A2 G7:` strings, that comment line is wrong and must be
re-measured, not carried.

**F5 — the entry states a measurement, not a landed state.** At base the arms are absent (E2/E3).
The 219→223 record is §11's measurement on the same bytes. If C1 does not land this round, the L1
must strike the entry's final "the arms land as C1" sentence; landing the arms makes it a landed
rule. Do not land the entry as a claim that the tip already prints 223.

**F6 (routed to L1) — corpus index.** A new file under `corpus/knowledge/` without a
`corpus/README.md` Coverage-map row reads `unindexed` in `verifiers/verify_corpus_integrity.py`
(the recurring red from rounds 49–60 spot-check landings). The entry needs its Coverage-map row in
the same commit.

**F7 — arm 4's direct call is load-bearing, not stylistic.** `action_conjunct` runs A2's
page-containment arm before G7 (v32:1151 onward), so on arm 4's cell the wrapper's earlier arm
supplies the `False` and the assertion would pass for the wrong reason. A landing that "simplifies"
arm 4 to `action_conjunct` does not pin SM5. This is the one place a reviewer should check the landed
patch against §11 byte-for-byte.

**F8 — filename conflict, reported verbatim, not resolved here.** `kotoba-r64.RevSourcesGate`
proposed `corpus/knowledge/span-missing-pinning-round64.md` for the S120 `used-by` cell. The L1
assignment and `ScribeSOURCESRow.md` §2 row 11 both name
`corpus/knowledge/g7-span-pinning-round64.md`. This draft keeps the assigned name; if the L1
prefers the reviewer's, the file path and the row's `used-by` cell change together, and line 1 of
this entry does not. Until then the census's mined-used-by check would print one missing path for
whichever name is not landed.

**F9 — what the entry deliberately does not claim.** It does not claim the arms pin SM4/SM6 (they
are red through the eligible-world arm), does not claim a corpus instance of the evasion (MutW2V32's
scan found none), and does not claim the W8 or F6 debts. § Limits states each in the entry's own
words, so a reviewer can score the bound without reading the round report.

**F10 — revision 2 (non-author feedback adopted).** `kotoba-r64.RevSourcesGate` re-verified the two
anchors independently (`grep -n 'id="S1.p1.1"\|id="S3.SS2.SSS2.p1.1"\|id="abstract1.1"'` →
snapshot lines 283, 319, 780; quotes at 324 and 781) and found my first draft's PDF-text-layer
ranges (`:40-52`, `:524-527`) were **not** the quote locations — they were the paper's chrome and
the §2.2 operator list as laid out by `pdftotext`. Revision 2 replaces them with the paragraph ids
plus the snapshot line numbers, labels the journal fields Crossref-metadata-only (no seat opened
the IEEE HTML; the scout got the HTTP 202 WAF, this seat got 202/0 B), and corrects `verified-at:`
so the 223 measurement is attributed to `landed_plus_spanfix7` (sha `ae84673e…`) instead of the
219-byte base sha `12d093a1…`. All three changes are in the block above; the entry draft and the
block were diffed (`diff -u /tmp/r64/entry.md /tmp/r64/block.md` → no output) so what lands is what
was reviewed. The reviewer also dropped their `span-missing-pinning-round64.md` proposal, so F8's
conflict is closed in favour of the assigned name.

**F10b — reviewer ruling and the sha separation.** RevSourcesGate's §11.1 closes F2, F4 and the sha
contradiction, and locates the separation in the source report itself: `MutW2V32.md:864` carries
`12d093a1…` with **219** assertions, `:934` carries `ae84673e…` as `landed_plus_spanfix7` (the 223
file) — the two shas `verified-at:` names are the ones the evidence names. ScribeLesson adopted the
anchor class as **M97** after re-running it (`sed -n '40,52p'` → `initializeReadingPreferences();`,
`</script>`, `<link rel="apple-touch-icon" …>` — chrome) and added **M98** (the SCORECARD r63
annotation cites `849a546e` where the receipt says `205 assertions`; the 219 refresh is
`2ba4547f`), which is lesson-side: this entry cites no SCORECARD receipt, only the Next-line debt. The lesson-side class
they asked for ("`pdftotext -layout` line indices read as quote anchors": a re-checker following
`:40-52`/`:524-527` lands in HTML chrome and the §2.2 operator list, not the quotes) is drafted to
ScribeLesson by message; this seat does not write the lesson.

**F11 — revision 4: the 223 digest was the prototype, and the suite's own gaps are now measured in
the entry.** ScribeLesson's finding-12 caution is correct: `ae84673e…` (`MutW2V32:934`) is
`landed_plus_spanfix7`, the prototype measured before the hardened arm-4 fixture, so it can never
be the landed file's digest. Reading `MutSpanArms.md` closed both halves at once: the applied arms
are sha256 `7791504715f3…` (147,220 B), print `0 failure(s) over 223 assertions` exit 0, and kill
SM1–SM6 there (SM4 five failures, SM6 ten). Revision 4 therefore names `7791504715f3…` as the 223
measurement source and leaves the landed digest to the C1 receipt. The same report carries two
results the entry's § Limits now states: **A2** — arm 4 with `g7_conjunct` swapped for
`action_conjunct` **survives** (0/223), which confirms the wrapper-masking mechanism but also shows
the direct call is a discipline no assertion pins; **A5** — deleting arms 2 and 3 leaves
`0 failure(s) over 221`, so the negative arms' *presence* rests on the count literal alone. Both
are measured on the 223 bytes, not inferred. Entry and report block re-diffed after the edit
(`diff -u` → no output, 120 lines).

**F12 — revision 5: no digest is pinnable before the commit, so the trio names states, not a
landed sha.** ScribeLesson's second caution lands: the worktree file moved from MutSpanArms'
`7791504715f3…` (147,220 B) to `f8f69cad…` (147,512 B, ` M`) — the +292 B carries the hardened
arm-4 fixture (`mode quota`, lines 2142-2145). I measured it here rather than taking the report's
word: self-test header `counter sha256 f8f69cad…`, tail `0 failure(s) over 223 assertions`, exit 0,
`grep -c 'A2 G7:'` → 7, `span_missing` still at 1055. Revision 5 therefore gives each digest one
job: `12d093a1…` = the committed 219 base; `f8f69cad…` = the worktree 223 bytes, labelled
uncommitted, with the committed digest left to the C1 receipt; `ae84673e…` = §11's prototype;
`7791504715f3…` = MutSpanArms' measurement source for A2/A5. The entry and the block were re-diffed
after the edit (`diff -u` → no output, 120 lines).

**F13 — the lesson side is closed, by content not by revision number.** ScribeLesson recorded
the digest split as finding 13 *raised-and-fixed*, with attribution: `f8f69cad…`/147,512 B and the
four-digest separation are this seat's measurement, while their own findings rest on
`MutSpanArms:120`/`:124` and were not re-executed by them — the same discipline this report uses
in E2/E3/E11. Their M97 now cites "the entry (revision 5 at report time)" by content (paragraph id
+ line span, one job per digest, both quotes `quote-equal after documented shaping`) rather than
by a peer revision number, which is the correct form: a lesson that pins a peer file's revision
is the drift class the same row documents, and my filename/revision will not be stable if the L1
re-lands the file. No change to this entry follows from it. Remaining PENDINGs are outside this
seat: the census (`ExecGateRow`), the two claim receipts (`ExecSpanArms`/`ExecSpanBefore`,
`ExecR64Counter`), and the committed C1 digest, which cannot be pinned while the worktree carries
` M verifiers/check_scoped_rules_v32.py`.

## 5. Dependencies recorded, not awaited

- **ScoutS120** — landed while this seat worked: report, snapshot, quote, tier proposal (all cited
  above). The entry is now pointed at that snapshot and those paragraph ids; if the L1 re-snapshots
  the page, the two ids and the size/sha in line 1 are the only fields to re-measure.
- **ScribeSOURCESRow** — `used-by` cell matches. **Closed by RevSourcesGate's ruling:** a row whose
  `source` is the bare DOI URL is consistent with this entry's preprint snapshot **iff** the row's
  `anchor` carries `(Crossref metadata, publisher HTML not opened)` and the quote/digest stay
  attributed to arXiv:2102.11378v2 — which line 1 already says. No re-point to the arXiv URL; both
  spellings are contract-legal (their row validated `NF=13`, validate exit 0).
- **ExecSpanArms / MutSpanArms** — the landed arm text and the post-landing `A2 G7:` count (F4/F7);
  MutSpanArms' `7791504715f3…` is the 223 source the entry now names, while ExecSpanArms' landed
  digest (its scratch run printed counter sha256 `20aeb3ef…`) is the value the C1 receipt must pin.

## 6. Touched surfaces

- Written: this report only. No product file, no verifier, no corpus file, no git/jj state, no
  sibling lane.
- `git status --porcelain` at seat start (read-only): `M
  .ufo/waves/round-63/w2/MutW2SplitClauses.md` (the inherited r63 seat edit of C2 check 1) plus the
  untracked `.ufo/waves/round-64/` wave files.
- Tools installed or upgraded: none. Scratch under `/tmp/r64` and `/tmp/s120*` is disposable.

## 7. Out of scope

The landing patch, the receipt numbers, the r64 counter, the SOURCES row's own fields, the lesson
draft, and every judgment about whether C1 passes. This seat supplies the file and the provenance,
and reports the conflicts verbatim for the canonical judge.

Report: .ufo/waves/round-64/w1/ScribeEntry.md
