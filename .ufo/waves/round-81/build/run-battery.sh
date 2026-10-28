#!/usr/bin/env bash
# run-battery.sh -- kotoba round-81 no-harm battery runner (plans/round-81.md
# § No-harm battery, § C1).  Ported from round-80 by seat Kb81E10Battery.
#
# usage: run-battery.sh <rev> <repo> <out-dir> [<report-path>]
#
#   <rev>          revision to measure (resolved to a full commit hash first)
#   <repo>         the git repository that holds <rev>.  This may be the real
#                  lane (/home/vgpnk/Projects/shokunin/kotoba-shokunin) or a
#                  scratch world clone -- the runner clones it into a
#                  fleet-shaped world of its own and measures there, so a
#                  world commit that exists only in a clone is measurable.
#   <out-dir>      directory that receives one receipt per command
#   <report-path>  optional: also run check_report_pointers.py on this report
#                  (the plan's battery names it; a report is not revision-bound)
#
# environment:
#   HYAKU_FLEET    fleet root (default: the parent directory of <repo>).  The
#                  counter derives its fleet root from --repo's parent, so when
#                  <repo> is a scratch clone the runner passes --fleet
#                  explicitly to keep the measured world fleet-shaped.
#   HYAKU_SCRATCH  seat scratch root (default: /fast/scratch/hyaku/kotoba-r81/
#                  Kb81E10Battery); each run uses $HYAKU_SCRATCH/battery/ and is
#                  removed on exit.  TMPDIR is exported inside it.
#   HYAKU_TIMEOUT  per-command timeout in seconds (default: 900 for the tip
#                  battery forms, 600 for the gates; a timeout is receipted as
#                  exit=124, never as green).
#
# Writes <out-dir>/NN-<name>.txt, one file per command, each of them:
#   line 1   # rev=<full hash> cmd=<the command> utc=<ISO-8601 Z>
#   line 2   # cwd=<the directory the command ran in>
#   line 3+  optional # note=<why this command is shaped this way>
#   body     the command's own stdout+stderr, byte for byte
#   last     exit=<the command's own status>
#
# Exit status of a command is captured from the command itself:
#       cmd >> f 2>&1; rc=$?; printf 'exit=%s\n' "$rc" >> f
# never from a downstream pipeline.  A pipeline reports its last element's
# status (round-80 lesson M80-1): `cmd | tail; echo $?` reports tail's status
# and hides the verdict.  The two awk|wc figures below therefore run without a
# pipeline (the awk writes its figure to a temp file which is then counted).
#
# Exit status of the runner: 0 every command exited 0 · 1 at least one command
# exited != 0 (a red battery is a reading, not a runner failure) · 2
# usage/environment error (unresolvable rev, unclonable repo, scratch toplevel
# mismatch, a required gate absent at <rev>).
#
# Stdlib only: bash, git, python3, coreutils (date, wc, awk, mktemp, rm).
# Concurrency: the commands run one at a time; each counter spawns its own
# children, so the runner never holds more than one battery process.
set -u

PROG=${0##*/}

usage() {
  sed -n '2,46p' "$0"
}

die() {
  printf '%s: %s\n' "$PROG" "$*" >&2
  exit 2
}

utc() {
  date -u +%Y-%m-%dT%H:%M:%SZ
}

q() {  # shell-quote one argument for a `bash -c` command string
  printf '%q' "$1"
}

if [ $# -lt 3 ] || [ $# -gt 4 ]; then
  usage >&2
  exit 2
fi
REV_IN=$1
REPO_IN=$2
OUT_IN=$3
REPORT=${4:-}

[ -d "$REPO_IN" ] || die "repo is not a directory: $REPO_IN"
REPO=$(cd "$REPO_IN" && pwd -P) || die "cannot enter repo: $REPO_IN"
TOP=$(git -C "$REPO" rev-parse --show-toplevel 2>/dev/null) \
  || die "not a git repository: $REPO"
[ "$TOP" = "$REPO" ] || die "repo $REPO is not its own git toplevel ($TOP)"
FULL=$(git -C "$REPO" rev-parse --verify --quiet "${REV_IN}^{commit}" 2>/dev/null) \
  || die "cannot resolve ${REV_IN} in $REPO"
[ -n "$FULL" ] || die "empty resolution for ${REV_IN} in $REPO"

mkdir -p "$OUT_IN" || die "cannot create out-dir: $OUT_IN"
OUT=$(cd "$OUT_IN" && pwd -P) || die "cannot enter out-dir: $OUT_IN"

FLEET=${HYAKU_FLEET:-$(dirname "$REPO")}
[ -d "$FLEET" ] || die "fleet root not found: $FLEET"
FLEET=$(cd "$FLEET" && pwd -P) || die "cannot enter fleet root: $FLEET"

SCRATCH_ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotoba-r81/Kb81E10Battery}/battery"
S="$SCRATCH_ROOT/run-$$-$RANDOM"
mkdir -p "$S/tmp" || die "cannot create scratch dir: $S"
export TMPDIR="$S/tmp"
cleanup() { rm -rf -- "$S"; }
trap cleanup EXIT
trap 'exit 129' HUP INT TERM

# --- the fleet-shaped world -------------------------------------------
# The gates resolve `../.ufo/...` and `../scripts/...` from the repo root, so
# a bare clone measures a different world than a fleet-shaped one (round-79
# finding F1: verify_skill_checklist.py --self-test reads 2 failures in a bare
# clone and 1 fleet-shaped at the same rev).  The world is therefore
# <S>/world/<lane directory name> with every other fleet entry symlinked beside
# it.  The world clone is named after the LANE, never after the scratch repo's
# own directory name: verify_skill_checklist.py's `trigger.name_directory`
# check reads SKILL.md's `name:` against the repo's own directory, so a world
# cloned as "clone" reads "name 'kotoba-shokunin' != directory 'clone'" and
# reddens a gate the tip battery measures green (the counter's own sandbox
# always names its clone `kotoba-shokunin`).
WORLD="$S/world"
mkdir -p "$WORLD" || die "cannot create world dir: $WORLD"
LANE_NAME=$(sed -n 's/^name:[[:space:]]*//p' "$REPO/SKILL.md" 2>/dev/null | head -n 1)
case "$LANE_NAME" in
  ""|*[!A-Za-z0-9._-]*) LANE_NAME=$(basename "$REPO") ;;
esac
CLONE="$WORLD/$LANE_NAME"
git clone -q --shared "$REPO" "$CLONE" >"$S/clone.log" 2>&1 \
  || die "git clone failed: $(tail -n 3 "$S/clone.log" | tr '\n' ' ')"
CLONE_TOP=$(git -C "$CLONE" rev-parse --show-toplevel 2>/dev/null)
[ "$CLONE_TOP" = "$CLONE" ] || die "scratch clone toplevel $CLONE_TOP is not $CLONE"
git -C "$CLONE" checkout -q --detach "$FULL" >"$S/checkout.log" 2>&1 \
  || die "cannot check out $FULL in the scratch clone: $(tail -n 3 "$S/checkout.log" | tr '\n' ' ')"
HEAD_NOW=$(git -C "$CLONE" rev-parse HEAD)
[ "$HEAD_NOW" = "$FULL" ] || die "scratch clone HEAD $HEAD_NOW is not $FULL"
for entry in "$FLEET"/* "$FLEET"/.[!.]*; do
  [ -e "$entry" ] || continue
  name=$(basename "$entry")
  [ "$name" = "$LANE_NAME" ] && continue
  ln -s "$entry" "$WORLD/$name" 2>/dev/null || true
done

# --- environment check ------------------------------------------------
for tool in git python3 awk wc date mktemp; do
  command -v "$tool" >/dev/null 2>&1 || die "required tool missing: $tool"
done
for gate in check_gate_registry.py check_assertion_floors.py verify_skill_checklist.py \
            verify_corpus_integrity.py verify_corpus_independent.py check_correction_sweep.py; do
  [ -f "$CLONE/verifiers/$gate" ] || die "$gate absent at $FULL"
done
[ -f "$CLONE/verifiers/check_tip_battery.py" ] \
  || die "check_tip_battery.py absent at $FULL"
CENSUS=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
[ -x "$CENSUS" ] || die "census script not executable: $CENSUS"

T_TIP=${HYAKU_TIMEOUT_TIP:-900}
T_GATE=${HYAKU_TIMEOUT_GATE:-600}

# --- receipt writer ---------------------------------------------------
RECEIPT_NAMES=()
RECEIPT_EXITS=()
RUN_FAIL=0

run_receipt() {  # run_receipt <file> <cwd> <timeout-s> <note> <cmd>
  local f="$OUT/$1" cwd="$2" tmo="$3" note="$4" cmd="$5" rc=0
  {
    printf '# rev=%s cmd=%s utc=%s\n' "$FULL" "$cmd" "$(utc)"
    printf '# cwd=%s\n' "$cwd"
    printf '# timeout=%ss shell=bash\n' "$tmo"
    [ -n "$note" ] && printf '# note=%s\n' "$note"
  } >"$f" || die "cannot write receipt header: $f"
  ( cd "$cwd" && exec timeout "$tmo" bash -c "$cmd" ) >>"$f" 2>&1
  rc=$?
  printf 'exit=%s\n' "$rc" >>"$f"
  RECEIPT_NAMES+=("$1")
  RECEIPT_EXITS+=("$rc")
  if [ "$rc" -ne 0 ]; then
    RUN_FAIL=1
  fi
  printf '%s: %s exit=%s\n' "$PROG" "$1" "$rc"
  return 0
}

figure_of() {  # the last non-comment, non-exit body line of a receipt
  grep -v -e '^#' -e '^exit=' "$1" 2>/dev/null | tail -n 1
}

IDX="$OUT/index.txt"
{
  printf 'runner=%s\n' "$PROG"
  printf 'rev=%s\n' "$FULL"
  printf 'repo=%s\n' "$REPO"
  printf 'fleet=%s\n' "$FLEET"
  printf 'world=%s\n' "$CLONE"
  printf 'utc=%s\n' "$(utc)"
  printf 'python=%s\n' "$(python3 -V 2>&1)"
  printf 'git=%s\n' "$(git --version 2>&1)"
} >"$IDX" || die "cannot write index: $IDX"

TIP_NOTE="form 1 of the plan's --repo . run from the world lane root; --fleet passed explicitly so a scratch world stays fleet-shaped"
TIP_NOTE2="form 2 of the plan's absolute --repo <lane> form"
GATE_NOTE="fleet-shaped scratch world checked out at \$rev"
CENSUS_NOTE="census reads the LIVE lane tree (--root is the fleet root), not \$rev"

# 01/02 -- the claim's own counter, both forms (plan C1 frozen predicate)
run_receipt 01-tip-battery-dot.txt "$CLONE" "$T_TIP" "$TIP_NOTE" \
  "python3 -B verifiers/check_tip_battery.py --rev $(q "$FULL") --repo . --fleet $(q "$FLEET")"
run_receipt 02-tip-battery-abs.txt "$CLONE" "$T_TIP" "$TIP_NOTE2" \
  "python3 -B verifiers/check_tip_battery.py --rev $(q "$FULL") --repo $(q "$CLONE") --fleet $(q "$FLEET")"

# 03..08 -- the six gates of the frozen battery, in the world at <rev>
run_receipt 03-gate-registry.txt "$CLONE" "$T_GATE" "$GATE_NOTE" \
  "python3 -B verifiers/check_gate_registry.py --rev $(q "$FULL")"
run_receipt 04-assertion-floors.txt "$CLONE" "$T_GATE" "runs the instrument self-tests (~100 s)" \
  "python3 -B verifiers/check_assertion_floors.py"
run_receipt 05-skill-checklist.txt "$CLONE" "$T_GATE" "$GATE_NOTE" \
  "python3 -B verifiers/verify_skill_checklist.py --json"
run_receipt 06-corpus-integrity.txt "$CLONE" "$T_GATE" "$GATE_NOTE" \
  "python3 -B verifiers/verify_corpus_integrity.py --json"
run_receipt 07-corpus-independent.txt "$CLONE" "$T_GATE" "$GATE_NOTE" \
  "python3 -B verifiers/verify_corpus_independent.py --json"
run_receipt 08-correction-sweep.txt "$CLONE" "$T_GATE" "same argv as the frozen battery's sixth gate" \
  "python3 -B verifiers/check_correction_sweep.py --root ."

# 09 -- fleet census (live lane tree, per its own flags)
run_receipt 09-census.txt /home/vgpnk/Projects/shokunin "$T_GATE" "$CENSUS_NOTE" \
  "$(q "$CENSUS") validate --root /home/vgpnk/Projects/shokunin kotoba"

# 10..14 -- SKILL.md size figures at <rev> (no pipeline: awk writes, wc counts)
for spec in "10-skill-lines:wc -l SKILL.md" \
            "11-skill-bytes:wc -c SKILL.md"; do
  name=${spec%%:*}; cmd=${spec#*:}
  run_receipt "$name.txt" "$CLONE" 120 "SKILL.md figure at \$rev" "$cmd"
done
run_receipt 12-skill-long120.txt "$CLONE" 120 "lines longer than 120 characters" \
  "awk 'length > 120' SKILL.md > \"\$TMPDIR/l120\" && wc -l < \"\$TMPDIR/l120\""
run_receipt 13-skill-long300.txt "$CLONE" 120 "lines longer than 300 characters" \
  "awk 'length > 300' SKILL.md > \"\$TMPDIR/l300\" && wc -l < \"\$TMPDIR/l300\""
run_receipt 14-skill-longest.txt "$CLONE" 120 "longest line length and its line number" \
  "awk '{ if (length > m) { m = length; n = NR } } END { printf \"longest=%d line=%d\\n\", m, n }' SKILL.md"

# 15 -- optional report pointers (the plan's battery names it; not revision-bound)
if [ -n "$REPORT" ]; then
  run_receipt 15-report-pointers.txt "$CLONE" "$T_GATE" \
    "report pointer gate on the named report (not revision-bound)" \
    "python3 -B verifiers/check_report_pointers.py --report $(q "$REPORT") --repo $(q "$CLONE") --rev $(q "$FULL")"
fi

# --- index and figures ------------------------------------------------
i=0
while [ "$i" -lt "${#RECEIPT_NAMES[@]}" ]; do
  printf '%s\texit=%s\t%s\n' \
    "${RECEIPT_NAMES[$i]}" "${RECEIPT_EXITS[$i]}" \
    "$(figure_of "$OUT/${RECEIPT_NAMES[$i]}")" >>"$IDX"
  i=$((i + 1))
done
green=0
i=0
while [ "$i" -lt "${#RECEIPT_EXITS[@]}" ]; do
  [ "${RECEIPT_EXITS[$i]}" -eq 0 ] && green=$((green + 1))
  i=$((i + 1))
done
{
  printf 'receipts=%s green=%s non-zero=%s\n' \
    "${#RECEIPT_NAMES[@]}" "$green" "$((${#RECEIPT_EXITS[@]} - green))"
} >>"$IDX"

printf '%s: rev %s; %d receipt(s), %d exit 0, %d non-zero; receipts in %s\n' \
  "$PROG" "$FULL" "${#RECEIPT_NAMES[@]}" "$green" \
  "$((${#RECEIPT_EXITS[@]} - green))" "$OUT"
for f in 01-tip-battery-dot.txt 02-tip-battery-abs.txt; do
  [ -f "$OUT/$f" ] && printf '%s: %s\n' "$f" "$(figure_of "$OUT/$f")"
done
exit "$RUN_FAIL"
