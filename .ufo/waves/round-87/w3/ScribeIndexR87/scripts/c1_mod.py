import mmap, re
ELF="/home/vgpnk/.local/bin/omp"
f=open(ELF,"rb"); blob=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
HDR=re.compile(rb"//[ \t]*packages/([A-Za-z0-9_./@-]+)")
hdrs={}
for m in HDR.finditer(blob):
    hdrs.setdefault(m.group(1).decode(), []).append(m.start())
print("distinct packages headers in ELF:", len(hdrs))
mods=["coding-agent/src/discovery/builtin.ts","coding-agent/src/discovery/claude.ts","coding-agent/src/discovery/agents.ts","coding-agent/src/discovery/codex.ts","coding-agent/src/discovery/helpers.ts","coding-agent/src/discovery/omp-plugins.ts","coding-agent/src/autolearn/managed-skills.ts"]
readers={"builtin .omp/skills":b'dir: fr.join(k, Ou.projectDir, "skills"),',
 "claude":b'dir: Fr.join(k, eh, "skills"),',
 "agents push":b'x.push(Rs.join(R, _, ...p));',
 "codex":b'return Xr.join(u.cwd, ".codex");',
 "helpers":b'return d.join(e.cwd, r.projectDir, n);',
 "plugins":b'dir: Zo.join(R.path, "skills"),',
 "managed":b'return Zm.join(u, "managed-skills");'}
rofs={k:blob.find(v) for k,v in readers.items()}
for k,v in rofs.items(): print(f"reader {k!r} first@{v}")
for m in mods:
    last=hdrs.get(m,[None])[-1] if m in hdrs else None
    print(f"module {m}: header_count={len(hdrs.get(m,[]))} last@{last}")
print("--- which (module, reader) pairs satisfy conjunct 3 ordering (quote first_occurrence >= last header):")
for m in mods:
    if m not in hdrs: continue
    last=hdrs[m][-1]
    ok=[k for k,v in rofs.items() if v>=last]
    print(f"  {m}: passes ordering for readers {ok}")
