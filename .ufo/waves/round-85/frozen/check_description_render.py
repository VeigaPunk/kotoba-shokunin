#!/usr/bin/env python3
"""check_description_render.py -- round-85 C1 counter (kotoba-shokunin).

Scores the SKILL.md frontmatter `description` against eight render rules,
R1..R8 (plan round-85 section C1), from committed bytes read through
read-only `git show`:

  SKILL.md                                          R1-R4, R7 and R5's --skill
  corpus/knowledge/sibling-overlap-census-round74.md,
  PROVINCE.md, verifiers/check_sibling_census.py    R5 (run as a subprocess)
  verifiers/fixtures/description-eval-round85.tsv   R6 (or --eval PATH, from disk)
  corpus/knowledge/description-trigger-discipline-round85.md   R8

Output: one line per rule, `R<k> <label>: ok|fail <detail>`, then the summary
`description render rules met N of 8`.  Exit 0 iff N == 8; 1 when the content
fails; 2 for an environment or usage error (unreadable repo, missing git,
unknown revision, unreadable --eval file, the census could not run).

--rev defaults to HEAD; --repo defaults to the checkout holding this script.
--json prints the same result as one JSON object.
--self-test builds throwaway git worlds under TMPDIR and asserts the controls
and one red arm per rule.

Usage:
  python3 -B verifiers/check_description_render.py [--rev REV] [--repo DIR]
      [--eval PATH] [--json]
  python3 -B verifiers/check_description_render.py --self-test
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
FIXTURES = LANE / "verifiers" / "fixtures" / "description-render"
BASE_REV = "1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b"

SKILL = "SKILL.md"
PROVINCE = "PROVINCE.md"
CENSUS_SCRIPT = "verifiers/check_sibling_census.py"
CENSUS_MD = "corpus/knowledge/sibling-overlap-census-round74.md"
EVAL_REL = "verifiers/fixtures/description-eval-round85.tsv"
KB_REL = "corpus/knowledge/description-trigger-discipline-round85.md"

RULES = (
    ("R1", "first_sentence_le_99"),
    ("R2", "prefix_carries_triggers"),
    ("R3", "spec_max_1024"),
    ("R4", "imperative_invocation"),
    ("R5", "sibling_clauses"),
    ("R6", "eval_set_shape"),
    ("R7", "no_xml_tag"),
    ("R8", "sourced_entry"),
)
LABELS = dict(RULES)
TARGET = len(RULES)

FIRST_SENTENCE_MAX = 99
PREFIX_CHARS = 99
SPEC_MIN = 1
SPEC_MAX = 1024
CENSUS_LINE = "skill description names 10 of 10 non-none lanes"
EVAL_HEADER = "label\tquery"
EVAL_LABELS = ("should-trigger", "should-not-trigger")
EVAL_ROWS_MIN = 8
EVAL_ROWS_MAX = 10
INDIRECT_MIN = 5
WORD_MIN = 4
KB_SOURCE = "S213"
KB_VERIFIED = "2026-11-04"
QUOTE_WORDS_MIN = 3
QUOTE_WORDS_MAX = 25

WS_RUN = re.compile(r"\s+")
BLOCK_SCALAR = re.compile(r"\A[>|][+-]?\s*")
SENTENCE_END = re.compile(r"\.(?=\s|\Z)")
QUOTE = re.compile(r'"([^"\n]+)"|\u201c([^\u201d\n]+)\u201d')


class EnvError(Exception):
    """The instrument cannot evaluate at all (exit 2)."""


# --------------------------------------------------------------------------
# committed bytes
# --------------------------------------------------------------------------

def first_line(data):
    text = data.decode("utf-8", "replace") if isinstance(data, bytes) else (data or "")
    lines = text.strip().splitlines()
    return lines[0] if lines else "(no diagnostic)"


def text_of(data):
    return data.decode("utf-8", "replace")


def git(repo, *args):
    """Read-only git in REPO.  A missing git raises OSError (exit 2 upstream)."""
    return subprocess.run(["git", "-C", str(repo), *args],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def check_checkout(repo):
    if not (repo / ".git").exists():
        raise EnvError("%s is not a git checkout" % repo)


def resolve_rev(repo, rev):
    proc = git(repo, "rev-parse", "--verify", "--quiet", rev + "^{commit}")
    if proc.returncode != 0:
        raise EnvError("revision %r is not a commit in %s" % (rev, repo))
    return proc.stdout.decode("utf-8").strip()


def rev_bytes(repo, rev, path):
    """Committed bytes of PATH at REV, or None when PATH is not a blob there."""
    spec = "%s:%s" % (rev, path)
    kind = git(repo, "cat-file", "-t", spec)
    if kind.returncode != 0 or kind.stdout.decode("utf-8").strip() != "blob":
        return None
    proc = git(repo, "show", spec)
    if proc.returncode != 0:
        raise EnvError("git show %s failed: %s" % (spec, first_line(proc.stderr)))
    return proc.stdout


def read_disk(path):
    try:
        return Path(path).read_bytes()
    except OSError as exc:
        raise EnvError("cannot read --eval %s: %s" % (path, exc.strerror or exc))


# --------------------------------------------------------------------------
# parsing
# --------------------------------------------------------------------------

def collapse(text):
    return WS_RUN.sub(" ", text).strip()


def description_of(skill_text):
    """The frontmatter `description`, as check_sibling_census.description_of:
    whitespace-collapsed, block-scalar indicator dropped, the value ends at
    any column-0 line.  '' when there is none."""
    if skill_text is None or not skill_text.startswith("---"):
        return ""
    front = skill_text.split("\n---", 1)[0]
    match = re.search(r"^description:(.*?)(?=^\S|\Z)", front, re.S | re.M)
    if not match:
        return ""
    return BLOCK_SCALAR.sub("", collapse(match.group(1))).strip()


def first_sentence(desc):
    """Text up to and including the first dot followed by a space or the end."""
    match = SENTENCE_END.search(desc)
    return desc[: match.end()] if match else desc


def trigger_terms(desc):
    """The quoted strings of the `Triggers:` clause, lower-cased.  The clause
    ends at the first dot outside quotes that is followed by a space or the
    end, so `SKILL.md` inside a quote does not end it."""
    idx = desc.find("Triggers:")
    if idx < 0:
        return []
    tail = desc[idx + len("Triggers:"):]
    end = len(tail)
    in_quote = False
    for i, ch in enumerate(tail):
        if ch == '"':
            in_quote = not in_quote
        elif ch == "." and not in_quote and (i + 1 == len(tail) or tail[i + 1] == " "):
            end = i
            break
    return [t.strip().lower() for t in re.findall(r'"([^"]+)"', tail[:end])
            if t.strip()]


def words_of(text):
    """Lower-cased alphanumeric words of WORD_MIN characters or more."""
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) >= WORD_MIN}


def parse_eval(text):
    """Rows (label, query) of the eval TSV, and the list of format errors."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    errors = []
    if not lines or lines[0] != EVAL_HEADER:
        errors.append("header is not exactly 'label<TAB>query'")
    rows = []
    for number, line in enumerate(lines[1:], 2):
        fields = line.split("\t")
        if len(fields) != 2:
            errors.append("line %d: %d tab-separated field(s), want 2"
                          % (number, len(fields)))
        elif fields[0] not in EVAL_LABELS:
            errors.append("line %d: label %r is not one of %s"
                          % (number, fields[0], "/".join(EVAL_LABELS)))
        elif not fields[1].strip():
            errors.append("line %d: empty query" % number)
        else:
            rows.append((fields[0], fields[1]))
    return rows, errors


def yn(flag):
    return "yes" if flag else "no"


# --------------------------------------------------------------------------
# the eight rules; each returns (ok, detail)
# --------------------------------------------------------------------------

def rule_r1(desc):
    if not desc:
        return False, "no description"
    n = len(first_sentence(desc))
    return n <= FIRST_SENTENCE_MAX, "first sentence %d chars (cap %d)" % (n, FIRST_SENTENCE_MAX)


def rule_r2(desc):
    prefix = desc[:PREFIX_CHARS].lower()
    has_skill = "skill" in prefix
    has_second = "prompt" in prefix or "skill.md" in prefix
    ok = has_skill and has_second
    return ok, ("first %d chars: 'skill' %s, 'prompt' or 'SKILL.md' %s"
                % (min(len(desc), PREFIX_CHARS), yn(has_skill), yn(has_second)))


def rule_r3(desc):
    n = len(desc)
    return (SPEC_MIN <= n <= SPEC_MAX,
            "description %d chars (%d-%d)" % (n, SPEC_MIN, SPEC_MAX))


def rule_r4(desc):
    invoke = "use this skill when" in desc.lower()
    triggers = "Triggers:" in desc
    return (invoke and triggers,
            "'use this skill when' %s, literal 'Triggers:' %s"
            % (yn(invoke), yn(triggers)))


def rule_r5(files):
    if files[SKILL] is None:
        return False, "SKILL.md absent at rev"
    absent = [p for p in (CENSUS_SCRIPT, CENSUS_MD, PROVINCE) if files[p] is None]
    if absent:
        return False, "absent at rev: %s" % ", ".join(absent)
    staged = ((CENSUS_SCRIPT, files[CENSUS_SCRIPT]), (CENSUS_MD, files[CENSUS_MD]),
              (PROVINCE, files[PROVINCE]), (SKILL, files[SKILL]))
    with tempfile.TemporaryDirectory(prefix="description-render-r5-") as tmp:
        root = Path(tmp)
        for rel, data in staged:
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        proc = subprocess.run(
            [sys.executable, "-B", str(root / CENSUS_SCRIPT), str(root / CENSUS_MD),
             "--province", str(root / PROVINCE), "--skill", str(root / SKILL)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode == 2:
        raise EnvError("census could not run: %s" % first_line(proc.stderr))
    out = proc.stdout.decode("utf-8", "replace").splitlines()
    if proc.returncode == 0 and CENSUS_LINE in out:
        return True, "census exit 0, '%s'" % CENSUS_LINE
    detail = "census exit %d" % proc.returncode
    named = [line for line in out if line.startswith("skill description names")]
    if named:
        detail += "; " + named[0]
    failures = [line for line in out if line.startswith("FAIL ")]
    if failures:
        detail += "; " + failures[0][:160]
    return False, detail


def rule_r6(desc, eval_text, eval_label):
    if eval_text is None:
        return False, "eval set absent: %s" % eval_label
    rows, errors = parse_eval(eval_text)
    if errors:
        return False, "%d malformed line(s); first: %s" % (len(errors), errors[0])
    counts = {label: sum(1 for lab, _ in rows if lab == label) for label in EVAL_LABELS}
    for label in EVAL_LABELS:
        if not EVAL_ROWS_MIN <= counts[label] <= EVAL_ROWS_MAX:
            return False, ("%s has %d rows, want %d-%d"
                           % (label, counts[label], EVAL_ROWS_MIN, EVAL_ROWS_MAX))
    terms = trigger_terms(desc)
    if not terms:
        return False, "description declares no quoted terms in its Triggers clause"
    indirect = sum(1 for label, query in rows
                   if label == "should-trigger"
                   and not any(t in query.lower() for t in terms))
    if indirect < INDIRECT_MIN:
        return False, "%d indirect should-trigger row(s), want >= %d" % (indirect, INDIRECT_MIN)
    words = words_of(desc)
    near = [query for label, query in rows
            if label == "should-not-trigger" and not (words_of(query) & words)]
    if near:
        return False, ("%d should-not-trigger row(s) share no word of >=%d chars with "
                       "the description; first: %r" % (len(near), WORD_MIN, near[0][:60]))
    return True, ("should-trigger %d (indirect %d), should-not-trigger %d, "
                  "%d trigger term(s)" % (counts["should-trigger"], indirect,
                                          counts["should-not-trigger"], len(terms)))


def rule_r7(desc):
    if not desc:
        return False, "no description"
    bad = sorted(set(re.findall(r"[<>]", desc)))
    if bad:
        return False, "found %s" % " ".join(bad)
    return True, "no '<' or '>'"


def rule_r8(kb_text):
    if kb_text is None:
        return False, "absent at rev: %s" % KB_REL
    lines = kb_text.splitlines()
    problems = []
    if not any(line.startswith("source:") and re.search(r"\b%s\b" % KB_SOURCE, line)
               for line in lines):
        problems.append("no 'source:' line naming %s" % KB_SOURCE)
    if not any(re.match(r"verified-at:\s*%s(?!\d)" % re.escape(KB_VERIFIED), line)
               for line in lines):
        problems.append("no 'verified-at: %s' line" % KB_VERIFIED)
    if not any(re.match(r"recheck:\s*\S", line) for line in lines):
        problems.append("no 'recheck:' line with a value")
    quotes = [a or b for a, b in QUOTE.findall(kb_text)]
    sized = [q for q in quotes
             if QUOTE_WORDS_MIN <= len(q.split()) <= QUOTE_WORDS_MAX]
    if not sized:
        problems.append("no located quote of %d-%d words"
                        % (QUOTE_WORDS_MIN, QUOTE_WORDS_MAX))
    if problems:
        return False, "; ".join(problems)
    return True, ("source %s, verified-at %s, recheck present, %d quote(s) in range"
                  % (KB_SOURCE, KB_VERIFIED, len(sized)))


# --------------------------------------------------------------------------
# evaluation and output
# --------------------------------------------------------------------------

def evaluate(repo, rev, eval_path=None):
    """Score REV of REPO.  EVAL_PATH, when given, replaces the committed eval
    TSV with the file on disk (the R6 input only)."""
    repo = Path(repo)
    check_checkout(repo)
    sha = resolve_rev(repo, rev)
    paths = (SKILL, CENSUS_SCRIPT, CENSUS_MD, PROVINCE, KB_REL, EVAL_REL)
    files = {p: rev_bytes(repo, sha, p) for p in paths}
    eval_bytes = read_disk(eval_path) if eval_path is not None else files[EVAL_REL]
    eval_label = eval_path if eval_path is not None else EVAL_REL
    skill_text = text_of(files[SKILL]) if files[SKILL] is not None else None
    desc = description_of(skill_text)
    eval_text = text_of(eval_bytes) if eval_bytes is not None else None
    kb_text = text_of(files[KB_REL]) if files[KB_REL] is not None else None

    checks = (
        ("R1", rule_r1(desc)),
        ("R2", rule_r2(desc)),
        ("R3", rule_r3(desc)),
        ("R4", rule_r4(desc)),
        ("R5", rule_r5(files)),
        ("R6", rule_r6(desc, eval_text, eval_label)),
        ("R7", rule_r7(desc)),
        ("R8", rule_r8(kb_text)),
    )
    rules = [{"id": rid, "label": LABELS[rid], "ok": bool(ok), "detail": detail}
             for rid, (ok, detail) in checks]
    met = sum(1 for rule in rules if rule["ok"])
    return {"rev": sha, "repo": str(repo), "rules": rules, "met": met, "of": TARGET}


def render(result):
    lines = ["%s %s: %s %s" % (r["id"], r["label"], "ok" if r["ok"] else "fail",
                              r["detail"]) for r in result["rules"]]
    lines.append("description render rules met %d of %d"
                 % (result["met"], result["of"]))
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Score the SKILL.md description against the eight render "
                    "rules R1-R8 (round-85 C1) at a committed revision.")
    ap.add_argument("--rev", default=None, metavar="REV",
                    help="revision to score (default HEAD)")
    ap.add_argument("--repo", default=None, metavar="DIR",
                    help="checkout the revision is read from (default: the "
                         "checkout holding this script)")
    ap.add_argument("--eval", dest="eval_path", default=None, metavar="PATH",
                    help="read the R6 eval TSV from PATH instead of the revision")
    ap.add_argument("--json", action="store_true",
                    help="print the result as one JSON object")
    ap.add_argument("--self-test", action="store_true",
                    help="build throwaway worlds and assert the controls and arms")
    args = ap.parse_args(argv)

    if args.self_test and (args.rev or args.repo or args.eval_path or args.json):
        ap.error("--self-test cannot be combined with --rev, --repo, --eval or --json")

    try:
        if args.self_test:
            return self_test()
        repo = Path(args.repo).expanduser().resolve() if args.repo else LANE
        result = evaluate(repo, args.rev or "HEAD", args.eval_path)
    except EnvError as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2
    except OSError as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for line in render(result):
            print(line)
    return 0 if result["met"] == TARGET else 1


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

def _sgit(repo, *args):
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "kotoba self-test",
                "GIT_AUTHOR_EMAIL": "self-test@example.invalid",
                "GIT_COMMITTER_NAME": "kotoba self-test",
                "GIT_COMMITTER_EMAIL": "self-test@example.invalid"})
    proc = subprocess.run(["git", "-C", str(repo), *args],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if proc.returncode != 0:
        raise RuntimeError("git %s failed: %s"
                           % (" ".join(args), first_line(proc.stderr)))
    return proc.stdout.decode("utf-8", "replace")


def _world(root, name, files):
    """A throwaway git repo holding FILES, committed once.  The toplevel is
    asserted before anything else is written into it."""
    repo = root / name
    repo.mkdir(parents=True)
    _sgit(repo, "init", "-q", "-b", "main")
    top = Path(_sgit(repo, "rev-parse", "--show-toplevel").strip())
    if top.resolve() != repo.resolve():
        raise RuntimeError("fixture %s resolves to %s" % (repo, top))
    _sgit(repo, "config", "user.name", "kotoba self-test")
    _sgit(repo, "config", "user.email", "self-test@example.invalid")
    _sgit(repo, "config", "commit.gpgsign", "false")
    for rel, data in files.items():
        target = repo / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    _sgit(repo, "add", "-A")
    _sgit(repo, "commit", "-q", "-m", "fixture")
    return repo


def _fixture(name):
    return (FIXTURES / name).read_bytes()


def _lane_bytes(rel):
    return (LANE / rel).read_bytes()


def _skill(desc):
    return ("---\nname: kotoba-shokunin\ndescription: >\n  %s\n---\n\n"
            "# kotoba-shokunin\n" % desc).encode("utf-8")


def _world_with(tmp, name, skill, eval_bytes, kb_bytes):
    files = {CENSUS_SCRIPT: _lane_bytes(CENSUS_SCRIPT),
             CENSUS_MD: _lane_bytes(CENSUS_MD),
             PROVINCE: _lane_bytes(PROVINCE)}
    if skill is not None:
        files[SKILL] = skill
    if eval_bytes is not None:
        files[EVAL_REL] = eval_bytes
    if kb_bytes is not None:
        files[KB_REL] = kb_bytes
    return _world(tmp, name, files)


def _run_main(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


FIRST_100 = ("Use this skill when auditing or rewriting a skill file or prompt "
             "for trigger fidelity and decisions.")
WIDE_FIRST = "Use this when auditing a markdown loader contract for trigger fidelity."
ROUTING_TAIL = ("Routing discipline and decision density apply to every markdown "
                "file that routes agents to work.")
SIBLING_SENTENCE = ("Sibling boundary: kagi, kake, kasegi, kengaku and kumitate own "
                    "their own SKILL.md content \u2014 this skill audits and reports; "
                    "fixes route to the owning lane.")


def self_test():
    failures = []
    total = 0

    def rec(what, ok, got=None):
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (what, got))

    def rule(result, rid):
        return next(r for r in result["rules"] if r["id"] == rid)

    def red(result, rid):
        return not rule(result, rid)["ok"]

    # pure parsing
    rec("description_of folds the block scalar",
        description_of("---\nname: x\ndescription: >\n  Alpha beta.\n  Gamma delta.\n---\n")
        == "Alpha beta. Gamma delta.")
    rec("description_of stops at a column-0 comment",
        description_of("---\ndescription: >\n  A b.\n# comment here\n---\n") == "A b.")
    rec("description_of empty without frontmatter",
        description_of("# no frontmatter\n") == "")
    rec("first_sentence stops at dot-space",
        first_sentence("Use this. Then more") == "Use this.")
    rec("first_sentence keeps a dot inside SKILL.md",
        first_sentence("Edit SKILL.md now") == "Edit SKILL.md now")
    rec("parse_eval rejects a bad header", parse_eval("label query\n")[1] != [])
    rec("FIRST_100 is exactly 100 characters", len(FIRST_100) == 100, len(FIRST_100))

    cand_skill = _fixture("candidate-SKILL.md")
    cand_eval = _fixture("candidate-eval.tsv")
    cand_kb = _fixture("candidate-knowledge.md")
    cand = description_of(text_of(cand_skill))
    rec("candidate first sentence is the plan's sentence",
        first_sentence(cand) == "Use this skill when auditing or rewriting a skill file or prompt.")
    rec("candidate trigger terms are the eight quoted strings",
        trigger_terms(cand) == ["skill file", "skill.md", "frontmatter description",
                                "trigger words", "prompt craft", "write a skill",
                                "audit this skill", "skill quality"],
        trigger_terms(cand))

    base_skill = rev_bytes(LANE, BASE_REV, SKILL)
    rec("base SKILL.md readable at the base commit", base_skill is not None)
    base_desc = description_of(text_of(base_skill)) if base_skill is not None else ""

    with tempfile.TemporaryDirectory(prefix="description-render-selftest-") as tmp_name:
        tmp = Path(tmp_name)

        def score(name, skill, eval_bytes, kb_bytes):
            return evaluate(_world_with(tmp, name, skill, eval_bytes, kb_bytes), "HEAD")

        # perfect fixture world: the candidate bytes on every input
        perfect = score("perfect", cand_skill, cand_eval, cand_kb)
        rec("perfect fixture world reads 8 of 8", perfect["met"] == 8,
            [(r["id"], r["detail"]) for r in perfect["rules"] if not r["ok"]])

        # eval override reads the file on disk instead of the revision
        no_eval = score("no-eval", cand_skill, None, cand_kb)
        rec("missing eval set: R6 red", red(no_eval, "R6"), rule(no_eval, "R6")["detail"])
        rec("missing eval set: 7 of 8", no_eval["met"] == 7, no_eval["met"])
        overridden = evaluate(no_eval and _world_with(tmp, "no-eval-override",
                                                      cand_skill, None, cand_kb),
                              "HEAD", eval_path=str(FIXTURES / "candidate-eval.tsv"))
        rec("--eval PATH supplies R6 when the revision has none",
            not red(overridden, "R6"), rule(overridden, "R6")["detail"])

        # naive 99-char cut of the base description (control W1)
        naive = score("naive-cut", _skill(base_desc[:99]), cand_eval, cand_kb)
        rec("W1 naive 99-char cut reads below 8", naive["met"] < 8, naive["met"])
        rec("W1 naive cut: R4 red", red(naive, "R4"), rule(naive, "R4")["detail"])

        # token dump (control W2): trigger list plus bare lane names
        terms = trigger_terms(cand)
        token_desc = ("Triggers: " + ", ".join('"%s"' % t for t in terms)
                      + ". chousa kagi kake kama kasegi kengaku kotodama kumitate tameshi.")
        dump = score("token-dump", _skill(token_desc), cand_eval, cand_kb)
        rec("W2 token dump reads below 8", dump["met"] < 8, dump["met"])
        rec("W2 token dump: R5 red", red(dump, "R5"), rule(dump, "R5")["detail"])

        # one red arm per rule
        first = first_sentence(cand)
        arm_r1 = cand.replace(first, FIRST_100, 1)
        rec("R1 arm applied", arm_r1 != cand)
        res = score("arm-r1", _skill(arm_r1), cand_eval, cand_kb)
        rec("R1 arm: R1 red", red(res, "R1"), rule(res, "R1")["detail"])

        arm_r2 = cand.replace(first, WIDE_FIRST + " " + ROUTING_TAIL + " " + first, 1)
        rec("R2 arm applied", arm_r2 != cand)
        rec("R2 arm: first 99 chars carry no 'skill' or 'prompt'",
            "skill" not in arm_r2[:99].lower() and "prompt" not in arm_r2[:99].lower(),
            arm_r2[:99])
        res = score("arm-r2", _skill(arm_r2), cand_eval, cand_kb)
        rec("R2 arm: R2 red", red(res, "R2"), rule(res, "R2")["detail"])

        arm_r3 = cand + " " + " ".join(["Routes stay with the owning lane."] * 35)
        res = score("arm-r3", _skill(arm_r3), cand_eval, cand_kb)
        rec("R3 arm: longer than 1024", len(arm_r3) > 1024, len(arm_r3))
        rec("R3 arm: R3 red", red(res, "R3"), rule(res, "R3")["detail"])

        arm_r4 = cand.replace("Use this skill when", "This skill applies when", 1)
        rec("R4 arm applied", arm_r4 != cand)
        res = score("arm-r4", _skill(arm_r4), cand_eval, cand_kb)
        rec("R4 arm: R4 red", red(res, "R4"), rule(res, "R4")["detail"])

        arm_r5 = cand.replace(SIBLING_SENTENCE, "", 1)
        rec("R5 arm applied", arm_r5 != cand)
        res = score("arm-r5", _skill(arm_r5), cand_eval, cand_kb)
        rec("R5 arm: sibling clause lost, R5 red", red(res, "R5"),
            rule(res, "R5")["detail"])

        lines = cand_eval.decode("utf-8").split("\n")
        kept, dropped = [], 0
        for line in lines:
            if line.startswith("should-trigger\t") and dropped < 2:
                dropped += 1
                continue
            kept.append(line)
        rec("R6 arm: two should-trigger rows removed", dropped == 2, dropped)
        res = score("arm-r6", cand_skill, "\n".join(kept).encode("utf-8"), cand_kb)
        rec("R6 arm: R6 red", red(res, "R6"), rule(res, "R6")["detail"])

        arm_r7 = cand.replace("Sibling boundary:", "Sibling <boundary>:", 1)
        rec("R7 arm applied", arm_r7 != cand)
        res = score("arm-r7", _skill(arm_r7), cand_eval, cand_kb)
        rec("R7 arm: R7 red", red(res, "R7"), rule(res, "R7")["detail"])

        kb_lines = cand_kb.decode("utf-8").splitlines()
        kb_arm = "\n".join(l for l in kb_lines if not l.startswith("recheck:")).encode("utf-8")
        rec("R8 arm applied", kb_arm != cand_kb)
        res = score("arm-r8", cand_skill, cand_eval, kb_arm)
        rec("R8 arm: R8 red", red(res, "R8"), rule(res, "R8")["detail"])

        # the base commit itself (control W0): four of eight
        base = evaluate(LANE, BASE_REV)
        reds = {r["id"] for r in base["rules"] if not r["ok"]}
        rec("W0 base commit reads 4 of 8 with R1, R4, R6, R8 red",
            reds == {"R1", "R4", "R6", "R8"} and base["met"] == 4,
            (base["met"], sorted(reds)))

        # exit ladder
        code, out, _ = _run_main(["--repo", str(tmp / "perfect")])
        rec("cli: perfect world exits 0", code == 0, code)
        rec("cli: perfect world prints the summary",
            out.strip().splitlines()[-1] == "description render rules met 8 of 8", out)
        code, _, _ = _run_main(["--repo", str(tmp / "naive-cut")])
        rec("cli: naive cut exits 1 (content)", code == 1, code)
        code, out, _ = _run_main(["--repo", str(tmp / "perfect"), "--json"])
        rec("cli: --json is one object with met 8",
            code == 0 and json.loads(out)["met"] == 8, (code, out[:80]))
        code, _, _ = _run_main(["--repo", str(tmp / "not-a-checkout")])
        rec("cli: non-checkout exits 2", code == 2, code)
        code, _, _ = _run_main(["--repo", str(tmp / "perfect"), "--rev", "0" * 40])
        rec("cli: unknown revision exits 2", code == 2, code)
        code, _, _ = _run_main(["--repo", str(tmp / "perfect"),
                                "--eval", str(tmp / "missing.tsv")])
        rec("cli: unreadable --eval exits 2", code == 2, code)

    for line in failures:
        print("FAIL " + line)
    print("%d failure(s) over %d assertions" % (len(failures), total))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
