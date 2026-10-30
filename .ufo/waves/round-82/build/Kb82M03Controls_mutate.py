#!/usr/bin/env python3
"""Kb82M03Controls: mutation probe of the E19 frozen C1 guard and the unchanged C1 counter.

Fixture-only. All mutants are commits in the scratch clone (never a lane/production file).
The live omp/opencode bytes are read, never written. Stubs and aliases live under scratch.
"""
import hashlib, json, os, subprocess, sys, time
from pathlib import Path

SEAT = 'Kb82M03Controls'
ROOT = Path('/fast/scratch/hyaku/kotoba-r82') / SEAT
CLONE = ROOT / 'clone'
TMP = ROOT / 'tmp'
FROZEN = ROOT / 'frozen'
STUB = ROOT / 'stub' / 'omp'
ALIAS = ROOT / 'alias' / 'omp'
BUILD = Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build')
GUARD = BUILD / 'Kb82E19PinGuard_guard.py'
OUT = BUILD / 'Kb82M03Controls_mutants.json'
BASE = '47dbe8781657de563ff867caca6244d28e3db504'
LIVE_OMP = '/home/vgpnk/.local/bin/omp'
LIVE_OC = '/home/vgpnk/.opencode/bin/opencode'
OMP_SHA = 'e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f'
OC_SHA = 'ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7'
OMP_NS = 1793326786168359786
OMP_ISO = '2026-10-29T23:19:46.168359786-03:00'
STALE_SHA = '9513ef9f19d7991aac6ae0cb6077bcf16662092ddde861c002a91cedc6f47f9a'
OLD_LINE = '"omp": "/home/vgpnk/.local/bin/omp.real"'
NEW_LINE = '"omp": "/home/vgpnk/.local/bin/omp"'
PINS = 'verifiers/check_substrate_pins.py'
SURF = 'verifiers/verify_surfaces.py'
BL = 'verifiers/baseline.json'
SB = 'verifiers/surfaces-baseline.json'
INV = 'corpus/knowledge/instruction-surface-census-round13.md'
CLASS = 'omp:agents-md/AGENTS.md'
GIT_ID = ['-c', 'user.name=Kb82M03Controls', '-c', 'user.email=Kb82M03Controls@scratch.invalid']
ENV = dict(os.environ, TMPDIR=str(TMP))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def git(*args):
    p = subprocess.run(['git', '-C', str(CLONE), *args], capture_output=True, text=True)
    if p.returncode:
        raise SystemExit('git %s rc=%d %s' % (args, p.returncode, p.stderr.strip()))
    return p.stdout.strip()


def assert_top():
    top = subprocess.run(['git', '-C', str(CLONE), 'rev-parse', '--show-toplevel'],
                         capture_output=True, text=True, check=True).stdout.strip()
    if top != str(CLONE):
        raise SystemExit('toplevel mismatch: ' + top)


def reset(rev):
    assert_top()
    git('checkout', '-q', '-f', '--detach', rev)
    git('clean', '-fdxq', '--', 'verifiers', 'corpus')


def edit(rel, old, new, count=1):
    p = CLONE / rel
    s = p.read_text(encoding='utf-8')
    n = s.count(old)
    if n != count:
        raise SystemExit('%s: %d match(es) for %r' % (rel, n, old[:70]))
    p.write_text(s.replace(old, new), encoding='utf-8')


def edit_json(rel, fn):
    p = CLONE / rel
    d = json.loads(p.read_text(encoding='utf-8'))
    fn(d)
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


def set_default(rel, path):
    edit(rel, NEW_LINE, '"omp": "%s"' % path)


def set_pin(sha_val=None, mtime=None):
    def f(d):
        m = d['measured_against']
        if sha_val is not None:
            m['omp_binary_sha256'] = sha_val
        if mtime is not None:
            m['omp_binary_mtime'] = mtime
    edit_json(BL, f)


def make_stub():
    STUB.parent.mkdir(parents=True, exist_ok=True)
    STUB.write_bytes(b'#!/bin/sh\necho omp/18.14.0\n')
    os.utime(STUB, ns=(OMP_NS, OMP_NS))
    return str(STUB)


def apply_G():
    edit(PINS, OLD_LINE, NEW_LINE)
    edit(SURF, OLD_LINE, NEW_LINE)
    set_pin(OMP_SHA, OMP_ISO)


def m_A1():
    apply_G()
    set_pin(sha_val=STALE_SHA)


def m_A2():
    apply_G()
    set_pin(mtime='2026-10-29T23:19:46.168359785-03:00')


def m_A3():
    apply_G()
    stub = make_stub()
    set_default(PINS, stub)
    set_default(SURF, stub)
    set_pin(sha(stub), OMP_ISO)


def canned_pins():
    return {'checks': [
        {'pin': 'omp_binary_sha256', 'verdict': 'PASS', 'expect': OMP_SHA, 'observed': OMP_SHA},
        {'pin': 'omp_binary_mtime', 'verdict': 'PASS', 'expect': OMP_ISO},
        {'pin': 'opencode_binary_sha256', 'verdict': 'PASS', 'expect': OC_SHA, 'observed': OC_SHA}]}


def canned_surf():
    return {'checks': [{'id': i, 'status': 'PASS'} for i in range(7)]}


def m_A4():
    apply_G()
    (CLONE / PINS).write_text('print(%r)\n' % json.dumps(canned_pins()), encoding='utf-8')


def m_A5():
    apply_G()
    (CLONE / SURF).write_text('print(%r)\n' % json.dumps(canned_surf()), encoding='utf-8')


SHADOW = '''"""Kb82M03Controls fixture: shadows stdlib json for instrument runs only."""
import importlib.util as _u, os as _o, sys as _s, sysconfig as _c
_p = _o.path.join(_c.get_paths()["stdlib"], "json", "__init__.py")
_spec = _u.spec_from_file_location("_stdlib_json", _p, submodule_search_locations=[_o.path.dirname(_p)])
_real = _u.module_from_spec(_spec)
_s.modules["_stdlib_json"] = _real
_spec.loader.exec_module(_real)
for _k, _v in vars(_real).items():
    if not _k.startswith("__"):
        globals()[_k] = _v
_PAY_PINS = %s
_PAY_SURF = %s
def dumps(obj, *a, **k):
    name = _o.path.basename(_s.argv[0])
    if name == "check_substrate_pins.py":
        return _real.dumps(_PAY_PINS, *a, **k)
    if name == "verify_surfaces.py":
        return _real.dumps(_PAY_SURF, *a, **k)
    return _real.dumps(obj, *a, **k)
'''


def m_A6():
    apply_G()
    (CLONE / 'verifiers' / 'json.py').write_text(SHADOW % (repr(canned_pins()), repr(canned_surf())), encoding='utf-8')


def m_A7():
    apply_G()

    def f(d):
        before = len(d['classes'])
        d['classes'] = [c for c in d['classes'] if c['class_id'] != CLASS]
        if len(d['classes']) != before - 1:
            raise SystemExit('class not found for deletion')
    edit_json(SB, f)


def m_A8():
    m_A7()
    p = CLONE / INV
    lines = p.read_text(encoding='utf-8').splitlines(keepends=True)
    keep = [l for l in lines if not (l.lstrip().startswith('|') and ('`%s`' % CLASS) in l)]
    if len(keep) == len(lines):
        raise SystemExit('no inventory row for ' + CLASS)
    p.write_text(''.join(keep), encoding='utf-8')


def m_A9():
    apply_G()
    stub = make_stub()
    edit_json(BL, lambda d: d['measured_against'].update({'omp_binary_path': stub}))


def m_C10():
    apply_G()
    ALIAS.parent.mkdir(parents=True, exist_ok=True)
    if ALIAS.is_symlink() or ALIAS.exists():
        ALIAS.unlink()
    os.symlink(LIVE_OMP, ALIAS)
    set_default(PINS, str(ALIAS))
    set_default(SURF, str(ALIAS))


def m_C11():
    apply_G()
    p = CLONE / PINS
    p.write_text(p.read_text(encoding='utf-8') + '\n# Kb82M03 probe: comment-only edit.\n', encoding='utf-8')


MUTANTS = [
    # name, kind, description, mutation
    ('C0-green-candidate', 'control', 'minimal live re-pin: defaults + pins at live omp bytes', apply_G),
    ('A1-wrong-omp-digest', 'attack', 'pin sha replaced by stale 18.12.2 digest; defaults live', m_A1),
    ('A2-ns-mtime-off-by-one', 'attack', 'pin mtime one nanosecond off; defaults live', m_A2),
    ('A3-self-pinned-stub-omp', 'attack', 'defaults+pins point at same-mtime stub; stub sha self-pinned', m_A3),
    ('A4-stub-output-pins-script', 'attack', 'check_substrate_pins.py replaced by canned PASS printer', m_A4),
    ('A5-stub-output-surfaces-script', 'attack', 'verify_surfaces.py replaced by canned 7-PASS printer', m_A5),
    ('A6-shadow-json-module-outside-guard-scope', 'attack', 'verifiers/json.py shadows stdlib json; both instruments byte-identical to G', m_A6),
    ('A7-class-deleted-baseline-only', 'attack', 'omp:agents-md/AGENTS.md deleted from surfaces-baseline; inventory untouched', m_A7),
    ('A8-class-deleted-baseline-and-inventory', 'attack', 'class deleted from baseline and inventory row removed', m_A8),
    ('A9-baseline-path-key-tamper', 'attack', 'extra measured_against key omp_binary_path -> stub; pins/defaults live', m_A9),
    ('C10-symlink-to-live-bytes', 'control', 'defaults via symlink to live omp; identity is bytes, expected accepted', m_C10),
    ('C11-comment-only-edit', 'control', 'comment appended to pins script; AST-insensitive, expected accepted', m_C11),
]


def run_guard(rev):
    t = time.monotonic()
    p = subprocess.run([sys.executable, '-B', str(GUARD), '--repo', str(CLONE), '--rev', rev],
                       capture_output=True, text=True, env=ENV, cwd=str(ROOT))
    ms = int((time.monotonic() - t) * 1000)
    out = {'exit': p.returncode, 'ms': ms, 'stderr_tail': p.stderr.strip()[-300:]}
    try:
        j = json.loads(p.stdout)
        out['red'] = [c['check'] for c in j.get('checks', []) if not c['pass']]
        out['checks'] = [(c['check'], c['pass']) for c in j.get('checks', [])]
        out['cannot_evaluate'] = j.get('cannot_evaluate')
    except ValueError:
        out['red'] = []
        out['cannot_evaluate'] = 'non-json stdout: ' + p.stdout[:200]
    return out


def run_counter(rev):
    t = time.monotonic()
    p = subprocess.run([sys.executable, '-B', str(FROZEN / 'check_substrate_repin_v2.py'),
                        '--rev', rev, '--repo', str(CLONE)],
                       capture_output=True, text=True, env=ENV, cwd=str(ROOT))
    ms = int((time.monotonic() - t) * 1000)
    return {'exit': p.returncode, 'ms': ms, 'stdout': p.stdout.strip(), 'stderr': p.stderr.strip()[-500:]}


def classify(kind, g, c):
    if kind == 'control':
        return 'accepted' if g['exit'] == 0 else 'FALSE-REJECT'
    if g['exit'] != 0:
        return 'killed-by-guard'
    if c['exit'] == 0:
        return 'SURVIVED-guard-and-counter'
    return 'survived-guard-killed-by-counter'


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    FROZEN.mkdir(parents=True, exist_ok=True)
    assert_top()
    if sha(LIVE_OMP) != OMP_SHA or sha(LIVE_OC) != OC_SHA:
        raise SystemExit('live host bytes differ from frozen identities; abort')
    frozen_bytes = subprocess.run(['git', '-C', str(CLONE), 'show', BASE + ':verifiers/check_substrate_repin_v2.py'],
                                  capture_output=True, check=True).stdout
    (FROZEN / 'check_substrate_repin_v2.py').write_bytes(frozen_bytes)
    report = {'seat': SEAT, 'base': BASE, 'live_omp_sha256': OMP_SHA, 'live_opencode_sha256': OC_SHA,
              'counter_sha256': hashlib.sha256(frozen_bytes).hexdigest(),
              'guard_sha256': sha(GUARD), 'guard_exit_expected_base': 1, 'runs': []}

    # base control: frozen before state, expected guard red and counter exit 2
    reset(BASE)
    base_rev = BASE
    g = run_guard(base_rev)
    c = run_counter(base_rev)
    report['runs'].append({'name': 'B0-base-unchanged', 'kind': 'base', 'rev': base_rev,
                           'description': 'unchanged base 47dbe87', 'guard': g, 'counter': c,
                           'classification': 'red-as-expected' if g['exit'] != 0 else 'UNEXPECTED-GREEN'})
    print('B0 guard=%d counter=%d' % (g['exit'], c['exit']), flush=True)

    # build G then mutants on top of G
    reset(BASE)
    apply_G()
    git('add', '-A')
    git(*GIT_ID, 'commit', '-q', '-m', 'Kb82M03 fixture: G good candidate (scratch only)')
    g_rev = git('rev-parse', 'HEAD')
    for name, kind, desc, fn in MUTANTS:
        reset(BASE)
        fn()
        git('add', '-A')
        git(*GIT_ID, 'commit', '-q', '-m', 'Kb82M03 fixture: ' + name)
        rev = git('rev-parse', 'HEAD')
        load0 = os.getloadavg()[0]
        g = run_guard(rev)
        c = run_counter(rev)
        verdict = classify(kind, g, c)
        report['runs'].append({'name': name, 'kind': kind, 'rev': rev, 'parent': g_rev,
                               'description': desc, 'load1_before_guard': round(load0, 2),
                               'guard': g, 'counter': c, 'classification': verdict})
        print('%s guard=%d(red=%s) counter=%d => %s' % (name, g['exit'], g['red'], c['exit'], verdict), flush=True)

    reset(BASE)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('WROTE', OUT, flush=True)


if __name__ == '__main__':
    main()
