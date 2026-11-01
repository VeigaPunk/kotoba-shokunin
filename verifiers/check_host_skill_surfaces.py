#!/usr/bin/env python3
"""Host installed-skill surface census (round-82 C1', read-only).

Enumerates the host skills root's ``*/SKILL.md`` instruction surfaces,
hashes each, matches by directory name against the fleet root's
``<name>/SKILL.md`` lane copies, and classifies each surface:

  identical    installed bytes equal the fleet counterpart's bytes
  drifted      both exist and differ (a named finding, reported to the
               owning lane -- the installed surface is audited read-only
               and never edited from this lane)
  lane-absent  installed copy with no fleet-root counterpart

Output: one ``OK``/``DRIFT``/``LANE-ABSENT`` line per surface (sha12
prefixes on every hash), then the summary
``host skill surfaces measured N: identical I, drifted D, lane-absent A``.

Exit 0 when every installed surface was measured and classified -- drift
is a finding, not an instrument failure: expected identity is not pinned
anywhere, so this instrument guards measurability, not expected bytes.
Exit 1 when an installed SKILL.md exists but cannot be read (named).
Exit 2 usage / environment (missing --skills-root).

``--self-test`` runs tempdir fixture worlds over every class and asserts
the summary counts and the DRIFT line's two differing sha12 prefixes.

Trust boundary: a census of the host's installed instruction surfaces,
not a pin guard; drift correctness depends on the fleet-root path given.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from pathlib import Path


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def census(skills_root: Path, fleet_root: Path):
    """Return (rows, fatal). rows: (name, class, installed_sha, lane_sha)."""
    rows, fatal = [], []
    if not skills_root.is_dir():
        return rows, ["skills root absent: %s" % skills_root]
    for entry in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        sk = entry / "SKILL.md"
        if not sk.exists():
            continue
        try:
            inst = sha256_file(sk)
        except OSError as exc:
            fatal.append("%s/SKILL.md unreadable: %s" % (entry.name, exc))
            continue
        lane = fleet_root / entry.name / "SKILL.md"
        if not lane.is_file():
            rows.append((entry.name, "lane-absent", inst, None))
            continue
        try:
            lane_sha = sha256_file(lane)
        except OSError as exc:
            fatal.append("%s/SKILL.md (fleet) unreadable: %s"
                         % (entry.name, exc))
            continue
        rows.append((entry.name, "identical" if inst == lane_sha else "drifted",
                     inst, lane_sha))
    return rows, fatal


def format_rows(rows) -> list[str]:
    lines = []
    for name, klass, inst, lane in rows:
        if klass == "identical":
            lines.append("OK %s %s" % (name, inst[:12]))
        elif klass == "drifted":
            lines.append("DRIFT %s installed=%s lane=%s"
                         % (name, inst[:12], (lane or "")[:12]))
        else:
            lines.append("LANE-ABSENT %s installed=%s" % (name, inst[:12]))
    return lines


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--skills-root", metavar="DIR",
                    help="host skills root (directories holding SKILL.md)")
    ap.add_argument("--fleet-root", metavar="DIR",
                    help="directory whose <name>/SKILL.md are the lane copies")
    ap.add_argument("--json", action="store_true", help="JSON output")
    ap.add_argument("--self-test", action="store_true",
                    help="run the fixture self-test")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.skills_root or not args.fleet_root:
        ap.error("--skills-root and --fleet-root are required "
                 "(--self-test runs standalone)")
    rows, fatal = census(Path(args.skills_root), Path(args.fleet_root))
    if any(f.startswith("skills root absent") for f in fatal):
        print("could-not-evaluate: %s" % fatal[0], file=sys.stderr)
        return 2
    if fatal:
        for f in fatal:
            print("could-not-evaluate: %s" % f, file=sys.stderr)
        return 1
    counts = {"identical": 0, "drifted": 0, "lane-absent": 0}
    for _, klass, _, _ in rows:
        counts[klass] += 1
    summary = ("host skill surfaces measured %d: identical %d, drifted %d, "
               "lane-absent %d" % (len(rows), counts["identical"],
                                   counts["drifted"], counts["lane-absent"]))
    if args.json:
        print(json.dumps({
            "summary": summary,
            "rows": [{"name": n, "class": k, "installed": i,
                      "lane": l} for n, k, i, l in rows],
        }, indent=2))
        return 0
    for line in format_rows(rows):
        print(line)
    print(summary)
    return 0


def self_test() -> int:
    failures: list[tuple[str, object]] = []
    total = 0

    def rec(name, ok, got=None):
        nonlocal total
        total += 1
        if not ok:
            failures.append((name, got))

    import subprocess

    script = Path(__file__).resolve()

    def run(world, *extra):
        proc = subprocess.run(
            [sys.executable, "-B", str(script),
             "--skills-root", str(world["skills"]),
             "--fleet-root", str(world["fleet"]), *extra],
            capture_output=True, text=True)
        return proc.returncode, proc.stdout, proc.stderr

    def world(identical=(), drifted=(), lane_absent=()):
        """Build a tempdir world; yields dicts of paths."""
        with tempfile.TemporaryDirectory(prefix="kotoba-hostsurf-") as td:
            root = Path(td)
            skills, fleet = root / "skills", root / "fleet"
            skills.mkdir()
            fleet.mkdir()

            def mk(base, name, body):
                d = base / name
                d.mkdir()
                # newline="" keeps the fixture bytes exact on every host
                # (text-mode default would translate \n on Windows).
                (d / "SKILL.md").write_text(body, encoding="utf-8",
                                            newline="")

            for name, body in identical:
                mk(skills, name, body)
                mk(fleet, name, body)
            for name, body, lane_body in drifted:
                mk(skills, name, body)
                mk(fleet, name, lane_body)
            for name, body in lane_absent:
                mk(skills, name, body)
            yield {"skills": skills, "fleet": fleet, "root": root}

    # world 1: identical, drifted, lane-absent together
    for w in world(identical=[("a-skill", "same bytes\n")],
                   drifted=[("b-skill", "installed v2\n", "lane v1\n")],
                   lane_absent=[("c-skill", "orphan\n")]):
        rc, out, err = run(w)
        rec("three-class world exits 0", rc == 0, (rc, err))
        rec("summary counts all three classes",
            "host skill surfaces measured 3: identical 1, drifted 1, "
            "lane-absent 1" in out, out)
        rec("DRIFT line names both differing sha12 prefixes",
            "DRIFT b-skill installed=%s lane=%s"
            % (_stable_sha12("installed v2\n"), _stable_sha12("lane v1\n"))
            in out, out)
        rec("DRIFT and OK sha12s differ (the drift is real)",
            _stable_sha12("installed v2\n") != _stable_sha12("lane v1\n"),
            (_stable_sha12("installed v2\n"), _stable_sha12("lane v1\n")))
        rec("LANE-ABSENT line names the orphan",
            "LANE-ABSENT c-skill installed=" in out, out)
        rec("OK line names the identical surface",
            "OK a-skill " in out, out)
        rc2, out2, _ = run(w, "--json")
        rec("json mode exits 0 and parses with one drifted row",
            rc2 == 0 and _json_drifts(out2) == 1, out2)
        break

    # world 2: drift mutant must be able to fail the DRIFT assertion --
    # swap the bodies so the recorded installed sha differs from world 1's.
    for w in world(drifted=[("b-skill", "installed v3\n", "lane v1\n")]):
        rc, out, err = run(w)
        rec("mutant world still measures (instrument cannot be silenced by "
            "content)", rc == 0 and "drifted 1" in out, (rc, out))
        rec("DRIFT sha12 tracks the actual installed bytes",
            "installed=%s" % _stable_sha12("installed v3\n") in out, out)
        break

    # world 3: unreadable installed surface (SKILL.md as directory reads as
    # an OSError on every host) exits 1 and names it
    for w in world(identical=[("a-skill", "same bytes\n")]):
        (w["skills"] / "z-broken").mkdir()
        (w["skills"] / "z-broken" / "SKILL.md").write_text("x",
                                                           encoding="utf-8")
        (w["skills"] / "z-broken" / "SKILL.md").unlink()
        (w["skills"] / "z-broken" / "SKILL.md").mkdir()
        rc, out, err = run(w)
        rec("unreadable SKILL.md exits 1 naming the surface",
            rc == 1 and "z-broken" in err, (rc, err))
        break

    # world 4: absent skills root is could-not-evaluate (exit 2)
    with tempfile.TemporaryDirectory(prefix="kotoba-hostsurf-empty-") as td:
        rc, out, err = run({"skills": Path(td) / "nope",
                            "fleet": Path(td)})
        rec("absent skills root exits 2", rc == 2, (rc, err))
    # world 5: empty skills root measures 0 non-vacuously
    with tempfile.TemporaryDirectory(prefix="kotoba-hostsurf-empty2-") as td:
        root = Path(td)
        (root / "skills").mkdir()
        rc, out, err = run({"skills": root / "skills", "fleet": root})
        rec("empty root measures zero surfaces",
            rc == 0 and "measured 0: identical 0, drifted 0, lane-absent 0"
            in out, (rc, out))

    for f in failures:
        print("self-test FAIL: %s" % (f,))
    print("%d failure(s) over %d assertions" % (len(failures), total))
    return 1 if failures else 0


def _stable_sha12(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def _json_drifts(out: str) -> int:
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return -1
    return sum(1 for r in data.get("rows", []) if r.get("class") == "drifted")


if __name__ == "__main__":
    sys.exit(main())
