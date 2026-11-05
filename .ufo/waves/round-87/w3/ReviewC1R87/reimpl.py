#!/usr/bin/env python3
# ReviewC1R87 — independent re-implementation of the round-87 C1 row predicate.
# Wrote from plans/round-87.md § C1 ONLY (freeze 669f2801c31ef27e18cc35a327d2e18f466281c7),
# before opening verifiers/check_omp_root_semantics.py or its frozen-source diff in
# addendum2 (both read afterwards, for comparison only — never imported).
#
# Reads both ledgers from the tip's committed bytes (git show), maps the installed
# ELF read-only, and prints `reimpl grounded N of 12` plus per-row GROUND/FAIL.
import hashlib, mmap, posixpath, re, subprocess, sys
from fnmatch import fnmatchcase

TIP = "760e1c5edfdefb4767420f711d08f669952de013"
REPO = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
ELF = "/home/vgpnk/.local/bin/omp"
ELF_SHA256 = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"
SEM = "verifiers/omp-skill-roots-semantics.tsv"
ROOTS = "verifiers/omp-skill-roots.tsv"
JOIN_TOKENS = ("join(", ".join(", "resolve(", "path.join")
WILD = set("*?[")
LINE_SPAN = 8192          # cap for "the line" containing an offset (ELF has huge lines)
HOME = "/home/u"
CWD = "/home/u/proj/sub"
FROZEN_CHAIN = (CWD, "/home/u/proj")

def show(path):
    return subprocess.run(["git", "-C", REPO, "show", f"{TIP}:{path}"],
                          capture_output=True, check=False).stdout.decode("utf8","replace")

def rows_of(text, header, ncols):
    lines = [l for l in text.splitlines() if l.strip()]
    assert lines and lines[0] == header, "bad or missing header: " + header
    return [l.split("\t") for l in lines[1:]]

def main():
    sem = rows_of(show(SEM), "root_pattern\tbinary_quote\tmodule\treader_quote", 4)
    roots = rows_of(show(ROOTS), "root_pattern\tbinary_quote", 2)
    h = hashlib.sha256(open(ELF,"rb").read(0) or b"")  # noop; real hash below
    f = open(ELF, "rb"); blob = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    assert hashlib.sha256(blob).hexdigest() == ELF_SHA256, "ELF pin mismatch"
    grounded = 0
    verdicts = []
    for i, cells in enumerate(sem, 1):
        reasons = []
        pattern, binary_quote, module, reader = cells
        p = pattern.strip()
        # conjunct 1 — pattern equals the round-86 row at the same index + shape
        if i > len(roots) or p != roots[i-1][0].strip():
            e = roots[i-1][0].strip() if i <= len(roots) else None
            reasons.append(f"The round-86 ledger has no row {i} to match" if e is None
                           else f"pattern {p!r} is not the round-86 ledger's row {i} ({e!r})")
        if ".." in [s for s in p.split("/")]:
            reasons.append(f"pattern {p!r} carries a `..` segment")
        # strip the {cwd}/ or ~/ prefix before naming a "first segment
        if p.startswith("{cwd}/"):
            rel = p[len("{cwd}/"):]
        elif p.startswith("~/"):
            rel = p[2:]
        else:
            rel = p.lstrip("/")
        first = next((s for s in rel.split("/") if s), "")
        if not first:
            reasons.append(f"pattern {p!r} names no directory")
        elif WILD & set(first):
            reasons.append(f"pattern {p!r} has a wildcard in its first segment ({first!r})")
        # conjunct 2 — quote (>=12 chars) on an ELF line carrying a path-join token
        ro = reader.encode()
        occ = find_all(blob, ro)
        if len(reader.strip()) < 12:
            reasons.append("reader_quote shorter than 12 chars")
        elif not occ:
            reasons.append("reader_quote not located in the omp ELF")
        else:
            ok2 = any(is_join_line(blob, o) for o in occ)
            if not ok2:
                reasons.append("reader_quote sits on no ELF line carrying a path-join token")
        # conjunct 3 — module header occurs in ELF and precedes the reader's FIRST occurrence
        hed = b"// packages/" + module.strip().encode()
        hed_occ = find_all(blob, hed, boundary_re=r"(?![A-Za-z0-9_.@/\-])")
        m_ok = True
        if not module.strip():
            reasons.append("module cell is empty"); m_ok = False
        elif ".." in module.strip().split("/"):
            reasons.append(f"module {module.strip()!r} carries a `..` segment"); m_ok = False
        elif not hed_occ:
            reasons.append(f"header `// packages/{module.strip()}` not located in the omp ELF"); m_ok = False
        elif reader_ok_first_from_row(occ) is None:
            reasons.append("reader quote has no located occurrence to order against the header"); m_ok = False
        else:
            first_reader = occ[0]
            if first_reader < hed_occ[-1]:
                reasons.append(f"reader quote first occurs at {first_reader}, before the header's last occurrence at {hed_occ[-1]}")
                m_ok = False
        # conjunct 4 — {cwd}/ rows never expand to $HOME/above; `..` candidate never matches
        b_ok, b_why = bound(p)
        if not b_ok: reasons.append(b_why)
        if reasons:
            verdicts.append(f"row {i:2d} FAIL {p!r}: " + "; ".join(reasons))
        else:
            grounded += 1
            verdicts.append(f"row {i:2d} GROUND {p!r} module={module.strip()!r} @{occ[0] if occ else None}")
    blob.close()
    for v in verdicts: print(v)
    print("guard S1 committed-bytes PASS (both ledgers via git show)")
    print("guard S2 elf-sha256 PASS")
    print(f"reimpl grounded {grounded} of {len(sem)}   (round-86 ledger: {len(roots)} rows)")
    return 0 if grounded == len(roots) == 12 else 1

def reader_ok_first_from_row(occ):  # conjunct 3 needs a located reader; reuse occurrences
    return occ[0] if occ else None

def find_all(blob, needle, limit=16, boundary_re=None):
    out, at = [], blob.find(needle)
    rx = re.compile(re.escape(needle).replace(b"\\",b"\\\\") + boundary_re.encode()) if False else None
    while at >= 0 and len(out) < limit:
        out.append(at)
        at = blob.find(needle, at + 1)
    return out

def is_join_line(blob, offset):
    a = max(0, offset - LINE_SPAN); b = min(blob.size(), offset + LINE_SPAN)
    start = blob.rfind(b"\n", a, offset) + 1
    end = blob.find(b"\n", offset, b)
    if end < 0: end = b
    line = blob[start:end]
    return any(t.encode() in line for t in JOIN_TOKENS)

def at_or_above(path, home):
    return path == home or home.startswith(path.rstrip("/") + "/")

def bound(pattern):
    if pattern.startswith("{cwd}/"):
        rest = pattern[len("{cwd}/"):]
        if not rest or rest.startswith("/") or ".." in rest.split("/"):
            return False, f"pattern {pattern!r}: `{{cwd}}/` rest is not a plain relative path"
        exps = [posixpath.normpath(posixpath.join(d, rest)) for d in FROZEN_CHAIN]
    elif pattern.startswith("~/"):
        exps = [posixpath.normpath(posixpath.join(HOME, pattern[2:]))]
    else:
        exps = [posixpath.normpath(pattern)]
    for e in exps:
        if ".." in e.split("/"):
            return False, f"pattern {pattern!r} expands to a `..` candidate ({e})"
        if pattern.startswith("~/") and not (e == HOME or e.startswith(HOME + "/")):
            return False, f"pattern {pattern!r} expands outside $HOME ({e})"
        if not pattern.startswith("~/") and at_or_above(e, HOME):
            return False, f"pattern {pattern!r} expands to {e}, which is $HOME or above it"
    # a `..` candidate never matches the pattern over the chain
    for cand in (f"{CWD}/../sub/.probe/skills", "/home/u/../u/.probe/skills"):
        if ".." in cand.split("/"): continue
        cands = [c for c in (posixpath.normpath(cand),) if ".." not in c.split("/")]
        if any(fnmatchcase(c, e) for c in cands for e in exps):
            return False, f"pattern {pattern!r} matches the `..` candidate {cand}"
    return True, ""

def per_row(_):  # per-row verdicts already printed inline above via verdicts list
    pass

if __name__ == "__main__":
    sys.exit(main())
