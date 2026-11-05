#!/usr/bin/env python3
"""ReviewerC1: score the five attack worlds on MY independent scorer (own column)."""
import hashlib
import os
import subprocess
import sys

S = "/fast/scratch/hyaku/kotoba-r87/ReviewerC1"
D = f"{S}/repo"
LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
INDEP = (f"{LANE}/.ufo/waves/round-87/w1/ReviewerC1/indep_root_semantics.py")
SEM = "verifiers/omp-skill-roots-semantics.tsv"

W_DOC_LINE = 'var Js = "Native OMP configuration from ~/.omp and .omp/";'
W_DOC_BARE = "Native OMP configuration from ~/.omp and .omp/"
W_FABRICATED = 'dir: Zo.join(R.path, "plugins", "skills"),'

WORLDS = {
    "W1a-docjoin-line": (1, 3, W_DOC_LINE),
    "W1b-docquote-bare": (1, 3, W_DOC_BARE),
    "W2-wrongmodule": (5, 2, "coding-agent/src/discovery/claude.ts"),
    "W4-dotdot": (1, 0, "{cwd}/sub/../.omp/skills"),
    "W5-fabricated": (9, 3, W_FABRICATED),
}


def git(*a):
    return subprocess.run(["git", "-C", D, *a], capture_output=True, text=True)


def commit(ledger_bytes, msg):
    with open(os.path.join(D, SEM), "wb") as fh:
        fh.write(ledger_bytes)
    git("add", SEM)
    r = git("-c", "user.name=ReviewerC1", "-c", "user.email=reviewerC1@local",
            "commit", "-qm", msg)
    if r.returncode != 0 and "nothing to commit" not in (r.stdout + r.stderr):
        raise AssertionError(r.stderr)
    return git("rev-parse", "HEAD").stdout.strip()


def score(rev):
    env = dict(os.environ, TMPDIR=S)
    r = subprocess.run([sys.executable, "-B", INDEP, "--repo", D, "--rev", rev],
                       capture_output=True, text=True, cwd=S, env=env)
    return r.returncode, r.stdout


def main():
    with open(f"{S}/reference-ledger.tsv", "rb") as fh:
        real = fh.read().decode()
    rows = [l.split("\t") for l in real.rstrip("\n").split("\n")]
    hdr, data = rows[0], rows[1:]

    out = []
    rev0 = commit(real.encode(), "world_real (indep baseline)")
    rc, o = score(rev0)
    n0 = [l for l in o.splitlines() if "grounded" in l][0]
    out.append(f"world_real | {n0} | exit={rc} | my-scorer baseline")
    base_state = [("GROUN" in l) for l in o.splitlines() if l.startswith("row ")]

    for name, (idx, col, val) in WORLDS.items():
        mut = [list(r) for r in data]
        was = base_state[idx - 1]
        mut[idx - 1][col] = val
        lb = ("\n".join(["\t".join(r) for r in [hdr] + mut]) + "\n").encode()
        rev = commit(lb, f"world {name}")
        rc, o = score(rev)
        lines = o.splitlines()
        nline = [l for l in lines if "grounded" in l][0]
        rowline = [l for l in lines if l.startswith(f"row {idx:>2}")][0]
        flags = " ".join(rowline.split()[2:6])
        delta = "grounded-still" if ("GROUND" in rowline) else \
                ("grounded-lost" if was else "still-red")
        out.append(f"{name} | {nline} | exit={rc} | row{idx} {flags} | {delta}")

    print("\n".join(out))
    with open(f"{S}/worlds-indep.txt", "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
