#!/usr/bin/env bash
# ExecReceiptRevs: read-only round-93 repair for unresolved landing receipts.
# Usage: check-receipt-revs.sh <receipts-dir> [REPO]
# REPO defaults to this lane. Counts occurrences, not unique revisions.
# Scratch declarations are line-local: `world rev`, `forgery`, or a path-shaped `/scratch/` token
# (round-93 CriticClaimsR93 D1: a bare word "scratch" anywhere on the line no longer exempts it).
# Exit: 0 resolved >= 1 and no misses; 1 unresolved or malformed declaration;
# 2 no candidates or unreadable input.
# Round-94 mined mistake (CriticClaimsR93 D2/D3, fixed by ExecReceiptHeaders): a line that is
# header-SHAPED after stripping leading whitespace (`REV=`, `measured rev `, `rev ` followed by a
# hex run, or the G1 prefix) but is not a well-formed header — hex run length not exactly 40
# (12 for G1), or leading whitespace — prints `MALFORMED <path>:<line> <reason>` and is counted;
# any MALFORMED or UNRESOLVED exits 1. Scratch declarations keep exempting a line.
set -u
if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
    echo 'usage: check-receipt-revs.sh <receipts-dir> [REPO]' >&2
    exit 2
fi
LANE="$(cd "$(dirname "$0")/../../.." && pwd)" || exit 2
exec python3 -B - "$1" "${2:-$LANE}" <<'PY'
import os
import re
import stat
import subprocess
import sys

root, repo = sys.argv[1:]
full = re.compile(r'(?<![0-9a-fA-F])[0-9a-fA-F]{40}(?![0-9a-fA-F])')
header = re.compile(r'^(?:REV=|measured rev |rev )[0-9a-fA-F]{40}(?![0-9a-fA-F])')
g1 = re.compile(r'^G1 revision identity PASS: rev ([0-9a-fA-F]{12})(?![0-9a-fA-F])')
shaped_header = re.compile(r'(?:REV=|measured rev |rev )([0-9a-fA-F]+)')
shaped_g1 = re.compile(r'G1 revision identity PASS: rev ([0-9a-fA-F]+)')
scratch_line = re.compile(r'world rev|forgery|/scratch/', re.IGNORECASE)
resolved = unresolved = scratch = malformed = files = 0

def git(*args):
    return subprocess.run(['git', '-C', repo, *args], stdout=subprocess.PIPE,
                          stderr=subprocess.DEVNULL, check=False)

def walk_error(error):
    raise error

try:
    if not os.path.isdir(root):
        raise OSError('receipts directory is missing or not a directory')
    for directory, dirs, names in os.walk(root, onerror=walk_error):
        dirs.sort()
        for name in sorted(names):
            path = os.path.join(directory, name)
            if not stat.S_ISREG(os.stat(path, follow_symlinks=False).st_mode):
                continue
            files += 1
            with open(path, encoding='utf-8', errors='replace') as stream:
                for number, line in enumerate(stream, 1):
                    prefix = g1.match(line)
                    declared = scratch_line.search(line) is not None
                    # World declarations need not use a lane-receipt header.
                    if declared:
                        scratch += len(full.findall(line))
                        if prefix:
                            scratch += 1
                        continue
                    if prefix:
                        tokens = [prefix.group(1)]
                    elif header.match(line):
                        tokens = full.findall(line)
                    else:
                        # Fail closed on a malformed declaration instead of reading the line as
                        # no receipt claim (round-93 CriticClaimsR93 D2/D3).
                        body = line.rstrip('\n')
                        stripped = body.lstrip()
                        shape = shaped_header.match(stripped) or shaped_g1.match(stripped)
                        if shape is None:
                            continue
                        reasons = []
                        if stripped != body:
                            reasons.append('leading whitespace before the declaration')
                        if shaped_g1.match(stripped):
                            if len(shape.group(1)) != 12:
                                reasons.append('G1 hex run is %d, not 12' % len(shape.group(1)))
                        elif len(shape.group(1)) != 40:
                            reasons.append('hex run is %d, not 40' % len(shape.group(1)))
                        if not reasons:
                            reasons.append('declaration is not a well-formed header')
                        malformed += 1
                        print(f'MALFORMED {path}:{number} {"; ".join(reasons)}')
                        continue
                    for token in tokens:
                        commit = token
                        if len(token) == 12:
                            result = git('rev-parse', '--verify', '-q', token + '^{commit}')
                            commit = result.stdout.decode().strip() if result.returncode == 0 else ''
                        if commit and git('cat-file', '-e', commit + '^{commit}').returncode == 0:
                            resolved += 1
                        else:
                            unresolved += 1
                            print(f'UNRESOLVED {token} {path}:{number}')
except (OSError, subprocess.SubprocessError) as error:
    print(f'could-not-evaluate: {error}', file=sys.stderr)
    sys.exit(2)

print(f'{scratch} scratch-declared')
print(f'malformed declarations: {malformed}')
print(f'receipt revisions: {resolved} resolved, {unresolved} unresolved over {files} files')
sys.exit(1 if (unresolved or malformed) else 0 if resolved else 2)
PY
