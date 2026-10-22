# ReplayC2Counter: C2 depth numbers, round 51 falsify

VERDICT: FAILS (bounded). The counts reproduce exactly: 0 of 7 (exit 1) at BASE, 7 of 7 (exit 0) at HEAD, 7 of 7 (exit 0) with live fetch. The seventh count, GitHub Copilot CLI (S031), rests on a per-directory lever that the entry's own text places outside its counted category and that the claim's bound ("removes one named skill") excludes. Under the entry's own exclusion rule the supportable count is 6 of 7 with the rows as they stand.

Attacks: C2 counter reruns at BASE and HEAD, live `--fetch`, `--self-test`, an independent curl check of the seven cited pages, one client hand-checked without the script (Copilot CLI), and in-memory probes of the Gate check and the key-term check.

## Setup

- Lane HEAD 59903b2637689739a5b9901956301da72d0effe1; BASE 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10.
- Private clone: `/fast/scratch/hyaku/kotoba-r51/falsify/ReplayC2Counter/lane` (`git clone`, then `git checkout -q 59903b26`). Page copies: `.../ReplayC2Counter/pages/`. The lane checkout was not written.
- Installs or upgrades: none. Tools used: git, curl, python3 (in-memory probes only), the read and grep tools.
- Leaf seat; no subagents.

## 1. Counter numbers (run in the private clone)

| # | command | UTC | result | exit |
|---|---|---|---|---|
| 1 | `python3 -B verifiers/check_overlap_levers.py --rev 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` | not timed | seven `UNBACKED: SKILL.md table absent (<client>)`; `overlap levers backed 0 of 7 clients` | 1 |
| 2 | `python3 -B verifiers/check_overlap_levers.py --rev 59903b2637689739a5b9901956301da72d0effe1` | not timed | seven `BACKED`; `overlap levers backed 7 of 7 clients` | 0 |
| 3 | `date -u; python3 -B verifiers/check_overlap_levers.py --rev 59903b26… --fetch; date -u` | start 2026-10-22T15:15:33Z, end 15:15:34Z | seven `FETCH <client>: quote found (<url>)`; `quotes found on live pages 7 of 7` | 0 |
| 4 | `python3 -B verifiers/check_overlap_levers.py --self-test` (HEAD) | not timed | `0 failures`, `22 assertions` | 0 |

- Row 1 is structural: at BASE the SKILL.md table does not exist, so all seven clients are 0 by absence.
- The denominator is pinned (counter lines 85-93), and it is not read from the revision.
- Row 3 took 1.33 s of wall time. That fits live requests, and my independent run below took about one second for seven pages.

## 2. Independent live check (no script)

Command: `curl -sS -L -o <file> -w '%{http_code} %{size_download}'` on the seven `.md` URLs in the entry's recheck line, run 2026-10-22T15:18:41Z to 15:18:42Z. Quote presence was checked with the grep tool on each file.

| client | HTTP | bytes | sha256 prefix (computed / recorded) | quote on cited line |
|---|---|---|---|---|
| Copilot SDK (`skills.md`) | 200 | 35,455 | 64856ff4 / 64856ff4 | 809, verbatim |
| Copilot CLI (`cli-command-reference.md`) | 200 | 461,944 | c61997ef / c61997ef | 1300, verbatim |
| VS Code (`agent-skills.md`) | 200 | 22,871 | de5ba34f / de5ba34f | 289, verbatim |
| Claude Code (`skills.md`) | 200 | 111,557 | cdfcb0df / cdfcb0df | 886, verbatim |
| opencode (`skills.md`) | 200 | 5,365 | f10ced73 / f10ced73 | 230, verbatim |
| Gemini CLI (`skills.md`) | 200 | 5,763 | 8e1b4cbe / 8e1b4cbe | 94, verbatim |
| Codex (`build-skills.md`) | 200 | 11,035 | ed6e324f / ed6e324f | 218, verbatim |

Seven of seven quotes are verbatim on the line the entry cites, and seven of seven hashes match. The byte counts match the SOURCES rows where they are recorded (S030, S031, S024, S029, S021).

## 3. Hand-check of one client end to end: GitHub Copilot CLI (S031), no script

1. SKILL.md line 397 (table at 394-402): `| GitHub Copilot CLI | exclude the skill's directory from discovery | user or operator | removed everywhere | S031 | \`ignoredSkillsLocations\` |`
2. Entry line 21 (row S031): quote "Use the `ignoredSkillsLocations` setting to exclude specific directories (and their descendants) from discovery, regardless of which location above would otherwise surface them." (cli-command-reference.md:1300). Its lever column says "the user's settings exclude whole skill directories from discovery".
3. SOURCES.md line 44 (S031): docs, tier A, mined, used-by `corpus/knowledge/skill-overlap-levers-round51.md`. Its scope cell says "The per-skill removal levers GitHub Copilot CLI documents".
4. Lesson round-51.md: `## Gate` at line 28, `### Admitted` at line 30, S031 entry at lines 44-50 with the same quote, "22 words".
5. Page cli-command-reference.md:1300 carries the quote verbatim. The same sentence says "specific directories (and their descendants)".

Links 1 to 4 agree on the row ID and the URL. Link 5 fails the bound. The plan's re-sized statement and SKILL.md line 388 both say each lever "removes one skill" or "one named skill". This lever's documented unit is a directory and everything beneath it. The entry says so itself at Limits line 91: "The Copilot CLI row's lever works per directory, not per skill name." Finding 1 (lines 42-44) lists "outside a scope (directory or path settings, not counted here)" as a category outside the count, then puts Copilot CLI under "removed everywhere" in the same paragraph. The entry contradicts itself on whether this client is counted.

## 4. Findings

**F1 (high). Copilot CLI is counted with a lever the claim's bound excludes.** Evidence is in section 3, plus:
- Counter lines 137-141 (REVIEWED_LEVERS comment): each reviewed term was "confirmed remove one named skill". `ignoredSkillsLocations` is in that list.
- Per-name lever on the same documentation family: cli-config-dir-reference.md:461, `disabledSkills`, "Skill names to disable. Listed skills are discovered but not loaded." (fetched 2026-10-22T15:21:34Z, HTTP 200, 166,811 B, sha256 8be36090…). The reviewed list already holds "copilot skill disable" for this client (counter line 144 at HEAD), and neither that term nor `disabledSkills` is quoted. Using `disabledSkills` would need a new SOURCES row, a Gate record, and a quote that carries the key term as a code span. The key term sits in a table cell on that page, so the quote form needs a decision. That is for the L1.
- Consequence: 6 of 7 with the rows as they stand.

**F2 (medium). The counter cannot see the distinction the bound turns on.** `ALLOWED_EFFECTS` (counter lines 119-120) accepts "outside a scope", while entry Finding 1 says that category is not counted. Relabelling S031 as "outside a scope", the honest label, would still give 7 of 7. The counter reads labels as text and never checks them against the entry.

**F3 (medium). The reviewed list was extended to match landed quotes, in the same commit as the rows.** `git log -S` shows commit 34cfffb (2026-10-22 12:11:45 -0300, message "reviewed list +3 terms") added `ignoredSkillsLocations` (Copilot CLI), `disable-model-invocation: true` (Claude Code) and `/skills disable <name>` (Gemini CLI). Commit 7c81a78 (12:07:31 -0300, the counter's landing) had REVIEWED_LEVERS without them (`git show 7c81a78:verifiers/check_overlap_levers.py`, lines 142-150). Entry Limits lines 86-90 disclose this, but the list is not a pre-set judgment: it was fitted to the rows.

**F4 (medium-low). The Gate check cannot tell admitted from rejected.** Probe, in memory on my clone: `gate_ids` on a lesson whose only mention of S029 sits under `### Rejected` returns `['S021', 'S029']`. The self-test has no such mutant. Current numbers are unaffected: all seven IDs are under `### Admitted` (lesson lines 30-54).

**F5 (low-medium). The key-term check does not test that the quote states the effect.** Probe: replacing the VS Code quote with the bare code span `` `disable-model-invocation` `` still gives `(True, '')`. The real quote (vscode.md:289) is a lead-in sentence: "Use the `user-invocable` and `disable-model-invocation` frontmatter properties to control how each skill is accessed:". The effect (auto-loading "No") is in the table row at vscode.md:295, outside the quoted line. The lever is real; the quote carries the key term but not the effect.

**F6 (low). Gemini CLI effect label.** SKILL.md line 401 says "removed everywhere". gemini.md:74-76 (NOTE): "`/skills disable` and `/skills enable` default to the `user` scope. Use `--scope workspace` to manage workspace-specific settings." The entry rejected this line as a quote (lesson Rejected list, line 69 onward) and kept the label. The count is unaffected, but the label is wrong.

**F7 (low). opencode S024 is a pattern lever.** opencode.md:143 shows `"internal-*": "deny"`, and line 156 says "Patterns support wildcards: `internal-*` matches `internal-docs`, `internal-tools`, etc." One rule can remove several named skills, and the entry's Limits do not say so. Exact-name use still meets the bound. The key term `deny` is one generic word, and the counter accepts any `deny` code span in the quote.

**F8 (low). The Copilot SDK quote comes from a section the entry calls a different phenomenon.** The quote is from "Skill conflicts" (skill-sdk.md:805-810). Entry Finding 2 (lines 48-50) says that section is about "conflicting instructions after both skills load, not two descriptions matching one prompt". The "Disabling skills" section (skill-sdk.md:177-189, "Disable specific skills while keeping others active", with a per-name `disabledSkills` list) is the closer fit. The S030 source row cites it (`:177-179`), but the quote does not use it.

**F9 (propagation).** The false phrase "removes one named skill" appears in SKILL.md lines 387-388, the entry at lines 10-12 and 46, corpus/README.md:75, and the plan's bound. Any fix must change all of them.

## 5. Verdict on 0 of 7 → 7 of 7

- Numbers: **HOLDS.** The four counter runs and the live fetch reproduce exactly (exit codes in section 1). The self-test passes. Seven of seven quotes are verbatim on the cited lines, and the seven hashes match.
- Depth claim as bounded: **FAILS.** Six of the seven quoted levers meet the one-named-skill bound on their quoted text (S021 per-skill policy in `agents/openai.yaml`, codex.md:195-207; S022 per-skill frontmatter, claude.md:886; S025 per-skill frontmatter, vscode.md:289 and :295; S030 per-name list, skill-sdk.md:809 and :187; S024 exact-name use, with F7; S029 named use, with F6). Copilot CLI (S031) does not, and the entry excludes that category itself.

## 6. Residual risk and verification gaps

- Outside this item: C1 freshness, the 17 no-harm gates, routed defects D1-D7.
- The live check is a substring test on bytes fetched at 15:15Z and 15:18Z. A later page change moves the numbers with no lane change.
- The per-name Copilot CLI lever (`disabledSkills`) was checked on the page only. It has no SOURCES row and no Gate record, and I did not test it against a client.
- Effect semantics for Claude Code, Codex and VS Code were checked against the lines I read (claude.md:886; codex.md:195-218; vscode.md:289-296). I did not run these clients.
- Probes P1 and P2 ran in memory on my clone copy. Nothing was written to the lane.

## 7. Command log

- `python3 -B verifiers/check_overlap_levers.py --rev 43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` → exit 1 (`overlap levers backed 0 of 7 clients`)
- `python3 -B verifiers/check_overlap_levers.py --rev 59903b2637689739a5b9901956301da72d0effe1` → exit 0 (`overlap levers backed 7 of 7 clients`)
- `date -u +%FT%TZ && python3 -B verifiers/check_overlap_levers.py --rev 59903b2637689739a5b9901956301da72d0effe1 --fetch; echo EXIT=$?; date -u +%FT%TZ` → 15:15:33Z, `quotes found on live pages 7 of 7`, EXIT=0, 15:15:34Z
- `python3 -B verifiers/check_overlap_levers.py --self-test` → `0 failures`, `22 assertions`, exit 0
- curl of the seven `.md` pages, 2026-10-22T15:18:41Z-15:18:42Z, each HTTP 200 (section 2)
- curl of cli-config-dir-reference.md, 2026-10-22T15:21:34Z, HTTP 200, 166,811 B, sha256 8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0
- `git -C <clone> log -S` on `ignoredSkillsLocations`, `/skills disable <name>`, `disable-model-invocation: true` → all three first appear in 34cfffb
- `git -C <clone> show 7c81a78:verifiers/check_overlap_levers.py` → REVIEWED_LEVERS lacks the three terms
