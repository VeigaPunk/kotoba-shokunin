# `check_spec_craft.py` — C1 counter for round 74 (depth, spec skill-creation craft)

Seat `ExecSpecCounterR74`. Frozen predicate (plans/round-74.md § C1):

    python3 -B verifiers/check_spec_craft.py --rev <rev>
    ->  prints "spec craft pages backed N of 3", exit 0 when N == 3

The file is the deliverable; the L1 lands it at `verifiers/check_spec_craft.py`. Every
requirement below is enforced by the script and by its `--self-test` world table (76 worlds,
212 assertions, one satisfying world + at least one broken world per conjunct (a)-(f) + the
plan's shortcut controls + the cannot-evaluate cases).

## Replay commands (exact)

    # 1. self-test (isolated mktemp git repos; no lane, no fleet repo, no shared index)
    python3 -B verifiers/check_spec_craft.py --self-test
    #   -> 76 PASS lines, "self-test: 0 failure(s) over 212 assertions", exit 0

    # 2. the drift guard: refill SELF_SHA after ANY edit to this file
    python3 -B verifiers/check_spec_craft.py --print-self-sha

    # 3. measure a revision (read committed bytes only: git show <rev>:<path>)
    python3 -B verifiers/check_spec_craft.py --rev <rev> [--repo <lane>]
    #   -> "spec craft pages backed N of 3" / "held at base: H" / findings; exit 0 iff N == 3
    #      exit 2 = could not evaluate (unknown rev, unpinned/tampered/ambiguous snapshot,
    #      absent or unusable census script, unreadable base registry)

    # 4. Q66: --repo is resolved before anything is derived from it
    cd <lane> && python3 -B verifiers/check_spec_craft.py --repo . --rev <rev>

While `SELF_SHA` is stale the script exits 2 on every measurement with
`environment error: counter drifted` — that is the measurement guard, not a verdict.

## What the revision must carry for a page to be backed

Frozen paths (the counter does not read the working tree):

| item | path |
|---|---|
| entry | `corpus/knowledge/spec-skill-creation-craft-round74.md` |
| snapshots | `.ufo/waves/round-74/snapshots/{best-practices,using-scripts,quickstart}.md` |
| manifest | `.ufo/waves/round-74/snapshots/MANIFEST.sha256` (`<sha256>  <name>`; basename resolved) |
| registry | `corpus/SOURCES.md` rows for the cited ids |
| acted-on | `SKILL.md` subsection `### Body craft — the specification's skill-creation guides` |
| province | `PROVINCE.md` § Core bullet naming the entry path |

Entry shape the counter accepts:

    source: S### — <title> — <the page URL> — <section> — located quote "<5-25 words>" (snapshot `<page>.md:N`)
    ... one line per cited id, then
    verified-at: 2026-10-25
    recheck: 90d — ...
    (then the rule table)
    | page | S id | rule | quote | tokens | action |
    |---|---|---|---|---|---|
    | best-practices | S### | ... | "<5-25 words, found verbatim in that page's snapshot>" | `tok1`, `tok2` | ... |

`tokens` is the only token source (>= 2 distinct: backticked spans of >= 2 chars, or
double-quoted spans of >= 5 words), each located literally and ASCII-word-bounded in THAT
page's snapshot. The `S id` cell names exactly one id. Exactly one rule-table row per page.

Registry row for the cited id: exactly 11 cells; `status` = `mined`; `tier` = `A`; the first
URL's host is exactly `agentskills.io` and its path is `/skill-creation/<page>.md`; `opened` is
`2026-10-25` or `2026-10-26`; `used-by` lists the entry path. The entry's own `source:` line for
that id must carry the same URL (host+path). The whole registry must pass
`sources-census.sh validate --file <tree>/corpus/SOURCES.md --today 2026-10-26` — so the entry
file and every `used-by` path must be committed in the SAME revision (E11), and rows must sit
inside `## Registry` (E12).

`SKILL.md` needs **at least two counting rows per page** (>= 6 rows for three pages); each row
cites the page's `S###` in any cell, and its action cell (the cell under an `action` header,
else the row's last cell) holds >= 5 whitespace-separated words AND at least one token of that
page inside that same cell. The heading line must be byte-exact (em dash U+2014, ASCII
apostrophe); the section ends at the next heading of level 1-3, so `####` stays inside and a
`##` row outside the subsection never counts.

Gate-registry row for SKILL.md (eight fields, conformant for `check_gate_registry.py`):

    | `verifiers/check_spec_craft.py` | gate | `python3 -B verifiers/check_spec_craft.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none | kotoba |

## Frozen readings (attack these, not the code)

The docstring lists all of them. The load-bearing ones:

* entry-absent returns `0 of 3`, exit 1, BEFORE any manifest access — this is what makes the
  plan's do-nothing control at base read `0 of 3` while a missing/tampered snapshot of an
  existing entry is exit 2;
* the tokens cell is the only token source, so a quote can never double as a token, and a
  single-character backticked span is not a token;
* tokens are matched literally: `scripts/` does not locate `scripts/validate.py`, and
  `.agents/skill` does not locate `.agents/skills/` (a slash-free token still matches when the
  page's `/` is the ASCII word boundary);
* the census is global: a non-conformant registry fails (b) for every page, so a row-level
  defect the census also rejects reads `0 of 3`, not `2 of 3`;
* the `quote` is the row's quote cell only (the `source:` line quote is not consulted).

## Evidence recorded by the builder

* `--self-test`: 76 worlds, 212 assertions, `0 failure(s)`, exit 0 (4.2 s wall).
* Do-nothing control at base `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` (fleet-shaped sandbox,
  `--shared` clone): `spec craft pages backed 0 of 3`, `held at base: 0`, exit 1.
* Live lane tip `329e7d91d7d750031c35d264f0e34af1d0ce8385`: `0 of 3`, exit 1 (the entry does not
  exist yet).
* A satisfying world committed inside a fleet-shaped sandbox over the REAL 148-row registry:
  `spec craft pages backed 3 of 3`, exit 0, 2.0 s wall (census included); `--repo .` relative
  form the same. Dangling `used-by` -> E11 -> `0 of 3`; rows appended outside `## Registry` ->
  E12 -> `0 of 3`. The snapshot bytes in that dry run are builder fixtures, so it proves the
  mechanics (census, pins, subsection, province), never that the real pages carry the tokens.
