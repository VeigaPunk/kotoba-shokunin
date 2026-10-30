#!/usr/bin/env python3
"""Kb82E06Controls_controls.py -- round-82 C1 predata shortcut controls.

Drives the UNCHANGED counter verifiers/check_substrate_repin_v2.py (frozen at
base 47dbe8781657de563ff867caca6244d28e3db504) against sandbox shortcut worlds
built as labelled commits in the seat's scratch clone:

  W0 base                -- unchanged base tree (do-nothing control)
  W1 path-only           -- omp default path -> live ELF, pins/baselines stale
  W2 pin-only            -- pins -> live values, default path still omp.real
  W3 fake-omp-elf        -- tree-local crafted ELF pinned as omp substrate
  W4 stdout-stub gates   -- pins/surfaces instruments replaced by JSON stubs
  W5a unkept class       -- W4 + one non-frozen opencode class dropped silently
  W5b ledger-extra       -- W4 + a live class added to the removal ledger
  W5c ledger-missing     -- W4 + one frozen class dropped from the ledger
  W6 stray-opencode-pin  -- W4 but the opencode pin names bytes that are not live
  W7 path+pin no-rederiv -- live path + live pins, REAL gates, stale omp classes

The runner itself never mutates the lane repo, the host, or anything outside
--work and the seat's scratch clone.  Every world commit is labelled
"sandbox:" and carries a scratch identity.  Stdlib only.

Usage:
  python3 -B Kb82E06Controls_controls.py --work <dir> --out <build-dir> \
      --counter <path> --repo <scratch-clone>
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import shlex
import shutil
import stat as statmod
import subprocess
import sys
import time
from pathlib import Path

BASE_REV = "47dbe8781657de563ff867caca6244d28e3db504"
SEAT = "Kb82E06Controls"
TARGET_LINE = ("host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; "
               "removal ledger 3 of 3 verified")
LIVE_OMP = Path("/home/vgpnk/.local/bin/omp")
LIVE_OPENCODE = Path("/home/vgpnk/.opencode/bin/opencode")
FROZEN_REMOVALS = {
    "opencode:instructions/CONTEXT.md": [r"CONTEXT\.md"],
    "opencode:instructions/CLAUDE.md": [
        r"disableClaudeCodePrompt",
        r'\["AGENTS\.md".{0,400}?"CONTEXT\.md"[^\]]{0,200}\]'],
    "opencode:claude-home/CLAUDE.md": [
        r'\.join\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.home\s*,\s*"\.([A-Za-z0-9_-]+)"\s*,'
        r'\s*"([A-Za-z0-9_.-]+\.md)"'],
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def stamp_ns(ns: int) -> str:
    sec, frac = divmod(ns, 10 ** 9)
    dt = datetime.datetime.fromtimestamp(sec, datetime.timezone.utc)
    local = dt.astimezone(datetime.timezone(datetime.timedelta(hours=-3)))
    return local.strftime("%Y-%m-%dT%H:%M:%S") + ".%09d-03:00" % frac


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None,
                          capture_output=True, text=True)


def git_clone(repo: Path, *args: str) -> str:
    proc = run(["git", "-C", str(repo), *args])
    if proc.returncode != 0:
        raise SystemExit("git %s failed: %s" % (shlex.join(args), proc.stderr))
    return proc.stdout.strip()


class Seat:
    def __init__(self, work: Path, out: Path, counter: Path, repo: Path) -> None:
        self.work = work
        self.out = out
        self.counter = counter
        self.repo = repo
        self.branch = "sandbox/%s-controls" % SEAT
        self.worlds_dir = work / "worlds"
        self.results: list[dict] = []
        self.host: dict = {}

    def log(self, msg: str) -> None:
        print(msg, flush=True)

    # -- host measurement (non-mutating, mirrors the independent guard) --------
    def measure_host(self) -> None:
        t0 = time.monotonic()
        omp_st = LIVE_OMP.stat()
        oc_st = LIVE_OPENCODE.stat()
        oc_dump = subprocess.run(
            ["strings", "-n", "4", str(LIVE_OPENCODE)],
            capture_output=True, timeout=600)
        if oc_dump.returncode != 0:
            raise SystemExit("strings on live opencode exited %d"
                             % oc_dump.returncode)
        oc_text = oc_dump.stdout.decode("utf-8", "replace")
        anchors = {}
        for cid, pats in FROZEN_REMOVALS.items():
            anchors[cid] = {p: bool(re.search(p, oc_text)) for p in pats}
        self.host = {
            "measured_by": "%s controls runner (independent predata guard)" % SEAT,
            "omp": {"path": str(LIVE_OMP),
                    "sha256": sha256_file(LIVE_OMP),
                    "bytes": omp_st.st_size,
                    "mtime_ns": omp_st.st_mtime_ns,
                    "mtime_iso_minus03": stamp_ns(omp_st.st_mtime_ns)},
            "opencode": {"path": str(LIVE_OPENCODE),
                         "sha256": sha256_file(LIVE_OPENCODE),
                         "bytes": oc_st.st_size,
                         "mtime_ns": oc_st.st_mtime_ns},
            "opencode_strings_exit": oc_dump.returncode,
            "opencode_dump_lines": len(oc_text.splitlines()),
            "frozen_removal_anchor_hits": anchors,
            "frozen_removal_anchors_all_absent":
                not any(any(v.values()) for v in anchors.values()),
            "elapsed_s": round(time.monotonic() - t0, 3),
        }
        (self.out / ("%s-host-measure.json" % SEAT)).write_text(
            json.dumps(self.host, indent=1, sort_keys=True) + "\n",
            encoding="utf-8")
        self.log("host measured: omp %s.. opencode %s.. anchors_absent=%s"
                 % (self.host["omp"]["sha256"][:12],
                    self.host["opencode"]["sha256"][:12],
                    self.host["frozen_removal_anchors_all_absent"]))

    # -- sandbox world construction -------------------------------------------
    def checkout_branch(self) -> None:
        top = Path(git_clone(self.repo, "rev-parse", "--show-toplevel")).resolve()
        assert top == self.repo.resolve(), "toplevel %s != %s" % (top, self.repo)
        head = git_clone(self.repo, "rev-parse", "HEAD")
        assert head == BASE_REV, "clone HEAD %s != base %s" % (head, BASE_REV)
        git_clone(self.repo, "checkout", "-q", "-b", self.branch)
        self.log("sandbox branch %s at %s" % (self.branch, BASE_REV))

    def world(self, name: str, mutate, parents: list[str] | None = None) -> str:
        """Commit one sandbox world on top of BASE_REV (or parent world)."""
        top = Path(git_clone(self.repo, "rev-parse", "--show-toplevel")).resolve()
        assert top == self.repo.resolve(), "toplevel drifted: %s" % top
        git_clone(self.repo, "checkout", "-q", "-B", self.branch, BASE_REV)
        git_clone(self.repo, "clean", "-qfd")
        mutate()
        git_clone(self.repo, "add", "-A")
        subject = "sandbox: %s %s" % (SEAT, name)
        git_clone(self.repo, "-c", "user.name=%s sandbox" % SEAT,
                  "-c", "user.email=%s-sandbox@example.invalid" % SEAT.lower(),
                  "-c", "core.hooksPath=/dev/null",
                  "commit", "-q", "-m", subject)
        rev = git_clone(self.repo, "rev-parse", "HEAD")
        self.log("world %-22s %s  %s" % (name, rev[:12], subject))
        return rev

    # -- world mutators --------------------------------------------------------
    def read(self, rel: str) -> str:
        return (self.repo / rel).read_text(encoding="utf-8")

    def write(self, rel: str, text: str) -> None:
        (self.repo / rel).write_text(text, encoding="utf-8")

    def retarget_omp(self, expr: str) -> None:
        pins = "verifiers/check_substrate_pins.py"
        surf = "verifiers/verify_surfaces.py"
        self.write(pins, self.read(pins).replace(
            '"omp": "/home/vgpnk/.local/bin/omp.real",', '"omp": %s,' % expr))
        self.write(surf, self.read(surf).replace(
            '"omp": "/home/vgpnk/.local/bin/omp.real",', '"omp": %s,' % expr))

    def repin_omp(self, sha: str, stamp: str) -> None:
        base = json.loads(self.read("verifiers/baseline.json"))
        ma = base["measured_against"]
        ma["omp_binary_sha256"] = sha
        ma["omp_binary_mtime"] = stamp
        self.write("verifiers/baseline.json", json.dumps(base, indent=1) + "\n")

    def stub_gates(self, oc_expect: str, note: str) -> None:
        pins_stub = STUB_PINS % {"oc": oc_expect, "note": note}
        surf_stub = STUB_SURFACES % {"note": note}
        self.write("verifiers/check_substrate_pins.py", pins_stub)
        self.write("verifiers/verify_surfaces.py", surf_stub)

    def mutate_fake_omp(self) -> None:
        fake = self.repo / "verifiers" / "sandbox-fake-omp.elf"
        payload = (b"\x7fELF sandbox fake omp ELF -- Kb82E06Controls control\n"
                   b"registration callees FAKE/FAKE/FAKE\n"
                   b"this substrate never ran on the host\n")
        fake.write_bytes(payload)
        ns = 1_793_326_786_168_359_786
        os.utime(fake, ns=(ns, ns))
        expr = 'str(Path(__file__).resolve().parent / "sandbox-fake-omp.elf")'
        self.retarget_omp(expr)
        self.repin_omp(hashlib.sha256(payload).hexdigest(), stamp_ns(ns))

    def mutate_unkept(self) -> None:
        path = self.repo / "verifiers" / "surfaces-baseline.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["classes"] = [r for r in data["classes"]
                           if r.get("class_id") != "opencode:config/instructions"]
        path.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")

    def mutate_ledger_extra(self) -> None:
        path = self.repo / "verifiers" / "census-removals.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["removed"].append({
            "class_id": "opencode:instructions/AGENTS.md",
            "literal": "AGENTS.md",
            "reason": "sandbox: ledgered although the literal is live"})
        path.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")

    def mutate_ledger_missing(self) -> None:
        path = self.repo / "verifiers" / "census-removals.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["removed"] = [r for r in data["removed"]
                           if r.get("class_id") != "opencode:instructions/CONTEXT.md"]
        path.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")

    # -- counter driving --------------------------------------------------------
    def run_counter(self, name: str, rev: str) -> dict:
        t0 = time.monotonic()
        proc = subprocess.run(
            [sys.executable, "-B", str(self.counter),
             "--repo", str(self.repo), "--rev", rev],
            capture_output=True, text=True,
            env={**os.environ, "TMPDIR": str(self.work / "tmp")})
        elapsed = round(time.monotonic() - t0, 3)
        blob_sha = {}
        for gate in ("verifiers/check_substrate_pins.py",
                     "verifiers/verify_surfaces.py",
                     "verifiers/check_substrate_repin_v2.py"):
            show = run(["git", "-C", str(self.repo), "show", "%s:%s" % (rev, gate)])
            blob_sha[gate] = hashlib.sha256(show.stdout.encode()).hexdigest() \
                if show.returncode == 0 else None
        out = proc.stdout
        reached = proc.returncode == 0 and TARGET_LINE in out
        rec = {"world": name, "rev": rev, "counter_exit": proc.returncode,
               "target_reached": reached, "frozen_line_present": TARGET_LINE in out,
               "stdout": out, "stderr": proc.stderr, "elapsed_s": elapsed,
               "gate_blob_sha256": blob_sha}
        self.results.append(rec)
        receipt = self.out / ("%s-world-%s.txt" % (SEAT, name))
        receipt.write_text(
            "# world %s rev %s\n# command: %s -B %s --repo %s --rev %s\n"
            "# counter exit: %d  target_reached: %s  elapsed: %ss\n"
            "# gate blobs: %s\n--- stdout ---\n%s--- stderr ---\n%s"
            % (name, rev, sys.executable, self.counter, self.repo, rev,
               proc.returncode, reached, elapsed,
               json.dumps(blob_sha, indent=1), out, proc.stderr),
            encoding="utf-8")
        first = (out.strip().splitlines() or ["<no output>"])[0]
        self.log("counter on %-22s exit=%d reached=%s :: %s"
                 % (name, proc.returncode, reached, first[:120]))
        return rec

    # -- top level --------------------------------------------------------------
    def run(self) -> int:
        (self.work / "tmp").mkdir(parents=True, exist_ok=True)
        os.environ["TMPDIR"] = str(self.work / "tmp")
        self.out.mkdir(parents=True, exist_ok=True)
        self.measure_host()
        self.checkout_branch()

        oc_sha = self.host["opencode"]["sha256"]
        omp_sha = self.host["omp"]["sha256"]
        omp_stamp = self.host["omp"]["mtime_iso_minus03"]
        wrong_sha = hashlib.sha256(b"sandbox bytes that are not the live "
                                   b"opencode").hexdigest()

        worlds: list[tuple[str, object]] = [
            ("W0-base", None),
            ("W1-path-only",
             lambda: self.retarget_omp('"/home/vgpnk/.local/bin/omp"')),
            ("W2-pin-only", lambda: self.repin_omp(omp_sha, omp_stamp)),
            ("W3-fake-omp-elf", self.mutate_fake_omp),
            ("W4-stdout-stub-gates", lambda: self.stub_gates(oc_sha, "green stub")),
            ("W5a-unkept-class", lambda: (self.stub_gates(oc_sha, "green stub"),
                                          self.mutate_unkept())),
            ("W5b-ledger-extra", lambda: (self.stub_gates(oc_sha, "green stub"),
                                          self.mutate_ledger_extra())),
            ("W5c-ledger-missing", lambda: (self.stub_gates(oc_sha, "green stub"),
                                            self.mutate_ledger_missing())),
            ("W6-stray-opencode-pin", lambda: self.stub_gates(wrong_sha, "stray")),
            ("W7-path-plus-pin-no-rederivation",
             lambda: (self.retarget_omp('"/home/vgpnk/.local/bin/omp"'),
                      self.repin_omp(omp_sha, omp_stamp))),
        ]
        for name, mutate in worlds:
            rev = BASE_REV if mutate is None else self.world(name, mutate)
            self.run_counter(name, rev)

        summary = {
            "seat": SEAT,
            "base_rev": BASE_REV,
            "counter": str(self.counter),
            "counter_sha256": sha256_file(self.counter),
            "counter_unchanged_at_base":
                git_clone(self.repo, "rev-parse", "%s:verifiers/check_substrate_repin_v2.py"
                          % BASE_REV) == git_clone(self.repo, "hash-object", str(self.counter)),
            "repo": str(self.repo),
            "target_line": TARGET_LINE,
            "worlds": [{k: r[k] for k in
                        ("world", "rev", "counter_exit", "target_reached",
                         "frozen_line_present", "elapsed_s", "gate_blob_sha256")}
                       for r in self.results],
            "results": self.results,
        }
        (self.out / ("%s-summary.json" % SEAT)).write_text(
            json.dumps(summary, indent=1) + "\n", encoding="utf-8")
        reached = [r["world"] for r in self.results if r["target_reached"]]
        self.log("TARGET-REACHED worlds: %s" % (reached or "none"))
        for r in self.results:
            if r["target_reached"]:
                self.log("WEAKNESS %s: unchanged counter accepts this world; "
                         "external guards must reject it" % r["world"])
        return 0


STUB_PINS = '''#!/usr/bin/env python3
"""SANDBOX STDOUT STUB -- not a measurement instrument (Kb82E06Controls W4+).

Prints a canned 3-row PASS pins report.  The opencode row names %(note)s
sha256 so the frozen counter's substrate-identity comparison is satisfied by
construction.  Stdlib only; ignores argv.
"""
import hashlib
import json

OPENCODE_EXPECT = "%(oc)s"

rows = [
    {"pin": "omp_binary_sha256", "kind": "sha256", "substrate": "omp",
     "verdict": "PASS", "expect": hashlib.sha256(b"stub omp").hexdigest(),
     "observed": hashlib.sha256(b"stub omp").hexdigest()},
    {"pin": "omp_binary_mtime", "kind": "mtime", "substrate": "omp",
     "verdict": "PASS", "expect": "2026-10-29T23:19:46.168359786-03:00",
     "observed": "2026-10-29T23:19:46.168359786-03:00"},
    {"pin": "opencode_binary_sha256", "kind": "sha256", "substrate": "opencode",
     "verdict": "PASS", "expect": OPENCODE_EXPECT, "observed": OPENCODE_EXPECT},
]
p = sum(1 for r in rows if r["verdict"] == "PASS")
print(json.dumps({"checks": rows, "pass": p, "fail": len(rows) - p,
                  "exit_code": 0 if p == len(rows) else 1}))
'''

STUB_SURFACES = '''#!/usr/bin/env python3
"""SANDBOX STDOUT STUB -- not a measurement instrument (Kb82E06Controls W4+).

Prints 7 canned PASS surface checks (%(note)s).  Stdlib only; ignores argv.
"""
import json

IDS = ("surfaces.literal_present", "surfaces.no_uncovered_class",
       "surfaces.opencode_extract", "surfaces.table_parity",
       "surfaces.literal_parity", "surfaces.kind_parity",
       "surfaces.excluded_reason")
checks = [{"id": cid, "status": "PASS"} for cid in IDS]
p = sum(1 for c in checks if c["status"] == "PASS")
print(json.dumps({"checks": checks, "pass": p,
                  "fail": len(checks) - p,
                  "exit_code": 0 if p == len(checks) else 1}))
'''


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    here = Path(__file__).resolve().parent
    ap.add_argument("--work", required=True, help="scratch work directory")
    ap.add_argument("--out", default=str(here),
                    help="receipt output directory (default: beside this script)")
    ap.add_argument("--counter", required=True,
                    help="path to the UNCHANGED check_substrate_repin_v2.py")
    ap.add_argument("--repo", required=True, help="seat scratch clone")
    args = ap.parse_args()
    work = Path(args.work).resolve()
    out = Path(args.out).resolve()
    counter = Path(args.counter).resolve()
    repo = Path(args.repo).resolve()
    for p in (work, out, counter, repo):
        if not p.exists():
            raise SystemExit("missing path: %s" % p)
    seat = Seat(work, out, counter, repo)
    return seat.run()


if __name__ == "__main__":
    sys.exit(main())
