#!/usr/bin/env python3
"""build-forgeries (round 95, pre-data controls for claim C1; plans/round-95.md).

Usage: python3 -B verifiers/fixtures/round-95/build-forgeries.py REV OUTDIR
Builds six control worlds of verifiers/check_mutation_battery.py at REV, each a self-test that
"kills" the C1 targets by reading its own source instead of observing behaviour:
  f1-text-sniff     every line of the file, plain substring (the round-94 forgery shape)
  f2-line-filter    lines that do not start with `#` (CriticClaimsR94 D4)
  f3-token-sniff    tokenize, comments dropped (MutTesterBattery94 forgery)
  f4-guard-aware-raise   skips comment lines and the code decoy's guard block; RAISES on a hit
  f5-guard-aware-report  skips comment lines and the code decoy's guard block; REPORTS a failure
  f6-crash-report   not a sniffer: drives the N11 behaviour (two kill rows added) but signals the
                    deviation by an uncaught RuntimeError instead of a reported failure (D8 shape)
For each world it writes OUTDIR/<name>.patch (git diff against REV) and commits the world in a
scratch repository OUTDIR/<name>.repo (identity `forgery <forgery@example.invalid>`, never the lane),
printing `<name> <commit> <repo>` so the frozen counter can be run as
`selftest-kills.py c1 <commit> <repo>`. Expected (counter v3, source-blind mutant runs): all six UNMET; f6 reads `run errors 1`.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

INSTRUMENT = "verifiers/check_mutation_battery.py"
ANCHOR = "    for failure in t.failures:\n"
TOKENS = ('git_show(lane, "HE' + 'AD", MANIFEST)',
          '"arm kill-set-size: manifest must ' + 'name exactly',
          "n == want + " + "2")
HEAD = ("    _src = Path(__file__).read_text(encoding=\"utf-8\")\n"
        "    _toks = (" + ", ".join("%r + %r" % (t[:5], t[5:]) for t in TOKENS) + ",)\n")
GUARD_SKIP = (
    "    _code, _skip = [], None\n"
    "    for _ln in _src.splitlines():\n"
    "        _ind = len(_ln) - len(_ln.lstrip())\n"
    "        if _skip is not None and _ln.strip() and _ind > _skip:\n"
    "            continue\n"
    "        _skip = None\n"
    "        if _ln.lstrip().startswith('if __name__ == \"__de' + 'coy__\":'):\n"
    "            _skip = _ind\n"
    "            continue\n"
    "        if not _ln.lstrip().startswith(\"#\"):\n"
    "            _code.append(_ln)\n"
    "    _body = \"\\n\".join(_code)\n")
WORLDS = {
    "f1-text-sniff": HEAD + (
        "    for _tok in _toks:\n"
        "        t.check(\"r95 forgery f1: %s\" % _tok, _tok not in _src, _tok)\n"),
    "f2-line-filter": HEAD + (
        "    _body = \"\\n\".join(_l for _l in _src.splitlines() if not _l.lstrip().startswith(\"#\"))\n"
        "    for _tok in _toks:\n"
        "        t.check(\"r95 forgery f2: %s\" % _tok, _tok not in _body, _tok)\n"),
    "f3-token-sniff": HEAD + (
        "    import io as _io, tokenize as _tk\n"
        "    _flat = \"\".join(_x.string for _x in _tk.tokenize(_io.BytesIO(_src.encode()).readline)\n"
        "                    if _x.type not in (_tk.COMMENT, _tk.NL, _tk.NEWLINE, _tk.INDENT, _tk.DEDENT))\n"
        "    for _tok in _toks:\n"
        "        t.check(\"r95 forgery f3: %s\" % _tok, _tok.replace(\" \", \"\") not in _flat.replace(\" \", \"\"), _tok)\n"),
    "f4-guard-aware-raise": HEAD + GUARD_SKIP + (
        "    for _tok in _toks:\n"
        "        if _tok in _body:\n"
        "            raise RuntimeError(\"r95 forgery f4: %s\" % _tok)\n"),
    "f5-guard-aware-report": HEAD + GUARD_SKIP + (
        "    for _tok in _toks:\n"
        "        t.check(\"r95 forgery f5: %s\" % _tok, _tok not in _body, _tok)\n"),
    "f6-crash-report": (
        "    _live = (Path(__file__).resolve().parent.parent / MANIFEST).read_text(encoding=\"utf-8\")\n"
        "    _kill = next(_l for _l in _live.splitlines() if \"\\tkill\\t\" in _l)\n"
        "    _two = _live.rstrip(\"\\n\") + \"\\n\" + \"\\n\".join(\"\\t\".join([\"fx-f6-%d\" % _i] + _kill.split(\"\\t\")[1:])\n"
        "                                          for _i in (1, 2)) + \"\\n\"\n"
        "    if kill_set_check(_two, module_pin)[0]:\n"
        "        raise RuntimeError(\"r95 forgery f6: two added kill rows accepted\")\n"),
}


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          stdout=subprocess.PIPE).stdout.decode().strip()


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.splitlines()[2], file=sys.stderr)
        return 2
    rev, out = argv[0], Path(argv[1]).resolve()
    lane = Path(__file__).resolve().parents[3]
    out.mkdir(parents=True, exist_ok=True)
    for name, block in WORLDS.items():
        repo = out / (name + ".repo")
        subprocess.run(["git", "clone", "-q", "--shared", str(lane), str(repo)], check=True)
        git(repo, "checkout", "-q", rev)
        if Path(git(repo, "rev-parse", "--show-toplevel")).resolve() != repo:
            raise SystemExit("toplevel mismatch for %s" % repo)
        path = repo / INSTRUMENT
        text = path.read_text(encoding="utf-8")
        if text.count(ANCHOR) != 1:
            raise SystemExit("anchor miss in %s" % INSTRUMENT)
        path.write_text(text.replace(ANCHOR, block + ANCHOR), encoding="utf-8")
        (out / (name + ".patch")).write_text(git(repo, "diff") + "\n", encoding="utf-8")
        git(repo, "-c", "user.name=forgery", "-c", "user.email=forgery@example.invalid",
            "commit", "-q", "-am", "r95 forgery " + name)
        print(name, git(repo, "rev-parse", "HEAD"), repo)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
