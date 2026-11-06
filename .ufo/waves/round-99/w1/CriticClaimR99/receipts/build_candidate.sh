#!/bin/bash
# build_candidate.sh -- build the round-99 candidate branches in the critic's scratch clone.
# Usage: build_candidate.sh <branch> <patch> [<patch> ...]
# Patches are applied in the order given on a fresh branch from the freeze commit.
set -euo pipefail
D=/fast/scratch/hyaku/kotoba-r99/CriticClaimR99/repo
FREEZE=b53e209603e7c480cd975ea543e415b66f695438
branch=$1; shift
cd "$D"
[ "$(git rev-parse --show-toplevel)" = "$D" ] || { echo "not my clone" >&2; exit 2; }
git checkout -q -B "$branch" "$FREEZE"
git reset -q --hard "$FREEZE"
git clean -fdq
for p in "$@"; do
  git apply --check "$p"
  git apply "$p"
  echo "applied $p"
done
git add -A
git -c user.name=scratch -c user.email=scratch@invalid commit -q -m "candidate $branch"
git rev-parse HEAD
