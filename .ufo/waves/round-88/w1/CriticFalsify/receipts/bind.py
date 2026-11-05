import mmap, re
fh=open("/home/vgpnk/.local/bin/omp","rb"); b=mmap.mmap(fh.fileno(),0,access=mmap.ACCESS_READ)
def line(off):
    s=b.rfind(b"\n",max(0,off-8192),off); s=0 if s<0 else s+1
    e=b.find(b"\n",off,off+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf8","replace")
# forged lines (r87 worlds) and the root literal tokens a legal binding set may draw from
forged = {
 "w_cross_row7 (.github/skills <- codex line)": (173879095, ".github/skills", ["github","skills","projectDir","cwd","join","d.join","e.cwd","n"]),
 "w_misattr_row12 (managed-skills <- plugins line)": (173914936, "~/.omp/agent/managed-skills", ["managed-skills","managed","skills","agent",".omp","omp","join"]),
 "w_renderline_row6 (.opencode/skills <- render line)": (188589625, ".opencode/skills", ["opencode","skills","projectDir","cwd","join"]),
}
for name,(off,pat,toks) in forged.items():
    ln=line(off)
    hit=[t for t in toks if t in ln]
    print(f"{name}\n   line={ln.strip()[:120]!r}\n   candidate binding tokens present on forged line: {hit}")
# Wne walk-up definition (rows 3,4,10,11 reader is x.push(Rs.join(R,_,...p)) / Wne(u)).
for pat in [rb"Wne\s*=", rb"function Wne", rb"Wne\(u\)\{", rb"Wne=\("]:
    m=[x.start() for x in re.finditer(pat,b)][:3]
    print("pattern",pat,"offsets",m)
