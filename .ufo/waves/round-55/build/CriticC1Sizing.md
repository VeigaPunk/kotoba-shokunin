Result: BREAKS — the frozen C1 predicate (`--fetch` exit 0, F>=4, G>=2) is met by a real-quote world that holds no explicit-invocation form at all, and "new ground" counts a case-flipped copy of a sentence already held in base knowledge; the counter stays frozen, so the repair is a pre-content erratum plus reviewer guards that bound the claim.

Seat: KotobaR55.CriticC1Sizing (critic, read-only). Sandbox: `/fast/scratch/hyaku/kotoba-r55/CriticC1Sizing`, cloned from the lane and checked out at plan commit `a10240c0`. The counter bytes ran unchanged: sha256 `4fc6e01ad576531c95265c7dcd2440b0b2bda0cd3520a0b317c46cd78b3ff5e5`, the same value the control receipts record. `--self-test` printed `self-test: 0 failure(s) over 29 assertions`, exit 0. Fixture builder: `probe/build.py` in the sandbox; fetched bytes are in `probe/`. Lane tip when this report was written: `ed3e899`, which has no C1 table or entry yet. No installs. No processes left running.

## Counterexample 1 — the predicate passes with zero explicit-invocation forms (the cheaper shortcut)

World W1, sandbox commit `04869b820c92891728d6dc4def5c08f6a3529f0a` on `a10240c0`. It adds a `### Explicit invocation by client` table, the entry, seven new SOURCES rows (S801-S807: tier A, docs, mined, opened 2026-10-22, used-by set to the entry), and a round-55 `## Gate`. Every quote is real text from a live page on the client's pinned host. Every page except Cursor's is already a SOURCES row at base under another id. None of the seven tokens is a form that invokes a named skill:

| client | token in form cell | what the token actually is | page (base row already citing it) |
|---|---|---|---|
| Claude Code | `/compact` | a built-in command; the page says built-ins "such as /compact are not" available as skills | code.claude.com/docs/en/skills.md (S053) |
| Codex | `@layer` | a CSS at-rule in the page's `<style>` block (`codex.html:37`) | learn.chatgpt.com/docs/build-skills (S021, S054) |
| VS Code | `#file:` | file-reference syntax | code.visualstudio.com/docs/agent-customization/agent-skills (S025, S055) |
| Copilot CLI | `/skills list` | a listing command | docs.github.com/.../cli-command-reference (S031, S038, S056) |
| Gemini CLI | `/skills list` | a listing command | geminicli.com/docs/cli/skills/ (S029) |
| Cursor | `/help/customization/skills.md` | the URL path of a "Related" link (`cursor.md:339`) | cursor.com/docs/skills.md (not a base row) |
| opencode | `/skills/<invented-r55-placeholder>/SKILL.md` | a file path whose placeholder text does not appear on the page | opencode.ai/docs/skills.md (S059) |

```
2026-10-22T23:15:06Z
$ timeout 600 python3 -B verifiers/check_explicit_invocation.py --rev 04869b82... --fetch
Claude Code  BACKED token=/compact new=True found=True
Codex        BACKED token=@layer new=True found=True
VS Code      BACKED token=#file: new=True found=True
Copilot CLI  BACKED token=/skills list new=True found=True
Gemini CLI   BACKED token=/skills list new=True found=True
Cursor       BACKED token=/help/customization/skills.md new=True found=True
opencode     BACKED token=/skills/<invented-r55-placeholder>/SKILL.md new=True found=True
explicit invocation forms found on the live page 7 of 7; new ground 7
exit 0
```

Why each token gets through (counter line numbers):
- `TOKEN_RE` (`:121`) is `^(?:[/$@#][A-Za-z<].*|...)$`. The `.*` accepts spaces and any trailing text. Any slash command, file path, URL path, `#` reference, `@` rule or `$VARIABLE` passes.
- The `_` arm accepts any identifier holding an underscore. That includes env-var names and a model-side tool name.
- The token only has to be a raw substring of the quote (`:358`), not a whole word.
- `norm` (`:284-289`) runs on the whole page: CSS, inline scripts and embedded JSON are all part of the text searched.
- `norm` also deletes `<...>` as if it were an HTML tag, on the quote side too. On markdown pages (`.md` routes) any words inside angle brackets in a quote are never checked against the page. The opencode row shows this.

§9 consequence: the committed shortcut control (`controls/C1-shortcut.txt`) only fabricates quotes, which is exactly what `--fetch` was designed to catch. It is not the cheapest control. W1 is cheaper (no fabrication, and pages the corpus already cites) and it passes. The receipt set therefore does not show that the predicate separates the claim from a cheap shortcut.

## Counterexample 2 — "new ground" re-scores knowledge held at base

World W3, sandbox commit `09053321c0df176097d63ad4f3e5fb3885743642`. The Codex row quotes the sentence base knowledge already holds (`corpus/knowledge/skill-overlap-levers-round51.md:26`: "explicit `$skill` invocation still works"), with the token's case flipped:

```
2026-10-22T23:16:25Z
Codex        BACKED token=$SKILL new=True found=True
explicit invocation forms found on the live page 4 of 4; new ground 4
exit 0
```

The live page has `$skill` in lowercase (`codex.html:966`). It passes because:
- `norm` lowercases both the page and the quote, so the quote does not have to be byte-exact.
- `new_ground` (`:371-374`) is a case-sensitive fixed-string test, so `$SKILL` is not counted as held.

The same rule turns a renamed placeholder or a longer variant into new ground:
- Base `SKILL.md:433` says Claude Code's "`/name` still works", and `:432` says VS Code is "manual `/` invocation only".
- `/skill-name` does not contain the substring `/name`, so the same form scores as new. World W2 below shows this.
- A suffixed token such as `/skill-name arg` would be new even if `/skill-name` were held. `TOKEN_RE` allows the space.

World W2, sandbox commit `f54cfd1654f59bf304e4515502c5bdd6d898e990`, uses real explicit forms: Claude Code, Copilot CLI and Cursor `/skill-name`, plus Codex `$skill-creator`. It prints `found on the live page 4 of 4; new ground 4`, exit 0 (2026-10-22T23:15:08Z). Two things about it:
- G counts clients, not distinct forms. Four "new ground" were earned by two strings, and three of those clients share one placeholder.
- Three of the four pages are already base SOURCES rows: S053, S021/S054 and S031/S038/S056.

What the new-ground haystack does not read (`base_texts`, `:178-183`): only `SKILL.md` and `corpus/knowledge/*.md` at base. It does not read the `corpus/SOURCES.md` anchor and teaches cells, `corpus/lessons/`, or the wave reports. In those, `activate_skill`, `/skills list` and `$CODEX_HOME` are held (for example `.ufo/waves/round-51/falsify/ReopenS029.md:76`, `.ufo/waves/round-54/build/SrcGeminiCLI.md:163`). The plan sentence describes the haystack accurately (Q31 holds there). The name "new ground" claims more than that haystack and that substring test can support.

## Counterexample 3 — the `_` arm admits the implicit path as the "explicit form"

The counter docstring allows "the tool the model calls" (`:7`, `:28-29`). For Gemini CLI that tool is the description-routed path, which is the opposite of what the Frontier row needs set aside:
- `geminicli.com/docs/cli/skills/` (fetched 2026-10-22T23:13:17Z, 200, 114,148 B, sha256 `b1789501…98640`), lines 202-203 with tags stripped: "When Gemini identifies a task matching a skill’s description, it calls the activate_skill tool."
- `raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/tools/activate-skill.md` (2026-10-22T23:17:13Z, 200, 1,515 B, sha256 `90abfd1b…fb30c`), lines 22-23: "The `activate_skill` tool is used exclusively by the Gemini agent. You cannot invoke this tool manually."

A Gemini row with `activate_skill` would pass the counter, count as new ground (absent from base `SKILL.md` and knowledge), and label the implicit signal as explicit. [INFERENCE] The same holds for any client whose skill tool name contains `_`.

## Is it a depth move or re-scoring held knowledge?

- Axis by surface (§9): it holds. AXES.md:11 defines depth as "decision tables with real thresholds, named error signatures, cited sources" with the test "A reader can act on SKILL.md alone". A new SKILL.md decision table with cited sources is that surface. The counter does not test the "act on it" half: the action cell only has to be non-dash text (`:317`, W1 used one constant phrase for every row), and the "What it does" cell is never read.
- Held at base: the per-client explicit forms are largely already in the lane.
  - `SKILL.md` § Overlap levers (`:428-435`) and `corpus/knowledge/skill-overlap-levers-round51.md:20-33` hold them for Claude Code ("`/name` still works"), VS Code ("manual `/` invocation only"; `user-invocable`), Codex ("explicit `$skill` invocation still works"), opencode ("still loadable by exact name") and omp (`/skill:`, `:82`).
  - All seven clients' skills pages except Cursor's are already SOURCES rows, several twice (S021=S054, S031=S038=S056, S024=S039=S059).
  - Genuinely unheld: the Cursor skills page as a source, and the Copilot CLI and Cursor `/skill-name` strings.
- Frontier fit: `corpus/README.md:95` names the step as "the intent-labeling pass on the proven join recipe". That recipe (`corpus/knowledge/trigger-miss-proxy-round6.md:5,13-16`) reads `opencode.db` and already strips slash-command tokens (`/skill:godspeed`, `/ufo`) as "invocation verbs, not router intent". C1 gives a seven-client lookup table that feeds that step but does not run it. For the one store the recipe reads, opencode documents a `/name` command only when a skill sets `opencode/slash` (`opencode.md:44`).
- [INFERENCE] As frozen, C1 is mostly a sourced re-statement of held per-client knowledge (breadth or reference work), with a small depth increment. The predicate cannot tell the two apart.

## What the predicate lets through that the plan sentence does not say (Q26, Q31)

The plan's Q31 paragraph (`plans/round-55.md:39-41`) names only listing or management commands, documented-versus-actual behaviour, and clients outside the seven. Unstated:
1. Built-in commands, file paths, URL paths, CSS at-rules, `#` context references and `$` env vars all satisfy the token rule (W1).
2. Model-side tool names, which are the implicit path, satisfy the `_` arm (Gemini).
3. The live-page haystack includes markup, CSS and script text.
4. The quote match ignores case, `*`, `_` and backticks, and drops `<...>` text on both sides. Quotes need not be byte-exact, despite the session rule.
5. A new id on a page already cited at base passes. Only the id is checked against base (`:331`), never the URL.
6. New ground is per string, case-sensitive and substring. Renamed placeholders, case flips and suffixed variants of held forms count, and G counts clients, not distinct forms.
7. The "What it does" cell is unread, and the action cell accepts any non-dash text.

Q26: the printed headline "explicit invocation forms found …" asserts explicitness. No counter output turns that on, and no guard with an exit code is cited. The plan names it as reviewer reading, which meets Q31, but Q26 also needs either a cited guard or a bounded statement.

## Impacted axes

- depth (C1 verdict): a pass is reachable without the claimed content (W1), and new ground can be inflated (W2, W3).
- consistency: the planned table would restate per-client explicit forms that § Overlap levers already carries. That makes two SKILL.md authorities for the same fact, which can drift, and `SKILL.md` is at 599/600 lines.
- calibration: a G that counts strings and clients overstates novelty.

## Smallest safe correction (counter untouched)

1. Before any C1 content lands (tip `ed3e899` has none), commit a plan erratum, as round 54 did with erratum 2 at `3b2535d2`. Under it, a row fails the claim even when the counter prints it as found if any of these hold:
   - (a) the form is not one a user types to invoke one named skill. That rules out listing or management commands, built-in commands, paths, URLs, markup, context references and model-side tools such as `activate_skill`.
   - (b) the quote is not byte-exact in the seat's sha256-recorded fetched bytes (case and angle-bracket text included).
   - (c) for new ground only: the source URL equals a base SOURCES row's URL, or the form, after case-folding and normalizing placeholders such as `<name>`/`skill-name`/`name`, is already in base `SKILL.md` or knowledge. Count G over distinct forms.
2. Commit W1 as a second §9 shortcut receipt. It is the cheapest control and the predicate passes it. Reproduce with `probe/build.py w1` on `a10240c0`, then run the counter with `--fetch`.
3. Read the C1 verdict on the counter AND the wave-2 per-row guard from item 1. If the guard drops F below 4 or G below 2, report C1 as a miss or as bounded, never as met.
4. Fold the new table into § Overlap levers, or cross-reference it from there, so one authority holds each client's explicit form.

Checks for the L1 to run: `python3 -B verifiers/check_explicit_invocation.py --self-test`, then the counter with `--rev <C1 rev> --fetch`. In wave 2, also run the per-row guard from item 1 against each found row's recorded bytes.
