# Independent C1 re-derivation: no import of verifiers/check_omp_root_semantics.py.
import hashlib, mmap, re, subprocess, sys
from pathlib import Path
LANE=Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin"); ELF=Path("/home/vgpnk/.local/bin/omp")
REV=sys.argv[1]; PIN="6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"
J=[b"join(", b".join(", b"resolve(", b"path.join"]
def show(p): 
    r=subprocess.run(["git","-C",str(LANE),"show",f"{REV}:{p}"],capture_output=True,text=True)
    return r.stdout if r.returncode==0 else None
FH=open(ELF,"rb"); data=FH.read(); dig=hashlib.sha256(data).hexdigest()
mm=mmap.mmap(FH.fileno(),0,access=mmap.ACCESS_READ)
sem=show("verifiers/omp-skill-roots-semantics.tsv"); roots=show("verifiers/omp-skill-roots.tsv")
print("elf sha256", dig, "pinned", dig==PIN, "| semantics ledger", "present" if sem else "ABSENT")
P=[l.split("\t")[0] for l in roots.splitlines()[1:] if l.strip()]
R=[l.split("\t") for l in sem.splitlines()[1:] if l.strip()] if sem else []
print("semantics rows", len(R), "round-86 patterns", len(P), "| header ok", (sem or "").splitlines()[0]=="root_pattern\tbinary_quote\tmodule\treader_quote")
def lineof(off):
    s=mm.rfind(b"\n",0,off)+1; e=mm.find(b"\n",off); return s,(mm.size if e<0 else e)
HDR=re.compile(rb"// packages/([A-Za-z0-9_./@-]+)")
def headers_at(before):
    out=[]
    for m in HDR.finditer(mm,0,before):
        out.append((m.start(), m.group(1).decode()))
    return out
ok=0
for i,c in enumerate(R,1):
    pat,doc,mod,q=[x.strip() for x in c]; why=[]
    if i>len(P) or pat!=P[i-1]: why.append("pattern != round-86 row")
    segs=[s for s in pat.split("/") if s]
    if ".." in segs: why.append("dotdot segment")
    rest=pat[len("{cwd}/"):] if pat.startswith("{cwd}/") else pat[2:] if pat.startswith("~/") else pat.lstrip("/")
    first=[s for s in rest.split("/") if s][:1]
    if first and set("*?[")&set(first[0]): why.append("wildcard first segment")
    if len(q)<12: why.append("quote <12 chars")
    offs=[]; at=mm.find(q.encode())
    while at>=0 and len(offs)<8: offs.append(at); at=mm.find(q.encode(),at+1)
    if not offs: why.append("quote absent from ELF")
    hit=None
    for off in offs:
        s,e=lineof(off); L=mm[s:e]
        if any(t in L for t in J): hit=(off,s,e); break
    if offs and not hit: why.append("no join token on the quote's line")
    if hit:
        off,s,e=hit
        # module attribution: nearest preceding package header on the same bundle
        hs=[h for h in headers_at(off) if h[0]>=0]
        nearest=hs[-1][1] if hs else None
        allh=[m.start() for m in re.finditer(re.escape(b"// packages/"+mod.encode())+rb"(?![A-Za-z0-9_.@/-])", mm)]
        if not allh: why.append("module header absent")
        elif off<allh[-1]: why.append("quote before module header's last occurrence")
        attr = "nearest-header==claimed" if nearest==mod else f"nearest-header={nearest!r}"
    else:
        attr="-"
    status="GROUND" if not why else "FAIL("+",".join(why)+")"
    if not why: ok+=1
    print(f"row {i:2d} {status:12s} {pat!r:44s} {attr}")
mm.close()
print(f"INDEPENDENT C1 score at {REV[:12]}: {ok} of 12")
