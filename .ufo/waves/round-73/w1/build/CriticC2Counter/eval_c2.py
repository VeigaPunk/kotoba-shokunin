#!/usr/bin/env python3
"""CriticC2Counter — literal implementation of the frozen C2 predicate
(plans/round-73-addendum-1.md, "Frozen predicate"), plus a simulation of the
documented omp truncator (corpus/knowledge/render-mechanism-round7.md:14-24).

R1: first sentence = text before the first `. `/`: ` followed by an uppercase
    letter, else the first 99 characters; 40 <= len <= 99.
R2: first 99 chars contain the whole words `skill` and `prompt` and at least
    one double-quoted string that is a member of the `Triggers:` list of D.
R3: len(D) <= 1024 and check_sibling_census (tree gate) exits 0 -- evaluated
    separately by run_r3.sh because it needs the fleet-shaped sandbox.

Truncator (documented JS):
    t = ws-collapse(description); if len(t) <= 100 return t;
    s = t.slice(0,99); o = s.match(/^.*?[.!?](?=\s|$)/);
    if o and len(o) >= 40: return o; else cut s at last ASCII space + U+2026.
"""
import re
import sys
import subprocess

BASE = "072048fa8e8a52c707d25f7079772fa317244eb7"


def base_description():
    raw = subprocess.check_output(
        ["git", "-C", "/home/vgpnk/Projects/shokunin/kotoba-shokunin",
         "show", "%s:SKILL.md" % BASE], text=True)
    lines = raw.split("\n")
    i = next(k for k, l in enumerate(lines) if l.startswith("description:"))
    body = []
    for l in lines[i + 1:]:
        if l and not l[0].isspace():
            break
        body.append(l)
    return " ".join(" ".join(body).split())


def r1(D):
    m = re.search(r"[.:] (?=[A-Z])", D)
    fs = D[:m.start()] if m else D[:99]
    return m.start() if m else None, fs, 40 <= len(fs) <= 99


def triggers(D):
    m = re.search(r"Triggers:(.*?)(?:Anti-triggers:|\Z)", D, re.S)
    return set(re.findall(r'"([^"]*)"', m.group(1))) if m else set()


def r2(D):
    w = D[:99]
    words = all(re.search(r'(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])' % x, w, re.I)
                for x in ("skill", "prompt"))
    quotes = re.findall(r'"([^"]*)"', w)
    hits = [q for q in quotes if q in triggers(D)]
    return words, quotes, hits, bool(words and hits)


def render(D):
    if len(D) <= 100:
        return D
    s = D[:99]
    m = re.search(r"^.*?[.!?](?=\s|$)", s)
    if m and len(m.group(0)) >= 40:
        return m.group(0)
    cut = s.rsplit(" ", 1)[0]
    return cut + "\u2026"


def show(name, D):
    b, fs, ok1 = r1(D)
    words, quotes, hits, ok2 = r2(D)
    print("%-18s len=%4d  R1=%s (boundary=%s fslen=%3d)  R2=%s (quotes_in_99=%s hits=%s)  len<=1024=%s"
          % (name, len(D), "PASS" if ok1 else "FAIL", b, len(fs), "PASS" if ok2 else "FAIL",
             quotes, hits, len(D) <= 1024))
    print("%-18s fs : %r" % ("", fs))
    print("%-18s render(%d): %r" % ("", len(render(D)), render(D)))
    print("%-18s render has quoted trigger: %s" % ("", bool(re.findall(r'"([^"]*)"', render(D)))))
    print()


def main():
    D = base_description()
    print("base folded D: len=%d" % len(D))
    show("BASE", D)
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            with open(path) as f:
                show(path.rsplit("/", 1)[-1], f.read().rstrip("\n"))


if __name__ == "__main__":
    main()
