# Independent re-implementation of the C1 frozen predicate (plans/round-87.md C1 + addendum 1 A1.1),
# written from the predicate text, not from the counter's code. Compared row-by-row to the counter.
import subprocess, sys, json, mmap, re
from pathlib import Path
S = Path("/fast/scratch/hyaku/kotoba-r87/ScribeIndexR87"); D = S / "repo"
ELF = "/home/vgpnk/.local/bin/omp"; TSV = "verifiers/omp-skill-roots-semantics.tsv"
JOIN = (b"join(", b".join(", b"resolve(", b"path.join")
def git(rev, path):
    p = subprocess.run(["git", "-C", str(D), "show", f"{rev}:{path}"], capture_output=True)
    return p.stdout.decode("utf-8", "replace") if p.returncode == 0 else None
f = open(ELF, "rb"); blob = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
def exact_line(off):
    s = blob.rfind(b"\n", 0, off); s = 0 if s < 0 else s + 1
    e = blob.find(b"\n", off); e = blob.size() if e < 0 else e
    return blob[s:e]
def all_occ(needle):
    out, at = [], blob.find(needle)
    while at >= 0:
        out.append(at); at = blob.find(needle, at + 1)
    return out
HDR = lambda m: re.compile(rb"// packages/" + re.escape(m.encode()) + rb"(?![A-Za-z0-9_./@-])")
def independent(rev):
    sem = git(rev, TSV); r86 = git(rev, "verifiers/omp-skill-roots.tsv")
    pats86 = [l.split("\t")[0] for l in r86.splitlines()[1:] if l.strip()]
    rows = [l.split("\t") for l in sem.splitlines()[1:] if l.strip()]
    res = {}
    for i in range(1, 13):
        if i > len(rows): res[i] = ("FAIL", "missing"); continue
        cells = rows[i-1]
        if len(cells) != 4: res[i] = ("FAIL", "cells"); continue
        pat, mod, rq = cells[0].strip(), cells[2].strip(), cells[3].strip()
        why = []
        if pat != pats86[i-1]: why.append("pattern!=r86")
        segs = [s for s in pat.split("/") if s]
        if ".." in segs: why.append("dotdot")
        first = next((s for s in (pat.split("/", 1)[1] if pat.startswith("{cwd}/") else pat.lstrip("~/")).split("/") if s), "")
        if any(c in "*?[" for c in first): why.append("wild-first")
        # conjunct 2: quote >=12 chars, occurs, exact line carries a join token
        offs = all_occ(rq.encode()) if len(rq) >= 12 else []
        if not offs: why.append("reader-not-in-elf")
        elif not any(any(j in exact_line(o) for j in JOIN) for o in offs): why.append("reader-line-no-join")
        # conjunct 3: header exists; quote's first occurrence after header's last occurrence
        hs = [m.start() for m in HDR(mod).finditer(blob)] if mod else []
        if not hs: why.append("module-header-absent")
        elif offs and offs[0] < hs[-1]: why.append("quote-before-header")
        # conjunct 4: {cwd}/ expansion on frozen chain stays below $HOME; ~/ stays under $HOME
        if pat.startswith("~/") is False and pat.startswith("{cwd}/") is False and pat.startswith("/"):
            why.append("abs-pattern-unbounded")  # none present; flagged if it ever appears
        res[i] = ("GROUND" if not why else "FAIL", ";".join(why))
    return res
if __name__ == "__main__":
    worlds = json.load(open(S / "c1-worlds-revs.json"))
    worlds["BASE_223ae62"] = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
    summary = {}
    for name, rev in worlds.items():
        ind = independent(rev)
        n = sum(1 for v in ind.values() if v[0] == "GROUND")
        cnt_txt = open(S / f"c1-{name}.txt").read() if name != "BASE_223ae62" else ""
        diffs = []
        for i in range(1, 13):
            want = ind[i][0]
            m = re.search(rf"^row {i:2d} (GROUND|FAIL)", cnt_txt, re.M)
            got = m.group(1) if m else ("n/a" if not cnt_txt else "absent")
            if cnt_txt and got != want: diffs.append((i, got, want))
        summary[name] = (n, diffs)
        print(f"{name:38s} indep_grounded={n:2d}/12 counter_vs_indep_row_diffs={diffs if cnt_txt else 'no-counter-run(base)'}")
