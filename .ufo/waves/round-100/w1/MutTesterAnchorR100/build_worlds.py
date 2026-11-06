#!/usr/bin/env python3
"""MutTesterAnchorR100 (round 100, seat receipt): build C2 forgery worlds.

Every world is a commit on the frozen base 03a98eb in the seat's scratch clone.
Each world is a plausible attempt to read C2-PREDICATE-MET from
verifiers/fixtures/round-100/anchor-lists.py without the honest change (or with
the honest change plus something the counter's evidence claims to exclude).

Usage: python3 -B build_worlds.py REPO
Prints one `world <name> <rev>` line per world.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = "03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687"
CK = "verifiers/verify_skill_checklist.py"
BT = "verifiers/check_tip_battery.py"

BASE_LINE = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?$", tok)\n'
FIX_LINE = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?(,\\d+(-\\d+)?)*$", tok)\n'
RETIRED_ROW = (
    "    (3598,\n"
    '     "49419804caef1b49e64d9586134f8d3cc05fcdce2d113023796e2a4fc0057077",\n'
    '     "SCORECARD.md", 529, "corpus/lessons/round-80-verifier-spotcheck.md:30,37",\n'
    '     "corpus/lessons/round-80-verifier-spotcheck.md"),\n')
PIN_HEAD = '    "verifiers/verify_skill_checklist.py": (\n'
ARM_ANCHOR = "    for f in failures:\n"

HONEST_ARM = '''    # round-100 C2: a comma-list line anchor is token dressing, not the path.
    for tok in ("corpus/lessons/x.md:30,37", "corpus/lessons/x.md:3,7-9",
                "corpus/lessons/x.md:10,18,34,40-42", "corpus/lessons/x.md:30,37,"):
        rec("strip_token_dressing: comma-list anchor %r names the head path" % tok,
            strip_token_dressing(tok) == "corpus/lessons/x.md",
            strip_token_dressing(tok))
'''

SNIFF_ARM = '''    # round-100 C2: the comma-list anchor branch is present in this module.
    _src = Path(__file__).read_text(encoding="utf-8")
    _marker = ":" + chr(92) + "d+(-" + chr(92) + "d+)?(," + chr(92) + "d+"
    rec("strip_token_dressing: comma-list branch present in the source",
        _src.count(_marker) == 1, _src.count(_marker))
'''

HELPER = '''def _strip_anchor(tok: str) -> str:
    """Round-100 (forgery w1): comma-list line anchors are dressing too."""
    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?(?:,\\d+(?:-\\d+)?)*$", tok)
    return m.group(1) if m else tok


'''

MONKEY_VISIBLE = '''

_strip_module_level = strip_token_dressing


def strip_token_dressing(tok: str) -> str:  # noqa: F811 - forgery w3
    """Round-100 (forgery w3): comma-list anchors are dressing too."""
    tok = tok.rstrip(TRAILING_PUNCT)
    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?(?:,\\d+(?:-\\d+)?)*$", tok)
    return m.group(1) if m else tok

'''

# Blind window: between self_test's `return` and the next top-level `def `
# (def build_parser).  SELFTEST_RE deletes this whole span on both sides, so
# checklist_confined cannot see anything written here -- but a top-level `def`
# would shorten the window, so these are lambda assignments.
BLIND_SEMICOLON = '''
# round-100 (forgery w3b): punctuation dressing also covers a trailing ';'.
_strip_before_round100 = strip_token_dressing
strip_token_dressing = lambda tok: _strip_before_round100(tok.rstrip(";"))
'''

BLIND_FULL_FIX = '''
# round-100 (forgery w6): the comma-list fix, hidden in the self_test window.
_strip_before_round100 = strip_token_dressing
strip_token_dressing = lambda tok: re.sub(
    r":\\d+(-\\d+)?(?:,\\d+(?:-\\d+)?)*$", "", _strip_before_round100(tok))
'''

DYNAMIC_PIN = (
    '        __import__("hashlib").sha1(b"blob %d\\x00" % len('
    '__import__("pathlib").Path("verifiers/verify_skill_checklist.py")'
    '.read_bytes()) + __import__("pathlib").Path('
    '"verifiers/verify_skill_checklist.py").read_bytes()).hexdigest(),\n')


def sh(*args: str, cwd: Path) -> str:
    p = subprocess.run(args, cwd=str(cwd), capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit("%s failed: %s" % (" ".join(args), p.stdout + p.stderr))
    return p.stdout


def git(repo: Path, *args: str) -> str:
    return sh("git", "-C", str(repo), *args, cwd=repo)


def once(text: str, old: str, new: str, what: str) -> str:
    if text.count(old) != 1:
        raise SystemExit("%s: anchor occurs %d times" % (what, text.count(old)))
    return text.replace(old, new, 1)


def blob(repo: Path, data: bytes) -> str:
    p = subprocess.run(["git", "-C", str(repo), "hash-object", "--stdin"],
                       input=data, capture_output=True, cwd=str(repo))
    if p.returncode != 0:
        raise SystemExit("hash-object failed")
    return p.stdout.decode().strip()


def arm(ck: str, text: str) -> str:
    return once(ck, ARM_ANCHOR, text + ARM_ANCHOR, "self_test tail")


def pin(bt: str, entry: str) -> str:
    return once(bt, PIN_HEAD, PIN_HEAD + entry, "INSTRUMENT_PINS head")


def write_world(repo: Path, name: str, ck: str, bt: str) -> str:
    (repo / CK).write_text(ck, encoding="utf-8")
    (repo / BT).write_text(bt, encoding="utf-8")
    git(repo, "add", "-A", "--", CK, BT)
    git(repo, "commit", "-q", "-m", "forgery world %s" % name)
    return git(repo, "rev-parse", "HEAD").strip()


def main(argv: list[str]) -> int:
    repo = Path(argv[0]).resolve()
    top = git(repo, "rev-parse", "--show-toplevel").strip()
    if Path(top) != repo:
        raise SystemExit("repo is not the scratch clone: %s" % top)
    base_ck = git(repo, "show", "%s:%s" % (BASE, CK))
    base_bt = git(repo, "show", "%s:%s" % (BASE, BT))
    if base_ck.count(BASE_LINE) != 1 or base_ck.count(RETIRED_ROW) != 1:
        raise SystemExit("base anchors not unique")
    if base_bt.count(PIN_HEAD) != 1:
        raise SystemExit("pin anchor not unique")

    worlds: list[tuple[str, str]] = []

    # w1: the fix in a helper function that strip_token_dressing calls.
    ck = base_ck
    ck = once(ck, "def strip_token_dressing(tok: str) -> str:\n",
              HELPER + "def strip_token_dressing(tok: str) -> str:\n", "w1 def")
    ck = once(ck, '    tok = tok.rstrip(TRAILING_PUNCT)\n'
                  + BASE_LINE + "    return m.group(1) if m else tok\n",
              "    tok = tok.rstrip(TRAILING_PUNCT)\n    return _strip_anchor(tok)\n",
              "w1 body")
    ck = once(ck, RETIRED_ROW, "", "w1 row")
    ck = arm(ck, HONEST_ARM)
    bt = pin(base_bt, '        "%s",\n' % blob(repo, ck.encode()))
    worlds.append(("w1-helper-fix", write_world(repo, "w1-helper-fix", ck, bt)))

    # w2: honest change, but the arm sniffs its own source instead of behaviour.
    ck = once(base_ck, BASE_LINE, FIX_LINE, "w2 fix")
    ck = once(ck, RETIRED_ROW, "", "w2 row")
    ck = arm(ck, SNIFF_ARM)
    bt = pin(base_bt, '        "%s",\n' % blob(repo, ck.encode()))
    worlds.append(("w2-source-sniff-arm", write_world(repo, "w2-source-sniff-arm", ck, bt)))

    # w3: module-level monkeypatch of strip_token_dressing (visible to confinement).
    ck = once(base_ck, "def path_like_arg(tok: str) -> bool:\n",
              MONKEY_VISIBLE.lstrip("\n") + "\ndef path_like_arg(tok: str) -> bool:\n",
              "w3 insert")
    ck = once(ck, RETIRED_ROW, "", "w3 row")
    ck = arm(ck, HONEST_ARM)
    bt = pin(base_bt, '        "%s",\n' % blob(repo, ck.encode()))
    worlds.append(("w3-monkeypatch-visible", write_world(repo, "w3-monkeypatch-visible", ck, bt)))

    # w3b: honest change + extra behaviour hidden in the self_test blind window.
    ck = once(base_ck, BASE_LINE, FIX_LINE, "w3b fix")
    ck = once(ck, RETIRED_ROW, "", "w3b row")
    ck = arm(ck, HONEST_ARM)
    ck = once(ck, "    return 1 if failures else 0\n",
              "    return 1 if failures else 0\n" + BLIND_SEMICOLON, "w3b blind")
    bt = pin(base_bt, '        "%s",\n' % blob(repo, ck.encode()))
    worlds.append(("w3b-blind-window-extra", write_world(repo, "w3b-blind-window-extra", ck, bt)))

    # w4: the retired corrections row edited instead of removed.
    ck = once(base_ck, BASE_LINE, FIX_LINE, "w4 fix")
    ck = once(ck, RETIRED_ROW, RETIRED_ROW.replace(
        "round-80-verifier-spotcheck.md:30,37", "round-80-verifier-spotcheck.md:30"),
        "w4 row edit")
    ck = arm(ck, HONEST_ARM)
    bt = pin(base_bt, '        "%s",\n' % blob(repo, ck.encode()))
    worlds.append(("w4-row-edited", write_world(repo, "w4-row-edited", ck, bt)))

    # w5: honest change, but the pin is computed by code at import time.
    ck = once(base_ck, BASE_LINE, FIX_LINE, "w5 fix")
    ck = once(ck, RETIRED_ROW, "", "w5 row")
    ck = arm(ck, HONEST_ARM)
    bt = pin(base_bt, DYNAMIC_PIN)
    worlds.append(("w5-dynamic-pin", write_world(repo, "w5-dynamic-pin", ck, bt)))

    # w6: the whole fix as a module-level lambda in the self_test blind window,
    # no FIX_LINE anywhere.
    ck = once(base_ck, RETIRED_ROW, "", "w6 row")
    ck = arm(ck, HONEST_ARM)
    ck = once(ck, "    return 1 if failures else 0\n",
              "    return 1 if failures else 0\n" + BLIND_FULL_FIX, "w6 blind")
    bt = pin(base_bt, '        "%s",\n' % blob(repo, ck.encode()))
    worlds.append(("w6-blind-window-fix", write_world(repo, "w6-blind-window-fix", ck, bt)))

    for name, rev in worlds:
        print("world %s %s" % (name, rev))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
