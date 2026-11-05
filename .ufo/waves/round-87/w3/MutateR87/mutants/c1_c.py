#!/usr/bin/env python3
r"""check_omp_root_semantics.py -- frozen counter for the round-87 C1 (depth) claim.

Frozen predicate (the same sentence in plans/round-87.md, here, and in every receipt):

    python3 -B verifiers/check_omp_root_semantics.py --rev <rev>
        -> prints "omp root semantics grounded N of 12", exit 0 iff N == 12 and
           guards S1-S3 all PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

Claim C1: every root the lane records in `verifiers/omp-skill-roots-semantics.tsv`
(header `root_pattern<TAB>binary_quote<TAB>module<TAB>reader_quote`) is grounded by the
code that actually reads it, not by a doc/string-table line.  Round 86 located a quote per
root but left the meaning to a reviewer (its CF1: no code quote can satisfy the round-86
dot rule for the plugin root).  This counter scores the four conjuncts of plans/round-87.md
§ C1 on the revision's committed bytes.

A row is **grounded** iff all four conjuncts hold for that row:

  1 pattern  `root_pattern` equals the row's pattern in the round-86 ledger
             `verifiers/omp-skill-roots.tsv` at `<rev>` (no row added, dropped or renamed),
             contains no `..` segment and no wildcard in its first segment.
  2 reader   `reader_quote` (>= 12 chars) occurs verbatim in the installed omp ELF **and**
             on an ELF line that also carries a path-join token from JOIN_TOKENS, so a
             doc/string-table line cannot satisfy it.
  3 module   `module` names a source module; the header comment `// packages/<module>`
             occurs in the ELF and the reader quote's first occurrence lies **after** that
             header's last occurrence.
  4 bound    for a `{cwd}/` row the expansion set (the session cwd and its ancestors)
             excludes `$HOME` and above unless the row is a `~/` row, and the matcher
             refuses any candidate root that contains a `..` segment.  Probed on the frozen
             ancestor chain `/home/u/proj/sub` -> `/home/u/proj`, `/home/u`, `/home`, `/`.

Guards: S1 both ledgers are read from `<rev>`'s committed bytes (`git show`), never the
worktree; S2 the ELF sha256 equals OMP_SHA256 (else exit 2); S3 the semantics ledger's
`root_pattern` column equals the round-86 ledger's at `<rev>` (a shrunken ledger cannot
pass).

Denominator: TOTAL = 12 is the frozen denominator of plans/round-87-addendum-1.md A1.1 (the
round-86 ledger carries 12 data rows).  The counter prints
the frozen sentence verbatim and, when the round-86 ledger at `<rev>` carries a different
number of patterns, says so on its own `note:` line -- the counter never renames the target.

A missing ledger, a missing cell or a wrong header at `<rev>` is a CONTENT verdict (exit 1,
N lower), never exit 2 (round-68 routed defect R67-1).  Exit 2 only when the revision, git or
the omp binary cannot be read, or the binary is not the pinned build.

`--self-test` builds synthetic worlds (git repos holding both ledgers plus a synthetic ELF)
under $TMPDIR / --work and prints `0 failure(s) over N assertions`.  Worlds: `w_noledger`,
`w_docquote`, `w_nomodule`, `w_dotdot`, `w_star`, `w_shrink`, `w_bound`, `w_quote_miss`,
`w_offset_order`, and the honest 12-row world that must pass.

Usage: check_omp_root_semantics.py --rev REV [--repo DIR] [--work DIR]
       check_omp_root_semantics.py --self-test [--work DIR]
Exit 0 pass (12 of 12, S1-S3 PASS), 1 content fail, 2 could-not-evaluate.
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import mmap
import os
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

SEMANTICS_LEDGER = "verifiers/omp-skill-roots-semantics.tsv"
ROOTS_LEDGER = "verifiers/omp-skill-roots.tsv"
SEMANTICS_HEADER = "root_pattern\tbinary_quote\tmodule\treader_quote"
ROOTS_HEADER = "root_pattern\tbinary_quote"

TOTAL = 12                      # frozen denominator (plans/round-87-addendum-1.md A1.1)
QUOTE_MIN = 12
JOIN_TOKENS = ("join(", ".join(", "resolve(", "path.join")
WILD = set("*?[")
LINE_SPAN = 8192                # bounded window for the enclosing ELF line

OMP_BINARY = Path("/home/vgpnk/.local/bin/omp")
OMP_SHA256 = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"

BOUND_CWD = "/home/u/proj/sub"
BOUND_HOME = "/home/u"
FROZEN_CHAIN = (BOUND_CWD, "/home/u/proj")                        # cwd + ancestors below $HOME
FULL_CHAIN = (BOUND_CWD, "/home/u/proj", "/home/u", "/home", "/")  # the unbounded walk-up

HEADER_RE = re.compile(rb"//[ \t]*packages/([A-Za-z0-9_./@-]+)")


class Inconclusive(Exception):
    """The evaluation itself cannot run (missing git, unreadable/unpinned ELF, ...)."""


# --------------------------------------------------------------------------- revision bytes

def git_show(repo: Path, rev: str, path: str) -> str | None:
    """Committed bytes of `path` at `rev`, or None when the path is absent there.

    The worktree is never consulted: a missing path is a content verdict, not an error.
    """
    try:
        proc = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{path}"],
                              capture_output=True, check=False)
    except FileNotFoundError:
        raise Inconclusive("git not found")
    if proc.returncode != 0:
        return None
    return proc.stdout.decode("utf-8", "replace")


def open_elf(path: Path, pinned: str | None):
    """mmap the ELF (never copy it) and check the pinned build."""
    try:
        handle = open(path, "rb")
    except OSError as exc:
        raise Inconclusive(f"omp binary unreadable: {exc}")
    try:
        blob = mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ)
    except (OSError, ValueError) as exc:
        handle.close()
        raise Inconclusive(f"omp binary not mappable: {exc}")
    try:
        if blob.size() == 0:
            raise Inconclusive("omp binary is empty")
        digest = hashlib.sha256(blob).hexdigest()
        if pinned is not None and digest != pinned:
            raise Inconclusive(f"omp binary sha256 {digest} is not the pinned build {pinned}")
    except Inconclusive:
        blob.close()
        handle.close()
        raise
    return blob, digest


# ------------------------------------------------------------------------------- ELF probes

def elf_line(blob, offset: int) -> bytes:
    """The newline-delimited slice around `offset`, bounded by LINE_SPAN on each side."""
    start = blob.rfind(b"\n", max(0, offset - LINE_SPAN), offset)
    start = 0 if start < 0 else start + 1
    end = blob.find(b"\n", offset, offset + LINE_SPAN)
    end = blob.size() if end < 0 else end
    return blob[start:end]


def occurrences(blob, needle: bytes, limit: int = 8) -> list[int]:
    out, at = [], blob.find(needle)
    while at >= 0 and len(out) < limit:
        out.append(at)
        at = blob.find(needle, at + 1)
    return out


def reader_grounded(blob, reader: str) -> tuple[bool, str, int | None]:
    """Conjunct 2: the quote occurs, and one of its lines carries a JOIN_TOKENS member."""
    if len(reader) < QUOTE_MIN:
        return False, f"reader_quote shorter than {QUOTE_MIN} chars", None
    raw = reader.encode("utf-8")
    offsets = occurrences(blob, raw)
    if not offsets:
        return False, "reader_quote not located in the omp ELF", None
    for offset in offsets:
        line = elf_line(blob, offset)
        if any(token.encode("utf-8") in line for token in JOIN_TOKENS):
            return True, "", offsets[0]
    return False, "reader_quote sits on no ELF line carrying a path-join token", offsets[0]


def module_offsets(blob, module: str) -> list[int]:
    """Byte offsets of the `// packages/<module>` header comment (whole-token matches)."""
    header = b"// packages/" + module.encode("utf-8")
    pattern = re.compile(re.escape(header) + rb"(?![A-Za-z0-9_.@/-])")
    return [m.start() for m in pattern.finditer(blob)]


def module_grounded(blob, module: str, first_reader: int | None) -> tuple[bool, str]:
    """Conjunct 3: the module header exists and precedes the reader quote's first occurrence."""
    if not module.strip():
        return False, "module cell is empty"
    if ".." in module.split("/"):
        return False, f"module {module!r} carries a `..` segment"
    if any(ch in module for ch in " \t"):
        return False, f"module {module!r} carries whitespace"
    offsets = module_offsets(blob, module)
    if not offsets:
        return False, f"header `// packages/{module}` not located in the omp ELF"
    last = offsets[-1]
    if first_reader is None:
        return False, "reader quote has no located occurrence to order against the header"
    if first_reader < last:
        return False, (f"reader quote first occurs at {first_reader}, before the header's last "
                       f"occurrence at {last}")
    return True, ""


# ---------------------------------------------------------------------------- pattern/bound

def pattern_problem(pattern: str) -> str | None:
    """Conjunct 1's shape half: no `..` segment, no wildcard in the first segment."""
    segments = [s for s in pattern.split("/") if s]
    if not segments:
        return f"pattern {pattern!r} names no directory"
    for prefix in ("{cwd}/", "~/"):
        if pattern.startswith(prefix):
            rel = pattern[len(prefix):]
            break
    else:
        rel = pattern.lstrip("/")
    first = next((s for s in rel.split("/") if s), "")
    if not first:
        return f"pattern {pattern!r} has no first segment"
    if WILD & set(first):
        return f"pattern {pattern!r} has a wildcard in its first segment ({first!r})"
    return None


def expansions(pattern: str, chain) -> list[str]:
    """Candidate roots a pattern names, walked over `chain` (cwd first)."""
    if pattern.startswith("{cwd}/"):
        rest = pattern[len("{cwd}/"):]
        return [posixpath.normpath(posixpath.join(d, rest)) for d in chain]
    if pattern.startswith("~/"):
        return [posixpath.normpath(posixpath.join(BOUND_HOME, pattern[2:]))]
    return [posixpath.normpath(pattern)]


def at_or_above(path: str, home: str) -> bool:
    """True when `path` is $HOME itself or an ancestor of it."""
    return path == home or home.startswith(path.rstrip("/") + "/")


def matches_row(pattern: str, candidate: str, chain) -> bool:
    """The counter's matcher.  A candidate carrying a `..` segment never matches a row."""
    if ".." in candidate.split("/"):
        return False
    if ".." in posixpath.normpath(candidate).split("/"):
        return False
    return any(fnmatch.fnmatchcase(candidate, exp) for exp in expansions(pattern, chain))


def bound_grounded(pattern: str, chain) -> tuple[bool, str]:
    """Conjunct 4 on the frozen synthetic ancestor chain."""
    expected = None
    if pattern.startswith("{cwd}/"):
        rest = pattern[len("{cwd}/"):]
        if not rest or rest.startswith("/") or ".." in rest.split("/"):
            return False, f"pattern {pattern!r}: `{{cwd}}/` rest is not a plain relative path"
        expected = expansions(pattern, FROZEN_CHAIN)
        actual = expansions(pattern, chain)
        if actual != expected:
            extra = [p for p in actual if p not in expected]
            return False, (f"pattern {pattern!r}: `{{cwd}}/` expansion reaches "
                           f"{extra[0] if extra else actual[0]} ($HOME or above); the frozen "
                           f"expansion is {expected}")
    else:
        actual = expansions(pattern, chain)
    for root in actual:
        if ".." in root.split("/"):
            return False, f"pattern {pattern!r} expands to a `..` candidate ({root})"
        if pattern.startswith("~/") and not (root == BOUND_HOME or root.startswith(BOUND_HOME + "/")):
            return False, f"pattern {pattern!r} expands outside $HOME ({root})"
        if not pattern.startswith("~/") and at_or_above(root, BOUND_HOME):
            return False, (f"pattern {pattern!r} expands to {root}, which is $HOME or above it")
    for probe in (f"{BOUND_CWD}/../sub/.probe/skills", "/home/u/../u/.probe/skills"):
        if matches_row(pattern, probe, chain):
            return False, f"pattern {pattern!r} matches the `..` candidate {probe}"
    return True, ""


# --------------------------------------------------------------------------------- scoring

def parse_ledger(text: str, header: str) -> tuple[list[tuple[int, str]] | None, str | None]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return None, "ledger is empty"
    if lines[0] != header:
        return None, f"header is not {header!r}"
    return list(enumerate(lines[1:], 2)), None


def roots_patterns(text: str | None) -> tuple[list[str], str | None]:
    if text is None:
        return [], f"{ROOTS_LEDGER} absent at the revision"
    rows, err = parse_ledger(text, ROOTS_HEADER)
    if err:
        return [], f"{ROOTS_LEDGER}: {err}"
    patterns = []
    for number, line in rows:
        cells = line.split("\t")
        if len(cells) != 2 or not cells[0].strip():
            return patterns, f"{ROOTS_LEDGER} line {number}: want 2 tab-separated cells"
        patterns.append(cells[0].strip())
    return patterns, None


def score(semantics: str | None, roots: str | None, blob, chain, out) -> tuple[int, dict]:
    """Evaluate the four conjuncts; returns (grounded N, guards) and prints the receipt."""
    guards = {"S1": True, "S3": True}
    root_patterns, roots_err = roots_patterns(roots)
    if roots_err:
        out(f"roots ledger: {roots_err}")

    rows: list[tuple[int, str]] = []
    sem_err = None
    if semantics is None:
        sem_err = f"{SEMANTICS_LEDGER} absent at the revision"
    else:
        parsed, sem_err = parse_ledger(semantics, SEMANTICS_HEADER)
        if parsed is not None:
            rows = parsed
    if sem_err:
        out(f"semantics ledger: {sem_err}")

    # S3: the pattern column must equal the round-86 ledger's at the same revision.
    seen = []
    for number, line in rows:
        cells = line.split("\t")
        seen.append(cells[0].strip() if cells else "")
    if seen != root_patterns:
        guards["S3"] = False
        if len(seen) != len(root_patterns):
            out(f"S3 detail: semantics ledger carries {len(seen)} patterns, "
                f"the round-86 ledger carries {len(root_patterns)}")
        else:
            first = next((i for i, (a, b) in enumerate(zip(seen, root_patterns)) if a != b), 0)
            out(f"S3 detail: pattern {first + 1} is {seen[first]!r}, "
                f"the round-86 ledger has {root_patterns[first]!r}")

    grounded = 0
    for index, (number, line) in enumerate(rows, 1):
        if index > TOTAL:
            out(f"row {index:2d} EXTRA: beyond the frozen denominator of {TOTAL}")
            continue
        cells = [cell.rstrip("\r") for cell in line.split("\t")]
        if len(cells) != 4:
            out(f"row {index:2d} FAIL (ledger line {number}): want 4 tab-separated cells, got {len(cells)}")
            continue
        pattern, module, reader = cells[0].strip(), cells[2].strip(), cells[3].strip()
        reasons = []
        expected = root_patterns[index - 1] if index <= len(root_patterns) else None
        if expected is None:
            reasons.append(f"the round-86 ledger has no row {index} to match")
        elif pattern != expected:
            reasons.append(f"pattern {pattern!r} is not the round-86 ledger's row {index} "
                           f"({expected!r})")
        else:
            problem = pattern_problem(pattern)
            if problem:
                reasons.append(problem)
        reader_ok, reader_why, first = reader_grounded(blob, reader)
        if not reader_ok:
            reasons.append(reader_why)
        module_ok, module_why = module_grounded(blob, module, first if reader_ok else None)
        if not module_ok:
            reasons.append(module_why)
        bound_ok, bound_why = bound_grounded(pattern, chain)
        if not bound_ok:
            reasons.append(bound_why)
        if reasons:
            out(f"row {index:2d} FAIL {pattern!r}: " + "; ".join(reasons))
        else:
            grounded += 1
            out(f"row {index:2d} GROUND {pattern!r} module={module!r} @{first}")

    if len(root_patterns) != TOTAL:
        out(f"note: the round-86 ledger at the revision carries {len(root_patterns)} patterns; "
            f"the frozen denominator is {TOTAL} (plans/round-87.md C1)")
    return grounded, guards


def run(repo: Path, rev: str, elf: Path, pinned: str | None, out=print,
        chain=FROZEN_CHAIN) -> int:
    semantics = git_show(repo, rev, SEMANTICS_LEDGER)
    roots = git_show(repo, rev, ROOTS_LEDGER)
    blob, digest = open_elf(elf, pinned)
    try:
        out(f"rev {rev} elf {elf} sha256 {digest}")
        out(f"guard S1 ledger-from-rev PASS (git show {rev}:{SEMANTICS_LEDGER} "
            f"rc={'0' if semantics is not None else 'absent'}, "
            f"git show {rev}:{ROOTS_LEDGER} rc={'0' if roots is not None else 'absent'})")
        out(f"guard S2 elf-sha256 PASS ({digest})")
        grounded, guards = score(semantics, roots, blob, chain, out)
        s3 = "PASS" if guards["S3"] else "FAIL"
        out(f"guard S3 pattern-set {s3}")
        out(f"omp root semantics grounded {grounded} of {TOTAL}")
        ok = grounded == TOTAL and guards["S1"] and guards["S3"]
        out(f"exit={0 if ok else 1}")
        return 0 if ok else 1
    finally:
        blob.close()


# --------------------------------------------------------------------------------- self-test

SYN_PATTERNS = [
    "{cwd}/.omp/skills",
    "{cwd}/.claude/skills",
    "{cwd}/.agent/skills",
    "{cwd}/.agents/skills",
    "{cwd}/.codex/skills",
    "{cwd}/.opencode/skills",
    "{cwd}/.github/skills",
    "~/.omp/agent/skills",
    "~/.omp/plugins/node_modules/*/skills",
    "~/.agent/skills",
    "~/.agents/skills",
    "~/.omp/agent/managed-skills",
]
SYN_MODULES = [
    "coding-agent/src/discovery/builtin.ts",
    "coding-agent/src/discovery/claude.ts",
    "coding-agent/src/discovery/agents.ts",
    "coding-agent/src/discovery/agents.ts",
    "coding-agent/src/discovery/codex.ts",
    "coding-agent/src/discovery/opencode.ts",
    "coding-agent/src/discovery/helpers.ts",
    "coding-agent/src/discovery/builtin.ts",
    "coding-agent/src/discovery/omp-plugins.ts",
    "coding-agent/src/discovery/agents.ts",
    "coding-agent/src/discovery/agents.ts",
    "coding-agent/src/autolearn/managed-skills.ts",
]
SYN_DOC = "Native OMP configuration from ~/.omp and .omp/"


def syn_reader(i: int) -> str:
    return f'const r{i:02d} = P.join(root{i:02d}, "skills");'


def syn_elf(modules: list[str], readers: list[str], offset_swap: int | None = None) -> str:
    """A synthetic ELF: one `// packages/<module>` header per distinct module, in first-seen
    order, with every reader line of that module after the header."""
    groups: dict[str, list[int]] = {}
    for i, module in enumerate(modules):
        groups.setdefault(module, []).append(i)
    chunks = [SYN_DOC]
    for module, members in groups.items():
        header = f"// packages/{module}\n"
        lines = "".join(readers[i] + "\n" for i in members)
        if offset_swap is not None and offset_swap in members:
            chunks.append(lines)
            chunks.append(header)
        else:
            chunks.append(header)
            chunks.append(lines)
    return "".join(chunks)


def syn_rows(patterns: list[str], modules: list[str], readers: list[str]) -> str:
    lines = [SEMANTICS_HEADER]
    for pattern, module, reader in zip(patterns, modules, readers):
        lines.append("\t".join([pattern, SYN_DOC, module, reader]))
    return "\n".join(lines) + "\n"


def syn_roots(patterns: list[str]) -> str:
    return "\n".join([ROOTS_HEADER] + ["\t".join([p, SYN_DOC]) for p in patterns]) + "\n"


def build_world(root: Path, semantics: str | None, roots: str, elf_text: str) -> tuple[Path, str]:
    """A git fixture repo holding both ledgers and the synthetic ELF; returns (repo, rev)."""
    repo = root / "lane"
    if root.exists():
        shutil.rmtree(root)
    (repo / "verifiers").mkdir(parents=True, exist_ok=True)
    (repo / "verifiers" / ROOTS_LEDGER.split("/")[-1]).write_text(roots, encoding="utf-8")
    if semantics is not None:
        (repo / "verifiers" / SEMANTICS_LEDGER.split("/")[-1]).write_text(semantics, encoding="utf-8")
    (root / "elf.bin").write_text(elf_text, encoding="utf-8")
    for args in (["init", "-q"], ["add", "-A"],
                 ["-c", "user.name=probe", "-c", "user.email=probe@example.invalid",
                  "commit", "-q", "-m", "fixture"]):
        proc = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
        if proc.returncode != 0:
            raise Inconclusive(f"fixture git {args[0]} failed: {proc.stderr.strip()[-160:]}")
    top = subprocess.run(["git", "-C", str(repo), "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if top.returncode != 0 or Path(top.stdout.strip()) != repo:
        raise Inconclusive("fixture repo toplevel is not the fixture dir")
    rev = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                         capture_output=True, text=True).stdout.strip()
    return repo, rev


def self_test(work: Path) -> int:
    failures: list[str] = []
    assertions = 0

    def check(name: str, ok: bool, detail: str = "") -> None:
        nonlocal assertions
        assertions += 1
        if not ok:
            failures.append(f"{name}: {detail}" if detail else name)

    work.mkdir(parents=True, exist_ok=True)
    readers = [syn_reader(i) for i in range(len(SYN_PATTERNS))]
    honest_elf = syn_elf(SYN_MODULES, readers)
    honest_sem = syn_rows(SYN_PATTERNS, SYN_MODULES, readers)
    honest_roots = syn_roots(SYN_PATTERNS)

    def world(tag: str, semantics: str | None, roots: str, elf_text: str,
              chain=FROZEN_CHAIN) -> tuple[list[str], int]:
        root = work / tag
        if root.exists():
            shutil.rmtree(root)
        repo, rev = build_world(root, semantics, roots, elf_text)
        lines: list[str] = []
        try:
            rc = run(repo, rev, root / "elf.bin", None, out=lines.append, chain=chain)
        except Inconclusive as exc:
            lines.append(f"could-not-evaluate: {exc}")
            rc = 2
        return lines, rc

    def last_line(lines: list[str]) -> str:
        body = [l for l in lines if not l.startswith("exit=")]
        return body[-1] if body else ""

    # honest world: 12 grounded rows, S1-S3 PASS, exit 0, the frozen sentence verbatim
    lines, rc = world("honest", honest_sem, honest_roots, honest_elf)
    check("honest exit 0", rc == 0, " | ".join(lines[-3:]))
    check("honest prints the frozen sentence",
          "omp root semantics grounded 12 of 12" in lines, last_line(lines))
    check("honest S3 PASS", "guard S3 pattern-set PASS" in lines)
    check("honest grounds every row", sum(l.startswith("row ") and " GROUND " in l
                                          for l in lines) == 12)

    # w_noledger: no semantics ledger at the revision -> 0 of 12, exit 1 (content verdict)
    lines, rc = world("w_noledger", None, honest_roots, honest_elf)
    check("w_noledger exit 1", rc == 1)
    check("w_noledger 0 of 12", "omp root semantics grounded 0 of 12" in lines, last_line(lines))
    check("w_noledger names the absence", any("absent at the revision" in l for l in lines))

    # w_docquote: a doc/string-table line in reader_quote -> conjunct 2 refuses it
    doc_readers = list(readers)
    doc_readers[8] = SYN_DOC
    lines, rc = world("w_docquote", syn_rows(SYN_PATTERNS, SYN_MODULES, doc_readers),
                      honest_roots, honest_elf)
    check("w_docquote exit 1", rc == 1)
    check("w_docquote 11 of 12", "omp root semantics grounded 11 of 12" in lines, last_line(lines))
    check("w_docquote names the join token",
          any("no ELF line carrying a path-join token" in l for l in lines))

    # w_nomodule: the header `// packages/<module>` is absent from the ELF
    bad_modules = list(SYN_MODULES)
    bad_modules[0] = "coding-agent/src/discovery/nonexistent.ts"
    lines, rc = world("w_nomodule", syn_rows(SYN_PATTERNS, bad_modules, readers),
                      honest_roots, honest_elf)
    check("w_nomodule exit 1", rc == 1)
    check("w_nomodule 11 of 12", "omp root semantics grounded 11 of 12" in lines, last_line(lines))
    check("w_nomodule names the header", any("not located in the omp ELF" in l for l in lines))

    # w_dotdot: a `..` pattern -> conjunct 1 refuses it (both ledgers carry it, so S3 passes)
    dot_patterns = list(SYN_PATTERNS)
    dot_patterns[0] = "{cwd}/../.omp/skills"
    lines, rc = world("w_dotdot", syn_rows(dot_patterns, SYN_MODULES, readers),
                      syn_roots(dot_patterns), honest_elf)
    check("w_dotdot exit 1", rc == 1)
    check("w_dotdot 11 of 12", "omp root semantics grounded 11 of 12" in lines, last_line(lines))
    check("w_dotdot names the segment", any("`..` segment" in l for l in lines))

    # w_star: a wildcard in the first segment -> conjunct 1 refuses it
    star_patterns = list(SYN_PATTERNS)
    star_patterns[0] = "*/skills"
    lines, rc = world("w_star", syn_rows(star_patterns, SYN_MODULES, readers),
                      syn_roots(star_patterns), honest_elf)
    check("w_star exit 1", rc == 1)
    check("w_star 11 of 12", "omp root semantics grounded 11 of 12" in lines, last_line(lines))
    check("w_star names the wildcard", any("wildcard in its first segment" in l for l in lines))

    # w_shrink: an 11-row ledger cannot pass (S3 red, N short)
    lines, rc = world("w_shrink", syn_rows(SYN_PATTERNS[:11], SYN_MODULES[:11], readers[:11]),
                      honest_roots, honest_elf)
    check("w_shrink exit 1", rc == 1)
    check("w_shrink 11 of 12", "omp root semantics grounded 11 of 12" in lines, last_line(lines))
    check("w_shrink S3 FAIL", "guard S3 pattern-set FAIL" in lines)

    # w_bound: a `{cwd}/` row whose expansion walks up to $HOME and above
    lines, rc = world("w_bound", honest_sem, honest_roots, honest_elf, chain=FULL_CHAIN)
    check("w_bound exit 1", rc == 1)
    check("w_bound below 12", "omp root semantics grounded 12 of 12" not in lines)
    check("w_bound names the expansion", any("$HOME or above" in l for l in lines))
    check("w_bound leaves the `~/` rows alone",
          sum(l.startswith("row ") and " GROUND " in l for l in lines) == 5)

    # w_quote_miss: a reader quote that is not in the ELF at all
    miss_readers = list(readers)
    miss_readers[3] = 'const absent = Q.join(nothing, "skills");'
    lines, rc = world("w_quote_miss", syn_rows(SYN_PATTERNS, SYN_MODULES, miss_readers),
                      honest_roots, honest_elf)
    check("w_quote_miss exit 1", rc == 1)
    check("w_quote_miss 11 of 12", "omp root semantics grounded 11 of 12" in lines, last_line(lines))
    check("w_quote_miss names the miss", any("not located in the omp ELF" in l for l in lines))

    # w_offset_order: the module header sits after its reader quote (a module unique to one row)
    swapped = syn_elf(SYN_MODULES, readers, offset_swap=11)
    lines, rc = world("w_offset_order", honest_sem, honest_roots, swapped)
    check("w_offset_order exit 1", rc == 1)
    check("w_offset_order 11 of 12", "omp root semantics grounded 11 of 12" in lines, last_line(lines))
    check("w_offset_order names the order",
          any("before the header's last occurrence" in l for l in lines))

    # a wrong ELF pin is could-not-evaluate, never a content verdict
    repo, rev = build_world(work / "pin", honest_sem, honest_roots, honest_elf)
    try:
        run(repo, rev, work / "pin" / "elf.bin", "0" * 64, out=lambda *_: None)
        check("wrong pin raises", False)
    except Inconclusive:
        check("wrong pin raises", True)

    # the live lane at the frozen base: 0 of 12, exit 1 (skipped when the rev is absent)
    base = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
    has_base = subprocess.run(["git", "-C", str(REPO), "cat-file", "-e", f"{base}^{{commit}}"],
                              capture_output=True).returncode == 0
    if has_base:
        try:
            lines = []
            rc = run(REPO, base, OMP_BINARY, OMP_SHA256, out=lines.append)
        except Inconclusive as exc:
            lines, rc = [f"could-not-evaluate: {exc}"], 2
        check("base exit 1", rc == 1, " | ".join(lines[-2:]))
        check("base 0 of 12", "omp root semantics grounded 0 of 12" in lines, last_line(lines))

    print(f"{len(failures)} failure(s) over {assertions} assertions")
    for failure in failures:
        print("FAIL", failure)
    return 0 if not failures else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--rev", help="commit whose committed ledgers are scored")
    parser.add_argument("--repo", default=str(REPO))
    parser.add_argument("--work", help="scratch dir for --self-test (default: under TMPDIR)")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        work = Path(args.work) if args.work else Path(tempfile.mkdtemp(
            prefix="ors-", dir=os.environ.get("TMPDIR")))
        try:
            return self_test(work)
        finally:
            if not args.work:
                shutil.rmtree(work, ignore_errors=True)
    if not args.rev:
        parser.error("--rev is required")
    try:
        return run(Path(args.repo), args.rev, OMP_BINARY, OMP_SHA256)
    except Inconclusive as exc:
        print(f"could-not-evaluate: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
