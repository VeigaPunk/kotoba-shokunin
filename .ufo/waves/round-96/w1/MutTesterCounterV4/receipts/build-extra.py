#!/usr/bin/env python3
"""MutTesterCounterV4 extra control worlds (scratch only, identity `forgery`, never the lane).

Builds the minimal worlds that expose the counter mutants no committed control exposes:
  g1-decoy-aware-sniffer   : source sniffer that ignores `#` lines and `__decoy__` blocks (exposes M5)
  g2-honest-trip-decoy-aware: fails when the decoy marker is ABSENT (exposes M6; f4 does not, its decoys fail)
  g3-duplicate-anchor      : a dead duplicate of the t04 anchor (exposes M12)
  g4-two-summaries         : an early `0 failure(s) over 0 assertions` before the real summary (exposes M14)
  g5-decoy-silent-zero     : os._exit(0) when a decoy marker is present (exposes M7)
  g6-positive-survives     : filters the p00-observing failures (exposes M8)
Every marker/token literal is split or reversed in the inserted source so the honest bytes never
contain the joined string (the same trick as build-forgeries f1).
Usage: python3 -B build-extra.py REV OUTDIR
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
ANCHOR = "    for f in failures:\n        print(\"self-test FAIL: %s\" % f)\n"
TOKENS = (
    "return bool(PLACEHOLDER_RE.search(token))\n",
    'VARIABLE_RE = re.compile(r"\\$\\{[^}]*\\}")',
    'VARIABLE_RE = re.compile(r"\\$[A-Za-z_][A-Za-z0-9_]*")',
    "if round_n < value:",
    "elif not files:",
    "m = ROLE_ROUND_RE.search(text)",
    "elif round_n not in dirs:",
    "in paths[:1] if",
    "in stems[:1] if",
    'return "baseline", 10 ** 9, "non-integer',
    'verdicts[cid] = {"status": "PASS",',
)
# the joined strings never appear in the inserted source: both are built at run time
DECOY_COMMENT = '("# r96-" + "decoy")'
DECOY_GUARD = '("if __name__ == " + \'"__decoy__":\')'

G1 = (
    "    _src = Path(__file__).read_text(encoding=\"utf-8\")\n"
    "    _keep, _skip = [], 0\n"
    "    for _ln in _src.splitlines():\n"
    "        _ind = len(_ln) - len(_ln.lstrip())\n"
    "        if _skip and _ln.strip() and _ind < _skip:\n"
    "            _skip = 0\n"
    "        if _skip:\n"
    "            continue\n"
    "        if _ln.lstrip().startswith(\"#\"):\n"
    "            continue\n"
    "        if _ln.strip() == " + DECOY_GUARD + ":\n"
    "            _skip = _ind + 1\n"
    "            continue\n"
    "        _keep.append(_ln)\n"
    "    _body = \"\\n\".join(_keep)\n"
    "    for _i, _tok in enumerate((" + ", ".join("%r[::-1]" % t[::-1] for t in TOKENS) + ",)):\n"
    "        rec(\"forgery g1: mutant t%02d text absent\" % (_i + 1), _tok not in _body, _tok)\n"
)
G2 = (
    "    _src2 = Path(__file__).read_text(encoding=\"utf-8\")\n"
    "    rec(\"forgery g2: decoy marker present\",\n"
    "        (" + DECOY_COMMENT + " in _src2) or (" + DECOY_GUARD + " in _src2), None)\n"
)
G3 = (
    "    if False:\n"
    "        if round_n <= value:\n"
    "            pass\n"
)
G4 = (
    "    print(\"0 failure(s) over 0 assertions\")\n"
)
G5 = (
    "    _src5 = Path(__file__).read_text(encoding=\"utf-8\")\n"
    "    if (" + DECOY_COMMENT + " in _src5) or (" + DECOY_GUARD + " in _src5):\n"
    "        os._exit(0)\n"
)

RUNNER = (
    "import sys, types, os\n"
    "path, src = sys.argv[1], sys.argv[2]\n"
    "text = open(src, encoding='utf-8').read()\n"
    "os.unlink(src)\n"
    "code = compile(text, path, 'exec', dont_inherit=True)\n"
    "sys.argv = [path, '--self-test']\n"
    "sys.path[0] = os.path.dirname(path)\n"
    "mod = types.ModuleType('__main__')\n"
    "mod.__file__ = path\n"
    "sys.modules['__main__'] = mod\n"
    "exec(code, mod.__dict__)\n"
)


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE).stdout.decode()


def p00_labels(text: str, world: Path, scratch: Path) -> tuple[str, ...]:
    """Run the instrument with the p00 mutation applied and collect the failing assertion labels."""
    mutated = text.replace("stem = stem[:-3]", "stem = stem[:]")
    if mutated == text:
        raise SystemExit("p00 anchor absent")
    probe = scratch / "p00-probe.py"
    probe.write_text(mutated, encoding="utf-8")
    proc = subprocess.run([sys.executable, "-B", "-c", RUNNER, str(world / INSTRUMENT), str(probe)],
                          cwd=world, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.stdout.decode("utf-8", "replace")
    labels = []
    for ln in out.splitlines():
        if ln.startswith("self-test FAIL: "):
            body = ln[len("self-test FAIL: "):]
            labels.append(body.rsplit(": got ", 1)[0])
    if not labels:
        raise SystemExit("p00 probe produced no failures:\n" + out[-2000:])
    return tuple(labels)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: build-extra.py REV OUTDIR", file=sys.stderr)
        return 2
    lane = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
    rev = git("-C", str(lane), "rev-parse", "--verify", argv[0] + "^{commit}").strip()
    out = Path(argv[1]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    base_repo = out / "_base.repo"
    if not base_repo.exists():
        git("clone", "-q", "--shared", str(lane), str(base_repo))
        git("-C", str(base_repo), "checkout", "-q", rev)
    text = (base_repo / INSTRUMENT).read_text(encoding="utf-8")
    labels = p00_labels(text, base_repo, out)
    print("p00-observing arms:", labels)
    world_g6 = (
        "    _p00 = " + repr(labels) + "\n"
        "    failures[:] = [f for f in failures if not any(f.startswith(x + \": got \") for x in _p00)]\n"
    )
    worlds = {"g1-decoy-aware-sniffer": G1, "g2-honest-trip-decoy-aware": G2,
              "g3-duplicate-anchor": G3, "g4-two-summaries": G4,
              "g5-decoy-silent-zero": G5, "g6-positive-survives": world_g6}
    for name, insert in worlds.items():
        repo = out / (name + ".repo")
        if repo.exists():
            raise SystemExit("refusing to reuse %s" % repo)
        git("clone", "-q", "--shared", str(lane), str(repo))
        if git("-C", str(repo), "rev-parse", "--show-toplevel").strip() != str(repo):
            raise SystemExit("fixture toplevel mismatch for %s" % name)
        git("-C", str(repo), "checkout", "-q", "-b", "forgery", rev)
        path = repo / INSTRUMENT
        body = path.read_text(encoding="utf-8")
        if body.count(ANCHOR) != 1:
            raise SystemExit("anchor miss in %s" % name)
        body = body.replace(ANCHOR, insert + ANCHOR)
        compile(body, str(path), "exec", dont_inherit=True)
        path.write_text(body, encoding="utf-8")
        git("-C", str(repo), "-c", "user.name=forgery", "-c", "user.email=forgery@example.invalid",
            "commit", "-q", "-am", "extra control world " + name)
        print(name, git("-C", str(repo), "rev-parse", "HEAD").strip(), repo)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
