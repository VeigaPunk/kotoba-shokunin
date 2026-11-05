import importlib.util, sys, mmap
from pathlib import Path
spec = importlib.util.spec_from_file_location("ors", "/fast/scratch/hyaku/kotoba-r87/MutateR87/repo760/verifiers/check_omp_root_semantics.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
blob, digest = m.open_elf(m.OMP_BINARY, None)
sem = (Path(m.REPO) / m.SEMANTICS_LEDGER).read_text()
roots = (Path(m.REPO) / m.ROOTS_LEDGER).read_text()
rows = [l.split("\t") for l in sem.splitlines()[1:]]
print("semantics header offsets:")
mods = sorted({r[2] for r in rows})
for mod in mods:
    offs = m.module_offsets(blob, mod)
    print("  %-45s last_header=%s n=%d" % (mod, offs[-1] if offs else None, len(offs)))
print("binary_quote occurrences (needs: found, no join token on its line, offset):")
for i, r in enumerate(rows, 1):
    q = r[1].encode(); offs = m.occurrences(blob, q)
    if not offs:
        print("  row%2d %-40r NOT FOUND" % (i, r[1][:40])); continue
    line = m.elf_line(blob, offs[0])
    join = [t for t in m.JOIN_TOKENS if t.encode() in line]
    print("  row%2d first=%d join=%s len=%d %r" % (i, offs[0], join, len(r[1]), r[1][:38]))
print("reader first offsets:")
for i, r in enumerate(rows, 1):
    offs = m.occurrences(blob, r[3].encode())
    print("  row%2d module=%-45s reader_first=%s" % (i, r[2], offs[0] if offs else None))
blob.close()
