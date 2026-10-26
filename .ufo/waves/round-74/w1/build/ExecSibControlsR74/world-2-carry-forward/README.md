# world-2-carry-forward — C2 shortcut control

**What it is.** world 1 plus a `delta` cell per row computed from `git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md` and quotes re-located by script wherever the old text still exists at the new pin. The pure carry-forward: measured, not asserted below 20.

**Overlay** (copied over a fresh `--shared` clone of the lane at
`1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`):

- `corpus/knowledge/sibling-overlap-census-round74.md` — the census entry.
- `PROVINCE.md` — the base file with the `## Adjacent` table rows re-pinned (world 7 keeps it at the base revision).
- `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` — the freeze receipt, copied unchanged. Not required: the counter falls back to the object store at `329e7d91` when the worktree lacks the file (measured: 18 of 20 with and without); the copy keeps the sandbox self-contained.

**Replay.**

```bash
F=/home/vgpnk/Projects/shokunin; BASE=1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
W=$F/kotoba-shokunin/.ufo/waves/round-74/w1/build/ExecSibControlsR74/world-2-carry-forward
P=$(mktemp -d /tmp/k74fleet-world-2-carry-forward.XXXX)
for e in "$F"/*; do b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"; done
git clone --shared -q --no-checkout "$F/kotoba-shokunin" "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q "$BASE"
cp -a "$W/overlay/." "$P/kotoba-shokunin/"
git -C "$P/kotoba-shokunin" -c user.name=control-seat \
    -c user.email=control@example.invalid add -A
git -C "$P/kotoba-shokunin" -c user.name=control-seat \
    -c user.email=control@example.invalid commit -q -m "control world world-2-carry-forward"
(cd "$P/kotoba-shokunin" && python3 -B verifiers/check_sibling_reread.py --rev HEAD)
rm -rf "$P"
```

`../score_worlds.sh <counter.py>` runs that replay over every world and prints
`<world> <N of 20> <exit>`; `../score_worlds.sh --emulate` prints the expected
score from `../emulate_reread.py` (the plan's conjuncts with the base checker's
own functions) when the counter is not available.

**Expected score.** 18 of 20 (mode: measured (check_sibling_reread.py)).

**Row lanes that fail** (from the recorded run):

- `revenger`: base row check: row 16 (census line 20) (lane revenger): SKILL.md exists at the pin but the skill cell says NONE; base row check: row 16 (census line 20) (lane revenger): names-kotoba cell 'no SKILL.md' but the pinned description gives 'no'; base row check: row 16 (census line 20) (lane revenger): arbitration cell 'no SKILL.md' but the pinned description gives 'no'
- `tabi`: classified none, but SKILL.md at the frozen head 856fa9e12021 names kotoba whole-word

**Bound.** The overlay is a test fixture: it is never committed to the lane and never merged. Scores are per-lane counts from the round-74 C2 predicate; the world says nothing about whether any classification is the right call.
