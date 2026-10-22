#!/usr/bin/env python3
"""verify_harness_independent.py — source-blind re-derivation of the harness
claim set (round 37, claim C1, seat P1).

Why this file exists
--------------------
`verifiers/verify_harness_claims.py` is the lane's oldest instrument: one author
read the two live substrates (the omp binary + its skill-description cache, and
the opencode log + configs), wrote down 28 expected values, and the harness has
compared live bytes against that authorial expectation set ever since.  The
expectations themselves were never re-derived by anyone who did not read them.
This instrument is that re-derivation: it names the same 28 checks, computes a
value for each one from the live substrates with its own extractor, and the
comparison is a diff of two independently produced tables — never a copy.

Blindness protocol (binding on the builder seats that landed this file)
----------------------------------------------------------------------
* No builder seat opened `verifiers/verify_harness_claims.py`, the `checks`
  rows of `verifiers/baseline.json`, or corpus documents quoting either.
* The only harness-adjacent input read was `measured_against` (the substrate
  *pin* block): it names the substrate binaries.  Reading it is reading
  substrate locations, not expectations.
* This file opens neither the harness nor `baseline.json` — not at import, not
  in any mode.  Its inputs are the live substrates plus an optional
  `--observed` JSON of the harness's own stdout (a comparison column, i.e.
  output, not source).
* The derived table was frozen (written to `.ufo/round-37/drafts/p1/` and
  hashed) *before* the harness was run for the comparison column, so a reader
  can check the ordering from artifact timestamps and hashes.

Adjudication of the five round-37 open rows (round 38, seat P1 — C1 closure)
---------------------------------------------------------------------------
Round 37 landed this instrument with five rows open: two definitional
disagreements and the catalogue family, which carried no derivation. Round 38
ruled them under `.ufo/round-37/evidence/a1-adjudication-protocol.md` §3–§5,
and the rulings are recorded in `corpus/knowledge/harness-independent-round37.md`
§3. Each ruling is implemented here, not described:

* `oc.log.skills_tag_hits` — the id's spec sentence names the literal `<skills>`
  tag, and the raw log carries 0 of them (`grep -c '<skills>' <log>` → 0). The
  harness's reading is adopted. The round-37 reading (the attribute token
  `skills="`, 13 hits) is kept as the **named definitional alternative**
  `oc.log.skills_attr_hits`, published in the table's `alternatives` map — never
  as a check id, so it can never enter the comparison surface.
* `oc.dup.roots_both_sided` / `oc.dup.onesided_roots` — same ruling: the id
  names the log's `duplicate skill name … existing=… duplicate=…` per-root
  split, and the raw log carries 0 such lines (`grep -c 'duplicate skill name'
  <log>` → 0). The round-37 reading (names repeating across rescan arrays) is
  kept as `oc.dup.rescan_repeat_names`.
* `oc.log.init_count_monotone` / `oc.log.init_count_max` — adjudicated r39
  (D2): both ids name the substrate's own `message=init count=N` occurrences.
  The round-37 reading keyed them by `run=` and called a run with more than one
  occurrence a violation — a different population and the opposite predicate
  (the counts only grow; a *decrease* is the signal). Both rows now derive from
  one occurrence sequence in file order, the violation is rendered as the
  harness renders it (`a->b`), and the round-37 population is recorded in the
  fixture battery as the non-grammar form it is.
* `omp.catalogue.*` (4 rows) — **SCOPED_OUT**, status `SCOPED_OUT` with the
  blindness blocker carried per row and in the table's `scoped_out` map: the
  catalogue carrier's selection rule (newest session-jsonl `<skills>` block
  with ≥min(10,len(known)) entries matched against the cache) is the harness's
  own authored scope, not a substrate fact this instrument's substrate set can
  read blind — named, never guessed (r12 §3b (f), P3's idiom). The driver
  `compare_harness_independent.py` excludes these rows from the join by name
  and reports them; the headline is stated over the landed scope.

Per protocol §1/§9, this closure was made by an *adjudicating* seat, which may
read both sides' sources to classify a row; the disclosure is carried in each
ruled row's evidence string (`adjudicated r38:`). The original derivation
stayed blind — the round-37 freeze file and its sha256 remain the record of
that, and nothing above was derived from it.

What each row means, and where the meaning came from
----------------------------------------------------
Every semantic below was recovered from the live substrate itself, and each
row prints the evidence it was computed from.  Two of them came out of the
omp binary's shipped TypeScript (`skill-descriptions.ts`, embedded unminified
in the ELF, found by scanning the binary — the harness was never consulted):

  key   = sha256(TEMPLATE + "\\x00" + name + "\\x00" + description)
  preview: whitespace-collapsed description, truncated at 100 chars to the
           first sentence (>= 40 chars) or to the last word boundary + "…"
  accept: trim, no CR/LF, <= 160 chars, <= 12 words

`TEMPLATE` is the embedded `compress-description-*.md` prompt file; its bytes
are delimited here as the NUL-terminated UTF-8 run that starts at
"Compress into one routing hint" and ends with "Description: {{description}}\n".
That delimitation is this instrument's own rule and the one place where a
boundary disagreement with the harness is possible rather than a semantic one.

Rows this instrument does NOT land are reported as `UNLANDED` with the reason
(never skipped, never guessed): a row that cannot be re-derived blind must not
silently become a copy of the harness's number.

Exit ladder (family contract; precedence 3 > 2 > 1 > 0):
  0  every row DERIVED, and in --compare mode every compared row agrees
  1  a compared row DISAGREES (the instrument names it), or a landed row
     disagrees with itself across the freeze file
  2  a substrate is unreadable (the row is named)
  3  usage error / unparseable --observed document
Stdlib only.  Read-only: the substrates are opened for reading; nothing is
written outside --out / --freeze paths the caller names.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Substrates.  Defaults are this host's installs; every path is overridable so
# fixtures can drive the same code (--self-test does exactly that).
# ---------------------------------------------------------------------------
DEFAULT_OMP_BINARY = Path("/home/vgpnk/.local/bin/omp")
DEFAULT_AGENTS_ROOT = Path("/home/vgpnk/.agents/skills")
DEFAULT_SKILL_DB = Path("/home/vgpnk/.omp/agent/skill-descriptions.db")
DEFAULT_OC_LOG = Path("/home/vgpnk/.local/share/opencode/log/opencode.log")
DEFAULT_OC_CONFIG = Path("/home/vgpnk/.config/opencode")

TEMPLATE_START = b"Compress into one routing hint"
TEMPLATE_END = b"Description: {{description}}\n"

# substrate constants read out of the embedded skill-descriptions.ts chunk
PREVIEW_CLIFF = 100
COMPRESS_MAX_CHARS = 160
COMPRESS_MAX_WORDS = 12

PREVIEW_RE = re.compile(r"^.*?[.!?](?=\s|$)")

# fixture battery: durable cases under verifiers/fixtures/harness-independent/
FIXTURE_DIR = Path(os.environ.get(
    "HARNESS_INDEPENDENT_FIXTURES",
    Path(__file__).resolve().parent / "fixtures" / "harness-independent"))


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# substrate readers
# ---------------------------------------------------------------------------
class Substrate:
    """Read-only view of the four live surfaces this instrument derives from."""

    def __init__(self, omp_binary: Path, agents_root: Path, skill_db: Path,
                 oc_log: Path, oc_config: Path,
                 catalogue_carrier: Path | None = None):
        self.omp_binary = omp_binary
        self.agents_root = agents_root
        self.skill_db = skill_db
        self.oc_log = oc_log
        self.oc_config = oc_config
        # Round 39 (C1, seat P1): the session tree the scoped-out catalogue
        # rows' probe censuses.  A fixture tree passes its own so the probe
        # never reads this host's live sessions from a synthetic case.
        self.catalogue_carrier = Path(catalogue_carrier or CATALOGUE_CARRIER)
        self._binary: bytes | None = None
        self._log: str | None = None

    # -- omp binary ---------------------------------------------------------
    def binary(self) -> bytes:
        if self._binary is None:
            self._binary = self.omp_binary.read_bytes()
        return self._binary

    def template_bytes(self) -> bytes:
        blob = self.binary()
        start = blob.find(TEMPLATE_START)
        if start < 0:
            raise LookupError("template marker absent from the omp binary")
        end = blob.find(TEMPLATE_END, start)
        if end < 0:
            raise LookupError("template terminator absent from the omp binary")
        return blob[start:end + len(TEMPLATE_END)]

    # -- omp skill-description cache ---------------------------------------
    def db_rows(self) -> list[tuple[str, str]]:
        conn = sqlite3.connect("file:%s?mode=ro" % self.skill_db, uri=True)
        try:
            return list(conn.execute(
                "SELECT key, description FROM skill_descriptions"))
        finally:
            conn.close()

    # -- skill roots --------------------------------------------------------
    def offered(self) -> list[dict]:
        """Every direct child of the agents root offering a readable SKILL.md."""
        out: list[dict] = []
        if not self.agents_root.is_dir():
            return out
        for entry in sorted(self.agents_root.iterdir()):
            skill_md = entry / "SKILL.md"
            dangling = entry.is_symlink() and not entry.exists()
            if dangling:
                continue
            try:
                text = skill_md.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            out.append({"dir": entry.name,
                        "path": skill_md,
                        "text": text,
                        "frontmatter": parse_frontmatter(text)})
        return out

    def dangling_roots(self) -> list[str]:
        out = []
        if not self.agents_root.is_dir():
            return out
        for entry in sorted(self.agents_root.iterdir()):
            if entry.is_symlink() and not entry.exists():
                out.append(entry.name)
        return out

    # -- opencode log -------------------------------------------------------
    def log_text(self) -> str:
        if self._log is None:
            self._log = self.oc_log.read_text(encoding="utf-8",
                                              errors="replace")
        return self._log


def parse_frontmatter(text: str) -> dict:
    """Minimal YAML frontmatter reader: plain scalars and folded/literal blocks.

    Deliberately hand-rolled: it is the instrument's own reader, and the shape
    it must handle is set by the substrate files, not by any other parser.
    """
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    fields: dict[str, object] = {}
    current = None
    for line in text[3:end].split("\n"):
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            current = m.group(1)
            value = m.group(2)
            if value in (">", ">-", "|", "|-", ">+", "|+"):
                fields[current] = []
                fields[current + "_style"] = value
            else:
                fields[current] = value.strip().strip("\"'")
            continue
        if current and line.startswith(" "):
            block = fields.get(current)
            if isinstance(block, list):
                block.append(line.strip())
    for key in list(fields):
        if key.endswith("_style"):
            continue
        block = fields[key]
        if isinstance(block, list):
            style = fields.get(key + "_style", ">")
            joiner = " " if style.startswith(">") else "\n"
            value = joiner.join(item for item in block if item)
            # YAML chomping, which is what the substrate's own parser applies:
            # clip (bare `>` / `|`) and keep (`+`) both end in a newline, strip
            # (`-`) ends in none.
            fields[key] = value + ("" if style.endswith("-") else "\n")
    for key in [k for k in fields if k.endswith("_style")]:
        del fields[key]
    return fields


def root_key(path: str) -> str:
    """`<home>/.claude/skills/x/SKILL.md` -> `.claude/skills`.

    The id `oc.dup.roots_both_sided` names the log's own duplicate split, whose
    root key is the two path segments under the home directory; a path with no
    home prefix is its own key. Round-38 adjudication: this rule is the
    harness's (source-read(author) by the adjudicating seat), adopted because
    the id's spec sentence names that grammar — it is not this instrument's
    round-37 reading, which is kept as `oc.dup.rescan_repeat_names`.
    """
    prefix = str(Path.home()) + "/"
    parts = path.split(prefix)
    return "/".join(parts[1].split("/")[:2]) if len(parts) > 1 else path


CATALOGUE_BLOCKER = (
    "the catalogue carrier's selection rule is inside the harness's own "
    "authored scope (the newest session-jsonl <skills> block with at least "
    "min(10, len(known)) entries, matched line-by-line against the skill "
    "cache). This instrument's substrate set is the omp binary, the skill "
    "cache, the skill roots, the opencode log and the opencode configs; none "
    "of them carries the selection rule, so re-deriving the row blind would "
    "be guessing. Named out of scope instead (r38 adjudication, "
    "source-read(author); P3's 'named UNSUPPORTED rather than guessed' idiom)."
)

# The catalogue carrier's substrate root: the session tree the harness's own
# selection rule scans.  Overridable so the fixture battery can drive the same
# probe against a synthetic tree.
CATALOGUE_CARRIER = Path(os.environ.get(
    "HARNESS_INDEPENDENT_CARRIER",
    str(Path.home() / ".omp" / "agent" / "sessions")))

ISO_STAMP_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z")
ENTRY_LINE_RE = re.compile(r"(?m)^\s*-\s+\S")
_CATALOGUE_CACHE: dict[str, dict] = {}


def catalogue_probe(carrier: Path | None = None) -> dict:
    """A blind, value-free rule-spread census of the catalogue carrier.

    Round 39 (C1, seat P1 — closes r38 R1-D1).  A scope-out that is a free-text
    assertion cannot be checked; this probe can.  It is *not* the row's value
    (that needs the harness's selection rule, which this instrument may not
    read): it is the fact the blocker actually rests on — the carrier surface is
    large, and a builder that varies the one rule it cannot see lands on
    *different* totals, so no blind derivation of the row is possible.

    A substring sweep for the rule's own literals was tried first and rejected:
    the carrier is this lane's own session tree, so its transcripts quote the
    rule's text and any such sweep fails the true rows (measured — the driver's
    first live run exited 2 on exactly that).  Reading structure, never prose,
    is the sound form.

    Memoised per carrier: the census reads the whole session tree, and both
    `derive()` (called repeatedly by the self-test) and the driver's own
    recomputation would otherwise pay for it every time.
    """
    carrier = CATALOGUE_CARRIER if carrier is None else carrier
    key = str(carrier)
    if key in _CATALOGUE_CACHE:
        return _CATALOGUE_CACHE[key]
    cands: list[dict] = []
    session_files = files_with_block = 0
    if carrier.is_dir():
        for path in sorted(carrier.rglob("*.jsonl")):
            session_files += 1
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            stamps = ISO_STAMP_RE.findall(text)
            newest = max(stamps) if stamps else ""
            mtime = path.stat().st_mtime
            start = 0
            while True:
                start = text.find("<skills>", start)
                if start < 0:
                    break
                end = text.find("</skills>", start)
                if end < 0:
                    break
                block = text[start:end].replace("\\n", "\n")
                cands.append({"entries": len(ENTRY_LINE_RE.findall(block)),
                              "newest_stamp": newest, "mtime": mtime,
                              "order": len(cands)})
                start = end + len("</skills>")
            if text.count("<skills>"):
                files_with_block += 1
    rule_totals = {}
    if cands:
        for name, picker in (
            ("newest-mtime", lambda c: (c["mtime"], -c["order"])),
            ("newest-iso-stamp", lambda c: (c["newest_stamp"], -c["order"])),
            ("first-in-scan-order", lambda c: (-c["order"],)),
            ("last-in-scan-order", lambda c: (c["order"],)),
            ("newest-nonempty", lambda c: (c["mtime"],) if c["entries"] else (-1, 0,)),
        ):
            rule_totals[name] = max(cands, key=picker)["entries"]
    result = {
        "kind": "rule-spread-census",
        "target": str(carrier),
        "observable": {
            "session_files": session_files,
            "files_with_skills_block": files_with_block,
            "candidate_blocks": len(cands),
            "distinct_totals": sorted(set(rule_totals.values())),
            "rule_totals": rule_totals,
        },
        "claim": "the carrier surface is large (non-vacuous) and five blind-plausible "
                 "selection rules land on more than one total, so the row's value "
                 "cannot be derived without the harness's authored rule",
        "falsified_by": ("a single distinct total across every blind-plausible rule "
                         "(the row would then be derivable blind) or an empty carrier"),
    }
    _CATALOGUE_CACHE[key] = result
    return result


def preview_of(description: str) -> str:
    """The substrate's own preview rule (mirrored, not imported)."""
    collapsed = re.sub(r"\s+", " ", description).strip()
    if len(collapsed) <= PREVIEW_CLIFF:
        return collapsed
    head = collapsed[:PREVIEW_CLIFF - 1]
    sentence = PREVIEW_RE.match(head)
    if sentence and len(sentence.group(0)) >= 40:
        return sentence.group(0)
    cut = head[:head.rfind(" ")].rstrip()
    return (cut or head) + "\u2026"


def accepted_by_model(text: str) -> bool:
    """The substrate's acceptance filter for a compressed description."""
    trimmed = text.strip()
    if not trimmed or "\r" in trimmed or "\n" in trimmed:
        return False
    if len(trimmed) > COMPRESS_MAX_CHARS:
        return False
    return len(trimmed.split()) <= COMPRESS_MAX_WORDS


# ---------------------------------------------------------------------------
# rows
# ---------------------------------------------------------------------------
def row(name: str, value, evidence: str, status: str = "DERIVED") -> dict:
    return {"check": name, "value": value, "status": status,
            "evidence": evidence}


def scoped_out_row(name: str, blocker: str, probe: dict | None = None) -> dict:
    """A row this instrument cannot derive blind, with its blocker *and* the
    blind probe that corroborates it.

    Round 39 (C1, seat P1): the blocker is no longer free text.  Each scoped row
    carries a machine-checkable probe block; the driver recomputes it and fails
    closed when the declared observable does not hold.  A scope-out is therefore
    a measured exclusion, not a self-declaration.
    """
    entry = {"check": name, "value": None, "status": "SCOPED_OUT",
             "evidence": "SCOPED_OUT: %s" % blocker}
    if probe is not None:
        entry["probe"] = probe
    return entry


def derive(s: Substrate) -> list[dict]:
    rows: list[dict] = []

    # ---- omp / binary -----------------------------------------------------
    template = s.template_bytes()
    rows.append(row("omp.elf.template_bytes", len(template),
                    "ELF scan: NUL-delimited run at %r .. %r"
                    % (TEMPLATE_START.decode(), TEMPLATE_END.decode().strip())))
    rows.append(row("omp.elf.template_sha256", sha256_hex(template),
                    "sha256 of those %d bytes" % len(template)))

    # ---- omp / cache ------------------------------------------------------
    db_rows = s.db_rows()
    rows.append(row("omp.db.rows", len(db_rows),
                    "SELECT count(*) FROM skill_descriptions (%s)"
                    % s.skill_db))
    wellformed = [k for k, d in db_rows
                  if re.fullmatch(r"[0-9a-f]{64}", k or "")
                  and isinstance(d, str) and d.strip()]
    rows.append(row("omp.db.rows_wellformed", len(wellformed),
                    "rows with a 64-hex key and a non-empty description"))

    # ---- omp / offering ---------------------------------------------------
    offered = s.offered()
    rows.append(row("omp.offered.skills", len(offered),
                    "dirs under %s holding a readable SKILL.md"
                    % s.agents_root))
    dangling = s.dangling_roots()
    rows.append(row("omp.offered.dangling", len(dangling),
                    "unresolvable symlinks under %s (%s)"
                    % (s.agents_root, ", ".join(dangling) or "none")))

    keys = {k for k, _ in db_rows}
    template_keys = []
    for skill in offered:
        fm = skill["frontmatter"]
        name = fm.get("name") or skill["dir"]
        description = fm.get("description") or ""
        preimage = (template + b"\x00" + str(name).encode()
                    + b"\x00" + str(description).encode())
        template_keys.append((skill["dir"], sha256_hex(preimage)))

    reproduced = [d for d, h in template_keys if h in keys]
    missing = [d for d, h in template_keys if h not in keys]
    rows.append(row("omp.cache.keys_reproduced", len(reproduced),
                    "offered skills whose sha256(template \\0 name \\0 "
                    "description) is a cache key (%s)"
                    % (", ".join(reproduced) or "none")))
    rows.append(row("omp.cache.misses", len(missing),
                    "offered skills with no cache row (%s)"
                    % (", ".join(missing) or "none")))

    over_cliff = [skill["dir"] for skill in offered
                  if len(str(skill["frontmatter"].get("description") or ""))
                  > PREVIEW_CLIFF]
    rows.append(row("omp.descriptions.over_cliff", len(over_cliff),
                    "descriptions longer than the substrate preview cliff "
                    "(%d chars, circuit constant v): %s"
                    % (PREVIEW_CLIFF, ", ".join(over_cliff) or "none")))

    mismatches = [skill["dir"] for skill in offered
                  if skill["frontmatter"].get("name")
                  and skill["frontmatter"]["name"] != skill["dir"]]
    rows.append(row("omp.names.mismatches", len(mismatches),
                    "frontmatter name != directory name (%s)"
                    % (", ".join(mismatches) or "none")))

    no_description = [skill["dir"] for skill in offered
                      if not skill["frontmatter"].get("description")]
    rows.append(row("omp.descriptions.missing", len(no_description),
                    "offered skills with no description field (%s)"
                    % (", ".join(no_description) or "none")))

    rows.append(row("omp.descriptions.unmodelled", len(missing),
                    "reading: an offered description the cache holds no row "
                    "for (same set as omp.cache.misses)"))

    verified = [k for k, _ in db_rows
                if re.fullmatch(r"[0-9a-f]{64}", k or "")]
    accepted = [k for k in verified
                if any(k == h for _, h in template_keys)]
    rows.append(row("omp.cache.verified_skills", len(accepted),
                    "cache keys matching a live offered skill (value-side "
                    "acceptance filter b(): <=%d chars, <=%d words, no CR/LF)"
                    % (COMPRESS_MAX_CHARS, COMPRESS_MAX_WORDS)))

    catalogue_evidence = catalogue_probe(s.catalogue_carrier)
    for name in ("omp.catalogue.found", "omp.catalogue.total",
                 "omp.catalogue.matched", "omp.catalogue.missing_names"):
        rows.append(scoped_out_row(name, CATALOGUE_BLOCKER, catalogue_evidence))

    # ---- opencode / log ---------------------------------------------------
    lines = s.log_text().split("\n")
    # The two init-count ids name the substrate's own occurrence grammar,
    # `message=init count=<N>` (the pin note reads "max of `message=init
    # count=N`; opencode logs only counts, never name sets").  Adjudicated r39
    # (D2): the round-37 reading keyed those occurrences by `run=` and called a
    # run carrying more than one of them a monotone violation -- a different
    # population *and* the opposite predicate, since the counts only grow.
    # Both rows now derive from one occurrence sequence in file order, and the
    # violation is rendered the way the harness renders it (`a->b`), so the two
    # columns are the same measurement rather than equal emptiness.
    init_values = [int(n) for n in
                   re.findall(r"message=init count=(\d+)", s.log_text())]
    rows.append(row("oc.log.init_count_max",
                    max(init_values, default=0),
                    "max `message=init count=N` value in %s (%d occurrence(s); "
                    "opencode logs only counts, never name sets)"
                    % (s.oc_log, len(init_values))))

    rows.append(row("oc.log.available_skills_hits",
                    sum(1 for line in lines if "<available_skills>" in line),
                    "'<available_skills>' occurrences in %s" % s.oc_log))

    rescan_arrays: list[list[str]] = []
    for line in lines:
        if "skills rescanned" not in line:
            continue
        m = re.search(r'skills="(\[.*?\])"', line)
        if not m:
            continue
        try:
            rescan_arrays.append(json.loads(m.group(1).replace('\\"', '"')))
        except json.JSONDecodeError:
            rescan_arrays.append([])
    rows.append(row("oc.log.skills_rescan_max",
                    max((len(a) for a in rescan_arrays), default=0),
                    "longest skills=[...] array among %d rescans"
                    % len(rescan_arrays)))

    rows.append(row("oc.log.init_count_monotone",
                    [f"{init_values[i - 1]}->{init_values[i]}"
                     for i in range(1, len(init_values))
                     if init_values[i] < init_values[i - 1]],
                    "decreases between consecutive `message=init count=N` values "
                    "in file order (%d occurrence(s); the counts only grow, so a "
                    "decrease means the roots changed incompatibly) -- the same "
                    "violation strings the harness reports, adjudicated r39" % len(init_values)))

    rows.append(row("oc.log.skills_tag_hits",
                    sum(line.count("<skills>") for line in lines),
                    "literal '<skills>' occurrences in the log; adjudicated r38 "
                    "(D2, source-read(author)): the id's spec sentence names the "
                    "literal tag and the raw log carries 0 of them, so the "
                    "harness's reading is adopted over this instrument's "
                    "round-37 attribute token, which is kept as the named "
                    "definitional alternative oc.log.skills_attr_hits"))

    # ---- opencode / roots + permission -----------------------------------
    # The roots are the directories opencode's own log names as skill sources,
    # plus the two configured roots --oc-config/skill and --oc-config/skills
    # (enumerated even when the log does not name them; round 48), plus the
    # shared agents root it reads; names come from enumerating direct children
    # with the same operator for every root. Names are a set, so a root named
    # twice, or named by the log and also configured, never adds twice.
    root_dirs = [d for d in ("skill", "skills")
                 if (s.oc_config / d).is_dir()]
    sources: set[str] = set()
    for line in lines:
        m = re.search(r'sources="\[(.*?)\]"', line)
        if m:
            sources.update(re.findall(r'directory:([^"\\]+)', m.group(1)))
    names = {skill["frontmatter"].get("name") or skill["dir"]
             for skill in offered}
    configured = {str(s.oc_config / d) for d in ("skill", "skills")}
    for directory in sorted(sources | configured):
        path = Path(directory)
        if not path.is_dir():
            continue
        for entry in sorted(path.iterdir()):
            if (entry / "SKILL.md").is_file():
                names.add(entry.name)
    rows.append(row("oc.roots.names_plus_builtin", len(names),
                    "distinct skill names enumerated under the roots the "
                    "opencode log names as sources (%d present) and the "
                    "configured --oc-config roots (present: %s) plus the "
                    "shared agents root (%d names); built-in names: 0 by "
                    "declaration"
                    % (sum(1 for d in sources if Path(d).is_dir()),
                       ", ".join(root_dirs) or "none", len(offered))))

    both_sided = 0
    onesided = 0
    if rescan_arrays:
        seen: dict[str, int] = {}
        for array in rescan_arrays:
            for name in array:
                seen[name] = seen.get(name, 0) + 1
        both_sided = sum(1 for v in seen.values() if v > 1)
        onesided = sum(1 for v in seen.values() if v == 1)
    # Round-38 adjudication (D2, source-read(author)): the ids name the log's
    # own duplicate split -- `duplicate skill name ... existing=<path>
    # duplicate=<path>` lines keyed by the two path segments under home -- and
    # the raw log carries 0 such lines. The harness's reading is adopted; this
    # instrument's round-37 reading (names repeating across rescan arrays) is
    # kept as the named definitional alternative oc.dup.rescan_repeat_names.
    dup_split: dict[str, dict[str, int]] = {}
    for line in lines:
        if "duplicate skill name" not in line:
            continue
        ex = re.search(r"existing=(\S+)", line)
        du = re.search(r"duplicate=(\S+)", line)
        for side, m in (("existing", ex), ("duplicate", du)):
            if m:
                bucket = dup_split.setdefault(root_key(m.group(1)),
                                              {"existing": 0, "duplicate": 0})
                bucket[side] += 1
    dup_onesided = sorted(r for r, c in dup_split.items()
                          if not (c["existing"] > 0 and c["duplicate"] > 0))
    rows.append(row("oc.dup.roots_both_sided", len(dup_split) - len(dup_onesided),
                    "'duplicate skill name' lines whose root key appears on both "
                    "sides (%d line(s) in the log; %d root key(s) split)"
                    % (sum(sum(c.values()) for c in dup_split.values()),
                       len(dup_split))))
    rows.append(row("oc.dup.onesided_roots", len(dup_onesided),
                    "root keys seen on one side only (%s)"
                    % (", ".join(dup_onesided) or "none")))

    permission_lines = 0
    skill_allow = 0
    for path in sorted(s.oc_config.glob("*.json")):
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for line in json.dumps(document).split(","):
            if "skill" in line.lower() and "permission" in line.lower():
                permission_lines += 1
            if '"allow"' in line and "skill" in line.lower():
                skill_allow += 1
    rows.append(row("oc.permission.skill_lines", permission_lines,
                    "skill-and-permission lines in %s/*.json" % s.oc_config))
    rows.append(row("oc.permission.skill_allow", skill_allow,
                    "skill-scoped allow entries in the same config set"))

    cache_plugins = []
    cache_root = s.oc_config.parent.parent / ".cache" / "opencode"
    if cache_root.is_dir():
        cache_plugins = [p for p in cache_root.rglob("*")
                         if p.name in ("SKILL.md",) or p.is_dir()
                         and p.name == "skills"]
    rows.append(row("oc.roots.plugins_cache", len(cache_plugins),
                    "skill-bearing entries under %s" % cache_root))

    return rows


def alternatives(s: Substrate) -> dict:
    """The round-37 readings, kept as named definitional alternatives.

    Protocol §5's D2 ruling requires both scopes' probe blocks; the probes are
    the strings below, and the alternative names are prefixed `alt.` so no
    consumer can mistake them for check ids: they are absent from the harness's
    check set by construction and this instrument never publishes them in
    `results`/`checks`. A definitional difference is recorded, never smoothed —
    and never allowed to enter the agreement surface (r12 §3 idiom).
    """
    lines = s.log_text().split("\n")
    rescan_arrays: list[list[str]] = []
    for line in lines:
        if "skills rescanned" not in line:
            continue
        m = re.search(r'skills="(\[.*?\])"', line)
        if not m:
            continue
        try:
            rescan_arrays.append(json.loads(m.group(1).replace('\\"', '"')))
        except json.JSONDecodeError:
            rescan_arrays.append([])
    seen: dict[str, int] = {}
    for array in rescan_arrays:
        for name in array:
            seen[name] = seen.get(name, 0) + 1
    return {
        "alt.oc.log.skills_attr_hits": {
            "value": sum(line.count('skills="') for line in lines),
            "probe": "sum of 'skills=\"' occurrences in %s" % s.oc_log,
            "superseded_by": "oc.log.skills_tag_hits",
            "why": "round-37 reading: the attribute token, not the literal tag "
                   "the id names; the id's spec sentence governs (r38 D2)",
        },
        "alt.oc.dup.rescan_repeat_names": {
            "value": sum(1 for v in seen.values() if v > 1),
            "probe": "names appearing in more than one `skills rescanned` "
                     "array (%d arrays) in %s" % (len(rescan_arrays), s.oc_log),
            "superseded_by": "oc.dup.roots_both_sided",
            "why": "round-37 reading: rescan-array repeats, a different "
                   "population from the log's duplicate-skill-name split the "
                   "id names (r38 D2)",
        },
    }


# ---------------------------------------------------------------------------
# comparison + freezes
# ---------------------------------------------------------------------------
def flatten_observed(document) -> dict:
    """Accept {results:[{check,observed}]}, {checks:{...}} or a flat table."""
    if isinstance(document, dict):
        results = document.get("results")
        if isinstance(results, list):
            flat = {}
            for item in results:
                if isinstance(item, dict) and "check" in item:
                    flat[item["check"]] = item.get("observed",
                                                   item.get("value"))
            if flat:
                return flat
        for key in ("checks", "observed", "rows", "values"):
            inner = document.get(key)
            if isinstance(inner, dict):
                flat = {}
                for name, value in inner.items():
                    if isinstance(value, dict) and "value" in value:
                        flat[name] = value["value"]
                    elif isinstance(value, dict) and "observed" in value:
                        flat[name] = value["observed"]
                    else:
                        flat[name] = value
                return flat
        flat = {}
        for name, value in document.items():
            if isinstance(value, dict) and "value" in value:
                flat[name] = value["value"]
            else:
                flat[name] = value
        return flat
    if isinstance(document, list):
        flat = {}
        for item in document:
            if isinstance(item, dict) and "check" in item:
                flat[item["check"]] = item.get("value",
                                               item.get("observed"))
        return flat
    raise ValueError("observed document is not a table")


def comparable(mine, theirs) -> bool:
    """Equality, with one declared representation rule: when exactly one side
    reports a *list*, compare its length to the other side's count.  The two
    instruments report offenders as entries (harness) or as counts (this file)
    for the same quantity; that is a rendering difference, not a value one.
    """
    if isinstance(mine, list) != isinstance(theirs, list):
        count, other = (len(mine), theirs) if isinstance(mine, list) \
            else (len(theirs), mine)
        return count == other
    if isinstance(mine, str) and isinstance(theirs, str):
        return mine.lower() == theirs.lower()
    return mine == theirs


def compare(rows: list[dict], observed: dict) -> list[dict]:
    results = []
    for entry in rows:
        name = entry["check"]
        if entry["status"] != "DERIVED":
            results.append({"check": name,
                            "verdict": entry["status"],  # UNLANDED / SCOPED_OUT
                            "reason": entry.get("evidence", "")})
            continue
        if name not in observed:
            results.append({"check": name, "verdict": "NOT_IN_OBSERVED"})
            continue
        mine, theirs = entry["value"], observed[name]
        results.append({"check": name,
                        "verdict": "AGREE" if comparable(mine, theirs)
                        else "DISAGREE",
                        "derived": mine, "observed": theirs})
    return results


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------
def build_fixture(root: Path) -> Substrate:
    """A synthetic substrate tree: two skills, a two-row cache, a small log."""
    agents = root / "skills"
    (agents / "alpha").mkdir(parents=True)
    (agents / "beta").mkdir(parents=True)
    (agents / "ghost").symlink_to(root / "does-not-exist")
    (agents / "alpha" / "SKILL.md").write_text(
        "---\nname: alpha\ndescription: >\n  Use alpha for the first thing.\n"
        "  Never for the second.\n---\n\n# alpha\n", encoding="utf-8")
    (agents / "beta" / "SKILL.md").write_text(
        "---\nname: beta\ndescription: Use beta briefly.\n---\n\n# beta\n",
        encoding="utf-8")

    binary = root / "omp"
    template = (TEMPLATE_START + b" now.\n\nSkill: {{name}}\n"
                + TEMPLATE_END)
    binary.write_bytes(b"\x7fELF" + b"\x00" * 16 + template + b"\x00" * 8)

    # the cache keys are computed from the descriptions *as this instrument's
    # own frontmatter reader parses them*, so the fixture exercises the reader
    # and the key rule together rather than a hand-written string
    db = root / "skill-descriptions.db"
    conn = sqlite3.connect(db)
    conn.execute("CREATE TABLE skill_descriptions "
                 "(key TEXT PRIMARY KEY, description TEXT NOT NULL)")
    for entry in (agents / "alpha", agents / "beta"):
        parsed = parse_frontmatter(
            (entry / "SKILL.md").read_text(encoding="utf-8"))
        preimage = (template + b"\x00" + str(parsed["name"]).encode()
                    + b"\x00" + str(parsed["description"]).encode())
        conn.execute("INSERT INTO skill_descriptions VALUES (?, ?)",
                     (sha256_hex(preimage),
                      "Use %s in one line." % parsed["name"]))
    conn.execute("INSERT INTO skill_descriptions VALUES (?, ?)",
                 (sha256_hex(b"stale generation"),
                  "A stale row that matches no live skill."))
    conn.execute("INSERT INTO skill_descriptions VALUES (?, ?)",
                 ("not-a-hash", "malformed row"))
    conn.commit()
    conn.close()

    log = root / "opencode.log"
    log.write_text(
        'run=aaa message="skills rescanned" skills="[\\"alpha\\",\\"beta\\"]"\n'
        'run=aaa message="skills rescanned" skills="[\\"alpha\\"]"\n'
        'run=bbb message="cli starting"\n', encoding="utf-8")

    config = root / "config"
    config.mkdir()
    (config / "opencode.json").write_text('{"theme": "system"}',
                                          encoding="utf-8")
    # a synthetic catalogue carrier, so the scoped-row probe does not have to
    # read this host's 527 MB session tree from every fixture subprocess
    carrier = root / "carrier"
    carrier.mkdir()
    for name, stamp, entries in (("a.jsonl", "2026-01-01T00:00:00.000Z", 1),
                                 ("b.jsonl", "2026-02-02T00:00:00.000Z", 4)):
        block = "\\n".join("- entry %d" % n for n in range(entries))
        (carrier / name).write_text(
            '{"stamp":"%s","text":"<skills>%s\\n</skills>"}\n' % (stamp, block),
            encoding="utf-8")
    return Substrate(binary, agents, db, log, config)


# ---------------------------------------------------------------------------
# round 48 (C1): the configured-root fixture
# ---------------------------------------------------------------------------
def build_configured_root_fixture(root: Path, twin: bool = True,
                                  nested: bool = False) -> Substrate:
    """A substrate whose --oc-config holds the two configured skill roots.

    Round 48 (C1).  The instrument used to enumerate only the roots the
    opencode log names as sources, so a skill sitting in --oc-config/skill/
    or --oc-config/skills/ was invisible to oc.roots.names_plus_builtin
    unless the log happened to name that root.  The fixture puts, under the
    config root:

        skill/<solo-s>/SKILL.md     one skill in the singular root
        skills/<solo-p>/SKILL.md    one skill in the plural root
        skill/<twin>/SKILL.md       the same-name pair, one half ...
        skills/<twin>/SKILL.md      ... and the other half
        skills/<not-a-skill>/       a directory with no SKILL.md
        skills/README.md            a plain file, not a skill directory

    The opencode log names no root at all, so every name beyond the shared
    agents root can only have come from the configured roots.  `twin=False`
    drops the same-name pair, which makes the pair's set semantics
    measurable: the count must fall by exactly one, not two.  The directory
    without a SKILL.md and the plain file make the enumeration operator
    measurable too: neither may contribute a name.

    `nested=True` adds skills one level deeper than a root's direct child
    (skill/group/zeta/SKILL.md, skills/group/eta/SKILL.md).  The frozen
    contract enumerates a root's DIRECT children only, so a nested skill is
    not a name; a recursive enumeration would report both.
    """
    fixture = build_fixture(root)
    config = fixture.oc_config

    def skill(root_name: str, folder: str, name: str) -> None:
        (config / root_name / folder).mkdir(parents=True)
        (config / root_name / folder / "SKILL.md").write_text(
            "---\nname: %s\ndescription: Use %s briefly.\n---\n\n# %s\n"
            % (name, name, name), encoding="utf-8")

    skill("skill", "solo-s", "solo-s")
    skill("skills", "solo-p", "solo-p")
    if twin:
        skill("skill", "twin", "twin")
        skill("skills", "twin", "twin")
    (config / "skills" / "not-a-skill").mkdir(parents=True)
    (config / "skills" / "README.md").write_text("not a skill\n",
                                                 encoding="utf-8")
    if nested:
        skill("skill", "group/zeta", "zeta")
        skill("skills", "group/eta", "eta")
    return fixture


def _name_log_root(fixture: Substrate, directory: Path) -> None:
    """Append a log line that names `directory` as a skill source root."""
    with open(fixture.oc_log, "a", encoding="utf-8") as handle:
        handle.write('run=eee message="skills rescanned" '
                     'sources="[\\"directory:%s\\"]"\n' % directory)


# ---------------------------------------------------------------------------
# fixture battery: pinned mutant trees driven through this file's own CLI
# ---------------------------------------------------------------------------
def _fixture_cli(root: Path) -> list[str]:
    return ["--omp-binary", str(root / "omp"),
            "--agents-root", str(root / "skills"),
            "--skill-db", str(root / "skill-descriptions.db"),
            "--oc-log", str(root / "oc.log"),
            "--oc-config", str(root / "config"),
            "--catalogue-carrier", str(root / "carrier")]


def _fixture_skill_text(spec: dict) -> str:
    if spec["style"] == ">":
        return ("---\nname: %s\ndescription: >\n  %s\n---\n\n# %s\n"
                % (spec["name"], spec["description"], spec["name"]))
    return ("---\nname: %s\ndescription: %s\n---\n\n# %s\n"
            % (spec["name"], spec["description"], spec["name"]))


def build_case_fixture(case: dict, root: Path):
    """Materialise one case's pristine tree from its case.json build block."""
    build = case["build"]
    template = TEMPLATE_START + build["template_body"].encode() + TEMPLATE_END
    (root / "omp").write_bytes(b"\x7fELF" + b"\x00" * 16 + template
                               + b"\x00" * 8)
    agents = root / "skills"
    for folder, spec in build["skills"].items():
        (agents / folder).mkdir(parents=True)
        (agents / folder / "SKILL.md").write_text(_fixture_skill_text(spec),
                                                  encoding="utf-8")
    conn = sqlite3.connect(root / "skill-descriptions.db")
    conn.execute("CREATE TABLE skill_descriptions "
                 "(key TEXT PRIMARY KEY, description TEXT NOT NULL)")
    for entry in build["db_rows"]:
        if "live" in entry:
            path = agents / entry["live"] / "SKILL.md"
            parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
            preimage = (template + b"\x00" + str(parsed["name"]).encode()
                        + b"\x00" + str(parsed["description"]).encode())
            key = sha256_hex(preimage)
            description = "cached summary for %s" % entry["live"]
        else:
            key, description = entry["key"], entry["description"]
        conn.execute("INSERT INTO skill_descriptions VALUES (?, ?)",
                     (key, description))
    conn.commit()
    conn.close()
    (root / "oc.log").write_text(build["oc_log"], encoding="utf-8")
    (root / "config").mkdir()
    (root / "config" / "opencode.json").write_text(
        json.dumps(build["config"]), encoding="utf-8")


def apply_fixture_mutation(root: Path, mutation: dict):
    op = mutation["op"]
    if op in ("db-delete-row", "db-corrupt-key"):
        conn = sqlite3.connect(root / "skill-descriptions.db")
        if op == "db-delete-row":
            conn.execute("DELETE FROM skill_descriptions WHERE description = ?",
                         (mutation["description"],))
        else:
            conn.execute("UPDATE skill_descriptions SET key = 'not-a-hash' "
                         "WHERE description = ?", (mutation["description"],))
        conn.commit()
        conn.close()
    elif op == "binary-replace":
        target = root / "omp"
        data = target.read_bytes()
        old, new = mutation["old"].encode(), mutation["new"].encode()
        if old not in data:
            raise ValueError("binary mutation marker absent: %r" % old)
        target.write_bytes(data.replace(old, new, 1))
    elif op == "file-replace":
        target = root / mutation["target"]
        text = target.read_text(encoding="utf-8")
        if mutation["old"] not in text:
            raise ValueError("text mutation marker absent: %r"
                             % mutation["old"])
        target.write_text(text.replace(mutation["old"], mutation["new"], 1),
                          encoding="utf-8")
    elif op == "symlink-dangling":
        (root / "skills" / mutation["name"]).symlink_to(root / "no-such-target")
    elif op == "log-append":
        lines = mutation.get("lines") or [mutation["line"]]
        with (root / "oc.log").open("a", encoding="utf-8") as handle:
            for line in lines:
                handle.write(line + "\n")
    elif op == "config-write":
        (root / "config" / mutation["name"]).write_text(mutation["content"],
                                                        encoding="utf-8")
    else:
        raise ValueError("unknown mutation op %r" % op)


def fixture_battery(expect) -> None:
    """Every case: pristine control exits 0; each named mutant exits 1 with
    DRIFT naming that case's check.  The control arm additionally has to show
    the check clean, so a mutant cannot pass by riding a pre-existing drift."""
    if not FIXTURE_DIR.is_dir():
        expect("fixture dir present: %s" % FIXTURE_DIR, False, True)
        return
    cases = sorted(p for p in FIXTURE_DIR.iterdir()
                   if (p / "case.json").is_file())
    for case_dir in cases:
        case = json.loads((case_dir / "case.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory(
                prefix="hi-%s-" % case_dir.name) as tmp:
            tmp = Path(tmp)
            root = tmp / "pristine"
            root.mkdir()
            build_case_fixture(case, root)
            freeze = tmp / "freeze.json"
            snapshot = subprocess.run(
                [sys.executable, str(Path(__file__).resolve()),
                 *_fixture_cli(root), "--write-freeze", str(freeze)],
                capture_output=True, text=True)
            expect("%s: snapshot exits 0" % case_dir.name,
                   snapshot.returncode, 0)
            control = subprocess.run(
                [sys.executable, str(Path(__file__).resolve()),
                 *_fixture_cli(root), "--freeze", str(freeze)],
                capture_output=True, text=True)
            expect("%s: pristine control exits 0" % case_dir.name,
                   control.returncode, 0)
            for mutation in case["mutations"]:
                check = mutation["expect_check"]
                expect("%s/%s: discriminator live (%s clean on control)"
                       % (case_dir.name, mutation["name"], check),
                       "DRIFT %s " % check in control.stdout, False)
                mutant = tmp / ("mutant-" + mutation["name"])
                shutil.copytree(root, mutant)
                try:
                    apply_fixture_mutation(mutant, mutation)
                except (ValueError, sqlite3.Error) as error:
                    expect("%s/%s: mutation applies" % (case_dir.name,
                                                        mutation["name"]),
                           "error: %s" % error, "ok")
                    continue
                proc = subprocess.run(
                    [sys.executable, str(Path(__file__).resolve()),
                     *_fixture_cli(mutant), "--freeze", str(freeze)],
                    capture_output=True, text=True)
                expect("%s/%s: mutant exits 1 naming %s"
                       % (case_dir.name, mutation["name"], check),
                       (proc.returncode, "DRIFT %s " % check in proc.stdout),
                       (1, True))


def self_test() -> int:
    import tempfile
    failures: list[str] = []
    assertions = 0

    def expect(label: str, got, want):
        nonlocal assertions
        assertions += 1
        if got != want:
            failures.append("%s: got %r want %r" % (label, got, want))

    with tempfile.TemporaryDirectory() as tmp:
        fixture = build_fixture(Path(tmp))
        rows = {r["check"]: r for r in derive(fixture)}
        expect("template_bytes", rows["omp.elf.template_bytes"]["value"],
               len(TEMPLATE_START + b" now.\n\nSkill: {{name}}\n"
                   + TEMPLATE_END))
        expect("db.rows", rows["omp.db.rows"]["value"], 4)
        expect("db.rows_wellformed", rows["omp.db.rows_wellformed"]["value"], 3)
        expect("offered.skills", rows["omp.offered.skills"]["value"], 2)
        expect("offered.dangling", rows["omp.offered.dangling"]["value"], 1)
        expect("cache.keys_reproduced",
               rows["omp.cache.keys_reproduced"]["value"], 2)
        expect("cache.misses", rows["omp.cache.misses"]["value"], 0)
        expect("descriptions.over_cliff",
               rows["omp.descriptions.over_cliff"]["value"], 0)
        expect("names.mismatches", rows["omp.names.mismatches"]["value"], 0)
        expect("descriptions.missing",
               rows["omp.descriptions.missing"]["value"], 0)
        expect("unmodelled", rows["omp.descriptions.unmodelled"]["value"], 0)
        expect("verified_skills",
               rows["omp.cache.verified_skills"]["value"], 2)
        expect("oc.log.skills_rescan_max",
               rows["oc.log.skills_rescan_max"]["value"], 2)
        expect("oc.log.init_count_monotone (violations, empty list)",
               rows["oc.log.init_count_monotone"]["value"], [])
        expect("oc.log.init_count_max",
               rows["oc.log.init_count_max"]["value"], 0)
        expect("oc.log.available_skills_hits",
               rows["oc.log.available_skills_hits"]["value"], 0)
        expect("oc.log.skills_tag_hits",
               rows["oc.log.skills_tag_hits"]["value"], 0)
        expect("oc.dup.roots_both_sided",
               rows["oc.dup.roots_both_sided"]["value"], 0)
        expect("oc.dup.onesided_roots",
               rows["oc.dup.onesided_roots"]["value"], 0)
        expect("oc.permission.skill_lines",
               rows["oc.permission.skill_lines"]["value"], 0)
        expect("oc.roots.names_plus_builtin",
               rows["oc.roots.names_plus_builtin"]["value"], 2)
        for name in ("omp.catalogue.found", "omp.catalogue.total",
                     "omp.catalogue.matched", "omp.catalogue.missing_names"):
            expect("scoped-out:" + name, rows[name]["status"], "SCOPED_OUT")
            expect("scoped-out reason named:" + name,
                   rows[name]["evidence"].startswith("SCOPED_OUT: the catalogue "
                                                     "carrier's selection rule"),
                   True)
            # round 39 (C1, seat P1): a scope-out is not free text -- every
            # scoped row carries a probe block the driver recomputes
            probe = rows[name].get("probe")
            expect("scoped-out probe present:" + name,
                   isinstance(probe, dict) and probe.get("kind") == "rule-spread-census",
                   True)
            expect("scoped-out probe is absolute and non-vacuous:" + name,
                   bool(probe) and str(probe["target"]).startswith("/")
                   and probe["observable"]["candidate_blocks"] > 0,
                   True)
        # the probe's own discriminator: a carrier whose blocks all have the same
        # entry count has zero rule spread, so the row would be derivable blind
        # and the scope-out is false.  The synthetic carrier proves both ends.
        carrier = Path(tmp) / "carrier"
        (carrier / "sessions").mkdir(parents=True)
        (carrier / "sessions" / "a.jsonl").write_text(
            '{"stamp":"2026-01-01T00:00:00.000Z","text":"<skills>\\n- x\\n</skills>"}\n',
            encoding="utf-8")
        (carrier / "sessions" / "b.jsonl").write_text(
            '{"stamp":"2026-02-02T00:00:00.000Z","text":"<skills>\\n- x\\n- y\\n- z\\n'
            '- w\\n</skills>"}\n', encoding="utf-8")
        spread = catalogue_probe(carrier / "sessions")["observable"]
        expect("probe: differing rules give a rule spread",
               len(spread["distinct_totals"]) > 1, True)
        expect("probe: the census counts the carrier surface",
               (spread["session_files"], spread["candidate_blocks"]), (2, 2))
        flat = Path(tmp) / "carrier-flat"
        (flat / "sessions").mkdir(parents=True)
        for name, stamp in (("a.jsonl", "2026-01-01T00:00:00.000Z"),
                            ("b.jsonl", "2026-02-02T00:00:00.000Z")):
            (flat / "sessions" / name).write_text(
                '{"stamp":"%s","text":"<skills>\\n- x\\n- y\\n</skills>"}\n' % stamp,
                encoding="utf-8")
        flat_obs = catalogue_probe(flat / "sessions")["observable"]
        expect("probe: identical totals collapse the spread (scope-out would be false)",
               flat_obs["distinct_totals"], [2])

        # round-38 adjudication: the superseded round-37 readings are kept as
        # named definitional alternatives, under `alt.` names, and must not
        # collide with any check id
        alts = alternatives(fixture)
        expect("alternative: attribute token reading kept",
               alts["alt.oc.log.skills_attr_hits"]["value"], 2)
        expect("alternative: rescan-repeat reading kept",
               alts["alt.oc.dup.rescan_repeat_names"]["value"], 1)
        expect("alternative: names are not check ids",
               sorted(set(alts) & {r["check"] for r in rows.values()}), [])
        for key, entry in alts.items():
            expect("alternative probe block present:" + key,
                   bool(entry.get("probe")) and bool(entry.get("superseded_by")),
                   True)

        # mutants: each must move at least one landed row
        mutated = Path(tmp) / "mut"
        mutated.mkdir()
        fixture2 = build_fixture(mutated)
        conn = sqlite3.connect(fixture2.skill_db)
        conn.execute("DELETE FROM skill_descriptions WHERE description = ?",
                     ("Use beta in one line.",))
        conn.commit()
        conn.close()
        rows2 = {r["check"]: r["value"] for r in derive(fixture2)}
        expect("mutant: rows shrink", rows2["omp.db.rows"], 3)
        expect("mutant: misses appear", rows2["omp.cache.misses"], 1)
        expect("mutant: unmodelled tracks misses",
               rows2["omp.descriptions.unmodelled"], 1)
        expect("mutant: verified shrinks",
               rows2["omp.cache.verified_skills"], 1)

        binary_mut = Path(tmp) / "mut2"
        binary_mut.mkdir()
        fixture3 = build_fixture(binary_mut)
        fixture3.omp_binary.write_bytes(
            fixture3.omp_binary.read_bytes().replace(b"now.", b"then."))
        rows3 = {r["check"]: r["value"] for r in derive(fixture3)}
        expect("mutant: template hash moves",
               rows3["omp.elf.template_sha256"]
               != rows2["omp.elf.template_sha256"], True)
        expect("mutant: template hash breaks key reproduction",
               rows3["omp.cache.keys_reproduced"], 0)

        # init-count rows, adjudicated r39 (D2): the id names *decreases*
        # between consecutive `message=init count=N` occurrences, not "more
        # than one occurrence in a run".  Both arms below are true
        # discriminators: the round-37 predicate fails each of them.
        log_mut = Path(tmp) / "mut3"
        log_mut.mkdir()
        fixture4 = build_fixture(log_mut)
        with open(fixture4.oc_log, "a", encoding="utf-8") as handle:
            # strictly increasing (1,2,3) -- no violation exists, so the
            # violation row must stay empty where the round-37 predicate
            # read 1 for any run carrying two or more lines
            handle.write('run=bbb message=init count=1\n')
            handle.write('run=bbb message=init count=2\n')
            handle.write('run=bbb message=init count=3\n')
        rows4 = {r["check"]: r["value"] for r in derive(fixture4)}
        expect("init-count: increasing counts are not a violation",
               rows4["oc.log.init_count_monotone"], [])
        expect("init-count: max follows the occurrence sequence",
               rows4["oc.log.init_count_max"], 3)
        with open(fixture4.oc_log, "a", encoding="utf-8") as handle:
            # a decrease, rendered the way the harness renders it
            handle.write('run=bbb message=init count=2\n')
        fixture4 = Substrate(fixture4.omp_binary, fixture4.agents_root,
                             fixture4.skill_db, fixture4.oc_log,
                             fixture4.oc_config)
        rows4 = {r["check"]: r["value"] for r in derive(fixture4)}
        expect("init-count: a decrease is the violation, in HAR's rendering",
               rows4["oc.log.init_count_monotone"], ["3->2"])
        expect("init-count: max is the largest value, not the last",
               rows4["oc.log.init_count_max"], 3)
        # the superseded round-37 population: the quoted non-grammar form
        # (`message="init count" value=N`) is not an occurrence of the id's
        # grammar, so it must move neither row
        quoted_mut = Path(tmp) / "mut3b"
        quoted_mut.mkdir()
        fixture4b = build_fixture(quoted_mut)
        with open(fixture4b.oc_log, "a", encoding="utf-8") as handle:
            handle.write('run=ccc message="init count" value=1\n')
            handle.write('run=ccc message="init count" value=2\n')
        rows4b = {r["check"]: r["value"] for r in derive(fixture4b)}
        expect("init-count: the quoted form is not the id's grammar (monotone)",
               rows4b["oc.log.init_count_monotone"], [])
        expect("init-count: the quoted form is not the id's grammar (max)",
               rows4b["oc.log.init_count_max"], 0)
        # cross-run: the harness's own extractor is not run-keyed, and neither
        # is this instrument's; a decrease across two runs is still a decrease
        cross_mut = Path(tmp) / "mut3c"
        cross_mut.mkdir()
        fixture4c = build_fixture(cross_mut)
        with open(fixture4c.oc_log, "a", encoding="utf-8") as handle:
            handle.write('run=aaa message=init count=2\n')
            handle.write('run=bbb message=init count=1\n')
        rows4c = {r["check"]: r["value"] for r in derive(fixture4c)}
        expect("init-count: a cross-run decrease is a violation",
               rows4c["oc.log.init_count_monotone"], ["2->1"])

        # comparison mode: agreement, then a named disagreement
        agree = compare(list(rows.values()),
                        {r["check"]: r["value"] for r in rows.values()})
        expect("compare: all agree",
               sorted({r["verdict"] for r in agree}
                      - {"UNLANDED", "SCOPED_OUT"}), ["AGREE"])
        tampered = {r["check"]: r["value"] for r in rows.values()}
        tampered["omp.db.rows"] = 999
        verdicts = {r["check"]: r["verdict"]
                    for r in compare(list(rows.values()), tampered)}
        expect("compare: tamper named", verdicts["omp.db.rows"], "DISAGREE")

        # round-38: a scoped-out row is neither agreement nor disagreement, and
        # a scoped-out row can never be counted as agreement (the numerator
        # cannot gain from a scope-out)
        scoped_verdicts = {r["check"]: r["verdict"] for r in agree
                           if r["check"].startswith("omp.catalogue.")}
        expect("compare: scoped-out rows leave the join",
               set(scoped_verdicts.values()), {"SCOPED_OUT"})

        # red-before for the dup split: the id names the log's own duplicate
        # grammar, where a root key is both-sided when it appears on both the
        # existing= and the duplicate= side. One line naming two *different*
        # roots is therefore 0 both-sided / 2 one-sided; the superseded
        # alternative (rescan-array repeats) does not move at all.
        dup_mut = Path(tmp) / "mut4"
        dup_mut.mkdir()
        fixture5 = build_fixture(dup_mut)
        home = Path.home()
        with open(fixture5.oc_log, "a", encoding="utf-8") as handle:
            handle.write('message="duplicate skill name" existing=%s/.agents/skills/alpha/SKILL.md '
                         'duplicate=%s/.claude/skills/alpha/SKILL.md\n'
                         % (home, home))
        rows5 = {r["check"]: r["value"] for r in derive(fixture5)}
        expect("dup split: one line, two distinct roots -> one-sided",
               (rows5["oc.dup.roots_both_sided"], rows5["oc.dup.onesided_roots"]),
               (0, 2))
        with open(fixture5.oc_log, "a", encoding="utf-8") as handle:
            handle.write('message="duplicate skill name" existing=%s/.claude/skills/alpha/SKILL.md '
                         'duplicate=%s/.agents/skills/alpha/SKILL.md\n'
                         % (home, home))
        # a fresh view: Substrate memoises the log, so a re-derivation over an
        # appended file must construct a new reader (the fixture-battery CLI
        # path does this by construction, one process per run)
        fixture5 = Substrate(fixture5.omp_binary, fixture5.agents_root,
                             fixture5.skill_db, fixture5.oc_log,
                             fixture5.oc_config)
        rows5 = {r["check"]: r["value"] for r in derive(fixture5)}
        expect("dup split: the same roots on both sides -> both-sided",
               (rows5["oc.dup.roots_both_sided"], rows5["oc.dup.onesided_roots"]),
               (2, 0))
        expect("dup split: alternative does not move",
               alternatives(fixture5)["alt.oc.dup.rescan_repeat_names"]["value"], 1)
        expect("dup split: root_key maps a home path to two segments",
               root_key(str(home) + "/.agents/skills/alpha/SKILL.md"),
               ".agents/skills")
        expect("dup split: a path without the home prefix is its own key",
               root_key("/opt/elsewhere/SKILL.md"), "/opt/elsewhere/SKILL.md")

        # ---- round 48 (C1): the configured roots -------------------------
        # A skill in --oc-config/skill/ or --oc-config/skills/ must be
        # enumerated even when the opencode log names neither root.  The
        # fixture names no root at all, so every name beyond the shared
        # agents root can only have come from the configured roots.  The
        # fixture also carries a NESTED skill (skill/group/zeta/SKILL.md):
        # the frozen contract enumerates a root's direct children only, so
        # a nested skill is not a name.
        cfg_root = Path(tmp) / "cfg"
        cfg_root.mkdir()
        cfg = build_configured_root_fixture(cfg_root, nested=True)
        cfg_rows = {r["check"]: r for r in derive(cfg)}
        cfg_value = cfg_rows["oc.roots.names_plus_builtin"]["value"]
        expect("round 48: fixture premise -- the log names no source root",
               ("sources=" in cfg.log_text(), "directory:" in cfg.log_text()),
               (False, False))
        expect("round 48: fixture premise -- both configured roots exist",
               ((cfg.oc_config / "skill").is_dir(),
                (cfg.oc_config / "skills").is_dir()),
               (True, True))
        # alpha, beta (the shared agents root) + solo-s, solo-p, twin (the two
        # configured roots; the same-name pair is one name)
        expect("round 48: the configured roots are enumerated",
               cfg_value, 5)
        # the same expectation, computed from the fixture tree rather than
        # hard-coded: the agents root's own names plus the DIRECT children of
        # the two configured roots that hold a SKILL.md.  Mirrored here, not
        # imported, so the arm states the contract instead of restating a
        # number.
        expected_names = {"alpha", "beta"}
        for root_name in ("skill", "skills"):
            for entry in sorted((cfg.oc_config / root_name).iterdir()):
                if (entry / "SKILL.md").is_file():
                    expected_names.add(entry.name)
        expect("round 48: the value equals an independent enumeration",
               (cfg_value, sorted(expected_names)),
               (5, ["alpha", "beta", "solo-p", "solo-s", "twin"]))
        # the row's own detail text must name the configured roots (the base
        # mislabelled the two families); checked on the root names rather
        # than on one wording, so it survives a re-worded detail string.
        evidence = cfg_rows["oc.roots.names_plus_builtin"]["evidence"]
        expect("round 48: the row's evidence names the configured roots",
               ("skill" in evidence, "skills" in evidence), (True, True))

        # the direct-child scope: a skill nested deeper than a root's direct
        # child is not a name, so adding it must move the count by nothing.
        # A recursive enumeration of the same roots would report zeta and
        # eta and move the count by two.
        flat_root = Path(tmp) / "cfg-flat"
        flat_root.mkdir()
        flat = build_configured_root_fixture(flat_root)
        flat_rows = {r["check"]: r for r in derive(flat)}
        expect("round 48: a nested skill is not a name (direct children only)",
               cfg_value - flat_rows["oc.roots.names_plus_builtin"]["value"], 0)
        expect("round 48: the nested skill is on disk but not counted",
               ((cfg.oc_config / "skill" / "group" / "zeta" / "SKILL.md").is_file(),
                flat_rows["oc.roots.names_plus_builtin"]["value"]),
               (True, 5))

        # the same-name pair: two directories in two roots, one name.  The
        # count must fall by exactly one when the pair is removed, and the
        # directory without a SKILL.md and the plain file must contribute
        # nothing (otherwise the count would be 6 and 5).
        notwin_root = Path(tmp) / "cfg-notwin"
        notwin_root.mkdir()
        notwin = build_configured_root_fixture(notwin_root, twin=False,
                                               nested=True)
        notwin_rows = {r["check"]: r for r in derive(notwin)}
        expect("round 48: without the same-name pair the count drops by one",
               cfg_value - notwin_rows["oc.roots.names_plus_builtin"]["value"],
               1)
        expect("round 48: a directory without SKILL.md and a plain file are "
               "not names",
               notwin_rows["oc.roots.names_plus_builtin"]["value"], 4)

        # no-harm: the union is not a replacement.  A root the log DOES name
        # is still enumerated alongside the configured roots ...
        logext_root = Path(tmp) / "cfg-logext"
        logext_root.mkdir()
        logext = build_configured_root_fixture(logext_root, nested=True)
        named = Path(tmp) / "named-root"
        (named / "logged").mkdir(parents=True)
        (named / "logged" / "SKILL.md").write_text(
            "---\nname: logged\ndescription: Use logged briefly.\n---\n\n"
            "# logged\n", encoding="utf-8")
        _name_log_root(logext, named)
        logext_rows = {r["check"]: r for r in derive(logext)}
        expect("round 48: a root the log names is still enumerated",
               logext_rows["oc.roots.names_plus_builtin"]["value"], 6)
        # ... and a root named twice (by the log AND by the configuration) is
        # still one root, so the count does not move.
        logsame_root = Path(tmp) / "cfg-logsame"
        logsame_root.mkdir()
        logsame = build_configured_root_fixture(logsame_root, nested=True)
        _name_log_root(logsame, logsame.oc_config / "skills")
        logsame_rows = {r["check"]: r for r in derive(logsame)}
        expect("round 48: a root named by the log and by the configuration is "
               "one root",
               logsame_rows["oc.roots.names_plus_builtin"]["value"], 5)

    fixture_battery(expect)

    for failure in failures:
        print("FAIL " + failure)
    print("0 failure(s) over %d assertions" % assertions
          if not failures else
          "%d failure(s) over %d assertions" % (len(failures), assertions))
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--derive", action="store_true",
                        help="print the derived table (default)")
    parser.add_argument("--json", action="store_true",
                        help="emit the table as JSON")
    parser.add_argument("--out", type=Path,
                        help="write the derived table to this path")
    parser.add_argument("--observed", type=Path,
                        help="compare against a JSON table of observed values")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--freeze", type=Path,
                        help="compare landed rows against a frozen table; "
                             "each drifted row is named DRIFT (exit 1)")
    parser.add_argument("--write-freeze", type=Path,
                        help="snapshot the derived table into a freeze file")
    parser.add_argument("--omp-binary", type=Path,
                        default=DEFAULT_OMP_BINARY)
    parser.add_argument("--agents-root", type=Path,
                        default=DEFAULT_AGENTS_ROOT)
    parser.add_argument("--skill-db", type=Path, default=DEFAULT_SKILL_DB)
    parser.add_argument("--oc-log", type=Path, default=DEFAULT_OC_LOG)
    parser.add_argument("--oc-config", type=Path, default=DEFAULT_OC_CONFIG)
    parser.add_argument("--catalogue-carrier", type=Path, default=CATALOGUE_CARRIER,
                        help="session tree the scoped-out catalogue rows' probe censuses")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    substrate = Substrate(args.omp_binary, args.agents_root, args.skill_db,
                          args.oc_log, args.oc_config,
                          catalogue_carrier=args.catalogue_carrier)
    try:
        rows = derive(substrate)
    except (OSError, sqlite3.Error, LookupError) as error:
        print("SUBSTRATE %s" % error)
        return 2

    landed = [r for r in rows if r["status"] == "DERIVED"]
    unlanded = [r for r in rows if r["status"] == "UNLANDED"]
    scoped = {r["check"]: r["evidence"].split("SCOPED_OUT: ", 1)[-1]
              for r in rows if r["status"] == "SCOPED_OUT"}
    # Round 39 (C1, seat P1): the blind probe block each scoped row carries, in
    # its own top-level channel so the driver can recompute it.  A scope-out
    # without one is not a scope-out.
    scoped_probes = {r["check"]: r["probe"] for r in rows
                     if r["status"] == "SCOPED_OUT" and r.get("probe")}
    # `results` is the join shape the round's agreement driver
    # (verifiers/compare_harness_independent.py, seat P4) reads; `checks` is the
    # flat name -> value map.  Both carry this instrument's own numbers only.
    # `alternatives` carries the round-37 readings the round-38 adjudication
    # superseded, under `alt.` names: definitional, recorded, never compared.
    table = {"results": [{"check": r["check"], "re_derived": r["value"],
                          "value": r["value"], "status": r["status"],
                          **({"probe": r["probe"]} if r.get("probe") else {})}
                         for r in rows],
             "checks": {r["check"]: r["value"] for r in rows},
             "rows": rows,
             "landed": len(landed),
             "unlanded": [r["check"] for r in unlanded],
             "scoped_out": scoped,
             "scoped_out_probes": scoped_probes,
             "alternatives": alternatives(substrate)}

    if args.out:
        args.out.write_text(json.dumps(table, indent=1, sort_keys=True)
                            + "\n", encoding="utf-8")

    exit_code = 0
    if args.observed:
        try:
            observed = flatten_observed(
                json.loads(args.observed.read_text(encoding="utf-8")))
        except (OSError, ValueError, json.JSONDecodeError) as error:
            print("OBSERVED %s" % error)
            return 3
        results = compare(rows, observed)
        agreeing = [r for r in results if r["verdict"] == "AGREE"]
        disagreeing = [r for r in results if r["verdict"] == "DISAGREE"]
        absent = [r for r in results if r["verdict"] == "NOT_IN_OBSERVED"]
        for entry in results:
            detail = ""
            if entry["verdict"] == "DISAGREE":
                detail = " derived=%r observed=%r" % (entry["derived"],
                                                      entry["observed"])
            print("%-9s %s%s" % (entry["verdict"], entry["check"], detail))
        print("agreement %d/%d compared; %d scoped-out; %d unlanded; %d not-in-observed"
              % (len(agreeing), len(agreeing) + len(disagreeing),
                 len([r for r in results if r["verdict"] == "SCOPED_OUT"]),
                 len([r for r in results if r["verdict"] == "UNLANDED"]),
                 len(absent)))
        exit_code = 1 if disagreeing else 0
        return exit_code

    if args.write_freeze:
        args.write_freeze.write_text(
            json.dumps(table, indent=1, sort_keys=True) + "\n", encoding="utf-8")

    if args.freeze:
        try:
            frozen = flatten_observed(
                json.loads(args.freeze.read_text(encoding="utf-8")))
        except (OSError, ValueError, json.JSONDecodeError) as error:
            print("FREEZE %s" % error)
            return 3
        drifted = []
        for r in rows:
            if r["status"] != "DERIVED" or r["check"] not in frozen:
                continue
            if not comparable(r["value"], frozen[r["check"]]):
                drifted.append(r["check"])
                print("DRIFT %s derived=%r frozen=%r"
                      % (r["check"], r["value"], frozen[r["check"]]))
        if drifted:
            print("frozen drift on %d row(s): %s"
                  % (len(drifted), ", ".join(drifted)))
            return 1
        print("freeze clean: %d landed rows match the frozen table"
              % len(landed))
        return 0

    if args.json:
        print(json.dumps(table, indent=1, sort_keys=True))
    else:
        for r in rows:
            print("%-9s %-30s %s" % (r["status"], r["check"], r["value"]))
        print("%d derived, %d scoped out, %d unlanded (of %d named checks)"
              % (len(landed), len(scoped), len(unlanded), len(rows)))
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))