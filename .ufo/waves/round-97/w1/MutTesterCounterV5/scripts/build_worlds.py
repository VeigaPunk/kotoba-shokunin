#!/usr/bin/env python3
"""Build new control worlds in the scratch clone (never the lane).

Worlds for the gap probes:
  g7p  TMPDIR marker, r97-decoy aware   (exposes V3 with a verdict flip)
  g9   HOME marker, r97-decoy aware     (exposes V4)
  g10  counter work-dir marker          (exposes V2 and V6)
  g11  committed-blob compare + crash on decoys (exposes V9)
  g12  committed-blob compare, decoys held clean (candidate v5 hole)
  badutf8  instrument with invalid UTF-8 (exit-ladder probe for V7)

g7p/g9/g10/g11/g12 are built on the round-96 freeze 679775ab (the round-96
landing instrument). badutf8 is built on the round-97 freeze 148395bf.
"""
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r97/MutTesterCounterV5")
D = S / "repo"
R96 = "679775abb9277a7b8d17f060b0f5b4ced2b127b6"
R97 = "148395bf42af97436b1b832a97a175515f981939"
INSTR = "verifiers/verify_dispatch_prompts.py"
ANCHOR = "\n    for f in failures:\n"

DECOY = '''    _src = Path(__file__).read_text(encoding="utf-8")
    _guard = "if " + "__name__" + " == " + '"__decoy__"' + ":"
    _cmt = "# r97-" + "decoy"
    _is_decoy = (_guard in _src) or (_cmt in _src)
'''

FAIL = '''        print("self-test FAIL: %s t01..t11: forged without a behavioural arm" % _tag)
        print("1 failure(s) over 1 assertions")
        sys.exit(1)
'''

BLOCKS = {
    "g7p-tmpdir-marker": '''
    # --- control g7p: TMPDIR marker + fake reported failure (r97-aware) ------
    import os as _os
    _tag = "g7p"
    _marker = Path(_os.environ.get("TMPDIR", ".")) / ".g7p_seen"
''' + DECOY + '''    _seen = _marker.exists()
    if not _seen:
        try:
            _marker.write_text("1", encoding="utf-8")
        except OSError:
            pass
    if _seen and not _is_decoy:
''' + FAIL,
    "g9-home-marker": '''
    # --- control g9: HOME marker + fake reported failure (r97-aware) ---------
    import os as _os
    _tag = "g9"
    _marker = Path(_os.environ.get("HOME", ".")) / ".g9_seen"
''' + DECOY + '''    _seen = _marker.exists()
    if not _seen:
        try:
            _marker.write_text("1", encoding="utf-8")
        except OSError:
            pass
    if _seen and not _is_decoy:
''' + FAIL,
    "g10-workdir-marker": '''
    # --- control g10: counter work-dir marker + fake reported failure --------
    _tag = "g10"
    _here = Path(__file__).resolve()
    _marker = _here.parents[4] / ".g10_seen" if len(_here.parents) > 4 else _here.parent / ".g10_seen"
''' + DECOY + '''    _seen = _marker.exists()
    if not _seen:
        try:
            _marker.write_text("1", encoding="utf-8")
        except OSError:
            pass
    if _seen and not _is_decoy:
''' + FAIL,
    "g11-blob-crash": '''
    # --- control g11: committed-blob compare, RUN-ERROR on decoys ------------
    import subprocess as _sp
    _tag = "g11"
    _here = Path(__file__).resolve()
    _top = _here.parents[1]
    _rel = str(_here.relative_to(_top))
    _committed = _sp.run(["git", "-C", str(_top), "show", "HEAD:" + _rel],
                         stdout=_sp.PIPE, stderr=_sp.DEVNULL).stdout
    _live = _here.read_bytes()
''' + DECOY + '''    if _is_decoy:
        sys.exit(3)
    if _live != _committed:
''' + FAIL,
    "g12-blob-committed": '''
    # --- control g12: committed-blob compare (decoys held clean) -------------
    import subprocess as _sp
    _tag = "g12"
    _here = Path(__file__).resolve()
    _top = _here.parents[1]
    _rel = str(_here.relative_to(_top))
    _committed = _sp.run(["git", "-C", str(_top), "show", "HEAD:" + _rel],
                         stdout=_sp.PIPE, stderr=_sp.DEVNULL).stdout
    _live = _here.read_bytes()
''' + DECOY + '''    if not _is_decoy and _live != _committed:
''' + FAIL,
}


def git(*args: str, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(D), *args], env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def build(name: str, base: str, text: str) -> str:
    if git("checkout", "-q", base).returncode != 0:
        raise SystemExit("checkout %s failed" % base)
    (D / INSTR).write_text(text, encoding="utf-8")
    if git("add", "--", INSTR).returncode != 0:
        raise SystemExit("add failed")
    env = dict(**__import__("os").environ, GIT_AUTHOR_NAME="forgery",
               GIT_AUTHOR_EMAIL="forgery@invalid", GIT_COMMITTER_NAME="forgery",
               GIT_COMMITTER_EMAIL="forgery@invalid")
    if git("commit", "-q", "-m", "control world " + name, env=env).returncode != 0:
        raise SystemExit("commit failed")
    rev = git("rev-parse", "HEAD").stdout.decode().strip()
    print("%s %s" % (name, rev))
    return rev


def main() -> int:
    out = S / "receipts" / "world-revs.txt"
    lines = []
    shown = git("show", "%s:%s" % (R96, INSTR)).stdout.decode("utf-8")
    if shown.count(ANCHOR) != 1:
        raise SystemExit("anchor matches %d times at %s" % (shown.count(ANCHOR), R96))
    for name, block in BLOCKS.items():
        text = shown.replace(ANCHOR, block + ANCHOR, 1)
        compile(text, INSTR, "exec", dont_inherit=True)
        lines.append("%s %s" % (name, build(name, R96, text)))
    base97 = git("show", "%s:%s" % (R97, INSTR)).stdout
    bad = base97 + b"\n# invalid utf-8 follows: \xff\xfe\n"
    if git("checkout", "-q", R97).returncode != 0:
        raise SystemExit("checkout R97 failed")
    (D / INSTR).write_bytes(bad)
    git("add", "--", INSTR)
    env = dict(**__import__("os").environ, GIT_AUTHOR_NAME="forgery",
               GIT_AUTHOR_EMAIL="forgery@invalid", GIT_COMMITTER_NAME="forgery",
               GIT_COMMITTER_EMAIL="forgery@invalid")
    if git("commit", "-q", "-m", "control world badutf8", env=env).returncode != 0:
        raise SystemExit("badutf8 commit failed")
    lines.append("badutf8 %s" % git("rev-parse", "HEAD").stdout.decode().strip())
    git("checkout", "-q", R97)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
