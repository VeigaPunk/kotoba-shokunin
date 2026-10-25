# w2-ledger-all — C2 shortcut control (2 of 4)

Plan item: "a world that ledgers every opencode class (must fail the exact-set conjunct)". Base
`c69711ee08279609374d895bb0f3c8c18ccf15c9`. This world is `w1-repin-only` plus a ledger file.

## Overlay inventory (complete files; copy onto the base)

| path | bytes | sha256 (prefix) |
|---|---|---|
| `verifiers/baseline.json` | 7 878 | `2696d58a6f4d08c5…` |
| `verifiers/check_substrate_pins.py` | 27 668 | `5b58e18b9534f71f…` |
| `verifiers/verify_surfaces.py` | 92 553 | `03e927f03c439272…` |
| `verifiers/census-removals.json` | 2 755 | `95f52436af986b3e…` |

`census-removals.json` is new (the file does not exist at the base). Shape, confirmed with the
counter seat: `{"removals": [{"class_id": "<id>", "literal": …, "context_kind": …, "reason": …,
"evidence": …}]}`; the counter reads only `removals[].class_id` (string, non-empty). It ledgers
**all nine** opencode classes declared at the base, each with
`"evidence": "none supplied (the shortcut)"`.

## Replay (exact)

```
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=c69711ee08279609374d895bb0f3c8c18ccf15c9
P=$(mktemp -d /tmp/k72fleet-replay-w2.XXXXXX)
for e in /home/vgpnk/Projects/shokunin/*; do n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$n"; done
git clone --shared -q "$L" "$P/kotoba-shokunin"
C=$P/kotoba-shokunin
git -C "$C" checkout -q --detach "$BASE"
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || exit 1
git -C "$C" config user.name "round-72 C2 shortcut control"
git -C "$C" config user.email "control@example.invalid"
cp -R <this dir>/overlay/. "$C/"
git -C "$C" add -A && git -C "$C" commit -q -m "w2-ledger-all: overlay on base $BASE"
cd "$C"
python3 -B verifiers/check_substrate_pins.py --json ; echo "exit=$?"
python3 -B verifiers/verify_surfaces.py --json     ; echo "exit=$?"
```

`./replay.sh` does exactly this (plus the counter step when the lane has it).

## Observed (replay of 2026-10-25, this host)

```
world commit: 5597aa2d575945ac296d504a13b88d34d96b4f7a
check_substrate_pins.py exit=0
verify_surfaces.py exit=1
check_substrate_repin_v2.py absent in the lane; counter not run
```

`observed-pins.json`: `pass 3 fail 0 exit_code 0` (three PASS).
`observed-surfaces.json`: `pass 5 fail 2 exit_code 1`, and **byte-identical** to
`w1-repin-only/observed-surfaces.json` (`sha256 2afd5745a13675f3…`) — neither existing instrument
opens `census-removals.json`.

The conjunct this world exists for is measured with `../ledger-probe.py` (probe, not the counter):

```
$ python3 -B ../ledger-probe.py --dump /tmp/k72-oc-strings.txt \
      --ledger overlay/verifiers/census-removals.json
base opencode classes 9; ledgered 9; required 1
  opencode:instructions/CONTEXT.md         literal CONTEXT.md         count 0     absent
  … eight more, all "present" (AGENTS.md 15, CLAUDE.md 3, instructions 281, https:// 1282, <system-reminder> 15)
FAIL ledgered but literal present: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md,
  opencode:config/instructions, opencode:config/instructions-remote,
  opencode:instruction-context/AGENTS.md, opencode:instructions/AGENTS.md,
  opencode:instructions/CLAUDE.md, opencode:read-hook/instructions
ledger conjunct FAILS                                    # exit 1
```

For contrast the honest minimal ledger holds on the same dump: one row naming
`opencode:instructions/CONTEXT.md` gives `required 1`, `ledger conjunct HOLDS`, exit 0.

## Reading below the target

* **ledger conjunct: FAILS** — 8 ledgered classes still have their literal in the live dump; the
  exact-set rule rejects every one of them.
* **surfaces: `p = 5 < 7`** — same extraction state as w1, which the ledger does not touch.
* Pins read `3/3, exit 0` — the ledger buys nothing on the pins conjunct either.
