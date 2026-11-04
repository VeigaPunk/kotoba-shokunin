import json, importlib.util, pathlib, re, sys
REPO = pathlib.Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
spec = importlib.util.spec_from_file_location("vs", REPO/"verifiers/verify_surfaces.py")
vs = importlib.util.module_from_spec(spec); spec.loader.exec_module(vs)

S = pathlib.Path("/fast/scratch/hyaku/kotoba-r85/ScoutSubstrate")
omp_dump = (S/"omp-1815.strings").read_text(errors="replace")
oc_dump  = (S/"opencode.strings").read_text(errors="replace")
dumps = {"omp": omp_dump, "opencode": oc_dump}

base = json.loads((REPO/"verifiers/surfaces-baseline.json").read_text())
entries = vs.load_baseline(REPO/"verifiers/surfaces-baseline.json")
removals = json.loads((REPO/"verifiers/census-removals.json").read_text())

# excused classes per removal rules
excused, rprob = vs.removal_problems(removals.get("removed", []), oc_dump)
print("=== removal_problems (excused set) ===")
print("excused:", sorted(excused))
print("problems:", rprob)
print()

declared_omp = {(e["group"], e["file"]) for e in entries
                if e["harness"]=="omp" and e["context_kind"]=="loader-group"}
extracted = {"omp": vs.extract_classes(omp_dump, "omp", declared_omp),
             "opencode": vs.extract_classes(oc_dump, "opencode", None)}
print("=== extracted omp loader-group (group,file) pairs:", len(extracted["omp"]))
for p in sorted(extracted["omp"]): print("   ", p)
print("=== extracted opencode pairs:", len(extracted["opencode"]))
for p in sorted(extracted["opencode"]): print("   ", p)
print()

print("=== per-baseline-id literal resolution ===")
print("%-8s %-42s %-10s %-14s %s" % ("harness","class_id","kind","literal_present","note"))
absent=[]
for e in entries:
    lit = e["literal"]; h=e["harness"]; kind=e["context_kind"]
    present = lit in dumps[h]
    note=""
    if kind in vs.LOADER_KINDS:
        if e["class_id"] in excused:
            note="EXCUSED (removal ledger)"
        elif not present:
            note="ABSENT from %s dump" % h
            absent.append(e["class_id"])
        elif kind=="loader-group":
            key=(e["group"], e["file"])
            if key not in extracted[h]:
                note="literal present but NO call shape for %s" % (key,)
                absent.append(e["class_id"]+" (shape)")
    elif kind in ("prompt-text","template-list","doc"):
        note="not loader-kind; %s" % ("present" if present else "absent")
    else:
        note="kind=%s" % kind
    print("%-8s %-42s %-10s %-14s %s" % (h, e["class_id"], kind, present, note))
print()
print("=== baseline literals that do NOT occur in their harness dump (loader-kind, unexcused) ===")
print(json.dumps(absent, indent=1))
print()

print("=== census-removals: declared-gone classes vs live opencode dump ===")
for r in removals["removed"]:
    lit=r["literal"]
    hits=[m.start() for m in re.finditer(re.escape(lit), oc_dump)]
    anchors={}
    for a in r["absent_anchors"]:
        ms=[m.start() for m in re.finditer(a, oc_dump)]
        anchors[a]=len(ms)
    print("  class_id=%s literal=%r literal_hits=%d anchor_hits=%s" % (r["class_id"], lit, len(hits), anchors))
print()
print("=== census-removals measured_against vs live ===")
ma=removals["measured_against"]
import hashlib
h=hashlib.sha256((S/"opencode.strings").read_bytes()).hexdigest()
print("  recorded dump_sha256:", ma["dump_sha256"])
print("  live opencode dump sha256:", h, "MATCH" if h==ma["dump_sha256"] else "DRIFT")
p=pathlib.Path(ma["opencode_binary"])
print("  recorded opencode_binary_sha256:", ma["opencode_binary_sha256"])
print("  live sha256:", hashlib.sha256(p.read_bytes()).hexdigest())
