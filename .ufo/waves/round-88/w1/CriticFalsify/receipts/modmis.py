import sys, importlib.util, os
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("r87", "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_omp_root_semantics.py")
r87 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r87)
blob, digest = r87.open_elf(r87.OMP_BINARY, r87.OMP_SHA256)
ledger = open(os.environ["TMPDIR"]+"/sem.tsv").read() if os.path.exists(os.environ["TMPDIR"]+"/sem.tsv") else None
import subprocess
ledger = subprocess.run(["git","-C","/fast/scratch/hyaku/kotoba-r88/CriticFalsify/repo","show","223ae62:verifiers/omp-skill-roots-semantics.tsv"],capture_output=True,text=True).stdout
ledger = subprocess.run(["git","-C","/home/vgpnk/Projects/shokunin/kotoba-shokunin","show","4df1e8005016c75390a5e06b209462df58c95918:verifiers/omp-skill-roots-semantics.tsv"],capture_output=True,text=True).stdout
rows = [l.split("\t") for l in ledger.splitlines()[1:] if l.strip()]
mods = sorted({r[2].strip() for r in rows})
print("rows", len(rows), "distinct modules in ledger", len(mods))
total_pass=0; total=0
for i,r in enumerate(rows,1):
    reader=r[3].strip()
    ok, why, first = r87.reader_grounded(blob, reader)
    passing=[]
    for m in mods:
        total+=1
        mok, mwhy = r87.module_grounded(blob, m, first if ok else None)
        if mok: passing.append(m.split("/")[-1]); total_pass+=1
    honest = r[2].strip()
    print(f"row {i:2d} {r[0]:<36} reader_ok={ok} honest={honest.split('/')[-1]!r:<28} modules_that_pass_conjunct3={len(passing)} {passing}")
print(f"\nconjunct-3 accepts {total_pass} of {total} (row,module) pairs; module conjunct sees only header ORDER")
