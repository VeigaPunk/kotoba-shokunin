import mmap,re
h=open("/home/vgpnk/.local/bin/omp","rb")
b=mmap.mmap(h.fileno(),0,access=mmap.ACCESS_READ)

def occ(n, limit=40):
    out,at=[],b.find(n)
    while at>=0 and len(out)<limit:
        out.append(at); at=b.find(n,at+1)
    return out

print("### duplicates")
for pat in [b"var ZO = {", b"return d.join(e.cwd, r.projectDir, n);", b"// packages/coding-agent/src/discovery/helpers.ts",
            b"var Ou = ZO.native;", b"var eh = \".claude\";", b"var y1 = [\".agent\", \".agents\"];",
            b"// packages/coding-agent/src/discovery/builtin.ts", b"// packages/coding-agent/src/discovery/agents.ts",
            b"// packages/coding-agent/src/discovery/codex.ts", b"// packages/coding-agent/src/discovery/claude.ts",
            b"// packages/coding-agent/src/discovery/omp-plugins.ts", b"// packages/coding-agent/src/autolearn/managed-skills.ts"]:
    print(pat.decode(), "->", occ(pat))

print()
print("### what is the 114xxxxxx region? bytes around 114486400")
print(repr(b[114486300:114486900]))
print()
print("### 114489000 region (row2 binary quote)")
print(repr(b[114488950:114489300]))
