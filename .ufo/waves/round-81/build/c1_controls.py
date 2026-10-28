#!/usr/bin/env python3
"""c1_controls.py -- C1 control worlds W0-W9 for kotoba round 81 (seat Kb81E06Controls).

WHAT THIS IS

``plans/round-81.md`` § C1 names ten control worlds that must be run on the
round-81 (E6-amended) tip-battery counter BEFORE any claim after-value is
measured.  Each world is a DO-NOTHING or SHORTCUT attempt; the control passes
only when the counter still reports red (exit 1) and, where the world injects a
specific corpus defect, the corpus gate's own detail line names that defect.

  W0  empty commit on the base tree        expect guards 5 of 5, `4 of 6`, exit 1
  W1  index+baseline repairs only          expect still red on report_dead/commit_unresolvable
  W2  R1 (report pointer/content) only     expect <=5 of 6, commit_unresolvable still red
  W3  R2 (verified external binding) only  expect <=5 of 6, report_dead still red
  W4  the two failing instruments stubbed  expect instrument-pin/instrument-size FAIL, exit 1
  W5  a base spot-check file edited        expect spotcheck-identity FAIL, exit 1
  W6  isolated-clone commit masked by      expect the token in commit_unresolvable_detail
      `owner/repo@<sha>`, no manifest row  (the r80 W8 killer class, Q75-strengthened)
  W7  a dead lane hash in a row carrying   expect the token in commit_unresolvable_detail
      the lane's own GitHub URL            (the r80 W9 killer class)
  W8  a seven-byte `marker` at the fleet   expect report_dead on the bare report token
      report path a lane symlink resolves  (the r80 W10 killer class)
  W9  a manifest entry whose evidence      expect the token in commit_unresolvable_detail
      receipt does not exist               (a manifest row alone never exempts)

WORLD SHAPE (port of the r80 c2_controls.py construction)

  1. ``D=<work>/<world>/fleet/kotoba-shokunin``; ``git -C D init -q``; identity
     ``scratch-r81`` / ``scratch@example.invalid``; ``git -C D rev-parse
     --show-toplevel`` must print ``D`` (a fixture outside its own repo is the
     classic way a damaged world writes into the caller's checkout).
  2. ``D/.git/objects/info/alternates`` names the base tree's object store
     (read-only sharing; the pinned base commit resolves inside the world).
  3. ``read-tree <base-rev>`` + ``checkout-index -a`` materialise the base tree;
     repair patches are applied with ``git -C D apply``; the world's fixture
     files are written next.
  4. ``git add -A`` (plus a forced add of every path a patch names),
     ``write-tree``, ``commit-tree -p <base-rev>`` and ``update-ref`` produce the
     measured commit.  The world is measured with
     ``python3 -B <counter> --repo D --rev <commit> --fleet <world>/fleet``.
  5. The fleet directory holds ``kotoba-shokunin`` (the world repo) plus every
     other entry of the real fleet as a read-only symlink, so report-pointer
     paths resolve exactly as in the lane; for W8 the ``.ufo/reports/...``
     ancestor of the marked report is mirrored as real directories and the
     marker file replaces the round-76 report.

THE LANE IS NEVER WRITTEN

``--base-tree`` is read only (``git -C`` inspection; alternates is a read-only
share).  Everything this script writes lives under ``--work`` (default: a fresh
directory under ``$TMPDIR``).  The real fleet root is only symlinked into the
worlds' fleet directories.

COUNTER UNDER TEST

``--counter`` is the counter file to run, verbatim, and its ``LINE_CAP`` /
``INSTRUMENT_PINS`` table are read back for the receipt.  The repair patches are
``--r1`` (verify_corpus_integrity.py report-pointer/content identity), ``--r2``
(verify_corpus_independent.py verified external binding), ``--manifest``
(verifiers/external-commits.json; folded into --r2 when the same patch adds it),
``--baseline`` (index + baseline refresh) and any number of ``--stack`` patches
applied to the full-stack worlds W6-W9.  A patch that does not apply is an
environment error, never a silent skip.

USAGE

  python3 -B .ufo/waves/round-81/build/c1_controls.py \\
      --counter .ufo/waves/round-81/build/check_tip_battery.amended.py \\
      --base-tree /fast/scratch/hyaku/kotoba-r81/Kb81E06Controls/base \\
      --r1 .ufo/waves/round-81/build/Kb81E01Integrity.patch \\
      --r2 .ufo/waves/round-81/build/Kb81E02Independent.patch \\
      --manifest .ufo/waves/round-81/build/Kb81E03ExtManifest.patch \\
      --baseline .ufo/waves/round-81/build/Kb81E04Baseline.patch \\
      --work /fast/scratch/hyaku/kotoba-r81/Kb81E06Controls/work \\
      --out .ufo/waves/round-81/build/c1_controls.txt

  --list          print the pre-registered expectation table and exit
  --only W0,W4    run only the named worlds
  --jobs N        worlds measured concurrently (default 3)
  --keep          keep the world repos (default: removed after the run)
  --verbose       echo the full counter output for every world
  --json          emit the machine-readable summary on stdout as JSON
  --out FILE      write the full receipt to FILE
  --label TEXT    stamp the receipt (e.g. "r80-proxy lower bound")
  --timeout N     per-world counter timeout in seconds (default 600)

Exit codes: 0 every measured world matched its pre-registration (skipped worlds
are named and counted); 1 at least one world diverged (a control went green is a
COUNTER DEFECT and is printed as such); 2 environment (no counter/base tree, a
patch that does not apply, a world that cannot be built).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
REAL_FLEET = Path("/home/vgpnk/Projects/shokunin")
BASE_REV = "b284223105f4d106f7e8f56ed4fd296c643cda0e"
STUB = "import sys\nsys.exit(0)\n"
GATE_INTEGRITY = "verifiers/verify_corpus_integrity.py"
GATE_INDEPENDENT = "verifiers/verify_corpus_independent.py"
SOURCES = "corpus/SOURCES.md"
SPOTCHECK = "corpus/lessons/round-72-verifier-spotcheck.md"   # latest base-file spot-check
MANIFEST = "verifiers/external-commits.json"
MARKER_REL = ".ufo/reports/round-76/kotoba.md"
MARKER_TOKEN = ".ufo/reports/round-76/kotoba.md"
MARKER_BYTES = b"marker\n"          # the seven-byte marker of the r80 W10 killer
LANE_URL = "https://github.com/kotoba-shokunin/kotoba-shokunin"


class EnvError(Exception):
    """The counter/base tree/world cannot be built: exit 2, never a verdict."""


# ------------------------------------------------------------------ helpers ---

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(repo: Path, *args: str, stdin: str | None = None) -> subprocess.CompletedProcess:
    """Every git call is -C'd at the world/base repo named here."""
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True, input=stdin)


def _must(proc: subprocess.CompletedProcess, what: str) -> str:
    if proc.returncode != 0:
        raise EnvError("%s failed (rc=%d): %s" % (what, proc.returncode,
                                                  (proc.stderr or proc.stdout).strip()))
    return proc.stdout


def assert_toplevel(repo: Path) -> None:
    proc = git(repo, "rev-parse", "--show-toplevel")
    got = proc.stdout.strip()
    if proc.returncode != 0 or os.path.realpath(got) != os.path.realpath(repo):
        raise EnvError("toplevel mismatch: git -C %s rev-parse --show-toplevel -> %r"
                       % (repo, got))


def objects_dir(repo: Path) -> Path:
    proc = git(repo, "rev-parse", "--path-format=absolute", "--git-path", "objects")
    if proc.returncode == 0 and proc.stdout.strip():
        return Path(proc.stdout.strip())
    dot = repo / ".git"
    if dot.is_dir():
        return dot / "objects"
    raise EnvError("cannot locate the object store of %s" % repo)


def patch_paths(patch: Path) -> list[str]:
    """Paths a unified diff names (b/ side), used for the forced staging."""
    paths: list[str] = []
    for line in patch.read_text(errors="replace").splitlines():
        m = re.match(r"^diff --git a/(\S+) b/(\S+)$", line)
        if m:
            paths.append(m.group(2))
    return paths


def apply_patch(repo: Path, patch: Path) -> None:
    proc = git(repo, "apply", "--whitespace=nowarn", str(patch))
    if proc.returncode != 0:
        raise EnvError("patch %s does not apply at %s: %s"
                       % (patch.name, repo, (proc.stderr or proc.stdout).strip()))


def write_file(repo: Path, rel: str, data: str | bytes) -> None:
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        path.unlink()
    mode = "wb" if isinstance(data, bytes) else "w"
    with open(path, mode) as fh:
        fh.write(data)


# ------------------------------------------------------------------ worlds ---

class Ctx:
    def __init__(self, work: Path, base_tree: Path, base_rev: str, patches: dict,
                 real_fleet: Path, timeout: int):
        self.work = work
        self.base_tree = base_tree
        self.base_rev = base_rev
        self.patches = patches          # role -> Path | None
        self.real_fleet = real_fleet
        self.timeout = timeout
        self.source_commit: str | None = None
        self.refresh: Path | None = None
        self.manifest_json: Path | None = None


def source_commit(ctx: Ctx, tag: str) -> str:
    """A real commit created in an isolated clone, absent from the lane and fleet.

    This is the r80 W8 construction: the object genuinely exists somewhere (so
    the world is not a synthetic hash), but the measured repo and the fleet both
    return 128 for it."""
    if ctx.source_commit:
        return ctx.source_commit
    src = ctx.work / ("source-" + tag)
    if src.exists():
        shutil.rmtree(src)
    src.mkdir(parents=True)
    proc = subprocess.run(["git", "init", "-q", str(src)], capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("cannot init the isolated source clone: %s" % proc.stderr.strip())
    assert_toplevel(src)
    for key, val in (("user.name", "scratch-r81"),
                     ("user.email", "scratch@example.invalid"),
                     ("commit.gpgsign", "false")):
        _must(git(src, "config", key, val), "source config " + key)
    write_file(src, "probe.txt", "isolated source probe\n")
    _must(git(src, "add", "-A"), "source add")
    _must(git(src, "commit", "-qm", "isolated source probe"), "source commit")
    ctx.source_commit = _must(git(src, "rev-parse", "HEAD"), "source rev-parse").strip()
    return ctx.source_commit


def mirror_with_marker(src: Path, dst: Path, parts: list[str]) -> None:
    """Mirror a directory as symlinks, except the marker chain, which becomes
    real directories ending in the seven-byte marker file."""
    dst.mkdir(parents=True, exist_ok=True)
    for entry in sorted(src.iterdir()):
        target = dst / entry.name
        if entry.name == parts[0] and len(parts) == 1:
            target.write_bytes(MARKER_BYTES)
        elif entry.name == parts[0]:
            mirror_with_marker(entry, target, parts[1:])
        else:
            try:
                target.symlink_to(entry)
            except FileExistsError:
                pass


def build_fleet(fleet: Path, real_fleet: Path, marker_rel: str | None) -> None:
    """A fleet-shaped directory: the world repo plus read-only links to the
    real fleet's other entries; with marker_rel, the .ufo ancestor chain of that
    report is real and the report itself is the seven-byte marker."""
    fleet.mkdir(parents=True, exist_ok=True)
    marker_parts = marker_rel.split("/") if marker_rel else None
    for entry in sorted(real_fleet.iterdir()):
        if entry.name in ("kotoba-shokunin", ".git"):
            continue
        target = fleet / entry.name
        if entry.name == ".ufo" and marker_parts is not None:
            if marker_parts[0] != ".ufo":
                raise EnvError("marker path must start with .ufo: %r" % marker_rel)
            mirror_with_marker(entry, target, marker_parts[1:])
        else:
            try:
                target.symlink_to(entry)
            except FileExistsError:
                pass


def build_world(name: str, ctx: Ctx, patch_roles: list[str], fixture,
                marker_rel: str | None) -> tuple[Path, Path, str, dict]:
    wdir = ctx.work / name
    if wdir.exists():
        shutil.rmtree(wdir)
    fleet = wdir / "fleet"
    repo = fleet / "kotoba-shokunin"
    (wdir / "tmp").mkdir(parents=True, exist_ok=True)
    repo.mkdir(parents=True)
    proc = subprocess.run(["git", "init", "-q", str(repo)], capture_output=True, text=True)
    if proc.returncode != 0:
        raise EnvError("world %s: git init failed: %s" % (name, proc.stderr.strip()))
    assert_toplevel(repo)
    for key, val in (("user.name", "scratch-r81"),
                     ("user.email", "scratch@example.invalid"),
                     ("commit.gpgsign", "false")):
        _must(git(repo, "config", key, val), "world config " + key)
    alt = repo / ".git" / "objects" / "info" / "alternates"
    alt.parent.mkdir(parents=True, exist_ok=True)
    alt.write_text(str(objects_dir(ctx.base_tree)) + "\n")

    _must(git(repo, "read-tree", ctx.base_rev), "world read-tree")
    _must(git(repo, "checkout-index", "-a", "-f"), "world checkout-index")

    touched: list[str] = []
    seen_patches: set[str] = set()
    for role in patch_roles:
        patch = ctx.patches.get(role)
        if patch is None:
            raise EnvError("world %s needs the %s patch, which was not supplied"
                           % (name, role))
        key = str(patch)
        if key in seen_patches:          # --r2 and --manifest may be one patch
            continue
        seen_patches.add(key)
        apply_patch(repo, patch)
        touched.extend(patch_paths(patch))

    if "manifest" in patch_roles and ctx.patches.get("manifest") is None:
        if ctx.manifest_json is None:
            raise EnvError("world %s needs the external-commits manifest (a patch "
                           "or --manifest-json)" % name)
        write_file(repo, MANIFEST, ctx.manifest_json.read_text())
        touched.append(MANIFEST)

    fixture(repo, ctx, wdir)
    diag: dict = {}

    def stage_and_commit(parent: str, message: str) -> str:
        _must(git(repo, "add", "-A"), "world add")
        for rel in sorted(set(touched)):
            if (repo / rel).exists() or (repo / rel).is_symlink():
                proc = git(repo, "add", "-f", "-A", "--", rel)
                if proc.returncode != 0:
                    raise EnvError("world %s: forced add of %s failed: %s"
                                   % (name, rel, proc.stderr.strip()))
        tree = _must(git(repo, "write-tree"), "world write-tree").strip()
        made = _must(git(repo, "commit-tree", tree, "-p", parent, "-m", message),
                     "world commit-tree").strip()
        _must(git(repo, "update-ref", "refs/heads/scratch-r81", made),
              "world update-ref")
        _must(git(repo, "symbolic-ref", "HEAD", "refs/heads/scratch-r81"),
              "world symbolic-ref")
        return made

    commit = stage_and_commit(ctx.base_rev, "control world %s" % name)
    if ctx.refresh is not None and "baseline" in patch_roles:
        env = dict(os.environ)
        env["TMPDIR"] = str(wdir / "tmp")
        try:
            rp = subprocess.run([sys.executable, "-B", str(ctx.refresh),
                                 "--repo", str(repo)],
                                capture_output=True, text=True, env=env,
                                cwd=str(repo), timeout=ctx.timeout)
            tail = [l for l in (rp.stdout or "").splitlines() if l.strip()]
            diag["refresh"] = {"exit": rp.returncode,
                               "last": tail[-1] if tail else "",
                               "stderr": (rp.stderr or "").strip()[-200:],
                               "at": commit}
        except subprocess.TimeoutExpired:
            diag["refresh"] = {"exit": None, "last": "timeout", "at": commit}
        if (repo / "verifiers/corpus-baseline.json").exists():
            commit = stage_and_commit(commit, "control world %s: baseline refresh" % name)
            diag["refresh"]["recommit"] = commit

    build_fleet(fleet, ctx.real_fleet, marker_rel)
    return wdir, repo, commit, diag


# ---------------------------------------------------------------- fixtures ---

def fx_none(repo: Path, ctx: Ctx, wdir: Path) -> None:
    return None


def fx_stub_instruments(repo: Path, ctx: Ctx, wdir: Path) -> None:
    for rel in (GATE_INTEGRITY, GATE_INDEPENDENT):
        write_file(repo, rel, STUB)


def fx_edit_spotcheck(repo: Path, ctx: Ctx, wdir: Path) -> None:
    path = repo / SPOTCHECK
    if not path.is_file():
        raise EnvError("spot-check fixture absent: %s" % SPOTCHECK)
    with open(path, "a") as fh:
        fh.write("\n<!-- control edit: spot-check identity world -->\n")


def _append_sources_row(repo: Path, row: str) -> None:
    path = repo / SOURCES
    if not path.is_file():
        raise EnvError("SOURCES fixture absent: %s" % SOURCES)
    text = path.read_text()
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + row + "\n")


def fx_marker_lane_commit(repo: Path, ctx: Ctx, wdir: Path) -> None:
    sha = source_commit(ctx, "w6")
    _append_sources_row(
        repo,
        "| S998 | Kotoba lane commit probe -- %s | docs | B | synthetic absent "
        "lane commit control, r81 W6 | commit `kotoba-shokunin/kotoba-shokunin@%s` | "
        "external-classification probe with no manifest row | mined | 2026-10-27 | "
        "90d | corpus/lessons/round-81.md |" % (LANE_URL, sha))


def fx_marker_lane_commit_bare(repo: Path, ctx: Ctx, wdir: Path) -> None:
    """Supplementary W6b: the same isolated-clone commit as a bare hex token
    (a real commit candidate) with an `owner/repo@` marker elsewhere in the row.
    This is the Q75 shape the E02 self-test pre-registers; W6 keeps the r80 W8
    literal shape (the marker inside the token)."""
    sha = source_commit(ctx, "w6")
    _append_sources_row(
        repo,
        "| S995 | Kotoba lane commit probe -- %s | docs | B | synthetic absent "
        "lane commit control, r81 W6b | commit `%s` | kotoba-shokunin/"
        "kotoba-shokunin@ marker with no manifest row | mined | 2026-10-27 | 90d | "
        "corpus/lessons/round-81.md |" % (LANE_URL, sha))


def fx_dead_lane_hash(repo: Path, ctx: Ctx, wdir: Path) -> None:
    sha = source_commit(ctx, "w6")
    _append_sources_row(
        repo,
        "| S997 | Kotoba lane GitHub probe -- %s | docs | B | synthetic absent "
        "lane commit control, r81 W7 | commit `%s` | lane-url external "
        "classification probe with no manifest row | mined | 2026-10-27 | 90d | "
        "corpus/lessons/round-81.md |" % (LANE_URL, sha))


def fx_marker_fleet(repo: Path, ctx: Ctx, wdir: Path) -> None:
    """Cite the marked report through the lane's own relative symlink.

    The corpus's checked report tokens resolve from the citing file's directory,
    then from the fleet root; a bare `.ufo/reports/...` token can never reach the
    measured tree.  The r80 W10 shape is a token whose relative path lands on the
    lane's `.ufo/reports/round-76/kotoba.md` symlink, which resolves to the fleet
    path the world marks.  `corpus/lessons/` -> repo root is two hops."""
    lesson = repo / "corpus/lessons/round-79.md"
    if not lesson.is_file():
        raise EnvError("citation fixture absent: corpus/lessons/round-79.md")
    with open(lesson, "a") as fh:
        fh.write("\nControl report pointer: `../../.ufo/reports/round-76/kotoba.md`\n")


def fx_manifest_missing_evidence(repo: Path, ctx: Ctx, wdir: Path) -> None:
    sha = source_commit(ctx, "w6")
    path = repo / MANIFEST
    if not path.is_file():
        raise EnvError("no %s after the stacked patches: the verified-binding "
                       "mechanism is absent" % MANIFEST)
    try:
        data = json.loads(path.read_text())
    except ValueError as exc:
        raise EnvError("%s is not JSON: %s" % (MANIFEST, exc))
    if isinstance(data, dict):
        rows = data.get("commits")
        if not isinstance(rows, list):
            raise EnvError("%s has no commits list" % MANIFEST)
        container = data
    elif isinstance(data, list):
        rows = data
        container = None
    else:
        raise EnvError("%s is neither a list nor an object" % MANIFEST)
    rows.append({
        "hash": sha,
        "repo": "example/example",
        "evidence": ".ufo/waves/round-81/snapshots/DOES-NOT-EXIST.json",
        "pinned_at": "2026-10-27T00:00:00Z",
    })
    if container is not None:
        container["commits"] = rows
        path.write_text(json.dumps(container, indent=2) + "\n")
    else:
        path.write_text(json.dumps(rows, indent=2) + "\n")
    _append_sources_row(
        repo,
        "| S996 | Manifest evidence probe -- %s | docs | B | synthetic absent "
        "lane commit control, r81 W9 | commit `%s` | manifest row whose evidence "
        "receipt is absent | mined | 2026-10-27 | 90d | corpus/lessons/round-81.md |"
        % (LANE_URL, sha))


# ------------------------------------------------------- pre-registrations ---

def _w(name, title, roles, fixture, marker, checks):
    return dict(name=name, title=title, roles=roles, fixture=fixture,
                marker=marker, checks=checks)


WORLDS = [
    _w("W0", "empty commit on the base tree", [], fx_none, None, dict(
        exit_code=1,
        must=["guard no-deletions PASS", "guards 5 of 5",
              "tip battery exit 0: 4 of 6"],
        detail=[],
        note="the base predicate: 4 of 6, guards hold, exit 1")),
    _w("W1", "index+baseline repairs only (no instrument repair)", ["baseline"],
       fx_none, None, dict(
        exit_code=1,
        must=["guards 5 of 5", "tip battery exit 0: 4 of 6"],
        must_not=[],
        detail=[("integrity", "report_dead", ("gt", 0)),
                ("integrity", "commit_unresolvable", ("gt", 0)),
                ("independent", "commit_unresolvable", ("gt", 0))],
        note="proves R1+R2 are load-bearing: the zero classes stay red")),
    _w("W2", "R1 (report pointer + content identity) only", ["r1"], fx_none, None, dict(
        exit_code=1,
        must=["guards 5 of 5"],
        must_not=["tip battery exit 0: 6 of 6"],
        detail=[],
        note="<=5 of 6: the published E01 artifact bundles both repairs for the "
             "integrity gate, so this world is gate-scoped (integrity green, "
             "independent still red); the plan's own criterion is the <=5")),
    _w("W3", "R2 (verified external binding) only", ["r2"], fx_none, None, dict(
        exit_code=1,
        must=["guards 5 of 5"],
        must_not=["tip battery exit 0: 6 of 6"],
        detail=[("integrity", "report_dead", ("gt", 0))],
        note="<=5 of 6 and the report-pointer class is still red")),
    _w("W4", "the two failing instruments stubbed to sys.exit(0)", [], fx_stub_instruments,
       None, dict(
        exit_code=1,
        must=["FAIL guard instrument-size", "FAIL guard instrument-pin"],
        must_not=[],
        detail=[],
        note="the anti-laundering load: the pin/size guards, not the battery line")),
    _w("W5", "a base spot-check file edited", [], fx_edit_spotcheck, None, dict(
        exit_code=1,
        must=["FAIL guard spotcheck-identity"],
        must_not=[],
        detail=[],
        note="a base spot-check may not be edited at the tip")),
    _w("W6", "isolated-clone commit masked by owner/repo@, no manifest row",
       ["r1", "r2", "manifest", "baseline"], fx_marker_lane_commit, None, dict(
        exit_code=1,
        must=[],
        must_not=[],
        detail=[("commit", ("commit_unresolvable_detail",
                            "commit_nonhash_detail"), ("sha", "<source>"))],
        note="the r80 W8 killer class: a marker alone never exempts (the token "
             "must land in a zero class, unresolvable or nonhash)")),
    _w("W7", "dead lane hash in a row carrying the lane's own GitHub URL",
       ["r1", "r2", "manifest", "baseline"], fx_dead_lane_hash, None, dict(
        exit_code=1,
        must=[],
        must_not=[],
        detail=[("commit", ("commit_unresolvable_detail",), ("sha", "<source>"))],
        note="the r80 W9 killer class: a lane URL is not a third repository")),
    _w("W8", "seven-byte marker at the fleet report the lane symlink resolves to",
       ["r1", "r2", "manifest", "baseline"], fx_marker_fleet, MARKER_REL, dict(
        exit_code=1,
        must=[],
        must_not=[],
        detail=[("commit", ("report_dead_detail",), ("substr", MARKER_TOKEN))],
        note="the r80 W10 killer class: a resolved path must still be a report")),
    _w("W9", "manifest row whose evidence receipt does not exist",
       ["r1", "r2", "manifest", "baseline"], fx_manifest_missing_evidence, None, dict(
        exit_code=1,
        must=[],
        must_not=[],
        detail=[("commit", ("commit_unresolvable_detail",), ("sha", "<source>"))],
        note="a manifest row alone never exempts; the receipt must be committed")),
    _w("W6b", "isolated-clone commit as a bare hex token, owner/repo@ in the row",
       ["r1", "r2", "manifest", "baseline"], fx_marker_lane_commit_bare, None, dict(
        exit_code=1,
        must=[],
        must_not=[],
        detail=[("commit", ("commit_unresolvable_detail",), ("sha", "<source>"))],
        note="supplementary (not in the plan's W0-W9 list): the Q75 bare-token "
             "shape, expected red as commit_unresolvable")),
]


WORLD_BY_NAME = {w["name"]: w for w in WORLDS}


# ------------------------------------------------------------------- runner ---

def run_counter(ctx: Ctx, counter: Path, repo: Path, commit: str, fleet: Path,
                tmpdir: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["TMPDIR"] = str(tmpdir)
    cmd = [sys.executable, "-B", str(counter), "--repo", str(repo),
           "--rev", commit, "--fleet", str(fleet)]
    return subprocess.run(cmd, capture_output=True, text=True, env=env,
                          timeout=ctx.timeout, cwd=str(repo))


def _flatten(data: dict) -> tuple[dict, dict]:
    """Normalise both corpus gates' JSON: counts and *_detail lists.

    integrity: {"observed": {"corpus": {...}}}
    independent: {"observed": {"commits": {...}, "pointers": {...}, "index": {...}}}
    """
    counts: dict = {}
    details: dict = {}
    observed = data.get("observed") if isinstance(data, dict) else None
    if isinstance(observed, dict):
        sections = []
        if isinstance(observed.get("corpus"), dict):
            sections.append(observed["corpus"])
        else:
            sections.append(observed)
        for sec in sections:
            stack = [sec]
            while stack:
                cur = stack.pop()
                for key, value in cur.items():
                    if isinstance(value, dict):
                        stack.append(value)
                    elif isinstance(value, list):
                        details.setdefault(key, value)
                    else:
                        counts.setdefault(key, value)
    return counts, details


def run_gate_json(ctx: Ctx, repo: Path, script: str, tmpdir: Path) -> dict:
    env = dict(os.environ)
    env["TMPDIR"] = str(tmpdir)
    argv = [sys.executable, "-B", str(repo / script), "--repo", str(repo), "--json"]
    if script == GATE_INTEGRITY:
        argv.append("--no-baseline")
    try:
        proc = subprocess.run(argv, capture_output=True, text=True, env=env,
                              timeout=ctx.timeout, cwd=str(repo))
    except subprocess.TimeoutExpired:
        return {"exit": None, "counts": {}, "details": {}, "error": "timeout"}
    text = proc.stdout.strip()
    start = text.find("{")
    if start < 0:
        return {"exit": proc.returncode, "counts": {}, "details": {},
                "error": "no JSON on stdout (exit %s): %s"
                         % (proc.returncode, (proc.stderr or text).strip()[-200:])}
    try:
        raw = json.loads(text[start:])
    except ValueError as exc:
        return {"exit": proc.returncode, "counts": {}, "details": {},
                "error": "unparsable JSON: %s" % exc}
    counts, details = _flatten(raw)
    return {"exit": proc.returncode, "counts": counts, "details": details,
            "error": None}


def _probe_counts(data: dict) -> dict:
    counts = data.get("counts", {})
    out = {k: counts.get(k) for k in ("report_dead", "commit_unresolvable",
                                      "commit_nonhash", "commit_external",
                                      "commit_total", "report_total")}
    out.update({"exit": data.get("exit"), "error": data.get("error")})
    return out


def detail_hit(data: dict, detail_keys, kind: str, needle: str) -> dict:
    out = {}
    present = False
    for key in detail_keys:
        detail = data.get("details", {}).get(key)
        if not isinstance(detail, list):
            out[key] = {"present": False, "error": data.get("error", "no detail list")}
            continue
        hit = [d for d in detail if needle and needle in d]
        present = present or bool(hit)
        out[key] = {"present": bool(hit), "hits": hit[:3], "count": len(detail)}
    out["any"] = present
    return out


def evaluate(observed: dict, world: dict, ctx: Ctx) -> tuple[bool, list[str]]:
    """Apply the pre-registration.  A world whose secret is gone (counter exit 0
    or the frozen 6 of 6 with exit 0) is a COUNTER DEFECT, named as such."""
    reasons: list[str] = []
    checks = world["checks"]
    if observed["exit"] != checks["exit_code"]:
        reasons.append("exit %s != expected %s"
                       % (observed["exit"], checks["exit_code"]))
    for needle in checks.get("must", []):
        if needle not in observed["stdout"]:
            reasons.append("missing counter line: %r" % needle)
    for needle in checks.get("must_not", []):
        if needle in observed["stdout"]:
            reasons.append("forbidden counter line present: %r" % needle)

    probes = observed.get("probe", {})
    full = observed.get("probe_full", {})
    for _key, detail_keys, spec in checks.get("detail", []):
        kind, needle = spec
        if kind == "gt":
            value = probes.get(_key, {}).get(detail_keys)
            if not isinstance(value, int):
                reasons.append("detail %s not an integer: %r (gate %s: %s)"
                               % (detail_keys, value, _key,
                                  probes.get(_key, {}).get("error")))

            elif not value > needle:
                reasons.append("detail %s == %r, expected > %r (gate %s)"
                               % (detail_keys, value, needle, _key))
            continue
        if needle == "<source>":
            needle = ctx.source_commit or ""
        hits = {g: detail_hit(full.get(g, {}), detail_keys, kind, needle)
                for g in ("integrity", "independent")}
        observed.setdefault("detail", {})["|".join(detail_keys)] = hits
        if not any(v.get("any") for v in hits.values()):
            reasons.append("detail %s does not name the world's token/class in "
                           "either corpus gate: %s"
                           % ("|".join(detail_keys), json.dumps(hits)[:400]))
    return (not reasons), reasons


def measure_world(world: dict, ctx: Ctx, counter: Path) -> dict:
    name = world["name"]
    rec: dict = {"name": name, "title": world["title"], "status": "ERROR",
                 "reasons": [], "stdout": "", "stderr": "", "exit": None}
    try:
        wdir = None
        wdir, repo, commit, diag = build_world(name, ctx, world["roles"],
                                               world["fixture"], world["marker"])
        rec["diag"] = diag
        rec["repo"] = str(repo)
        rec["commit"] = commit
        tmpdir = wdir / "tmp"
        tmpdir.mkdir(exist_ok=True)
        rec["tmpdir"] = tmpdir
        cmd = [sys.executable, "-B", str(counter), "--repo", str(repo),
               "--rev", commit, "--fleet", str(wdir / "fleet")]
        rec["command"] = " ".join(cmd)
        if world["marker"]:
            resolved = os.path.realpath(repo / world["marker"])
            want = os.path.realpath(wdir / "fleet" / world["marker"])
            data = Path(resolved).read_bytes() if Path(resolved).is_file() else b""
            rec["marker_check"] = {"resolved": resolved, "expected": want,
                                   "bytes": len(data), "is_marker": data == MARKER_BYTES}
            if resolved != want or data != MARKER_BYTES:
                raise EnvError("marker fixture did not land: %s" % rec["marker_check"])
        proc = run_counter(ctx, counter, repo, commit, wdir / "fleet", tmpdir)
        rec["stdout"], rec["stderr"] = proc.stdout, proc.stderr
        rec["exit"] = proc.returncode
        full = {
            "integrity": run_gate_json(ctx, repo, GATE_INTEGRITY, tmpdir),
            "independent": run_gate_json(ctx, repo, GATE_INDEPENDENT, tmpdir),
        }
        rec["probe_full"] = full
        rec["probe"] = {g: _probe_counts(v) for g, v in full.items()}
        ok, reasons = evaluate(rec, world, ctx)
        rec["reasons"] = reasons
        rec["status"] = "PASS" if ok else "FAIL"
        last = [l for l in proc.stdout.splitlines() if l.strip()]
        rec["last_line"] = last[-1] if last else ""
        if rec["exit"] == 0:
            rec["defect"] = ("COUNTER DEFECT: the control world reached the claim "
                             "target (counter exit 0)")
    except subprocess.TimeoutExpired:
        rec["status"] = "ERROR"
        rec["reasons"] = ["counter timed out after %d s" % ctx.timeout]
    except EnvError as exc:
        rec["status"] = "ERROR"
        rec["reasons"] = [str(exc)]
    except Exception as exc:                    # a harness bug is still an error
        rec["status"] = "ERROR"
        rec["reasons"] = ["%s: %s" % (type(exc).__name__, exc),
                          traceback.format_exc()[-600:]]
    finally:
        if wdir is not None and not ctx.keep:
            shutil.rmtree(wdir, ignore_errors=True)
    return rec


# --------------------------------------------------------------------- main ---

def counter_meta(counter: Path) -> dict:
    text = counter.read_text(errors="replace")
    cap = re.search(r"^LINE_CAP = (\d+)", text, re.M)
    pins = re.findall(r'^\s{4}"(verifiers/[^"]+)":\s*\(', text, re.M)
    return {"path": str(counter), "sha256": sha256(counter),
            "bytes": counter.stat().st_size,
            "line_cap": int(cap.group(1)) if cap else None,
            "pin_files": pins,
            "base_constant": (re.search(r'^BASE = "([0-9a-f]+)"', text, re.M) or [None, None])[1]}


def patch_meta(ctx: Ctx) -> list[dict]:
    rows = []
    for role, path in sorted(ctx.patches.items()):
        if path is None:
            continue
        rows.append({"role": role, "path": str(path), "sha256": sha256(path),
                     "bytes": path.stat().st_size})
    return rows


def print_table() -> None:
    print("pre-registered expectation table (plans/round-81.md § C1)")
    for w in WORLDS:
        ch = w["checks"]
        print("  %-3s %-58s roles=%s exit=%s must=%s detail=%s"
              % (w["name"], w["title"], ",".join(w["roles"]) or "-",
                 ch["exit_code"], ch.get("must") or "-",
                 ch.get("detail") or "-"))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="C1 control worlds W0-W9 (kotoba round 81)")
    ap.add_argument("--counter", required=False)
    ap.add_argument("--base-tree", required=False)
    ap.add_argument("--base-rev", default=BASE_REV)
    ap.add_argument("--work")
    ap.add_argument("--r1")
    ap.add_argument("--r2")
    ap.add_argument("--manifest")
    ap.add_argument("--baseline")
    ap.add_argument("--refresh", help="refresh-corpus-baseline.py run inside the "
                                      "baseline-bearing worlds before the commit")
    ap.add_argument("--manifest-json", help="candidate verifiers/external-commits.json "
                                            "content, committed in the worlds when no "
                                            "manifest patch is supplied")
    ap.add_argument("--stack", action="append", default=[],
                    help="extra repair patch applied to the full-stack worlds W6-W9")
    ap.add_argument("--real-fleet", default=str(REAL_FLEET))
    ap.add_argument("--only")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out")
    ap.add_argument("--label", default="")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args(argv)

    if args.list:
        print_table()
        return 0
    if not args.counter:
        print("c1_controls: --counter is required (see --list)", file=sys.stderr)
        return 2
    if not args.base_tree:
        print("c1_controls: --base-tree is required (see --list)", file=sys.stderr)
        return 2

    counter = Path(args.counter).resolve()
    base_tree = Path(args.base_tree).resolve()
    if not counter.is_file():
        print("c1_controls: no counter at %s" % counter, file=sys.stderr)
        return 2
    if not base_tree.is_dir():
        print("c1_controls: no base tree at %s" % base_tree, file=sys.stderr)
        return 2
    rev = git(base_tree, "rev-parse", "--verify", "--quiet", args.base_rev + "^{commit}")
    if rev.returncode != 0:
        print("c1_controls: base revision %s is not in %s" % (args.base_rev, base_tree),
              file=sys.stderr)
        return 2
    base_rev = rev.stdout.strip()

    if args.work:
        work = Path(args.work).resolve()
        work.mkdir(parents=True, exist_ok=True)
    else:
        work = Path(tempfile.mkdtemp(prefix="c1-controls-",
                                     dir=os.environ.get("TMPDIR") or None))
    (work / "tmp").mkdir(exist_ok=True)

    patches: dict = {}
    for role, value in (("r1", args.r1), ("r2", args.r2),
                        ("manifest", args.manifest), ("baseline", args.baseline)):
        patches[role] = Path(value).resolve() if value else None
    for i, value in enumerate(args.stack):
        patches["stack%d" % i] = Path(value).resolve()
    for role, path in patches.items():
        if path is not None and not path.is_file():
            print("c1_controls: %s patch not found: %s" % (role, path), file=sys.stderr)
            return 2
    if patches.get("manifest") is None:
        for role in ("r2", "r1"):        # either repair may carry the manifest file
            cand = patches.get(role)
            if cand is not None and MANIFEST in patch_paths(cand):
                patches["manifest"] = cand           # the same patch adds the manifest
                break

    ctx = Ctx(work, base_tree, base_rev, patches, Path(args.real_fleet).resolve(),
              args.timeout)
    ctx.keep = args.keep
    if args.manifest_json:
        ctx.manifest_json = Path(args.manifest_json).resolve()
        if not ctx.manifest_json.is_file():
            print("c1_controls: no manifest json at %s" % ctx.manifest_json,
                  file=sys.stderr)
            return 2
    if args.refresh:
        ctx.refresh = Path(args.refresh).resolve()
        if not ctx.refresh.is_file():
            print("c1_controls: no refresh script at %s" % ctx.refresh, file=sys.stderr)
            return 2

    selected = list(WORLDS)
    if args.only:
        names = [n.strip().upper() for n in args.only.split(",") if n.strip()]
        upper = {w["name"].upper(): w for w in WORLDS}
        unknown = [n for n in names if n not in upper]
        if unknown:
            print("c1_controls: unknown world(s): %s" % ",".join(unknown), file=sys.stderr)
            return 2
        selected = [upper[n] for n in names]

    # skipped worlds are named, never silently dropped
    runnable, skipped = [], []
    for w in selected:
        missing = [r for r in w["roles"] if ctx.patches.get(r) is None
                   and not (r == "manifest" and ctx.manifest_json is not None)]
        if missing:
            skipped.append({"name": w["name"], "title": w["title"],
                            "missing_patches": missing})
        else:
            runnable.append(w)

    results: list[dict] = []
    if runnable:
        with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
            futures = [(w, pool.submit(measure_world, w, ctx, counter)) for w in runnable]
            for w, fut in futures:
                results.append(fut.result())
    for rec in skipped:
        rec["status"] = "SKIPPED"

    meta = counter_meta(counter)
    lines: list[str] = []
    lines.append("c1_controls.py -- C1 control worlds W0-W9, kotoba round 81 (Kb81E06Controls)")
    lines.append("generated: %s" % __import__("datetime").datetime.now().isoformat(timespec="seconds"))
    if args.label:
        lines.append("label: %s" % args.label)
    lines.append("base rev: %s (base tree %s)" % (base_rev, base_tree))
    lines.append("counter: %s  sha256 %s  bytes %d  LINE_CAP %s  BASE %s"
                 % (meta["path"], meta["sha256"], meta["bytes"],
                    meta["line_cap"], meta["base_constant"]))
    lines.append("counter pin files: %s" % (", ".join(meta["pin_files"]) or "-"))
    for row in patch_meta(ctx):
        lines.append("patch %-9s %s  sha256 %s  bytes %d"
                     % (row["role"], row["path"], row["sha256"], row["bytes"]))
    if ctx.manifest_json is not None:
        lines.append("manifest json (world fixture): %s  sha256 %s"
                     % (ctx.manifest_json, sha256(ctx.manifest_json)))
    if ctx.refresh is not None:
        lines.append("baseline refresh: %s  sha256 %s"
                     % (ctx.refresh, sha256(ctx.refresh)))
    lines.append("real fleet (read-only link source): %s" % ctx.real_fleet)
    lines.append("work dir: %s" % ctx.work)
    lines.append("")

    for rec in results:
        lines.append("=" * 78)
        lines.append("== %s %s" % (rec["name"], rec["title"]))
        lines.append("repo: %s" % rec.get("repo", "-"))
        lines.append("commit: %s" % rec.get("commit", "-"))
        if rec.get("command"):
            lines.append("command: %s" % rec["command"])
        lines.append("--- counter stdout ---")
        lines.extend((rec["stdout"] or "").rstrip("\n").splitlines())
        lines.append("--- counter stderr ---")
        lines.extend((rec["stderr"] or "").rstrip("\n").splitlines())
        lines.append("--- observed ---")
        lines.append("exit: %s" % rec["exit"])
        lines.append("frozen line: %s" % rec.get("last_line", ""))
        if rec.get("diag"):
            lines.append("world diag: %s" % json.dumps(rec["diag"], sort_keys=True))
        if rec.get("marker_check"):
            lines.append("marker: %s" % json.dumps(rec["marker_check"], sort_keys=True))
        if rec.get("probe"):
            lines.append("gate probes: %s" % json.dumps(rec["probe"], sort_keys=True))
        if rec.get("detail"):
            lines.append("detail hits: %s" % json.dumps(rec["detail"], sort_keys=True))
        lines.append("expected: exit %s; %s" % (
            WORLD_BY_NAME[rec["name"]]["checks"]["exit_code"],
            "; ".join(WORLD_BY_NAME[rec["name"]]["checks"].get("must") or []) or
            WORLD_BY_NAME[rec["name"]]["checks"].get("note", "")))
        lines.append("status: %s" % rec["status"])
        for reason in rec["reasons"]:
            lines.append("  reason: %s" % reason)
        if rec.get("defect"):
            lines.append("  %s" % rec["defect"])
        lines.append("")

    for rec in skipped:
        lines.append("== %s %s" % (rec["name"], rec["title"]))
        lines.append("status: SKIPPED (missing patches: %s)"
                     % ", ".join(rec["missing_patches"]))
        lines.append("")

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = [r for r in results if r["status"] == "FAIL"]
    errored = [r for r in results if r["status"] == "ERROR"]
    summary = ("summary: %d measured, %d PASS, %d FAIL, %d ERROR, %d SKIPPED"
               % (len(results), passed, len(failed), len(errored), len(skipped)))
    lines.append(summary)
    for rec in failed:
        lines.append("FAIL %s: %s" % (rec["name"], "; ".join(rec["reasons"])[:400]))
    for rec in errored:
        lines.append("ERROR %s: %s" % (rec["name"], "; ".join(rec["reasons"])[:400]))
    text = "\n".join(lines) + "\n"

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
    if args.verbose or args.json:
        if args.json:
            payload = {"counter": meta, "patches": patch_meta(ctx),
                       "base_rev": base_rev, "results": results, "skipped": skipped,
                       "summary": summary}
            print(json.dumps(payload, indent=2, sort_keys=True))
        else:
            print(text)
    elif not args.out:
        print(text)
    else:
        print(summary)

    return 0 if not failed and not errored else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
