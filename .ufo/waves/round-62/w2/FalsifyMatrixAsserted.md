# FalsifyMatrixAsserted — is the absorption summary computed, or would asserted records pass?

Date: 2026-10-23 (UTC). Seat: `L1kotoba62.FalsifyMatrixAsserted`. Axes: **depth + calibration**.
Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, stated tip
`e6da78bbe420722dd18a13182a7c4b64ce02f005` (verified ancestor of HEAD `3f911504…`;
`git merge-base --is-ancestor` exit 0; instrument bytes identical at both revs,
`git show <rev>:verifiers/check_erratum_absorption.py | sha256sum` → `afb4ff74…` twice).
Lane read-only except this report; all probes ran under `/tmp` (`/tmp/fake_matrix.py`,
`/tmp/fake_scorer.py`, `/tmp/r62assert/`).

## Target bytes (re-hashed)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && sha256sum verifiers/check_erratum_absorption.py verifiers/check_scoped_rules.py
afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b  verifiers/check_erratum_absorption.py
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  verifiers/check_scoped_rules.py
```

Both match the receipt (`C1-absorb-measure.txt:3-4`). The real gate was re-run at HEAD
and reproduces the receipt verbatim:

```
$ python3 -B verifiers/check_erratum_absorption.py --self-test   # at HEAD 3f911504
…
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
… six survivor rows identical to C1-absorb-measure.txt:12-17 …
exit=0
```

## Verdict: the instrument has a hollow class — confirmed, with construction

`summarize()` **computes** the line from whatever `MatrixRun` it is given
(`:371-398`: `absorbed`, `flips`, `survivors`, `controls` are all folded over
`run.baseline`/`run.mutations`/`run.controls`). The defect is upstream:
`validate_run()` (`:326-355`) validates **shape only, never provenance or content**.
Every require is structural:

| check | line | what it verifies | what it ignores |
|---|---|---|---|
| `isinstance(run, MatrixRun)` | 327-328 | type tag | how the run was produced |
| `set(run.baseline) == names` | 330 | 5 keys | anything else |
| `observation.ids == expected_ids and len(observation.reasons) == 2` | 331-335, 341-345 | idents + tuple arity | reason contents, types, truthiness |
| `set(run.mutations) == names`, inner sweep keys | 336-340 | key sets | same |
| controls ids/arity | 346-354 | key sets + arity | same |
| cross-mutation invariance `verdicts(changed[other]) == verdicts(baseline[other])` | 364-369 | tuple equality | satisfied by object identity |

Nothing compares a reason to the counter; `bool(reasons)` is the only predicate ever
applied to a reason tuple (`:359,379-383,392-395`).

### Construction 1 — direct `MatrixRun` forgery (constant reasons, 0 counter calls)

`/tmp/fake_matrix.py` builds a `MatrixRun` whose only true facts are the instance
**idents** (copied from `ERRATA`/`control_pairs()`); every reason is the constant
`("asserted-rejection",)` or `()`:

- baseline: E2/E2b `[REJ,REJ]`; E2c/E2e/E2f `[ACC,ACC]`
- mutations: diagonal cells for E2/E2b `[ACC,ACC]`; **every off-diagonal cell is the
  baseline `GroupObservation` object itself** (invariance by identity)
- controls: `absorbed-control` before `[REJ,REJ]`/after `[ACC,ACC]`;
  `surviving-control` `[ACC,ACC]` both ways

```
$ python3 -B /tmp/fake_matrix.py
FAKE-A (E2+E2b asserted absorbed): ACCEPTED by summarize
  errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
  guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
  survivor E2c e2c-wrong-supersedes-target: []
  … (all six survivor rows, byte-identical to the receipt) …
  self_test floors: measured==5 True; controls==2 True
FAKE-B (all 5 asserted absorbed): ACCEPTED by summarize
  errata measured 5 of 5; absorbed 5 of 5; surviving 0; controls 2 of 2
  guard flips: E2 2; E2b 2; E2c 2; E2e 2; E2f 2
  self_test floors: measured==5 True; controls==2 True
STRING-AUDITOR: REJECTED: auditor supplied a label/constant, not arm-level run records
exit=0
```

FAKE-A reproduces the committed receipt **exactly** — headline, flips row, and every
survivor line — from pure constants. FAKE-B shows the summary floors never bound the
answer: `absorbed 5 of 5; surviving 0` passes every require in `summarize` and the two
`self_test` floors (`:434-435`); per erratum E1 (`plans/round-62.md:255-261`) the
predicate's exit criterion is only `measured` + `controls`, so even the maximal lie is
inside spec. The string auditor dies only on the `isinstance` check at `:328`.

### Construction 2 — scorer injection through the real `run_matrix` (still 0 arm calls)

`/tmp/fake_scorer.py` drives the **unmodified** `run_matrix` with a scorer that never
invokes `attack.score(counter)`. It sniffs whether the counter's guard attribute is
currently a foreign stub (`getattr(counter, attr).__module__ != counter.__name__` —
the `patched()` context at `:305,315` swaps module identity):

```
$ python3 -B /tmp/fake_scorer.py
counter module name: check_scoped_rules_frozen
evil-scorer run through real run_matrix: ACCEPTED by summarize
  errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
  … identical flips and six survivor rows …
exit=0
```

The only check a scorer output meets is `score_one`'s list-of-str guard (`:251-252`);
`sniff_scorer` returns `["asserted-rejection"]`/`[]`. So a per-arm verdict is produced
**without a single counter arm executing**.

### Construction 3 — end-to-end mutant (gate survives `--self-test`)

Sandbox `/tmp/r62assert/`: byte-identical instrument + pinned counter (hashes above),
one edit — inject `sniff_scorer` and change `self_test`'s first line to
`run_matrix(counter, scorer=sniff_scorer)`:

```
$ cd /tmp/r62assert && python3 -B check_erratum_absorption.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
exit=0
```

All 11 stdout lines are byte-identical to `C1-absorb-measure.txt:8-17`, produced by a
matrix in which **zero counter arms were scored**. This is strictly stronger than
`FalsifyMatrixMutants.md` m3 (headline-only forgery): here headline, flips, and every
survivor row are internally consistent *and* fabricated — no contradiction exists for a
reviewer to catch.

## Why the three self-test negative arms do not cover it (`self_test` :438-460)

- `summarize(hollow_label_auditor())` (:439-444): kills a `str` via the `isinstance`
  at :328 — my forgeries are real `MatrixRun` objects.
- `check_content_variant(counter, label_scorer)` (:447-452): `self_test` hard-codes
  `real_scorer` at `:436` for its own variant arm, so an injected scorer never reaches
  it; the label table fails only because original and variant share one ident. A
  state-sniffing scorer is unaffected.
- `summarize(run_matrix(counter, execute_mutations=False))` (:455-460): kills a
  structurally *incomplete* run at :337 — my mutations dict is fully populated.

Kill rule (ii) in `plans/round-62.md:96` — "a *label* auditor that returns constants
must fail the controls" — is overclaimed as written: a constant/state-keyed auditor
that preserves the record shape passes the controls (the sniff detects the E2-patch
window during `control-after`), the invariance arm, and both `self_test` floors.
Kill rule (iii)'s "each guard mutation must be shown to change exactly its erratum's
verdicts" is enforced only in the *no-harm* direction (`:364-369`); the *efficacy*
direction — own mutation must flip its own class — is asserted nowhere: FAKE-B's
diagonal is pure assertion, and a run with zero flips anywhere also passes `summarize`.

## Secondary findings (calibration)

1. **`expected_rejected` is dead data on 9 of 10 instances.** Only `check_content_variant`
   reads it (`:418-421`, variant arm only). The ten baseline verdicts are never compared
   to the catalogue's declared predictions — harmless under the E1-corrected "K/N
   computed" predicate, but the frozen predictions are asserted nowhere.
2. **`journal` is plumbed but never used.** `run_matrix(..., journal=)` exists
   (:293,:295,:307,:314-316) yet `self_test`/`main` never pass one, and `summarize`
   never validates journal contents — the one hook that could carry per-arm provenance
   is decorative.
3. **Reason contents are never inspected.** Rejected instances' reason strings are
   never printed; `validate_run` does not check `reasons` element types (only arity 2),
   so `("anything",)` or even a non-string-bearing tuple passes. The plan's "a non-empty
   reason list **naming the arm**" (`plans/round-62.md:45-46`) is unverified —
   `("asserted-rejection",)` sufficed.

## Residual risk and scope bound

- The **committed receipt is genuine**: the shipped `self_test`/`main` always builds
  the run in-process via `run_matrix(counter)` with `real_scorer`, and I reproduced its
  output at HEAD (`exit=0`, identical lines). No CLI or file path admits a foreign
  `MatrixRun`. The hollow class lives in the acceptance boundary the instrument's own
  negative tests define (`summarize(raw_run)`), not in a reachable data path — a
  coverage gap on the gate (Q25/Q47 class), matching how `FalsifyMatrixMutants.md`
  framed m3, not evidence the landed datum is wrong.
- What would kill it: nothing in the file. Shape validation cannot establish
  provenance; at minimum `validate_run` could require reason-tuple element types, and
  `self_test` could plumb `journal` and assert each entry's scorer-returned reasons
  against a re-score — the surviving forgery would then need the counter to lie, not
  the records.

## Lane integrity

No lane product/verifier/corpus/fleet/sibling/`.ufo/state`/MANIFEST/index write; the
only lane write is this report. `/tmp` artifacts: `fake_matrix.py`, `fake_scorer.py`,
`r62assert/` (mutant copy; instrument sha `afb4ff74…` at copy, mutated in place —
lane original untouched). No subagent, background job, model parameter, install, or
network call; ≤4 sequential processes, each <120 s.

## Tooling

No installs or updates were needed or made (python3 3.14 system binary; pacman paused).
