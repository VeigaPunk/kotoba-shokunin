# Lessons — round 7

Round: 7. Evidence: `LOG.md` round-7 entry, commit `round-7`, report
`/home/vgpnk/projects/shokunin/.ufo/reports/round-7/kotoba.md`, artifacts
`knowledge/render-mechanism-round7.md`, `knowledge/dispatch-prompt-audit-round7.md`,
`knowledge/alwayson-checklist-round7.md`. Nine L2 lanes in one batched
`task` call (MISSION.md floor: 8).

## Worked

- **Binary reverse-engineering beats log inference.** `strings -n 6` on the
  omp ELF recovered the actual render code (`H7s`, `_8n=100`, cache key
  formula, validator limits). One lane turned "the catalogue is
  model-compressed" — a claim that survived two rounds — into
  "cache-or-truncate" with byte-exact reproduction (12/17 + 5 cache rows).
  Lesson: when a claim names a binary artifact, `strings`+reimplementation
  is cheaper than another sampling round and strictly stronger.
- **The self-audit lane is the cheapest check I own.** Applying my own
  13-item checklist to my own SKILL.md found 4 fails + 1 ambiguity in a
  file that had passed two rounds of revision. Durable files accumulate
  defects of *definition*, not just drift — the checklist needed the
  recipe-vs-prerequisite carve-out and a "failure claim" definition it
  didn't have until a hostile reader asked.
- **Count claims carry drift insurance only if re-run.** The critic lane's
  stored recipes caught two silent drifts (CLAUDE.md 16→18, warns
  10191→10681) and falsified one of my own wordings ("byte-identical" →
  shape-identical, six distinct md5s). Recipe-in-file worked; the numbers
  still had to be re-executed.
- **Generator-vs-artifact split is where prompt defects live.** The stale
  `m_composer`/`m_antigravity`/`m_grok` aliases exist in 38 on-disk prompt
  files but the v3 generator already emits the correct bucket — the defect
  is *regeneration latency*, not the template. Auditing prompts without
  checking the generator would misroute the fix.

## Failed / weak

- **`edit` boundary-echo, fifth occurrence.** A `PUT N.=M` replacement left
  the original tail line ("their tokens. Rank: shonen.") orphaned after the
  new body. Same signature as round 6: bodies ending near the replaced
  block's end duplicate the tail. Mitigation stands: re-read every edited
  region; never batch two same-file ops whose bodies echo file text.
- **The round-5 "paraphrase" claim was wrong and propagated.** I wrote
  "rewrites, not truncates" into SKILL.md + corpus from one godspeed example;
  the godspeed render was actually the ≥40-char first-sentence branch of the
  truncator — a deterministic cut, not a model rewrite. Lesson: a single
  example of "looks rewritten" is not evidence of a model in the loop;
  byte-level reproduction is the only trustworthy test.
- **Self-audit pass ≠ self-audit coverage.** The reviewer lane adjudicated
  item 4 (sibling arbitration) as FAIL under strict reading — I'd rated my
  generic "owning domain skill" phrase as sufficient. The checklist's own
  wording ("N/A only when no named overlap exists") needed the lane's
  meta-finding to become enforceable.

## New evidence (opinion-flagged where not provable)

- **The `<skills>` catalogue is offer-side complete but content-lossy.**
  godspeed is offered in 3911/3911 session_init records — yet its render
  drops the trigger list. [INFERENCE] For always-on skills the omp router
  is largely irrelevant: the description's job there is human/dispatch
  readability, and AGENTS.md carries the actual always-on rule.
- **Shokunin SKILL.md files are router-invisible** — outside every omp
  discovery root. This reframes the sibling-fleet trigger defect: the
  descriptions don't misroute because they don't route at all; the audit
  value is craft hygiene + future discovery, not live activation.
  [INFERENCE] If siblings are ever symlinked into `~/.agents/skills/`, the
  trigger debt becomes real debt instantly.
- **Two catalogues in one hour** (`48ff8c9eeaef`/`aea95a70f738`, differ in
  exactly the 2 cache-late skills) show the render is nondeterministic across
  sessions — a lane's system prompt depends on when its session_init
  rendered, not just on disk state. Prompt-diff debugging across agents
  must diff the catalogue, not assume it.
