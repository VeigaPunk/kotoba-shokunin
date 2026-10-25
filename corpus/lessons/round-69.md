---
author: kotoba L1 (round 69, hyaku run 6, attempt 2)
date: 2026-10-25
round: 69
lane: kotoba
---

# Round 69 — lesson (kotoba, hyaku run 6)

Attempt 1 died 13 minutes in on a provider error (watchdog
`lane-dead-no-report kotoba round=69`). Its uncommitted outputs were inherited: the frozen plan
commit `a238989a` (claims, three counters, base/junk controls, freeze receipt), the assimilation
scratch under `.ufo/waves/round-69/assimilation/` (append-block, entry draft, validate receipt,
collision files), and the control receipts under `.ufo/waves/round-69/controls/`. They were
re-verified and reused; nothing else from attempt 1 was carried.

**Freeze receipt explanation (checks the entry-absent exit 2).** The freeze receipt
(`.ufo/waves/round-69/controls/freeze-receipt.txt`) records `check_skill_precedence --self-test`
exit 2 (`selftest setup failed: the entry is not present in the working tree`) at freeze time.
That is a setup artifact, not a defect verdict: the counter's `--self-test` builds its honest world
from the working-tree entry (QUALITY Q48), which only exists after C1's content lands. The content
verdict for a missing entry is the measurement path (`--rev` → `0 of 5`, exit 1), which the base
control exercises. At the committed round-69 tip, with the entry present, `--self-test` exits 0
(18 assertions).

## Gate

The round assimilated from the read-only campaign package
`/home/vgpnk/Projects/shokuknow/merge/kotoba/` on **one theme**: **skill name-collision
precedence** — what a client documents about two same-named skills. Nothing in that tree was
written, committed or executed; only its bytes were read.

**Admit (5 source rows, 1 knowledge entry).** Every cited source was re-opened by this round —
the campaign's own `opened` date and quote prove nothing about this lane (CORPUS.md rule 1). The
access date below is **this round's** date, not the campaign's.

**Delta against round 50, stated before the rows.** `skill-selection-rules-round50.md` already
carries a "which one wins" column with same-name rules for six client pages, opencode's exact
uniqueness sentence among them (S024's page). This round's new ground is the **four clients that
column does not hold** (Roo Code, Amp, Deep Code, Junie) plus the cross-client synthesis; the
opencode row is re-carried, not discovered. Two route facts bound the opencode row: the cited
`/docs/skills/` route states only uniqueness, while `/v2/docs/skills/` (registry row S064,
mined in round 54 for a different question) carries a § Precedence ladder — the row and entry
scope themselves to the V1 route and claim nothing about the ladder.

**Tier.** All six rows are tier A: `CORPUS.md`'s tier rule makes official client documentation A,
which is what the lane's other client-docs rows (S022, S024, S025, S029) use; the r68 cohort's
tier B (S199-S202) is not re-litigated here.

- **S203 — Roo Code Documentation — Skills**, https://docs.roocode.com/features/skills — opened
  2026-10-25 by the L1. Located under `What Skills Let You Do` → Override Control; the located
  quote is: "Project skills override global skills, mode-specific override generic" (8 words). The
  same page's `Choose a location` lists label the native root "Roo-specific (higher priority)".
- **S204 — Amp — Agent Skills**, https://ampcode.com/docs/customize/skills — opened 2026-10-25 by
  the L1. Located under `Skill Sources and Precedence`; the located quote is: "Local skills mask
  repository skills with the same name." (9 words).
- **S205 — Deep Code — Agent Skills**, https://deepcode.vegamo.cn/en/docs/configuration/agent-skills
  — opened 2026-10-25 by the L1. Located under `Scan Locations`; the located quote is: "only the
  highest-priority one is kept" (6 words).
- **S206 — Junie — Agent Skills**, https://junie.jetbrains.com/docs/agent-skills.html — opened
  2026-10-25 by the L1. Located under `Skill location`; the located quote is: "the project-level
  skill takes precedence and the user-level skill is ignored." (11 words).
- **S207 — opencode — Agent skills**, https://opencode.ai/docs/skills/ — opened 2026-10-25 by the
  L1. Located under `Troubleshoot loading`; the located quote is: "Ensure skill names are unique
  across all locations" (8 words).

**Admit (1 correction row).** **S208 — Microsoft Agent Framework — Agent Skills**,
https://learn.microsoft.com/en-us/agent-framework/agents/skills — opened 2026-10-25 by the L1.
Located under `Use Agent Skills with Harness Agent`, at both occurrences of the approval
sentence (the page's separate `Tool approval` heading carries a different sentence about the
provider's tool names); the located quote is: "All three skill tools require approval by
default." (8 words). S208 supersedes the S201 row's anchor; S201 keeps the
`Security best practices` sentence as its anchor. The r68 entry names S208 in an appended
amendment and carries a `source: S208` line.

**Reject (1 staged claim, kept as a refusal with a flip condition).**

- **Refused — the staged S201 quote "All three skill tools require approval by default".** The
  round-68 lesson refused the staged wording as a *paraphrase* of what the page states ("The
  staged wording is a paraphrase", `corpus/lessons/round-68.md:52-58`), not by claiming absence.
  That judgement was **wrong**: the sentence is verbatim on the page (twice), and the true defect
  was the anchor (it sits in the tool-approval prose, not under `Security best practices`).
  The refusal is corrected by S208 and mined as mistake R68-6 below. Flip: the correction would
  be withdrawn only if the sentence stopped being verbatim on the page at the section named
  above — i.e. a re-fetch of that section finds different wording.

**Shaping notes (QUALITY Q42, routed defect R68-4).** S200's located quote drops `<code>` tags
around `.kilo/skills/` (the words are contiguous on the fetched page; the tags are a later
inline-code render). S202's located quote drops `**` bold markers around "Standard Agent Skills
path" (the words are contiguous on the fetched line; the markers are inline emphasis).

**Stripped `recheck` prose** (from the staged rows, kept here per the contract):

- S203 — "re-fetch the page and confirm the Override Control bullet and the native-root priority
  label are unchanged"
- S204 — "re-fetch the page and confirm the local-masks-repository sentence is unchanged"
- S205 — "re-fetch the English page and confirm the highest-priority-kept sentence is unchanged"
- S206 — "re-fetch the page and confirm the project-level-precedence sentence is unchanged"
- S207 — "re-fetch the page and confirm the uniqueness check is unchanged"

**Id collision (checked in scratch, before the first append).** 128 registry ids
(`assimilation/reg-ids`), 188 staged ids (`assimilation/staged-ids`), **0 collisions**
(`assimilation/collisions`, empty by construction: `comm -12` of the two sorted id files). The
guard's non-vacuity proof
(`assimilation/guard-proof/`) shows an indented `  | S203 |` row collides under the census
parser's 0–3-space pattern and is missed by a column-zero-only pattern. The adopted ids continue
the lane's registry as staged (S203–S207); no renumbering was needed and no citation was re-pointed
by arithmetic.

**Scratch transformation and validation, before the first append.** The append block was built in
scratch from the rows the admitted entries cite, normalized to the lane's 11-column schema, and
mirrored over a copy of the lane's `corpus/` plus `SKILL.md`:
`scripts/sources-census.sh validate --file .ufo/waves/round-69/assimilation/validate/corpus/SOURCES.md`
→ **exit 0** (`file ok`, warnings only), first run at attempt 1 and re-run after this round's
append.

**Quarantine — the campaign's absent-defect register, this lane's slice.** Derived in scratch
(`awk` over the register's data rows): **13 rows** — 7 carry the register's `payload-absent`
verdict and 6 carry `unreachable` (`assimilation/quarantine-slice`; the six `unreachable` rows'
class cell is the register's `unfetchable` wording, recorded here as `unreachable`). Hand-checked
this round: every `payload-absent` row refused (the quoted span was not located on the page this
round fetched), every `unreachable` row marked unverifiable. Rows S185 (Roo Code) and S172 (Junie)
are this theme's rows; both were re-opened under S203 and S206 with quotes located this round —
S172's register span truncates mid-word and elides both `<code>` parentheticals, so its
`payload-absent` verdict names a folded anchor copy rather than a missing payload (the M111 class
recurring on the campaign surface, where Q62's scope does not reach). Nothing from the register
was adopted.

**considerthese.** One still-unimplemented proposal mined from the operator-authored
`considerthese/2026-10-24.md` (never edited): the skill-description audit against the committed
per-client threshold table. The reflection is a pointer, not evidence; the C1 entry's `## Scope`
and the round's claim declarations cite the same bar. The measured description stands at 1,020
parsed characters against the documented 1,024 cap — the proposal stays open.

## Mistakes

- **M111 — class: a refusal whose reason is false (R68-6, S201).** Evidence: `corpus/lessons/round-68.md`
  § Gate refused the staged S201 quote "All three skill tools require approval by default" — not by
  claiming absence, but by judging the staged wording a *paraphrase* of a tool list. The sentence
  is verbatim on the page (twice), and the r68 scout log
  (`.ufo/waves/round-68/w1/logs/ScoutMsAgentFramework.log:62-64`) already recorded it as present but
  outside the `Security best practices` subsection; the true defect was the anchor. Captured by:
  R68-6 in `corpus/lessons/round-68-verifier-spotcheck.md` for this instance, and M33 in
  `corpus/lessons/round-51.md` (captured by Q23 + Q14) for the class. **Fix (shown able to fail):**
  row S208 quotes the approval sentence in its anchor and supersedes the S201 anchor, the r68 entry
  gains a `source: S208` line, and QUALITY Q62 grounds refusals in observed facts. The fix fails
  the counter's D5/D6 conjuncts at `a5f7459` (measured `0 of 8`) and passes them at the round-69
  landing commit.
- **M112 — class: uncommitted round-68 wave paths (R68-7).** Evidence: 24 lane-authored paths
  under `.ufo/waves/round-68/w1/` (10 modified logs/drafts, 14 untracked seat reports/controls)
  were uncommitted at the r68 tip while the r68 report's landed-changes row said evidence landed at
  `2dd3567a`; one of them, `.ufo/waves/round-68/w1/controls/c2falsify-clone/`, is a 269 MB git
  clone — the M109 class recurring. Captured by: the r68 closure's routed defect R68-7
  (`corpus/lessons/round-68-verifier-spotcheck.md` § Routed defects; "landed means committed").
  **Fix (shown able to fail):** each of the 24 paths is committed under this round's landing
  commit, or dispositioned — the clone is dispositioned as
  `disposition: removed .ufo/waves/round-68/w1/controls/c2falsify-clone/` — and D7 also pins the
  landed diff at +6379/−251, so a one-line replacement of the largest log fails the counter.

## Status changes

- S203, S204, S205, S206, S207 — `mined` at landing (2026-10-25), tier A (official client docs,
  `CORPUS.md` tier rule), kind `docs`, recheck
  `90d`, `used-by corpus/knowledge/skill-name-precedence-round69.md`.
- S208 — `mined` at landing (2026-10-25), tier A, kind `docs`, recheck `90d`, `used-by
  corpus/knowledge/client-trust-gates-round68.md`; `teaches` opens `supersedes S201 —`.
- No prior row's `status`, `recheck` or `used-by` was changed: `corpus/SOURCES.md` gained six rows
  and lost none.

## Errata (appended in round 70; the text above is not edited)

- Erratum (K69-10): the § Gate preamble's "`--self-test` exits 0 (18 assertions)" is stale — the shipped counter `verifiers/check_skill_precedence.py` prints `self-test: 0 failure(s) over 22 assertions` at the r69 tip `9ce102b9e3f8896d5ed3f050ee896ca90d693a38`, as `controls/postfreeze-receipt.txt` and `.ufo/waves/round-70/receipts/r69-tip-defense.txt` record; "(18 assertions)" above reads 22 assertions.
- Erratum (K69-9): the § Status changes line "No prior row's `status`, `recheck` or `used-by` was changed" is true of those three cells but omits an in-place edit outside them: S201's anchor cell changed from `(13 words)` to `(14 words)` in `a02ba7e` (`git diff a5f7459 9ce102b -- corpus/SOURCES.md`). The new count is the true one; the old→new log the SOURCES contract requires is in `corpus/lessons/round-70.md` § Status changes.
