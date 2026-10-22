# Verdict: HOLDS-BOUNDED — ReopenS021, C2 Codex row (four points hold; bounds F1–F3)

Verdict: HOLDS-BOUNDED. The Codex row (`corpus/knowledge/skill-overlap-levers-round51.md`, § Levers by client; `SKILL.md` § Anti-patterns, Codex row) matches the live page on all four points. Bounds: one S021 citation range misses the line it cites (F1); the counter checks a row's `held by` and `effect` only against vocabularies, not per client (F2); the counter's Codex key-term set admits a term the entry lists as uncounted (F3). None changes the landed Codex row.

This report supersedes my first draft. That draft said "25 hits" for the Codex grep (the count is 32) and gave exit codes I had not captured. Both are corrected below.

## Fresh fetch (my own re-open)

- Command: `curl -sS -o /fast/scratch/hyaku/kotoba-r51/falsify/ReopenS021/build-skills.md -w 'HTTP=%{http_code} bytes=%{size_download}\n' https://learn.chatgpt.com/docs/build-skills.md`. Output: `HTTP=200 bytes=11035`. Exit status not echoed; the file was re-hashed in a later call (below).
- `sha256sum` of the file: `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`. The expected prefix `ed6e324f` matches. The same hash is printed again by a later `sha256sum build-skills.md | cut -c1-64`.
- Access time: `date -u` → `2026-10-22T15:14:41Z`.
- Tools installed or updated: none. curl, grep, sed, python3 and sha256sum were already present.

## Point 1: quote verbatim, 25 words or fewer, key term as a backtick span. HOLDS

- Entry Codex row cites `build-skills.md:218`. Its quote is: `allow_implicit_invocation` (default: `true`): When `false`, Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works.
- Python compare of that quote against line 218 of my fetched bytes: `QUOTE_EQUAL True`. Word count `WORDS 20`. Backtick span present `BACKTICK_SPAN True`. The script printed without a traceback.
- The SKILL.md Codex row's key term cell is the same exact span, `allow_implicit_invocation`.

## Point 2: the page says what the lever, held-by and effect cells say. HOLDS

Sections read in full: lines 1-29 (intro), 27-53 (budget), 50-87 (file tree), 88-138 (how Codex uses skills; where it loads them), 175-233 (enable or disable; optional metadata; best practices).

- Lever, "a per-skill policy turns off implicit invocation; explicit `$skill` use still works": line 195 says "Add `agents/openai.yaml` … to set invocation policy". Line 207 shows the `policy:` block with `allow_implicit_invocation: false`. Line 218 gives the effect.
- Held by, "skill author": the file tree at lines 50-82 puts `agents/openai.yaml` inside `my-skill/`, so the file travels with the skill. The page never says who may edit it or whether a user can override it. "Skill author" is inferred from the file's location. This is a bound, not a defect.
- Effect, "automatic choice off": line 218 says Codex "won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works". That is automatic choice off with manual use kept.
- The page's user-level disable (`[[skills.config]]` with `enabled = false`, lines 181-191) is a different lever. The entry does not count it for this row.

## Point 3: S021 row (`corpus/SOURCES.md:34`). HOLDS, with one citation defect (F1)

- Kind `docs`: yes. Tier `A`: yes. Status `mined`: yes, verified-at 2026-10-22, recheck 90d.
- URL `https://learn.chatgpt.com/docs/build-skills` is under the prefix `https://learn.chatgpt.com/docs/`, which the counter pins for Codex (`verifiers/check_overlap_levers.py:133`).
- `used-by` includes `corpus/knowledge/skill-overlap-levers-round51.md`: yes.
- `corpus/lessons/round-51.md` § Gate, Admitted, records the S021 re-open (seat `SrcCodex`, hash `ed6e324f…`, `build-skills.md:218`): yes.
- Revision facts: 11,035 bytes (matches my fetch). "232 lines" matches `wc -l` (232). `grep -c ''` gives 233 because the last line has no trailing newline; `tail -c1` prints `.`.
- F1 (Minor, citation): the row cites "page intro md:37-40 (budget, shortening, may omit skills)". "May omit" is on line 41: "sets, Codex may omit some skills from the initial list and show a warning." The range should be `md:37-41`. Line 40 holds "shortens".

## Point 4: no documented rule between two skills that both remain candidates. HOLDS

Exact sweep, `grep -niE 'overlap|conflict|precedence|tie|both|choose|select|priorit' build-skills.md`: 5 lines (5, 46, 96, 98, 138). `sweep_exit=0`. Each read in context:

- Line 5: "tie" is inside "capabilities". Not a rule.
- Line 46: "When Codex selects a skill, it still reads the full SKILL.md instructions". Describes loading after a choice. Not a rule between candidates.
- Line 96: "type `@` to select a skill" (ChatGPT) and "run `/skills` or type `$` to mention a skill" (Codex CLI). These are the user's explicit choice of one skill. They are not a host tie-break. The entry claims no host rule, and it does not say explicit naming is absent, so the claim stands.
- Lines 98-103: implicit choice happens "when your task matches the skill `description`", followed by "write concise descriptions with clear scope and boundaries" and "so a host can still match the skill if descriptions are shortened". The description is the only documented influence, as the entry says.
- Line 138: "If two skills share the same `name`, Codex doesn't merge them; both can appear in skill selectors." No arbiter is named, and both stay. This supports the entry's negative.

Extended sweep, because the first pattern misses budget and omission wording: `grep -niE 'omit|shorten|budget|limit|order|first|remain|instead'` gives 7 lines (40, 41, 44, 46, 103, 108, 112). `ext_exit=0`.

- Lines 40-41: "If many skills are installed, Codex shortens skill descriptions first. For large skill sets, Codex may omit some skills from the initial list and show a warning." This is the page's only omission rule. It orders which text shrinks (descriptions first) and says skills may drop from the initial list. It does not say which skills drop, or in what order. It does not decide between two candidates that both stay in the list. It is a budget, not a per-skill lever, so the entry's count is unaffected.
- Lines 43-44: `skills.max_context_tokens` raises the budget to at most 10,000 tokens. A user setting, not a choice rule.
- Lines 108 and 112 are about creating skills, not choosing them.
- The entry's Limits do not mention the omission rule (Info, F4).

## Counter-level findings (what the counter does with the Codex row)

- F2 (Minor, bound on the counter): `held by` and `effect` are checked only for membership in two vocabularies: `ALLOWED_HELD_BY` (`skill author`, `user or operator`, `app developer`; `check_overlap_levers.py:118`) and `ALLOWED_EFFECTS` (line 119). The checks at lines 345-351 test membership and nothing else. `grep -nE 'held_by *(==|!=)|effect *(==|!=)|\["held_by"\]|\["effect"\]'` finds only those lines, so no per-client comparison exists. The round plan's hardening wording is "six columns with pinned `held by` and `effect` values" (`plans/round-51.md`, § Re-sizing, C2). That is met only in the vocabulary sense.
  - [INFERENCE, not executed] A Codex row reading `user or operator | removed everywhere | S021 | allow_implicit_invocation` would pass every per-client check at lines 330-415, because the key term and quote checks do not depend on the holder or effect cells. I did not run a mutant to confirm this.
  - The landed Codex row is correct, so this is a bound on the counter, not a defect in the row.
- F3 (Minor, inconsistency): `REVIEWED_LEVERS["Codex"]` = `{"allow_implicit_invocation", "enabled = false"}` (`check_overlap_levers.py:151`). The entry's "Other levers … not counted" paragraph lists the same page's Codex `[[skills.config]]` with `enabled = false` (`:183-189`) as not counted. The list and the entry disagree. A row would need a backtick span `enabled = false` in its quote to pass, and the page's example sits in a TOML code block with no backticks, so the path is narrow. The landed row is unaffected. Either drop the term or count the lever.
- F4 (Info): the entry's Limits do not mention the page's budget-omission rule (lines 40-41).

## Residual risk and verification gaps

- The fetch is one snapshot at 15:14:41Z. The page can change after it. The entry's `recheck` line compares the `.md` hash, so later drift is detectable.
- Holder "skill author" is inferred from file location. The page does not say who may edit `agents/openai.yaml`.
- I did not run `check_overlap_levers.py`, `--fetch`, `--self-test`, or any mutant. F2 rests on reading the code.
- Scope was the Codex row only. The other six client rows were not checked.

## Evidence

Scratch root: `/fast/scratch/hyaku/kotoba-r51/falsify/ReopenS021/`. Lane access was read-only. The only write was this report.

| # | command | output | exit |
|---|---|---|---|
| 1 | `curl -sS -o build-skills.md -w 'HTTP=%{http_code} bytes=%{size_download}\n' https://learn.chatgpt.com/docs/build-skills.md` | `HTTP=200 bytes=11035` | not echoed |
| 2 | `sha256sum build-skills.md` | `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` | printed, no error |
| 3 | `date -u` | `2026-10-22T15:14:41Z` | printed |
| 4 | python3 compare, line 218 against the entry quote | `QUOTE_EQUAL True`, `WORDS 20`, `BACKTICK_SPAN True` | no traceback |
| 5 | `grep -ciE 'codex' build-skills.md` | `32` | not echoed; grep exits 0 when it selects lines |
| 6 | `wc -l`, `grep -c ''`, `tail -c1` on build-skills.md | `232`, `233`, `.` | printed |
| 7 | exact sweep `grep -niE 'overlap\|conflict\|precedence\|tie\|both\|choose\|select\|priorit'` | 5 lines: 5, 46, 96, 98, 138 | `sweep_exit=0` |
| 8 | extended sweep `grep -niE 'omit\|shorten\|budget\|limit\|order\|first\|remain\|instead'` | 7 lines: 40, 41, 44, 46, 103, 108, 112 | `ext_exit=0` |
| 9 | `grep -niE 'openai.yaml\|FileTree\|SKILL.md\|agents/'` | file tree 78; text 195 | `yaml_exit=0` |
| 10 | `grep -nE 'Implicit\|implicit\|concise descriptions\|still reads\|skills.max_context_tokens\|allow_implicit'` | 43, 46, 98, 101, 207, 218 | `impl_exit=0` |
| 11 | `sed -n '37,41p' build-skills.md \| cat -n` | line 41 holds "may omit" | `EXIT=0` |
| 12 | `sed -n '137,152p' verifiers/check_overlap_levers.py` (lane, read only) | `REVIEWED_LEVERS`, Codex at line 151 | `EXIT=0` |
| 13 | `sed -n '330,415p' verifiers/check_overlap_levers.py` (lane, read only) | per-client checks; holder and effect at 345-351 | `EXIT=0` |
| 14 | `grep -nE 'held_by *(==\|!=)\|effect *(==\|!=)…' verifiers/check_overlap_levers.py` (lane, read only) | 345, 347, 349, 351 only | `EXIT=0` |

Report: .ufo/waves/round-51/falsify/ReopenS021.md
