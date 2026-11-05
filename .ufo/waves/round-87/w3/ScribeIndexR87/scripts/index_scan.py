import re, subprocess, os, json
from pathlib import Path
S = Path("/fast/scratch/hyaku/kotoba-r87/ScribeIndexR87")
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin"); FLEET = Path("/home/vgpnk/Projects/shokunin")
def git(repo, *a):
    return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True)
def commit_exists(h):
    lane = git(LANE, "cat-file", "-e", h + "^{commit}").returncode == 0
    fleet = git(FLEET, "cat-file", "-e", h + "^{commit}").returncode == 0
    return ("lane" if lane else "") + ("+fleet" if fleet else "") or "absent"
DOCS = ["corpus/lessons/round-87.md", "plans/round-87.md", "plans/round-87-addendum-1.md", "plans/round-87-addendum-2.md"]
LOG_START, SC_START = 3298, 601
def block_range(path, start):
    lines = open(LANE / path, encoding="utf-8").read().splitlines()
    end = len(lines)
    for i in range(start, len(lines)):  # 0-based index i == line i+1
        if lines[i].startswith("## ") and i + 1 > start:
            end = i; break
    return start, end, lines
results = {"docs": {}, "block": {}, "pointers": []}
TOKEN = re.compile(r"`([^`\n]+)`")
HEX = re.compile(r"^[0-9a-f]{7,40}$")
PATHLIKE = ("corpus/", "plans/", "verifiers/", ".ufo/", "LOG.md", "SCORECARD.md", "SKILL.md", "considerthese/", "/home/", "~/", "../", "scripts/", "templates/")
def check_path(tok, origin_file):
    t = re.sub(r":\d+(-\d+)?$", "", tok.strip())
    if t.startswith("~/"):
        p = Path(os.path.expanduser(t)); return ("exists" if p.exists() else "dangling"), str(p)
    if t.startswith("/"):
        p = Path(t); return ("exists" if p.exists() else "dangling"), str(p)
    cands = [LANE / t, (LANE / origin_file).parent / t]
    if t.startswith(".ufo/reports/") or t.startswith("../") :
        cands.append(FLEET / t)
    for c in cands:
        try:
            if c.exists() or c.is_symlink() and not c.exists() and False: return "exists", str(c)
        except OSError: pass
    for c in cands:
        if c.is_symlink() and not c.exists(): return "dangling-symlink", str(c)
    return "dangling", t
def scan(path, lines, lo, hi):
    for idx in range(lo - 1, hi):
        line = lines[idx]
        for m in TOKEN.finditer(line):
            tok = m.group(1).strip()
            if HEX.match(tok):
                results["pointers"].append([path, idx + 1, "commit", tok, commit_exists(tok)])
            elif "/" in tok and " " not in tok and tok.startswith(PATHLIKE) and not any(c in tok for c in "<>*{}") and "…" not in tok and "..." not in tok:
                st, where = check_path(tok, path)
                results["pointers"].append([path, idx + 1, "path", tok, st])
for d in DOCS:
    lines = open(LANE / d, encoding="utf-8").read().splitlines()
    results["docs"][d] = {"lines": len(lines), "headings": [[i + 1, l] for i, l in enumerate(lines) if l.startswith("#")]}
    scan(d, lines, 1, len(lines))
for path, start in [("LOG.md", LOG_START), ("SCORECARD.md", SC_START)]:
    s, e, lines = block_range(path, start)
    results["block"][path] = {"start": s, "end": e, "end_is_next_heading_or_eof": True}
    scan(path, lines, s, e)
json.dump(results, open(S / "index_scan.json", "w"), indent=1, ensure_ascii=False)
res = results["pointers"]
from collections import Counter
print("pointers scanned:", len(res)); print(Counter(r[4].split(":")[0].split("+")[0] if r[2]=="commit" else r[4] for r in res))
for r in res:
    if r[4] not in ("exists",) and not (r[2]=="commit" and r[4] != "absent"):
        print("DANGLING?", r[0], r[1], r[2], r[3], r[4])
