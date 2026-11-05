import sys, subprocess, importlib.util
sys.dont_write_bytecode = True
from pathlib import Path
S = Path("/fast/scratch/hyaku/kotoba-r87/ScribeIndexR87"); D = S / "repo"
spec = importlib.util.spec_from_file_location("c1", str(D / "verifiers" / "check_omp_root_semantics.py"))
c1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c1)
TIP = "d1c031833c37af99196f72f84a6643f84eec129a"
sem = subprocess.run(["git","-C",str(D),"show",f"{TIP}:verifiers/omp-skill-roots-semantics.tsv"],capture_output=True,text=True).stdout
roots = subprocess.run(["git","-C",str(D),"show",f"{TIP}:verifiers/omp-skill-roots.tsv"],capture_output=True,text=True).stdout
Z = b"Z" * 20000
HDR = b"// packages/coding-agent/src/discovery/builtin.ts\n"
JOINLINE = b"const q = other.join(a, b);\n"          # a join token on an EARLIER newline-delimited line
def world(quote: bytes):
    # quote sits in a newline-free run of >8 KiB on both sides: no join on its own line
    return HDR + JOINLINE + Z + quote + Z + b"\n"
cases = {
  "A_join_quote_no_join_on_own_line": world(b'dir: fr.join(k, Ou.projectDir, "skills"),'),
  "B_doc_string_quote": world(b"Native OMP configuration from ~/.omp and .omp/"),
}
import mmap
for label, raw in cases.items():
    p = str(S / ('fixture-' + label + '.elf'))
    open(p,'wb').write(raw)
    fh = open(p,'rb'); blob = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
    lines = []
    grounded, guards = c1.score(sem, roots, blob, c1.FROZEN_CHAIN, lines.append)
    row1 = [l for l in lines if l.startswith("row  1")]
    print(f"{label}: counter row1 -> {row1[0][:160] if row1 else 'no row1 line'}")
    print(f"   counter grounded over full 12-row ledger (only row 1 can ground here): {grounded}")
    # exact-line reading of the same bytes (my independent rule)
    q = {"A_join_quote_no_join_on_own_line": b'dir: fr.join(k, Ou.projectDir, "skills"),', "B_doc_string_quote": b"Native OMP configuration from ~/.omp and .omp/"}[label]
    off = blob.find(q); s = blob.rfind(b"\n", 0, off) + 1; e = blob.find(b"\n", off)
    line = blob[s:e]
    print(f"   exact newline-delimited line length={len(line)} join-on-that-line={any(j in line for j in (b'join(', b'.join(', b'resolve(', b'path.join'))}")
    print(f'   8KiB newline window before quote present: {blob.rfind(bytes([10]), max(0, off-8192), off) >= 0}; after: {blob.find(bytes([10]), off, off+8192) >= 0}')
