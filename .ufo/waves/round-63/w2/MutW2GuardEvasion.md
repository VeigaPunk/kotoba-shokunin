# MutW2GuardEvasion

role: mutation tester (leaf member; no subagent dispatch; no installs)
item: Replay RevG9Guard's nine probe cells against the **committed** v32 at
`cbbee56e` in `/tmp` with a driver that calls `action_conjunct` directly;
confirm or overturn each wave-1 verdict with verbatim output; mutate the
committed guard to test which wave-1 claims the landed instrument actually
pins.

Report path: `.ufo/waves/round-63/w2/MutW2GuardEvasion.md` (lane-relative).
Scratch: `/tmp/mutw2g9` (disposable). **No lane production file was modified**;
the only lane write is this report. Verified at close: lane
`verifiers/check_scoped_rules_v32.py` sha256 `4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`,
`git status --porcelain` shows only the L1's untracked wave-2 dispatch files
and this report directory, `HEAD` = `cbbee56e9a3589b0b46736ad36f1b77701def80e`,
jj working copy empty.

Tooling: **no tool was installed or updated** (no pacman / uv / npx / cargo
transaction; nothing to record on the update-safety channel).

---

## 0. Baseline and a provenance finding that re-scopes the whole replay

Wave-1 probed **untracked** bytes; the committed bytes are different. This is
a material finding, not a formality — three of the nine wave-1 verdicts were
overturned by the landing, and one wave-1 verdict was against a file that no
longer exists anywhere in the repository.

| bytes | sha256 | where |
|---|---|---|
| wave-1 target (`RevG9Guard.md:6`, `CriticC1Bound.md:88`, `RevClaimC1.md:7`, `MutG9Guard.md:84`) | `8371f707c571b74f6e3ec072690c771342fdd078b220c6ec3c617c6b18f21f28` | **not in git** (`git cat-file -t` → `fatal: Not a valid object name`), **not in the jj store** (714 blobs in `.jj/repo/store/extra` scanned by sha256; whole `.jj` tree scanned; `jj file show` at every rev → `e3b0c442…` (absent) / `4246069129…`) |
| committed at `cbbee56e` | `4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33` | `git ls-tree cbbee56e verifiers/check_scoped_rules_v32.py` → blob `89a176b9561af5eef36d29f9a8d6786f3af1c031` |

The difference is substantive, not cosmetic. Committed v32 changed the G9 arm
from wave-1's shape to a revised one:

* wave-1 (`8371f707`): `w = content_words(clause)`, floor `MIN_CONTENT` = 3.
* committed (`4246069129`): `w = page_words(clause)` (backticked spans
  **included**), floor `MIN_CLAUSE` = 2 (`verifiers/check_scoped_rules_v32.py:1062`,
  `:1118-1133`).

So the replay below is against bytes that are *not* the wave-1 bytes, and the
L1 had already closed some of wave-1's evasion lanes before this wave. The
committed lesson says so explicitly (`corpus/knowledge/compound-clause-citation-round63.md:71-75`:
"Clause words are counted with backticked spans included (`page_words`) …
the two-word fabrication `and uploads files` is now checked").

**Pristine committed baseline** (`/tmp/mutw2g9/tree`, extracted with
`git archive cbbee56e`, so the bytes are the commit's, not the worktree's):

```
$ cd /tmp/mutw2g9/tree && python3 -B verifiers/check_scoped_rules_v32.py --self-test
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
EXIT=0
```

Note: **208** assertions, not the 201 that wave-1 recorded
(`RevG9Guard.md`, `MutG9Guard.md` — both `201`). The L1 added the four G9
discriminating arms MutG9Guard named. Every wave-1 statement of the form
"201 assertions" is therefore stale for the committed bytes.

---

## 1. The nine probe cells, replayed (verbatim)

Driver `/tmp/mutw2g9/driver.py` imports the module **by path**
(`importlib.util.spec_from_file_location`, `sys.dont_write_bytecode = True`),
extracts the real `PAGES`/`ACTIONS`/`QUOTES` fixtures from the committed
`self_test` by AST, and calls `action_conjunct(lines, cell, 1, page)` and
`g9_conjunct(lines, cell, 1, page)` directly — no `self_test` is invoked by the
probes.

```
$ cd /tmp/mutw2g9 && python3 -B driver.py tree/verifiers/check_scoped_rules_v32.py "committed v32 @ cbbee56e"
```

| # | cell | wave-1 verdict (8371f707) | **committed verdict (4246069129)** | status |
|---|---|---|---|---|
| C01 | `…glob syntax and secretly uploads files.` (frozen instance) | REJECT `A2 G9` | **REJECT** `['A2 G9: clause "secretly uploads files." is supported outside the cited line']` | **CONFIRMED** |
| C02 | `…glob syntax and uploads files.` | ACCEPT (2-word tail) | **REJECT** `['A2 G9: clause "uploads files." is supported outside the cited line']` | **OVERTURNED** — now checked (`MIN_CLAUSE`=2, `page_words`) |
| C03 | `…glob syntax and exfiltrates.` | ACCEPT (1-word tail) | **ACCEPT** `[]` | **CONFIRMED** (see §3: structurally unclosable) |
| C04 | `…glob syntax and \`secretly uploads files\`.` | ACCEPT (backtick hides span) | **REJECT** `['A2 G9: clause "\`secretly uploads files\`." is supported outside the cited line']` | **OVERTURNED** — `page_words` counts the span |
| C05 | 8-word backticked fabrication, **page supports it** | ACCEPT (0 counted words) | **REJECT** `['A2 G9: clause "\`secretly uploads files mirror telemetry beacon remote endpoint nightly\`." is supported outside the cited line']` | **OVERTURNED** |
| C05b | same 8-word backticked fabrication, **page does not support it** | (wave-1 did not separate this case) | **ACCEPT** `[]` | **NEW RESIDUAL LANE — see §4** |
| C06 | `…glob syntax \`and secretly uploads files.` (unpaired backtick) | ACCEPT (no split) | **ACCEPT** `[]` | **CONFIRMED** (still bound) |
| C07 | `…glob syntax and stores rulerboard syntaxis nightly.` | ACCEPT (3/4 via 4-char collision) | **ACCEPT** `[]` | **CONFIRMED** (still bound) |
| C08 | `The tool runs search-and-replace across the index nightly before every scheduled weekly maintenance pass.` | REJECT (over-rejection) | **REJECT** `['A2: action cell supports 7 of its 11 content word(s) at line 1 (need >= 8)']`; `G9_ONLY` `['A2 G9: clause "-replace across the index nightly before every scheduled weekly maintenance pass." is supported outside the cited line']` | **CONFIRMED** — over-rejection persists, and the cited line now trips A2's aggregate first |
| C09 | `The tool writes mode "quota; limits cold" into its config string nightly.` | REJECT (quoted `;` splits) | **REJECT** `['A2 G9: clause "limits cold" into its config string nightly." is supported outside the cited line']` | **CONFIRMED** — mangled-fragment over-rejection persists verbatim |
| C09b | same literal in backticks | ACCEPT | **ACCEPT** `[]` | **CONFIRMED** (verdict flips on quoting style alone) |
| C10 | `The agent writes audit logs to cold storage on every run and rotates them weekly into archives.` | REJECT (no relatedness test) | **REJECT** `['A2 G9: clause "rotates them weekly into archives." is supported outside the cited line']` | **CONFIRMED** — over-rejection persists |
| C11 | `…glob syntax for android command wrappers.` | ACCEPT (`\b` holds) | **ACCEPT** `[]` | **CONFIRMED** |

Eligible rows (real `PAGES`/`ACTIONS` from the committed source), which the
frozen predicate's `eligible rows pass 4 of 4` line depends on:

```
  S900 L=5 -> []
  S901 L=4 -> []
  S902 L=4 -> []
  S903 L=4 -> []
```

**Frozen predicate: needs no change.** The frozen instance still rejects
(C01, with the identical reason string wave-1 recorded) and the four eligible
rows still pass (`[]` each; the committed self-test prints
`worlds reject 7 of 7; eligible rows pass 4 of 4`, exit 0). Every other
verdict above is a **bound lane**, recorded in §3–§4 with its evidence.

---

## 2. Mutation battery on the committed guard

Twelve one-point mutants, each built by `/tmp/mutw2g9/build.py` from a fresh
`git archive cbbee56e` tree (`/tmp/mutw2g9/mut/<name>/`), each **also** run as
an in-place cycle (`/tmp/mutw2g9/cycle.py`, `cycle2.py`) that mutates the
scratch bytes, runs the detector, **restores the saved bytes**, and re-runs the
detector. Detector = the committed `--self-test` (the frozen predicate) plus
the per-cell replay.

| mutant | change | self-test exit | `survivors closed` | C01 | C02 | C03 | C04 | C05b | verdict |
|---|---|---|---|---|---|---|---|---|---|
| pristine | — | 0 | 6 of 6 | REJECT | REJECT | ACCEPT | REJECT | ACCEPT | — |
| M1 | `MIN_CLAUSE` 2→3 | **0** | 6 of 6 | REJECT | **ACCEPT** | ACCEPT | REJECT | ACCEPT | **SURVIVED** |
| M2 | clause words counted with `content_words` (wave-1 form) | 1 | 6 of 6 | REJECT | REJECT | ACCEPT | **ACCEPT** | ACCEPT | KILLED |
| M3 | `;` split boundary removed | 1 | 6 of 6 | REJECT | REJECT | ACCEPT | REJECT | ACCEPT | KILLED |
| M4 | `and` split boundary removed | 1 | **5 of 6** | **ACCEPT** | ACCEPT | ACCEPT | ACCEPT | ACCEPT | KILLED |
| M5 | G9 arm is a no-op | 1 | **5 of 6** | **ACCEPT** | ACCEPT | ACCEPT | ACCEPT | ACCEPT | KILLED |
| M6 | page gate fires on ONE page-supported word | **0** | 6 of 6 | REJECT | REJECT | ACCEPT | REJECT | **REJECT** | **SURVIVED** |
| M7 | cited-line gate needs only ONE shared word | 1 | 6 of 6 | REJECT | REJECT | ACCEPT | REJECT | ACCEPT | KILLED |
| M8 | `MIN_CLAUSE` 2→1 | **0** | 6 of 6 | REJECT | REJECT | **ACCEPT** | REJECT | ACCEPT | **SURVIVED** (no-op) |
| M9 | clause need floor removed (line gate) | **0** | 6 of 6 | REJECT | REJECT | **ACCEPT** | REJECT | ACCEPT | **SURVIVED** |
| M10 | M9 + `MIN_CLAUSE`=1 | **0** | 6 of 6 | REJECT | REJECT | **ACCEPT** | REJECT | ACCEPT | **SURVIVED** |
| M11 | M9 + `MIN_CLAUSE`=1 + page-gate floor 1 | **0** | 6 of 6 | REJECT | REJECT | **REJECT** | REJECT | ACCEPT | **SURVIVED** |
| M12 | wave-1 MutG9Guard's M6 form: G9 skips backticked cells | 1 | 6 of 6 | REJECT | REJECT | ACCEPT | REJECT | ACCEPT | KILLED |

Hashes and restoration evidence (in-place cycle, `/tmp/mutw2g9/cycle.py`):

```
MUTANT M1_MIN_CLAUSE_3
  before sha256 : 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
  mutated sha256: 89bfde1f4e8aeffede573c0991253e0a51fbd15acb40f06ac433d8d7d054090f
  detector: self-test exit 0
  after sha256  : 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
  bytes identical to before: True
VERDICT M1_MIN_CLAUSE_3: SURVIVED (self-test exit 0 on mutant, 0 on restored)
```

(the same before/mutated/after triple was produced for M2–M12; every
`after sha256` equals the `before sha256` above and every restored run
re-printed `self-test: 0 failure(s) over 208 assertions`, exit 0 — see
`/tmp/mutw2g9/out_cycles.txt` and `/tmp/mutw2g9/out_mutants.txt`).

### What the battery proves

1. **Wave-1's three surviving mutants are now dead.** Wave-1's `MutG9Guard.md`
   reported M2 (`;`-only split), M3 (threshold 1) and M6 (backtick skip) as
   surviving the whole suite. On the committed bytes their counterparts are
   **M4 (killed, `survivors closed 5 of 6`), M7 (killed) and M12 (killed)**.
   The L1's four added G9 assertions did what MutG9Guard asked. **Wave-1's
   "three mutants survive the whole 201-assertion suite" finding is stale and
   must not be carried into the round-63 report.**
2. **Four mutants still survive the committed 208-assertion suite**: M1, M6,
   M8/M9/M10 (all three equivalent in effect — the one-word lane is not
   closable by lowering `MIN_CLAUSE` or the clause need floor alone) and M11.
   M11 is the important one: it **closes the one-word lane** (C03 flips
   ACCEPT→REJECT) and the committed self-test **still prints all three
   predicate lines and exits 0**. The suite does not distinguish the shipped
   guard from a stricter one, so the shipped guard's one-word exemption is
   **unpinned**.
3. **M6 is a genuine over-rejection mutant the suite does not see.** It makes
   the page gate fire on one page-supported word; C05b flips ACCEPT→REJECT,
   i.e. G9 would report a clause that is *absent* from the page — exactly the
   double-report the plan says G9 cannot do — and the committed self-test is
   green. **The "G9 never double-reports" scope claim is unpinned.**
4. **M1 is an under-rejection mutant the suite does not see.** It restores
   wave-1's `MIN_CONTENT`-3 floor; C02 flips REJECT→ACCEPT, re-opening the
   two-word fabrication lane that the committed lesson claims is closed
   (`compound-clause-citation-round63.md:73-75`). The committed self-test
   asserts `"A2 G9: a backticked fabrication is counted and rejected"` and a
   3-word "one shared word" arm, but **no assertion pins the two-word
   clause**.

### The proposed added assertions (measured, not asserted)

Two named assertions, inserted after the committed backtick arm in
`self_test` (the `g9_line` / `g9_page` locals are in scope there), kill the
two surviving behavioural mutants:

```python
        # --- MutW2GuardEvasion (round 63, wave 2): named assertions
        # pinning the G9 clause-content floor and the page-scope gate.
        check("A2 G9: a TWO-word off-citation clause is rejected",
              named(action_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and uploads files. (S900 :1)",
                  1, g9_page), "G9"), True)
        check("A2 G9: a clause absent from the page is NOT reported by G9",
              g9_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and `secretly exfiltrates telemetry "
                  "beacons nightly`. (S900 :1)",
                  1, g9_page), [])
```

Measured (`/tmp/mutw2g9/check_assertions.py`):

```
pristine+assertions sha256 = 0795faa26b3944d2ba4cdcc63be0c0d57a744e5b0550d74097f85121e2b6d4e1
  pristine+assertions: self-test exit 0
    | survivors closed 6 of 6
    | self-test: 0 failure(s) over 210 assertions
M1_MIN_CLAUSE_3 + assertions: self-test exit 1  -> KILLED
M6_page_gate_one_word + assertions: self-test exit 1  -> KILLED
M8_MIN_CLAUSE_1 + assertions: self-test exit 0  -> STILL SURVIVES
M11_both_gates_floor_1 + assertions: self-test exit 0  -> STILL SURVIVES
```

A third assertion pins the **declared** one-word exemption and kills M11
(`/tmp/mutw2g9/check_assertions3.py`):

```python
        check("A2 G9: a ONE-word clause is exempt (declared bound)",
              g9_conjunct(
                  [g9_line],
                  g9_line[:-1] + " and exfiltrates. (S900 :1)",
                  1, g9_page), [])
```

```
pristine+assertion3 sha256 = 14ab8733c441293537f10aa867c21a8d1060c6b9a509ab90ee27ca59f9d48ce0
  pristine+assertion3: exit 0
    | survivors closed 6 of 6
    | self-test: 0 failure(s) over 209 assertions
M11_both_gates_floor_1 + assertion3: exit 1 -> KILLED
```

With all three, M1, M6 and M11 are all killed and the pristine bytes stay
green. These are **missing-assertion findings, not contract changes**: the
contract's `6 of 6` / `4 of 4` holds throughout, and the three added
assertions change no production behaviour.

---

## 3. Bound lanes (recorded, not fixed)

**B1 — the one-word tail lane (C03) is structurally unclosable, not merely
unpinned.** With `MIN_CLAUSE` = 2 the clause `exfiltrates.` is skipped
outright. Lowering the floor does not help, because `fwd_need(1)` is floored
by `MIN_SHARED` = 2:

```
$ python3 -B probe2.py tree/verifiers/check_scoped_rules_v32.py
L3  one-word clause: closable at ANY MIN_CLAUSE?
  clause words: ['exfiltrates'] (len 1)
  fwd_need(1) = 2  (MIN_SHARED floor = 2)
  covered by page = 1 ; the page gate needs >= 2 -> UNSATISFIABLE (a 1-word clause can never cover 2)
  ACTION (MIN_CLAUSE=2, page supports 'exfiltrates'): []
```

M8/M9/M10 confirm this empirically (C03 stays ACCEPT under every one-floor
change). Only M11 — lowering **both** gates' floors to 1 — flips C03 to
REJECT, and it does so with the committed self-test still green. **Smallest
safe correction: none to the contract.** Record as a named bound in the
lesson's `## Limits` and pin it with the third assertion above; do **not**
lower `MIN_SHARED` (that constant is A2's own forward-fraction floor and is
asserted at `verifiers/check_scoped_rules_v32.py:2063-2066`).

**B2 — the `and`-boundary split is over-eager on hyphenated lexemes (C08)**
and **B3 — it is quote-blind on `;` (C09)**, and **B4 — G9 has no
relatedness test, so a legitimate continuation is rejected (C10)**. All three
persist verbatim on the committed bytes (see the §1 table). These are
wave-1's lanes 3, 5 and 7 and the L1's committed lesson already names them
(`compound-clause-citation-round63.md:77-82`). **No correction proposed**: the
committed lesson's wording ("Other joiners … are still not modelled") already
bounds them honestly, and the frozen predicate does not depend on them.

**B5 — the 4-character-prefix collision (C07/C07b) is inherited from A2's
`supported()`, not G9-specific.** Committed `supported()` is
`w == word or w.startswith(word[:4])` (`verifiers/check_scoped_rules_v32.py:1035-1039`),
so `rulerboard`→`rules` and `syntaxis`→`syntax` count as support. C07/C07b
remain ACCEPT on the committed bytes. Wave-1 called this "G9 inherits A2's
weakest link"; the same is true after the landing.

**B6 — the unpaired-backtick lane (C06) persists.** An unpaired backtick
leaves `in_code` true for the rest of the cell, so the `and` never splits and
the whole cell is one clause; committed `ACTION` is `[]`. The lesson does not
name this one; it is worth one line in `## Limits`.

---

## 4. NEW residual lane — a backticked fabrication the page does not support
is admitted

This lane is **not** in wave-1's nine cells and **not** covered by the
committed self-test. It follows directly from the L1's own change (counting
backticked spans with `page_words`) interacting with the plan's page-scope
note.

The plan says (`plans/round-63.md`, §C1 "The guard (declared before data)"):
*"The rule is scoped to page-present clauses so it cannot double-report words
the A2 page-containment check already rejects."* The committed lesson repeats
it (`compound-clause-citation-round63.md:35-37`): *"A clause absent from the
page too is already reported by A2's page-containment arm, so G9 never
double-reports it."*

**That premise is false for backticked spans.** A2's page-containment arm
counts `content_words(cell)`, which **strips** backticked spans
(`verifiers/check_scoped_rules_v32.py:1008-1013`, `BACKTICK_RE.sub`). So for
a backticked clause the words are invisible to A2, while G9 declines it
precisely *because* the page does not support it — G9's own page gate
(`:1129`) requires `covered(w, page) >= fwd_need(len(w))`. The two arms
decline the same clause for opposite reasons, and nothing reports it.

Measured (`/tmp/mutw2g9/probe4.py`, verbatim):

```
L1  backticked MULTI-WORD clause, words ABSENT from the page
  cell  : 'The configuration stores project rules using glob syntax. and `exfiltrates telemetry beacons nightly`.'
  ACTION: []
  G9    : []
  verdict: ACCEPT

L2  control: same fabrication, NOT backticked, words absent from page
  cell  : 'The configuration stores project rules using glob syntax. and exfiltrates telemetry beacons nightly.'
  ACTION: ['A2: action cell supports 7 of its 11 content word(s) at line 1 (need >= 8)']
  verdict: REJECT

L3  control: same fabrication, backticked, words PRESENT on the page
  ACTION: ['A2 G9: clause "`exfiltrates telemetry beacons nightly`." is supported outside the cited line']
  verdict: REJECT

L4  control: SINGLE-token backticked identifier absent from the page
  ACTION: ['A2 G7: backticked identifier(s) exfiltrates occur in neither the cited line nor the committed snapshot']
  verdict: REJECT

L5  TWO-word backticked span, words absent from the page
  ACTION: []
  verdict: ACCEPT
```

Mechanism, term by term (`/tmp/mutw2g9/probe3.py`, `probe5.py`):

```
  clause page_words  : ['beacons', 'exfiltrates', 'nightly', 'secretly', 'telemetry']
  covered by page    : 1  ; fwd_need = 4
  cell content_words : ['configuration', 'glob', 'project', 'rules', 'stores', 'syntax', 'using']
  G7 identifier regex : []  <- a multi-word span is not an identifier
```

and the A2 page-containment arm **does** fire on the same words when they are
bare (`probe5.py`, case X):

```
  ACTION : ['A2: action word(s) buffers, entropy, quantizes do not occur on the committed snapshot']
```

So the lane is: **a multi-word backticked span whose words occur in neither
the cited line nor the page is admitted by the committed guard.** G7 catches
only *single-token* identifiers (`BACKTICKED_IDENTIFIER_RE` = `` `([A-Za-z_][A-Za-z0-9_]*)` ``,
`:405`); the multi-word span is invisible to it. This is the same class of
defect the L1 already closed for the *page-supported* case (C04/C05), one
step further out: the landing fixed "backticked fabrication whose words the
page supports" and left "backticked fabrication whose words the page does not
support" open.

**Impact on the frozen predicate: none.** C01 still rejects, the four eligible
rows still pass, `survivors closed 6 of 6` still holds, exit 0. The frozen
predicate needs no change for this lane either; the lane is a **coverage
finding about G7**, and the smallest safe correction is to extend G7 — the
arm that already owns "a backticked identifier must occur in the cited line or
the committed snapshot" — to multi-word spans.

### Smallest safe correction (exact proposed text)

In `g7_conjunct` (`verifiers/check_scoped_rules_v32.py:1046-1063`), after the
existing `missing` computation and before its `if missing:` return, and one
new return arm:

```python
    span_missing = sorted({
        word
        for span in BACKTICK_RE.findall(cell)
        for word in span.split()
        if len(word) >= 4 and word.lower() not in STOPWORDS
        and word.lower() not in content_words(raw_line)
        and not supported(word.lower(), page_words(raw_page))})
    ...
    if span_missing:
        return ["A2 G7: backticked span word(s) %s occur in neither the cited "
                "line nor the committed snapshot" % ", ".join(span_missing)]
```

Measured (`/tmp/mutw2g9/check_fixes.py`, variant A; scratch copy sha256
`5dbe79348bc4fd34a8230f601f87463209068d637b4aeb9cff042e18a8e080e1`):

```
variantA_g7_span  sha256=5dbe79348bc4fd34a8230f601f87463209068d637b4aeb9cff042e18a8e080e1
  self-test exit 0
    | worlds reject 7 of 7; eligible rows pass 4 of 4
    | survivors closed 6 of 6
    | must-fail E2e guard disabled admits e2e-negated-path-key: yes
    | must-fail G7 disabled admits e2f-backticked-event-claim: yes
    | must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
    | self-test: 0 failure(s) over 208 assertions
  frozen instance : ['A2 G9: clause "secretly uploads files." is supported outside the cited line']
  residual lane   : ['A2 G7: backticked span word(s) beacons, exfiltrates, nightly, telemetry occur in neither the cited line nor the committed snapshot']
  bare equivalent : ['A2: action cell supports 7 of its 11 content word(s) at line 1 (need >= 8)']
  eligible S900 L=5 : []
  eligible S901 L=4 : []
  eligible S902 L=4 : []
  eligible S903 L=4 : []
  real-corpus rows differing: 0
```

The real-corpus no-harm check (`/tmp/mutw2g9/check_fixes.py`, `noharm.py`) runs
the production `judge()` over the lane's committed `SKILL.md`,
`corpus/SOURCES.md`, `corpus/knowledge/scoped-rules-round60.md` and
`corpus/lessons/round-60.md` against the four committed snapshots
`.ufo/waves/round-60/snapshots/S9xx.page`, and diffs every row's reasons
between the pristine and the patched module:

```
rows: pristine=7 fixed=7
rows with differing reasons: 0
```

**An alternative placement was tested and rejected.** Extending A2's
page-containment arm instead (variant B, `A2: action word(s) … do not occur on
the committed snapshot`) also closes the lane and also leaves the real corpus
unchanged, but it **breaks the committed self-test** — it turns the G7
must-fail arm red, because the survivor's backticked identifier is then
caught by A2 rather than by G7:

```
variantB_a2_page_containment  sha256=c658a3c3c693e50e133a73cc84d29ecf6aaf2e488618c6da958318e7f1419ac8
  self-test exit 1
    | must-fail G7 disabled admits e2f-backticked-event-claim: no
    | self-test: 2 failure(s) over 208 assertions
```

Variant A (extend G7) is therefore the safe placement: it keeps the G7
must-fail arm meaningful (`yes`), keeps all three predicate lines, keeps
`208` assertions green, keeps the four eligible rows passing, and changes no
row of the real corpus.

**Text for the round-63 lesson's `## Limits`** (one sentence, to be added by
the L1):

```
- **A backticked span whose words occur in neither the cited line nor the
  page is not reported by G9.** G9 declines a clause the page does not
  support, and A2's page-containment arm cannot see it because
  `content_words` strips backticked spans; G7 reaches only single-token
  identifiers. Until G7 is extended to multi-word spans, such a clause is
  admitted (round 63, wave 2, `MutW2GuardEvasion`).
```

---

## 5. Verdict on the committed bytes

**The committed predicate stands as declared, and needs no change.**
`python3 -B verifiers/check_scoped_rules_v32.py --self-test` at
`cbbee56e9a3589b0b46736ad36f1b77701def80e` prints

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
```

and exits 0; the frozen instance still rejects with the identical reason
string; the four eligible rows still pass. Nothing in this replay falsifies
C1's frozen predicate, and I propose **no** change to it.

**But three claims must be corrected in the round report, and one new lane
must be recorded:**

1. **Wave-1's mutation finding is stale.** `MutG9Guard.md`'s "three mutants
   survive the whole 201-assertion suite" no longer holds: on the committed
   bytes the corresponding mutants are **killed** (M4 `survivors closed 5 of
   6`; M7; M12). Wave-1's `201 assertions` is also `208` now.
2. **Wave-1's per-cell ACCEPT verdicts must be re-stated against the
   committed bytes.** C02, C04 and C05 are now **REJECT**; C01, C03, C06,
   C07, C08, C09, C09b, C10, C11 stand as wave-1 recorded them. Wave-1's
   target sha `8371f707…` is **not recoverable** from git or the jj store, so
   its probes cannot be re-run byte-for-byte; they are superseded by the
   committed bytes, which this report replays.
3. **Three mutants still survive the committed 208-assertion suite** (M1, M6,
   M11-equivalents) — the two-word clause floor, the "G9 never double-reports"
   page-scope claim, and the one-word-clause exemption are **unpinned**. The
   three named assertions in §2 kill all three with the pristine bytes green.
4. **NEW bound lane** (§4): a backticked multi-word span absent from both the
   cited line and the page is admitted by the committed guard. The plan's and
   the lesson's "G9 never double-reports a page-absent clause" premise is
   false for backticked spans, because A2's page-containment arm counts
   `content_words`, which strips them. The smallest safe correction is to
   extend `g7_conjunct` to multi-word spans (exact text in §4); measured
   green on the frozen predicate, the four eligible rows, all 208 assertions
   and the real corpus (0 rows differ). Until that lands, the lesson's
   `## Limits` needs the sentence quoted in §4.

**Depth axis.** The guard is now class-level for the case the L1 targeted
(backticked and short fabrications are counted, not just the frozen string),
and the landing closed three of wave-1's six evasion lanes — real depth
progress on top of wave 1. The remaining depth gaps are the four-character
prefix collision (inherited from A2), the one-word lane (structurally
unclosable without touching A2's `MIN_SHARED` floor), the quote-blind
splitter, the missing relatedness test, and the new backticked page-absent
lane — all lexical-model limits, all nameable, none of them falsifying the
frozen predicate.

**Calibration axis.** The committed lesson's `## Limits` is honest about
C06-adjacent, C08, C09 and C10 lanes and about the four-character prefix
swap, but it (a) overstates the closure of the backticked-fabrication lane
("lane 2, closed before the report") — the closure holds only when the page
supports the span, (b) claims "G9 never double-reports" a page-absent clause,
which is false for backticked spans, and (c) does not name the unpinned
one-word exemption or the unpinned two-word floor. Three sentences in
`## Limits` plus three named assertions in the self-test would bring the
lesson and the instrument into exact agreement.

---

## Artifacts (all under `/tmp/mutw2g9`, disposable)

| file | what |
|---|---|
| `driver.py` | nine-cell replay driver (calls `action_conjunct`/`g9_conjunct` directly; AST-extracts the committed `PAGES`/`ACTIONS`) |
| `build.py` | mutant builder (12 one-point patches from a `git archive cbbee56e` tree) |
| `run_mutants.py` | runs the frozen predicate + the driver on every mutant and on the restored pristine copy |
| `cycle.py`, `cycle2.py` | in-place mutate → detect → **restore** → re-detect cycles with before/mutated/after hashes |
| `probe2.py` | one-word-lane arithmetic (`fwd_need` floor, `MIN_SHARED`) |
| `probe3.py`, `probe4.py`, `probe5.py` | the backticked page-absent lane and its controls (bare / page-present / single-token) |
| `check_assertions.py`, `check_assertions3.py` | the three proposed named assertions; which mutants they kill |
| `check_fix.py`, `check_fixes.py` | the proposed G7 extension (variant A) vs the A2 alternative (variant B), with the real-corpus no-harm diff |
| `out_committed.txt`, `out_mutants.txt`, `out_cycles.txt`, `out_probe2.txt`, `out_probe3.txt`, `out_probe4.txt`, `out_probe5.txt`, `out_assertions.txt`, `out_assertions3.txt`, `out_fixes.txt` | verbatim transcripts |

**Restoration / lane integrity.** Every in-place cycle restored the exact
bytes: `after sha256 == before sha256 ==
4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`, and every
restored run printed `self-test: 0 failure(s) over 208 assertions`, exit 0.
The lane was never mutated: `verifiers/check_scoped_rules_v32.py` is
`4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`,
`verifiers/check_scoped_rules_v31.py` is
`a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858`,
`verifiers/check_erratum_absorption.py` is
`afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b`,
`git status --porcelain` lists only the L1's untracked wave-2 dispatch files
plus this report, `HEAD` = `cbbee56e9a3589b0b46736ad36f1b77701def80e`, jj
working copy empty. No tool was installed or updated.

Report: `.ufo/waves/round-63/w2/MutW2GuardEvasion.md`
