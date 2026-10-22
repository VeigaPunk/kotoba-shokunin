# SrcCopilotSdk — round-51 build seat (C2 source: GitHub Copilot SDK skills page)

**Result (one line): HOLDS-BOUNDED — the Copilot SDK page documents removal levers that keep one of two
overlapping skills out of the model's choice (`disabledSkills`, `skillDirectories`, provider-level
`enableSkills: false`), it documents NO tie-break between two matching skills, and the round-50 reject reason
"provider catalogs, not SKILL.md routing" is inaccurate — D4 correction and a new SOURCES row drafted below.**

## Fetch record (ordinary means: `curl -sSL`; no browser, no bot challenge)

| file | URL | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| skills.md | https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills**`.md`** | 2026-10-22T14:19:11Z | 200 (`text/markdown`) | 35,455 | `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3` |
| skills.html | https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills (no suffix) | 2026-10-22T14:20:57Z | 200 (`text/html`) | 875,354 | `29dab37a496fd903a4e87f7650eb3a370f1033b990b61e2ee1a5d6868ce01830` |
| src.md | https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-sdk/features/skills.md | 2026-10-22T14:21Z | 200 | 32,294 | `396b985044328e253be90476ff9bcee837b5d7c265742629b59d8c7a1e3cd375` |

**Variant used: the `.md` route** (the site serves markdown at the `.md` suffix; it is the text of record —
815 lines). The `.md` bytes are **byte-identical to the round-50 seat's fetch** (sha256 `64856ff4…`,
2026-10-22T12:31:51Z, seat `.ufo/waves/round-50/build/SrcCopilotSkills.md`), so the round-50 line numbers
still hold. The authored `github/docs` source is the same prose without the rendered code-tab wrappers
(809 lines; `disabledSkills` at `:191,286,691,802`); the served `.md` numbers are the ones cited below.
Local copies: `/fast/scratch/hyaku/kotoba-r51/build/SrcCopilotSdk/`.

**Existing registry row: none.** `grep -c "copilot-sdk" corpus/SOURCES.md` → `0` (exit 1). The round-50
lesson rejected the page (`corpus/lessons/round-50.md` § Gate, "Three drafted rows not written") with the
reason "provider catalogs, not SKILL.md routing"; routed defect **D4** is
`corpus/lessons/round-50-verifier-spotcheck.md:189-192` and `:260-262`.

## The levers this client documents (other than description wording)

| key term (code token) | what it does, per the page | where it is set | verbatim quote (≤25 words) + location |
|---|---|---|---|
| `disabledSkills` (Node.js; `disabled_skills` Python; `DisabledSkills` Go/.NET) | **disables entirely** for the session: the skill is excluded, so the model is never offered it; § Skill conflicts names it *the* remedy when skills conflict | session-creation config in the SDK call — **not** a settings file | "Use `disabledSkills` to exclude conflicting skills" (`skills.md:809`) |
| `skillDirectories` | **scopes by path**: only these parent directories are scanned, so a skill outside them is never loaded | session-creation config in the SDK call | "The `skillDirectories` option points to the parent directory (e.g., `./skills`). The CLI discovers all `SKILL.md` files in immediate subdirectories." (`skills.md:262`) |
| `disable-model-invocation` (frontmatter key; catalog field `disableModelInvocation`) | **user-only invocation** in intent — the field marks the skill as not model-invocable; the page names the key and the catalog field but **states the effect only by the field name** ([INFERENCE] for the effect) | `SKILL.md` YAML frontmatter — documented for **provider-served** SKILL.md files (`:648`) and as catalog metadata (`:302`); the disk-loaded SKILL.md format section names only `name` and `description` (`:286-291`), so the page does not document it for disk-loaded skills | "Map `user-invocable`, `disable-model-invocation`, and `argument-hint` to the matching optional fields when the frontmatter sets them." (`skills.md:648`) |
| `enableSkills` | **disables entirely** a whole provider: set to `false` the provider stays bound but is never called, so none of its skills are offered | session-creation config | "A provider enables skills unless you set `enableSkills` to `false`, which keeps the provider bound but never called." (`skills.md:683`) |
| `includedBuiltinSkills` | **scopes by allowlist**: under `mode: "empty"` the SDK excludes every runtime-bundled built-in skill by default; this field re-admits named ones | session options (`mode: "empty"`, `:711-724`) | "To allow selected runtime-bundled skills, set `includedBuiltinSkills` (or the language-specific casing) to their names." (`skills.md:720-722`) |

Not a lever, but the one replacement rule the page states (name-keyed, not description-keyed): "A provider
skill with the same name as a file-based skill replaces the file-based skill, and `skills.reload` reports a
warning." (`skills.md:685`, § Provider lifecycle). It decides between two copies of one **name**; it says
nothing about two differently named skills whose descriptions both match.

## Does the page say anything about choosing BETWEEN two matching skills? — No.

The requested sweep `grep -niE 'overlap|conflict|precedence|disable|deny|permission|hidden|invocation'`
returns **51 lines** on the fetched bytes; every one is catalogued in
`/fast/scratch/hyaku/kotoba-r51/build/SrcCopilotSdk/sweep_requested.txt`. Counts per term: `overlap` 1
(`:810`), `conflict` 3 (`:805,807,809` — the heading and its two remedies), `precedence` 0, `deny` 0,
`permission` 27 (all `onPermissionRequest` / `PermissionHandler` code for tool approvals, `:37,163,242,…`),
`hidden` 1 (`:639`, about build folders in a related-files list), `invocation` 4 (`:302,648,653,687`).
A second sweep for choice words: `tie[- ]?break` 0, `ambigu` 0, `prioriti` 0, `specifici` 0, `choose` 0,
`trigger` 0, `which skill` 0, `matching skills` 0, `both match` 0; `select` 3, all unrelated (`selectively`
at `:288`, C# `.Select(` at `:449`, "selected" at `:720`). So the only overlap prose is § Skill conflicts, and
it prescribes **removal, not arbitration** — triggered by "conflicting instructions" (`:807`), never by two
descriptions that both match. The page does not even state how the model chooses among catalog entries
(GitHub's *add-skills* how-to, row S027, states that; this page does not).

**Bound, as the assignment requires:** a disable/deny lever removes a skill from the choice; it is not a
documented tie-break. This page documents **no** tie-break, so it cannot be cited as one — `disabledSkills` is
a removal lever and nothing more. The round-50 entry's finding 4 ("the documented remedy for overlap is
specificity in the description") therefore does not hold for this client, and `SKILL.md:375-377` (D3) must be
rewritten under C2.

## Best lever for the table: `disabledSkills`

It is the only lever the page states **as the remedy for conflicting skills** (`:809`), it applies to
file-based `SKILL.md` skills (not only provider catalogs), and its key term is a single backticked token
that occurs verbatim in the quote.

(a) **SKILL.md § Anti-patterns, "Overlap levers by client" table row** (columns `| client | lever | row | key term |`):

```
| GitHub Copilot SDK | Disable the conflicting skill for the session so the model is never offered it | S030 | `disabledSkills` |
```

(b) **Entry table row** for `corpus/knowledge/skill-overlap-levers-round51.md` (columns
`| client | row | lever | quote |`; the quote cell starts with a double-quoted string then a location):

```
| GitHub Copilot SDK | S030 | Disable a conflicting skill by name in the session config, so it is never offered | "Use `disabledSkills` to exclude conflicting skills" (skills.md:809) |
```

(c) **Registry cell change: none — there is no existing row.** Full new row in the registry's column shape
(`| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`),
**S030** = the next free id after the registry's last row (S029); the L1 assigns the final id at integration:

```
| S030 | GitHub Docs — Custom skills (GitHub Copilot SDK) — https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills | docs | A | What the GitHub Copilot SDK documents as levers, other than description wording, for keeping one of two overlapping skills from being chosen or loaded (vendor documentation for GitHub Copilot, not a measurement of omp or opencode) | § SKILL.md format (`skills.md:11,252,262,286-291`); § Disabling skills (`:177-179`); § Configuration options → § SessionConfig skill fields (`:697,700,703,706`); § Troubleshooting → § Skill conflicts (`:805-810`); § Built-in skills and `mode: "empty"` (`:711-724`); § Provider lifecycle (`:683-685`); § Serving existing SKILL.md files (`:648`); fetched as .../copilot-sdk/features/skills.md (200, 35,455 B, sha256 `64856ff4…`) on 2026-10-22T14:19:11Z | The documented remedy for conflicting skills is to remove one, not to reword it: "Use `disabledSkills` to exclude conflicting skills" (`:809`) and "Reorganize skill directories to avoid overlaps" (`:810`); `skillDirectories` scopes which directories are scanned (`:262`); the page states no rule for choosing between two differently named skills whose descriptions both match, and the one replacement rule it does state is keyed on the name (`:685`) | mined | 2026-10-22 | 90d | corpus/knowledge/skill-overlap-levers-round51.md, corpus/lessons/round-51.md |
```

Census check of this row, run in my private clone (`/fast/scratch/hyaku/kotoba-r51/build/SrcCopilotSdk/lane`),
not in the lane: `scripts/sources-census.sh validate --file corpus/SOURCES.md --today 2026-10-22` → exit 0 with
the three pre-existing W04 warnings only (S018, S019, S021) — **provided** `corpus/knowledge/skill-overlap-levers-round51.md`
and `corpus/lessons/round-51.md` exist on disk; with them absent the same command prints two `E11` rows for
S030 and exits 1. Integration note for the L1: create both files before the census runs.

## D4: appended correction paragraph for `corpus/lessons/round-50.md` § Gate (draft, not written)

> **Erratum (round 51, routed defect D4): the reject reason for the Copilot SDK skills page.** The round-50
> gate rejected that page's row with the reason "provider catalogs, not SKILL.md routing" (§ Gate, "Three
> drafted rows not written"). The reason is inaccurate, and the page is now written as `corpus/SOURCES.md`
> row **S030**. The page documents file-based `SKILL.md` skills, not only provider catalogs: "A skill is a
> named directory containing a `SKILL.md` file" (`skills.md:11`); "The `skillDirectories` option points to
> the parent directory (e.g., `./skills`). The CLI discovers all `SKILL.md` files in immediate subdirectories."
> (`skills.md:262`); the frontmatter fields it names are `name` and `description` (`skills.md:286-291`).
> Its § Skill conflicts section gives the remedy for overlapping skills, and that remedy is neither a
> tie-break nor a description rule: "Use `disabledSkills` to exclude conflicting skills" (`skills.md:809`);
> "Reorganize skill directories to avoid overlaps" (`skills.md:810`). Both remove one of two overlapping
> skills from the session's choice. The page states **no** rule for choosing between two differently named
> skills whose descriptions both match (sweep on the fetched bytes: `precedence` 0, `deny` 0, `ambigu` 0,
> `tie[- ]?break` 0, `choose` 0, `both match` 0; the three `select` hits are `selectively` at `:288`, C#
> `.Select(` at `:449`, "selected" at `:720`); the one replacement rule it does state is keyed on the name —
> "A provider skill with the same name as a file-based skill replaces the file-based skill" (`skills.md:685`).
> Page re-opened 2026-10-22T14:19:11Z by seat `.ufo/waves/round-51/build/SrcCopilotSdk.md`:
> `curl -sSL https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md` → 200, 35,455 B,
> sha256 `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3`, byte-identical to the round-50
> fetch. The round-50 entry's finding 4 ("the documented remedy for overlap is specificity in the
> description") therefore does not hold for this client: it is one remedy among several, and `SKILL.md:375-377`
> is rewritten under C2.

## Evidence (commands, exit codes, all run 2026-10-22 UTC)

- `curl -sSL -o skills.md -w '%{http_code} %{size_download} %{content_type} %{url_effective}' <...>/skills.md` → exit 0, `200 35455 text/markdown; charset=utf-8`; `sha256sum` → `64856ff4…`; `wc -c` → 35455; `wc -l` → 815.
- `curl -sSL -o skills.html ...` → exit 0, `200 875354 text/html`; `sha256sum` → `29dab37a4…`.
- `curl -sSL -o src.md https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-sdk/features/skills.md` → exit 0, `200 32294`; `sha256sum` → `396b9850…`.
- `grep -niE 'overlap|conflict|precedence|disable|deny|permission|hidden|invocation' skills.md` → 51 lines (saved to `sweep_requested.txt`).
- Per-term counts (each `grep -ciE`, exit 0): `overlap` 1, `conflict` 3, `precedence` 0, `disable` 19, `deny` 0, `permission` 27, `hidden` 1, `invocation` 4.
- Choice-word sweep (each `grep -ciE`, exit 0): `tie[- ]?break` 0, `ambigu` 0, `prioriti` 0, `most specific` 0, `specifici` 0, `choose` 0, `which skill` 0, `matching skills` 0, `both match` 0, `trigger` 0, `applies to` 0, `select` 3.
- `grep -c "copilot-sdk" corpus/SOURCES.md` → `0`, exit 1 (no existing row).
- `scripts/sources-census.sh validate --file corpus/SOURCES.md --today 2026-10-22` in the clone: baseline → exit 0 (3 W04); with S030 inserted and the two used-by files present → exit 0 (same 3 W04); with them absent → exit 1 (2 × E11 for S030).
- Verifier-shape simulation (substring checks on the drafted rows): key term cell `` `disabledSkills` `` occurs in the quote with backticks (True) and bare (True); contains "description" (False); quote occurs in the normalised `.md` bytes (True) and in the HTML route once tags are stripped (True). `KotobaR51.LeverGuard` (author of `verifiers/check_overlap_levers.py`) re-ran his script against my three rows and reported them **BACKED**, with a normaliser that folds whitespace and markdown emphasis on both sides and strips HTML tags.

## Bounds, tooling, out of scope

- Lane mutation: **none**. Nothing under `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was edited except this
  report file; no git write command ran in the lane, the fleet repo or any sibling lane; no `jj` command ran.
  The clone at `/fast/scratch/hyaku/kotoba-r51/build/SrcCopilotSdk/lane` is private (git clone of the lane at
  `43ca0bfb`) and is where the census check ran.
- Tooling: **no install or upgrade was needed** — `curl`, `grep`, `sha256sum`, `wc`, `python3` are already on
  this host, so no pacman/uv/npm channel was used (the pacman guard is moot for this seat).
- Not this seat: writing `corpus/SOURCES.md`, `corpus/lessons/round-50.md`, `SKILL.md` § Anti-patterns, or
  `corpus/knowledge/skill-overlap-levers-round51.md` — the drafts above are for the L1 to integrate. A
  convenience diff carrying only the SOURCES.md row is at
  `/fast/scratch/hyaku/kotoba-r51/build/SrcCopilotSdk/patch.diff` (partial by design: no lesson paragraph,
  no SKILL.md table).
- Not claimed: that `disabledSkills` removes the entry from the session's skill *catalog* (the page says
  "Skills to disable", `:697`, and "exclude conflicting skills", `:809`, and does not describe the catalog's
  contents); that `disable-model-invocation` is honoured for disk-loaded skills (documented for
  provider-served SKILL.md files only, `:648`); that any of these levers is a tie-break (none is).
