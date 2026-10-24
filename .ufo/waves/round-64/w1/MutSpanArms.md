# MutSpanArms

role: mutation tester (leaf member — no subagent dispatch, no lane writes)
item: score the four new G7 `span_missing` self-test arms (C1) as a mutation
target: A1 expectation flips ×4, A2 arm-4 call-site swap, A3 fixture
substitution control, A4/A6 re-verify SM2/SM3 red, A5 delete arms 2–3; plus
the §11 20 k-cell discrimination replicate.
date: 2026-10-24. Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(jj-colocated), base tip `c04fffbeafcaf810897258d56f99cca736ed3a91` (plan
freeze; lane bytes at `078eec4`). Detector: the frozen predicate
`python3 -B verifiers/check_scoped_rules_v32.py --self-test`. No installs; no
git/jj writes; the lane was not written except this report file.

Scratch: `/tmp/mutspan64` (disposable). Because the counter's self-test
resolves committed blobs and imports a sibling verifier relative to `__file__`,
the scratch is an independent clone (`git clone --no-hardlinks` of the lane into
`/tmp/mutspan64/tree`, no hardlinks, nothing written back); the counter under
test is `tree/verifiers/check_scoped_rules_v32.py`. Mutant files are retained
at `/tmp/mutspan64/mutants/*.py`. Python 3.14.8.

---

## 0. Dependency finding — the arms were not available from ExecSpanArms

`.ufo/waves/round-64/w1/` at 00:38 lists `ConnSibling.md`, `CriticC2Bound.md`,
`ExecCalibVerify.md`, `ExecCensusAfter.md`, `ExecGateRow.md`,
`ExecSeatDriftFix.md`, `ExecSpanBefore.md`, `ScoutQualityDebt.md`,
`ScoutS049.md`, `ScribeLOGCorr.md`, `ScribeQ60.md`, `ScribeSHONEN.md`,
`swarm-registry.json` — **no `ExecSpanArms.md`**. Per the ticket I took the
four arms from `MutW2V32.md` §11, lines 937–966 (the fenced block after
"The missing assertion."), byte-for-byte:

```
block: 30 lines, 4 `check(` calls, 1642 bytes,
sha256 5900a62ad95f5ed8180a3ee9837ca92979c6f51bb9164d6d6c5563dfcfa48c1f
```

**Finding 0 (reproducibility).** §11 records the *resulting file* sha
`ae84673ed61d1d2858a7600ab8870c0545163340d39922104a85c967e1da71bf` but **not
the insertion point**. Five plausible placements of the verbatim block into
the base bytes were hashed and none reproduces `ae84673e`:

```
after-identifier-check   3612e76a442e77aa07352d835c16bf0981c0effe2b6c2ac2cc4c69e2bbf6b44c
before-g9-probes         22703865726571fcab065625e799e233d9292b4868f3ab82c149a88d5c814417
after-onword-clause      d8024540732d94fac0a9d5a2e78fbf9b74ebbbeb42160f705ae74790a3413834
after-probes-loop        266c15805d06cf68bef82c490cde38ec0809d17768b0456582d95c21138fb1ef
before-own-sha256        fa685f1ffb189a651a3277369debe759d7407b30bba2c640fca0713c27e25cca
```

[INFERENCE] the seat's file carries a comment header or spacing §11 does not
show. The **check bodies** I scored are §11's bytes exactly; the placement is
mine. Placement is immaterial, measured: three valid placements each print
`0 failure(s) over 223 assertions`, exit 0 —

```
placement before-g9-probes   exit=0 self-test: 0 failure(s) over 223 assertions sha=703be977030b
placement after-probes-loop  exit=0 self-test: 0 failure(s) over 223 assertions sha=a87ea99b7e12
placement end-before-own-sha exit=0 self-test: 0 failure(s) over 223 assertions sha=7791504715f3
```

Scored suite (`/tmp/mutspan64/arms_pristine.py`, arms before the
own-sha256 checks):

```
base   (219) sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43 145577 bytes
v32+arms (223) sha256 7791504715f308e2cedf4f9cc746ae08d513a3dc01861b4afe1fb2a84911cda2 147220 bytes
```

**Ask for the L1:** when C1 lands, record the insertion line (or the landed
sha) in the receipt, otherwise the 223-assertion file cannot be re-derived from
the report the way §11's 219-assertion file cannot.

---

## 1. Baselines (before any mutation)

Base bytes, committed lane counter at `078eec4` / `c04fffb`:

```
$ cd /tmp/mutspan64/tree && python3 -B verifiers/check_scoped_rules_v32.py --self-test
...
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 219 assertions
EXIT=0
```

With the four §11 arms appended (all four predicate lines, as frozen in the
plan):

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
EXIT=0
```

Prior lines are unchanged from the 219 run (same three lines, same
`eligible rows pass 4 of 4`); the arms add exactly 4 assertions and change no
committed-row verdict. Detector runtime 0.26 s per run.

---

## 2. THE KILL TABLE

Each mutant is **one exact-string replacement** (or one 2-check deletion) in
the 223-assertion bytes; the builder asserts each anchor occurs exactly once.
After **every** run the scratch counter was rewritten from the pristine bytes
and re-hashed to `77915047…` (asserted in the harness).

| mutant | mutation | sha256 | exit | self-test line | FAIL lines | verdict |
|---|---|---|---|---|---|---|
| **A1-arm1-flip** | arm 1 expectation `True`→`False` | `7a1ce757c8d0…40a2` | **1** | 1 failure / 223 | arm 1 | **KILLED** |
| **A1-arm2-flip** | arm 2 expectation `False`→`True` | `d681812c48ae…c770` | **1** | 1 failure / 223 | arm 2 | **KILLED** |
| **A1-arm3-flip** | arm 3 expectation `False`→`True` | `401c5a7ae2fa…1b63` | **1** | 1 failure / 223 | arm 3 | **KILLED** |
| **A1-arm4-flip** | arm 4 expectation `False`→`True` | `4b4165974c6d…e0e4` | **1** | 1 failure / 223 | arm 4 | **KILLED** |
| **A2** | arm 4 `named(g7_conjunct(` → `named(action_conjunct(` | `7b18ee991eff…184a` | **0** | **0 failures / 223** | — | **SURVIVED** |
| **A3a** | arm 1 span `` `exfiltrates credentials` `` → `` `glob syntax` `` (supported by the cited line) | `c7ef14bdd573…03c5` | **1** | 1 failure / 223 | arm 1 (got False, expected True) | **CONTROL RED — as declared** (not equivalent; the arm is input-bound) |
| **A3b** | as A3a **and** expectation `True`→`False` (well-formed positive control) | `0a59a5452f09…ee29` | **0** | 0 failures / 223 | — | **green control** (admissible; see F4) |
| **A4 = SM2** | guard floor dropped: `if len(word) >= 4 and word.lower() not in STOPWORDS` → `if word.lower() not in STOPWORDS` | `db5ec80df83c…3af9` | **1** | 1 failure / 223 | arm 3 (got True, expected False) | **KILLED** |
| **A5** | arms 2 and 3 deleted entirely | `415016972c7c…ff66` | **0** | **0 failures / 221** | — | **SURVIVED behaviourally**; killed only by the count literal (F2) |
| **A5 × SM2** | A5 + SM2 | `62738e0a3f8e…a56c` | **0** | 0 failures / 221 | — | SM2 **survives** on the reduced suite |
| **A5 × SM3** | A5 + SM3 | `9e16acb94026…20eb` | **0** | 0 failures / 221 | — | SM3 **survives** on the reduced suite |
| **A6 = SM3** | STOPWORDS filter dropped: `if len(word) >= 4 and word.lower() not in STOPWORDS` → `if len(word) >= 4` | `6181e5b50876…d5d2` | **1** | 1 failure / 223 | arm 2 (got True, expected False) | **KILLED** |
| SM1 (re-verify) | `span_missing = […comprehension…]` → `span_missing = []` | `3cdbc3de045f…e047` | **1** | 1 failure / 223 | arm 1 | **KILLED** |
| SM4 (re-verify) | page check dropped | `842050b7146d…3e78` | **1** | 5 failures / 223 | world lines (`eligible rows pass 2 of 4`) | **KILLED** |
| SM5 (re-verify) | cited-line check dropped | `0531bb1692e2…e985` | **1** | 1 failure / 223 | arm 4 | **KILLED** |
| SM6 (re-verify) | `if span_missing:` → `if True:` | `211aff15a1c1…20b0fc` | **1** | 10 failures / 223 | worlds + arms 2,3,4 | **KILLED** |
| **A2 × SM5** | A2 wiring + SM5 | `f330391dbcd6…f6ae` | **0** | **0 failures / 223** | — | SM5 **survives** under the A2 wiring → A2 is **not equivalent** |
| HARDENED arm 4 | arm 4 cell → `` The tool writes quota nightly and `mode quota`. `` | `ded23ac3d80d…1384` | **0** | 0 failures / 223 | — | green (see §5) |

Full 64-hex hashes and the mutated files: `/tmp/mutspan64/mutants/`.

---

## 3. Verbatim output per mutant

```
=== A1-arm1-flip  exit=1
    worlds reject 7 of 7; eligible rows pass 4 of 4
    survivors closed 6 of 6
    must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got True, expected False
=== A1-arm2-flip  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span made only of stopwords is not rejected: got False, expected True
=== A1-arm3-flip  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got False, expected True
=== A1-arm4-flip  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got False, expected True
=== A2-arm4-wired-to-action_conjunct  exit=0
    worlds reject 7 of 7; eligible rows pass 4 of 4
    survivors closed 6 of 6
    must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
    self-test: 0 failure(s) over 223 assertions
=== A3a-arm1-supported-span  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
=== A3b-arm1-supported-span-expFalse  exit=0
    self-test: 0 failure(s) over 223 assertions
=== A4-SM2-floor-dropped  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False
=== A6-SM3-stopwords-dropped  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
=== A5-arms2-3-deleted  exit=0
    worlds reject 7 of 7; eligible rows pass 4 of 4
    survivors closed 6 of 6
    must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
    self-test: 0 failure(s) over 221 assertions
=== A5-x-SM2  exit=0
    self-test: 0 failure(s) over 221 assertions
=== A5-x-SM3  exit=0
    self-test: 0 failure(s) over 221 assertions
=== SM1-branch-removed  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
=== SM4-page-check-dropped  exit=1
    worlds reject 7 of 7; eligible rows pass 2 of 4
    self-test: 5 failure(s) over 223 assertions
    FAIL> FAIL eligible world: the four counted rows are backed: got ['Claude Code', 'VS Code'], expected ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']
    FAIL> FAIL eligible world: the four counted rows are found live: got [True, True, False, False], expected [True, True, True, True]
    FAIL> FAIL eligible world: the CLI exits 0 at a target of 4: got 1, expected 0
    FAIL> FAIL eligible world: the summary line is the v2 one: got '... 2 of 4; ... 2 of 4', expected '... 4 of 4; ... 4 of 4'
    FAIL> FAIL the predicate line is computed from four passing eligible rows: got 2, expected 4
=== SM5-citedline-check-dropped  exit=1
    self-test: 1 failure(s) over 223 assertions
    FAIL> FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
=== SM6-branch-always-fires  exit=1
    worlds reject 7 of 7; eligible rows pass 0 of 4
    must-fail G9 disabled admits e2f-compound-purpose-outside-citation: no
    self-test: 10 failure(s) over 223 assertions
    FAIL> FAIL A2: a cell the cited line supports passes: got ['A2 G7: backticked span word(s)  occur in neither ...'], expected []
    FAIL> FAIL eligible world: the four counted rows are backed: got [], expected [four clients]
    ... (5 world lines) ...
    FAIL> FAIL must-fail G9 mutation admits the compound-purpose survivor: got False, expected True
    FAIL> FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
    FAIL> FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False
    FAIL> FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
=== A2-x-SM5  exit=0
    self-test: 0 failure(s) over 223 assertions
=== HARDENED-arm4-clean-cell  exit=0
    self-test: 0 failure(s) over 223 assertions
```

(Output blocks elide only lines repeated verbatim from the pristine run; every
FAIL line is quoted in full except SM6's five world lines, abbreviated with
`...` in this one place. The three non-count predicate lines are identical in
every run except SM4/SM6, which change `eligible rows pass` / `must-fail G9`
as quoted.)

---

## 4. Findings

### F1 — A2 survives: arm 4's fixture is not A2-clean, so the assertion cannot see its own call site

The arm-4 cell is

```
The tool writes mode quota nightly and `mode quota`.
page: The tool writes quota nightly.\n\n## Appendix\nThe agent secretly uploads files.
```

`content_words()` strips backticked spans, so the word `mode` — which appears
**both** in plain text and inside the span — is a cell content word, and the
page lacks it. Measured on the landed bytes:

```
landed g7_conjunct      -> []
landed action_conjunct  -> ['A2: action word(s) mode do not occur on the committed snapshot']
landed g9_conjunct      -> []
content_words(cell)     -> ['mode', 'nightly', 'quota', 'tool', 'writes']
page_words(page)        -> ['agent','appendix','files','nightly','quota','secretly','tool','uploads','writes']
BACKTICK_RE.findall     -> ['mode quota']
```

So `named(action_conjunct(...), "G7")` is `False` — **not because G7 allowed
the span, but because A2 rejected the cell first and short-circuited before
`g7_conjunct` is reached** (`action_conjunct` returns at the page check,
`verifiers/check_scoped_rules_v32.py:1179-1182`). The arm passes for the wrong
reason. Verdict: **SURVIVED**.

**Not equivalent** — the mutant is observably weaker in composition. With SM5
(the cited-line check dropped) the landed arm 4 kills it; under the A2 wiring
SM5 survives the same 223 assertions:

```
landed  × SM5  exit=1  FAIL A2 G7: ... present in the cited line is not rejected ...
A2-wiring × SM5  exit=0  self-test: 0 failure(s) over 223 assertions
```

So arm 4's SM5-killing power is a property of the call site, not of the arm's
wording. §11's claim "arm 4 kills SM5" is true only for the `g7_conjunct`
wiring it uses.

### F2 — A5: deleting arms 2–3 leaves the suite green; only the count literal notices, and arms 2–3 are the sole killers of SM2/SM3

Deleting the two negative-witness checks yields `0 failure(s) over 221
assertions`, exit **0**, with all three behavioural predicate lines unchanged.
The frozen predicate still fails — because it names the literal
`self-test: 0 failure(s) over 223 assertions`, not because any assertion
detects the deletion. Substantively the loss is real, not cosmetic: with arms
2–3 gone, both floor/filter mutants survive

```
A5 × SM2  exit=0  0 failures / 221
A5 × SM3  exit=0  0 failures / 221
```

and arms 2–3 map one-to-one onto them (SM2's single FAIL line is arm 3's, SM3's
is arm 2's — see §3). Consequence for C1's receipt: the `219→223` count is a
**load-bearing guard** against arm deletion, not bookkeeping; any later
"assertion count updated" edit that keeps 0 failures would silently un-pin
SM2/SM3. [INFERENCE from the measured single-FAIL lists: arms 2–3 are the only
killers of SM2/SM3; arm 1/arm 4 deletion would similarly un-pin SM1/SM5.]

### F3 — A1 kills are real but self-referential

Each expectation flip is killed, at exactly 1 failure, **by its own arm only**.
So A1 proves no arm is a tautology (the asserted value is load-bearing), but it
cannot show the arms discriminate *the guard*; that evidence is A4/A6 (and
SM1/SM4/SM5/SM6). No mutant in this battery scored EQUIVALENT.

### F4 — A3: the fixture-substitution control goes red as declared; the well-formed variant is admissible

Replacing arm 1's fabricated span with a cited-line-supported span
(`` `glob syntax` ``) while keeping `expected True` turns arm 1 red
(`got False, expected True`) — the arm is bound to its fabricated fixture, so
the control behaves as declared. The well-formed variant (same substitution,
expectation `False`) is green at 223 assertions and is a genuine negative
control — but it is semantically arm 4's assertion (a supported span is not
rejected), so it adds wording robustness, not new coverage. I read the
ticket's "positive control — must pass" as *the control must behave as
declared*, and the declared reading is unambiguous only for A3a: a supported
span **cannot** satisfy arm 1 as written. Both measurements are above so either
reading is served.

### F5 — the arms kill all six §11 mutants on the reconstructed bytes

SM1←arm 1, SM2←arm 3, SM3←arm 2, SM4←world lines, SM5←arm 4 (under the landed
wiring), SM6←world lines + arms 2–4. This independently reproduces §11's
`landed_plus_spanfix7` kill table on bytes that are §11's check bodies verbatim.

---

## 5. Discrimination replicate — SM2 vs landed over 20 000 random cells

Two generators, both 20 000 cells, ~0.4 s each (no need for the 2 000-cell
fallback). Generator A: page = cited line + appendix; generator B: three page
modes (line+appendix / appendix only / paraphrased line), spans 1–3 words from
a mixed vocabulary (short non-stopwords `ox id url api …`, long content words,
≥4-char stopwords, invented words). Verdict difference = `bool(g7_conjunct)`
differs.

| metric | generator A | generator B | §11 reported |
|---|---|---|---|
| SM2 verdict divergence | **3 567 / 20 000 (17.8 %)** | **3 505 / 20 000 (17.52 %)** | 3 607 / 20 000 (18.0 %) |
| SM2 reverse (landed rejects, SM2 accepts) | **0** | **0** | — |
| SM2 divergence cells containing a ≥1 short unsupported non-stopword | — | **3 505 / 3 505 (100 %)** | — |
| both reject, different reason word-set | — | 5 721 (28.6 %) | — |
| SM3 verdict divergence | — | 2 166 (10.8 %) | — |
| SM5 verdict divergence | — | **192 (0.96 %)**, all with page ∌ cited line (appendix-only 132, paraphrased 60); **0** when page ⊇ line | — |

**Mechanism, exactly.** SM2 differs only on spans containing a word shorter
than 4 characters that is not a stopword and is unsupported by both the cited
line and the page — 3 505 of 3 505 divergent cells (and 0 cells outside that
class). SM2 is monotone: dropping a conjunct only widens `span_missing`, so it
never accepts where landed rejects (0/40 000 across both runs). §11's figure
(3 607) is **not exactly reproducible** — the generator is not recorded in §11 —
but two independent generators land within 1 % of it, so the "genuinely
different, not equivalent" conclusion holds. §11's named archetypes reproduce
verbatim:

```
SM2 `ox it`            landed []  | SM2 ['... span word(s) it, ox ...']
SM3 `because otherwise` landed [] | SM3 ['... span word(s) because, otherwise ...']
SM5 `mode quota`        landed [] | SM5 ['... span word(s) mode ...']   (page lacks "mode")
```

New structural detail on SM5: because `page_words` is built from the page and
the counter's real pages contain the cited line, SM5's rejection set is a
**superset of landed's only when the page omits a cited-line word**; measured
divergence is zero when the page is a superset of the cited line. SM5's
non-equivalence is therefore real but narrower than SM2's/SM3's — worth naming
in C1's bound.

---

## 6. Constructive hardening for arm 4 (one-word fixture edit, measured)

Move the page-absent word so it occurs **only inside the backticked span**:

```
- The tool writes mode quota nightly and `mode quota`.
+ The tool writes quota nightly and `mode quota`.
```

(`mode` then vanishes from `content_words(cell)`, so A2's page check passes and
the assertion actually exercises the G7 branch.) Measured:

```
HARDENED (landed bytes)              exit=0  0 failures / 223   sha ded23ac3d80d…1384
HARDENED × SM5  (g7 wiring)          exit=1  FAIL A2 G7: ... present in the cited line ... got True, expected False
HARDENED × A2 wiring                 exit=0  0 failures / 223
HARDENED × A2 wiring × SM5           exit=1  FAIL A2 G7: ... present in the cited line ... got True, expected False
```

i.e. under the hardened fixture arm 4 kills SM5 **under either call site**, which
closes F1's consequence. Recommendation: land arm 4 with this cell (same name,
same expectation, 223 assertions, all prior lines unchanged) or state F1 in
C1's bound as an accepted coverage limit.

---

## 7. Claims supported / falsified

- **C1 "the four arms turn all six `span_missing` mutants red" — SUPPORTED**
  on the reconstructed bytes (SM1–SM6 all exit 1 with the declared FAIL lines,
  §3/F5), and no committed-row verdict changed (`eligible rows pass 4 of 4` in
  every run).
- **C1 "the arms append to the existing suite; nothing is rewritten" —
  SUPPORTED**: the three other predicate lines are identical in every run;
  exactly +4 assertions (219→223).
- **C1 "223 assertions" — SUPPORTED** as the count, and F2 adds a reason it
  matters: the count is the only detector of arm deletion.
- **C1 "arm 4 kills SM5" — PARTIALLY FALSIFIED**: true under the landed
  `g7_conjunct` wiring, false under `action_conjunct` (A2-survival, A2×SM5
  survival). The claim's wording should either name the call site or the arm
  should adopt the §6 fixture.
- **§11's non-equivalence note — CORROBORATED**, with SM5's divergence
  condition quantified (page must omit a cited-line word) and SM2's divergence
  class proved exact over 40 000 cells.
- **§11's 20 k figure 3 607 — not exactly reproducible** (generator unrecorded);
  17.52 %–17.8 % independently, same order and same mechanism. Label the
  round-63 number as generator-specific if cited again.

---

## 8. Restoration and bounds evidence

- **Restore discipline:** every scored run (18 in the final capture block plus
  the earlier scoring, A5 and hardening runs) rewrote the scratch counter from
  `arms_pristine.py` afterwards and asserted
  `sha256 == 7791504715f308e2cedf4f9cc746ae08d513a3dc01861b4afe1fb2a84911cda2`;
  the final harness line printed
  `=== restore verified: scratch v32 sha 7791504715f3…`. No run left a mutant
  in place.
- **Lane untouched by this seat:** `verifiers/check_scoped_rules_v32.py` in the
  lane still hashes `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`
  (145577 bytes) after all work. `git status --porcelain` carried the dispatch
  entries (`M .ufo/waves/round-63/w2/MutW2SplitClauses.md`,
  `?? w1-dispatch.{err,json}`, `?? w1-spec.json`, `?? w1/`) throughout; by my
  final check it had additionally gained `M plans/round-64.md` and
  `?? .ufo/waves/round-64/snapshots/` from concurrent seats (not written by me;
  recorded as observed, not as my change). My only lane write is this report.
  The scratch clone was created
  with `git clone --no-hardlinks` so no lane object/index was touched and no
  hardlink can write back.
- **No tooling installed** (stdlib `python3` 3.14.8, `git` read paths only);
  nothing to record under the tooling directive.
- Scratch retained for audit: `/tmp/mutspan64/{base.py,arms_block.txt,arms_pristine.py,mutants/*.py,final_runs.txt,tree/}`.

## 9. Reproduction (exact anchors)

- arm block: `MutW2V32.md` lines 937–966, sha `5900a62a…`, inserted before
  `        # -- the counter's own sha256 (v2) --------------------------------`
  in the base bytes.
- A1: within each arm's `check(...)` slice, replace the final `, True)` ↔
  `, False)` (arm slices start at their `check("A2 G7: …"` markers).
- A2: within arm 4's slice, `named(g7_conjunct(` → `named(action_conjunct(`.
- A3: within arm 1's slice, `` `exfiltrates credentials` `` → `` `glob syntax` ``
  (A3b additionally flips that arm's trailing `, True)` → `, False)`).
- A4: `if len(word) >= 4 and word.lower() not in STOPWORDS` →
  `if word.lower() not in STOPWORDS`.
- A6: `if len(word) >= 4 and word.lower() not in STOPWORDS` → `if len(word) >= 4`.
- A5: delete the slices from arm 2's `check(` marker to arm 4's `check(` marker.
- Run: `cd /tmp/mutspan64/tree && python3 -B verifiers/check_scoped_rules_v32.py --self-test`.

No judgement on landing, no integration, no other runtime invoked.

Report: .ufo/waves/round-64/w1/MutSpanArms.md
