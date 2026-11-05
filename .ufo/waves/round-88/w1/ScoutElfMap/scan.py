#!/usr/bin/env python3
"""Read-only ELF scan for ScoutElfMap (round-88 w1)."""
import mmap, re, sys, hashlib

ELF = "/home/vgpnk/.local/bin/omp"
PIN = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"
LINE_SPAN = 8192
JOIN_TOKENS = (b"join(", b".join(", b"resolve(", b"path.join")

LEDGER = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/omp-skill-roots-semantics.tsv"

def elf_line(blob, offset, span=LINE_SPAN):
    start = blob.rfind(b"\n", max(0, offset - span), offset)
    start = 0 if start < 0 else start + 1
    end = blob.find(b"\n", offset, offset + span)
    end = blob.size() if end < 0 else end
    return blob[start:end]

def occ(blob, needle, limit=64):
    out, at = [], blob.find(needle)
    while at >= 0 and len(out) < limit:
        out.append(at)
        at = blob.find(needle, at + 1)
    return out

def module_offsets(blob, module):
    header = b"// packages/" + module.encode()
    pat = re.compile(re.escape(header) + rb"(?![A-Za-z0-9_.@/-])")
    return [m.start() for m in pat.finditer(blob)]

def has_join(line):
    return any(t in line for t in JOIN_TOKENS)

h = open(ELF, "rb")
blob = mmap.mmap(h.fileno(), 0, access=mmap.ACCESS_READ)
digest = hashlib.sha256(blob).hexdigest()
print("ELF sha256:", digest, "PIN-MATCH" if digest == PIN else "PIN-MISMATCH-STOP")
if digest != PIN:
    sys.exit(2)
print("ELF size:", blob.size())

rows = []
with open(LEDGER, "r", encoding="utf-8") as fh:
    lines = [l.rstrip("\n") for l in fh if l.strip()]
header = lines[0]
assert header == "root_pattern\tbinary_quote\tmodule\treader_quote", header
for l in lines[1:]:
    rows.append(l.split("\t"))
print("ledger rows:", len(rows))

def clean(b):
    try:
        s = b.decode("utf-8")
    except UnicodeDecodeError:
        s = repr(b)
    return s

for i, (pat, bq, mod, rq) in enumerate(rows, 1):
    print("=" * 100)
    print(f"ROW {i}: pattern={pat!r} module={mod!r}")
    mo = module_offsets(blob, mod)
    print(f"  module_header_offsets({mod}): {mo}")
    ro = occ(blob, rq.encode())
    print(f"  reader_quote_offsets: {ro}")
    bo = occ(blob, bq.encode())
    print(f"  binary_quote_offsets: {bo[:6]}{' ...' if len(bo) > 6 else ''}")
    # reader occurrences with join token on their line
    for o in ro:
        line = elf_line(blob, o)
        print(f"    reader@{o} join={has_join(line)} line={clean(line)[:400]!r}")
    # nearest join-token line to reader first occurrence
    if ro:
        anchor = ro[0]
        # scan lines around: find all newline-delimited lines in a window
        lo = max(0, anchor - 200000)
        hi = min(blob.size(), anchor + 200000)
        window = blob[lo:hi]
        best = None
        pos = 0
        while True:
            nl = window.find(b"\n", pos)
            if nl < 0:
                break
            line = window[pos:nl]
            abs_start = lo + pos
            abs_end = lo + nl
            if has_join(line) and abs_start <= anchor <= abs_end + 1:
                pass
            pos = nl + 1
        # simpler: enumerate lines in window and pick join lines nearest to anchor
        lines_w = []
        pos = 0
        for m in re.finditer(rb"[^\n]*", window):
            seg = m.group(0)
            abs_start = lo + m.start()
            if has_join(seg):
                lines_w.append((abs(abs_start - anchor), abs_start, seg))
        lines_w.sort()
        print(f"  nearest join lines to reader@{anchor}:")
        for d, s, seg in lines_w[:6]:
            print(f"    d={d} @{s} {clean(seg)[:300]!r}")
    if bo:
        for o in bo[:4]:
            print(f"    binary@{o} line={clean(elf_line(blob, o))[:300]!r}")
