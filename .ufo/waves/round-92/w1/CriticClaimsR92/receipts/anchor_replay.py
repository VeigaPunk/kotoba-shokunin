import json, re, subprocess, sys
rev = sys.argv[1]
man = subprocess.run(["git","show",f"{rev}:verifiers/fixtures/mutation-battery/manifest.tsv"],capture_output=True,text=True,check=True).stdout
bad = []
n = 0
for ln in man.splitlines()[1:]:
    if not ln.strip(): continue
    rid,target,cls,recipe,disp = ln.split("\t")
    if cls == "equivalent": continue
    r = json.loads(recipe)
    text = subprocess.run(["git","show",f"{rev}:{target}"],capture_output=True,text=True).stdout
    for k,e in enumerate(r.get("edits",[]),1):
        n += 1
        found = len(re.compile(e["anchor"]).findall(text))
        want = int(e.get("count",1))
        if found != want:
            bad.append((rid,k,target,found,want))
print(f"rev {rev[:12]}: anchored edits checked={n} mismatched={len(bad)}")
for b in bad: print("  MISS", b)
