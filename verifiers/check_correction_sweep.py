#!/usr/bin/env python3
r"""check_correction_sweep.py -- the round-52 fix for lesson M36 (shown able to fail).

Round 51's corrections sweep missed two places that still stated a superseded
claim without the declared result (round-51 spot-check, routed defects 1-2):
`corpus/README.md` (the round-51 Core note: `overlap levers backed 7 of 7
clients`) and the `SCORECARD.md` depth cell (lead `7 of 7`, exit 0 @
`34cfffbb`).  This check sweeps the registry below.

Rule per registry entry: every Markdown block of FILE that contains the STALE
pattern must also contain the DECLARED pattern; with `lead: true` the DECLARED
pattern must occur BEFORE the first STALE match in that block (a headline leads
with the declared result).  A block is a list item with its indented
continuation lines, a paragraph, or one table row.

Usage: check_correction_sweep.py (--rev REV | --root DIR) | --self-test
Exit 0 clean, 1 a block violates an entry, 2 could not evaluate.
A new superseded claim is added as a new registry row; rows are not edited.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
REGISTRY = (
    {"id": "r51-c2-readme", "file": "corpus/README.md",
     "stale": r"overlap levers backed 7 of 7 clients", "declared": r"4 of 7", "lead": False},
    {"id": "r51-c2-scorecard-lead", "file": "SCORECARD.md",
     "stale": r"`7 of 7`, exit 0 @ `34cfffbb`", "declared": r"4 of 7", "lead": True},
    {"id": "r51-c2-province", "file": "PROVINCE.md",
     "stale": r"overlap levers backed 7 of 7 clients", "declared": r"4 of 7", "lead": False},
    # round 52 attempt 2 (M38, Q29/Q30): opencode and Copilot CLI were recorded
    # as silent on MCP server instructions; S041 and S042 document both.
    {"id": "r52-c2-skill-silent", "file": "SKILL.md",
     "stale": r"say nothing about server instructions", "declared": r"S041", "lead": False},
    {"id": "r52-c2-province-five", "file": "PROVINCE.md",
     "stale": r"specification and five pinned clients", "declared": r"S041", "lead": False},
    {"id": "r52-c2-readme-five", "file": "corpus/README.md",
     "stale": r"five client pages \(S032 spec", "declared": r"S041", "lead": False},
    # round 53 (Q29): the round-53 C2 corpus corrections and re-measurements.
    # Knowledge entries and README rows keep the stale phrase verbatim and carry
    # the declared re-measurement in the same block; the two SKILL.md rows are
    # canaries -- the replacement wording removes the stale phrase, so the row
    # fires only if it is reintroduced without the declared result.
    {"id": "r53-c2-claudemd-semantics", "file": "corpus/knowledge/claude-md-surface.md",
     "stale": r"Same load semantics as AGENTS\.md",
     "declared": r"round-53 correction \(2026-10-22\)", "lead": False},
    {"id": "r53-c2-census-agentsmd-alwayson",
     "file": "corpus/knowledge/instruction-surface-census-round13.md",
     "stale": r"Always-on: injected into every session in its repo",
     "declared": r"round-53 correction \(2026-10-22\)", "lead": False},
    {"id": "r53-c2-agentsmd-six-files",
     "file": "corpus/knowledge/agents-md-and-dispatch-surfaces.md",
     "stale": r"6 identical-shape files in",
     "declared": r"held 17 `AGENTS\.md` files", "lead": False},
    {"id": "r53-c2-agentsmd-host-60-lines",
     "file": "corpus/knowledge/agents-md-and-dispatch-surfaces.md",
     "stale": r"\(~60 lines\)", "declared": r"14 lines / 949 B", "lead": False},
    {"id": "r53-c2-readme-six-child", "file": "corpus/README.md",
     "stale": r"6 child AGENTS\.md", "declared": r"17 child files", "lead": False},
    {"id": "r53-c2-skill-75-line", "file": "SKILL.md",
     "stale": r"75-line host", "declared": r"14 lines / 949 B", "lead": False},
    {"id": "r53-c2-skill-six-files", "file": "SKILL.md",
     "stale": r"AGENTS\.md` \(6 files\)", "declared": r"17 files", "lead": False},
    {"id": "r53-c2-baseline-pointer", "file": "verifiers/checklist-baseline.json",
     "stale": r"host file lines 48 and 51",
     "declared": r"round-53 re-measure \(2026-10-22\)", "lead": False},
    {"id": "r57-r2-s076-note", "file": "corpus/knowledge/agent-definition-files-round56.md",
     "stale": r"holds no agent word", "declared": r"Round-57 correction", "lead": False},
    {"id": "r57-r2-s078-note", "file": "corpus/knowledge/agent-definition-files-round56.md",
     "stale": r"body of a fenced example", "declared": r"Round-57 correction", "lead": False},
    {"id": "r57-r2-skill-singular-agent", "file": "SKILL.md",
     "stale": r"singular `agent/` still loads", "declared": r"migrate-v1\.mdx:486", "lead": False},
)

# Files a registry row names that the self-test's four fixed fixtures do not
# write; seeded per case so `sweep` never sees a missing file (round 53).
SEEDED = (
    "corpus/knowledge/claude-md-surface.md",
    "corpus/knowledge/instruction-surface-census-round13.md",
    "corpus/knowledge/agents-md-and-dispatch-surfaces.md",
    "verifiers/checklist-baseline.json",
    "corpus/knowledge/agent-definition-files-round56.md",
)


def blocks(text: str) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    cur: list[str] = []
    start = 0
    for i, ln in enumerate(text.splitlines(), 1):
        new_item = bool(re.match(r"^(?:[-*] |\d+\. |\|)", ln)) or ln.startswith("#")
        if not ln.strip() or new_item:
            if cur:
                out.append((start, "\n".join(cur)))
            cur = [] if not ln.strip() else [ln]
            start = i
            if ln.startswith("|") or ln.startswith("#"):
                out.append((i, ln))
                cur = []
            continue
        if not cur:
            start = i
        cur.append(ln)
    if cur:
        out.append((start, "\n".join(cur)))
    return out


def sweep(read) -> list[str]:
    bad = []
    for e in REGISTRY:
        text = read(e["file"])
        if text is None:
            raise RuntimeError("missing %s" % e["file"])
        for line, b in blocks(text):
            m = re.search(e["stale"], b)
            if not m:
                continue
            d = re.search(e["declared"], b)
            if not d or (e["lead"] and d.start() > m.start()):
                bad.append("%s %s:%d stale claim without the declared result%s" % (
                    e["id"], e["file"], line, " leading" if e["lead"] else ""))
    return bad


def reader(rev: str | None, root: str | None):
    def read(path: str):
        if rev:
            r = subprocess.run(["git", "-C", str(LANE), "show", "%s:%s" % (rev, path)],
                               capture_output=True)
            return r.stdout.decode("utf-8") if r.returncode == 0 else None
        p = Path(root) / path
        return p.read_text(encoding="utf-8") if p.is_file() else None
    return read


def revision_error(rev: str, where, code: int, detail: str) -> str:
    """The could-not-evaluate reason for a failed `rev-parse --verify --quiet`.

    An unknown revision is git's own exit 1 with no diagnostic.  Any other
    failure (a refusing git: dubious ownership, no repository, a broken object
    store) is an environment failure and is reported with git's own words,
    never as a claim about the revision.
    """
    detail = detail.strip()
    if code == 1 and not detail:
        return "revision %r is not a commit in %s" % (rev, where)
    first = detail.splitlines()[0] if detail else "(git printed no diagnostic)"
    return ("git rev-parse %r failed in %s (exit %d): %s"
            % (rev, where, code, first))


def verify_revision(rev: str) -> None:
    r = subprocess.run(["git", "-C", str(LANE), "rev-parse", "--verify", "--quiet",
                        "%s^{commit}" % rev], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(revision_error(
            rev, LANE, r.returncode, r.stderr.decode("utf-8", "replace")))


def self_test() -> int:
    fails, n = [], 0

    def case(name, readme, score, want, province="- nothing stale\n",
             skill="- nothing stale\n", seed=None):
        nonlocal n
        n += 1
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "corpus").mkdir()
            (Path(t) / "corpus/README.md").write_text(readme)
            (Path(t) / "SCORECARD.md").write_text(score)
            (Path(t) / "PROVINCE.md").write_text(province)
            (Path(t) / "SKILL.md").write_text(skill)
            for rel in SEEDED:
                p = Path(t) / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text((seed or {}).get(rel, "- fixture\n"))
            got = sweep(reader(None, t))
        ids = sorted(x.split()[0] for x in got)
        if ids != sorted(want):
            fails.append("%s: got %r" % (name, got))

    stale_r = "- note: `overlap levers backed 7 of 7 clients`.\n  more text\n"
    fixed_r = stale_r + "  Correction: declared result 4 of 7.\n"
    later_r = stale_r + "\n- next item: 4 of 7 elsewhere\n"
    stale_s = "| depth | 9 | `0 of 7` -> `7 of 7`, exit 0 @ `34cfffbb`; correction 4 of 7 |\n"
    fixed_s = "| depth | 9 | declared 4 of 7; widened `7 of 7`, exit 0 @ `34cfffbb` |\n"
    case("red both", stale_r, stale_s, ["r51-c2-readme", "r51-c2-scorecard-lead"])
    case("green both", fixed_r, fixed_s, [])
    case("correction in another block is not a correction", later_r, fixed_s, ["r51-c2-readme"])
    case("declared after the stale lead fails", fixed_r, stale_s, ["r51-c2-scorecard-lead"])
    case("no stale claim: clean", "- nothing here\n", "| depth | 9 | x |\n", [])
    silent = "| every client | a skill too | the opencode pages say nothing about server instructions |\n"
    case("r52 silent negative without S041 fails", "- x\n", "| d | 9 | x |\n",
         ["r52-c2-skill-silent"], skill=silent)
    case("r52 silent negative with S041 passes", "- x\n", "| d | 9 | x |\n", [],
         skill=silent.replace("|\n", "; corrected by S041 |\n"))
    # round 53 (Q29): each round-53 row is shown red without its correction and
    # green with it, on the file the row names.
    stale_c = "- Same load semantics as AGENTS.md (always-on when present in the repo) -> tax\n"
    red_c = {"corpus/knowledge/claude-md-surface.md": stale_c}
    grn_c = {"corpus/knowledge/claude-md-surface.md":
             stale_c + "  round-53 correction (2026-10-22): not the same semantics\n"}
    case("r53 claude-md semantics red", "- x\n", "| d | 9 | x |\n",
         ["r53-c2-claudemd-semantics"], seed=red_c)
    case("r53 claude-md semantics green", "- x\n", "| d | 9 | x |\n", [], seed=grn_c)
    base_red = {"verifiers/checklist-baseline.json":
                '      "disposition": "unexecuted:x; host file lines 48 and 51"\n'}
    base_grn = {"verifiers/checklist-baseline.json":
                '      "disposition": "unexecuted:x; host file lines 48 and 51;'
                ' round-53 re-measure (2026-10-22): 14 lines / 949 B"\n'}
    case("r53 baseline pointer red", "- x\n", "| d | 9 | x |\n",
         ["r53-c2-baseline-pointer"], seed=base_red)
    case("r53 baseline pointer green", "- x\n", "| d | 9 | x |\n", [], seed=base_grn)
    # round 57 (Q29, R2): each round-57 row red without its correction, green with it.
    ent = "corpus/knowledge/agent-definition-files-round56.md"
    stale_e = "S076's project line holds no agent word. S078's quote is the body of a fenced example.\n"
    case("r57 quote notes red", "- x\n", "| d | 9 | x |\n",
         ["r57-r2-s076-note", "r57-r2-s078-note"], seed={ent: stale_e})
    case("r57 quote notes green", "- x\n", "| d | 9 | x |\n", [],
         seed={ent: stale_e.rstrip("\n") + " Round-57 correction (R2): see the lesson.\n"})
    case("r57 singular agent clause red", "- x\n", "| d | 9 | x |\n",
         ["r57-r2-skill-singular-agent"],
         skill="| opencode | `.opencode/agents` (singular `agent/` still loads per a docs commit) |\n")
    case("r57 singular agent clause green", "- x\n", "| d | 9 | x |\n", [],
         skill="| opencode | singular `agent/` still loads (`migrate-v1.mdx:486`) |\n")

    script = str(Path(__file__).resolve())

    def run_cli(rev: str, env=None):
        return subprocess.run([sys.executable, "-B", script, "--rev", rev], cwd=LANE,
                              env=env, capture_output=True, text=True)

    unknown = "0" * 40
    p = run_cli(unknown)
    n += 1
    if (p.returncode != 2 or not p.stderr.startswith("could-not-evaluate: ")
            or "is not a commit" not in p.stderr):
        fails.append("unknown revision: exit %d, stderr %r" % (p.returncode, p.stderr))

    with tempfile.TemporaryDirectory() as t:
        Path(t, "python3").symlink_to(sys.executable)
        env = os.environ.copy()
        env["PATH"] = t
        p = run_cli("HEAD", env)
    n += 1
    if (p.returncode != 2 or not p.stderr.startswith("could-not-evaluate: ")
            or "'git'" not in p.stderr):
        fails.append("git unavailable: exit %d, stderr %r" % (p.returncode, p.stderr))

    # A git that is present and refuses (exit 128, e.g. dubious ownership) is
    # an environment failure: the gate must quote git's own refusal, not claim
    # the revision is unknown.
    with tempfile.TemporaryDirectory() as t:
        Path(t, "python3").symlink_to(sys.executable)
        shim = Path(t, "git")
        shim.write_text("#!/bin/sh\n"
                        "echo \"fatal: detected dubious ownership in repository"
                        " at '/x/y'\" >&2\n"
                        "exit 128\n", encoding="utf-8")
        shim.chmod(0o755)
        env = os.environ.copy()
        env["PATH"] = t
        p = run_cli("HEAD", env)
    n += 1
    if (p.returncode != 2 or not p.stderr.startswith("could-not-evaluate: ")
            or "is not a commit" in p.stderr
            or "dubious ownership" not in p.stderr):
        fails.append("refusing git: exit %d, stderr %r" % (p.returncode, p.stderr))

    print("%d failure(s) over %d assertions" % (len(fails), n))
    for f in fails:
        print("FAIL", f)
    return 1 if fails else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--rev")
    g.add_argument("--root")
    g.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    try:
        if a.rev:
            verify_revision(a.rev)
        bad = sweep(reader(a.rev, a.root))
    except (OSError, RuntimeError) as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    for b in bad:
        print("FAIL", b)
    print("correction sweep: %d stale block(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
