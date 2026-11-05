import mmap, re, sys, csv
ELF="/home/vgpnk/.local/bin/omp"
LINE_SPAN=8192
JOIN=("join(", ".join(", "resolve(", "path.join")
f=open(ELF,"rb"); blob=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
def counter_line(off):
    start=blob.rfind(b"\n", max(0,off-LINE_SPAN), off)
    start=0 if start<0 else start+1
    end=blob.find(b"\n", off, off+LINE_SPAN)
    end=blob.size() if end<0 else end
    return start,end
def exact_line(off):
    s=blob.rfind(b"\n",0,off); s=0 if s<0 else s+1
    e=blob.find(b"\n",off); e=blob.size() if e<0 else e
    return s,e
def occ(needle, limit=10**9):
    out=[]; at=blob.find(needle)
    while at>=0 and len(out)<limit:
        out.append(at); at=blob.find(needle,at+1)
    return out
def report(label, q):
    raw=q.encode()
    offs=occ(raw)
    print(f"== {label!r} len={len(q)} occurrences={len(offs)}")
    for o in offs[:8]:
        cs,ce=counter_line(o); es,ee=exact_line(o)
        cl=blob[cs:ce]; el=blob[es:ee]
        cj=[t for t in JOIN if t.encode() in cl]
        ej=[t for t in JOIN if t.encode() in el]
        print(f"  @{o}: counter_line_len={ce-cs} exact_line_len={ee-es} "
              f"window_newline_left={'Y' if blob.rfind(b'\\n',max(0,o-LINE_SPAN),o)>=0 else 'N'} "
              f"window_newline_right={'Y' if blob.find(b'\\n',o,o+LINE_SPAN)>=0 else 'N'} "
              f"join_in_counter_line={cj} join_in_exact_line={ej}")
    return offs
quotes=[]
with open(sys.argv[1]) as fh:
    rd=csv.reader(fh, delimiter="\t")
    next(rd)
    for row in rd:
        quotes.append((row[0], row[3]))
for pat, rq in quotes:
    report("reader:"+pat, rq)
for doc in ["Native OMP configuration from ~/.omp and .omp/", 'var Gh = ".omp";']:
    report("doc:"+doc, doc)
