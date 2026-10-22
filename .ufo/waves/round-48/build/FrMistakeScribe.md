# FrMistakeScribe — round-48 frontier: mined class, landing state, discriminating demonstration

Seat: `KotobaR48.FrMistakeScribe` (scribe, leaf, no delegation). Lane base `75f671b109d8eddd0d64c1429bd6379fe577175a`; HEAD at close `84b9c9ba89559b51a72c83c2b9605b184df4ae9e`. Read-only on the lane except this report. Tools installed or updated: none (system `python3`, `git`, `curl`, `sha256sum` only).

## Findings

### F1 — The mined class arrived, merged into landed M24 (not M27)

The class I mined (attribution truth: a registry `teaches` cell claims a rule an authority's own bytes do not carry / denies a rule they do carry) is already integrated into the landed lesson `corpus/lessons/round-48.md` as **M24 "Rule credited to the wrong authority, and a lexical approximation described as a vendor rule"**, captured-by `none → Q20`. The number I had reserved (M27) landed with a *different* class (instrument self-hash through process substitution). So round-48 already carries the class; my contribution is the **discriminating demonstration** (F2) and the sub-report closure.

Landing commit: `887b6af` (M24–M27), HEAD `84b9c9ba`. `git cat-file -e HEAD:corpus/lessons/round-48.md` → exit 0.

### F2 — Landed M24's "shown able to fail" is link-presence, not attribution truth

Landed M24 demo: `git show 75f671b:SKILL.md | sed -n 151p` → 0 hits for `frontmatter-rule-authorities`; landed line → 1. But appending the link to the base line while it still cites S001/S003 and names no parsed rule also yields 1 (`grep -c 'frontmatter-rule-authorities'` on base + `+ append "See corpus/knowledge/frontmatter-rule-authorities-round48.md."` → 1, still citing `S003`). Link counts do not test the mis-credit. The fix's ability to fail is better demonstrated by the attribution checker (F3), which fails on the live S003 cell and passes on corrected superseding wording.

### F3 — Attribution checker: exact demonstration (5 arms, all rerun this session)

Prototype (scratch, not a lane instrument; never run against the lane gate battery): `attribution-check.py` (sha256 `3f650a72…`). It binds each claim to (a) authority bytes sha256-pinned in `manifest.json`, and (b) the exact lane row via `git show 75f671b:<path>` / `WORKTREE`. Exit 0 = every claim matches stated polarity; 1 = refuted; 2 = usage/cache/manifest/lane-blob error.

Exact command (one arm):

```
python3 -B attribution-check.py --manifest manifest.json --cases cases-lane-today.json \
  --cache cache --lane /home/vgpnk/Projects/shokunin/kotoba-shokunin
```

Arms (each rerun now; exit codes verbatim):

| arm | cases | exit | output |
|---|---|---|---|
| A1 live lane (75f671b S003 cell) | `cases-lane-today.json` | **1** | `cases=9 refuted=1`; refuted `s003-lacks-500-line-rule` (`present=False` vs spec line 237 `under 500 lines`, `count=1`) |
| A2 corrected superseding wording | `cases-superseding-control.json` | **0** | `cases=8 refuted=0` |
| A3 polarity mutant (S003 500-line flip present→absent) | `cases-polarity-mutant.json` | **1** | `cases=8 refuted=1`; `s003-mutant-absent-500-line holds=False` |
| A4 tampered manifest sha | `manifest-tampered.json` | **2** | `ERROR: sha256 drift for agentskills-specification.md` |
| A5 S019 worktree-bound superseding control | `cases-s019-supersede-control.json` | **0** | `cases=8 refuted=0` |

So: live cell refutes (exit 1), corrected superseding wording passes (exit 0), polarity mutant fails (exit 1), tampered pin blocked (exit 2), and the S019 superseding rows (peer FrSourcesRowsScribe) validate (exit 0). This is the fix "shown able to fail": it catches the mis-attribution and validates the repaired cells.

### F4 — Q20/Q21 landed with different grounding names than the FrQualityCriteria draft

`corpus/QUALITY.md` at HEAD has Q01–Q21; Q20/Q21 are grounded in the *landed* M24/M26 (not the FrQualityCriteria draft class names). FrQualityCriteria confirms their earlier Q20/Q21 draft was superseded and deleted; the only patch they ship is `quality-q22-q23.patch` (adds Q22 after Q21, applies cleanly to `84b9c9ba`, 23 Q-rows, 6 pipes each). M25 and M27 have no QUALITY grounding row at HEAD (`git show HEAD:corpus/QUALITY.md | grep -c 'M25\|M27'` → 0); Q22 is absent (count of `^| Q2` = 2). Not mine to add — FrQualityCriteria owns QUALITY rows and has Q22/Q23.

## Evidence

- `git rev-parse HEAD` → `84b9c9ba89559b51a72c83c2b9605b184df4ae9e` (exit 0).
- `git log --oneline -1 887b6af` → "round-48: C1 freshness – knowledge entry …; SOURCES S016-S021 …; lesson round-48 (M24-M27, Gate); Q20-Q21; …" (exit 0).
- Lesson M-rows at HEAD: `M24 M25 M26 M27` (`grep -o "^| M[0-9]*"`).
- QUALITY Q-rows at HEAD: Q01–Q21 (no Q22). `grep -c "^| Q2"` → 2.
- SOURCES S019 at HEAD: present (`grep -c "^| S019 "` → 1); worktree clean for `corpus/SOURCES.md`.
- `grep -rn "teaches" verifiers/*.py` → no output (exit 1); captured-by `none` confirmed: no lane instrument checks attribution truth.
- Authority bytes (fetched this session, 2026-10-22T08:55Z; sha256 pinned): `agentskills-specification.md` `9a67de89…`; `anthropic-best-practices.md` `f0a5d61b…`. Located quotes: spec line 237 "Keep your main `SKILL.md` under 500 lines."; bp line 155 "Cannot contain XML tags". Spec `grep -ci 'XML tag'` → 0; `grep -ci 'angle'` → 0. (These pin the S003 cell refutation.)
- Scratch artifacts (sha256): `attribution-check.py` `3f650a72…`; `attribution-demo.sh` `84345412…`; `demo-one-liner.sh` `0787daac…`; `manifest.json` `c1113421…`; `cases-lane-today.json` `9537e81e…`; `cases-superseding-control.json` `2ade7f0c…`; `cases-s019-supersede-control.json` `022f7393…`; `cases-polarity-mutant.json` (written this session); `agentskills-specification.md` `9a67de89…`; `anthropic-best-practices.md` `f0a5d61b…`.

## Coordination

- `FrQualityCriteria` (Q20/Q21 landed; will ship Q22/Q23 patch; carries M28/M29 rows I relay to L1 — I cannot edit the lesson, read-only bound).
- `FrSourcesRowsScribe`: S018/S019 superseding rows validated by A2/A5 (exit 0); their Gate table/sweeps are paste-ready; their E11 blocked until lesson file landed — now landed at `887b6af`.
- My Q23 slot: released (the attribution class is already Q20-captured); FrQualityCriteria uses Q22 (defect 4 custody) + Q23 (defect 5 closure metadata).

## Out-of-scope / handed off

- Lesson file authorship and further rows are L1's; I do not edit `corpus/lessons/round-48.md`.
- M28 (custody) / M29 (closure metadata over frozen inputs) rows: FrQualityCriteria hands the verbatim text; I cannot paste into the lesson — they must be appended by L1 after the landed M27 (their evidence: copy-of-receipt `sha256sum` identical `8bec447a…` while `stat -c '%i'` differs; `git cat-file -e` exit 128 on six scratch commits, exit 1 on tree `a736f640…`; M29: tracked-but-unindexed lesson → `verify_corpus_integrity.py` DRIFT 1, baseline bump alone still exit 1, index row + expectation → exit 0).
- Attempt-1 stale-author process (candidate b): covered by FrAttempt1Audit report; no Mistakes row (routed item 4 disposed it). No triangle with this report.
