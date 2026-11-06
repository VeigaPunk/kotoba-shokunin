# ScoutSourcesR96 — C1's two sources re-opened, two candidates judged

Seat: ScoutSourcesR96 (round 96, wave r96-w1). No repo writes; receipts under
`.ufo/waves/round-96/w1/ScoutSourcesR96/`.
All fetches: `curl -sS -L`, host `vgpnk`, 2026-11-06, UTC 03:0x (response `date:` headers below).
Scratch: `/fast/scratch/hyaku/kotoba-r96/ScoutSourcesR96` (removed before yield).

## 1. Re-open of the two sources the plan cites (verified against the L1 receipt)

### 1.1 PIT — "Mutation operators" — https://pitest.org/quickstart/mutators/

| field | value |
|---|---|
| access date | 2026-11-06 (response `date: Fri, 06 Nov 2026 03:08:23 GMT`) |
| HTTP | 200 (`HTTP/2 200`, `content-length: 67033`, `last-modified: Wed, 03 Jun 2026 08:45:37 GMT`, `etag: "6a1fe9b1-105d9"`) |
| bytes | 67033 |
| sha256 | `a31331daf89f246f3e02c0da92578d4ad2163c53741c3700437e75b9a1602da2` |
| equals L1's? | **YES** — byte-identical to `receipts/sources-opened.txt` (size and sha256 both match) |
| title | `<title>Mutation operators</title>` |

Located quote (16 words, `wc -w` = 16), HTML **lines 317–319**:

```
317: <p>The conditionals boundary mutator replaces the relational operators <code class="language-plaintext highlighter-rouge">&lt;, &lt;=, &gt;, &gt;=</code></p>
318:
319: <p>with their boundary counterpart as per the table below.</p>
```

The sentence is split across two `<p>` elements by a blank line 318; the quote is the two `<p>` bodies
joined with the blank line dropped — **quote-equal after documented shaping** (Q56), not byte-exact.
The heading is line 313: `<h2 id="conditionals-boundary-mutator-conditionals_boundary">Conditionals Boundary Mutator (CONDITIONALS_BOUNDARY)</h2>`.

The `<=` → `<` table row, HTML **lines 333–336** (cells at 334 and 335):

```
328:   <tbody>
333:     <tr>
334:       <td>&lt;=</td>
335:       <td>&lt;</td>
336:     </tr>
```

The full table is lines 329–344 (`<`→`<=`, `<=`→`<`, `>`→`>=`, `>=`→`>`). The `<=`→`<` direction that
target `t04-le-to-lt` needs is the second row, verbatim on the page.

**Verdict: ADMIT (recommends S271).** Tier **A** — the mutation-testing tool's own documentation, official
docs for the scope "the boundary mutation class and its operator table". Distinct document from the
registry's PIT rows: S262 and S269 both hold `https://pitest.org/quickstart/basic_concepts` (outcome
vocabulary), this is `quickstart/mutators` — `grep -c 'quickstart/mutators' corpus/SOURCES.md` = **0**.
Scope must stay on the operator table (it grounds `t04`); it is not a mutation-score or outcome-vocabulary
source (S262/S269 keep that).
**Flip condition:** the re-open loses the `<=`→`<` row or the boundary sentence (page revision), or a
registry row on this exact URL appears first (Q84 — then cite that id instead of adding a row).

### 1.2 POSIX.1-2024 XCU — "Shell Command Language", § 2.6.2 Parameter Expansion — https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html

| field | value |
|---|---|
| access date | 2026-11-06 (response `Date: Fri, 06 Nov 2026 03:08:24 GMT`) |
| HTTP | 200 (`HTTP/1.1 200 OK`, `Content-Length: 357953`) |
| bytes | 357953 |
| sha256 | `0889867a53fe12508a71e8739ec23ecdddc95e6f67697c98e26acc8ff0ec1acd` |
| equals L1's? | **YES** — byte-identical to `receipts/sources-opened.txt` |
| title | `<title>Shell Command Language</title>` |

Section heading, HTML **line 777**: `<h4><a name="tag_19_06_02" id="tag_19_06_02"></a>2.6.2 Parameter Expansion</h4>`.

Located quote (22 words, `wc -w` = 22), HTML **lines 790–791** (the sentence continues to line 792):

```
790: <p class="tent">The parameter name or symbol can be enclosed in braces, which are optional except for positional parameters with
791: more than one digit or when <i>parameter</i> is a name and is followed by a character that could be interpreted as part of the
792: name.</p>
```

The quote is the first two source lines of one `<p>`, folded at the page's own line break and cut before
"or when …" — **quote-equal after documented shaping** (Q56): dropped bytes are line 791's tail from
` or when ` and the `<i>parameter</i>` markup, plus line 792.

**Verdict: ADMIT (recommends S272).** Tier **A** — a specification, authoritative for "what a parameter
expansion is". Registry holds no opengroup row: `grep -c 'opengroup' corpus/SOURCES.md` = **0**. The rule
grounds `t01`–`t03`: braces are optional, so both `${X}` and bare `$X` are parameter expansions, and an
unsubstituted variable in a report path is either form.
**Flip condition:** a re-open shows the sentence absent or reworded so braces are no longer optional, or
the registry gains a row on this URL.

**Observed discrepancy (minor, L1 receipt only — not a counter defect):** `receipts/sources-opened.txt`
records this quote as "19 words". Measured here:
`printf '%s\n' 'The parameter name or symbol can be enclosed in braces, which are optional except for positional parameters with more than one digit' | wc -w` → **22**.
The PIT quote's "16 words" is correct (same command → 16). The counter never counts words, so no reading
changes; the receipt's count is the only thing off.

## 2. Two further candidates, judged

### 2.1 GNU Bash manual — "Shell Parameter Expansion" — https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html

| field | value |
|---|---|
| access date | 2026-11-06 |
| HTTP | **000** (no response) |
| bytes | 0 |
| sha256 | — (empty) |

Two attempts: `curl -sS --max-time 25 …` → `curl: (28) Connection timed out after 25001 milliseconds`,
`HTTP=000 SIZE=0`; retry `curl -4 -sS --connect-timeout 8 --max-time 20 …` → `curl: (28) Connection timed
out after 8000 milliseconds`, `HTTP=000 SIZE=0`. `gnu.org` did not answer from this host in either family.

**Verdict: REJECT — could not be opened.** SOURCES contract rule 1 requires the row be written only after
opening the source in the round that writes it; an unopened page cannot carry a located quote. The
rejection is grounded in the observed timeout, not in a claim about what the page lacks (Q62).
**Flip condition:** a fetch from this host returns HTTP 200 with the braces sentence located; then it is
admissible as the shell's own statement of the rule (see 2.2 for the reachable equivalent).

### 2.2 Bash manual, maintainer's own distribution — BASH(1) man page, 2025 April 7 — https://tiswww.case.edu/php/chet/bash/bash.html

Opened as the reachable stand-in for 2.1.

| field | value |
|---|---|
| access date | 2026-11-06 (response `Date: Fri, 06 Nov 2026 03:08:25 GMT`) |
| HTTP | 200 (`HTTP/1.1 200 OK`) |
| bytes | 426217 |
| sha256 | `79394ccb66e4d572f47d8b01634d3b08a87f705a230605006e25aecd5e033475` |
| title | `<TITLE>BASH(1) Manual Page</TITLE>`, page header `BASH(1) 2025 April 7 BASH(1)` (line 6) |

Located quote (22 words, `wc -w` = 22), HTML **lines 4516–4520** under `<H4>Parameter Expansion</H4>` (line 4510):

```
4516: The parameter name
4517: or symbol to be expanded may be enclosed in braces, which
4518: are optional but serve to protect the variable to be expanded from
4519: characters immediately following it which could be
4520: interpreted as part of the name.
```

Also line 1924–1925, the same rule from the positional-parameter side: "When a positional parameter
consisting of more than a single digit is expanded, it must be enclosed in braces".

**Verdict: ADMIT (corroborating row, optional if the scribe keeps the registry short).** Tier **A** —
the shell maintainer's own published manual, authoritative for "what Bash does with `$X`". Its value is
Q23's requirement that a rule attributed to an authority carry the sweep showing whether the other
authorities state it: POSIX 2.6.2 and BASH(1) state the same optionality, so the lane can say the rule is
not one document's phrasing. Distinct document and distinct host from every registry row
(`grep -c -i 'tiswww\|case.edu' corpus/SOURCES.md` = **0**).
**Flip condition:** if the scribe records the corroboration in the round-96 lesson Gate as the Q23 sweep
witness and keeps the registry at two new rows, this row is not required; it flips to *reject-redundant*
on that choice. It flips to *reject* outright if a re-open loses the sentence.

### 2.3 Stryker Mutator — "Supported mutators" — https://stryker-mutator.io/docs/mutation-testing-elements/supported-mutators/

| field | value |
|---|---|
| access date | 2026-11-06 (response `date: Fri, 06 Nov 2026 03:08:25 GMT`, `last-modified: Thu, 05 Nov 2026 19:17:34 GMT`) |
| HTTP | 200 (`HTTP/2 200`) |
| bytes | 47923 |
| sha256 | `96a74c93f6c9d410cfd656742a3ef4938affbba3f202468bb943d79371f5a404` |
| title | `<title data-rh=true>Supported mutators | Stryker Mutator</title>` |

Located quote — the § Equality Operator table row, HTML **line 43** (section heading at line 42,
`id=equality-operator`):

```
42: <h2 class="anchor anchorTargetStickyNavbar_fMAl" id=equality-operator>Equality Operator …
43: <table>…<tr><td>LessThanEqualBoundary<td><code>a &lt;= b</code><td><code>a &lt; b</code> …
```

Quote as rendered: `LessThanEqualBoundary a <= b a < b` (6 tokens). The page is entity-escaped
(`&lt;=`), so the quote is **quote-equal after documented shaping** (Q56) — the dropped bytes are the
`<code>`/`<td>` markup and the `&lt;` entity escapes. The same table carries `LessThanBoundary`
(`a < b` → `a <= b`), `GreaterThanBoundary` and `GreaterThanEqualBoundary`, so both directions of the
boundary class are stated.

**Verdict: ADMIT (recommends a third row, or the second half of the t04 grounding).** Tier **A** —
official docs of a mutation-testing tool. Distinct document from S260, which holds
`https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/` (outcome
vocabulary); `grep -c 'supported-mutators' corpus/SOURCES.md` = **0**. It is the cleanest second authority
for `t04`: it names the mutation by operator (`LessThanEqualBoundary`) rather than only by prose, and it
states the `<=` → `<` direction explicitly.
**Flip condition:** the table drops the boundary rows, or the registry gains this URL (then cite that id).

### 2.4 mutmut — "mutmut — python mutation tester" (latest) — https://mutmut.readthedocs.io/en/latest/

| field | value |
|---|---|
| access date | 2026-11-06 (response `date: Fri, 06 Nov 2026 03:08:25 GMT`, `last-modified: Fri, 23 Oct 2026 18:18:05 GMT`) |
| HTTP | 200 (`HTTP/2 200`) |
| bytes | 51074 |
| sha256 | `07453b3fdb3b962a4cc5aff66d7614a11016c9ce0ea482654c99e17688ec9cad` |
| title | `<title>mutmut - python mutation tester &#8212; mutmut  documentation</title>` |

Located quote, HTML **line 523** under `<h2>Example mutations</h2>` (line 520):

```
522: <li><p>Integer literals are changed by adding 1. So 0 becomes 1, 5 becomes 6, etc.</p></li>
523: <li><p><cite>&lt;</cite> is changed to <cite>&lt;=</cite></p></li>
524: <li><p>break is changed to continue and vice versa</p></li>
```

**Verdict: REJECT.** Observed facts, not an absence claim: the page's only relational example is the
`<` → `<=` direction (line 523) and it defers the full operator list to source — line 527: "See
`node_mutation.py` for the full list and `test_mutation.py` for tests describing them." The `<=` → `<`
direction that `t04` needs is therefore **not stated on the page** (scope mismatch), and as a general
"boundary mutation exists" row it adds nothing PIT § Conditionals Boundary and Stryker § Equality Operator
do not state more completely and with the direction. Registry holds no mutmut row
(`grep -c -i 'mutmut' corpus/SOURCES.md` = 0).
**Flip condition:** a page revision listing the reverse direction, or a row pinned to `node_mutation.py`
at a named commit (source code is tier A for the scope "the operator list this tool applies").

## 3. Registry checks (commands and observed output)

```
grep -c 'quickstart/mutators' corpus/SOURCES.md            → 0
grep -c 'opengroup' corpus/SOURCES.md                      → 0
grep -c 'supported-mutators' corpus/SOURCES.md             → 0
grep -c -i 'mutmut' corpus/SOURCES.md                      → 0
grep -c -i 'tiswww\|case.edu' corpus/SOURCES.md            → 0
grep -n 'stryker-mutator.io' corpus/SOURCES.md             → 1 hit, S260 (mutant-states-and-metrics)
grep -oE '^\| S[0-9]{3} ' corpus/SOURCES.md | tail -3      → S268, S269, S270
```

Next free ids after S270 are S271 and S272 — consistent with the plan's assignment.

## 4. What this seat did not do

- No repo writes, no patch, no commit, no lane git/jj command.
- No judgement on the counter's predicate or on any seat's arms; the counter was read (header only) to
  name the mutant classes each candidate must ground.
- The gnu.org timeout is a host-network observation, not a claim about that page's content.

## 4a. Receipts (the fetched bytes, so a reviewer re-checks the quotes without a network)

```
.ufo/waves/round-96/w1/ScoutSourcesR96/pit-mutators.html      67033 B  a31331da…b2da2
.ufo/waves/round-96/w1/ScoutSourcesR96/posix-chap02.html     357953 B  0889867a…1acd
.ufo/waves/round-96/w1/ScoutSourcesR96/stryker-mutators.html  47923 B  96a74c93…a404
.ufo/waves/round-96/w1/ScoutSourcesR96/mutmut-mutators.html   51074 B  07453b3f…9cad
.ufo/waves/round-96/w1/ScoutSourcesR96/bash-ref-tiswww.html  426217 B  79394ccb…3475
du -sb .ufo/waves/round-96/w1/ScoutSourcesR96/ → 950200   (2026-11-06)
```

Disclosed for Q11/Q82: 950 200 B, of which 426 217 B is the BASH(1) man page (one quote, § 2.2) and
425 KB the two plan-cited pages whose byte-identity with the L1 receipts is the claim of § 1. If the wave
tree is over budget, the BASH(1) page is the one to drop: its URL is live and its hash and lines are
recorded here.

## 5. Findings for the L1

1. Both re-opened sources are **byte-identical** to the L1's receipts (sha256 and size), and both located
   quotes are present at the recorded lines (PIT 317–319 + table row 333–336; POSIX 790–791, heading 777).
2. `receipts/sources-opened.txt` states the POSIX quote is "19 words"; it is **22** (`wc -w`, command
   above). No reading depends on it; the receipt's count is the only defect.
3. `gnu.org` is unreachable from this host (two timeouts); the reachable BASH(1) page at
   `tiswww.case.edu` carries the same rule and is the better row if a second authority is wanted.
4. Stryker § Equality Operator names `LessThanEqualBoundary a <= b → a < b` — the strongest second
   authority for `t04` found; mutmut does not state that direction.
