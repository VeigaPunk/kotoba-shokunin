# M01MutDescCounter — C1 frozen-counter mutation probe

## Result

- Frozen target: `verifiers/check_desc_craft.py`; its lane SHA-256 before and after the probe was `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`, matching the round-77 plan pin.
- Pristine scratch copy had the same SHA-256 and ran `python3 -B pristine/check_desc_craft.py --self-test`: `self-test: 0 failure(s) over 53 assertions`, exit 0.
- Generated **34 single-point behavioral mutants**, re-pinning each mutant's blanked `SELF_SHA` so the guard could not trivially kill it. Results: **26 survived**, **8 were killed by behavioral self-test assertions**; all ran 53 assertions. The 26 survivor rows, exact changed lines, rationale, outputs and mutant after-hashes are in [the survivor table](../build/M01MutDescCounter.survivors.md).
- Additional drift-guard control: M12 without re-pinning was killed, but this is **not** a behavioral kill. Each fixture's in-process `main()` returned exit 2 with `environment error: counter drifted`; self-test reported 18 failures / 53 assertions, exit 1.
- No tool was installed.

## Exact commands and outputs

Pristine baseline command (from scratch root):

```sh
python3 -B pristine/check_desc_craft.py --self-test > out/pristine-selftest.txt 2>&1; echo "exit=$?" >> out/pristine-selftest.txt
```

Recorded output tail:

```text
self-test: 0 failure(s) over 53 assertions
exit=0
```

Re-pin sanity command:

```sh
python3 -B mutants/M01.py --print-self-sha
```

Output matched the mutant file's `SELF_SHA` exactly: `be34597ef3f138551e771e5d91904ddcdc4ceb6f85b7069980d6c0a098104b29`.

The complete batch command (2 concurrent slots, each child limited to 120 seconds) was:

```sh
ls mutants/*.py | xargs -P2 -I{} sh -c 'n=$(basename "$1" .py); timeout 120 python3 -B "$1" --self-test > "out/$n.txt" 2>&1; echo "exit=$?" >> "out/$n.txt"' _ {}
```

It ran 35 files (34 re-pinned behavioral mutants plus the stale-pin control) in 8.65 seconds. Each re-pinned mutant produced its own captured self-test output and explicit exit line. Killed mutant outputs:

| ID | Mutant SHA-256 (after) | Actual detector output | Kill evidence |
|---|---|---|---|
| M01 | `83623315e1e1e5be1549d9f32e4cc0b54d88e588d07db448798fba43ff537abd` | 18 failures / 53 assertions; exit 1 | Honest world expected `6 of 6`, mutant printed `6 of 7`. |
| M02 | `8405fcded0b930fc123d6955fb2ce878993a2e50d4e4cc4c181e7ab384b9f4b0` | 18 failures / 53 assertions; exit 1 | Honest world expected `6 of 6`, mutant printed `6 of 5`. |
| M03 | `6368842c0a220ce19c26b34417d2c8f9f3f8655d5eba745a47953f146ed303b3` | 17 failures / 53 assertions; exit 1 | Honest world expected six conjuncts; removing (d) printed `5 of 6`. |
| M06 | `28623226985526ac7b28dfa4746a7f92f1b55144f289b0a1990fb8ce1aaddb91` | 4 failures / 53 assertions; exit 1 | Broken quote worlds emitted `required 3`, violating their asserted `required 4` finding. |
| M12 | `23ac617f2eedff1118e832c35dc56ccb6fc59c296dfc81d4ff1d64962441a8b5` | 1 failure / 53 assertions; exit 1 | The HTTP-404 world passed (a) and printed `6 of 6`, but expected failure / `5 of 6`. |
| M19 | `f01d98c27e8b395ed04b6a4c5bfab0208a71ed3a93d99197216a0938e8ab625a` | 1 failure / 53 assertions; exit 1 | The wrong-digest Gate world passed (a) after any hex token was accepted. |
| M20 | `2144db223ee0a3a570d95836c51113ffed6a9187462c7bfe8557bb60560f337a` | 13 failures / 53 assertions; exit 1 | Honest world failed because snapshot digest equality was inverted. |
| M29 | `81205ad79aa7fd46f44ab4ec556ec202b76d91f93f2590528c1b360e195905c3` | 1 failure / 53 assertions; exit 1 | Uncited-quote world passed (b), printing `6 of 6`, rather than expected `5 of 6`. |

The stale-pin control hash was `4d7d708f67f516082d9b4709efe24bfcd15f9da7fc21b3a0c0fc95832ffd5808`; it produced `self-test: 18 failure(s) over 53 assertions`, exit 1, with each fixture's `main()` reporting `environment error: counter drifted` (exit 2). This establishes why re-pinning was required to distinguish behavioral mutants from integrity-guard kills.

## Restoration evidence

Only scratch copies were mutated. The frozen lane file SHA-256 was independently checked again after the batch and remained exactly the plan pin; the pristine scratch copy also remained that hash. No lane counter bytes were changed. Scratch cleanup is performed before hand-off; only the two named lane deliverables remain.

VERDICT: 26 of 34 behavior mutants survived the frozen self-test; substantial fixture coverage gaps disclosed, no counter edits made.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/M01MutDescCounter.survivors.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/M01MutDescCounter.md
