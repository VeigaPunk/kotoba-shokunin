# ExecFetchArm — C1 `--fetch` arm (round 69, wave 1)

Seat: `L1Kotoba69-2.ExecFetchArm`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Instrument: `verifiers/check_skill_precedence.py`, sha256
`9c796574c2d588f27869e0e14289c1be8f0b3f3e56f785d68eb64ee5e756da48` (same bytes in the sandbox).

## Verdict

**The fetch arm passes on the L1's draft bytes: `skill precedence backed 5 of 5`, `live quotes found 5 of 5`,
exit 0.** All five located quotes are live, each exactly once in tag-stripped page text, each under the
section its source line names, and each page also carries the rule its table cell claims.

**But the prescribed `--rev <branch-tip>` invocation fails at the lane's actual branch tip**, exit 1,
`skill precedence backed 0 of 5`, because the entry and its two corpus edits are **uncommitted**. At
`a238989` the counter never reaches `fetch()` (it gates on `n == TOTAL`), so its `live quotes found 0 of 5`
line is a *skipped* fetch, not five fetch attempts or five failures. This is a revision-bound blocker, not
a source or counter defect: the same instrument on a `/tmp` shared-clone revision containing the draft
prints 5 of 5 and exit 0.

Lane tip at start and at report time: `a238989a96cb0d2b939679126b832d75b861ca6e` (branch `master`,
detached export). `git status --porcelain`: `?? corpus/knowledge/skill-name-precedence-round69.md`,
` M corpus/SOURCES.md`, ` M corpus/README.md`.

## Run 1 — as prescribed, at the branch tip (fails)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/check_skill_precedence.py --rev a238989a96cb0d2b939679126b832d75b861ca6e --fetch
measured-rev: a238989a96cb0d2b939679126b832d75b861ca6e
skill precedence backed 0 of 5
  - entry missing: corpus/knowledge/skill-name-precedence-round69.md
live quotes found 0 of 5
exit=1
```

No `fetch S20x:` line appears — proof that no URL was attempted (source: `main()` line
`found, results = fetch(Path(tmp)) if args.fetch and n == TOTAL else (0, [])`).

## Run 2 — working-tree draft (passes)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/check_skill_precedence.py --fetch
measured-rev: working-tree
skill precedence backed 5 of 5
  fetch S203: found
  fetch S204: found
  fetch S205: found
  fetch S206: found
  fetch S207: found
live quotes found 5 of 5
exit=0
```

## Run 3 — `--rev` path over a sandbox revision carrying the draft (passes)

Built read-only from the lane; the lane index and `jj` state were never written:

```
git clone --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/k69-fetcharm-1717020/lane
git -C … checkout a238989a96cb0d2b939679126b832d75b861ca6e
cp corpus/knowledge/skill-name-precedence-round69.md  …/corpus/knowledge/
cp corpus/SOURCES.md corpus/README.md                 …/corpus/
git -C … add <the three paths> && git -C … commit   # sandbox identity only
```

```
$ cd /tmp/k69-fetcharm-1717020/lane
$ python3 -B verifiers/check_skill_precedence.py --rev f2231559c7d6b5ca0df493fcebad033adb150c0c --fetch
measured-rev: f2231559c7d6b5ca0df493fcebad033adb150c0c
skill precedence backed 5 of 5
  fetch S203: found
  fetch S204: found
  fetch S205: found
  fetch S206: found
  fetch S207: found
live quotes found 5 of 5
exit=0
```

Sandbox commit `f223155` ("sandbox: r69 C1 draft", 3 files, +68). Sandbox rev is **not** a lane commit
and does not satisfy the lane's branch tip; it isolates the cause of Run 1 to the uncommitted content.

## Independent re-open (re-ran the fetch myself, not the counter's claim)

Same UA as the counter (`Mozilla/5.0 kotoba-lane-check`), urllib, `timeout=40`.

| id | URL cited | HTTP | final URL | quote in tag-stripped text | section anchor named in source line |
|---|---|---|---|---|---|
| S203 | `https://docs.roocode.com/features/skills` | 200 | `https://roocodeinc.github.io/Roo-Code/features/skills/` (2 redirects, first 301) | 1× | "What Skills Let You Do" ✓, "Override Control" bullet ✓, "Choose a location" ✓, "Roo-specific (higher priority)" ✓ (2×) |
| S204 | `https://ampcode.com/docs/customize/skills` | 200 | same | 1× | "Skill Sources and Precedence" ✓ |
| S205 | `https://deepcode.vegamo.cn/en/docs/configuration/agent-skills` | 200 | same | 1× (3× raw, HTML duplication) | "Scan Locations" ✓ |
| S206 | `https://junie.jetbrains.com/docs/agent-skills.html` | 200 | same | 1× | "Skill location" ✓ |
| S207 | `https://opencode.ai/docs/skills/` | 200 | same | 1× | "Troubleshoot loading" ✓ |

Rule-cell support (beyond the located quote):

- **S203**: the page's own "Override Priority" list reads Project `.roo` mode-specific → Project `.roo`
  generic → Project `.agents` mode-specific → Project `.agents` generic → Global `.roo` … → Global
  `.agents` generic, and says `.roo/` paths "always take precedence over `.agents/` paths at the same
  project level". Project-beats-global and root-beats-root both hold. The entry's Limits disclosure is
  accurate: that list is markup-bearing (`<strong>` wrapping e.g. `Project <code>.roo</code>
  mode-specific`, `<code>` around `.roo`/`.agents`) and the root label does rest on the unshaped
  "Roo-specific (higher priority)" heading lines. A markup-free in-section sentence also exists —
  "When skills with the same name exist in multiple locations, this priority applies (highest to
  lowest)." — advisory only; it states the collision rule but not the root order.
- **S204**: "Amp uses the first skill with a given frontmatter name." plus the ordered source list; the
  quote is followed by "A personal skill masks a workspace skill … both mask official Amp skills."
- **S205**: quote sits in "Scan Locations" before a 1–5 priority table (project `.deepcode` → project
  `.agents` → user `.deepcode` → user `.agents` → built-in).
- **S206**: quote is the full same-name sentence; the troubleshooting section repeats that the
  user-level skill "will be skipped" — matches "ignored rather than merged".
- **S207**: page has **0** occurrences of "precedence", "duplicate", "collision"; "Override per agent"
  is a permissions section, not name resolution. Only the uniqueness sentence exists. "No precedence
  stated" is supported.

## Negative controls (proves "found" is not a tautology)

Two throwaway worlds in `/tmp`, built from the lane's draft and passed straight to the module's
`check()`/`fetch()` (no lane write):

| mutation | `check()` | `fetch()` |
|---|---|---|
| replace the S204 URL with `https://ampcode.com/docs/customize/skills-does-not-exist-xyz` in entry source line + registry row | 5 of 5 | `4`; `S204: FETCH FAILED HTTP Error 404: Not Found` |
| replace the S204 quote with "Local skills always beat official Amp skills of the same name." | 5 of 5 | `4`; `S204: NOT FOUND` |

So a dead URL and a fabricated quote each drop the count, and neither is counted as found. The fetch
arm is the only conjunct that can kill a stale-but-well-formed entry.

## Observations (not verdicts)

1. **Blocker for the frozen predicate.** For `--rev` to print 5 of 5, the L1 must commit all three
   paths (`corpus/knowledge/skill-name-precedence-round69.md`, `corpus/SOURCES.md`,
   `corpus/README.md`); committing the entry alone also fails, because the five `S20x` rows and the
   coverage-map index row live in the latter two. Draft digests measured here: entry
   `9e1f74a1d6d0eec57919efe7d2ee95bf8bb551d149b1914b27580fb1229e718a`, SOURCES
   `aaed976a4f77e15826271925997413b4a6409fad55bc7f90ed057002bae9b7c4`, README
   `79a5760f7e5c7f2d278f459a3d8bdc5cfe0d3d7fdc6b359cda14fc8426d1af11`.
2. **Failure lines omit the URL.** `fetch()` prints `S204: FETCH FAILED …` with no host, so an operator
   cannot tell a dead citation from a network blip without joining the id to `corpus/SOURCES.md`. Cheap
   fix if wanted; not claimed here.
3. **S203's citation redirects off-host** (`docs.roocode.com` 301 → `roocodeinc.github.io`). It resolves
   to the same docs page and urllib follows it, so the quote check is valid; if the registry ever pins a
   non-redirecting host, this row is the one to re-point.
4. No package installs or upgrades were made. Lane untouched: its `git status` for `corpus/`,
   `verifiers/`, `PROVINCE.md`, `SKILL.md`, `plans/` is unchanged from before the run apart from
   sibling seats' concurrent writes (`corpus/lessons/round-69.md` appeared while this seat ran).

## Evidence paths

- Sandbox: `/tmp/k69-fetcharm-1717020/lane` (rev `f223155`), worlds
  `/tmp/k69-fetcharm-1717020/world-dead-url`, `/tmp/k69-fetcharm-1717020/world-fake-quote`.
- Full raw bodies and tool output for the re-open: eval artifacts `50892`, `51881`.
- Commands above are copy-pasteable; Run 3 needs the sandbox to exist (rebuild with the three lines
  shown if `/tmp` was cleaned).
