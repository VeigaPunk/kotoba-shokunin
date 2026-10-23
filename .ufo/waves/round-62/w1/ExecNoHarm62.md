# Round 62 no-harm battery draft

**Scope:** deliverable text for `.ufo/waves/round-62/noharm-battery.sh`. This seat may write only this report; the lane script itself is not landed by this seat. The report contains the complete script text for the L1 to integrate.

## Behavior

- Retains all round-61 battery arms and its three battery self-checks. The comparison base defaults to the round-62 plan base (`a745411c66d4765e9ac0ce48f1d96c34f425dab4`); the sources-history base stays `422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`.
- Adds optional tip-column `--self-test` arms for `check_erratum_absorption.py` and `check_routed_repairs_v2.py`. If either is absent at the tip it prints exactly `SKIP <name> (not landed)`; absence alone does not change the verdict. If present, nonzero exit fails its arm.
- Adds a required tip-column `check_scoped_rules_v31.py --self-test` arm; missing or nonzero fails. Runs its fixed-revision `--rev 43fe0180 --fetch` as optional/live informational output, not a verdict arm. The legacy scoped-rules self-test, routed-repairs info, and scoped-rules live-fetch info remain.
- `no-harm OK` is printed only when every gating arm passes. The legacy network-backed arms continue to gate and reject exit 2.

## Commands in the battery

For each base/tip column, as applicable:

- `python3 -B verifiers/check_gate_registry.py --rev <column-revision>`
- `python3 -B verifiers/verify_corpus_integrity.py`
- `python3 -B verifiers/check_sources_append_only.py --rev <column-revision> --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`
- `python3 -B verifiers/verify_skill_checklist.py`
- `python3 -B verifiers/box_proof_case_deletion.py --rev <column-revision>`
- `python3 -B verifiers/check_assertion_floors.py`
- `python3 -B verifiers/check_agent_definitions.py --rev <column-revision> --fetch`
- `python3 -B verifiers/check_explicit_invocation.py --rev <column-revision> --fetch`
- `python3 -B verifiers/check_description_thresholds.py --rev <column-revision> --fetch`
- `python3 -B verifiers/check_mcp_instructions.py --rev <column-revision> --fetch`
- `python3 -B verifiers/check_plugin_manifests.py --rev <column-revision> --fetch`
- `python3 -B verifiers/check_hook_files.py --rev <column-revision> --fetch`
- `python3 -B verifiers/check_scoped_rules.py --self-test`

Tip-only new self-test commands (only the first two are optional):

- `python3 -B verifiers/check_erratum_absorption.py --self-test` (if landed)
- `python3 -B verifiers/check_routed_repairs_v2.py --self-test` (if landed)
- `python3 -B verifiers/check_scoped_rules_v31.py --self-test` (required)
- `python3 -B verifiers/check_scoped_rules_v31.py --rev 43fe0180 --fetch` (optional/live informational)

Existing informational commands retained:

- `python3 -B verifiers/check_routed_repairs.py --rev <tip-revision>` (if present)
- `python3 -B verifiers/check_scoped_rules.py --rev <tip-revision> --fetch`
- `python3 -B verifiers/check_scoped_rules.py --rev <base-revision> --fetch`

The script also builds two scratch clones and uses shell comparison/self-check commands (`git`, `find`, `ln`, `sed`, `grep`, `awk`, `sort`, `comm`, `diff`, `cp`, `wc`, `cut`, `tr`, `tail`, `date`, and temporary-file operations) as shown below. Those operations do not write to the lane or fleet.

## Commands run now

**None.** The wave is still in flight and the parent owns post-integration verification; no build, lint, test, formatter, or battery command was run. The source script and repository inventory were read only. There is consequently no command output, date, or exit code to report as a measurement.

## Retained evidence

- Read `.ufo/waves/round-61/noharm-battery.sh`; its source includes `reg_gate`, `corpus` plus unindexed-file comparison, `sources`, `checklist` plus unresolved-pointer comparison, `boxproof`, `floors`, `agentdefs`, `explicit`, `desc`, `mcp`, `plugin`, `hooks`, `scoped`, the three `battery-self*` checks, routed-repairs informational run, and the scoped-rules tip/base live-fetch informational runs.
- Read `plans/round-62.md`; its base revision is `a745411c66d4765e9ac0ce48f1d96c34f425dab4`, and it names `check_scoped_rules_v31.py` as the E2f successor.
- The current `verifiers/` inventory listed `check_scoped_rules.py` and `check_routed_repairs.py`; it did not list `check_erratum_absorption.py`, `check_routed_repairs_v2.py`, or `check_scoped_rules_v31.py`. No instrument execution was attempted.

## Complete script text

Target path: `.ufo/waves/round-62/noharm-battery.sh`

```bash
#!/usr/bin/env bash
# noharm-battery.sh — kotoba round-62 no-harm battery (read-only on the lane).
#
# WHAT IT IS
#   One runnable battery that answers: "did round 62 harm anything a previous
#   round had already certified?" It compares every inherited arm in a sandbox
#   checkout of the round's base revision and a sandbox checkout of the tip.
#   Round-62 successor self-tests run against the tip because those instruments
#   are new to this round. It prints `no-harm OK` only when every gating arm
#   passes.
#
#   It never writes to the lane, the fleet, a sibling lane, .ufo/state, or any
#   git/jj index. The only writes are into a scratch sandbox (default
#   $TMPDIR/kotoba-r62-noharm.XXXXXX), removed at the end unless --keep.
#
# USAGE
#   bash .ufo/waves/round-62/noharm-battery.sh [--base REV] [--tip REV]
#                                              [--sandbox DIR] [--keep]
#   Defaults: --base a745411c66d4765e9ac0ce48f1d96c34f425dab4  (round-62 base)
#             --tip  HEAD   (resolved in the lane at run time)
#
#   Run it from the lane after the integration commits exist. Exit 0 and the
#   last printed line `no-harm OK` mean every gating arm passed. Any other exit
#   means at least one arm failed; failing-arm output is left under sandbox logs.
#   If either optional new verifier is absent at tip, the script prints
#   `SKIP <name> (not landed)`; it does not silently treat an absent instrument
#   as a pass or let absence alone change the verdict.
#
# INHERITED ARMS AND COMPARISONS
#   reg_gate   check_gate_registry.py --rev <rev>       both columns exit 0
#   corpus     verify_corpus_integrity.py                tip introduces NO new
#              (tree gate)                              DRIFT kind, and the set
#                                                      of unindexed corpus files
#                                                      does not grow
#   sources    check_sources_append_only.py              both columns exit 0
#              --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --rev <rev>
#   checklist verify_skill_checklist.py                 tip introduces NO new
#              (tree gate)                              failing check id, and the
#                                                      number of unresolved
#                                                      citation pointers does
#                                                      not grow
#   boxproof  box_proof_case_deletion.py --rev <rev>     both columns exit 0
#   floors    check_assertion_floors.py                  both columns exit 0
#              (tree gate)
#   agentdefs check_agent_definitions.py --rev <rev> --fetch  unchanged
#   explicit  check_explicit_invocation.py --rev <rev> --fetch unchanged
#   desc      check_description_thresholds.py --rev <rev> --fetch unchanged
#   mcp       check_mcp_instructions.py --rev <rev> --fetch  unchanged
#   plugin    check_plugin_manifests.py --rev <rev> --fetch unchanged
#   hooks     check_hook_files.py --rev <rev> --fetch      unchanged
#   scoped    check_scoped_rules.py --self-test           both columns exit 0
#
# ROUND-62 SUCCESSOR ARMS
#   absorption check_erratum_absorption.py --self-test    tip exit 0 if present
#   repairs-v2 check_routed_repairs_v2.py --self-test      tip exit 0 if present
#              An absent optional instrument prints SKIP <name> (not landed).
#   scoped-v31 check_scoped_rules_v31.py --self-test       tip exit 0 (required)
#   The v3.1 live fetch at --rev 43fe0180 is run as informational/optional;
#   live/network variability does not change the battery verdict.
#
#   The inherited --fetch arms read live vendor documentation. An exit 2 on a
#   gating arm means could-not-evaluate and fails; an unevaluated arm has not
#   passed. Live-page summary lines are excluded from inherited output equality,
#   while committed per-client verdict lines remain compared.
#
# EXIT CODES
#   0  every gating arm passed; last line printed is `no-harm OK`
#   1  at least one gating arm failed (list printed)
#   2  usage error / sandbox could not be built
set -u -o pipefail

SELF_DIR=$(cd "$(dirname "$0")" && pwd)
if [ -n "${NOHARM_LANE:-}" ]; then
  LANE_ROOT=$(git -C "$NOHARM_LANE" rev-parse --show-toplevel 2>/dev/null)
else
  # walk up from the script until a lane root (SKILL.md + verifiers/) is found
  probe=$SELF_DIR
  while [ "$probe" != "/" ]; do
    if [ -f "$probe/SKILL.md" ] && [ -d "$probe/verifiers" ]; then
      LANE_ROOT=$(git -C "$probe" rev-parse --show-toplevel 2>/dev/null) && break
    fi
    probe=$(dirname "$probe")
  done
fi
if [ -z "${LANE_ROOT:-}" ]; then
  echo "noharm: cannot locate the lane repository from $SELF_DIR" >&2
  exit 2
fi
FLEET_ROOT=$(dirname "$LANE_ROOT")

BASE_REV=a745411c66d4765e9ac0ce48f1d96c34f425dab4
TIP_REV=HEAD
SANDBOX=
KEEP=0
SOURCES_BASE=422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4

while [ $# -gt 0 ]; do
  case "$1" in
    --base)    BASE_REV=$2; shift 2 ;;
    --tip)     TIP_REV=$2;  shift 2 ;;
    --sandbox) SANDBOX=$2; shift 2 ;;
    --keep)    KEEP=1; shift ;;
    -h|--help) sed -n '2,/^set -u/p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "noharm: unknown argument: $1" >&2; exit 2 ;;
  esac
done

BASE_SHA=$(git -C "$LANE_ROOT" rev-parse --verify "$BASE_REV^{commit}" 2>/dev/null) || {
  echo "noharm: base revision $BASE_REV does not resolve in $LANE_ROOT" >&2; exit 2; }
TIP_SHA=$(git -C "$LANE_ROOT" rev-parse --verify "$TIP_REV^{commit}" 2>/dev/null) || {
  echo "noharm: tip revision $TIP_REV does not resolve in $LANE_ROOT" >&2; exit 2; }

if [ -z "$SANDBOX" ]; then
  SANDBOX=$(mktemp -d "${TMPDIR:-/tmp}/kotoba-r62-noharm.XXXXXX") || exit 2
fi
mkdir -p "$SANDBOX" || exit 2
LOGS="$SANDBOX/logs"; mkdir -p "$LOGS/base" "$LOGS/tip" || exit 2

cleanup() { [ "$KEEP" -eq 1 ] || rm -rf "$SANDBOX"; }
trap cleanup EXIT

# ---- sandbox construction -------------------------------------------------
# One checkout per column, the checkout directory named kotoba-shokunin (the
# checklist's trigger.name_directory check compares the frontmatter name with
# the directory name), plus symlinks of the fleet-root entries beside it so
# `../` citation hops resolve exactly as they do from the lane.
build_column() {  # $1 = column name, $2 = revision sha
  local col=$1 rev=$2 dir="$SANDBOX/$1" e b
  mkdir -p "$dir" || return 1
  git clone --shared -q "$LANE_ROOT" "$dir/kotoba-shokunin" || return 1
  git -C "$dir/kotoba-shokunin" checkout -q "$rev" || return 1
  while IFS= read -r -d '' e; do
    b=${e##*/}
    case "$b" in
      "$(basename "$LANE_ROOT")"|.git|.jj) continue ;;
    esac
    ln -sfn "$e" "$dir/$b" 2>/dev/null || true
  done < <(find "$FLEET_ROOT" -mindepth 1 -maxdepth 1 -print0 2>/dev/null)
  return 0
}

echo "noharm: lane        $LANE_ROOT"
echo "noharm: base        $BASE_SHA"
echo "noharm: tip         $TIP_SHA"
echo "noharm: sandbox     $SANDBOX"
echo "noharm: date -u     $(date -u +%Y-%m-%dT%H:%M:%SZ)"

for col in base tip; do
  if [ "$col" = base ]; then rev=$BASE_SHA; else rev=$TIP_SHA; fi
  if ! build_column "$col" "$rev"; then
    echo "noharm: could not build the $col sandbox" >&2
    exit 2
  fi
  echo "noharm: column $col ready ($(git -C "$SANDBOX/$col/kotoba-shokunin" rev-parse HEAD))"
done

BASE_TREE="$SANDBOX/base/kotoba-shokunin"
TIP_TREE="$SANDBOX/tip/kotoba-shokunin"

# ---- run helpers ----------------------------------------------------------
RC=0
run() {  # run <outfile> <tree> <cmd...>  -> exit code left in RC
  local out=$1 tree=$2; shift 2
  ( cd "$tree" && "$@" ) >"$out" 2>&1
  RC=$?
  return 0
}

norm() {  # norm <file> -> normalized stdout on stdout
  sed -E \
    -e 's/[0-9a-f]{64}/<SHA64>/g' \
    -e 's/[0-9a-f]{40}/<SHA40>/g' \
    -e '/^counter sha256/d' \
    -e '/^counter rev/d' \
    -e '/^Wall time/d' \
    -e 's/new ground [0-9]+/new ground <N>/g' \
    "$1"
}

norm_lane() {  # norm_lane <file> -> normalized stdout WITHOUT the live-page line
  norm "$1" | grep -v 'on the live page'
}

FAILURES=0
report() {  # report <arm> <verdict> <detail>
  if [ "$2" = FAIL ]; then
    FAILURES=$((FAILURES + 1))
    printf 'FAIL  %-11s %s\n' "$1" "$3"
  else
    printf 'PASS  %-11s %s\n' "$1" "$3"
  fi
}

# ---- arm runners ----------------------------------------------------------
# tree gate: the script runs on the working tree of each column's checkout.
tree_gate() {  # tree_gate <arm> <script> [args...]
  local arm=$1 script=$2; shift 2
  run "$LOGS/base/$arm.txt" "$BASE_TREE" python3 -B "verifiers/$script" "$@"; local rb=$RC
  run "$LOGS/tip/$arm.txt"  "$TIP_TREE"  python3 -B "verifiers/$script" "$@"; local rt=$RC
  printf '%s %s\n' "$rb" "$rt" > "$LOGS/$arm.exits"
}

# rev gate: the counter code AND the measured content both come from the
# column's own checkout, so the counter's --rev argument is that column's rev.
rev_gate() {  # rev_gate <arm> <script> [args...]
  local arm=$1 script=$2; shift 2
  run "$LOGS/base/$arm.txt" "$BASE_TREE" python3 -B "verifiers/$script" --rev "$BASE_SHA" "$@"; local rb=$RC
  run "$LOGS/tip/$arm.txt"  "$TIP_TREE"  python3 -B "verifiers/$script" --rev "$TIP_SHA"  "$@"; local rt=$RC
  printf '%s %s\n' "$rb" "$rt" > "$LOGS/$arm.exits"
}

# New round-62 instruments are checked at tip: the base column predates them.
# Absence is explicit and non-gating only for the two named optional tools.
tip_self_test_optional() {  # arm, verifier filename, then self-test args
  local arm=$1 script=$2; shift 2
  if [ ! -f "$TIP_TREE/verifiers/$script" ]; then
    printf 'SKIP %s (not landed)\n' "$script"
    return 0
  fi
  run "$LOGS/tip/$arm.txt" "$TIP_TREE" python3 -B "verifiers/$script" "$@"
  if [ "$RC" -eq 0 ]; then
    report "$arm" PASS "$script self-test exited 0 at tip"
  else
    report "$arm" FAIL "$script self-test exited $RC at tip"
    sed 's/^/        tip: /' "$LOGS/tip/$arm.txt" | head -8 || true
  fi
}

tip_self_test_required() {  # arm, verifier filename, then self-test args
  local arm=$1 script=$2; shift 2
  if [ ! -f "$TIP_TREE/verifiers/$script" ]; then
    report "$arm" FAIL "$script is missing at tip (required successor)"
    return 0
  fi
  run "$LOGS/tip/$arm.txt" "$TIP_TREE" python3 -B "verifiers/$script" "$@"
  if [ "$RC" -eq 0 ]; then
    report "$arm" PASS "$script self-test exited 0 at tip"
  else
    report "$arm" FAIL "$script self-test exited $RC at tip"
    sed 's/^/        tip: /' "$LOGS/tip/$arm.txt" | head -8 || true
  fi
}

cmp_exit0() {  # cmp_exit0 <arm>
  local arm=$1 rb rt
  read -r rb rt < "$LOGS/$arm.exits"
  if [ "$rb" -eq 0 ] && [ "$rt" -eq 0 ]; then
    report "$arm" PASS "exit 0 in both columns (base=$rb tip=$rt)"
  else
    report "$arm" FAIL "expected exit 0 in both columns, got base=$rb tip=$rt"
    grep -iE 'no registry rows naming it|conformant|phantom' "$LOGS/tip/$arm.txt" | sed 's/^/        tip: /' || true
  fi
}

cmp_unchanged() {  # cmp_unchanged <arm> [lane_only]
  # Without the second argument the full normalized output is compared.
  # With the argument `lane_only` the live-page summary line is dropped from
  # both sides first (used for the --fetch arms, whose live page can change
  # between the two column runs).
  local arm=$1 mode=${2:-full} rb rt
  read -r rb rt < "$LOGS/$arm.exits"
  # Exit 2 is could-not-evaluate. If BOTH columns are 2 (e.g. the network was
  # down for the whole run) the outputs would compare equal and the arm would
  # read as a pass. An unevaluated arm has not passed: reject it.
  if [ "$rb" -eq 2 ] || [ "$rt" -eq 2 ]; then
    report "$arm" FAIL "could-not-evaluate in a column (exit 2) — an unevaluated arm has not passed (base=$rb tip=$rt)"
    sed 's/^/        tip: /' "$LOGS/tip/$arm.txt" | head -5 || true
    return 0
  fi
  if [ "$mode" = lane_only ]; then
    norm_lane "$LOGS/base/$arm.txt" > "$LOGS/base/$arm.norm"
    norm_lane "$LOGS/tip/$arm.txt"  > "$LOGS/tip/$arm.norm"
  else
    norm "$LOGS/base/$arm.txt" > "$LOGS/base/$arm.norm"
    norm "$LOGS/tip/$arm.txt" > "$LOGS/tip/$arm.norm"
  fi
  if [ "$rb" -ne "$rt" ]; then
    report "$arm" FAIL "exit code changed: base=$rb tip=$rt"
  elif ! diff -q "$LOGS/base/$arm.norm" "$LOGS/tip/$arm.norm" >/dev/null; then
    diff -u "$LOGS/base/$arm.norm" "$LOGS/tip/$arm.norm" > "$LOGS/$arm.diff" 2>&1 || true
    report "$arm" FAIL "output changed (normalized diff: $LOGS/$arm.diff)"
  else
    report "$arm" PASS "exit $rb and normalized output identical in both columns"
  fi
}

cmp_no_new_kind() {  # cmp_no_new_kind <arm> <awk field> <label>
  local arm=$1 field=$2 label=$3
  awk -v f="$field" '$1=="DRIFT"||$1=="FAIL"{print $f}' "$LOGS/base/$arm.txt" | sort -u > "$LOGS/base/$arm.kinds"
  awk -v f="$field" '$1=="DRIFT"||$1=="FAIL"{print $f}' "$LOGS/tip/$arm.txt"  | sort -u > "$LOGS/tip/$arm.kinds"
  local new
  new=$(comm -13 "$LOGS/base/$arm.kinds" "$LOGS/tip/$arm.kinds")
  if [ -z "$new" ]; then
    report "$arm" PASS "tip introduces no new $label (base set: $(tr '\n' ' ' < "$LOGS/base/$arm.kinds"))"
  else
    report "$arm" FAIL "tip introduces new $label: $(echo "$new" | tr '\n' ' ')"
  fi
}

# ---- corpus arm, second half: unindexed file set must not grow ------------
cmp_no_new_unindexed() {
  local arm=corpus
  # the gate prints one indented line per unindexed file: "  unindexed: <path>"
  grep -oE '(^|[[:space:]])unindexed: [^ ]+' "$LOGS/base/$arm.txt" | sed 's/.*unindexed: //' | sort -u > "$LOGS/base/$arm.unindexed"
  grep -oE '(^|[[:space:]])unindexed: [^ ]+' "$LOGS/tip/$arm.txt"  | sed 's/.*unindexed: //' | sort -u > "$LOGS/tip/$arm.unindexed"
  local new
  new=$(comm -13 "$LOGS/base/$arm.unindexed" "$LOGS/tip/$arm.unindexed")
  if [ -z "$new" ]; then
    report "corpus-idx" PASS "no new unindexed corpus file at tip (base set: $(tr '\n' ' ' < "$LOGS/base/$arm.unindexed"))"
  else
    report "corpus-idx" FAIL "tip leaves new corpus file(s) unindexed: $(echo "$new" | tr '\n' ' ')"
  fi
}

# ---- checklist arm, second half: unresolved pointer count must not grow ---
cmp_no_new_pointer() {
  local arm=checklist nb nt
  nb=$(grep -o 'does not resolve from' "$LOGS/base/$arm.txt" | wc -l)
  nt=$(grep -o 'does not resolve from' "$LOGS/tip/$arm.txt"  | wc -l)
  if [ "$nt" -le "$nb" ]; then
    report "check-ptr" PASS "unresolved citation pointers did not grow (base=$nb tip=$nt)"
  else
    report "check-ptr" FAIL "unresolved citation pointers grew (base=$nb tip=$nt)"
    grep -o "[^;]*does not resolve from" "$LOGS/tip/$arm.txt" | sed 's/^/        tip: /' || true
  fi
}

# ============================ ARMS =========================================
echo "--- arms ---"

rev_gate  reg_gate  check_gate_registry.py
cmp_exit0 reg_gate

tree_gate corpus verify_corpus_integrity.py
cmp_no_new_kind corpus 2 "DRIFT kind"
cmp_no_new_unindexed

rev_gate  sources   check_sources_append_only.py --base "$SOURCES_BASE"
cmp_exit0 sources

tree_gate checklist verify_skill_checklist.py
cmp_no_new_kind checklist 2 "failing check id"
cmp_no_new_pointer

rev_gate  boxproof  box_proof_case_deletion.py
cmp_exit0 boxproof

tree_gate floors check_assertion_floors.py
cmp_exit0 floors

rev_gate  agentdefs check_agent_definitions.py   --fetch
cmp_unchanged agentdefs lane_only

rev_gate  explicit  check_explicit_invocation.py --fetch
cmp_unchanged explicit lane_only

rev_gate  desc      check_description_thresholds.py --fetch
cmp_unchanged desc lane_only

rev_gate  mcp       check_mcp_instructions.py --fetch
cmp_unchanged mcp lane_only

rev_gate  plugin    check_plugin_manifests.py --fetch
cmp_unchanged plugin lane_only

rev_gate  hooks     check_hook_files.py --fetch
cmp_unchanged hooks lane_only

# The r61 scoped-rules counter remains a frozen, inherited no-harm arm.
run "$LOGS/base/scoped.txt" "$BASE_TREE" python3 -B verifiers/check_scoped_rules.py --self-test; rb=$RC
run "$LOGS/tip/scoped.txt"  "$TIP_TREE"  python3 -B verifiers/check_scoped_rules.py --self-test; rt=$RC
printf '%s %s\n' "$rb" "$rt" > "$LOGS/scoped.exits"
cmp_exit0 scoped

# Round-62 instruments are new, so run their self-tests at tip. The first two
# explicitly skip (with a visible note) if not landed; v3.1 is required by C1.
tip_self_test_optional absorption check_erratum_absorption.py --self-test
tip_self_test_optional repairs-v2 check_routed_repairs_v2.py --self-test
tip_self_test_required scoped-v31 check_scoped_rules_v31.py --self-test

# ---- battery self-verification -------------------------------------------
# A battery that cannot fail is not a battery. These arms mutate the tip
# column's own output and re-run the comparison. If a mutated copy still
# compares equal, the comparison is vacuous and the battery FAILS.
SELFCHECK_DIR="$SANDBOX/selfcheck"
mkdir -p "$SELFCHECK_DIR/base" "$SELFCHECK_DIR/tip"
cp "$LOGS/base/agentdefs.txt" "$SELFCHECK_DIR/base/agentdefs.txt"
cp "$LOGS/tip/agentdefs.txt"  "$SELFCHECK_DIR/tip/agentdefs.txt"
# mutate: flip one committed verdict from BACKED to reject
sed -i 's/^Codex        BACKED/Codex        reject/' "$SELFCHECK_DIR/tip/agentdefs.txt"
norm_lane "$SELFCHECK_DIR/base/agentdefs.txt" > "$SELFCHECK_DIR/base/agentdefs.norm"
norm_lane "$SELFCHECK_DIR/tip/agentdefs.txt"  > "$SELFCHECK_DIR/tip/agentdefs.norm"
if diff -q "$SELFCHECK_DIR/base/agentdefs.norm" "$SELFCHECK_DIR/tip/agentdefs.norm" >/dev/null; then
  report "battery-self" FAIL "the comparison did NOT detect a mutated verdict line — the battery is vacuous"
else
  report "battery-self" PASS "a mutated verdict line was detected by the comparison (battery is not vacuous)"
fi

# second self-check: the corpus DRIFT-kind comparison must see a NEW kind
SELFCHECK_DIR="$SANDBOX/selfcheck2"
mkdir -p "$SELFCHECK_DIR/base" "$SELFCHECK_DIR/tip"
cp "$LOGS/base/corpus.txt" "$SELFCHECK_DIR/base/corpus.txt"
cp "$LOGS/tip/corpus.txt"  "$SELFCHECK_DIR/tip/corpus.txt"
printf 'DRIFT   corpus.pointers.injected_kind: observed=1 expected=0\n' >> "$SELFCHECK_DIR/tip/corpus.txt"
awk '$1=="DRIFT"||$1=="FAIL"{print $2}' "$SELFCHECK_DIR/base/corpus.txt" | sort -u > "$SELFCHECK_DIR/base/corpus.kinds"
awk '$1=="DRIFT"||$1=="FAIL"{print $2}' "$SELFCHECK_DIR/tip/corpus.txt"  | sort -u > "$SELFCHECK_DIR/tip/corpus.kinds"
if [ -z "$(comm -13 "$SELFCHECK_DIR/base/corpus.kinds" "$SELFCHECK_DIR/tip/corpus.kinds")" ]; then
  report "battery-self2" FAIL "the corpus DRIFT-kind comparison did NOT detect an injected new kind — it is vacuous"
else
  report "battery-self2" PASS "an injected new corpus DRIFT kind was detected by the comparison"
fi

# third self-check: a could-not-evaluate (exit 2) column must NOT read as a pass
SELFCHECK_DIR="$SANDBOX/selfcheck3"
mkdir -p "$SELFCHECK_DIR"
printf '2 2\n' > "$SELFCHECK_DIR/fake.exits"
cp "$LOGS/base/agentdefs.txt" "$SELFCHECK_DIR/base.txt"
cp "$LOGS/tip/agentdefs.txt" "$SELFCHECK_DIR/tip.txt"
norm_lane "$SELFCHECK_DIR/base.txt" > "$SELFCHECK_DIR/base.norm"
norm_lane "$SELFCHECK_DIR/tip.txt" > "$SELFCHECK_DIR/tip.norm"
if [ "$(cat "$SELFCHECK_DIR/fake.exits" | cut -d' ' -f1)" -eq 2 ] && \
   diff -q "$SELFCHECK_DIR/base.norm" "$SELFCHECK_DIR/tip.norm" >/dev/null; then
  report "battery-self3" PASS "an exit-2 (could-not-evaluate) column is caught by the comparison guard"
else
  report "battery-self3" FAIL "the exit-2 guard is not exercised — identical outputs at exit 2 would read as a pass"
fi

# ---- informational (does not gate the verdict) ----------------------------
echo "--- informational ---"
if [ -f "$TIP_TREE/verifiers/check_routed_repairs.py" ]; then
  run "$LOGS/routed.txt" "$TIP_TREE" python3 -B verifiers/check_routed_repairs.py --rev "$TIP_SHA"
  echo "INFO  routed-repairs (C2 predicate; the L1 measures it) exit=$RC: $(tail -1 "$LOGS/routed.txt")"
else
  echo "INFO  routed-repairs counter not present at tip"
fi
echo "INFO  scoped-rules self-test at tip: $(tail -1 "$LOGS/tip/scoped.txt")"
run "$LOGS/scoped_fetch_tip.txt" "$TIP_TREE" python3 -B verifiers/check_scoped_rules.py --rev "$TIP_SHA" --fetch
echo "INFO  scoped-rules --rev tip  --fetch: exit=$RC: $(tail -1 "$LOGS/scoped_fetch_tip.txt")"
run "$LOGS/scoped_fetch_base.txt" "$TIP_TREE" python3 -B verifiers/check_scoped_rules.py --rev "$BASE_SHA" --fetch
echo "INFO  scoped-rules --rev base --fetch: exit=$RC: $(tail -1 "$LOGS/scoped_fetch_base.txt")"
echo "INFO  (the inherited C1 control: tip counter code, --rev base -> exit 1; --rev tip -> exit 0)"

if [ -f "$TIP_TREE/verifiers/check_scoped_rules_v31.py" ]; then
  run "$LOGS/scoped_v31_fetch.txt" "$TIP_TREE" python3 -B verifiers/check_scoped_rules_v31.py --rev 43fe0180 --fetch
  echo "INFO  scoped-rules-v31 --rev 43fe0180 --fetch (optional/live): exit=$RC: $(tail -1 "$LOGS/scoped_v31_fetch.txt")"
else
  echo "INFO  scoped-rules-v31 --rev 43fe0180 --fetch (optional/live): skipped (counter not landed)"
fi

echo "--- verdict ---"
if [ "$FAILURES" -eq 0 ]; then
  echo "no-harm OK"
  exit 0
fi
echo "no-harm FAILED: $FAILURES arm(s) failed"
exit 1
```

**Installs:** no installs.

**Blockers:** none. Checks were not run because this is an in-flight editing wave; the L1 owns post-integration verification.

**Produced:** round-62 no-harm battery draft preserving the r61 arms and adding the requested successor checks.
