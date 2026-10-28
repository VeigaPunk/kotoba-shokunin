#!/usr/bin/env python3
"""Scratch attack driver for Kb81C02C2; runs frozen counter in isolated repos."""
import importlib.util, json, os, shutil, sys
from pathlib import Path
P=Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/check_sdk_allowed_tools.py')
S=Path('/fast/scratch/hyaku/kotoba-r81/Kb81C02C2')
os.environ['TMPDIR']=str(S/'tmp')
(S/'tmp').mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('counter',P); c=importlib.util.module_from_spec(spec); sys.modules['counter']=c; spec.loader.exec_module(c)
c._WORK=str(S/'work'); Path(c._WORK).mkdir(parents=True,exist_ok=True)
base=c._honest(); pin=c.SNAPSHOT_PIN; body=c.FIX_PAGE

def run(label, files, expected=None):
    d, rev=c._world(files)
    old=(c.BASE_REV,c.SNAPSHOT_PIN,c._INTERNAL_SELFTEST)
    import hashlib, io
    from contextlib import redirect_stdout, redirect_stderr
    body = files.get(c.SNAPSHOT_PATH)
    run_pin = pin if body is None else hashlib.sha256(body.encode() if isinstance(body,str) else body).hexdigest()
    c.BASE_REV=rev; c.SNAPSHOT_PIN=run_pin; c._INTERNAL_SELFTEST=True
    try:
        out=io.StringIO()
        try:
            with redirect_stdout(out),redirect_stderr(out): rc=c.main(['--repo',d,'--rev','HEAD','--work',c._WORK])
        except Exception as e:
            rc='EXC'; out.write(type(e).__name__+': '+str(e))
        text=out.getvalue()
    finally:
        c.BASE_REV,c.SNAPSHOT_PIN,c._INTERNAL_SELFTEST=old
        shutil.rmtree(d,ignore_errors=True)
    print(f'WORLD {label}\nexit={rc}\n{text.rstrip()}\n')

# (a) authoritative snapshot at a different path only; fixed path cannot resolve.
f=dict(base); f.pop(c.SNAPSHOT_PATH); f['.ufo/waves/round-81/snapshots/renamed/S249.md']=body
run('A alternate snapshot path',f)
# (b) real bytes + valid S249, but S248 used-by kept at the base value.
f=dict(base); f[c.SOURCES]=c._reg({c.SNAPSHOT_ID:c.FIX_PAGE},s248_used_by='—')
run('B S249 updated; S248 unchanged',f)
# (c) quote moved before first heading, with all content identities coherently repinned.
changed='The allowedTools option in your query configuration is stated here.\n\n# Agent SDK skills\n\n## Later\n\nBody text.\n'
f=c._honest({c.SNAPSHOT_ID:changed},entry=c._entry(quote='The allowedTools option in your query configuration is stated here'))
run('C quote before first heading with repinned bytes',f)
# (d) unrelated page at same canonical URL bytes: valid but unrelated body retains the quoted field phrase.
unrelated='# Other Product\n\n## Tools\n\nThe allowedTools option in your query configuration is stated here.\n'
f=c._honest({c.SNAPSHOT_ID:unrelated},entry=c._entry(quote='The allowedTools option in your query configuration is stated here'))
run('D unrelated bytes behind canonical URL metadata',f)
# (e1) strongest weak-quote control: valid token-bearing quote about an unrelated feature.
body2=c.FIX_PAGE.replace('In SDK sessions, you can pre-approve tools for a project or personal skill with the skill\'s `allowed-tools` frontmatter or with the `allowedTools` option (`allowed_tools` in Python) in your query configuration.', 'The allowedTools option appears in this unrelated example for formatting only.')
q='The allowedTools option appears in this unrelated example for formatting only.'
f=c._honest({c.SNAPSHOT_ID:body2},entry=c._entry(quote=q))
run('E unrelated quote with token, in valid text view',f)
# (e2) byte-count/date lie in anchor while SHA/path are correct.
f=dict(base); rows=c._reg({c.SNAPSHOT_ID:c.FIX_PAGE}); f[c.SOURCES]=rows.replace(f'{len(body.encode())} B', '1 B').replace(f'fetched {c.CAPTURE}', 'fetched 1970-01-01')
run('F wrong anchor byte count and stale date',f)
# (e3) basename-in-substring satisfies snapshot_named; it must be rejected only if exact path required.
f=dict(base); f[c.SOURCES]=c._reg({c.SNAPSHOT_ID:c.FIX_PAGE}); f[c.SOURCES]=f[c.SOURCES].replace(c.SNAPSHOT_PATH, 'unrelated/S249.md.bak')
run('G anchor mentions S249.md.bak only',f)
# (e4) fetch record wrong URL but correct pin and bytes.
bodyhash=__import__('hashlib').sha256(body.encode()).hexdigest()
f=dict(base); f[c.FETCH_JSON]=json.dumps({'url':'https://unrelated.example/other.md','http':200,'bytes':len(body.encode()),'sha256':bodyhash})
run('H fetch record URL unrelated but pin/size match',f)
# (f) no heading means first-heading requirement should be impossible, but the
# current locator treats the missing first heading as no positional constraint.
headless='The allowedTools option appears in this unrelated example for formatting only.\n'
f=c._honest({c.SNAPSHOT_ID:headless},entry=c._entry(quote='The allowedTools option appears in this unrelated example for formatting only.'))
run('I headingless snapshot quote',f)
