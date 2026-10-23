#!/usr/bin/env python3
"""box_proof_case_deletion.py -- the counter for claim C2 (operability).

C2 states: deleting any one of the six must-fail cases from
``verifiers/fixtures/dispatch-prompts/manifest.json`` makes that revision's
own box proof

    python3 -B verifiers/verify_dispatch_prompts.py --box-proof \\
        --map verifiers/checklist-baseline.json

exit 1.  This driver measures that at an arbitrary revision.

The denominator is pinned to the six conjunct names of the two boxes, not to
whatever the manifest happens to hold at ``<rev>``:

    dispatch.04  report_path_literal, report_stem_is_lane_id,
                 lane_identity_known
    dispatch.08  filename_role_round_equal, filename_report_dir_round_equal,
                 round_le_latest_dispatched

How a run works:

1. the tree at ``<rev>`` is exported read-only with ``git archive <rev> |
   tar -x -C <tmpdir>`` -- nothing is ever written in the lane;
2. the fixture manifest is read from the exported tree;
3. the intact box proof runs as a control; unless it exits 0 the driver
   aborts with exit 2 (a revision whose own intact box proof already fails
   cannot be scored for case coverage);
4. for each of the six conjuncts the manifest entry that carries that
   conjunct is deleted -- the entry only, never a fixture directory -- and
   the revision's own instrument is re-run; a conjunct with no case at
   ``<rev>`` is reported ``survived (absent)``;
5. the must-pass control cases and the N/A cases of the manifest (at
   f3046466: d04-control, d08-control and d08-missing-state) are deleted in
   turn and scored the same way, outside the six.

A deletion counts as a kill only when the instrument exits exactly 1, its
stdout carries ``boxes proven 1`` or ``boxes proven 0``, and its stderr
carries a line naming the deleted case's conjunct (for a case that declares
no conjunct: its id).  Any other outcome is ``survived`` (the proof did not
break for that case) or ``error`` (the instrument failed for an unrelated
reason -- a usage or substrate error).

Output: one line per case, then ``controls killed C of N``, ``na killed A of
M`` and, as the last line, ``killed K of 6``.  Exit 0 only when K == 6 and no
run errored, else 1.  Read-only with respect to the lane; standard library
only; deterministic.
"""

import argparse
import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path, PurePosixPath

INSTRUMENT_REL = Path("verifiers") / "verify_dispatch_prompts.py"
MANIFEST_REL = (Path("verifiers") / "fixtures" / "dispatch-prompts"
                 / "manifest.json")
FIXTURES_REL = Path("verifiers") / "fixtures" / "dispatch-prompts"
MAP_REL = Path("verifiers") / "checklist-baseline.json"

# The pinned denominator: the six conjunct names of the two boxes.  A
# conjunct is scored whether or not the manifest at <rev> carries a case for
# it; a conjunct with no case prints "survived (absent)".
CONJUNCTS = (
    ("dispatch.04", "report_path_literal"),
    ("dispatch.04", "report_stem_is_lane_id"),
    ("dispatch.04", "lane_identity_known"),
    ("dispatch.08", "filename_role_round_equal"),
    ("dispatch.08", "filename_report_dir_round_equal"),
    ("dispatch.08", "round_le_latest_dispatched"),
)

PROVEN_LINES = ("boxes proven 0", "boxes proven 1")


class DriverError(Exception):
    """The driver cannot run at all (bad revision, missing tree, ...)."""


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def repo_root(explicit: str | None) -> Path:
    """The git checkout the revision is read from.

    Default: the checkout that holds this script (its ``verifiers/`` parent
    is the repository root).  ``--repo`` overrides it.
    """
    if explicit:
        return Path(explicit).resolve()
    here = Path(__file__).resolve().parent.parent
    if (here / ".git").exists():
        return here
    return Path.cwd().resolve()


def safe_member(member: tarfile.TarInfo, dest: Path) -> tarfile.TarInfo | None:
    """The member to extract, or None to skip it.

    A member is skipped when its path escapes the destination or when it is a
    link with an absolute target: the archive carries one such fixture link
    (``.ufo/round-46/drafts/.../symlinked-scope-directory-cwd/verifiers``),
    which no verifier reads and which must not be materialised outside the
    temporary export.
    """
    name = member.name
    if name.startswith("/") or ".." in PurePosixPath(name).parts:
        return None
    if member.issym() or member.islnk():
        if member.linkname.startswith("/"):
            return None
    return member


def export_tree(root: Path, rev: str, dest: Path) -> None:
    """``git archive <rev> | tar -x -C <dest>`` -- a read-only export.

    The lane is never written to; the archive stream is unpacked into a
    temporary directory.
    """
    with tempfile.TemporaryFile() as errfile:
        proc = subprocess.Popen(
            ["git", "-C", str(root), "archive", "--format=tar", rev],
            stdout=subprocess.PIPE, stderr=errfile)
        try:
            with tarfile.open(fileobj=proc.stdout, mode="r|") as tar:
                for member in tar:
                    keep = safe_member(member, dest)
                    if keep is None:
                        continue
                    tar.extract(keep, dest)
        finally:
            if proc.stdout is not None:
                proc.stdout.close()
            proc.wait()
        if proc.returncode != 0:
            errfile.seek(0)
            err = errfile.read().decode("utf-8", "replace").strip()
            raise DriverError("git archive %s failed (exit %d): %s"
                              % (rev, proc.returncode, err))


def read_manifest(path: Path) -> dict:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise DriverError("cannot read %s (%s)"
                          % (path, exc.strerror or exc))
    try:
        data = json.loads(raw)
    except ValueError as exc:
        raise DriverError("cannot parse %s (%s)" % (path, exc))
    if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
        raise DriverError("%s: no 'cases' list" % path)
    return data


def write_manifest(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8")


def instrument_supports_fixtures(root: Path) -> bool:
    """True when this revision's instrument accepts ``--fixtures``."""
    try:
        proc = subprocess.run(
            [sys.executable, "-B", str(root / INSTRUMENT_REL), "--help"],
            cwd=str(root), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        return False
    return "--fixtures" in (proc.stdout or "") + (proc.stderr or "")


def run_box_proof(root: Path, fixtures: Path | None) -> tuple[int, str, str]:
    """Run the revision's own box proof; return (exit code, stdout, stderr)."""
    cmd = [sys.executable, "-B", str(root / INSTRUMENT_REL),
           "--box-proof", "--map", str(MAP_REL)]
    if fixtures is not None:
        cmd += ["--fixtures", str(fixtures)]
    proc = subprocess.run(cmd, cwd=str(root), stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, text=True, timeout=600)
    return proc.returncode, proc.stdout or "", proc.stderr or ""


def classify(exit_code: int, stdout: str, stderr: str,
             names: list[str]) -> str:
    """``killed`` | ``survived`` | ``error`` for one deletion.

    A kill needs all three: exit code exactly 1, ``boxes proven 1`` or
    ``boxes proven 0`` on stdout, and a stderr line naming the deleted case's
    conjunct (or its id, when the case declares no conjunct).
    """
    if exit_code == 0:
        return "survived"
    if exit_code != 1:
        return "error"
    proven = any(line.strip() in PROVEN_LINES
                 for line in stdout.splitlines())
    named = any(name and name in stderr for name in names)
    return "killed" if (proven and named) else "survived"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", required=False, metavar="COMMIT",
                    help="revision whose box proof is measured")
    ap.add_argument("--repo", default=None, metavar="DIR",
                    help="checkout the revision is read from (default: the "
                         "checkout holding this script)")
    ap.add_argument("--in-place", action="store_true",
                    help="do not use the instrument's --fixtures option; "
                         "rewrite the exported tree's manifest instead")
    ap.add_argument("--self-test", action="store_true",
                    help="run isolated temporary-fixture tests")
    return ap


def self_test() -> int:
    """Exercise killed and surviving deletions in an isolated fixture repo."""
    assertions = 0
    failures = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    case_ids = (
        "d04-placeholder",
        "d04-stem",
        "d04-unknown-lane",
        "d08-role-round",
        "d08-report-dir-round",
        "d08-above-state",
    )
    stub = """import json
import sys
from pathlib import Path

case_names = {
    "d04-placeholder": ("dispatch.04", "report_path_literal"),
    "d04-stem": ("dispatch.04", "report_stem_is_lane_id"),
    "d04-unknown-lane": ("dispatch.04", "lane_identity_known"),
    "d08-role-round": ("dispatch.08", "filename_role_round_equal"),
    "d08-report-dir-round": ("dispatch.08", "filename_report_dir_round_equal"),
    "d08-above-state": ("dispatch.08", "round_le_latest_dispatched"),
}
if "--help" in sys.argv:
    print("usage: fixture instrument --box-proof --fixtures")
    raise SystemExit(0)
args = sys.argv[1:]
if "--box-proof" not in args:
    raise SystemExit(2)
map_path = Path(args[args.index("--map") + 1])
survive = json.loads(map_path.read_text(encoding="utf-8")).get("survive")
fixtures = Path("verifiers/fixtures/dispatch-prompts")
if "--fixtures" in args:
    fixtures = Path(args[args.index("--fixtures") + 1])
cases = json.loads((fixtures / "manifest.json").read_text(encoding="utf-8"))["cases"]
remaining = {case.get("id") for case in cases if isinstance(case, dict)}
missing = (set(case_names) | {"d04-control"}) - remaining
if not missing:
    print("boxes proven 2")
    raise SystemExit(0)
if len(missing) != 1:
    raise SystemExit(2)
case_id = next(iter(missing))
if case_id == "d04-control" or case_id == survive:
    print("boxes proven 2")
    raise SystemExit(0)
check, conjunct = case_names[case_id]
print("boxes proven 1")
print("box-proof: %s/%s: %s missing" % (check, case_id, conjunct),
      file=sys.stderr)
raise SystemExit(1)
"""
    try:
        with tempfile.TemporaryDirectory(
                prefix="box-proof-case-deletion-selftest-") as tmp:
            repo = Path(tmp)
            fixture_dir = repo / FIXTURES_REL
            fixture_dir.mkdir(parents=True)
            (fixture_dir / "marker").write_text("fixture\n", encoding="utf-8")
            (fixture_dir / "manifest.json").write_text(
                json.dumps({
                    "cases": [
                        {"check": check_name,
                         "expect_conjunct": conjunct,
                         "expect_verdict": "FAIL",
                         "id": case_id}
                        for case_id, (check_name, conjunct)
                        in zip(case_ids, CONJUNCTS)
                    ] + [{"check": "dispatch.04", "expect_verdict": "PASS",
                          "id": "d04-control"}]
                }, indent=2) + "\n",
                encoding="utf-8")
            baseline = repo / MAP_REL
            baseline.parent.mkdir(parents=True, exist_ok=True)
            baseline.write_text('{"survive": "d04-control"}\n',
                                encoding="utf-8")
            instrument = repo / INSTRUMENT_REL
            instrument.parent.mkdir(parents=True, exist_ok=True)
            instrument.write_text(stub, encoding="utf-8")

            def git(*args: str) -> str:
                proc = subprocess.run(
                    ["git", "-C", str(repo), *args],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if proc.returncode:
                    raise RuntimeError(proc.stderr.strip() or
                                       "git %s failed" % " ".join(args))
                return proc.stdout.strip()

            def commit(label: str) -> str:
                git("add", "-A")
                git("-c", "user.name=kotoba self-test",
                    "-c", "user.email=self-test@example.invalid",
                    "-c", "commit.gpgsign=false",
                    "-c", "core.hooksPath=/dev/null",
                    "commit", "-q", "-m", label)
                return git("rev-parse", "HEAD")

            git("init", "-q")
            rev_clean = commit("all must-fail cases break the proof")

            def run_revision(rev: str) -> tuple[int, str, str]:
                out, err = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(out), \
                        contextlib.redirect_stderr(err):
                    code = main(["--rev", rev, "--repo", str(repo)])
                return code, out.getvalue(), err.getvalue()

            code, out, err = run_revision(rev_clean)
            check("complete fixture returns clean", code, 0)
            check("killed finding is stable",
                  "case d04-placeholder (report_path_literal): exit 1 killed"
                  in out, True)
            check("surviving control finding is stable",
                  "control d04-control: exit 0 survived" in out, True)
            check("complete fixture summary", out.splitlines()[-1],
                  "killed 6 of 6")
            check("complete fixture stderr", err, "")

            baseline.write_text('{"survive": "d04-placeholder"}\n',
                                encoding="utf-8")
            rev_surviving = commit("one must-fail deletion survives")
            code, out, err = run_revision(rev_surviving)
            check("incomplete fixture returns failed", code, 1)
            check("surviving deletion finding is stable",
                  "case d04-placeholder (report_path_literal): exit 0 survived"
                  in out, True)
            check("another deletion is still killed",
                  "case d04-stem (report_stem_is_lane_id): exit 1 killed"
                  in out, True)
            check("incomplete fixture summary", out.splitlines()[-1],
                  "killed 5 of 6")
            check("incomplete fixture stderr", err, "")
            code, out, err = run_revision("0" * 40)
            check("unknown revision returns could-not-evaluate", code, 2)
            check("unknown revision reports could-not-evaluate",
                  "could-not-evaluate:" in err, True)

            python_only = repo / "python-only"
            python_only.mkdir()
            (python_only / "python3").symlink_to(sys.executable)
            old_path = os.environ.get("PATH")
            try:
                os.environ["PATH"] = str(python_only)
                code, out, err = run_revision(rev_clean)
            finally:
                if old_path is None:
                    os.environ.pop("PATH", None)
                else:
                    os.environ["PATH"] = old_path
            check("missing git returns could-not-evaluate", code, 2)
            check("missing git reports could-not-evaluate",
                  "could-not-evaluate:" in err, True)
    except (OSError, subprocess.SubprocessError, RuntimeError) as exc:
        failures += 1
        print("FAIL isolated fixture run: %s" % exc)

    print("self-test: %d failure(s) over %d assertions"
          % (failures, assertions))
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = build_parser()
    args = ap.parse_args(argv)
    if args.self_test:
        if args.rev is not None or args.repo is not None or args.in_place:
            ap.error("--self-test cannot be combined with --rev, --repo, or "
                     "--in-place")
        return self_test()
    if args.rev is None:
        ap.error("the following arguments are required: --rev")
    root = repo_root(args.repo)
    if not (root / ".git").exists():
        print("ERROR %s is not a git checkout" % root, file=sys.stderr)
        return 2

    try:
        checked = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--verify", "--quiet",
             "%s^{commit}" % args.rev],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except OSError as exc:
        print("could-not-evaluate: git revision check could not run: %s"
              % exc, file=sys.stderr)
        return 2
    if checked.returncode != 0:
        print("could-not-evaluate: revision %r is not a commit in %s"
              % (args.rev, root), file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory(prefix="box-proof-case-deletion-") as tmp:
        tmpdir = Path(tmp)
        export = tmpdir / "export"
        export.mkdir()
        try:
            export_tree(root, args.rev, export)
        except OSError as exc:
            print("could-not-evaluate: git archive could not run: %s" % exc,
                  file=sys.stderr)
            return 2
        except DriverError as exc:
            print("ERROR %s" % exc, file=sys.stderr)
            return 2

        instrument = export / INSTRUMENT_REL
        if not instrument.is_file():
            print("ERROR %s has no %s" % (args.rev, INSTRUMENT_REL),
                  file=sys.stderr)
            return 2
        manifest_path = export / MANIFEST_REL
        if not manifest_path.is_file():
            print("ERROR %s has no %s" % (args.rev, MANIFEST_REL),
                  file=sys.stderr)
            return 2

        manifest = read_manifest(manifest_path)
        cases = [c for c in manifest["cases"] if isinstance(c, dict)]

        # -- control: the intact box proof must exit 0 --------------------
        code, out, err = run_box_proof(export, None)
        print("control: exit %d %s" % (code, out.strip().splitlines()[-1]
                                       if out.strip() else ""), flush=True)
        if code != 0:
            print("ERROR the intact box proof at %s does not exit 0; "
                  "case coverage is not measurable" % args.rev,
                  file=sys.stderr)
            return 2

        use_fixtures = ((not args.in_place)
                        and instrument_supports_fixtures(export))
        print("fixtures: %s" % ("--fixtures" if use_fixtures else "in-place"),
              flush=True)

        errors = 0

        def attempt(case: dict, names: list[str], label: str) -> str:
            """Delete one manifest entry (only the entry) and re-run.

            The fixture directories are never touched: the deletion removes
            the manifest entry alone.
            """
            nonlocal errors
            cid = case.get("id")
            reduced = dict(manifest)
            reduced["cases"] = [c for c in manifest["cases"]
                                if not (isinstance(c, dict)
                                        and c.get("id") == cid)]
            if use_fixtures:
                work = tmpdir / ("fixtures-%s" % cid)
                shutil.copytree(export / FIXTURES_REL, work)
                write_manifest(work / "manifest.json", reduced)
                rcode, rout, rerr = run_box_proof(export, work)
            else:
                write_manifest(manifest_path, reduced)
                rcode, rout, rerr = run_box_proof(export, None)
            verdict = classify(rcode, rout, rerr, names)
            if verdict == "error":
                errors += 1
            print("%s: exit %d %s" % (label, rcode, verdict), flush=True)
            return verdict

        # -- the six conjuncts (the pinned denominator) --------------------
        killed = 0
        for check, conjunct in CONJUNCTS:
            holders = [c for c in cases
                       if c.get("expect_conjunct") == conjunct
                       and c.get("check") == check]
            must_fail = [c for c in holders
                         if c.get("expect_verdict") == "FAIL"]
            pool = must_fail or holders
            if not pool:
                print("conjunct %s (%s): no case at %s survived (absent)"
                      % (conjunct, check, args.rev), flush=True)
                continue
            case = pool[0]
            verdict = attempt(case, [conjunct],
                              "case %s (%s)" % (case.get("id"), conjunct))
            if verdict == "killed":
                killed += 1

        # -- the must-pass controls and the N/A case (outside the six) ------
        controls = [c for c in cases if c.get("expect_verdict") == "PASS"]
        na_cases = [c for c in cases if c.get("expect_verdict") == "N/A"]
        controls_killed = 0
        for case in controls:
            # a control declares no conjunct: its box stands for it
            names = [case.get("id"), case.get("check")]
            verdict = attempt(case, names,
                              "control %s" % case.get("id"))
            if verdict == "killed":
                controls_killed += 1
        na_killed = 0
        for case in na_cases:
            names = [case.get("expect_conjunct") or case.get("id")]
            verdict = attempt(case, names, "na %s" % case.get("id"))
            if verdict == "killed":
                na_killed += 1

        print("controls killed %d of %d" % (controls_killed, len(controls)),
              flush=True)
        print("na killed %d of %d" % (na_killed, len(na_cases)), flush=True)
        print("killed %d of 6" % killed, flush=True)
        if errors:
            print("ERROR %d run(s) errored" % errors, file=sys.stderr)
            return 1
        return 0 if killed == 6 else 1


if __name__ == "__main__":
    sys.exit(main())
