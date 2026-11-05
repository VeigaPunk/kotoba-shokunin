import subprocess, sys, os, json, mmap, re, posixpath
from pathlib import Path
S = Path("/fast/scratch/hyaku/kotoba-r87/ScribeIndexR87"); D = S / "repo"
TSV = "verifiers/omp-skill-roots-semantics.tsv"; ELF = "/home/vgpnk/.local/bin/omp"
TIP = "d1c031833c37af99196f72f84a6643f84eec129a"; SEMHDR = "root_pattern\tbinary_quote\tmodule\treader_quote"
def git(*a, inp=None):
    return subprocess.run(["git", "-C", str(D), *a], capture_output=True, text=True, input=inp).stdout
def tsv_at(rev): return git("show", f"{rev}:{TSV}")
base_text = tsv_at(TIP)
rows = [l.split("\t") for l in base_text.splitlines()[1:] if l.strip()]
r86 = [l.split("\t")[0] for l in git("show", f"{TIP}:verifiers/omp-skill-roots.tsv").splitlines()[1:] if l.strip()]
def emit(rs): return SEMHDR + "\n" + "\n".join("\t".join(r) for r in rs) + "\n"
def commit(name, text):
    assert git("rev-parse", "--show-toplevel").strip() == str(D)
    (D / TSV).write_text(text, encoding="utf-8")
    git("add", "--", TSV)
    subprocess.run(["git", "-C", str(D), "-c", "user.name=scribe-scratch", "-c", "user.email=scribe@scratch.invalid",
                    "commit", "-q", "--no-verify", "-m", f"scratch C1 world {name}"], check=True)
    return git("rev-parse", "HEAD").strip()
JOINS = ("join(", ".join(", "resolve(", "path.join")
CODEX = 'return Xr.join(u.cwd, ".codex");'
worlds = {}
worlds["W0_honest_tip"] = TIP
worlds["W1_donothing_binary_as_reader"] = commit("W1", emit([[r[0], r[1], r[2], r[1]] for r in rows]))
worlds["W2_docquote_row1"] = commit("W2", emit([[rows[0][0], rows[0][1], rows[0][2], rows[0][1]]] + rows[1:]))
worlds["W3_nomodule_row1"] = commit("W3", emit([[rows[0][0], rows[0][1], "coding-agent/src/discovery/nonexistent.ts", rows[0][3]]] + rows[1:]))
worlds["W4_shrink_11rows"] = commit("W4", emit(rows[:11]))
worlds["W5_module_collapse_helpers"] = commit("W5", emit([[r[0], r[1], "coding-agent/src/discovery/helpers.ts", r[3]] for r in rows]))
worlds["W6_reader_swap_plugins_to_codex"] = commit("W6", emit(rows[:8] + [[rows[8][0], rows[8][1], "coding-agent/src/discovery/codex.ts", CODEX]] + rows[9:]))
worlds["W7_one_codex_line_for_all_12"] = commit("W7", emit([[r[0], r[1], "coding-agent/src/discovery/codex.ts", CODEX] for r in rows]))
worlds["W8_dotdot_row1"] = commit("W8", emit([["{cwd}/../.omp/skills", rows[0][1], rows[0][2], rows[0][3]]] + rows[1:]))
json.dump(worlds, open(S / "c1-worlds-revs.json", "w"), indent=1)
for name, rev in worlds.items():
    proc = subprocess.run(["python3", "-B", "verifiers/check_omp_root_semantics.py", "--rev", rev],
                          cwd=str(D), capture_output=True, text=True, env=dict(os.environ, TMPDIR=str(S)))
    out = proc.stdout + proc.stderr
    tail = [l for l in out.splitlines() if l.startswith("omp root") or l.startswith("exit=") or l.startswith("S3 detail") or l.startswith("guard S3")]
    print(f"{name:38s} rev={rev[:10]} rc={proc.returncode} | " + " | ".join(tail))
    open(S / f"c1-{name}.txt", "w").write(out)
