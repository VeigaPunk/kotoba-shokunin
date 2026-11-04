#!/usr/bin/env bash
# score.sh <world-tag> <module-file> <ledger-file|none>  -> receipts/<tag>.txt
set -u
S=/fast/scratch/hyaku/kotoba-r86/Critic
D=$S/repo
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
FREEZE=${FREEZE:-ecfad51fe3f24540a6d67d2b54920929c7b83041}
export TMPDIR=$S
tag=$1 mod=$2 led=$3
[ "$(git -C "$D" rev-parse --show-toplevel)" = "$D" ] || { echo "clone toplevel mismatch"; exit 2; }
git -C "$D" reset -q --hard "$FREEZE"
cp "$mod" "$D/verifiers/verify_harness_claims.py"
if [ "$led" != none ]; then cp "$led" "$D/verifiers/omp-skill-roots.tsv"; git -C "$D" add verifiers/omp-skill-roots.tsv; fi
git -C "$D" -c user.name=seat -c user.email=seat@local commit -qam "world $tag"
rev=$(git -C "$D" rev-parse HEAD)
mkdir -p "$S/receipts" "$S/work-$tag"
{
  echo "# world $tag  (critic seat, round 86; scratch clone of $FREEZE)"
  echo "\$ sha256sum verifiers/verify_harness_claims.py verifiers/omp-skill-roots.tsv (at $rev)"
  (cd "$D" && sha256sum verifiers/verify_harness_claims.py; [ -f verifiers/omp-skill-roots.tsv ] && sha256sum verifiers/omp-skill-roots.tsv || echo "no ledger")
  sha256sum "$LANE/verifiers/check_omp_catalogue_repro.py"
  echo "$ TMPDIR=$S python3 -B $LANE/verifiers/check_omp_catalogue_repro.py --repo $D --rev $rev --work $S/work-$tag"
  python3 -B "$LANE/verifiers/check_omp_catalogue_repro.py" --repo "$D" --rev "$rev" --work "$S/work-$tag"
  echo "exit=$?"
} > "$S/receipts/$tag.txt" 2>&1
rm -rf "$S/work-$tag"
grep -E '^(guard|omp catalogue|exit=|could-not)' "$S/receipts/$tag.txt"
grep -c 'render-differs' "$S/receipts/$tag.txt" | sed 's/^/render-differs /'
grep -c 'not-discovered' "$S/receipts/$tag.txt" | sed 's/^/not-discovered /'
