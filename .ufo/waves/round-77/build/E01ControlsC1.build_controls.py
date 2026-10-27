#!/usr/bin/env python3
"""E01ControlsC1 -- Q37 control worlds for the frozen C1 counter (kotoba r77).

Builds six isolated scratch git repos on the *frozen* counter blob
(``verifiers/check_desc_craft.py`` sha256 cf3c45d9...) and scores each one by
running the frozen counter over that world:

    python3 -B <counter-copy> --repo <world> --rev <world-head>

Five worlds must fail (W1..W5, one shortcut each); one world (W0) is the
attribution arm and must reach the target.  Every run's exit status is the
process's own (``subprocess`` return code) -- never a pipeline's.

Scratch: ``--work`` then ``TMPDIR`` (a TMPDIR under /tmp is refused) then
/fast/scratch/hyaku/kotoba-r77/E01ControlsC1.  Nothing is written outside the
scratch root and the receipt path.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
LANE_HEAD = "6523aced1ee0ebe07dca996213bdc645a6acbd1e"
CLAIM_BASE = "2f675548eaad2a037a899d39247c1fd7a88aaf48"
COUNTER_REL = "verifiers/check_desc_craft.py"
COUNTER_SHA = "cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e"
DEFAULT_WORK = Path("/fast/scratch/hyaku/kotoba-r77/E01ControlsC1")
DEFAULT_RECEIPT = (LANE / ".ufo/waves/round-77/build"
                   / "E01ControlsC1.c1-controls.txt")

ENTRY = "corpus/knowledge/description-craft-round76.md"
SOURCES = "corpus/SOURCES.md"
SKILLMD = "SKILL.md"
LESSON = "corpus/lessons/round-76.md"
SNAPDIR = ".ufo/waves/round-76/snapshots"
PAGES = ("optimizing-descriptions", "evaluating-skills", "best-practices")
OD = "optimizing-descriptions"
OD_URL = "https://agentskills.io/skill-creation/optimizing-descriptions.md"
OLD_USED_BY = "corpus/knowledge/skill-eval-artefacts-round70.md"
CONJUNCTS = ("a", "b", "c", "d", "e", "f")
TOTAL = 6

# Located quotes from the committed optimizing-descriptions snapshot.  Every
# one is verified below with the frozen counter's own helpers before it is
# written into a world: one physical line, after the page's first heading,
# absent from the other two snapshots.
OD_QUOTES = (
    "A skill only helps if it gets activated.",
    "This means the description carries the entire burden of triggering.",
    "Describe what the user is trying to achieve, not the skill's "
    "internal mechanics.",
    "The most useful should-trigger queries are ones where the skill would "
    "help but the connection isn't obvious from the query alone.",
    "The basic approach: run each query through your agent with the skill "
    "installed and observe whether the agent invokes it.",
)

# Real sentences from the committed best-practices snapshot: the wrong page.
BP_QUOTES = (
    "The key is feeding domain-specific context into the creation process.",
    "Complete a real task in conversation with an agent, providing context, "
    "corrections, and preferences along the way.",
    "The key is project-specific material, not generic references.",
    "Every token in your skill competes for the agent's attention with "
    "everything else in that window.",
    "The first draft of a skill usually needs refinement.",
)

ROW = (
    "| write the `description` as an instruction about user intent, and be "
    "pushy about the contexts it covers | S213 optimizing-descriptions; "
    "`" + ENTRY + "` | Quote the page's own wording: \"Frame the description "
    "as an instruction to the agent\", \"Err on the side of being pushy\" "
    "about contexts a user may not name, and keep the trigger surface out of "
    "the body prose. |"
)

ROW_ANCHOR = "| confirm discovery before trusting a path |"

RESULT_RE = re.compile(r"^\(([a-f])\) [^:]+: (pass|fail)$")


# ------------------------------------------------------------------- helpers

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(repo: Path, *args: str,
        env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True, env=env)


def must(proc: subprocess.CompletedProcess, what: str) -> subprocess.CompletedProcess:
    if proc.returncode != 0:
        raise SystemExit(f"FATAL {what}: exit {proc.returncode}\n"
                         f"{proc.stdout}{proc.stderr}")
    return proc


def show(clone: Path, rev: str, rel: str) -> bytes:
    proc = subprocess.run(["git", "-C", str(clone), "show", f"{rev}:{rel}"],
                          capture_output=True)
    if proc.returncode != 0:
        raise SystemExit(f"FATAL git show {rev}:{rel}: "
                         f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout


def load_counter(path: Path):
    spec = importlib.util.spec_from_file_location("e01_counter", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def line_of(snaps, page: str, quote: str) -> int:
    lines = snaps.line_numbers(page, quote)
    if not lines:
        raise SystemExit(f"FATAL quote is not on a single line of {page}: "
                         f"{quote!r}")
    return lines[0]


# ------------------------------------------------------------------- content

def skill_with_row(skill_text: str) -> str:
    lines = skill_text.split("\n")
    hits = [i for i, ln in enumerate(lines) if ln.startswith(ROW_ANCHOR)]
    if len(hits) != 1:
        raise SystemExit(f"FATAL Body craft anchor found {len(hits)} times")
    lines.insert(hits[0] + 1, ROW)
    return "\n".join(lines)


def sources_with_used_by(text: str) -> str:
    out: list[str] = []
    changed = 0
    for line in text.split("\n"):
        if line.startswith("| S213 |"):
            cells = line.strip().strip("|").split("|")
            if cells[-1].strip() != OLD_USED_BY:
                raise SystemExit(f"FATAL S213 used-by cell is "
                                 f"{cells[-1]!r}, not {OLD_USED_BY!r}")
            cells[-1] = (f" {OLD_USED_BY}, {ENTRY} ")
            line = "|" + "|".join(cells) + "|"
            changed += 1
        out.append(line)
    if changed != 1:
        raise SystemExit(f"FATAL S213 row found {changed} times")
    return "\n".join(out)


def lesson_text(od_digest: str) -> str:
    return "\n".join([
        "# Round 76 lessons -- kotoba (control world E01ControlsC1)",
        "",
        "## Gate",
        "",
        "Source opened this round: " + OD_URL + " (2026-10-27), HTTP 200.",
        "Located quote: \"Err on the side of being pushy\" (7 words) at "
        "`optimizing-descriptions.md:27`.",
        "Snapshot set: `" + SNAPDIR + "/MANIFEST.sha256` pins the pages and "
        "`fetch-record.json` records their fetches; optimizing-descriptions "
        "digest " + od_digest + ".",
        "",
        "## Registry changes",
        "",
        "S213 `used-by` changed old -> new: `" + OLD_USED_BY + "` -> `"
        + OLD_USED_BY + ", " + ENTRY + "`.",
        "",
    ])


def entry_text(head_quote: str, head_line: int,
               rows: list[tuple[str, str, int]],
               audit_desc: int, audit_first: int,
               page: str = OD) -> str:
    """The honest entry shape; `rows` are (quote, rule, page-line) triples."""
    head = [
        f"source: S213 -- Agent Skills -- {OD_URL} -- section Writing "
        f"effective descriptions (`{OD}.md:{head_line}`) -- located quote "
        f"\"{head_quote}\"",
        "verified-at: 2026-10-27",
        f"recheck: 90d -- `grep -c -F -- \"Err on the side of being pushy\" "
        f"{SNAPDIR}/{OD}.md` prints 1",
        "ground: control world E01ControlsC1 -- every quote below is one "
        "line of the committed S213 snapshot; the audit numbers are the "
        "counter's own render of this world's SKILL.md.",
        "",
        "# Writing a skill's `description` -- S213, admitted and summed",
        "",
        "| page | S id | rule | quote | location | token | action |",
        "|---|---|---|---|---|---|---|",
    ]
    body = [
        f"| {page} | S213 | {rule} | \"{quote}\" | `{page}.md:{n}` | "
        f"token | action |"
        for quote, rule, n in rows
    ]
    tail = [
        "",
        "## This lane's own `description`, measured",
        "",
        "| measured field | value | how measured |",
        "|---|---|---|",
        f"| rendered `description` length (characters) | {audit_desc} | the "
        "YAML folded block, clip chomping |",
        f"| first sentence length (characters) | {audit_first} | the same "
        "render to the first `. ` boundary, period included |",
        "",
    ]
    return "\n".join(head + body + tail)


def token_entry() -> str:
    names = ("(a) snapshot chain (b) located quotes (c) act-on "
             "(d) self-audit (e) registry (f) provenance")
    return "\n".join([
        f"source: S213 -- Agent Skills -- {OD_URL} -- {names}",
        "verified-at: 2026-10-27",
        "recheck: 90d",
        "",
        "# " + names,
        "",
        "All six conjuncts are covered; see the names above.",
        "",
    ])


def stub_entry() -> str:
    return "\n".join([
        "# Description craft -- S213",
        "",
        "TODO: land the quotes, the audit table and the registry cell.",
        "",
    ])


# ------------------------------------------------------------------- worlds

def make_world(root: Path, name: str, files: dict[str, bytes]) -> Path:
    d = Path(tempfile.mkdtemp(prefix=name + "-", dir=str(root)))
    must(git(d, "init", "-q"), f"{name}: git init")
    must(git(d, "config", "user.name", "scratch-r77"), f"{name}: config name")
    must(git(d, "config", "user.email", "scratch@example.invalid"),
         f"{name}: config email")
    top = must(git(d, "rev-parse", "--show-toplevel"),
               f"{name}: rev-parse toplevel").stdout.strip()
    if Path(top).resolve() != d.resolve():
        raise SystemExit(f"FATAL {name}: toplevel {top!r} != {d}")
    for rel, data in files.items():
        p = d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    env = dict(os.environ,
               GIT_AUTHOR_NAME="scratch-r77",
               GIT_AUTHOR_EMAIL="scratch@example.invalid",
               GIT_COMMITTER_NAME="scratch-r77",
               GIT_COMMITTER_EMAIL="scratch@example.invalid")
    subprocess.run(["git", "-c", "commit.gpgsign=false", "-C", str(d),
                    "add", "-A"], check=True, capture_output=True, env=env)
    subprocess.run(["git", "-c", "commit.gpgsign=false", "-C", str(d),
                    "commit", "-qm", f"E01ControlsC1 {name}", "--allow-empty"],
                   check=True, capture_output=True, env=env)
    return d


def score(python: str, counter: Path, world: Path) -> dict:
    rev = must(git(world, "rev-parse", "HEAD"), "world rev").stdout.strip()
    cmd = [python, "-B", str(counter), "--repo", str(world), "--rev", rev]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    verdicts: dict[str, str] = {}
    for line in proc.stdout.split("\n"):
        m = RESULT_RE.match(line.strip())
        if m:
            verdicts[m.group(1)] = m.group(2)
    backed = None
    for line in proc.stdout.split("\n"):
        m = re.match(r"^description craft backed (\d+) of (\d+)$", line.strip())
        if m:
            backed = (int(m.group(1)), int(m.group(2)))
    return {"rev": rev, "cmd": cmd, "exit": proc.returncode,
            "stdout": proc.stdout, "stderr": proc.stderr,
            "verdicts": verdicts, "backed": backed}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--work", default=None,
                    help="scratch root (falls back to TMPDIR, then "
                         + str(DEFAULT_WORK) + ")")
    ap.add_argument("--receipt", default=str(DEFAULT_RECEIPT))
    ap.add_argument("--keep", action="store_true",
                    help="keep the scratch worlds for inspection")
    args = ap.parse_args(argv)

    work = args.work or os.environ.get("TMPDIR") or str(DEFAULT_WORK)
    work_path = Path(work).expanduser().resolve()
    if str(work_path) == "/tmp" or str(work_path).startswith("/tmp/"):
        work_path = DEFAULT_WORK
    for sub in ("clone", "counter", "worlds", "selftest"):
        (work_path / sub).mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------- frozen instrument
    lane_bytes = (LANE / COUNTER_REL).read_bytes()
    if sha256(lane_bytes) != COUNTER_SHA:
        raise SystemExit(f"FATAL lane counter is {sha256(lane_bytes)}, not "
                         f"the frozen {COUNTER_SHA}")
    clone = work_path / "clone"
    must(subprocess.run(["git", "clone", "--shared", str(LANE), str(clone)],
                        capture_output=True, text=True),
         "clone the lane")
    top = must(git(clone, "rev-parse", "--show-toplevel"),
               "clone toplevel").stdout.strip()
    if Path(top).resolve() != clone.resolve():
        raise SystemExit(f"FATAL clone toplevel {top!r} != {clone}")
    must(git(clone, "config", "user.name", "scratch-r77"), "clone config name")
    must(git(clone, "config", "user.email", "scratch@example.invalid"),
         "clone config email")
    must(git(clone, "cat-file", "-t", LANE_HEAD), "lane head object")

    counter_copy = work_path / "counter" / "check_desc_craft.py"
    counter_bytes = show(clone, LANE_HEAD, COUNTER_REL)
    if sha256(counter_bytes) != COUNTER_SHA:
        raise SystemExit(f"FATAL committed counter at {LANE_HEAD[:8]} is "
                         f"{sha256(counter_bytes)}, not the frozen "
                         f"{COUNTER_SHA}")
    counter_copy.write_bytes(counter_bytes)
    if sha256(counter_copy.read_bytes()) != COUNTER_SHA:
        raise SystemExit("FATAL counter copy drifted")
    mod = load_counter(counter_copy)
    self_sha = must(subprocess.run([sys.executable, "-B", str(counter_copy),
                                    "--print-self-sha"],
                                   capture_output=True, text=True),
                    "counter --print-self-sha").stdout.strip()

    # ------------------------------------------------ real bytes at the base
    base_skill = show(clone, CLAIM_BASE, SKILLMD).decode()
    base_sources = show(clone, CLAIM_BASE, SOURCES).decode()
    base_snaps = {p: show(clone, CLAIM_BASE, f"{SNAPDIR}/{p}.md") for p in PAGES}
    base_manifest = show(clone, CLAIM_BASE, f"{SNAPDIR}/MANIFEST.sha256")
    base_record = show(clone, CLAIM_BASE, f"{SNAPDIR}/fetch-record.json")
    for page, data in base_snaps.items():
        if sha256(data) != mod.PAGE_SHA[page]:
            raise SystemExit(f"FATAL {page} bytes at {CLAIM_BASE[:8]} are "
                             f"{sha256(data)}, not the pinned {mod.PAGE_SHA[page]}")

    snap_files = {f"{SNAPDIR}/{p}.md": d for p, d in base_snaps.items()}
    snap_files[f"{SNAPDIR}/MANIFEST.sha256"] = base_manifest
    snap_files[f"{SNAPDIR}/fetch-record.json"] = base_record

    # the counter's own snapshot reader, over the world bytes
    probe = make_world(work_path / "worlds", "probe", dict(snap_files))
    snaps = mod.Snapshots(mod.Repo(probe, "HEAD"))
    shutil.rmtree(probe, ignore_errors=True)
    digest = sha256(base_snaps[OD])

    od_rows: list[tuple[str, str, int]] = []
    for i, quote in enumerate(OD_QUOTES, 1):
        n = line_of(snaps, OD, quote)
        if not snaps.after_first_heading(OD, quote):
            raise SystemExit(f"FATAL quote is not after the first heading: "
                             f"{quote!r}")
        if any(snaps.occurs(p, quote) for p in PAGES if p != OD):
            raise SystemExit(f"FATAL quote is not page-unique: {quote!r}")
        if not (mod.MIN_QUOTE_WORDS <= mod.words(quote) <= mod.MAX_QUOTE_WORDS):
            raise SystemExit(f"FATAL quote word count: {quote!r}")
        od_rows.append((quote, f"rule {i}", n))
    bp_rows: list[tuple[str, str, int]] = []
    for i, quote in enumerate(BP_QUOTES, 1):
        n = line_of(snaps, "best-practices", quote)
        if snaps.occurs(OD, quote) or snaps.occurs("evaluating-skills", quote):
            raise SystemExit(f"FATAL best-practices quote also on another "
                             f"page: {quote!r}")
        bp_rows.append((quote, f"rule {i}", n))
    for frag in ("Frame the description as an instruction to the agent",
                 "Err on the side of being pushy"):
        if not snaps.after_first_heading(OD, frag):
            raise SystemExit(f"FATAL act-on fragment is not located: {frag!r}")

    skill_row = skill_with_row(base_skill)
    sources_new = sources_with_used_by(base_sources)
    clip, stripped, first = mod.description_measures(skill_row)
    if mod.description_measures(base_skill) != (clip, stripped, first):
        raise SystemExit("FATAL the Body craft row changed the frontmatter "
                         f"measures ({clip}, {stripped}, {first})")

    honest = {
        SKILLMD: skill_row.encode(),
        SOURCES: sources_new.encode(),
        ENTRY: entry_text(OD_QUOTES[0], od_rows[0][2], od_rows,
                          clip, first).encode(),
        LESSON: lesson_text(digest).encode(),
    }
    honest.update(snap_files)

    specs: list[dict] = []

    def add(name: str, label: str, why: str, files: dict[str, bytes],
            expect_exit: int, expect_backed: int,
            expect_fail: tuple[str, ...]) -> None:
        specs.append(dict(name=name, label=label, why=why, files=files,
                          expect_exit=expect_exit,
                          expect_backed=expect_backed,
                          expect_fail=frozenset(expect_fail)))

    # W0: the attribution arm.  It must reach the target, or the matrix below
    # cannot attribute anything.
    add("W0", "W0 honest baseline (attribution arm)",
        "not a must-fail world: an honest world on the real committed base "
        "bytes must reach 6 of 6 (exit 0); every must-fail world below "
        "differs from it in exactly one dimension",
        honest, 0, 6, ())

    # W1: fabricated -- stub entry, empty snapshot set.
    w1 = {SKILLMD: base_skill.encode(), ENTRY: stub_entry().encode()}
    add("W1", "W1 fabricated (stub entry, empty snapshot set)",
        "fabricated: a stub entry with no snapshot bytes, no lesson, no "
        "registry edit and no audit table; no conjunct can hold",
        w1, 1, 0, CONJUNCTS)

    # W2: real text from the WRONG page.
    w2 = dict(honest)
    w2[ENTRY] = entry_text(OD_QUOTES[0], od_rows[0][2], bp_rows,
                           clip, first, page="best-practices").encode()
    add("W2", "W2 wrong-page real text (best-practices quotes)",
        "the rule rows quote the committed best-practices snapshot verbatim "
        "-- real bytes, wrong page; the page-unique arm of (b) must reject "
        "them, so only (b) fails",
        w2, 1, 5, ("b",))

    # W3: token dump naming all six conjuncts.
    w3 = dict(honest)
    w3[ENTRY] = token_entry().encode()
    add("W3", "W3 token dump (names all six conjuncts)",
        "the entry names (a)-(f) and carries an honest provenance trio, but "
        "no located quotes and no audit table: naming is not content, so (b) "
        "and (d) fail",
        w3, 1, 4, ("b", "d"))

    # W4: cheapest do-nothing -- row + used-by edit, no entry.
    w4 = {SKILLMD: skill_row.encode(), SOURCES: sources_new.encode()}
    add("W4", "W4 cheapest do-nothing (row + used-by, no entry)",
        "only a rewritten SKILL.md row and the S213 used-by edit: no entry, "
        "no lesson, no snapshots -- nothing to back a conjunct",
        w4, 1, 0, CONJUNCTS)

    # W5: the audit numbers reformatted (stripped 1021 instead of clip 1022).
    w5 = dict(honest)
    w5[ENTRY] = entry_text(OD_QUOTES[0], od_rows[0][2], od_rows,
                           stripped, first).encode()
    add("W5", "W5 audit numbers reformatted (1021 stripped, not 1022 clip)",
        "an honest world whose audit table states the stripped render "
        f"{stripped} instead of the clip-preserving {clip}; (d) must fail on "
        "the recomputation from this world's SKILL.md",
        w5, 1, 5, ("d",))

    # ------------------------------------------------------------ run them
    python = shutil.which("python3") or sys.executable
    results: list[dict] = []
    for spec in specs:
        d = make_world(work_path / "worlds", spec["name"], spec["files"])
        got = score(python, counter_copy, d)
        got.update(spec)
        got["files"] = sorted(spec["files"])
        results.append(got)
        if not args.keep:
            shutil.rmtree(d, ignore_errors=True)

    selftest = subprocess.run([python, "-B", str(counter_copy),
                               "--self-test", "--work",
                               str(work_path / "selftest")],
                              capture_output=True, text=True)
    selftest_tail = (selftest.stdout.strip().split("\n") or [""])[-1]

    # ------------------------------------------------------------- verdicts
    defects: list[str] = []
    mismatches: list[str] = []
    for r in results:
        got_backed = None if r["backed"] is None else r["backed"][0]
        if r["expect_exit"] != 0:
            if r["exit"] == 0 or got_backed == TOTAL:
                defects.append(
                    f"COUNTER DEFECT: {r['label']} printed "
                    f"{r['backed']!r} with exit {r['exit']} -- a must-fail "
                    f"world met the target")
        if r["exit"] != r["expect_exit"]:
            mismatches.append(f"{r['name']}: exit {r['exit']} "
                              f"(expected {r['expect_exit']})")
        if got_backed != r["expect_backed"]:
            mismatches.append(f"{r['name']}: backed {got_backed} "
                              f"(expected {r['expect_backed']})")
        failed = {k for k, v in r["verdicts"].items() if v == "fail"}
        if failed != set(r["expect_fail"]):
            mismatches.append(f"{r['name']}: failing conjuncts "
                              f"{sorted(failed)} (expected "
                              f"{sorted(r['expect_fail'])})")
        if len(r["verdicts"]) != TOTAL:
            mismatches.append(f"{r['name']}: {len(r['verdicts'])} conjunct "
                              "verdict lines printed, expected 6")

    pyver = subprocess.run([python, "-V"], capture_output=True,
                           text=True).stdout.strip()
    out: list[str] = []
    out.append("# E01ControlsC1 -- C1 control worlds on the frozen counter blob")
    out.append("# kotoba round 77, wave w1, seat E01ControlsC1")
    out.append(f"generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    out.append(f"counter: {COUNTER_REL}")
    out.append(f"counter-sha256: {COUNTER_SHA}")
    out.append(f"counter-copy-sha256: {sha256(counter_copy.read_bytes())}")
    out.append(f"counter-lane-bytes-sha256: {sha256(lane_bytes)}")
    out.append(f"counter-self-sha (--print-self-sha): {self_sha}")
    out.append(f"counter-source-rev: {LANE_HEAD} (lane HEAD, frozen blob)")
    out.append(f"lane: {LANE}")
    out.append(f"claim-base-rev: {CLAIM_BASE}")
    out.append(f"python: {sys.executable} ({pyver})")
    out.append("cmd-form: python3 -B <counter-copy> --repo <world> --rev <world-head>")
    out.append("# exit codes below are each process's own (subprocess return code);")
    out.append("# no pipeline stands between the counter and the recorded status.")
    out.append(f"scratch: {work_path} ({'kept' if args.keep else 'removed after this receipt'})")
    out.append("")
    if defects:
        for line in defects:
            out.append(line)
        out.append("")
    if mismatches:
        out.append("UNEXPECTED (world-construction or counter-nuance; read the block):")
        for line in mismatches:
            out.append(f"  {line}")
        out.append("")
    out.append(f"honest-world measures: clip {clip} / stripped {stripped} / "
               f"first sentence {first} (SKILL.md at the world tip)")
    out.append("")

    for r in results:
        out.append("=" * 78)
        out.append(f"{r['label']}")
        out.append(f"world-rev: {r['rev']}")
        out.append(f"world-files ({len(r['files'])}): {' '.join(r['files'])}")
        out.append(f"why: {r['why']}")
        out.append(f"expect: backed {r['expect_backed']} of {TOTAL}, exit "
                   f"{r['expect_exit']}, failing conjuncts "
                   f"{sorted(r['expect_fail']) or 'none'}")
        out.append("cmd: " + " ".join(r["cmd"]))
        out.append(f"exit={r['exit']}")
        out.append("stdout:")
        out.append(r["stdout"].rstrip("\n") if r["stdout"] else "(empty)")
        if r["stderr"].strip():
            out.append("stderr:")
            out.append(r["stderr"].rstrip("\n"))
        out.append("")

    out.append("=" * 78)
    out.append("matrix (P = pass, F = fail, as printed by the counter)")
    out.append("world  backed exit  " + " ".join(f"({c})" for c in CONJUNCTS))
    for r in results:
        cells = " ".join({"pass": "P", "fail": "F"}.get(
            r["verdicts"].get(c, ""), "?") for c in CONJUNCTS)
        backed = "n/a" if r["backed"] is None else f"{r['backed'][0]}/{r['backed'][1]}"
        out.append(f"{r['name']:<5} {backed:>6} {r['exit']:>4}  {cells}")
    out.append("")
    out.append(f"cross-check: counter --self-test --work {work_path / 'selftest'} "
               f"-> exit={selftest.returncode}; {selftest_tail}")
    out.append("")
    if defects:
        out.append("VERDICT: COUNTER DEFECT -- a must-fail world met the target; "
                   "stop the round before data.")
    elif mismatches:
        out.append("VERDICT: worlds ran but the matrix is not the expected one; "
                   "read the UNEXPECTED block.")
    else:
        out.append("VERDICT: PASS -- all five must-fail worlds fail, the honest "
                   "baseline reaches 6 of 6, and no must-fail world exits 0.")
    out.append("")

    receipt = Path(args.receipt)
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text("\n".join(out), encoding="utf-8")

    if not args.keep:
        for sub in ("worlds", "clone", "counter", "selftest"):
            shutil.rmtree(work_path / sub, ignore_errors=True)
        try:
            work_path.rmdir()
        except OSError:
            pass

    print("\n".join(out))
    return 1 if (defects or mismatches) else 0


if __name__ == "__main__":
    sys.exit(main())
