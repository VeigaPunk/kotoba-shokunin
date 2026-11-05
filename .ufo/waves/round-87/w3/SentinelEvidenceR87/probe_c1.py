import hashlib, mmap, re, subprocess, sys
from pathlib import Path
sys.path.insert(0, "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers")
import check_omp_root_semantics as C

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
ELF  = Path("/home/vgpnk/.local/bin/omp")
REV  = sys.argv[1]

blob = open(ELF, "rb")
mm = mmap.mmap(blob.fileno(), 0, access=mmap.ACCESS_READ)
digest = hashlib.sha256(open(ELF,"rb").read()).hexdigest()
print("elf sha256", digest, "pinned", digest == C.OMP_SHA256)

sem = subprocess.run(["git","-C",str(LANE),"show",f"{REV}:verifiers/omp-skill-roots-semantics.tsv"],capture_output=True,text=True).stdout
roots = subprocess.run(["git","-C",str(LANE),"show",f"{REV}:verifiers/omp-skill-roots.tsv"],capture_output=True,text=True).stdout
rpat = [l.split("\t")[0] for l in roots.splitlines()[1:] if l.strip()]
rows = [l.split("\t") for l in sem.splitlines()[1:] if l.strip()]
print("rows", len(rows), "round86 patterns", len(rpat))

J = C.JOIN_TOKENS
def strict_line(off):
    start = mm.rfind(b"\n", 0, off) + 1
    end = mm.find(b"\n", off)
    return (start, mm.size if end < 0 else end)

print("\n%-3s %-42s %-6s %-9s %s" % ("#", "pattern", "quote", "line_len", "nearest_join_token:dist"))
for i,(cells) in enumerate(rows,1):
    pat, bq, module, quote = [c.strip() for c in cells]
    raw = quote.encode()
    offs = C.occurrences(mm, raw, 8) or [None]
    best = None
    for off in offs:
        if off is None: continue
        s,e = strict_line(off)
        line = mm[s:e]
        pos = [line.find(t.encode()) for t in J]
        pos = [p for p in pos if p >= 0]
        if pos:
            d = min(abs(s+p-off) for p in pos)
            if best is None or d < best[0]:
                best = (d, e-s, off, s+e)
    print("%-3d %-42s %-6s %-9s %s" % (i, pat, quote[:22]+"…" if len(quote)>23 else quote,
          best[1] if best else "-", ("%s %d bytes from quote start" % (best[3], best[0])) if best else "NO JOINT TOKEN ON TRUE LINE"))
mm.close()

print("\n--- bound conjunct under the two chains the module defines")
sem_txt = sem
for chain_name, chain in (("FROZEN_CHAIN", C.FROZEN_CHAIN), ("FULL_CHAIN", C.FULL_CHAIN)):
    bad = 0
    for i,cells in enumerate(rows,1):
        ok, why = C.bound_grounded(cells[0].strip(), chain)
        if not ok:
            bad += 1
            print(f"{chain_name} row {i:2d} FAIL {cells[0].strip()!r}: {why}")
    print(f"{chain_name}: bound fails on {bad} of {len(rows)} rows")

print("\n--- score() with each chain, same committed bytes")
for chain_name, chain in (("FROZEN_CHAIN", C.FROZEN_CHAIN), ("FULL_CHAIN", C.FULL_CHAIN)):
    blob2 = open(ELF,"rb"); mm2 = mmap.mmap(blob2.fileno(),0,access=mmap.ACCESS_READ)
    lines=[]
    g,guards = C.score(sem_txt, roots, mm2, chain, lines.append)
    fails=[l for l in lines if "FAIL" in l]
    print(f"{chain_name}: grounded {g} of {C.TOTAL}; guards S3={'PASS' if guards['S3'] else 'FAIL'}; first fail: {fails[0][:120] if fails else 'none'}")
    mm2.close(); blob2.close()
