#!/usr/bin/env bash
# run-battery.sh — kotoba round-79 no-harm battery runner (plans/round-79.md
# § No-harm battery), revision-bound.  Written by seat Kb79E07BatteryRunner.
#
# usage: run-battery.sh <rev> <lane-repo> <out-dir> [<report-path>]
#
#   <rev>          revision to measure (resolved to a full commit hash first)
#   <lane-repo>    the kotoba lane working tree that holds <rev>.  Only the two
#                  check_tip_battery.py forms run from here: that counter builds
#                  its own fleet-shaped sandbox from --repo/--fleet, so it needs
#                  the real lane, not a clone.  Every other gate that reads the
#                  tree runs in a fleet-shaped scratch clone checked out at <rev>
#                  (see Scratch below) -- the same construction the counter uses
#   <out-dir>      directory that receives one receipt per command
#   <report-path>  optional: also run check_report_pointers.py on this report
#                  (the plan's battery names it; a report is not revision-bound)
#
# Writes <out-dir>/NN-<name>.txt, one file per command, each of them:
#   line 1   # rev=<full hash> cmd=<the command> utc=<ISO-8601 Z>
#   line 2   # cwd=<the directory the command ran in>
#   line 3   # timeout=<n>s shell=bash-o-pipefail wall=<n>s
#   line 4+  optional # note=<why this command is shaped this way>
#   body     the command's own stdout+stderr, byte for byte
#   last     exit=<the command's own status>   (`cmd >> f 2>&1; rc=$?`)
# plus <out-dir>/index.txt: run provenance (rev, lane, fleet, python3, git, utc),
# a name<TAB>exit index and the frozen tip-battery lines + SKILL.md figures
# extracted from the receipts, so the battery is readable from one file.
#
# Exit status: 0 every command exited 0 · 1 at least one command exited != 0
# (a red battery is a reading, not a runner failure) · 2 usage/environment
# error (unresolvable rev, unclonable lane, scratch clone toplevel mismatch).
# A timeout is receipted as exit=124 (coreutils timeout), never as green.
#
# Scratch: $HYAKU_SCRATCH/kotoba-r79-battery/run-<pid>-<rand> (default
# $HYAKU_SCRATCH=/fast/scratch/hyaku), TMPDIR inside it, removed on exit.  The
# clone lives at <scratch>/world/<lane basename> and every other entry of the
# lane's fleet root is symlinked beside it (read-only), because the gates
# resolve ../.ufo/... and ../scripts/... from the repo root: a bare clone
# measures a different world (verify_skill_checklist.py --self-test reads 2
# failures bare against 1 fleet-shaped at the same rev).
# Read-only on the lane: no git write happens outside that scratch dir.
# Stdlib tools only: bash, git, python3, coreutils (timeout, wc, awk, date).
# Concurrency: the commands run one at a time; each counter spawns its own
# children, so the runner itself never holds more than one battery process.
set -u
set -o pipefail

PROG=${0##*/}

usage() {
  sed -n '2,42p' "$0"
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
LANE_IN=$2
OUT_IN=$3
REPORT=${4:-}

[ -d "$LANE_IN" ] || die "lane repo is not a directory: $LANE_IN"
LANE=$(cd "$LANE_IN" && pwd -P) || die "cannot enter lane repo: $LANE_IN"
TOP=$(git -C "$LANE" rev-parse --show-toplevel 2>/dev/null) \
  || die "not a git repository: $LANE"
[ "$TOP" = "$LANE" ] || die "lane repo $LANE is not its own git toplevel ($TOP)"
FULL=$(git -C "$LANE" rev-parse --verify --quiet "${REV_IN}^{commit}" 2>/dev/null) \
  || die "cannot resolve ${REV_IN} in $LANE"
[ -n "$FULL" ] || die "empty resolution for ${REV_IN} in $LANE"

mkdir -p "$OUT_IN" || die "cannot create out-dir: $OUT_IN"
OUT=$(cd "$OUT_IN" && pwd -P) || die "cannot enter out-dir: $OUT_IN"

SCRATCH_ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r79-battery"
S="$SCRATCH_ROOT/run-$$-$RANDOM"
mkdir -p "$S/tmp" || die "cannot create scratch dir: $S"
export TMPDIR="$S/tmp"
cleanup() { rm -rf -- "$S"; }
trap cleanup EXIT
trap 'exit 129' HUP INT TERM

FLEET=$(dirname "$LANE")
[ -d "$FLEET" ] || die "cannot find the fleet root beside the lane: $FLEET"
CLONE_PARENT="$S/world"
CLONE="$CLONE_PARENT/$(basename "$LANE")"
mkdir -p "$CLONE_PARENT" || die "cannot create scratch world: $CLONE_PARENT"
git clone -q --shared "$LANE" "$CLONE" >"$S/clone.log" 2>&1 \
  || die "git clone failed: $(tail -n 3 "$S/clone.log" | tr '\n' ' ')"
CLONE_TOP=$(git -C "$CLONE" rev-parse --show-toplevel 2>/dev/null)
[ "$CLONE_TOP" = "$CLONE" ] || die "scratch clone toplevel $CLONE_TOP is not $CLONE"
git -C "$CLONE" checkout -q --detach "$FULL" >"$S/checkout.log" 2>&1 \
  || die "cannot check out $FULL in the scratch clone: $(tail -n 3 "$S/checkout.log" | tr '\n' ' ')"
HEAD_NOW=$(git -C "$CLONE" rev-parse HEAD)
[ "$HEAD_NOW" = "$FULL" ] || die "scratch clone HEAD $HEAD_NOW is not $FULL"
# fleet-shape the clone (same construction as check_tip_battery.build_sandbox): the
# gates resolve `../.ufo/...` and `../scripts/...` from the repo root, so a bare clone
# measures a different world -- verify_skill_checklist.py --self-test reads 2 failures
# bare and 1 fleet-shaped at the same rev (receipts .ufo/waves/round-79/build/
# selftest-bare-*.log; probe 2026-10-27).  Symlinks only; nothing is written through.
for entry in "$FLEET"/* "$FLEET"/.[!.]*; do
  [ -e "$entry" ] || continue
  base=${entry##*/}
  [ "$base" = "${LANE##*/}" ] && continue
  ln -s "$entry" "$CLONE_PARENT/$base" 2>/dev/null || true
done

# --- environment check ------------------------------------------------
for tool in git python3 awk wc date; do
  command -v "$tool" >/dev/null 2>&1 || die "required tool missing: $tool"
done
for gate in check_gate_registry.py check_assertion_floors.py verify_skill_checklist.py \
            verify_corpus_integrity.py verify_corpus_independent.py check_correction_sweep.py; do
  [ -f "$CLONE/verifiers/$gate" ] || die "$gate absent at $FULL"
done
[ -f "$LANE/verifiers/check_tip_battery.py" ] || die "check_tip_battery.py absent in $LANE"
CENSUS=/home/vgpnk/Projects/shokunin/scripts/sources-census.sh
[ -x "$CENSUS" ] || die "census script not executable: $CENSUS"

# --- receipt writer ---------------------------------------------------
RECEIPT_NAMES=()
RECEIPT_EXITS=()
RUN_FAIL=0

run_receipt() {  # run_receipt <file> <cwd> <timeout-s> <note> <cmd>
  local name=$1 cwd=$2 tmo=$3 note=$4 cmd=$5
  local dest="$OUT/$name" body="$S/body.$name" rc t0 t1
  t0=$(date +%s)
  printf '%s: %s\n' "$PROG" "$name" >&2
  if command -v timeout >/dev/null 2>&1; then
    ( cd "$cwd" || exit 111
      exec timeout -k 5 "${tmo}s" bash -o pipefail -c "$cmd"
    ) >"$body" 2>&1
  else
    ( cd "$cwd" || exit 111
      exec bash -o pipefail -c "$cmd"
    ) >"$body" 2>&1
  fi
  rc=$?
  t1=$(date +%s)
  {
    printf '# rev=%s cmd=%s utc=%s\n' "$FULL" "$cmd" "$(utc)"
    printf '# cwd=%s\n' "$cwd"
    printf '# timeout=%ss shell=bash-o-pipefail wall=%ss\n' "$tmo" "$((t1 - t0))"
    [ -n "$note" ] && printf '# note=%s\n' "$note"
    cat "$body"
    # the body may lack a trailing newline: never glue exit= onto its last line
    if [ -s "$body" ] && [ -n "$(tail -c 1 "$body")" ]; then
      printf '\n'
    fi
    printf 'exit=%s\n' "$rc"
  } >"$dest" || die "cannot write receipt: $dest"
  rm -f -- "$body"
  RECEIPT_NAMES+=("$name")
  RECEIPT_EXITS+=("$rc")
  [ "$rc" -eq 0 ] || RUN_FAIL=1
  if [ "$rc" -eq 124 ]; then
    printf '%s: %s hit the %ss timeout\n' "$PROG" "$name" "$tmo" >&2
  fi
}

figure_of() {  # the first body line of a receipt (no header, no exit line)
  grep -v -e '^#' -e '^exit=' "$1" 2>/dev/null | head -n 1
}

IDX="$OUT/index.txt"
{
  printf '# run-battery.sh round-79 no-harm battery\n'
  printf '# rev=%s\n' "$FULL"
  printf '# lane=%s\n' "$LANE"
  printf '# fleet=%s\n' "$FLEET"
  printf '# clone=%s (fleet-shaped: fleet entries symlinked beside it)\n' "$CLONE"
  printf '# out=%s\n' "$OUT"
  printf '# scratch=%s (removed on exit)\n' "$S"
  printf '# started=%s\n' "$(utc)"
  printf '# python3=%s\n' "$(python3 --version 2>&1)"
  printf '# git=%s\n' "$(git --version 2>&1)"
  printf '# base=%s\n' "b10bcbc6b00f8f56b202ccbadca311007b5b463c"
} >"$IDX" || die "cannot write index: $IDX"

TIP_NOTE="check_tip_battery.py builds its own fleet-shaped sandbox from --repo/--fleet; form 1 is the plan's --repo . run from the lane root"
TIP_NOTE2="form 2 of the same counter with the absolute lane path"
CENSUS_NOTE="census reads the LIVE lane tree (--root is the fleet root), not \$rev; it is the fleet census step of the plan's battery"

# 01/02 — the claim's own counter, both forms (plan form 1 and form 2)
run_receipt 01-tip-battery-dot.txt "$LANE" 900 "$TIP_NOTE" \
  "python3 -B verifiers/check_tip_battery.py --rev $(q "$FULL") --repo ."
run_receipt 02-tip-battery-abs.txt "$LANE" 900 "$TIP_NOTE2" \
  "python3 -B verifiers/check_tip_battery.py --rev $(q "$FULL") --repo $(q "$LANE")"

# 03..08 — the six gates of the frozen battery, in the scratch clone at <rev>
run_receipt 03-gate-registry.txt "$CLONE" 600 "fleet-shaped scratch clone checked out at \$rev" \
  "python3 -B verifiers/check_gate_registry.py --rev $(q "$FULL")"
run_receipt 04-assertion-floors.txt "$CLONE" 600 "runs the instrument self-tests (~100 s)" \
  "python3 -B verifiers/check_assertion_floors.py"
run_receipt 05-skill-checklist.txt "$CLONE" 600 "fleet-shaped scratch clone checked out at \$rev" \
  "python3 -B verifiers/verify_skill_checklist.py --json"
run_receipt 06-corpus-integrity.txt "$CLONE" 600 "fleet-shaped scratch clone checked out at \$rev" \
  "python3 -B verifiers/verify_corpus_integrity.py --json"
run_receipt 07-corpus-independent.txt "$CLONE" 600 "fleet-shaped scratch clone checked out at \$rev" \
  "python3 -B verifiers/verify_corpus_independent.py --json"
run_receipt 08-correction-sweep.txt "$CLONE" 600 "same argv as the frozen battery's sixth gate" \
  "python3 -B verifiers/check_correction_sweep.py --root ."

# 09 — fleet census (live lane tree, per its own flags)
run_receipt 09-census.txt /home/vgpnk/Projects/shokunin 600 "$CENSUS_NOTE" \
  "$(q "$CENSUS") validate --root /home/vgpnk/Projects/shokunin kotoba"

# 10..14 — SKILL.md size figures (considerthese 2026-10-26 proposal 1), at <rev>
run_receipt 10-skill-lines.txt "$CLONE" 120 "plan ceiling: <= 600 lines (590 at the r79 base)" \
  "wc -l SKILL.md"
run_receipt 11-skill-bytes.txt "$CLONE" 120 "byte ceiling figure (not claimed this round)" \
  "wc -c SKILL.md"
run_receipt 12-skill-long120.txt "$CLONE" 120 "lines longer than 120 characters" \
  "awk 'length > 120' SKILL.md | wc -l"
run_receipt 13-skill-long300.txt "$CLONE" 120 "lines longer than 300 characters" \
  "awk 'length > 300' SKILL.md | wc -l"
run_receipt 14-skill-longest.txt "$CLONE" 120 "longest line length and its line number" \
  "awk '{ if (length > m) { m = length; n = NR } } END { printf \"longest=%d line=%d\\n\", m, n }' SKILL.md"

# 15 — optional report pointers (the plan's battery names it; not revision-bound)
if [ -n "$REPORT" ]; then
  [ -f "$REPORT" ] || die "report not found: $REPORT"
  REPORT_ABS=$(cd "$(dirname "$REPORT")" && pwd -P)/$(basename "$REPORT")
  run_receipt 15-report-pointers.txt "$CLONE" 600 "the plan's check_report_pointers step on the round report" \
    "python3 -B verifiers/check_report_pointers.py --report $(q "$REPORT_ABS") --repo . --rev $(q "$FULL")"
fi

# --- index and figures ------------------------------------------------
i=0
while [ "$i" -lt "${#RECEIPT_NAMES[@]}" ]; do
  printf '%s\t%s\n' "${RECEIPT_NAMES[$i]}" "${RECEIPT_EXITS[$i]}" >>"$IDX"
  i=$((i + 1))
done
{
  printf '# finished=%s\n' "$(utc)"
  for f in 01-tip-battery-dot.txt 02-tip-battery-abs.txt; do
    line=$(grep -E 'guards [0-9]+ of [0-9]+; tip battery exit 0: [0-9]+ of [0-9]+' "$OUT/$f" 2>/dev/null | tail -n 1)
    printf '# figure %s: %s\n' "$f" "${line:-<no frozen line>}"
  done
  for f in 10-skill-lines.txt 11-skill-bytes.txt 12-skill-long120.txt 13-skill-long300.txt \
           14-skill-longest.txt; do
    printf '# figure %s: %s\n' "$f" "$(figure_of "$OUT/$f")"
  done
} >>"$IDX" 2>/dev/null

green=0
i=0
while [ "$i" -lt "${#RECEIPT_EXITS[@]}" ]; do
  [ "${RECEIPT_EXITS[$i]}" -eq 0 ] && green=$((green + 1))
  i=$((i + 1))
done
printf '%s: rev %s; %d receipt(s), %d exit 0, %d non-zero; receipts in %s\n' \
  "$PROG" "$FULL" "${#RECEIPT_NAMES[@]}" "$green" \
  "$((${#RECEIPT_NAMES[@]} - green))" "$OUT"
for f in 01-tip-battery-dot.txt 02-tip-battery-abs.txt; do
  line=$(grep -E 'guards [0-9]+ of [0-9]+; tip battery exit 0: [0-9]+ of [0-9]+' "$OUT/$f" 2>/dev/null | tail -n 1)
  printf '%s: %s\n' "${f%.txt}" "${line:-<no frozen line>}"
done
exit "$RUN_FAIL"
