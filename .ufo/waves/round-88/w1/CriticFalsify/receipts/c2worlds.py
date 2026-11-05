import json, os, re, shutil, subprocess, sys
T=os.environ["TMPDIR"]; D=f"{T}/repo"; W=f"{T}/worlds"
def run_json(root):
    p=subprocess.run(["python3","-B","verifiers/verify_corpus_integrity.py","--json"],cwd=root,capture_output=True,text=True)
    d=json.loads(p.stdout)
    return {r["check"]:r["verdict"] for r in d["results"]}, p.returncode
def copy(name):
    dst=f"{W}/{name}"; shutil.copytree(D,dst,symlinks=True); return dst
def addfile(root,rel,text):
    os.makedirs(os.path.dirname(f"{root}/{rel}"),exist_ok=True); open(f"{root}/{rel}","w").write(text)
base,brc=run_json(D)
names=sorted(base); red_base={n for n,v in base.items() if v!="PASS"}
print("BASE rc",brc,"names",len(names),"red",sorted(red_base))
worlds={}
# W1: new unresolvable commit citation in a NEW lesson line; name already red at base
r=copy("addred_same")
addfile(r,"corpus/lessons/r88-probe-same.md","probe\n\nSee commit `1234567890abcdef1234567890abcdef12345678` (unresolvable).\n")
worlds["w_added_red_same_name"]=r
# W2: new non-hash commit token; commit_nonhash is green at base
r=copy("addred_new")
addfile(r,"corpus/lessons/r88-probe-new.md","probe\n\nSee commit `zz-not-hex` here.\n")
worlds["w_added_red_new_name"]=r
# W3: silence report_dead IN PLACE (name kept, verdict forced PASS)
r=copy("silenced_inplace")
f=f"{r}/verifiers/verify_corpus_integrity.py"; s=open(f).read()
old='        row["verdict"] = "PASS" if ok else ("OBSERVE" if ok is None else "DRIFT")\n'
assert s.count(old)==1, s.count(old)
s=s.replace(old, old+'        if cid == "corpus.pointers.report_dead": row["verdict"] = "PASS"\n')
open(f,"w").write(s); worlds["w_silenced_inplace"]=r
# W4: remove a check entirely
r=copy("removed_check")
f=f"{r}/verifiers/verify_corpus_integrity.py"; s=open(f).read()
line='    "corpus.pointers.commit_nonhash": ("zero", "commit_nonhash"),\n'
assert s.count(line)==1; s=s.replace(line,""); open(f,"w").write(s); worlds["w_removed_check"]=r
# W5: count-growth inside an already-red name, no name change (second unresolvable)
r=copy("addred_count")
addfile(r,"corpus/lessons/r88-probe-count.md","probe\n\nSee commit `fedcba9876543210fedcba9876543210fedcba98` and commit `0011223344556677889900112233445566778899`.\n")
worlds["w_count_growth_red_name"]=r
for name,root in worlds.items():
    v,rc=run_json(root)
    names_ok = sorted(v)==names
    red={n for n,x in v.items() if x!="PASS"}
    drift={n for n,x in v.items() if x=="DRIFT"}
    mono = red <= red_base
    print(f"\n{name}: rc={rc} names={len(v)} identity={'PASS' if names_ok else 'FAIL'} monotone(red⊆base)={'PASS' if mono else 'FAIL'} -> D5v2 {'PASS' if (names_ok and mono) else 'FAIL'}")
    print("   red now:", sorted(red), "new reds:", sorted(red-red_base), "healed:", sorted(red_base-red))
    print("   verdict of names changed vs base:", {n:(base.get(n),v.get(n)) for n in set(base)|set(v) if base.get(n)!=v.get(n)})
