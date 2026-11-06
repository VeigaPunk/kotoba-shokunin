#!/usr/bin/env python3
"""MutTesterAnchorR100 cheap pre-check: predict the counter's truth table, the
self-test count and the revert-mutant verdict for each forgery world, without
the ~4 min battery conjunct.

Usage: python3 -B probe_worlds.py REPO WORLDS_FILE
Exact reuse of the counter's ROWS/world() so the prediction is not a re-write.
"""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

COUNTER = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/"
               "round-100/anchor-lists.py")
CK = "verifiers/verify_skill_checklist.py"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(cmd, cwd, timeout=600):
    p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True,
                       timeout=timeout)
    return p.returncode, p.stdout + p.stderr


def main(argv: list[str]) -> int:
    repo = Path(argv[0]).resolve()
    worlds = [tuple(ln.split()[1:3]) for ln in Path(argv[1]).read_text().splitlines()
              if ln.strip()]
    al = load(COUNTER, "anchor_lists_counter")
    root = Path(tempfile.mkdtemp(prefix="probe-", dir=str(Path(__import__("os").environ["TMPDIR"]))))
    try:
        for name, rev in worlds:
            subprocess.run(["git", "-C", str(repo), "checkout", "-q", rev], check=True)
            ck_path = repo / CK
            text = ck_path.read_text(encoding="utf-8")
            # truth table, both public paths, exact counter semantics
            work = root / name
            work.mkdir()
            rev_ck = work / "rev_checklist.py"
            rev_ck.write_text(text, encoding="utf-8")
            mod = load(rev_ck, "ck_" + name.replace("-", "_"))
            wdir = work / "worlds"
            wdir.mkdir()
            mism = 0
            for rid, tok, truth in al.ROWS:
                for path in ("governance", "trigger"):
                    w = al.world(wdir, rid + "-" + path)
                    try:
                        if path == "governance":
                            (w / "LOG.md").write_text("- row: `%s`\n" % tok, encoding="utf-8")
                            (w / "SCORECARD.md").write_text("- anchor: `%s`\n" % al.X,
                                                            encoding="utf-8")
                            st = mod.check_governance_citations(w, errata=(), corrections=())[0]
                        else:
                            st = mod.check_citation_resolves(["- `%s`" % tok], w)[0]
                    except Exception as exc:
                        st = "EXC %s" % type(exc).__name__
                    got = {"PASS": "resolves", "FAIL": "red"}.get(st, "other:%s" % st)
                    if got != truth:
                        mism += 1
                        print("  %s %s %s got %s" % (name, rid, path, got))
                    shutil.rmtree(w, ignore_errors=True)
            rc, out = run([sys.executable, "-B", CK, "--self-test"], repo)
            lastl = [ln for ln in out.strip().splitlines() if ln.strip()][-1]
            # revert mutant, on disk, same shape as the counter
            kill = "ABSENT"
            if text.count(al.FIX_LINE) == 1:
                ck_path.write_text(text.replace(al.FIX_LINE, al.BASE_LINE), encoding="utf-8")
                try:
                    rc2, out2 = run([sys.executable, "-B", CK, "--self-test"], repo)
                finally:
                    ck_path.write_text(text, encoding="utf-8")
                last2 = [ln for ln in out2.strip().splitlines() if ln.strip()][-1]
                reported = (rc2 == 1 and any(ln.startswith("self-test FAIL: ")
                                             for ln in out2.splitlines()))
                kill = "KILLED" if reported else "SURVIVED"
                kill += " (exit %s last %r)" % (rc2, last2[:90])
            print("world %s rev %s mismatches %d of %d; selftest exit %s last %r; kill %s"
                  % (name, rev, mism, 2 * len(al.ROWS), rc, lastl[:90], kill))
            subprocess.run(["git", "-C", str(repo), "checkout", "-q", "--", CK], check=True)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
