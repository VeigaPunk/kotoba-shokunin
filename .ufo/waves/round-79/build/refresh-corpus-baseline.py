#!/usr/bin/env python3
"""refresh-corpus-baseline.py -- re-record verifiers/corpus-baseline.json from the gate's own bytes.

Owner: kotoba round 79, wave 1, seat Kb79E03IndexBaseline (C1 repair 3 of 4: corpus index and
baseline). Re-runnable at any tip: the three `equal` expectations the corpus gate compares against
a baseline (`corpus.index.tracked_files`, `corpus.pointers.report_total`,
`corpus.pointers.commit_total`) are copied from the gate's own
`python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` observation over the tree
this script points at. `zero` expectations stay `expect: 0`; they are never fitted to an
observation, so a live zero-mode defect keeps the gate red and is named, not laundered.

usage:
  refresh-corpus-baseline.py --repo <root> [--note-key KEY] [--carry CHECK_ID ...]
                             [--dry-run] [--keep-temp]

  --repo <root>        toplevel of the git work tree holding the tree to record (typically a
                       scratch clone committed at the tip the baseline should describe)
  --note-key <key>     key under `notes` that records this re-record (default: round79_rerecord)
  --carry <CHECK_ID>   repeatable; a `zero`-mode check whose nonzero observation is a known,
                       separately-owned defect. Its expectation is still written as 0 and the
                       residual is named in `measured_against.note` and on stdout. `corpus.index.*`
                       classes can never be carried -- an unindexed or stale index row is the thing
                       this script's caller must fix first.
  --dry-run            print old -> new for every baseline key and stop before writing
  --keep-temp          keep the TMPDIR directory holding the two raw gate JSON documents and
                       print its path (default: remove it)

Preconditions, all fail-closed (exit 2, baseline untouched):
  * <root> is a directory and the toplevel of a git work tree (`rev-parse --show-toplevel`)
  * the tree carries verifiers/verify_corpus_integrity.py, verifiers/verify_corpus_independent.py,
    verifiers/corpus-baseline.json and corpus/README.md
  * `git status --porcelain` is empty: the gate reads worktree bytes while the baseline is
    recorded at HEAD, so a dirty tree makes the recorded head ambiguous (this also rules out
    untracked corpus files, which `git ls-files corpus/` -- the gate's universe -- cannot see)
  * the integrity gate's `--self-test` passes (the instrument's own model is falsified first)
  * the integrity gate and the independent re-derivation both run (exit 0 or 1); exit 2/3, a
    missing `observed` block or an unparseable document is an environment answer, not a baseline
  * after the write, the integrity gate's only remaining drift is a class named by `--carry`; a
    red independent gate is printed (it does not own this baseline) and left to the caller
  * the two gates agree on every observed class this script records (tracked_files, unindexed,
    stale, missing, report_total, commit_total); disagreement refuses. On the three remaining
    zero-mode classes a divergence is printed and stamped into the note, because their expectation
    is 0 either way and the divergence is a finding about the instruments
  * every baseline check id resolves to an observed key, has mode `equal` or `zero`, and an
    integer observation; a nonzero zero-mode class refuses unless named by `--carry`

Writes exactly one path: `<root>/verifiers/corpus-baseline.json` (never through a symlink). The
gate JSON documents live under `$TMPDIR` (or the interpreter's default temp dir) and are removed on
exit unless `--keep-temp`.

Exit: 0 written (or dry-run), 2 refused, 3 internal or post-condition failure.

Re-run order at a tip (this is the one that matters for a round that adds corpus files):
  1. index every new tracked corpus file in corpus/README.md's `## Coverage map` (column 2),
  2. commit that tree,
  3. run this script against it (clean tree, committed tip),
  4. re-run both corpus gates and the tip battery.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

INTEGRITY = "verifiers/verify_corpus_integrity.py"
INDEPENDENT = "verifiers/verify_corpus_independent.py"
BASELINE = "verifiers/corpus-baseline.json"
INDEX = "corpus/README.md"
REQUIRED = (INTEGRITY, INDEPENDENT, BASELINE, INDEX)

# baseline check id -> where the independent re-derivation carries the same class
INDEPENDENT_KEYS = {
    "corpus.index.tracked_files": ("index", "tracked_files"),
    "corpus.index.unindexed": ("index", "unindexed"),
    "corpus.index.stale_patterns": ("index", "stale_tokens"),
    "corpus.index.missing_paths": ("index", "missing_paths"),
    "corpus.pointers.report_total": ("pointers", "report_total"),
    "corpus.pointers.report_dead": ("pointers", "report_dead"),
    "corpus.pointers.commit_total": ("commits", "commit_total"),
    "corpus.pointers.commit_unresolvable": ("commits", "commit_unresolvable"),
    "corpus.pointers.commit_nonhash": ("commits", "commit_nonhash"),
}
# Classes whose observed value this script writes into the baseline. The two instruments must
# agree on every one of them or nothing is recorded.
HARD_CROSS_CHECK = {
    "corpus.index.tracked_files",
    "corpus.index.unindexed",
    "corpus.index.stale_patterns",
    "corpus.index.missing_paths",
    "corpus.pointers.report_total",
    "corpus.pointers.commit_total",
}
# zero-mode classes whose observation is never recorded (expect stays 0): a divergence between the
# instruments is reported and stamped into the note, because it is a finding about the instruments,
# not a value to record. Measured at the round-79 base: the integrity gate harvests
# `HEAD:.ufo/reports/round-77/kotoba.md` as one token (the `HEAD:` prefix defeats its fleet hop) and
# reads report_dead 1, while the independent derivation reads 0.
SOFT_CROSS_CHECK = set(INDEPENDENT_KEYS) - HARD_CROSS_CHECK
INDEX_PREFIX = "corpus.index."


class Refused(Exception):
    """The tree or the bytes cannot honestly answer the question (exit 2)."""


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)


def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return run(["git", "-C", str(root), *args], root)


def open_tree(raw: str) -> Path:
    """Resolve `--repo` to the toplevel of a git work tree; refuse anything else."""
    root = Path(raw).expanduser()
    if not root.is_dir():
        raise Refused(f"--repo {raw}: no such directory")
    root = root.resolve()
    proc = git(root, "rev-parse", "--show-toplevel")
    if proc.returncode != 0:
        raise Refused(f"--repo {root}: not a git work tree ({proc.stderr.strip()})")
    top = Path(proc.stdout.strip()).resolve()
    if top != root:
        raise Refused(f"--repo {root} is not the work-tree toplevel ({top})")
    missing = [rel for rel in REQUIRED if not (root / rel).is_file()]
    if missing:
        raise Refused(f"--repo {root}: unexpected tree, missing {', '.join(missing)}")
    status = git(root, "status", "--porcelain", "--untracked-files=all")
    if status.returncode != 0:
        raise Refused(f"--repo {root}: cannot read git status ({status.stderr.strip()})")
    dirty = [line for line in status.stdout.splitlines() if line.strip()]
    if dirty:
        shown = "\n  ".join(dirty[:20])
        more = "" if len(dirty) <= 20 else f"\n  ... {len(dirty) - 20} more"
        raise Refused(
            "dirty tree: the gate reads worktree bytes while the baseline is recorded at HEAD; "
            f"commit or clean these paths first:\n  {shown}{more}"
        )
    return root


def gate_json(root: Path, tmp: Path, name: str, script: str, *extra: str) -> tuple[int, dict]:
    """Run one gate with `--json`; return (own exit status, parsed document)."""
    proc = run([sys.executable, "-B", str(root / script), "--repo", str(root), "--json", *extra], root)
    out = tmp / f"{name}.json"
    err = tmp / f"{name}.err"
    out.write_text(proc.stdout, encoding="utf-8")
    err.write_text(proc.stderr, encoding="utf-8")
    if proc.returncode not in (0, 1):
        detail = (proc.stderr.strip() or proc.stdout.strip()).splitlines()[:10]
        raise Refused(
            f"{script} exited {proc.returncode} (environment answer, not a measurement): "
            + " | ".join(detail)
        )
    try:
        doc = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise Refused(f"{script} did not emit JSON: {exc}") from exc
    if "observed" not in doc:
        raise Refused(f"{script} JSON has no `observed` block")
    return proc.returncode, doc


def self_test(root: Path) -> None:
    proc = run([sys.executable, "-B", str(root / INTEGRITY), "--self-test"], root)
    if proc.returncode != 0:
        tail = (proc.stdout.strip() or proc.stderr.strip()).splitlines()[-5:]
        raise Refused(
            f"{INTEGRITY} --self-test exited {proc.returncode}; refusing to record a baseline "
            "from an instrument that does not pass its own fixtures: " + " | ".join(tail)
        )


def check_mode(mode: object, check_id: str) -> str:
    if mode not in ("equal", "zero"):
        raise Refused(f"{BASELINE}: {check_id} has unknown mode {mode!r}")
    return str(mode)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="re-record verifiers/corpus-baseline.json from the corpus gate's own JSON"
    )
    ap.add_argument("--repo", required=True, help="toplevel of the git work tree to record")
    ap.add_argument("--note-key", default="round79_rerecord", help="key under `notes`")
    ap.add_argument(
        "--carry",
        action="append",
        default=[],
        metavar="CHECK_ID",
        help="zero-mode check with a known nonzero residual (never a corpus.index.* class)",
    )
    ap.add_argument("--dry-run", action="store_true", help="print old -> new, do not write")
    ap.add_argument("--keep-temp", action="store_true", help="keep the raw gate JSON (TMPDIR)")
    args = ap.parse_args(argv)

    tmpdir: str | None = None
    try:
        root = open_tree(args.repo)

        carried = set(args.carry)
        for check_id in sorted(carried):
            if check_id.startswith(INDEX_PREFIX):
                raise Refused(
                    f"--carry {check_id}: an index class is never carried -- write the missing "
                    "coverage-map row (or remove the stale token) and re-run"
                )

        self_test(root)

        tmpdir = tempfile.mkdtemp(
            prefix="refresh-corpus-baseline.", dir=os.environ.get("TMPDIR") or None
        )
        tmp = Path(tmpdir)

        _, integrity_doc = gate_json(root, tmp, "integrity", INTEGRITY, "--no-baseline")
        _, independent_doc = gate_json(root, tmp, "independent", INDEPENDENT)

        observed = integrity_doc["observed"].get("corpus")
        if not isinstance(observed, dict):
            raise Refused(f"{INTEGRITY} JSON has no `observed.corpus` object")
        other = independent_doc["observed"]

        divergences: list[tuple[str, int, int]] = []
        for check_id, path in INDEPENDENT_KEYS.items():
            node: object = other
            for part in path:
                if not isinstance(node, dict) or part not in node:
                    raise Refused(
                        f"{INDEPENDENT} JSON has no `observed.{'.'.join(path)}` "
                        f"(needed to cross-check {check_id})"
                    )
                node = node[part]
            key = check_id.rsplit(".", 1)[-1]
            if key not in observed:
                raise Refused(f"{INTEGRITY} JSON has no observed key {key!r} for {check_id}")
            mine, theirs = int(observed[key]), int(node)  # type: ignore[arg-type]
            if mine == theirs:
                continue
            if check_id in HARD_CROSS_CHECK:
                raise Refused(
                    f"the two gates disagree on {check_id}: integrity {mine} vs independent "
                    f"{theirs}; refusing to record either"
                )
            divergences.append((check_id, mine, theirs))
            print(
                f"gate disagreement (not recorded, expectation stays 0): {check_id} "
                f"integrity {mine} vs independent {theirs}"
            )

        baseline_path = root / BASELINE
        if baseline_path.is_symlink():
            raise Refused(f"{BASELINE} is a symlink; refusing to write through it")
        baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
        checks = baseline.get("checks")
        if not isinstance(checks, dict) or not checks:
            raise Refused(f"{BASELINE} has no `checks` object")

        changes: list[tuple[str, object, int]] = []
        carried_red: list[tuple[str, int]] = []
        for check_id, row in checks.items():
            if not isinstance(row, dict):
                raise Refused(f"{BASELINE}: {check_id} is not an object")
            key = check_id.rsplit(".", 1)[-1]
            if key not in observed:
                raise Refused(f"{BASELINE}: {check_id} has no observed key {key!r}")
            now = int(observed[key])
            old = row.get("expect")
            mode = check_mode(row.get("mode"), check_id)
            if mode == "zero":
                if now != 0 and check_id not in carried:
                    raise Refused(
                        f"zero-mode {check_id} observed {now}, not 0; fix the drift (or name the "
                        "known residual with --carry) -- a baseline never records a zero-mode "
                        "value"
                    )
                if now != 0:
                    carried_red.append((check_id, now))
                row["expect"] = 0
                if old != 0:
                    changes.append((check_id, old, 0))
                continue
            row["expect"] = now
            if old != now:
                changes.append((check_id, old, now))

        head = git(root, "rev-parse", "HEAD").stdout.strip()
        subject = git(root, "log", "-1", "--format=%s").stdout.strip()
        # `git branch --contains` is not usable here: on a detached HEAD it prints a pseudo-entry
        # ("(HEAD detached from ...)") that is not a branch. Only refs/heads prove resolvability.
        on_branch = git(
            root, "for-each-ref", "--contains", head, "--format=%(refname:short)", "refs/heads"
        ).stdout.split()
        head_label = head[:7] if on_branch else (
            f"{head[:7]} (detached measurement commit; resolvable in the measuring clone only, "
            "not in the lane repository)"
        )
        moved = (
            ", ".join(f"{cid.rsplit('.', 1)[-1]} {old} -> {new}" for cid, old, new in changes)
            or "no expectation moved"
        )
        residual = (
            "; carried residual (baseline expectation stays 0, gate remains red): "
            + ", ".join(f"{cid} observed {now}" for cid, now in carried_red)
            if carried_red
            else "; every zero-mode class observed 0"
        )
        noted = (
            "; instrument divergence (not recorded, expectation stays 0): "
            + ", ".join(f"{cid} integrity {mine} vs independent {theirs}" for cid, mine, theirs in divergences)
            if divergences
            else ""
        )
        repo_name = (baseline.get("measured_against") or {}).get("repo") or os.path.basename(str(root))

        baseline["as_of"] = datetime.date.today().isoformat()
        baseline["measured_against"] = {
            "repo": repo_name,
            "head": head_label,
            "head_subject": subject,
            "git_status": "clean (git status --porcelain empty at the recorded tip)",
            "command": "python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json",
            "note": (
                f"Baseline refreshed by refresh-corpus-baseline.py at {head_label} "
                f"({subject or '(no subject)'}) from the corpus gate's own --no-baseline --json "
                f"over a clean worktree, cross-checked class-for-class against the independent "
                f"re-derivation: {moved}{residual}{noted}. Expectations are re-recorded to observed "
                "committed bytes, never fitted to a denominator."
            ),
        }
        baseline.setdefault("notes", {})[args.note_key] = (
            f"round 79 C1 repair (corpus index + baseline) re-recorded at {head_label} "
            f"({subject or '(no subject)'}): {moved}{residual}{noted}. Index rows for every "
            "previously unindexed corpus file were committed first; the gate's own counts were "
            "observed afterwards, not before."
        )

        for check_id, old, new in changes:
            print(f"{check_id:<34s} {old} -> {new}")
        if not changes:
            print("no expectation moved")
        for check_id, now in carried_red:
            print(f"carried red: {check_id} observed {now}, expectation stays 0")

        if args.dry_run:
            print(f"dry-run: {baseline_path} untouched (head {head_label})")
            return 0

        baseline_path.write_text(
            json.dumps(baseline, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"wrote {baseline_path} (head {head_label})")

        # Post-condition: the re-recorded file reads green for every class it owns; a carried
        # residual is the only acceptable remaining drift.
        proc = run(
            [sys.executable, "-B", str(root / INTEGRITY), "--repo", str(root), "--json"], root
        )
        try:
            post = json.loads(proc.stdout)
        except json.JSONDecodeError:
            print(f"post-refresh: {INTEGRITY} did not emit JSON (exit {proc.returncode})")
            return 3
        rows = post.get("results") or []
        drift = [r["check"] for r in rows if r.get("verdict") == "DRIFT"]
        passed = len(rows) - len(drift)
        print(
            f"post-refresh: {passed}/{len(rows)} checks pass, exit {proc.returncode}"
            + (f", drift: {', '.join(drift)}" if drift else "")
        )
        unowned = [cid for cid in drift if cid not in dict(carried_red)]
        if unowned:
            print(f"post-refresh: drift this script does not own: {', '.join(unowned)}", file=sys.stderr)
            return 3

        ind = run([sys.executable, "-B", str(root / INDEPENDENT), "--repo", str(root)], root)
        last = (ind.stdout.strip().splitlines() or ["(no output)"])[-1]
        print(f"independent: exit {ind.returncode}; {last}")
        if ind.returncode not in (0, 1):
            return 3
        if ind.returncode == 1:
            # The baseline serves the integrity gate. A red re-derivation is reported loudly (its
            # exit status is the sum of its own zero-mode classes) but does not fail the write:
            # the caller's next step re-runs both gates and adjudicates the divergence, which is
            # also stamped into `measured_against.note` when the two instruments disagree.
            print(
                "independent: red (exit 1); it does not own this baseline, but the caller must "
                "adjudicate its residual before claiming a green corpus",
                file=sys.stderr,
            )
        return 0
    except Refused as exc:
        print(f"refresh-corpus-baseline: refused: {exc}", file=sys.stderr)
        return 2
    finally:
        if tmpdir is not None:
            if args.keep_temp:
                print(f"temp: {tmpdir}")
            else:
                for name in ("integrity.json", "integrity.err", "independent.json", "independent.err"):
                    try:
                        os.unlink(os.path.join(tmpdir, name))
                    except OSError:
                        pass
                try:
                    os.rmdir(tmpdir)
                except OSError:
                    pass


if __name__ == "__main__":
    sys.exit(main())
