# ExecAuthorControls — C1 control worlds (round 72, wave 1)

Eleven committed bundles for the C1 predicate of `plans/round-72.md` § C1, built over the frozen
base `c69711ee08279609374d895bb0f3c8c18ccf15c9` (lane `kotoba-shokunin`, branch `master`).

**Verdict in one line:** the honest world reads `4 of 4` exit 0 and the base reads `0 of 4` exit 1,
all eight named shortcut worlds read below 4 — and **two worlds read `4 of 4` exit 0 without carrying
the rule**: `w9-token-list` (the frozen clause (a) tests token membership, not rule carriage) and
`w10-quote-echo-snapshot` (clause (d) cannot tell a page snapshot from a quote echoed back). Both are
kill-rule hits on the C1 counter, found before any data was scored.

Scores below are **measured** by `oracle_author_rules_literal.py` — this seat's literal reading of
the frozen predicate, because `verifiers/check_author_rules.py` did not exist when these bundles
were built (`ls verifiers | grep author` → `check_instruction_authority.py` only). The lane counter
belongs to another seat; the oracle is a draft the counter's author can diff against, not a
substitute for it.

## Layout

```
carrier/                        the honest overlay, shared by every world
  SKILL.md                      base + four rule boxes in § Trigger-fidelity checklist (616 lines)
  corpus/SOURCES.md             base + rows S255, S262, S263 (status mined, used-by = the entry)
  corpus/knowledge/resident-index-and-rungs-round72.md    the A4 entry (provenance trio, quotes)
  corpus/README.md              base + one coverage-map line for the entry
  .ufo/waves/round-72/snapshots/   S255/S262/S263 captures + <id>.sha256 pins + pins.json
<world>/README.md               what the world is, the clause it should trip, the prediction
<world>/delta.patch             one unified diff against carrier (the single-clause defect)
<world>/.ufo/waves/round-72/snapshots/   only for the two snapshot worlds (pins recomputed)
oracle_author_rules_literal.py  the literal (a)-(d) reading used to score every world
replay.sh                       build + commit + score one world in a throwaway --shared clone
gen.py                          regenerates carrier/ and every delta from the base bytes
```

## Replay

```sh
cd .ufo/waves/round-72/w1/build/ExecAuthorControls
bash replay.sh honest                 # -> 4 of 4, exit 0
bash replay.sh w9-token-list          # -> 4 of 4, exit 0   (the hole)
bash replay.sh w6-a4-quote-absent     # -> 3 of 4, exit 1
```

`replay.sh` clones the lane with `--shared` into `$D/kotoba-shokunin` (so the clone directory carries
the lane's own name and `trigger.name_directory` is not a sandbox artifact), checks out the base,
asserts `git rev-parse --show-toplevel` equals the clone, copies `carrier/`, copies the world's own
overlay files, applies `delta.patch`, commits inside the clone under a throwaway identity, and runs
the oracle at `--rev HEAD`. The lane is only read. Set `LANE=` / `BASE=` to point elsewhere.

## The honest overlay — what the four boxes carry

| rule | frozen tokens | the rule as written | tail |
|---|---|---|---|
| A1 | `name` `unique` `precedence` | no client merges two same-named skills; four of five routes order the collision and one order reverses, so the name must be unique, not ladder-resolved | `S203, S207` → `skill-name-precedence-round69.md` |
| A2 | `authority` `level` `body` | a `SKILL.md` body is not a privileged instruction: say the level, and that a higher authority overrides it | `S123, S129` → `instruction-authority-ladder-round67.md` |
| A3 | `install` `trust` `command` | a skill that runs a command executes repository-controlled instructions: name the install path and the gate it cleared | `S198, S200, S208` → `client-trust-gates-round68.md` |
| A4 | `prompt` `always-on` `skill` `index` | one-off prompt / skill / always-on index, by reuse and specificity, with the always-on surface an index not a payload | `S255, S262, S263` → `resident-index-and-rungs-round72.md` |

The A4 rows were re-fetched and pinned by this seat on 2026-10-25; every located quote was re-found
in the pinned bytes before the world was committed:

```
$ bash fetch.sh
S255  https://agentskills.io/skill.md  16035 bytes  status 200
S262  https://docs.factory.ai/cli/configuration/skills.md  17567 bytes  status 200
S263  https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md  4793 bytes  status 200
```

Three independent fetches (two by this seat, and the captures a sibling seat had already made under
the lane's `.ufo/waves/round-72/snapshots/`) agree byte-for-byte, so the carrier adopts that
directory's names and pin convention — `<id>-<slug>.md` plus an `<id>.sha256` file of
`sha256  filename` lines — rather than a second convention:

```
624f1c7f14a89481823f156aad5b665064a3c595cd9682e73c26f48db88994fc  S255-agent-skills-skill-md.md
81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9  S262-factory-droid-skills.md
5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5  S263-pi-skills.md
```

Located quotes, each ≤25 words: S255 "at startup they load only the name and description of each
skill (~50-100 tokens per skill)" (16 words); S262 "Use skills when instructions are too specific
for always-on \`AGENTS.md\`" (10 words); S263 "Pi advertises each available skill by name and
description, then loads its full instructions only when the task calls for them." (20 words).

## The worlds

| world | mutation | clause it should trip | predicted | measured |
|---|---|---|---|---|
| `honest` | none — the carrier verbatim | — (the exit-0 arm) | 4 of 4, exit 0 | **4 of 4, exit 0** |
| `w1-queued-rows` | the three A4 rows: status `mined` → `queued`, used-by intact | (b) status | 3 of 4, exit 1 | **3 of 4, exit 1** — `A4: (b) S255: status=queued; S262: status=queued; S263: status=queued` |
| `w2-used-by-omits` | row S262: used-by → `—`, status stays `mined` | (b) used-by | 3 of 4, exit 1 | **3 of 4, exit 1** — `A4: (b) S262: used-by omits entry` |
| `w3-html-comment` | the four boxes wrapped in `<!-- … -->` | (a) rendered bytes | 0 of 4, exit 1 | **0 of 4, exit 1** |
| `w4-fenced` | the four boxes inside a ``` fence | (a) rendered bytes | 0 of 4, exit 1 | **0 of 4, exit 1** |
| `w5-outside-section` | the four boxes moved to the end of § Sources | (a) section | 0 of 4, exit 1 | **0 of 4, exit 1** |
| `w6-a4-quote-absent` | S262 snapshot truncated to five lines, pins recomputed over the truncation | (d) quote-in-snapshot | 3 of 4, exit 1 | **3 of 4, exit 1** — `A4: (d) S262 quote absent from snapshot` |
| `w7-unknown-id` | A1 tail cites `S999` beside the real `S203` | (b) registry row | 3 of 4, exit 1 | **3 of 4, exit 1** — `A1: (b) S999: no registry row` |
| `w8-entry-no-trio` | the A4 entry keeps `source:` lines, loses `verified-at:`/`recheck:` | (c) provenance | 3 of 4, exit 1 | **3 of 4, exit 1** — `A4: (c) no verified-at:/recheck:` |
| `w9-token-list` | the four boxes replaced by their token sets alone, honest tails | (a) as frozen cannot | 4 of 4, exit 0 | **4 of 4, exit 0 — HOLE** |
| `w10-quote-echo-snapshot` | S262 snapshot replaced by a one-line echo of the quote, pin recomputed | (d) as frozen cannot | 4 of 4, exit 0 | **4 of 4, exit 0 — HOLE** |

Base do-nothing control (measured with the same oracle):

```
$ python3 -B oracle_author_rules_literal.py --repo <clone of c69711e> --rev c69711ee08279609374d895bb0f3c8c18ccf15c9
  A1: (a) candidates=0
  A2: (a) candidates=0
  A3: (a) candidates=0
  A4: (a) candidates=0
author-facing rules in SKILL.md 0 of 4
exit=1
```

The two exit-2 branches were exercised on the `w10` sandbox (not committed as worlds):

```
  ENV (d) S262 snapshot sha256 dd3c8e33f1df != pin (S262-factory-droid-skills.md)   -> exit 2
  ENV (d) S262 snapshot absent: S262-factory-droid-skills.md                        -> exit 2
```

## Headline — the two worlds that read 4 of 4 without carrying the rule

**`w9-token-list`.** Boxes of the form

```
- [ ] `name` `unique` `precedence`.
      (sourced: S203, S207; entry: corpus/knowledge/skill-name-precedence-round69.md)
```

Conjunct (a) asks only that the box's joined text "carries the rule's token set as whole words" and
"ends with the tail". Both hold; (b) and (c) hold because the apparatus underneath is honest. **The
clause that should have caught it is (a) itself** — "carries the rule's token set" is a membership
test, and membership is not carriage: the frozen sentence has no conjunct that an executing agent
could act on. The plan's own framing ("four rules an executing agent can act on") is the unmet
intent, and a critic needs no fabrication to reach it — the four tails are copyable from the honest
boxes, and the tokens are the predicate's own words.

Minimal repairs that keep the predicate a predicate (for the counter's author, before data):
1. freeze, per rule, one *sentence fragment* the box must contain (e.g. A1 "do not rely on any
   client's precedence ladder"), so the test is text the agent acts on, not vocabulary; or
2. require the box to contain an action cell — a frozen verb set (`do`, `never`, `say`, `name`,
   `pick`) plus a frozen object per rule — and drop the bare token-set test.

Either way the token test as written cannot be load-bearing alone, and `w9` is the receipt.

**`w10-quote-echo-snapshot`.** A snapshot file whose entire content is the located quote, pinned by
an honest sha256. Conjunct (d) holds: the quote *is* word-bounded in a committed, sha256-pinned file
under `snapshots/`. Nothing in (d) reads the snapshot's size, its URL, or its shape — so a critic
can satisfy "a snapshot of the cited page" with the page's own quote. The clause that should have
caught it is (d): it needs a provenance conjunct (the pin record must name the fetched URL and a
byte count that a 60-byte echo cannot meet, or the snapshot must be ≥ some frozen floor and carry
the page's own header). `w6` shows the same clause catching the *opposite* defect (a real page
capture that lost the quote), so (d) is load-bearing in one direction only.

## Counter readings the predicate does not fix (each is a place two honest counters diverge)

1. **"the quote cell" does not exist.** The 11-cell registry row has no quote cell; the located quote
   lives inside `anchor` after the literal marker `quote `. The oracle reads `quote\s+"…"`. A counter
   that instead takes the *first* quoted span of `anchor` fails the honest world: S255's anchor opens
   with the section label `"Product summary"` (2 words), below the frozen 5–25-word floor. Observed:
   `A4: (d) S255 quote 2 words` before the oracle was corrected. The counter must freeze one reading.
2. **A1–A3 have no snapshot check.** (d) is A4-only, so the three rule texts sourced from entries
   already held can be fabricated while (a)–(c) hold; only A4's quote is pinned. If (d) is meant to
   be the anti-fabrication conjunct, it is scoped to a quarter of the claim.
3. **No date floor in (c).** `verified-at:` and `recheck:` must exist, not be recent: a
   `verified-at: 1999-01-01` entry passes (c) unchanged.
4. **"inside `## Trigger-fidelity checklist` (up to the next `## ` heading)"** presumes one such
   heading. A second heading of the same name makes first-match and last-match counters score
   different files; the oracle takes the first.
5. **Pin granularity is unstated.** An id may pin more than one capture (the lane's S263 set already
   holds the skills page plus two support pages); the oracle verifies every pinned file of a cited id
   and requires the quote in at least one. A counter that instead demands the quote in *the* single
   snapshot must say which file that is.
6. **Snapshot normalization is unstated.** The factory page's served `.md` carries backticks the
   staged row cell drops (`always-on \`AGENTS.md\`` vs `always-on AGENTS.md`); the honest world pins
   the served bytes and carries the backticks in the cell. A counter that normalizes the snapshot by
   stripping backticks would fail the honest world and pass a stripped cell — the normalization has
   to be named in the predicate, not chosen by each instrument (Q42).

## Integration cost, measured (for the L1, not done here)

The honest overlay is `616` lines of `SKILL.md` against the frozen 600-line budget, and the lane's
own checklist instrument sees exactly two new FAILs relative to the base clone:

```
$ cd <honest sandbox>/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py --json
checklist.box_map_complete FAIL | unmapped box at line 327 (sha256 cd0e2cd95318…); … line 331 (b177aaf39d52…); … line 335 (0f3f2e82a6a8…); … line 339 (d57fcec94639…)
trigger.line_budget       FAIL | 616 lines exceed budget 600 (from box at line 320)
pass 7 of 11
$ cd <base clone>/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py --json
pass 9 of 11          # both FAILs there are trigger.citation_resolves / governance.citation_resolves,
                      # the ../ fleet-root artifacts of a bare /tmp clone — the honest world inherits them
```

So landing the four boxes needs **16 non-box lines freed** (touching box text is not an option: the
baseline pins every box by text hash) and **four new entries in `verifiers/checklist-baseline.json`**
mapped to each box's sha256. Neither is a control-world change; both are landing work.

The registry append is clean under the fleet census validator once the staged cells are normalized
(see the next section): 0 E codes, the same 20 pre-existing W04 warnings as the base, exit 0.

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate <honest sandbox> --root <honest sandbox>
honest census exit=0   # 0 lines matching TAB E, 20 lines matching TAB W
```

## Two defects in the staged inputs (found while building the carrier)

1. **The staged `recheck` cells are E09-invalid.** `SOURCES.append.md` carries
   `90d — re-fetch the raw file and confirm … (ran 2026-10-23)` in the cell; the fleet validator
   accepts only a bare cadence, so an append copied verbatim is rejected:

   ```
   kotoba-shokunin  E09  S263 recheck=90d — re-fetch the raw file and confirm the advertise-then-load sentence and the decision boundary are unchanged (ran 2026-10-25)
   ```

   `gen.py` keeps the cadence (`90d`) and drops the prose; the prose belongs on the entry's own
   `recheck:` line, where it already is.
2. **The staged S262 quote cell drops backticks the served bytes carry.** The row says
   `always-on AGENTS.md`; the served `.md` says ``always-on `AGENTS.md` ``. A snapshot pinned to the
   served bytes therefore fails a literal quote search against the staged cell — which is exactly
   what (d) checks. The carrier's cell carries the backticks. This is a normalization the predicate
   must name (Q42), not a choice each instrument makes.

## What is NOT verified here

- The lane counter's reading. Every score above is the oracle's; if `check_author_rules.py` freezes
  a different reading of "the quote cell", "rendered", or the pin format, the scores move and the
  oracle should be diffed against it first.
- The snapshots are this seat's fetches of 2026-10-25, byte-identical to the sibling seat's captures
  already in the lane; the sha256s are in `carrier/.ufo/waves/round-72/snapshots/<id>.sha256` and
  `pins.json`. `docs.factory.ai/cli/configuration/skills` answers `308` to
  `docs.factory.com/harness/skills`, so the pinned bytes are the page's own `.md` sibling at the
  cited path.
- The four boxes are a draft. They carry the rules the plan names, but the rule wording is this
  seat's, and the entry body is a draft the L1 owns.
