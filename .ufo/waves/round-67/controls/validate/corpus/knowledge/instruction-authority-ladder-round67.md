# Instruction authority ladder and the boundary it draws around skill bodies

source: S123 — OpenAI Model Spec (August 18, 2026) — https://model-spec.openai.com/2026-08-18 — `# Instructions and levels of authority` → `# The chain of command`
source: S124 — anthropics/skills — skill-creator/SKILL.md — https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md — tree `dbd4588` — `# Description Optimization` → `# Step 1: Generate trigger eval queries`
source: S129 — Many-Tier Instruction Hierarchy in LLM Agents — arXiv:2604.09443 — https://arxiv.org/abs/2604.09443 — `# abstract`
verified-at: 2026-10-24
recheck: 90d — re-fetch the Model Spec page, the pinned skill-creator tree and the arXiv record; confirm the override sentence, the trigger-eval numbers and the abstract's level/task/agent counts still read the same
ground: the lane's open item on what an instruction may assert and at whose authority level — the layer above the skill format, previously unheld.

**The ladder.** OpenAI's Model Spec assigns every instruction a level of authority and states
the override rule: "Instructions with higher authority override those with lower authority."
Under `# Instructions and levels of authority` the page names the levels Root, System, Developer,
User and Guideline, in that order; under `# The chain of command` the ordering it renders adds
**No Authority** as a sixth. The page's header reads `August 18, 2026`; the literal string
`2026/08/18` does **not** appear in the fetched main text, so this entry cites the date as the
page renders it and does not assert a version string.

**Why it matters to skill craft.** A `SKILL.md` body is not a privileged instruction; it is text
a model reads and may or may not obey. Anthropic's own reference skill treats the description as
the mechanism that governs behaviour, and gives the eval loop it optimises with:
"Create 20 eval queries — a mix of should-trigger and should-not-trigger." The same file states
that the loop "evaluates current description (running each query 3 times to get reliable trigger
rate)", with a 60/40 held-out split and up to 5 iterations. So the craft surface splits in two —
the *description* decides whether the skill is entered at all; the *body* is obeyed only to the
extent the model chooses to obey it.

**The measurement, and why a fixed ladder is not enough.** ManyIH argues that a fixed few-level
paradigm is inadequate for agentic settings: the fixed paradigm "assumes a fixed, small set of
privilege levels (typically fewer than five) defined by rigid role labels", which is inadequate
where conflicts arise across many sources. Its benchmark requires navigating up to 12 levels of
conflicting instructions across 853 agentic tasks spanning 46 real-world agents, and frontier
models score roughly 40%. The ladder is therefore not a solved problem: a skill author cannot
assume their instruction outranks, or is outranked by, a retrieved document.

**Consequence for the lane.** Any future claim of the form "a skill body may instruct X" must
name the authority level it speaks at. The lane held no row for this layer before this round.

**Bounds.** (i) The Model Spec is OpenAI's own training-time contract; it is evidence about
OpenAI's authority model, not a claim that any other client implements it. (ii) The six-level
reading (Root → System → Developer → User → Guideline → No Authority) is what the chain-of-command
section renders; the five-level reading is what the earlier section lists. Both are recorded here
because the page carries both. (iii) The Anthropic row is one vendor's reference skill at one
pinned tree — it is evidence about how that vendor teaches skill authoring, not a measurement of
any client's behaviour. (iv) The arXiv figures are the paper's own reported benchmark numbers;
the abstract attaches the ~40% score to "the current frontier models" without naming one model.
(v) No client was run: this entry is documentary evidence, re-opened 2026-10-24 by the round-67
scouts (`ScoutModelSpec`, `ScoutSkillCreator`, `ScoutArxiv` logs under
`.ufo/waves/round-67/w1/logs/`).
