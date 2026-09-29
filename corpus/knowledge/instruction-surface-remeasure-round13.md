# Instruction-surface re-measurement — the second witness (round 13)

**Runner.** L2 lane `scout-independent` (seat `ProposedReptile`), dispatched by
this lane in round 13 and **blind**: it did not read the L1's anchors, the two
surface scouts' scratch, the plan, this repo's census file, or
`verifiers/verify_surfaces.py`. Recorded verdicts below are its own; the
agreement table is the L1's, and its scratch artifacts are not in this repo.

**Why it counts as a derivation and not a re-run.** Different method, same
question: it never invoked `strings` — it wrote its own printable-run extractor
(`re.finditer(rb"[\x20-\x7e]{8,}")` over raw bytes → `offset<TAB>len<TAB>text`,
833,846 runs for omp / 344,469 for opencode), then adjudicated each candidate by
reading the enclosing code window. Method, artifacts, and per-class provenance
commands are in its record; the L1 reproduced the load-bearing literals by an
independent byte scan (`omp` `RULES.md` 6 hits, `enabledProviders` 4,
`disabledProviders` 21; opencode `<system-reminder>` 18, `{mode,modes}` 2,
`CONTEXT.md` 1 — and omp `CONTEXT.md` 0).

## Agreement (check-for-check, against `instruction-surface-census-round13.md`)

| Question | Census (L1) | Second derivation | Verdict |
|---|---|---|---|
| opencode `CLAUDE.md`: loader or prompt text? | loader — `y[1]` in the name-priority list + `n[1]` = `~/.claude/CLAUDE.md`, gated by `OPENCODE_DISABLE_CLAUDE_CODE{,_PROMPT}` | same, with byte anchors (`Instruction` service, `systemPaths`), plus `.cursor*`/`copilot`/`CONVENTIONS` hits confined to the `/init` template | **agree** — and this is the question one L2 lane got wrong; the disagreement is the round's finding |
| opencode project walk semantics | first existing name per directory, `y` = AGENTS.md → CLAUDE.md → CONTEXT.md | `findUp` iterates names in order, `break` on first name with hits, all ancestor dirs of that name collected | **agree** |
| opencode config `instructions` | path/glob/`https://`, remote fetched (`concurrency: 4`) and rendered `Instructions from: <url>` | same, with the 5 s timeout named and `./`/absolute/glob resolution modes | **agree** |
| omp `.md` context classes | 8 machine-extracted registrations (`agents-md`, `claude-md`, `opencode`, `gemini` ×3, `github` copilot, `windsurf` global_rules) | same set, each with an enclosing function and byte offset | **agree** |
| omp registry is per-ecosystem/provider | one class per tool family; exclusions carry reasons | registry is a capability table (`Ut(<id>, {id, displayName, description, priority, load})`) with kinds `context-files`/`rules`/`system-prompt`/`instructions`/`skills`/… | **agree** (its structural read is deeper; adopted into the census's § Method) |
| prompt-text vs loader literals | `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md` inside opencode are `/init` template text | same, with offsets and a byte-identical `b=Create or update AGENTS.md` anchor | **agree** |

## What the second witness added (now in the census)

1. **Provider enablement gates the user-level half.** `RTo` = opt-in set
   `{cursor,codex,claude,claude-plugins,gemini,opencode,windsurf,github}`;
   `eu()` admits a provider's *user* paths only when it is enabled
   (`enabledProviders`, `*`/`all`, or `CLAUDE_CONFIG_DIR` for claude);
   `disabledProviders` removes it entirely; **project-level `Cl` paths are never
   gated**. Default-on: `agents-md`, `agents`, `native`, `claude-md`, `cline`,
   `github` project paths. Craft consequence: *a repo carrying `GEMINI.md` or
   `.cursor/rules` does not mean the harness read it* — the user's provider list
   decides the user-level half.
2. **`RULES.md`** — a single-file rules class (`~/.omp/agent/RULES.md` + nearest
   `<ancestor>/.omp/RULES.md`), separate from the `rules/` directories.
3. **opencode's read hook** — `Instruction.resolve`, called from
   `ReadTool.execute`, appends the nearest ancestor instruction file to a *tool
   result* as `<system-reminder>`: a second injection channel beside the system
   prompt (so a rule file can arrive mid-session, attached to a read).
4. **`*.instructions.md` are glob-scoped, not standing prompt text** —
   `applyTo` `**`/`*`/`**/*` → alwaysApply; otherwise triggered. The census's
   github/instructions class is therefore *conditional* rule text.
5. **Agent definitions supply `agent.prompt` as the system head** when that agent
   runs (opencode `{agent,agents}/*.md` and `{mode,modes}/*.md`) — an override
   channel, not ambient context.

## Where the two disagree (recorded, not smoothed)

- **Description-vs-code gaps in omp's registry** (the census anchors those two
  hand-declared classes on the registry's own description strings): the
  descriptions name `.cursorrules` and `.windsurfrules`, and the second witness
  found **no code path** reading either literal. The classes are real
  (`.cursor/rules/*.{mdc,md}`, `.windsurf/rules/*.md`,
  `~/.codeium/windsurf/memories/global_rules.md`); the *literals in the
  description* are partial overstatements. The census now says so on both rows.
- **`.opencode/AGENTS.md` / project `.codex/AGENTS.md`**: no read path — both
  agree, against a plausible reading of the registry text ("Load AGENTS.md from
  `~/.config/opencode/`", "`~/.codex/AGENTS.md` (user-level only)"). The census
  rows already carry "user-level only"; the second witness confirms.
- **Unresolved by both**: whether `LDe` ("instructions") bodies ever enter the
  system prompt (no direct consumer call found), memory-store classes, and
  opencode version matching (no TS checkout on this host → binary-only,
  `1.18.31` per `--version`).

## Verdict

**Agreement on every load-bearing file class**, one lane-vs-lane disagreement
resolved by the L1 against the host-census lane (see the census's § The
disagreement this census had to adjudicate), five additions adopted, two
description-vs-code gaps recorded, and **one item left unresolved by both lanes**
(whether `LDe`/`instructions` bodies ever enter the system prompt — a shared open
question, not a disagreement; the verdict above says "class", not "every claim the
two lanes make"). Round-12's rule applies unchanged: agreement between two
derivations is evidence, and their first disagreement is the finding — here the
round's first disagreement was *between L2 lanes*, and it was decided by reading
the code, not by counting strings.