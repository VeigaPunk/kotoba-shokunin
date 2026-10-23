# Round 61 — ExecWorldFixtures

**Seat:** `kotoba-r61-wave-ExecWorldFixtures` (executor, leaf).
**Date -u run start:** `2026-10-23`.
**Lane (read-only):** `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at base `f3246d1493b60ea1c0d947a19c39f9e08e92f326`.
**Counter working copy (committed, read via import for verification only):**
`verifiers/check_scoped_rules.py` sha256 `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a` (counter v2).

## Task

Reconstruct the seven frozen worlds W1–W7 from the r60 receipts as committable
fixture definitions, plus W0 do-nothing. For every world: exact fixture layout
(file tree), exact row text (SOURCES rows, SKILL cells, lesson Gate lines,
snapshot bytes identified by source path+sha256), expected v3 reject reason
(arm + printed line), r60 ground citation. For W1 also identify the round-53
scratch bytes CtlReopenForged used and verify sha256. W5/W6 were rebuilt
end-to-end from ExecKeyForms with exact key-site lines. W7 = best v1-hollow
rescore world (found F=1).

## Method / verification evidence

Commands below ran from scratch `/fast/scratch/hyaku/kotoba-r61/ExecWorldFixtures`
(`date -u` = `Fri 23 Oct 2026 19:16:13Z` during fetch verification), the lane was
read-only; copies of the committed counter were imported for judging.

1. r53 bytes reuse:
   - `/fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md` sha256
     `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff` (51,971 B),
     named in `.ufo/waves/round-53/build/ScribeClaudeCode.md:13` (`sha256 971d75bf…`,
     51,971 B, fetched 2026-10-22T20:04:43Z).
   - `/fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/copilot-cli-custom-instructions.md`
     sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` (8,730 B).
   - `/fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.4524a03e99d4`
     sha256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` (17,403 B).
   The two latter byte-identical to committed snapshot S106.page/S108.page.

2. Alias fetch for W2:
   - `/fast/scratch/hyaku/kotoba-r60/CtlReopenHeldKey/probe/fetches/alias/1792757481166658578-1469463.page`
     sha256 `c568aae2c633029aa6a8b612de437f275bbe8f39c5866ef7382f89073e7f9c43` (63,447 B) German alias.
   - same dir `1792757481335959824-1472269.page` sha256 `70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e` (8,826 B) enterprise alias; both quoted verbatim.

3. World tables were each evaluated with the committed v2 counter's `judge()` offline
   (read-only import). Summaries:
   - W1:` Claude/Copilot/Cursor all BACKED (v2). Matches r60 record (S3/3 F3/3 exit 0).
   - W2: all BACKED (v2); matches r60 record S3/3.
   - W3: Cursor rejected already under v2 via held-base key (line `base row S049 already
     records key rules`); the other two back.
   - W4: Cursor accepted offline under v2 (v2 only killed redirect at --fetch time).
   - W5: `patterns`@238 scope key backs under v2 (ExecKeyForms hole confirmation).
   - W6: invented cell at :209 backs under v2.
   - W7: reconstructed CtlFabSnapshot pristine world reproduces S1/F1, three rows reject
     by the base-URL conjunct.

4. Verification snippets (command/pinned output):

```text
$ sha256sum /fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md \
  /fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/copilot-cli-custom-instructions.md \
  /fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.4524a03e99d4

971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff  ...memory.md
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  ...copilot-cli-custom-instructions.md
884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  ...gate.4524a03e99d4
```

```text
$ python3 -B probe_v2_worlds.py | grep '^bytes'
bytes claude_r53   51971 971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff
bytes claude_fresh 54043 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7
bytes vscode       23715 a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f
bytes copilot       8730 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
bytes cursor       17403 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
bytes claude_de    63447 c568aae2c633029aa6a8b612de437f275bbe8f39c5866ef7382f89073e7f9c43
bytes copilot_ent   8826 70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e
exit 0
```

(The probe uses imports; output above is verbatim.)

Ma background claimed mesa of S*—S115 fetched (to check four-eligible-row A4(iv) unaffected):
- S114.page sha `00e45ea5…` and S115.page sha `884c67ca…` are **identical** to the r60
  S106.page/S108.page snapshot bytes. Flagged below as an L1-level risk for the measured
  table self-scan clause (E2c condition 4).

---

## World catalog (File tree + source)

Each world is a directory under `verifiers/fixtures/scoped-rules/`; files that
must go in each commit are given per world (2-commit for W1, 1-commit for rest).

Shared manifest schema (each dir `manifest.json`):

```json
{
  "schema": "kotoba-scoped-rules-fixture-v1",
  "world": "W1",
  "r60_citation": "path:line",
  "expected_reject": {"client": "Claude Code", "arm": "A4", "line": "..."},
  "commits": [{"msg": "...", "files": ["corpus/SOURCES.md", ...], "author_date": "..."}],
  "snapshots": {"S116": {"bytes": 51971, "path": "/fast/scratch/.../memory.md", "sha256": "971d75bf..."}}
}
```

---

## W0 — do-nothing definition

Layout: `verifiers/fixtures/scoped-rules/W0/`.
Files: `SKILL.md` (header-only section, no rows), `corpus/SOURCES.md` could be the same
base-blank (empty world rows none); `entry.md` and `lesson.md` contain no rows; no
snapshots.
Expected v3 printed lines (same sentences as v2, copied from r60 freeze receipt
`freeze2-selftest.txt` + rediscovered control `controls/CtlDoNothing.md`):
```
scoped rule files backed on committed snapshots 0 of 0; live not run
reject <Client>: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```
for each of the 7 clients; exit code offline 1. With `--fetch`: line `found on the live
page 0 of 0` and exit 1. Citation: `.ufo/waves/round-60/controls/CtlDoNothing.md`.

---

## W1 — CtlReopenForged d (recycled round-53 bytes under fresh-fetch claim)

Layout (two commits, per E2c binding (2)/(3) and L1 steering):

```
verifiers/fixtures/scoped-rules/W1/
  commit-A/   (author date 2026-10-22T20:04:43Z)
    snapshots/S116.page     (r53 claude r bytes)  # blob-only; committed first
    corpus/SOURCES.md                       # BASE=31092dc6 table incl. S043 full sha
  commit-B/   (author date 2026-10-23T12:06:23Z)
    SKILL.md / entry.md / lesson.md / SOURCES.new.md / snapshots/S117.page, S118.page
```

Exact SOURCES rows for the world (`SOURCES.new.md` merged into commit-B `corpus/SOURCES.md`):

```
| S116 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Claude Code project rule files in `.claude/rules/` and frontmatter `paths` for matching-file scope (vendor documentation, not a runtime test) | § Organize rules with `.claude/rules/` (`memory.md:166,168`); § Path-specific rules (`:194-200`); fetched 2026-10-23T12:06:23Z, HTTP 200, 51,971 B, sha256 971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff | re-opens S043 — Claude Code documents `.claude/rules/` files and YAML frontmatter `paths` to scope rules to matching files | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md, corpus/lessons/round-60.md |
| S117 | GitHub Docs — Adding custom instructions for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | Copilot CLI repository-scoped modular instruction files and their path selector (vendor documentation, not a runtime test) | § Types of custom instructions table (`add-custom-instructions.md:13-22`); asked Creating path-specific custom instructions (`:52-60`); fetched 2026-10-23T12:06:23Z, HTTP 200, 8,730 B, sha256 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980 | re-opens S048 — Copilot CLI's repository modular instruction files use `.github/instructions/**/*.instructions.md` with an `applyTo` glob | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md, corpus/lessons/round-60.md |
| S118 | Cursor Docs — Rules — https://cursor.com/docs/rules | docs | A | Cursor project rule files under `.cursor/rules` and path-glob scoping of `.mdc` files | § Project rules (`rules.md:30-32`); example frontmatter (`rules.md:83-85`); fetched 2026-10-23T12:06:23Z, HTTP 200, 17,403 B, sha256 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8 | re-opens S049 — Cursor documents project rules in `.cursor/rules` as `.mdc` files; `globs` scopes a rule to specific files or directories | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md, corpus/lessons/round-60.md |
```

SKILL section (with exact cells):

```
### Scoped rule files by client
| Client | Rule files | Scope key | Action |
|---|---|---|---|
| Claude Code | `.claude/rules/` | `paths` (S116 :198) | Scope rules to specific files using YAML frontmatter and matching patterns (S116 :194) |
| Copilot CLI | `.github/instructions` | `applyTo` (S117 :66) | Create a frontmatter block containing `applyTo` and use glob syntax to specify files or directories (S117 :60) |
| Cursor | `.cursor/rules` | `globs` (S118 :85) | Use `globs` to scope a rule to specific files or directories; separate multiple patterns with commas (S118 :131) |
```

Session quotes (Gate + entry) as in r60 table (verbatim within the associated byte-fetch).

Expected v3 reject (arm A4): the world's S116 row carries a full sha `971d75bf…`
also recorded in base row S043; thus A4 conjunct (iv) rejects. Relevant printed line
(expected, must be pinned against integrated v3 text):
```
reject Claude Code: entry row S116: snapshot sha256 971d75bf… is already recorded in the base SOURCES table by row S043 (byte-identity alias; declare anchored `supersedes S043 —` if intended)
```
Also A4 (iii) consistency clause may fire given commit A is dated 2026-10-22 (< opened
2026-10-23); report triaged to the L1. Ground: `controls-v2/CtlReopenForged.md`
§variant-d + `controls-v2/SUMMARY.md` row `CtlReopenForged d MET`.

## W2 — CtlReopenHeldKey b (locale / enterprise alias renderings)

Rows are FRESH (no `re-opens` prefix) per E2b/MutFixtures seam S1. Source table:

```
| S116 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/de/memory.md | docs | A | … | fetched 2026-10-23T12:11:20Z, HTTP 200, 63,447 B, sha256 c568aae2c633029aa6a8b612de437f275bbe8f39c5866ef7382f89073e7f9c43 | Claude Code documents `.claude/rules/` files and YAML frontmatter `paths` … | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md, corpus/lessons/round-60.md |
| S117 | GitHub Docs — … — https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | … | fetched 2026-10-23T12:11:20Z, HTTP 200, 8,826 B, sha256 70aef6793ae9896ad98f12c75eb3d8c3cae504c6ea728c257b794d2f00c09e8e | Copilot CLI's … `.github/instructions/**/*.instructions.md` … | mined | 2026-10-23 | 90d | … |
| S118 | Cursor Docs — Rules — https://cursor.com/docs/rules | … | re-opens S049 — … | mined | 2026-10-23 | 90d | … |
```

SKILL identical to W1 except Scope keys cited with S116 :198 / S117 :66 / S118 :85; S116 quote and action are German (r60 receipt anchors `:18`, `:194`, `:198`).

Expected v3 reject (arm A3(b)) — printed lines:
```
reject Claude Code: entry row S116: S116 URL 'https://code.claude.com/docs/de/memory.md' is a locale rendering of a same-host row's URL (base row S043); A3(b) fresh-row alias
reject Copilot CLI: entry row S117: S117 URL 'https://docs.github.com/en/enterprise-cloud@latest/…' diverges from base row S048 by an @version/enterprise suffix; A3(b) fresh-row alias
reject opencode: …
```
Ground: `controls-v2/CtlReopenHeldKey.md` (alias section) + `controls-v2/SUMMARY.md`.

## W3 — CtlReopenHeldKey a (held key)

Structure: the pristine world rows S116-S118 with realctions capture S118 (Cursor) scope
key cell changed to `rules` cited `S118 :146`; snapshot S118 = cursor canonical bytes.

Expected v3 reject (arm A1 canonical-set AND retained held-key conjunct):
```
reject Cursor: entry row S118: scope key 'rules' is not in the canonical scope-key set for Cursor (globs); S118 URL 'https://cursor.com/docs/rules' is already a base SOURCES URL; base row S049 already records key rules
```
Citation: `controls-v2/CtlReopenHeldKey.md` / `controls-v2/SUMMARY.md` (row `held-key a`).

## W4 — CtlReopenHeldKey c (live redirect to a different base key)

S118 row URL `https://cursor.com/docs/context/rules`, teaches `re-opens S052 —`, redirect target host/key S049. A3(a) is expected to reject offline in v3 (url_key war swup). Printed:
```
reject Cursor: entry row S118: re-open names base S052 but request URL 'https://cursor.com/docs/context/rules' yields url_key not equal to S052's url_key; A3(a)
```
Citation: `controls-v2/CtlReopenHeldKey.md` (redirect section). Note: v2 only killed this with `--fetch`; report that v3 derives an offline kill via A3.

## W5 — wrong scope key (ExecKeyForms as-pattern / claudeMdExcludes)

Rebuild end-to-end (copy of ExecKeyForms W-wrong world): font fresh rows for Claude
Code, VS Code, Copilot CLI, Cursor but set S116 scope key `patterns` cited at `S116 :238`
(pass `claudeMdExcludes` cited at `S116 :339` as documented variant). All rows retain proper
snapshot bytes/shas, quotes, entries, Gate lines.
Exact key-site lines on committed S103.page:
- `:238` → `Each brace group multiplies the number of expanded patterns: `src/*.{ts,tsx}` expands to two patterns, and `{a,b}/{c,d}/*.{ts,tsx}` to eight. To keep expansion bounded, a rule's whole `paths` list shares one budget of 1,000 expanded patterns and 4 MiB, and patterns without braces don't count against it.`
- `:339` → `  "claudeMdExcludes": [` followed by `:340` `    "**/monorepo/CLAUDE.md",`

Expected v3 line: `reject Claude Code: SKILL.md scope key 'patterns' is not in Claude Code's canonical scope-key set {paths} (A1)`.
Ground: `build/ExecKeyForms.md` (Part 1b/2), r60 closure §8 wording.

## W6 — invented action (ExecKeyForms published cell)

Same 4-client world, Scope key remains `paths` (S116 :198); Action cell replaced by:

```
Create the rule file in the project and add frontmatter so it loads only for the matching files. (S116 :209)
```

Key-site/claim details (measured against S103.page): line 209 is “Rules without a `paths`
field are loaded unconditionally and apply to all files …”. Under guarded A2 the cell must
fail G7 claim-span (raw load/event claim can't be satisfied on one line).

Expected printed `reject Claude Code: SKILL.md action cell claim 'loads only for the matching files' is not supported by line 209 (A2)`.
Ground: `build/ExecKeyForms.md` Part 2 (table rows for Claude Code).

## W7 — best v1-hollow rescore world (found F=1)

Chosen: CtlFabSnapshot “genuine pristine baseline” `a2893fa2` (S 1 of 4 / F 1 of 4 /
exit 1), because among v1 control worlds re-scored under v2 its rescore returned the
max observed F=1 while retaining required bytes internally representable (re-using the
four census page snapshots). Its fixture mirrors `controls/CtlFabSnapshot.md`’s pristine
world (real census rows; four eligible rows S116/S117/S118/S119 with tokens paths/applyTo/
applyTo/globs; real page bytes, row URLs equal base-source, no re-opens).
Expected v3 printed reject list: base-URL conjunct forms same line as v2's:
```
reject Claude Code: entry row S116: S116 URL 'https://code.claude.com/docs/en/memory.md' is already a base SOURCES URL; re-open names no base row with this URL
reject Copilot CLI: entry row S118: … is already a base SOURCES URL; re-open names no base row with this URL
reject Cursor: entry row S119: … is already a base SOURCES URL; re-open names no base row with this URL
```
Bound caveat noted: rejection here relies on the retained base-URL conjunct and is a
regression, not A-arm specific. Citation: `controls/CtlFabSnapshot.md` and
`controls-v2/CtlRescoreV2.md` (rows `a2893fa2` / `b713e5b1`).

---

## Expected v3 line format note

The printed `reject <client>: …` strings above are derived (a) from the frozen arm spec
(N1–A4) and (b) from observed v2 lines under the same row bytes. They are expectations;
the exact spacing/identifier glyphs are owned by the v3 counter seat and must be pinned in
receipts once the counter lands. None of these strings have been emitted by any v3 binary
yet (v3 source not committed as of this writing) — I did not fabricate a run result.

## Risks / blockers to surface to L1

1. **Canonical-key SOURCES rows S112–S115 may share digest with r60 eligibility rows.**
   Measured here: S114.page == `00e45ea5…` (same as S106.page) and S115.page ==
   `884c67ca…` (same as S108.page). E2c condition (4) (“the scan covers the measured
   commit's table too, excluding self”) will then pit e.g. S106 vs S114 / S108 vs S115,
   producing a false A4(iv) rejection of the eligible rows when the fixture/lane table
   carries both. Requires an exclusion rule for canonical-key authoring rows (or using
   different source URLs/PIDs for canonical-key rows) before the 4-of-4 positive arm can
   pass.
2. **W1 two-commit shape.** Steering mandates A=2026-10-22 blob commit, B=2026-10-23
   rows. E2c clause (iii) becomes true ⇒ an offline reject might double-report with (iv);
   the printed line ordering is L1-integration concern.
3. **Snapshot source applicability.** Some W2 alias bytes are preserved only in
   round-60 scratch (german c568aae2…). There is no committed lane-bytes equivalent; the
   fixture manifest retains the scratch sha-path pair for L1 materialization, and captures
   that its current online re-fetch differs (64,758 B, sha c72a26dd…).
4. **W7 depends on old base-URL conjunct** rather than the A-arms; keep in plans to
   preserve “worlds reject 7 of 7” invariant.

## Installs/Recall

No tools installed or upgraded (operator rule considered; pacman paused, nothing missing).
Blockers: none beyond items 1–4 to integrate. Produced: fixture trees/tables for W0–W7 +
sha verification + v2 world-eval receipts + catalogue.
