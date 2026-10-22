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
import json
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
    ap.add_argument("--rev", required=True, metavar="COMMIT",
                    help="revision whose box proof is measured")
    ap.add_argument("--repo", default=None, metavar="DIR",
                    help="checkout the revision is read from (default: the "
                         "checkout holding this script)")
    ap.add_argument("--in-place", action="store_true",
                    help="do not use the instrument's --fixtures option; "
                         "rewrite the exported tree's manifest instead")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = repo_root(args.repo)
    if not (root / ".git").exists():
        print("ERROR %s is not a git checkout" % root, file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory(prefix="box-proof-case-deletion-") as tmp:
        tmpdir = Path(tmp)
        export = tmpdir / "export"
        export.mkdir()
        try:
            export_tree(root, args.rev, export)
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
