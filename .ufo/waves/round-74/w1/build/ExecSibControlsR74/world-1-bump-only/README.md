# world-1-bump-only — C2 shortcut control

**What it is.** r49 entry copied to the r74 path with every census commit cell bumped to the freeze head and nothing else (no delta cell, quotes and mechanical cells as written at round 49).

**Overlay** (copied over a fresh `--shared` clone of the lane at
`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`):

- `corpus/knowledge/sibling-overlap-census-round74.md` — the census entry.
- `PROVINCE.md` — the base file with the `## Adjacent` table rows re-pinned (world 7 keeps it at the base revision).
- `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` — the freeze receipt, copied unchanged. Not required: the counter falls back to the object store at `329e7d91` when the worktree lacks the file (measured: 18 of 20 with and without); the copy keeps the sandbox self-contained.

**Replay.**

```bash
F=/home/vgpnk/Projects/shokunin; BASE=1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
W=$F/kotoba-shokunin/.ufo/waves/round-74/w1/build/ExecSibControlsR74/world-1-bump-only
P=$(mktemp -d /tmp/k74fleet-world-1-bump-only.XXXX)
for e in "$F"/*; do b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"; done
git clone --shared -q --no-checkout "$F/kotoba-shokunin" "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q "$BASE"
cp -a "$W/overlay/." "$P/kotoba-shokunin/"
git -C "$P/kotoba-shokunin" -c user.name=control-seat \
    -c user.email=control@example.invalid add -A
git -C "$P/kotoba-shokunin" -c user.name=control-seat \
    -c user.email=control@example.invalid commit -q -m "control world world-1-bump-only"
(cd "$P/kotoba-shokunin" && python3 -B verifiers/check_sibling_reread.py --rev HEAD)
rm -rf "$P"
```

`../score_worlds.sh <counter.py>` runs that replay over every world and prints
`<world> <N of 20> <exit>`; `../score_worlds.sh --emulate` prints the expected
score from `../emulate_reread.py` (the plan's conjuncts with the base checker's
own functions) when the counter is not available.

**Expected score.** 0 of 20 (mode: measured (check_sibling_reread.py)).

**Row lanes that fail** (from the recorded run):

- `audio`: entry has no row for audio
- `chousa`: entry has no row for chousa
- `game-dev-2d`: entry has no row for game-dev-2d
- `game-dev-3d`: entry has no row for game-dev-3d
- `kagi`: entry has no row for kagi
- `kaidoku`: entry has no row for kaidoku
- `kake`: entry has no row for kake
- `kama`: entry has no row for kama
- `kasegi`: entry has no row for kasegi
- `kengaku`: entry has no row for kengaku
- `kotodama`: entry has no row for kotodama
- `kumitate`: entry has no row for kumitate
- `lore`: entry has no row for lore
- `mado`: entry has no row for mado
- `mori`: entry has no row for mori
- `revenger`: entry has no row for revenger
- `souji`: entry has no row for souji
- `tabi`: entry has no row for tabi
- `tameshi`: entry has no row for tameshi
- `tsukuroi`: entry has no row for tsukuroi

**Bound.** The overlay is a test fixture: it is never committed to the lane and never merged. Scores are per-lane counts from the round-74 C2 predicate; the world says nothing about whether any classification is the right call.
