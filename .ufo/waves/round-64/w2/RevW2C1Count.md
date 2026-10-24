# RevW2C1Count

role: reviewer (leaf member — no subagent dispatch, no lane writes)
item: re-run and independently re-derive C1's counted predicate at the measured tip
`c019919c97ab5fe98e87a7754b4449ea4e699c99`; recompute the counter sha256 against
`receipts/C1-span-measure.txt`; re-run the SM1–SM6 kill battery from the committed
bytes; flag any mismatch or unattributed kill.
date: 2026-10-24. Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(jj-colocated). Read-only: no lane/jj/git write was issued, no install performed.
Scratch `/tmp/c1r` (`git archive c019919c`), `/tmp/c1b` (`git archive 078eec4`),
`/tmp/*_lab`, `/tmp/probe*.py`.

## 0. Environment / canonical runtime

```
$ git rev-parse HEAD
b99fb79c27042e0f8a598cbbb4d81479a806b518       # "round-64: measurements"
$ git merge-base --is-ancestor c019919c… HEAD ; echo $?
0
$ git status --porcelain
 M .ufo/waves/round-64/receipts/noharm-tip.txt
?? .ufo/waves/round-64/w2/
$ sha256sum verifiers/check_scoped_rules_v32.py
f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
$ git show HEAD:verifiers/check_scoped_rules_v32.py | sha256sum
f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
```
`git diff --stat c019919c HEAD` touches no `verifiers/` path — HEAD, the working
tree and the measured tip carry **one** counter, one sha. Exactly one
`check_scoped_rules_v32*` file exists in the tree (`find . -name` ⇒ 1). Every
measurement below runs the committed bytes extracted with `git archive
c019919c` into `/tmp/c1r` (siblings under `verifiers/` present, since the
counter imports `check_erratum_absorption.py` at v32:2695); the tree runs
standalone with no lane git dependency.

[NOTE] `python3 -B … --self-test | tee file; echo EXIT=$?` reports **tee**'s
status. Every exit code below is captured without a pipeline.

## 1. The counted predicate — REPRODUCED exactly

```
$ cd /tmp/c1r && sha256sum verifiers/check_scoped_rules_v32.py
f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test > /tmp/c1_st.out 2>&1
$ echo $?
0
```
The four frozen lines, each present **once**, in the declared order
(lines 9, 16, 19, 20 of 21), byte-identical to `plans/round-64.md` §C1 and to
the receipt:

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
```

Receipt pair vs committed bytes:

```
recomputed sha256(git show c019919c:verifiers/check_scoped_rules_v32.py)
  = f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
receipt occurrences of "counter sha256[:]  <64hex>" = 2
  line 3  counter sha256 f8f69c…113d
  line 25 counter sha256: f8f69c…113d
both equal the committed blob: True
$ git diff --quiet HEAD -- .ufo/waves/round-64/receipts/C1-span-measure.txt ; echo $?
0                                        # receipt has no worktree drift
```

**The count is computed, not literal.** `grep -n '\b223\b'` over the counter
⇒ no match. Independent proof by output-diff of the base counter at `078eec4`:

```
$ cd /tmp/c1b && sha256sum verifiers/check_scoped_rules_v32.py
12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test ; echo $?
0
$ diff /tmp/c1b_base.txt /tmp/c1r_pristine.txt
1c1
< counter sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
---
> counter sha256 f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
21c21
< self-test: 0 failure(s) over 219 assertions
---
> self-test: 0 failure(s) over 223 assertions
```
Exactly two lines differ across the 21-line output: the own-sha line and the
tally. **"Every prior line byte-identical; nothing is rewritten" is true as
written** (19/21 lines identical, the two that differ are the sha and the count).

Label-level delta, by instrumenting `check()` on scratch copies of both trees
(`/tmp/c1r_lab`, `/tmp/c1b_lab`; `print("CHECK> " + name)` after
`assertions += 1`):

```
/tmp/c1r_lab exit=0  CHECK> lines: 223
/tmp/c1b_lab exit=0  CHECK> lines: 219
$ diff base.labels tip.labels
22a23,26
> A2 G7: a backticked span made only of stopwords is not rejected
> A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected
> A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it
> A2 G7: a backticked span word shorter than four characters is not rejected
duplicate labels at tip: 0
```
The assertion-set delta is **exactly the four new arms** — no arm removed,
renamed, or shadowed by a duplicate label, and 219+4 = 223.

Determinism / environment robustness (md5 of full output):
```
run1 run2 run3                    exit 0,0,0   687711a73196ef7b869932057243690e (x3)
TZ=Pacific/Kiritimati             exit 0       687711a7…  (identical)
TZ=Etc/GMT+12                     exit 0       687711a7…  (identical)
LC_ALL=C LANG=C                   exit 0       687711a7…  (identical)
```
The suite stubs `run_curl` per world (v32:2285–2311) and reads no wall clock
(`grep datetime.now|date.today|time.time()` ⇒ no match), so the predicate is
network- and date-independent on this host.

Do-nothing control (a), `verifiers/check_scoped_rules_v31.py --self-test`,
exit 0: `survivors closed 5 of 6` … `self-test: 0 failure(s) over 201
assertions` — matches the plan's declared control; it cannot reach 223.

## 2. The kill conjunct — REPRODUCED, all six exit 1

Battery re-derived from MutW2V32 §11 (the only committed definition): each
mutant is **one exact-string replacement** in the `c019919c` bytes, anchor
occurrence asserted `== 1`; the pristine file is restored and re-hashed
(f8f69c) after every run.

| mutant | anchor (exact) | exit | tally | FAIL lines measured | receipt FAIL lines | verdict |
|---|---|---|---|---|---|---|
| SM1 branch removed | comprehension → `span_missing = []` | **1** | 1/223 | 1: arm1 label | same, byte-identical | KILLED |
| SM2 floor dropped | `if len(word) >= 4 and word.lower() not in STOPWORDS` → `if word.lower() not in STOPWORDS` | **1** | 1/223 | 1: arm3 label | same | KILLED |
| SM3 STOPWORDS dropped | same anchor → `if len(word) >= 4` | **1** | 1/223 | 1: arm2 label | same | KILLED |
| SM4 page check dropped | drop `and not supported(word.lower(), page_words(raw_page))` | **1** | 5/223 | **5** (worlds + predicate) | **2** | KILLED |
| SM5 cited-line dropped | drop `and word.lower() not in content_words(raw_line)` | **1** | 1/223 | 1: arm4 label | same | KILLED |
| SM6 always fires | `if span_missing:` → `if True:` | **1** | 10/223 | **10** (1 A2 + 3 new arms + 5 world + predicate + must-fail) | **2** | KILLED |

Verbatim, tip bytes (`/tmp/c1r`), exit codes as printed above:

```
SM1 exit=1  FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
SM2 exit=1  FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False
SM3 exit=1  FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
SM4 exit=1  worlds reject 7 of 7; eligible rows pass 2 of 4   (5 failures)
            FAIL eligible world: the four counted rows are backed: got ['Claude Code', 'VS Code'], expected ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']
            FAIL eligible world: the four counted rows are found live: got [True, True, False, False], …
            FAIL eligible world: the CLI exits 0 at a target of 4: got 1, expected 0
            FAIL eligible world: the summary line is the v2 one: got '… 2 of 4; … 2 of 4', expected '… 4 of 4; … 4 of 4'
            FAIL the predicate line is computed from four passing eligible rows: got 2, expected 4
SM5 exit=1  FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
SM6 exit=1  worlds reject 7 of 7; eligible rows pass 0 of 4   (10 failures)
            FAIL A2: a cell the cited line supports passes: got ['A2 G7: backticked span word(s)  occur in neither the cited line nor the committed snapshot'], expected []
            FAIL A2 G7: a backticked span made only of stopwords is not rejected / … shorter than four characters … / … present in the cited line …
            FAIL eligible world: ×4 + FAIL the predicate line … got 0, expected 4
            FAIL must-fail G9 mutation admits the compound-purpose survivor: got False, expected True
```

No mutant dies on the tautological own-sha assertion (v32:2900–2903 compares
`self_sha()` — read from `__file__` — with `hashlib.sha256(own)` of the same
bytes), and no mutant's kill is attributable to the tally itself: every FAIL
listed above is a semantic assertion.

**The "SM4/SM6 via pre-existing arms" clause, tested directly** — the same six
mutations on the **base** bytes at `078eec4`:

```
BASE 078eec4 SM1: exit=0 SURVIVED  0 failure(s) over 219 assertions
BASE 078eec4 SM2: exit=0 SURVIVED  0 failure(s) over 219
BASE 078eec4 SM3: exit=0 SURVIVED  0 failure(s) over 219
BASE 078eec4 SM4: exit=1 KILLED    5 failure(s) over 219
BASE 078eec4 SM5: exit=0 SURVIVED  0 failure(s) over 219
BASE 078eec4 SM6: exit=1 KILLED    7 failure(s) over 219
```
So the C1 motivating claim ("4 of 6 survive the 219 suite") and the attribution
("SM4/SM6 already red at base, not credited to the new arms") are both true.
The five label *texts* SM4 fails on all pre-exist at base (`grep -Fxc` = 1 in
both base and tip label dumps), as does SM6's A2 label.

### Attribution inside the arms (branch-level, not just label-level)

Direct probes on the committed module:

```
arm1 BACKTICK_RE spans            ['exfiltrates credentials']
arm1 BACKTICKED_IDENTIFIER_RE     []                     # single-token regex — the `missing` branch cannot claim this cell
arm1 g7_conjunct                  ['A2 G7: backticked span word(s) credentials occur in neither the cited line nor the committed snapshot']
arm1 action_conjunct              same single G7 span reason
arm1 span_missing                 ['credentials']         # 'exfiltrates' IS supported: 4-char prefix vs page word 'exfiltrated'
arm2/arm3/arm4 action_conjunct    []                     # negative witnesses admitted, no earlier A2 gate masks them
run_curl at judge level           page-derived lines (v32:1555–1557: lines = page.splitlines())
g7_conjunct call sites            only action_conjunct (v32:1179) and self-test arm 4 (v32:2157)
```
Arm 1's kill is produced by the **span branch's own message**, not by the
identifier branch — SM1 is genuinely pinned. Arms 2–4 are clean negative
witnesses (the full `action_conjunct` admits their cells, so the only thing
that can reject them is the branch under test) — i.e. MutSpanArms F1's
wrong-reason failure mode is closed at the tip by the hardened arm 4.

## Findings

**F1 — MEDIUM (pin depth; extends MutSpanArms F2 to arms 1 and 4, not named in
E3 or C1's Bound).** Every one of SM1/SM2/SM3/SM5 is killed by **exactly one**
assertion, and the counter's exit code cannot see arm deletion — only the
receipt's `223` literal can:

```
arms 2+3 deleted        exit=0  self-test: 0 failure(s) over 221 assertions
arms 2+3 deleted × SM2  exit=0  0 failure(s) over 221      # SM2 then survives
arm 1 deleted           exit=0  self-test: 0 failure(s) over 222 assertions
arm 1 deleted × SM1     exit=0  0 failure(s) over 222      # SM1 then survives
arms 1–3 deleted        exit=0  self-test: 0 failure(s) over 220 assertions
```
`MutW2V32` §11's count is load-bearing precisely because the suite is silent
here. The four arms as landed are one-deep per mutant, and a later "assertion
count updated" edit that keeps 0 failures un-pins SM1/SM2/SM3/SM5 with no
counter-side signal. Cheapest fix: an intra-suite tally assertion at the end of
`selftest()` (`check("assertion tally", assertions, 223)`) — it fails closed on
deletion, at exit 1, without adding behavioural coverage. This is a coverage
*shape* finding, not a false predicate: at the landed bytes all six kills are
real.

**F2 — LOW (receipt precision; M95-adjacent).** `receipts/C1-span-kill.txt`
quotes **2 of SM4's 5** and **2 of SM6's 10** measured FAIL lines with no
elision marker (no `…`/`+N more`). Verdicts (`exit=1`) and every quoted line are
byte-exact, so nothing is false; but a literal re-derivation diff against the
receipt shows a mismatch (2 vs 5, 2 vs 10), which is the same class the C2
counter polices in the r63 report citations.

**F3 — LOW (attribution wording in LOG/SCORECARD).** `LOG.md:2602` and
`SCORECARD.md:375` say the kill conjunct holds "with arm-attributed FAIL lines
(SM4/SM6 by the pre-existing `eligible world` arms)". Measured: true for SM4
(all 5 of its FAILs are pre-existing), but SM6's **first** FAIL is the
pre-existing `A2: a cell the cited line supports passes` (not a world arm) and
3 of its 10 FAILs are the *new* arms 2/3/4. The defensible sentence is the one
my base run proves: "SM4/SM6 were already red at base (5 and 7 failures at
`078eec4`), so their kills are not credited to the new arms."

**F4 — LOW (arm-1 label/fixture precision).** Arm 1's label claims "a
backticked span whose words occur in neither the cited line nor the page", but
`span_missing` = `['credentials']`: `exfiltrates` is **supported** by the
4-char prefix rule against the page word `exfiltrated`. The witness is "one
fabricated word inside an otherwise-supported span", which is a stronger pin
than the label states (it also exercises `supported()`'s prefix arm) but the
plural misstates it. Separately, arm 1's fixture is not judge-shaped
(`raw_line` is not a line of the page it passes), the same class E3 records for
arm 4 only; E3's sentence should cover both arms or the label should stop
implying a page-absence witness.

**F5 — corroboration (no defect).** E3's SM5 claim is accurate, re-derived
independently: `g7_conjunct` is reachable only through `action_conjunct`, and
`judge()` hands it `lines = page.splitlines()` (v32:1552–1557), so the
cited-line filter cannot fire on any judge-reachable input. The declared bound
is honest, not a cover story.

## Residual risk

- The mutation *operators* for SM4/SM5 are prose in `MutW2V32` §11, never
  committed as a script. My replacements are the minimal exact-string
  removals of the two `and` continuations, unique in the file, and they
  reproduce the claimed labels exactly; a different-but-defensible removal
  would still drop the same conjunct. [INFERENCE] low risk.
- The `kotodama R64-M9` attribution rule invoked by LOG/SCORECARD is outside
  this item and was not audited.
- `.ufo/waves/round-64/receipts/noharm-tip.txt` is modified in the worktree at
  measurement time (not committed); it is not part of C1 and was not audited.

## Verification gaps

- No live-fetch path was exercised (the self-test stubs `run_curl`); whether
  `--rev <tip> --fetch` still exits 0 at `c019919c` is not claimed here.
- Only `check_scoped_rules_v32.py` was attacked; the C2 counter and the
  S120/lesson/LOG claims belong to sibling seats.

Report: .ufo/waves/round-64/w2/RevW2C1Count.md
