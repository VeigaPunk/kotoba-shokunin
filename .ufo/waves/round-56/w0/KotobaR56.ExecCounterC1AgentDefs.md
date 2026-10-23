# Round 56 · w0 · KotobaR56.ExecCounterC1AgentDefs — frozen C1 (depth) counter

Counter `/fast/scratch/hyaku/kotoba-r56/KotobaR56.ExecCounterC1AgentDefs/check_agent_definitions.py`, sha256 `1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c` (1059 lines). A byte-identical copy sits at `<seat>/lane/verifiers/check_agent_definitions.py` and is the file the runs below used; integrate the same bytes at `<lane>/verifiers/check_agent_definitions.py`.
Reads: read-only `git -C <lane> show|grep` against the sandbox clone `<seat>/lane` (clone of the lane, holds b0b7140b); `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE` unset for every run; no claim content scored; no tool installed or upgraded.

## `--self-test` (exit 0)

`self-test: 0 failure(s) over 86 assertions`
Arms: token grammar (both spec examples, case-insensitive agent segment, dot-less and `agents.md` rejected), normalise (all three spec examples), boundary rule (`opencode.ai/docs/agents/` rejects `.ai/docs/agents`; letter/digit/`.`/`/`/`-` rejected; start/space/backtick/quote/`(`/`[` accepted), URL normalisation (`…/sub-agents.md` == `…/sub-agents`), quote word bounds 2/3/25/26, straight/curly quote stripping, agent-word-outside-token, the verbatim-location clause (glob token vs concrete quote path rejected, trailing-slash and `~/`-less forms accepted), duplicate SKILL.md rows, wrong headers, foreign heading, the whole judge on a synthetic world (base id, base URL, Gate miss, tier B, queued, other opened date, off-host, bad token, missing token, quote without path, quote without outside agent word), page normalisation and the found rule, Gate containment, host pins, grep-count summing.

## Base revision `b0b7140b` (exit 1)

`agent-definition locations found on the live page 0 of 0; new ground 0`
then seven client lines, each `SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client`.
`--rev b0b7140b` without `--fetch`: `agent-definition locations backed 0 of 0`, exit 1 (the non-fetch run is not the predicate).
`--rev deadbeef`: `could-not-evaluate: revision 'deadbeef' is not a commit in <lane>`, exit 2.
Cross-check of the new-ground rule against the plan's held forms (`git grep -i -F -c -e <form> b0b7140b -- . ':!.ufo'` summed): `.claude/agents` 3, `.codex/agents` 5, `.opencode/agent` 10, `.opencode/agents` 10; one base SOURCES row cites `sub-agents`. The plan's "held at base" statement therefore holds under this counter, and Claude Code/Codex/opencode rows cannot score new ground.

## Frozen predicate (docstring, verbatim in substance)

`python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch` exits 0 iff it prints `agent-definition locations found on the live page F of K; new ground G` with F >= 5 and G >= 2; receipt label `C1 predicate: --fetch exit 0 (F>=5, G>=2)`.

## Rules the spec left open — the choice taken

1. Lane path: parent of the script's `verifiers/` dir first (v2 rule); a copy outside the lane walks up for `SKILL.md` + `corpus/SOURCES.md`, then falls back to `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; never from the environment.
2. K counts CLIENTS not rows: exactly one SKILL.md row with a well-formed location token; a duplicate row disqualifies the client and drops it from K (K <= 7); the >=3-word action floor does not affect K.
3. Client-cell match: markdown emphasis/backticks stripped, case preserved, whole-cell equality ("exact match to CLIENTS"); no prefix or fuzzy match.
4. Entry rows: duplicates are declared disqualifying only for SKILL.md rows, so a client is backed if ANY of its entry rows satisfies every condition, first qualifying row as receipt (v2's exactly-one rule not re-imposed).
5. "that raw token appears in the quote": read as the raw location token itself (the plan's "quotes that path verbatim"), not only a token whose normalise() matches; the quote must carry the token case-insensitively, or its form without a leading `~/`, or without a trailing `/`. That keeps glob locations from passing on a different concrete file while a slash/`~/` spelling difference still backs.
6. Quote path tokens: maximal runs of `[A-Za-z0-9_.~/*_-]` with trailing sentence punctuation trimmed (a leading dot is never trimmed: it is what makes the dot-directory); the token must be well-formed by the frozen grammar before normalise() is compared. A path inside a URL never qualifies, because the scheme/host joins the run and the run then fails well-formedness.
7. Quote cell: one surrounding pair of straight or curly double quotes stripped when present; an unquoted cell is used as-is.
8. Backticks: stripped for the word count and for the matching normalisation (live page, Gate); the Gate check accepts the whitespace-normalised quote raw or backtick-stripped against the same normalisation of `## Gate`.
9. Gate scope: the whole `## Gate` section of `corpus/lessons/round-56.md` (to the next `## ` heading), not only the cited S### row — the spec says the quote "occurs in § Gate".
10. URL normalisation: lowercase scheme+host only (path case kept); trailing `/` stripped before a trailing `.md`; fragment/query dropped; the cited row's first URL is "its URL", every URL of a BASE_REV row joins the base set; trailing sentence punctuation trimmed from matched URLs.
11. Base count is the pinned `git grep -i -F -c <norm> BASE -- . ':!.ufo'` summed (git counts matching lines per file, not occurrences); exit 1 -> 0 hits, any other non-zero -> exit 2 (measured: `hyaku` 112 non-.ufo vs 2045 whole tree, so the exclusion is live).
12. Boundary predecessor: the spec's positive enumeration (start, whitespace, backtick, quote char, `(`, `[`) is enforced, so a preceding `,`/`:`/`=` is not a boundary; the weaker "i.e. not preceded by a letter, digit, `.`, `/`, `-`" restatement loses to the stricter enumeration.
13. Fetch token forms: raw token and its form without leading `~/`, each also passed through the page normalisation (drops `*`, `_`, backticks) so a glob location can match a page showing the glob; 30 s timeout, one retry; >5 MiB page or network failure = not found (exit 2 stays reserved for rev/git/file failures).
14. SOURCES row shape: v2's 11-column parse, any other field count is "absent or malformed"; only the spec's conditions are imposed — v2's kind and used-by conditions are not added because the frozen spec does not list them.
15. Entry "Location" cell: no condition is stated, so it is unconstrained (not even non-empty).
16. Output order: the exact output line first, then one line per client, per "Output line (exact): … Then one line per client" (v2 printed the summary last); `--json` is kept from v2 as an extra mode and changes neither the line nor the exit code.
17. A missing SKILL.md/entry/lesson at a revision is empty content (nothing backed), not an error, so the base revision exits 1 (not 2); exit 2 is only unknown revision, git failure, unreadable/undecodable file, or an unlocatable lane.
