# World 7 — staged rows appended as-is in campaign schema

Defect: the six package rows (S214, S216, S217, S218, S219, S221) appended verbatim to the lane's registry under the staged entry; their `recheck` cells are prose, their `used-by` cells name package paths that do not exist in the lane, and S214/S216 collide with lane rows.

Conjunct under test: **(b) plus the registry schema**.

Predicted reading (plan's predicate): **0 of 4, exit 1; census exit 1**.

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
cp -a "$B/7-staged-rows-as-is/tree/." "$R"/
# 4. commit with a throwaway identity inside the sandbox only
git -C "$R" add -A
git -C "$R" -c user.name=<seat> -c user.email=<seat>@localhost commit -q -m "7-staged-rows-as-is"

# 5. read it
REV=$(git -C "$R" rev-parse HEAD)
python3 -B "$B/own-reading.py" --repo "$R" --rev "$REV"
python3 -B "$B/../ExecCnCounter/check_cn_vendor_surfaces.py" --repo "$R" --rev "$REV"
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
     --file "$R/corpus/SOURCES.md" --today "$(date -I)"
```

`bash replay.sh 7-staged-rows-as-is` from the parent directory performs exactly these steps.
If the counter draft's `SELF_SHA` is still all zeros it exits 2 with
`counter drifted`; replay.sh then runs a local copy with the value
`--print-self-sha` reports filled in, and the draft itself is never edited here.



Observed schema findings on the committed sandbox tree: E03 x2 (S214, S216 already in the lane), E09 x6 (every row's `recheck` is prose), E11 x15 (`used-by` package paths missing), W04 x20 (pre-existing) — exit 1. Running `--file` against this bundle's partial `tree/corpus/SOURCES.md` also exits 1 but reports 228 E11, because the bundle carries no `SKILL.md` and no `corpus/knowledge/` files; use the sandbox copy for attributable findings. The staged rows carry 11 cells and no escaped pipe (`grep -c '\\|'` over the six lines is 0), so the campaign schema's defect here is prose cells and package paths, not an escaped pipe.
