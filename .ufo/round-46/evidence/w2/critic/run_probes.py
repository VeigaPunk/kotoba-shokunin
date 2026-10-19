import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path('/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin')
ROOT = Path('/tmp/kotoba-r46-critic')
CURRENT = REPO / 'verifiers/compare_harness_independent.py'
FROZEN = REPO / '.ufo/round-46/evidence/x3/frozen-comparator-055d3b9.py'
PYTHON = sys.executable


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n'
    path.write_text(data, encoding='utf-8')
    return data.encode('utf-8')


def run_arm(name, live_text, ind_text, scope_text, *, cwd_arg=None, scope_arg=None, scope_source=None, expect_n=1):
    d = ROOT / name
    d.mkdir(parents=True, exist_ok=True)
    live = d / 'live.json'
    independent = d / 'independent.json'
    scope = Path(scope_source) if scope_source is not None else d / 'scope.json'
    live.write_text(live_text, encoding='utf-8')
    independent.write_text(ind_text, encoding='utf-8')
    if scope_source is None:
        scope.write_text(scope_text, encoding='utf-8')
    cwd_arg = cwd_arg or str(REPO)
    scope_arg = scope_arg or str(scope)
    inputs = {
        'live': {'path': str(live), 'sha256': sha(live.read_bytes())},
        'independent': {'path': str(independent), 'sha256': sha(independent.read_bytes())},
        'scope': {'path': str(scope), 'sha256': sha(scope.read_bytes())},
    }
    input_set = sha(json.dumps(inputs, sort_keys=True, separators=(',', ':')).encode())
    arm = {'name': name, 'input_set_sha256': input_set, 'inputs': inputs, 'runs': {}}
    for flavor, comparator in (('frozen-055d3b9', FROZEN), ('committed-HEAD', CURRENT)):
        receipt = d / f'{flavor}.receipt.json'
        argv = [PYTHON, str(comparator), '--live-json', str(live),
                '--independent-json', str(independent), '--cwd', cwd_arg,
                '--scope-file', scope_arg, '--expect-n', str(expect_n),
                '--no-stamp', '--json', '--receipt', str(receipt)]
        proc = subprocess.run(argv, cwd=str(REPO), capture_output=True, text=True,
                              env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, check=False)
        result = {
            'comparator': str(comparator),
            'comparator_sha256': sha(comparator.read_bytes()),
            'argv': argv,
            'cwd': str(REPO),
            'exit': proc.returncode,
            'stdout_sha256': sha(proc.stdout.encode()),
            'stderr_sha256': sha(proc.stderr.encode()),
            'stderr': proc.stderr.strip(),
            'receipt_path': str(receipt),
            'receipt_sha256': sha(receipt.read_bytes()) if receipt.exists() else None,
        }
        if proc.stdout.strip():
            try:
                report = json.loads(proc.stdout)
                result['headline'] = report.get('reason')
                result['join'] = report.get('join')
                if receipt.exists():
                    receipt_obj = json.loads(receipt.read_text(encoding='utf-8'))
                    result['receipt_scope_file'] = receipt_obj.get('scope_file')
            except (ValueError, OSError):
                result['stdout_prefix'] = proc.stdout[:400]
        arm['runs'][flavor] = result
    return arm


empty_scope = '{"scope_out":{}}\n'
one_live = json.dumps({'results': [{'check': 'a.b', 'observed': 1, 'mode': 'equal', 'verdict': 'PASS'}]}, separators=(',', ':')) + '\n'
one_ind = json.dumps({'results': [{'check': 'a.b', 'value': 1, 'status': 'DERIVED'}]}, separators=(',', ':')) + '\n'

# C1: --cwd is a relative path to a symlinked directory, and --scope-file is
# relative to that cwd. The scope itself has no exclusions, so the honest join
# is green; receipt must name/hash the resolved scope actually read.
c1 = ROOT / 'c1-symlink-relative-cwd'
target = c1 / 'actual-cwd'
target.mkdir(parents=True, exist_ok=True)
(target / 'scope.json').write_text(empty_scope, encoding='utf-8')
alias = c1 / 'cwd-alias'
if alias.is_symlink() or alias.exists():
    alias.unlink()
alias.symlink_to(target, target_is_directory=True)
relcwd = os.path.relpath(alias, start=REPO)
arm1 = run_arm('c1-symlink-relative-cwd', one_live, one_ind, empty_scope,
               cwd_arg=relcwd, scope_arg='scope.json', scope_source=target / 'scope.json')

# C2: case-variant non-row metadata key contradicts rows but is ignored.
case_live = json.dumps({
    'results': [{'check': 'a.b', 'observed': 1, 'mode': 'equal', 'verdict': 'PASS'}],
    'modes': {'a.b': 'equal'}, 'verdicts': {'a.b': 'PASS'},
    'Modes': {'a.b': 'positive'},
}, separators=(',', ':')) + '\n'
arm2 = run_arm('c2-case-variant-shadow', case_live, one_ind, empty_scope)

# C2: Python's permissive JSON decoder accepts NaN (outside RFC 8259), and
# canon() compares two NaNs as a matching float reading.
arm3 = run_arm('c2-nan-values',
               '{"results":[{"check":"a.b","observed":NaN,"mode":"equal","verdict":"PASS"}]}\n',
               '{"results":[{"check":"a.b","value":NaN,"status":"DERIVED"}]}\n',
               empty_scope)

# C2: repeated member at a nested, unregistered metadata key is still found by
# the committed parser's recursive object_pairs_hook.
dup_live = ('{"extensions":{"nested":{"x":1,"x":2}},'
            '"results":[{"check":"a.b","observed":1,"mode":"equal","verdict":"PASS"}]}\n')
arm4 = run_arm('c2-nested-duplicate-member', dup_live, one_ind, empty_scope)

# C3: materialize a deterministic carrier with two blocks (1 vs 2 entries).
# Add a plausible record-level `kind` that contradicts committed scope_out.kind;
# the current parser ignores it while validating probe.kind separately.
c3 = ROOT / 'c3-blocker-kind-drift'
carrier = c3 / 'carrier'
carrier.mkdir(parents=True, exist_ok=True)
(carrier / 'one.jsonl').write_text(
    '2026-10-19T00:00:00Z\\n<skills>\\n- a\\n</skills>\\n<skills>\\n- a\\n- b\\n</skills>\\n',
    encoding='utf-8')
# The literal \n sequences above mirror log-carried escaped newlines, which
# recompute_probe converts before counting.
reason = 'blocker belongs to authored scope'
target_text = str(carrier.resolve())
kind = 'rule-spread-census'
observable = {
    'session_files': 1, 'files_with_skills_block': 1, 'candidate_blocks': 2,
    'distinct_totals': [1, 2],
    'rule_totals': {
        'newest-mtime': 1, 'newest-iso-stamp': 1,
        'first-in-scan-order': 1, 'last-in-scan-order': 2,
        'newest-nonempty': 1,
    },
}
probe = {'kind': kind, 'target': target_text, 'observable': observable,
         'claim': 'a valid carrier spread', 'falsified_by': 'single total'}
scoped_record = {'check': 'a.b', 'value': None, 'status': 'SCOPED_OUT',
                 'evidence': 'SCOPED_OUT: ' + reason, 'probe': probe,
                 'kind': 'external-authority'}
c3_live = json.dumps({'results': [{'check': 'a.b', 'observed': 1,
                                   'mode': 'equal', 'verdict': 'PASS'}]}, separators=(',', ':')) + '\n'
c3_ind = json.dumps({'results': [scoped_record], 'scoped_out': {'a.b': reason},
                     'scoped_out_probes': {'a.b': probe}}, separators=(',', ':')) + '\n'
c3_scope = json.dumps({'scope_out': {'a.b': {'kind': 'rule-in-author-scope', 'reason': reason}},
                       'probe_contract': {'kind': kind, 'target': target_text}},
                      separators=(',', ':')) + '\n'
arm5 = run_arm('c3-blocker-kind-drift', c3_live, c3_ind, c3_scope)

results = {
    'repo': str(REPO),
    'current_head': '78ee57e5ed6fa409476dabea6bd8146ba37425dd',
    'current_comparator_sha256': sha(CURRENT.read_bytes()),
    'frozen_comparator_sha256': sha(FROZEN.read_bytes()),
    'arms': [arm1, arm2, arm3, arm4, arm5],
}
(ROOT / 'results.json').write_text(json.dumps(results, indent=2, sort_keys=True) + '\n', encoding='utf-8')
print(json.dumps(results, indent=2, sort_keys=True))
