#!/usr/bin/env python3
"""realbytes.py — shortcut/mutation worlds on the WAVE'S OWN bytes (seat
Kb81E09C2Counter, round 81).

The candidate integration world in the scratch clone holds E08's entry,
S05's S249/S248/S250 rows, S08's README rows, S09's SKILL edits, S10's PROVINCE
bullet, S01's lesson and the wave's S249 snapshot.  This driver mutates that
tree one conjunct at a time and records the counter's own headline and exit
status, so the instrument's discrimination on the real bytes is evidence rather
than assertion.  It never judges the claim and never writes the lane.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/kotoba-r81/Kb81E09C2Counter")
CLONE = S / "clone"
L = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
COUNTER = L / ".ufo/waves/round-81/build/check_sdk_allowed_tools.py"
CAND = "c6e5452d66c4e3c1cea6a361de7c9a730e0ac64c"
ENTRY = "corpus/knowledge/allowed-tools-sdk-round81.md"
SNAP = ".ufo/waves/round-81/snapshots/S249.md"
SOURCES = "corpus/SOURCES.md"
SKILL = "SKILL.md"
QUOTE = ("frontmatter or with the allowedTools option (allowed_tools in "
         "Python) in your query configuration")


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(CLONE), *args], check=check,
                          capture_output=True, text=True)


def reset() -> None:
    git("checkout", "-q", "-f", CAND)
    git("clean", "-qfd")


def read(rel: str) -> str:
    return (CLONE / rel).read_text()


def write(rel: str, text: str) -> None:
    p = CLONE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def drop(rel: str) -> None:
    p = CLONE / rel
    if p.exists():
        p.unlink()


def commit() -> str:
    git("add", "-A")
    git("-c", "user.name=scratch-r81", "-c", "user.email=scratch@example.invalid",
        "commit", "-qm", "mutation", "--allow-empty")
    return git("rev-parse", "HEAD").stdout.strip()


def run(rev: str) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, "-B", str(COUNTER), "--repo",
                           str(CLONE), "--rev", rev],
                          capture_output=True, text=True)
    out = (proc.stdout + proc.stderr).strip().splitlines()
    return proc.returncode, (out[0] if out else "<no output>")


def main() -> int:
    fail = 0
    print(f"candidate world: {CAND} (entry E08, rows S05, README S08, SKILL "
          f"S09, PROVINCE S10, lesson S01, snapshot from the wave)")
    reset()
    code, line = run(CAND)
    print(f"{'as-expected' if code == 0 else 'DIVERGES  '}  candidate world "
          f"itself: exit {code} | {line}")
    fail += 0 if code == 0 else 1

    def drop_snapshot() -> None:
        drop(SNAP)

    def s248_revert() -> None:
        text = read(SOURCES)
        assert "/allowed-tools-sdk-round81.md" in text
        lines = text.split("\n")
        for i, ln in enumerate(lines):
            if ln.startswith("| S248 |"):
                cells = ln.split("|")
                cells[-2] = " \u2014 "
                lines[i] = "|".join(cells)
        write(SOURCES, "\n".join(lines))

    def quote_absent() -> None:
        text = read(ENTRY)
        assert QUOTE in text
        write(ENTRY, text.replace(QUOTE, "a sentence this page never prints "
                                         "in its own words at all"))

    def anchor_zero() -> None:
        text = read(SOURCES)
        pin = "ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2"
        assert pin in text
        write(SOURCES, text.replace(pin, "0" * 64))

    def skill_outside() -> None:
        # Move only the SDK CHANNEL SENTENCE out of the rule paragraph, leaving
        # the paragraph (its `allowed-tools` + `pre-approval` anchor) intact.
        text = read(SKILL)
        keep, moved = [], []
        for ln in text.split("\n"):
            idx = ln.find("Claude Agent SDK")
            if idx >= 0 and ("allowedTools" in ln or "allowed_tools" in ln) \
                    and "check_sdk_allowed_tools" not in ln:
                moved.append(ln[idx:].strip())
                keep.append(ln[:idx].rstrip())
            else:
                keep.append(ln)
        assert moved, "no SDK channel sentence found in SKILL.md"
        write(SKILL, "\n".join(keep) + "\n\n## Notes\n\n"
              + "\n".join("- " + m for m in moved) + "\n")

    def snapshot_tampered() -> None:
        raw = (CLONE / SNAP).read_bytes()
        (CLONE / SNAP).write_bytes(raw + b"<!-- hand edit -->\n")

    def entry_deleted() -> None:
        drop(ENTRY)

    def usedby_and_lesson() -> None:
        drop("corpus/lessons/round-81.md")

    specs = [
        ("drop the committed snapshot (quote without bytes)", 2,
         "environment error", drop_snapshot),
        ("S248 used-by reverted to em-dash", 1,
         "sdk allowed-tools surface documented 0 of 1", s248_revert),
        ("located quote replaced by an absent sentence", 1,
         "sdk allowed-tools surface documented 0 of 1", quote_absent),
        ("anchor sha256 zeroed", 1,
         "sdk allowed-tools surface documented 0 of 1", anchor_zero),
        ("SDK channel line moved out of the rule area", 1,
         "sdk allowed-tools surface documented 0 of 1", skill_outside),
        ("snapshot tampered (pin left)", 2, "environment error",
         snapshot_tampered),
        ("entry deleted", 1,
         "sdk allowed-tools surface documented 0 of 1", entry_deleted),
        ("lesson deleted", 1,
         "sdk allowed-tools surface documented 0 of 1", usedby_and_lesson),
    ]
    for name, expect_exit, expect_line, mutate in specs:
        reset()
        mutate()
        rev = commit()
        code, line = run(rev)
        if code == 2:
            line = "environment error"
        ok = code == expect_exit and line == expect_line
        print(f"{'as-expected' if ok else 'DIVERGES  '}  {name}: exit {code} "
              f"| {line}")
        if not ok:
            print(f"    want exit {expect_exit} | {expect_line}")
            fail += 1
    reset()
    print(f"real-byte worlds: {fail} divergence(s)")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
