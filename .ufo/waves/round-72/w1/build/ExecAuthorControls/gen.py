#!/usr/bin/env python3
"""gen.py — build the C1 control-world bundles for round 72, wave 1 (seat ExecAuthorControls).

Usage: python3 -B gen.py --base <clean checkout of c69711e> --out <build/ExecAuthorControls>

Everything it writes is a draft under .ufo/waves/round-72/w1/build/ExecAuthorControls/.
No committed lane file is touched: the base bytes are read from a throwaway --shared clone.

Layout produced
  carrier/                       the honest overlay (four rule boxes, the rung entry, three
                                 registry rows, the corpus index line, three pinned snapshots)
  <world>/delta.patch            one unified diff against carrier (the single-clause defect)
  <world>/WORLD.md               what the world is, the clause it should trip, the prediction
  pins.json + SHA256SUMS         snapshot pins, rewritten per world that tampers a snapshot
"""
from __future__ import annotations

import argparse
import hashlib
import os
import json
import re
import shutil
import subprocess
from pathlib import Path

STAGED = Path("/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md")
ENTRY = "corpus/knowledge/resident-index-and-rungs-round72.md"
SNAP_DIR = ".ufo/waves/round-72/snapshots"
A4_IDS = ["S255", "S262", "S263"]
# the names and pin convention already used at .ufo/waves/round-72/snapshots/ in the lane (a sibling
# seat's captures of the same pages, byte-identical to this seat's fetch): <id>-<slug>.<ext> plus
# <id>.sha256 lines "sha256  filename"
SNAP_NAMES = {"S255": "S255-agent-skills-skill-md.md",
              "S262": "S262-factory-droid-skills.md",
              "S263": "S263-pi-skills.md"}

# --- the four boxes (honest carrier) -------------------------------------------------------
BOXES = {
    "A1": """- [ ] Skill `name` uniqueness: no client merges two same-named skills — four of the five cited
      routes resolve a collision by order and one of those orders reverses, so pick a `name` that
      is unique across every location the client loads, not a client's `precedence` ladder.
      (sourced: S203, S207; entry: corpus/knowledge/skill-name-precedence-round69.md)""",
    "A2": """- [ ] `authority` level: a `SKILL.md` `body` is not a privileged instruction — say which `level`
      of the instruction ladder the rule sits at, and that a higher `authority` overrides it, so no
      rule asks the body to outrank the user's own turn.
      (sourced: S123, S129; entry: corpus/knowledge/instruction-authority-ladder-round67.md)""",
    "A3": """- [ ] `install`-path `trust`: a skill that runs a `command` executes repository-controlled
      instructions — name the `install` path it was found at and the gate it cleared, and never
      let a fetched skill's `command` run ahead of the client's approval gate.
      (sourced: S198, S200, S208; entry: corpus/knowledge/client-trust-gates-round68.md)""",
    "A4": """- [ ] Rung, then shape: a one-off `prompt` for a single use, a `skill` for what is too specific
      for an always-on file and too shaped for a prompt, and the always-on file kept as an `index`
      — names and descriptions resident, the payload retrievable on demand.
      (sourced: S255, S262, S263; entry: corpus/knowledge/resident-index-and-rungs-round72.md)""",
}

# the token-only variant: the same four tails, no rule text at all (the headline world)
TOKEN_BOXES = {
    "A1": "- [ ] `name` `unique` `precedence`.\n"
          "      (sourced: S203, S207; entry: corpus/knowledge/skill-name-precedence-round69.md)",
    "A2": "- [ ] `authority` `level` `body`.\n"
          "      (sourced: S123, S129; entry: corpus/knowledge/instruction-authority-ladder-round67.md)",
    "A3": "- [ ] `install` `trust` `command`.\n"
          "      (sourced: S198, S200, S208; entry: corpus/knowledge/client-trust-gates-round68.md)",
    "A4": "- [ ] `prompt` `always-on` `skill` `index`.\n"
          "      (sourced: S255, S262, S263; entry: corpus/knowledge/resident-index-and-rungs-round72.md)",
}

ANCHOR = """      negation, or quotes it in backticks, is read as the rule, not a stub)

## Agent-definition fidelity checklist"""

ENTRY_HEAD = """source: S255 — Agent Skills — skill.md (the format one-pager) — https://agentskills.io/skill.md — the "Product summary" and "Key files and paths" sections — located quote "at startup they load only the name and description of each skill (~50-100 tokens per skill)"
source: S262 — Factory Documentation — Skills — https://docs.factory.ai/cli/configuration/skills — the "Skills" page under the Droid harness — located quote "Use skills when instructions are too specific for always-on `AGENTS.md`"
source: S263 — pi-mono — coding agent — Skills — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md — the "# Skills" heading — located quote "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them."
verified-at: 2026-10-25
recheck: 90d — re-fetch all three pages and confirm each located quote and the rung boundary it carries are unchanged

# The middle rung and the resident index — what belongs in a skill, an always-on file, or a one-off prompt

The lane had inferred the three-rung instruction ladder from how each client implements loading:
a one-off prompt below, a skill in the middle, an always-on context file above. Two of the three
vendors in the round-72 assimilation package state that middle rung in their own words, and the
specification's own one-pager states the cost side that makes the top rung an index rather than a
payload.

## What the three rows state

| rung | the sentence it rests on | what it decides for an author | source |
|---|---|---|---|
| one-off `prompt` | "too structured for a one-off prompt" (the same sentence that names the skill rung) | a use that happens once is a prompt, not a file | S262 |
| `skill` | "Use skills when instructions are too specific for always-on `AGENTS.md`, too structured for a one-off prompt, and useful enough to reuse." | reusable, specific, too shaped to be a prompt: this is the skill's ground | S262 |
| `skill` (second vendor) | "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them." | the middle rung is on-demand by construction, and its resident part is name + description | S263 |
| `always-on` file | "at startup they load only the name and description of each skill (~50-100 tokens per skill)" | the resident surface is an index; the payload is what must stay retrievable | S255 |

## The rule this entry carries

A skill is for instructions that are too specific for an always-on file and too shaped for a
one-off prompt, and that are reused. When the choice is between the skill rung and the always-on
rung, the always-on file stays an index — names and descriptions resident, the payload
retrievable — because the resident surface is the one every turn pays for.

## What the rows do not settle

S262 and S263 name the boundary between the prompt rung and the skill rung, not the boundary
between the skill rung and the always-on rung: neither states when a rule must be resident
rather than retrievable. S255 states the resident cost of a skill catalogue, not the size at
which an always-on block stops paying. The invocation failure the lane measured (a skill that
is offered and never invoked) is the failure of the middle rung, and none of these three rows
measures it.

## Provenance (this draft)

Fetched and pinned by seat ExecAuthorControls on 2026-10-25; every located quote above was
re-found in the pinned bytes by a literal word-bounded search before the world was committed.
`docs.factory.ai/cli/configuration/skills` answers 308 to `docs.factory.com/harness/skills`; the
snapshot is the page's own `.md` sibling at the same path, so the bytes are the served text and
not a rendered HTML page. Sha256 of each snapshot is in `%(snapdir)s/<id>.sha256` (and `pins.json`).
"""


def sh(*args: str) -> str:
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout


def staged_rows() -> dict[str, str]:
    rows = {}
    for line in STAGED.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| (S\d{3}) \|", line)
        if m:
            rows[m.group(1)] = line
    return rows


def rewrite_row(line: str, ident: str) -> str:
    cells = [c for c in line.strip().strip("|").split("|")]
    assert len(cells) == 11, (ident, len(cells))
    cells = [c.strip() for c in cells]
    cells[10] = ENTRY                      # used-by names the entry this world appends
    cells[8] = "2026-10-25"                # opened: this seat's re-fetch
    # the fleet validator (sources-census.sh E09) accepts only a bare cadence in this cell; the
    # staged cell's prose ("90d — re-fetch … (ran 2026-10-23)") is E09-invalid, so keep the cadence
    m = re.match(r"^(\d+d|on-[a-z]+|\d{4}-\d{2}-\d{2})", cells[9])
    cells[9] = m.group(1) if m else cells[9]
    if ident == "S262":
        # the staged cell drops the backticks the served .md carries; the pin is the served bytes
        cells[5] = cells[5].replace("always-on AGENTS.md", "always-on `AGENTS.md`")
    return "| " + " | ".join(cells) + " |"


def add_boxes(skill: str, boxes: dict[str, str]) -> str:
    assert ANCHOR in skill
    block = "\n".join(boxes[k] for k in ("A1", "A2", "A3", "A4"))
    head = "      negation, or quotes it in backticks, is read as the rule, not a stub)\n"
    return skill.replace(ANCHOR, head + block + "\n\n## Agent-definition fidelity checklist", 1)


def add_rows(sources: str, rows: dict[str, str]) -> str:
    lines = sources.splitlines()
    last = max(i for i, l in enumerate(lines) if re.match(r"^\| S\d{3} \|", l))
    block = [rewrite_row(rows[i], i) for i in A4_IDS]
    lines[last + 1:last + 1] = block
    return "\n".join(lines) + "\n"


def add_index(readme: str) -> str:
    lines = readme.splitlines()
    at = max(i for i, l in enumerate(lines) if "skill-name-precedence-round69.md" in l)
    lines.insert(at + 1, (
        "| Resident index and the middle rung (round 72) | `knowledge/resident-index-and-rungs-round72.md` | "
        "the rung rule stated by two vendors (S262 Factory, S263 pi) plus the specification one-pager's "
        "resident-cost sentence (S255): a skill is for instructions too specific for an always-on file and "
        "too shaped for a one-off prompt, and the always-on surface stays an index rather than a payload; "
        "the three rows were re-fetched and sha256-pinned under `.ufo/waves/round-72/snapshots/` on "
        "2026-10-25 |"
    ))
    return "\n".join(lines) + "\n"


def snapshots(out: Path, fetched: dict[str, tuple[str, str, int]]) -> dict:
    """fetched: id -> (url, local file, http status). Returns the pin record."""
    d = out / "carrier" / SNAP_DIR
    d.mkdir(parents=True, exist_ok=True)
    pins = []
    for ident, (url, src, status) in fetched.items():
        raw = Path(src).read_bytes()
        name = SNAP_NAMES[ident]
        (d / name).write_bytes(raw)
        pins.append({"id": ident, "path": f"{SNAP_DIR}/{name}", "url": url,
                     "http_status": status, "bytes": len(raw),
                     "sha256": hashlib.sha256(raw).hexdigest()})
    write_pins(out / "carrier", pins)
    return {"snapshots": pins}


def write_pins(root: Path, pins: list[dict]) -> None:
    d = root / SNAP_DIR
    (d / "pins.json").write_text(json.dumps(
        {"fetched-at": "2026-10-25", "snapshots": pins}, indent=2) + "\n", encoding="utf-8")
    for p in pins:
        (d / f"{p['id']}.sha256").write_text(
            f"{p['sha256']}  {p['path'].rsplit('/', 1)[1]}\n", encoding="utf-8")


def patch(world: Path, root: Path, rel: str, new_text: str) -> None:
    """Write world/delta.patch as a unified diff carrier/<rel> -> world content."""
    old = (root / "carrier" / rel).read_text(encoding="utf-8")
    tmp = world / "_new" / rel
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(new_text, encoding="utf-8")
    diff = subprocess.run(
        ["diff", "-u", "--label", f"a/{rel}", "--label", f"b/{rel}",
         str(root / "carrier" / rel), str(tmp)],
        capture_output=True, text=True).stdout
    shutil.rmtree(world / "_new")
    (world / "delta.patch").write_text(diff, encoding="utf-8")


WORLD_SPECS = [
    ("honest", "exit-0 arm: four boxes that really carry the rules",
     "none — the carrier verbatim", "4 of 4, exit 0",
     "(a)-(d) all hold; this is the arm that must read 4."),
    ("w1-queued-rows", "boxes citing `queued` rows",
     "the three appended A4 rows: `status` `mined` -> `queued` (used-by left intact)",
     "3 of 4, exit 1",
     "(b) status conjunct — the rows resolve and name the entry, so only `status` catches it."),
    ("w2-used-by-omits", "boxes citing rows whose `used-by` omits the entry",
     "row S262: `used-by` -> `—` (status stays `mined`)",
     "3 of 4, exit 1",
     "(b) used-by conjunct — the row is mined, tiered and real; only the back-link is missing."),
    ("w3-html-comment", "the boxes inside an HTML comment",
     "the four boxes wrapped in `<!--` … `-->` inside the checklist section",
     "0 of 4, exit 1",
     "(a) rendered-bytes conjunct — the predicate removes HTML comments before it looks for boxes."),
    ("w4-fenced", "the boxes inside a fence",
     "the four boxes inside a ``` fence inside the checklist section",
     "0 of 4, exit 1",
     "(a) rendered-bytes conjunct — fenced blocks are removed before box extraction."),
    ("w5-outside-section", "the boxes placed outside the checklist section (in § Sources)",
     "the four boxes moved to the end of `## Sources`, section otherwise unchanged",
     "0 of 4, exit 1",
     "(a) section conjunct — the boxes are rendered but not inside `## Trigger-fidelity checklist`."),
    ("w6-a4-quote-absent", "an A4 box whose quote is absent from its snapshot",
     "snapshot S262 truncated to its first five lines; pins recomputed over the truncated bytes",
     "3 of 4, exit 1",
     "(d) quote-in-snapshot conjunct — the pin is honest (it pins the truncated bytes), the quote is gone."),
    ("w7-unknown-id", "a box naming an id that resolves in no registry row",
     "A1 tail cites `S999` beside the real `S203`",
     "3 of 4, exit 1",
     "(b) registry-row conjunct — every cited id must be an 11-cell row; S999 is in none."),
    ("w8-entry-no-trio", "the entry without the provenance trio",
     "the A4 entry keeps its `source:` lines and loses `verified-at:` and `recheck:`",
     "3 of 4, exit 1",
     "(c) provenance conjunct — the entry exists and names its ids, but carries no verification date."),
    ("w10-quote-echo-snapshot", "an A4 snapshot that is the quote echoed back",
     "snapshot S262 replaced by a one-line file holding exactly the located quote; pin recomputed",
     "4 of 4, exit 0 — the second counter hole",
     "(d) as frozen cannot tell a page snapshot from a quote echo: the pin is honest, the file is "
     "not the page, and no conjunct reads the snapshot's provenance."),
    ("w9-token-list", "HEADLINE: token-only boxes over a fully honest apparatus",
     "the four boxes replaced by their token sets alone (`name` `unique` `precedence` …) plus the honest tails",
     "4 of 4, exit 0 — the counter hole",
     "(a) as frozen cannot catch it: it tests token membership, not rule carriage. The clause that "
     "should have caught it is (a)'s \"carries the rule's token set\"."),
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    base, out = Path(a.base), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    skill = (base / "SKILL.md").read_text(encoding="utf-8")
    sources = (base / "corpus/SOURCES.md").read_text(encoding="utf-8")
    readme = (base / "corpus/README.md").read_text(encoding="utf-8")

    carrier = out / "carrier"
    (carrier / "corpus/knowledge").mkdir(parents=True, exist_ok=True)
    (carrier / "SKILL.md").write_text(add_boxes(skill, BOXES), encoding="utf-8")
    (carrier / "corpus/SOURCES.md").write_text(add_rows(sources, staged_rows()), encoding="utf-8")
    (carrier / "corpus/README.md").write_text(add_index(readme), encoding="utf-8")
    # fetched bytes: FETCHED/ (written by fetch.sh) or, on a re-run, the already-pinned snapshots
    fetched = {}
    for ident, url, name in (
        ("S255", "https://agentskills.io/skill.md", SNAP_NAMES["S255"]),
        ("S262", "https://docs.factory.ai/cli/configuration/skills.md", SNAP_NAMES["S262"]),
        ("S263", "https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md",
         SNAP_NAMES["S263"]),
    ):
        src = Path(os.environ.get("FETCHED", "/tmp/k72w1-ExecAuthorControls.fetch")) / name
        if not src.exists():
            src = out / "carrier" / SNAP_DIR / name
        status = 200
        st = src.with_suffix(src.suffix + ".status")
        if st.exists():
            status = int(st.read_text().split()[0])
        fetched[ident] = (url, str(src), status)
    pins = snapshots(out, fetched)["snapshots"]
    (carrier / ENTRY).write_text(ENTRY_HEAD % {"snapdir": SNAP_DIR}, encoding="utf-8")

    carrier_skill = (carrier / "SKILL.md").read_text(encoding="utf-8")
    carrier_sources = (carrier / "corpus/SOURCES.md").read_text(encoding="utf-8")

    for name, title, mutation, prediction, clause in WORLD_SPECS:
        w = out / name
        w.mkdir(parents=True, exist_ok=True)
        (w / "README.md").write_text(
            f"# {name} — {title}\n\n"
            f"**Mutation:** {mutation}\n\n"
            f"**Prediction:** {prediction}\n\n"
            f"**Clause that should catch it:** {clause}\n\n"
            f"Replay: `bash replay.sh {name}` from this directory "
            f"(clones the lane `--shared`, checks out the base, applies `carrier/` then "
            f"`delta.patch`, commits inside the throwaway clone, runs the literal oracle).\n",
            encoding="utf-8")
        if name == "honest":
            (w / "delta.patch").write_text("", encoding="utf-8")
        elif name == "w1-queued-rows":
            rows = staged_rows()
            new = add_rows(sources, rows)
            new = "\n".join(re.sub(r"\| mined \| 2026-10-25 \|", "| queued | 2026-10-25 |", l)
                            if re.match(r"^\| S(255|262|263) \|", l) else l
                            for l in new.splitlines()) + "\n"
            patch(w, out, "corpus/SOURCES.md", new)
        elif name == "w2-used-by-omits":
            new = "\n".join(
                re.sub(r"\| corpus/knowledge/resident-index-and-rungs-round72\.md \|$", "| — |", l)
                if l.startswith("| S262 |") else l
                for l in carrier_sources.splitlines()) + "\n"
            patch(w, out, "corpus/SOURCES.md", new)
        elif name == "w3-html-comment":
            block = "\n".join(BOXES[k] for k in ("A1", "A2", "A3", "A4"))
            new = carrier_skill.replace(block, "<!--\n" + block + "\n-->", 1)
            patch(w, out, "SKILL.md", new)
        elif name == "w4-fenced":
            block = "\n".join(BOXES[k] for k in ("A1", "A2", "A3", "A4"))
            new = carrier_skill.replace(block, "```\n" + block + "\n```", 1)
            patch(w, out, "SKILL.md", new)
        elif name == "w5-outside-section":
            block = "\n".join(BOXES[k] for k in ("A1", "A2", "A3", "A4"))
            new = carrier_skill.replace(block + "\n\n", "", 1).rstrip("\n") + "\n\n" + block + "\n"
            patch(w, out, "SKILL.md", new)
        elif name == "w6-a4-quote-absent":
            snap = carrier / SNAP_DIR / SNAP_NAMES["S262"]
            raw = snap.read_bytes()
            cut = b"\n".join(raw.splitlines()[:5]) + b"\n"
            (w / "_snap").mkdir(exist_ok=True)
            (w / "_snap" / SNAP_NAMES["S262"]).write_bytes(cut)
            d = w / SNAP_DIR
            d.mkdir(parents=True, exist_ok=True)
            (d / SNAP_NAMES["S262"]).write_bytes(cut)
            tampered = []
            for p in pins:
                q = dict(p)
                if p["id"] == "S262":
                    q["bytes"] = len(cut)
                    q["sha256"] = hashlib.sha256(cut).hexdigest()
                    q["truncation"] = "first five lines of the served .md only"
                tampered.append(q)
            write_pins(w, tampered)
            shutil.rmtree(w / "_snap")
            (w / "delta.patch").write_text("", encoding="utf-8")
        elif name == "w7-unknown-id":
            new = carrier_skill.replace("(sourced: S203, S207; entry:", "(sourced: S203, S999; entry:", 1)
            patch(w, out, "SKILL.md", new)
        elif name == "w8-entry-no-trio":
            body = (carrier / ENTRY).read_text(encoding="utf-8")
            new = re.sub(r"^verified-at:.*\n", "", body, flags=re.M)
            new = re.sub(r"^recheck:.*\n", "", new, flags=re.M)
            patch(w, out, ENTRY, new)
        elif name == "w10-quote-echo-snapshot":
            echo = b'Use skills when instructions are too specific for always-on `AGENTS.md`\n'
            d = w / SNAP_DIR
            d.mkdir(parents=True, exist_ok=True)
            (d / SNAP_NAMES["S262"]).write_bytes(echo)
            echoed = []
            for p2 in pins:
                q = dict(p2)
                if p2["id"] == "S262":
                    q["bytes"] = len(echo)
                    q["sha256"] = hashlib.sha256(echo).hexdigest()
                    q["snapshot_kind"] = "quote echo, not a page capture"
                echoed.append(q)
            write_pins(w, echoed)
            (w / "delta.patch").write_text("", encoding="utf-8")
        elif name == "w9-token-list":
            block = "\n".join(BOXES[k] for k in ("A1", "A2", "A3", "A4"))
            new = carrier_skill.replace(block, "\n".join(TOKEN_BOXES[k] for k in ("A1", "A2", "A3", "A4")), 1)
            patch(w, out, "SKILL.md", new)

    print("carrier + %d worlds written under %s" % (len(WORLD_SPECS), out))


if __name__ == "__main__":
    main()
