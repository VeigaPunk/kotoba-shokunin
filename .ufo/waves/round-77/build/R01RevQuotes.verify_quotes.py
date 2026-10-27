#!/usr/bin/env python3
"""R01RevQuotes.verify_quotes.py — independent quote verifier, kotoba round-77 w1.

Verifies EVERY quotation in .ufo/waves/round-76/build/entry-draft.md and
.ufo/waves/round-76/build/quotes-s213.md against the three round-76 snapshots:

  1. literal substring of ONE physical line of optimizing-descriptions.md,
     compared after collapsing whitespace runs to single spaces ONLY
     (no case folding, no punctuation or quote-mark folding);
  2. word count (whitespace split) <= 25;
  3. occurs on a line AFTER the page's first heading (first line matching ^# );
  4. absent from evaluating-skills.md and best-practices.md (per-line, whole
     body chrome included).

Also recomputes: snapshot digests/byte/line counts vs MANIFEST.sha256 and
fetch-record.json; the JSON block inside quotes-s213.md field by field; the
nine recheck tokens of entry-draft.md's `recheck:` line (each on exactly one
line); the page-absence sweeps both drafts claim; and every
`optimizing-descriptions.md:N` line pointer either draft makes. Lane-side
quotation checks (SKILL.md description quotes, frontmatter-trigger-surface.md
quote) run against committed bytes exported by git show, passed via --skill-*.

Usage:
  python3 -B R01RevQuotes.verify_quotes.py [--out LOGFILE] \
      [--skill-base P] [--skill-head P] [--fts-head P]

Exit 0 = every REQUIRED check passed; 1 = at least one failed.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
SNAP = LANE / ".ufo/waves/round-76/snapshots"
BUILD = LANE / ".ufo/waves/round-76/build"

EXPECTED = {  # bytes, lines, sha256 — as claimed in quotes-s213.md / entry-draft.md
    "optimizing-descriptions.md": (13403, 196,
        "7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837"),
    "evaluating-skills.md": (16973, 300,
        "a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684"),
    "best-practices.md": (15060, 277,
        "ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41"),
}

# (id, source draft, quote, claimed line or None, claimed words or None)
QUOTES = [
    ("E01", "entry-draft.md",
     "An under-specified description means the skill won't trigger when it should; an over-broad description means it triggers when it shouldn't.",
     9, 20),
    ("E02", "entry-draft.md", "Frame the description as an instruction to the agent", 25, None),
    ("E03", "entry-draft.md", "Describe what the user is trying to achieve, not the skill's internal mechanics.", 26, None),
    ("E04", "entry-draft.md", "Err on the side of being pushy", 27, None),
    ("E05", "entry-draft.md", "Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly", 27, None),
    ("E06", "entry-draft.md", "A few sentences to a short paragraph is usually right", 28, None),
    ("E07", "entry-draft.md", "enforces a hard limit of 1024 characters.", 28, None),
    ("E08", "entry-draft.md", "even if they don't explicitly mention", 27, None),
    ("E09", "entry-draft.md", "typically only consult skills for tasks that require knowledge or capabilities beyond what they can handle alone", 19, None),
    ("E10", "entry-draft.md", "A few sentences to a short paragraph", 28, None),
    ("E11", "entry-draft.md", "Use imperative phrasing", 25, None),
    ("Q01", "quotes-s213.md", "Use imperative phrasing.", 25, 3),
    ("Q02", "quotes-s213.md", "Frame the description as an instruction to the agent: \"Use this skill when...\" rather than \"This skill does...\"", 25, 18),
    ("Q03", "quotes-s213.md", "Describe what the user is trying to achieve, not the skill's internal mechanics.", 26, 13),
    ("Q04", "quotes-s213.md", "Err on the side of being pushy", 27, 7),
    ("Q05", "quotes-s213.md", "Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly", 27, 17),
    ("Q06", "quotes-s213.md", "This means the description carries the entire burden of triggering.", 17, 10),
    ("Q07", "quotes-s213.md", "These test whether the description captures the skill's scope.", 45, 9),
    ("Q08", "quotes-s213.md", "If should-trigger queries are failing, the description may be too narrow. Broaden the scope or add context about when the skill is useful.", 155, 23),
    ("Q09", "quotes-s213.md", "A few sentences to a short paragraph is usually right", 28, 10),
    ("Q10", "quotes-s213.md", "long enough to cover the skill's scope, short enough that it doesn't bloat the agent's context across many skills", 28, 19),
    ("Q11", "quotes-s213.md", "enforces a hard limit of 1024 characters.", 28, 7),
    ("Q12", "quotes-s213.md", "Check that the description stays under the 1024-character limit — descriptions tend to grow during optimization.", 159, 16),
    ("Q13", "quotes-s213.md", "Avoid adding specific keywords from failed queries", 157, 7),
    ("F01", "quotes-s213.md (suggested-min fragments)", "Use imperative phrasing", None, None),
    ("F02", "quotes-s213.md (suggested-min fragments)", "captures the skill's scope", None, None),
    ("F03", "quotes-s213.md (suggested-min fragments)", "A few sentences to a short paragraph", None, None),
    ("F04", "quotes-s213.md (worked-example prose)", "Analyze CSV and tabular data files", None, None),
    ("F05", "quotes-s213.md (worked-example prose)", "Use this skill when the user has a CSV, TSV, or Excel file", None, None),
]

# entry-draft / quotes-s213 line pointers into optimizing-descriptions.md
POINTERS = [
    ("entry-draft.md", 9,  "An under-specified description means"),
    ("entry-draft.md", 13, "## How skill triggering works"),
    ("entry-draft.md", 17, "carries the entire burden of triggering"),
    ("entry-draft.md", 19, "typically only consult skills"),
    ("entry-draft.md", 21, "## Writing effective descriptions"),
    ("entry-draft.md", 25, "Use imperative phrasing"),
    ("entry-draft.md", 26, "Describe what the user is trying to achieve"),
    ("entry-draft.md", 27, "Err on the side of being pushy"),
    ("entry-draft.md", 28, "Keep it concise"),
    ("entry-draft.md", 157, "Avoid adding specific keywords from failed queries"),
    ("entry-draft.md", 159, "Check that the description stays under the 1024-character limit"),
    ("entry-draft.md", 192, "The improved description is more specific about what the skill does"),
    ("quotes-s213.md", 5,  "# Optimizing skill descriptions"),
    ("quotes-s213.md", 21, "## Writing effective descriptions"),
    ("quotes-s213.md", 43, "### Should-trigger queries"),
    ("quotes-s213.md", 45, "These test whether the description captures the skill's scope"),
    ("quotes-s213.md", 149, "## The optimization loop"),
    ("quotes-s213.md", 155, "If should-trigger queries are failing"),
    ("quotes-s213.md", 157, "Avoid adding specific keywords from failed queries"),
    ("quotes-s213.md", 159, "Check that the description stays under the 1024-character limit"),
]

RECHECK_TOKENS = [
    "under-specified description",
    "Frame the description as an instruction",
    "not the skill's internal mechanics",
    "Err on the side of being pushy",
    "doesn't name the domain directly",
    "even if they don't explicitly mention",
    "A few sentences to a short paragraph",
    "hard limit of 1024 characters",
    "typically only consult skills",
]

ABSENCE_SWEEP = ["front-load", "front load", "use case", "lead with", "starts with",
                 "first sentence", "self-contained", "self contained", "opening",
                 "single sentence", "one-sentence"]


def collapse(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fold_description(path: Path):
    """Crude YAML folded-scalar render of SKILL.md's `description:` block."""
    lines = path.read_text(encoding="utf-8").splitlines()
    key_i = next(i for i, l in enumerate(lines[:40]) if l.startswith("description:"))
    header = lines[key_i]
    block = []
    for l in lines[key_i + 1:]:
        if l.startswith("---") or (l.strip() and not l[0].isspace()):
            break
        if l.startswith((" ", "\t")) or not l.strip():
            block.append(l.strip())
    return header, " ".join(x for x in block if x != "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    ap.add_argument("--skill-base", default=None)
    ap.add_argument("--skill-head", default=None)
    ap.add_argument("--fts-head", default=None)
    args = ap.parse_args()

    out = []
    def say(s=""):
        out.append(s)

    fails = []

    def verdict(name, ok, detail):
        tag = "PASS" if ok else "FAIL"
        if not ok:
            fails.append(f"{name}: {detail}")
        say(f"  [{tag}] {name} — {detail}")

    # ---------- snapshot identity ----------
    say("## A. Snapshot identity (recomputed sha256 / bytes / lines)")
    blobs = {}
    for name, (eb, el, eh) in EXPECTED.items():
        b = (SNAP / name).read_bytes()
        t = b.decode("utf-8")
        blobs[name] = t
        h, nb, nl = sha256(b), len(b), len(t.splitlines())
        ok = (h == eh and nb == eb and nl == el)
        verdict(f"identity:{name}", ok,
                f"sha256 {'==' if h == eh else '!='} pinned, bytes {nb}/{eb}, lines {nl}/{el}")
    opt_lines = blobs["optimizing-descriptions.md"].splitlines()
    eva_lines = blobs["evaluating-skills.md"].splitlines()
    best_lines = blobs["best-practices.md"].splitlines()

    fh = next((i for i, l in enumerate(opt_lines, 1) if re.match(r"^#\s", l)), None)
    say(f"  first heading of optimizing-descriptions.md: line {fh} "
        f"{opt_lines[fh-1]!r} (quotes-s213.md claims line 5)")
    verdict("first-heading-line-5", fh == 5, f"recomputed {fh}")

    manifest = (SNAP / "MANIFEST.sha256").read_text()
    rec = json.loads((SNAP / "fetch-record.json").read_text())
    for name, (_, _, eh) in EXPECTED.items():
        m_ok = any(line.split()[0] == eh and line.split()[1].endswith(name)
                   for line in manifest.splitlines() if line.strip())
        r = next(x for x in rec if x["filename"] == name)
        verdict(f"manifest+fetch:{name}", m_ok and r["sha256"] == eh and r["http_status"] == 200,
                f"MANIFEST {'ok' if m_ok else 'MISSING'}, fetch http {r['http_status']}, digest match {r['sha256'] == eh}")

    # ---------- quotes ----------
    say()
    say("## B. Quotation checks (one-line, ws-collapsed, <=25 words, after first heading, page-unique)")
    say("  id  src                 wc  claimed_line  lines_found(after-first-heading)  chrome  eva  best  verdict")
    quote_rows = []
    for qid, src, quote, cline, cwords in QUOTES:
        q = collapse(quote)
        wc = len(quote.split())
        hits = [i for i, l in enumerate(opt_lines, 1) if q in collapse(l)]
        body = [i for i in hits if i > fh]
        chrome = [i for i in hits if i <= fh]
        in_eva = any(q in collapse(l) for l in eva_lines)
        in_best = any(q in collapse(l) for l in best_lines)
        ok = bool(body) and wc <= 25 and not in_eva and not in_best
        notes = []
        if cline is not None and cline not in hits:
            ok = False
            notes.append(f"NOT on claimed line {cline}")
        if cwords is not None and cwords != wc:
            ok = False
            notes.append(f"word count {wc} != claimed {cwords}")
        if hits and not body:
            ok = False
            notes.append("only before/at first heading (chrome)")
        d = (f"{wc:>2}  {str(cline):>12}  {str(body) if body else str(hits) or '[]':>34}  "
             f"{str(chrome):>5}  {'Y' if in_eva else '-'}    {'Y' if in_best else '-'}  "
             f"[{'PASS' if ok else 'FAIL'}] {'; '.join(notes)}")
        say(f"  {qid:<4}{src:<20}{d}")
        quote_rows.append((qid, ok))
        if not ok:
            fails.append(f"quote {qid}: fails snapshot criteria ({'; '.join(notes) or 'see row'})")

    # ---------- JSON cross-check inside quotes-s213.md ----------
    say()
    say("## C. quotes-s213.md consumable JSON cross-check (field by field, recomputed)")
    qtxt = (BUILD / "quotes-s213.md").read_text(encoding="utf-8")
    m = re.search(r"```json\s*\n(.*?)```", qtxt, re.S)
    if not m:
        verdict("json-block-present", False, "no ```json block found")
    else:
        items = json.loads(m.group(1))
        all_ok = len(items) == 13
        for it in items:
            q = collapse(it["quote"])
            wc = len(it["quote"].split())
            hits = [i for i, l in enumerate(opt_lines, 1) if q in collapse(l)]
            body = [i for i in hits if i > fh]
            chrome3 = [i for i in hits if i <= 3]
            exp = {
                "words": wc,
                "line": body[0] if len(body) == 1 else None,
                "occurrences": len(body),
                "in_evaluating": any(q in collapse(l) for l in eva_lines),
                "in_best_practices": any(q in collapse(l) for l in best_lines),
                "after_first_heading": bool(body),
                "chrome_hit": bool(chrome3),
            }
            bad = [f"{k}: claimed {it[k]!r} vs recomputed {v!r}"
                   for k, v in exp.items() if it.get(k) != v]
            if bad:
                all_ok = False
                fails.append(f"json item {it['quote'][:40]!r}: " + "; ".join(bad))
                say(f"  [FAIL] {it['quote'][:48]!r} — " + "; ".join(bad))
        verdict("json-block-13-items", len(items) == 13, f"{len(items)} items")
        if all_ok:
            verdict("json-block-fields", True, "all 13 items match recomputed words/line/occurrences/page-uniqueness/chrome")

    # ---------- recheck tokens ----------
    say()
    say("## D. entry-draft.md `recheck:` nine tokens (fixed-string, expected on exactly 1 line each)")
    for t in RECHECK_TOKENS:
        n = sum(1 for l in opt_lines if t in l)
        verdict(f"token:{t[:34]!r}", n == 1, f"{n} line(s)")

    # ---------- absence sweeps ----------
    say()
    say("## E. Page-absence sweeps the two drafts claim (case-insensitive)")
    for term in ABSENCE_SWEEP:
        rows = [i for i, l in enumerate(opt_lines, 1) if term.lower() in l.lower()]
        verdict(f"sweep-0-hits:{term!r}", not rows, f"{len(rows)} hit(s) {rows[:5]}")
    front = [i for i, l in enumerate(opt_lines, 1) if "front" in l.lower()]
    verdict("front-hits-lines-9-173", front == [9, 173], f"lines {front}")

    # ---------- pointers ----------
    say()
    say("## F. optimizing-descriptions.md:N line pointers (needle must be on that line)")
    for src, n, needle in POINTERS:
        got = collapse(opt_lines[n - 1]) if 1 <= n <= len(opt_lines) else "<out of range>"
        verdict(f"ptr {src} :{n}", needle in got, f"{needle!r} on line: {got[:96]!r}")
    say("  worked-example range entry-draft.md :184-:188 / quotes-s213.md :179-:190, :192:")
    for i in range(179, 197):
        say(f"    {i:>3}: {collapse(opt_lines[i-1])!r}")
    verdict("range-184-188-after-block",
            collapse(opt_lines[183]) == "description: >"
            and "Analyze CSV and tabular data files" in collapse(opt_lines[184])
            and "skill when" in collapse(opt_lines[186]),
            "yaml After-example opens at :184 (`description: >`), capability clause :185, "
            "imperative trigger clause second at :186-:187; value's closing line is :189 "
            "(entry's cited range :184-:188 stops one line short — informational)")

    # ---------- lane-side quotations (committed bytes, git-show exports) ----------
    say()
    say("## G. Lane-side quotations (secondary: SKILL.md at r76 base b7f13f4 / freeze tip 6523aced; "
        "frontmatter-trigger-surface.md at tip)")
    skill_paths = [p for p in (args.skill_base, args.skill_head) if p]
    renders = []
    for p in skill_paths:
        path = Path(p)
        header, render = fold_description(path)
        renders.append((path, render))
        clip = len(render) + 1  # clip-preserving: terminal newline kept
        stripped = len(render)
        idx = render.find(". ")
        sent = render[:idx + 1] if idx >= 0 else render
        say(f"  {path.name} ({path}): description block render len clip={clip} stripped={stripped} "
            f"(entry claims 1022/1021 at b7f13f4); first sentence len={len(sent)} (claim 151); "
            f"key line: {header!r}")
        say(f"    render head: {render[:150]!r}")

    # ---------- L01 quote-fidelity: entry quotes sentence 1 WITH backticks ----------
    say()
    say("## F2. entry-draft.md sentence-1 quote fidelity vs committed description bytes")
    bt = "Prompt & skill craft — audits, writes, and rewrites `SKILL.md` / `AGENTS.md` / dispatch prompts / system prompts"
    nobt = "Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts"
    for label, frag in [("as-written (with backticks)", bt), ("no-backtick form", nobt)]:
        in_renders = [collapse(frag) in collapse(r) for _, r in renders]
        same = len({collapse(r) for _, r in renders}) == 1 if renders else False
        verdict(f"L01 {label}", all(in_renders) and bool(renders) and same,
                f"in {sum(in_renders)}/{len(renders)} exported renders (b7f13f4 vs 6523aced identical={same})")

    for label, frag in [
        ("L02 sentence-7 (entry: cheapest cut)",
         "Note: shokunin files sit outside the omp discovery roots, so omp never reads this text."),
    ]:
        oks = [collapse(frag) in collapse(r) for _, r in renders]
        same = len({collapse(r) for _, r in renders}) == 1 if renders else False
        verdict(label, all(oks) and bool(renders) and same,
                f"found in {sum(oks)}/{len(renders)} exported SKILL.md bytes, renders identical={same}")
    if args.fts_head:
        ftxt = Path(args.fts_head).read_text(encoding="utf-8")
        frag = "`description` craft is audit-hygiene, not routing surface"
        cq = collapse(ftxt)
        hit = collapse(frag) in cq
        loc = [i for i, l in enumerate(ftxt.splitlines(), 1) if "audit-hygiene" in l]
        verdict("L03 frontmatter-trigger-surface.md:153-:154", hit,
                f"ws-collapsed substring found={hit}, 'audit-hygiene' on line(s) {loc} (entry cites :153-:154)")

    say()
    say(f"## SUMMARY: {len(QUOTES)} quotes checked, "
        f"{sum(1 for _, ok in quote_rows if ok)} PASS / {sum(1 for _, ok in quote_rows if not ok)} FAIL; "
        f"{len(fails)} required check(s) failed overall")

    report = "\n".join(out) + "\n"
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"log written: {args.out}")
    print(report)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
