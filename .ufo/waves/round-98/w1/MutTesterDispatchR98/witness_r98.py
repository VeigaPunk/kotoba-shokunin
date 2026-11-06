#!/usr/bin/env python3
"""witness_r98.py -- differential witnesses for the probe_r98 mutant table.

Usage: witness_r98.py REV REPO [--only id,...]

Loads the honest instrument (git show REV:verifiers/verify_dispatch_prompts.py)
and each mutant as a module, builds the SAME fixture input for both, and prints
the observed difference (honest vs mutant).  No subprocess, no lane write.
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from probe_r98 import MUTANTS  # noqa: E402

GOOD = """You are the kote L1, round 7. Working dir: /fleet/kote-shokunin.

L0 template (must not trip dispatch.04): `<lane> | round-<N> | <question>`

Write the round report at `/fleet/.ufo/reports/round-7/kote.md` on the
main repo. | godspeed
"""


def load(path: Path, tag: str):
    spec = importlib.util.spec_from_file_location("inst_" + tag, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def case(root: Path, name: str, files: dict[str, str],
         baseline: str | None = None, legacy: str | None = None,
         repo: bool = True) -> Path:
    c = root / name
    (c / "prompts").mkdir(parents=True, exist_ok=True)
    (c / "state").mkdir(parents=True, exist_ok=True)
    (c / "fleet").mkdir(parents=True, exist_ok=True)
    if repo:
        (c / "fleet" / "kote-shokunin").mkdir(parents=True, exist_ok=True)
    for fname, text in files.items():
        (c / "prompts" / fname).write_text(text, encoding="utf-8")
    if baseline is not None:
        (c / "state" / "kote.report-baseline").write_text(
            baseline + " " + "0" * 64 + "\n", encoding="utf-8")
    if legacy is not None:
        (c / "state" / "kote.round").write_text(legacy + "\n", encoding="utf-8")
    return c


def build_proof(mod, root: Path):
    proof = root / "proof"
    fx = proof / "fixtures" / "dispatch-prompts"
    fx.mkdir(parents=True, exist_ok=True)
    (proof / "verifiers").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(LANE / "SKILL.md", proof / "SKILL.md")
    box_map = {"schema": "kotoba-checklist-map-v1",
               "boxes": [{"box_id": cid,
                          "section": "Dispatch-prompt fidelity checklist",
                          "text_sha256": mod.PINNED_BOX_SHA[cid],
                          "disposition": "delegated:" + mod.DELEGATION_TARGET}
                         for cid in mod.CHECK_IDS]}
    map_path = proof / "verifiers" / mod.BASELINE_NAME
    map_path.write_text(json.dumps(box_map, indent=2, sort_keys=True),
                        encoding="utf-8")
    cases = mod._proof_fixture_corpus(fx)
    write_manifest(fx, cases)
    return proof, map_path, fx, cases


def write_manifest(fx: Path, cases: list[dict]) -> None:
    (fx / "manifest.json").write_text(
        json.dumps({"schema": "kotoba-dispatch-fixtures-v1", "cases": cases,
                    "note": "witness corpus"}, indent=2, sort_keys=True),
        encoding="utf-8")


def run_proof(mod, map_path: Path, fx: Path) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = mod.box_proof(map_path, fx)
    return code, out.getvalue().strip(), err.getvalue().strip()


def run_main(mod, argv: list[str]) -> tuple[int, str]:
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        code = mod.main(argv)
    return code, out.getvalue().strip()


# --- one witness per mutant id: f(mod, root) -> JSON-able observation ---------

def w_n01(mod, root):
    c = case(root, "n01", {"kote-L1.md.bak": GOOD})
    r = mod.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
    return {"evaluated": r["evaluated"], "status": r["status"],
            "out_of_scope": [o["file"] for o in r["out_of_scope"]]}


def w_n02(mod, root):
    c = case(root, "n02", {"kote-round-7.md": GOOD.replace("round 7.", "round 8.")},
             baseline="9")
    r = mod.evaluate_dispatch_08(c / "prompts", c / "state", c / "fleet")
    f = mod._verdict_of(r, "kote-round-7.md")
    return {"file_verdict": f["verdict"],
            "role": f["conjuncts"]["filename_role_round_equal"]["status"]}


def w_n03(mod, root):
    _p, mp, fx, _c = build_proof(mod, root)
    m = json.loads(mp.read_text(encoding="utf-8"))
    for e in m["boxes"]:
        if e["box_id"] == "dispatch.04":
            e["text_sha256"] = "0" * 64
    mp.write_text(json.dumps(m, indent=2, sort_keys=True), encoding="utf-8")
    code, out, err = run_proof(mod, mp, fx)
    return {"rc": code, "out": out, "err": err.splitlines()[-1] if err else ""}


def w_n04(mod, root):
    proof, mp, fx, _c = build_proof(mod, root)
    (proof / "SKILL.md").unlink()
    code, out, err = run_proof(mod, mp, fx)
    return {"rc": code, "out": out, "err": err.splitlines()[-1] if err else ""}


def w_n05(mod, root):
    _p, mp, fx, cases = build_proof(mod, root)
    twin = dict(next(c for c in cases if c["id"] == "d04-stem"))
    twin["id"] = "d04-stem-labelled-pass"
    twin["expect_verdict"] = "PASS"
    write_manifest(fx, cases + [twin])
    code, out, err = run_proof(mod, mp, fx)
    return {"rc": code, "out": out,
            "err": [ln for ln in err.splitlines() if "verdict" in ln][:1]}


def w_n06(mod, root):
    _p, mp, fx, cases = build_proof(mod, root)
    ctl = next(c for c in cases if c["id"] == "d04-control")
    ctl["expect_conjunct"] = "report_path_literal"
    ctl["expect_conjunct_status"] = "FAIL"
    write_manifest(fx, cases)
    code, out, err = run_proof(mod, mp, fx)
    return {"rc": code, "out": out,
            "err": [ln for ln in err.splitlines() if "conjunct" in ln][:1]}


def w_n07(mod, root):
    c = case(root, "n07", {"kote-round-7.md": GOOD}, baseline="9")
    rs = mod.run_checks(c / "prompts", c / "state", c / "fleet",
                        ["dispatch.04", "dispatch.08"])
    return {"results": [r["id"] for r in rs]}


def w_n08(mod, root):
    c = case(root, "n08",
             {"kote-round-7.md": GOOD.replace("/round-7/kote.md", "/round-7/other.md")},
             baseline="9")
    rc, out = run_main(mod, ["--prompts", str(c / "prompts"),
                             "--state-dir", str(c / "state"),
                             "--fleet", str(c / "fleet")])
    return {"rc": rc, "out": out.splitlines()[:1]}


def w_n09(mod, root):
    c = case(root, "n09", {"kote-round-7.md": GOOD.replace("round 7.", "round 6.")},
             baseline="9")
    rc, out = run_main(mod, ["--prompts", str(c / "prompts"),
                             "--state-dir", str(c / "state"),
                             "--fleet", str(c / "fleet"),
                             "--check", "dispatch.04"])
    return {"rc": rc, "out": out.splitlines()}


def w_n10(mod, root):
    c = case(root, "n10", {"kote-round-7.md": GOOD}, baseline="9")
    p = c / "prompts" / "kote-round-7.md"
    p.chmod(0o000)
    try:
        try:
            r = mod.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
            obs = {"raised": None, "evaluated": r["evaluated"],
                   "status": r["status"]}
        except Exception as exc:  # noqa: BLE001
            obs = {"raised": exc.__class__.__name__, "text": str(exc)[:80]}
    finally:
        p.chmod(0o600)
    return obs


def w_n11(mod, root):
    _p, mp, fx, cases = build_proof(mod, root)
    ctl = next(c for c in cases if c["id"] == "d04-control")
    ctl["file"] = "kote-round-7"
    write_manifest(fx, cases)
    code, out, err = run_proof(mod, mp, fx)
    return {"rc": code, "out": out,
            "err": [ln for ln in err.splitlines() if "not evaluated" in ln][:1]}


def w_n12(mod, root):
    text = ("You are the kote L1, round 7. Working dir: /fleet/kote-shokunin.\n\n"
            "Write the report at `.ufo/reports/round-7/..`. | godspeed\n")
    c = case(root, "n12", {"kote-round-7.md": text}, baseline="9")
    r = mod.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
    f = mod._verdict_of(r, "kote-round-7.md")
    return {"paths": mod.report_paths(text), "status": r["status"],
            "file_verdict": f["verdict"],
            "stem": f["conjuncts"]["report_stem_is_lane_id"]["status"]}


def w_n13(mod, root):
    _p, mp, fx, _c = build_proof(mod, root)
    m = json.loads(mp.read_text(encoding="utf-8"))
    good = next(e for e in m["boxes"] if e["box_id"] == "dispatch.04")
    bad = dict(good)
    bad["disposition"] = "executed:elsewhere.py"
    m["boxes"] = [bad] + [e for e in m["boxes"] if e["box_id"] != "dispatch.04"] + [good]
    mp.write_text(json.dumps(m, indent=2, sort_keys=True), encoding="utf-8")
    code, out, err = run_proof(mod, mp, fx)
    return {"rc": code, "out": out,
            "err": [ln for ln in err.splitlines() if "disposition" in ln][:1]}


def w_n14(mod, root):
    text7 = GOOD.replace("round 7.", "round 6.")
    text8 = ("You are the kote L1, round 8. Working dir: /fleet/kote-shokunin.\n\n"
             "Land the notes. | godspeed\n")
    c = case(root, "n14", {"kote-round-7.md": text7, "kote-round-8.md": text8},
             baseline="9")
    r = mod.evaluate_dispatch_08(c / "prompts", c / "state", c / "fleet")
    return {"status": r["status"], "evaluated": r["evaluated"],
            "detail": r["detail"]}


def w_n15(mod, root):
    text = ("notes for the round\n\n"
            "Write it at `.ufo/reports/round-7/kote.md`.\n")
    c = case(root, "n15", {"notes.txt": text}, baseline="9")
    r = mod.evaluate_dispatch_04(c / "prompts", c / "state", c / "fleet")
    return {"evaluated": r["evaluated"], "status": r["status"],
            "out_of_scope": [o["file"] for o in r["out_of_scope"]]}


def w_n16(mod, root):
    _p, mp, fx, _c = build_proof(mod, root)
    code, out, err = run_proof(mod, mp, fx)
    return {"rc": code, "out": out,
            "err": [ln for ln in err.splitlines() if "live SKILL.md" in ln][:1]}


def w_n17(mod, root):
    _p, mp, fx, _c = build_proof(mod, root)
    code, out, err = run_proof(mod, mp, fx)
    return {"rc": code, "out": out,
            "err": [ln for ln in err.splitlines() if "no isolated" in ln][:2]}


def w_n18(mod, root):
    files = [{"file": "a", "verdict": "N/A", "conjuncts": {}}]
    r = mod._finish("x", files, [])
    return {"status": r["status"], "detail": r["detail"]}


def w_n19(mod, root):
    c = case(root, "n19", {"kote-round-7.md": GOOD}, legacy="6")
    (c / "state" / "kote.report-baseline").mkdir()
    return {"state_source": mod.state_source(c / "state", "kote")}


def w_n20(mod, root):
    lines = ["## Dispatch-prompt fidelity checklist", ""]
    for i in range(1, 11):
        lines.append("- [ ] dispatch box %d text" % i)
    text = "\n".join(lines) + "\n"
    try:
        out = mod.dispatch_box_sha256(text)
        return {"keys": len(out), "last": sorted(out)[-1]}
    except Exception as exc:  # noqa: BLE001
        return {"raised": exc.__class__.__name__, "text": str(exc)[:80]}


WITNESSES = {
    "n01-l1-suffix-unanchored": w_n01,
    "n02-role-round-above": w_n02,
    "n03-proof-map-hash-unenforced": w_n03,
    "n04-proof-missing-skill-as-pinned": w_n04,
    "n05-proof-verdict-mismatch-unenforced": w_n05,
    "n06-proof-conjunct-status-unenforced": w_n06,
    "n07-runchecks-first-check-only": w_n07,
    "n08-main-fail-exit-zero": w_n08,
    "n09-main-check-ignored": w_n09,
    "n10-readtext-oserror-empty": w_n10,
    "n11-verdict-of-prefix": w_n11,
    "n12-report-stem-dotdot": w_n12,
    "n13-map-duplicate-first-wins": w_n13,
    "n14-finish-fails-nas": w_n14,
    "n15-outofscope-nonmd-evaluated": w_n15,
    "n16-box-section-ignored": w_n16,
    "n17-proof-case-first-only": w_n17,
    "n18-finish-na-count-zero": w_n18,
    "n19-state-baseline-exists": w_n19,
    "n20-box-ninth-limit": w_n20,
}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("rev")
    ap.add_argument("repo")
    ap.add_argument("--only", default="")
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    only = {s for s in args.only.split(",") if s}
    root = Path(tempfile.mkdtemp(prefix="witness."))
    try:
        shown = subprocess.run(["git", "-C", str(repo), "show",
                                "%s:%s" % (args.rev, INSTRUMENT)],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if shown.returncode != 0:
            print("NOT-EVALUATED: instrument absent at %s" % args.rev)
            return 2
        original = shown.stdout.decode("utf-8")
        print("witness rev %s repo %s" % (args.rev, repo))
        diffs = 0
        for name, anchor, repl, _defect in MUTANTS:
            if only and name not in only:
                continue
            hdir = root / (name + ".honest")
            mdir = root / (name + ".mutant")
            hdir.mkdir()
            mdir.mkdir()
            hp = hdir / "inst.py"
            mp = mdir / "inst.py"
            hp.write_text(original, encoding="utf-8")
            mp.write_text(original.replace(anchor, repl), encoding="utf-8")
            honest = load(hp, name + "-h")
            mutant = load(mp, name + "-m")
            fn = WITNESSES[name]
            h = fn(honest, hdir)
            m = fn(mutant, mdir)
            same = json.dumps(h, sort_keys=True) == json.dumps(m, sort_keys=True)
            diffs += 0 if same else 1
            print("%-40s %s" % (name, "SAME" if same else "DIFFERS"))
            print("  honest: %s" % json.dumps(h, sort_keys=True))
            print("  mutant: %s" % json.dumps(m, sort_keys=True))
        print("witnesses: %d DIFFERS" % diffs)
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
