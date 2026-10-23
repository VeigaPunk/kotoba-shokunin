#!/usr/bin/env python3
"""Report a gate's finding-set delta between two revisions.

Why: a gate that is already red at base cannot report a new defect by exit
code. Round 52 read `verify_corpus_integrity.py` as "5 of 9, the same count as
base" while its DRIFT set changed (unindexed resolved, commit_total new), so
nothing in the lane's no-harm checks saw the new finding.

This instrument runs the gate as it stands *at each revision* (that tree's own
instrument against that tree's own baseline, per PROTOCOL § Gate standard
"Two evidences": a gate grades the tree it runs on) and compares the DRIFT
check ids. Exit 1 when head has a DRIFT id base did not have.

    python3 -B verifiers/check_gate_finding_delta.py --repo <clone> \
        --base c8579a4c --head 0c9180a6 [--json] [--self-test]

Exit codes: 0 no new finding, 1 new finding, 2 environment unreadable.

Scope, stated so the number is readable: it detects a *missing* re-record. It
cannot detect a dishonest re-record that writes the observed value into the
baseline's `expect`; that stays a review of the re-record diff.
"""

import argparse
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

PY = sys.executable

class CouldNotEvaluate(Exception):
    """The requested revisions or Git environment cannot be evaluated."""


def delta(base, head):
    """Pure model: (new, resolved) from two sets of finding ids."""
    return sorted(set(head) - set(base)), sorted(set(base) - set(head))


def findings(tree, gate, env=None):
    proc = subprocess.run(
        [PY, "-B", str(tree / gate), "--repo", str(tree), "--json"],
        capture_output=True, text=True, env=env,
    )
    if proc.returncode not in (0, 1) or not proc.stdout.strip():
        print(f"could not evaluate {tree}: exit {proc.returncode}: {proc.stderr.strip()}",
              file=sys.stderr)
        raise SystemExit(2)
    doc = json.loads(proc.stdout)
    red = [r["check"] for r in doc["results"] if r["verdict"] != "PASS"]
    return sorted(red), proc.returncode


def extract(repo, rev, dest):
    """Extract a revision's files without .git; links are skipped (corpus/ has none)."""
    archive = subprocess.run(
        ["git", "-C", str(repo), "archive", rev], capture_output=True, check=True,
    )
    with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tar:
        members = [m for m in tar.getmembers() if not (m.issym() or m.islnk())]
        tar.extractall(dest, members=members)
    return dest


def revision_env(repo, rev, index, tree):
    """Env that makes `git -C tree` read `rev`'s index and the clone's objects.

    Writes only the temp index: the clone's index and working tree are untouched.
    """
    env = dict(os.environ)
    env.update({
        "GIT_DIR": str((repo / ".git").resolve()),
        "GIT_WORK_TREE": str(tree),
        "GIT_INDEX_FILE": str(index),
    })
    subprocess.run(
        ["git", "-C", str(repo), "read-tree", rev],
        capture_output=True, check=True, env=env,
    )
    return env


def validate_revision(repo, rev):
    proc = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--verify", "--quiet",
         "%s^{commit}" % rev],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise CouldNotEvaluate("revision %r is not a commit in %s" % (rev, repo))


def run(repo, base, head, gate, as_json):
    validate_revision(repo, base)
    validate_revision(repo, head)

    with tempfile.TemporaryDirectory(prefix="finding-delta.") as tmp:
        tmp = Path(tmp)
        btree = extract(repo, base, tmp / "base")
        htree = extract(repo, head, tmp / "head")
        benv = revision_env(repo, base, tmp / "base.index", btree)
        henv = revision_env(repo, head, tmp / "head.index", htree)
        bset, bcode = findings(btree, gate, benv)
        hset, hcode = findings(htree, gate, henv)
    new, resolved = delta(bset, hset)
    if as_json:
        print(json.dumps({
            "base": {"rev": base, "drift": bset, "exit": bcode},
            "head": {"rev": head, "drift": hset, "exit": hcode},
            "new": new, "resolved": resolved,
        }, indent=1, sort_keys=True))
        return 1 if new else 0
    print(f"gate finding delta {base} -> {head}: base drift {len(bset)}, head drift {len(hset)}")
    print(f"  new: {', '.join(new) if new else 'none'}")
    print(f"  resolved: {', '.join(resolved) if resolved else 'none'}")
    print(f"finding delta: new {len(new)}, resolved {len(resolved)}")
    return 1 if new else 0


def self_test():
    failures = []
    assertions = 0

    def eq(label, got, want):
        nonlocal assertions
        assertions += 1
        if got != want:
            failures.append(f"{label}: got {got!r}, want {want!r}")

    eq("delta/identical", delta(["a", "b"], ["a", "b"]), ([], []))
    eq("delta/new", delta(["a"], ["a", "b"]), (["b"], []))
    eq("delta/resolved", delta(["a", "b"], ["b"]), ([], ["a"]))
    eq("delta/mixed", delta(["a", "b"], ["b", "c"]), (["c"], ["a"]))
    eq("delta/empty-base", delta([], []), ([], []))

    # exit-code arm over two synthetic trees whose stub gate prints a fixed set
    with tempfile.TemporaryDirectory(prefix="finding-delta-selftest.") as tmp:
        root = Path(tmp)
        for name, ids in (("base", ["a"]), ("head", ["a", "b"]), ("same", ["a"])):
            tree = root / name
            (tree / "verifiers").mkdir(parents=True)
            (tree / "verifiers/gate.py").write_text(
                "import json, sys\n"
                f"print(json.dumps({{'results': [{{'check': i, 'verdict': 'DRIFT'}} for i in {ids!r}]\n"
                f"                     + [{{'check': 'ok', 'verdict': 'PASS'}}]}}))\n"
                "sys.exit(1)\n"
            )
        stub = Path("verifiers/gate.py")

        def stub_findings(tree):
            return findings(tree, stub)

        eq("arm/new-finding-red", delta(stub_findings(root / "base")[0], stub_findings(root / "head")[0]),
           (["b"], []))
        eq("arm/no-new-finding", delta(stub_findings(root / "base")[0], stub_findings(root / "same")[0]),
           ([], []))
        red_exit = 1 if delta(stub_findings(root / "base")[0], stub_findings(root / "head")[0])[0] else 0
        green_exit = 1 if delta(stub_findings(root / "base")[0], stub_findings(root / "same")[0])[0] else 0
        eq("arm/exit-red", red_exit, 1)
        eq("arm/exit-green", green_exit, 0)

    repo = Path(__file__).resolve().parent.parent
    script = Path(__file__).resolve()
    test_env = dict(os.environ)
    for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE"):
        test_env.pop(key, None)
    unknown = "0" * 40
    for label, base, head in (
        ("arm/unknown-base-revision", unknown, "HEAD"),
        ("arm/unknown-head-revision", "HEAD", unknown),
    ):
        proc = subprocess.run(
            [PY, "-B", str(script), "--repo", str(repo),
             "--base", base, "--head", head],
            cwd=repo, env=test_env, capture_output=True, text=True, timeout=30,
        )
        eq(label, (proc.returncode, proc.stderr.startswith("could-not-evaluate: ")),
           (2, True))

    with tempfile.TemporaryDirectory(prefix="finding-delta-nogit.") as tmp:
        nogit = Path(tmp)
        (nogit / "python3").symlink_to(PY)
        no_git_env = dict(test_env, PATH=str(nogit))
        proc = subprocess.run(
            [PY, "-B", str(script), "--repo", str(repo),
             "--base", "HEAD", "--head", "HEAD"],
            cwd=repo, env=no_git_env, capture_output=True, text=True, timeout=30,
        )
        eq("arm/git-unavailable",
           (proc.returncode, proc.stderr.startswith("could-not-evaluate: ")),
           (2, True))

    print(f"self-test: {len(failures)} failure(s) over {assertions} assertions")
    for failure in failures:
        print(f"FAIL {failure}")
    return 1 if failures else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=False, default=".")
    ap.add_argument("--base")
    ap.add_argument("--head")
    ap.add_argument("--gate", default="verifiers/verify_corpus_integrity.py")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if not args.base or not args.head:
        ap.error("--base and --head are required")
    try:
        return run(Path(args.repo).resolve(), args.base, args.head,
                   Path(args.gate), args.json)
    except (CouldNotEvaluate, OSError, subprocess.CalledProcessError) as e:
        print(f"could-not-evaluate: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
