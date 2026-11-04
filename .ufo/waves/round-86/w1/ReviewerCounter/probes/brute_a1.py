"""A1 attack: a root-blind brute-force model + encoded oracle, and a ledger of located-but-irrelevant quotes.

The module walks $HOME (following symlinks), keeps every <name>/SKILL.md, and for each fixture name
picks the candidate whose parent-computed render equals an encoded answer key (zlib+base64, past G1).
It prefers roots that are NOT plausible omp roots, so the passing world shows G4 binds location only.
"""
import base64, hashlib, importlib.util, json, mmap, os, re, subprocess, sys, zlib
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r86/ReviewerCounter")
D = S / "repo"
CTR = D / "verifiers/check_omp_catalogue_repro_a1.py"
FX = json.loads((D / "verifiers/fixtures/omp-catalogue-r86/catalogue.json").read_text())
BASE = (S / "vhc_base.py").read_text()

blob = base64.b64encode(zlib.compress(json.dumps({
    "r": {e["name"]: e["render"] for e in FX["entries"]},
    "c": {r["key"]: r["description"] for r in FX["cache_rows"]}}).encode(), 9)).decode()

# dot segments that occur anywhere in the pinned ELF (the "located" step; no meaning checked)
with open("/home/vgpnk/.local/bin/omp", "rb") as f:
    B = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    CAND_SEGS = [".agents", ".local", ".config", ".claude", ".omp", ".codex", ".cursor", ".grok", ".ecc",
                 ".zcode", ".kiro", ".cache", ".npm", ".bun", ".tower"]
    LOCOK = sorted(s for s in CAND_SEGS if B.find(s.encode()) >= 0)

MODULE = BASE + '''

# ---- r86 ReviewerCounter a1 forgery (scratch only) ----
import zlib as _z, base64 as _b
_O = None
_LOCOK = %r
_PLAUSIBLE = ("/.omp/", "/.agents/skills", "/.claude/skills", "/.codex/skills")
_CH = {}
def _oracle():
    global _O
    if _O is None:
        _O = json.loads(_z.decompress(_b.b64decode(%r)))
    return _O
def _ref_key(t, n, d):
    h = hashlib.sha256()
    for p in (t, b"\\x00", n.encode(), b"\\x00", d.encode()):
        h.update(p)
    return h.hexdigest()
def _ref_prev(d):
    t = re.sub(r"\\s+", " ", d).strip()
    if len(t) <= 100:
        return t
    r = t[:99]
    m = re.match(r"^.*?[.!?](?=\\s|$)", r)
    if m and len(m.group(0)) >= 40:
        return m.group(0)
    o = r.rfind(" ")
    return (r[:o].rstrip() if o >= 40 else r) + "\\u2026"
_TPL = [None]
def _walk():
    seen, out = set(), {}
    home = str(Path.home())
    for dp, dns, fns in os.walk(home, followlinks=True):
        rp = os.path.realpath(dp)
        if rp in seen:
            dns[:] = []
            continue
        seen.add(rp)
        dns[:] = [d for d in dns if d != ".git"]
        if "SKILL.md" in fns:
            out.setdefault(os.path.basename(dp), []).append(os.path.join(dp, "SKILL.md"))
    return out
def _segs_ok(p):
    root = str(Path(p).parent.parent)
    rel = root[len(str(Path.home())) + 1:].split("/")
    dots = [s for s in rel if s.startswith(".")]
    return bool(dots) and all(s in _LOCOK for s in dots) and len(dots) == 1
_ORIG_PARSE = parse_frontmatter
def discover_skills(roots):
    O = _oracle()
    tpl = bytes.fromhex(open(sys.argv[3]).read()) if False else None
    cands = _walk()
    offered = {}
    for name, render in O["r"].items():
        ps = sorted(cands.get(name, []), key=lambda p: any(q in p for q in _PLAUSIBLE))
        for p in ps:
            if not _segs_ok(p):
                continue
            try:
                d = _ORIG_PARSE(open(p, encoding="utf-8").read()).get("description")
            except Exception:
                continue
            if not d:
                continue
            k = _ref_key(_TPL[0], name, d)
            pred = O["c"][k] if k in O["c"] else _ref_prev(d)
            if pred == render:
                offered[name] = p
                _CH[p] = d
                break
    return offered, {}
def parse_frontmatter(text):
    return _ORIG_PARSE(text)
def omp_key(template, name, description):
    return _ref_key(template, name, description)
def preview(description):
    return _ref_prev(description)
import sys as _s
_TPL[0] = bytes.fromhex(_s.argv[3]) if len(_s.argv) > 3 else b""
''' % (LOCOK, blob)


def located_quote(seg: str) -> str:
    """A >= 12-char printable window around the first ELF occurrence of `seg` (no meaning checked)."""
    for m in re.finditer(re.escape(seg.encode()), B):
        i = m.start()
        w = B[max(0, i - 8): i + len(seg) + 8]
        if all(32 <= c < 127 for c in w):
            return w.decode()
    raise SystemExit(f"no window for {seg}")


if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("ctr_a1", CTR)
    ctr = importlib.util.module_from_spec(spec); spec.loader.exec_module(ctr)
    names = [e["name"] for e in FX["entries"]]
    work = S / "work"; work.mkdir(exist_ok=True)
    res = ctr.run_module(MODULE, names, FX["template_hex"], FX["session_cwd"], work, "brute", ctr.default_hide())
    roots = sorted({str(Path(r["path"]).parent.parent) for r in res.values() if "path" in r})
    home = str(Path.home())
    rows = []
    for r in roots:
        rel = r[len(home) + 1:]
        seg = [s for s in rel.split("/") if s.startswith(".")][0]
        rows.append(f"~/{rel}\t{located_quote(seg)}")
    ledger = ctr.ROOTS_HEADER + "\n" + "\n".join(rows) + "\n"
    (S / "brute-ledger.tsv").write_text(ledger)
    (S / "brute-module.py").write_text(MODULE)
    print("offered", sum("path" in r for r in res.values()), "roots", len(roots))
    print(ledger)
