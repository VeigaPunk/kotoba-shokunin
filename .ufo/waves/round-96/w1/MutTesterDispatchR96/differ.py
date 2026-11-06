#!/usr/bin/env python3
"""MutTesterDispatchR96 differential witness driver (round 96, wave r96-w1; NOT a lane file).

For every mutant in probe.py's table, exhibit an input on which the honest instrument and the
mutated instrument disagree (a real behavioural difference, not an equivalent mutant), or --
for the three mutants named equivalent -- show that a corpus of inputs produces identical
results and state the static reason.

Usage: python3 -B differ.py REV REPO
Exit 0 all witnesses resolved, 2 could-not-evaluate. Never edits the lane.
"""
from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
INSTRUMENT = "verifiers/verify_dispatch_prompts.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("probe_r96", HERE / "probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_module(path: Path, text: str, name: str):
    mod = types.ModuleType(name)
    mod.__file__ = str(path)
    exec(compile(text, str(path), "exec", dont_inherit=True), mod.__dict__)
    return mod


def tree(root: Path, name: str, files: dict[str, str], state: dict[str, str],
         fleet_dirs: list[str], fleet_files: list[str]) -> Path:
    case = root / name
    (case / "prompts").mkdir(parents=True, exist_ok=True)
    (case / "state").mkdir(parents=True, exist_ok=True)
    (case / "fleet").mkdir(parents=True, exist_ok=True)
    for fn, text in files.items():
        (case / "prompts" / fn).write_text(text, encoding="utf-8")
    for fn, text in state.items():
        (case / "state" / fn).write_text(text, encoding="utf-8")
    for d in fleet_dirs:
        (case / "fleet" / d).mkdir(parents=True, exist_ok=True)
    for f in fleet_files:
        (case / "fleet" / f).write_text("fixture marker\n", encoding="utf-8")
    return case


GOOD = "You are the kote L1, round 7. Working dir: /fleet/kote-shokunin.\n\nWrite the round report at `/fleet/.ufo/reports/round-7/kote.md` on the\nmain repo. | godspeed\n"


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: differ.py REV REPO", file=sys.stderr)
        return 2
    rev, repo = argv
    got = subprocess.run(["git", "-C", repo, "rev-parse", "--verify", "-q", rev + "^{commit}"],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if got.returncode != 0:
        print("DIFFER-NOT-EVALUATED: REV %s is not a commit of %s" % (rev, repo))
        return 2
    rev = got.stdout.decode().strip()
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r96" / "differ"
    root.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="run.", dir=root))
    try:
        clone = work / "world" / "kotoba-shokunin"
        clone.parent.mkdir()
        for cmd in (["git", "clone", "-q", "--shared", repo, str(clone)],
                    ["git", "-C", str(clone), "checkout", "-q", rev]):
            if subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
                print("DIFFER-NOT-EVALUATED: clone or checkout failed")
                return 2
        path = clone / INSTRUMENT
        original = path.read_text(encoding="utf-8")
        honest = load_module(path, original, "instrument_honest")
        probe = load_probe()
        fx = work / "fx"
        fx.mkdir()
        print("differ rev %s instrument %s" % (rev, INSTRUMENT))

        def mutated(mid: str):
            for m in probe.MUTANTS:
                if m[0] == mid:
                    assert original.count(m[1]) == 1, mid
                    return load_module(path, original.replace(m[1], m[2]), "instrument_" + mid)
            raise KeyError(mid)

        def show(mid: str, what: str, a, b) -> None:
            print("%-32s %-46s honest=%r mutant=%r %s"
                  % (mid, what, a, b, "DIFFERS" if a != b else "IDENTICAL"))

        # m01: a report path followed by a sentence period
        m = mutated("m01-rstrip-dot")
        t = "Write it at .ufo/reports/round-7/kote.md. Then stop."
        show("m01-rstrip-dot", "report_paths(sentence-final dot)",
             honest.report_paths(t), m.report_paths(t))

        # m02: an empty baseline file
        c = tree(fx, "emptybase", {"kote-round-7.md": GOOD},
                 {"kote.report-baseline": ""}, ["kote-shokunin"], [])
        m = mutated("m02-empty-baseline")
        show("m02-empty-baseline", "state_source(empty baseline)",
             honest.state_source(c / "state", "kote"), m.state_source(c / "state", "kote"))

        # m03: a fleet-root role whose report stem is not the lane id
        c = tree(fx, "fleetroot", {"agg-round-7.md": GOOD.replace("kote", "agg")},
                 {"agg.round": "7"}, [], [])
        m = mutated("m03-fleetroot-stem-pass")
        hf = honest.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        mf = m.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        show("m03-fleetroot-stem-pass", "fleet-root report_stem_is_lane_id",
             hf["files"][0]["conjuncts"]["report_stem_is_lane_id"]["status"],
             mf["files"][0]["conjuncts"]["report_stem_is_lane_id"]["status"])

        # m04: a lane known only by its .report-baseline state file
        c = tree(fx, "onlybaseline", {"agg-round-7.md": GOOD.replace("kote", "agg")},
                 {"agg.report-baseline": "9 " + "0" * 64 + "\n"}, [], [])
        m = mutated("m04-fleetroot-no-baseline")
        show("m04-fleetroot-no-baseline", "lane_kind(baseline-only lane)",
             honest.lane_kind("agg", c / "fleet", c / "state"),
             m.lane_kind("agg", c / "fleet", c / "state"))

        # m05: an empty '<>' in a report path
        m = mutated("m05-placeholder-empty-angle")
        show("m05-placeholder-empty-angle", "has_placeholder('kote<>')",
             honest.has_placeholder("kote<>"), m.has_placeholder("kote<>"))

        # m06: a plain file named <lane>-shokunin
        c = tree(fx, "laneisfile", {"kote-round-7.md": GOOD}, {"kote.report-baseline": "9\n"},
                 [], ["kote-shokunin"])
        m = mutated("m06-sibling-file-as-lane")
        show("m06-sibling-file-as-lane", "lane_kind(<lane>-shokunin is a file)",
             honest.lane_kind("kote", c / "fleet", c / "state"),
             m.lane_kind("kote", c / "fleet", c / "state"))

        # m07: a report dir without the round- prefix
        m = mutated("m07-report-regex-noprefix")
        t = "land it at .ufo/reports/7/kote.md now"
        show("m07-report-regex-noprefix", "report_paths(.ufo/reports/7/kote.md)",
             honest.report_paths(t), m.report_paths(t))

        # m08: 'round7' with no space
        m = mutated("m08-role-regex-nospace")
        t = "You are the kote L1, round7 of up to 1024."
        show("m08-role-regex-nospace", "role_round(round7)", honest.role_round(t),
             m.role_round(t))

        # m09: the fleet-root out-of-scope reason text (equivalent)
        m = mutated("m09-outofscope-reason")
        c = tree(fx, "fleetroot2", {"agg-round-7.md": GOOD.replace("kote", "agg")},
                 {"agg.round": "7"}, [], [])
        hf = honest.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        mf = m.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        hreason = hf["out_of_scope"][0]["reason"]
        mreason = mf["out_of_scope"][0]["reason"]
        print("%-32s %-46s honest=%r mutant=%r %s"
              % ("m09-outofscope-reason", "out_of_scope[0]['reason']", hreason, mreason,
                 "DIFFERS (text only)" if hreason != mreason else "IDENTICAL"))
        print("%-32s %-46s %s" % ("m09-outofscope-reason", "verdicts/statuses identical",
                                  "YES" if hf["files"] == mf["files"] and hf["status"] == mf["status"]
                                  else "NO"))

        # m10: the per-file note on a file with no report path
        m = mutated("m10-file-note-dropped")
        c = tree(fx, "nopath", {"kote-round-7.md": "You are the kote L1, round 7.\nNo path.\n"},
                 {"kote.report-baseline": "9\n"}, ["kote-shokunin"], [])
        hf = honest.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        mf = m.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        show("m10-file-note-dropped", "file['note'] on a no-path file",
             hf["files"][0].get("note"), mf["files"][0].get("note"))

        # m11: evaluated counts a FAILing file
        m = mutated("m11-evaluated-pass-only")
        c = tree(fx, "onefail", {"kote-round-7.md": GOOD.replace("/round-7/kote.md", "/round-7/other.md")},
                 {"kote.report-baseline": "9\n"}, ["kote-shokunin"], [])
        hf = honest.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        mf = m.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        show("m11-evaluated-pass-only", "evaluated with one FAILing file",
             hf["evaluated"], mf["evaluated"])

        # m12: an unreadable baseline (mode 000, so read_text raises OSError)
        c = tree(fx, "unreadable", {"kote-round-7.md": GOOD},
                 {"kote.report-baseline": "9\n"}, ["kote-shokunin"], [])
        os.chmod(c / "state" / "kote.report-baseline", 0o000)
        m = mutated("m12-unreadable-as-baseline")
        try:
            show("m12-unreadable-as-baseline", "state_source(unreadable baseline)",
                 honest.state_source(c / "state", "kote"),
                 m.state_source(c / "state", "kote"))
        finally:
            os.chmod(c / "state" / "kote.report-baseline", 0o644)

        # m13: a lane known only by its legacy .round file
        c = tree(fx, "legacyonly", {"agg-round-7.md": GOOD.replace("kote", "agg")},
                 {"agg.round": "7"}, [], [])
        m = mutated("m13-lane-kind-legacy-dropped")
        show("m13-lane-kind-legacy-dropped", "lane_kind(legacy-only lane)",
             honest.lane_kind("agg", c / "fleet", c / "state"),
             m.lane_kind("agg", c / "fleet", c / "state"))

        # m14: the check status with exactly one failing file
        m = mutated("m14-finish-single-fail-na")
        c = tree(fx, "onefail2", {"kote-round-7.md": GOOD.replace("/round-7/kote.md", "/round-7/other.md")},
                 {"kote.report-baseline": "9\n"}, ["kote-shokunin"], [])
        hf = honest.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        mf = m.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        show("m14-finish-single-fail-na", "check status with one failing file",
             hf["status"], mf["status"])

        # m15 / m16: claimed equivalent -- differential corpus must be identical
        corpus = [
            "land under .ufo/reports/round-4/. Re-read.",
            "at `/x/.ufo/reports/round-9/kote.md` now",
            "Write it at .ufo/reports/round-7/kote.md. Then stop.",
            "Write it at .ufo/reports/round-7/kote.md; then",
            "Write it at .ufo/reports/round-7/kote.md, then",
            "Write it at .ufo/reports/round-7/kote.md: then",
            "paths .ufo/reports/round-7/a.md .ufo/reports/round-8/b.md",
            ".ufo/reports/round-4/..",
            ".ufo/reports/round-4/.",
            ".ufo/reports/round-4/...",
            ".ufo/reports/round-4/<>",
            ".ufo/reports/round-4/$X",
            ".ufo/reports/round-4/${X}",
            ".ufo/reports/round-4/kote.md.",
            ".ufo/reports/round-12/kote",
            "no path here at all",
        ]
        for mid in ("m15-has-placeholder-redundant", "m16-dotdot-skip"):
            m = mutated(mid)
            same = all(honest.report_paths(t) == m.report_paths(t) for t in corpus)
            print("%-32s %-46s %s" % (mid, "report_paths over %d texts" % len(corpus),
                                      "IDENTICAL" if same else "DIFFERS"))
        # m15 also runs through evaluate_dispatch_04: compare on the same corpus
        m = mutated("m15-has-placeholder-redundant")
        same = True
        for i, t in enumerate(corpus):
            c = tree(fx, "corpus%d" % i, {"kote-round-7.md": t},
                     {"kote.report-baseline": "9\n"}, ["kote-shokunin"], [])
            hf = honest.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
            mf = m.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
            same = same and hf == mf
        print("%-32s %-46s %s" % ("m15-has-placeholder-redundant",
                                  "evaluate_dispatch_04 over %d texts" % len(corpus),
                                  "IDENTICAL" if same else "DIFFERS"))

        # m18: the baseline round read from the last field
        c = tree(fx, "baseline", {"kote-round-7.md": GOOD},
                 {"kote.report-baseline": "9 " + "0" * 64 + "\n"}, ["kote-shokunin"], [])
        m = mutated("m18-state-last-field")
        show("m18-state-last-field", "state_source('9 <64 zeros>')",
             honest.state_source(c / "state", "kote"), m.state_source(c / "state", "kote"))

        # m19: only the first conjunct decides the file verdict
        m = mutated("m19-file-first-conjunct-only")
        c = tree(fx, "wrongstem", {"kote-round-7.md": GOOD.replace("/round-7/kote.md", "/round-7/other.md")},
                 {"kote.report-baseline": "9\n"}, ["kote-shokunin"], [])
        hf = honest.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        mf = m.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
        show("m19-file-first-conjunct-only", "file verdict with a wrong stem",
             hf["files"][0]["verdict"], mf["files"][0]["verdict"])
        return 0
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
