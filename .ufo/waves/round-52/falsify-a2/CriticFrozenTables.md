Result: MIXED — the frozen-counter rule HOLDS on all three attacks (no counter file or judgment table changed after 4c003a4b, no tunable table is read from the measured tree for C1, no C2-scored content predates the freeze), but the uncommitted SCORECARD.md diff misdescribes the frozen C2 counter as checking the location cell, which it never reads.

Seat: KotobaR52a2.CriticFrozenTables (critic, falsify-a2). Judged revision c8407a453788df964df5a7b835dd0ce1360de882; plan commit 4c003a4b9c7dae8ebb8ad34bbc14cd1706febeeb; base c8579a4c5b48789e56fb9060ddd48f33569e1215; C1 c2107ecff4d257f91757dcc6a57bf23031bd85a9.
Counter runs were done in my sandbox clone /fast/scratch/hyaku/kotoba-r52a2/CriticFrozenTables (HEAD c8407a45). Only read-only git and jj (`--ignore-working-copy`) commands ran in the lane.
Tooling: no installs or updates.

## Attack 1 — did a counter file or any judgment table it reads change in 4c003a4b..c8407a45? HOLDS

Inputs of each counter, read from the source:

- `verifiers/check_callee_rename.py`:
  - In-script pins: `FIXTURE_REV = "c8579a4c…"` (:61), `CASES` (the 4 fixture/baseline/inventory triples, :66-71), `OC_FIXTURE` (:72), `BASE_CALLEES` (19 names, :74-75), `GENERIC_CALL_RE` (:76-80), `PLANT_PAIR`/`PLANT_ID` (:81-82), `CHECKS` (:83), and the fresh-name pool and rename rule (:95-124).
  - File inputs: 8 fixture files under `verifiers/fixtures/surfaces/`, read with `git show c8579a4c:<path>` at :158 (a hardcoded SHA, never the measured revision). The only input taken from `--rev` is `verifiers/verify_surfaces.py`, which is the artifact being measured (:160-161).
- `verifiers/check_mcp_instructions.py`:
  - In-script pins: `ENTRY`/`SOURCES`/`LESSON` paths, `TARGET = 3`, `OPENED = "2026-10-22"`, `WORD = "instructions"`, `MAX_WORDS = 25`, `CLIENTS` (7), `HOSTS` (per-client host/path pins) and `HEADER` (:62-90).
  - Inputs read from `--rev`: the entry, `corpus/SOURCES.md` and `corpus/lessons/round-52.md` (:184-186). These are the scored content; see attack 2.

Commands (lane, read-only):

```
$ git diff --stat 4c003a4b c8407a45 -- verifiers/check_callee_rename.py verifiers/check_mcp_instructions.py
(empty)  exit=0
$ git diff --stat c8579a4c c8407a45 -- verifiers/fixtures/
(empty)  exit=0
$ git rev-parse <rev>:<f> ; git hash-object <f>
check_callee_rename.py    P=f50297fb… H=f50297fb… working-tree=f50297fb…
check_mcp_instructions.py P=0023d8f5… H=0023d8f5… working-tree=0023d8f5…
```

- The fixtures are unchanged in base..head. Even if they had changed, the counter would not see it, because it reads them at the hardcoded `c8579a4c`.
- The plan commit's jj history (`jj --ignore-working-copy evolog -r 4c003a4b`) has predecessors `bc519eaa` and `8733198b`, both at 12:57:28-03:00. Both carry the same counter blobs (`f50297fb…`, `0023d8f5…`). The earlier snapshot `c9529557` (12:47:18-03:00) has neither counter. So no earlier, different counter bytes exist in the lane history.
- Two guard tables did change after the plan: `verifiers/floors-registry.json` (`surfaces` floor 119 → 129) and `verifiers/check_assertion_floors.py` (the same number in 4 places, `git diff 4c003a4b c8407a45`).
  - These are no-harm guards, not tables either counter reads.
  - The change tightens rather than widens: a higher floor means more self-test assertions are required.
  - Not a BREAK.

## Attack 2 — does the frozen counter read anything from the measured revision that the C1/C2 work could tune to pass?

### C1: HOLDS

- The gate from `--rev` is copied alone into a temp directory (:159-161). The counter passes `--repo <tmp>/fixtures`, `--baseline` and `--inventory` explicitly, all from the frozen fixtures (:127-130).
- The new admission rule takes its declared pairs from the baseline file. At c8407a45, `main` calls `declared_loader_pairs(entries, h)`, where `entries` comes from `--baseline`. A frozen fixture therefore decides admission, not a table in the measured tree.
- The gate's own defaults are never used in a counter run:
  - `DEFAULT_REPO` and `FIXTURES` (verify_surfaces.py:160-161) resolve into the temp directory.
  - The `surfaces-baseline.json` and `DEFAULT_INVENTORY` fallbacks in `main` apply only when the flags are absent, and the counter always passes them.
- No counter data is hardcoded in the gate. `grep -nE 'rnplant|RNPLANT|"evil"|EVIL|ascii_uppercase|random|seed'` on the c8407a45 gate finds only a comment (:226) and self-test lines (:1185, :1202).
- Seed sweep in the sandbox, `--rev c8407a45`:
  - Seeds 7, 1234, 1, 2, 3, 5, 11, 13, 99, 100, 4242 and 31337 each print `callee-rename robust 4 of 4 fixtures`.
  - At c2107ec, seeds 7 and 1234 print 4 of 4 with exit 0.
- Before and after values reproduce:

| Revision | Output | Exit |
|---|---|---|
| c8579a4c | `0 of 4` | 1 |
| 4c003a4b | `0 of 4` | 1 |
| c2107ec | `4 of 4` | 0 |
| c8407a45 | `4 of 4` | 0 |

### C2: HOLDS on the frozen rule, with three tradeoffs or latent defects (none changes the count)

- **Tradeoff T1, low: the counter reads self-attested judgment cells from the measured tree.**
  - The `tier`, `kind`, `status`, `opened` and `used-by` cells of the cited `SOURCES.md` row (:211-221) are written by the same C2 commit.
  - The Gate-record check ("the lesson contains the id and the verbatim quote", :234) is circular, because the C2 author writes both files.
  - The plan declared these reads (plans/round-52.md:43-44), so this is not a widening. But no file outside the measured tree vouches for "tier A".
  - Counterexample: relabeling a row to tier `A` satisfies the counter. No counted row currently relies on this, since S037 (blog) is honestly tier `B` and is not counted.
  - The only external check is `--fetch`, which I ran: sandbox, 2026-10-22T17:52:43Z, `--rev c8407a45 --fetch` printed `backed 5 of 7`, `found on the live page 5 of 5`, exit 0.
  - Impacted axis: coverage (the claim is bounded to "format-conforming, quote on the live page").
- **Latent defect L1, low, frozen: the host-pin path prefix has no boundary, and any subdomain matches.** Probe of the frozen `host_ok` in the sandbox (exit 0):
  - True for MCP specification with `https://github.com/modelcontextprotocolX/evil/...`, a different GitHub owner.
  - True for MCP specification with `https://gist.github.com/modelcontextprotocol-fan/abc`.
  - True for Codex with `https://github.com/openai/codex-universal/...`.
  - True for Codex with `https://developers.openai.com/api/docs/guides/tools-connectors-mcp`, which is not Codex documentation.
  - True for Copilot CLI with `https://docs.github.com/.../coding-agent/extend-coding-agent-with-mcp`, which is not CLI documentation.
  - None of the 5 counted URLs uses this. All are canonical client hosts with client-specific paths: S032 modelcontextprotocol.io/specification, S033 code.claude.com/docs/en/mcp.md, S034 code.visualstudio.com/updates/v1_104, S035 developers.openai.com/codex/mcp.md, S036 geminicli.com/docs/tools/mcp-server.md.
  - Smallest safe correction: none this round, since editing the frozen counter is itself a second measurement. Carry a boundary-checked pin (`path == "/"+p or path.startswith("/"+p+"/")`) into the next round's counter.
- **Latent defect L2, low: the frozen word rule does not tie the word to server instructions.**
  - The backed Gemini CLI quote is "which will be appended to the system instructions.". It contains `instructions` only through "system instructions".
  - Whether the quote supports the reading is reviewer territory (the plan says the counter does not measure meaning, plans/round-52.md:51).

## Attack 3 — did any C2-scored content land in the plan commit or before it? HOLDS

- `git show --stat 4c003a4b` lists exactly `plans/round-52.md`, `verifiers/check_callee_rename.py` and `verifiers/check_mcp_instructions.py`.
- `git cat-file -e` shows `corpus/knowledge/mcp-server-instructions-round52.md` and `corpus/lessons/round-52.md` absent at both c8579a4c and 4c003a4b.
- At 4c003a4b, `git show 4c003a4b:corpus/SOURCES.md | grep -nE '^\| *S03[2-8] '` exits 1 (no rows), and the entry path appears in that file 0 times.
- None of the 5 backed quotes or their source URLs occurs anywhere in the c8579a4c or 4c003a4b trees (`git grep -F -l`, 0 files each). The quotes were taken from `check_mcp_instructions.py --rev c8407a45 --json`.
- Timing:
  - Freeze: plan commit committer time 2026-10-22T15:57:28Z.
  - Recorded fetch times in SOURCES rows S032–S037 and the lesson (:17-37) run from 17:04:55Z to 17:07:03Z, all after the freeze.
  - The earliest round-52 artifact file is `.ufo/waves/round-52/build-spec.json`, mtime 13:00:19-03:00 = 16:00:19Z, also after the freeze.
- Host-pin provenance: most pinned hosts were already in the base tree from earlier rounds.

| Host | Files at c8579a4c |
|---|---|
| geminicli.com | 26 |
| anomalyco/opencode | 21 |
| code.claude.com | 51 |
| developers.openai.com | 29 |
| code.visualstudio.com | 25 |
| modelcontextprotocol.io | 0 |
| blog.modelcontextprotocol.io | 0 |

  - Where the two MCP pins came from is not recorded. [INFERENCE] The likeliest source is background knowledge, not peeking at data. No artifact predating the freeze shows either host. The blog pin cannot have helped the count, since S037 is tier B and is not counted.
- Before and after values reproduce:

| Revision | Output | Exit |
|---|---|---|
| c8579a4c | `backed 0 of 7` | 1 |
| 4c003a4b | `backed 0 of 7` | 1 |
| c2107ec | `backed 0 of 7` | 1 |
| c8407a45 | `backed 5 of 7` (opencode and Copilot CLI have 0 rows) | 0 |

## Attack 4 (secondary target) — uncommitted SCORECARD.md diff: BREAKS, severity medium-low

- **B1: false description of the frozen counter.**
  - `SCORECARD.md:30` (coverage cell, working tree only) says: "The counter checks location, length, the word `instructions`, host and Gate record".
  - The frozen counter never reads the location cell. It uses only `r[0]` (:195), `r[1]` (:201) and `r[2]` (:226). The `location` string is checked only as a header name (:90, :131).
  - The claim does not appear in any committed file: `git grep -i -E 'checks? (the )?location|location, length' c8407a45 -- ':!.ufo'` exits 1.
  - Impacted axes: coverage and calibration (false provenance of what was measured).
  - Smallest correction: delete "location," or write "length, the word `instructions`, host and Gate record; the location cell is not checked".
- **B2, low: the attempt-1 completion paragraph (SCORECARD.md, new text after the round-52 "Next" paragraph) says "the falsify wave ran on live roles only".**
  - The assignment record says the attempt-1 falsify wave was cut off by the 17:26Z restart and left no seat report.
  - Correction: say the attempt-1 falsify wave left no report and attempt 2 re-ran it.
- **Note, low:** the new "Next: round 53" paragraph lists the S024 superseding row and the fixture labels for lines 9, 15 and 33. Attempt 2 intends to land both, so the paragraph goes stale if they land.

## Pointers for sibling seats (out of my target, not tested)

- [INFERENCE] The C1 counter cannot tell the declared-admission rule apart from a simpler rule that admits any callee two or more characters long. The decoy callee `q` is one character, and every fresh and historical callee is two or three. The escape critic (KotobaR52a2.CriticC1Escape) is the right seat to probe it.
