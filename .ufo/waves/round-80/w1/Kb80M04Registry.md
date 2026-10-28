# Kb80M04Registry — mutation test of the SKILL.md/registry layer (round 80 w1)

Seat: Kb80M04Registry (mutation-tester, leaf — no subagents, no background jobs beyond
own tool calls). Date: 2026-10-27. Lane base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Tool installs: none (pacman never invoked; no host service touched).

## What was probed

The C1 repair-stack piece 1 (registry rows in `SKILL.md`) is load-bearing for the tip
battery only if the frozen counter `check_gate_registry.py` reds on each plausible defect
of the delta. Five mutants of the registry delta, one defect each:

| id | mutant | defect injected |
|---|---|---|
| M1 | `mut1-verdict-map-swap` | third row's verdict map swapped: `0=failed, 1=clean, 2=could-not-evaluate` |
| M2 | `mut2-selftest-flag-missing` | `check_desc_craft.py` row's self-test cell emptied (flag removed) |
| M3 | `mut3-probe-kind` | `check_r75_routed_repairs.py` row kind `gate` → `probe` |
| M4 | `mut4-withdrawal-annotation-dropped` | " — claim withdrawn r79 before data (declared r76, never landed); not a claim gate until redesigned and re-controlled" deleted from the `check_desc_craft.py` row |
| M5 | `mut5-nonexistent-script` | third row name+entry cells → `verifiers/check_allowed_tools_probe.py` (script absent) |

## Worlds (all built in the scratch clone only; lane untouched)

- Control `28a9dcb87905e4b0db2dd2887110ff16de85203f`: r79 `Kb79E01Registry.patch` applied
  with `git apply --index` (clean at base; sha256 of the patch source is the fleet's
  reviewed c411106e…), then my authored third row for `check_allowed_tools.py` (kind gate,
  `--self-test`, pinned values `in-file`, owner kotoba), then
  `verifiers/check_allowed_tools.py` copied byte-for-byte from the r79 draft
  `.ufo/waves/round-79/build/check_allowed_tools.py` (2288 lines, has the exact
  `add_argument("--self-test")` handler the row names). Universe becomes 63 scripts.
  Patch published: `Kb80M04Registry-control.patch` (applies at base).
- Mutants `e320359…`, `8a19a6a…`, `50ccb9c…`, `ee9d17e…`, `e5e1f96…`: control bytes with
  exactly the one row defect above (each replacement asserted to hit exactly one line).

Counter bytes used: registry checks ran the base bytes of
`verifiers/check_gate_registry.py` from the scratch clone (its `LANE` resolves to the
clone; it reads committed bytes at `--rev`). Battery runs used the round-72 frozen
`check_tip_battery.py` bytes at the measured world. I did NOT amend the battery by
erratum E5: no world modifies any of the six pinned instrument scripts, so
`instrument-size`/`instrument-pin` are measured against the base blobs and read PASS in
all six battery receipts (E5's `LINE_CAP` 40→60 and the two new pins are orthogonal to
the registry gate's battery slot — they exist for repairs 4+5, which my worlds do not
carry). The third row's wording describes the round-80 amended C2 counter per the plan
("documented N of 6"); my scratch world executes the r79 draft bytes (which print
"backed N of 6"). No gate reads that wording: the registry counter never executes the
script and the battery's six frozen gates do not include it.

## Gate level — check_gate_registry.py (baseline first)

Command (cwd = scratch clone), receipt = body + own exit status, never a pipeline:

```
python3 -B verifiers/check_gate_registry.py --rev <rev> > receipt 2>&1; rc=$?; echo "exit=$rc" >> receipt
```

- Control `28a9dcb`: `gate registry rows conformant 63 of 63 lane verifiers; phantom 0`,
  **exit 0** — green baseline, so every mutant verdict below is a reading, not an
  environment failure. Receipt `Kb80M04Registry-registry-control.txt`.

| world | exit | counter line | exact detector |
|---|---|---|---|
| M1 `e320359` | 1 | `62 of 63 …; phantom 0` | `check_allowed_tools.py  no gate verdict map lacks 0=clean and 1=failed` |
| M2 `8a19a6a` | 1 | `62 of 63 …; phantom 0` | `check_desc_craft.py  no self-test cell names no backticked flag` |
| M3 `50ccb9c` | 1 | `62 of 63 …; phantom 0` | `check_r75_routed_repairs.py  no probe verdict map declares 1=failed; probe script has an exact --self-test handler` |
| M4 `ee9d17e` | **0** | `63 of 63 …; phantom 0` | — (no detector fired) |
| M5 `e5e1f96` | 1 | `62 of 63 …; phantom 1` | `check_allowed_tools.py  no registry rows naming it: 0 (need 1)` + `PHANTOM verifiers/check_allowed_tools_probe.py` |

## Battery level — the registry gate is load-bearing for C1

Command (cwd = scratch clone, fresh `TMPDIR` per run, own exit captured):

```
TMPDIR=$S/tmp/<name> python3 -B verifiers/check_tip_battery.py --repo $S/clone --rev <rev> --fleet /home/vgpnk/Projects/shokunin > receipt 2>&1; echo "exit=$?" >> receipt
```

Base figure cited from the published receipt
`.ufo/waves/round-80/receipts/tipbattery-base-dot.txt` (2026-10-27T22:57:17Z):
`guards 5 of 5; tip battery exit 0: 1 of 6`, `gate verifiers/check_gate_registry.py exit 1`.

| world | registry gate | frozen line | battery exit |
|---|---|---|---|
| base `398cbe1` (published) | exit 1 | `guards 5 of 5; tip battery exit 0: 1 of 6` | 1 |
| control `28a9dcb` | **exit 0** | `guards 5 of 5; tip battery exit 0: 2 of 6` | 1 |
| M1 `e320359` | exit 1 | `guards 5 of 5; tip battery exit 0: 1 of 6` | 1 |
| M2 `8a19a6a` | exit 1 | `guards 5 of 5; tip battery exit 0: 1 of 6` | 1 |
| M3 `50ccb9c` | exit 1 | `guards 5 of 5; tip battery exit 0: 1 of 6` | 1 |
| M4 `ee9d17e` | exit 0 | `guards 5 of 5; tip battery exit 0: 2 of 6` | 1 |
| M5 `e5e1f96` | exit 1 | `guards 5 of 5; tip battery exit 0: 1 of 6` | 1 |

Reading: the registry delta is worth exactly one battery slot (base 1 → control 2 of 6
with `exit 0` on the gate; each killing mutant drops the figure back to 1 of 6 with
`exit 1` on the gate; nothing else moves — all five structural guards PASS `5 of 5` in
every run, floors-registry untouched, six instrument scripts byte-identical to base).
Battery exit is 1 in all my worlds because my minimal world carries only repair 1 of 5;
the claim-level 6 of 6 is not reachable here and was not the probe. The verdict that
matters: at any world where the registry rows carry one of the four killed defects, C1
cannot reach its frozen figure — the gate reds and the battery count drops by exactly
the registry slot.

## M4 SURVIVED — coverage finding

Dropping the withdrawal annotation ("claim withdrawn r79 before data …") from a
withdrawn row reds nothing: `check_gate_registry.py` extracts only `<code>=<class>`
pairs (`PAIR_RE`) from the verdict-map cell and never reads prose; no battery guard and
none of the other five frozen gates reads SKILL.md row prose either. Empirically: gate
`63 of 63, exit 0` and battery `2 of 6` — byte-identical readings to the control. The
r79-review,Q46 withdrawal status of `check_desc_craft.py`/`check_r75_routed_repairs.py`
is therefore enforced by human review only. This is a coverage finding, not permission
to change the contract: the annotation stays in the landed rows (the control patch keeps
it) and the round-80 non-author closure spot-check should eyeball it explicitly.

## Restoration and non-interference

- All mutants lived only in `/fast/scratch/hyaku/kotoba-r80/Kb80M04Registry/clone`
  (detached scratch commits); no sibling source and no lane file was mutated. The lane
  was only ever read: during my session the lane HEAD moved by others
  (`308bff94eab9e296631d6c1201566a02a224d559` at my final check) and
  `git -C <lane> status --porcelain -- SKILL.md verifiers/` printed 0 lines — my probe
  targets are untouched in the lane tree. Scratch dir removed before yielding.
- Receipts copied to build/ before cleanup; sha256 of every published file is in the
  receipt files' own `exit=` tail plus the table below.

## Published deliverables (sha256, all under `.ufo/waves/round-80/build/`)

```
131ed7ed682e4752936ccce572862d9bd5a7f090f6134cb3fbf9d3425392676f  Kb80M04Registry-control.patch
2013b9bd444e1adb41c3d2bdd6b29c1e19a537cfc7c13b59e7c4abe616ade6e5  Kb80M04Registry-mut1-verdict-map-swap.patch
58a0c246d3d9e66e04b12670b70cca47ebcebd203b21a8899c2f89f582a80bff  Kb80M04Registry-mut2-selftest-flag-missing.patch
041400506b8634eb52e50262558a5fd7e4b2aaf0c750e6eef4127d6e4c76a658  Kb80M04Registry-mut3-probe-kind.patch
810d278b6c8106a0519fa4591c3a7168a6332eb5fe9d85be892a6969d368d0f8  Kb80M04Registry-mut4-withdrawal-annotation-dropped.patch
dc1f6e6fb14745600d2fe8ed6c28860cec6539194491ff7034d321676ff4f775  Kb80M04Registry-mut5-nonexistent-script.patch
3a99b3783196e1160ea9694aaf4065ee92c6dda8723ae40f4b28bdddafcf92d8  Kb80M04Registry-registry-control.txt
48ea0720b5129240a49071dcef8c8a62585193c11cc63deb641688b2697c532c  Kb80M04Registry-registry-mut1-verdict-map-swap.txt
19dab6a41d9f4934d834f1a4018a4a1a52cd2b6aad7023640748584c53a6da7b  Kb80M04Registry-registry-mut2-selftest-flag-missing.txt
a954bf69a2bf546b4228f7dc3dc4073c990b5a2f99e4f621ba8bfe9130ad1b6c  Kb80M04Registry-registry-mut3-probe-kind.txt
0c6b115270ef2bd029b299e9907c7bdf049194ea1c854287f19823b218d8cf03  Kb80M04Registry-registry-mut4-withdrawal-annotation-dropped.txt
8f2b57440921b9917a0ad6d1c5baa6521ebc2bcd9477899d501b95c910bcb147  Kb80M04Registry-registry-mut5-nonexistent-script.txt
5d62ddff535a7562eb2a2d3d8de4de263b27ea4676cee35a5cd0a38b6933499c  Kb80M04Registry-tipbattery-control.txt
ad5685e789cacd6e521438798c21d07eb4a025819d2166801ea19deff9856ff6  Kb80M04Registry-tipbattery-mut1-verdict-map-swap.txt
8ac50f9d83dc0f06c2a313dae55f41e262d19f62d92f2c28a89163ac2a395699  Kb80M04Registry-tipbattery-mut2-selftest-flag-missing.txt
06d2a606efe71c71744812aa0a1df49f81efde5e35dc01de0f7dd2e191926b9d  Kb80M04Registry-tipbattery-mut3-probe-kind.txt
711962532f7bb934a91ac6772dfa6549b1c85748cf60b5ecd42a9967e3df1099  Kb80M04Registry-tipbattery-mut4-withdrawal-annotation-dropped.txt
4c67f301b8ac231c8dcbce67d8b72b984e7a8ba4eddf3cd8657d2b66ffb0d354  Kb80M04Registry-tipbattery-mut5-nonexistent-script.txt
```

Coordination note for the C1 battery runner (Kb80E10Battery): if the E01 seat's own
patch is absent, `Kb80M04Registry-control.patch` is the registry input I verified green
(63 of 63) at base — it is my control world, not the reviewed E01 deliverable; say which
you used. Its third row is my authorship from the r79 draft bytes.

VERDICT: registry layer is load-bearing for C1 — M1/M2/M3/M5 killed at gate and battery level (−1 battery slot each, control green baseline 63 of 63 / 2 of 6), M4 (withdrawal annotation) survives every machine check and stays a human-review obligation.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80M04Registry.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M04Registry-control.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M04Registry-mut1-verdict-map-swap.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M04Registry-mut2-selftest-flag-missing.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M04Registry-mut3-probe-kind.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M04Registry-mut4-withdrawal-annotation-dropped.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M04Registry-mut5-nonexistent-script.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M04Registry-registry-*.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80M04Registry-tipbattery-*.txt
