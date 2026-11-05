import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def ctx(o,bef,aft): return b[max(0,o-bef):o+aft].decode("utf-8","replace")
def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")

print("### dFe occurrences")
for m in re.finditer(rb"dFe", b):
    print(m.start(), repr(line_at(m.start()))[:160])
print()
print("### ul( occurrences near codex")
for m in list(re.finditer(rb"\bul\b", b))[:1]: pass
for m in list(re.finditer(rb"function ul\(", b))[:3]:
    print("ul at", m.start()); print(ctx(m.start(),0,400))
print()
print("### codex.ts module region 173878900-173880400")
print(ctx(173878972,0,1500))
