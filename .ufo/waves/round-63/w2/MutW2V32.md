# MutW2V32

role: mutation tester (leaf member — no subagent dispatch, no installs)
item: MutW2V32 — mutation-test the committed v32 counter at `cbbee56e` with
MutG9Guard's six `g9_conjunct` mutants plus two `split_clauses` mutants
(unpaired-backtick handling, hyphen boundary); score each against the frozen
predicate (the file's own `--self-test`); report the kill table verbatim and
the exact missing fixture assertion per surviving mutant.

Target: `verifiers/check_scoped_rules_v32.py` at revision
`cbbee56e9a3589b0b46736ad36f1b77701def80e`, sha256
`4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`
(138846 bytes). Functions under mutation: `g9_conjunct` (v32:1099-1133),
`split_clauses` (v32:1065-1095), `CLAUSE_AND_RE` (v32:1061), and the
`action_conjunct` wiring (v32:1164-1165).

Scratch: `/tmp/mutw2v32` (disposable). Revision-pinned tree extracted with
`git archive cbbee56e | tar -x -C /tmp/mutw2v32/base`; the mutated copy is
`/tmp/mutw2v32/work/verifiers/check_scoped_rules_v32.py`, mutated in place and
restored from `/tmp/mutw2v32/pristine.py` after every variant. **The lane was
not written** — only this report file was created; `git status --porcelain` at
the end shows the same five untracked wave-2 paths as at the start.

Detector: the frozen predicate itself — `python3 -B
verifiers/check_scoped_rules_v32.py --self-test` (208 assertions on the
committed bytes). No tooling was installed for this seat; stdlib `python3` only.

Overlap note: sibling seat `kotoba-r63.MutW2SplitClauses` ran a dedicated
`split_clauses` battery and established that split-`;`-only and split-`and`-only
are killed while seven other splitter mutants survive. I do not re-report their
kill table. I credit their record for the split-`;`-only / split-`and`-only
kills (identical to my M1/M2 below) and re-derive the two `split_clauses`
mutants my own brief names, **adding the mutation-semantics detail their
headline does not carry**: for each of my two survivors I identify the exact
fixture that kills it, and I show that one of the two (the unpaired backtick)
is a **defect-side** survivor — the committed bytes fail the assertion that
pins it — which needs a guard-side correction, not only a fixture.

**Revision note (corrections from the sibling seat, all verified and adopted).**
The sibling re-measured my claims independently and found six specifics wrong
or overstated. I verified each on the committed bytes and **all six
corrections are correct**; §10 records them with the measurements, and the
package in §6 is the one I stand behind. In short: (1) my hyphen fixture does
not kill the left-only hyphen guard — the sibling's ARM6 is strictly stronger
and I adopt it; (2) my FX_BT and their ARM7 are **mutually exclusive** and the
L1 must be shown that, not silently resolved; (3) my guard fix was
**parity-of-count** pairing, which is *not* BACKTICK_RE's pairing — the
corrected fix derives the paired positions from `BACKTICK_RE.finditer` itself;
(4) **my package leaves five of their mutants alive** — verified on my own
bytes, and the union package in §6 replaces it; (5) my example cell does not
actually diverge on clauses, only on pairings; (6) my find-latch description
missed the dominant divergence class.

---

## Findings

### 1. Baseline: the frozen predicate holds on the committed bytes

```
$ cd /tmp/mutw2v32/base && python3 -B verifiers/check_scoped_rules_v32.py --self-test
counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude"
world W3: Cursor reject=True arm=A1 line='entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base'
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line='entry row S900: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)'
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after rejected
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
EXIT=0
```

The three declared lines are all present and the exit is 0. The predicate is
reachable and green.

### 2. THE KILL TABLE (verbatim)

Eight mutants. Each is ONE exact-string replacement in the committed base
bytes; the builder asserts each anchor occurs exactly once, so no mutant can
be a silent no-op (`/tmp/mutw2v32/build.py`, base sha
`4246069129115f03…`, 138846 bytes). Each mutant file was scored by swapping it
into `/tmp/mutw2v32/work/verifiers/check_scoped_rules_v32.py`, running the
frozen predicate, then restoring the pristine bytes and re-hashing.

| mutant | change | frozen G9 instance | three predicate lines | self-test exit | FAIL lines | killed by the frozen predicate? |
|---|---|---|---|---|---|---|
| **pristine** | — | REJECT | all three present | 0 | 0 | — |
| **M1** split-`;` only | `CLAUSE_AND_RE` never matches (only `;` splits) | **ACCEPT** | `survivors closed 5 of 6` | **1** | 6 | **YES** |
| **M2** split-`and` only | the `;` branch is dead (only `and` splits) | REJECT | all three present | **1** | 2 | **YES** |
| **M3** clause `fwd_need`→1 | `covered(w, line_w) >= 1` instead of `>= fwd_need(len(w))` | REJECT | all three present | **1** | 2 | **YES** |
| **M4** guard returns `[]` | `g9_conjunct` returns `[]` unconditionally | **ACCEPT** | `survivors closed 5 of 6` | **1** | 8 | **YES** |
| **M5** page-support-not-line | the cited-line check uses `covered(w, page)` | **ACCEPT** | `survivors closed 5 of 6` | **1** | 8 | **YES** |
| **M6** skip backticked cells | `g9_conjunct` returns `[]` if the cell carries a backticked identifier | REJECT | all three present | **1** | 1 | **YES** |
| **M7** unpaired backtick is literal | a backtick opens code mode only when the cell's backtick count is even | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |
| **M8** hyphen is not a boundary | `CLAUSE_AND_RE = (?<![-\w])and(?![-\w])` | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |

**Six of eight mutants are killed; two survive.** The six kills are exactly
MutG9Guard's six (`split-;` only, `split-and` only, clause `fwd_need`→1,
guard returns `[]`, page-support-not-line, skip backticked cells) — the
committed v32 now carries the four `A2 G9:` discriminating arms (v32:2114-2133)
and the three `g9_probes` (v32:2739-2754) that wave 1 landed from
MutG9Guard's named missing assertions, and they bite all six.

Two mutants are not in MutG9Guard's list and are this seat's own additions to
the `split_clauses` half:

- **M7** — an unpaired backtick does not open a code span.
- **M8** — the word `and` is not a clause boundary when hyphen-adjacent.

Variant sha256 (base `4246069129115f03…`):

```
mut_M1_split_semicolon_only          ec3d06441336ea69fa5b9ad313aca7bc64ea5fb248996284f50e2ce44bc54701
mut_M2_split_and_only                45bbb2d9266e6f5bb1e958fa8e1539b8d52e479eecae8f2ad8e2318f1cf3f931
mut_M3_clause_need_one               85116debe13faa0e9fa58302b479dcc92b4a9ab3848d25511cf9254223d9d87a
mut_M4_guard_returns_empty           67ed29e4f1f127b5039d3436256bd20a9fc2760def7a3a4295842e87ea3b6555
mut_M5_page_support_not_line         641ba9e67cb430042b3803275b8d36b543569b6cc63bc5b91047087ca8d38ea7
mut_M6_skip_backticked_cells         1139005790df3240fabba8db884c5907c104b511ea43b6d5b3cfb70806e44491
mut_M6b_g9guard_wiring               f9f78672580656424ea08df2a0eaec76f2920a8ab89ee807c27ae6e4693a5026
mut_M7_unpaired_backtick_literal     96ddc6040ccb6d6d025d014907880428258d15d40d7b1aa75ee8fa99b6b5ef1b
mut_M8_hyphen_is_not_a_boundary      0cba735c410c05cf9e428deb9160fe7ce5f4bf71d834d79d3b64fa0c269025e4
```

### 3. The six kills, verbatim FAIL lines

**M1** (split-`;` only) — the frozen G9 instance flips to **ACCEPT** and
`survivors closed` drops to 5 of 6:

```
FAIL A2 G9: an `and`-joined purpose clause off the cited line is rejected: got False, expected True
FAIL A2 G9: a clause with one shared word is still rejected (need 2): got False, expected True
FAIL A2 G9: a backticked fabrication is counted and rejected: got False, expected True
FAIL successor survivor verdicts close all six frozen instances: got (True, True, True, True, True, False), expected (True, True, True, True, True, True)
FAIL G9 probe one-supported-word is rejected as supported outside the cited line: got False, expected True
FAIL G9 probe backticked-cell is rejected as supported outside the cited line: got False, expected True
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 5 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 6 failure(s) over 208 assertions
exit 1
```

**M2** (split-`and` only) — all three predicate lines still print and
`survivors closed 6 of 6` still holds; only the two `;`-boundary assertions go
red:

```
FAIL A2 G9: a `;`-joined purpose clause off the cited line is rejected: got False, expected True
FAIL G9 probe semicolon-split is rejected as supported outside the cited line: got False, expected True
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
self-test: 2 failure(s) over 208 assertions
exit 1
```

**M3** (clause `fwd_need`→1) — the two threshold assertions go red; the three
predicate lines are untouched:

```
FAIL A2 G9: a clause with one shared word is still rejected (need 2): got False, expected True
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
FAIL G9 probe one-supported-word is rejected as supported outside the cited line: got False, expected True
self-test: 2 failure(s) over 208 assertions
exit 1
```

**M4** (guard returns `[]`) and **M5** (page-support-not-line) — both make the
frozen instance ACCEPT and print the identical eight FAIL lines:

```
FAIL A2 G9: an `and`-joined purpose clause off the cited line is rejected: got False, expected True
FAIL A2 G9: a `;`-joined purpose clause off the cited line is rejected: got False, expected True
FAIL A2 G9: a clause with one shared word is still rejected (need 2): got False, expected True
FAIL A2 G9: a backticked fabrication is counted and rejected: got False, expected True
worlds reject 7 of 7; eligible rows pass 4 of 4
FAIL successor survivor verdicts close all six frozen instances: got (True, True, True, True, True, False), expected (True, True, True, True, True, True)
survivors closed 5 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
FAIL G9 probe semicolon-split is rejected as supported outside the cited line: got False, expected True
FAIL G9 probe one-supported-word is rejected as supported outside the cited line: got False, expected True
FAIL G9 probe backticked-cell is rejected as supported outside the cited line: got False, expected True
self-test: 8 failure(s) over 208 assertions
exit 1
```

**M6** (skip backticked cells) — killed by exactly one assertion:

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
FAIL G9 probe backticked-cell is rejected as supported outside the cited line: got False, expected True
self-test: 1 failure(s) over 208 assertions
exit 1
```

**M6b** — MutG9Guard's *exact* wiring form of M6 (`action_conjunct` returns
`g7_reasons` early when the cell carries a backticked identifier, instead of my
in-`g9_conjunct` form) is **also killed**, by the same single assertion:

```
FAIL G9 probe backticked-cell is rejected as supported outside the cited line: got False, expected True
self-test: 1 failure(s) over 208 assertions
exit 1
```

So M6 is killed in **both** plausible wirings — the kill is a property of the
guard's placement, not of the mutant's syntax.

### 4. The two survivors — what exactly is unpinned

Both survivors print all three predicate lines, exit 0, and change no
committed-row verdict. The predicate's three lines do **not** fail, so per the
item's rule both are **self-test coverage bounds**, not predicate defects.

#### M7 — unpaired-backtick handling (a DEFECT-SIDE survivor)

The committed `split_clauses` latches `in_code` on **every** backtick and never
un-latches it if the count is odd:

```
1065: def split_clauses(cell: str) -> list[str]:
…
1082:            if ch == "`":
1083:                in_code = not in_code
```

So a cell with **one** backtick has its entire remainder masked as code, and
the clause split never happens. Measured on the committed bytes
(`/tmp/mutw2v32/probe.py`, cell = cited line + `` `glob syntax and secretly
uploads files. ``):

```
C6 unpaired backtick (odd count)       g9=adm action=adm
```

The arm-by-arm breakdown for that cell:

```
stray-backtick  words=10 covered=7 need=7  A2fwd=True  A2page_missing=[]  G7=[]  G9=[]  ACTION=[]
frozen          words=10 covered=7 need=7  A2fwd=True  A2page_missing=[]  G7=[]  G9=['A2 G9: clause "secretly uploads files." is supported outside the cited line']  ACTION=[...same...]
```

That is: the cell carries a compound-purpose clause that the page supports and
the cited line does not — the exact G9 class the guard was landed to close —
and A2's forward fraction (7 of 10, need 7), A2's page containment, reverse
coverage and G7 all pass, so **only G9 can catch it, and G9 is silenced by a
stray backtick**. This is the same class of escape as the frozen survivor,
reachable through a one-character edit of the cell.

The internal inconsistency that makes this a defect rather than a design
choice: `content_words` strips backticked spans with `BACKTICK_RE =
re.compile(r"`([^`]+)`")` (v32:393) and `G7` matches identifiers with
`BACKTICKED_IDENTIFIER_RE = re.compile(r"`([A-Za-z_][A-Za-z0-9_]*)`")`
(v32:405) — **both require a matched pair**. `split_clauses` is the only one of
the three that uses a bare toggle, so an unpaired backtick is masked by
`split_clauses` while being literal text to `content_words` and to `G7`.

Measured: `BACKTICK_RE.findall("…using `glob syntax and secretly uploads files.")`
→ `[]` (nothing stripped), while `split_clauses` returns the whole cell as one
clause.

**Direction matters, and it is what makes M7 different from the other seven
sibling survivors.** M7 makes the counter reject *more*, never less
(`C6 unpaired backtick: adm → REJ`). It is therefore the mutant that
**repairs** the hole. Its survival therefore means: *the committed bytes
contain a hole that no assertion can see*. The fixture that pins the correct
behaviour is **RED on the committed bytes**:

```
=== pristine exit=1
    FAIL A2 G9: a clause after an unbalanced backtick is still rejected: got False, expected True
    self-test: 1 failure(s) over 209 assertions
=== mut_M7_unpaired_backtick_literal exit=0
    self-test: 0 failure(s) over 209 assertions
```

So M7 cannot be closed by adding a fixture alone — it needs the guard-side
correction of §6 first. (Note the sibling seat's M3p has the same *direction*
but a different *mechanism* — theirs gates on "a closing backtick follows",
mine gates on the parity of the cell's backtick count. Both survive; both are
repairs; the fixture text and the guard fix below are the same for both.)

#### M8 — hyphen boundary (a strict-side survivor, clean coverage fixture)

On the committed bytes a hyphen-adjacent `and` **is** a boundary: the regex is
`r"\band\b"` (v32:1061) and `\b` is a word boundary, and a hyphen is a
**non-word** character, so `\band\b` matches the `and` in `and-uploads` and in
`read-and-write`. Measured:

```
=== pristine
  C7 hyphen-adjacent `and`               g9=REJ action=REJ
      reason: A2 G9: clause "-secretly uploads files." is supported outside the cited line
  C8 hyphenated compound                 g9=REJ action=REJ
      reason: A2 G9: clause "-store secrets." is supported outside the cited line
=== mut_M8_hyphen_is_not_a_boundary
  C7 hyphen-adjacent `and`               g9=adm action=adm
  C8 hyphenated compound                 g9=adm action=adm
```

So the committed bytes are the **strict** side here: they reject the
hyphen-glued clause, and M8 is the mutant that stops rejecting it. M8's
survival is a pure coverage gap, and the fixture that kills it is **GREEN on
the committed bytes**:

```
=== pristine exit=0
    self-test: 0 failure(s) over 209 assertions
=== mut_M8_hyphen_is_not_a_boundary exit=1
    FAIL A2 G9: a hyphen-adjacent `and` clause off the cited line is rejected: got False, expected True
    self-test: 1 failure(s) over 209 assertions
```

The sibling seat's M4 (`hyphen is a word char`) is the same family and is
killed by the same fixture (verified below).

### 5. THE FIXTURE × MUTANT MATRIX (verbatim)

Each fixture was spliced into the self-test of each variant and the whole
predicate re-run. `RED` = exit 1 (the fixture fails on that variant),
`green` = exit 0.

```
variant                            FX_BT                   FX_HYPHEN               FX_COMPOUND
pristine                           exit=1 RED              exit=0 green            exit=1 RED
mut_M7_unpaired_backtick_literal   exit=0 green            exit=0 green            exit=1 RED
mut_M8_hyphen_is_not_a_boundary    exit=1 RED              exit=1 RED              exit=0 green
f_bt (guard fix only)              exit=0 green            exit=0 green            exit=1 RED
mut_M1_split_semicolon_only        exit=1 RED              exit=1 RED              exit=1 RED
mut_M2_split_and_only              exit=1 RED              exit=1 RED              exit=1 RED
mut_M3_clause_need_one             exit=1 RED              exit=1 RED              exit=1 RED
mut_M4_guard_returns_empty         exit=1 RED              exit=1 RED              exit=1 RED
mut_M5_page_support_not_line       exit=1 RED              exit=1 RED              exit=1 RED
mut_M6_skip_backticked_cells       exit=1 RED              exit=1 RED              exit=1 RED
restored: 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
```

Cross-check against the sibling seat's *exact* mutant bytes (rebuilt verbatim
from their Artifacts block into `/tmp/mutw2v32/x_sib_M3p.py` sha
`2a6ecf20d245bf85…` and `x_sib_M4.py` sha `ed84f4e616b74c67…`):

```
variant                            FX_BT                   FX_HYPHEN               FX_COMPOUND
pristine                           exit=1 RED              exit=0 green            exit=1 RED
x_sib_M3p (their unpaired backtick) exit=0 green            exit=0 green            exit=1 RED
x_sib_M4 (their hyphen word char)  exit=1 RED              exit=1 RED              exit=0 green
restored: 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
```

**FX_HYPHEN kills both hyphen mutants** (mine M8 and the sibling's M4);
**FX_BT is green on both unpaired-backtick mutants** (mine M7 and the sibling's
M3p) and red on the committed bytes. So the two fixture arms are
complementary to the sibling's seven-arm proposal, not a duplicate of it.

**Correction to this matrix (§10 correction 1):** `FX_HYPHEN` does **not** kill
the *left-only* hyphen guard (`x_M4a`) — it is green there. The sibling seat's
ARM6 kills all three hyphen shapes and is the arm the corrected package
carries. The corrected package's full arm-by-arm matrix is in §6.

### 6. Smallest safe correction (exact text) — FINAL: THE UNION PACKAGE

**This section supersedes my own earlier two packages.** The sibling seat
scored all nine of their mutants against my package bytes and found **five
mutants alive** (M3, M3p, M5, M6, M7). I re-verified that on my own bytes by
rebuilding their nine exact diffs against my package file — it is correct
(§10 correction 4). My package fixed the defect but pinned no assertion for
the guard's *other* semantics, so the no-latch (M3), find-latch (M3p),
quote-protected (M5), case-sensitive (M6) and `;`-glued (M7) variants all pass
it. **Their arm set is a strict superset in coverage.**

The package below is therefore the **union**: the same guard fix (true
`BACKTICK_RE` pairing) + the sibling's eight arms + my `FX_HYPHEN`. It is
measured here to kill **all nine** of the sibling's mutants and all six of
MutG9Guard's, with no harm on the committed corpus.

**Part 1 — the guard fix (required).** In
`verifiers/check_scoped_rules_v32.py`, `split_clauses` (v32:1065-1095), replace
the mask block

```python
    clauses: list[str] = []
    current: list[str] = []
    in_code = False
    i = 0
    while i < len(cell):
        ch = cell[i]
        if ch == "`":
            in_code = not in_code
            current.append(ch)
            i += 1
            continue
```

with

```python
    clauses: list[str] = []
    current: list[str] = []
    in_code = False
    # A backtick opens a code span only when it is part of a CLOSED backtick
    # span -- the same pairing BACKTICK_RE uses for content_words and G7's
    # identifier check.  An unbalanced backtick is literal text: it must not
    # mask the rest of the cell, or one stray backtick would switch the clause
    # split off and let a compound-purpose clause through unchecked.
    paired = set()
    for _m in BACKTICK_RE.finditer(cell):
        paired.add(_m.start())
        paired.add(_m.end() - 1)
    i = 0
    while i < len(cell):
        ch = cell[i]
        if ch == "`":
            if i in paired:
                in_code = not in_code
            current.append(ch)
            i += 1
            continue
```

**Part 2 — the nine arms.** In the self-test, immediately before the
`# -- G9 probes that kill the split/threshold/backtick mutants -----` block
(v32:2726), insert (arms 1-8 are the sibling seat's, reproduced verbatim from
their Artifacts block with arm 7 re-pinned per their §7; arm 9 is mine):

```python
        # -- G9 split-semantics arms (round 63 wave 2, MutW2SplitClauses) --
        g9_split_line = "The configuration stores project rules using glob syntax."
        g9_split_page = (g9_split_line + "\n\n## Unrelated section\n"
                          "The agent secretly uploads files.")
        # (1) the `and` boundary is case-insensitive.
        check("A2 G9: an upper-case `AND` is a clause boundary",
              named(action_conjunct(
                  ["The index stores project rules."],
                  "The index stores project rules AND it is rebuilt nightly.",
                  1,
                  "The index stores project rules.\n\n## Schedule\n"
                  "The index is rebuilt nightly."), "G9"), True)
        # (2) the `and` boundary is a WORD, not a whitespace-delimited token.
        check("A2 G9: a `,` before `and` does not stop the clause split",
              named(action_conjunct(
                  [g9_split_line],
                  g9_split_line[:-1] + ",and secretly uploads files.",
                  1, g9_split_page), "G9"), True)
        # (3) a backticked span is opaque.
        check("A2 G9: a `;` inside a backticked span is not a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  "The index writes mode `quota; limits cold` nightly.",
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), False)
        # (4) the `;` boundary needs no trailing space.
        check("A2 G9: a `;` glued to the next word is still a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  "The index writes mode quota;limits cold nightly.",
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), True)
        # (5) the `;` boundary is not quote-aware.
        check("A2 G9: a `;` inside a double-quoted span is a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  'The index writes mode "quota; limits cold" nightly.',
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), True)
        # (6) the `and` boundary does split inside a `-and-` compound lexeme.
        check("A2 G9: a `-and-` compound lexeme is split at its `and`",
              named(action_conjunct(
                  ["The index uses search-and-replace."],
                  "The index uses search-and-replace nightly.",
                  1,
                  "The index uses search-and-replace.\n\n## Schedule\n"
                  "The index is rebuilt nightly."), "G9"), True)
        # (7) an unpaired backtick does NOT mask the rest of the cell
        #     (MutW2V32's defect-naming form, re-pinned to the fixed
        #     behaviour; MutW2V32's own `FX_HYPHEN` follows).
        check("A2 G9: a clause after an unbalanced backtick is still rejected",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " `glob syntax and uploads files. (S900 :1)",
                  1, g9_page), "G9"), True)
        # (8) an `and` between two closed backtick spans is a boundary.
        check("A2 G9: an `and` between two closed backtick spans is a boundary",
              any(r.startswith("A2 G9: clause \"secretly uploads files")
                  for r in g9_conjunct(
                      ["The tool writes mode quota nightly."],
                      'The tool writes `mode quota` and secretly uploads files `now`.',
                      1,
                      "The tool writes mode quota nightly.\n\n## Appendix\n"
                      "The agent secretly uploads files.")), True)
        # (9) a hyphen-adjacent `and` is a boundary (MutW2V32's `FX_HYPHEN`).
        check("A2 G9: a hyphen-adjacent `and` clause off the cited line is "
              "rejected",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and-uploads files. (S900 :1)",
                  1, g9_page), "G9"), True)
```

**Part 2 note — the exclusivity, resolved by re-pinning, not by omission.**
Arms 1-8 above are the sibling's, with **arm 7 re-pinned** to `expected True`
on MutW2V32's cell (the form that requires the guard fix). The sibling's
*original* arm 7 (`expected False`, pinning the current defective behaviour)
is **not** landed — it is mutually exclusive with the re-pinned form (§10
correction 2). The L1 should land the re-pinned form above and drop the
original.

Measured on the union package (`/tmp/mutw2v32/h_union.py`, sha
`810d9009dd5c1a71fd1b3f4015e14343eaac631886f52b233b1011352ddb8b20`):

```
pristine exit=0
  counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
  self-test: 0 failure(s) over 208 assertions
h_union exit=0 sha256=810d9009dd5c1a71fd1b3f4015e14343eaac631886f52b233b1011352ddb8b20
  counter sha256 810d9009dd5c1a71fd1b3f4015e14343eaac631886f52b233b1011352ddb8b20
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
  self-test: 0 failure(s) over 217 assertions
```

All three predicate lines unchanged, 217 assertions, 0 failures, exit 0.

**The union package kills all nine of the sibling's mutants** (their exact
diffs, rebuilt against the union bytes — `/tmp/mutw2v32/build_all_sib.py`):

```
sib_M1_on_h_union  exit=1  12 failure(s) over 217 assertions
sib_M2_on_h_union  exit=1   4 failure(s) over 217 assertions
sib_M3_on_h_union  exit=1   1 failure(s) over 217 assertions
   FAIL A2 G9: a `;` inside a backticked span is not a clause boundary: got True, expected False
sib_M3p_on_h_union exit=1   1 failure(s) over 217 assertions
   FAIL A2 G9: an `and` between two closed backtick spans is a boundary: got False, expected True
sib_M4_on_h_union  exit=1   2 failure(s) over 217 assertions
sib_M5_on_h_union  exit=1   1 failure(s) over 217 assertions
   FAIL A2 G9: a `;` inside a double-quoted span is a clause boundary: got False, expected True
sib_M6_on_h_union  exit=1   1 failure(s) over 217 assertions
   FAIL A2 G9: an upper-case `AND` is a clause boundary: got False, expected True
sib_M7_on_h_union  exit=1   1 failure(s) over 217 assertions
   FAIL A2 G9: a `;` glued to the next word is still a clause boundary: got False, expected True
sib_M8_on_h_union  exit=1   3 failure(s) over 217 assertions
```

**For contrast, my own 211-assertion package leaves five of them alive**
(`/tmp/mutw2v32/g_final2.py`, sha `80610c21ee473e2d…`, same nine diffs):

```
sib_M1_on_g_final2 exit=1   9 failure(s) over 211 assertions
sib_M2_on_g_final2 exit=1   2 failure(s) over 211 assertions
sib_M3_on_g_final2 exit=0   0 failure(s) over 211 assertions   SURVIVES
sib_M3p_on_g_final2 exit=0  0 failure(s) over 211 assertions   SURVIVES
sib_M4_on_g_final2 exit=1   2 failure(s) over 211 assertions
sib_M5_on_g_final2 exit=0   0 failure(s) over 211 assertions   SURVIVES
sib_M6_on_g_final2 exit=0   0 failure(s) over 211 assertions   SURVIVES
sib_M7_on_g_final2 exit=0   0 failure(s) over 211 assertions   SURVIVES
sib_M8_on_g_final2 exit=1   2 failure(s) over 211 assertions
```

This is the sibling seat's decisive finding, reproduced on my own bytes.

**The superseded 211-assertion package (`g_final2`), for the record:**
guard fix (true `BACKTICK_RE` pairing) + FX_BT + FX_HYPHEN + ARM6 ->
exit 0, `self-test: 0 failure(s) over 211 assertions`, all three predicate
lines unchanged, `judge()` verdicts on the four committed rows byte-identical
(4 of 4 backed). It is **not** the package to land: it leaves five of the
sibling's mutants alive (above). Its arm-by-arm cross matrix, retained for
the record:

```
The corrected package's discrimination, measured arm by arm
(`/tmp/mutw2v32/cross_matrix.py`, ARM6 and ARM7 transcribed verbatim from the
sibling's Artifacts block):

```
variant                            FX_BT               ARM6                ARM7                FX_HYPHEN
pristine                           exit=1 RED          exit=0 green        exit=0 green        exit=0 green
x_sib_M3p (their unpaired backtick) exit=0 green        exit=0 green        exit=1 RED          exit=0 green
x_sib_M4 (their hyphen word char)  exit=1 RED          exit=1 RED          exit=0 green        exit=1 RED
x_M4a (hyphen excluded LEFT only)  exit=1 RED          exit=1 RED          exit=0 green        exit=0 green
x_M4b (hyphen excluded BOTH sides) exit=1 RED          exit=1 RED          exit=0 green        exit=1 RED
x_M4c (hyphen excluded RIGHT only) exit=1 RED          exit=1 RED          exit=0 green        exit=1 RED
x_fix_mine (parity pairing)        exit=0 green        exit=0 green        exit=1 RED          exit=0 green
x_fix_findlatch (find-latch)       exit=0 green        exit=0 green        exit=1 RED          exit=0 green
x_fix_truere (true BT_RE pairing)  exit=0 green        exit=0 green        exit=1 RED          exit=0 green
mut_M7_unpaired_backtick_literal   exit=0 green        exit=0 green        exit=1 RED          exit=0 green
mut_M8_hyphen_is_not_a_boundary    exit=1 RED          exit=1 RED          exit=0 green        exit=1 RED
g_final2 (corrected package)       exit=0 green        exit=0 green        exit=1 RED          exit=0 green
restored: 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
```

```

### 7. No-harm on the committed corpus

`judge()` was run on the **committed** bytes at `cbbee56e` (SKILL.md,
`corpus/knowledge/scoped-rules-round60.md`, `corpus/SOURCES.md`,
`corpus/lessons/round-60.md`, and the round-60 snapshots, all read with
`git show <rev>:<path>`) under pristine and under the **union package**
`h_union`:

```
judge() verdicts identical on committed rows: True
backed count pristine: 4
backed count h_union : 4
```

(The same check on the superseded `g_final2` package also returned
`judge() verdicts identical on committed rows: True`, `4 of 4` — both packages
are no-harm on the committed corpus; they differ only in coverage.)

The per-row verdicts are byte-identical (`Claude Code`, `Copilot CLI`, `Cursor`
and `VS Code` backed; `Codex`, `Gemini CLI`, `opencode` rejected with the same
`why` lists). The `--rev` run on the lane's own committed bytes is unchanged
by construction (the lane file is untouched):

```
$ python3 -B verifiers/check_scoped_rules_v32.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33; rev cbbee56e9a3589b0b46736ad36f1b77701def80e
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
EXIT=1
```

### 8. Reachability of the two holes on the committed corpus

Both holes are **latent on the committed corpus** — neither is reachable by
today's rows, so neither changes a verdict (consistent with §7).

- **Unpaired backtick.** Scanning every table cell of the committed
  `SKILL.md` (66 316 bytes) for an odd backtick count: **0 odd table cells**.
  The three `A2 G9` scope rows' action cells carry 0, 0, 2 and 4 backticks —
  all balanced. So the guard's latent hole cannot fire on any row as written;
  it fires on the next cell that carries one stray backtick.
- **Hyphen-adjacent `and`.** 15 table cells in `SKILL.md` contain a
  hyphen-adjacent `and` (e.g. `search-and-replace`, `config-and-…`), but
  **0 of them are in the 4th (action) column** of a scope row — the ones that
  reach `action_conjunct`. The nearest scope-row action cells are
  `"Create a path-specific instruction file with an `applyTo` glob; use glob
  syntax …"` (Copilot CLI) and `"Use `globs` to scope a rule to specific files
  or directories. Separate multiple patterns with commas."` (Cursor) — no
  hyphen-adjacent `and`, and the `;`/`and` splits they do carry are both
  supported by their cited lines (the eligible rows pass 4 of 4).

Direct replay of every committed scope-table action cell that carries a
citation (7 cells) under pristine and all four surviving/fixed variants:
**0 cells where any mutant changes the verdict**.

### 9. Restoration and lane integrity

Every variant was applied in place to
`/tmp/mutw2v32/work/verifiers/check_scoped_rules_v32.py`, measured, then
restored from `/tmp/mutw2v32/pristine.py` and re-hashed. The final line of
every run:

```
restored sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33  OK
final work copy sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33  OK
```

Lane bytes unchanged at the end of the seat:

```
4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33  verifiers/check_scoped_rules_v32.py
```

`git show cbbee56e:verifiers/check_scoped_rules_v32.py | sha256sum` →
`4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33` (identical).
`git rev-parse HEAD` → `cbbee56e9a3589b0b46736ad36f1b77701def80e` (unchanged).
`git status --porcelain` shows the same five untracked wave-2 paths as at the
start (`w2-dispatch.err`, `w2-dispatch.json`, `w2-spec.json`, `w2/`,
`receipts.new-C1.txt`, `receipts.new-C2-interim.txt`) and no new lane entry
beyond this report file.

### 10. The sibling seat's corrections — verified, adopted, and bounded

`kotoba-r63.MutW2SplitClauses` re-measured my claims independently and found
three specific problems with them. I re-verified each on the committed bytes;
**all three corrections are correct** and are adopted here. The corrected
package is §6; this section is the evidence for the changes.

**Correction 1 — my hyphen fixture does not kill the left-only hyphen guard.
CONFIRMED.** My `FX_HYPHEN` cell is `…glob syntax and-uploads files.`: the
hyphen is on the **right** of the `and`, and the `and` is preceded by a
**space**. A guard that excludes the hyphen only on the left
(`(?<![A-Za-z0-9-])and\b`) therefore still splits it, so `FX_HYPHEN` cannot
see that shape. Measured over the three shapes a real implementation can take:

```
variant                            FX_BT               ARM6                ARM7                FX_HYPHEN
x_M4a (hyphen excluded LEFT only)  exit=1 RED          exit=1 RED          exit=0 green        exit=0 green
x_M4b (hyphen excluded BOTH sides) exit=1 RED          exit=1 RED          exit=0 green        exit=1 RED
x_M4c (hyphen excluded RIGHT only) exit=1 RED          exit=1 RED          exit=0 green        exit=1 RED
```

`FX_HYPHEN` is **green on `x_M4a`** — it does not kill it. The sibling's
**ARM6** (cell `"The index uses search-and-replace nightly."`, hyphen on
**both** sides of the `and`) is red on all three shapes and is green on the
committed bytes. ARM6 is adopted into the package in §6, and `FX_HYPHEN` is
retained as a second arm (it is the only one of the pair that covers a
hyphen on the **right** of the `and`).

**Correction 2 — my FX_BT and the sibling's ARM7 are mutually exclusive.
CONFIRMED, AND IT IS A DECISION FOR THE L1.** `FX_BT` asserts the
unpaired-backtick cell IS rejected (`expected True`); ARM7 asserts it is NOT
(`expected False`). They cannot both hold:

```
variant                            FX_BT               ARM6                ARM7                FX_HYPHEN
pristine                           exit=1 RED          exit=0 green        exit=0 green        exit=0 green
x_sib_M3p (their unpaired backtick) exit=0 green        exit=0 green        exit=1 RED          exit=0 green
g_final2 (guard fix + my arms)     exit=0 green        exit=0 green        exit=1 RED          exit=0 green
```

On the committed bytes `FX_BT` is red and ARM7 is green; after the guard fix
`FX_BT` is green and ARM7 is red. The coherent package — the one that both
fixes the hole and pins the fixed behaviour — takes **FX_BT**, and ARM7 must
be dropped or re-pinned to `expected True`. The L1 must be shown this, not
silently resolved: **do not land both arms.**

**Correction 3 — my guard fix was NOT "exactly BACKTICK_RE's pairing".
CONFIRMED, and I state which implementation I now stand behind.** My first
package paired the cell's backticks by **parity of the count**
(`ticks[k], ticks[k+1]` for `k = 0, 2, 4, …`). That is *not* `BACKTICK_RE`'s
pairing, because `BACKTICK_RE = re.compile(r"`([^`]+)`")` requires a **non-empty**
span: two adjacent backticks are **not** a match, so the pairing shifts.
Measured on `a ``b `c` and d` (a **pairing-level** divergence — see
correction 5 below; the clause split is the same on this particular string):

```
BACKTICK_RE  : [3, 6]  (spans [(3, 7, '`b `')])
parity-pair  : [2, 3, 6, 8]
DIVERGES     : True
```

Randomized differential over 40 000 synthetic cells (alphabet
`a b and ` x y ; ␣ c`): parity pairing and true `BACKTICK_RE` pairing
**diverge on 77 cells, and every one of the 77 contains an empty backtick
span ``` `` ```**; zero divergences on cells without one. The find-latch
implementation the sibling names (`in_code = cell.find("`", i + 1) != -1`)
diverges from both on **158** cells, including the two-closed-span cells
(`'a `b` c and d `e`'`, `` '`x` and `y` and `z`' ``) — it masks the text
*between* two closed spans, which neither pairing does (**this describes the
`(4,2)` class only; the dominant class is `(3,1)` — see correction 6 below**):

```
=== fix_findlatch
   'a `b` c and d `e`'                                            -> ['a `b` c and d `e`']
   '`x` and `y` and `z`'                                          -> ['`x` and `y` and `z`']
=== fix_mine(parity) / fix_truere
   'a `b` c and d `e`'                                            -> ['a `b` c', 'd `e`']
   '`x` and `y` and `z`'                                          -> ['`x`', '`y`', '`z`']
```

**The corrected fix in §6 derives the paired positions from
`BACKTICK_RE.finditer` itself** — it is then *exactly* the pairing
`content_words` and G7 already use, so all three backtick consumers in the
file agree, which was the point I claimed and had not delivered. On the
sibling's ARM8 discriminating cell the corrected fix and the parity fix agree
and the find-latch does not:

```
parity     ARM8 g9 -> ['A2 G9: clause "secretly uploads files `now`." is supported outside the cited line']
truere     ARM8 g9 -> ['A2 G9: clause "secretly uploads files `now`." is supported outside the cited line']
findlatch  ARM8 g9 -> ['A2 G9: clause "The tool writes `mode quota` and secretly uploads files `now`." is supported outside the cited line']
```

Both the parity and the true-pairing fixes make the whole package green
(210 and 211 assertions respectively, exit 0), so the choice between them is
not decided by the fixtures — it is decided by which one makes the file's
three backtick consumers agree. I adopt **true `BACKTICK_RE` pairing**.

**Correction 4 — MY PACKAGE LEAVES FIVE MUTANTS ALIVE. CONFIRMED ON MY OWN
BYTES, AND ADOPTED.** The sibling scored all nine of their mutants against my
package file (`/tmp/mutw2v32/g_final2.py`, sha `80610c21…`) and found five
survivors. I rebuilt their nine exact diffs against my package bytes
(`/tmp/mutw2v32/build_all_sib.py`) and reproduced it exactly:

```
sib_M1_on_g_final2 exit=1   9 failure(s) over 211 assertions
sib_M2_on_g_final2 exit=1   2 failure(s) over 211 assertions
sib_M3_on_g_final2 exit=0   0 failure(s) over 211 assertions   SURVIVES
sib_M3p_on_g_final2 exit=0  0 failure(s) over 211 assertions   SURVIVES
sib_M4_on_g_final2 exit=1   2 failure(s) over 211 assertions
sib_M5_on_g_final2 exit=0   0 failure(s) over 211 assertions   SURVIVES
sib_M6_on_g_final2 exit=0   0 failure(s) over 211 assertions   SURVIVES
sib_M7_on_g_final2 exit=0   0 failure(s) over 211 assertions   SURVIVES
sib_M8_on_g_final2 exit=1   2 failure(s) over 211 assertions
```

The diagnosis is right and it is the same diagnosis as their own: **my
package fixed the defect but pinned no assertion for the guard's other
semantics**, so the no-latch (M3), find-latch (M3p), quote-protected (M5),
case-sensitive (M6) and `;`-glued (M7) variants all pass it. Their arm set is
a strict superset in coverage. **§6 now carries the union package** (their
eight arms + my `FX_HYPHEN` on the same guard fix), which I measured to kill
all nine on my own bytes, with no harm on the committed corpus.

**Correction 5 — my example cell does not actually diverge on CLAUSES.
CONFIRMED.** I used `'a ``b `c` and d'` as "the divergent cell". My *pairing*
figures for it are right (`BACKTICK_RE` pairs `[3,6]`, parity pairs `[2,3]`
and `[6,8]`), but the resulting **clause split** is identical across all
three implementations:

```
'a ``b `c` and d'  parity   -> ['a ``b `c`', 'd']
                   truere   -> ['a ``b `c`', 'd']
                   findlatch-> ['a ``b `c`', 'd']
```

So it is a **pairing-level** divergence, not a clause-level one, and this
particular string is not one of the 135 cells where parity and true pairing
differ in clauses. The general claim stands unchanged (every parity-vs-true
divergence contains an empty backtick span); the example was a poor
illustration of it. Corrected in §10 correction 3 above.

**Correction 6 — my find-latch description missed the dominant class.
CONFIRMED.** I described the find-latch as "masking the text *between* two
closed spans", which describes the `(4,2)` class but not the majority one.
Measured on my own corpus (40 002 cells, seed 20261023):

```
total divergent cells: 81
  (3 backticks, 1 closed span): 71
  (4 backticks, 1 closed span):  6
  (4 backticks, 2 closed spans): 3
  (5 backticks, 1 closed span):  1
```

The dominant class is **(3 backticks, 1 closed span)** — the find-latch keeps
masking across a *closed* span's closing backtick because it looks ahead for
*any* later backtick, so it swallows a `;` that the true pairing splits on.
This is the substantive reason the find-latch must not be landed, and my
one-clause description understated it. Corrected above.

### 11. POST-LANDING: the L1's new `g7_conjunct span_missing` branch is load-bearing but UNPINNED

The sibling seat reported that the L1 has landed the union in the lane
working tree (`verifiers/check_scoped_rules_v32.py`, sha
`12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`, **219
assertions**), and flagged that the landed file carries an extra
`g7_conjunct` `span_missing` arm which is outside both our batteries. That is
G7-level and inside my remit, so I attacked it on the lane's own landed
bytes (copied to `/tmp/mutw2v32/landed_pristine.py`; the lane was not
modified).

**The landed bytes are green and complete on the splitter battery.** Rebuilt
against the landed bytes, all nine of the sibling's mutants are red, and the
`M3`/`M3p` re-expressions relative to the landed guard fix (whose anchor the
landing rewrote) are red too:

```
landed pristine exit=0  self-test: 0 failure(s) over 219 assertions
sib_M1_on_landed_pristine      exit=1 KILLED
sib_M2_on_landed_pristine      exit=1 KILLED
sib_M3post_on_landed_pristine  exit=1 KILLED   FAIL A2 G9: a `;` inside a backticked span is not a clause boundary: got True, expected False
sib_M3ppost_on_landed_pristine exit=1 KILLED   FAIL A2 G9: an `and` between two closed backtick spans is a boundary: got False, expected True
sib_M4_on_landed_pristine      exit=1 KILLED
sib_M5_on_landed_pristine      exit=1 KILLED
sib_M6_on_landed_pristine      exit=1 KILLED
sib_M7_on_landed_pristine      exit=1 KILLED
sib_M8_on_landed_pristine      exit=1 KILLED
```

`judge()` on the committed rows is byte-identical across committed, LANDED
and LANDED-plus-my-assertions: all four rows backed, `4 of 4`.

**The finding: the L1's new `span_missing` branch is LOAD-BEARING but has NO
assertion pinning it.** The branch (landed v32:1055-1068) computes

```python
    span_missing = sorted({
        word
        for span in BACKTICK_RE.findall(cell)
        for word in span.split()
        if len(word) >= 4 and word.lower() not in STOPWORDS
        and word.lower() not in content_words(raw_line)
        and not supported(word.lower(), page_words(raw_page))})
```

and rejects the cell with `A2 G7: backticked span word(s) …`. Six mutants of
it, each one exact-string replacement, scored on the landed 219-assertion
self-test:

| mutant | change | landed self-test | killed? |
|---|---|---|---|
| **SM1** | the whole branch removed (`span_missing = []`) | exit 0, `0 failure(s) over 219 assertions` | **NO — SURVIVES** |
| **SM2** | the `len(word) >= 4` floor dropped | exit 0, `0 failure(s) over 219 assertions` | **NO — SURVIVES** |
| **SM3** | the `STOPWORDS` filter dropped | exit 0, `0 failure(s) over 219 assertions` | **NO — SURVIVES** |
| **SM4** | the page check dropped | exit 1 | YES — `FAIL eligible world: the four counted rows are backed` |
| **SM5** | the cited-line check dropped | exit 0, `0 failure(s) over 219 assertions` | **NO — SURVIVES** |
| **SM6** | the branch always fires | exit 1 | YES — `FAIL eligible world: the four counted rows are backed` |

**SM1 surviving is the important one, because the branch is load-bearing.**
The branch closes an evasion that the landed bytes otherwise admit: a cell
whose backticked span fabricates words occurring neither in the cited line nor
on the page. `content_words()` strips backticked spans, so A2's forward
fraction and page containment cannot see the fabrication, and G9's page gate
skips a clause absent from the page — so with SM1 (branch removed) the cell is
**ADMITTED**:

```
cell: 'The configuration stores project rules using glob syntax and `exfiltrates credentials`.'
  LANDED                G7=REJ  G9=-    ACTION=REJECTED
  SM1 (branch removed)  G7=-    G9=-    ACTION=ADMITTED  <-- EVASION
```

**The missing assertion.** Four arms, each green on the landed bytes and red
on the mutant it targets (`/tmp/mutw2v32/landed_plus_spanfix7.py`, sha
`ae84673ed61d1d2858a7600ab8870c0545163340d39922104a85c967e1da71bf`):

```python
        check("A2 G7: a backticked span whose words occur in neither the "
              "cited line nor the page is rejected",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and `exfiltrates credentials`.",
                  1, g9_page), "G7"), True)
        check("A2 G7: a backticked span made only of stopwords is not "
              "rejected",
              named(action_conjunct(
                  ["The tool writes mode quota nightly."],
                  "The tool writes mode quota nightly and `because otherwise`.",
                  1,
                  "The tool writes mode quota nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), False)
        check("A2 G7: a backticked span word shorter than four characters is "
              "not rejected",
              named(action_conjunct(
                  ["The tool writes mode quota nightly."],
                  "The tool writes mode quota nightly and `ox it`.",
                  1,
                  "The tool writes mode quota nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), False)
        check("A2 G7: a backticked span word present in the cited line is "
              "not rejected even when the page lacks it",
              named(g7_conjunct(
                  ["The tool writes mode quota nightly."],
                  "The tool writes mode quota nightly and `mode quota`.",
                  1,
                  "The tool writes quota nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), False)
```

Measured: the four arms are **green on the landed bytes** (`0 failure(s) over
223 assertions`, exit 0) and turn **all six** `span_missing` mutants red:

```
landed_plus_spanfix7           exit=0  self-test: 0 failure(s) over 223 assertions
spanfix7_SM1  exit=1 KILLED   FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected
spanfix7_SM2  exit=1 KILLED   FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False
spanfix7_SM3  exit=1 KILLED   FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
spanfix7_SM4  exit=1 KILLED   FAIL eligible world: the four counted rows are backed
spanfix7_SM5  exit=1 KILLED   FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lack
spanfix7_SM6  exit=1 KILLED   FAIL eligible world: the four counted rows are backed
```

and the nine splitter mutants stay red on top of them:

```
sib_M1..M8 on landed_plus_spanfix7  exit=1 KILLED (all nine)
```

`judge()` verdicts on the committed rows remain byte-identical (4 of 4 backed,
`committed == LANDED+4assertions: True`).

Two notes on why SM2, SM3 and SM5 are genuine coverage gaps rather than
equivalent mutants. Over 20 000 random cells SM2 differs from the landed
behaviour on **3 607** (it starts rejecting spans made of short or stopword
words); SM3 differs on any span whose only ≥4-character word is a stopword
(e.g. `` `because otherwise` `` — landed accepts, SM3 rejects); and SM5
differs on a span word present in the **cited line but absent from the page**
(e.g. `` `mode quota` `` — landed accepts because the cited-line check saves
it, SM5 rejects). SM3 and SM5 are exactly what the second and fourth arms
above pin.

**Scope note.** The landed file also carries a `MutW2GuardEvasion` block of
three new `A2 G9` arms (a two-word off-citation clause is rejected; a clause
absent from the page is NOT reported by G9; a one-word clause is exempt as a
declared bound). Those are G9-level and inside my remit; I read them and they
are consistent with the committed guard's semantics, and the one-word-clause
arm is labelled a declared bound rather than an endorsement — which is the
labelling discipline this report has used throughout. I did not re-report
them as findings because they are L1 additions with assertions already
pinning them.

### 12. POST-INTEGRATION: the sibling's three E3 claims, checked against the committed tip

The sibling seat reported three checkable defects in the L1's Erratum E3
(`plans/round-63.md`). The lane has since advanced — the L1 committed the
integration (`849a546`), the final measurements (`2ba4547`) and the sibling's
own post-landing update (`75370a5`), and the working tree is clean. I checked
all three claims against the **committed tip** (`75370a5`) rather than the
working tree the sibling was looking at. **None of the three holds at the
tip**, and one of them targets the wrong document.

**Claim 1 — "the receipt names both wordings … the receipt names NEITHER …
the entry `corpus/knowledge/erratum-absorption-round62.md` names neither
either".** This rests on a misreading of E3 and on the wrong entry file. E3's
sentence is: "The deviation and both wordings are documented in the code
only — `MIN_CONTENT = 3` at v32:314 …, `MIN_CLAUSE = 2` at v32:1072, and the
`g9_conjunct` floor comment at v32:1136-1140; **the entry names the landed
rule**, and the refreshed receipt names the landed sha and assertion count."
E3 does not claim the *receipt* names the wordings. The entry it names is the
**round-63** entry, added by the L1 in `849a546` —
`corpus/knowledge/compound-clause-citation-round63.md` — and that entry names
the landed rule with both wordings and the deviation recorded:

```
34: outside backticked spans. For each resulting clause with at least
35: `MIN_CLAUSE` = 2 content words (counted with backticked spans included), require
45: "every resulting clause with ≥ `MIN_CONTENT` content words"; the landed gate is
46: stricter — ≥ `MIN_CLAUSE` = 2 **page** words with backticked spans included —
```

Measured: `MIN_CLAUSE` ×4 (lines 34, 46, 79, 97) and `MIN_CONTENT` ×1 (line 45)
in `compound-clause-citation-round63.md`. The sibling grepped
`erratum-absorption-round62.md` — the **round-62** entry, a different document —
where both counts are 0, and concluded the wordings are in the code only. They
are in the round-63 entry, exactly as E3 says. E3's three code citations also
resolve correctly against the landed bytes: `MIN_CONTENT = 3` is at v32:314,
`MIN_CLAUSE = 2` at v32:1072, and the floor comment at v32:1136-1140.

**Claim 2 — "the receipt is stale on two numbers: sha 5523088… / 205
assertions against the landed 12d093a1… / 219".** RESOLVED at the tip. The
stale values the sibling saw are the pre-refresh receipt; the committed
receipt now reads

```
counter sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
self-test: 0 failure(s) over 219 assertions
```

which is the landed sha and the landed assertion count. It was refreshed in
`2ba4547` ("final receipts at measured rev 849a546e (C1 219 assertions …)").

**Claim 3 — "E2's 're-run recorded in
`.ufo/waves/round-63/receipts/C2-before-rerun.txt`' — that file does not exist
anywhere in the tree."** RESOLVED at the tip. The file exists and is committed
at `849a546`; its tail is

```
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
the do-nothing control at 35d44b4b4dcdda234b5dbff7af37e432fec55f05 is never a certification
exit=1
```

which is exactly the hardened-counter re-run E2 claims (`0 of 5`, exit 1, with
E1's two-conjunct `append-only` failing at `grew_by=0`).

**My own §11 finding is unchanged and still live at the tip.** The committed
`v32` is sha `12d093a1…` — byte-identical to the landed bytes I attacked — and
at the final tip `75370a5`:

```
landed base sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
landed pristine exit=0  self-test: 0 failure(s) over 219 assertions
landed_SM1_branch_removed      exit=0 SURVIVED  self-test: 0 failure(s) over 219 assertions
```

and there is exactly **one** `check("A2 G7: …")` assertion in the file
(`"A2 G7: an unsupported backticked identifier is rejected"`), which targets
the `missing` (identifier) branch, not `span_missing`. So the L1's G7
multi-word-span arm is landed but **still unpinned** by any assertion, and the
four arms in §11 remain unlanded. The round-63 entry describes that arm
correctly ("backticked span words are caught by G7's multi-word span arm
(`A2 G7: backticked span word(s) …`, landed in erratum E3)") and makes no
claim that it is asserted — consistent with §11.

---

## Verdict

**The committed predicate holds; six of eight mutants are killed; two survive,
and the two survivors are self-test coverage bounds (the predicate's three
lines do not fail).** The six kills confirm that wave 1's landing of
MutG9Guard's named missing assertions (the four `A2 G9:` arms and the three
`g9_probes`) closed MutG9Guard's wave-1 gap: every one of MutG9Guard's six
mutants is now red at exit 1 on the committed bytes, in both plausible wirings
for the skip-backticked-cells mutant.

**The one finding that is not merely a coverage bound is M7 (unpaired backtick),
and it is a defect in the committed guard, not in the suite.** On the committed
bytes a cell carrying a single stray backtick has its entire remainder masked
as code by `split_clauses`, so the compound-purpose clause is never split out
and G9 is silent — while A2's forward fraction, A2's page containment, reverse
coverage and G7 all pass, i.e. exactly the G9 class the guard was landed to
close, reached through a one-character edit of the cell. The mutant M7 (and
the sibling seat's M3p, which reaches the same state by a different route)
**repairs** that hole, so its survival means the committed bytes contain a
hole no assertion can see. `content_words` (`BACKTICK_RE`) and G7
(`BACKTICKED_IDENTIFIER_RE`) both require a *matched pair* of backticks;
`split_clauses` is the only one of the three that uses a bare toggle, and
aligning it with the other two is the smallest safe correction.

**Smallest safe correction, exact text, in §6 — the UNION package.** (1) derive
the paired backtick positions from `BACKTICK_RE.finditer` in `split_clauses`,
so a backtick masks a span only when it is part of a **closed** span — the same
pairing `content_words` and G7 already use; (2) land the **sibling seat's
eight arms** (with arm 7 re-pinned to `expected True` on MutW2V32's cell)
plus **my `FX_HYPHEN`**. Measured on the union package `h_union`: **217
assertions, 0 failures, exit 0**, all three predicate lines unchanged,
`judge()` verdicts on the four committed rows byte-identical (4 of 4 backed),
and **all nine of the sibling's mutants and all six of MutG9Guard's mutants
are red**.

**My own first package is superseded and must not be landed.** It fixed the
defect but pinned no assertion for the guard's other semantics, leaving five
of the sibling's mutants alive (M3 no-latch, M3p find-latch, M5
quote-protected, M6 case-sensitive, M7 `;`-glued) — verified on my own bytes
by rebuilding their nine exact diffs against my package file (§10 correction
4). The sibling's arm set is a strict superset in coverage; the union is what
I stand behind.

**One decision the L1 must make explicitly, not silently.** The unpaired-
backtick fixture comes in two mutually exclusive forms — the re-pinned
`expected True` (the fixed behaviour, red on the committed bytes) and the
sibling's original ARM7 `expected False` (pins the current defective
behaviour, green on the committed bytes). They cannot both hold (§10
correction 2). The union package takes the **re-pinned** form, because it
lands the guard fix; the original ARM7 must be dropped. **Do not land both.**

**Post-integration status (§11, §12).** The L1 has committed the integration
(`849a546`), the final measurements (`2ba4547`) and the sibling's post-landing
update (`75370a5`); the working tree is clean and the committed `v32` is sha
`12d093a1…`, byte-identical to the landed bytes I attacked. Against that
committed tip: all nine splitter mutants are **red**; the L1's own additional
`g7_conjunct span_missing` branch is **load-bearing but still unpinned** —
`SM1` (the branch deleted) survives the 219-assertion self-test, and with it
deleted a cell whose backticked span fabricates words occurring neither in the
cited line nor on the page is **ADMITTED**. The four arms in §11 are green on
the committed bytes and turn all six `span_missing` mutants red, with no
change to any committed-row verdict; they are **not yet landed**.

Three defects reported against Erratum E3 by the sibling seat do **not** hold
at the committed tip (§12): E3's "the entry names the landed rule" is true of
the round-63 entry the L1 added (`compound-clause-citation-round63.md` names
`MIN_CLAUSE` ×4 and `MIN_CONTENT` ×1, with the deviation recorded) — the
sibling checked the round-62 entry instead; the C1 receipt is no longer stale
(it names `12d093a1…` / `219 assertions`, refreshed in `2ba4547`); and
`C2-before-rerun.txt` exists and is committed at `849a546`, satisfying E2's
claim. The L1 should not act on those three.

**Coverage bound, stated for the L1.** M8 (hyphen boundary) is a pure coverage
gap and needs no behaviour change: the committed bytes already take the strict
side (a hyphen-adjacent `and` is a boundary, so `…glob syntax and-uploads
files.` is rejected with `A2 G9: clause "-uploads files. (S900 :1)" is
supported outside the cited line`), and the hyphen arms pin that. The sibling
seat's seven-arm proposal covers the same family; their hyphen arm is killed by
the same fixture as mine, and their unpaired-backtick arm is green under the
same guard fix. The L1 should take one hyphen fixture per hyphen-guard shape
that matters (ARM6 covers all three) and one unpaired-backtick fixture, not two
of each.

**What would change my mind:** the L1 showing a committed-corpus action cell
with an odd backtick count or a hyphen-adjacent `and` (which would make the
hole live rather than latent — my scan found none), or a reasoned argument that
`split_clauses`'s bare toggle is intended and that the plan's guard wording
("split … outside backticks") means "outside any backtick, paired or not"
rather than "outside a closed backtick span". Note that under the second
reading `content_words` and G7 — which require a matched pair — would be
inconsistent with `split_clauses`, and I could not reach a reading under which
all three agree except the paired one.

Report: .ufo/waves/round-63/w2/MutW2V32.md
