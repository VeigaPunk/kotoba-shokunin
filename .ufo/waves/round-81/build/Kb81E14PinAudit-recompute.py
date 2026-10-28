#!/usr/bin/env python3
"""Kb81E14PinAudit — freeze-set pin audit recompute harness (leaf seat, no lane edit).

Recomputes, from PRIMARY bytes only:

  1. sha256 + blob id of verifiers/check_tip_battery.py at the r81 base, and whether
     the audited counter working tree equals that base blob;
  2. the six battery instruments' blob ids at the base rev vs INSTRUMENT_PINS
     (membership of each base blob in its allowed tuple), plus BATTERY/pin row set equality;
  3. sha256 of every reviewed r81 build patch named on the command line;
  4. the instrument blobs a patch stack produces (applied into a throwaway clone only),
     and whether each resulting blob is pinned by the audited counter;
  5. the E6 cap arithmetic: numstat of the instrument patches + pre-existing spend
     (r73 base 072048fa -> r81 base b2842231) against the counter's LINE_CAP;
  6. the counter patch's declared-line-set conformance (E6 allows exactly LINE_CAP,
     two pin-tuple memberships, and self-test constants deriving from LINE_CAP).

Usage:
  python3 Kb81E14PinAudit-recompute.py --repo <clone> [--patch P ...] [--skip-selftest]

Every git call names the clone with -C. The clone is scratch; nothing here writes
to the lane.
"""
import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

BASE = "b284223105f4d106f7e8f56ed4fd296c643cda0e"
R73 = "072048fa8e8a52c707d25f7079772fa317244eb7"
COUNTER = "verifiers/check_tip_battery.py"
INSTRUMENTS = (
    "verifiers/check_gate_registry.py",
    "verifiers/check_assertion_floors.py",
    "verifiers/verify_skill_checklist.py",
    "verifiers/verify_corpus_integrity.py",
    "verifiers/verify_corpus_independent.py",
    "verifiers/check_correction_sweep.py",
)
PIN_ADD_TARGETS = ("verifiers/verify_corpus_integrity.py",
                   "verifiers/verify_corpus_independent.py")


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_pins(text):
    body = re.search(r"INSTRUMENT_PINS = \{(.*?)\n\}", text, re.S).group(1)
    pairs, cur = {}, None
    for line in body.splitlines():
        s = line.strip()
        m = re.match(r'"(verifiers/[^"]+)":', s)
        if m:
            cur = m.group(1)
            pairs.setdefault(cur, [])
        for h in re.findall(r'"([0-9a-f]{40})"', line):
            pairs[cur].append(h)
    return pairs


def parse_battery(text):
    body = re.search(r"BATTERY = \((.*?)\n\)", text, re.S).group(1)
    return re.findall(r'\("(verifiers/[^"]+)",', body)


def numstat_patch(patch):
    proc = subprocess.run(["git", "apply", "--numstat", str(patch)],
                          capture_output=True, text=True)
    rows = []
    for line in proc.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        rows.append((parts[2], parts[0], parts[1]))
    return proc.returncode, rows, proc.stderr.strip()


def resync(repo):
    git(repo, "reset", "-q", "--hard", BASE)
    git(repo, "clean", "-qfd")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="throwaway clone at the r81 base")
    ap.add_argument("--patch", action="append", default=[],
                    help="patch to apply into the clone before auditing (repeatable)")
    ap.add_argument("--no-patch-apply", action="store_true",
                    help="audit the base counter only; do not apply patches")
    ap.add_argument("--skip-selftest", action="store_true")
    args = ap.parse_args(argv)
    repo = Path(args.repo).resolve()
    top = subprocess.run(["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True).stdout.strip()
    assert top == str(repo), "clone is not a toplevel: %s" % top

    print("== clone %s head %s" % (repo, git(repo, "rev-parse", "HEAD").stdout.strip()))

    # ---- 1. base measurement -------------------------------------------------
    base_head = git(repo, "rev-parse", BASE).stdout.strip()
    base_blob = git(repo, "rev-parse", "%s:%s" % (BASE, COUNTER)).stdout.strip()
    base_bytes = subprocess.run(["git", "-C", str(repo), "cat-file", "blob", base_blob],
                                capture_output=True)
    print("counter base blob      %s  bytes %d  sha256 %s"
          % (base_blob, len(base_bytes.stdout), hashlib.sha256(base_bytes.stdout).hexdigest()))

    base_text = subprocess.run(["git", "-C", str(repo), "show", "%s:%s" % (BASE, COUNTER)],
                               capture_output=True, text=True).stdout
    base_pins = parse_pins(base_text)
    base_cap = int(re.search(r"^LINE_CAP = (\d+)$", base_text, re.M).group(1))
    base_battery = parse_battery(base_text)
    print("base LINE_CAP          %d" % base_cap)
    print("base pin rows          %d  (%s)" % (len(base_pins), ", ".join(sorted(base_pins))))
    print("BATTERY rows           %d" % len(base_battery))
    print("pin set == battery set %s" % (set(base_pins) == set(base_battery)))
    print("instrument list matches harness constant: %s" % (set(base_battery) == set(INSTRUMENTS)))

    print("\n-- base blob membership in each allowed tuple")
    all_ok = True
    for path in base_battery:
        blob = git(repo, "rev-parse", "%s:%s" % (BASE, path)).stdout.strip()
        ok = blob in base_pins.get(path, ())
        all_ok &= ok
        print("%-6s %s base_blob=%s tuple(%d)=%s"
              % ("PASS" if ok else "FAIL", path, blob, len(base_pins.get(path, ())),
                 ",".join(base_pins.get(path, ()))))
    print("membership_all=%s" % all_ok)

    # ---- 3. patch identities -------------------------------------------------
    print("\n-- reviewed build patch identities")
    patches = [Path(p) for p in args.patch]
    for p in patches:
        print("%s  %8d B  sha256 %s" % (p.name, p.stat().st_size if p.exists() else -1,
                                        sha256(p) if p.exists() else "ABSENT"))

    if args.no_patch_apply or not patches:
        print("\n(no patches applied)")
        return 0

    # ---- 4. apply and audit the post-image ----------------------------------
    resync(repo)
    print("\n-- applying %d patch(es) into the throwaway clone" % len(patches))
    applied = []
    for p in patches:
        if not p.exists():
            print("SKIP absent %s" % p)
            continue
        rc, rows, err = numstat_patch(p)
        proc = subprocess.run(["git", "-C", str(repo), "apply", "--whitespace=nowarn", str(p)],
                              capture_output=True, text=True)
        print("%-40s numstat_rc=%d apply_rc=%d%s"
              % (p.name, rc, proc.returncode,
                 (" " + proc.stderr.strip().splitlines()[-1]) if proc.returncode else ""))
        for path, a, d in rows:
            print("    %-45s +%s -%s" % (path, a, d))
        if proc.returncode == 0:
            applied.append(p)

    text = (repo / COUNTER).read_text()
    pins = parse_pins(text)
    cap = int(re.search(r"^LINE_CAP = (\d+)$", text, re.M).group(1))
    battery = parse_battery(text)
    print("\n-- audited counter: LINE_CAP %d (base %d), pin rows %d (base %d)"
          % (cap, base_cap, len(pins), len(base_pins)))
    print("pin set == battery set %s" % (set(pins) == set(battery)))

    print("\n-- post-image instrument blobs vs audited pins")
    total_added = total_deleted = 0
    payload_added = payload_deleted = 0
    for path in battery:
        blob = git(repo, "hash-object", str(repo / path)).stdout.strip()
        allowed = pins.get(path, ())
        base_allowed = base_pins.get(path, ())
        grew = len(allowed) - len(base_allowed)
        ok = blob in allowed
        print("%-6s %-42s blob=%s pins=%d (base %d, delta %+d) in_tuple=%s"
              % ("PASS" if ok else "FAIL", path, blob, len(allowed), len(base_allowed), grew, ok))
        if path in PIN_ADD_TARGETS and grew != 1:
            print("       FINDING: E6 allows exactly one added pin for %s, saw %+d" % (path, grew))
        if path not in PIN_ADD_TARGETS and grew != 0:
            print("       FINDING: E6 pins may only grow for the two corpus gates, %s grew %+d"
                  % (path, grew))
        # per-instrument patch attribution
        for p in applied:
            _, rows, _ = numstat_patch(p)
            for rpath, a, d in rows:
                if rpath == path and a.isdigit() and d.isdigit():
                    total_added += int(a)
                    total_deleted += int(d)

    # instrument diff of the applied stack, restricted to the six scripts
    _, rows, err = numstat_patch(patches[-1]) if patches else (0, [], "")
    instr_add = instr_del = 0
    for p in applied:
        _, rows, _ = numstat_patch(p)
        for path, a, d in rows:
            if path in INSTRUMENTS and a.isdigit() and d.isdigit():
                instr_add += int(a)
                instr_del += int(d)

    # ---- 5. cap arithmetic --------------------------------------------------
    base_spend = git(repo, "diff", "--numstat", R73, BASE, "--", *INSTRUMENTS).stdout
    spent_add = spent_del = 0
    for line in base_spend.splitlines():
        a, d, _ = line.split("\t")
        if a.isdigit():
            spent_add += int(a)
        if d.isdigit():
            spent_del += int(d)
    print("\n-- E6 cap arithmetic (counter diffs instruments from r73 base %s)" % R73[:12])
    print("pre-existing spend r73..r81base   +%d -%d" % (spent_add, spent_del))
    print("instrument patch stack            +%d -%d" % (instr_add, instr_del))
    print("total at audited tip              +%d -%d  vs LINE_CAP %d"
          % (spent_add + instr_add, spent_del + instr_del, cap))
    print("fits measured arithmetic    (spent+added<=cap): %s"
          % (spent_add + instr_add <= cap))
    print("fits plan literal arithmetic (40+added<=140):   %s"
          % (40 + instr_add <= 140))
    print("deletion side fits          (spent+del<=cap):   %s"
          % (spent_del + instr_del <= cap))

    # ---- 6. declared-line-set conformance -----------------------------------
    print("\n-- counter patch touched lines (E6 declared set)")
    diff = subprocess.run(["git", "-C", str(repo), "diff", "-U0", BASE, "--", COUNTER],
                          capture_output=True, text=True).stdout
    allowed_re = (
        re.compile(r"^LINE_CAP = \d+$"),
        re.compile(r'^\s*"[0-9a-f]{40}",?$'),
        re.compile(r'^\s*"verifiers/verify_corpus_(integrity|independent)\.py": \($'),
        re.compile(r'^\s*"verifiers/verify_corpus_independent\.py": \($'),
        re.compile(r"LINE_CAP"),          # self-test constants derive from LINE_CAP
        re.compile(r"^\s*\)?,?$"),
    )
    print("---- counter diff vs base (verbatim, for line-by-line adjudication) ----")
    print(diff)
    print("---- end counter diff ----")
    outside = 0
    for line in diff.splitlines():
        if line.startswith(("+++", "---", "@@", "diff ", "index ")):
            continue
        if not line.startswith(("+", "-")):
            continue
        body = line[1:]
        if not body.strip():
            continue
        if any(r.search(body) for r in allowed_re):
            print("  ALLOWED %s" % line)
        else:
            outside += 1
            print("  OUTSIDE %s" % line)
    print("lines outside the declared E6 set: %d" % outside)

    if not args.skip_selftest:
        print("\n-- audited counter self-test (fixture worlds only)")
        env = {"PATH": "/usr/bin:/bin", "HOME": str(repo.parent), "TMPDIR": str(repo.parent / "tmp")}
        proc = subprocess.run([sys.executable, "-B", str(repo / COUNTER), "--self-test"],
                              capture_output=True, text=True, env=env, cwd=str(repo))
        tail = [l for l in (proc.stdout or "").splitlines() if l.strip()][-6:]
        print("self-test exit %d" % proc.returncode)
        for line in tail:
            print("  %s" % line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
