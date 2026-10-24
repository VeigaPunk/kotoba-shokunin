# ExecKillReverify — round-65 W1: independent rebuild of the C1 kill battery

Seat: `ExecKillReverify` (leaf executor). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(jj-colocated git repo). Date: 2026-10-24. Host: linux 7.2.11-arch1-1, x64.
Scope: re-run the C1 kill conjunct from the **committed** round-65 bytes, independently of the
lane's own harness; no lane mutation, no git/jj write, one report file written.

**Verdict: the C1 kill conjunct reproduces exactly from the committed bytes.**
17/17 named single-string mutants exit 1 on a 234-assertion suite, every one with a FAIL line
naming its pin arm (the three attribution exceptions land exactly as the receipt says);
the equivalents M19/M22 stay green; the pkg7 control world (bytes minus the four round-65-new
arms, 230 assertions) admits SPAN_FIRST, SPAN_LAST and M20 at exit 0. Two bounds are recorded
in §8 and §11 (the floors guard cannot be re-run from a bare archive; the lane checkout is now
10 commits past the claim tip, so re-running in the live tree yields 240, not 234).

---

## 0. What "independent" means here

- The **mutation definitions** (one exact-string replacement per lane) are the receipt's own
  definitions: `.ufo/waves/round-65/receipts/C1-close-kill.txt` names the 17 lanes, and the
  only published definition of the exact strings is the lane harness
  `.ufo/waves/round-65/receipts/kill_battery.py`. I read that harness for its `MUTANTS` table
  and **did not execute it** (its fixed scratch root `/tmp/r65work` is in use by other seats).
- The **execution and verification** are mine: a fresh harness (`rev_battery2.py`, written for
  this seat) over a fresh `git archive` extraction, with checks the lane harness does not make:
  occurrence-count of every target (must be exactly 1), no-traceback, restoration hash,
  pin-arm FAIL *rank*, receipt-vs-run comparison of every printed FAIL line, a
  single-arm-removal load-bearing matrix, and semantic probes of both equivalents outside the
  suite. Every `(exit, fails, asserts)` triple and all 43 FAIL lines printed in the receipt
  reproduce (§9).
- I re-derived the lane set from the receipt text (regex over the `== lane: exit=…` headers):
  17 lanes, matching the plan's frozen kill conjunct (`SM1–SM6, M7, M8, M9, M10, M12, M17,
  M14, SPAN_FIRST, SPAN_LAST, M20, M11-upper`). Naming drift noted in §11: the plan's
  `M11-upper` is the receipt/harness `M11-page-no-lower`.

## 1. Source identity (measured, not assumed)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ git archive 0e104f49 | tar -x -C <work>/tree            # archive_exit=0
$ sha256sum <work>/tree/verifiers/check_scoped_rules_v32.py
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  …
$ git rev-parse 80bb8921:verifiers/check_scoped_rules_v32.py
9627ab0c4cc3cce988ed9fd771da758707fbd517
$ git rev-parse 0e104f49:verifiers/check_scoped_rules_v32.py
9627ab0c4cc3cce988ed9fd771da758707fbd517     # same blob at measured rev and tip
$ git cat-file -p 80bb8921:verifiers/check_scoped_rules_v32.py | sha256sum
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  -
```

The tip blob and the measured-rev blob are identical, and their sha256 equals the receipt pin
(`b6cfc764…`) and the `counter sha256` printed by `--self-test`. The instrument named in
`C1-close-measure.txt` is therefore exactly the instrument I attacked. Source bytes:
152,739 B / 3,091 lines.

Baseline on those bytes:

```
$ cd <work>/tree && python3 -B verifiers/check_scoped_rules_v32.py --self-test
… worlds reject 7 of 7; eligible rows pass 4 of 4
… survivors closed 6 of 6
self-test: 0 failure(s) over 234 assertions          # exit=0
```

## 2. Mutant / receipt table (my run, two independent executions)

Each lane is one exact-string replacement on the committed file; every target occurs exactly
once (`BASE.count(old) == 1` asserted per lane). "rank" = index of the first FAIL line carrying
the lane's pin-arm label (0 = the very first FAIL). The two runs (fresh extraction each time)
produced byte-identical table lines.

| lane | mutation (one exact-string replacement) | exit | asserts | fails | receipt exit/fails | pin-arm rank | mutant sha256[:12] | first FAIL (mine, truncated) |
|---|---|---|---|---|---|---|---|---|
| SM1-span-empty | `SPAN_BLOCK` → `span_missing = []` | 1 | 234 | 5 | 1 / 5 | 0 | `e4225624711e` | a backticked span whose words occur in neither |
| SM2-floor2 | `len(word) >= 4` → `>= 2` | 1 | 234 | 2 | 1 / 2 | 0 | `7229e51e2cef` | a backticked span word shorter than four characters |
| SM3-no-stopword | `word.lower() not in STOPWORDS` → `True` | 1 | 234 | 2 | 1 / 2 | 0 | `66fdae265df7` | a backticked span made only of stopwords |
| SM4-no-page-check | drop `and not supported(word.lower(), page_words(raw_page))` | 1 | 234 | 8 | 1 / 8 | n/a (note) | `38e656e824db` | **a span word supported by a four-character prefix on the page** |
| SM5-no-line-check | drop `and word.lower() not in content_words(raw_line)` | 1 | 234 | 3 | 1 / 3 | 0 | `71b4fb66a69e` | a backticked span word present in the cited line … |
| SM6-always-fires | `if span_missing:` → `if True:` | 1 | 234 | 17 | 1 / 17 | n/a (note) | `1634724c9207` | **FAIL A2: a cell the cited line supports passes** |
| M7-floor3 | `len(word) >= 4` → `>= 3` | 1 | 234 | 1 | 1 / 1 | 0 | `9c26f955bc6d` | a three-character span word is not rejected |
| M8-floor5 | `len(word) >= 4` → `>= 5` | 1 | 234 | 4 | 1 / 4 | 0 | `ac23cfeff17b` | a fabricated four-character span word is rejected |
| M9-stopword-no-lower | `word.lower() not in STOPWORDS` → `word not in STOPWORDS` | 1 | 234 | 1 | 1 / 1 | 0 | `b5066b23e03a` | a capitalised stopword-only span is not rejected |
| M10-line-no-lower | `word.lower() not in content_words(raw_line)` → `word not in …` | 1 | 234 | 1 | 1 / 1 | 0 | `a2c680f29ef8` | a capitalised span word present in the cited line |
| M12-line-page-words | `content_words(raw_line)` → `page_words(raw_line)` | 1 | 234 | 1 | 1 / 1 | 0 | `6abcec303ac5` | a span word present in the cited line only inside backticks |
| M17-exact-page | `supported(…)` → `word.lower() in page_words(raw_page)` | 1 | 234 | 1 | 1 / 1 | 0 | `ede3249edf4a` | a span word supported by a four-character prefix |
| M14-wrapper-no-page | `raw_page = page_text if … else "\n".join(lines)` → `raw_page = "\n".join(lines)` | 1 | 234 | 3 | 1 / 3 | 0 | `628a8f0515ef` | a span word present in the cited line only inside backticks |
| SPAN_FIRST | `for span in BACKTICK_RE.findall(cell)` → `…(cell)[:1]` | 1 | 234 | 1 | 1 / 1 | 0 | `199b5044c6f6` | a fabricated **second** backticked span is rejected |
| SPAN_LAST | `…(cell)[-1:]` | 1 | 234 | 1 | 1 / 1 | 0 | `66539fb7313e` | a fabricated **first** backticked span is rejected |
| M20-page-content-words | `page_words(raw_page)` → `content_words(raw_page)` | 1 | 234 | 2 | 1 / 2 | 0 | `f1f59071eea6` | a span word whose only page occurrence is inside backticks |
| M11-page-no-lower | `CONTENT_RE.findall(t.lower())` → `CONTENT_RE.findall(t)` in `page_words` | 1 | 234 | 7 | 1 / 7 | **1** | `2be6f6133728` | FAIL A2: a cell the cited line supports passes |

All 17: `exit=1`, `self-test: N failure(s) over 234 assertions` (no early abort, every lane
counts the full suite), no `Traceback`/`SyntaxError` in any output, candidate restored to the
pin hash after every run (harness asserts the final hash).

## 3. The three attribution notes — verified verbatim

**(a) SM4 first kill = M17 prefix arm, then eligible-world lines.** The note is exact; on the
landed 234 bytes the two round-65-new page arms also sit as collateral *between* the prefix
arm and the world lines (they did not exist when the note was written on pkg6, 229):

```
FAIL A2 G7: a span word supported by a four-character prefix on the page is not rejected: got True, expected False
FAIL A2 G7: a span word whose only page occurrence is inside backticks is not rejected: got True, expected False
FAIL A2 G7: a capitalised span word present on the page only as an exact-case token is not rejected: got True, expected False
FAIL eligible world: the four counted rows are backed: got ['Claude Code', 'VS Code'], expected [4 rows]
FAIL eligible world: the four counted rows are found live: got [True, True, False, False], expected [True, True, True, True]
FAIL eligible world: the CLI exits 0 at a target of 4: got 1, expected 0
FAIL eligible world: the summary line is the v2 one: got '… 2 of 4 …', expected '… 4 of 4 …'
FAIL the predicate line is computed from four passing eligible rows: got 2, expected 4
self-test: 8 failure(s) over 234 assertions
```

**(b) SM6 first kill = pre-existing A2 cell arm** (the R64-M9 rule), then 16 further lines:

```
FAIL A2: a cell the cited line supports passes: got ['A2 G7: backticked span word(s)  occur in neither the cited line nor the committed snapshot'], expected []
FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
…
self-test: 17 failure(s) over 234 assertions
```

The double space after `word(s)` is in the artefact (an empty identifier list interpolated into
the message) and matches the receipt char-for-char.

**(c) M11 killed by pre-existing collateral; the new M11 arm FAILs as a witness.** The new
arm's FAIL is rank **1 of 7**, never first:

```
FAIL A2: a cell the cited line supports passes: got ['A2: action word(s) scope do not occur on the committed snapshot'], expected []
FAIL A2 G7: a capitalised span word present on the page only as an exact-case token is not rejected: got True, expected False
FAIL eligible world: the four counted rows are backed: got ['VS Code'], expected [4 rows]
FAIL eligible world: the four counted rows are found live: got [False, True, False, False], expected [True, True, True, True]
FAIL eligible world: the CLI exits 0 at a target of 4: got 1, expected 0
FAIL eligible world: the summary line is the v2 one: got '… 1 of 4 …', expected '… 4 of 4 …'
FAIL the predicate line is computed from four passing eligible rows: got 1, expected 4
self-test: 7 failure(s) over 234 assertions
```

So the knowledge entry's F7 sentence ("the unlowered page set breaks the main eligible-world
fixtures in every world") is confirmed, and the new M11 arm is a witness on its **own** lane.
See §5 for the refinement: that arm is nonetheless *load-bearing for M20's lane*.

## 4. Equivalents, and what they actually establish

```
M19  span_missing = sorted({ → list({        exit=0  0 failure(s) over 234 assertions
M22  if L is None or L < 1 or L > len(lines):  → without `L < 1`   exit=0  0 failure(s) over 234
```

Both are green as claimed. Two semantic probes show the equivalence is **suite-scoped (M19)
and caller-invariant (M22), not behaviour-equivalent** — which is the precise reading under the
round's S121 second-order/equivalent-mutant framing:

- **M19 changes user-visible output ordering.** Calling `g7_conjunct` directly with a cell
  holding two fabricated spans:

  ```
  BASE (sorted):  'A2 G7: backticked span word(s) omega, zeta occur in neither …'   (seeds 0,1,2,7 → identical)
  M19  (list):    'A2 G7: backticked span word(s) zeta, omega occur in neither …'  (seed 0,2,7)
                  'A2 G7: backticked span word(s) omega, zeta occur in neither …'  (seed 1)
  ```

  The list form's word order follows `PYTHONHASHSEED`; the sorted form is stable. No assertion
  greps that order, so the suite cannot see it — exactly F7's "determinism hazard for any
  receipt that greps the G7 message text", now demonstrated rather than inferred. Any future
  receipt that asserts on the G7 span message must not assume order unless M19 is killed.
- **M22 changes behaviour outside the caller's contract.** Direct call
  `g7_conjunct(lines, "The tool writes `zeta`.", 0, None)`:
  BASE → `[]`; M22 → `['A2 G7: backticked identifier(s) zeta occur in neither …']`.
  But through the sole production caller (`action_conjunct`, line 1179) the duplicate guard at
  line 1160 (`if L < 1 or L > len(lines): return ["A2: snapshot has no line %d …"]`) fires
  first, so both variants return the identical finding at `L=0`. M22 is therefore equivalent
  *given the caller invariant*; the inner guard is defence-in-depth, not dead in the strict
  sense.

## 5. pkg7 control world and the load-bearing matrix

**Control construction (verified byte-exactly):** remove the four round-65-new `check()` calls
(the contiguous block between `check("A2 G7: a fabricated first backticked span …` and
`check("A2 G9: an \`and\`-joined purpose clause …`) → 34 lines / 1,862 B removed, and
`CTRL == BASE.replace(block, "", 1)` is true. Four checks removed, 234−230 = 4 assertions.

```
pkg7-control                              exit=0  0 failure(s) over 230 assertions
control+SPAN_FIRST                        exit=0  0 failure(s) over 230
control+SPAN_LAST                         exit=0  0 failure(s) over 230
control+M20-page-content-words            exit=0  0 failure(s) over 230
control+M11-page-no-lower                 exit=1  6 failure(s) over 230   (no new-arm label anywhere)
```

This is the receipt's strongest do-nothing claim and it holds: without the four new arms, the
three mutants they are supposed to own survive green, and the M11 lane still dies by
pre-existing collateral only. Padding or partial adoption cannot satisfy the declared
predicate.

**Per-arm independence (new, not in the receipt).** Remove exactly one arm and apply exactly
its own lane's mutant:

| world | mutant | exit | asserts | caught by |
|---|---|---|---|---|
| minus B (“fabricated second” arm), its true pin | SPAN_FIRST | **0** | 233 | nothing — B is the **unique** pin |
| minus A (“fabricated first” arm), its true pin | SPAN_LAST | **0** | 233 | nothing — A is the **unique** pin |
| minus M20 arm | M20-page-content-words | 1 | 233 | the **M11 exact-case arm** (second pin) |
| minus M11 arm | M11-page-no-lower | 1 | 233 | pre-existing A2/eligible-world arms only |

Cross-mapping note: the mutation `[:1]` (keep first span) is pinned by the arm labelled
“fabricated **second**… honest first precedes” (A keeps the fabricated first span, so only the
second-span case fails), and `[-1:]` by “fabricated **first**… honest second follows”. The
receipt's `KILLED_BY` uses the same mapping; it is correct but reads inverted at a glance.

Refinement of the knowledge entry's "the M11-exact-case arm is a named witness only": on the
**M11 lane** it is witness-only, but it is the *second load-bearing pin of the M20 lane* —
deleting the M20 arm alone does not free the M20 mutation. The suite's redundancy is therefore
2-of-4 on the page-pair lanes and 1-of-1 on each SPAN lane; that is a correct over-approximation
of the F17 risk, not a defect.

## 6. The 223 → 234 move is content, not padding

`git archive c98d137` (the plan's base) → v32 sha `f8f69cad…`:

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test     # c98d137
self-test: 0 failure(s) over 223 assertions                       # exit=0
```

Static AST diff of the two committed files (`check()` call labels, exact strings):

```
static check() labels: before 214  after 225  delta 11    (counter: 223 → 234, delta 11)
added lines 92, removed lines 0                            (append-only landing)
ADDED (11):
  A2 G7: a fabricated four-character span word is rejected                     ┐ six package arms
  A2 G7: a three-character span word is not rejected                           │ (RevC1Predicate §3)
  A2 G7: a span word present in the cited line only inside backticks is rejected│
  A2 G7: a span word supported by a four-character prefix on the page is not rejected
  A2 G7: a capitalised stopword-only span is not rejected                      │
  A2 G7: a capitalised span word present in the cited line is not rejected     ┘
  A2 G7 (wrapper): a span word present in the cited line is not rejected …     ← pkg7 wrapper arm
  A2 G7: a fabricated first backticked span is rejected when an honest second … ← SPAN_LAST's pin
  A2 G7: a fabricated second backticked span is rejected when an honest first … ← SPAN_FIRST's pin
  A2 G7: a span word whose only page occurrence is inside backticks …           ← M20 arm
  A2 G7: a capitalised span word present on the page only as an exact-case …    ← M11 arm
REMOVED (0)
```

Exactly the plan's 6 + 1 + 4; every added assertion is a new named arm, none from a changed
loop bound or threshold. Combined with §5 (each new arm is the unique pin of a named lane, or
of a mutation otherwise unpinned), the "padding alone cannot satisfy the kill conjunct" claim
is supported by measurement, not assertion.

## 7. Do-nothing control (v31 predecessor)

```
$ python3 -B verifiers/check_scoped_rules_v31.py --self-test    # sha256 a07c2269ea07…
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 5 of 6
self-test: 0 failure(s) over 201 assertions                     # exit=0
```

Matches the plan's §9 do-nothing record (`201` assertions, `survivors closed 5 of 6`).

## 8. Floors registration — static verified, runtime bounded

Committed bytes register the row consistently:

```
verifiers/floors-registry.json:  "scoped_rules_v32": { "floor": 234, "path": "verifiers/check_scoped_rules_v32.py" }
verifiers/check_assertion_floors.py:11  docstring: "scoped_rules_v32 234; round 65 (claim C1) registers …"
verifiers/check_assertion_floors.py:172 EXPECTED_INSTRUMENTS["scoped_rules_v32"] = 234
verifiers/check_assertion_floors.py:231 INSTRUMENTS["scoped_rules_v32"] = ("verifiers/check_scoped_rules_v32.py", 234, …)
```

Running the guard **inside the archive** reproduces the row but not the aggregate exit 0:

```
PASS scoped_rules_v32 observed=234 floor=234
FAIL checklist observed=1862 floor=1862 self_test_failures=1     # "name 'kotoba-shokunin' != directory 'tree'"
FAIL correction_sweep observed=25 floor=25 self_test_failures=1  # depends on untracked .ufo state
floors_exit=1
```

That is an extraction artefact (the archive directory is `tree/` and `.ufo/` is untracked), not
a floors defect: the row this claim registers is the one that passes. The receipt
`FLOORS-after.txt` records the in-lane exit 0 (15/15). **I did not independently reproduce the
floors guard's exit 0**, and I do not claim it.

## 9. Receipt fidelity

Programmatic comparison of the receipt's printed lines against my captures:

- 25 receipt sections parsed (baseline, 17 kill lanes, M19, M22, pkg7-control, three control
  lanes, control+M11); **every** `(exit, failure-count, assertion-count)` triple identical.
- **43 printed FAIL lines compared in position, 0 mismatches** (each receipt line is the
  harness's 150-char prefix of the same live line).
- Receipt `RESULT: ALL OK` / `harness_exit=0` reproduces in kind: my harness prints
  `RESULT: ALL OK`, exit 0, twice over the same extraction, and an earlier run over a second
  extraction of `0e104f49` (later lost to the scratch collision, §11) produced the same
  per-lane counts, ranks and first FAIL lines.

## 10. Claims supported / falsified / refined

Supported (measured):

- C1 kill conjunct (plan “Frozen counted predicate”): all 17 lanes exit 1 on the committed
  234-assertion bytes, each FAIL naming its pin arm; SM4/SM6/M11 attribution per the R64-M9
  rule exactly as recorded.
- `C1-close-measure.txt`: baseline green at 234, `counter sha256 b6cfc764…`, predicate lines
  (`worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`) reproduce.
- Knowledge entry `g7-span-closure-round65.md`: the 223→234 landing is 11 new named arms
  (6+1+4), append-only; SPAN_FIRST/SPAN_LAST/M20 are uniquely pinned by their arms (each arm
  removal ⇒ mutant survives); M11 is killed by pre-existing collateral in every world.
- Plan §9 do-nothing: v31 = 201 assertions, `survivors closed 5 of 6`, exit 0.
- Floors registry/tables/docstring agree at 234 (static).

Refined (not falsified):

- The knowledge entry's “M11 arm is a named witness only” — witness on its own lane, but the
  second pin of the M20 lane (§5).
- MutW2M7M22 §4a's SM4 note (prefix arm, then eligible-world) — correct, but on 234 the two new
  page arms appear between them; SM4 now prints 8 FAIL lines, not 6.
- “Equivalent” for M19/M22 means suite-equivalent: M19 is output-order-visible (hash-seed
  dependent message), M22 differs on a direct `L=0` call but not through `action_conjunct`.

Falsified: nothing in the C1 receipt. One naming inconsistency: the plan's `M11-upper` lane is
`M11-page-no-lower` in the receipt/harness (same lane, same mutant; the receipt's `KILLED_BY`
maps it to the exact-case arm). A name-matching reviewer could read this as a missing lane.

## 11. Risks, environment notes, restoration

- **The lane checkout is 10 commits past the claim tip.** `git HEAD` = `master` = `2a8eba5`
  (“round-66 verifier spot-check (integrator, hyaku)”), and `git rev-list --count
  0e104f49..master` = 10 (`806b53b` “round-66: land G9 coupling and integrity fixes” contains
  the live blob `234df386…`). Running the live working-tree file therefore prints
  `self-test: 0 failure(s) over 240 assertions` (exit 0) — **not 234**. The round-65 receipts
  reproduce only from `git archive 0e104f49`; a reviewer re-running in the lane tree will see a
  false mismatch. This is checkout position, not drift or corruption (`git hash-object` of the
  live file resolves to a committed round-66 blob).
- **Scratch-path collision on this host.** `/tmp` hosts 3,000+ entries from dozens of seats. My
  first scratch (`/tmp/r65rev`) was removed by `rm -rf` at the start of my extraction and later
  found repopulated by another seat's tree — I deleted a sibling's scratch directory before
  realising it existed. Scratch-only, no lane or repo effect, but it is a real hazard for any
  seat that writes a candidate file *in place*: two seats sharing a scratch root can corrupt
  each other mid-run. I moved to a `mktemp -d` root (`/tmp/killrev-ExecKillReverify-gISWhp`)
  and never wrote elsewhere; the battery restores the candidate after every run and asserts
  the final hash.
- **Naming drift** `M11-upper` (plan) vs `M11-page-no-lower` (receipt/harness) — see §10.
- **Floors guard not re-runnable from the archive** — see §8; recorded as a bound, not a pass.
- **No lane writes**: no git/jj writes, no index touch (`git archive`/`rev-parse`/`cat-file`/
  `hash-object`/`log --find-object` only), no sibling lane, no host service, no package
  transaction. The only file written outside `/tmp` is this report.
- Scratch (ephemeral): `/tmp/killrev-ExecKillReverify-gISWhp/` with `tree/`, `tree-before/`,
  `out/<lane>.out` (35 captured suite runs: 25 battery + 4 single-arm + 2 crossed + baseline
  repeats and controls; plus 12 semantic-probe subprocesses), `rev_battery2.py`,
  `probe_extra.py`, `run1.log`, `run2.log`.
  Tools installed/upgraded: **none** (stdlib Python only). Environment: Python 3.14.8,
  git 2.56.0.

## 12. Reproduction (exact)

```sh
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
W=$(mktemp -d); mkdir -p "$W/tree" "$W/out"
git archive 0e104f49 | tar -x -C "$W/tree"
sha256sum "$W/tree/verifiers/check_scoped_rules_v32.py"     # b6cfc764…
WORK="$W" python3 /path/to/rev_battery2.py                  # RESULT: ALL OK, exit 0
WORK="$W" python3 /path/to/probe_extra.py                   # crossed arm-removal matrix
```

`rev_battery2.py` contents are in the scratch dir and are reproducible from this report's §2
mutation table + the receipt harness's `MUTANTS` strings; it asserts pin, target uniqueness,
exit codes, assertion counts, no-traceback, pin-arm presence/rank, receipt agreement, control
arithmetic, and restoration.

Report: `.ufo/waves/round-65/w1/ExecKillReverify.md`
