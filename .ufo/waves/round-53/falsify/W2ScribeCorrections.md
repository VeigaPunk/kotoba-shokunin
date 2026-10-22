Result: MIXED — all seven named statements and all six always-on dispositions are false or unverifiable as written at `c775d682`, and every drafted correction reproduces on the live host/docs today, but the Q29 registry as shipped cannot carry the knowledge-entry rows: one row naming a file outside the sweep's four self-test fixtures turns `--self-test` into a `RuntimeError`, and a JSON target collapses to a single block, so its row is file-level rather than per-disposition.

Round-53 falsify, seat `KotobaR53.W2ScribeCorrections`, measured 2026-10-22T20:30–21:05Z.
Judged revision `c775d6823bfca8f0de8c0874032a954438b38edc` (lane `HEAD`, verified). Lane files were read only;
every write went to the sandbox clone at
`/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53ScribeCorrections/` (`clone`, `pristine`, `probe-selftest`, `src`).
No lane edit, no git/jj write in the lane, no fleet write, no subagent, no model call, no install or upgrade.

**Working-tree warning, read first.** The lane working tree is no longer `c775d682`: `git status` shows 11
modified and 3 untracked paths, including `SKILL.md` (+10 lines) and `corpus/README.md` (+11). The L1 has
already replaced the `SKILL.md` always-on evidence sentence in flight (quoted in §3.6). All line numbers below
are the **judged revision's**, with the current working-tree line added where it differs; my drafts are against
`c775d682` as assigned, and §3.6 states the reconciliation.

---

## 1. Live re-verification (every command run, exit code and output)

### 1.1 Host surface

```
$ wc -l < ~/.agents/AGENTS.md            → 14
$ wc -c < ~/.agents/AGENTS.md            → 949
$ sha256sum ~/.agents/AGENTS.md          → 7b06a503110ca86373c1da0daf3694d5ce57f4ae9a792dd09fcf3c4ae4b1896e
$ sed -n '1p' ~/.agents/AGENTS.md        → # Operator tooling directive — 2026-10-19
$ sed -n '48p;51p' ~/.agents/AGENTS.md   → (no output), exit 0
$ grep -c 'name the axes' ~/.agents/AGENTS.md               → 0
$ grep -c 'iterate cheap in parallel' ~/.agents/AGENTS.md   → 0
$ grep -c 'no worktrees' ~/.agents/AGENTS.md                → 0
$ grep -c 'Zero procedures' ~/.agents/AGENTS.md             → 0
$ grep -n -i 'RULES.md|before installing' ~/.agents/AGENTS.md
5:Before installing, read `/home/vgpnk/.omp/agent/RULES.md` for the official-source/channel policy, …
$ grep -cE '[0-9]{4}-[0-9]{2}-[0-9]{2}' ~/.agents/AGENTS.md → 1 (line 1)
$ ls -d /home/vgpnk/projects             → ls: cannot access '/home/vgpnk/projects': No such file or directory, exit 2
$ find . -maxdepth 2 -name AGENTS.md -path './*/AGENTS.md' | wc -l   (cwd /home/vgpnk/Projects/shokunin) → 17
$ (tail -n +2 each of the 17) | md5sum | cut -c1-12 | sort | uniq -c
      9 12a62ab90292
      4 96f7dfd1d7d3
      1 464981f930a8
      1 5f0c5ef0d655
      1 9f1250a8f81c
      1 bc1a9ee7bb77
$ wc -l /home/vgpnk/Projects/shokunin/AGENTS.md → 92   (fleet-root file, in no prior census)
$ ls /home/vgpnk/Projects/shokunin/.ufo/prompts/*-L1.md | wc -l → 8
$ od -c AGENTS.md (lane) → "# kotoba-shokunin operating rules\n\n- Work only…"  ⇒ the "5-line" family counts a blank second line
```

### 1.2 Documents (fetched this seat, independent of the wave-1 scouts)

| # | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| D1 | `https://code.claude.com/docs/en/memory.md` | 2026-10-22T20:38:10Z | 200 | 51,971 | `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff` |
| D2 | `https://learn.chatgpt.com/docs/agent-configuration/agents-md.md` | 2026-10-22T20:38:11Z | 200 | 9,149 | `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e` |
| D3 | `https://opencode.ai/docs/rules.md` | 2026-10-22T20:38:11Z | 200 | 6,684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` |

All three hashes equal the ones the wave-1 scouts recorded (`ScoutLaneCorpusAlwaysOn.md` Part A), so the
documents have not moved between their fetch and mine. Quotes below are from my own fetched bytes, line
numbers in those bytes, each ≤25 words:

- D1 `:356` — "An `AGENTS.md`, and no `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it" → "Your `AGENTS.md`".
- D1 `:357` — both present → "Your `CLAUDE.md` files only".
- D1 `:364` — "Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later."
- D1 `:378` — "Not read: `AGENTS.local.md`, `AGENTS.override.md`, or anything under a `.agents/` directory".
- D1 `:390` — "`claude-md-or-agents-md` … This is the default".
- D1 `:603` — "By default Claude reads `AGENTS.md` only when you have no `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it."
- D1 `:442` — "putting an `@AGENTS.md` import in a `CLAUDE.md` next to it"; D1 `:455` — `ln -s AGENTS.md CLAUDE.md`.
- D2 `:11` — "Codex reads `AGENTS.override.md` if it exists. Otherwise, Codex reads `AGENTS.md`."
- D2 `:12` — "Codex includes at most one file per directory"; D2 `:15` — "stops adding files once the combined size reaches the limit defined by `project_doc_max_bytes` (32 KiB by default)".
- D3 `:76` — "**Project rules**: `CLAUDE.md` in your project directory (used if no `AGENTS.md` exists)".
- D3 `:98` — "if you have both `AGENTS.md` and `CLAUDE.md`, only `AGENTS.md` is used".
- D3 `:132` — "While opencode doesn't automatically parse file references in `AGENTS.md`".

### 1.3 Instrument observations on the live surface (read-only, run once)

```
$ python3 -B verifiers/verify_alwayson.py --check alwayson.04 --target /home/vgpnk/.agents
FAIL alwayson.04: /home/vgpnk/.agents: dated/transient text found: AGENTS.md:1 ISO date/timestamp '2026-10-19'   exit 1
$ python3 -B verifiers/verify_alwayson.py --check alwayson.07 --target /home/vgpnk/.agents
PASS alwayson.07: /home/vgpnk/.agents: 1 selected files; no independent AGENTS/CLAUDE pair                     exit 0
$ python3 -B verifiers/verify_alwayson.py --check alwayson.07 --target /home/vgpnk/Projects/shokunin
PASS alwayson.07: …: 1 selected files; no independent AGENTS/CLAUDE pair                                       exit 0
```

These are observations of the instrument on the live population, not the C2 claim (which counts pinned cases);
I ran them only because two drafted sentences assert what the instrument does to the host file.

---

## 2. Attack table

Each named statement is attacked against the live host and the three documents. "Statement" is the text at the
judged revision; "now" is the measured fact.

| # | Target (`c775d682`) | Statement | Now | Verdict |
|---|---|---|---|---|
| S1 | `corpus/knowledge/claude-md-surface.md:33-34` | "Same load semantics as AGENTS.md (always-on when present in the repo)" | Claude Code: `CLAUDE.md` replaces `AGENTS.md` (D1 `:357`, `:603`); opencode: `CLAUDE.md` is a fallback used only when no `AGENTS.md` exists (D3 `:76`, `:98`); omp: at one depth the two tie and `AGENTS.md` takes the slot (`ScoutOmpAlwaysOn.md:195`) | **BREAKS** |
| S2 | `corpus/knowledge/instruction-surface-census-round13.md:474` | "AGENTS.md \| Always-on: injected into every session in its repo" | false as a law: D1 `:356-357`, `:378`; D2 `:11-12`, `:15`. True only for the two harnesses the row names, and there subject to their own slot rules | **BREAKS** |
| S3 | `corpus/knowledge/agents-md-and-dispatch-surfaces.md:10` | "6 identical-shape files in `/home/vgpnk/projects/shokunin/*/AGENTS.md` … Always injected for sessions rooted in the repo" | the lowercase root does not exist (`ls` exit 2); 17 files, 9/4/4 body families; "always injected" false across clients (D1 `:357`, `:378`; D2 `:11-12`) | **BREAKS** |
| S4 | `…agents-md-and-dispatch-surfaces.md:26-29` | "`~/.agents/AGENTS.md` (~60 lines) … posture rules ("name the axes"…), runtime bans ("no worktrees") … Zero procedures" | 14 lines / 949 B; all four quoted strings 0 hits; line 5 redirects to `~/.omp/agent/RULES.md`; line 1 is a date | **BREAKS** |
| S5 | `corpus/README.md:12` | "6 child AGENTS.md + `~/.agents/AGENTS.md` + 8 `.ufo/prompts/*-L1.md`" | 17 child files; host 14 lines / 949 B; the `8` still measures 8 | **BREAKS** (count only) |
| S6 | `SKILL.md:363-364` | "(6/6 repo files pass; the 75-line host `~/.agents/AGENTS.md` fails procedures/dates/style)" | 9 of 17 files carry the 5-line body; the host file is 14 lines / 949 B and its cited lines do not exist | **BREAKS** (partly repaired in flight, §3.6) |
| S7 | `SKILL.md:461-462` (working tree `:465-466`) | "`/home/vgpnk/projects/shokunin/*/AGENTS.md` (6 files) + `~/.agents/AGENTS.md`" | lowercase path unresolvable; 17 files | **BREAKS** (untouched by the L1's edit) |
| S8 | `verifiers/checklist-baseline.json` alwayson dispositions, boxes `alwayson.01/.02/.03/.05/.06/.08` | "7 files at round 15 … the hand-applied no-dated-text box splits 6 PASS / 1 FAIL (host file lines 48 and 51)" | the host file has 14 lines; `sed -n '48p;51p'` prints nothing, so the pointer is unverifiable and the split is not re-checkable; the scope is 17 nested files + host (+4 depth-2 project files) | **BREAKS** (pointer + count) |
| S9 | the Q29 mechanism itself | "the superseded claim's stale phrase and its declared result go into `check_correction_sweep.py`'s registry" (`corpus/QUALITY.md:40`) | the registry supports only the four files the self-test writes; a knowledge-entry row crashes `--self-test`; a JSON row degenerates to one block | **BREAKS** (see §6.1, §6.2) |
| S10 | `corpus/knowledge/instruction-surface-census-round13.md:478` (not in my target list) | "**omp** … reads it *alongside* AGENTS.md" | the round's own omp reading: "`AGENTS.md` wins, `CLAUDE.md` is marked `_shadowed` and is not injected at that depth" (`ScoutOmpAlwaysOn.md:195`) | **BREAKS** (new; routed to the L1) |

What **HOLDS**, and must not be re-reported as a defect:

- `census:478`'s opencode half (env-gated fallback) matches D3 `:76`, `:83-85`, `:98` on every clause.
- `claude-md-surface.md:40-42` ("file-name ≠ loader contract") is unchanged and D3 `:132` is a second witness.
- `agents-md:15-17`'s claim that the family shares one body, title line aside, is still true of 9 files.
- The lane's own `AGENTS.md` is 5 lines with the blank second line the family shares (od dump above).
- `corpus/README.md:87`'s "no executed or delegated box" sentence is true at `c775d682` for the six remaining
  boxes; the L1's in-flight round-53 note is what narrows it.

---

## 3. Draft corrections (verbatim, append-only unless marked "replacement")

Placement rule that every draft obeys, and the reason: `check_correction_sweep.py`'s `blocks()` splits on blank
lines and on lines starting `- `/`* `/`1. `/`|`/`#`. A correction placed in a **new paragraph** is a new block,
so the stale block would still carry the stale phrase without the declared result and the sweep would fail.
Every knowledge-entry note below is therefore appended **inside the stale block** (indented continuation of the
list item, or an unindented continuation line of the paragraph, or inside the same table row). This is also the
lane's existing convention: `corpus/README.md:20` carries a `**round-27 note:**` inside the row it corrects.

### 3.1 `corpus/knowledge/claude-md-surface.md` — append to the bullet that starts at `:33`

```markdown
- Same load semantics as AGENTS.md (always-on when present in the repo) →
  same constraint-survival craft rule applies; a 4339-line CLAUDE.md is an
  unconditional tax on every session in that repo.
  **round-53 correction (2026-10-22):** the two names do not load the same way,
  and the premise fails in both directions. Claude Code reads a `CLAUDE.md`
  (or `.claude/CLAUDE.md`, `CLAUDE.local.md`) in place of `AGENTS.md` when one
  exists in the working directory or above it, and reads `AGENTS.md` only when
  none does — with the installed 2.1.304 default `claude-md-or-agents-md`
  (`claude plugin configure cc-plugin-agents-md@builtin --json`,
  `ScoutClaudeBehaviour.md` § 3; docs S043 `memory.md:356-357`, `:603`).
  opencode uses `CLAUDE.md` only when no `AGENTS.md` exists in that directory
  (S045 `rules.mdx:76`, `:98`). omp registers the two names as separate
  providers and, at one depth, the two tie and `AGENTS.md` takes the slot, so a
  standalone `CLAUDE.md` beside an `AGENTS.md` is shadowed rather than read
  (`ScoutOmpAlwaysOn.md:77-78`, `:195`; [INFERENCE] on the tie direction, no
  session was run), while `~/.claude/CLAUDE.md` is a higher-priority provider
  that loads beside a project `AGENTS.md` (one user file and one project file
  per depth are different keys, `ScoutOmpAlwaysOn.md:435`).
  The craft conclusion survives for the file each client actually reads — the
  tax is on the bytes that load — and the per-client table is
  `corpus/knowledge/alwayson-rule-files-round53.md`.
```

### 3.2 `corpus/knowledge/instruction-surface-census-round13.md:474` — same row, Load-condition cell

The row is one line and one block; append inside the cell (no `|` in the appended text):

```
| AGENTS.md | Always-on: injected into every session in its repo — **round-53 correction (2026-10-22):** true of the two harnesses this row's parse surface names, subject to their own shadowing (omp keeps one file per scope and depth, and its two standalone names tie at priority 10 with `AGENTS.md` taking the slot, `ScoutOmpAlwaysOn.md:77-78`, `:195`, [INFERENCE] on the tie direction, no session was run; opencode takes the first name that exists per directory, `AGENTS.md` before `CLAUDE.md`, S045 `rules.mdx:98`; the CLAUDE.md row below says the two are read alongside, which this narrows), and false as a law across clients: Claude Code reads `CLAUDE.md` files only when one counts (S043 `memory.md:357`) and reads nothing under a `.agents/` directory (`:378`), Codex reads `AGENTS.override.md` ahead of `AGENTS.md`, one file per directory, stopping at 32 KiB combined (S044 `agents-md.md:11-15`); per-client table `corpus/knowledge/alwayson-rule-files-round53.md` | No frontmatter, no router — … (rest of the row unchanged)
```

### 3.3 `corpus/knowledge/agents-md-and-dispatch-surfaces.md:10` — same row

```
| AGENTS.md | 6 identical-shape files in `/home/vgpnk/projects/shokunin/*/AGENTS.md` + `~/.agents/AGENTS.md` — **round-53 correction (2026-10-22):** the root is `/home/vgpnk/Projects/shokunin` (capital `P`; the lowercase path does not exist on this host) and it held 17 `AGENTS.md` files, of which 9 share the 5-line body (md5 `12a62ab9…` over lines 2-end), 4 share a second body (`96f7dfd1…`) and 4 are singletons | Always injected for sessions rooted in the repo — **bounded round-53 (2026-10-22):** true of the harnesses of that era (omp, opencode), not of every client: Claude Code reads `CLAUDE.md` files only when one counts and nothing under `.agents/` (S043 `memory.md:357`, `:378`), Codex reads `AGENTS.override.md` ahead of `AGENTS.md` with at most one file per directory (S044 `agents-md.md:11-12`); per-client table `corpus/knowledge/alwayson-rule-files-round53.md` |
```

### 3.4 `corpus/knowledge/agents-md-and-dispatch-surfaces.md:26-29` — append to the paragraph

```markdown
**round-53 correction (2026-10-22):** the file changed. `~/.agents/AGENTS.md`
measures 14 lines / 949 B (sha256 `7b06a503…`), its first line is
`# Operator tooling directive — 2026-10-19`, and none of the quoted posture text
survives (`name the axes` 0 hits, `iterate cheap in parallel` 0, `no worktrees`
0). Line 5 now sends the reader to `~/.omp/agent/RULES.md` before any install, so
"zero procedures" no longer holds of it: it carries a cross-file procedure
pointer and a dated heading. The delegated instrument's verdict on that
directory, run 2026-10-22: `verify_alwayson.py --check alwayson.04 --target
~/.agents` → `FAIL ... AGENTS.md:1 ISO date/timestamp '2026-10-19'`, exit 1.
`~/.agents` has no VCS, so the round-6 bytes are not recoverable; this is a
re-measurement, not a diff. The sibling family is 17 files, not 6 — the row
above carries the split.
```

### 3.5 `corpus/README.md:12` — same index row

```
| AGENTS.md & dispatch prompts | `knowledge/agents-md-and-dispatch-surfaces.md` | 6 child AGENTS.md + `~/.agents/AGENTS.md` + 8 `.ufo/prompts/*-L1.md` — **round-53 correction (2026-10-22):** 17 child files (`ls /home/vgpnk/Projects/shokunin/*/AGENTS.md \| wc -l` → 17; 9 share the 5-line body), the host file 14 lines / 949 B, and the prompt count still measures 8; the lowercase `/home/vgpnk/projects` root the knowledge file cites does not exist |
```

### 3.6 `SKILL.md:363-364` — replacement (task asked for replacement wording here)

```markdown
Run before editing any always-loaded rules file. Observed evidence +
application matrix in `corpus/knowledge/alwayson-checklist-round7.md`; its
population line is round-7 era. Re-measured 2026-10-22: 17 `AGENTS.md` files
under `/home/vgpnk/Projects/shokunin/*/` (9 on the 5-line template) and the host
`~/.agents/AGENTS.md` at 14 lines / 949 B with a dated first line; per-client
resolution in `corpus/knowledge/alwayson-rule-files-round53.md`.
```

**Reconciliation with the in-flight edit.** The working tree now reads:

```
Run before editing any always-loaded rules file. Round-7 evidence +
application matrix (6/6 repo files passed; the host `~/.agents/AGENTS.md`, then
75 lines and 14 at round 53, failed procedures/dates/style) in
`corpus/knowledge/alwayson-checklist-round7.md`. Boxes 4 and 7 run one at a time as …
```

That wording removes the present-tense "75-line host" claim by dating it, so the freshness defect is gone
either way; mine additionally states the 17-file population and the 5-line family. **Do not apply both** — pick
one. If the L1 keeps their sentence, registry row `r53-c2-skill-75-line` below becomes vacuous (the phrase
`75-line host` is gone) and should be re-targeted to `stale: r"6/6 repo files passed"`,
`declared: r"14 at round 53"`, or dropped.

### 3.7 `SKILL.md:461-462` (working tree `:465-466`) — replacement

```markdown
- `/home/vgpnk/Projects/shokunin/*/AGENTS.md` (17 files on 2026-10-22; 9 share
  the 5-line template body) + `~/.agents/AGENTS.md` (14 lines / 949 B) —
  always-on constraint files; no frontmatter, terse imperatives.
```

### 3.8 `verifiers/checklist-baseline.json` — append to all six shared dispositions

Same string at `:208`, `:214`, `:220`, `:232`, `:238`, `:250` (boxes `alwayson.01/.02/.03/.05/.06/.08`). Append
inside the JSON string (no `"` added, `unexecuted:` prefix preserved so `DISPOSITION_RE` still matches):

```
; round-53 re-measure (2026-10-22): the host file is 14 lines / 949 B (sha256 7b06a503110ca86373c1da0daf3694d5ce57f4ae9a792dd09fcf3c4ae4b1896e), so the cited host lines 48 and 51 no longer exist and the round-15 split is not re-checkable; this scope now holds 17 nested AGENTS.md files under Projects/shokunin plus the host file (and 4 further project-level files at depth 2: kimi-code, opencodeufo, shokunin, ufo-fsd-alpha), and the live dated-text hit is host line 1, which the delegated instrument already fails (alwayson.04 on ~/.agents: AGENTS.md:1 ISO date/timestamp 2026-10-19, exit 1; see corpus/knowledge/alwayson-rule-files-round53.md)
```

---

## 4. Draft registry rows and the sweep patch Q29 needs

### 4.1 Registry rows (insert before the closing `)` of `REGISTRY`)

```python
    # round 53 (Q29): the round-53 C2 corpus corrections and re-measurements.
    # Knowledge entries and README rows keep the stale phrase verbatim and carry
    # the declared re-measurement in the same block; the two SKILL.md rows are
    # canaries -- the replacement wording removes the stale phrase, so the row
    # fires only if it is reintroduced without the declared result.
    {"id": "r53-c2-claudemd-semantics", "file": "corpus/knowledge/claude-md-surface.md",
     "stale": r"Same load semantics as AGENTS\.md",
     "declared": r"round-53 correction \(2026-10-22\)", "lead": False},
    {"id": "r53-c2-census-agentsmd-alwayson",
     "file": "corpus/knowledge/instruction-surface-census-round13.md",
     "stale": r"Always-on: injected into every session in its repo",
     "declared": r"round-53 correction \(2026-10-22\)", "lead": False},
    {"id": "r53-c2-agentsmd-six-files",
     "file": "corpus/knowledge/agents-md-and-dispatch-surfaces.md",
     "stale": r"6 identical-shape files in",
     "declared": r"held 17 `AGENTS\.md` files", "lead": False},
    {"id": "r53-c2-agentsmd-host-60-lines",
     "file": "corpus/knowledge/agents-md-and-dispatch-surfaces.md",
     "stale": r"\(~60 lines\)", "declared": r"14 lines / 949 B", "lead": False},
    {"id": "r53-c2-readme-six-child", "file": "corpus/README.md",
     "stale": r"6 child AGENTS\.md", "declared": r"17 child files", "lead": False},
    {"id": "r53-c2-skill-75-line", "file": "SKILL.md",
     "stale": r"75-line host", "declared": r"14 lines / 949 B", "lead": False},
    {"id": "r53-c2-skill-six-files", "file": "SKILL.md",
     "stale": r"AGENTS\.md` \(6 files\)", "declared": r"17 files", "lead": False},
    {"id": "r53-c2-baseline-pointer", "file": "verifiers/checklist-baseline.json",
     "stale": r"host file lines 48 and 51",
     "declared": r"round-53 re-measure \(2026-10-22\)", "lead": False},
```

### 4.2 The patch without which those rows break the self-test (§6.1)

```python
# Files a registry row names that the self-test's four fixed fixtures do not
# write; seeded per case so `sweep` never sees a missing file (round 53).
SEEDED = (
    "corpus/knowledge/claude-md-surface.md",
    "corpus/knowledge/instruction-surface-census-round13.md",
    "corpus/knowledge/agents-md-and-dispatch-surfaces.md",
    "verifiers/checklist-baseline.json",
)
```

and inside `self_test()`:

```python
    def case(name, readme, score, want, province="- nothing stale\n",
             skill="- nothing stale\n", seed=None):
        nonlocal n
        n += 1
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "corpus").mkdir()
            (Path(t) / "corpus/README.md").write_text(readme)
            (Path(t) / "SCORECARD.md").write_text(score)
            (Path(t) / "PROVINCE.md").write_text(province)
            (Path(t) / "SKILL.md").write_text(skill)
            for rel in SEEDED:
                p = Path(t) / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text((seed or {}).get(rel, "- fixture\n"))
            got = sweep(reader(None, t))
```

plus four cases that show the new rows able to fail (assertion count 7 → 11; the round-52 precedent for growth is
`corpus/lessons/round-52.md:124`, "self-test 5 → 7"):

```python
    # round 53 (Q29): each round-53 row is shown red without its correction and
    # green with it, on the file the row names.
    stale_c = "- Same load semantics as AGENTS.md (always-on when present in the repo) -> tax\n"
    red_c = {"corpus/knowledge/claude-md-surface.md": stale_c}
    grn_c = {"corpus/knowledge/claude-md-surface.md":
             stale_c + "  round-53 correction (2026-10-22): not the same semantics\n"}
    case("r53 claude-md semantics red", "- x\n", "| d | 9 | x |\n",
         ["r53-c2-claudemd-semantics"], seed=red_c)
    case("r53 claude-md semantics green", "- x\n", "| d | 9 | x |\n", [], seed=grn_c)
    base_red = {"verifiers/checklist-baseline.json":
                '      "disposition": "unexecuted:x; host file lines 48 and 51"\n'}
    base_grn = {"verifiers/checklist-baseline.json":
                '      "disposition": "unexecuted:x; host file lines 48 and 51;'
                ' round-53 re-measure (2026-10-22): 14 lines / 949 B"\n'}
    case("r53 baseline pointer red", "- x\n", "| d | 9 | x |\n",
         ["r53-c2-baseline-pointer"], seed=base_red)
    case("r53 baseline pointer green", "- x\n", "| d | 9 | x |\n", [], seed=base_grn)
```

If the L1 prefers not to touch `self_test()`, the alternative is a `reader` that returns `""` for a missing file
instead of `None` (so `sweep` does not raise), but then a typo in a `file` field becomes silent — worse. Seed
the fixtures.

---

## 5. Gate runs proving the drafts (sandbox clone only)

Clone `clone` = `git clone` of the lane, checked out at `c775d682`, drafts applied, three local commits
(`af231f3d`, `e0127d4d`, final `99a262d9c3b084822ff3758354ca36be9a135a1b`); never pushed.

```
# 1. red before the corrections (rows read the committed bytes at c775d682)
$ python3 -B verifiers/check_correction_sweep.py --rev c775d6823bfca8f0de8c0874032a954438b38edc
FAIL r53-c2-claudemd-semantics corpus/knowledge/claude-md-surface.md:33 stale claim without the declared result
FAIL r53-c2-census-agentsmd-alwayson corpus/knowledge/instruction-surface-census-round13.md:474 stale claim without the declared result
FAIL r53-c2-agentsmd-six-files corpus/knowledge/agents-md-and-dispatch-surfaces.md:10 stale claim without the declared result
FAIL r53-c2-agentsmd-host-60-lines corpus/knowledge/agents-md-and-dispatch-surfaces.md:26 stale claim without the declared result
FAIL r53-c2-readme-six-child corpus/README.md:12 stale claim without the declared result
FAIL r53-c2-skill-75-line SKILL.md:362 stale claim without the declared result
FAIL r53-c2-skill-six-files SKILL.md:461 stale claim without the declared result
FAIL r53-c2-baseline-pointer verifiers/checklist-baseline.json:1 stale claim without the declared result
correction sweep: 8 stale block(s)                                                          exit 1

# 2. green at the corrected commit
$ python3 -B verifiers/check_correction_sweep.py --rev 99a262d9c3b084822ff3758354ca36be9a135a1b
correction sweep: 0 stale block(s)                                                          exit 0
$ python3 -B verifiers/check_correction_sweep.py --root .                                   → 0 stale block(s), exit 0
$ python3 -B verifiers/check_correction_sweep.py --self-test
0 failure(s) over 11 assertions                                                             exit 0

# 3. the edits do not disturb C2 or the box map
$ python3 -B verifiers/check_alwayson_boxes.py --rev 99a262d9c3b084822ff3758354ca36be9a135a1b
always-on boxes executed and discriminating 2 of 8                                          exit 0
$ python3 -B verifiers/verify_skill_checklist.py --json --check checklist.box_map_complete
"status": "PASS"  ("pass": 1, "fail": 0)                                                    exit 0
$ python3 -B verifiers/verify_alwayson.py --self-test
0 failure(s) over 89 assertions                                                             exit 0
$ python3 -c 'json.load(open("verifiers/checklist-baseline.json"))'                          → 41 boxes, valid

# 4. no-harm on the corpus gate (identical observed block in both clones)
$ python3 -B verifiers/verify_corpus_integrity.py --json   # pristine c775d682 vs corrected
both: tracked_files 77, unindexed 1 (alwayson-rule-files-round53.md), report_total 49, report_dead 0,
      commit_total 32, commit_unresolvable 1 → identical observed values; exit 1 both (pre-existing
      routed-defect-2 state, not caused by these edits)
```

`verify_skill_checklist.py` with no `--check` reports `exit_code 1, pass 8, fail 3` **in both** the pristine and
the corrected clone, with the same three ids (`trigger.name_directory`, `trigger.citation_resolves`,
`governance.citation_resolves`); those are sandbox artifacts (the clone directory is named `clone`, not
`kotoba-shokunin`, and `../.ufo/reports/...` resolves into the absent fleet root), not effects of my edits.

---

## 6. Defects, with severity

### 6.1 HIGH — the Q29 registry cannot name a knowledge entry without breaking `--self-test`

`self_test()` writes exactly four files into its temporary tree (`corpus/README.md`, `SCORECARD.md`,
`PROVINCE.md`, `SKILL.md`) and then calls `sweep(reader(None, t))`, which iterates **every** registry row and
raises `RuntimeError("missing %s")` for a file that is not there. Proof, on a pristine copy of the judged
revision with one knowledge-file row added:

```
$ python3 -B verifiers/check_correction_sweep.py --self-test
Traceback (most recent call last):
  File ".../verifiers/check_correction_sweep.py", line 124, in self_test
    case("red both", stale_r, stale_s, ["r51-c2-readme", "r51-c2-scorecard-lead"])
  File ".../verifiers/check_correction_sweep.py", line 78, in sweep
    raise RuntimeError("missing %s" % e["file"])
RuntimeError: missing corpus/knowledge/claude-md-surface.md
                                                                                            exit 1
```

Impact: Q29 names "knowledge entries" as a target class (`corpus/QUALITY.md:40`), and the plan's no-harm guard
requires `check_correction_sweep.py` "unchanged in exit code" (plan § No-harm guards, erratum § 6). The first
row that obeys Q29 for a knowledge entry turns the self-test into a traceback. Fix: §4.2.

### 6.2 MEDIUM — a JSON registry target collapses to one block, so its row is file-level

Measured with the shipped `blocks()`:

```
verifiers/checklist-baseline.json: 254 lines -> 1 block(s); first block starts at line 1, 254 lines
corpus/knowledge/claude-md-surface.md: 51 lines -> 19 block(s)
corpus/README.md: 189 lines -> 99 block(s)
```

`checklist-baseline.json` has no blank lines and no line starting `- `/`|`/`#`, so every line joins one block.
A row on it therefore checks only "the declared phrase appears somewhere in the file": correcting one of the six
dispositions would satisfy the row while five stale ones remain. This is not fatal (the row still catches
removal of the whole note, and it does fire red at `c775d682` — see §5.1), but it is weaker than the registry
docstring implies. Options for the L1: accept it and say so in the row's comment; or teach `blocks()` to split
on `^\s*[{}\[\]]` for JSON; or register the six dispositions as six rows with a per-box `stale` pattern that
includes the `box_id` (still one block, so no gain). I recommend the comment.

### 6.3 MEDIUM — `census-round13.md:478` states omp reads `CLAUDE.md` "alongside" `AGENTS.md`; the round's own evidence contradicts it

`ScoutOmpAlwaysOn.md:195`: "`AGENTS.md` wins, `CLAUDE.md` is marked `_shadowed` and is not injected at that
depth", with [INFERENCE] only on the tie direction (`:198`). The wave-1 corpus scout counted `:478` as
holding (`ScoutLaneCorpusAlwaysOn.md` Part B row 18), so the defect is new to this seat. It matters because
S1/S2 corrections must not lean on it — my drafts state the shadowing instead. Suggested correction and row (if
the L1 routes it):

```python
    {"id": "r53-c2-census-omp-alongside",
     "file": "corpus/knowledge/instruction-surface-census-round13.md",
     "stale": r"reads it \*alongside\* AGENTS\.md",
     "declared": r"shadowed", "lead": False},
```

```markdown
  **round-53 correction (2026-10-22):** "alongside" is true across scopes, not at one depth. omp keeps one user
  file and one project file per depth (`ScoutOmpAlwaysOn.md:435`); a standalone `CLAUDE.md` beside an `AGENTS.md`
  ties at priority 10 and is shadowed (`:77-78`, `:195`, [INFERENCE] on the tie direction), while
  `~/.claude/CLAUDE.md` (priority 80, user scope) does load beside a project `AGENTS.md`.
```

### 6.4 MEDIUM — the six unexecuted always-on dispositions describe box 04's result as the reason for every box

At `c775d682` the string at `:208/.214/.220/.232/.238/.250` is identical for `alwayson.01/.02/.03/.05/.06/.08`
and says "the hand-applied **no-dated-text** box splits 6 PASS / 1 FAIL". That is box `alwayson.04`'s
disposition, carried as the evidence for six other boxes (constraint-only, procedures, triggers, style, template
family, size). My §3.8 append keeps the historical sentence (Q29: the stale phrase stays) and adds the
re-measurement, but the mislabeling survives. The honest fix is a second sentence naming each box's own
round-15 reading or saying it was never applied per box; that is a map-content decision, so I route it rather
than draft it.

### 6.5 MEDIUM — `SKILL.md:461-462` was not touched by the in-flight repair

The L1's working-tree edit fixes `:363` but the surface row still reads
`/home/vgpnk/projects/shokunin/*/AGENTS.md` (lowercase, unresolvable) with `(6 files)`. Draft §3.7. Severity is
medium because this line is inside the skill's own evidence list, where a reader copies the path.

### 6.6 LOW — `corpus/knowledge/alwayson-checklist-round7.md:29-30` still carries the dead population numbers

```
| `~/.agents/AGENTS.md` (75 lines, 3781 B) | **FAIL** AC-1/2/4/5: carries procedures (`Load and obey
  ~/.agents/godspeed-core/directive.md` :18; `Run the-janitor tac-check` :55), dated text (:48,:51 …) |
```

`:18`, `:55`, `:48`, `:51` cannot exist in a 14-line file, and `SKILL.md:363` points readers here. Not in my
target list; report only. If it is corrected, it needs its own registry row (`stale: r"75 lines, 3781 B"`).

### 6.7 LOW — the quoted 5-line template omits the blank second line

`agents-md-and-dispatch-surfaces.md:15-22` shows four lines (title + three bullets) but every member of the
family measures 5 lines (`od -c` above: `# …\n\n- Work …`). The `md5 12a62ab9…` figure in §3.3 is over
`tail -n +2`, i.e. blank line plus three bullets. Cosmetic, but it is the file's own "identical 5-line template"
evidence.

### 6.8 LOW — the in-flight README note cannot satisfy a correctly written Q29 row

`corpus/README.md:90` (frontier row) still says "the agent-definition and always-on checklists have no executed
or delegated box"; the L1's new paragraph at `:105-113` corrects it in a **different block**. Under the sweep's
block rule, a row with `stale: r"no executed or delegated box"` and `declared: r"alwayson\.04"` would fail. Either
edit the row in place or register it as a canary deliberately (stale phrase removed from the row).

---

## 7. Out of scope / not checked

- The changelog/release-notes leg of Q30 for all three clients: **not opened** by this seat. Nothing here should
  be read as a "client documents nothing" negative; all three are `current docs opened, changelog not checked`.
- Gemini CLI, Copilot (VS Code and CLI), Cursor, Zed, and the `agents.md` site: not opened by me. My corrections
  cite only S043/S044/S045 plus the lane's own omp readings; the other rows of the round-53 entry are
  unreviewed by this seat.
- I did not re-derive C1 (opencode re-pin) or run its counter; that is `W2RerunC2`/`W2CriticC1Landed` territory.
  I used the opencode docs page only as a source for the opencode loader statements.
- I did not run `check_sibling_census.py`, `verify_harness_claims.py`, `check_overlap_levers.py`,
  `fault_injection_corpus.sh` or `verify_dispatch_prompts.py --box-proof`; only the gates in §5, plus the two
  instrument observations in §1.3.
- Whether the L1's in-flight `SKILL.md`/`README.md` edits land as they now stand: unknown; §3.6 gives the
  reconciliation rule and the row variant.
- No install or upgrade was needed this seat, so there is no tooling change to record.

---

## Artifacts

- This report: `.ufo/waves/round-53/falsify/W2ScribeCorrections.md`
- Sandbox (not in the lane): `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53ScribeCorrections/`
  - `clone/` — drafts applied, final commit `99a262d9c3b084822ff3758354ca36be9a135a1b`
  - `pristine/` — `c775d682`, used for the before-comparison
  - `probe-selftest/` — the §6.1 crash reproduction
  - `src/` — the three fetched documents (`claudecode-memory.md`, `codex-agents-md.md`, `opencode-rules.md`)
