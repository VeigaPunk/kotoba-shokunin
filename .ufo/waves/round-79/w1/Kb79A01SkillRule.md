Seat: Kb79A01SkillRule — C2 author-facing deliverables, draft set 1 (round 79, wave 1).

Scope given: draft (1) the SKILL.md rule line(s), (2) the Gate-registry row for `verifiers/check_allowed_tools.py`,
(3) the `PROVINCE.md` `## Core` bullet, (4) the `corpus/README.md` coverage-map row; verify the Claude Code and
Factory statements myself; state the SKILL.md line-budget arithmetic; name the gates that read the sections I
touch and which of them count the lines I add. Drafts only — the L1 integrates after the wave.

All four paste-ready blocks are in `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A01SkillRule.md`
(§1–§4), with placement, rationale and the clause→source table. My own fetch evidence is in
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A01SkillRule-fetch-receipt.txt`.

## 1. What I read, and how

Read from the lane (absolute): `SKILL.md` (`grep -c '^## '` → 12 (`## ` headings at lines 60, 153, 158, 195, 218, 309, 355,
389, 413, 436, 445, 514); `wc -l` → 590), `plans/round-79.md` (whole), `corpus/knowledge/spec-skill-creation-craft-round74.md`
(head: source lines, `verified-at:`, `recheck:`, the per-page rule table it feeds in `SKILL.md` § Compression rules),
`corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (head + per-vendor map), `PROVINCE.md` § Core (20 bullets),
`corpus/README.md` coverage map (header line 5 + rows 142–146), and the gate sources named in §5.

Own fetches (2026-10-27, `curl -sSL -A 'Mozilla/5.0' --max-time 60 -o <n>.page -w '%{http_code}' <url>`; curl rc = 0 on
every call — without `-f`, curl reports 0 even for 404, so the HTTP code is the datum):

| row | URL | HTTP | bytes | sha256 | `allowed-tools` occurrences |
|---|---|---:|---:|---|---:|
| S226 | `agentskills.io/specification.md` | 200 | 7 608 | `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` | 4 |
| S227 | `code.claude.com/docs/en/skills.md` | 200 | 117 962 | `31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9` | 23 |
| S228 | `docs.factory.ai/cli/configuration/skills` | 200 | 341 235 | `81457fbf081aceaa5b90c50a8d7685450dc8801229f9a9202e40acde8fa201fa` | 21 |
| S229 (`/.md` form) | `learn.microsoft.com/en-us/agent-framework/agents/skills.md` | **404** | 17 969 | `a460fa575ff2f538af34e8e9ad5481a14595bef250f8a4745eeb255ccb9a8115` | 0 (error page) |
| S229 (plain path) | `learn.microsoft.com/en-us/agent-framework/agents/skills` | 200 | 157 339 | `34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2` | 1 |
| S230 | `raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md` | 200 | 4 793 | `5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5` | 1 |
| S231 | `raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md` | 200 | 77 634 | `fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0` | 1 |

The Claude and Factory checks the ticket asked for, verbatim from those bytes (my fetch's line numbers):

- Claude Code, `skills.md:404`: "Tools Claude can use without asking permission during the turn that invokes this
  skill. The grant clears when you send your next message. Accepts a space- or comma-separated string, or a YAML list."
  - `:617`: "It does not restrict which tools are available: every tool remains callable"
  - `:643` (under `allowManagedPermissionRulesOnly`): "Claude Code ignores `allowed-tools` in project and personal
    skills" — "requires Claude Code v2.1.282 or later" on the line above it.
  - `:632`/`:405`: `disallowed-tools` — "Tools removed from Claude's available pool while this skill is active."
- Factory, tag-stripped body: "Declares the tools the skill is designed to use. It is metadata for review,
  packaging, and UI display; it does not add tools or sandbox standard skill invocation." Also: "Droid stores it as
  skill metadata and shows it in skill surfaces, but standard skill invocation is not a runtime sandbox." and "Do
  not rely on allowed-tools as a security boundary for skills. To enforce tool access, use a custom droid with a
  tool policy or run the workflow in a restricted subagent."
- Spec `:35`/`:175`: "Space-separated string of pre-approved tools the skill may use. (Experimental)" /
  "Experimental. Support for this field may vary between agent implementations".
- MSAF: "Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent
  implementations." pi `:78`: "| `allowed-tools` | Experimental pre-approved tool list |".
- Vibe `README.md:725-728`: the `~/.vibe/skills/code-review/SKILL.md` example writes `allowed-tools:` then
  `- read`, `- grep`, `- ask_user_question`; the bullets that follow explain `user-invocable` and
  `disable-model-invocation` only.

## 2. The four drafts (summary; exact blocks in the build file)

1. **SKILL.md rule line** — one physical line (999 chars), inserted after the `Portability floor` paragraph that
   ends at `SKILL.md:162`, before `### Description thresholds by client` (`:164`), with one blank line above it.
   Section choice: `## Frontmatter craft — the trigger surface`, because the field is frontmatter, that section is
   the only home of field-level rules and the two per-client field tables, and the adjacent paragraph is the exact
   precedent (a prose portability rule that names its authorities and hands depth to an entry). Content: what the
   field means on all six surfaces (Open specification, Claude Code, Factory, Microsoft Agent Framework, pi, Mistral
   Vibe), then the decision — write the spec's space-separated string form, never rely on the field for restriction
   (a deny rule, a tool policy or `disallowed-tools` is where restriction lives), and state what the skill needs in
   the body. It names all six so the line carries the entry path **and** the surface names on one physical line
   (plan §C2 conjunct (g) reads "one rule line citing the entry path and naming ≥3 surfaces").
2. **Gate-registry row** — eight cells, `kind` = `gate`, entry command carries the script path, verdict map
   `0=clean, 1=failed, 2=could-not-evaluate`, `--self-test`, pinned values `in-file SELF_SHA;
   .ufo/waves/round-79/snapshots/MANIFEST.sha256`, write scope "none (reads `git show <rev>:<path>`; a `--self-test`
   writes isolated fixture repos under `$TMPDIR`, removed)", owner `kotoba`.
3. **PROVINCE.md `## Core` bullet** — appended after the round-74 sibling bullet (`PROVINCE.md:33`), before
   `## Frontier` (`:34`); two sentences: the documentary per-surface finding with "(S226–S231; documentary evidence,
   no client run)", then "Acted on in `SKILL.md` § Frontmatter craft and counted by
   `verifiers/check_allowed_tools.py --rev <rev>`."
4. **corpus/README.md coverage-map row** — appended after the `Sibling census re-pin (round 74)` row (line 146),
   three cells, entry path in the map's `knowledge/…` form, counter in the `../verifiers/…` form, base figure
   `0 of 6` at `b10bcbc`, snapshots pinned in `../.ufo/waves/round-79/snapshots/MANIFEST.sha256`.

## 3. Checks I ran on my own blocks

- Registry row parsed with the real `check_gate_registry.py` helpers (`cells`, `PAIR_RE`, `FLAG_RE`, `PATH_RE`,
  imported via `importlib`): **8 cells**, `kind` = `gate`, pairs `[('0','clean'), ('1','failed'),
  ('2','could-not-evaluate')]`, self-test flag `--self-test`, one pinned path, script path present in the entry
  command, owner `kotoba`. Exit of that verification: 0.
- Rule line: 1 physical line, 999 chars, three `allowed-tools` occurrences, the entry path once, and each of the six
  frozen surface names matched **ASCII-word-bounded and case-sensitively** as the entry's first cells spell them
  (`Open specification`, `Claude Code`, `Factory`, `Microsoft Agent Framework`, `pi`, `Mistral Vibe`). I first wrote
  "the open specification" lowercase and changed it, because the round-73 counter matches its vendor tokens
  case-sensitively and the C2 counter is being built from it.
- Line budget: **590 + 2 (C1's two registry rows) + 1 (this registry row) + 2 (blank + rule line) = 595 ≤ 600**, 5
  lines of headroom. Seat S07's census (`.ufo/waves/round-79/w1/Kb79S07BudgetCensus.md`) prices the plan's "+7
  lines" at 597; the difference is mine alone — I spend 4 of the 4 permitted rule lines' worth as 1 content line +
  1 separator, so 595, and 597 remains the figure if anything else adds 2.
  - Shortenable existing lines, named not edited (no pointer lost): `SKILL.md:508`, `:511`, `:512` (registry
    verdict-map cells whose guard prose and withdrawn-claim history `verifiers/README.md` already holds — the
    section preamble cites that file), `:509` (the cn-vendor row's four-vendor enumeration, repeated in PROVINCE and
    the README row), `:193` (the skill-eval bullet's row-count/comparator detail, held by
    `corpus/knowledge/skill-eval-artefacts-round70.md`). I would not shorten line 162: every token there is a rule or
    a row id.

## 4. Gates that read the sections I touch, and which count my lines

`grep -n 'SKILL.md' verifiers/*.py | wc -l` → **433** lines across the checklist gates, the per-client counters and the
corpus gates. Restricted to my two SKILL.md changes (a paragraph in § Frontmatter craft, one row in § Gate registry):

| gate | what it reads | counts my lines? |
|---|---|---|
| `verifiers/verify_skill_checklist.py` | whole file — `trigger.line_budget` (`n = len(lines)`, `--max-lines` default 600), plus `trigger.citation_resolves`, `trigger.no_placeholder` | **Yes** — the only gate that counts them; 590 → 595 against 600 |
| `verifiers/check_gate_registry.py` | `## Gate registry` (`HEADING`), header tuple, exactly one row per lane verifier, `phantom` rows (a `verifiers/…` row with no file fails), pinned-path existence | counts the row, not lines; the row must land **with** the counter script and with the committed `MANIFEST.sha256` |
| `verifiers/check_cn_vendor_surfaces.py` | its own `## Instruction surfaces` decision row, its own registry row (`registry_home_ok`), `PROVINCE.md` bullets | no — rows/tokens in the sections it names only |
| `verifiers/check_spec_craft.py` | `§ Compression rules` rows citing the round-74 entry | no (different section) |
| `verifiers/check_author_rules.py` | four rendered boxes in `§ Trigger-fidelity checklist` | no (different section) |
| `verifiers/check_agentdef_boxes.py`, `check_alwayson_boxes.py` | their own checklist sections | no (different sections) |
| `verifiers/check_assertion_floors.py` | `verifiers/*.py` instruments via `verifiers/floors-registry.json` | no — floors are per verifier file |
| `verifiers/check_tip_battery.py` | six BATTERY scripts, `INSTRUMENT_PINS`, and a no-deletion guard naming `SKILL.md` | no — `LINE_CAP = 40` applies to the instrument scripts; `SKILL.md` appears only in the deletion guard |

## 5. Cross-checks against sibling seats (read, not assumed)

- `w1/Kb79S07BudgetCensus.md` — base `SKILL.md` 78 647 B / 590 lines, longest line 1 095 chars. Same line figure as
  mine; my rule line at 999 chars sits under the existing longest line, so it introduces no new maximum.
- `w1/Kb79R02ClaudeRow.md` — same three sentences I read (L404 grant + forms, L617 non-restriction, L643
  `allowManagedPermissionRulesOnly`), plus L636 (`strictPluginOnlyCustomization` hooks loses the pre-approval) and the
  v2.1.282 floor. The row's `pre-approves` label and its "granted for one turn; unlisted tools still permission-gated"
  reading agree with my line's "leaves every tool callable".
- `w1/Kb79R03FactoryRow.md` — reports `does not add tools` **1 hit** in its converted snapshot; my raw-HTML fetch has
  the string twice (Next.js payload + rendered DOM carry the same sentence). Not a conflict: one statement, two
  renderings. The row also flags F2 — the 5–25-word pipe-free quote cannot carry `allowed-tools` and
  `does not add tools` together — which is a contract issue for the late-frozen counter, not for my rule line (my
  Factory clause is a paraphrase, not a quote).
- `w1/Kb79CR02C2Target.md` — argues the frozen headline measures form, not semantics, and that labels can be copied
  from the plan. My rule line does not lean on the counter's score for its semantics: each clause is a sentence I
  fetched and quoted in §1 above, and the line says "documentary evidence, no client run". If the L1 adopts the
  critic's form-level headline, the SKILL.md line is unaffected; if reviewers must confirm each label, my clause
  table is the checklist they can work from.

## 6. Findings the L1 needs

1. **S229 needs the alternate URL form, said out loud.** The `.md` route is 404 (17 969 B error page, 0 hits); the
   plain path on the same host and path prefix is 200 with the field. The C2 brief permits the second form for a
   seat whose first form returns no usable text; the row seat must record which form the snapshot is. The frozen host
   check (`learn.microsoft.com`) is satisfied either way.
2. **Registry row and counter must land in one commit.** `check_gate_registry.py` `judge()` fails a row whose Name
   path is absent from the file set (`phantom`), and `judge_row` requires the backticked pinned path to exist at the
   measured revision. So the row, `verifiers/check_allowed_tools.py` and
   `.ufo/waves/round-79/snapshots/MANIFEST.sha256` ship together.
3. **Vibe's `unstated` label is correct on my bytes** — one `allowed-tools` occurrence, in the example; the page's
   own semantics bullets are about `user-invocable` and `disable-model-invocation`. Sweep in the receipt.
4. **Rule-line risk if the C2 counter checks surface names case-sensitively.** It very likely will, since
   `check_cn_vendor_surfaces.py` matches vendor tokens with a boundary regex and no case folding. I normalised all
   six names to the entry's frozen first-cell forms; if the L1 spells a surface differently in the entry
   (`Open specification` vs `open specification`), the SKILL.md line and the entry must agree.
5. **Line-budget interdependency.** C1's two registry rows plus mine plus my 2 insertion lines put the file at 595.
   Any further SKILL.md addition this round beyond 5 lines trips `trigger.line_budget`, and the shorten-candidates in
   §3 are the budget back.

## 7. Limits

- Drafts only: I did not edit `SKILL.md`, `PROVINCE.md` or `corpus/README.md`; no lane file outside
  `.ufo/waves/round-79/` was written; no git/jj mutation anywhere (read-only `git show`/`rev-parse`/`status` only).
- I did not run `verifiers/check_allowed_tools.py` (not built yet) and scored no data on it.
- I pinned no snapshots — the row seats own `.ufo/waves/round-79/snapshots/`; my fetches are transient, and the
  receipt's sha256 values are the durable record after my scratch dir is removed.
- I ran no lane gate, so nothing here is a gate result; the numbers are `wc -l` / `grep -c` over committed bytes, my
  curl results, and one `importlib` parse of my own row with `check_gate_registry.py`'s helpers.
- The lane `HEAD` moved while I read (`daa3a09` → `d9d01c2` → `60ba11f`); SKILL.md measured 590 lines, 0
  `allowed-tools`, 60 registry rows at each re-read, and the three target files were clean.
- No client was installed, loaded, routed or refused: every semantic statement above is documentary.
- Scratch: `/fast/scratch/hyaku/kotoba-r79/Kb79A01SkillRule` removed before yield (`rm -rf`); nothing was left there.
- No tools installed or upgraded; nothing ran outside the tool calls listed.

VERDICT: Four C2 author-facing drafts are ready to paste — one 999-char SKILL.md rule line in § Frontmatter craft naming all six surfaces and the non-restriction decision, an eight-cell `gate` registry row, a two-sentence PROVINCE `## Core` bullet and a README coverage row — with the line budget at 595 of 600 and the Claude, Factory formula and S229 URL-form facts verified against my own fetches.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A01SkillRule.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A01SkillRule-fetch-receipt.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79A01SkillRule.md
