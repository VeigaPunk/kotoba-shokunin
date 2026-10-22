# SourcesContract — frontier-step mechanics for C2's rows (round 51, build wave)

**Result: MECHANICS SETTLED for C2's `corpus/SOURCES.md` work.** The registry stays census-clean (exit 0,
the same three W04 lines the plan expects before and after) if the six existing rows are edited only in
`used-by`, the new Copilot SDK row is appended inside `## Registry` with 11 columns, and the entry file
exists before the gate runs. Two traps: an in-place `anchor`/`teaches` edit breaks contract v1 rule 2
yet the census cannot see it (observed exit 0), and re-using an old URL with a *different* `scope`
string raises a new W04 even when `teaches` says `supersedes`.

Read: `CORPUS.md:64-140` (contract v1); `scripts/sources-census.sh` sha256 `3fb72615…` (rules `:620-676`).

## 1. Observed facts

- 29 rows (`grep -c '^| S' corpus/SOURCES.md` → `29`); max id `S029`, `grep -c 'S030'` → `0`, so the
  next id is **`S030`**. Headings at lines 10 (`## Registry`), 44 (`## Paths`), 62, 113; rows end at
  line 42, so a new row goes between line 42 and `## Paths`.
- S021/S022/S024/S025/S028/S029 already read `status=mined`, `recheck=90d`, `opened=2026-10-22`, each
  `used-by` naming two or three round-49/50 files.
- The Copilot SDK URL `https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills` is in no
  row; round 50's seat opened it (`.ufo/waves/round-50/build/SrcCopilotSkills.md:19,34`: 200, 35,455 B,
  sha256 `64856ff4…`), § Skill conflicts at lines 805-810 carrying the D4 lever.
- Same-round `mined` precedent: `a78fec1` ("new entry skill-selection-rules-round50 (S024-S029, S022,
  S019) cited…"); round-50 § Gate (`corpus/lessons/round-50.md:44-46`) lists S024-S029 "new, `mined`".
- Not contract-clean precedent: `bf109ca` rewrote S019/S022/S026/S028 `anchor`/`scope`/`teaches` in
  place, logged at round-50 § Gate as "S019 and S022 also gain anchor, scope and teaches text". Rule 2
  permits only `status`, `recheck`, `used-by` in place; a correction is a new row with `supersedes`.

## 2. (1) Rules for S030 and for touching the six rows

Census codes, each verified on a scratch copy of the lane registry (`/fast/scratch/hyaku/kotoba-r51/build/SourcesContract/mut`):

| change | code | observed |
|---|---|---|
| ≠11 columns, e.g. a pipe character inside a cell | E01 exit 1 | `E01 S030 fields=12` |
| id off `S[0-9]{3,}` / duplicate id | E02 / E03 exit 1 | rule only; S030 unused |
| new row reuses an old URL **and** its scope string, `teaches` lacks `supersedes S###` | E04 exit 1 | exit 1 |
| same, `teaches` opens `supersedes S028 —` | none | exit 0 |
| new row reuses an old URL with a **different** scope string, with or without `supersedes` | **W04** exit 0 | `W04 S030 duplicate url … across scopes` in both |
| `kind` off the 10-value enum / `tier` off ABC / `community` at A | E05 / E06 / E10 exit 1 | rule only |
| `status=watch` or any non-enum | E07 exit 1 | `E07 S030 status=watch` |
| `opened` not ISO or later than today's UTC date | E08 exit 1 | rule only; `2026-10-22` valid |
| `recheck` not ISO / `NNd` / symbolic (`on-release`, `on-commit`) | E09 exit 1 | rule only; `90d` fine |
| `mined` row whose `used-by` path is absent | E11 exit 1 | `E11 S030 missing used-by corpus/knowledge/skill-overlap-levers-round51.md` |
| row after `## Paths` (any non-`Registry` section) | E12 exit 1 | `E12 S030 row outside Registry section` |
| tier C + mined / thin reject / mined with used-by `—` | W01 / W02 / W03 warnings | rule only |

For S030 realistically only W03 can appear (used-by `—`, which also blinds the C2 counter); no W04,
because the URL is new.

**Log in the round lesson § Gate** (rule 1 for new rows, rule 2 for in-place changes):
1. S030 — URL, UTC access time, ≤25-word quote with its location grounding `teaches`, in round-50's
   four-column shape `| row | URL | accessed (UTC) | quote, at most 25 words (location) |` with the seat
   report inside the quote cell (`corpus/lessons/round-50.md:56-69`).
2. Each of the six rows — `status` old→new (`mined`→`mined`), `recheck` old→new (`90d`→`90d`),
   `used-by` old→new (existing paths → those plus `corpus/knowledge/skill-overlap-levers-round51.md`), in
   round-50's sentence shape ("Status `mined` → `mined`; recheck `90d` → `90d`; `used-by` A → A, B").
3. D4 — the round-50 reject reason ("provider catalogs, not SKILL.md routing") is wrong; record the
   corrected reason and that the row is now written. A drafted-and-unwritten row needs its reason plus
   pointer (round-50 "Rejected, with reasons"); a silent drop has no record.

**New W04 or error, concretely.** New W04 only from a re-used URL under a different scope string: writing
the six rows as superseding rows with re-worded `scope` cells adds up to six W04 lines, while
`plans/round-51.md:61-64` expects three before and after, so copy `scope` verbatim or leave it alone.
- New errors: E11 if the entry is not at the exact path (a near-miss name still satisfies the counter's
  substring test, so E11 is the only catch); E01 from any `|` in a cell; E12 after `## Paths`; E04 for a
  re-used URL plus scope without `supersedes`; E03 from a reused S030; E07 from `watch`.
- Invisible to census and still illegal: editing `anchor`/`teaches` of an existing row. A mutant that
  removes `supersedes S013 —` from S021 validates `ok`, exit 0 — the census keeps no old values, so only
  the log and review catch it. Compliant form: a new row with the same URL and `scope`, `teaches` opening
  `supersedes S022 —`. For C2, change neither cell; the counter reads `status` and `used-by` only.

## 3. (2) Column shape and status values

`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` over
`|---|---|---|---|---|---|---|---|---|---|---|` (`corpus/SOURCES.md:12-13`). Eleven cells ⇒ **13** `|`-separated
fields; the check is `NF==13`; a stray pipe inside a cell reports `fields=12`.
- `id` = `S` + three or more digits, never reused; `kind` one of `spec docs paper code tool dataset
  talk book community own-work`; `tier` one of `A B C` scoped to `scope`, `community` never A; `status`
  one of **`queued` | `mined` | `rejected`** (`watch` is not a status); `opened` ISO date; `recheck` ISO
  date, `NNd`, or symbolic cadence; `used-by` repo-relative paths or `—` (`CORPUS.md:80-100`).
- No `|` inside a cell. The maintained parser accepts 0-3 leading spaces before a heading or row and
  ignores 4 or more as indented code; the frozen manual census examples assume column zero.
- Rows live only under a heading whose text is exactly `Registry` (E12 otherwise).

## 4. (3) `mined` while the citing entry lands in the same round

**Yes.** Contract v1 defines `mined` as "cited by ≥1 path in `used-by`" with no round-distance rule, and
rule 1 only requires the author to open the source that round. The one ordering constraint is E11:
`used-by` resolves against the lane tree at validate time. Observed on one row: entry absent → `E11`,
exit 1; entry present → `ok`, exit 0. The census never reads entry content; the C2 counter does.

## 5. (4) Canonical run (read-only, no `--out`)

`./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`, from
`/home/vgpnk/Projects/shokunin`, 2026-10-22T14:23:01Z, script sha256 `3fb72615…`:

```
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
EXIT=0
```

No E codes, three W warnings, exit 0; S018/S019/S021 are pre-existing re-scoped supersede rows.

## 6. Checklist for the L1

1. Land `corpus/knowledge/skill-overlap-levers-round51.md` first (its `## Levers by client` table,
   `| client | row | lever | quote |`), so no interim gate prints E11.
2. Append S030 as the last registry row, before `## Paths`, 11 cells, no pipes: `source` =
   `GitHub Docs — <page title> — https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills`
   (the first `https` URL is what `--fetch` opens); `kind docs`; `tier A`; `scope` names only this page's
   topic; `anchor` = section, lines, fetch date, yield; `teaches` = the conflict lever (`disabledSkills`
   or directory reorganisation); `status mined`; `opened 2026-10-22`; `recheck 90d`;
   `used-by corpus/knowledge/skill-overlap-levers-round51.md`.
3. On the six rows change **only** `used-by`, appending that path; leave `status`, `recheck`,
   `opened`, `scope`, `anchor`, `teaches` untouched. Need new row facts? A superseding row with the
   same URL, the same `scope` text, `teaches` opening `supersedes S0NN —`.
4. In the lesson § Gate: the S030 record row, the six old→new lines, and the D4 correction.
5. Re-run the § 5 command and diff: `exit 0` with the same three W04 lines. Any E code is a patch defect;
   a **fourth** W04 means a `scope` cell was re-worded on a re-used URL.
6. Commit, then `python3 -B verifiers/check_overlap_levers.py --rev <rev>`: every `S###` in `SKILL.md`
   and in the entry must be `mined` with `skill-overlap-levers-round51` in its `used-by` cell, and the
   entry quote must carry the key term verbatim; `--fetch` opens the first `https` URL in the row's
   `source` cell (citing S024 fetches `opencode.ai/docs/skills`). Add `corpus/lessons/round-51.md` to a
   `used-by` cell only after that file exists.

## 7. Confidence and remaining unknowns

- High (executed): every code and exit status above, the E11 same-round flip, invisibility of in-place
  `anchor`/`teaches` edits, W04 with and without `supersedes`. High (frozen text): rule-2 boundary, the
  status enum, `NF==13`, 0-3 space tolerance.
- Open: whether the L1 wants new `teaches` text on the six rows — the counter does not need it, and the
  supersede route holds W04 at three only if `scope` is copied verbatim. `verifiers/check_overlap_levers.py`
  did not exist when this seat ran, so its parsing is known from the build-spec text only.
- Not run: census `selftest`, `overdue`, the C2 counter, any fetch. No tool installs; writes confined to
  `/fast/scratch/hyaku/kotoba-r51/build/SourcesContract/` and this report.

## 8. Evidence: commands and exit codes

```
grep -c '^| S' corpus/SOURCES.md -> 29 ; grep -c 'S030' -> 0 (exit 1) ; grep -n '^## ' -> 10,44,62,113
git log -4 -- corpus/SOURCES.md corpus/knowledge/skill-selection-rules-round50.md -> exit 0 (a78fec1, bf109ca)
git show bf109ca -- corpus/SOURCES.md | grep '^[-+]| S0' -> exit 0 (in-place S019/S022/S026/S028 cells)
./scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba -> EXIT=0 (§ 5)
python3 mutant matrix over /fast/scratch/.../SourcesContract/mut -> exit codes as in § 2 (baseline exit 0,
  M9 in-place teaches edit exit 0, E01/E04/E07/E11/E12 mutants exit 1)
```
