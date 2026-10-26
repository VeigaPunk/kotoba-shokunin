#!/usr/bin/env bash
# score_worlds.sh — run a C1 spec-craft counter over every round-74 shortcut world.
#
#   ./score_worlds.sh <counter.py> [world-dir ...]
#
# For each world: build a fleet-shaped sandbox (every sibling entry of the fleet root
# symlinked in, the lane cloned `--shared`), check out base 1e03d19, apply the world's
# `world.patch`, commit it inside the clone only, then run the counter at `--rev HEAD`.
# Prints one line per world:  <world> <N of 3> <exit>
# Exit 2 is the counter's environment class (tampered/unpinned snapshot) and prints no
# score line; that world's N field is `-` and the exit field carries the 2.
#
# Nothing is written outside the sandbox; the sandbox is removed on exit.
set -u

if [ $# -lt 1 ]; then
  sed -n '2,12p' "$0"; exit 2
fi
COUNTER=$(readlink -f "$1" 2>/dev/null) || { echo "no counter at $1" >&2; exit 2; }
shift
HERE=$(cd "$(dirname "$0")" && pwd)
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
FLEET=/home/vgpnk/Projects/shokunin
BASE=1e03d1991bc02281b00a5b7a5e00c9d5d5d72908

if [ $# -gt 0 ]; then
  WORLDS=("$@")
else
  mapfile -t WORLDS < <(find "$HERE" -maxdepth 1 -type d -name 'w[0-9][0-9]-*' | sort)
fi

P=$(mktemp -d /tmp/k74w1-score.XXXXXX)
trap 'rm -rf "$P"' EXIT

# Freeze the counter once: a file being edited mid-run makes every later world
# read `counter drifted` (a moving instrument is not a measurement).
cp "$COUNTER" "$P/_counter_frozen.py"
pin=$(sed -n 's/^SELF_SHA = "\([0-9a-f]*\)".*/\1/p' "$P/_counter_frozen.py")
live=$(python3 -B "$P/_counter_frozen.py" --print-self-sha 2>/dev/null)
if [ -z "$pin" ] || [ "$pin" != "$live" ]; then
  echo "counter is mid-edit (SELF_SHA $pin, blanked sha $live); refusing to score" >&2
  exit 2
fi
COUNTER="$P/_counter_frozen.py"
echo "# counter frozen: $COUNTER sha256 $(sha256sum "$P/_counter_frozen.py" | cut -d' ' -f1)" >&2
for e in "$FLEET"/*; do
  n=$(basename "$e")
  [ "$n" = kotoba-shokunin ] && continue
  ln -s "$e" "$P/$n"
done

fail=0
for W in "${WORLDS[@]}"; do
  name=$(basename "$W")
  [ -f "$W/world.patch" ] || { echo "$name - MISSING-PATCH"; fail=1; continue; }
  C="$P/$name"
  if ! git clone --shared -q --no-checkout "$LANE" "$C" 2>/dev/null; then
    echo "$name - CLONE-FAILED"; fail=1; continue
  fi
  git -C "$C" checkout -q --detach "$BASE" || { echo "$name - CHECKOUT-FAILED"; fail=1; continue; }
  if [ "$(git -C "$C" rev-parse --show-toplevel)" != "$C" ]; then
    echo "$name - NOT-OWN-TOPLEVEL"; fail=1; continue
  fi
  if ! git -C "$C" apply --whitespace=nowarn "$W/world.patch"; then
    echo "$name - PATCH-FAILED"; fail=1; continue
  fi
  git -C "$C" add -A
  git -C "$C" -c user.name='round-74 C1 control' -c user.email='control@example.invalid' \
    commit -q -m "$name: shortcut world on $BASE" || { echo "$name - COMMIT-FAILED"; fail=1; continue; }

  cp "$COUNTER" "$C/_check_spec_craft_ctl.py"
  rm -f "$W/score.stdout.txt" "$W/score.stderr.txt"
  out=$(cd "$C" && python3 -B _check_spec_craft_ctl.py --rev HEAD 2>"$P/$name.err")
  rc=$?
  n=$(printf '%s\n' "$out" | sed -n 's/.*spec craft pages backed \([0-9][0-9]*\) of 3.*/\1/p' | tail -1)
  [ -n "$n" ] || n=-
  printf '%s %s of 3 %s\n' "$name" "$n" "$rc"
  if [ -s "$P/$name.err" ]; then
    printf '%s\n' "$out" > "$W/score.stdout.txt"
    sed 's/^/  stderr: /' "$P/$name.err" > "$W/score.stderr.txt"
  else
    printf '%s\n' "$out" > "$W/score.stdout.txt"
  fi
  [ "$rc" -eq 0 ] || [ "$rc" -eq 1 ] || [ "$rc" -eq 2 ] || fail=1
done

exit $fail
