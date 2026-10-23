Result: MIXED — the C1 v2 predicate is met at the tip as declared (`5 of 5; new ground 4`, exit 0), and no seat scored C1 content before erratum 1; but two of the four new-ground forms re-score forms the lane already held, which addendum §9 says is not depth; the entry misstates what the lane held; the erratum's "strictly stricter" claim is false for `--fetch`; and three sandbox worlds with no newly learned form still meet v2.

Seat: KotobaR55.CriticC1Landed (critic, wave 2 FALSIFY). Read-only on the lane; every run below was in my sandbox clone `/fast/scratch/hyaku/kotoba-r55/CriticC1Landed` (cloned from the lane, checked out at `f0e6b695`). Nothing was installed. No lane file was edited except this report.

## 0. The predicate at the tip (re-run)

The counter at the tip is the erratum v2 counter: sha256 `e13eb88d8cfc32fc8975968280aa5a0055416fb07e43facbf1f585d951787e5a`, identical to `b04a9005:verifiers/check_explicit_invocation.py`. The v1 counter at `a10240c0` is `4fc6e01a…`, which matches the hash recorded in `ReviewPlanControls.md:35`.

```
$ timeout 600 python3 -B verifiers/check_explicit_invocation.py --rev f0e6b695b746775823b65a8c45de7d50ea33e84f --fetch
Fri 23 Oct 2026 12:08:53 AM UTC
Claude Code  BACKED token=/skill-name new=False found=True
Codex        BACKED token=$setup-demo-app new=True found=True
VS Code      no quote does not contain the word skill
Copilot CLI  BACKED token=/frontend-design new=True found=True
Gemini CLI   no SKILL.md form cell has no backticked invocation token
Cursor       BACKED token=/skill-name new=True found=True
opencode     BACKED token=@skill-id new=True found=True
user-typed invocation forms found on the live page 5 of 5; new ground 4
exit=0
```

`C1 predicate (v2): --fetch exit 0 (F>=4, G>=2)` — MET as declared at `f0e6b695`.

## 1. Is the depth axis named by the surface it changes (addendum §9)?

§9 is in the fleet repository at commit `4248e92`, file `scripts/hyaku/lane-addendum.md`. It says to name the axis by the surface the round changes, and that "Re-scoring a rule the lane already holds on new inputs … is quality work, never coverage or depth".

- **Naming holds.** The plan header names the surface (`plans/round-55.md:17-20`: a new SKILL.md decision table, a new entry and new SOURCES rows). The table has an action column and cited rows, which matches the depth definition in fleet `AXES.md:11` ("decision tables … cited sources").
- **Small scope slip.** The C1 commit `96155796` also changes `corpus/README.md` (10 lines: the corpus index and a Frontier note). The plan's causal-separability sentence (`plans/round-55.md:64-65`) lists only SKILL.md, the entry, SOURCES.md and the lesson Gate. The counter does not read README.md, so the verdict is unaffected.
- **Re-scoring.** Four of the seven table rows give forms that were held at base `f0e5de82`. This is the §9 re-scoring class:

| client | form held at base | where it was held at `f0e5de82` |
|---|---|---|
| Claude Code | `/name` | `SKILL.md:430` ("`/name` still works"); `corpus/knowledge/skill-overlap-levers-round51.md:23` ("the user can still run `/name`") |
| VS Code | `/` command | `SKILL.md:429` ("manual `/` invocation only"); `skill-overlap-levers-round51.md:22` ("the `/` command still works") |
| Codex | `$skill` | `skill-overlap-levers-round51.md:26` ("explicit `$skill` invocation still works") |
| Copilot CLI | `/SKILL-NAME` | `corpus/SOURCES.md` rows S031, S038 and S056 (S031 teaches cell: "`/SKILL-NAME` stays available"). The lane's own Gate states this: `corpus/lessons/round-55.md` § Gate › Rejected, first row |

- **What is new at base.** The new material is the Cursor per-skill `/skill-name` form (base held only the `/skills` listing command: `SKILL.md:190`, S058), the opencode V2 `@skill-id` mention (base held only "loadable by exact name", `SKILL.md:431`), the Gemini CLI distinction between the model's tool call and a user-typed form (not counted), and the action column's use of the forms as a measurement classifier. The base Overlap-levers table is about removal levers and has no such column.

Impacted axes: depth (how strong the C1 verdict is), and consistency/calibration (the claim says more than its evidence).

## 2. New ground or re-scoring held knowledge?

**Counterexample.** The counter reports `new ground 4`. Two of those four are held forms reached through a new page with a new example name:

- Codex `$setup-demo-app`: the `$skill` form is held at `skill-overlap-levers-round51.md:26`. Source S066 is a blog post with a new URL.
- Copilot CLI `/frontend-design`: the `/SKILL-NAME` form is held in S031, S038 and S056. Source S068 is a how-to page with a new URL.

The Gate's Rejected table refuses the base pages for exactly this reason ("re-citing it would re-score held knowledge", Codex row; "already rows S031, S038, S056 at base", Copilot row). The same forms were then admitted from new pages. The v2 new-ground rule only checks the literal token and the URL string (`check_explicit_invocation.py:438-446`), so a new example name on a new page scores as new.

Reading per client and per form under §9, the counted new ground at the tip is **2** (Cursor and opencode). That still meets G ≥ 2, but with no margin.

**The critic's fix was only partly adopted.** The wave-1 critic proposed normalizing placeholders for new ground (fix (c), `.ufo/waves/round-55/build/CriticC1Sizing.md:110`) and built world W2 for this class (`:57-63`). v2 adopted case-folding and the URL rule but not placeholder or example normalization. The erratum receipt `controls/C1-shortcut-W1W3.txt` covers W1 and W3 only. I ran W2 (`f54cfd16`, fetched into my sandbox from the CriticC1Sizing clone) under v2: `found on the live page 4 of 4; new ground 1`, exit 1. It fails only because W2's rows reuse base URLs. The landed content and my world A below avoid that by using new pages.

**The entry over-claims.** `corpus/knowledge/explicit-invocation-round55.md` § Relation to what the lane already held says round 51 "did not hold … the Copilot CLI, VS Code, Cursor and opencode forms". That is false for VS Code (`SKILL.md:429`, round-51 `:22`) and false for Copilot CLI (S031, S038 and S056, as the same round's Gate says). The section also leaves out that Claude Code's `/name` was held (`SKILL.md:430`). This is the over-wide record defect again (rounds 50-54).

## 3. Was erratum 1 a rule change after data?

**Commit order** (`git log f0e5de82..f0e6b695`): `a10240c0` (plan, committed 20:11:10 -03:00) → `ed3e8996` → `b04a9005` (erratum; authored and committed 20:22:16 -03:00 = 23:22:16Z) → `96155796` (C1 content; authored 20:22:16, committed 20:23:49 -03:00). The order is linear, and the C1 content commit comes after the erratum.

**The data existed before the rule.**
- The new SOURCES rows record fetch times from 23:12:21Z to 23:15:25Z (`corpus/SOURCES.md:78-84`).
- The seven source-seat reports have lane mtimes from 20:14:45 to 20:17:33 -03:00 (`stat`, `.ufo/waves/round-55/build/Src*.md`).
- The v2 receipts have mtimes 20:21:48 and 20:22:00.

So the quotes and rows were in hand while v2 was written. The plan admits this: "the L1 had read their draft rows" (`plans/round-55.md:101-102`).

**No seat scored C1 content before `b04a9005`.** Every source seat records only `--self-test`:
- `SrcClaudeCode.md:65`, `SrcCodex.md:64`, `SrcCopilotCLI.md:62`, `SrcCursor.md:46`, `SrcGeminiCLI.md:50,54`, `SrcVSCode.md:48`, `Srcopencode.md:50`.
- `CriticC1Sizing` scored only its own sandbox worlds (W1, W2, W3). `ExecEnvSweep.md:168` ran `--root` on broken scratch trees. `MutC1Counter.md` (mtime 21:02) is after the erratum.

So the §9 test "a rule changed after any seat has scored" is **not crossed**. Erratum 1 stands formally.

**The justification for the erratum is false.** Erratum 1 is licensed by "every v2 rule only adds a failure" (`plans/round-55.md:101-103`), and the docstring says "every client it backs, v1 also backs" (`check_explicit_invocation.py:79-80`). That holds for backing without `--fetch`, but not for the `--fetch` match. v1 removed `<…>` text from both the quote and the page *before* unescaping HTML entities. v2 keeps angle text in the quote and unescapes after removing page tags. So a quote with angle text that the page writes as `&lt;…&gt;` is found by v2 and missed by v1:

```
$ timeout 60 python3 -B -c '<load v1 = a10240c0 counter, v2 = b04a9005 counter; compare norm(q) in norm(page) vs norm(q) in norm_page(page)>'
'use <b> /x-y skill now' v1 found: False | v2 found: True
'type /x-y <name> skill' v1 found: False | v2 found: True
exit=0
```

(The pages were `<p>use &lt;b&gt; /x-y skill now</p>` and `<p>type <code>/x-y</code> &lt;name&gt; skill</p>`.) No landed quote contains `<` (count 0 over the seven entry quote cells), so the tip result does not depend on this. It is a false statement in the erratum's own justification, not a change in the verdict.

## 4. Can a cheaper shortcut still meet v2?

Yes. I built three sandbox worlds on the tip (branch `shortcut-held` in my clone). Each one meets the frozen v2 predicate with **no form that was not already held at base**. Every quote is real text from a pinned host.

Fetch records:
- 2026-10-23T00:11:11Z: `https://code.visualstudio.com/docs/agent-customization/agent-skills.md`, HTTP 200, 23082 B, sha256 `26973567be23eb5756eb6db62afacf055455fbe6f427d40b45659aacb44d361a`. The quote spans lines 285-287; I stripped the backticks, as the counter's normalization does.
- 2026-10-23T00:12:09Z: `https://code.claude.com/docs/en/skills.md` and `…/slash-commands.md`, both HTTP 200, both 112748 B, both sha256 `909dd50ab595e5511d0c24e00527ec4f5ad9acc90e308f7df992c071b1ddc737`. These are byte-identical bytes under two URL keys. Quotes are at lines 639 and 675.

| world | sandbox commit | change from the tip | counter output | exit |
|---|---|---|---|---|
| A: held forms only | `8e768f70d62123cec756b3c6802e74e8735ba051` | Drop the Gemini CLI, Cursor and opencode rows. The VS Code quote becomes "select a skill to invoke it. You can add extra context after the slash command. For example, /webapp-testing for the login page" (22 words) | `found on the live page 4 of 4; new ground 2` | 0 |
| C: not an invocation form | `671aeeed1b252043167bca9423fbd28db0c153c1` | A, plus the Claude Code form becomes `` `$ARGUMENTS` `` (a substitution placeholder in the skill body), quote "Both you and Claude can pass arguments when invoking a skill. Arguments are available via the $ARGUMENTS placeholder." | `found on the live page 4 of 4; new ground 2` | 0 |
| B: alias URL | `205eb9854493d48b41f59e191518899eec74987b` | C, plus the S065 URL becomes `…/slash-commands.md` (same bytes as the base row `code.claude.com/docs/en/skills`), with Claude Code token `/migrate-component` from line 675 | `found on the live page 4 of 4; new ground 3`, Claude Code `new=True` | 0 |

Command for each world: `timeout 600 python3 -B verifiers/check_explicit_invocation.py --rev <commit> --fetch`. The runs were at 00:11:59Z, 00:12:35Z and 00:12:51Z.

What these worlds show:
- **A:** the predicate is reachable with zero learned forms. G = 2 comes entirely from the Codex and Copilot example-name re-scorings.
- **C:** a token that is not a "user-typed invocation form" passes v2's token rule and is counted in F. This is the W1 class surviving v2, on a placeholder that BUILTINS does not list.
- **B:** the URL rule compares URL strings, so a second route to the same page turns held knowledge into new ground.

`QUALITY.md` Q37 (added this round in `f2cc4099`) names "a case or placeholder variant of held knowledge" as a required before-data control. No receipt covers the example-name variant or the alias URL.

## Smallest safe corrections (reported only; the counter stays frozen; for the L1 to integrate)

1. **Verdict wording.** Keep `C1 predicate (v2) MET` and report beside it: "counter new ground 4, of which 2 re-score held forms (Codex `$`, Copilot CLI `/`); new under §9 per client: 2 (Cursor `/skill-name`, opencode `@skill-id`)". No depth band move should rest on G = 4.
2. **Entry fix.** Narrow § Relation to what the lane already held in `explicit-invocation-round55.md`: VS Code `/` and Claude Code `/name` were held in base SKILL.md § Overlap levers and the round-51 entry, and Copilot CLI `/SKILL-NAME` was held in S031, S038 and S056.
3. **Erratum text.** Append a note that the `--fetch` match is not monotone from v1 to v2 (angle text in quotes, entity-escaped pages), and that no landed quote depends on it. Do not keep "strictly stricter" unqualified.
4. **Next round's counter (a new measurement, not this one).** Read the base SOURCES teaches and anchor cells in the new-ground haystack. Judge novelty per (client, sigil form), with example names and placeholders normalized. Key held pages by content hash, not URL string. Add `$ARGUMENTS`-class placeholders to the non-form list. Commit receipts for worlds A, B and C as Q37 controls before data.

Checks for the L1: re-run `python3 -B verifiers/check_explicit_invocation.py --rev f0e6b695b746775823b65a8c45de7d50ea33e84f --fetch`, and run the same command on my three sandbox commits (they exist only in `/fast/scratch/hyaku/kotoba-r55/CriticC1Landed`). Process hygiene: the one background search I started was killed; no process of mine is left running.
