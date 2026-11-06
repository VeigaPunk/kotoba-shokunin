# MutTesterAnchorR100 — attack on the C2 counter (`anchor-lists.py` v1) and the new comma-anchor regex

Seat: MutTesterAnchorR100 (attack seat, wave r100-w1). Scratch: `/fast/scratch/hyaku/kotoba-r100/MutTesterAnchorR100/`
(removed before yield). Lane writes: this file + `w1/MutTesterAnchorR100/` receipts only. No counter, plan or
frozen predicate was edited; every world and mutant lives in the seat's scratch clone.

Base: `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`. Counter instrument sha256
`c31db02dca3a292c394bdfd551106996a40250e42c80bc27d6190c51fc99af02 anchor-lists.py` (unchanged; every
receipt records it). Candidate measured in part (b): `0f86d4ccde188bd915b6a77b25ae2c9f0bbc85a8` —
base + `ScribeCorpusR100.patch` + `ExecAnchorR100.patch` + `ExecArmsR100.patch`, applied in that order
(the prescribed order; `ExecAnchorR100.patch` sha256 `f2d1efee…c92`). Its checklist blob is
`94d11c7a103590bfeea93910da6710bd8a64f0c6` = the blob the builder admitted to `INSTRUMENT_PINS`, and
its battery blob is `575da5b6…`. The mutant table was run twice — on `c20dd7a2690514690df2d3293a44a565a488e25d`
(base + Anchor only, built before the other two patches existed) and on the full candidate — with
identical results (`mutants.txt`, `mutants-full-candidate.txt`): the two extra patches do not touch
`verifiers/verify_skill_checklist.py`.

## Method

Part (a): eight forgery worlds, each a commit on the frozen base in the seat's scratch clone
(`build_worlds.py`, revs in `worlds.txt`), measured with the frozen command
`HYAKU_SCRATCH=… python3 -B verifiers/fixtures/round-100/anchor-lists.py <rev> <scratch clone>`.
Each world is a plausible way to make the counter's six conjuncts read MET without the honest change
(or, for w3b/w5, with the honest change plus something the counter's evidence claims to exclude).
Full readings are in `counter-<world>.txt`; the confinement conjunct was additionally evaluated
directly with the counter's own `checklist_confined` (`confined.txt` below).

Part (b): ten mutants of the new regex (`strip_token_dressing` fix line) and four mutants of the new
self-test arms, applied in the candidate checkout and classified by the checklist's own
`--self-test` under the counter's kill rule (`self-test FAIL: ` line + `N failure(s) over M
assertions`, N ≥ 1, exit 1). Every mutant restores the exact candidate bytes (`mutants.txt` records
the before/after sha256 of each restore; `witness-arms.txt` the arm witness pairs).

## Part (a) — eight forgery worlds

| world | rev | counter tally | verdict | caught by |
|---|---|---|---|---|
| w1-helper-fix | 428f08f7 | `mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant ABSENT; frozen 2 of 3; battery ok` | UNMET | kill (ABSENT) + frozen (bytes outside) |
| w2-source-sniff-arm | d2676811 | `mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant KILLED; frozen 3 of 3; battery ok` | **MET** | nothing — disclosed bound, confirmed |
| w3-monkeypatch-visible | fd950ab4 | `mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant ABSENT; frozen 2 of 3; battery ok` | UNMET | kill (ABSENT) + frozen (bytes outside) |
| w3b-blind-window-extra | da5d6d5e | `mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant KILLED; frozen 3 of 3; battery ok` | **MET** | nothing — confinement blind window (finding F3) |
| w4-row-edited | bfd4e321 | `mismatches 0 of 28; gate RED; self-test HELD; revert mutant KILLED; frozen 2 of 3; battery FAIL` | UNMET | frozen (corrections rows) + gate RED |
| w5-dynamic-pin | 43c26184 | `mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant KILLED; frozen 3 of 3; battery ok` | **MET** | nothing — self-computed pin (finding F1) |
| w6-blind-window-fix | 5b503ffb | `mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant ABSENT; frozen 2 of 3; battery ok` | UNMET | kill (ABSENT) + frozen (bytes outside) |
| w7-fixture-special-case | 9b4db1f1 | `mismatches 0 of 28; gate GREEN; self-test HELD; revert mutant ABSENT; frozen 2 of 3; battery ok` | UNMET | kill (ABSENT) + frozen (bytes outside) |

**3 of 8 worlds read `C2-PREDICATE-MET` (rc 0): w2, w3b, w5.** Two of those are counter
findings (F1, F3); w2 is the bound the counter header already discloses (F2). The five refused worlds
are refused by the *byte* conjuncts (kill + confinement), never by the truth table: every world had
`mismatches 0 of 28`, i.e. no world could make the behavioural conjunct fail — the fix line is the only
thing that moves it, and the confinement pins it to `FIX_LINE`.

w7 is the sixth named forgery shape: `citation_resolve` is replaced (in the blind window, so the
confinement cannot see it) by a lambda that special-cases the frozen fixture path **and** the one live
stale path, with **no** fix line. Measured directly on the world's module: truth table `0 of 28`
mismatches **and** the real-tree governance check `('PASS', 1666)` — i.e. both the truth-table conjunct
and the gate conjunct are fooled without the fix. Only the kill conjunct (`FIX_LINE` absent → ABSENT)
and the confinement (base line still present) refuse it.

Direct evaluation of the counter's own `checklist_confined` on each world (no counter run needed):

```
w1-helper-fix              confined=False (bytes differ outside the fix line, self_test and the corrections data)
w2-source-sniff-arm        confined=True
w3-monkeypatch-visible     confined=False (bytes differ outside the fix line, self_test and the corrections data)
w3b-blind-window-extra     confined=True
w4-row-edited              confined=False (corrections rows are not the base rows minus the one retired row)
w5-dynamic-pin             confined=True
w6-blind-window-fix        confined=False (bytes differ outside the fix line, self_test and the corrections data)
w7-fixture-special-case    confined=False (bytes differ outside the fix line, self_test and the corrections data)
```

All eight worlds read `mismatches 0 of 28` in the cheap pre-check (`probe_worlds.py`, exact reuse of
the counter's `ROWS`/`world()`). That is the important negative result: **the truth table does not
separate the honest change from a forgery by itself.** w1/w3/w6 implement the same behaviour outside
the fix line, and w7 special-cases the frozen fixture path (and the one live stale path) — all four
read `mismatches 0 of 28`, and w7 also reads the real-tree gate green. What separates them from the
honest change is the *byte* evidence: the fix line must be present at its base location (kill) and the
file must be byte-identical elsewhere (confinement). The truth table's value is that it is the one
conjunct a forger cannot satisfy *without* either the fix or a byte-visible substitute — which is why
F3 (a byte-visible substitute the confinement cannot see) is the finding that matters.

## Findings

### F1 — the instrument pin is vacuous when it is computed by code (severity: medium)

`frozen` conjunct 2 only requires `check_tip_battery.py` to be identical **outside** the
`INSTRUMENT_PINS = {…}` block, and the pin guard compares `git rev-parse <rev>:<path>` against
whatever the block evaluates to. A world that keeps the honest change but writes the admitted entry as
an expression instead of a literal

```python
    "verifiers/verify_skill_checklist.py": (
        __import__("hashlib").sha1(b"blob %d\x00" % len(__import__("pathlib").Path("verifiers/verify_skill_checklist.py").read_bytes()) + __import__("pathlib").Path("verifiers/verify_skill_checklist.py").read_bytes()).hexdigest(),
```

reads `frozen 3 of 3` and `battery … guards 5 of 5` (world `w5-dynamic-pin`, `counter-w5-dynamic-pin.txt`,
rc 0, `C2-PREDICATE-MET`). The pin then admits **any** checklist blob, so the two evidence lines the
claim cites for the pin — "frozen 3 of 3" and "guards 5 of 5" — assert nothing about the blob being a
reviewed one. The battery is run with `cwd` = the sandbox, so the relative path resolves to the REV
bytes; the computed digest equals the git blob id exactly.

Minimal fix (counter-side, no predicate change): in `checklist_confined`, require every code line
added to the REV `INSTRUMENT_PINS` block (comments and closing brackets allowed) to be a literal
40-hex admission. Probed against the counter's own `PINS_RE` (`fix-probes.txt`):

```
pin-literal probe (comments/closers allowed) honest candidate c20dd7a   admitted=True  code-added=['        "94d11c7a103590bfeea93910da6710bd8a64f0c6"),']
pin-literal probe (comments/closers allowed) w5-dynamic-pin             admitted=False code-added=['        __import__("hashlib").sha1(…).hexdigest(),']
pin-literal probe (comments/closers allowed) w3b-blind-window-extra     admitted=True  code-added=['        "b27785691189a2c4a7afff141e80c8802465b930",']
```

i.e. the honest candidate and a legitimate literal admission still pass, and w5 is refused. An AST
check (`ast.parse` the block, every tuple element an `ast.Constant` matching `^[0-9a-f]{40}$`) is the
equivalent, stricter form.

### F2 — the kill conjunct is satisfiable by a source-sniffing arm; the truth table is not (severity: informational, disclosed)

World `w2-source-sniff-arm` keeps the honest fix line and replaces the behavioural arm with

```python
    _src = Path(__file__).read_text(encoding="utf-8")
    _marker = ":" + chr(92) + "d+(-" + chr(92) + "d+)?(," + chr(92) + "d+"
    rec("strip_token_dressing: comma-list branch present in the source",
        _src.count(_marker) == 1, _src.count(_marker))
```

and reads `revert mutant KILLED` → `C2-PREDICATE-MET` (rc 0). This is the bound the counter header
already discloses ("the kill conjunct runs the mutant on disk only … a self-test that sniffs its own
source for BASE_LINE would read KILLED; reviewers read the arm"), now measured. It does **not** let a
world skip the honest change: the truth table calls both public checks on fixture inputs, so a
source-sniffing arm does not move the truth table at all: without a behavioural fix the table reads
`mismatches 8 of 28` (the pre-data base reading, `receipts/c2-base.txt`), and a source sniff cannot
change that. The defence is the reviewer conjunct; the builder's arm (`ExecAnchorR100.patch`) is
behavioural (it calls `check_citation_resolves`/`check_governance_citations`), so the landed arm is
not this shape.

### F3 — `checklist_confined`'s self_test window extends past the function body (severity: low-medium)

`SELFTEST_RE = r"^def self_test\(\).*?(?=^def )"` deletes everything from `def self_test()` to the next
**top-level** `def `. In the base file that span includes the module-level code between
`return 1 if failures else 0` and `def build_parser()` (the `# --- cli` comment block). Any module-level
statement written there is invisible to the confinement conjunct, while it *is* executed at import by
the truth table and by the gate.

World `w3b-blind-window-extra` puts the honest fix in place and adds, in that window,

```python
_strip_before_round100 = strip_token_dressing
strip_token_dressing = lambda tok: _strip_before_round100(tok.rstrip(";"))
```

and reads `confined=True` (above), `frozen 3 of 3`, `mismatches 0 of 28`, `C2-PREDICATE-MET`
(`counter-w3b-blind-window-extra.txt`). The file therefore contains unreviewed module-level code that
the evidence line "confined to the fix line, self_test and one retired row" explicitly denies. The
behavioural conjuncts still pin the comma-anchor surface (a lambda that reverted the fix would read
`mismatches 8 of 28`), so this is an evidence overclaim rather than a way to pass without the fix —
but it is the hiding place for any change the truth table does not sample (e.g. a second anchor form,
a fixture-keyed special case, a `check_governance_citations` override keyed on `corrections != ()`).

Minimal fix: bound the window by the function's real extent — `ast.parse`, take the `FunctionDef`
named `self_test`, and delete `lines[node.lineno-1:node.end_lineno]` — instead of the next `^def `.
That keeps the admitted shape (one insert-only region inside `self_test`) and refuses w3b. Probed
(`fix-probes.txt`):

```
ast-window probe honest candidate           confined=True
ast-window probe w3b-blind-window-extra     confined=False bytes differ outside {fix line, self_test body, corrections}
ast-window probe w2-source-sniff-arm        confined=True
```

### F4 — the corrections conjunct is exact and order-sensitive (no finding)

`w4-row-edited` edits the retired row's stale token (`…:30,37` → `…:30`) instead of removing it:
`confined=False (corrections rows are not the base rows minus the one retired row)`, and the real-tree
gate is RED from the fail-closed correction check. The comparison is list equality against
`base rows minus the one retired row`, so an edit, a reorder, a duplicate or an addition is refused.
The world cannot reach MET.

### F5 — the truth table and the gate are both foolable by a path-keyed special case; the kill conjunct is what refuses it

World `w7-fixture-special-case` (no fix line) replaces `citation_resolve` in the blind window with a
lambda that answers True for `corpus/lessons/x.md:<comma anchor>` **and** for
`round-80-verifier-spotcheck.md:<comma anchor>`:

```python
_cit_before_round100 = citation_resolve
citation_resolve = lambda tok, repo: True if re.search(
    r"(corpus/lessons/x\.md|round-80-verifier-spotcheck\.md)"
    r":\d+(-\d+)?(,\d+(-\d+)?)*$", tok) else _cit_before_round100(tok, repo)
```

Measured on that module: truth table `0 of 28` mismatches **and** the real-tree governance check
`('PASS', 1666)` — the two conjuncts that are supposed to prove the behaviour are both satisfied
without `strip_token_dressing` changing at all. What refuses the world is (a) the kill conjunct:
`FIX_LINE` is absent → `revert mutant ABSENT`; and (b) the confinement: the base line is still in
place where the counter's normalised base has `FIX_LINE`. So the predicate's load-bearing conjuncts
here are the *byte* ones, not the behavioural ones — which is the mirror image of F2 (where the
behavioural conjuncts carry the weight and the kill is fakeable). Both facts follow from the same
design: the behavioural evidence is a frozen fixture world, and the byte evidence has a blind window.

Note the world also shows why `checklist_confined` must not be relaxed: a fixture-keyed special case
is invisible to the truth table's *content* (the fixture path is frozen in `ROWS`) and is only caught
by the byte comparison.

## Part (b) — mutants of the new regex and the new arms (candidate `c20dd7a`)

Detector: `python3 -B verifiers/verify_skill_checklist.py --self-test` in the candidate checkout;
KILLED = exit 1 with a `self-test FAIL: ` line and `N failure(s) over M assertions`, N ≥ 1.
Honest candidate: exit 0, `0 failure(s) over 1886 assertions`, sha256 `e66e7da1…95f8b0`.

| mutant | defect | verdict | witness |
|---|---|---|---|
| R1-single-element | `(,\d+(-\d+)?)$` — one list item only | KILLED (8 failures) | arm `…:10,18,34,40-42` |
| R2-plus | `(,\d+(-\d+)?)+$` — a comma item required | KILLED (6) | arm `…:42` |
| R3-charclass | `:[\d,-]+$` | KILLED (4) | red arms `…:30,,37`, `…:,30` |
| R4-unanchored | trailing `$` dropped | KILLED (4) | red arms `…:30,abc`, `…:30,,37` |
| R5-space-after-comma | `(,\s*\d+(-\d+)?)*$` | **SURVIVED** | **equivalent** on every surface reachable through the two public checks: citation tokens are `\S+` splits, so a space can never sit inside a token; no pool token differs |
| R6-no-rstrip | `tok.rstrip(TRAILING_PUNCT)` dropped | KILLED (2) | arm `…:30,37,` |
| R7-no-range | `(-\d+)?` dropped | KILLED (4) | arm `…:1-2` |
| R8-cap-two | `(,\d+(-\d+)?){0,2}$` | KILLED (2) | arm `…:10,18,34,40-42` |
| R9-optional-trailing-comma | `(,\d+(-\d+)?)*,?$` | **SURVIVED** | **equivalent**: the rstrip already removes the trailing comma before the regex; no pool token differs |
| R10-empty-digits | first `\d+` → `\d*` | KILLED (2) | red arm `…:,30` |

8 of 10 killed; the two survivors are provably equivalent on the reachable surface (named, not
excused). The arms also caught R1/R2/R7 twice over (`citation-anchor-ok` from the pre-existing
self-test fires as well), i.e. the new regex is pinned by older arms too.

Arm mutants (the self-test cannot see its own weakening; the witness is the defect that survives
behind the weakened arm, `witness-arms.txt`):

| arm mutant | effect | self-test | regex/checker defects that then survive |
|---|---|---|---|
| A1-no-governance-arms | the 11 governance arms dropped | SURVIVED (1879 assertions) | governance-only defect (`check_governance_citations` resolving comma tokens raw): KILLED with honest arms (4 failures), **SURVIVED** behind A1 |
| A2-no-red-arms | both `red_tokens` loops dropped | SURVIVED (1871) | R3, R4, R10 survive behind it |
| A3-source-sniff | arms replaced by a source sniff | SURVIVED (1865) | R4, R6, R8 survive behind it (and the BASE_LINE revert is still "killed" — F2) |
| A4-not-FAIL-is-pass | ok arms accept `status != "FAIL"` (N/A passes) | SURVIVED (1886) | trigger-side N/A tolerance is backstopped: the same defect also drops the governance subject, so the governance arms' `evaluated == 2` fires (4 failures). No defect in this probe set exploits A4 alone. |

Reading: the trigger-side ok/red arms are the load-bearing pair (A2 and A3 both open R3/R4/R6/R8/R10);
the governance arms are not load-bearing for any regex mutant (the same helper serves both paths) but
they are load-bearing for a governance-only defect (A1's witness), so all 22 arms are justified — the
governance half is the only detector for the governance path's use of the helper.

## Restoration evidence

`mutants.txt` and `witness-arms.txt` print `restored True` per mutant (sha256 of the checklist after
restore equals `e66e7da1ef778d4cdaa33dee71ad34f6c12ad2cbb975f371e5af68712595f8b0`), and a final
`final restore sha256 … OK`. The counter never writes to the measured repo; no lane file was touched.

## Risks / bounds of this probe

- Part (a) worlds are built by me, so they are plausible cheats, not a proof of completeness; the
  conjuncts I could not break are reported as such (F4, F5).
- The part (b) table was first taken on base + `ExecAnchorR100.patch` (the other two patches did not
  exist yet) and then re-taken on the full ordered candidate `0f86d4cc`; the checklist blob is the
  same in both, so the table is exact for the full candidate. If the L1 re-lands the checklist (a
  changed blob), the table must be re-run.
- The candidate's corpus gates are red (unindexed round-99 spot-check lesson, new round-100 lesson):
  that is landing no-harm work, not a C2 failure, and the C2 counter does not read the corpus gates
  (`counter-*.txt` show `battery exit 1 ok` with `tip battery exit 0: 4 of 6`).
- The battery conjunct dominates each counter run (~190 s in `check_assertion_floors`); two runs at a
  time were used, as allowed.
- F1/F3 are counter defects: reported, never rescued. No counter byte, plan byte or frozen predicate
  was modified by this seat.
