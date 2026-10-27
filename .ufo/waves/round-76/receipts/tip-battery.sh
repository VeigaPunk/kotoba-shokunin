#!/usr/bin/env bash
# tip-battery.sh — kotoba round-76 no-harm battery runner.
#
# Runs every gate command of the round-76 no-harm battery (plans/round-76.md
# § "No-harm battery"; the base battery is receipted at
# .ufo/waves/round-76/base-battery/base-battery.txt) and prints, for each,
# the command line, its stdout, its stderr (when non-empty) and its exit
# code.  The first line of the output is the measured revision
# (`git rev-parse HEAD` of the measured repository by default, overridable
# with --rev); the second line names the repository that was measured.
#
# Usage:
#   tip-battery.sh [--repo DIR] [--rev REV] [--census-root DIR]
#                  [--census-lane NAME] [--help]
#
#   --repo DIR        lane repository to measure (default: the repository
#                     that holds this script, i.e. four levels above the
#                     receipts directory).
#   --rev REV         revision passed to the --rev gates and printed on the
#                     first line (default: `git rev-parse HEAD` of --repo).
#   --census-root DIR fleet root holding the lane roster
#                     (default: /home/vgpnk/Projects/shokunin).
#   --census-lane     lane id used by the fleet-root census run
#                     (default: kotoba).
#
# Exit status: 0 when every gate exited 0 and SKILL.md is within its
# 600-line budget; 1 otherwise.  The script never mutates the repository it
# measures (read-only git usage only; the census tool is read-only in
# `validate` mode).
#
# Installed by seat B24TipBatteryScript (round 76, wave w1).

set -u

SELF="${BASH_SOURCE[0]}"
HERE=$(cd -- "$(dirname -- "$SELF")" && pwd)

REPO=""
REV=""
CENSUS_ROOT="/home/vgpnk/Projects/shokunin"
CENSUS_LANE="kotoba"
CENSUS_SCRIPT="/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"
SKILL_BUDGET=600

usage() {
    sed -n '2,32p' "$SELF" | sed 's/^# \{0,1\}//'
}

while [ $# -gt 0 ]; do
    case "$1" in
        --repo) REPO="${2:-}"; shift 2 ;;
        --rev) REV="${2:-}"; shift 2 ;;
        --census-root) CENSUS_ROOT="${2:-}"; shift 2 ;;
        --census-lane) CENSUS_LANE="${2:-}"; shift 2 ;;
        -h|--help) usage; exit 0 ;;
        *) echo "tip-battery.sh: unknown argument: $1" >&2; exit 2 ;;
    esac
done

if [ -z "$REPO" ]; then
    # receipts/ -> round-76/ -> waves/ -> .ufo/ -> lane repository root
    REPO=$(cd -- "$HERE/../../../.." && pwd) || exit 2
fi
[ -d "$REPO" ] || { echo "tip-battery.sh: --repo not a directory: $REPO" >&2; exit 2; }
REPO=$(cd -- "$REPO" && pwd)

REPO_HEAD=$(git -C "$REPO" rev-parse HEAD 2>/dev/null) || {
    echo "tip-battery.sh: cannot read HEAD in $REPO" >&2; exit 2; }

if [ -z "$REV" ]; then
    REV="$REPO_HEAD"
fi

cd -- "$REPO" || exit 2

TMP=$(mktemp -d "${TMPDIR:-/tmp}/tip-battery.XXXXXX") || exit 2
trap 'rm -rf -- "$TMP"' EXIT

FAILED=0
TOTAL=0
declare -a SUMMARY=()

run() {
    local label="$1"; shift
    TOTAL=$((TOTAL + 1))
    printf '== %s\n' "$label"
    "$@" >"$TMP/out" 2>"$TMP/err"
    local rc=$?
    cat "$TMP/out"
    if [ -s "$TMP/err" ]; then
        printf -- '-- stderr:\n'
        cat "$TMP/err"
    fi
    printf 'exit=%s\n' "$rc"
    SUMMARY+=("$label	$rc")
    [ "$rc" -eq 0 ] || FAILED=$((FAILED + 1))
    return 0
}

# --- line 1: `git rev-parse HEAD` of the measured repository -----------------
printf '%s\n' "$REPO_HEAD"
printf 'TIP BATTERY — kotoba round 76 no-harm battery\n'
printf 'repo: %s\n' "$REPO"
printf 'repo HEAD: %s\n' "$REPO_HEAD"
printf 'measured rev: %s\n' "$REV"
printf 'census root: %s\n' "$CENSUS_ROOT"
if [ "$REV" != "$REPO_HEAD" ]; then
    printf 'NOTE: measured rev %s differs from the repo HEAD %s; the --rev gates\n' "$REV" "$REPO_HEAD"
    printf 'NOTE: measure the tip revision by running the script at the tip tree without --rev.\n'
fi
printf 'date (UTC): %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
printf -- '----\n'

# --- the no-harm battery ----------------------------------------------------
run "python3 -B verifiers/verify_corpus_integrity.py --json" \
    python3 -B verifiers/verify_corpus_integrity.py --json

run "python3 -B verifiers/verify_corpus_independent.py --json" \
    python3 -B verifiers/verify_corpus_independent.py --json

run "python3 -B verifiers/check_gate_registry.py --rev $REV" \
    python3 -B verifiers/check_gate_registry.py --rev "$REV"

run "python3 -B verifiers/check_assertion_floors.py" \
    python3 -B verifiers/check_assertion_floors.py

run "python3 -B verifiers/verify_skill_checklist.py --json" \
    python3 -B verifiers/verify_skill_checklist.py --json

run "python3 -B verifiers/check_spec_craft.py --rev $REV" \
    python3 -B verifiers/check_spec_craft.py --rev "$REV"

run "python3 -B verifiers/check_sibling_reread.py --rev $REV" \
    python3 -B verifiers/check_sibling_reread.py --rev "$REV"

# Census: the fleet-root lane run (the shape recorded in the plan's base
# battery) when the measured repository is that lane; otherwise the same
# tool in --file mode against the measured repository's registry, so the
# census always reads the tree under test.
LANE_DIR="$CENSUS_ROOT/$CENSUS_LANE-shokunin"
if [ "$REPO" = "$LANE_DIR" ]; then
    run "sources-census.sh validate --root $CENSUS_ROOT $CENSUS_LANE" \
        "$CENSUS_SCRIPT" validate --root "$CENSUS_ROOT" "$CENSUS_LANE"
else
    run "sources-census.sh validate --file $REPO/corpus/SOURCES.md" \
        "$CENSUS_SCRIPT" validate --file "$REPO/corpus/SOURCES.md"
fi

run "wc -l SKILL.md" wc -l SKILL.md

# --- SKILL.md line budget ---------------------------------------------------
SKILL_LINES=$(wc -l < SKILL.md 2>/dev/null | tr -d '[:space:]')
if [ -z "$SKILL_LINES" ]; then
    SKILL_LINES=0
    BUDGET_RC=1
elif [ "$SKILL_LINES" -gt "$SKILL_BUDGET" ]; then
    BUDGET_RC=1
else
    BUDGET_RC=0
fi
TOTAL=$((TOTAL + 1))
printf '== SKILL.md line budget (<= %s)\n' "$SKILL_BUDGET"
printf '%s lines\n' "$SKILL_LINES"
printf 'exit=%s\n' "$BUDGET_RC"
SUMMARY+=("SKILL.md line budget (<= $SKILL_BUDGET)	$BUDGET_RC")
[ "$BUDGET_RC" -eq 0 ] || FAILED=$((FAILED + 1))

# --- summary ----------------------------------------------------------------
printf -- '----\n'
printf '== summary\n'
for row in "${SUMMARY[@]}"; do
    printf '%s\n' "$row"
done
printf 'gates green: %s of %s\n' "$((TOTAL - FAILED))" "$TOTAL"

if [ "$FAILED" -eq 0 ]; then
    printf 'battery: PASS\n'
    exit 0
fi
printf 'battery: FAIL (%s gate(s) red)\n' "$FAILED"
exit 1
