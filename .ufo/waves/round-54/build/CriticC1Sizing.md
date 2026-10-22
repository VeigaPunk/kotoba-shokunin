Result: MIXED — the counter's mechanics hold (frozen, starts at 0, exact host and quote matching, one source cannot serve two clients), but `4 of 7` is already reachable from rows and quotes the lane held before this round, so the claim cannot fail as a learning claim; four further attacks also reach the target with low-quality artifacts.

Seat: KotobaR54.CriticC1Sizing (critic, build wave). Counter read at the plan commit
`e33715486a45a4a857b64c30e6b695f7995858b8` (blob sha256 `4edad582…`). Sandbox clone
`/fast/scratch/hyaku/kotoba-r54/CriticC1Sizing` at `7ad05d34`. World builder (scratch):
`/fast/scratch/hyaku/kotoba-r54/CriticC1Sizing/.scratch/build_worlds.py`, worlds under `.scratch/worlds/`.
Each world holds only the four files the counter reads; SKILL.md is the plan-commit file plus a table,
SOURCES.md is the plan-commit file with the entry path appended to `used-by` (contract rule 2 allows that
in place). The table's "Past the threshold" and "Action" cells are `x` in every world. No installs, no
paid model calls, no lane edits other than this file.

## Summary

| # | Attack | Verdict | Impacted axes |
|---|---|---|---|
| 1 | Plan statement says nothing the counter does not check (Q26/Q31) | BREAKS (narrow, three clauses) | calibration |
| 2 | `4 of 7` can fail, and the claim covers new ground | BREAKS (the strongest counterexample) | depth, calibration |
| 3 | A number in another sense counts (name cap, rule length, the `1` of `1-1024`) | BREAKS | depth, calibration |
| 4 | An invented quote counts | BREAKS in the declared run; caught by `--fetch` but the exit code does not change | calibration |
| 5 | One source cited for two clients | HOLDS | — |
| 6 | Community or wrong-product content on a pinned host | BREAKS (issues, forum subdomain, any docs.github.com page) | calibration |
| 7 | SOURCES URL redirects off-host | HOLDS for the declared run; `--fetch` follows any redirect (small defect, no real case observed) | calibration (minor) |
| 8 | Freeze and before-value (Q28, Q19) | HOLDS | — |
| 9 | `--json` output | small defect: not valid JSON | operability (minor) |

## Baseline runs (the plan's before-value)

```
python3 -B verifiers/check_description_thresholds.py --rev <rev>   (sandbox, 2026-10-22T21:15Z)
  422ffd10 → "description thresholds backed 0 of 7 clients", exit 1
  e3371548 → "description thresholds backed 0 of 7 clients", exit 1
  7ad05d34 → "description thresholds backed 0 of 7 clients", exit 1
python3 -B verifiers/check_description_thresholds.py --self-test → "self-test: 0 failure(s) over 22 assertions", exit 0
```

## 2. `4 of 7` is met by what the lane already held — BREAKS (strongest counterexample)

Every SOURCES row from S016 to S052 is tier A, `mined`, opened `2026-10-22`, with 13 pipe fields (awk over
`git show e3371548:corpus/SOURCES.md`). Rounds 48 to 53 all ran on 2026-10-22, so the counter's
`OPENED = "2026-10-22"` (line 82) does not tell a round-54 row from a round-48 row. The docstring says
"a `corpus/SOURCES.md` row opened in round 54" (line 11); the code checks only the date (line 282).

Before this round the lane already recorded, verbatim and on each client's pinned host:

| client | row (host) | quote already recorded | where it was recorded |
|---|---|---|---|
| Claude Code | S022 (code.claude.com) | "truncated at 1,536 characters in the skill listing" | `.ufo/waves/round-48/build/C2ClaudeDocs.md:117`; finding 5 of `corpus/knowledge/skill-selection-rules-round50.md:47-48` |
| Codex | S021 (learn.chatgpt.com) | "By default, this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown." | `.ufo/waves/round-48/falsify/A17GateLines.md:30` |
| VS Code | S025 (code.visualstudio.com) | "Be specific about both capabilities and use cases to help Copilot decide when to load the skill. Maximum 1024 characters." | `.ufo/waves/round-50/build/SrcVSCodeSkills.md:103` |
| opencode | S024 (opencode.ai) | "`description` must be 1-1024 characters." | `.ufo/waves/round-48/build/C2CodexOpencodeDocs.md:76` |

SKILL.md at the plan commit already tells the author "`description` ≤1024 chars" (`SKILL.md:177`) and "stay
under 1,024 characters" (`SKILL.md:399`), and already carries a measured render row for opencode
("Full `description` byte-for-byte … no truncation", `SKILL.md:106`) and omp (`SKILL.md:105`).

World A (these four rows, these four quotes, `used-by` appended, no new row, no page opened this round):

```
python3 -B verifiers/check_description_thresholds.py --root .scratch/worlds/A-reuse-no-new-source
  Claude Code BACKED / Codex BACKED / VS Code BACKED / opencode BACKED
  description thresholds backed 4 of 7 clients          exit 0
... --fetch   (2026-10-22T21:19:32Z)
  description thresholds backed 4 of 7 clients
  description thresholds found on the live page 4 of 4   exit 0
```

So the target is met in both measurements by restating round-48 and round-50 findings in a new table. The
counter can still fail mechanically (0 at base), but the claim cannot fail *as learning*: the four clients the
lane already covers equal the target. Two of the four numbers (VS Code, opencode) are the open spec's
authoring maximum (S018 "Must be 1-1024 characters", already tabled by `frontmatter-rule-authorities-round48.md:44`).
They do not say how much of a description reaches the model, which is the Frontier half the plan says C1
works. The ground the lane does not hold yet is Copilot CLI, Gemini CLI and Cursor for skill descriptions,
plus listing budgets or cuts beyond the four rows above. [INFERENCE: from the grep of `corpus/knowledge`,
SKILL.md and the round 48–53 seat reports; I did not sweep those three clients' docs.]

Fixable or tradeoff: the counter is frozen, so this is a sizing tradeoff the canonical judge must weigh, not
something a seat can repair. Smallest safe correction (a second measurement reported beside the declared
one, which Q28 allows; no change to the counter): for each BACKED client, report
(a) whether its `S###` row is new, meaning `git show e3371548:corpus/SOURCES.md | grep -c '^| S0NN |'` prints 0, and
(b) whether its number is new, meaning `git grep -n -F '<number>' e3371548 -- corpus/knowledge SKILL.md`
finds nothing for that client. Read the depth credit on the count of clients that are new on both. If that count is 0, the judge
should refuse depth credit for C1 even when the counter prints 4 of 7 (CORPUS.md SOURCES rule 4: expansion
counts entries "on uncovered coverage-map ground").

## 1. Plan statement versus counter (Q26, Q31) — BREAKS, narrow

Every number and cell rule in the plan's C1 statement maps to a check in `judge()` (lines 239–304): the client
list, the heading and header, a number in the threshold cell, a non-empty action cell, 3–25 words, the same
number as a whole token, string equality with the Gate quote for the same `S###`, tier, kind, status, date,
`used-by`, and host. The before-value is reproduced. Three clauses go further than the code:

- "quotes … that same number **from** a tier-A `mined` … row": the declared run never compares the quote
  with the source's bytes; it only checks the row's fields (attack 4, world C). The plan's "does not measure"
  list does not name this; it mentions `--fetch` only as a second measurement.
- The printed line and the plan's "does not measure" list both assume the number is a *description*
  threshold ("whether a number is a render cut, a listing budget or an authoring maximum"). The counter does
  not check that the number concerns the description at all (attack 3, world B).
- "the learning claim" and "C1 works the Frontier row Per-render consumption" are coverage claims that no
  counter output turns on (attack 2, world A).
- In the counter's own prose, docstring line 11 says "opened in round 54"; the code checks a date shared
  with rounds 48–53. This is a Q31 defect in frozen text.

Smallest safe correction: the entry's Limits and the lesson state, as reviewer judgment, that the counter does
not check that the quote occurs in the source in the declared run, that the number concerns `description`,
that the row was opened in round 54 rather than on 2026-10-22, or that the page is vendor documentation.
Then report the new-ground count from attack 2 beside the declared line.

## 3. Numbers in another sense — BREAKS

```
world B-other-sense-numbers (Claude Code via S019 "Maximum 64 characters" — the name cap, bp.md:153;
Cursor via S052 "Keep rules under 500 lines" — rule files, `.ufo/waves/round-53/build/*ursor*.md:82`)
  Claude Code BACKED, Cursor BACKED (+ Codex, VS Code, opencode)
  description thresholds backed 5 of 7 clients          exit 0
world D-trivial-token (opencode threshold cell "1 skill"; quote "`description` must be 1-1024 characters.")
  opencode BACKED — the token "1" matches the lower bound of "1-1024"
  description thresholds backed 4 of 7 clients          exit 0
```

The number regex `\d[\d,]*(?:\.\d+)?%?` (line 107) and `has_token` (line 218) accept any number in the cell
that also appears in the quote, so a one-digit token or a date part such as `10` from `2026-10-22` also
counts. The entry's `reading` cell is never read. Fixable by reviewer reading: the falsify wave checks every
BACKED row's reading against the quote and refuses rows whose number is not a description limit.

## 4. An invented quote — BREAKS in the declared run

```
world C-fabricated-quote (adds Gemini CLI, S029, "Gemini CLI truncates each skill description at 4,096 characters"
— invented; recorded identically in the entry and the Gate)
  declared: Gemini CLI BACKED; description thresholds backed 5 of 7 clients     exit 0
  --fetch (2026-10-22T21:19:32Z): Gemini CLI BACKED found=False
            description thresholds found on the live page 4 of 5               exit 0
```

The Gate is written by the same author as the entry, so the string equality check (line 298) shows
consistency between the two, not that the quote came from the source. `--fetch` catches the invention, but its exit code
stays 0 whenever 4 other quotes are found, so it cannot falsify one client's provenance. Fixable: the
lesson Gate records URL, UTC time, HTTP status, bytes and sha256 per row (contract rule 1); report `found F of K`
beside the declared line, and treat any BACKED client with `found=False` as a refused row, not as noise.

## 5. One source cited for two clients — HOLDS

```
python3 -B (import check_description_thresholds): every pin of every client probed against every other
client's pins with host_ok() → no overlap ("overlap scan done", no OVERLAP line)
host_ok("https://github.com/microsoft/vscode-docs-fork/x", VS Code) → False   (whole path-segment prefix)
host_ok("https://code.claude.com.evil.io/docs", Claude Code)       → False   (sibling host)
```

The host sets are disjoint and the duplicate-row checks (lines 250, 260) allow one row per client, so one
`S###` cannot back two clients. Two rows with the same URL (as S031 and S038 already are) can still be cited by only one
client, because the host decides the client.

## 6. Community or wrong-product content on a pinned host — BREAKS

```
host_ok("https://github.com/anthropics/claude-code/issues/99999", Claude Code)   → True
host_ok("https://github.com/google-gemini/gemini-cli/discussions/1", Gemini CLI) → True
host_ok("https://github.com/sst/opencode/pull/1", opencode)                      → True
host_ok("https://forum.cursor.com/t/anything/1", Cursor)                         → True
host_ok("https://docs.github.com/en/actions/writing-workflows", Copilot CLI)      → True
host_ok(S027's Copilot cloud-agent URL, Copilot CLI)                              → True
world E-issue-thread-on-pinned-host (Claude Code via an issue URL, tier "A", invented user comment)
  Claude Code BACKED; description thresholds backed 4 of 7 clients              exit 0
```

The repo pins (`github.com/<org>/<repo>`) cover issues, pull requests and discussions written by anyone. The
bare-host pins admit every subdomain (line 192: `host.endswith("." + h)`), including a forum. `docs.github.com`
covers every GitHub product, so a Copilot cloud-agent or SDK page counts as Copilot CLI. Tier `A` is the
author's own label. Q32 asks for "host equality plus a whole path-segment prefix"; the subdomain rule is
wider than that wording, and the self-test asserts it passes ("subdomain pin passes", line 385). Fixable
by the reviewer, since the counter is frozen: the falsify wave confirms that each BACKED row's URL is a vendor
docs or changelog page for that client's product, not an issue, forum or other product's page. Record the subdomain rule as a known
counter limit against Q32.

## 7. Off-host redirect — HOLDS for the declared run; small defect in `--fetch`

The declared run never fetches; it judges the recorded URL string only, so a redirect cannot change it.
`fetch()` (lines 233–236) uses `urllib.request.urlopen`, which follows redirects, and nothing checks the final
host (`grep -n -E 'geturl|redirect|HTTPRedirect'` → no match, exit 1). Local probe: `localhost:<p>/docs` answering
302 to `127.0.0.1:<q>/page` → `fetch()` returned the second host's body and the quote was "found" (True).
Real pinned URLs, curl `-L` at 2026-10-22T21:19:46Z: docs.cursor.com → cursor.com, docs.anthropic.com and
docs.claude.com → code.claude.com, github.com/sst/opencode → github.com/anomalyco/opencode,
developers.openai.com → learn.chatgpt.com. Each stays within the same client's pins, and five other pinned URLs
answer 200 with no redirect. So I observed no real case that leaves a client's pins. Smallest correction: the SOURCES row records the
final URL after redirects (S013 and S051 already note their 308 and 301).

## 8. Freeze and before-value (Q28, Q19) — HOLDS

`git cat-file -e 422ffd10:verifiers/check_description_thresholds.py` → exit 128 (absent at base);
`git diff --quiet e3371548 7ad05d34 -- verifiers/check_description_thresholds.py` → exit 0 (unchanged at
tip). The enabling commit touches only `SKILL.md` and `verifiers/README.md`. The self-test carries the Q32
must-fail arms (sibling host `code.claude.com.evil.io`, line 359; Gate fragment, lines 363–365).

## 9. `--json` is not valid JSON — small defect

`--json` prints the JSON object and then the line `description thresholds backed …` (line 438 runs
unconditionally), so `json.load` fails with "Extra data: line 95 column 1" (world A and world C with
`--fetch --json`). Frozen; anyone reading the JSON should cut it at the closing brace or read the plain-text line.

## What the judge should weigh

- The counter correctly checks the table's *shape and consistency*. It does not show *learning*. With the
  target sized at 4, the table can be filled from rows that rounds 48 and 50 already hold (world A, live-checked
  4 of 4). This is premature saturation: a tradeoff the canonical judge must reject for depth credit unless the
  new-ground count reported beside the declared line (attack 2) is at least 1.
- Attacks 3, 4 and 6 are fixable defects for reviewers: the falsify wave reads each BACKED row's quote, host and
  reading, and the entry's Limits say the counter does not check them (Q31).
