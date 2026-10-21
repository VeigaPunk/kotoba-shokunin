import re, json
from pathlib import Path
OM = Path('/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings').read_text(errors='replace')
ASSIGN = re.compile(r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*"([^"\\\n]{1,80})"')
bind = {}
for m in ASSIGN.finditer(OM):
    bind.setdefault(m.group(1), set()).add(m.group(2))
# generic shape: NAME(<v>, <group|var>, "<file>.md")  -- callee name left open
SHAPE = re.compile(r'(?<![A-Za-z0-9_$.])([A-Za-z_$][A-Za-z0-9_$]{0,3})\(\s*u\s*,\s*("([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*"([A-Za-z0-9_./-]+\.md)"\s*[,)]')
rows = []
for m in SHAPE.finditer(OM):
    callee, grp_lit, grp_var, f = m.group(1), m.group(3), m.group(4), m.group(5)
    groups = [grp_lit] if grp_lit else sorted(bind.get(grp_var, {f'UNBOUND:{grp_var}'}))
    line = OM.count('\n', 0, m.start()) + 1
    for g in groups:
        rows.append({'callee': callee, 'group': g, 'file': f, 'line': line, 'group_via': 'literal' if grp_lit else f'var {grp_var}'})
uniq = sorted({(r['callee'], r['group'], r['file'], r['line'], r['group_via']) for r in rows}, key=lambda t: t[3])
for u in uniq: print(u)
base = ['agents-md/AGENTS.md','claude-md/CLAUDE.md','opencode/AGENTS.md','gemini/GEMINI.md','gemini/system.md','gemini/SYSTEM_TEMPLATE.md','github/copilot-instructions.md','windsurf/memories/global_rules.md']
got = {f'{g}/{f}' for (_,g,f,_,_) in uniq if not g.startswith('UNBOUND')}
print('baseline 8 loader ids reproduced by generic shape:', sum(1 for b in base if b in got), '/', len(base))
print('missing:', [b for b in base if b not in got])
print('extra ids (not in baseline 8):', sorted(got - set(base)))
print('callee names:', sorted({u[0] for u in uniq}))
# name-collision probe: how many distinct top-level definitions of each callee name
for name in ['Xl','Fo','lq']:
    defs = re.findall(r'(?:function %s\(|(?:var|let|const) %s\s*=)' % (name, name), OM)
    print(name, 'definitions/declarations:', len(defs))
