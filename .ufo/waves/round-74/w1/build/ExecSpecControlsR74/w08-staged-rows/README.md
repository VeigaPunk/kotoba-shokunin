# w08-staged-rows — round-74 C1 shortcut control

Base: lane `kotoba-shokunin`, branch `master`, rev `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` (the r73 non-author closure
spot-check commit, r74 plan `329e7d91d7d750031c35d264f0e34af1d0ce8385`). Plan § C1 shortcut
controls. The world is a single patch applied to a **fresh `--shared` clone** of the base in a
fleet-shaped `/tmp` sandbox; the commit exists only inside that clone.

## What it changes

the package's `SOURCES.append.md` appended as-is inside `## Registry` (campaign-schema rows, its own header row, prose recheck, ids S203–S3xx that collide with the lane's).

Files carried by `world.patch` (complete new content for each):

- `.ufo/waves/round-74/snapshots/MANIFEST.sha256` (247 B)
- `.ufo/waves/round-74/snapshots/best-practices.md` (15060 B)
- `.ufo/waves/round-74/snapshots/quickstart.md` (4080 B)
- `.ufo/waves/round-74/snapshots/using-scripts.md` (12078 B)
- `PROVINCE.md` (21853 B)
- `SKILL.md` (75387 B)
- `corpus/SOURCES.md` (341092 B)
- `corpus/knowledge/spec-skill-creation-craft-round74.md` (2268 B)

## Predicate clause it defeats and expected score

- expected: **0 of 3 or exit 2 (below 3)**
- defeats: (b) the registry is not census-conformant: E02 on the second header row and E03/E04 on the colliding campaign ids.
- census at the applied revision (`scripts/sources-census.sh validate --today 2026-10-26 --file <clone>/corpus/SOURCES.md kotoba`): **exit 1**
- measured score: **0 of 3, exit 1**

## Replay (exact)

```
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
W=<this world dir>
P=$(mktemp -d /tmp/k74w1-fleet-w08-staged-rows.XXXXXX)
for e in /home/vgpnk/Projects/shokunin/*; do n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$n"; done
git clone --shared -q --no-checkout "$L" "$P/kotoba-shokunin"
C=$P/kotoba-shokunin
git -C "$C" checkout -q --detach "$BASE"
[ "$(git -C "$C" rev-parse --show-toplevel)" = "$C" ] || exit 1
git -C "$C" apply --whitespace=nowarn "$W/world.patch"
git -C "$C" add -A
git -C "$C" -c user.name='round-74 C1 control' -c user.email='control@example.invalid' \
  commit -q -m 'w08-staged-rows: shortcut world on 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908'
COUNTER=${COUNTER:-$L/.ufo/waves/round-74/w1/build/ExecSpecCounterR74/check_spec_craft.py}
cp "$COUNTER" "$C/_check_spec_craft_ctl.py"
cd "$C" && python3 -B _check_spec_craft_ctl.py --rev HEAD; echo "exit=$?"
```

`w08-staged-rows/score.stdout.txt` is the counter's own stdout for that run, `w08-staged-rows/score.stderr.txt` its
stderr (present only for a world in the counter's exit-2 class). `../score-worlds.out` is the whole
table over every world, produced by `../score_worlds.sh`; `../README.md` names the counter sha the
table was measured at.
