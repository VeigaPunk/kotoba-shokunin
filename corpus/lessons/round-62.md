---
author: kotoba L1 round 62
date: 2026-10-23
round: 62
lane: kotoba
---

# Round 62 — lesson (kotoba, hyaku run 5, attempt 2)

## Gate

S118 was opened on 2026-10-23 by `SrcRulesFrontmatter`; its fetched page and lane snapshot are recorded below. The source-seat fetch command and output are in `.ufo/waves/round-62/w1/SrcRulesFrontmatter.md:11-25` (`date -u +%Y-%m-%dT%H:%M:%SZ`; the recorded `curl` command; HTTP status, size, and SHA-256). The quote locator is re-openable with `sed -n '250p' .ufo/waves/round-62/snapshots/S118.page`.

- **S118 Claude Code (re-opens S103)** — https://code.claude.com/docs/en/memory.md — accessed 2026-10-23T20:49:56Z (HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`; seat `SrcRulesFrontmatter`; snapshot `.ufo/waves/round-62/snapshots/S118.page`) — § Rule frontmatter reference, `memory.md:250`: “Glob patterns that scope the rule to matching files”. S118 is admitted, not rejected; no S118 reject/flip is recorded.
- Round-start census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` — exit 0 (`.ufo/waves/round-62/census-before.txt:3-20`).

Rejected (with reason), from `.ufo/waves/round-61/wave/ScoutKeyPagesA.md` § *Census rejections* and its probe records:

- S047's `https://code.visualstudio.com/docs/copilot/customization/custom-instructions.md` returned HTTP 404 with body `Not Found`; Cursor's `https://cursor.com/docs/rules.md` and `https://cursor.com/docs/reference/plugins.md` `.md` forms also returned HTTP 404, with response headed `# Page not found`. These are dead URLs, not usable sources (`ScoutKeyPagesA.md:143-152,162-169,220-225`).
- Cursor's `https://cursor.com/docs/context/rules` redirected to the base `https://cursor.com/docs/rules`; it is an alias, not a distinct source (`ScoutKeyPagesA.md:193,220-225`).
- Enumeration-only probes did not provide an `applyTo` frontmatter field table: the concepts page `…/prompting-and-context/custom-instructions.md`, sha256 `6e7964dc1951c64c1b740b70e0353e56de6ae100805347b99440f050416de933`; support matrix `…/reference/custom-instructions-support.md`, sha256 `90150f5a25f493640b9a52da6ac0a363ece8ece13429bd2c6c4e5ebb0c44e814`; customization cheat sheet `…/reference/customization-cheat-sheet.md`, sha256 `25f43326fb38833208df14cc9d9f6a72bf182f0785bf5b2a86748953a0fc3b25`; VS Code learn page `https://code.visualstudio.com/learn/customizations/2-instructions.md`, sha256 `2d842e6b67e5b82b36ec51542a1026b85cef16b0a79d0e9bea2de3444d6f22e7`. The first three mention custom instructions or path globs but do not enumerate the frontmatter field set; the last is an enumeration, not the required field table (`ScoutKeyPagesA.md:156`).

## Mistakes

- **M93 — class: erratum recorded as absorbed without an arm-level receipt** · Evidence: the landed `action_conjunct` has no E2f G7 event-claim or G9 compound-purpose conjunct; `content_words` strips backticked spans and the action check contains only support-fraction logic (`verifiers/check_scoped_rules.py:972-1040`). The r61 report says “five pre-data arm amendments each forced by a measured attack” (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-61/kotoba.md:40`), but the plan records those attacks as measured against draft predicate text, not the landed counter (`plans/round-62.md:19-24`; `.ufo/waves/round-62/w1/ScoutPriorReceipts.md:10-18`). · captured-by: C1 absorption matrix; its recorded command `python3 -B verifiers/check_erratum_absorption.py --self-test` reports `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2` (`.ufo/waves/round-62/controls/absorption-hollow.txt:16-27`). · fix: `verifiers/check_scoped_rules_v31.py` adds G7 (`:1046-1088`) and explicitly keeps G9 (compound-purpose) as a declared surviving bound (`:2578-2615`); pair it with Q57 and the C1 matrix. · shown able to fail: `.ufo/waves/round-62/controls/absorption-hollow.txt:5-8` records the hollow variant exiting 1, but its diagnostic is a missing `check_scoped_rules.py` path, not the intended guard-direction rejection; the instrument report separately records the hollow shortcut rejected for missing run records (`.ufo/waves/round-62/w1/ExecAbsorbInstrument.md:70-72`).

## Status changes (contract rule 2, old → new)

- S118 `queued` → `mined` — `corpus/SOURCES.md:129` now names this lesson and `corpus/knowledge/erratum-absorption-round62.md` in `used-by`.

## Falsify corrections
- (to be filled by wave 2)
