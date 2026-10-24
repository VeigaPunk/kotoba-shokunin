# RevSpotcheckCrosswalk — C2 counter ↔ r63 spot-check routed items

Round 64, wave 1 (build), hyaku run 5, 2026-10-24. Reviewer seat, independent leaf.
Read-only: no production file edited, no `git`/`jj` write, no tool installed or upgraded.
Base tip at dispatch `078eec4`; plan freeze `c04fffbeafcaf810897258d56f99cca736ed3a91`.

Axis (godspeed, named before data): **mapping exactness** (is the 4↔4 bijection real in both
directions), **computation soundness** (does each check compute the quantity it claims), and
**bound honesty** (what `4 of 4` does not cover). Cheapest moves that improve one axis without
harming another are taken; nothing here changes the frozen predicate's headline or exit codes.

**Review state.** At the time of this review `verifiers/check_r64_routed_repairs.py` does **not
exist** (`ls verifiers/*r64*` → `No such file or directory`, 00:37). Every check-level finding
below is therefore against the plan's frozen text (`plans/round-64.md` L120–145) and the committed
evidence, not against an implementation. That makes it actionable *pre-landing*, which is the
point.

## Verdict (3 sentences)

The intended mapping is sound: items 1–4 of the spot-check's routed list map onto checks 1–4 of
C2 one-to-one, on four disjoint artifacts, and no check is an orphan. But **F1** shows check 4's
frozen computation ("counting `check(` invocations … expected 23") cannot produce 23 from the
committed bytes — the static count is 20 — so as written the predicate can never print
`4 of 4` without a pre-data erratum or a hardcoded literal. **F2** shows items 5–6 have **no**
recorded non-counting bound anywhere in the C2 text, so the headline `4 of 4` is unguarded against
being read as `6 of 6`.

## Crosswalk — routed item → check, with measured evidence

| # | Routed item (`corpus/lessons/round-63-verifier-spotcheck.md`) | C2 check (`plans/round-64.md`) | Check's own artifact (disjoint) | Discriminating evidence measured this seat |
|---|---|---|---|---|
| 1 | L164–167 **uncommitted working-tree edit** `MutW2SplitClauses.md` (41+/13- vs `38defdc`; "commit or revert") | **1 `seat-edit-committed`** (L122–127) | `.ufo/waves/round-63/w2/MutW2SplitClauses.md` | marker `temporal mismatch` → worktree **1**, `38defdc` **0**, `HEAD` **0**; it is an *added* line (`+   was a **temporal mismatch** on my part.`); numstat **82/29** (see F7) |
| 2 | L168–173 **report citation imprecision**: controls cited "@ `35d44b4b`", committed at `8c4cefa` / `cbbee56`; "the M95 citation class, in the report itself" | **2 `control-revs-named`** (L128–133) | the two control blobs + an appended LOG suffix line | `git log --diff-filter=A --format=%H -1`: `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8`, `cbbee56e9a3589b0b46736ad36f1b77701def80e` — plan's expected literals **correct**; `git ls-tree -r 35d44b4b -- .ufo/waves/round-63/controls/` prints **nothing** (spot-check premise true); at `8c4cefa` it prints only `C1-do-nothing-v31.txt`; each control pins `at: 35d44b4b4dcdda…` internally |
| 3 | L174–177 **lowest-axis parenthetical**: report named calibration/consistency (10) lowest owned; SCORECARD owns depth (9) below it | **3 `lowest-axis-corrected`** (L134–139) | `SCORECARD.md` axes table + an appended LOG suffix line | `SCORECARD.md:28` `| depth | 9 | … | owned |`; `:29` `| consistency (calibration sub-axis) | 10 | … | owned |`; the five advisory rows are 8.5/8.5/8/8.5/8.0 → owned minimum **depth 9**, premise true |
| 4 | L178–180 **stale seat number**: `ExecW2E2Patch`'s table says "21 assertions"; committed counter has 23 | **4 `assertion-count-named`** (L140–145) | `verifiers/check_r63_routed_repairs.py` + `.ufo/waves/round-63/w2/ExecW2E2Patch.md` | committed counter prints `self-test: 0 failure(s) over 23 assertions`, rc 0, 561 ms; static `check(` count is **20** (F1). `ExecW2E2Patch.md:496` carries `self-test: 0 failure(s) over 21 assertions`, exit 0 — the stale cell is real |
| 5 | L181–184 **deferred item**: E3 G7 `span_missing` pinning arms land in round 64 — "recorded in `a107520` and the lesson row (t)" | **none — C1 owns it** | C1's predicate (`check_scoped_rules_v32.py --self-test`) and its receipts | `a107520` exists, subject matches; `corpus/lessons/round-63.md:96` is the `| t |` row (`deferred-to-round-64`, 223 assertions); `MutW2V32.md:911/970-974` carries SM1–SM6 and the 223-assertion landed line. Plan C1 L34–44 *and* Routed-input handling bullet 1 name it → **owner recorded, non-counting bound NOT recorded** (F2) |
| 6 | L185–187 **SHONEN for the operator**: four `[~]` boxes, promotion operator-owned, "no `[x]` written by this closure" | **none — operator-owned** | `SHONEN.md` (fleet) | `grep -n 'SHONEN\|item 5\|item 6\|items 5\|deferred\|six' plans/round-64.md` → hits only at L34/40/41 (C1 prose), **zero** SHONEN hits. Not counted (correct), **nowhere recorded** (F2) |

Mapping is **one check per item for 1–4**, and each of the four checks reads a different artifact
(`MutW2SplitClauses.md` / controls + LOG / SCORECARD + LOG / r63 counter + `ExecW2E2Patch.md`).
No check targets item 5 or 6 → **no orphan check inflating the count**: the denominator 4 is the
right denominator for "lane-side defects routed 1–4".

## Attacks on the mapping (many-to-one, one-to-many, bundling)

1. **Many-to-one (one check closing two items): none found.** Check 2 is the only candidate
   (item 2 is two facts: two committing revs). It closes one item; the base pin `35d44b4b` it also
   requires is part of item 2's remedy ("Cite the committing rev plus the pinned base"), not item
   3's. Check 4's expected 23 comes from the *same counter* that check 1's material (item 4) is
   about, but check 1 reads the seat edit, check 4 reads the counter — disjoint.
2. **One-to-many (one line satisfying three checks): real, latent.** Checks 2, 3 and 4 each
   require "an appended-suffix line of LOG.md"; nothing in the plan requires the matches to be on
   *distinct* lines. One line could read
   `controls at 8c4cefa / cbbee56 (base 35d44b4b); depth 9 is the lowest owned axis, below
   consistency 10` and satisfy checks 2 **and** 3 at once, so `4 of 4` could represent three
   corrections. The drafted block (`.ufo/waves/round-64/w1/ScribeLOGCorr.md` § A, two separate
   bullets) is distinct today, so this is a counter-hardening item, not a text defect → **F6**.
3. **Denominator inflation / deflation:** none. Items 5–6 are excluded, and no check silently
   counts an item outside 1–4 (each check's artifact is item-specific).
4. **Missing items:** the spot-check section has exactly six numbered items
   (`grep -nE '^[0-9]+\. '` → 164/168/174/178/181/185); the plan routes 1–4 plus the item-5
   pointer. Count is complete.

## Findings, by severity

### F1 — HIGH — check 4's declared computation cannot yield 23; the frozen text is unsatisfiable as written

`plans/round-64.md:140-145`: "computes the r63 C2 counter's self-test tally **by counting
`check(` invocations** … (expected 23, cross-checked against the spot-check's own count)".
Measured on the committed blob (`verifiers/check_r63_routed_repairs.py`, sha256
`b9e627371cfc5e83a5bbde2b2ab455c819cc9419eafded5c5671bf35d66ed105`, 651 lines):

```
$ grep -c 'check(' verifiers/check_r63_routed_repairs.py            → 20   (lines)
$ grep -o 'check(' verifiers/check_r63_routed_repairs.py | wc -l    → 20   (occurrences)
$ grep -n 'def check(' verifiers/check_r63_routed_repairs.py        → 427:    def check(name: str, actual: object, expected: object) -> None:
$ awk 'NR>=420 && NR<=613' … | grep -o 'check(' | wc -l             → 20   (inside self_test: 19 call sites + the closure def)
```

19 static call sites, of which two sit inside `for arm_label, mode, cand_src, cand_name in (…)`
over a **3-tuple** (lines 595, 601) → 17 + 2×3 = **23**, which is exactly the spot-check's own
derivation (`round-63-verifier-spotcheck.md:96-98`: "17 fixed `check()` calls + the counter-arms
loop (3 arms × 2 checks …) = **23**"). A static `check(` count gives **20**; no reading of "counting
`check(` invocations" gives 23 without also modelling loop multiplicity, which the plan does not
say. Consequences: implemented literally, the counter prints `0 of 4` at every rev (false red at
the target); implemented to pass, the 23 is a literal — the label-only class the r63 E2 hardening
exists to kill. This also explains a sibling deviation: `ScribeLOGCorr.md:44-45` states the counter
"reads the tally by materialising the r63 counter and running its `--self-test` (spec:
`over N assertions`, expect 23)" — a different method, silently substituted for the frozen one.

Measured fix (recommended, faithful, cheap). Materialise the blob at `<rev>` and run it; this is
the same "run the candidate as a process" discipline the r63 E2 arms already use:

```
$ git show HEAD:verifiers/check_r63_routed_repairs.py > /tmp/r63mat/verifiers/check_r63_routed_repairs.py
$ python3 -B /tmp/r63mat/verifiers/check_r63_routed_repairs.py --self-test | tail -1
self-test: 0 failure(s) over 23 assertions          # rc=0, wall_ms=509
```

The counter must then parse `over (\d+) assertions` from that stdout (the blob's `self_test()`
builds its own temp git worlds and never reads the lane's `LOG` through `LANE`, so a `/tmp`
materialisation is faithful — verified above). Fallback without execution: an `ast` count of
`check(...)` Call nodes in `self_test` (17) plus `2 × len(arm tuple)` (3 arms) — the spot-check's
own arithmetic, mechanically applied. Either way this is an **erratum E1, pre-data**, and the
erratum line must carry the static count 20 so the correction is falsifiable. Exact text in
"Deliverables" below.

### F2 — HIGH (bound honesty) — items 5 and 6 have no recorded non-counting bound

Requirement: items 5–6 must be explicitly **not counted**, with the bound recorded. Where things
stand:

- Item 5's *owner* is recorded (plan C1 L34–44 and Routed-input handling bullet 1: "G7
  span_missing pinning arms → C1 (primary material)"; `a107520`, lesson row `t`,
  `MutW2V32.md:911/970-974` all present). But **no C2 text says the counter excludes it**.
- Item 6 is recorded **nowhere**: `grep -n 'SHONEN\|item 5\|item 6\|items 5\|deferred\|six'
  plans/round-64.md` returns three hits, all C1 prose about the arms; zero for SHONEN.
- The C2 Bound (`plans/round-64.md:159-161`) reads only: "the counter binds these four routed
  defects of one spot-check; a new self-assessment mismatch class is outside it".

So the headline `4 of 4` has an unstated denominator guard: a reader (or a round-64 receipt
consumer) can read it as "all six routed items addressed". This is exactly the class the r63
counter's docstring handled by naming its bounds. Fix: the counter docstring's `Bounds` paragraph
(and the report's C2 section) must name items 5–6, their owners, and state `4 of 4` ≠ `6 of 6`.
Exact text below.

### F3 — MEDIUM — two checks hard-code one of two admissible remedies; the routing doc admits both

- Item 1 says "**commit or revert**". Check 1 credits only the commit (marker present). Plan
  pre-declares the commit path, so this is a declared narrowing — but the counter's bound must say
  that the revert branch is an admissible lane remedy that scores 0 of 4 here, or a future revert
  choice will look like an unclosed defect.
- Item 4 says "amend the seat file **or note the drift in the round-64 lesson sweep**". Check 4
  credits only the seat-file amendment. Same class.
- Secondary: check 1's marker is a single English phrase that can only ever *disappear* by a later
  rewording; there is no semantic tie to the correction, and the check cannot distinguish "the seat
  edit was committed" from "the phrase happens to survive a rewrite". Bounded, but name it.

Evidence: `MutW2SplitClauses.md` marker counts 1 / 0 / 0; the added diff line is
`+   was a **temporal mismatch** on my part.` (bold markers do not break the substring search).

### F4 — MEDIUM — check 3's table parse is positional and the real SCORECARD table contains unescaped `|`

`plans/round-64.md:134-139` says the counter "parses the axes table of SCORECARD.md". The committed
table has pipes inside evidence cells:

```
line 26 pipes=6 | line 27 pipes=6 | line 28 pipes=6 | line 29 pipes=6 | line 30 pipes=6
line 31 pipes=7 | line 32 pipes=10 | line 33 pipes=6 | line 34 pipes=15 | line 35 pipes=0
naive field[3] (the "Owned?" column): 31 → "grep -c '<skills>'` 1 → 0 (exit 1…"; 32 → "Ho"; 34 → "grep -cE '^\\"
```

Depth (9) and consistency (10) happen to parse because their rows have six pipes, so the owned
minimum comes out 9 **by luck**. A positional split must be replaced by a right-split (the
`Owned?` column is **second-from-last**: `| Axis | Score | Evidence | Owned? | Last change |`),
plus a self-test arm whose constructed table carries an embedded `|` inside an *owned* row's
evidence cell. Without it, a cosmetic SCORECARD edit turns check 3 into a false red at the tip.

### F5 — MEDIUM — token-only matchers pass the exact false statements the routed items correct

- Check 3's required tokens are `depth`, `lowest owned axis`, `9`, `10`, `consistency`. The
  **inverted** sentence — "consistency (10) is the lowest owned axis; depth 9" — contains every
  token. A correction that repeats item 3's error in swapped form would score GREEN. (The drafted
  LOG line, `ScribeLOGCorr.md:68`, is honest — "depth is the lowest owned axis, 9 below consistency
  10" — so this is a matcher defect, not a text defect.)
- Check 2's tokens admit **swapped attribution** ("`C1-do-nothing-v31.txt` committed at
  `cbbee56`, `C2-before-r62tip.txt` at `8c4cefa`"), which is the same class of wrong prose the
  M95 defect is about.

Fix: bind subject to predicate — e.g. check 3 requires `depth` within ~80 non-period characters of
`lowest`; check 2 requires each rev token on the same line as its filename. And add two self-test
worlds whose correction line is inverted / swapped and must score red. If the lane keeps
token-only matching, the r63 bound sentence ("a correction that names the right tokens with wrong
prose are outside it") must be carried verbatim into the r64 docstring — currently the plan's
bound does not say it.

### F6 — LOW/MEDIUM — checks 2/3/4 do not require distinct suffix lines (bundling)

See attack 2. Enforce distinct appended-line indices (cheap: keep the matched line numbers in a
set and require three distinct indices for the three LOG-side checks), with a constructed-world
arm whose single line carries all tokens and must fail. Today's draft uses two bullets and no LOG
line for check 4, so the honest path is unaffected.

### F7 — LOW (calibration datum) — the routing document's own item-1 measurement is unreproducible

Spot-check states `41+/13-` twice (L29 table row and L165 item 1); the plan's inherited-state
paragraph says `82+/29-`. Measured now, against a committed baseline that is provably unchanged:

```
$ git diff --numstat -- .ufo/waves/round-63/w2/MutW2SplitClauses.md      → 82  29
$ git diff --numstat 38defdc -- <path>                                   → 82  29
$ git diff -w --numstat 38defdc -- <path>                                → 82  29
$ git rev-parse HEAD:<path> vs 38defdc:<path>                            → same
$ plain diff(1) of the two blobs                                         → 79 added / 29 removed
```

No numstat variant reproduces 41/13, and the file's mtime (`00:12:59`) **precedes** the spot-check
file's (`00:20:07`), so "the worktree grew after that closure" (`.ufo/.../ScoutQualityDebt.md:154`)
is `[INFERENCE]`, not a measurement. The plan's 82/29 is the true value. C2 check 1 does not verify
the diffstat (its marker is sufficient), so this does **not** need a fifth check — but it must be
recorded, because a routing doc that misstates its own measurement is precisely the class C2
counts, and it is currently outside the count. One sentence in the round-64 LOG's inherited-state
bullet suffices ("the spot-check's 41/13 is not reproducible against `38defdc`; measured 82/29").

## Motivating-evidence verbatim check (plan C2 vs spot-check)

Plan text, `plans/round-64.md:94-97`:

```
(2) report citation imprecision — the two round-63 controls cited "@
`35d44b4b`" while `C1-do-nothing-v31.txt` was committed at `8c4cefa` and
`C2-before-r62tip.txt` at `cbbee56` (each pins base `35d44b4b` internally) —
"the M95 citation class, in the report itself";
```

Spot-check text, `corpus/lessons/round-63-verifier-spotcheck.md:168-173`:

```
2. **Report citation imprecision:** the Before→after section cites the two
   controls "@ `35d44b4b`", but `C1-do-nothing-v31.txt` was committed at
   `8c4cefa` and `C2-before-r62tip.txt` at `cbbee56` (each pins base
   `35d44b4b` internally). The cited rev does not contain the files — the
   M95 citation class, in the report itself. Cite the committing rev plus the
   pinned base.
```

```
$ grep -n 'M95 citation class' corpus/lessons/round-63-verifier-spotcheck.md
172:   M95 citation class, in the report itself. Cite the committing rev plus the
$ grep -n 'M95 citation class' plans/round-64.md
97:"the M95 citation class, in the report itself"; (3) the report's lowest-axis
$ grep -n '8c4cefa\|cbbee56\|35d44b4b' corpus/lessons/round-63-verifier-spotcheck.md
13:Round window: `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` →
27:… (`cbbee56e`; `## Adjacent` 33→35/37) …
28:… `b8531d5`, `8c4cefa`, `35d44b4b` all `merge-base --is-ancestor` of `master`
169:   controls "@ `35d44b4b`", but `C1-do-nothing-v31.txt` was committed at
170:   `8c4cefa` and `C2-before-r62tip.txt` at `cbbee56` (each pins base
171:   `35d44b4b` internally). The cited rev does not contain the files — the
```

**Result: verbatim-accurate.** The quoted fragment `the M95 citation class, in the report itself`
matches byte-for-byte (only the sentence-final period sits outside the plan's quotation marks); the
rev literals `8c4cefa` / `cbbee56` / base `35d44b4b` are the spot-check's own, and both committing
revs are **true** (`8c4cefa8e1…`, `cbbee56e9a…`). The plan changes one connective ("but" → "while")
outside quotation marks, which is a paraphrase, not a misquote. Nothing here supports a citation
defect in the plan; the M95 class in the *plan's* C2 is clean.

## Deliverables for the L1 (exact text; nothing else changed)

### D1 — erratum E1, pre-data (append inside the r64 counter's module docstring, after the "four checks" list)

```
Erratum E1 (round 64, pre-data, declared before any after-measurement; the frozen
predicate's headline `r63 routed defects closed 4 of 4` and both exit codes are
unchanged).  Check 4's tally is MATERIALISED AND EXECUTED, not counted statically:
the plan's sentence "counting `check(` invocations" cannot produce 23 from the
committed blob -- the static count is 20 occurrences (19 call sites plus the
`def check(` closure at line 427), and the runtime total is 17 fixed call sites
plus 2 call sites x the 3-arm tuple = 23.  The counter writes
`git show <rev>:verifiers/check_r63_routed_repairs.py` into a temporary
`verifiers/` directory, runs it with `--self-test` under a 120 s timeout, and
reads `over (\d+) assertions` from its stdout; a blob that exits nonzero or
prints no tally is an environment error, never a silent zero.  Measured on the
committed blob (sha256 b9e627371cfc5e83a5bbde2b2ab455c819cc9419eafded5c5671bf35d66ed105):
`self-test: 0 failure(s) over 23 assertions`, exit 0, 509-561 ms.
```

### D2 — the counter's `Bounds (declared before data)` paragraph

```
Bounds (declared before data).  The counter binds routed items 1-4 of
corpus/lessons/round-63-verifier-spotcheck.md § "Routed defects and notes for
the lane" and no others; the denominator is four because only those four are
lane-side defects requiring a correction.  Item 5 (deferred E3 G7 `span_missing`
pinning arms) is NOT counted here: it is a deliverable owned by C1 and verified
by C1's own frozen predicate (`check_scoped_rules_v32.py --self-test` printing
`self-test: 0 failure(s) over 223 assertions`), recorded in `a107520`, lesson row
(t) and MutW2V32 §11.  Item 6 (SHONEN promotion) is operator-owned and outside
every lane counter; no `[x]` is written by this closure.  `4 of 4` must not be
read as `6 of 6`.  Within items 1-4 the counter credits only the remedy the
round-64 plan declared: item 1's `revert` branch and item 4's
`note the drift in the lesson sweep` branch are admissible lane remedies that
score zero here.  Checks 2, 3 and 4 are token linkage on appended LOG suffix
lines: they prove the correction names the measured value, not that every
sentence around it is true -- a correction that names the right tokens with
wrong prose is outside the counter (carried verbatim from the r63 bound).
```

### D3 — matcher specs (three lines the implementation must satisfy, each with its red arm)

1. Check 2: rev token on the **same appended line** as its filename, both directions; red arm =
   the swapped-attribution line ("C1 at `cbbee56`, C2 at `8c4cefa`").
2. Check 3: `depth` within 80 non-period characters of `lowest`, with standalone `9` and `10` and
   `consistency` on the same line; red arm = the inverted sentence ("consistency (10) is the
   lowest owned axis; depth 9").
3. Checks 2/3 LOG matches must occupy **distinct** appended line indices; red arm = one line
   carrying every token.

### D4 — SCORECARD parse rule (tested against the committed table)

Do **not** left-split. The `Owned?` column is second-from-last, and evidence cells carry raw `|`.
Tested code (run against `SCORECARD.md:26-34`; prints `owned minimum: ('depth', 9)` and classifies
all rows, including the 7/10/15-pipe rows, correctly):

```python
def owned_scores(table_text: str) -> dict[str, int]:
    scores: dict[str, int] = {}
    for line in table_text.splitlines():
        s = line.strip()
        if not s.startswith("|") or not s.endswith("|"):
            continue
        s = s[:-1]                                   # drop the trailing pipe
        owned_cell = s.rsplit("|", 2)[1].strip()      # second-from-last cell
        cells = s[1:].split("|", 2)                   # axis | score | rest
        axis, score = cells[0].strip(), cells[1].strip()
        if owned_cell != "owned":
            continue
        try:
            scores[axis] = int(score)
        except ValueError:
            raise EnvError("owned row %r has a non-integer score %r"
                           % (axis, score))           # never skip: a skip lowers the minimum
    return scores
```

A non-integer score on an **owned** row is an environment error, not a skip — skipping is how a
reformatted row silently leaves the minimum. Red arm: a constructed table with an embedded `|`
inside an *owned* row's evidence cell yields the same owned minimum (`depth 9`).

### D5 — one sentence for the LOG inherited-state bullet (F7)

```
The spot-check's `41+/13-` diffstat for the inherited seat edit is not reproducible
against `38defdc` (`git diff --numstat` = 82/29, `-w` also 82/29, plain `diff` 79/29);
this round's 82/29 is the measured value.
```

## Claims this review supports / falsifies

- **Supports** C2's *structure*: items 1–4 ↔ checks 1–4 is a genuine bijection on four disjoint
  artifacts; no orphan check; the count's denominator is correct. Supports item-2's premise
  (`35d44b4b` contains neither control), item-3's premise (owned minimum = depth 9), item-4's
  premise (the `21` cell exists at `ExecW2E2Patch.md:496`), and check 1's marker discrimination
  (1/0/0).
- **Supports** the plan's C2 motivating quotes as verbatim-accurate.
- **Falsifies** check 4's declared computation as a route to 23 (F1) — the predicate is
  unreachable as written without erratum E1.
- **Falsifies** the completeness of C2's declared bound (F2): items 5–6 are not explicitly
  excluded anywhere in the C2 text.
- **Does not touch** C1 (the four `span_missing` arms and the 223-assertion predicate are a sibling
  reviewer's beat); item 5's pointers were checked only for existence and ownership.

## Residual risk and verification gaps

- `verifiers/check_r64_routed_repairs.py` does not exist at review time; F1–F6 are text-level and
  will bind the implementation only if the L1 lands the erratum and the matcher specs. If the
  executor implements the plan's literal "counting `check(` invocations", the tip prints `0 of 4`.
- I did not execute the r64 counter (absent) or the C1 predicate (out of scope). The only
  executions were the committed r63 counter's `--self-test` (twice: in-lane and from `/tmp`
  materialisation; rc 0, 23 assertions, 561/509 ms).
- `[INFERENCE]` where labelled: the "worktree grew after closure" explanation for the 41/13 number
  is not supported by any measurement available to me (F7); the mtime ordering argues against it.
- Item 3's remedy ("fix the parenthetical wording") cannot be applied to the round-63 report from
  inside this lane (write bounds), so check 3 necessarily certifies a LOG erratum rather than the
  original sentence's repair. That is the lane's append-only convention, but it is a narrowing the
  bound should name if the L1 wants the count to mean "the report text was fixed".

## Tooling

No install or upgrade was made. All commands were repo `git` reads, `grep`, `awk`, `python3`, and
one `diff`; no `git`/`jj` write, no index mutation, no lane production file touched. The only file
written is this report.
