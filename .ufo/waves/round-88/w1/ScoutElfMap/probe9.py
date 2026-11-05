import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")
def ctx(o,bef,aft): return b[max(0,o-bef):o+aft].decode("utf-8","replace")

for pat in (rb"function we\(", rb"function \$o\(", rb"function M\(", rb"function qh\("):
    for m in re.finditer(pat, b):
        if 166880000 < m.start() < 166900000:
            print(pat, m.start(), repr(line_at(m.start()))[:120])
print()
print("### class e constructor agentDir default")
print(ctx(166888490,0,700))
print()
print("### opencode/github caller contexts")
print(ctx(173903100,0,300))
print("...")
print(ctx(173910410,0,260))
