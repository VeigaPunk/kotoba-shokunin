import mmap, hashlib, sys, re
p="/home/vgpnk/.local/bin/omp"
h=open(p,'rb'); b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
print("sha256", hashlib.sha256(b).hexdigest())
def line(off):
    s=b.rfind(b"\n",max(0,off-8192),off); s=0 if s<0 else s+1
    e=b.find(b"\n",off,off+8192); e=b.size() if e<0 else e
    return b[s:e]
# forged-world quote lines (r87 worlds) and honest quote lines
cases = {
 "honest r7 .github (quote=r6 line)": (172785704, b'return d.join(e.cwd, r.projectDir, n);'),
 "forged w_cross_row7 (.github<-codex)": (173879095, b'return Xr.join(u.cwd, ".codex");'),
 "forged w_misattr_row12 (managed<-plugins)": (173914936, b'dir: Zo.join(R.path, "skills"),'),
 "forged w_renderline_row6 (opencode<-render)": (188589625, None),
}
for name,(off,q) in cases.items():
    ln = line(off)
    print("\n##", name, "@", off, "linelen", len(ln))
    print("   line:", ln[:300])
# token survey: join-token lines carrying candidate generic tokens
join=(b"join(",b".join(",b"resolve(",b"path.join")
def is_join(l): return any(j in l for j in join)
toks=[b"skills",b"cwd",b"projectDir",b"managed-skills",b".codex",b".github",b"agent",b".omp"]
# walk all newline-delimited lines once, cheap enough for 277MB? sample by regex finditer on join tokens
hits={t:0 for t in toks}; total=0
for m in re.finditer(rb"[^\n]{0,200}(?:join\(|\.join\(|resolve\(|path\.join)[^\n]{0,200}", b, flags=0):
    total+=1
    s=m.group(0)
    for t in toks:
        if t in s: hits[t]+=1
    if total>400000: break
print("\njoin-carrying line sample total", total)
for t in toks: print(f"  join-lines containing {t!r}: {hits[t]}")
