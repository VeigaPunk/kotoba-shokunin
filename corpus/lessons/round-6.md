# Lessons — round 6

Round: 6. Evidence: `LOG.md` round-6 entry, commit `a614927`, report
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-6/kotoba.md`,
artifacts `knowledge/agent-def-audit-round6.md`,
`knowledge/claude-md-surface.md`, `knowledge/trigger-miss-proxy-round6.md`.

## Worked

- **Second verbatim-checklist audit lane, second healthy yield.** Handing a
  blank-context reviewer the 9 items verbatim again produced a strict matrix
  + 10 meta-findings; zero clarification requests. Pattern confirmed: a
  checklist is dual-use — it audits files *and* audits itself. Both audits
  (round 5 + 6) shipped definitional fixes the same round.
- **The mechanical proxy beat expectation.** Literal-trigger measurement was
  filed as "needs a labeling pass" — the cleaned session-level proxy
  answered a narrower but real question in ~20 lines of SQL+python: unique
  trigger tokens have 0% literal miss; the residual miss mass is
  domain-term ambiguity, not router failure. Cleaning mattered: raw text
  turned `/skill:godspeed` dispatch blobs into 60 phantom `ufo` hits; after
  scrubbing slash-tokens and injected directive text, `ufo` intent sessions
  dropped 105→13.
- **Cross-surface census discipline.** CLAUDE.md survey classified before
  measuring: 16 files → 5 authored / 1 template / 10 vendored; loader strings
  prove *recognition*, not *injection* — 0 captured system-prompt inclusions
  and no session ever ran in a CLAUDE.md dir. "Cold channel" is the honest
  verdict, not "works".
- **Meta-finding → checklist fix loop is fast.** All 10 audit meta-findings
  resolved in SKILL.md the same round (schema-not-list key rule,
  same-name-differing-content blocks, file-path bases, harness-literal
  carve-out). The audit also corrected *my own* round-4 counts (13→14,
  7→11) — durable evidence claims drift in counting, not just in text.

## Failed / weak

- **`edit` boundary-echo, fourth round running.** This round's instance:
  `PUT >N` after a same-file `PUT N.=M` in one batch duplicated a line;
  a `PUT N.=M` replacement auto-repaired (dropped a body line already
  present) leaving a stray duplicated header in SHONEN.md. Signature is now
  sharper: *any op whose body text equals adjacent file text* risks a
  boundary echo — two occurrences this round, both caught by re-reading.
  Mitigation that works: re-read the edited region after every `edit` batch;
  never batch two ops on the same file where bodies echo file text.
- **The round-4 counts were wrong and nobody noticed for two rounds.** 13/18
  and 7/18 stood in SKILL.md + corpus for two rounds until an auditor
  re-counted. Lesson: census claims in durable files need a re-countable
  recipe stored next to the number (the md5sum recipe existed; the count
  itself still drifted — the recipe must be *re-run*, not just stored).
- **`the-*` name literals were invisible to my checklist draft.** AD-4's
  original "recognized values" enumeration couldn't adjudicate real keys;
  the audit's meta-3/meta-7 forced the schema-based rewrite. Drafting
  checklists against *observed* key inventories (not imagined ones) is the
  fix — the evidence file already had the inventory; I didn't consult it.

## New evidence (opinion-flagged where not provable)

- **godspeed's always-on contract leaks at the harness layer.** 205/398
  sessions loaded it (51.5%) despite "use on every prompt" — [INFERENCE]
  the leak is likely offer-side (skill not catalogued or compressed render
  dropped in some lanes), not refusal-side: loaded-when-named rate is ~72%.
  A `description` rule cannot fix an offer-side hole; worth relaying as a
  routing/harness finding, not a craft defect.
- **Agent-definition fleet health > SKILL.md fleet health** (15/18 vs 0/5
  fail) — the difference correlates with hand-maintenance vs template
  minting. Prediction: the mint-template fix remains the single highest-
  leverage change for the sibling fleet; this round's audit adds that
  template-minted files should mint *with* a checklist run.
- **`ufo.md` is the riskiest file in the agent fleet** — the default_agent,
  largest file (197 lines), missing `name:`, carrying a 30-day-stale seat
  note, and delegating via `the-*` names no roster key matches. One file
  concentrates 3 of the fleet's 4 fail cells' surroundings.
