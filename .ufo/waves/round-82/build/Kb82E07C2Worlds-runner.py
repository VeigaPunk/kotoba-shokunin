#!/usr/bin/env python3
"""Kb82E07C2Worlds -- C2 independent discriminator runner (round 82).

Independent harness for the operability repair of
verifiers/verify_skill_checklist.py --self-test.  The failing named arm
"governance: live round-65 corrections land, errata-excused" reads the live
LOG.md / SCORECARD.md (and, via ../ corrected tokens, paths outside the
repo), so a fixture-only repair must prove the round-65 correction
machinery against isolated worlds instead.

Worlds (each an isolated temp repo: LOG.md + SCORECARD.md + corpus/):
  W1 valid-correction        -> green: 1 recorded correction excused
  W2 missing-correction      -> red: stale token named
  W3 stale-target-restored   -> red: "stale, the old token now resolves"
  W4 unrelated-dead-citation -> red: unrelated subject named, no masking
  W5 guard-disabled (5x)     -> red: byte-pin / wording / horizon /
                                live-subject / corrected-token guards are
                                load-bearing in the replacement fixture
  W6 live-drift independence -> mutating a scratch copy's live SCORECARD.md
                                between two selftest runs must not change
                                the fixture-arm results (hermetic patch), or
                                exposes the base defect (live coupling)

Usage:
  runner.py --verifier <path/to/verify_skill_checklist.py> \
            [--receipts <dir>] [--selftest-repo <repocopy>] [--tag <label>]

W6 runs only when --selftest-repo names a scratch copy of the whole repo;
it shells out to `python3 -B verifiers/verify_skill_checklist.py --self-test`
there, appends one dead citation to SCORECARD.md, re-runs, and diffs.
Exit 0 iff every executed world discriminates as required.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

NOTICE = ('SCORECARD.md:9 token "corpus/gone.md" -> '
          '"corpus/live.md" (round-65 notice).')


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_world(root: Path, *, extra_dead: bool = False) -> None:
    """Fixture repo mirroring the selftest's own hermetic pattern."""
    (root / "corpus").mkdir(parents=True)
    (root / "corpus" / "live.md").write_text("", encoding="utf-8")
    (root / "LOG.md").write_text(
        "`corpus/live.md`\n%s\n" % NOTICE, encoding="utf-8")
    score = "padding line\n" * 8 + "`corpus/gone.md`\n"
    if extra_dead:
        score += "`corpus/other-dead.md`\n"
    (root / "SCORECARD.md").write_text(score, encoding="utf-8")


def correction_row(sline: int = 9, stale: str = "corpus/gone.md",
                   corrected: str = "corpus/live.md") -> tuple:
    return (2, sha(NOTICE), "SCORECARD.md", sline, stale, corrected)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verifier", required=True)
    ap.add_argument("--receipts", default=None)
    ap.add_argument("--selftest-repo", default=None)
    ap.add_argument("--tag", default="run")
    args = ap.parse_args()

    vpath = Path(args.verifier).resolve()
    spec = importlib.util.spec_from_file_location("vsc_under_test", vpath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    results: list[dict] = []

    def run_case(name: str, repo: Path, *, errata=(), horizon=None,
                 corrections=(), corrh=None):
        kw = {}
        if horizon is not None:
            kw["horizon"] = horizon
        if corrh is not None:
            kw["corrections_horizon"] = corrh
        out = mod.check_governance_citations(
            repo, errata=errata, corrections=corrections, **kw)
        results.append({"world": name, "verifier": str(vpath),
                        "repo": str(repo), "out": out})
        return out

    with tempfile.TemporaryDirectory(
            prefix="kotoba-c2worlds-", dir=os.environ.get("TMPDIR")) as td:
        td_path = Path(td)

        # W1 valid correction -> green
        w1 = td_path / "w1"; build_world(w1)
        st, ev, det = run_case("W1-valid-correction", w1,
                               corrections=(correction_row(),), corrh=2)
        ok = st == "PASS" and "1 recorded correction(s) excused" in det
        results[-1]["expect"] = "PASS / 1 correction excused"
        results[-1]["discriminates"] = ok

        # W2 missing correction -> red
        w2 = td_path / "w2"; build_world(w2)
        st, ev, det = run_case("W2-missing-correction", w2, corrections=(),
                               corrh=2)
        ok = st == "FAIL" and "corpus/gone.md" in det
        results[-1]["expect"] = "FAIL names corpus/gone.md"
        results[-1]["discriminates"] = ok

        # W3 stale target restored -> red
        w3 = td_path / "w3"; build_world(w3)
        (w3 / "corpus" / "gone.md").write_text("", encoding="utf-8")
        st, ev, det = run_case("W3-stale-target-restored", w3,
                               corrections=(correction_row(),), corrh=2)
        ok = st == "FAIL" and "stale, the old token now resolves" in det
        results[-1]["expect"] = "FAIL stale-token-restored"
        results[-1]["discriminates"] = ok

        # W4 unrelated dead citation -> red (no masking)
        w4 = td_path / "w4"; build_world(w4, extra_dead=True)
        st, ev, det = run_case("W4-unrelated-dead-citation", w4,
                               corrections=(correction_row(),), corrh=2)
        ok = (st == "FAIL" and "corpus/other-dead.md" in det
              and "1 recorded correction(s) excused" in det)
        results[-1]["expect"] = ("FAIL names corpus/other-dead.md; named "
                                 "correction still excused")
        results[-1]["discriminates"] = ok

        # W5 guard-disabled variants -> each red
        guards = [
            ("W5a-digest-drift", dict(corrections=((2, "0" * 64) +
                                                  correction_row()[2:],),
                                      corrh=2), "drifted"),
            ("W5b-wording", dict(corrections=(correction_row()[:4]
                                              + ("corpus/x.md",)
                                              + correction_row()[5:],),
                                 corrh=2), "wording"),
            ("W5c-past-horizon", dict(corrections=(correction_row(),),
                                      corrh=1), "past horizon"),
            ("W5d-no-live-subject", dict(corrections=(correction_row()[:3]
                                                      + (8,)
                                                      + correction_row()[4:],),
                                         corrh=2), "names no live red"),
            ("W5e-corrected-dead", dict(corrections=(correction_row()[:5]
                                                     + ("corpus/absent.md",),
                                                     ), corrh=2),
             "does not resolve"),
        ]
        for name, kw, needle in guards:
            wd = td_path / name.lower(); build_world(wd)
            st, ev, det = run_case(name, wd, **kw)
            ok = st == "FAIL" and needle in det
            results[-1]["expect"] = "FAIL mentions %r" % needle
            results[-1]["discriminates"] = ok

    # W6 live-drift independence (subprocess; only with a repo copy)
    w6 = {"world": "W6-live-drift-independence", "ran": False}
    if args.selftest_repo:
        rep = Path(args.selftest_repo).resolve()
        script = rep / "verifiers" / "verify_skill_checklist.py"
        env = dict(os.environ)
        def run_selftest() -> tuple[int, str]:
            p = subprocess.run(
                [sys.executable, "-B", str(script), "--self-test"],
                cwd=rep, env=env, capture_output=True, text=True)
            return p.returncode, p.stdout + p.stderr
        rc1, out1 = run_selftest()
        sc = rep / "SCORECARD.md"
        snapshot = sc.read_text(encoding="utf-8")
        with sc.open("a", encoding="utf-8") as fh:
            fh.write("\n`corpus/lesson-definitely-absent-round82.md`\n")
        rc2, out2 = run_selftest()
        sc.write_text(snapshot, encoding="utf-8")
        same = (rc1 == rc2 and out1 == out2)
        w6.update({"ran": True, "repo": str(rep),
                   "rc_before": rc1, "rc_after_mutation": rc2,
                   "outputs_identical": same,
                   "tail_before": out1.strip().splitlines()[-1:],
                   "tail_after": out2.strip().splitlines()[-1:]})
    results.append(w6)

    passed = sum(1 for r in results
                 if r.get("discriminates") or (r["world"].startswith("W6")
                                               and r.get("ran")
                                               and r.get("outputs_identical")))
    verdict = all(r.get("discriminates", False) for r in results[:6])
    if w6["ran"]:
        verdict = verdict and w6["outputs_identical"]

    summary = {
        "tag": args.tag,
        "verifier_under_test": str(vpath),
        "verifier_sha256": sha(vpath.read_bytes().decode("utf-8", "replace"))
        if False else hashlib.sha256(vpath.read_bytes()).hexdigest(),
        "worlds_total": len(results),
        "worlds_discriminating": sum(1 for r in results
                                     if r.get("discriminates")),
        "w6_ran": w6["ran"],
        "verdict": "PASS" if verdict else "FAIL",
    }
    print(json.dumps({"summary": summary, "worlds": results}, indent=2))

    if args.receipts:
        rdir = Path(args.receipts); rdir.mkdir(parents=True, exist_ok=True)
        (rdir / ("worlds-%s.json" % args.tag)).write_text(
            json.dumps({"summary": summary, "worlds": results}, indent=2),
            encoding="utf-8")
        (rdir / ("summary-%s.txt" % args.tag)).write_text(
            "\n".join("%s: %s" % (r["world"], "DISCRIMINATES" if
                                  r.get("discriminates") else
                                  ("IDENTICAL-UNDER-LIVE-DRIFT" if
                                   r.get("outputs_identical") else "NO"))
                      for r in results) + "\nverdict=%s\n" % summary["verdict"],
            encoding="utf-8")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
