#!/usr/bin/env python3
"""Fleet-shaped sandbox builder (replica of check_tip_battery.build_sandbox).

Usage: python3 -B make_sandbox.py REPO REV PARENT
Creates PARENT/kotoba-shokunin (clone of REPO at REV) plus the fleet root's
other entries as symlinks beside it. Prints the sandbox path.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

FLEET = Path("/home/vgpnk/Projects/shokunin")


def main() -> int:
    repo, rev, parent = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
    parent.mkdir(parents=True, exist_ok=True)
    clone = parent / "kotoba-shokunin"
    p = subprocess.run(["git", "clone", "--shared", "-q", "--no-checkout", str(repo), str(clone)],
                       capture_output=True, text=True)
    if p.returncode != 0:
        print("clone failed: %s" % p.stderr.strip(), file=sys.stderr)
        return 2
    for entry in FLEET.iterdir():
        if entry.name == "kotoba-shokunin":
            continue
        link = parent / entry.name
        if not link.exists() and not link.is_symlink():
            link.symlink_to(entry)
    p = subprocess.run(["git", "-C", str(clone), "checkout", "-q", rev],
                       capture_output=True, text=True)
    if p.returncode != 0:
        print("checkout failed: %s" % p.stderr.strip(), file=sys.stderr)
        return 2
    print(clone)
    return 0


if __name__ == "__main__":
    sys.exit(main())
