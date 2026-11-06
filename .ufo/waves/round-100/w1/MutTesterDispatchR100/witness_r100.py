#!/usr/bin/env python3
"""witness_r100.py -- differential witness per verdict-bearing survivor.

Usage: python3 -B witness_r100.py INSTRUMENT_PATH LABEL

Loads the honest instrument and each mutated text (from probe_r100.py's MUTANTS
table) as modules, calls the same function on the same fixture input, and prints
honest vs mutant.  No subprocess, no network, no git; every fixture lives under
TMPDIR.  A case prints DIFFERS only when the two modules really disagree.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOOD = """You are the kote L1, round 7. Working dir: /fleet/kote-shokunin.

L0 template (must not trip dispatch.04): `<lane> | round-<N> | <question>`

Write the round report at `/fleet/.ufo/reports/round-7/kote.md` on the
main repo. | godspeed
"""


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tree(root: Path, name: str, text: str, baseline: str | None = "9") -> Path:
    c = root / name
    (c / "prompts").mkdir(parents=True, exist_ok=True)
    (c / "state").mkdir(parents=True, exist_ok=True)
    (c / "fleet" / "kote-shokunin").mkdir(parents=True, exist_ok=True)
    (c / "prompts" / "kote-round-7.md").write_text(text, encoding="utf-8")
    if baseline is not None:
        (c / "state" / "kote.report-baseline").write_text(
            baseline + " " + "0" * 64 + "\n", encoding="utf-8")
    return c


def run_main(mod, argv):
    out_b, err_b = io.StringIO(), io.StringIO()
    rc = None
    try:
        with contextlib.redirect_stdout(out_b), contextlib.redirect_stderr(err_b):
            rc = mod.main(argv)
    except SystemExit as exc:
        rc = "SystemExit(%s)" % (exc.code,)
    except Exception as exc:  # noqa: BLE001 -- the witness reports the class
        rc = "raised %s" % type(exc).__name__
    return rc, out_b.getvalue(), err_b.getvalue()


def payload(out: str):
    try:
        return json.loads(out)
    except ValueError:
        return None


def argv_of(c: Path, extra=()):
    return list(extra) + ["--prompts", str(c / "prompts"),
                          "--state-dir", str(c / "state"),
                          "--fleet", str(c / "fleet")]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: witness_r100.py INSTRUMENT LABEL", file=sys.stderr)
        return 2
    inst_path, label = Path(argv[0]), argv[1]
    sys.path.insert(0, str(HERE))
    import probe_r100  # noqa: E402 -- the mutant table lives there
    original = inst_path.read_text(encoding="utf-8")
    work = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "witness"
    work.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix="w.", dir=work))
    differs = same = skipped = 0
    try:
        honest = load_module(inst_path, "honest_instrument")
        print("witness %s instrument %s sha256 %s"
              % (label, inst_path, __import__("hashlib").sha256(
                  inst_path.read_bytes()).hexdigest()))
        mods = {}
        for name, anchor, repl, _d in probe_r100.MUTANTS:
            mt = original.replace(anchor, repl)
            p = root / (name + ".py")
            p.write_text(mt, encoding="utf-8")
            mods[name] = load_module(p, "mut_" + name.replace("-", "_"))

        def case(cid: str, what: str, fn) -> None:
            nonlocal differs, same, skipped
            try:
                h = fn(honest)
                m = fn(mods[cid])
            except Exception as exc:  # noqa: BLE001
                print("CASE %-42s ERROR %r" % (cid, exc))
                skipped += 1
                return
            if h == m:
                same += 1
                verdict = "SAME"
            else:
                differs += 1
                verdict = "DIFFERS"
            print("CASE %-42s %-8s %s" % (cid, verdict, what))
            print("    honest %r" % (h,))
            print("    mutant %r" % (m,))

        # --- m01 / m02: a plain file as --state-dir -----------------------
        c = tree(root, "statefile", GOOD)
        state_file = c / "statefile"
        state_file.write_text("not a directory\n", encoding="utf-8")
        argv_state = ["--prompts", str(c / "prompts"),
                      "--state-dir", str(state_file),
                      "--fleet", str(c / "fleet")]

        def f_m01(mod):
            rc, out, err = run_main(mod, argv_state)
            return rc, "not a directory (state directory)" in err, out.strip()[:60]

        case("w01-substrate-state-fleet-unchecked", "plain file as --state-dir", f_m01)

        def f_m02(mod):
            rc, out, err = run_main(mod, argv_state)
            return rc, err.strip()

        case("w02-substrate-state-what-mislabeled", "the substrate message text", f_m02)

        # --- m03: the success --json payload's exit_code ------------------
        fail_tree = tree(root, "fail", GOOD.replace("/round-7/kote.md",
                                                    "/round-7/other.md"))
        pass_tree = tree(root, "pass", GOOD)
        na_tree = tree(root, "na", GOOD, baseline=None)

        def f_m03(mod):
            rc, out, err = run_main(mod, argv_of(fail_tree, ["--json"]))
            p = payload(out) or {}
            return rc, p.get("exit_code"), p.get("fail"), p.get("pass")

        case("w03-json-success-exitcode-zero", "FAIL run: rc, payload exit_code/fail/pass", f_m03)

        def f_m04(mod):
            rc, out, err = run_main(mod, argv_of(na_tree, ["--json"]))
            p = payload(out) or {}
            return rc, p.get("na"), [r.get("status") for r in p.get("checks", [])]

        case("w04-json-na-count-zero", "all-N/A run: payload na and statuses", f_m04)

        def f_m05(mod):
            rc, out, err = run_main(mod, argv_of(pass_tree, ["--json"]))
            p = payload(out) or {}
            return rc, p.get("pass"), p.get("fail"), p.get("na")

        case("w05-json-pass-count-zero", "PASS run: payload pass/fail/na", f_m05)

        def f_m06(mod):
            rc, out, err = run_main(mod, argv_of(fail_tree, ["--json"]))
            p = payload(out) or {}
            return rc, p.get("fail"), p.get("pass")

        case("w06-json-fail-count-zero", "FAIL run: payload fail/pass", f_m06)

        # --- m07 / m08: the EnvError --json payload -----------------------
        env_tree = tree(root, "env", GOOD)
        victim = env_tree / "prompts" / "kote-round-7.md"
        victim.chmod(0o000)
        try:
            if os.geteuid() == 0 or os.access(victim, os.R_OK):
                print("SKIP w07-enverror-json-exitcode-zero: a mode-000 file is "
                      "still readable as uid %d" % os.geteuid())
                print("SKIP w08-enverror-json-error-empty: same guard")
                skipped += 2
            else:
                def f_m07(mod):
                    rc, out, err = run_main(mod, argv_of(env_tree, ["--json"]))
                    p = payload(out) or {}
                    return rc, p.get("exit_code"), bool(p.get("error"))

                case("w07-enverror-json-exitcode-zero", "EnvError run: rc and payload exit_code", f_m07)

                def f_m08(mod):
                    rc, out, err = run_main(mod, argv_of(env_tree, ["--json"]))
                    p = payload(out) or {}
                    return rc, p.get("exit_code"), p.get("error")

                case("w08-enverror-json-error-empty", "EnvError run: payload error text", f_m08)
        finally:
            victim.chmod(0o600)

        # --- m09: read_text on invalid UTF-8 ------------------------------
        bad = root / "latin1.txt"
        bad.write_bytes(b"caf\xe9\n")

        def f_m09(mod):
            try:
                return ("returned", mod.read_text(bad, "prompt file"))
            except Exception as exc:  # noqa: BLE001
                return ("raised", type(exc).__name__)

        case("w09-readtext-errors-replace", "read_text on a non-UTF-8 byte", f_m09)

        # --- m10: run_checks duplicates -----------------------------------
        def f_m10(mod):
            rs = mod.run_checks(pass_tree / "prompts", pass_tree / "state",
                                pass_tree / "fleet",
                                ["dispatch.04", "dispatch.08"])
            return [r["id"] for r in rs]

        case("w10-runchecks-duplicate-first", "run_checks id list", f_m10)

        # --- m11: the --state-dir default ---------------------------------
        def f_m11(mod):
            old_p, old_s = mod.DEFAULT_PROMPTS, mod.DEFAULT_STATE_DIR
            mod.DEFAULT_PROMPTS = pass_tree / "prompts"
            mod.DEFAULT_STATE_DIR = pass_tree / "state"
            try:
                rc, out, err = run_main(mod, ["--prompts", str(pass_tree / "prompts"),
                                              "--fleet", str(pass_tree / "fleet")])
            finally:
                mod.DEFAULT_PROMPTS, mod.DEFAULT_STATE_DIR = old_p, old_s
            return rc, out.strip().splitlines()

        case("w11-parser-state-default-prompts", "no --state-dir: rc and result lines", f_m11)

        # --- m12: an unknown --check id -----------------------------------
        def f_m12(mod):
            rc, out, err = run_main(mod, argv_of(pass_tree, ["--check", "dispatch.09"]))
            return rc, out.strip().splitlines(), err.strip().splitlines()[-1:] 

        case("w12-parser-check-choices-dropped", "unknown --check id", f_m12)

        # --- m13: any vs all in the exit code -----------------------------
        def f_m13(mod):
            rc, out, err = run_main(mod, argv_of(fail_tree))
            return rc, out.strip().splitlines()

        case("w13-main-code-all-not-any", "one FAIL + one PASS: rc", f_m13)

        # --- m14: the default check set -----------------------------------
        def f_m14(mod):
            rc, out, err = run_main(mod, argv_of(pass_tree))
            return rc, out.strip().splitlines()

        case("w14-main-wanted-empty", "no --check: rc and result lines", f_m14)

        # --- m15: emit_json key order -------------------------------------
        def f_m15(mod):
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                mod.emit_json({"b": 1, "a": 2})
            return buf.getvalue()

        case("w15-emit-json-sort-keys-off", "emit_json key order", f_m15)

        # --- m16: the --box-proof default map path ------------------------
        proof = root / "proof"
        (proof / "verifiers").mkdir(parents=True)
        (proof / "fixtures").mkdir(parents=True)
        shutil.copy2(inst_path.parent / "checklist-baseline.json",
                     proof / "verifiers" / "checklist-baseline.json")
        shutil.copy2(inst_path.parent.parent / "SKILL.md", proof / "SKILL.md")
        shutil.copytree(inst_path.parent / "fixtures" / "dispatch-prompts",
                        proof / "fixtures" / "dispatch-prompts")

        def f_m16(mod):
            old_v, old_f = mod.VERIFIERS_DIR, mod.FIXTURES_DIR
            mod.VERIFIERS_DIR = proof / "verifiers"
            mod.FIXTURES_DIR = proof / "fixtures" / "dispatch-prompts"
            try:
                rc, out, err = run_main(mod, ["--box-proof"])
            finally:
                mod.VERIFIERS_DIR, mod.FIXTURES_DIR = old_v, old_f
            return rc, out.strip(), err.strip().splitlines()[:1]

        case("w16-parser-map-default-fixtures", "default --box-proof map path", f_m16)

        print("witness totals: DIFFERS %d, SAME %d, SKIPPED/ERROR %d"
              % (differs, same, skipped))
        return 0
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
