# ExecSpecCounterR74 — C1 frozen counter `check_spec_craft.py`

Lane kotoba, round 74 wave 1. Seat scope: build the C1 counter exactly to plans/round-74.md § C1.
Read-only on every committed lane file; drafts under `.ufo/waves/round-74/w1/build/ExecSpecCounterR74/`.

## Verdict

**Built and self-tested green; the predicate is implemented as frozen and the do-nothing control
reads `0 of 3`, exit 1.** The counter is not yet exercised on claim data: the entry, the three
real page snapshots and the registry rows do not exist at any lane revision, which is the
sources/counters wave's work, not this seat's. What is proven here: the counter's mechanics
(six conjuncts, exit 1 vs exit 2, pins, census, SKILL.md act-on, province), the do-nothing figure
at base, and a `3 of 3` reachable over the REAL 148-row registry in a fleet-shaped sandbox with
builder-fixture snapshot bytes (those bytes are fixtures, not evidence about the pages).

Deliverables (the L1 lands both; I wrote no tracked file):

| file | sha256 | size |
|---|---|---|
| `.ufo/waves/round-74/w1/build/ExecSpecCounterR74/check_spec_craft.py` | `2ac18bedf3ab7e7767eeeddd68eaf7130139405b137e62f7ab677dd0a4e13840` | 69,686 B, 1,534 lines |
| `.ufo/waves/round-74/w1/build/ExecSpecCounterR74/README.md` | — | 6.3 KB, exact replay commands + landing shapes |

The in-file drift guard is frozen at blanked sha
`4065253e24f203772a30b6498101a77e4a88fca8a72aaa8377d71e46f42c39c8`.

## Evidence

**V1 — the self-test is green (76 worlds, 212 assertions, exit 0).**

```
$ python3 -B .ufo/waves/round-74/w1/build/ExecSpecCounterR74/check_spec_craft.py --self-test
PASS honest world scores 3 of 3: exit 0
PASS relative --repo . resolves before deriving (Q66): exit 0
PASS base world (entry absent) is the do-nothing control: exit 1
…
PASS base registry unreadable is exit 2: exit 2
self-test: 0 failure(s) over 212 assertions
SELFTEST_EXIT=0        (wall 4.2 s)
```
Every world is an isolated local git repo under a fresh `mktemp -d` with two commits; the
fixture's `git rev-parse --show-toplevel` equals the fixture dir before the first commit. Q48:
one satisfying world (exit 0 and the exact line `spec craft pages backed 3 of 3`) plus at least
one broken world per conjunct (a)-(f); (c) asserts exit 2 because the plan's (c) says so, every
other broken conjunct asserts exit 1. Q66: the relative `--repo .` world runs with the cwd set to
the fixture.

**V2 — the do-nothing control at base is `0 of 3`, exit 1** (fleet-shaped sandbox:
`/home/vgpnk/Projects/shokunin/*` symlinked except the lane, `git clone --shared` of the lane,
`checkout -q 1e03d19…`):

```
$ python3 -B <counter> --repo <sandbox>/kotoba-shokunin --rev 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
spec craft pages backed 0 of 3
held at base: 0
province core names the entry: no
  PROVINCE.md § Core does not name corpus/knowledge/spec-skill-creation-craft-round74.md (conjunct (f) holds for every page)
  entry corpus/knowledge/spec-skill-creation-craft-round74.md absent at 1e03d199… (the frozen path is the entry's only home)
EXIT=1        (wall 0.1 s)
```

**V3 — the live lane tip is `0 of 3`, exit 1** (read-only, real worktree):

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B <counter> --rev 329e7d91d7d750031c35d264f0e34af1d0ce8385 --repo .
measured-rev: 329e7d91d7d750031c35d264f0e34af1d0ce8385
spec craft pages backed 0 of 3
held at base: 0
EXIT=1
```

**V4 — `3 of 3` is reachable over the real 148-row registry** (same fleet-shaped sandbox; entry,
three registry rows, three snapshots + manifest, the SKILL.md subsection and the PROVINCE bullet
written into the clone, committed inside the clone only):

```
$ python3 -B <counter> --repo <sandbox>/kotoba-shokunin --rev HEAD
measured-rev: HEAD
spec craft pages backed 3 of 3
held at base: 0
province core names the entry: yes
  backed: best-practices
  backed: using-scripts
  backed: quickstart
EXIT=0        (wall 1.9–2.0 s, census included)
```
The snapshot bytes in that world are builder fixtures, so this proves the census/pin/subsection/
province plumbing on the real registry — never that the real pages carry the tokens.

**V5 — the census reads the whole tree, so E11 does not misfire on the real registry.** The
control seat reported E11 for all 148 base rows from a `--file` copy that holds only
`SOURCES.md`; my construction extracts `git archive <rev>` and resolves `used-by` against the
extracted tree:

```
$ git archive 1e03d19… | tar -x -C $T && bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file $T/corpus/SOURCES.md --today 2026-10-26
      1 ok
     20 W04
exit=0
```

**V6 — three falsifiers on the real registry** (each committed in the sandbox clone, then
`git reset --hard` back):

```
relative --repo .            -> spec craft pages backed 3 of 3, exit 0
dangling used-by on S224     -> spec craft pages backed 0 of 3, exit 1
                                (census E11; the S224 page also prints "used-by … does not list …")
rows moved outside ## Registry -> spec craft pages backed 0 of 3, exit 1 (census E12)
```

**V7 — the leak I found and killed (this is why the token reading is literal).** An earlier build
carried r73's trailing-slash token shaping (`scripts/` matched `scripts/validate.py`). Measured,
that made the plan's Q37 shortcut world score a pass:

```
FAIL (a) a token of another page's snapshot (Q37): exit 0 (want 1; …)
      output='…\nspec craft pages backed 3 of 3\n…'
```
By the plan's kill rule ("any shortcut world scoring 3 means the counter is wrong") the shaping
was the defect. It is removed: tokens are matched literally and ASCII-word-bounded on the
whitespace-collapsed snapshot. The same world now reads `2 of 3`, and two new worlds pin the
behaviour (`scripts/` does not locate `scripts/validate.py`; `.agents/skill` does not locate
`.agents/skills/`).

**V8 — base sweeps re-run by this seat, not accepted from the receipt** (the plan's held figure):

```
$ git rev-parse HEAD
329e7d91d7d750031c35d264f0e34af1d0ce8385
$ grep -cE 'agentskills\.io/skill-creation/(best-practices|using-scripts|quickstart)' corpus/SOURCES.md
0
$ grep -rniE 'calibrating control|defaults, not menus|favou?r procedures|fragility of the task|one-off commands|pipx run|uvx ruff' corpus SKILL.md PROVINCE.md | wc -l
0
```
So `held at base: 0` is the measured do-nothing figure, not an assumption.

**V9 — one prior artefact a critic should see, not counted by the counter.** A round-53 wave
build already records a fetch of the best-practices page: `.ufo/waves/round-53/build/ScribeDatedAuthority.md:116`
(`14,884 bytes`, `sha256 05173180a1be5ef1ca2e06cb79a1b38067763a4a8bc9a2eb1a989abcc0e37626`), with a
15-word located quote at `:32`. It is a build artefact, not a registry row and not guidance in
`SKILL.md`/`PROVINCE.md`, so the C1 ground statement stands; the sources seats can reuse it as a
second fetch record, and a wave-2 reviewer can attack "the lane does not hold the page".

## Conjunct implementation, and the readings a reviewer should attack

The docstring carries the full list. The load-bearing decisions, each with the reason it can
only fail more:

1. **Entry-absent returns `0 of 3`, exit 1, before any manifest read.** Without this ordering
   the plan's own do-nothing control would be exit 2 (no manifest at base exists). A missing or
   tampered snapshot of an EXISTING entry is exit 2, as (c) says.
2. **The `tokens` cell is the only token source** (>= 2 distinct: backticked spans of >= 2 chars,
   or double-quoted spans of >= 5 words). The `quote` cell is not a token source, so a quote
   cannot double as a token; a single-character backticked span is not a command or a path.
3. **The `S id` cell names exactly one id**; the row's first URL must be exactly
   `https://agentskills.io/skill-creation/<page>.md` (host equality, no subdomain; a different
   agentskills page fails), and the entry's own `source:` line for that id must carry that same
   host+path, so a pinned snapshot cannot be the wrong page.
4. **The census is global**: a non-conformant registry fails (b) for every page. Consequence,
   measured: the 12-cell row, the dangling used-by, the post-window `opened` and the duplicate-id
   worlds read `0 of 3` (not `2 of 3`) because the census also rejects them; the page-level
   finding is still printed. Counter worlds are asserted accordingly.
5. **`--today 2026-10-26` is passed to the census** so E08 is deterministic across the round-74
   window; the counter's own `opened` window (2026-10-25 or 2026-10-26) still rejects every date
   outside it. `opened: 2026-10-26` is an honest `3 of 3` world.
6. **Snapshot tokens and quotes are matched on the whitespace-collapsed snapshot** (the only
   shaping (d) names, and r73's family reading): a rule sentence wrapped across a line still
   locates; nothing else is shaped (no backtick stripping, no case folding).
7. **The SKILL.md heading is byte-exact** (em dash U+2014, ASCII apostrophe); a duplicated heading
   or a hyphen/curly-apostrophe variant is `0 of 3`. Rows counted: at least two per page, the
   action cell is the `action` column (else the last cell), >= 5 words, and it must itself carry
   a token of that page. A row outside the subsection (after the next `##`/`###`) never counts; a
   `####` sub-heading stays inside (both have worlds).
8. **Bounded (Q26/Q51):** the counter counts form, pins, cells, quotes and tokens. Whether a rule
   sentence is TRUE of the page, and whether the SKILL.md action is the right action, is a
   reviewer judgement this counter does not make; wave-2 reviewers must re-derive it.

## Landing requirements for the L1 (the counter enforces each)

* `corpus/knowledge/spec-skill-creation-craft-round74.md`: leading `source:` lines for every
  cited id, then `verified-at:`, then `recheck:`; a 6-column rule table
  `page | S id | rule | quote | tokens | action`, exactly one row per page, page names
  `best-practices`, `using-scripts`, `quickstart` (a trailing `.md` tolerated).
* `.ufo/waves/round-74/snapshots/{best-practices,using-scripts,quickstart}.md` +
  `.ufo/waves/round-74/snapshots/MANIFEST.sha256` (`<sha256>  <name>`; a key may carry the
  snapshot-directory prefix).
* `corpus/SOURCES.md`: three new 11-cell rows inside `## Registry`, `kind docs`, `tier A`,
  `status mined`, `opened 2026-10-25` (or `2026-10-26`), `recheck 90d`, `used-by` the entry path,
  first URL the page's own `https://agentskills.io/skill-creation/<page>.md`; the entry must be
  committed **in the same commit** (census E11 over `used-by`).
* `SKILL.md`: `### Body craft — the specification's skill-creation guides` with **>= 2 rows per
  page** (>= 6 rows; 10 lines with heading, blank, header, separator) and `| Page | Action |` (or
  any header carrying an `action` column). Budget: the plan reserved +14 lines; this shape fits.
* `PROVINCE.md` § Core: a `- ` bullet naming the entry path.
* `SKILL.md` § Gate registry row (8 fields, conformant for `check_gate_registry.py`):
  `| \`verifiers/check_spec_craft.py\` | gate | \`python3 -B verifiers/check_spec_craft.py --rev <rev>\` | 0=clean, 1=failed, 2=could-not-evaluate | \`--self-test\` | in-file | none | kotoba |`
* After ANY edit to the counter, refill `SELF_SHA` from `--print-self-sha`; while stale every
  measurement exits 2 with `environment error: counter drifted`.

## Bounds, not observed

* The three real pages were not fetched by this seat: their token/quote content, and therefore a
  real `3 of 3`, is unmeasured here. The Q45 census seat's count is what decides whether the
  target stays 3 (the counter requires each page to carry >= 2 literals and one 5–25-word quote
  the entry can use).
* No lane gate was run (wave-1 editing in flight; the L1 owns the battery). No network fetch, no
  install, no jj mutation, no tracked lane file written.
* The counter's exported surfaces are read from the measured revision's bytes only
  (`git show <rev>:<path>`); no instrument of the measured tree is executed (Q33).

## Tooling and scratch

No tool was installed or upgraded. Scratch: one fleet-shaped sandbox
`/tmp/k74fleet-ExecSpecCounterR74.w97exrxp` (symlinks + `--shared` clone; the only git writes
happened inside the clone, with a throwaway identity, and were reset), plus
`/tmp/k74selftest.out`, `/tmp/k74census.out`, `/tmp/k74sandbox.path` — all deleted before
returning. Self-test fixtures are `mktemp -d` dirs removed by each world.

## Checks the main agent should run after landing

1. `python3 -B verifiers/check_spec_craft.py --print-self-sha` — must print the frozen
   `SELF_SHA` above (else the landed bytes are not these bytes).
2. `python3 -B verifiers/check_spec_craft.py --self-test` — `0 failure(s) over 212 assertions`,
   exit 0.
3. `python3 -B verifiers/check_spec_craft.py --rev <data commit>` — the declared C1 figure.
4. `python3 -B verifiers/check_gate_registry.py --rev <tip>` and the tip battery (Q50/Q65).
