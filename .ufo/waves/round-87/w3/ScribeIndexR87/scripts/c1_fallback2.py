import sys, subprocess, importlib.util, mmap
sys.dont_write_bytecode = True
from pathlib import Path
S = Path("/fast/scratch/hyaku/kotoba-r87/ScribeIndexR87"); D = S / "repo"
spec = importlib.util.spec_from_file_location("c1", str(D / "verifiers" / "check_omp_root_semantics.py"))
c1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c1)
TIP = "d1c031833c37af99196f72f84a6643f84eec129a"
sem = subprocess.run(["git","-C",str(D),"show",f"{TIP}:verifiers/omp-skill-roots-semantics.tsv"],capture_output=True,text=True).stdout
roots = subprocess.run(["git","-C",str(D),"show",f"{TIP}:verifiers/omp-skill-roots.tsv"],capture_output=True,text=True).stdout
def with_row1_reader(q):
    lines = sem.splitlines()
    cells = lines[1].split("\t"); cells[3] = q; lines[1] = "\t".join(cells)
    return "\n".join(lines) + "\n"
def run_case(label, quote, body_extra=b""):
    Z = b"Z" * 20000
    raw = b"// packages/coding-agent/src/discovery/builtin.ts\nconst a = other.join(x, y);\n" + Z + quote + Z + b"\n" + body_extra
    p = str(S / ("fixture-" + label + ".elf")); open(p, "wb").write(raw)
    fh = open(p, "rb"); blob = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
    lines = []
    grounded, _ = c1.score(with_row1_reader(quote.decode()), roots, blob, c1.FROZEN_CHAIN, lines.append)
    row1 = [l for l in lines if l.startswith("row  1")][0]
    off = blob.find(quote); s = blob.rfind(b"\n", 0, off) + 1; e = blob.find(b"\n", off); line = blob[s:e]
    print(f"{label}\n  counter: {row1[:150]}\n  exact-line length={len(line)} join-in-exact-line={any(j in line for j in (b'join(', b'.join(', b'resolve(', b'path.join'))} | newline within 8KiB before/after quote: {blob.rfind(b'\n', max(0, off-8192), off) >= 0}/{blob.find(b'\n', off, off+8192) >= 0}")
run_case("A_neutral_code_quote_join_only_on_earlier_line", b'const root = "skills";')
run_case("B_doc_string_quote_no_join", b"Native OMP configuration from ~/.omp and .omp/")
