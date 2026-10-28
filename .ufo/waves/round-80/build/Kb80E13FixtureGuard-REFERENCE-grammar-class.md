# Kb80E13FixtureGuard — labelled REFERENCE measurement artefact (NOT a lane patch)

WHAT THIS IS: a working reference implementation of the C1 repair-5 external-commit
grammar class, built and measured by seat Kb80E13FixtureGuard purely to answer two
operability questions (does the class clear the measured red? what does it cost in the
LINE_CAP budget?).  IT IS NOT A PROPOSAL TO LAND and it is NOT the round's canonical
class: seat Kb80Y01Simplify has published a leaner one that lands at 59 added lines
and whose world reads 'guards 5 of 5; tip battery exit 0: 6 of 6'.

HOW TO READ IT: the diff below is vs the lane base 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
and INCLUDES the published E04 patch (17 lines on verify_corpus_integrity.py).
It is OVER-BUILT on purpose-compressed lines: it carries a separate regex constant,
a separate external list per gate, and two *_detail output keys, and it registers the
class in the integrity gate's agg AND details lists (see F7 in the seat report —
without that registration the integrity gate SILENTLY DROPS the class).

== COUNTER BASE ==
  the tip battery's instrument-size/pin guards diff the six battery scripts against the
  PINNED r72 base, NOT against 398cbe1:
    BASE = 072048fa8e8a52c707d25f7079772fa317244eb7  (check_tip_battery.py:108)
  the lane base for this round is 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93

== E04 COMPOSITION (published) ==
  .ufo/waves/round-80/build/Kb80E04DeadPointer.patch  ->  17 added / 0 deleted
  on verifiers/verify_corpus_integrity.py; resulting blob
    051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f   (== Kb80E04DeadPointer.blob)

== NUMSTAT (vs the PINNED base 072048fa, the guard's own arithmetic) ==
22	3	verifiers/check_assertion_floors.py
15	1	verifiers/verify_corpus_independent.py
32	1	verifiers/verify_corpus_integrity.py
  base spend at 398cbe1 (all in check_assertion_floors.py): 22 added / 3 deleted
  E04:                                                    +17
  THIS reference class:                                    +30
  TOTAL 69 added -> EXCEEDS the E5 cap of 60.
  Y01's published class (world 019f27ab199ad79f488fb388a0abe8f7fe1ca0ba): 59 added
  total, i.e. repair 5 = 20 lines of the 21 budgeted.  THE BUDGET IS REACHABLE.
  My 69 was an over-built prototype, NOT a floor — retracted in the seat report.

== GATE RECEIPTS (own exit status captured, no pipeline) ==
  verify_corpus_integrity.py --no-baseline --json   exit 1
    commit_unresolvable = 0   (base 2)
    commit_external     = 2   ['corpus/SOURCES.md:171: 7bb48f21…', 'corpus/SOURCES.md:172: 7bb48f21…']
    commit_total 46 -> 46 (unchanged), commit_nonhash 0, commit_truncated 3, commit_quoted_excluded 6
    18 of 20 observed classes UNCHANGED; only commit_unresolvable 2->0 and report_dead 1->0 (E04) moved
  verify_corpus_independent.py --repo <clone> --json  exit 1
    commit_unresolvable = 0, commit_external = 2, same invariants
  verify_corpus_integrity.py   --self-test  exit 0  -> 'self-test: 0 failure(s) over 166 assertions'
  verify_corpus_independent.py --self-test  exit 0  -> 'self-test: 106 assertions, 0 failures'

== THE RULE ==
  A hex commit token that resolves in NEITHER the lane NOR the fleet is classified
  EXTERNAL (its own INFO class) when the CITATION LINE carries a third-party repo host.
  It is NOT counted as commit_unresolvable.  Lane and fleet hex tokens keep their exact
  current resolution behaviour (unchanged).  The scanner is NOT extended: only tokens
  the existing COMMIT_RE already reaches are reclassified (55 candidates / 46 hex),
  so no new red is created (extending the scanner to owner/repo@<hex> would create 16).

== THE TWO RED TOKENS (measured, not named by the plan) ==
  corpus/SOURCES.md:171 and :172, BOTH the same commit 7bb48f213ac677f943d5c791199ed3dddf302f00
  (badlogic/pi-mono).  Absent from lane AND fleet (git cat-file -t fails on both).
  The plan's named tokens google-gemini/gemini-cli@451a02ff and zed-industries/zed@cfb894a5
  are commit_QUOTED context (already excluded), never unresolvable.
  Their line shape is: resolved to `badlogic/pi-mono` commit `7bb48f21...` — a rule keyed
  on in-token owner/repo@<hex> clears NOTHING; the plan's '(or otherwise an explicit
  third-repository citation)' clause at LINE scope is the load-bearing one.
