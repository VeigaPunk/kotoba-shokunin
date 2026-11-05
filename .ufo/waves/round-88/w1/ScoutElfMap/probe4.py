import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def ctx(o,bef,aft): return b[max(0,o-bef):o+aft].decode("utf-8","replace")
def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")
def hdr(o):
    hs=[(m.start(),m.group(0).decode()) for m in re.finditer(rb"//[ \t]*packages/[A-Za-z0-9_./@-]+", b[max(0,o-300000):o])]
    return hs[-1] if hs else None

print("### claude-plugins fallback values")
for m in re.finditer(rb"fallback", b):
    if 173830000 < m.start() < 173860000:
        print(m.start(), repr(line_at(m.start()))[:200])
print()
print("### g1 callers / descriptor")
for m in re.finditer(rb"g1\(", b):
    if 173830000 < m.start() < 173860000:
        print(m.start(), repr(line_at(m.start()))[:200])
print()
print("### descriptor with fallback: \"skills\"")
for m in re.finditer(rb"fallback: \"skills\"", b):
    print(m.start(), repr(line_at(m.start()))[:220])
print()
print("### header offsets (absolute) for unledgered reader offsets")
for name,o in [("~/.claude/skills",173840218),("~/.codex/skills",173882129),
               ("~/.config/opencode/skills",172785499),("<agent-plugin>/skills",173778070),
               ("<claude-plugin>/skills",173851107),("~/.omp/plugins/node_modules/*",166892485)]:
    hs=[(m.start(),m.group(0).decode()) for m in re.finditer(rb"//[ \t]*packages/[A-Za-z0-9_./@-]+", b[max(0,o-300000):o])]
    print(name, o, hs[-1] if hs else None)
