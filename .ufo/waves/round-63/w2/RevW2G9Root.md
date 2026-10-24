# RevW2G9Root

role: revenger, wave 2 falsify (leaf seat; no subagent dispatch, no installs — pacman pause respected, stdlib only, lane untouched except this report)
item: reverse-engineer `g9_conjunct`'s root cause per RevG9Guard finding 9 (the
content-words floor plus `supported()`'s first-4-char prefix test as the shared
evasion gate); produce (1) the minimal "why these bounds" paragraph for the
knowledge entry, (2) a verdict on any single-line change closing the short-tail
lane without touching the frozen predicate's three lines, (3) confirmation that
the plan's guard description matches the committed code word for word.

Attack surface: **committed bytes at cbbee56e** (`git show <rev>:verifiers/
check_scoped_rules_v32.py`, sha256 `4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`).
All probes ran on `/tmp/w2g9root/` copies with the committed sibling verifiers
extracted at the same revision (`check_erratum_absorption.py` `afb4ff74…`,
`check_scoped_rules_v31.py` `a07c2269…`, `check_scoped_rules.py`) — the
self-test loads those siblings from the script's own directory
(`v32:2651-2655`, `check_erratum_absorption.py:81`), so a lone copy cannot run
it. Committed `plans/round-63.md` diffed **byte-identical** to the working
plan, so every plan quote below is the frozen text.

## Headline: the item's premise is stale at the committed tip

RevG9Guard finding 9 described the **pre-commit working copy** (sha
`8371f707…`, untracked at wave 1): gate `w = content_words(clause); if len(w)
< MIN_CONTENT: continue`. The committed bytes at cbbee56e moved the gate:

```python
# verifiers/check_scoped_rules_v32.py:1116-1126 (committed)
        # G9 counts CONTENT WORDS INCLUDING BACKTICKED SPANS: `content_words`
        # strips them, so a fabrication wrapped in backticks would carry too few
        # words to be checked while `page_words` still finds it on the page
        # (RevG9Guard's lane 2). MIN_CLAUSE = 2 is the floor that still checks
        # the smallest fabrication (`and uploads files`); a one-word clause is
        # below A2's own MIN_SHARED floor and stays exempt.
        w = page_words(clause)
        if len(w) < MIN_CLAUSE:
```

`MIN_CONTENT = 3` (v32:314) is, at the committed tip, **A2's whole-cell floor
only** (v32:1145-1147; grep: no other use). The G9 clause gate is
`MIN_CLAUSE = 2` over `page_words` (backticked spans included). Consequences,
all measured on the committed bytes:

- the backtick-smuggle lane (RevG9Guard lane 2) is **closed**:
  `… and \`secretly uploads files\`.` → `['A2 G9: clause "\`secretly uploads files\`." is supported outside the cited line']`;
- the 2-word short tail (lanes 1/6) is **closed**: `… and uploads files.` →
  `['A2 G9: clause "uploads files." is supported outside the cited line']`;
- the **one-word, page-present tail is still admitted** (`… and exfiltrates.`
  with `It also exfiltrates.` on the page → `action_conjunct = []`): the floor
  skips it before any gate sees it;
- the **4-char prefix-collision tail is still admitted** (`… and stores
  rulerboard syntaxis nightly.` with `The job also runs nightly.` on the page →
  `[]`): inherited `supported()` (`SUPPORT_PREFIX = 4`, v32:354, 1038-1039) —
  the prefix test is exactly as wave 1 described, still shared with A2.

So "the content_words floor (MIN_CONTENT=3) plus supported()'s prefix test are
the shared gate for every evasion lane" was true of the wave-1 working copy;
at cbbee56e the surviving short-tail lane is gated by `MIN_CLAUSE`+`MIN_SHARED`
(not `MIN_CONTENT`), and the prefix lane by `supported()` alone. [INFERENCE on
intent: the L1 hardened the guard after wave 1 and documented the divergence
in the code comment and the landed entry — the plan text was left frozen.]

Baseline receipt (my own run, committed bytes, `/tmp/w2g9root`):

```text
$ python3 -B check_scoped_rules_v32.py --self-test   # exit 0
counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2f-compound-purpose-outside-citation: before accepted; after rejected
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
```

The committed self-test now carries 4 G9 unit assertions (v32:2115-2133),
3 G9 mutant probes (v32:2737-2758) and the 3 must-fail arms (v32:2695-2726) —
MutG9Guard's demanded assertions landed. Spot-check that they discriminate:
splicing `if ch == ";":` → `if False:` (sha `1bbde9e4ed406984`) → exit 1,
`FAIL A2 G9: a \`; \`-joined purpose clause off the cited line is rejected` +
`FAIL G9 probe semicolon-split …`, `2 failure(s) over 208 assertions`.

## Deliverable 1 — "why these bounds" paragraph for the knowledge entry

Exact proposed text (slots into `corpus/knowledge/compound-clause-citation-round63.md`,
extending the "Short clauses are exempt." Limits bullet; every clause is
grounded in the receipts below):

> Why these bounds: the clause floor is 2 because 2 is the smallest count this
> guard can act on at all — `fwd_need` never returns less than `MIN_SHARED` =
> 2, so a one-word clause cannot clear even the page arm and checking it is an
> arithmetic no-op; the floor skips exactly what the threshold would skip.
> Clauses that short are A2's job: the whole-cell forward fraction and the
> page-containment arm price every word regardless of clause structure, so G9
> only adds a verdict where a clause is long enough to carry a claim the cited
> line does not make. The support relation is inherited, not introduced: G9
> defines no matcher and scores clauses through A2's own `covered`/`supported`
> pair (same word, or a word sharing its first four characters,
> `SUPPORT_PREFIX = 4`), because the survivor class is defined as a cell that
> passes every A2 arm — any other vocabulary standard would redraw the
> boundary instead of closing the class. The prefix collisions that admission
> still allows are therefore A2's weakness surfaced in a new place, not a
> separate G9 rule.

Receipts behind each clause: `fwd_need(n) = max(MIN_SHARED, ceil(2n/3))`
(v32:1016-1018; measured `fwd_need(1)=2, fwd_need(2)=2, fwd_need(3)=2`);
floor-before-threshold order (v32:1125 → 1127 → 1129); the measured no-ops in
Deliverable 2; `covered`/`supported` reuse (v32:1042-1043, 1035-1039); the
whole-cell A2 arms at v32:1144-1163. The floor value 2 (not the plan's
`MIN_CONTENT = 3`) is also load-bearing on a counted fixture: eligible S901's
action cell splits at `and` into `["Use multiple instruction files per topic",
"apply them selectively."]`, clause 2 has `page_words` n=2 (`them` is a
stopword, `apply` is not), so under the landed floor it is **exercised** and
clears at its cited line (`g9_conjunct(S901, L=4) = []`, measured), whereas
the plan's ≥3-content-words wording would have skipped it. Note the plan's
pre-data sentence "S901/S903 carry no split boundary" is factually wrong about
S901 (committed `ACTIONS["S901"]` contains ` and `); the landed entry already
corrects this ("S901's `and` clause clears the threshold at its cited line") —
no further correction needed there.

## Deliverable 2 — verdict on a single-line change

**Verdict: NO single-line change closes the remaining short-tail lane (the
one-word, page-present tail), and changing the hinted line is a v33 move, NOT
this round — MIN_CONTENT (v32:314) is not even the operative gate at the
committed tip.** Measured on committed bytes, each mutant a fresh copy, full
`--self-test` per copy:

| single-line change | self-test (3 frozen lines) | 1-word tail | effect |
|---|---|---|---|
| pristine cbbee56e (`42460691…`) | exit 0, 208/208 | ADMITTED | — |
| `MIN_CLAUSE = 2` → `1` (`4cfee0d2…`) | exit 0, all 3 lines green | ADMITTED | no-op: `fwd_need(1)=MIN_SHARED=2` makes both arms unsatisfiable |
| `MIN_CONTENT = 3` → `1` (`1eca751e…`) | exit 0, all 3 lines green | ADMITTED | never reaches the clause gate; silently loosens A2's whole-cell floor (no self-test assertion pins it — measured) |
| `MIN_SHARED = 2` → `1` (`26edef2b…`) | exit 0, all 3 lines green | ADMITTED | no-op: the floor still skips the clause first |
| page gate → `covered(w, page) >= max(1, len(w)):` (`a0d24622…`) | exit 0, all 3 lines green | ADMITTED | unreachable for 1-word clauses (floor runs first) |
| **two lines**: `MIN_CLAUSE=1` + `MIN_SHARED=1` (`78fd5f2c…`) | exit 0, all 3 lines green | **rejected**: `['A2 G9: clause "exfiltrates." is supported outside the cited line']` | the minimal measured-closing change needs two coordinated constants |

Every candidate that closes the lane in one line either skips it at the floor
or cannot satisfy `fwd_need`'s `MIN_SHARED` floor; the two constants are
arithmetically coupled (`fwd_need(1) = max(MIN_SHARED, 1) = MIN_SHARED`), so
no one-line rewrite of either alone can do it. Even the two-line combo would
be an edit to a receipt-pinned instrument: the self-test prints
`counter sha256 42460691…` as its own bytes' hash, and the round's method
freezes a predicate per counter version. **Any floor/threshold change is
therefore a v33 move with its own declared-before-data predicate and re-run
controls — out of scope for round 63, exactly as the item hints.** The honest
bound to record is the one the landed entry already states ("a one-word false
tail passes"), now with the measured reason: the floor and the threshold are
coupled through `MIN_SHARED`.

## Deliverable 3 — plan guard description vs committed code, word for word

Plan §C1 "The guard (declared before data)" (frozen; committed plan is
byte-identical to the working copy), checked sentence by sentence:

| # | plan sentence | committed code | verdict |
|---|---|---|---|
| 1 | signature `g9_conjunct(lines, cell, L, page_text)` | v32:1099-1100 | MATCH |
| 2 | "splits the action cell at coordinating boundaries (`;` and the word `and`, case-insensitive, outside backticks)" | `split_clauses` v32:1065-1096; `CLAUSE_AND_RE = re.compile(r"\band\b", re.IGNORECASE)` v32:1061; `;` at 1080-1084; `in_code` guard | MATCH |
| 3 | "for every resulting clause with ≥ `MIN_CONTENT` content words" | `w = page_words(clause); if len(w) < MIN_CLAUSE: continue` (v32:1124-1126), `MIN_CLAUSE = 2` v32:1062 | **MISMATCH** — constant renamed and revalued (3/content_words → 2/page_words incl. backticked spans) |
| 4 | "requires the same forward-support fraction A2 uses (`fwd_need`) from the cited line" | `if covered(w, line_w) >= fwd_need(len(w)): continue` v32:1127 | MATCH |
| 5 | "A clause that the page supports but the cited line does not is rejected as `A2 G9: clause "…" is supported outside the cited line`" | reason literal v32:1130-1132 verbatim; page arm `covered(w, page) >= fwd_need(len(w))` v32:1129 (plan leaves the page-arm threshold unnamed; it is landed as the same `fwd_need` fraction — MutG9 finding 8's INFO note) | MATCH (reason string word for word) |
| 6 | "scoped to page-present clauses so it cannot double-report words the A2 page-containment check already rejects" | docstring v32:1101-1115; extensionally: through `action_conjunct`, A2 containment (v32:1160-1163) returns before `g9_conjunct` (v32:1164-1165), so G9 is reached only with every cell word page-supported and its page arm is then automatically satisfied | MATCH |
| 7 | "`action_conjunct` appends its reasons after `g7_conjunct`'s." | `return g7_conjunct(...) + g9_conjunct(...)` v32:1164-1165 | MATCH |

**Confirmation verdict: 6 of 7 sentences match word for word; sentence 3 does
not.** The divergence is real, deliberate, and *stricter* than the frozen plan
wording: it closes the backtick-smuggle lane and the 2-word short tail, keeps
`eligible rows pass 4 of 4` green (measured), and is documented in the code
comment (v32:1116-1123, naming RevG9Guard's lane 2) and in the landed entry's
rule text ("at least `MIN_CLAUSE` = 2 content words (counted with backticked
spans included)"). The plan itself is frozen and correctly NOT rewritten in
place — but no committed record names the plan-sentence deviation.

**Smallest safe correction (exact proposed text).** The entry already carries
the rule-side facts and the bound; the only missing record is one appended
line tying the landed gate back to the frozen plan sentence. Append to
`LOG.md` (or the round-63 entry's provenance) a dated correction line in the
lane's appended-notice form, e.g.:

> correction (2026-10-23): plans/round-63.md §C1 guard sentence "for every
> resulting clause with ≥ `MIN_CONTENT` content words" landed as "≥
> `MIN_CLAUSE` = 2 page words including backticked spans"
> (`verifiers/check_scoped_rules_v32.py:1124-1126`): the frozen 3-word
> `content_words` floor would have skipped the two-word tail `and uploads
> files` (admitted, RevG9Guard T1) and the backtick-wrapped fabrication
> (RevG9Guard lane 2); measured at cbbee56e the self-test still prints `worlds
> reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` /
> `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`,
> exit 0, 208 assertions, and eligible S901's 2-word `and` clause is exercised
> and clears at its cited line.

No code change is proposed: the committed bytes are receipt-pinned and meet
the frozen predicate; the one-word-tail bound stands as declared until a v33.

## Divergences and confidence

- Stale premise (high confidence, measured): the item's "content_words floor
  (MIN_CONTENT=3) is the shared gate" describes the pre-commit working copy,
  not cbbee56e; at the tip the G9 gate is `MIN_CLAUSE=2`/`page_words`.
- Plan-vs-code constant mismatch (high confidence, byte-level): deliverable 3
  row 3; entry already documents the landed value, nothing documents the plan
  deviation — correction text above.
- Plan pre-data note "S901/S903 carry no split boundary" wrong about S901
  (high confidence, fixture text + measured split); already corrected in the
  landed entry, no action needed.
- Remaining open lanes at cbbee56e (high confidence, measured): one-word
  page-present tail (floor/threshold coupling); 4-char prefix-collision tail
  (inherited `supported()`); wave-1 over-rejection lanes (quote-blind `;`,
  `-and-` compounds, no relatedness test) unchanged — all declared bounds in
  the entry's Limits.
- [INFERENCE] (medium): the hardening happened between the wave-1 probes and
  the commit; the wave-1 reports describe sha `8371f707…` and the committed
  bytes hash `42460691…`, and the code comment cites RevG9Guard's lane 2.
- A2's whole-cell `MIN_CONTENT` floor has no discriminating self-test
  assertion (measured: no `check()` label touches it; `MIN_CONTENT=1` mutant
  stays 208/208 green) — same missing-assertion class MutG9Guard named for
  G9; noted as residual, not this seat's fix.

Artifacts: `/tmp/w2g9root/` — `probe.py`, `probe2.py`, `probe3.py`,
`pristine.out`, `m_minclause1.py` (`4cfee0d2…`), `m_mincontent1.py`
(`1eca751e…`), `m_minshared1.py` (`26edef2b…`), `m_pagegate.py`
(`a0d24622…`), `m_two.py` (`78fd5f2c…`), `m_semi.py` (`1bbde9e4…`). No lane
file besides this report was created or modified; no tools were installed.
