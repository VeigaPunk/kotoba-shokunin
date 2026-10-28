"""Which hop resolves the live dead pointer? (lane-first, then fleet)"""
import subprocess, sys
from pathlib import Path
LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
FLEET = Path("/home/vgpnk/Projects/shokunin")
TOKEN = "HEAD:.ufo/reports/round-77/kotoba.md"
def git(repo, *a):
    return subprocess.run(["git","-C",str(repo),*a],capture_output=True,text=True)
# lane hop: nearest ancestor of the citing dir carrying .git
at = (LANE/"corpus/lessons").resolve()
lane = next((p for p in (at,*at.parents) if (p/".git").exists()), None)
print("citing dir        :", at)
print("lane repo (hop 1) :", lane)
print("  git cat-file -e %r -> rc=%d" % (TOKEN, git(lane,"cat-file","-e",TOKEN).returncode))
print("fleet repo (hop 2):", FLEET)
print("  git cat-file -e %r -> rc=%d" % (TOKEN, git(FLEET,"cat-file","-e",TOKEN).returncode))
print("lane working tree has the path:", (LANE/".ufo/reports/round-77/kotoba.md").is_file())
print("fleet working tree has the path:", (FLEET/".ufo/reports/round-77/kotoba.md").is_file())
