# World 3 — honest set, one vendor row carries an invented root

Defect: the TRAE row's discovery-root cell names `.bytedance/skills/`, a path that does not occur in `S217.page`; every other token, row and pin is honest.

Conjunct under test: **(a) token occurrence**.

Predicted reading (plan's predicate): **3 of 4, exit 1 (TRAE fails)**.

## Bundle

    tree/      the overlay copied over the sandbox worktree

## Replay (fresh `--shared` clone of the base; git writes only inside the sandbox)

```sh
# 1. fleet-shaped sandbox: symlink every fleet-root entry except the lane
P=$(mktemp -d /tmp/k73fleet-<you>.XXXX)
for e in /home/vgpnk/Projects/shokunin/*; do
  b=$(basename "$e"); [ "$b" = kotoba-shokunin ] && continue; ln -s "$e" "$P/$b"
done

# 2. a fresh shared clone at the frozen base, checked out on a throwaway branch
git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    "$P/kotoba-shokunin"
R=$P/kotoba-shokunin
git -C "$R" checkout -q -B world 072048fa8e8a52c707d25f7079772fa317244eb7
[ "$(git -C "$R" rev-parse --show-toplevel)" = "$R" ] || exit 1

# 3. apply the bundles (B = this bundle root; adjust the path if you copied it)
B=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecCnControls
cp -a "$B/_common/tree/." "$R"/
cp -a "$B/3-invented-root/tree/." "$R"/
# 4. commit with a throwaway identity inside the sandbox only
git -C "$R" add -A
git -C "$R" -c user.name=<seat> -c user.email=<seat>@localhost commit -q -m "3-invented-root"

# 5. read it
REV=$(git -C "$R" rev-parse HEAD)
python3 -B "$B/own-reading.py" --repo "$R" --rev "$REV"
python3 -B "$B/../ExecCnCounter/check_cn_vendor_surfaces.py" --repo "$R" --rev "$REV"
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
     --file "$R/corpus/SOURCES.md" --today "$(date -I)"
```

`bash replay.sh 3-invented-root` from the parent directory performs exactly these steps.
If the counter draft's `SELF_SHA` is still all zeros it exits 2 with
`counter drifted`; replay.sh then runs a local copy with the value
`--print-self-sha` reports filled in, and the draft itself is never edited here.



