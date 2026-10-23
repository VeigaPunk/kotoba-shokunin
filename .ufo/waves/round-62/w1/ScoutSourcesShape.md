# ScoutSourcesShape — SOURCES / registry shape (round 62)

Seat: KotobaR62.ScoutSourcesShape. Read-only. No lane/fleet mutation. Scratch probes under `/fast/scratch/hyaku/kotoba-r62/ScoutSourcesShape/` are constructed inputs to the fleet script, not lane state.

Confidence: high on the row bytes, the snapshot hash, the live validator, and the W04/E04 branch. The plan does not freeze S118's `scope` cell, so "W04 by design" is conditional on that cell (measured below).

## S103 at tip — URL, sha, quote

Row: `kotoba-shokunin/corpus/SOURCES.md:115` (NF=13). The quote is **not** in the row. The ≤25-word quote is in `corpus/lessons/round-60.md:10` and is a prefix of the committed snapshot.

- URL: `https://code.claude.com/docs/en/memory.md`
- Normalized census key (`url_of` in `scripts/sources-census.sh:600-604`: strip fragment, strip one trailing slash, lowercase the host only): `code.claude.com/docs/en/memory.md`
- sha256: `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7`
- Access recorded on the row: fetched 2026-10-23T12:08:16Z, HTTP 200, 54,043 B, seat SrcClaudeCode
- Quote (`round-60.md:10`, 14 words): `memory.md:168`: "For larger projects, you can organize instructions into multiple files using the `.claude/rules/` directory."

Snapshot check, 2026-10-23T20:51:28Z:

```
$ sha256sum .ufo/waves/round-60/snapshots/S103.page
82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7
54043 bytes
```

Line 168 of that file begins with the Gate sentence and then continues ("This keeps instructions modular…"). The recorded quote is the first sentence only.

Exact row:

```
| S103 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Claude Code project rule files in `.claude/rules/` and frontmatter `paths` for matching-file scope (vendor documentation; not a runtime test) | § Organize rules with `.claude/rules/` (`memory.md:166,168`); § Path-specific rules (`:194-200`); rule frontmatter (`:246-250`); fetched 2026-10-23T12:08:16Z, HTTP 200, 54,043 B, sha256 `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` (seat SrcClaudeCode) | re-opens S043 — Claude Code documents `.claude/rules/` files and YAML frontmatter `paths` to scope rules to matching files | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md, corpus/lessons/round-60.md |
```

Same URL already on S043 (`SOURCES.md:56`), different scope (always-on files vs `.claude/rules/` + `paths`). S103's own `teaches` opens `re-opens S043 —`, not `re-opens S103 —`.

## What a `re-opens S103 —` row looks like (S114 / S115)

No row at tip teaches `re-opens S103 —`. S114 re-opens S048; S115 re-opens S108. Both are the shape to copy: `teaches` opens `re-opens SNNN — ` (em dash), the URL is the re-opened row's URL, and the **scope string differs** from that row. `re-opens` is not the contract's correction prefix. Contract rule 2 (`/home/vgpnk/Projects/shokunin/CORPUS.md:117-118`) says a correction's `teaches` opens `supersedes S0NN —`. The E04 exemption (`sources-census.sh:646-648`) matches only `supersedes S[0-9]{3}`.

S114 (`SOURCES.md:126`), teaches:

```
re-opens S048 — canonical scope-key set: Copilot CLI documents `.github/instructions/**/*.instructions.md` and names `applyTo`; scope-key[Copilot CLI]=applyTo
```

URL `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` (also S048 and S106). Scope is not S048's scope.

S115 (`SOURCES.md:127`), teaches:

```
re-opens S108 — Cursor project rule files live under `.cursor/rules` as `.mdc` files, and `globs` scopes rules to specific files or directories; scope-key[Cursor]=globs
```

URL `https://cursor.com/docs/rules` (also S108). S049 is `https://cursor.com/docs/rules.md` — a different census key (`.md` is not stripped).

A `re-opens S103 —` row is that pattern with the S103 URL and a scope string that is not S103's and not S043's:

```
| S118 | <title> — https://code.claude.com/docs/en/memory.md | docs | A | <scope text different from S043 and from S103> | <heading / memory.md:line; fetch date; bytes; sha256> | re-opens S103 — <one grounded benefit> | mined | 2026-10-23 | 90d | <repo-relative paths that exist> |
```

Ids: 115 rows, S001–S117, unused **S092** and **S116**. S118 is free. The plan names S118; this seat does not renumber.

## Does the planned S118 URL produce W04 by design?

**Yes, if the new scope text differs from both existing holders of that URL. No, if the scope cell is copied from S103: that is E04, exit 1, because `re-opens` does not exempt.**

Mechanism (`sources-census.sh:643-649`):

- `scope_key = normalized_url SUBSEP scope`
- W04 when the URL was already seen and this `scope_key` was not. Warning. Header line 33: warnings do not affect clean lanes. Selftest `W04-does-not-fail-validation` expects exit 0 (`sources-census.sh:361-365`). Header exit legend (`:16-18`): 0 clean or warnings; 1 E-codes or overdue; 2 usage/missing registry; 3 selftest failure.
- E04 when the same URL **and** the same scope are already held by a non-rejected row, this row is not `rejected`, and `teaches` does not match `supersedes S[0-9]{3}`.

Live tree already warns on this URL (S043 then S103). S114 and S115 are the same pattern and are already in that warning list.

Constructed probe (copy of `corpus/SOURCES.md` at `…/probe-lane/corpus/SOURCES.md`, `lessons/`, `knowledge/`, and `SKILL.md` symlinked so E11 resolves; `--today 2026-10-23`). Not lane state.

| case | teaches | scope | result |
|---|---|---|---|
| diff-scope | `re-opens S103 — …` | new text | exit **0**. Adds `file W04 S118 duplicate url code.claude.com/docs/en/memory.md across scopes`. No E-code. |
| same-scope | `re-opens S103 — …` | exact S103 scope | exit **1**. `file E04 S118 duplicate url code.claude.com/docs/en/memory.md within scope …`. No W04 for S118. |
| same-scope | `supersedes S103 — …` | exact S103 scope | exit **0**. No S118 W04 and no E04. Pre-existing `W04 S103` remains. |

So a S114/S115-style re-open (different scope, `re-opens` not `supersedes`) adds one W04 and stays exit 0. That is the design. Copying S103's scope with `re-opens` fails validation.

## Where `corpus/README.md` indexes entries

The index is the `## Coverage map` table only: `corpus/README.md:5` through the next `##` heading, `## Frontier` at line 108.

Harvester: `verifiers/verify_corpus_integrity.py` `file_column_tokens` (`:361-394`). It takes backticked tokens in **column 2** (the File cell) of `|` rows inside that section. Fenced rows do not count as promises. A tracked `corpus/` file other than `README.md` that no such token matches is `corpus.index.unindexed` (zero required). Round-61 rows are lines 104–106. A new `corpus/knowledge/…` or `corpus/lessons/round-62.md` is indexed by a new Coverage-map row **before** `## Frontier`, File cell backticked, path relative to `corpus/` for files inside it (`knowledge/….md`, `lessons/round-62.md`) or `../` for paths outside `corpus/`. This seat did not run `verify_corpus_integrity.py`.

## Row skeleton (column order)

From `CORPUS.md:86` and `corpus/SOURCES.md:12`. Eleven columns. A data row splits to NF=13 (empty fields outside the pipes). No `|` inside a cell.

```
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
```

- `id` — `S` + 3 or more digits, next unused, never reused
- `source` — title — canonical URL
- `kind` — `spec|docs|paper|code|tool|dataset|talk|book|community|own-work`
- `tier` — `A|B|C` (`community` never A)
- `scope` — the claim the tier applies to (this string is the W04/E04 discriminator)
- `anchor` — section/line plus revision; never a bare homepage
- `teaches` — one benefit; a re-open here is `re-opens S103 — …`; a correction is `supersedes S103 — …`
- `status` — `queued|mined|rejected`
- `opened` — ISO date, not in the future
- `recheck` — ISO date, `NNd`, or symbolic (`90d`, `on-release`, `on-commit`)
- `used-by` — comma-separated repo-relative paths, or `—`. `mined` plus `—` is W03. `mined` plus a missing path is E11.

## Census

`CORPUS.md:131-148` ("Census — run from the lane root") is **seven** commands, not four. The four whose comments state a required result, run from the lane root at 2026-10-23T20:51:28Z, all exit 0:

| # | command (CORPUS.md) | required stdout | measured | exit |
|---|---|---|---|---|
| 1 | malformed rows, `awk` NF!=13, `END{print n+0}` | `0` | `0` | 0 |
| 2 | duplicate ids, `awk` ids \| `sort` \| `uniq -d` | nothing | empty | 0 |
| 3 | enum / tier-inflation `awk` | nothing | empty | 0 |
| 4 | mined `used-by` paths exist (`awk` \| `while read`) | nothing | empty | 0 |

The other three in the same fence, same run, also exit 0 (no required constant in the doc; `grep -c` exits 1 only when the count is 0):

- rows: `115` exit 0
- tier (`$5`): `A=112 B=2 C=1` exit 0
- status (`$9`): `mined=107 queued=7 rejected=1` exit 0

107+7+1=115. These four are the contract's "must print 0 / must print nothing" checks. Expected exit on this registry: **0, 0, 0, 0**.

### Validator (pasted)

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-23T20:51:28Z

$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

Fifteen W04 lines, no E-code. Same set as `.ufo/waves/round-62/census-before.txt` (that file is 2026-10-23T20:44:55Z; this re-run is later). S103, S114, and S115 are already W04.

Not in CORPUS.md; measured the same evening because the script's data modes are the other census surface. `census` and `shared` at 2026-10-23T20:52:33Z:

```
$ sources-census.sh census --root /home/vgpnk/Projects/shokunin kotoba
kotoba	rows	115
kotoba	tier.A	112
kotoba	tier.B	2
kotoba	tier.C	1
kotoba	status.mined	107
kotoba	status.queued	7
kotoba	status.rejected	1
FLEET	rows	115
FLEET	tier.A	112
FLEET	tier.B	2
FLEET	tier.C	1
FLEET	tier.invalid	0
FLEET	status.queued	7
FLEET	status.mined	107
FLEET	status.rejected	1
FLEET	status.invalid	0
FLEET	missing	0
exit=0

$ sources-census.sh shared --root /home/vgpnk/Projects/shokunin kotoba
(empty)
exit=0
```

`shared` with one lane prints nothing (a shared URL needs two lanes). `overdue` at the same stamp: exit 0, cadence lines only, no `overdue` line. ISO-date rows do not appear as cadence; S043, S046, and S060 were absent from the cadence list and were not overdue. `selftest` was not run.

## Gaps

- S118's scope sentence is not in the plan, so W04 vs E04 is not fixed until that cell is written.
- `verify_corpus_integrity.py` was not run.
- No lsp server was required; these are markdown rows and the census script, read directly.

installs: no installs
blockers: none
Attacked: S103 URL/sha/quote, the S114/S115 `re-opens` shape, and whether S118's memory.md URL is a W04 by design.
