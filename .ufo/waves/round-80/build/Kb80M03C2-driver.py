#!/usr/bin/env python3
"""Kb80M03C2 world builder + probe runner (scratch tool, disposable).

Builds six committed worlds on top of the r80 base inside the scratch clone
and runs the ported frozen counter against them with each command's own exit
status captured.  Mutant probes run through the same run_counter().
"""
import hashlib
import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
S = Path("/fast/scratch/hyaku/kotoba-r80/Kb80M03C2")
CLONE = S / "clone"
REC = S / "receipts"
BASE = "398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93"
PORT = S / "port" / "check_allowed_tools.py"

spec = importlib.util.spec_from_file_location("port", PORT)
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

pages = {P.FIX[k][0]: P._page(k, P.SURFACES[k]) for k in P.SURFACE_ORDER}

DROP_RE = re.compile(r"^ {0,3}\|\s*S(226|227|228|229|230|231)\s*\|")

ROW = ("| `" + P.COUNTER_PATH + "` | gate | `python3 -B " + P.COUNTER_PATH
       + " --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | "
         "`--self-test` | in-file | none | kotoba |")
RULE = ("- `allowed-tools` per client: Open specification, Claude Code, "
        "Factory, Microsoft Agent Framework, pi and Mistral Vibe are recorded "
        "in `" + P.ENTRY + "`.")
BULLET = ("- allowed-tools semantics per client: Open specification, Claude "
          "Code, Factory, Microsoft Agent Framework, pi and Mistral Vibe, in "
          "`" + P.ENTRY + "`, counted by the counter.")

PARA = ("The `allowed-tools` field of Claude Code is documented here and this "
        "page states without prompting you for approval in its own words.")
BANNER = ("## The allowed-tools field of Claude Code is documented here and "
          "this page states without prompting you for approval in its own "
          "words")
QUOTE4 = ("The allowed-tools field of Claude Code is documented here and this "
          "page states without prompting you for approval in its own words")

GITENV = dict(os.environ,
              GIT_AUTHOR_NAME="scratch-r80",
              GIT_AUTHOR_EMAIL="scratch@example.invalid",
              GIT_COMMITTER_NAME="scratch-r80",
              GIT_COMMITTER_EMAIL="scratch@example.invalid",
              TMPDIR=str(S / "tmp"))


def git(*args):
    r = subprocess.run(["git", "-C", str(CLONE), *args], capture_output=True,
                       text=True, env=GITENV)
    if r.returncode != 0:
        raise RuntimeError(f"git {args[:3]} failed: {r.stderr}")
    return r.stdout


def show_base(path):
    return subprocess.run(["git", "-C", str(CLONE), "show", f"{BASE}:{path}"],
                          check=True, capture_output=True, text=True,
                          env=GITENV).stdout


def world_sources(overrides, pg):
    keep = [l for l in show_base("corpus/SOURCES.md").splitlines()
            if not DROP_RE.match(l)]
    rows = [P._reg_line(P.FIX[k][0], pg, k, **overrides.get(k, {}))
            for k in P.SURFACE_ORDER]
    return "\n".join(keep + [""] + rows) + "\n"


def world_skill():
    return show_base("SKILL.md") + "\n" + ROW + "\n\n" + RULE + "\n"


def world_province():
    lines = show_base("PROVINCE.md").splitlines()
    out, inserted = [], False
    for l in lines:
        out.append(l)
        if not inserted and l.strip() == "## Core":
            out += ["", BULLET]
            inserted = True
    if not inserted:
        out += ["", "## Core", "", BULLET]
    return "\n".join(out) + "\n"


def world_files(*, sources, entry, pg):
    files = {
        "corpus/SOURCES.md": sources,
        P.ENTRY: entry,
        P.MANIFEST: P._manifest(pg),
        "SKILL.md": world_skill(),
        "PROVINCE.md": world_province(),
    }
    for key in P.SURFACE_ORDER:
        files[f"{P.SNAPDIR}/{P.FIX[key][2]}"] = pg[P.FIX[key][0]]
    return files


def commit_world(name, files):
    git("checkout", "-q", "--detach", BASE)
    st = git("status", "--porcelain")
    if st.strip():
        raise RuntimeError(f"dirty tree after checkout: {st!r}")
    for rel, text in files.items():
        p = CLONE / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    git("add", "-A")
    git("-c", "commit.gpgsign=false", "commit", "-qm", name)
    return git("rev-parse", "HEAD").strip()


def run_counter(tag, counter, rev, repo=None):
    cmd = ["python3", "-B", str(counter), "--repo", str(repo or CLONE),
           "--rev", rev, "--work", str(S / "tmp")]
    out_path = REC / f"Kb80M03C2-{tag}.txt"
    with open(out_path, "w") as f:
        f.write("$ " + " ".join(cmd) + "\n")
        r = subprocess.run(cmd, capture_output=True, text=True, env=GITENV)
        f.write(r.stdout)
        if r.stderr:
            f.write("--- stderr ---\n" + r.stderr)
        f.write(f"exit={r.returncode}\n")
    return r.returncode, r.stdout + r.stderr


def main():
    results = []

    # ---- worlds -----------------------------------------------------------
    wH = commit_world("Kb80M03C2 honest world", world_files(
        sources=world_sources({}, pages),
        entry=P._entry_text(pages), pg=pages))

    w1 = commit_world("Kb80M03C2 W1: one 12-cell registry row (S227)",
                      world_files(
                          sources=world_sources(
                              {"claude": {"extra": 1}}, pages),
                          entry=P._entry_text(pages), pg=pages))

    evil = "https://agentskills.io.evil.test/specification.md"
    entry3 = P._entry_text(pages)
    n = entry3.count("https://agentskills.io/specification.md")
    assert n == 1, f"S226 url occurrences in entry: {n}"
    w3 = commit_world("Kb80M03C2 W3: sibling host agentskills.io.evil.test",
                      world_files(
                          sources=world_sources(
                              {"spec": {"url": evil}}, pages),
                          entry=entry3.replace(
                              "https://agentskills.io/specification.md", evil),
                          pg=pages))

    pg4 = dict(pages)
    assert PARA in pages["S227"], "claude paragraph not found"
    pg4["S227"] = pages["S227"].replace(PARA, BANNER)
    w4 = commit_world("Kb80M03C2 W4: quote located on a banner heading line",
                      world_files(
                          sources=world_sources({}, pg4),
                          entry=P._entry_text(pg4, quotes={"claude": QUOTE4}),
                          pg=pg4))

    w5 = commit_world(
        "Kb80M03C2 W5: S227 used-by names the round-79 entry, not the entry",
        world_files(
            sources=world_sources(
                {"claude": {"used_by":
                            "corpus/knowledge/allowed-tools-surfaces-round79.md"}},
                pages),
            entry=P._entry_text(pages), pg=pages))

    w6 = commit_world("Kb80M03C2 W6: S227 opened 2026-10-26 (stale)",
                      world_files(
                          sources=world_sources(
                              {"claude": {"opened": "2026-10-26"}}, pages),
                          entry=P._entry_text(pages), pg=pages))

    worlds = {"WH": wH, "W1": w1, "W3": w3, "W4": w4, "W5": w5, "W6": w6}
    (REC / "worlds.sha256").write_text("".join(
        f"{sha}  {name}\n" for name, sha in sorted(worlds.items())))

    # ---- port probes ------------------------------------------------------
    rc0, out0 = run_counter("R0-lane-base", PORT, BASE, repo=LANE)
    results.append(("R0 port x LANE base", rc0,
                    "documented 0 of 6" in out0, "documented 0 of 6" in out0))
    rc1, out1 = run_counter("R1-port-WH", PORT, wH)
    baseline_ok = rc1 == 0 and "documented 6 of 6" in out1 \
        and "generator world:" in out1
    results.append(("R1 port x WH (baseline)", rc1, baseline_ok, None))
    if not baseline_ok:
        print("BASELINE FAILURE — every mutant verdict is inconclusive")
        for r in results:
            print(r)
        return 3

    def pair(tag, world, expect_finding):
        rcf, outf = run_counter(f"{tag}-frozen", PORT, world)
        okf = rcf == 1 and expect_finding in outf \
            and "documented 5 of 6" in outf
        results.append((f"{tag} frozen x {world[:8]}", rcf, okf,
                        expect_finding))
        return rcf, outf

    pair("R2-W1", w1, "12 cells")
    pair("R6-W3", w3, "no URL on spec's pinned host")
    pair("R8-W4", w4, "heading line")
    pair("R10-W5", w5, "used-by")
    pair("R12-W6", w6, "was not opened this round")

    print("worlds:", {k: v[:12] for k, v in worlds.items()})
    print("generator-world line in R1:",
          [l for l in out1.splitlines() if "generator world" in l])
    for r in results:
        print(r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
