"""Held-out class probe for the E04 `<rev>:<path>` report-pointer fix.

Usage: probe_rev_pointer.py <instrument.py> <label>
Prints one line per class:  <label> <case> <token> <verdict>

The lane-hop case cites from a directory INSIDE the lane repo (that is how the
corpus cites: corpus/lessons/*.md); the fleet-hop case cites from a directory
outside both repos (a non-repo citing directory).
"""
import importlib.util, subprocess, sys, tempfile
from pathlib import Path

INSTR = Path(sys.argv[1])
LABEL = sys.argv[2]
spec = importlib.util.spec_from_file_location("vci", INSTR)
vci = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vci)


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True, check=True)


def make_repo(root: Path, files: dict) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    for rel, body in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
    git(root, "add", "-A")
    git(root, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "seed")
    return root


with tempfile.TemporaryDirectory() as td:
    tmp = Path(td)
    lane = make_repo(tmp / "lane", {".ufo/reports/round-60/kotoba.md": "lane report\n"})
    fleet = make_repo(tmp / "fleet", {".ufo/reports/round-61/kotoba.md": "fleet report\n"})
    cite_outside = tmp / "cite"                     # not a repo
    cite_outside.mkdir()
    cite_inside = lane / "corpus" / "lessons"       # inside the lane repo
    cite_inside.mkdir(parents=True)
    # an uncommitted file in the lane working tree, absent from lane HEAD
    (lane / ".ufo/reports/round-62").mkdir(parents=True, exist_ok=True)
    (lane / ".ufo/reports/round-62/kotoba.md").write_text("uncommitted\n", encoding="utf-8")

    cases = [
        ("A rev-in-lane",       cite_inside,  "HEAD:.ufo/reports/round-60/kotoba.md"),
        ("B rev-in-fleet",      cite_outside, "HEAD:.ufo/reports/round-61/kotoba.md"),
        ("C rev-in-lane-uncommitted-file", cite_inside, "HEAD:.ufo/reports/round-62/kotoba.md"),
        ("D rev-absent-both",   cite_outside, "HEAD:.ufo/reports/round-99/kotoba.md"),
        ("E rev-unresolvable",  cite_outside, "nosuchrev:.ufo/reports/round-60/kotoba.md"),
        ("F bare-in-lane",      cite_inside,  ".ufo/reports/round-60/kotoba.md"),
        ("G bare-absent",       cite_outside, ".ufo/reports/round-98/kotoba.md"),
        ("H absolute-nonexistent", cite_outside, "/nonexistent/abs/report.md"),
        ("I relative-two-up",   cite_inside,  "../../.ufo/reports/round-60/kotoba.md"),
    ]
    for name, base, token in cases:
        try:
            verdict = vci.report_pointer_exists(base, token, fleet)
        except Exception as exc:                      # never raises in either arm
            verdict = "RAISED:%s" % type(exc).__name__
        print(f"{LABEL} {name} token={token!r} verdict={verdict}")
