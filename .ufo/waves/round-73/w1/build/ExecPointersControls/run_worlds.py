#!/usr/bin/env python3
"""Run the pointer-gate draft against every control world in this directory.

Usage: python3 -B run_worlds.py [--gate PATH] [--keep-sandboxes]

Contract read from each <world>/world.json:
  rev            revision the tokens are resolved at
  round          the round a bare ``receipts/`` token resolves against
  sandbox        null, or {rev, untracked:[paths]} -> a --shared clone of the lane
                 with those files written but not committed
  reports[]      file, expect_exit, expect_tally, expect_names, optional
                 round/rev overrides and also_at_control_rev

The gate CLI is `check_report_pointers.py --report F --repo R --rev V [--round N]`.
If the draft rejects --round the runner retries without it and says so.

Every run is stored verbatim under readings/, plus a summary.tsv. No lane file is
written; sandboxes live under /tmp and are removed unless --keep-sandboxes.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
DEFAULT_GATE = os.path.join(HERE, "..", "ExecPointersGate", "check_report_pointers.py")


def build_sandbox(spec, tag):
    base = tempfile.mkdtemp(prefix="k73w1-ExecPointersControls.%s." % tag)
    lane = os.path.join(base, "lane")
    run = ["git", "clone", "--shared", "-q", "--no-checkout", LANE, lane]
    r = subprocess.run(run, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("clone failed: %s\n%s" % (" ".join(run), r.stderr))
    r = subprocess.run(["git", "-C", lane, "checkout", "-q", spec["rev"]], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("checkout failed: %s" % r.stderr)
    top = subprocess.run(["git", "-C", lane, "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True).stdout.strip()
    if os.path.realpath(top) != os.path.realpath(lane):
        raise SystemExit("sandbox toplevel mismatch: %r != %r" % (top, lane))
    for rel in spec.get("untracked", []):
        p = os.path.join(lane, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fh:
            fh.write("untracked fixture: exists on disk, absent from %s\n" % spec["rev"])
    return base, lane


def run_gate(gate, report, repo, rev, rnd, timeout=120):
    cmd = [sys.executable, "-B", gate, "--report", report, "--repo", repo, "--rev", rev,
           "--round", str(rnd)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    note = ""
    if r.returncode == 2 and "round" in (r.stderr or "") and "unrecognized" in (r.stderr or "").lower():
        cmd = cmd[:-2]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        note = "retried without --round (draft CLI has no --round)"
    return cmd, r, note


def main():
    args = sys.argv[1:]
    keep = "--keep-sandboxes" in args
    gate = DEFAULT_GATE
    if "--gate" in args:
        gate = args[args.index("--gate") + 1]
    if not os.path.isfile(gate):
        print("GATE ABSENT: %s" % gate)
        return 2
    import hashlib
    import time
    gate_bytes = open(gate, "rb").read()
    gate_sha = hashlib.sha256(gate_bytes).hexdigest()
    gate_id = "sha256:%s bytes:%d mtime:%s" % (
        gate_sha, len(gate_bytes),
        time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(os.path.getmtime(gate))))
    print("# gate %s" % gate_id)
    readings = os.path.join(HERE, "readings")
    os.makedirs(readings, exist_ok=True)
    rows = []
    sandboxes = []
    worlds = sorted(d for d in os.listdir(HERE)
                    if os.path.isdir(os.path.join(HERE, d)) and d not in ("readings", "__pycache__"))
    for world in worlds:
        wdir = os.path.join(HERE, world)
        cfgp = os.path.join(wdir, "world.json")
        if not os.path.isfile(cfgp):
            continue
        cfg = json.load(open(cfgp))
        repo = LANE
        sb_note = "lane tree (committed objects only)"
        if cfg.get("sandbox"):
            base, repo = build_sandbox(cfg["sandbox"], world)
            sandboxes.append(base)
            sb_note = "sandbox %s at %s, untracked %s" % (repo, cfg["sandbox"]["rev"],
                                                          ",".join(cfg["sandbox"].get("untracked", [])))
        for rep in cfg["reports"]:
            path = os.path.join(wdir, rep["file"])
            rnd = rep.get("round", cfg["round"])
            tries = [("", rep.get("rev", cfg["rev"]), rep)]
            if rep.get("also_at_control_rev"):
                c = rep["also_at_control_rev"]
                tries.append(("control", cfg.get("control_rev", ""), c))
            for label, rev, exp in tries:
                cmd, r, note = run_gate(gate, path, repo, rev, rnd)
                out = (r.stdout or "").strip()
                err = (r.stderr or "").strip()
                match = "MATCH" if r.returncode == exp["expect_exit"] else "DIFF"
                tag = world if not label else "%s@%s" % (world, label)
                fn = os.path.join(readings, "%s__%s.txt" % (tag, rep["file"].replace(".md", "")))
                with open(fn, "w") as fh:
                    fh.write("# gate: %s\n# sandbox: %s\n# command: %s\n# exit: %d\n# expected exit: %d\n"
                             "# stdout:\n%s\n# stderr:\n%s\n# note: %s\n"
                             % (gate_id, sb_note, " ".join(cmd), r.returncode, exp["expect_exit"], out, err, note))
                missing = [n for n in exp.get("expect_names", []) if n not in out and n not in err]
                rows.append((tag, rep["file"], rev[:8], r.returncode, exp["expect_exit"], match,
                             out.splitlines()[0] if out else "", ",".join(missing)))
    hdr = "world\treport\trev\texit\texpect\tverdict\treading\tunnamed"
    print(hdr)
    for row in rows:
        print("\t".join(str(x) for x in row))
    with open(os.path.join(readings, "summary.tsv"), "w") as fh:
        fh.write("# gate: %s\n" % gate_id)
        fh.write(hdr + "\n")
        for row in rows:
            fh.write("\t".join(str(x) for x in row) + "\n")
    with open(os.path.join(readings, "GATE.txt"), "w") as fh:
        fh.write("%s\n%s\n" % (os.path.abspath(gate), gate_id))
    if not keep:
        for b in sandboxes:
            shutil.rmtree(b, ignore_errors=True)
    return 0 if all(r[5] == "MATCH" for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
