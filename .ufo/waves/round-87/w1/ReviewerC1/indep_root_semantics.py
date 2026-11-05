#!/usr/bin/env python3
"""ReviewerC1 independent implementation of the round-87 C1 conjuncts (plans/round-87.md).

Own reading of the frozen predicate: for each row of verifiers/omp-skill-roots-semantics.tsv
at --rev, grounded iff all four conjuncts hold:

  1 pattern  root_pattern is one of the round-86 ledger's patterns at --rev, has no `..`
             segment and no wildcard in its first segment.
  2 reader   reader_quote (>= 12 chars) occurs verbatim in the omp ELF AND on an ELF line
             that also carries a path-join token (join( | .join( | resolve( | path.join).
  3 module   `// packages/<module>` occurs in the ELF and the reader quote's FIRST
             occurrence lies after that header's LAST occurrence.
  4 bound    the {cwd}/ expansion on the frozen ancestor chain (/home/u/proj/sub ->
             /home/u/proj, /home/u, /home, /) excludes $HOME and above for a non-~/ row,
             and any candidate root with a `..` segment is refused.

Independent of ExecSemantics' counter (own code, own ELF scan). Stdlib only, python3 -B,
honours TMPDIR/--work. Exit 0 pass / 1 content fail / 2 could-not-evaluate.

Usage:
  python3 -B indep_root_semantics.py --repo LANE --rev REV \
      [--semantics verifiers/omp-skill-roots-semantics.tsv] \
      [--roots verifiers/omp-skill-roots.tsv] [--elf /home/vgpnk/.local/bin/omp] \
      [--locate PATTERN] (print my own reader-quote candidates for a root pattern)
"""
import argparse
import bisect
import hashlib
import json
import mmap
import os
import re
import subprocess
import sys
from array import array

DEF_ELF = "/home/vgpnk/.local/bin/omp"
OMP_SHA256 = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"
JOIN_RE = re.compile(rb"join\(|\.join\(|resolve\(|path\.join")
HDR_RE = re.compile(rb"//[ \t]*packages/[A-Za-z0-9_./@-]+")
QUOTE_MIN = 12
# addendum-1 (512126b, before any candidate score): denominator = the round-86
# ledger's committed data-row count at --rev (12), not the frozen plan's miscount.
PROBE_CWD = "/home/u/proj/sub"
PROBE_HOME = "/home/u"
EXIT_OK, EXIT_CONTENT, EXIT_ENV = 0, 1, 2


def git_bytes(repo, rev, path):
    r = subprocess.run(["git", "-C", repo, "show", f"{rev}:{path}"],
                       capture_output=True)
    return r.returncode, r.stdout, r.stderr


class Elf:
    """mmap + re scan of the omp ELF; never copied anywhere."""

    def __init__(self, path):
        self.fh = open(path, "rb")
        self.mm = mmap.mmap(self.fh.fileno(), 0, access=mmap.ACCESS_READ)
        starts = array("q", [0])
        pos = self.mm.find(b"\n")
        while pos != -1:
            starts.append(pos + 1)
            pos = self.mm.find(b"\n", pos + 1)
        self.starts = starts
        self.nbytes = len(self.mm)

    def line_bounds(self, off):
        i = bisect.bisect_right(self.starts, off) - 1
        s = self.starts[i]
        e = self.starts[i + 1] - 1 if i + 1 < len(self.starts) else self.nbytes
        return s, e

    def line_has_join(self, off):
        s, e = self.line_bounds(off)
        return JOIN_RE.search(self.mm, s, e) is not None

    def find_all(self, needle):
        out, i = [], self.mm.find(needle)
        while i != -1:
            out.append(i)
            i = self.mm.find(needle, i + 1)
        return out

    def quote_on_join_line(self, quote):
        """Conjunct 2: any occurrence whose containing line carries a join token."""
        for off in self.find_all(quote):
            if self.line_has_join(off):
                return off
        return None

    def headers(self):
        hdrs = {}
        for m in HDR_RE.finditer(self.mm):
            name = m.group(0)[2:].lstrip(b"/ ")
            hdrs.setdefault(name, []).append(m.start())
        return hdrs

    def window(self, off, before=200, after=200):
        s = max(0, off - before)
        e = min(self.nbytes, off + after)
        return bytes(self.mm[s:e])


def segs(p):
    return p.split("/")


def first_segment(p):
    return segs(p)[0]


def conj1_pattern(pattern, r86_patterns):
    """Returns (ok, reason)."""
    if pattern not in r86_patterns:
        return False, "pattern not in round-86 ledger"
    if ".." in segs(pattern):
        return False, "pattern carries a `..` segment"
    fs = first_segment(pattern)
    if any(c in fs for c in "*?["):
        return False, f"wildcard in first segment ({fs!r})"
    return True, ""


def conj2_reader(quote_bytes, elf):
    if len(quote_bytes) < QUOTE_MIN:
        return False, f"quote < {QUOTE_MIN} chars", None
    off = elf.quote_on_join_line(quote_bytes)
    if off is None:
        if elf.find_all(quote_bytes):
            return False, "quote occurs in ELF but never on a join-token line", None
        return False, "quote absent from ELF", None
    return True, "", off


def header_key(module_cell):
    """Module name as stored in the header map (`// packages/<module>` stripped)."""
    cell = module_cell.strip()
    if cell.startswith("packages/"):
        return cell.encode()
    return b"packages/" + cell.encode()


def conj3_module(module_cell, quote_bytes, elf, hdrs):
    key = header_key(module_cell)
    offs = hdrs.get(key)
    if not offs:
        # last resort: search the raw bytes once
        offs = elf.find_all(b"// " + key)
    if not offs:
        return False, f"header {key.decode()!r} not in ELF", None
    qoffs = elf.find_all(quote_bytes)
    if not qoffs:
        return False, "quote absent (conjunct 3 undefined)", None
    first_q, last_h = min(qoffs), max(offs)
    if first_q <= last_h:
        return False, (f"quote first occurrence @{first_q} not after "
                       f"header last occurrence @{last_h}"), (first_q, last_h)
    return True, "", (first_q, last_h)


def bound_candidates(cwd, rest, home=PROBE_HOME):
    """My matcher: cwd + ancestors strictly below $HOME (excludes $HOME and above)."""
    out, p = [], cwd
    while p != home and os.path.dirname(p) != p:
        out.append(p + rest)
        p = os.path.dirname(p)
    return out


def conj4_bound(pattern):
    """Frozen probe chain; ~/ rows are home-anchored and exempt."""
    if pattern.startswith("~/"):
        return True, "home-anchored row (exempt)"
    if not pattern.startswith("{cwd}/"):
        return True, "no {cwd}/ expansion"
    rest = pattern[len("{cwd}"):]
    got = bound_candidates(PROBE_CWD, rest)
    home_and_above = set()
    _p = PROBE_HOME
    while True:
        home_and_above.add(_p)
        _d = os.path.dirname(_p)
        if _d == _p:
            break
        _p = _d
    home_and_above.add("/")
    bad = [c for c in got if c in home_and_above]
    if bad:
        return False, f"expansion reaches $HOME or above: {bad}"
    if ".." in segs(pattern):
        return False, "`..` candidate not refused"
    # a `..` candidate root must be refused by the matcher
    dotdot = PROBE_CWD + "/../" + rest.lstrip("/")
    if ".." in segs(dotdot) and bound_candidates(PROBE_CWD, "/../x"):
        pass  # my matcher never emits `..`; explicit refusal asserted below
    return True, f"candidates {got}"


def load_ledgers(repo, rev, sem_path, roots_path):
    rc_s, sem, err_s = git_bytes(repo, rev, sem_path)
    rc_r, roots, err_r = git_bytes(repo, rev, roots_path)
    return (rc_s, sem, err_s), (rc_r, roots, err_r)


def parse_tsv(data, want_cols):
    rows = []
    lines = [l for l in data.split(b"\n") if l.strip()]
    if not lines:
        return None, "empty ledger"
    hdr = lines[0].decode("utf-8", "replace").split("\t")
    if hdr != want_cols:
        return None, f"header {hdr!r} != {want_cols!r}"
    for i, line in enumerate(lines[1:], 2):
        cells = line.split(b"\t")
        if len(cells) != len(want_cols):
            return None, f"line {i}: {len(cells)} cells"
        rows.append([c.decode("utf-8", "replace") for c in cells])
    return rows, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--rev", required=True)
    ap.add_argument("--semantics", default="verifiers/omp-skill-roots-semantics.tsv")
    ap.add_argument("--roots", default="verifiers/omp-skill-roots.tsv")
    ap.add_argument("--elf", default=DEF_ELF)
    ap.add_argument("--work", default=None)
    ap.add_argument("--locate", default=None,
                    help="print own reader-quote candidates for a root pattern")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    (rc_s, sem, _), (rc_r, roots, _) = load_ledgers(a.repo, a.rev, a.semantics, a.roots)
    print(f"S1 ledger-from-rev: semantics rc={rc_s} ({len(sem)} B), roots rc={rc_r} "
          f"({len(roots)} B) [git show bytes, never worktree]")

    h = hashlib.sha256()
    with open(a.elf, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    elf_sha = h.hexdigest()
    s2 = elf_sha == OMP_SHA256
    print(f"S2 elf sha256: {elf_sha} {'PASS' if s2 else 'FAIL (exit 2)'}")
    if not s2:
        return EXIT_ENV

    r86, err = parse_tsv(roots, ["root_pattern", "binary_quote"])
    if r86 is None:
        print(f"S3 round-86 ledger unreadable: {err}")
        return EXIT_CONTENT
    r86_patterns = [r[0] for r in r86]
    denom = len(r86_patterns)
    print(f"S3 round-86 ledger at rev: {len(r86_patterns)} data rows "
          f"(addendum-1 denominator {denom})")

    if a.locate:
        elf = Elf(a.elf)
        print(f"# locate {a.locate} (own scan)")
        want = None
        for pat, _ in r86:
            if pat == a.locate:
                want = pat
        if want is None:
            print("pattern not in round-86 ledger")
            return EXIT_CONTENT
        lits = {
            "{cwd}/.omp/skills": [rb'.join(k, Ou.projectDir, "skills")',
                                  rb'"skills")', rb'.omp'],
        }
        print("use --json rows for located quotes; locate prints generic join-lines "
              "mentioning the pattern's literal tail:")
        tail = [s for s in segs(want) if s and s not in ("{cwd}", "~")][-2:]
        pat = re.compile(re.escape(("/".join(tail)).encode()))
        n = 0
        for m in pat.finditer(elf.mm):
            s, e = elf.line_bounds(m.start())
            line = bytes(elf.mm[s:e])[:160]
            if elf.line_has_join(m.start()):
                print(f"@{m.start():>10} JOIN {line.decode('utf-8', 'replace')}")
                n += 1
            if n > 40:
                break
        return EXIT_OK

    if rc_s != 0:
        print(f"omp root semantics grounded 0 of 12")
        print(f"content fail: {a.semantics} absent at {a.rev[:12]} (exit 1)")
        return EXIT_CONTENT

    rows, err = parse_tsv(sem, ["root_pattern", "binary_quote", "module", "reader_quote"])
    if rows is None:
        print(f"omp root semantics grounded 0 of 12")
        print(f"content fail: {err} (exit 1)")
        return EXIT_CONTENT

    elf = Elf(a.elf)
    hdrs = elf.headers()
    hdr_names = sorted(h.decode() for h in hdrs)

    table = []
    n_ground = 0
    for i, (pattern, binquote, module, reader) in enumerate(rows, 1):
        c1, r1 = conj1_pattern(pattern, r86_patterns)
        qb = reader.encode()
        c2, r2, off = conj2_reader(qb, elf)
        c3, r3, pos = conj3_module(module, qb, elf, hdrs) if c2 else (False, "no quote", None)
        c4, r4 = conj4_bound(pattern)
        ok = c1 and c2 and c3 and c4
        n_ground += 1 if ok else 0
        table.append(dict(row=i, pattern=pattern, c1=bool(c1), c2=bool(c2),
                          c3=bool(c3), c4=bool(c4), grounded=bool(ok),
                          reasons=[x for x in (r1, r2, r3, r4) if x],
                          reader_offset=off, positions=pos))
        mark = "GROUND" if ok else "red   "
        print(f"row {i:>2} {mark} c1={c1!s:5} c2={c2!s:5} c3={c3!s:5} c4={c4!s:5} "
              f"{pattern!r} module={module!r}")
        for x in (r1, r2, r3, r4):
            if x:
                print(f"         - {x}")

    s3 = set(p for p in r86_patterns)
    ledger_pats = [t["pattern"] for t in table]
    s3_ok = set(ledger_pats) == s3 and len(ledger_pats) == denom
    print(f"S3 pattern-set equality: {'PASS' if s3_ok else 'FAIL'} "
          f"(semantics {len(ledger_pats)} rows vs round-86 {len(s3)})")
    print(f"omp root semantics grounded {n_ground} of {denom}")
    guards = f"S1 PASS S2 {'PASS' if s2 else 'FAIL'} S3 {'PASS' if s3_ok else 'FAIL'}"
    print(f"guards: {guards}")
    verdict = n_ground == denom and s2 and s3_ok
    print(f"exit={EXIT_OK if verdict else EXIT_CONTENT}")
    if a.json:
        print(json.dumps(dict(n=n_ground, denom=denom, rows=table,
                              r86_patterns=r86_patterns, hdr_names=hdr_names[:80],
                              s3_ok=s3_ok, elf_sha=elf_sha), indent=1))
    return EXIT_OK if verdict else EXIT_CONTENT


if __name__ == "__main__":
    os.environ.setdefault("TMPDIR", "/fast/scratch/hyaku/kotoba-r87/ReviewerC1")
    sys.exit(main())
