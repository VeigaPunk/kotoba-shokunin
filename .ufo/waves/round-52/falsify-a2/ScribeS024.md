Result: MIXED — the carried S024 superseding row (S039) can be written this round with no new census warning, but S024's recorded HTML-route hash is now stale and the scope cell must stay byte-identical to S024's for that no-warning outcome.

Seat `KotobaR52a2.ScribeS024`. Carried item 4 of the round-51 spot-check: a superseding SOURCES row for
S024 (opencode Agent skills, https://opencode.ai/docs/skills). Lane `kotoba-shokunin`. I edited no lane file
except this report; every write I made went to my own scratch dir
`/fast/scratch/hyaku/kotoba-r52a2/ScribeS024/`. No tools installed or upgraded (nothing needed).

## 1. Re-open of the source (fetch record)

Ordinary means only (`curl`, no browser, no access-control circumvention).

```
$ cd /fast/scratch/hyaku/kotoba-r52a2/ScribeS024
$ date -u +%Y-%m-%dT%H:%M:%SZ          # 2026-10-22T17:50:09Z
$ curl -sS -L -w '%{http_code} %{content_type} %{size_download}\n' -o skills.md https://opencode.ai/docs/skills.md
200 text/plain; charset=utf-8 5365     # exit 0
$ date -u +%Y-%m-%dT%H:%M:%SZ          # 2026-10-22T17:50:09Z
$ wc -c < skills.md                    # 5365
$ sha256sum skills.md
f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561  skills.md
```

* URL `https://opencode.ai/docs/skills.md` — HTTP 200, `text/plain; charset=utf-8`, **5,365 B**,
  **sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561`** at **2026-10-22T17:50:09Z**.
* Two further `.md` fetches later in the same session returned the same digest → the `.md` route is
  byte-stable.
* The `.md` bytes are **byte-identical to the digest S024 already records** (`f10ced73…`,
  `corpus/SOURCES.md:37`), so the prose this row quotes did not move.
* HTML route `https://opencode.ai/docs/skills` at 17:51:13Z: HTTP 200, `text/html`, **73,201 B**,
  **sha256 `1f918b527340f86c53d5866e11ab837e87e9e245f8550f3f3eee98190a06460c`** (3 fetches, one digest);
  footer stamp `<time datetime="2026-10-22T16:30:59.000Z">Oct 22, 2026</time>`.

Anchor lines in the fetched bytes (line numbers are of the fetched `skills.md`, 231 lines, last line
unterminated):

| line | content |
|---|---|
| 133 | `## Configure permissions` (section runs 133-156) |
| 152-154 | permission table rows `allow` / `deny` / `ask` |
| 153 | `` | `deny`     | Skill hidden from agent, access rejected  | `` |
| 160 | `## Override per agent` (160-188) |
| 192 | `## Disable the skill tool` (192-219) |
| 223 | `## Troubleshoot loading` (223-231) |
| 230 | `4. Check permissions—skills with `deny` are hidden from agents` (em dash = U+2014, bytes `e2 80 94`) |

The round-51 lesson's claim that the permission lever lives at `skills.md:133-156, 230` is confirmed
against the live bytes; the page also documents the per-agent override (`:160-188`) and
`tools: skill: false` (`:192-219`), and **no registry row records them**: `grep -c 'permission'
corpus/SOURCES.md` → 1 (the round-51 search-log line `:121`), `grep -c 'tools: skill'` → 0,
`grep -c 'autoinvoke'` → 2 (S024's row `:37` and the same search-log line).

## 2. Draft row S039 — 11 cells, column order of S038

`corpus/SOURCES.md` header order is
`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`
(`corpus/SOURCES.md:12`; the S038 row is `:51`). The row below is the copy-ready text (one line, 1,467
chars; `NF=13` verified by `awk -F'|'`), with `scope` **byte-identical to S024's scope cell**
(`corpus/SOURCES.md:37`) so that the census raises no new warning:

```
| S039 | opencode — Agent skills — https://opencode.ai/docs/skills | docs | A | What opencode's own documentation states about how a skill's description reaches the model, and whether it documents a tie-break between two skills whose descriptions both match (vendor documentation for opencode's current release; not a measurement of omp or of opencode v1.19.3) | § Configure permissions (`skills.md:133-156`); § Override per agent (`skills.md:160-188`); § Disable the skill tool (`skills.md:192-219`); § Troubleshoot loading, item 4 (`skills.md:230`); re-opened as https://opencode.ai/docs/skills.md on 2026-10-22T17:50:09Z (200, 5,365 B, sha256 `f10ced73…`, text/plain), byte-identical to the S024 fetch; the HTML route (200, 73,201 B, sha256 `1f918b52…`) now stamps "Last updated: Oct 22, 2026" (`<time datetime="2026-10-22T16:30:59.000Z">`), so S024's recorded HTML hash `4d96fa56…` and its "Oct 20, 2026" stamp are stale | supersedes S024 — the page documents a pattern-based `permission.skill` gate in `opencode.json` where `deny` hides the skill from the agent and rejects access, `ask` prompts the user and `allow` loads it immediately, plus a per-agent `permission.skill` override and `tools: skill: false`; S024's claim that the only collision controls are name uniqueness and `opencode/autoinvoke: "false"` is contradicted by these same-page levers | mined | 2026-10-22 | 90d | corpus/knowledge/skill-overlap-levers-round51.md, corpus/lessons/round-52.md |
```

Cell-by-cell (what each cell asserts and where it is grounded):

1. **id** `S039` — next unused id; the lane's ids run S001-S038 (`corpus/SOURCES.md:14-51`), and `S039`
   appears nowhere in the lane outside this wave's own dispatch JSON.
2. **source** `opencode — Agent skills — https://opencode.ai/docs/skills` — same cell as S024 (the canonical
   HTML URL; the `.md` route is the fetch target and is named in the anchor cell).
3. **kind** `docs` — vendor documentation.
4. **tier** `A` — the page is opencode's own documentation for opencode's current release; S024 already
   carries tier A for the same URL and the scope note ("not a measurement of omp or of opencode v1.19.3") is
   kept verbatim, so no tier inflation is introduced.
5. **scope** — S024's scope cell, byte-identical (582 chars incl. surrounding spaces). This is the
   load-bearing choice; see §5.
6. **anchor** — four line-level section anchors plus the fetch record, and the fresh HTML-route hash that
   corrects S024's stale one (§7 F1).
7. **teaches** — opens `supersedes S024 —` as contract v1 rule 2 requires ("a correction is a new row
   whose `teaches` opens `supersedes S0NN —`", `CORPUS.md` § SOURCES.md rule 2). One grounded benefit: the
   page documents permission-level removal levers (`deny` / `ask` / `allow`, per-agent override, tool
   disable) that S024's cell omits and that S024's "its only collision controls are ..." clause is
   contradicted by. No `|` inside any cell (markdown table safety) — asserted mechanically.
8. **status** `mined` — cited by ≥1 path in `used-by` (contract § status).
9. **opened** `2026-10-22` — the date of this re-open; census E08 wants a past/present ISO date.
10. **recheck** `90d` — same cadence as S024 (the page is unversioned vendor documentation).
11. **used-by** — two variants, see §6.

## 3. Gate entry for `corpus/lessons/round-52.md`

House format of that file's `## Gate` → `### Admitted` block (`corpus/lessons/round-52.md:13-40`); the
bullet below is copy-ready and carries URL, access date, byte count, sha256 and a located ≤25-word quote:

```
- **S039** (supersedes S024; carried item 4 of the round-51 spot-check) — https://opencode.ai/docs/skills.md,
  re-opened 2026-10-22T17:50:09Z, 5,365 B, sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561`
  (byte-identical to the S024 fetch; the HTML route is 73,201 B, sha256 `1f918b527340f86c53d5866e11ab837e87e9e245f8550f3f3eee98190a06460c`,
  stamping "Last updated: Oct 22, 2026"). Quote (`skills.md:230`): "Check permissions—skills with `deny` are hidden from agents"
```

* Quote is verbatim from the fetched bytes (line 230, em dash U+2014), **8 words** (`wc -w` → 8, limit 25).
* Optional second located quote if the L1 prefers the table row: `skills.md:153` — `` | `deny` | Skill hidden
  from agent, access rejected | `` (a markdown table row; the round-51 lesson rejected a table-row quote for
  a *registry cell* because of the `|` characters, which does not apply to a prose Gate bullet).
* The Gate bullet also needs the sweep line the other rows carry (`corpus/lessons/round-52.md:39-40`: the
  `grep -c` sweep). For S039 the sweep over the fetched markdown is `grep -c 'deny'` → **3** (lines 143, 153,
  230; `grep -o 'deny' | wc -l` → 3), and `grep -c 'permission'` → 7. Measured on the fetched bytes.

## 4. Old → new log line for S024's status

**S024's `status` does not change. No old→new line is owed for S024.**

Precedent, from the same file the L1 will edit (`corpus/lessons/round-52.md:60-62`, the round-52 lesson's
"Rows touched (old → new)"):

```
### Rows touched (old → new)

None of S001–S031 changed in place. S031's `teaches` is superseded by the new row S038 (append-only, contract rule 2).
```

S031 was superseded by S038 and **no cell of S031 changed** (`corpus/SOURCES.md:44`: `status` still `mined`,
`recheck` still `90d`, `used-by` still only the round-51 entry — the round-52 lesson is *not* in it). The
same holds for S024. Copy-ready replacement for line 62:

```
None of S001–S031 changed in place. S024's `teaches` is superseded by the new row S039, and S031's `teaches` is superseded by the new row S038 (append-only, contract rule 2).
```

And if the L1 wants an explicit per-row record, this is the honest one (nothing changes):

```
- S024: `status` mined → mined, `recheck` 90d → 90d, `used-by` unchanged (`corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md, corpus/knowledge/skill-overlap-levers-round51.md`) — no in-place cell change; the narrower `teaches` is superseded by the new row S039 (append-only, contract rule 2).
```

Do **not** extend S024's `used-by` with `corpus/lessons/round-52.md`: the S031 precedent keeps the
superseded row's `used-by` unchanged even though the round-52 lesson records its supersession.

## 5. Would the census warn on the duplicate URL? — measured

Today's census on the untouched lane (2026-10-22T17:49:59Z):

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
EXIT=0
```

**S038 produces no W04 even though it duplicates S031's URL.** The reason is in the implementation
(`scripts/sources-census.sh:643-649`): W04 fires only when the same URL appears with a *different* `scope`
cell text; S038's scope cell is byte-identical to S031's (verified by splitting both rows), so the
`(url, scope)` pair already exists and no warning is printed. E04 (duplicate URL **within** one scope) is
exempted only by the literal token `supersedes S0NN` in the `teaches` cell.

I reproduced this on scratch copies of the lane registry (never in the lane), each with `corpus/knowledge`
and `corpus/lessons` symlinked so the E11 used-by check resolves:

| scratch lane | S039 variant | census output | exit |
|---|---|---|---|
| `census-0` | none (baseline copy of today's lane file) | 3 W04 (S018, S019, S021), `ok` | 0 |
| `census-A` | `scope` **byte-identical** to S024's; `teaches` opens `supersedes S024 —` | 3 W04 (S018, S019, S021), `ok` — **no new line** | 0 |
| `census-B` | `scope` widened to cover the permission levers | 4 W04 — adds `W04 S039 duplicate url opencode.ai/docs/skills across scopes` — `ok` | 0 |
| `census-C` | as A, but `used-by` = lesson only | 3 W04, `ok` | 0 |
| `census-E` | as A, but `teaches` **without** the literal `supersedes S024` | `E04 S039 duplicate url opencode.ai/docs/skills within scope …` | **1** |

Answer to the question as asked: **the census does not warn on the duplicate URL if S039 keeps S024's
scope cell byte-identical** (the S038 pattern), and it warns **W04** — a warning only, exit still 0,
`kotoba ok` — if the scope cell is changed at all. The W04 that a widened scope would add is the same
class the lane already carries three times (S018, S019, S021 — all superseding rows whose scope was
rewritten), and the round-48 build seat called that class "the accepted cost of rule 2's superseding
mechanism" (`.ufo/waves/round-48/build/FrSourcesRowsScribe.md:141`).

This also reproduces, independently, the routed defect's own census probe, quoted verbatim from
`corpus/lessons/round-51.md:169-172`:

> **S024 `teaches` gap** (`ReopenS024.md`): the Gate reason above for not writing a superseding row is
> wrong as stated. A superseding row with the same `scope`, placed below S024, raises no W04 and no
> E04 (census probe, exit 0). The narrower `teaches` cell is carried to round 52 as a superseding row;
> the entry already carries the page's permission and metadata levers.

My measurement confirms it: same scope → no W04, no E04, exit 0.

## 6. `used-by` variants (pick one)

* **Recommended (as drafted above):** `corpus/knowledge/skill-overlap-levers-round51.md, corpus/lessons/round-52.md`.
  The entry's `source:` line already cites the permission anchors (`skills.md:133-188, 230`,
  `corpus/knowledge/skill-overlap-levers-round51.md:1`) — but it cites them under **S024**, whose anchor
  cell does not cover the permission section, which is exactly the gap this row closes. If S039's
  `used-by` names the entry, the L1 should therefore also append S039 to that `source:` line (keeping
  S024 for `skills.md:45, 128-129`), so the citation and the row match. Census E11 passes either way
  (both paths exist) — this is a provenance-honesty call, not a gate call.
* **Zero-edit alternative:** `corpus/lessons/round-52.md` only (exactly S038's shape,
  `corpus/SOURCES.md:51`), leaving the round-51 entry untouched. The lesson's Gate bullet cites S039, so
  `mined` is truthful.

## 7. Findings (each with severity)

**F1 — medium — S024's anchor cell carries a stale HTML-route hash and a stale footer stamp.**
`corpus/SOURCES.md:37` records "the HTML route (200, 73201 B, sha256 `4d96fa56…`) carries the footer stamp
'Last updated: Oct 20, 2026'". Today's HTML fetch: 200, 73,201 B, sha256 `1f918b52…`, stamp "Oct 22, 2026"
(`<time datetime="2026-10-22T16:30:59.000Z">`). Same byte count, different digest — the stamp string is the
same length, so only the hash reveals the change. The page was rebuilt at 2026-10-22T16:30:59Z. The `.md`
route is unchanged (`f10ced73…`), so no quoted fact moved. Contract rule 2 forbids editing S024's anchor in
place, so the correction can only ride in on the superseding row — which is why S039's anchor cell carries
the fresh HTML record. *Fix:* land S039 with the anchor cell drafted above; do not edit S024.

**F2 — medium — the round-51 L1's stated reason for not writing this row is false as stated.**
`corpus/lessons/round-51.md:63-67` says: "a superseding row with the same URL would add a W04
duplicate-URL warning, so the narrower cell stays". Measured: a superseding row with the same URL **and the
same scope** adds no W04 and no E04 (exit 0, `census-A`). W04 is scope-sensitive
(`scripts/sources-census.sh:643-645`) and S038 already proves it on the same URL pair. The same file
already carries the correction at `:171` (quoted in §5), so the residual defect is that the *Gate reason at
:63-67* still stands uncorrected next to it. *Fix (L1):* record the erratum in the round-52 lesson
(append-only); do not edit `round-51.md`.

**F3 — low — a widened scope would add a census warning.** See §5 (`census-B`): one extra W04 line, exit
still 0. Acceptable but avoidable; the routed defect's instruction ("with the same `scope`") points at the
no-warning form. *Recommendation:* keep S024's scope cell byte-identical (as drafted).

**F4 — low — a landmine in the no-warning form.** With an identical scope, the `teaches` cell must contain
the literal token `supersedes S024`, otherwise the census raises **E04 and exits 1** (`census-E`; the
exemption is `teaches !~ /supersedes S[0-9]{3}/`, `scripts/sources-census.sh:646-649`). Any rewording of
the first clause of the `teaches` cell (e.g. "supersedes S024:") still matches; dropping the row id does
not. *Check before landing:* `grep -c 'supersedes S024' corpus/SOURCES.md` → ≥1.

**F5 — low — do not add a `check_correction_sweep.py` registry row for this supersession.**
`verifiers/check_correction_sweep.py:30-37` holds three registry rows (README / SCORECARD / PROVINCE) and
its own docstring says "A new superseded claim is added as a new registry row; rows are not edited". The
sweep requires the DECLARED pattern to appear **in the same Markdown block** as the STALE pattern
(`verifiers/check_correction_sweep.py:63-77`). A registry row scoped to `corpus/SOURCES.md` whose stale
pattern is S024's `teaches` text would therefore be red by construction: the S024 row block cannot contain
`supersedes S024` without editing `teaches` in place, which contract rule 2 forbids. S024's cell is narrow
but not false, so it is not a "superseded claim" of the kind the sweep registry targets. *Recommendation:*
no new sweep registry row for this item.

**F6 — info — counters the L1's other surfaces will move.** Measured on the scratch registry
(`sources-census.sh census`): rows 38 → 39, tier.A 36 → 37, status.mined 29 → 30 (queued 8, rejected 1
unchanged). Any lane prose that states the registry size must be swept — `corpus/README.md:75` names the
seven client rows "(S030, S031, S025, S022, S024, S029, S021)" and could name S039;
`corpus/README.md:147-149` (Core note) already records the opencode permission `deny` lever, so it needs no
correction. I did not find a committed "38 rows" claim in `corpus/README.md`, `SCORECARD.md` or
`PROVINCE.md`; `grep -n '38 rows' …` → no hit.

## 8. Conflicts, verbatim

1. `corpus/lessons/round-51.md:65-66` (the L1's Gate reason): "and a superseding row with the same URL would
   add a W04 duplicate-URL warning, so the narrower cell stays and the entry carries the fuller reading".
   → **Contradicted** by measurement (`census-A`: no W04, exit 0) and by `corpus/lessons/round-51.md:171`
   ("A superseding row with the same `scope`, placed below S024, raises no W04 and no E04 (census probe,
   exit 0)").
2. `corpus/SOURCES.md:37` (S024 anchor): "the HTML route (200, 73201 B, sha256 `4d96fa56…`) carries the
   footer stamp 'Last updated: Oct 20, 2026'". → **Stale**: same byte count, today's sha256
   `1f918b527340f86c53d5866e11ab837e87e9e245f8550f3f3eee98190a06460c`, stamp "Oct 22, 2026".

## 9. Out of scope / not done (for the L1)

* I did **not** edit any lane file except this report: no row written, no Gate entry appended, no lesson
  edit, no entry/README amendment, no commit, no push, no git write of any kind in the lane.
* I did not run any lane verifier (`check_correction_sweep.py`, `check_mcp_instructions.py`,
  `check_callee_rename.py`) — outside this seat's target, and the L1 owns the gate matrix.
* I did not re-open S031/S038's URL (no need for this item) and did not touch the fixture-label or D2/D7/R1/R5
  carried items.
* Whether the round-51 entry's `source:` line should gain S039 (§6) is a lane-authoring decision I left to
  the L1.

## 10. Artifacts (all under my own scratch dir, nothing pushed)

* `/fast/scratch/hyaku/kotoba-r52a2/ScribeS024/skills.md` — the fetched page (5,365 B, sha256 `f10ced73…`).
* `/fast/scratch/hyaku/kotoba-r52a2/ScribeS024/skills.html`, `h1.html`, `h2.html`, `h3.html` — HTML route
  (73,201 B, sha256 `1f918b52…`).
* `/fast/scratch/hyaku/kotoba-r52a2/ScribeS024/fetch-time.txt` — UTC stamps (2026-10-22T17:50:09Z).
* `/fast/scratch/hyaku/kotoba-r52a2/ScribeS024/row-F1.txt` (drafted row, recommended `used-by`) and
  `row-F2.txt` (lesson-only `used-by` variant) — the exact bytes of the drafted row.
* `/fast/scratch/hyaku/kotoba-r52a2/ScribeS024/census-{0,A,B,C,E,F1,F2}/kotoba-shokunin/` — scratch lane
  copies used for the census measurements in §5 (symlinked `corpus/knowledge`, `corpus/lessons`, `SKILL.md`;
  the registry file is a copy with the S039 row appended, the lane file itself untouched).

Command set actually run, with exits: `curl` (§1, exit 0), `sha256sum`/`wc -c` (§1, exit 0),
`grep -n`/`awk` line probes (§1, exit 0), `sources-census.sh validate|census` (§5, exits 0/0/0/0/1/0/0 as
tabulated), `git -C <lane> status --porcelain` (read-only, exit 0 → `M SCORECARD.md` — the inherited
attempt-1 diff, not mine — and `?? .ufo/waves/round-52/`, the untracked wave dir that now holds this
report). No git write, no jj command, no push. Tools installed: **none**.
