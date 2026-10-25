# w3b-stub-full-ledger — C2 shortcut control (composite, added by this seat)

Not one of the four worlds the plan names. It is `w3-stub-pinned` **plus** `w2-ledger-all`'s
ledger, and it exists because each of those two worlds defeats only one conjunct: w3 beats the
pins conjunct and the extraction vacuity keeps `p < 7`; w2 beats nothing but is the ledger the
stub world would need. Combined, every conjunct except `p == 7` holds. Base
`c69711ee08279609374d895bb0f3c8c18ccf15c9`.

## Overlay inventory (complete files; copy onto the base)

| path | bytes | sha256 (prefix) |
|---|---|---|
| `verifiers/baseline.json` | 7 878 | `c77087e57b4ad6ea…` |
| `verifiers/check_substrate_pins.py` | 27 680 | `8da15d9260ddc84e…` |
| `verifiers/verify_surfaces.py` | 92 565 | `9cf7fc86f1bc33d2…` |
| `verifiers/fixtures/opencode-stub.bin` | 358 | `80bb558fc717ff9d…` |
| `verifiers/census-removals.json` | 2 755 | `95f52436af986b3e…` |

Identical to `w3-stub-pinned` plus the ledger of all nine base opencode classes.

## Replay (exact)

Same as `w3-stub-pinned` with `w3b` in the sandbox name, the commit message and the `__CLONE__`
substitution — `./replay.sh` in this directory is that script, verbatim:

```
P=$(mktemp -d /tmp/k72fleet-replay-w3b.XXXXXX)   # fleet-shaped parent, 38 symlinks
git clone --shared -q "$L" "$P/kotoba-shokunin"
C=$P/kotoba-shokunin
git -C "$C" checkout -q --detach c69711ee08279609374d895bb0f3c8c18ccf15c9
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || exit 1
cp -R <this dir>/overlay/. "$C/"
sed -i "s|__CLONE__|$C|g" "$C/verifiers/check_substrate_pins.py" "$C/verifiers/verify_surfaces.py"
git -C "$C" add -A && git -C "$C" commit -q -m "w3b-stub-full-ledger: overlay on base <base>"
cd "$C"
python3 -B verifiers/check_substrate_pins.py --json ; echo "exit=$?"
python3 -B verifiers/verify_surfaces.py --json     ; echo "exit=$?"
```

## Observed (replay of 2026-10-25, this host)

```
world commit: b04a34b94a9bd10c2fe88053fbe876a3d87677ec
check_substrate_pins.py exit=0
verify_surfaces.py exit=1
check_substrate_repin_v2.py absent in the lane; counter not run
```

`observed-pins.json`: `pass 3 fail 0 exit_code 0` — all three PASS, the opencode one against the
358-byte stub.
`observed-surfaces.json`: `pass 5 fail 2 exit_code 1` — `surfaces.literal_present` FAIL (9
literals absent), `surfaces.opencode_extract` FAIL (vacuity, 0 classes from 7 rules).

Ledger conjunct, measured with `../ledger-probe.py` against the stub's own `strings -n 4` dump:

```
$ strings -n 4 overlay/verifiers/fixtures/opencode-stub.bin > /tmp/stub-strings.txt
$ python3 -B ../ledger-probe.py --dump /tmp/stub-strings.txt \
      --ledger overlay/verifiers/census-removals.json
base opencode classes 9; ledgered 9; required 9
  (every declared literal: count 0, absent)
ledger conjunct HOLDS                                    # exit 0
```

## Reading below the target — and why it is the headline

* **surfaces: `p = 5 < 7`** — the only conjunct this world fails.
* **pins: 3/3, exit 0** and **ledger: HOLDS** — both satisfied by a 358-byte text file plus a
  wholesale ledger.
* Consequence: if the wave-1 Q45 census lowers the surfaces target to 5 or less (the plan permits
  a lowering before data), **this world reads exit 0** — a shortcut world passing the counter,
  which the kill rule forbids. The counter therefore needs a substrate-identity conjunct before
  data (e.g. the pinned opencode bytes must be the live ELF `ca9b3ee2…` / 240 416 944 bytes, or a
  size/ELF-magic floor), because `pass`-counting alone cannot see the difference: the 7-check
  `(id, status)` vector here is byte-identical to `w1-repin-only`'s
  (`sha256 93cd5b3e29136d8c…`).
