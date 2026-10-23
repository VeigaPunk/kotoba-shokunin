#!/usr/bin/env bash
# fault_injection_corpus.sh — landable fault-injection harness for the corpus
# instruments (round 12). Plants exactly one fault per throwaway clone of this
# repo, runs both corpus instruments in the clone, and asserts on the JSON.
#
# Gating model (what "PASS" means here):
#   * must-fire faults (a,b,c,d1,d2,e) — the author's instrument must exit non-zero
#     with its intended check id in DRIFT, and the independent instrument (when
#     present) must exit non-zero too; both rows are gating.
#   * (f) is the class's documented BLIND SPOT, not a must-fire: a pointer moved
#     OUT of the .ufo/reports/round-N/ grammar stops being a pointer, so neither
#     tokenizer can flag it. PASS means the author's instrument exits 0 under
#     --no-baseline (faithfully blind) AND the equal-mode count detector notices
#     report_total against the baseline.
#   * must-not-fire mutations (g) must exit 0 in both instruments.
#   * (h) must not fire as a promise, and must be RECORDED as context: the author's
#     instrument has to report report_pointers_quoted +1 with the checked
#     population unchanged (exit 0 alone would also pass if the token vanished
#     from every key).
#
# Usage:
#   fault_injection_corpus.sh [--repo DIR] [--keep-worlds] [--self-test]
#     --repo DIR     target repo (default: this script's grandparent)
#     --keep-worlds  keep the per-fault clone worlds (default: remove)
#     --self-test    verify the assertion machinery on deliberately broken
#                    fixture worlds, then exit (0 ok / 1 broken)
#
# Exit codes: 0 every verdict PASS/SKIP · 1 any verdict FAIL/MISS/WRONG-CLASS/
# FALSE-POSITIVE/INVALID-PLANT · 2 environment unreadable.
# Worlds live under ${TMPDIR:-/tmp}/round12-faults.$$ and are removed on exit
# unless --keep-worlds. Dependencies: bash, git, python3, coreutils. No network.
# Deterministic output: fixed fault order, LC_ALL=C.
set -u
export LC_ALL=C

SELF=$0
SCRIPT_DIR=$(cd "$(dirname "$SELF")" && pwd) || exit 2
REPO=$(cd "$SCRIPT_DIR/.." && pwd) || exit 2
KEEP=0
SELFTEST=0
while [ $# -gt 0 ]; do
  case $1 in
    --repo)      [ $# -ge 2 ] || { echo "usage: $1 needs a value" >&2; exit 2; }; REPO=$(cd "$2" 2>/dev/null && pwd) || { echo "cannot read --repo: $2" >&2; exit 2; }; shift 2 ;;
    --repo=*)    REPO=$(cd "${1#*=}" 2>/dev/null && pwd) || { echo "cannot read $1" >&2; exit 2; }; shift ;;
    --keep-worlds) KEEP=1; shift ;;
    --self-test) SELFTEST=1; shift ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

INSTRUMENT=verifiers/verify_corpus_integrity.py
INDEPENDENT=verifiers/verify_corpus_independent.py
WORLDS=${TMPDIR:-/tmp}/round12-faults.$$
mkdir -p "$WORLDS" || exit 2
cleanup() { [ "$KEEP" = 1 ] || rm -rf "$WORLDS"; }
trap cleanup EXIT INT TERM

# --- environment guards (exit 2) -------------------------------------------
command -v python3 >/dev/null 2>&1 || { echo "env unreadable: python3 not found" >&2; exit 2; }
command -v git     >/dev/null 2>&1 || { echo "env unreadable: git not found" >&2; exit 2; }
git -C "$REPO" rev-parse --git-dir >/dev/null 2>&1 || { echo "env unreadable: not a git repo: $REPO" >&2; exit 2; }
[ -f "$REPO/$INSTRUMENT" ] || { echo "env unreadable: missing $REPO/$INSTRUMENT" >&2; exit 2; }
[ -d "$REPO/corpus" ]       || { echo "env unreadable: missing $REPO/corpus" >&2; exit 2; }

INSTRUMENT_SHA=$(sha256sum "$REPO/$INSTRUMENT" | awk '{print $1}')
REPO_HEAD=$(git -C "$REPO" rev-parse --short=7 HEAD 2>/dev/null || echo none)
if [ -f "$REPO/$INDEPENDENT" ]; then INDEP=present; else INDEP=absent; fi
FAIL=0

say() { printf '%s\n' "$*"; }

# --- world construction -----------------------------------------------------
new_world() { # <id> -> echoes world dir; clone carries committed state only,
              # the live (possibly uncommitted) instruments are copied over it
  local w="$WORLDS/$1"
  git clone --quiet --no-hardlinks "file://$REPO" "$w" >/dev/null 2>&1 \
    || git clone --quiet --no-hardlinks "$REPO" "$w" >/dev/null 2>&1 \
    || { echo "env unreadable: clone failed for $1" >&2; return 2; }
  git -C "$w" checkout --quiet --detach HEAD || return 2
  cp "$REPO/$INSTRUMENT" "$w/$INSTRUMENT" || return 2
  [ -f "$REPO/verifiers/corpus-baseline.json" ] && \
    cp "$REPO/verifiers/corpus-baseline.json" "$w/verifiers/corpus-baseline.json"
  [ "$INDEP" = present ] && cp "$REPO/$INDEPENDENT" "$w/$INDEPENDENT"
  printf '%s' "$w"
}

# --- exact-count text surgery (a no-op anchor aborts the plant) -------------
replace_once() { # <world> <relpath> <old> <new>
  python3 - "$1" "$2" "$3" "$4" <<'PY'
import sys
run, rel, old, new = sys.argv[1:5]
p = f"{run}/{rel}"
t = open(p, encoding="utf-8").read()
n = t.count(old)
assert n == 1, f"anchor not unique ({n}x) in {rel}: {old!r}"
open(p, "w", encoding="utf-8").write(t.replace(old, new, 1))
PY
}

append_text() { # <world> <relpath> <text>
  python3 - "$1" "$2" "$3" <<'PY'
import sys
run, rel, text = sys.argv[1], sys.argv[2], sys.argv[3]
p = f"{run}/{rel}"
t = open(p, encoding="utf-8").read()
with open(p, "a", encoding="utf-8") as fh:
    fh.write(text if (not t or t.endswith("\n")) else "\n" + text)
PY
}

insert_index_row() { # <world> <row> — after the last existing table row
  python3 - "$1" "$2" <<'PY'
import sys
run, row = sys.argv[1], sys.argv[2]
p = f"{run}/corpus/README.md"
lines = open(p, encoding="utf-8").read().splitlines(keepends=True)
start = next(i for i, l in enumerate(lines) if l.startswith("## Coverage map"))
end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
idx = max(i for i in range(start, end) if lines[i].startswith("|"))
lines.insert(idx + 1, row + "\n")
open(p, "w", encoding="utf-8").write("".join(lines))
PY
}

# --- instruments ------------------------------------------------------------
json_field() { # <world> <dotted.path> -> echoes the value, empty on failure
  python3 - "$1/out.json" "$2" <<'PY'
import json, sys
try:
    raw = open(sys.argv[1], encoding="utf-8").read()
    d = json.loads(raw[raw.find("{"):])
    for part in sys.argv[2].split("."):
        d = d[part]
    print(d)
except Exception:
    print("")
PY
}

run_integrity() { # <world> -> echoes exit; captures out.json/err.txt
  local w=$1
  ( cd "$w" && python3 "$INSTRUMENT" --repo "$w" --no-baseline --json ) \
    >"$w/out.json" 2>"$w/err.txt"
  echo $?
}

run_independent() { # <world> -> echoes "skip" or exit code; writes indep.json
  local w=$1
  [ "$INDEP" = present ] || { echo skip; return 0; }
  ( cd "$w" && python3 "$INDEPENDENT" --repo "$w" --json ) >"$w/indep.json" 2>"$w/indep.err"
  echo $?
}

indep_drift_ids() { # <world> -> comma-joined DRIFT check ids, "-", or UNPARSEABLE
  python3 - "$1/indep.json" <<'PY'
import json, sys
try:
    raw = open(sys.argv[1], encoding="utf-8").read()
    d = json.loads(raw[raw.find("{"):])
    ids = [r["check"] for r in d["results"] if r["verdict"] == "DRIFT"]
    print(",".join(ids) if ids else "-")
except Exception:
    print("UNPARSEABLE")
PY
}

drift_ids() { # <world> -> comma-joined DRIFT check ids, "-", or UNPARSEABLE
  python3 - "$1/out.json" <<'PY'
import json, sys
try:
    raw = open(sys.argv[1], encoding="utf-8").read()
    d = json.loads(raw[raw.find("{"):])
    ids = [r["check"] for r in d["results"] if r["verdict"] == "DRIFT"]
    print(",".join(ids) if ids else "-")
except Exception:
    print("UNPARSEABLE")
PY
}

# --- fault planters: each mutates its world, then SELF-VERIFIES the plant
#     (grep the file / git state) so a no-op mutation can never masquerade as
#     a missed detection. Echo 0 when planted, 1 when not. --------------------

plant_a() { # dead report pointer in a tracked lesson
  append_text "$1" "corpus/lessons/round-3.md" \
"Fault injection (a): dead report pointer \`.ufo/reports/round-77/x.md\` (planted by $SELF).
" || return 1
  grep -qF '.ufo/reports/round-77/x.md' "$1/corpus/lessons/round-3.md"
}

plant_b() { # existing citation turned non-hash
  replace_once "$1" "corpus/lessons/round-4.md" 'commit `397b29c`' 'commit `round-99`' || return 1
  grep -qF 'commit `round-99`' "$1/corpus/lessons/round-4.md"
}

plant_c() { # fresh 7-hex token that must not resolve
  git -C "$1" cat-file -e 'deadbee^{commit}' 2>/dev/null && return 1 # vacuous if it resolves
  append_text "$1" "corpus/lessons/round-6.md" \
"Fault injection (c): commit \`deadbee\` (planted 7-hex token, expected unresolvable).
" || return 1
  grep -qF 'commit `deadbee`' "$1/corpus/lessons/round-6.md"
}

plant_d1() { # index row naming a nonexistent corpus file (missing path)
  insert_index_row "$1" '| Fault injection (d1) | `knowledge/gone-file-fault.md` | planted: no such corpus file |' || return 1
  grep -qF 'knowledge/gone-file-fault.md' "$1/corpus/README.md"
}

plant_d2() { # index row naming an on-disk but untracked file (stale pattern)
  printf 'Fault injection (d2).\n\nThis file exists on disk only; it is not added to the git index.\n' \
    >"$1/corpus/knowledge/untracked-fault.md" || return 1
  insert_index_row "$1" '| Fault injection (d2) | `knowledge/untracked-fault.md` | planted: exists on disk, untracked |' || return 1
  [ -f "$1/corpus/knowledge/untracked-fault.md" ] \
    && ! git -C "$1" ls-files corpus | grep -q untracked-fault \
    && grep -qF 'knowledge/untracked-fault.md' "$1/corpus/README.md"
}

plant_e() { # new tracked corpus file covered by no index row (git add, NO commit)
  printf 'Fault injection (e).\n\nThis file is tracked in the git index and covered by no corpus README row. It deliberately carries no report pointer and no commit citation.\n' \
    >"$1/corpus/knowledge/fault-injected-note.md" || return 1
  git -C "$1" add corpus/knowledge/fault-injected-note.md || return 1
  git -C "$1" ls-files corpus | grep -q fault-injected-note \
    && ! grep -qF 'fault-injected-note' "$1/corpus/README.md"
}

plant_f() { # resolving pointer moved one directory up, out of reports/
  local old=/home/vgpnk/Projects/shokunin/.ufo/reports/round-4/kotoba.md
  local new=/home/vgpnk/Projects/shokunin/.ufo/round-4/kotoba.md
  [ -e "$old" ] && [ ! -e "$new" ] || return 1 # vacuous if the host moved it
  replace_once "$1" "corpus/lessons/round-4.md" "$old" "$new" || return 1
  grep -qF '.ufo/round-4/kotoba.md' "$1/corpus/lessons/round-4.md" \
    && ! grep -qF '.ufo/reports/round-4/kotoba.md' "$1/corpus/lessons/round-4.md"
}

plant_g() { # EQUIVALENT MUTATION: reword citation-free prose; must NOT fire
  replace_once "$1" "corpus/lessons/round-1.md" \
    'telemetry exists to test against. Falsifiable' \
    'telemetry exists to test it against. Falsifiable' || return 1
  grep -qF 'test it against. Falsifiable' "$1/corpus/lessons/round-1.md" \
    && ! grep -qF 'test against. Falsifiable' "$1/corpus/lessons/round-1.md"
}

plant_h() { # double-quoted dead pointer: documented context; must NOT fire
  append_text "$1" "corpus/lessons/round-3.md" \
"Fault injection (h): quoted context \".ufo/reports/round-77/x.md\" must stay unchecked.
" || return 1
  grep -qF '".ufo/reports/round-77/x.md"' "$1/corpus/lessons/round-3.md"
}

# --- verdict layer (asserts on the JSON, never on prose) --------------------
# Table: fault | script | exit | fired-class | verdict

row() { # <fault> <script> <exit> <fired> <verdict>
  printf '%s | %s | %s | %s | %s\n' "$1" "$2" "$3" "$4" "$5"
  case $5 in
    PASS*|SKIP*) : ;;
    INFO*) : ;;
    *) FAIL=1 ;;
  esac
}

fault_must_fire() { # <id> <planter> <expected-class>
  local id=$1 planter=$2 cls=$3 w ex fired indep indep_fired verdict
  w=$(new_world "fault-$id") || { row "fault-$id" "world" "-" "-" "FAIL"; return 0; }
  if ! "$planter" "$w"; then
    row "fault-$id" "$id" "-" "-" "INVALID-PLANT"
    return 0
  fi
  ex=$(run_integrity "$w")
  fired=$(drift_ids "$w")
  indep=$(run_independent "$w")
  indep_fired=$(indep_drift_ids "$w")
  verdict=FAIL
  if [ "$ex" = 0 ]; then
    verdict=MISS
  elif ! printf '%s' "$fired" | grep -qF -- "$cls"; then
    verdict="WRONG-CLASS(expected=$cls)"
  elif [ "$indep" = skip ]; then
    # the independent instrument is absent: the author's class is still gating,
    # but the round's claim covers both — say so instead of implying parity.
    verdict="PASS(author-only; independent=absent)"
  elif [ "$indep" = 0 ]; then
    verdict="MISS(independent-verdict)"
  elif ! printf '%s' "$indep_fired" | grep -qF -- "$cls"; then
    verdict="WRONG-CLASS(independent expected=$cls got=${indep_fired:-none})"
  else
    verdict=PASS
  fi
  row "fault-$id" "integrity" "$ex" "$fired" "$verdict"
  row "fault-$id" "independent" "$indep" "$indep_fired" "$([ "$indep" = skip ] && echo SKIP || echo "INFO(gating)")"
}

# (f) is the class's documented blind spot, not a must-fire: a pointer moved OUT
# of the .ufo/reports/round-N/ grammar stops being a pointer, so neither
# tokenizer can flag it. PASS means: the author's instrument exits 0 under
# --no-baseline (faithfully blind) AND the equal-mode count detector notices
# report_total moving 1 down against the baseline. Anything else is a FAIL.
fault_known_blind_f() { # <id> <planter>
  local id=$1 planter=$2 w ex fired indep indep_fired base_ex blind_total ctl_w ctl_ex ctl_fired ctl_base_ex ctl_total delta verdict
  ctl_w=$(new_world "fault-$id-control") || { row "fault-$id" "world" "-" "-" "FAIL"; return 0; }
  ctl_ex=$(run_integrity "$ctl_w")
  ctl_fired=$(drift_ids "$ctl_w")
  ctl_total=$(json_field "$ctl_w" "observed.corpus.report_total")
  ( cd "$ctl_w" && python3 "$INSTRUMENT" --repo "$ctl_w" ) >"$ctl_w/out-baseline.txt" 2>&1
  ctl_base_ex=$?
  w=$(new_world "fault-$id") || { row "fault-$id" "world" "-" "-" "FAIL"; return 0; }
  if ! "$planter" "$w"; then
    row "fault-$id" "$id" "-" "-" "INVALID-PLANT"
    return 0
  fi
  ex=$(run_integrity "$w")
  fired=$(drift_ids "$w")
  indep=$(run_independent "$w")
  indep_fired=$(indep_drift_ids "$w")
  blind_total=$(json_field "$w" "observed.corpus.report_total")
  ( cd "$w" && python3 "$INSTRUMENT" --repo "$w" ) >"$w/out-baseline.txt" 2>&1
  base_ex=$?
  delta=""
  if [ -n "$ctl_total" ] && [ -n "$blind_total" ]; then
    delta=$(( ctl_total - blind_total ))
  fi
  verdict=FAIL
  if [ "$ctl_ex" = 0 ] && [ "$ctl_fired" = "-" ] && [ "$ex" = 0 ] && [ "$fired" = "-" ] && [ "$ctl_base_ex" = 0 ] && [ "$base_ex" = 1 ] && [ "$delta" = 1 ]; then
    verdict="PASS(blind-spot documented: control_total=$ctl_total plant_total=$blind_total delta=$delta; no-baseline exit 0; baseline-mode control exit $ctl_base_ex plant exit $base_ex)"
  fi
  row "fault-$id" "integrity" "$ex" "$fired" "$verdict"
  row "fault-$id" "independent" "$indep" "-" "$([ "$indep" = skip ] && echo SKIP || echo "INFO(non-gating)")"
}

# (h) must not fire as a promise AND must still be recorded as context: the
# author's instrument has to report report_pointers_quoted +1 with the checked
# population unchanged. The count assertion is the point — "exit 0" alone would
# pass even if the token had vanished from every key.
fault_h_context() { # <id> <planter>
  local id=$1 planter=$2 w ex fired quoted checked ctl_w ctl_ex ctl_fired ctl_quoted ctl_checked verdict
  ctl_w=$(new_world "fault-$id-control") || { row "fault-$id" "world" "-" "-" "FAIL"; return 0; }
  ctl_ex=$(run_integrity "$ctl_w")
  ctl_fired=$(drift_ids "$ctl_w")
  ctl_quoted=$(json_field "$ctl_w" "observed.corpus.report_pointers_quoted")
  ctl_checked=$(json_field "$ctl_w" "observed.corpus.report_total")
  w=$(new_world "fault-$id") || { row "fault-$id" "world" "-" "-" "FAIL"; return 0; }
  if ! "$planter" "$w"; then
    row "fault-$id" "$id" "-" "-" "INVALID-PLANT"
    return 0
  fi
  ex=$(run_integrity "$w")
  fired=$(drift_ids "$w")
  quoted=$(json_field "$w" "observed.corpus.report_pointers_quoted")
  checked=$(json_field "$w" "observed.corpus.report_total")
  verdict=FAIL
  if [ "$ex" = "$ctl_ex" ] && { [ "$ex" = 0 ] || [ "$ex" = 1 ]; } && [ "$fired" = "$ctl_fired" ] && [ "$fired" != UNPARSEABLE ] && [ -n "$ctl_quoted" ] && [ -n "$quoted" ] && [ "$quoted" = "$((ctl_quoted + 1))" ] && [ "$checked" = "$ctl_checked" ]; then
    verdict="PASS(context: quoted=$quoted, control=$ctl_quoted, checked=$checked unchanged)"
  fi
  row "fault-$id" "integrity" "$ex" "$fired" "$verdict"
}

fault_must_not_fire() { # <id> <planter>
  local id=$1 planter=$2 w ex fired indep indep_fired ctl_w ctl_ex ctl_fired ctl_indep ctl_indep_fired verdict
  ctl_w=$(new_world "fault-$id-control") || { row "fault-$id" "world" "-" "-" "FAIL"; return 0; }
  ctl_ex=$(run_integrity "$ctl_w")
  ctl_fired=$(drift_ids "$ctl_w")
  ctl_indep=$(run_independent "$ctl_w")
  ctl_indep_fired=$(indep_drift_ids "$ctl_w")
  w=$(new_world "fault-$id") || { row "fault-$id" "world" "-" "-" "FAIL"; return 0; }
  if ! "$planter" "$w"; then
    row "fault-$id" "$id" "-" "-" "INVALID-PLANT"
    return 0
  fi
  ex=$(run_integrity "$w")
  fired=$(drift_ids "$w")
  indep=$(run_independent "$w")
  indep_fired=$(indep_drift_ids "$w")
  verdict=FALSE-POSITIVE
  if [ "$ex" = "$ctl_ex" ] && { [ "$ex" = 0 ] || [ "$ex" = 1 ]; } && [ "$fired" = "$ctl_fired" ] && [ "$fired" != UNPARSEABLE ] && [ "$indep" = "$ctl_indep" ] && { [ "$indep" = skip ] || { { [ "$indep" = 0 ] || [ "$indep" = 1 ]; } && [ "$indep_fired" != UNPARSEABLE ] && [ "$indep_fired" = "$ctl_indep_fired" ]; }; }; then
    verdict="PASS(no new drift vs control)"
  fi
  row "fault-$id" "integrity" "$ex" "$fired" "$verdict"
  row "fault-$id" "independent" "$indep" "-" "$([ "$indep" = skip ] && echo SKIP || echo "INFO(gating)")"
}

control_clean() { # pristine world must stay clean, in both instruments
  local w ex fired indep verdict
  w=$(new_world "fault-0-control") || { row "fault-0-control" "world" "-" "-" "FAIL"; return 0; }
  ex=$(run_integrity "$w")
  fired=$(drift_ids "$w")
  indep=$(run_independent "$w")
  verdict=FAIL-control-dirty
  if [ "$ex" = 0 ] && [ "$fired" = "-" ] && { [ "$indep" = skip ] || [ "$indep" = 0 ]; }; then
    verdict=PASS
  fi
  row "fault-0-control" "integrity" "$ex" "$fired" "$verdict"
  row "fault-0-control" "independent" "$indep" "-" "$([ "$indep" = skip ] && echo SKIP || echo "INFO(gating)")"
}

# --- self-test: prove the assertion machinery can fail ----------------------
# T2 applies no mutation and must reproduce the control result; T1 plants (a)
# and must still fire; T3 plants the harmless (g) mutation and must preserve the
# control result; T4 proves the plant guard rejects the no-op world.
self_test() {
  local st=0 w ex fired ctl_w ctl_ex ctl_fired
  say "self-test: building fixture worlds under $WORLDS"

  ctl_w=$(new_world "selftest-control") || return 2
  ctl_ex=$(run_integrity "$ctl_w")
  ctl_fired=$(drift_ids "$ctl_w")
  if { [ "$ctl_ex" != 0 ] && [ "$ctl_ex" != 1 ]; } || [ "$ctl_fired" = UNPARSEABLE ]; then
    say "self-test control: FAIL (exit=$ctl_ex fired=$ctl_fired)"
    return 1
  fi

  w=$(new_world "selftest-t1") || return 2
  plant_a "$w"; ex=$(run_integrity "$w"); fired=$(drift_ids "$w")
  if [ "$ex" != 0 ] && printf '%s' "$fired" | grep -qF -- 'corpus.pointers.report_dead'
  then say "self-test T1 must-fire assertion fires on planted (a): PASS"; else say "self-test T1: FAIL"; st=1; fi

  w=$(new_world "selftest-t2")   # deliberately broken: NO mutation applied
  : ; ex=$(run_integrity "$w"); fired=$(drift_ids "$w")
  if [ "$ex" = "$ctl_ex" ] && [ "$fired" = "$ctl_fired" ]; then say "self-test T2 no-op world preserves control result (exit=$ex, fired=$fired): PASS"; else say "self-test T2: FAIL (exit=$ex fired=$fired; control=$ctl_ex/$ctl_fired)"; st=1; fi
  # T4: the plant guard must DISTINGUISH the unmutated world — the (a) marker
  # grep has to fail here, so a no-op mutation cannot masquerade as planted.
  if grep -qF '.ufo/reports/round-77/x.md' "$w/corpus/lessons/round-3.md"
  then say "self-test T4 plant guard accepted an unmutated world: FAIL"; st=1
  else say "self-test T4 plant guard rejects unmutated world (marker absent): PASS"; fi

  w=$(new_world "selftest-t3") || return 2
  if ! plant_g "$w"; then
    say "self-test T3: FAIL (invalid plant)"
    st=1
  else
    ex=$(run_integrity "$w"); fired=$(drift_ids "$w")
    if [ "$ex" = "$ctl_ex" ] && [ "$fired" = "$ctl_fired" ]; then say "self-test T3 must-not-fire assertion preserves control result: PASS"; else say "self-test T3: FAIL (exit=$ex fired=$fired; control=$ctl_ex/$ctl_fired)"; st=1; fi
  fi

  say "self-test: $([ "$st" = 0 ] && echo OK || echo BROKEN)"
  return "$st"
}

# --- main -------------------------------------------------------------------
if [ "$SELFTEST" = 1 ]; then
  self_test
  exit $?
fi

say "fault_injection_corpus.sh: repo=$REPO head=$REPO_HEAD instrument_sha256=$INSTRUMENT_SHA independent=$INDEP worlds=$WORLDS"
say "fault | script | exit | fired-class | verdict"
control_clean
fault_must_fire a plant_a corpus.pointers.report_dead
fault_must_fire b plant_b corpus.pointers.commit_nonhash
fault_must_fire c plant_c corpus.pointers.commit_unresolvable
fault_must_fire d1 plant_d1 corpus.index.missing_paths
fault_must_fire d2 plant_d2 corpus.index.stale_patterns
fault_must_fire e plant_e corpus.index.unindexed
fault_known_blind_f f plant_f
fault_must_not_fire g plant_g
fault_h_context h plant_h
say "verdict: $([ "$FAIL" = 0 ] && echo 'ALL PASS' || echo 'FAILURES PRESENT')"
[ "$FAIL" = 0 ]
exit $?
