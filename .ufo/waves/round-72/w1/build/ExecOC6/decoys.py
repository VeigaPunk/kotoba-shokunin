#!/usr/bin/env python3
"""Regenerate the round-72 OC-6 decoys from a shared opencode strings dump and
report what the re-derived rule does with each one.

Usage:  python3 -B decoys.py [DUMP] [OUTDIR]

DUMP defaults to /tmp/k72-oc-strings.txt (sha256 020fb253…, opencode v2.1.4).
Each decoy keeps the rule's tokens and breaks exactly one conjunct; the real
dump must read MATCH and every decoy NO-MATCH.
"""
from __future__ import annotations

import hashlib
import importlib.util
import os
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (name, old bytes, new bytes) — each keeps every token the rule scans for and
# removes only the instruction-loading role of one conjunct.
DECOYS = (
    # the instruction key rendered with the `core/codemode` layer's render
    # (same GA({key:…,codec:…,read:…,render:{…removed:()=>…}}) shape)
    ("decoy-codemode-layer",
     'r=(a)=>GA({key:__,codec:po(m_),read:u(a),render:{initial:Rr,changed:B_,'
     'removed:()=>"Previously loaded instructions no longer apply."}})',
     'r=(a)=>GA({key:__,codec:po(m_),read:u(a),render:{initial:Tu,changed:M_,'
     'removed:()=>"Code Mode tools are no longer available. Do not use any '
     'previously listed Code Mode tools."}})'),
    # the SessionContext composition drops the discovery layer
    ("decoy-no-compose", "deps:[VT,yP,DA,Sue,M6,yue", "deps:[VT,yP,DA,Sue,yue"),
    # the config plugin walks another target
    ("decoy-no-walk",
     'up({targets:["AGENTS.md"],start:T,stop:V,type:"file"})',
     'up({targets:["CLAUDE.md"],start:T,stop:V,type:"file"})'),
    # the discovery service label renamed, all other tokens kept
    ("decoy-service-renamed",
     'class WT extends U()("@opencode/InstructionDiscovery")',
     'class WT extends U()("@opencode/InstructionDiscoveryX")'),
)


def load_rule():
    spec = importlib.util.spec_from_file_location(
        "oc6_scratch", HERE / "verify_surfaces.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(argv: list[str]) -> int:
    dump_path = argv[1] if len(argv) > 1 else "/tmp/k72-oc-strings.txt"
    raw = Path(dump_path).read_bytes()
    print("dump %s sha256 %s bytes %d"
          % (dump_path, hashlib.sha256(raw).hexdigest(), len(raw)))
    dump = raw.decode("utf-8", "replace")
    rule = load_rule()
    print("%-26s %s" % ("live dump", "MATCH" if rule.opencode_context_layer_v214_matches(dump) else "NO-MATCH"))
    if len(argv) > 2:
        outdir = Path(argv[2])
    else:
        outdir = Path(tempfile.mkdtemp(prefix="k72oc6-decoys."))
    failures = 0
    for name, old, new in DECOYS:
        if dump.count(old) != 1:
            print("%-26s SKIP: anchor occurs %d times" % (name, dump.count(old)))
            failures += 1
            continue
        text = dump.replace(old, new)
        path = outdir / (name + ".txt")
        path.write_text(text, encoding="utf-8")
        got = rule.opencode_context_layer_v214_matches(text)
        print("%-26s %s  (%s)" % (name, "MATCH" if got else "NO-MATCH", path))
        failures += 1 if got else 0
    print("%d decoy/decoys accepted (must be 0)" % failures)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
