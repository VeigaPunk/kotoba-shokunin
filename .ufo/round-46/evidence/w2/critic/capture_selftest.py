import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
repo = Path('/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin')
cmd = [sys.executable, str(repo / 'verifiers/compare_harness_independent.py'), '--self-test']
p = subprocess.run(cmd, cwd=str(repo), capture_output=True, text=True,
                   env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, check=False)
root = Path('/tmp/kotoba-r46-critic')
(root / 'comparator-selftest.stdout').write_text(p.stdout, encoding='utf-8')
(root / 'comparator-selftest.stderr').write_text(p.stderr, encoding='utf-8')
source_sha = hashlib.sha256((repo / 'verifiers/compare_harness_independent.py').read_bytes()).hexdigest()
print(json.dumps({
    'argv': cmd, 'cwd': str(repo), 'exit': p.returncode,
    'comparator_sha256': source_sha,
    'stdout_path': str(root / 'comparator-selftest.stdout'),
    'stdout_sha256': hashlib.sha256(p.stdout.encode()).hexdigest(),
    'stderr_path': str(root / 'comparator-selftest.stderr'),
    'stderr_sha256': hashlib.sha256(p.stderr.encode()).hexdigest(),
}, indent=2, sort_keys=True))
sys.exit(0)
