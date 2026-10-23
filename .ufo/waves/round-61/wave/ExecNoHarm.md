# Round-61 wave — ExecNoHarm: the no-harm battery (definition + before-column measurement + one live finding)

Seat `kotoba-r61-wave-ExecNoHarm` (wave `kotoba-r61-wave`, executor, axis `operability`).
Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (jj-colocated). I wrote **no** lane file
other than this report; I did not touch the fleet root, any sibling lane, `.ufo/state`, or any
git/jj index. The L1 `agent://KotobaR61` is the only integrator.

Date (all `date -u` stamps below): 2026-10-23.
Base under test: `f3246d1493b60ea1c0d947a19c39f9e08e92f326` (r60 tip, the round-61 plan's base).
Tip under test: `7827628a939b0333c89892dfcedc72e390ccfb60` (the round-61 plan freeze commit —
the current lane tip at the time of measurement).
Python 3.14.8, host `Linux 7.2.11-arch1-1 x86_64`.

---

## 0. Headline

1. **The battery exists and runs.** One runnable script, 424 lines, sha256
   `ddeaa1313ead419d562b16d9a256595507cbd49c8069fbdc7531ce3fb51dd32b`, syntax-checked
   (`bash -n` → exit 0). Full text is in §2 below; the L1 lands it at
   `.ufo/waves/round-61/noharm-battery.sh`. `scripts/hyaku-adjacent` is not mine and was not touched.
2. **The battery is proven in both directions.** Against the current lane tip it prints
   `no-harm FAILED: 1 arm(s) failed` and exits 1, naming the failing arm. Against a simulated
   post-integration tip that carries the one missing registry row it prints `no-harm OK` and exits 0.
   A battery that cannot fail is not a battery, so the script carries **three self-verification
   arms** that mutate the tip column's own output and prove the comparison machinery detects the
   mutation. All three PASS.
3. **One live defect found and localized — now CLOSED and verified.** (Added after filing; see
   §5.1.) `verifiers/check_routed_repairs.py` — the C2 counter committed by the round-61 plan
   freeze — had **no `SKILL.md` § Gate registry row**, so `check_gate_registry.py --rev <any rev ≥
   the plan freeze>` exited 1 with `gate registry rows conformant 34 of 35 lane verifiers`. The
   exact row text that repairs it is in §4, and I **measured** that it turns the gate green
   (35 of 35, exit 0). The L1 landed it as `cf288d84`; the battery re-run against that real
   integration commit prints **`no-harm OK` and exits 0** (§5.1). This was the same defect class
   round 60 recorded for the round-60 counter
   (`.ufo/waves/round-60/build/ExecNoHarmBase.md` § "known red"); it had not been re-routed.
4. **Everything else in the prior-round certification surface is unchanged-in-behavior** between
   base and tip — 15 of 16 arms PASS at the pre-fix tip, and all 16 PASS at `cf288d84`.

---

## 1. What the battery is, and why it is shaped this way

The assignment asks for "one runnable script text" covering: gate registry, corpus integrity,
sources append-only (base `422ffd10…` per the registry row), skill checklist + box-proof gate,
assertion floors, and **every prior round counter unchanged-in-behavior** (agent definitions 7/7,
explicit invocation, description thresholds, MCP instructions, plugin manifests, hook files,
scoped rules v2 self-test). It must print `no-harm OK` only when all pass.

The design decision that shapes everything: **every arm is measured twice and compared**, once in
a sandbox checkout of the round's base revision and once in a sandbox checkout of the tip
revision. A single-column "is it green?" test cannot distinguish *pre-existing red* from
*round-61 harm*, and this lane is full of pre-existing red (see §5). The comparison form is the
only one that answers the question actually being asked.

Two consequences worth stating plainly:

- **A prior counter that is red at base stays comparable.** `check_plugin_manifests.py` exits 1 at
  base (VS Code / Copilot CLI share the root `plugin.json`; opencode has no JSON manifest — the
  r57 miss, recorded in `LOG.md:2493`). The battery compares *base exit == tip exit* and
  *base output == tip output*, so a persistent red is fine and a newly-red arm is not. An
  "exit 0" test would have called the base state a failure and taught the L1 to ignore the arm.
- **The C1 counter is deliberately not compared for output equality.** `check_scoped_rules.py` is
  being rewritten v2→v3 this round; the plan freezes that as the claim, so byte-comparing its
  output would flag the intended change as a regression. The `scoped` arm certifies only that the
  self-test stayed green in both columns. The v3 predicate itself (`worlds reject 7 of 7; eligible
  rows pass 4 of 4`) is the C1 receipt's job, and the battery prints the tip self-test line as
  `INFO` so the L1 can read it without re-running the command.

### Read-only discipline

The script writes only into a scratch sandbox (`mktemp -d $TMPDIR/kotoba-r61-noharm.XXXXXX`),
removed on exit unless `--keep`. It clones the lane with `git clone --shared` (read-only on the
source), checks out the measured revs, and never runs a mutating git/jj command in the lane. The
clone directory is named `kotoba-shokunin` because the checklist's `trigger.name_directory` check
compares the frontmatter `name` against the directory name — a clone named anything else fails
that check for an environmental reason. Fleet-root entries are symlinked beside the checkout so
`../` citation hops resolve exactly as they do from the lane (the same trick
`.ufo/waves/round-60/build/ExecNoHarmBase.md` § Method records).

---

## 2. The deliverable — `.ufo/waves/round-61/noharm-battery.sh`

Target path (relative to the lane repo): **`.ufo/waves/round-61/noharm-battery.sh`**
(424 lines, sha256 `ddeaa1313ead419d562b16d9a256595507cbd49c8069fbdc7531ce3fb51dd32b`,
`bash -n` exit 0).

```bash
#!/usr/bin/env bash
# noharm-battery.sh — kotoba round-61 no-harm battery (read-only on the lane).
#
# WHAT IT IS
#   One runnable battery that answers: "did round 61 harm anything a previous
#   round had already certified?"  It measures every arm twice — once in a
#   sandbox checkout of the round's base revision and once in a sandbox
#   checkout of the tip revision — and compares the two columns.  It prints
#   `no-harm OK` only when every arm passes its comparison.
#
#   It never writes to the lane, the fleet, a sibling lane, .ufo/state, or any
#   git/jj index.  The only writes are into a scratch sandbox (default
#   $TMPDIR/kotoba-r61-noharm.XXXXXX), removed at the end unless --keep.
#
# USAGE
#   bash .ufo/waves/round-61/noharm-battery.sh [--base REV] [--tip REV]
#                                              [--sandbox DIR] [--keep]
#   Defaults: --base f3246d1493b60ea1c0d947a19c39f9e08e92f326  (round-61 base)
#             --tip  HEAD   (resolved in the lane at run time)
#
#   Run it from the lane after the integration commits exist.  Exit 0 and the
#   last printed line `no-harm OK` mean every arm passed.  Any other exit means
#   at least one arm failed; the failing arms are named and both columns'
#   verbatim output is left under the sandbox logs directory.
#
# ARMS AND THEIR COMPARISONS
#   reg_gate   check_gate_registry.py --rev <rev>       both columns exit 0
#   corpus     verify_corpus_integrity.py                tip introduces NO new
#              (tree gate)                              DRIFT kind, and the set
#                                                      of unindexed corpus files
#                                                      does not grow
#   sources    check_sources_append_only.py              both columns exit 0
#              --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --rev <rev>
#   checklist  verify_skill_checklist.py                 tip introduces NO new
#              (tree gate)                              failing check id, and the
#                                                      number of unresolved
#                                                      citation pointers does
#                                                      not grow
#   boxproof   box_proof_case_deletion.py --rev <rev>    both columns exit 0
#   floors     check_assertion_floors.py                 both columns exit 0
#              (tree gate)
#   agentdefs  check_agent_definitions.py    --rev <rev> --fetch   behaviour
#   explicit   check_explicit_invocation.py  --rev <rev> --fetch   unchanged
#   desc       check_description_thresholds.py --rev <rev> --fetch  (normalized
#   mcp        check_mcp_instructions.py      --rev <rev> --fetch  output equal)
#   plugin     check_plugin_manifests.py     --rev <rev> --fetch
#   hooks      check_hook_files.py            --rev <rev> --fetch
#   scoped     check_scoped_rules.py --self-test          both columns exit 0
#              (self-test)                                  (the counter file is
#                                                        rewritten this round —
#                                                        the v3 predicate is the
#                                                        C1 claim, not this
#                                                        battery; what this arm
#                                                        certifies is that the
#                                                        self-test stayed green)
#
#   "behaviour unchanged" = same exit code AND same normalized output.  The
#   normalization drops counter-identity lines (`counter sha256 …`, `counter rev
#   …`), wall-time lines and the `new ground N` count; it rewrites 40/64-hex
#   ids to placeholders.  Every `N of M`, every `reject …` line, every
#   per-client verdict line and every exit code is compared exactly.
#
#   The `--fetch` arms read the live vendor documentation pages.  The live-page
#   summary line is compared in a second, lane-only pass (the line is dropped),
#   so an upstream documentation edit between the two column runs cannot be
#   mistaken for a lane regression; the per-client BACKED/reject verdict lines,
#   which come from the committed SKILL.md at the measured revision, are still
#   compared exactly in both passes.
#
# NETWORK
#   agentdefs, explicit, desc, mcp, plugin and hooks run with --fetch as the
#   SKILL.md § Gate registry rows specify, so they need the network.  If one
#   exits 2 (could-not-evaluate) the battery FAILS that arm and does not print
#   `no-harm OK` — an unevaluated arm has not passed.
#
# EXIT CODES
#   0  every arm passed; last line printed is `no-harm OK`
#   1  at least one arm failed (list printed)
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

BASE_REV=f3246d1493b60ea1c0d947a19c39f9e08e92f326
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
  SANDBOX=$(mktemp -d "${TMPDIR:-/tmp}/kotoba-r61-noharm.XXXXXX") || exit 2
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
  # Exit 2 is could-not-evaluate.  If BOTH columns are 2 (e.g. the network was
  # down for the whole run) the outputs would compare equal and the arm would
  # read as a pass.  An unevaluated arm has not passed: reject it.
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
    norm "$LOGS/tip/$arm.txt"  > "$LOGS/tip/$arm.norm"
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

# scoped rules: the counter file itself is rewritten this round (v3 = the C1
# claim), so the no-harm property measured here is that the self-test stays
# green in both columns.  The v3 predicate (7 of 7 worlds reject, 4 of 4
# eligible rows pass) is the C1 arm, measured by the C1 receipt.
run "$LOGS/base/scoped.txt" "$BASE_TREE" python3 -B verifiers/check_scoped_rules.py --self-test; rb=$RC
run "$LOGS/tip/scoped.txt"  "$TIP_TREE"  python3 -B verifiers/check_scoped_rules.py --self-test; rt=$RC
printf '%s %s\n' "$rb" "$rt" > "$LOGS/scoped.exits"
cmp_exit0 scoped

# ---- battery self-verification -------------------------------------------
# A battery that cannot fail is not a battery.  These arms mutate the tip
# column's own output and re-run the comparison.  If a mutated copy still
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
cp "$LOGS/tip/agentdefs.txt"  "$SELFCHECK_DIR/tip.txt"
norm_lane "$SELFCHECK_DIR/base.txt" > "$SELFCHECK_DIR/base.norm"
norm_lane "$SELFCHECK_DIR/tip.txt"  > "$SELFCHECK_DIR/tip.norm"
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
echo "INFO  (the C1 control the plan freezes is: tip counter code, --rev base -> exit 1; --rev tip -> exit 0)"

echo "--- verdict ---"
if [ "$FAILURES" -eq 0 ]; then
  echo "no-harm OK"
  exit 0
fi
echo "no-harm FAILED: $FAILURES arm(s) failed"
exit 1
```

---

## 3. The measurement — before-column and tip-column, verbatim

### 3.1 Command

```
cd /fast/scratch/hyaku/kotoba-r61/ExecNoHarm
NOHARM_LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin \
  timeout 3000 bash noharm-battery.sh \
    --base f3246d1493b60ea1c0d947a19c39f9e08e92f326 \
    --tip  7827628a939b0333c89892dfcedc72e390ccfb60 \
    --sandbox /fast/scratch/hyaku/kotoba-r61/ExecNoHarm/sbx6 --keep
```

`date -u` at start: `2026-10-23T19:35:10Z`. Wall: 176.30 s. Exit code: **1**.

### 3.2 Output, pasted

```
noharm: lane        /home/vgpnk/Projects/shokunin/kotoba-shokunin
noharm: base        f3246d1493b60ea1c0d947a19c39f9e08e92f326
noharm: tip         7827628a939b0333c89892dfcedc72e390ccfb60
noharm: sandbox     /fast/scratch/hyaku/kotoba-r61/ExecNoHarm/sbx6
noharm: date -u     2026-10-23T19:35:10Z
noharm: column base ready (f3246d1493b60ea1c0d947a19c39f9e08e92f326)
noharm: column tip ready (7827628a939b0333c89892dfcedc72e390ccfb60)
--- arms ---
FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1
        tip: verifiers/check_routed_repairs.py            no registry rows naming it: 0 (need 1)
        tip: gate registry rows conformant 34 of 35 lane verifiers; phantom 0
PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
PASS  corpus-idx  no new unindexed corpus file at tip (base set: corpus/lessons/round-60-verifier-spotcheck.md )
PASS  sources     exit 0 in both columns (base=0 tip=0)
PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
PASS  check-ptr   unresolved citation pointers did not grow (base=2 tip=2)
PASS  boxproof    exit 0 in both columns (base=0 tip=0)
PASS  floors      exit 0 in both columns (base=0 tip=0)
PASS  agentdefs   exit 0 and normalized output identical in both columns
PASS  explicit    exit 0 and normalized output identical in both columns
PASS  desc        exit 0 and normalized output identical in both columns
PASS  mcp         exit 0 and normalized output identical in both columns
PASS  plugin      exit 1 and normalized output identical in both columns
PASS  hooks       exit 0 and normalized output identical in both columns
PASS  scoped      exit 0 in both columns (base=0 tip=0)
PASS  battery-self a mutated verdict line was detected by the comparison (battery is not vacuous)
PASS  battery-self2 an injected new corpus DRIFT kind was detected by the comparison
PASS  battery-self3 an exit-2 (could-not-evaluate) column is caught by the comparison guard
--- informational ---
INFO  routed-repairs (C2 predicate; the L1 measures it) exit=1: routed repairs verified 0 of 6
INFO  scoped-rules self-test at tip: self-test: 0 failure(s) over 318 assertions
INFO  scoped-rules --rev tip  --fetch: exit=0: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
INFO  scoped-rules --rev base --fetch: exit=0: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
INFO  (the C1 control the plan freezes is: tip counter code, --rev base -> exit 1; --rev tip -> exit 0)
--- verdict ---
no-harm FAILED: 1 arm(s) failed
```

Exit code of the battery: **1**. `BATTERY_EXIT=1`.

### 3.3 What each arm measured, and the raw base-column output

The arms the assignment names, and the raw output each produced at **base** `f3246d14`:

**`reg_gate` — `python3 -B verifiers/check_gate_registry.py --rev f3246d14`** — exit 0, 34 of 34:

```
verifiers/box_proof_case_deletion.py         OK
verifiers/check_agent_definitions.py         OK
verifiers/check_agentdef_boxes.py            OK
verifiers/check_alwayson_boxes.py            OK
verifiers/check_assertion_floors.py          OK
verifiers/check_callee_rename.py             OK
verifiers/check_command_files.py             OK
verifiers/check_correction_sweep.py          OK
verifiers/check_could_not_evaluate.py        OK
verifiers/check_description_thresholds.py    OK
verifiers/check_explicit_invocation.py       OK
verifiers/check_gate_finding_delta.py        OK
verifiers/check_gate_registry.py             OK
verifiers/check_hook_files.py                OK
verifiers/check_infoless_fences.py           OK
verifiers/check_mcp_instructions.py          OK
verifiers/check_opencode_repin.py            OK
verifiers/check_overlap_levers.py            OK
verifiers/check_plugin_manifests.py          OK
verifiers/check_scoped_rules.py              OK
verifiers/check_sibling_census.py            OK
verifiers/check_sources_append_only.py       OK
verifiers/check_substrate_pins.py            OK
verifiers/check_sweep_mutants.py             OK
verifiers/compare_harness_independent.py     OK
verifiers/fault_injection_corpus.sh          OK
verifiers/verify_alwayson.py                 OK
verifiers/verify_corpus_independent.py       OK
verifiers/verify_corpus_integrity.py         OK
verifiers/verify_dispatch_prompts.py         OK
verifiers/verify_harness_claims.py           OK
verifiers/verify_harness_independent.py      OK
verifiers/verify_skill_checklist.py          OK
verifiers/verify_surfaces.py                 OK
gate registry rows conformant 34 of 34 lane verifiers; phantom 0
```

**`corpus` — `python3 -B verifiers/verify_corpus_integrity.py`** (tree gate, base tree) — exit 1,
4 of 9 checks pass, 5 DRIFT (all pre-existing at base; identical DRIFT-kind set at tip):

```
corpus.index    tracked=100 unindexed=1 stale=0 missing=0  (117 FILE-column patterns over 99 md files)
corpus.pointers report_dead=0/67 commit_total=34 unresolvable=1 nonhash=0 …
           unindexed: corpus/lessons/round-60-verifier-spotcheck.md
DRIFT   corpus.index.tracked_files: observed=100 expected=81
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=67 expected=51
DRIFT   corpus.pointers.commit_total: observed=34 expected=32
DRIFT   corpus.pointers.commit_unresolvable: observed=1 expected=0 / empty
4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
```

**`sources` — `python3 -B verifiers/check_sources_append_only.py --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --rev f3246d14`** — exit 0:

```
log  5a097e12b S046 used-by: …les-round53.md -> …les-round53.md, corpus/l…
log  6de8e2eb4 S028 used-by: …les-round50.md -> …les-round50.md, corpus/k…
sources append-only rows clean: 9 commits scanned, 0 protected-cell changes
```

**`checklist` — `python3 -B verifiers/verify_skill_checklist.py`** (tree gate, base tree) — exit 1,
one failing check id, `governance.citation_resolves` (pre-existing; the two pointers are
`.ufo/reports/round-60/kotoba.md` cited from `LOG.md:2533` and `SCORECARD.md:156`, which live in
the **fleet** report tree, not the lane's):

```
PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 4 delegated, 29 unexecuted); delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2; delegated verifiers/verify_alwayson.py: --box-proof exit 0: boxes proven 2
PASS trigger.frontmatter_parses: evaluated 4 — frontmatter parses: name='kotoba-shokunin', description 1019 chars
PASS trigger.name_directory: evaluated 1 — name 'kotoba-shokunin' == directory 'kotoba-shokunin'
PASS trigger.literal_trigger_string: evaluated 1 — description carries literal 'Triggers:'
PASS trigger.anti_trigger_clause: evaluated 1 — exclusion marker 'Anti-triggers' present …
PASS trigger.no_xml_tag: evaluated 2 — no XML tag in name, description …
PASS trigger.line_budget: evaluated 591 — 591 lines within budget 600 (from box at line 320)
PASS trigger.no_placeholder: evaluated 524 — no placeholder markers in 524 scanned lines
PASS trigger.command_binary_resolves: evaluated 34 — 19 segments; 34 command subject(s) resolve
PASS trigger.citation_resolves: evaluated 145 — 145 repo-rooted citation token(s) resolve from the repo root
FAIL governance.citation_resolves: evaluated 1101 — LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve from <lane>; SCORECARD.md:156: '.ufo/reports/round-60/kotoba.md' does not resolve from <lane>; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused
```

**`boxproof` — `python3 -B verifiers/box_proof_case_deletion.py --rev f3246d14`** — exit 0:

```
control: exit 0 boxes proven 2
fixtures: --fixtures
case d04-placeholder (report_path_literal): exit 1 killed
case d04-stem (report_stem_is_lane_id): exit 1 killed
case d04-unknown-lane (lane_identity_known): exit 1 killed
case d08-role-round (filename_role_round_equal): exit 1 killed
case d08-report-dir-round (filename_report_dir_round_equal): exit 1 killed
case d08-above-state (round_le_latest_dispatched): exit 1 killed
control d04-control: exit 1 killed
control d08-control: exit 1 killed
na d08-missing-state: exit 1 killed
controls killed 2 of 2
na killed 1 of 1
killed 6 of 6
```

**`floors` — `python3 -B verifiers/check_assertion_floors.py`** (tree gate, base tree) — exit 0,
14 floors (wall 102.04 s):

```
PASS harness observed=10 floor=10
PASS corpus_integrity observed=152 floor=152
PASS corpus_independent observed=99 floor=93
PASS surfaces observed=175 floor=175
PASS checklist observed=1852 floor=1852
PASS pins observed=62 floor=62
PASS harness_independent observed=123 floor=123
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=165 floor=150
PASS dispatch_prompts observed=56 floor=56
PASS sibling_census observed=68 floor=68
PASS overlap_levers observed=55 floor=51
PASS alwayson observed=89 floor=89
PASS correction_sweep observed=25 floor=25
```

**`agentdefs` — `python3 -B verifiers/check_agent_definitions.py --rev f3246d14 --fetch`** — exit 0,
7 of 7:

```
agent-definition locations found on the live page 7 of 7; new ground 3
Claude Code  BACKED token=.claude/agents/ norm=.claude/agents found=yes base_count=3
Codex        BACKED token=.codex/agents/ norm=.codex/agents found=yes base_count=5
VS Code      BACKED token=.github/agents norm=.github/agents found=yes base_count=0
Copilot CLI  BACKED token=.github/agents/ norm=.github/agents found=yes base_count=0
Gemini CLI   BACKED token=.gemini/agents/*.md norm=.gemini/agents found=yes base_count=0
Cursor       BACKED token=.cursor/agents norm=.cursor/agents found=yes base_count=0
opencode     BACKED token=.opencode/agents norm=.opencode/agents found=yes base_count=10
```

**`explicit` — `python3 -B verifiers/check_explicit_invocation.py --rev f3246d14 --fetch`** — exit 0,
5 of 5:

```
Claude Code  BACKED token=/skill-name new=False found=True
Codex        BACKED token=$setup-demo-app new=True found=True
VS Code      no quote does not contain the word skill
Copilot CLI  BACKED token=/frontend-design new=True found=True
Gemini CLI   no SKILL.md form cell has no backticked invocation token
Cursor       BACKED token=/skill-name new=True found=True
opencode     BACKED token=@skill-id new=True found=True
user-typed invocation forms found on the live page 5 of 5; new ground 4
```

**`desc` — `python3 -B verifiers/check_description_thresholds.py --rev f3246d14 --fetch`** — exit 0,
7 of 7 clients:

```
Claude Code  BACKED found=True
Codex        BACKED found=True
VS Code      BACKED found=True
Copilot CLI  BACKED found=True
Gemini CLI   BACKED found=True
Cursor       BACKED found=True
opencode     BACKED found=True
description thresholds backed 7 of 7 clients
description thresholds found on the live page 7 of 7
```

**`mcp` — `python3 -B verifiers/check_mcp_instructions.py --rev f3246d14 --fetch`** — exit 0, 7 of 7:

```
MCP specification  BACKED found=True
Claude Code        BACKED found=True
VS Code            BACKED found=True
Codex              BACKED found=True
Gemini CLI         BACKED found=True
opencode           BACKED found=True
Copilot CLI        BACKED found=True
mcp instructions backed 7 of 7 clients
mcp instructions found on the live page 7 of 7
```

**`plugin` — `python3 -B verifiers/check_plugin_manifests.py --rev f3246d14 --fetch`** — exit **1**
(pre-existing r57 miss: VS Code and Copilot CLI share the root `plugin.json`; opencode has no JSON
manifest — `LOG.md:2493`), identical output at tip:

```
counter sha256 7cefb99751b948c2d7f24e68b245f28ecaf5e8a9a116b55a1c5ab191ed47cdd6
counter rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
```

**`hooks` — `python3 -B verifiers/check_hook_files.py --rev f3246d14 --fetch`** — exit 0, 6 of 6:

```
hook files backed on committed snapshots 6 of 6; found on the live page 6 of 6; new ground 6
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
reject opencode: SKILL.md hook config cell holds no backticked token; no entry row names the client
```

**`scoped` — `python3 -B verifiers/check_scoped_rules.py --self-test`** — exit 0 in both columns
(v2 at base and at tip — the v3 rewrite has not landed yet):

```
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions
```

---

## 4. The one live finding — a missing gate-registry row for the C2 counter

**What.** `verifiers/check_routed_repairs.py` was committed by the round-61 plan freeze
(`7827628a`). `SKILL.md` § Gate registry has 34 rows; `verifiers/` at that rev holds 35 `.py`/`.sh`
files. The registry gate's universe is every `.py`/`.sh` blob under `verifiers/` at the measured
rev (`verifiers/check_gate_registry.py:118-129`, `Tree.universe()`), and each needs exactly one
row (`judge()`, `:225-235`).

**Evidence (command, output, date -u, exit code):**

```
$ date -u
Fri 23 Oct 2026 07:39:09 PM UTC
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/check_gate_registry.py --rev 7827628a939b0333c89892dfcedc72e390ccfb60
...
verifiers/check_routed_repairs.py            no registry rows naming it: 0 (need 1)
gate registry rows conformant 34 of 35 lane verifiers; phantom 0
exit=1
```

Set difference, measured:

```
$ ls verifiers/*.py verifiers/*.sh | sed 's|verifiers/||' | sort > /tmp/vfiles.txt
$ grep '^| `verifiers/' SKILL.md | awk -F'`' '{print $2}' | sed 's|verifiers/||' | sort > /tmp/vrows.txt
$ diff /tmp/vfiles.txt /tmp/vrows.txt
20d19
< check_routed_repairs.py
diffexit=1
```

At the **base** rev `f3246d14` the same diff is empty (34 files, 34 rows, exit 0) — the counter
did not exist yet. So the red is *introduced by the round-61 plan freeze commit*, and it will
persist through the integration commits unless the L1 lands the row.

**The exact row that repairs it** (insert in `SKILL.md` § Gate registry, in the table, e.g.
directly after the `verifiers/check_scoped_rules.py` row):

```
| `verifiers/check_routed_repairs.py` | gate | `python3 -B verifiers/check_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |
```

**Measured proof that this row is conformant.** I cloned the lane at `7827628a`, inserted exactly
that row, committed it in the clone, and ran the registry gate against the new commit:

```
$ git -c user.name=t -c user.email=t@t commit -qam "test: add routed repairs registry row"
$ python3 -B verifiers/check_gate_registry.py --rev b5b496b0c434f5284bfaf34c1b9677bd0d4bb5c0
...
gate registry rows conformant 35 of 35 lane verifiers; phantom 0
exit=0
```

And with that row in place, the whole battery goes green (§5). I did **not** commit anything to the
lane: the test clone lives entirely under `/fast/scratch/hyaku/kotoba-r61/ExecNoHarm/rowtest/`.

**Line-budget note for the L1.** `SKILL.md` is 591 lines and the trigger box at `SKILL.md:320`
reads `File ≤ 600 lines` — 9 lines of headroom. One registry row costs one line. Fine.

**Why this matters beyond the registry gate.** The C2 counter is the one the plan freezes as
`verifiers/check_routed_repairs.py` with a committed base control. If the integration leaves the
registry red, then `check_gate_registry.py --rev <tip>` is red at the tip, and the L1's
integration measurement inherits a red gate that no round-61 work caused but that round-61
committed. Round 60 recorded exactly this for the round-60 counter
(`.ufo/waves/round-60/build/ExecNoHarmBase.md` § findings, item 2: "The gate-registry gate is RED
at every rev that carries the new counter, and green at the base"). This time it was not
re-routed, so the L1 should close it in the integration commit, not leave it to the next round.

---

## 5. The green path — proof that `no-harm OK` is reachable

The battery must print `no-harm OK` only when all pass, and it must be *able* to print it. I
verified this by running the identical script against a simulated post-integration tip: the clone
from §4 with the registry row committed (`b5b496b0`).

```
$ date -u   # run start 2026-10-23T19:31:33Z (from the preserved sandbox's first
            # artifact mtime, sbx5/logs/base created 16:31:33 -0300); wall 195.60 s;
            # last artifact written 2026-10-23T19:34:48Z (sbx5/logs mtime)
$ NOHARM_LANE=/fast/scratch/hyaku/kotoba-r61/ExecNoHarm/rowtest/kotoba-shokunin \
    bash noharm-battery.sh --base f3246d14… --tip b5b496b0… --sandbox …/sbx5 --keep
noharm: column tip ready (b5b496b0c434f5284bfaf34c1b9677bd0d4bb5c0)
--- arms ---
PASS  reg_gate    exit 0 in both columns (base=0 tip=0)
PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
PASS  corpus-idx  no new unindexed corpus file at tip (base set: corpus/lessons/round-60-verifier-spotcheck.md )
PASS  sources     exit 0 in both columns (base=0 tip=0)
PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
PASS  check-ptr   unresolved citation pointers did not grow (base=2 tip=2)
PASS  boxproof    exit 0 in both columns (base=0 tip=0)
PASS  floors      exit 0 in both columns (base=0 tip=0)
PASS  agentdefs   exit 0 and normalized output identical in both columns
PASS  explicit    exit 0 and normalized output identical in both columns
PASS  desc        exit 0 and normalized output identical in both columns
PASS  mcp         exit 0 and normalized output identical in both columns
PASS  plugin      exit 1 and normalized output identical in both columns
PASS  hooks       exit 0 and normalized output identical in both columns
PASS  scoped      exit 0 in both columns (base=0 tip=0)
PASS  battery-self a mutated verdict line was detected by the comparison (battery is not vacuous)
--- verdict ---
no-harm OK
```

Exit code **0**. `BATTERY_EXIT=0`.

So the battery's verdict line is reachable and is not a constant.

### 5.1 Post-fix verification against the L1's own integration commit

After this report was filed, the L1 landed the §4 row as
`cf288d84b1a6f128855ccf92178404c6a53e7bdf` — "round-61: gate registry row for
check_routed_repairs.py (ExecNoHarm gate-verified text; closes the 34/35 red the freeze
introduced)", `SKILL.md | 1 +`, one insertion. The landed row is **byte-identical** to the row I
measured in §4:

```
$ git show cf288d84 -- SKILL.md | grep '^+' | grep routed_repairs
+| `verifiers/check_routed_repairs.py` | gate | `python3 -B verifiers/check_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |
```

The battery re-run against that real integration commit — not a simulation — prints `no-harm OK`
and exits 0. Command, `date -u`, wall, exit code:

```
$ date -u   # run start 2026-10-23T19:40:33Z (from the script's own banner)
$ NOHARM_LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin \
  timeout 3000 bash noharm-battery.sh \
    --base f3246d1493b60ea1c0d947a19c39f9e08e92f326 \
    --tip  cf288d84b1a6f128855ccf92178404c6a53e7bdf \
    --sandbox /fast/scratch/hyaku/kotoba-r61/ExecNoHarm/sbx7 --keep
noharm: lane        /home/vgpnk/Projects/shokunin/kotoba-shokunin
noharm: base        f3246d1493b60ea1c0d947a19c39f9e08e92f326
noharm: tip         cf288d84b1a6f128855ccf92178404c6a53e7bdf
noharm: sandbox     /fast/scratch/hyaku/kotoba-r61/ExecNoHarm/sbx7
noharm: date -u     2026-10-23T19:40:33Z
noharm: column base ready (f3246d1493b60ea1c0d947a19c39f9e08e92f326)
noharm: column tip ready (cf288d84b1a6f128855ccf92178404c6a53e7bdf)
--- arms ---
PASS  reg_gate    exit 0 in both columns (base=0 tip=0)
PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
PASS  corpus-idx  no new unindexed corpus file at tip (base set: corpus/lessons/round-60-verifier-spotcheck.md )
PASS  sources     exit 0 in both columns (base=0 tip=0)
PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
PASS  check-ptr   unresolved citation pointers did not grow (base=2 tip=2)
PASS  boxproof    exit 0 in both columns (base=0 tip=0)
PASS  floors      exit 0 in both columns (base=0 tip=0)
PASS  agentdefs   exit 0 and normalized output identical in both columns
PASS  explicit    exit 0 and normalized output identical in both columns
PASS  desc        exit 0 and normalized output identical in both columns
PASS  mcp         exit 0 and normalized output identical in both columns
PASS  plugin      exit 1 and normalized output identical in both columns
PASS  hooks       exit 0 and normalized output identical in both columns
PASS  scoped      exit 0 in both columns (base=0 tip=0)
PASS  battery-self a mutated verdict line was detected by the comparison (battery is not vacuous)
PASS  battery-self2 an injected new corpus DRIFT kind was detected by the comparison
PASS  battery-self3 an exit-2 (could-not-evaluate) column is caught by the comparison guard
--- informational ---
INFO  routed-repairs (C2 predicate; the L1 measures it) exit=1: routed repairs verified 0 of 6
INFO  scoped-rules self-test at tip: self-test: 0 failure(s) over 318 assertions
INFO  scoped-rules --rev tip  --fetch: exit=0: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
INFO  scoped-rules --rev base --fetch: exit=0: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
INFO  (the C1 control the plan freezes is: tip counter code, --rev base -> exit 1; --rev tip -> exit 0)
--- verdict ---
no-harm OK
```

Wall 191.03 s. Exit code **0**. `BATTERY_EXIT=0`.

**The finding in §4 is closed and verified against the lane's own committed bytes** — not against
my simulation. The remaining `INFO` lines are the claims' own arms: the C2 counter still reads
`0 of 6` because the six routed repairs are not landed yet, and the scoped-rules counter is
still v2 (318 assertions) because the v3 draft has not landed. Both are the L1's integration
measurement, not the battery's verdict.

---

## 6. Which arms need the landed v3 and must therefore run at integration

| arm | runs clean at base NOW? | runs at integration? |
|---|---|---|
| `reg_gate` | base exit 0 / 34 of 34; **tip red 34 of 35** | yes — needs the §4 row landed |
| `corpus` (DRIFT kind, unindexed set) | yes (both columns red at the same 5 DRIFT kinds — pre-existing) | yes — the tip column's DRIFT set will grow as new corpus files land; the arm compares *kinds*, not counts |
| `corpus-idx` (unindexed file set) | yes (base set = {`corpus/lessons/round-60-verifier-spotcheck.md`}) | yes — the new round-61 lesson/entry files must be indexed in `corpus/README.md` or this arm fails |
| `sources` (append-only, base `422ffd10…`) | yes, exit 0 both columns | yes — **this is the C3 arm**: appending S117 must not touch a protected cell |
| `checklist` (failing check id + pointer count) | yes (base red on `governance.citation_resolves`, 2 pointers) | yes — the count must not grow |
| `boxproof` | yes, exit 0 both columns | yes |
| `floors` | yes, exit 0 both columns, 14 floors | yes — if the round adds a counter, `verifiers/floors-registry.json` may need a floor entry; `ExecGateRegistry`'s item |
| `agentdefs` (7 of 7) | yes, exit 0 both columns | yes |
| `explicit` (5 of 5) | yes, exit 0 both columns | yes |
| `desc` (7 of 7) | yes, exit 0 both columns | yes |
| `mcp` (7 of 7) | yes, exit 0 both columns | yes |
| `plugin` (4 of 4, exit 1) | yes — exit 1 in **both** columns, identical output | yes |
| `hooks` (6 of 6) | yes, exit 0 both columns | yes |
| `scoped` (self-test green) | yes — v2 self-test green at base and tip (318 assertions) | yes — but at integration the counter is **v3**; the arm certifies only "still green", the v3 predicate is the C1 receipt's |
| `battery-self` / `self2` / `self3` | yes — all three PASS | yes |

**What the battery does NOT do, deliberately.** It does not measure the C1 predicate
(`worlds reject 7 of 7; eligible rows pass 4 of 4`), the C2 predicate (`routed repairs verified
6 of 6`), or the C3 count (`grep -c 'self-assessment-at-writing' corpus/SOURCES.md` = 1). Those are
the claims' own arms, owned by the C1/C2/C3 seats and the L1's integration measurement. The
battery prints the C1 and C2 predicate lines as `INFO` so the L1 can read them from one run
without a second command, but it does not gate on them — a no-harm battery that also judges the
claims it is supposed to protect is not a no-harm battery.

**The one thing the L1 must do for the battery to be runnable at integration:** land it at
`.ufo/waves/round-61/noharm-battery.sh` (the script finds the lane root by walking up from its
own directory to the first ancestor with `SKILL.md` + `verifiers/`, so it works from either
`.ufo/waves/round-61/` or a deeper path). Then run it with `--tip HEAD`.

---

## 7. Risks, honesty notes, and what I could not verify

**Pre-existing red is not round-61 harm — but the L1 should read the reds.**
- `verify_corpus_integrity.py` is **red at base** (exit 1, 5 DRIFT). The battery compares the
  DRIFT-*kind* set, so a round-61 file that introduces a *new* kind of drift fails the arm; a
  round-61 file that merely changes a count (more tracked files, more report pointers) does not.
  That is the right line to draw for a no-harm check, but it means "corpus PASS" does not mean
  "corpus green".
- `verify_skill_checklist.py` is **red at base** (`governance.citation_resolves`, 2 pointers at
  `LOG.md:2533` and `SCORECARD.md:156`). Those pointers name `.ufo/reports/round-60/kotoba.md`,
  which lives in the **fleet** report tree (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotoba.md`),
  not in the lane's `.ufo/reports/` (the lane carries rounds 20–48 only). The checklist resolves
  repo-rooted tokens from the lane root, so it cannot see the fleet copy. Pre-existing; not mine
  to fix; the L1 may want to route it.
- `check_plugin_manifests.py` is **red at base** (exit 1). Unchanged in behavior. Consistent with
  `LOG.md:2493` (the r57 miss) and with `.ufo/waves/round-58/falsify/NoHarmGates.md`.

**Things I did not verify, and why.**
- I did **not** measure the C1 v3 predicate, the C2 six-of-six count, or the C3 SOURCES count.
  The v3 counter does not exist yet; the C2 repairs are not landed; the C3 row is not appended.
  Those are the claims' arms, not mine.
- I did **not** run the round-60 no-harm receipt's full 33-gate `--self-test` sweep. The battery
  covers the arms the assignment names (the seven prior-round counters plus the five structural
  gates), which is a different and narrower set. If the L1 wants the whole registered column,
  `.ufo/waves/round-60/receipts/noharm-base-selftests.txt` is the recipe to copy.
- The `--fetch` arms read the live vendor documentation pages, so they are network-dependent.
  I verified the network is reachable from this host (`curl -sS -o /dev/null -w '%{http_code}\n'
  https://code.claude.com/docs/en/skills.md` → `200`, exit 0). I added the exit-2 guard so a
  network outage **fails** the arm rather than reading as a pass, and the `lane_only` pass so an
  upstream doc edit between the two column runs cannot be mistaken for a lane regression. The
  per-client BACKED/reject verdict lines — the part that comes from the committed SKILL.md — are
  still compared exactly.
- **The live-page numerator** (`found on the live page 7 of 7`) is dropped by the `lane_only`
  pass; the denominator (the number of clients the lane claims) and every per-client verdict are
  compared exactly. This is a deliberate loosening, disclosed here.
- I did **not** run `scripts/hyaku/jj-lane.sh` or any other lane-writing command. My lane state is
  untouched; `git status --porcelain` in the lane shows only the other wave seats' untracked
  report files under `.ufo/waves/round-61/wave/` (not mine).

**Scope note.** `scripts/hyaku-adjacent` was not mine and was not touched. The battery is
delivered as the *content* of `.ufo/waves/round-61/noharm-battery.sh` for the L1 to land, per the
assignment.

**Scratch is untrusted and is not cited as evidence.** Everything under
`/fast/scratch/hyaku/kotoba-r61/ExecNoHarm/` (sandboxes `sbx1`–`sbx6`, the row-test clone
`rowtest/`, the runner script) is scratch. The evidence in this report is the command, its pasted
output, the `date -u` stamp, and the exit code, all reproducible from the lane.

---

## 8. Handoff to the L1

1. ~~**Land the registry row** (§4)~~ — **DONE**: landed as `cf288d84` (byte-identical to the
   measured text); the battery re-run against it prints `no-harm OK`, exit 0 (§5.1).
2. **Land the battery** at `.ufo/waves/round-61/noharm-battery.sh` (full text in §2; sha256
   `ddeaa1313ead419d562b16d9a256595507cbd49c8069fbdc7531ce3fb51dd32b`). Not yet landed — the L1
   owns it.
3. **Re-run it at final integration** with `--tip HEAD` and paste the output into the round
   receipt. The last line must be `no-harm OK` for the round to close on the operability axis.
   Note the battery's arms are tip-sensitive: when the C1 v3 counter lands, the `scoped` arm's
   self-test must still exit 0 (it will, if the v3 draft is sound); when the C2 repairs and the
   C3 row land, the `sources`, `corpus-idx` and `routed-repairs` arms move.
4. **Read the two `INFO` lines** the battery prints: they carry the C1 self-test line and the C2
   routed-repairs count from the same run, so the L1 need not re-run those two commands.

---

**Installs:** none. No tool was installed or upgraded by this seat; the battery uses only `bash`,
`git`, `grep`/`sed`/`awk`/`diff`/`comm` (all present on the host) and the lane's own Python 3.14.8
verifiers. Per the operator's tooling directive (2026-10-19) and the pacman guard (orchestrator
ruling 2026-10-20, all pacman transactions PAUSED host-wide), nothing was installed: the task
required no new tool, so the `uv tool`/`npx`/official-binary channels were not exercised either.

**Blockers:** none. The one live finding (§4) is a defect in the lane's committed bytes, not a
blocker for this seat; the L1 can fix it with a one-line registry row whose exact text and whose
measured effect are both recorded above.

**What this seat attacked/produced:** produced the round-61 no-harm battery (one runnable script,
16 arms + 3 self-verification arms, proven red at the pre-fix tip and green against the L1's own
integration commit `cf288d84`) and attacked it against the lane's committed bytes, which surfaced
exactly one live defect — the C2 counter `verifiers/check_routed_repairs.py` had no `SKILL.md` §
Gate registry row, leaving `check_gate_registry.py` red (34 of 35) at every revision from the
round-61 plan freeze onward; the L1 landed the measured one-line row and the battery now prints
`no-harm OK`.
