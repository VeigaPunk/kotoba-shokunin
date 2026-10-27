#!/usr/bin/env bash
# E12BatteryScript.battery.sh — kotoba round-77 no-harm battery runner.
#
# Given a lane revision and a receipt path, this script
#   * makes a scratch `git clone --shared` of the lane under
#     /fast/scratch/hyaku/kotoba-r77/E12BatteryScript (removed on exit),
#     as <scratch>/fleet/kotoba-shokunin inside a FLEET-SHAPED sandbox: the
#     directory keeps the lane's name and the other entries of the fleet root
#     are symlinked read-only beside it.  Both are measurement requirements,
#     not conveniences: verify_skill_checklist rejects `name != directory`, and
#     the lane's `../.ufo/...` citations need the fleet beside the lane
#     (round-73 M127; same construction as verifiers/check_tip_battery.py),
#   * checks <rev> out in the CLONE only — the lane's worktree and git index
#     are never touched and no git write happens anywhere except the clone,
#   * runs the round-77 no-harm battery (plans/round-77.md § "No-harm
#     battery") from the clone root, capturing EACH COMMAND'S OWN exit status
#     on its own `exit=N` line — no pipeline is ever on the status path (the
#     round-76 `... | tail` defect that made a red gate read 0),
#   * writes the transcript to <receipt>; line 1 of the receipt is the
#     resolved revision SHA.
#
# Gates run (each with its own `exit=N`):
#   verify_corpus_integrity.py --json
#   verify_corpus_independent.py --json
#   check_gate_registry.py --rev
#   check_assertion_floors.py
#   check_tip_battery.py --rev
#   verify_skill_checklist.py --json
#   check_skill_evals_v2.py --rev
#   check_desc_craft.py --rev                    (round-77 C1, depth)
#   check_r75_routed_repairs.py --rev --work     (round-77 C2, consistency)
#   sources-census.sh validate --root <fleet> <lane>   (FLEET lane path —
#       announces that it measures <fleet>/<lane>-shokunin, NOT the clone)
#   sources-census.sh validate --file <clone>/corpus/SOURCES.md  (the clone)
#   wc -l SKILL.md
#   SKILL.md line budget <= 600 (derived from `wc -l`, recorded as its own
#       exit, never read through a pipe)
#
# Exit status: 0 when every item is green, 1 when any item is red, 2 for a
# usage/environment failure (bad arguments, unknown revision, clone/checkout
# failure, unwritable receipt).  A gate stopped by the per-gate watchdog is
# recorded as `exit=124` and is red.
#
# Nothing is inferred: a gate that cannot run is recorded with the status the
# command actually returned (or 2 for the could-not-evaluate cases the gate
# itself reports).  A gate whose script is not shipped at <rev> is recorded as
# exit=2 with that reason and is NOT run — a missing instrument never reads as
# a red gate reading (check_tip_battery's discipline).
#
# Installed by seat E12BatteryScript (round 77, wave w1).

set -u

SELF="${BASH_SOURCE[0]}"
SELF_DIR=$(cd -- "$(dirname -- "$SELF")" && pwd -P)

REV=""
RECEIPT=""
LANE=""
CENSUS_ROOT="/home/vgpnk/Projects/shokunin"
CENSUS_LANE="kotoba"
CENSUS_SCRIPT=""
SCRATCH_PARENT="/fast/scratch/hyaku/kotoba-r77/E12BatteryScript"
TIMEOUT=900
SKILL_BUDGET=600

usage() {
    cat <<'EOF'
usage: E12BatteryScript.battery.sh --rev <rev> --receipt <path>
                                   [--repo <lane>] [--census-root <dir>]
                                   [--census-lane <name>] [--census-script <path>]
                                   [--scratch-parent <dir>] [--timeout <secs>]

  --rev <rev>            lane revision measured (resolved to a commit SHA)
  --receipt <path>       transcript path; line 1 is the resolved SHA
  --repo <lane>          lane repository (default: nearest ancestor of this
                         script carrying verifiers/ and SKILL.md)
  --census-root <dir>    fleet root for the fleet-shaped census run
                         (default: /home/vgpnk/Projects/shokunin)
  --census-lane <name>   lane id for the fleet-shaped census run (default: kotoba)
  --census-script <p>    sources-census.sh (default: <census-root>/scripts/sources-census.sh)
  --scratch-parent <d>   parent of the scratch sandbox
                         (default: /fast/scratch/hyaku/kotoba-r77/E12BatteryScript)
  --timeout <secs>       per-gate watchdog (default: 900; exit=124 when it fires)

The measured tree is always the scratch clone (named kotoba-shokunin, beside
symlinks to the fleet root's other entries) checked out at <rev>; --repo names
only the source of objects.  The lane is read with git (rev-parse, clone) and
never written.
EOF
}

die() { printf 'battery: %s\n' "$*" >&2; exit 2; }
need_value() { [ "$1" -ge 2 ] || die "option $2 needs a value"; }

while [ $# -gt 0 ]; do
    case "$1" in
        --rev)            need_value $# "$1"; REV="$2"; shift 2 ;;
        --receipt)        need_value $# "$1"; RECEIPT="$2"; shift 2 ;;
        --repo)           need_value $# "$1"; LANE="$2"; shift 2 ;;
        --census-root)    need_value $# "$1"; CENSUS_ROOT="$2"; shift 2 ;;
        --census-lane)    need_value $# "$1"; CENSUS_LANE="$2"; shift 2 ;;
        --census-script)  need_value $# "$1"; CENSUS_SCRIPT="$2"; shift 2 ;;
        --scratch-parent) need_value $# "$1"; SCRATCH_PARENT="$2"; shift 2 ;;
        --timeout)        need_value $# "$1"; TIMEOUT="$2"; shift 2 ;;
        --help|-h)        usage; exit 0 ;;
        *)                printf 'battery: unknown argument: %s\n' "$1" >&2; usage >&2; exit 2 ;;
    esac
done

[ -n "$REV" ] || { usage >&2; die "--rev is required"; }
[ -n "$RECEIPT" ] || { usage >&2; die "--receipt is required"; }
case "$TIMEOUT" in ''|*[!0-9]*) die "--timeout must be a whole number of seconds" ;; esac

find_lane() {
    local d="$1"
    while [ -n "$d" ]; do
        if [ -d "$d/verifiers" ] && [ -f "$d/SKILL.md" ]; then
            printf '%s\n' "$d"
            return 0
        fi
        [ "$d" = "/" ] && return 1
        d=$(dirname -- "$d")
    done
    return 1
}

if [ -z "$LANE" ]; then
    LANE=$(find_lane "$SELF_DIR") || die "cannot find the lane root above $SELF_DIR; pass --repo"
fi
[ -d "$LANE" ] || die "--repo is not a directory: $LANE"
LANE=$(cd -- "$LANE" && pwd -P) || die "cannot resolve --repo: $LANE"
[ -d "$LANE/verifiers" ] && [ -f "$LANE/SKILL.md" ] || die "$LANE is not a lane (no verifiers/ or SKILL.md)"
[ -z "$CENSUS_SCRIPT" ] && CENSUS_SCRIPT="$CENSUS_ROOT/scripts/sources-census.sh"

for tool in git python3 timeout wc sha256sum mktemp basename dirname; do
    command -v "$tool" >/dev/null 2>&1 || die "required tool not on PATH: $tool"
done
[ -f "$CENSUS_SCRIPT" ] || die "census tool not found: $CENSUS_SCRIPT"

# --- the measured revision (resolved in the lane; read-only) -----------------
REV_SHA=$(git -C "$LANE" rev-parse --verify --quiet "$REV^{commit}")
rc=$?
if [ "$rc" -ne 0 ] || [ -z "$REV_SHA" ]; then
    die "--rev $REV is not a commit in $LANE"
fi

# --- scratch fleet-shaped sandbox (trap-removed) -----------------------------
[ -d "$CENSUS_ROOT" ] || die "census root is not a directory: $CENSUS_ROOT"
CENSUS_ROOT=$(cd -- "$CENSUS_ROOT" && pwd -P) || die "cannot resolve the census root"
[ "$CENSUS_ROOT" = "$LANE" ] && die "the census root is the lane itself ($CENSUS_ROOT); a fleet-shaped sandbox cannot be built"
mkdir -p -- "$SCRATCH_PARENT" || die "cannot create $SCRATCH_PARENT"
S=$(mktemp -d "$SCRATCH_PARENT/run.XXXXXX") || die "cannot create a scratch dir under $SCRATCH_PARENT"
cleanup() {
    rm -rf -- "$S"
}
trap cleanup EXIT
trap 'exit 130' INT TERM

SANDBOX="$S/fleet"
mkdir -p -- "$SANDBOX" || die "cannot create the sandbox $SANDBOX"
CLONE="$SANDBOX/kotoba-shokunin"
for entry in "$CENSUS_ROOT"/* "$CENSUS_ROOT"/.[!.]*; do
    [ -e "$entry" ] || continue
    name=$(basename -- "$entry")
    [ "$name" = "kotoba-shokunin" ] && continue
    ln -s -- "$entry" "$SANDBOX/$name" || die "cannot link the fleet entry $name into the sandbox"
done
git clone --shared -q --no-checkout "$LANE" "$CLONE" || die "cannot clone $LANE"
CLONE=$(cd -- "$CLONE" && pwd -P) || die "cannot resolve the clone path"
TOP=$(git -C "$CLONE" rev-parse --show-toplevel 2>/dev/null) || TOP=""
[ "$TOP" = "$CLONE" ] || die "clone toplevel is '$TOP', expected '$CLONE'"
# Identity for any scratch commit a gate may make inside the clone (none is
# expected; the lane itself is never committed to).
git -C "$CLONE" config user.name "scratch-r77" || die "cannot set the clone user.name"
git -C "$CLONE" config user.email "scratch@example.invalid" || die "cannot set the clone user.email"
git -C "$CLONE" checkout -q -f --detach "$REV_SHA" || die "cannot check out $REV_SHA in the clone"
HEAD_SHA=$(git -C "$CLONE" rev-parse HEAD) || die "cannot read the clone HEAD"
[ "$HEAD_SHA" = "$REV_SHA" ] || die "clone HEAD $HEAD_SHA != measured $REV_SHA"

WORK="$S/work"
mkdir -p -- "$WORK" || die "cannot create the work dir $WORK"

# --- receipt ----------------------------------------------------------------
RECEIPT_DIR=$(dirname -- "$RECEIPT")
mkdir -p -- "$RECEIPT_DIR" || die "cannot create the receipt directory $RECEIPT_DIR"
RECEIPT_DIR=$(cd -- "$RECEIPT_DIR" && pwd -P) || die "cannot resolve $RECEIPT_DIR"
RECEIPT="$RECEIPT_DIR/$(basename -- "$RECEIPT")"
: >"$RECEIPT" || die "cannot write the receipt $RECEIPT"

say() { printf '%s\n' "$*" >>"$RECEIPT"; printf '%s\n' "$*"; }
emit() { cat -- "$1" >>"$RECEIPT"; cat -- "$1"; }

render_cmd() {
    local out="" a
    for a in "$@"; do out="$out $(printf '%q' "$a")"; done
    printf '%s\n' "${out# }"
}

SCRIPT_SHA=$(sha256sum -- "$SELF") || SCRIPT_SHA="(unreadable) $SELF"
SCRIPT_SHA=${SCRIPT_SHA%% *}

# line 1: the resolved revision
printf '%s\n' "$REV_SHA" >>"$RECEIPT"
printf '%s\n' "$REV_SHA"
say "BATTERY — kotoba round-77 no-harm battery (clone-scoped; seat E12BatteryScript)"
say "requested rev: $REV"
say "lane (object source, read-only): $LANE"
say "measured tree: $CLONE  (git clone --shared, checked out --detach at $REV_SHA, removed on exit)"
say "fleet-shaped sandbox: $SANDBOX  (the fleet root's other entries are read-only symlinks; the lane's own bytes are the clone)"
if [ -e "$SANDBOX/.ufo" ]; then
    say "sandbox ../ shape: $SANDBOX/.ufo present (lane-relative ../.ufo citations resolve)"
else
    say "sandbox ../ shape: $SANDBOX/.ufo ABSENT (../.ufo citations will read red)"
fi
say "scratch: $S"
say "census: root=$CENSUS_ROOT lane=$CENSUS_LANE script=$CENSUS_SCRIPT"
say "per-gate watchdog: timeout --signal=TERM --kill-after=15 $TIMEOUT (exit=124 when it fires)"
say "runner sha256: $SCRIPT_SHA"
say "date (UTC): $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
say 'status capture: each gate is a simple command, its $? is read on the next'
say 'line and printed as `exit=N` — no pipeline, no subshell on the status path.'
say '----'

TOTAL=0
RED=0
declare -a SUMMARY=()

run() {
    local label="$1"; shift
    local rc
    TOTAL=$((TOTAL + 1))
    say "== $label"
    say "cmd: $(render_cmd "$@")"
    timeout --signal=TERM --kill-after=15 "$TIMEOUT" "$@" >"$S/stdout" 2>"$S/stderr"
    rc=$?                       # the command's OWN status: no pipe, no subshell
    emit "$S/stdout"
    if [ -s "$S/stderr" ]; then
        say "-- stderr:"
        emit "$S/stderr"
    fi
    say "exit=$rc"
    SUMMARY+=("$label"$'\t'"$rc")
    if [ "$rc" -ne 0 ]; then RED=$((RED + 1)); fi
}

verdict() {   # verdict <label> <rc> [detail...]
    local label="$1"; local rc="$2"; shift 2
    TOTAL=$((TOTAL + 1))
    say "== $label"
    if [ $# -gt 0 ]; then say "$*"; fi
    say "exit=$rc"
    SUMMARY+=("$label"$'\t'"$rc")
    if [ "$rc" -ne 0 ]; then RED=$((RED + 1)); fi
}

# A gate whose script is not shipped at the measured revision cannot produce a
# verdict.  Record could-not-evaluate (2) and say why, rather than letting a
# missing file read as a red gate (check_tip_battery's discipline: never report
# a verdict you could not measure).
run_script() {   # run_script <label> <repo-relative script> <command...>
    local label="$1" script_rel="$2"; shift 2
    if git -C "$CLONE" cat-file -e "$REV_SHA:$script_rel" 2>/dev/null; then
        run "$label" "$@"
    else
        verdict "$label" 2 \
            "$script_rel is not present at $REV_SHA; the gate was not run." \
            "cmd: $(render_cmd "$@")"
    fi
}

cd -- "$CLONE" || die "cannot cd into the clone"

# --- the no-harm battery ----------------------------------------------------
run_script "verify_corpus_integrity.py --json" verifiers/verify_corpus_integrity.py \
    python3 -B verifiers/verify_corpus_integrity.py --json --repo "$CLONE"

run_script "verify_corpus_independent.py --json" verifiers/verify_corpus_independent.py \
    python3 -B verifiers/verify_corpus_independent.py --json --repo "$CLONE"

run_script "check_gate_registry.py --rev $REV_SHA" verifiers/check_gate_registry.py \
    python3 -B verifiers/check_gate_registry.py --rev "$REV_SHA"

run_script "check_assertion_floors.py" verifiers/check_assertion_floors.py \
    python3 -B verifiers/check_assertion_floors.py --repo "$CLONE"

run_script "check_tip_battery.py --rev $REV_SHA" verifiers/check_tip_battery.py \
    python3 -B verifiers/check_tip_battery.py --rev "$REV_SHA" \
        --repo "$CLONE" --fleet "$CENSUS_ROOT"

run_script "verify_skill_checklist.py --json" verifiers/verify_skill_checklist.py \
    python3 -B verifiers/verify_skill_checklist.py --json --repo "$CLONE"

run_script "check_skill_evals_v2.py --rev $REV_SHA" verifiers/check_skill_evals_v2.py \
    python3 -B verifiers/check_skill_evals_v2.py --rev "$REV_SHA" \
        --repo "$CLONE" --census "$CENSUS_SCRIPT"

run_script "check_desc_craft.py --rev $REV_SHA (round-77 C1, depth)" verifiers/check_desc_craft.py \
    python3 -B verifiers/check_desc_craft.py --rev "$REV_SHA" --repo "$CLONE"

run_script "check_r75_routed_repairs.py --rev $REV_SHA --work $WORK (round-77 C2, consistency)" verifiers/check_r75_routed_repairs.py \
    python3 -B verifiers/check_r75_routed_repairs.py --rev "$REV_SHA" \
        --repo "$CLONE" --work "$WORK"

say 'NOTE: the fleet-root census form parses the FLEET lane path'
say "NOTE: ($CENSUS_ROOT/$CENSUS_LANE-shokunin), NOT the clone; the --file form below"
say 'NOTE: measures the clone, i.e. the revision under test.  Both statuses are recorded.'

run "sources-census.sh validate --root $CENSUS_ROOT $CENSUS_LANE (fleet lane path)" \
    bash "$CENSUS_SCRIPT" validate --root "$CENSUS_ROOT" "$CENSUS_LANE"

run "sources-census.sh validate --file $CLONE/corpus/SOURCES.md (measured revision)" \
    bash "$CENSUS_SCRIPT" validate --file "$CLONE/corpus/SOURCES.md"

run "wc -l SKILL.md" wc -l SKILL.md

# --- SKILL.md line budget (derived; wc's own status read without a pipe) -----
SKILL_LINES=$(wc -l <SKILL.md)
WC_RC=$?
if [ "$WC_RC" -ne 0 ] || [ -z "$SKILL_LINES" ]; then
    BUDGET_RC=2
    BUDGET_NOTE="could not read SKILL.md (wc -l status $WC_RC)"
elif [ "$SKILL_LINES" -gt "$SKILL_BUDGET" ]; then
    BUDGET_RC=1
    BUDGET_NOTE="$SKILL_LINES lines, over the $SKILL_BUDGET-line budget (wc -l status $WC_RC)"
else
    BUDGET_RC=0
    BUDGET_NOTE="$SKILL_LINES lines, within the $SKILL_BUDGET-line budget (wc -l status $WC_RC)"
fi
verdict "SKILL.md line budget <= $SKILL_BUDGET (derived from wc -l)" "$BUDGET_RC" "$BUDGET_NOTE"

# --- summary ----------------------------------------------------------------
say '----'
say '== summary'
for entry in "${SUMMARY[@]}"; do say "$entry"; done
say "gates green: $((TOTAL - RED)) of $TOTAL"
say "receipt: $RECEIPT"

if [ "$RED" -eq 0 ]; then
    say 'battery: PASS'
    exit 0
fi
say "battery: FAIL ($RED of $TOTAL red)"
exit 1
