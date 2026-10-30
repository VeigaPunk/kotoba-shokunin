#!/usr/bin/env python3
"""Round-82 descriptive registry census; not an admission gate."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repo', type=Path, required=True)
parser.add_argument('--rev', required=True)
args = parser.parse_args()
text = subprocess.check_output(
    ['git', '-C', str(args.repo.resolve()), 'show',
     f'{args.rev}:corpus/SOURCES.md'], text=True)
rows = [line.split('|') for line in text.splitlines()
        if re.match(r'^ {0,3}\|\s*S\d{3,}\s*\|', line)]
print(json.dumps({
    'revision': args.rev,
    'rows': len(rows),
    'tiers': dict(sorted(Counter(row[4].strip() for row in rows).items())),
    'status': dict(sorted(Counter(row[8].strip() for row in rows).items())),
    'malformed': sum(len(row) != 13 for row in rows),
}, sort_keys=True))
