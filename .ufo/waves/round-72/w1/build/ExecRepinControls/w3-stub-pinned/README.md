# w3-stub-pinned — C2 shortcut control (3 of 4)

Plan item: "a stub file at the pinned opencode path whose sha is pinned (must fail extraction
vacuity)". Base `c69711ee08279609374d895bb0f3c8c18ccf15c9`. This world is `w1-repin-only` with
the opencode path moved onto a 358-byte text stub inside the clone and the baseline pin set to
the stub's sha.

## Overlay inventory (complete files; copy onto the base)

| path | bytes | sha256 (prefix) |
|---|---|---|
| `verifiers/baseline.json` | 7 878 | `c77087e57b4ad6ea…` |
| `verifiers/check_substrate_pins.py` | 27 680 | `8da15d9260ddc84e…` |
| `verifiers/verify_surfaces.py` | 92 565 | `9cf7fc86f1bc33d2…` |
| `verifiers/fixtures/opencode-stub.bin` | 358 | `80bb558fc717ff9d…` |

* `baseline.json`: `opencode_binary_sha256` = `80bb558fc717ff9df2837e0f26916852ce5df75740682681db2967ea6b192aac`
  (the stub's own sha). `omp_binary_sha256` / `omp_binary_mtime` stay at the r51 values, which the
  live `omp.real` still satisfies. No key shaped `opencode_binary_<word>` was added, so the pin
  script still reports exactly 3 rows.
* both path constants: `opencode` → `__CLONE__/verifiers/fixtures/opencode-stub.bin`, the literal
  placeholder `replay.sh` substitutes with the sandbox clone's absolute path.
* the stub is five comment lines plus two text lines; `strings -n 4` of it yields those words and
  nothing that could be a loader shape.

## Replay (exact)

```
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=c69711ee08279609374d895bb0f3c8c18ccf15c9
P=$(mktemp -d /tmp/k72fleet-replay-w3.XXXXXX)
for e in /home/vgpnk/Projects/shokunin/*; do n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$n"; done
git clone --shared -q "$L" "$P/kotoba-shokunin"
C=$P/kotoba-shokunin
git -C "$C" checkout -q --detach "$BASE"
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || exit 1
git -C "$C" config user.name "round-72 C2 shortcut control"
git -C "$C" config user.email "control@example.invalid"
cp -R <this dir>/overlay/. "$C/"
sed -i "s|__CLONE__|$C|g" "$C/verifiers/check_substrate_pins.py" "$C/verifiers/verify_surfaces.py"
git -C "$C" add -A && git -C "$C" commit -q -m "w3-stub-pinned: overlay on base $BASE"
cd "$C"
python3 -B verifiers/check_substrate_pins.py --json ; echo "exit=$?"
python3 -B verifiers/verify_surfaces.py --json     ; echo "exit=$?"
```

`./replay.sh` does exactly this (plus the counter step when the lane has it). The sandbox must
outlive the counter run: the pinned opencode path is absolute and points into it.

## Observed (replay of 2026-10-25, this host)

```
world commit: 5a2621a6b2792d216341b5eb55090bc4d103d6f3
check_substrate_pins.py exit=0
verify_surfaces.py exit=1
check_substrate_repin_v2.py absent in the lane; counter not run
```

`observed-pins.json`: `pass 3 fail 0 exit_code 0` — including
`opencode_binary_sha256 PASS` against
`/tmp/k72fleet-replay-w3.H1gjCn/kotoba-shokunin/verifiers/fixtures/opencode-stub.bin`.

`observed-surfaces.json`: `pass 5 fail 2 exit_code 1` —

| check | status | detail (first clause) |
|---|---|---|
| `surfaces.literal_present` | **FAIL** | 9 loader literals not verifiable (every declared opencode literal is absent from the stub dump) |
| `surfaces.opencode_extract` | **FAIL** | vacuity: 0 classes from 7 rules; 9 declared classes produced by no rule |
| the other five | PASS | same as w1 |

Substrate read: opencode = the 358-byte stub, `80bb558f…`.

## Reading below the target

* **surfaces: `p = 5 < 7`** — extraction vacuity, exactly as the plan requires of this control.
* **pins conjunct: defeated** — `3/3, exit 0` against a text stub. The pins instrument compares a
  sha and an mtime; it has no notion of "is this a binary".
* The 7-check `(id, status)` vector is byte-identical to w1's
  (`jq -c '[.checks[]|{id,status}]' | sha256sum` → `93cd5b3e29136d8c…` for both). Only `detail`
  differs (9 unverifiable literals here, 1 on the live bytes). This is the calibration finding:
  at the verdict level a stub is indistinguishable from a genuine un-derived substrate.
