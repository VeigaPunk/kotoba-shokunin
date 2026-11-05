import mmap, re, sys, json

P = "/home/vgpnk/.local/bin/omp"
JOIN_TOKENS = ("join(", ".join(", "resolve(", "path.join")

CANDS = [
 ("{cwd}/.omp/skills", "coding-agent/src/discovery/builtin.ts", 'dir: fr.join(k, Ou.projectDir, "skills"),'),
 ("{cwd}/.claude/skills", "coding-agent/src/discovery/claude.ts", 'dir: Fr.join(k, eh, "skills"),'),
 ("{cwd}/.agent/skills", "coding-agent/src/discovery/agents.ts", 'x.push(Rs.join(R, _, ...p));'),
 ("{cwd}/.agents/skills", "coding-agent/src/discovery/agents.ts", 'x.push(Rs.join(R, _, ...p));'),
 ("{cwd}/.codex/skills", "coding-agent/src/discovery/codex.ts", 'return Xr.join(u.cwd, ".codex");'),
 ("{cwd}/.opencode/skills", "coding-agent/src/discovery/helpers.ts", 'return d.join(e.cwd, r.projectDir, n);'),
 ("{cwd}/.github/skills", "coding-agent/src/discovery/helpers.ts", 'return d.join(e.cwd, r.projectDir, n);'),
 ("~/.omp/agent/skills", "coding-agent/src/discovery/builtin.ts", 'dir: fr.join(we(), "skills"),'),
 ("~/.omp/plugins/node_modules/*/skills", "coding-agent/src/discovery/omp-plugins.ts", 'dir: Zo.join(R.path, "skills"),'),
 ("~/.agent/skills", "coding-agent/src/discovery/agents.ts", 'return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));'),
 ("~/.agents/skills", "coding-agent/src/discovery/agents.ts", 'return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));'),
 ("~/.omp/agent/managed-skills", "coding-agent/src/autolearn/managed-skills.ts", 'return Zm.join(u, "managed-skills");'),
]

f = open(P, "rb"); m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

def line_at(off):
    a = m.rfind(b"\n", 0, off) + 1
    b = m.find(b"\n", off)
    if b < 0: b = len(m)
    return m[a:b].decode("utf-8", "replace")

def all_offsets(needle):
    out = []
    start = 0
    nb = needle.encode()
    while True:
        i = m.find(nb, start)
        if i < 0: break
        out.append(i)
        start = i + 1
    return out

hdr_cache = {}
def header_offsets(module):
    if module not in hdr_cache:
        needle = ("// packages/" + module).encode()
        offs = []
        start = 0
        while True:
            i = m.find(needle, start)
            if i < 0: break
            offs.append(i)
            start = i + 1
        hdr_cache[module] = offs
    return hdr_cache[module]

rows = []
fails = 0
for pat, mod, quote in CANDS:
    offs = all_offsets(quote)
    hdrs = header_offsets(mod)
    ok_len = len(quote) >= 12
    ok_one = "\n" not in quote and "\t" not in quote
    ok_join = any(t in quote for t in JOIN_TOKENS)
    ok_found = bool(offs)
    first = offs[0] if offs else -1
    ok_after = bool(hdrs) and ok_found and first > hdrs[-1]
    ok_line = ok_found and any(t in line_at(first) for t in JOIN_TOKENS)
    ok = all([ok_len, ok_one, ok_join, ok_found, ok_after, ok_line])
    if not ok: fails += 1
    rows.append(dict(pat=pat, mod=mod, quote=quote, n=len(offs), first=first,
                     hdr_first=hdrs[0] if hdrs else -1, hdr_last=hdrs[-1] if hdrs else -1,
                     hdr_n=len(hdrs), ok=ok, line=line_at(first) if ok_found else ""))
    print(f"{'OK ' if ok else 'BAD'} first={first:>10} nhdr={len(hdrs)} hdr_last={hdrs[-1] if hdrs else -1:>10} occ={len(offs)} {pat}")
    print(f"      mod={mod}")
    print(f"      quote={quote!r}")
    if not ok:
        print(f"      len={ok_len} one_line={ok_one} join={ok_join} found={ok_found} after_hdr={ok_after} line_join={ok_line}")
print("FAILS", fails)
json.dump(rows, open("verify.json","w"), indent=1)
