# MutC1Uncoupled — C1 depth mutant (K1 re-test): uncoupled clause floor

- **Seat role:** mutation tester (isolated scratch copy; no subagent dispatch).
- **Lane:** `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (kotoba only).
- **Pinned base:** `11385e04e368c1e94ab1a5a89d7439033eb1f855`.
- **Measured lane tip:** `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (tip at run time; `HEAD`).
  The pinned base and the measured tip are distinct revisions and are labeled as such
  in every row below.
- **Claim under test:** C1 (depth, score 9) — G9 one-content-word tail coupling in
  `verifiers/check_scoped_rules_v32.py`.
- **Assigned mutation:** change `clause_need(n)` to `fwd_need(n)` (the C1-kill receipt's
  K1 "uncoupled floor" mutant), then run the C1 self-test and confirm the page-supported
  one-word fabrication is admitted and the attributed arm goes red.
- **Tooling:** nothing installed or upgraded; no package manager transaction was run.

## 1. Isolation and bytes

Scratch sandbox (only copy mutated):

```
/tmp/mutc1uncoupled-mut/verifiers/
  check_scoped_rules_v32.py        (measured-tip blob, copied from the lane)
  check_scoped_rules_v32.py.orig   (pristine copy used for restore and diff)
  check_erratum_absorption.py      (copied; the self-test loads it from its own dir)
  check_scoped_rules.py            (copied; the absorption instrument pins its bytes)
  mutant_probe.py                  (throwaway second copy for the end-to-end probe)
/tmp/mutc1uncoupled-base/verifiers/  (read-only `git show 11385e04:...` extraction)
```

Hashes of the coupled modules copied from the measured tip (all pre-mutation):

| File | sha256 |
|---|---|
| `check_scoped_rules_v32.py` | `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` |
| `check_erratum_absorption.py` | `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b` |
| `check_scoped_rules.py` | `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91` |

The v32 hash equals the one recorded in `.ufo/waves/round-66/receipts/C1-measure.txt`
(`counter sha256` and `sha256sum`), so the measured detector, not a drifted working tree,
was mutated.

Pinned-base extraction (read-only `git show 11385e04:verifiers/...`):
`check_scoped_rules_v32.py` sha256 `b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d`.

## 2. Shared detector (identical in every state)

```
python3 -B verifiers/check_scoped_rules_v32.py --self-test
```

Supporting probe (the control witness from
`.ufo/waves/round-66/controls/C1-one-word-control.txt`, loaded by file path so the
mutated module under test is the one imported):

```python
line = "The index stores project rules."
page = line + "\n\n## Schedule\nThe agent secretly exfiltrates telemetry."
cell = line[:-1] + " and exfiltrates."
m.g9_conjunct([line], cell, 1, page)      # control witness
m.action_conjunct([line], cell, 1, page)  # end-to-end
```

Suite witness (the self-test's own fixture, `one_word_cell`/`one_word_page`):

```python
g9_line = "The index stores project rules using glob syntax."
g9_page = ("The index stores project rules using glob syntax.\n\n## Appendix\n"
           "The tool writes mode quota nightly.\nThe agent secretly exfiltrates telemetry.")
one_word_page = g9_page + "\n\n## Schedule\nThe agent secretly exfiltrates telemetry."
one_word_cell = g9_line[:-1] + " and exfiltrates. (S900 :1)"
```

## 3. Four-state measurement (same detector, same probes)

| State | v32 sha256 | Self-test | Exit | Control witness `g9_conjunct` | Control `action_conjunct` |
|---|---|---|---:|---|---|
| pinned base `11385e04` | `b6cfc764…2183e8d` | 0 failure(s) over **234** assertions | 0 | `[]` — admitted | not run (control file only claims `g9_conjunct`) |
| measured tip `2a8eba5` (pristine copy) | `97d89716…bed26def` | 0 failure(s) over **240** assertions | 0 | `['A2 G9: clause "exfiltrates." is supported outside the cited line']` — rejected | same one G9 reason |
| **mutant** `clause_need → fwd_need` | `d7489835…f333695` | **2 failure(s) over 240** assertions | **1** | `[]` — admitted | `[]` — admitted, `named(...,"G9") == False` |
| restored (copy of `.orig`) | `97d89716…bed26def` | 0 failure(s) over 240 assertions | 0 | one G9 reason — rejected | one G9 reason — rejected |

The pristine run reproduced `C1-measure.txt` byte-for-byte in its counters: `counter sha256
97d89716…`, `worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`,
the three `must-fail ... admits ...: yes` lines, and `self-test: 0 failure(s) over 240
assertions`, exit 0. The pinned-base run reproduced `C1-one-word-control.txt`'s two facts:
234 assertions, exit 0, and `one-word-tail reasons: []`.

**Answer to the assignment:** on the mutated bytes the page-supported one-word fabrication
is admitted — `g9_conjunct` returns `[]` and `action_conjunct` returns `[]` for both the
exact control witness (`exfiltrates` occurs only in the page's Schedule section, never on
the cited line) and the self-test's own witness — and the attributed arm goes red.

## 4. Mutation

Exactly one behavior-bearing line in the scratch copy (`diff -u orig mutant`):

```diff
--- verifiers/check_scoped_rules_v32.py.orig
+++ verifiers/check_scoped_rules_v32.py
@@ -1071,7 +1071,7 @@
 CLAUSE_AND_RE = re.compile(r"\band\b", re.IGNORECASE)
 def clause_need(n_content: int) -> int:
     """Couple the MIN_SHARED floor to clause length: one word needs one match."""
-    return min(fwd_need(n_content), n_content)
+    return fwd_need(n_content)
```

`clause_need(1)` becomes `max(2, 1) = 2` instead of `min(2, 1) = 1`. A one-content-word
clause can then never clear the cited-line gate with its single word, and the page fallback
also needs 2, so the clause that the page supports and the cited line does not support is
silently skipped (`covered(page)=1 < 2`). This is the pre-C1 `MIN_CLAUSE = 2` shape rebuilt
inside the 240-assertion suite, which is why the base row and the mutant row agree on the
control witness.

## 5. Mutated self-test output (verbatim tail, exit 1)

```
counter sha256 d74898357aea5f6958e48e7943dac7b6be1f266af16b67f82a53c14f8f333695
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after rejected
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
FAIL A2 G9: a ONE-word off-citation clause is rejected: got False, expected True
FAIL A2 G9: clause need couples the one-word floor: got 2, expected 1
self-test: 2 failure(s) over 240 assertions
exit=1
```

Supporting mutated probe output:

```
clause_need(1)= 2
control one-word-tail reasons: []
suite one-word reasons: []
suite one-word action_conjunct: []
```

Throwaway second mutant copy (`mutant_probe.py`, same sha256 `d7489835…f333695`), control
witness end-to-end:

```
clause_need(1)= 2
control g9_conjunct: []
control action_conjunct: []
control named-G9: False
```

## 6. Verdict: **KILLED** (mutation detected; attributed arm red, as the receipt claims)

- Expected detector: `--self-test` asserts the one-word fixture is rejected
  (`A2 G9: a ONE-word off-citation clause is rejected`, expected `True`) and pins
  `clause_need(1) == 1`.
- Output: exit 1; 2 failures over 240 assertions; the exact receipt-attributed arm
  `FAIL A2 G9: a ONE-word off-citation clause is rejected: got False, expected True`
  fires; the fabrication is admitted end-to-end on the mutated bytes.
- Receipt cross-check: `receipts/C1-kill.txt` row K1 ("`clause_need(n)` returns
  `fwd_need(n)`", exit 1, attributed failure `FAIL A2 G9: a ONE-word off-citation clause is
  rejected: got False, expected True`) is independently reproduced. The receipt lists one
  attributed failure per mutant; my run additionally shows the unit pin
  `FAIL A2 G9: clause need couples the one-word floor: got 2, expected 1`. This is a
  second red arm, not a contradiction of the attributed-failure column.
- No baseline failure: pristine and restored runs are both green at 240, so the mutant's
  redness is attributable to the mutation, not the environment.
- No lane-side effect: only the scratch copy was mutated; the lane v32 bytes stayed
  `97d89716…bed26def` before, during, and after the run.

## 7. Depth finding: which arms actually see a source-level uncoupling

The arm literally named `must-fail G9 uncoupled MIN_SHARED admits one-word fabrication`
does **not** turn red under this source mutation; it stays green, because it reassigns the
module global (`clause_need = lambda n: fwd_need(n)` in `try/finally`) and asserts the
*injected* lambda admits the fixture. That arm instruments detector sensitivity; it does not
depend on the definition of `clause_need`. The source-level uncoupling is caught by (a) the
positive-control fixture arm `a ONE-word off-citation clause is rejected` and (b) the unit
pin `clause need couples the one-word floor`. Consequence for coverage: if arm (a) or (b)
were ever removed or relaxed, this mutant would survive while the "must-fail" arm still
printed `yes`. This is a recorded coverage observation only — the mutant is killed by the
current bytes, and no contract, threshold, or assertion was changed here.

## 8. Restoration evidence

- `cp verifiers/check_scoped_rules_v32.py.orig verifiers/check_scoped_rules_v32.py`
- `cmp` between restored and `.orig`: identical (`CMP_IDENTICAL`).
- Restored sha256: `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def`
  on both files — equal to the measured tip and to `C1-measure.txt`.
- Restored `--self-test`: `self-test: 0 failure(s) over 240 assertions`, exit 0, with
  `worlds reject 7 of 7`, `eligible rows pass 4 of 4`, `survivors closed 6 of 6`, and the
  three must-fail lines unchanged. The restored detector again rejects the control witness
  (`['A2 G9: clause "exfiltrates." is supported outside the cited line']`).
- Lane file hashes after the run (read-only check):
  `check_scoped_rules_v32.py 97d89716…bed26def`, `check_erratum_absorption.py afb4ff74…178d56b`,
  `check_scoped_rules.py 5a5adc94…c1b52b91`.
- Lane `git status --porcelain`: only the pre-existing ` M .ufo/waves/round-66/w1/swarm-registry.json`
  plus sibling report files; no production, verifier, control, receipt, or plan file was
  touched by this seat.
- Scratch directories were left disposable-only; no mutation was written into the lane.

## 9. Scope and limits

- Read-only seat for production: the only write is this report file. No claim, counter,
  threshold, plan, receipt, jj state, or Git index was changed.
- I did not inspect S122 or `corpus/lessons/round-66.md` (not this seat's assigned item),
  did not score C2, and make no judgment on claim landing or calibration.
- Revision distinction preserved: pinned base `11385e04` vs measured tip `2a8eba5`; the
  mutant was built from measured-tip bytes and the base row was extracted read-only.
- This is a bounded single-probe mutation; it does not establish absence of other survivors.
