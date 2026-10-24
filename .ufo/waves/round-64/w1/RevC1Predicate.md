# RevC1Predicate — C1 predicate attack (round 64, wave 1)

role: reviewer (leaf; no subagent dispatch)
item: attack the C1 frozen predicate of `plans/round-64.md` and answer four
questions with receipts: (1) can the four-line predicate be satisfied by a
counter that does not pin the branch; (2) is `0 failure(s) over 223 assertions`
freeze-safe; (3) do SM4/SM6 plus the four new arms leave a `span_missing` lane
unpinned; (4) is arm 4's direct `g7_conjunct` call semantically different from
the `action_conjunct` wrapper.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base tip `078eec4`,
lane HEAD at review time `c04fffbe` (plan freeze). **The lane was not
written**; the only file this seat creates is this report.
Tooling: **nothing installed or upgraded** (stdlib `python3` only; no pacman,
no uv, no npx — the host-wide pacman pause was respected by not touching it).
Scratch: `/tmp/revc1` (disposable): `git archive c04fffbe | tar -x -C
/tmp/revc1/tree` gives a byte-identical, isolated lane tree; every variant is a
`verifiers/check_scoped_rules_v32.py` replacement inside that tree and the
frozen command is run from it.

## 0. Canonical bytes this review measures

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD
c04fffbeafcaf810897258d56f99cca736ed3a91
$ git show 078eec4:verifiers/check_scoped_rules_v32.py | sha256sum
12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43  -
$ git show HEAD:verifiers/check_scoped_rules_v32.py | sha256sum
12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43  -
$ cd /tmp/revc1/tree && python3 -B verifiers/check_scoped_rules_v32.py --self-test | tail -1
self-test: 0 failure(s) over 219 assertions          # exit 0
```

The verifier bytes are identical at `078eec4` and `HEAD`, so C1 control (c)
("the predicate command at base `078eec4` prints `219 assertions`") is true at
both revisions. Landing the four arms (byte-exact `MutW2V32.md` §11 package)
on those bytes gives, on my own copy:

```
sha256 d61c3eda67a0311fe9bf1d287dce2fb33f11e624294b6cbed1ec262e1089fc1f
self-test: 0 failure(s) over 223 assertions          # exit 0, no FAIL lines
```

**Independent re-derivation of the §11 matrix at 219** (my run, not a citation):

```
SM1_branch_removed       exit=0 self-test: 0 failure(s) over 219 assertions   SURVIVES
SM2_floor_dropped        exit=0 self-test: 0 failure(s) over 219 assertions   SURVIVES
SM3_stopwords_dropped    exit=0 self-test: 0 failure(s) over 219 assertions   SURVIVES
SM4_page_check_dropped   exit=1 FAIL eligible world: the four counted rows are backed: got ['Claude Code', 'VS Code'], expected ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']
SM5_line_check_dropped   exit=0 self-test: 0 failure(s) over 219 assertions   SURVIVES
SM6_always_fires         exit=1 FAIL A2: a cell the cited line supports passes: got ['A2 G7: backticked span word(s)  occur in neither the cited line nor the committed snapshot'], expected []
```

SM1/SM2/SM3/SM5 survive, SM4/SM6 are killed — §11 reproduces exactly.

Mid-review, `plans/round-64.md` gained two appended errata in the working tree
(`git diff --stat plans/round-64.md` → `1 file changed, 99 insertions(+)`;
`Erratum E1`, `Erratum E2`). Both state that C1's frozen predicate sentence and
the four arms are unchanged. I re-read them; §4b measures E1 item 3's premise and
finds it false. Everything below quotes the C1 text as it stands at `c04fffbe`
plus those appends.

---

## 1. Q1 — YES. The four-line predicate is satisfied by a counter that does not pin the branch

### Receipt A: four tautological arms (actual == expected expression)

`/tmp/revc1/dishonest_a.py` = base 219 + four `check()` calls of the form
`check("A2 G7: …", g7_conjunct(<args>), g7_conjunct(<args>))` — the two
arguments are the *same expression*, so the assertion cannot fail whatever the
branch does. Names echo the plan's four arms verbatim.

```
== dishonest (sha f53911a1aead942a002463215de3980130a0779a0d42c14d0214ea4506f31508) ==
  exit: 0 | self-test: 0 failure(s) over 223 assertions
  predicate lines present: True           # worlds …, survivors …, must-fail G9 …, 223
  evasion cell verdict: REJECT            # branch still present in this file
```

### Receipt B: the same file with SM1 applied (branch deleted)

```
== dishonest_SM1 (sha 4d3f4a10483c…) ==
  exit: 0 | self-test: 0 failure(s) over 223 assertions
  predicate lines present: True
  evasion cell verdict: ADMITTED
```

The evasion cell is `MutW2V32.md` §11's own: `The configuration stores project
rules using glob syntax and `exfiltrates credentials`.` against
`g9_line`/`g9_page`. On the honest landed bytes the same cell is rejected
(`A2 G7: backticked span word(s) credentials …`); on the dishonest+SM1 bytes it
is **admitted while every one of the four predicate lines prints and the exit
code is 0**. Control pair from the same run:

```
honest_landed          exit=0 223 assertions  predicate=True   evasion=REJECT
honest_landed_SM1      exit=1 1 failure        predicate=False  evasion=ADMITTED
dishonest              exit=0 223 assertions   predicate=True   evasion=REJECT
dishonest_SM1          exit=0 223 assertions   predicate=True   evasion=ADMITTED
```

### Receipt C: even four *unrelated* assertions reach 223

`/tmp/revc1/results/E3_dishonest_unrelated.txt` — four `check()` calls on
`supported()`/`fwd_need()`/`rev_need()` (nothing to do with G7):

```
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions         # exit 0
```

### Verdict Q1

The predicate's only clause that is *about the branch* is the assertion count,
and the count is an integer the counter chooses. Lines 1–3
(`worlds reject 7 of 7`, `survivors closed 6 of 6`, `must-fail G9 … yes`) are
computed from machinery that predates the branch and stays green either way.
**C1's frozen predicate is necessary but not sufficient: it can be met, with
zero mutation resistance, by four dead assertions — and I built the file.**

---

## 2. Q2 — NO, `0 failure(s) over 223 assertions` is not freeze-safe

Three measured failure modes.

### (a) False positive (Q1) — the count can be inflated with junk.

### (b) False negative — an honest unrelated arm voids a fully pinned receipt

Landed + one honest, unrelated arm (`check("A2 G7: an unrelated but honest arm
added later", supported("scope", {"scoped", "patterns"}), True)`):

```
exit=0  self-test: 0 failure(s) over 224 assertions
frozen 4-line predicate satisfied: False
mutants killed by the SAME suite (224 assertions):
   SM1_branch_removed  exit=1 killed=True
   SM2_floor_dropped   exit=1 killed=True
   SM3_stopwords_dropped exit=1 killed=True
   SM4_page_check_dropped exit=1 killed=True
   SM5_line_check_dropped exit=1 killed=True
   SM6_always_fires    exit=1 killed=True
```

The guard is fully pinned; the predicate says "no". Any future honest assertion
(including the closing arms in §3) silently voids the receipt and forces a
re-freeze — the predicate is a **count lock, not an evidence lock**.

### (c) The C2 check-4 idiom cannot certify this count

C2 check 4 counts `check(` invocations. Here the printed count is not the call
count — traced with `sys.settrace` on the landed bytes:

```
self-test: 0 failure(s) over 223 assertions
total check calls 223
  ('run_world', 2595) x 6        # one check() inside run_world, once per world
  ('self_test', 2897) x 3        # g9_probes loop, three probes
static `check(` sites in self_test(): 217
```

`check(` appears 217 times in the file and fires 223 times. A static-count
equality check (the `check_r63_routed_repairs.py` check-4 pattern) is off by six
here and must not be reused for C1.

### Wording guard (recommended, adopt verbatim)

Replace the predicate's fourth line with a *pair* plus a kill-rule conjunct,
and keep the count out of the load-bearing position:

```
python3 -B verifiers/check_scoped_rules_v32.py --self-test
  exit 0, and these lines are present:
    worlds reject 7 of 7; eligible rows pass 4 of 4
    survivors closed 6 of 6
    must-fail E2e guard disabled admits e2e-negated-path-key: yes
    must-fail G7 disabled admits e2f-backticked-event-claim: yes
    must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
    counter sha256 <S>  with <S> = sha256 of the committed file at <rev>
    self-test: 0 failure(s) over <N> assertions
  where (<S>, <N>) is the receipt's pinned PAIR: <S> is recomputed from
  `git show <rev>:verifiers/check_scoped_rules_v32.py | sha256sum`, never read
  from the printed line, and <N> is accepted only together with <S>.
  AND the kill conjunct: each of SM1..SM6 (and each closing lane M7/M8/M9/
  M10/M12/M17 from §3) applied to the committed bytes at <rev> makes the same
  command exit nonzero with a FAIL line naming that mutant's target.
```

Two properties this buys: an honest extra arm moves `<S>` and `<N>` together
and the receipt is *known* stale instead of *falsely* failed; and a dishonest
four-assertion counter cannot satisfy the kill conjunct at all, because SM1
still survives. The self-test already prints its own sha256 line (self-computed),
so **it is not evidence**: the sha must be recomputed from committed bytes by
the receipt/counter, otherwise a mutant that keeps the branch can print the
constant.

Add the missing anti-shrink gate in the same commit: `check_scoped_rules_v32.py`
has **no row in `verifiers/floors-registry.json`** (`grep -n check_scoped
verifiers/floors-registry.json` → nothing; `grep -c scoped
verifiers/check_assertion_floors.py` → 2, both prose in the docstring). This is
the r62 F17 debt verbatim ("deleted self-test arms are invisible to the floor
guard … the smallest fix is an assertion-count line plus registry rows — v31
already prints `201 assertions` and only needs the row"). v32 already prints the
count line, so C1 needs the registry row at the landed count (223, or 229/230 if
the §3 closing arms are adopted). Without it the four arms can be deleted later
with every gate green; with it, deletion fails loudly. A floor row is a lower
bound — it catches deletion, not inflation — so it is complementary to the kill
conjunct, not a substitute.

---

## 3. Q3 — YES: six verdict-flipping `span_missing` lanes survive SM4/SM6 plus the four arms

Re-derived from the committed branch (`v32:1055-1063`) and measured on the
landed 223-assertion suite. "Verdict" is `action_conjunct(...)` REJECT/ADMIT
through the wrapper with a real `page_text`; witnesses are in
`/tmp/revc1/p_*.py` and `results/landed_*.txt`.

| lane | mutation | witness (cell · line · page) | landed vs mutant | status on 4 arms |
|---|---|---|---|---|
| **M8** floor `>=4`→`>=5` | `if len(word) >= 5` | `…and `zeta quota`.` · line has quota · page lacks zeta | REJECT (span `zeta`) vs **ADMIT** | **SURVIVES — evasion** |
| **M12** line check uses `page_words` | `word.lower() not in page_words(raw_line)` | `…and `zeta quorum`.` · line `` The tool writes `zeta` quorum nightly. `` · page lacks zeta | REJECT vs **ADMIT** | **SURVIVES — evasion** |
| **M7** floor `>=4`→`>=3` | `if len(word) >= 3` | `…and `zap quota`.` | ADMIT vs REJECT | SURVIVES — false reject |
| **M9** `.lower()` dropped on STOPWORDS | `word not in STOPWORDS` | `…and `Because only`.` | ADMIT vs REJECT | SURVIVES — false reject |
| **M10** `.lower()` dropped on the line set | `word not in content_words(raw_line)` | `…and `Mode quota`.` · line has `Mode` · page lacks mode | ADMIT vs REJECT | SURVIVES — false reject |
| **M17** prefix support → exact match | `word.lower() not in page_words(raw_page)` | `…and `scope rules`.` · page has `scoped` | ADMIT vs REJECT | SURVIVES — false reject |
| M11 `.lower()` dropped on the page set | `supported(word, …)` | `…and `ZETA quota`.` | same verdict, extra G7 reason | SURVIVES — diagnostic only |
| M14 wrapper drops `page_text` | `g7_conjunct(lines, cell, L)` | `…and `zeta quorum`.` with zeta only later on the page | same verdict (G9 rejects first) | SURVIVES — diagnostic only |
| M20 page set `page_words`→`content_words` | `content_words(raw_page)` | span word supported on the page only inside backticks | same verdict (G9 rejects first) | SURVIVES — diagnostic only |
| M18 message priority (`missing` vs `span_missing`) swapped | message only | — | — | SURVIVES — cannot fire with a single-span cell |
| M19 `sorted({…})`→`list({…})` | message word order becomes hash-seed dependent | — | — | SURVIVES — determinism, not semantics |
| M22 `g7_conjunct` L-guard weakened | `if L is None:` | — | unreachable: `action_conjunct` bounds L before the call | SURVIVES — equivalent in context |

Kill lines on the landed suite for the six lanes it does kill:

```
SM1 exit=1 FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
SM2 exit=1 FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False
SM3 exit=1 FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
SM4 exit=1 FAIL eligible world: the four counted rows are backed: got ['Claude Code', 'VS Code'], expected [...]
SM5 exit=1 FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
SM6 exit=1 FAIL A2: a cell the cited line supports passes: got ['A2 G7: backticked span word(s)  occur in …'], expected []
```

**Attribution caveat:** SM4 and SM6 are killed by *pre-existing* arms
(`eligible world: the four counted rows are backed`, `A2: a cell the cited line
supports passes`), not by any of the four new arms. A receipt that presents
"the SM1–SM6 battery is red" as evidence for the four arms must say which arms
do the killing, or it credit-claims twice. (§11 quoted the world FAIL for SM6;
my first-failing assertion is the A2 one. Both are red — only the quoted line
differs.)

**The two evasion lanes are the finding that matters.** M8 admits a fabricated
four-character span word; M12 admits a span word whose only "presence" on the
cited line is inside another backticked span. Both are the same class as SM1
(admission of a fabrication), and the plan's bound ("the four measured lanes")
does not name them.

A 4000-cell random sweep (crude generator: single spans, line == page) diverged
only on M7 (12/4000) and M8 (1/4000) and never on the case/prefix lanes — the
sweep under-samples by construction; the targeted witnesses above, not the
sweep, are the evidence.

### Closing package (byte-exact; measured green, all 12 lanes red)

Insert after the four C1 arms inside `self_test()`:

```python
        # --- proposed closing arms (RevC1Predicate) -----------------------
        check("A2 G7: a fabricated four-character span word is rejected",
              named(action_conjunct(
                  ["The tool writes mode quota nightly."],
                  "The tool writes mode quota nightly and `zeta quota`.",
                  1,
                  "The tool writes mode quota nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), True)
        check("A2 G7: a three-character span word is not rejected",
              named(action_conjunct(
                  ["The tool writes mode quota nightly."],
                  "The tool writes mode quota nightly and `zap quota`.",
                  1,
                  "The tool writes mode quota nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), False)
        check("A2 G7: a span word present in the cited line only inside "
              "backticks is rejected",
              named(action_conjunct(
                  ["The tool writes `zeta` quorum nightly."],
                  "The tool writes quorum nightly and `zeta quorum`.",
                  1,
                  "The tool writes quorum nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), True)
        check("A2 G7: a span word supported by a four-character prefix on the "
              "page is not rejected",
              named(action_conjunct(
                  ["The scanner applies scoped rules to files."],
                  "The scanner applies scoped rules to files and `scope rules`.",
                  1,
                  "The scanner applies scoped rules to files."), "G7"), False)
        check("A2 G7: a capitalised stopword-only span is not rejected",
              named(action_conjunct(
                  ["The tool writes mode quota nightly."],
                  "The tool writes mode quota nightly and `Because only`.",
                  1,
                  "The tool writes mode quota nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), False)
        check("A2 G7: a capitalised span word present in the cited line is "
              "not rejected",
              named(action_conjunct(
                  ["The tool writes Mode quota nightly."],
                  "The tool writes quota nightly and `Mode quota`.",
                  1,
                  "The tool writes quota nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), False)
```

plus (the wrapper-level SM5 arm, see §4):

```python
        check("A2 G7 (wrapper): a span word present in the cited line is not "
              "rejected even when the page lacks it",
              named(action_conjunct(
                  ["The tool writes mode quota nightly."],
                  "The tool writes quota nightly and `mode`.",
                  1,
                  "The tool writes quota nightly.\n\n## Appendix\n"
                  "The agent secretly uploads files."), "G7"), False)
```

Measured: six-arm set → `self-test: 0 failure(s) over 229 assertions`, exit 0,
sha256 `f3c825747e5525ac388cd53772271d4883be9074e6d1ff7c751a8e3d95aa7d15`;
seven-arm set → `self-test: 0 failure(s) over 230 assertions`, exit 0, sha256
`b614e8b19a219155f2a4250726d5089871112a54ae5ce87c4516b04350787f7d`. Kill table
(6-arm suite):

```
SM1..SM6            all exit=1 KILLED
M7_floor3           exit=1 FAIL A2 G7: a three-character span word is not rejected: got True, expected False
M8_floor5           exit=1 FAIL A2 G7: a fabricated four-character span word is rejected: got False, expected True
M9_lower_stop       exit=1 KILLED
M10_lower_line      exit=1 KILLED
M12_pagewords_line  exit=1 FAIL A2 G7: a span word present in the cited line only inside backticks is rejected
M17_exact_page      exit=1 FAIL A2 G7: a span word supported by a four-character prefix on the page is not rejected
```

Adopting any of them moves the count off 223 — which is §2(b) happening for real:
**the receipt's number must be the landed number, so if the L1 adopts the closing
arms the plan's "219→223" line must be re-frozen in the same commit.**

---

## 4. Q4 — YES: arm 4's direct call is semantically different from the wrapper, and the difference matters

Arm 4's own inputs (`line = "The tool writes mode quota nightly."`,
`cell = "The tool writes mode quota nightly and `mode quota`."`,
`page = "The tool writes quota nightly.\n\n## Appendix\nThe agent secretly
uploads files."`) through both entry points, on the landed module:

```
g7_conjunct   -> []
action_conj   -> ['A2: action word(s) mode do not occur on the committed snapshot']
named(...,'G7') on the wrapper result -> False
named(...,'G7') on the direct result  -> False
```

The wrapper rejects **before** G7, at A2's page-containment gate, because the
un-backticked occurrence of `mode` in the cell is a content word the page lacks.
So on arm 4's inputs no `judge()` path ever reaches the cited-line exemption the
arm asserts: arm 4 is a **unit test of `g7_conjunct`**, not a pin on the counter's
behaviour, and its name ("a backticked span word present in the cited line is not
rejected even when the page lacks it") reads like an end-to-end guarantee that
the wrapper does not provide.

SM5 is nevertheless end-to-end observable — via a *different* cell, where the
span word occurs in the cell only inside backticks:

```
cell: The tool writes quota nightly and `mode`.   (line has `mode`, page does not)
  landed action_conjunct -> []                                   (ADMIT)
  SM5    action_conjunct -> ['A2 G7: backticked span word(s) mode occur in …']  (REJECT)
  SM1    action_conjunct -> []
```

So arm 4 is a valid SM5 killer (it is the only one in the four), but it is the
weakest possible form of it: it cannot catch wrapper wiring that changes which
page the branch sees (M14), the page-set construction (M20), or the support
predicate (M17) — this is exactly why those three lanes survive §3. **Recommend:
keep arm 4, rename it with an explicit `g7_conjunct unit:` prefix, and add the
wrapper-level SM5 cell above as its end-to-end counterpart.**

### 4b. The current plan's Erratum E1 item 3 contradicts this measurement

While this seat was running, `plans/round-64.md` gained (working tree, +99 lines)
an "Erratum E1 (pre-data)" whose item 3 reads:

> `CriticC1Bound` showed the full `judge()` path derives lines from the page,
> making the cited-line filter redundant for reachable judge inputs; arm 4's
> witness is a direct `g7_conjunct` call per MutW2V32 §11.

The premise is **false as stated**, and my Receipt Q4b is the counterexample:
for a cell whose span word occurs *only* inside backticks, the wrapper is
reachable at the filter and the verdict flips (landed ADMIT / SM5 REJECT). The
filter is redundant only when the same word also occurs unbackticked in the
cell, in which case A2's page gate rejects first (that is what arm 4's own
inputs show). The accurate sentence is: "the cited-line filter is masked by
A2's page gate whenever the span word also appears verbatim in the cell; for
backticked-only words it is judge-reachable and load-bearing."

Consequence for the erratum's disposition ("C1's Bound records that SM5's pin
is component-level, not a judge-level evasion lane"): the pin need not stay
component-level — the wrapper-level arm in §3 pins it at the level the judgment
actually runs, at the cost of one assertion. The rest of the erratum ("the four
arms and the 223-assertion predicate are unchanged") is exactly the freeze
problem §2 measures; it does not fix F3.

---

## 5. Findings by severity

**F1 (critical, C1 as worded: falsified).** The frozen four-line predicate is
satisfied by a counter that does not pin the branch (`dishonest_SM1`: 223
assertions, exit 0, all four lines, documented evasion ADMITTED). The predicate
must gain the kill conjunct in §2; the count alone is not evidence.

**F2 (high, C1 as worded: partially falsified).** The four arms leave six
verdict-flipping lanes, two of them admission-flipping (M8 four-character
fabricated span word; M12 span word "present" only inside another backticked
span). The claim "arms 2–4 pin the floors and filters" is true only for "a floor
exists and is >2" and "the filter exists" — not for the floor's value (pinned
only in `(2, 11]`), nor for case-folding, nor for the support predicate.
Closing package in §3 (measured green, all 12 lanes red).

**F3 (high, C1 receipt).** `0 failure(s) over 223 assertions` is neither
necessary nor sufficient for the claim: an honest extra arm voids it with the
branch fully pinned (224, six mutants still red), and four dead assertions
satisfy it. Pin `(sha256, N)` as a pair *and* the kill set.

**F4 (medium, C1 receipt mechanics).** The printed count is not the `check(`
site count (217 sites, 223 firings: `run_world` ×6, `g9_probes` ×3). Reusing C2
check 4's static-count idiom for C1 will disagree by six.

**F5 (medium, C1 integration).** Landing 223 without amending the live corpus
sentences ships a stale count in the same round that closes the stale-citation
class: `corpus/knowledge/compound-clause-citation-round63.md:120`
("`self-test: 0 failure(s) over 219` in its `## Verification` block) and
`corpus/README.md:112` ("`../verifiers/check_scoped_rules_v32.py --self-test`,
219 assertions"). Both must be amended (or explicitly revision-pinned) in the
landing commit.

**F5b (medium, C1 durability).** `check_scoped_rules_v32.py` has no row in
`verifiers/floors-registry.json` (verified: `grep -n check_scoped
verifiers/floors-registry.json` → no match; the two `scoped` hits in
`check_assertion_floors.py` are docstring prose). This is the r62 F17 debt
exactly. Nothing pins 219, which is why the stale sentences above survive — and
nothing would catch the four arms being deleted later: the self-test would print
`0 failure(s) over 219 assertions`, every gate green, the branch unpinned again.
Register the instrument at the landed count in the same commit.

**F6 (low, predicate wording).** The plan says the command "prints all four
lines"; it prints 21 non-blank lines, including **three** must-fail lines
(`E2e`, `G7`, `G9`), of which the predicate names only the G9 one. A verifier
reading "all four lines" as a full-output diff fails; as a subset check it
passes. The receipt should say "prints these lines among others" and should add
the E2e line (computed, free). Exact observed block:

```
counter sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 219 assertions
```

**F7 (low, determinism).** `sorted({…})` → `list({…})` survives; the G7 message
word order then depends on the hash seed, so any receipt that greps the exact
`A2 G7: backticked span word(s) …` text is flaky. Arm 1 asserts the reason's
presence (`named(...,"G7")`), never its text. If the control (b) receipt quotes
the FAIL line, that coupling should be pinned by asserting the message string.

**F8 (informational).** `g7_conjunct`'s own `L` bounds guard is unreachable
through `action_conjunct` (which bounds `L` first). With arm 4 establishing a
direct-call contract, that guard becomes contract surface — either pin it with a
direct-call arm (`L=7` → `[]`, as the dishonest variant accidentally did) or
delete it. Today it is an unpinned, unreachable line.

**F9 (high, plan erratum).** Erratum E1 item 3's premise ("the cited-line filter
[is] redundant for reachable judge inputs") is contradicted by a measured
wrapper-level witness (Receipt Q4b: landed ADMIT / SM5 REJECT for a
backticked-only span word). The erratum will be landed pre-data as a verified
correction; it should be amended before the plan freeze is treated as final, and
C1's Bound should not record a component-level-only pin when one extra arm pins
it at judge level.

## 6. Claim mapping

- **C1's "the four arms land and turn SM1–SM6 red"**: *supported* — reproduced
  on my own bytes (223, exit 0, six red).
- **C1's "the `span_missing` branch is pinned"**: *falsified as stated* — six
  lanes, two admission-flipping, survive (F2).
- **C1's frozen predicate as a freeze token**: *falsified* — satisfiable without
  pinning (F1) and voidable by an honest arm (F3).
- **Plan Erratum E1 item 3** ("SM5's filter is redundant for reachable judge
  inputs"): *falsified* — see Receipt Q4b and F9.
- **C2** untouched by this review.

## 7. Residual risk and verification gaps

- My divergence sweep is a weak generator (identical line/page, lowercase single
  spans). The lane counts for the case/prefix lanes rest on targeted witnesses,
  not on sampling; a real generator (multi-span cells, page ≠ lines, capitalised
  tokens) would likely find more lanes, not fewer. [INFERENCE]
- I did not mutate the *identifier* branch (`BACKTICKED_IDENTIFIER_RE` / the
  `missing` path) or the A2 fraction machinery; C1's bound excludes them, and
  they remain unmeasured here.
- I did not run `judge()` against the committed rows on the closing package; the
  four arms and the closing arms are pure `action_conjunct`/`g7_conjunct` calls,
  so the "4 of 4 backed" line is untouched by construction — but the L1's
  own "landed bytes print `4 of 4`" receipt must be re-run after landing.
- The closing arms' witnesses depend on `MIN_CONTENT = 3`, `SUPPORT_PREFIX = 4`
  and `STOPWORDS` membership (`because`, `otherwise`, `only`); a future change to
  any of those changes the arms' expected verdicts. That coupling is inherent to
  this style of arm and should be named in the lesson.
- All measurements are at `c04fffbe`/`12d093a1…`; nothing here certifies a later
  revision.
