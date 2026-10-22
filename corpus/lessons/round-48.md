# Lessons — round 48

Round: 48 (hyaku campaign, attempt 2; attempt 1 was failed at T0 and is not resumed). Lane base
`75f671b109d8eddd0d64c1429bd6379fe577175a`. Claims: C1 freshness — the knowledge entry
`corpus/knowledge/frontmatter-rule-authorities-round48.md`, which repairs routed item 3 of
`corpus/lessons/round-47-verifier-spotcheck.md`; C2 depth — configured-root enumeration in
`verifiers/verify_harness_independent.py` (landed `d1ae45830235c38320b31032b57a8323cbf90b17`).
Plan: `plans/round-48.md`. Wave evidence: `.ufo/waves/round-48/build/`.

## Mistakes

`captured-by` names the criterion or instrument that should have caught the class;
`none → Qnn` means nothing caught it and this round adds the criterion.

|class|evidence pointer (command → output)|captured-by|fix|
|---|---|---|---|
| M24 Rule credited to the wrong authority, and a lexical approximation described as a vendor rule | `git show 75f671b:corpus/SOURCES.md \| grep -c 'an Anthropic-only rule the open spec lacks'` → 1 (S003 teach), while `curl -fsSL https://agentskills.io/specification.md \| grep -c 'under 500 lines'` → 1 (the spec states the rule); `git show 75f671b:SKILL.md \| grep -c 'is stricter and refuses any'` → 1, while the lane check FAILs a single-quoted `'\u003cb\u003e'` that the packager accepts and PASSes an alias-hidden `<b>` the packager refuses (`.ufo/waves/round-48/build/C2LaneCheckerRun.md`, 10 fixtures) | none → Q20 | Superseding rows S018 (S001), S019 (S003), S020 (S010); `SKILL.md` § Portability floor rewritten to name the parsed rule and point to the entry, which carries the run counterexamples. Shown able to fail: Q20 applied to the base sentence (`git show 75f671b:SKILL.md \| sed -n 151p`) fails — it names no parsed rule and links no run counterexample (`grep -c 'frontmatter-rule-authorities'` on that line → 0); on the landed line → 1. |
| M25 Coverage sweep searched source names, not rule content | The plan's novelty sweep `grep -rn 'agentskills\|skills-ref' corpus/knowledge SKILL.md` → 0 hits in `SKILL.md`, yet `grep -n '1024' SKILL.md` → line 151 already stated the per-authority rules (`.ufo/waves/round-48/build/C2UncoveredSweep.md`) | Q14 (a negative claim carries its sweep) — satisfied in form, too narrow in content | The entry's novelty claim now rests on both sweeps (source names and rule terms), and `SKILL.md:151` points to the entry so the fact keeps one home. Shown able to fail: the source-name sweep returns 0 on `SKILL.md`, the content sweep returns 1 — the narrow sweep would have certified a duplicate. |
| M26 A repair claim named after the routed row, not the routed cause | The first plan framed configured-root enumeration as "repair routed defect 1, configured-root half"; `C1ClaimCritic.md` and `C1JoinDefinitionHistory.md` show the round-47 join drop is the producer's `customize-opencode` byte probe (`verify_harness_claims.py:477-479`), which the change does not touch; on this host both roots are absent and the row reads 10 before and after | none → Q21 | Claims re-ordered before any landing (`plans/round-48.md` re-ordering note); the configured-root claim is scored improved-bounded and says it does not resolve defect 1. Shown able to fail: Q21 asks for the cause's measurement; the producer reads 11 and the instrument 10 on the live row at both base and landing, so a "defect 1 repaired" claim fails it. |
| M27 Instrument self-hash read through process substitution | First landed ruler run used `python3 -B <(git show …ruler.py)`; its receipt recorded `ruler_sha256` `e3b0c442…` (the hash of empty input) instead of `01af33a6…` | none (the ruler hashes `__file__`, which a pipe empties) | Re-run from the committed path after `git show <rev>:.ufo/round-48/tools/config-root-ruler.py \| sha256sum` matched the working file (`01af33a6…`); the retained receipt `.ufo/round-48/verification/after-configured-root.json` carries `ruler_sha256` `01af33a6…`. Shown able to fail: the discarded receipt's `ruler_sha256` differs from the committed ruler's hash. |
| M28 Hash match read as custody (round 47, routed item 4) | Round 47 deleted and then rebuilt its shared scratch snapshot; four sha256 matches against committed receipts were offered as recovery (fleet `.ufo/reports/round-47/kotoba.md`, "reconstructed, not uninterrupted custody"). Demonstration this round (`.ufo/waves/round-48/build/FrQualityCriteria.md` F3): a copy of `.ufo/round-48/verification/before-configured-root.json` has the same sha256 `8bec447a…` but a different inode; the named round-47 scratch commits (`git cat-file -e b1b48d1` and five more) exit 128 | none → Q22 | Q22 states what a hash match proves (byte identity) and what it does not (custody, inode/mtime, historical-object recovery). Shown able to fail: the copy passes a hash check yet fails an inode check, so a custody claim resting on the hash alone fails Q22. No cleanup or reconstruction ran this round. |

## Gate

**Rows written this round** (each opened on 2026-10-22 by a wave-1 seat; the seat report holds
the full fetch record). No existing row's `status`, `recheck` or `used-by` changed; S001, S003,
S010 and S013 stay as written (contract rule 2) and are superseded by new rows.

| row | URL | accessed (UTC) | quote, at most 25 words (location) |
|---|---|---|---|
| S016 | https://github.com/anomalyco/opencode/blob/v1.19.3/packages/opencode/src/skill/index.ts (tag v1.19.3 = `e3c4eb24`) | 2026-10-22T08:13:22Z | `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"` (`packages/opencode/src/skill/index.ts:24`) — seat `C1UpstreamLoaderSource.md` |
| S017 | https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref/src/skills_ref/validator.py | 2026-10-22T08:16Z | `if not all(c.isalnum() or c == "-" for c in name):` (`validator.py:54`) — seats `C2SkillsRefSource.md`, `FrSourcesRowsScribe.md` |
| S018 | https://agentskills.io/specification | 2026-10-22T08:14:16Z | "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)" (§ `name` field, `specification.md:64`) |
| S019 | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | 2026-10-22T08:16Z | "Cannot contain XML tags" (§ Skill structure, `best-practices.md:155` and `:162`) — seat `C2ClaudeDocs.md` |
| S020 | own work: `python3 -B verifiers/verify_skill_checklist.py --self-test` at `75f671b` | 2026-10-22 | "0 failure(s) over 1845 assertions" (final line, exit 0) — seats `FrSourceDefects.md`, `C2LaneCheckerRun.md` |
| S021 | https://learn.chatgpt.com/docs/build-skills | 2026-10-22T08:13:33Z | "By default, this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown." (md:37-39) — seat `FrSourceDefects.md` |

Status changes logged old→new: S016–S021 created as `mined` (used-by the entry, and the lesson
for S016). No other row moved.

Sweeps behind the negative claims (contract rule 5): spec `grep -ci 'xml'` → 0 (exit 1),
`grep -ci 'third person'` → 0 (exit 1); skills-ref `validator.py` `grep -c '<'` → 0 (exit 1) and
repository-wide `git grep -c -i angle` → 0 (exit 1) (`FrSourcesRowsScribe.md`, `C2SkillsRefSource.md`).

**Search log (round 48).** Question: which authority imposes which SKILL.md frontmatter rule, and
which directories opencode 1.19.3 scans for skills. Where: the agentskills.io spec and client
guide, the `agentskills/agentskills` repository, Anthropic's best-practices and overview pages,
`anthropics/skills` at `dbd4588` and `main`, OpenAI's build-skills page, opencode's docs and its
v1.19.3 source, Claude Code's skills page, the installed opencode and omp binaries. Identified 11;
included 6 rows (S016–S021); excluded 5 as rows this round: opencode docs (unversioned; documents
rules 1.19.3 does not enforce), Claude Code skills page and the Skills API guide (opened, rules
recorded in `C2ClaudeDocs.md`; no claim rests on them yet), the installed omp binary
(`C2OmpLoaderRules.md`; omp 18.12.6 enforces only a path-separator check on normal discovery; no
claim rests on it), `anthropics/skills` `main` (byte-identical to the S012 pin, no new row needed).
Stop rationale: every claim of this round rests on an opened row.

## Routed items from the round-47 spot-check

| item | disposition this round |
|---|---|
| 1 join definition and carrier | Not resolved. C2 closes the configured-root input gap in the same row; the built-in marker disagreement stays routed (M26). Original 21/24 and 20/24 evidence untouched. |
| 2 source anchors, README 24/24, erratum horizon | S018–S021 supersede S001/S003/S010/S013 (old cells kept). README 24/24 lines qualified in `corpus/README.md`; erratum horizon 2315 versus 2343+ LOG lines recorded there. |
| 3 parsed vendor rule versus lexical mirror | Repaired by C1: the entry tables both rules and runs the YAML-alias, Unicode and escaped-value counterexamples. |
| 4 absence and reconstruction facts | Lesson-backed criterion Q22 (M28). No cleanup or reconstruction this round. Attempt 1's private-tree pointers are named as not re-verifiable from the lane (`FrAttempt1Audit.md`). |
| 5 prospective closure metadata | No new criterion: the observed class (an unindexed closure file, round-47 M21) is already caught by both corpus instruments, and this round's two new corpus files were indexed with the owning baseline re-recorded (61 → 63). No frozen input, receipt or producer target was edited; attempt 1's committed instrument, oracle and before receipt are reused byte-identical (sha256 checked). |

## Falsify-wave corrections (wave 2, lane-dispatched — not a non-author spot-check)

- `A28QualityRows`: Q20 bound only the approximation half of M24 and missed `PROVINCE.md`,
  `corpus/README.md` and check detail strings → **Q23 supersedes Q20** (Q20 stays as the audit
  trail). The check's FAIL detail string (`verifiers/verify_skill_checklist.py`, `check_no_xml_tag`)
  and `PROVINCE.md` Core still called the packager "stricter" or said the check executes S003's rule
  → both corrected. Q21's `grounded in` cell names M26 by a shorter label than the M26 row's class
  text; the row is not rewritten (append-only), this line records the mismatch.
- `A09ClaimSizingC1`: the S001 and S003 `used-by` cells still named `SKILL.md`, which cites S018 and
  S019 since `887b6af`. Changed in place (contract rule 2), logged old→new: S001 `SKILL.md` →
  `corpus/lessons/round-46.md`; S003 `SKILL.md` → `corpus/lessons/round-46.md, corpus/lessons/round-47.md`.
  The same seat rated C1's axis label a medium defect (34 → 35 is the expansion observable); the
  declared target is not changed after landing — the report carries the disagreement.
- `FrQualityCriteria`: routed item 4 gets Q22 (M28). Its draft Q23-for-item-5 was not taken (see the
  routed-items table).
- `A24UnreadableRoot`: with `--oc-config/skills` unreadable, the round-48 instrument exits 2 (caught
  `SUBSTRATE` permission error) where base exited 0 because it never read that root. Recorded as an
  open behavior question in `SCORECARD.md` (next round), not fixed this round.
- `A10FillerHunt`: about 12 of the entry's 60 cells repeat facts already held at base; six
  inter-authority disagreements are new (0 hits in `SKILL.md` at base). Corrected in the entry: the
  spec table citation (spec.md:27 → :30), the false "gives maxima only", the `source:` line now
  carries URLs and the sections the cells cite, and the PyPI-versus-pinned skills-ref byte difference
  is disclosed. S012 `used-by` changed in place, logged old→new: `SKILL.md` →
  `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md`. Not corrected this round:
  several counts in the entry carry no command and date (Q13) and four negative cells carry no
  sweep (Q14) — listed in `.ufo/waves/round-48/falsify/A10FillerHunt.md`; open for the next round.
