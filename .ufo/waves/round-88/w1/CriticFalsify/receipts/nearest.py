import sys, importlib.util, re, subprocess
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("r87", "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_omp_root_semantics.py")
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
blob, _ = r.open_elf(r.OMP_BINARY, r.OMP_SHA256)
ledger = subprocess.run(["git","-C","/home/vgpnk/Projects/shokunin/kotoba-shokunin","show","4df1e8005016c75390a5e06b209462df58c95918:verifiers/omp-skill-roots-semantics.tsv"],capture_output=True,text=True).stdout
hdrs = [(m.start(), m.group(1)) for m in re.finditer(rb"// packages/([A-Za-z0-9_./@-]+)", blob)]
offs=[h[0] for h in hdrs]
import bisect
agree=0
for i,row in enumerate([l.split("\t") for l in ledger.splitlines()[1:] if l.strip()],1):
    ok, why, first = r.reader_grounded(blob, row[3].strip())
    j = bisect.bisect_left(offs, first) - 1
    near = hdrs[j][1].decode() if j>=0 else None
    mod = row[2].strip()
    same = (near == mod.replace("coding-agent/src/","").replace(".ts","")) or (near and mod.endswith(near.split("/")[-1]) )
    near_full = near
    print(f"row {i:2d} ledger={mod.split('/')[-1]:<22} nearest-preceding-header={near_full!r} at {hdrs[j][0] if j>=0 else None} reader@{first} -> {'AGREE' if mod.endswith(near.split('/')[-1]) else 'DISAGREE'}")
