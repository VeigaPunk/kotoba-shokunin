import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)
def line_at(o):
    s=b.rfind(b"\n",max(0,o-8192),o); s=0 if s<0 else s+1
    e=b.find(b"\n",o,o+8192); e=b.size() if e<0 else e
    return b[s:e].decode("utf-8","replace")
def ctx(o,bef,aft): return b[max(0,o-bef):o+aft].decode("utf-8","replace")

print("### y1 literal offsets (agents.ts module, header 173864077)")
for lit in (b'".agent"', b'".agents"'):
    ms=[m.start() for m in re.finditer(re.escape(lit), b)]
    print(lit, [m for m in ms if 173864077 < m < 173870000], [line_at(m)[:80] for m in ms if 173864077 < m < 173870000])
print()
print("### ZO table: .opencode / .github projectDir offsets (helpers.ts module, header 172783788)")
for lit in (b'".opencode"', b'".github"', b'".config/opencode"'):
    ms=[m.start() for m in re.finditer(re.escape(lit), b)]
    keep=[m for m in ms if 172783788 < m < 172790000]
    print(lit, keep, [line_at(m)[:70] for m in keep])
print()
print("### callers of Ac( / V$e( with \"skills\"")
for m in re.finditer(rb"Ac\(", b):
    if 172780000 < m.start() < 172795000:
        print(m.start(), repr(line_at(m.start()))[:160])
print()
print("### ZO.opencode / ZO.github use sites (helper module region)")
for m in re.finditer(rb"ZO\.", b):
    if 172780000 < m.start() < 172800000:
        print(m.start(), repr(line_at(m.start()))[:160])
print()
print("### node_modules / plugins dir composition")
for m in re.finditer(rb'"node_modules"', b):
    print(m.start(), repr(line_at(m.start()))[:140])
print()
print("### \$o( definition")
for m in re.finditer(rb"function \$o\(", b):
    print(m.start()); print(ctx(m.start(),0,300))
