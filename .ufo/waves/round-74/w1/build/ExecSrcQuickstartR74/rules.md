# Quickstart page — the 12 strongest author rules (located in snapshot.md, lines as numbered there)

Snapshot: `snapshot.md` (= the fetched `.md`, 83 lines, 4 080 B, sha256 `7c480b44…c32bffb`).
Each quote was produced with `sed -n '<n>p' snapshot.md`; the bytes dropped are named per row.
Tokens are the backticked commands/paths and the quoted sentences an entry row may carry.

| # | rule (one line) | quote (≤25 words) | line | bytes dropped | tokens | action an author performs |
|---|---|---|---|---|---|---|
| 1 | The default discovery root for a VS Code project is `.agents/skills/` | "VS Code looks for skills in `.agents/skills/` by default." | 21 | the line's first and third sentences, and their punctuation | `.agents/skills/` | create the skill under `.agents/skills/<name>/SKILL.md` and nowhere else by default |
| 2 | A skill is a directory with a `SKILL.md` inside it | "A skill is a folder containing a `SKILL.md` file." | 21 | sentences 2–3 of line 21 | `SKILL.md` | make the skill a folder whose entry file is `SKILL.md`, never a loose file |
| 3 | The path is relative to the project root, project-scoped | "Create `.agents/skills/roll-dice/SKILL.md` in your project:" | 21 | sentences 1–2 of line 21 | `.agents/skills/roll-dice/SKILL.md` | place the folder inside the project tree, not in a user-home root |
| 4 | Frontmatter `name` must equal the folder name | "A short identifier for the skill. Must match the folder name." | 46 | the bullet marker and the `**`name`** — ` prefix | `name` | set `name:` to the directory name exactly |
| 5 | `description` is an activation decision, not a summary | "Tells the agent when to use this skill. This is how the agent decides whether to activate it." | 47 | the bullet marker and the `**`description`** — ` prefix | `description` | write the description as the when-to-use cue the client matches on |
| 6 | The worked description states capability then the user's phrasings | "Roll dice using a random number generator. Use when asked to roll a die (d6, d20, etc.), roll dice, or generate a random dice roll." | 26 | the `description: ` label | `Use when asked`, `(d6, d20, etc.)` | open with the capability in one clause, then "Use when asked …" with concrete phrasings |
| 7 | A first skill is one small file | "one file, under 20 lines" | 44 | "That's it — " before and "Here's what each part does:" after | "one file, under 20 lines" | ship the first version as one file of under twenty lines |
| 8 | Confirm discovery before trusting the path | "Type `/skills` to confirm that `roll-dice` appears in the list." | 55 | the `4. ` marker and the following sentence | `/skills`, `.agents/skills/roll-dice/SKILL.md` | list skills with `/skills` and fix the path if the name is missing |
| 9 | Test activation with a natural user prompt and let it run | "The agent should activate the `roll-dice` skill. It may ask for permission to run a terminal command — allow it." | 58 | the following sentence about the returned number | `roll-dice` | run one realistic request ("Roll a d20"), not the skill name, and permit the command |
| 10 | Model variance is a known cause of a silent miss | "Tool-use reliability varies across models" | 62 | the callout's preceding sentence and the two following clauses | "Tool-use reliability varies across models" | if no command runs, retry on another model before rewriting the skill |
| 11 | Keep the skill client-neutral so it travels | "The same skill works in any compatible agent, including Claude Code and OpenAI Codex." | 17 | the callout's first sentence and the `> ` prefix | "Claude Code and OpenAI Codex" | avoid client-specific claims so the same folder loads in another harness |
| 12 | Discovery reads metadata only; the body loads on activation | "It read only the `name` and `description`, just enough to know when the skill might be relevant." | 68 | the `1. **Discovery** — When the chat session started, the agent scanned default skill directories and found your skill.` prefix | `name`, `description` | keep the always-loaded metadata short and put the procedure in the body |

Token census for the C1 Q45 question (this page alone), counting distinct backticked spans plus each quoted
rule sentence as one token: 10 of the 12 rules carry ≥2 tokens; rules 7 and 10 carry one quoted sentence each
("one file, under 20 lines"; "Tool-use reliability varies across models"). The page therefore clears C1's
"≥2 rule tokens" bar for a page row with a wide margin, so `quickstart` is a valid `P` under C1 (a).
