#!/usr/bin/env python3
"""own-reading.py — the C1 conjuncts re-read independently, for calibrating the
shortcut worlds of plans/round-73.md § C1.

This is NOT the claim counter. The claim counter is
``verifiers/check_cn_vendor_surfaces.py`` (drafted this wave by ExecCnCounter).
This file exists so the shortcut worlds can say which conjunct they are meant to
break, measured by one reader that is not the counter under test. When the two
readers disagree, the counter is right until the plan says otherwise.

Literal reading implemented here (no clock, no network, committed bytes only):

  (a) the entry at the frozen path opens with ``source:`` lines for every cited
      id, then ``verified-at:`` and ``recheck:``; exactly one vendor-table row
      for V; that row carries at least three backticked tokens, at least one of
      them a root/placement token (contains ``/`` or starts ``.``/``~``), at
      least two of them frontmatter key tokens; every token occurs
      word-bounded in the committed page snapshot of a source the row cites;
  (b) every cited id is exactly one 11-cell registry row with status ``mined``,
      tier ``A``/``B``, and a used-by cell naming the frozen entry;
  (c) that row's snapshot under ``.ufo/waves/round-73/snapshots/`` hashes to the
      pin in the committed ``MANIFEST.sha256`` (missing/tampered -> exit 2);
  (d) the row's located quote (5-25 words) is found in that snapshot after
      whitespace collapse.

Usage:
  python3 -B own-reading.py --repo <git worktree> --rev <rev>
exit 0 iff backed 4 of 4; 1 otherwise; 2 when an input cannot be read.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys

ENTRY = "corpus/knowledge/chinese-vendor-skill-surfaces-round73.md"
SOURCES = "corpus/SOURCES.md"
SNAPDIR = ".ufo/waves/round-73/snapshots"
BASE_REV = "072048fa8e8a52c707d25f7079772fa317244eb7"
VENDORS = ("TRAE", "CodeBuddy", "Kimi Code", "Zhipu")
HOSTS = {
    "TRAE": ("docs.trae.cn",),
    "CodeBuddy": ("www.codebuddy.ai",),
    "Kimi Code": ("github.com/moonshotai/kimi-cli", "www.kimi.com"),
    "Zhipu": ("docs.bigmodel.cn",),
}
SID_RE = re.compile(r"\bS\d{3,}\b")
TOKEN_RE = re.compile(r"`([^`\n]+)`")
LOCATED_RE = re.compile(r'located quote\s+"([^"]+)"')
URL_RE = re.compile(r"https?://[^\s|]+")
KEY_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]*")


class EnvError(Exception):
    pass


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", t.replace("*", "").replace("`", "")).strip()


def rendered(t: str) -> str:
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    out, fence = [], False
    for line in t.splitlines():
        if re.match(r"^\s*```", line):
            fence = not fence
            continue
        if not fence:
            out.append(line)
    return "\n".join(out)


def word_bounded(needle: str, hay: str) -> bool:
    return re.search(r"(?<![\w])" + re.escape(needle) + r"(?![\w])", hay) is not None


def cells(line: str) -> list[str]:
    parts = line.split("|")
    if parts and not parts[0].strip():
        parts = parts[1:]
    if parts and not parts[-1].strip():
        parts = parts[:-1]
    return [c.strip() for c in parts]


def show(repo: str, rev: str, path: str) -> str | None:
    p = subprocess.run(["git", "-C", repo, "show", f"{rev}:{path}"],
                       capture_output=True)
    return p.stdout.decode("utf-8", "replace") if p.returncode == 0 else None


def entry_head(text: str):
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    src = []
    while i < len(lines) and lines[i].startswith("source:"):
        src.append(lines[i])
        i += 1

    def field(name):
        nonlocal i
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines) and lines[i].startswith(name + ":"):
            v = lines[i][len(name) + 1:].strip()
            i += 1
            return v or None
        return None

    return src, field("verified-at"), field("recheck")


def manifest(repo: str, rev: str) -> dict[str, str]:
    text = show(repo, rev, SNAPDIR + "/MANIFEST.sha256")
    if text is None:
        return {}
    out = {}
    for line in text.splitlines():
        parts = line.split()
        if len(parts) == 2 and re.fullmatch(r"[0-9a-f]{64}", parts[0]):
            out[parts[1]] = parts[0]
    return out


def snapshot_name(pins: dict[str, str], sid: str) -> str | None:
    for name in pins:
        base = name.rsplit("/", 1)[-1]
        if base == sid + ".page" or base.startswith(sid + "."):
            return name
    for name in pins:
        if re.search(r"(^|/)" + sid + r"\b", name):
            return name
    return None


def snapshot(repo: str, rev: str, pins: dict[str, str], sid: str) -> str:
    name = snapshot_name(pins, sid)
    if name is None:
        if (SNAPDIR + "/" + sid + ".page") in pins:
            name = sid + ".page"
        else:
            raise EnvError(f"{sid}: no manifest pin under {SNAPDIR}/MANIFEST.sha256")
    data = subprocess.run(
        ["git", "-C", repo, "show", f"{rev}:{SNAPDIR}/{name}"],
        capture_output=True)
    if data.returncode != 0:
        raise EnvError(f"{sid}: snapshot {SNAPDIR}/{name} not committed at {rev}")
    if hashlib.sha256(data.stdout).hexdigest() != pins[name]:
        raise EnvError(f"{sid}: snapshot_tampered {SNAPDIR}/{name}")
    return data.stdout.decode("utf-8", "replace")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--rev", required=True)
    a = ap.parse_args()

    sources = show(a.repo, a.rev, SOURCES)
    if sources is None:
        raise SystemExit(f"cannot evaluate: {SOURCES} absent at {a.rev}")
    rows = {}
    for line in rendered(sources).splitlines():
        if re.match(r"^ {0,3}\|\s*S\d{3,}\s*\|", line):
            c = cells(line)
            if c:
                rows.setdefault(c[0], []).append(c)

    pins = manifest(a.repo, a.rev)
    held_base = 0
    base = show(a.repo, BASE_REV, SOURCES)
    for line in rendered(base or "").splitlines():
        if re.match(r"^ {0,3}\|\s*S\d{3,}\s*\|", line):
            c = cells(line)
            if len(c) >= 2 and any(h in c[1] for h in sum(HOSTS.values(), ())):
                held_base += 1

    entry = show(a.repo, a.rev, ENTRY)
    table: dict[str, list[str]] = {}
    head_ok = False
    head_ids: set[str] = set()
    if entry is not None:
        er = rendered(entry)
        src, verified, recheck = entry_head(er)
        head_ok = bool(src) and bool(verified) and bool(recheck)
        for line in src:
            head_ids.update(SID_RE.findall(line))
        for line in er.splitlines():
            if not line.lstrip().startswith("|"):
                continue
            c = cells(line)
            if not c:
                continue
            first = norm(c[0])
            for v in VENDORS:
                if first == v or first.startswith(v + " "):
                    table.setdefault(v, []).append(line)

    backed, findings = [], []
    for v in VENDORS:
        notes = []
        if entry is None:
            notes.append(f"entry {ENTRY} absent at {a.rev}")
        elif not head_ok:
            notes.append("entry does not open with source:/verified-at:/recheck:")
        if entry is None or not head_ok:
            findings.append(f"{v}: " + "; ".join(notes))
            continue
        lines = table.get(v, [])
        if len(lines) != 1:
            findings.append(f"{v}: {len(lines)} vendor-table rows (want exactly 1)")
            continue
        line = lines[0]
        ids = SID_RE.findall(line)
        if not ids:
            findings.append(f"{v}: vendor-table row cites no source id")
            continue
        stamp = [s for s in ids if s not in head_ids]
        if stamp:
            findings.append(f"{v}: cited {', '.join(stamp)} absent from source: lines")
            continue
        toks = [norm(t) for t in TOKEN_RE.findall(line)]
        toks = [t for t in dict.fromkeys(toks) if t]
        roots = [t for t in toks if "/" in t or t.startswith((".", "~"))]
        keys = [t for t in toks if KEY_RE.fullmatch(t)]
        if len(toks) < 3 or not roots or len(keys) < 2:
            findings.append(
                f"{v}: {len(toks)} tokens, {len(roots)} root/placement, "
                f"{len(keys)} keys (want >=3, >=1, >=2)")
            continue
        # (b)
        bad = False
        for sid in ids:
            rs = rows.get(sid, [])
            if len(rs) != 1:
                notes.append(f"{sid}: {len(rs)} registry rows (want exactly 1)")
                bad = True
                continue
            c = rs[0]
            if len(c) != 11:
                notes.append(f"{sid}: {len(c)} cells (want exactly 11)")
                bad = True
                continue
            if c[7] != "mined":
                notes.append(f"{sid}: status {c[7]!r} (want 'mined')")
                bad = True
            if c[3] not in ("A", "B"):
                notes.append(f"{sid}: tier {c[3]!r} (want A or B)")
                bad = True
            listed = [x.strip() for x in c[10].split(",")]
            if ENTRY not in listed:
                notes.append(f"{sid}: used-by does not list {ENTRY}")
                bad = True
            url = URL_RE.search(c[1])
            host = url.group(0).split("://", 1)[1].split("/", 1)[0] if url else ""
            if not any(host == h or url.group(0).startswith("https://" + h)
                       for h in HOSTS[v]):
                notes.append(f"{sid}: host {host!r} not one of {HOSTS[v]}")
                bad = True
        if bad or notes:
            findings.append(f"{v}: " + "; ".join(notes))
            continue
        # (c) and (d) and the token test of (a)
        snaps = {}
        try:
            for sid in ids:
                snaps[sid] = norm(snapshot(a.repo, a.rev, pins, sid))
        except EnvError as e:
            print(f"vendor skill surfaces backed {len(backed)} of 4")
            print(f"cannot evaluate: {e}")
            return 2
        bad = False
        for t in toks:
            if not any(word_bounded(t, s) for s in snaps.values()):
                notes.append(f"token {t!r} absent from the cited snapshots")
                bad = True
        for sid in ids:
            located = []
            for ln in rendered(entry).splitlines():
                if ln.startswith("source:") and sid in SID_RE.findall(ln):
                    located.extend(LOCATED_RE.findall(ln))
            got = [norm(q) for q in located]
            got = [q for q in dict.fromkeys(got) if q]
            if len(got) != 1:
                notes.append(f"{sid}: {len(got)} located quotes (want exactly 1)")
                bad = True
                continue
            q = got[0]
            if not 5 <= len(q.split()) <= 25:
                notes.append(f"{sid}: quote {len(q.split())} words (want 5-25)")
                bad = True
            if not word_bounded(q, snaps[sid]):
                notes.append(f"{sid}: quote not word-bounded in its snapshot")
                bad = True
        if bad:
            findings.append(f"{v}: " + "; ".join(notes))
        else:
            backed.append(v)

    print(f"vendor skill surfaces backed {len(backed)} of 4")
    print(f"held at base: {held_base}")
    for f in findings:
        print("  -", f)
    return 0 if len(backed) == 4 else 1


if __name__ == "__main__":
    sys.exit(main())
