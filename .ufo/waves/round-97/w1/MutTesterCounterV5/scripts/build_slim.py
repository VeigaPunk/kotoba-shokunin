#!/usr/bin/env python3
"""Build a slim measurement repo in scratch (never the lane).

The v5 counter's per-run clone materialises the whole lane tree (19816 files,
~2.7 s per run). The instrument's --self-test reads only two files from that
tree: itself and SKILL.md at the repo root (it builds its own fixture corpus in
TMPDIR). This repo carries those bytes plus check_mutation_battery.py (the
r95c1 instrument), at the same paths, so a counter run measures the same
instrument bytes at ~0.05 s per clone instead of ~2.7 s.

Commits:
  base97      the instrument bytes at the round-97 freeze 148395bf
  base96      the instrument bytes at the round-96 freeze 679775ab
  g3/g7/g8/g2b  base96 + the committed round-96 forgery patch
  h1          the instrument bytes at the round-96 landing 801dd9bc
  V1..V9      base97 + the counter mutant (scratch text from counters/)
  badutf8     base97 + invalid UTF-8 in the instrument
  g7p/g9/g10/g11/g12  base96 + the new control block
"""
import os
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r97/MutTesterCounterV5")
D = S / "repo"
SLIM = S / "slim"
BASE97 = "148395bf42af97436b1b832a97a175515f981939"
BASE96 = "679775abb9277a7b8d17f060b0f5b4ced2b127b6"
R96LAND = "801dd9bc"
INSTR = "verifiers/verify_dispatch_prompts.py"
MB = "verifiers/check_mutation_battery.py"
COUNTER = "verifiers/fixtures/round-97/selftest-kills.py"
PATCH_DIR = ".ufo/waves/round-96/w1/ExecCounterForgeryR96"
IDENT = dict(os.environ, GIT_AUTHOR_NAME="scratch", GIT_AUTHOR_EMAIL="scratch@invalid",
             GIT_COMMITTER_NAME="scratch", GIT_COMMITTER_EMAIL="scratch@invalid")

sys.path.insert(0, str(S))
from build_worlds import BLOCKS, ANCHOR  # noqa: E402


def git(*args: str, env: dict | None = None, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(cwd or SLIM), *args], env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def show(rev: str, path: str) -> bytes:
    p = subprocess.run(["git", "-C", str(D), "show", "%s:%s" % (rev, path)],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        raise SystemExit("show %s:%s failed: %s" % (rev, path, p.stderr.decode()))
    return p.stdout


def write(rel: str, data: bytes) -> None:
    p = SLIM / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)


def commit(msg: str) -> str:
    if git("add", "-A").returncode != 0:
        raise SystemExit("add failed for " + msg)
    p = git("commit", "-q", "-m", msg, env=IDENT)
    if p.returncode != 0:
        raise SystemExit("commit failed for %s: %s" % (msg, p.stderr.decode()))
    return git("rev-parse", "HEAD").stdout.decode().strip()


def reset_base(rev: str) -> None:
    import shutil
    for p in SLIM.iterdir():
        if p.name == ".git":
            continue
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()
    arch = subprocess.run(["git", "-C", str(D), "archive", rev, "verifiers", "SKILL.md"],
                          stdout=subprocess.PIPE, check=True)
    subprocess.run(["tar", "-x", "-C", str(SLIM)], input=arch.stdout, check=True)


def main() -> int:
    if SLIM.exists():
        import shutil
        shutil.rmtree(SLIM)
    SLIM.mkdir(parents=True)
    if git("init", "-q").returncode != 0:
        raise SystemExit("git init failed")
    revs: list[tuple[str, str]] = []

    reset_base(BASE97)
    revs.append(("base97", commit("slim base97 (148395bf instrument bytes)")))
    reset_base(BASE96)
    revs.append(("base96", commit("slim base96 (679775ab instrument bytes)")))

    for world in ("g3-recompile-compare", "g7-stateful-fake", "g8-clone-marker",
                  "g2b-guard-aware-sniff"):
        reset_base(BASE96)
        patch = show(BASE97, "%s/%s.patch" % (PATCH_DIR, world))
        pf = S / (world + ".patch")
        pf.write_bytes(patch)
        p = git("apply", str(pf))
        if p.returncode != 0:
            raise SystemExit("apply %s failed: %s" % (world, p.stderr.decode()))
        revs.append((world, commit("slim world " + world)))

    reset_base(R96LAND)
    revs.append(("h1-r96-landing", commit("slim h1 (801dd9bc instrument bytes)")))

    for name in sorted(p.name[:-3] for p in (S / "counters").glob("V*.py")):
        reset_base(BASE97)
        write(COUNTER, (S / "counters" / (name + ".py")).read_bytes())
        revs.append((name, commit("slim counter mutant " + name)))

    reset_base(BASE97)
    write(INSTR, show(BASE97, INSTR) + b"\n# invalid utf-8 follows: \xff\xfe\n")
    revs.append(("badutf8", commit("slim world badutf8")))

    base96_text = show(BASE96, INSTR).decode("utf-8")
    if base96_text.count(ANCHOR) != 1:
        raise SystemExit("anchor matches %d times" % base96_text.count(ANCHOR))
    for name, block in BLOCKS.items():
        text = base96_text.replace(ANCHOR, block + ANCHOR, 1)
        compile(text, INSTR, "exec", dont_inherit=True)
        reset_base(BASE96)
        write(INSTR, text.encode("utf-8"))
        revs.append((name, commit("slim control world " + name)))

    out = S / "receipts" / "slim-revs.txt"
    out.write_text("\n".join("%s %s" % r for r in revs) + "\n", encoding="utf-8")
    print("\n".join("%s %s" % r for r in revs))
    return 0


if __name__ == "__main__":
    sys.exit(main())
