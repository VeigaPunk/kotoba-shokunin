import json, subprocess, sys
from pathlib import Path
R = Path("/fast/scratch/hyaku/kotoba-r87/MutateR87/repo760")
SEM = "verifiers/omp-skill-roots-semantics.tsv"; ROOTS = "verifiers/omp-skill-roots.tsv"

def git(*a):
    p = subprocess.run(["git", "-C", str(R), *a], capture_output=True, text=True)
    if p.returncode: raise SystemExit("git %s: %s" % (a[0], p.stderr.strip()[-300:]))
    return p.stdout

assert Path(git("rev-parse", "--show-toplevel").strip()) == R
base = git("rev-parse", "master").strip()
sem = git("show", "master:" + SEM); roots = git("show", "master:" + ROOTS)

def world(tag, sem_text, roots_text):
    git("checkout", "-q", "-B", "w_" + tag, base)
    (R / SEM).write_text(sem_text); (R / ROOTS).write_text(roots_text)
    git("add", "-A")
    git("-c", "user.name=probe", "-c", "user.email=probe@example.invalid",
        "commit", "-q", "-m", "forged world " + tag)
    return git("rev-parse", "HEAD").strip()

def rows(text): return text.splitlines()
def set_cell(text, index, column, value):
    """index is 1-based data row (0 = header)."""
    lines = text.splitlines()
    i = index  # header at 0, row n at index n
    cells = lines[i].split("\t"); cells[column] = value
    lines[i] = "\t".join(cells)
    return "\n".join(lines) + "\n"

out = {}
out["f_a_docquote"] = world("f_a", set_cell(sem, 9, 3, "// packages/coding-agent/src/discovery/omp-plugins.ts"), roots)
out["f_b_order"]    = world("f_b", set_cell(sem, 1, 2, "coding-agent/src/discovery/omp-plugins.ts"), roots)
dot = "~/.omp/../.omp/agent/skills"
out["f_c_dotdot"]   = world("f_c", set_cell(sem, 8, 0, dot), set_cell(roots, 8, 0, dot))
star = "*/skills"
out["f_d_star"]     = world("f_d", set_cell(sem, 1, 0, star), set_cell(roots, 1, 0, star))
short_sem = "\n".join(rows(sem)[:12]) + "\n"; short_roots = "\n".join(rows(roots)[:12]) + "\n"
out["f_e_eleven"]   = world("f_e", short_sem, short_roots)
assert Path(git("rev-parse", "--show-toplevel").strip()) == R
json.dump(out, open("/fast/scratch/hyaku/kotoba-r87/MutateR87/base/worlds.json", "w"), indent=1)
print(json.dumps(out, indent=1))
print("rows: sem=%d roots=%d" % (len(rows(sem)) - 1, len(rows(roots)) - 1))
