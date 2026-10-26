#!/usr/bin/env bash
# score_worlds.sh -- run one counter over every control world and print
# "<world> <N of 20> <exit>".
#
#   score_worlds.sh <counter.py> [fleet-root] [--diag]   # the real counter, in a fresh sandbox
#   score_worlds.sh --emulate [fleet-root] [--diag]      # expected score, emulate_reread.py
#
# `--diag` also scores the diag-* bundles (diagnostics, not plan worlds).
#
# Counter mode replays each world the way the plan measures it: a fresh
# `--shared` clone of the base lane rev inside a fleet-shaped sandbox (every
# entry of the fleet root symlinked in except kotoba-shokunin), the world's
# overlay copied over it, one commit inside the sandbox only, then
# `python3 -B <counter> --rev HEAD` from the sandbox lane root.  The counter
# sees `../<lane>-shokunin` exactly as it does in the real measurement; the
# live fleet repos stay read-only.
#
# Emulate mode reads the overlay files in place and applies the plan's
# conjuncts with the base checker's functions; it is an expected score, never
# a measurement.
set -uo pipefail

HERE=$(cd "$(dirname "$0")" && pwd)
BASE_REV=1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
MODE=${1:-}
FLEET=${2:-/home/vgpnk/Projects/shokunin}
INCLUDE_DIAG=${3:-}
LANE=$(basename "$FLEET")/kotoba-shokunin

if [ -z "$MODE" ]; then
  echo "usage: $0 <counter.py>|--emulate [fleet-root]" >&2
  exit 2
fi

run_counter_world() {
  local world=$1 dir=$2
  local sandbox
  sandbox=$(mktemp -d /tmp/k74fleet-score.XXXXXX) || return 1
  local entry
  for entry in "$FLEET"/*; do
    [ "$(basename "$entry")" = kotoba-shokunin ] && continue
    ln -s "$entry" "$sandbox/$(basename "$entry")"
  done
  if ! git clone --shared -q --no-checkout "$FLEET/kotoba-shokunin" \
        "$sandbox/kotoba-shokunin"; then
    echo "$world ? of 20 2"; rm -rf "$sandbox"; return
  fi
  git -C "$sandbox/kotoba-shokunin" checkout -q "$BASE_REV" || {
    echo "$world ? of 20 2"; rm -rf "$sandbox"; return; }
  cp -a "$dir/overlay/." "$sandbox/kotoba-shokunin/" || {
    echo "$world ? of 20 2"; rm -rf "$sandbox"; return; }
  git -C "$sandbox/kotoba-shokunin" \
      -c user.name=control-seat -c user.email=control@example.invalid \
      add -A >/dev/null
  git -C "$sandbox/kotoba-shokunin" \
      -c user.name=control-seat -c user.email=control@example.invalid \
      commit -q -m "control world $world" >/dev/null
  local log=$HERE/logs/$world.log
  mkdir -p "$HERE/logs"
  # The counter resolves the lane from its own file path, not from cwd
  # (check_sibling_reread.py `resolve_repo`), so the sandbox lane root is
  # passed explicitly.  Without this the copy under the live lane measures the
  # live lane.
  ( cd "$sandbox/kotoba-shokunin" &&
    timeout 300 python3 -B "$MODE" --repo "$sandbox/kotoba-shokunin" --rev HEAD ) > "$log" 2>&1
  local rc=$?
  local n
  n=$(sed -n 's/.*sibling rows re-pinned and re-read \([0-9][0-9]*\) of 20.*/\1/p' "$log" | tail -1)
  printf '%s %s of 20 %s\n' "$world" "${n:-?}" "$rc"
  rm -rf "$sandbox"
}

run_emulated_world() {
  local world=$1 dir=$2
  # Emulated logs are kept apart from the measured ones (`logs/`), so a later
  # --emulate run can never overwrite the counter's evidence.
  local log=$HERE/logs-emulated/$world.log
  mkdir -p "$HERE/logs-emulated"
  ( cd "$HERE" && timeout 300 python3 -B emulate_reread.py "$dir" --fleet "$FLEET" ) \
      > "$log" 2>&1
  local rc=$?
  local n
  n=$(sed -n 's/.*sibling rows re-pinned and re-read \([0-9][0-9]*\) of 20.*/\1/p' "$log" | tail -1)
  printf '%s %s of 20 %s\n' "$world" "${n:-?}" "$rc"
}

if [ "$MODE" = "--emulate" ]; then
  echo "# mode: emulated expected score (emulate_reread.py), counter not run"
else
  echo "# mode: measured with $MODE"
fi

dirs=("$HERE"/world-*/)
if [ "$INCLUDE_DIAG" = "--diag" ]; then dirs+=("$HERE"/diag-*/); fi
for dir in "${dirs[@]}"; do
  world=$(basename "$dir")
  if [ "$MODE" = "--emulate" ]; then
    run_emulated_world "$world" "$dir"
  else
    run_counter_world "$world" "$dir"
  fi
done
