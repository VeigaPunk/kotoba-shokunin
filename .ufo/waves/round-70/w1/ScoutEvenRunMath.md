# ScoutEvenRunMath — falsifier of § The one disagreement (round 70, wave 1)

**Verdict: HOLDS within the section's own scope (default threshold 0.5, distinct query strings). Claims (a), (b) and (c) all survive the enumeration over run counts 1–8. Two scope limits are not stated in the section and should be:**

1. **(a) is about the configured run count, not the denominator `run_eval.py` actually divides by.** It divides by `len(triggers)`, collected per *query string* (`query_triggers[query]`, S211 l.213–229). A query string that appears twice in the eval set is scored over 6 runs at the default of 3, so 3/6 = 0.5 can occur. I reproduced this by running the real `run_eval()` with a stubbed query runner. Upstream `run_loop.py` passes `train_set + test_set` straight to `run_eval()` and never deduplicates them (pinned tree, l.87–99).
2. **The Action "keep the run count odd" is enough only at the default threshold of 0.5.** The two rules disagree exactly when *threshold × n* is a whole number. With a non-default `--trigger-threshold` (l.267), odd run counts also hit the gap: 0.2, 0.4, 0.6 and 0.8 at n = 5, and 1/3 and 2/3 at n = 3.

Neither limit contradicts a sentence as written: the section says "with the reference default". The Action sentence, though, gives no condition on the threshold.

Inputs checked: knowledge file `corpus/knowledge/skill-eval-artefacts-round70.md` (last changed in `ac3c0f14`), lane tip `16b212a390c7ce68b6bce49b2c3766b154fbcbae`, and snapshots `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt` and `S210-optimizing-descriptions.md`.

## Rules compared

- Spec (S210 snapshot l.92): "A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default). A should-not-trigger query passes if its trigger rate is below that threshold." I read "above" as `>` and "below" as `<`.
- `run_eval.py` (S211 snapshot l.229–234): `trigger_rate = sum(triggers) / len(triggers)`, then `did_pass = trigger_rate >= trigger_threshold` for should-trigger queries and `trigger_rate < trigger_threshold` otherwise.
- Defaults: CLI `--runs-per-query` 3 (l.266) and `--trigger-threshold` 0.5 (l.267). The *function* default is `runs_per_query: int = 1` (l.191); n = 1 has no gap, so this changes nothing. Upstream `run_loop.py` at the pinned tree also defaults to 3 and 0.5 (l.252–253).

Snapshot integrity: `sha256sum .ufo/waves/round-70/snapshots/S211-run_eval.py.txt` printed `43e3b8f80dbf69c343967ba77e268fae991d9fa3ed68b32a0ff02532cd48657f`, 11 464 B, 310 lines. A live fetch of `raw.githubusercontent.com/anthropics/skills/dbd4588f…/skills/skill-creator/scripts/run_eval.py` printed the same sha256.

## Table — threshold 0.5, run counts 1–8

Command: `cd /tmp/k70w1-ScoutEvenRunMath.0le6 && python3 -B gapcount.py "$PWD"` (script in the appendix). Rates are computed as `run_eval` computes them, as a float `k/n`. The last column is the probability that a query whose true firing chance is 0.5 lands exactly on the gap: C(n, n/2) / 2ⁿ.

| n | attainable rates | should-trigger: spec and `run_eval` disagree at | should-not-trigger disagree at | P(gap \| p = 0.5) |
|---|---|---|---|---|
| 1 | 0, 1 | — | — | 0.0000 |
| 2 | 0, 1/2, 1 | 1/2 | — | 0.5000 |
| 3 | 0, 1/3, 2/3, 1 | — | — | 0.0000 |
| 4 | 0, 1/4, 1/2, 3/4, 1 | 2/4 | — | 0.3750 |
| 5 | 0, 1/5 … 4/5, 1 | — | — | 0.0000 |
| 6 | 0, 1/6, 1/3, 1/2, 2/3, 5/6, 1 | 3/6 | — | 0.3125 |
| 7 | 0, 1/7 … 6/7, 1 | — | — | 0.0000 |
| 8 | 0, 1/8 … 7/8, 1 | 4/8 | — | 0.2734 |

In every gap case `run_eval` says PASS and the spec says FAIL. The disagreement never goes the other way, because `>=` accepts everything `>` accepts.

- **(a) HOLDS.** At n = 3 the attainable rates are 0, 1/3, 2/3 and 1, and there is no disagreement. The same is true of every odd n from 1 to 7.
- **(b) HOLDS, and more broadly.** At n = 2 and n = 4, the rate 1/2 passes under `run_eval` and fails under the spec. This happens at **every** even n (6 and 8 too). A coin-flip query hits it 50 %, 37.5 %, 31.25 % and 27.3 % of the time at n = 2, 4, 6 and 8.
- **(c) HOLDS.** There are zero should-not-trigger disagreements at any n, because both rules use strict `<`. It also holds at every non-default threshold tested (the "should-not gaps 0" lines below).

## Non-default thresholds (CLI `--trigger-threshold`, l.267)

Same run. Each line lists the run counts with a should-trigger gap:

```
t=0.2: gap at {5: ['1/5']}; odd n with gap [5]; should-not gaps 0
t=0.25: gap at {4: ['1/4'], 8: ['2/8']}; odd n with gap -; should-not gaps 0
t=0.3333333333333333: gap at {3: ['1/3'], 6: ['2/6']}; odd n with gap [3]; should-not gaps 0
t=0.4: gap at {5: ['2/5']}; odd n with gap [5]; should-not gaps 0
t=0.6: gap at {5: ['3/5']}; odd n with gap [5]; should-not gaps 0
t=0.6666666666666666: gap at {3: ['2/3'], 6: ['4/6']}; odd n with gap [3]; should-not gaps 0
t=0.75: gap at {4: ['3/4'], 8: ['6/8']}; odd n with gap -; should-not gaps 0
t=0.8: gap at {5: ['4/5']}; odd n with gap [5]; should-not gaps 0
```

So "keep the run count odd" only fixes the 0.5 case. A rule that works at any threshold: choose n so that *threshold × n* is not a whole number, or state which rule the report applies.

Float check: across thresholds 0.01–0.99 (step 0.01) and n = 1–8, Python's float `k/n >= float(t)` agreed with the exact comparison against the decimal the user typed in all 891 combinations. Three combinations differed from a comparison against the binary double's exact value: 0.20 at 1/5, 0.40 at 2/5 and 0.80 at 4/5. That is because the nearest double to 0.2 lies slightly above 1/5, so it is a quirk of my reference value, not of `run_eval`. The float division in `run_eval` matches the decimal intent, so the table above has no rounding artefacts. (Command: the inline `python3 -B -c` loop comparing `k/n>=t`, `F(k,n)>=F(t)` and `F(k,n)>=F(ts)`, which printed exactly those three lines.)

## Real `run_eval()` aggregation (stubbed runner, same run)

I loaded the snapshot as `run_eval.py` in scratch with a stub `scripts/utils.py`. `ProcessPoolExecutor` was swapped for `ThreadPoolExecutor`, which leaves the aggregation logic unchanged. `run_single_query` was stubbed to alternate True, False, True, … per query string, and to raise for queries starting with `boom`.

```
default runs=3, distinct queries: triggers=2/3 rate=0.6666666666666666 run_eval pass=True spec pass=True disagree=False
runs=2 (even): triggers=1/2 rate=0.5 run_eval pass=True spec pass=False disagree=True
runs=4 (even): triggers=2/4 rate=0.5 run_eval pass=True spec pass=False disagree=True
runs=3, query string duplicated: triggers=3/6 rate=0.5 run_eval pass=True spec pass=False disagree=True
Warning: query failed: timeout   (x3)
runs=3, failing runner: triggers=0/3 rate=0.0 run_eval pass=False spec pass=False disagree=False
runs=2, should-not: triggers=1/2 rate=0.5 run_eval pass=False spec pass=False disagree=False
```

- A failed or timed-out run cannot shrink the denominator. The `except` branch appends `False` (l.223–225), so with distinct queries `len(triggers) == runs_per_query`. The "failing runner" line confirms 0/3.
- Duplicating a query string at the default of 3 runs gives 3/6 = 0.5, a pass under `run_eval` and a fail under the spec. This is scope limit 1 above. Side observation: `query_items[query] = item` (l.218) is overwritten in `as_completed` order. If the duplicates carry *different* `should_trigger` labels, which label scores the merged rate depends on completion order. I read this in the code but did not run that case.

## Remaining unknowns

- I did not check whether any real eval set the lane cites (S124, or skill-creator examples) contains a duplicated query string. Only the mechanism is shown.
- I did not test the label race between conflicting duplicate labels.

## Tooling

No installs or upgrades. I used the system `python3` (3.14.8), `curl`, `rg` and `awk`. Scratch directory `/tmp/k70w1-ScoutEvenRunMath.0le6` (snapshot copy, stub, script and upstream fetches) is deleted before return. I changed no committed lane file.

## Appendix — `gapcount.py` (core enumeration)

```python
from fractions import Fraction
from math import comb
def spec(rate, t, st):   return rate > t if st else rate < t
def reval(rate, t, st):  return rate >= t if st else rate < t
def gaps(n, t, st):
    return [k for k in range(n + 1) if spec(k / n, t, st) != reval(k / n, t, st)]
for n in range(1, 9):
    g_st, g_sn = gaps(n, 0.5, True), gaps(n, 0.5, False)
    p = sum(comb(n, k) for k in g_st) / 2 ** n
    print(n, [str(Fraction(k, n)) for k in range(n + 1)], g_st, g_sn, f"{p:.4f}")
for ts in ["0.2", "0.25", "0.3333333333333333", "0.4", "0.6", "0.6666666666666666", "0.75", "0.8"]:
    t = float(ts)
    print(ts, {n: gaps(n, t, True) for n in range(1, 9) if gaps(n, t, True)},
          sum(len(gaps(n, t, False)) for n in range(1, 9)))
```
