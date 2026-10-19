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
           relative to the citing file's directory (rooted as-is, ``~`` against
           ``$HOME``, otherwise joined).  Excluded: tokens with ``<``/``>``, with
           ``*``, with whitespace, with a ``..`` segment after the leading ``../``
           hops; a token fully inside double quotes on its line is CONTEXT.
COMMITS    ``commit `<token>``` (word ``commit`` not preceded by a letter, digit,
           underscore or hyphen, token backticked) must be 7-40 hex characters and
           ``git -C <repo> cat-file -e <token>^{commit}`` must succeed.  A citation
           fully inside double quotes on its line is CONTEXT.

Exit: 0 every violation class empty, 1 any violation, 2 environment unreadable.
Read-only: never writes inside the analysed repository.  Deterministic output.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

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
    """Environment unreadable: not a git repo, corpus/ or corpus/README.md absent,
    or a tracked corpus file that cannot be read (deleted, a directory, unreadable)."""


def _git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args], capture_output=True, text=True
    )


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
HEX_RE = re.compile(r"\A[0-9a-fA-F]+\Z")


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


def pointer_shape(token):
    if token.startswith("/"):
        return "absolute"
    if token.startswith("~"):
        return "tilde"
    if token.startswith("./") or token.startswith("../"):
        return "relative"
    return "bare"


# --------------------------------------------------------------------- index ---


def coverage_cells(repo):
    """[(lineno, cell)] of column 2 in coverage-map table rows of corpus/README.md."""
    readme = os.path.join(repo, "corpus", "README.md")
    if not os.path.exists(readme):
        raise EnvError("corpus/README.md missing")
    cells, in_section, outside = [], False, []
    with _open_text(readme, "corpus/README.md") as fh:
        for lineno, line in enumerate(fh, 1):
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
        if not is_corpus_internal(token):
            continue
        patterns = expand_braces(token)
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


def analyse_pointers(repo, tracked_corpus):
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
                    if not os.path.exists(resolve_pointer(token, path)):
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


def analyse_commits(repo, tracked_corpus):
    quoted, nonhash, unresolvable, citations = [], [], [], []
    for rel in tracked_corpus:
        path = os.path.join(repo, rel)
        with _open_text(path, rel) as fh:
            for lineno, line in enumerate(fh, 1):
                quotes = quote_spans(line)
                for token, start, end in commit_tokens(line):
                    if _inside(quotes, start, end):
                        quoted.append("%s:%d: %s" % (rel, lineno, token))
                        continue
                    citations.append("%s:%d: %s" % (rel, lineno, token))
                    if not (7 <= len(token) <= 40 and HEX_RE.match(token)):
                        nonhash.append("%s:%d: %s" % (rel, lineno, token))
                        continue
                    proc = _git(repo, "cat-file", "-e", "%s^{commit}" % token)
                    if proc.returncode != 0:
                        unresolvable.append("%s:%d: %s" % (rel, lineno, token))
    return {
        "commit_candidates": len(citations) + len(quoted),
        "commit_total": len(citations),
        "commit_hex_total": sum(
            1 for c in citations if HEX_RE.match(c.rsplit(": ", 1)[-1])
            and 7 <= len(c.rsplit(": ", 1)[-1]) <= 40
        ),
        "commit_quoted": len(quoted),
        "commit_quoted_detail": sorted(quoted),
        "commit_nonhash": len(nonhash),
        "commit_nonhash_detail": sorted(nonhash),
        "commit_unresolvable": len(unresolvable),
        "commit_unresolvable_detail": sorted(unresolvable),
    }


# ------------------------------------------------------------------- analysis ---


def analyse(repo):
    repo = os.path.abspath(repo)
    if _git(repo, "rev-parse", "--git-dir").returncode != 0:
        raise EnvError("not a git repository: %s" % repo)
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
        "unresolvable=%d"
        % (com["commit_candidates"], com["commit_total"], com["commit_hex_total"],
           com["commit_quoted"], com["commit_nonhash"], com["commit_unresolvable"])
    )
    for res in results:
        lines.append(
            "  %-38s %-8s observed=%s %s"
            % (res["check"], res["mode"], res["observed"], res["verdict"])
        )
    for key in ("unindexed_detail", "stale_tokens_detail", "missing_paths_detail",
                "report_dead_detail", "report_excluded_detail",
                "report_quoted_detail", "commit_nonhash_detail",
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
quoted context "commit `deadbeef`"
hyphen prefix foo-commit `deadbeef`
letter prefix xcommit `deadbeef`
no space commit`deadbeef`
""" % (short, big))
    _git(root, "add", "-A")


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
               "corpus/README.md:12: nomatch/*.md"],
              "index: stale detail (glob token counts as stale pattern)")
        st.eq(idx["missing_paths"], 1, "index: only the non-glob ghost is missing")
        st.eq(idx["missing_paths_detail"],
              ["corpus/README.md:10: knowledge/ghost.md -> corpus/knowledge/ghost.md"],
              "index: missing detail (brace expansions are path-checked per expansion)")
        st.eq(idx["index_tokens"], 6, "index: six tokens in the coverage map")
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
        st.eq(com["commit_candidates"], 6, "commits: candidate population")
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
        sys.stderr.write("environment unreadable: %s\n" % exc)
        return 2
    observed = analysis["observed"]
    print(render(analysis["repo"], analysis["head"], observed,
                 results_of(observed), args.json))
    return exit_code(observed)


if __name__ == "__main__":
    sys.exit(main())