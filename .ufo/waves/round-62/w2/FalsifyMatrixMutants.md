# FalsifyMatrixMutants — C1 absorption instrument: four-mutant probe

Date: 2026-10-23 (UTC). Seat: `L1kotoba62.FalsifyMatrixMutants`. Axis: **depth**.
Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at tip
`e6da78bbe420722dd18a13182a7c4b64ce02f005`, read-only except this report.

## Target bytes

| file | sha256 observed |
|---|---|
| `verifiers/check_erratum_absorption.py` | `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b` |
| `verifiers/check_scoped_rules.py` (pinned by `COUNTER_SHA256`) | `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91` |

```
$ sha256sum verifiers/check_erratum_absorption.py verifiers/check_scoped_rules.py
afb4ff74…  verifiers/check_erratum_absorption.py
5a5adc94…  verifiers/check_scoped_rules.py
```

**Method.** Five isolated directories `/tmp/r62c1mut-L1kotoba62/{pristine,m1,m2,m3,m4}`,
each containing a byte-identical copy of the instrument *and* of the frozen counter, so
`COUNTER_PATH = Path(__file__).with_name("check_scoped_rules.py")` resolves to the pinned
counter. All five copies hashed to the two tip values above before mutation
(`sha256sum /tmp/r62c1mut-L1kotoba62/*/check_*`). Each mutant run:

```
cd /tmp/r62c1mut-L1kotoba62/<mutant>
python3 -B check_erratum_absorption.py --self-test
```

## Baseline — pristine copy, exit 0

```
$ cd /tmp/r62c1mut-L1kotoba62/pristine && python3 -B check_erratum_absorption.py --self-test
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

The ten stdout lines are byte-identical to the `--self-test` block of
`.ufo/waves/round-62/C1-absorb-measure.txt` (slice between the command line and `exit=0`;
`diff` printed nothing, `diff_exit=0`, 10 lines each). The committed receipt is therefore
re-derived from committed bytes in an isolated copy — the sandbox is faithful and the
baseline is green, so mutant kills below are meaningful.

## Results

| # | mutation (one per copy) | site | expected detector | observed | exit | verdict |
|---|---|---|---|---|---|---|
| m1 | primary matrix run is reject-only: `run_matrix(counter, execute_mutations=False)` | instrument `:432` | `validate_run` missing-mutations require | `absorption self-test failed: guard-mutation direction is missing for one or more errata` | 1 | **killed** |
| m2 | real scorer replaced by the fixture-label scorer: `run_matrix(counter, scorer=label_scorer)` | instrument `:432` | seeded-controls require (`:435`) | `absorption self-test failed: seeded controls did not classify in both directions` | 1 | **killed** |
| m3 | summary headline hard-coded: literal `"errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2"` | instrument `:489-490` | none exists | full green output, wrong headline, `exit=0` | 0 | **SURVIVED** |
| m4 | one erratum removed from `ERRATA`: the `E2f` `Erratum(...)` block deleted | instrument `:212-229` | `require(summary.measured == 5)` (`:434`) | `absorption self-test failed: not all five erratum classes were measured` | 1 | **killed** |

Each diff touched only the named bytes (`diff -u pristine <mutant>`); no shared guard,
catalogue row, or counter byte was altered.

### m1 — reject-only matrix (killed)

```diff
 def self_test(counter: ModuleType) -> Summary:
-    run = run_matrix(counter)
+    run = run_matrix(counter, execute_mutations=False)
```

```
$ python3 -B check_erratum_absorption.py --self-test
absorption self-test failed: guard-mutation direction is missing for one or more errata
exit=1
```

The diagnostic is the message at `:337`, raised from `validate_run` because
`set(run.mutations) == names` is empty. It reproduces, on the real self-test path, the
exact diagnostic that the committed control `controls/absorption-hollow.txt` records for
variant H ("hollow: never runs the guard-mutation direction"), so that control receipt is
consistent with the landed bytes.

### m2 — fixture-label scorer (killed)

```diff
 def self_test(counter: ModuleType) -> Summary:
-    run = run_matrix(counter)
+    run = run_matrix(counter, scorer=label_scorer)
```

```
$ python3 -B check_erratum_absorption.py --self-test
absorption self-test failed: seeded controls did not classify in both directions
exit=1
```

`label_scorer` (`:260-262`) returns `["label-only rejection"]` for every id starting `e2`
and `[]` otherwise; the control idents start `control-`, so `absorbed-control.before` is
empty and the `:435` require fails. This matches the variant-L diagnostic in
`absorption-hollow.txt`. (Had a label table been keyed to satisfy the controls too,
`check_content_variant(counter, label_scorer)` would still fail on the same-ID content
variant — the structural defence the critics demanded is present for this class.)

### m3 — hard-coded headline (SURVIVED)

```diff
-    print("errata measured %d of 5; absorbed %d of 5; surviving %d; controls %d of 2" %
-          (summary.measured, summary.absorbed, len(summary.survivors), summary.controls))
+    print("errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2")
```

The literal chosen is the plan's pre-data expectation (`plans/round-62.md` §C1 / E1), i.e.
the plausible defect of pasting the expected line into the printer. The computed run
underneath is unchanged and still genuine; only the report sentence is substituted.

```
$ python3 -B check_erratum_absorption.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
exit=0
```

The mutant prints `absorbed 4 of 5; surviving 2` and then six survivor rows computed by
the same run: a self-contradictory receipt, accepted by the gate.

### m4 — E2f removed from `ERRATA` (killed)

```diff
-    Erratum(
-        "E2f",
-        ( … two action_attack instances … ),
-        (("action_conjunct", lambda *args, **kwargs: []),),
-    ),
```

```
$ python3 -B check_erratum_absorption.py --self-test
absorption self-test failed: not all five erratum classes were measured
exit=1
```

`measured` is `len(run.baseline)` (`:397`), computed from the four remaining catalogue
entries, so the literal `== 5` require at `:434` fires.

## The named bound

**m3 is not killed.** Mechanism, from the landed bytes:

- `self_test()` (`:431-461`) computes a `Summary` and returns it. It asserts
  `summary.measured == 5` (`:434`) and `summary.controls == 2` (`:435`), runs the
  content-variant arm, and exercises three negative auditor arms. None of these reads
  program output.
- `main()` (`:464-496`) prints *after* every assertion, at `:489-492`, then guards
  `if summary.measured != 5 or summary.controls != 2: return 1` (`:494-495`) on the
  computed fields.
- The instrument contains no output-capture or parsing primitive:
  `grep -n "capsys\|redirect_stdout\|StringIO\|sys.stdout\|subprocess\|stdout"` over
  `verifiers/check_erratum_absorption.py` returns **none**; the only prints are stderr
  diagnostics (`:474,:477`) and the four report lines (`:482-492`).

So the gate binds the *classification* (measured/controls) and the *survivor rows*, but
not the headline sentence. A substituted headline that contradicts the computed summary
and the rows printed directly below it exits 0. Hard-coding the true line is a strictly
weaker form of the same unconditioned print and would also pass.

**No other committed check catches it.** The no-harm battery's arm for this instrument is
`tip_self_test_optional absorption check_erratum_absorption.py --self-test`
(`.ufo/waves/round-62/noharm-battery.sh:377`), and that helper (`:214-226`) passes on
`RC -eq 0` only — it never inspects stdout. The C1 receipt `C1-absorb-measure.txt` is
captured text, not a re-derived comparison. Only a human/diff review stands between a
fabricated headline and a green gate.

**Gap against the wave-1 specification.** `ExecGateArms.md:20` (item C) required capturing
"the actual survivor records and computed summary" and asserting
`(records, count, summary_line) == (…)`, with `:25` adding "do not print a fabricated
green predicate to hide it". The landed self-test has no such equality assertion; this
probe shows the described hole survives in the landed bytes. The wave-1 critic
(`CriticC1Hollow.md` §2.6) also required deriving the survivor count and summary "from the
same matrix" and exercising public-main arms; the landed gate derives the rows but never
compares the printed sentence.

**What the mutant does and does not show.** It does **not** show the landed C1 datum is
wrong: the pristine run recomputes `absorbed 2 of 5; surviving 6` and the six named
survivors, byte-identical to the receipt. It shows that the committed detector cannot
distinguish that report from a hard-coded one — a coverage finding on the gate (Q25/Q47
class), not evidence against the contract's semantics. This seat does not change the
predicate; the bound is reported, not repaired.

## Restoration evidence

Post-edit mutant hashes:

```
64caea57a367cd34c721b2375b8319eb00f62f7fa61fff09d17734039bc2df23  m1
e6bdef7f7b29abaa2ce283b299ea74707a6b498a13001ef930098bcd144e139d  m2
b70a187854f6c3736415cbde525f611eb4feabb044e1bc43f271b1560e241d80  m3
b217bdbba86f0b1632af06f193e4fdd74923efa1b582b5f05383a1ad8c4cac4e  m4
```

Every mutant copy was overwritten from `pristine/`; restored hashes are all
`afb4ff74c266…` (`sha256sum /tmp/r62c1mut-L1kotoba62/m*/check_erratum_absorption.py`).
Restored m3 re-run prints the computed true line and exits 0:

```
$ cd /tmp/r62c1mut-L1kotoba62/m3 && python3 -B check_erratum_absorption.py --self-test
…
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
… six survivor rows …
exit=0
```

Lane bytes after the probe are unchanged (`sha256sum` of both files equals the tip values
above). No lane product, verifier, corpus, fleet, sibling, `.ufo/state`, MANIFEST or
jj/git-index file was written; the only lane write is this report. No subagent, background
job, model parameter, install, or network call; all lane access was read-only
`sha256sum`/`grep`/`sed -n`/`ls`; commands ran sequentially (≤4 processes, ≤120 s each).

## Tooling

No installs or updates were needed or made.
