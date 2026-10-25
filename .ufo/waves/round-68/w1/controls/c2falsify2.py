import json, subprocess, os
C = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-68/w1/controls/c2falsify-clone"
HEAD = "cafa29d0adb489b9b6b146445ee8bb9eef074e6e"
BASE = "e94ae32a5cd8dc3ee8e2d247816784bec2750cc0"
TOKEN = "lessons/round-67-verifier-spotcheck.md"
def sh(*a): return subprocess.run(a, cwd=C, capture_output=True, text=True)
def git(*a):
    r = sh("git", *a); assert r.returncode == 0, (a, r.stderr); return r.stdout
def commit_all(m): git("-c","user.name=critic","-c","user.email=critic@scratch","commit","-aqm",m)
def counter(rev):
    r = sh("python3","-B","verifiers/check_r67_routed_repairs.py","--rev",rev)
    return r.stdout.strip(), r.stderr.strip(), r.returncode
def primary():
    r = sh("python3","-B","verifiers/verify_corpus_integrity.py")
    return next((l for l in r.stdout.splitlines() if "checks pass" in l), "??"), r.returncode
def independent(): return sh("python3","-B","verifiers/verify_corpus_independent.py","--json").returncode
def R(): git("checkout","-fq",HEAD,"--","."); git("reset","-q","--hard",HEAD)
out = []
def P(*a): print(*a); out.append(" ".join(str(x) for x in a))

# C0v2: base contract, full stderr
git("checkout","-fq",BASE)
o,e,c = counter(BASE)
P("C0v2 counter-at-BASE: stdout=%r stderr=%r exit=%d" % (o,e,c))
R()
# K2b: honest row-alone-at-base (correct token), primary gate only
git("checkout","-fq",BASE)
p=f"{C}/corpus/README.md"; t=open(p).read()
i=t.index("Coverage map"); j=t.index("\n|",i); k=t.index("\n",j+2)+1
open(p,"w").write(t[:k]+f"| (critic stub) | `{TOKEN}` |  |  |\n"+t[k:])
commit_all("K2b: correct-token stub row only at base")
r=git("rev-parse","HEAD").strip()[:8]
P("K2b row-alone-at-base (correct token):", primary(), "rev", r)
R()
# E2: rubber-stamp row with CORRECT token at HEAD
p=f"{C}/corpus/README.md"; t=open(p).read()
landed=[l for l in t.splitlines() if TOKEN in l and l.startswith("|")]
assert len(landed)==1, landed
open(p,"w").write(t.replace(landed[0], f"| (critic stub: names the file, carries no content) | `{TOKEN}` |  |  |"))
commit_all("E2: contentless but well-formed coverage row")
r=git("rev-parse","HEAD").strip()
o,e,c=counter(r)
P("E2 rubber-stamp-row rev", r[:8])
P("E2 primary:", primary())
P("E2 independent exit:", independent())
P("E2 counter stdout=%r stderr=%r exit=%d" % (o,e,c))
R()
# D2: disclosure deleted, full findings
for rel in ("LOG.md","SCORECARD.md","corpus/lessons/round-68.md"):
    fp=f"{C}/{rel}"; t=open(fp).read()
    open(fp,"w").write(t.replace(".ufo/waves/round-67/w1/controls/junk-world","[redacted-for-control]"))
commit_all("D2: junk-world disclosure removed")
r=git("rev-parse","HEAD").strip()
o,e,c=counter(r)
P("D2 disclosure-deleted rev", r[:8], "counter stdout=%r exit=%d" % (o,c))
R()
# F2: denial text, full output
denial=("\n- **Critic falsifier (scratch only).** R67-1 is denied: the line "
        "`environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md` "
        "was never printed; the receipt path `.ufo/waves/round-67/controls/census-validate-append.txt` "
        "was never wrong; the mirror `.ufo/waves/round-67/w1/controls/junk-world` never existed.\n")
open(f"{C}/LOG.md","a").write(denial)
commit_all("F2: denial paragraph with all three substrings")
r=git("rev-parse","HEAD").strip()
o,e,c=counter(r)
P("F2 denial-text rev", r[:8], "counter stdout=%r exit=%d" % (o,c))
R()
P("Z final clone status:", git("status","--porcelain").strip() or "(clean)")
