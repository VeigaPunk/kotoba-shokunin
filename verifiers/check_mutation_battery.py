#!/usr/bin/env python3
"""Mutation battery over the round-89 gate instruments at one revision (round-90 C1).

Frozen predicate (plans/round-90.md § C1; the same sentence is the receipt line):
`python3 -B verifiers/check_mutation_battery.py --rev <rev> --work <dir>` prints
`mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors S of S`
and exits 0 iff K == M and E == E and S == S_declared and guards G1-G3 PASS, where M, E and
S_declared are the class counts of the committed manifest
`verifiers/fixtures/mutation-battery/manifest.tsv` (classes kill, equivalent, survivor).

Method. The revision is materialised as a scratch clone of the lane (<work>/fleet/<lane>),
checked out detached at <rev>; the lane itself is only read. Each target's probes run unmodified
first: that observation is the baseline. A kill or survivor row applies its anchored regex edits
to the revision bytes and is killed when any probe's exit code or result-bearing output differs
from the baseline. An equivalent row applies one generated semantics-preserving rewrite to every
eligible site of its target (a comment before each top-level statement, a marker in each docstring,
trailing whitespace on code lines outside strings) and survives only if every probe stays identical.
Output lines that carry run-specific tokens (scratch paths, 12+ hex digits) are excluded from the
observation; exit codes are always compared.

Guards. G1 revision identity: --rev is a full commit of the lane, the scratch clone is detached at
--rev with a clean tree, and every target and the manifest are read through `git show <rev>:<path>`,
never the working tree. G2 copy integrity: each revision copy and each mutant is read back from
disk and its sha256 must equal the sha256 recorded from the revision bytes. G3 registry presence:
`git show <rev>:SKILL.md` names check_mutation_battery.py on at least one line. --allow-unregistered
(a pre-registry opt-in, not part of the frozen predicate) reports G3 without letting it decide the exit.
Since round-91 C1 the probe set also covers the battery's own `--self-test`, whose G1 commit-check,
G1 clean-tree and G2 restore read-back self-test arms are the kill channel for the battery-guard
manifest rows (mb-m2, mb-m15, mb-m16).

Exit ladder: 0 pass, 1 content fail, 2 could-not-evaluate (a guard trips, an anchor no longer
matches the revision bytes, or a probe baseline does not hold). --self-test prints
`0 failure(s) over N assertions`.
Since round-92 C2(a) the self-test arm `kill-set-size` pins the kill-row count of the working-tree
manifest to KILL_SET_PINNED; a dropped or added kill row fails that arm by name.
"""
from __future__ import annotations

import argparse
import ast
import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tokenize
from dataclasses import dataclass
from pathlib import Path

MANIFEST = "verifiers/fixtures/mutation-battery/manifest.tsv"
SKILL = "SKILL.md"
BATTERY = "check_mutation_battery.py"
FG = "verifiers/check_freeze_gate.py"
D5 = "verifiers/check_r86_routed_repairs_v3.py"
BAT = "verifiers/check_mutation_battery.py"
SYMLINK_PROBE = ".ufo/reports/round-76/kotoba.md"   # the d5 gate's Q79 location-class probe
PROBE_TIMEOUT = 120
CLASSES = ("kill", "equivalent", "survivor")
HEADER = ("id", "target", "class", "recipe", "disposition")
EQ_KINDS = ("comment-insert", "docstring-reword", "trailing-whitespace")
COMMENT_MARK = "# battery-equivalence: comment-insert"
DOCSTRING_MARK = " [battery-reword]"
LINE_FMT = ("mutation battery killed %d of %d kill-set; equivalents survived %d of %d; "
            "disclosed survivors %d of %d")
# target -> ((label, argv, declared baseline exit or None), ...); the frozen probe set (§ C1;
# round-91 C1 adds the battery's own self-test as the third probe target)
PROBES = {
    FG: (("fg-self-test", ["--self-test"], 0),
         ("fg-fixed-plan", ["--plan", "verifiers/fixtures/freeze-gate/r88-controls-fixed.md"], 0),
         ("fg-unsat-plan", ["--plan", "verifiers/fixtures/freeze-gate/r88-controls.md"], 1)),
    D5: (("d5-self-test", ["--self-test"], None),
         ("d5-base-receipt", ["--base-receipt", ".ufo/waves/round-89/receipts/d5v3-base-receipt.json"], None)),
    BAT: (("bat-self-test", ["--self-test"], 0),),
}
# a probe output line carrying one of these is run-specific and is not part of the observation
RUN_SPECIFIC = re.compile(r"\b[0-9a-f]{12,}\b")

# the kill-set size pinned at the round-92 freeze: the kill rows of the committed manifest at
# e073723ae667b64e534f8621bddb83ad12ad0e71. The self-test arm kill-set-size compares the manifest's
# kill-row count to this literal, so a dropped kill row fails by name rather than only changing the
# count printed in the predicate line.
KILL_SET_PINNED = 17


class CouldNotEvaluate(Exception):
    """A guard tripped or the battery cannot measure (exit 2)."""


@dataclass(frozen=True)
class Row:
    rid: str
    target: str
    cls: str
    recipe: dict
    disposition: str


def clean_env(**extra: str) -> dict:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env.update(extra)
    return env


def git(repo: Path, *args: str) -> tuple[int, bytes]:
    p = subprocess.run(["git", "-C", str(repo), *args], env=clean_env(),
                       capture_output=True)
    return p.returncode, p.stdout


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def toplevel(path: Path) -> Path:
    rc, out = git(path, "rev-parse", "--show-toplevel")
    if rc != 0:
        raise CouldNotEvaluate("not inside a git worktree: %s" % path)
    return Path(out.decode().strip()).resolve()


def git_show(repo: Path, rev: str, path: str) -> bytes:
    rc, out = git(repo, "show", "%s:%s" % (rev, path))
    if rc != 0:
        raise CouldNotEvaluate("G1: git show %s:%s failed" % (rev, path))
    return out


def parse_manifest(text: str) -> list[Row]:
    lines = text.splitlines()
    if not lines or tuple(lines[0].split("\t")) != HEADER:
        raise CouldNotEvaluate("manifest header must be %s" % "\\t".join(HEADER))
    rows: list[Row] = []
    seen: set[str] = set()
    for lineno, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != len(HEADER):
            raise CouldNotEvaluate("manifest line %d: %d columns, expected %d"
                                   % (lineno, len(parts), len(HEADER)))
        rid, target, cls, recipe_text, disposition = parts
        if rid in seen:
            raise CouldNotEvaluate("manifest id %s is not unique" % rid)
        seen.add(rid)
        if cls not in CLASSES:
            raise CouldNotEvaluate("manifest %s: class %r not in %s" % (rid, cls, CLASSES))
        if target not in PROBES:
            raise CouldNotEvaluate("manifest %s: target %r has no probe set" % (rid, target))
        try:
            recipe = json.loads(recipe_text)
        except ValueError as exc:
            raise CouldNotEvaluate("manifest %s: recipe is not JSON (%s)" % (rid, exc))
        if cls == "equivalent":
            if recipe.get("op") != "rewrite" or recipe.get("kind") not in EQ_KINDS:
                raise CouldNotEvaluate("manifest %s: equivalent recipe must be a rewrite in %s"
                                       % (rid, EQ_KINDS))
        else:
            edits = recipe.get("edits")
            if recipe.get("op") != "replace" or not isinstance(edits, list) or not edits:
                raise CouldNotEvaluate("manifest %s: %s recipe must be replace with edits"
                                       % (rid, cls))
            for edit in edits:
                if not isinstance(edit, dict) or "anchor" not in edit or "with" not in edit:
                    raise CouldNotEvaluate("manifest %s: edit needs anchor and with" % rid)
        if cls == "survivor" and not disposition.strip():
            raise CouldNotEvaluate("manifest %s: survivor row needs a disposition" % rid)
        rows.append(Row(rid, target, cls, recipe, disposition))
    return rows


def kill_set_size(text: str) -> int:
    """The kill rows the battery derives from a manifest text, through the G1 parse path."""
    return sum(1 for row in parse_manifest(text) if row.cls == "kill")


def kill_set_check(text: str, pinned: int | None = None) -> tuple[bool, str]:
    """kill-set-size arm: the kill-row count must equal the pin (default KILL_SET_PINNED); malformed text is refused."""
    want = KILL_SET_PINNED if pinned is None else pinned
    try:
        n = kill_set_size(text)
    except CouldNotEvaluate as exc:
        return False, "manifest malformed: %s" % exc
    return n == want, "observed %d kill rows, pinned %d" % (n, want)


def apply_recipe(text: str, row: Row) -> str:
    out = text
    for k, edit in enumerate(row.recipe["edits"], 1):
        pattern = re.compile(edit["anchor"])
        want = int(edit.get("count", 1))
        found = len(pattern.findall(out))
        if found != want:
            raise CouldNotEvaluate("anchor miss: %s edit %d matches %d time(s) in the revision "
                                   "bytes, expected %d" % (row.rid, k, found, want))
        out = pattern.sub(lambda m, w=edit["with"]: w, out)
    return out


def _comment_insert(text: str) -> str:
    starts = set()
    for node in ast.parse(text).body:
        decorators = [d.lineno for d in getattr(node, "decorator_list", [])]
        starts.add(min(decorators + [node.lineno]))
    out = []
    for i, line in enumerate(text.split("\n"), 1):
        if i in starts:
            out.append(COMMENT_MARK)
        out.append(line)
    return "\n".join(out)


def _docstring_reword(text: str) -> str:
    tree = ast.parse(text)
    sites: set[tuple[int, int]] = set()

    def visit(node: ast.AST) -> None:
        body = getattr(node, "body", None)
        if (body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant)
                and isinstance(body[0].value.value, str)):
            sites.add((body[0].value.lineno, body[0].value.col_offset))

    visit(tree)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            visit(node)
    parts = text.split("\n")
    quote = re.compile(r'"""|\'\'\'|"|\'')
    for lineno, col in sorted(sites, reverse=True):
        line = parts[lineno - 1]
        start = len(line.encode("utf-8")[:col].decode("utf-8", "ignore"))
        m = quote.search(line, start)
        if m is None:
            raise CouldNotEvaluate("docstring at line %d has no opening quote" % lineno)
        parts[lineno - 1] = line[:m.end()] + DOCSTRING_MARK + line[m.end():]
    return "\n".join(parts)


def _trailing_whitespace(text: str) -> str:
    parts = text.split("\n")
    multi: set[int] = set()
    for tok in tokenize.generate_tokens(io.StringIO(text).readline):
        if tok.start[0] != tok.end[0]:
            multi.update(range(tok.start[0], tok.end[0] + 1))
    out = []
    for i, line in enumerate(parts, 1):
        if i in multi or line.endswith("\\") or (i == len(parts) and line == ""):
            out.append(line)
        else:
            out.append(line + "  ")
    return "\n".join(out)


def rewrite(text: str, kind: str) -> str:
    if kind == "comment-insert":
        return _comment_insert(text)
    if kind == "docstring-reword":
        return _docstring_reword(text)
    if kind == "trailing-whitespace":
        return _trailing_whitespace(text)
    raise CouldNotEvaluate("unknown rewrite kind %r" % kind)


def write_target(path: Path, data: bytes) -> None:
    path.write_bytes(data)


def place(path: Path, data: bytes, expect: str, label: str) -> None:
    """G2: write a copy, read it back, and require the recorded sha256."""
    write_target(path, data)
    got = sha256(path.read_bytes())
    if got != expect:
        raise CouldNotEvaluate("G2 copy integrity: %s on disk sha256 %s, recorded %s"
                               % (label, got[:12], expect[:12]))


def materialize(lane: Path, rev: str, work: Path) -> Path:
    """G1: a scratch clone of the lane detached at rev, in the lane's parent shape."""
    fleet = work / "fleet"
    dest = fleet / lane.name
    if dest.exists():
        shutil.rmtree(dest)
    fleet.mkdir(parents=True, exist_ok=True)
    report = lane.parent / SYMLINK_PROBE
    if report.is_file():
        link = fleet / SYMLINK_PROBE
        link.parent.mkdir(parents=True, exist_ok=True)
        if not os.path.lexists(link):
            link.symlink_to(report)
    rc, _ = git(fleet, "clone", "-q", "--shared", "--no-checkout", str(lane), str(dest))
    if rc != 0:
        raise CouldNotEvaluate("G1: cloning the lane into scratch failed")
    rc, _ = git(dest, "checkout", "-q", "--detach", rev)
    if rc != 0:
        raise CouldNotEvaluate("G1: checkout of %s in scratch failed" % rev)
    if toplevel(dest) != dest.resolve():
        raise CouldNotEvaluate("G1: scratch toplevel is not %s" % dest)
    rc, out = git(dest, "rev-parse", "HEAD")
    if rc != 0 or out.decode().strip() != rev:
        raise CouldNotEvaluate("G1: scratch HEAD is not --rev")
    rc, out = git(dest, "status", "--porcelain")
    if rc != 0 or out.strip():
        raise CouldNotEvaluate("G1: scratch clone is not clean at --rev")
    return dest


def run_specific(line: str, markers: tuple[str, ...]) -> bool:
    return any(m in line for m in markers) or bool(RUN_SPECIFIC.search(line))


def observe(tree: Path, target: str, argv: list[str], tmp: Path, work: Path) -> tuple[int, str]:
    try:
        p = subprocess.run([sys.executable, "-B", target, *argv], cwd=str(tree),
                           env=clean_env(TMPDIR=str(tmp)), capture_output=True,
                           timeout=PROBE_TIMEOUT)
    except subprocess.TimeoutExpired:
        return (-1, "timeout after %ds" % PROBE_TIMEOUT)
    text = (p.stdout + p.stderr).decode("utf-8", "replace")
    markers = (str(tmp), str(work))
    kept = [ln for ln in text.splitlines() if not run_specific(ln, markers)]
    return (p.returncode, "\n".join(kept))


def observe_all(tree: Path, target: str, tmp: Path, work: Path) -> dict[str, tuple[int, str]]:
    return {label: observe(tree, target, argv, tmp, work) for label, argv, _d in PROBES[target]}


def check_baseline(target: str, obs: dict[str, tuple[int, str]]) -> None:
    for label, _argv, declared in PROBES[target]:
        rc, _text = obs[label]
        if rc < 0:
            raise CouldNotEvaluate("baseline probe %s timed out" % label)
        if declared is not None and rc != declared:
            raise CouldNotEvaluate("baseline %s exit %d, declared %d: the revision does not hold "
                                   "the frozen baseline" % (label, rc, declared))


def diff_against(base: dict, obs: dict) -> list[str]:
    out = []
    for label in base:
        if base[label] != obs[label]:
            if base[label][0] != obs[label][0]:
                out.append("%s exit %d->%d" % (label, base[label][0], obs[label][0]))
            else:
                out.append("%s output changed" % label)
    return out


def evaluate(rev: str, work: Path, allow_unregistered: bool, pinned: int | None = None) -> int:
    if not re.fullmatch(r"[0-9a-f]{40}", rev or ""):
        raise CouldNotEvaluate("G1: --rev must be a full 40-hex revision, got %r" % rev)
    lane = toplevel(Path.cwd())
    rc, out = git(lane, "rev-parse", "--verify", "-q", rev + "^{commit}")
    if rc != 0 or out.decode().strip() != rev:
        raise CouldNotEvaluate("G1: %s is not a commit of %s" % (rev, lane))
    work.mkdir(parents=True, exist_ok=True)
    work = work.resolve()
    tmp = work / "tmp"
    tmp.mkdir(exist_ok=True)

    committed = git_show(lane, rev, MANIFEST).decode("utf-8")
    rows = parse_manifest(committed)
    if {row.target for row in rows} != set(PROBES):
        raise CouldNotEvaluate("manifest must name exactly the targets %s" % sorted(PROBES))
    ok_pin, pin_detail = kill_set_check(committed, pinned)
    if not ok_pin:
        raise CouldNotEvaluate("arm kill-set-size: manifest at %s has %s"
                               % (rev[:12], pin_detail))
    g3_rows = sum(1 for ln in git_show(lane, rev, SKILL).splitlines()
                  if BATTERY.encode() in ln)

    dest = materialize(lane, rev, work)
    data: dict[str, bytes] = {}
    rec_sha: dict[str, str] = {}
    base: dict[str, dict] = {}
    for target in PROBES:
        data[target] = git_show(lane, rev, target)
        rec_sha[target] = sha256(data[target])
        place(dest / target, data[target], rec_sha[target], "revision bytes of " + target)
        base[target] = observe_all(dest, target, tmp, work)
        check_baseline(target, base[target])

    results = []
    copies = 0
    for row in rows:
        text = data[row.target].decode("utf-8")
        mutated = (rewrite(text, row.recipe["kind"]) if row.cls == "equivalent"
                   else apply_recipe(text, row))
        if mutated == text:
            raise CouldNotEvaluate("%s: recipe changed no bytes" % row.rid)
        try:
            compile(mutated, row.target, "exec")
        except SyntaxError as exc:
            raise CouldNotEvaluate("%s: mutant does not compile (%s)" % (row.rid, exc))
        new = mutated.encode("utf-8")
        place(dest / row.target, new, sha256(new), row.rid)
        copies += 1
        obs = observe_all(dest, row.target, tmp, work)
        place(dest / row.target, data[row.target], rec_sha[row.target], "restore " + row.target)
        diffs = diff_against(base[row.target], obs)
        if row.cls == "equivalent":
            status = "survived" if not diffs else "KILLED (equivalence broken)"
        elif row.cls == "kill":
            status = "killed" if diffs else "SURVIVED (kill-class row not killed)"
        else:
            status = ("KILLED (survivor-class row flipped)" if diffs
                      else "survived (disclosed: %s)" % row.disposition)
        results.append({"id": row.rid, "cls": row.cls, "target": row.target,
                        "status": status, "diffs": diffs, "disposition": row.disposition})
        print("%-34s %-10s %s%s" % (row.rid, row.cls, status,
                                    ("  [" + "; ".join(diffs) + "]") if diffs else ""))

    kills = [r for r in results if r["cls"] == "kill"]
    eqs = [r for r in results if r["cls"] == "equivalent"]
    survs = [r for r in results if r["cls"] == "survivor"]
    M, K = len(kills), sum(1 for r in kills if r["diffs"])
    E, E_s = len(eqs), sum(1 for r in eqs if not r["diffs"])
    S_decl, S_disc = len(survs), sum(1 for r in survs if not r["diffs"])
    if M == 0 or E == 0:
        raise CouldNotEvaluate("manifest must declare kill and equivalent rows")

    g3_ok = g3_rows >= 1
    print("G1 revision identity PASS: rev %s; lane %s; targets and manifest read by "
          "git show; scratch clone detached at rev and clean" % (rev[:12], lane.name))
    print("G2 copy integrity PASS: %d mutant copies and %d revision copies read back at their "
          "recorded sha256" % (copies, len(PROBES)))
    if g3_ok:
        print("G3 registry presence PASS: %d SKILL.md line(s) name %s" % (g3_rows, BATTERY))
    else:
        note = (" (--allow-unregistered: pre-registry opt-in, not part of the frozen predicate)"
                if allow_unregistered else "")
        print("G3 registry presence FAIL: %d SKILL.md line(s) name %s%s"
              % (g3_rows, BATTERY, note))

    record = {"schema": "kotoba.mutation-battery/1", "rev": rev, "lane": lane.name,
              "baseline": {t: {lbl: list(v) for lbl, v in base[t].items()} for t in PROBES},
              "rev_sha256": rec_sha, "rows": results, "g3_rows": g3_rows}
    (work / "battery-record.json").write_text(json.dumps(record, indent=2) + "\n",
                                              encoding="utf-8")
    print(LINE_FMT % (K, M, E_s, E, S_disc, S_decl))
    ok = (K == M and M >= 8 and E_s == E and E >= 4 and S_disc == S_decl
          and (g3_ok or allow_unregistered))
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", help="full revision hash of the lane to measure")
    ap.add_argument("--work", help="scratch directory (clone, probe TMPDIR, record)")
    ap.add_argument("--self-test", action="store_true",
                    help="drive main() on satisfying and broken fixtures and each guard arm")
    ap.add_argument("--allow-unregistered", action="store_true",
                    help="pre-registry opt-in: G3 is reported, not enforced (not the frozen predicate)")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.rev or not args.work:
        ap.error("--rev and --work are required")
    try:
        return evaluate(args.rev, Path(args.work), args.allow_unregistered)
    except CouldNotEvaluate as exc:
        print("could-not-evaluate: %s" % exc)
        return 2
    except OSError as exc:
        print("could-not-evaluate: %s" % exc)
        return 2


# --- self-test -------------------------------------------------------------

FX_FG = '''"""Stub freeze gate for the mutation-battery self-test."""
import sys

ARGS = " ".join(sys.argv[1:])
if "--self-test" in sys.argv:
    print("0 failure(s) over 3 assertions")
    sys.exit(0)
if "r88-controls-fixed.md" in ARGS:
    print("freeze gate: 4 control(s) held -- freeze may proceed")
    sys.exit(0)
print("REFUSED control w_added_red")
sys.exit(1)
'''

FX_D5 = '''"""Stub D5 gate for the mutation-battery self-test."""
import os
import sys

NOTE = """first line
second line
"""


def unused():
    return 0


if "--self-test" in sys.argv:
    print("0 failure(s) over 2 assertions")
    print("work", os.environ.get("TMPDIR"))
    sys.exit(0)
print("r86 routed defects closed 4 of 5")
print("instance drift 4")
sys.exit(1)
'''

FX_D5_LINECOUNT = FX_D5.replace(
    'print("r86 routed defects closed 4 of 5")',
    'print("source lines", len(open(__file__).read().splitlines()))\n'
    'print("r86 routed defects closed 4 of 5")')

FX_BAT = '''"""Stub mutation battery for the mutation-battery self-test."""
import sys

if "--self-test" in sys.argv:
    print("0 failure(s) over 4 assertions")
    sys.exit(0)
sys.exit(2)
'''

SKILL_WITH = "# fixture skill\n\nRegistry: `verifiers/check_mutation_battery.py` | gate\n"
SKILL_WITHOUT = "# fixture skill\n"


def _edit(anchor: str, with_text: str) -> dict:
    return {"op": "replace", "edits": [{"anchor": anchor, "with": with_text}]}


FX_KILL_FG = ("fx-k1-fg-selftest-exit", FG, "kill",
              _edit(r'print\("0 failure\(s\) over 3 assertions"\)\n    sys\.exit\(0\)',
                    'print("0 failure(s) over 3 assertions")\n    sys.exit(1)'),
              "fixture: the self-test exit flips")
FX_KILL_STDOUT = ("fx-k2-fg-fixed-stdout", FG, "kill",
                  _edit(r"4 control\(s\) held", "5 control(s) held"),
                  "fixture: a result-bearing stdout line flips")
FX_KILL_D5 = ("fx-k3-d5-result-line", D5, "kill",
              _edit(r'print\("instance drift 4"\)', 'print("instance drift 5")'),
              "fixture: the base-receipt result line flips")
FX_SURVIVOR = ("fx-s1-d5-dead-rename", D5, "survivor",
               _edit(r"def unused\(\):", "def unused_renamed():"),
               "fixture: a dead function's rename is observed by no probe")
FX_KILL_DEAD = ("fx-k4-d5-dead-return", D5, "kill",
                _edit(r"    return 0\n", "    return 1\n"),
                "fixture: a kill-class row no probe observes (broken conjunct)")
FX_MISSING = ("fx-x-missing-anchor", FG, "kill",
              _edit("NO SUCH ANCHOR IN THE STUB", "x"),
              "fixture: anchor absent from the revision bytes")
FX_KILL_REFUSED = ("fx-k5-fg-refused-line", FG, "kill",
                    _edit(r"REFUSED control w_added_red", "REFUSED control w_added_blue"),
                    "fixture: the unsatisfied-control result line flips")
FX_KILL_FG_COUNT = ("fx-k6-fg-selftest-count", FG, "kill",
                    _edit(r"over 3 assertions", "over 8 assertions"),
                    "fixture: the freeze-gate self-test tally line flips")
FX_KILL_D5_COUNT = ("fx-k7-d5-selftest-count", D5, "kill",
                    _edit(r"over 2 assertions", "over 9 assertions"),
                    "fixture: the D5 self-test tally line flips")
FX_KILL_D5_CLOSED = ("fx-k8-d5-closed-line", D5, "kill",
                     _edit(r"closed 4 of 5", "closed 4 of 6"),
                     "fixture: the base-receipt closed-count line flips")
FX_KILL_D5_EXIT = ("fx-k9-d5-receipt-exit", D5, "kill",
                   _edit(r'print\("instance drift 4"\)\nsys\.exit\(1\)',
                         'print("instance drift 4")\nsys.exit(0)'),
                   "fixture: the base-receipt probe exit flips 1 -> 0")
FX_KILL_BAT = ("fx-k10-bat-selftest-count", BAT, "kill",
               _edit(r"over 4 assertions", "over 9 assertions"),
               "fixture: the battery stub's self-test tally flips")


def _eq_rows() -> list[tuple]:
    return [("eq-%s-%s" % (tag, kind), target, "equivalent",
             {"op": "rewrite", "kind": kind},
             "generated at measurement time: %s at every eligible site" % kind)
            for tag, target in (("fg", FG), ("d5", D5), ("bat", BAT)) for kind in EQ_KINDS]


def _satisfying_rows() -> list[tuple]:
    return [FX_KILL_FG, FX_KILL_STDOUT, FX_KILL_D5, FX_SURVIVOR,
            FX_KILL_REFUSED, FX_KILL_FG_COUNT, FX_KILL_D5_COUNT, FX_KILL_D5_CLOSED,
            FX_KILL_D5_EXIT, FX_KILL_BAT] + _eq_rows()


def _manifest_text(rows: list[tuple]) -> str:
    lines = ["\t".join(HEADER)]
    for rid, target, cls, recipe, disp in rows:
        lines.append("\t".join([rid, target, cls, json.dumps(recipe), disp]))
    return "\n".join(lines) + "\n"


def _git_fixture(repo: Path, *args: str) -> str:
    rc, out = git(repo, *args)
    if rc != 0:
        raise AssertionError("fixture git %s failed" % " ".join(args))
    return out.decode().strip()


def build_fixture(root: Path, name: str, rows: list[tuple], skill: str,
                  fg_text: str = FX_FG, d5_text: str = FX_D5, poison: bool = False) -> Path:
    repo = root / name
    repo.mkdir(parents=True)
    _git_fixture(repo, "init", "-q")
    files = {FG: fg_text, D5: d5_text, BAT: FX_BAT, MANIFEST: _manifest_text(rows), SKILL: skill}
    for rel, text in files.items():
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    assert toplevel(repo) == repo.resolve(), "fixture toplevel must be the fixture"
    _git_fixture(repo, "add", "-A")
    _git_fixture(repo, "-c", "user.name=battery-selftest",
                 "-c", "user.email=battery-selftest@example.invalid",
                 "commit", "-q", "-m", "fixture")
    if poison:
        # an uncommitted working-tree edit that would fail the baseline if read (G1 arm)
        (repo / FG).write_text("raise SystemExit(1)\n" + fg_text, encoding="utf-8")
    return repo


def run_main(repo: Path, rev: str, work: Path, allow: bool = False) -> tuple[int, str]:
    argv = ["--rev", rev, "--work", str(work)] + (["--allow-unregistered"] if allow else [])
    buf = io.StringIO()
    old = os.getcwd()
    os.chdir(repo)
    try:
        with contextlib.redirect_stdout(buf):
            rc = main(argv)
    finally:
        os.chdir(old)
    return rc, buf.getvalue()

def run_evaluate(repo: Path, rev: str, work: Path, pinned: int, allow: bool = False) -> tuple[int, str]:
    buf = io.StringIO()
    old = os.getcwd()
    os.chdir(repo)
    try:
        with contextlib.redirect_stdout(buf):
            try:
                rc = evaluate(rev, work, allow, pinned)
            except CouldNotEvaluate as exc:
                print("could-not-evaluate: %s" % exc)
                rc = 2
    finally:
        os.chdir(old)
    return rc, buf.getvalue()


class _Tally:
    def __init__(self) -> None:
        self.n = 0
        self.failures: list[str] = []

    def check(self, arm: str, cond: bool, detail: str = "") -> None:
        self.n += 1
        if not cond:
            self.failures.append("%s :: %s" % (arm, detail.strip()[-400:]))


def self_test() -> int:
    global write_target, git, place, KILL_SET_PINNED
    # round 93 (ReviewerKillPin, blocking): the fixture arms rebind the module pin; the live arms
    # read the pin captured here, and the finally block restores it.
    module_pin = KILL_SET_PINNED
    t = _Tally()
    root = Path(tempfile.mkdtemp(prefix="mutation-battery-selftest-"))
    try:
        KILL_SET_PINNED = 9
        line_ok = LINE_FMT % (9, 9, 9, 9, 1, 1)
        line_broken = LINE_FMT % (9, 10, 9, 9, 1, 1)
        line_eq = LINE_FMT % (9, 9, 8, 9, 1, 1)

        ok = build_fixture(root, "ok", _satisfying_rows(), SKILL_WITH)
        rc, out = run_main(ok, head(ok), root / "w-ok")
        t.check("satisfying world (clean): exit 0 with every kill killed and every "
                "equivalent and survivor as declared", rc == 0, out)
        t.check("satisfying world (clean): the exact predicate line is printed",
                line_ok in out.splitlines(), out)

        dirty = build_fixture(root, "dirty", _satisfying_rows(), SKILL_WITH, poison=True)
        rc, out = run_main(dirty, head(dirty), root / "w-dirty")
        t.check("G1 dirty working tree: verdict read from --rev bytes, exit 0",
                rc == 0, out)
        t.check("G1 dirty working tree: the exact predicate line is printed",
                line_ok in out.splitlines(), out)

        KILL_SET_PINNED = 10
        broken = build_fixture(root, "broken", _satisfying_rows() + [FX_KILL_DEAD], SKILL_WITH)
        rc, out = run_main(broken, head(broken), root / "w-broken")
        t.check("broken conjunct K == M: a kill-class row that no probe flips exits 1",
                rc == 1 and "kill-set-size" not in out, out)
        t.check("broken conjunct K == M: the line reads killed 9 of 10",
                line_broken in out.splitlines(), out)

        KILL_SET_PINNED = 9
        rc, out = run_main(ok, head(ok)[:12], root / "w-short")
        t.check("G1 revision identity: a non-full --rev is could-not-evaluate (exit 2)",
                rc == 2, out)
        t.check("G1 revision identity: the refusal names G1",
                "G1" in out, out)

        rc, out = run_main(ok, "f" * 40, root / "w-g1commit")
        t.check("G1 commit check: a full-hex --rev that is not a commit exits 2", rc == 2, out)
        t.check("G1 commit check: the refusal says the revision is not a commit",
                "is not a commit" in out, out)

        real_git = git

        def dirty_status(repo, *args):
            if args == ("status", "--porcelain") and "fleet" in repo.parts:
                return (0, b" M verifiers/ghost.py\n")
            return real_git(repo, *args)

        git = dirty_status
        try:
            rc, out = run_main(ok, head(ok), root / "w-dirtyclone")
        finally:
            git = real_git
        t.check("G1 clean-tree guard: a dirtied scratch clone exits 2", rc == 2, out)
        t.check("G1 clean-tree guard: the refusal says the scratch clone is not clean at --rev",
                "not clean" in out, out)

        real_place = place

        def tampered_restore(path, data, expect, label):
            payload = data + b"\n# restore-tamper\n" if label.startswith("restore ") else data
            real_place(path, payload, expect, label)

        place = tampered_restore
        try:
            rc, out = run_main(ok, head(ok), root / "w-restore")
        finally:
            place = real_place
        t.check("G2 restore read-back: a tampered revision restore after a mutant exits 2",
                rc == 2, out)
        t.check("G2 restore read-back: the refusal names G2 copy integrity on the restore copy",
                "G2 copy integrity" in out and "restore" in out, out)

        real_write = write_target

        def tampered(path: Path, data: bytes) -> None:
            real_write(path, data + b"\n# tamper\n")

        write_target = tampered
        try:
            rc, out = run_main(ok, head(ok), root / "w-tamper")
        finally:
            write_target = real_write
        t.check("G2 copy integrity: a copy that differs from the recorded bytes exits 2",
                rc == 2, out)
        t.check("G2 copy integrity: the refusal names G2", "G2" in out, out)

        bare = build_fixture(root, "bare", _satisfying_rows(), SKILL_WITHOUT)
        rc, out = run_main(bare, head(bare), root / "w-bare")
        t.check("G3 registry presence: no SKILL.md row naming the battery exits 1",
                rc == 1, out)
        t.check("G3 registry presence: the failure names G3 and keeps the predicate line",
                "G3" in out and line_ok in out.splitlines(), out)
        rc, out = run_main(bare, head(bare), root / "w-bare-allow", allow=True)
        t.check("--allow-unregistered: only G3 is waived, exit 0 with the same line",
                rc == 0 and line_ok in out.splitlines(), out)

        KILL_SET_PINNED = 10
        miss = build_fixture(root, "miss", _satisfying_rows() + [FX_MISSING], SKILL_WITH)
        rc, out = run_main(miss, head(miss), root / "w-miss")
        t.check("anchor: a recipe whose anchor is absent from the revision exits 2",
                rc == 2 and "anchor miss" in out, out)

        KILL_SET_PINNED = 9
        linecount = build_fixture(root, "linecount", _satisfying_rows(), SKILL_WITH,
                                  d5_text=FX_D5_LINECOUNT)
        rc, out = run_main(linecount, head(linecount), root / "w-lc")
        t.check("E == E: an equivalence rewrite that changes a probe output exits 1",
                rc == 1 and line_eq in out.splitlines(), out)

        probe_tmp = root / "tmp-observe"
        probe_tmp.mkdir()
        got = observe(ok, D5, ["--self-test"], probe_tmp, root / "w-observe")
        t.check("probe observation: the run-specific TMPDIR line is dropped, the result kept",
                got == (0, "0 failure(s) over 2 assertions"), repr(got))

        t.check("equivalence arm comment-insert: marker lines added and the stub compiles",
                rewrite(FX_D5, "comment-insert").count(COMMENT_MARK) >= 3
                and compile(rewrite(FX_D5, "comment-insert"), "x", "exec") is not None,
                rewrite(FX_D5, "comment-insert")[:200])
        reworded = rewrite(FX_D5, "docstring-reword")
        t.check("equivalence arm docstring-reword: marks the docstrings only",
                reworded.count(DOCSTRING_MARK) == 1 and "NOTE = \"\"\"first line" in reworded,
                reworded[:200])
        spaced = rewrite(FX_D5, "trailing-whitespace")
        t.check("equivalence arm trailing-whitespace: code lines padded, multi-line strings kept",
                "    return 0  \n" in spaced and 'NOTE = """first line\nsecond line\n"""' in spaced,
                spaced[:300])

        live = Path(__file__).resolve().parent.parent / MANIFEST
        live_text = live.read_text(encoding="utf-8") if live.is_file() else ""
        live_ok, live_detail = kill_set_check(live_text, module_pin)
        t.check("arm kill-set-size: the live manifest's kill-row count equals the pin",
                live_ok, live_detail)
        first_kill = next((ln for ln in live_text.splitlines() if "\tkill\t" in ln), None)
        dropped_text = "\n".join(ln for ln in live_text.splitlines() if ln != first_kill) + "\n"
        dropped_ok, dropped_detail = kill_set_check(dropped_text, module_pin)
        t.check("arm kill-set-size: a manifest with one kill row dropped is refused by the pin",
                not dropped_ok, dropped_detail)
        broken_ok, broken_detail = kill_set_check("not a manifest\n")
        t.check("arm kill-set-size: an unparseable manifest is refused, not raised",
                not broken_ok and "malformed" in broken_detail, broken_detail)
        pinned_rows = _satisfying_rows()
        pinned_count = sum(1 for r in pinned_rows if r[2] == "kill")
        ok_rows = build_fixture(root, "revok", pinned_rows, SKILL_WITH)
        rc, out = run_evaluate(ok_rows, head(ok_rows), root / "w-revok", pinned_count)
        t.check("kill-set-size rev path: a committed manifest matching the pin exits 0 without naming kill-set-size",
                rc == 0 and "kill-set-size" not in out, out)
        dropped = build_fixture(root, "revdrop", [r for i, r in enumerate(pinned_rows) if i != 0], SKILL_WITH)
        rc, out = run_evaluate(dropped, head(dropped), root / "w-revdrop", pinned_count)
        t.check("kill-set-size rev path: a committed manifest dropping a kill row exits 2 naming kill-set-size",
                rc == 2 and "kill-set-size" in out, out)
        broken_rev = build_fixture(root, "revbroken", pinned_rows + [FX_KILL_DEAD], SKILL_WITH)
        rc, out = run_evaluate(broken_rev, head(broken_rev), root / "w-revbroken", pinned_count + 1)
        t.check("kill-set-size rev path: an unrelated baseline failure does not name kill-set-size",
                rc == 1 and "kill-set-size" not in out, out)
    finally:
        shutil.rmtree(root, ignore_errors=True)
        KILL_SET_PINNED = module_pin
    for failure in t.failures:
        print("FAIL " + failure)
    print("%d failure(s) over %d assertions" % (len(t.failures), t.n))
    return 0 if not t.failures else 1


def head(repo: Path) -> str:
    return _git_fixture(repo, "rev-parse", "HEAD")


if __name__ == "__main__":
    sys.exit(main())
