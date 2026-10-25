#!/usr/bin/env bash
# Re-record verifiers/corpus-baseline.json from the observed tree — one command.
#
# Run from the lane root AFTER every round-72 file is tracked and indexed and the
# closing content commit exists. The three `equal` cells are read back from the
# instrument itself (never typed by hand); every `zero` cell stays 0 and is
# asserted, not assumed.
#
#   bash .ufo/waves/round-72/w1/build/ExecIndexBaseline/rerecord-at-tip.sh [<rev>]
#
# <rev> defaults to the short HEAD; pass the landed content commit explicitly if
# you re-record before the paperwork commit.
set -euo pipefail
rev=${1:-$(git rev-parse --short=7 HEAD)}
out=$(mktemp)
trap 'rm -f "$out"' EXIT
# a dirty zero-mode check makes this exit 1: keep the JSON, let the guard refuse.
python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json > "$out" || true
python3 - "$rev" "$out" <<'PY'
import json, sys

rev, path = sys.argv[1], sys.argv[2]
obs = json.load(open(path))["observed"]["corpus"]
base_path = "verifiers/corpus-baseline.json"
b = json.load(open(base_path, encoding="utf-8"))
cells = {
    "corpus.index.tracked_files": "tracked_files",
    "corpus.pointers.report_total": "report_total",
    "corpus.pointers.commit_total": "commit_total",
}
zero = ("unindexed", "stale_patterns", "missing_paths", "report_dead",
        "commit_unresolvable", "commit_nonhash")
dirty = {k: obs[k] for k in zero if obs[k]}
if dirty:
    sys.exit("refusing to re-record: zero-mode checks are not zero: %r" % dirty)
old = {k: b["checks"][k]["expect"] for k in cells}
for check, key in cells.items():
    b["checks"][check]["expect"] = obs[key]
b["as_of"] = "2026-10-25"
b["measured_against"]["head"] = rev
b["measured_against"]["git_status"] = "round-72 closing tip; every round file tracked and indexed"
b["notes"]["round72_tip_rerecord"] = (
    "round 72 closing re-record at %s from python3 -B verifiers/verify_corpus_integrity.py "
    "--no-baseline --json: tracked_files %d -> %d, report_total %d -> %d, commit_total %d -> %d; "
    "every zero-defect expectation observed zero (unindexed, stale_patterns, missing_paths, "
    "report_dead, commit_unresolvable, commit_nonhash)."
    % (rev, old["corpus.index.tracked_files"], obs["tracked_files"],
       old["corpus.pointers.report_total"], obs["report_total"],
       old["corpus.pointers.commit_total"], obs["commit_total"])
)
with open(base_path, "w", encoding="utf-8") as fh:
    json.dump(b, fh, indent=1, ensure_ascii=False)
print("corpus-baseline.json -> %d / %d / %d (tracked_files / report_total / commit_total)"
      % (obs["tracked_files"], obs["report_total"], obs["commit_total"]))
PY
python3 -B verifiers/verify_corpus_integrity.py
python3 -B verifiers/verify_corpus_independent.py
