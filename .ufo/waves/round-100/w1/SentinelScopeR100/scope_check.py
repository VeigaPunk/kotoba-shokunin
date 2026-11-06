#!/usr/bin/env python3
"""SentinelScopeR100 independent scope checker (round 100).

Usage: python3 -B scope_check.py REPO BASE CAND
Reads only committed blobs via `git -C REPO show REV:path` (read-only).
Prints one line per check: PASS/FAIL <check>: <detail>. Exit 0 iff all PASS.
"""
from __future__ import annotations

import ast
import difflib
import hashlib
import subprocess
import sys

ALLOWED = {
    "corpus/SOURCES.md",
    "corpus/lessons/round-100.md",
    "verifiers/verify_skill_checklist.py",
    "verifiers/check_tip_battery.py",
    "verifiers/verify_dispatch_prompts.py",
}
RETIRED_STALE = "corpus/lessons/round-80-verifier-spotcheck.md:30,37"
BASE_LINE = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?$", tok)\n'
FIX_LINE = '    m = re.match(r"^(.+\\.\\w+):\\d+(-\\d+)?(,\\d+(-\\d+)?)*$", tok)\n'

fails: list[str] = []


def run(*args: str) -> str:
    p = subprocess.run(args, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("%s -> rc %d: %s" % (" ".join(args), p.returncode, p.stderr.strip()))
    return p.stdout


def show(repo: str, rev: str, path: str) -> bytes | None:
    p = subprocess.run(["git", "-C", repo, "show", "%s:%s" % (rev, path)],
                       capture_output=True)
    return p.stdout if p.returncode == 0 else None


def report(ok: bool, name: str, detail: str) -> None:
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)
    if not ok:
        fails.append(name)


def text_of(repo: str, rev: str, path: str) -> str:
    raw = show(repo, rev, path)
    if raw is None:
        raise RuntimeError("absent at %s: %s" % (rev, path))
    return raw.decode("utf-8")


def func_span(src: str, name: str) -> tuple[int, int]:
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return node.lineno, node.end_lineno
    raise RuntimeError("no top-level def %s" % name)


def assign_span(src: str, name: str) -> tuple[int, int]:
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return node.lineno, node.end_lineno
    raise RuntimeError("no top-level assignment %s" % name)


def outside(src: str, span: tuple[int, int]) -> str:
    lines = src.splitlines(keepends=True)
    a, b = span
    return "".join(lines[: a - 1]) + "".join(lines[b:])


def main() -> int:
    repo, base, cand = sys.argv[1], sys.argv[2], sys.argv[3]

    # A. changed file set
    ns = run("git", "-C", repo, "diff", "--name-status", base, cand)
    changed = [ln.split("\t", 1) for ln in ns.splitlines() if ln.strip()]
    names = {c[1] for c in changed}
    extra = sorted(names - ALLOWED)
    missing = sorted(ALLOWED - names)
    report(not extra and not missing, "changed-set",
           "changed=%s extra=%s missing=%s" % (sorted(names), extra, missing))

    # B. frozen files byte-identical
    frozen = ["SKILL.md", "verifiers/verify_corpus_integrity.py",
              "verifiers/verify_corpus_independent.py", "verifiers/floors-registry.json",
              "verifiers/corpus-baseline.json"]
    spot = [n for n in names if "verifier-spotcheck" in n or n.startswith("verifiers/fixtures/")]
    same = []
    for path in frozen:
        a, b = show(repo, base, path), show(repo, cand, path)
        same.append((path, a is not None and a == b))
    report(all(ok for _, ok in same) and not spot, "frozen-bytes",
           "identical=%s; spotcheck/fixture touched=%s" % ([p for p, ok in same if ok], spot))

    # C. dispatch prompts: production code outside self_test() byte-identical, insert-only inside
    dp_base = text_of(repo, base, "verifiers/verify_dispatch_prompts.py")
    dp_cand = text_of(repo, cand, "verifiers/verify_dispatch_prompts.py")
    span_b = func_span(dp_base, "self_test")
    span_c = func_span(dp_cand, "self_test")
    prod_same = outside(dp_base, span_b) == outside(dp_cand, span_c)
    body_b = "".join(dp_base.splitlines(keepends=True)[span_b[0] - 1: span_b[1]])
    body_c = "".join(dp_cand.splitlines(keepends=True)[span_c[0] - 1: span_c[1]])
    ops = difflib.SequenceMatcher(a=body_b.splitlines(), b=body_c.splitlines(),
                                  autojunk=False).get_opcodes()
    bad = [op for op in ops if op[0] in ("delete", "replace")]
    report(prod_same and not bad, "dispatch-production",
           "outside self_test identical=%s; self_test ops=%s; non-insert opcodes=%s"
           % (prod_same, sorted({op[0] for op in ops}), bad[:4]))

    # D. checklist: fix line, self_test body, one corrections row
    ck_base = text_of(repo, base, "verifiers/verify_skill_checklist.py")
    ck_cand = text_of(repo, cand, "verifiers/verify_skill_checklist.py")
    report(ck_cand.count(FIX_LINE) == 1 and ck_cand.count(BASE_LINE) == 0,
           "checklist-fixline",
           "FIX_LINE occurrences=%d BASE_LINE occurrences=%d"
           % (ck_cand.count(FIX_LINE), ck_cand.count(BASE_LINE)))
    cb, cc = func_span(ck_base, "self_test"), func_span(ck_cand, "self_test")
    ab, ac = assign_span(ck_base, "GOVERNANCE_CORRECTIONS"), assign_span(ck_cand, "GOVERNANCE_CORRECTIONS")

    def normalize(src: str, fspan: tuple[int, int], aspan: tuple[int, int]) -> str:
        lines = src.splitlines(keepends=True)
        keep = []
        for i, ln in enumerate(lines, 1):
            if fspan[0] <= i <= fspan[1]:
                continue
            if aspan[0] <= i <= aspan[1]:
                continue
            keep.append(ln)
        return "".join(keep).replace(BASE_LINE, FIX_LINE)

    norm_same = normalize(ck_base, cb, ab) == normalize(ck_cand, cc, ac)
    rows_b = ast.literal_eval("".join(ck_base.splitlines(keepends=True)[ab[0] - 1: ab[1]]).split("=", 1)[1])
    rows_c = ast.literal_eval("".join(ck_cand.splitlines(keepends=True)[ac[0] - 1: ac[1]]).split("=", 1)[1])
    removed = [r for r in rows_b if r not in rows_c]
    added = [r for r in rows_c if r not in rows_b]
    row_ok = (len(removed) == 1 and not added
              and RETIRED_STALE in removed[0])
    report(norm_same and row_ok, "checklist-confined",
           "normalized identical=%s; rows base=%d cand=%d removed=%s added=%s"
           % (norm_same, len(rows_b), len(rows_c), removed, added))

    # E. battery: identical outside INSTRUMENT_PINS
    tb_base = text_of(repo, base, "verifiers/check_tip_battery.py")
    tb_cand = text_of(repo, cand, "verifiers/check_tip_battery.py")
    pin_b = assign_span(tb_base, "INSTRUMENT_PINS")
    pin_c = assign_span(tb_cand, "INSTRUMENT_PINS")
    report(outside(tb_base, pin_b) == outside(tb_cand, pin_c), "battery-pins-only",
           "outside INSTRUMENT_PINS identical=%s"
           % (outside(tb_base, pin_b) == outside(tb_cand, pin_c)))

    # F. SOURCES.md append-only rows S282-S285 (pure-addition diff, table rows)
    src_base = text_of(repo, base, "corpus/SOURCES.md")
    src_cand = text_of(repo, cand, "corpus/SOURCES.md")
    sd = run("git", "-C", repo, "diff", "--unified=0", base, cand, "--", "corpus/SOURCES.md")
    s_add = [ln[1:] for ln in sd.splitlines()
             if ln.startswith("+") and not ln.startswith("+++")]
    s_del = [ln for ln in sd.splitlines()
             if ln.startswith("-") and not ln.startswith("---")]
    ids = [r.split("|")[1].strip() if r.count("|") >= 2 else "" for r in s_add]
    rows_ok = all(r.startswith("| ") and r.count("|") == 12 for r in s_add)
    # the four rows sit inside the registry table: the next non-blank candidate
    # line after the block is the "## Paths" heading
    cl = src_cand.splitlines()
    last = max(i for i, ln in enumerate(cl) if ln in s_add) if s_add else -1
    nxt = next((ln for ln in cl[last + 1:] if ln.strip()), "")
    report(not s_del and ids == ["S282", "S283", "S284", "S285"] and rows_ok
           and nxt.startswith("## "),
           "sources-append",
           "deleted lines=%d added=%d ids=%s 13-column rows=%s next=%r"
           % (len(s_del), len(s_add), ids, rows_ok, nxt))

    # G. round-100 lesson is new
    report(show(repo, base, "corpus/lessons/round-100.md") is None
           and show(repo, cand, "corpus/lessons/round-100.md") is not None,
           "lesson-new", "absent at base, present at candidate")

    print("SCOPE %s" % ("PASS" if not fails else "FAIL " + ",".join(fails)))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
