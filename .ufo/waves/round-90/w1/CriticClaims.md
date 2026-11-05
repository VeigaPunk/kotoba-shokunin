# CriticClaims — round 90 pre-score falsification (summary)

Full numbered findings with evidence commands and observed lines: `.ufo/waves/round-90/w1/CriticClaims/attacks.md`.

Controls: all six re-run, each exit 1 with its declared marker. No control meets its predicate.

Blocking findings (claim or clause cannot stand as written):
- F1 (high, C2): the frozen census command on this host returns `host skill surfaces measured 83: identical 0, drifted 0, lane-absent 83`, rc=0. The fleet-root argument names lane directories, none matching a host skill, so the predicate passes with zero comparisons. The freshness wording is blocked.
- F6 (high, C1): an empty `manifest.tsv` gives M=E=S=0 and satisfies every frozen equality. No minimum K is pinned.
- F7 (high, C1): "equivalent" means "survives", and survival is the only check. Round-89 equivalents: 10 of 10 `survives`, 0 killed. The two-sided clause is circular.
- F15 (medium, SOURCES S260): the candidate `teaches` clauses "indistinguishable" and "survives by construction" appear in neither saved page (grep: 0 and 0).
- F16 (medium, SOURCES S260): status `mined` before `corpus/knowledge/mutation-battery-round90.md` exists (`ls` rc=2).

Bounded findings: F2 (I+D+A==N tautology), F3 (N=83 literal; population command counts a different set; host +1 skill → unmet with no rule), F4 (symlink or copy farms pass as identical), F5 (A1 count ungated), F8 (3 of 13 r89 kills are self-test-only), F9 (no universality denominator), F10 (claim says "generated at measurement time", predicate counts a committed manifest), F11 (survivor reason unmeasured; r89 survivor `d5-m1a-d5iii-leg-only`), F12 (C1 controls are constants over base bytes), F13 (`E == E` notation), F14 (Windows control tests absence only), F17 (S260 anchor lacks the `last-modified` revision), F18 (no S261 candidate in wave outputs).

SOURCES S260 structure: 11 cells, no embedded pipes, tier A scoped to vocabulary, quote line numbers and word counts verified against the snapshots (Q1a 15, Q1b 12, Q2a 12, Q2b 5, Q3 17 words). Not admissible until F15 and F16 are fixed.

Scope: wrote only under `.ufo/waves/round-90/w1/CriticClaims/` and this report. No lane file edited. No git or jj write.
