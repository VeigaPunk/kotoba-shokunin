# ExecAuthorControls — C1 control worlds (round 72, wave 1)

**Verdict.** Eleven bundles are built under
`.ufo/waves/round-72/w1/build/ExecAuthorControls/` over base `c69711ee08279609374d895bb0f3c8c18ccf15c9`,
and every one is measured, not predicted: the honest world reads `4 of 4` exit 0, the base reads
`0 of 4` exit 1, all eight worlds the plan names read below 4 — and **two worlds read `4 of 4`
exit 0 without carrying the rule**: `w9-token-list` (clause (a) tests token membership, not rule
carriage) and `w10-quote-echo-snapshot` (clause (d) cannot tell a page snapshot from a quote echoed
back). Both are kill-rule hits on the C1 counter, found before any data was scored.

Axes worked: **depth** — the frozen predicate has two holes and six readings it leaves open, each
shown with a world or a measurement rather than asserted; **calibration** — predicted and measured
scores agree for all eleven worlds, the base and honest arms are both exercised, the exit-2 branches
are exercised, and the honest world's landing cost is measured against the lane's own instrument.

The counter `verifiers/check_author_rules.py` does not exist at the base, so every score below comes
from `oracle_author_rules_literal.py`, this seat's literal reading of the frozen sentence (its
readings are named in its docstring so the counter's author can diff against it):

```
$ ls verifiers | grep -i author
check_instruction_authority.py
```

## What was built

```
.ufo/waves/round-72/w1/build/ExecAuthorControls/
  carrier/        honest overlay: SKILL.md (600 -> 616 lines, four rule boxes), corpus/SOURCES.md
                  (+S255, S262, S263), corpus/knowledge/resident-index-and-rungs-round72.md (46 lines),
                  corpus/README.md (+1 coverage-map line), .ufo/waves/round-72/snapshots/ (3 captures
                  + <id>.sha256 pins + pins.json)
  honest/ w1-queued-rows/ w2-used-by-omits/ w3-html-comment/ w4-fenced/ w5-outside-section/
  w6-a4-quote-absent/ w7-unknown-id/ w8-entry-no-trio/ w9-token-list/ w10-quote-echo-snapshot/
                  each: README.md (mutation, clause, prediction) + delta.patch (or overlay files for
                  the two snapshot worlds)
  oracle_author_rules_literal.py   the (a)-(d) reading used to score
  replay.sh       clone --shared -> checkout base -> carrier -> delta -> commit -> score
  gen.py          regenerates carrier/ and every delta from the base bytes
  fetch.sh        re-fetches the three snapshots (records HTTP status per capture)
```

Replay is one command per world and writes only inside the throwaway clone:

```
$ bash replay.sh honest
== honest  (sandbox /tmp/k72w1-ExecAuthorControls.replay.FIqNap/kotoba-shokunin)
author-facing rules in SKILL.md 4 of 4
exit=0
```

`replay.sh` asserts `git rev-parse --show-toplevel` equals the clone before its first commit and
commits under a throwaway identity inside that clone only.

## Measured scores (all eleven, plus the base)

| world | mutation | measured |
|---|---|---|
| base `c69711e` (do-nothing) | — | `0 of 4`, exit 1 — `A1..A4: (a) candidates=0` |
| `honest` | carrier verbatim | **`4 of 4`, exit 0** |
| `w1-queued-rows` | the three A4 rows `mined` -> `queued` | `3 of 4`, exit 1 — `A4: (b) S255: status=queued; S262: status=queued; S263: status=queued` |
| `w2-used-by-omits` | S262 `used-by` -> `—` | `3 of 4`, exit 1 — `A4: (b) S262: used-by omits entry` |
| `w3-html-comment` | boxes inside `<!-- … -->` | `0 of 4`, exit 1 — `A1..A4: (a) candidates=0` |
| `w4-fenced` | boxes inside a ``` fence | `0 of 4`, exit 1 — `A1..A4: (a) candidates=0` |
| `w5-outside-section` | boxes at the end of § Sources | `0 of 4`, exit 1 — `A1..A4: (a) candidates=0` |
| `w6-a4-quote-absent` | S262 snapshot truncated to five lines, pin recomputed | `3 of 4`, exit 1 — `A4: (d) S262 quote absent from snapshot` |
| `w7-unknown-id` | A1 tail cites `S999` beside `S203` | `3 of 4`, exit 1 — `A1: (b) S999: no registry row` |
| `w8-entry-no-trio` | entry loses `verified-at:`/`recheck:` | `3 of 4`, exit 1 — `A4: (c) no verified-at:/recheck:` |
| `w9-token-list` | token-only boxes, honest tails | **`4 of 4`, exit 0 — HOLE** |
| `w10-quote-echo-snapshot` | snapshot = the quote echoed back, pin honest | **`4 of 4`, exit 0 — HOLE** |

Each world isolates one clause: `w1` keeps `used-by` intact so only `status` can catch it; `w2` keeps
`status` mined so only the back-link can; `w6` recomputes the pin over the truncated bytes so the
failure is quote-absence, not a tamper; `w7` cites a real id beside the fake one so (a) still passes.

The two exit-2 branches were exercised on the `w10` sandbox (not committed as worlds):

```
  ENV (d) S262 snapshot sha256 dd3c8e33f1df != pin (S262-factory-droid-skills.md)   -> exit 2
  ENV (d) S262 snapshot absent: S262-factory-droid-skills.md                        -> exit 2
```

## Headline — the two worlds that read 4 of 4 without carrying the rule

**`w9-token-list` — the cheapest real-input shortcut.** The four boxes are replaced by their token
sets alone, e.g.

```
- [ ] `name` `unique` `precedence`.
      (sourced: S203, S207; entry: corpus/knowledge/skill-name-precedence-round69.md)
```

Clause (a) asks that the box's joined text "carries the rule's token set as whole words" and "ends
with the tail". Both hold; (b) and (c) hold because the apparatus underneath is honest; (d) does not
apply to A1–A3. **The clause that should have caught it is (a) itself**: "carries the rule's token
set" is a membership test, and membership is not carriage. The critic needs no fabrication — the
four tails are copyable from any honest box and the tokens are the predicate's own words. The plan's
framing ("four rules an executing agent can act on") is the intent (a) does not encode.

Minimal repairs that stay checkable (for the counter's author, before data):
1. freeze one *sentence fragment* per rule that the box must contain (e.g. A1 "do not rely on any
   client's precedence ladder"), so the test is text an agent acts on rather than vocabulary; or
2. require a frozen action cell per rule (verb set `do|never|say|name|pick` + a frozen object) and
   drop the bare token test.

**`w10-quote-echo-snapshot` — (d) has no provenance conjunct.** The S262 snapshot is a one-line file
whose entire content is the located quote, pinned by an honest sha256. (d) holds: the quote is
word-bounded in a committed, sha256-pinned file under `snapshots/`. Nothing in (d) reads the
snapshot's size, its URL or its shape. **The clause that should have caught it is (d)**: it needs a
provenance conjunct (the pin record must name the fetched URL and a byte count a 60-byte echo cannot
meet) or a frozen floor plus a page-own-header requirement. `w6` shows (d) load-bearing in the
opposite direction only, so the clause guards a lost quote, not a fabricated snapshot.

## Six readings the predicate leaves open (each observed, each a divergence between honest counters)

1. **"the quote cell" does not exist.** The 11-cell registry row has no quote cell; the located quote
   lives inside `anchor` after the literal marker `quote `. The oracle reads `quote\s+"…"`. A counter
   that takes the *first* quoted span of `anchor` fails the honest world, because S255's anchor opens
   with the section label `"Product summary"` — observed before the oracle was corrected:
   `A4: (d) S255 quote 2 words`. One reading must be frozen.
2. **A1–A3 are never snapshot-checked.** (d) is A4-only, so the three rule texts sourced from entries
   already held can be fabricated while (a)–(c) hold. If (d) is the anti-fabrication conjunct, it
   covers a quarter of the claim.
3. **No date floor in (c).** `verified-at:` and `recheck:` must exist, not be recent: a
   `verified-at: 1999-01-01` entry passes (c) unchanged.
4. **"inside `## Trigger-fidelity checklist` (up to the next `## ` heading)"** presumes exactly one
   such heading; a second one makes first-match and last-match counters score different files (the
   oracle takes the first).
5. **Pin granularity is unstated.** The lane's S263 snapshot set already holds the skills page plus
   two support pages, so "a snapshot of the cited page" is ambiguous at id granularity. The oracle
   verifies every pinned file of a cited id and requires the located quote in at least one of them;
   a counter that demands *the* single snapshot must say which file that is.
6. **Snapshot normalization is unstated.** See the S262 backtick defect below: whether the snapshot
   is compared with or without backticks decides the honest world's verdict.

## Two defects in the staged assimilation inputs (found while building the carrier)

1. **The staged `recheck` cells are E09-invalid.** Copying `SOURCES.append.md`'s cell verbatim
   (`90d — re-fetch … (ran 2026-10-23)`) makes the fleet validator reject the append:

   ```
   $ bash scripts/sources-census.sh validate <sandbox> --root <sandbox>
   kotoba-shokunin  E09  S263 recheck=90d — re-fetch the raw file and confirm the advertise-then-load sentence and the decision boundary are unchanged (ran 2026-10-25)
   ```

   `sources-census.sh:664-666` accepts only `NNd`, an ISO date, or a symbolic cadence in that cell.
   The carrier keeps `90d`; the prose belongs on the entry's own `recheck:` line, where it is.
   After the normalization: 0 E codes, the same 20 pre-existing W04 warnings as the base, exit 0.
2. **The staged S262 quote cell drops backticks the served bytes carry.** The row says
   `always-on AGENTS.md`; the served `.md` says ``always-on `AGENTS.md` `` — so a snapshot pinned to
   the served bytes fails a literal quote search against the staged cell, which is exactly (d). The
   carrier's cell carries the backticks. This is a normalization the predicate must name (Q42).

## The honest world, and what landing it costs

The four boxes carry the rules, one per frozen token set:

| rule | box text (first clause) | tail |
|---|---|---|
| A1 | no client merges two same-named skills — four of the five cited routes order the collision and one order reverses, so the name must be unique | `S203, S207` -> `skill-name-precedence-round69.md` |
| A2 | a `SKILL.md` body is not a privileged instruction — say the level, and that a higher authority overrides it | `S123, S129` -> `instruction-authority-ladder-round67.md` |
| A3 | a skill that runs a command executes repository-controlled instructions — name the install path and the gate it cleared | `S198, S200, S208` -> `client-trust-gates-round68.md` |
| A4 | one-off prompt / skill / always-on index, by reuse and specificity, with the resident surface an index not a payload | `S255, S262, S263` -> `resident-index-and-rungs-round72.md` |

The A4 rows were re-fetched and pinned by this seat; all located quotes were re-found in the pinned
bytes (≤25 words each, quoted from the fetched bytes):

```
$ bash fetch.sh    # writes $FETCHED/S255-agent-skills-skill-md.md, …/S262-factory-droid-skills.md, …/S263-pi-skills.md
S255  https://agentskills.io/skill.md  16035 bytes  status 200   "at startup they load only the name and description of each skill (~50-100 tokens per skill)"
S262  https://docs.factory.ai/cli/configuration/skills.md  17567 bytes  status 200   "Use skills when instructions are too specific for always-on `AGENTS.md`"
S263  https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md  4793 bytes  status 200   "Pi advertises each available skill by name and description, then loads its full instructions only when the task calls for them."
```

A second and third fetch reproduced all three sha256s byte-for-byte, and a sibling seat's captures
already in the lane at `.ufo/waves/round-72/snapshots/` (`S255-agent-skills-skill-md.md`,
`S262-factory-droid-skills.md`, `S263-pi-skills.md`) are the same bytes — three independent fetches,
one answer. The carrier therefore adopts that directory's names and pin convention (`<id>-<slug>.md`
plus an `<id>.sha256` file of `sha256  filename` lines) instead of inventing a second one, so the L1
can land the carrier's three files into the existing directory as a no-op copy:

```
624f1c7f14a89481823f156aad5b665064a3c595cd9682e73c26f48db88994fc  S255-agent-skills-skill-md.md
81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9  S262-factory-droid-skills.md
5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5  S263-pi-skills.md
```

`docs.factory.ai/cli/configuration/skills` answers `308` to `docs.factory.com/harness/skills`, so the
pinned bytes are the page's own `.md` sibling at the cited path, not a rendered HTML page.

Landing cost, measured against the lane's own instrument rather than asserted:

```
$ cd <honest sandbox>/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py --json
checklist.box_map_complete FAIL | unmapped box at line 327 (…sha256 cd0e2cd95318…); … 331 (b177aaf39d52…); … 335; … 339
trigger.line_budget       FAIL | 616 lines exceed budget 600 (from box at line 320)
pass 7 of 11
$ cd <base clone>/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py --json
pass 9 of 11     # both FAILs there are the ../ fleet-root citation checks, which the honest world inherits
```

So the boxes cost **16 non-box lines freed** (box text cannot move: the baseline pins every box by
text hash) and **four entries in `verifiers/checklist-baseline.json`** mapped to the four box
sha256s. Both are landing work for the L1, not control-world changes, and neither was done here.

## Contract compliance

- Wrote only: this report, `build/ExecAuthorControls/**`, and scratch under
  `/tmp/k72w1-ExecAuthorControls.*` (deleted before returning). No committed lane file, no jj state,
  no lane index, no fleet repo, no sibling lane, no `/home/vgpnk/Projects/shokuknow` write.
- Lane state after the wave-1 work: `git log --oneline -1` -> `e61fd29`; `git status --porcelain` -> 6
  untracked entries: `.ufo/waves/round-72/w1/` (which holds this report and the build tree — the only
  one that is mine), `.ufo/waves/round-72/snapshots/` (a sibling seat's captures, used read-only),
  `w1.ready` and `w1.ready.dispatched` (the L1's dispatch), and two `verifiers/fixtures/oc2-v2.1.4-*.txt`
  from the C2 seat. No tracked file is modified.
- `git diff --stat c69711e e61fd29 -- SKILL.md corpus/` is empty: overlaying either revision gives the
  same `SKILL.md` and corpus, so the assignment's base is the plan's base for this surface.
- No tool installed or upgraded (no `uv tool`, `npx`, binary download, or pacman call was made).
- **One scratch-cleanup mistake, repaired and verified.** My cleanup used `rm -rf /tmp/k72w1-ExecAuthorControls.*
  /tmp/k72-*.md /tmp/k72-*.html /tmp/k72-*.txt`, whose last two globs also matched the *shared* input
  dumps `/tmp/k72-omp-strings.txt` and `/tmp/k72-oc-strings.txt`. Both were deleted and both were
  restored by re-running the same command on the same binaries:

  ```
  $ strings -n 4 ~/.local/bin/omp.real > /tmp/k72-omp-strings.txt
  $ strings -n 4 ~/.opencode/bin/opencode > /tmp/k72-oc-strings.txt
  $ sha256sum /tmp/k72-omp-strings.txt /tmp/k72-oc-strings.txt
  953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f  /tmp/k72-omp-strings.txt
  020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089  /tmp/k72-oc-strings.txt
  ```

  Both match the sha256 prefixes the round brief states for those dumps (`953b19df…`, `020fb253…`),
  so the restored files are byte-identical to the ones deleted; the window was under a minute and no
  other seat's scratch was touched.

## What is not verified here

- The lane counter's reading of (a)–(d). Every score is the oracle's; if `check_author_rules.py`
  freezes a different reading of "the quote cell", "rendered", or the pin format, the scores move and
  the oracle should be diffed against it first.
- The snapshots are this seat's fetches of 2026-10-25, byte-identical to the sibling seat's captures
  already in the lane (three independent fetches, one answer); the entry body is a draft the L1 owns.
- The A4 rule's `index` half rests on S255's resident-cost sentence. S248's degradation side was
  fetched and read but deliberately **not** cited in the honest world: its third quoted span
  ("A compressed 8KB docs index embedded directly in `AGENTS.md` …") resolves in the page only after
  inline code is rendered back to backticks, so citing it would import the same normalization problem
  as the S262 cell. Not a claim either way.
