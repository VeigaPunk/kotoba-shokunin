# MutW2V32Arms — wave-2 falsifier: the LANDED v32 arms at `c019919c`

role: mutation tester (leaf; no subagent dispatch, no lane writes)
item: mutation-test the **landed** (not reconstructed) round-64 C1 arms on real
bytes — (a) flip each new arm's expectation, (b) swap arm 4 back to the
unhardened §11 cell and show the A2-wiring mask returns (SM5 then survives),
(c) delete arms 2–3 and verify the count drops to 221 with the frozen 223
literal as the only guard, (d) re-run `MutSpanArms`' A3 positive control — plus
the cross-round kill check: every mutant the r63 **219**-assertion suite
admitted must be red on the landed **223** suite.
date: 2026-10-24. Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(jj-colocated). Measured tip `c019919c97ab5fe98e87a7754b4449ea4e699c99`
(base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`).
Detector (the frozen predicate's own command), unchanged for every run:

```
python3 -B verifiers/check_scoped_rules_v32.py --self-test
```

Scratch `/tmp/mutw2v32r64` (disposable): `git clone --no-hardlinks` of the lane
plus a `git worktree` at base `078eec4` for the 219 control. **No installs**
(stdlib `python3` 3.14.8, read-only `git`), nothing to record under the tooling
directive. The lane was written only at this report path.

---

## 0. Baseline and byte identity

Landed v32 extracted with `git show c019919c:verifiers/check_scoped_rules_v32.py`:

```
sha256 f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d  147512 bytes  3000 lines
```

`git diff --stat 078eec4 c019919c -- verifiers/check_scoped_rules_v32.py` →
`1 file changed, 34 insertions(+)` — **a pure insertion**; no prior line is
rewritten, so C1's "the four arms append to the existing suite; nothing is
rewritten" holds at byte level. The landed file also equals the lane working
tree file (`sha256sum` of both, identical), and HEAD `b99fb79` (measurements)
carries the same bytes as `c019919c`.

```
$ cd /tmp/mutw2v32r64/tree && python3 -B verifiers/check_scoped_rules_v32.py --self-test
counter sha256 f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
...
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
EXIT=0
```

Base control (worktree at `078eec4`, sha `12d093a1…`, the §11 bytes): same 21-line
shape, `self-test: 0 failure(s) over 219 assertions`, `EXIT=0`.

**Note on the frozen predicate's shape (bound, not a kill).** The predicate
names four lines; the suite prints **21** (own-sha, 8 world lines, 6 survivor
lines, 3 `must-fail` lines, 2 summaries, the tally). The four named lines are
present, so the predicate reads as *containment* and PASSES. Consequence worth
naming: the E2e and G7 `must-fail` summary lines are **not pinned by C1's four
lines** — only the `0 failure(s)` tally would notice their arms breaking. The
wave-1 baselines (`MutSpanArms` §1) quote the same run as "all four predicate
lines", an elision of the two extra `must-fail` lines; the landed receipt
should not repeat that elision unlabelled (M95 class, reporting only).

**Static-vs-runtime tally.** `grep -c '^        check('` on the landed bytes
counts **214**, not 223 (some `check(` calls sit at other indents, and loop
bodies multiply at runtime). This is exactly the failure mode E1 item 2 fixed
for the C2 counter — a literal count can never certify — and it confirms the
landed C1 tally must be read from the runtime line, never from a static scan.

---

## 1. (a) Expectation flips on the landed arms — 4/4 KILLED

One exact-string edit per mutant, inside that arm's own `check(...)` slice
(the builder asserts every anchor occurs exactly once and that the four slices
are ordered); restored to `f8f69cad…` after every run.

| mutant | edit | mutant sha256 | exit | tally | FAIL line | verdict |
|---|---|---|---|---|---|---|
| A1-arm1-flip | arm 1 `, True)`→`, False)` | `e08af5fd5cf2…e904` | **1** | 1 / 223 | arm 1 (`got True, expected False`) | **KILLED** |
| A1-arm2-flip | arm 2 `, False)`→`, True)` | `1dfe44f012bb…f019` | **1** | 1 / 223 | arm 2 (`got False, expected True`) | **KILLED** |
| A1-arm3-flip | arm 3 `, False)`→`, True)` | `7dad25636e90…6a84` | **1** | 1 / 223 | arm 3 (`got False, expected True`) | **KILLED** |
| A1-arm4-flip | arm 4 `, False)`→`, True)` | `fb4468ce5480…ec7f` | **1** | 1 / 223 | arm 4 (`got False, expected True`) | **KILLED** |

```
=== A1-arm1-flip  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got True, expected False
=== A1-arm2-flip  exit=1
    FAIL> FAIL A2 G7: a backticked span made only of stopwords is not rejected: got False, expected True
=== A1-arm3-flip  exit=1
    FAIL> FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got False, expected True
=== A1-arm4-flip  exit=1
    FAIL> FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got False, expected True
```

Each flip fails at **exactly one** assertion and by **its own** label: no arm is
a tautology, and no flip collides with a sibling arm. (This is the A1 property
only; discrimination of the *guard* is §5.)

---

## 2. (b) Arm 4 fixture/call-site matrix — E3.2 is load-bearing

Two fixture variants × two call sites, each scored on the landed bytes, plus
each × SM5 (the cited-line check dropped). All edits are within arm 4's slice;
`named(g7_conjunct(` occurs exactly once in the file, so the call-site swap is
unambiguous.

| variant | exit | tally | verdict |
|---|---|---|---|
| unhardened cell, `g7_conjunct` (§11 original) | 0 | 0 / 223 | green |
| unhardened cell, `action_conjunct` (A2 wiring) | 0 | 0 / 223 | green **for the wrong reason** |
| unhardened cell, `g7_conjunct` **× SM5** | **1** | 1 / 223 | SM5 **KILLED** |
| unhardened cell, `action_conjunct` **× SM5** | **0** | **0 / 223** | SM5 **SURVIVES** ← the mask |
| hardened cell (landed), `action_conjunct` | 0 | 0 / 223 | green |
| hardened cell (landed), `action_conjunct` **× SM5** | **1** | 1 / 223 | SM5 **KILLED** |

```
=== B-unhardened-arm4-A2wiring-x-SM5   sha=fc82a5ff9ddcb394 exit=0
    self-test: 0 failure(s) over 223 assertions
=== B-unhardened-arm4-g7wiring-x-SM5   sha=bc3cc1cc178ecd87 exit=1
    FAIL> FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
=== B-hardened-arm4-A2wiring-x-SM5     sha=8ebfe483031a68bf exit=1
    FAIL> FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
```

**The mask, measured at the component level** (importing the landed module and
the SM5 mutant directly; `named(r, "G7")` is `any("G7" in x for x in r)` per
landed:1767):

```
HARDENED   cell: The tool writes quota nightly and `mode quota`.
   landed g7=False act=False | g7_reasons=[] | act_reasons=[]
   SM5    g7=True  act=True  | g7_reasons=['A2 G7: backticked span word(s) mode occur in neither the cited line nor the committed snapshot']
UNHARDENED cell: The tool writes mode quota nightly and `mode quota`.
   landed g7=False act=False | g7_reasons=[] | act_reasons=['A2: action word(s) mode do not occur on the committed snapshot']
   SM5    g7=True  act=False | g7_reasons=['A2 G7: backticked span word(s) mode occur in neither the cited line nor the committed snapshot']
                             | act_reasons=['A2: action word(s) mode do not occur on the committed snapshot']
```

With the unhardened cell, `content_words()` keeps `mode` (it also occurs in plain
text) while the page lacks it, so `action_conjunct` returns at its page gate
(landed:1169–1173) **before** the `g7_conjunct` call at landed:1179 — the arm's
`False` expectation is then satisfied by an `A2:` reason, and SM5's new `A2 G7:`
reason never reaches the assertion. With the landed hardened cell, `mode` exists
only inside the backticked span, A2 passes, G7 is reached, and SM5 is killed
**under either call site**. **Verdict: E3.2's fixture change is load-bearing and
is landed; without it the landed suite would admit SM5 under A2 wiring.** Arm 4's
`g7_conjunct` call site is now immaterial (it kills SM5 either way), so no
residual F1 exposure remains in the landed bytes.

**Arms 1–3 are A2-clean (no sibling of the F1 defect).** Measured with
`action_conjunct` on each arm's own fixture:

```
arm1 landed/SM2/SM3 -> ['A2 G7: backticked span word(s) credentials …']   (G7 reached)
arm2 landed -> [] ; SM3 -> ['A2 G7: … because, otherwise …']              (G7 reached)
arm3 landed -> [] ; SM2 -> ['A2 G7: … it, ox …']                          (G7 reached)
```

Every reason is an `A2 G7:` reason, i.e. A2's gates pass and the G7 branch is
actually exercised; the short-circuit defect existed only in the unhardened arm 4.

---

## 3. (c) Deleting arms 2–3 — 221, and the count literal is the only detector

| mutant | edit | sha256 | exit | tally |
|---|---|---|---|---|
| C-arms2-3-deleted | arm 2 `check(` → arm 4 `check(` removed | `d621564ceb05…36e8` | **0** | **0 / 221** |
| C × SM2 | + floor dropped | `8c27f12624fe…f29b` | **0** | **0 / 221** |
| C × SM3 | + STOPWORDS dropped | `25060b1257f2…95a2` | **0** | **0 / 221** |

```
=== C-arms2-3-deleted  exit=0
    worlds reject 7 of 7; eligible rows pass 4 of 4
    survivors closed 6 of 6
    must-fail E2e guard disabled admits e2e-negated-path-key: yes
    must-fail G7 disabled admits e2f-backticked-event-claim: yes
    must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
    self-test: 0 failure(s) over 221 assertions
```

All six non-tally predicate lines are **byte-identical** to the pristine run, so
nothing behavioural notices the deletion. The frozen predicate, evaluated
literally (four named lines must be present, exit 0), separates the cases:

```
PREDICATE[landed]:            PASS (exit 0, four lines present)
PREDICATE[base-078eec4]:      FAIL (exit=0 missing=1)  MISSING: self-test: 0 failure(s) over 223 assertions
PREDICATE[arms2-3-deleted]:   FAIL (exit=0 missing=1)  MISSING: self-test: 0 failure(s) over 223 assertions
```

**Verdict: the `223` literal is the sole anti-deletion guard, and it is
sufficient for exactly this deletion** — but it is a *count*, not a
discrimination check: any future edit that keeps the count at 223 while
weakening an arm is invisible to it, and the same literal is the only thing
that distinguishes 221 from 223. The measured consequence is real: with arms
2–3 gone, **SM2 and SM3 both survive** (`0 failure(s) over 221 assertions`,
exit 0), so deleting the two negative witnesses silently un-pins the floor and
the STOPWORDS filter. This reproduces `MutSpanArms` F2 on the landed bytes.

---

## 4. (d) `MutSpanArms` A3 positive control, re-run on landed bytes

| mutant | edit | sha256 | exit | tally | verdict |
|---|---|---|---|---|---|
| A3a | arm 1 span `` `exfiltrates credentials` `` → `` `glob syntax` `` | `0d6e34aae77f…dad7` | **1** | 1 / 223 | **red as declared** (`got False, expected True`) |
| A3b | A3a + arm 1 expectation `True`→`False` | `82cf3565d65e…6ab8` | **0** | 0 / 223 | **green control** |

```
=== A3a-arm1-supported-span            exit=1
    FAIL> FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
=== A3b-arm1-supported-span-expFalse   exit=0
    self-test: 0 failure(s) over 223 assertions
```

A3a's red is the declared control behaviour (a supported span cannot satisfy
arm 1 as written), and it proves arm 1 is input-bound rather than label-bound.
A3b is the well-formed green control. **Verdict: reproduced, both readings
served** — identical to `MutSpanArms` §3/A3a,A3b, now on the landed bytes.

---

## 5. The cross-round kill check — every 219-admitted mutant is red at 223

`SM` mutants are exact-string edits of the landed guard (each anchor asserted
unique): SM1 `span_missing = []`; SM2 floor dropped; SM3 STOPWORDS dropped;
SM4 page check dropped; SM5 cited-line check dropped; SM6 `if span_missing:`
→ `if True:`.

**At base `078eec4` (219 assertions, sha `12d093a1…`) — the r63 admission set:**

```
SM1 exit=0  0 failure(s) over 219 assertions      SURVIVES
SM2 exit=0  0 failure(s) over 219 assertions      SURVIVES
SM3 exit=0  0 failure(s) over 219 assertions      SURVIVES
SM4 exit=1  5 failure(s) over 219 assertions      killed (world lines)
SM5 exit=0  0 failure(s) over 219 assertions      SURVIVES
SM6 exit=1  7 failure(s) over 219 assertions      killed (world lines + A2)
```

**At the landed tip (223 assertions) — all six red, each by its own label:**

| mutant | sha256 | exit | tally | FAIL label | verdict |
|---|---|---|---|---|---|
| SM1 branch removed | `acb23eadf5b9…b380` | **1** | 1 / 223 | **arm 1** | **KILLED** |
| SM2 floor dropped | `84c6c0e9a137…fa98` | **1** | 1 / 223 | **arm 3** | **KILLED** |
| SM3 STOPWORDS dropped | `e43ca64bc7eb…f4d9` | **1** | 1 / 223 | **arm 2** | **KILLED** |
| SM4 page check dropped | `296b5744c74b…9b39` | **1** | 5 / 223 | world lines (`eligible rows pass 2 of 4`) | **KILLED** (not a new-arm pin) |
| SM5 cited-line check dropped | `c84ea21478ff…e4a5` | **1** | 1 / 223 | **arm 4** | **KILLED** |
| SM6 branch always fires | `17f3d799e8c0…5528` | **1** | 10 / 223 | world lines + arms 2,3,4 | **KILLED** (not a new-arm pin) |

```
=== SM1-branch-removed  exit=1
    FAIL> FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
=== SM2-floor-dropped  exit=1
    FAIL> FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False
=== SM3-stopwords-dropped  exit=1
    FAIL> FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
=== SM5-citedline-check-dropped  exit=1
    FAIL> FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
```

**Verdict: the landed suite kills all four mutants the 219 suite admitted
(SM1, SM2, SM3, SM5), each with its own new arm's FAIL label** — the E3.1 kill
conjunct holds on real bytes. SM4/SM6 stay red on pre-existing world arms and
are correctly *not* counted as new-arm pins (the `ConnSibling` R64-M9
discipline). No committed-row verdict moved: `eligible rows pass 4 of 4` and
`worlds reject 7 of 7` in every landed run.

**Load-bearing, not just asserted.** Component-level evasion witness (the arm 1
cell, through the composition G7 actually sits in):

```
LANDED action_conjunct -> ['A2 G7: backticked span word(s) credentials occur in neither the cited line nor the committed snapshot']
SM1    action_conjunct -> []  (ADMITTED)
```

So with the branch removed the fabricated span is accepted; arm 1 is the
assertion that stands between the two. This is component-level, not the full
`judge()` path (which needs a constructed world); `MutW2V32` §11 measured the
judge-level ADMIT and I did not re-run it — labelled as such rather than
claimed.

---

## 6. Findings

- **F1 (E3.2 verified, load-bearing).** Arm 4's hardened fixture is what makes
  the landed arm discriminate SM5 under A2 wiring; the §11 original cell leaves
  SM5 alive (`B-unhardened × A2 × SM5` = exit 0, 0/223) while still printing the
  four frozen lines. E3.2's "same arm name, same expectation, all prior lines
  unchanged" is confirmed by the pure-insertion diff and the 223 tally.
- **F2 (the count literal is the only anti-deletion guard).** `C-arms2-3-deleted`
  is green at 221 with every other predicate line byte-identical; SM2 and SM3
  survive on the reduced suite. The `223` literal is therefore load-bearing
  *and* under-discriminating: it detects deletion, not weakening at constant
  count. Any later "count refresh" edit is a guard edit and must be receipted as
  such.
- **F3 (predicate is containment-shaped).** The frozen C1 predicate names 4 of
  the suite's 21 output lines; the E2e and G7 `must-fail` summary lines ride
  along unpinned (their arms' failures are still caught by the `0 failure(s)`
  tally). Not a defect in the claim; a wording bound for the receipt, and the
  wave-1 "all four predicate lines" quotes elide the other two.
- **F4 (static tally ≠ runtime tally).** 214 `^        check(` tokens vs 223
  runtime assertions on the same bytes. Reconfirms E1.2's decision to
  materialize and run the counter instead of counting tokens — the C1 receipt
  must never substitute a static count.
- **F5 (arms 1–3 are A2-clean).** Their reasons are `A2 G7:` reasons, so they
  reach the branch; the F1 short-circuit class exists only in the unhardened
  arm 4 and is closed in the landed bytes. No sibling exposure found.
- **F6 (no equivalent mutants in this battery).** Every mutant that stayed green
  (`B-unhardened × A2`, `C-arms2-3-deleted`, `C × SM2/SM3`, `A3b`) is either a
  deliberate mask/control or an observable loss of discrimination shown above;
  none is an equivalent mutant.

## 7. Restoration and bounds evidence

- **Restore discipline:** every one of the 21 scored runs rewrote
  `tree/verifiers/check_scoped_rules_v32.py` from `/tmp/mutw2v32r64/landed.py`
  in a `finally` block and asserted `sha256 == f8f69cad…`; the harness's last
  line printed `=== restore verified: scratch v32 sha f8f69cada703`. The 219
  control harness asserted `12d093a1…` the same way (final `base/` hash above).
  The standalone 221 run was followed by `cp landed.py` + `sha256sum` =
  `f8f69cad…`.
- **Before/after:** landed bytes `f8f69cad…` (147512 B) before the battery and
  after; base bytes `12d093a1…` (145577 B) before and after.
- **Lane untouched:** `verifiers/check_scoped_rules_v32.py` still hashes
  `f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d` after all
  work; `git status --porcelain` shows only a sibling's
  `M .ufo/waves/round-64/receipts/noharm-tip.txt` and the `?? w2/` directory
  (not mine). No git/jj writes in the lane; the clone used `--no-hardlinks` and
  the base worktree lives inside the scratch clone.
- **Bounds:** detector = the frozen command only; component probes import the
  module and call `g7_conjunct`/`action_conjunct`/`content_words`/`page_words`
  directly; no full `judge()` re-run, no other runtime, no network, no installs.
  Scratch retained for audit: `/tmp/mutw2v32r64/{landed.py,base219.py,m221.py,
  sm1_v32.py,sm2_v32.py,sm3_v32.py,sm5_v32.py,harness.py,predicate.sh,
  results.json,tree/,base/}`.

## 8. Reproduction anchors (exact)

- landed bytes: `git show c019919c:verifiers/check_scoped_rules_v32.py` →
  `f8f69cad…`; arms at lines 2129–2162; guard `span_missing` at 1055–1067;
  `action_conjunct` page gate 1169–1173, `g7_conjunct` call 1179.
- A1: inside arm *i*'s slice (from its `check("A2 G7: …` marker to the next
  `        check(`), the trailing `, True)` ↔ `, False)`.
- B: `"The tool writes quota nightly and \`mode quota\`."` →
  `"The tool writes mode quota nightly and \`mode quota\`."` (unharden);
  arm 4's `named(g7_conjunct(` → `named(action_conjunct(` (A2 wiring).
- C: delete from arm 2's `check(` marker to arm 4's `check(` marker.
- A3: arm 1 `` `exfiltrates credentials` `` → `` `glob syntax` `` (+ expectation
  flip for A3b).
- SM1 `span_missing = sorted({…})` → `span_missing = []`; SM2
  `if len(word) >= 4 and word.lower() not in STOPWORDS` → `if word.lower() not in STOPWORDS`;
  SM3 → `if len(word) >= 4`; SM4 drop `        and not supported(word.lower(), page_words(raw_page))})`;
  SM5 drop `        and word.lower() not in content_words(raw_line)`;
  SM6 `    if span_missing:` → `    if True:`.
- run: `cd /tmp/mutw2v32r64/tree && python3 -B verifiers/check_scoped_rules_v32.py --self-test`.

No judgement on landing, no integration, no ship recommendation, no other
runtime invoked. Stop after this probe.

Report: .ufo/waves/round-64/w2/MutW2V32Arms.md
