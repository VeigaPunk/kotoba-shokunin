#!/usr/bin/env python3
"""Build the three OC-2 decoys from a real opencode strings dump (round 72).

Usage: python3 make_decoys.py <oc-strings.txt> <outdir>

Each decoy keeps the same tokens and breaks exactly one binding of the
replacement rule:

  decoy-a-moved.txt   the config join is moved out of the
                      `opencode.config.instruction` plugin into the neighbouring
                      `opencode.config.location-watcher` plugin (same tokens, no
                      instruction-loading role).
  decoy-b-callee.txt  the join stays in place but its callee is renamed, so it is
                      no longer an alias imported as `join` from "path".
  decoy-c-method.txt  the round-14 `.join(<v>.config,"AGENTS.md")` METHOD shape is
                      planted in the neighbouring plugin (the shape the committed
                      rule's OC_CONFIG_JOIN_RE accepts, with no loader role).
"""
import os
import sys

PLUGIN = 'id:"opencode.config.instruction"'
NEXT = 'tt({id:"opencode.config.'
WATCHER = 'tt({id:"opencode.config.location-watcher",effect:c(function*(e){'
JOIN = 'j1(r.config,"AGENTS.md")'


def splice(dump: str, insert: str) -> str:
    at = dump.find(WATCHER)
    assert at >= 0, "location-watcher plugin not found"
    at += len(WATCHER)
    return dump[:at] + insert + dump[at:]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    src, outdir = argv
    with open(src, encoding="utf-8", errors="replace") as fh:
        dump = fh.read()
    start = dump.find(PLUGIN)
    end = dump.find(NEXT, start + 10)
    assert start >= 0 and end > start, "instruction plugin window not found"
    head, window, tail = dump[:start], dump[start:end], dump[end:]
    assert JOIN in window, "config join not found inside the instruction plugin"
    os.makedirs(outdir, exist_ok=True)
    stripped = window.replace(JOIN, "void 0", 1)
    variants = {
        "decoy-a-moved.txt": splice(head + stripped + tail, JOIN + ";"),
        "decoy-b-callee.txt": head + window.replace(
            JOIN, 'zz(r.config,"AGENTS.md")', 1) + tail,
        "decoy-c-method.txt": splice(
            head + stripped + tail, '.join(r.config,"AGENTS.md");'),
    }
    for name, text in variants.items():
        with open(os.path.join(outdir, name), "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote", os.path.join(outdir, name), len(text), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
