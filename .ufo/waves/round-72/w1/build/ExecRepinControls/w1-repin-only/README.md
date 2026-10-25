# w1-repin-only — C2 shortcut control (1 of 4)

Plan item: "a re-pin that edits only the baseline shas and paths and leaves rules OC-1…OC-6
unchanged (must read `p < 7`)". Base `c69711ee08279609374d895bb0f3c8c18ccf15c9`.

## Overlay inventory (complete files; copy onto the base)

| path | bytes | sha256 (prefix) |
|---|---|---|
| `verifiers/baseline.json` | 7 878 | `2696d58a6f4d08c5…` |
| `verifiers/check_substrate_pins.py` | 27 668 | `5b58e18b9534f71f…` |
| `verifiers/verify_surfaces.py` | 92 553 | `03e927f03c439272…` |

Three edits, nothing else (`world.patch`, 43 lines):

* `verifiers/baseline.json`: `opencode_binary_sha256` `538fcb1b…` → `ca9b3ee262e33bb4e7aa0e12…`
  (the live `~/.opencode/bin/opencode` v2.1.4). The omp pins already name the bytes of
  `omp.real`, so only the path moves on that side.
* `verifiers/check_substrate_pins.py`: `BINARIES` → `~/.local/bin/omp.real`,
  `~/.opencode/bin/opencode`.
* `verifiers/verify_surfaces.py`: `DEFAULT_BINARIES` → the same two paths.

`corpus/knowledge/instruction-surface-census-round13.md` (the OC-1…OC-6 rule table),
`verifiers/surfaces-baseline.json` (the 42 declared classes) and every rule implementation in
`verify_surfaces.py` are **byte-identical to the base** — no derivation happened.

## Replay (exact)

```
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=c69711ee08279609374d895bb0f3c8c18ccf15c9
P=$(mktemp -d /tmp/k72fleet-replay-w1.XXXXXX)
for e in /home/vgpnk/Projects/shokunin/*; do n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$n"; done
git clone --shared -q "$L" "$P/kotoba-shokunin"
C=$P/kotoba-shokunin
git -C "$C" checkout -q --detach "$BASE"
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || exit 1
git -C "$C" config user.name "round-72 C2 shortcut control"
git -C "$C" config user.email "control@example.invalid"
cp -R <this dir>/overlay/. "$C/"
git -C "$C" add -A && git -C "$C" commit -q -m "w1-repin-only: overlay on base $BASE"
cd "$C"
python3 -B verifiers/check_substrate_pins.py --json ; echo "exit=$?"
python3 -B verifiers/verify_surfaces.py --json     ; echo "exit=$?"
```

`./replay.sh` does exactly this (plus the counter step when the lane has it) and deletes the
sandbox on exit; `KEEP=1 ./replay.sh` keeps it.

## Observed (replay of 2026-10-25, this host)

```
world commit: b6c2e11b6218c5a7909cb2f676966fd82b2cdc2c
check_substrate_pins.py exit=0
verify_surfaces.py exit=1
check_substrate_repin_v2.py absent in the lane; counter not run
```

`observed-pins.json`: `pass 3 fail 0 exit_code 0` — `omp_binary_sha256 PASS`,
`omp_binary_mtime PASS`, `opencode_binary_sha256 PASS`.

`observed-surfaces.json`: `pass 5 fail 2 exit_code 1` —

| check | status | detail (first clause) |
|---|---|---|
| `surfaces.literal_present` | **FAIL** | 1 loader literal not verifiable: `opencode:instructions/CONTEXT.md` (`CONTEXT.md` absent from the dump) |
| `surfaces.no_uncovered_class` | PASS | all 8 extracted loader classes declared |
| `surfaces.opencode_extract` | **FAIL** | vacuity: 0 classes from 7 rules; 9 declared classes produced by no rule; OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6 matched nothing |
| `surfaces.table_parity` | PASS | 42 ids |
| `surfaces.literal_parity` | PASS | 42 literals |
| `surfaces.kind_parity` | PASS | 42 kinds |
| `surfaces.excluded_reason` | PASS | 8 excluded entries |

Substrate read: omp `/home/vgpnk/.local/bin/omp.real` `85d9daf3…` 256 702 432 bytes; opencode
`/home/vgpnk/.opencode/bin/opencode` `ca9b3ee2…` 240 416 944 bytes.

## Reading below the target

* **surfaces: `p = 5 < 7`** — the world defeats the *pins* conjunct completely (a sha/path edit
  reads `3/3, exit 0` with no re-derivation) and is stopped only by the extraction conjunct.
* The surface JSON here is byte-identical to `w2-ledger-all`'s and `w4-omp-mtime-stale`'s
  (`sha256 2afd5745a13675f3…`): the ledger file is invisible to both instruments.
