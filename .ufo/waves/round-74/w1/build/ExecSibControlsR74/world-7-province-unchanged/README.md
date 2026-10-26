# world-7-province-unchanged — C2 shortcut control

**What it is.** world 2's entry against the base PROVINCE.md § Adjacent (round-49 commit cells, unchanged).

**Overlay** (copied over a fresh `--shared` clone of the lane at
`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`):

- `corpus/knowledge/sibling-overlap-census-round74.md` — the census entry.
- `PROVINCE.md` — the base file with the `## Adjacent` table rows re-pinned (world 7 keeps it at the base revision).
- `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` — the freeze receipt, copied unchanged. Not required: the counter falls back to the object store at `329e7d91` when the worktree lacks the file (measured: 18 of 20 with and without); the copy keeps the sandbox self-contained.

**Replay.**

```bash
F=/home/vgpnk/Projects/shokunin; BASE=1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
W=$F/kotoba-shokunin/.ufo/waves/round-74/w1/build/ExecSibControlsR74/world-7-province-unchanged
P=$(mktemp -d /tmp/k74fleet-world-7-province-unchanged.XXXX)
for e in "$F"/*; do b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"; done
git clone --shared -q --no-checkout "$F/kotoba-shokunin" "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q "$BASE"
cp -a "$W/overlay/." "$P/kotoba-shokunin/"
git -C "$P/kotoba-shokunin" -c user.name=control-seat \
    -c user.email=control@example.invalid add -A
git -C "$P/kotoba-shokunin" -c user.name=control-seat \
    -c user.email=control@example.invalid commit -q -m "control world world-7-province-unchanged"
(cd "$P/kotoba-shokunin" && python3 -B verifiers/check_sibling_reread.py --rev HEAD)
rm -rf "$P"
```

`../score_worlds.sh <counter.py>` runs that replay over every world and prints
`<world> <N of 20> <exit>`; `../score_worlds.sh --emulate` prints the expected
score from `../emulate_reread.py` (the plan's conjuncts with the base checker's
own functions) when the counter is not available.

**Expected score.** 4 of 20 (mode: measured (check_sibling_reread.py)).

**Row lanes that fail** (from the recorded run):

- `chousa`: PROVINCE.md § Adjacent commit 6c5eb1466f2b does not match the entry's 00f8c7f5272a
- `kagi`: PROVINCE.md § Adjacent commit 899c50b42634 does not match the entry's 69b61db46be4
- `kaidoku`: PROVINCE.md § Adjacent commit 08c7a7299ed6 does not match the entry's 3b1ab3c9d248
- `kake`: PROVINCE.md § Adjacent commit e73d48bbf207 does not match the entry's 20217f23eca1
- `kama`: PROVINCE.md § Adjacent commit c808ba07f09c does not match the entry's 3e6fdbe9e0ca
- `kasegi`: PROVINCE.md § Adjacent commit 1fafde8f1145 does not match the entry's a155310d1ee9
- `kengaku`: PROVINCE.md § Adjacent commit 1f3b0f1ec41e does not match the entry's f9efce3beb07
- `kotodama`: PROVINCE.md § Adjacent commit 35f0d49f96f1 does not match the entry's f7104cbce186
- `kumitate`: PROVINCE.md § Adjacent commit fac39171ac28 does not match the entry's 2ca91a0c8154
- `mado`: PROVINCE.md § Adjacent commit e33ea30461f6 does not match the entry's 62dd798bb084
- `mori`: PROVINCE.md § Adjacent commit 28b79d3d1b76 does not match the entry's 24ebc7991e90
- `revenger`: base row check: row 16 (census line 20) (lane revenger): SKILL.md exists at the pin but the skill cell says NONE; base row check: row 16 (census line 20) (lane revenger): names-kotoba cell 'no SKILL.md' but the pinned description gives 'no'; base row check: row 16 (census line 20) (lane revenger): arbitration cell 'no SKILL.md' but the pinned description gives 'no'; PROVINCE.md § Adjacent commit 876630dbb4d6 does not match the entry's 6da884c6708f
- `souji`: PROVINCE.md § Adjacent commit 4edb25dfe262 does not match the entry's b8cb4b31ce80
- `tabi`: PROVINCE.md § Adjacent commit e3cf4e0d30bb does not match the entry's 856fa9e12021; classified none, but SKILL.md at the frozen head 856fa9e12021 names kotoba whole-word
- `tameshi`: PROVINCE.md § Adjacent commit 3b20f073c730 does not match the entry's a944eb55d64a
- `tsukuroi`: PROVINCE.md § Adjacent commit 22fd1642e7fa does not match the entry's 8bd001f58bfd

**Bound.** The overlay is a test fixture: it is never committed to the lane and never merged. Scores are per-lane counts from the round-74 C2 predicate; the world says nothing about whether any classification is the right call.
