# diag-2b-recomputed — C2 shortcut control (diagnostic, not a control)

**What it is.** world 2 with `revenger`'s three mechanical cells recomputed from its pinned `SKILL.md` (the lane gained a skill file at the freeze head: `path=SKILL.md`, `names kotoba=no`, `arbitration=no`). Diagnostic: measures the carry-forward ceiling once the one stale mechanical cell set is fixed.

**Overlay** (copied over a fresh `--shared` clone of the lane at
`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`):

- `corpus/knowledge/sibling-overlap-census-round74.md` — the census entry.
- `PROVINCE.md` — the base file with the `## Adjacent` table rows re-pinned (world 7 keeps it at the base revision).
- `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` — the freeze receipt, copied unchanged. Not required: the counter falls back to the object store at `329e7d91` when the worktree lacks the file (measured: 18 of 20 with and without); the copy keeps the sandbox self-contained.

**Replay.**

```bash
F=/home/vgpnk/Projects/shokunin; BASE=1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
W=$F/kotoba-shokunin/.ufo/waves/round-74/w1/build/ExecSibControlsR74/diag-2b-recomputed
P=$(mktemp -d /tmp/k74fleet-diag-2b-recomputed.XXXX)
for e in "$F"/*; do b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"; done
git clone --shared -q --no-checkout "$F/kotoba-shokunin" "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q "$BASE"
cp -a "$W/overlay/." "$P/kotoba-shokunin/"
git -C "$P/kotoba-shokunin" -c user.name=control-seat \
    -c user.email=control@example.invalid add -A
git -C "$P/kotoba-shokunin" -c user.name=control-seat \
    -c user.email=control@example.invalid commit -q -m "control world diag-2b-recomputed"
(cd "$P/kotoba-shokunin" && python3 -B verifiers/check_sibling_reread.py --rev HEAD)
rm -rf "$P"
```

`../score_worlds.sh <counter.py>` runs that replay over every world and prints
`<world> <N of 20> <exit>`; `../score_worlds.sh --emulate` prints the expected
score from `../emulate_reread.py` (the plan's conjuncts with the base checker's
own functions) when the counter is not available.

**Expected score.** 19 of 20 (mode: measured (check_sibling_reread.py)).

**Row lanes that fail** (from the recorded run):

- `tabi`: classified none, but SKILL.md at the frozen head 856fa9e12021 names kotoba whole-word

**Bound.** The overlay is a test fixture: it is never committed to the lane and never merged. Scores are per-lane counts from the round-74 C2 predicate; the world says nothing about whether any classification is the right call.
