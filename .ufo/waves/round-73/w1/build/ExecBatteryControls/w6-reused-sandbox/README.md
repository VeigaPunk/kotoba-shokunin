# w6-reused-sandbox

**Kind:** plan § C3 shortcut control 6 — a copy of the counter whose "second consecutive
run" is the first sandbox reused (no independence).

**Base:** `072048fa8e8a52c707d25f7079772fa317244eb7`  **World rev (measured):**
`b818a4c40e0b3bc22b9bfdd99833e885cad0e20f`  **Tree:** `40eb2ac3214b56d1c6e5a5faabc884b0005dddc0`

## Move (1)

`measure()` builds **one** sandbox and loops the battery over it twice, printing both run
labels with the same clone path:

```python
            clone = build_sandbox(repo, rev, fleet, parent)
            # Two consecutive runs.  The second run reuses the first run's
            # sandbox: one sandbox is built, so the two readings cannot drift.
            for _run in (1, 2):
                failures, summary, info = run_guards(clone, base, rev)
                gates = run_battery(clone, rev)
                readings.append((failures, summary, info, gates))
            failures, summary, info, gates = readings[-1]
    ...
    for run_no, reading in enumerate(readings, 1):
        print("run %d sandbox %s" % (run_no, clone))
```

A fresh-sandbox counter would print two different `/tmp/k72-tip-*/kotoba-shokunin` paths.

## Frozen counter's reading (absolute `--repo`, fleet-shaped parent)

| gate | exit | wall |
|---|---|---|
| check_gate_registry `--rev <rev>` | 0 | 0.4s |
| check_assertion_floors | 0 | 52.9s |
| verify_skill_checklist | 0 | 1.5s |
| verify_corpus_integrity | **1** | 0.3s |
| verify_corpus_independent | **1** | 0.5s |
| check_correction_sweep `--root .` | 0 | 0.0s |

**`tip battery exit 0: 4 of 6`, counter exit 1** (`counter.out`, run 21:20). Guards:
`instrument-size` FAIL (inherited 76/24) and nothing else — the world's counter is never
looked at.

## The world's own claim (`counter-world-own.out`)

```
run 1 sandbox /tmp/k72-tip-r_df8wbm/kotoba-shokunin
run 2 sandbox /tmp/k72-tip-r_df8wbm/kotoba-shokunin
...
tip battery exit 0: 4 of 6
```

One sandbox, two "consecutive runs", the same frozen line. The only artefact that betrays the
shortcut is the pair of identical paths — and no guard, and no reading rule, compares them.

## Why the frozen counter cannot see it

`BATTERY` enumerates the six *gate* scripts and `INSTRUMENT_PINS` covers exactly those six;
`verifiers/check_tip_battery.py` is neither. Probe D in `../guard-probes.txt` shows the
missing anchor (cap repaired, counter blob added to the pin set):

```
D  w6 live base, self-pin, cap 200 ->
   FAIL instrument-pin: verifiers/check_tip_battery.py blob f5463914f31ee9c1cbefe7db93b5f539d699b552
        at b818a4c40e0b3bc22b9bfdd99833e885cad0e20f is not a pinned blob
D0 base 072048f self-pin, cap 200 -> ALL GUARDS PASS
```

Plan expectation ("a counter run whose second sandbox disagrees with its first must not count
the gate"): the frozen predicate it names requires *two runs on fresh sandboxes*, which the
frozen counter does not implement (it runs once — see F4 in `../README.md`). With the pin the
world fails; without it the world reads 4 of 6 for reasons that have nothing to do with the
attack (the base's two red corpus gates).

## Replay

```sh
sh replay.sh            # frozen counter's reading for this world
KEEP=1 sh replay.sh     # then: python3 -B <sandbox>/verifiers/check_tip_battery.py \
                        #   --rev <rev> --repo <sandbox>/kotoba-shokunin --fleet <sandbox>
```
