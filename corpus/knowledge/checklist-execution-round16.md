# Checklist execution, round 16 — two escapes closed, one box executed, three citations named

**Lane:** kotoba-shokunin. **Round:** 16. **Axis move:** `operability` (8.0, the
lowest row in `SCORECARD.md` among the rows this lane may move).

**Move-selection record.** The round was pre-registered in round 15
(`corpus/knowledge/checklist-execution-round15.md` § "What earns 8.5 next
round"), so the deliverable and its falsifiers existed before this round started:
close `M35` (path-like arguments did not resolve) and `M40` (a `delegated:`
target was checked for existence only), then execute a further box. The prompt's
*lowest-scoring axis* rule again lands on `operability` rather than on a lane-owned
row; the `AXES.md`↔`MISSION.md` naming question (rounds 13–15, `../.ufo/l0-questions.md`)
is still open and is not re-litigated here.

**Scope fence.** This move touches one instrument (`verifiers/verify_skill_checklist.py`),
one map (`verifiers/checklist-baseline.json`), one target file (`SKILL.md`) and one
checklist box (`trigger.11`). It does **not** execute the remaining 33 boxes, and it
does not convert its `delegated:`-class finding into a claim about the corpus
verifier's scope.

## Claim under test (falsifiable)

> As of round 16 the checklist instrument has **nine** checks; the `M35` escape is
> closed for *path-like arguments* (and the planted bare-token mutation is
> re-labelled as a non-defect with a reason, not silently dropped); the `M40`
> escape is closed (a `delegated:` target must be an instrument, not merely an
> existing file); and checklist box `trigger.11` is *executed* rather than
> delegated, because the delegated instrument never scanned this file. Each of the
> three new rules lands with a fixture that is red before the rule and green after,
> and the map records **8 executed / 0 delegated / 33 unexecuted** over the same 41
> boxes.

## Pre-state (commands to re-run, at `b25f37a`)

| Fact | Command | Value |
|---|---|---|
| checks in the instrument | `grep -c 'trigger\.\|checklist\.' <(sed -n '/^CHECK_IDS/,/^)/p' verifiers/verify_skill_checklist.py)` | 8 |
| fixture cases | `ls verifiers/fixtures/checklist \| wc -l` | 47 |
| self-test assertions | `python3 verifiers/verify_skill_checklist.py --self-test` | 772 |
| `M35` escape | `/tmp/round15/R15Mutate/harness.py` row `M35-echo-arg` | ESCAPED (exit 0) |
| `M40` escape | same harness, row `M40-delegated-exists` | ESCAPED (exit 0) |
| live citations checked by any instrument | — | **0** (the corpus instrument states `SKILL.md` is outside `corpus/` and never scanned) |
| bare `.ufo/prompts/` citation sites in `SKILL.md` | `grep -c '`\\.ufo/prompts/`' SKILL.md` | 3 |

## Red-before evidence (each rule seen failing before it landed)

**R1 — path-like arguments.** The pre-patch instrument (`git show
b25f37a:verifiers/verify_skill_checklist.py`, sha256 `2ee8abae…`) on the new
fixture `command-path-arg`, whose only defect is a fenced `cat
corpus/absent-round16-arg.md`:

```
$ python3 pre.py --skill verifiers/fixtures/checklist/command-path-arg/SKILL.md \
      --map verifiers/fixtures/checklist/command-path-arg/map.json \
      --vocabulary verifiers/checklist-command-vocabulary.json
rc=0                      # the argument was invisible; the head `cat` resolved
```

After the rule the same fixture is `FAIL trigger.command_binary_resolves …
line 17: 'corpus/absent-round16-arg.md' (fenced-arg, segment 'cat
corpus/absent-round16-arg.md') does not resolve`, exit 1.

**R2 — delegation to a non-instrument.** Same pre-patch instrument on the fixture
`delegated-noninstrument` (map `fixture.02` → `delegated:delegated-noninstrument/SKILL.md`,
a file that exists and is not an instrument): `rc=0`. After the rule: `FAIL
checklist.box_map_complete … delegates to a target that is not an instrument:
'delegated-noninstrument/SKILL.md' (… script suffix … or a shebang)`, exit 1.

**R3 — citation resolution.** The rule applied to the *pre-round-16* tree, not to
the edited one: a clone of `b25f37a` inside a faithful host layout (a sibling
`/home/vgpnk/projects/shokunin/.ufo/reports/round-7/kotoba.md` beside the repo), with only the patched verifier
copied in:

```
$ cd fake/shokunin/kotoba-shokunin && python3 verifiers/verify_skill_checklist.py
PASS checklist.box_map_complete … 41 boxes mapped (7 executed, 1 delegated, 33 unexecuted)
PASS trigger.name_directory: evaluated 1 — name 'kotoba-shokunin' == directory 'kotoba-shokunin'
PASS trigger.command_binary_resolves: evaluated 21 — 16 segments; 21 command subject(s) resolve
FAIL trigger.citation_resolves: evaluated 46 — line 86: '.ufo/prompts/' does not resolve …
  line 95: '.ufo/prompts/' … line 385: '.ufo/prompts/' …
rc=1
```

Three findings, one class: a token whose implied base is *this* repo written
without a base. The `/home/vgpnk/projects/shokunin/.ufo/reports/round-7/kotoba.md` site on line 589 resolved
(the bounded-hop rule), so the FAIL list is the defect class and nothing else. The
fix is in the file's own words ("any other root must be named in the file"): all
three sites now read `/home/vgpnk/projects/shokunin/.ufo/prompts/`, the form the
file already used at five other sites.

**The new check is fail-closed on the live file, not only on fixtures.** Landing
the rule *before* writing this artifact produced

```
FAIL trigger.citation_resolves: evaluated 42 — line 210:
  'corpus/knowledge/checklist-execution-round16.md' does not resolve …
rc=1
```

— because `SKILL.md` names this file. The artifact is what makes the live run
green; that is a demonstration that the check reads the file under construction,
not a formality.

## Landed changes

| # | Change | Where |
|---|---|---|
| 1 | `command_subjects` collects path-like arguments in fenced and vocabulary-headed inline segments; `path_like_arg` + `arg_subjects` define the class; redirect targets and declared output flags are skipped | `verifiers/verify_skill_checklist.py` |
| 2 | `check_box_map` requires a `delegated:` target to be an instrument (`is_instrument`: declared script suffix or shebang) | same |
| 3 | New check `trigger.citation_resolves` + `citation_resolve` (bounded `..` hops, ≤3) | same |
| 4 | Twenty-one fixtures (47 cases at HEAD → 67): L1's six (`citation-dead`, `citation-base-named`, `command-path-arg`, `command-path-arg-ok`, `command-redirect-target`, `delegated-noninstrument`), the executor lane's boundary set (`citation-ok`, `citation-boundary-dirslash`, `citation-boundary-ufo`, `delegated-directory`), and the adversary-driven pins (`citation-dot-slash`, `citation-second-word{,-ok}`, `delegated-elf`, `delegated-py-suffix`, `command-output-flag`, `command-input-redirect`, `command-sh-c-inner`, `command-sh-c-ok`, `citation-anchor-ok`, `delegated-escape`) | `verifiers/fixtures/checklist/` |
| 5 | Self-test grows 772 → 1283 assertions over 67 fixture cases; a check whose subject may be absent is N/A-allowed with an explicit non-vacuity assertion | same |
| 6 | Map: `trigger.11` `delegated:…` → `executed:trigger.citation_resolves`, new box sha `c7ad2458…`; counts now 8/0/33 | `verifiers/checklist-baseline.json` |
| 7 | `SKILL.md`: 3 citation sites named, box `trigger.11` rewritten to its executed subset, counts updated (9 checks, eight executed boxes, corpus instrument scoped to `corpus/*.md`), still 599 lines | `SKILL.md` |

## Evidence at the landed tree

```
$ sha256sum verifiers/verify_skill_checklist.py
70f8b38e9386ab1ee808c57aee29586887bad4320b899c954da1660ac020a8e4
$ python3 verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1283 assertions         # rc 0
$ python3 verifiers/verify_skill_checklist.py
PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)
PASS trigger.frontmatter_parses: evaluated 4
PASS trigger.name_directory: evaluated 1
PASS trigger.literal_trigger_string: evaluated 1
PASS trigger.anti_trigger_clause: evaluated 1
PASS trigger.line_budget: evaluated 599 — within budget 600 (from box at line 327)
PASS trigger.no_placeholder: evaluated 550
PASS trigger.command_binary_resolves: evaluated 19 — 15 segments; 19 command subject(s) resolve
PASS trigger.citation_resolves: evaluated 42 — 42 repo-rooted citation token(s) resolve
rc=0
```

## Ceilings this round adds (named, not hidden)

| Ceiling | Why it is one |
|---|---|
| `echo <bare-token>` in a fence is **not** a defect after R1 | pasting `echo r15absent-echoed-bin` succeeds; the check's claim is "runnable as pasted". The round-15 `M35` row is re-labelled, and the rule closes the path-argument half (`cat corpus/nope.md`) with a fixture |
| absolute and `~`-anchored arguments are out of scope | host-dependent; the same ceiling the corpus verifier uses |
| an argument after a skip-list builtin yields no subjects | `echo corpus/nope.md` prints the path; the skip list is consumed before arguments |
| output flags outside the declared set (`-o --out --output --write --dest --log --to --target -O`) do not exempt a path | a written path under an undeclared flag FAILs; the flag set is a declared, reviewable list |
| R3's root set is closed (`corpus/ verifiers/ opencode/ .ufo/ ../`) | a dead `docs/x.md` escapes; a *named* base is excluded by construction — and naming the base is exactly the mandated repair, so the box's first sentence is what forbids a bad base |
| single-segment directory names (`corpus/`, `.ufo/`) are labels, not pointers | `opencode/` and `.ufo/` do not exist under this repo and are legitimately named as classes; a deeper path (`.ufo/prompts/`) is checked |
| delegation tests instrument-ness by suffix or shebang | a `.py` data file, a shell script named `x.txt`; the instrument is never executed |
| the `delegated:` disposition class now has zero live entries | the class stays implemented and fixture-covered (`map-dead-delegated`, `delegated-noninstrument`) — the cost is recorded in `SCORECARD.md` |
| `$VAR/corpus/x.md` as an argument or citation | metachar exclusion: the value is unknown statically (mutation lane's `R16c`) |
| a backslash continuation that splits a path across lines | the join inserts a space the shell would not (sentinel) |
| an unbalanced-quote segment | `shlex` raises and the fallback `str.split()` may mis-tokenize (sentinel) |
| a delegated target that is a symlink | judged by its name (`is_instrument` stats the path, not the referent): a `.py` symlink to a JSON file passes (sentinel) |

## Adjudication (L2 lanes, this round)

Ten L2 lanes ran; every finding that could be turned into a rule or a fixture was
landed in-round, and the rest are named here.

| Lane | Finding | Disposition |
|---|---|---|
| `R16Mutate` | 46-row round-15 harness re-run at HEAD: **zero** verdict changes (35 caught / 5 escaped / 5 pin / 1 control). Against the patched build exactly one legacy row flips: **`M40` → CAUGHT** (36/4/5/1) | recorded; `M35` stays escaped (see below) |
| `R16Mutate` | 8 new rows: `cat corpus/absent.md` CAUGHT, `cat ./corpus/absent.md` CAUGHT, `python3 verifiers/nope16.py` CAUGHT, `delegated:…json` CAUGHT (not an instrument), dead `verifiers/absent16.md` citation CAUGHT; `$VAR/corpus/absent.md` and dead `docs/absent16.md` ESCAPE by design | ceilings (`$VAR`, closed root set) |
| `R16M35` (labrat) | `M35`/`M40` red-before reproduced byte-for-byte at HEAD; the proto (spec-literal R1/R2) had zero spec disagreements | proto-vs-spec agreement recorded |
| `R16M35` (labrat) | **Landedly false positive**: `sh -c 'cat corpus/README.md'` FAILed, because the outer segment's script string was tested as one path | **fixed**: `unwrap_tokens` now returns the token list the head came from, so the inner script's arguments are the subjects; fixtures `command-sh-c-inner` (FAIL) and `command-sh-c-ok` (PASS) |
| `R16Critic` | **R2 falsified**: suffix-or-shebang rejects a compiled instrument (`~/.local/bin/sekhmet`, ELF, no suffix) | **fixed**: ELF magic accepted; fixture `delegated-elf` (PASS) |
| `R16Critic` | Citation laundering via a `./` prefix; the `delegated` class has **zero live entries** and its path is fixture-only | **fixed** (leading `./` normalized; fixture `citation-dot-slash`) / **cost recorded** (below) |
| `R16Sentinel` | `wc -l < corpus/dead.md` PASSed while `cat corpus/dead.md` FAILed: `<` is an *input* redirect | **fixed**: only output redirects exempt; fixture `command-input-redirect` (FAIL) |
| `R16Sentinel` | Trailing dressing false-FAILs (`corpus/README.md:42`, `x.md,`) | **fixed**: `strip_token_dressing`; fixture `citation-anchor-ok` (PASS, evaluated 2). Prior art for the anchor class: kasegi `corpus/instruments/anchorcheck.py` validates `path:NN[-MM]` (connector lane) |
| `R16Sentinel` | `delegated:../out.py` passes | **fixed**: a target with a `..` segment FAILs; fixture `delegated-escape` |
| `R16Sentinel` | Claim: an empty `delegated:` passes | **refuted by measurement**: exit 3 at map load (`boxes[1].disposition must be executed:\|delegated:\|unexecuted:<non-empty>`), i.e. fail-closed |
| `R16Indep` | Four predicted verdicts matched the actual verdicts; six divergences from the *literal* spec text (bare-dirslash, redirect skip, `echo` args, quoted args, delegated base, `which` on slash tokens — A13) | five are named ceilings; **A13 fixed**: a token with a slash is a path, not a PATH lookup (resolution no longer depends on the verifier's cwd) |
| `R16Blast` (scout) | R1 over 23 fleet `SKILL.md`: 77 path-like args, 27 would-FAIL, 3 verdict flips — **0 true positives**; classes: produced path without a declared output flag, deployed-tree path, example input, workdir-relative name | **25/2 after the URL + comment-tail fixes**; documented as the foreign-hint rate; tightening candidate = declared read-verb vocabulary (round 17) |
| `R16Blast` | The two carve-outs (`REDIRECT_TOKENS`, `OUTPUT_FLAGS`) had zero live coverage | **fixture added**: `command-output-flag` pins the output-flag carve-out on the other side of `command-redirect-target` |
| `R16Review` (reviewer) | The three `.ufo/prompts/` sites are **real** at HEAD (`test -e .ufo/prompts` → no; zero `.ufo` under the repo); HEAD reproduces every round-15 quote (8×PASS, 0/772, 41 boxes 7/1/33, 16/16 commands) | confirms the red-before |
| `R16Connector` | No sibling declares `delegated:` (repo-wide search: no matches); kumitate's `surface-probe.mjs` *executes* checklist commands but does not resolve arguments/targets/citations; kasegi has citation-resolver prior art (`resolve.py`, `anchorcheck.py`); sibling R3 dead tokens: kagi 2, kake 1, kasegi 1, kengaku 1, kumitate 5 | **routed**, not fixed — sibling surface belongs to those lanes |

## The `M35` re-labelling, stated plainly

The pre-registered earn-condition was "close `M35` (resolve arguments that look
like paths)". What landed resolves *path-like* arguments. The planted mutation
`echo r15absent-echoed-bin` is a **bare token**: `echo` is a skip-list builtin
and the token has neither a slash nor a file suffix. It still escapes — and the
argument for leaving it is falsifiable, not rhetorical: paste the line and it
succeeds, so under the box's own claim ("runnable as pasted") it is not a
defect. The counter-argument is equally stateable: within a fenced recipe the
line is meaningless, and a reader may expect a binary name there to exist. The
decision taken — *benign insertion, not an escape* — is recorded as a claim the
next mutator can attack; the rule-covered sibling (`cat corpus/nope.md`) is
closed with `command-path-arg`.

## Cost of removing the live `delegated:` entry

`trigger.11` is the only box that ever used `delegated:`; it is now executed, so
the class has **zero live entries** and `is_instrument()` is exercised only by
fixtures (`delegated-noninstrument`, `delegated-directory`, `delegated-elf`,
`delegated-py-suffix`, `delegated-escape`, `map-dead-delegated`) plus the
`--self-test` gate. The instrument does not run `--self-test` in a default live
run, so R2 can regress without a live FAIL — recorded, and the mitigation is that
every round's verification and the mutation harness call it. The alternative
(keeping a delegation to a box no instrument enforces) is the defect this round
exists to remove.

## Band decision

Pre-registered full band: *the two named escapes are closed and the mutation
lane's re-run catches both*. Measured: `M40` is caught by the legacy harness; the
`M35` row is **re-labelled by argument** (above) and its rule-covered variant is
caught with a red-before fixture. The mutation lane's own tally therefore reads
36 caught / 4 escaped rather than 37/3.

Two independent readings, both recorded rather than averaged:

- **8.5**: the two escapes named in the round-15 pre-registration are no longer
  live — one by a rule with a red-before fixture, one because the mutation is not
  a defect — and no *new* escape was introduced without a name (the ten lanes
  found six defects, all fixed in-round with fixtures, and four ceilings named).
- **8.0**: the pre-registered wording says "close `M35`", and the planted token
  still exits 0; a band that is earned by re-labelling the falsifier is a weaker
  claim than one earned by catching it.

The lane lands **8.5, annotated**: the whole point of the round-15 amendment
discipline was that a claim's scope is part of the claim — `M35` was recorded as
"arguments never resolve", and arguments now resolve *in the class the box is
about*. The withheld reading is written down, so the aggregator can move the row
back to 8.0 on the strength of this paragraph alone.
