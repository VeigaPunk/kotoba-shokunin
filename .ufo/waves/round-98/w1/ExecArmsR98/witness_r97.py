#!/usr/bin/env python3
"""MutTesterDispatchR97 differential witnesses (round 97, wave r97-w1; NOT a lane file).

For every mutant of probe_r97.py that is not killed, show the behavioural
difference between the honest instrument and the mutant: the same call, on the
same input, executed against both texts, with the observed values printed side
by side.  Also used to name the equivalent mutant.

Usage: python3 -B witness_r97.py LABEL REV REPO
Exit 0 when every witness ran, 2 otherwise. Never edits the lane.
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
sys.path.insert(0, str(Path(__file__).resolve().parent))
import probe_r97  # noqa: E402  (the mutant table lives next to this file)

GOOD = ("You are the kote L1, round 7. Working dir: /fleet/kote-shokunin.\n"
        "\n"
        "Write the round report at `/fleet/.ufo/reports/round-7/kote.md` on the\n"
        "main repo. | godspeed\n")


def load_mod(text: str, path: Path) -> dict:
    ns = {"__name__": "witness_mod", "__file__": str(path)}
    exec(compile(text, str(path), "exec", dont_inherit=True), ns)
    return ns


def case_tree(root: Path, name: str, text: str, baseline: str | None = None,
              legacy: str | None = None, subdir: bool = False) -> Path:
    case = root / name
    (case / "prompts").mkdir(parents=True, exist_ok=True)
    (case / "state").mkdir(parents=True, exist_ok=True)
    (case / "fleet" / "kote-shokunin").mkdir(parents=True, exist_ok=True)
    (case / "prompts" / "kote-round-7.md").write_text(text, encoding="utf-8")
    if subdir:
        (case / "prompts" / "ghost-round-7.md").mkdir()
    if baseline is not None:
        (case / "state" / "kote.report-baseline").write_text(
            baseline + " " + "0" * 64 + "\n", encoding="utf-8")
    if legacy is not None:
        (case / "state" / "kote.round").write_text(legacy + "\n", encoding="utf-8")
    return case


def safe(fn):
    try:
        return fn()
    except Exception as exc:  # the witness reports the exception, never hides it
        return "%s: %s" % (type(exc).__name__, exc)


def proof_tree(root: Path, repo: Path, rev: str, kind: str) -> tuple[Path, Path]:
    """A box-proof tree: committed map + fixtures + SKILL.md, then the defect."""
    tree = root / ("proof-" + kind)
    (tree / "verifiers").mkdir(parents=True)
    shutil.copy2(repo / "verifiers" / "checklist-baseline.json",
                 tree / "verifiers" / "checklist-baseline.json")
    shutil.copytree(repo / "verifiers" / "fixtures" / "dispatch-prompts",
                    tree / "verifiers" / "fixtures" / "dispatch-prompts")
    shutil.copy2(repo / "SKILL.md", tree / "SKILL.md")
    map_path = tree / "verifiers" / "checklist-baseline.json"
    if kind == "disposition":
        data = json.loads(map_path.read_text(encoding="utf-8"))
        for box in data["boxes"]:
            if box["box_id"] == "dispatch.04":
                box["disposition"] = "executed:" + INSTRUMENT
        map_path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    elif kind == "skill":
        skill = tree / "SKILL.md"
        lines = skill.read_text(encoding="utf-8").splitlines(keepends=True)
        in_section = False
        seen = 0
        for i, line in enumerate(lines):
            if line.startswith("#"):
                in_section = line.strip() == "## Dispatch-prompt fidelity checklist"
                continue
            if in_section and line.lstrip().startswith("- [ ]"):
                if seen == 3:  # dispatch.04 is the fourth box of the section
                    lines[i] = line.rstrip("\n") + " (reworded)\n"
                    break
                seen += 1
        skill.write_text("".join(lines), encoding="utf-8")
    return map_path, tree / "verifiers" / "fixtures" / "dispatch-prompts"


def run_proof(ns: dict, map_path: Path, fixtures: Path) -> tuple[int, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = ns["box_proof"](map_path, fixtures)
    return code, (out.getvalue() + err.getvalue()).strip().splitlines()[-1]


def witness(mid: str, ns: dict, root: Path, repo: Path, rev: str):
    """One call per mutant; returns the observed value under this module text."""
    if mid == "m20-lane-suffix-unanchored":
        return ns["lane_of"]("kote-round-7.md.bak")
    if mid == "m21-l1-kind-round":
        case = root / "l1"
        (case / "prompts").mkdir(parents=True, exist_ok=True)
        (case / "state").mkdir(parents=True, exist_ok=True)
        (case / "fleet").mkdir(parents=True, exist_ok=True)
        (case / "prompts" / "kote-L1.md").write_text(GOOD, encoding="utf-8")
        r = ns["evaluate_dispatch_08"](case / "prompts", case / "state", case / "fleet")
        return (r["evaluated"], len(r["out_of_scope"]), r["status"])
    if mid == "m22-dirs-first-only":
        case = case_tree(root, "dirs", GOOD + "Earlier note: "
                         "`/fleet/.ufo/reports/round-8/kote.md`.\n", "9")
        r = ns["evaluate_dispatch_08"](case / "prompts", case / "state", case / "fleet")
        f = ns["_verdict_of"](r, "kote-round-7.md")
        return f["conjuncts"]["filename_report_dir_round_equal"]["status"]
    if mid == "m23-verdict-first-file":
        res = {"files": [{"file": "a", "verdict": "PASS"},
                         {"file": "b", "verdict": "FAIL"}]}
        return ns["_verdict_of"](res, "b")
    if mid == "m24-proof-disposition-unenforced":
        map_path, fx = proof_tree(root, repo, rev, "disposition")
        return run_proof(ns, map_path, fx)
    if mid == "m25-proof-live-hash-unenforced":
        map_path, fx = proof_tree(root, repo, rev, "skill")
        return run_proof(ns, map_path, fx)
    if mid == "m26-fence-any-close":
        skill = ("# Dispatch-prompt fidelity checklist\n"
                 "\n"
                 "```\n"
                 "code\n"
                 "~~~\n"
                 "- [ ] box four text\n"
                 "```\n")
        return ns["dispatch_box_sha256"](skill)
    if mid == "m27-legacy-exists":
        case = root / "legacy-dir"
        (case / "state" / "kote.round").mkdir(parents=True, exist_ok=True)
        return ns["state_source"](case / "state", "kote")
    if mid == "m28-prompts-include-dirs":
        case = case_tree(root, "subdir", GOOD, "9", subdir=True)
        return safe(lambda: ns["evaluate_dispatch_04"](
            case / "prompts", case / "state", case / "fleet")["evaluated"])
    if mid == "m29-file-result-na-first":
        return ns["_file_result"]("f", "kote", {
            "a": {"status": "FAIL"}, "b": {"status": "N/A"}})["verdict"]
    if mid == "m30-state-splitlines":
        case = root / "baseline"
        (case / "state").mkdir(parents=True, exist_ok=True)
        (case / "state" / "kote.report-baseline").write_text(
            "9 " + "0" * 64 + "\n", encoding="utf-8")
        return ns["state_source"](case / "state", "kote")
    if mid == "m31-md-uppercase":
        return ns["report_paths"]("at `/x/.ufo/reports/round-7/kote.MD` now")
    if mid == "m32-report-paths-sorted":
        return ns["report_paths"](
            "a .ufo/reports/round-9/k.md b .ufo/reports/round-4/k.md")
    if mid == "m33-role-last-line":
        return ns["role_round"]("You are the kote L1, round 6.\n\n"
                                "This dispatch is round 7.")
    if mid == "m34-finish-fails-first-only":
        files = [{"file": "a", "verdict": "FAIL",
                  "conjuncts": {"report_path_literal": {"status": "FAIL"}}},
                 {"file": "b", "verdict": "FAIL",
                  "conjuncts": {"report_stem_is_lane_id": {"status": "FAIL"}}}]
        return ns["_finish"]("dispatch.04", files, [])["detail"]
    raise KeyError(mid)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: witness_r97.py LABEL REV REPO", file=sys.stderr)
        return 2
    label, rev, repo = argv
    got = subprocess.run(["git", "-C", repo, "rev-parse", "--verify", "-q", rev + "^{commit}"],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if got.returncode != 0:
        print("WITNESS-NOT-EVALUATED: REV %s is not a commit of %s" % (rev, repo))
        return 2
    rev = got.stdout.decode().strip()
    shown = subprocess.run(["git", "-C", repo, "show", "%s:%s" % (rev, INSTRUMENT)],
                           stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if shown.returncode != 0:
        print("WITNESS-NOT-EVALUATED: instrument absent at %s" % rev)
        return 2
    original = shown.stdout.decode("utf-8")
    repo_path = Path(repo).resolve()
    root = Path(tempfile.mkdtemp(prefix="witness.", dir=os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")))
    try:
        print("witness %s rev %s" % (label, rev))
        for mid, anchor, repl, klass, note in probe_r97.MUTANTS:
            if original.count(anchor) != 1:
                print("%-34s ANCHOR-MISS" % mid)
                continue
            mutated = original.replace(anchor, repl)
            base_ns = load_mod(original, root / "base" / INSTRUMENT)
            mut_ns = load_mod(mutated, root / "mut" / INSTRUMENT)
            a = safe(lambda: witness(mid, base_ns, root / ("b-" + mid), repo_path, rev))
            b = safe(lambda: witness(mid, mut_ns, root / ("m-" + mid), repo_path, rev))
            same = a == b
            print("%-34s %s" % (mid, "EQUIVALENT-ON-WITNESS" if same else "DIFFERS"))
            print("  base   %r" % (a,))
            print("  mutant %r" % (b,))
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
