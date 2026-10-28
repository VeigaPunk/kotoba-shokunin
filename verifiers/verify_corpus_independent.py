#!/usr/bin/env python3
"""verify_corpus_independent.py — non-author re-derivation of the corpus verdict classes.

An INDEPENDENT implementation: written from the class specification alone, with its
own tokenizer, its own counting code and its own fixtures.  It does not import,
read or copy ``verifiers/verify_corpus_integrity.py`` or
``corpus/knowledge/corpus-integrity-round11.md``.  Its value is that agreement with
that instrument is then *evidence*, not a restatement.

Classes (all scoped to tracked ``corpus/*.md``):

INDEX      every tracked corpus markdown file except ``corpus/README.md`` must be
           denoted by at least one backticked token in column 2 (File) of a
           coverage-map table row of ``corpus/README.md``.  Tokens may carry
           ``{a,b}`` alternation and globs.  A corpus-internal token matching no
           tracked file is STALE; a non-glob token whose corpus-relative path does
           not exist on disk is MISSING; a tracked file no token denotes is UNINDEXED.
POINTERS   a token whose text matches ``…/.ufo/reports/round-<digits>/….md`` inside a
           tracked corpus markdown file promises the file exists.  Resolution is
           relative to the citing file's directory (rooted as-is, `~` against
           `$HOME`, otherwise joined); a bare `.ufo/reports/...` path also
           resolves against the fleet root /home/vgpnk/Projects/shokunin when
           present there; a `<rev>:<path>` token resolves as a git object there,
           then in the fleet root, and both it and the bare fleet-root hop must
           bind identity (>= 400 bytes with `## SHONEN`) -- a marker file stays
           dead; an explicit locator is existence-only. Excluded: tokens with
           `<`/`>`, `*`, whitespace, or a `..` segment after the leading `../` hops;
           a quoted token is CONTEXT.
COMMITS    ``commit `<token>``` (word ``commit`` not preceded by a letter, digit,
           underscore or hyphen, token backticked) must be 7-40 hex characters and
           name a commit object in the lane repo or declared parent fleet root.
           A citation inside double quotes or a matching Markdown code span is
           CONTEXT, not a live commit reference.  A 7-40 hex prefix closed by a
           single U+2026 ellipsis is truncated CONTEXT (`commit_truncated_detail`).
           Round 81: a hex token absent from both is `commit_external` (INFO, never
           a drift class) only when the committed `verifiers/external-commits.json`
           binds it to a third repository through a committed receipt carrying both
           the hash and the repository; a line marker alone never exempts.

Exit: 0 every violation class empty, 1 any violation, 2 environment unreadable.
Read-only: never writes inside the analysed repository.  Deterministic output.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

FLEET_ROOT = "/home/vgpnk/Projects/shokunin"

CHECK_IDS = (
    "corpus.index.tracked_files",
    "corpus.index.unindexed",
    "corpus.index.stale_patterns",
    "corpus.index.missing_paths",
    "corpus.pointers.report_total",
    "corpus.pointers.report_dead",
    "corpus.pointers.commit_total",
    "corpus.pointers.commit_unresolvable",
    "corpus.pointers.commit_nonhash",
)

# ---------------------------------------------------------------- environment ---


class EnvError(Exception):
    """Environment unreadable: git unavailable/not a repo, corpus/ absent, or
    a tracked corpus file that cannot be read (deleted, a directory, unreadable)."""


def _git(repo, *args):
    try:
        return subprocess.run(
            ["git", "-C", repo, *args], capture_output=True, text=True
        )
    except OSError as exc:
        raise EnvError("git not runnable: %s" % exc) from exc


def git_unreadable(repo, proc):
    """The EnvError text for a failed `git rev-parse --git-dir`.

    A directory git reads and rejects is not a repository; a git that refuses
    to read at all (dubious ownership, a broken installation) is an
    environment failure and is reported with git's own words.
    """
    detail = (proc.stderr or "").strip()
    if "not a git repository" in detail:
        return "not a git repository: %s" % repo
    first = detail.splitlines()[0] if detail else "(git printed no diagnostic)"
    return ("git rev-parse --git-dir failed in %s (exit %d): %s"
            % (repo, proc.returncode, first))


def _open_text(path, label):
    """Open a corpus file for reading, or raise EnvError (exit 2) naming it.

    ``label`` is the repo-relative name, matching the primary instrument's
    ``cannot read tracked file <rel>`` idiom; the absolute path stays in the
    OSError text.
    """
    try:
        return open(path, encoding="utf-8")
    except OSError as exc:
        raise EnvError("cannot read tracked file %s: %s" % (label, exc)) from exc


def tracked_paths(repo, prefix):
    """Tracked, repo-relative paths under ``prefix`` (sorted)."""
    proc = _git(repo, "ls-files", "--", prefix)
    if proc.returncode != 0:
        raise EnvError("git ls-files failed: %s" % proc.stderr.strip())
    return sorted(p for p in proc.stdout.splitlines() if p)


def corpus_markdown(repo):
    return [p for p in tracked_paths(repo, "corpus/") if p.endswith(".md")]


# -------------------------------------------------------------------- tokens ---

# A path token: leading path part, the anchored ufo-reports shape, a tail up to the
# first ".md".  The tail admits whitespace (so that the whitespace exclusion of the
# specification is reachable at all) but never a backtick or a double quote; the
# leading part may not contain whitespace or any bracket/separator that would glue
# prose onto a path.
POINTER_RE = re.compile(
    r"""[^\s`"()\[\],;:]*\.ufo/reports/round-\d+/[^`"]*?\.md"""
)
COMMIT_RE = re.compile(r"(?<![A-Za-z0-9_-])commit\s+`([^`\s]+)`")
# Round 36 (scout P3b): a fenced region is opaque to the index census -- a
# coverage row quoted inside a ``` block is an example, not an index promise.
# Round 39 (seat P4, from V6b's r38 proof): closing needs CommonMark 4.5's rule
# -- same fence character, length >= the opener's, and no info string -- or a
# spec-illegal pseudo-closer silently ends the region early.
# Round 40 (seat F2, from V4's r39 residual): 4.5 also caps the fence line's
# indentation at three columns, and a tab reaches column 4, so the fence line
# may carry spaces only. A fence-like line indented four or more columns is
# indented code, content -- it neither opens nor closes a region.
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
HEX_RE = re.compile(r"\A[0-9a-fA-F]+\Z")
TRUNCATED_RE = re.compile(r"\A[0-9a-fA-F]{7,40}\u2026\Z")
# Round 81 (Q75): the reviewed manifest, the `<rev>:` prefix of an object-expression
# pointer (a ref name carrying a letter, or 7-40 hex, so `file.md:15:` never becomes
# one), and the round from which reports carry `## SHONEN` uniformly.
EXTERNAL_MANIFEST = "verifiers/external-commits.json"
IDENTITY_FROM_ROUND, REPORT_MIN_BYTES, REPORT_MARKER = 19, 400, b"## SHONEN"
ROUND_RE = re.compile(r"round-(\d+)/")
REV_PREFIX_RE = re.compile(r"(?<![A-Za-z0-9_./-])"
                           r"([A-Za-z_][A-Za-z0-9_.@^~/-]*|[0-9a-fA-F]{7,40}):\Z")


def backticked_spans(line):
    """[(start, end)] offsets of backticked regions, left to right."""
    pos = [i for i, ch in enumerate(line) if ch == "`"]
    return [(pos[k] + 1, pos[k + 1]) for k in range(0, len(pos) - 1, 2)]


def quote_spans(line):
    """[(start, end)] offsets of double-quoted regions, left to right."""
    spans, opening = [], None
    i = 0
    while i < len(line):
        if line[i] == "\\":
            i += 2
            continue
        if line[i] == '"':
            if opening is None:
                opening = i
            else:
                spans.append((opening, i + 1))
                opening = None
        i += 1
    return spans

def code_span_spans(line):
    """[(start, end)] complete matching Markdown code spans on one line."""
    runs = [(m.start(), m.end(), len(m.group())) for m in re.finditer(r"`+", line)]

    def unescaped(pos):
        slashes = 0
        pos -= 1
        while pos >= 0 and line[pos] == "\\":
            slashes += 1
            pos -= 1
        return slashes % 2 == 0

    spans = []
    i = 0
    while i < len(runs):
        open_start, _open_end, width = runs[i]
        if not unescaped(open_start):
            i += 1
            continue
        for j in range(i + 1, len(runs)):
            close_start, close_end, close_width = runs[j]
            if close_width == width and unescaped(close_start):
                spans.append((open_start, close_end))
                i = j + 1
                break
        else:
            i += 1
    return spans




def _inside(spans, start, end):
    return any(s <= start and end <= e for s, e in spans)


def pointer_tokens(line):
    """[(token, start, end)] for one line.

    Backticked spans are scanned first (a token may then contain whitespace, which
    the exclusion rule can reject); non-whitespace runs outside backticks are
    scanned second, so that prose mentions of a path are promises too.
    """
    out = []
    spans = backticked_spans(line)
    for s, e in spans:
        text = line[s:e]
        for m in POINTER_RE.finditer(text):
            out.append((m.group(0), s + m.start(), s + m.end()))
    for m in re.finditer(r"[^\s`\"]+", line):
        if _inside(spans, m.start(), m.end()):
            continue
        for pm in POINTER_RE.finditer(m.group(0)):
            out.append(
                (pm.group(0), m.start() + pm.start(), m.start() + pm.end())
            )
    # Round 81: a `<rev>:` glued to the match makes the token an object expression
    # (`HEAD:.ufo/reports/...`), so the revision belongs to the promise it makes.
    for i, (_token, start, end) in enumerate(out):
        rev = REV_PREFIX_RE.search(line[:start])
        if rev:
            out[i] = (line[rev.start():end], rev.start(), end)
    out.sort(key=lambda t: (t[1], t[2]))
    return out


def commit_tokens(line):
    """[(token, start, end)] for one line; span covers the whole citation."""
    return [(m.group(1), m.start(), m.end()) for m in COMMIT_RE.finditer(line)]


def has_dotdot_after_hops(token):
    rest = token
    while rest.startswith("../"):
        rest = rest[3:]
    return ".." in rest.split("/")


def pointer_exclusion(token):
    """Why the token is not a promise, or None."""
    if "<" in token or ">" in token:
        return "angle-bracket"
    if "*" in token:
        return "glob"
    if re.search(r"\s", token):
        return "whitespace"
    if has_dotdot_after_hops(token):
        return "dotdot-after-hops"
    return None


def resolve_pointer(token, citing_file):
    """Absolute path the token names, resolved from the citing file's directory."""
    if token.startswith("/"):
        return os.path.normpath(token)
    if token.startswith("~"):
        home = os.environ.get("HOME", "")
        if token == "~":
            return os.path.normpath(home)
        if token.startswith("~/"):
            return os.path.normpath(os.path.join(home, token[2:]))
        return os.path.normpath(token)  # ~user form: kept literal, will not resolve
    return os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(citing_file)), token)
    )


def report_target(token, citing_file, repo, fleet_root=FLEET_ROOT):
    """(route, bytes): "object" a `<rev>:<path>` expression read from the citing
    repo then the fleet root, "path" a path from the citing file, "fallback" the
    fleet hop for a bare path, "dead" nothing."""
    _rev, sep, rest = token.partition(":")
    if sep and rest.startswith(".ufo/reports/"):
        fleet = [fleet_root] if fleet_root and os.path.abspath(fleet_root) != repo else []
        for candidate in [repo] + fleet:
            proc = subprocess.run(["git", "-C", candidate, "cat-file", "blob", token],
                                  capture_output=True)
            if proc.returncode == 0:
                return "object", proc.stdout
        return "dead", None
    for route, found in (("path", resolve_pointer(token, citing_file)),
                         ("fallback", os.path.join(fleet_root, token))):
        if route == "fallback" and not token.startswith(".ufo/reports/"):
            continue
        if os.path.isfile(found):
            with open(found, "rb") as fh:
                return route, fh.read()
    return "dead", None


def report_identity_ok(token, data):
    """A report from round 19 on carries `## SHONEN`, and an object expression
    always claims report content; earlier targets predate the heading and stay
    existence-only -- a marker arm, not a completeness judgment of history."""
    m = ROUND_RE.search(token)
    if ":" not in token.split("/")[0] and not (m and int(m.group(1)) >= IDENTITY_FROM_ROUND):
        return True
    return data is not None and len(data) >= REPORT_MIN_BYTES and REPORT_MARKER in data


def pointer_shape(token):
    if token.startswith("/"):
        return "absolute"
    if token.startswith("~"):
        return "tilde"
    if token.startswith("./") or token.startswith("../"):
        return "relative"
    return "bare"


# --------------------------------------------------------------------- index ---


def fenced_line_numbers(lines):
    """1-based line numbers of a fenced region, fence lines included.

    An unclosed fence runs to EOF, so a half-deleted closer hides the tail
    rather than resurrecting it.

    Round 39 (seat P4): a fence-looking line closes the region only when it
    satisfies CommonMark 4.5 -- same fence character, at least as long as the
    opener, and no info string. Anything else (``` inside a ```` block,
    ```python, ``` nope) is content, not a closer, so the region stays opaque.

    Round 40 (seat F2): 4.5 also caps the fence line's indentation at three
    columns (a tab reaches column 4), so a fence-like line indented four or
    more columns is indented code -- content -- and neither opens nor closes
    the region. FENCE_RE carries the cap.
    """
    inside, char, open_len, out = False, "", 0, set()
    for lineno, line in enumerate(lines, 1):
        m = FENCE_RE.match(line)
        if m:
            out.add(lineno)
            run = m.group(1)
            if not inside:
                inside, char, open_len = True, run[0], len(run)
            elif run[0] == char and len(run) >= open_len and not m.group(2).strip():
                inside = False
        elif inside:
            out.add(lineno)
    return out


def coverage_cells(repo):
    """[(lineno, cell)] of column 2 in coverage-map table rows of corpus/README.md.

    Round 36 (scout P3b): rows inside a fenced region are skipped -- a quoted
    example of a coverage row is not a coverage promise.
    """
    readme = os.path.join(repo, "corpus", "README.md")
    if not os.path.exists(readme):
        raise EnvError("corpus/README.md missing")
    with _open_text(readme, "corpus/README.md") as fh:
        lines = fh.read().splitlines()
    opaque = fenced_line_numbers(lines)
    cells, in_section, outside = [], False, []
    for lineno, line in enumerate(lines, 1):
        if lineno in opaque:
            continue
        stripped = line.strip()
        if stripped.startswith("## "):
            in_section = stripped == "## Coverage map"
            continue
        if not stripped.startswith("|"):
            continue
        parts = stripped.split("|")
        if len(parts) < 5:
            continue
        cell = parts[2]
        if set(cell.strip()) <= set("-: "):
            continue
        (cells if in_section else outside).append((lineno, cell))
    return cells, outside


def expand_braces(token):
    m = re.search(r"\{([^{}]*)\}", token)
    if not m:
        return [token]
    out = []
    for alt in m.group(1).split(","):
        out.extend(expand_braces(token[: m.start()] + alt + token[m.end():]))
    return out


def is_corpus_internal(token):
    return not (token.startswith("/") or token.startswith("~") or
                token.startswith("../"))


def is_glob(token):
    return any(ch in token for ch in "*?[")


def analyse_index(repo, tracked_corpus):
    cells, outside = coverage_cells(repo)
    tokens = []
    for lineno, cell in cells:
        for m in re.finditer(r"`([^`]*)`", cell):
            tokens.append((lineno, m.group(1)))
    outside_tokens = [
        m.group(1)
        for _, cell in outside
        for m in re.finditer(r"`([^`]*)`", cell)
    ]
    corpus_rel = [p[len("corpus/"):] for p in tracked_corpus]
    all_rel = [p[len("corpus/"):] for p in tracked_paths(repo, "corpus/")]

    stale, missing, denoted = [], [], set()
    for lineno, token in tokens:
        patterns = expand_braces(token)
        # Round 33 (X2 companion): a rooted token (`/`, `~`, `../`) denotes no
        # corpus file, so it can be neither stale nor a coverage hit — but it is
        # still a path promise, and the checker now checks it. Skipping it here
        # outright left the two instruments disagreeing on exactly those shapes
        # (round-33 X4 defect 2). So: corpus-internal tokens get the full
        # stale/denoted/path treatment; rooted tokens get the path test only.
        if is_corpus_internal(token):
            hits = {
                rel
                for rel in all_rel
                for pat in patterns
                if _fnmatch(rel, pat)
            }
            denoted |= hits
            if not hits:
                stale.append("corpus/README.md:%d: %s" % (lineno, token))
        # A token is path-checked when no expansion carries a glob character:
        # brace alternation is expanded first and every expansion is then read as
        # the literal corpus-relative path it names.
        if not any(is_glob(pat) for pat in patterns):
            for pat in patterns:
                if not os.path.exists(os.path.join(repo, "corpus", pat)):
                    missing.append(
                        "corpus/README.md:%d: %s -> corpus/%s"
                        % (lineno, token, pat)
                    )
    unindexed = [
        p for p in tracked_corpus
        if p != "corpus/README.md" and p[len("corpus/"):] not in denoted
    ]
    return {
        "md_files": len(tracked_corpus),
        "tracked_files": len(tracked_paths(repo, "corpus/")),
        "index_tokens": len(tokens),
        "index_tokens_outside_coverage_map": len(outside_tokens),
        "unindexed": len(unindexed),
        "unindexed_detail": sorted(unindexed),
        "stale_tokens": len(stale),
        "stale_tokens_detail": sorted(stale),
        "missing_paths": len(missing),
        "missing_paths_detail": sorted(missing),
    }


def _fnmatch(name, pattern):
    import fnmatch

    return fnmatch.fnmatchcase(name, pattern)


# ------------------------------------------------------------------ pointers ---


def analyse_pointers(repo, tracked_corpus, fleet_root=FLEET_ROOT):
    excluded, quoted, dead, checked = [], [], [], []
    shapes = {"absolute": 0, "tilde": 0, "relative": 0, "bare": 0}
    candidates = 0
    for rel in tracked_corpus:
        path = os.path.join(repo, rel)
        with _open_text(path, rel) as fh:
            for lineno, line in enumerate(fh, 1):
                quotes = quote_spans(line)
                for token, start, end in pointer_tokens(line):
                    candidates += 1
                    why = pointer_exclusion(token)
                    if why:
                        excluded.append("%s:%d: %s [%s]" % (rel, lineno, token, why))
                        continue
                    if _inside(quotes, start, end):
                        quoted.append("%s:%d: %s" % (rel, lineno, token))
                        continue
                    checked.append("%s:%d: %s" % (rel, lineno, token))
                    shapes[pointer_shape(token)] += 1
                    route, payload = report_target(token, path, repo, fleet_root)
                    if route == "dead" or not report_identity_ok(token, payload):
                        dead.append("%s:%d: %s" % (rel, lineno, token))
    return {
        "report_candidates": candidates,
        "report_total": len(checked),
        "report_excluded": len(excluded),
        "report_excluded_detail": sorted(excluded),
        "report_quoted": len(quoted),
        "report_quoted_detail": sorted(quoted),
        "report_shapes": shapes,
        "report_dead": len(dead),
        "report_dead_detail": sorted(dead),
    }


def _committed_blob(repo, rel):
    """Bytes of ``HEAD:<rel>`` when rel is tracked there, else None."""
    if _git(repo, "ls-files", "--error-unmatch", "--", rel).returncode != 0:
        return None
    proc = subprocess.run(["git", "-C", repo, "cat-file", "blob", "HEAD:%s" % rel],
                          capture_output=True)
    return proc.stdout if proc.returncode == 0 else None


def _committed_blob(repo, rel):
    """Committed bytes of ``HEAD:<rel>``, else None (working-tree bytes are no evidence)."""
    proc = subprocess.run(["git", "-C", repo, "cat-file", "blob", "HEAD:%s" % rel],
                          capture_output=True)
    return proc.stdout if proc.returncode == 0 else None


def external_commits(repo):
    """{lowercase hex: repository} bound by the committed evidence manifest.

    Round 81 (Q75): a hash absent from lane and fleet is `commit_external` only
    through the committed `verifiers/external-commits.json` and a committed receipt
    whose pinned sha256 matches and whose bytes carry both the hash and the
    repository; every failed binding stays `commit_unresolvable`.  A line marker
    (`owner/repo@`, a repository URL in the row) never exempts."""
    try:
        rows = json.loads(_committed_blob(repo, EXTERNAL_MANIFEST).decode())["commits"]
    except (AttributeError, KeyError, TypeError, UnicodeDecodeError, ValueError):
        return {}
    bound = {}
    for row in rows if isinstance(rows, list) else []:
        row = row if isinstance(row, dict) else {}
        sha, name = row.get("hash"), row.get("repository")
        evidence = _committed_blob(repo, row.get("receipt") or "")
        text = (evidence or b"").decode("utf-8", "replace").lower()
        if not (evidence is not None and isinstance(sha, str) and isinstance(name, str)
                and len(sha) == 40 and sha == sha.lower() and HEX_RE.match(sha)
                and hashlib.sha256(evidence).hexdigest() == row.get("receipt_sha256")
                and sha in text and name.lower() in text
                and bound.get(sha, name) == name):
            if isinstance(sha, str):
                bound.pop(sha, None)  # unbound, or contradictory evidence
            continue
        bound[sha] = name
    return bound


def analyse_commits(repo, tracked_corpus, fleet_root=FLEET_ROOT, externals=None):
    if externals is None:
        externals = external_commits(repo)
    quoted, nonhash, unresolvable, citations = [], [], [], []
    external = []
    truncated = []
    for rel in tracked_corpus:
        path = os.path.join(repo, rel)
        with _open_text(path, rel) as fh:
            for lineno, line in enumerate(fh, 1):
                quotes = quote_spans(line)
                code = code_span_spans(line)
                for token, start, end in commit_tokens(line):
                    if _inside(quotes, start, end) or _inside(code, start, end):
                        quoted.append("%s:%d: %s" % (rel, lineno, token))
                        continue
                    if TRUNCATED_RE.match(token):
                        truncated.append("%s:%d: %s" % (rel, lineno, token))
                        continue
                    citations.append("%s:%d: %s" % (rel, lineno, token))
                    if not (7 <= len(token) <= 40 and HEX_RE.match(token)):
                        nonhash.append("%s:%d: %s" % (rel, lineno, token))
                        continue
                    proc = _git(repo, "cat-file", "-e", "%s^{commit}" % token)
                    if (proc.returncode != 0 and fleet_root
                            and os.path.abspath(fleet_root) != os.path.abspath(repo)):
                        proc = _git(fleet_root, "cat-file", "-e",
                                    "%s^{commit}" % token)
                    if proc.returncode != 0:
                        site = "%s:%d: %s" % (rel, lineno, token)
                        (external if token.lower() in externals
                         else unresolvable).append(site)
    return {
        "commit_candidates": len(citations) + len(quoted) + len(truncated),
        "commit_total": len(citations),
        "commit_hex_total": sum(
            1 for c in citations if HEX_RE.match(c.rsplit(": ", 1)[-1])
            and 7 <= len(c.rsplit(": ", 1)[-1]) <= 40
        ),
        "commit_quoted": len(quoted),
        "commit_quoted_detail": sorted(quoted),
        "commit_nonhash": len(nonhash),
        "commit_nonhash_detail": sorted(nonhash),
        "commit_truncated": len(truncated),
        "commit_truncated_detail": sorted(truncated),
        "commit_unresolvable": len(unresolvable),
        "commit_unresolvable_detail": sorted(unresolvable),
        "commit_external": len(external),
        "commit_external_detail": sorted(external),
    }


# ------------------------------------------------------------------- analysis ---


def analyse(repo):
    repo = os.path.abspath(repo)
    probe = _git(repo, "rev-parse", "--git-dir")
    if probe.returncode != 0:
        raise EnvError(git_unreadable(repo, probe))
    if not os.path.isdir(os.path.join(repo, "corpus")):
        raise EnvError("corpus/ missing in %s" % repo)
    if not os.path.isfile(os.path.join(repo, "corpus", "README.md")):
        raise EnvError("corpus/README.md missing in %s" % repo)
    tracked = corpus_markdown(repo)
    head = _git(repo, "rev-parse", "--short", "HEAD").stdout.strip()
    observed = {
        "index": analyse_index(repo, tracked),
        "pointers": analyse_pointers(repo, tracked),
        "commits": analyse_commits(repo, tracked),
    }
    return {"repo": repo, "head": head, "observed": observed}


def results_of(observed):
    idx, ptr, com = observed["index"], observed["pointers"], observed["commits"]
    return [
        {"check": CHECK_IDS[0], "mode": "observe",
         "observed": idx["tracked_files"], "verdict": "INFO"},
        {"check": CHECK_IDS[1], "mode": "zero",
         "observed": idx["unindexed"], "verdict": _v(idx["unindexed"])},
        {"check": CHECK_IDS[2], "mode": "zero",
         "observed": idx["stale_tokens"], "verdict": _v(idx["stale_tokens"])},
        {"check": CHECK_IDS[3], "mode": "zero",
         "observed": idx["missing_paths"], "verdict": _v(idx["missing_paths"])},
        {"check": CHECK_IDS[4], "mode": "observe",
         "observed": ptr["report_total"], "verdict": "INFO"},
        {"check": CHECK_IDS[5], "mode": "zero",
         "observed": ptr["report_dead"], "verdict": _v(ptr["report_dead"])},
        {"check": CHECK_IDS[6], "mode": "observe",
         "observed": com["commit_hex_total"], "verdict": "INFO"},
        {"check": CHECK_IDS[7], "mode": "zero",
         "observed": com["commit_unresolvable"], "verdict": _v(com["commit_unresolvable"])},
        {"check": CHECK_IDS[8], "mode": "zero",
         "observed": com["commit_nonhash"], "verdict": _v(com["commit_nonhash"])},
    ]


def _v(n):
    return "PASS" if n == 0 else "DRIFT"


def violations(observed):
    idx, ptr, com = observed["index"], observed["pointers"], observed["commits"]
    return (idx["unindexed"] + idx["stale_tokens"] + idx["missing_paths"] +
            ptr["report_dead"] + com["commit_unresolvable"] + com["commit_nonhash"])


def exit_code(observed):
    return 0 if violations(observed) == 0 else 1


# ------------------------------------------------------------------ rendering ---


def render(repo, head, observed, results, as_json):
    if as_json:
        return json.dumps(
            {"repo": repo, "head": head, "observed": observed, "results": results},
            indent=2, sort_keys=True,
        )
    lines = ["corpus independent derivation: %s (HEAD %s)" % (repo, head)]
    idx, ptr, com = observed["index"], observed["pointers"], observed["commits"]
    lines.append(
        "index   tracked_files=%d index_tokens=%d (outside coverage map=%d) "
        "unindexed=%d stale=%d missing=%d"
        % (idx["tracked_files"], idx["index_tokens"],
           idx["index_tokens_outside_coverage_map"], idx["unindexed"],
           idx["stale_tokens"], idx["missing_paths"])
    )
    lines.append(
        "points  candidates=%d checked=%d excluded=%d quoted=%d dead=%d shapes=%s"
        % (ptr["report_candidates"], ptr["report_total"], ptr["report_excluded"],
           ptr["report_quoted"], ptr["report_dead"], ptr["report_shapes"])
    )
    lines.append(
        "commits candidates=%d citations=%d hex=%d quoted=%d nonhash=%d "
        "unresolvable=%d external=%d"
        % (com["commit_candidates"], com["commit_total"], com["commit_hex_total"],
           com["commit_quoted"], com["commit_nonhash"], com["commit_unresolvable"],
           com["commit_external"])
    )
    for res in results:
        lines.append(
            "  %-38s %-8s observed=%s %s"
            % (res["check"], res["mode"], res["observed"], res["verdict"])
        )
    for key in ("unindexed_detail", "stale_tokens_detail", "missing_paths_detail",
                "report_dead_detail", "report_excluded_detail",
                "report_quoted_detail", "commit_nonhash_detail",
                "commit_truncated_detail", "commit_external_detail",
                "commit_unresolvable_detail", "commit_quoted_detail"):
        src = idx if key in idx else ptr if key in ptr else com
        for row in src[key]:
            lines.append("  ! %s" % row)
    lines.append("exit %d" % exit_code(observed))
    return "\n".join(lines)


# ----------------------------------------------------------------- self-test ---


class _SelfTest:
    def __init__(self):
        self.n = 0
        self.failures = []

    def eq(self, got, want, what):
        self.n += 1
        if got != want:
            self.failures.append("%s: got %r want %r" % (what, got, want))
            print("not ok %d - %s: got %r want %r" % (self.n, what, got, want))
        else:
            print("ok %d - %s" % (self.n, what))


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def _git_init(root, commit=False):
    os.makedirs(root, exist_ok=True)
    _git(root, "init", "-q")
    _git(root, "add", "-A")
    if commit:
        _git(root, "-c", "user.email=a@b", "-c", "user.name=t",
             "commit", "-q", "-m", "init")


def _fixture_index(root):
    _write(os.path.join(root, "corpus/README.md"), """# t

## Coverage map

| Area | File | Basis |
|------|------|-------|
| A | `knowledge/a.md` | x |
| BC | `knowledge/{b,c}.md` | x |
| Lessons | `lessons/*.md` | x |
| Ghost | `knowledge/ghost.md` | x |
| External | `../verifiers/other.py` | x |
| Rooted dead | `/tmp/x2-nowhere.md` | x |
| Rooted dead dir | `../nowhere/dead-dir/` | x |
| Globby | `nomatch/*.md` | x |
| Nothing | no token here | x |

## Other

| Area | File | Basis |
|------|------|-------|
| Outside | `knowledge/outside.md` | x |
""")
    for rel in ("corpus/knowledge/a.md", "corpus/knowledge/b.md",
                "corpus/knowledge/c.md", "corpus/knowledge/orphan.md",
                "corpus/lessons/z.md"):
        _write(os.path.join(root, rel), "# %s\n" % rel)
    _git_init(root)


def _fixture_fence(root, fenced=True, pseudo=False, indent=None, blockquote=False):
    lines = ["# t", "", "## Coverage map", "",
             "| Area | File | Basis |", "|------|------|-------|",
             "| Live | `knowledge/a.md` | x |"]
    if pseudo:
        # Round 39 (seat P4): the r38 exploit shape -- a ```` block whose only
        # pseudo-closer is a shorter ```. The quoted row must stay opaque.
        lines += ["````", "```", "| Fenced | `knowledge/b.md` | x |", "````"]
    elif indent is not None:
        # Round 40 (seat F2, from V4's r39 residual): a fence-like line indented
        # four or more columns (spaces or a tab) is indented code -- content --
        # so it cannot close the ```` block and the quoted row stays opaque.
        lines += ["````", indent, "| Fenced | `knowledge/b.md` | x |", "````"]
    elif blockquote:
        lines += ["> ````", "> | Fenced | `knowledge/b.md` | x |", "> ````"]
    elif fenced:
        lines += ["```", "| Fenced | `knowledge/b.md` | x |", "```"]
    else:
        lines += ["| Fenced | `knowledge/b.md` | x |"]
    _write(os.path.join(root, "corpus/README.md"), "\n".join(lines) + "\n")
    for rel in ("corpus/knowledge/a.md", "corpus/knowledge/b.md"):
        _write(os.path.join(root, rel), "# %s\n" % rel)
    _git_init(root)


def _fixture_pointers(root, home):
    _write(os.path.join(root, "corpus/README.md"), "# t\n")
    _write(os.path.join(root, "corpus/knowledge/p.md"), """
relative resolvable `./rel/.ufo/reports/round-1/a.md`
relative dead `./rel/.ufo/reports/round-9/gone.md`
absolute resolvable `%s/abs/.ufo/reports/round-2/b.md`
tilde resolvable `~/.ufo/reports/round-3/c.md`
bare resolvable `.ufo/reports/round-4/d.md`
bare dead `.ufo/reports/round-9/e.md`
excluded angle `<repo>/.ufo/reports/round-1/x.md`
excluded glob `.ufo/reports/round-1/*.md`
excluded whitespace `.ufo/reports/round-1/x y.md`
excluded dotdot `../up/../.ufo/reports/round-1/x.md`
quoted context ".ufo/reports/round-1/x.md"
prose /prose/.ufo/reports/round-7/p.md
""" % root)
    for rel in ("corpus/knowledge/rel/.ufo/reports/round-1/a.md",
                "corpus/knowledge/.ufo/reports/round-4/d.md",
                "abs/.ufo/reports/round-2/b.md"):
        _write(os.path.join(root, rel), "# x\n")
    _write(os.path.join(home, ".ufo/reports/round-3/c.md"), "# x\n")
    _git_init(root)


def _fixture_commits(root):
    _write(os.path.join(root, "corpus/README.md"), "# t\n")
    _git_init(root, commit=True)
    sha = _git(root, "rev-parse", "HEAD").stdout.strip()
    short = sha[:7]
    big = "a" * 41
    _write(os.path.join(root, "corpus/knowledge/c.md"), """
resolvable commit `%s`
unresolvable commit `deadbeef`
nonhash word commit `notahash`
nonhash short commit `abc123`
nonhash long commit `%s`
truncated id commit `abcdef1…`
quoted context "commit `deadbeef`"
hyphen prefix foo-commit `deadbeef`
letter prefix xcommit `deadbeef`
no space commit`deadbeef`
""" % (short, big))
    _git(root, "add", "-A")


def _report_body():
    return "# report\n\n" + "row\n" * 120 + "## SHONEN\n"


def _fixture_round81(root, fleet):
    """Round 81: external-commit binding and report identity in one measured repo."""
    rec = ".ufo/waves/round-1/snapshots/E1.fetch.json"
    receipt = "https://github.com/acme/widget %s\n" % ("4" * 40)
    _write(os.path.join(root, "corpus/README.md"), "# t\n")
    _write(os.path.join(root, rec), receipt)
    _write(os.path.join(root, EXTERNAL_MANIFEST), json.dumps({"commits": [{
        "hash": "4" * 40, "repository": "acme/widget", "receipt": rec,
        "receipt_sha256": hashlib.sha256(receipt.encode()).hexdigest()}]}))
    _write(os.path.join(root, "corpus/knowledge/r.md"), """
bound commit `%s`
marked commit `%s` acme/widget@ https://github.com/acme/widget
object `HEAD:.ufo/reports/round-5/kotoba.md`
object marker `HEAD:.ufo/reports/round-6/kotoba.md`
object gone `HEAD:.ufo/reports/round-9/none.md`
fallback `.ufo/reports/round-20/kotoba.md`
fallback marker `.ufo/reports/round-21/kotoba.md`
""" % ("4" * 40, "5" * 40))
    _write(os.path.join(root, ".ufo/reports/round-5/kotoba.md"), _report_body())
    _write(os.path.join(root, ".ufo/reports/round-6/kotoba.md"), "marker\n")
    _write(os.path.join(fleet, ".ufo/reports/round-20/kotoba.md"), _report_body())
    _write(os.path.join(fleet, ".ufo/reports/round-21/kotoba.md"), "marker\n")
    _git_init(root, commit=True)


def _fixture_clean(root):
    _write(os.path.join(root, "corpus/README.md"), """# t

## Coverage map

| Area | File | Basis |
|------|------|-------|
| A | `knowledge/a.md` | x |
""")
    _write(os.path.join(root, "corpus/knowledge/a.md"), "# a\n")
    _git_init(root)


def self_test():
    st = _SelfTest()
    tmp = tempfile.mkdtemp(prefix="corpus-independent-selftest-")
    old_home = os.environ.get("HOME")
    try:
        # -- index: brace + glob coverage, stale, unindexed, missing -------------
        iroot = os.path.join(tmp, "index")
        _fixture_index(iroot)
        idx = analyse_index(iroot, corpus_markdown(iroot))
        st.eq(idx["unindexed"], 1, "index: only orphan.md unindexed")
        st.eq(idx["unindexed_detail"], ["corpus/knowledge/orphan.md"],
              "index: unindexed detail names orphan.md")
        st.eq(idx["stale_tokens"], 2, "index: ghost.md + nomatch/*.md stale")
        st.eq(idx["stale_tokens_detail"],
              ["corpus/README.md:10: knowledge/ghost.md",
               "corpus/README.md:14: nomatch/*.md"],
              "index: stale detail (glob token counts as stale pattern)")
        st.eq(idx["missing_paths"], 4,
              "index: ghost + 3 rooted tokens (external, rooted dead, rooted dead dir)")
        st.eq(idx["missing_paths_detail"],
              ["corpus/README.md:10: knowledge/ghost.md -> corpus/knowledge/ghost.md",
               "corpus/README.md:11: ../verifiers/other.py -> corpus/../verifiers/other.py",
               "corpus/README.md:12: /tmp/x2-nowhere.md -> corpus//tmp/x2-nowhere.md",
               "corpus/README.md:13: ../nowhere/dead-dir/ -> corpus/../nowhere/dead-dir/"],
              "index: missing detail (brace expansions path-checked; rooted tokens checked)")
        st.eq(idx["index_tokens"], 8, "index: eight tokens in the coverage map")
        st.eq(idx["index_tokens_outside_coverage_map"], 1,
              "index: one token outside the coverage map section, not counted")
        # brace expansion denotes both b and c; lessons/*.md denotes z.md
        st.eq(sorted(expand_braces("knowledge/{b,c}.md")),
              ["knowledge/b.md", "knowledge/c.md"], "index: brace expansion")
        st.eq(sorted(expand_braces("a/{b,c}/{d,e}.md")),
              ["a/b/d.md", "a/b/e.md", "a/c/d.md", "a/c/e.md"],
              "index: nested brace expansion")
        st.eq(expand_braces("no/braces.md"), ["no/braces.md"],
              "index: token without braces is its own expansion")
        st.eq(is_corpus_internal("../verifiers/x.py"), False,
              "index: ../ token is not corpus-internal")
        st.eq(is_corpus_internal("/abs/x.md"), False,
              "index: rooted token is not corpus-internal")

        # -- index: a fenced row is quoted text, not a coverage promise ----------
        # Round 36 (scout P3b): the census used to harvest a coverage row that
        # sits inside a ``` block, so a fenced copy of a real row kept the index
        # satisfied. The unfenced fixture is the control that proves the fence
        # (not something else) is the discriminator.
        froot = os.path.join(tmp, "fence")
        _fixture_fence(froot, fenced=True)
        fidx = analyse_index(froot, corpus_markdown(froot))
        st.eq(fidx["index_tokens"], 1,
              "fence: only the live row's token is harvested")
        st.eq(fidx["unindexed"], 1, "fence: the fenced row's file stays unindexed")
        st.eq(fidx["unindexed_detail"], ["corpus/knowledge/b.md"],
              "fence: unindexed detail names the fenced row's file")
        uroot = os.path.join(tmp, "fence-unfenced")
        _fixture_fence(uroot, fenced=False)
        uidx = analyse_index(uroot, corpus_markdown(uroot))
        st.eq(uidx["index_tokens"], 2,
              "fence control: without the fence both rows count")
        st.eq(uidx["unindexed"], 0, "fence control: both files are covered")
        # Round 39 (seat P4) end to end: the r38 exploit shape on the real path --
        # a ```` block closed only by a shorter ```. Before the closer rule this
        # fixture harvested the quoted row and reported unindexed=0 (silent
        # false-PASS, exit 0); the row must now stay opaque.
        proot = os.path.join(tmp, "fence-pseudo-closer")
        _fixture_fence(proot, pseudo=True)
        pidx = analyse_index(proot, corpus_markdown(proot))
        st.eq(pidx["index_tokens"], 1,
              "fence pseudo-closer: only the live row's token is harvested")
        st.eq(pidx["unindexed"], 1,
              "fence pseudo-closer: the quoted row's file stays unindexed")
        st.eq(fenced_line_numbers(["x", "~~~", "a", "```", "b", "```", "c", "~~~", "d"]),
              {2, 3, 4, 5, 6, 7, 8},
              "fence: a mismatched fence char does not close")
        # cmark 0.31.2 sourcepos classifies an unclosed tilde fence and a mixed
        # backtick pseudo-closer as one code block through EOF. Its blockquote
        # fence sourcepos is lines 1-3, which the line-only scanner misses; the
        # coverage-path impact remains fail-safe because the row is prefixed by >.
        st.eq(fenced_line_numbers(["before", "~~~", "body", "| row"]), {2, 3, 4},
              "fence: an unclosed tilde fence runs to EOF")
        st.eq(fenced_line_numbers(["~~~", "body", "```", "tail"]), {1, 2, 3, 4},
              "fence: a mixed backtick pseudo-closer does not close tilde")
        st.eq(fenced_line_numbers(["> ````", "> body", "> ````"]), set(),
              "fence: blockquote container is outside the line scanner")
        qroot = os.path.join(tmp, "fence-blockquote")
        _fixture_fence(qroot, blockquote=True)
        qidx = analyse_index(qroot, corpus_markdown(qroot))
        st.eq(qidx["index_tokens"], 1,
              "blockquote fence: only the live row is harvested")
        st.eq(qidx["unindexed"], 1,
              "blockquote fence: quoted row file remains unindexed")
        st.eq(qidx["unindexed_detail"], ["corpus/knowledge/b.md"],
              "blockquote fence: fail-safe impact names the unindexed file")
        # Round 39 (seat P4): the CommonMark 4.5 closer rule. A fence-looking line
        # closes the region only with the same char, length >= the opener's and no
        # info string; every other shape is content. Each assertion is one of
        # V6b's three silent false-PASS exploits or a boundary of the rule.
        st.eq(fenced_line_numbers(["x", "````", "row", "```", "more", "````"]),
              {2, 3, 4, 5, 6}, "fence: a shorter closer is content, not a closer")
        st.eq(fenced_line_numbers(["x", "````", "row", "```python", "more", "````"]),
              {2, 3, 4, 5, 6}, "fence: a closer with an info string is content")
        st.eq(fenced_line_numbers(["x", "```", "row", "``` nope", "more", "```"]),
              {2, 3, 4, 5, 6}, "fence: a closer with trailing text is content")
        st.eq(fenced_line_numbers(["x", "```", "row", "`````", "after"]), {2, 3, 4},
              "fence: a longer closer closes")
        st.eq(fenced_line_numbers(["x", "````", "row", "````", "after"]), {2, 3, 4},
              "fence: a same-length closer closes")
        st.eq(fenced_line_numbers(["x", "```", "row", "```   ", "after"]), {2, 3, 4},
              "fence: an empty-info closer with trailing blanks closes")
        st.eq(fenced_line_numbers(["x", "````python", "row", "```", "````"]),
              {2, 3, 4, 5},
              "fence: a legal info opener still needs a >= opener-length closer")
        # Round 40 (seat F2, from V4's r39 residual): CommonMark 4.5 also caps
        # the fence line's indentation at three columns, and a tab advances to
        # column 4 (spec § Tabs), so any leading tab is already too deep. A
        # fence-like line indented four or more columns is indented code --
        # content: it neither opens nor closes a region. Before the cap a
        # 4-space or tab pseudo-closer ended the ```` block early and the
        # quoted row read as a live promise (unindexed=0, exit 0). Every
        # expected set below is derived from cmark 0.31.2 alone; the
        # 0/2/3-space controls prove the cap, not the shape, is the
        # discriminator.
        st.eq(fenced_line_numbers(["x", "````", "````", "after"]), {2, 3},
              "fence indent: a 0-space closer closes")
        st.eq(fenced_line_numbers(["x", "````", "  ````", "after"]), {2, 3},
              "fence indent: a 2-space closer closes")
        st.eq(fenced_line_numbers(["x", "````", "   ````", "row", "````"]),
              {2, 3, 5}, "fence indent: a 3-space closer closes")
        st.eq(fenced_line_numbers(["x", "````", "    ````", "row", "````"]),
              {2, 3, 4, 5}, "fence indent: a 4-space closer is content")
        st.eq(fenced_line_numbers(["x", "````", "\t````", "row", "````"]),
              {2, 3, 4, 5}, "fence indent: a tab closer is content")
        st.eq(fenced_line_numbers(["x", "````", "  \t````", "row", "````"]),
              {2, 3, 4, 5}, "fence indent: a mixed space+tab closer is content")
        st.eq(fenced_line_numbers(["x", "    ````", "row", "````", "after"]),
              {4, 5}, "fence indent: a 4-space opener is content")
        st.eq(fenced_line_numbers(["x", "\t````", "row", "````", "after"]),
              {4, 5}, "fence indent: a tab opener is content")
        st.eq(fenced_line_numbers(["x", "~~~~", "    ~~~~", "row", "~~~~"]),
              {2, 3, 4, 5}, "fence indent: a 4-space tilde closer is content")
        st.eq(fenced_line_numbers(["x", "~~~~", "\t~~~~", "row", "~~~~"]),
              {2, 3, 4, 5}, "fence indent: a tab tilde closer is content")
        # End to end on the census path: the quoted row must stay opaque, so
        # knowledge/b.md stays unindexed and the gate fails safe. The 3-space
        # control closes, so both rows count and b.md is covered.
        for tag, closer in (("4space", "    ````"), ("tab", "\t````")):
            iroot2 = os.path.join(tmp, "fence-indent-" + tag)
            _fixture_fence(iroot2, indent=closer)
            iidx = analyse_index(iroot2, corpus_markdown(iroot2))
            st.eq(iidx["index_tokens"], 1,
                  f"fence indent {tag}: only the live row's token is harvested")
            st.eq(iidx["unindexed"], 1,
                  f"fence indent {tag}: the quoted row's file stays unindexed")
            st.eq(iidx["unindexed_detail"], ["corpus/knowledge/b.md"],
                  f"fence indent {tag}: unindexed detail names the quoted file")
        croot = os.path.join(tmp, "fence-indent-3space-control")
        _fixture_fence(croot, indent="   ````")
        cidx = analyse_index(croot, corpus_markdown(croot))
        st.eq(cidx["index_tokens"], 2,
              "fence indent control: a 3-space closer closes, both rows count")
        st.eq(cidx["unindexed"], 0,
              "fence indent control: a 3-space closer covers the second file")

        # -- pointers: four shapes, every exclusion, quoted context, dead --------
        proot = os.path.join(tmp, "pointers")
        phome = os.path.join(tmp, "home")
        os.makedirs(phome)
        _fixture_pointers(proot, phome)
        os.environ["HOME"] = phome
        ptr = analyse_pointers(proot, corpus_markdown(proot))
        st.eq(ptr["report_total"], 7, "pointers: seven checked promises")
        st.eq(ptr["report_shapes"],
              {"absolute": 2, "bare": 2, "relative": 2, "tilde": 1},
              "pointers: all four shapes counted")
        st.eq(ptr["report_excluded"], 4, "pointers: four excluded tokens")
        st.eq(sorted(r.rsplit("[", 1)[-1].rstrip("]")
                     for r in ptr["report_excluded_detail"]),
              ["angle-bracket", "dotdot-after-hops", "glob", "whitespace"],
              "pointers: every exclusion reason fires")
        st.eq(ptr["report_quoted"], 1, "pointers: one quoted token is context")
        st.eq(ptr["report_dead"], 3,
              "pointers: dead relative, dead bare and dead prose token")
        st.eq(sorted(r.rsplit(": ", 1)[-1] for r in ptr["report_dead_detail"]),
              ["./rel/.ufo/reports/round-9/gone.md",
               ".ufo/reports/round-9/e.md",
               "/prose/.ufo/reports/round-7/p.md"],
              "pointers: dead detail")
        st.eq(ptr["report_candidates"], 12, "pointers: candidate population")
        st.eq(pointer_shape("/a/b.md"), "absolute", "pointers: shape absolute")
        st.eq(pointer_shape("~/.a/b.md"), "tilde", "pointers: shape tilde")
        st.eq(pointer_shape("../a/b.md"), "relative", "pointers: shape relative")
        st.eq(pointer_shape(".a/b.md"), "bare", "pointers: shape bare")
        st.eq(resolve_pointer("/a/b.md", "/x/y.md"), "/a/b.md",
              "pointers: rooted token resolves as-is")
        st.eq(resolve_pointer("~/b.md", "/x/y.md"), os.path.join(phome, "b.md"),
              "pointers: tilde resolves against HOME")
        st.eq(resolve_pointer("../b.md", "/x/y/z.md"), "/x/b.md",
              "pointers: relative hops resolve from the citing directory")
        st.eq(resolve_pointer(".ufo/reports/round-1/a.md",
                              "/x/corpus/k.md"),
              "/x/corpus/.ufo/reports/round-1/a.md",
              "pointers: bare token joins the citing directory")
        st.eq(has_dotdot_after_hops("../../a/../b.md"), True,
              "pointers: dotdot after leading hops detected")
        st.eq(has_dotdot_after_hops("../../../a/b.md"), False,
              "pointers: pure leading hops are not dotdot-after-hops")

        fallback_repo = os.path.join(tmp, "fleet-fallback-lane")
        fallback_fleet = os.path.join(tmp, "fleet-fallback-root")
        _write(os.path.join(fallback_repo, "corpus/lessons/closure.md"),
               "Report `.ufo/reports/round-53/kotoba.md`\n")
        _write(os.path.join(fallback_fleet, ".ufo/reports/round-53/kotoba.md"),
               _report_body())
        fallback = analyse_pointers(
            fallback_repo, ["corpus/lessons/closure.md"], fallback_fleet
        )
        st.eq(fallback["report_total"], 1,
              "pointers: fleet-root report remains checked")
        st.eq(fallback["report_dead"], 0,
              "pointers: a real fleet report binds identity; a marker would not")

        # -- commits: nonhash vs unresolvable vs resolvable ----------------------
        croot = os.path.join(tmp, "commits")
        _fixture_commits(croot)
        com = analyse_commits(croot, corpus_markdown(croot))
        st.eq(com["commit_total"], 5, "commits: five citations in scope")
        st.eq(com["commit_nonhash"], 3, "commits: 6-hex, 41-hex and word are nonhash")
        st.eq(com["commit_unresolvable"], 1,
              "commits: deadbeef unresolvable, the real sha resolvable")
        st.eq(com["commit_hex_total"] - com["commit_unresolvable"], 1,
              "commits: exactly one hex citation resolves")
        st.eq(com["commit_quoted"], 1, "commits: quoted citation is context")
        st.eq(com["commit_candidates"], 7, "commits: candidate population")
        st.eq(com["commit_truncated"], 1, "commits: hex+ellipsis is context")
        st.eq(TRUNCATED_RE.match("abc12\u2026") is not None, False,
              "commits: short prefix stays nonhash")
        st.eq(com["commit_hex_total"], 2, "commits: two hex-shaped citations")
        st.eq(len(com["commit_nonhash_detail"]), 3, "commits: nonhash detail sorted")
        st.eq(sorted(r.rsplit(": ", 1)[-1] for r in com["commit_unresolvable_detail"]),
              ["deadbeef"],
              "commits: unresolvable detail")
        st.eq(HEX_RE.match("abcdef1") is not None, True, "commits: 7 hex accepted")
        st.eq(HEX_RE.match("ABCDEF1") is not None, True,
              "commits: uppercase hex accepted")
        st.eq(bool(7 <= len("abcdef") <= 40 and HEX_RE.match("abcdef")), False,
              "commits: 6 hex rejected by length")
        # Round 66: independently derive the parent-fleet object fallback and
        # code-span context exclusion. The lane and fleet objects are distinct;
        # the nested single-backtick token is inside an outer double-backtick
        # example and must not become a live unresolved citation.
        fleet_root = os.path.join(tmp, "commit-fleet")
        _write(os.path.join(fleet_root, "seed.txt"), "fleet-only object\n")
        _git_init(fleet_root, commit=True)
        fleet_sha = _git(fleet_root, "rev-parse", "HEAD").stdout.strip()
        _write(os.path.join(croot, "corpus/knowledge/fleet.md"),
               "fleet-only commit `%s`\n"
               "The `` commit `451a02ff` `` grammar is explanatory.\n" % fleet_sha)
        _git(croot, "add", "-A")
        fleet_com = analyse_commits(croot, corpus_markdown(croot), fleet_root)
        st.eq(fleet_com["commit_total"], 6,
              "commits: fleet-only object is one live citation")
        st.eq(fleet_com["commit_unresolvable"], 1,
              "commits: only the genuinely absent lane token stays unresolved")
        st.eq(fleet_com["commit_quoted"], 2,
              "commits: double-quoted and code-span examples are context")
        st.eq(fleet_com["commit_candidates"], 9,
              "commits: context candidates stay visible, never live")

        # -- round 81: external binding (Q75) and report identity ---------------
        r81 = os.path.join(tmp, "round81")
        r81fleet = os.path.join(tmp, "round81-fleet")
        _fixture_round81(r81, r81fleet)
        xobs = analyse_commits(r81, corpus_markdown(r81))
        st.eq((xobs["commit_external"], xobs["commit_unresolvable"]), (1, 1),
              "r81: the receipt-pinned hash is external, the marker-bound one is not")
        p81 = analyse_pointers(r81, corpus_markdown(r81), r81fleet)
        st.eq((p81["report_total"], p81["report_dead"]), (5, 3),
              "r81: absent objects and markers are dead on the object and fleet routes")
        _write(os.path.join(r81, EXTERNAL_MANIFEST), json.dumps({"commits": [{
            "hash": "4" * 40, "repository": "acme/widget",
            "receipt": ".ufo/waves/round-1/snapshots/E1.fetch.json",
            "receipt_sha256": "0" * 64}]}))
        _git_init(r81, commit=True)
        st.eq(analyse_commits(r81, corpus_markdown(r81))["commit_external"], 0,
              "r81: a wrong receipt pin binds nothing; a line marker never exempts")
        _write(os.path.join(r81, ".ufo/reports/round-5/kotoba.md"), "marker\n")
        _git_init(r81, commit=True)
        st.eq(analyse_pointers(r81, corpus_markdown(r81), r81fleet)["report_dead"], 4,
              "r81: substituting a marker for a cited report turns it dead")


        # -- clean fixture: verdicts and exit code -------------------------------
        froot = os.path.join(tmp, "clean")
        _fixture_clean(froot)
        obs = analyse(froot)["observed"]
        st.eq(violations(obs), 0, "clean: no violations")
        st.eq(exit_code(obs), 0, "clean: exit 0")
        st.eq([r["verdict"] for r in results_of(obs) if r["mode"] == "zero"],
              ["PASS"] * 6, "clean: six violation classes all PASS")

        # -- environment gate ----------------------------------------------------
        plain = os.path.join(tmp, "plain")
        os.makedirs(plain)
        try:
            analyse(plain)
            st.eq("no-raise", "EnvError", "env: non-git directory rejected")
        except EnvError:
            st.eq("EnvError", "EnvError", "env: non-git directory rejected")
        nogit = os.path.join(tmp, "nogit")
        _git_init(nogit)
        try:
            analyse(nogit)
            st.eq("no-raise", "EnvError", "env: missing corpus/ rejected")
        except EnvError:
            st.eq("EnvError", "EnvError", "env: missing corpus/ rejected")

        # -- own CLI end to end --------------------------------------------------
        proc = subprocess.run(
            [sys.executable, os.path.abspath(__file__), "--repo", froot, "--json"],
            capture_output=True, text=True,
        )
        st.eq(proc.returncode, 0, "cli: clean fixture exits 0")
        st.eq(json.loads(proc.stdout)["repo"], froot, "cli: json names the repo")
        proc = subprocess.run(
            [sys.executable, os.path.abspath(__file__), "--repo", iroot, "--json"],
            capture_output=True, text=True,
        )
        st.eq(proc.returncode, 1, "cli: drifting fixture exits 1")
        st.eq(json.loads(proc.stdout)["observed"]["index"]["unindexed"], 1,
              "cli: drifting fixture reports unindexed=1")
        # -- could-not-evaluate: git is unavailable -----------------------------
        no_git_path = os.path.join(tmp, "no-git-path")
        os.makedirs(no_git_path)
        os.symlink(sys.executable, os.path.join(no_git_path, "python3"))
        no_git_env = dict(os.environ)
        no_git_env["PATH"] = no_git_path
        proc = subprocess.run(
            [sys.executable, os.path.abspath(__file__), "--repo", froot],
            capture_output=True, text=True, env=no_git_env,
        )
        st.eq(proc.returncode, 2, "cli: unavailable git exits 2")
        st.eq(proc.stderr.startswith("could-not-evaluate: git not runnable:"), True,
              "cli: unavailable git reports could-not-evaluate")

        # -- could-not-evaluate: git is present and refuses (exit 128) ---------
        # A refusing git is an environment failure: the gate must quote git's
        # own words, not claim the repository is not a repository.
        refusing_path = os.path.join(tmp, "refusing-git-path")
        os.makedirs(refusing_path)
        os.symlink(sys.executable, os.path.join(refusing_path, "python3"))
        shim = os.path.join(refusing_path, "git")
        with open(shim, "w", encoding="utf-8") as fh:
            fh.write("#!/bin/sh\n"
                     "echo \"fatal: detected dubious ownership in repository"
                     " at '/x/y'\" >&2\n"
                     "exit 128\n")
        os.chmod(shim, 0o755)
        refusing_env = dict(os.environ)
        refusing_env["PATH"] = refusing_path
        proc = subprocess.run(
            [sys.executable, os.path.abspath(__file__), "--repo", froot],
            capture_output=True, text=True, env=refusing_env,
        )
        st.eq(proc.returncode, 2, "cli: refusing git exits 2")
        st.eq(proc.stderr.startswith("could-not-evaluate: "), True,
              "cli: refusing git reports could-not-evaluate")
        st.eq("not a git repository" in proc.stderr, False,
              "cli: refusing git is not reported as a non-repository")
        st.eq("dubious ownership" in proc.stderr, True,
              "cli: refusing git quotes git's own refusal")
    finally:
        if old_home is None:
            os.environ.pop("HOME", None)
        else:
            os.environ["HOME"] = old_home
        shutil.rmtree(tmp, ignore_errors=True)
    print("self-test: %d assertions, %d failures" % (st.n, len(st.failures)))
    return 1 if st.failures else 0


# ----------------------------------------------------------------------- main ---


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="independent corpus integrity derivation (index, pointers, commits)")
    parser.add_argument("--repo", default=os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))),
        help="repository to analyse (default: this script's grandparent directory)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--self-test", action="store_true",
                        help="falsify this model on its own fixtures")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    try:
        analysis = analyse(args.repo)
    except EnvError as exc:
        sys.stderr.write("could-not-evaluate: %s\n" % exc)
        return 2
    observed = analysis["observed"]
    print(render(analysis["repo"], analysis["head"], observed,
                 results_of(observed), args.json))
    return exit_code(observed)


if __name__ == "__main__":
    sys.exit(main())