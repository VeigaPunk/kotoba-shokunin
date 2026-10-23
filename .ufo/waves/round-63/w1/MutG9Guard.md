# MutG9Guard

role: mutation tester (leaf seat; no subagent dispatch, no installs, lane read-only)
item: MutG9Guard — mutate the planned G9 guard in a /tmp copy of v31 with my own
`g9_conjunct`, six mutants, each scored on the frozen survivor and the four eligible cells.

Scratch: `/tmp/mutg9` (disposable). Base bytes: `/tmp/mutg9/check_scoped_rules_v31.py`,
sha256 `a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858`.
The lane was not written; only this report was created.

## Findings

**1. The predicate is reachable, and the do-nothing control really fails it.**
`python3 -B verifiers/check_scoped_rules_v31.py --self-test` →
`worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 5 of 6` /
`bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per
CriticC1Hollow.`, exit 0. My own implementation of the plan's guard, spliced into the v31
copy (`/tmp/mutg9/build.py pristine /tmp/mutg9/p_pristine.py`; sha
`4a544729dd8414e4…`), prints the three declared lines and exits 0:
`survivors closed 6 of 6`, `must-fail G9 disabled admits
e2f-compound-purpose-outside-citation: yes`, `self-test: 0 failure(s) over 201 assertions`.
So the predicate can pass, and the guard as specified works.

**2. Mutant table (same detector on pristine/mutated/restored bytes).** Detector: the
spliced file's own `--self-test` (the frozen predicate) plus a per-cell driver
`python3 -B /tmp/mutg9/detector.py <variant>` that calls
`action_conjunct(lines, cell, L, page_text)` on the frozen instance and the four eligible
cells. All six mutant files carry my guard with exactly one behaviour-bearing change.

| mutant | change | frozen G9 | eligible rows | winner? | predicate exit | assertion that catches it |
|---|---|---|---|---|---|---|
| pristine | spec guard | rejected | 4 of 4 pass | — | 0 | — |
| M1 | split on `;` only | **admitted** `[]` | 4 of 4 pass | killed | 1 | `successor survivor verdicts close all six frozen instances` |
| M2 | split on ` and ` only | rejected | 4 of 4 pass | **SURVIVES** | 0 | none (P_SEMI admitted) |
| M3 | clause `fwd_need` → 1 | rejected | 4 of 4 pass | **SURVIVES** | 0 | none (P_ONE admitted) |
| M4 | guard returns `[]` | **admitted** `[]` | 4 of 4 pass | killed | 1 | same survivor assertion (must-fail arm still prints `yes`) |
| M5 | page support, not line | **admitted** `[]` | 4 of 4 pass | killed | 1 | same survivor assertion |
| M6 | after g7, skip backticked cells | rejected | 4 of 4 pass | **SURVIVES** | 0 | none (P_TICK admitted) |

Real outputs, `/tmp/mutg9/st_M*.out`:
`M1`/`M4`/`M5` → `FAIL successor survivor verdicts close all six frozen instances: got
(True, True, True, True, True, False), expected (True, True, True, True, True, True)`,
`survivors closed 5 of 6`, exit 1. `M2`/`M3`/`M6` → `survivors closed 6 of 6`,
`self-test: 0 failure(s) over 201 assertions`, exit 0 (byte-for-byte the pristine predicate
output apart from the sha line).

**3. The must-fail arm is not a guard-quality assertion.** M4 *is* a production guard that
returns `[]`, and its third predicate line still prints
`must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`
(`/tmp/mutg9/st_M4.out:21`), because the arm re-stubs `g9_conjunct` in process
(`verifiers/check_scoped_rules_v32.py:2682-2692`). Only the survivor matrix
(`verifiers/check_scoped_rules_v32.py:2647-2650`, `expected_after = (True,) * 6`) can kill a
no-op guard — and it is the same assertion that kills M1 and M5, i.e. G9 has exactly one
discriminating assertion in the whole self-test.

**4. The eligible-row arm can never catch an under-strict guard.** It is computed from the
live/pass flags only — `eligible_pass = sum(1 for c in FOUR if found[c])`
(`verifiers/check_scoped_rules_v31.py:2422`), inherited unchanged by v32 at 2604 — never
from `action_conjunct` reasons. All four eligible cells pass under every mutant including a
guard that never fires. Their designed role is false-positive control; they are not a
detector for G9.

**5. Three mutants survive the whole 201-assertion suite; each needs a named fixture.**
Each probe below is a genuine G9-class instance: A2 forward fraction, A2 page containment,
A2 reverse coverage and G7 are all clean and v31 admits it
(`/tmp/mutg9`, driver output: `A2+G7 alone: clean | v31 action_conjunct: admitted`).

- **P_SEMI** (catches M2, the missing `;` boundary): cited line
  `The configuration stores project rules using glob syntax.`; cell
  `…glob syntax; secretly uploads files.`; page adds `The agent secretly uploads files.`
  Pristine → `['A2 G9: clause "secretly uploads files." is supported outside the cited line']`;
  M2 → `[]`. Missing assertion: *"G9 splits a `;`-glued outside-citation clause"*.
- **P_ONE** (catches M3, the threshold): same line/page; cell
  `…glob syntax and stores files secretly.` Pristine → `['A2 G9: clause "stores files
  secretly." is supported outside the cited line']`; M3 → `[]`. Missing assertion: *"G9
  requires fwd_need, not one shared word"*.
- **P_TICK** (catches M6, the backtick skip): cited line
  `The configuration stores project rules using `globs` syntax.`; cell adds
  ` and secretly uploads files.`; page adds the unrelated sentence. Pristine → reason naming
  `secretly uploads files.`; M6 → `[]`. Missing assertion: *"G9 is not skipped when the cell
  carries a backticked identifier"*.

**6. Cross-check on the shipped v32 bytes.** `verifiers/check_scoped_rules_v32.py`
sha256 `8371f707c571b74f…` is behaviourally identical to my implementation on this detector:
G9 rejected with the same reason, eligible 4 of 4, and P_SEMI/P_ONE/P_TICK all rejected
(`python3 -B /tmp/mutg9/detector.py /tmp/mutg9/p_shipped.py`). Splicing M2, M3 and M6 into the
shipped bytes (`s_M2.py` `420cc3ef…`, `s_M3.py` `2e1b077e…`, `s_M6.py` `031559454…`) still
yields `0 failure(s) over 201 assertions`, exit 0, `survivors closed 6 of 6`. The shipped
file has no unit assertion on `split_clauses` or `g9_conjunct`
(`grep -n 'split_clauses\|g9_conjunct' verifiers/check_scoped_rules_v32.py` → only def at
1064/1098, wiring at 1116/1157, stub arm at 2682-2687), so the three mutants are invisible to
it, not merely unexercised.

**7. Why M3 matters: the frozen fixture sits at the exact A2 threshold.**
`frozen whole-cell: words=10 covered=7 need=7` (`/tmp/mutg9`, probe output). The survivor
only reaches G9 because the whole cell clears forward support by zero margin; lowering the
clause threshold to 1 is not an idle mutation but the left edge of the band the guard lives
in.

**8. Page-gate divergence (INFO, not a defect).** The shipped guard decides "page-present"
with `covered(w, page) >= fwd_need(len(w))`; the plan says page-present. Proven extensionally
equal whenever G9 is reached through `action_conjunct`: whole-cell page containment implies
every clause word is page-supported, so `covered(w, page) = |w| >= fwd_need(|w|)`. Direct
calls differ — clause `quietly uploads archives nightly` with only three of its words on the
page: mine `[]`, shipped `['A2 G9: clause "quietly uploads archives nightly" …']`. Implication
for the L1: add any new G9 unit assertions through `action_conjunct`, not `g9_conjunct`.

**9. Restoration and lane integrity.** In-place cycle on the scratch base: before
`a07c2269…`; M1 spliced in place → `a3a547ab3ef8e75e4a6872b7f21b587fe221b05a450e30346f647e551c1cd46f`,
self-test exit 1, `survivors closed 5 of 6`; restored from saved bytes → `a07c2269…`, self-test
exit 0 and the detector again reports `G9 admitted` / eligible 4 of 4, i.e. the v31 control
behaviour. Lane bytes unchanged: `check_scoped_rules_v31.py a07c2269…`,
`check_scoped_rules_v32.py 8371f707…`, `check_scoped_rules.py 5a5adc94…`,
`check_erratum_absorption.py afb4ff74…`. No pacman/uv/npx installs were made.

## Artifacts

My guard implementation (spliced into the v31 copy; mutant knobs are `G9_BOUNDARY_RE`,
`G9_NEED`, `G9_SKIP_BACKTICK`):

```python
G9_BOUNDARY_RE = re.compile(r";|\band\b", re.IGNORECASE)   # M1: r";"   M2: r" and "
G9_NEED = fwd_need                                          # M3: lambda _n: 1
G9_SKIP_BACKTICK = False                                    # M6: True


def _g9_mask(cell):
    mask = bytearray(len(cell))
    in_code = False
    for i, ch in enumerate(cell):
        if ch == "`":
            in_code = not in_code
            mask[i] = 1
            continue
        mask[i] = 1 if in_code else 0
    return mask


def split_clauses(cell):
    mask = _g9_mask(cell)
    clauses, start = [], 0
    for m in G9_BOUNDARY_RE.finditer(cell):
        if any(mask[m.start():m.end()]):
            continue
        clauses.append(cell[start:m.start()])
        start = m.end()
    clauses.append(cell[start:])
    return [c.strip() for c in clauses if c.strip()]


def g9_conjunct(lines, cell, L, page_text=None):
    if <M4 knob: True>:
        return []
    if L is None or not cell or L < 1 or L > len(lines):
        return []
    line_w = content_words(lines[L - 1])
    page = page_words(page_text if page_text is not None else "\n".join(lines))
    reasons = []
    for clause in split_clauses(cell):
        w = content_words(clause)
        if len(w) < MIN_CONTENT:
            continue
        if covered(w, line_w) >= G9_NEED(len(w)):      # M5: covered(w, page)
            continue
        if all(supported(x, page) for x in w):
            reasons.append('A2 G9: clause "%s" is supported outside the cited line'
                           % clause)
    return reasons
```

Wiring in `action_conjunct` (pristine, M1-M5): `return g7_conjunct(lines, cell, L,
page_text) + g9_conjunct(lines, cell, L, page_text)`. M6 wiring:
`g7_reasons = g7_conjunct(...); if g7_reasons or (G9_SKIP_BACKTICK and
BACKTICKED_IDENTIFIER_RE.search(cell)): return g7_reasons; return g9_conjunct(...)`.

Probe fixtures (each admitted by v31; each rejected by the pristine guard):

```python
P_SEMI_LINES = ["The configuration stores project rules using glob syntax."]
P_SEMI_CELL  = "The configuration stores project rules using glob syntax; secretly uploads files."
P_ONE_CELL   = "The configuration stores project rules using glob syntax and stores files secretly."
P_TICK_LINES = ["The configuration stores project rules using `globs` syntax."]
P_TICK_CELL  = "The configuration stores project rules using `globs` syntax and secretly uploads files."
PAGE         = ("The configuration stores project rules using glob syntax.\n\n"
                 "## Unrelated section\nThe agent secretly uploads files.")
```

Replay (stdlib python3 only; files under `/tmp/mutg9`):
```
python3 -B build.py pristine|M1|M2|M3|M4|M5|M6|shipped out.py
python3 -B out.py --self-test          # the frozen predicate
python3 -B detector.py out.py          # per-cell JSON: G9, four eligible rows, P_*
```
Variant hashes: `p_pristine.py 4a544729…`, `p_M1.py a3a547ab…`, `p_M2.py 8aa8b010…`,
`p_M3.py b5f69a68…`, `p_M4.py 33446172…`, `p_M5.py 9a47b4ab…`, `p_M6.py 1577a6e3…`,
`p_shipped.py 8371f707…`, `s_M2.py 420cc3ef…`, `s_M3.py 2e1b077e…`, `s_M6.py 031559454…`.

Proposed added assertions (text only; I did not touch v32):
```python
check("G9 splits a `;`-glued outside-citation clause",
      action_conjunct(P_SEMI_LINES, P_SEMI_CELL, 1, PAGE), [...reason...])
check("G9 requires fwd_need, not one shared word",
      action_conjunct(P_SEMI_LINES, P_ONE_CELL, 1, PAGE), [...reason...])
check("G9 is not skipped when the cell carries a backticked identifier",
      action_conjunct(P_TICK_LINES, P_TICK_CELL, 1, PAGE), [...reason...])
```

## Verdict

ATTACKS. The plan's guard is sound and my independent implementation closes G9 (6 of 6,
exit 0), but the frozen predicate's power over G9 rests on one fixture plus a stub arm that
cannot distinguish a working guard from a no-op (M4 prints `yes`). M2 (`;`-only split), M3
(threshold 1) and M6 (backtick skip) each admit a real G9-class instance while the predicate
prints all three lines and exits 0 — on my bytes and on the shipped v32 bytes alike. That is a
missing-assertion finding, not a contract change: the contract's `6 of 6` still holds and the
three named fixtures would make each mutant fail (exit 1) while pristine stays `6 of 6` / `4 of 4`.

What would change my mind: adding P_SEMI/P_ONE/P_TICK through `action_conjunct` and observing
M2/M3/M6 flip to exit 1 with the pristine still exit 0, or a reasoned argument that the
shipped `covered(w, page) >= fwd_need` page gate makes one of the three probes unreachable
(I could not reach a difference through `action_conjunct`; finding 8 shows the gates
coincide there).
