# SOURCES — where kotoba learns

`corpus/knowledge/` holds admitted facts; this file holds the places they come
from — what each teaches, how far to trust it for which scope, and when to look
again. Contract: fleet `SOURCES-CONTRACT-v1.md` (2026-10-19). A row exists only
for a source the row's author opened this round; access evidence lives in
`.ufo/round-46/evidence/w2/sources/fetch-log.json` (round 46), the seat reports under
`.ufo/waves/round-47/build/` (round 47), and the round lesson's `## Gate`.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Agent Skills — Specification — https://agentskills.io/specification | spec | A | SKILL.md frontmatter format and file-structure rules | § Skill metadata table, § Progressive disclosure; live page opened 2026-10-19 | Name is 1-64 lowercase-hyphen chars matching its directory; description 1-1024 chars saying what and when; SKILL.md under 500 lines with detail moved to reference files | mined | 2026-10-19 | on-release | corpus/lessons/round-46.md |
| S002 | Agent Skills — How to add skills support to your agent — https://agentskills.io/client-implementation/adding-skills-support | docs | A | Client-side loading and validation policy for SKILL.md | § Handling malformed YAML, § Lenient validation; live page opened 2026-10-19 | Unquoted values containing colons are technically invalid YAML; lenient clients warn and load anyway on name mismatch, so a strict local gate is stricter than the client contract | mined | 2026-10-19 | 90d | SKILL.md |
| S003 | Claude Docs — Agent Skills best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | docs | A | Anthropic authoring rules for name and description | § Skill structure field list; live page opened 2026-10-19 | The description cannot contain XML tags, must be third person, and states what the skill does and when; body under 500 lines; an Anthropic-only rule the open spec lacks | mined | 2026-10-19 | 90d | corpus/lessons/round-46.md, corpus/lessons/round-47.md |
| S004 | AGENTS.md — open format site — https://agents.md/ | spec | A | Always-on context-file precedence convention | § FAQ "What if instructions conflict?"; live page opened 2026-10-19 | Conflict rule for always-on files: the closest AGENTS.md to the edited file wins and explicit user chat prompts override everything | queued | 2026-10-19 | 90d | — |
| S005 | CommonMark Spec 0.31.2 — https://spec.commonmark.org/0.31.2/ | spec | A | Fenced code block syntax the lane's box/quote extraction implements | § Fenced code blocks; version 0.31.2 | A code fence is at least three backticks or tildes preceded by up to three spaces of indentation; a backtick fence's info string may not contain a backtick | queued | 2026-10-19 | on-release | — |
| S006 | RFC 8259 — The JavaScript Object Notation (JSON) Data Interchange Format — https://www.rfc-editor.org/rfc/rfc8259.txt | spec | A | Duplicate-name semantics in JSON objects (round-46 C2 door) | §4 Objects | Object names SHOULD be unique; when they are not, receiver behavior is unpredictable — the normative basis for the comparator's duplicate-member detection | queued | 2026-10-19 | on-release | — |
| S007 | Python docs — json: JSON encoder and decoder — https://docs.python.org/3/library/json.html | docs | A | This host's actual duplicate-name decode behavior | § Standard Compliance and Interoperability | Python's decoder accepts repeated names and keeps only the last pair, so a last-wins silent read is the implementation default the comparator must not inherit uncritically | queued | 2026-10-19 | 365d | — |
| S008 | YAML Specification 1.2.2 — https://yaml.org/spec/1.2.2/ | spec | A | Plain-scalar restrictions behind the frontmatter strictness lead | §7.3.3 Plain Style | Plain scalars must never contain the colon-space or space-hash combinations, since both are ambiguous with key/value pairs and comments | mined | 2026-10-19 | on-release | SKILL.md |
| S009 | kotoba own work — verifiers/compare_harness_independent.py --self-test — run 2026-10-19, exit 0 | own-work | A | The comparator's own self-model at the round-46 landing commit | Final line "self-test: 0 failure(s) over 328 assertions"; commit 78ee57e | The join driver's channel-agreement model, including cross-channel divergence classes, is exercisable on committed fixtures without either live instrument | queued | 2026-10-19 | on-commit | — |
| S010 | kotoba own work — verifiers/verify_skill_checklist.py — --self-test exit 0 and --json exit 1 (9 PASS / 1 FAIL governance.citation_resolves at LOG.md:2111) runs 2026-10-19 | own-work | A | The lane's executed-box gate and frontmatter parse coverage | Final line "0 failure(s) over 1597 assertions"; --json "checklist.box_map_complete ... 41 boxes mapped" | All 41 prose boxes are accounted for as executed, delegated, or unexecuted under a sha256-pinned normalization; the frontmatter check is a lenient structural parse with no XML-tag rule | queued | 2026-10-19 | on-commit | — |
| S011 | Agentman — How Do You Build Your First Agent Skill? — https://agentman.ai/blog/build-your-first-agent-skill-skillmd-anatomy | community | C | SKILL.md authoring claims for beginners | Field-table paragraph and "safety note" paragraph; opened 2026-10-19 | REJECTED: claims a name/folder mismatch means the skill "will not load" where the client guide (S002) says warn and load; credits an angle-bracket ban to the agentskills.io spec which has none (0 mentions); quantitative claims cite unnamed analyses; flip: re-check if the spec gains the rule or the client guide tightens to refuse mismatched names | rejected | 2026-10-19 | 180d | — |
| S012 | anthropics/skills — skill-creator reference skill (quick_validate.py) — https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator | code | A | SKILL.md `description` validation in Anthropic's own reference packaging tooling | `skills/skill-creator/scripts/quick_validate.py:79-81` "Check for angle brackets"; tree `dbd4588` (2026-10-09); opened 2026-10-21 | Anthropic's packager refuses any `<` or `>` in `description`, not only well-formed XML tags — stricter than the S003 prose rule; the open spec states neither | mined | 2026-10-21 | 90d | SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md |
| S013 | OpenAI — Build skills (ChatGPT and Codex) — https://learn.chatgpt.com/docs/build-skills | docs | A | Codex client skill routing: initial-list budget, description shortening, implicit invocation | § How ChatGPT and Codex use skills; page Last-Modified 2026-10-21T15:05:00Z; opened 2026-10-21 (308 from developers.openai.com/codex/skills) | Codex caps its initial skill list at 2% of context (8,000 characters when unknown), shortens descriptions first, and gates implicit invocation on the description | queued | 2026-10-21 | 90d | — |
| S014 | Anthropic Engineering — Equipping agents for the real world with Agent Skills — https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills | docs | A | Anthropic's three-level progressive-disclosure loading model for skills | § The anatomy of a skill, "At startup" paragraph; published 2025-10-16, modified 2026-10-18; opened 2026-10-21 | Name and description are preloaded for every installed skill as disclosure level one; the SKILL.md body loads only when the skill is judged relevant | queued | 2026-10-21 | 90d | — |
| S015 | kotoba own work — `sha256sum -c SHA256SUMS` in /fast/scratch/kotoba-r47/shared (frozen omp 18.12.5 and opencode 1.19.3 snapshot) — run 2026-10-21, exit 0 | own-work | A | Identity of the substrate bytes the round-47 instruction-surface re-derivation and re-pin measure | SHA256SUMS lines `bin/omp-18.12.5` fdbc8136… and `bin/opencode-1.19.3` 179ca421…; live `~/.local/bin/omp` and the npx-cache ELF hash equal | A substrate pin is the binary's sha256, not its version string or path: the opencode path moved channel (2.0.26 → npm 1.19.3) while the version string went down | mined | 2026-10-21 | on-release | corpus/knowledge/instruction-surface-census-round13.md |
| S016 | anomalyco/opencode — skill discovery, tag v1.19.3 — https://github.com/anomalyco/opencode/blob/v1.19.3/packages/opencode/src/skill/index.ts#L24 | code | A | Which directories under an opencode config directory are scanned for SKILL.md, and at what depth | `packages/opencode/src/skill/index.ts:24` `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"`; `:205-207`; `config/paths.ts:23-40`; tag v1.19.3 = upstream commit e3c4eb242585dcd77be1a867391b7c25fd47ce52; opened 2026-10-22 | Both `skill/` and `skills/` under every configured directory are scanned recursively, and `**` also matches zero segments, so a `SKILL.md` directly in either dir loads; identity is the frontmatter name, not the directory name | mined | 2026-10-22 | on-release | corpus/lessons/round-48.md |
| S017 | agentskills/agentskills — skills-ref reference validator v0.1.0 — https://github.com/agentskills/agentskills/tree/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref | code | A | What the open spec's own reference validator enforces for SKILL.md frontmatter (name, description, compatibility, unknown fields) | `skills-ref/src/skills_ref/validator.py:10-113` and `parser.py:36-73` at upstream commit 69ef37e9424c0a7ea9dd2293b559e43ec8176379 (main tip, 2026-08-09); `pyproject.toml` version 0.1.0, `strictyaml>=1.7.3`; opened 2026-10-22 | The spec's own validator has no description character rule at all (non-empty plus a 1024-character cap) and tests the name charset with the Unicode-aware `str.isalnum()` after NFKC folding, so it accepts what an ASCII-only regex rejects; its README marks the library demonstration-only | mined | 2026-10-22 | on-commit | corpus/knowledge/frontmatter-rule-authorities-round48.md |
| S018 | Agent Skills — Specification — https://agentskills.io/specification | spec | A | SKILL.md frontmatter field rules, with the page's own headings and the pinned file that renders them | § Frontmatter table, § `name` field, § `description` field, § Progressive disclosure; live page fetched as https://agentskills.io/specification.md (200, 7608 B, sha256 `9a67de89…`) on 2026-10-22, byte-identical to the round-47 fetch; the same rule text in the pinned source `docs/specification.mdx` at upstream commit 69ef37e9 (lines 27, 61-65, 94, 224) | supersedes S001 — the page has no "Skill metadata table" heading, so S001's anchor named a heading that does not exist; the name rule is stated twice in different words ("unicode lowercase alphanumeric" in § `name` field versus "Lowercase letters, numbers, and hyphens only" in the Frontmatter table) and S001's teach cell drops the consecutive-hyphen rule | mined | 2026-10-22 | 90d | SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md, corpus/knowledge/sibling-overlap-census-round49.md |
| S019 | Claude Docs — Agent Skills best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | docs | A | Anthropic's authoring rules for name and description | § Skill structure field list, § Writing effective descriptions, § Progressive disclosure patterns; fetched as .../best-practices.md (200, 42169 B, sha256 `f0a5d61b…`) on 2026-10-22; the round-47 fetch was 42028 B, sha256 `727f3fa1…` — editorial drift only, the rule lines are unchanged | supersedes S003 — the 500-line body rule is not Anthropic-only: the open spec states it too (S018 § Progressive disclosure); Anthropic-only are the no-XML-tags rule on both `name` and `description`, the reserved words "anthropic" and "claude", and the third-person description rule | mined | 2026-10-22 | 90d | SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md |
| S020 | kotoba own work — verifiers/verify_skill_checklist.py — `--self-test` exit 0 and `--json` exit 0 run 2026-10-22 at lane tip 75f671b | own-work | A | The lane's executed-box gate and what its frontmatter XML-tag check executes | `--self-test` final line "0 failure(s) over 1845 assertions"; `--json` exit 0, 11 PASS / 0 FAIL, 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted); `trigger.no_xml_tag` at `verify_skill_checklist.py:404,409,1294`; seat runs `.ufo/waves/round-48/build/C2LaneCheckerRun.md` | supersedes S010 — the S010 counts (1597 assertions, --json exit 1 9/1) and its "no XML-tag rule" clause are stale since round 47; the check is lexical over the unparsed scalar text: it misses an alias-hidden tag and non-tag brackets that Anthropic's packager refuses, and it fails a single-quoted escape text the packager accepts | mined | 2026-10-22 | on-commit | corpus/knowledge/frontmatter-rule-authorities-round48.md |
| S021 | OpenAI — Build skills (ChatGPT and Codex) — https://learn.chatgpt.com/docs/build-skills | docs | A | Documented Codex and ChatGPT skill-list budget and implicit invocation (vendor documentation, not a measurement of omp or opencode) | page intro md:37-40 (budget, shortening, may omit skills); md:43-44 override; § How ChatGPT and Codex use skills md:91, implicit-invocation bullet md:98-99; revision = build-skills.md sha256 `ed6e324f…` (11,035 B, 232 lines), fetched 2026-10-22T08:13:33Z, byte-identical to the round-47 fetch while the HTML Last-Modified moved | supersedes S013 — by default Codex's initial skill list uses at most 2% of the context window, or 8,000 characters when the window is unknown, may omit skills and shortens descriptions first; `skills.max_context_tokens` overrides it (up to 10,000 tokens); implicit invocation is stated for ChatGPT or Codex and keys on the description | mined | 2026-10-22 | 90d | corpus/knowledge/frontmatter-rule-authorities-round48.md |
| S022 | Claude Code — Extend Claude with skills — https://code.claude.com/docs/en/skills | docs | A | How Claude Code decides which of several available skills to use (the `description`'s role) and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode) | § Frontmatter reference, `description` row (`skills.md:389`); § Create your first skill (`skills.md:114`); § Resolve skills that share a name (`skills.md:196-198`); § Troubleshooting → § Skill triggers too often (`skills.md:1190-1195`); fetched as https://code.claude.com/docs/en/skills.md (200, 111557 B, sha256 `cdfcb0df…`) on 2026-10-22T09:41:02Z, byte-identical to the round-48 fetch of the same route; the HTML route (200, 1233129 B, sha256 `10219534…`) serves the same prose and did not redirect | The `description` is the field Claude uses to decide whether a skill applies (with `when_to_use` appended in the listing; names are always listed, and under a 1% context budget the least-used skills' descriptions are dropped first, `skills.md:1207-1213` — listing priority, not a tie-break) — and the page states no arbitration rule for overlapping descriptions (sweeps: `arbitrat`, `tie-?break`, `ambigu`, `overlap` → 0 each); a name clash is settled by origin (enterprise over personal over project), and a skill that fires where it should not is fixed by making the description more specific or by setting `disable-model-invocation: true` | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md |
| S023 | Claude Docs — Agent Skills overview — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | docs | A | Anthropic's documented progressive-disclosure loading model for Claude: how a skill's `name` and `description` enter the system prompt at startup, and how the description decides whether the skill applies (vendor documentation, not a measurement of omp or opencode) | § Level 1: Metadata (always loaded) (`overview.md:48`, text at :59), § Level 2: Instructions (loaded when triggered) (`overview.md:82`), § How Skills work level table (`overview.md:106`); fetched as .../agent-skills/overview.md (200, 21840 B, sha256 `7913d455…`) on 2026-10-22T09:38:50Z, byte-identical to the round-48 fetch of the same route; the HTML route (200, 557288 B, sha256 `0c1d8f68…`) carries the same sentences inside a client app shell | Name and description are the only skill text in context before a trigger: the metadata is loaded at startup into the system prompt and the description is what the request is matched against, so the description decides whether a skill applies; the page states no rule for choosing between overlapping descriptions | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md |

## Paths

- **Authoring a SKILL.md that loads everywhere — S018 → S017 → S008 → S019 → S012 → S002 → S011.**
  The normative field contract first (S018 supersedes S001's anchor and teach); its own reference
  validator, which reads the name charset as Unicode; the YAML mechanics that make a plain-scalar
  description break; Anthropic's rules (S019 supersedes S003: no XML tags, reserved words and third
  person are Anthropic-only, while the 500-line body rule is shared with the spec); the packager that
  bans any angle bracket in the parsed value; then the lenient client contract that explains why
  invalid files still load; the rejected tutorial last. Round 48: the earlier sentence here said the
  spec does not carry the 500-line rule — it does (S018 § Progressive disclosure). Per-authority table:
  `corpus/knowledge/frontmatter-rule-authorities-round48.md`.
- **Why the comparator distrusts its input JSON — S006 → S007 → S009 → S010.**
  The RFC says duplicate names SHOULD be unique and receiver behavior is
  unpredictable; Python's default is one of those unpredictable behaviors
  (last-wins). The two own-work rows are where those facts land: the comparator
  now parses every published channel and detects duplicate members, and the
  checklist gate demonstrates the lane's fail-closed fixture pattern.

## Search log

- **2026-10-19 — leads sweep for round-46 rows.** Question: which opened sources
  teach the lane's domain and ground this round's claims (scope-file resolution,
  duplicate JSON members, scope-out metadata trust). Where: `kotoba-art.md` §3
  (30-row registry draft) plus § "Leads (unopened)" in the same dossier, against
  `.ufo/round-46/claims.json` C1–C3. Identified 30 rows + ~40 lead bullets;
  screened 30 rows; included 8 external rows (S001–S008) plus 1 rejected row
  (S011) re-opened today; excluded ~21 rows for redundancy (papers whose point
  the spec rows carry for this lane's use), out-of-scope security/injection
  items (adjacent to kasegi), and sources not re-opened today (rule 1 forbids
  copying a row unopened). Stop rationale: the contract asks 8–14 honest rows;
  a short registry of opened rows beats a long one (contract rule 4).
- **2026-10-19 — own-work gate selection.** Question: which re-runnable lane
  gates qualify as tier-A own-work rows. Where: `verifiers/` directory, run
  directly from the lane root. Identified 2 candidate instruments
  (`compare_harness_independent.py`, `verify_skill_checklist.py`); screened 2;
  included 2; excluded 0. Both self-tests run today, exit 0. Stop rationale:
  those are the two instruments this round's claims and the frontmatter leads
  rest on.
- **2026-10-19 — rejected-row verification.** Question: does the Agentman
  tutorial still contradict the client contract. Where: agentman.ai page plus
  cross-check greps of the spec (`angle bracket` → 0 hits) and client guide.
  Identified 1 candidate; screened 1; included 1 as `rejected`; excluded 0.
  Stop rationale: contract requires at least one rejected row and a rejection
  is evidence of taste.

- **2026-10-21 — round-47 sources sweep (C1, C2 grounding).** Question: which opened
  sources ground the description XML-tag rule beyond S003, how the skill-routing hosts
  load descriptions, and which bytes the substrate re-pin measures. Where: the round-46
  `## Leads (unopened)` list (anthropics/skills, Anthropic Engineering, learn.chatgpt.com
  Build skills) plus the opencode skills docs and Anthropic platform skills pages, and the
  frozen snapshot directory. Identified 7 candidates; screened 7; included 4 (S012–S015);
  excluded 3 — the anthropics/skills `spec/agent-skills-spec.md` (a 3-line pointer, no
  rule content), the opencode skills docs (documents keys 1.19.3 lacks; tier B at best,
  no claim rests on it), the Anthropic platform skills guide (states the rule S003
  already carries, no upload rejection). Re-opened S001–S005 and S008 (no status change;
  S001 anchor-label defect recorded in `lessons/round-47.md` § Gate). Stop rationale:
  every round-47 claim now rests on an opened row; further leads serve no claim.

- **2026-10-22 — round-48 sources sweep (C1 and C2 grounding).** Question: which authority
  imposes which SKILL.md frontmatter rule, and which directories opencode 1.19.3 scans for skills.
  Where: the agentskills.io spec and client guide, `agentskills/agentskills`, Anthropic's best-practices
  and overview pages, `anthropics/skills` at `dbd4588` and `main`, OpenAI's build-skills page,
  opencode's docs and its v1.19.3 source, Claude Code's skills page, the installed opencode and omp
  binaries. Identified 11; screened 11; included 6 (S016–S021); excluded 5 — opencode docs
  (unversioned, ahead of the 1.19.3 binary), Claude Code skills page and the Skills API guide (rules
  recorded in `.ufo/waves/round-48/build/C2ClaudeDocs.md`, no claim rests on them yet), the omp binary
  (no claim rests on it), `anthropics/skills` `main` (byte-identical to the S012 pin). Stop rationale:
  every round-48 claim rests on an opened row. Full record: `corpus/lessons/round-48.md` § Gate.

## Leads (unopened)

- anthropics/skills — skill-creator/SKILL.md (executable trigger-optimization loop: 20 queries, 3 runs, 60/40 held-out split).
- Claude blog — Improving skill-creator: Test, measure, and refine Agent Skills.
- developers.openai.com — Testing Agent Skills Systematically with Evals (should_trigger CSV protocol).
- SkillsBench (arXiv 2602.12670) — paired with/without-skill efficacy; cite v1 for the self-generated condition.
- SkillRouter (arXiv 2603.22455) — metadata-only routing loses 37–44 points at ~80K skills.
- ACES (arXiv 2608.20614) — Skill Lift via paired live trials; scans vs LLM-judge correlate at ρ 0.14.
- Self-evolving skills study (arXiv 2608.02636) — sparse validation-filtered search; all 11 selections used failure feedback.
- Vercel — AGENTS.md outperforms skills in our agent evals (56% non-invocation; compressed index at 100%).
- arXiv 2602.11988 — context files: no general gain, +20% inference cost.
- arXiv 2606.20512 — probe-and-refine guidance tuning: 33.0% vs 28.3% vs 25.5%.
- Anthropic Engineering — Effective context engineering for AI agents.
- Chroma — Context Rot technical report.
- ACE (arXiv 2510.04618), GEPA (arXiv 2507.19457), dspy.GEPA docs — reflective optimizers and delta playbooks.
- OpenAI — IH-Challenge, Model Spec 2026-08-18, ManyIH (arXiv 2604.09443) — instruction-hierarchy authority models.
- Skill-injection evidence (arXiv 2510.26328, 2601.10338, 2510.09023), Meta Rule of Two — adjacent to kasegi; report, do not absorb.
- Full unopened lead lists in `.tower` fleet-ledger `kaika-w1/kotoba-art.md` § "Leads (unopened)" (skill routing, skill evaluation, self-evolution, skill security, context files, injection architecture, vendor code pins).
