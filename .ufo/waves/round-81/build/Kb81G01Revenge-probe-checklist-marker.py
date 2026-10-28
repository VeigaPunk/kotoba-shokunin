#!/usr/bin/env python3
"""Kb81G01Revenge — does the checklist's citation predicate accept a marker file?

Function-level probe of verifiers/verify_skill_checklist.py's own predicate
(`citation_resolve`, the function `governance.citation_resolves` calls), on the
LANE'S committed bytes, against a throwaway fixture tree under TMPDIR.  No fleet
or lane file is touched; the repo is read, never written.
"""
import importlib.util
import os
import pathlib
import shutil
import tempfile

LANE_SPEC = "/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_skill_checklist.py"
S = pathlib.Path(tempfile.mkdtemp(prefix="kb81g01-marker-"))
try:
    lane = S / "fleet" / "lane"
    lane.mkdir(parents=True)
    (S / "fleet" / ".ufo" / "reports" / "round-16").mkdir(parents=True)
    marker = S / "fleet" / ".ufo" / "reports" / "round-16" / "kotoba.md"
    marker.write_text("marker\n")          # exactly the W10-class artefact (7 bytes)

    spec = importlib.util.spec_from_file_location("vsc", LANE_SPEC)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    tok = "../.ufo/reports/round-16/kotoba.md"
    print("fixture fleet:", S / "fleet")
    print("token:", tok)
    print("lane copy of the token's own path exists?",
          (lane / ".ufo" / "reports" / "round-16" / "kotoba.md").exists())
    print("citation_resolve(token, lane) ->", m.citation_resolve(tok, lane),
          "   (lane.parent is the fixture fleet holding the marker)")
    print("marker bytes:", marker.stat().st_size, repr(marker.read_text()))
    marker.unlink()
    print("after removing the marker ->", m.citation_resolve(tok, lane))
finally:
    shutil.rmtree(S, ignore_errors=True)
