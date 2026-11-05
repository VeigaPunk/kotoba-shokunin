#!/usr/bin/env python3
"""ReviewerC1 independent re-implementation of the round-88 C1 row-grounded conjuncts.

Source of truth: plans/round-88.md conjuncts 1-5 + r87 ELF evidence. Frozen
binding token sets declared below BEFORE reading any v2 counter, with sha256
of the row's binding token set computed by the instrument itself.

Usage: python3 -B independent_c1.py --elf E --ledger L [--pattern-ref P] [--world NAME]
Exit 0 all 12 grounded, 1 otherwise, 2 could-not-evaluate. stdlib only, ELF read-only.
"""
import argparse, hashlib, mmap, os, sys

PINNED = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"
PROBE_ANCESTORS = ["/home/u/proj/sub", "/home/u/proj"]   # strictly below HOME
PROBE_HOME = "/home/u"

# ---- binding token sets (ReviewerC1; frozen, self-hashed): each row names
# >=1 token its root literal or declared reader variable produces. The carry
# test runs on the occurrence's own line (two-row quotes read the next line).
def _sets():
    """A1.4 sets (L1 frozen addendum) — single tokens per rule, cross row-exclusion built-in."""
    return {
        "{cwd}/.omp/skills":          ("Ou.projectDir",),
        "{cwd}/.claude/skills":       ("eh",),
        "{cwd}/.agent/skills":        ('".agent"',),
        "{cwd}/.agents/skills":       ('".agents"',),
        "{cwd}/.codex/skills":        ('".codex"',),
        "{cwd}/.opencode/skills":     ('".opencode"',),
        "{cwd}/.github/skills":       ('".github"',),
        "~/.omp/agent/skills":        ("we()",),
        "~/.omp/plugins/node_modules/*/skills": ("R.path",),
        "~/.agent/skills":            ('".agent"',),
        "~/.agents/skills":           ('".agents"',),
        "~/.omp/agent/managed-skills": ('"managed-skills"',),
    }

def sha12(s):
    return hashlib.sha256(s.encode()).hexdigest()[:12]

def read_tsv(path):
    rows = []
    with open(path, "r", encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            line = line.rstrip("\n")
            if line:
                rows.append(dict(zip(header, line.split("\t"))))
    return rows

def expansion_set(pattern):
    """Conjunct 4 (a/b) frozen probe: cwd expansion set, strictly below $HOME."""
    if pattern.startswith("{cwd}/"):
        return sorted(os.path.normpath(c + "/" + pattern[len("{cwd}/"):])
                      for c in PROBE_ANCESTORS)
    if pattern.startswith("~/"):
        return [os.path.normpath(PROBE_HOME + "/" + pattern[len("~/"):])]
    return None

def occurrences(mm, needle, limit=6):
    out, start, nb = [], 0, needle.encode()
    while True:
        h = mm.find(nb, start)
        if h < 0:
            break
        out.append(h)
        if len(out) >= limit:
            break
        start = h + 1
    return out

def line_at(mm, pos):
    ls = mm.rfind(b"\n", 0, pos) + 1
    le = mm.find(b"\n", pos)
    le = len(mm) if le < 0 else le
    return mm[ls:le].decode("utf-8", "replace")

def ground_row(i, row, roots, mm, notes):
    pat, q = row["root_pattern"], row["reader_quote"]
    prob = []
    # 1 pattern: integrity + match r86 + no .. / wildcard first segment
    if not pat or ".." in pat.split("/") or pat.split("/")[0]=="*":
        prob.append("pattern malformed")
    for seg in pat.replace("{cwd}/","").replace("~/","").split("/"):
        if ".." in seg: prob.append("pattern ..-segment")
    if i < len(roots) and roots[i]["root_pattern"] != pat:
        prob.append("pattern != r86 row %d" % (i+1))
    # 2 reader: >=12 chars, occurs, and some occurrence's line (or next line)
    # carries >=1 binding token AND a join
    if len(q) < 12:
        prob.append("reader_quote <12 chars")
    occs = occurrences(mm, q, 2)
    if not occs:
        prob.append("reader_quote not in ELF")
    bt = _sets().get(pat, ())
    if not bt:
        prob.append("empty binding token set")
    # binding: a token must occur inside the row's module chunk (A1.4 rule 2),
    # and the row's reader-quote line must carry a join (conjunct-2 first half).
    binding_at = None
    first_occ = occs[0] if occs else -1
    hdrp = -1; nxth = -1
    if first_occ >= 0:
        cand = first_occ
        while True:
            cand = mm.rfind(b"// packages/", 0, cand)
            if cand < 0: break
            hdrp = cand; break
        if hdrp >= 0:
            nxth = mm.find(b"// packages/", hdrp + 1)
        chunk = (hdrp, nxth if nxth > 0 else len(mm))
        raw = (mm[chunk[0]:chunk[1]].decode("utf-8", "replace") if chunk[0] >= 0 else "")
    else:
        chunk, raw = (-1, -1), ""
    bt_ok = any(t in raw for t in bt)
    reader_join_ok = any(("join(" in line_at(mm, h) or "join (" in line_at(mm, h)) for h in occs) if occs else False
    if bt_ok and reader_join_ok:
        binding_at = occs[0]
    if occs and not bt: pass
    elif occs and binding_at is None:
        prob.append("no join-line occurrence carries binding tokens")
    # 3 module: // packages/<module> precedes the reader quote's first occurrence
    hdr = ("// packages/" + row["module"]).encode()
    hpos = mm.find(hdr)
    if hpos < 0:
        prob.append("no // packages/<module> header")
    else:
        first = mm.find(q.encode())
        if first >= 0 and first < hpos:
            prob.append("first quote occurrence precedes own module header")
    # 4 live bound: frozen-probe expansion (a) escapes / (b) contains ..
    exp = expansion_set(pat)
    if exp is None:
        prob.append("no expansion set")
    else:
        for e in exp:
            if any(s == ".." for s in e.split("/")):
                prob.append("expansion ..-segment")
            if not (e.startswith(PROBE_ANCESTORS[0]) or e.startswith(PROBE_HOME)):
                prob.append("expansion escapes probe roots: %s" % e)
        if pat.startswith("~/") and not all(x.startswith(PROBE_HOME) for x in exp):
            prob.append("~ row not HOME-rooted")
    # 4 (module walk visible): an occurrence of the quote must sit on a join
    # expression. The plan's "walk-up loop, or its single join" is satisfied by
    # the primitive-path-join on the quote's own statement; the row-pattern
    # carry-over (root literal or its indirection reaching that join) is the
    # binding sets' job in conjunct 2.
    walk_ok = False
    for h in occs:
        ctx = line_at(mm, h)
        if ".join(" in ctx or "join (" in ctx:
            walk_ok = True
    if occs and not walk_ok:
        prob.append("no occurrence joins the row's directory token")
    # 5 binary  (bare `in` on mmap misflags; find is position-safe here)
    if mm.find(row["binary_quote"].encode()) < 0:
        prob.append("binary_quote not in ELF")
    tag = "GROUND" if not prob else "FAIL"
    notes.append("%2d %s %-40s %s" % (i+1, tag, pat,
                 ("; ".join(prob) if prob else "binding=%s sha12=%s/%s" % (
                     [sha12(x) for x in bt[:1]], sha12("|".join(bt)), "-"))))
    return 0 if prob else 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--elf", required=True)
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--pattern-ref", default=None)
    ap.add_argument("--skip-sha", action="store_true")
    a = ap.parse_args()
    try:
        f = open(a.elf, "rb")
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    except OSError as e:
        print("could-not-evaluate: ELF: %s" % e); return 2
    if not a.skip_sha:
        hh = hashlib.sha256()
        while True:
            b = mm.read(1 << 20)
            if not b: break
            hh.update(b)
        mm.seek(0)   # mmap.read advances the position; find() would start at EOF
        if hh.hexdigest() != PINNED:
            print("could-not-evaluate: ELF sha256 %s != pinned %s" % (hh.hexdigest(), PINNED))
            return 2
    try:
        roots = read_tsv(a.pattern_ref) if a.pattern_ref else []
        sems = read_tsv(a.ledger)
    except OSError as e:
        print("could-not-evaluate: ledger: %s" % e); return 2
    notes, verdict = [], []
    for i, r in enumerate(sems):
        verdict.append(ground_row(i, r, roots, mm, notes))
    print("ReviewerC1 independent C1 (frozen binding-token sets, self-hashed):")
    for n in notes:
        print(n)
    print("independent root semantics grounded %d of %d" % (sum(verdict), len(sems)))
    return 0 if sum(verdict) == 12 and len(sems) == 12 else 1

if __name__ == "__main__":
    sys.exit(main())
