#!/usr/bin/env python3
"""c2_controls.py — kotoba round-81 C2 control worlds (seat Kb81E07C2Worlds).

Builds the plan's control worlds (plans/round-81.md § C2: C0-C4) plus two
oracle worlds (H0b, H0) as ISOLATED scratch git repositories at the r81 base
`b284223105f4d106f7e8f56ed4fd296c643cda0e`, runs the round-81 C2 counter
against each measured commit, and compares the observation with a table fixed
BEFORE the first measurement.

Every world is its own repo: `git init` in a fresh temp dir under --work, one
`objects/info/alternates` line to a read-only `git clone --shared` of the lane
at the base, `read-tree <base>`, fixture blobs via `hash-object`/`update-index`,
`write-tree` + `commit-tree -p <base>`, and `rev-parse --show-toplevel` asserted
equal to the world dir.  The lane is read-only throughout.

The counter under test is `.ufo/waves/round-81/build/check_sdk_allowed_tools.py`
when seat Kb81E09C2Counter has published it.  If it is absent, the suite falls
back to `Kb81E07C2Worlds.ref-counter.py` (this seat's PROVISIONAL reference
implementation of the plan's conjuncts (a)-(g)) and every result is marked
PROVISIONAL in the receipt.

Worlds (expected counts fixed before measurement; see PRE-REGISTRATION):

  C0   base copy, no evidence                                 0 of 1, exit 1
  C1   honest + snapshot bytes tampered against the pin       0 of 1, exit 1
  C2   honest + S248 used-by not updated                      0 of 1, exit 1
  C3   honest + snapshot only in the worktree (uncommitted)   0 of 1, exit 1
  C4   prose asserts 1 of 1, no evidence files                0 of 1, exit 1
  H0   oracle: corpus seat's S249/S248 rows VERBATIM          1 of 1, exit 0
  H0n  oracle: same, S249 anchor fetch record normalised      1 of 1, exit 0
  R0   oracle: entry seat's own S249 row (cells §1)           1 of 1, exit 0

H0, H0n and R0 are diagnostics, not controls: a control that is red proves the
counter refuses that shape only if an honest world can be green.  They are
scored and reported exactly like the controls.  No world reaching the target is
narrowed: it is reported as a counter defect (plan § C2).

Exit of THIS suite: 0 all worlds match the pre-registration, 1 any divergence,
2 unmeasurable (counter could not evaluate any world / fixtures invalid).
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
BUILD = LANE / ".ufo/waves/round-81/build"
BASE_REV = "b284223105f4d106f7e8f56ed4fd296c643cda0e"
PUBLISHED_COUNTER = BUILD / "check_sdk_allowed_tools.py"
REF_COUNTER = BUILD / "Kb81E07C2Worlds.ref-counter.py"
S05_MD = BUILD / "Kb81S05SourcesEdits.md"
ENTRY_SRC = BUILD / "allowed-tools-sdk-round81.md"
CELLS_MD = BUILD / "Kb81E08C2Entry.integration-cells.md"
LESSON_SRC = BUILD / "Kb81S01Lesson.md"
SNAP_SRC = LANE / ".ufo/waves/round-81/snapshots/S249.md"
DEFAULT_WORK = Path(os.environ.get(
    "TMPDIR", "/fast/scratch/hyaku/kotoba-r81/Kb81E07C2Worlds/tmp"))

PIN = "ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2"
PIN_BYTES = 28395
ENTRY = "corpus/knowledge/allowed-tools-sdk-round81.md"
SOURCES = "corpus/SOURCES.md"
SNAP_REL = ".ufo/waves/round-81/snapshots/S249.md"
URL = "https://code.claude.com/docs/en/agent-sdk/skills.md"
COUNTER_REL = "verifiers/check_sdk_allowed_tools.py"
CAPTURE = "2026-10-27"
QUOTE = ("the allowedTools option (allowed_tools in Python) in your query "
         "configuration")
LESSON = "corpus/lessons/round-81.md"
ROW = "S249"
PRIOR = "S248"

ROW_LINE_RE = re.compile(r"^ {0,3}\|\s*(S\d{3,})\s*\|")
N_RE = re.compile(r"sdk allowed-tools surface documented (\d+) of (\d+)\s*$")
FETCH_PAREN_RE = re.compile(
    r"fetched (\d{4}-\d\d-\d\d(?:T\d\d:\d\d:\d\dZ)?) \([^)]*\), HTTP 200")

# ------------------------------------------------------------ pre-registration
# Fixed BEFORE the first measurement of this suite and printed by the run.
# `n` is the counter's own headline count; `exit` the counter's own status.
EXPECT = [
    ("C0", 0, 1, "base copy, no evidence"),
    ("C1", 0, 1, "honest world, snapshot bytes tampered against the pin"),
    ("C2", 0, 1, "honest world, S248 used-by not updated"),
    ("C3", 0, 1, "honest world, snapshot only in the worktree (uncommitted)"),
    ("C4", 0, 1, "prose asserts 1 of 1, no evidence files"),
    ("N1", 0, 1, "diagnostic: honest shape minus the lesson (arm is load-bearing)"),
    ("H1", 1, 0, "oracle: full honest shape, corpus seat's S249/S248 rows"),
    ("R1", 1, 0, "oracle: full honest shape, entry seat's own S249 row (cells §1)"),
]
WORLD_ORDER = [w for w, _n, _e, _why in EXPECT]
EXPECT_BY = {w: (n, e, why) for w, n, e, why in EXPECT}
ORACLES = {w for w, _n, e, _why in EXPECT if e == 0}


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def git(repo, args, stdin=None, check=True):
    proc = subprocess.run(["git", "-C", str(repo), *args], input=stdin,
                          capture_output=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"git -C {repo} {' '.join(args)}: "
                           f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc


def split_cells(line):
    """Escape-aware markdown cell split; a ``\\|`` is cell content."""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    out, cur, i = [], "", 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "\\|"
            i += 2
            continue
        if c == "|":
            out.append(cur.strip())
            cur = ""
            i += 1
            continue
        cur += c
        i += 1
    out.append(cur.strip())
    return out


def join_cells(cells):
    return "| " + " | ".join(cells) + " |"


def set_used_by(row, value):
    cells = split_cells(row)
    cells[-1] = value
    return join_cells(cells)


# ------------------------------------------------------------------ fixtures
def fenced_after(text, prefix):
    """The first fenced block after a heading that starts with ``prefix``."""
    started = inside = False
    out = []
    for ln in text.splitlines():
        if not started:
            if ln.startswith(prefix):
                started = True
            continue
        if ln.strip() == "```":
            if inside:
                break
            inside = True
            continue
        if inside:
            out.append(ln)
    return "\n".join(out) if out else None


def integration_cells():
    """The entry seat's own cell texts (build/Kb81E08C2Entry.integration-cells.md)."""
    if not CELLS_MD.exists():
        return None
    text = CELLS_MD.read_text(encoding="utf-8")
    cells = {
        "s249_row": fenced_after(text, "## 1. `corpus/SOURCES.md`"),
        "skill_sentence": fenced_after(text, "## 3. `SKILL.md`"),
        "skill_row": fenced_after(text, "## 4. `SKILL.md`"),
        "readme_row": fenced_after(text, "## 5. `corpus/README.md`"),
        "province_bullet": fenced_after(text, "## 6. `PROVINCE.md`"),
    }
    if len(split_cells(cells["s249_row"] or "")) != 11:
        return None
    if not (cells["skill_row"] or "").startswith("| `" + COUNTER_REL):
        return None
    if not (cells["readme_row"] or "").startswith("| Agent SDK"):
        return None
    if not (cells["province_bullet"] or "").startswith("- "):
        return None
    if not (cells["skill_sentence"] or "").strip():
        return None
    return cells


def entry_payload():
    """The entry seat's published entry verbatim, else this seat's fallback."""
    if ENTRY_SRC.exists():
        data = ENTRY_SRC.read_bytes()
        text = data.decode("utf-8", "replace")
        if (f"verified-at: {CAPTURE}" in text and "recheck:" in text
                and "source: S249" in text and "S249.md" in text):
            return data, f"entry seat's file verbatim ({ENTRY_SRC.name})"
    return entry_text(), "derived by this seat (entry seat's file absent)"


def lesson_payload():
    """The lesson seat's published draft verbatim, else a minimal fallback."""
    if LESSON_SRC.exists():
        data = LESSON_SRC.read_bytes()
        text = data.decode("utf-8", "replace")
        if any(PRIOR in ln and ENTRY in ln and ("\u2192" in ln or "->" in ln)
               for ln in text.splitlines()):
            return data, f"lesson seat's file verbatim ({LESSON_SRC.name})"
    line = (f"- {PRIOR} used-by — → {ENTRY} (round-81 C2; old cell "
            f"`—`, new cell the entry name).")
    return ("# Round 81 — kotoba (attempt 1)\n\n## Sources & frontier\n\n"
            + line + "\n"), "derived by this seat (lesson seat's file absent)"


def entry_text():
    return f"""source: S249 — Claude Code Agent SDK — Skills — {URL} — \
§ Pre-approve tools for skills — located quote "{QUOTE}" (snapshot `{SNAP_REL}`)
verified-at: {CAPTURE}
recheck: 30d — re-fetch the page and confirm the located quote still occurs \
after the first heading; the pin is sha256 {PIN}

ground: at base `{BASE_REV}` no entry states the Agent SDK's grant channel and \
row S248 is `queued` with `used-by` `—`.

# The Agent SDK `allowedTools` channel beside the frontmatter field

The SDK page documents a second grant channel for skill tools: query-config \
`allowedTools` (`allowed_tools` in Python) beside the SKILL.md `allowed-tools` \
frontmatter field, and managed settings can ignore both.

Located quote: "{QUOTE}"

Everything below is documentary: the page was fetched twice on {CAPTURE} \
({PIN_BYTES} B, sha256 `{PIN}`, byte-identical); no SDK was installed or run.
"""


def fallback_s249_row():
    cells = [
        ROW,
        f"Claude Code Agent SDK — Skills — {URL}",
        "docs",
        "A",
        ("The Agent SDK's allowedTools/allowed_tools query-configuration grant "
         "channel and the managed-settings override that disables it, as the "
         "SDK vendor's own statement of that option"),
        (f"§ Pre-approve tools for skills, blockquote at line 348 (grant note "
         f"line 389); snapshot `{SNAP_REL}` sha256 `ac62c2df…`; fetched "
         f"2026-10-28T02:27:26Z, HTTP 200, {PIN_BYTES} B, sha256 `{PIN}`; "
         f"located quote \"{QUOTE}\""),
        ("The page states that in SDK sessions the frontmatter field and the "
         "allowedTools query option both pre-approve the listed tools, that "
         "managed settings can override both, and that the list pre-approves "
         "rather than restricts"),
        "mined",
        CAPTURE,
        "90d",
        ENTRY,
    ]
    return join_cells(cells)


def s05_rows():
    """The corpus seat's published S249 and updated S248 rows, verbatim."""
    if not S05_MD.exists():
        return None
    text = S05_MD.read_text(encoding="utf-8")
    s249 = s248 = None
    for ln in text.splitlines():
        if s249 is None and ln.startswith("| S249 |"):
            s249 = ln
        if s248 is None and ln.startswith("| S248 |") and ENTRY in ln:
            s248 = ln
    if s249 is None or s248 is None:
        return None
    return {"S249": s249, "S248": s248, "verbatim": True}


def normalise_fetch_record(row):
    """Drop a parenthetical between the fetch instant and `, HTTP 200`."""
    return FETCH_PAREN_RE.sub(r"fetched \1, HTTP 200", row)


def rows_for_controls(base_sources):
    """S249 (+ normalised anchor) and the S248 row with used-by updated."""
    published = s05_rows()
    if published is not None:
        s249 = normalise_fetch_record(published["S249"])
        s248 = published["S248"]
        provenance = ("corpus seat's rows verbatim (the anchor normaliser "
                      "matched nothing)" if s249 == published["S249"] else
                      "corpus seat's rows, S249 anchor fetch record normalised")
    else:
        s249 = fallback_s249_row()
        base_s248 = next((ln for ln in base_sources.splitlines()
                          if ROW_LINE_RE.match(ln)
                          and ROW_LINE_RE.match(ln).group(1) == PRIOR), None)
        if base_s248 is None:
            raise RuntimeError("base tree has no S248 row")
        s248 = set_used_by(base_s248, ENTRY)
        provenance = "derived by this seat (corpus seat's row file absent)"
    if len(split_cells(s249)) != 11 or len(split_cells(s248)) != 11:
        raise RuntimeError("fixture row does not carry 11 cells")
    return s249, s248, provenance


def sources_document(base_text, s249_row, s248_row=None):
    lines = base_text.splitlines()
    idx = next((i for i, ln in enumerate(lines)
                if ROW_LINE_RE.match(ln)
                and ROW_LINE_RE.match(ln).group(1) == PRIOR), None)
    if idx is None:
        raise RuntimeError("base SOURCES.md has no S248 row to anchor the edit")
    out = list(lines)
    if s248_row is not None:
        out[idx] = s248_row
    out.insert(idx + 1, s249_row)
    return "\n".join(out) + ("\n" if base_text.endswith("\n") else "")


def fallback_skill_sentence():
    return (" Round 81: the Claude Agent SDK documents a query-config "
            "`allowedTools` block (`allowed_tools` in Python) that "
            "pre-approves the same skill tools, and managed settings can "
            f"ignore both (S248/S249; entry `{ENTRY}`).")


def fallback_skill_row():
    return (f"| `{COUNTER_REL}` | gate | `python3 -B {COUNTER_REL} "
            f"--rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — "
            f"round-81 C2 counter (depth): the Agent SDK `allowedTools` "
            f"grant channel documented over committed bytes (S249 row, "
            f"pinned snapshot, located quote) plus the entry, SKILL.md, "
            f"README and PROVINCE conjuncts; prints `sdk allowed-tools "
            f"surface documented N of 1` | `--self-test` | in-file | temp "
            f"git fixture trees under `$TMPDIR` (removed); the measured "
            f"tree is read-only | kotoba |")


def skill_document(base_text, sentence=None, row=None):
    lines = base_text.splitlines()
    idx = next((i for i, ln in enumerate(lines)
                if ln.startswith("Treat `allowed-tools` as pre-approval")), None)
    if idx is None:
        raise RuntimeError("base SKILL.md has no allowed-tools rule line")
    lines[idx] = lines[idx].rstrip() + (sentence or fallback_skill_sentence())
    anchor = next((i for i, ln in enumerate(lines)
                   if "| `verifiers/check_allowed_tools.py` | gate |" in ln), None)
    if anchor is None:
        raise RuntimeError("base SKILL.md has no allowed-tools counter row")
    lines.insert(anchor + 1, row or fallback_skill_row())
    return "\n".join(lines) + ("\n" if base_text.endswith("\n") else "")


def fallback_readme_row():
    return (f"| SDK allowed-tools channel (round 81) | "
            f"`knowledge/allowed-tools-sdk-round81.md` | the Claude Agent "
            f"SDK's query-config `allowedTools`/`allowed_tools` grant "
            f"channel beside the SKILL.md frontmatter field, with the "
            f"managed-settings override (S249, snapshot-pinned "
            f"{CAPTURE}); documentary only |")


def readme_document(base_text, row=None):
    lines = base_text.splitlines()
    idx = next((i for i, ln in enumerate(lines)
                if ln.startswith("| Allowed-tools surfaces (round 80)")), None)
    if idx is None:
        raise RuntimeError("base README.md has no round-80 allowed-tools row")
    lines.insert(idx + 1, row or fallback_readme_row())
    return "\n".join(lines) + ("\n" if base_text.endswith("\n") else "")


def fallback_province_bullet():
    return (f"- Claude Agent SDK `allowedTools` grant channel (round 81): "
            f"the SDK's query-config `allowedTools` (`allowed_tools` in "
            f"Python) pre-approves the same skill tools as the SKILL.md "
            f"frontmatter field and managed settings can ignore both "
            f"(S249) — `{ENTRY}`, counted by `{COUNTER_REL} --rev <rev>`.")


def province_document(base_text, bullet=None):
    lines = base_text.splitlines()
    idx = next((i for i, ln in enumerate(lines)
                if ln.startswith("Appended round 46")), None)
    if idx is None:
        raise RuntimeError("base PROVINCE.md has no Core introduction line")
    lines.insert(idx + 1, bullet or fallback_province_bullet())
    return "\n".join(lines) + ("\n" if base_text.endswith("\n") else "")


# ------------------------------------------------------------------- the base
def ensure_base_clone(work):
    clone = work / "base-clone"
    if (clone / ".git").exists():
        return clone
    proc = subprocess.run(["git", "clone", "-q", "--shared", str(LANE),
                           str(clone)], capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError("base clone failed: "
                           + proc.stderr.decode("utf-8", "replace").strip())
    git(clone, ["checkout", "-q", BASE_REV])
    top = git(clone, ["rev-parse", "--show-toplevel"]).stdout.decode().strip()
    if Path(top).resolve() != clone.resolve():
        raise RuntimeError(f"base clone toplevel {top!r} is not {clone}")
    return clone


def base_text(clone, path):
    proc = git(clone, ["show", f"{BASE_REV}:{path}"], check=False)
    if proc.returncode != 0:
        raise RuntimeError(f"base tree has no {path}")
    return proc.stdout.decode("utf-8", "replace")


def base_absent(clone, path):
    return git(clone, ["cat-file", "-e", f"{BASE_REV}:{path}"],
               check=False).returncode != 0


# ---------------------------------------------------------------- build worlds
def build_world(work, clone, files, tag):
    d = Path(tempfile.mkdtemp(prefix=f"{tag}-", dir=str(work)))
    try:
        git(d, ["init", "-q"])
        git(d, ["config", "user.name", "scratch-r81"])
        git(d, ["config", "user.email", "scratch@example.invalid"])
        top = git(d, ["rev-parse", "--show-toplevel"]).stdout.decode().strip()
        if Path(top).resolve() != d.resolve():
            raise RuntimeError(f"fixture toplevel {top!r} is not {d}")
        obj = git(clone, ["rev-parse", "--git-path",
                          "objects"]).stdout.decode().strip()
        obj_path = Path(obj)
        if not obj_path.is_absolute():
            obj_path = (clone / obj_path).resolve()
        info = d / ".git" / "objects" / "info"
        info.mkdir(parents=True, exist_ok=True)
        (info / "alternates").write_text(str(obj_path) + "\n")
        if git(d, ["cat-file", "-t", f"{BASE_REV}^{{commit}}"],
               check=False).returncode != 0:
            raise RuntimeError(f"base revision not readable through {obj_path}")
        git(d, ["read-tree", BASE_REV])
        for rel, payload in files.items():
            if payload is None:
                git(d, ["update-index", "--force-remove", rel], check=False)
                continue
            blob = git(d, ["hash-object", "-w", "--stdin"],
                       stdin=payload if isinstance(payload, bytes)
                       else payload.encode()).stdout.decode().strip()
            git(d, ["update-index", "--add", "--cacheinfo",
                    f"100644,{blob},{rel}"])
        tree = git(d, ["write-tree"]).stdout.decode().strip()
        env = dict(os.environ,
                   GIT_AUTHOR_DATE="2026-10-27T00:00:00Z",
                   GIT_COMMITTER_DATE="2026-10-27T00:00:00Z")
        commit = subprocess.run(
            ["git", "-C", str(d), "commit-tree", tree, "-p", BASE_REV],
            input=f"c2r81 control world {tag}\n".encode(),
            capture_output=True, env=env)
        if commit.returncode != 0:
            raise RuntimeError("commit-tree failed: "
                               + commit.stderr.decode("utf-8", "replace"))
        sha = commit.stdout.decode().strip()
        git(d, ["update-ref", f"refs/heads/{tag}", sha])
        return d, sha, tree
    except Exception:
        shutil.rmtree(d, ignore_errors=True)
        raise


def run_counter(counter, world, rev, timeout=180):
    proc = subprocess.run(
        [sys.executable, "-B", str(counter), "--repo", str(world),
         "--rev", rev],
        capture_output=True, text=True, cwd=str(world), timeout=timeout)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def parse_output(out):
    res = {"n": None, "of": None, "headline": None, "findings": [],
           "other": [], "error": None}
    for line in out.splitlines():
        bare = line.rstrip()
        if bare != bare.lstrip():
            stripped = bare.strip()
            if stripped:
                res["findings"].append(stripped)
            continue
        if not bare:
            continue
        m = N_RE.match(bare)
        if m and res["n"] is None:
            res["n"], res["of"] = int(m.group(1)), int(m.group(2))
            res["headline"] = bare
            continue
        if bare.startswith("environment error"):
            res["error"] = bare
            continue
        res["other"].append(bare)
    return res


# ------------------------------------------------------------------ fixtures
def fixture_snapshot():
    if not SNAP_SRC.exists():
        raise RuntimeError(f"snapshot fixture missing: {SNAP_SRC}")
    data = SNAP_SRC.read_bytes()
    digest = sha256_bytes(data)
    if digest != PIN or len(data) != PIN_BYTES:
        raise RuntimeError(f"snapshot fixture is not the pin: {digest} "
                           f"{len(data)} B")
    return data


def preflight(clone, snap):
    """Fixture invariants, checked before any world is built."""
    errs = []
    if not base_absent(clone, ENTRY):
        errs.append(f"base tree already carries {ENTRY}")
    if not base_absent(clone, SNAP_REL):
        errs.append(f"base tree already carries {SNAP_REL}")
    sources = base_text(clone, SOURCES)
    prior = [ln for ln in sources.splitlines()
             if ROW_LINE_RE.match(ln) and ROW_LINE_RE.match(ln).group(1) == PRIOR]
    if len(prior) != 1:
        errs.append(f"base S248 row count {len(prior)}")
    elif split_cells(prior[0])[-1] != "\u2014":
        errs.append("base S248 used-by is not the empty marker")
    if any(ROW_LINE_RE.match(ln) and ROW_LINE_RE.match(ln).group(1) == ROW
           for ln in sources.splitlines()):
        errs.append("base tree already carries an S249 row")
    if not base_absent(clone, COUNTER_REL):
        errs.append(f"base tree already carries {COUNTER_REL}")
    skill = base_text(clone, "SKILL.md")
    if ENTRY in skill or COUNTER_REL in skill:
        errs.append("base SKILL.md already names the entry or the counter")
    for path in ("corpus/README.md", "PROVINCE.md"):
        if ENTRY in base_text(clone, path):
            errs.append(f"base {path} already names the entry")
    view = [re.sub(r"\s+", " ", ln.replace("`", "")).strip()
            for ln in snap.decode("utf-8", "replace").splitlines()]
    view = [ln for ln in view if ln]
    head = next((i for i, ln in enumerate(view) if ln.startswith("#")), None)
    if head is None:
        errs.append("snapshot text view has no heading")
    elif QUOTE not in " ".join(view[head + 1:]):
        errs.append("fixture quote does not occur in the snapshot view")
    if not 3 <= len(QUOTE.split()) <= 25:
        errs.append("fixture quote word count out of bounds")
    return errs


# --------------------------------------------------------------------- driver
def make_world_files(name, clone, snap, materials):
    """(files, untracked) for one world; fixture bytes only."""
    base_sources = base_text(clone, SOURCES)
    honest = {
        ENTRY: materials["entry"],
        SOURCES: sources_document(base_sources, materials["s249_row"],
                                  materials["s248_row"]),
        SNAP_REL: snap,
        "SKILL.md": skill_document(base_text(clone, "SKILL.md"),
                                   materials["skill_sentence"],
                                   materials["skill_row"]),
        "corpus/README.md": readme_document(base_text(clone, "corpus/README.md"),
                                            materials["readme_row"]),
        "PROVINCE.md": province_document(base_text(clone, "PROVINCE.md"),
                                         materials["province_bullet"]),
        LESSON: materials["lesson"],
    }
    if name == "C0":
        return {}, {}
    if name == "C4":
        return {"corpus/lessons/round-81-controls.md":
                ("sdk allowed-tools surface documented 1 of 1\n\n"
                 "This paragraph asserts the round-81 C2 headline. No entry, "
                 "registry row, snapshot or counter evidence is committed in "
                 "this world; prose must earn nothing.\n")}, {}
    if name in ("H1", "R1"):
        return dict(honest), {}
    if name == "N1":
        files = dict(honest)
        files.pop(LESSON)
        return files, {}
    if name == "C1":
        files = dict(honest)
        files[SNAP_REL] = snap + b"\n"          # pin mismatch, quote intact
        return files, {}
    if name == "C2":
        files = dict(honest)
        files[SOURCES] = sources_document(base_sources, materials["s249_row"],
                                          None)
        return files, {}
    if name == "C3":
        files = dict(honest)
        files.pop(SNAP_REL)
        return files, {SNAP_REL: snap}          # present, never committed
    raise KeyError(name)


def compare(name, code, parsed):
    """(ok, why, credited, class_note).

    A CONTROL world passes when the counter does not credit it: no headline
    count of 1 and no exit 0.  Exit 1 (a failed conjunct) and exit 2
    (could-not-evaluate) are both refusals, and the class is reported beside
    the pre-registered exit rather than hidden.  An ORACLE world passes only
    on the exact pre-registered count and exit: an honest shape must be
    certifiable, or no control's refusal is attributable.
    """
    want_n, want_exit, why = EXPECT_BY[name]
    n = parsed["n"]
    credited = (n == 1) or (code == 0)
    if name in ORACLES:
        ok = (n == want_n and code == want_exit)
    else:
        ok = not credited
    cls = {0: "exit 0 (credited)", 1: "exit 1 (failed conjunct)",
           2: "exit 2 (could-not-evaluate)"}.get(code, f"exit {code}")
    note = "" if code == want_exit else (
        f"CLASS: pre-registered exit {want_exit}, observed {cls}")
    return ok, why, credited, note


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="round-81 C2 control worlds (seat Kb81E07C2Worlds)")
    ap.add_argument("--work", default=str(DEFAULT_WORK),
                    help="parent directory for the base clone and every world")
    ap.add_argument("--counter", default=None,
                    help="counter file under test (default: the published "
                         "build/check_sdk_allowed_tools.py, else this seat's "
                         "PROVISIONAL reference)")
    ap.add_argument("--list", action="store_true",
                    help="print the pre-registration and exit")
    ap.add_argument("--keep", action="store_true",
                    help="keep the world directories after the run")
    args = ap.parse_args(argv)

    print("c2_controls.py — kotoba round 81 C2 control worlds "
          "(seat Kb81E07C2Worlds)")
    print(f"run: {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
    print(f"lane: {LANE}")
    print(f"base rev: {BASE_REV}")
    print("pre-registration (fixed before measurement):")
    print("  world  expected        conjunct broken / role")
    for name, n, code, why in EXPECT:
        print(f"  {name:<5}  {n} of 1 exit {code}  {why}")
    if args.list:
        return 0

    work = Path(args.work)
    work.mkdir(parents=True, exist_ok=True)

    if args.counter:
        counter = Path(args.counter)
        provisional = "PROVISIONAL reference" in counter.read_text(
            encoding="utf-8", errors="replace")
    elif PUBLISHED_COUNTER.exists():
        counter = PUBLISHED_COUNTER
        provisional = False
    else:
        counter = REF_COUNTER
        provisional = True
    if not counter.exists():
        print(f"environment error: no counter at {counter}")
        return 2
    counter_bytes = counter.read_bytes()
    print(f"counter: {counter}")
    print(f"counter sha256: {sha256_bytes(counter_bytes)}")
    status = ("PROVISIONAL (inline reference — the published E09 counter is "
              "absent)" if provisional else "PUBLISHED")
    print(f"counter status: {status}")

    try:
        snap = fixture_snapshot()
        print(f"snapshot fixture: {SNAP_SRC} sha256 {sha256_bytes(snap)} "
              f"{len(snap)} B")
        clone = ensure_base_clone(work)
        print(f"base clone: {clone}")
        errs = preflight(clone, snap)
    except Exception as exc:                      # noqa: BLE001 - fail closed
        print(f"environment error: {exc}")
        return 2
    if errs:
        print("preflight FAILED — fixtures invalid, no world measured:")
        for e in errs:
            print(f"  {e}")
        return 2
    print("preflight: OK (base tree lacks every claim path; fixture quote "
          "locates in the snapshot view)")

    base_sources = base_text(clone, SOURCES)
    base_tree = git(clone, ["rev-parse", f"{BASE_REV}^{{tree}}"]
                    ).stdout.decode().strip()
    s249, s248, provenance = rows_for_controls(base_sources)
    published = s05_rows()
    cells = integration_cells()
    entry_bytes, entry_provenance = entry_payload()
    lesson_bytes, lesson_provenance = lesson_payload()
    print(f"fixture entry: {entry_provenance}, {len(entry_bytes)} B")
    print(f"fixture lesson: {lesson_provenance}, {len(lesson_bytes)} B")
    print(f"fixture cells: "
          f"{'entry seat\'s integration-cells verbatim' if cells else 'derived by this seat'}")
    print(f"fixture rows: {provenance}")

    def materials(row_s249, row_s248):
        return {
            "entry": entry_bytes,
            "s249_row": row_s249,
            "s248_row": row_s248,
            "skill_sentence": cells["skill_sentence"] if cells else None,
            "skill_row": cells["skill_row"] if cells else None,
            "readme_row": cells["readme_row"] if cells else None,
            "province_bullet": cells["province_bullet"] if cells else None,
            "lesson": lesson_bytes,
        }

    rows = []
    for name in WORLD_ORDER:
        if published is not None and name != "R1":
            row_s249, row_s248 = published["S249"], published["S248"]
        elif name == "R1" and cells is not None:
            row_s249, row_s248 = cells["s249_row"], s248
        else:
            row_s249, row_s248 = s249, s248
        files, untracked = make_world_files(
            name, clone, snap, materials(row_s249, row_s248))
        try:
            world, commit, tree = build_world(work, clone, files, name)
        except Exception as exc:                  # noqa: BLE001
            print(f"\n### {name}: environment error building the world: {exc}")
            rows.append((name, None, None, {}, "BUILD-ERROR"))
            continue
        for rel, payload in untracked.items():
            target = world / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
        code, out = run_counter(counter, world, commit)
        parsed = parse_output(out)
        ok, why, credited, note = compare(name, code, parsed)
        verdict = "PASS" if ok else ("CREDITED" if credited else "DIVERGES")
        rows.append((name, code, parsed, {"commit": commit, "why": why,
                                          "note": note, "credited": credited},
                     verdict))
        print(f"\n### {name} — {why}")
        print(f"world: {world}")
        print(f"commit: {commit} (parent {BASE_REV})")
        print(f"tree: {tree}")
        if name == "C0":
            print("tree identity: " + ("equal to the base tree (a base copy)"
                  if tree == base_tree else "DIFFERS from the base tree"))
        print(f"command: python3 -B {counter} --repo {world} --rev {commit}")
        print(f"exit: {code}")
        print("stdout:")
        body = out.rstrip("\n").splitlines()
        if not body:
            print("  (no output)")
        for line in body:
            print(f"  {line.rstrip()}")
        observed_n = ("none" if parsed["n"] is None
                      else f"{parsed['n']} of {parsed['of']}")
        print(f"expected: {EXPECT_BY[name][0]} of 1, exit {EXPECT_BY[name][1]}")
        print(f"observed: {observed_n}, exit {code}"
              f" ({'credited' if credited else 'refused'})")
        if note:
            print(note)
        print(f"verdict: {verdict}")
        if not args.keep:
            shutil.rmtree(world, ignore_errors=True)

    print("\nSUMMARY")
    print("world  role     expected        observed        exit  class"
          "                  verdict")
    passes = diverges = errors = 0
    exit2 = 0
    for name, code, parsed, meta, verdict in rows:
        want_n, want_exit, _why = EXPECT_BY[name]
        role = "oracle" if name in ORACLES else "control"
        observed = ("build-error" if code is None
                    else "no count" if parsed.get("n") is None
                    else f"{parsed['n']} of {parsed['of']}")
        exit_s = "-" if code is None else str(code)
        cls = ("-" if code is None else
               "credited" if meta.get("credited") else
               "refused/finding" if code == 1 else "refused/cannot-eval")
        print(f"{name:<6} {role:<8} {want_n} of 1 exit {want_exit}   "
              f"{observed:<14}  {exit_s:<4}  {cls:<20} {verdict}")
        if verdict == "PASS":
            passes += 1
        elif verdict in ("DIVERGES", "CREDITED"):
            diverges += 1
        else:
            errors += 1
        if code == 2:
            exit2 += 1
    total = len(rows)
    print(f"suite: {total} worlds, {passes} PASS, {diverges} DIVERGE, "
          f"{errors} BUILD-ERROR")
    if exit2 == total:
        print("verdict: UNMEASURABLE — the counter could not evaluate any "
              "world (exit 2 everywhere)")
        return 2
    if errors or diverges:
        print("verdict: DIVERGENCES — see the per-world blocks above")
        return 1
    print("verdict: CONTROLS-HOLD — every control refused, every oracle "
          "certified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
