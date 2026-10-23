#!/usr/bin/env bash
# check_report_hashes.sh — read-only check that hash-like hex tokens in a wave
# report resolve as commits in the lane repository (round-57 R1/Q41).
#
# usage: check_report_hashes.sh <lane-repo> <report.md>
#
# Prints one line per offending occurrence:  <report>:<line>: <token>
#
# Candidates: hex runs of 7-40 characters that are not part of a longer hex run
# (so a full 64-char sha256 never matches, while a short prefix would).
# Skipped, so content digests are not reported as missing commits:
#   - any token on a line containing "sandbox" (any case): a labelled sandbox
#     hash, per the round-57 bounds;
#   - any token introduced by a digest marker (sha256, sha-256, sha512, sha1,
#     md5, blake2, b2sum, cksum, digest, hash) within three non-alphanumeric
#     characters.
# A token resolves if `git rev-parse --verify <token>^{commit}` succeeds, i.e.
# it names one commit object in the lane repo (an ambiguous prefix fails).
#
# exit 0: every scanned token resolves as a commit
# exit 1: at least one token does not (all such tokens are printed)
# exit 2: usage error (argument count, unreadable report, not a git repository)
set -u

unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR \
      GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES

prog=${0##*/}
usage() { printf 'usage: %s <lane-repo> <report.md>\n' "$prog" >&2; exit 2; }
fatal_usage() { printf '%s: %s\n' "$prog" "$1" >&2; usage; }

[ "$#" -eq 2 ] || usage
repo=$1
report=$2

[ -d "$repo" ] || fatal_usage "not a directory: $repo"
[ -f "$report" ] && [ -r "$report" ] || fatal_usage "not a readable file: $report"
command -v git >/dev/null 2>&1 || fatal_usage "git not found in PATH"
command -v python3 >/dev/null 2>&1 || fatal_usage "python3 not found in PATH"
git -C "$repo" rev-parse --git-dir >/dev/null 2>&1 || fatal_usage "not a git repository: $repo"

status=0
tmp=$(mktemp) || fatal_usage "mktemp failed"
trap 'rm -f "$tmp"' EXIT
python3 - "$report" >"$tmp" <<'PY' || fatal_usage "scan failed: $report"
import re
import sys

path = sys.argv[1]
TOKEN = re.compile(r'(?<![0-9A-Fa-f])([0-9A-Fa-f]{7,40})(?![0-9A-Fa-f])')
DIGEST = re.compile(
    r'(?i)(?:sha-?256|sha-?512|sha-?1|md5|blake2b?|b2sum|cksum|digest|hash)[^0-9A-Za-z]{0,3}$'
)

with open(path, encoding='utf-8', errors='replace') as fh:
    for lineno, line in enumerate(fh, 1):
        line = line.rstrip('\n')
        if 'sandbox' in line.lower():
            continue
        for match in TOKEN.finditer(line):
            if DIGEST.search(line[:match.start()]):
                continue
            sys.stdout.write('%d\t%s\n' % (lineno, match.group(1)))
PY

while IFS=$'\t' read -r lineno tok; do
    [ -n "${tok:-}" ] || continue
    if git --no-optional-locks -C "$repo" rev-parse --verify --quiet "${tok}^{commit}" >/dev/null 2>&1; then
        continue
    fi
    printf '%s:%s: %s\n' "$report" "$lineno" "$tok"
    status=1
done <"$tmp"
exit "$status"
