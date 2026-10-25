import importlib.util, sys
spec = importlib.util.spec_from_file_location("vs", "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_surfaces.py")
vs = importlib.util.module_from_spec(spec); spec.loader.exec_module(vs)
dump = open('/tmp/k72w1-ExecOC4/oc-strings.txt', errors='replace').read()
ids, report = vs.extract_opencode_classes(dump)
for r in report:
    print("%-6s matched=%-5s owns=%s missing=%s" % (r['rule_id'], r['matched'], r['owns'], r['missing']))
print("ids:", sorted(ids))
print("OC-4 rule fn opencode_read_hook_matches ->", vs.opencode_read_hook_matches(dump))
print("OC_READ_TOOL_ENTRY_RE hits:", len(vs.OC_READ_TOOL_ENTRY_RE.findall(dump)))
print("OC_READ_HOOK_ENTRY_RE hits:", len(vs.OC_READ_HOOK_ENTRY_RE.findall(dump)))
print("OC_READ_CALL_RE hits:", len(vs.OC_READ_CALL_RE.findall(dump)))
