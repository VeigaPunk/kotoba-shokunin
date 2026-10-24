# MutW2M7M22 — mutation spot-check of RevC1Predicate's M7–M22 lanes (round 64, wave 2)

role: mutation-tester (leaf; no subagent dispatch)
item: spot-check RevC1Predicate's M7–M22 lanes against the **landed** bytes at
`c019919c`; construct M8 and M12 and test each for admission-flipping **through
`judge()`** (not only through `action_conjunct`); apply the seat's closing
package (6 arms → 229; +wrapper arm → 230) and verify the lanes close.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` — **read-only outside this
report**; no git/jj writes; all mutation in `/tmp/mutw2` (disposable).
Tooling: **nothing installed or upgraded** (stdlib `python3` 3.14.8 only; the
host-wide pacman pause was respected by not touching it).

## 0. Bytes measured

```
$ git -C …/kotoba-shokunin rev-parse HEAD
b99fb79c27042e0f8a598cbbb4d81479a806b518          # r64 measurements commit
$ git show c019919c97ab5fe98e87a7754b4449ea4e699c99:verifiers/check_scoped_rules_v32.py | sha256sum
f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d  -   # the landed v32
$ sha256sum verifiers/check_scoped_rules_v32.py      # lane on disk, untouched
f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
$ cd /tmp/mutw2/tree && python3 -B verifiers/check_scoped_rules_v32.py --self-test
self-test: 0 failure(s) over 223 assertions          # exit 0
```

`/tmp/mutw2/tree` = `git archive c019919c | tar -x`; its verifier hashes to the
same `f8f69cad…`, so every mutant below is one exact string replacement in a
byte-identical copy of the landed instrument. Baseline green at 223 — no
baseline failure, so every kill/survival below is attributable.

## 1. The probe had to be a `judge()` probe, and that changes the lane map

RevC1Predicate measured `action_conjunct(lines, cell, L, page_text)` with
`lines` and `page_text` supplied independently (its witnesses put a line in
`lines` that the page does not contain). `judge()` does not work that way:

```
v32:1543-1556 (entry_row_verdict)   page = data.decode(...); lines = page.splitlines()
v32:1556                             action_conjunct(lines, action_cell, action_line, page)
```

The cited line is **a line of the page**, so `page_words(page) ⊇
content_words(line)` for every reachable call. That makes several of the seat's
"line vs page" lanes equivalent under `judge()`, and it is exactly the class the
assignment asks me to test.

Probe harness (`/tmp/mutw2/harness.py`): import the landed module, `exec` its
own `self_test()` fixture builders (`QUOTES/PAGES/ACTIONS/KEYS/…`,
`skill_text`, `entry_text`, `sources_text`, `lesson_text`, `base_rows`,
`sources_text`) extracted verbatim from the module source, then call
`judge(skill, entry, sources, lesson, base_sources,
snapshot_of=lambda sid: pages[sid].encode(), intro_of=lambda sid: None)` with
S900's action cell = the witness cell, S900's snapshot = the cited line at line
5 followed by the appendix. Control (proves the harness is wired like the
self-test's eligible world, not a broken call):

```
stock fixture backed: ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']   # exit 0
```

## 2. Per-lane verdicts on the landed bytes (judge level)

Witness construction: cited line = page line 5; appendix = extra page lines.
`landed → mutant` is `row["backed"]` from `judge()`.

| lane | judge-level landed → mutant | judge-reachable? | verdict on landed bytes |
|---|---|---|---|
| **M8** floor 4→5 | REJECT `A2 G7: … span word(s) zeta` → **backed=True** | **YES** | **REAL admission lane; confirmed at judge level** |
| M7 floor 4→3 | backed=True → REJECT `… span word(s) zap` | YES | verdict-flipping (over-rejection) |
| M9 `.lower()` off STOPWORDS | backed=True → REJECT `… span word(s) Because` | YES | verdict-flipping (over-rejection) |
| M17 prefix→exact on page | backed=True → REJECT `… span word(s) scope` | YES | verdict-flipping (over-rejection) |
| M20 page set `page_words`→`content_words` | backed=True → REJECT `… span word(s) zeta` | **YES** (single-word backticked span on the page, below G9's `MIN_CLAUSE`) | **verdict-flipping — the seat's "diagnostic only" is wrong** |
| **M12** line set `content_words`→`page_words` | REJECT `A2 G9: clause … supported outside the cited line` → **same G9 REJECT** | **NO — equivalent** | component-only; not an evasion through `judge()` |
| M10 `.lower()` off the line set | backed=True → backed=True | NO — equivalent (page contains the cited line's case-insensitively folded words) | component-only |
| M14 wrapper drops `page_text` | backed=True → backed=True | NO — equivalent (`"\n".join(lines)` is the page modulo a trailing newline) | component-only, but see §4 |
| M11 `.lower()` off the page set | REJECT (G9) → REJECT (G7+G9), **same verdict** | verdict unchanged | diagnostic only (matches the seat) |
| M22 `L`-guard weakened | — | unreachable (`action_conjunct` bounds L first) | equivalent |
| M18/M19 | message text/order only | — | verdict-neutral |

Receipts (verbatim, one line per probe):

```
M8   landed       backed=False why=['… A2 G7: backticked span word(s) zeta occur in neither the cited line nor the committed snapshot']
M8   M8_mutant    backed=True  why=[]
M12  landed       backed=False why=['… A2 G9: clause "`zeta quorum`. (SS900 :5)" is supported outside the cited line']
M12  M12_mutant   backed=False why=['… A2 G9: clause "`zeta quorum`. (SS900 :5)" is supported outside the cited line']
M7   landed       backed=True  why=[]      | M7_mutant  backed=False why=['… span word(s) zap …']
M9   landed       backed=True  why=[]      | M9_mutant  backed=False why=['… span word(s) Because …']
M17  landed       backed=True  why=[]      | M17_mutant backed=False why=['… span word(s) scope …']
M10  landed       backed=True  why=[]      | M10_mutant backed=True  why=[]
M20  landed       backed=True  why=[]      | M20_mutant backed=False why=['… span word(s) zeta …']
M11  landed       backed=False (G9 "`Zeta quota`… supported outside the cited line")
M11  M11_mutant   backed=False (G7 "span word(s) Zeta …" + the same G9)  # same verdict, extra reason
M14  landed       backed=True  why=[]      | M14_mutant backed=True  why=[]
```

Witnesses (page = cited line at line 5 + appendix; cell is S900's action cell):

- M8: `` The tool writes mode quota nightly and `zeta quota`. `` / line
  `The tool writes mode quota nightly.` / appendix `The agent secretly uploads files.`
- M12: `` The tool writes quorum nightly and `zeta quorum`. `` / line
  `` The tool writes `zeta` quorum nightly. `` / same appendix
- M9: `` … and `Because only`. `` · M10: `` … and `Mode quota`. `` with line `… writes Mode quota …`
- M17: `` The scanner applies scoped rules to files and `scope rules`. ``
- M20: `` The tool writes mode quota nightly and `zeta`. `` with page line 7
  `` The `zeta` appendix sentence. `` (single content word in the clause → G9's
  `MIN_CLAUSE = 2` skips it, so the span branch is the only gate)

Component-level controls on the seat's exact inputs reproduce its table exactly
(`M8`/`M12` REJECT→ADMIT; `M7`/`M17` ADMIT→REJECT via direct
`action_conjunct` with `lines` ⊄ page). So the seat's numbers are reproducible —
they are just not judge-level numbers for M10/M12.

### 2b. M12 is not an evasion lane through `judge()`

Honest `g7_conjunct` admits the M12 witness under `judge()` because the cited
line is on the page, so `page_words(page)` contains `zeta` (inside backticks).
The only rejection is pre-existing G9 ("supported outside the cited line"), and
G9 fires identically under the mutant — the mutant's line-set swap cannot make a
word that *is* on the line disappear from the page. Two readings follow:

- the seat's "M12 SURVIVES — evasion" holds **only** for a caller that passes a
  line the page does not contain, which `judge()` never does;
- the seat's Q4b/F9 argument ("the cited-line filter is judge-reachable for
  backticked-only words, landed ADMIT / SM5 REJECT") uses the same
  inconsistent-line configuration. Measured through `judge()`:

```
SM5 lane cell      landed backed=False (G7 zeta)   SM5_mutant backed=False (G7 zeta)   # identical
wrapper-arm cell   landed backed=True  why=[]      SM5_mutant backed=True  why=[]      # identical
```

So **SM5 is judge-equivalent**: dropping the cited-line check changes no
`judge()` verdict. Plan Erratum E1 item 3's premise ("the cited-line filter is
redundant for reachable judge inputs") is **correct**, and RevC1Predicate's F9
(falsifying it) is itself falsified at judge level. The E1 disposition
("SM5's pin is component-level") stands, and the seat's recommended
wrapper-level arm is still component-level, not judge-level. This corrects the
one place where the wave-1 report told the L1 to amend a correct erratum.

## 3. M8 — the one real lane, and it is clear-cut at judge level

Landed `judge()` rejects the fabricated four-character span word (`zeta`) with
the G7 span reason; the `>= 5` mutant returns `backed=True, why=[]` — i.e. the
row would be **counted** (`eligible rows pass 4 of 4` machinery sees it as
backed) with a fabricated citation. This is an admission lane through the full
judge path, not just through the wrapper. It is also the only evasion lane among
the twelve, so C1's bound reduces to: *the fabricated-span case must be pinned;
the line-set cases are unobservable through `judge()`.*

## 4. The closing package: counts reproduce, shas do not; kills verified

Applied byte-exactly from the report (§3's two fenced blocks read from the file,
never retyped) at the anchor immediately after the four landed arms
(`check("A2 G9: an `and`-joined purpose clause off the cited line is rejected",`).

```
pkg6 (six arms)       sha256 56fb9b3a90f29c78899e65709d21a0aa14d1de5a5ce4f0b02e66838f399b7221
                      exit 0   self-test: 0 failure(s) over 229 assertions
pkg7 (+wrapper arm)   sha256 a198aa508185a79fe98700590f6209cd6ac54af4c5e96a3bb5cea59b597049c3
                      exit 0   self-test: 0 failure(s) over 230 assertions
seat quoted           229 → f3c825747e5525ac388cd53772271d4883be9074e6d1ff7c751a8e3d95aa7d15
                      230 → b614e8b19a219155f2a4250726d5089871112a54ae5ce87c4516b04350787f7d
```

The **counts** 229/230 and the green run reproduce; the **shas do not**. They are
not an artefact of the landed arm-4 hardening alone: on the seat's own quoted
base (`c04fffb`, sha `12d093a1…`, 219) I inserted MutW2V32 §11's four-arm fence
verbatim at three plausible anchors and then this package:

```
frozen219 + §11 four arms, anchor before `# G9 discriminating arms`   3612e76a442e77aa07352d835c16bf0981c0effe2b6c2ac2cc4c69e2bbf6b44c
frozen219 + §11 four arms, anchor before the `unsupported …` arm      78275152ba831a7087f95a0c6933a8704b404ffb7906b9a34723278e0e2da030
frozen219 + §11 four arms, anchor before the G9 arms                  4d857ecd809a1448ab6d95bc3252de3e7b79aa5da8868dffea3697dcb7358dff
   claimed at that state                                              d61c3eda67a0311fe9bf1d287dce2fb33f11e624294b6cbed1ec262e1089fc1f
+ six arms at the G9-arms anchor                                       728629d04fddc25af0318f3e51af12f69fce64b094d2420c4939ef83537fa8fd  (229)
+ seven arms                                                          49eb34ce420571c54f9ba4bed1d1780e6f69b7d012ed9fe6a8839b393f725d0b  (230)
```

Every run prints the claimed assertion count and exits 0, but none reaches the
claimed sha. Conclusion: the quoted `(sha256, N)` pairs pin an unpublished byte
layout (the seat's private working file), so the package as quoted cannot be
used as a `(sha, N)` freeze token until the exact patch is landed and the sha
recomputed from committed bytes. That is a concrete instance of the seat's own
F3 — and it means the L1 must not copy `f3c82574…`/`b614e8b1…` into a receipt.

### 4a. Kill table on `pkg6` (229 assertions) — all twelve named lanes

| mutant (exact-string replacement) | exit | killing assertion (first) |
|---|---|---|
| M7 `>= 3` | 1 | `A2 G7: a three-character span word is not rejected: got True` |
| M8 `>= 5` | 1 | `A2 G7: a fabricated four-character span word is rejected: got False` (+ the M12 arm) |
| M9 `word not in STOPWORDS` | 1 | `A2 G7: a capitalised stopword-only span is not rejected` |
| M10 `word not in content_words(raw_line)` | 1 | `A2 G7: a capitalised span word present in the cited line is not rejected` |
| M12 `page_words(raw_line)` | 1 | `A2 G7: a span word present in the cited line only inside backticks is rejected` |
| M17 exact page match | 1 | `A2 G7: a span word supported by a four-character prefix on the page is not rejected` |
| SM1 `span_missing = []` | 1 | `A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected` (3 FAIL lines) |
| SM2 floor dropped (`>= 2`) | 1 | `A2 G7: a backticked span word shorter than four characters is not rejected` (2) |
| SM3 stopwords dropped | 1 | `A2 G7: a backticked span made only of stopwords is not rejected` (2) |
| SM4 page check dropped | 1 | `A2 G7: a span word supported by a four-character prefix …` then 5 eligible-world lines (6) |
| SM5 line check dropped | 1 | `A2 G7: a backticked span word present in the cited line is not rejected …` (2; 3 under `pkg7`) |
| SM6 always fires | 1 | same arm (9) |
| **M14 wrapper drops `page_text`** | **1** | **`A2 G7: a span word present in the cited line only inside backticks is rejected`** |
| M11 `.lower()` off the page set | **0** | survives 229 |
| M20 page set → `content_words` | **0** | survives 229 |
| M19 `sorted`→`list` | **0** | survives 229 (determinism only) |
| M22 `L`-guard weakened | **0** | survives (equivalent) |

Two corrections to the seat's table: **(i) M14 is killed** by the package — the
M12 arm's witness (`lines` = the backticked line, `page_text` lacking `zeta`)
also pins the wrapper's `page_text` plumbing; the seat listed it as surviving
"diagnostic only". **(ii) SM4's first failure is the M17 prefix arm**, not the
pre-existing eligible-world arm, so the seat's attribution caveat is incomplete
on the closing suite (the world lines are there too — 6 FAIL lines total).

The seven-arm suite (`pkg7`) is identical except SM5 kills 3 assertions instead
of 2 — the wrapper arm adds one SM5 pin, exactly as the seat predicted. It
changes nothing else.

## 5. Does the deferred package verify?

- **Assertion counts and green state: verified.** 223 + 6 = 229, +1 = 230, both
  exit 0, no FAIL lines, and the predicate lines still print (`worlds reject 7
  of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`).
- **Kill behavior: verified.** All six named lanes plus SM1–SM6 go red, each
  FAIL naming its target arm; M14 additionally dies (bonus wiring pin).
- **Shas: NOT verified** (§4). They pin an unpublished layout and must be
  recomputed at landing.
- **Coverage: one judge-level lane remains open — M20.** On `pkg6` the
  single-word-backticked-span witness is admitted by the honest bytes and
  rejected by the M20 mutant (both through `judge()`), and the package contains
  no arm for it:

```
pkg6       judge backed=True  why=[]
pkg6+M20   judge backed=False why=['… A2 G7: backticked span word(s) zeta …']
```

  This is an over-rejection lane (honest admits a claim the page *does* support,
  the mutant rejects it), so it is a false-reject rather than an evasion — but
  it is verdict-flipping and unpinned. Round-65 candidate.
- **Component-only arms are not defects.** The M12 arm is a legitimate pin (it
  kills M14 even though M12 itself is judge-equivalent); the M10 arm is the
  weakest (judge-equivalent and it only kills its own mutant).

## 6. Lane state and restoration evidence

`/tmp/mutw2` is disposable and was the only mutated location; the lane was read
only (`git show`, `git archive`) and its verifier is byte-identical to the
landed blob before and after:

```
$ sha256sum verifiers/check_scoped_rules_v32.py
f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
$ git status --porcelain
 M .ufo/waves/round-64/receipts/noharm-tip.txt      # pre-existing, not mine
?? .ufo/waves/round-64/w2/                          # wave-2 reports (mine inside)
```

No git/jj write, no sibling lane touched, no host service or package touched.
All temporary mutants lived at `/tmp/mutw2/tree/verifiers/mut_*.py` and were
deleted after each run; `pkg6.py`/`pkg7.py`/`seat223.py` remain only in scratch.

## 7. Findings (severity ordered) and round-65 candidate list

**F1 (critical, confirmed): M8 is a real `judge()` admission lane and the landed
four arms do not close it.** `landed223 + M8` self-test: exit 0, `0 failure(s)
over 223 assertions`. The closing package's fabricated-four-character arm kills
it (exit 1). Land that arm (or all six) — C1's "the branch is pinned" is false
until it lands.

**F2 (high, correction): M12's "evasion" is not judge-reachable.** Through
`judge()` the witness is rejected by pre-existing G9 in both honest and mutant
code; the line-set swap is equivalent because `page_words(page) ⊇
content_words(line)`. The same holds for M10. Record them as component-level
pins; do not carry "two admission-flipping lanes" into the round-65 claims.

**F3 (high, correction): RevC1Predicate F9 / §4b is falsified; Erratum E1 item 3
is correct.** SM5 (cited-line check dropped) is judge-equivalent on both the M8
and wrapper-arm witnesses. The L1 should not amend E1 item 3 in the direction
the seat recommended; the component-level pin disposition stands.

**F4 (medium, new): M20 is a judge-level verdict-flipping lane the package
leaves open** (receipt in §5). It needs one arm with a single-content-word
backticked span whose only page support is a backticked occurrence, e.g.
`` The tool writes mode quota nightly and `zeta`. `` with the page line
`` The `zeta` appendix sentence. ``.

**F5 (medium, package provenance): the quoted 229/230 shas are not
reproducible** from the report, the landed bytes, or the seat's quoted base
under three insertion anchors (§4). Land a patch, not a sha; recompute
`(sha, N)` from committed bytes; register the row in
`verifiers/floors-registry.json` at the *landed* count so later arm deletion is
visible (the seat's F5b remains open, and 223→229/230 moves the number).

**F6 (low, attribution): M14 is killed by the M12 arm**, and SM4's first killer
is the M17 arm — update the kill table and the "which arm kills what" sentence
if the package lands with a kill-conjunct receipt.

**F7 (low, residual): M11, M18, M19, M22 remain unpinned**; M22's `L` guard is
unreachable contract surface under `judge()` (equivalent), M19 is a determinism
hazard for any receipt that greps the G7 message text.

## 8. Addendum — cross-check of two further lanes (peer report, re-measured)

`CriticW2Bounds-2` reported two mutants outside the M7–M22 list; I re-derived
both on my own bytes rather than accepting the claim.

### 8a. Span-iterator restriction — CONFIRMED, unpinned, judge-level admission

Exact anchors in the landed branch, each one exact-string replacement:

```
for span in BACKTICK_RE.findall(cell)          ->  …(cell)[:1]      # only the first span checked
for span in BACKTICK_RE.findall(cell)          ->  …(cell)[-1:]     # only the last span checked
```

Survival (measured, `0 failure(s)`, exit 0 on **every** suite):

```
SPAN_FIRST check_scoped_rules_v32 exit=0 223 assertions
SPAN_FIRST pkg6                   exit=0 229 assertions
SPAN_FIRST pkg7                   exit=0 230 assertions
SPAN_LAST  check_scoped_rules_v32 exit=0 223 assertions
SPAN_LAST  pkg6                   exit=0 229 assertions
SPAN_LAST  pkg7                   exit=0 230 assertions
```

Full-judge receipt — two backticked spans, one honest (`mode quota`, on the
cited line) and one fabricated (`zeta quota`, absent from line and page):

```
cell  …`mode quota` and `zeta quota`.     landed REJECT (G7 zeta)   SPAN_FIRST backed=True   SPAN_LAST REJECT
cell  …`zeta quota` and `mode quota`.     landed REJECT (G7 zeta)   SPAN_FIRST REJECT        SPAN_LAST backed=True
```

So a cell with two spans smuggles the fabrication past the branch whenever the
fabricated span is not the one the mutant inspects — a **full judge admission**
(not component-only) that neither the landed four arms nor the 6/7-arm package
pins. This is a second real evasion class beside M8, and it is the strongest
round-65 candidate found in this seat. (The *word*-level restriction
`span.split()[:1]`/`[-1:]` is **not** the same mutant and is killed: `[:1]`
fails landed arm 1 — it drops `credentials` from `exfiltrates credentials` —
and `[-1:]` fails pkg6's M12 arm. Do not generalize the survival to word-level
iteration.)

### 8b. M11 — refinement: it becomes judge-reachable when the page holds the exact uppercase token

My §2 table measured M11 as "diagnostic only" with a page whose only occurrence
was lowercase (`zeta`). With the **exact uppercase** `ZETA` on the page — so the
identifier branch's `token in raw_page` passes — and the cited line lacking it:

```
cell The tool writes mode quota nightly and `ZETA`.
page  <cited line> + "The `ZETA` appendix sentence."
landed         backed=True   why=[]
M11 mutant     backed=False  why=['… A2 G7: backticked span word(s) ZETA …']
survival       landed 223 exit=0 · pkg6 229 exit=0 · pkg7 230 exit=0
```

A full-judge **over-rejection** (false reject), not merely a message change; the
identifier branch had masked it in the lowercase witness. The package leaves it
unpinned, consistent with F7.

Both addenda are additional round-65 candidates: an arm with two spans
(honest + fabricated) closes 8a; a `ZETA`/uppercase-on-page arm closes 8b.

Report: .ufo/waves/round-64/w2/MutW2M7M22.md
