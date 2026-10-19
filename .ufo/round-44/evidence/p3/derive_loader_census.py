import hashlib
import json
import pathlib
import re
import subprocess
import sys
from datetime import datetime, timezone

repo = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(repo / "verifiers"))
import verify_surfaces as surfaces

binary = pathlib.Path("/home/vgpnk/.local/bin/omp")
binary_bytes = binary.read_bytes()
stat = binary.stat()
seconds, nanos = divmod(stat.st_mtime_ns, 1_000_000_000)
local_time = datetime.fromtimestamp(seconds, timezone.utc).astimezone()
offset = local_time.strftime("%z")
offset = offset[:3] + ":" + offset[3:]
mtime_iso = "%s.%09d%s" % (local_time.strftime("%Y-%m-%dT%H:%M:%S"), nanos, offset)
strings = subprocess.run(["strings", "-n", "4", str(binary)], capture_output=True, check=True, timeout=600)
dump = strings.stdout.decode("utf-8", "replace")
new_pattern = re.compile(
    r'(?<![A-Za-z0-9_$])(?:Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo)\(\s*[^\s,()]+\s*,\s*'
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)
constants = surfaces.constant_table(dump)
calls = []
for match in new_pattern.finditer(dump):
    callee = match.group(0).split("(", 1)[0]
    quoted, ident, filename = match.groups()
    group = quoted if quoted else constants.get(ident, "<unresolved-var:%s>" % ident)
    binding = None
    if ident and ident in constants:
        binding_pattern = re.compile(
            r"(?<![A-Za-z0-9_$.])" + re.escape(ident) + r'\s*=\s*"([^"\\\n]{1,80})"'
        )
        binding_match = binding_pattern.search(dump)
        binding = (ident + ' = "' + binding_match.group(1) + '"') if binding_match else None
    calls.append({"callee": callee, "group": group, "file": filename,
                  "call": match.group(0), "group_binding": binding})

class_ids = sorted({"omp:%s/%s" % (call["group"], call["file"]) for call in calls})
expected_descriptions = {
    "omp:agents-md/AGENTS.md": "Standalone AGENTS.md files (Codex/Gemini style)",
    "omp:claude-md/CLAUDE.md": "Standalone CLAUDE.md files (Claude Code style)",
    "omp:opencode/AGENTS.md": "Load AGENTS.md from ~/.config/opencode/",
    "omp:gemini/GEMINI.md": "Load GEMINI.md context files",
    "omp:gemini/system.md": "Load system.md custom system prompt files",
    "omp:gemini/SYSTEM_TEMPLATE.md": "Custom system prompt files (SYSTEM.md, SYSTEM_TEMPLATE.md) that modify agent behavior",
    "omp:github/copilot-instructions.md": "Load copilot-instructions.md from .github/",
    "omp:windsurf/memories/global_rules.md": "Load rules from Windsurf",
}
lines = dump.splitlines()
descriptions = {}
for class_id, needle in expected_descriptions.items():
    found = [line.strip() for line in lines if "description:" in line and needle in line]
    descriptions[class_id] = {"needle": needle, "matches": found[:3], "present": bool(found)}
entries = surfaces.load_baseline(repo / "verifiers/surfaces-baseline.json")
baseline_classes = sorted(
    "omp:%s/%s" % (entry["group"], entry["file"])
    for entry in entries
    if entry["harness"] == "omp" and entry["context_kind"] == "loader-group"
)
version = subprocess.run([str(binary), "--version"], capture_output=True, text=True, check=True).stdout.strip()
head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
tree = subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
output = {
    "captured_at_utc": datetime.now(timezone.utc).isoformat(),
    "repo_head": head,
    "repo_tree": tree,
    "binary": {"path": str(binary), "sha256": hashlib.sha256(binary_bytes).hexdigest(),
               "size_bytes": len(binary_bytes), "mtime_ns": stat.st_mtime_ns,
               "mtime_iso_local": mtime_iso, "version_command": [str(binary), "--version"],
               "version": version},
    "strings": {"command": ["strings", "-n", "4", str(binary)],
                "stdout_sha256": hashlib.sha256(strings.stdout).hexdigest(),
                "line_count": len(lines)},
    "extractors": {"current_CALL_RE_match_count": len(surfaces.CALL_RE.findall(dump)),
                   "current_OMP_CALL_RE_match_count": len(surfaces.OMP_CALL_RE.findall(dump)),
                   "candidate_pattern": new_pattern.pattern,
                   "candidate_call_site_count": len(calls),
                   "candidate_unique_class_count": len(class_ids)},
    "candidate_call_sites": calls,
    "registry_descriptions": descriptions,
    "baseline_loader_group_class_ids": baseline_classes,
    "candidate_class_ids": class_ids,
    "candidate_equals_baseline": class_ids == baseline_classes,
    "all_descriptions_present": all(row["present"] for row in descriptions.values()),
}
print(json.dumps(output, indent=2, sort_keys=True))
if not output["candidate_equals_baseline"] or not output["all_descriptions_present"]:
    raise SystemExit(1)
