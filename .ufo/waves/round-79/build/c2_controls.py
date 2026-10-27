#!/usr/bin/env python3
"""c2_controls.py — C2 control worlds for kotoba round 79 (seat Kb79X02C2Controls).

WHAT THIS IS

``plans/round-79.md`` § C2 names a control suite that must be run **before** any
claim data is scored on the frozen counter: C0 base copy, C1 token dump, C2
wrong-page real text, C3 shared-banner quote, C4 script-only scrape, C5
label-only, C6 sibling-host, C7 wrong sha pin / tampered snapshot, C8
first-answer baseline, C9 duplicate row, C10 quote without ``allowed-tools``.
This script builds each of those worlds as its own isolated scratch git repo and
prints, per world, the counter's verdict line (``allowed-tools surfaces backed N
of 6``, and ``script-only world: M of 6`` when printed) together with the
counter's own exit code.

Two properties matter and are both structural:

  * **No network.** Every page in every world is a fixed synthetic text in this
    file. Nothing is fetched, nothing is scraped, and no world can be confused
    with the six real pages: a control world exists to attack the counter's
    *reading*, not to supply claim data.
  * **The lane is read-only.** ``--base-tree`` is only read, with
    ``git -C <base-tree> rev-parse/cat-file``. Every world lives under
    ``--work`` (default: a fresh ``mktemp -d`` under ``$TMPDIR``).

WORLD SHAPE AND WHY THE BASE LINEAGE IS THERE

Each world is built in five plumbing steps inside ``D=$(mktemp -d -p "$WORK")``:

  1. ``git -C "$D" init -q``, identity ``scratch-r79`` /
     ``scratch@example.invalid``, and ``git -C "$D" rev-parse --show-toplevel``
     must print ``$D`` (a fixture outside its own repo is the classic way a
     damaged world writes into the caller's checkout).
  2. ``.git/objects/info/alternates`` is pointed at the base clone's object
     store (one line, read-only sharing — this is what ``git clone --shared``
     writes). It exists for one reason: the frozen counters compute their
     do-nothing figure ``held at base`` by reading ``BASE_REV`` (round 79 base
     ``b10bcbc6…``) **from the measured repo**, and a fixture repo that does not
     contain that commit cannot be evaluated at all (exit 2 before the verdict
     line). Sharing the object store makes ``BASE_REV`` resolvable without
     copying 190 MB per world and without ever writing to the base tree.
  3. ``git -C "$D" read-tree <base-rev>`` seeds the index with the real base
     tree (objects already present through the alternate), so the measured
     commit is "the base tree with the world's fixture files replaced" — the
     same shape as a lane commit.
  4. Each fixture file is written as a blob (``hash-object -w --stdin``) and
     placed with ``update-index --add --cacheinfo``; no worktree is checked out,
     so a 12-world run costs kilobytes, not gigabytes.
  5. ``write-tree`` + ``commit-tree -p <base-rev>`` + ``update-ref`` produce the
     measured commit. The counter is then run against it with
     ``--repo <D> --rev <commit>``.

The counter file itself is placed in every world at ``verifiers/
check_allowed_tools.py`` (its bytes are the ``--counter`` file), because the
frozen predicate's tree conjunct (g) asks for a registry row *for that counter*
and the lane will hold the counter at the same commit as the data. C0 is the
exception by construction: it measures the base revision itself.

PRE-REGISTERED EXPECTATIONS

``EXPECT`` below is the expected-verdict table written before any run (it is
also printed by ``--list`` and reproduced in the seat report). The script
compares the observed verdict with the pre-registered one and says
``as-expected`` or ``DIVERGES``. It does **not** judge the claim: divergence is
evidence for the L1, and ``exit 0`` from this script means only "every world
behaved as pre-registered".

Three readings of the plan are encoded deliberately and are named so a reviewer
can attack them:

  * **C4 may reach 6 of 6.** Q71: what a script-only world reaches is
    form-level, so C4 is expected to pass and is reported beside the headline,
    never as a counter defect. It is the world that shows what "no judgement"
    buys: pins, quotes and tokens can all be produced mechanically.
  * **Single-surface controls sit at 5 of 6.** C9, C10 and a one-row C6 could
    each only ever remove one surface, and 5 is still the frozen target
    (``N >= 5``). So C6 and C10 break **two** surfaces each (plan-named primary
    probe plus one partner) so the world can fall *below* the target and the
    plan's "any control reaching N >= 5 is a counter defect" rule has a chance
    to bite; C9 is left at exactly one surface because the duplicate-row
    mechanism *is* the single-surface mechanism — its verdict is read from the
    N value (6 = the duplicate was counted, a defect; 5 = the surface was
    disqualified and the plan's arithmetic, not the counter, leaves the world at
    the target; the L1 records it).
  * **C7 may be exit 2.** A tampered snapshot is a *could-not-evaluate* in the
    template counter (``snapshot_tampered``), so C7 accepts exit 1 or 2 and
    accepts an absent verdict line; anything that prints 5 or more, or exits 0,
    is the defect.

USAGE

  python3 -B .ufo/waves/round-79/build/c2_controls.py \\
      --counter .ufo/waves/round-79/build/check_allowed_tools.py \\
      --base-tree /home/vgpnk/Projects/shokunin/kotoba-shokunin \\
      --work /fast/scratch/hyaku/kotoba-r79/Kb79X02C2Controls/work

  --list            print the pre-registered expectation table and exit
  --only C3,C6      run only the named worlds
  --keep            keep the world repos (default: removed after each run)
  --verbose         print every counter line for every world
  --out FILE        write the full log to FILE (receipt) as well as stdout
  --json            write the machine-readable summary to stdout as JSON

Exit codes: 0 every world matched its pre-registration; 1 at least one world
diverged (or the counters could not be run); 2 environment (no counter, no base
tree, unreadable base revision, world build failure).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# --------------------------------------------------------------- frozen table
# Surfaces, ids, hosts and grant labels frozen by plans/round-79.md § C2.
# `tokens` are the row's page tokens (>= 3, always `allowed-tools`, one
# value-form token and one grant-semantics token); `ground` is the page token
# the (f) conjunct requires inside the located quote.
SURFACES = [
    dict(sid="S226", key="spec", name="Open specification", short="spec",
         ext="md", title="Agent Skills specification",
         url="https://agentskills.io/specification.md",
         section="allowed-tools field", grant="experimental",
         ground="Experimental",
         tokens=("allowed-tools", "space-separated", "Experimental")),
    dict(sid="S227", key="claude", name="Claude Code", short="claude",
         ext="md", title="Extend Claude with skills",
         url="https://code.claude.com/docs/en/skills.md",
         section="Frontmatter reference", grant="pre-approves",
         ground="without prompting you for approval",
         tokens=("allowed-tools", "comma-separated",
                 "without prompting you for approval")),
    dict(sid="S228", key="factory", name="Factory", short="factory",
         ext="md", title="Skills configuration",
         url="https://docs.factory.com/harness/skills",
         section="Declare intended tools", grant="metadata-only",
         ground="metadata",
         tokens=("allowed-tools", "sandbox", "metadata")),
    dict(sid="S229", key="msaf", name="Microsoft Agent Framework", short="msaf",
         ext="html", title="Agent Framework skills",
         url="https://learn.microsoft.com/en-us/agent-framework/agents/skills",
         section="Skills frontmatter", grant="experimental",
         ground="Experimental",
         tokens=("allowed-tools", "Space-delimited", "Experimental")),
    dict(sid="S230", key="pi", name="pi", short="pi", ext="md",
         title="Coding agent skills",
         url="https://raw.githubusercontent.com/badlogic/pi-mono/main/"
             "packages/coding-agent/docs/skills.md",
         section="Frontmatter", grant="experimental", ground="Experimental",
         tokens=("allowed-tools", "pre-approved", "Experimental")),
    dict(sid="S231", key="vibe", name="Mistral Vibe", short="vibe", ext="md",
         title="Mistral Vibe README",
         url="https://raw.githubusercontent.com/mistralai/mistral-vibe/main/"
             "README.md",
         section="Skill example", grant="unstated", ground="allowed-tools:",
         tokens=("allowed-tools", "allowed-tools:", "read", "bash")),
]
BY_SID = {s["sid"]: s for s in SURFACES}
BY_KEY = {s["key"]: s for s in SURFACES}

TOTAL = 6
SOURCES = "corpus/SOURCES.md"
ENTRY = "corpus/knowledge/allowed-tools-surfaces-round79.md"
SNAPDIR = ".ufo/waves/round-79/snapshots"
MANIFEST = SNAPDIR + "/MANIFEST.sha256"
PROVINCE = "PROVINCE.md"
SKILLMD = "SKILL.md"
COUNTER_PATH = "verifiers/check_allowed_tools.py"
CAPTURE = "2026-10-27"
FETCHED = "2026-10-27T00:00:00Z"
LANE_BASE = "b10bcbc6b00f8f56b202ccbadca311007b5b463c"
REGISTRY_HEADER = (
    "| id | source | kind | tier | scope | anchor | teaches | status | opened "
    "| recheck | used-by |\n"
    "|---|---|---|---|---|---|---|---|---|---|---|")

# --------------------------------------------------------- synthetic pages
# Fixed text, no network. Each page carries: the token `allowed-tools`, the
# surface's value-form token, the grant-ground token, and one attributable
# sentence the honest world quotes.
PAGES = {
    "S226": (
        "# Agent Skills specification\n"
        "\n"
        "## Frontmatter fields\n"
        "\n"
        "| Field | Required | Description |\n"
        "|---|---|---|\n"
        "| allowed-tools | no | Space-separated list of tools the agent may "
        "invoke without prompting. |\n"
        "\n"
        "### allowed-tools field\n"
        "\n"
        "Experimental: support for allowed-tools may vary between agent "
        "implementations.\n"
        "\n"
        "The allowed-tools value is a space-separated string of tool names.\n"),
    "S227": (
        "# Extend Claude with skills\n"
        "\n"
        "## Frontmatter reference\n"
        "\n"
        "| Field | Description |\n"
        "|---|---|\n"
        "| allowed-tools | Tools Claude can use during the turn that invokes "
        "the skill. |\n"
        "\n"
        "The allowed-tools field grants the listed tools for the turn that "
        "invokes the skill, so Claude can use them without prompting you for "
        "approval.\n"
        "\n"
        "Tools Claude can use during the turn that invokes the skill are "
        "pre-approved only for that turn.\n"
        "\n"
        "## Pre-approve tools for a skill\n"
        "\n"
        "The field accepts a space- or comma-separated string, or a YAML "
        "list, of tool names.\n"),
    "S228": (
        "# Skills configuration\n"
        "\n"
        "## Frontmatter\n"
        "\n"
        "| Field | Description |\n"
        "|---|---|\n"
        "| allowed-tools | Metadata for review and packaging; it does not add "
        "tools to the agent. |\n"
        "\n"
        "## Declare intended tools\n"
        "\n"
        "The allowed-tools field is metadata for review and packaging, and it "
        "does not add tools to the agent.\n"
        "\n"
        "It does not sandbox standard skill invocation either.\n"),
    "S229": (
        "<!doctype html>\n"
        '<html lang="en"><head><title>Agent Framework skills</title>\n'
        "<style>td{padding:0}</style>\n"
        "<script>window.__page = 1;</script>\n"
        "</head>\n"
        "<body>\n"
        "<h1>Agent Framework skills</h1>\n"
        "<table>\n"
        "<tr><th>Field</th><th>Description</th></tr>\n"
        "<tr><td>allowed-tools</td><td>Space-delimited list of pre-approved "
        "tools. Experimental, support may vary between agent "
        "implementations.</td></tr>\n"
        "</table>\n"
        "<p>Space-delimited list of pre-approved tools for the agent.</p>\n"
        "</body></html>\n"),
    "S230": (
        "# Coding agent skills\n"
        "\n"
        "## Frontmatter\n"
        "\n"
        "| Field | Description |\n"
        "|---|---|\n"
        "| allowed-tools | Experimental pre-approved tool list. |\n"
        "\n"
        "The allowed-tools field is an Experimental list of pre-approved "
        "tools for the skill.\n"
        "\n"
        "Other frontmatter fields are stable.\n"),
    "S231": (
        "# Mistral Vibe\n"
        "\n"
        "Skills live in `.vibe/skills/` and carry YAML frontmatter.\n"
        "\n"
        "```markdown\n"
        "---\n"
        "name: commit-helper\n"
        "description: Draft commit messages from the staged diff\n"
        "allowed-tools:\n"
        "  - read\n"
        "  - grep\n"
        "  - bash\n"
        "---\n"
        "```\n"
        "\n"
        "The example above ships with the CLI.\n"),
}

# The honest world's located quote per surface (5-25 words, contains
# `allowed-tools`, carries the grant-ground token, occurs in that page only).
QUOTES = {
    "S226": "Experimental: support for allowed-tools may vary between agent "
            "implementations",
    "S227": "allowed-tools field grants the listed tools for the turn that "
            "invokes the skill, so Claude can use them without prompting you "
            "for approval",
    "S228": "allowed-tools field is metadata for review and packaging, and it "
            "does not add tools to the agent",
    "S229": "allowed-tools Space-delimited list of pre-approved tools. "
            "Experimental, support may vary between agent implementations",
    "S230": "allowed-tools field is an Experimental list of pre-approved "
            "tools for the skill",
    "S231": "description: Draft commit messages from the staged diff "
            "allowed-tools: read grep bash",
}

# The shared banner C3 puts on every page: identical bytes on every host, and
# it carries every frozen page token, so only a Q70 / banner exclusion can
# reject it.
BANNER = ("Site banner: Experimental allowed-tools: metadata pre-approved "
          "tools without prompting you for approval; this does not add tools")

# C10's token-less quotes (they occur in the page, they just do not contain
# `allowed-tools`).
TOKENLESS = {
    "S227": "Tools Claude can use during the turn that invokes the skill",
    "S229": "Space-delimited list of pre-approved tools",
}

# C6's sibling hosts: same host, path prefix extended by one segment.
SIBLING_URL = {
    "S230": "https://raw.githubusercontent.com/badlogic/pi-mono-evil/main/"
            "packages/coding-agent/docs/skills.md",
    "S231": "https://raw.githubusercontent.com/mistralai/mistral-vibe-evil/"
            "main/README.md",
}

# --------------------------------------------------------------- text shaping
TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1\s*>", re.I | re.S)
ENTITY_RE = re.compile(r"&(#x?[0-9a-fA-F]+|[a-zA-Z]+);")
LIST_MARKER_RE = re.compile(r"(?m)^[ \t]{0,3}[*+\-][ \t]+")


def ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def shaped_lines(text: str, ext: str) -> list[str]:
    """The counter's snapshot text view, line by line (before whitespace
    collapse): `.html` loses script/style blocks, tags become one space and
    entities are decoded; Markdown loses every backtick byte and an unordered
    list marker; then each line's whitespace is collapsed."""
    if ext.lstrip(".").lower() in ("html", "htm"):
        text = SCRIPT_STYLE_RE.sub(" ", text)
        text = TAG_RE.sub(" ", text)
        text = ENTITY_RE.sub(lambda m: _entity(m.group(0)), text)
    elif ext.lstrip(".").lower() in ("md", "markdown"):
        text = text.replace("`", "")
        text = LIST_MARKER_RE.sub("", text)
    return [line for line in (ws(ln) for ln in text.splitlines()) if line]


def text_view(text: str, ext: str) -> str:
    """One collapsed string of the text view (the form quotes are matched in)."""
    return ws(" ".join(shaped_lines(text, ext)))


def _entity(token: str) -> str:
    import html as _html
    return _html.unescape(token)


def word_bounded(needle: str, haystack: str) -> bool:
    return re.search(r"(?<![A-Za-z0-9_])" + re.escape(needle)
                     + r"(?![A-Za-z0-9_])", haystack) is not None


def snap_name(sid: str) -> str:
    s = BY_SID[sid]
    return f"{sid}-{s['short']}.{s['ext']}"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


# ------------------------------------------------------------- world builders
def manifest_text(texts: dict[str, str]) -> str:
    return "".join(f"{sha(v)}  {k}\n" for k, v in texts.items())


def registry_text(rows: list[dict]) -> str:
    body = []
    for r in rows:
        cells = [
            r["sid"],
            f"{BY_SID[r['sid']]['title']} — {r['url']}",
            "docs",
            r["tier"],
            r["scope"],
            r["anchor"],
            r["teaches"],
            r["status"],
            r["opened"],
            r["recheck"],
            ENTRY,
        ]
        assert len(cells) == 11
        assert not any("|" in c for c in cells), cells
        body.append("| " + " | ".join(cells) + " |")
    head = ("# SOURCES fixture\n\n## Registry\n\n" + REGISTRY_HEADER + "\n")
    return head + ("\n".join(body) + "\n" if body else "")


def anchor_for(sid: str, snap: str, quote: str | None) -> str:
    s = BY_SID[sid]
    body = f"§ {s['section']}"
    if quote:
        body += f' — located quote "{quote}"'
    body += (f"; fetched {FETCHED}, HTTP 200, {len(snap.encode())} B, "
             f"sha256 {sha(snap)}")
    return body


def registry_rows(texts: dict[str, str], *, urls: dict[str, str] | None = None,
                  quotes: dict[str, str] | None = None,
                  sha_break: tuple[str, ...] = (),
                  tier: str = "B", cite: list[str] | None = None) -> list[dict]:
    """One registry row per cited id (order of `cite`, default: all six)."""
    urls = urls or {}
    quotes = QUOTES if quotes is None else quotes
    rows = []
    for sid in (cite if cite is not None else [s["sid"] for s in SURFACES]):
        anchor = anchor_for(sid, texts[snap_name(sid)], quotes.get(sid))
        if sid in sha_break:
            anchor = re.sub(r"sha256 [0-9a-f]{64}", "sha256 " + "0" * 64,
                            anchor)
        rows.append(dict(sid=sid, url=urls.get(sid, BY_SID[sid]["url"]),
                         tier="A" if sid == "S226" else tier,
                         scope="fixture scope",
                         anchor=anchor,
                         teaches="fixture: what the page says about the field",
                         status="mined", opened=CAPTURE, recheck="30d"))
    return rows


def entry_text(rows: list[dict], *, quotes: dict[str, str] | None = None,
               locate: bool = True, prose: str | None = None) -> str:
    """The entry: source lines, verified-at, recheck, then the surface table.

    `rows` is a list of dicts with sid, surface (the frozen first cell), tokens,
    grant and quote. Duplicate sids are allowed on purpose (C9). The `source:`
    lines and the table rows carry the SAME located quote for a given sid (the
    counter reads a line's single `located quote "..."` span, so two different
    quotes for one id is a finding, never a pass)."""
    quotes = QUOTES if quotes is None else quotes
    head: list[str] = []
    seen: list[str] = []
    for r in rows:
        if r["sid"] in seen:
            continue
        seen.append(r["sid"])
        s = BY_SID[r["sid"]]
        q = r.get("quote", quotes.get(r["sid"]))
        line = (f"source: {r['sid']} — {s['title']} — {r['url']} — "
                f"§ {s['section']}")
        if locate and q:
            line += f' — located quote "{q}"'
        line += f" (snapshot `{snap_name(r['sid'])}:3`)"
        head.append(line)
    out = list(head)
    out += ["", f"verified-at: {CAPTURE}",
            "recheck: 30d — curl each URL and grep -c -F 'allowed-tools' "
            "against the pinned snapshot",
            "view: `.html` snapshots lose `script` and `style` blocks, tags "
            "become one space and entities are decoded; Markdown snapshots "
            "lose every backtick byte and an unordered-list marker; every "
            "whitespace run is then collapsed.",
            "ground: fixture — the six synthetic pages of this control world",
            "", "# allowed-tools surfaces (fixture)", ""]
    if prose:
        out += [prose, ""]
    out += ["| surface | source | page tokens | grant | located quote |",
            "|---|---|---|---|---|"]
    for r in rows:
        toks = ", ".join("`" + t + "`" for t in r["tokens"])
        q = r.get("quote", quotes.get(r["sid"]))
        cell = f'located quote "{q}"' if q else "not quoted"
        out.append(f"| {r['surface']} | {r['sid']} | {toks} | {r['grant']} "
                   f"| {cell} |")
    out += ["", "## Limits", "",
            "Synthetic fixture bytes; the counter reads cells and tokens only.",
            ""]
    return "\n".join(out)


PROVINCE_OK = (
    "# fixture province\n\n## Core\n\n"
    "- `allowed-tools` surfaces: what the field means in the Open specification, "
    "Claude Code, Factory, Microsoft Agent Framework, pi and Mistral Vibe, in "
    f"`{ENTRY}`, counted by the counter.\n\n## Frontier\n\n- none\n")


def skill_ok() -> str:
    return (
        "# fixture skill\n\n## Rules\n\n"
        "- `allowed-tools` means different things per client: the Open "
        "specification marks it experimental, Claude Code pre-approves per "
        "turn, Factory calls it metadata, pi and the Microsoft Agent Framework "
        "call it experimental, and Mistral Vibe's example shows an unstated "
        f"YAML list — see `{ENTRY}`.\n\n## Gate registry\n\n"
        "| Name | Kind | Entry command | Verdict map | Self-test | Pinned "
        "values | Write scope | Owner |\n"
        "|---|---|---|---|---|---|---|---|\n"
        f"| `{COUNTER_PATH}` | gate | `python3 -B {COUNTER_PATH} --rev <rev>` "
        "| 0=backed, 1=content verdict, 2=could-not-evaluate | `--self-test` "
        "| in-file | none | kotoba |\n")


def row(sid: str, **kw) -> dict:
    s = BY_SID[sid]
    base = dict(sid=sid, surface=s["name"], tokens=s["tokens"],
                grant=s["grant"], url=s["url"])
    base.update(kw)
    return base


def honest_world(quotes: dict[str, str] | None = None,
                 *, urls: dict[str, str] | None = None) -> dict:
    """H and the base of every one-conjunct world: six honest rows, six
    snapshots, a manifest whose pins are the snapshot digests, six mined
    registry rows, an honest province and an honest SKILL.md."""
    quotes = QUOTES if quotes is None else quotes
    texts = {snap_name(s["sid"]): PAGES[s["sid"]] for s in SURFACES}
    files = {
        SOURCES: registry_text(registry_rows(texts, urls=urls, quotes=quotes)),
        ENTRY: entry_text([row(s["sid"]) for s in SURFACES], quotes=quotes),
        MANIFEST: manifest_text(texts),
        PROVINCE: PROVINCE_OK,
        SKILLMD: skill_ok(),
    }
    for name, text in texts.items():
        files[f"{SNAPDIR}/{name}"] = text
    return files


def world_files(name: str) -> tuple[dict, list[str], str | None]:
    """(files, notes, measured_rev_or_None). `None` as a file value deletes a
    base-tree path; a `None` rev means "measure the base revision" (C0)."""
    notes: list[str] = []
    if name == "C0":
        return {}, ["measures the base revision itself (no world commit)"], None

    files = honest_world()
    texts = {snap_name(s["sid"]): PAGES[s["sid"]] for s in SURFACES}

    if name == "H":
        return files, ["honest six-surface world (plumbing oracle)"], "HEAD"

    if name == "C1":
        rows = [row(s["sid"]) for s in SURFACES]
        for n in list(texts):
            files.pop(f"{SNAPDIR}/{n}", None)
        files.pop(MANIFEST, None)
        files[ENTRY] = entry_text(rows)
        files[SOURCES] = registry_text(registry_rows(texts))
        return files, ["entry names every token and label; no snapshot, no "
                       "manifest, pins point at bytes that are not there"], "HEAD"

    if name == "C2":
        order = [s["sid"] for s in SURFACES]
        shifted = {sid: QUOTES[order[(i + 1) % len(order)]]
                   for i, sid in enumerate(order)}
        files[ENTRY] = entry_text([row(s["sid"]) for s in SURFACES],
                                  quotes=shifted)
        files[SOURCES] = registry_text(registry_rows(texts, quotes=shifted))
        return files, ["every row quotes another surface's page text"], "HEAD"

    if name == "C3":
        banner_texts = {n: BANNER + "\n\n" + t for n, t in texts.items()}
        shared = {s["sid"]: BANNER for s in SURFACES}
        files[ENTRY] = entry_text([row(s["sid"]) for s in SURFACES],
                                  quotes=shared)
        files[MANIFEST] = manifest_text(banner_texts)
        files[SOURCES] = registry_text(
            registry_rows(banner_texts, quotes=shared))
        for n, t in banner_texts.items():
            files[f"{SNAPDIR}/{n}"] = t
        return files, ["one banner line, identical in all six snapshots, is "
                       "the located quote of every row"], "HEAD"

    if name == "C4":
        return _script_only(files, texts)

    if name == "C5":
        rows = [row(s["sid"], quote=None) for s in SURFACES]
        files[ENTRY] = entry_text(rows, locate=False)
        files[SOURCES] = registry_text(registry_rows(texts, quotes={}))
        return files, ["grant labels and page tokens, no quote anywhere"], "HEAD"

    if name == "C6":
        files = honest_world(urls=SIBLING_URL)
        files[ENTRY] = entry_text([row(s["sid"], url=SIBLING_URL.get(
            s["sid"], s["url"])) for s in SURFACES])
        files[SOURCES] = registry_text(registry_rows(texts, urls=SIBLING_URL))
        return files, ["two rows cite `…-evil/…` siblings of the frozen "
                       "host+path prefixes (pi-mono-evil, mistral-vibe-evil)"], \
            "HEAD"

    if name == "C7":
        tampered = PAGES["S230"] + ("\nTampered bytes added after the pin "
                                    "was written.\n")
        files[MANIFEST] = manifest_text(texts)          # pins the honest bytes
        files[f"{SNAPDIR}/{snap_name('S230')}"] = tampered
        return files, ["pi snapshot bytes changed after the pin was written "
                       "(the pin and the anchor still name the old bytes)"], \
            "HEAD"

    if name == "C7a":
        files[SOURCES] = registry_text(
            registry_rows(texts, sha_break=("S230", "S231")))
        return files, ["pi's and vibe's registry anchors carry a wrong sha "
                       "while manifest and snapshot bytes are intact"], "HEAD"

    if name == "C8":
        rows = [row(s["sid"], tokens=("allowed-tools",), quote=None)
                for s in SURFACES]
        for n in list(texts):
            files.pop(f"{SNAPDIR}/{n}", None)
        files.pop(MANIFEST, None)
        files[SOURCES] = registry_text([])
        files[ENTRY] = entry_text(
            rows, locate=False,
            prose="The census counts six pages that state the field, so all "
                  "six surfaces are backed (6 of 6) with no snapshot at all.")
        return files, ["the first answer from the census: 6 of 6 asserted in "
                       "prose, no snapshot, no registry row, no pin"], "HEAD"

    if name == "C9":
        rows = [row(s["sid"]) for s in SURFACES]
        rows.append(row("S230"))                       # second pi row
        files[ENTRY] = entry_text(rows)
        return files, ["two rows for surface `pi` (same id, same cells)"], "HEAD"

    if name == "C10":
        quotes = dict(QUOTES)
        quotes.update(TOKENLESS)
        files[ENTRY] = entry_text([row(s["sid"]) for s in SURFACES],
                                  quotes=quotes)
        files[SOURCES] = registry_text(registry_rows(texts, quotes=quotes))
        return files, ["claude and msaf quotes occur in the page but do not "
                       "contain `allowed-tools`"], "HEAD"

    raise SystemExit(f"unknown world {name}")


def view_lines(text: str, ext: str) -> list[str]:
    """Non-empty shaped lines of the text view."""
    return [line for line in shaped_lines(text, ext) if line]


def _derived_quote(text: str, ext: str, tok: str, ground: str) -> str | None:
    """Mechanical quote: a whole non-heading body line carrying both tokens in
    5-25 words and holding no `|`; failing that, the shortest cross-line window
    that STARTS on a body line outside the first-heading block (the frozen Q70
    reading, which the plan states, so a competent scraper applies it)."""
    lines = shaped_lines(text, ext)
    first_head = next((i for i, ln in enumerate(lines) if ln.startswith("#")),
                      None)
    for line in lines:
        if not line or line.startswith("#") or "|" in line:
            continue
        if 5 <= len(line.split()) <= 25 and tok in line and ground in line:
            return line
    words: list[str] = []
    line_of: list[int] = []
    for i, line in enumerate(lines):
        for w in line.split():
            words.append(w)
            line_of.append(i)
    for i in range(len(words)):
        if lines[line_of[i]].startswith("#"):
            continue
        if first_head is not None and line_of[i] <= first_head + 1:
            continue
        for j in range(i + 5, min(i + 26, len(words) + 1)):
            cand = " ".join(words[i:j])
            if "|" in cand:
                continue
            if tok in cand and ground in cand:
                return cand
    return None


def _script_only(files: dict, texts: dict[str, str]) -> tuple[dict, list, str]:
    """C4: build the entry with no judgement at all.

    The script takes the fixed page text, extracts a quote mechanically (the
    first shaped line carrying `allowed-tools` and the grant-ground token in
    5-25 words, else the shortest cross-line window), counts the backticked
    tokens by looking the frozen token table up, takes the grant label from the
    same table, computes the pins from the snapshot bytes and assembles the
    registry rows. Every value that a reader would judge (which label, which
    token) is supplied by the frozen table, not by the page.
    """
    derived: dict[str, str] = {}
    for s in SURFACES:
        q = _derived_quote(PAGES[s["sid"]], s["ext"], "allowed-tools",
                           s["ground"])
        if q is None:
            raise SystemExit(
                f"C4 extraction failed for {s['sid']}: no 5-25 word quote "
                f"contains both `allowed-tools` and {s['ground']!r}")
        derived[s["sid"]] = q
    rows = []
    for s in SURFACES:
        toks = []
        for t in s["tokens"]:
            if word_bounded(t, text_view(PAGES[s["sid"]], s["ext"])):
                toks.append(t)
        if "allowed-tools" not in toks:
            toks.insert(0, "allowed-tools")
        rows.append(row(s["sid"], tokens=tuple(toks), quote=derived[s["sid"]]))
    files[ENTRY] = entry_text(rows, quotes=derived)
    files[SOURCES] = registry_text(registry_rows(texts, quotes=derived))
    files[MANIFEST] = manifest_text(texts)
    notes = ["script-generated entry: quote = minimal 5-25 word window holding "
             "`allowed-tools` + the label's ground token; tokens and labels "
             "looked up in the frozen table; pins computed from bytes"]
    for sid in [s["sid"] for s in SURFACES]:
        notes.append(f"derived {sid}: {derived[sid]}")
    return files, notes, "HEAD"


def _window(view: str, tok: str, ground: str) -> str | None:
    """The shortest 5-25 word window holding both tokens.

    A window containing `|` is skipped: the located quote is a table cell, and
    an inner pipe would turn one row into several (a different defect than the
    one this world tests), so the script keeps extending past the table markup.
    """
    words = view.split()
    for i in range(len(words)):
        for j in range(i + 5, min(i + 26, len(words) + 1)):
            cand = " ".join(words[i:j])
            if "|" in cand:
                continue
            if tok in cand and ground in cand:
                return cand
    return None


# ------------------------------------------------------------- git plumbing
class GitError(RuntimeError):
    pass


def git(repo: Path, args: list[str], stdin: bytes | None = None,
        check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(["git", "-C", str(repo), *args], input=stdin,
                          capture_output=True)
    if check and proc.returncode != 0:
        raise GitError(f"git -C {repo} {' '.join(args)}: "
                       f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc


def build_world(work: Path, base: Path, base_rev: str,
                files: dict[str, str | None],
                counter_bytes: bytes | None,
                tag: str) -> tuple[Path, str]:
    d = Path(tempfile.mkdtemp(prefix=f"{tag}-", dir=str(work)))
    try:
        git(d, ["init", "-q"])
        git(d, ["config", "user.name", "scratch-r79"])
        git(d, ["config", "user.email", "scratch@example.invalid"])
        top = git(d, ["rev-parse", "--show-toplevel"]).stdout.decode().strip()
        if Path(top).resolve() != d.resolve():
            raise GitError(f"fixture toplevel {top!r} is not {d}")
        # Lineage: share the base clone's object store read-only so the frozen
        # BASE_REV is resolvable inside the world (see the module docstring).
        obj = git(base, ["rev-parse", "--git-path", "objects"]).stdout.decode()
        obj_path = Path(obj.strip())
        if not obj_path.is_absolute():
            obj_path = (base / obj_path).resolve()
        info = d / ".git" / "objects" / "info"
        info.mkdir(parents=True, exist_ok=True)
        (info / "alternates").write_text(str(obj_path) + "\n")
        if git(d, ["cat-file", "-t", f"{base_rev}^{{commit}}"],
               check=False).returncode != 0:
            raise GitError(f"base revision {base_rev} is not readable through "
                           f"the alternate {obj_path}")
        if files or counter_bytes is not None:
            git(d, ["read-tree", base_rev])
        for rel, text in files.items():
            if text is None:
                git(d, ["update-index", "--force-remove", rel], check=False)
                continue
            blob = git(d, ["hash-object", "-w", "--stdin"],
                       stdin=text.encode()).stdout.decode().strip()
            git(d, ["update-index", "--add", "--cacheinfo",
                    f"100644,{blob},{rel}"])
        if counter_bytes is not None:
            blob = git(d, ["hash-object", "-w", "--stdin"],
                       stdin=counter_bytes).stdout.decode().strip()
            git(d, ["update-index", "--add", "--cacheinfo",
                    f"100755,{blob},{COUNTER_PATH}"])
        tree = git(d, ["write-tree"]).stdout.decode().strip()
        commit = git(d, ["commit-tree", tree, "-p", base_rev],
                     stdin=f"c2r79 control world {tag}\n".encode()
                     ).stdout.decode().strip()
        git(d, ["update-ref", f"refs/heads/{tag}", commit])
        return d, commit
    except Exception:
        shutil.rmtree(d, ignore_errors=True)
        raise


def run_counter(counter: Path, world: Path, rev: str,
                timeout: int) -> tuple[int, str]:
    proc = subprocess.run(
        [sys.executable, "-B", str(counter), "--repo", str(world),
         "--rev", rev],
        capture_output=True, text=True, cwd=str(world), timeout=timeout)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


N_RE = re.compile(r"allowed-tools surfaces backed (\d+) of (\d+)\s*$")
SCRIPT_RE = re.compile(r"script-only world: (\d+) of (\d+)\s*$")
OTHER_RE = re.compile(r"^(held at base:.*|province surfaces named.*|registry "
                      r"home.*|opened this round.*|measured-rev:.*)$")


def parse_output(out: str) -> dict:
    res = {"n": None, "of": None, "script": None, "other": [], "findings": [],
           "error": None}
    for line in out.splitlines():
        bare = line.rstrip()
        if bare != bare.lstrip():          # indented: a finding, not a verdict
            if bare.strip():
                res["findings"].append(bare.strip())
            continue
        m = N_RE.match(bare)
        if m and res["n"] is None:
            res["n"], res["of"] = int(m.group(1)), int(m.group(2))
            continue
        m = SCRIPT_RE.match(bare)
        if m and res["script"] is None:
            res["script"] = f"{int(m.group(1))} of {int(m.group(2))}"
            continue
        m = OTHER_RE.match(bare)
        if m:
            res["other"].append(bare)
            continue
        if bare.startswith("environment error"):
            res["error"] = bare
    return res


# ------------------------------------------------- pre-registered expectation
def expect(name: str) -> dict:
    return EXPECT[name]


EXPECT: dict[str, dict] = {
    "H": dict(n_in=(6,), exit_in=(0,), what="honest six-surface world (plumbing "
              "oracle, NOT a control: it says whether this generator and the "
              "counter can agree on a well-formed world at all)",
              defect="any divergence is a generator/counter plumbing "
                     "mismatch, never claim evidence"),
    "C0": dict(n_in=(0,), exit_in=(1,), what="base copy: nothing done",
               defect="N >= 1, or exit 0"),
    "C1": dict(n_in=(0, None), exit_in=(1, 2), what="token dump: every token, "
               "label and quote, no snapshot, no manifest (a missing manifest "
               "is `could not evaluate`, never a backed surface)",
               defect="N >= 1, or exit 0"),
    "C2": dict(n_in=(0,), exit_in=(1,), what="wrong-page text: every quote "
               "taken from another surface's page",
               defect="N >= 1, or exit 0"),
    "C3": dict(n_in=(0,), exit_in=(1,), what="shared banner: one banner line, "
               "identical in all six snapshots, quoted by every row",
               defect="N >= 1 (a banner/subtitle accepted as a located "
                      "quote); >= 5 is the plan's defect threshold"),
    "C4": dict(n_in=(6,), exit_in=(0,), what="script-only scrape: form "
               "generated mechanically from fixed text with pins, quotes and "
               "labels",
               defect="NOT a defect: Q71 form-level world; N <= 5 means the "
                      "counter rejects mechanically-correct form (a finding, "
                      "not a counter defect)"),
    "C5": dict(n_in=(0, None), exit_in=(1, 2), what="label-only: grant labels "
               "and page tokens, no quote anywhere",
               defect="N >= 1, or exit 0"),
    "C6": dict(n_in=(4,), exit_in=(1,), what="sibling host: pi-mono-evil and "
               "mistral-vibe-evil URLs (a string-prefix test passes them)",
               defect="N >= 5, or exit 0"),
    "C7": dict(n_in=(None,), exit_in=(1, 2), what="tampered snapshot: pi's "
               "committed bytes changed after the pin was written (the other "
               "pin probes live in C7a, because a tampered pin aborts the "
               "evaluation before any later surface is read)",
               defect="exit 0, or a verdict line claiming a full count from "
                      "bytes that do not hash to their pin"),
    "C7a": dict(n_in=(4,), exit_in=(1,), what="wrong sha pin: pi's and vibe's "
                "registry anchors carry a sha that is not the pin (snapshot "
                "bytes intact)",
                defect="N >= 5, or exit 0"),
    "C8": dict(n_in=(0,), exit_in=(1,), what="first-answer baseline: 6 of 6 "
               "asserted from the census, no snapshot, no row, no pin",
               defect="N >= 1, or exit 0"),
    "C9": dict(n_in=(5,), exit_in=(0, 1), what="duplicate row: two rows for "
               "`pi`",
               defect="N = 6 (the duplicate was counted twice). N = 5 is the "
                      "surface disqualified: the target is still met by the "
                      "frozen rule, so the L1 records it as the plan's own "
                      "arithmetic and reads the N value, not the exit code"),
    "C10": dict(n_in=(4,), exit_in=(1,), what="quote without the token: claude "
                "and msaf quote page sentences that lack `allowed-tools`",
                defect="N >= 5, or exit 0"),
}
ORDER = ["H", "C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C7a", "C8",
         "C9", "C10"]


# ------------------------------------------------------------- self-check
def self_check() -> list[str]:
    """Fixture invariants, checked before any world is built.

    Not a counter check: this is the generator's own arithmetic — every honest
    quote is 5-25 words, occurs in its own page's text view, carries the grant
    ground token and the token `allowed-tools`, and occurs in no other page."""
    errs: list[str] = []
    views = {sid: text_view(t, BY_SID[sid]["ext"]) for sid, t in PAGES.items()}
    for sid, q in QUOTES.items():
        s = BY_SID[sid]
        words = len(q.split())
        if not 5 <= words <= 25:
            errs.append(f"{sid}: quote is {words} words")
        if q not in views[sid]:
            errs.append(f"{sid}: quote is not a substring of its own page")
        if "allowed-tools" not in q:
            errs.append(f"{sid}: quote lacks `allowed-tools`")
        if s["ground"] not in q:
            errs.append(f"{sid}: quote lacks its ground token {s['ground']!r}")
        for other, v in views.items():
            if other != sid and q in v:
                errs.append(f"{sid}: quote also occurs in {other} (Q70)")
        for t in s["tokens"]:
            if not word_bounded(t, views[sid]):
                errs.append(f"{sid}: token {t!r} not word-bounded in page")
    if len(BANNER.split()) > 25:
        errs.append("C3 banner exceeds 25 words")
    for sid, q in TOKENLESS.items():
        if q not in views[sid]:
            errs.append(f"C10 {sid}: token-less quote is not in the page")
        if "allowed-tools" in q:
            errs.append(f"C10 {sid}: token-less quote contains the token")
    for sid, url in SIBLING_URL.items():
        host_pin = BY_SID[sid]["url"].split("/main/")[0]
        if not url.startswith(host_pin):
            errs.append(f"C6 {sid}: sibling URL does not extend the prefix")
    return errs


# ------------------------------------------------------------------- driver
def compare(name: str, code: int, parsed: dict) -> tuple[bool, str]:
    exp = EXPECT[name]
    n = parsed["n"]
    ok_n = n in exp["n_in"]
    ok_exit = code in exp["exit_in"]
    ok = ok_n and ok_exit
    bits = []
    if not ok_n:
        bits.append(f"N={n!r} (pre-registered {exp['n_in']})")
    if not ok_exit:
        bits.append(f"exit {code} (pre-registered {exp['exit_in']})")
    return ok, ("as-expected" if ok else "DIVERGES: " + "; ".join(bits))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="C2 control worlds for kotoba round 79 (plan § C2)")
    ap.add_argument("--counter", required=False,
                    help="path to the frozen C2 counter "
                         "(verifiers/check_allowed_tools.py)")
    ap.add_argument("--base-tree", default="/home/vgpnk/Projects/shokunin/"
                    "kotoba-shokunin",
                    help="lane clone whose object store supplies the base "
                         "lineage (read-only)")
    ap.add_argument("--base-rev", default=LANE_BASE,
                    help="base revision the frozen counters read as BASE_REV")
    ap.add_argument("--work", default=None,
                    help="scratch dir for the worlds (default: mktemp -d "
                         "under $TMPDIR)")
    ap.add_argument("--only", default=None,
                    help="comma-separated world names, e.g. C3,C6")
    ap.add_argument("--keep", action="store_true", help="keep world repos")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--list", action="store_true",
                    help="print the pre-registered expectation table and exit")
    ap.add_argument("--json", action="store_true", help="machine summary")
    ap.add_argument("--out", default=None, help="receipt file for the full log")
    ap.add_argument("--timeout", type=int, default=300,
                    help="per-counter-run timeout (s)")
    args = ap.parse_args(argv)

    if args.list:
        print("world  expected N  expected exit  what it breaks")
        for name in ORDER:
            e = EXPECT[name]
            print(f"{name:<6} {e['n_in']!s:<11} {e['exit_in']!s:<14} "
                  f"{e['what']}")
            print(f"       defect signature: {e['defect']}")
        print("\nH is the honest plumbing oracle, not a control: it must "
              "reach 6 of 6 exit 0 or the generator/counter pair is broken.")
        return 0

    if not args.counter:
        print("environment: --counter is required (the frozen counter file)",
              file=sys.stderr)
        return 2
    counter = Path(args.counter)
    if not counter.is_file():
        print(f"environment: counter {counter} is not a file", file=sys.stderr)
        return 2
    counter = counter.resolve()
    base = Path(args.base_tree)
    if not base.is_dir():
        print(f"environment: base tree {base} is not a directory",
              file=sys.stderr)
        return 2
    base = base.resolve()
    proc = git(base, ["rev-parse", "--verify", "-q",
                      f"{args.base_rev}^{{commit}}"], check=False)
    if proc.returncode != 0:
        print(f"environment: {args.base_rev} is not a commit in {base}",
              file=sys.stderr)
        return 2
    base_rev = proc.stdout.decode().strip()

    errs = self_check()
    if errs:
        print("generator self-check FAILED (fixtures, not the counter):",
              file=sys.stderr)
        for e in errs:
            print("  " + e, file=sys.stderr)
        return 2

    work = Path(args.work) if args.work else Path(tempfile.mkdtemp(
        prefix="c2r79-", dir=os.environ.get("TMPDIR")))
    work.mkdir(parents=True, exist_ok=True)
    counter_bytes = counter.read_bytes()

    names = [n.strip() for n in args.only.split(",")] if args.only else ORDER
    unknown = [n for n in names if n not in ORDER]
    if unknown:
        print(f"environment: unknown world(s) {unknown}", file=sys.stderr)
        return 2

    log: list[str] = []
    summary: list[dict] = []

    def say(line: str = "") -> None:
        print(line)
        log.append(line)

    say(f"c2_controls: counter={counter}")
    say(f"c2_controls: base-tree={base} base-rev={base_rev}")
    say(f"c2_controls: work={work}  worlds={','.join(names)}")
    say("")

    failures = 0
    for name in names:
        files, notes, rev_sel = world_files(name)
        world: Path | None = None
        try:
            try:
                world, commit = build_world(work, base, base_rev, files,
                                            counter_bytes, name)
            except (GitError, OSError) as exc:
                say(f"=== {name} === BUILD FAILED: {exc}")
                summary.append(dict(world=name, build="failed",
                                    error=str(exc)))
                failures += 1
                continue
            rev = base_rev if rev_sel is None else commit
            try:
                code, out = run_counter(counter, world, rev, args.timeout)
            except subprocess.TimeoutExpired:
                say(f"=== {name} === COUNTER TIMEOUT after {args.timeout}s")
                summary.append(dict(world=name, world_dir=str(world),
                                    rev=rev, timeout=True))
                failures += 1
                continue
            parsed = parse_output(out)
            n_line = ("allowed-tools surfaces backed "
                      f"{parsed['n']} of {parsed['of']}") if parsed["n"] is not None \
                else "(no verdict line)"
            ok, verdict = compare(name, code, parsed)
            if not ok:
                failures += 1
            say(f"=== {name} === {EXPECT[name]['what']}")
            say(f"    world-rev: {rev}")
            say(f"    {n_line}")
            if parsed["script"]:
                say(f"    script-only world: {parsed['script']}")
            for o in parsed["other"]:
                say(f"    {o}")
            if parsed["error"]:
                say(f"    {parsed['error']}")
            for f in parsed["findings"]:
                if name == "H" or args.verbose or not ok:
                    say(f"    finding: {f}")
            say(f"    counter exit: {code}")
            say(f"    pre-registered: N in {EXPECT[name]['n_in']} exit in "
                f"{EXPECT[name]['exit_in']} — {verdict}")
            say(f"    defect signature: {EXPECT[name]['defect']}")
            for note in notes:
                say(f"    note: {note}")
            if args.verbose or not ok:
                say("    --- counter output ---")
                for line in out.rstrip("\n").splitlines():
                    say("    | " + line)
                say("    --- end ---")
            say("")
            summary.append(dict(world=name, world_dir=str(world), rev=rev,
                                exit=code, n=parsed["n"], of=parsed["of"],
                                script=parsed["script"], other=parsed["other"],
                                error=parsed["error"], verdict=verdict,
                                as_expected=ok, notes=notes))
        finally:
            if world is not None and not args.keep:
                shutil.rmtree(world, ignore_errors=True)

    say(f"c2_controls: {len(names)} world(s), {failures} divergence(s); "
        f"pre-registration is evidence, the L1 judges")
    if not args.keep and not args.only:
        try:
            work.rmdir()
        except OSError:
            pass

    if args.json:
        print(json.dumps(dict(counter=str(counter), base=str(base),
                              base_rev=base_rev, worlds=summary),
                         indent=1))
    if args.out:
        Path(args.out).write_text("\n".join(log) + "\n")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
