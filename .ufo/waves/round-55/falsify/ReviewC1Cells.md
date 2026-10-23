Result: HOLDS — routed defect 3 is repaired: each of the four narrowed cells in SKILL.md § Description thresholds by client (ed3e8996, present at tip f0e6b695) says no more than its re-opened source, and `check_description_thresholds.py --fetch` exits 0.

# Scope

Routed defect 3 from `corpus/lessons/round-54-verifier-spotcheck.md:217-223` names four over-wide
cells. Diff `git show ed3e8996 -- SKILL.md` changed exactly four cells in § Description thresholds
by client (also: anti-pattern prose moved verbatim to `corpus/knowledge/skill-overlap-levers-round51.md`,
two registry rows added for the round-55 counters — both judged out of this item's scope; the
registry cells describe the counters and contain no numeric claims).

# Cell-by-cell check (each new cell vs its re-opened source)

## Cell 1 — Codex, "Past the threshold" (SKILL.md:186)

New text: "At the initial-list budget, Codex shortens descriptions first; for large skill sets it may
omit skills from the initial list with a warning; selecting a skill still reads the full `SKILL.md`."
The unpinned sentence "(its shipped parser also cuts each catalog description at 1,024 characters,
`corpus/knowledge/frontmatter-rule-authorities-round48.md:51`)" was dropped, as routed
(`spotcheck:219-220`: the cited entry says that claim is "not tabled here because no source row pins
that code").

Source: S054 = learn.chatgpt.com/docs/build-skills(.md), fetched bytes lines 38-46:
- :38-39 "By default, this list uses at most 2% of the model's context window, or 8,000 characters
  when the context window is unknown."
- :40-41 "If many skills are installed, Codex shortens skill descriptions first. For large skill sets,
  Codex may omit some skills from the initial list and show a warning."
- :46 "When Codex selects a skill, it still reads the full SKILL.md instructions for that skill."

Verdict: within source. "At the initial-list budget" is a fair paraphrase of the :38-41 sequence
(shortening is what happens when the list budget binds); "may omit… with a warning" and "still reads
the full SKILL.md" are near-verbatim. No claim remains that lacks a pinned source.

## Cell 2 — Gemini CLI, "Documented threshold" (SKILL.md:189)

New text: "No threshold: ~100 words is a size estimate for metadata (name + description), which is
always in context."

Source: S057 = geminicli.com/docs/cli/skills-best-practices.md, fetched bytes :24:
`1.  **Metadata (name + description)**: Always in context (~100 words).`
(byte verbatim; markdown `**` retained in the fetched bytes — the round-54 minor defect about the
stripped quote is in the lesson, not this cell.)

Verdict: within source, and matches the routed instruction "Mark it as no threshold"
(`spotcheck:218`). The page states a parenthesised size figure, no rule and no consequence; the cell
says exactly that. Note (not a defect): the cell now says "No threshold" while the counter still
counts Gemini CLI as BACKED because `100` is a number token — the counter docstring disclaims this
judgment (`verifiers/check_description_thresholds.py:46-48`), and the routed fix chose honesty over
the counter's label. The paired entry reading
(`corpus/knowledge/skill-listing-thresholds-round54.md:44`) calls it "a soft per-skill listing
budget, not an authoring maximum or a per-entry cut" — consistent, slightly different framing;
harmless.

## Cell 3 — Gemini CLI, "Past the threshold" (SKILL.md:189)

New text: "The loader keeps `frontmatter.description` as-is (`skillLoader.ts:211`) and the prompt
template inserts it directly (`snippets.ts:320`) at `google-gemini/gemini-cli@451a02ff`; no
description cut appears in these steps, so longer descriptions spend context."

This adds the source pointer the routed defect said was missing (`spotcheck:223`).

Sources re-opened at the pinned commit `451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1`:
- `packages/core/src/skills/skillLoader.ts:211` — `description: frontmatter.description,` inside the
  object `loadSkillMetadata` returns (`:208-213`). Grep of the whole file for `slice|substr|truncat|
  .length|1024|maxL` finds only YAML-unquoting slices (`:70`, `:92`, `:100`) and parser bookkeeping;
  no length cut on `description`.
- `packages/core/src/prompts/snippets.ts:314-320` — `renderAgentSkills` maps each skill to
  `<skill><name>…</name><description>${skill.description}</description>…`, and `:144` shows the
  rendered block interpolated into the larger prompt template. Grep finds no length cut on
  `skill.description`.

Verdict: within source. "Inserts it directly" is template-interpolation accurate; "no description
cut appears in these steps" is honestly scoped to the two files and confirmed by grep. The inference
"longer descriptions spend context" follows from the listing being prompt text (S057 "Always in
context") plus direct insertion. The cell does not claim client-wide absence of truncation (that
would be over-wide — the grep covers only these two files, and upstream consumers of
`AgentSkillOptions` are not cited). Entry reading (`:44`) matches.

## Cell 4 — Cursor, "Action" (SKILL.md:190)

New text: "Keep `description` at or under 1,024 characters; an over-limit skill still loads and gets
a yellow warning in `/skills`." The unsourced advice "move detail into `references/`" was dropped,
as routed (`spotcheck:221-222`: it is not in S058; dropping was one of the two allowed fixes, and no
`cursor.com/docs/skills.md` citation was added — that route stays optional, not required).

Source: S058 = cursor.com/docs/release-notes.md, fetched bytes :120-122 (§ v2026.10.08 → § Skills):
- :122 "`/skills` flags skills that break the Agent Skills limits. Skills that load but exceed the
  spec's limits now show a yellow warning count in `/skills`, and selecting one lists what to fix
  under it. Warnings cover a name over 64 characters or not in lowercase-hyphen form, a frontmatter
  `name` that doesn't match the folder, a description over 1,024 characters, and a body over about
  5,000 tokens."
(The byte quote above runs long for context; the lane's recorded quote ends at "1,024 characters"
per `skill-listing-thresholds-round54.md:45` and matches the fetched bytes verbatim.)

Verdict: within source. "still loads" paraphrases "Skills that load but exceed the spec's limits";
"yellow warning in `/skills`" is verbatim substance; "at or under 1,024" restates the documented
warning trigger as advice — the normal Action-cell direction, no added claim.

# Counter run (own sandbox clone)

```
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/ReviewC1Cells
git -C … checkout -q f0e6b695b746775823b65a8c45de7d50ea33e84f   # HEAD verified = f0e6b695
cd /fast/scratch/hyaku/kotoba-r55/ReviewC1Cells
timeout 300 python3 -B verifiers/check_description_thresholds.py --rev f0e6b695… --fetch
Claude Code  BACKED found=True
Codex        BACKED found=True
VS Code      BACKED found=True
Copilot CLI  BACKED found=True
Gemini CLI   BACKED found=True
Cursor      BACKED found=True
opencode     BACKED found=True
description thresholds backed 7 of 7 clients
description thresholds found on the live page 7 of 7
exit 0
```

The narrowed cells did not drop the count (7 of 7 ≥ target 4); the Gemini "No threshold" wording
keeps a number token (`100`), so the counter's mechanical BACKED label is unchanged — as routed
("None of them drops the count below 4 of 7" was the defect's own framing).

# Source access record (ordinary curl; `date -u` lines observed)

`date -u` printed `Fri 23 Oct 2026 12:13:17 AM UTC` immediately before the five GETs and
`Fri 23 Oct 2026 12:13:19 AM UTC` immediately after (host local time is UTC-3, so the UTC date is
2026-10-23 — inside the session's 2026-10-22/23 window).

| URL | status | bytes | sha256 (recorded prefix in SOURCES) |
|---|---|---|---|
| geminicli.com/docs/cli/skills-best-practices.md | 200 | 3,257 | `612c3b83…` = S057 record — byte-identical to the recorded fetch |
| cursor.com/docs/release-notes.md | 200 | 301,193 | `fd4d830a…` = S058 record — byte-identical |
| learn.chatgpt.com/docs/build-skills.md | 200 | 11,035 | `ed6e324f…` = S054 record — byte-identical |
| raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff…/packages/core/src/skills/skillLoader.ts | 200 | 6,560 | `8bce3215…` (not previously recorded in SOURCES) |
| raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff…/packages/core/src/prompts/snippets.ts | 200 | 70,505 | `b2cccbd0…` (not previously recorded in SOURCES) |

Fetched bytes live at `/fast/scratch/hyaku/kotoba-r55/ReviewC1Cells/fetches/` (my scratch only).

# Findings

None at defect severity. All four routed fixes land: the unpinned Codex parser claim and the
unsourced Cursor `references/` advice are gone; the Gemini threshold is marked "No threshold"; the
Gemini no-cut claim now carries its `skillLoader.ts`/`snippets.ts` pin, which verifies.

## Residual risk / verification gaps

- The cell claims "no description cut appears in these steps" scoped to two files at one commit.
  Other consumers of `AgentSkillOptions`/`SkillDefinition` upstream of `renderAgentSkills` are not
  cited; a cut elsewhere in the pipeline would not contradict the cell as worded, but "the
  description reaches the prompt whole" (entry :44) leans on the same two files. Acceptable as
  scoped; a future reader wanting stronger assurance would need a full call-chain read.
- "No threshold" vs the counter's mechanical BACKED label: the counter counts the cell anyway, so
  the honesty fix is invisible to the count. Known and disclosed in the counter docstring (Q31,
  `check_description_thresholds.py:46-48`).
- Minor: SKILL.md cell says "size estimate"; entry :44 says "soft per-skill listing budget". Both
  deny a limit; the words differ. Not a defect.
- Sources unchanged since the round-54 records (all sha256 prefixes match), so the admits still hold
  today.

No installs or upgrades performed. No lane files mutated; all runs and fetches in
`/fast/scratch/hyaku/kotoba-r55/ReviewC1Cells/` (clone at f0e6b695); no processes left running.
