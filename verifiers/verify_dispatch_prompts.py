#!/usr/bin/env python3
"""verify_dispatch_prompts.py -- machine check for the two executable
dispatch-prompt checklist boxes of SKILL.md.

The claim under test: the prose boxes ``dispatch.04`` (report path is literal
and its file name is the lane's id) and ``dispatch.08`` (round token is
identical across file name, role line and report dir, and is at most the
lane's latest dispatched round) are *executed* over a directory of dispatch
prompts -- not merely attested in prose.

Scope and model
---------------
* The scan is non-recursive over the prompts directory root.  Subdirectories
  (the fleet's ``closure/`` tree) are out of scope and are reported.
* A prompt file's *lane id* is the stem prefix of its name:
  ``<lane>-round-<N>.md`` and ``<lane>-L1.md``.  Any other name is out of
  scope for both boxes and is listed with a reason.
* dispatch.04 conjuncts, per in-scope file:
  - ``report_path_literal`` -- the report path carries no ``<...>``
    placeholder and no unsubstituted ``${...}`` / ``$VAR``.
  - ``report_stem_is_lane_id`` -- the report path's file stem is the lane id.
  - ``lane_identity_known`` -- the lane id names a lane this fleet knows:
    a ``<fleet>/<id>-shokunin`` repository, or a ``<state-dir>/<id>.round``
    / ``<state-dir>/<id>.report-baseline`` state file.
  Only the *report path* is scanned for placeholders: an L0 ``<lane> |
  round-<N>`` template or a command template elsewhere in the body does not
  trip the box.
* dispatch.08 conjuncts, per ``<lane>-round-<N>.md`` file:
  - ``filename_role_round_equal`` -- the role line's round is N.
  - ``filename_report_dir_round_equal`` -- the report path's round dir is N.
  - ``round_le_latest_dispatched`` -- N is at most the lane's latest
    dispatched round, read as the first whitespace field of
    ``<state-dir>/<lane>.report-baseline`` (the hyaku driver's record).  A
    lane that still has only the legacy ``<state-dir>/<lane>.round`` file
    (frozen since 2026-10-15) is reported ``state-stale`` and *not
    compared*; a lane with neither file is N/A.  A missing state source is
    never a pass.

Verdicts
--------
Every conjunct carries its own status (PASS / FAIL / N/A).  A file's verdict
is FAIL if any conjunct FAILs, else N/A if any conjunct is N/A, else PASS.
A check's verdict is FAIL if any file FAILs, else N/A if no file is PASS,
else PASS.  Every check prints ``evaluated N``; ``N == 0`` is never a PASS.

Exit codes: 0 all selected checks PASS; 1 a check FAILed; 2 usage or
substrate error (missing/unreadable directory or map).  Read-only; stdlib
only; deterministic.

The box proof (``--box-proof``)
-------------------------------
``--box-proof`` proves, for each of the two boxes, that the checklist map
delegates the box to this instrument, that the live ``SKILL.md`` box text
still hashes to the constant pinned in this file, and that the committed
fixtures discriminate every one of the six *named* conjuncts --
``report_path_literal``, ``report_stem_is_lane_id``, ``lane_identity_known``,
``filename_role_round_equal``, ``filename_report_dir_round_equal`` and
``round_le_latest_dispatched`` -- one must-fail fixture case each.  The
coverage is read from the *observed* conjunct statuses, not from the case's
``expect_conjunct`` label: a conjunct is covered when some must-fail case
fails on it and on no conjunct outside the one co-failure pinned in
``ALLOWED_CO_FAIL``.  The conjunct list is the constant ``CONJUNCTS``,
next to the pinned box hashes, never read from the manifest, so deleting a
must-fail case from the manifest leaves its conjunct uncovered: the box is
not counted, the uncovered conjunct is named, and the run exits 1.

Each box also needs a must-pass control case whose observed conjuncts are
all PASS, and dispatch.08 needs a case whose observed
``round_le_latest_dispatched`` is N/A (a missing state source is never a
pass).  A missing fixture directory or an unreadable fixture file is a
substrate error: a problem line and exit 2, never a traceback.

The bound of that claim: the fixtures discriminate the six named conjuncts,
one must-fail case each.  The box clauses *without* a fixture -- the
unsubstituted variable (``${...}`` / ``$VAR``), ``<=`` at equality with the
lane's latest dispatched round, the legacy-state arm (``state-stale``) and a
non-digit round folder -- are **not** proven by this instrument.
"""

import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parent.parent
VERIFIERS_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = VERIFIERS_DIR / "fixtures" / "dispatch-prompts"
BASELINE_NAME = "checklist-baseline.json"
SKILL_NAME = "SKILL.md"

DEFAULT_PROMPTS = Path("/home/vgpnk/Projects/shokunin/.ufo/prompts")
DEFAULT_STATE_DIR = Path("/home/vgpnk/Projects/shokunin/.ufo/state")
DEFAULT_FLEET = Path("/home/vgpnk/Projects/shokunin")

CHECK_IDS = ("dispatch.04", "dispatch.08")
DELEGATION_TARGET = "verifiers/verify_dispatch_prompts.py"

# The box texts this instrument executes, pinned by the sha256 of their
# normalised checklist text (the kotoba-checklist-v1 normalisation rule:
# first line minus the '- [ ]' marker plus the stripped continuation lines,
# joined with one space, whitespace runs collapsed to one space, stripped,
# UTF-8 sha256).  A reworded box no longer matches its pin, so the proof
# below fails loudly instead of silently executing a different box.
PINNED_BOX_SHA = {
    "dispatch.04": "62c20a8110515010d560d29526d22765b095594da1407340bed76f5e21040515",
    "dispatch.08": "f5c37baa2ca839ea8dd091f3f42f091db0715e1f6a755e5ae894e48c79cd46d2",
}

# The named conjuncts of each box, pinned here next to the box text hashes
# and never derived from the fixture manifest.  The box proof requires one
# isolated must-fail fixture case per named conjunct, so deleting a case
# from the manifest leaves its conjunct uncovered and the box unproven -- a
# deleted case cannot delete its own expectation, because the expectation
# lives in this constant and not in the manifest.
CONJUNCTS = {
    "dispatch.04": ("report_path_literal", "report_stem_is_lane_id",
                    "lane_identity_known"),
    "dispatch.08": ("filename_role_round_equal",
                    "filename_report_dir_round_equal",
                    "round_le_latest_dispatched"),
}

# The one co-failure the fixture corpus is allowed: a report path's
# placeholder sits inside the file stem, so a case that proves
# report_path_literal also fails report_stem_is_lane_id.  No other pairing
# is allowed, in either direction.
ALLOWED_CO_FAIL = {"report_path_literal": frozenset({"report_stem_is_lane_id"})}

# The clause a missing state source must show: N/A, never a pass.
NA_ARM_CONJUNCT = "round_le_latest_dispatched"

ROUND_FILE_RE = re.compile(r"^(?P<lane>.+)-round-(?P<round>\d+)\.md$")
L1_FILE_RE = re.compile(r"^(?P<lane>.+)-L1\.md$")
# A report path: '.ufo/reports/round-<N>/<stem>', absolute or relative.
REPORT_PATH_RE = re.compile(r"\.ufo/reports/round-(\d+)/([^\s`'\"()\[\]]+)")
# The role line's round token: the first 'round <digits>' on line 1.
ROLE_ROUND_RE = re.compile(r"\bround\s+(\d+)\b")
PLACEHOLDER_RE = re.compile(r"<[^<>]*>")
VARIABLE_RE = re.compile(r"\$\{[^}]*\}|\$[A-Za-z_][A-Za-z0-9_]*")

DISPOSITION_RE = re.compile(r"^(executed|delegated|unexecuted):(.+)$")


class EnvError(Exception):
    """A substrate the run needs is missing or unreadable."""


# ---------------------------------------------------------------------------
# extraction helpers
# ---------------------------------------------------------------------------

def read_text(path: Path, what: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise EnvError("%s: %s (%s)" % (path, exc.strerror or exc, what))


def lane_of(name: str) -> tuple[str | None, int | None, str | None]:
    """(lane id, round, kind) for a prompt file name; kind is None if the name
    is not a dispatch-prompt name at all."""
    m = ROUND_FILE_RE.match(name)
    if m:
        return m.group("lane"), int(m.group("round")), "round"
    m = L1_FILE_RE.match(name)
    if m:
        return m.group("lane"), None, "l1"
    return None, None, None


def report_paths(text: str) -> list[tuple[int, str]]:
    """(round dir, file stem) for every report path in the text.

    A mention of the reports *directory* ('.ufo/reports/round-4/') carries no
    file stem and is not a report path; a stem is kept only when it names a
    file (trailing sentence punctuation is stripped)."""
    out = []
    for m in REPORT_PATH_RE.finditer(text):
        stem = m.group(2).rstrip(".,;:")
        if not stem or stem in (".", ".."):
            continue
        if stem.endswith(".md"):
            stem = stem[:-3]
        out.append((int(m.group(1)), stem))
    return out


def role_round(text: str) -> int | None:
    """The round token of the role line (line 1), or None when absent."""
    lines = text.splitlines()
    if not lines:
        return None
    m = ROLE_ROUND_RE.search(lines[0])
    return int(m.group(1)) if m else None


def has_placeholder(token: str) -> bool:
    return bool(PLACEHOLDER_RE.search(token)) or bool(VARIABLE_RE.search(token))


def lane_kind(lane: str, fleet: Path, state_dir: Path) -> str:
    """'sibling-lane' | 'fleet-root-role' | 'unknown'.

    A sibling lane owns a ``<fleet>/<lane>-shokunin`` repository; its report
    file stem is the lane id.  A fleet-root role (the aggregator and the
    protocol lane) owns no per-lane repository and reports to a fleet-level
    artefact, so the stem conjunct does not apply to it -- it is listed out
    of scope with that reason, not silently excepted.  An id that is neither
    names no lane this fleet knows."""
    if (fleet / ("%s-shokunin" % lane)).is_dir():
        return "sibling-lane"
    if (state_dir / ("%s.round" % lane)).is_file() or \
            (state_dir / ("%s.report-baseline" % lane)).is_file():
        return "fleet-root-role"
    return "unknown"


def state_source(state_dir: Path, lane: str) -> tuple[str, int | None, str]:
    """('baseline', round, detail) | ('stale', None, detail) | ('none', None, detail).

    ``baseline`` is the hyaku driver's record: the first whitespace field of
    ``<state-dir>/<lane>.report-baseline`` -- the lane's latest dispatched
    round.  A lane that still has only the legacy ``<lane>.round`` file
    (frozen since 2026-10-15) is 'stale': reported, never compared.  A lane
    with neither file has no state source."""
    base = state_dir / ("%s.report-baseline" % lane)
    if base.is_file():
        try:
            raw = base.read_text(encoding="utf-8")
        except OSError as exc:
            return "none", None, "unreadable %s (%s)" % (base, exc.strerror or exc)
        first = raw.split()[:1]
        if not first:
            return "none", None, "empty %s" % base
        try:
            return "baseline", int(first[0]), "%s = %s" % (base.name, first[0])
        except ValueError:
            return "none", None, "non-integer round in %s: %r" % (base, first[0])
    legacy = state_dir / ("%s.round" % lane)
    if legacy.is_file():
        return "stale", None, ("state-stale: only %s present (legacy, frozen "
                               "since 2026-10-15); not compared" % legacy.name)
    return "none", None, "no state file for lane %r" % lane


# ---------------------------------------------------------------------------
# checklist box extraction (the kotoba-checklist-v1 normalisation rule)
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
BOX_RE = re.compile(r"^(\s*)-\s+\[([ xX])\]\s?(.*)$")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
DISPATCH_SECTION = "Dispatch-prompt fidelity checklist"
BOX_ORDER = ("dispatch.01", "dispatch.02", "dispatch.03", "dispatch.04",
             "dispatch.05", "dispatch.06", "dispatch.07", "dispatch.08",
             "dispatch.09")


def _fenced(lines: list[str]) -> set[int]:
    """1-based line numbers inside a fenced code block (opaque)."""
    opaque: set[int] = set()
    fence: str | None = None
    for i, line in enumerate(lines, 1):
        m = FENCE_RE.match(line)
        if fence is None:
            if m:
                fence = m.group(1)[0] * 3
                opaque.add(i)
            continue
        opaque.add(i)
        if m and m.group(1)[0] * 3 == fence:
            fence = None
    return opaque


def dispatch_box_sha256(skill_text: str) -> dict[str, str]:
    """{box_id: sha256} for the nine dispatch-prompt checklist boxes.

    The normalisation mirrors verifiers/verify_skill_checklist.py: the box's
    first line minus the '- [ ] ' marker plus every stripped continuation
    line, joined with one space, whitespace runs collapsed to one space,
    stripped, UTF-8 sha256."""
    lines = skill_text.splitlines()
    opaque = _fenced(lines)
    out: dict[str, str] = {}
    section = ""
    i = 0
    while i < len(lines):
        if i + 1 in opaque:
            i += 1
            continue
        hm = HEADING_RE.match(lines[i])
        if hm:
            section = hm.group(1).strip()
            i += 1
            continue
        bm = BOX_RE.match(lines[i])
        if not bm or section != DISPATCH_SECTION:
            i += 1
            continue
        indent = len(bm.group(1))
        parts = [bm.group(3)]
        j = i + 1
        while j < len(lines):
            line = lines[j]
            if HEADING_RE.match(line) or BOX_RE.match(line):
                break
            if not line.strip() or j + 1 in opaque:
                break
            if len(line) - len(line.lstrip()) <= indent:
                break
            parts.append(line.strip())
            j += 1
        text = re.sub(r"\s+", " ", " ".join(p for p in parts if p)).strip()
        if len(out) < len(BOX_ORDER):
            out[BOX_ORDER[len(out)]] = hashlib.sha256(
                text.encode("utf-8")).hexdigest()
        i = j
    return out


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------

def _file_result(name: str, lane: str | None, verdicts: dict[str, dict],
                 note: str = "") -> dict:
    statuses = [v["status"] for v in verdicts.values()]
    if "FAIL" in statuses:
        verdict = "FAIL"
    elif "N/A" in statuses:
        verdict = "N/A"
    else:
        verdict = "PASS"
    out = {"file": name, "lane": lane, "verdict": verdict,
           "conjuncts": verdicts}
    if note:
        out["note"] = note
    return out


def evaluate_dispatch_04(prompts_dir: Path, state_dir: Path, fleet: Path) -> dict:
    """The dispatch.04 box over the prompts directory."""
    names = sorted(p.name for p in prompts_dir.iterdir() if p.is_file())
    out_of_scope = []
    files = []
    for name in names:
        lane, _round, kind = lane_of(name)
        if lane is None:
            out_of_scope.append({
                "file": name, "check": "dispatch.04",
                "reason": "name is not <lane>-round-<N>.md or <lane>-L1.md"})
            continue
        text = read_text(prompts_dir / name, "prompt file")
        paths = report_paths(text)
        verdicts: dict[str, dict] = {}
        if not paths:
            for cid in CONJUNCTS["dispatch.04"]:
                verdicts[cid] = {"status": "N/A",
                                 "detail": "no report path found in the file"}
            files.append(_file_result(name, lane, verdicts,
                                      note="no report path found"))
            continue
        bad = [(r, s) for r, s in paths if has_placeholder(s) or has_placeholder(
            ".ufo/reports/round-%d/%s" % (r, s))]
        if bad:
            verdicts["report_path_literal"] = {
                "status": "FAIL",
                "detail": "report path carries a placeholder or an "
                          "unsubstituted variable: %s"
                          % ", ".join(".ufo/reports/round-%d/%s" % b for b in bad)}
        else:
            verdicts["report_path_literal"] = {
                "status": "PASS",
                "detail": "%d report path(s), all literal" % len(paths)}
        kind_of_lane = lane_kind(lane, fleet, state_dir)
        if kind_of_lane == "unknown":
            verdicts["lane_identity_known"] = {
                "status": "FAIL",
                "detail": "lane id %r names no known lane: no %s repository "
                          "and no state file" % (lane, "%s-shokunin" % lane)}
            verdicts["report_stem_is_lane_id"] = {
                "status": "N/A",
                "detail": "lane identity unknown"}
        elif kind_of_lane == "fleet-root-role":
            stems = sorted({s for _r, s in paths})
            verdicts["report_stem_is_lane_id"] = {
                "status": "N/A",
                "detail": "out of scope: fleet-root role (no %s repository); "
                          "its report artefact is fleet-level, observed stem(s) %s"
                          % ("%s-shokunin" % lane, ", ".join(stems) or "<none>")}
            verdicts["lane_identity_known"] = {
                "status": "PASS",
                "detail": "known fleet-root role (state file present)"}
            out_of_scope.append({
                "file": name, "check": "dispatch.04",
                "reason": "conjunct report_stem_is_lane_id does not apply: "
                          "fleet-root role with no %s repository"
                          % ("%s-shokunin" % lane)})
        else:
            stems = sorted({s for _r, s in paths})
            wrong = [s for s in stems if s != lane]
            if wrong:
                verdicts["report_stem_is_lane_id"] = {
                    "status": "FAIL",
                    "detail": "report stem(s) %s != lane id %r"
                              % (", ".join(wrong), lane)}
            else:
                verdicts["report_stem_is_lane_id"] = {
                    "status": "PASS",
                    "detail": "report stem %r == lane id" % lane}
            verdicts["lane_identity_known"] = {
                "status": "PASS",
                "detail": "sibling lane repository %s-shokunin" % lane}
        files.append(_file_result(name, lane, verdicts))
    return _finish("dispatch.04", files, out_of_scope)


def evaluate_dispatch_08(prompts_dir: Path, state_dir: Path, fleet: Path) -> dict:
    """The dispatch.08 box over the prompts directory."""
    names = sorted(p.name for p in prompts_dir.iterdir() if p.is_file())
    out_of_scope = []
    files = []
    for name in names:
        lane, round_n, kind = lane_of(name)
        if lane is None:
            out_of_scope.append({
                "file": name, "check": "dispatch.08",
                "reason": "name is not <lane>-round-<N>.md or <lane>-L1.md"})
            continue
        if kind != "round":
            out_of_scope.append({
                "file": name, "check": "dispatch.08",
                "reason": "spawn file: the box's round token is read from the "
                          "file name, and a <lane>-L1.md name carries none"})
            continue
        text = read_text(prompts_dir / name, "prompt file")
        verdicts: dict[str, dict] = {}
        rr = role_round(text)
        if rr is None:
            verdicts["filename_role_round_equal"] = {
                "status": "FAIL",
                "detail": "no role-line round token on line 1"}
        elif rr != round_n:
            verdicts["filename_role_round_equal"] = {
                "status": "FAIL",
                "detail": "role line says round %d, file name says %d"
                          % (rr, round_n)}
        else:
            verdicts["filename_role_round_equal"] = {
                "status": "PASS", "detail": "role line round %d" % rr}
        paths = report_paths(text)
        dirs = sorted({r for r, _s in paths})
        if not paths:
            verdicts["filename_report_dir_round_equal"] = {
                "status": "N/A", "detail": "no report path found in the file"}
        elif dirs != [round_n]:
            verdicts["filename_report_dir_round_equal"] = {
                "status": "FAIL",
                "detail": "report dir round(s) %s != file name round %d"
                          % (", ".join(str(d) for d in dirs), round_n)}
        else:
            verdicts["filename_report_dir_round_equal"] = {
                "status": "PASS",
                "detail": "report dir round %d" % round_n}
        state, value, detail = state_source(state_dir, lane)
        if state == "baseline":
            if round_n <= value:
                verdicts["round_le_latest_dispatched"] = {
                    "status": "PASS",
                    "detail": "round %d <= latest dispatched %d (%s)"
                              % (round_n, value, detail)}
            else:
                verdicts["round_le_latest_dispatched"] = {
                    "status": "FAIL",
                    "detail": "round %d > latest dispatched %d (%s)"
                              % (round_n, value, detail)}
        else:
            verdicts["round_le_latest_dispatched"] = {
                "status": "N/A", "detail": detail}
        files.append(_file_result(name, lane, verdicts))
    return _finish("dispatch.08", files, out_of_scope)


def _finish(check_id: str, files: list[dict], out_of_scope: list[dict]) -> dict:
    evaluated = len(files)
    fails = [f for f in files if f["verdict"] == "FAIL"]
    nas = [f for f in files if f["verdict"] == "N/A"]
    if fails:
        status = "FAIL"
    elif not files or not any(f["verdict"] == "PASS" for f in files):
        status = "N/A"
    else:
        status = "PASS"
    detail = "%d file(s) evaluated: %d PASS, %d FAIL, %d N/A; %d out of scope" % (
        evaluated, evaluated - len(fails) - len(nas), len(fails), len(nas),
        len(out_of_scope))
    if fails:
        detail += "; failing files: " + ", ".join(
            "%s (%s)" % (f["file"], ",".join(
                c for c, v in f["conjuncts"].items() if v["status"] == "FAIL"))
            for f in fails[:12])
    return {"id": check_id, "status": status, "evaluated": evaluated,
            "detail": detail, "files": files, "out_of_scope": out_of_scope}


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--prompts", default=str(DEFAULT_PROMPTS), metavar="DIR",
                    help="dispatch-prompts directory (default: %(default)s)")
    ap.add_argument("--state-dir", default=str(DEFAULT_STATE_DIR), metavar="DIR",
                    help="fleet state directory (default: %(default)s)")
    ap.add_argument("--fleet", default=str(DEFAULT_FLEET), metavar="DIR",
                    help="fleet root holding the <lane>-shokunin repositories "
                         "(default: %(default)s)")
    ap.add_argument("--check", action="append", choices=CHECK_IDS, default=None,
                    help="run only this check (repeatable); default: all")
    ap.add_argument("--self-test", action="store_true",
                    help="assert the checks on temporary fixtures only (its "
                         "exit code is not comparable to a live run)")
    ap.add_argument("--box-proof", action="store_true",
                    help="prove that both boxes are delegated to this "
                         "instrument and that the committed fixtures "
                         "discriminate each of the six named conjuncts "
                         "(report_path_literal, report_stem_is_lane_id, "
                         "lane_identity_known, filename_role_round_equal, "
                         "filename_report_dir_round_equal, "
                         "round_le_latest_dispatched), one must-fail fixture "
                         "case each, read from the observed conjunct "
                         "statuses and not from the case labels. A named "
                         "conjunct with no isolated must-fail case is "
                         "reported as uncovered, its box is not counted and "
                         "the run exits 1; each box also needs an all-PASS "
                         "control case, and dispatch.08 a case whose "
                         "round_le_latest_dispatched is N/A. The box clauses "
                         "without a fixture -- the unsubstituted variable, <= "
                         "at equality, the legacy-state arm and a non-digit "
                         "round folder -- are not proven.")
    ap.add_argument("--map", default=None, metavar="PATH",
                    help="box-map JSON for --box-proof (default: "
                         "<repo>/verifiers/%s)" % BASELINE_NAME)
    ap.add_argument("--fixtures", default=None, metavar="DIR",
                    help="fixture corpus for --box-proof (default: "
                         "<repo>/verifiers/fixtures/dispatch-prompts)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    return ap


def emit_json(payload: dict) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def run_checks(prompts: Path, state_dir: Path, fleet: Path,
                wanted: list[str]) -> list[dict]:
    results = []
    for cid in wanted:
        if cid == "dispatch.04":
            results.append(evaluate_dispatch_04(prompts, state_dir, fleet))
        else:
            results.append(evaluate_dispatch_08(prompts, state_dir, fleet))
    return results


# ---------------------------------------------------------------------------
# self-test (temporary fixtures only)
# ---------------------------------------------------------------------------

SELF_TEST_PROMPT = """You are the kote L1, round {round}. Working dir: /fleet/kote-shokunin.

L0 template (must not trip dispatch.04): `<lane> | round-<N> | <question>`

Write the round report at `/fleet/.ufo/reports/round-{round}/kote.md` on the
main repo. | godspeed
"""


def _write_case(root: Path, name: str, text: str, baseline: str | None,
                legacy: str | None) -> Path:
    case = root / name
    (case / "prompts").mkdir(parents=True, exist_ok=True)
    (case / "state").mkdir(parents=True, exist_ok=True)
    (case / "fleet" / "kote-shokunin").mkdir(parents=True, exist_ok=True)
    (case / "fleet" / "kote-shokunin" / "keep").write_text(
        "fixture marker\n", encoding="utf-8")
    fname = "kote-round-7.md"
    (case / "prompts" / fname).write_text(text, encoding="utf-8")
    if baseline is not None:
        (case / "state" / "kote.report-baseline").write_text(
            baseline + " " + "0" * 64 + "\n", encoding="utf-8")
    if legacy is not None:
        (case / "state" / "kote.round").write_text(legacy + "\n", encoding="utf-8")
    return case


def _verdict_of(result: dict, fname: str) -> dict | None:
    for f in result["files"]:
        if f["file"] == fname:
            return f
    return None


# The six named conjuncts, restated here so that a change to the pinned
# constant in the instrument is caught by the self-test and not only by the
# fixture corpus.
SELF_TEST_CONJUNCTS = {
    "dispatch.04": ("report_path_literal", "report_stem_is_lane_id",
                    "lane_identity_known"),
    "dispatch.08": ("filename_role_round_equal",
                    "filename_report_dir_round_equal",
                    "round_le_latest_dispatched"),
}


def _proof_fixture_corpus(root: Path) -> list[dict]:
    """Build a synthetic dispatch fixture corpus in the shape of the
    committed one: one must-pass control and one must-fail case per named
    conjunct, one case directory each.  Returns the manifest case list."""
    good = SELF_TEST_PROMPT.format(round=7)
    specs = [
        # id, check, file, verdict, conjunct, text, state round
        ("d04-control", "dispatch.04", "kote-round-7.md", "PASS", None,
         good, "9"),
        ("d04-placeholder", "dispatch.04", "kote-round-7.md", "FAIL",
         "report_path_literal",
         good.replace("/round-7/kote.md", "/round-7/<lane>.md"), "9"),
        ("d04-stem", "dispatch.04", "kote-round-7.md", "FAIL",
         "report_stem_is_lane_id",
         good.replace("/round-7/kote.md", "/round-7/other.md"), "9"),
        ("d04-unknown-lane", "dispatch.04", "ghost-round-7.md", "FAIL",
         "lane_identity_known", good.replace("kote", "ghost"), None),
        ("d08-control", "dispatch.08", "kote-round-7.md", "PASS", None,
         good, "9"),
        ("d08-role-round", "dispatch.08", "kote-round-7.md", "FAIL",
         "filename_role_round_equal", good.replace("round 7.", "round 6."),
         "9"),
        ("d08-report-dir-round", "dispatch.08", "kote-round-7.md", "FAIL",
         "filename_report_dir_round_equal",
         good.replace("/round-7/", "/round-6/"), "9"),
        ("d08-above-state", "dispatch.08", "kote-round-7.md", "FAIL",
         "round_le_latest_dispatched", good, "6"),
        ("d08-missing-state", "dispatch.08", "kote-round-7.md", "N/A",
         "round_le_latest_dispatched", good, None),
    ]
    cases: list[dict] = []
    for cid, check, fname, verdict, conj, text, state in specs:
        case_dir = root / cid
        (case_dir / "prompts").mkdir(parents=True, exist_ok=True)
        (case_dir / "state").mkdir(parents=True, exist_ok=True)
        (case_dir / "fleet").mkdir(parents=True, exist_ok=True)
        if fname.startswith("kote"):
            # a lane the fleet knows, so only the named conjunct fails
            (case_dir / "fleet" / "kote-shokunin").mkdir(parents=True,
                                                        exist_ok=True)
        (case_dir / "prompts" / fname).write_text(text, encoding="utf-8")
        if state is not None:
            (case_dir / "state" / "kote.report-baseline").write_text(
                state + " " + "0" * 64 + "\n", encoding="utf-8")
        entry = {"id": cid, "check": check, "dir": cid, "file": fname,
                 "expect_verdict": verdict}
        if conj is not None:
            entry["expect_conjunct"] = conj
            entry["expect_conjunct_status"] = (
                "FAIL" if verdict == "FAIL" else verdict)
        cases.append(entry)
    return cases


def self_test() -> int:
    failures: list[str] = []
    total = 0

    def rec(what: str, ok: bool, got: object) -> None:
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (what, got))

    with tempfile.TemporaryDirectory(prefix="dispatch-selftest-") as tmp:
        root = Path(tmp)
        good = SELF_TEST_PROMPT.format(round=7)

        # --- control: a correct prompt passes both boxes -------------------
        case = _write_case(root, "control", good, "9", None)
        r04 = evaluate_dispatch_04(case / "prompts", case / "state",
                                   case / "fleet")
        r08 = evaluate_dispatch_08(case / "prompts", case / "state",
                                   case / "fleet")
        f04 = _verdict_of(r04, "kote-round-7.md")
        f08 = _verdict_of(r08, "kote-round-7.md")
        rec("control: dispatch.04 verdict PASS", f04 and f04["verdict"] == "PASS",
            f04)
        rec("control: dispatch.08 verdict PASS", f08 and f08["verdict"] == "PASS",
            f08)
        rec("control: dispatch.04 evaluated 1", r04["evaluated"] == 1,
            r04["evaluated"])
        rec("control: dispatch.08 evaluated 1", r08["evaluated"] == 1,
            r08["evaluated"])
        rec("control: the L0 '<lane> | round-<N>' template in the body does "
            "not trip dispatch.04",
            f04 and f04["conjuncts"]["report_path_literal"]["status"] == "PASS",
            f04 and f04["conjuncts"]["report_path_literal"])

        # --- dispatch.04: placeholder in the report path -------------------
        case = _write_case(root, "ph", good.replace(
            "/round-7/kote.md", "/round-7/<lane>.md"), "9", None)
        r = evaluate_dispatch_04(case / "prompts", case / "state", case / "fleet")
        f = _verdict_of(r, "kote-round-7.md")
        rec("placeholder report path: dispatch.04 FAIL",
            f and f["verdict"] == "FAIL", f)
        rec("placeholder report path: conjunct report_path_literal FAIL",
            f and f["conjuncts"]["report_path_literal"]["status"] == "FAIL", f)

        # --- dispatch.04: wrong lane stem ----------------------------------
        case = _write_case(root, "stem", good.replace(
            "/round-7/kote.md", "/round-7/other.md"), "9", None)
        r = evaluate_dispatch_04(case / "prompts", case / "state", case / "fleet")
        f = _verdict_of(r, "kote-round-7.md")
        rec("wrong lane stem: dispatch.04 FAIL", f and f["verdict"] == "FAIL", f)
        rec("wrong lane stem: conjunct report_stem_is_lane_id FAIL",
            f and f["conjuncts"]["report_stem_is_lane_id"]["status"] == "FAIL", f)

        # --- dispatch.04: unknown lane -------------------------------------
        case = root / "unknown"
        (case / "prompts").mkdir(parents=True, exist_ok=True)
        (case / "state").mkdir(parents=True, exist_ok=True)
        (case / "fleet").mkdir(parents=True, exist_ok=True)
        (case / "prompts" / "ghost-round-7.md").write_text(
            SELF_TEST_PROMPT.format(round=7).replace("kote", "ghost"),
            encoding="utf-8")
        r = evaluate_dispatch_04(case / "prompts", case / "state", case / "fleet")
        f = _verdict_of(r, "ghost-round-7.md")
        rec("unknown lane: dispatch.04 FAIL", f and f["verdict"] == "FAIL", f)
        rec("unknown lane: conjunct lane_identity_known FAIL",
            f and f["conjuncts"]["lane_identity_known"]["status"] == "FAIL", f)

        # --- dispatch.08: role-line round mismatch -------------------------
        case = _write_case(root, "role", good.replace("round 7.", "round 6."),
                           "9", None)
        r = evaluate_dispatch_08(case / "prompts", case / "state", case / "fleet")
        f = _verdict_of(r, "kote-round-7.md")
        rec("role-line round mismatch: dispatch.08 FAIL",
            f and f["verdict"] == "FAIL", f)
        rec("role-line round mismatch: conjunct filename_role_round_equal FAIL",
            f and f["conjuncts"]["filename_role_round_equal"]["status"] == "FAIL",
            f)

        # --- dispatch.08: report-dir round mismatch ------------------------
        case = _write_case(root, "dir", good.replace("/round-7/", "/round-6/"),
                           "9", None)
        r = evaluate_dispatch_08(case / "prompts", case / "state", case / "fleet")
        f = _verdict_of(r, "kote-round-7.md")
        rec("report-dir round mismatch: dispatch.08 FAIL",
            f and f["verdict"] == "FAIL", f)
        rec("report-dir round mismatch: conjunct "
            "filename_report_dir_round_equal FAIL",
            f and f["conjuncts"]["filename_report_dir_round_equal"]["status"]
            == "FAIL", f)

        # --- dispatch.08: round above the latest dispatched round -----------
        case = _write_case(root, "above", good, "6", None)
        r = evaluate_dispatch_08(case / "prompts", case / "state", case / "fleet")
        f = _verdict_of(r, "kote-round-7.md")
        rec("round above state: dispatch.08 FAIL", f and f["verdict"] == "FAIL", f)
        rec("round above state: conjunct round_le_latest_dispatched FAIL",
            f and f["conjuncts"]["round_le_latest_dispatched"]["status"] == "FAIL",
            f)

        # --- dispatch.08: missing state source is N/A, never a pass --------
        case = _write_case(root, "nostate", good, None, None)
        r = evaluate_dispatch_08(case / "prompts", case / "state", case / "fleet")
        f = _verdict_of(r, "kote-round-7.md")
        rec("missing state: dispatch.08 file verdict is not PASS",
            f and f["verdict"] != "PASS", f)
        rec("missing state: conjunct round_le_latest_dispatched is N/A",
            f and f["conjuncts"]["round_le_latest_dispatched"]["status"] == "N/A",
            f and f["conjuncts"]["round_le_latest_dispatched"])

        # --- dispatch.08: legacy-only state is state-stale, not compared ---
        case = _write_case(root, "stale", good, None, "6")
        r = evaluate_dispatch_08(case / "prompts", case / "state", case / "fleet")
        f = _verdict_of(r, "kote-round-7.md")
        rec("state-stale lane: conjunct round_le_latest_dispatched is N/A",
            f and f["conjuncts"]["round_le_latest_dispatched"]["status"] == "N/A",
            f and f["conjuncts"]["round_le_latest_dispatched"])
        rec("state-stale lane: the detail names state-stale",
            f and "state-stale" in f["conjuncts"]["round_le_latest_dispatched"]
            ["detail"], f)

        # --- out-of-scope names and the never-pass-on-zero rule ------------
        case = root / "scope"
        (case / "prompts").mkdir(parents=True, exist_ok=True)
        (case / "state").mkdir(parents=True, exist_ok=True)
        (case / "fleet").mkdir(parents=True, exist_ok=True)
        (case / "prompts" / "kote-L1.md").write_text(good, encoding="utf-8")
        (case / "prompts" / "kote-round-7-continuation-x.md").write_text(
            good, encoding="utf-8")
        r04 = evaluate_dispatch_04(case / "prompts", case / "state",
                                   case / "fleet")
        r08 = evaluate_dispatch_08(case / "prompts", case / "state",
                                   case / "fleet")
        rec("an L1 file is in scope for dispatch.04",
            r04["evaluated"] == 1, r04["evaluated"])
        rec("an L1 file is out of scope for dispatch.08",
            r08["evaluated"] == 0 and len(r08["out_of_scope"]) == 2,
            (r08["evaluated"], r08["out_of_scope"]))
        rec("dispatch.08 with no in-scope file is never a PASS",
            r08["status"] != "PASS", r08["status"])
        empty = root / "empty"
        (empty / "prompts").mkdir(parents=True, exist_ok=True)
        (empty / "state").mkdir(parents=True, exist_ok=True)
        (empty / "fleet").mkdir(parents=True, exist_ok=True)
        z04 = evaluate_dispatch_04(empty / "prompts", empty / "state",
                                   empty / "fleet")
        z08 = evaluate_dispatch_08(empty / "prompts", empty / "state",
                                   empty / "fleet")
        rec("an empty prompts directory is never a PASS",
            z04["status"] != "PASS" and z08["status"] != "PASS",
            (z04["status"], z08["status"]))
        rec("an empty prompts directory evaluates 0",
            z04["evaluated"] == 0 and z08["evaluated"] == 0,
            (z04["evaluated"], z08["evaluated"]))

        # --- the extraction helpers on the live-shaped text -----------------
        rec("report_paths skips a directory mention",
            report_paths("land under .ufo/reports/round-4/. Re-read.") == [],
            report_paths("land under .ufo/reports/round-4/. Re-read."))
        rec("report_paths keeps an absolute report path",
            report_paths("at `/x/.ufo/reports/round-9/kote.md` now")
            == [(9, "kote")],
            report_paths("at `/x/.ufo/reports/round-9/kote.md` now"))
        rec("role_round reads the first round token only",
            role_round("You are the x L1, round 7 of up to 1024.") == 7,
            role_round("You are the x L1, round 7 of up to 1024."))
        rec("lane_of reads a round file",
            lane_of("kote-round-7.md") == ("kote", 7, "round"),
            lane_of("kote-round-7.md"))
        rec("lane_of reads an L1 file",
            lane_of("kote-L1.md") == ("kote", None, "l1"), lane_of("kote-L1.md"))
        rec("lane_of rejects a foreign name",
            lane_of("kote-round-7-continuation-x.md") == (None, None, None),
            lane_of("kote-round-7-continuation-x.md"))

        # --- the box proof enforces its own fixture coverage ---------------
        rec("the pinned conjunct list names the six conjuncts",
            CONJUNCTS == SELF_TEST_CONJUNCTS, CONJUNCTS)
        proof = root / "proof"
        fx = proof / "fixtures" / "dispatch-prompts"
        fx.mkdir(parents=True, exist_ok=True)
        (proof / "verifiers").mkdir(parents=True, exist_ok=True)
        skill_src = Path(__file__).resolve().parent.parent / SKILL_NAME
        skill_err = None
        try:
            (proof / SKILL_NAME).write_text(
                skill_src.read_text(encoding="utf-8"), encoding="utf-8")
        except OSError as exc:
            skill_err = exc
        rec("the proof tree carries a copy of SKILL.md", skill_err is None,
            skill_err)
        box_map = {"schema": "kotoba-checklist-map-v1",
                   "boxes": [{"box_id": cid,
                              "section": "Dispatch-prompt fidelity checklist",
                              "text_sha256": PINNED_BOX_SHA[cid],
                              "disposition": "delegated:" + DELEGATION_TARGET}
                             for cid in CHECK_IDS]}
        map_path = proof / "verifiers" / BASELINE_NAME
        map_path.write_text(json.dumps(box_map, indent=2, sort_keys=True),
                            encoding="utf-8")
        cases = _proof_fixture_corpus(fx)
        manifest_path = fx / "manifest.json"

        def write_manifest(cs: list[dict], note: str = "self-test corpus") \
                -> None:
            manifest_path.write_text(
                json.dumps({"schema": "kotoba-dispatch-fixtures-v1",
                            "cases": cs, "note": note},
                           indent=2, sort_keys=True),
                encoding="utf-8")

        def run_proof(tree: Path | None = None) -> tuple[int, str, str]:
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), \
                    contextlib.redirect_stderr(err):
                code = box_proof(map_path, tree or fx)
            return code, out.getvalue(), err.getvalue()

        def by_id(cid: str) -> dict:
            return next(c for c in cases if c["id"] == cid)

        write_manifest(cases)
        code, out, err = run_proof()
        rec("box proof: a complete corpus proves both boxes",
            code == 0 and "boxes proven 2" in out, (code, out, err))
        # every must-fail case deleted in turn leaves its conjunct uncovered
        for entry in cases:
            if entry.get("expect_verdict") != "FAIL":
                continue
            write_manifest([c for c in cases if c["id"] != entry["id"]])
            code, out, err = run_proof()
            rec("box proof: deleting %s leaves the box unproven"
                % entry["id"], code == 1, (code, out, err))
            rec("box proof: deleting %s names the box and the conjunct"
                % entry["id"],
                entry["check"] in err and entry["expect_conjunct"] in err,
                (entry["check"], entry["expect_conjunct"], err))
        # the control case and the N/A arm carry weight too
        for entry in cases:
            if entry.get("expect_verdict") not in ("PASS", "N/A"):
                continue
            write_manifest([c for c in cases if c["id"] != entry["id"]])
            code, out, err = run_proof()
            rec("box proof: deleting %s leaves the box unproven"
                % entry["id"], code == 1, (code, out, err))
        # a note-only edit changes nothing
        write_manifest(cases, note="self-test corpus, edited note")
        code, out, err = run_proof()
        rec("box proof: a note-only manifest edit is still a proof",
            code == 0 and "boxes proven 2" in out, (code, out, err))
        # a twin of a must-fail case replaces it without weakening the proof
        twin = dict(by_id("d04-stem"))
        twin["id"] = "d04-stem-twin"
        write_manifest([c for c in cases if c["id"] != "d04-stem"] + [twin])
        code, out, err = run_proof()
        rec("box proof: a twin of a must-fail case replaces it",
            code == 0 and "boxes proven 2" in out, (code, out, err))
        # a relabelled copy of the placeholder case cannot cover the stem
        copy = dict(by_id("d04-placeholder"))
        copy["id"] = "d04-stem-copy"
        copy["expect_conjunct"] = "report_stem_is_lane_id"
        write_manifest([c for c in cases if c["id"] != "d04-stem"] + [copy])
        code, out, err = run_proof()
        rec("box proof: a relabelled placeholder copy cannot cover the stem",
            code == 1 and "report_stem_is_lane_id" in err, (code, out, err))
        # no must-fail case at all: the expectation list is not the manifest
        write_manifest([c for c in cases if c.get("expect_verdict") != "FAIL"])
        code, out, err = run_proof()
        rec("box proof: a corpus with no must-fail case proves no box",
            code == 1 and "boxes proven 0" in out, (code, out, err))
        # a case that names a conjunct the box does not have is rejected
        bogus = json.loads(json.dumps(cases))
        bogus[1]["expect_conjunct"] = "not_a_named_conjunct"
        write_manifest(bogus)
        code, out, err = run_proof()
        rec("box proof: a must-fail case naming an unnamed conjunct is "
            "rejected", code == 1 and "not_a_named_conjunct" in err,
            (code, out, err))
        # a missing fixture directory is a substrate error, never a traceback
        broken = root / "proof-broken"
        shutil.copytree(fx, broken)
        shutil.rmtree(broken / "d04-stem")
        out2, err2 = io.StringIO(), io.StringIO()
        code = None
        try:
            with contextlib.redirect_stdout(out2), \
                    contextlib.redirect_stderr(err2):
                code = box_proof(map_path, broken)
        except Exception as exc:
            # the uninstrumented proof raises here; the fix must not
            err2.write("raised %r" % (exc,))
        rec("box proof: a missing fixture directory is a substrate error",
            code == 2 and "Traceback" not in err2.getvalue(),
            (code, err2.getvalue()))
        write_manifest(cases)

    for f in failures:
        print("self-test FAIL: %s" % f)
    print("%d failure(s) over %d assertions" % (len(failures), total))
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# box proof
# ---------------------------------------------------------------------------

def box_proof(map_path: Path, fixtures: Path) -> int:
    """Prove that both boxes are delegated here and that the committed
    fixtures discriminate every one of the six named conjuncts.

    A box counts only when all of the following hold:

    * the checklist map delegates the box to this instrument, the map's
      ``text_sha256`` equals the constant pinned in this file and the live
      ``SKILL.md`` box text hashes to it;
    * every manifest case for the box matches its expected verdict, and a
      case that names a conjunct matches that conjunct's expected status;
    * every conjunct named for the box in ``CONJUNCTS`` has a must-fail
      case whose *observed* failing conjunct is it.  The observation, not
      the case's ``expect_conjunct`` label, is the authority; a case may
      fail one further conjunct, but only in the pairing pinned in
      ``ALLOWED_CO_FAIL``;
    * the box has a must-pass control case whose observed conjuncts are all
      PASS, and, for the box that owns the N/A arm, a case whose observed
      ``round_le_latest_dispatched`` is N/A.

    The third rule is what makes the proof enforce its own coverage: the
    conjunct list is the constant ``CONJUNCTS``, never read from the
    manifest, so deleting a must-fail case leaves its conjunct without an
    isolated case, the box uncounted and the exit code 1.  Each uncovered
    conjunct is reported as
    ``box-proof: <box>: no isolated must-fail case for conjunct <name>``.

    A missing fixture directory or an unreadable fixture file is a substrate
    error, not a failed proof: it is reported as a problem line and the run
    exits 2, never a traceback.

    The bound of the claim: the fixtures discriminate the six named
    conjuncts, one must-fail case each.  The box clauses without a fixture
    -- the unsubstituted variable, ``<=`` at equality, the legacy-state arm
    and a non-digit round folder -- are not proven by this instrument.

    Prints ``boxes proven N`` on stdout; N is the number of boxes satisfying
    all the rules above.  Exit 0 only when N == 2."""
    problems: list[str] = []
    proven = 0
    substrate_error = False
    try:
        raw = map_path.read_text(encoding="utf-8")
        box_map = json.loads(raw)
    except (OSError, ValueError) as exc:
        print("boxes proven 0")
        print("box-proof: cannot read the box map %s (%s)"
              % (map_path, exc), file=sys.stderr)
        return 2
    entries = {}
    for e in box_map.get("boxes", []):
        entries[e.get("box_id")] = e
    try:
        skill_text = (map_path.parent.parent / SKILL_NAME).read_text(
            encoding="utf-8")
        live = dispatch_box_sha256(skill_text)
    except OSError as exc:
        live = {}
        problems.append("cannot read SKILL.md (%s)" % (exc.strerror or exc))
    try:
        manifest = json.loads((fixtures / "manifest.json").read_text(
            encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print("boxes proven 0")
        print("box-proof: cannot read the fixture manifest (%s)" % exc,
              file=sys.stderr)
        return 2
    for cid in CHECK_IDS:
        entry = entries.get(cid)
        if entry is None:
            problems.append("%s: no map entry" % cid)
            continue
        want = "delegated:" + DELEGATION_TARGET
        if entry.get("disposition") != want:
            problems.append("%s: map disposition is %r, not %r"
                            % (cid, entry.get("disposition"), want))
            continue
        pinned = PINNED_BOX_SHA.get(cid)
        if entry.get("text_sha256") != pinned:
            problems.append("%s: map text_sha256 %r != pinned %r"
                            % (cid, entry.get("text_sha256"), pinned))
            continue
        if live.get(cid) != pinned:
            problems.append("%s: live SKILL.md box hash %r != pinned %r"
                            % (cid, live.get(cid), pinned))
            continue
        cases = [c for c in manifest.get("cases", []) if c.get("check") == cid]
        if not cases:
            problems.append("%s: no fixture cases" % cid)
            continue
        ok = True
        # the observed failing conjuncts of every case that matched its
        # expected verdict; the coverage rule reads these, not the labels
        observed_fail: list[set[str]] = []
        control_ok = False
        na_ok = False
        for c in cases:
            case_dir = fixtures / c["dir"]
            want_check = c["check"]
            try:
                result = (evaluate_dispatch_04 if want_check == "dispatch.04"
                          else evaluate_dispatch_08)(case_dir / "prompts",
                                                    case_dir / "state",
                                                    case_dir / "fleet")
            except (EnvError, OSError) as exc:
                problems.append("%s/%s: %s" % (cid, c["id"], exc))
                substrate_error = True
                ok = False
                continue
            f = _verdict_of(result, c["file"])
            if f is None:
                problems.append("%s/%s: file %r not evaluated"
                                % (cid, c["id"], c["file"]))
                ok = False
                continue
            if f["verdict"] != c.get("expect_verdict"):
                problems.append("%s/%s: %s verdict %r, expected %r"
                                % (cid, c["id"], c["file"], f["verdict"],
                                   c.get("expect_verdict")))
                ok = False
                continue
            named = c.get("expect_conjunct")
            if named is not None:
                status = f["conjuncts"].get(named, {}).get("status")
                if status != c.get("expect_conjunct_status", "FAIL"):
                    problems.append("%s/%s: conjunct %s is %r, expected %r"
                                    % (cid, c["id"], named, status,
                                   c.get("expect_conjunct_status", "FAIL")))
                    ok = False
            fails = {n for n, info in f["conjuncts"].items()
                     if info.get("status") == "FAIL"}
            if c.get("expect_verdict") == "FAIL":
                observed_fail.append(fails)
            elif c.get("expect_verdict") == "PASS":
                if not fails and all(info.get("status") == "PASS"
                                     for info in f["conjuncts"].values()):
                    control_ok = True
            elif c.get("expect_verdict") == "N/A":
                if f["conjuncts"].get(NA_ARM_CONJUNCT, {}).get("status") \
                        == "N/A":
                    na_ok = True
        for n in CONJUNCTS.get(cid, ()):
            allowed = ALLOWED_CO_FAIL.get(n, frozenset())
            if not any(n in fails and (fails - {n}) <= allowed
                       for fails in observed_fail):
                problems.append("%s: no isolated must-fail case for conjunct "
                                "%s" % (cid, n))
                ok = False
        if not control_ok:
            problems.append("%s: no all-PASS control case" % cid)
            ok = False
        if NA_ARM_CONJUNCT in CONJUNCTS.get(cid, ()) and not na_ok:
            problems.append("%s: no N/A case for conjunct %s"
                            % (cid, NA_ARM_CONJUNCT))
            ok = False
        if ok:
            proven += 1
    print("boxes proven %d" % proven)
    for p in problems:
        print("box-proof: %s" % p, file=sys.stderr)
    if substrate_error:
        return 2
    return 0 if proven == 2 else 1


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        return self_test()
    if args.box_proof:
        map_path = Path(args.map) if args.map else \
            VERIFIERS_DIR / BASELINE_NAME
        fixtures = Path(args.fixtures) if args.fixtures else FIXTURES_DIR
        return box_proof(map_path, fixtures)
    prompts = Path(args.prompts)
    state_dir = Path(args.state_dir)
    fleet = Path(args.fleet)
    for path, what in ((prompts, "prompts directory"),
                       (state_dir, "state directory"),
                       (fleet, "fleet root")):
        if not path.is_dir():
            if args.json:
                emit_json({"checks": [], "pass": 0, "fail": 0, "na": 0,
                           "exit_code": 2,
                           "error": "%s: not a directory (%s)" % (path, what)})
            else:
                print("ERROR %s: not a directory (%s)" % (path, what),
                      file=sys.stderr)
            return 2
    wanted = list(args.check) if args.check else list(CHECK_IDS)
    try:
        results = run_checks(prompts, state_dir, fleet, wanted)
    except EnvError as exc:
        if args.json:
            emit_json({"checks": [], "pass": 0, "fail": 0, "na": 0,
                       "exit_code": 2, "error": str(exc)})
        else:
            print("ERROR %s" % exc, file=sys.stderr)
        return 2
    code = 1 if any(r["status"] == "FAIL" for r in results) else 0
    if args.json:
        emit_json({
            "checks": results,
            "pass": sum(1 for r in results if r["status"] == "PASS"),
            "fail": sum(1 for r in results if r["status"] == "FAIL"),
            "na": sum(1 for r in results if r["status"] == "N/A"),
            "exit_code": code,
        })
    else:
        for r in results:
            print("%s %s: evaluated %d — %s"
                  % (r["status"], r["id"], r["evaluated"], r["detail"]))
    return code


if __name__ == "__main__":
    sys.exit(main())
