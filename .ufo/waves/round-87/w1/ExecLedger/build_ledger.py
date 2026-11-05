import subprocess, sys, mmap, json
LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
OUT = LANE + "/verifiers/omp-skill-roots-semantics.tsv"
ELF = "/home/vgpnk/.local/bin/omp"

MAP = {
 "{cwd}/.omp/skills": ("coding-agent/src/discovery/builtin.ts", 'dir: fr.join(k, Ou.projectDir, "skills"),'),
 "{cwd}/.claude/skills": ("coding-agent/src/discovery/claude.ts", 'dir: Fr.join(k, eh, "skills"),'),
 "{cwd}/.agent/skills": ("coding-agent/src/discovery/agents.ts", 'x.push(Rs.join(R, _, ...p));'),
 "{cwd}/.agents/skills": ("coding-agent/src/discovery/agents.ts", 'x.push(Rs.join(R, _, ...p));'),
 "{cwd}/.codex/skills": ("coding-agent/src/discovery/codex.ts", 'return Xr.join(u.cwd, ".codex");'),
 "{cwd}/.opencode/skills": ("coding-agent/src/discovery/helpers.ts", 'return d.join(e.cwd, r.projectDir, n);'),
 "{cwd}/.github/skills": ("coding-agent/src/discovery/helpers.ts", 'return d.join(e.cwd, r.projectDir, n);'),
 "~/.omp/agent/skills": ("coding-agent/src/discovery/builtin.ts", 'dir: fr.join(we(), "skills"),'),
 "~/.omp/plugins/node_modules/*/skills": ("coding-agent/src/discovery/omp-plugins.ts", 'dir: Zo.join(R.path, "skills"),'),
 "~/.agent/skills": ("coding-agent/src/discovery/agents.ts", 'return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));'),
 "~/.agents/skills": ("coding-agent/src/discovery/agents.ts", 'return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));'),
 "~/.omp/agent/managed-skills": ("coding-agent/src/autolearn/managed-skills.ts", 'return Zm.join(u, "managed-skills");'),
}

raw = subprocess.run(["git", "-C", LANE, "show", f"{BASE}:verifiers/omp-skill-roots.tsv"],
                     capture_output=True, check=True).stdout
lines = raw.decode("utf-8").split("\n")
if lines and lines[-1] == "": lines.pop()
header, body = lines[0], lines[1:]
out = ["root_pattern\tbinary_quote\tmodule\treader_quote"]
for line in body:
    cells = line.split("\t")
    assert len(cells) == 2, line
    pat, bq = cells
    mod, rq = MAP[pat]
    assert "\t" not in rq and "\n" not in rq and len(rq) >= 12
    out.append("\t".join([pat, bq, mod, rq]))
data = ("\n".join(out) + "\n").encode("utf-8")
open(OUT, "wb").write(data)
print("wrote", OUT, len(out)-1, "data rows", len(data), "bytes")
