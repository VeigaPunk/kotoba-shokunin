verdict: HOLDS — S012 (anthropics/skills skill-creator `quick_validate.py`) survives re-open: the quoted line, anchor 79–81, revision `dbd4588` (= main HEAD), tier A and `mined`/`used-by: SKILL.md` all check out; three minor calibration notes, no counterexample to the row's factual claims.

# W2S012Reopen — S012 re-open at 7ad7fad

Lane: kotoba-shokunin, round-47 falsify (wave 2). HEAD under test:
`7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b`). Row under test:
`corpus/SOURCES.md:25`, inside `## Registry` (`:10`–`:29`), before `## Paths` (`:30`).
Scratch canonical clone: `/fast/scratch/kotoba-r47/w2/W2S012Reopen-2/kotoba-shokunin`
(HEAD detached at 7ad7fad). Production tree read-only; no installs or upgrades (curl,
python3/PyYAML 6.0.3, coreutils, git only).

## 1. Source re-open — observed facts

Pinned raw fetch, HTTP 200, 3972 bytes, 102 lines, sha256
`67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365`:

```
79:        # Check for angle brackets
80:        if '<' in description or '>' in description:
81:            return False, "Description cannot contain angle brackets (< or >)"
```

- The quoted string is byte-exact at `:81`; `grep -cF` → 1. The anchor's quoted
  `"Check for angle brackets"` is byte-exact at `:79`. The range `79–81` is the whole block.
- `https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/scripts/quick_validate.py`
  is byte-identical (`cmp` exit 0, same sha256); GitHub API `compare/dbd4588...main` →
  `status identical, ahead_by 0, behind_by 0`, i.e. the pinned commit **is** main HEAD on
  2026-10-21. Commit date `2026-10-09T18:45:49Z` matches the row's `tree dbd4588 (2026-10-09)`.
  The tree URL `.../tree/dbd4588.../skills/skill-creator` returns HTTP 200.
- **The packager really refuses.** `package_skill.py:17` imports `validate_skill`;
  `:72–76` abort with `return None` before archiving on failure. End-to-end fixture
  (`description: a < b comparison`): `python3 package_skill.py fix-tagged` → exit 1,
  `Validation failed: Description cannot contain angle brackets (< or >)`, no output dir.
- **Any angle bracket, not tag grammar.** Bare `<`, bare `>`, and `<skills>` each exit 1
  with that message; plain text exits 0. The "not only well-formed XML tags" clause holds.
- **The open spec (S001) states neither.** Rendered `https://agentskills.io/specification`
  (HTTP 200, 459866 bytes): `xml` 0, `bracket` 0, `markup` 0; the sole `<` is
  `Instructions (< 5000 tokens recommended)` (body-size budget). The frontmatter table's
  description cell reads only `Max 1024 characters. Non-empty. Describes what the skill
  does and when to use it.` The row's "the open spec states neither" is true.

## 2. Row cells vs `CORPUS.md` § SOURCES.md contract

| cell | value at `corpus/SOURCES.md:25` | contract test | result |
|---|---|---|---|
| anchor | `skills/skill-creator/scripts/quick_validate.py:79-81` "Check for angle brackets"; tree `dbd4588` (2026-10-09) | exact line + revision, never a bare homepage (`CORPUS.md` § Shape) | **pass** — line block byte-exact; commit date and main-HEAD identity verified |
| teaches | packager refuses any `<`/`>`; stricter than S003; spec states neither | one grounded benefit | **pass** — all three clauses reproduced (fixtures + spec sweep; S003 quote at `corpus/SOURCES.md:16`) |
| kind / tier | `code` / `A` | A includes "source code", scoped to `scope` | **pass** — tier scoped to the reference packager's behavior, which is what the code enforces |
| scope | "SKILL.md `description` validation in Anthropic's own reference packaging tooling" | scoped, not global | **pass with bound** — see F3 |
| status / used-by | `mined` / `SKILL.md` | `mined` = cited by ≥1 path in used-by; used-by = knowledge-entry/lesson paths | **pass mechanically, contract prose tension** — see F1 |
| opened / recheck | `2026-10-21` / `90d` | ISO date; ISO date or cadence | **pass** |
| format | NF=13 | 11 cells, no `|` in a cell | **pass** (frozen census `malformed=0`) |
| Gate record | `corpus/lessons/round-47.md:35` — URL, `2026-10-21T15:55:51Z`, 8-word quote, `:81`, sha256 `67cf5703…`, record path | rule 1: URL + access date + ≤25-word quote with location | **pass** (8 words; sha256 and line verified; record exists) |

Census at 7ad7fad, run from the lane root: rows 15, malformed 0, `A=14 C=1`,
`mined=6 queued=8 rejected=1`, no duplicate ids, no enum/tier-inflation, no missing
used-by path; maintained `scripts/sources-census.sh validate --file … --today 2026-10-21`
→ `file ok`, exit 0. `git diff c61a973b..7ad7fad -- corpus/SOURCES.md` = 19 insertions /
4 deletions, and the deletions are the header evidence sentence plus two promoted
`## Leads` bullets — **no existing row's status/recheck/used-by changed**, so the Gate's
"old→new: none" is true.

## 3. Findings

### F1 — `used-by: SKILL.md` is a real citer but a path class the contract prose omits (minor; pre-existing)

`CORPUS.md:107`: "`used-by` — repo-relative paths of the knowledge entries or lessons
citing the row, comma-separated, or `—`." S012 names `SKILL.md`, which is neither.
It does genuinely cite the row — `SKILL.md:151`: "Anthropic's reference packager (S012)
is stricter and refuses any `<`/`>`" — so `mined` is mechanically true, and the frozen
census (which only tests existence) passes.

Counter-evidence that a strict reading would want a corpus path:
- `grep -rln "S012" corpus/knowledge/` → no output, exit 1 (no knowledge entry cites it);
- `corpus/lessons/round-47.md:42` is a lesson that does cite it, but is not in `used-by`.

This is not a round-47 regression: S003 (`corpus/SOURCES.md:16`) and S008 (`:21`) carry
the same `used-by: SKILL.md` value at BASE and at 7ad7fad (no row cell changed in the
landing diff). Disposition: contract-owner decision — widen the prose to admit the
skill's own SKILL.md, or list `corpus/lessons/round-47.md`; the row is not falsely
`mined` either way.

### F2 — the lesson says the check's detail line cites S012; it states the rule without citing S012 (minor)

`corpus/lessons/round-47.md:42–43`: "and on S012, which the check's detail line and
`SKILL.md` § Portability floor cite as the stricter vendor packager rule."
`SKILL.md:151` does cite S012. The check's detail line does not:
`verifiers/verify_skill_checklist.py:1307–1308` reads
`"S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any
'<'/'>' and is stricter"` — no row id, no URL; the docstring at `:102` cites only
S003/S001/S002. Repro: `grep -rn "S012" verifiers/` → no output, exit 1.
The fact is true and S012 grounds it; the sentence's attribution ("the check's detail
line … cite[s] [S012]") is the overstatement. Reference-drift class, wording only —
a one-word fix ("the check's detail line states the same rule, grounded by S012") would
close it. It is a lesson-prose defect, not a SOURCES row defect.

### F3 — scope bound: the vendor's description validation does **not** enforce non-empty, so cite S012 only for the angle rule (observation, not a falsification)

Fixtures `description: ""` and `description: "   "` both return `Skill is valid!` exit 0
(`quick_validate.py:78` guards the whole block with `if description:`), while the open
spec's description cell says "Non-empty". The row's `teaches` claims only the angle rule,
and the anchor pins it — so the row's claim survives. But the `scope` cell ("`description`
validation") is broader than `teaches`: a downstream citation must not treat S012 as
evidence that the packager enforces non-empty or the spec's other description constraints.
No other S012 claim depends on this.

## 4. Mutation tests — the census checks are live for this row

Copies in `/tmp`; production untouched; commands run from the lane root so relative
used-by paths resolve.

| mutant | command | observed |
|---|---|---|
| S012 tier `A` → `D` | frozen enum awk | `tier S012 D` |
| S012 used-by `SKILL.md` → `DOES-NOT-EXIST.md` | frozen mined-path awk + existence loop | `missing: DOES-NOT-EXIST.md` |
| production control | same two commands | no output (clean) |

## 5. Commands and exit codes

| # | command | exit | key output |
|---|---|---|---|
| 1 | `git clone --no-hardlinks … && git checkout --detach 7ad7fad` | 0 | HEAD `7ad7fad…` |
| 2 | `curl -sSL -w 'HTTP:%{http_code}' …/dbd4588…/quick_validate.py` | 0 | `HTTP:200`, 3972 B, sha256 `67cf5703…` |
| 3 | `curl … raw.githubusercontent.com/anthropics/skills/main/…/quick_validate.py` + `cmp` | 0 | identical (`main` = pin) |
| 4 | `curl api.github.com/repos/anthropics/skills/commits/dbd4588…` | 0 | `2026-10-09T18:45:49Z` |
| 5 | `curl api.github.com/…/compare/dbd4588…...main` | 0 | `identical`, ahead 0 / behind 0 |
| 6 | `grep -cF 'Description cannot contain angle brackets (< or >)' qv.py` | 0 | `1` (line 81) |
| 7 | `python3 qv.py` on `<`, `>`, `<skills>` fixtures | 1,1,1 | `Description cannot contain angle brackets (< or >)` |
| 8 | `python3 qv.py` on plain fixture | 0 | `Skill is valid!` |
| 9 | `python3 package_skill.py fix-tagged /tmp/s012/out` | 1 | `Validation failed: …`; no output dir |
| 10 | `python3 qv.py` on `""` / `"   "` description | 0,0 | `Skill is valid!` (F3) |
| 11 | spec fetch + render sweep (`xml`/`bracket`/`markup`) | 0 | 0/0/0; only `<` is `< 5000 tokens` |
| 12 | frozen SOURCES census (rows/malformed/tier/status/dup/enum/mined-path) | 0 | 15 / 0 / A=14 C=1 / mined6 queued8 rej1 / none / none |
| 13 | `bash scripts/sources-census.sh validate --file … --today 2026-10-21` | 0 | `file ok` |
| 14 | two census mutants + control | 0 | `tier S012 D`; `missing: DOES-NOT-EXIST.md`; control clean |
| 15 | `grep -rn "S012" verifiers/` | 1 | no output (F2) |
| 16 | `grep -rln "S012" corpus/knowledge/` | 1 | no output (F1) |
| 17 | `python3 -B verifiers/verify_corpus_independent.py --repo .` | 0 | `tracked_files=60`, unindexed/stale/missing/dead/unresolvable=0 |

Artifacts: `W2S012Reopen.fetch.txt` (source/fetch/identity evidence, fixtures, spec sweep);
`W2S012Reopen.census.txt` (census, mutants, citation sweep, landing diff).

## 6. What I did NOT check

- **C1** — did not re-derive omp/opencode surfaces or run `verify_surfaces.py` /
  `check_substrate_pins.py`; the S015 pin row is outside this lane.
- **C2 execution** — did not run `verify_skill_checklist.py` (self-test, `--json`, or
  fixture battery); I read the gate and its detail line only. The C2 pass/fail claim is
  another seat's.
- **C3** — did not run the fault harness, `verify_corpus_integrity.py`, or re-check the
  `corpus-baseline.json` 58→60 delta; I only observed `tracked_files=60` as a side effect
  of command 17. Did not verify M20–M22.
- **Other rows** — S013–S015 and the S001–S011 re-opens were not re-opened here.
- The access timestamp `2026-10-21T15:55:51Z` is lane-local and not independently
  verifiable from the committed tree.
- The build report's pre-move history claims (`37292f3` init, `ef74077` move) were not
  re-derived beyond the commits API listing for the current path (2 commits: `1ed29a0`
  2026-02-06, `ef74077` 2025-12-01); the landed row carries neither claim, so the row is
  unaffected.
- Did not execute `~/.local/bin/opencode` or launch any omp session (contract); not
  needed for this source.
- Did not check licensing/attribution for quoting the 8-word vendor error string.
