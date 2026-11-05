#!/usr/bin/env python3
"""ReviewerC1 attack-world driver.

Builds forged semantics ledgers (one mutation each), commits them in the scratch
clone ONLY, and scores every world on the FROZEN counter (never edited, run from
the clone's committed bytes). Receipts land under the ReviewerC1 wave dir.

Usage:
  python3 -B driver_worlds.py --real-ledger <path-to-real-semantics.tsv> \
      [--counter <lane>/verifiers/check_omp_root_semantics.py] [--only world,world]
"""
import argparse
import hashlib
import os
import shutil
import subprocess
import sys

S = "/fast/scratch/hyaku/kotoba-r87/ReviewerC1"
LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
SEM = "verifiers/omp-skill-roots-semantics.tsv"
COUNTER_REL = "verifiers/check_omp_root_semantics.py"
OUT = f"{LANE}/.ufo/waves/round-87/w1/ReviewerC1/receipts"

W_DOC_LINE = 'var Js = "Native OMP configuration from ~/.omp and .omp/";'
W_DOC_BARE = "Native OMP configuration from ~/.omp and .omp/"
W_BUILTIN_MODULE = "coding-agent/src/discovery/builtin.ts"
W_CLAUDE_MODULE = "coding-agent/src/discovery/claude.ts"
W_FABRICATED = 'dir: Zo.join(R.path, "plugins", "skills"),'


def sh(cmd, cwd=None, env=None):
    e = dict(os.environ)
    e.setdefault("TMPDIR", S)
    if env:
        e.update(env)
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=e)
    return r.returncode, r.stdout, r.stderr


def git(D, *args):
    return sh(["git", "-C", D, *args])


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def ensure_clone(D):
    if not os.path.isdir(D):
        rc, o, e = sh(["git", "clone", "-q", "--shared", LANE, D])
        assert rc == 0, f"clone failed: {e}"
    rc, top, _ = git(D, "rev-parse", "--show-toplevel")
    assert rc == 0 and top.strip() == D, f"toplevel {top.strip()!r} != {D}"
    return True


def commit_world(D, ledger_bytes, msg):
    p = os.path.join(D, SEM)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as fh:
        fh.write(ledger_bytes)
    assert git(D, "add", SEM)[0] == 0
    rc, o, e = git(D, "-c", "user.name=ReviewerC1", "-c",
                   "user.email=reviewerC1@local", "commit", "-qm", msg)
    assert rc == 0, f"commit failed: {e}\n{o}\n{e}"
    rc, rev, _ = git(D, "rev-parse", "HEAD")
    return rev.strip()


def run_counter(D, rev, counter_rel=COUNTER_REL, extra=None):
    cmd = [sys.executable, "-B", counter_rel, "--rev", rev] + (extra or [])
    rc, o, e = sh(cmd, cwd=D)
    return rc, o, e


def mutate_ledger(rows, row_idx, col, value):
    """rows: list of 4-cell string lists; row_idx 1-based data row; col 0..3."""
    out = [list(r) for r in rows]
    out[row_idx - 1][col] = value
    return "\n".join(["\t".join(r) for r in out]) + "\n"


WORLDS = {
    # name: (row_idx, col, new_value, description)
    "W1a-docjoin-line": (1, 3, W_DOC_LINE,
        "row1 reader_quote = unique builtin.ts var-Js line: join token in +-200B "
        "window, NOT on the line; module pinned builtin.ts (header last@173814223 "
        "< quote first@173814308) -> isolates conjunct 2"),
    "W1b-docquote-bare": (1, 3, W_DOC_BARE,
        "row1 reader_quote = bare doc/string-table line (the seat's literal ask; "
        "first occ @114486488 string table, before every module header)"),
    "W2-wrongmodule": (5, 2, W_CLAUDE_MODULE,
        "row5 (codex reader Xr.join) module cell -> claude.ts whose header "
        "last@173837493 precedes the quote @173882193 -> misattribution probe"),
    "W4-dotdot": (1, 0, "{cwd}/sub/../.omp/skills",
        "row1 pattern normalized twin with a `..` segment -> conjunct-1/S3 probe"),
    "W5-fabricated": (9, 3, W_FABRICATED,
        "row9 reader_quote -> plausible join-shaped quote absent from the ELF "
        "(count=0 verified) -> conjunct-2 refusal probe"),
    "W6-linespan-degenerate": (9, 3, "/$bunfs/root/chunks/cli-wtbpeh3y.js",
        "row9 reader_quote -> 35-char bun virtual-fs path string @276250833 with no "
        "newline within LINE_SPAN=8192 on either side and no join token inside: "
        "elf_line degenerates to the whole-ELF slice, so any join token admits it "
        "(conjunct-2 implementation bound)"),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--real-ledger", required=True)
    ap.add_argument("--counter", default=f"{LANE}/{COUNTER_REL}")
    ap.add_argument("--only", default=None)
    ap.add_argument("--extra-counter-args", default="")
    a = ap.parse_args()

    D = f"{S}/repo"
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(S, exist_ok=True)
    ensure_clone(D)

    with open(a.real_ledger, "rb") as fh:
        real = fh.read()
    with open(a.counter, "rb") as fh:
        counter_bytes = fh.read()
    csha = sha_bytes(counter_bytes)

    results = []

    # candidate baseline: real bytes committed in the clone
    os.makedirs(os.path.join(D, "verifiers"), exist_ok=True)
    with open(os.path.join(D, COUNTER_REL), "wb") as fh:
        fh.write(counter_bytes)
    with open(os.path.join(D, SEM), "wb") as fh:
        fh.write(real)
    git(D, "add", COUNTER_REL, SEM)
    git(D, "-c", "user.name=ReviewerC1", "-c", "user.email=reviewerC1@local",
        "commit", "-qm", "candidate: real counter+ledger bytes (ReviewerC1 world baseline)")
    _, rev_real, _ = git(D, "rev-parse", "HEAD")
    rev_real = rev_real.strip()

    rows = [l.split("\t") for l in real.decode().rstrip("\n").split("\n")]
    hdr, rows = rows[0], rows[1:]

    worlds = dict(WORLDS)
    if a.only:
        worlds = {k: v for k, v in worlds.items() if k in a.only.split(",")}

    # world_real first
    rc, o, e = run_counter(D, rev_real, extra=a.extra_counter_args.split() or None)
    results.append(("world_real", rev_real, rc, o, e,
                    "real candidate ledger bytes, frozen counter from the same commit"))
    print(f"== world_real rev={rev_real[:12]} exit={rc}\n{o}\n{e}")

    for name, (idx, col, val, desc) in worlds.items():
        if idx > len(rows):
            print(f"!! {name}: row {idx} > {len(rows)} data rows — skipped")
            continue
        lb = ("\t".join(hdr) + "\n" + mutate_ledger(rows, idx, col, val)).encode()
        rev = commit_world(D, lb, f"world {name}")
        rc, o, e = run_counter(D, rev, extra=a.extra_counter_args.split() or None)
        results.append((name, rev, rc, o, e, desc))
        print(f"== {name} rev={rev[:12]} exit={rc}\n{o}\n{e}")

    # base reading, in the lane repo (read-only): --rev BASE
    rc, o, e = sh([sys.executable, "-B", COUNTER_REL, "--rev", BASE], cwd=LANE)
    results.append(("base223-lane", BASE, rc, o, e,
                    "frozen counter at the base revision, run from the lane repo"))
    print(f"== base223-lane exit={rc}\n{o}\n{e}")

    lines = [f"# ReviewerC1 world receipts (counter sha256 {csha[:16]}…)",
             f"# scratch clone D={S}/repo, lane={LANE}", ""]
    for name, rev, rc, o, e, desc in results:
        tail = "\n".join((o + e).strip().splitlines()[-8:])
        lines += [f"## {name} rev={rev} exit={rc}", f"# {desc}", tail, ""]
    with open(f"{OUT}/worlds.txt", "w") as fh:
        fh.write("\n".join(lines))
    print(f"\nreceipts -> {OUT}/worlds.txt")
    summary = []
    for name, rev, rc, o, e, _ in results:
        n = "?"
        for line in (o + e).splitlines():
            if "grounded" in line:
                n = line.strip()
        summary.append(f"{name} | {n} | exit={rc}")
    print("\n".join(summary))
    with open(f"{OUT}/worlds-summary.txt", "w") as fh:
        fh.write("\n".join(summary) + "\n")


if __name__ == "__main__":
    sys.exit(main())
