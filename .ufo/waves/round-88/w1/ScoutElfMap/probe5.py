import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def ctx(o,bef,aft): return b[max(0,o-bef):o+aft].decode("utf-8","replace")
def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")

print("### managed-skills.ts region 173809642-173810100")
print(ctx(173809642,0,520))
print()
print("### qh() in dirs.ts")
for m in re.finditer(rb"function qh\(", b):
    print(m.start()); print(ctx(m.start(),0,300)); break
print()
print("### agentDir getter in config class")
for m in list(re.finditer(rb"agentDir", b))[:8]:
    print(m.start(), repr(line_at(m.start()))[:180])
print()
print("### .omp/agent literal")
for pat in (rb"\.omp/agent", rb"agentDir\s*="):
    print(pat, [m.start() for m in list(re.finditer(pat,b))[:12]])
