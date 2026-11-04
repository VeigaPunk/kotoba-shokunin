#!/usr/bin/env python3
r"""check_omp_catalogue_repro.py -- frozen counter for the round-86 C1 (freshness) claim.

Frozen predicate (the same sentence in plans/round-86.md, here, and in every receipt):

    python3 -B verifiers/check_omp_catalogue_repro.py --rev <rev>
        -> prints "omp catalogue lines reproduced N of 215", exit 0 iff N >= 205
           and guards G1-G4 all PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

Claim C1: the lane's model of the omp skill catalogue -- the discovery roots
(`WALKUP_REL`, `USER_ROOTS`), `discover_skills`, `parse_frontmatter`, `omp_key`
and `preview` in `verifiers/verify_harness_claims.py` -- reproduces the
`<skills>` block omp 18.15.0 actually rendered on this host.  The block was
captured once, at the round-86 freeze, from a real session transcript and is
committed with the cache rows of that moment in
`verifiers/fixtures/omp-catalogue-r86/catalogue.json` (sha256 pinned below).

For `--rev <rev>` the counter writes `git show <rev>:verifiers/verify_harness_claims.py`
into a scratch dir (honours TMPDIR / --work), imports it, and for every fixture
entry (name, render) predicts:

    roots   = [Path(session_cwd)/r for r in mod.WALKUP_REL] + list(mod.USER_ROOTS)
    offered = mod.discover_skills(roots)[0]           # name -> SKILL.md path
    fm      = mod.parse_frontmatter(path.read_text())
    key     = mod.omp_key(template, name, fm["description"])
    predict = cache_rows[key] if key in cache_rows else mod.preview(fm["description"])

A line is reproduced iff predict == render byte for byte.  The template bytes
and cache rows come from the fixture (hermetic); the SKILL.md files are read
live from the roots the model names -- discovery is the claimed surface.

Isolation: the revision's module never runs in this process.  A runner executes
it under bwrap with the omp session transcripts, the description cache and
agent/history databases, the whole fleet tree (/home/vgpnk/Projects/shokunin,
which holds this fixture and every receipt), /fast/scratch, /tmp and /var/tmp
hidden, and returns name -> (path, key, preview) as JSON; the guards run here
on that output, so the module can neither read the catalogue it is scored
against nor patch the guards.  No bwrap -> exit 2.

Guards (evaluated on the revision's bytes and on the model's outputs):
  G1 no-echo    the module's source carries no string constant containing
                "sessions", "<skills>", ".jsonl", "catalogue.json",
                "skill-descriptions.db" inside discover_skills / parse_frontmatter /
                preview / omp_key / USER_ROOTS / WALKUP_REL, and the whole module
                carries no string constant equal to a fixture render of >= 40 chars
                (a hardcoded answer key).
  G2 provenance every offered path of a reproduced name is a regular file named
                SKILL.md that resolves outside the lane repo, the fixture dir and
                every scratch root (/tmp, /var/tmp, /fast/scratch, $TMPDIR), and
                whose mtime and ctime both precede the catalogue's render time
                (fixture `session_timestamp`; a user cannot set ctime back).
  G3 fixture    the fixture's sha256 equals FIXTURE_SHA256 and it holds 215 entries.
  G4 roots      the revision carries `verifiers/omp-skill-roots.tsv` (header
                `root_pattern<TAB>binary_quote`); the root of every reproduced
                name (SKILL.md's grandparent) matches some row's pattern (`~/`
                expanded; `{cwd}/` = the session cwd or any ancestor; fnmatch
                globs), and every row's quote (>= 12 chars) occurs verbatim in
                the installed omp binary OMP_BINARY, whose sha256 must equal
                OMP_SHA256 (else exit 2).  Addendum 1 (plans/round-86-addendum-1.md,
                before any candidate data): each pattern names a literal
                dot-directory segment (`.agents`, `.omp`, ...), carries no
                wildcard in that segment or in its first segment, and its quote
                contains every literal dot segment verbatim -- a bare `*` row or
                a quote that never names the client directory is refused.
                Whether a quote is the code that makes omp read the root is a
                reviewer judgement, not this counter's.

Exit 2 when the revision or the module cannot be loaded, git is missing, the
fixture is unreadable, or the omp binary is absent or not the pinned build.
`--self-test` exercises the guards and the count on synthetic worlds under
TMPDIR and prints `0 failure(s) over N assertions`.
"""
from __future__ import annotations

import argparse
import re
import fnmatch
import ast
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
FIXTURE = HERE / "fixtures" / "omp-catalogue-r86" / "catalogue.json"
FIXTURE_SHA256 = "0b3443e1058fffa75a287faca7d839d4bbfa3b7cd6f672783e1b0e70d714b488"
TOTAL = 215
TARGET = 205
MODULE_PATH = "verifiers/verify_harness_claims.py"
GUARDED_DEFS = ("discover_skills", "parse_frontmatter", "preview", "omp_key")
GUARDED_NAMES = ("USER_ROOTS", "WALKUP_REL")
ECHO_TOKENS = ("sessions", "<skills>", ".jsonl", "catalogue.json", "skill-descriptions.db")
HARDCODE_MIN = 40
ROOTS_LEDGER = "verifiers/omp-skill-roots.tsv"
ROOTS_HEADER = "root_pattern\tbinary_quote"
QUOTE_MIN = 12
OMP_BINARY = Path("/home/vgpnk/.local/bin/omp")
OMP_SHA256 = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"


class Inconclusive(Exception):
    pass


def read_ledger(repo: Path, rev: str) -> str | None:
    out = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{ROOTS_LEDGER}"],
                         capture_output=True, check=False)
    return out.stdout.decode("utf-8") if out.returncode == 0 else None


def read_binary(path: Path, pinned: str) -> bytes:
    try:
        blob = path.read_bytes()
    except OSError as exc:
        raise Inconclusive(f"omp binary unreadable: {exc}")
    digest = hashlib.sha256(blob).hexdigest()
    if digest != pinned:
        raise Inconclusive(f"omp binary sha256 {digest} is not the pinned build {pinned}")
    return blob


def _expand(pattern: str, cwd: Path) -> list[str]:
    if pattern.startswith("{cwd}/"):
        rest = pattern[len("{cwd}/"):]
        return [str(d / rest) for d in [cwd, *cwd.parents]]
    if pattern.startswith("~/"):
        return [str(Path.home() / pattern[2:])]
    return [pattern]

WILD = set("*?[")


def _pattern_problem(pattern: str, quote: str) -> str | None:
    """Addendum-1 (round 86, before any candidate data): a root pattern names the client directory
    it is about.  Its relative part (after `~/`, `{cwd}/` or `/`) must contain at least one literal
    dot-directory segment (`.agents`, `.omp`, ...); no dot segment and no first segment may carry a
    wildcard; and the quote must contain every literal dot segment verbatim.  A bare `*` row, a
    wildcard over the client directory, or a quote that never names the directory is refused."""
    for prefix in ("{cwd}/", "~/"):
        if pattern.startswith(prefix):
            rel = pattern[len(prefix):]
            break
    else:
        rel = pattern.lstrip("/")
    segs = [s for s in rel.split("/") if s]
    if not segs:
        return f"pattern {pattern!r} names no directory"
    if WILD & set(segs[0]):
        return f"pattern {pattern!r} has a wildcard in its first segment"
    dots = [s for s in segs if s.startswith(".") or (WILD & set(s) and s.lstrip("*?[").startswith("."))]
    if any(WILD & set(s) for s in dots):
        return f"pattern {pattern!r} has a wildcard in a dot-directory segment"
    if not dots:
        return f"pattern {pattern!r} names no literal dot-directory"
    missing = [s for s in dots if s not in quote]
    if missing:
        return f"quote does not name {missing[0]!r} of pattern {pattern!r}"
    return None



def guard_g4(ledger: str | None, names: list[str], offered: dict, cwd: Path, binary: bytes) -> list[str]:
    if ledger is None:
        return [f"{ROOTS_LEDGER} absent at the revision"]
    lines = [l for l in ledger.splitlines() if l.strip()]
    if not lines or lines[0] != ROOTS_HEADER:
        return [f"{ROOTS_LEDGER} header is not {ROOTS_HEADER!r}"]
    findings, patterns = [], []
    for i, line in enumerate(lines[1:], 2):
        cells = line.split("\t")
        if len(cells) != 2 or not cells[0].strip():
            findings.append(f"ledger line {i}: want 2 tab-separated cells")
            continue
        pattern, quote = cells[0].strip(), cells[1]
        if len(quote) < QUOTE_MIN or quote.encode("utf-8") not in binary:
            findings.append(f"ledger line {i}: quote not located in the omp binary ({quote[:40]!r})")
            continue
        problem = _pattern_problem(pattern, quote)
        if problem:
            findings.append(f"ledger line {i}: {problem}")
            continue
        patterns.extend(_expand(pattern, cwd))
    for name in names:
        root = str(Path(offered[name]).parent.parent)
        if not any(fnmatch.fnmatchcase(root, p) for p in patterns):
            findings.append(f"{name}: root {root} matches no located ledger pattern")
    return findings


def load_fixture(path: Path, pinned: str | None) -> dict:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise Inconclusive(f"fixture unreadable: {exc}")
    digest = hashlib.sha256(raw).hexdigest()
    data = json.loads(raw.decode("utf-8"))
    data["_sha256"] = digest
    data["_pinned_ok"] = pinned is None or digest == pinned
    return data


def module_source(repo: Path, rev: str) -> str:
    try:
        out = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{MODULE_PATH}"],
                             capture_output=True, check=False)
    except FileNotFoundError:
        raise Inconclusive("git not found")
    if out.returncode != 0:
        raise Inconclusive(f"cannot read {MODULE_PATH} at {rev}: {out.stderr.decode(errors='replace').strip()}")
    return out.stdout.decode("utf-8")


RUNNER = r'''
import importlib.util, json, sys
from pathlib import Path
mod_path, names_path, template_hex, cwd = sys.argv[1:5]
spec = importlib.util.spec_from_file_location("vhc_scored", mod_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
for attr in %r:
    if not hasattr(mod, attr):
        print(json.dumps({"error": "module lacks " + attr})); sys.exit(3)
template = bytes.fromhex(template_hex)
roots = [Path(cwd) / rel for rel in mod.WALKUP_REL] + [Path(r) for r in mod.USER_ROOTS]
offered = mod.discover_skills(roots)[0]
out = {}
for name in json.loads(Path(names_path).read_text()):
    path = offered.get(name)
    if path is None:
        out[name] = {"reason": "not-discovered"}; continue
    try:
        fm = mod.parse_frontmatter(Path(path).read_text(encoding="utf-8"))
    except Exception as exc:
        out[name] = {"reason": "parse-error " + type(exc).__name__, "path": str(path)}; continue
    desc = fm.get("description") if isinstance(fm, dict) else None
    if desc is None or (isinstance(fm, dict) and fm.get("style") == "unmodelled"):
        out[name] = {"reason": "no-description", "path": str(path)}; continue
    out[name] = {"path": str(path), "desc": desc, "key": mod.omp_key(template, name, desc), "preview": mod.preview(desc)}
print(json.dumps(out))
''' % (GUARDED_DEFS + GUARDED_NAMES,)


def default_hide() -> list[Path]:
    """What the scored module must not see: every place a copy of the rendered catalogue lives.
    Addendum 1: all of ~/.omp is hidden (session transcripts, the description cache, agent/history
    DBs and ~/.omp/logs request dumps, which Sentinel-3 found carrying all 215 renders); only the
    skill-bearing subtrees in default_rebind() are bound back."""
    home = Path.home()
    return [home / ".omp", Path("/home/vgpnk/Projects/shokunin"), Path("/fast/scratch"),
            Path("/tmp"), Path("/var/tmp"), Path("/dev/shm"), Path("/run/user")]


def default_rebind() -> list[Path]:
    """Skill-bearing omp subtrees bound back read-only after ~/.omp is hidden (if they exist)."""
    home = Path.home()
    return [home / ".omp/plugins/node_modules", home / ".omp/agent/skills"]


def run_module(src: str, names: list[str], template_hex: str, cwd: str, work: Path, tag: str,
               hide: list[Path], rebind: list[Path] | None = None) -> dict:
    """Run the revision's model in a bwrap sandbox that hides `hide`; the module never shares this
    process, so it cannot patch the guards, and it cannot read the catalogue it is scored against.
    Addendum 1: no network, own pid/ipc namespaces, a new session, and a cleared environment."""
    box = Path(tempfile.mkdtemp(prefix=f"box-{tag}-", dir=str(work)))
    (box / "vhc.py").write_text(src, encoding="utf-8")
    (box / "runner.py").write_text(RUNNER, encoding="utf-8")
    (box / "names.json").write_text(json.dumps(names), encoding="utf-8")
    cmd = [sys.executable, "-B", str(box / "runner.py"), str(box / "vhc.py"), str(box / "names.json"),
           template_hex, cwd]
    if hide:
        if not shutil.which("bwrap"):
            raise Inconclusive("bwrap not found: the scored module cannot be sandboxed")
        wrap = ["bwrap", "--ro-bind", "/", "/", "--dev", "/dev", "--proc", "/proc", "--die-with-parent",
                "--unshare-net", "--unshare-pid", "--unshare-ipc", "--new-session", "--clearenv",
                "--setenv", "HOME", str(Path.home()), "--setenv", "PATH", "/usr/bin:/bin",
                "--setenv", "LANG", "C.UTF-8"]
        for h in hide:
            if h.is_dir():
                wrap += ["--tmpfs", str(h)]
            elif h.exists():
                wrap += ["--ro-bind", "/dev/null", str(h)]
        for r in (default_rebind() if rebind is None else rebind):
            if r.is_dir():
                wrap += ["--ro-bind", str(r), str(r)]
        wrap += ["--ro-bind", str(box), str(box)]
        cmd = wrap + cmd
    out = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=600)
    if out.returncode != 0:
        raise Inconclusive(f"module run failed rc={out.returncode}: {(out.stdout + out.stderr).strip()[-300:]}")
    try:
        return json.loads(out.stdout.strip().splitlines()[-1])
    except (ValueError, IndexError):
        raise Inconclusive("module run printed no JSON")


def _consts(node: ast.AST) -> list[str]:
    return [n.value for n in ast.walk(node) if isinstance(n, ast.Constant) and isinstance(n.value, str)]


def guard_g1(src: str, renders: list[str]) -> list[str]:
    tree = ast.parse(src)
    findings = []
    for node in tree.body:
        name = None
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in GUARDED_DEFS:
            name = node.name
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in targets:
                if isinstance(t, ast.Name) and t.id in GUARDED_NAMES:
                    name = t.id
        if name is None:
            continue
        for s in _consts(node):
            for tok in ECHO_TOKENS:
                if tok in s:
                    findings.append(f"echo token {tok!r} in {name}")
    long_renders = {r for r in renders if len(r) >= HARDCODE_MIN}
    for s in _consts(tree):
        if s in long_renders:
            findings.append(f"hardcoded render literal {s[:40]!r}...")
    return findings


def ref_key(template: bytes, name: str, desc: str) -> str:
    """omp 18.15.0 `A(e)` in skill-descriptions.ts: sha256(prompt ‖ 0x00 ‖ name ‖ 0x00 ‖ description)."""
    h = hashlib.sha256()
    for part in (template, b"\x00", name.encode(), b"\x00", desc.encode()):
        h.update(part)
    return h.hexdigest()


def ref_preview(desc: str) -> str:
    """omp 18.15.0 `dnt` (previewSkillDescription) in skill-descriptions.ts: k = 100, E = 40."""
    t = re.sub(r"\s+", " ", desc).strip()
    if len(t) <= 100:
        return t
    r = t[:99]
    m = re.match(r"^.*?[.!?](?=\s|$)", r)
    if m and len(m.group(0)) >= 40:
        return m.group(0)
    o = r.rfind(" ")
    c = r[:o].rstrip() if o >= 40 else r
    return c + "\u2026"


def _collapse(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def predict(src: str, fixture: dict, work: Path, tag: str, hide: list[Path]) -> tuple[dict, dict, dict]:
    """Addendum 1: the module contributes discovery (path) and parsing (desc) only; the parent
    checks the path's directory is the skill's name, that the description occurs in the file it
    names, that the module's key and preview equal the reference, and computes the render itself.
    An answer key in the module (however encoded) cannot reach a render the file does not yield."""
    rows = {r["key"]: r["description"] for r in fixture["cache_rows"]}
    template = bytes.fromhex(fixture["template_hex"])
    names = [e["name"] for e in fixture["entries"]]
    res = run_module(src, names, fixture["template_hex"], fixture["session_cwd"], work, tag, hide)
    preds, reasons, offered = {}, {}, {}
    for name in names:
        r = res.get(name) or {"reason": "not-discovered"}
        if not isinstance(r, dict):
            reasons[name] = "malformed-output"
            continue
        if "path" in r:
            offered[name] = str(r["path"])
        if "reason" in r:
            reasons[name] = str(r["reason"])
            continue
        path, desc = Path(str(r.get("path"))), r.get("desc")
        if path.parent.name != name:
            reasons[name] = f"dir-name-differs ({path.parent.name})"
            continue
        if not isinstance(desc, str) or not _collapse(desc):
            reasons[name] = "no-description"
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            reasons[name] = "unreadable-path"
            continue
        if _collapse(desc) not in _collapse(text.replace('\\"', '"')):
            reasons[name] = "desc-not-in-file"
            continue
        key = ref_key(template, name, desc)
        if r.get("key") != key:
            reasons[name] = "key-differs-from-reference"
            continue
        if r.get("preview") != ref_preview(desc):
            reasons[name] = "preview-differs-from-reference"
            continue
        preds[name] = rows[key] if key in rows else ref_preview(desc)
    return preds, reasons, offered


def default_scratch() -> list[Path]:
    scratch = [Path(p) for p in ("/tmp", "/var/tmp", "/fast/scratch")]
    if os.environ.get("TMPDIR"):
        scratch.append(Path(os.environ["TMPDIR"]))
    return scratch


def guard_g2(names: list[str], offered: dict, forbidden: list[Path], scratch: list[Path],
             frozen_epoch: float | None) -> list[str]:
    findings = []
    for name in names:
        p = Path(offered[name])
        if p.name != "SKILL.md" or not p.is_file():
            findings.append(f"{name}: {p} is not a SKILL.md file")
            continue
        real = p.resolve()
        for f in list(forbidden) + scratch:
            try:
                real.relative_to(f.resolve())
                findings.append(f"{name}: {real} resolves inside {f}")
            except ValueError:
                pass
        # st_ctime cannot be set back by a user-level writer, so a forged file cannot backdate it
        st = real.stat()
        if frozen_epoch is not None and max(st.st_mtime, st.st_ctime) > frozen_epoch:
            findings.append(f"{name}: {real} modified (mtime/ctime) after the catalogue was rendered")
    return findings


def score(src: str, fixture: dict, work: Path, tag: str, forbidden: list[Path], out=print,
          scratch: list[Path] | None = None, frozen_epoch: float | None = None,
          ledger: str | None = None, binary: bytes = b"", hide: list[Path] | None = None) -> int:
    scratch = default_scratch() if scratch is None else scratch
    hide = default_hide() if hide is None else hide
    entries = fixture["entries"]
    preds, reasons, offered = predict(src, fixture, work, tag, hide)
    reproduced = [e["name"] for e in entries if preds.get(e["name"]) == e["render"]]
    for e in entries:
        n = e["name"]
        if n in reasons:
            out(f"MISS {n} {reasons[n]}")
        elif preds[n] != e["render"]:
            out(f"MISS {n} render-differs predicted={preds[n][:60]!r} observed={e['render'][:60]!r}")
    g1 = guard_g1(src, [e["render"] for e in entries])
    g2 = guard_g2(reproduced, offered, forbidden, scratch, frozen_epoch)
    g3 = [] if fixture["_pinned_ok"] and len(entries) == TOTAL else [
        f"fixture sha256 {fixture['_sha256']} entries {len(entries)}"]
    g4 = guard_g4(ledger, reproduced, offered, Path(fixture["session_cwd"]), binary)
    for label, fnd in (("G1 no-echo", g1), ("G2 provenance", g2), ("G3 fixture", g3), ("G4 roots", g4)):
        out(f"guard {label} {'PASS' if not fnd else 'FAIL'}" + ("" if not fnd else f" ({len(fnd)}): {fnd[0]}"))
    n = len(reproduced)
    out(f"omp catalogue lines reproduced {n} of {len(entries)}")
    ok = n >= TARGET and not (g1 or g2 or g3 or g4)
    return 0 if ok else 1


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------
GOOD_MODULE = '''
import hashlib, re
from pathlib import Path
WALKUP_REL = []
USER_ROOTS = [{roots}]
def discover_skills(roots):
    out = {{}}
    for r in roots:
        r = Path(r)
        if r.is_dir():
            for e in sorted(r.iterdir()):
                if (e / "SKILL.md").is_file():
                    out.setdefault(e.name, e / "SKILL.md")
    return out, {{}}
def parse_frontmatter(text):
    m = re.search(r"^description: (.*)$", text, re.M)
    return {{"description": m.group(1) if m else None, "style": "plain"}}
def omp_key(template, name, description):
    h = hashlib.sha256(); h.update(template); h.update(b"\\x00"); h.update(name.encode()); h.update(b"\\x00"); h.update(description.encode())
    return h.hexdigest()
def preview(description):
    t = re.sub(r"\\s+", " ", description).strip()
    if len(t) <= 100:
        return t
    s = t[:99]
    m = re.match(r"^.*?[.!?](?=\\s|$)", s)
    if m and len(m.group(0)) >= 40:
        return m.group(0)
    o = s.rfind(" ")
    return (s[:o].rstrip() if o >= 40 else s) + "\\u2026"
'''


def self_test() -> int:
    failures = 0
    count = 0

    def check(label, cond):
        nonlocal failures, count
        count += 1
        if not cond:
            failures += 1
            print(f"FAIL {label}")

    base = Path(tempfile.mkdtemp(prefix="ocr-selftest-", dir=os.environ.get("TMPDIR")))
    try:
        root = base / ".fakeclient" / "skills"
        descs = {
            "alpha": "Short alpha description that stays verbatim.",
            "beta": "Beta does one thing well. " + "x" * 120,
            "gamma": "gamma " + "word " * 40,
        }
        for n, d in descs.items():
            (root / n).mkdir(parents=True)
            (root / n / "SKILL.md").write_text(f"---\nname: {n}\ndescription: {d}\n---\nbody\n")
        template = b"T{{name}}{{description}}"
        good = GOOD_MODULE.format(roots=repr(str(root)))
        spec = importlib.util.spec_from_file_location("vhc_selftest", base / "vhc_selftest.py")
        (base / "vhc_selftest.py").write_text(good, encoding="utf-8")
        gmod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gmod)
        renders = {n: gmod.preview(d) for n, d in descs.items()}
        cached = gmod.omp_key(template, "alpha", descs["alpha"])
        renders["alpha"] = "Alpha one-liner from cache."
        fixture = {"template_hex": template.hex(), "session_cwd": str(base),
                   "entries": [{"name": n, "render": renders[n]} for n in descs],
                   "cache_rows": [{"key": cached, "description": renders["alpha"]}],
                   "_pinned_ok": True, "_sha256": "x"}
        global TOTAL, TARGET
        saved = TOTAL, TARGET
        quote = 'loadSkillsFromDir(".fakeclient")-QUOTE'
        blob = b"\x00junk " + quote.encode() + b" more loadSkillsFromDir-QUOTE\x00"
        ledger = f"{ROOTS_HEADER}\n{root}\t{quote}\n"
        S = {"scratch": [], "frozen_epoch": None, "ledger": ledger, "binary": blob, "hide": []}
        TOTAL, TARGET = 3, 3
        lines: list[str] = []
        try:
            rc = score(good, fixture, base, "w_good", [REPO], out=lines.append, **S)
            check("good world exit 0", rc == 0)
            check("good world 3 of 3", "omp catalogue lines reproduced 3 of 3" in lines)
            # do-nothing: a root list that misses the root
            lines.clear()
            rc = score(GOOD_MODULE.format(roots=""), fixture, base, "w_empty", [REPO], out=lines.append, **S)
            check("empty roots exit 1", rc == 1)
            check("empty roots 0 of 3", "omp catalogue lines reproduced 0 of 3" in lines)
            check("empty roots MISS reason", any(l.startswith("MISS alpha not-discovered") for l in lines))
            # echo forgery: discovery names the session transcript
            lines.clear()
            echo = good.replace("def discover_skills(roots):",
                                "def discover_skills(roots):\n    _ = '~/.omp/agent/sessions'")
            rc = score(echo, fixture, base, "w_echo", [REPO], out=lines.append, **S)
            check("echo forgery exit 1", rc == 1)
            check("echo forgery G1 FAIL", any(l.startswith("guard G1 no-echo FAIL") for l in lines))
            # hardcode forgery: an answer key literal anywhere in the module
            lines.clear()
            hard = good + f"\nANSWERS = {{'gamma': {renders['gamma']!r}}}\n"
            rc = score(hard, fixture, base, "w_hard", [REPO], out=lines.append, **S)
            check("hardcode forgery exit 1", rc == 1)
            check("hardcode forgery G1 FAIL", any("hardcoded render literal" in l for l in lines))
            # wrong preview: sentence back-off floor 10 instead of 40
            lines.clear()
            wrong = good.replace("len(m.group(0)) >= 40", "len(m.group(0)) >= 10")
            rc = score(wrong, fixture, base, "w_wrong", [REPO], out=lines.append, **S)
            check("wrong floor exit 1", rc == 1)
            check("wrong floor below 3", "omp catalogue lines reproduced 3 of 3" not in lines)
            # provenance: a root inside the forbidden tree
            lines.clear()
            rc = score(good, fixture, base, "w_prov", [root], out=lines.append, **S)
            check("provenance exit 1", rc == 1)
            check("provenance G2 FAIL", any(l.startswith("guard G2 provenance FAIL") for l in lines))
            # fixture pin
            lines.clear()
            bad = dict(fixture, _pinned_ok=False)
            rc = score(good, bad, base, "w_pin", [REPO], out=lines.append, **S)
            check("fixture pin exit 1", rc == 1)
            check("fixture pin G3 FAIL", any(l.startswith("guard G3 fixture FAIL") for l in lines))
            # cache precedence: dropping the cache row makes alpha a preview, not the one-liner
            lines.clear()
            nocache = dict(fixture, cache_rows=[])
            rc = score(good, nocache, base, "w_nocache", [REPO], out=lines.append, **S)
            check("no-cache exit 1", rc == 1)
            check("no-cache alpha differs", any(l.startswith("MISS alpha render-differs") for l in lines))
            # addendum-1 arms (ReviewerCounter-2): one old SKILL.md offered for every name, and an
            # answer key hidden past G1 (base64, served by call order through preview)
            import base64
            onepath = good.replace("    return out, {}\n", "    first = next(iter(out.values()), None)\n"
                                   "    return {n: first for n in ('alpha', 'beta', 'gamma')}, {}\n", 1)
            lines.clear()
            rc = score(onepath, fixture, base, "w_onepath", [REPO], out=lines.append, **S)
            check("one-path forgery exit 1", rc == 1)
            check("one-path forgery dir-name MISS", any("dir-name-differs" in l for l in lines))
            enc = base64.b64encode(json.dumps([renders[n] for n in ("alpha", "beta", "gamma")]).encode()).decode()
            keyed = good + ("\nimport base64 as _b, json as _j\n_K = _j.loads(_b.b64decode(%r))\n_i = [0]\n"
                            "def preview(description):\n    _i[0] += 1\n    return _K[_i[0] - 1]\n" % enc)
            lines.clear()
            rc = score(keyed, fixture, base, "w_b64key", [REPO], out=lines.append, **S)
            check("encoded answer key exit 1", rc == 1)
            check("encoded answer key preview MISS", any("preview-differs-from-reference" in l for l in lines))
            # scratch provenance: SKILL.md files written under a scratch root are refused
            lines.clear()
            rc = score(good, fixture, base, "w_scratch", [REPO], out=lines.append, scratch=[base],
                       frozen_epoch=None, ledger=ledger, binary=blob, hide=[])
            check("scratch-root forgery exit 1", rc == 1)
            check("scratch-root forgery G2 FAIL", any(l.startswith("guard G2 provenance FAIL") for l in lines))
            # files modified after the catalogue was rendered are refused
            lines.clear()
            rc = score(good, fixture, base, "w_mtime", [REPO], out=lines.append, scratch=[], frozen_epoch=0.0,
                       ledger=ledger, binary=blob, hide=[])
            check("post-render file exit 1", rc == 1)
            check("post-render file G2 FAIL", any("after the catalogue was rendered" in l for l in lines))
            # module that cannot import is could-not-evaluate
            try:
                run_module("raise RuntimeError('x')", ["alpha"], template.hex(), str(base), base, "w_broken", [])
                check("broken module raises", False)
            except Inconclusive:
                check("broken module raises", True)
            # sandbox: a hidden root is invisible to the scored module (bwrap), so nothing is discovered
            if shutil.which("bwrap"):
                lines.clear()
                rc = score(good, fixture, base, "w_hidden", [REPO], out=lines.append, scratch=[],
                           frozen_epoch=None, ledger=ledger, binary=blob, hide=[root])
                check("hidden root exit 1", rc == 1)
                check("hidden root 0 of 3", "omp catalogue lines reproduced 0 of 3" in lines)
            else:
                check("bwrap present for the sandbox arm", False)
            # G4: no ledger, an unlocated quote, and a root no pattern covers are each refused
            for tag, led in (("w_noledger", None),
                             ("w_fakequote", f"{ROOTS_HEADER}\n{root}\tnot-in-the-binary-quote\n"),
                             ("w_otherroot", f"{ROOTS_HEADER}\n{base}/.fakeclient/elsewhere\t{quote}\n"),
                             ("w_header", f"pattern\tquote\n{root}\t{quote}\n"),
                             # addendum-1 arms: the Critic-2 `*` row, a wildcard over the client
                             # directory, a pattern with no dot-directory, a quote that never names it
                             ("w_star", f"{ROOTS_HEADER}\n*\t{quote}\n"),
                             ("w_dotwild", f"{ROOTS_HEADER}\n{base}/.*/skills\t{quote}\n"),
                             ("w_nodot", f"{ROOTS_HEADER}\n{base}/plain/skills\t{quote}\n"),
                             ("w_quotemiss", f"{ROOTS_HEADER}\n{root}\tloadSkillsFromDir-QUOTE\n")):
                lines.clear()
                rc = score(good, fixture, base, tag, [REPO], out=lines.append, scratch=[], frozen_epoch=None,
                           ledger=led, binary=blob, hide=[])
                check(f"{tag} exit 1", rc == 1)
                check(f"{tag} G4 FAIL", any(l.startswith("guard G4 roots FAIL") for l in lines))
            # G4: a glob pattern and a {cwd}/ pattern both cover the root
            for tag, pat in (("w_glob", f"{root.parent}/sk*"), ("w_cwd", "{cwd}/.fakeclient/skills")):
                lines.clear()
                rc = score(good, fixture, base, tag, [REPO], out=lines.append, scratch=[], frozen_epoch=None,
                           ledger=f"{ROOTS_HEADER}\n{pat}\t{quote}\n", binary=blob, hide=[])
                check(f"{tag} exit 0", rc == 0)
        finally:
            TOTAL, TARGET = saved
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print(f"{failures} failure(s) over {count} assertions")
    return 0 if failures == 0 else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rev", help="full commit hash whose verify_harness_claims.py is scored")
    ap.add_argument("--repo", default=str(REPO))
    ap.add_argument("--work", help="scratch dir (default: a temp dir under TMPDIR)")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.rev:
        ap.error("--rev is required")
    work = Path(args.work) if args.work else Path(tempfile.mkdtemp(prefix="ocr-", dir=os.environ.get("TMPDIR")))
    work.mkdir(parents=True, exist_ok=True)
    try:
        fixture = load_fixture(FIXTURE, FIXTURE_SHA256)
        src = module_source(Path(args.repo), args.rev)
        print(f"rev {args.rev} fixture sha256 {fixture['_sha256']} session_cwd {fixture['session_cwd']}")
        epoch = datetime.fromisoformat(fixture["session_timestamp"].replace("Z", "+00:00")).timestamp()
        binary = read_binary(OMP_BINARY, OMP_SHA256)
        return score(src, fixture, work, "rev", [Path(args.repo), FIXTURE.parent], frozen_epoch=epoch,
                     ledger=read_ledger(Path(args.repo), args.rev), binary=binary)
    except Inconclusive as exc:
        print(f"could-not-evaluate: {exc}")
        return 2
    finally:
        if not args.work:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
