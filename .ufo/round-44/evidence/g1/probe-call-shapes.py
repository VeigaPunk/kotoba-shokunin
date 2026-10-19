from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, "verifiers")
import verify_surfaces as surfaces

DUMP = Path(".ufo/round-44/drafts/g1/omp-live-18.12.2-strings.txt")
SHAPE_RE = re.compile(
    r'(?<![A-Za-z0-9_$])([A-Za-z_$][A-Za-z0-9_$]*)\(\s*[^\s,()]+\s*,\s*'
    r'(?:"([a-z0-9_-]+)"|([A-Za-z_$][A-Za-z0-9_$]*))\s*,\s*'
    r'"([A-Za-z0-9_./-]+\.md)"(?=\s*[,)])'
)


def main() -> int:
    dump = DUMP.read_text(errors="replace")
    constants = surfaces.constant_table(dump)
    matches = list(SHAPE_RE.finditer(dump))
    pairs = sorted({
        (
            match.group(2) or constants.get(
                match.group(3), "<unresolved-var:%s>" % match.group(3)),
            match.group(4),
        )
        for match in matches
    })
    entries = surfaces.load_baseline(Path("verifiers/surfaces-baseline.json"))
    declared = sorted(
        (entry["group"], entry["file"])
        for entry in entries
        if entry["harness"] == "omp" and entry["context_kind"] == "loader-group"
    )
    print("registered_shape_calls=%d" % len(matches))
    print("callee_counts=%s" % dict(collections.Counter(m.group(1) for m in matches)))
    print("unique_group_file_pairs=%d" % len(pairs))
    print("pairs=%s" % pairs)
    print("declared_omp_loader_group_pairs=%d" % len(declared))
    print("declared_pairs=%s" % declared)
    print("pair_set_equal=%s" % (pairs == declared))
    print("existing_omp_allowlist_extract=%d" % len(surfaces.extract_classes(dump, "omp")))
    print("OMP_CALL_RE_matches=%d" % len(surfaces.OMP_CALL_RE.findall(dump)))
    for match in matches:
        group = match.group(2) or constants.get(
            match.group(3), "<unresolved-var:%s>" % match.group(3))
        print("call=%s group=%s file=%s" % (match.group(1), group, match.group(4)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
