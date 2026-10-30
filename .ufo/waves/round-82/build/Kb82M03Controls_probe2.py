#!/usr/bin/env python3
"""Kb82M03Controls probe 2: fixed json-shadow (A6b) and self-pinned omp-strings stub (A10).

Reuses the frozen harness functions from Kb82M03Controls_mutate.py (same guard/counter/commit path).
Fixture-only; scratch clone; no lane/production write.
"""
import importlib.util, json, os, subprocess, sys
from pathlib import Path

BUILD = Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build')
spec = importlib.util.spec_from_file_location('mut', BUILD / 'Kb82M03Controls_mutate.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

SHADOW2 = '''"""Kb82M03Controls fixture: shadows stdlib json for instrument runs only (fixed loader)."""
import os as _o, sys as _s
_me = _s.modules["json"]
_here = _o.path.dirname(_o.path.abspath(__file__))
_saved = _s.path[:]
_s.modules.pop("json", None)
_s.path[:] = [p for p in _saved if _o.path.abspath(p or ".") != _here]
import json as _real
_s.path[:] = _saved
_s.modules["json"] = _me
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

STUB_STR = M.ROOT / 'stub' / 'omp_strings'


def m_A6b():
    M.apply_G()
    (M.CLONE / 'verifiers' / 'json.py').write_text(
        SHADOW2 % (repr(M.canned_pins()), repr(M.canned_surf())), encoding='utf-8')


def m_A10():
    M.apply_G()
    STUB_STR.parent.mkdir(parents=True, exist_ok=True)
    dump = subprocess.run(['strings', '-n', '4', M.LIVE_OMP], capture_output=True, check=True).stdout
    STUB_STR.write_bytes(dump)
    os.utime(STUB_STR, ns=(M.OMP_NS, M.OMP_NS))
    stub = str(STUB_STR)
    M.set_default(M.PINS, stub)
    M.set_default(M.SURF, stub)
    M.set_pin(M.sha(stub), M.OMP_ISO)


def run_guard_selftest():
    t = __import__('time').monotonic()
    p = subprocess.run([sys.executable, '-B', str(M.GUARD), '--self-test'],
                       capture_output=True, text=True, env=M.ENV, cwd=str(M.ROOT))
    return {'exit': p.returncode, 'ms': int((__import__('time').monotonic() - t) * 1000),
            'stdout_tail': p.stdout.strip().splitlines()[-3:], 'stderr_tail': p.stderr.strip()[-200:]}


def main():
    M.ROOT.mkdir(parents=True, exist_ok=True)
    M.TMP.mkdir(parents=True, exist_ok=True)
    M.FROZEN.mkdir(parents=True, exist_ok=True)
    M.assert_top()
    frozen_bytes = subprocess.run(['git', '-C', str(M.CLONE), 'show',
                                   M.BASE + ':verifiers/check_substrate_repin_v2.py'],
                                  capture_output=True, check=True).stdout
    (M.FROZEN / 'check_substrate_repin_v2.py').write_bytes(frozen_bytes)
    out = {'seat': M.SEAT, 'guard_selftest': run_guard_selftest(), 'runs': []}
    print('guard --self-test exit=%d tail=%s' % (out['guard_selftest']['exit'],
                                                 out['guard_selftest']['stdout_tail']), flush=True)
    for name, kind, desc, fn in [
        ('A6b-shadow-json-fixed', 'attack', 'verifiers/json.py shadows stdlib json (fixed loader); instruments byte-identical to G', m_A6b),
        ('A10-self-pinned-omp-strings-stub', 'attack', 'omp defaults+pins -> stub whose bytes are live `strings -n 4` dump (mtime ns = live)', m_A10),
    ]:
        M.reset(M.BASE)
        fn()
        M.git('add', '-A')
        M.git(*M.GIT_ID, 'commit', '-q', '-m', 'Kb82M03 probe2: ' + name)
        rev = M.git('rev-parse', 'HEAD')
        g = M.run_guard(rev)
        c = M.run_counter(rev)
        verdict = M.classify(kind, g, c)
        out['runs'].append({'name': name, 'kind': kind, 'rev': rev, 'description': desc,
                            'guard': g, 'counter': c, 'classification': verdict})
        print('%s guard=%d(red=%s) counter=%d => %s' % (name, g['exit'], g['red'], c['exit'], verdict), flush=True)
        print('   counter stdout:', c['stdout'].replace('\n', ' | ')[:300], flush=True)
        print('   counter stderr:', c['stderr'].replace('\n', ' | ')[-300:], flush=True)
    M.reset(M.BASE)
    (BUILD / 'Kb82M03Controls_probe2.json').write_text(json.dumps(out, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('WROTE probe2', flush=True)


if __name__ == '__main__':
    main()
