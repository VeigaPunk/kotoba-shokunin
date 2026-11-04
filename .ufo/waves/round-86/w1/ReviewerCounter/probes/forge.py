"""Build forgery/escape probe modules, commit each in the scratch clone, score with the frozen counter."""
import base64, json, os, subprocess, sys, zlib
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r86/ReviewerCounter")
D = S / "repo"
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
COUNTER = LANE / "verifiers/check_omp_catalogue_repro.py"
FX = json.loads((LANE / "verifiers/fixtures/omp-catalogue-r86/catalogue.json").read_text())
ANCHOR = "/home/vgpnk/.agents/skills/ufo/SKILL.md"   # one real, old SKILL.md outside every forbidden root

COMMON = '''
import json, os, re
from pathlib import Path
WALKUP_REL = []
USER_ROOTS = []
_CUR = [None]
_ANCHOR = %r
def discover_skills(roots):
    return {n: _ANCHOR for n in _leak()}, {}
def parse_frontmatter(text):
    return {"description": "x", "style": "plain"}
def omp_key(template, name, description):
    _CUR[0] = name
    return "no-such-key"
def preview(description):
    return _leak()[_CUR[0]]
_MEMO = {}
def _parse_block(text):
    out = {}
    for m in re.finditer(r"^- ([^:\\n]+): (.*)$", text, re.M):
        out.setdefault(m.group(1), m.group(2))
    return out
''' % ANCHOR

LEAKS = {
    # G1 bypass: every render split in two string constants (no constant equals a render)
    "F1-split-literal": lambda: "def _leak():\n    return {\n" + "".join(
        f"        {e['name']!r}: {e['render'][:20]!r} + {e['render'][20:]!r},\n" for e in FX["entries"]) + "    }\n",
    # G1 bypass: compressed answer key
    "F2-zlib-key": lambda: "import base64, zlib\n_K = %r\ndef _leak():\n    return json.loads(zlib.decompress(base64.b64decode(_K)))\n" % (
        base64.b64encode(zlib.compress(json.dumps({e["name"]: e["render"] for e in FX["entries"]}).encode(), 9)).decode()),
    # network: the frozen fixture itself, public on GitHub at the freeze commit
    "E1-network-github": lambda: '''import urllib.request
_U = "https://raw.githubusercontent.com/VeigaPunk/kotoba-shokunin/ecfad51fe3f24540a6d67d2b54920929c7b83041/verifiers/fixtures/omp-catalogue-r86/catalogue.json"
def _leak():
    if "k" not in _MEMO:
        d = json.loads(urllib.request.urlopen(_U, timeout=30).read())
        _MEMO["k"] = {e["name"]: e["render"] for e in d["entries"]}
    return _MEMO["k"]
''',
}


def git(*a):
    return subprocess.run(["git", "-C", str(D), *a], check=True, capture_output=True, text=True).stdout.strip()


def score(tag, module_src, ledger, counter=None):
    counter = counter or COUNTER
    assert git("rev-parse", "--show-toplevel") == str(D)
    (D / "verifiers/verify_harness_claims.py").write_text(module_src)
    (D / "verifiers/omp-skill-roots.tsv").write_text(ledger)
    git("add", "-A")
    git("-c", "user.name=seat", "-c", "user.email=seat@local", "commit", "-qm", tag)
    rev = git("rev-parse", "HEAD")
    env = dict(os.environ, TMPDIR=str(S))
    out = subprocess.run([sys.executable, "-B", str(counter), "--repo", str(D), "--rev", rev],
                         capture_output=True, text=True, env=env)
    body = out.stdout + out.stderr
    import hashlib
    rec = (f"# counter {counter} sha256 {hashlib.sha256(Path(counter).read_bytes()).hexdigest()}\n"
           f"# ledger: {ledger!r}\n"
           f"$ TMPDIR={S} python3 -B {counter} --repo {D} --rev {rev}   # probe {tag}\n{body}exit={out.returncode}\n")
    return rev, out.returncode, rec


if __name__ == "__main__":
    rd = Path(sys.argv[1]); rd.mkdir(parents=True, exist_ok=True)
    mode = sys.argv[2]  # frozen | a1
    counter = {"frozen": D / "verifiers/check_omp_catalogue_repro.py", "a1": D / "verifiers/check_omp_catalogue_repro_a1.py"}[mode]
    ledger = {"frozen": "root_pattern\tbinary_quote\n*\tapplication/json\n",
              "a1": "root_pattern\tbinary_quote\n~/.agents/skills\tapp.agents.hub\n"}[mode]
    wanted = sys.argv[3:] or list(LEAKS)
    for tag in wanted:
        extra = LEAKS[tag]() if tag in LEAKS else Path(tag).read_text()
        name = (tag if tag in LEAKS else Path(tag).stem) + "-" + mode
        src = COMMON + extra
        rev, rc, rec = score(name, src, ledger, counter)
        (rd / f"probe-{name}.txt").write_text(rec + "\n--- module (first 60 lines) ---\n" + "\n".join(src.splitlines()[:60]) + "\n")
        last = [l for l in rec.splitlines() if l.startswith(("guard", "omp catalogue", "exit=", "could-not"))]
        print(name, rev[:12], rc, " | ".join(last))
