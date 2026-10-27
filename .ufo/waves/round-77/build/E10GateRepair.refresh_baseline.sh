#!/usr/bin/env bash
# E10GateRepair.refresh_baseline.sh — recompute verifiers/corpus-baseline.json
# from the tree it is pointed at, print every changed expectation old -> new, and
# write the file. No expectation is hand-written: each `equal` value is copied
# from the integrity gate's own `--no-baseline --json` observation; each `zero`
# value is asserted 0 before it is written.
#
# usage: E10GateRepair.refresh_baseline.sh <repo-root> [note-key] [--dry-run]
#   <repo-root>  toplevel of the git work tree holding the FINAL round tree
#                (typically a scratch clone), never a subdirectory
#   [note-key]   key under "notes" to record the re-record (default round77_rerecord)
#   --dry-run    print old -> new and stop before writing
#
# Fail-closed preconditions (exit 2, baseline untouched):
#   * <repo-root> is the toplevel of a git work tree
#   * verifiers/verify_corpus_integrity.py and verifiers/verify_corpus_independent.py exist
#   * the integrity gate exits 0 on the tree with --no-baseline (i.e. every
#     zero-mode violation is empty) — a baseline is never recorded over drift
#   * the independent gate exits 0 on the same tree
#   * every baseline check id still resolves to an observed key, and every
#     zero-mode observation is 0
#
# Exit: 0 written (or dry-run), 2 refused, 3 internal error.
set -uo pipefail

usage() {
    sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
}

die() {
    printf 'refresh_baseline: %s\n' "$*" >&2
    exit 2
}

[ $# -ge 1 ] || { usage >&2; exit 2; }

repo=$1; shift
note_key=round77_rerecord
dry_run=0
for arg in "$@"; do
    case $arg in
        --dry-run) dry_run=1 ;;
        -h|--help) usage; exit 0 ;;
        -*) die "unknown option: $arg" ;;
        *) note_key=$arg ;;
    esac
done

[ -d "$repo" ] || die "no such directory: $repo"
here=$(cd "$repo" && pwd -P) || die "cannot enter $repo"
top=$(git -C "$here" rev-parse --show-toplevel 2>/dev/null) || die "not a git work tree: $here"
top=$(cd "$top" && pwd -P)
[ "$top" = "$here" ] || die "repo root $here is not the work-tree toplevel $top"

for f in verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py \
         verifiers/corpus-baseline.json; do
    [ -f "$top/$f" ] || die "missing $f under $top"
done

# The gate counts `git ls-files corpus/`, so an untracked corpus file is
# invisible to it: staging or committing the final tree in this clone is a
# precondition, not an optional step.
untracked=$(git -C "$top" ls-files --others --exclude-standard -- corpus/)
[ -z "$untracked" ] || {
    printf 'refresh_baseline: untracked corpus file(s) the gate cannot see:\n%s\n' "$untracked" >&2
    die "stage or commit the final corpus tree in this clone before re-recording"
}

tmp=$(mktemp -d "${TMPDIR:-/tmp}/e10-baseline.XXXXXX") || die "cannot create a temp dir"
trap 'rm -rf -- "$tmp"' EXIT

# Gate 1: integrity, no baseline -> exit 0 iff every zero-mode class is empty.
python3 -B "$top/verifiers/verify_corpus_integrity.py" --repo "$top" --no-baseline --json \
    > "$tmp/integrity.json" 2> "$tmp/integrity.err"
rc=$?
[ "$rc" -eq 0 ] || {
    sed -n '1,40p' "$tmp/integrity.err" >&2
    die "integrity gate exited $rc on $top; fix the drift before re-recording a baseline"
}

# Gate 2: the independent re-derivation, same tree.
python3 -B "$top/verifiers/verify_corpus_independent.py" --repo "$top" --json \
    > "$tmp/independent.json" 2> "$tmp/independent.err"
rc=$?
[ "$rc" -eq 0 ] || {
    sed -n '1,40p' "$tmp/independent.err" >&2
    die "independent gate exited $rc on $top; fix the drift before re-recording a baseline"
}

python3 - "$top" "$tmp/integrity.json" "$tmp/independent.json" "$note_key" "$dry_run" <<'PY'
import datetime
import json
import os
import subprocess
import sys

top, integrity_json, independent_json, note_key, dry_run = sys.argv[1:6]

obs_doc = json.load(open(integrity_json, encoding="utf-8"))
observed = obs_doc["observed"]["corpus"]
ind_doc = json.load(open(independent_json, encoding="utf-8"))

baseline_path = os.path.join(top, "verifiers/corpus-baseline.json")
baseline = json.load(open(baseline_path, encoding="utf-8"))

# Cross-check: the independent measurement must agree with the one being recorded.
ind = ind_doc["observed"]
pairs = [
    ("tracked_files", ind["index"]["tracked_files"]),
    ("unindexed", ind["index"]["unindexed"]),
    ("stale_patterns", ind["index"]["stale_tokens"]),
    ("missing_paths", ind["index"]["missing_paths"]),
    ("report_total", ind["pointers"]["report_total"]),
    ("report_dead", ind["pointers"]["report_dead"]),
    ("commit_total", ind["commits"]["commit_total"]),
    ("commit_unresolvable", ind["commits"]["commit_unresolvable"]),
    ("commit_nonhash", ind["commits"]["commit_nonhash"]),
]
for key, other in pairs:
    if key in observed and int(observed[key]) != int(other):
        sys.stderr.write(
            "refresh_baseline: the two gates disagree on %s (%r vs %r); refusing\n"
            % (key, observed[key], other)
        )
        sys.exit(2)

# A check id is `corpus.<family>.<observation>`; the observation is its last
# component in the gate's flat dict. Derive it, never hand-map it.
changes = []
for check_id, row in baseline["checks"].items():
    key = check_id.rsplit(".", 1)[-1]
    if key not in observed:
        sys.stderr.write("refresh_baseline: %s has no observed key %r\n" % (check_id, key))
        sys.exit(2)
    now = int(observed[key])
    old = row.get("expect")
    if row.get("mode") == "zero":
        if now != 0:
            sys.stderr.write(
                "refresh_baseline: zero-mode %s observed %d, not 0; refusing\n" % (check_id, now)
            )
            sys.exit(2)
        row["expect"] = 0
        if old != 0:
            changes.append((check_id, old, 0))
        continue
    if row.get("mode") != "equal":
        sys.stderr.write("refresh_baseline: unknown mode %r for %s\n" % (row.get("mode"), check_id))
        sys.exit(2)
    row["expect"] = now
    if old != now:
        changes.append((check_id, old, now))

head = subprocess.run(
    ["git", "-C", top, "rev-parse", "HEAD"], capture_output=True, text=True
).stdout.strip()
subject = subprocess.run(
    ["git", "-C", top, "log", "-1", "--format=%s"], capture_output=True, text=True
).stdout.strip()
status = subprocess.run(
    ["git", "-C", top, "status", "--porcelain"], capture_output=True, text=True
).stdout.splitlines()
dirty = "clean" if not status else "%d path(s) uncommitted" % len(status)

today = datetime.date.today().isoformat()
moved = ", ".join("%s %s -> %s" % (cid.rsplit(".", 1)[-1], old, new)
                  for cid, old, new in changes) or "no expectation moved"

# `repo` names the lane the baseline belongs to, not the scratch directory the
# measurement ran in, so the recorded value is kept when one exists.
repo_name = (baseline.get("measured_against") or {}).get("repo") or os.path.basename(top)

baseline["as_of"] = today
baseline["measured_against"] = {
    "repo": repo_name,
    "head": head[:7],
    "head_subject": subject,
    "git_status": dirty,
    "command": "python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json",
    "note": (
        "Round-77 baseline refresh, computed by E10GateRepair.refresh_baseline.sh from the "
        "integrity gate's own --no-baseline --json over the final tree at %s (%s; %s): %s. "
        "The independent gate agreed on every recorded class and exited 0 before the write. "
        "Expectations are re-recorded to observed committed bytes, not fitted to a denominator; "
        "zero-mode expectations stay zero."
        % (head[:7], subject or "(no subject)", dirty, moved)
    ),
}
note = (
    "round 77 closure repair of R76-D4: re-recorded at %s (%s; %s) with %s. tracked_files "
    "144 -> the observed count closes the two unindexed closure spot-checks "
    "(corpus/lessons/round-75-verifier-spotcheck.md, round-76-verifier-spotcheck.md), whose "
    "cited report pointers and commit tokens are also why report_total and commit_total move. "
    "Every zero-mode expectation observed zero; the script refuses to write otherwise."
    % (head[:7], subject or "(no subject)", dirty, moved)
)
baseline.setdefault("notes", {})[note_key] = note

if dry_run == "1":
    for cid, old, new in changes:
        print("%-34s %s -> %s" % (cid.rsplit(".", 1)[-1], old, new))
    if not changes:
        print("no expectation moved")
    print("dry-run: %s untouched" % baseline_path)
    sys.exit(0)

with open(baseline_path, "w", encoding="utf-8") as fh:
    json.dump(baseline, fh, indent=1, ensure_ascii=False)
    fh.write("\n")

for cid, old, new in changes:
    print("%-34s %s -> %s" % (cid.rsplit(".", 1)[-1], old, new))
if not changes:
    print("no expectation moved")
print("wrote %s (head %s)" % (baseline_path, head[:7]))
PY
rc=$?
[ "$rc" -eq 0 ] || exit "$rc"

# Post-condition: the gate now reads the re-recorded file green.
python3 -B "$top/verifiers/verify_corpus_integrity.py" --repo "$top" --json \
    > "$tmp/post.json" 2> "$tmp/post.err"
rc=$?
if [ "$rc" -ne 0 ]; then
    sed -n '1,40p' "$tmp/post.err" >&2
    printf 'refresh_baseline: the re-recorded baseline does not read green (exit %s)\n' "$rc" >&2
    exit 3
fi
python3 -B "$top/verifiers/verify_corpus_independent.py" --repo "$top" --json \
    > "$tmp/post-ind.json" 2> "$tmp/post-ind.err"
rc=$?
if [ "$rc" -ne 0 ]; then
    sed -n '1,40p' "$tmp/post-ind.err" >&2
    printf 'refresh_baseline: the independent gate does not read green (exit %s)\n' "$rc" >&2
    exit 3
fi
printf 'verified: both corpus gates exit 0 against the re-recorded baseline\n'
