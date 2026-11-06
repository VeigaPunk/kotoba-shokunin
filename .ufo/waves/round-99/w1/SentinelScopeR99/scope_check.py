#!/usr/bin/env python3
"""SentinelScopeR99 scope checker: production bytes of verify_dispatch_prompts.py
must be unchanged outside self_test() and its self-test-only helpers/constants.

Usage: scope_check.py BASE_REPO BASE_REV CAND_REPO CAND_REV
Exit 0 = scope holds, 1 = violation, 2 = could-not-evaluate.
"""
import ast
import subprocess
import sys

TARGET = "verifiers/verify_dispatch_prompts.py"


def show(repo, rev, path):
    p = subprocess.run(["git", "-C", repo, "show", "%s:%s" % (rev, path)],
                       capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit("could-not-evaluate: %s:%s: %s" % (rev, path, p.stderr.strip()))
    return p.stdout


def top_map(src):
    tree = ast.parse(src)
    named = {}
    unnamed = []
    for node in tree.body:
        name = None
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            name = node.name
        elif isinstance(node, ast.Assign):
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name = node.target.id
        if name is None:
            unnamed.append(node)
        else:
            named[name] = node
    return tree, named, unnamed


def refs(node):
    out = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            out.add(n.id)
    return out


def reach(named, roots, stop=()):
    """Names reachable from roots; `stop` nodes are visited but not expanded."""
    seen = set()
    stack = [r for r in roots if r in named]
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        if cur in stop:
            continue
        for r in refs(named[cur]):
            if r in named and r not in seen:
                stack.append(r)
    return seen


def seg(src, node):
    return ast.get_source_segment(src, node)


def main():
    if sys.argv[1] == "--pair":
        if len(sys.argv) != 4:
            print(__doc__)
            return 2
        bsrc = open(sys.argv[2], encoding="utf-8").read()
        csrc = open(sys.argv[3], encoding="utf-8").read()
    else:
        if len(sys.argv) != 5:
            print(__doc__)
            return 2
        brepo, brev, crepo, crev = sys.argv[1:]
        bsrc = show(brepo, brev, TARGET)
        csrc = show(crepo, crev, TARGET)
    if bsrc == csrc:
        print("PRODUCTION-IDENTICAL (whole file byte-identical)")
        return 0
    btree, bnamed, bunnamed = top_map(bsrc)
    ctree, cnamed, cunnamed = top_map(csrc)
    if "self_test" not in bnamed or "self_test" not in cnamed:
        print("could-not-evaluate: no self_test()")
        return 2
    bself = reach(bnamed, ["self_test"])
    cself = reach(cnamed, ["self_test"])
    # self_test() is called from main(), so it is reachable from production;
    # it is nevertheless the one function the seat owns.  Treat it as a leaf
    # when computing production reachability and exempt it from the byte check.
    bprod_roots = set(bnamed) - bself
    cprod_roots = set(cnamed) - cself
    bprod = reach(bnamed, bprod_roots, stop={"self_test"})
    cprod = reach(cnamed, cprod_roots, stop={"self_test"})
    bad = []
    # unnamed top-level statements (docstring, imports, if-main) must be identical
    if len(bunnamed) != len(cunnamed):
        bad.append("unnamed top-level statement count %d -> %d" % (len(bunnamed), len(cunnamed)))
    else:
        for i, (b, c) in enumerate(zip(bunnamed, cunnamed)):
            if seg(bsrc, b) != seg(csrc, c):
                bad.append("unnamed top-level statement #%d changed: %r" % (i, seg(csrc, c)[:80]))
    # every production-reachable named node must be byte-identical
    for name in sorted(bprod - {"self_test"}):
        if name not in cnamed:
            bad.append("production node removed: %s" % name)
            continue
        if seg(bsrc, bnamed[name]) != seg(csrc, cnamed[name]):
            bad.append("production node changed: %s" % name)
    # nodes removed from the candidate: only self-test-only ones may go
    for name in sorted(set(bnamed) - set(cnamed)):
        if name in bprod and name != "self_test":
            bad.append("production node removed: %s" % name)
        else:
            print("note: self-test-only node removed: %s" % name)
    # nodes added: only self-test-only ones may appear
    for name in sorted(set(cnamed) - set(bnamed)):
        if name in cprod:
            bad.append("production node added: %s" % name)
        else:
            print("note: self-test-only node added: %s" % name)
    # a node that was self-test-only and is now production-reachable is a change
    for name in sorted(set(bnamed) & set(cnamed)):
        if name not in bprod and name in cprod:
            bad.append("self-test-only node became production-reachable: %s" % name)
    print("base self-test-only nodes: %d; production-reachable nodes: %d" % (len(bself), len(bprod)))
    print("cand self-test-only nodes: %d; production-reachable nodes: %d" % (len(cself), len(cprod)))
    if bad:
        for b in bad:
            print("SCOPE-VIOLATION %s" % b)
        return 1
    print("PRODUCTION-IDENTICAL outside self_test() and its self-test-only helpers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
