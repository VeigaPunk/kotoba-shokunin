# ScribeLesson — round-64 wave 1, lesson draft (kotoba)

Seat: `kotoba-r64.ScribeLesson` (scribe). Scope: draft `corpus/lessons/round-64.md` and
deliver it byte-exact for the L1 to apply. Read-only outside this report; no lane file was
written, no git/jj write was run, no product code touched.

## Behavior

- Read the frozen plan (`plans/round-64.md` @ `c04fffb`) and then the committed errata E1–E3
  (same file @ `5613392`, committed while this seat worked), the r63 spot-check
  (`corpus/lessons/round-63-verifier-spotcheck.md`), the r63 lesson
  (`corpus/lessons/round-63.md`, M95 row line 52, row (t) line 96), and
  `.ufo/waves/round-63/w2/MutW2V32.md` §11 (lines 860–1009).
- Re-derived the M96 premise from committed bytes: both round-63 controls were committed at
  revisions other than the one the r63 report cites, and the cited rev does not contain
  them.
- Verified the C2 check-1 marker premise and the C2 check-4 tally model from committed
  bytes; both are recorded under Findings (the plan's E1/E2 later adopted the same two
  facts, independently).
- Verified S120's landed evidence from the snapshot itself: sha256/type, the `abstract1.1`
  paragraph id at line 283, the quote's 22-word count and its line-spanning shaping, and the
  identity mismatch in the dispatch's identifier triple.
- Verified and adopted `ScribeEntry`'s M97 candidate (`pdf-text-layer-line-as-anchor`) after
  re-running its anchors against the committed snapshot; verified the M98 material from
  `SCORECARD.md:373` and the receipt bytes at `849a546e` / `2ba4547f`.
- Drafted the lesson: frontmatter, `## Gate` (S120 + S049 filled from the landed seat
  evidence, census + receipts PENDING), `## Mistakes` M96–M98 plus the recorded non-author
  misquote, empty `## Falsify corrections` table, `## Routed-input handling` with the three
  routed inputs and the four-defect crosswalk, `## Status changes`, `## Method provenance`,
  `## Bounds`.
- Proposed (not landed) Q60 row text for `ScribeQ60`; the lesson references Q60 as the
  criterion and marks the QUALITY row PENDING (`grep -c 'Q60' corpus/QUALITY.md` → `0` at
  report time).

## Gates — what was executed here, with real output

All commands are read-only git/grep against the lane repo
(`/home/vgpnk/Projects/shokunin/kotoba-shokunin`). No lane gate was executed (Gate standard:
this seat makes no gate claim).

1. Control committing revisions:

```
$ git log --diff-filter=A --format='%H %s' -1 -- .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8 round-63: plan freeze and C1 do-nothing control (v31 5 of 6), census-before
$ git log --diff-filter=A --format='%H %s' -1 -- .ufo/waves/round-63/controls/C2-before-r62tip.txt
cbbee56e9a3589b0b46736ad36f1b77701def80e round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32), r62 routed-repairs counter, S119 + entry, LOG corrections (defects 1-4), w1 evidence
$ git cat-file -e 35d44b4b:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt ; echo "exit=$?"
fatal: path '.ufo/waves/round-63/controls/C1-do-nothing-v31.txt' exists on disk, but not in '35d44b4b'
exit=128
```

Supports M96 and C2 check 2's expected revs (`8c4cefa…`, `cbbee56…`); falsifies the r63
report's "@ `35d44b4b`" phrasing as a containing-revision citation.

2. The controls pin the base internally (so `35d44b4b` is the measured base, not the
container):

```
$ git show 8c4cefa:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt | grep -n '35d44b4b'
2:at: 35d44b4b4dcdda234b5dbff7af37e432fec55f05
$ git show cbbee56:.ufo/waves/round-63/controls/C2-before-r62tip.txt | grep -n '35d44b4b'
1:FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
```

3. C2 check-1 marker premise:

```
$ git show 078eec4:.ufo/waves/round-63/w2/MutW2SplitClauses.md | grep -c 'temporal mismatch'
0
$ grep -c 'temporal mismatch' .ufo/waves/round-63/w2/MutW2SplitClauses.md
1
$ git show 38defdc:.ufo/waves/round-63/w2/MutW2SplitClauses.md | grep -c 'temporal mismatch'
0
```

4. C2 check-4 tally source (`verifiers/check_r63_routed_repairs.py` at tip):

```
$ grep -c 'check(' verifiers/check_r63_routed_repairs.py
20
$ python3 -c "import ast,pathlib;t=ast.parse(pathlib.Path('verifiers/check_r63_routed_repairs.py').read_text());\
n=[f for f in t.body if isinstance(f,ast.FunctionDef) and f.name=='self_test'][0];\
print(len([c for c in ast.walk(n) if isinstance(c,ast.Call) and getattr(c.func,'id',None)=='check']))"
19
 (17 fixed at lines 444,450,452,454,456,458,460,476,478,485,497,510,517,523,533,543,550;
   2 in-loop at 595,601, executed once per arm × 3 arms = 6 → 17 + 6 = 23 executed)
```

5. Lane state (re-measured after the plan errata landed):

```
$ git log --oneline -3
5613392 round-64: errata E1-E3 pre-data (C2 suffix-anchoring/tally-materialization/matcher discipline; C1 kill conjunct + pin pair, hardened arm-4 fixture, M7-M22 debt recorded)
c04fffb round-64: freeze plan — C1 G7 span_missing pinning arms (219->223), C2 r63 routed defects counter (4 of 4); two v1 waves 32+32
078eec4 round-63 verifier spot-check (integrator, hyaku): non-author admit/reject
$ git status --porcelain
 M .ufo/waves/round-63/w2/MutW2SplitClauses.md
 M verifiers/check_scoped_rules_v32.py
?? .ufo/waves/round-64/snapshots/
?? .ufo/waves/round-64/w1-dispatch.err
?? .ufo/waves/round-64/w1-dispatch.json
?? .ufo/waves/round-64/w1-spec.json
?? .ufo/waves/round-64/w1/
```

   (`verifiers/check_scoped_rules_v32.py` is `ExecSpanArms`' uncommitted C1 landing; this seat
   read it only as a state fact, never as a measured claim.)

6. Absence checks (dependencies, not defects):

```
$ ls corpus/lessons/round-64.md verifiers/check_r64_routed_repairs.py
ls: cannot access 'corpus/lessons/round-64.md': No such file or directory
ls: cannot access 'verifiers/check_r64_routed_repairs.py': No such file or directory
$ grep -c '^| S120' corpus/SOURCES.md      # 0
$ grep -c 'Q60' corpus/QUALITY.md          # 0
$ grep -n '^## .*Round 64' LOG.md          # no output (only the r63 post-close deferred-item note at LOG.md:2588)
```

7. S120 snapshot identity, anchors and quote shaping (independent of the scout's report):

```
$ file .ufo/waves/round-64/snapshots/S120.page
HTML document, Unicode text, UTF-8 text, with very long lines (1234)
$ sha256sum .ufo/waves/round-64/snapshots/S120.page
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8
$ grep -n 'id="S1.p1.1"\|id="S3.SS2.SSS2.p1.1"' …/S120.page | cut -c1-60
319:<p id="S1.p1.1" class="ltx_p">Software testing is the predominant…
780:<p id="S3.SS2.SSS2.p1.1" class="ltx_p">Equivalent mutants, which are…
$ sed -n '40,52p' …/S120.page | head -3
  initializeReadingPreferences();
</script>
<link rel="apple-touch-icon" sizes="180x180"
$ printf '%s\n' "<quote>" | wc -w
22
$ sed -n '283,284p' …/S120.page | tr '\n' ' ' | grep -c "<quote>"
1
$ sed -n '283,284p' …/S120.page | grep -c "<quote>"     # single-line form
0        # exit 1 — the quote spans a line break (283→284)
```

8. M98 premise (receipt content at the cited rev):

```
$ git show 849a546e:.ufo/waves/round-63/receipts/C1-g9-measure.txt | grep -c '219 assertions'
0
$ git show 849a546e:.ufo/waves/round-63/receipts/C1-g9-measure.txt | grep -c '205 assertions'
1
$ git show 2ba4547f:.ufo/waves/round-63/receipts/C1-g9-measure.txt | grep -c '219 assertions'
1
$ sed -n '373p' SCORECARD.md | grep -o '.\{0,120\}849a546.\{0,90\}'
f 4` / `survivors closed 6 of 6` / … exit 0 @ `849a546effbc081e44f2dcd5c49d1055074b7ebb` (committed v32 sha256 `12d093a1…`, 219 assertions;
```

9. Non-author size-quote erratum:

```
$ git diff --numstat 38defdc -- .ufo/waves/round-63/w2/MutW2SplitClauses.md
82	29	.ufo/waves/round-63/w2/MutW2SplitClauses.md
```

10. Entry-revision-3 span anchors (quotes taken from `ScribeEntry.md` §1 and §1.3, snapshot
    lines tag-stripped and single-space joined before matching):

```
$ python3 - <<'PY'
import re, pathlib
L = pathlib.Path('.ufo/waves/round-64/snapshots/S120.page').read_text().splitlines()
w = lambda a,b: re.sub(r'\s+',' ', re.sub(r'<[^>]+>','', ' '.join(L[a-1:b]))).strip()
q1 = "However, code coverage alone might be misleading, in particular when program statements are covered but the expected program outcome is not asserted upon"
q2 = "Equivalent mutants, which are semantically equivalent to the mutated program, are a plague in mutation testing and cannot generally be detected automatically"
for n,q,a,b in (("q1",q1,324,326),("q2",q2,780,782)):
    print(n, "window", q in w(a,b), "| drop-first", q in w(a+1,b),
          "| drop-last", q in w(a,b-1), "| any single line",
          [i for i in range(a,b+1) if q in w(i,i)])
PY
q1 window True | drop-first False | drop-last False | any single line []
q2 window True | drop-first False | drop-last False | any single line []
```

11. The in-flight C1 bytes do not equal either published prototype digest:

```
$ sha256sum verifiers/check_scoped_rules_v32.py ; stat -c '%s bytes' verifiers/check_scoped_rules_v32.py
f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d  verifiers/check_scoped_rules_v32.py
147512 bytes
$ grep -n 'The tool writes quota nightly and `mode quota`.' verifiers/check_scoped_rules_v32.py
2159:                  "The tool writes quota nightly and `mode quota`.",
```

```
$ grep -n '7791504715f3\|147220' .ufo/waves/round-64/w1/MutSpanArms.md | cut -c1-120
67:v32+arms (223) sha256 7791504715f308e2cedf4f9cc746ae08d513a3dc01861b4afe1fb2a84911cda2 147220 bytes
```

   (The file is `ExecSpanArms`' uncommitted landing and may still move; recorded as a state
   observation, never as a pin.)

## Full lesson draft — `corpus/lessons/round-64.md`

Apply as the file's exact content. Every PENDING marker names its owner; no measurement is
invented and no gate line is stated that was not run.

````markdown
---
author: kotoba L1 round-64 seat draft
date: 2026-10-24
round: 64
lane: kotoba
---

# Round 64 — lesson (kotoba, hyaku run 5)

Wave-1 draft by `ScribeLesson`. Everything marked **PENDING** is filled by the named seat
or the L1 before the report commit; the plan's expected results are labelled as
declarations, never as results, and no command output is stated that this lane did not
observe.

## Gate

**S120 (new row, opened 2026-10-24).** The dispatch's candidate identifiers were falsified and
the title-matched primary opened instead. Opened source: Petrović, Ivanković, Fraser & Just,
*Practical Mutation Testing at Scale* (subtitle *A view from Google*), arXiv:2102.11378v2
[cs.SE] 26 Feb 2021 — the mutation-testing primary for the C1 method (a load-bearing branch
is pinned by kill-witnesses, not by line coverage) and the source the round's C1 knowledge
entry cites. Journal version *IEEE TSE* (DOI `10.1109/TSE.2021.3107634`) is Crossref
metadata only and was **not opened**.

- URL: `https://arxiv.org/html/2102.11378` — HTTP 200, `text/html`; opened 2026-10-24
  (`ScoutS120.md` § Opened source).
- Snapshot: `.ufo/waves/round-64/snapshots/S120.page`, 571,600 B, sha256
  `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8` (measured by this seat:
  `file` → HTML, `sha256sum` as shown; the export mirror `export.arxiv.org/html/2102.11378v2`
  returned a sha256-identical body per `ScoutS120.md`).
- Quote (22 words, `wc -w` on the quote's own line per Q54: `printf '%s\n' '<quote>' | wc -w`
  → `22`): “Mutation analysis assesses a test suite’s adequacy by measuring its ability to
  detect small artificial faults, systematically seeded into the tested program.”
  - Anchor: abstract paragraph `abstract1.1`, which opens at snapshot line 283.
  - Shaping (Q53/Q56, measured): the sentence **spans snapshot lines 283–284** — the HTML
    breaks it between `detect ` and `faults`. It is `quote-equal after documented shaping`
    (one space joins the lines), **not** a literal single-line substring and so never
    `byte-exact`: `sed -n '283,284p' … | tr '\n' ' ' | grep -c '<quote>'` → `1`; the same
    `grep` without the join → `0`, exit 1. A re-checker must run the two-line form.
- Tier: **A**, scoped by `ScoutS120` to this paper's own statement that mutation analysis
  measures adequacy by detecting seeded faults; the Google deployment is the setting, not a
  license to read a kill as line coverage or as a real fault.
- Dispatch provenance (recorded, not a lane Mistakes row — the lane plan carries neither
  token, `grep -c '2103.02722\|ICSE43902' plans/round-64.md` → `0`): the wave spec carried
  arXiv:2103.02722 and DOI `10.1109/ICSE43902.2021.00068`; the first opens a different title
  (a Markov-jump-process paper) and the second resolved to IEEE document 9401981 then HTTP
  202 (never opened) — `ScoutS120.md` § Plan identifiers. The opened artifact, not the
  identifier triple, is what the row cites.

**S049 live context — re-probe append (measured by `ScoutS049`, 2026-10-24T03:35:37Z).**
Both request profiles were re-probed and the dated result is committed in
`.ufo/waves/round-64/w1/ScoutS049.md`; the row and the round-63 errata note stand
unwritten-over (append-only; Q34 owns SOURCES appends).

- Observed (the seat's measurement, not this seat's — no `curl` was run here): `Accept:
  text/markdown` → HTTP 404, 389 B, sha256 `4f98eb06…`; default `Accept: */*` → HTTP 200,
  17,252 B, sha256 `dae9d3ec…` (reproduces the 2026-10-23 re-probe, **not** the 2026-10-22
  17,403 B / `884c67ca…` receipt); control `…/docs/rules` (no `.md`) → HTTP 200, 540,892 B,
  `text/html`, sha256 `35ff98b0…`.
- What it tests: the errata's claim (a request-profile result, not a dead URL) — reproduced;
  the rejection of a second row from the `.md` spelling stands with its corrected reason.
- Remaining action: the dated search-log line in `corpus/SOURCES.md` — PENDING
  (`ScribeSOURCESRow`); `ScoutS049.md` supplies the append text.

**Round-start census — PENDING (`ExecGateRow`).**
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` — exit
code and warning counts pasted from the committed `.ufo/waves/round-64/census-before.txt`;
no count is predicted here.

**Claim receipts — counted predicates as frozen in the plan and its errata (E1–E3, committed
at `5613392`); measured values PENDING.**

| claim | counted predicate | control (declared) | measured tip (PENDING) |
|---|---|---|---|
| C1 (depth) | `python3 -B verifiers/check_scoped_rules_v32.py --self-test` prints the four frozen lines and exits 0, **and** the receipt pins the `(sha256, 223)` pair recomputed from the landed bytes, **and** the kill conjunct holds: each of SM1–SM6 exits 1 on the landed bytes with its own discriminating FAIL label (SM4/SM6 go red on pre-existing `eligible world` arms and are not new-arm pins) — E3.1 | v32 at base `078eec4`: declared `219 assertions` (the four arms absent) | PENDING (`ExecSpanArms`, `ExecSpanBefore`; receipt under `.ufo/waves/round-64/`). The pin is the **landed** bytes' own sha256 — never a prototype digest: `ae84673e…` (`MutW2V32:934`) and `7791504715f3…`/147,220 B (`MutSpanArms` § measured, `:67`) are measurement sources for the 223-assertion suite, and E3.2's hardened arm-4 fixture means the landed bytes differ from both; `12d093a1…`/219 (`MutW2V32:864`) is the superseded pair |
| C2 (consistency) | `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>` prints `r63 routed defects closed 4 of 4`, exit 0, with the hardened definitions: checks 2–3 scan only lines after the first `## 2026-10-24 — Round 64` LOG header (E1.1), check 1 carries a discrimination floor (marker line an addition vs `38defdc`, ≥60 added lines, E2.1), check 4 runs the materialized self-test and cross-checks its `over N assertions` against the static 17 + 2×3 = 23 (E1.2/E2.4), matchers are ordered and content-shaped (E3.5) | the same counter at `BASE_REV` = `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`: `0 of 4`, exit nonzero — and the counter **refuses** unless the pinned base scores exactly `0 of 4` (E2.5) | PENDING (`ExecR64Counter`) |

Stale-`219` repairs carried with the arms (E3, freshness — no source row is rewritten):
`corpus/README.md:112` and `corpus/knowledge/compound-clause-citation-round63.md:120`.

Rejections (with reason): the dispatch's two identifiers — arXiv:2103.02722 (opens a different
title) and DOI `10.1109/ICSE43902.2021.00068` (IEEE document 9401981, HTTP 202, never
opened) — recorded in `ScoutS120.md` § Plan identifiers. `ScoutS120Alt`'s three fallbacks (a
Google Engineering blog, a university mutation-testing chapter, PIT docs) were **not**
screened because the title-matched primary opened; they stay leads, not rejections. A
rejection is evidence of taste and stays a row or a recorded reason; a screen that never
opened a candidate does not count as one. PENDING (`RevSourcesGate`) for the gate review's
own exclusion list.

## Mistakes

- **M96 — class: reference-drift (M95-class recurrence, here in a citation's shape).**
  Evidence: `.ufo/reports/round-63/kotoba.md:31-32` (fleet repo) cites both round-63
  controls "@ `35d44b4b`" — line 31 “v31 control, `controls/C1-do-nothing-v31.txt` @
  `35d44b4b`”, line 32 “`controls/C2-before-r62tip.txt` … exit 1 @ `35d44b4b`”. The files
  were committed elsewhere: `git log --diff-filter=A --format=%H -1 --
  .ufo/waves/round-63/controls/C1-do-nothing-v31.txt` → `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8`;
  the same command for `C2-before-r62tip.txt` →
  `cbbee56e9a3589b0b46736ad36f1b77701def80e`; and
  `git cat-file -e 35d44b4b:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` prints
  `fatal: path '.ufo/waves/round-63/controls/C1-do-nothing-v31.txt' exists on disk, but not
  in '35d44b4b'`, exit 128. `35d44b4b` is the *measured base*, which both controls pin
  internally (`at: 35d44b4b…` in C1; `FAIL late-write-tracked not a tracked blob at
  35d44b4b…` in C2) — it is not the revision that contains them. Captured-by: none at r63
  — M95 mined the class from r62 artifacts (a receipt sha existing in no store, a false
  ancestry clause, a false same-URL sentence) and never stated the citation-shape rule that
  a cited revision must *contain* the cited blob; the nearest rows name values, not
  containers (Q48 printed-vs-computed, Q58 recomputation-in-closure). Now Q60. Fix
  (appended; the r63 report is the closure's record and is not rewritten): C2's checks 1–4
  land in `verifiers/check_r64_routed_repairs.py` under the r63 E2 discipline (base arm
  pinned in code, the counter refuses to certify while the control is green); check 2
  `control-revs-named` recomputes both committing revs from `<rev>` with `git log
  --diff-filter=A … -1` and requires a round-64 LOG correction line to name both revs plus
  the pinned base `35d44b4b`; checks 1, 3 and 4 close the spot-check's remaining routed
  defects. Errata bind the implementation: E1.1 anchors checks 2–3 to the round-64 LOG
  header (the r63 corrections line co-locates all three tokens, so a whole-LOG scan
  false-greens at base), E2.5 makes the counter refuse unless the pinned base scores exactly
  `0 of 4`, and E3.5 requires ordered content-shaped matchers rather than token scans.
  Found by `corpus/lessons/round-63-verifier-spotcheck.md` § Routed defects item
  2; the crosswalk is re-checked at r64 by `RevSpotcheckCrosswalk`.

- **M97 — class: anchor-drift (`pdf-text-layer-line-as-anchor`: an anchor that resolves
  against the wrong rendering).** Evidence: the first draft of
  `corpus/knowledge/g7-span-pinning-round64.md` cited `S120.page:40-52` and `:524-527` as
  the quote anchors. The committed snapshot
  `.ufo/waves/round-64/snapshots/S120.page` (571,600 B, HTML, sha256 `15963c3e67b5…`) holds
  those ranges in page chrome — `sed -n '40,52p'` prints icon and stylesheet `<link>` lines —
  while the quoted spans sit inside the paragraphs that open at 319
  (`<p id="S1.p1.1"`) and 780 (`<p id="S3.SS2.SSS2.p1.1"`):
  `grep -n 'id="S1.p1.1"\|id="S3.SS2.SSS2.p1.1"' S120.page` → `319`, `780`. The quote windows
  are **spans**, not lines: quote 1 occupies 324–326 and quote 2 780–782 — after tag-strip and
  single-space line-join, each quote is contained in its window and in **no single line** of
  it, and dropping either end of the window loses it (measured on the committed bytes). The
  indices were a text-layer rendering's, not the committed snapshot's. Captured-by: the
  non-author source gate re-running the anchors (`RevSourcesGate` §11.1; `ScribeEntry`
  F10/F10b) — no lane check reads anchors, so both wrong anchors passed every script; the
  entry (revision 5 at report time) anchors by paragraph id **plus line span** and gives each
  digest one job (committed / worktree-uncommitted / prototype-measurement), keeping both
  quotes labelled
  `quote-equal after documented shaping` (line-join only; quote 1 also drops the paper's own
  `[2], [3]` markers), never `byte-exact` (Q56). Fix (appended; entry and lesson now agree):
  anchor a quote by the **committed snapshot's** paragraph id plus its snapshot line **span**,
  so a re-checker runs one `sed -n '<a>,<b>p'` — a lone line number cannot anchor a
  line-spanning quote, which is exactly how the first draft's indices drifted; never by a
  text-layer index of a different rendering. Not a typo: the wrong anchor still matched real
  lines and still "resolved" — the M95/M96 failure shape, a citation that looks checkable and
  checks the wrong bytes. M96 asks whether a cited revision *contains* the file; M97 asks
  whether the cited span *contains* the quote.

- **M98 — class: reference-drift (M95 class, receipt content at a named rev).** Evidence:
  `SCORECARD.md:373` (round-63 annotation) states `exit 0 @ 849a546effbc081e44f2dcd5c49d1055074b7ebb`
  with "committed v32 sha256 `12d093a1…`, 219 assertions" and cites
  `.ufo/waves/round-63/receipts/C1-g9-measure.txt`. At that rev the cited receipt holds the
  stale wave-1 bytes: `git show 849a546e:.ufo/waves/round-63/receipts/C1-g9-measure.txt |
  grep -c '219 assertions'` → `0`, the same command for `205 assertions` → `1`; the
  219-assertion refresh is committed at `2ba4547f` (`grep -c '219 assertions'` → `1`). The
  v32 bytes are identical at both revs, so the *verdict* is true and only the
  receipt-content-to-rev pairing is wrong — which is what makes it hard to see. Captured-by:
  `ScribeQ60` F2 at r64; nothing at r63 — Q58's recomputation rule binds closure of routed
  spot-check defects, not a scorecard annotation's receipt pointer. Fix (pre-data, E1
  disposition): the round-64 SCORECARD annotation carries an erratum line naming
  `2ba4547f` and the stale-content fact; the repair is verified by `ScoutReceiptSweep` and
  wave-2 re-derivation, and is deliberately **not** one of C2's four counted checks (C2's
  bound names exactly the spot-check's four routed defects).

**Recorded, not repaired (non-author file).** The r63 spot-check's defect 1 quotes the
working-tree edit as "41 insertions/13 deletions"; the measured diff is
`git diff --numstat 38defdc -- .ufo/waves/round-63/w2/MutW2SplitClauses.md` → `82  29`. The
spot-check file is non-author and is never edited (Q52 discipline applied to quotes); the
misquote is recorded here and in the round-64 report, and the routing it serves — the edit
was uncommitted at closure and lands under round 64 — stands unchanged.

Wave 2 appends M99+ only for attacks it actually lands; nothing is reserved here.

## Falsify corrections

Filled after wave 2 (dispatched only if wave 1 yields ≥32 distinct attack items); empty at
wave-1 draft time. Every row names the distinct attack, the seat(s) that made it, and the
disposition as landed against the hardened instruments.

| # | distinct attack | source seat(s) | disposition as landed |
|---|---|---|---|

## Routed-input handling

Three routed inputs arrive from the round-63 closure (`plans/round-64.md` § Routed-input
handling); none may be dropped, and each names where it lands.

| routed input | source | lands in | status |
|---|---|---|---|
| 1. G7 `span_missing` pinning arms (four measured, 223 assertions, all six SM mutants red) | `corpus/lessons/round-63.md` row (t); `.ufo/waves/round-63/w2/MutW2V32.md` §11 (at `75370a5`); LOG.md:2588 post-close note | C1 — four self-test arms appended to `verifiers/check_scoped_rules_v32.py`, byte-exact from §11 (arm 4 calls `g7_conjunct` directly — the SM5 kill), plus the refreshed receipt at the measured tip | PENDING (`ExecSpanArms`, `ExecSpanBefore`) |
| 2. M95 citation-class defect (controls cited "@ `35d44b4b`", committed at `8c4cefa8` / `cbbee56e`) | `corpus/lessons/round-63-verifier-spotcheck.md` § Routed defects item 2 | C2 checks 1–2 in `verifiers/check_r64_routed_repairs.py`; M96 above; `corpus/QUALITY.md` Q60; the `LOG.md` round-64 corrections line naming both committing revs + the pinned base | PENDING (`ExecR64Counter`, `ScribeQ60`, `ScribeLOGCorr`) |
| 3. S049 request-profile errata (`.md` route 404 under `Accept: text/markdown`, 200 by default) | `corpus/SOURCES.md` § Search log (round-63 note); r63 lesson § Gate | live context only — the Gate re-probe above; the SOURCES search log gains a dated 2026-10-24 line; no row field is rewritten | PENDING (`ScoutS049`, `ScribeSOURCESRow`) |

The spot-check's four routed defects map onto C2's four checks, and the two remaining items
are not C2 material:

1. uncommitted seat edit `MutW2SplitClauses.md` → check 1 (`seat-edit-committed`): the
   marker `temporal mismatch` is present in the inherited working-tree edit and absent from
   the committed copy (measured 0 at both `078eec4` and `38defdc`; the worktree carries 1);
2. citation imprecision → check 2 (routed input 2 above);
3. lowest-axis parenthetical → check 3 (`lowest-axis-corrected`): SCORECARD owns depth at 9
   below consistency at 10, so depth is the lowest owned axis;
4. stale seat number "21 assertions" vs the committed counter's 23 → check 4
   (`assertion-count-named`), whose expected 23 is the *executed* tally (17 fixed calls +
   2 in-loop call sites × 3 arms), not a raw text count.

Item 5 (the deferred arms) is routed input 1; item 6 (SHONEN `[~]` → `[x]` promotion) is
operator-owned and out of lane scope.

## Status changes (contract rule 2, old → new)

- S120 — new row → **PENDING** (`opened` → `mined` at the row's landing); `used-by` names
  the round-64 knowledge entry (`ScribeEntry`; path PENDING) and this lesson.
- S049 — `mined` unchanged; `recheck 90d` not due (opened 2026-10-22); the 2026-10-24
  re-probe appends to the search log, and no field is rewritten.

## Method provenance

The four C1 arms are not re-derived here: they are byte-exact from `MutW2V32` §11, measured
there on `/tmp/mutw2v32/landed_plus_spanfix7.py` (sha256 `ae84673e…`, 223 assertions), with
all six `span_missing` mutants red and the nine splitter mutants still red on top. The C2
counter follows `check_r63_routed_repairs.py`'s E2 hardening — computed-from-`<rev>`
checks, the base arm pinned in code, label-only / fingerprint / worktree process arms — and
Q58's closure rule (a routed defect closes only on recomputation from the measured
revision's bytes). Q60 carries the citation-shape rule M96 names. S120 supplies the
external method; the source is opened and snapshotted (Gate above), and only its registry row
is PENDING (`ScribeSOURCESRow`).

## Bounds

- C1 pins the `span_missing` branch's four measured lanes; the W8 escape class and A2's F6
  compound-purpose bound remain surviving debt (SCORECARD's round-64 Next line).
- C2 binds the four routed defects of one spot-check; a new self-assessment mismatch class
  is outside it, and the tie to its own tally (check 4) is a *model* of executed
  assertions, so a future edit to the loop shape moves the expected number and must
  re-freeze it.
- S120 is one primary source: admission is not a survey, and the Gate's rejection record
  states which candidates were screened and why.
- C1's arm 4 pins SM5 at the component level (`g7_conjunct` direct call, per `MutW2V32`
  §11) and `RevC1Predicate` Q4 showed SM5 **is** judge-reachable, which withdraws E1 item 3;
  the wrapper-level SM5 witness belongs to the deferred closing package, not this round
  (E3.3).
- The six M7–M22 verdict-flipping lanes and the diagnostic lanes are newly found surviving
  debt, not claim scope: recorded as round-65 candidates with the seat's measured closing
  package (6 arms → 229 assertions, sha `f3c82574…`; plus the wrapper SM5 arm → 230, sha
  `b614e8b1…`) in the SCORECARD Next line (E3.4).
- C2's remedy choice is fixed: commit the seat edit (it is a verified self-correction) and
  append the drift note rather than rewrite a dated seat cell; the alternative remedies
  (revert; amend) stay recorded (E3.6). `check_scoped_rules_v32.py` still has no
  `floors-registry.json` row — carried gate debt, round-65 candidate (E3).
- The pin must be a `(sha256, 223)` **pair**, and the count is not decoration: `MutSpanArms`
  measured (a) arm 4's `g7_conjunct` swapped for `action_conjunct` survives at `0 failures /
  223` (A2 — the wrapper-masking mechanism, and the direct call is a discipline no assertion
  pins) and (b) deleting arms 2–3 leaves `0 failure(s) over 221` (A5 — killed only by the
  count literal). A receipt that pins `0 failure(s)` without the sha256-and-count pair cannot
  see either edit.
````

## Proposed Q60 row (for `ScribeQ60`; NOT landed by this seat)

Draft text supplied so the lesson's "now Q60" reference is checkable. `corpus/QUALITY.md`
columns are `id | criterion | applies to | grounded in | supersedes`.

```
| Q60 | A citation of a revision for a file states a revision that contains the cited blob: the committing revision computed from the repository (`git log --diff-filter=A --format=%H -1 -- <path>`) or a revision at which `git cat-file -e <rev>:<path>` succeeds; a revision the file merely measures, quotes inside its own bytes, or predates is not the citing revision and is named separately as the pinned base. | report, lesson and receipt citations of committed artifacts | M96 `reference-drift` in citation shape (`corpus/lessons/round-64.md` § Mistakes): the round-63 report cites two controls "@ `35d44b4b`" while they were committed at `8c4cefa8` / `cbbee56e` and `35d44b4b` does not contain them (exit 128). | — |
```

Fix-shown-able-to-fail check for the row (the Q59 discipline, offered to `ScribeQ60`):
`git cat-file -e 35d44b4b:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` exits 128
(red) while `git cat-file -e 8c4cefa:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt`
exits 0 (green) — the rule discriminates on the two real citations.

## Findings (what each supports / falsifies)

1. **Check 4's expected 23 is an executed tally, not a text count.** Supports C2 check 4 as
   *worded* ("the counter computes the r63 C2 counter's self-test tally"), falsifies a
   literal reading of "counting `check(` invocations": `grep -c 'check('` = 20 (includes the
   `def check(` line) and AST call sites = 19, while 23 = 17 fixed + 2 in-loop × 3 arms.
   An implementation using a raw count prints a wrong tally at every revision and C2 cannot
   reach 4 of 4. Reported to `ExecR64Counter` and `RevC2Checks`; the plan's errata E1.2 and
   E2.4 (committed `5613392`) independently adopt the runtime-tally + static-cross-check fix,
   so the finding is absorbed and the lesson's C2 row names the adopted form.
2. **Check 2 has a base-arm leak through pre-existing LOG tokens.** `LOG.md:2576` (the r63
   "corrections to this block" line) already names *both* `8c4cefa8` and `cbbee56e`, and
   `cbbee56` appears on three LOG lines. A whole-LOG scan therefore passes at `BASE_REV`
   `078eec4` and the frozen control prints 1 of 4 instead of the declared 0 of 4. The plan's
   hardening sentence ("whole-LOG substring matches do not count") is the fix: the scan must
   be scoped to a round-64 correction line appended after the r63 block. This does not
   falsify the plan; it falsifies any suffix-unscoped implementation. Reported to both seats;
   absorbed by E1.1 (header-anchored suffix) and E2.5 (refuse unless the base scores exactly
   `0 of 4`) at `5613392`.
3. **Check 1's premise holds.** `temporal mismatch` = 0 at `078eec4` and `38defdc`, 1 in the
   inherited working-tree edit — so check 1 is discriminating at base and closes defect 1
   only if the edit is committed.
4. **Check 2's expected committing revs hold.** `8c4cefa8…` and `cbbee56e…` re-derived;
   `35d44b4b` provably lacks the C1 control (exit 128). Supports M96 and the plan's expected
   values.
5. **Dependency state at report time (recorded, not blockers).** Landed while this seat
   worked: the S120 snapshot (`.ufo/waves/round-64/snapshots/S120.page`), the scout reports
   (`ScoutS120.md`, `ScoutS049.md`), and the plan errata E1–E3 at `5613392`. Still absent:
   `corpus/lessons/round-64.md` (this draft is its content),
   `verifiers/check_r64_routed_repairs.py`, `corpus/QUALITY.md` Q60, the `corpus/SOURCES.md`
   S120 row, and the `LOG.md` round-64 corrections block. The lesson marks every
   still-unmeasured gate/receipt value PENDING rather than borrowing an expected value as a
   measured one.
6. **Base vs tip.** Dispatch names base tip `078eec4`; the lane tip moved to `c04fffb` (plan
   freeze) and then `5613392` (errata E1–E3) during this seat's run. C2's control revision
   stays `078eec4a1f6a41c64ff8806f58b46a67cd413bfc` per the plan; runs against the later
   revisions include the plan/errata files, so the pinned base remains the declared one.
   [INFERENCE] None of the three revisions carries a `## 2026-10-24 — Round 64` LOG header,
   so E1.1's header-anchored checks 2–3 fail at all three and the `0 of 4` control holds.
7. **S120's quote is line-spanning, so a single-line substring claim would be false.** The
   22-word gate quote sits at snapshot lines 283–284 (the HTML breaks it between `detect `
   and `faults`); `sed -n '283,284p' | tr '\n' ' ' | grep -c '<quote>'` → `1`, the single-line
   `grep` → `0`, exit 1. The Gate records it as `quote-equal after documented shaping`
   (Q53/Q56) with the two-line re-check command, never as `byte-exact`. Supports the Gate
   row; falsifies a "literal substring of the snapshot" phrasing.
8. **The dispatch's S120 identifier triple did not identify the paper.** The plan file
   carries neither token (`grep -c '2103.02722\|ICSE43902' plans/round-64.md` → `0`); the
   wave spec carries both. Per `ScoutS120.md`: arXiv:2103.02722 opens a different title, and
   DOI `10.1109/ICSE43902.2021.00068` resolved to IEEE document 9401981 then HTTP 202 and was
   never opened. The opened artifact is arXiv:2102.11378 (title-matched, HTML, sha256
   `15963c3e…`). Recorded in the Gate as provenance, not as a lane `Mistakes` row (the lane
   plan did not author the identifiers).
9. **`ScribeEntry`'s M97 candidate verified and adopted.** `grep -n 'id="S1.p1.1"\|id="S3.SS2.SSS2.p1.1"'`
   on the snapshot prints 319 and 780; `sed -n '40,52p'` prints `initializeReadingPreferences();`,
   `</script>` and `<link rel="apple-touch-icon" …>` (page chrome, not quote text); lines 324
   and 781 carry the quoted spans. The row lands with the class name `pdf-text-layer-line-as-anchor`
   and the fix stated as snapshot paragraph id + snapshot line span (sharpened by finding 11).
10. **M98 and the non-author misquote verified.** SCORECARD:373's `849a546e` citation points
   at a receipt whose bytes there say `205 assertions` (the 219 refresh is `2ba4547f`);
   and the r63 spot-check's "41+/13-" measures `82  29` under `git diff --numstat 38defdc`.
   Both facts are recorded in the lesson (M98 and the "Recorded, not repaired" paragraph).
11. **`ScribeEntry`'s span anchors verified, and they sharpen M97's fix.** With the quotes
   taken from the entry's own text, tag-stripping and single-space joining the snapshot
   windows gives: quote 1 ∈ 324–326 ✓, quote 2 ∈ 780–782 ✓; for each, dropping either end of
   the window loses the quote, and **no single line** in either window contains its quote. So
   the fix is a line *span*, not a line number — a lone line anchor cannot hold a
   line-spanning quote, which is the mechanism by which the first draft's indices drifted.
   M97's evidence and fix now say span, and record the entry's labels (`quote-equal after
   documented shaping`, line-join only; quote 1 also drops `[2], [3]`), never `byte-exact`.
   The entry's revision 5 keeps these spans unchanged.
12. **No prototype digest may become the pin.** `ae84673e…` (`MutW2V32:934`) and
    `7791504715f3…`/147,220 B (`MutSpanArms:67`) both describe 223-assertion *prototypes*;
    E3.2 lands a hardened arm-4 fixture, so the landed bytes differ from both. The Gate's C1
    row now names the pin as the landed bytes' own sha256 and lists both prototypes as
    measurement sources only.
13. **The entry's prototype pin — raised and fixed in its revision 5.** My measurement:
    `sha256sum verifiers/check_scoped_rules_v32.py` (working tree, uncommitted) →
    `f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d`, 147,512 B — not
    `7791504715f3…`/147,220 B, so the earlier `verified-at:` named bytes that would not land.
    The worktree carries E3.2's hardened arm-4 cell (`"The tool writes quota nightly and
    \`mode quota\`."` at 2159, page lacking `mode` at 2161); +292 B is the consistent
    **inference**, the digests are the measurement. Disposition (peer's revision 5, reported
    back and not re-run here — no gate was executed by this seat): one job per digest —
    `12d093a1…` the committed 219 base, `f8f69cad…` the worktree 223 bytes labelled
    *uncommitted*, `ae84673e…` §11's prototype, `7791504715f3…` `MutSpanArms`' measurement
    source for A2/A5 — with the committed digest left to the C1 receipt. That is the shape
    finding 12 asks for. The worktree may still move before `ExecSpanArms` commits, so no sha
    is asserted here as the pin.

## Touched surfaces

- Wrote exactly one file: `.ufo/waves/round-64/w1/ScribeLesson.md` (this report).
- Read-only elsewhere. No edit to `corpus/`, `verifiers/`, `LOG.md`, `SCORECARD.md`,
  `SHONEN.md`, `SKILL.md`, no git/jj write, no product code.

## Out of scope (left to named owners)

- Landing `corpus/lessons/round-64.md` (L1 applies the block above; the S120 and S049 values
  in it are already filled from the landed seat evidence — only the census and the
  claim-receipt measurements remain PENDING).
- `corpus/QUALITY.md` Q60 row (`ScribeQ60`); `LOG.md` round-64 corrections (`ScribeLOGCorr`);
  the `corpus/SOURCES.md` S120 row and S049 search-log append (`ScribeSOURCESRow`).
- C1 arms and receipts (`ExecSpanArms`, `ExecSpanBefore`); C2 counter (`ExecR64Counter`);
  SCORECARD annotations (`ScribeSCORECARD`, including the M98 erratum line);
  knowledge entry (`ScribeEntry`).
- SHONEN `[~]` → `[x]` promotion is operator-owned.

## Tooling

No installs, upgrades, or pacman transactions (host-wide pause respected). Tools used:
`git` (read-only), `grep`, `sed`, `awk`, `printf`, `python3` (read-only AST/substring use),
`ls`, `sha256sum`, `file`, `wc`.

## Artifact paths

- This report: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/w1/ScribeLesson.md`
- Lesson content for landing: block above (`corpus/lessons/round-64.md`)
- Evidence read: `plans/round-64.md` (incl. errata E1–E3 @ `5613392`); `corpus/lessons/round-63.md`
  (52, 96); `corpus/lessons/round-63-verifier-spotcheck.md`; `.ufo/waves/round-63/w2/MutW2V32.md`
  (860–1009); `.ufo/reports/round-63/kotoba.md:31-32` (fleet repo); `LOG.md:2576,2588`;
  `corpus/QUALITY.md` (Q58/Q59 rows); `corpus/SOURCES.md` (row 62, search log 150–248);
  `verifiers/check_r63_routed_repairs.py`; `SCORECARD.md:28-29,373`;
  `.ufo/waves/round-64/w1/swarm-registry.json`; `.ufo/waves/round-64/w1/ScoutS120.md`;
  `.ufo/waves/round-64/w1/ScoutS049.md`; `.ufo/waves/round-64/w1/ScribeEntry.md` (F10/F10b);
  `.ufo/waves/round-64/w1/RevSourcesGate.md` (§11.1);
  `.ufo/waves/round-64/snapshots/S120.page` (571,600 B, sha256 `15963c3e…`).
