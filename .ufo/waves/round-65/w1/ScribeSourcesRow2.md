# ScribeSourcesRow2 — S121 row audit against SOURCES-CONTRACT-v1 (+ census + freshness)

Seat: scribe, wave `kotoba-r65-w1`, 2026-10-24. Judged axis: **freshness**.
Lane bounds respected: read-only outside this file; no git/jj writes; scratch only under
`/tmp` (`/tmp/r65` = `git archive` export of the measured rev, `/tmp/SOURCES-c98d137.md`,
`/tmp/S121-refetch.pdf`); at most 2 concurrent processes; no subagent dispatch.

Revs audited (all resolved, all ancestors of `master`):

| rev | role | resolved |
|---|---|---|
| `c98d137` | before-state / r64 close (base for the diff) | `c98d1378236bae56d9d2ecacd5db59a4cc142e1e` |
| `80bb8921` | round-65 implementation (C1/C2 surfaces) | `80bb89211841289bc802fa7b55057f0ef266d19e` |
| `5253b281` | round-65 receipts | `5253b28174a17dccba8db391b2a5b9bc6470472a` |
| `0e104f49` | round-65 frontier (the S121 row lands here) | `0e104f498b3df1466284074c5b3a6e5b523420cd` |
| `2a8eba56` | live HEAD at audit time (round 66) | clean `corpus/`; only peer `.ufo/` report files untracked |

---

## 1. The S121 row, re-read at `0e104f49` (`corpus/SOURCES.md:132`)

Verbatim cell dump (11 cells, NF=13; produced by splitting the line on `|`):

| # | column | value |
|---|---|---|
| 1 | id | `S121` |
| 2 | source | `Overcoming the Equivalent Mutant Problem: A Systematic Literature Review and a Comparative Experiment of Second Order Mutation (Madeyski, Orzeszyna, Torkar, Józala) — https://madeyski.e-informatyka.pl/download/Madeyski13TSE.pdf` |
| 3 | kind | `paper` |
| 4 | tier | `A` |
| 5 | scope | `Primary peer-reviewed study for the claim this row scopes: second-order mutation — coupling two first-order mutation sites into one mutant — is a designed, measured strategy whose benefit is fewer equivalent mutants and lower test effort; a witness carrying an honest span beside a fabricated span is a first-class adequacy check, not an artificial one. Scoped to SOM's measured advantages; the lane's two-span verifier arm is the lane's application, not the paper's object. Author-hosted preprint v.2 of the IEEE TSE paper; the publisher record is DOI 10.1109/TSE.2013.44 (from the PDF header line 90)` |
| 6 | anchor | `author-hosted preprint v.2 PDF of IEEE TSE 40(1):23-42, Jan 2014, the artifact opened and quoted: abstract (PDF text line 64), §5 HOM-generation strategies paragraph (PDF text lines 1174-1176); opened 2026-10-24 (HTTP 200, 1,126,684 B, application/pdf, sha256 \`bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3\`); snapshot \`.ufo/waves/round-65/snapshots/S121.pdf\` with extracted text \`S121.txt\` (quotes verified against it whitespace-normalized)` |
| 7 | teaches | `"The experiment indicated that SOM in general and JudyDiffOp strategy in particular provide the best results" — abstract, 16 words; support quote (lines 1174-1176): "Empirical results suggest that applying SOMs reduced the number of mutants by approximately 50%, without much decrease in the quality of the test suite."` |
| 8 | status | `mined` |
| 9 | opened | `2026-10-24` |
| 10 | recheck | `180d` |
| 11 | used-by | `corpus/knowledge/g7-span-closure-round65.md, corpus/lessons/round-65.md` |

### 1a. Row assertion battery (exit 0; all PASS)

Run: `cd /tmp/r65/kotoba-shokunin && python3 - <<'PY' … PY` (14 assertions over the row;
the script is a transcription of the contract's census rules, not a project instrument):

```
S121 rows found: 1
NF (awk -F|): 13 | cells: 11
PASS - id pattern S+3digits
PASS - kind in enum
PASS - tier in ABC
PASS - status in enum
PASS - community never A
PASS - opened ISO and <= today
PASS - recheck ISO or cadence
PASS - mined => >=1 used-by
PASS - used-by exists: corpus/knowledge/g7-span-closure-round65.md
PASS - used-by exists: corpus/lessons/round-65.md
PASS - no backtick-pipe escape needed
PASS - id unique
PASS - url unique across registry (raw)
PASS - anchor has a line/section locator
sha256 of snapshot: bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3
snapshot bytes: 1126684
```

Interpretation:

- **11 well-formed cells** — yes: NF=13 under `awk -F'|'`, and no `|` smuggled inside a
  cell (the two quotes contain em-dashes and semicolons, no pipes).
- **kind** — `paper` ∈ contract enum
  `spec · docs · paper · code · tool · dataset · talk · book · community · own-work`.
- **tier** — `A` ∈ `ABC`; row is `paper`, so the contract's inflation rule (`community` is
  never A) is not triggered. **Scoped, not inflated:** the scope cell names the exact
  claim ("SOM's measured advantages") and explicitly disclaims the lane's application
  ("the lane's two-span verifier arm is the lane's application, not the paper's object").
  Tier A rests on contract clause "original paper"; the artifact is the author-hosted
  preprint v.2 whose header carries the IEEE TSE pagination, and the scope cell says so
  rather than implying the publisher copy was read. *[INFERENCE] I judge A correct for
  this scope; the only residual is preprint-vs-version-of-record, which the row discloses.*
- **status** — `mined` ∈ enum, and `mined` requires ≥1 used-by path (contract); both paths
  exist on disk at the measured rev (`git cat-file -e 0e104f49:<path>` → EXISTS for both);
  the census E11 pass over all 111 mined rows printed nothing.
- **opened / recheck** — `2026-10-24` is the round date and not future (E08 clean);
  `180d` is a contract cadence; `overdue` reports `S121 recheck=180d opened=2026-10-24`
  as a symbolic cadence with no overdue finding (exit 0) — due 2027-04-22 by the
  census's `opened + N` rule.
- **id** — c98d137 max id was `S120` (`git show c98d137:corpus/SOURCES.md | grep -oE '^\| S[0-9]{3,}' | sort | tail -3`
  → S118, S119, S120), so `S121` is "the next unused"; no duplicate id, no URL shared
  with another row (raw-URL count 1; the fleet `validate` also reports no E04 for it).

### 1b. Contract rule 1 (a row is a claim) — satisfied

`corpus/lessons/round-65.md` § Gate records, for S121: the URL; access
`2026-10-24 (HTTP 200, 1,126,684 B, application/pdf, sha256 bad1b681…)`; a **16-word**
gate quote with location (`abstract, PDF text line 64`); a 24-word support quote at
`lines 1174-1176`; the identity read from the opened bytes (authors, venue, p. 23, DOI
from header line 90); and the rejected first candidate (arXiv:1309.4818, M101). I
re-checked the quote strings against the committed snapshot:

```
abstract quote normalized-match: True
word count: 16
support quote normalized-match: True
```

(`re.sub(r'\s+',' ')` over `.ufo/waves/round-65/snapshots/S121.txt`; the abstract sentence
wraps lines 64-65, the support quote sits exactly on 1174-1176.)

---

## 2. No in-place edits elsewhere — exactly one added line

```
$ git diff --numstat c98d137..0e104f49 -- corpus/SOURCES.md
1	0	corpus/SOURCES.md

$ git diff --stat c98d137..0e104f49 -- corpus/SOURCES.md
 corpus/SOURCES.md | 1 +
 1 file changed, 1 insertion(+)

$ git diff c98d137..0e104f49 -- corpus/SOURCES.md | grep -c '^+[^+]'   → 1
$ git diff c98d137..0e104f49 -- corpus/SOURCES.md | grep -c '^-[^-]'   → 0
$ git show c98d137:corpus/SOURCES.md | grep -c '| S121 |'             → 0
```

The single hunk is `@@ -129,6 +129,7 @@` and its only `+` line is the S121 row, inserted
above the blank line before `## Paths`. Contract rule 2 (append-only; only `status`,
`recheck`, `used-by` change in place) is therefore satisfied — no other row's cell was
touched, and the lesson's § Status changes says so too ("No other registry row changed").

Commit-level check (a revert round-trip would be invisible in the endpoint diff, so I
listed every commit in the range that touches the file):

```
$ git log --format='%h %s' c98d137..0e104f49 -- corpus/SOURCES.md
0e104f4 round-65: frontier step (S121 row + snapshot, g7-span-closure entry, round-65 lesson M99-M101, README index, census-after 119 rows exit 0) + SCORECARD round-65 annotations/Next-66 + SHONEN refresh
```

One commit, `1 0` numstat, one added line. **No in-place edit exists anywhere in the range.**

---

## 3. Census, re-run (histograms pasted)

### 3a. Contract census block, run from the lane root

```sh
# rows
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
# malformed rows — 11 columns means NF=13; must print 0
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
# tier histogram / status histogram / dup ids / enum violations / mined used-by existence
```

| tree | rows | malformed (NF≠13) | tier histogram | status histogram | dup ids | enum/inflation | missing used-by |
|---|---|---|---|---|---|---|---|
| `c98d137` (before) | **118** | 0 | `A=115 B=2 C=1` | `mined=110 queued=7 rejected=1` | none | none | none |
| `0e104f49` (after) | **119** | 0 | `A=116 B=2 C=1` | `mined=111 queued=7 rejected=1` | none | none | none |
| live HEAD `2a8eba56` (r66) | **120** | 0 | `A=117 B=2 C=1` | `mined=112 queued=7 rejected=1` | none | none | none |

The +1 row / +1 tier-A / +1 mined is exactly S121 and nothing else (the r66 row S122 is the
live-tree delta, outside this claim).

Raw output at `0e104f49` (export `/tmp/r65/kotoba-shokunin`):

```
### ROUND-65 TREE @0e104f49 ###
--- rows ---
119
--- malformed (must be 0) ---
0
--- tier histogram ---
A=116 B=2 C=1
--- status histogram ---
mined=111 queued=7 rejected=1
--- duplicate ids (must be empty) ---
--- enum violations / tier inflation (must be empty) ---
--- mined used-by missing (must be empty) ---
--- done rc=0 ---
```

### 3b. Fleet census (`scripts/sources-census.sh`)

```
$ scripts/sources-census.sh census /tmp/r65/kotoba-shokunin          # round-65 bytes
kotoba-shokunin	rows	119
kotoba-shokunin	tier.A	116
kotoba-shokunin	tier.B	2
kotoba-shokunin	tier.C	1
kotoba-shokunin	status.mined	111
kotoba-shokunin	status.queued	7
kotoba-shokunin	status.rejected	1
FLEET	rows	119
FLEET	tier.A	116
FLEET	tier.B	2
FLEET	tier.C	1
FLEET	tier.invalid	0
FLEET	status.queued	7
FLEET	status.mined	111
FLEET	status.rejected	1
FLEET	status.invalid	0
census-rc=0

$ scripts/sources-census.sh validate /tmp/r65/kotoba-shokunin     # 16 W04 + ok, exit 0
kotoba-shokunin	W04	S018 duplicate url agentskills.io/specification across scopes
… (W04 for S019, S021, S054, S055, S056, S065, S086, S103, S104, S106, S110, S111, S114, S115, S118) …
kotoba-shokunin	ok	/tmp/r65/kotoba-shokunin/corpus/SOURCES.md
validate-rc=0
```

```
$ scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotoba     # live r66
kotoba	rows	120
kotoba	tier.A	117
kotoba	tier.B	2
kotoba	tier.C	1
kotoba	status.mined	112
kotoba	status.queued	7
kotoba	status.rejected	1
…
census-rc=0
$ scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
… 16 × W04 (same set) …
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
validate-rc=0
```

**Receipt reproduction:** my `validate` re-run at `0e104f49`, with the lane label and path
normalized to the receipt's, is byte-identical to `.ufo/waves/round-65/census-after.txt`
(`diff … && echo RECEIPT-MATCHES-RERUN` → `RECEIPT-MATCHES-RERUN`; 17 lines).

**Receipt nuance (finding F4 below):** `census-before.txt` and `census-after.txt` are
**byte-identical** (`diff` → `IDENTICAL`) because `validate` output is row-count-free
(16 W04 diagnostics + `ok`, unchanged by a clean row). The 118→119 growth is evidenced by
`census` mode (which the plan quoted but did not save as a receipt) and by my grep counts,
not by the receipt pair.

**Freshness queue:** `scripts/sources-census.sh overdue --root … kotoba` → exit 0; S121
appears as `kotoba	cadence	S121 recheck=180d opened=2026-10-24`; no row is overdue.

---

## 4. Freshness probes

| probe | command | result |
|---|---|---|
| live re-open of the source | `curl -sS -D - -o /tmp/S121-refetch.pdf https://madeyski.e-informatyka.pl/download/Madeyski13TSE.pdf` | `HTTP/1.1 200`, `Content-Type: application/pdf`, `Content-Length: 1126684`, `Last-Modified: Mon, 25 Aug 2014 12:21:18 GMT`; curl-rc=0 |
| snapshot identity | `sha256sum /tmp/S121-refetch.pdf` | `bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3` — **identical to the row's pin and to the committed snapshot** (row's `bad1b681…`, snapshot 1,126,684 B) |
| artifact static? | server `Last-Modified` 2014-08-25 | the author-hosted artifact has not changed since 2014; no drift can be hidden by cache |
| row stable after the frontier | `sha256sum` of the `S121` line at `HEAD` vs `0e104f49` | both `b8d19614a987bc062e3e03068b876b903ad88da99c7eeb23e2bd508b7116e17c` — **byte-identical**; commits after the frontier that touch SOURCES.md (`9e75e73`, `806b53b`) added S122 only |
| DOI metadata (publisher record, opened today) | `read https://api.crossref.org/works/10.1109/TSE.2013.44` | `"volume": "40"`, `"issue": "1"`, `"page": "23-42"`, `"published-print": 2014-01`, `"publisher": "IEEE"`, title exact, authors Madeyski / Orzeszyna / Torkar / Jozala |
| bib numbers from the opened bytes | `sed -n '1,8p;86,92p' .ufo/waves/round-65/snapshots/S121.txt` | line 1 `IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, VOL. 40, NO. 1, JANUARY 2014 (PREPRINT V.2)`, printed page `23`; DOI `10.1109/TSE.2013.44` on line 90 |
| page span of the opened artifact | bare page markers in `S121.txt` | `39, 40, 41, 42, 43, 44` — the PDF's printed pages run **23–44** (22 pages) |
| non-author independent check | `corpus/lessons/round-65-verifier-spotcheck.md` (commit `11385e0`, descendant of `0e104f49`) | third-party seat re-opened the row and the source and records **agree** on the admit, the row, and the arXiv rejection |
| used-by entry's own pin | `python3 -B verifiers/check_scoped_rules_v32.py --self-test` on the `0e104f49` export | exit 0; `survivors closed 6 of 6`; `self-test: 0 failure(s) over 234 assertions`; instrument sha256 `b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d` — matches the knowledge entry's `verified-at: tip 80bb8921, v32 sha256 b6cfc764…, 234 assertions` |
| instrument drift at HEAD | `sha256sum verifiers/check_scoped_rules_v32.py` (live) | `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` — the round-66 tree has moved the verifier; the entry's pin is round-scoped (names `80bb8921`) and is not falsified, but it is not a HEAD measurement [INFERENCE: HEAD's assertion count not asserted by me] |

Sibling cross-check: `.ufo/waves/round-65/w1/ScoutS121Reopen.md` (peer scout) independently
re-fetched the source and found bytes identical; my findings agree with it except that I
close its `[INFERENCE]` about the page range with the Crossref lookup (§4) and I add the
locator gap in §5 F3.

---

## 5. Findings

**F1 — contract rule 5 gap: no `## Search log` note for round 65 (registry-level, not row-level).**
`git show 0e104f49:corpus/SOURCES.md | grep -cF '1309.4818'` → **0**; the `## Search log`
section's `2026-10-24` entries are all round-64 (S120 opening, S049 live re-probe) plus a
placement correction. The round-65 bounded search — the arXiv:1309.4818 candidate opened and
rejected, the replacement S121 opened and included — is recorded only in `plans/round-65.md`,
`corpus/lessons/round-65.md` (§ Gate, M101) and `corpus/README.md`
(`grep -rIl '1309.4818'` over the export → those three files; not SOURCES.md). Contract shape
requires "one prose note per bounded search (rule 5)" with identified/screened/included/excluded
counts and a stop rationale, and the plan's frontier sentence says the rejection is "recorded
in the search log" — as written that sentence is not true of `corpus/SOURCES.md`. Round 66
shows the intended form (the appended "search-query clarification" note for S122). Append-only
fix available to a later round; the S121 row itself is unaffected.

**F2 — page range is the publisher's, but the row attaches it to the preface artifact.**
Cells 5/6 say "IEEE TSE 40(1):23-42" for the author-hosted preprint. The opened PDF's own
printed page numbers run 23–44 (markers 39,40,41,42,43,44; 22 pages). Crossref confirms
`page: 23-42` for the version of record, and the lesson's Gate correctly says only "p. 23" and
"the publisher record was not opened". So the number is true of the journal article but is not
observable in the cited artifact; the anchor wording implies it was. Low severity; the
only correct fix would be a wording note (append-only) or a superseding row, and my Crossref
probe now supplies the missing provenance.

**F3 — the `teaches` clause "lower test effort" is true of the paper but outside the row's named locators.**
The row names abstract line 64 and lines 1174-1176. "Test effort" is stated at
**lines 1115-1116**: "SOM has potential advantages … e.g. reducing the number of equivalent
mutants [30], [57], [63] and reducing test effort (testing time) due to a reduced number of
produced second order mutants" (echoed at 2456). The abstract's areas list at line 65
("mutation testing time; time needed for manual classification") is also outside the named
quote. Claim not falsified — the paper says it — but the locator set is one line short of the
teaching sentence. [INFERENCE] severity low; the row's quote discipline is otherwise exact
(16/24 words, both verbatim, both at the stated lines).

**F4 — receipt pair cannot show the census delta.** `census-before.txt` and
`census-after.txt` are byte-identical; `validate` mode emits no row count. The 118→119 growth
is only visible in `census` mode (my re-run: `kotoba rows 119`, `census-rc=0`) and in the
registry itself. Not a false claim — the plan states "validate … 118 rows" — but a later
reader should not expect the delta in the pair.

**F5 — instrument drift at HEAD (disclosure, not a falsification).** The S121 used-by entry
pins `verified-at: tip 80bb8921, sha b6cfc764…, 234 assertions`; that pin reproduces on the
`0e104f49` bytes (I ran it). At live HEAD the same file hashes `97d89716…`, so the pin is
historical by construction (it names its tip) and must not be read as a current measurement.

**F6 — positives worth recording.** The row's snapshot pin reproduces against the live
network today (byte-identical, static since 2014); the row is byte-identical at HEAD; the
row's id/URL are unique; E11/E12 are clean; the non-author spot-check agrees.

---

## 6. Claims supported / falsified

Supported:

- "S121 is a well-formed, contract-v1 row" — 11 cells, NF=13, enums pass, tier A scoped by
  its own scope text, `mined` backed by two existing used-by paths, anchor with line locators
  and revision, opened date not future, `180d` cadence.
- "The registry change is a single append" — `1 0` numstat, one commit
  (`0e104f4`), one added line, zero deletions, no in-place cell edits in any commit of
  `c98d137..0e104f49`.
- "Census after: 119 rows, exit 0, 16 W04, tier A=116/B=2/C=1, mined=111/queued=7/rejected=1"
  — reproduced; `validate` receipt byte-identical after label/path normalization.
- "The S121 row cites the artifact actually opened" — snapshot sha256 and size reproduce
  from a fresh fetch; both quotes verbatim at the stated lines; DOI at header line 90.
- "S121's used-by entry's measurement (`234 assertions`, sha `b6cfc764…`) holds at the
  round-65 bytes" — reproduced on the `0e104f49` export.

Falsified / corrected:

- The plan's "recorded in the search log" (frontier step) — **not** in `corpus/SOURCES.md`'s
  `## Search log` at `0e104f49`; the record lives in the plan, the lesson's Gate/M101, and
  the README (F1).
- The row's "23-42" attributed to the opened preprint — the artifact spans printed pages
  23–44; 23–42 is the Crossref publisher record (F2).
- The implicit reading that the two census receipts are a before/after pair — they are
  identical (F4).

---

## 7. Out of scope (named, not judged)

- C1's kill battery (17 lanes) and C2's governance mechanism: other seats own those; I only
  re-ran the C1 self-test as a freshness probe for the S121 used-by entry.
- Round-66's S122 row and the `9e75e73`/`806b53b` SOURCES edits: outside the round-65 claim;
  reported only as the live-tree delta (120 rows).
- Tier A preprint-vs-publisher judgment beyond the row's own scope wording: noted, not
  escalated.
- No fix applied: append-only corrections (search-log note, anchor wording) belong to a
  later round; this seat writes only this report.

## 8. Tooling

No installs or upgrades this seat (uv/pacman untouched; pacman pause respected). Tools used
were pre-installed: `git`, `awk`, `grep`, `python3`, `curl`, `sha256sum`, `diff`, plus the
lane's own `scripts/sources-census.sh`.

## 9. Artifacts

- This report: `.ufo/waves/round-65/w1/ScribeSourcesRow2.md`
- Scratch (not committed, `/tmp`): `/tmp/r65/kotoba-shokunin` (git-archive export of
  `0e104f49`), `/tmp/SOURCES-c98d137.md`, `/tmp/s121-r65.txt`, `/tmp/s121-live.txt`,
  `/tmp/S121-refetch.pdf`, `/tmp/census-rerun.txt`, `/tmp/s121-headers.txt`.
- Read-only inputs relied on: `.ufo/waves/round-65/{census-before,census-after}.txt`,
  `.ufo/waves/round-65/snapshots/S121.{pdf,txt}`, `corpus/lessons/round-65.md`,
  `corpus/knowledge/g7-span-closure-round65.md`, `corpus/lessons/round-65-verifier-spotcheck.md`,
  `.ufo/waves/round-65/w1/ScoutS121Reopen.md`,
  `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`.
