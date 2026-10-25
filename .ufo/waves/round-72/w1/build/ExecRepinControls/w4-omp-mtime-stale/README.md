# w4-omp-mtime-stale — C2 shortcut control (4 of 4)

Plan item: "a world that pins `omp.real` but leaves `omp_binary_mtime` at the old value". Base
`c69711ee08279609374d895bb0f3c8c18ccf15c9`. This world is `w1-repin-only` with one extra byte
edit: `omp_binary_mtime` back at the round-47 stamp.

## Overlay inventory (complete files; copy onto the base)

| path | bytes | sha256 (prefix) |
|---|---|---|
| `verifiers/baseline.json` | 7 878 | `fdc9cb61f52c6f8e…` |
| `verifiers/check_substrate_pins.py` | 27 668 | `5b58e18b9534f71f…` |
| `verifiers/verify_surfaces.py` | 92 553 | `03e927f03c439272…` |

Edits (`world.patch`, 48 lines):

* `baseline.json`: `opencode_binary_sha256` → `ca9b3ee2…` (live v2.1.4) **and**
  `omp_binary_mtime` `2026-10-21T20:37:24.615549837-03:00` → `2026-10-21T03:30:38.135013187-03:00`
  (the round-47 value for the earlier `omp/18.12.5` build). `omp_binary_sha256` stays correct for
  `omp.real`.
* both path constants → `~/.local/bin/omp.real`, `~/.opencode/bin/opencode`.

## Replay (exact)

```
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=c69711ee08279609374d895bb0f3c8c18ccf15c9
P=$(mktemp -d /tmp/k72fleet-replay-w4.XXXXXX)
for e in /home/vgpnk/Projects/shokunin/*; do n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$n"; done
git clone --shared -q "$L" "$P/kotoba-shokunin"
C=$P/kotoba-shokunin
git -C "$C" checkout -q --detach "$BASE"
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || exit 1
git -C "$C" config user.name "round-72 C2 shortcut control"
git -C "$C" config user.email "control@example.invalid"
cp -R <this dir>/overlay/. "$C/"
git -C "$C" add -A && git -C "$C" commit -q -m "w4-omp-mtime-stale: overlay on base $BASE"
cd "$C"
python3 -B verifiers/check_substrate_pins.py --json ; echo "exit=$?"
python3 -B verifiers/verify_surfaces.py --json     ; echo "exit=$?"
```

`./replay.sh` does exactly this (plus the counter step when the lane has it).

## Observed (replay of 2026-10-25, this host)

```
world commit: 1e997d59403ec8b61fe1b1dc2e51c8ca8612f688
check_substrate_pins.py exit=1
verify_surfaces.py exit=1
check_substrate_repin_v2.py absent in the lane; counter not run
```

`observed-pins.json`: `pass 2 fail 1 exit_code 1` —

| pin | verdict | observed |
|---|---|---|
| `omp_binary_sha256` | PASS | `85d9daf3…` on `/home/vgpnk/.local/bin/omp.real` |
| `omp_binary_mtime` | **DRIFT** | `expect 2026-10-21T03:30:38.135013187-03:00`, observed `1792625844615549837` ns, `delta_ns 173397942086864`, `tolerance_ns 0` |
| `opencode_binary_sha256` | PASS | `ca9b3ee2…` on `/home/vgpnk/.opencode/bin/opencode` |

`observed-surfaces.json`: `pass 5 fail 2 exit_code 1`, byte-identical to
`w1-repin-only/observed-surfaces.json` (`sha256 2afd5745a13675f3…`) — the surfaces instrument does
not read the pin block at all.

## Reading below the target

* **pins: `k = 2 < 3`** — the mtime conjunct is the one this world isolates; a correct sha does
  not carry a stale mtime, so the pin pair is genuinely two-sided.
* **surfaces: `p = 5 < 7`** — unchanged from w1.
* Note for the counter: a stale mtime reds the pin half while the surfaces half is untouched, so
  the two conjuncts are independent — and, per w1/w3, the pin half alone is satisfiable without
  any derivation.
