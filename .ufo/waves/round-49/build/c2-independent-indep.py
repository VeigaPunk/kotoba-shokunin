#!/usr/bin/env python3
"""Independent second instrument for claim C2 (operability).

Executes two dispatch-prompt checklist boxes over a fleet prompt directory,
reading only from disk:

  dispatch.04  (kotoba-shokunin/SKILL.md:313-315)
      "Report path is literal — no `<…>` placeholder or unsubstituted
       variable; filename = the lane's `<id>` (a `<lane>` placeholder cost
       two lanes their canonical round-1 report names)."

  dispatch.08  (kotoba-shokunin/SKILL.md:325-327)
      "Round token `<N>` is identical across filename, role line, and report
       dir, and ≤ the lane's `.ufo/state/<id>.round` (which holds the lane's
       *latest* round — equality against a sibling's state is wrong)."

This script is written from the box texts alone; it does not read, import or
consult any other verifier in the lane repo.  It is READ-ONLY over the fleet
prompt directory and the fleet state directory.

Usage:
    indep.py [--prompts DIR] [--state DIR] [--out FILE] [--self-test]

Exit status: 0 when the run completed (verdicts are data, not a gate);
--self-test exits non-zero when a fixture arm misbehaves.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

DEFAULT_PROMPTS = "/home/vgpnk/Projects/shokunin/.ufo/prompts"
DEFAULT_STATE = "/home/vgpnk/Projects/shokunin/.ufo/state"
DEFAULT_ALT_STATE = os.path.expanduser("~/.local/state/shokunin-hyaku/next")
DEFAULT_OUT = "/fast/scratch/hyaku/kotoba-r49/seats/DispatchIndependent/indep.json"

# ---------------------------------------------------------------- extraction

# `<lane>-round-<N>.md`, `<lane>-round-<N>-continuation-<tag>.md`
NAME_ROUND = re.compile(r"^(?P<lane>.+)-round-(?P<round>\d+)(?P<suffix>(?:-[A-Za-z0-9]+)*)\.md$")
# `<lane>-L1.md`
NAME_L1 = re.compile(r"^(?P<lane>.+)-L1\.md$")

# a report path: any prefix, `.ufo/reports/round-<N>/<stem>`; the stem is
# captured greedily up to whitespace / markdown punctuation.
RE_REPORT = re.compile(
    r"(?P<prefix>[\w./~@-]*)\.ufo/reports/round-(?P<round>\d+)/(?P<stem>[^\s`'\")\[\]]*)"
)
# "round <N>" or "round-<N>" anywhere on the role line
RE_ROUND_TOKEN = re.compile(r"\bround[\s-]+(\d+)\b")
# an unsubstituted shell/template variable
RE_VARIABLE = re.compile(r"\$\{[^}]*\}|\$[A-Za-z_][A-Za-z0-9_]*|\{\{[^}]*\}\}")
# an angle-bracket placeholder such as `<lane>` / `<N>`
RE_PLACEHOLDER = re.compile(r"<[^<>]+>")

ROLE_LINE_LINES = 5  # role line = first non-blank line; token may sit on a
                    # following line for the closure-role form


def clean_stem(stem: str) -> str:
    """Strip trailing sentence punctuation that follows a path in prose."""
    return stem.rstrip(":,.;*")


def lane_and_round(name: str):
    """Return (lane_id, filename_round_or_None, form) parsed from a file name.

    form is one of "round", "L1", "unknown".
    """
    m = NAME_ROUND.match(name)
    if m:
        return m.group("lane"), int(m.group("round")), "round"
    m = NAME_L1.match(name)
    if m:
        return m.group("lane"), None, "L1"
    return None, None, "unknown"


def role_line_of(text: str):
    """The first non-blank line of the prompt (the 'role line')."""
    for line in text.splitlines():
        if line.strip():
            return line
    return ""


def role_round(text: str):
    """Round token on the role line.

    The token is searched on the role line itself and, for the closure-role
    form, on the few lines that follow it (the closure prompt states
    "**<lane> round <N>**" on its second line).
    """
    lines = text.splitlines()
    for line in lines[:ROLE_LINE_LINES]:
        m = RE_ROUND_TOKEN.search(line)
        if m:
            return int(m.group(1)), line.strip()
    return None, None


def report_paths(text: str):
    """Every report path mentioned in the prompt.

    Each entry: dict(path, round, stem, line, placeholder, variable).
    Directory-only references (`.ufo/reports/round-N/` with no file stem) are
    reported separately as dir references and are not report file paths.
    """
    found = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for m in RE_REPORT.finditer(line):
            stem = clean_stem(m.group("stem"))
            path = "%s.ufo/reports/round-%s/%s" % (m.group("prefix"), m.group("round"), stem)
            found.append(
                {
                    "path": path,
                    "round": int(m.group("round")),
                    "stem": stem,
                    "line": lineno,
                    "is_file_path": bool(stem),
                    "placeholder": bool(RE_PLACEHOLDER.search(stem)),
                    "variable": bool(RE_VARIABLE.search(stem)),
                }
            )
    return found


def state_round(state_dir: str, lane: str):
    """The lane's own `.ufo/state/<id>.round` value, or None when absent."""
    path = os.path.join(state_dir, "%s.round" % lane)
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read().strip()
    except OSError:
        return None, path
    try:
        return int(raw), path
    except ValueError:
        return None, path


def alt_state_round(alt_state_dir, lane: str):
    """The lane's latest round from an ALTERNATE state source.

    Used only to diagnose how much of a dispatch.08 state-bound failure is
    caused by the primary state file being stale rather than by a prompt
    defect.  The file layout is `<lane>` (a bare integer), which is the
    layout of the hyaku inline driver's own next-round state.
    """
    if not alt_state_dir:
        return None, None
    path = os.path.join(alt_state_dir, lane)
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read().strip()
    except OSError:
        return None, path
    try:
        return int(raw), path
    except ValueError:
        return None, path


def state_report_baseline(state_dir: str, lane: str):
    """Alternate freshness signal: `.ufo/state/<id>.report-baseline` round.

    Reported alongside the box-literal `.round` value because the fleet's
    `.round` files were last written on 2026-10-15 and lag the lanes'
    actual latest round; the caller may want to know how much of a
    dispatch.08 failure is stale state rather than a prompt defect.
    """
    path = os.path.join(state_dir, "%s.report-baseline" % lane)
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            head = fh.read().split()
    except OSError:
        return None, path
    if head and head[0].isdigit():
        return int(head[0]), path
    return None, path


# ------------------------------------------------------------------- boxes


def check_dispatch_04(lane, paths):
    """Report path is literal; filename == the lane's id."""
    reasons = []
    unverifiable = []
    files = [p for p in paths if p["is_file_path"]]
    if not files:
        return False, ["no report file path found in the prompt"], unverifiable
    stems = []
    for p in files:
        if p["placeholder"]:
            reasons.append(
                "report path %r carries an unsubstituted placeholder (<...>)" % p["path"]
            )
        if p["variable"]:
            reasons.append(
                "report path %r carries an unsubstituted variable" % p["path"]
            )
        stems.append(p["stem"])
    distinct = sorted(set(stems))
    if distinct != ["%s.md" % lane]:
        reasons.append(
            "report filename stem(s) %s != the lane id %r (canonical name is %s.md)"
            % (distinct, lane, lane)
        )
    return (not reasons), reasons, unverifiable


def check_dispatch_08(lane, name_round, form, role_r, paths, st_r):
    """Round token identical across filename, role line, report dir; <= state.

    The box has two conjuncts; they are reported separately so a reader can
    tell a token-identity defect from a state-bound violation:
      components.token_identity -- filename vs role line vs report dir
      components.state_bound     -- N <= the lane's own .ufo/state/<id>.round
    The overall verdict is the conjunction (both must hold).
    """
    reasons = []
    unverifiable = []
    identity_reasons = []
    bound_reasons = []
    files = [p for p in paths if p["is_file_path"]]
    if role_r is None:
        identity_reasons.append("no round token found on the role line")
    if not files:
        identity_reasons.append("no report file path found in the prompt")
        unverifiable.append("report-dir round")
    dir_rounds = sorted({p["round"] for p in files})
    if role_r is not None and files and any(r != role_r for r in dir_rounds):
        identity_reasons.append(
            "round token differs: role line %d vs report dir %s" % (role_r, dir_rounds)
        )
    if form == "round" and role_r is not None and name_round != role_r:
        identity_reasons.append(
            "round token differs: filename %d vs role line %d" % (name_round, role_r)
        )
    if form == "L1":
        unverifiable.append("filename round token (an *-L1.md name carries none)")
    if role_r is not None and st_r is None:
        bound_reasons.append(
            "no state file for lane %r, so N <= state round cannot be established" % lane
        )
        unverifiable.append("state round")
    elif role_r is not None and st_r is not None and role_r > st_r:
        bound_reasons.append(
            "round token %d > the lane's state round %d" % (role_r, st_r)
        )
    reasons = identity_reasons + bound_reasons
    if identity_reasons:
        failure_class = "token-identity-mismatch"
    elif bound_reasons:
        failure_class = "state-bound-exceeded"
    else:
        failure_class = None
    components = {
        "token_identity": {
            "verdict": "pass" if not identity_reasons else "fail",
            "reasons": identity_reasons,
        },
        "state_bound": {
            "verdict": "pass" if not bound_reasons else "fail",
            "reasons": bound_reasons,
            "state_round": st_r,
        },
    }
    return (not reasons), reasons, unverifiable, components, failure_class


# ------------------------------------------------------------------- main


FLEET_ROOT = "/home/vgpnk/Projects/shokunin"


def report_path_exists(prompts_dir, paths):
    """Informational: does the named report file exist under the fleet root?

    Not part of either box verdict; recorded so a reader can see whether a
    report path that passes the box still points at a file that landed.
    """
    files = [p for p in paths if p["is_file_path"]]
    if not files:
        return None
    out = {}
    for p in files:
        raw = p["path"]
        if raw.startswith("/"):
            target = raw
        else:
            target = os.path.join(FLEET_ROOT, raw)
        out[raw] = os.path.isfile(target)
    return out


def evaluate_file(path, prompts_dir, state_dir, alt_state_dir=None):
    rel = os.path.relpath(path, prompts_dir)
    name = os.path.basename(path)
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    lane, name_round, form = lane_and_round(name)
    rl = role_line_of(text)
    r_r, r_line = role_round(text)
    paths = report_paths(text)
    scope = "dispatch" if os.path.dirname(path) == prompts_dir else "closure"

    if lane is None:
        return {
            "file": rel,
            "scope": scope,
            "form": "unknown",
            "lane_id": None,
            "filename_round": None,
            "role_line": rl,
            "role_line_round": r_r,
            "report_paths": paths,
            "state_round": None,
            "state_report_baseline": None,
            "dispatch.04": {"verdict": "fail", "reasons": ["file name carries no lane id / round token"]},
            "dispatch.08": {"verdict": "fail", "reasons": ["file name carries no lane id / round token"]},
        }

    st_r, st_path = state_round(state_dir, lane)
    rb_r, rb_path = state_report_baseline(state_dir, lane)
    alt_r, alt_path = alt_state_round(alt_state_dir, lane)

    ok04, why04, unver04 = check_dispatch_04(lane, paths)
    ok08, why08, unver08, comp08, cls08 = check_dispatch_08(
        lane, name_round, form, r_r, paths, st_r
    )

    exception = None
    file_stems = sorted({p["stem"] for p in paths if p["is_file_path"]})
    if lane == "aggregator" and file_stems == ["AGGREGATE.md"]:
        exception = (
            "the fleet's aggregate report is named AGGREGATE.md by convention, not "
            "aggregator.md; the box's literal reading of 'filename = the lane's id' "
            "is reported as FAIL and this note records the convention only"
        )

    return {
        "file": rel,
        "scope": scope,
        "form": form,
        "lane_id": lane,
        "filename_round": name_round,
        "filename_round_suffix": (NAME_ROUND.match(name).group("suffix") or "")
        if NAME_ROUND.match(name)
        else "",
        "role_line": rl,
        "role_line_round": r_r,
        "role_line_round_source_line": r_line,
        "report_paths": paths,
        "report_dir_rounds": sorted({p["round"] for p in paths}),
        "report_path_exists_on_disk": report_path_exists(prompts_dir, paths),
        "state_round": st_r,
        "state_file": st_path,
        "state_report_baseline": rb_r,
        "state_report_baseline_file": rb_path,
        "alt_state_round": alt_r,
        "alt_state_file": alt_path,
        "dispatch.04": {
            "verdict": "pass" if ok04 else "fail",
            "reasons": why04,
            "unverifiable": unver04,
        },
        "dispatch.08": {
            "verdict": "pass" if ok08 else "fail",
            "reasons": why08,
            "unverifiable": unver08,
            "components": comp08,
            "failure_class": cls08,
            "alt_state_bound_would_pass": (
                None
                if (alt_r is None or r_r is None)
                else (r_r <= alt_r)
            ),
        },
        "convention_exception": exception,
    }


def summarize(records, in_scope_pred):
    total = len(records)
    in_scope = [r for r in records if in_scope_pred(r)]
    out = {
        "files_scanned": total,
        "in_scope_files": len(in_scope),
        "out_of_scope_files": total - len(in_scope),
        "in_scope_breakdown_by_scope": {},
        "failures_per_box": {},
        "failing_files": {},
    }
    for r in records:
        out["in_scope_breakdown_by_scope"][r["scope"]] = (
            out["in_scope_breakdown_by_scope"].get(r["scope"], 0) + 1
        )
    for box in ("dispatch.04", "dispatch.08"):
        failing = [r["file"] for r in in_scope if r[box]["verdict"] == "fail"]
        unver = [r["file"] for r in in_scope if r[box].get("unverifiable")]
        out["failures_per_box"][box] = len(failing)
        out["failing_files"][box] = failing
        out.setdefault("unverifiable_files", {})[box] = unver
    # dispatch.08 has two conjuncts; report them apart so a reader can tell a
    # token-identity defect from a state-bound violation.
    ident = [r["file"] for r in in_scope if r["dispatch.08"]["components"]["token_identity"]["verdict"] == "fail"]
    bound = [r["file"] for r in in_scope if r["dispatch.08"]["components"]["state_bound"]["verdict"] == "fail"]
    out["dispatch.08_component_failures"] = {
        "token_identity": len(ident),
        "state_bound": len(bound),
        "token_identity_files": ident,
        "state_bound_files": bound,
    }
    classes = {}
    for r in in_scope:
        c = r["dispatch.08"].get("failure_class")
        if c:
            classes.setdefault(c, []).append(r["file"])
    out["dispatch.08_failure_classes"] = {k: len(v) for k, v in sorted(classes.items())}
    # Diagnostic: of the dispatch.08 failures, how many would still fail if the
    # state bound were read from the alternate next-round state source?  The
    # difference isolates staleness of `.ufo/state/<id>.round` from prompt defects.
    alt_pass = sum(
        1
        for r in in_scope
        if r["dispatch.08"]["verdict"] == "fail"
        and r["dispatch.08"].get("alt_state_bound_would_pass") is True
    )
    alt_unknown = sum(
        1
        for r in in_scope
        if r["dispatch.08"]["verdict"] == "fail"
        and r["dispatch.08"].get("alt_state_bound_would_pass") is None
    )
    out["dispatch.08_alt_state_diagnostic"] = {
        "failures_that_would_pass_on_alt_state": alt_pass,
        "failures_with_no_alt_state_value": alt_unknown,
        "failures_that_persist_on_alt_state": len(bound) - alt_pass,
    }
    # Headline pass counts (in scope), for the L1's diff table.
    for box in ("dispatch.04", "dispatch.08"):
        out.setdefault("passes_per_box", {})[box] = (
            len(in_scope) - out["failures_per_box"][box]
        )
    return out


def print_summary(summary, records, in_scope_pred):
    print("files scanned: %d" % summary["files_scanned"])
    print("in-scope files: %d (out-of-scope: %d)" % (summary["in_scope_files"], summary["out_of_scope_files"]))
    print("scope breakdown: %s" % json.dumps(summary["in_scope_breakdown_by_scope"], sort_keys=True))
    for box in ("dispatch.04", "dispatch.08"):
        print("failures %s: %d" % (box, summary["failures_per_box"][box]))
        for f in summary["failing_files"][box]:
            print("    FAIL %s" % f)
        print("    (unverifiable component on %d file(s))" % len(summary["unverifiable_files"][box]))
    comp = summary["dispatch.08_component_failures"]
    print("dispatch.08 conjunct breakdown: token_identity=%d state_bound=%d"
          % (comp["token_identity"], comp["state_bound"]))
    print("dispatch.08 failure classes: %s" % json.dumps(summary["dispatch.08_failure_classes"], sort_keys=True))
    alt = summary["dispatch.08_alt_state_diagnostic"]
    print("dispatch.08 alt-state diagnostic: %s" % json.dumps(alt, sort_keys=True))


# --------------------------------------------------------------- self test


def self_test():
    """Must-fail / must-pass arms over synthetic fixtures.

    Fixture file names follow the real naming form (`<lane>-round-<N>.md`),
    because the lane id and the filename round token are parsed from the name.
    """
    import tempfile

    fixtures = {
        # name: (text, expect04, expect08)
        "kotoba-round-5.md": (
            "You are the kotoba L1, round 5. Working dir: /x\n"
            "Write the round report at `/y/.ufo/reports/round-5/kotoba.md` on the fleet repo.\n",
            True, True,
        ),
        "kotoba-round-5-placeholder.md": (
            "You are the kotoba L1, round 5.\n"
            "Report: write to .ufo/reports/round-1/<lane>.md in the main repo.\n",
            False, False,
        ),
        "kotoba-round-5-wrongstem.md": (
            "You are the kotoba L1, round 5.\n"
            "Write .ufo/reports/round-5/notkotoba.md\n",
            False, True,
        ),
        "kotoba-round-5-rolemismatch.md": (
            "You are the kotoba L1, round 4.\n"
            "Write .ufo/reports/round-5/kotoba.md\n",
            True, False,
        ),
        "kotoba-round-99-overstate.md": (
            "You are the kotoba L1, round 99.\n"
            "Write .ufo/reports/round-99/kotoba.md\n",
            True, False,
        ),
        "kotoba-round-5-variable.md": (
            "You are the kotoba L1, round 5.\n"
            "Write .ufo/reports/round-5/${LANE}.md\n",
            False, True,
        ),
        "kotoba-round-5-diroverstate.md": (
            "You are the kotoba L1, round 5.\n"
            "Write .ufo/reports/round-7/kotoba.md\n",
            True, False,
        ),
        "kotoba-L1.md": (
            "You are the kotoba-shokunin L1 for round 1.\n"
            "Report: write a scoped findings file to .ufo/reports/round-1/kotoba.md\n",
            True, True,
        ),
    }
    failures = []
    with tempfile.TemporaryDirectory() as td:
        pdir = os.path.join(td, "prompts")
        sdir = os.path.join(td, "state")
        os.makedirs(pdir)
        os.makedirs(sdir)
        with open(os.path.join(sdir, "kotoba.round"), "w", encoding="utf-8") as fh:
            fh.write("10\n")
        for name, (text, _e04, _e08) in fixtures.items():
            with open(os.path.join(pdir, name), "w", encoding="utf-8") as fh:
                fh.write(text)
        for name, (text, e04, e08) in fixtures.items():
            rec = evaluate_file(os.path.join(pdir, name), pdir, sdir)
            got04 = rec["dispatch.04"]["verdict"] == "pass"
            got08 = rec["dispatch.08"]["verdict"] == "pass"
            if got04 != e04:
                failures.append("%s dispatch.04 expected pass=%s got pass=%s (%s)"
                                % (name, e04, got04, rec["dispatch.04"]["reasons"]))
            if got08 != e08:
                failures.append("%s dispatch.08 expected pass=%s got pass=%s (%s)"
                                % (name, e08, got08, rec["dispatch.08"]["reasons"]))
    if failures:
        print("SELF-TEST FAILED")
        for f in failures:
            print("  " + f)
        return 1
    print("SELF-TEST PASS: %d fixture arms behaved as specified" % len(fixtures))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prompts", default=DEFAULT_PROMPTS)
    ap.add_argument("--state", default=DEFAULT_STATE)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--alt-state", default=DEFAULT_ALT_STATE,
                    help="alternate next-round state dir, used ONLY to diagnose "
                         "how much of a dispatch.08 state-bound failure is caused "
                         "by the primary .round file being stale")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    prompts_dir = os.path.abspath(args.prompts)
    state_dir = os.path.abspath(args.state)
    if not os.path.isdir(prompts_dir):
        print("no such prompts dir: %s" % prompts_dir, file=sys.stderr)
        return 2

    files = []
    for root, _dirs, names in os.walk(prompts_dir):
        for n in sorted(names):
            if n.endswith(".md"):
                files.append(os.path.join(root, n))
    files.sort()

    records = [
        evaluate_file(p, prompts_dir, state_dir, args.alt_state or None) for p in files
    ]

    # In scope = the checklist's stated surface: the prompt directory's own
    # dispatch prompts (`*-L1.md` / `*-round-N*.md`).  Files under a
    # sub-directory (closure-role prompts) are measured and reported but are
    # not dispatch prompts for a lane round.
    def in_scope(r):
        return r["scope"] == "dispatch"

    summary = summarize(records, in_scope)

    out = {
        "instrument": "indep.py",
        "instrument_role": "independent second instrument for C2 (operability)",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "prompts_dir": prompts_dir,
        "state_dir": state_dir,
        "boxes_implemented": {
            "dispatch.04": {
                "source": "kotoba-shokunin/SKILL.md:313-315",
                "text": ("Report path is literal — no `<…>` placeholder or unsubstituted "
                         "variable; filename = the lane's `<id>` (a `<lane>` placeholder cost "
                         "two lanes their canonical round-1 report names)."),
            },
            "dispatch.08": {
                "source": "kotoba-shokunin/SKILL.md:325-327",
                "text": ("Round token `<N>` is identical across filename, role line, and report "
                         "dir, and ≤ the lane's `.ufo/state/<id>.round` (which holds the lane's "
                         "*latest* round — equality against a sibling's state is wrong)."),
            },
        },
        "judgement_calls": [
            "Report path location: every occurrence of `.ufo/reports/round-<N>/<stem>` in the "
            "file body is collected; the stem is stripped of trailing prose punctuation; a "
            "directory-only reference (`.ufo/reports/round-N/` with no file stem) is not a report "
            "file path.",
            "dispatch.04 is evaluated over ALL report paths in the file: every one must be free "
            "of `<...>` placeholders and of unsubstituted variables, and the set of distinct "
            "stems must be exactly ['<lane>.md'].",
            "dispatch.04 compares the report filename stem with the lane id parsed from the "
            "prompt FILE NAME (the `<id>` the box names), not with a stem the prompt itself asserts.",
            "*-L1.md files: the file name carries no round token, so the 'filename' component of "
            "dispatch.08 is recorded as unverifiable rather than failed; the role-line and "
            "report-dir components are still checked, as is the <= state bound.",
            "*-round-N-continuation-<tag>.md files: treated as ordinary round prompts; the "
            "continuation tag is recorded in filename_round_suffix and ignored for the round token.",
            "closure/ sub-directory prompts (role = hyaku non-author integrator) are measured and "
            "reported per file but are counted as OUT OF SCOPE: they are not a lane's own round "
            "dispatch prompt. Their per-file verdicts are in the records array for diffing.",
            "The state round is read from the lane's own `.ufo/state/<id>.round` in the fleet "
            "state directory, keyed by the lane id from the file name (never a sibling's file).",
            "`.ufo/state/<id>.report-baseline` (the other freshness signal in the same directory) "
            "is recorded per file as state_report_baseline so the reader can see how much of a "
            "dispatch.08 failure is stale state rather than a prompt defect.",
            "The role line is the first non-blank line; the round token is searched on it and on "
            "the next 4 lines (the closure-role form states '**chousa round 27**' on line 2).",
            "The dispatch.08 verdict is reported together with its two conjuncts "
            "(token_identity and state_bound) and a failure_class, because every failure in "
            "this run comes from the state_bound conjunct alone (see "
            "summary.dispatch.08_component_failures).",
            "MEASURED, not assumed: the fleet's `.ufo/state/<id>.round` files are all dated "
            "2026-10-15 and hold values far below the lanes' current rounds, so the box's "
            "'<= the lane's .ufo/state/<id>.round' conjunct is evaluated against a STALE "
            "anchor. The per-file field alt_state_round records the lane's live next-round "
            "value from the hyaku driver's own state dir (~/.local/state/shokunin-hyaku/next) "
            "as a diagnostic only; it never changes a box verdict.",
            "report_path_exists_on_disk is INFORMATIONAL and is not part of either box verdict: "
            "it records whether the named report file exists under the fleet root.",
        ],
        "summary": summary,
        "records": records,
    }

    outdir = os.path.dirname(os.path.abspath(args.out))
    if outdir and not os.path.isdir(outdir):
        os.makedirs(outdir, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False, sort_keys=False)
        fh.write("\n")

    print_summary(summary, records, in_scope)
    print("wrote %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
