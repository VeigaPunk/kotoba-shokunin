import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)

def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")

def ctx(o,bef,aft):
    return b[max(0,o-bef):o+aft].decode("utf-8","replace")

def header_before(o):
    hdrs=[(m.start(), m.group(0).decode()) for m in re.finditer(rb"//[ \t]*packages/[A-Za-z0-9_./@-]+", b[max(0,o-200000):o])]
    return hdrs[-1] if hdrs else None

print("### codex region 173882050-173882300")
print(ctx(173882050,0,260))
print()
print("### 173882193 line:", repr(line_at(173882193)))
print()
print("### dFe definition search")
for m in re.finditer(rb"function dFe\(", b):
    print("dFe at", m.start(), repr(line_at(m.start())))
    print(ctx(m.start(), 0, 700))
print()
print("### agentDir / we() semantics")
for pat in (rb"agentDir", rb"rootSubdir"):
    ms=[m.start() for m in re.finditer(pat, b)]
    print(pat, len(ms), ms[:5])
# find class e config agentDir getter
for m in list(re.finditer(rb"get agentDir\(\)", b))[:3]:
    print("get agentDir at", m.start())
    print(ctx(m.start(), 0, 500))
print()
print("### module header before each ledger reader offset and each unledgered offset")
LED=[("{cwd}/.omp/skills",173819979),("{cwd}/.claude/skills",173840364),("{cwd}/.agent/skills",173865724),
     ("{cwd}/.agents/skills",173865724),("{cwd}/.codex/skills",173879095),("{cwd}/.opencode/skills",172785704),
     ("{cwd}/.github/skills",172785704),("~/.omp/agent/skills",173820135),
     ("~/.omp/plugins/node_modules/*/skills",173914936),("~/.agent/skills",173865523),
     ("~/.agents/skills",173865523),("~/.omp/agent/managed-skills",173809938)]
UNL=[("~/.claude/skills",173840218),("~/.codex/skills",173882129),("~/.config/opencode/skills",172785499),
     ("<agent-plugin>/skills",173778070),("<claude-plugin>/skills",173851107),("~/.omp/plugins/node_modules/*",166892485)]
for name,o in LED+UNL:
    print(f"{name}\t{o}\theader={header_before(o)}")
