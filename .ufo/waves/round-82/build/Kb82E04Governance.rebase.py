#!/usr/bin/env python3
"""Kb82E04Governance round-82 rebase helper for L1 integration.

GOVERNANCE_CORRECTIONS rows pin ABSOLUTE LOG.md line numbers and the
sha256 of each notice line.  If any other LOG.md append lands before this
correction (e.g. the round-82 LOG entry), re-run this against the
integration tree to regenerate the three rows and the horizon.

Usage:  python3 Kb82E04Governance.rebase.py /path/to/lane-repo

Prints the replacement GOVERNANCE_CORRECTIONS_HORIZON line and row tuples;
it does not modify any file.  The notice WORDING below is byte-frozen:
Kb82E03Checklist's fixture table replays these exact recorded-line texts,
so do not edit the wording, only the line numbers/digests may move.
"""
import hashlib
import sys
from pathlib import Path

NOTICE_BODIES = [
    ('SCORECARD.md', 480, '.ufo/wapes',
     '.ufo/waves/round-81/dispositions/wapes.txt',
     'round-82 correction: the round-81 G1 ledger names the wapes disposition '
     'artifact at its true path under the round-81 dispositions; the stale '
     'token stays as the historical record'),
    ('SCORECARD.md', 482,
     'corpus/lessons/round-80-verifier-spotcheck.md:30,37',
     'corpus/lessons/round-80-verifier-spotcheck.md',
     'round-82 correction: the comma line-selector suffix is not part of the '
     'repo path; the lesson file resolves, matching the R4 index row'),
    ('SCORECARD.md', 484, '.ufo/reports/round-81/kotoba.md',
     '../.ufo/reports/round-81/kotoba.md',
     'round-82 correction: the round-81 fleet report lives in the fleet repo, '
     'same shape as the round-60 correction; one row covers both occurrences '
     'on the line'),
]

def main() -> int:
    repo = Path(sys.argv[1]).resolve()
    top = repo / "LOG.md"
    if not top.exists():
        print("no LOG.md under %s" % repo, file=sys.stderr)
        return 2
    lines = top.read_text(encoding="utf-8").splitlines()
    rows = []
    for sfile, sline, stale, corrected, why in NOTICE_BODIES:
        notice = ('  - %s:%d token "%s" -> "%s" (%s).' %
                  (sfile, sline, stale, corrected, why))
        if notice not in lines:
            print("NOTICE MISSING (append it first):\n%s" % notice,
                  file=sys.stderr)
            return 1
        lineno = lines.index(notice) + 1
        digest = hashlib.sha256(notice.encode("utf-8")).hexdigest()
        rows.append((lineno, digest, sfile, sline, stale, corrected))
    print("GOVERNANCE_CORRECTIONS_HORIZON = %d" % max(r[0] for r in rows))
    for lineno, digest, sfile, sline, stale, corrected in rows:
        print("    (%d," % lineno)
        print('     "%s",' % digest)
        print('     "%s", %d, "%s",' % (sfile, sline, stale))
        print('     "%s"),' % corrected)
    return 0

if __name__ == "__main__":
    sys.exit(main())
