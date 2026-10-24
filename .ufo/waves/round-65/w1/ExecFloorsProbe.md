# ExecFloorsProbe — round 65, wave 1: floors registration probes (C1 / F17 close)

Seat: `ExecFloorsProbe` (leaf executor). Scope: the three probes in the ticket — (1) delete one
round-65 arm and show the floors guard names `scoped_rules_v32 observed<N floor`, (2) registry-row
deletion fails the anchor drift check with the class named, (3) the live walk at the tip is all-PASS
and the guard self-test prints 165. Read-only outside this report; all mutation in `/tmp` trees.

Measured 2026-10-24. Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, git HEAD
`2a8eba56b3f9321b70c569fa2816d42237ca49a2` (round-66 spot-check), jj `@`
`2d2a13cdcd65f80fb1ee93e028d8d152ced6232f`. The lane has moved past the round-65 tip the ticket
names (`0e104f49`): round 66 landed six additional v32 assertions, so the live floor is **240**, not
the ticket's 234. Both revisions are probed below; hashes pin every measurement.

## Axes (godspeed)

- **Operability of the C1 floors registration**: can a single deleted arm be made to read green, and
  does the guard stop it? Measured, per arm, at both floors.
- **Anchor directionality**: whose deletion is caught — the registry's row or the guard's tables?
  Both directions measured.
- **Live green**: the tip walk and the guard self-test, unmodified.

## Trees and identity

| tree | bytes | sha256 | self-test |
|---|---|---|---|
| live `verifiers/check_scoped_rules_v32.py` | 154,495 B | `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` | 240 assertions |
| landing `80bb8921:verifiers/check_scoped_rules_v32.py` | 152,760 B | `b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d` | 234 assertions |
| live `verifiers/floors-registry.json` | 3,370 B | `910bb193be4968d552a531f5dfad2c4000665d44617fa36f435bc7a1d2572c91` | floors: `scoped_rules_v32 240`, `checklist 1862` |
| live `verifiers/check_assertion_floors.py` | 83,926 B | `fb5d31ad44809eecd9e1996d54fb97706c38500fe27aa01b87fde7cacae0c094` | 165 assertions |

The landing hash equals the `counter sha256` in `.ufo/waves/round-65/receipts/C1-close-measure.txt`
(`b6cfc764…`), so the receipt's 234-assertion pin reproduces byte-for-byte. The live hash differs
because round 66 landed the six G9 coupling assertions (guard docstring lines 17-20: "round 66 …
raises scoped_rules_v32 234 -> 240").

Every probe tree is `/tmp/floorprobe/<name>`: `verifiers/` copied (`cp -a` for live,
`git archive 80bb8921 verifiers` for the landing rev), with the 13 non-probed instrument paths
replaced by hermetic stubs that print each instrument's summary shape at that tree's own registry
floor. Only `scoped_rules_v32` (and `floors_guard`, which is the running guard itself) is real, so a
FAIL line is attributable to the row under probe and nothing else.

## Probe 1 — one deleted arm, guard red at both floors

Arm block counted programmatically in the landed source: **11 `check()` calls** between
`# Round-65 closing package` and the next `A2 G9` block (labels 1-11: fabricated four-char span;
three-char; cited-line-only backtick; four-char prefix; capitalised stopword-only; capitalised
cited-line; wrapper; SPAN_FIRST; SPAN_LAST-descriptor; M20; M11-exact-case). Deletion was by exact
line-range removal of one whole `check(...)` call; nothing else changed.

### 1a. Live tree, floor 240 — delete arm 9 (`a fabricated second backticked span is rejected when an honest first span precedes it`)

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test
self-test: 0 failure(s) over 239 assertions
exit=0                      ← the self-test stays GREEN; the arm is gone

$ python3 -B verifiers/check_assertion_floors.py --repo /tmp/floorprobe/live --load 1
PASS harness observed=10 floor=10
PASS corpus_integrity observed=161 floor=161
PASS corpus_independent observed=103 floor=103
PASS surfaces observed=175 floor=175
PASS checklist observed=1862 floor=1862
PASS pins observed=62 floor=62
PASS harness_independent observed=123 floor=123
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=165 floor=150
PASS dispatch_prompts observed=56 floor=56
PASS sibling_census observed=68 floor=68
PASS overlap_levers observed=51 floor=51
PASS alwayson observed=89 floor=89
PASS correction_sweep observed=25 floor=25
FAIL scoped_rules_v32 observed=239 floor=240
exit=1
```

### 1b. Landing rev 80bb8921, floor 234 — same arm deleted

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test
self-test: 0 failure(s) over 233 assertions
exit=0

$ python3 -B verifiers/check_assertion_floors.py --repo /tmp/floorprobe/r65 --load 1
… (14 PASS lines identical in shape)
FAIL scoped_rules_v32 observed=233 floor=234
exit=1
```

This is the exact shape the ticket asks for: `observed=233 floor=234`, class `FAIL`, exit 1.

### 1c. All 11 arms, individually, both floors

Sequential sweep, one deletion per run, 11 runs per rev (63.9 s per rev; at most two processes alive:
the guard plus one child):

- live (floor 240): every arm → self-test `0 failure(s) over 239 assertions`, exit 0; guard
  `FAIL scoped_rules_v32 observed=239 floor=240`, 14 PASS, exit 1 — 11/11.
- landing (floor 234): every arm → self-test `0 failure(s) over 233 assertions`, exit 0; guard
  `FAIL scoped_rules_v32 observed=233 floor=234`, 14 PASS, exit 1 — 11/11.

### 1d. Controls (same trees, pristine bytes)

```
$ … --repo /tmp/floorprobe/live --load 1
PASS scoped_rules_v32 observed=240 floor=240
exit=0
$ … --repo /tmp/floorprobe/r65 --load 1
PASS scoped_rules_v32 observed=234 floor=234
exit=0
```

So the red in 1a/1b is caused by the deletion, not by the /tmp tree, the stubs, or the run order.

## Probe 2 — registry-row deletion: anchor drift, class named

### 2a. `scoped_rules_v32` row deleted from `verifiers/floors-registry.json`, `instrument_total` left at 15

```
FAIL registry size drift: instrument_total=15 but 14 entries in verifiers/floors-registry.json
FAIL registry extra row: scoped_rules_v32 (carried by the guard tables, absent from verifiers/floors-registry.json)
exit=2
```
`PASS` lines in the output: 0 — the anchor refuses before any instrument reruns.

### 2b. Same deletion with `instrument_total` edited to 14 (the deliberate coordinated half-bump)

```
FAIL registry extra row: scoped_rules_v32 (carried by the guard tables, absent from verifiers/floors-registry.json)
exit=2
```

**Class named: `extra row`** (`registry_anchor_drift`, `set(INSTRUMENTS) - set(entries)`), preceded by
`size drift` whenever the registry's declared inventory is not adjusted. Exit 2 in both shapes.

### 2c. Opposite direction — row deleted from BOTH in-file tables, registry intact

```
FAIL registry row vanish: scoped_rules_v32 (listed in verifiers/floors-registry.json, absent from both guard tables)
exit=2
```
**Class named: `row vanish`.** 0 PASS lines. The two directions are distinct classes and neither is
silent; `size drift` is the third (registry inventory vs entry count).

## Probe 3 — live tip: walk all-PASS, guard self-test 165

```
$ python3 -B verifiers/check_assertion_floors.py          # live tree, 92.47 s
PASS harness observed=10 floor=10
PASS corpus_integrity observed=161 floor=161
PASS corpus_independent observed=103 floor=103
PASS surfaces observed=175 floor=175
PASS checklist observed=1862 floor=1862
PASS pins observed=62 floor=62
PASS harness_independent observed=123 floor=123
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=165 floor=150
PASS dispatch_prompts observed=56 floor=56
PASS sibling_census observed=68 floor=68
PASS overlap_levers observed=55 floor=51
PASS alwayson observed=89 floor=89
PASS correction_sweep observed=25 floor=25
PASS scoped_rules_v32 observed=240 floor=240
exit=0

$ python3 -B verifiers/check_assertion_floors.py --self-test     # 4.97 s
0 failure(s) over 165 assertions
exit=0

$ python3 -B verifiers/check_scoped_rules_v32.py --self-test
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
self-test: 0 failure(s) over 240 assertions
exit=0
```

Bump-in-step holds at the measured bytes: registry `scoped_rules_v32 240` (line 61-63) /
`checklist 1862` (line 5-7), guard `EXPECTED_INSTRUMENTS` 240 & 1862 (lines 176, 166), guard
`INSTRUMENTS` 240 & 1862 (lines 235, 211), docstring enumeration `scoped_rules_v32 240` (line 11)
and `checklist 1862` (line 8). Eight occurrences across the three files, one value per instrument.

## Measured residual — compensated deletion passes the floor

Delete arm 9 **and** add one trivial `check("A2 G7: padding marker (compensating count)", True, True)`:

```
self-test: 0 failure(s) over 240 assertions      exit=0
PASS scoped_rules_v32 observed=240 floor=240     exit=0
```

The floor is a count guard: it raises silent arm deletion to "delete one, add filler". The plan's §9
argument — a padding-only patch is falsified by the kill battery, not by the count — is confirmed as
the load-bearing mechanism here. The row is necessary but not sufficient for arm semantics.

## Claims supported / falsified

- **SUPPORTED — C1's F17 close is operative.** The `scoped_rules_v32` row is registered and every
  one of the 11 round-65 arms is individually load-bearing: bare deletion of any one exits 1 with
  `FAIL scoped_rules_v32 observed=239 floor=240` (landing: `observed=233 floor=234`).
- **SUPPORTED — bump-in-step at the measured tip** (registry, both guard tables, docstring, observed
  counts) for `scoped_rules_v32 240` and `checklist 1862`, and the live walk is 15/15 PASS, exit 0.
- **SUPPORTED — anchor drift is bidirectional and class-named** (`extra row`, `row vanish`, plus
  `size drift`), exit 2, zero instruments rerun.
- **FALSIFIED as a statement about the current tip — "floor 234".** Live floor is 240; 234 is the
  round-65 landing floor only (reproduced exactly at `80bb8921`, sha `b6cfc764…` = receipt pin).
  Not a defect: round 66's documented bump. The ticket's number is stale by one revision.
- **PARTIALLY FALSIFIED — "the floor prevents arm deletion".** True for a bare deletion; false for a
  compensated one (measured above). [INFERENCE] the same holds for 2-for-1 swaps anywhere in the
  suite, since the guard reads only `(failures, assertions)`.

## Risks

- **Trust boundary (guard docstring, scout T4):** a coordinated edit of both in-file tables + the
  registry (including `instrument_total`) + this docstring is out of scope and was not tested. The
  anchor catches every *half* of that edit; the whole of it is the documented ceiling.
- **Count-only floor** — compensated deletion silent (measured). Semantic coverage rests on the kill
  battery (`.ufo/waves/round-65/receipts/C1-close-kill.txt`), which this seat did not re-run (out of
  the assigned scope; sibling lanes own the kill battery).
- **Moving surface:** this report probes a tree six assertions past the round-65 tip; hashes above
  pin exactly what was measured, and the landing-rev probes use the committed `80bb8921` bytes.

## Blocker

None.

## Tooling / process

No tool installed or upgraded. All probes were `python3 -B` against `/tmp/floorprobe/*`; the lane
tree was read-only (`jj diff --stat verifiers` → `0 files changed, 0 insertions(+)`). Longest holds:
the live walk 92.47 s, two 11-arm sweeps 63.9 s each — sequential, never more than two processes
(the guard plus one child), under the 120 s per-probe cap. Scratch: `/tmp/floorprobe/{live,r65,
pristine,regdel,regdel-total14,regvanish}` plus `*.out`.
