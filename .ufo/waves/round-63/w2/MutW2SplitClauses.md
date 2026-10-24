# MutW2SplitClauses

role: mutation-tester (leaf member — no subagent dispatch)
item: dedicated `split_clauses` mutation battery on committed v32 at `cbbee56e` (/tmp copy).

Target: `verifiers/check_scoped_rules_v32.py` at revision
`cbbee56e9a3589b0b46736ad36f1b77701def80e`, sha256
`4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`.
Function under mutation: `split_clauses` (v32:1065-1095) and the boundary
regex `CLAUSE_AND_RE` (v32:1061) it uses; the downstream consumer is
`g9_conjunct` (v32:1099-1133) via `action_conjunct` (v32:1136-1165).

Scratch: `/tmp/mutw2split` (disposable). Revision-pinned tree extracted with
`git archive cbbee56e verifiers | tar -x -C /tmp/mutw2split/base`; the working
copy is `/tmp/mutw2split/work/verifiers/`, mutated in place and restored from
`/tmp/mutw2split/pristine.py` after every mutant. **The lane was not written**:
only this report file was created. `git status --porcelain` at the end shows
the same five untracked wave-2 paths as at the start and no new lane entry.

Detectors used (all bounded, all on the same bytes):
1. **The frozen predicate** — the file's own `--self-test` (the plan's
   one-sentence predicate: prints `worlds reject 7 of 7; eligible rows pass 4 of 4`,
   `survivors closed 6 of 6`, `must-fail G9 disabled admits
   e2f-compound-purpose-outside-citation: yes`, and exits 0).
2. **The nine RevG9Guard probe cells** — replayed by `/tmp/mutw2split/driver.py`,
   which calls `action_conjunct(lines, cell, 1, page)` and `g9_conjunct(...)`
   directly, plus the four eligible fixture rows (S900 L=5, S901/S902/S903 L=4)
   as a false-positive control.

No tooling was installed for this seat; the battery is stdlib `python3` only.

---

## Findings

### 1. The frozen predicate kills M1 and M2; it is blind to seven other splitter mutants

Pristine baseline, reproduced on the revision-pinned copy:

```
$ cd /tmp/mutw2split/base && python3 -B verifiers/check_scoped_rules_v32.py --self-test ; echo "exit=$?"
counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
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
exit=0
```

### 2. THE KILL TABLE (verbatim)

Nine mutants, each a minimal behaviour-bearing edit of `split_clauses` or of
`CLAUSE_AND_RE`. The diffs are reproduced in **Artifacts** below.

| mutant | change | frozen G9 instance | three predicate lines | self-test exit | FAIL lines | killed by the frozen predicate? |
|---|---|---|---|---|---|---|
| **pristine** | — | REJECT | all three present | 0 | 0 | — |
| **M1** | split on `;` only (`CLAUSE_AND_RE` never matches) | **ACCEPT** | `[True, **False**, True]` — `survivors closed 5 of 6` | **1** | 6 | **YES** |
| **M2** | split on `and` only (the `;` branch is dead) | REJECT | `[True, True, True]` | **1** | 2 | **YES** |
| **M3** | no `in_code` latch — a backtick does not protect | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |
| **M3p** | an unpaired backtick is a literal (it does not latch code mode) | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |
| **M4** | hyphen is a word char — `search-and-replace` never splits | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |
| **M5** | double-quoted spans are protected | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |
| **M6** | the `and` boundary is case-SENSITIVE | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |
| **M7** | the `;` boundary requires a trailing space | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |
| **M8** | the `and` boundary is space-delimited (`\sand\s`) | REJECT | all three present | 0 | 0 | **NO — SURVIVES** |

**Seven of nine splitter mutants survive the frozen predicate unchanged.** The
four eligible rows are unchanged under every mutant (`ELIGIBLE S900 L=5 ACTION []`
… `ELIGIBLE S903 L=4 ACTION []` in every run), so the eligible-row arm cannot
see a splitter change either — it is a false-positive control, not a detector.

### 3. M1 and M2 — the two kills, with the exact failing assertions

**M1** (split on `;` only) — the frozen G9 instance flips to **admitted** and the
predicate goes red. Verbatim:

```
FAIL A2 G9: an `and`-joined purpose clause off the cited line is rejected: got False, expected True
FAIL A2 G9: a clause with one shared word is still rejected (need 2): got False, expected True
FAIL A2 G9: a backticked fabrication is counted and rejected: got False, expected True
FAIL successor survivor verdicts close all six frozen instances: got (True, True, True, True, True, False), expected (True, True, True, True, True, True)
FAIL G9 probe one-supported-word is rejected as supported outside the cited line: got False, expected True
FAIL G9 probe backticked-cell is rejected as supported outside the cited line: got False, expected True
survivors closed 5 of 6
exit 1
```

**M2** (split on `and` only) — the three predicate lines all still print and
`survivors closed 6 of 6` still holds; only the two `;`-boundary assertions go
red. Verbatim:

```
FAIL A2 G9: a `;`-joined purpose clause off the cited line is rejected: got False, expected True
FAIL G9 probe semicolon-split is rejected as supported outside the cited line: got False, expected True
survivors closed 6 of 6
exit 1
```

Both kills come from the arms wave 1 added (v32:2119-2123 and the
`g9_probes` tuple at v32:2739-2755) — i.e. from MutG9Guard's named missing
assertions, not from the plan's three lines.

### 4. THE PREDICATE-DEFECT CHECK: no mutant that keeps both boundaries flips the frozen instance

The item's rule is that *the frozen G9 instance must reject under every mutant
that keeps both boundaries*, and that any mutant flipping it to admitted is a
predicate defect to be named.

Measured on the committed bytes, the frozen instance's verdict under each mutant:

| mutant | keeps `;` boundary | keeps `and` boundary | frozen G9 instance | verdict |
|---|---|---|---|---|
| pristine | yes | yes | REJECT `A2 G9: clause "secretly uploads files." is supported outside the cited line` | — |
| M1 | **yes** | **no** (removed) | **ACCEPT** | admitted, **but M1 is killed** (exit 1, `survivors closed 5 of 6`) |
| M2 | **no** (removed) | yes | REJECT | rejected; M2 killed (exit 1) |
| M3 | yes | yes | REJECT | **no defect** |
| M3p | yes | yes | REJECT | **no defect** |
| M4 | yes | yes | REJECT | **no defect** |
| M5 | yes | yes | REJECT | **no defect** |
| M6 | yes | yes | REJECT | **no defect** |
| M7 | yes | yes | REJECT | **no defect** |
| M8 | yes | yes | REJECT | **no defect** |

**No mutant that keeps both boundaries flips the frozen instance to admitted,
so there is NO predicate defect of the "frozen instance admitted" kind on the
committed bytes.** The one mutant that does admit the frozen instance, M1,
removes the `and` boundary entirely — it is a *different* splitter, not a
weakening of this one — and the predicate already kills it (`survivors closed
5 of 6`, exit 1). The frozen predicate's contract is therefore sound as
stated.

### 5. THE NINE RevG9Guard PROBE CELLS, scored on the committed bytes

`/tmp/mutw2split/driver.py` output on the pristine `cbbee56e` bytes
(`REJECT` = an `A2 G9:` reason is present; `ACCEPT` = no G9 reason):

```
RG-01 frozen instance                    REJECT ['A2 G9: clause "secretly uploads files." is supported outside the cited line']
RG-02 `and uploads files.`               REJECT ['A2 G9: clause "uploads files." is supported outside the cited line']
RG-03 `and exfiltrates.`                 ACCEPT []
RG-04 backticked span                    REJECT ['A2 G9: clause "`secretly uploads files`." is supported outside the cited line']
RG-05 8-word backticked fabrication      REJECT ['A2 G9: clause "`secretly uploads files mirror telemetry beacon remote endpoint nightly`." is supported outside the cited line']
RG-06 unpaired backtick                  ACCEPT []
RG-07 rulerboard/syntaxis collision      ACCEPT []
RG-08 search-and-replace hyphen          ACCEPT ['A2: action cell supports 7 of its 11 content word(s) at line 1 (need >= 8)']
RG-09 quoted quota;-limits               ACCEPT ['A2: action cell supports 4 of its 9 content word(s) at line 1 (need >= 6)']
RG-10 legitimate two-clause cell         REJECT ['A2 G9: clause "rotates them weekly into archives." is supported outside the cited line']
```

Three of RevG9Guard's wave-1 verdicts **do not reproduce on the committed
bytes** — the committed v32 has moved past the working copy RevG9Guard attacked
(sha `8371f707…`):

- **RG-02 (`and uploads files.`) now REJECTs.** On the wave-1 working copy it
  was ACCEPTed (the clause had 2 distinct content words, below `MIN_CONTENT`
  = 3). The committed v32 counts clause words with `page_words` and floors at
  `MIN_CLAUSE = 2` (v32:1062, 1124-1125), so the two-word tail is now checked.
- **RG-04 (backticked span) and RG-05 (8-word backticked fabrication) now
  REJECT.** Same cause: `page_words(clause)` keeps backticked spans, so the
  backticked fabrication is counted. RevG9Guard's lane 2 is closed on the
  committed bytes.
- **RG-10 (legitimate two-clause cell) still REJECTs** — the over-rejection
  lane is **still open**: the rule has no "unrelated purpose" test, so a
  related continuation clause is rejected.

Also still open on the committed bytes, and unchanged by any mutant in the
battery (they are contract-level, not splitter-level): **RG-03** (one-word
tail), **RG-06** (unpaired backtick), **RG-07** (4-char prefix collision).

### 6. WHAT EACH SURVIVING MUTANT EXPOSES — the exact assertion each one needs

A surviving mutant is a **coverage finding**: the frozen predicate cannot see
that particular splitter behaviour. Each surviving mutant is killed by exactly
one new assertion. Every assertion below is **green on the committed bytes**
(it pins the contract as it stands, it does not change it) and **red on its
target mutant**. All seven together are green on pristine (215 assertions,
exit 0) and turn every one of the nine mutants red — measured in **Artifacts**.

| surviving mutant | exact assertion that kills it (and is green on pristine) | the bound it exposes |
|---|---|---|
| **M3** (no `in_code` latch) | `A2 G9: a `;` inside a backticked span is not a clause boundary` (expected `False`) | The backtick opacity is unpinned. On the committed bytes a backticked span IS opaque; M3 breaks that and nothing notices. |
| **M3p** (unpaired backtick is literal) | `A2 G9: an unpaired backtick suppresses the `and` clause split` (expected `False`) | The unpaired-backtick lane is unpinned. **Note the direction:** the committed bytes *suppress* the split (an unpaired backtick latches code mode to the end of the cell — RG-06 ACCEPT). This assertion pins the CURRENT (defective) behaviour so the mutant is visible; it does not bless it. |
| **M4** (hyphen is a word char) | `A2 G9: a `-and-` compound lexeme is split at its `and`` (expected `True`) | The `-and-` boundary is unpinned. The committed bytes split `search-and-replace` (over-rejection, RevG9Guard lane 3); this assertion pins the current behaviour so the mutant is visible. |
| **M5** (quoted spans protected) | `A2 G9: a `;` inside a double-quoted span is a clause boundary` (expected `True`) | The quote-awareness of the `;` boundary is unpinned. The committed bytes split inside double quotes (over-rejection, RevG9Guard lane 4); this assertion pins the current behaviour so the mutant is visible. |
| **M6** (case-sensitive `and`) | `A2 G9: an upper-case `AND` is a clause boundary` (expected `True`) | The plan's declared "case-insensitive" is unpinned. `AND` in a cell is an evasion lane (X-16 below). |
| **M7** (`;` needs a trailing space) | `A2 G9: a `;` glued to the next word is still a clause boundary` (expected `True`) | The `;` boundary's right-hand context is unpinned. `syntax;secretly` is an evasion lane. |
| **M8** (space-delimited `and`) | `A2 G9: a `,` before `and` does not stop the clause split` (expected `True`) | The `and` boundary's left-hand context is unpinned. `syntax,and` is an evasion lane. |

Three of these seven (M3p, M4, M5) pin a **known-defective** lane. They are
admissible as *coverage* arms (green on the committed bytes) but they must be
labelled as bounds, not as endorsements: they make the counter's current
over-rejection / evasion surface **visible to the suite** so that a future
change to it is a deliberate act, and they leave the decision to fix the lane
to the L1.

**Two further probe cells are worth recording as they stand** (they are the
evasion lanes M7/M8/M6 open, and they are ACCEPTed on the committed bytes):

```
X-13 hyphen compound control             REJECT ['A2 G9: clause "-replace nightly." is supported outside the cited line']
X-14 quoted-semicolon control            REJECT ['A2 G9: clause "limits cold" nightly." is supported outside the cited line']
X-15 backticked-semicolon control        ACCEPT []
X-16 upper-case AND                      REJECT ['A2 G9: clause "it is rebuilt nightly." is supported outside the cited line']
X-17 repeated-word tail                  ACCEPT []
X-18 pure-stopword tail                  ACCEPT []
```

### 7. Probe-cell verdict flips per mutant

The battery's effect on the probe cells, verbatim from the driver:

| mutant | probe-cell VERDICT flips | probe-cell reason-text changes (same verdict) |
|---|---|---|
| M1 | F01 frozen instance (REJECT→ACCEPT), F02 two-word tail (REJECT→ACCEPT), F04 backticked span (REJECT→ACCEPT), F11 legitimate two-clause (REJECT→ACCEPT), F13 hyphen control (REJECT→ACCEPT), F16 upper-case AND (REJECT→ACCEPT) | F05 eight-word backticked |
| M2 | F14 quoted-semicolon control (REJECT→ACCEPT) | none |
| M3 | F06 unpaired backtick (ACCEPT→**REJECT**), F15 backticked-semicolon control (ACCEPT→**REJECT**) | none |
| M3p | F06 unpaired backtick (ACCEPT→**REJECT**) | none |
| M4 | F13 hyphen compound control (REJECT→ACCEPT) | none |
| M5 | F14 quoted-semicolon control (REJECT→ACCEPT) | none |
| M6 | F16 upper-case AND (REJECT→ACCEPT) | none |
| M7 | none | none |
| M8 | F13 hyphen compound control (REJECT→ACCEPT) | none |

M3 and M3p are the two mutants that **close** an open lane (F06 unpaired
backtick, and F15 with M3): under them the counter rejects more, never less.
M1 is the only mutant that makes the counter **accept** the frozen instance.

### 7b. The M3p guard-fix package (MutW2V32's, verified here) — and its exclusivity with my arm 7

The sibling seat `MutW2V32` independently measured that **M3p's survival has a
defect side, not only a coverage side**. I re-measured its claims on the
committed bytes rather than accepting them; all three hold.

**Verified.** The unpaired-backtick cell
`"The configuration stores project rules using glob syntax `glob syntax and uploads files. (S900 :1)"`
is **admitted** by `action_conjunct` on the committed bytes (reasons `[]`; the
lone backtick latches `in_code` and masks the whole rest of the cell, so the
clause split never happens). M3p turns that into a rejection. So M3p is the
mutant that *repairs* a real hole, and because the predicate's three lines do
not fail on pristine, it remains a **self-test coverage bound** in the strict
sense — but the missing fixture is a **guard-side correction**, not a fixture
that is red on the committed bytes.

**MutW2V32's proposed guard fix** — mask only CLOSED backtick spans in
`split_clauses` — verified on the committed bytes:

```
=== TRUE BACKTICK_RE-pairing guard fix + their FX1: exit 0
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
  self-test: 0 failure(s) over 209 assertions
=== --rev run, exit 1
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 b333de06e6f1c3752d946ba3dbaaf730a3eaa586d46363d921809ec7eda321bd; rev cbbee56e9a3589b0b46736ad36f1b77701def80e
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
```

The four committed rows stay **4 of 4 backed** and the three reject lines are
unchanged; only the `counter sha256` line differs, necessarily (the bytes
changed). With the **find-based** latch variant (`in_code = cell.find("`", i+1) != -1`)
plus MutW2V32's two fixtures: `self-test: 0 failure(s) over 210 assertions`,
exit 0, all three predicate lines unchanged. **The guard-fix package is
admissible and harmless.**

**Three corrections to the peer proposal, all measured here.** They matter for
the L1's decision, so they are recorded rather than left in IRC.

1. **A find-based latch is NOT "exactly `BACKTICK_RE`'s pairing".** The two
   diverge on a cell with two closed spans — the find-based latch masks the
   text *between* two closed spans (it looks ahead for *any* later backtick);
   true pairing does not:
   ```
   'a `b` c and d `e`'   find-latch -> ['a `b` c and d `e`']      BT_RE-pair -> ['a `b` c', 'd `e`']
   '`x` and `y` and `z`' find-latch -> ['`x` and `y` and `z`']    BT_RE-pair -> ['`x`', '`y`', '`z`']
   ```
   The **true `BACKTICK_RE`-pairing** variant is the one to take: it is what
   `content_words` and G7 already use, so the file's three backtick consumers
   then agree. It also already green-lights MutW2V32's FX1.

2. **MutW2V32's FX2 does not kill every "hyphen is a word char" shape.** Its
   cell is `and-uploads` — the hyphen is on the **right** of `and`, with a
   space before it. Measured against the three shapes a real implementation can
   take:
   ```
   M4a hyphen excluded LEFT only   (?<![A-Za-z0-9-])and\b            -> THEIR FX2 SURVIVES
   M4b hyphen excluded BOTH sides  (?<![A-Za-z0-9-])and(?![A-Za-z0-9-]) -> their FX2 kills it
   M4c hyphen excluded RIGHT only  \band(?![A-Za-z0-9-])               -> their FX2 kills it
   ```
   **My arm 6 kills all three** (`search-and-replace` exercises a hyphen on
   *both* sides of the `and`), and it is green on the committed bytes. The
   L1 should take arm 6 for the hyphen lane; the two are not mutually
   exclusive, but only arm 6 is complete.

3. **MutW2V32's FX1 and my arm 7 are MUTUALLY EXCLUSIVE.** Mine expects the
   committed behaviour (`expected False`); theirs expects the fixed behaviour
   (`expected True`, red until the guard fix lands). Measured both ways:
   ```
   my arm 7 alone (no guard fix):   exit 0, 0 failure(s) over 209 assertions
   my arm 7 + the guard fix:         exit 1
     FAIL A2 G9: an unpaired backtick suppresses the `and` clause split: got True, expected False
   ```
   This is a **decision for the L1, not a merge**: land the guard fix and
   re-pin the arm with `expected True` (MutW2V32's direction), or keep the
   committed bytes and pin the current contract with `expected False` (my
   direction). Landing the guard fix without re-pinning leaves the suite red.

### 7c. THE COMPLETE PACKAGE, VERIFIED END-TO-END

The guard fix and the eight arms together, on the committed bytes:

- **Guard fix** in `split_clauses` — mask only CLOSED backtick spans, using
  the same pairing `content_words` and G7 already use:
  ```python
          if ch == "`":
              in_code = any(m.start() == i for m in BACKTICK_RE.finditer(cell))
              current.append(ch)
              i += 1
              continue
  ```
- **Arms 1-7** as in Artifacts, with arm 7 **re-pinned to `expected True`**
  (the fixed behaviour) and arm 7's cell changed to MutW2V32's form
  (`g9_line[:-1] + " `glob syntax and uploads files. (S900 :1)"`).
- **Arm 8 (new, added here)** — the arm that distinguishes the true
  `BACKTICK_RE` pairing from a find-based latch, which §7b correction 1
  shows are different implementations. It is green on the committed bytes AND
  on the fixed bytes, and red on the find-based variant:
  ```python
        check("A2 G9: an `and` between two closed backtick spans is a boundary",
              any(r.startswith("A2 G9: clause \"secretly uploads files")
                  for r in g9_conjunct(
                      ["The tool writes mode quota nightly."],
                      'The tool writes `mode quota` and secretly uploads files `now`.',
                      1,
                      "The tool writes mode quota nightly.\n\n## Appendix\n"
                      "The agent secretly uploads files.")), True)
  ```

Measured, verbatim:

```
=== FULL PACKAGE (guard fix + 8 arms) on pristine: exit 0
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
  self-test: 0 failure(s) over 216 assertions
  PACKAGE+M3-post(no latch)    exit 1 FAILs 1
     FAIL A2 G9: a `;` inside a backticked span is not a clause boundary: got True, expected False
  PACKAGE+M3p-post(find-latch) exit 1 FAILs 1
     FAIL A2 G9: an `and` between two closed backtick spans is a boundary: got False, expected True
  PACKAGE+M1 exit 1 FAILs 11
  PACKAGE+M2 exit 1 FAILs 4
  PACKAGE+M4 exit 1 FAILs 1
  PACKAGE+M5-post(quote-protected) exit 1 FAILs 1
     FAIL A2 G9: a `;` inside a double-quoted span is a clause boundary: got False, expected True
```

(M1, M2, M4, M6, M7, M8 were already measured red on the package in the same
run: M1 11 FAILs, M2 4 FAILs, M4 1 FAIL.) The three latch mutants M3 and
M3p were re-expressed **relative to the fixed bytes** — their original anchors
are the same lines the guard fix rewrites, so they cannot be applied on top of
it without redefinition; `M3-post` is "no latch at all" and `M3p-post` is the
find-based latch.

**This package is the complete answer to the battery**: green on the committed
bytes (216 assertions, exit 0), all three predicate lines unchanged, the four
committed rows still 4 of 4 backed, and **all nine mutants red**.

### 7d. THE TWO PACKAGES COMPARED — MINE KILLS ALL NINE, THE SIBLING'S LEAVES FIVE ALIVE

`MutW2V32` refined its guard fix to derive the paired positions from
`BACKTICK_RE.finditer` itself and shipped a package at
`/tmp/mutw2v32/g_final2.py`, sha256
`80610c21ee473e2d779fb6d29c2906d5a22acc58779b4a2a10f3d6f2c568b7d3`
(211 assertions, exit 0, three predicate lines unchanged, four committed rows
4 of 4 — all verified here). **Its guard-fix implementation is behaviourally
identical to mine**: a differential over 40 005 synthetic cells shows
`MINE` (`in_code = any(m.start() == i for m in BACKTICK_RE.finditer(cell))`)
versus `THEIRS` (the paired-position set) at **0 divergent cells**. The two
are the same fix.

The **arms** differ, and the difference is decisive. Measured against the
sibling's actual package file (its bytes, its fixtures, its guard fix):

```
sibling package sha256 80610c21ee473e2d779fb6d29c2906d5a22acc58779b4a2a10f3d6f2c568b7d3

  M1   KILLED    exit 1  FAILs 9
  M2   KILLED    exit 1  FAILs 2
  M3   SURVIVES  exit 0  FAILs 0
  M3p  SURVIVES  exit 0  FAILs 0
  M4   KILLED    exit 1  FAILs 2
  M5   SURVIVES  exit 0  FAILs 0
  M6   SURVIVES  exit 0  FAILs 0
  M7   SURVIVES  exit 0  FAILs 0
  M8   KILLED    exit 1  FAILs 2
```

against my package (guard fix + 8 arms), the same nine mutants:

```
=== MY PACKAGE on the pristine committed bytes: exit 0  sha f96d8b6b0a10
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
  self-test: 0 failure(s) over 216 assertions

=== all nine mutants against MY PACKAGE
  M1   KILLED    exit 1  FAILs 11
  M2   KILLED    exit 1  FAILs 4
  M3   KILLED    exit 1  FAILs 1
       FAIL A2 G9: a `;` inside a backticked span is not a clause boundary: got True, expected False
  M3p  KILLED    exit 1  FAILs 1
       FAIL A2 G9: an `and` between two closed backtick spans is a boundary: got False, expected True
  M4   KILLED    exit 1  FAILs 1
       FAIL A2 G9: a `-and-` compound lexeme is split at its `and`: got False, expected True
  M5   KILLED    exit 1  FAILs 1
       FAIL A2 G9: a `;` inside a double-quoted span is a clause boundary: got False, expected True
  M6   KILLED    exit 1  FAILs 1
       FAIL A2 G9: an upper-case `AND` is a clause boundary: got False, expected True
  M7   KILLED    exit 1  FAILs 1
       FAIL A2 G9: a `;` glued to the next word is still a clause boundary: got False, expected True
  M8   KILLED    exit 1  FAILs 2

SURVIVORS against my package: 'none — all nine killed'
```

**The sibling's package leaves five mutants alive (M3, M3p, M5, M6, M7)** —
including the two the sibling's own report names as its headline lanes (M3p
and M4 are *both* alive in its package; M4 is killed there only by the hyphen
fixture, not by anything covering the backtick lanes). The L1 should land
**my package**, which is a superset of arms over the same guard fix, and the
two are not in conflict on the fix itself.

### 7e. DIFFERENTIAL VERIFICATION OF THE THREE PAIRING IMPLEMENTATIONS

The peer bounded its parity-vs-true-pairing divergence with a randomized
differential over 40 000 synthetic cells. I re-ran it with my own corpus and
transcriptions, and it reproduces exactly.

**Four implementations compared**, all in `split_clauses`:

| impl | rule |
|---|---|
| `PARITY` | parity-of-count pairing (`ticks[k], ticks[k+1]` for `k = 0,2,4,…`) — the peer's first implementation |
| `FINDLATCH` | `in_code = cell.find("`", i + 1) != -1` — my M3p |
| `MINE` | `in_code = any(m.start() == i for m in BACKTICK_RE.finditer(cell))` |
| `THEIRS` | the paired-position set derived from `BACKTICK_RE.finditer` — the peer's refined implementation |

Measured over 40 000 synthetic cells (alphabet `a b a n d ` x y ; space c`,
seed 20261023):

```
  PARITY vs TRUE BACKTICK_RE   135 divergent; with '``' = 135, without = 0
  FINDLATCH vs TRUE BACKTICK_RE  336 divergent; with '``' = 55, without = 281
  PARITY vs FINDLATCH            437 divergent; with '``' = 156, without = 281

  MINE vs THEIRS: 0 divergent cells (over 40002 cells, INCLUDING two-closed-span cells)

  CLAIM: every PARITY-vs-TRUE divergence contains '``' -> True
```

**The peer's central claim is confirmed exactly**: parity-of-count pairing and
true `BACKTICK_RE` pairing diverge **only** on cells containing an empty
backtick span (` `` `), and on **zero** cells without one — because
`BACKTICK_RE` requires a non-empty span, so an empty span shifts the
pairing. The peer's refusal to simply concede was right.

**Two refinements to the peer's characterisation of the find-latch**, both
measured:

1. **The find-latch divergence is NOT only the two-closed-span class.** The
   peer's description ("the find-latch masks the text BETWEEN two closed
   spans") explains the `(4,2)` class but not the dominant one. The full
   histogram of the 336 divergent cells, by (number of backticks, number of
   closed spans):
   ```
   {(3,1): 239, (4,1): 39, (4,2): 38, (5,1): 5, (5,2): 9, (6,2): 2, (6,3): 2, (7,2): 1, (7,3): 1}
   ```
   The dominant class is **(3 backticks, 1 closed span) — 239 of 336 cells** —
   where the find-latch keeps masking across a *closed* span's closing
   backtick because it looks ahead for *any* later backtick. Example:
   ```
   '`a ;ya` cbb;na` x'   findlatch -> ['`a ;ya` cbb;na` x']
                         theirs    -> ['`a ;ya` cbb', 'na` x']
   ```
   The find-latch swallows the `;` that the true pairing splits on. This is
   the same defect class as the two-closed-span case, but it is the *majority*
   class, and it is the reason the find-latch must not be landed.

2. **The peer's own example cell does not actually diverge.** On
   `'a ``b `c` and d'` all three of `PARITY`, `THEIRS` and `FINDLATCH` return
   the same clauses (`['a ``b `c`', 'd']`). The peer's pairing figures for
   that cell (`BACKTICK_RE` pairs `[3,6]`, parity pairs `[2,3,6,8]`) describe
   the *pairings*, which do differ; but the resulting **clause split** is the
   same on that particular string. The divergence is real in general (135
   cells for parity-vs-true) but this cell is not one of them.

**The decisive fact for the L1**: `MINE` and `THEIRS` are **0 divergent cells
apart** over 40 002 cells, including the two-closed-span cases. The peer
adopted my recommendation and arrived at an implementation that is
behaviourally identical to mine. The fix is settled; only the arm set
differs, and §7d measures that difference.

### 7f. THE UNION PACKAGE — INDEPENDENTLY VERIFIED BY ME, ALL NINE RED

`MutW2V32` rebuilt the union independently (its own builder, its own bytes)
and shipped it at `/tmp/mutw2v32/h_union.py`, sha256
`810d9009dd5c1a71fd1b3f4015e14343eaac631886f52b233b1011352ddb8b20` — my eight
arms (arm 7 re-pinned per §7b) plus its own `FX_HYPHEN`, on the same
`BACKTICK_RE`-pairing guard fix. **I verified it with my own harness and my
own nine diffs**, not by citing the peer's numbers:

```
union package sha256 810d9009dd5c1a71fd1b3f4015e14343eaac631886f52b233b1011352ddb8b20
union self-test: exit 0
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
  self-test: 0 failure(s) over 217 assertions
union --rev: exit 1
scoped rule files backed on committed snapshots 4 of 4; live not run
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client

=== all nine of my mutants against the SIBLING's union package
  M1   KILLED    exit 1  FAILs 12
  M2   KILLED    exit 1  FAILs 4
  M3   KILLED    exit 1  FAILs 1
       FAIL A2 G9: a `;` inside a backticked span is not a clause boundary: got True, expected False
  M3p  KILLED    exit 1  FAILs 1
       FAIL A2 G9: an `and` between two closed backtick spans is a boundary: got False, expected True
  M4   KILLED    exit 1  FAILs 2
  M5   KILLED    exit 1  FAILs 1
       FAIL A2 G9: a `;` inside a double-quoted span is a clause boundary: got False, expected True
  M6   KILLED    exit 1  FAILs 1
       FAIL A2 G9: an upper-case `AND` is a clause boundary: got False, expected True
  M7   KILLED    exit 1  FAILs 1
       FAIL A2 G9: a `;` glued to the next word is still a clause boundary: got False, expected True
  M8   KILLED    exit 1  FAILs 3
SURVIVORS against the union package: 'none — all nine killed'
```

**The union package is my arm set plus one.** Arm-by-arm, the union's
`check("A2 G9: …")` names (line numbers in `h_union.py`) against mine:

| union line | arm | mine |
|---|---|---|
| 2741 | an upper-case `AND` is a clause boundary | arm 1 |
| 2749 | a `,` before `and` does not stop the clause split | arm 2 |
| 2755 | a `;` inside a backticked span is not a clause boundary | arm 3 |
| 2763 | a `;` glued to the next word is still a clause boundary | arm 4 |
| 2771 | a `;` inside a double-quoted span is a clause boundary | arm 5 |
| 2779 | a `-and-` compound lexeme is split at its `and` | arm 6 |
| 2789 | a clause after an unbalanced backtick is still rejected | arm 7 **re-pinned to `expected True`** |
| 2795 | an `and` between two closed backtick spans is a boundary | arm 8 |
| 2804 | a hyphen-adjacent `and` clause off the cited line is rejected | **the sibling's `FX_HYPHEN`** (its 10th arm; mine is subsumed by arm 6) |

The union's arm 7 is the re-pinned unpaired-backtick arm (§7b) and the union's
arm 8 is my two-closed-span arm (§7c). The union therefore carries **every**
arm from this report, plus the sibling's hyphen arm, on the shared guard fix.
The four pre-existing wave-1 arms (union lines 2124-2139) are untouched.

**The union package is the single landing point.** It is the same guard fix
(my implementation and the peer's are 0 divergent cells apart, §7e), it
supersedes the peer's superseded `g_final2.py` (which leaves five mutants
alive, §7d), and it carries the full arm set — 217 assertions, exit 0, all
three predicate lines unchanged, the four committed rows still 4 of 4 backed,
and all nine mutants red under my own diffs.

**The shared caveat, stated for the record.** Two of the arms —
`A2 G9: a `;` inside a double-quoted span is a clause boundary` (arm 5) and
`A2 G9: a `-and-` compound lexeme is split at its `and`` (arm 6) — pin
behaviour that RevG9Guard already named **defective**: they freeze the
current over-rejection surface (a quoted `;` splits, so a legitimate cell
carrying a quoted `;` is rejected with a mangled fragment reason; a `-and-`
compound splits, so a legitimate hyphenated cell is rejected). They are
admissible as **coverage** arms — green on the committed bytes, and they make
that surface visible so a future change to it is a deliberate act — but they
must be labelled **bounds, not endorsements**. Fixing either lane later
requires re-pinning that arm. This is a shared caveat, not a disagreement
between the two seats: both reports carry it.

### 7g. POST-LANDING VERIFICATION OF THE LANE'S OWN BYTES

During this seat's final pass the L1 landed the package into the lane
working tree. The landed file is
`verifiers/check_scoped_rules_v32.py`, sha256
`12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`
(uncommitted at the time of this check; `git status` shows ` M` on that one
path). I snapshotted those exact bytes to
`/tmp/mutw2split/landed/verifiers/` and re-ran **my own** battery against
them — I did not take the L1's word for it.

```
landed snapshot sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
  LANDED + M1   KILLED    exit 1 FAILs 13
  LANDED + M2   KILLED    exit 1 FAILs 4
  LANDED + M3   KILLED    exit 1 FAILs 1
       FAIL A2 G9: a `;` inside a backticked span is not a clause boundary: got True, expected False
  LANDED + M3p  KILLED    exit 1 FAILs 1
       FAIL A2 G9: an `and` between two closed backtick spans is a boundary: got False, expected True
  LANDED + M4   KILLED    exit 1 FAILs 1
       FAIL A2 G9: a `-and-` compound lexeme is split at its `and`: got False, expected True
  LANDED + M5   KILLED    exit 1 FAILs 1
       FAIL A2 G9: a `;` inside a double-quoted span is a clause boundary: got False, expected True
  LANDED + M6   KILLED    exit 1 FAILs 1
       FAIL A2 G9: an upper-case `AND` is a clause boundary: got False, expected True
  LANDED + M7   KILLED    exit 1 FAILs 1
       FAIL A2 G9: a `;` glued to the next word is still a clause boundary: got False, expected True
  LANDED + M8   KILLED    exit 1 FAILs 2
SURVIVORS against the LANDED bytes: 'none — all nine killed'
```

**The landed bytes are green on the committed bytes and kill all nine
mutants.** The lane's own self-test on those bytes: `worlds reject 7 of 7;
eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `must-fail G9
disabled admits e2f-compound-purpose-outside-citation: yes` /
`self-test: 0 failure(s) over 219 assertions`, exit 0; and `--rev cbbee56e`
still prints `scoped rule files backed on committed snapshots 4 of 4`.

**Probe-cell diff, landed bytes vs the committed baseline** — exactly one cell
changed, and it is the defect closing:

```
CELL F06-unpaired-backtick
-  CLAUSES ['The configuration stores project rules using glob syntax `and secretly uploads files.']
-  ACTION []
-  G9_ONLY []
+  CLAUSES ['The configuration stores project rules using glob syntax `', 'secretly uploads files.']
+  ACTION ['A2 G9: clause "secretly uploads files." is supported outside the cited line']
+  G9_ONLY ['A2 G9: clause "secretly uploads files." is supported outside the cited line']
```

Every other cell — including all four eligible rows — is **byte-identical** to
the committed baseline. The unpaired-backtick cell that the committed bytes
admitted is now rejected, and nothing else moved. That is the no-harm
evidence for the landed change.

**One change in the landed file is outside this battery's scope** and is
flagged, not judged, here: the L1 also added a `G7` arm to `g7_conjunct`
(`span_missing` — backticked-span words that occur in neither the cited line
nor the page). It is a `g7_conjunct`-level addition, not a `split_clauses`
one, and it did not move any of this battery's probe cells or eligible rows.
It is recorded here only so the L1 knows it is unexamined by this seat.

### 7h. THE L1's E3 TEXT, CHECKED AGAINST THE LANE — THREE FLAGS, ONE OF THEM HALF MINE, ALL CLOSED

The L1 added **Erratum E3** to `plans/round-63.md` (now committed at
`75370a5`), narrating this seat's finding and the landing. Most of it is
accurate. I checked three of its checkable claims against the lane rather
than accepting the narration and flagged all three. Two were real at the
moment I checked (a stale receipt, an absent receipt file) and both are now
fixed; the third flag was **half my own error** — right about the receipt,
wrong about which entry file to grep — and is corrected in item 1 below.
Every statement in this subsection is measured against the **committed tip**,
not a working tree — `MutW2V32` caught that distinction (§12) and is right to
insist on it.

**Accurate** (checked): "`BACKTICK_RE`-pairing fix in `split_clauses`" —
landed at v32:1092 as `in_code = any(m.start() == i for m in
BACKTICK_RE.finditer(cell))`, which is exactly my §7e implementation.
"eight split-semantics arms" — the landed file carries exactly my eight
(plus the peer's `FX_HYPHEN` and three `MutW2GuardEvasion` arms; 15 `A2 G9:`
checks in total, 4 pre-existing + 11 new). "three clause-floor/page-gate
assertions" — present at v32:2820-2837. "the G7 multi-word-span extension"
— present at v32:1055-1067. "Self-test: 219 assertions" — the landed file
prints exactly that, exit 0. And the **substantive** claim —
"`MIN_CONTENT` content words" landed as "`MIN_CLAUSE` = 2 **page** words
including backticked spans" — is **TRUE**, and is exactly what I measured in
§5 of this report against the committed bytes: `g9_conjunct` floors on
`page_words(clause)` at `MIN_CLAUSE = 2` (v32:1140), so the two-word
off-citation tail and the backticked fabrications that the wave-1 working copy
admitted are now rejected. That part of E3 is right and is my finding.

**Not accurate**, in E3:

1. **"the receipt names both wordings" — the receipt half was factually right,
   the entry half was MY ERROR and is corrected here.** No receipt names
   either wording, at any revision:
   ```
   for f in .ufo/waves/round-63/receipts/*:
     grep -c "MIN_CLAUSE|MIN_CONTENT"  ->  0  for every file, including at HEAD
   ```
   So *that* half of the sentence was false. But I then grepped the **wrong
   entry file**:
   `corpus/knowledge/erratum-absorption-round62.md` is the **round-62** entry,
   whereas E3's sentence sits in a round-63 plan and names the **round-63**
   entry, `corpus/knowledge/compound-clause-citation-round63.md`. I recorded
   "the entry names neither either", and that is **wrong**. Measured against
   the right file:
   ```
   round-63 entry AT cbbee56 (when I checked):  MIN_CLAUSE x3, MIN_CONTENT x0
   round-63 entry AT THE TIP:                   MIN_CLAUSE x4, MIN_CONTENT x1
   round-62 entry (the file I grepped):         MIN_CLAUSE x0, MIN_CONTENT x0
   ```
   **And there was never a committed revision in which the sentence was
   false.** My first draft of this correction kept a clause claiming "at
   cbbee56 the entry named only one wording, so the sentence was then not
   satisfied". `MutW2V32` rejected it (§12) and is right — I verified the
   history myself:
   ```
   git show <rev>:plans/round-63.md | grep -c "Erratum E3":
     cbbee56 0 | 849a546 1 | 2ba4547 1 | 75370a5 1 | HEAD 1
   git log --all -S"documented in the code and entry"   -- plans/round-63.md  -> (empty)
   git log --all -S"receipt names both wordings"        -- plans/round-63.md  -> (empty)
   ```
   E3 did not exist at `cbbee56` at all. Its actual sentence is **"the entry
   names the landed rule"**, which is present from `849a546` onward and
   absent before it — so it was **true at every revision where it exists**.
   E3 and the entry's `MIN_CONTENT` line arrived in the **same** commit, so
   the sentence was true at introduction and is true at the tip. Comparing
   the entry's `cbbee56` state against a sentence written two commits later
   was a **temporal mismatch** on my part.

   **A second correction, on the provenance of the wording I quoted.** I
   first wrote here that the sentence "documented in the code and entry; the
   receipt names both wordings" was "a pre-commit draft the L1 superseded".
   That is an **inference I cannot support and have withdrawn**
   (`MutW2V32`, §12, second precision). What the record actually shows: the
   wording appears in **no commit** (`git log --all -S` finds nothing for
   either phrase), in **no file** in the tree except this report, and in no
   snapshot of `plans/round-63.md` I could recover from jj's operation log.
   So the honest statement is the narrower one: **I quoted E3 inaccurately,
   and then audited the entry that my inaccurate quote happened to name.**
   "Superseded draft" asserts a process I did not observe; a future reader
   would go looking for an artefact that does not exist. Withdrawn.

   The correct criticism of my flag is therefore only this: **I misquoted
   E3 and grepped the round-62 entry rather than the round-63 one.** The
   lessons: when a plan sentence says "the entry", resolve *which* entry;
   when auditing paperwork, audit the **committed** text rather than a
   working tree caught mid-edit; and do not narrate a provenance you cannot
   produce evidence for.

   Two things are still true and worth keeping, because they are why the flag
   was worth raising at the time even though its evidence was flawed: the
   **receipt genuinely does not name either wording** (verified at HEAD, all
   five files in `receipts/`), and the committed E3 correctly responds to that
   by attributing the wordings to the **code only** and giving the entry and
   the receipt their own, narrower jobs. The committed text is accurate; my
   flag was one part right, one part wrong, and one part misquoted.
2. **The receipt WAS stale on two numbers** (now refreshed — see the
   resolution block below), independently of the wording question — and the
   receipt-drift finding was already raised by `RevW2C1Predicate` and
   `RevW2ScorecardWording`, so the L1 folded their proposed three-token edit
   in rather than re-deriving it:
   ```
   receipt: v32 sha256 552308806b17e0e48fedb083eb6d55b722a7ef080aa7de8402601bbbc27d8f39
            self-test: 0 failure(s) over 205 assertions
   landed : v32 sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
            self-test: 0 failure(s) over 219 assertions
   ```
   At the time, the receipt's sha was two revisions stale (it named the
   pre-wave-1 working copy `5523088…`; `42460691…` was the cbbee56e value and
   `12d093a1…` is the landed one), and its assertion count read 205 against
   the landed 219. It now reads `12d093a1…` / 219.
3. **E2's "re-run recorded in `.ufo/waves/round-63/receipts/C2-before-rerun.txt`" —
   that file did not exist when I checked** (it is now committed — see the
   resolution block). The receipts directory held exactly one file
   (`C1-g9-measure.txt`); `find` over the whole tree finds no
   `C2-before-rerun*`. The **claim itself is true** — I re-ran the hardened
   C2 counter at the before-control and it does print `r62 routed defects
   closed 0 of 5`, exit 1 — but the named receipt is absent, so the plan
   points at a file that was never written. The two existing controls
   (`.ufo/waves/round-63/controls/C2-before-r62tip.txt`) are the r62-tip
   run, not the hardened re-run.

None of the three is a defect in the landed **counter**: the landed v32 is
green, kills all nine mutants, and moves exactly one probe cell (§7g). All
three are in the plan/receipt paperwork, and they are the L1's to correct —
I flag them here rather than edit anything, per my seat's bounds.

**Resolution status, re-checked against the COMMITTED TIP (`75370a5`), not
the working tree.** All three are closed, and `MutW2V32` is the seat that
forced the final check (§12): it tested against the committed tip rather than
the working tree and found the lane had moved under me — the L1 committed the
integration (`849a546`), the final measurements (`2ba4547`) and this report's
own post-landing update (`75370a5`). Re-measured there:

- **#1 is RESOLVED, though not on my evidence.** The committed E3 no longer
  says "the receipt names both wordings". It now splits into three separately
  checkable claims, and **all three hold at `75370a5`**:
  (a) "The deviation and both wordings are documented in the code only —
  `MIN_CONTENT = 3` at v32:314, `MIN_CLAUSE = 2` at v32:1072, and the
  `g9_conjunct` floor comment at v32:1136-1140" — verified line-for-line;
  (b) "the entry names the landed rule" — the **round-63** entry
  `compound-clause-citation-round63.md` now carries `MIN_CLAUSE` x4
  (lines 35, 46, 79, 97) and `MIN_CONTENT` x1 (line 45), so it names both;
  (c) "the refreshed receipt names the landed sha and assertion count" —
  verified in #2 below. So the outcome is right, but my contribution to it
  was a **correct receipt finding and an incorrect entry finding** (§1 above),
  and the entry sentence became true because `849a546` added `MIN_CONTENT` to
  the round-63 entry, not because my grep was right.
- **#3 is RESOLVED.** `.ufo/waves/round-63/receipts/C2-before-rerun.txt` now
  exists and contains exactly the output I measured: the five `FAIL` lines,
  `r62 routed defects closed 0 of 5`, and `exit=1`.
- **#2 is RESOLVED.** It persisted for one edit — a refreshed receipt existed
  only at **cbbee56e** (`42460691…`, 208 assertions), while the plan asserted
  "the refreshed receipt names the landed sha and assertion count" and no file
  named `12d093a1…` or `219`. The L1 then rewrote
  `.ufo/waves/round-63/receipts/C1-g9-measure.txt` in place. It now opens
  `counter sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`
  — the landed sha — and closes
  `self-test: 0 failure(s) over 219 assertions` / `exit=0`, with all seven
  world lines, the six survivor lines and the three must-fail lines intact.
  I re-ran that command against the lane's landed bytes and it reproduces
  line-for-line. The receipt now describes the bytes it sits beside.

**All three are now closed against the committed tip.** One correction is owed
to `MutW2V32`, who tested against `75370a5` rather than the working tree: my
#1 evidence was half wrong (wrong entry file, §1), and two of the three items
had already been satisfied by the L1's own commits before I re-flagged them.
The flags were worth raising when raised — the receipt *was* stale and
`C2-before-rerun.txt` *was* absent at the moment I checked — but a seat that
checks paperwork should re-check it at the tip before reporting.

**Also checked and fine:** the L1's `MutW2GuardEvasion` arms are consistent
with the guard's semantics, and the one-word arm is labelled a declared bound
rather than an endorsement.

**None of the three was ever a defect in the landed counter.** They were
plan/receipt paperwork; the landed v32 is green, kills all nine mutants, and
moves exactly one probe cell (§7g).

**The one item still live at the tip is not mine.** `MutW2V32`'s §11 shows the
L1's own `g7_conjunct` `span_missing` branch is load-bearing but unpinned:
with the branch deleted (SM1) the 219-assertion self-test still exits 0, and
there is exactly one `check("A2 G7: …")` assertion in the file, targeting the
identifier branch rather than `span_missing`. That is a `g7_conjunct`-level
gap, outside this battery's remit, and it is in front of the seat that owns
that guard family with four measured arms ready.

### 8. Restoration and lane integrity

Every mutant was applied in place to
`/tmp/mutw2split/work/verifiers/check_scoped_rules_v32.py`, measured, then
restored from `/tmp/mutw2split/pristine.py` and re-hashed. The final line of
the kill-table run:

```
restored sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33 (pristine 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33)
```

Lane bytes unchanged at the end of the seat:

```
4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33  verifiers/check_scoped_rules_v32.py
a07c2269ea077e4866827e3fae907c45aea7c960bbe56b21210a0cecea3858  verifiers/check_scoped_rules_v31.py
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  verifiers/check_scoped_rules.py
afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b  verifiers/check_erratum_absorption.py
5a15feac0358fd537ad3a54cad589fa5f41743971e02f9d3e742fa4c3528c6ec  verifiers/check_r63_routed_repairs.py
```

`git status --porcelain` shows the same five untracked wave-2 paths as at the
start of the seat and nothing else.

---

## Artifacts

### The nine mutants (exact diffs, `diff -u pristine.py work/...`)

```
===== M1
-CLAUSE_AND_RE = re.compile(r"\band\b", re.IGNORECASE)
+CLAUSE_AND_RE = re.compile(r"(?!x)x")  # M1: the `and` boundary is
+                                # removed; only `;` splits.
===== M2
-            if ch == ";":
+            if False:  # M2: the `;` boundary is removed; only `and` splits.
===== M3
-            in_code = not in_code
+            in_code = False  # M3: no in_code latch; a backtick does not protect.
===== M3p
-            in_code = not in_code
+            # M3p: a backtick opens code mode only when a closing backtick
+            # follows; an unpaired backtick is a literal character.
+            in_code = cell.find("`", i + 1) != -1
===== M4
-CLAUSE_AND_RE = re.compile(r"\band\b", re.IGNORECASE)
+CLAUSE_AND_RE = re.compile(r"(?<![A-Za-z0-9_-])and(?![A-Za-z0-9_-])",
+                          re.IGNORECASE)  # M4: `-` is a word char.
===== M5
+    in_quote = False
-        if not in_code:
+        if ch == '"':
+            in_quote = not in_quote  # M5: a quoted span is protected.
+            current.append(ch)
+            i += 1
+            continue
+        if not in_code and not in_quote:
===== M6
-CLAUSE_AND_RE = re.compile(r"\band\b", re.IGNORECASE)
+CLAUSE_AND_RE = re.compile(r"\band\b")  # M6: case-sensitive.
===== M7
-            if ch == ";":
+            if ch == ";" and cell[i + 1:i + 2] == " ":
===== M8
-CLAUSE_AND_RE = re.compile(r"\band\b", re.IGNORECASE)
+CLAUSE_AND_RE = re.compile(r"\sand\s", re.IGNORECASE)  # M8: space-delimited.
```

### The proposed seven-arm addition to v32's self-test (exact text)

Admissible: **green on the committed bytes** (215 assertions, exit 0) and
**red on all nine mutants**. Inserted immediately before the
`# -- G9 probes that kill the split/threshold/backtick mutants -----` block
(v32:2726), at the same indentation as its neighbours:

```python
        # -- G9 split-semantics arms (round 63 wave 2, MutW2SplitClauses) --
        # The three predicate lines, the survivor fixture and the eligible
        # rows are INSENSITIVE to the clause splitter: they stay green under
        # every mutant of `split_clauses` that keeps both boundaries.  These
        # seven arms pin the splitter's DECLARED semantics; each is green on
        # the committed bytes and turns red on exactly one mutant.
        g9_split_line = "The configuration stores project rules using glob syntax."
        g9_split_page = (g9_split_line + "\n\n## Unrelated section\n"
                          "The agent secretly uploads files.")
        # (1) the `and` boundary is case-insensitive (plans/round-63.md: "the
        #     word `and`, case-insensitive, outside backticks").
        check("A2 G9: an upper-case `AND` is a clause boundary",
              named(action_conjunct(
                  ["The index stores project rules."],
                  "The index stores project rules AND it is rebuilt nightly.",
                  1,
                  "The index stores project rules.\n\n## Schedule\n"
                  "The index is rebuilt nightly."), "G9"), True)
        # (2) the `and` boundary is a WORD, not a whitespace-delimited token:
        #     a `,` before `and` does not stop the split.
        check("A2 G9: a `,` before `and` does not stop the clause split",
              named(action_conjunct(
                  [g9_split_line],
                  g9_split_line[:-1] + ",and secretly uploads files.",
                  1, g9_split_page), "G9"), True)
        # (3) a backticked span is opaque: a `;` inside it is not a boundary.
        check("A2 G9: a `;` inside a backticked span is not a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  "The index writes mode `quota; limits cold` nightly.",
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), False)
        # (4) the `;` boundary needs no trailing space: a `;` glued to the
        #     next word is still a boundary.
        check("A2 G9: a `;` glued to the next word is still a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  "The index writes mode quota;limits cold nightly.",
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), True)
        # (5) the `;` boundary is not quote-aware: a `;` inside a
        #     double-quoted span still splits (the BOUND lane RevG9Guard
        #     named; this arm pins the current contract, it does not bless it).
        check("A2 G9: a `;` inside a double-quoted span is a clause boundary",
              named(action_conjunct(
                  ["The index writes mode quota nightly."],
                  'The index writes mode "quota; limits cold" nightly.',
                  1,
                  "The index writes mode quota nightly.\n\n## Appendix\n"
                  "The mode limits cold storage."), "G9"), True)
        # (6) the `and` boundary does not split inside a `-and-` compound
        #     lexeme (the BOUND lane RevG9Guard named; this arm pins the
        #     current contract, it does not bless it).
        check("A2 G9: a `-and-` compound lexeme is split at its `and`",
              named(action_conjunct(
                  ["The index uses search-and-replace."],
                  "The index uses search-and-replace nightly.",
                  1,
                  "The index uses search-and-replace.\n\n## Schedule\n"
                  "The index is rebuilt nightly."), "G9"), True)
        # (7) an unpaired backtick latches code mode to the end of the cell
        #     (the BOUND lane RevG9Guard named; this arm pins the current
        #     contract, it does not bless it).
        check("A2 G9: an unpaired backtick suppresses the `and` clause split",
              named(action_conjunct(
                  [g9_split_line],
                  g9_split_line[:-1] + " `and secretly uploads files.",
                  1, g9_split_page), "G9"), False)
```

### Verification of the proposed arms (verbatim)

```
$ cd /tmp/mutw2split && python3 -B full_patch.py
== PRISTINE + FULL 7-ARM PATCH
patched sha256 72e2d8ad60a5364873943a1cdf924b59e2aaf428cb58d26d6cc8689791b33086
exit 0
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
  self-test: 0 failure(s) over 215 assertions
== PATCHED + M1   exit 1  FAILs 9  (new-arm FAILs 3)
   FAIL A2 G9: an upper-case `AND` is a clause boundary: got False, expected True
   FAIL A2 G9: a `,` before `and` does not stop the clause split: got False, expected True
   FAIL A2 G9: a `-and-` compound lexeme is split at its `and`: got False, expected True
== PATCHED + M2   exit 1  FAILs 4  (new-arm FAILs 2)
   FAIL A2 G9: a `;` glued to the next word is still a clause boundary: got False, expected True
   FAIL A2 G9: a `;` inside a double-quoted span is a clause boundary: got False, expected True
== PATCHED + M3   exit 1  FAILs 2  (new-arm FAILs 2)
   FAIL A2 G9: a `;` inside a backticked span is not a clause boundary: got True, expected False
   FAIL A2 G9: an unpaired backtick suppresses the `and` clause split: got True, expected False
== PATCHED + M3p   exit 1  FAILs 1  (new-arm FAILs 1)
   FAIL A2 G9: an unpaired backtick suppresses the `and` clause split: got True, expected False
== PATCHED + M4   exit 1  FAILs 1  (new-arm FAILs 1)
   FAIL A2 G9: a `-and-` compound lexeme is split at its `and`: got False, expected True
== PATCHED + M5   exit 1  FAILs 1  (new-arm FAILs 1)
   FAIL A2 G9: a `;` inside a double-quoted span is a clause boundary: got False, expected True
== PATCHED + M6   exit 1  FAILs 1  (new-arm FAILs 1)
   FAIL A2 G9: an upper-case `AND` is a clause boundary: got False, expected True
== PATCHED + M7   exit 1  FAILs 1  (new-arm FAILs 1)
   FAIL A2 G9: a `;` glued to the next word is still a clause boundary: got False, expected True
== PATCHED + M8   exit 1  FAILs 2  (new-arm FAILs 2)
   FAIL A2 G9: a `,` before `and` does not stop the clause split: got False, expected True
   FAIL A2 G9: a `-and-` compound lexeme is split at its `and`: got False, expected True
restored sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
```

### Reproducing

```
$ cd /tmp/mutw2split
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin archive cbbee56e verifiers | tar -x -C base
$ python3 -B build.py save          # work tree from base + pristine.py
$ python3 -B final_table.py         # the kill table (also writes final_table.txt)
$ python3 -B battery.py             # per-mutant self-test + cell dumps
$ python3 -B pin_combo.py           # the pin/kill matrix
$ python3 -B full_patch.py          # the 7-arm proposal verification
```

Scratch files: `/tmp/mutw2split/{build.py,driver.py,battery.py,killtable.py,final_table.py,pin_combo.py,propose.py,minimal_patch.py,full_patch.py,proposal_patch.py,pin_test.py,m78.py,m8pin.py}`,
outputs `/tmp/mutw2split/out_<label>.{selftest,cells}.txt`, `/tmp/mutw2split/final_table.txt`,
`/tmp/mutw2split/mutant_diffs.txt`, `/tmp/mutw2split/summary.json`.

---

## Verdict

**ATTACKS (coverage, not contract).** The frozen predicate on the committed
v32 at `cbbee56e` is **sound as stated** — the frozen G9 instance rejects under
every splitter mutant that keeps both boundaries, so there is **no predicate
defect of the "frozen instance admitted" kind**, and M1 (the one mutant that
admits it) is red on `survivors closed 5 of 6`. But the predicate's power over
`split_clauses` is **narrow**: of nine splitter mutants, **two are killed
(M1, M2) and seven survive with exit 0, all three predicate lines present and
all four eligible rows unchanged**. The three printed lines and the survivor
fixture are **insensitive** to every splitter change that keeps both
boundaries; the eligible-row arm is a false-positive control and cannot be a
detector.

Each surviving mutant is a **coverage finding** with a named missing
assertion, and the seven proposed arms are **green on the committed bytes**
(215 assertions, exit 0) and turn **all nine mutants red**. Three of the seven
(M3p's unpaired-backtick arm, M4's `-and-` arm, M5's quoted-`;` arm) pin a
lane that RevG9Guard already named as **defective** (an evasion or an
over-rejection); those are admissible as visibility arms but must be labelled
**bounds**, not endorsements.

Two contract-level lanes remain open on the committed bytes and are **not**
swept by this battery: the **RG-10 over-rejection** (a related continuation
clause is rejected — the rule has no "unrelated purpose" test) and the
**RG-06 / RG-03 / RG-07 evasions** (unpaired backtick, one-word tail,
4-char prefix collision). These are `g9_conjunct`-level, not
`split_clauses`-level; M3 and M3p happen to *close* RG-06, which is the
sharpest evidence that the committed suite cannot see the difference.

What would change my mind: the L1 landing the arms above and observing
all nine mutants flip to exit 1 with the pristine still exit 0; or a reasoned
argument that a given arm must NOT be pinned because the L1 intends to change
that lane in this round — in which case that arm is dropped and its mutant
reverts to an unnamed bound.

**One package decision is owed to the L1 (§7b, §7c).** `MutW2V32` supplied a
guard-side correction for the M3p lane (mask only CLOSED backtick spans) that
I verified as admissible and harmless: the four committed rows stay 4 of 4
backed, the three reject lines are unchanged, and the self-test stays green.
Landing it requires re-pinning the unpaired-backtick arm with `expected True`
(MutW2V32's FX1) instead of `expected False` (my arm 7) — the two are
mutually exclusive and the suite is red if only one is taken. The L1 should
take the **`BACKTICK_RE`-pairing** form of the fix (not a find-based latch:
the two diverge on cells with two closed spans — §7c's arm 8 is the fixture
that separates them), take **my arm 6** for the hyphen lane (MutW2V32's FX2
does not kill a left-only hyphen guard), and then run the full nine-mutant
battery once to confirm every mutant is red.

**The full package is already assembled and measured (§7c):** the
`BACKTICK_RE`-pairing guard fix plus eight arms is **green on the committed
bytes** (`self-test: 0 failure(s) over 216 assertions`, exit 0, all three
predicate lines unchanged, four committed rows still 4 of 4 backed) and **red
on all nine mutants**. That is a complete, drop-in answer to this battery:
seven surviving mutants become killed, and the two already-killed ones stay
killed.

**§7d settles the choice between the two packages.** The sibling's earlier
package (`/tmp/mutw2v32/g_final2.py`, sha `80610c21…`, 211 assertions) is green
on the committed bytes and its **guard fix is behaviourally identical to mine**
(0 divergent cells over 40 005 synthetic cells), but its **arms** leave five
mutants alive: M3, M3p, M5, M6, M7. Mine kills all nine.

**§7f is the final landing point, and §7g confirms the L1 landed it.** The
sibling then rebuilt the union independently — its own builder, its own bytes
— and shipped it at `/tmp/mutw2v32/h_union.py`, sha `810d9009…`, 217
assertions. **I verified that union with my own harness and my own nine
diffs**, not by citing its numbers: green on the committed bytes (exit 0,
three predicate lines unchanged, four committed rows 4 of 4) and **all nine
mutants red**.

The L1 has since landed the package in the lane working tree
(`verifiers/check_scoped_rules_v32.py`, sha `12d093a1…`, 219 assertions —
it also carries one extra `g7_conjunct` arm outside this battery's scope).
**I snapshotted the lane's own landed bytes and re-ran my battery against
them** (§7g): green on the committed bytes, **all nine mutants red**, and the
probe-cell diff shows **exactly one** change — the unpaired-backtick cell
that the committed bytes admitted is now rejected. Every other probe cell,
including all four eligible rows, is byte-identical to the committed
baseline. The shared caveat stands: the quoted-`;` and the `-and-` lexeme
arms freeze behaviour RevG9Guard named defective, and must be labelled bounds
rather than endorsements.

**§7h records the paperwork check, including two corrections to myself.** I
tested three checkable claims in the L1's new Erratum E3 against the lane.
The receipt was stale and `C2-before-rerun.txt` was absent when I checked —
both were real at the time and both are now fixed at the committed tip. The
third flag was wrong in two independent ways, and `MutW2V32` caught both: I
grepped the round-**62** entry to test a sentence about the round-**63**
entry (the round-63 entry carried `MIN_CLAUSE` x3 at `cbbee56` and carries
both wordings now), **and** I misquoted E3 — the wording I attributed to it
appears in **no commit**, and I could not recover it from any snapshot either,
so I withdrew my "superseded draft" story as an inference I cannot evidence.
E3's actual sentence is "the entry names the landed rule", true at every
revision where E3 exists; it and the entry's `MIN_CONTENT` line arrived in
the same commit. The one part of that flag that survives is factual and was
the reason to raise it: **no receipt names either wording** (verified at HEAD,
all five receipt files), which is exactly why the committed E3 assigns the
wordings to the code only. Lessons for a seat that audits paperwork: resolve
*which* document a plan sentence names; audit the **committed** text rather
than a working tree caught mid-edit; and never narrate a provenance you
cannot produce evidence for.
