#!/usr/bin/env bash
# c1-killpin-rev (round 93, claim C1, frozen counting command; plans/round-93.md § C1).
# Usage: bash verifiers/fixtures/round-93/c1-killpin-rev.sh [REV] [REPO]
#   REV  full commit to measure (default: the tip of branch master of REPO)
#   REPO repository to clone REV from (default: this lane; a scratch repo for the forgery control)
# Builds three COMMITTED worlds from REV in its own scratch clone (identity scratch@invalid) and runs
# the public mutation battery `verifiers/check_mutation_battery.py --rev <world rev> --work <dir>`
# from that clone's working tree (REV's own checker bytes):
#   drop   : the first `kill` row of verifiers/fixtures/mutation-battery/manifest.tsv removed
#            -> conjunct holds iff rc == 2 AND the output names `kill-set-size`
#   other  : kill rows untouched; the fg-fixed-plan probe fixture emptied (a non-kill-set baseline
#            failure) -> conjunct holds iff rc == 2 AND the output does NOT name `kill-set-size`
#   honest : REV itself, unmodified -> conjunct holds iff rc == 0 AND the output does NOT name
#            `kill-set-size`
# Predicate (frozen): C1-PREDICATE-MET iff all three conjuncts hold. Exit 0 met, 1 unmet,
# 2 could-not-evaluate (scratch, clone or commit failure). Stdout: one line per world, then the
# predicate label. Scratch under ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r93/c1-killpin, removed
# on exit.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
REPO="${2:-$LANE}"
REV="$(git -C "$REPO" rev-parse --verify -q "${1:-$(git -C "$REPO" rev-parse master)}^{commit}")" \
  || { echo "C1-NOT-EVALUATED: REV is not a commit of $REPO"; exit 2; }
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r93/c1-killpin"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/run.XXXX")" || { echo "C1-NOT-EVALUATED: scratch unavailable"; exit 2; }
trap 'rm -rf -- "$W"' EXIT
export TMPDIR="$W"
echo "rev $REV repo $REPO"

S="$W/world/kotoba-shokunin"
mkdir -p "$W/world"
git clone -q --shared "$REPO" "$S" && git -C "$S" checkout -q "$REV" \
  || { echo "C1-NOT-EVALUATED: clone or checkout failed"; exit 2; }
[ "$(git -C "$S" rev-parse --show-toplevel)" = "$S" ] || { echo "C1-NOT-EVALUATED: clone toplevel mismatch"; exit 2; }
MAN=verifiers/fixtures/mutation-battery/manifest.tsv

world_commit() {  # message -> prints world rev
  git -C "$S" add -A -- verifiers/ >/dev/null && \
  git -C "$S" -c user.name=scratch -c user.email=scratch@invalid commit -q -m "$1" >/dev/null && \
  git -C "$S" rev-parse HEAD
}

battery() {  # rev label -> sets RC, OUT
  OUT="$(cd "$S" && python3 -B verifiers/check_mutation_battery.py --rev "$1" --work "$W/bat-$2" 2>&1)"; RC=$?
}

named() { printf '%s\n' "$OUT" | grep -q 'kill-set-size' && echo yes || echo no; }

# honest world first (REV unmodified)
battery "$REV" honest; H_RC=$RC; H_N=$(named)
printf '%s\n' "$OUT" | tail -1 | sed 's/^/  honest last: /'

# drop world
python3 -B - "$S/$MAN" <<'PY' || { echo "C1-NOT-EVALUATED: drop edit failed"; exit 2; }
import pathlib, sys
p = pathlib.Path(sys.argv[1]); lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
for i, ln in enumerate(lines[1:], 1):
    f = ln.rstrip("\n").split("\t")
    if len(f) >= 3 and f[2] == "kill":
        del lines[i]; break
else:
    raise SystemExit(1)
p.write_text("".join(lines), encoding="utf-8")
PY
DREV="$(world_commit "round-93 c1 drop world (scratch, not a lane commit)")" || { echo "C1-NOT-EVALUATED: drop commit failed"; exit 2; }
battery "$DREV" drop; D_RC=$RC; D_N=$(named)
printf '%s\n' "$OUT" | tail -1 | sed 's/^/  drop last: /'

# other world (from the drop world's parent: restore manifest, empty the fg-fixed-plan fixture)
git -C "$S" checkout -q "$REV" || { echo "C1-NOT-EVALUATED: reset to REV failed"; exit 2; }
: > "$S/verifiers/fixtures/freeze-gate/r88-controls-fixed.md"
OREV="$(world_commit "round-93 c1 other-baseline world (scratch, not a lane commit)")" || { echo "C1-NOT-EVALUATED: other commit failed"; exit 2; }
battery "$OREV" other; O_RC=$RC; O_N=$(named)
printf '%s\n' "$OUT" | tail -1 | sed 's/^/  other last: /'

d_ok=no; o_ok=no; h_ok=no
[ "$D_RC" = 2 ] && [ "$D_N" = yes ] && d_ok=yes
[ "$O_RC" = 2 ] && [ "$O_N" = no ] && o_ok=yes
[ "$H_RC" = 0 ] && [ "$H_N" = no ] && h_ok=yes
echo "drop world $DREV rc $D_RC names kill-set-size $D_N: $d_ok"
echo "other world $OREV rc $O_RC names kill-set-size $O_N: $o_ok"
echo "honest world $REV rc $H_RC names kill-set-size $H_N: $h_ok"
if [ "$d_ok$o_ok$h_ok" = yesyesyes ]; then echo "C1-PREDICATE-MET"; exit 0; fi
echo "C1-PREDICATE-UNMET"; exit 1
