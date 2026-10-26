# World 5 — honest set, one token-stuffed vendor row

Defect: the TRAE row adds `~/.trae/skills/` to its roots. The page states the project root `.trae/skills/` and the user root `~/.trae-cn/skills`; it never states an international `~/.trae/skills/` (0 occurrences in `S217.page`).

Conjunct under test: **(a) token occurrence, under the counter's token shaping**.

Predicted reading (plan's predicate): **3 of 4, exit 1 by this bundle's own reading (the token, as written, is absent); the wave-1 counter draft reads 4 of 4, exit 0 — a kill-rule hit**.

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
cp -a "$B/5-token-stuffed/tree/." "$R"/
# 4. commit with a throwaway identity inside the sandbox only
git -C "$R" add -A
git -C "$R" -c user.name=<seat> -c user.email=<seat>@localhost commit -q -m "5-token-stuffed"

# 5. read it
REV=$(git -C "$R" rev-parse HEAD)
python3 -B "$B/own-reading.py" --repo "$R" --rev "$REV"
python3 -B "$B/../ExecCnCounter/check_cn_vendor_surfaces.py" --repo "$R" --rev "$REV"
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
     --file "$R/corpus/SOURCES.md" --today "$(date -I)"
```

`bash replay.sh 5-token-stuffed` from the parent directory performs exactly these steps.
If the counter draft's `SELF_SHA` is still all zeros it exits 2 with
`counter drifted`; replay.sh then runs a local copy with the value
`--print-self-sha` reports filled in, and the draft itself is never edited here.



Why the counter passes it: `token_forms()` (counter lines 337-346 in draft sha256 `051d3e2d…`) also tries the token with a leading `~/` removed, so `~/.trae/skills/` is backed by the snapshot's `.trae/skills/` — the project root standing in for a user root. The one-line delta that clears it: drop the `~/`-strip form (keep only the trailing-slash form); the token then reads absent, exactly as written.
