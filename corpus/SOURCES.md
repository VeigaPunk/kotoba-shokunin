# SOURCES — where kotoba learns

`corpus/knowledge/` holds admitted facts; this file holds the places they come
from — what each teaches, how far to trust it for which scope, and when to look
again. Contract: fleet `SOURCES-CONTRACT-v1.md` (2026-10-19). A row exists only
for a source the row's author opened this round; access evidence lives in
`.ufo/round-46/evidence/w2/sources/fetch-log.json` and the round lesson's
`## Gate`.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Agent Skills — Specification — https://agentskills.io/specification | spec | A | SKILL.md frontmatter format and file-structure rules | § Skill metadata table, § Progressive disclosure; live page opened 2026-10-19 | Name is 1-64 lowercase-hyphen chars matching its directory; description 1-1024 chars saying what and when; SKILL.md under 500 lines with detail moved to reference files | mined | 2026-10-19 | on-release | SKILL.md |
| S002 | Agent Skills — How to add skills support to your agent — https://agentskills.io/client-implementation/adding-skills-support | docs | A | Client-side loading and validation policy for SKILL.md | § Handling malformed YAML, § Lenient validation; live page opened 2026-10-19 | Unquoted values containing colons are technically invalid YAML; lenient clients warn and load anyway on name mismatch, so a strict local gate is stricter than the client contract | mined | 2026-10-19 | 90d | SKILL.md |
| S003 | Claude Docs — Agent Skills best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | docs | A | Anthropic authoring rules for name and description | § Skill structure field list; live page opened 2026-10-19 | The description cannot contain XML tags, must be third person, and states what the skill does and when; body under 500 lines; an Anthropic-only rule the open spec lacks | mined | 2026-10-19 | 90d | SKILL.md |
| S004 | AGENTS.md — open format site — https://agents.md/ | spec | A | Always-on context-file precedence convention | § FAQ "What if instructions conflict?"; live page opened 2026-10-19 | Conflict rule for always-on files: the closest AGENTS.md to the edited file wins and explicit user chat prompts override everything | queued | 2026-10-19 | 90d | — |
| S005 | CommonMark Spec 0.31.2 — https://spec.commonmark.org/0.31.2/ | spec | A | Fenced code block syntax the lane's box/quote extraction implements | § Fenced code blocks; version 0.31.2 | A code fence is at least three backticks or tildes preceded by up to three spaces of indentation; a backtick fence's info string may not contain a backtick | queued | 2026-10-19 | on-release | — |
| S006 | RFC 8259 — The JavaScript Object Notation (JSON) Data Interchange Format — https://www.rfc-editor.org/rfc/rfc8259.txt | spec | A | Duplicate-name semantics in JSON objects (round-46 C2 door) | §4 Objects | Object names SHOULD be unique; when they are not, receiver behavior is unpredictable — the normative basis for the comparator's duplicate-member detection | queued | 2026-10-19 | on-release | — |
| S007 | Python docs — json: JSON encoder and decoder — https://docs.python.org/3/library/json.html | docs | A | This host's actual duplicate-name decode behavior | § Standard Compliance and Interoperability | Python's decoder accepts repeated names and keeps only the last pair, so a last-wins silent read is the implementation default the comparator must not inherit uncritically | queued | 2026-10-19 | 365d | — |
| S008 | YAML Specification 1.2.2 — https://yaml.org/spec/1.2.2/ | spec | A | Plain-scalar restrictions behind the frontmatter strictness lead | §7.3.3 Plain Style | Plain scalars must never contain the colon-space or space-hash combinations, since both are ambiguous with key/value pairs and comments | mined | 2026-10-19 | on-release | SKILL.md |
| S009 | kotoba own work — verifiers/compare_harness_independent.py --self-test — run 2026-10-19, exit 0 | own-work | A | The comparator's own self-model at the round-46 landing commit | Final line "self-test: 0 failure(s) over 328 assertions"; commit 78ee57e | The join driver's channel-agreement model, including cross-channel divergence classes, is exercisable on committed fixtures without either live instrument | queued | 2026-10-19 | on-commit | — |
| S010 | kotoba own work — verifiers/verify_skill_checklist.py — --self-test exit 0 and --json exit 1 (9 PASS / 1 FAIL governance.citation_resolves at LOG.md:2111) runs 2026-10-19 | own-work | A | The lane's executed-box gate and frontmatter parse coverage | Final line "0 failure(s) over 1597 assertions"; --json "checklist.box_map_complete ... 41 boxes mapped" | All 41 prose boxes are accounted for as executed, delegated, or unexecuted under a sha256-pinned normalization; the frontmatter check is a lenient structural parse with no XML-tag rule | queued | 2026-10-19 | on-commit | — |
| S011 | Agentman — How Do You Build Your First Agent Skill? — https://agentman.ai/blog/build-your-first-agent-skill-skillmd-anatomy | community | C | SKILL.md authoring claims for beginners | Field-table paragraph and "safety note" paragraph; opened 2026-10-19 | REJECTED: claims a name/folder mismatch means the skill "will not load" where the client guide (S002) says warn and load; credits an angle-bracket ban to the agentskills.io spec which has none (0 mentions); quantitative claims cite unnamed analyses; flip: re-check if the spec gains the rule or the client guide tightens to refuse mismatched names | rejected | 2026-10-19 | 180d | — |

## Paths

- **Authoring a SKILL.md that loads everywhere — S001 → S008 → S003 → S002 → S011.**
  The normative field contract first; the YAML mechanics that make a
  plain-scalar description break; the vendor-only rules (no XML tags, third
  person, 500 lines) that the spec does not carry; then the lenient client
  contract that explains why invalid files still load; the rejected tutorial
  last — knowing the rule it gets wrong is what makes it evidence of taste.
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

## Leads (unopened)

- Anthropic Engineering — Equipping agents for the real world with Agent Skills (origin of the 3-level progressive-disclosure model).
- anthropics/skills — skill-creator/SKILL.md (executable trigger-optimization loop: 20 queries, 3 runs, 60/40 held-out split).
- Claude blog — Improving skill-creator: Test, measure, and refine Agent Skills.
- learn.chatgpt.com — Build skills (Codex router contract: 2% catalog budget, front-loaded trigger words).
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
