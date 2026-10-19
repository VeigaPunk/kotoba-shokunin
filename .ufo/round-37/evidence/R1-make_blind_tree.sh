#!/usr/bin/env bash
# R1 remedy probe: build a worktree in which C1's source-blindness is a
# CONSTRUCTION property instead of an attestation, then scan it for the pin
# set. Review artifact — the parent decides whether to adopt it.
#
# Usage: make_blind_tree.sh [target-dir]      (default: <this dir>/blind-tree)
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Depth-independent repo root: walk up until the harness source is found, so the
# script keeps working when moved between .ufo/round-*/evidence and drafts/*/.
REPO="$(cd "$HERE" && while [ "$PWD" != / ]; do
  [ -f "$PWD/verifiers/verify_harness_claims.py" ] && break
  cd ..
done; pwd)"
[ -f "$REPO/verifiers/verify_harness_claims.py" ] || { echo "repo root not found from $HERE" >&2; exit 3; }
TARGET="${1:-$HERE/blind-tree}"

# HARNESS_TOKENS = the C1 pin surface: the harness's expected 64-hex value, its
# check-id strings, and its own stdout value forms. Any hit is a scrub defect.
# GUARD_TOKENS = the *pins guard's* substrate shas: not part of the harness's 28
# pins, required by check_substrate_pins.py, reported informationally.
HARNESS_TOKENS='c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51'
HARNESS_TOKENS="$HARNESS_TOKENS"'|omp\.catalogue\.matched|oc\.log\.init_count_max|oc\.log\.skills_rescan_max'
HARNESS_TOKENS="$HARNESS_TOKENS"'|omp\.cache\.keys_reproduced|omp\.offered\.skills|omp\.descriptions\.over_cliff'
HARNESS_TOKENS="$HARNESS_TOKENS"'|keys_reproduced=7|db_rows=14|offered=7|28/28 checks pass'
GUARD_TOKENS='bf1e86a935b1ea26166a5280001eccea1205e6c21efe1b5853f0fd368c754974|d9123b9bcdb0a31f7ab9fe9812b58a9dc1768ad6d97e7b276dff1181813218c9'
TOKENS="$HARNESS_TOKENS|$GUARD_TOKENS"

echo "repo=$REPO"
echo "target=$TARGET"
rm -rf "$TARGET"; mkdir -p "$TARGET"
# git archive of HEAD: no .git/ -> the history channel (git show/log -p) is closed
git -C "$REPO" archive HEAD | tar -x -C "$TARGET"

# 1. the harness source and its compiled cache (both leak check-id structure)
rm -f "$TARGET/verifiers/verify_harness_claims.py"
rm -rf "$TARGET/verifiers/__pycache__"

# 2. baseline.json -> pins-guard block only; the `checks` block and the notes
#    textually leak expected values. The round-21 note is redacted because it
#    states db_rows/offered/keys_reproduced/dangling in prose.
python3 - "$TARGET/verifiers/baseline.json" <<'PY'
import json, sys
p = sys.argv[1]
d = json.load(open(p))
keep = {k: d[k] for k in ("as_of", "host") if k in d}
# keep pin-shaped keys only: every prose note in measured_against leaked pin
# values in prose (round-21 note: db_rows/offered/keys_reproduced/dangling;
# round18_move: keys_reproduced=7 / 17->7)
ma = {k: v for k, v in d.get("measured_against", {}).items()
      if k.endswith("_sha256") or k.endswith("_mtime")}
ma["blind_note"] = "prose notes redacted for the blind worktree (they leaked pin values)"
keep["measured_against"] = ma
json.dump(keep, open(p, "w"), indent=1, sort_keys=True)
PY

# 3. documents that quote the pin set or the harness stdout (measured inventory)
for f in LOG.md SCORECARD.md SKILL.md corpus/README.md \
         corpus/knowledge/harness-router-models-round9.md \
         corpus/knowledge/harness-verifier-round10.md \
         corpus/knowledge/instruction-surface-census-round13.md \
         corpus/knowledge/skill-activation-telemetry.md \
         corpus/lessons/round-10.md; do
  rm -f "$TARGET/$f"
done
rm -rf "$TARGET/.ufo"     # prior-round fragments + reports quote the pins (~500 files)

# 4. scan: any residual HARNESS pin hit is a defect of this scrub, not of the reader
hits="$(grep -rIlE "$HARNESS_TOKENS" --exclude-dir=.git "$TARGET" 2>/dev/null | sed "s|$TARGET/||" || true)"
echo "--- residual HARNESS pin-surface files (must be none) ---"
if [ -n "$hits" ]; then echo "$hits"; else echo "(none)"; fi
echo "harness_pin_residual_count=$(printf '%s' "$hits" | grep -c . || true)"
guard="$(grep -rIlE "$GUARD_TOKENS" --exclude-dir=.git "$TARGET" 2>/dev/null | sed "s|$TARGET/||" || true)"
echo "pins-guard substrate shas present (expected; check_substrate_pins.py needs them): ${guard:-none}"
echo "dot_git_present=$([ -d "$TARGET/.git" ] && echo yes || echo no)"

# 5. the scrub must not starve the blind builder: substrate is outside the repo
python3 - "$TARGET" <<'PY'
import pathlib, sqlite3, sys
tree = pathlib.Path(sys.argv[1])
db = pathlib.Path.home() / ".omp/agent/skill-descriptions.db"
rows = sqlite3.connect(f"file:{db}?mode=ro", uri=True).execute("select count(*) from sqlite_master").fetchone()
print(f"substrate_reachable_from_scrub_tree=yes (db sqlite_master rows={rows[0]})  tree_files={sum(1 for _ in tree.rglob('*'))}")
PY
# and the pins guard must still run inside the scrub tree (redaction is non-breaking)
python3 "$TARGET/verifiers/check_substrate_pins.py" >/dev/null 2>&1 \
  && echo "pins_guard_in_scrub_tree=exit 0" || echo "pins_guard_in_scrub_tree=NONZERO (see report)"