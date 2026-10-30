#!/usr/bin/env python3
"""Independent round82 C1 predata guard; never execute candidate instruments.
Exit 0: independent invariants hold; 1: rejected; 2: unreadable input.
Scope: exact round82 base class retention and default-only instrument cutover.
Semantic extractor changes are rejected, not implicitly approved.
"""
import argparse
import ast
import calendar
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from datetime import datetime, timezone

BASE = '47dbe8781657de563ff867caca6244d28e3db504'
HOST = {'omp': '/home/vgpnk/.local/bin/omp',
        'opencode': '/home/vgpnk/.opencode/bin/opencode'}
INSTRUMENTS = {'check_substrate_pins.py': 'BINARIES',
               'verify_surfaces.py': 'DEFAULT_BINARIES'}
HOST_FROZEN = {
    'omp': {'sha256': 'e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f',
            'mtime_ns': 1793326786168359786, 'bytes': 276244656},
    'opencode': {'sha256': 'ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7',
                 'mtime_ns': 499162500000000000, 'bytes': 240416944},
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def measure(path):
    path = Path(path)
    with path.open('rb') as stream:
        before = os.fstat(stream.fileno())
        magic = stream.read(4)
        stream.seek(0)
        sha = hashlib.file_digest(stream, 'sha256').hexdigest()
        after = os.fstat(stream.fileno())
    identity = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
    if identity(before) != identity(after) or identity(after) != identity(path.stat()):
        raise ValueError('binary changed during measurement: ' + str(path))
    return {'path': str(path.resolve()), 'elf': magic == b'\x7fELF',
            'sha256': sha, 'mtime_ns': after.st_mtime_ns, 'bytes': after.st_size}


def parse_stamp(text):
    # Exact nanoseconds only: no float conversion or tolerance widening.
    match = re.fullmatch(r'(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)\.(\d{9})(Z|[+-]\d\d:\d\d)', text)
    if not match:
        raise ValueError('mtime pin must have timezone and nine fractional digits')
    dt = datetime.fromisoformat(match[1] + match[3].replace('Z', '+00:00'))
    return calendar.timegm(dt.utctimetuple()) * 10**9 + int(match[2])


def script_shape(text, default_name):
    tree = ast.parse(text)
    defaults = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == default_name for t in node.targets):
            if defaults is not None or len(node.targets) != 1:
                raise ValueError('ambiguous default assignment')
            defaults = ast.literal_eval(node.value)
            node.value = ast.Constant(value='FROZEN-DEFAULT-PATH-DICTIONARY')
    if not isinstance(defaults, dict) or set(defaults) != set(HOST) or not all(isinstance(v, str) for v in defaults.values()):
        raise ValueError('unrecognized default dictionary: ' + default_name)
    # Ignore explanatory docstrings, but retain every executable AST statement.
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant) and isinstance(node.body[0].value.value, str):
                node.body.pop(0)
    return defaults, digest(ast.dump(tree, include_attributes=False).encode())


def classes(document):
    rows = document['classes']
    if not isinstance(rows, list) or not rows:
        raise ValueError('empty or malformed census')
    result = {}
    for row in rows:
        cid = row['class_id']
        if not isinstance(cid, str) or cid in result:
            raise ValueError('invalid or duplicate class id')
        result[cid] = {key: row[key] for key in ('harness', 'literal', 'context_kind', 'verdict')}
    return result


def evaluate(base, candidate, live, frozen=None):
    checks = []
    def check(name, ok, detail):
        checks.append({'check': name, 'pass': bool(ok), 'detail': detail})
    frozen = HOST_FROZEN if frozen is None else frozen
    for harness, identity in frozen.items():
        check(harness + '.frozen-live-identity',
              all(live[harness][key] == value for key, value in identity.items()),
              identity)
    expected = candidate['baseline.json']['measured_against']
    for harness, facts in live.items():
        check(harness + '.ELF', facts['elf'], facts)
        check(harness + '.sha-pin', expected.get(harness + '_binary_sha256') == facts['sha256'], expected.get(harness + '_binary_sha256'))
    try:
        pinned_ns = parse_stamp(expected['omp_binary_mtime'])
    except (KeyError, TypeError, ValueError) as exc:
        pinned_ns = str(exc)
    check('omp.ns-mtime-pin', pinned_ns == live['omp']['mtime_ns'], pinned_ns)
    for filename, default_name in INSTRUMENTS.items():
        try:
            defaults, shape = script_shape(candidate[filename], default_name)
            _, base_shape = script_shape(base[filename], default_name)
            check(filename + '.executable-AST', shape == base_shape, {'base': base_shape, 'candidate': shape})
            for harness, path in defaults.items():
                try:
                    facts = measure(path)
                    ok = facts['elf'] and all(facts[key] == live[harness][key] for key in ('sha256', 'bytes', 'mtime_ns'))
                    check(filename + '.' + harness + '.defaults', ok, facts)
                except (OSError, ValueError) as exc:
                    check(filename + '.' + harness + '.defaults', False, str(exc))
        except (ValueError, SyntaxError, TypeError) as exc:
            check(filename + '.AST-defaults', False, str(exc))
    old = classes(base['surfaces-baseline.json'])
    new = classes(candidate['surfaces-baseline.json'])
    check('census.exact-base-identities', old == new,
          {'base_count': len(old), 'candidate_count': len(new),
           'removed': sorted(old.keys() - new.keys()), 'added': sorted(new.keys() - old.keys()),
           'changed': sorted(key for key in old.keys() & new.keys() if old[key] != new[key])})
    check('removal-ledger.unchanged', candidate['census-removals.json'] == base['census-removals.json'],
          'round82 does not silently retire additional classes')
    return checks


def git(repo, *args):
    return subprocess.run(['git', '-C', str(repo), *args], capture_output=True, check=True, timeout=120).stdout


def load(repo, rev):
    result = {}
    for filename in ('baseline.json', 'surfaces-baseline.json', 'census-removals.json', *INSTRUMENTS):
        text = git(repo, 'show', rev + ':verifiers/' + filename).decode()
        result[filename] = json.loads(text) if filename.endswith('.json') else text
    return result


def self_test():
    with tempfile.TemporaryDirectory(prefix='pin-guard-') as directory:
        paths = {h: str(Path(directory) / h) for h in HOST}
        for path in paths.values():
            Path(path).write_bytes(b'\x7fELFfixture-only-not-executable\n')
            os.utime(path, ns=(1793300000123456789, 1793300000123456789))
        live = {h: measure(p) for h, p in paths.items()}
        base = {'baseline.json': {'measured_against': {
            'omp_binary_sha256': live['omp']['sha256'],
            'opencode_binary_sha256': live['opencode']['sha256'],
            'omp_binary_mtime': '2026-10-29T18:53:20.123456789+00:00'}},
            'surfaces-baseline.json': {'classes': [{'class_id': 'omp:agents-md/AGENTS.md', 'harness': 'omp', 'literal': 'AGENTS.md', 'context_kind': 'loader-group', 'verdict': 'governed'}]},
            'census-removals.json': {'removed': []}}
        for filename, name in INSTRUMENTS.items():
            base[filename] = name + ' = ' + repr(paths) + '\ndef actual_check():\n    return 1 + 2\n'
        failures = 0
        assertions = 0
        def world(name, mutate, expected_ok, required_red=None):
            nonlocal failures, assertions
            candidate = copy.deepcopy(base)
            mutate(candidate)
            rows = evaluate(base, candidate, live, frozen=live)
            red = [r['check'] for r in rows if not r['pass']]
            ok = (not red) == expected_ok and (required_red is None or required_red in red)
            assertions += 1
            failures += not ok
            print(json.dumps({'world': name, 'guard_exit': int(bool(red)), 'red': red, 'assertion': 'PASS' if ok else 'FAIL'}, sort_keys=True))
        world('matching fixture', lambda c: None, True)
        wrong = str(Path(directory) / 'stub')
        Path(wrong).write_text('print canned pass\n')
        def wrong_binary(c):
            for filename, name in INSTRUMENTS.items():
                c[filename] = c[filename].replace(repr(paths['omp']), repr(wrong))
            c['baseline.json']['measured_against']['omp_binary_sha256'] = measure(wrong)['sha256']
        world('wrong binary even when self-pinned', wrong_binary, False, 'check_substrate_pins.py.omp.defaults')
        world('wrong pin', lambda c: c['baseline.json']['measured_against'].update(omp_binary_sha256='0'*64), False, 'omp.sha-pin')
        world('wrong ns mtime', lambda c: c['baseline.json']['measured_against'].update(omp_binary_mtime='2026-10-29T18:53:20.123456788+00:00'), False, 'omp.ns-mtime-pin')
        # Keep one class so deletion is a measured rejection rather than a parse error.
        extra = dict(base['surfaces-baseline.json']['classes'][0], class_id='omp:claude-md/CLAUDE.md')
        base['surfaces-baseline.json']['classes'].append(extra)
        world('deleted base class', lambda c: c['surfaces-baseline.json']['classes'].pop(), False, 'census.exact-base-identities')
        for filename, name in INSTRUMENTS.items():
            def stub(c, f=filename, n=name):
                c[f] = n + ' = ' + repr(paths) + '\nprint("all checks PASS")\n'
            world(filename + ' stdout stub with correct binary and pins', stub, False, filename + '.executable-AST')
        world('changed removal ledger', lambda c: c['census-removals.json']['removed'].append({'class_id': 'omp:agents-md/AGENTS.md'}), False, 'removal-ledger.unchanged')
        changed_live = copy.deepcopy(live)
        changed_live['omp']['sha256'] = 'f' * 64
        rows = evaluate(base, base, changed_live, frozen=live)
        ok = any(r['check'] == 'omp.frozen-live-identity' and not r['pass'] for r in rows)
        assertions += 1
        failures += not ok
        print(json.dumps({'world': 'changed live bytes', 'guard_exit': 1, 'assertion': 'PASS' if ok else 'FAIL'}))
        print(f'{failures} failure(s) over {assertions} assertions')
        return int(bool(failures))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path)
    parser.add_argument('--rev')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if not args.repo or not args.rev:
        parser.error('--repo and --rev required')
    try:
        rev = git(args.repo, 'rev-parse', '--verify', args.rev + '^{commit}').decode().strip()
        live = {h: measure(p) for h, p in HOST.items()}
        base = load(args.repo, BASE)
        candidate = load(args.repo, rev)
        rows = evaluate(base, candidate, live)
        scope = git(args.repo, 'diff', '--name-only', BASE, rev, '--', 'verifiers', 'corpus').decode().splitlines()
        print(json.dumps({'base': BASE, 'revision': rev, 'live': live, 'checks': rows,
                          'extracted_scope_changed_paths': scope,
                          'scope_policy': 'all executable instrument AST frozen except default dictionaries; exact base census/ledger retained',
                          'guard_sha256': digest(Path(__file__).read_bytes())}, indent=2, sort_keys=True))
        return int(any(not r['pass'] for r in rows))
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(json.dumps({'cannot_evaluate': str(exc)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
