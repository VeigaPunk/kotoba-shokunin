import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")
def ctx(o,bef,aft): return b[max(0,o-bef):o+aft].decode("utf-8","replace")

print("### jp configDir helper @170545336")
print(ctx(170545336,0,800))
print()
print("### Ac( callers with 'skills' (search whole ELF for Ac(<x>, \"skills\") style)")
for m in re.finditer(rb"Ac\(", b):
    ln = line_at(m.start())
    if "skills" in ln:
        print(m.start(), repr(ln)[:200])
print()
print("### os( callers with 'skills'")
for m in re.finditer(rb"\bos\(", b):
    ln = line_at(m.start())
    if "skills" in ln or "Ac" in ln:
        print(m.start(), repr(ln)[:200])
