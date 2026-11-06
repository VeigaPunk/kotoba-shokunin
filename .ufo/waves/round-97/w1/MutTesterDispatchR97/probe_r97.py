#!/usr/bin/env python3
"""MutTesterDispatchR97 probe driver (round 97, wave r97-w1; NOT a lane file).

Measures a table of NEW mutants of verifiers/verify_dispatch_prompts.py at a given
revision with the v5 counter's own machinery (RUNNER, classify, code_decoy,
NotEvaluated imported from a scratch copy of
verifiers/fixtures/round-97/selftest-kills.py) and the v5 rules 4-5: every run
gets a fresh clone of REV plus a fresh TMPDIR/HOME/XDG_CACHE_HOME, and a mutant
is KILLED only when its source-blind run AND its mirror run are both
REPORTED-FAILURE.  The comment decoy and code decoy are measured too.

Usage: python3 -B probe_r97.py LABEL REV REPO
Exit 0 measurement completed, 2 could-not-evaluate. Never edits the lane.
"""
from __future__ import annotations

import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
COUNTER_SRC = LANE / "verifiers/fixtures/round-97/selftest-kills.py"
INSTRUMENT = "verifiers/verify_dispatch_prompts.py"
PREFIX = "self-test FAIL: "
TIMEOUT_S = 600

# (id, anchor, replacement, class, note)
# Every anchor is a literal substring of the instrument; every replacement keeps
# the line count (the counter's code decoy refuses a line-count change).
MUTANTS = [
    ("m20-lane-suffix-unanchored",
     'ROUND_FILE_RE = re.compile(r"^(?P<lane>.+)-round-(?P<round>\\d+)\\.md$")',
     'ROUND_FILE_RE = re.compile(r"^(?P<lane>.+)-round-(?P<round>\\d+)\\.md")',
     "lane-name-parse",
     "the prompt-name regex is not end-anchored, so 'kote-round-7.md.bak' "
     "names a dispatch prompt"),
    ("m21-l1-kind-round",
     'return m.group("lane"), None, "l1"',
     'return m.group("lane"), None, "round"',
     "l1-kind",
     "an L1 spawn file is typed 'round', so dispatch.08 evaluates it"),
    ("m22-dirs-first-only",
     "dirs = sorted({r for r, _s in paths})",
     "dirs = sorted({r for r, _s in paths})[:1]",
     "report-dir-set",
     "only the lowest report-dir round is compared to the file-name round"),
    ("m23-verdict-first-file",
     '    for f in result["files"]:',
     '    for f in result["files"][:1]:',
     "_verdict_of",
     "the verdict lookup searches only the first evaluated file"),
    ("m24-proof-disposition-unenforced",
     '        if entry.get("disposition") != want:',
     '        if entry.get("disposition") is None:',
     "box-proof-map",
     "a map entry whose disposition is not the delegation is accepted"),
    ("m25-proof-live-hash-unenforced",
     "        if live.get(cid) != pinned:",
     "        if live.get(cid) is None:",
     "box-proof-live-hash",
     "the live SKILL.md box hash is not compared to the pin when present"),
    ("m26-fence-any-close",
     "        if m and m.group(1)[0] * 3 == fence:",
     "        if m:",
     "box-hash-fence",
     "any fence line closes a fenced block, whatever its marker"),
    ("m27-legacy-exists",
     "    if legacy.is_file():",
     "    if legacy.exists():",
     "state-legacy-kind",
     "a directory named <lane>.round counts as the legacy state file"),
    ("m28-prompts-include-dirs",
     '    """The dispatch.04 box over the prompts directory."""\n'
     "    names = sorted(p.name for p in prompts_dir.iterdir() if p.is_file())",
     '    """The dispatch.04 box over the prompts directory."""\n'
     "    names = sorted(p.name for p in prompts_dir.iterdir() if True)",
     "prompts-listing",
     "a subdirectory of the prompts directory is treated as a prompt file"),
    ("m29-file-result-na-first",
     '    if "FAIL" in statuses:\n        verdict = "FAIL"\n'
     '    elif "N/A" in statuses:\n        verdict = "N/A"',
     '    if "N/A" in statuses:\n        verdict = "N/A"\n'
     '    elif "FAIL" in statuses:\n        verdict = "FAIL"',
     "_file_result-precedence",
     "a file with one FAIL and one N/A conjunct reads N/A, not FAIL"),
    ("m30-state-splitlines",
     "        first = raw.split()[:1]",
     "        first = raw.splitlines()[:1]",
     "state-source-split",
     "the baseline round is read from the whole first line, not its first field"),
    ("m31-md-uppercase",
     '        if stem.endswith(".md"):',
     '        if stem.endswith(".md") or stem.endswith(".MD"):',
     "report-stem-suffix",
     "an upper-case .MD report suffix is stripped like .md"),
    ("m32-report-paths-sorted",
     "        out.append((int(m.group(1)), stem))\n    return out",
     "        out.append((int(m.group(1)), stem))\n    return sorted(out)",
     "report-path-order",
     "report_paths returns its paths sorted instead of in text order"),
    ("m33-role-last-line",
     "    m = ROLE_ROUND_RE.search(lines[0])",
     "    m = ROLE_ROUND_RE.search(lines[-1])",
     "role-line",
     "the role round is read from the last line, not line 1"),
    ("m34-finish-fails-first-only",
     "            for f in fails[:12])",
     "            for f in fails[:1])",
     "_finish-detail",
     "the failing-files detail names only the first failing file"),
]


def load_counter():
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r97" / "counter"
    root.mkdir(parents=True, exist_ok=True)
    copy = root / "selftest-kills-v5.py"
    shutil.copyfile(COUNTER_SRC, copy)
    spec = importlib.util.spec_from_file_location("frozen_counter_r97", copy)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fresh_world(work: Path, repo: str, rev: str, tag: str) -> tuple[Path, Path, dict]:
    d = Path(tempfile.mkdtemp(prefix=tag + ".", dir=work))
    clone = d / "world" / "kotoba-shokunin"
    clone.parent.mkdir()
    for sub in ("tmp", "home", "cache"):
        (d / sub).mkdir()
    for cmd in (["git", "clone", "-q", "--shared", "--no-checkout", repo, str(clone)],
                ["git", "-C", str(clone), "checkout", "-q", "--detach", rev]):
        if subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
            raise RuntimeError("clone or checkout failed")
    env = dict(os.environ, TMPDIR=str(d / "tmp"), HOME=str(d / "home"),
               XDG_CACHE_HOME=str(d / "cache"), PYTHONDONTWRITEBYTECODE="1")
    return d, clone, env


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: probe_r97.py LABEL REV REPO", file=sys.stderr)
        return 2
    label, rev, repo = argv
    c = load_counter()
    got = subprocess.run(["git", "-C", repo, "rev-parse", "--verify", "-q", rev + "^{commit}"],
                         stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if got.returncode != 0:
        print("PROBE-NOT-EVALUATED: REV %s is not a commit of %s" % (rev, repo))
        return 2
    rev = got.stdout.decode().strip()
    root = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "kotoba-r97" / "probe"
    root.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="%s." % label, dir=root))
    try:
        shown = subprocess.run(["git", "-C", repo, "show", "%s:%s" % (rev, INSTRUMENT)],
                               stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if shown.returncode != 0:
            print("PROBE-NOT-EVALUATED: instrument absent at %s" % rev)
            return 2
        original = shown.stdout.decode("utf-8")
        before = sha(original)
        csha = sha(COUNTER_SRC.read_text(encoding="utf-8"))
        print("probe %s rev %s repo %s instrument %s sha256 %s counter sha256 %s"
              % (label, rev, repo, INSTRUMENT, before, csha))

        def run_text(text: str, on_disk: str, what: str) -> tuple[int, str, str, str]:
            try:
                compile(text, INSTRUMENT, "exec", dont_inherit=True)
            except SyntaxError as exc:
                return -1, "does not compile: %s" % exc, "NOT-COMPILED", "-"
            try:
                d, clone, env = fresh_world(work, repo, rev, what.replace(" ", "-"))
            except RuntimeError as exc:
                raise c.NotEvaluated(str(exc))
            try:
                path = clone / INSTRUMENT
                path.write_text(on_disk, encoding="utf-8")
                src = d / "src.py"
                src.write_text(text, encoding="utf-8")
                try:
                    proc = subprocess.run([sys.executable, "-B", "-c", c.RUNNER, str(path), str(src)],
                                          cwd=clone, env=env, stdout=subprocess.PIPE,
                                          stderr=subprocess.STDOUT, timeout=TIMEOUT_S)
                except subprocess.TimeoutExpired:
                    raise c.NotEvaluated("%s: self-test timeout after %ds" % (what, TIMEOUT_S))
                out = proc.stdout.decode("utf-8", "replace")
                restored = "OK" if sha(path.read_text(encoding="utf-8")) == sha(on_disk) else "MISMATCH"
                return proc.returncode, out, c.classify(proc.returncode, out, PREFIX), restored
            finally:
                shutil.rmtree(d, ignore_errors=True)

        def summary(out: str) -> str:
            return c.last_line(out)

        def fails(out: str) -> list[str]:
            return [ln for ln in out.splitlines() if ln.startswith(PREFIX)]

        rc, out, cls, restored = run_text(original, original, "honest-before")
        print("honest-before rc %d %s restored %s: %s" % (rc, cls, restored, summary(out)))
        honest_clean = cls == "CLEAN"
        rows = []
        for mid, anchor, repl, klass, note in MUTANTS:
            n = original.count(anchor)
            if n != 1:
                print("mutant %s ANCHOR-MISS (%d match(es)) [%s]" % (mid, n, klass))
                rows.append((mid, klass, "ANCHOR-MISS", "-", "-", "-", ""))
                continue
            mutated = original.replace(anchor, repl)
            brc, bout, bcls, brest = run_text(mutated, original, "blind-" + mid)
            mrc, mout, mcls, mrest = run_text(mutated, mutated, "mirror-" + mid)
            killed = bcls == "REPORTED-FAILURE" and mcls == "REPORTED-FAILURE"
            if killed:
                verdict = "KILLED"
            elif "RUN-ERROR" in (bcls, mcls) or "NOT-COMPILED" in (bcls, mcls):
                verdict = "RUN-ERROR"
            else:
                verdict = "SURVIVED"
            print("mutant %s [%s]" % (mid, klass))
            print("  blind  rc %d %s restored %s: %s" % (brc, bcls, brest, summary(bout)))
            print("  mirror rc %d %s restored %s: %s" % (mrc, mcls, mrest, summary(mout)))
            for ln in fails(bout)[:4]:
                print("  | blind  %s" % ln)
            for ln in fails(mout)[:4]:
                print("  | mirror %s" % ln)
            ctext = original.rstrip("\n") + "\n" + "".join(
                c.DECOY_MARK + ln + "\n" for ln in repl.splitlines())
            crc, cout, ccls, crestore = run_text(ctext, ctext, "comment-" + mid)
            print("  comment decoy rc %d %s restored %s: %s"
                  % (crc, "HELD" if ccls == "CLEAN" else ccls, crestore, summary(cout)))
            try:
                dtext = c.code_decoy(original, mutated, mid)
                drc, dout, dcls, drestore = run_text(dtext, dtext, "code-" + mid)
                print("  code decoy rc %d %s restored %s: %s"
                      % (drc, "HELD" if dcls == "CLEAN" else dcls, drestore, summary(dout)))
                decoy = "HELD" if dcls == "CLEAN" else dcls
            except c.NotEvaluated as exc:
                print("  code decoy NOT-EVALUATED: %s" % exc)
                decoy = "NOT-EVALUATED"
            print("  => %s" % verdict)
            rows.append((mid, klass, verdict, bcls, mcls,
                         "comment=%s code=%s" % ("HELD" if ccls == "CLEAN" else ccls, decoy), note))
        rc, out, cls, restored = run_text(original, original, "honest-after")
        print("honest-after rc %d %s restored %s: %s" % (rc, cls, restored, summary(out)))
        print("--- summary %s ---" % label)
        for mid, klass, verdict, bcls, mcls, decoys, note in rows:
            print("%-34s %-24s %-12s blind=%-16s mirror=%-16s %s"
                  % (mid, klass, verdict, bcls, mcls, decoys))
        counts: dict[str, int] = {}
        for _m, _k, v, _b, _mi, _d, _n in rows:
            counts[v] = counts.get(v, 0) + 1
        print("honest %s; totals %s" % (
            "CLEAN" if honest_clean and cls == "CLEAN" else "NOT-CLEAN",
            ", ".join("%s %d" % (k, counts[k]) for k in sorted(counts))))
        return 0 if honest_clean and cls == "CLEAN" else 2
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
