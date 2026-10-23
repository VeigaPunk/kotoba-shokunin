Result: MIXED — S070's quote is byte-exact on the live page at the stated location and every grounding mechanic holds, but the "only included via `/skill-name`" absolutes carried in four lane cells are under-cut by the same page's Custom-Mode path (`cursor-skills.md:29,218`).

# Reopen S070 (Cursor Docs — Agent Skills, https://cursor.com/docs/skills.md)

## Re-open receipt (my own fetch, read-only)

```
$ date -u
Fri 23 Oct 2026 12:09:33 AM UTC
$ curl -sS -o cursor-skills.md -w 'HTTP %{http_code}\nbytes %{size_download}\n' https://cursor.com/docs/skills.md
HTTP 200
bytes 18477
$ sha256sum cursor-skills.md
a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d
```

Byte-identical to the receipt in `corpus/SOURCES.md:83` and `corpus/lessons/round-55.md:19`
(HTTP 200, 18,477 B, sha256 `a642fa96…`, opened 2026-10-22T23:12:21Z by seat SrcCursor). The page
has not moved since admission. Fetched bytes kept at
`/fast/scratch/hyaku/kotoba-r55/ReopenS070/cursor-skills.md` (348 lines).

Host pin: `verifiers/check_explicit_invocation.py:136` gives
`HOSTS["Cursor"] = ("cursor.com", "docs.cursor.com")`; the URL host `cursor.com` matches.

Revision note: the lane working copy is `722e474a…`; `git diff HEAD f0e6b695` is empty for
`corpus/SOURCES.md`, `corpus/lessons/round-55.md`, `corpus/knowledge/explicit-invocation-round55.md`
and `SKILL.md`, and `git show f0e6b695` of each affected cell returned the text checked below —
so all cells reviewed are exactly the tip's cells.

## Per-cell verdicts

| cell | verdict | evidence |
|---|---|---|
| Gate quote (`corpus/lessons/round-55.md:19`) | **HOLDS** | "When `true`, the skill is only included when explicitly invoked via `/skill-name`. The agent will not automatically apply it based on context." is a byte-exact substring of the fetched bytes, sitting inside the `disable-model-invocation` row at line 175 (stated `cursor-skills.md:175`). 22 words (≤25). No normalisation needed — the backticks are in the raw bytes; the counter-normalised form is also a substring (`When true, the skill is only included…` in normalised page: True). |
| teaches (`corpus/SOURCES.md:83`) | **HOLDS** (borderline, see finding) | 16 words ≤25. "included only when explicitly invoked via `/skill-name`, never automatically" compresses `:175` faithfully. |
| entry quote + location (`corpus/knowledge/explicit-invocation-round55.md:27`) | **HOLDS** | Identical string to the Gate quote, same correct location `:175`; contains the SKILL.md form token `/skill-name` verbatim and the word `skill`. |
| entry reading (`…:27`) | **HOLDS** (borderline, see finding) | "Typing `/` plus the skill name in Agent chat invokes it for one message (`:29`)" compresses `:29` ("manually invoked by typing `/` in Agent chat and searching for the skill name. A skill invoked this way attaches to one message"). |
| SKILL.md form (`SKILL.md:204`, `/skill-name`) | **HOLDS** | Token matches TOKEN_RE and occurs verbatim in the quote; `:214` documents typing `/skill-name` in chat. |
| SKILL.md what-it-does, clause 1 ("Attaches the named skill to one message (`cursor-skills.md:29`)") | **HOLDS** | `:29` literally says "attaches to one message". |
| SKILL.md what-it-does clause 2 + teaches "only" clause + entry reading "only way" clause + SKILL.md action clause 2 | **BREAKS** (over-wide, page-internal counterexample) | see finding below |

## Finding 1 — the "only included via `/skill-name`" absolutes are over-wide on the sourced page itself

Over-wide phrases:

- `SKILL.md:204` action: "**a flagged skill can only appear in such turns**"
- `SKILL.md:204` what-it-does: "`disable-model-invocation: true` makes this **the only way it is included**"
- `corpus/knowledge/explicit-invocation-round55.md:27` reading: "with the flag set it is **the only way the skill is included**"
- `corpus/SOURCES.md:83` teaches: "included **only** when explicitly invoked via `/skill-name`" (mirrors the vendor wording, so the least culpable of the four)

The page states the absolute twice — `:175` ("the skill is only included when explicitly invoked via
`/skill-name`") and `:214` ("it is only included in context when you explicitly type `/skill-name` in
chat") — but the same page documents a second inclusion path it never exempts from the flag:

- `:29`: "To keep a skill on for the whole session, use it as a Custom Mode with Option+Enter (Mac) or
  Alt+Enter (Windows)."
- `:218`: "**Any** skill with a valid frontmatter block can back a Custom Mode, which keeps the skill
  in context for the whole session."

`disable-model-invocation` is itself a valid frontmatter field (`:175` is its table row), so on the
page a flagged skill can back an active Custom Mode and sit in context in turns whose message never
used `/name`. The cells repeat the page's absolute, so none of them says more than the page's flag
row — but the page taken whole does not support the absolute, and the cells give the reader no bound.
Concretely, SKILL.md's action cell advises a classifier "a flagged skill can only appear in such
turns"; by `:218` that advice can misclassify Custom-Mode turns (the flagged skill appears, no `/name`
was typed). The honest bound would be "the only *automatic/chat-invocation* path" or a note that
Custom Modes are a separate documented inclusion path. This is the same shape as round-54 routed
defect 3 (over-wide C1 cells, `corpus/lessons/round-55.md:54`): the cell asserts an exclusivity the
page hedges elsewhere on the page.

Mitigating facts for the L1: the absolute is the vendor's own wording (the cell quotes it
byte-exactly), and whether a flagged skill *actually* backs a Custom Mode is undocumented — the page
is silent, so this is a documented-capability counterexample, not a demonstrated one. If the
standard is "the cell must say no more than the page", the flag row alone technically warrants the
clause; if the standard is the round-54 over-wide-cell bar (cells must not assert what the page
under-cuts elsewhere), all four clauses are over-wide.

## Mechanics (all HOLD)

- S070 is new this round: `git show f0e5de82:corpus/SOURCES.md | grep -c 'S070'` → 0.
- Row shape at tip: 11 cells; kind `docs`, tier `A`, status `mined`, opened `2026-10-22`, used-by
  names `corpus/knowledge/explicit-invocation-round55.md` and `corpus/lessons/round-55.md`.
- Locations all verified on the fetched bytes: § How skills work `cursor-skills.md:29` ✓ (sentence at
  line 29), `disable-model-invocation` row `:175` ✓, § Disabling automatic invocation `:212-214` ✓
  (heading `:212`, rule `:214`).
- Other S070 uses checked (`grep -rn 'S070'` lane-wide): knowledge frontmatter `source:` line (matches
  the fetched URL), Findings 1 and 3 (`:33` `/` sigil in Cursor ✓; `:44` "Cursor
  `disable-model-invocation: true` (S070 `:175`)" ✓ but shares the flag's "only" reading), and
  `falsify/CriticNewGround.md:24` (new-ground bookkeeping, no content claim needing the page).
- No installs needed; fetch via system `curl`, checks via `python3`, `grep`, read-only `git`.
