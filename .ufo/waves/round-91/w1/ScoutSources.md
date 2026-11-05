# ScoutSources — round 91 w1 (S262, S263, one rejection candidate)

Seat: **ScoutSources**. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Scope: open TWO sources and record a located quote for each, plus ONE rejection candidate that was
opened and rejected. Read-only scout: **no corpus file was written by this seat** — ScribeCorpus
drafts the rows; this report is the located-quote record the rows are measured from.

Access date for every fetch below: **2026-11-05** (UTC; host clock, `date -u` at fetch time
2026-11-05T15:09:05Z, fetch window 15:09:05Z–15:09:06Z).

---

## Result

**S262 opened and grounded** at the PIT (pitest) maintainer documentation page
`https://pitest.org/quickstart/basic_concepts` — HTTP 200, 12155 B, sha256
`c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a`. This page carries all three
notions S262 is asked to carry: a killed mutant, a survived mutant, and the equivalent-mutant
notion (with the two named grounds of equivalence).

**S263 opened and grounded** at the official Python documentation
`https://docs.python.org/3/library/subprocess.html` — HTTP 200, 208648 B, sha256
`ad6b9afdab3e06d44870cb53a3f399ce565d7993fcd34f0bda510f7196e35dac`. The located statement of the
timeout semantics is in the `subprocess.run` entry.

**One rejection candidate opened and rejected**: Wikipedia "Mutation testing" (HTTP 200, 170845 B,
sha256 `52cedf2bd7438ac219a480eaad661dc156eb92fc37eb5d97fc86dc27ed6cfdb8`) — crowd-editable, and
its mutation-score formula counts equivalent mutants in the denominator, which is the opposite
convention from the two-sided rule this round's C1 rests on.

`SOURCE_READY` (wave dir) carries the two admitted URLs.

---

## S262 — PIT (pitest) documentation, "Basic concepts"

| cell | value |
|---|---|
| URL | `https://pitest.org/quickstart/basic_concepts` (final URL after the 301: `https://pitest.org/quickstart/basic_concepts/`) |
| access date | 2026-11-05 |
| kind | docs |
| tier | **A** — scoped to *the mutation-testing outcome vocabulary and the notion of an equivalent mutation as the mutation-testing tool PIT's own maintainer documentation states them* (not this lane's battery mechanics, not a mutation score formula) |
| scope | the taxonomy of a mutant's outcome (Killed / Survived / No coverage / Non viable / Timed Out / Memory error / Run error) and the two grounds PIT names for equivalence; the second ground (a difference outside the scope of testing) is the semantics-preserving-equivalent notion the two-sided rule (Q47) needs |
| anchor | § **Equivalent Mutations** (`<h2 id="equivalent-mutations">`, HTML line 120; body HTML lines 122–146) and § **Running the tests** (`<h2 id="running-the-tests">`, HTML line 154; outcome list HTML lines 163–171; definitions HTML lines 175–179); page title "Basic concepts" (`<h1 id="basic-concepts">`). Revision anchor: the page's own upstream source file `quickstart/basic_concepts.markdown` in `hcoles/pitest-site` (branch `gh-pages`) at commit **`e8995cd59e3c`**, committed **2025-10-24T06:38:49Z** ("docs: replace 'Lived' with 'Survived' for consistency") — sha256 `2d2b7f5d3d27ace19949b4cc1948193e23cc901335c0dc8f0a24415b67613a13` (4371 B), the same file's last change in the site's `gh-pages` history (`gh-pages` tip `614bec6fd166`, 2026-06-03T08:44:50Z). Served page HTTP `last-modified: Wed, 03 Jun 2026 08:45:37 GMT`, `etag: "6a1fe9b1-2f7b"` — consistent with that tip. The three located quotes are quote-equal in BOTH the served HTML and that markdown source (tag-stripped), at markdown lines 59–60, 107 and 109. |
| teaches | a survivor is not automatically a test-suite weakness: PIT separates **Killed**, **Survived** and **No coverage** as three different outcomes, and names equivalence as the reason a mutant can survive by construction, so a two-sided measure can require every semantics-preserving equivalent to survive without charging that survival as a defect |

### S262 located quotes (verbatim, as found)

Quote 1 — the equivalent-mutant notion (the Q47 notion) — HTML lines 122–123, § Equivalent Mutations:

> not all mutations will behave differently than the unmutated class. These mutants are referred to as equivalent mutations.

* bytes: **122** · sha256 `3055e9b0bffff8624f31f29d1d2af58b5df04b2b3200c02774eef3db10ff7bc6` · 18 words
* cross-check: quote-equal in the upstream markdown at `quickstart/basic_concepts.markdown` lines 59–60 (after stripping `**`), i.e. in the file's own bytes, not only in the rendered page.

Quote 2 — a killed mutant — HTML line 175, § Running the tests:

> Killed means a test caught the mutation successfully.

* bytes: **53** · sha256 `1866d732763a8005871f4607c601853fb784570ab83daf12771ef7d6852cf3e9` · 8 words
* cross-check: markdown line 107 at `e8995cd59e3c`.

Quote 3 — a survived mutant — HTML line 177, § Running the tests:

> Survived means the mutation was not detected by the covering test.

* bytes: **66** · sha256 `264faf7df1856d92dfc5e8252a5ed05c00239b7f4c1cb1f124d6badd2f7db747` · 11 words
* cross-check: markdown line 109 at `e8995cd59e3c`.

Two further located sentences from the same page, recorded so the row's scope can be stated exactly
(they are the second ground of equivalence and the third outcome state):

* HTML line 128 — "The resulting mutant behaves in exactly the same way as the original" (64 B, 10 words)
* HTML line 146 — "The resulting mutant behaves differently but in a way that is outside the scope of testing." (88 B, 14 words)
* HTML line 179 — "No coverage is the same as Survived except there were no tests that exercised the line of code where the mutation was created." (126 B, 24 words)

### S262 fetch status line

```
url=https://pitest.org/quickstart/basic_concepts http=200 bytes=12155 eff=https://pitest.org/quickstart/basic_concepts/ time=0.020159
sha256 c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a
HTTP/2 301 -> location: https://pitest.org/quickstart/basic_concepts/
HTTP/2 200  content-type: text/html; charset=utf-8
         last-modified: Wed, 03 Jun 2026 08:45:37 GMT
         etag: "6a1fe9b1-2f7b"
         content-length: 12155
```

### S262 route ledger (honest)

- `https://pitest.org/quickstart/mutation_coverage/` → **HTTP 404** (no such page; the site has no
  per-mutant-state doc set).
- `https://pitest.org/sitemap.xml` → **HTTP 404**.
- Full nav walk of `pitest.org` (home, /about, /faq/, /quickstart/ and its subpages
  advanced/ant/basic_concepts/commandline/incremental_analysis/maven/mutators, /downloads,
  /how_to_help, /links, /weak_tests) — pages whose bytes contain the word "equivalent":
  `/quickstart/basic_concepts` (6 hits), `/quickstart/mutators` (11), `/quickstart/commandline` (1),
  `/quickstart/maven` (1); **0 hits** on the other twelve pages fetched. The FAQ page answers a
  *different* question ("I have mutations that are not killed but should be") and its answer is
  about the Java compiler's `finally`-block copying (HTML line 116 ff.), not about equivalence —
  so the FAQ is not a substitute anchor for the equivalent-mutant notion.

---

## S263 — Python documentation, `subprocess`

| cell | value |
|---|---|
| URL | `https://docs.python.org/3/library/subprocess.html` |
| access date | 2026-11-05 |
| kind | docs |
| tier | **A** — the official Python documentation, primary and authoritative for the semantics of `subprocess` timeouts |
| scope | what `subprocess` does when a child does not exit within `timeout` seconds: the `run()` contract (child killed and waited for, then `TimeoutExpired` re-raised) and the `Popen.communicate()` contract (child NOT killed) — the two differ, and the lane's guards call `subprocess.run(..., timeout=cap)`, so the `run()` contract is the one that binds them |
| anchor | § **Using the subprocess Module** → definition-list entry **`subprocess.run`** (`<dt class="sig sig-object py" id="subprocess.run">`, HTML line 270), timeout paragraph at HTML lines 288–292; contrast entry **`subprocess.Popen.communicate`** at HTML line 1042. Revision anchor: the page's own footer, HTML line 2037 — "Last updated on Nov 05, 2026 (12:47 UTC)."; page title "subprocess — Subprocess management — Python 3.15.2 documentation" (HTML line 20). Served HTTP `last-modified: Thu, 05 Nov 2026 12:49:35 GMT`, `etag: "6aec7b5f-32f08"`. |
| teaches | a timeout on `subprocess.run()` is a kill-and-wait contract, not an abandon: the child is killed and reaped before `TimeoutExpired` is raised, so a guard that catches `TimeoutExpired` can report a timeout without leaking an orphan child — while `Popen.communicate(timeout=…)` alone leaves the child running, so the two APIs are not interchangeable for a timeout gate |

### S263 located quote (verbatim, as found)

Located statement of the timeout semantics, § `subprocess.run`, HTML lines 289–291:

> If the timeout expires, the child process will be killed and waited for. The TimeoutExpired exception will be re-raised after the child process has terminated.

* bytes: **159** · sha256 `9b4db9fcb046e69ab0f1f5f0761f08891e5ff75416aeb49261a800fabb15f066` · 25 words
* the quoted string is **not** a contiguous raw-HTML substring in one line: the page breaks it across
  HTML lines 289–291 and wraps `TimeoutExpired` in a cross-reference link
  (`<a class="reference internal" href="#subprocess.TimeoutExpired" …><code …><span class="pre">TimeoutExpired</span></code></a>`).
  It is quote-equal after tag-stripping and whitespace-collapsing; no word was altered.

The contrasting statement, § `subprocess.Popen.communicate`, HTML line 1042 — recorded so the row's
scope can be stated exactly:

> The child process is not killed if the timeout expires

* bytes: **54** · sha256 `f24e2318b0ccacb8750be40034f5c62d2882e3b85a5e1cf1ce52dc0136c2bba8` · 10 words

Two further located statements on the same page, recorded for completeness of the timeout semantics:

* HTML line 1673–1675 (§ Exceptions) — "will raise TimeoutExpired if the timeout expires before the process exits." (the module-wide statement: every function and method accepting a `timeout` parameter)
* HTML line 984 (§ `subprocess.Popen.wait`) — "If the process does not terminate after timeout seconds, raise a TimeoutExpired exception."

### S263 fetch status line

```
url=https://docs.python.org/3/library/subprocess.html http=200 bytes=208648 eff=https://docs.python.org/3/library/subprocess.html time=0.020689
sha256 ad6b9afdab3e06d44870cb53a3f399ce565d7993fcd34f0bda510f7196e35dac
HTTP/2 200  content-type: text/html
         last-modified: Thu, 05 Nov 2026 12:49:35 GMT
         etag: "6aec7b5f-32f08"
         content-length: 208648
```

### Local corroboration of the `run()` contract (own-work, not a source row)

The fetched page is the **3.15.2** documentation; this host's interpreter is **Python 3.14.8**
(`/usr/lib/python3.14/subprocess.py`). The same contract is visible in the local bytes:
`subprocess.run` is defined at line 513, and its timeout handler at lines 558–571 does
`process.kill()` (line 559) then `process.wait()` (line 570) then `raise` (line 571) — i.e. the
child is killed and reaped **before** `TimeoutExpired` propagates, exactly as the located quote
states. Recorded so the quote's scope (the `run()` contract) is not over-read onto
`Popen.communicate`, whose own timeout does not kill.

---

## Rejection candidate — opened and rejected

| cell | value |
|---|---|
| URL | `https://en.wikipedia.org/wiki/Mutation_testing` |
| access date | 2026-11-05 |
| kind | community |
| tier | **C** (lead only) |
| status | rejected |
| reason | it is a crowd-editable tertiary page (a lead, never support for a tier-A-scoped claim), **and** its stated score formula is the opposite convention from the one this round's two-sided rule (Q47) rests on: the article's own sentence (located, text line 96) reads "the mutation score is the number of mutants killed / total number of mutants" — it counts equivalent mutants in the denominator, so an equivalent mutant that survives by construction is charged as a score defect, which is exactly the confusion the two-sided rule exists to prevent. The article's equivalent-mutant sentence (text line 125, "Such mutants are called equivalent mutants") is a usable lead but is uncited at that point and carries no authority over the denominator question. |
| flip condition | re-open and admit as a **lead-only** row if a future claim needs plain-language orientation to the equivalent-mutant notion and no primary source states it directly — or, if the article is revised so its score formula excludes equivalent mutants from the denominator **and** cites a primary source for that exclusion, in which case the score sentence becomes quotable as a tertiary summary (never as the authority for the denominator). The current revision (`oldid=1373580212`, "This page was last edited on 6 September 2026, at 19:05") does not qualify. |

### Rejection fetch status line

```
url=https://en.wikipedia.org/wiki/Mutation_testing http=200 bytes=170845 eff=https://en.wikipedia.org/wiki/Mutation_testing time=0.321702
sha256 52cedf2bd7438ac219a480eaad661dc156eb92fc37eb5d97fc86dc27ed6cfdb8
HTTP/2 200  content-type: text/html; charset=UTF-8
         last-modified: Fri, 30 Oct 2026 04:02:13 GMT
         content-length: 170845
page revision: wgCurRevisionId 1373580212 — "This page was last edited on 6 September 2026, at 19:05"
```

---

## Route ledger — sources opened and NOT proposed as rows

**Jia & Harman survey (the plan's third-choice route for S262) — opened, reachable, but not
proposed, and the reason is already the corpus's own standing judgment.** The plan lists it as a
fallback; it was fetched and read:

- `https://mutationtesting.uni.lu/TR-09-06.pdf` → **HTTP 200, 434884 B**, `application/pdf`, sha256
  `ea504d791f2462c281db555c327503975dafda036bef845263c2c97ea5b56ab9` (the King's College London
  technical-report version of the IEEE TSE 37(5):649–678 (2011) paper). PDF text line 584 locates the
  equivalent-mutant definition: "These mutants are called Equivalent Mutants." and lines 585–587
  "They are syntactically different but functionally equivalent to the original program."
- `https://dl.acm.org/doi/10.1109/TSE.2010.62` (publisher record) → **HTTP 403**, 5480 B challenge
  page; `https://ieeexplore.ieee.org/document/5971769` → **HTTP 202, 0 B** (bot wall).
- **Why it is not proposed:** the lane's corpus already screened this exact work out — `corpus/SOURCES.md`
  (round-64 search log, lines 414–417) records "Jia and Harman, 'An Analysis and Survey of the
  Development of Mutation Testing', IEEE TSE 37(5):649–678, 2011: secondary survey, tier B at best,
  and it duplicates S120's scope". Re-proposing it as S262 would reopen a rejection the corpus has
  already ruled on, and S260 (Stryker's own docs) plus S120 already carry the killed/survived/
  equivalent vocabulary. The PIT page is the primary/maintainer route the plan's first choice names
  and it states all three notions in one place, so the survey is left as a lead in this report only.

---

## Findings for the scribe (row content is ScribeCorpus's to draft)

1. **Row ids.** S262 and S263 are the two admitted rows this round. The rejection row is a third
   registry row; the corpus's next free id after `S261` is `S264`. No id is asserted here — the
   scribe owns the numbering.
2. **Census-count arithmetic — the scribe and L1 should measure, not assume.** The plan's Frontier
   step predicts the census going `187 → 189`. The plan's own counting command is
   `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`, currently **187**,
   and it counts **rejected** rows too — the 187 decompose as 163 `mined` + 7 `queued` +
   17 `rejected` (measured: `bash scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotoba`
   → `kotoba rows 187`, `status.mined 163`, `status.queued 7`, `status.rejected 17`, exit 0).
   Therefore **187 + 2 = 189 is reached only if the rejection candidate lands OUTSIDE the
   registry table** — as prose in the search log, the way the round-64 exclusions were recorded
   (`corpus/SOURCES.md` lines 405–418 are prose, not `| S### |` rows). If the rejection is instead
   appended as a registry-shaped `| S264 | … | rejected |` row, the count becomes **190** and the
   plan's "189 expected" is off by one. Both shapes satisfy the contract (a `rejected` registry row
   is legal — `S011` is one), so this seat does not choose: the count must be measured after the
   scribe's append and the plan's expectation stated or corrected at integration. Flagged because a
   silent 190-vs-189 mismatch would read as a census regression.
3. **Census `E04`/`W04` are clear for the two admitted URLs** — neither
   `https://pitest.org/quickstart/basic_concepts` nor
   `https://docs.python.org/3/library/subprocess.html` occurs anywhere in the current registry
   (the only `docs.python.org` URLs present are `.../library/tempfile.html` and `.../library/json.html`),
   and no `wikipedia` URL is present either. Measured: `grep -c 'wikipedia' corpus/SOURCES.md` → 0.
4. **`E11` (used-by path must exist on disk)** — the two rows' `used-by` cells must name the two
   knowledge files the plan names: `corpus/knowledge/mutation-battery-arms-round91.md` (C1, cites
   S262) and `corpus/knowledge/timeout-calibration-round91.md` (C2, cites S263). Neither file exists
   yet; both are ScribeCorpus's to create in this wave, so the `used-by` paths become valid only
   once that append lands.
5. **Suggested `recheck` cadences** (the scribe's call): PIT's page is a tool's own documentation
   that ships with releases → `on-release`; the Python documentation page → `365d` (matching the
   cadence used by the two existing `docs.python.org` rows, `S007` and `S253`).
6. **`opened` cell** for all three rows: `2026-11-05`.
7. **Tier discipline.** S262 = A, S263 = A, the rejection = C with status `rejected`. A rejected
   row is `kind community` at tier C, so `E10` (community at tier A) does not fire.
8. **Quote grounding form.** Per the round-89 note recorded in the round-90 scout report, the
   digests above are fetch-time metadata; the quotes are grounded in **line anchors + byte size +
   page title**, never in the digest. Line numbers are anchors into the bytes this seat saved
   (`S262-pitest-basic_concepts.html`, `S263-python-subprocess.html`), not stable upstream
   coordinates. The one upstream-stable anchor available is the PIT markdown source at commit
   `e8995cd59e3c`, where all three S262 quotes are quote-equal — that is the strongest anchor in
   this set and is the one the S262 row should carry.

---

## Risks

- **Scope overlap between S260 and S262 (flagged, not resolved here).** S260 is Stryker's own
  "Mutant states and metrics" page and already carries the killed/survived/equivalent vocabulary
  and the mutation-score definition at tier A. S262 as scoped above is a **second tool's** maintainer
  documentation and adds two things S260 does not state in this form: the **third outcome state**
  (`No coverage`, distinct from `Survived`) and the **two named grounds of equivalence** (behaves
  exactly as the original; behaves differently but outside the scope of testing). The S262 row's
  scope cell should say so explicitly, or the two rows read as duplicates. This is a scribe-side
  wording decision; the sources themselves are distinct (different URL, different tool, different
  maintainer) and raise no census duplicate-URL finding.
- **Live-page volatility.** Both admitted URLs are live documentation pages fetched on 2026-11-05;
  the Python page self-declares "Last updated on Nov 05, 2026 (12:47 UTC)" — i.e. it was rebuilt the
  same day — so line anchors move. The quotes, byte sizes and page titles are the durable facts.
- **Version skew between the fetched doc and this host.** The S263 page is the 3.15.2 documentation;
  the host runs 3.14.8. The `run()` contract was re-checked against the host's own
  `/usr/lib/python3.14/subprocess.py` (lines 558–571) and matches, but the row should not claim the
  3.15.2 text describes the host's interpreter.
- **No defect in the plan or in the frozen controls was found.** The plan's S262 route order
  (PIT documentation first, Stryker's page excluded because it is S260) is satisfiable as written:
  PIT's page states all three required notions with located quotes.
- **The `S263` wording choice is the one the C2 leg actually depends on.** C2 leg A calibrates
  `SELF_TEST_TIMEOUT_S` for `subprocess.run(..., timeout=cap)` children; the located `run()` quote
  is the one that binds, and the `Popen.communicate` quote is the contrast that keeps the row's
  scope honest. A row that quoted only `Popen.communicate`'s sentence would state the **wrong**
  contract for the lane's own call site.

---

## Evidence files written by this seat (all under this seat's wave dir)

| file | bytes | sha256 |
|---|---|---|
| `S262-pitest-basic_concepts.html` | 12155 | `c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a` |
| `S262-upstream-basic_concepts.markdown` (at `e8995cd59e3c`) | 4371 | `2d2b7f5d3d27ace19949b4cc1948193e23cc901335c0dc8f0a24415b67613a13` |
| `S263-python-subprocess.html` | 208648 | `ad6b9afdab3e06d44870cb53a3f399ce565d7993fcd34f0bda510f7196e35dac` |
| `rej-wikipedia-mutation-testing.html` | 170845 | `52cedf2bd7438ac219a480eaad661dc156eb92fc37eb5d97fc86dc27ed6cfdb8` |
| `fetch-log.txt` | — | fetch status lines, response headers, route probes |
| `quote-receipts.txt` | — | per-quote bytes, sha256, word count, anchor |

## Constraints honoured

- Writes confined to `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-91/w1/ScoutSources/`
  plus this seat's report file and the mandated `SOURCE_READY` handoff marker. **No corpus file was
  written** (`corpus/SOURCES.md` untouched — ScribeCorpus owns the rows).
- **No git or jj write** was run against the lane, the fleet root, or any sibling lane; no `add`,
  `commit`, `stash`, `checkout`, `reset`, `switch`, `pull`, `push`, `branch`, or mutating `jj`
  command. Read-only git was not needed by this seat.
- Nothing was written to the fleet root, a sibling lane, `considerthese/`, `.ufo/state/`,
  `.ufo/watchdog.log`, `MANIFEST.json`, `scripts/`, `templates/`, or `/home/vgpnk/Projects/shokuknow`.
- No host or kernel setting was changed; no `sysctl -w`, no write to `/proc/sys`. No tool was
  installed or upgraded this seat (`curl` and `python3 -B` from the system were used).
