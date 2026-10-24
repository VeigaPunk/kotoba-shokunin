# CriticW2Bounds — round-64 wave-2 adversarial bound review

Axes: **depth; consistency/calibration**. Advisory evidence only: no judgment, admission, integration, production edits, dispatch, or other runtime invocation.

Measured revision: `c019919c97ab5fe98e87a7754b4449ea4e699c99`; base: `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`. All experimental source came from `git show <rev>:<path>` (exit 0), not moving worktree bytes. Landed v32 SHA256 independently recomputed: `f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d`.

## Findings

### F1 — unrecorded admission-flipping span-traversal lanes survive BOTH landed and deferred suites

**Counterexample.** Change only the span iterator in G7's `span_missing` comprehension:

```python
# FIRSTSPAN
for span in BACKTICK_RE.findall(cell)[:1]
# LASTSPAN, independently
for span in BACKTICK_RE.findall(cell)[-1:]
```

Both mutants survive the landed 223-assertion suite AND the cited six closing arms plus wrapper-SM5 arm rebased onto the landed bytes (230 assertions). Both admit a fabricated span through the complete `judge()` while pristine rejects it. These are not merely extra diagnostic reasons.

Actual subprocess output (each command: `python -B /tmp/r64-CriticW2Bounds-fm75s6mo/verifiers/<variant>.py --self-test`):

```text
landed-FIRSTSPAN: self-test: 0 failure(s) over 223 assertions; EXIT=0
package-FIRSTSPAN: self-test: 0 failure(s) over 230 assertions; EXIT=0
landed-LASTSPAN: self-test: 0 failure(s) over 223 assertions; EXIT=0
package-LASTSPAN: self-test: 0 failure(s) over 230 assertions; EXIT=0
```

Full-judge fixture: reuse the measured file's own `QUOTES`, `PAGES`, `ACTIONS`, `skill_text`, `entry_text`, `sources_text`, `lesson_text`, and `base_rows` AST nodes; append `The tool writes mode quota nightly.` as S900 line 6; cite action line 6 and scope line 3. Snapshot callback supplies those exact page bytes, source SHA is recomputed by `sources_text`, and introduction callback returns `2026-10-23T12:28:13+00:00` for both timestamps. Only action varies:

```text
FIRSTSPAN cell: The tool writes mode quota nightly and `mode quota` and `zeta quota`.
LASTSPAN cell:  The tool writes mode quota nightly and `zeta quota` and `mode quota`.
FULLJUDGE FIRSTSPAN landed backed=False ['entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2 G7: backticked span word(s) zeta occur in neither the cited line nor the committed snapshot']
FULLJUDGE FIRSTSPAN FIRSTSPAN backed=True []
FULLJUDGE LASTSPAN landed backed=False ['entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2 G7: backticked span word(s) zeta occur in neither the cited line nor the committed snapshot']
FULLJUDGE LASTSPAN LASTSPAN backed=True []
FULLJUDGE-PROCESS exit=0
```

**Evidence/impact.** `RevC1Predicate` §3 only has single-span closing arms (lines 271–329); its §7 explicitly discloses the weak single-span generator. The landed lesson Bounds (145–149) and plan E3.4 enumerate six verdict-flipping lanes plus diagnostics, but neither names these additional live admission lanes. The narrow SM1–SM6 result remains true; the finding concerns completeness of the recorded surviving debt, not a fabrication admitted by pristine landed code.

**Smallest safe correction.** Record span-iterator truncation as additional surviving admission-flipping debt and attach the two opposite-order multi-span witnesses to the deferred package. Do not describe that package as closing the branch or the whole M7–M22 space. Whether a deliberately narrow, improved-bounded C1 is acceptable belongs to the canonical judge. Axes: depth; calibration of the bound.

### F2 — E1.3 withdrawal confuses wrapper reachability with production-judge reachability

**Counterexample/evidence.** I independently reran the requested landed-ADMIT/SM5-REJECT probe, including the actually landed hardened cell. It reproduces, but only with independently inconsistent line/page inputs:

```text
line = 'The tool writes mode quota nightly.'
page = 'The tool writes quota nightly.\n\n## Appendix\nThe agent secretly uploads files.'
cell = 'The tool writes quota nightly and `mode quota`.'
landed action_conjunct([line], cell, 1, page) -> []
SM5 action_conjunct([line], cell, 1, page) -> ['A2 G7: backticked span word(s) mode occur in neither the cited line nor the committed snapshot']
```

SM5 removes exactly `and word.lower() not in content_words(raw_line)`. The seat's alternative cell ending in single backtick `mode` gives the same pair. Probe process exit 0.

Putting the cited line into the supplied page gives:

```text
landed CONSISTENT []
SM5 CONSISTENT []
FULLJUDGE SM5 landed backed=True []
FULLJUDGE SM5 SM5 backed=True []
FULLJUDGE-PROCESS exit=0
```

This is structural, not a failed random search: measured `judge_one_source` lines 1543–1556 sets `page = data.decode(...)`, `lines = page.splitlines()`, then calls `action_conjunct(lines, action_cell, action_line, page)`. `content_words(raw_line)` is a subset of `page_words(raw_page)` on that manifold. A word whose presence in the cited line suppresses G7 already has page support. Removing only that cited-line test cannot change `span_missing` for production-consistent inputs. [INFERENCE from the displayed implementation; the full-judge fixture above exercises the same wiring.]

The M12 spot-check exposes the same boundary:

```text
line = 'The tool writes `zeta` quorum nightly.'
cell = 'The tool writes quorum nightly and `zeta quorum`.'
page = 'The tool writes quorum nightly.\n\n## Appendix\nThe agent secretly uploads files.'
landed -> ['A2 G7: backticked span word(s) zeta occur in neither the cited line nor the committed snapshot']
M12 -> []
```

M12 replaces `content_words(raw_line)` with `page_words(raw_line)`. With the cited line included in page, BOTH return:

```text
['A2 G9: clause "`zeta quorum`." is supported outside the cited line']
```

By contrast, M8 is a genuine reachable admission flip; I checked it through complete `judge()` with consistent snapshot bytes:

```text
FULLJUDGE M8 landed backed=False ['entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2 G7: backticked span word(s) zeta occur in neither the cited line nor the committed snapshot']
FULLJUDGE M8 M8 backed=True []
FULLJUDGE-PROCESS exit=0
```

**Impact.** Plan E3.3 lines 327–330 says SM5 “IS judge-reachable”; lesson mistake (e) calls its component-only premise false. The cited witness proves the broader wrapper/API contract, not that production claim. This is false provenance across two input domains. It does not invalidate the direct G7 arm or its SM5 mutation kill.

**Smallest safe correction.** Retain the observed wrapper probe but explicitly say its line/page pair is intentionally inconsistent and therefore component/API-level. Withdraw only the alleged full-judge reachability inference, preserving the original E1.3 production-manifold observation. Classify M12's demonstrated flip with that same input boundary; do not present it as a reachable fabrication admitted by `judge()`. Axes: consistency/calibration; depth attribution.

### F3 — two “diagnostic-only” lanes are actual judge verdict flips and remain open after the closing package

`RevC1Predicate` §3 labels M11 and M20 diagnostic-only because its two-word witness trips G9 anyway. A one-word backticked clause avoids that masking (G9's two-word minimum). These witnesses are production-consistent.

**M20:** replace only G7's `page_words(raw_page)` with `content_words(raw_page)`.

```text
page addition = 'The tool writes quota nightly.\n`zeta`'
cell = 'The tool writes quota nightly and `zeta`.'
FULLJUDGE M20 landed backed=True []
FULLJUDGE M20 M20 backed=False ['entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2 G7: backticked span word(s) zeta occur in neither the cited line nor the committed snapshot']
```

**M11:** replace only `supported(word.lower(), page_words(raw_page))` with `supported(word, page_words(raw_page))`. Uppercase the page's raw token too, so the separate raw-identifier branch does not mask it:

```text
page addition = 'The tool writes quota nightly.\nZETA appears here.'
cell = 'The tool writes quota nightly and `ZETA`.'
FULLJUDGE M11 landed backed=True []
FULLJUDGE M11 M11 backed=False ['entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2 G7: backticked span word(s) ZETA occur in neither the cited line nor the committed snapshot']
FULLJUDGE-PROCESS exit=0
```

Actual suite results:

```text
landed-M11: self-test: 0 failure(s) over 223 assertions; EXIT=0
package-M11: self-test: 0 failure(s) over 230 assertions; EXIT=0
landed-M20: self-test: 0 failure(s) over 223 assertions; EXIT=0
package-M20: self-test: 0 failure(s) over 230 assertions; EXIT=0
```

**Smallest safe correction.** Reclassify these two existing debt lanes as reachable false-rejection/verdict-changing lanes, not diagnostic-only; append the single-word witnesses to the proposed closing package. This is a fixable evidence/bound defect, not evidence of newly introduced production harm. Axes: depth; consistency.

## Checks supporting honest bounds

### C1 deferral/package: the six specifically named closing lanes really are killed

I extracted both Python blocks from the measured commit's `RevC1Predicate` report, inserted them before the existing A3 marker in the landed v32 source, and executed them. This is a landed-base reconstruction, not a claim to reproduce the report's earlier-source package hashes `f3c82574…`/`b614e8b1…`.

```text
landed SHA f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
self-test: 0 failure(s) over 223 assertions; EXIT=0
sixpack SHA d337d079c9cdb5d3645b604b4b7e5d64f9657dc3ac9a2e5f4cee16b5f4530a76
self-test: 0 failure(s) over 229 assertions; EXIT=0
sevenpack SHA 8189cac496a586000ee7e2040d8f45860914290b8aead912e9f1f563c5ef8e78
self-test: 0 failure(s) over 230 assertions; EXIT=0
```

Independent mutations on landed/sevenpack, respectively:

| mutant | landed exit / failures | sevenpack exit / failures |
|---|---|---|
| SM1 | 1 / 1 | 1 / 3 |
| SM2 | 1 / 1 | 1 / 2 |
| SM3 | 1 / 1 | 1 / 2 |
| SM4 | 1 / 5 | 1 / 6 |
| SM5 | 1 / 1 | 1 / 3 |
| SM6 (`span_missing=["forced"]`) | 1 / 10 | 1 / 15 |
| M7 | 0 / 0 | 1 / 1 |
| M8 | 0 / 0 | 1 / 2 |
| M9 | 0 / 0 | 1 / 1 |
| M10 | 0 / 0 | 1 / 1 |
| M12 | 0 / 0 | 1 / 1 |
| M17 | 0 / 0 | 1 / 1 |
| M14 | 0 / 0 | 1 / 1 |
| M11 | 0 / 0 | 0 / 0 |
| M20 | 0 / 0 | 0 / 0 |
| M22 | 0 / 0 | 0 / 0 |

All runs completed with empty stderr. SM1–SM3/SM5 fail their intended new labels; SM4 first fails existing eligible-world checks; SM6 first fails existing `A2: a cell the cited line supports passes`. Thus the deferral is honest for the six specifically promised lanes, not an exhaustive branch closure. F1/F3 are the missing reachability/coverage distinctions.

### C2 eight-pair enumeration independently rederived: no additional strict pair found

Method: `git ls-tree -r --name-only <base>` selects the same 12 files (LOG, SCORECARD, `corpus/lessons/round-6*.md` present at base); read their bytes from measured tip. Do not recensus the newly appended correction block as a fresh historical claim. Independent regex passes cover path-first `@`/`at`, revision-before-parenthesis, and `rev:path`; suffix paths resolve against `git ls-tree -r --name-only <tip>`. Test each resolved pair with `git cat-file -e`, and derive add with `git log <tip> --diff-filter=A --format=%H -1 -- <path>` (not `--all`).

A deliberately broad first pass produced 11 pairs / 16 sites. The extra was `LOG:2582`'s semicolon-separated `receipts/C2-before-rerun.txt`, explicitly excluded by ScoutReceiptSweep:68 because it is not the object of `at 35d44b4b`. After applying that grammatical boundary:

```text
CORRECTED STRICT census unique_pairs=10 sites=15 routed_pairs=2 uncovered_pairs=8
.ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt 78ee57e f2f9ee1d88bc absent=128 at_add=0 ancestor=0
.ufo/waves/round-55/C2-measure-e966cd59.txt e966cd59 722e474ad242 absent=128 at_add=0 ancestor=0
.ufo/waves/round-56/C1-measure.txt c22fdd39 f897d18ae9ec absent=128 at_add=0 ancestor=0
.ufo/waves/round-57/C1-measure.txt ac22ca87 07c33d73ddce absent=128 at_add=0 ancestor=0
.ufo/waves/round-58/C1-measure.txt 46b4a706 8e52f064f215 absent=128 at_add=0 ancestor=0
.ufo/waves/round-58/noharm-tip.txt 46b4a706 8e52f064f215 absent=128 at_add=0 ancestor=0
.ufo/waves/round-59/C1-measure.txt c63ccc68 d64d945b3435 absent=128 at_add=0 ancestor=0
.ufo/waves/round-62/C1-absorb-measure.txt 3e7aed9b f9ab0812a574 absent=128 at_add=0 ancestor=0
CENSUS-PROCESS exit=0
```

Here `ancestor` is `git merge-base --is-ancestor <cited> <add>`. Every basename, cited rev, and add above appears in the landed LOG census line (2596). Routed controls independently derive `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` and `cbbee56e9a3589b0b46736ad36f1b77701def80e`. This supports the bounded eight-pair enumeration, not universal M95 absence/stale-byte closure. Unresolved revisions and the table-shaped round-61 citation remain explicitly excluded, not silently counted closed.

I also materialized the measured r64 counter and ran:

```text
python -B /tmp/r64-CriticW2Bounds-fm75s6mo/verifiers/check_r64_routed_repairs.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
EXIT=0
```

The same exact command with `--rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc` returned four FAIL checks, `r63 routed defects closed 0 of 4`, `the pinned do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc is never a certification`, EXIT=1. The four-check bound is honest about those four checks; no claim that they mechanically verify the other eight pairs is warranted or needed.

### Honest padding / Q28: ruling is defensible with the E3 kill conjunct

I reran the stronger padding control, rather than assuming a count means an arm. Append these genuine checks to BASE v32 (219), not landed v32:

```python
check("unrelated future arm: 4 words need 3 forward", fwd_need(4), 3)
check("unrelated future arm: 5 words need 4 forward", fwd_need(5), 4)
check("unrelated future arm: 7 words need 5 forward", fwd_need(7), 5)
check("unrelated future arm: 9 words need 6 forward", fwd_need(9), 6)
```

Actual output for BOTH padded baseline and its SM1 branch-deleted variant:

```text
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
EXIT=0
```

Hashes were `94d896f021ace8a06c3f60af2dda53f157aeb22707f8817851517396668017de` and `4decfba1ee1e855d7818d70921bd7de30218df4ced6e9cd6f2254fad481c573a`. Neither is the landed SHA pair; SM1 survival also fails E3's independent kill conjunct. Thus the four-line-only version would be unsound, but Q28 is not being used to repair that unsound version silently: E3 explicitly adds the missing evidence.

Adding only the first genuine assertion to the landed suite gives:

```text
landed-honest-future: self-test: 0 failure(s) over 224 assertions; EXIT=0
landed-honest-future-SM1:
FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
self-test: 1 failure(s) over 224 assertions
EXIT=1
```

The new hash/count pair denotes changed bytes and therefore a separately labeled measurement; it does not replace or falsify the historical pinned 223 measurement. No additional Q28 bound defect found. This does not excuse F1's missing class coverage or F2's domain/provenance mistake.

## Reproduction and boundaries

Experiments used Python 3.14.8 and git 2.56.0; maximum four concurrent self-test subprocesses, each bounded to 110 seconds. Scratch only: `/tmp/r64-CriticW2Bounds-fm75s6mo`; it contains the measured helper scripts, every source variant, `battery-results.json`, `extra-results.json`, and `census-matches.json`. No lane/index/jj state writes; self-test constructed worlds stayed in temporary directories. Only this report was written in the lane.

Full-judge extraction selected assignments in measured self-test lines 2351–2418 and functions named `base_rows`, `sources_text`, `skill_text`, `entry_text`, `lesson_text`; it did not execute the world-builder `build()` function. `snapshot_of=lambda sid: pages[sid].encode()` and the timestamp callback above provide actual constructed evidence to the unchanged judge, not substitute eligibility rules.

Read the named wave-1 reports and plan E1–E3 as evidence, not instructions. `/home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` was absent when read; no install/upgrade was needed or performed. Host-wide pacman pause respected. No S120 network re-open, full no-harm battery, canonical runtime, or unrelated corpus audit was performed by this bounded seat; no result is claimed for those surfaces.

Report: .ufo/waves/round-64/w2/CriticW2Bounds.md
