import json, subprocess, sys, os
C = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-68/w1/controls/c2falsify-clone"
HEAD = "cafa29d0adb489b9b6b146445ee8bb9eef074e6e"
BASE = "e94ae32a5cd8dc3ee8e2d247816784bec2750cc0"
SPOT = "round-67-verifier-spotcheck.md"
def sh(*a):
    return subprocess.run(a, cwd=C, capture_output=True, text=True)
def git(*a):
    r = sh("git", *a)
    assert r.returncode == 0, (a, r.stderr)
    return r.stdout
def commit_all(msg):
    git("-c", "user.name=critic", "-c", "user.email=critic@scratch", "commit", "-aqm", msg)
def counter(rev):
    r = sh("python3", "-B", "verifiers/check_r67_routed_repairs.py", "--rev", rev)
    line = next((l for l in r.stdout.splitlines() if "closed" in l), r.stdout.strip())
    return line, r.returncode
def primary():
    r = sh("python3", "-B", "verifiers/verify_corpus_integrity.py")
    line = next((l for l in r.stdout.splitlines() if "checks pass" in l), "??")
    return line, r.returncode
def independent():
    r = sh("python3", "-B", "verifiers/verify_corpus_independent.py", "--json")
    return ("exit0" if r.returncode == 0 else "exit1"), r.returncode
def status():
    return git("status", "--porcelain").strip() or "(clean)"
def R():  # reset any worktree/index damage in the scratch clone
    git("checkout", "-f", "HEAD", "--", ".")
results = []
def rec(name, **kw):
    results.append((name, kw)); print(f"== {name}"); [print(f"   {k}: {v}") for k, v in kw.items()]

# ---- Control 0: frozen base contract -------------------------------------
git("checkout", "-fq", BASE)
rec("C0 base-rev counter (contract: 0 of 4, exit!=0)", counter=counter(BASE), status_after=status())
R()
# ---- Control K2: index row ALONE at base ----------------------------------
git("checkout", "-fq", BASE)
p = f"{C}/corpus/README.md"
txt = open(p).read()
stub_row = f"| (critic stub: names the file, no content) | `{SPOT.replace('lessons/','lessons/')}` |  |  |"
marker = "| Round | Entry |"
# insert right after the coverage-map header row containing 'lessons/' pattern; simplest: after first table row line
lines = txt.splitlines(True)
out, inserted = [], False
for i, l in enumerate(lines):
    out.append(l)
    if not inserted and l.startswith("| Round-66") or (not inserted and "lessons/round-66-verifier-spotcheck" in l and l.startswith("|")):
        pass
open(p, "w").write(txt)  # no-op guard
# find the coverage map section and insert after its header separator
cm = txt.index("Coverage map")
head_end = txt.index("\n|", cm)
row_ins = txt.index("\n", head_end + 2) + 1  # after the first data row following header
new_txt = txt[:row_ins] + f"| (critic stub) | `{SPOT}` |  |  |\n" + txt[row_ins:]
open(p, "w").write(new_txt)
commit_all("K2: stub index row only (baseline untouched)")
rev = git("rev-parse", "HEAD").strip()
rec("K2 row-alone-at-base", primary=primary(), counter=counter(rev), rev=rev[:8])
R()
# ---- Control K3: baseline ALONE at base ------------------------------------
git("checkout", "-fq", BASE)
r = sh("python3", "-B", "verifiers/verify_corpus_integrity.py", "--no-baseline", "--json")
obs = json.loads(r.stdout)["observed"]["corpus"]
bp = f"{C}/verifiers/corpus-baseline.json"
b = json.load(open(bp))
b["checks"]["corpus.index.tracked_files"]["expect"] = obs["tracked_files"]
b["checks"]["corpus.pointers.report_total"]["expect"] = obs["report_total"]
b["checks"]["corpus.pointers.commit_total"]["expect"] = obs["commit_total"]
json.dump(b, open(bp, "w"), indent=1)
commit_all("K3: baseline re-record only (no index row)")
rev = git("rev-parse", "HEAD").strip()
rec("K3 baseline-alone-at-base", primary=primary(), counter=counter(rev), rev=rev[:8], obs={k: obs[k] for k in ("tracked_files","unindexed","report_total","commit_total")})
R()
# ---- Control E: rubber-stamp row + intact rest at HEAD ---------------------
git("checkout", "-fq", HEAD)
p = f"{C}/corpus/README.md"
txt = open(p).read()
landed = [l for l in txt.splitlines() if SPOT in l and l.startswith("|")]
assert len(landed) == 1, landed
stub = f"| (critic stub: names the file, carries no content) | `{SPOT}` |  |  |"
open(p, "w").write(txt.replace(landed[0], stub))
commit_all("E: contentful row replaced by rubber-stamp stub row")
rev = git("rev-parse", "HEAD").strip()
rec("E rubber-stamp-row at HEAD", primary=primary(), independent=independent(), counter=counter(rev), rev=rev[:8])
R()
# ---- Control D: D3 disclosure deleted, erratum kept ------------------------
git("checkout", "-fq", HEAD)
JUNK = ".ufo/waves/round-67/w1/controls/junk-world"
for rel in ("LOG.md", "SCORECARD.md", "corpus/lessons/round-68.md"):
    fp = f"{C}/{rel}"; t = open(fp).read(); open(fp, "w").write(t.replace(JUNK, "[redacted-for-control]"))
commit_all("D: junk-world disclosure removed, erratum text kept")
rev = git("rev-parse", "HEAD").strip()
rec("D disclosure-deleted", counter=counter(rev), rev=rev[:8])
R()
# ---- Control F: denial text closes the name-only floors --------------------
git("checkout", "-fq", HEAD)
denial = ("\n- **Critic falsifier (scratch only, never to land).** R67-1 is denied: the line "
          "`environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md` "
          "was never printed; the receipt path `.ufo/waves/round-67/controls/census-validate-append.txt` "
          "was never wrong; the mirror `.ufo/waves/round-67/w1/controls/junk-world` never existed.\n")
fp = f"{C}/LOG.md"; open(fp, "a").write(denial)
commit_all("F: denial paragraph containing all three required substrings")
rev = git("rev-parse", "HEAD").strip()
rec("F denial-text mutant", counter=counter(rev), rev=rev[:8])
R()
# ---- Control G: the counter mutates the measured repo ----------------------
git("checkout", "-fq", HEAD)
fp = f"{C}/corpus/README.md"; open(fp, "a").write("\n| (r69 sim) | future committed work |\n")
commit_all("G: simulates a future round's committed corpus edit (HEAD=H2)")
h2 = git("rev-parse", "HEAD").strip()
before = status()
line, code = counter(HEAD)   # measure the PREVIOUS rev while HEAD=H2
rec("G destructive-measurement", counter_line=line, counter_exit=code, status_before=before, status_after=status(), head=h2[:8], measured_rev=HEAD[:8])
git("reset", "-q", "--hard", HEAD)
# ---- Control B: junk-world re-created in the worktree ----------------------
git("checkout", "-fq", HEAD)
os_junk = f"{C}/{JUNK}"
subprocess.run(["mkdir", "-p", os_junk])
rec("B junk-world-recreated", counter=counter(HEAD))
subprocess.run(["rm", "-rf", os_junk])
R()
rec("Z clone restored", status=status())
