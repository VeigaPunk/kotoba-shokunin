# ExecC1Counter — C1 counter draft (round-68 wave 1, executor seat)

Seat: executor (C1). Deliverable: the client-trust-gates counter, drafted — NOT installed
(`verifiers/` is the L1's). No lane git/jj state touched; no writes outside the two files below.

## Files written

1. **`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-68/w1/drafts/check_client_trust_gates.py`**
   — the counter (Python stdlib only, mirrors `verifiers/check_instruction_authority.py`'s shape).
2. This report.

## Contract conformance (all verified by execution below)

- `--rev <full-sha>` prints `client trust gates backed N of 5`; exit 0 ⟺ N == 5; exit 1 otherwise;
  exit 2 with `environment error: ...` on stderr for usage/environment only.
- `--repo <path>` override; default resolves to the nearest ancestor holding
  `corpus/SOURCES.md`, so the same file works from `drafts/` now and from `verifiers/` once
  installed (no edit needed at install time).
- `--fetch` re-opens each cited URL, strips script/style/tags, unescapes entities,
  whitespace/punctuation-folds both sides, and locates each id's anchor-bound quote. Network
  failures print `unreachable (<exc>)` — never counted as found, never silently dropped, and
  never moving the exit code (the fetch is a measurement; the verdict stays the content's).
- `--self-test`: fixture-built in a throwaway git repo under the system temp dir — needs no lane
  content (passes BEFORE the entry lands) and no network; asserts the R67-1 classification
  end-to-end through `main()`.

## The R67-1 classification, fixed

R67-1 reproduced live at the r67 base (contrast case, r67 counter unmodified):

```
$ python3 -B verifiers/check_instruction_authority.py --rev 2a8eba56b3f9321b70c569fa2816d42237ca49a2
environment error: cannot read corpus/knowledge/instruction-authority-ladder-round67.md at 2a8eba56b3f9321b70c569fa2816d42237ca49a2
exit=2
```

The r68 draft's rule (in the docstring, enforced in code): absence of a measured FILE at a
resolvable revision (entry, SOURCES.md, README.md) is a CONTENT verdict → `backed 0 of 5`, exit 1;
only failure to RUN the measurement (unknown revision, unreadable/non-git repo, git unavailable)
is exit 2. Verified at the pinned base `e94ae32a5cd8dc3ee8e2d247816784bec2750cc0`:

```
$ python3 -B .ufo/waves/round-68/w1/drafts/check_client_trust_gates.py --rev e94ae32a5cd8dc3ee8e2d247816784bec2750cc0
client trust gates backed 0 of 5
  - entry missing: corpus/knowledge/client-trust-gates-round68.md
base exit=1
```

Unknown revision stays environment:

```
$ python3 -B .../check_client_trust_gates.py --rev deadbeef...deadbeef
environment error: unknown revision 'deadbeef…' (git rev-parse failed: no output)
unknown-rev exit=2
```

## `--self-test` output (16 assertions, 0 failures)

```
PASS honest world at head rev
PASS honest world, working tree
PASS base control: missing entry is content (exit 1), not environment
PASS unknown revision is environment (exit 2)
PASS broken world rejected: entry missing
PASS broken world rejected: no source lines
PASS broken world rejected: only 4 source lines
PASS broken world rejected: duplicate id in source lines
PASS broken world rejected: id does not resolve
PASS broken world rejected: row not mined
PASS broken world rejected: source cell absent from the entry's source line
PASS broken world rejected: quote not in the anchor cell
PASS broken world rejected: id and quote not in a per-client table row
PASS broken world rejected: no verified-at
PASS broken world rejected: no recheck
PASS broken world rejected: no coverage-map row
self-test: 0 failure(s) over 16 assertions
self-test exit=0
```

## Before-state evidence (base `e94ae32a`, the frozen "Before")

- Entry absent at the base: `git show e94ae32a…:corpus/knowledge/client-trust-gates-round68.md`
  → exit 128; the draft's base control therefore reaches `0 of 5`, exit 1 (above).
- None of the five client URLs at the base: `git show e94ae32a…:corpus/SOURCES.md | grep -cE
  'vtcode|parallelworks|kilo\.ai|agent-framework|mistral-vibe'` → **0**.
- The counter itself did not exist at the base (no such path in the base tree).

## Bonus measurement: the honest world is already live in the working tree

The L1's C1 content is present uncommitted in the lane working tree (entry mtime Oct 24 23:00;
rows **S198** vtcode, **S199** parallelworks, **S200** kilo.ai, **S201** agent-framework,
**S202** mistral-vibe; coverage-map row present). Measured against it:

```
$ python3 -B .ufo/waves/round-68/w1/drafts/check_client_trust_gates.py --fetch
client trust gates backed 5 of 5
--fetch: quotes located on live pages: 5 of 5
--fetch S198: quote found <https://raw.githubusercontent.com/vinhnx/vtcode/main/docs/skills/SKILLS_GUIDE.md>
--fetch S199: quote found <https://parallelworks.com/docs/ai/code/skills>
--fetch S200: quote found <https://kilo.ai/docs/customize/skills>
--fetch S201: quote found <https://learn.microsoft.com/en-us/agent-framework/agents/skills>
--fetch S202: quote found <https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md>
worktree+fetch exit=0
```

So the third frozen conjunct (`--fetch` finds each of the 5 located quotes on its live page)
reproduces **5 of 5** on this host today, through this draft.

## Design decisions the L1 should know (remaining risks, named)

1. **Conjunct 7 is checked structurally.** "Client name and quoted behaviour occur in the
   per-client table" is enforced as: one ≥4-cell table row carries the id AND an anchor-bound
   located quote. The client *name* is not hardcoded (content, not names — Q25/Q26); its
   correctness is a review matter, not a counter matter.
2. **"Opens with" = first non-blank line is a `source:` line, ids within the first 10 lines,
   no duplicates, exactly 5** (one per client row). The landed entry satisfies this; any future
   entry with a preamble line would fail conjunct 2 by design.
3. **Counting semantics:** a global malformation (verified-at/recheck/coverage map/source-line
   shape) zeroes the count — the entry as a whole backs nothing (the r67 rule, kept for global
   conjuncts). A per-client failure (conjunctions 3/4/6/7 for one id) drops only that client, so
   partial credit prints honestly (e.g. `backed 4 of 5`, exit 1). Consequently `backed 5 of 5`
   implies exit 0 — no contradictory state exists.
4. **`--fetch` matching is a heuristic** (tag-strip + entity-unescape + whitespace/punctuation
   fold). A quote rendered oddly (split by inline tags the stripper joined differently, or an
   image-alt interpolation) would print `quote NOT found` — an honest negative, never counted,
   never silent; it cannot flip the exit code.
5. **`recheck:` is a prefix check** (any value), mirroring the r67 counter; the ISO-date/cadence
   validation of the cell lives in the registry gates (C2's `sources-census`), not here.

## Handoff

Install: `cp .ufo/waves/round-68/w1/drafts/check_client_trust_gates.py verifiers/check_client_trust_gates.py`
(L1's move; no content edit needed — the default repo path resolves from either location).
Run after landing: `python3 -B verifiers/check_client_trust_gates.py --rev <landed-sha>` and
`--rev e94ae32a…` for the base control; `--self-test` is content-independent.

Blockers: none.
