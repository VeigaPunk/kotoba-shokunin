#!/usr/bin/env python3
"""Round-88 counter for the five round-86 routed defects (C2, D5 v2).

Frozen predicate (plans/round-88.md § C2, carried verbatim):

    python3 -B verifiers/check_r86_routed_repairs_v2.py --rev <rev>
        -> prints "r86 routed defects closed N of 5", exit 0 iff N == 5;
           exit 1 otherwise; exit 2 = could-not-evaluate.

D1-D4 are the round-87 counter's items, reused unchanged: this file imports
`verifiers/check_r86_routed_repairs.py` (byte-frozen) and calls its
`check_d1`..`check_d4`, which read `<rev>`'s committed bytes only.

D5 (v2) replaces the round-87 exact-red-set conjunct, which healed external red
falsified (R87-D8). It holds iff BOTH, each measured in a scratch clone of the
lane (the lane tree is never the scored instrument):

  (i)  identity: `verifiers/verify_corpus_integrity.py --json` at <rev> and at
       BASE_REV list the same SET of check names, nine names at both. A removed
       or silenced check fails (i).
  (ii) monotone: the names whose verdict is DRIFT at <rev> are a SUBSET of the
       names DRIFT at BASE_REV. A new DRIFT name fails (ii); a healed one passes.

Honest bound (plans/round-88.md): (ii) is evaluated on names, so a new instance
of a name that is already DRIFT at BASE_REV is not visible to it.

Usage: check_r86_routed_repairs_v2.py --rev REV [--repo DIR] [--work DIR]
       check_r86_routed_repairs_v2.py --self-test
Exit 0 clean (5 of 5), 1 a check fails, 2 could not evaluate.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import check_r86_routed_repairs as r87  # noqa: E402  frozen round-87 counter (D1-D4)

LANE = r87.LANE
TARGET = 5
BASE_REV = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
INTEGRITY = "verifiers/verify_corpus_integrity.py"
NAME_COUNT = 9
GIT_TIMEOUT = 300
Unevaluable = r87.Unevaluable


# --- scratch trees ---------------------------------------------------------

def scratch_tree(repo: Path, rev: str, work: Path, label: str) -> Path:
    """Scratch clone of `repo` checked out detached at `rev`. The lane is read only."""
    box = Path(tempfile.mkdtemp(prefix="tree-%s-" % label, dir=str(work)))
    tree = box / "tree"
    proc = r87._git(repo.resolve(), "clone", "-q", "--shared",
                    str(repo.resolve()), str(tree))
    if proc.returncode != 0:
        raise Unevaluable("clone for %s: %s" % (label, proc.stderr.strip()[-200:]))
    top = r87._git(tree, "rev-parse", "--show-toplevel")
    if top.returncode != 0 or Path(top.stdout.strip()).resolve() != tree.resolve():
        raise Unevaluable("scratch clone %s is not its own toplevel" % tree)
    proc = r87._git(tree, "checkout", "-q", "--detach", rev)
    if proc.returncode != 0:
        raise Unevaluable("checkout %s in %s: %s"
                          % (rev[:12], label, proc.stderr.strip()[-200:]))
    return tree


# --- integrity reading -----------------------------------------------------

def integrity_names(tree: Path) -> tuple[list[str], list[str]]:
    """(all check names, DRIFT check names) of the tree's own integrity gate."""
    script = tree / INTEGRITY
    if not script.is_file():
        raise Unevaluable("%s absent in %s" % (INTEGRITY, tree.name))
    try:
        run = subprocess.run([sys.executable, "-B", INTEGRITY, "--json"],
                             cwd=str(tree), capture_output=True, text=True,
                             timeout=GIT_TIMEOUT)
    except (OSError, subprocess.SubprocessError) as exc:
        raise Unevaluable("integrity run in %s failed: %s" % (tree.name, exc)) from exc
    if run.returncode not in (0, 1):
        raise Unevaluable("%s exit=%d in %s: %s"
                          % (INTEGRITY, run.returncode, tree.name,
                             (run.stdout + run.stderr).strip()[-200:]))
    try:
        doc = json.loads(run.stdout)
    except ValueError as exc:
        raise Unevaluable("%s --json did not parse in %s: %s"
                          % (INTEGRITY, tree.name, exc)) from exc
    results = doc.get("results") if isinstance(doc, dict) else None
    if not isinstance(results, list) or not results:
        raise Unevaluable("%s --json carries no results in %s" % (INTEGRITY, tree.name))
    names: list[str] = []
    drift: list[str] = []
    for row in results:
        name = row.get("check") if isinstance(row, dict) else None
        verdict = row.get("verdict") if isinstance(row, dict) else None
        if not isinstance(name, str) or verdict not in ("PASS", "DRIFT"):
            raise Unevaluable("%s row %r verdict %r is not PASS or DRIFT"
                              % (INTEGRITY, name, verdict))
        names.append(name)
        if verdict == "DRIFT":
            drift.append(name)
    if len(set(names)) != len(names):
        raise Unevaluable("%s in %s repeats a check name" % (INTEGRITY, tree.name))
    return sorted(names), sorted(drift)


# --- D5 (v2) ---------------------------------------------------------------

def identity_holds(names_rev: list[str], names_base: list[str]) -> bool:
    """(i): the same set of names at both revisions, nine names at the base."""
    return set(names_rev) == set(names_base) and len(set(names_base)) == NAME_COUNT


def monotone_holds(drift_rev: list[str], drift_base: list[str]) -> bool:
    """(ii): DRIFT names at <rev> are a subset of DRIFT names at the base."""
    return set(drift_rev) <= set(drift_base)


def d5_measure(repo: Path, rev: str, base_rev: str, work: Path) -> dict:
    base_tree = scratch_tree(repo, base_rev, work, "base")
    rev_tree = scratch_tree(repo, rev, work, "rev")
    names_base, drift_base = integrity_names(base_tree)
    names_rev, drift_rev = integrity_names(rev_tree)
    return {"names_base": names_base, "drift_base": drift_base,
            "names_rev": names_rev, "drift_rev": drift_rev}


def d5_verdict(m: dict) -> tuple[bool, bool, str]:
    """(identity, monotone, detail) from one measurement."""
    ident = identity_holds(m["names_rev"], m["names_base"])
    mono = monotone_holds(m["drift_rev"], m["drift_base"])
    bits = []
    if ident:
        bits.append("identity: %d names equal at base and rev" % len(m["names_rev"]))
    else:
        missing = sorted(set(m["names_base"]) - set(m["names_rev"]))
        extra = sorted(set(m["names_rev"]) - set(m["names_base"]))
        bits.append("identity FAIL: rev has %d names, base has %d; missing %s, extra %s"
                    % (len(m["names_rev"]), len(m["names_base"]), missing, extra))
    if mono:
        bits.append("monotone: DRIFT at rev %s is a subset of base %s"
                    % (m["drift_rev"], m["drift_base"]))
    else:
        new = sorted(set(m["drift_rev"]) - set(m["drift_base"]))
        bits.append("monotone FAIL: DRIFT at rev not at base: %s" % new)
    return ident, mono, "; ".join(bits)


def check_d5(repo: Path, rev: str, work: Path, landing: str,
             validator: Path, base_rev: str) -> tuple[bool, str]:
    del landing, validator
    m = d5_measure(repo, rev, base_rev, work)
    ident, mono, detail = d5_verdict(m)
    return ident and mono, detail


# --- driver ----------------------------------------------------------------

ITEMS = (("d1", r87.check_d1), ("d2", r87.check_d2), ("d3", r87.check_d3),
         ("d4", r87.check_d4), ("d5", check_d5))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", help="lane revision to check")
    ap.add_argument("--repo", default=str(LANE), help="lane repository")
    ap.add_argument("--work", help="scratch parent directory (default: $TMPDIR)")
    ap.add_argument("--self-test", action="store_true", help="run the fixture self-test")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.rev:
        ap.error("--rev is required unless --self-test is selected")

    repo = Path(args.repo)
    if not repo.is_dir():
        print("could-not-evaluate: repo not found: %s" % repo, file=sys.stderr)
        return 2
    parent = (Path(args.work) if args.work
              else Path(os.environ.get("TMPDIR") or tempfile.gettempdir()))
    try:
        parent.mkdir(parents=True, exist_ok=True)
        work = Path(tempfile.mkdtemp(prefix="r88-routed-v2-", dir=str(parent)))
    except OSError as exc:
        print("could-not-evaluate: scratch dir: %s" % exc, file=sys.stderr)
        return 2

    rows: list[tuple[str, bool, str]] = []
    try:
        rev = r87._resolve(repo, args.rev)
        for cid, check in ITEMS:
            ok, detail = check(repo, rev, work, r87.LANDING_REV,
                               r87.OMP_VALIDATOR, BASE_REV)
            rows.append((cid, ok, detail))
    except Unevaluable as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2
    finally:
        shutil.rmtree(work, ignore_errors=True)

    for cid, ok, detail in rows:
        print("%s %-3s %s" % ("PASS" if ok else "FAIL", cid, detail))
    score = sum(1 for _cid, ok, _detail in rows if ok)
    print("r86 routed defects closed %d of %d" % (score, TARGET))
    return 0 if score == TARGET else 1


# --- self-test -------------------------------------------------------------

NINE_NAMES = (
    "corpus.index.tracked_files",
    "corpus.index.unindexed",
    "corpus.index.stale_patterns",
    "corpus.index.missing_paths",
    "corpus.pointers.report_total",
    "corpus.pointers.report_dead",
    "corpus.pointers.commit_total",
    "corpus.pointers.commit_unresolvable",
    "corpus.pointers.commit_nonhash",
)
BASE_DRIFT = (
    "corpus.index.tracked_files",
    "corpus.index.unindexed",
    "corpus.pointers.report_total",
    "corpus.pointers.report_dead",
    "corpus.pointers.commit_total",
    "corpus.pointers.commit_unresolvable",
)

# A fixture integrity gate with the --json shape of verify_corpus_integrity.py.
# The committed MODE file selects the world, so a world changes the gate's
# verdicts or its check list without changing any other part of the fixture.
FIXTURE_INTEGRITY = """#!/usr/bin/env python3
\"\"\"fixture integrity gate: the --json shape of verify_corpus_integrity.py.\"\"\"
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODE = (ROOT / "MODE").read_text().strip()
NAMES = %(names)r
DRIFT = set(%(drift)r)
if MODE == "healed":
    DRIFT.discard("corpus.pointers.report_dead")
if MODE == "silenced":
    NAMES.remove("corpus.pointers.commit_unresolvable")
    DRIFT.discard("corpus.pointers.commit_unresolvable")
if MODE == "newname":
    DRIFT.add("corpus.pointers.commit_nonhash")
if MODE == "garbage":
    print("no json here")
    raise SystemExit(0)
rows = [{"check": n, "mode": "zero", "observed": int(n in DRIFT),
         "verdict": "DRIFT" if n in DRIFT else "PASS"} for n in NAMES]
print(json.dumps({"observed": {"corpus": {}}, "results": rows}, indent=2))
raise SystemExit(1 if DRIFT else 0)
""" % {"names": list(NINE_NAMES), "drift": list(BASE_DRIFT)}


def _git_fixture(repo: Path, *args: str) -> str:
    proc = r87._git(repo, *args)
    if proc.returncode != 0:
        raise RuntimeError("fixture git %s: %s" % (args[0], proc.stderr.strip()[-200:]))
    return proc.stdout.strip()


def _fixture_world(repo: Path, message: str, mode: str,
                   extra: dict[str, str] | None = None) -> str:
    files = {INTEGRITY: FIXTURE_INTEGRITY, "MODE": mode + "\n"}
    files.update(extra or {})
    for rel, body in files.items():
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    _git_fixture(repo, "add", "-A")
    _git_fixture(repo, "-c", "user.name=probe", "-c",
                 "user.email=probe@example.invalid", "commit", "-q", "--allow-empty",
                 "-m", message)
    return _git_fixture(repo, "rev-parse", "HEAD")


def self_test() -> int:
    failures: list[str] = []
    assertions = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        nonlocal assertions
        assertions += 1
        if not ok:
            failures.append("%s%s" % (label, (": " + detail) if detail else ""))

    # --- (i) and (ii) as pure functions -----------------------------------
    check("arm (i) identity: equal nine-name sets at both revisions hold",
          identity_holds(list(NINE_NAMES), list(NINE_NAMES)))
    check("arm (i) identity: a silenced check (eight names) fails identity",
          not identity_holds(list(NINE_NAMES[:-1]), list(NINE_NAMES)))
    check("arm (i) identity: a renamed check fails identity",
          not identity_holds(list(NINE_NAMES[:-1]) + ["corpus.pointers.renamed"],
                             list(NINE_NAMES)))
    check("arm (ii) monotone: a DRIFT set equal to the base's holds",
          monotone_holds(list(BASE_DRIFT), list(BASE_DRIFT)))
    check("arm (ii) monotone: a strict subset (healed reds) holds",
          monotone_holds(list(BASE_DRIFT[1:]), list(BASE_DRIFT)))
    check("arm (ii) monotone: a new DRIFT name fails",
          not monotone_holds(list(BASE_DRIFT) + ["corpus.pointers.commit_nonhash"],
                             list(BASE_DRIFT)))

    with tempfile.TemporaryDirectory(prefix="r88-routed-v2-fixture-") as tdir:
        root = Path(tdir)
        work = root / "work"
        work.mkdir()
        repo = root / "lane"
        repo.mkdir()
        _git_fixture(repo, "init", "-q")

        base = _fixture_world(repo, "base world", "base")
        # the landing-shaped tip: in scratch clones it reads the base set
        tip = _fixture_world(repo, "tip world", "base")
        healed = _fixture_world(repo, "healed world", "healed")
        added = _fixture_world(repo, "added red world", "added", {
            "corpus/lessons/new-line.md": "commit `0123456789abcdef0123456789abcdef01234567`\n",
        })
        silenced = _fixture_world(repo, "silenced world", "silenced")
        newname = _fixture_world(repo, "new name world", "newname")
        garbage = _fixture_world(repo, "garbage world", "garbage")

        def measure(rev: str) -> dict:
            return d5_measure(repo, rev, base, work)

        m_tip = measure(tip)
        ident, mono, _detail = d5_verdict(m_tip)
        check("arm w_tip: the landing-shaped world passes D5 (i) and (ii)",
              ident and mono, _detail)

        m_healed = measure(healed)
        ident, mono, detail = d5_verdict(m_healed)
        check("arm w_healed: the base with its one report_dead red fixed passes D5",
              ident and mono, detail)

        m_added = measure(added)
        ident, mono, detail = d5_verdict(m_added)
        check("arm w_added_red (frozen control): an added unresolvable commit "
              "citation expects D5 FAIL via (ii); the names-set reads it as PASS "
              "(counter defect, see ExecMonotoneD5.md)",
              not mono, detail)
        check("arm w_added_red: identity still holds on the added-red world",
              ident, detail)

        m_sil = measure(silenced)
        ident, mono, detail = d5_verdict(m_sil)
        check("arm w_silenced: one removed integrity check fails D5 via (i)",
              not ident and "identity FAIL" in detail, detail)
        check("arm w_silenced monotone-only: (ii) alone reads PASS, which is why (i) exists",
              mono, detail)

        m_new = measure(newname)
        ident, mono, detail = d5_verdict(m_new)
        check("arm w_newname (supplementary): a DRIFT name absent at the base fails via (ii)",
              not mono and ident, detail)

        try:
            garbage_tree = scratch_tree(repo, garbage, work, "garbage")
            integrity_names(garbage_tree)
            check("arm w_garbage: a run without JSON is could-not-evaluate, never a pass",
                  False, "integrity_names returned without raising")
        except Unevaluable as exc:
            check("arm w_garbage: a run without JSON is could-not-evaluate, never a pass",
                  "did not parse" in str(exc), str(exc))

        try:
            check_d5(repo, "0" * 40, work, "", Path("/nonexistent"), base)
            check("arm w_unresolvable: an unresolvable revision is could-not-evaluate",
                  False, "check_d5 returned without raising")
        except Unevaluable as exc:
            check("arm w_unresolvable: an unresolvable revision is could-not-evaluate",
                  "checkout" in str(exc) or "clone" in str(exc), str(exc))

        ok, detail = check_d5(repo, tip, work, "", Path("/nonexistent"), base)
        check("arm w_tip via check_d5: the D5 item reports PASS on the landing-shaped world",
              ok, detail)

    print("%d failure(s) over %d assertions" % (len(failures), assertions))
    for failure in failures:
        print("FAIL", failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
