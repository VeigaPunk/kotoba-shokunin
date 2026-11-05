import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")
def ctx(o,bef,aft): return b[max(0,o-bef):o+aft].decode("utf-8","replace")

print("### function jp( definition")
for m in re.finditer(rb"function jp\(", b):
    print(m.start()); print(ctx(m.start(),0,700)); print("---")
print()
print("### configDir getter")
for m in re.finditer(rb"configDir", b):
    if 172770000 < m.start() < 172790000:
        print(m.start(), repr(line_at(m.start()))[:180])
print()
print("### Ac( call sites with \"skills\"")
for m in re.finditer(rb"Ac\(", b):
    if 172780000 < m.start() < 172800000 or 173900000 < m.start() < 173950000:
        print(m.start(), repr(line_at(m.start()))[:200])
print()
print("### os( call sites (projectDir helper)")
for m in re.finditer(rb"\bos\(", b):
    if 172780000 < m.start() < 172800000:
        print(m.start(), repr(line_at(m.start()))[:200])
