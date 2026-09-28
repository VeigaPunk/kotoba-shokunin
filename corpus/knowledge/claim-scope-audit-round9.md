# Harness-claim scope audit — round 9 (before → after)

Round 9 axis move: **consistency**. Target `SKILL.md`; the defect class is a
claim that is true on one skill harness but written as a universal rule.
Before-state measured by an L2 sentinel lane against `SKILL.md` md5
`143fe473368ec9e2bb7adde9d0425b1c` (487 lines, working tree `8c300ad`); the
lane wrote only `/tmp` scratch, so the baseline is reproduced here in-repo.
After-state measured on the landed file (see `LOG.md` round-9 for the commit).

Method: sweep every claim marker (`router`, `cliff`, `<skills>`, `slice(0,99)`,
`render`, `truncat`, `catalogue`, `compressed`, `99`, `sees`), split into claim
units, classify **SCOPED** (names its harness), **UNSCOPED** (universal wording,
true on one harness only), **UNSUPPORTED** (no citation).

## Before — `SKILL.md` @ `143fe473…` (31 claim units)

`UNSCOPED=9 UNSCOPED-with-counterexample=9 UNSUPPORTED=7` (15 SCOPED).
`grep -c '<available_skills>' SKILL.md` → `0` — the opencode surface was
absent from the file entirely.

| Lines | Verdict | Claim (abridged) | Harness counterexample |
|---|---:|---|---|
| 21–29 | UNSCOPED | "the `description` is the only part the router always sees … cache-or-truncate … `slice(0,99)`" | opencode renders it untruncated |
| 27–28 | UNSCOPED | "only 5/17 skills have cached renders … the truncator is the default" | opencode has no such cache/truncator path |
| 68 | UNSUPPORTED | "frontmatter = router index; body = executor contract" | no citation; one-harness contract |
| 70 | UNSUPPORTED | "No frontmatter, no router — every byte loads every time" | no citation; loader not verified |
| 132–138 | UNSCOPED | "on this host the router sees it through a cache-or-truncate render" | names no harness |
| 139–142 | UNSCOPED | "Measured over the live 17-skill catalogue: only 17.7% of source description chars reach the router" | omp-only measurement |
| 149 | UNSUPPORTED | "Quoted strings match how routers and humans actually phrase intent" | no citation |
| 159–161 | UNSUPPORTED | "the router never reads the body" | stage/harness unnamed |
| 172–180 | UNSCOPED | "The 99-char cliff is absolute" | opencode has no cliff |
| 173–174 | UNSCOPED | "Anything past ws-collapsed offset 99 is invisible in the default path" | omp only |
| 182–185 | UNSCOPED | "If the first `.`/`!`/`?` sentence is ≥40 chars it renders whole … discards sentence 2+" | omp truncator branch |
| 241 | UNSUPPORTED | "the router can't either" | metaphor presented as measured limit |
| 255–256 | UNSUPPORTED | "body/PROVINCE boundary text does not count — the router never reads it" | stage unnamed |
| 387 | UNSUPPORTED | "Router never sees it; false activation" | no harness |
| 402 | UNSCOPED | "Default render is `slice(0,99)`+`…`" | opencode default is untruncated |
| 403 | UNSCOPED | "The ≥40-char first-sentence branch renders sentence 1 verbatim" | omp branch only |

## After — landed `SKILL.md` (round-9 commit)

Independent sentinel re-measurement on the landed file (29 claim units):
**UNSCOPED 9 → 0**, UNSUPPORTED 7 → 6, SCOPED 15 → 23; of the 16 before-defects,
10 RESOLVED and 6 RESIDUAL (all six uncited rather than false-on-one-harness).
The six residuals were then cured in the same round by re-wording each to cite
the router model or to be labelled guidance/heuristic — post-cure greps:
`grep -c 'router never\|Router never\|router can.t either\|every byte loads every time'` → 0.

| Probe | Before | After |
|---|---:|---:|
| `grep -c '<available_skills>' SKILL.md` | 0 | 3 |
| `grep -c 'on this host the router sees'` | 1 | 0 |
| `grep -c 'the router always sees'` | 1 | 0 |
| `grep -c 'the truncator is the default'` | 1 | 0 |
| `grep -c '10681'` (superseded drift count) | 1 | 0 |
| `grep -c '5/17 skills today'` (superseded) | 1 | 0 |
| `grep -c '^## Router model'` | 0 | 1 |

New section `## Router model — which harness, which gate` carries a 5-column
decision table (`Harness | Catalogue tag | Description render | Offer gate
(action) | Failure mode`) with one row per harness, plus a check-before-predict
recipe per harness. Rules 8 and 9, the frontmatter-craft opener, the intro
paragraph and three anti-pattern rows now name their harness.

Residual risk recorded honestly: the wording "the router" survives in places
where both harnesses behave the same (frontmatter-only routing) — that is
scope-accurate, not a defect; the round-9 verifier lane's verdict on the landed
file is recorded in `LOG.md` round 9 and the round report.

Drift note that motivated part of the move: the omp cache tier grew
5/17 → 17/17 rows inside the round's window
(`sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from
skill_descriptions;"` → 17, db mtime `2026-09-28 17:57:58`, WAL-mode so the
mtime is a lower bound), so "the truncator is the default" was stale as well as
unscoped.