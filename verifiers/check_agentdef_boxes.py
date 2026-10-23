#!/usr/bin/env python3
r"""check_agentdef_boxes.py -- frozen counter for the round-56 C2 (operability) claim.

Round 56, claim C2.  Surface: the SKILL.md section "Agent-definition fidelity
checklist" (nine boxes, agentdef.01..agentdef.09) and the execution of that
checklist by a delegate instrument.  At BASE_REV
b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 every one of the nine boxes carries
an `unexecuted:` disposition in verifiers/checklist-baseline.json, so no box
of the section is executed at base.

This counter is frozen before any claim content exists.  The box set, the
operational reading of every box, the case generator and the instrument
contract are pinned here and never read from the revision measured.

WHAT IS MEASURED
----------------
T = the number of boxes in <rev>'s verifiers/checklist-baseline.json whose
`section` is exactly "Agent-definition fidelity checklist".  N = the number
of those boxes that COUNT.

A box COUNTS iff all four of the following hold.

(a) Delegation.  The box's `disposition` in <rev>'s map is
    `delegated:<repo-relative path>`; the path is not absolute and has no
    `..` component; and the path exists in <rev> as a blob (`git ls-tree`).
(b) Un-reworded box.  The box's `text_sha256` in <rev>'s map equals the
    BASE_REV map's `text_sha256` for the same box_id (PINNED_BOX_SHA below,
    captured from BASE_REV's map).  A reworded box does not count.
(c) No standard-library shadow.  The extracted tree of <rev> (git archive
    into a fresh temp dir) contains no `.py` file under `verifiers/` whose
    stem is a member of sys.stdlib_module_names.  Such a file could shadow a
    module the delegate imports, so the box does not count and the line says
    which file shadows what.  (This closes the round-55 `verifiers/argparse.py`
    class, where a planted shadow captured the instrument's own imports.)
    The archive covers `verifiers/` plus the delegated script's own path when
    that path lives outside `verifiers/`; nothing else of the revision is
    read.
(d) Discrimination.  For every case the counter generates at run time for
    that box, the delegate

        python3 -B -P <tmp tree>/<path> --check <box> --target <case dir> --json

    run with cwd = a fresh empty temp dir, with PYTHONPATH, PYTHONHOME and
    PYTHONSTARTUP removed from the environment and PYTHONSAFEPATH=1 set, with
    a 20 s timeout, exits 0 and prints a JSON `checks` list holding the entry
    {"id": <box>, "status": "PASS"} when the case expects PASS, and exits 1
    with that entry's status "FAIL" when the case expects FAIL.  Any other
    exit code, a missing entry for the box, unparseable JSON, or a timeout
    makes the box not count.  `-P` (equivalent to PYTHONSAFEPATH) keeps the
    delegate's own directory off its import path.

THE OPERATIONAL READING OF EACH BOX (the rule the instrument is judged by)
------------------------------------------------------------------------
The counter does not score claim content; it scores whether a delegate can
tell these five boxes apart.  The reading below is the contract: an
instrument that implements it exactly passes every generated case.

Common file shape.  A case directory holds one or more agent definition
files at `agents/<stem>.md` and, when the box needs a roster artifact, an
`opencode.json` at the case directory root.  An agent file is a YAML
frontmatter block -- a first line `---`, then `key: value` lines, then a
closing `---` -- followed by the body (the remaining lines).  The
frontmatter keys the reading uses are `name` (the agent's declared name) and
`subagents` (a roster of further agent names; given either as a YAML block
sequence of `  - name` lines or as a comma separated inline list).  The body
is everything after the closing `---`.

agentdef.01 -- `name` matches the file stem.
  Let the agent files of the case directory be A.  For a file f with stem s:
  f is defective when (i) it declares `name:` and the declared name differs
  from s; or (ii) it does not declare `name:` and the sibling set of f -- the
  other agent files of the same directory -- is non-empty and every sibling
  declares a `name:`.  Clause (ii) is the box's "absent `name:` fails latent"
  clause: opencode falls back to the stem, so the defect only bites when the
  roster is otherwise consistent.  The box PASSES iff no file of A is
  defective.  A file whose declared name equals its stem PASSES even when
  every sibling also declares a name.

agentdef.02 -- reachability.
  `opencode.json` is a JSON object; its `agent` map is the object under the
  top level key `agent`, whose keys are the enrolled agent names.  An agent
  file is identified by its declared `name:` when it declares one and by its
  file stem otherwise.  The enrolled set is the identifiers that appear as
  keys of the `agent` map.  Reachability is the least fixed point of: an
  identifier is reachable if it is enrolled, and if an identifier is
  reachable then every name listed in that agent file's `subagents:` roster
  is reachable.  The box PASSES iff every agent file of the case directory
  is reachable, and FAILS iff some agent file is an orphan -- enrolled
  nowhere and named by no reachable agent.  An agent that is enrolled in no
  map but is listed in the `subagents:` roster of a reachable agent IS
  reachable and the box PASSES.

agentdef.05 -- no dated operational text in the frontmatter.
  The frontmatter block of every agent file of the case directory is scanned
  (the body is NOT scanned: a dated body anecdote is this box's business
  nowhere, and a date in the body alone must PASS).  The frontmatter is
  DEFECTIVE when it contains any of:
    * an ISO calendar date, `YYYY-MM-DD` (this also covers an ISO
      timestamp such as `2026-10-22T19:37Z`);
    * a month-name date, `Month D` or `D Month` ("November 1", "1 November");
    * a round index: `round 12`, `round-12`, `round #12` (any case), or the
      phrase `PROPOSE round`.
  A version number such as `3.12` is NOT a date and does not make the box
  fail.  The box PASSES iff no frontmatter of the case directory is
  defective.

agentdef.06 -- the body is persistent identity, not per-task job text.
  The body of every agent file of the case directory is scanned (the
  frontmatter is not).  The body is DEFECTIVE when it contains any of:
    * the phrase `your current task` (any case);
    * a round index: `round 12`, `round-12`, `round #12` (any case);
    * a one-shot instruction: `one-shot`, `once only`, `only this once`,
      `for this task only`, `this time only`, `just this once` (any case).
  The bare word `task` is not a defect: only the phrase `your current task`
  is.  The box PASSES iff no body of the case directory is defective.

agentdef.07 -- no duplicated blocks in the body.
  The body of every agent file of the case directory is split into
  paragraphs -- maximal runs of consecutive non-blank lines -- and into
  sections -- a heading line (`#`..`######` plus a title) opens a section
  whose name is the heading title, and the text before the first heading is
  an unnamed section.  A paragraph is normalised by collapsing its internal
  whitespace runs to single spaces.  The body is DEFECTIVE when
    * two distinct paragraphs of the body normalise to the same text and
      that text is at least 40 characters long (a repeated short line such as
      `- yes` or `---` is not a duplicated block and does not make the body
      defective); or
    * two sections carry the same name and their contents differ (a
      conflicting near-duplicate is a conflict defect, not a pass).
  The box PASSES iff no body of the case directory is defective.

THE OTHER FOUR BOXES
---------------------
Case generators exist for agentdef.01, .02, .05, .06 and .07 only.
agentdef.03, .04, .08 and .09 have no generator, so they can never count and
their line says so.  They are still listed in the output, because T counts
every box of the section.

CASE GENERATION (run time, never pinned)
-----------------------------------------
Every run generates, for each of the five generated boxes, at least four PASS
cases and at least four FAIL cases.  The stems, agent names, filler words,
dates, timestamps, version numbers and round indices are drawn from a
`random.Random` seeded with a seed that is itself drawn from `secrets` and
printed on the last output line, so a run is reproducible from its seed but
unpredictable before it.

Case directory names are random hex and leak no expectation.  The PASS and
the FAIL member of a twin live in directories with the SAME random-hex base
name under different random-hex parents, and carry the same agent file names:
a delegate that keys its answer on the case directory name or on the file
names cannot tell the twin pair apart, so it necessarily answers one of the
two wrongly and the box cannot count.  Only the content of the case
distinguishes a twin pair, and the content differs only in the defect the box
reads.

Each PASS case has a FAIL twin that differs only in that defect, and the
twin pair is of similar size.  Every box also carries at least one
hard-negative PASS case -- a case a plausible but wrong reading would fail:

  agentdef.01  a file whose declared name equals its stem while every
               sibling also declares a name;
  agentdef.02  an agent reached only through another enrolled agent's
               `subagents:` roster;
  agentdef.05  a date in the body only (the box reads the frontmatter
               only), and a version number such as `3.12` in the
               description;
  agentdef.06  the bare word `task` inside a stable constraint sentence;
  agentdef.07  a repeated short line under 40 characters (`- yes`), which
               is not a duplicated block.

INSTRUMENT CONTRACT AND TRUST BOUNDARY
--------------------------------------
The counter runs the delegate of the revision under measurement, from a
fresh extraction of that revision, over cases the counter makes itself, in
an isolated interpreter: `-B` (no bytecode), `-P` and PYTHONSAFEPATH=1 (the
script's directory is not on the import path), PYTHONPATH/PYTHONHOME/
PYTHONSTARTUP removed, a fresh empty working directory, and a 20 s timeout
per case.  The counter never reads the working tree: it reads <rev> only
through `git show`, `git ls-tree` and `git archive`, with GIT_OPTIONAL_LOCKS
set so that no git command writes to the lane's index.  The counter also
removes its own directory from sys.path at start-up, so that a
standard-library shadow planted beside the counter cannot capture the
counter's own imports.

The counter is the instrument that measures; the delegate is the instrument
that is measured.  A delegate that always answers PASS, always answers FAIL,
ignores `--target`, remaps a real finding onto exit 2, keys its answer on the
case directory or file names, or never opens the target, scores zero boxes:
the counter's own `--self-test` proves each of those.

OUTPUT
------
The first output line is exactly

    agent-definition boxes executed and discriminating N of T

followed by one line per box of the section (`counted` with the case tally,
or `not counted` with the reason), followed by the seed used.  Exit 0 iff
N >= 3, exit 1 otherwise, exit 2 when the revision could not be evaluated at
all (unknown revision, git failure, unreadable map).

FROZEN PREDICATE
----------------
    python3 -B verifiers/check_agentdef_boxes.py --rev <rev>

exits 0 iff it prints `agent-definition boxes executed and discriminating N of
T` with N >= 3.  Receipt label: `C2 predicate: exit 0 (N>=3)`.
"""
from __future__ import annotations

import sys

# A standard-library shadow planted beside this script (the round-55
# `verifiers/argparse.py` class) would capture the counter's own imports.
# The script's own directory is removed from sys.path before anything else is
# imported.  `sys` itself is a built-in and cannot be shadowed.
try:
    import os as _os

    _HERE = _os.path.dirname(_os.path.realpath(__file__))
    sys.path[:] = [p for p in sys.path
                   if p not in ("", ".", _HERE)
                   and _os.path.realpath(p or ".") != _HERE]
except Exception:  # pragma: no cover - defensive only
    pass

import argparse
import json
import os
import random
import re
import secrets
import shutil
import subprocess
import tarfile
import tempfile
import time
from pathlib import Path

BASE_REV = "b0b7140b5a7cf8a50f13989ee6285fc8ee245c41"
SECTION = "Agent-definition fidelity checklist"
TIMEOUT = 20
MIN_COUNT = 3
TOTAL_BUDGET = 240.0

# The boxes this counter generates cases for.  The other four boxes of the
# section have no generator and can never count.
GENERATED_BOXES = ("agentdef.01", "agentdef.02", "agentdef.05", "agentdef.06",
                   "agentdef.07")

# BASE_REV's map values for the nine agent-definition boxes.  A box whose
# text_sha256 differs at the measured revision was reworded and does not
# count.
PINNED_BOX_SHA = {
    "agentdef.01": "c2fee506851ae855ac201f5bec09955f064d89fab1cba1a0a95cfe64f347d46b",
    "agentdef.02": "f90776ef64ec17c57f39be671f4ca0e12eb71f1980a4182beff53f96cb58e158",
    "agentdef.03": "56e05a00051f3ea871c178232bc75f58a63866cb9d96c7c7a63f985837eec05d",
    "agentdef.04": "ce7d6d18ec120534e9daec593a621b9de372a077fe256b6b5042b8be6d2a4928",
    "agentdef.05": "bc080391481eea0ba684fc895b2476e9da855cee2b9b95f72b029ca5edd94ca8",
    "agentdef.06": "aaf30b111cfa191a092cc0f30e76bbb67434fbade34888522b3dc3ac76c049e6",
    "agentdef.07": "918a8c986f60be26339624ef5b2355682d0b8719deebb90aea4479735a5a3943",
    "agentdef.08": "a1431bc75aeb2401cc3336937d72eda8c28116d2a7a42c920cd5ef392a8392d9",
    "agentdef.09": "ca2257a57b9df92898bf1eeac4be3b8ed3331e3251af3e4e5f8c277fd235f06a",
}

WORDS = (
    "quill", "harbor", "lantern", "beacon", "ember", "cobalt", "thicket",
    "marrow", "saffron", "cinder", "onyx", "vellum", "juniper", "basalt",
    "kestrel", "moss", "drift", "plinth", "tallow", "nimbus", "ochre",
    "rundle", "sable", "teasel", "umber", "verge", "whinchat", "xenon",
    "yarrow", "zephyr", "bracken", "cobble",
)

SURFACES = ("ingestion", "ledger", "registry", "dispatch", "provenance",
            "capacity", "coverage", "lineage")

ROLES = ("keeper", "scribe", "warden", "weaver", "binder", "usher", "broker")

DESCRIPTIONS = (
    "Handles the {surface} surface for the orchestrator.",
    "Owns the {surface} roster and its entries.",
    "Reviews the {surface} surface for the lane owner.",
)

BODY_TEMPLATE = """You are the {role} for the {surface} surface.

## Responsibilities

- Keep the {surface} roster current.
- Record every decision with its source.

## Constraints

- Do not edit files outside the assigned surface.
- Leave the workspace unchanged unless asked."""

DUP_PARAGRAPH = ("- Every entry names the artifact it describes.\n"
                 "- Entries stay in the order they were accepted.")
DUP_PARAGRAPH_ALT = ("- Every entry names the artifact it indexes.\n"
                     "- Entries stay in the order they were accepted.")
LEDGER_PARAGRAPH = "- Record each accepted entry in the shared surface ledger."
CLOSE_PARAGRAPH = "- Summarize the accepted entries in the closing note."


# --------------------------------------------------------------------------
# git helpers (read-only; GIT_OPTIONAL_LOCKS keeps the lane's index alone)
# --------------------------------------------------------------------------

def git(repo: Path, *args: str, check: bool = True) -> bytes:
    env = dict(os.environ)
    env["GIT_OPTIONAL_LOCKS"] = "0"
    proc = subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          env=env, timeout=120)
    if check and proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, args,
                                            proc.stdout, proc.stderr)
    return proc.stdout


def git_text(repo: Path, *args: str, check: bool = True) -> str:
    return git(repo, *args, check=check).decode("utf-8", "replace")


def lane_default() -> Path:
    """The lane repository: the parent of this script's `verifiers/` dir."""
    here = Path(__file__).resolve().parent
    if here.name == "verifiers":
        return here.parent
    return here


# --------------------------------------------------------------------------
# case model
# --------------------------------------------------------------------------

class Case:
    """One generated case.  `group` names the twin pair it belongs to."""

    __slots__ = ("box", "label", "group", "files", "expect")

    def __init__(self, box: str, label: str, group: str, files: dict[str, str],
                 expect: str) -> None:
        self.box = box
        self.label = label
        self.group = group
        self.files = files
        self.expect = expect


class StemPool:
    """Distinct agent stems drawn from the seeded generator."""

    def __init__(self, rng: random.Random) -> None:
        self._rng = rng
        self._used: set[str] = set()

    def next(self) -> str:
        while True:
            stem = "%s-%s" % (self._rng.choice(WORDS), self._rng.choice(WORDS))
            if stem not in self._used:
                self._used.add(stem)
                return stem

    def other(self, avoid: str) -> str:
        while True:
            stem = "%s-%s" % (self._rng.choice(WORDS), self._rng.choice(WORDS))
            if stem != avoid and stem not in self._used:
                self._used.add(stem)
                return stem


def agent_doc(stem: str, name: str | None, description: str,
              body: str, subagents: list[str] | None = None,
              extra_front: list[str] | None = None) -> str:
    front = ["---"]
    if name is not None:
        front.append("name: " + name)
    front.append("description: " + description)
    if extra_front:
        front.extend(extra_front)
    if subagents:
        front.append("subagents:")
        front.extend("  - " + s for s in subagents)
    front.append("---")
    return "\n".join(front) + "\n\n" + body.strip("\n") + "\n"


def standard_body(rng: random.Random, extra: list[str] | None = None) -> str:
    body = BODY_TEMPLATE.format(role=rng.choice(ROLES),
                                surface=rng.choice(SURFACES))
    if extra:
        body = body + "\n" + "\n".join(extra)
    return body


def roster_json(names: list[str], with_agent_key: bool = True) -> str:
    if not with_agent_key:
        payload = {"theme": "reference"}
    else:
        payload = {"agent": {n: {"description": "Enrolled agent %s." % n}
                             for n in names}}
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def pick_date(rng: random.Random) -> str:
    """A random ISO calendar date in 2025..2027."""
    return "%04d-%02d-%02d" % (rng.choice((2025, 2026, 2027)),
                               rng.randint(1, 12), rng.randint(1, 28))


def pick_timestamp(rng: random.Random) -> str:
    return "%sT%02d:%02dZ" % (pick_date(rng), rng.randint(0, 23),
                              rng.randint(0, 59))


def pick_version(rng: random.Random) -> str:
    return "%d.%d" % (rng.randint(1, 9), rng.randint(1, 20))


def pick_round(rng: random.Random) -> int:
    return rng.randint(2, 99)


# --------------------------------------------------------------------------
# case generators, one per generated box
# --------------------------------------------------------------------------

def cases_agentdef_01(rng: random.Random, stems: StemPool) -> list[Case]:
    out: list[Case] = []
    desc = rng.choice(DESCRIPTIONS).format(surface=rng.choice(SURFACES))

    # F1: one file, declared name equal to the stem (PASS) / different (FAIL).
    s = stems.next()
    other = stems.other(s)
    body = standard_body(rng)
    out.append(Case("agentdef.01", "f1-name-matches-stem", "g1",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, body)}, "PASS"))
    out.append(Case("agentdef.01", "f1-name-differs-from-stem", "g1",
                    {"agents/%s.md" % s: agent_doc(s, other, desc, body)}, "FAIL"))

    # F2: target and a sibling that both declare a name; the target's name is
    # absent in the FAIL member, which is the box's latent-defect clause.
    t = stems.next()
    g = stems.next()
    out.append(Case("agentdef.01", "f2-sibling-roster-consistent", "g2",
                    {"agents/%s.md" % t: agent_doc(t, t, desc, body),
                     "agents/%s.md" % g: agent_doc(g, g, desc, body)}, "PASS"))
    out.append(Case("agentdef.01", "f2-absent-name-with-declaring-sibling", "g2",
                    {"agents/%s.md" % t: agent_doc(t, None, desc, body),
                     "agents/%s.md" % g: agent_doc(g, g, desc, body)}, "FAIL"))

    # F3: neither file declares a name (PASS); the sibling does (FAIL).
    t = stems.next()
    g = stems.next()
    out.append(Case("agentdef.01", "f3-no-name-anywhere", "g3",
                    {"agents/%s.md" % t: agent_doc(t, None, desc, body),
                     "agents/%s.md" % g: agent_doc(g, None, desc, body)}, "PASS"))
    out.append(Case("agentdef.01", "f3-sibling-declares-name", "g3",
                    {"agents/%s.md" % t: agent_doc(t, None, desc, body),
                     "agents/%s.md" % g: agent_doc(g, g, desc, body)}, "FAIL"))

    # F4: three files, all declaring matching names (PASS); one mismatched
    # (FAIL).
    t = stems.next()
    g1 = stems.next()
    g2 = stems.next()
    out.append(Case("agentdef.01", "f4-three-consistent-names", "g4",
                    {"agents/%s.md" % t: agent_doc(t, t, desc, body),
                     "agents/%s.md" % g1: agent_doc(g1, g1, desc, body),
                     "agents/%s.md" % g2: agent_doc(g2, g2, desc, body)}, "PASS"))
    out.append(Case("agentdef.01", "f4-one-mismatched-name", "g4",
                    {"agents/%s.md" % t: agent_doc(t, t, desc, body),
                     "agents/%s.md" % g1: agent_doc(g1, g1, desc, body),
                     "agents/%s.md" % g2: agent_doc(g2, other, desc, body)},
                    "FAIL"))
    return out


def cases_agentdef_02(rng: random.Random, stems: StemPool) -> list[Case]:
    out: list[Case] = []
    desc = rng.choice(DESCRIPTIONS).format(surface=rng.choice(SURFACES))
    body = standard_body(rng)

    # F1: enrolled in the agent map (PASS) / not enrolled (FAIL).
    s = stems.next()
    out.append(Case("agentdef.02", "f1-enrolled-in-agent-map", "g1",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, body),
                     "opencode.json": roster_json([s])}, "PASS"))
    out.append(Case("agentdef.02", "f1-orphan-not-enrolled", "g1",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, body),
                     "opencode.json": roster_json([])}, "FAIL"))

    # F2: a child reached only through the enrolled parent's subagents roster
    # (PASS) / the parent names no subagent (FAIL).
    p = stems.next()
    c = stems.next()
    out.append(Case("agentdef.02", "f2-child-reached-via-subagents", "g2",
                    {"agents/%s.md" % p: agent_doc(p, p, desc, body,
                                                   subagents=[c]),
                     "agents/%s.md" % c: agent_doc(c, c, desc, body),
                     "opencode.json": roster_json([p])}, "PASS"))
    out.append(Case("agentdef.02", "f2-parent-names-no-subagent", "g2",
                    {"agents/%s.md" % p: agent_doc(p, p, desc, body),
                     "agents/%s.md" % c: agent_doc(c, c, desc, body),
                     "opencode.json": roster_json([p])}, "FAIL"))

    # F3: the parent is not enrolled, so its roster reaches nobody (FAIL);
    # enrolling the parent makes the child reachable (PASS).
    p = stems.next()
    c = stems.next()
    out.append(Case("agentdef.02", "f3-unreachable-parent-roster", "g3",
                    {"agents/%s.md" % p: agent_doc(p, p, desc, body,
                                                   subagents=[c]),
                     "agents/%s.md" % c: agent_doc(c, c, desc, body),
                     "opencode.json": roster_json([])}, "FAIL"))
    out.append(Case("agentdef.02", "f3-enrolled-parent-roster", "g3",
                    {"agents/%s.md" % p: agent_doc(p, p, desc, body,
                                                   subagents=[c]),
                     "agents/%s.md" % c: agent_doc(c, c, desc, body),
                     "opencode.json": roster_json([p])}, "PASS"))

    # F4: two agents, both enrolled (PASS) / one of them not (FAIL).
    a = stems.next()
    b = stems.next()
    out.append(Case("agentdef.02", "f4-both-enrolled", "g4",
                    {"agents/%s.md" % a: agent_doc(a, a, desc, body),
                     "agents/%s.md" % b: agent_doc(b, b, desc, body),
                     "opencode.json": roster_json([a, b])}, "PASS"))
    out.append(Case("agentdef.02", "f4-second-agent-orphan", "g4",
                    {"agents/%s.md" % a: agent_doc(a, a, desc, body),
                     "agents/%s.md" % b: agent_doc(b, b, desc, body),
                     "opencode.json": roster_json([a])}, "FAIL"))

    # F5: no agent map at all (FAIL) / the agent map present (PASS).
    s = stems.next()
    out.append(Case("agentdef.02", "f5-roster-without-agent-map", "g5",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, body),
                     "opencode.json": roster_json([], with_agent_key=False)},
                    "FAIL"))
    out.append(Case("agentdef.02", "f5-roster-with-agent-map", "g5",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, body),
                     "opencode.json": roster_json([s])}, "PASS"))
    return out


def cases_agentdef_05(rng: random.Random, stems: StemPool) -> list[Case]:
    out: list[Case] = []
    surface = rng.choice(SURFACES)
    desc = rng.choice(DESCRIPTIONS).format(surface=surface)
    body = standard_body(rng)
    date_a = pick_date(rng)
    date_b = pick_date(rng)
    version = pick_version(rng)
    dated_body = body + "\n\nThe lane shipped a fix on %s." % date_a

    # F1: a date in the description (FAIL) / no date (PASS).
    s = stems.next()
    out.append(Case("agentdef.05", "f1-description-without-date", "g1",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, body)}, "PASS"))
    out.append(Case("agentdef.05", "f1-description-with-date", "g1",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc + " Until %s, keep the old reader." % date_a,
                        body)}, "FAIL"))

    # F2: a version number in the description is not a date (PASS) / the same
    # description carrying a date is (FAIL).  The hard negative of this box:
    # the version is not a date.
    s = stems.next()
    out.append(Case("agentdef.05", "f2-version-number-not-a-date", "g2",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc + " The reader needs schema %s." % version,
                        body)}, "PASS"))
    out.append(Case("agentdef.05", "f2-description-with-a-date", "g2",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc + " The reader needs schema %s." % date_b,
                        body)}, "FAIL"))

    # F3: a round-indexed routing note (FAIL) / a neutral cadence (PASS).
    s = stems.next()
    out.append(Case("agentdef.05", "f3-neutral-cadence", "g3",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, "Mandatory every handover cycle for the %s surface."
                        % surface, body)}, "PASS"))
    out.append(Case("agentdef.05", "f3-round-indexed-routing-note", "g3",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, "Mandatory every PROPOSE round for the %s surface."
                        % surface, body)}, "FAIL"))

    # F4: a date in the body only (PASS) / the same date in the description
    # (FAIL).  The hard negative of this box: the box reads the frontmatter
    # only, so a dated body anecdote passes.
    s = stems.next()
    out.append(Case("agentdef.05", "f4-date-in-body-only", "g4",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, dated_body)},
                    "PASS"))
    out.append(Case("agentdef.05", "f4-date-moved-into-description", "g4",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc + " The lane shipped a fix on %s." % date_a,
                        body)}, "FAIL"))

    # F5: a dated frontmatter key (FAIL) / a version number in the same key
    # (PASS).
    s = stems.next()
    out.append(Case("agentdef.05", "f5-frontmatter-version-not-a-date", "g5",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, body,
                                                   extra_front=["updated: %s" % version])},
                    "PASS"))
    out.append(Case("agentdef.05", "f5-frontmatter-timestamp", "g5",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, body,
                                                   extra_front=["updated: %s" % pick_timestamp(rng)])},
                    "FAIL"))
    return out


def cases_agentdef_06(rng: random.Random, stems: StemPool) -> list[Case]:
    out: list[Case] = []
    desc = rng.choice(DESCRIPTIONS).format(surface=rng.choice(SURFACES))
    body = standard_body(rng)
    surface = rng.choice(SURFACES)
    round_index = pick_round(rng)

    # F1: `your current task` (FAIL) / the standing duty (PASS).
    s = stems.next()
    out.append(Case("agentdef.06", "f1-standing-duty", "g1",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        body + "\n\nYour standing duty is to refresh the %s roster."
                        % surface)}, "PASS"))
    out.append(Case("agentdef.06", "f1-current-task-phrase", "g1",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        body + "\n\nYour current task is to refresh the %s roster."
                        % surface)}, "FAIL"))

    # F2: a round number (FAIL) / a handover (PASS).
    s = stems.next()
    out.append(Case("agentdef.06", "f2-handover-cadence", "g2",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        body + "\n\nAt every handover, refresh the %s roster."
                        % surface)}, "PASS"))
    out.append(Case("agentdef.06", "f2-round-number", "g2",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        body + "\n\nIn round %d, refresh the %s roster."
                        % (round_index, surface))}, "FAIL"))

    # F3: a one-shot instruction (FAIL) / a standing task (PASS).
    s = stems.next()
    out.append(Case("agentdef.06", "f3-standing-task", "g3",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        body + "\n\nThis is a standing task: sweep the %s queue each cycle."
                        % surface)}, "PASS"))
    out.append(Case("agentdef.06", "f3-one-shot-instruction", "g3",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        body + "\n\nThis is a one-shot task: sweep the %s queue once."
                        % surface)}, "FAIL"))

    # F4: the bare word `task` in a stable constraint (PASS) / the same
    # sentence plus a current-task line (FAIL).  The hard negative of this
    # box: only the phrase `your current task` is a defect, not `task`.
    s = stems.next()
    stable = body + "\n- Keep one task per commit."
    out.append(Case("agentdef.06", "f4-bare-word-task", "g4",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, stable)}, "PASS"))
    out.append(Case("agentdef.06", "f4-task-word-plus-current-task", "g4",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc, stable + "\n\nYour current task: fix the %s build."
                        % surface)}, "FAIL"))
    return out


def cases_agentdef_07(rng: random.Random, stems: StemPool) -> list[Case]:
    out: list[Case] = []
    desc = rng.choice(DESCRIPTIONS).format(surface=rng.choice(SURFACES))

    # F1: the same paragraph twice (FAIL) / a distinct second paragraph
    # (PASS).
    s = stems.next()
    out.append(Case("agentdef.07", "f1-paragraph-not-duplicated", "g1",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        "You are the keeper for the lineage surface.\n\n"
                        "## Register\n\n%s\n\n## Seal\n\n%s"
                        % (DUP_PARAGRAPH, DUP_PARAGRAPH_ALT))}, "PASS"))
    out.append(Case("agentdef.07", "f1-paragraph-duplicated", "g1",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        "You are the keeper for the lineage surface.\n\n"
                        "## Register\n\n%s\n\n## Seal\n\n%s"
                        % (DUP_PARAGRAPH, DUP_PARAGRAPH))}, "FAIL"))

    # F2: two sections of the same name with differing content (FAIL) / the
    # second renamed (PASS).
    s = stems.next()
    out.append(Case("agentdef.07", "f2-distinct-section-names", "g2",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        "You are the keeper for the lineage surface.\n\n"
                        "## DESPAWN\n\n- Record the handoff together with its reason.\n\n"
                        "## RESPAWN\n\n- Record the handoff together with its owner.")},
                    "PASS"))
    out.append(Case("agentdef.07", "f2-same-section-name-different-content", "g2",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        "You are the keeper for the lineage surface.\n\n"
                        "## DESPAWN\n\n- Record the handoff together with its reason.\n\n"
                        "## DESPAWN\n\n- Record the handoff together with its owner.")},
                    "FAIL"))

    # F3: a repeated short line is not a duplicated block (PASS); the same
    # body plus a repeated long paragraph is (FAIL).
    s = stems.next()
    short_repeat = ("You are the keeper for the lineage surface.\n\n"
                    "## Loop\n\n- yes\n\n## Ledger\n\n%s\n\n- yes\n\n"
                    "## Close\n\n%s" % (LEDGER_PARAGRAPH, CLOSE_PARAGRAPH))
    out.append(Case("agentdef.07", "f3-repeated-short-line", "g3",
                    {"agents/%s.md" % s: agent_doc(s, s, desc, short_repeat)},
                    "PASS"))
    out.append(Case("agentdef.07", "f3-repeated-long-paragraph", "g3",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        short_repeat + "\n\n" + LEDGER_PARAGRAPH)}, "FAIL"))

    # F4: three sections with distinct paragraphs (PASS) / the third repeats
    # the first (FAIL).
    s = stems.next()
    out.append(Case("agentdef.07", "f4-distinct-sections", "g4",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        "You are the keeper for the lineage surface.\n\n"
                        "## Intake\n\n%s\n\n## Register\n\n"
                        "- Note the artifact that each entry describes.\n\n"
                        "## Close\n\n%s" % (LEDGER_PARAGRAPH, CLOSE_PARAGRAPH))},
                    "PASS"))
    out.append(Case("agentdef.07", "f4-third-section-repeats-first", "g4",
                    {"agents/%s.md" % s: agent_doc(
                        s, s, desc,
                        "You are the keeper for the lineage surface.\n\n"
                        "## Intake\n\n%s\n\n## Register\n\n"
                        "- Note the artifact that each entry describes.\n\n"
                        "## Close\n\n%s" % (LEDGER_PARAGRAPH, LEDGER_PARAGRAPH))},
                    "FAIL"))
    return out


GENERATORS = {
    "agentdef.01": cases_agentdef_01,
    "agentdef.02": cases_agentdef_02,
    "agentdef.05": cases_agentdef_05,
    "agentdef.06": cases_agentdef_06,
    "agentdef.07": cases_agentdef_07,
}


def build_cases(rng: random.Random) -> dict[str, list[Case]]:
    stems = StemPool(rng)
    out: dict[str, list[Case]] = {}
    for box in GENERATED_BOXES:
        out[box] = GENERATORS[box](rng, stems)
    return out


# --------------------------------------------------------------------------
# running the delegate
# --------------------------------------------------------------------------

def delegate_env() -> dict[str, str]:
    env = dict(os.environ)
    for name in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP"):
        env.pop(name, None)
    env["PYTHONSAFEPATH"] = "1"
    env["GIT_OPTIONAL_LOCKS"] = "0"
    return env


def run_case(script: Path, box: str, target: Path, expect: str,
             cwd: Path) -> tuple[bool, str]:
    """Run the delegate over one case.  Returns (as_expected, observed)."""
    try:
        proc = subprocess.run(
            [sys.executable, "-B", "-P", str(script), "--check", box,
             "--target", str(target), "--json"],
            capture_output=True, text=True, timeout=TIMEOUT, env=delegate_env(),
            cwd=str(cwd))
    except subprocess.TimeoutExpired:
        return False, "timeout after %ds" % TIMEOUT
    except OSError as exc:
        return False, "could not run delegate: %s" % exc
    try:
        payload = json.loads(proc.stdout)
    except (json.JSONDecodeError, TypeError, ValueError):
        return False, "exit %d, unparseable JSON" % proc.returncode
    if not isinstance(payload, dict):
        return False, "exit %d, JSON is not an object" % proc.returncode
    entries = payload.get("checks")
    if not isinstance(entries, list):
        return False, "exit %d, no checks list" % proc.returncode
    statuses = []
    for entry in entries:
        if isinstance(entry, dict) and entry.get("id") == box:
            statuses.append(entry.get("status"))
    if not statuses:
        return False, "exit %d, no checks entry for %s" % (proc.returncode, box)
    want_rc = 0 if expect == "PASS" else 1
    ok = proc.returncode == want_rc and all(s == expect for s in statuses)
    return ok, "exit %d, status %s" % (proc.returncode,
                                       "/".join(map(str, statuses)))


# --------------------------------------------------------------------------
# the measurement
# --------------------------------------------------------------------------

def extract_tree(repo: Path, rev: str, dest: Path,
                 paths: list[str]) -> None:
    """Extract the revision's `verifiers/` tree (and the delegated path) into
    dest.

    Only the paths the measurement needs are archived: `verifiers/` for the
    standard-library shadow scan, plus the delegated script's own path when it
    lives outside `verifiers/`.  The whole tree is not archived: it carries
    absolute symlinks under `.ufo/` that a safe extraction refuses, and the
    measurement reads nothing else.
    """
    env = dict(os.environ)
    env["GIT_OPTIONAL_LOCKS"] = "0"
    proc = subprocess.Popen(["git", "-C", str(repo), "archive", "--format=tar",
                              rev, "--"] + paths,
                            stdout=subprocess.PIPE, env=env)
    try:
        with tarfile.open(fileobj=proc.stdout, mode="r|") as tar:
            try:
                tar.extractall(dest, filter="data")
            except TypeError:  # pragma: no cover - Python < 3.12
                tar.extractall(dest)
    finally:
        if proc.stdout is not None:
            proc.stdout.close()
        rc = proc.wait()
    if rc != 0:
        raise subprocess.CalledProcessError(rc, ["git", "archive", rev])


def stdlib_shadows(tree: Path) -> list[str]:
    """verifiers/*.py whose stem shadows a standard-library module."""
    found = []
    verifiers = tree / "verifiers"
    if not verifiers.is_dir():
        return found
    stdlib = getattr(sys, "stdlib_module_names", ())
    for path in sorted(verifiers.rglob("*.py")):
        stem = path.stem
        if stem in stdlib:
            found.append(str(path.relative_to(tree)))
    return found


def map_boxes(repo: Path, rev: str) -> list[dict]:
    raw = git(repo, "show", "%s:verifiers/checklist-baseline.json" % rev)
    data = json.loads(raw.decode("utf-8"))
    boxes = data["boxes"]
    if not isinstance(boxes, list):
        raise ValueError("map has no boxes list")
    return boxes


def section_boxes(repo: Path, rev: str) -> list[dict]:
    return [b for b in map_boxes(repo, rev) if b.get("section") == SECTION]


def delegated_path(box: dict) -> tuple[str | None, str | None]:
    """Return (path, reason) for a box's delegation."""
    disposition = box.get("disposition")
    if not isinstance(disposition, str) or not disposition:
        return None, "no disposition"
    if not disposition.startswith("delegated:"):
        kind = disposition.split(":", 1)[0] or disposition
        return None, "disposition is %s, not delegated" % kind
    path = disposition.split(":", 1)[1].strip()
    if not path:
        return None, "delegated path is empty"
    if path.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", path):
        return None, "delegated path is absolute: %s" % path
    if ".." in Path(path).parts:
        return None, "delegated path escapes the repository: %s" % path
    return path, None


def path_exists(repo: Path, rev: str, path: str) -> bool:
    out = git_text(repo, "ls-tree", rev, "--", path)
    for line in out.splitlines():
        meta, _, name = line.partition("\t")
        fields = meta.split()
        if len(fields) >= 3 and fields[1] == "blob" and name == path:
            return True
    return False


def evaluate(repo: Path, rev: str, seed: str) -> tuple[int, list[str], str]:
    """Measure the revision.  Returns (exit code, output lines, first line)."""
    boxes = section_boxes(repo, rev)
    total = len(boxes)
    rng = random.Random(seed)
    cases = build_cases(rng)
    lines: list[str] = []
    counted = 0
    started = time.monotonic()
    # One random-hex base name per twin pair: the PASS and the FAIL member of
    # a pair share it, so a delegate that keys its answer on the case
    # directory name answers both members alike and is wrong on one of them.
    group_base: dict[str, str] = {}

    # Pass 1 -- conditions (a) and (b), which need no tree.
    pending: list[tuple[str, str]] = []   # (box id, delegated path)
    for box in boxes:
        box_id = box.get("box_id") or "<unnamed>"
        if box_id not in GENERATED_BOXES:
            lines.append("  %s: not counted (no case generator for this box: "
                         "this counter generates cases for %s)"
                         % (box_id, ", ".join(GENERATED_BOXES)))
            continue
        path, reason = delegated_path(box)
        if path is None:
            lines.append("  %s: not counted (%s)" % (box_id, reason))
            continue
        if not path_exists(repo, rev, path):
            lines.append("  %s: not counted (delegated path %s is absent at "
                         "the revision)" % (box_id, path))
            continue
        pinned = PINNED_BOX_SHA.get(box_id)
        if pinned is None:
            lines.append("  %s: not counted (no pinned base sha for this "
                         "box id)" % box_id)
            continue
        if box.get("text_sha256") != pinned:
            lines.append("  %s: not counted (box text was reworded at this "
                         "revision)" % box_id)
            continue
        pending.append((box_id, path))

    if not pending:
        header = "agent-definition boxes executed and discriminating %d of %d" % (
            counted, total)
        return (0 if counted >= MIN_COUNT else 1), [header] + lines, header

    # Pass 2 -- condition (c): the shadow scan needs the revision's tree.
    tree = Path(tempfile.mkdtemp(prefix="agentdef-tree-"))
    try:
        paths = {"verifiers"}
        for _box_id, path in pending:
            if not path.startswith("verifiers/"):
                paths.add(path)
        try:
            extract_tree(repo, rev, tree, sorted(paths))
        except (OSError, subprocess.CalledProcessError, tarfile.TarError) as exc:
            for box_id, _path in pending:
                lines.append("  %s: not counted (could not extract the "
                             "revision tree: %s)" % (box_id, exc))
            header = "agent-definition boxes executed and discriminating %d of %d" % (
                counted, total)
            return (0 if counted >= MIN_COUNT else 1), [header] + lines, header
        shadows = stdlib_shadows(tree)

        # Pass 3 -- conditions (c) and (d).
        for box_id, path in pending:
            if shadows:
                lines.append("  %s: not counted (stdlib shadow under verifiers/: "
                             "%s)" % (box_id, ", ".join(shadows)))
                continue
            script = tree / path
            if not script.is_file():
                lines.append("  %s: not counted (delegated path %s is not a file "
                             "in the revision tree)" % (box_id, path))
                continue
            bad: list[str] = []
            total_cases = 0
            workdir = Path(tempfile.mkdtemp(prefix="agentdef-cases-"))
            try:
                for case in cases[box_id]:
                    if time.monotonic() - started > TOTAL_BUDGET:
                        bad.append("run budget exhausted before %s" % case.label)
                        break
                    total_cases += 1
                    # The twin pair shares its base name; only the random
                    # parent differs, so a name-keyed delegate cannot tell the
                    # two members apart.
                    key = "%s/%s" % (case.box, case.group)
                    if key not in group_base:
                        group_base[key] = secrets.token_hex(8)
                    target = workdir / secrets.token_hex(8) / group_base[key]
                    target.mkdir(parents=True)
                    for rel, text in case.files.items():
                        dest = target / rel
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        dest.write_text(text, encoding="utf-8")
                    cwd = workdir / secrets.token_hex(8)
                    cwd.mkdir()
                    ok, observed = run_case(script, box_id, target, case.expect,
                                            cwd)
                    shutil.rmtree(cwd, ignore_errors=True)
                    if not ok:
                        bad.append("%s expected %s, saw %s"
                                   % (case.label, case.expect, observed))
            finally:
                shutil.rmtree(workdir, ignore_errors=True)
            if bad:
                lines.append("  %s: not counted (%d of %d cases wrong: %s)"
                             % (box_id, len(bad), total_cases,
                                "; ".join(bad[:4])))
            else:
                counted += 1
                lines.append("  %s: counted (%d of %d cases)"
                             % (box_id, total_cases, total_cases))
    finally:
        shutil.rmtree(tree, ignore_errors=True)

    header = "agent-definition boxes executed and discriminating %d of %d" % (
        counted, total)
    return (0 if counted >= MIN_COUNT else 1), [header] + lines, header


# --------------------------------------------------------------------------
# the reference delegate (self-test fixture only -- never a lane file)
# --------------------------------------------------------------------------

REFERENCE_DELEGATE = r'''#!/usr/bin/env python3
# Reference delegate for the agent-definition boxes.
# SELF-TEST FIXTURE ONLY: it lives inside check_agentdef_boxes.py and is
# never shipped as a lane file.  It implements the operational readings
# stated in that counter's docstring, and exists to prove that the counter's
# generated cases are satisfiable.
import argparse
import json
import re
import sys
from pathlib import Path

MONTHS = ("January|February|March|April|May|June|July|August|September|"
          "October|November|December")
ISO_DATE_RE = re.compile(r"(?<!\d)\d{4}-\d{2}-\d{2}(?!\d)")
MONTH_DAY_RE = re.compile(r"(?:\b(?:%s)\s+\d{1,2}\b)|(?:\b\d{1,2}\s+(?:%s)\b)"
                          % (MONTHS, MONTHS), re.I)
ROUND_RE = re.compile(r"\bround[-\s#]?\d+\b|\bpropose\s+round\b", re.I)
CURRENT_TASK_RE = re.compile(r"\byour\s+current\s+task\b", re.I)
ONE_SHOT_RE = re.compile(r"\bone[-\s]shot\b|\bonce\s+only\b|"
                         r"\bonly\s+this\s+once\b|\bfor\s+this\s+task\s+only\b|"
                         r"\bthis\s+time\s+only\b|\bjust\s+this\s+once\b", re.I)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
MIN_DUP_LEN = 40


def parse_doc(text):
    lines = text.split("\n")
    fm = {}
    fm_text = ""
    body = text
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                head = lines[1:i]
                fm_text = "\n".join(head)
                body = "\n".join(lines[i + 1:])
                key = None
                for line in head:
                    if line.startswith("  - ") and key is not None:
                        if not isinstance(fm.get(key), list):
                            fm[key] = []
                        fm[key].append(line[4:].strip())
                        continue
                    if ":" in line:
                        key, value = line.split(":", 1)
                        key = key.strip()
                        fm[key] = value.strip()
                break
    return fm, fm_text, body


def agent_files(target):
    agents = target / "agents"
    if not agents.is_dir():
        return []
    return sorted(agents.glob("*.md"))


def check_01(target):
    files = agent_files(target)
    if not files:
        return "FAIL", "no agent files in the target"
    docs = {}
    for path in files:
        with path.open(encoding="utf-8") as handle:
            docs[path] = parse_doc(handle.read())
    for path in files:
        stem = path.stem
        name = (docs[path][0].get("name") or "").strip()
        if name:
            if name != stem:
                return "FAIL", "declared name %r differs from stem %r" % (name, stem)
            continue
        siblings = [other for other in files if other != path]
        if siblings and all((docs[other][0].get("name") or "").strip()
                            for other in siblings):
            return "FAIL", "no name declared while every sibling declares one"
    return "PASS", "%d agent files" % len(files)


def check_02(target):
    files = agent_files(target)
    if not files:
        return "FAIL", "no agent files in the target"
    identifiers = {}
    for path in files:
        with path.open(encoding="utf-8") as handle:
            fm, _fm_text, _body = parse_doc(handle.read())
        name = (fm.get("name") or "").strip()
        identifiers[path] = name or path.stem
    enrolled = set()
    roster = target / "opencode.json"
    if roster.is_file():
        try:
            with roster.open(encoding="utf-8") as handle:
                payload = json.load(handle)
        except (OSError, ValueError):
            payload = {}
        agent_map = payload.get("agent") if isinstance(payload, dict) else None
        if isinstance(agent_map, dict):
            enrolled = {str(key).strip() for key in agent_map}
    reachable = set()
    changed = True
    while changed:
        changed = False
        for path in files:
            ident = identifiers[path]
            if ident in enrolled and ident not in reachable:
                reachable.add(ident)
                changed = True
        for path in files:
            ident = identifiers[path]
            if ident not in reachable:
                continue
            with path.open(encoding="utf-8") as handle:
                fm, _fm_text, _body = parse_doc(handle.read())
            subs = fm.get("subagents")
            if isinstance(subs, str):
                subs = [subs]
            elif not isinstance(subs, list):
                subs = []
            for name in subs:
                name = str(name).strip()
                if name and name not in reachable:
                    reachable.add(name)
                    changed = True
    for path in files:
        if identifiers[path] not in reachable:
            return "FAIL", "agent %r is not reachable" % identifiers[path]
    return "PASS", "%d agents reachable" % len(files)


def check_05(target):
    files = agent_files(target)
    if not files:
        return "FAIL", "no agent files in the target"
    for path in files:
        with path.open(encoding="utf-8") as handle:
            _fm, fm_text, _body = parse_doc(handle.read())
        if ISO_DATE_RE.search(fm_text):
            return "FAIL", "%s: ISO date in the frontmatter" % path.stem
        if MONTH_DAY_RE.search(fm_text):
            return "FAIL", "%s: month-name date in the frontmatter" % path.stem
        if ROUND_RE.search(fm_text):
            return "FAIL", "%s: round index in the frontmatter" % path.stem
    return "PASS", "%d agent files" % len(files)


def check_06(target):
    files = agent_files(target)
    if not files:
        return "FAIL", "no agent files in the target"
    for path in files:
        with path.open(encoding="utf-8") as handle:
            _fm, _fm_text, body = parse_doc(handle.read())
        if CURRENT_TASK_RE.search(body):
            return "FAIL", "%s: 'your current task' in the body" % path.stem
        if ROUND_RE.search(body):
            return "FAIL", "%s: round index in the body" % path.stem
        if ONE_SHOT_RE.search(body):
            return "FAIL", "%s: one-shot instruction in the body" % path.stem
    return "PASS", "%d agent files" % len(files)


def analyze_body(body):
    paragraphs = []
    sections = []
    current_name = None
    current_paragraphs = []
    buffer = []

    def flush():
        if buffer:
            text = " ".join(part.strip() for part in buffer)
            text = re.sub(r"\s+", " ", text).strip()
            paragraphs.append(text)
            if current_name is not None:
                current_paragraphs.append(text)
            del buffer[:]

    for line in body.split("\n"):
        match = HEADING_RE.match(line)
        if match:
            flush()
            if current_name is not None:
                sections.append((current_name, "\n".join(current_paragraphs)))
                current_paragraphs = []
            current_name = match.group(1).strip()
        elif not line.strip():
            flush()
        else:
            buffer.append(line)
    flush()
    if current_name is not None:
        sections.append((current_name, "\n".join(current_paragraphs)))
    return paragraphs, sections


def check_07(target):
    files = agent_files(target)
    if not files:
        return "FAIL", "no agent files in the target"
    for path in files:
        with path.open(encoding="utf-8") as handle:
            _fm, _fm_text, body = parse_doc(handle.read())
        paragraphs, sections = analyze_body(body)
        seen = set()
        for text in paragraphs:
            if len(text) < MIN_DUP_LEN:
                continue
            if text in seen:
                return "FAIL", "%s: duplicated paragraph" % path.stem
            seen.add(text)
        by_name = {}
        for name, content in sections:
            if name in by_name and by_name[name] != content:
                return "FAIL", "%s: same-name sections with differing content" % path.stem
            by_name[name] = content
    return "PASS", "%d agent files" % len(files)


CHECKS = {
    "agentdef.01": check_01,
    "agentdef.02": check_02,
    "agentdef.05": check_05,
    "agentdef.06": check_06,
    "agentdef.07": check_07,
}


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    func = CHECKS.get(args.check)
    if func is None:
        print("unsupported check %s" % args.check, file=sys.stderr)
        return 2
    try:
        status, detail = func(Path(args.target))
    except (OSError, ValueError) as exc:
        status, detail = "ERROR", str(exc)
    code = {"PASS": 0, "FAIL": 1}.get(status, 2)
    if args.json:
        print(json.dumps({"checks": [{"id": args.check, "status": status,
                                      "detail": detail}],
                          "exit_code": code}, indent=2, sort_keys=True))
    else:
        print("%s %s: %s" % (status, args.check, detail))
    return code


if __name__ == "__main__":
    sys.exit(main())
'''

CONSTANT_PASS_DELEGATE = r'''#!/usr/bin/env python3
# SELF-TEST FIXTURE: always answers PASS.
import argparse, json, sys
p = argparse.ArgumentParser()
p.add_argument("--check", required=True)
p.add_argument("--target", required=True)
p.add_argument("--json", action="store_true")
a = p.parse_args()
print(json.dumps({"checks": [{"id": a.check, "status": "PASS", "detail": "stub"}]}))
sys.exit(0)
'''

CONSTANT_FAIL_DELEGATE = r'''#!/usr/bin/env python3
# SELF-TEST FIXTURE: always answers FAIL.
import argparse, json, sys
p = argparse.ArgumentParser()
p.add_argument("--check", required=True)
p.add_argument("--target", required=True)
p.add_argument("--json", action="store_true")
a = p.parse_args()
print(json.dumps({"checks": [{"id": a.check, "status": "FAIL", "detail": "stub"}]}))
sys.exit(1)
'''

NO_READER_DELEGATE = r'''#!/usr/bin/env python3
# SELF-TEST FIXTURE: lists the target directory but never opens a case file,
# so it cannot read the defect it is asked about.
import argparse, json, os, sys
p = argparse.ArgumentParser()
p.add_argument("--check", required=True)
p.add_argument("--target", required=True)
p.add_argument("--json", action="store_true")
a = p.parse_args()
try:
    names = os.listdir(a.target)
except OSError:
    names = []
status = "PASS" if names else "FAIL"
print(json.dumps({"checks": [{"id": a.check, "status": status, "detail": "listing"}]}))
sys.exit(0 if status == "PASS" else 1)
'''

JUNK_DELEGATE = r'''#!/usr/bin/env python3
# SELF-TEST FIXTURE: prints something that is not the contract's JSON.
import argparse, sys
p = argparse.ArgumentParser()
p.add_argument("--check", required=True)
p.add_argument("--target", required=True)
p.add_argument("--json", action="store_true")
p.parse_args()
print("checked the surface")
sys.exit(0)
'''

ID_KEYED_DELEGATE = r'''#!/usr/bin/env python3
# SELF-TEST FIXTURE: keys its answer on the box id alone, never on the case.
import argparse, json, sys
p = argparse.ArgumentParser()
p.add_argument("--check", required=True)
p.add_argument("--target", required=True)
p.add_argument("--json", action="store_true")
a = p.parse_args()
status = "PASS" if a.check in ("agentdef.01", "agentdef.02") else "FAIL"
print(json.dumps({"checks": [{"id": a.check, "status": status, "detail": "by id"}]}))
sys.exit(0 if status == "PASS" else 1)
'''

EXIT_REMAP_DELEGATE = r'''#!/usr/bin/env python3
# SELF-TEST FIXTURE: prints FAIL but exits 2 (the round-55 remap class).
import argparse, json, sys
p = argparse.ArgumentParser()
p.add_argument("--check", required=True)
p.add_argument("--target", required=True)
p.add_argument("--json", action="store_true")
a = p.parse_args()
print(json.dumps({"checks": [{"id": a.check, "status": "FAIL", "detail": "stub"}]}))
sys.exit(2)
'''

NAME_KEYED_DELEGATE = r'''#!/usr/bin/env python3
# SELF-TEST FIXTURE: keys its answer on the case directory name and the file
# names instead of on the content of the case.
import argparse, hashlib, json, os, sys
p = argparse.ArgumentParser()
p.add_argument("--check", required=True)
p.add_argument("--target", required=True)
p.add_argument("--json", action="store_true")
a = p.parse_args()
names = []
for root, dirs, files in os.walk(a.target):
    dirs.sort()
    for name in sorted(files):
        names.append(os.path.relpath(os.path.join(root, name), a.target))
digest = hashlib.sha256(os.path.basename(a.target).encode("utf-8")).hexdigest()
for name in names:
    digest = hashlib.sha256((digest + name).encode("utf-8")).hexdigest()
status = "PASS" if int(digest[:8], 16) % 2 == 0 else "FAIL"
print(json.dumps({"checks": [{"id": a.check, "status": status, "detail": "by name"}]}))
sys.exit(0 if status == "PASS" else 1)
'''


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

class Report:
    def __init__(self) -> None:
        self.assertions = 0
        self.failures = 0
        self.notes: list[str] = []

    def check(self, name: str, ok: bool, detail: str = "") -> bool:
        self.assertions += 1
        if not ok:
            self.failures += 1
            self.notes.append("FAILED %s%s" % (name, (": " + detail) if detail else ""))
        return ok


def fixture_map(dispositions: dict[str, str],
                shas: dict[str, str] | None = None) -> dict:
    shas = shas or {}
    boxes = []
    for index in range(1, 10):
        box_id = "agentdef.%02d" % index
        boxes.append({
            "box_id": box_id,
            "section": SECTION,
            "text_sha256": shas.get(box_id, PINNED_BOX_SHA[box_id]),
            "disposition": dispositions.get(
                box_id, "unexecuted:surface = opencode/agents/*.md; no box"),
        })
    return {"schema": "kotoba-checklist-v1", "file": "SKILL.md",
            "normalization": "fixture", "boxes": boxes, "box_total": len(boxes)}


def init_repo(root: Path, files: dict[str, str]) -> str:
    root.mkdir(parents=True, exist_ok=True)
    for rel, text in files.items():
        dest = root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
    env = dict(os.environ)
    env["GIT_OPTIONAL_LOCKS"] = "0"
    env.update({"GIT_AUTHOR_NAME": "kotoba self-test",
                "GIT_AUTHOR_EMAIL": "kotoba-self-test@invalid",
                "GIT_COMMITTER_NAME": "kotoba self-test",
                "GIT_COMMITTER_EMAIL": "kotoba-self-test@invalid"})
    subprocess.run(["git", "init", "--quiet", str(root)], check=True, env=env,
                   timeout=60)
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=True, env=env,
                   timeout=60)
    subprocess.run(["git", "-C", str(root), "commit", "--quiet", "-m",
                    "agentdef counter self-test"], check=True, env=env, timeout=60)
    out = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                         check=True, capture_output=True, env=env, timeout=60)
    return out.stdout.decode("ascii").strip()


def counter_env() -> dict[str, str]:
    """The environment the frozen predicate runs the counter under."""
    env = dict(os.environ)
    env["GIT_OPTIONAL_LOCKS"] = "0"
    return env


def run_counter(repo: Path, rev: str, timeout: int = 150) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, "-B", str(Path(__file__).resolve()), "--rev", rev,
         "--repo", str(repo)],
        capture_output=True, text=True, timeout=timeout, env=counter_env())
    return proc.returncode, proc.stdout, proc.stderr


def self_test() -> int:
    report = Report()
    with tempfile.TemporaryDirectory(prefix="agentdef-selftest-") as td:
        root = Path(td)

        # The generators themselves must satisfy the frozen case rules: at
        # least four PASS and four FAIL cases per box, every PASS case paired
        # with a FAIL twin of the same group, and every twin pair of similar
        # size and of the same file names.
        generated = build_cases(random.Random("generator-self-test"))
        for box, box_cases in generated.items():
            passes = [c for c in box_cases if c.expect == "PASS"]
            fails = [c for c in box_cases if c.expect == "FAIL"]
            report.check("%s: at least four PASS cases" % box, len(passes) >= 4,
                         "%d PASS cases" % len(passes))
            report.check("%s: at least four FAIL cases" % box, len(fails) >= 4,
                         "%d FAIL cases" % len(fails))
            for group in {c.group for c in box_cases}:
                pair = [c for c in box_cases if c.group == group]
                report.check("%s/%s: one PASS and one FAIL" % (box, group),
                             sorted(c.expect for c in pair) == ["FAIL", "PASS"],
                             str([(c.label, c.expect) for c in pair]))
                if len(pair) == 2:
                    same_names = (sorted(pair[0].files) == sorted(pair[1].files))
                    report.check("%s/%s: twins share their file names"
                                 % (box, group), same_names,
                                 str((sorted(pair[0].files), sorted(pair[1].files))))
                    size_a = sum(len(v) for v in pair[0].files.values())
                    size_b = sum(len(v) for v in pair[1].files.values())
                    ratio = (max(size_a, size_b) / max(1, min(size_a, size_b)))
                    report.check("%s/%s: twins are of similar size"
                                 % (box, group), ratio <= 1.5,
                                 "%d vs %d bytes" % (size_a, size_b))

        def scenario(name: str, delegate_source: str,
                     dispositions: dict[str, str] | None = None,
                     extra_files: dict[str, str] | None = None,
                     shas: dict[str, str] | None = None) -> tuple[int, str, str]:
            disp = dispositions or {
                box: "delegated:verifiers/verify_agentdef.py"
                for box in GENERATED_BOXES}
            files = {
                "verifiers/checklist-baseline.json": json.dumps(
                    fixture_map(disp, shas), indent=2, sort_keys=True) + "\n",
                "verifiers/verify_agentdef.py": delegate_source,
            }
            if extra_files:
                files.update(extra_files)
            repo = root / name
            rev = init_repo(repo, files)
            return run_counter(repo, rev)

        # (a) the reference delegate proves the generators are satisfiable.
        rc, out, err = scenario("reference", REFERENCE_DELEGATE)
        report.check("reference: exit 0", rc == 0, "exit %d %s" % (rc, err[:400]))
        report.check("reference: 5 of 9",
                     "agent-definition boxes executed and discriminating 5 of 9"
                     in out, out[:800])
        for box in GENERATED_BOXES:
            report.check("reference: %s counted" % box,
                         ("  %s: counted (" % box) in out, out[:800])
        for box in ("agentdef.03", "agentdef.04", "agentdef.08", "agentdef.09"):
            report.check("reference: %s has no generator" % box,
                         ("  %s: not counted (no case generator" % box) in out,
                         out[:800])

        # (b) shortcuts that must not score a single box.
        for name, source in (("constant-pass", CONSTANT_PASS_DELEGATE),
                             ("constant-fail", CONSTANT_FAIL_DELEGATE),
                             ("no-reader", NO_READER_DELEGATE),
                             ("junk", JUNK_DELEGATE),
                             ("id-keyed", ID_KEYED_DELEGATE),
                             ("exit-remap", EXIT_REMAP_DELEGATE),
                             ("name-keyed", NAME_KEYED_DELEGATE)):
            rc, out, err = scenario(name, source)
            report.check("%s: exit 1" % name, rc == 1,
                         "exit %d %s" % (rc, err[:400]))
            report.check("%s: 0 of 9" % name,
                         "agent-definition boxes executed and discriminating 0 of 9"
                         in out, out[:800])

        # (c) a reworded box and an unusable delegated path disqualify.
        disp = {box: "delegated:verifiers/verify_agentdef.py"
                for box in GENERATED_BOXES}
        rc, out, err = scenario("reworded", REFERENCE_DELEGATE,
                                 dispositions=disp,
                                 shas={"agentdef.01": "0" * 64})
        report.check("reworded: agentdef.01 not counted",
                     "  agentdef.01: not counted (box text was reworded" in out,
                     out[:800])
        report.check("reworded: 4 of 9",
                     "agent-definition boxes executed and discriminating 4 of 9"
                     in out, out[:800])

        absolute = dict(disp)
        absolute["agentdef.02"] = "delegated:/tmp/verify_agentdef.py"
        rc, out, err = scenario("absolute-path", REFERENCE_DELEGATE,
                                 dispositions=absolute)
        report.check("absolute path: agentdef.02 not counted",
                     "  agentdef.02: not counted (delegated path is absolute"
                     in out, out[:800])

        dotdot = dict(disp)
        dotdot["agentdef.02"] = "delegated:../verify_agentdef.py"
        rc, out, err = scenario("dotdot-path", REFERENCE_DELEGATE,
                                 dispositions=dotdot)
        report.check("dotdot path: agentdef.02 not counted",
                     "  agentdef.02: not counted (delegated path escapes the "
                     "repository" in out, out[:800])

        # (c2) a stdlib shadow planted beside the counter itself must not
        # capture the counter's imports: the counter passes, the measured
        # revision is still measured (the round-55 argparse-shadow class).
        shadow_dir = root / "counter-shadow"
        shadow_dir.mkdir()
        shutil.copy(Path(__file__).resolve(),
                    shadow_dir / "check_agentdef_boxes.py")
        (shadow_dir / "argparse.py").write_text(
            "raise SystemExit(9)\n", encoding="utf-8")
        reference_repo = root / "reference"
        proc = subprocess.run(
            [sys.executable, "-B",
             str(shadow_dir / "check_agentdef_boxes.py"),
             "--rev", git_text(reference_repo, "rev-parse", "HEAD").strip(),
             "--repo", str(reference_repo)],
            capture_output=True, text=True, timeout=150, env=counter_env())
        report.check("counter shadow: counter still measures",
                     "agent-definition boxes executed and discriminating 5 of 9"
                     in proc.stdout,
                     "exit %d %s %s" % (proc.returncode, proc.stdout[:300],
                                        proc.stderr[:300]))
        report.check("counter shadow: the shadow was not imported",
                     proc.returncode == 0,
                     "exit %d %s" % (proc.returncode, proc.stderr[:300]))

        # (d) a stdlib shadow under verifiers/ disqualifies every box.
        rc, out, err = scenario("stdlib-shadow", REFERENCE_DELEGATE,
                                 extra_files={"verifiers/argparse.py":
                                              "# shadow\n"})
        report.check("stdlib shadow: 0 of 9",
                     "agent-definition boxes executed and discriminating 0 of 9"
                     in out, out[:800])
        report.check("stdlib shadow: the line says why",
                     "stdlib shadow under verifiers/: verifiers/argparse.py"
                     in out, out[:800])

    print("self-test: %d failure(s) over %d assertions"
          % (report.failures, report.assertions))
    for note in report.notes:
        print(note)
    return 0 if report.failures == 0 else 1


# --------------------------------------------------------------------------
# entry point
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--rev", help="lane revision to measure")
    parser.add_argument("--repo", default=str(lane_default()),
                        help="lane repository")
    parser.add_argument("--self-test", action="store_true",
                        help="exercise isolated fixtures")
    args = parser.parse_args(argv)
    if args.self_test:
        if args.rev:
            parser.error("--self-test cannot be combined with --rev")
        return self_test()
    if not args.rev:
        parser.error("--rev is required")
    repo = Path(args.repo)
    seed = secrets.token_hex(16)
    try:
        code, lines, header = evaluate(repo, args.rev, seed)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired,
            OSError, ValueError, KeyError, json.JSONDecodeError,
            tarfile.TarError) as exc:
        print("cannot evaluate: %s" % exc, file=sys.stderr)
        return 2
    print(header)
    for line in lines[1:]:
        print(line)
    print("seed: %s" % seed)
    return code


if __name__ == "__main__":
    sys.exit(main())
