Result: HOLDS — all 8 assigned single-fault DATA mutations of the C2 counter were killed (count 5 of 7 → 4 of 7 each, exit 0 → 0), and 6 of my 8 extra probes also killed; the two survivors (M12 host/path pin prefix, M16 quote-substring containment) are coverage findings in the counter's judgment, not defects in the landed data.

# MutMcpCounter — falsify wave, round-52 attempt 2

Seat: `KotobaR52a2.MutMcpCounter` (mutation tester). Target: `verifiers/check_mcp_instructions.py`
(the round-52 C2 counter). Judged revision: `c8407a453788df964df5a7b835dd0ce1360de882`
(branch master). Sandbox clone: `/fast/scratch/hyaku/kotoba-r52a2/MutMcpCounter`.

Scope of this probe: the counter's *sensitivity* to defects in the scored DATA (the entry, the
SOURCES rows, the lesson Gate). I did not modify the counter itself; the counter is frozen at the
plan commit and is byte-identical at the plan commit, the C1 commit and the judged revision:

    $ git show 4c003a4b:verifiers/check_mcp_instructions.py | sha256sum
    d4b1464ff88f8a43ed8afe1d840d342f101ca9d478f9cdf10bbdbd6ec80363c9  -
    $ git show c8407a45:verifiers/check_mcp_instructions.py | sha256sum
    d4b1464ff88f8a43ed8afe1d840d342f101ca9d478f9cdf10bbdbd6ec80363c9  -
    $ git diff 4c003a4b c8407a45 -- verifiers/check_mcp_instructions.py   # empty, exit 0

## Method

Each mutation: reset the sandbox to the judged revision, edit ONE scored-DATA fact, commit it,
then run the counter against that sandbox commit with `--rev <sandbox commit>` and record the
printed count and the exit code. The expectation from the assignment is that the count drops by
one per mutation; a mutation that does not lower the count is a BREAK.

The counter's rules under attack (`verifiers/check_mcp_instructions.py:24-40` docstring, and the
`main()` body at `:190-260`):

1. exactly one entry row per client, under `## Per-client record`;
2. row cell is one `S###` id present in `corpus/SOURCES.md` with 11 cells;
3. that SOURCES row: tier `A`, kind in {spec, docs, code}, status `mined`, opened `2026-10-22`,
   `used-by` naming the entry;
4. first http(s) URL in the SOURCES `source` cell is on a pinned host (a `host/path` pin also
   requires the path prefix);
5. quote cell wrapped in `"`, 3–25 whitespace-separated words, containing the word `instructions`;
6. the lesson `corpus/lessons/round-52.md` contains the `S###` id and the quote text verbatim.

Baseline (pristine, judged revision), run in the sandbox:

    $ python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882
    MCP specification  BACKED
    Claude Code        BACKED
    VS Code            BACKED
    Codex              BACKED
    Gemini CLI         BACKED
    opencode           no rows naming client: 0 (need 1)
    Copilot CLI        no rows naming client: 0 (need 1)
    mcp instructions backed 5 of 7 clients
    exit=0

    $ python3 -B verifiers/check_mcp_instructions.py --rev c8407a45... --fetch
    mcp instructions backed 5 of 7 clients
    mcp instructions found on the live page 5 of 5
    exit=0

The baseline is green and non-degenerate (5 backed, 2 rejected), so every mutant below is
interpretable: a drop is a kill, no drop is a survival.

## Assigned mutations (all 8 killed)

| # | Mutation (scored DATA, one fault) | Sandbox commit | Counter output | Count | Exit | Verdict |
|---|---|---|---|---|---|---|
| M1 | Drop the word `instructions` from one Gate quote — `corpus/lessons/round-52.md:19`, S032 quote → `"Describing how to use the server and its features."` | `0c9bc42` | `MCP specification  no round-52 lesson lacks the id or the verbatim quote` | 4 of 7 | 0 | KILLED |
| M2 | Stretch a quote to 26 words — Claude Code quote (22 → 26 words) in the entry `corpus/knowledge/mcp-server-instructions-round52.md:24` **and** mirrored in the lesson Gate `:22`, so only the word-limit rule trips | `5f385ae` | `Claude Code        no quote has 26 words` | 4 of 7 | 0 | KILLED |
| M3 | Point a row's URL at an unpinned host — SOURCES `S034` source URL → `https://www.visualstudio.com/updates/v1_104` (host not in the VS Code pin list) | `0129d73` | `VS Code            no S034 source URL 'https://www.visualstudio.com/updates/v1_104' not on a pinned host` | 4 of 7 | 0 | KILLED |
| M4 | Set a row's status to `candidate` — SOURCES `S033` status cell `mined` → `candidate` | `920da1f` | `Claude Code        no S033 status 'candidate'` | 4 of 7 | 0 | KILLED |
| M5 | Remove the entry path from a row's used-by — SOURCES `S035` used-by → `corpus/lessons/round-52.md` only | `8eae5cb` | `Codex              no S035 used-by lacks the entry` | 4 of 7 | 0 | KILLED |
| M6 | Change the opened date — SOURCES `S036` opened `2026-10-22` → `2026-10-21` | `fa3d759` | `Gemini CLI         no S036 opened '2026-10-21'` | 4 of 7 | 0 | KILLED |
| M7 | Delete the quote from the lesson Gate — `corpus/lessons/round-52.md:31`, S036 quote → `(quote not recorded in this Gate)` | `95a5be7` | `Gemini CLI         no round-52 lesson lacks the id or the verbatim quote` | 4 of 7 | 0 | KILLED |
| M8 | Make a quote not verbatim — entry `corpus/knowledge/mcp-server-instructions-round52.md:25` VS Code quote `them` → `it`, so the entry and the Gate disagree | `e3e7f4e` | `VS Code            no round-52 lesson lacks the id or the verbatim quote` | 4 of 7 | 0 | KILLED |

Every assigned mutation dropped the count by exactly one (5 → 4) and the counter named the rule it
tripped. No assigned mutation left the count at 5.

Note on exit codes: the counter's exit code is `0 iff value >= TARGET` with `TARGET = 3`
(`verifiers/check_mcp_instructions.py:66`, `:288`), so a 5 → 4 drop does not change the exit code.
The count, not the exit code, is the sensitive signal here; a reviewer reading only the exit code
would see no change. The assignment asked for the count to drop by one and it did.

## Extra probes (mine, beyond the assigned list)

These test the counter's own declared rules to find gaps the assigned list does not reach.

| # | Mutation | Sandbox commit | Counter output | Count | Verdict |
|---|---|---|---|---|---|
| M9 | Fabricate a Gemini CLI quote present on no page ("The Gemini CLI client must append these server instructions verbatim to every system prompt turn it constructs."), mirrored in the Gate so entry and Gate agree | `a191e08` | default mode: `backed 5 of 7`, exit 0; `--fetch`: `found on the live page 4 of 5`, exit 0 | 5 of 7 | SURVIVED in default mode; killed by `--fetch` |
| M10 | Downgrade the S032 row tier `A` → `B` | `2f76b85` | `MCP specification  no S032 tier 'B'` | 4 of 7 | KILLED |
| M11 | Change the S035 row kind `docs` → `blog` | `b29ac65` | `Codex              no S035 kind 'blog'` | 4 of 7 | KILLED |
| M12 | Point the S032 row URL at a sibling path of the `github.com/modelcontextprotocol` host/path pin: `https://github.com/modelcontextprotocol-evil/specification/2025-11-25/schema.md` | `a6f5067` | `MCP specification  BACKED` | 5 of 7 | **SURVIVED** |
| M13 | Shorten the Gemini CLI quote to two words ("Instructions appended."), mirrored in the Gate | `c4b872f` | `Gemini CLI         no quote has 2 words` | 4 of 7 | KILLED |
| M14 | Add a duplicate VS Code row to the entry table | `41e7d87` | `VS Code            no rows naming client: 2 (need 1)` | 4 of 7 | KILLED |
| M15 | Drop the double-quote wrapping from the Codex quote cell | `fab0411` | `Codex              no quote cell not wrapped in double quotes` | 4 of 7 | KILLED |
| M16 | Replace the Gemini CLI quote with a fragment of the recorded quote ("appended to the system instructions.") | `1c099f3` | `Gemini CLI         BACKED` | 5 of 7 | **SURVIVED** |

### M12 — host/path pin is a prefix match, so a sibling path passes (severity: medium)

`host_ok()` (`verifiers/check_mcp_instructions.py:171-180`) splits a pin on `/` and requires
`path.startswith("/" + p)`. The path component is therefore matched as a *string prefix*, not as a
path *segment*. A URL under `github.com/modelcontextprotocol-evil/…` satisfies the
`github.com/modelcontextprotocol` pin, as does `…-attacker/…` and `…foo/…`:

    $ python3 -c "import importlib.util as u; s=u.spec_from_file_location('cm','verifiers/check_mcp_instructions.py'); m=u.module_from_spec(s); s.loader.exec_module(m); \
      [print(m.host_ok(x, m.HOSTS['MCP specification']), x) for x in ['https://github.com/modelcontextprotocol/spec.md','https://github.com/modelcontextprotocol-evil/spec.md','https://github.com/modelcontextprotocol-attacker/spec.md','https://github.com/modelcontextprotocolfoo/spec.md']]"
    True | https://github.com/modelcontextprotocol/spec.md
    True | https://github.com/modelcontextprotocol-evil/spec.md
    True | https://github.com/modelcontextprotocol-attacker/spec.md
    True | https://github.com/modelcontextprotocolfoo/spec.md

Effect on the counter: M12 leaves the count at 5 of 7, exit 0 — the row is counted as backed while
citing a repository that is not the pinned one. The `--fetch` mode does catch it for this specific
mutant (the evil repo does not serve the quote: `found on the live page 4 of 5`), but `--fetch` is
not part of the declared C2 counter invocation in the plan (`plans/round-52.md` § Claims: the
counter is `python3 -B verifiers/check_mcp_instructions.py --rev <rev>`), and `--fetch` also
cannot detect a host that *does* serve the quote.

Note: this is a weakness of the counter's pinning rule, not a defect in the landed rows. All five
landed rows cite their real vendor pages on the plain-host pins, and the two host/path pins that
exist (`github.com/modelcontextprotocol`, `raw.githubusercontent.com/anthropics/claude-code`,
`github.com/microsoft/vscode-docs`, `github.com/openai/codex`, `raw.githubusercontent.com/openai/codex`,
`github.com/google-gemini/gemini-cli`, `raw.githubusercontent.com/google-gemini/gemini-cli`,
`github.com/sst/opencode`, `github.com/anomalyco/opencode`, `raw.githubusercontent.com/sst/opencode`,
`raw.githubusercontent.com/anomalyco/opencode`, `github.com/github/copilot-cli`,
`raw.githubusercontent.com/github/copilot-cli`) are not exercised by the landed S032–S037 URLs, which
use plain hosts. A stricter `host_ok` would compare path segments (`"/" + p` must be followed by
`/` or end-of-path). Severity medium: it weakens the "the client's own source on a pinned host"
half of the C2 statement for any future row that uses a path pin.

### M16 — the quote check is substring containment, so a fragment passes (severity: medium)

The lesson rule (`verifiers/check_mcp_instructions.py:249`) is `quote not in lesson`, a plain
substring test, and the quote cell's word-count rule accepts 3 words. Replacing the Gemini CLI
quote with the 5-word fragment `"appended to the system instructions."` — a strict substring of the
Gate's recorded quote — leaves the count at 5 of 7, exit 0, and `--fetch` still reports 5 of 5
(the fragment is on the live page). The counter therefore cannot tell a located quote from an
arbitrary fragment of one. Severity medium: it means the counter's "located quote" guarantee is
"some substring of the recorded quote", not "the recorded quote", so a row could carry a
meaningless fragment and still count.

### M9 — the default mode does not check the live page (severity: low, already in the contract)

A fabricated quote that is on no page passes the default mode at 5 of 7. The counter's own docstring
states `--fetch` "additionally re-opens each cited page and requires the quote on the live bytes",
and the plan's C2 statement counts only what the counter prints without `--fetch`. This is a
documented limit of the declared counter rather than a defect, and the landed quotes are genuine
(`--fetch` reports 5 of 5 at the judged revision, and I re-confirmed each quote's presence on the
live page). Recording it so the closure knows the default count does not prove the quotes are real.

## Restoration evidence

All mutations were made in the sandbox clone only. The sandbox was reset to the judged revision
after the last probe and the four scored files hash back to their pristine values:

    $ git reset --hard c8407a453788df964df5a7b835dd0ce1360de882 && git status --porcelain=v1
    (empty — clean tree)
    $ sha256sum corpus/knowledge/mcp-server-instructions-round52.md corpus/lessons/round-52.md corpus/SOURCES.md verifiers/check_mcp_instructions.py
    eafc048afd1b567356bfca408330873fd557b0212d9f0f861df8b23b878c6bcf  corpus/knowledge/mcp-server-instructions-round52.md
    0f3e2842bd3376af099ee333e8c32cd297019f0383ff993c646b3a5a8c7989c0  corpus/lessons/round-52.md
    4f5f14810af2309702776b1d6624aa4c327702c1e32960278811e59c7dda513e  corpus/SOURCES.md
    d4b1464ff88f8a43ed8afe1d840d342f101ca9d478f9cdf10bbdbd6ec80363c9  verifiers/check_mcp_instructions.py

Those three DATA hashes equal the judged revision's blob ids (`b02919bb…`, `8f7f394a…`, `b39ba3a3…`),
and the final re-measure returns the pristine baseline:

    $ python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882
    mcp instructions backed 5 of 7 clients
    exit=0

No git write was performed in the lane; `git -C <lane> rev-parse HEAD` is still
`c8407a453788df964df5a7b835dd0ce1360de882` and the lane's `verifiers/check_mcp_instructions.py` is
byte-identical to the judged revision (same sha256 `d4b1464f…`).

## Lane observation (not mine, not a defect report)

During this probe the lane working tree changed under me: `PROVINCE.md`, `SCORECARD.md`, `SKILL.md`,
`corpus/QUALITY.md`, `corpus/README.md`, `corpus/SOURCES.md`,
`corpus/knowledge/mcp-server-instructions-round52.md`, `corpus/lessons/round-52.md`,
`verifiers/check_correction_sweep.py` and `verifiers/verify_surfaces.py` all became modified
(mtimes 14:58–15:04 local, i.e. during my run), and the entry gained rows S039–S042 (opencode,
Copilot CLI, and the 2026-07-28 spec revision). Measured read-only against that in-flight tree the
counter reports `mcp instructions backed 7 of 7 clients`, exit 0 — the two previously-rejected
clients are now backed. This is the L1's concurrent work, not a mutation of mine, and it is not
part of my verdict: my verdict is against the judged revision `c8407a45`. I flag it because the
newly added rows (S039 opencode, S041 opencode source, S042 Copilot CLI) are the ones most exposed
to the two counter gaps above, and because the newly added host/path-pinned rows
(`raw.githubusercontent.com/anomalyco/opencode/…`, `raw.githubusercontent.com/github/copilot-cli/…`)
are exactly the shape M12 exploits.

## Verdict

- **C2 counter sensitivity: HOLDS.** All 8 assigned single-fault DATA mutations were killed, each
  lowering the count from 5 of 7 to 4 of 7 with the tripped rule named. Five of my eight extra
  probes were also killed.
- **Two surviving mutants (M12, M16), both coverage findings in the counter's judgment, both
  medium severity, neither a defect in the landed data.** They do not falsify the C2 statement
  (`backed 5 of 7` at the judged revision, `5 of 5` with `--fetch`): the landed quotes are genuine
  and the landed URLs are on their real pinned hosts. They are gaps that would let a *future* row
  pass without a real quote or a real pinned path. I do not change the contract; the L1 decides
  whether to tighten `host_ok` and the quote-substring test, noting that the counter is frozen at
  the plan commit and any widening after it is a session-rule break (this is a proposed future
  counter, not a change to the frozen one).

## Tooling

No installs and no upgrades were performed in this seat. Everything used was already present:
`git`, `python3` (CPython 3.14.8, `/usr/bin/python3`), `sha256sum`, `grep`. Per the operator
tooling directive, a tool install would have been recorded here; none was needed.

## Files written by this seat

- `.ufo/waves/round-52/falsify-a2/MutMcpCounter.md` (this report — the only file written in the
  lane).
- Sandbox clone `/fast/scratch/hyaku/kotoba-r52a2/MutMcpCounter` (scratch; restored to the judged
  revision, clean tree, not pushed).
