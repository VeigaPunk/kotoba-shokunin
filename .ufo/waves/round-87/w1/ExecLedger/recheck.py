import mmap, subprocess, hashlib, sys
LANE="/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE="223ae62424f8ab1eb365d733eb648d6228ddd7e8"
NEW=LANE+"/verifiers/omp-skill-roots-semantics.tsv"
OLD=LANE+"/verifiers/omp-skill-roots.tsv"
ELF="/home/vgpnk/.local/bin/omp"
HEADER="root_pattern\tbinary_quote\tmodule\treader_quote"
JOIN=("join(", ".join(", "resolve(", "path.join")
bad=0
def fail(msg):
    global bad
    bad+=1
    print("FAIL", msg)

raw=open(NEW,"rb").read()
try: txt=raw.decode("utf-8")
except UnicodeDecodeError as e: fail(f"not utf-8: {e}"); sys.exit(2)
lines=txt.split("\n")
if lines[-1]=="": lines.pop()
if lines[0]!=HEADER: fail(f"header mismatch {lines[0]!r}")
print("header exact:", lines[0]==HEADER)
rows=[l.split("\t") for l in lines[1:]]
print("data rows:", len(rows))
for i,r in enumerate(rows,2):
    if len(r)!=4: fail(f"line {i}: {len(r)} cells")
print("sha256 new", hashlib.sha256(raw).hexdigest())

base=subprocess.run(["git","-C",LANE,"show",f"{BASE}:verifiers/omp-skill-roots.tsv"],capture_output=True,check=True).stdout.decode("utf-8").split("\n")
if base and base[-1]=="": base.pop()
base_rows=[l.split("\t") for l in base[1:]]
print("base rows:", len(base_rows))
pats_new=[r[0] for r in rows]; pats_old=[b[0] for b in base_rows]
print("cut -f1 equal:", pats_new==pats_old)
print("cut -f2 equal:", [r[1] for r in rows]==[b[1] for b in base_rows])
print("order same:", pats_new==pats_old)

f=open(ELF,"rb"); m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
def line_at(off):
    a=m.rfind(b"\n",0,off)+1; b=m.find(b"\n",off)
    return m[a:(b if b>=0 else len(m))].decode("utf-8","replace")
for i,(pat,bq,mod,rq) in enumerate(rows,2):
    if rq=="NONE":
        print(f"row {i} {pat}: NONE (no reader)"); continue
    nb=rq.encode()
    off=m.find(nb)
    if off<0:
        fail(f"row {i} {pat}: quote not in ELF"); continue
    if m.find(nb,off+1)>=0:
        print(f"  note row {i}: quote occurs more than once")
    ln=line_at(off)
    hdr=("// packages/"+mod).encode()
    hoffs=[]; s=0
    while True:
        j=m.find(hdr,s)
        if j<0: break
        hoffs.append(j); s=j+1
    okj=any(t in ln for t in JOIN)
    oka=bool(hoffs) and off>hoffs[-1]
    oklen=len(rq)>=12
    print(f"row {i:>2} {pat:<44} off={off:>10} len={len(rq):>2} join={okj} mod_hdrs={len(hoffs)} hdr_last={hoffs[-1] if hoffs else -1:>10} after={oka}")
    print(f"        module={mod}")
    print(f"        line={ln.strip()!r}")
    if not (okj and oka and oklen): fail(f"row {i} conjunct failure")
print("FAILURES", bad)
sys.exit(1 if bad else 0)
