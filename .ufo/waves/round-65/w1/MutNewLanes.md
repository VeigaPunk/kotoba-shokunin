# MutNewLanes — ten fresh single-string mutants of the g7 span branch (round 65, wave 1)

Seat: mutation-tester, wave kotoba-r65-w1, 2026-10-24. Leaf member: no subagent
dispatch. Lane bounds respected: every write landed under `/tmp/mutnew-lanes/`
plus this report file; the fleet repo, sibling lanes and the jj/git index were
read-only (read-only `git show`/`git rev-parse` only, no `git`/`jj` write).
Bounded probe: ≤4 concurrent processes, each detector run ~0.28 s.

## Target bytes

The attack surface is the landed round-65 instrument, extracted from the
implementation commit (never from the dirty worktree, which has since moved to
round 66):

```
$ git show 80bb8921:verifiers/check_scoped_rules_v32.py | sha256sum
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  -
$ git show 0e104f49:verifiers/check_scoped_rules_v32.py | sha256sum
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  -
$ sha256sum verifiers/check_scoped_rules_v32.py        # worktree, round-66 HEAD
97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def
```

`b6cfc764…` is the sha the C1 receipt pins (`.ufo/waves/round-65/receipts/
C1-close-measure.txt`), so the frozen plan's counter and my scratch copy are the
same bytes: 152,760 B, landed into `/tmp/mutnew-lanes/verifiers/` via
`git archive 80bb8921 verifiers` (51 files, so the sibling
`check_erratum_absorption.py` load at landed line 2787 resolves).

Mutation sites (landed line numbers): `SUPPORT_PREFIX = 4` :354 ·
`content_words` :1008-1013 · `supported()` :1035-1039 · `g7_conjunct` :1046-1068,
the `span_missing` comprehension at :1055-1061.

## 1. Detector and baseline

The detector is the plan's own bounded predicate: the self-test, no `--fetch`.

```
$ python3 -B /tmp/mutnew-lanes/verifiers/check_scoped_rules_v32.py --self-test
counter sha256 b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d
...
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 234 assertions
exit=0
```

Baseline is green and reproducible: four pristine-byte runs (a harness baseline
and a post-restoration run in each of two harness passes) all exit 0 with
`0 failure(s) over 234 assertions` and sha `b6cfc764…`. A baseline failure would
have been inconclusive; there was none. The self-test's only writes are inside
`tempfile.mkdtemp` fixtures (landed :2421-2427), and `lane_dir()` falls back to
the lane for reads only, so the run is side-effect-free on the lane.

Harness: `/tmp/mutnew-lanes/mutate.py` asserts each `old` string occurs exactly
once in the landed bytes, writes the mutated bytes into the scratch copy, runs
the detector, then restores the pristine bytes. All ten replacements were
unique (the harness would have aborted otherwise).

## 2. The ten mutants

| # | mutant | single-string change (site) | mutated sha256 (full) | detector | verdict |
|---|---|---|---|---|---|
| A | **swap the two set operands** | `content_words(raw_line)` + `page_words(raw_page)` → `content_words(raw_page)` + `page_words(raw_line)` (:1060-1061) | `f1655acc73e4a2c4740c42570bdc08cc2aab53bd693af794a8fa40cb64473594` | exit 1, 3 failures | **KILLED** by A3 (+A10, A11) |
| B | **`SUPPORT_PREFIX` 4 → 8** | `SUPPORT_PREFIX = 4` → `= 8` (:354) | `47b67092d2ee2878b0fd1945f82aa63aa5c39746be400d224f000fbca1b2ab47` | exit 0, **0 failures / 234** | **SURVIVES — new lane (see §4)** |
| C | **floor ≥4 → ≥6** | `len(word) >= 4` → `>= 6` (:1059) | `6049c0e1ce8bd730e2eb29163cfcefe8fa0b70d123811321e66368d8cc20ecf7` | exit 1, 4 failures | **KILLED** by A1 (+A3, A8, A9) |
| D | **`finditer` for `findall`** | `for span in BACKTICK_RE.findall(cell)` → `finditer(cell)` (:1057) | `8702ce2aac945b749a1518a8e313a56615bdb8d587221ca1451ec4bdb93a1c0b` | exit 1, **traceback**, no summary | **KILLED — by crash, no arm (see §5)** |
| E | **`span.split()[:1]`** | first word of each span only (:1058) | `ab3f3826d094f62ae20b024f55c613fafaff10b97c9e46eb599e1eee06d684f1` | exit 1, 1 failure | **KILLED — by an r64 arm, none of the 11 (see §5)** |
| F | **`not in` → `in`** (line-set inversion) | `word.lower() not in content_words(raw_line)` → `in` (:1060) | `11db26314381a43a58cd059fd825f67b997234b8875740d2733dcd1f5b4309f4` | exit 1, 8 failures | **KILLED** by A1 (+A3, A6, A7, A8, A9) |
| G | **`.lower()` dropped in `content_words`** | `CONTENT_RE.findall(t.lower())` → `findall(t)` (:1013) | `c0441dcc34ff60ae2125d45abf4ae753d601f854cacf2f2494511cf291113f90` | exit 1, 8 failures | **KILLED** by A6 (+A2 units, eligible-world) |
| H | **`.lower()` dropped on the probe word** | `supported(word.lower(), page_words(...))` → `supported(word, …)` (:1061) | `0d1c68a28e9c36dacbf486f61b9025d5dcf860546b6cb9669acba2658ab19632` | exit 1, 1 failure | **KILLED** by A11 (single-arm) |
| I | **span set reported under the identifier flag** | `if span_missing:` → `if missing:` (:1065) | `4a5a1e1b0e50ff1f62ada8e17400ecf0435821697bc03d287141212d1385563d` | exit 1, 5 failures | **KILLED** by A1 (+A3, A8, A9) |
| J | **floor boundary ≥4 → >4** | `len(word) >= 4` → `> 4` (:1059) | `e114bab27ee2c38da1fb1d72033f591190fa3ca52f121a72587a6c97cb2b9795` | exit 1, 4 failures | **KILLED** by A1 (+A3, A8, A9) |

Full digests and the exact FAIL lines are reproduced by
`python3 -B /tmp/mutnew-lanes/mutate.py` (deterministic across two runs).

Raw output, verbatim, from `/tmp/mutnew-lanes/rawfails.py` (re-applies each
mutant and prints every line starting `FAIL ` or naming the exception; `check()`
emits `FAIL <name>: got %r, expected %r`, landed :1766):

```
== MUT-A exit=1
   FAIL A2 G7: a span word present in the cited line only inside backticks is rejected: got False, expected True
   FAIL A2 G7: a span word whose only page occurrence is inside backticks is not rejected: got True, expected False
   FAIL A2 G7: a capitalised span word present on the page only as an exact-case token is not rejected: got True, expected False
== MUT-B exit=0
== MUT-C exit=1
   FAIL A2 G7: a fabricated four-character span word is rejected: got False, expected True
   FAIL A2 G7: a span word present in the cited line only inside backticks is rejected: got False, expected True
   FAIL A2 G7: a fabricated first backticked span is rejected when an honest second span follows it: got False, expected True
   FAIL A2 G7: a fabricated second backticked span is rejected when an honest first span precedes it: got False, expected True
== MUT-D exit=1
   AttributeError: 're.Match' object has no attribute 'split'
== MUT-E exit=1
   FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
== MUT-F exit=1
   FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
   FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
   FAIL A2 G7: a fabricated four-character span word is rejected: got False, expected True
   FAIL A2 G7: a span word present in the cited line only inside backticks is rejected: got False, expected True
   FAIL A2 G7: a capitalised span word present in the cited line is not rejected: got True, expected False
   FAIL A2 G7 (wrapper): a span word present in the cited line is not rejected even when the page lacks it: got True, expected False
   FAIL A2 G7: a fabricated first backticked span is rejected when an honest second span follows it: got False, expected True
   FAIL A2 G7: a fabricated second backticked span is rejected when an honest first span precedes it: got False, expected True
== MUT-G exit=1
   FAIL A2 cell words drop backticks, citations and stopwords: got {'rule', 'cope', 'file'}, expected {'rule', 'scope', 'file'}
   FAIL A2: a cell the cited line supports passes: got ['A2: action word(s) cope do not occur on the committed snapshot'], expected []
   FAIL A2 G7: a capitalised span word present in the cited line is not rejected: got True, expected False
   FAIL eligible world: the four counted rows are backed: got ['VS Code'], expected ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']
   FAIL eligible world: the four counted rows are found live: got [False, True, False, False], expected [True, True, True, True]
   FAIL eligible world: the CLI exits 0 at a target of 4: got 1, expected 0
   FAIL eligible world: the summary line is the v2 one: got 'scoped rule files backed on committed snapshots 1 of 4; found on the live page 1 of 4', expected 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4'
   FAIL the predicate line is computed from four passing eligible rows: got 1, expected 4
== MUT-H exit=1
   FAIL A2 G7: a capitalised span word present on the page only as an exact-case token is not rejected: got True, expected False
== MUT-I exit=1
   FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
   FAIL A2 G7: a fabricated four-character span word is rejected: got False, expected True
   FAIL A2 G7: a span word present in the cited line only inside backticks is rejected: got False, expected True
   FAIL A2 G7: a fabricated first backticked span is rejected when an honest second span follows it: got False, expected True
   FAIL A2 G7: a fabricated second backticked span is rejected when an honest first span precedes it: got False, expected True
== MUT-J exit=1
   FAIL A2 G7: a fabricated four-character span word is rejected: got False, expected True
   FAIL A2 G7: a span word present in the cited line only inside backticks is rejected: got False, expected True
   FAIL A2 G7: a fabricated first backticked span is rejected when an honest second span follows it: got False, expected True
   FAIL A2 G7: a fabricated second backticked span is rejected when an honest first span precedes it: got False, expected True
restored sha b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d
```

MUT-D's traceback tail (from the harness's own capture of the run):
`    for word in span.split()` / `                ^^^^^^^^^^` /
`AttributeError: 're.Match' object has no attribute 'split'`.

Every non-crashing run still reported `self-test: … over 234 assertions`; the
crash run printed no summary at all. So no mutant changed the assertion count —
the floors guard registered at 234 sees none of them, which is exactly why the
kill battery exists. (MUT-G is the loudest: dropping one `.lower()` in
`content_words` also turns `Scope` into the non-word `cope` and collapses the
eligible world to 1 of 4 — the case fold is load-bearing on the live path, yet
A6 is the only *new* arm that sees it.)

## 3. Attribution against the 11 new arms

Arms (landed line, name):

| id | line | arm |
|---|---|---|
| A1 | 2169 | a fabricated four-character span word is rejected |
| A2 | 2176 | a three-character span word is not rejected |
| A3 | 2183 | a span word present in the cited line only inside backticks is rejected |
| A4 | 2191 | a span word supported by a four-character prefix on the page is not rejected |
| A5 | 2198 | a capitalised stopword-only span is not rejected |
| A6 | 2205 | a capitalised span word present in the cited line is not rejected |
| A7 | 2213 | (wrapper) a span word present in the cited line is not rejected even when the page lacks it |
| A8 | 2221 | a fabricated first backticked span is rejected when an honest second span follows it |
| A9 | 2230 | a fabricated second backticked span is rejected when an honest first span precedes it |
| A10 | 2239 | a span word whose only page occurrence is inside backticks is not rejected |
| A11 | 2247 | a capitalised span word present on the page only as an exact-case token is not rejected |

Kill matrix (arm → mutants it killed):

| arm | killed | firing mutants |
|---|---|---|
| A1 | yes | C, F, I, J |
| A2 | **not reached by this set** | — (r64's `>= 3` mutant, MutW2M7M22 §4) |
| A3 | yes | A, C, F, I, J |
| A4 | **not reached by this set** | — (r64's exact-match mutant, MutW2M7M22 §4) |
| A5 | **not reached by this set** | — (r64's `STOPWORDS` mutant, MutW2M7M22 §4) |
| A6 | yes | F, G |
| A7 | yes | F |
| A8 | yes | C, F, I, J |
| A9 | yes | C, F, I, J |
| A10 | yes | A |
| A11 | yes | A, H |

Eight of the eleven new arms fired as the canonical killer of at least one
plausible single-string mutant. A2/A4/A5 did not fire here, but each is already
shown killable by the round-64 mutants `>= 3`, exact-match and
`not in STOPWORDS` (`.ufo/waves/round-64/w2/MutW2M7M22.md` §4, lines 191-196) —
absence from my set is non-coverage by my ten, not a dead pin. A4's insensitivity
to the *width* of the prefix is the subject of §4.

## 4. Survivor MUT-B (`SUPPORT_PREFIX 4 → 8`) — a judge-level lane

The mutant survives the whole battery (exit 0, `0 failure(s) over 234
assertions`), and it is not a cosmetic survivor: run against the real landed
artifacts at the round tip it drops the product's counted line from 4 of 4 to
3 of 4.

```
$ python3 -B /tmp/mutnew-lanes/pristine_v32.py --rev 0e104f498b3df1466284074c5b3a6e5b523420cd
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d; rev 0e104f49…
$ echo $?   # 1 -- predicate() returns 1 whenever --fetch is absent (:1719)

$ python3 -B /tmp/mutnew-lanes/variants/MUT-B.py --rev 0e104f498b3df1466284074c5b3a6e5b523420cd
scoped rule files backed on committed snapshots 3 of 4; live not run
counter sha256 47b67092d2ee2878b0fd1945f82aa63aa5c39746be400d224f000fbca1b2ab47; rev 0e104f49…
reject Copilot CLI: entry row S106: snapshot .ufo/waves/round-60/snapshots/S106.page:
  A2 G9: clause "Create a path-specific instruction file with an `applyTo` glob"
  is supported outside the cited line
```

(the `rev 0e104f49…` tail and the wrapped reason line are elided/wrapped for
width; the file prints them on one line.)

Values parsed from the `--json` block on the same rev (`backed`, `of`,
per-client), layout mine:

```
pristine_v32     backed=4 of 4   Copilot CLI backed=True  why=[]                        row=S106
variants/MUT-B   backed=3 of 4   Copilot CLI backed=False why=['entry row S106: … A2 G9: …'] row=None
```

(Exit code is 1 for both: `predicate()` at :1719 returns 1 whenever `--fetch`
is absent, so the *count*, not the exit, is the discriminating observable here.)

Component proof, at the exact call site `judge()` uses (:1555
`action_conjunct(lines, action_cell, action_line, page)`, whose reasons are
appended to the row `why` and `"backed": not why` at :1637 — i.e. the component
verdict *is* the row verdict):

```
supported('specific',  {'specified'})   landed=True  mutant=False
supported('scope',     {'scoped'})      landed=True  mutant=True
supported('instruction',{'instructions'}) landed=True mutant=True
supported('patterns',  {'pattern'})     landed=True  mutant=False
supported('requirement',{'require'})    landed=True  mutant=False

witness lines = ['A path-scoped rule loads on the matching file.']
        cell  = 'A path-scoped rule loads on the matching `file patterns`.'
        page  = 'A path-scoped rule loads on the matching file.\n\n## Appendix\nThe pattern table is stored.'
landed action_conjunct -> []
MUT-B  action_conjunct -> ['A2 G7: backticked span word(s) patterns occur in neither the cited line nor the committed snapshot']
```

Mechanism: `supported()` truncates the *probe* word to `SUPPORT_PREFIX` and asks
whether a page word starts with it. A4's witness is `scope`/`scoped`, where the
page word is longer than the probe, so `word[:8]` is still a prefix and A4 stays
green at width 8; the same holds for the two `A2 support:` unit arms. The width
only bites when the page form is *shorter* than the probe's truncated prefix or
diverges inside the first 8 characters (`patterns`/`pattern`,
`specific`/`specified`, `requirement`/`require`) — the real S106 clause
("path-specific" vs the page's "specify/specified") is precisely such a pair.
Blast radius is not the span branch alone: `supported()` is used by `covered()`
(:1043, A2 forward/reverse fractions and every G9 clause) and by A2's page
containment (:1170), so the unpinned width sits under all of them.

**New lane name: `PREFIX-WIDTH` (MUT-B).** Coverage finding, not a contract
change. The pin that would kill it is one boundary assertion on the admitted
side, e.g.

```
check("A2 support: a four-character root supports a longer word form",
      supported("specific", {"specified"}), True)
```

which is `True` on the landed bytes and `False` under the mutant (measured
above). Note also that A4 asserts the *existence* of prefix support, never its
width, so no amount of re-reading A4 narrows this.

## 5. Two attribution nuances

- **MUT-E (`span.split()[:1]`) is killed, but by a round-64 arm, none of the
  eleven.** The killer is `A2 G7: a backticked span whose words occur in
  neither the cited line nor the page is rejected` (r64 pinning block), whose
  witness `` `exfiltrates credentials` `` has `exfiltrates` prefix-supported on
  the page and `credentials` absent — the second word only. Measured:
  `landed r64 cell -> ['… span word(s) credentials …']`, `MUT-E -> []`.
  The eleven new arms do **not** pin intra-span word coverage: A8/A9 pin the
  *order of spans*, and in both of their witnesses the fabricated word is the
  first word of its span, so `[:1]` keeps them green. That is coherent (the
  class is closed by an older arm, so no new lane opens), but the deficit is
  real: `mode zeta` (first word exactly in the line, second fabricated, phrase
  span so `BACKTICKED_IDENTIFIER_RE` cannot see it) is rejected by the landed
  bytes and admitted by the mutant —
  `landed inner cell -> ['… span word(s) zeta …']`, `MUT-E -> []`.
- **MUT-D (`finditer`) is killed without arm attribution.** `BACKTICK_RE.
  finditer` yields `re.Match`, whose `.split()` does not exist, so the battery
  aborts with a traceback: exit 1 but **no `self-test:` summary line and no FAIL
  line**. The plan's kill conjunct demands "exits 1 with a FAIL line attributed
  to its pin arm"; a crash-mutant satisfies the exit but not the attribution and
  truncates every later arm. Nothing in the battery pins iterator *type*; the
  kill here is incidental (any exception in the same statement would read the
  same way). Not a lane — the defect is unshippable — but worth recording so a
  future "killed" tally does not count a crash as arm coverage.

## 6. Restoration evidence

Every mutant was written only into `/tmp/mutnew-lanes/verifiers/`, and the
harness rewrites the pristine bytes after the tenth run:

```
$ sha256sum /tmp/mutnew-lanes/verifiers/check_scoped_rules_v32.py /tmp/mutnew-lanes/pristine_v32.py
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  …/verifiers/check_scoped_rules_v32.py
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d  …/pristine_v32.py

$ python3 -B /tmp/mutnew-lanes/verifiers/check_scoped_rules_v32.py --self-test | tail -1
self-test: 0 failure(s) over 234 assertions        # exit=0
```

Scratch sha == the landed commit's sha (`git show 80bb8921:… | sha256sum`), so
"restored" is byte-identical, not merely equivalent. The lane worktree file was
never a mutation target:

```
$ sha256sum verifiers/check_scoped_rules_v32.py
97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def   # round-66 HEAD, unchanged
$ stat -c '%s %y' verifiers/check_scoped_rules_v32.py
154495 2026-10-24 03:44:17 -0300    # mtime predates every probe run (~04:40)
```

No write was issued anywhere under
`/home/vgpnk/Projects/shokunin/kotoba-shokunin` except this report file.

## 7. Claims supported / falsified

- **Supports** C1's kill conjunct for 8 of the 11 new arms: A1, A3, A6, A7, A8,
  A9, A10, A11 each produced the FAIL line that kills a plausible single-string
  defect of the span branch (table §3). The landed span branch is pinned for
  operand identity (A), the floor (C, J), the line-set polarity (F), the case
  fold inside `content_words` (G), the probe's case fold (H) and the
  span-set/report wiring (I).
- **Supports** the plan's determinism/fixture-leak posture in the narrow sense
  that the detector is reproducible: four green baseline/restoration runs (two
  harness baselines, two restorations) all print exit 0, `0 failure(s) over 234
  assertions`, sha `b6cfc764…`, and every mutant run is identical across two
  harness passes. Nothing leaked out of the tempdir fixtures.
- **Falsifies (coverage, not contract)** the reading that the 11 arms close the
  span branch's support semantics: `SUPPORT_PREFIX 4 → 8` survives 234/234 and
  regresses the judge-level counted line 4 of 4 → 3 of 4 on the landed artifacts
  (S106 Copilot CLI), because the only prefix arm (A4) is insensitive to width.
  New lane: `PREFIX-WIDTH` (§4).
- **Corrects** an attribution expectation: `span.split()[:1]` is killed by the
  round-64 "neither the cited line nor the page" arm, not by any of the eleven —
  A8/A9 pin span order, not intra-span words (§5).
- **Records** that crash-kills (MUT-D) satisfy "exit 1" but not "FAIL line
  attributed to its pin arm", and hide every later assertion (§5).

## Gaps / residual unknowns

- [INFERENCE] Judge-level reachability of the §4 witness was demonstrated by
  running `main --rev 0e104f49` on the real artifacts (4 of 4 → 3 of 4), not by
  constructing a synthetic world through `judge()`; the row reasons printed are
  the ones :1555 appends, so the two agree.
- [INFERENCE] I did not test widths other than 8 (e.g. 6): the lane's existence
  is established by one surviving width, not by a width sweep.
- A2/A4/A5's aliveness rests on the round-64 mutants I re-read, not re-ran
  (they are outside this seat's ten).

## Tooling

No installs or upgrades this seat (python3 3.14, git, sha256sum all
pre-installed; the host-wide pacman pause was respected — no pacman invocation
of any kind).

Report: .ufo/waves/round-65/w1/MutNewLanes.md
