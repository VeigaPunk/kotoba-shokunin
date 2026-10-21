verdict: a description-scoped XML-tag check flags exactly one of 18 lane SKILL.md files at BASE — kotoba's own `<skills>` at `SKILL.md:14`, folded out of `description: >` at `:3`; all 17 sibling lanes carry no `<` or `>` anywhere in their description, so C2 needs no sibling edits and its only real falsifier is a block-scalar fixture, not a plain-scalar one.

# C2 fleet scan — description XML-tag adjacency (report-only)

Scope: every `/home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md` top-level file, frontmatter
`description` only (the C2 rule, `plans/round-47.md:28`, sourced on `corpus/SOURCES.md:16` S003:
"The description cannot contain XML tags"). Sibling lanes are read-only and own their own files;
this report is a routing note, not a change request.

Method: descriptions parsed with the lane's own structural
`parse_frontmatter` (`verifiers/verify_skill_checklist.py:472`) imported from a scratch clone at
BASE, so block scalars and indented continuations fold exactly as the live verifier folds them.
Three candidate rules were applied to the folded value: strict tag
`<[/!?]?[A-Za-z][\w.:-]*(?:\s[^<>\n]*)?/?>`, S003-loose `</?[A-Za-z][^<>\n]*>`, and any-angle
`[<>]`. Evidence artifact: `.ufo/waves/round-47/build/C2FleetScan.scan.json`.

## Findings

**F1 — the single hit, and why the fold is the whole test.** kotoba `SKILL.md:3` is
`description: >`; the token is on continuation line `SKILL.md:14` ("never reach the `<skills>`
router — craft here is audit-side"). A check that reads only the raw text after `description:`
sees `>` and vacuously PASSes; a check that reads the parsed value sees `['<skills>']`. This is
the exact shape a planted mutation must reproduce (F6). kotoba SKILL.md at BASE sha256
`c8b245b7dd2cfeb99855e968fb2cf778d820dcbcecd21195e320d5fa41eaa0fb`.

The token is also **backticked** (`` `<skills>` ``). A second independent vacuity: the existing
`check_anti_trigger` strips quoted/backticked spans before its vocabulary test
(`ALL_QUOTED_SPANS_RE`, `verifiers/verify_skill_checklist.py:364`, applied at `:1230-1236`); an
XML check copied from that shape would erase this very token and PASS. The check must scan the
raw folded value, not a span-stripped one.

**F2 — sibling lanes: zero angle characters, so every regex agrees.** 17 sibling descriptions
contain no `<` or `>` at all (strict, loose and any-angle rules all return the same failing set
`{kotoba-shokunin}`). Description style varies — 6 quoted, 10 plain, 2 block (`kotoba:3`,
`lore:2`) — but no lane currently exercises the parser's tag path. Routing note: no sibling lane
would fail the new check, before or after C2, and none needs notification beyond this report.

**F3 — scope must be the folded `description` value, never the file or body.** All 18 lanes carry
XML-like tokens in their bodies (6 to 108 token lines each); kotoba's body alone has 18 such
lines (`<skills>` at `:22,:91,:96,:99,:111,:430`, `<available_skills>` at `:41,:92,:114,:430`,
others at `:42,:98,:151,...`). A whole-file grep — or a rule that "cleans" the body — would fail
18/18 lanes forever and would strip kotoba's actual subject matter. Whole-frontmatter scanning
(all keys, not just `description`) happens to hit only `:14` today, but that is incidental: the
check should read `fields["description"]` exactly as `check_literal_trigger` (`:1205`) and
`check_anti_trigger` (`:1230`) do.

**F4 — a `yaml.safe_load` implementation would be right on kotoba and unusable fleet-wide.**
PyYAML 6.0.3 rejects 10/18 lane frontmatters with `mapping values are not allowed here`, because
10 lanes use unquoted plain scalars containing `: ` (e.g. `tsukuroi-shokunin/SKILL.md:3`
"…repair. Rank: shonen (probation)."). kotoba's block scalar parses and does surface the tag, so
the defect would be caught, but the parser choice must stay `parse_frontmatter` (structural), not
strict YAML. Kotoba's own `trigger.frontmatter_parses` PASS is therefore not evidence that YAML
validity is fleet-wide.

**F5 — self-test calibration cost is exactly 7 CASES rows.** `self_test` computes
`passes = [c for c in CHECK_IDS if c not in fails and c not in nas]`
(`verifiers/verify_skill_checklist.py:1842`), so a new id defaults to "expected PASS" on every
fixture. None of the 71 fixture cases carries a tag in a parsed description (6 have no parseable
frontmatter at all), so no existing fixture gains a *tag* failure, but a check that FAILs when the
description is unparsable/empty — consistent with the two
neighbouring description checks — forces the new id into these rows' expected fails:
`no-frontmatter:1679`, `fm-null:1683`, `fm-malformed:1687`, `fm-dup-key:1691`,
`fm-body-yaml:1695`, `fm-stray-indent:1700`, `empty-file:1758`. Reporting N/A instead is not
free: `NA_ALLOWED` (`:1830`) admits only the two citation checks, and the loop still asserts
every non-listed id PASSes with `evaluated > 0`. `--check` choices derive from `CHECK_IDS`
(`:2114`), so argparse needs no separate edit; the `--json` tally goes 10 → 11
(`CHECK_IDS` `:282-293`; no XML check exists at BASE — `grep -n 'no_xml\|xml_tag' …` rc 1).

**F6 — fixture discriminating power (counterexample to the planned acceptance).** The plan's
acceptance is "`--self-test` rejects the planted-tag mutation". A plain-scalar plant
(`description: … <skills> …`) proves only the regex; it does not prove the fold. Because the live
defect is on a continuation line, the fixture family needs at least one **block-scalar** case
(`description: >` + tag on an indented line, i.e. kotoba's BASE shape) or a first-line-only
implementation passes the self-test while the live file still fails. A tag-free control should
pin the boundary: `arity < 3` is not a tag and must pass; `Map<K>` is tag-shaped and would be
flagged (`Map<K,V>` is not, because `,` is outside `[\w.:-]`). If S003's "XML tags" is read
broadly, also pin `<!-- -->` / `<?…?>` — the strict regex above does not match comments or PIs.
Error messages should name the physical line (here `:14`, not `:3`); a folded-value check with
line `:3` sends the author to the wrong place. Two plants, not one: an unbackticked tag on a
continuation line (folds), and a backticked tag (span-strip vacuity, F1) — the live token is both.

**F7 — coverage.** 21 `*-shokunin` directories; 18 have a top-level `SKILL.md`; 3 do not
(`audio-shokunin`, `game-dev-2d-shokunin`, `revenger-shokunin`). A fleet sweep must treat
"absent" as absent, not FAIL. `mori-shokukin/` (only `.ufo`) and
`tameshi-shokukin/tameshi-shokunin/` (empty) are not lanes and carry no `SKILL.md`. 4632
`SKILL.md` files exist at depth >= 2 across the fleet (the depth >= 4 sample is dominated by
`.ufo` scratch mirrors) — outside the declared target and not scanned. Only kotoba has a
`verifiers/` tree at all (`ls -d */verifiers` -> 1), so the new check is kotoba-only and cannot
be run against a sibling lane without copying the instrument into that lane (a lane violation).

**F8 — parent-claim reproduction is clone-limited [INFERENCE].** Running the BASE verifier from
the clone with a symlink named `kotoba-shokunin` gives **8 PASS / 2 FAIL** (`--skill` symlinked
path, map from the clone): `trigger.name_directory` PASSes correctly, and both FAILs are citation
artifacts — `trigger.citation_resolves` at `SKILL.md:515` (`../.ufo/reports/round-7/kotoba.md`)
and `governance.citation_resolves` at `LOG.md:177` (`../.ufo/reports/round-9/kotoba.md`). Both
targets exist in the fleet root (`test -e` rc 0 each) and are untracked, not ignored
(`git check-ignore` rc 1 → untracked → absent from the clone). The plan's 9 PASS / 1 FAIL at the
lane root is therefore consistent, with `governance.citation_resolves` the remaining red — the C3
target, not a C2 concern. I did not run the verifier in the production lane to confirm the 9th
PASS directly.

**F9 — "descriptions that mention router tags" = 1 lane.** Only kotoba's description mentions
"router" (and carries `<skills>`). No lane description contains `skill://`, `system-reminder`,
`available_skills`, "skills tag" or "router tag"; the apparent `kotodama` "tag" hit is the
substring in "era staging" (false positive, not a mention).

**F10 — freshness of this note.** Sibling repos advanced during the scan
(kagi 144babcb892f→3fb77271eeee, kaidoku 9d64b95393bb→fe18f13f7984, tsukuroi ae01e50f5820
→56c8ba3840cc, tameshi d2eaecd443bf→bd38c02a8b74). For all 18 lanes the parsed description at `HEAD:SKILL.md` equals the working
tree (byte-for-byte on the description value), so the table below is not stale relative to those
commits. Re-check head shas before quoting the table after this wave.

## Table — lane, token, line (description scope)

| lane | HEAD (12) | description | style | len | token:line | verdict |
|---|---|---|---|---|---|---|
| chousa-shokunin | dd72641e5746 | :3 | quoted | 373 | — | PASS |
| game-dev-3d-shokunin | 89dd182b7094 | :3 | plain | 737 | — | PASS |
| kagi-shokunin | 3fb77271eeee | :3 | plain | 120 | — | PASS |
| kaidoku-shokunin | fe18f13f7984 | :3 | plain | 604 | — | PASS |
| kake-shokunin | 97404de4ff73 | :3 | plain | 119 | — | PASS |
| kama-shokunin | 245a37f69628 | :3 | plain | 141 | — | PASS (SKILL.md dirty; desc == HEAD) |
| kasegi-shokunin | 8bf980721554 | :3 | plain | 121 | — | PASS |
| kengaku-shokunin | 31934e5660f1 | :3 | quoted | 882 | — | PASS |
| **kotoba-shokunin** | **c61a973b2e02 (BASE)** | **:3** | **block `>`** | **814** | **`<skills>` :14** | **FAIL — only hit** |
| kotodama-shokunin | 4ad268365524 | :3 | quoted | 613 | — | PASS |
| kumitate-shokunin | 2fa28e576122 | :3 | plain | 131 | — | PASS |
| lore-shokunin | 380ef3abc7c7 | :2 | block `>` | 648 | — | PASS (block scalar, tag-free) |
| mado-shokunin | 8c7420938369 | :3 | plain | 73 | — | PASS |
| mori-shokunin | 1bfe708a170c | :3 | quoted | 369 | — | PASS |
| souji-shokunin | 81a2646d53f9 | :2 | quoted | 545 | — | PASS |
| tabi-shokunin | 0f24164be77e | :3 | plain | 78 | — | PASS |
| tameshi-shokunin | bd38c02a8b74 | :3 | quoted | 196 | — | PASS |
| tsukuroi-shokunin | 56c8ba3840cc | :3 | plain | 79 | — | PASS |
| audio-shokunin | 0462a5440f23 | — | — | — | no top-level SKILL.md | N/A (absent, not FAIL) |
| game-dev-2d-shokunin | bce53b83a21e | — | — | — | no top-level SKILL.md | N/A (absent, not FAIL) |
| revenger-shokunin | e0a4b0c4348e | — | — | — | no top-level SKILL.md | N/A (absent, not FAIL) |

## Commands run (all read-only; no production-file write, no gate run in the lane)

- `git -C kotoba-shokunin rev-parse HEAD` → 0, `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.
- `git clone -q --no-hardlinks … /fast/scratch/kotoba-r47/C2FleetScan/lane` → 0; `checkout --detach c61a…` → 0.
- `python3 -B /fast/scratch/kotoba-r47/C2FleetScan/scan.py` → 1 (scanner's own convention: 1 = a description carries a tag); summary `lanes_with_top_SKILL=18 desc_tag_fail_strict=1 desc_angle_any=1`.
- `python3 -B lane/verifiers/verify_skill_checklist.py --json` → 1, `pass 7 fail 3`; with
  `--skill …/kotoba-shokunin/SKILL.md --map …/checklist-baseline.json` → 1, `pass 8 fail 2`
  (both runs in the clone; see F8 for why they differ from the lane's 9/1).
- `test -e .ufo/reports/round-7/kotoba.md` → 0; `test -e .ufo/reports/round-9/kotoba.md` → 0;
  `git check-ignore -v .ufo/reports/round-7/kotoba.md` → 1 (not ignored, untracked).
- `grep -n 'no_xml\|xml_tag' verifiers/verify_skill_checklist.py` → 1 (no such check at BASE).
- `python3 -c 'import yaml; …'` (PyYAML 6.0.3) over 18 frontmatters → 10 rejections (F4).
- `date -Is` → 2026-10-21T13:00:36-03:00.

Artifacts: `.ufo/waves/round-47/build/C2FleetScan.scan.json` (18 KB, per-lane evidence incl.
strict-YAML verdict and the 7 affected CASES) and `C2FleetScan.checklist-base.json` (clone run).
No tool installs; nothing written outside `.ufo/waves/round-47/build/` and
`/fast/scratch/kotoba-r47/C2FleetScan/`.

## Risks / second-order effects

- Regex choice does not change today's routing (F2) but decides future false positives: `[<>]`
  fails comparators and arrows; a tag-syntax regex fails `Map<K>`; neither matches comments/PIs.
- Removing kotoba's `<skills>` at `:14` leaves 18 body lines with XML-like tokens by design (F3);
  a later "cleanup" that greps the whole file would delete the skill's subject matter.
- Sibling repos are moving during the wave (F10); the table's HEAD column dates the claim.
- Do not let C2's fixture be only a plain-scalar plant (F6) — that is the one mutation class that
  the live file does not exercise.

## What I did NOT check

- Did not run any verifier inside the production lane, and did not run `--self-test` (the C2
  check does not exist at BASE; its fixtures cannot be exercised).
- Did not scan the 4632 nested `SKILL.md` files (mostly `.ufo` scratch) or host skill roots
  (`~/.omp/agent/skills`, `~/.config/**`) — outside the declared target.
- Did not inspect how `audio-shokunin`, `game-dev-2d-shokunin`, `revenger-shokunin` are
  discovered without a top-level `SKILL.md`.
- Did not read sibling LOG.md/corpus for independent XML-tag rules; only `description` values.
- Did not edit, commit, or message sibling lanes; no sibling lane needs a change per F2.
