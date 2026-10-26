#!/usr/bin/env python3
"""Cause probe for M127: what fleet root does the base counter derive from `--repo .`?

Calls the base counter's own build_sandbox() with the argument forms main() derives
for `--repo .` and for an absolute --repo, then reports the sandbox's `../.ufo`
link.  Read-only apart from one tempfile sandbox under /tmp.

usage: python3 -B probe_fleet_root.py <lane-repo> <rev>
       (repo = "." when the cwd is the lane, for form A)
"""
from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
from pathlib import Path

BASE_COUNTER = Path(__file__).with_name("base_counter.py")


def load():
    spec = importlib.util.spec_from_file_location("base_counter", BASE_COUNTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def report(mod, label: str, repo_arg: str, rev: str) -> None:
    repo = Path(repo_arg)
    fleet = repo.parent                       # main(): fleet = ... else repo.parent
    print("== %s: --repo %r" % (label, repo_arg))
    print("   repo=%r fleet=%r  fleet==repo:%s" % (str(repo), str(fleet), fleet == repo))
    with tempfile.TemporaryDirectory(prefix="k73probe-") as tdir:
        parent = Path(tdir)
        try:
            clone = mod.build_sandbox(repo, rev, fleet, parent)
        except Exception as exc:              # EnvError and anything else
            print("   build_sandbox raised %s: %s" % (type(exc).__name__, exc))
            return
        print("   clone=%s" % clone)
        ufo = parent / ".ufo"
        if ufo.is_symlink():
            target = os.readlink(ufo)
            print("   ..%s.ufo is a symlink -> %r (exists=%s)"
                  % (os.sep, target, ufo.exists()))
            print("   ..%s.ufo%sreports%sround-7%skotoba.md exists=%s"
                  % (os.sep, os.sep, os.sep, os.sep,
                     (ufo / "reports/round-7/kotoba.md").exists()))
        else:
            print("   ..%s.ufo is %s" % (os.sep, "absent" if not ufo.exists() else "present"))
        links = sorted(p.name for p in parent.iterdir() if p.is_symlink())
        print("   symlinked entries (%d): %s" % (len(links), " ".join(links[:8])))


def main(argv: list[str]) -> int:
    mod = load()
    rev = argv[1]
    report(mod, "form A (documented r72 invocation)", ".", rev)
    report(mod, "form B (absolute lane path)", str(Path(".").resolve()), rev)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
