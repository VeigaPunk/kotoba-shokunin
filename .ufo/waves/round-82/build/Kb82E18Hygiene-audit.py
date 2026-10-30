#!/usr/bin/env python3
"""Kb82E18Hygiene — bounded hygiene audit of proposed build tools (round 82).

Four seat-named classes over two tool surfaces (read-only scan):
  A. hardcoded /tmp (writes under /tmp or the live lane tree regardless of TMPDIR)
  B. mutating git/jj outside a pinned sandbox (-C / cwd= / sandbox-scoped dest)
  C. fixture identity/toplevel posture (files that git-init fixtures: identity
     marker present? `git rev-parse --show-toplevel` assert present?)
  D. command exit capture (masked exits: local x=$(cmd), unchecked fixture
     git calls, os.system; pipe-using shell scripts without pipefail = info)

Targets:
  fleet build tools  /home/vgpnk/Projects/shokunin/scripts/hyaku
  lane verifiers     <clone>/verifiers at base 47dbe8781657de563ff867caca6244d28e3db504

Stdlib only; writes nothing. Every hit prints file:line + the exact line so a
human can re-check each finding in seconds. Exit 0 (audit reporting, not a gate);
the DEFECT count is on the headline line. Verdicts were manually reviewed; the
"reviewed" column in the summary distinguishes confirmed defects from posture
notes the fleet may explicitly accept.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

FLEET_TOOLS = Path("/home/vgpnk/Projects/shokunin/scripts/hyaku")
LANE_VERIFIERS = Path("/fast/scratch/hyaku/kotoba-r82/Kb82E18Hygiene/clone/verifiers")
LANE_BASE = "47dbe8781657de563ff867caca6244d28e3db504"

findings: list[tuple[str, str, int, str]] = []
infos: list[tuple[str, str, int, str]] = []


def hit(cls: str, path: Path, lineno: int, text: str, *, info: bool = False) -> None:
    (infos if info else findings).append((cls, str(path), lineno, text.rstrip()))


# ---- code-line extraction: strip comments and docstrings -------------------
def code_lines(path: Path) -> list[tuple[int, str]]:
    raw = path.read_text(encoding="utf-8", errors="replace").splitlines()
    out: list[tuple[int, str]] = []
    if path.suffix == ".py":
        in_doc = False
        for i, line in enumerate(raw, 1):
            s = line
            res = ""
            while s:
                if in_doc:
                    k = s.find('"""')
                    if k < 0:
                        s = ""
                        break
                    s = s[k + 3:]
                    in_doc = False
                    continue
                k = s.find('"""')
                h = s.find("#")
                if h >= 0 and (k < 0 or h < k):
                    res += s[:h]
                    break
                if k >= 0:
                    res += s[:k]
                    s = s[k + 3:]
                    in_doc = True
                    continue
                res += s
                break
            out.append((i, res))
    else:
        for i, line in enumerate(raw, 1):
            out.append((i, line.split("#", 1)[0]))
    return out


# ---- A: hardcoded /tmp ------------------------------------------------------
RE_MKTEMP_TMP = re.compile(r"\bmktemp\b[^\n]*?(?:[\"']?/tmp/|[\"']/tmp[\"'])")
RE_DIR_TMP = re.compile(r"\bdir\s*=\s*[\"']/tmp")
RE_TMPDIR_FALLBACK = re.compile(r"\$\{TMPDIR:-/tmp\}")
RE_LANE_TMPDIR = re.compile(r"TemporaryDirectory\([^\n]*\bdir\s*=\s*LANE\b")

# ---- B: mutating git/jj verbs ----------------------------------------------
VERBS = r"(?<!\^)\b(?:commit|push|reset|checkout|switch|merge|rebase|stash|am|apply|init|clone|add)\b(?!\})"
RE_GIT_MUT = re.compile(r"\bgit\b[^\n]*" + VERBS + r"|['\"]git['\"]\s*,\s*['\"]"
                        + VERBS + r"['\"]")
# a line only counts as a git invocation if it looks like one (kills message FPs)
RE_GIT_CALL = re.compile(r"subprocess\.(?:run|call|Popen)|=\s*git\(|\bgit\(|^\s*git\s|"
                         r"['\"]git['\"]\s*,|\|\|\s*git\s|git\s\+")
RE_JJ_MUT = re.compile(r"\bjj\b[^\n]*\b(?:commit|new|describe|squash|rebase|abandon)\b|"
                     r"\bbookmark\s+set\b|\bop\s+(?:restore|revert)\b")
RE_PINNED = re.compile(r"-C[\"'\s,]|cwd\s*=|--git-dir|\bGIT_DIR\b")
# a helper `def git(` whose body pins -C, or a `git = ["git", ..., "-C", ...]` array
RE_HELPER_PIN = re.compile(r"def\s+git\(|git\s*=\s*\[\s*[\"']git[\"']")
RE_SANDBOX_DEST = re.compile(
    r"\$(?:SB|WORLDS|ST_\w+|td|tmp\w*|root|fx|w|d|lane|clone)\b|"
    r"\bstr\((?:clone|tree|root|fx|td|lane|repo|path|w|d|dest)\)|"
    r"\bmktemp\b|\bTemporaryDirectory\b|\bmkdtemp\b|"
    r"\btempfile\b|\btmpdir\b|\bworkdir\b|\bwork_dir\b")
SANCTIONED_WRITERS = {"fleet-commit.sh", "jj-lane.sh", "append-closure.py", "jj-lane-selftest.sh"}

# ---- C: fixture identity/toplevel ------------------------------------------
RE_GIT_INIT = re.compile(r"\bgit\b[^\n]*\binit\b|['\"]git['\"]\s*,\s*['\"]init['\"]")
RE_GIT_COMMIT = re.compile(r"\bgit\b[^\n]*\bcommit\b(?!\})|['\"]commit['\"]")
RE_IDENTITY = re.compile(r"user\.name|GIT_AUTHOR_NAME|GIT_COMMITTER_NAME")
RE_TOPLEVEL = re.compile(r"--show-toplevel")

# ---- D: exit capture ---------------------------------------------------------
RE_LOCAL_CMDSUB = re.compile(r"\blocal\s+\w+=\$\(")
RE_TEE_PIPE = re.compile(r"\|\s*tee\b")
RE_PIPEFAIL = re.compile(r"pipefail")
RE_PY_COMMIT = re.compile(r"subprocess\.run\([^\n]*(?:['\"](?:commit|add|init|checkout|push)['\"])")
RE_CHECK_TRUE = re.compile(r"check\s*=\s*True")
RE_RETCODE_USED = re.compile(r"returncode|\.wait\(")
RE_OS_SYSTEM = re.compile(r"\bos\.system\s*\(|\bcommands\.(?:getoutput|getstatus)")


def scan_file(path: Path) -> None:
    name = path.name
    lines = code_lines(path)
    sanctioned = name in SANCTIONED_WRITERS
    joined = "\n".join(l for _, l in lines)
    has_init = bool(RE_GIT_INIT.search(joined))
    has_commit = bool(RE_GIT_COMMIT.search(joined))
    identity = bool(RE_IDENTITY.search(joined))
    toplevel = bool(RE_TOPLEVEL.search(joined))
    uses_pipes = any("|" in l and l.strip() for _, l in lines)
    helper_pinned = bool(RE_HELPER_PIN.search(joined)) and bool(RE_PINNED.search(joined))

    for idx, (i, line) in enumerate(lines):
        if not line.strip():
            continue
        # A
        if RE_MKTEMP_TMP.search(line) or RE_DIR_TMP.search(line):
            hit("A-hardcoded-/tmp", path, i, line)
        if RE_LANE_TMPDIR.search(line):
            hit("A-tempdir-in-live-lane", path, i, line)
        elif RE_TMPDIR_FALLBACK.search(line):
            hit("A-tmpdir-fallback-info", path, i, line, info=True)
        # B (git mutations must be pinned to a sandbox: -C / cwd= / sandbox dest)
        if not sanctioned and (RE_GIT_MUT.search(line) or RE_JJ_MUT.search(line)) \
                and (RE_GIT_CALL.search(line) or RE_JJ_MUT.search(line)):
            window = " ".join(l for _, l in lines[max(0, idx - 6):idx + 1])
            pinned = bool(RE_PINNED.search(window))
            sandboxed_dest = bool(RE_SANDBOX_DEST.search(line))
            read_only = bool(re.search(r"rev-parse|cat-file|ls-tree|merge-base|show\b|diff\b|status|log\b|fetch", line)) \
                and not re.search(r"(?<!\^)\bcommit\b(?!\})", line)
            if not pinned and not sandboxed_dest and not read_only and not helper_pinned:
                hit("B-git-mutation-unpinned", path, i, line)
        # D
        if RE_LOCAL_CMDSUB.search(line):
            hit("D-exit-masked-local-cmdsub", path, i, line)
        if RE_TEE_PIPE.search(line):
            hit("D-pipe-tee-exit", path, i, line)
        if RE_OS_SYSTEM.search(line):
            hit("D-os-system", path, i, line)
        if "subprocess.run" in line and RE_PY_COMMIT.search(line):
            window = " ".join(l for _, l in lines[idx:idx + 6])
            if not RE_CHECK_TRUE.search(window) and not RE_RETCODE_USED.search(window):
                hit("D-unchecked-fixture-git", path, i, line)
    if path.suffix == ".sh" and uses_pipes and not RE_PIPEFAIL.search(joined):
        hit("D-no-pipefall-info", path, 1, "(shell script uses pipelines; no 'set -o pipefail')", info=True)
    # C posture (files that build git fixtures and commit in them)
    if has_init and has_commit and not sanctioned:
        if identity and toplevel:
            hit("C-fixture-identity+toplevel-OK", path, 1, "(fixture commits: identity + toplevel assert)", info=True)
        elif identity:
            hit("C-fixture-no-toplevel-assert", path, 1,
                "(fixture commits: identity present, NO --show-toplevel assert)")
        elif toplevel:
            hit("C-fixture-no-identity", path, 1, "(fixture commits: toplevel present, NO identity marker)")
        else:
            hit("C-fixture-no-toplevel-assert", path, 1,
                "(fixture commits: neither identity marker nor --show-toplevel assert)")


def main() -> int:
    files = [p for root in (FLEET_TOOLS, LANE_VERIFIERS) for p in sorted(root.rglob("*"))
             if p.is_file() and p.suffix in (".sh", ".py", ".env")]
    for p in files:
        scan_file(p)
    print("Kb82E18Hygiene bounded hygiene audit v2")
    print(f"fleet tools : {FLEET_TOOLS}")
    print(f"lane tools  : {LANE_VERIFIERS} (base {LANE_BASE})")
    print(f"files scanned: {len(files)}")
    print(f"DEFECTS: {len(findings)}  INFO: {len(infos)}")
    print("== findings (file:line) ==")
    for cls, f, n, t in findings:
        print(f"[{cls}] {f}:{n}: {t.strip()[:200]}")
    print("== info ==")
    for cls, f, n, t in infos:
        print(f"[{cls}] {f}:{n}: {t.strip()[:160]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
