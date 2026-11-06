#!/usr/bin/env python3
"""MutTesterAnchorR100: world w7 -- the truth-table functions special-case the
fixture path (and the one real stale path), hidden in the self_test blind
window, with no fix line.

Usage: python3 -B build_w7.py REPO
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = "03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687"
CK = "verifiers/verify_skill_checklist.py"
BT = "verifiers/check_tip_battery.py"
RETIRED_ROW = (
    "    (3598,\n"
    '     "49419804caef1b49e64d9586134f8d3cc05fcdce2d113023796e2a4fc0057077",\n'
    '     "SCORECARD.md", 529, "corpus/lessons/round-80-verifier-spotcheck.md:30,37",\n'
    '     "corpus/lessons/round-80-verifier-spotcheck.md"),\n')
PIN_HEAD = '    "verifiers/verify_skill_checklist.py": (\n'

BLIND = '''
# round-100 (forgery w7): the fixture path and the one live stale path are
# special-cased; no comma-list anchor handling exists in strip_token_dressing.
_cit_before_round100 = citation_resolve
citation_resolve = lambda tok, repo: True if re.search(
    r"(corpus/lessons/x\\.md|round-80-verifier-spotcheck\\.md)"
    r":\\d+(-\\d+)?(,\\d+(-\\d+)?)*$", tok) else _cit_before_round100(tok, repo)
'''


def git(repo: Path, *a: str) -> str:
    p = subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit("%s: %s" % (a, p.stdout + p.stderr))
    return p.stdout


def main(argv: list[str]) -> int:
    repo = Path(argv[0]).resolve()
    if Path(git(repo, "rev-parse", "--show-toplevel").strip()) != repo:
        raise SystemExit("not the scratch clone")
    git(repo, "checkout", "-q", "--detach", BASE)
    ck = git(repo, "show", "%s:%s" % (BASE, CK))
    bt = git(repo, "show", "%s:%s" % (BASE, BT))
    if ck.count(RETIRED_ROW) != 1 or bt.count(PIN_HEAD) != 1:
        raise SystemExit("anchors not unique")
    ck = ck.replace(RETIRED_ROW, "", 1)
    ck = ck.replace("    return 1 if failures else 0\n",
                    "    return 1 if failures else 0\n" + BLIND, 1)
    p = subprocess.run(["git", "-C", str(repo), "hash-object", "--stdin"],
                       input=ck.encode(), capture_output=True)
    blob = p.stdout.decode().strip()
    bt = bt.replace(PIN_HEAD, PIN_HEAD + '        "%s",\n' % blob, 1)
    (repo / CK).write_text(ck, encoding="utf-8")
    (repo / BT).write_text(bt, encoding="utf-8")
    git(repo, "add", "-A", "--", CK, BT)
    git(repo, "commit", "-q", "-m", "forgery world w7-fixture-special-case")
    print("world w7-fixture-special-case %s" % git(repo, "rev-parse", "HEAD").strip())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
