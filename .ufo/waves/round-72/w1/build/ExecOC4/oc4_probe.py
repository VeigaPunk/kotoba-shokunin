#!/usr/bin/env python3
"""Round-72 OC-4 probe: the re-derived rule against the real v2.1.4 dump, the
v2.1.4 fixtures, the decoys and the previous generations.

Usage: python3 -B oc4_probe.py <opencode-strings-dump> [fixtures-dir]

Prints, for each input, whether `opencode_read_hook_matches` accepts it, plus the
dump line numbers of the five edges the rule binds (so the derivation can be
re-checked without trusting this script).
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("vs", HERE / "verify_surfaces.py")
vs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vs)


def edges(dump: str) -> list[str]:
    """(label, 1-based dump line) for each edge the rule binds, all inside the
    module that defines the instruction service."""
    svc = vs.OC_INSTR_SERVICE_RE.search(dump)
    if svc is None:
        return ["instruction service class        ABSENT"]
    module = vs.opencode_module(dump, svc.start())
    seps = list(vs.OC_MODULE_SEP_RE.finditer(dump, 0, svc.start()))
    base = seps[-1].end() if seps else 0
    assert dump[base:base + len(module)] == module
    out = []
    for label, pat in (
            ("instruction service class", vs.OC_INSTR_SERVICE_RE),
            ("render template", vs.OC_INSTR_RENDER_RE),
            ("read plugin registration", vs.OC_READ_PLUGIN_RE),
            ("read-plugin walk-up", vs.OC_READ_WALK_RE),
            ("read-plugin instruction load", vs.OC_READ_INSTR_LOAD_RE)):
        m = pat.search(module)
        out.append("%-30s %s" % (label, dump.count("\n", 0, base + m.start()) + 1
                                 if m else "ABSENT (in module)"))
    for label, needle in (
            ('service .of({load:})', ".of({load:"),
            ('LF="AGENTS.md" binding', '="AGENTS.md"')):
        pos = module.find(needle)
        out.append("%-30s %s" % (label, dump.count("\n", 0, base + pos) + 1
                                 if pos >= 0 else "ABSENT (in module)"))
    return out


def main(argv: list[str]) -> int:
    dump_path = Path(argv[1])
    fx = Path(argv[2]) if len(argv) > 2 else HERE / "fixtures"
    dump = dump_path.read_text(encoding="utf-8", errors="replace")

    print("dump: %s (%d bytes, %d lines)" % (dump_path, len(dump),
                                             dump.count("\n") + 1))
    print("module separators (v2.1.4 `// @bun @bytecode`):",
          len(vs.OC_MODULE_SEP_RE.findall(dump)))
    print("1.19.x separator `\\n// @bun\\n` occurrences:",
          dump.count("\n// @bun\n"))
    print()
    print("edges of the re-derived OC-4 witness in the real dump:")
    for line in edges(dump):
        print("  " + line)
    print()
    print("opencode_read_hook_matches(real dump) = %s"
          % vs.opencode_read_hook_matches(dump))
    print()

    fixtures = sorted(p for p in fx.glob("strings-*.txt"))
    print("%-52s %s" % ("fixture", "OC-4"))
    for p in fixtures:
        text = p.read_text(encoding="utf-8", errors="replace")
        print("%-52s %s" % (p.name, vs.opencode_read_hook_matches(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
