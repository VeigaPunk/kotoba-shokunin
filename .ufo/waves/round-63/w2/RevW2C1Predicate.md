# RevW2C1Predicate

role: reviewer/falsifier (leaf seat, wave 2 — no subagent dispatch)
item: Attack the C1 counted predicate **as committed at cbbee56e**; verify the
three frozen lines verbatim + exit 0, `survivors_closed` computed (no hardcoded
6), the must-fail G9 arm stubs `g9_conjunct` in-process, and the stale receipt
`.ufo/waves/round-63/receipts/C1-g9-measure.txt` (v32 sha `552308806b…`, 205
assertions) vs the committed bytes (sha `4246069129…`, 208 assertions).

Method: clean pinned copy — `git archive cbbee56e9a3589b0b46736ad36f1b77701def80e
| tar -x -C /tmp/r63-w2-c1pred` (tree `924deea54f55d8f3dc7a61cd0c377ab2c36c643f`,
6116 files). The lane was never mutated; all probes ran under /tmp. No tool
installs needed (system python3 only).

## Findings by severity

### 1. [DEFECT — the assigned one] Committed C1 receipt is one v32 revision stale

`.ufo/waves/round-63/receipts/C1-g9-measure.txt` **is tracked** at cbbee56e
(`git ls-files` lists it; committed bytes == working bytes, sha256 of the file
`911780714b…`). It records:

```
v32 sha256 552308806b17e0e48fedb083eb6d55b722a7ef080aa7de8402601bbbc27d8f39
base 35d44b4b4dcdda234b5dbff7af37e432fec55f05 (working tree)
...
self-test: 0 failure(s) over 205 assertions
```

The committed verifier prints `counter sha256
4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33` (identical to
`sha256sum verifiers/check_scoped_rules_v32.py`, so `self_sha()` reads own bytes
honestly) and `self-test: 0 failure(s) over 208 assertions`. The receipt predates
the three G9 mutant-killer probe checks (`check_scoped_rules_v32.py:2739-2754`,
"G9 probe … is rejected as supported outside the cited line" — the
semicolon-split / one-supported-word / backticked-cell probes landing
MutG9Guard's M2/M3/M6 findings), which is exactly the 205→208 delta (an even
earlier wave-1 measurement at sha `8371f707…` over 201 assertions is recorded in
w1/RevClaimC1.md and w1/MutG9Guard.md). The receipt's `base 35d44b4b…(working
tree)` line also names the wrong revision for a committed-bytes claim.

**Smallest safe correction (L1 must land):** re-run
`python3 -B verifiers/check_scoped_rules_v32.py --self-test` at cbbee56e and
replace the receipt with:

```text
C1 predicate: python3 -B verifiers/check_scoped_rules_v32.py --self-test
v32 sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
measured at cbbee56e9a3589b0b46736ad36f1b77701def80e
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
self-test: 0 failure(s) over 208 assertions
exit=0
```

Minimal alternative: edit three tokens in place — sha `552308806b…` →
`4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`, `205` → `208`,
`base 35d44b4b…(working tree)` → `measured at cbbee56e…`. The sha and the
assertion count MUST change; the survivor/must-fail lines are already accurate.
Other references to the stale sha (`w1/ScribeLesson.md`, `w2-spec.json`,
`w2-dispatch.json`) are historical evidence / dispatch metadata describing the
defect itself — no fix needed. LOG.md carries no v32 sha reference.

### 2. [VERIFIED] Three frozen lines print verbatim; exit 0; deterministic

`cd /tmp/r63-w2-c1pred && python3 -B verifiers/check_scoped_rules_v32.py
--self-test` → exit 0, verbatim:

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
```

Two consecutive runs byte-identical (`diff` clean). Exit path honest:
`sys.exit(main())` → `return self_test()` → `return 1 if failures else 0`
(:2763, :2787, :2852); `failures`/`assertions` are incremented inside `check()`
(:1745-1748), never literals. Any failed check forces a nonzero exit — a green
run cannot print `6 of 6` while a survivor is still admitted
(`check("successor survivor verdicts close all six frozen instances",
tuple(bool(after[i]) …), (True,)*6)` :2681-2682).

### 3. [VERIFIED] `survivors_closed` is computed; denominator is structurally pinned

`check_scoped_rules_v32.py:2687-2689`:

```python
survivors_closed = sum(1 for ident in survivor_ids
                       if not before[ident] and after[ident])
print("survivors closed %d of 6" % survivors_closed)
```

`before` is scored against the *sha-pinned r61 bytes*:
`absorption.load_counter(absorption.COUNTER_PATH)` (:2655) double-pins
`verifiers/check_scoped_rules.py` — file digest and imported-module
`self_sha()` both required to equal `COUNTER_SHA256 =
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`
(check_erratum_absorption.py:15, 78-98); measured sha256 of the committed r61
file is exactly `5a5adc94…`. `after` is scored against
`sys.modules[__name__]` (:2656). The literal `of 6` denominator cannot silently
drift: `check("all six frozen survivor instances were loaded",
frozenset(attacks), survivor_id_set)` (:2673) pins the survivor set to six, and
the `(True,)*6` tuple checks pin both directions. Same for `of 4` (pinned by
`check(eligible_pass, 4)` :2643) and `of 7` (`check((rejected, len(worlds)),
(7,7))` :2639-2640). Cosmetic nit only: the format literals could read
`%d of %d` with `len(survivor_ids)`/`len(FOUR)` — safe as committed.

### 4. [VERIFIED] Must-fail G9 arm really stubs `g9_conjunct` in-process

`current_counter = sys.modules[__name__]` (:2656), so
`current_counter.g9_conjunct = lambda *_args: []` (:2717) mutates the module
global that `action_conjunct` calls **bare** at :1164
(`return g7_conjunct(...) + g9_conjunct(...)` — call-time module-dict lookup).
`try/finally` restores the real function (:2720). The scored path is
`attack.score → counter.action_conjunct(lines, cell, 1, page_text)`
(check_erratum_absorption.py:159-164) on the frozen fixture (absorption
:221-227: cited line stops at `glob syntax.`, `and`-glued `secretly uploads
files.` clause, page's unrelated section carries those words — matches the
plan's declared instance). Stub returns `[]` → `g9_admitted = not [] → True` →
`yes`. The arm proves `g9_conjunct` is load-bearing for this instance; the
`expected_after` check proves the *unstubbed* guard rejects it. Both directions
exercised in one run.

All fetch/state isolation is in-process too: `score()`/`cli()` save and restore
`BASE`, `TARGET`, `lane_dir`, `run_curl` globals around a dict-fed
`run_curl` lambda (:2455-2463, :2490-2503); W4's `arm=live` line is
dict-served, zero network. Temp dirs use `mkdtemp(prefix="csr-world-")` (:2278)
and are `shutil.rmtree`'d in `finally` (:2764-2766) — no scratch leaked.

### 5. [VERIFIED] Controls behave as declared

- Do-nothing control: v31 at committed bytes (sha `a07c2269ea077e48…`, matching
  the plan's motivating evidence) prints `survivors closed 5 of 6`,
  `survivor e2f-compound-purpose-outside-citation: before accepted; after
  accepted`, `bound: G9 remains unimplemented…`, only two must-fail arms, 201
  assertions, exit 0 — cannot meet the predicate. Matches
  `controls/C1-do-nothing-v31.txt` modulo the nit in §6.
- Label control: stubbed g9 admits → prints `yes` and still exits 0 only because
  the stub is restored before the probes; a *permanently* admitting guard is
  killed by the `expected_after` check (MutG9Guard M4 verified this earlier).

### 6. [RESIDUAL RISK / BOUND UPDATES]

- **RevClaimC1's sub-`MIN_CONTENT` escape bound is CLOSED at committed bytes.**
  Committed `g9_conjunct` counts clause words with `page_words` (keeps
  backticked spans) and floors at `MIN_CLAUSE = 2` (:1124-1125, :1062). My probe
  on the clean tree:
  `action_conjunct(lines, "…glob syntax and uploads files.", 1, page)`
  → `['A2 G9: clause "uploads files." is supported outside the cited line']`
  — the 2-word clause no longer escapes. Page-absent clause correctly stays an
  A2 page-containment rejection (`files, uploads do not occur on the committed
  snapshot`), no double-report.
- **MutG9Guard M2/M3/M6 addressed:** the three committed probes (:2739-2754)
  check `any(r.startswith("A2 G:") for r in action_conjunct(...))` — through
  `action_conjunct`, per MutG9Guard's own recommendation (its finding 8).
- **Still-open residual (inside declared contract):** bag-of-words paraphrase
  hole — a clause glued from the cited line's own vocabulary counts as
  "supported" (RevClaimC1 §4, CriticC1Bound). Inside the instrument's declared
  word-support contract; not a defect of this closure.
- **Still-open structural bound:** the must-fail arm proves load-bearingness on
  the ONE frozen instance; a no-op guard for *other* instances is caught only by
  the three named probes, not by a class-level detector. The eligible-row arm is
  a false-positive control by design and never reads `action_conjunct` reasons.
- **[COSMETIC]** `controls/C1-do-nothing-v31.txt` omits the two `e2c-*` survivor
  lines v31 actually prints (my run shows all six); the C1 receipt includes all
  six. Curated digest, accurate lines — inconsistent convention, no falsity.

## Verdict

**PROPOSES — C1's counted predicate holds on the committed bytes.** All three
frozen lines print verbatim, exit 0, computed numerators, real in-process
stubbing, real sha-pinned frozen counter for `before`, deterministic and
offline. **One required L1 correction: refresh
`.ufo/waves/round-63/receipts/C1-g9-measure.txt` to sha `4246069129…` / 208
assertions / `measured at cbbee56e…`** — the committed receipt describes one
v32 revision earlier (three-token in-place fix or the replacement text in §1).
Residuals: paraphrase-hole (declared contract), one-instance must-fail arm plus
three mutant probes (structural bound), cosmetic literal denominators and a
truncated v31 control digest.

Verification exercised: `git archive` extract → two `--self-test` runs (diff
clean, exit 0), v31 control run, source reads of every counting/stub site,
sha256sums of v32/v31/r61-counter/receipt, `git ls-files`/`log`/`show` on lane
(read-only), bound-closure probe via imported module. Not verified: behavior
under Python implementations other than CPython 3 (out of scope), LSP
unavailable/unnecessary for a self-contained stdlib script.
