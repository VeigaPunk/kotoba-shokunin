#!/usr/bin/env python3
"""C3 landing proof (seat V7).  Records and re-proves the round-37 C3
after-contract independently of the builder's diff:

  A identity    all 71 recorded fixture dirs / 145 files byte-identical
  B live        10 live runs: rc 0, stderr empty, stdout byte-identical
                across runs and (post) equal to the pre-landing stdout hash
  C selftest    0 failures; count reported (post: strictly above the pre count)
  D floors      check_assertion_floors.py checklist floor in all three
                carriers (docstring, EXPECTED_INSTRUMENTS, INSTRUMENTS)
                equals the observed self-test count
  E guardlive   the guard live run is 6/6 PASS, checklist observed==floor

Phases: --phase pre replays the sealed pre-state (expects count==1504,
floors==1504, live hash == recorded).  --phase post asserts the after-state.
Any FAIL exits 1.  Read-only: no writes outside --json.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_MANIFEST = HERE / "fixture-manifest-pre.sha256"
DEFAULT_DIRS = HERE / "fixture-dirs-pre.txt"
DEFAULT_PRE = HERE / "pre-state.txt"
FIXTURE_REL = "verifiers/fixtures/checklist"


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_kv(p: Path) -> dict:
    out = {}
    for line in p.read_text().splitlines():
        if "=" in line:
            k, _, v = line.partition("=")
            out[k.strip()] = v.strip()
    return out


def build_manifest(repo: Path) -> dict:
    root = repo / FIXTURE_REL
    m = {}
    for p in sorted(root.rglob("*")):
        if p.is_file():
            m[p.relative_to(repo).as_posix()] = sha256_file(p)
    return m


def run_bytes(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    return r.returncode, r.stdout, r.stderr


class Proof:
    def __init__(self, repo: Path, phase: str, pre: dict):
        self.repo = repo
        self.phase = phase
        self.pre = pre
        self.rows = []
        self.failed = 0

    def rec(self, name, ok, detail):
        self.rows.append({"check": name, "ok": bool(ok), "detail": detail})
        if not ok:
            self.failed += 1
        print("%s %-22s %s" % ("PASS" if ok else "FAIL", name, detail))

    # ---- A: fixture byte-identity -------------------------------------
    def check_identity(self):
        recorded = {}
        for line in DEFAULT_MANIFEST.read_text().splitlines():
            d, _, p = line.partition("  ")
            recorded[p] = d
        cur = build_manifest(self.repo)
        missing = sorted(set(recorded) - set(cur))
        changed = sorted(p for p in recorded if p in cur and cur[p] != recorded[p])
        added = sorted(set(cur) - set(recorded))
        ok = not missing and not changed
        self.rec("identity.files", ok,
                 "recorded=%d missing=%d changed=%d added=%d"
                 % (len(recorded), len(missing), len(changed), len(added)))
        if missing:
            print("      missing: " + " ".join(missing[:5]))
        if changed:
            print("      changed: " + " ".join(changed[:5]))
        if added:
            print("      added:   " + " ".join(added[:5]))
        dirs = [d for d in DEFAULT_DIRS.read_text().splitlines() if d]
        gone = [d for d in dirs if not (self.repo / d).is_dir()]
        self.rec("identity.dirs", not gone,
                 "recorded_dirs=%d missing_dirs=%d" % (len(dirs), len(gone)))
        if self.phase == "pre":
            self.rec("identity.pre_exact", not added,
                     "additions in pre phase (expected 0): %d" % len(added))

    # ---- B: live 10x byte-invariance ----------------------------------
    def check_live(self):
        outs = []
        rcs = []
        errs = []
        instr = self.pre.get("instrument_override") or \
            "verifiers/verify_skill_checklist.py"
        cmd = [sys.executable, instr]
        if self.pre.get("instrument_override"):
            cmd += ["--repo", str(self.repo)]
        for _ in range(10):
            rc, out, err = run_bytes(cmd, self.repo)
            rcs.append(rc)
            outs.append(out)
            errs.append(err)
        hashes = {sha256_bytes(o) for o in outs}
        passes = outs[0].decode().count("\nPASS ") + outs[0].decode().startswith("PASS ")
        ok = (set(rcs) == {0} and len(hashes) == 1 and all(e == b"" for e in errs)
              and passes == 10)
        self.rec("live.10x", ok,
                 "rcs=%s unique_stdout=%d stderr_empty=%s PASS_lines=%d sha=%s"
                 % (sorted(set(rcs)), len(hashes),
                    all(e == b"" for e in errs), passes,
                    sorted(hashes)[0][:16]))
        baseline = self.pre.get("live_stdout_sha256")
        same = sorted(hashes)[0] == baseline
        if self.phase == "pre":
            self.rec("live.matches_recorded", same,
                     "recorded=%s observed=%s" % (baseline[:16],
                                                  sorted(hashes)[0][:16]))
        else:
            self.rec("live.byte_invariant_vs_pre", same,
                     "pre=%s post=%s" % (baseline[:16], sorted(hashes)[0][:16]))

    # ---- C: self-test count -------------------------------------------
    def check_selftest(self):
        rc, out, err = run_bytes([sys.executable,
                                  "verifiers/verify_skill_checklist.py",
                                  "--self-test"], self.repo)
        text = out.decode() + err.decode()
        m = re.search(r"(\d+) failure\(s\) over (\d+) assertions", text)
        if not m:
            self.rec("selftest", False, "unparseable rc=%d tail=%r" %
                     (rc, text.strip().splitlines()[-1:]))
            return
        fails, count = int(m.group(1)), int(m.group(2))
        pre_count = int(self.pre.get("selftest_assertions", "0"))
        if self.phase == "pre":
            self.rec("selftest", fails == 0 and count == pre_count and rc == 0,
                     "rc=%d failures=%d assertions=%d (recorded %d)"
                     % (rc, fails, count, pre_count))
        else:
            self.rec("selftest.failures", fails == 0 and rc == 0,
                     "rc=%d failures=%d assertions=%d" % (rc, fails, count))
            self.rec("selftest.count_bumped", count > pre_count,
                     "pre=%d post=%d delta=%d" % (pre_count, count,
                                                  count - pre_count))
        self.observed_count = count

    # ---- D: floors in-step --------------------------------------------
    def check_floors(self):
        src = (self.repo / "verifiers/check_assertion_floors.py").read_text()
        doc = src.split("'''")[1] if "'''" in src else src[:2000]
        m = re.search(r"checklist (\d+)", doc)
        exp = re.findall(r'"checklist":\s*(\d+)', src)
        inst = re.findall(r'"checklist":\s*\("[^"]+",\s*(\d+)', src)
        count = getattr(self, "observed_count", None)
        if count is None:
            rc, out, err = run_bytes([sys.executable,
                                      "verifiers/verify_skill_checklist.py",
                                      "--self-test"], self.repo)
            mm = re.search(r"(\d+) failure\(s\) over (\d+) assertions",
                           (out + err).decode())
            count = int(mm.group(2)) if mm else -1
        carriers = {"docstring": int(m.group(1)) if m else None,
                    "EXPECTED_INSTRUMENTS": int(exp[0]) if exp else None,
                    "INSTRUMENTS": int(inst[0]) if inst else None}
        reg = self.repo / "verifiers/floors-registry.json"
        if reg.is_file() or self.phase == "post":
            try:
                carriers["floors-registry.json"] = json.loads(
                    reg.read_text())["instruments"]["checklist"]["floor"]
            except Exception as exc:
                carriers["floors-registry.json"] = "unreadable (%s)" % exc
        ok = all(v == count for v in carriers.values())
        self.rec("floors.in_step", ok,
                 "observed=%d carriers=%s" % (count, carriers))
        if self.phase == "pre":
            self.rec("floors.pre", count == int(self.pre.get(
                "selftest_assertions", "0")),
                "observed=%d pre=%s" % (count, self.pre.get("selftest_assertions")))

    # ---- E: guard live run --------------------------------------------
    def check_guard(self):
        rc, out, err = run_bytes([sys.executable,
                                  "verifiers/check_assertion_floors.py"],
                                 self.repo)
        text = (out + err).decode()
        rows = re.findall(r"(\w+) observed=(\d+) floor=(\d+)", text)
        passes = text.count("\nPASS ") + text.startswith("PASS ")
        ck = dict((n, (int(o), int(f))) for n, o, f in rows).get("checklist")
        ok = rc == 0 and passes == 6 and ck is not None and ck[0] == ck[1]
        self.rec("guard.live", ok,
                 "rc=%d PASS_rows=%d checklist=%s" % (rc, passes, ck))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--phase", choices=["pre", "post"], required=True)
    ap.add_argument("--pre-state", type=Path, default=DEFAULT_PRE)
    ap.add_argument("--json", type=Path)
    ap.add_argument("--only", action="append", default=[])
    args = ap.parse_args()
    repo = args.repo.resolve()
    pre = load_kv(args.pre_state)
    p = Proof(repo, args.phase, pre)
    checks = {"identity": p.check_identity, "live": p.check_live,
              "selftest": p.check_selftest, "floors": p.check_floors,
              "guard": p.check_guard}
    if args.only:
        for name in args.only:
            checks[name]()
    else:
        for name, fn in checks.items():
            fn()
    rc = 0
    try:
        rc = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short",
                             "HEAD"], stdout=subprocess.PIPE).stdout.decode().strip()
    except Exception:
        pass
    summary = {"phase": args.phase, "repo": str(repo), "head": rc,
               "instrument_sha256": sha256_file(
                   repo / "verifiers/verify_skill_checklist.py"),
               "rows": p.rows, "failed": p.failed,
               "instrument_dirty_vs_pre": sha256_file(
                   repo / "verifiers/verify_skill_checklist.py")
               != pre.get("instrument_verify_skill_checklist_sha256")}
    print("--- head=%s instrument_sha=%s dirty_vs_pre=%s failed=%d"
          % (summary["head"], summary["instrument_sha256"][:12],
             summary["instrument_dirty_vs_pre"], p.failed))
    if args.json:
        args.json.write_text(json.dumps(summary, indent=1) + "\n")
    return 1 if p.failed else 0


if __name__ == "__main__":
    sys.exit(main())