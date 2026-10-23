# RevClaimC1

role: reviewer/falsifier (leaf, wave 1)
item: Falsify C1's counted predicate (`plans/round-63.md` §C1) via three
attacks: (a) print-without-guard shortcut, (b) single-fixture overfit, (c) v31
baseline survival. All probes read-only; runs executed on `/tmp/revclaimc1/run/`
copies (v31 sha `a07c2269…`, v32 sha `8371f707…` at time of test; v32 is an
untracked WIP file and may keep moving).

## Findings

1. **Predicate holds as declared (v32 state `8371f707`).**
   `cd /tmp/revclaimc1/run && python3 -B check_scoped_rules_v32.py --self-test`
   → exit 0, prints verbatim:
   ```
   worlds reject 7 of 7; eligible rows pass 4 of 4
   survivors closed 6 of 6
   must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
   self-test: 0 failure(s) over 201 assertions
   ```
   All six `before accepted; after rejected` flips printed; 201 assertions, 0
   failures. No hardcoded `"6 of 6"` literal in v32: `survivors_closed` is
   `sum(...)` at `verifiers/check_scoped_rules_v32.py:2654-2656`, and the
   must-fail G9 arm (2681-2691) really stubs `current_counter.g9_conjunct`
   (module attribute, hit by `action_conjunct`'s call at :1157-1158).

2. **Attack (a) — shortcut exists only at degenerate level; structure excludes
   it inside the self-test.** Cheapest predicate-satisfier that never runs a
   guard: a ~4-line literal print + `sys.exit(0)` — the frozen text constrains
   stdout+exit only, so no verifier-side check *can* exclude it; a second
   outside counter that echoed the three lines would also "meet" the wording.
   But for a counter exercising the real machinery, the guard is load-bearing
   by construction: `survivors closed` is computed from
   `not before[ident] and after[ident]`; printing `6 of 6` while `after[G9]`
   is False fails `check("successor survivor verdicts close all six frozen
   instances", (True,)*6)` (v32:2647-2649) → exit 1, so a prints-only inflation
   still exits nonzero. The must-fail arm forces the after-rejection to come
   *through* `g9_conjunct` specifically: stub it and the frozen instance is
   admitted again (`yes`). A literal `survivors_closed = 6` cannot beat the
   tuple check. **Verdict (a): attack fails against this artifact; residual =
   predicate can't distinguish a truly trivial counter (structural scope, not
   a defect of this build).**

3. **Attack (b) — `6 of 6` games ONE frozen fixture only in principle; the real
   guard is class-level.** A `g9_conjunct` specialized on vocabulary —
   `if "secretly uploads files" in cell: return [reason]` — does pass the
   whole predicate (frozen instance rejected, no eligible row split, stub
   makes it admit): the predicate as frozen **does not require a second
   instance**. I constructed two new G9-class instances disjoint in vocabulary
   and scored them against v32's real guard:
   ```
   NEW1 (and-join): "…nightly and silently broadcasts telemetry."
        v31 action: []   (admits — matches the survivor class)
        v32 action: ['A2 G9: clause "silently broadcasts telemetry." is
                     supported outside the cited line']
   NEW3 (and-join, thin overlap): "…and quietly mirrors writes."
        v32 action: A2 aggregate-reject ('supports 3 of its 6 ... need >= 4');
        g9_conjunct itself still emits the G9 reason.
   NEW2' (';'-join): same — A2 aggregate fires first; g9 reason present.
   ```
   So `g9_conjunct` generalizes (rejecting for a per-clause reason, not the
   fixture string), while `action_conjunct`'s *first* A2 aggregate check often
   masks the G9 diagnostic on low-overlap variants — honest class closure at
   the guard level even when the emitted reason is plain A2. Bounds observed:
   (i) a clause under `MIN_CONTENT`=3 distinct content words escapes
   (`…and uploads files.` → `action_conjunct` returns `[]` — admitted; a
   <3-word off-citation clause is a real admitted sub-class); (ii) new clauses
   must clear ≥`fwd_need` on the page too, so an unsupported clause stays an
   A2 page-containment rejection, by design. **Verdict (b): no overfit defect
   in this build — the *claim itself* is one-instance bounded; semantic-class
   closure remains an uncounted bound (mirrors CriticC1Bound's inference, now
   confirmed empirically).**

4. **Borrowed-vocabulary tail (peer witness, executed).**
   CriticC1Bound's static witness — clause2 glued from the cited line's own
   words: cell `The configuration stores project rules using glob syntax and
   uploads project files using glob syntax.` vs. the frozen cited line.
   Measured under BOTH page vectors — my fuller page (`The agent uploads
   project files using glob syntax.`) and the peer's frozen original page
   (`## Unrelated section\nThe agent secretly uploads files.`): clause2 words
   {files,glob,project,syntax,uploads,using}, covered on line 4/6 ≥ need 4 →
   `g9_conjunct` returns `[]`, `action_conjunct` admits.
   The guard inherits A2's bag-of-words model, so an off-citation
   clause paraphrased from the cited line's vocabulary is counted "supported"
   — a semantic hole, but inside the instrument's declared word-support
   contract (the same fraction A2 uses). Residual risk, not a defect of the
   closure as declared.

5. **Attack (c) — v31 control fails the predicate, as required.**
   `python3 -B check_scoped_rules_v31.py --self-test` → exit 0 but prints
   `survivors closed 5 of 6`, `survivor e2f-compound-purpose-outside-citation:
   before accepted; after accepted`, and `bound: G9 remains unimplemented…`
   instead of the must-fail G9 line — only two must-fail arms. The do-nothing
   control cannot meet the predicate. **Verdict (c): predicate survives the
   v31 baseline correctly.**

6. **Residual mechanics verified.** `action_attack` scores via
   `counter.action_conjunct(lines, cell, 1, page_text)`
   (`check_erratum_absorption.py:159-164`); the must-fail stub replaces the
   module attr `g9_conjunct`, which `action_conjunct` calls — so the arm
   measures exactly the new arm, not g7 or A2. Eligible-row risk is real but
   bounded: G9 appends a reason only when clause-support fails the cited line
   AND passes the page (v32:1116-1125).

## Artifacts

Probe transcripts (run under `/tmp/revclaimc1/run/`):

```text
v32 --self-test (sha 8371f707): exit 0
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
v31 --self-test (sha a07c2269): exit 0
  survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
  survivors closed 5 of 6
  bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
```

```python
# second-instance + cheat probe (module loaded from /tmp copy of v32)
lines1 = ["The daemon prunes expired session tokens nightly."]
cell1  = "The daemon prunes expired session tokens nightly and silently broadcasts telemetry."
page1  = "The daemon prunes expired session tokens nightly.\n\n## Observability\nThe daemon silently broadcasts telemetry."
v31.action_conjunct(lines1, cell1, 1, page1)  # -> []      (admits)
v32.action_conjunct(lines1, cell1, 1, page1)  # -> ['A2 G9: clause "silently broadcasts telemetry." is supported outside the cited line']

# vocabulary-specialized cheat passes predicate structure (not the shipped guard):
def cheat(lines, cell, L, page_text=None):
    return ['A2 G9: …'] if "secretly uploads files" in cell else []
# bound 1: <MIN_CONTENT-word clause escapes: '…and uploads files.' -> []
# bound 2: borrowed-vocab clause: '…and uploads project files using glob syntax.'
#          -> g9 [] / action [] (covered 4/6 >= need 4 on the cited line)
```

## Verdict

**PROPOSES** — the counted predicate is met honestly by v32 @ `8371f707`
(three lines computed, exit 0, must-fail arm load-bearing, v31 control fails
5-of-6). To change my mind: show the frozen instance's after-rejection does
not originate in `g9_conjunct`, or a v32 revision where the must-fail arm no
longer flips the frozen instance, or the v32 file drifting so the self-test
diverges from the frozen wording (it is untracked — the L1 must pin its sha
into the receipt before close).
