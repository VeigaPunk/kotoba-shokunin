"""OC-1 re-derivation probe: real witness vs decoys, on fetched bytes only.

Usage: python3 oc1_probe.py <scratch verify_surfaces.py> <oc dump>
"""
import importlib.util
import sys

mod_path, dump_path = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("vs_scratch", mod_path)
vs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vs)

dump = open(dump_path, encoding="utf-8", errors="replace").read()
lines = dump.split("\n")


def oc1(text: str) -> dict:
    row = [r for r in vs.extract_opencode_classes(text)[1] if r["rule_id"] == "OC-1"][0]
    return row


print("== real dump: %s ==" % dump_path)
walk = vs.OC_LOADER_SOURCE_RE.search(dump)
print("OC_LOADER_SOURCE_RE span:", walk.span() if walk else None)
region = dump[max(0, walk.start() - vs.OC_LOADER_REGION):walk.end()]
print("config-join names in region:", sorted(set(vs.OC_LOADER_CONFIG_JOIN_RE.findall(region))))
print("derived target names:", sorted(set(vs.OC_MD_NAME_RE.findall(walk.group("targets")))))
row = oc1(dump)
print("OC-1 row:", {k: row[k] for k in ("rule_id", "owns", "matched")})

print("\n== decoy A: ReadTool default name, dump line 708708 (same literal, no loader role) ==")
decoy_a = lines[708707]
i = decoy_a.find('LF="AGENTS.md"')
print("bytes at col %d: %r" % (i, decoy_a[i - 20:i + 30]))
row = oc1(decoy_a)
print("OC-1 row:", {k: row[k] for k in ("owns", "matched")})

print("\n== decoy B: same tokens, bare walk with no loader wrapper ==")
decoy_b = ('function q(){return l.up({targets:["AGENTS.md"],start:T,stop:V,type:"file"})}'
           ';D=l.resolve(j1(r.config,"AGENTS.md"))')
print("bytes:", decoy_b)
row = oc1(decoy_b)
print("OC-1 row:", {k: row[k] for k in ("owns", "matched")})

print("\n== decoy C: same tokens under a different plugin wrapper ==")
decoy_c = ('c("OtherPlugin.projectSource")(function*(){if(!C)return[];let we=yield*Q('
           'yield*l.up({targets:["AGENTS.md"],start:T,stop:V,type:"file"}),l.resolve)});'
           'D=l.resolve(j1(r.config,"AGENTS.md"))')
print("bytes:", decoy_c)
row = oc1(decoy_c)
print("OC-1 row:", {k: row[k] for k in ("owns", "matched")})

print("\n== growth: real loader region with a second name planted ==")
grown = region.replace('targets:["AGENTS.md"]', 'targets:["AGENTS.md","CLAUDE.md"]')
assert grown != region
row = oc1(grown)
print("OC-1 row:", {k: row[k] for k in ("owns", "matched")})
print("planted name surfaces:", "opencode:instructions/CLAUDE.md" in row["owns"])
