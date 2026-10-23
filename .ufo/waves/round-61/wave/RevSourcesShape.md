# RevSourcesShape — S112–S117 row-shape audit vs SOURCES contract v1

Round 61 attempt 1, wave seat `RevSourcesShape` (reviewer, depth). 2026-10-23.
Scope: planned row shapes S112–S117 against contract v1 (`/home/vgpnk/Projects/shokunin/CORPUS.md` § SOURCES.md; frozen copy `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`): 11 columns (NF=13), no `|` in cells, id sequence after S111, teaches-cell rules, status enum, duplicate-url census consequence, plus the CORPUS.md § Census awk/grep blocks run against a copy with the rows appended. Read-only lane/fleet honored; all test copies live under `/fast/scratch/hyaku/kotoba-r61/RevSourcesShape/` (untrusted scratch).

**Auditee availability.** At audit time only one row text exists: ScribeC3's committed draft of S117 (`.ufo/waves/round-61/wave/ScribeC3.md`). ScribeS112–S115 have fetched page bytes in scratch but no drafted row text; their "planned shape" is the wave-spec directive (`.ufo/waves/round-61/wave-spec.json` items ScribeS112–S115, ScribeC3). I therefore (a) audited the frozen directives, (b) audited the concrete S117 draft cell-by-cell, and (c) shape-tested representative rows built strictly to the directives. Findings against directives are marked **[plan-text]**; findings against written text are marked **[draft]**.

---

## Findings, by severity

### F1 — HIGH [plan-text]: two `re-opens` directives name a base row whose URL is NOT byte-identical to the row being opened

Frozen arm **A3** (plan `plans/round-61.md` §C1): *"a re-open row's URL must be byte-identical to its base row's URL."* Two directives name the wrong base:

- **ScribeS113** is told `teaches 're-opens S047 …'`. S047's URL is `https://code.visualstudio.com/docs/copilot/customization/custom-instructions`; the successor page actually used in round 60 is S105's `https://code.visualstudio.com/docs/agent-customization/custom-instructions.md` (S105 source cell, `corpus/SOURCES.md:117`). If the scribe opens the successor page (as the directive's parenthetical intends) and declares `re-opens S047`, either (a) v3's A3 compares URL bytes against S047 and rejects the landed row — a kill-rule failure (`any world exits 0` is not the trigger; an *eligible-row pass* failure is: the row is expected to land and pass live), or (b) A3 keys the base by normalized-URL match and finds S105, leaving `teaches` asserting lineage to a row whose URL it does not share — corrupt re-open lineage, exactly the class A3 exists to police.
- **ScribeS115** is told `(S049/S108's page cursor.com/docs/rules …)` with no declared teaches wording. S049's URL is `https://cursor.com/docs/rules.md`; S108's is `https://cursor.com/docs/rules` (SOURCES.md:120). The fetchable URL is the non-`.md` form (`a '.md' URL 404s` per the same prompt). Only `re-opens S108` is byte-identical; `re-opens S049` would either fail A3 or be a false lineage claim.

Corollary for the ledger: under the validator's `url_of` normalization (scheme stripped, one trailing slash stripped, fragment stripped, **host-only** lowercased — `scripts/sources-census.sh:600-605`), `…/rules` and `…/rules.md` are *different* normalized URLs. That is why S108 (re-open of S049's `.md` URL) produced **no** W04 at r60, while S106/S110/S111 did. If S113 lands on S105's URL declaring `re-opens S047`, the re-open is also invisible to W04 (different URL cluster) — no census signal guards the mismatch. Required fixes: S113 teaches names **S105** (the byte-identical successor row; S047 may be named as the older ancestor in the same cell); S115 teaches names **S108**. The L1 must re-check ScribeS113's/ScribeS115's landed `teaches`/`source` cells against this, since the directive text is wrong.

### F2 — MEDIUM [shape rule, demonstrated]: a re-open row must not repeat a prior row's scope cell on the same normalized URL — E04 → validate exit 1

`scripts/sources-census.sh:644-649`: `E04` fires when a row's normalized-URL+scope pair was already claimed by a non-rejected row, **unless** the new row's `teaches` contains `supersedes S[0-9]{3}`. The wave-spec teaches wording (`re-opens S…`) does not exempt. Demonstrated on copy B (S112 carrying S103's scope verbatim, teaches `re-opens S043/S103`):

```
file	E04	S112 duplicate url code.claude.com/docs/en/memory.md within scope Claude Code project rule files in `.claude/rules/` and frontmatter `paths` for matching-file scope (vendor documentation; not a runtime test)
validate exit = 1
```

The same row with teaches `supersedes S103 — canonical scope-key set` produced **zero** W04/E04, exit 0 (copy C) — the exemption both avoids E04 and suppresses W04 because the same-scope pair is exempted before the W04 "across scopes" check can attach. Consequence for the four C1 rows: each must carry a **genuinely different scope cell** from every earlier row on the same URL (S112 ≠ S043 and S103; S113 ≠ S047 and S105; S114 ≠ S048 and S106; S115 ≠ S049 and S108), or declare `supersedes`. The plan's canonical-scope-key wording is naturally a new scope, so spec-following scribes stay clean — but the checker compares raw trimmed scope text case-sensitively; a case-only tweak "differs" mechanically while staying dishonest. Integration pre-flight: run `validate` on the integrated file; any E04 is a hard fail of the round's exit-0 requirement.

### F3 — MEDIUM [plan-text]: S116 is unassigned; Gate-coverage text claims six rows

Row-bearing wave items are exactly ScribeS112/S113/S114/S115 (C1) and ScribeC3 (S117). `grep -c S116` over `plans/round-61.md` and `wave-dispatch.json` → 0; no wave-spec item names S116. Yet the ScribeLesson prompt says the lesson's `## Gate` records *"every new row S112-S117"*. Options: assign a row to S116 (any late addition takes it, per `id = next unused`), or fix the enumeration strings to "S112–S115 and S117" in the lesson Gate, report, and census commentary. Leaving an unexplained gap while the Gate text enumerates S112–S117 is the same sloppy-record class this round's C2 repairs exist to fix. Note: a bare id gap is not itself a contract violation — the registry already skips S092 (110 rows, S001–S111; `sort -u` gap check below). The defect is only the mismatch between text and landed ids.

### F4 — LOW [draft]: S117 `queued` + non-`—` used-by is unprecedented and sits against the status semantics

ScribeC3's draft (verbatim): `… | queued | 2026-10-23 | 180d | corpus/knowledge/writing-revision-calibration-round61.md |`. Contract status semantics: `mined` = "cited by ≥1 path in `used-by`"; `queued` = "opened, worth mining". All 7 committed `queued` rows have `used-by = —` (awk census below: `total queued: 7`, zero queued-with-used-by). Every row that landed with its citing entry in the same round landed `mined` (S104–S111 all `mined`). Since the citing entry `corpus/knowledge/writing-revision-calibration-round61.md` lands in the same integration commit, the honest status is `mined`. `queued`+used-by is legal to every machine check (E11 only inspects `mined` rows, W03 only `mined`), so nothing alarms — precisely why a reviewer should say it. Either land `mined` or land `queued` with `used-by = —` and log the status flip old→new when the entry cites it (contract rule 2 logging discipline). RevKamaRow may adjust teaches content independently; this finding is about status only.

### F5 — LOW [draft]: S117 anchor carries no revision

Contract: anchor = "exact section / heading / page / line **plus revision** (version, commit, or publication date)". Draft anchor: `the entry head, "Checking self-assessment statements at writing"` — a location, no revision. The kama file's head carries `verified-at: 2026-10-23` (`kama-shokunin/corpus/knowledge/self-assessment-at-writing.md:2`); r60 rows cite `fetched <ISO ts> (HTTP 200, N B, sha256 …)` inside anchor cells. Cheapest honest fix keeping ScribeC3's wording: `the entry head, "Checking self-assessment statements at writing" (`:5`); opened 2026-10-23, verified-at 2026-10-23 per entry head`. (A sha256 of the sibling file would be stronger still but is a judgment call — the lane does not hash sibling artifacts elsewhere.)

---

## Checklist vs contract v1 (audited items)

| Rule | Result | Evidence |
|---|---|---|
| 11 columns → NF=13 | PASS for S117 draft verbatim and spec-shaped S112–S115 | frozen malformed-block prints `0` on copy A (below) |
| no `|` inside cells | PASS | same block (any embedded `|` would shift NF off 13) |
| id = next unused after S111 | PASS for S112–S115, S117; S116 unassigned → F3 | base max id S111 (`sort -u` check); pre-existing S092 gap |
| kind enum | PASS (`docs` ×4, `own-work` ×1) | enum block empty |
| tier enum + community≠A | PASS (A×4, B×1) | enum block empty |
| teaches cell | directive wording `re-opens S0NN — canonical scope-key set` is the S108 precedent and satisfies "one grounded learner benefit"; **two directives name a non-byte-identical base → F1**; any *corrective* row must instead open `supersedes S0NN —` (contract rule 2), which also changes census outcome → F2 |
| status enum | all cells in {queued, mined, rejected}; S117's `queued`+used-by semantic issue → F4 |
| opened / recheck | `2026-10-23` ≤ today passes E08; `90d`/`180d` pass E09 | validator exits |
| used-by | `queued` S117 exempt from E11 by rule; if S112–S115 land `mined` (S108 precedent), their used-by files must exist in the same commit or E11 fires → integration-order requirement |
| placement | rows must be appended inside `## Registry` before `## Paths` (E12 guard confirmed live in script) | my copies appended there; 0 E12 |
| credential/private material | none in any draft shape | rule 6 |

## Duplicate-url census consequence (the asked question)

Validator semantics (read: `scripts/sources-census.sh:600-605,643-654`): `url_of` strips scheme, one trailing `/`, `#fragment`, and lowercases the host **only**. Path case, `.md` suffix, and query strings survive — `page` vs `page.md` vs `page?v=1` are three distinct normalized URLs.

- **W04** (`same URL across scopes`, warning-only, never fails): fires when a row's normalized URL was seen under a *different* scope. Committed baseline = 13 W04, all from earlier re-opens; S110 (`code.claude.com/docs/en/hooks.md` vs S096) and S111 (`learn.chatgpt.com/docs/hooks.md` vs S097) each added exactly one W04 by writing a **differing scope** cell — the committed pattern, and `.ufo/waves/round-61/census-before.txt` records the 13-line baseline ending `ok`/`exit=0`.
- **Expected after S112–S117 as directed:** +4 W04 (S112, S113, S114, S115 — each re-opens a URL under a new scope), **17 total, still exit 0**. S117 contributes none: its `../kama-shokunin/…` path yields no URL. This is the bounded delta the plan's "(exit 0, 13 W04)" must be updated to expect; if any scribe finds an *unopened* canonical URL (permitted alternative for S113), that row adds zero.
- **E04 trap:** same URL + *same* scope + teaches lacking `supersedes S\d{3}` → error, validate exit 1 (demonstrated, F2). Same URL + same scope + `supersedes S0NN` → clean, and no W04 either.

## Measurements (commands, output, `date -u`, exit)

Setup: `/fast/scratch/hyaku/kotoba-r61/RevSourcesShape/lane-copy/` = full `corpus/` + `SKILL.md` copy; five rows (spec-shaped S112–S115 + ScribeC3's verbatim S117) appended before `## Paths`; stub files created for the two new used-by paths (`scoped-rules-counter-round61.md`, `writing-revision-calibration-round61.md`, `lessons/round-61.md`) to model post-integration existence for E11. Variants `lane-copy-e04` (S112 with S103's scope verbatim) and `lane-copy-sup` (same scope, teaches `supersedes S103 —`).

### Frozen CORPUS.md § Census blocks on copy A (verbatim commands)

```
### date -u: 2026-10-23T19:16:29Z
### rows
115
### malformed (must be 0)
0
### tier
A=112 B=2 C=1
### status
mined=106 queued=8 rejected=1
### dup ids (must be empty)
(empty)
### enum/tier-inflation (must be empty)
(empty)
### mined used-by missing (must be empty)
(empty)
```

(Base file for reference: `rows` → 110; the +5 = S112,S113,S114,S115,S117. `queued` 7→8 is S117; `mined` 102→106 is S112–S115 modeled `mined` per S108 precedent.)

### Maintained validator, `sources-census.sh validate --file` — exits measured 2026-10-23T19:15Z

| file | W04 | E-lines | exit |
|---|---|---|---|
| real tip `corpus/SOURCES.md` (baseline) | 13 | 0 | 0 |
| copy A (S112–S115 + S117, distinct scopes) | 17 | 0 | **0** |
| copy B (S112 repeats S103's scope, `re-opens`) | 13 | 1 (E04 S112) | **1** |
| copy C (same repeat scope, `supersedes S103`) | 13 | 0 | **0** |

Copy-A W04 delta lines (all four new):

```
file	W04	S112 duplicate url code.claude.com/docs/en/memory.md across scopes
file	W04	S113 duplicate url code.visualstudio.com/docs/agent-customization/custom-instructions.md across scopes
file	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S115 duplicate url cursor.com/docs/rules across scopes
file	ok	…/lane-copy/corpus/SOURCES.md
```

E04 demonstration line (copy B): pasted under F2 above.

### Id sequence proof

```
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md → 110
sorted unique ids: count 110, min 1, max 111, gaps in 1..111: [92]
date -u: 2026-10-23T19:16:22Z
```

### Queued-with-used-by precedent check

```
awk … (status=queued && used-by≠"—") print; END print total →
total queued: 7            (no queued-with-used-by lines printed — zero precedent)
```

## Representative rows used in copy A (seat-built to the wave-spec shape; NOT scribe drafts)

```markdown
| S112 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Claude Code `.claude/rules/` frontmatter `paths` as the canonical scoped-rule key (vendor documentation; not a runtime test) | § Path-specific rules (`memory.md:194-200`); rule frontmatter (`:246-250`); fetched 2026-10-23 (HTTP 200) | re-opens S043/S103 — canonical scope-key set | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-counter-round61.md, corpus/lessons/round-61.md |
| S113 | Visual Studio Code — Use custom instructions in VS Code — https://code.visualstudio.com/docs/agent-customization/custom-instructions.md | docs | A | VS Code `.github/instructions/*.instructions.md` frontmatter `applyTo` as the canonical scoped-rule key (vendor documentation; not a runtime test) | `applyTo` field (`custom-instructions.md:150-158`) and example (`:160-164`); fetched 2026-10-23 (HTTP 200) | re-opens S047 — canonical scope-key set | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-counter-round61.md, corpus/lessons/round-61.md |
| S114 | GitHub Docs — Adding custom instructions for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | Copilot CLI `.github/instructions/*.instructions.md` frontmatter `applyTo` as the canonical scoped-rule key (vendor documentation; not a runtime test) | § Creating path-specific custom instructions (`:52-60`); frontmatter example (`:64-68`); fetched 2026-10-23 (HTTP 200) | re-opens S048 — canonical scope-key set | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-counter-round61.md, corpus/lessons/round-61.md |
| S115 | Cursor Docs — Rules — https://cursor.com/docs/rules | docs | A | Cursor `.cursor/rules` frontmatter `globs` as the canonical scoped-rule key (vendor documentation; not a runtime test) | § Glob pattern examples (`rules.md:130-131`); fetched 2026-10-23 (HTTP 200) | re-opens S108 — canonical scope-key set | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-counter-round61.md, corpus/lessons/round-61.md |
| S117 | kama-shokunin — `../kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` | own-work | B | writing-revision calibration for prompt-craft self-assessment | the entry head, "Checking self-assessment statements at writing" | Checking a self-assessment against its writing revision can distinguish a calibration error present then from later drift | queued | 2026-10-23 | 180d | corpus/knowledge/writing-revision-calibration-round61.md |
```

(S113's teaches deliberately reproduces the wave-spec's `re-opens S047` wording — this is the F1 defect under audit; the corrected cell reads `re-opens S105 — canonical scope-key set`. S115's `re-opens S108` is my correction to the prompt's bare `(S049/S108's page …)`; it is the only byte-identical base.)

## Residual risk and verification gaps

- **S112–S115 literal drafts do not exist yet.** My copy-A run proves the *shape space* is safe (+4 W04, exit 0) but not the landed text; the L1 should re-run `sources-census.sh validate` on the integrated file before `census-after.txt` is written. Any scope cell copied verbatim from a base row converts to E04 (F2).
- **F1 severity depends on how v3 keys the A3 base row** (declared `re-opens`/`supersedes` token vs normalized-URL lookup). Either way the directive names a wrong base — the fix (S105, S108) is correct under both designs; ExecCounterV3/ExecSelftestArms should state which keying v3 uses.
- **Unopened-URL alternative for S113** is allowed by the directive; if exercised, `teaches` should read as a fresh open (not `re-opens S047`), and the W04 delta drops by one — record which branch landed in the Gate.
- `opened = 2026-10-23` passes E08 today; a row landed after UTC midnight with an unchanged `opened` stays legal (past/present), but an `opened` of a *future* date would E04-style fail as E08 — none in play.
- Query-string aliases are normalized-URL-distinct (F2 mechanism) — a same-page URL with tracking params would evade both W04 and E04; byte-identity is A3's job, not the census's.
- The manual `mined used-by` block and E11 both assume used-by files exist at census time: **landing order** — rows with `mined` must commit together with or after `scoped-rules-counter-round61.md`, `lessons/round-61.md`, `writing-revision-calibration-round61.md`, or the census exits 1.
- Verified against the *committed* v2-era validator and frozen contract; if the L1 lands a validator change this round, these W04/E04 semantics should be re-confirmed against the landed script.

Installs: no installs (bash/gawk/python3/coreutils only; pacman untouched per the pause).
Blockers: none.
Produced: audit of planned S112–S117 row shapes vs contract v1 — 5 findings (1 HIGH: S113/S115 teaches name non-byte-identical base rows, fix S105/S108; 1 MEDIUM: E04 same-scope re-open trap demonstrated, exit 1; 1 MEDIUM: S116 unassigned vs "S112–S117" Gate text; 2 LOW: S117 queued+used-by precedent, S117 anchor revision) — plus measured census deltas (+4 W04 → 17 total, exit 0) on a spec-shaped copy and the E04/supersedes control runs.
