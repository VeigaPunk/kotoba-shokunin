# Independent C2 re-derivation (D1-D4 from committed bytes; D5 from blobs + the measured gate).
import json, re, subprocess, sys
from pathlib import Path
LANE=Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin"); BASE="223ae62424f8ab1eb365d733eb648d6228ddd7e8"
VALIDATOR=Path.home()/"Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs"
REV=sys.argv[1]
def git(*a): return subprocess.run(["git","-C",str(LANE),*a],capture_output=True,text=True)
def show(rev,p):
    r=git("show",f"{rev}:{p}"); return r.stdout if r.returncode==0 else None
def blob(rev,p):
    r=git("rev-parse","--verify","-q",f"{rev}:{p}"); return r.stdout.strip() if r.returncode==0 else None
def anc(a,b):
    return git("merge-base","--is-ancestor",a,b).returncode==0
print("rev", REV)
# D1
ok1=False
cat=show(REV,".ufo/waves/round-86/receipts/tip-catalogue.txt"); reg=show(REV,".ufo/waves/round-86/receipts/tip-registry.txt")
if cat and reg:
    named=set(re.findall(r"\b[0-9a-f]{7,40}\b", cat+reg))
    instr=["verifiers/check_omp_catalogue_repro.py","verifiers/check_gate_registry.py"]
    carry=[]
    for tok in named:
        r=git("rev-parse","--verify","-q",tok+"^{commit}")
        if r.returncode: continue
        sha=r.stdout.strip()
        if not anc(sha,REV): continue
        if all(blob(sha,i)==blob(REV,i) for i in instr): carry.append(sha[:8])
    ok1=(bool(carry) and "exit=0" in cat and "exit=0" in reg
         and "omp catalogue lines reproduced 215 of 215" in cat
         and "gate registry rows conformant 67 of 67" in reg)
    print(f"D1 receipts={'yes' if cat else 'no'}/{ 'yes' if reg else 'no'} named-carrying-rev={sorted(set(carry))} -> {'PASS' if ok1 else 'FAIL'}")
else:
    print("D1 receipts missing at rev -> FAIL")
# D2
sentence="planner/distiller/labrat/Main are frozen-topology seats and can never be swarm lanes."
def norm(t): return " ".join(t.replace("`","").split())
carriers=[show(REV,"plans/round-87.md") or "", show(REV,"corpus/lessons/round-87.md") or ""]
carried=any(norm(sentence) in norm(c) for c in carriers)
vs=VALIDATOR.read_text() if VALIDATOR.exists() else ""
inval=norm(sentence) in norm(vs)
m=re.search(r"SWARM_ROLES\s*=\s*(?:new\s+Set\()?\[(.*?)\]", vs, re.S) or re.search(r"SWARM_ROLES\s*=\s*\[(.*?)\]", vs, re.S)
roles=re.findall(r"['\"]([a-z-]+)['\"]", m.group(1)) if m else []
ok2=carried and inval and roles and "planner" not in roles
print(f"D2 validator={'present' if VALIDATOR.exists() else 'ABSENT'} sentence-in-validator={inval} roles={len(roles)} planner-in-roles={'planner' in roles} carried={carried} -> {'PASS' if ok2 else 'FAIL'}")
# D3
les=show(REV,"corpus/lessons/round-87.md") or ""
sec=re.search(r"^## Gate\s*$(.*?)(?=^## |\Z)", les, re.S|re.M)
rows=[l for l in (sec.group(1).splitlines() if sec else []) if l.strip().startswith("|")]
rej=[]
for l in rows:
    cells=[c.strip() for c in l.strip().strip("|").split("|")]
    bare=[c.replace("*","").replace("_","").strip().lower() for c in cells]
    if "reject" in bare:
        j=bare.index("reject")
        reason=max((cells[k] for k in range(len(cells)) if k!=j and not cells[k].startswith("---")), key=len, default="")
        if len(reason.split())>=8: rej.append(reason[:60])
ok3=bool(rej)
print(f"D3 gate-rows={len(rows)} reject-rows-with->=8-word-reason={len(rej)} -> {'PASS' if ok3 else 'FAIL'} {rej[:1]}")
# D4
p87=show(REV,"plans/round-87.md") or ""
ok4="after the first candidate score" in p87
print(f"D4 kill-rule sentence in plans/round-87.md={ok4} -> {'PASS' if ok4 else 'FAIL'}")
# D5 (i)(ii)
b1=(blob(BASE,"corpus/lessons/round-86-verifier-spotcheck.md"), blob(REV,"corpus/lessons/round-86-verifier-spotcheck.md"))
b2=(blob(BASE,"corpus/lessons/round-81.md"), blob(REV,"corpus/lessons/round-81.md"))
i_ii = b1[0]==b1[1] and b2[0]==b2[1]
lesson=les
iv = ("corpus/lessons/round-86-verifier-spotcheck.md:33" in lesson and "corpus/lessons/round-81.md:8" in lesson and "left red and disclosed" in lesson)
print(f"D5(i)(ii) spotcheck {b1[0][:8]}=={b1[1][:8]} round81 {b2[0][:8]}=={b2[1][:8]} -> {'PASS' if i_ii else 'FAIL'}")
print(f"D5(iv) lesson names both sites + 'left red and disclosed'={iv} -> {'PASS' if iv else 'FAIL'}")
