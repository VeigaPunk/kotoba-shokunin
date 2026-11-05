#!/usr/bin/env python3
"""Read-only probe: for each C1 row, locate the reader_quote in the omp ELF and print
(a) the nearest preceding `// packages/<x>` header of ANY module, (b) the row module's own
last preceding header, (c) the nearest following header. Tests whether conjunct 3's
"after the last header" ordering coincides with real chunk membership."""
import mmap, re, sys

ELF = "/home/vgpnk/.local/bin/omp"
LEDGER = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/omp-skill-roots-semantics.tsv"

rows = []
for line in open(LEDGER, encoding="utf-8").read().splitlines()[1:]:
    if not line.strip():
        continue
    pat, _bq, mod, quote = line.split("\t")
    rows.append((pat, mod, quote))

H = re.compile(rb"//[ \t]*packages/([A-Za-z0-9_./@-]+)")
with open(ELF, "rb") as f:
    blob = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    headers = [(m.start(), m.group(1).decode()) for m in H.finditer(blob)]
    print(f"headers in ELF: {len(headers)}; first={headers[0]}; last={headers[-1]}")
    hoff = [o for o, _ in headers]

    import bisect
    for i, (pat, mod, quote) in enumerate(rows, 1):
        q = quote.encode()
        offs, at = [], blob.find(q)
        while at >= 0 and len(offs) < 6:
            offs.append(at)
            at = blob.find(q, at + 1)
        print(f"\nrow {i:2d} {pat}")
        print(f"  module={mod}  quote={quote!r}")
        print(f"  occurrences={offs}")
        if not offs:
            continue
        first = offs[0]
        j = bisect.bisect_left(hoff, first) - 1        # nearest preceding header of any module
        k = bisect.bisect_left(hoff, first)            # nearest following header
        prev_mod = headers[j][1] if j >= 0 else "<none>"
        next_mod = headers[k][1] if k < len(headers) else "<none>"
        own = [o for o, m in headers if m == mod and o < first]
        own_last = own[-1] if own else None
        print(f"  nearest preceding header (any)  @{hoff[j] if j>=0 else -1} {prev_mod}")
        print(f"  nearest following header (any)  @{hoff[k] if k<len(headers) else -1} {next_mod}")
        print(f"  own module last header before   @{own_last}")
        print(f"  VERDICT chunk-header==module: {prev_mod == mod}")
    blob.close()
