#!/usr/bin/env python3
"""Print the OC-2 report row for the committed rule and for the scratch replacement.

Usage: python3 probe_oc2.py <opencode-strings-dump> [...]

Read-only.  Regenerate the dump with
  strings -n 4 ~/.opencode/bin/opencode > oc-strings.txt      # sha256 020fb253…
and pass any mutated copy (see make_decoys.py) or fixture in its place.
"""
import importlib.util
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = LANE + "/verifiers/verify_surfaces.py"
NEW = LANE + "/.ufo/waves/round-72/w1/build/ExecOC2/verify_surfaces.py"


def load(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(argv: list[str]) -> int:
    base, new = load(BASE, "vs_base"), load(NEW, "vs_new")
    for path in argv:
        with open(path, encoding="utf-8", errors="replace") as fh:
            dump = fh.read()
        for label, module in (("base", base), ("new", new)):
            _, report = module.extract_opencode_classes(dump)
            oc2 = next(r for r in report if r["rule_id"] == "OC-2")
            print("%-34s %-4s OC-2 matched=%s owns=%s missing=%s"
                  % (path.rsplit("/", 1)[-1], label, oc2["matched"],
                     oc2["owns"], oc2["missing"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
