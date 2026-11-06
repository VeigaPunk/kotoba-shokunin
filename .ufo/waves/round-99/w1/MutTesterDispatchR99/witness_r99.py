#!/usr/bin/env python3
"""witness_r99.py -- differential witnesses for the probe_r99 mutant table.

Usage: witness_r99.py REV REPO [--only id,...]

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

INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from probe_r99 import MUTANTS  # noqa: E402

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


def run_main(mod, argv: list[str]) -> tuple[int, str]:
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        code = mod.main(argv)
    return code, out.getvalue().strip()


def plain_file(root: Path, name: str) -> Path:
    p = root / name
    p.write_text("not a directory\n", encoding="utf-8")
    return p


# --- one witness per mutant id: f(mod, root) -> JSON-able observation ---------

def w_m01(mod, root):
    c = case(root, "m01", {"kote-round-7.md": GOOD}, baseline="9")
    bad = plain_file(root, "m01-file")
    code, out = run_main(mod, ["--prompts", str(bad),
                               "--state-dir", str(c / "state"),
                               "--fleet", str(c / "fleet")])
    return {"rc": code, "out": out}


def w_m02(mod, root):
    c = case(root, "m02", {"kote-round-7.md": GOOD}, baseline="9")
    p = c / "prompts" / "kote-round-7.md"
    p.chmod(0o000)
    try:
        code, out = run_main(mod, ["--prompts", str(c / "prompts"),
                                   "--state-dir", str(c / "state"),
                                   "--fleet", str(c / "fleet")])
    finally:
        p.chmod(0o600)
    return {"rc": code, "out": out}


def w_m03(mod, root):
    c = case(root, "m03", {"kote-round-7.md": GOOD}, baseline="9")
    bad = plain_file(root, "m03-file")
    code, out = run_main(mod, ["--json", "--prompts", str(bad),
                               "--state-dir", str(c / "state"),
                               "--fleet", str(c / "fleet")])
    try:
        payload = json.loads(out)
    except ValueError:
        return {"rc": code, "out": out}
    return {"rc": code, "json_exit_code": payload.get("exit_code"),
            "json_error": payload.get("error")}


def w_m04(mod, root):
    # the argv target passes; the module default target fails, so the
    # observation names which tree main() actually read
    a = case(root, "m04-argv", {"kote-round-7.md": GOOD}, baseline="9")
    b = case(root, "m04-default",
             {"kote-round-7.md": GOOD.replace("round 7.", "round 6.")},
             baseline="9")
    mod.DEFAULT_PROMPTS = b / "prompts"
    mod.DEFAULT_STATE_DIR = b / "state"
    mod.DEFAULT_FLEET = b / "fleet"
    code, out = run_main(mod, ["--prompts", str(a / "prompts"),
                               "--state-dir", str(a / "state"),
                               "--fleet", str(a / "fleet")])
    return {"rc": code, "out": out}


def w_m05(mod, root):
    c = case(root, "m05", {"kote-round-7.md": GOOD}, baseline="9")
    code, out = run_main(mod, ["--check", "dispatch.04",
                               "--check", "dispatch.08",
                               "--prompts", str(c / "prompts"),
                               "--state-dir", str(c / "state"),
                               "--fleet", str(c / "fleet")])
    lines = [ln for ln in out.splitlines() if ln.strip()]
    return {"rc": code, "lines": len(lines),
            "ids": [ln.split()[1].rstrip(":") for ln in lines]}


def w_m06(mod, root):
    c = case(root, "m06", {"kote-round-7.md": GOOD}, baseline="9")
    rs = mod.run_checks(c / "prompts", c / "state", c / "fleet",
                        ["dispatch.04", "dispatch.08"])
    return {"ids": [r["id"] for r in rs],
            "statuses": [r["status"] for r in rs]}


def w_m07(mod, root):
    c = case(root, "m07", {"kote-round-7.md": GOOD}, baseline="9")
    rs = mod.run_checks(c / "prompts", c / "state", c / "fleet",
                        ["dispatch.08"])
    return {"ids": [r["id"] for r in rs],
            "statuses": [r["status"] for r in rs]}


def w_m08(mod, root):
    c = case(root, "m08", {})
    p = c / "prompts" / "note.txt"
    p.write_text("caf\u00e9\n", encoding="utf-8")
    return {"text": mod.read_text(p, "prompt file")}


def w_m09(mod, root):
    c = case(root, "m09", {})
    p = c / "prompts" / "missing.md"
    try:
        mod.read_text(p, "prompt file")
        return {"exc": None}
    except mod.EnvError as exc:
        return {"exc": "EnvError", "msg": str(exc)}


def w_m19(mod, root):
    return {"lane_of a-L1-L1.md": list(mod.lane_of("a-L1-L1.md")),
            "lane_of kote-L1.md": list(mod.lane_of("kote-L1.md"))}


def w_m21(mod, root):
    # the fence sits at two leading spaces: FENCE_RE accepts 0-3, and the
    # box's own indent is 0, so the honest normalisation stops at the fence
    # line while the mutant hashes the fenced lines into the box text
    text = ("# Dispatch-prompt fidelity checklist\n\n"
            "- [ ] Box A first line.\n"
            "      continuation line\n"
            "  ```\n"
            "  fenced line\n"
            "  ```\n"
            "      after the fence\n")
    return {"hash": mod.dispatch_box_sha256(text)}


def w_m22(mod, root):
    c = case(root, "m22", {"kote-round-7.md": GOOD}, baseline="9")
    bad = plain_file(root, "m22-file")
    try:
        code, out = run_main(mod, ["--prompts", str(bad),
                                   "--state-dir", str(c / "state"),
                                   "--fleet", str(c / "fleet")])
        return {"rc": code, "out": out}
    except Exception as exc:
        return {"rc": "raised", "exc": "%s: %s" % (type(exc).__name__, exc)}


WITNESSES = {
    "m01-main-notdir-exit-zero": w_m01,
    "m02-main-env-error-exit-one": w_m02,
    "m03-main-json-exitcode-zero": w_m03,
    "m04-main-argv-ignored": w_m04,
    "m05-check-flag-not-repeatable": w_m05,
    "m06-runchecks-reversed": w_m06,
    "m07-runchecks-else-04": w_m07,
    "m08-readtext-latin1": w_m08,
    "m09-readtext-what-dropped": w_m09,
    "m19-l1-lane-nongreedy": w_m19,
    "m21-box-fenced-continuation": w_m21,
    "m22-main-dir-check-exists": w_m22,
}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("rev")
    ap.add_argument("repo")
    ap.add_argument("--only", default="")
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    only = {s for s in args.only.split(",") if s}
    root = Path(tempfile.mkdtemp(prefix="witness.",
                                 dir=os.environ.get("HYAKU_SCRATCH") or None))
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
            if name not in WITNESSES:
                print("%-40s NO-WITNESS (killed: the self-test observes it)"
                      % name)
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
