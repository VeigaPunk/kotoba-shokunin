#!/usr/bin/env python3
"""MutTesterBattery95 r95-w1: mutants of check_mutation_battery.py's --rev manifest/pin
path beyond the frozen set (n1/n5/n11/n10) plus the round-94 survivor N4 re-run.

Method = the frozen counter's own: literal substitution into the instrument text, executed
source-blind through the counter's RUNNER (imported read-only from selftest-kills.py): the
mutated text is compiled under the instrument's path and executed as __main__ with
argv [path, --self-test] while the instrument file on disk holds honest bytes.
Classification is the counter's rule 1: REPORTED-FAILURE -> KILLED, CLEAN -> SURVIVED,
anything else RUN-ERROR. The honest run must be CLEAN or every reading is inconclusive.

N4 (pin check moved after the probe loop) is a move, built as two literal edits: the 4-line
pin-check block is deleted and reinserted immediately before the results tally.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

COUNTER = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-95/selftest-kills.py")
_spec = importlib.util.spec_from_file_location("selftest_kills_v3", COUNTER)
CTR = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CTR)

INSTRUMENT = CTR.INSTRUMENT

PIN = 'return n == want, "observed'
TSC = "if {row.target for row in rows} != set(PROBES):"
MAN = 'committed = git_show(lane, rev, MANIFEST).decode("utf-8")'
CALL = "ok_pin, pin_detail = kill_set_check(committed, pinned)"
DETAIL = 'return n == want, "observed %d kill rows, pinned %d" % (n, want)'
MALF = 'return False, "manifest malformed: %s" % exc'
WANT = "want = KILL_SET_PINNED if pinned is None else pinned"
REW = 'raise CouldNotEvaluate("manifest must name exactly the targets %s"'

MUTANTS = [
    ("m01-pin-plus-three", PIN, 1,
     'return n == want + 3, "observed',
     "pin accepts exactly three kill rows above the pin"),
    ("m02-pin-le-plus-two", PIN, 1,
     'return n <= want + 2, "observed',
     "pin accepts up to two kill rows above the pin"),
    ("m03-manifest-at-parent", MAN, 1,
     'committed = git_show(lane, rev + "^", MANIFEST).decode("utf-8")',
     "--rev kill-set check reads the manifest at rev^ (parent), not rev"),
    ("m04-target-refusal-reworded", REW, 1,
     'raise CouldNotEvaluate("manifest names unexpected targets %s"',
     "target-set refusal message reworded (no label, like the honest text)"),
    ("m05-target-check-skipped", TSC, 1,
     "if False:",
     "target-set membership check skipped entirely"),
    ("m06-worktree-when-dirty", CALL, 1,
     'ok_pin, pin_detail = kill_set_check((lambda wt: wt if wt != committed else committed)((lane / MANIFEST).read_text(encoding="utf-8")), pinned)',
     "kill_set_check given the working-tree manifest text whenever it differs from committed (identical on clean worlds)"),
    ("m07-pin-arg-ignored", CALL, 1,
     "ok_pin, pin_detail = kill_set_check(committed)",
     "rev path ignores the caller's pinned argument, always pins the default"),
    ("m08-target-check-subset", TSC, 1,
     "if {row.target for row in rows} < set(PROBES):",
     "target-set check refuses only proper subsets (extra targets accepted)"),
    ("m09-pin-detail-drops-pinned", DETAIL, 1,
     'return n == want, "observed %d kill rows" % (n,)',
     "pin refusal detail no longer reports the pinned number"),
    ("m10-malformed-ok", MALF, 1,
     'return True, "manifest malformed: %s" % exc',
     "a malformed manifest passes kill_set_check"),
    ("m11-pin-swap", WANT, 1,
     "want = pinned if pinned is None else KILL_SET_PINNED",
     "default and caller's pin swapped (explicit pins get the default)"),
]


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def mutant_n4(original: str) -> str:
    """Move the pin check after the probe loop (round-94 survivor N4)."""
    lines = original.splitlines(keepends=True)
    idx = [i for i, ln in enumerate(lines)
           if ln == "    ok_pin, pin_detail = kill_set_check(committed, pinned)\n"]
    if len(idx) != 1:
        raise CTR.NotEvaluated("n4: pin-call line matches %d time(s)" % len(idx))
    i = idx[0]
    block = lines[i:i + 4]
    if not (len(block) == 4
            and block[1].strip() == "if not ok_pin:"
            and block[2].strip() == 'raise CouldNotEvaluate("arm kill-set-size: manifest at %s has %s"'
            and block[3].strip() == "% (rev[:12], pin_detail))"):
        raise CTR.NotEvaluated("n4: pin-check block has an unexpected shape: %r" % (block,))
    rest = [ln for j, ln in enumerate(lines) if not (i <= j < i + 4)]
    anchor = '    kills = [r for r in results if r["cls"] == "kill"]\n'
    hits = [j for j, ln in enumerate(rest) if ln == anchor]
    if len(hits) != 1:
        raise CTR.NotEvaluated("n4: kills-tally line matches %d time(s)" % len(hits))
    return "".join(rest[:hits[0]] + block + rest[hits[0]:])


def verdict_of(cls: str) -> str:
    return {"REPORTED-FAILURE": "KILLED", "CLEAN": "SURVIVED"}.get(cls, "RUN-ERROR")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--rev", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    got = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "-q", a.rev + "^{commit}"],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if got.returncode != 0:
        print("PROBE-NOT-EVALUATED: %s is not a commit of %s" % (a.rev, a.repo))
        return 2
    rev = got.stdout.decode().strip()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    root = out / "probe"
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(parents=True)
    env = dict(os.environ, TMPDIR=str(root / "tmp"), PYTHONDONTWRITEBYTECODE="1")
    (root / "tmp").mkdir()
    clone = root / "world" / "kotoba-shokunin"
    clone.parent.mkdir()
    for cmd in (["git", "clone", "-q", "--shared", str(repo), str(clone)],
                ["git", "-C", str(clone), "checkout", "-q", rev]):
        if subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
            print("PROBE-NOT-EVALUATED: clone or checkout failed")
            return 2
    path = clone / INSTRUMENT
    if not path.is_file():
        print("PROBE-NOT-EVALUATED: instrument %s absent" % INSTRUMENT)
        return 2
    original = path.read_text(encoding="utf-8")
    src = root / "src.py"
    results: list[dict] = []

    def run_text(text: str, label: str, on_disk: str):
        try:
            compile(text, str(path), "exec", dont_inherit=True)
        except SyntaxError as exc:
            raise CTR.NotEvaluated("%s does not compile: %s" % (label, exc))
        t0 = time.time()
        path.write_text(on_disk, encoding="utf-8")
        try:
            rc, o = CTR.run_selftest(clone, env, text, src)
        finally:
            path.write_text(original, encoding="utf-8")
        dt = time.time() - t0
        safe = label.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
        (out / ("run-%s.txt" % safe)).write_text(o, encoding="utf-8")
        return rc, o, CTR.classify(rc, o), dt

    rc_h, o_h, cls_h, dt_h = run_text(original, "honest", original)
    results.append({"name": "honest", "rc": rc_h, "class": cls_h, "secs": round(dt_h, 1),
                    "tail": CTR.last_line(o_h)})
    if cls_h != "CLEAN":
        (out / "results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        print("honest run is %s (rc %d) — inconclusive, stopping" % (cls_h, rc_h))
        return 2
    print("honest CLEAN rc %d (%.1fs)" % (rc_h, dt_h))

    for name, anchor, count, repl, why in MUTANTS:
        rec: dict = {"name": name, "why": why}
        found = original.count(anchor)
        if found != count:
            rec.update({"verdict": "NOT-EVALUATED",
                        "detail": "anchor matches %d time(s), expected %d" % (found, count)})
            results.append(rec)
            print("%-30s NOT-EVALUATED (%s)" % (name, rec["detail"]))
            continue
        try:
            rc, o, cls, dt = run_text(original.replace(anchor, repl), name, original)
        except CTR.NotEvaluated as exc:
            rec.update({"verdict": "NOT-EVALUATED", "detail": str(exc)})
            results.append(rec)
            print("%-30s NOT-EVALUATED (%s)" % (name, exc))
            continue
        v = verdict_of(cls)
        rec.update({"rc": rc, "class": cls, "verdict": v, "secs": round(dt, 1),
                    "fails": sum(1 for ln in o.splitlines() if ln.startswith("FAIL ")),
                    "tail": CTR.last_line(o)})
        results.append(rec)
        print("%-30s rc %d %-9s %s | %s" % (name, rc, v, rec["tail"][:90], why[:60]))

    try:
        n4text = mutant_n4(original)
        rc, o, cls, dt = run_text(n4text, "n4-pin-after-loop", original)
        v = verdict_of(cls)
        d = list(difflib.unified_diff(o_h.splitlines(), o.splitlines(), lineterm="", n=0))
        changed = [ln for ln in d if ln[:1] in "+-" and ln[:3] not in ("+++", "---")]
        (out / "n4-vs-honest.diff").write_text("\n".join(d[:400]) + "\n", encoding="utf-8")
        results.append({"name": "n4-pin-after-loop (r94 survivor re-run)",
                        "rc": rc, "class": cls, "verdict": v, "secs": round(dt, 1),
                        "fails": sum(1 for ln in o.splitlines() if ln.startswith("FAIL ")),
                        "tail": CTR.last_line(o),
                        "output_lines_changed_vs_honest": len(changed)})
        print("%-30s rc %d %-9s %s | %d output lines differ vs honest"
              % ("n4-pin-after-loop", rc, v, CTR.last_line(o)[:80], len(changed)))
    except CTR.NotEvaluated as exc:
        results.append({"name": "n4-pin-after-loop (r94 survivor re-run)",
                        "verdict": "NOT-EVALUATED", "detail": str(exc)})
        print("n4-pin-after-loop NOT-EVALUATED (%s)" % exc)

    back = path.read_text(encoding="utf-8")
    st = subprocess.run(["git", "-C", str(clone), "status", "--porcelain", "--", INSTRUMENT],
                        stdout=subprocess.PIPE).stdout.decode().strip()
    results.append({"name": "restoration", "instrument_bytes_match": back == original,
                    "sha256": sha(back), "git_status_clean": st == ""})
    (out / "results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    ne = sum(1 for r in results if r.get("verdict") == "NOT-EVALUATED")
    print("restoration: bytes match=%s sha %s git-clean=%s" % (back == original, sha(back)[:12], st == ""))
    print("PROBE-DONE mutants=%d not-evaluated=%d" % (len(MUTANTS) + 1, ne))
    return 2 if ne else 0


if __name__ == "__main__":
    sys.exit(main())
