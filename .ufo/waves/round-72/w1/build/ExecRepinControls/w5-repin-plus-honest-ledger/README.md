# w5-repin-plus-honest-ledger — C2 shortcut control (6th, added)

Added at `ExecRepinCounter`'s request to make the **lowering hazard** a measured world instead of
a paragraph: this world is `w1-repin-only` (paths + baseline sha only, OC-1…OC-6 untouched) plus
the **honest minimal ledger** — exactly the one base opencode class whose literal is absent from
the live v2.1.4 dump (`opencode:instructions/CONTEXT.md`). Base
`c69711ee08279609374d895bb0f3c8c18ccf15c9`.

## Overlay inventory (complete files; copy onto the base)

| path | bytes | sha256 (prefix) |
|---|---|---|
| `verifiers/baseline.json` | 7 878 | `2696d58a6f4d08c5…` |
| `verifiers/check_substrate_pins.py` | 27 668 | `5b58e18b9534f71f…` |
| `verifiers/verify_surfaces.py` | 92 553 | `03e927f03c439272…` |
| `verifiers/census-removals.json` | 993 | `0d13…` (single row, `opencode:instructions/CONTEXT.md`) |

The ledger row's evidence: `strings -n 4 /home/vgpnk/.opencode/bin/opencode | grep -c -F
CONTEXT.md` → `0` (measured 2026-10-25; dump sha256 `020fb253…`). `removals[].class_id` is the
only field the counter reads.

## Replay (exact)

Identical to `w1-repin-only`'s (no `__CLONE__` substitution needed — the opencode path is the
live `~/.opencode/bin/opencode`): `./replay.sh` in this directory is that script with the world
name changed.

## Observed (replay of 2026-10-25, this host)

```
world commit: 752764508ac377ebc5704b7ba2fcd12273740acc
check_substrate_pins.py exit=0
verify_surfaces.py exit=1
```

`observed-pins.json`: `pass 3 fail 0 exit_code 0` (all three PASS on live paths).
`observed-surfaces.json`: `pass 5 fail 2 exit_code 1` — `surfaces.literal_present` FAIL
(`CONTEXT.md` absent), `surfaces.opencode_extract` FAIL (vacuity, 0 classes from 7 rules).

`../ledger-probe.py --dump /tmp/k72-oc-strings.txt --ledger overlay/verifiers/census-removals.json`:
`base opencode classes 9; ledgered 1; required 1` → `ledger conjunct HOLDS`, exit 0.

The frozen counter (my own run of `ExecRepinCounter`'s draft):

```
$ python3 -B <build>/ExecRepinCounter/check_substrate_repin_v2.py --rev 7527645… --repo <sandbox>/kotoba-shokunin
host substrate re-derived: pins OK 3/3; surfaces pass 5 of 7; removal ledger 1 of 1 verified
substrate opencode: /home/vgpnk/.opencode/bin/opencode sha256 ca9b3ee2… bytes 240416944 strings 1237844
FAIL surfaces: 5 of 7 check(s) PASS, 7 check(s) reported, 7 expected
exit=1
```

## What this world proves

At the **frozen target 7** this world reads exit 1, so it is a valid control (below target on
surfaces). The lowering hazard was then measured, not inferred: a throwaway copy of the counter
with `CHECKS_TOTAL = 5` (lane file untouched, /tmp copy deleted after) run against this world
reads `pins OK 3/3; surfaces pass 5 of 5; removal ledger 1 of 1 verified` as the output line,
but still **exit 1** (output retained as `observed-counter-L5.txt`):

```
FAIL surfaces: 5 of 7 check(s) PASS, 7 check(s) reported, 5 expected
```

The line documents the counter's row-count guard (`len(checks) != CHECKS_TOTAL` reds the run):
lowering the number alone cannot green this world while `verify_surfaces.py` still reports its 7
checks. The **reachable** hazard is a lowering **plus** retiring two checks from `CHECK_IDS` in
`verifiers/verify_surfaces.py` — a visible instrument change whose self-test assertion count moves
the `floors-registry.json` floor, so the floors gate can see it. What neither the target number nor
the verdict vector can see is the identity of the failing checks: this world's 7-check `(id,
status)` vector is byte-identical to w1's (`sha256 93cd5b3e29136d8c…`), so a
retirement-plus-lowering combination would read clean while the OC rules stay un-derived — the
load-bearing reason a lowering below 7 must carry a detail-reading check or an
extraction-population floor.
