#!/bin/bash
# SentinelScopeR99 file-scope checks. Usage: scope_files.sh <CAND_REV> <D>
set -uo pipefail
S=/fast/scratch/hyaku/kotoba-r99/SentinelScopeR99
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=b53e209603e7c480cd975ea543e415b66f695438
REV="$1"; D="$2"
LOG=$S/scope-files.log
: > "$LOG"
{
echo "=== diff --stat"
git -C "$D" diff --stat "$BASE" "$REV"
echo
echo "=== diff --name-status"
git -C "$D" diff --name-status "$BASE" "$REV"
echo
echo "=== SKILL.md"
echo "base $(git -C "$LANE" show "$BASE:SKILL.md" | sha256sum)"
echo "cand $(git -C "$D" show "$REV:SKILL.md" | sha256sum)"
echo
echo "=== spotcheck files"
git -C "$LANE" ls-tree -r --name-only "$BASE" -- corpus/lessons | grep spotcheck | while read -r f; do
  a=$(git -C "$LANE" show "$BASE:$f" | sha256sum | cut -d' ' -f1)
  b=$(git -C "$D" show "$REV:$f" | sha256sum | cut -d' ' -f1)
  [ "$a" = "$b" ] || echo "CHANGED $f"
done
echo "spotcheck scan done"
echo
echo "=== verifiers/fixtures tree"
a=$(git -C "$LANE" ls-tree -r "$BASE" -- verifiers/fixtures | sort | sha256sum | cut -d' ' -f1)
b=$(git -C "$D" ls-tree -r "$REV" -- verifiers/fixtures | sort | sha256sum | cut -d' ' -f1)
echo "base $a"; echo "cand $b"; [ "$a" = "$b" ] && echo FIXTURES-IDENTICAL || echo FIXTURES-CHANGED
echo
echo "=== frozen corpus gates"
for f in verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py; do
  a=$(git -C "$LANE" show "$BASE:$f" | sha256sum | cut -d' ' -f1)
  b=$(git -C "$D" show "$REV:$f" | sha256sum | cut -d' ' -f1)
  echo "$f base $a cand $b"; [ "$a" = "$b" ] && echo "  IDENTICAL" || echo "  CHANGED"
done
echo
echo "=== verify_dispatch_prompts production bytes"
python3 -B "$S/scope_check.py" "$LANE" "$BASE" "$D" "$REV"
echo "rc=$?"
} >> "$LOG" 2>&1
echo DONE >> "$LOG"
