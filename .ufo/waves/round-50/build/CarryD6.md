# CarryD6 — routed defect D6 (carried items), round-50 build

Seat `KotobaR50.CarryD6` (UFO-FSD scout, leaf, no delegation). Date 2026-10-22. Lane read-only except
this file; lane head `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`, `git status --porcelain` shows only
`?? .ufo/waves/round-50/`, `?? plans/round-50.md` (untouched). No tool installed or upgraded; no pacman
transaction attempted. Scratch: `/fast/scratch/hyaku/kotoba-r50/build/CarryD6/` (`oc-index.ts`, `fx/`).

**Result: ALL THREE STILL OPEN at `f3046466`.** R4 has 2 of 23 count rows unprovenanced and its fixture
inputs untracked; R5's v2 oracle exists only as a proposal, with v1 the only frozen file; R1's fallback
is byte-identical to the round-49 head that falsify F1 failed, and the self-test still pins the
divergent count green.

## R4 — two round-48 counts without a reproducing command

State at base (`corpus/knowledge/frontmatter-rule-authorities-round48.md`, 186 lines): table row `32`
(line 149) still says `24 probe fixtures … no stored run list … **no — 24 not reproducible**`; row `56`
(line 157) still says `**no — printed command cannot produce 0**`; the closing paragraph (line 185) still
says "partly addressed, not closed".

Reproduced the mismatch this session against the persisted round-48 fixture tree:
`python3 -B /fast/scratch/hyaku/kotoba-r49/seats/R4CountProvenance/counts.py` → exit 0,
`probe_files 36 probe_dirs 36 probe_distinct 29`. The seat's own cited path (`lane/probes{,2..14}/`) has
14 probe roots whose recursive `SKILL.md` counts are `probes 12, probes2 7, probes3 3, probes4 1,
probes5 1, probes6 1, probes7 1, probes8 1, probes9 2, probes10 1, probes11 1, probes12 2, probes13 1,
probes14 2` = 36; no selector yields 24, and the round-48 doc names zero individual probes
(`grep -oE 'p_[a-z0-9_]+' | sort -u | wc -l` → 0), so 24 cannot be recovered from the text either.
Row 56 reproduced on the seat's sources: printed pattern
`grep -niE 'third person|reserved|max_lines|line_count|500' validator.py parser.py models.py` →
`validator.py:12:MAX_COMPATIBILITY_LENGTH = 500`, exit 0 (one hit, not 0); executed pattern
`grep -niE -e 'max_lines' -e 'body length' -e '500 line' -e 'line_count'` → no output, exit 1. The
general clause still holds: `git ls-files | grep -c 'p_alias\|probes/'` → 0, and `.ufo/round-48/` tracks
only `instrument.json`, the oracle, the ruler and four receipts.

What closing it needs: (1) row 32 — a committed manifest naming the exact fixtures used (path plus
content hash, ~40 lines), or restate the cell as "36 fixtures, 29 distinct contents" with `counts.py` copied
in-lane; (2) row 56 — replace the printed pattern with the executed one at body line 56 (one line);
(3) the larger half — a committed re-run script that re-fetches the six sources by their cited URLs and
pinned commit and recomputes every row, ~80–120 lines plus one file, feasible but a wave item.

Carry sentence (R4): R4 is carried because its two unprovenanced counts live in a round-48 provenance
table that no round-50 counter reads, while this round's claims measure the SKILL.md description text (C1)
and the dispatch-prompt box proof (C2), so closing it would spend build seats without moving either counter.

## R5 — the v2 configured-root oracle is not frozen

State at base: only v1 is frozen — `.ufo/round-48/oracle/config-root-cases.json`, `schema`
`kotoba-configured-root-oracle-v1`, 13 cases, sha256 `1d09a38c…` (working tree and `git show HEAD:`
agree). No v2 file exists: `grep -rln 'configured-root-oracle-v2'` → only
`.ufo/waves/round-49/build/R5Disposition.md`; `ls .ufo/round-50/oracle` → absent; `git ls-tree -r HEAD`
under `.ufo/round-48/` has no second oracle or ruler. The v1 pin surface is intact and refuses
substitution: `instrument.json` `instruments.1.sha256` = `1d09a38c…`, `consumer.sha256` = `872993f8…`,
four receipts carry the same oracle hash, and the ruler enforces oracle-hash equality (`:161-163`), schema
equality (`:165-166`), a baseline receipt carrying that hash (`:179-181`), and refuses a non-BASE
revision without it (`:184-185`). The seven proposed v2 case values and rule sources are tabulated in
`R5Disposition.md` §6 (three identity cases red against the dir-keyed BASE, four nested scope rows), so
the remaining work is mechanical but must be pre-registered.

What closing it needs: one package opened before any measurement — a new
`.ufo/round-N/oracle/config-root-cases-v2.json` (20 cases = 13 v1 + 7, with a per-file `names` map and the
identity contract sentence), a `config-root-ruler-v2.py` accepting schema v2, a fresh BASE receipt whose
`oracle_sha256` is the v2 hash (BASE counts must be the `a5adc146` consumer `f576c23f…`, not v1's
`197b5a4`), and a new `instrument.json` pre-registering the argv. Two new tools, one oracle, one instrument,
one receipt; the nested rows must be labelled instrument-scope values, never loader parity. Item (a), the
built-in marker join, cannot be closed by any oracle case — it needs an operator decision on the name-slot
reading (`index.ts:277-278`) and a frozen carrier; editing v1 is ruled out by the hash/schema refusals.

Carry sentence (R5): R5 is carried because the v2 oracle must be frozen and its argv pre-registered before
any case runs, and round 50's claims measure two other instruments (C1 the SKILL.md description, C2 the box
proof), so opening the v2 triplet now would create an instrument this wave is not measuring.

## R1 — the no-name fallback counts a skill opencode v1.19.3 skips

State at base: `verifiers/verify_harness_independent.py` sha256 `54f9c95b…` is the exact hash
`MutR1Keying.md` records as its pristine round-49 head, so F1–F4 and M4 apply to these bytes unchanged.
`skill_identity` (`:311-312`) returns `name if isinstance(name, str) and name else dir_name`; the fallback
arm at `:1661` still expects count 3; the derive comment at `:673` still says the agents root "has always
fallen back to" the directory name.

Verified the opencode side this session from the pinned source (fetched 2026-10-22T12:29:54Z, HTTP 200,
11,843 bytes, sha256 `91dce57f…`, identical to the hash in `R5Disposition.md`): `:53-59`
`isSkillFrontmatter` requires `typeof data.name === "string"`; `:123` `if (!isSkillFrontmatter(md.data))
return`, with no event and no log; `:121` `if (!md) return` for an unreadable file; `:134` the skill is
keyed by `md.data.name`.

Probe of the landed module on six shapes (scratch `fx/`, exit 0); each is a skill opencode does not count
as R1 does:

| fixture | `read_frontmatter` | `skill_identity` | opencode v1.19.3 |
|---|---|---|---|
| no `name` | `{'description': …}` | `'no-name'` (dir) | skipped (`:123`) |
| `name: ""` | `{'name': ''}` | `'empty-name'` (dir) | loaded under key `""` |
| `name: 123` | `{'name': '123'}` | `'123'` | skipped, type is number |
| `name: x # note` | `{'name': 'x # note'}` | `'x # note'` | `x` |
| `"name": x` | `{}` | `'quoted-key'` (dir) | `x` |
| unreadable file | `{}` | `'unreadable'` (dir) | skipped (`:121`) |

Green test on the wrong rule: `--self-test` → exit 0, `0 failure(s) over 123 assertions`; the floor is
123 (`floors-registry.json:30`), so the fb arm passes with the divergent count and `MutR1Keying` M4
(fallback → `""`) still survives, bytes identical.

What closing it needs: (1) a contract decision — skip nameless and non-string names like opencode (empty
string keyed `""`), or keep the fallback and label it a deliberate bounded divergence in the docstring and
SCORECARD; (2) correct or implement the agents-root clause at `:673` (F2); (3) replace the fb count
assertion with a direct `skill_identity` assertion and add a second nameless skill, raising the assertion
count → `harness_independent` floor 123 → 124 in step with `check_assertion_floors.py`'s in-file tables;
(4) either declare the reader's accepted YAML subset or handle F3's twelve edge inputs, separable and the
expensive part. Roughly 20–30 lines in one file plus a floor bump, if the decision is limited to the skip
rule. Write collision noted: round 50's `FloorsRegister` seat already edits `floors-registry.json`
(`instrument_total` 10 → 11), so an R1 floor bump this wave would be a second writer to that file.

Carry sentence (R1): R1 is carried because closing it needs an identity-contract decision plus an
assertion-floor bump in the registry that round 50's D3 registration is already editing, and neither C1
(the description text) nor C2 (the box proof) depends on that operator.

Umbrella sentence (one line, if the report wants a single line): D6 is carried because its three items are
pre-registered-instrument, provenance and identity-contract work whose carriers are the harness verifier,
the round-48 oracle family and a round-48 provenance table, while round 50 measures C1 and C2, so no
closing action on any of the three could move either counter.
## Evidence (commands, exit codes, hashes)

- `git rev-parse HEAD` → `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`, exit 0; `git status --porcelain` →
  the two untracked round-50 paths only, exit 0.
- R4: `grep -n '24 not reproducible\|printed command cannot produce 0' …round48.md` → lines 149, 157,
  exit 0; `grep -n 'partly addressed'` → line 185, exit 0.
- R4 counts: `python3 -B …/R4CountProvenance/counts.py` → exit 0, `probe_files 36 probe_dirs 36
  probe_distinct 29`; per-root recursive `SKILL.md` glob → the fourteen numbers above, sum 36, exit 0;
  `git ls-files | grep -c 'p_alias\|probes/'` → `0`, exit 1.
- R4 row 56: printed pattern → one hit `validator.py:12:MAX_COMPATIBILITY_LENGTH = 500`, exit 0; executed
  pattern → no output, exit 1.
- R5: `jq -r '.schema, (.cases|length)' …/config-root-cases.json` → `kotoba-configured-root-oracle-v1` /
  `13`, exit 0; `git show HEAD:… | sha256sum` and `sha256sum` → both `1d09a38c…`, exit 0;
  `grep -rln 'configured-root-oracle-v2' .` → only `R5Disposition.md`, exit 0; `ls .ufo/round-50/oracle`
  → "No such file or directory", exit 2; `grep -rl '1d09a38c' .ufo/round-48/verification/ | wc -l` → 4,
  exit 0.
- R1: `sha256sum verifiers/verify_harness_independent.py` → `54f9c95b…`, exit 0 (equals `MutR1Keying`'s
  pristine hash); `python3 -B verifiers/verify_harness_independent.py --self-test` → exit 0, `0 failure(s)
  over 123 assertions`; `grep -n 'harness_independent' -A2 verifiers/floors-registry.json` →
  `"floor": 123`, exit 0; scratch probe over `fx/` → exit 0.
- Source read: `curl -sSL -o oc-index.ts -w 'status=%{http_code} bytes=%{size_download}'` on the pinned
  URL → `status=200 bytes=11843`, exit 0, 2026-10-22T12:29:54Z, sha256 `91dce57f…`; quotes at `:53`,
  `:121`, `:123`, `:134`; no fetched code executed.

## Remaining unknowns

- Whether 24 was ever a real count is unknown (fourteen probe roots plus ten nested fixtures is an
  arithmetic that fits, but nothing stores it); restating the cell is the honest close without a run list.
- Whether R5's v2 freezes `expected_base_count` at `a5adc146` or a later BASE is a Main call the base
  bytes cannot settle.
- Whether R1 should match opencode (skip) or declare the fallback a bounded divergence is undecided in
  every committed record; both are defensible and the choice sets the self-test arms.
